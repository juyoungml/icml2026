#!/usr/bin/env python3
"""Build a time-budgeted researcher action plan for the ICML 2026 workspace."""

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


def first_split(value: str, limit: int = 2) -> str:
    parts = [part.strip() for part in (value or "").split(";") if part.strip()]
    return " ; ".join(parts[:limit])


def first_rows(rows: list[dict[str, str]], limit: int) -> str:
    return " ; ".join(f"{row.get('sprint')} #{row.get('sprint_rank')}: {row.get('title')}" for row in rows[:limit])


def main() -> int:
    dashboard = read_csv(PROCESSED / "icml2026_review_execution_dashboard.csv")
    claim_actions = read_csv(PROCESSED / "icml2026_review_execution_claim_actions.csv")
    claim_risk = read_csv(PROCESSED / "icml2026_claim_risk_register.csv")
    area_risk = read_csv(PROCESSED / "icml2026_area_risk_register.csv")
    safe_statements = read_csv(PROCESSED / "icml2026_safe_statement_register.csv")
    briefs = read_csv(PROCESSED / "icml2026_sprint_reading_briefs.csv")
    taxonomy_queue = read_csv(PROCESSED / "icml2026_taxonomy_adjudication_queue.csv")
    artifact_queue = read_csv(PROCESSED / "icml2026_artifact_audit_queue.csv")
    divergence = read_csv(PROCESSED / "icml2026_public_program_divergence_set.csv")

    critical_claims = [row for row in claim_risk if row.get("risk_tier") == "critical"]
    high_claims = [row for row in claim_risk if row.get("risk_tier") == "high"]
    critical_areas = [row for row in area_risk if row.get("risk_tier") == "critical"]
    sprint_01 = [row for row in briefs if row.get("sprint") == "sprint_01"]
    sprint_02 = [row for row in briefs if row.get("sprint") == "sprint_02"]
    active_claim_actions = [row for row in claim_actions if row.get("action_priority") in {"1", "2"}]
    metric_status = Counter(row.get("status", "") for row in dashboard)
    safe_status = Counter(row.get("wording_status", "") for row in safe_statements)

    rows: list[dict[str, object]] = [
        {
            "time_budget": "30_minutes",
            "mode": "orientation",
            "objective": "Understand what can and cannot be safely said right now.",
            "primary_actions": "Read the safe statement register, review execution dashboard, and claim risk register snapshots.",
            "artifacts_to_open": "reports/icml2026_safe_statement_register.md ; reports/icml2026_review_execution_dashboard.md ; reports/icml2026_claim_risk_register.md",
            "expected_output": "A short list of allowed hypotheses, unsafe wording, and the first claims to review.",
            "stop_condition": f"Can explain why {safe_status.get('hypothesis_only', 0)} claims are hypothesis-only and why no claim is headline-ready.",
            "risk_if_skipped": "The overview seed may be read as final prose even though all promotion gates are still closed.",
        },
        {
            "time_budget": "2_hours",
            "mode": "claim_triage",
            "objective": "Start validating the core thesis claims without trying to review the whole corpus.",
            "primary_actions": f"Read first briefs for critical claims: {first_rows(sprint_01, 6)}.",
            "artifacts_to_open": "reports/icml2026_sprint_reading_brief_index.md ; data/manual/icml2026_review_sprint_01_paper_notes.csv",
            "expected_output": "Initial paper notes for the highest-priority sprint-01 papers and clear uncertainty notes for C01/C02/C03/C07.",
            "stop_condition": "At least 4 first-sprint paper notes have contribution, evidence, limitations, taxonomy, and claim-implication fields filled.",
            "risk_if_skipped": "Claims remain title/abstract-derived and cannot move toward promotion.",
        },
        {
            "time_budget": "half_day",
            "mode": "risk_reduction",
            "objective": "Reduce the biggest ways the landscape could be misleading.",
            "primary_actions": (
                f"Adjudicate top taxonomy clusters {', '.join(row.get('semantic_cluster_id', '') for row in taxonomy_queue[:3])}; "
                f"review high-risk areas {', '.join(row.get('area', '') for row in critical_areas[:3])}; "
                f"inspect top artifact queue entries {', '.join(row.get('event_id', '') for row in artifact_queue[:3])}."
            ),
            "artifacts_to_open": "reports/icml2026_area_risk_register.md ; reports/icml2026_taxonomy_adjudication_queue.md ; reports/icml2026_artifact_audit_queue.md",
            "expected_output": "Boundary decisions for top clusters, artifact notes for top repositories, and updated caveats for the riskiest areas.",
            "stop_condition": "Can state whether the top area-ranking and artifact-visibility signals survived first manual checks.",
            "risk_if_skipped": "Area shares, subarea claims, and reproducibility language may overstate heuristic metadata.",
        },
        {
            "time_budget": "1_day",
            "mode": "claim_coverage",
            "objective": "Cover every active claim action with at least initial paper notes.",
            "primary_actions": f"Work through sprint 01 core claims and sprint 02 C04/C05 papers: {first_rows(sprint_02, 6)}.",
            "artifacts_to_open": "reports/icml2026_sprint_reading_brief_index.md ; data/manual/icml2026_review_sprint_02_paper_notes.csv ; reports/icml2026_claim_decision_board.md",
            "expected_output": "Paper-note coverage for C01/C02/C03/C04/C05/C07 and a regenerated decision board.",
            "stop_condition": f"Every active claim action has paper-note progress: {len(active_claim_actions)} active claim actions tracked.",
            "risk_if_skipped": "C04/C05 remain uncovered and the report cannot responsibly discuss public/program and neighboring-venue contrasts.",
        },
        {
            "time_budget": "full_review_sprint",
            "mode": "promotion_readiness",
            "objective": "Convert notes into reviewed overlays and determine which claims can be promoted, demoted, or kept as context.",
            "primary_actions": "Fill overlay rows from paper-note bridges, run the value linter, rebuild reviewed tables, acceptance criteria, decision board, safe statements, and validation.",
            "artifacts_to_open": "reports/icml2026_paper_note_overlay_bridge.md ; reports/icml2026_sprint_02_overlay_bridge.md ; reports/icml2026_claim_acceptance_criteria.md",
            "expected_output": "A checked thesis map with promoted, demoted, and caveated claims plus updated safe wording.",
            "stop_condition": f"Validation stays green and manual progress moves beyond dashboard status mix {dict(metric_status)}.",
            "risk_if_skipped": "Manual notes remain isolated and never update the actual claim/area evidence gates.",
        },
    ]

    fieldnames = [
        "time_budget",
        "mode",
        "objective",
        "primary_actions",
        "artifacts_to_open",
        "expected_output",
        "stop_condition",
        "risk_if_skipped",
    ]
    write_csv(PROCESSED / "icml2026_researcher_action_plan.csv", rows, fieldnames)
    write_report(rows, critical_claims, high_claims, critical_areas, divergence)
    print(f"Wrote {PROCESSED / 'icml2026_researcher_action_plan.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_researcher_action_plan.md'}")
    return 0


