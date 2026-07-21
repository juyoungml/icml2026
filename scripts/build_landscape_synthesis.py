#!/usr/bin/env python3
"""Build a researcher-facing synthesis and claim register for ICML 2026."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"Missing required input: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def fnum(value: str) -> float:
    try:
        return float(value or 0)
    except ValueError:
        return 0.0


def inum(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def pct(value: float) -> str:
    return f"{value * 100:.1f}%"


def pp(value: float) -> str:
    return f"{value * 100:+.1f} pp"


def load_by(key: str, rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {row[key]: row for row in rows}


def reproducibility_by_area() -> dict[str, dict[str, object]]:
    taxonomy_rows = read_csv(PROCESSED / "icml2026_manual_taxonomy_papers.csv")
    repro_rows = read_csv(PROCESSED / "icml2026_reproducibility_papers.csv")
    repro_by_event = {row["event_id"]: row for row in repro_rows}
    grouped: dict[str, dict[str, int]] = {}
    for row in taxonomy_rows:
        area = row["area"]
        repro = repro_by_event.get(row["event_id"], {})
        grouped.setdefault(area, {"paper_count": 0, "github_url_count": 0, "likely_code_count": 0, "manual_check_count": 0})
        grouped[area]["paper_count"] += 1
        has_github = repro.get("has_github_url") == "true" or bool(repro.get("github_url"))
        needs_manual = bool(repro.get("needs_manual_check_reason"))
        if has_github:
            grouped[area]["github_url_count"] += 1
        if has_github and not needs_manual:
            grouped[area]["likely_code_count"] += 1
        if needs_manual:
            grouped[area]["manual_check_count"] += 1
    output: dict[str, dict[str, object]] = {}
    for area, counts in grouped.items():
        total = max(1, counts["paper_count"])
        output[area] = {
            **counts,
            "github_url_share": round(counts["github_url_count"] / total, 4),
            "likely_code_share": round(counts["likely_code_count"] / total, 4),
            "manual_check_share": round(counts["manual_check_count"] / total, 4),
        }
    return output


def top_rows(rows: list[dict[str, object]], key: str, limit: int = 5, reverse: bool = True) -> list[dict[str, object]]:
    return sorted(rows, key=lambda row: float(row[key]), reverse=reverse)[:limit]


def make_signal_matrix() -> list[dict[str, object]]:
    areas = load_by("area", read_csv(PROCESSED / "icml2026_manual_taxonomy_areas.csv"))
    program = load_by("group", read_csv(PROCESSED / "icml2026_area_program_calibration.csv"))
    arxiv = load_by("area", read_csv(PROCESSED / "arxiv_taxonomy_trend_summary.csv"))
    historical = load_by("area", read_csv(PROCESSED / "historical_venue_delta_summary.csv"))
    evidence = load_by("area", read_csv(PROCESSED / "icml2026_area_evidence_summary.csv"))
    reproducibility = reproducibility_by_area()

    rows: list[dict[str, object]] = []
    for area, area_row in areas.items():
        p = program.get(area, {})
        a = arxiv.get(area, {})
        h = historical.get(area, {})
        e = evidence.get(area, {})
        r = reproducibility.get(area, {})
        paper_share = fnum(area_row.get("share", ""))
        oral_enrichment = fnum(p.get("oral_enrichment", ""))
        public_enrichment = fnum(p.get("public_attention_enrichment", ""))
        arxiv_growth = fnum(a.get("growth_2025_vs_2024", ""))
        venue_delta = fnum(h.get("delta_vs_baseline_avg", ""))
        github_share = fnum(str(r.get("github_url_share", e.get("github_url_share", area_row.get("github_url_share", "")))))
        benchmark_share = fnum(e.get("benchmark_mention_share", ""))
        signal_tags = []
        if paper_share >= 0.10:
            signal_tags.append("large_area")
        if oral_enrichment >= 1.2:
            signal_tags.append("program_overweight")
        if public_enrichment >= 1.2:
            signal_tags.append("public_overweight")
        if venue_delta >= 0.015:
            signal_tags.append("venue_overweight")
        if venue_delta <= -0.015:
            signal_tags.append("venue_underweight")
        if arxiv_growth >= 0.50:
            signal_tags.append("fast_arxiv_growth")
        if github_share >= 0.30:
            signal_tags.append("high_artifact_visibility")
        if benchmark_share >= 0.12:
            signal_tags.append("benchmark_heavy")
        rows.append(
            {
                "area": area,
                "taxonomy_papers": inum(area_row.get("paper_count", "")),
                "taxonomy_share": round(paper_share, 4),
                "oral_enrichment": oral_enrichment,
                "award_count": inum(area_row.get("award_count", "")),
                "public_attention_enrichment": public_enrichment,
                "votes_per_paper": fnum(area_row.get("votes_per_paper", "")),
                "historical_delta_vs_baseline": round(venue_delta, 4),
                "historical_relative_to_baseline": h.get("relative_to_baseline_avg", ""),
                "arxiv_2025_vs_2024_growth": round(arxiv_growth, 4),
                "github_url_share": round(github_share, 4),
                "benchmark_mention_share": round(benchmark_share, 4),
                "metric_mention_share": round(fnum(e.get("metric_mention_share", "")), 4),
                "likely_code_share": r.get("likely_code_share", ""),
                "manual_check_artifact_share": r.get("manual_check_share", ""),
                "signal_tags": "; ".join(signal_tags),
                "representative_papers": area_row.get("representative_papers", ""),
            }
        )
    rows.sort(key=lambda row: (-float(row["taxonomy_share"]), str(row["area"])))
    return rows


def claim(claim_id: str, theme: str, statement: str, evidence: str, strength: str, caveats: str, next_validation: str) -> dict[str, str]:
    return {
        "claim_id": claim_id,
        "theme": theme,
        "statement": statement,
        "evidence": evidence,
        "strength": strength,
        "caveats": caveats,
        "next_validation": next_validation,
    }


def build_claims(matrix: list[dict[str, object]]) -> list[dict[str, str]]:
    by_area = {str(row["area"]): row for row in matrix}
    claims: list[dict[str, str]] = []

    llm = by_area["LLM Reasoning, Post-Training, and RLVR"]
    claims.append(
        claim(
            "C01",
            "LLM reasoning center of gravity",
            "LLM reasoning/post-training is the largest ICML 2026 area and is also overweight relative to nearby accepted-paper baselines.",
            f"{llm['taxonomy_papers']} taxonomy papers ({pct(float(llm['taxonomy_share']))}); "
            f"historical delta {pp(float(llm['historical_delta_vs_baseline']))}; "
            f"public-attention enrichment {float(llm['public_attention_enrichment']):.2f}x.",
            "strong_for_landscape",
            "Area boundaries include general LLM training/evaluation and some diffusion-language papers; paper-level taxonomy still needs review.",
            "Manually inspect boundary clusters 14, 21, and 24 before making subarea-level claims.",
        )
    )

    systems = by_area["Systems and Efficient Foundation Models"]
    agents = by_area["Agents, Code, and Tool Use"]
    claims.append(
        claim(
            "C02",
            "Infrastructure and agentic workloads",
            "Systems/efficiency and agents/code look smaller than LLM reasoning by paper count, but both are clear ICML 2026 overweights versus the neighboring-venue baseline.",
            f"Systems historical delta {pp(float(systems['historical_delta_vs_baseline']))}, relative {systems['historical_relative_to_baseline']}x; "
            f"Agents historical delta {pp(float(agents['historical_delta_vs_baseline']))}, relative {agents['historical_relative_to_baseline']}x.",
            "moderate_to_strong",
            "Historical comparison uses a keyword scorer; ICML 2025 and NeurIPS 2025 lack static abstracts in the current pull.",
            "Read top positive-delta papers and check whether deltas reflect real venue emphasis or metadata/topic-label differences.",
        )
    )

    safety = by_area["Safety, Governance, Privacy, and Society"]
    theory = by_area["Theory, Optimization, and Algorithms"]
    claims.append(
        claim(
            "C03",
            "Program committee attention",
            "Theory and safety/governance receive more program signal than their public-attention signal would predict.",
            f"Theory oral enrichment {float(theory['oral_enrichment']):.2f}x vs public enrichment {float(theory['public_attention_enrichment']):.2f}x; "
            f"Safety oral enrichment {float(safety['oral_enrichment']):.2f}x and {safety['award_count']} awards vs public enrichment {float(safety['public_attention_enrichment']):.2f}x.",
            "strong_for_triage",
            "Oral/award counts are program signals, not full quality labels; award counts are small and volatile.",
            "Review low-public/high-program papers to extract the technical reasons for committee interest.",
        )
    )

    robotics = by_area["Robotics, Embodiment, and World Models"]
    claims.append(
        claim(
            "C04",
            "Public attention mismatch",
            "Robotics/embodiment is small by taxonomy count but unusually strong in public attention.",
            f"{robotics['taxonomy_papers']} papers ({pct(float(robotics['taxonomy_share']))}); "
            f"public-attention enrichment {float(robotics['public_attention_enrichment']):.2f}x vs oral enrichment {float(robotics['oral_enrichment']):.2f}x.",
            "moderate",
            "AlphaXiv likely overweights shareable VLA/world-model work and project-page traffic.",
            "Inspect whether the high-attention papers are benchmarks, demos, or reusable models rather than core ICML program emphasis.",
        )
    )

    multimodal = by_area["Multimodal, Vision, and Perception"]
    claims.append(
        claim(
            "C05",
            "Neighboring-venue contrast",
            "Multimodal/vision is large inside ICML 2026 but underweight relative to NeurIPS 2025 and ICLR 2026 accepted-paper baselines.",
            f"{multimodal['taxonomy_papers']} taxonomy papers ({pct(float(multimodal['taxonomy_share']))}); "
            f"historical delta {pp(float(multimodal['historical_delta_vs_baseline']))}, relative {multimodal['historical_relative_to_baseline']}x.",
            "moderate",
            "This is the area most sensitive to venue scope and title/topic classification; ICLR/NeurIPS vision-heavy shares may dominate the baseline average.",
            "Break multimodal into vision-language reasoning, video, 3D, and robustness before interpreting the aggregate underweight.",
        )
    )

    fast_arxiv = top_rows(matrix, "arxiv_2025_vs_2024_growth", 4)
    claims.append(
        claim(
            "C06",
            "External trend context",
            "The fastest broad arXiv growth areas are multimodal/vision, LLM reasoning, and safety/governance, but ICML 2026 does not mirror this ranking exactly.",
            "; ".join(f"{row['area']}: {pct(float(row['arxiv_2025_vs_2024_growth']))}" for row in fast_arxiv),
            "context_only",
            "arXiv queries are broad, overlapping, and not acceptance or quality signals.",
            "Use accepted-paper corpora, not arXiv counts, for publication-ready year-over-year venue claims.",
        )
    )

    artifact_rows = top_rows(matrix, "github_url_share", 4)
    claims.append(
        claim(
            "C07",
            "Artifact visibility",
            "Artifacts are most visible in agents/code, LLM reasoning, systems, and multimodal/vision, while theory remains much less artifact-linked.",
            "; ".join(f"{row['area']}: GitHub URL share {pct(float(row['github_url_share']))}" for row in artifact_rows),
            "moderate",
            "GitHub metadata comes from AlphaXiv and does not prove runnable reproduction; some high-star links are templates or index repos.",
            "Clone/check high-signal repositories and separate code, benchmark, dataset, checkpoint, and project-page links.",
        )
    )

    claims.append(
        claim(
            "C08",
            "Validation priority",
            "The biggest remaining quality jump is not more plotting; it is paper-level validation of boundary clusters and high-impact claims.",
            "21 of 42 semantic clusters are marked needs_review; validation queue contains 192 papers across 12 areas.",
            "process_claim",
            "The queue organizes review but does not mean evidence fields have been checked.",
            "Fill validation packets and reconcile reviewed fields back into a checked CSV.",
        )
    )
    return claims


def write_report(matrix: list[dict[str, object]], claims: list[dict[str, str]]) -> None:
    largest = top_rows(matrix, "taxonomy_share", 5)
    program = top_rows(matrix, "oral_enrichment", 5)
    public = top_rows(matrix, "public_attention_enrichment", 5)
    venue = top_rows(matrix, "historical_delta_vs_baseline", 5)
    arxiv = top_rows(matrix, "arxiv_2025_vs_2024_growth", 5)
    artifacts = top_rows(matrix, "github_url_share", 5)

    lines = [
        "# ICML 2026 Landscape Synthesis",
        "",
        "This is the researcher-facing synthesis layer: a claim register plus the strongest cross-source signals from the ICML 2026 EDA workspace.",
        "It is designed to be read before the longer area reports and validation packets.",
        "",
        "## Fast Read",
        "",
    ]
    for item in claims[:5]:
        lines.append(f"- **{item['theme']}**: {item['statement']} Evidence: {item['evidence']}")

    lines.extend(
        [
            "",
            "## Signal Matrix Highlights",
            "",
            "### Largest ICML 2026 Taxonomy Areas",
        ]
    )
    for row in largest:
        lines.append(
            f"- {row['area']}: {row['taxonomy_papers']} papers ({pct(float(row['taxonomy_share']))}); "
            f"votes/paper {float(row['votes_per_paper']):.2f}; tags: {row['signal_tags']}"
        )

    lines.append("")
    lines.append("### Highest Program-Signal Enrichment")
    for row in program:
        lines.append(f"- {row['area']}: oral enrichment {float(row['oral_enrichment']):.2f}x; awards {row['award_count']}; public enrichment {float(row['public_attention_enrichment']):.2f}x")

    lines.append("")
    lines.append("### Highest Public-Attention Enrichment")
    for row in public:
        lines.append(f"- {row['area']}: public enrichment {float(row['public_attention_enrichment']):.2f}x; oral enrichment {float(row['oral_enrichment']):.2f}x; votes/paper {float(row['votes_per_paper']):.2f}")

    lines.append("")
    lines.append("### ICML 2026 Overweights vs Accepted-Paper Baseline")
    for row in venue:
        lines.append(f"- {row['area']}: {pp(float(row['historical_delta_vs_baseline']))}; relative {row['historical_relative_to_baseline']}x")

    lines.append("")
    lines.append("### Fastest arXiv Query Growth")
    for row in arxiv:
        lines.append(f"- {row['area']}: 2025 vs 2024 growth {pct(float(row['arxiv_2025_vs_2024_growth']))}")

    lines.append("")
    lines.append("### Highest Artifact Visibility")
    for row in artifacts:
        lines.append(f"- {row['area']}: GitHub URL share {pct(float(row['github_url_share']))}; likely-code share {pct(float(row['likely_code_share']))}")

    lines.extend(
        [
            "",
            "## Claim Register",
            "",
            "| Claim | Strength | Evidence | Caveat | Next validation |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in claims:
        lines.append(
            f"| {item['claim_id']}: {item['theme']} | {item['strength']} | {item['evidence']} | {item['caveats']} | {item['next_validation']} |"
        )

    lines.extend(
        [
            "",
            "## How To Use This",
            "",
            "- Use `data/processed/icml2026_landscape_signal_matrix.csv` for sorting/filtering areas by signal type.",
            "- Use `data/processed/icml2026_landscape_claim_register.csv` as the backbone for a report outline or slide narrative.",
            "- Use `reports/icml2026_claim_validation_packet_index.md` to review the paper-level evidence behind each major claim.",
            "- Treat claims marked `context_only`, `moderate`, or `process_claim` as prompts for manual review, not final assertions.",
            "",
            "## Caveats",
            "",
            "- The 12-area taxonomy is a curated seed over semantic clusters; several clusters remain marked `needs_review`.",
            "- Historical accepted-paper deltas use a shared keyword scorer, not the semantic-cluster taxonomy.",
            "- arXiv trends are broad query-count context, not venue acceptance trends.",
            "- AlphaXiv votes and GitHub metadata are public-attention/artifact proxies, not quality or reproducibility proof.",
            "- Program signal means oral/award selection only; it does not capture reviewer scores or full committee deliberation.",
        ]
    )
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "icml2026_landscape_synthesis.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    matrix = make_signal_matrix()
    claims = build_claims(matrix)
    write_csv(
        PROCESSED / "icml2026_landscape_signal_matrix.csv",
        matrix,
        [
            "area", "taxonomy_papers", "taxonomy_share", "oral_enrichment", "award_count",
            "public_attention_enrichment", "votes_per_paper", "historical_delta_vs_baseline",
            "historical_relative_to_baseline", "arxiv_2025_vs_2024_growth", "github_url_share",
            "benchmark_mention_share", "metric_mention_share", "likely_code_share",
            "manual_check_artifact_share", "signal_tags", "representative_papers",
        ],
    )
    write_csv(
        PROCESSED / "icml2026_landscape_claim_register.csv",
        claims,
        ["claim_id", "theme", "statement", "evidence", "strength", "caveats", "next_validation"],
    )
    write_report(matrix, claims)
    print(f"Wrote {PROCESSED / 'icml2026_landscape_signal_matrix.csv'} ({len(matrix)} rows)")
    print(f"Wrote {PROCESSED / 'icml2026_landscape_claim_register.csv'} ({len(claims)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_landscape_synthesis.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
