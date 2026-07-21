#!/usr/bin/env python3
"""Evaluate explicit acceptance criteria for ICML 2026 synthesis claims."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
MANUAL = ROOT / "data" / "manual"
REPORTS = ROOT / "reports"


CRITERIA = {
    "C01": {
        "minimum_reviewed_rows": 8,
        "minimum_support_rows": 5,
        "minimum_paper_notes": 4,
        "requires_taxonomy_resolution": True,
        "requires_artifact_check": False,
        "special_check": "Boundary papers must confirm this is LLM reasoning/post-training rather than broad LLM infrastructure spillover.",
    },
    "C02": {
        "minimum_reviewed_rows": 8,
        "minimum_support_rows": 5,
        "minimum_paper_notes": 4,
        "requires_taxonomy_resolution": True,
        "requires_artifact_check": False,
        "special_check": "Historical-delta interpretation must survive a spot check of systems and agents/code examples.",
    },
    "C03": {
        "minimum_reviewed_rows": 8,
        "minimum_support_rows": 5,
        "minimum_paper_notes": 4,
        "requires_taxonomy_resolution": True,
        "requires_artifact_check": False,
        "special_check": "Low-public/high-program papers must yield concrete technical reasons for committee attention.",
    },
    "C04": {
        "minimum_reviewed_rows": 6,
        "minimum_support_rows": 4,
        "minimum_paper_notes": 3,
        "requires_taxonomy_resolution": False,
        "requires_artifact_check": False,
        "special_check": "High-attention robotics papers must be labeled as benchmark, demo, reusable model, or core algorithmic contribution.",
    },
    "C05": {
        "minimum_reviewed_rows": 7,
        "minimum_support_rows": 4,
        "minimum_paper_notes": 3,
        "requires_taxonomy_resolution": True,
        "requires_artifact_check": False,
        "special_check": "Multimodal/vision aggregate must be broken into submodes before interpreting the neighboring-venue contrast.",
    },
    "C06": {
        "minimum_reviewed_rows": 0,
        "minimum_support_rows": 0,
        "minimum_paper_notes": 0,
        "requires_taxonomy_resolution": False,
        "requires_artifact_check": False,
        "special_check": "Use only as external context; do not promote to a venue-quality or acceptance trend claim.",
    },
    "C07": {
        "minimum_reviewed_rows": 8,
        "minimum_support_rows": 5,
        "minimum_paper_notes": 4,
        "requires_taxonomy_resolution": False,
        "requires_artifact_check": True,
        "special_check": "Repository links must be manually inspected for runnable code, data/checkpoints, license, and stale/broken state.",
    },
    "C08": {
        "minimum_reviewed_rows": 0,
        "minimum_support_rows": 0,
        "minimum_paper_notes": 0,
        "requires_taxonomy_resolution": False,
        "requires_artifact_check": False,
        "special_check": "Keep as a process/workflow claim; acceptance means the validation workflow remains explicit and auditable.",
    },
}


SUPPORT_VALUES = {"supports", "support", "yes", "strong_support", "partial_support"}
WEAKEN_VALUES = {"weakens", "weaken", "no", "contradicts", "unsupported"}
TAXONOMY_BAD_VALUES = {"too_broad", "too_narrow", "wrong_area", "wrong_subarea", "unclear"}
ARTIFACT_CHECKED_VALUES = {"live_checked", "runnable", "broken"}


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


def norm(value: str) -> str:
    return (value or "").strip().lower()


def note_started(row: dict[str, str]) -> bool:
    return any(
        norm(row.get(field, ""))
        for field in [
            "paper_read_status",
            "contribution_summary",
            "novelty_judgment",
            "method_summary",
            "evidence_strength",
            "limitations",
            "claim_implications",
            "taxonomy_correction",
            "final_report_use",
            "paper_note",
        ]
    )


def claim_note_counts(notes: list[dict[str, str]]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for row in notes:
        if not note_started(row):
            continue
        for claim_id in split_list(row.get("claim_ids", "")):
            counts[claim_id] += 1
    return counts


def gate_status(done: bool) -> str:
    return "pass" if done else "not_met"


def build_rows() -> list[dict[str, object]]:
    claims = read_csv(PROCESSED / "icml2026_landscape_claim_register.csv")
    thesis = {row["claim_id"]: row for row in read_csv(PROCESSED / "icml2026_researcher_thesis_map.csv")}
    reviewed = read_csv(PROCESSED / "icml2026_claim_validation_reviewed.csv")
    notes = optional_csv(MANUAL / "icml2026_review_sprint_01_paper_notes.csv")
    note_counts = claim_note_counts(notes)

    by_claim: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in reviewed:
        by_claim[row["claim_id"]].append(row)

    rows: list[dict[str, object]] = []
    for claim in claims:
        claim_id = claim["claim_id"]
        criteria = CRITERIA[claim_id]
        items = by_claim[claim_id]
        reviewed_rows = [row for row in items if row.get("reviewed") == "true"]
        support_rows = [
            row for row in reviewed_rows
            if norm(row.get("manual_claim_support", "")) in SUPPORT_VALUES
        ]
        weaken_rows = [
            row for row in reviewed_rows
            if norm(row.get("manual_claim_support", "")) in WEAKEN_VALUES
        ]
        unresolved_taxonomy = [
            row for row in reviewed_rows
            if norm(row.get("manual_taxonomy_judgment", "")) in TAXONOMY_BAD_VALUES
        ]
        artifact_checked = [
            row for row in reviewed_rows
            if norm(row.get("manual_artifact_judgment", "")) in ARTIFACT_CHECKED_VALUES
        ]

        review_gate = len(reviewed_rows) >= int(criteria["minimum_reviewed_rows"])
        support_gate = len(support_rows) >= int(criteria["minimum_support_rows"]) and not weaken_rows
        note_gate = note_counts[claim_id] >= int(criteria["minimum_paper_notes"])
        taxonomy_gate = not criteria["requires_taxonomy_resolution"] or (
            review_gate and not unresolved_taxonomy
        )
        artifact_gate = not criteria["requires_artifact_check"] or len(artifact_checked) >= int(criteria["minimum_support_rows"])
        process_gate = claim_id in {"C06", "C08"}

        all_gates = [review_gate, support_gate, note_gate, taxonomy_gate, artifact_gate]
        if process_gate:
            decision = "context_or_workflow_only"
        elif all(all_gates):
            decision = "promote_candidate"
        elif len(reviewed_rows):
            decision = "partially_checked"
        else:
            decision = "not_ready"

        missing = []
        if not review_gate:
            missing.append(f"reviewed rows {len(reviewed_rows)}/{criteria['minimum_reviewed_rows']}")
        if not support_gate:
            missing.append(f"support rows {len(support_rows)}/{criteria['minimum_support_rows']} with {len(weaken_rows)} weakening rows")
        if not note_gate:
            missing.append(f"paper notes {note_counts[claim_id]}/{criteria['minimum_paper_notes']}")
        if not taxonomy_gate:
            missing.append("taxonomy boundary unresolved")
        if not artifact_gate:
            missing.append(f"artifact checks {len(artifact_checked)}/{criteria['minimum_support_rows']}")

        rows.append(
            {
                "claim_id": claim_id,
                "theme": claim["theme"],
                "thesis_role": thesis.get(claim_id, {}).get("thesis_role", ""),
                "decision": decision,
                "review_gate": gate_status(review_gate),
                "support_gate": gate_status(support_gate),
                "paper_note_gate": gate_status(note_gate),
                "taxonomy_gate": gate_status(taxonomy_gate),
                "artifact_gate": gate_status(artifact_gate),
                "minimum_reviewed_rows": criteria["minimum_reviewed_rows"],
                "reviewed_rows": len(reviewed_rows),
                "minimum_support_rows": criteria["minimum_support_rows"],
                "support_rows": len(support_rows),
                "weakening_rows": len(weaken_rows),
                "minimum_paper_notes": criteria["minimum_paper_notes"],
                "paper_notes_started": note_counts[claim_id],
                "artifact_rows_checked": len(artifact_checked),
                "missing_for_promotion": "; ".join(missing) if missing else "none",
                "special_check": criteria["special_check"],
                "allowed_next_use": next_use(decision),
            }
        )

    return rows


def next_use(decision: str) -> str:
    if decision == "promote_candidate":
        return "Can be promoted into a headline thesis after prose review."
    if decision == "partially_checked":
        return "Use only with reviewed-row citations and explicit caveats."
    if decision == "context_or_workflow_only":
        return "Use as context or workflow framing, not as a field-quality conclusion."
    return "Use as directional hypothesis or reading guide only."


def write_report(rows: list[dict[str, object]]) -> None:
    decisions = Counter(str(row["decision"]) for row in rows)
    promotable = decisions.get("promote_candidate", 0)
    lines = [
        "# ICML 2026 Claim Acceptance Criteria",
        "",
        "Explicit promotion gates for synthesis claims.",
        "This report turns semantic validation into checkable criteria rather than relying on broad structural validation.",
        "",
        "## Snapshot",
        "",
        f"- Claims evaluated: {len(rows)}",
        f"- Promotion candidates: {promotable}",
        f"- Decision mix: {', '.join(f'{key}: {count}' for key, count in sorted(decisions.items()))}",
        "",
        "## Criteria Table",
        "",
        "| Claim | Decision | Review | Support | Notes | Taxonomy | Artifact | Missing |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| `{row['claim_id']}` {row['theme']} | {row['decision']} | "
            f"{row['reviewed_rows']}/{row['minimum_reviewed_rows']} | "
            f"{row['support_rows']}/{row['minimum_support_rows']} | "
            f"{row['paper_notes_started']}/{row['minimum_paper_notes']} | "
            f"{row['taxonomy_gate']} | {row['artifact_gate']} | {row['missing_for_promotion']} |"
        )

    lines.extend(["", "## Claim-Specific Checks", ""])
    for row in rows:
        lines.extend(
            [
                f"### {row['claim_id']}: {row['theme']}",
                "",
                f"- Thesis role: `{row['thesis_role']}`",
                f"- Decision: `{row['decision']}`",
                f"- Allowed next use: {row['allowed_next_use']}",
                f"- Special check: {row['special_check']}",
                f"- Missing for promotion: {row['missing_for_promotion']}",
                "",
            ]
        )

    lines.extend(
        [
            "## How To Use",
            "",
            "- Do not promote a headline claim unless `decision` is `promote_candidate`.",
            "- Treat `context_or_workflow_only` claims as framing, even when their criteria are structurally satisfied.",
            "- When overlays and paper notes are filled, rerun this report before editing the overview seed.",
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_claim_acceptance_criteria.csv`",
            "- `reports/icml2026_claim_acceptance_criteria.md`",
        ]
    )
    (REPORTS / "icml2026_claim_acceptance_criteria.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    rows = build_rows()
    fieldnames = [
        "claim_id",
        "theme",
        "thesis_role",
        "decision",
        "review_gate",
        "support_gate",
        "paper_note_gate",
        "taxonomy_gate",
        "artifact_gate",
        "minimum_reviewed_rows",
        "reviewed_rows",
        "minimum_support_rows",
        "support_rows",
        "weakening_rows",
        "minimum_paper_notes",
        "paper_notes_started",
        "artifact_rows_checked",
        "missing_for_promotion",
        "special_check",
        "allowed_next_use",
    ]
    write_csv(PROCESSED / "icml2026_claim_acceptance_criteria.csv", rows, fieldnames)
    write_report(rows)
    print(f"Wrote {PROCESSED / 'icml2026_claim_acceptance_criteria.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_claim_acceptance_criteria.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
