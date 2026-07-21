#!/usr/bin/env python3
"""Build per-area briefing cards for researcher navigation."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"
BRIEF_DIR = REPORTS / "area_briefing_cards"


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


def pct(value: str) -> str:
    return f"{fnum(value) * 100:.1f}%"


def pp(value: str) -> str:
    return f"{fnum(value) * 100:+.1f} pp"


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def split_items(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split(" | ") if part.strip()]


def top(rows: list[dict[str, str]], key, limit: int) -> list[dict[str, str]]:
    return sorted(rows, key=key, reverse=True)[:limit]


def score_program(row: dict[str, str]) -> tuple[int, int, int, int, str]:
    return (
        1 if row.get("award") else 0,
        1 if row.get("is_oral") == "true" else 0,
        inum(row.get("public_total_votes", "")),
        inum(row.get("github_stars", "")),
        row.get("title", ""),
    )


def score_public(row: dict[str, str]) -> tuple[int, int, int, str]:
    return (
        inum(row.get("public_total_votes", "")),
        inum(row.get("visits_last_7_days", "")),
        inum(row.get("github_stars", "")),
        row.get("title", ""),
    )


def score_artifact(row: dict[str, str]) -> tuple[int, int, int, str]:
    return (
        1 if row.get("github_url") else 0,
        inum(row.get("github_stars", "")),
        inum(row.get("public_total_votes", "")),
        row.get("title", ""),
    )


def paper_line(row: dict[str, str]) -> str:
    flags = []
    if row.get("award"):
        flags.append(row["award"])
    if row.get("is_oral") == "true":
        flags.append("oral")
    if row.get("public_total_votes"):
        flags.append(f"votes={row['public_total_votes']}")
    if row.get("github_url"):
        flags.append(f"github_stars={row.get('github_stars') or '0'}")
    if row.get("review_status") == "needs_review":
        flags.append("taxonomy-review")
    return f"{row['title']} ({'; '.join(flags)})"


def trust_readout(signal: dict[str, str], fault: dict[str, str], area_rows: list[dict[str, str]]) -> tuple[str, str]:
    risk_reasons = []
    if inum(fault.get("clusters_needing_review", "")):
        risk_reasons.append(f"{fault['clusters_needing_review']} taxonomy clusters need review")
    if fnum(signal.get("public_attention_enrichment", "")) >= 1.2 and fnum(signal.get("oral_enrichment", "")) < 1.0:
        risk_reasons.append("public attention exceeds program signal")
    if fnum(signal.get("oral_enrichment", "")) >= 1.2 and fnum(signal.get("public_attention_enrichment", "")) < 0.8:
        risk_reasons.append("program signal exceeds public attention")
    if abs(fnum(signal.get("historical_delta_vs_baseline", ""))) >= 0.015:
        risk_reasons.append("historical baseline contrast is material")
    low_conf = sum(row.get("evidence_confidence") in {"low", "very_low"} for row in area_rows)
    if low_conf:
        risk_reasons.append(f"{low_conf} low-confidence evidence-code rows in full area")
    if not risk_reasons:
        return "usable_for_orientation", "Area-level orientation is reasonably stable, but paper-level claims still need review."
    if len(risk_reasons) >= 3 or inum(fault.get("clusters_needing_review", "")) >= 3:
        return "high_review_need", "; ".join(risk_reasons)
    return "moderate_review_need", "; ".join(risk_reasons)


def build_area_rows() -> list[dict[str, object]]:
    signals = {row["area"]: row for row in read_csv(PROCESSED / "icml2026_landscape_signal_matrix.csv")}
    fault_lines = {row["area"]: row for row in read_csv(PROCESSED / "icml2026_area_fault_lines.csv")}
    papers = read_csv(PROCESSED / "icml2026_paper_explorer.csv")
    review_progress = {
        row["group"]: row
        for row in read_csv(PROCESSED / "manual_review_progress.csv")
        if row["queue_type"] == "area_validation"
    }

    by_area: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in papers:
        by_area[row["area"]].append(row)

    out: list[dict[str, object]] = []
    for area, signal in signals.items():
        fault = fault_lines[area]
        rows = by_area[area]
        program_papers = top(rows, score_program, 6)
        public_non_program = top(
            [row for row in rows if row.get("is_oral") != "true" and not row.get("award")],
            score_public,
            6,
        )
        artifact_papers = top([row for row in rows if row.get("github_url")], score_artifact, 5)
        boundary_papers = top([row for row in rows if row.get("review_status") == "needs_review"], score_public, 5)
        trust_tier, trust_reason = trust_readout(signal, fault, rows)
        progress = review_progress.get(area, {})
        out.append(
            {
                "area": area,
                "brief_path": f"reports/area_briefing_cards/{slugify(area)}.md",
                "trust_tier": trust_tier,
                "trust_reason": trust_reason,
                "paper_count": inum(signal["taxonomy_papers"]),
                "taxonomy_share": signal["taxonomy_share"],
                "oral_enrichment": signal["oral_enrichment"],
                "public_attention_enrichment": signal["public_attention_enrichment"],
                "historical_delta_vs_baseline": signal["historical_delta_vs_baseline"],
                "github_url_share": signal["github_url_share"],
                "review_rows": progress.get("review_rows", "0"),
                "reviewed_rows": progress.get("reviewed_rows", "0"),
                "remaining_rows": progress.get("remaining_rows", "0"),
                "headline": fault["headline"],
                "fault_lines": fault["fault_lines"],
                "read_for": fault["read_for"],
                "top_subareas": fault["top_subareas"],
                "top_methods": fault["top_method_families"],
                "top_evaluations": fault["top_evaluation_settings"],
                "program_papers": " | ".join(row["title"] for row in program_papers),
                "public_non_program_papers": " | ".join(row["title"] for row in public_non_program),
                "artifact_papers": " | ".join(row["title"] for row in artifact_papers),
                "boundary_papers": " | ".join(row["title"] for row in boundary_papers),
            }
        )
    out.sort(key=lambda row: (-float(row["taxonomy_share"]), str(row["area"])))
    return out


def write_area_card(row: dict[str, object]) -> None:
    area = str(row["area"])
    signal = row
    fault_lines = split_items(str(row["fault_lines"]))
    read_for = split_items(str(row["read_for"]))
    path = BRIEF_DIR / f"{slugify(area)}.md"

    papers = read_csv(PROCESSED / "icml2026_paper_explorer.csv")
    area_papers = [paper for paper in papers if paper["area"] == area]
    program_papers = top(area_papers, score_program, 8)
    public_non_program = top(
        [paper for paper in area_papers if paper.get("is_oral") != "true" and not paper.get("award")],
        score_public,
        6,
    )
    artifact_papers = top([paper for paper in area_papers if paper.get("github_url")], score_artifact, 6)
    boundary_papers = top([paper for paper in area_papers if paper.get("review_status") == "needs_review"], score_public, 6)
    evidence_conf = Counter(paper.get("evidence_confidence", "") for paper in area_papers)
    contribution_mix = Counter(paper.get("primary_contribution_type", "") for paper in area_papers)

    lines = [
        f"# {area}",
        "",
        str(row["headline"]),
        "",
        "## Signal Snapshot",
        "",
        f"- Papers: {row['paper_count']:,} ({pct(str(signal['taxonomy_share']))} of corpus)",
        f"- Oral enrichment: {float(signal['oral_enrichment']):.2f}x",
        f"- Public-attention enrichment: {float(signal['public_attention_enrichment']):.2f}x",
        f"- Historical accepted-paper delta: {pp(str(signal['historical_delta_vs_baseline']))}",
        f"- GitHub URL share: {pct(str(signal['github_url_share']))}",
        f"- Manual area-review progress: {row['reviewed_rows']}/{row['review_rows']} rows reviewed; {row['remaining_rows']} remaining",
        f"- Trust tier: `{row['trust_tier']}` - {row['trust_reason']}",
        "",
        "## Fault Lines",
        "",
    ]
    for item in fault_lines:
        lines.append(f"- {item}")

    lines.extend(["", "## Read For", ""])
    for item in read_for:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## Shape Of The Area",
            "",
            f"- Top subareas: {row['top_subareas']}",
            f"- Method-family cues: {row['top_methods']}",
            f"- Evaluation-setting cues: {row['top_evaluations']}",
            "- Contribution mix: " + "; ".join(f"{name or 'Uncoded'} ({count})" for name, count in contribution_mix.most_common(8)),
            "- Evidence confidence: " + "; ".join(f"{name or 'blank'} ({count})" for name, count in evidence_conf.most_common()),
            "",
            "## Start Here",
            "",
        ]
    )
    for paper in program_papers[:6]:
        lines.append(f"- {paper_line(paper)}")

    lines.extend(["", "## Public Attention Not Program-Selected", ""])
    for paper in public_non_program:
        lines.append(f"- {paper_line(paper)}")

    lines.extend(["", "## Artifact-Visible Papers To Inspect", ""])
    for paper in artifact_papers:
        caveat = " manual-check" if paper.get("needs_manual_check_reason") else ""
        lines.append(f"- {paper_line(paper)}{caveat}")

    lines.extend(["", "## Boundary / Taxonomy Review Candidates", ""])
    if boundary_papers:
        for paper in boundary_papers:
            lines.append(f"- {paper_line(paper)}")
    else:
        lines.append("- No high-signal `needs_review` papers in this area briefing sample.")

    lines.extend(
        [
            "",
            "## What Could Break This Area Story",
            "",
            "- The area taxonomy is generated from semantic clusters and curated mappings, not full manual paper reading.",
            "- Public attention is AlphaXiv attention; it can reflect sharing dynamics rather than technical importance.",
            "- GitHub URL share is artifact visibility, not runnable reproducibility.",
            "- Evidence-code labels are heuristic and should be checked against the paper before making benchmark, dataset, metric, or result-character claims.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_index(rows: list[dict[str, object]]) -> None:
    lines = [
        "# ICML 2026 Area Briefing Cards",
        "",
        "Compact per-area guides for researchers who want to understand one ICML 2026 landscape slice quickly.",
        "These cards summarize signals, fault lines, papers to read first, public/program divergence, artifact-visible papers, and caveats.",
        "",
        "## Index",
        "",
        "| Area | Papers | Trust Tier | Manual Review | Key Signals | Card |",
        "| --- | ---: | --- | ---: | --- | --- |",
    ]
    for row in rows:
        rel = Path(str(row["brief_path"])).relative_to("reports")
        signals = (
            f"oral {float(row['oral_enrichment']):.2f}x; "
            f"public {float(row['public_attention_enrichment']):.2f}x; "
            f"delta {pp(str(row['historical_delta_vs_baseline']))}"
        )
        lines.append(
            f"| {row['area']} | {row['paper_count']} | {row['trust_tier']} | "
            f"{row['reviewed_rows']}/{row['review_rows']} | {signals} | [open]({rel}) |"
        )
    lines.extend(
        [
            "",
            "## Use Notes",
            "",
            "- Use the cards to choose what to read, not as final literature-review prose.",
            "- Start with areas marked `high_review_need` if the report thesis relies on them.",
            "- Fill the area validation packets before making subarea-level or benchmark/dataset claims.",
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_area_briefing_cards.csv`",
            "- `reports/icml2026_area_briefing_card_index.md`",
            "- `reports/area_briefing_cards/*.md`",
        ]
    )
    (REPORTS / "icml2026_area_briefing_card_index.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    BRIEF_DIR.mkdir(parents=True, exist_ok=True)
    for path in BRIEF_DIR.glob("*.md"):
        path.unlink()
    rows = build_area_rows()
    write_csv(
        PROCESSED / "icml2026_area_briefing_cards.csv",
        rows,
        [
            "area", "brief_path", "trust_tier", "trust_reason", "paper_count", "taxonomy_share",
            "oral_enrichment", "public_attention_enrichment", "historical_delta_vs_baseline",
            "github_url_share", "review_rows", "reviewed_rows", "remaining_rows", "headline",
            "fault_lines", "read_for", "top_subareas", "top_methods", "top_evaluations",
            "program_papers", "public_non_program_papers", "artifact_papers", "boundary_papers",
        ],
    )
    for row in rows:
        write_area_card(row)
    write_index(rows)
    print(f"Wrote {PROCESSED / 'icml2026_area_briefing_cards.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_area_briefing_card_index.md'}")
    print(f"Wrote {BRIEF_DIR} ({len(list(BRIEF_DIR.glob('*.md')))} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
