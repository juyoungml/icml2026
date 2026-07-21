#!/usr/bin/env python3
"""Build a paper source-access map for the ICML 2026 review sprints."""

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


def by_key(rows: list[dict[str, str]], key: str) -> dict[str, dict[str, str]]:
    return {row.get(key, ""): row for row in rows}


def split_semicolon(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def arxiv_pdf_url(arxiv_id: str) -> str:
    if not arxiv_id:
        return ""
    return f"https://arxiv.org/pdf/{arxiv_id}"


def access_status(row: dict[str, object]) -> str:
    if row.get("openreview_url") and row.get("arxiv_pdf_url") and row.get("github_url"):
        return "paper_pdf_artifact"
    if row.get("openreview_url") and row.get("arxiv_pdf_url"):
        return "paper_pdf"
    if row.get("openreview_url"):
        return "openreview_only"
    if row.get("arxiv_pdf_url"):
        return "arxiv_only"
    return "icml_page_only"


def build_rows() -> list[dict[str, object]]:
    briefs = read_csv(PROCESSED / "icml2026_sprint_reading_briefs.csv")
    tasks = read_csv(PROCESSED / "icml2026_review_decision_tasks.csv")
    papers = by_key(read_csv(PROCESSED / "icml2026_papers.csv"), "event_id")
    alphaxiv = by_key(read_csv(PROCESSED / "alphaxiv_icml2026_joined.csv"), "icml_id")

    tasks_by_event: dict[str, list[dict[str, str]]] = defaultdict(list)
    for task in tasks:
        tasks_by_event[task.get("event_id", "")].append(task)

    rows: list[dict[str, object]] = []
    for brief in briefs:
        event_id = brief["event_id"]
        official = papers.get(event_id, {})
        alpha = alphaxiv.get(event_id, {})
        event_tasks = sorted(tasks_by_event.get(event_id, []), key=lambda row: int(row.get("priority_rank") or 9999))
        claim_ids = [row.get("claim_id", "") for row in event_tasks]
        task_focuses = [row.get("task_focus", "") for row in event_tasks]
        required_fields: list[str] = []
        for task in event_tasks:
            for field in split_semicolon(task.get("required_manual_fields", "")):
                if field not in required_fields:
                    required_fields.append(field)
        arxiv_id = alpha.get("arxiv_id", "")
        row: dict[str, object] = {
            "event_id": event_id,
            "sprint": brief.get("sprint", ""),
            "sprint_rank": brief.get("sprint_rank", ""),
            "title": brief.get("title", ""),
            "area": brief.get("area", ""),
            "subarea": brief.get("subarea", ""),
            "target_claims": "; ".join(claim_ids),
            "task_focuses": "; ".join(dict.fromkeys(task_focuses)),
            "icml_url": brief.get("icml_url", "") or official.get("url", ""),
            "openreview_url": official.get("openreview_url", "") or official.get("paper_url", ""),
            "alphaxiv_url": brief.get("alphaxiv_url", "") or alpha.get("alphaxiv_url", ""),
            "arxiv_id": arxiv_id,
            "arxiv_abs_url": f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else "",
            "arxiv_pdf_url": arxiv_pdf_url(arxiv_id),
            "github_url": brief.get("github_url", "") or alpha.get("github_url", ""),
            "brief_path": brief.get("brief_path", ""),
            "paper_note_file": "data/manual/icml2026_review_sprint_02_paper_notes.csv"
            if brief.get("sprint") == "sprint_02"
            else "data/manual/icml2026_review_sprint_01_paper_notes.csv",
            "local_context": " ; ".join(
                part
                for part in [
                    brief.get("brief_path", ""),
                    brief.get("claim_packet_links", ""),
                    brief.get("claim_dossier_links", ""),
                    brief.get("area_briefing_link", ""),
                ]
                if part
            ),
            "required_extraction_fields": " ; ".join(required_fields),
            "pdf_review_checklist": "claim contribution; novelty delta; method mechanism; baselines; datasets; metrics; ablations or negative cases; limitations; taxonomy fit; claim implication; artifact status",
            "artifact_check_needed": "yes" if brief.get("github_url") or any(task.get("claim_id") == "C07" for task in event_tasks) else "no",
            "source_gap": "",
        }
        row["source_status"] = access_status(row)
        gaps = []
        if not row["openreview_url"]:
            gaps.append("missing_openreview")
        if not row["arxiv_pdf_url"]:
            gaps.append("missing_arxiv_pdf")
        if row["artifact_check_needed"] == "yes" and not row["github_url"]:
            gaps.append("artifact_expected_but_no_github")
        row["source_gap"] = "; ".join(gaps) if gaps else "none"
        rows.append(row)

    rows.sort(key=lambda row: (row["sprint"], int(str(row["sprint_rank"]) or 999), row["event_id"]))
    return rows


def write_report(rows: list[dict[str, object]]) -> None:
    status_counts = Counter(str(row["source_status"]) for row in rows)
    gap_counts = Counter(gap for row in rows for gap in split_semicolon(str(row["source_gap"])) if gap != "none")
    lines = [
        "# ICML 2026 Paper Source Access Map",
        "",
        "Access map for the sprint papers: official page, OpenReview, arXiv/PDF, artifact link, local brief, and extraction checklist.",
        "",
        "This does not certify that a PDF or repository was read. It only makes source acquisition and review writeback explicit.",
        "",
        "## Snapshot",
        "",
        f"- Sprint papers: {len(rows)}",
        f"- With OpenReview URL: {sum(bool(row['openreview_url']) for row in rows)}",
        f"- With arXiv PDF URL: {sum(bool(row['arxiv_pdf_url']) for row in rows)}",
        f"- With GitHub URL: {sum(bool(row['github_url']) for row in rows)}",
        f"- Access statuses: {', '.join(f'{status}={count}' for status, count in sorted(status_counts.items()))}",
        f"- Source gaps: {', '.join(f'{gap}={count}' for gap, count in sorted(gap_counts.items())) if gap_counts else 'none'}",
        "",
        "## First 20 Papers",
        "",
        "| Sprint | Rank | Paper | Claims | Access | Source gap |",
        "| --- | ---: | --- | --- | --- | --- |",
    ]
    for row in rows[:20]:
        access_parts = [
            f"[ICML]({row['icml_url']})" if row["icml_url"] else "ICML missing",
            f"[OpenReview]({row['openreview_url']})" if row["openreview_url"] else "OpenReview missing",
            f"[PDF]({row['arxiv_pdf_url']})" if row["arxiv_pdf_url"] else "PDF missing",
        ]
        if row["github_url"]:
            access_parts.append(f"[GitHub]({row['github_url']})")
        lines.append(
            f"| {row['sprint']} | {row['sprint_rank']} | {row['title']} | {row['target_claims']} | {' / '.join(access_parts)} | {row['source_gap']} |"
        )

    lines.extend(
        [
            "",
            "## Source-Gap Queue",
            "",
            "| Sprint | Rank | Paper | Gap | Fallback |",
            "| --- | ---: | --- | --- | --- |",
        ]
    )
    gap_rows = [row for row in rows if row["source_gap"] != "none"]
    for row in gap_rows:
        fallback = row["openreview_url"] or row["icml_url"] or row["alphaxiv_url"] or "manual search required"
        fallback_text = f"[fallback]({fallback})" if str(fallback).startswith("http") else fallback
        lines.append(f"| {row['sprint']} | {row['sprint_rank']} | {row['title']} | {row['source_gap']} | {fallback_text} |")
    if not gap_rows:
        lines.append("|  |  | none | none | none |")

    lines.extend(
        [
            "",
            "## Review Extraction Fields",
            "",
            "For every paper, extract: contribution, novelty, mechanism, baselines, datasets, metrics, ablations or negative cases, limitations, taxonomy fit, claim implication, and artifact status when applicable.",
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_paper_source_access_map.csv`",
            "- `reports/icml2026_paper_source_access_map.md`",
        ]
    )
    (REPORTS / "icml2026_paper_source_access_map.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    rows = build_rows()
    fieldnames = [
        "event_id",
        "sprint",
        "sprint_rank",
        "title",
        "area",
        "subarea",
        "target_claims",
        "task_focuses",
        "icml_url",
        "openreview_url",
        "alphaxiv_url",
        "arxiv_id",
        "arxiv_abs_url",
        "arxiv_pdf_url",
        "github_url",
        "source_status",
        "source_gap",
        "brief_path",
        "paper_note_file",
        "local_context",
        "required_extraction_fields",
        "pdf_review_checklist",
        "artifact_check_needed",
    ]
    write_csv(PROCESSED / "icml2026_paper_source_access_map.csv", rows, fieldnames)
    write_report(rows)
    print(f"Wrote {PROCESSED / 'icml2026_paper_source_access_map.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_paper_source_access_map.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
