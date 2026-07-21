#!/usr/bin/env python3
"""Build a focused first-sprint packet for manual paper review."""

from __future__ import annotations

import argparse
import csv
import re
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


def excerpt(text: str, limit: int = 700) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) <= limit:
        return text
    return text[: limit - 3].rsplit(" ", 1)[0] + "..."


def split_list(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def build_rows(limit: int) -> list[dict[str, object]]:
    plan = read_csv(PROCESSED / "icml2026_researcher_review_plan.csv")[:limit]
    claim_queue = read_csv(PROCESSED / "icml2026_claim_validation_queue.csv")
    area_queue = read_csv(PROCESSED / "icml2026_manual_validation_queue.csv")
    claim_by_event: dict[str, list[dict[str, str]]] = {}
    area_by_event: dict[str, list[dict[str, str]]] = {}
    for row in claim_queue:
        claim_by_event.setdefault(row["event_id"], []).append(row)
    for row in area_queue:
        area_by_event.setdefault(row["event_id"], []).append(row)

    rows: list[dict[str, object]] = []
    for row in plan:
        event_id = row["event_id"]
        claim_rows = claim_by_event.get(event_id, [])
        area_rows = area_by_event.get(event_id, [])
        seed = claim_rows[0] if claim_rows else area_rows[0]
        claim_overlay_keys = [
            f"{item['claim_id']}::{event_id}" for item in claim_rows
        ]
        area_overlay_keys = [
            f"{item['area']}::{event_id}" for item in area_rows
        ]
        rows.append(
            {
                "sprint_rank": row["global_review_rank"],
                "event_id": event_id,
                "title": row["title"],
                "review_phase": row["review_phase"],
                "area": row["area"],
                "subarea": row["subarea"],
                "claim_ids": row["claim_ids"],
                "why_first": row["priority_reason"],
                "claim_overlay_keys": " | ".join(claim_overlay_keys),
                "area_overlay_keys": " | ".join(area_overlay_keys),
                "claim_fields_to_fill": "manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes" if claim_rows else "",
                "area_fields_to_fill": "manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes" if area_rows else "",
                "review_focus": row["review_focus"],
                "claim_packet_links": row["claim_packet_links"],
                "claim_dossier_links": row["claim_dossier_links"],
                "area_packet_link": row["area_packet_link"],
                "area_briefing_link": row["area_briefing_link"],
                "signals": "; ".join(
                    part for part in [
                        "oral" if row["is_oral"] == "true" else "",
                        row["award"],
                        f"votes={row['public_total_votes']}" if row["public_total_votes"] else "",
                        f"github_stars={row['github_stars']}" if row["github_url"] else "",
                        "taxonomy_review" if row["taxonomy_review_status"] == "needs_review" else "",
                        "artifact_manual_check" if row["needs_manual_check_reason"] else "",
                        f"evidence={row['evidence_confidence']}" if row["evidence_confidence"] else "",
                    ]
                    if part
                ),
                "method_families": row["method_families"],
                "evaluation_settings": row["evaluation_settings"],
                "abstract_excerpt": excerpt(seed.get("abstract", "")),
                "icml_url": row["icml_url"],
                "alphaxiv_url": row["alphaxiv_url"],
                "github_url": row["github_url"],
            }
        )
    return rows


def write_report(rows: list[dict[str, object]], limit: int) -> None:
    phase_counts = Counter(str(row["review_phase"]) for row in rows)
    claim_rows = sum(bool(row["claim_overlay_keys"]) for row in rows)
    area_rows = sum(bool(row["area_overlay_keys"]) for row in rows)
    lines = [
        "# ICML 2026 Review Sprint 01",
        "",
        f"Focused manual-review packet for the top {limit} papers in the researcher review plan.",
        "This is a reading worksheet; judgments should be entered in `data/manual/claim_review_overrides.csv` and `data/manual/area_review_overrides.csv`.",
        "",
        "## Sprint Snapshot",
        "",
        f"- Papers: {len(rows)}",
        f"- Papers touching claim overlays: {claim_rows}",
        f"- Papers touching area overlays: {area_rows}",
        f"- Phase mix: {', '.join(f'{name}: {count}' for name, count in phase_counts.most_common())}",
        "",
        "## Execution Checklist",
        "",
        "1. Read the paper abstract and, when needed, the ICML/AlphaXiv page.",
        "2. Open the linked claim packet/dossier or area packet/card.",
        "3. Fill the overlay keys listed for that paper in `data/manual/`.",
        "4. Use `manual_notes` for concise evidence, corrections, and caveats.",
        "5. Re-run the progress/readiness pipeline after the sprint.",
        "",
        "## Papers",
        "",
    ]
    for row in rows:
        lines.extend(
            [
                f"### {row['sprint_rank']}. {row['title']}",
                "",
                f"- Phase: `{row['review_phase']}`",
                f"- Area: {row['area']} / {row['subarea']}",
                f"- Claims: {row['claim_ids'] or 'none'}",
                f"- Why first: {row['why_first']}",
                f"- Signals: {row['signals'] or 'none'}",
                f"- Claim overlay keys: {row['claim_overlay_keys'] or 'none'}",
                f"- Area overlay keys: {row['area_overlay_keys'] or 'none'}",
                f"- Claim fields: {row['claim_fields_to_fill'] or 'none'}",
                f"- Area fields: {row['area_fields_to_fill'] or 'none'}",
                f"- Claim packets: {row['claim_packet_links'] or 'none'}",
                f"- Claim dossiers: {row['claim_dossier_links'] or 'none'}",
                f"- Area packet: {row['area_packet_link'] or 'none'}",
                f"- Area briefing: {row['area_briefing_link'] or 'none'}",
                f"- URLs: [ICML]({row['icml_url']})" + (f" / [AlphaXiv]({row['alphaxiv_url']})" if row["alphaxiv_url"] else ""),
                "",
                "Abstract excerpt:",
                "",
                str(row["abstract_excerpt"]) or "No abstract excerpt available.",
                "",
                "Manual judgment prompts:",
                "- Does this paper support, weaken, or complicate the associated claim(s)?",
                "- Is the area/subarea assignment correct enough for report use?",
                "- Are artifact and benchmark/data/metric signals real after checking the source?",
                "- What exact sentence-level caveat should be carried into the final report?",
                "",
            ]
        )
    lines.extend(
        [
            "## Outputs",
            "",
            "- `data/processed/icml2026_review_sprint_01.csv`",
            "- `reports/icml2026_review_sprint_01.md`",
        ]
    )
    (REPORTS / "icml2026_review_sprint_01.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=40)
    args = parser.parse_args()
    rows = build_rows(args.limit)
    fieldnames = [
        "sprint_rank", "event_id", "title", "review_phase", "area", "subarea",
        "claim_ids", "why_first", "claim_overlay_keys", "area_overlay_keys",
        "claim_fields_to_fill", "area_fields_to_fill", "review_focus",
        "claim_packet_links", "claim_dossier_links", "area_packet_link",
        "area_briefing_link", "signals", "method_families", "evaluation_settings",
        "abstract_excerpt", "icml_url", "alphaxiv_url", "github_url",
    ]
    write_csv(PROCESSED / "icml2026_review_sprint_01.csv", rows, fieldnames)
    write_report(rows, args.limit)
    print(f"Wrote {PROCESSED / 'icml2026_review_sprint_01.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_review_sprint_01.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
