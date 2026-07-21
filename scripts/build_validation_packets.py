#!/usr/bin/env python3
"""Generate area-specific markdown packets for manual paper validation."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"
PACKET_DIR = REPORTS / "validation_packets"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"Missing required input: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def compact(value: str, fallback: str = "none") -> str:
    return value.strip() if value and value.strip() else fallback


def flags_for(row: dict[str, str]) -> list[str]:
    flags = [row["selection_reason"]]
    if row["is_oral"] == "true":
        flags.append("oral")
    if row["award"]:
        flags.append(row["award"])
    if row["cluster_review_status"] == "needs_review":
        flags.append("taxonomy-review")
    if row["heuristic_evidence_confidence"] != "medium":
        flags.append(f"evidence-{row['heuristic_evidence_confidence']}")
    if row["github_url"]:
        flags.append("github")
    return flags


def checkbox_block() -> list[str]:
    return [
        "Validation checklist:",
        "- [ ] Contribution type checked",
        "- [ ] Method family checked",
        "- [ ] Benchmarks/datasets/metrics checked",
        "- [ ] Artifact status checked",
        "- [ ] Fault-line relevance written",
        "",
        "Manual notes:",
        "",
        "- Primary contribution type:",
        "- Method family:",
        "- Benchmarks:",
        "- Datasets:",
        "- Metrics:",
        "- Artifact status:",
        "- Result character:",
        "- Fault-line relevance:",
        "- Notes:",
    ]


def main() -> int:
    queue = read_csv(PROCESSED / "icml2026_manual_validation_queue.csv")
    fault_rows = read_csv(PROCESSED / "icml2026_area_fault_lines.csv")
    fault_by_area = {row["area"]: row for row in fault_rows}
    by_area: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in queue:
        by_area[row["area"]].append(row)

    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    index_lines = [
        "# ICML 2026 Validation Packet Index",
        "",
        "These packets convert the manual validation queue into area-specific reading worksheets.",
        "They are for human review; checked fields should be copied back into `data/processed/icml2026_manual_validation_queue.csv` or a reviewed derivative.",
        "",
        "## Packets",
        "",
    ]

    for area in [row["area"] for row in fault_rows]:
        rows = sorted(by_area[area], key=lambda row: int(row["area_review_rank"]))
        fault = fault_by_area[area]
        slug = slugify(area)
        path = PACKET_DIR / f"{slug}.md"
        reason_counts = Counter(row["selection_reason"] for row in rows)
        lines = [
            f"# {area}",
            "",
            "Manual validation packet for representative and boundary papers.",
            "",
            "## Area Context",
            "",
            f"Headline: {fault['headline']}",
            "",
            "Fault lines:",
        ]
        for item in fault["fault_lines"].split(" | "):
            lines.append(f"- {item}")
        lines.extend(["", "What to read for:"])
        for item in fault["read_for"].split(" | "):
            lines.append(f"- {item}")
        lines.extend(
            [
                "",
                "## Queue Summary",
                "",
                f"- Papers: {len(rows)}",
                f"- Selection mix: {', '.join(f'{k}={v}' for k, v in reason_counts.most_common())}",
                f"- Papers from taxonomy-review clusters: {sum(row['cluster_review_status'] == 'needs_review' for row in rows)}",
                f"- Papers with GitHub URLs: {sum(bool(row['github_url']) for row in rows)}",
                "",
                "## Papers",
                "",
            ]
        )

        for row in rows:
            lines.append(f"### {row['area_review_rank']}. {row['title']}")
            lines.append("")
            lines.append(f"Flags: {', '.join(flags_for(row))}")
            lines.append("")
            lines.append(f"- Subarea: {row['subarea']}")
            lines.append(f"- Votes: {row['public_total_votes']}")
            lines.append(f"- ICML URL: {compact(row['url'])}")
            lines.append(f"- AlphaXiv URL: {compact(row['alphaxiv_url'])}")
            lines.append(f"- GitHub URL: {compact(row['github_url'])}")
            lines.append(f"- Artifact confidence: {compact(row['artifact_confidence'])}")
            lines.append(f"- Cluster review: {compact(row['cluster_review_status'])}; {compact(row['cluster_review_notes'])}")
            lines.append("")
            lines.append("Heuristic evidence codes:")
            lines.append(f"- Primary contribution: {compact(row['heuristic_primary_contribution_type'])}")
            lines.append(f"- Contribution types: {compact(row['heuristic_contribution_types'])}")
            lines.append(f"- Method families: {compact(row['heuristic_method_families'])}")
            lines.append(f"- Evaluation settings: {compact(row['heuristic_evaluation_settings'])}")
            lines.append(f"- Result claim cues: {compact(row['heuristic_result_claim_types'])}")
            lines.append(f"- Benchmarks: {compact(row['heuristic_benchmark_mentions'])}")
            lines.append(f"- Datasets: {compact(row['heuristic_dataset_mentions'])}")
            lines.append(f"- Metrics: {compact(row['heuristic_metric_mentions'])}")
            lines.append("")
            lines.append("Abstract:")
            lines.append("")
            lines.append(compact(row["abstract"], "No abstract available."))
            lines.append("")
            lines.extend(checkbox_block())
            lines.append("")

        path.write_text("\n".join(lines), encoding="utf-8")
        index_lines.append(f"- [{area}](validation_packets/{path.name}) - {len(rows)} papers")

    index_lines.extend(
        [
            "",
            "## Review Guidance",
            "",
            "- Prioritize correcting false benchmark/dataset/metric tags.",
            "- For papers in taxonomy-review clusters, decide whether the current area/subarea assignment is acceptable.",
            "- For public-only papers, check whether the attention reflects a genuine landscape signal or community hype.",
            "- For program-only papers, check whether the low public attention hides an important technical contribution.",
        ]
    )
    index_path = REPORTS / "icml2026_validation_packet_index.md"
    index_path.write_text("\n".join(index_lines), encoding="utf-8")

    print(f"Wrote {index_path}")
    for path in sorted(PACKET_DIR.glob("*.md")):
        print(f"Wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
