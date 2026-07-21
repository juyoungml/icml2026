#!/usr/bin/env python3
"""Build a transfer checklist from first-sprint paper notes to review overlays."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
MANUAL = ROOT / "data" / "manual"
REPORTS = ROOT / "reports"


CLAIM_ALLOWED_VALUES = (
    "manual_claim_support: supports, partial_support, weakens, contradicts, not_applicable, unclear; "
    "manual_taxonomy_judgment: correct, too_broad, too_narrow, wrong_area, wrong_subarea, unclear; "
    "manual_artifact_judgment: not_applicable, none, linked_unchecked, live_checked, runnable, broken"
)
AREA_ALLOWED_VALUES = (
    "manual_validated: yes, partial, no, unclear; "
    "manual_primary_contribution_type: method, theory, system, dataset, benchmark, analysis, application, survey_or_position, unclear; "
    "manual_artifact_status: none, linked_unchecked, live_checked, runnable, broken, not_applicable; "
    "manual_fault_line_relevance: headline, supporting, caveat, not_relevant, unclear"
)


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


def split_keys(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split("|") if part.strip()]


def nonempty(value: object) -> bool:
    return bool(str(value or "").strip())


def note_status(row: dict[str, str]) -> str:
    if not any(
        nonempty(row.get(field))
        for field in [
            "paper_read_status",
            "contribution_summary",
            "novelty_judgment",
            "method_summary",
            "evidence_strength",
            "limitations",
            "artifact_status_checked",
            "claim_implications",
            "taxonomy_correction",
            "final_report_use",
            "paper_note",
        ]
    ):
        return "pending_note"
    if row.get("paper_read_status") == "blocked":
        return "blocked"
    if nonempty(row.get("claim_implications")) or nonempty(row.get("taxonomy_correction")):
        return "ready_for_overlay_transfer"
    return "note_started_needs_decision"


def target_exists(key: str, target_type: str, claim_keys: set[str], area_keys: set[str]) -> bool:
    if target_type == "claim":
        return key in claim_keys
    return key in area_keys


def claim_id_from_key(key: str) -> str:
    return key.split("::", 1)[0] if "::" in key else ""


def bridge_row(
    note: dict[str, str],
    suggestion: dict[str, str],
    target_type: str,
    overlay_key: str,
    target_present: bool,
) -> dict[str, object]:
    status = note_status(note)
    if target_type == "claim":
        target_file = "data/manual/claim_review_overrides.csv"
        overlay_fields = "manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes"
        source_fields = "claim_implications; taxonomy_correction; artifact_status_checked; evidence_strength; limitations; final_report_use"
        allowed = CLAIM_ALLOWED_VALUES
        instruction = (
            "Use the paper note to decide whether this paper supports, weakens, complicates, or is not applicable "
            "to the linked claim; copy concise evidence and caveats into manual_notes."
        )
    else:
        target_file = "data/manual/area_review_overrides.csv"
        overlay_fields = (
            "manual_validated; manual_primary_contribution_type; manual_method_family; manual_benchmarks; "
            "manual_datasets; manual_metrics; manual_artifact_status; manual_result_character; "
            "manual_fault_line_relevance; manual_notes"
        )
        source_fields = (
            "contribution_summary; novelty_judgment; method_summary; baselines_checked; datasets_checked; "
            "metrics_checked; evidence_strength; taxonomy_correction; final_report_use"
        )
        allowed = AREA_ALLOWED_VALUES
        instruction = (
            "Use the paper note to validate the area/subarea assignment, contribution type, method/evidence fields, "
            "artifact status, and whether the paper should be a headline, support, caveat, or excluded example."
        )

    if not target_present:
        blocking_gap = "overlay target missing"
    elif status == "pending_note":
        blocking_gap = "paper note not started"
    elif status == "note_started_needs_decision":
        blocking_gap = "note exists but claim/taxonomy decision fields are not filled"
    elif status == "blocked":
        blocking_gap = "paper read blocked"
    else:
        blocking_gap = "ready to transfer"

    return {
        "target_type": target_type,
        "target_file": target_file,
        "overlay_key": overlay_key,
        "target_present": str(target_present).lower(),
        "event_id": note.get("event_id", ""),
        "sprint_rank": note.get("sprint_rank", ""),
        "title": note.get("title", ""),
        "area": note.get("area", ""),
        "subarea": note.get("subarea", ""),
        "claim_id": claim_id_from_key(overlay_key) if target_type == "claim" else "",
        "note_status": status,
        "blocking_gap": blocking_gap,
        "source_fields_to_read": source_fields,
        "overlay_fields_to_update": overlay_fields,
        "allowed_values": allowed,
        "transfer_instruction": instruction,
        "claim_implication_prompt": suggestion.get("claim_implication_prompt", ""),
        "taxonomy_question": suggestion.get("taxonomy_question", ""),
        "artifact_check_prompt": suggestion.get("artifact_check_prompt", ""),
        "note_claim_implications": note.get("claim_implications", ""),
        "note_taxonomy_correction": note.get("taxonomy_correction", ""),
        "note_evidence_strength": note.get("evidence_strength", ""),
        "note_artifact_status_checked": note.get("artifact_status_checked", ""),
        "note_final_report_use": note.get("final_report_use", ""),
    }


def main() -> int:
    notes = read_csv(MANUAL / "icml2026_review_sprint_01_paper_notes.csv")
    suggestions = {
        row["event_id"]: row
        for row in read_csv(PROCESSED / "icml2026_sprint_prereview_suggestions.csv")
    }
    claim_overlays = read_csv(MANUAL / "claim_review_overrides.csv")
    area_overlays = read_csv(MANUAL / "area_review_overrides.csv")
    claim_keys = {f"{row['claim_id']}::{row['event_id']}" for row in claim_overlays}
    area_keys = {f"{row['area']}::{row['event_id']}" for row in area_overlays}

    rows: list[dict[str, object]] = []
    for note in notes:
        suggestion = suggestions.get(note.get("event_id", ""), {})
        for key in split_keys(note.get("claim_overlay_keys", "")):
            rows.append(bridge_row(note, suggestion, "claim", key, target_exists(key, "claim", claim_keys, area_keys)))
        for key in split_keys(note.get("area_overlay_keys", "")):
            rows.append(bridge_row(note, suggestion, "area", key, target_exists(key, "area", claim_keys, area_keys)))

    rows.sort(key=lambda row: (int(row["sprint_rank"] or 9999), row["target_type"], row["overlay_key"]))
    fieldnames = [
        "target_type",
        "target_file",
        "overlay_key",
        "target_present",
        "event_id",
        "sprint_rank",
        "title",
        "area",
        "subarea",
        "claim_id",
        "note_status",
        "blocking_gap",
        "source_fields_to_read",
        "overlay_fields_to_update",
        "allowed_values",
        "transfer_instruction",
        "claim_implication_prompt",
        "taxonomy_question",
        "artifact_check_prompt",
        "note_claim_implications",
        "note_taxonomy_correction",
        "note_evidence_strength",
        "note_artifact_status_checked",
        "note_final_report_use",
    ]
    write_csv(PROCESSED / "icml2026_paper_note_overlay_bridge.csv", rows, fieldnames)

    claim_rows = [row for row in rows if row["target_type"] == "claim"]
    area_rows = [row for row in rows if row["target_type"] == "area"]
    ready_rows = [row for row in rows if row["blocking_gap"] == "ready to transfer"]
    missing_targets = [row for row in rows if row["target_present"] != "true"]

    lines = [
        "# ICML 2026 Paper Note to Overlay Bridge",
        "",
        "Transfer checklist from first-sprint paper notes into claim and area review overlays.",
        "",
        "## Snapshot",
        "",
        f"- Sprint papers represented: {len(notes)}",
        f"- Overlay transfer rows: {len(rows)}",
        f"- Claim overlay targets: {len(claim_rows)}",
        f"- Area overlay targets: {len(area_rows)}",
        f"- Ready to transfer now: {len(ready_rows)}",
        f"- Missing overlay targets: {len(missing_targets)}",
        "",
        "## Workflow",
        "",
        "1. Fill `data/manual/icml2026_review_sprint_01_paper_notes.csv` while reading papers.",
        "2. Rebuild this bridge.",
        "3. For rows marked `ready to transfer`, copy concise decisions into the target overlay file and fields listed in the row.",
        "4. Rebuild reviewed tables, review progress, readiness, acceptance criteria, and validation.",
        "",
        "## First Rows",
        "",
        "| Rank | Target | Overlay key | Blocking gap | Source fields | Overlay fields |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for row in rows[:25]:
        lines.append(
            f"| {row['sprint_rank']} | {row['target_type']} | `{row['overlay_key']}` | {row['blocking_gap']} | "
            f"{row['source_fields_to_read']} | {row['overlay_fields_to_update']} |"
        )
    lines.extend(
        [
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_paper_note_overlay_bridge.csv`",
            "- `reports/icml2026_paper_note_overlay_bridge.md`",
        ]
    )
    (REPORTS / "icml2026_paper_note_overlay_bridge.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {PROCESSED / 'icml2026_paper_note_overlay_bridge.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_paper_note_overlay_bridge.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
