#!/usr/bin/env python3
"""Build paper-level reading sets for public-attention vs program-signal divergence."""

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


def intish(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def fnum(value: str) -> float:
    try:
        return float(value or 0)
    except ValueError:
        return 0.0


def classify(row: dict[str, str], vote_rank: int, corpus_size: int) -> tuple[str, str]:
    is_program = row.get("is_oral") == "true" or bool(row.get("award"))
    votes = intish(row.get("public_total_votes", ""))
    top_public = vote_rank <= 150 or votes >= 100
    low_public = votes <= 15
    if top_public and not is_program:
        return "public_ahead_of_program", "High AlphaXiv attention without oral/award signal."
    if is_program and low_public:
        return "program_ahead_of_public", "Oral/award paper with low AlphaXiv public votes."
    if bool(row.get("award")) and votes <= 50:
        return "award_low_public", "Award paper with low public-attention signal."
    if is_program and top_public:
        return "public_and_program_aligned", "Both program and public signals are high."
    if vote_rank <= max(10, corpus_size // 100):
        return "extreme_public_attention", "Top public-attention paper; inspect why it spread."
    return "context", "Lower-priority context row."


def main() -> int:
    papers = read_csv(PROCESSED / "icml2026_paper_explorer.csv")
    review_plan = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_researcher_review_plan.csv")}
    notes = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_sprint_prereview_suggestions.csv")}

    ranked = sorted(papers, key=lambda row: intish(row.get("public_total_votes", "")), reverse=True)
    rank_by_event = {row["event_id"]: rank for rank, row in enumerate(ranked, start=1)}
    rows: list[dict[str, object]] = []
    for row in papers:
        rank = rank_by_event[row["event_id"]]
        category, reason = classify(row, rank, len(papers))
        if category == "context":
            continue
        plan_row = review_plan.get(row["event_id"], {})
        note = notes.get(row["event_id"], {})
        is_program = row.get("is_oral") == "true" or bool(row.get("award"))
        votes = intish(row.get("public_total_votes", ""))
        divergence_score = (
            votes
            if category == "public_ahead_of_program"
            else 1000 - votes
            if category in {"program_ahead_of_public", "award_low_public"}
            else 500 + votes
        )
        rows.append(
            {
                "category": category,
                "divergence_score": divergence_score,
                "public_vote_rank": rank,
                "event_id": row["event_id"],
                "title": row["title"],
                "area": row["area"],
                "subarea": row["subarea"],
                "is_oral": row["is_oral"],
                "award": row["award"],
                "public_total_votes": votes,
                "visits_last_7_days": row.get("visits_last_7_days", ""),
                "github_url": row.get("github_url", ""),
                "github_stars": row.get("github_stars", ""),
                "review_plan_rank": plan_row.get("global_review_rank", ""),
                "review_phase": plan_row.get("review_phase", ""),
                "claim_ids": plan_row.get("claim_ids", ""),
                "taxonomy_review_status": row.get("review_status", ""),
                "evidence_confidence": row.get("evidence_confidence", ""),
                "primary_contribution_type": row.get("primary_contribution_type", ""),
                "method_families": row.get("method_families", ""),
                "evaluation_settings": row.get("evaluation_settings", ""),
                "calibration_question": calibration_question(category, row, reason),
                "suggested_first_check": note.get("reviewer_warning", "") or reason,
                "url": row.get("url", ""),
                "alphaxiv_url": row.get("alphaxiv_url", ""),
            }
        )

    rows.sort(key=lambda row: (str(row["category"]), -int(row["divergence_score"]), int(row["public_vote_rank"])))
    # Keep the artifact focused but broad enough for area comparisons.
    kept = []
    per_category = Counter()
    for row in rows:
        if per_category[str(row["category"])] >= 50:
            continue
        kept.append(row)
        per_category[str(row["category"])] += 1
    rows = kept

    fieldnames = [
        "category",
        "divergence_score",
        "public_vote_rank",
        "event_id",
        "title",
        "area",
        "subarea",
        "is_oral",
        "award",
        "public_total_votes",
        "visits_last_7_days",
        "github_url",
        "github_stars",
        "review_plan_rank",
        "review_phase",
        "claim_ids",
        "taxonomy_review_status",
        "evidence_confidence",
        "primary_contribution_type",
        "method_families",
        "evaluation_settings",
        "calibration_question",
        "suggested_first_check",
        "url",
        "alphaxiv_url",
    ]
    write_csv(PROCESSED / "icml2026_public_program_divergence_set.csv", rows, fieldnames)
    write_report(rows)
    print(f"Wrote {PROCESSED / 'icml2026_public_program_divergence_set.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_public_program_divergence_set.md'}")
    return 0


def calibration_question(category: str, row: dict[str, str], reason: str) -> str:
    if category == "public_ahead_of_program":
        return "Is public attention driven by technical novelty, artifact usability, benchmark/demo appeal, topic popularity, or social amplification?"
    if category == "program_ahead_of_public":
        return "What technical reason might explain oral/award selection despite low public attention?"
    if category == "award_low_public":
        return "Does the award recognize theory, position framing, or committee-valued rigor that AlphaXiv underweights?"
    if category == "public_and_program_aligned":
        return "What properties make this paper visible to both the program committee and public audience?"
    return reason


def write_report(rows: list[dict[str, object]]) -> None:
    counts = Counter(str(row["category"]) for row in rows)
    lines = [
        "# ICML 2026 Public/Program Divergence Reading Set",
        "",
        "Paper-level reading set for calibrating AlphaXiv public attention against ICML oral/award program signal.",
        "Use this to avoid treating public votes as paper quality.",
        "",
        "## Snapshot",
        "",
        f"- Papers in reading set: {len(rows)}",
        f"- Category mix: {', '.join(f'{category}: {count}' for category, count in sorted(counts.items()))}",
        "",
        "## Category Guide",
        "",
        "- `public_ahead_of_program`: high AlphaXiv attention without oral/award signal.",
        "- `program_ahead_of_public`: oral/award signal with low AlphaXiv votes.",
        "- `award_low_public`: award paper with low public signal.",
        "- `public_and_program_aligned`: high public and program signal.",
        "- `extreme_public_attention`: top public-attention paper to inspect as a spread mechanism.",
        "",
    ]
    for category in sorted(counts):
        lines.extend([f"## {category}", "", "| Rank | Paper | Area | Votes | Program | Calibration question |", "| ---: | --- | --- | ---: | --- | --- |"])
        for row in [item for item in rows if item["category"] == category][:15]:
            program = "oral" if row["is_oral"] == "true" else ""
            if row["award"]:
                program = f"{program}; {row['award']}".strip("; ")
            lines.append(
                f"| {row['public_vote_rank']} | {row['title']} | {row['area']} | {row['public_total_votes']} | "
                f"{program or 'none'} | {row['calibration_question']} |"
            )
        lines.append("")
    lines.extend(
        [
            "## How To Use",
            "",
            "- Read a balanced sample from `public_ahead_of_program` and `program_ahead_of_public` before writing about public attention.",
            "- Label whether attention seems driven by novelty, artifact availability, topic popularity, demo/benchmark appeal, or committee-valued rigor.",
            "- Do not use this table as a quality ranking.",
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_public_program_divergence_set.csv`",
            "- `reports/icml2026_public_program_divergence_set.md`",
        ]
    )
    (REPORTS / "icml2026_public_program_divergence_set.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
