#!/usr/bin/env python3
"""Lint manual review CSV coded values against the manual review codebook."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
MANUAL = ROOT / "data" / "manual"
REPORTS = ROOT / "reports"


TARGETS = [
    ("claim_overlay", MANUAL / "claim_review_overrides.csv", "claim_id", "event_id"),
    ("area_overlay", MANUAL / "area_review_overrides.csv", "area", "event_id"),
    ("paper_notes", MANUAL / "icml2026_review_sprint_01_paper_notes.csv", "sprint_rank", "event_id"),
    ("paper_notes", MANUAL / "icml2026_review_sprint_02_paper_notes.csv", "sprint_rank", "event_id"),
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


def load_allowed() -> dict[tuple[str, str], set[str]]:
    allowed: dict[tuple[str, str], set[str]] = defaultdict(set)
    for row in read_csv(PROCESSED / "icml2026_manual_review_codebook.csv"):
        allowed[(row["table"], row["field"])].add(row["allowed_value"])
    return allowed


def lint_rows() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    allowed = load_allowed()
    issues: list[dict[str, object]] = []
    summary: list[dict[str, object]] = []

    for table, path, key1, key2 in TARGETS:
        rows = read_csv(path)
        coded_fields = sorted(field for tbl, field in allowed if tbl == table)
        checked_values = 0
        invalid_values = 0
        filled_rows = set()
        for index, row in enumerate(rows, start=2):
            row_has_value = False
            for field in coded_fields:
                value = (row.get(field, "") or "").strip()
                if not value:
                    continue
                checked_values += 1
                row_has_value = True
                if value not in allowed[(table, field)]:
                    invalid_values += 1
                    issues.append(
                        {
                            "path": str(path.relative_to(ROOT)),
                            "table": table,
                            "row_number": index,
                            "key": f"{row.get(key1, '')}::{row.get(key2, '')}",
                            "field": field,
                            "value": value,
                            "allowed_values": "; ".join(sorted(allowed[(table, field)])),
                            "message": "Non-canonical coded value; use the manual review codebook value or move nuance into notes.",
                        }
                    )
            if row_has_value:
                filled_rows.add(index)
        summary.append(
            {
                "path": str(path.relative_to(ROOT)),
                "table": table,
                "rows": len(rows),
                "coded_fields": len(coded_fields),
                "rows_with_coded_values": len(filled_rows),
                "checked_values": checked_values,
                "invalid_values": invalid_values,
            }
        )
    return issues, summary


def write_report(issues: list[dict[str, object]], summary: list[dict[str, object]]) -> None:
    total_checked = sum(int(row["checked_values"]) for row in summary)
    total_invalid = len(issues)
    lines = [
        "# ICML 2026 Manual Review Value Lint",
        "",
        "Checks non-empty coded manual review fields against `data/processed/icml2026_manual_review_codebook.csv`.",
        "Blank fields are allowed and mean the row has not been reviewed yet.",
        "",
        "## Summary",
        "",
        f"- Files checked: {len(summary)}",
        f"- Coded values checked: {total_checked}",
        f"- Invalid coded values: {total_invalid}",
        "",
        "## Files",
        "",
        "| File | Table | Rows | Coded fields | Rows with coded values | Checked values | Invalid values |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in summary:
        lines.append(
            f"| `{row['path']}` | {row['table']} | {row['rows']} | {row['coded_fields']} | "
            f"{row['rows_with_coded_values']} | {row['checked_values']} | {row['invalid_values']} |"
        )

    lines.append("")
    if issues:
        lines.extend(
            [
                "## Invalid Values",
                "",
                "| File | Row | Key | Field | Value | Allowed values |",
                "| --- | ---: | --- | --- | --- | --- |",
            ]
        )
        for issue in issues:
            lines.append(
                f"| `{issue['path']}` | {issue['row_number']} | `{issue['key']}` | `{issue['field']}` | "
                f"`{issue['value']}` | {issue['allowed_values']} |"
            )
        lines.append("")
    else:
        lines.extend(["## Invalid Values", "", "No invalid coded values found.", ""])

    lines.extend(
        [
            "## Outputs",
            "",
            "- `data/processed/icml2026_manual_review_value_lint.csv`",
            "- `data/processed/icml2026_manual_review_value_lint_summary.csv`",
            "- `reports/icml2026_manual_review_value_lint.md`",
        ]
    )
    (REPORTS / "icml2026_manual_review_value_lint.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    issues, summary = lint_rows()
    write_csv(
        PROCESSED / "icml2026_manual_review_value_lint.csv",
        issues,
        ["path", "table", "row_number", "key", "field", "value", "allowed_values", "message"],
    )
    write_csv(
        PROCESSED / "icml2026_manual_review_value_lint_summary.csv",
        summary,
        ["path", "table", "rows", "coded_fields", "rows_with_coded_values", "checked_values", "invalid_values"],
    )
    write_report(issues, summary)
    print(f"Wrote {PROCESSED / 'icml2026_manual_review_value_lint.csv'} ({len(issues)} issues)")
    print(f"Wrote {PROCESSED / 'icml2026_manual_review_value_lint_summary.csv'} ({len(summary)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_manual_review_value_lint.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
