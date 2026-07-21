#!/usr/bin/env python3
"""Summarize manual review progress across validation queues."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
MANUAL = ROOT / "data" / "manual"
REPORTS = ROOT / "reports"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"Missing required input: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def apply_manual_overrides(rows: list[dict[str, str]], path: Path, key_fields: list[str], manual_fields: list[str]) -> list[dict[str, str]]:
    if not path.exists():
        return rows
    overrides = read_csv(path)
    by_key = {
        tuple(row.get(field, "") for field in key_fields): row
        for row in overrides
    }
    merged = []
    for row in rows:
        out = dict(row)
        override = by_key.get(tuple(row.get(field, "") for field in key_fields))
        if override:
            for field in manual_fields:
                value = (override.get(field, "") or "").strip()
                if value:
                    out[field] = value
        merged.append(out)
    return merged


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def is_filled(value: str) -> bool:
    return bool((value or "").strip())


def pct(done: int, total: int) -> str:
    return f"{(done / total * 100):.1f}%" if total else "0.0%"


def claim_review_complete(row: dict[str, str]) -> bool:
    return (
        is_filled(row.get("manual_claim_support", ""))
        or is_filled(row.get("manual_taxonomy_judgment", ""))
        or is_filled(row.get("manual_artifact_judgment", ""))
        or is_filled(row.get("manual_notes", ""))
    )


def area_review_complete(row: dict[str, str]) -> bool:
    return (
        is_filled(row.get("manual_validated", ""))
        or is_filled(row.get("manual_primary_contribution_type", ""))
        or is_filled(row.get("manual_method_family", ""))
        or is_filled(row.get("manual_benchmarks", ""))
        or is_filled(row.get("manual_datasets", ""))
        or is_filled(row.get("manual_metrics", ""))
        or is_filled(row.get("manual_artifact_status", ""))
        or is_filled(row.get("manual_result_character", ""))
        or is_filled(row.get("manual_fault_line_relevance", ""))
        or is_filled(row.get("manual_notes", ""))
    )


def summarize_group(rows: list[dict[str, str]], key: str, complete_fn, queue_type: str) -> list[dict[str, object]]:
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[row[key]].append(row)
    out = []
    for group, items in groups.items():
        complete = sum(complete_fn(row) for row in items)
        program = sum(row.get("is_oral") == "true" or bool(row.get("award")) for row in items)
        taxonomy_review = sum((row.get("review_status") or row.get("cluster_review_status")) == "needs_review" for row in items)
        github = sum(bool(row.get("github_url")) for row in items)
        out.append(
            {
                "queue_type": queue_type,
                "group": group,
                "review_rows": len(items),
                "reviewed_rows": complete,
                "remaining_rows": len(items) - complete,
                "completion_rate": round(complete / len(items), 4) if items else 0,
                "program_or_award_rows": program,
                "taxonomy_review_rows": taxonomy_review,
                "github_rows": github,
            }
        )
    out.sort(key=lambda row: (str(row["queue_type"]), -int(row["remaining_rows"]), str(row["group"])))
    return out


def main() -> int:
    reviewed_claims = PROCESSED / "icml2026_claim_validation_reviewed.csv"
    reviewed_areas = PROCESSED / "icml2026_area_validation_reviewed.csv"
    if reviewed_claims.exists() and reviewed_areas.exists():
        claim_rows = read_csv(reviewed_claims)
        area_rows = read_csv(reviewed_areas)
    else:
        claim_rows = read_csv(PROCESSED / "icml2026_claim_validation_queue.csv")
        area_rows = read_csv(PROCESSED / "icml2026_manual_validation_queue.csv")
        claim_rows = apply_manual_overrides(
            claim_rows,
            MANUAL / "claim_review_overrides.csv",
            ["claim_id", "event_id"],
            ["manual_claim_support", "manual_taxonomy_judgment", "manual_artifact_judgment", "manual_notes"],
        )
        area_rows = apply_manual_overrides(
            area_rows,
            MANUAL / "area_review_overrides.csv",
            ["area", "event_id"],
            [
                "manual_validated", "manual_primary_contribution_type", "manual_method_family",
                "manual_benchmarks", "manual_datasets", "manual_metrics", "manual_artifact_status",
                "manual_result_character", "manual_fault_line_relevance", "manual_notes",
            ],
        )

    summary_rows = []
    summary_rows.extend(summarize_group(claim_rows, "claim_id", claim_review_complete, "claim_validation"))
    summary_rows.extend(summarize_group(area_rows, "area", area_review_complete, "area_validation"))

    total_claim_reviewed = sum(claim_review_complete(row) for row in claim_rows)
    total_area_reviewed = sum(area_review_complete(row) for row in area_rows)
    claim_reason_counts = Counter(row["selection_reason"] for row in claim_rows if not claim_review_complete(row))
    area_reason_counts = Counter(row["selection_reason"] for row in area_rows if not area_review_complete(row))

    write_csv(
        PROCESSED / "manual_review_progress.csv",
        summary_rows,
        [
            "queue_type", "group", "review_rows", "reviewed_rows", "remaining_rows",
            "completion_rate", "program_or_award_rows", "taxonomy_review_rows", "github_rows",
        ],
    )

    lines = [
        "# ICML 2026 Manual Review Progress",
        "",
        "This report tracks whether the manual review queues have actually been filled.",
        "A blank manual field means the relevant claim, evidence tag, taxonomy assignment, or artifact judgment is still unchecked.",
        "",
        "## Snapshot",
        "",
        f"- Claim-validation rows reviewed: {total_claim_reviewed}/{len(claim_rows)} ({pct(total_claim_reviewed, len(claim_rows))})",
        f"- Area-validation rows reviewed: {total_area_reviewed}/{len(area_rows)} ({pct(total_area_reviewed, len(area_rows))})",
        f"- Total remaining review rows: {(len(claim_rows) - total_claim_reviewed) + (len(area_rows) - total_area_reviewed)}",
        "",
        "## Claim Review Progress",
        "",
        "| Claim | Rows | Reviewed | Remaining | Program/Award | Taxonomy Review | GitHub |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in [r for r in summary_rows if r["queue_type"] == "claim_validation"]:
        lines.append(
            f"| {row['group']} | {row['review_rows']} | {row['reviewed_rows']} | {row['remaining_rows']} | "
            f"{row['program_or_award_rows']} | {row['taxonomy_review_rows']} | {row['github_rows']} |"
        )

    lines.extend(
        [
            "",
            "## Area Review Progress",
            "",
            "| Area | Rows | Reviewed | Remaining | Program/Award | Taxonomy Review | GitHub |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in [r for r in summary_rows if r["queue_type"] == "area_validation"]:
        lines.append(
            f"| {row['group']} | {row['review_rows']} | {row['reviewed_rows']} | {row['remaining_rows']} | "
            f"{row['program_or_award_rows']} | {row['taxonomy_review_rows']} | {row['github_rows']} |"
        )

    lines.extend(
        [
            "",
            "## Unreviewed Selection Mix",
            "",
            "Claim-validation reasons:",
        ]
    )
    for reason, count in claim_reason_counts.most_common():
        lines.append(f"- {reason}: {count}")
    lines.append("")
    lines.append("Area-validation reasons:")
    for reason, count in area_reason_counts.most_common():
        lines.append(f"- {reason}: {count}")

    lines.extend(
        [
            "",
            "## Recommended Review Order",
            "",
            "1. Claim packets C01, C02, C03, and C07 because they support the main narrative and artifact claims.",
            "2. Area packets for LLM Reasoning, Systems, Safety/Governance, Theory, and Multimodal/Vision because they anchor the report thesis.",
            "3. Taxonomy-review rows before any subarea-level publication claim.",
            "4. GitHub-linked rows with high stars or manual-check reasons before any reproducibility claim.",
            "",
            "## Outputs",
            "",
            "- `data/processed/manual_review_progress.csv`",
            "- `data/processed/icml2026_claim_validation_reviewed.csv`",
            "- `data/processed/icml2026_area_validation_reviewed.csv`",
            "- `reports/manual_review_progress.md`",
        ]
    )
    (REPORTS / "manual_review_progress.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {PROCESSED / 'manual_review_progress.csv'} ({len(summary_rows)} rows)")
    print(f"Wrote {REPORTS / 'manual_review_progress.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
