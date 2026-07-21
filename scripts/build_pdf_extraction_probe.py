#!/usr/bin/env python3
"""Probe PDF availability and extractability for prioritized ICML 2026 sprint papers."""

from __future__ import annotations

import argparse
import csv
import re
import time
from collections import Counter
from pathlib import Path

import requests
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
RAW = ROOT / "data" / "raw" / "pdf_probe"
REPORTS = ROOT / "reports"

USER_AGENT = "icml2026-research-workspace/0.1 (source availability probe)"

SECTION_PATTERNS = {
    "introduction": r"\b1\.?\s+Introduction\b|\bIntroduction\b",
    "related_work": r"\bRelated Work\b",
    "method": r"\bMethod\b|\bMethods\b|\bApproach\b|\bAlgorithm\b",
    "experiment": r"\bExperiment\b|\bExperiments\b|\bEvaluation\b",
    "result": r"\bResult\b|\bResults\b",
    "ablation": r"\bAblation\b|\bAblations\b",
    "limitation": r"\bLimitations?\b|\bFailure Cases?\b",
    "conclusion": r"\bConclusion\b|\bDiscussion\b",
}

EVIDENCE_CUES = {
    "baseline": r"\bbaseline(s)?\b",
    "ablation": r"\bablation(s)?\b",
    "dataset": r"\bdataset(s)?\b|\bdata set(s)?\b",
    "metric": r"\bmetric(s)?\b|\baccuracy\b|\bpass@k\b|\bwin rate\b|\bF1\b",
    "limitation": r"\blimitation(s)?\b|\bfailure case(s)?\b",
    "theorem": r"\btheorem\b|\bproof\b|\blemma\b",
    "artifact": r"\bcode\b|\bgithub\b|\brepository\b|\bimplementation\b",
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


def download_pdf(url: str, path: Path, refresh: bool = False) -> tuple[str, int, str]:
    if path.exists() and path.stat().st_size > 10_000 and not refresh:
        return "cached", path.stat().st_size, ""
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
        if response.status_code != 200:
            return f"http_{response.status_code}", 0, response.text[:200]
        content_type = response.headers.get("content-type", "")
        content = response.content
        if len(content) < 10_000 or not content.startswith(b"%PDF"):
            return "not_pdf", len(content), content_type
        path.write_bytes(content)
        time.sleep(0.25)
        return "downloaded", len(content), ""
    except requests.RequestException as exc:
        return "request_error", 0, str(exc)


def extract_pdf(path: Path, max_pages: int = 4) -> dict[str, object]:
    try:
        reader = PdfReader(str(path))
        page_count = len(reader.pages)
        texts = []
        for page in reader.pages[:max_pages]:
            try:
                texts.append(page.extract_text() or "")
            except Exception:
                texts.append("")
        sample = clean("\n".join(texts))
        lowered = sample.lower()
        sections = [
            name
            for name, pattern in SECTION_PATTERNS.items()
            if re.search(pattern, sample, flags=re.IGNORECASE)
        ]
        cue_counts = {
            name: len(re.findall(pattern, lowered, flags=re.IGNORECASE))
            for name, pattern in EVIDENCE_CUES.items()
        }
        return {
            "extract_status": "ok" if sample else "empty_text",
            "page_count": page_count,
            "sample_text_chars": len(sample),
            "detected_sections": "; ".join(sections),
            "evidence_cue_counts": "; ".join(f"{name}={count}" for name, count in cue_counts.items()),
            "extraction_error": "",
        }
    except Exception as exc:
        return {
            "extract_status": "extract_error",
            "page_count": "",
            "sample_text_chars": 0,
            "detected_sections": "",
            "evidence_cue_counts": "",
            "extraction_error": str(exc),
        }


def build_rows(limit: int, refresh: bool) -> list[dict[str, object]]:
    source_rows = [row for row in read_csv(PROCESSED / "icml2026_paper_source_access_map.csv") if row.get("arxiv_pdf_url")]
    source_rows.sort(key=lambda row: (row.get("sprint", ""), int(row.get("sprint_rank") or 999)))
    selected = source_rows[:limit]
    rows: list[dict[str, object]] = []
    for row in selected:
        event_id = row["event_id"]
        pdf_path = RAW / f"{event_id}.pdf"
        download_status, pdf_bytes, download_error = download_pdf(row["arxiv_pdf_url"], pdf_path, refresh=refresh)
        extracted = (
            extract_pdf(pdf_path)
            if download_status in {"downloaded", "cached"} and pdf_path.exists()
            else {
                "extract_status": "not_attempted",
                "page_count": "",
                "sample_text_chars": 0,
                "detected_sections": "",
                "evidence_cue_counts": "",
                "extraction_error": "",
            }
        )
        rows.append(
            {
                "event_id": event_id,
                "sprint": row.get("sprint", ""),
                "sprint_rank": row.get("sprint_rank", ""),
                "title": row.get("title", ""),
                "target_claims": row.get("target_claims", ""),
                "task_focuses": row.get("task_focuses", ""),
                "arxiv_id": row.get("arxiv_id", ""),
                "arxiv_pdf_url": row.get("arxiv_pdf_url", ""),
                "local_pdf_path": str(pdf_path.relative_to(ROOT)) if pdf_path.exists() else "",
                "download_status": download_status,
                "pdf_bytes": pdf_bytes,
                "download_error": download_error,
                **extracted,
                "manual_review_next_step": "Open PDF and complete contribution, novelty, method, evidence, limitation, taxonomy, claim, and artifact fields.",
            }
        )
    return rows


def write_report(rows: list[dict[str, object]]) -> None:
    download_counts = Counter(str(row["download_status"]) for row in rows)
    extract_counts = Counter(str(row["extract_status"]) for row in rows)
    lines = [
        "# ICML 2026 PDF Extraction Probe",
        "",
        "Bounded source-extraction probe for prioritized sprint papers with arXiv PDF URLs.",
        "",
        "This is not a paper review and does not promote any claim. It checks whether the workflow can obtain PDFs and extract enough structure to support manual review.",
        "",
        "## Snapshot",
        "",
        f"- Probe rows: {len(rows)}",
        f"- Download statuses: {', '.join(f'{key}={value}' for key, value in sorted(download_counts.items()))}",
        f"- Extraction statuses: {', '.join(f'{key}={value}' for key, value in sorted(extract_counts.items()))}",
        f"- Extracted text rows: {sum(int(row.get('sample_text_chars', 0) or 0) > 500 for row in rows)}",
        "",
        "## Probed Papers",
        "",
        "| Sprint | Rank | Paper | Claims | Download | Pages | Sections | Evidence cues |",
        "| --- | ---: | --- | --- | --- | ---: | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['sprint']} | {row['sprint_rank']} | {row['title']} | {row['target_claims']} | "
            f"{row['download_status']} / {row['extract_status']} | {row['page_count']} | "
            f"{row['detected_sections'] or 'none'} | {row['evidence_cue_counts'] or 'none'} |"
        )
    lines.extend(
        [
            "",
            "## Use",
            "",
            "Use this as a source-readiness check only. Actual judgments still belong in the sprint paper-note CSVs and manual overlay files.",
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_pdf_extraction_probe.csv`",
            "- `reports/icml2026_pdf_extraction_probe.md`",
            "- `data/raw/pdf_probe/*.pdf` for cached probe PDFs",
        ]
    )
    (REPORTS / "icml2026_pdf_extraction_probe.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=8, help="Number of source-map rows with arXiv PDFs to probe.")
    parser.add_argument("--refresh", action="store_true", help="Redownload PDFs even if cached.")
    args = parser.parse_args()
    rows = build_rows(limit=args.limit, refresh=args.refresh)
    fieldnames = [
        "event_id",
        "sprint",
        "sprint_rank",
        "title",
        "target_claims",
        "task_focuses",
        "arxiv_id",
        "arxiv_pdf_url",
        "local_pdf_path",
        "download_status",
        "pdf_bytes",
        "download_error",
        "extract_status",
        "page_count",
        "sample_text_chars",
        "detected_sections",
        "evidence_cue_counts",
        "extraction_error",
        "manual_review_next_step",
    ]
    write_csv(PROCESSED / "icml2026_pdf_extraction_probe.csv", rows, fieldnames)
    write_report(rows)
    print(f"Wrote {PROCESSED / 'icml2026_pdf_extraction_probe.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_pdf_extraction_probe.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