def write_report(
    rows: list[dict[str, object]],
    critical_claims: list[dict[str, str]],
    high_claims: list[dict[str, str]],
    critical_areas: list[dict[str, str]],
    divergence: list[dict[str, str]],
) -> None:
    lines = [
        "# ICML 2026 Researcher Action Plan",
        "",
        "Time-budgeted execution plan for turning the current workspace into a stronger ICML 2026 research brief.",
        "",
        "## Priority Context",
        "",
        f"- Critical claims: {', '.join(row['claim_id'] for row in critical_claims)}",
        f"- High-risk claims: {', '.join(row['claim_id'] for row in high_claims)}",
        f"- Critical areas: {', '.join(row['area'] for row in critical_areas[:7])}",
        f"- Public/program divergence papers queued: {len(divergence)}",
        "",
        "## Time-Budgeted Plan",
        "",
        "| Budget | Mode | Objective | Primary actions | Stop condition |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['time_budget']} | {row['mode']} | {row['objective']} | {row['primary_actions']} | {row['stop_condition']} |"
        )
    lines.extend(["", "## Detailed Steps", ""])
    for row in rows:
        artifacts = [part.strip() for part in str(row["artifacts_to_open"]).split(";") if part.strip()]
        lines.extend(
            [
                f"### {row['time_budget']}: {row['mode']}",
                "",
                f"- Objective: {row['objective']}",
                "- Open:",
                *[f"  - `{artifact}`" for artifact in artifacts],
                f"- Expected output: {row['expected_output']}",
                f"- Stop condition: {row['stop_condition']}",
                f"- Risk if skipped: {row['risk_if_skipped']}",
                "",
            ]
        )
    lines.extend(
        [
            "## Outputs",
            "",
            "- `data/processed/icml2026_researcher_action_plan.csv`",
            "- `reports/icml2026_researcher_action_plan.md`",
        ]
    )
    (REPORTS / "icml2026_researcher_action_plan.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
