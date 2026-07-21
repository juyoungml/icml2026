#!/usr/bin/env python3
"""Build a researcher-facing thesis hierarchy for the ICML 2026 landscape."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
MANUAL = ROOT / "data" / "manual"
REPORTS = ROOT / "reports"


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


def is_started_note(row: dict[str, str]) -> bool:
    fields = [
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
    return any((row.get(field, "") or "").strip() for field in fields)


def thesis_role(claim: dict[str, str], readiness_tier: str) -> tuple[str, str, str]:
    claim_id = claim["claim_id"]
    strength = claim["strength"]
    if readiness_tier == "publication_ready_seed":
        return (
            "promotable_headline",
            "Can be used as a headline claim after final prose review.",
            "State directly and cite reviewed paper rows.",
        )
    if readiness_tier == "partially_checked":
        return (
            "checked_supporting_claim",
            "Can support the narrative with explicit caveats.",
            "Use cautious language and cite reviewed rows.",
        )
    if claim_id in {"C01", "C02", "C03"}:
        return (
            "core_thesis_candidate",
            "Central to the report thesis, but currently directional because manual review is empty.",
            "Phrase as a landscape signal, not a settled paper-level conclusion.",
        )
    if claim_id in {"C04", "C05", "C07"} or strength == "moderate":
        return (
            "supporting_hypothesis",
            "Useful as a reading lens and contrast case.",
            "Use as a hypothesis until the linked papers and artifacts are checked.",
        )
    if strength == "context_only":
        return (
            "context_frame",
            "Useful background context, not a headline claim.",
            "Frame as external context with clear source limitations.",
        )
    if strength == "process_claim":
        return (
            "workflow_claim",
            "Describes the project validation workflow.",
            "Use to explain what remains unchecked, not as a field trend.",
        )
    return (
        "supporting_hypothesis",
        "Useful but not yet checked enough for a headline.",
        "Use as a hypothesis and attach caveats.",
    )


def top_papers_for_claim(review_plan: list[dict[str, str]], claim_id: str, limit: int = 5) -> list[str]:
    rows = [
        row for row in review_plan
        if claim_id in split_list(row.get("claim_ids", ""))
    ]
    rows.sort(key=lambda row: int(float(row.get("global_review_rank", "9999") or 9999)))
    return [
        f"{row['global_review_rank']}. {row['title']} ({row['event_id']})"
        for row in rows[:limit]
    ]


def build_rows() -> list[dict[str, object]]:
    claims = read_csv(PROCESSED / "icml2026_landscape_claim_register.csv")
    readiness = {
        row["id"]: row for row in read_csv(PROCESSED / "icml2026_researcher_readiness_audit.csv")
        if row.get("audit_type") == "claim"
    }
    reviewed_claims = read_csv(PROCESSED / "icml2026_claim_validation_reviewed.csv")
    review_plan = read_csv(PROCESSED / "icml2026_researcher_review_plan.csv")
    dossiers = read_csv(PROCESSED / "icml2026_claim_evidence_dossiers.csv")
    notes = optional_csv(MANUAL / "icml2026_review_sprint_01_paper_notes.csv")
    notes_by_event = {row["event_id"]: row for row in notes}

    reviewed_by_claim: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in reviewed_claims:
        reviewed_by_claim[row["claim_id"]].append(row)

    dossier_buckets: dict[str, Counter[str]] = defaultdict(Counter)
    for row in dossiers:
        dossier_buckets[row["claim_id"]][row.get("pre_review_bucket", "")] += 1

    sprint_note_counts: dict[str, int] = defaultdict(int)
    sprint_note_started: dict[str, int] = defaultdict(int)
    for row in review_plan[:40]:
        note = notes_by_event.get(row["event_id"], {})
        for claim_id in split_list(row.get("claim_ids", "")):
            sprint_note_counts[claim_id] += 1
            if note and is_started_note(note):
                sprint_note_started[claim_id] += 1

    out: list[dict[str, object]] = []
    for claim in claims:
        claim_id = claim["claim_id"]
        audit = readiness.get(claim_id, {})
        tier = audit.get("readiness_tier", "unknown")
        role, status, wording = thesis_role(claim, tier)
        claim_rows = reviewed_by_claim.get(claim_id, [])
        reviewed = sum(row.get("reviewed") == "true" for row in claim_rows)
        remaining = len(claim_rows) - reviewed
        bucket_summary = "; ".join(
            f"{bucket}: {count}" for bucket, count in dossier_buckets[claim_id].most_common() if bucket
        )
        blockers = []
        if remaining:
            blockers.append(f"{remaining} claim-review rows unreviewed")
        if int(float(audit.get("taxonomy_review_rows", 0) or 0)):
            blockers.append(f"{audit['taxonomy_review_rows']} taxonomy-boundary rows")
        if int(float(audit.get("low_confidence_rows", 0) or 0)):
            blockers.append(f"{audit['low_confidence_rows']} low-confidence evidence rows")
        if claim_id == "C07":
            blockers.append("repository links need live/manual inspection")
        if claim_id in {"C02", "C05", "C06"}:
            blockers.append("historical/arXiv baseline sensitivity")

        out.append(
            {
                "claim_id": claim_id,
                "theme": claim["theme"],
                "thesis_role": role,
                "readiness_tier": tier,
                "current_status": status,
                "allowed_wording": wording,
                "statement": claim["statement"],
                "evidence": claim["evidence"],
                "caveats": claim["caveats"],
                "review_rows": len(claim_rows),
                "reviewed_rows": reviewed,
                "remaining_rows": remaining,
                "sprint_papers": sprint_note_counts[claim_id],
                "sprint_notes_started": sprint_note_started[claim_id],
                "pre_review_bucket_mix": bucket_summary,
                "top_papers_to_read": " | ".join(top_papers_for_claim(review_plan, claim_id)),
                "blocking_checks": "; ".join(blockers) if blockers else "final prose review",
                "next_validation": claim["next_validation"],
            }
        )

    role_order = {
        "promotable_headline": 0,
        "checked_supporting_claim": 1,
        "core_thesis_candidate": 2,
        "supporting_hypothesis": 3,
        "context_frame": 4,
        "workflow_claim": 5,
    }
    out.sort(key=lambda row: (role_order.get(str(row["thesis_role"]), 99), str(row["claim_id"])))
    return out


def optional_acceptance_decisions() -> dict[str, str]:
    path = PROCESSED / "icml2026_claim_acceptance_criteria.csv"
    if not path.exists():
        return {}
    return {row["claim_id"]: row.get("decision", "") for row in read_csv(path)}


def write_report(rows: list[dict[str, object]]) -> None:
    acceptance = optional_acceptance_decisions()
    role_counts = Counter(str(row["thesis_role"]) for row in rows)
    reviewed = sum(int(row["reviewed_rows"]) for row in rows)
    review_rows = sum(int(row["review_rows"]) for row in rows)
    notes_started = sum(int(row["sprint_notes_started"]) for row in rows)
    sprint_rows = sum(int(row["sprint_papers"]) for row in rows)
    lines = [
        "# ICML 2026 Researcher Thesis Map",
        "",
        "A claim hierarchy for turning the ICML 2026 EDA workspace into a coherent ML landscape report.",
        "This is intentionally conservative: unreviewed claims remain thesis candidates or hypotheses, not publication-ready conclusions.",
        "",
        "## Snapshot",
        "",
        f"- Claims mapped: {len(rows)}",
        f"- Role mix: {', '.join(f'{role}: {count}' for role, count in sorted(role_counts.items()))}",
        f"- Claim-review rows checked: {reviewed}/{review_rows}",
        f"- First-sprint paper notes started across claim links: {notes_started}/{sprint_rows}",
        "",
        "## Recommended Thesis Hierarchy",
        "",
        "| Claim | Role | Readiness | Allowed wording | Blocking checks |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| `{row['claim_id']}` {row['theme']} | {row['thesis_role']} | {row['readiness_tier']} | "
            f"{row['allowed_wording']} | {row['blocking_checks']} |"
        )

    lines.extend(["", "## Claim Detail", ""])
    for row in rows:
        lines.extend(
            [
                f"### {row['claim_id']}: {row['theme']}",
                "",
                f"- Role: `{row['thesis_role']}`",
                f"- Status: {row['current_status']}",
                f"- Statement: {row['statement']}",
                f"- Evidence: {row['evidence']}",
                f"- Caveats: {row['caveats']}",
                f"- Review progress: {row['reviewed_rows']}/{row['review_rows']} claim rows; "
                f"{row['sprint_notes_started']}/{row['sprint_papers']} linked first-sprint notes started",
                f"- Pre-review bucket mix: {row['pre_review_bucket_mix'] or 'none'}",
                f"- Papers to read first: {row['top_papers_to_read'] or 'none'}",
                f"- Next validation: {row['next_validation']}",
                f"- Acceptance decision: `{acceptance.get(str(row['claim_id']), 'not_built_yet')}`",
                "",
            ]
        )

    lines.extend(
        [
            "## How To Use This Map",
            "",
            "- Lead with `core_thesis_candidate` claims only as directional signals until their paper rows are reviewed.",
            "- Use `supporting_hypothesis` claims to structure reading, not to make final assertions.",
            "- Keep `context_frame` and `workflow_claim` rows out of headline result slides.",
            "- Promote claims only after reviewed rows and paper notes support the exact wording.",
            "- Use `reports/icml2026_claim_acceptance_criteria.md` as the promotion gate before editing the overview seed.",
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_researcher_thesis_map.csv`",
            "- `reports/icml2026_researcher_thesis_map.md`",
        ]
    )
    (REPORTS / "icml2026_researcher_thesis_map.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    rows = build_rows()
    fieldnames = [
        "claim_id",
        "theme",
        "thesis_role",
        "readiness_tier",
        "current_status",
        "allowed_wording",
        "statement",
        "evidence",
        "caveats",
        "review_rows",
        "reviewed_rows",
        "remaining_rows",
        "sprint_papers",
        "sprint_notes_started",
        "pre_review_bucket_mix",
        "top_papers_to_read",
        "blocking_checks",
        "next_validation",
    ]
    write_csv(PROCESSED / "icml2026_researcher_thesis_map.csv", rows, fieldnames)
    write_report(rows)
    print(f"Wrote {PROCESSED / 'icml2026_researcher_thesis_map.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_researcher_thesis_map.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
