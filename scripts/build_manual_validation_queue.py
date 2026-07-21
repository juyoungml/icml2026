#!/usr/bin/env python3
"""Build a manual validation queue for representative ICML 2026 papers."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"

TARGET_PER_AREA = 16
REPRESENTATIVE_QUOTA = 6
PUBLIC_ONLY_QUOTA = 4
PROGRAM_ONLY_QUOTA = 4


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


def split_pipe(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split("|") if part.strip()]


def add_candidate(
    selected: list[dict[str, str]],
    seen: set[str],
    row: dict[str, str],
    reason: str,
) -> None:
    key = row["title"]
    if key in seen:
        return
    copy = dict(row)
    copy["selection_reason"] = reason
    selected.append(copy)
    seen.add(key)


def add_from_titles(
    selected: list[dict[str, str]],
    seen: set[str],
    by_title: dict[str, dict[str, str]],
    titles: list[str],
    reason: str,
    quota: int,
) -> None:
    added = 0
    for title in titles:
        if added >= quota:
            return
        if title not in by_title or title in seen:
            continue
        add_candidate(selected, seen, by_title[title], reason)
        added += 1


def main() -> int:
    evidence_rows = read_csv(PROCESSED / "icml2026_paper_evidence_codes.csv")
    fault_rows = read_csv(PROCESSED / "icml2026_area_fault_lines.csv")
    cluster_rows = read_csv(PROCESSED / "icml2026_manual_taxonomy_clusters.csv")

    by_title = {row["title"]: row for row in evidence_rows}
    by_area: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in evidence_rows:
        by_area[row["area"]].append(row)
    cluster_status = {row["semantic_cluster_id"]: row for row in cluster_rows}

    queue = []
    for fault in fault_rows:
        area = fault["area"]
        rows = by_area[area]
        selected: list[dict[str, str]] = []
        seen: set[str] = set()

        add_from_titles(
            selected, seen, by_title, split_pipe(fault["representative_papers"]),
            "fault_line_representative", REPRESENTATIVE_QUOTA,
        )
        add_from_titles(
            selected, seen, by_title, split_pipe(fault["public_not_program_papers"]),
            "public_attention_not_program_signal", PUBLIC_ONLY_QUOTA,
        )
        add_from_titles(
            selected, seen, by_title, split_pipe(fault["program_not_public_papers"]),
            "program_signal_low_public_attention", PROGRAM_ONLY_QUOTA,
        )

        boundary = [
            row for row in rows
            if cluster_status.get(row["semantic_cluster_id"], {}).get("review_status") == "needs_review"
        ]
        for row in sorted(boundary, key=lambda r: (intish(r["public_total_votes"]), r["is_oral"] == "true"), reverse=True):
            if len(selected) >= TARGET_PER_AREA:
                break
            add_candidate(selected, seen, row, "taxonomy_boundary_cluster")

        low_conf = [row for row in rows if row["evidence_confidence"] != "medium"]
        for row in sorted(low_conf, key=lambda r: intish(r["public_total_votes"]), reverse=True):
            if len(selected) >= TARGET_PER_AREA:
                break
            add_candidate(selected, seen, row, "low_evidence_code_confidence")

        for row in sorted(rows, key=lambda r: intish(r["public_total_votes"]), reverse=True):
            if len(selected) >= TARGET_PER_AREA:
                break
            add_candidate(selected, seen, row, "area_high_public_attention_fill")

        for rank, row in enumerate(selected, start=1):
            cluster = cluster_status.get(row["semantic_cluster_id"], {})
            queue.append(
                {
                    "area": area,
                    "area_review_rank": rank,
                    "selection_reason": row["selection_reason"],
                    "event_id": row["event_id"],
                    "title": row["title"],
                    "subarea": row["subarea"],
                    "semantic_cluster_id": row["semantic_cluster_id"],
                    "cluster_review_status": cluster.get("review_status", ""),
                    "cluster_review_notes": cluster.get("review_notes", ""),
                    "is_oral": row["is_oral"],
                    "award": row["award"],
                    "public_total_votes": row["public_total_votes"],
                    "github_url": row["github_url"],
                    "artifact_confidence": row["artifact_confidence"],
                    "heuristic_primary_contribution_type": row["primary_contribution_type"],
                    "heuristic_contribution_types": row["contribution_types"],
                    "heuristic_method_families": row["method_families"],
                    "heuristic_evaluation_settings": row["evaluation_settings"],
                    "heuristic_result_claim_types": row["result_claim_types"],
                    "heuristic_benchmark_mentions": row["benchmark_mentions"],
                    "heuristic_dataset_mentions": row["dataset_mentions"],
                    "heuristic_metric_mentions": row["metric_mentions"],
                    "heuristic_evidence_confidence": row["evidence_confidence"],
                    "manual_validated": "",
                    "manual_primary_contribution_type": "",
                    "manual_method_family": "",
                    "manual_benchmarks": "",
                    "manual_datasets": "",
                    "manual_metrics": "",
                    "manual_artifact_status": "",
                    "manual_result_character": "",
                    "manual_fault_line_relevance": "",
                    "manual_notes": "",
                    "url": row["url"],
                    "alphaxiv_url": row["alphaxiv_url"],
                    "abstract": row["abstract"],
                }
            )

    area_counts = Counter(row["area"] for row in queue)
    reason_counts = Counter(row["selection_reason"] for row in queue)
    review_cluster_count = sum(row["cluster_review_status"] == "needs_review" for row in queue)
    github_count = sum(bool(row["github_url"]) for row in queue)
    oral_award_count = sum(row["is_oral"] == "true" or bool(row["award"]) for row in queue)

    write_csv(
        PROCESSED / "icml2026_manual_validation_queue.csv",
        queue,
        [
            "area", "area_review_rank", "selection_reason", "event_id", "title", "subarea",
            "semantic_cluster_id", "cluster_review_status", "cluster_review_notes", "is_oral",
            "award", "public_total_votes", "github_url", "artifact_confidence",
            "heuristic_primary_contribution_type", "heuristic_contribution_types",
            "heuristic_method_families", "heuristic_evaluation_settings",
            "heuristic_result_claim_types", "heuristic_benchmark_mentions",
            "heuristic_dataset_mentions", "heuristic_metric_mentions",
            "heuristic_evidence_confidence", "manual_validated",
            "manual_primary_contribution_type", "manual_method_family", "manual_benchmarks",
            "manual_datasets", "manual_metrics", "manual_artifact_status",
            "manual_result_character", "manual_fault_line_relevance", "manual_notes",
            "url", "alphaxiv_url", "abstract",
        ],
    )

    lines = [
        "# ICML 2026 Manual Validation Queue",
        "",
        "This queue selects papers for human validation of taxonomy boundaries and evidence codes.",
        "It is designed to turn heuristic tags into trustworthy report claims.",
        "",
        "## Snapshot",
        "",
        f"- Queue size: {len(queue):,}",
        f"- Areas covered: {len(area_counts):,}",
        f"- Target papers per area: up to {TARGET_PER_AREA}",
        f"- Default quotas: {REPRESENTATIVE_QUOTA} representative, {PUBLIC_ONLY_QUOTA} public-only, {PROGRAM_ONLY_QUOTA} program-only, then boundary/low-confidence fill",
        f"- Papers from taxonomy clusters needing review: {review_cluster_count:,}",
        f"- Oral/award papers in queue: {oral_award_count:,}",
        f"- Papers with GitHub URLs in queue: {github_count:,}",
        "",
        "## Selection Reasons",
        "",
    ]
    for reason, count in reason_counts.most_common():
        lines.append(f"- {reason}: {count}")

    lines.extend(["", "## Area Queues", ""])
    for area in [row["area"] for row in fault_rows]:
        lines.append(f"### {area}")
        area_rows = [row for row in queue if row["area"] == area]
        lines.append(f"- Papers selected: {len(area_rows)}")
        lines.append(f"- Selection mix: {', '.join(f'{k}={v}' for k, v in Counter(row['selection_reason'] for row in area_rows).most_common())}")
        for row in area_rows[:8]:
            flags = [row["selection_reason"]]
            if row["is_oral"] == "true":
                flags.append("oral")
            if row["award"]:
                flags.append(row["award"])
            if row["cluster_review_status"] == "needs_review":
                flags.append("taxonomy-review")
            lines.append(f"  - {row['title']} ({'; '.join(flags)}; votes {row['public_total_votes']})")
        lines.append("")

    lines.extend(
        [
            "## Manual Fields To Fill",
            "",
            "- `manual_validated`: yes/no.",
            "- `manual_primary_contribution_type`: benchmark, dataset, method, theory, system, position, application, other.",
            "- `manual_method_family`: concise human-checked method label.",
            "- `manual_benchmarks`, `manual_datasets`, `manual_metrics`: verified names or `none`.",
            "- `manual_artifact_status`: none, linked, live-unchecked, live-checked, runnable, broken, not-applicable.",
            "- `manual_result_character`: positive, negative, mixed, position, theory, benchmark, unclear.",
            "- `manual_fault_line_relevance`: why this paper supports or challenges an area fault line.",
            "",
            "## Caveats",
            "",
            "- Selection is deterministic and heuristic; it is a review queue, not a final reading list.",
            "- The queue intentionally includes public-only, program-signal, and boundary-cluster papers so manual review is not popularity-only.",
        ]
    )
    report_path = REPORTS / "icml2026_manual_validation_queue.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {PROCESSED / 'icml2026_manual_validation_queue.csv'}")
    print(f"Wrote {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
