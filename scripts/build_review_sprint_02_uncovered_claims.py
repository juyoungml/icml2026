#!/usr/bin/env python3
"""Build a second review sprint for claims missing first-sprint coverage."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
MANUAL = ROOT / "data" / "manual"
REPORTS = ROOT / "reports"

TARGET_CLAIMS = ["C04", "C05"]
PER_CLAIM_LIMIT = 8

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


def clip(text: str, limit: int = 500) -> str:
    text = clean(text)
    if len(text) <= limit:
        return text
    return text[: limit - 3].rsplit(" ", 1)[0] + "..."


def split_list(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def contains_claim(row: dict[str, str], claim_id: str) -> bool:
    return claim_id in split_list(row.get("claim_ids", ""))


def selected_review_plan_rows() -> list[dict[str, str]]:
    plan = read_csv(PROCESSED / "icml2026_researcher_review_plan.csv")
    selected: dict[str, dict[str, str]] = {}
    for claim_id in TARGET_CLAIMS:
        rows = [row for row in plan if contains_claim(row, claim_id)]
        rows.sort(key=lambda row: int(float(row.get("global_review_rank", "9999") or 9999)))
        for row in rows[:PER_CLAIM_LIMIT]:
            selected[row["event_id"]] = row
    return sorted(selected.values(), key=lambda row: int(float(row.get("global_review_rank", "9999") or 9999)))


def build_sprint_rows() -> list[dict[str, object]]:
    selected = selected_review_plan_rows()
    claim_queue = read_csv(PROCESSED / "icml2026_claim_validation_queue.csv")
    area_queue = read_csv(PROCESSED / "icml2026_manual_validation_queue.csv")
    claim_by_event: dict[str, list[dict[str, str]]] = defaultdict(list)
    area_by_event: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in claim_queue:
        claim_by_event[row["event_id"]].append(row)
    for row in area_queue:
        area_by_event[row["event_id"]].append(row)

    rows: list[dict[str, object]] = []
    for sprint_rank, row in enumerate(selected, start=1):
        event_id = row["event_id"]
        claim_rows = claim_by_event[event_id]
        area_rows = area_by_event.get(event_id, [])
        seed = claim_rows[0] if claim_rows else (area_rows[0] if area_rows else row)
        target_claims = [claim_id for claim_id in TARGET_CLAIMS if contains_claim(row, claim_id)]
        rows.append(
            {
                "sprint_rank": sprint_rank,
                "global_review_rank": row["global_review_rank"],
                "target_claims": "; ".join(target_claims),
                "event_id": event_id,
                "title": row["title"],
                "review_phase": row["review_phase"],
                "area": row["area"],
                "subarea": row["subarea"],
                "claim_ids": row["claim_ids"],
                "why_in_sprint": (
                    "claim missing sprint-01 coverage; "
                    f"targets {', '.join(target_claims)}; {row['priority_reason']}"
                ),
                "claim_overlay_keys": " | ".join(f"{item['claim_id']}::{event_id}" for item in claim_rows),
                "area_overlay_keys": " | ".join(f"{item['area']}::{event_id}" for item in area_rows),
                "claim_fields_to_fill": "manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes",
                "area_fields_to_fill": (
                    "manual_validated; manual_primary_contribution_type; manual_method_family; "
                    "manual_artifact_status; manual_fault_line_relevance; manual_notes"
                    if area_rows else ""
                ),
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
                "abstract_excerpt": clip(seed.get("abstract", "")),
                "icml_url": row["icml_url"],
                "alphaxiv_url": row["alphaxiv_url"],
                "github_url": row["github_url"],
            }
        )
    return rows


def write_sprint(rows: list[dict[str, object]]) -> None:
    fieldnames = [
        "sprint_rank", "global_review_rank", "target_claims", "event_id", "title",
        "review_phase", "area", "subarea", "claim_ids", "why_in_sprint",
        "claim_overlay_keys", "area_overlay_keys", "claim_fields_to_fill",
        "area_fields_to_fill", "review_focus", "claim_packet_links",
        "claim_dossier_links", "area_packet_link", "area_briefing_link",
        "signals", "method_families", "evaluation_settings", "abstract_excerpt",
        "icml_url", "alphaxiv_url", "github_url",
    ]
    write_csv(PROCESSED / "icml2026_review_sprint_02.csv", rows, fieldnames)
    phase_counts = Counter(str(row["review_phase"]) for row in rows)
    claim_counts = Counter(
        claim_id for row in rows for claim_id in split_list(str(row["target_claims"]))
    )
    lines = [
        "# ICML 2026 Review Sprint 02",
        "",
        "Focused second sprint for claims that had no first-sprint paper-note coverage.",
        "",
        "## Sprint Snapshot",
        "",
        f"- Papers: {len(rows)}",
        f"- Target claims: {', '.join(f'{key}: {value}' for key, value in claim_counts.items())}",
        f"- Phase mix: {', '.join(f'{key}: {value}' for key, value in phase_counts.most_common())}",
        "",
        "## Papers",
        "",
    ]
    for row in rows:
        lines.extend(
            [
                f"### {row['sprint_rank']}. {row['title']}",
                "",
                f"- Global review rank: {row['global_review_rank']}",
                f"- Target claims: {row['target_claims']}",
                f"- Area: {row['area']} / {row['subarea']}",
                f"- Why in sprint: {row['why_in_sprint']}",
                f"- Claim overlay keys: {row['claim_overlay_keys']}",
                f"- Area overlay keys: {row['area_overlay_keys'] or 'none'}",
                f"- Signals: {row['signals'] or 'none'}",
                f"- Claim packets: {row['claim_packet_links'] or 'none'}",
                f"- URLs: [ICML]({row['icml_url']})"
                + (f" / [AlphaXiv]({row['alphaxiv_url']})" if row["alphaxiv_url"] else ""),
                "",
                "Abstract excerpt:",
                "",
                str(row["abstract_excerpt"]) or "No abstract excerpt available.",
                "",
            ]
        )
    lines.extend(
        [
            "## Outputs",
            "",
            "- `data/processed/icml2026_review_sprint_02.csv`",
            "- `reports/icml2026_review_sprint_02.md`",
        ]
    )
    (REPORTS / "icml2026_review_sprint_02.md").write_text("\n".join(lines), encoding="utf-8")


def contribution_prompt(row: dict[str, object]) -> str:
    claim_text = str(row["target_claims"])
    if "C04" in claim_text:
        return "Label whether this robotics/world-model paper is mainly benchmark, demo, reusable model, or core algorithmic contribution."
    if "C05" in claim_text:
        return "Break the multimodal/vision contribution into submode: video, 3D/spatial, multimodal reasoning, robustness, or general vision-language."
    return "Identify the actual contribution and whether it supports the linked claim."


def write_prereview(rows: list[dict[str, object]]) -> None:
    out = []
    for row in rows:
        out.append(
            {
                "sprint_rank": row["sprint_rank"],
                "event_id": row["event_id"],
                "title": row["title"],
                "target_claims": row["target_claims"],
                "area": row["area"],
                "subarea": row["subarea"],
                "contribution_check": contribution_prompt(row),
                "evidence_to_verify": "Check baselines, datasets, metrics, ablations, negative cases, and whether artifact links support the claim.",
                "taxonomy_question": row["review_focus"] or "Check whether the assigned area/subarea is accurate enough for report use.",
                "artifact_check_prompt": (
                    "Open GitHub/project link and record code/data/checkpoint/runnable status."
                    if row["github_url"] else "No GitHub URL in metadata; record none/not_applicable unless the PDF shows a release."
                ),
                "suggested_note_seed": clip(
                    f"Contribution check: {contribution_prompt(row)} Evidence: inspect baselines, data, metrics, and limitations. "
                    f"Claim implication: decide supports / weakens / complicates / not_applicable for {row['target_claims']}."
                ),
                "abstract_basis": row["abstract_excerpt"],
            }
        )
    fieldnames = [
        "sprint_rank", "event_id", "title", "target_claims", "area", "subarea",
        "contribution_check", "evidence_to_verify", "taxonomy_question",
        "artifact_check_prompt", "suggested_note_seed", "abstract_basis",
    ]
    write_csv(PROCESSED / "icml2026_sprint_02_prereview_suggestions.csv", out, fieldnames)
    lines = [
        "# ICML 2026 Sprint 02 Pre-Review Suggestions",
        "",
        "Machine-generated prompts for the uncovered-claim sprint.",
        "",
        f"- Sprint papers covered: {len(out)}",
        "",
        "| Rank | Paper | Target claims | Contribution check |",
        "| ---: | --- | --- | --- |",
    ]
    for row in out:
        lines.append(f"| {row['sprint_rank']} | {row['title']} | {row['target_claims']} | {row['contribution_check']} |")
    lines.extend(
        [
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_sprint_02_prereview_suggestions.csv`",
            "- `reports/icml2026_sprint_02_prereview_suggestions.md`",
        ]
    )
    (REPORTS / "icml2026_sprint_02_prereview_suggestions.md").write_text("\n".join(lines), encoding="utf-8")


def existing_notes() -> dict[str, dict[str, str]]:
    path = MANUAL / "icml2026_review_sprint_02_paper_notes.csv"
    if not path.exists():
        return {}
    return {row.get("event_id", ""): row for row in read_csv(path)}


def write_notes(rows: list[dict[str, object]]) -> None:
    old = existing_notes()
    explorer = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_paper_explorer.csv")}
    out = []
    preserved = 0
    for row in rows:
        note = old.get(str(row["event_id"]), {})
        paper = explorer.get(str(row["event_id"]), {})
        item = {
            "event_id": row["event_id"],
            "sprint_rank": row["sprint_rank"],
            "global_review_rank": row["global_review_rank"],
            "target_claims": row["target_claims"],
            "review_phase": row["review_phase"],
            "title": row["title"],
            "area": row["area"],
            "subarea": row["subarea"],
            "claim_ids": row["claim_ids"],
            "why_in_sprint": row["why_in_sprint"],
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
            if str(value).strip():
                preserved += 1
            item[field] = value
        out.append(item)

    fieldnames = [
        "event_id", "sprint_rank", "global_review_rank", "target_claims",
        "review_phase", "title", "area", "subarea", "claim_ids", "why_in_sprint",
        "signals", "method_families", "evaluation_settings", "benchmark_mentions",
        "dataset_mentions", "metric_mentions", "claim_overlay_keys", "area_overlay_keys",
        "icml_url", "alphaxiv_url", "github_url", *MANUAL_FIELDS,
    ]
    write_csv(MANUAL / "icml2026_review_sprint_02_paper_notes.csv", out, fieldnames)
    lines = [
        "# ICML 2026 Sprint 02 Paper Note Workspace",
        "",
        "Human-editable notes for the uncovered-claim sprint focused on C04 and C05.",
        "",
        f"- Sprint papers: {len(out)}",
        f"- Manual field values preserved during rebuild: {preserved}",
        "",
        "## Files",
        "",
        "- `data/manual/icml2026_review_sprint_02_paper_notes.csv`",
        "- `data/processed/icml2026_sprint_02_prereview_suggestions.csv`",
        "- `data/processed/icml2026_sprint_02_overlay_bridge.csv`",
        "- `reports/icml2026_manual_review_codebook.md`",
        "",
        "## Use The Codebook",
        "",
        "Use canonical values from `reports/icml2026_manual_review_codebook.md` for `paper_read_status`, `evidence_strength`, `taxonomy_correction`, `final_report_use`, and overlay-transfer decisions.",
    ]
    (REPORTS / "icml2026_sprint_02_paper_note_workspace.md").write_text("\n".join(lines), encoding="utf-8")


def note_status(row: dict[str, str]) -> str:
    if not any((row.get(field, "") or "").strip() for field in MANUAL_FIELDS):
        return "pending_note"
    if row.get("paper_read_status") == "blocked":
        return "blocked"
    if (row.get("claim_implications", "") or row.get("taxonomy_correction", "")).strip():
        return "ready_for_overlay_transfer"
    return "note_started_needs_decision"


def write_bridge() -> None:
    notes = read_csv(MANUAL / "icml2026_review_sprint_02_paper_notes.csv")
    claim_keys = {f"{row['claim_id']}::{row['event_id']}" for row in read_csv(MANUAL / "claim_review_overrides.csv")}
    area_keys = {f"{row['area']}::{row['event_id']}" for row in read_csv(MANUAL / "area_review_overrides.csv")}
    rows = []
    for note in notes:
        for key in [part.strip() for part in note.get("claim_overlay_keys", "").split("|") if part.strip()]:
            rows.append(
                {
                    "target_type": "claim",
                    "target_file": "data/manual/claim_review_overrides.csv",
                    "overlay_key": key,
                    "target_present": str(key in claim_keys).lower(),
                    "event_id": note["event_id"],
                    "sprint_rank": note["sprint_rank"],
                    "title": note["title"],
                    "target_claims": note["target_claims"],
                    "claim_id": key.split("::", 1)[0],
                    "note_status": note_status(note),
                    "blocking_gap": "paper note not started" if note_status(note) == "pending_note" else "ready to inspect",
                    "source_fields_to_read": "claim_implications; taxonomy_correction; artifact_status_checked; evidence_strength; limitations; final_report_use",
                    "overlay_fields_to_update": "manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes",
                }
            )
        for key in [part.strip() for part in note.get("area_overlay_keys", "").split("|") if part.strip()]:
            rows.append(
                {
                    "target_type": "area",
                    "target_file": "data/manual/area_review_overrides.csv",
                    "overlay_key": key,
                    "target_present": str(key in area_keys).lower(),
                    "event_id": note["event_id"],
                    "sprint_rank": note["sprint_rank"],
                    "title": note["title"],
                    "target_claims": note["target_claims"],
                    "claim_id": "",
                    "note_status": note_status(note),
                    "blocking_gap": "paper note not started" if note_status(note) == "pending_note" else "ready to inspect",
                    "source_fields_to_read": "contribution_summary; novelty_judgment; method_summary; evidence_strength; taxonomy_correction; final_report_use",
                    "overlay_fields_to_update": "manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes",
                }
            )
    fieldnames = [
        "target_type", "target_file", "overlay_key", "target_present", "event_id",
        "sprint_rank", "title", "target_claims", "claim_id", "note_status",
        "blocking_gap", "source_fields_to_read", "overlay_fields_to_update",
    ]
    write_csv(PROCESSED / "icml2026_sprint_02_overlay_bridge.csv", rows, fieldnames)
    counts = Counter(row["target_type"] for row in rows)
    lines = [
        "# ICML 2026 Sprint 02 Overlay Bridge",
        "",
        "Transfer checklist from sprint 02 paper notes into review overlays.",
        "",
        f"- Transfer rows: {len(rows)}",
        f"- Target mix: {', '.join(f'{key}: {value}' for key, value in counts.items())}",
        f"- Missing targets: {sum(row['target_present'] != 'true' for row in rows)}",
        "",
        "## Outputs",
        "",
        "- `data/processed/icml2026_sprint_02_overlay_bridge.csv`",
        "- `reports/icml2026_sprint_02_overlay_bridge.md`",
    ]
    (REPORTS / "icml2026_sprint_02_overlay_bridge.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    rows = build_sprint_rows()
    write_sprint(rows)
    write_prereview(rows)
    write_notes(rows)
    write_bridge()
    print(f"Wrote {PROCESSED / 'icml2026_review_sprint_02.csv'} ({len(rows)} rows)")
    print(f"Wrote {PROCESSED / 'icml2026_sprint_02_prereview_suggestions.csv'} ({len(rows)} rows)")
    print(f"Wrote {MANUAL / 'icml2026_review_sprint_02_paper_notes.csv'} ({len(rows)} rows)")
    print(f"Wrote {PROCESSED / 'icml2026_sprint_02_overlay_bridge.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
