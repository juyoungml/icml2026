#!/usr/bin/env python3
"""Build a reviewer-ready worksheet for probed ICML 2026 PDFs."""

from __future__ import annotations

import csv
from collections import defaultdict
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


def unique_join(values: list[str], limit: int | None = None) -> str:
    out = []
    for value in values:
        if value and value not in out:
            out.append(value)
    if limit is not None:
        out = out[:limit]
    return " ; ".join(out)


def build_rows() -> list[dict[str, object]]:
    cards = read_csv(PROCESSED / "icml2026_pdf_review_cards.csv")
    source = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_paper_source_access_map.csv")}
    tasks_by_event: dict[str, list[dict[str, str]]] = defaultdict(list)
    for task in read_csv(PROCESSED / "icml2026_review_decision_tasks.csv"):
        tasks_by_event[task["event_id"]].append(task)

    rows: list[dict[str, object]] = []
    for card in cards:
        event_id = card["event_id"]
        tasks = sorted(tasks_by_event.get(event_id, []), key=lambda row: int(row.get("priority_rank") or 9999))
        source_row = source.get(event_id, {})
        rows.append(
            {
                "event_id": event_id,
                "sprint": card["sprint"],
                "sprint_rank": card["sprint_rank"],
                "title": card["title"],
                "target_claims": card["target_claims"],
                "task_ids": card["task_ids"],
                "task_focuses": unique_join([task.get("task_focus", "") for task in tasks]),
                "local_pdf_path": card["local_pdf_path"],
                "pdf_card_path": f"reports/pdf_review_cards/{event_id}.md",
                "brief_path": card["brief_path"],
                "paper_note_file": card["paper_note_file"],
                "icml_url": source_row.get("icml_url", ""),
                "openreview_url": source_row.get("openreview_url", ""),
                "arxiv_pdf_url": source_row.get("arxiv_pdf_url", ""),
                "github_url": source_row.get("github_url", ""),
                "method_pages": card["method_pages"],
                "evidence_pages": card["evidence_pages"],
                "limitation_pages": card["limitation_pages"],
                "artifact_pages": card["artifact_pages"],
                "claim_questions": unique_join([task.get("claim_question", "") for task in tasks], limit=3),
                "support_tests": unique_join([task.get("support_signal", "") for task in tasks], limit=3),
                "weakening_tests": unique_join([task.get("weakening_signal", "") for task in tasks], limit=3),
                "blocking_risks": unique_join([task.get("blocking_risk", "") for task in tasks], limit=3),
                "required_manual_fields": card["required_manual_fields"],
                "read_order": "pdf_card -> method_pages -> evidence_pages -> limitation_pages -> artifact_pages -> paper_note_file -> claim_overlay",
                "paper_read_status": "",
                "contribution_summary": "",
                "novelty_judgment": "",
                "method_summary": "",
                "evidence_strength": "",
                "baselines_checked": "",
                "datasets_checked": "",
                "metrics_checked": "",
                "limitations": "",
                "artifact_status_checked": "",
                "reproducibility_notes": "",
                "claim_implications": "",
                "taxonomy_correction": "",
                "representative_quote_or_result": "",
                "final_report_use": "",
                "reviewer_notes": "",
            }
        )
    rows.sort(key=lambda row: (row["sprint"], int(str(row["sprint_rank"]) or 999), row["event_id"]))
    return rows


def write_report(rows: list[dict[str, object]]) -> None:
    lines = [
        "# ICML 2026 PDF Review Worksheet",
        "",
        "Reviewer-ready worksheet for the bounded PDF subset. It joins source links, page-level navigation, claim decision tests, and blank paper-note fields.",
        "",
        "This is not a completed review. Blank judgment fields are intentional and should be filled after reading the PDF pages.",
        "",
        "## Snapshot",
        "",
        f"- Worksheet rows: {len(rows)}",
        f"- Claims covered: {len({claim.strip() for row in rows for claim in str(row['target_claims']).split(';') if claim.strip()})}",
        f"- Rows with artifact checks: {sum(str(row['github_url']).strip() != '' for row in rows)}",
        "",
        "## Review Order",
        "",
        "1. Open the PDF review card.",
        "2. Read method pages, then evidence pages, then limitation pages.",
        "3. Inspect artifact pages and repository when applicable.",
        "4. Fill the blank judgment fields in the worksheet or the canonical paper-note file.",
        "5. Transfer claim and taxonomy judgments through the overlay bridge.",
        "",
        "## Worksheet Rows",
        "",
        "| Sprint | Rank | Paper | Claims | Pages | Writeback |",
        "| --- | ---: | --- | --- | --- | --- |",
    ]
    for row in rows:
        pages = f"method {row['method_pages']}; evidence {row['evidence_pages']}; limitations {row['limitation_pages'] or 'not detected'}"
        lines.append(
            f"| {row['sprint']} | {row['sprint_rank']} | [{row['title']}]({row['pdf_card_path'].replace('reports/', '')}) | "
            f"{row['target_claims']} | {pages} | `{row['paper_note_file']}` |"
        )
    lines.extend(
        [
            "",
            "## Coded Values",
            "",
            "Use `reports/icml2026_manual_review_codebook.md` for allowed values. Do not invent coded values in `paper_read_status`, `novelty_judgment`, `evidence_strength`, `artifact_status_checked`, `taxonomy_correction`, or `final_report_use`.",
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_pdf_review_worksheet.csv`",
            "- `reports/icml2026_pdf_review_worksheet.md`",
        ]
    )
    (REPORTS / "icml2026_pdf_review_worksheet.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    rows = build_rows()
    fieldnames = [
        "event_id",
        "sprint",
        "sprint_rank",
        "title",
        "target_claims",
        "task_ids",
        "task_focuses",
        "local_pdf_path",
        "pdf_card_path",
        "brief_path",
        "paper_note_file",
        "icml_url",
        "openreview_url",
        "arxiv_pdf_url",
        "github_url",
        "method_pages",
        "evidence_pages",
        "limitation_pages",
        "artifact_pages",
        "claim_questions",
        "support_tests",
        "weakening_tests",
        "blocking_risks",
        "required_manual_fields",
        "read_order",
        "paper_read_status",
        "contribution_summary",
        "novelty_judgment",
        "method_summary",
        "evidence_strength",
        "baselines_checked",
        "datasets_checked",
        "metrics_checked",
        "limitations",
        "artifact_status_checked",
        "reproducibility_notes",
        "claim_implications",
        "taxonomy_correction",
        "representative_quote_or_result",
        "final_report_use",
        "reviewer_notes",
    ]
    write_csv(PROCESSED / "icml2026_pdf_review_worksheet.csv", rows, fieldnames)
    write_report(rows)
    print(f"Wrote {PROCESSED / 'icml2026_pdf_review_worksheet.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_pdf_review_worksheet.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
