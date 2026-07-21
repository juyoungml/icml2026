#!/usr/bin/env python3
"""Build claim-specific validation packets for the ICML 2026 synthesis."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"
PACKET_DIR = REPORTS / "claim_validation_packets"


CLAIM_SPECS = {
    "C01": {
        "theme": "LLM reasoning center of gravity",
        "review_question": "Are the LLM reasoning/post-training papers genuinely central, or are boundary clusters inflating the area?",
        "target": 14,
    },
    "C02": {
        "theme": "Infrastructure and agentic workloads",
        "review_question": "Do systems/efficiency and agents/code overweights reflect real ICML 2026 emphasis rather than classifier artifacts?",
        "target": 14,
    },
    "C03": {
        "theme": "Program committee attention",
        "review_question": "Why do theory and safety/governance receive stronger program signal than public attention?",
        "target": 14,
    },
    "C04": {
        "theme": "Public attention mismatch",
        "review_question": "Is robotics/world-model public attention driven by substantive research artifacts, benchmarks, demos, or hype?",
        "target": 12,
    },
    "C05": {
        "theme": "Neighboring-venue contrast",
        "review_question": "Is multimodal/vision truly underweight versus neighboring venues, or is the aggregate hiding subarea differences?",
        "target": 14,
    },
    "C06": {
        "theme": "External trend context",
        "review_question": "Do fast arXiv-growth areas map to actual ICML 2026 paper themes, or only to broad query terms?",
        "target": 16,
    },
    "C07": {
        "theme": "Artifact visibility",
        "review_question": "Which high-visibility GitHub links appear to be real research artifacts rather than templates, indexes, or project pages?",
        "target": 16,
    },
    "C08": {
        "theme": "Validation priority",
        "review_question": "Which taxonomy boundary clusters most urgently need manual relabeling before publication claims?",
        "target": 18,
    },
}


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


def intish(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def floatish(value: str) -> float:
    try:
        return float(value or 0)
    except ValueError:
        return 0.0


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def compact(value: str, fallback: str = "none") -> str:
    return value.strip() if value and value.strip() else fallback


def score_public(row: dict[str, str]) -> tuple[int, int, str]:
    return (intish(row.get("public_total_votes", "")), intish(row.get("visits_last_7_days", "")), row.get("title", ""))


def score_program(row: dict[str, str]) -> tuple[int, int, int, str]:
    return (
        1 if row.get("award") else 0,
        1 if row.get("is_oral") == "true" else 0,
        intish(row.get("public_total_votes", "")),
        row.get("title", ""),
    )


def add_candidate(
    selected: list[dict[str, str]],
    seen: set[str],
    row: dict[str, str],
    reason: str,
    review_focus: str,
) -> None:
    event_id = row.get("event_id", "")
    if not event_id or event_id in seen:
        return
    copy = dict(row)
    copy["selection_reason"] = reason
    copy["review_focus"] = review_focus
    selected.append(copy)
    seen.add(event_id)


def add_until(
    selected: list[dict[str, str]],
    seen: set[str],
    candidates: list[dict[str, str]],
    target: int,
    reason: str,
    review_focus: str,
) -> None:
    for row in candidates:
        if len(selected) >= target:
            return
        add_candidate(selected, seen, row, reason, review_focus)


def enriched_rows() -> list[dict[str, str]]:
    manual_rows = read_csv(PROCESSED / "icml2026_manual_taxonomy_papers.csv")
    evidence = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_paper_evidence_codes.csv")}
    clusters = {row["semantic_cluster_id"]: row for row in read_csv(PROCESSED / "icml2026_manual_taxonomy_clusters.csv")}
    repro = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_reproducibility_papers.csv")}

    rows = []
    for row in manual_rows:
        ev = evidence.get(row["event_id"], {})
        cluster = clusters.get(row["semantic_cluster_id"], {})
        rp = repro.get(row["event_id"], {})
        rows.append(
            {
                **row,
                "abstract": ev.get("abstract", ""),
                "primary_contribution_type": ev.get("primary_contribution_type", ""),
                "contribution_types": ev.get("contribution_types", ""),
                "method_families": ev.get("method_families", ""),
                "evaluation_settings": ev.get("evaluation_settings", ""),
                "result_claim_types": ev.get("result_claim_types", ""),
                "benchmark_mentions": ev.get("benchmark_mentions", ""),
                "dataset_mentions": ev.get("dataset_mentions", ""),
                "metric_mentions": ev.get("metric_mentions", ""),
                "evidence_confidence": ev.get("evidence_confidence", ""),
                "cluster_review_notes": cluster.get("review_notes", ""),
                "github_repo": rp.get("github_repo", ""),
                "github_stars": rp.get("github_stars", ""),
                "needs_manual_check_reason": rp.get("needs_manual_check_reason", ""),
            }
        )
    return rows


def select_claim_rows(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    by_area: dict[str, list[dict[str, str]]] = defaultdict(list)
    by_cluster: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_area[row["area"]].append(row)
        by_cluster[row["semantic_cluster_id"]].append(row)

    selections: dict[str, list[dict[str, str]]] = {}

    def select_for(claim_id: str) -> tuple[list[dict[str, str]], set[str], int]:
        return [], set(), CLAIM_SPECS[claim_id]["target"]

    selected, seen, target = select_for("C01")
    boundary = [
        row for row in by_area["LLM Reasoning, Post-Training, and RLVR"]
        if row["semantic_cluster_id"] in {"14", "21", "24"} or row["review_status"] == "needs_review"
    ]
    add_until(selected, seen, sorted(boundary, key=score_program, reverse=True), 8, "llm_boundary_cluster", "Check whether this is genuinely LLM reasoning/post-training or a broader LLM/system/safety paper.")
    add_until(selected, seen, sorted(by_area["LLM Reasoning, Post-Training, and RLVR"], key=score_public, reverse=True), target, "llm_high_attention_core", "Check whether high attention supports the center-of-gravity claim.")
    selections["C01"] = selected

    selected, seen, target = select_for("C02")
    systems_agents = by_area["Systems and Efficient Foundation Models"] + by_area["Agents, Code, and Tool Use"]
    add_until(selected, seen, sorted(systems_agents, key=score_program, reverse=True), 7, "systems_agents_program_signal", "Check whether program-selected papers substantiate systems/agents emphasis.")
    add_until(selected, seen, sorted(systems_agents, key=score_public, reverse=True), target, "systems_agents_public_signal", "Check whether public signal reflects core infrastructure/agent workloads or broad LLM spillover.")
    selections["C02"] = selected

    selected, seen, target = select_for("C03")
    theory_safety = by_area["Theory, Optimization, and Algorithms"] + by_area["Safety, Governance, Privacy, and Society"]
    program_low_public = [
        row for row in theory_safety
        if row["is_oral"] == "true" or row.get("award")
    ]
    add_until(selected, seen, sorted(program_low_public, key=score_program, reverse=True), target, "program_high_public_lower", "Identify the technical reason for high program signal and whether public attention misses it.")
    selections["C03"] = selected

    selected, seen, target = select_for("C04")
    robotics = by_area["Robotics, Embodiment, and World Models"]
    non_program = [row for row in robotics if row["is_oral"] != "true" and not row.get("award")]
    add_until(selected, seen, sorted(non_program, key=score_public, reverse=True), 9, "robotics_public_not_program", "Classify the source of public attention: benchmark, demo, artifact, model release, or hype.")
    add_until(selected, seen, sorted(robotics, key=score_program, reverse=True), target, "robotics_program_anchor", "Compare public-heavy robotics papers against program-selected anchors.")
    selections["C04"] = selected

    selected, seen, target = select_for("C05")
    multimodal = by_area["Multimodal, Vision, and Perception"]
    subareas_seen = set()
    for row in sorted(multimodal, key=score_program, reverse=True):
        if row["subarea"] in subareas_seen:
            continue
        add_candidate(selected, seen, row, "multimodal_subarea_anchor", "Check whether each subarea behaves differently from the aggregate underweight claim.")
        subareas_seen.add(row["subarea"])
    add_until(selected, seen, sorted(multimodal, key=score_public, reverse=True), target, "multimodal_high_attention", "Check whether high-attention ICML multimodal papers look more like ICLR/NeurIPS-style vision work or ICML-style ML methods.")
    selections["C05"] = selected

    selected, seen, target = select_for("C06")
    for area in [
        "Multimodal, Vision, and Perception",
        "LLM Reasoning, Post-Training, and RLVR",
        "Safety, Governance, Privacy, and Society",
        "Systems and Efficient Foundation Models",
    ]:
        add_until(selected, seen, sorted(by_area[area], key=score_public, reverse=True), min(target, len(selected) + 4), "fast_arxiv_area_sample", "Check whether broad arXiv-growth terms correspond to the paper's actual contribution.")
    selections["C06"] = selected

    selected, seen, target = select_for("C07")
    artifact_candidates = [row for row in rows if row.get("github_url")]
    manual_check = [row for row in artifact_candidates if row.get("needs_manual_check_reason")]
    add_until(selected, seen, sorted(manual_check, key=lambda r: intish(r.get("github_stars", "")), reverse=True), 7, "artifact_manual_check", "Determine whether the GitHub link is a real paper artifact or a template/index/project page.")
    add_until(selected, seen, sorted(artifact_candidates, key=lambda r: intish(r.get("github_stars", "")), reverse=True), target, "artifact_high_star", "Check artifact type, license/readme quality, and whether reproduction assets are present.")
    selections["C07"] = selected

    selected, seen, target = select_for("C08")
    needs_review = [row for row in rows if row["review_status"] == "needs_review"]
    cluster_seen = set()
    for row in sorted(needs_review, key=score_public, reverse=True):
        if row["semantic_cluster_id"] in cluster_seen:
            continue
        add_candidate(selected, seen, row, "taxonomy_boundary_cluster_anchor", "Decide whether this cluster should remain in the assigned area/subarea or be relabeled.")
        cluster_seen.add(row["semantic_cluster_id"])
        if len(selected) >= 12:
            break
    add_until(selected, seen, sorted(needs_review, key=score_program, reverse=True), target, "taxonomy_boundary_program_public_fill", "Use high-signal papers to stress-test taxonomy boundaries.")
    selections["C08"] = selected

    return selections


def build_queue(selections: dict[str, list[dict[str, str]]]) -> list[dict[str, object]]:
    claims = {row["claim_id"]: row for row in read_csv(PROCESSED / "icml2026_landscape_claim_register.csv")}
    queue = []
    for claim_id, rows in selections.items():
        claim = claims.get(claim_id, {})
        for rank, row in enumerate(rows, start=1):
            queue.append(
                {
                    "claim_id": claim_id,
                    "claim_theme": CLAIM_SPECS[claim_id]["theme"],
                    "claim_statement": claim.get("statement", ""),
                    "claim_strength": claim.get("strength", ""),
                    "claim_review_question": CLAIM_SPECS[claim_id]["review_question"],
                    "claim_review_rank": rank,
                    "selection_reason": row["selection_reason"],
                    "review_focus": row["review_focus"],
                    "event_id": row["event_id"],
                    "title": row["title"],
                    "area": row["area"],
                    "subarea": row["subarea"],
                    "semantic_cluster_id": row["semantic_cluster_id"],
                    "semantic_cluster_label": row["semantic_cluster_label"],
                    "taxonomy_confidence": row["taxonomy_confidence"],
                    "review_status": row["review_status"],
                    "cluster_review_notes": row.get("cluster_review_notes", ""),
                    "is_oral": row["is_oral"],
                    "award": row["award"],
                    "public_total_votes": row["public_total_votes"],
                    "visits_last_7_days": row["visits_last_7_days"],
                    "github_url": row["github_url"],
                    "github_repo": row.get("github_repo", ""),
                    "github_stars": row.get("github_stars", ""),
                    "needs_manual_check_reason": row.get("needs_manual_check_reason", ""),
                    "primary_contribution_type": row.get("primary_contribution_type", ""),
                    "method_families": row.get("method_families", ""),
                    "evaluation_settings": row.get("evaluation_settings", ""),
                    "benchmark_mentions": row.get("benchmark_mentions", ""),
                    "dataset_mentions": row.get("dataset_mentions", ""),
                    "metric_mentions": row.get("metric_mentions", ""),
                    "evidence_confidence": row.get("evidence_confidence", ""),
                    "manual_claim_support": "",
                    "manual_taxonomy_judgment": "",
                    "manual_artifact_judgment": "",
                    "manual_notes": "",
                    "url": row["url"],
                    "alphaxiv_url": row["alphaxiv_url"],
                    "abstract": row.get("abstract", ""),
                }
            )
    return queue


def write_packets(queue: list[dict[str, object]]) -> None:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    by_claim: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in queue:
        by_claim[str(row["claim_id"])].append(row)

    index_lines = [
        "# ICML 2026 Claim Validation Packet Index",
        "",
        "These packets convert the synthesis claim register into paper-level review tasks.",
        "They are designed to answer: what exactly should a researcher read before trusting each landscape claim?",
        "",
        "## Packets",
        "",
    ]

    for claim_id in sorted(by_claim):
        rows = sorted(by_claim[claim_id], key=lambda row: int(row["claim_review_rank"]))
        spec = CLAIM_SPECS[claim_id]
        reason_counts = Counter(str(row["selection_reason"]) for row in rows)
        path = PACKET_DIR / f"{claim_id.lower()}-{slugify(spec['theme'])}.md"
        lines = [
            f"# {claim_id}: {spec['theme']}",
            "",
            f"Review question: {spec['review_question']}",
            "",
            "## Queue Summary",
            "",
            f"- Papers: {len(rows)}",
            f"- Selection mix: {', '.join(f'{k}={v}' for k, v in reason_counts.most_common())}",
            f"- Oral/award papers: {sum(row['is_oral'] == 'true' or bool(row['award']) for row in rows)}",
            f"- Taxonomy-review papers: {sum(row['review_status'] == 'needs_review' for row in rows)}",
            f"- GitHub-linked papers: {sum(bool(row['github_url']) for row in rows)}",
            "",
            "## Papers",
            "",
        ]
        for row in rows:
            flags = [str(row["selection_reason"])]
            if row["is_oral"] == "true":
                flags.append("oral")
            if row["award"]:
                flags.append(str(row["award"]))
            if row["review_status"] == "needs_review":
                flags.append("taxonomy-review")
            if row["github_url"]:
                flags.append("github")
            lines.extend(
                [
                    f"### {row['claim_review_rank']}. {row['title']}",
                    "",
                    f"Flags: {', '.join(flags)}",
                    "",
                    f"- Review focus: {row['review_focus']}",
                    f"- Area/subarea: {row['area']} / {row['subarea']}",
                    f"- Cluster: {row['semantic_cluster_id']} - {row['semantic_cluster_label']}",
                    f"- Cluster review: {compact(str(row['review_status']))}; {compact(str(row['cluster_review_notes']))}",
                    f"- Program/public: oral={row['is_oral']}; award={compact(str(row['award']))}; votes={row['public_total_votes']}; 7d visits={row['visits_last_7_days']}",
                    f"- Artifact: {compact(str(row['github_url']))}; stars={compact(str(row['github_stars']))}; manual-check={compact(str(row['needs_manual_check_reason']))}",
                    f"- Evidence tags: contribution={compact(str(row['primary_contribution_type']))}; methods={compact(str(row['method_families']))}; eval={compact(str(row['evaluation_settings']))}",
                    f"- Benchmark/data/metric cues: {compact(str(row['benchmark_mentions']))} / {compact(str(row['dataset_mentions']))} / {compact(str(row['metric_mentions']))}",
                    f"- ICML URL: {compact(str(row['url']))}",
                    f"- AlphaXiv URL: {compact(str(row['alphaxiv_url']))}",
                    "",
                    "Abstract:",
                    "",
                    compact(str(row["abstract"]), "No abstract available."),
                    "",
                    "Manual review:",
                    "- [ ] Claim support checked",
                    "- [ ] Taxonomy judgment checked",
                    "- [ ] Artifact judgment checked, if applicable",
                    "- Claim support:",
                    "- Taxonomy judgment:",
                    "- Artifact judgment:",
                    "- Notes:",
                    "",
                ]
            )
        path.write_text("\n".join(lines), encoding="utf-8")
        index_lines.append(f"- [{claim_id}: {spec['theme']}](claim_validation_packets/{path.name}) - {len(rows)} papers")

    index_lines.extend(
        [
            "",
            "## Review Guidance",
            "",
            "- Mark whether each paper supports, weakens, or is irrelevant to the associated synthesis claim.",
            "- For boundary clusters, record whether the area/subarea should change.",
            "- For artifact claims, distinguish runnable code, benchmark/data release, project page, template/index, and unavailable links.",
            "- After review, copy checked judgments into `data/processed/icml2026_claim_validation_queue.csv` or a reviewed derivative.",
        ]
    )
    (REPORTS / "icml2026_claim_validation_packet_index.md").write_text("\n".join(index_lines), encoding="utf-8")


def write_report(queue: list[dict[str, object]]) -> None:
    claim_counts = Counter(str(row["claim_id"]) for row in queue)
    reason_counts = Counter(str(row["selection_reason"]) for row in queue)
    lines = [
        "# ICML 2026 Claim Validation Queue",
        "",
        "This queue turns the landscape synthesis claim register into concrete paper-level review tasks.",
        "",
        "## Snapshot",
        "",
        f"- Queue rows: {len(queue):,}",
        f"- Claims covered: {len(claim_counts):,}",
        f"- Oral/award rows: {sum(row['is_oral'] == 'true' or bool(row['award']) for row in queue):,}",
        f"- Taxonomy-review rows: {sum(row['review_status'] == 'needs_review' for row in queue):,}",
        f"- GitHub-linked rows: {sum(bool(row['github_url']) for row in queue):,}",
        "",
        "## Claim Coverage",
        "",
    ]
    for claim_id in sorted(claim_counts):
        lines.append(f"- {claim_id} - {CLAIM_SPECS[claim_id]['theme']}: {claim_counts[claim_id]} papers")
    lines.extend(["", "## Selection Reasons", ""])
    for reason, count in reason_counts.most_common():
        lines.append(f"- {reason}: {count}")
    lines.extend(
        [
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_claim_validation_queue.csv`",
            "- `reports/icml2026_claim_validation_packet_index.md`",
            "- `reports/claim_validation_packets/*.md`",
            "",
            "## Caveats",
            "",
            "- This is a review workflow artifact. Blank manual fields mean the claim has not been validated yet.",
            "- Paper selections are designed for high-yield review, not statistical representativeness.",
            "- Claim validation should be reconciled back into the claim register before publication or presentation.",
        ]
    )
    (REPORTS / "icml2026_claim_validation_queue.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    rows = enriched_rows()
    selections = select_claim_rows(rows)
    queue = build_queue(selections)
    write_csv(
        PROCESSED / "icml2026_claim_validation_queue.csv",
        queue,
        [
            "claim_id", "claim_theme", "claim_statement", "claim_strength", "claim_review_question",
            "claim_review_rank", "selection_reason", "review_focus", "event_id", "title",
            "area", "subarea", "semantic_cluster_id", "semantic_cluster_label",
            "taxonomy_confidence", "review_status", "cluster_review_notes", "is_oral",
            "award", "public_total_votes", "visits_last_7_days", "github_url", "github_repo",
            "github_stars", "needs_manual_check_reason", "primary_contribution_type",
            "method_families", "evaluation_settings", "benchmark_mentions", "dataset_mentions",
            "metric_mentions", "evidence_confidence", "manual_claim_support",
            "manual_taxonomy_judgment", "manual_artifact_judgment", "manual_notes",
            "url", "alphaxiv_url", "abstract",
        ],
    )
    write_packets(queue)
    write_report(queue)
    print(f"Wrote {PROCESSED / 'icml2026_claim_validation_queue.csv'} ({len(queue)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_claim_validation_queue.md'}")
    print(f"Wrote {REPORTS / 'icml2026_claim_validation_packet_index.md'}")
    print(f"Wrote {len(CLAIM_SPECS)} claim validation packets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
