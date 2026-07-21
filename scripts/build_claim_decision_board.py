#!/usr/bin/env python3
"""Build a claim-level decision board for ICML 2026 researcher review."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"


PROMOTION_DECISION_ORDER = {
    "promote_candidate": 0,
    "partially_checked": 1,
    "not_ready": 2,
    "context_or_workflow_only": 3,
}


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"Missing required input: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def optional_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    return read_csv(path)


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def split_list(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def to_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except (TypeError, ValueError):
        return 0


def bridge_action_summary(rows: list[dict[str, str]], limit: int = 5) -> str:
    rows = sorted(rows, key=lambda row: (to_int(row.get("sprint_rank")), row.get("overlay_key", "")))
    summaries = []
    seen_events = set()
    for row in rows:
        event_id = row.get("event_id", "")
        if event_id in seen_events:
            continue
        seen_events.add(event_id)
        summaries.append(
            f"{row.get('sprint_rank')}. {row.get('title')} ({event_id}) -> {row.get('overlay_key')}"
        )
        if len(summaries) >= limit:
            break
    return " | ".join(summaries)


def next_decision(decision: str, missing: str, bridge_rows: int, sprint_rows: int, sprint_02_rows: int) -> str:
    if decision == "promote_candidate":
        return "Draft final prose and cite reviewed rows."
    if decision == "partially_checked":
        return "Use only reviewed rows; fill remaining gaps before headline use."
    if decision == "context_or_workflow_only":
        return "Keep as framing/context; do not promote as a paper-quality claim."
    if bridge_rows == 0 or sprint_rows == 0:
        if sprint_02_rows:
            return "Use sprint 02 paper notes, then transfer decisions through the sprint 02 overlay bridge."
        return "Schedule this claim into the next paper-note sprint before expecting promotion."
    if "paper notes" in missing:
        return "Fill first-sprint paper notes, then transfer decisions through the overlay bridge."
    if "artifact checks" in missing:
        return "Inspect repositories and record artifact judgments before using reproducibility language."
    if "taxonomy boundary" in missing:
        return "Resolve taxonomy-boundary papers before subarea or share claims."
    return "Fill reviewed overlay rows until review/support gates pass."


def main() -> int:
    claims = {row["claim_id"]: row for row in read_csv(PROCESSED / "icml2026_landscape_claim_register.csv")}
    thesis = {row["claim_id"]: row for row in read_csv(PROCESSED / "icml2026_researcher_thesis_map.csv")}
    acceptance = {row["claim_id"]: row for row in read_csv(PROCESSED / "icml2026_claim_acceptance_criteria.csv")}
    readiness = {
        row["id"]: row
        for row in read_csv(PROCESSED / "icml2026_researcher_readiness_audit.csv")
        if row.get("audit_type") == "claim"
    }
    review_plan = read_csv(PROCESSED / "icml2026_researcher_review_plan.csv")
    bridge = read_csv(PROCESSED / "icml2026_paper_note_overlay_bridge.csv")
    sprint_02 = optional_csv(PROCESSED / "icml2026_review_sprint_02.csv")
    sprint_02_bridge = optional_csv(PROCESSED / "icml2026_sprint_02_overlay_bridge.csv")

    bridge_by_claim: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in bridge:
        if row.get("target_type") == "claim" and row.get("claim_id"):
            bridge_by_claim[row["claim_id"]].append(row)

    sprint_by_claim: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in review_plan:
        rank = to_int(row.get("global_review_rank"))
        if rank > 40:
            continue
        for claim_id in split_list(row.get("claim_ids", "")):
            sprint_by_claim[claim_id].append(row)

    sprint_02_by_claim: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in sprint_02:
        for claim_id in split_list(row.get("target_claims", "")):
            sprint_02_by_claim[claim_id].append(row)

    sprint_02_bridge_by_claim: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in sprint_02_bridge:
        claim_id = row.get("claim_id", "")
        if row.get("target_type") == "claim" and claim_id:
            sprint_02_bridge_by_claim[claim_id].append(row)

    rows: list[dict[str, object]] = []
    for claim_id, claim in claims.items():
        accept = acceptance.get(claim_id, {})
        claim_bridge = bridge_by_claim.get(claim_id, [])
        claim_sprint_02 = sprint_02_by_claim.get(claim_id, [])
        claim_sprint_02_bridge = sprint_02_bridge_by_claim.get(claim_id, [])
        blocking_gaps = Counter(row.get("blocking_gap", "") for row in claim_bridge)
        ready_transfer = blocking_gaps.get("ready to transfer", 0)
        pending_notes = blocking_gaps.get("paper note not started", 0)
        note_started_needs_decision = blocking_gaps.get("note exists but claim/taxonomy decision fields are not filled", 0)
        missing = accept.get("missing_for_promotion", "")
        sprint_rows = sprint_by_claim.get(claim_id, [])
        rows.append(
            {
                "claim_id": claim_id,
                "theme": claim.get("theme", ""),
                "thesis_role": thesis.get(claim_id, {}).get("thesis_role", ""),
                "decision": accept.get("decision", ""),
                "readiness_tier": thesis.get(claim_id, {}).get("readiness_tier", readiness.get(claim_id, {}).get("readiness_tier", "")),
                "allowed_next_use": accept.get("allowed_next_use", ""),
                "statement": claim.get("statement", ""),
                "evidence": claim.get("evidence", ""),
                "primary_caveat": claim.get("caveats", ""),
                "reviewed_rows": accept.get("reviewed_rows", ""),
                "minimum_reviewed_rows": accept.get("minimum_reviewed_rows", ""),
                "support_rows": accept.get("support_rows", ""),
                "minimum_support_rows": accept.get("minimum_support_rows", ""),
                "paper_notes_started": accept.get("paper_notes_started", ""),
                "minimum_paper_notes": accept.get("minimum_paper_notes", ""),
                "missing_for_promotion": missing,
                "claim_bridge_rows": len(claim_bridge),
                "bridge_pending_notes": pending_notes,
                "bridge_started_needs_decision": note_started_needs_decision,
                "bridge_ready_to_transfer": ready_transfer,
                "sprint_claim_papers": len(sprint_rows),
                "sprint_02_claim_papers": len(claim_sprint_02),
                "sprint_02_bridge_rows": len(claim_sprint_02_bridge),
                "next_decision_action": next_decision(
                    accept.get("decision", ""),
                    missing,
                    len(claim_bridge),
                    len(sprint_rows),
                    len(claim_sprint_02),
                ),
                "first_overlay_actions": bridge_action_summary(claim_bridge),
                "top_papers_to_read": thesis.get(claim_id, {}).get("top_papers_to_read", ""),
                "special_check": accept.get("special_check", ""),
            }
        )

    rows.sort(
        key=lambda row: (
            PROMOTION_DECISION_ORDER.get(str(row["decision"]), 9),
            0 if str(row["thesis_role"]) == "core_thesis_candidate" else 1,
            str(row["claim_id"]),
        )
    )

    fieldnames = [
        "claim_id",
        "theme",
        "thesis_role",
        "decision",
        "readiness_tier",
        "allowed_next_use",
        "statement",
        "evidence",
        "primary_caveat",
        "reviewed_rows",
        "minimum_reviewed_rows",
        "support_rows",
        "minimum_support_rows",
        "paper_notes_started",
        "minimum_paper_notes",
        "missing_for_promotion",
        "claim_bridge_rows",
        "bridge_pending_notes",
        "bridge_started_needs_decision",
        "bridge_ready_to_transfer",
        "sprint_claim_papers",
        "sprint_02_claim_papers",
        "sprint_02_bridge_rows",
        "next_decision_action",
        "first_overlay_actions",
        "top_papers_to_read",
        "special_check",
    ]
    write_csv(PROCESSED / "icml2026_claim_decision_board.csv", rows, fieldnames)

    decisions = Counter(str(row["decision"]) for row in rows)
    lines = [
        "# ICML 2026 Claim Decision Board",
        "",
        "Claim-level operating view for deciding what can be used now and what review action unlocks it.",
        "",
        "## Snapshot",
        "",
        f"- Claims tracked: {len(rows)}",
        f"- Decision mix: {', '.join(f'{key}: {value}' for key, value in decisions.most_common())}",
        f"- Claim overlay bridge rows: {sum(int(row['claim_bridge_rows']) for row in rows)}",
        f"- Sprint 02 claim papers: {sum(int(row['sprint_02_claim_papers']) for row in rows)}",
        f"- Ready-to-transfer bridge rows: {sum(int(row['bridge_ready_to_transfer']) for row in rows)}",
        "",
        "## Board",
        "",
        "| Claim | Role | Decision | Review | Notes | Sprint 01 bridge | Sprint 02 papers | Next action |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in rows:
        lines.append(
            f"| `{row['claim_id']}` {row['theme']} | {row['thesis_role']} | {row['decision']} | "
            f"{row['reviewed_rows']}/{row['minimum_reviewed_rows']} | "
            f"{row['paper_notes_started']}/{row['minimum_paper_notes']} | "
            f"{row['bridge_ready_to_transfer']}/{row['claim_bridge_rows']} ready | "
            f"{row['sprint_02_claim_papers']} | "
            f"{row['next_decision_action']} |"
        )

    lines.extend(["", "## First Actions By Claim", ""])
    for row in rows:
        lines.extend(
            [
                f"### {row['claim_id']}: {row['theme']}",
                "",
                f"- Allowed use now: {row['allowed_next_use']}",
                f"- Missing for promotion: {row['missing_for_promotion']}",
                f"- Special check: {row['special_check']}",
                f"- First overlay actions: {row['first_overlay_actions'] or 'No sprint overlay target in bridge.'}",
                "",
            ]
        )

    lines.extend(
        [
            "## Outputs",
            "",
            "- `data/processed/icml2026_claim_decision_board.csv`",
            "- `reports/icml2026_claim_decision_board.md`",
        ]
    )
    (REPORTS / "icml2026_claim_decision_board.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {PROCESSED / 'icml2026_claim_decision_board.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_claim_decision_board.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
