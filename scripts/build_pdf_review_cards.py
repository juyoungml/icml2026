#!/usr/bin/env python3
"""Build page-level PDF review cards for probed ICML 2026 papers."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"
CARD_DIR = REPORTS / "pdf_review_cards"


SECTION_PATTERNS = {
    "introduction": r"\b1\.?\s+Introduction\b|\bIntroduction\b",
    "related_work": r"\bRelated Work\b",
    "method": r"\bMethod\b|\bMethods\b|\bApproach\b|\bAlgorithm\b|\bFramework\b",
    "experiment": r"\bExperiment\b|\bExperiments\b|\bEvaluation\b|\bEmpirical\b",
    "result": r"\bResult\b|\bResults\b|\bFindings\b",
    "ablation": r"\bAblation\b|\bAblations\b",
    "limitation": r"\bLimitations?\b|\bFailure Cases?\b|\bWeakness(es)?\b",
    "conclusion": r"\bConclusion\b|\bDiscussion\b",
}

EVIDENCE_CUES = {
    "baseline": r"\bbaseline(s)?\b",
    "ablation": r"\bablation(s)?\b",
    "dataset": r"\bdataset(s)?\b|\bdata set(s)?\b|\bbenchmark(s)?\b",
    "metric": r"\bmetric(s)?\b|\baccuracy\b|\bpass@k\b|\bwin rate\b|\bF1\b|\bAUC\b|\bBLEU\b",
    "limitation": r"\blimitation(s)?\b|\bfailure case(s)?\b|\bfuture work\b",
    "theorem": r"\btheorem\b|\bproof\b|\blemma\b|\bproposition\b",
    "artifact": r"\bcode\b|\bgithub\b|\brepository\b|\bimplementation\b|\brelease\b",
}


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


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def count_matches(patterns: dict[str, str], text: str) -> dict[str, int]:
    return {name: len(re.findall(pattern, text, flags=re.IGNORECASE)) for name, pattern in patterns.items()}


def top_pages(page_rows: list[dict[str, object]], score_fields: list[str], limit: int = 3) -> str:
    ranked = sorted(
        page_rows,
        key=lambda row: (
            -sum(int(row.get(field, 0) or 0) for field in score_fields),
            int(row.get("page_number", 999)),
        ),
    )
    selected = [
        f"p{row['page_number']}"
        for row in ranked
        if sum(int(row.get(field, 0) or 0) for field in score_fields) > 0
    ][:limit]
    return "; ".join(selected)


def pages_with_sections(page_rows: list[dict[str, object]], sections: set[str], limit: int = 3) -> str:
    selected = []
    for row in page_rows:
        found = set(str(row.get("section_hits", "")).split("; "))
        if sections.intersection(found):
            selected.append(f"p{row['page_number']}")
    return "; ".join(selected[:limit])


def review_flags(card: dict[str, object]) -> str:
    flags = []
    if not card["method_pages"]:
        flags.append("method_pages_not_detected")
    if not card["evidence_pages"]:
        flags.append("evidence_pages_not_detected")
    if not card["limitation_pages"]:
        flags.append("limitation_pages_not_detected")
    if card["artifact_check_needed"] == "yes" and not card["artifact_pages"]:
        flags.append("artifact_pages_not_detected")
    return "; ".join(flags) if flags else "none"


def build_page_rows(probe_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    page_rows: list[dict[str, object]] = []
    for probe in probe_rows:
        pdf_path = ROOT / probe.get("local_pdf_path", "")
        if not pdf_path.exists():
            continue
        reader = PdfReader(str(pdf_path))
        for idx, page in enumerate(reader.pages, start=1):
            try:
                text = clean(page.extract_text() or "")
            except Exception:
                text = ""
            section_counts = count_matches(SECTION_PATTERNS, text)
            cue_counts = count_matches(EVIDENCE_CUES, text)
            section_hits = [name for name, count in section_counts.items() if count > 0]
            row: dict[str, object] = {
                "event_id": probe["event_id"],
                "sprint": probe["sprint"],
                "sprint_rank": probe["sprint_rank"],
                "title": probe["title"],
                "page_number": idx,
                "text_chars": len(text),
                "section_hits": "; ".join(section_hits),
            }
            row.update({f"section_{name}": count for name, count in section_counts.items()})
            row.update({f"cue_{name}": count for name, count in cue_counts.items()})
            row["method_score"] = row["section_method"] + row["section_experiment"] + row["cue_theorem"]
            row["evidence_score"] = row["section_experiment"] + row["section_result"] + row["cue_baseline"] + row["cue_ablation"] + row["cue_dataset"] + row["cue_metric"]
            row["limitation_score"] = row["section_limitation"] + row["cue_limitation"]
            row["artifact_score"] = row["cue_artifact"]
            page_rows.append(row)
    return page_rows


def build_cards(probe_rows: list[dict[str, str]], page_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    source = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_paper_source_access_map.csv")}
    tasks_by_event: dict[str, list[str]] = {}
    for task in read_csv(PROCESSED / "icml2026_review_decision_tasks.csv"):
        tasks_by_event.setdefault(task["event_id"], []).append(task["task_id"])

    pages_by_event: dict[str, list[dict[str, object]]] = {}
    for page in page_rows:
        pages_by_event.setdefault(str(page["event_id"]), []).append(page)

    cards: list[dict[str, object]] = []
    for probe in probe_rows:
        event_id = probe["event_id"]
        pages = pages_by_event.get(event_id, [])
        source_row = source.get(event_id, {})
        card: dict[str, object] = {
            "event_id": event_id,
            "sprint": probe["sprint"],
            "sprint_rank": probe["sprint_rank"],
            "title": probe["title"],
            "target_claims": probe["target_claims"],
            "task_ids": "; ".join(tasks_by_event.get(event_id, [])),
            "page_count": probe["page_count"],
            "local_pdf_path": probe["local_pdf_path"],
            "paper_note_file": source_row.get("paper_note_file", ""),
            "brief_path": source_row.get("brief_path", ""),
            "method_pages": pages_with_sections(pages, {"method"}) or top_pages(pages, ["method_score"]),
            "evidence_pages": pages_with_sections(pages, {"experiment", "result", "ablation"}) or top_pages(pages, ["evidence_score"]),
            "limitation_pages": pages_with_sections(pages, {"limitation"}) or top_pages(pages, ["limitation_score"]),
            "artifact_pages": top_pages(pages, ["artifact_score"]),
            "artifact_check_needed": source_row.get("artifact_check_needed", ""),
            "required_manual_fields": source_row.get("required_extraction_fields", ""),
            "review_sequence": "1 contribution/novelty; 2 method; 3 evidence/baselines; 4 limitations; 5 taxonomy; 6 claim implication; 7 artifact if needed",
        }
        card["review_flags"] = review_flags(card)
        cards.append(card)
    return cards


def write_card_reports(cards: list[dict[str, object]], page_rows: list[dict[str, object]]) -> None:
    CARD_DIR.mkdir(parents=True, exist_ok=True)
    pages_by_event: dict[str, list[dict[str, object]]] = {}
    for row in page_rows:
        pages_by_event.setdefault(str(row["event_id"]), []).append(row)

    for card in cards:
        pages = pages_by_event.get(str(card["event_id"]), [])
        lines = [
            f"# {card['title']}",
            "",
            f"- Event ID: `{card['event_id']}`",
            f"- Sprint: `{card['sprint']}` rank {card['sprint_rank']}",
            f"- Target claims: {card['target_claims']}",
            f"- Local PDF: `{card['local_pdf_path']}`",
            f"- Paper-note file: `{card['paper_note_file']}`",
            f"- Brief: `{card['brief_path']}`",
            f"- Review flags: {card['review_flags']}",
            "",
            "## Suggested Page Pass",
            "",
            f"- Method/mechanism pages: {card['method_pages'] or 'not detected'}",
            f"- Evidence/result pages: {card['evidence_pages'] or 'not detected'}",
            f"- Limitation pages: {card['limitation_pages'] or 'not detected'}",
            f"- Artifact pages: {card['artifact_pages'] or 'not detected'}",
            "",
            "## Page Cue Table",
            "",
            "| Page | Chars | Sections | Evidence score | Limitation score | Artifact score |",
            "| ---: | ---: | --- | ---: | ---: | ---: |",
        ]
        for page in pages:
            if int(page.get("evidence_score", 0) or 0) or int(page.get("method_score", 0) or 0) or int(page.get("artifact_score", 0) or 0) or int(page.get("limitation_score", 0) or 0):
                lines.append(
                    f"| {page['page_number']} | {page['text_chars']} | {page['section_hits'] or 'none'} | "
                    f"{page['evidence_score']} | {page['limitation_score']} | {page['artifact_score']} |"
                )
        lines.extend(
            [
                "",
                "## Writeback",
                "",
                "Use this card only to navigate the PDF. Put judgments in the paper-note file and overlay files.",
            ]
        )
        path = CARD_DIR / f"{card['event_id']}.md"
        path.write_text("\n".join(lines), encoding="utf-8")


def write_index_report(cards: list[dict[str, object]], page_rows: list[dict[str, object]]) -> None:
    flags = Counter(str(card["review_flags"]) for card in cards)
    lines = [
        "# ICML 2026 PDF Review Cards",
        "",
        "Page-level navigation cards for the bounded PDF extraction subset.",
        "",
        "These cards do not contain paper prose and do not make review judgments. They point reviewers to likely method, evidence, limitation, and artifact pages.",
        "",
        "## Snapshot",
        "",
        f"- Cards: {len(cards)}",
        f"- Page cue rows: {len(page_rows)}",
        f"- Review-flag states: {', '.join(f'{key}={value}' for key, value in sorted(flags.items()))}",
        "",
        "## Cards",
        "",
        "| Sprint | Rank | Paper | Claims | Method | Evidence | Limitations | Artifact | Flags |",
        "| --- | ---: | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for card in cards:
        link = f"pdf_review_cards/{card['event_id']}.md"
        lines.append(
            f"| {card['sprint']} | {card['sprint_rank']} | [{card['title']}]({link}) | {card['target_claims']} | "
            f"{card['method_pages'] or 'not detected'} | {card['evidence_pages'] or 'not detected'} | "
            f"{card['limitation_pages'] or 'not detected'} | {card['artifact_pages'] or 'not detected'} | {card['review_flags']} |"
        )
    lines.extend(
        [
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_pdf_review_cards.csv`",
            "- `data/processed/icml2026_pdf_page_cues.csv`",
            "- `reports/icml2026_pdf_review_cards.md`",
            "- `reports/pdf_review_cards/*.md`",
        ]
    )
    (REPORTS / "icml2026_pdf_review_cards.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    probe_rows = [row for row in read_csv(PROCESSED / "icml2026_pdf_extraction_probe.csv") if row.get("extract_status") == "ok"]
    page_rows = build_page_rows(probe_rows)
    cards = build_cards(probe_rows, page_rows)

    page_fieldnames = [
        "event_id",
        "sprint",
        "sprint_rank",
        "title",
        "page_number",
        "text_chars",
        "section_hits",
        *[f"section_{name}" for name in SECTION_PATTERNS],
        *[f"cue_{name}" for name in EVIDENCE_CUES],
        "method_score",
        "evidence_score",
        "limitation_score",
        "artifact_score",
    ]
    card_fieldnames = [
        "event_id",
        "sprint",
        "sprint_rank",
        "title",
        "target_claims",
        "task_ids",
        "page_count",
        "local_pdf_path",
        "paper_note_file",
        "brief_path",
        "method_pages",
        "evidence_pages",
        "limitation_pages",
        "artifact_pages",
        "artifact_check_needed",
        "required_manual_fields",
        "review_sequence",
        "review_flags",
    ]
    write_csv(PROCESSED / "icml2026_pdf_page_cues.csv", page_rows, page_fieldnames)
    write_csv(PROCESSED / "icml2026_pdf_review_cards.csv", cards, card_fieldnames)
    write_card_reports(cards, page_rows)
    write_index_report(cards, page_rows)
    print(f"Wrote {PROCESSED / 'icml2026_pdf_page_cues.csv'} ({len(page_rows)} rows)")
    print(f"Wrote {PROCESSED / 'icml2026_pdf_review_cards.csv'} ({len(cards)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_pdf_review_cards.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
