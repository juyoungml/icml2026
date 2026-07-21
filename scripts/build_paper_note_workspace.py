#!/usr/bin/env python3
"""Create a human-editable paper-note workspace for first-sprint ICML 2026 review."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
MANUAL = ROOT / "data" / "manual"
REPORTS = ROOT / "reports"


MANUAL_FIELDS = [
    "reviewer",
    "review_date",
    "review_source",
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
    "paper_note",
]


FIELDNAMES = [
    "event_id",
    "sprint_rank",
    "review_phase",
    "title",
    "area",
    "subarea",
    "claim_ids",
    "why_first",
    "signals",
    "method_families",
    "evaluation_settings",
    "benchmark_mentions",
    "dataset_mentions",
    "metric_mentions",
    "claim_overlay_keys",
    "area_overlay_keys",
    "icml_url",
    "alphaxiv_url",
    "github_url",
    *MANUAL_FIELDS,
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


def nonempty(value: str) -> bool:
    return bool((value or "").strip())


def existing_notes(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    return {row.get("event_id", ""): row for row in read_csv(path)}


def build_rows(force: bool) -> tuple[list[dict[str, object]], int]:
    sprint = read_csv(PROCESSED / "icml2026_review_sprint_01.csv")
    explorer = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_paper_explorer.csv")}
    old = {} if force else existing_notes(MANUAL / "icml2026_review_sprint_01_paper_notes.csv")
    preserved = 0
    rows: list[dict[str, object]] = []

    for row in sprint:
        paper = explorer.get(row["event_id"], {})
        note = old.get(row["event_id"], {})
        out: dict[str, object] = {
            "event_id": row["event_id"],
            "sprint_rank": row["sprint_rank"],
            "review_phase": row["review_phase"],
            "title": row["title"],
            "area": row["area"],
            "subarea": row["subarea"],
            "claim_ids": row["claim_ids"],
            "why_first": row["why_first"],
            "signals": row["signals"],
            "method_families": row["method_families"],
            "evaluation_settings": row["evaluation_settings"],
            "benchmark_mentions": paper.get("benchmark_mentions", ""),
            "dataset_mentions": paper.get("dataset_mentions", ""),
            "metric_mentions": paper.get("metric_mentions", ""),
            "claim_overlay_keys": row["claim_overlay_keys"],
            "area_overlay_keys": row["area_overlay_keys"],
            "icml_url": row["icml_url"],
            "alphaxiv_url": row["alphaxiv_url"],
            "github_url": row["github_url"],
        }
        for field in MANUAL_FIELDS:
            value = note.get(field, "")
            if nonempty(value):
                preserved += 1
            out[field] = value
        rows.append(out)
    return rows, preserved


def note_complete(row: dict[str, object]) -> bool:
    return any(nonempty(str(row.get(field, ""))) for field in MANUAL_FIELDS)


def write_report(rows: list[dict[str, object]], preserved: int, force: bool) -> None:
    complete = sum(note_complete(row) for row in rows)
    lines = [
        "# ICML 2026 Paper Note Workspace",
        "",
        "Human-editable paper-note sheet for the first review sprint.",
        "Use this to capture researcher judgments that are too rich for the claim and area overlay fields.",
        "",
        "## Snapshot",
        "",
        f"- Sprint papers: {len(rows)}",
        f"- Paper notes started: {complete}/{len(rows)}",
        f"- Manual field values preserved during rebuild: {preserved}",
        f"- Force overwrite used: {'yes' if force else 'no'}",
        "",
        "## File",
        "",
        "- `data/manual/icml2026_review_sprint_01_paper_notes.csv`",
        "- Suggested starting prompts: `data/processed/icml2026_sprint_prereview_suggestions.csv`",
        "- Overlay transfer checklist: `data/processed/icml2026_paper_note_overlay_bridge.csv`",
        "- Canonical codebook: `reports/icml2026_manual_review_codebook.md`",
        "",
        "## Fields To Fill",
        "",
        "- `paper_read_status`: abstract_only, skimmed, read_main, read_full, blocked.",
        "- `contribution_summary`: one or two sentences on what the paper actually contributes.",
        "- `novelty_judgment`: new_problem, new_method, stronger_theory, better_system, benchmark_package, incremental, unclear.",
        "- `method_summary`: compact mechanism-level description, not just the title phrasing.",
        "- `evidence_strength`: strong, moderate, weak, negative_or_mixed, unclear.",
        "- `baselines_checked`, `datasets_checked`, `metrics_checked`: what was actually compared or measured.",
        "- `limitations`: stated or inferred limitations that should affect the report narrative.",
        "- `artifact_status_checked`: none, linked_unchecked, live_checked, runnable, broken, not_applicable.",
        "- `claim_implications`: how the paper changes the linked synthesis claim(s).",
        "- `taxonomy_correction`: keep, relabel_area, relabel_subarea, split_boundary, unclear.",
        "- `final_report_use`: headline_example, supporting_example, caveat_example, exclude, undecided.",
        "",
        "## How This Fits The Workflow",
        "",
        "1. Fill paper notes while reading the top-40 sprint papers.",
        "2. Use the pre-review suggestions as hypotheses, not as checked judgments.",
        "3. Rebuild the paper-note overlay bridge.",
        "4. Transfer direct claim/area judgments into the overlay files listed in the bridge rows.",
        "5. Rebuild reviewed tables, progress, readiness, gap audit, dashboard, and validation.",
        "",
        "```bash",
        "python3 scripts/build_manual_review_codebook.py",
        "python3 scripts/build_paper_note_overlay_bridge.py",
        "python3 scripts/lint_manual_review_values.py",
        "python3 scripts/build_reviewed_validation_tables.py",
        "python3 scripts/build_review_progress.py",
        "python3 scripts/build_researcher_readiness_audit.py",
        "python3 scripts/build_researcher_gap_audit.py",
        "python3 scripts/build_project_index.py",
        "python3 scripts/validate_workspace.py",
        "```",
    ]
    (REPORTS / "icml2026_paper_note_workspace.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="clear existing manual paper-note fields")
    args = parser.parse_args()
    rows, preserved = build_rows(args.force)
    write_csv(MANUAL / "icml2026_review_sprint_01_paper_notes.csv", rows, FIELDNAMES)
    write_report(rows, preserved, args.force)
    print(f"Wrote {MANUAL / 'icml2026_review_sprint_01_paper_notes.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_paper_note_workspace.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
