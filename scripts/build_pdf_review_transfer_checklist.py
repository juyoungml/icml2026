#!/usr/bin/env python3
"""Build a focused transfer checklist from PDF review worksheet rows to overlays."""

from __future__ import annotations

import csv
from collections import Counter
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


def main() -> int:
    worksheet = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_pdf_review_worksheet.csv")}
    bridge = read_csv(PROCESSED / "icml2026_paper_note_overlay_bridge.csv")

    rows: list[dict[str, object]] = []
    for bridge_row in bridge:
        event_id = bridge_row.get("event_id", "")
        if event_id not in worksheet:
            continue
        sheet = worksheet[event_id]
        rows.append(
            {
                "event_id": event_id,
                "sprint_rank": sheet.get("sprint_rank", ""),
                "title": sheet.get("title", ""),
                "target_type": bridge_row.get("target_type", ""),
                "overlay_key": bridge_row.get("overlay_key", ""),
                "target_file": bridge_row.get("target_file", ""),
                "target_present": bridge_row.get("target_present", ""),
                "claim_id": bridge_row.get("claim_id", ""),
                "pdf_card_path": sheet.get("pdf_card_path", ""),
                "worksheet_path": "data/processed/icml2026_pdf_review_worksheet.csv",
                "paper_note_file": sheet.get("paper_note_file", ""),
                "page_pass": f"method {sheet.get('method_pages', '')}; evidence {sheet.get('evidence_pages', '')}; limitations {sheet.get('limitation_pages', '')}; artifact {sheet.get('artifact_pages', '') or 'not detected'}",
                "source_fields_to_read": bridge_row.get("source_fields_to_read", ""),
                "overlay_fields_to_update": bridge_row.get("overlay_fields_to_update", ""),
                "allowed_values": bridge_row.get("allowed_values", ""),
                "current_note_status": bridge_row.get("note_status", ""),
                "current_blocking_gap": bridge_row.get("blocking_gap", ""),
                "transfer_instruction": bridge_row.get("transfer_instruction", ""),
                "post_transfer_commands": "uv run python scripts/lint_manual_review_values.py && uv run python scripts/build_reviewed_validation_tables.py && uv run python scripts/build_review_progress.py && uv run python scripts/build_researcher_readiness_audit.py && uv run python scripts/build_claim_acceptance_criteria.py && uv run python scripts/build_claim_decision_board.py && uv run python scripts/build_safe_statement_register.py && uv run python scripts/validate_workspace.py",
            }
        )

    rows.sort(key=lambda row: (int(str(row["sprint_rank"]) or 999), str(row["target_type"]), str(row["overlay_key"])))
    fieldnames = [
        "event_id",
        "sprint_rank",
        "title",
        "target_type",
        "overlay_key",
        "target_file",
        "target_present",
        "claim_id",
        "pdf_card_path",
        "worksheet_path",
        "paper_note_file",
        "page_pass",
        "source_fields_to_read",
        "overlay_fields_to_update",
        "allowed_values",
        "current_note_status",
        "current_blocking_gap",
        "transfer_instruction",
        "post_transfer_commands",
    ]
    write_csv(PROCESSED / "icml2026_pdf_review_transfer_checklist.csv", rows, fieldnames)
    write_report(rows)
    print(f"Wrote {PROCESSED / 'icml2026_pdf_review_transfer_checklist.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_pdf_review_transfer_checklist.md'}")
    return 0


def write_report(rows: list[dict[str, object]]) -> None:
    type_counts = Counter(str(row["target_type"]) for row in rows)
    event_count = len({row["event_id"] for row in rows})
    lines = [
        "# ICML 2026 PDF Review Transfer Checklist",
        "",
        "Focused transfer checklist for moving completed bounded-PDF worksheet judgments into canonical paper notes and manual overlay files.",
        "",
        "This checklist is generated from blank or partially blank review state. It is a transfer map, not evidence that transfer has happened.",
        "",
        "## Snapshot",
        "",
        f"- Transfer rows: {len(rows)}",
        f"- Papers covered: {event_count}",
        f"- Target mix: {', '.join(f'{key}={value}' for key, value in sorted(type_counts.items()))}",
        "",
        "## Transfer Sequence",
        "",
        "1. Fill the worksheet judgment fields after reading the PDF card pages.",
        "2. Copy paper-level judgments into the canonical paper-note row for the same `event_id`.",
        "3. Use this checklist to transfer claim and area judgments into the target overlay rows.",
        "4. Run the post-transfer commands to rebuild reviewed tables, claim decisions, safe wording, and validation.",
        "",
        "## Checklist",
        "",
        "| Rank | Paper | Target | Overlay key | Current gap | Fields to update |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['sprint_rank']} | {row['title']} | {row['target_type']} | `{row['overlay_key']}` | "
            f"{row['current_blocking_gap']} | {row['overlay_fields_to_update']} |"
        )
    lines.extend(
        [
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_pdf_review_transfer_checklist.csv`",
            "- `reports/icml2026_pdf_review_transfer_checklist.md`",
        ]
    )
    (REPORTS / "icml2026_pdf_review_transfer_checklist.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
