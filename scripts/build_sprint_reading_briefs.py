#!/usr/bin/env python3
"""Build consolidated per-paper reading briefs for manual review sprints."""

from __future__ import annotations

import csv
import re
import shutil
import unicodedata
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
MANUAL = ROOT / "data" / "manual"
REPORTS = ROOT / "reports"
BRIEF_DIR = REPORTS / "review_reading_briefs"


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


def clip(text: str, limit: int = 900) -> str:
    text = clean(text)
    if len(text) <= limit:
        return text
    return text[: limit - 3].rsplit(" ", 1)[0] + "..."


def split_semicolon(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def note_started(row: dict[str, str]) -> bool:
    manual_fields = [
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
    return any(clean(row.get(field, "")) for field in manual_fields)


def slugify(title: str, event_id: str) -> str:
    normalized = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", normalized.lower()).strip("-")
    return f"{event_id}-{slug[:70] or 'paper'}.md"


def local_report_link(path: str, from_dir: Path = BRIEF_DIR) -> str:
    if not path:
        return ""
    target = ROOT / path
    try:
        rel = target.relative_to(from_dir)
    except ValueError:
        rel = Path("..") / target.relative_to(REPORTS)
    return str(rel).replace("\\", "/")


def markdown_links(paths: str, label_prefix: str) -> str:
    links = []
    for idx, path in enumerate(split_semicolon(paths), start=1):
        label = label_prefix if len(split_semicolon(paths)) == 1 else f"{label_prefix} {idx}"
        links.append(f"[{label}]({local_report_link(path)})")
    return ", ".join(links)


def index_by_event(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {row.get("event_id", ""): row for row in rows}


def build_rows() -> list[dict[str, object]]:
    sprint_01 = read_csv(PROCESSED / "icml2026_review_sprint_01.csv")
    sprint_02 = read_csv(PROCESSED / "icml2026_review_sprint_02.csv")
    suggestions_01 = index_by_event(read_csv(PROCESSED / "icml2026_sprint_prereview_suggestions.csv"))
    suggestions_02 = index_by_event(read_csv(PROCESSED / "icml2026_sprint_02_prereview_suggestions.csv"))
    notes_01 = index_by_event(read_csv(MANUAL / "icml2026_review_sprint_01_paper_notes.csv"))
    notes_02 = index_by_event(read_csv(MANUAL / "icml2026_review_sprint_02_paper_notes.csv"))

    rows: list[dict[str, object]] = []
    for sprint_name, sprint_rows, suggestions, notes in [
        ("sprint_01", sprint_01, suggestions_01, notes_01),
        ("sprint_02", sprint_02, suggestions_02, notes_02),
    ]:
        for row in sprint_rows:
            event_id = row["event_id"]
            suggestion = suggestions.get(event_id, {})
            note = notes.get(event_id, {})
            contribution_prompt = (
                suggestion.get("contribution_hypothesis")
                or suggestion.get("contribution_check")
                or "Identify the actual contribution, mechanism, and evidence level from the paper."
            )
            taxonomy_prompt = suggestion.get("taxonomy_question") or row.get("review_focus", "")
            claim_prompt = suggestion.get("claim_implication_prompt") or (
                f"Decide supports / weakens / complicates / not_applicable for {row.get('target_claims') or row.get('claim_ids') or 'linked claims'}."
            )
            artifact_prompt = suggestion.get("artifact_check_prompt") or (
                "Open GitHub/project link and record code/data/checkpoint/runnable status."
                if row.get("github_url")
                else "No GitHub URL in metadata; record none/not_applicable unless the PDF shows a release."
            )
            target_claims = row.get("target_claims") or row.get("claim_ids", "")
            brief_filename = slugify(row["title"], event_id)
            rows.append(
                {
                    "sprint": sprint_name,
                    "sprint_rank": row["sprint_rank"],
                    "global_review_rank": row.get("global_review_rank", row["sprint_rank"]),
                    "event_id": event_id,
                    "title": row["title"],
                    "area": row["area"],
                    "subarea": row["subarea"],
                    "target_claims": target_claims,
                    "review_phase": row["review_phase"],
                    "note_status": "started" if note_started(note) else "not_started",
                    "claim_overlay_keys": row.get("claim_overlay_keys", ""),
                    "area_overlay_keys": row.get("area_overlay_keys", ""),
                    "contribution_prompt": contribution_prompt,
                    "method_prompt": suggestion.get("method_hypothesis", ""),
                    "evidence_prompt": suggestion.get("evidence_to_verify", ""),
                    "taxonomy_prompt": taxonomy_prompt,
                    "claim_prompt": claim_prompt,
                    "artifact_prompt": artifact_prompt,
                    "reviewer_warning": suggestion.get("reviewer_warning", ""),
                    "suggested_note_seed": suggestion.get("suggested_note_seed", ""),
                    "signals": row.get("signals", ""),
                    "method_families": row.get("method_families", ""),
                    "evaluation_settings": row.get("evaluation_settings", ""),
                    "abstract_excerpt": clip(row.get("abstract_excerpt") or suggestion.get("abstract_basis", "")),
                    "claim_packet_links": row.get("claim_packet_links", ""),
                    "claim_dossier_links": row.get("claim_dossier_links", ""),
                    "area_packet_link": row.get("area_packet_link", ""),
                    "area_briefing_link": row.get("area_briefing_link", ""),
                    "icml_url": row.get("icml_url", ""),
                    "alphaxiv_url": row.get("alphaxiv_url", ""),
                    "github_url": row.get("github_url", ""),
                    "brief_path": f"reports/review_reading_briefs/{brief_filename}",
                }
            )
    return rows


def write_brief(row: dict[str, object]) -> None:
    path = ROOT / str(row["brief_path"])
    claim_packets = markdown_links(str(row["claim_packet_links"]), "claim packet")
    claim_dossiers = markdown_links(str(row["claim_dossier_links"]), "claim dossier")
    area_packet = f"[area packet]({local_report_link(str(row['area_packet_link']))})" if row["area_packet_link"] else "none"
    area_briefing = f"[area briefing]({local_report_link(str(row['area_briefing_link']))})" if row["area_briefing_link"] else "none"
    external_links = [f"[ICML]({row['icml_url']})"]
    if row["alphaxiv_url"]:
        external_links.append(f"[AlphaXiv]({row['alphaxiv_url']})")
    if row["github_url"]:
        external_links.append(f"[GitHub]({row['github_url']})")

    lines = [
        f"# {row['title']}",
        "",
        f"- Sprint: `{row['sprint']}` rank {row['sprint_rank']}",
        f"- Global review rank: {row['global_review_rank']}",
        f"- Event ID: `{row['event_id']}`",
        f"- Area: {row['area']} / {row['subarea']}",
        f"- Target claims: {row['target_claims'] or 'none'}",
        f"- Review phase: `{row['review_phase']}`",
        f"- Note status: `{row['note_status']}`",
        f"- Signals: {row['signals'] or 'none'}",
        f"- Links: {' / '.join(external_links)}",
        "",
        "## Where To Record Judgments",
        "",
        f"- Claim overlay keys: {row['claim_overlay_keys'] or 'none'}",
        f"- Area overlay keys: {row['area_overlay_keys'] or 'none'}",
        f"- Paper-note file: `data/manual/icml2026_review_{'sprint_01' if row['sprint'] == 'sprint_01' else 'sprint_02'}_paper_notes.csv`",
        "",
        "## Local Context",
        "",
        f"- Claim packets: {claim_packets or 'none'}",
        f"- Claim dossiers: {claim_dossiers or 'none'}",
        f"- Area packet: {area_packet}",
        f"- Area briefing: {area_briefing}",
        "",
        "## What To Verify",
        "",
        f"- Contribution: {row['contribution_prompt']}",
        f"- Method: {row['method_prompt'] or row['method_families'] or 'Identify core method family and whether it matches the metadata tags.'}",
        f"- Evidence: {row['evidence_prompt'] or 'Check baselines, datasets, metrics, ablations, and negative cases.'}",
        f"- Taxonomy: {row['taxonomy_prompt'] or 'Check whether the assigned area/subarea is accurate enough for report use.'}",
        f"- Claim implication: {row['claim_prompt']}",
        f"- Artifact: {row['artifact_prompt']}",
    ]
    if row["reviewer_warning"]:
        lines.append(f"- Warning: {row['reviewer_warning']}")
    lines.extend(
        [
            "",
            "## Abstract Excerpt",
            "",
            str(row["abstract_excerpt"]) or "No abstract excerpt available.",
            "",
            "## Suggested Note Seed",
            "",
            str(row["suggested_note_seed"]) or "Start with contribution, mechanism, evidence, limitations, artifact status, and claim implication.",
            "",
            "## Minimum Manual Fields",
            "",
            "- `paper_read_status`",
            "- `contribution_summary`",
            "- `novelty_judgment`",
            "- `method_summary`",
            "- `evidence_strength`",
            "- `baselines_checked`, `datasets_checked`, `metrics_checked`",
            "- `limitations`",
            "- `artifact_status_checked`",
            "- `claim_implications`",
            "- `taxonomy_correction`",
            "- `final_report_use`",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_index(rows: list[dict[str, object]]) -> None:
    sprint_counts = Counter(str(row["sprint"]) for row in rows)
    note_counts = Counter(str(row["note_status"]) for row in rows)
    claim_counts = Counter(
        claim
        for row in rows
        for claim in split_semicolon(str(row["target_claims"]))
    )
    area_counts = Counter(str(row["area"]) for row in rows)

    lines = [
        "# ICML 2026 Sprint Reading Briefs",
        "",
        "Consolidated paper-by-paper reading desk for the manual review sprints.",
        "Each brief combines sprint metadata, claim context, overlay keys, pre-review prompts, artifact checks, and local report links.",
        "",
        "## Snapshot",
        "",
        f"- Briefs: {len(rows)}",
        f"- Sprint mix: {', '.join(f'{key}: {value}' for key, value in sprint_counts.items())}",
        f"- Note status: {', '.join(f'{key}: {value}' for key, value in note_counts.items())}",
        f"- Claim coverage: {', '.join(f'{key}: {value}' for key, value in sorted(claim_counts.items()))}",
        f"- Areas represented: {len(area_counts)}",
        "",
        "## Review Order",
        "",
        "| Sprint | Rank | Paper | Claims | Area | Note status |",
        "| --- | ---: | --- | --- | --- | --- |",
    ]
    for row in rows:
        rel_path = Path(str(row["brief_path"])).relative_to("reports")
        lines.append(
            f"| {row['sprint']} | {row['sprint_rank']} | "
            f"[{row['title']}]({rel_path}) | {row['target_claims'] or 'none'} | "
            f"{row['area']} | {row['note_status']} |"
        )

    lines.extend(
        [
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_sprint_reading_briefs.csv`",
            "- `reports/icml2026_sprint_reading_brief_index.md`",
            "- `reports/review_reading_briefs/*.md`",
        ]
    )
    (REPORTS / "icml2026_sprint_reading_brief_index.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    rows = build_rows()
    if BRIEF_DIR.exists():
        shutil.rmtree(BRIEF_DIR)
    BRIEF_DIR.mkdir(parents=True, exist_ok=True)
    for row in rows:
        write_brief(row)
    fieldnames = [
        "sprint", "sprint_rank", "global_review_rank", "event_id", "title", "area",
        "subarea", "target_claims", "review_phase", "note_status",
        "claim_overlay_keys", "area_overlay_keys", "contribution_prompt",
        "method_prompt", "evidence_prompt", "taxonomy_prompt", "claim_prompt",
        "artifact_prompt", "reviewer_warning", "suggested_note_seed", "signals",
        "method_families", "evaluation_settings", "abstract_excerpt",
        "claim_packet_links", "claim_dossier_links", "area_packet_link",
        "area_briefing_link", "icml_url", "alphaxiv_url", "github_url",
        "brief_path",
    ]
    write_csv(PROCESSED / "icml2026_sprint_reading_briefs.csv", rows, fieldnames)
    write_index(rows)
    print(f"Wrote {PROCESSED / 'icml2026_sprint_reading_briefs.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_sprint_reading_brief_index.md'}")
    print(f"Wrote {BRIEF_DIR} ({len(rows)} briefs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
