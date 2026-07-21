#!/usr/bin/env python3
"""Build a focused taxonomy-boundary adjudication queue for ICML 2026."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
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


def intish(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def fnum(value: str) -> float:
    try:
        return float(value or 0)
    except ValueError:
        return 0.0


def split_titles(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split("|") if part.strip()]


def decision_prompt(row: dict[str, str]) -> str:
    notes = row.get("review_notes", "")
    confidence = row.get("taxonomy_confidence", "")
    if "split across lexical clusters" in notes:
        return "Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood."
    if confidence != "high":
        return "Decide whether current area/subarea is central enough or should be relabeled."
    if intish(row.get("paper_count", "")) < 75:
        return "Small cluster: decide whether to merge into a broader subarea or keep as distinct."
    return "Spot-check representative papers and confirm the current area/subarea label."


def priority_score(row: dict[str, str], queued_papers: int) -> float:
    score = 0.0
    score += queued_papers * 4
    score += intish(row.get("oral_count", "")) * 3
    score += intish(row.get("award_count", "")) * 6
    score += min(fnum(row.get("votes_per_paper", "")), 30)
    if row.get("taxonomy_confidence") != "high":
        score += 10
    if "split across lexical clusters" in row.get("review_notes", ""):
        score += 8
    if intish(row.get("paper_count", "")) < 75:
        score += 4
    return round(score, 3)


def main() -> int:
    clusters = read_csv(PROCESSED / "icml2026_manual_taxonomy_clusters.csv")
    taxonomy_papers = read_csv(PROCESSED / "icml2026_manual_taxonomy_papers.csv")
    area_queue = read_csv(PROCESSED / "icml2026_area_validation_reviewed.csv")

    papers_by_cluster: dict[str, list[dict[str, str]]] = defaultdict(list)
    queued_by_cluster: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in taxonomy_papers:
        papers_by_cluster[row["semantic_cluster_id"]].append(row)
    for row in area_queue:
        queued_by_cluster[row["semantic_cluster_id"]].append(row)

    rows: list[dict[str, object]] = []
    for cluster in clusters:
        if cluster.get("review_status") == "stable_seed":
            continue
        cluster_id = cluster["semantic_cluster_id"]
        papers = papers_by_cluster[cluster_id]
        queued = queued_by_cluster.get(cluster_id, [])
        high_signal = sorted(
            papers,
            key=lambda row: (
                bool(row.get("award")),
                row.get("is_oral") == "true",
                intish(row.get("public_total_votes", "")),
            ),
            reverse=True,
        )[:8]
        queued_titles = [row["title"] for row in queued[:8]]
        rows.append(
            {
                "adjudication_rank": 0,
                "priority_score": priority_score(cluster, len(queued)),
                "semantic_cluster_id": cluster_id,
                "current_area": cluster["area"],
                "current_subarea": cluster["subarea"],
                "taxonomy_confidence": cluster["taxonomy_confidence"],
                "review_status": cluster["review_status"],
                "review_notes": cluster["review_notes"],
                "paper_count": cluster["paper_count"],
                "oral_count": cluster["oral_count"],
                "award_count": cluster["award_count"],
                "votes_per_paper": cluster["votes_per_paper"],
                "queued_papers": len(queued),
                "semantic_cluster_label": cluster["semantic_cluster_label"],
                "top_terms": cluster["top_terms"],
                "top_topic_groups": cluster["top_topic_groups"],
                "top_themes": cluster["top_themes"],
                "top_lexical_clusters": cluster["top_lexical_clusters"],
                "central_papers": cluster["central_papers"],
                "high_signal_papers": " | ".join(row["title"] for row in high_signal),
                "queued_papers_to_read": " | ".join(queued_titles),
                "decision_prompt": decision_prompt(cluster),
                "allowed_decisions": "keep; relabel_area; relabel_subarea; split_cluster; merge_cluster; unclear",
                "manual_decision_destination": "data/manual/area_review_overrides.csv manual_fault_line_relevance/manual_notes, then update TAXONOMY mapping if relabeling is accepted",
            }
        )

    rows.sort(key=lambda row: (-float(row["priority_score"]), int(str(row["semantic_cluster_id"]))))
    for idx, row in enumerate(rows, start=1):
        row["adjudication_rank"] = idx

    fieldnames = [
        "adjudication_rank",
        "priority_score",
        "semantic_cluster_id",
        "current_area",
        "current_subarea",
        "taxonomy_confidence",
        "review_status",
        "review_notes",
        "paper_count",
        "oral_count",
        "award_count",
        "votes_per_paper",
        "queued_papers",
        "semantic_cluster_label",
        "top_terms",
        "top_topic_groups",
        "top_themes",
        "top_lexical_clusters",
        "central_papers",
        "high_signal_papers",
        "queued_papers_to_read",
        "decision_prompt",
        "allowed_decisions",
        "manual_decision_destination",
    ]
    write_csv(PROCESSED / "icml2026_taxonomy_adjudication_queue.csv", rows, fieldnames)
    write_report(rows)
    print(f"Wrote {PROCESSED / 'icml2026_taxonomy_adjudication_queue.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_taxonomy_adjudication_queue.md'}")
    return 0


def write_report(rows: list[dict[str, object]]) -> None:
    area_counts = Counter(str(row["current_area"]) for row in rows)
    lines = [
        "# ICML 2026 Taxonomy Adjudication Queue",
        "",
        "Cluster-level queue for resolving taxonomy boundaries before using subarea-level landscape claims.",
        "This does not change the taxonomy; it prioritizes what a human should adjudicate first.",
        "",
        "## Snapshot",
        "",
        f"- Clusters needing adjudication: {len(rows)}",
        f"- Queued paper-review rows covered: {sum(int(row['queued_papers']) for row in rows)}",
        f"- Area mix: {', '.join(f'{area}: {count}' for area, count in area_counts.most_common())}",
        "",
        "## Top Adjudication Targets",
        "",
        "| Rank | Cluster | Current area/subarea | Why review | Queued papers | Decision prompt |",
        "| ---: | --- | --- | --- | ---: | --- |",
    ]
    for row in rows[:20]:
        lines.append(
            f"| {row['adjudication_rank']} | {row['semantic_cluster_id']}: {row['semantic_cluster_label']} | "
            f"{row['current_area']} / {row['current_subarea']} | {row['review_notes']} | "
            f"{row['queued_papers']} | {row['decision_prompt']} |"
        )

    lines.extend(["", "## Cluster Details", ""])
    for row in rows:
        lines.extend(
            [
                f"### {row['adjudication_rank']}. Cluster {row['semantic_cluster_id']}: {row['semantic_cluster_label']}",
                "",
                f"- Current mapping: {row['current_area']} / {row['current_subarea']}",
                f"- Review notes: {row['review_notes']}",
                f"- Papers: {row['paper_count']}; orals: {row['oral_count']}; awards: {row['award_count']}; votes/paper: {row['votes_per_paper']}",
                f"- Top terms: {row['top_terms']}",
                f"- Top topic groups: {row['top_topic_groups']}",
                f"- Queued papers to read: {row['queued_papers_to_read'] or 'none in area queue'}",
                f"- High-signal papers: {row['high_signal_papers']}",
                f"- Decision prompt: {row['decision_prompt']}",
                "",
            ]
        )

    lines.extend(
        [
            "## How To Use",
            "",
            "- Read queued papers first, then high-signal papers if the cluster remains ambiguous.",
            "- Record paper-level judgments in `data/manual/area_review_overrides.csv`.",
            "- If multiple papers support relabeling, update `TAXONOMY` in `scripts/build_manual_taxonomy_seed.py` and rebuild downstream artifacts.",
            "- Do not use subarea-level claims for these clusters until adjudication is complete.",
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_taxonomy_adjudication_queue.csv`",
            "- `reports/icml2026_taxonomy_adjudication_queue.md`",
        ]
    )
    (REPORTS / "icml2026_taxonomy_adjudication_queue.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
