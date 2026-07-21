#!/usr/bin/env python3
"""Build an execution dashboard for manual ICML 2026 review."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
MANUAL = ROOT / "data" / "manual"
REPORTS = ROOT / "reports"


NOTE_FIELDS = [
    "paper_read_status",
    "contribution_summary",
    "novelty_judgment",
    "method_summary",
    "evidence_strength",
    "limitations",
    "artifact_status_checked",
    "claim_implications",
    "taxonomy_correction",
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


def note_started(row: dict[str, str]) -> bool:
    return any((row.get(field, "") or "").strip() for field in NOTE_FIELDS)


def as_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except (TypeError, ValueError):
        return 0


def pct(done: int, total: int) -> str:
    return f"{done / total * 100:.1f}%" if total else "0.0%"


def status_for(done: int, total: int, *, inverse: bool = False) -> str:
    if inverse:
        return "pass" if done == 0 else "needs_attention"
    if total and done >= total:
        return "complete"
    if done:
        return "in_progress"
    return "not_started"


def metric_row(
    area: str,
    metric: str,
    current: int,
    target: int,
    status: str,
    next_action: str,
    source: str,
) -> dict[str, object]:
    return {
        "area": area,
        "metric": metric,
        "current": current,
        "target": target,
        "completion_rate": pct(current, target),
        "status": status,
        "next_action": next_action,
        "source": source,
    }


def build_metrics() -> list[dict[str, object]]:
    progress = read_csv(PROCESSED / "manual_review_progress.csv")
    lint_issues = read_csv(PROCESSED / "icml2026_manual_review_value_lint.csv")
    lint_summary = read_csv(PROCESSED / "icml2026_manual_review_value_lint_summary.csv")
    acceptance = read_csv(PROCESSED / "icml2026_claim_acceptance_criteria.csv")
    notes_01 = read_csv(MANUAL / "icml2026_review_sprint_01_paper_notes.csv")
    notes_02 = read_csv(MANUAL / "icml2026_review_sprint_02_paper_notes.csv")
    bridge_01 = read_csv(PROCESSED / "icml2026_paper_note_overlay_bridge.csv")
    bridge_02 = read_csv(PROCESSED / "icml2026_sprint_02_overlay_bridge.csv")
    codebook = read_csv(PROCESSED / "icml2026_manual_review_codebook.csv")

    total_review_rows = sum(as_int(row.get("review_rows")) for row in progress)
    reviewed_rows = sum(as_int(row.get("reviewed_rows")) for row in progress)
    notes_01_started = sum(note_started(row) for row in notes_01)
    notes_02_started = sum(note_started(row) for row in notes_02)
    ready_bridge_01 = sum(row.get("blocking_gap") == "ready to transfer" for row in bridge_01)
    ready_bridge_02 = sum(row.get("blocking_gap") == "ready to transfer" for row in bridge_02)
    promotable = sum(row.get("decision") == "promote_candidate" for row in acceptance)
    checked_lint_values = sum(as_int(row.get("checked_values")) for row in lint_summary)

    return [
        metric_row(
            "manual_review",
            "reviewed_validation_rows",
            reviewed_rows,
            total_review_rows,
            status_for(reviewed_rows, total_review_rows),
            "Fill claim and area overlay rows after paper-note review.",
            "data/processed/manual_review_progress.csv",
        ),
        metric_row(
            "manual_review",
            "sprint_01_notes_started",
            notes_01_started,
            len(notes_01),
            status_for(notes_01_started, len(notes_01)),
            "Start with sprint 01 notes for C01/C02/C03/C07 and transfer decisions through the bridge.",
            "data/manual/icml2026_review_sprint_01_paper_notes.csv",
        ),
        metric_row(
            "manual_review",
            "sprint_02_notes_started",
            notes_02_started,
            len(notes_02),
            status_for(notes_02_started, len(notes_02)),
            "Use sprint 02 to unblock C04 and C05.",
            "data/manual/icml2026_review_sprint_02_paper_notes.csv",
        ),
        metric_row(
            "manual_review",
            "sprint_01_bridge_ready",
            ready_bridge_01,
            len(bridge_01),
            status_for(ready_bridge_01, len(bridge_01)),
            "After notes are filled, rebuild bridge and transfer ready rows into overlays.",
            "data/processed/icml2026_paper_note_overlay_bridge.csv",
        ),
        metric_row(
            "manual_review",
            "sprint_02_bridge_ready",
            ready_bridge_02,
            len(bridge_02),
            status_for(ready_bridge_02, len(bridge_02)),
            "After sprint 02 notes are filled, transfer C04/C05 rows into overlays.",
            "data/processed/icml2026_sprint_02_overlay_bridge.csv",
        ),
        metric_row(
            "quality_gate",
            "invalid_coded_values",
            len(lint_issues),
            0,
            status_for(len(lint_issues), 0, inverse=True),
            "Fix invalid coded values before rebuilding reviewed tables.",
            "data/processed/icml2026_manual_review_value_lint.csv",
        ),
        metric_row(
            "quality_gate",
            "coded_values_checked",
            checked_lint_values,
            checked_lint_values,
            "pass",
            "Run the linter after every manual edit.",
            "data/processed/icml2026_manual_review_value_lint_summary.csv",
        ),
        metric_row(
            "quality_gate",
            "codebook_rows",
            len(codebook),
            75,
            "pass" if len(codebook) >= 75 else "needs_attention",
            "Use canonical values from the codebook for all coded fields.",
            "data/processed/icml2026_manual_review_codebook.csv",
        ),
        metric_row(
            "claim_gate",
            "promote_candidate_claims",
            promotable,
            len(acceptance),
            status_for(promotable, len(acceptance)),
            "Promote no claim until acceptance criteria pass.",
            "data/processed/icml2026_claim_acceptance_criteria.csv",
        ),
    ]


def build_claim_actions() -> list[dict[str, object]]:
    decision_board = read_csv(PROCESSED / "icml2026_claim_decision_board.csv")
    acceptance = {row["claim_id"]: row for row in read_csv(PROCESSED / "icml2026_claim_acceptance_criteria.csv")}
    rows: list[dict[str, object]] = []
    for row in decision_board:
        claim_id = row["claim_id"]
        accept = acceptance.get(claim_id, {})
        sprint = "sprint_01" if as_int(row.get("sprint_claim_papers")) else ("sprint_02" if as_int(row.get("sprint_02_claim_papers")) else "none")
        if row.get("decision") == "context_or_workflow_only":
            action_priority = 4
        elif sprint == "sprint_01":
            action_priority = 1
        elif sprint == "sprint_02":
            action_priority = 2
        else:
            action_priority = 3
        rows.append(
            {
                "action_priority": action_priority,
                "claim_id": claim_id,
                "theme": row.get("theme", ""),
                "decision": row.get("decision", ""),
                "reviewed_rows": row.get("reviewed_rows", ""),
                "minimum_reviewed_rows": row.get("minimum_reviewed_rows", ""),
                "paper_notes_started": row.get("paper_notes_started", ""),
                "minimum_paper_notes": row.get("minimum_paper_notes", ""),
                "assigned_sprint": sprint,
                "sprint_01_papers": row.get("sprint_claim_papers", ""),
                "sprint_02_papers": row.get("sprint_02_claim_papers", ""),
                "bridge_ready": row.get("bridge_ready_to_transfer", ""),
                "missing_for_promotion": accept.get("missing_for_promotion", row.get("missing_for_promotion", "")),
                "next_action": row.get("next_decision_action", ""),
                "first_overlay_actions": row.get("first_overlay_actions", ""),
            }
        )
    rows.sort(key=lambda item: (int(item["action_priority"]), str(item["claim_id"])))
    return rows


def write_report(metrics: list[dict[str, object]], actions: list[dict[str, object]]) -> None:
    status_counts = Counter(str(row["status"]) for row in metrics)
    next_claims = [row for row in actions if int(row["action_priority"]) in {1, 2}]
    lines = [
        "# ICML 2026 Review Execution Dashboard",
        "",
        "Operational dashboard for moving manual paper review into validated claim decisions.",
        "",
        "## Snapshot",
        "",
        f"- Metrics tracked: {len(metrics)}",
        f"- Metric status mix: {', '.join(f'{key}: {value}' for key, value in status_counts.most_common())}",
        f"- Claims needing sprint execution: {len(next_claims)}",
        "",
        "## Metrics",
        "",
        "| Area | Metric | Current | Target | Rate | Status | Next action |",
        "| --- | --- | ---: | ---: | ---: | --- | --- |",
    ]
    for row in metrics:
        lines.append(
            f"| {row['area']} | `{row['metric']}` | {row['current']} | {row['target']} | "
            f"{row['completion_rate']} | {row['status']} | {row['next_action']} |"
        )

    lines.extend(
        [
            "",
            "## Claim Actions",
            "",
            "| Priority | Claim | Decision | Sprint | Review | Notes | Next action |",
            "| ---: | --- | --- | --- | ---: | ---: | --- |",
        ]
    )
    for row in actions:
        lines.append(
            f"| {row['action_priority']} | `{row['claim_id']}` {row['theme']} | {row['decision']} | "
            f"{row['assigned_sprint']} | {row['reviewed_rows']}/{row['minimum_reviewed_rows']} | "
            f"{row['paper_notes_started']}/{row['minimum_paper_notes']} | {row['next_action']} |"
        )

    lines.extend(
        [
            "",
            "## Execution Order",
            "",
            "1. Fill sprint 01 paper notes for C01, C02, C03, and C07.",
            "2. Run `python3 scripts/build_paper_note_overlay_bridge.py` and `python3 scripts/lint_manual_review_values.py`.",
            "3. Transfer ready sprint 01 rows into claim and area overlays.",
            "4. Fill sprint 02 notes for C04 and C05, then rebuild its overlay bridge.",
            "5. Rebuild reviewed tables, progress, readiness, acceptance criteria, decision board, and validation.",
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_review_execution_dashboard.csv`",
            "- `data/processed/icml2026_review_execution_claim_actions.csv`",
            "- `reports/icml2026_review_execution_dashboard.md`",
        ]
    )
    (REPORTS / "icml2026_review_execution_dashboard.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    metrics = build_metrics()
    actions = build_claim_actions()
    write_csv(
        PROCESSED / "icml2026_review_execution_dashboard.csv",
        metrics,
        ["area", "metric", "current", "target", "completion_rate", "status", "next_action", "source"],
    )
    write_csv(
        PROCESSED / "icml2026_review_execution_claim_actions.csv",
        actions,
        [
            "action_priority",
            "claim_id",
            "theme",
            "decision",
            "reviewed_rows",
            "minimum_reviewed_rows",
            "paper_notes_started",
            "minimum_paper_notes",
            "assigned_sprint",
            "sprint_01_papers",
            "sprint_02_papers",
            "bridge_ready",
            "missing_for_promotion",
            "next_action",
            "first_overlay_actions",
        ],
    )
    write_report(metrics, actions)
    print(f"Wrote {PROCESSED / 'icml2026_review_execution_dashboard.csv'} ({len(metrics)} rows)")
    print(f"Wrote {PROCESSED / 'icml2026_review_execution_claim_actions.csv'} ({len(actions)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_review_execution_dashboard.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
