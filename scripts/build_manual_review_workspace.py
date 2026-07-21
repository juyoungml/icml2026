#!/usr/bin/env python3
"""Create human-editable manual review overlay templates."""

from __future__ import annotations

import argparse
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


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str], force: bool) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        return False
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return True


def review_plan_by_event() -> dict[str, dict[str, str]]:
    plan_path = PROCESSED / "icml2026_researcher_review_plan.csv"
    if not plan_path.exists():
        return {}
    return {row["event_id"]: row for row in read_csv(plan_path)}


def build_claim_rows() -> list[dict[str, object]]:
    plan = review_plan_by_event()
    rows = []
    for row in read_csv(PROCESSED / "icml2026_claim_validation_queue.csv"):
        plan_row = plan.get(row["event_id"], {})
        rows.append(
            {
                "claim_id": row["claim_id"],
                "event_id": row["event_id"],
                "global_review_rank": plan_row.get("global_review_rank", ""),
                "claim_review_rank": row["claim_review_rank"],
                "title": row["title"],
                "area": row["area"],
                "selection_reason": row["selection_reason"],
                "review_focus": row["review_focus"],
                "reviewer": "",
                "review_date": "",
                "review_source": "",
                "manual_claim_support": "",
                "manual_taxonomy_judgment": "",
                "manual_artifact_judgment": "",
                "manual_notes": "",
            }
        )
    rows.sort(key=lambda item: (int(item["global_review_rank"] or 9999), item["claim_id"], int(item["claim_review_rank"])))
    return rows


def build_area_rows() -> list[dict[str, object]]:
    plan = review_plan_by_event()
    rows = []
    for row in read_csv(PROCESSED / "icml2026_manual_validation_queue.csv"):
        plan_row = plan.get(row["event_id"], {})
        rows.append(
            {
                "area": row["area"],
                "event_id": row["event_id"],
                "global_review_rank": plan_row.get("global_review_rank", ""),
                "area_review_rank": row["area_review_rank"],
                "title": row["title"],
                "subarea": row["subarea"],
                "selection_reason": row["selection_reason"],
                "reviewer": "",
                "review_date": "",
                "review_source": "",
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
            }
        )
    rows.sort(key=lambda item: (int(item["global_review_rank"] or 9999), item["area"], int(item["area_review_rank"])))
    return rows


def write_report(claim_written: bool, area_written: bool) -> None:
    claim_rows = build_claim_rows()
    area_rows = build_area_rows()
    lines = [
        "# ICML 2026 Manual Review Workspace",
        "",
        "This creates human-editable overlay files for manual review judgments.",
        "Generated queue files in `data/processed/` should stay reproducible; fill the files in `data/manual/` instead.",
        "",
        "## Files",
        "",
        f"- `data/manual/claim_review_overrides.csv` - {len(claim_rows)} claim-review rows",
        f"- `data/manual/area_review_overrides.csv` - {len(area_rows)} area-review rows",
        "",
        "## Current Write Status",
        "",
        f"- Claim overlay {'created/updated' if claim_written else 'preserved'}",
        f"- Area overlay {'created/updated' if area_written else 'preserved'}",
        "",
        "## Codebook",
        "",
        "- Canonical values: `data/processed/icml2026_manual_review_codebook.csv`",
        "- Human guide: `reports/icml2026_manual_review_codebook.md`",
        "",
        "## How To Fill Claim Rows",
        "",
        "- `manual_claim_support`: supports, partial_support, weakens, contradicts, not_applicable, unclear.",
        "- `manual_taxonomy_judgment`: correct, too_broad, too_narrow, wrong_area, wrong_subarea, unclear.",
        "- `manual_artifact_judgment`: not_applicable, none, linked_unchecked, live_checked, runnable, broken.",
        "- `manual_notes`: concise evidence, caveat, or correction.",
        "",
        "## How To Fill Area Rows",
        "",
        "- `manual_validated`: yes, partial, no, unclear.",
        "- `manual_primary_contribution_type`: method, theory, system, dataset, benchmark, analysis, application, survey_or_position, unclear.",
        "- `manual_artifact_status`: none, linked_unchecked, live_checked, runnable, broken, not_applicable.",
        "- `manual_fault_line_relevance`: headline, supporting, caveat, not_relevant, unclear.",
        "",
        "## Rebuild After Editing",
        "",
        "```bash",
        "uv run python scripts/lint_manual_review_values.py",
        "uv run python scripts/build_reviewed_validation_tables.py",
        "uv run python scripts/build_review_progress.py",
        "uv run python scripts/build_researcher_readiness_audit.py",
        "uv run python scripts/build_researcher_gap_audit.py",
        "uv run python scripts/build_area_briefing_cards.py",
        "uv run python scripts/build_static_dashboard.py",
        "uv run python scripts/build_project_index.py",
        "uv run python scripts/validate_workspace.py",
        "```",
    ]
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "manual_review_workspace.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="overwrite existing manual overlay files")
    args = parser.parse_args()

    claim_fields = [
        "claim_id", "event_id", "global_review_rank", "claim_review_rank", "title", "area",
        "selection_reason", "review_focus", "reviewer", "review_date", "review_source",
        *CLAIM_MANUAL_FIELDS,
    ]
    area_fields = [
        "area", "event_id", "global_review_rank", "area_review_rank", "title", "subarea",
        "selection_reason", "reviewer", "review_date", "review_source", *AREA_MANUAL_FIELDS,
    ]
    claim_written = write_csv(MANUAL / "claim_review_overrides.csv", build_claim_rows(), claim_fields, args.force)
    area_written = write_csv(MANUAL / "area_review_overrides.csv", build_area_rows(), area_fields, args.force)
    write_report(claim_written, area_written)
    print(f"{'Wrote' if claim_written else 'Preserved'} {MANUAL / 'claim_review_overrides.csv'}")
    print(f"{'Wrote' if area_written else 'Preserved'} {MANUAL / 'area_review_overrides.csv'}")
    print(f"Wrote {REPORTS / 'manual_review_workspace.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
