#!/usr/bin/env python3
"""Merge generated validation queues with human review overlays."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
MANUAL = ROOT / "data" / "manual"
REPORTS = ROOT / "reports"

CLAIM_MANUAL_FIELDS = [
    "manual_claim_support",
    "manual_taxonomy_judgment",
    "manual_artifact_judgment",
    "manual_notes",
]

AREA_MANUAL_FIELDS = [
    "manual_validated",
    "manual_primary_contribution_type",
    "manual_method_family",
    "manual_benchmarks",
    "manual_datasets",
    "manual_metrics",
    "manual_artifact_status",
    "manual_result_character",
    "manual_fault_line_relevance",
    "manual_notes",
]


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


def is_filled(value: str) -> bool:
    return bool((value or "").strip())


def overlay_index(path: Path, key_fields: list[str]) -> dict[tuple[str, ...], dict[str, str]]:
    if not path.exists():
        return {}
    return {
        tuple(row.get(field, "") for field in key_fields): row
        for row in read_csv(path)
    }


def merge_rows(
    rows: list[dict[str, str]],
    overrides: dict[tuple[str, ...], dict[str, str]],
    key_fields: list[str],
    manual_fields: list[str],
) -> list[dict[str, object]]:
    merged = []
    for row in rows:
        out: dict[str, object] = dict(row)
        override = overrides.get(tuple(row.get(field, "") for field in key_fields), {})
        filled_fields = []
        for field in manual_fields:
            value = (override.get(field, "") or "").strip()
            if value:
                out[field] = value
                filled_fields.append(field)
        out["review_overlay_present"] = "true" if override else "false"
        out["review_overlay_filled_fields"] = "; ".join(filled_fields)
        out["reviewed"] = "true" if filled_fields else "false"
        out["reviewer"] = override.get("reviewer", "")
        out["review_date"] = override.get("review_date", "")
        out["review_source"] = override.get("review_source", "")
        merged.append(out)
    return merged


def write_report(claim_rows: list[dict[str, object]], area_rows: list[dict[str, object]]) -> None:
    claim_reviewed = sum(row["reviewed"] == "true" for row in claim_rows)
    area_reviewed = sum(row["reviewed"] == "true" for row in area_rows)
    lines = [
        "# ICML 2026 Reviewed Validation Tables",
        "",
        "These tables merge reproducible generated validation queues with human-editable review overlays.",
        "They are the auditable reviewed view used by downstream progress and readiness reports.",
        "",
        "## Snapshot",
        "",
        f"- Claim reviewed rows: {claim_reviewed}/{len(claim_rows)}",
        f"- Area reviewed rows: {area_reviewed}/{len(area_rows)}",
        f"- Total reviewed rows: {claim_reviewed + area_reviewed}/{len(claim_rows) + len(area_rows)}",
        "",
        "## Inputs",
        "",
        "- `data/processed/icml2026_claim_validation_queue.csv`",
        "- `data/processed/icml2026_manual_validation_queue.csv`",
        "- `data/manual/claim_review_overrides.csv`",
        "- `data/manual/area_review_overrides.csv`",
        "",
        "## Outputs",
        "",
        "- `data/processed/icml2026_claim_validation_reviewed.csv`",
        "- `data/processed/icml2026_area_validation_reviewed.csv`",
        "- `reports/reviewed_validation_tables.md`",
    ]
    (REPORTS / "reviewed_validation_tables.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    claim_rows = read_csv(PROCESSED / "icml2026_claim_validation_queue.csv")
    area_rows = read_csv(PROCESSED / "icml2026_manual_validation_queue.csv")
    claim_overrides = overlay_index(MANUAL / "claim_review_overrides.csv", ["claim_id", "event_id"])
    area_overrides = overlay_index(MANUAL / "area_review_overrides.csv", ["area", "event_id"])

    reviewed_claims = merge_rows(claim_rows, claim_overrides, ["claim_id", "event_id"], CLAIM_MANUAL_FIELDS)
    reviewed_areas = merge_rows(area_rows, area_overrides, ["area", "event_id"], AREA_MANUAL_FIELDS)

    claim_fields = list(claim_rows[0].keys()) + [
        "review_overlay_present", "review_overlay_filled_fields", "reviewed", "reviewer", "review_date", "review_source",
    ]
    area_fields = list(area_rows[0].keys()) + [
        "review_overlay_present", "review_overlay_filled_fields", "reviewed", "reviewer", "review_date", "review_source",
    ]
    write_csv(PROCESSED / "icml2026_claim_validation_reviewed.csv", reviewed_claims, claim_fields)
    write_csv(PROCESSED / "icml2026_area_validation_reviewed.csv", reviewed_areas, area_fields)
    write_report(reviewed_claims, reviewed_areas)
    print(f"Wrote {PROCESSED / 'icml2026_claim_validation_reviewed.csv'} ({len(reviewed_claims)} rows)")
    print(f"Wrote {PROCESSED / 'icml2026_area_validation_reviewed.csv'} ({len(reviewed_areas)} rows)")
    print(f"Wrote {REPORTS / 'reviewed_validation_tables.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
