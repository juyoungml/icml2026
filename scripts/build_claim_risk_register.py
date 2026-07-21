#!/usr/bin/env python3
"""Build a falsification-oriented risk register for synthesis claims."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"


CLAIM_RISK_GUIDANCE = {
    "C01": {
        "weakest_assumption": "The large LLM/post-training area is not inflated by broad LLM infrastructure, generic evaluation, or diffusion-language boundary papers.",
        "falsification_test": "Review boundary papers and relabel any that are mainly systems, safety, or general language-model evaluation; recompute whether LLM reasoning still leads the landscape.",
        "counterevidence_to_seek": "Strong papers whose main contribution is infrastructure, safety, or generic modeling despite being counted as LLM reasoning/post-training.",
    },
    "C02": {
        "weakest_assumption": "Systems, agents, and code/tool-use papers form a coherent infrastructure shift rather than several unrelated pockets.",
        "falsification_test": "Read representative systems and agents/code papers and check whether the mechanism is reusable infrastructure, benchmark packaging, or ordinary model training.",
        "counterevidence_to_seek": "Papers tagged as infrastructure where the actual contribution is narrow evaluation, dataset construction, or a non-agentic method.",
    },
    "C03": {
        "weakest_assumption": "Oral/award selection reflects concrete technical or conceptual importance, not just position-paper salience or topic timeliness.",
        "falsification_test": "Compare low-public/high-program papers against their abstracts/PDFs and label the committee-selection rationale.",
        "counterevidence_to_seek": "Program-forward papers with weak technical novelty, unclear evidence, or primarily policy/editorial contribution.",
    },
    "C04": {
        "weakest_assumption": "Public attention around robotics/world models reflects a recognizable mismatch with program selection rather than metadata or community-size artifacts.",
        "falsification_test": "Classify high-attention robotics papers as benchmark, demo, reusable model, or core algorithmic contribution and compare with oral/award status.",
        "counterevidence_to_seek": "High-vote robotics papers that are also clearly program-significant, technically deep, and not merely demo-visible.",
    },
    "C05": {
        "weakest_assumption": "The neighboring-venue contrast is meaningful after multimodal/vision is split into video, 3D/spatial, VLA, robustness, and generic vision-language submodes.",
        "falsification_test": "Break the sprint-02 multimodal/vision papers into submodes before interpreting the aggregate underweight/overweight signal.",
        "counterevidence_to_seek": "Submodes that are strong at ICML 2026 even if the aggregate multimodal/vision area looks underweight versus baselines.",
    },
    "C06": {
        "weakest_assumption": "External arXiv and neighboring-venue baselines are useful context without implying venue policy or causal field momentum.",
        "falsification_test": "Run sensitivity checks on broad query terms and accepted-paper baselines before using any trend language.",
        "counterevidence_to_seek": "Query variants or neighboring venues that reverse the claimed direction for the same area.",
    },
    "C07": {
        "weakest_assumption": "Visible repository links imply meaningful reproducibility rather than project pages, stale code, missing data, or unrunnable releases.",
        "falsification_test": "Open linked repositories for high-signal papers and record license, release state, data/checkpoints, dependencies, and runnable example.",
        "counterevidence_to_seek": "High-visibility papers whose repository is missing, stale, non-runnable, data-free, or not actually tied to the paper.",
    },
    "C08": {
        "weakest_assumption": "The validation workflow is explicit enough to prevent directional heuristics from being promoted as settled conclusions.",
        "falsification_test": "Audit every report headline against reviewed rows, paper notes, acceptance criteria, and manual caveats before presentation use.",
        "counterevidence_to_seek": "Any final-report claim that lacks reviewed paper rows, has unresolved taxonomy boundaries, or cites AlphaXiv/GitHub as quality evidence.",
    },
}


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


def split_list(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def to_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except (TypeError, ValueError):
        return 0


def contains_claim(row: dict[str, str], claim_id: str) -> bool:
    return claim_id in split_list(row.get("target_claims", "") or row.get("claim_ids", ""))


def risk_tier(decision: str, thesis_role: str, missing: str, bucket_mix: Counter[str]) -> str:
    if decision == "promote_candidate":
        return "watch"
    if decision == "context_or_workflow_only":
        return "process"
    if "artifact checks" in missing or bucket_mix.get("high_risk_artifact", 0):
        return "high"
    if thesis_role == "core_thesis_candidate":
        return "critical"
    return "high"


def top_briefs(briefs: list[dict[str, str]], claim_id: str, limit: int = 4) -> str:
    rows = [row for row in briefs if contains_claim(row, claim_id)]
    rows.sort(key=lambda row: (row.get("sprint", ""), to_int(row.get("sprint_rank"))))
    return " ; ".join(
        f"{row.get('sprint')} #{row.get('sprint_rank')}: {row.get('title')} ({row.get('event_id')})"
        for row in rows[:limit]
    )


def brief_paths(briefs: list[dict[str, str]], claim_id: str, limit: int = 4) -> str:
    rows = [row for row in briefs if contains_claim(row, claim_id)]
    rows.sort(key=lambda row: (row.get("sprint", ""), to_int(row.get("sprint_rank"))))
    return " ; ".join(row.get("brief_path", "") for row in rows[:limit])


def main() -> int:
    claims = {row["claim_id"]: row for row in read_csv(PROCESSED / "icml2026_landscape_claim_register.csv")}
    acceptance = {row["claim_id"]: row for row in read_csv(PROCESSED / "icml2026_claim_acceptance_criteria.csv")}
    board = {row["claim_id"]: row for row in read_csv(PROCESSED / "icml2026_claim_decision_board.csv")}
    thesis = {row["claim_id"]: row for row in read_csv(PROCESSED / "icml2026_researcher_thesis_map.csv")}
    dossiers = read_csv(PROCESSED / "icml2026_claim_evidence_dossiers.csv")
    briefs = read_csv(PROCESSED / "icml2026_sprint_reading_briefs.csv")

    bucket_by_claim: dict[str, Counter[str]] = defaultdict(Counter)
    confidence_by_claim: dict[str, Counter[str]] = defaultdict(Counter)
    taxonomy_needs_by_claim: Counter[str] = Counter()
    artifact_needs_by_claim: Counter[str] = Counter()
    for row in dossiers:
        claim_id = row.get("claim_id", "")
        bucket_by_claim[claim_id][row.get("pre_review_bucket", "")] += 1
        confidence_by_claim[claim_id][row.get("evidence_confidence", "")] += 1
        if row.get("taxonomy_review_status") == "needs_review":
            taxonomy_needs_by_claim[claim_id] += 1
        if row.get("needs_manual_check_reason") or row.get("github_url"):
            artifact_needs_by_claim[claim_id] += 1

    rows: list[dict[str, object]] = []
    for claim_id in sorted(claims):
        claim = claims[claim_id]
        accept = acceptance.get(claim_id, {})
        decision_row = board.get(claim_id, {})
        thesis_row = thesis.get(claim_id, {})
        guidance = CLAIM_RISK_GUIDANCE[claim_id]
        bucket_mix = bucket_by_claim[claim_id]
        missing = accept.get("missing_for_promotion", "")
        tier = risk_tier(accept.get("decision", ""), thesis_row.get("thesis_role", ""), missing, bucket_mix)
        manual_evidence_needed = []
        if "reviewed rows" in missing:
            manual_evidence_needed.append(f"review rows {accept.get('reviewed_rows')}/{accept.get('minimum_reviewed_rows')}")
        if "support rows" in missing:
            manual_evidence_needed.append(f"support rows {accept.get('support_rows')}/{accept.get('minimum_support_rows')}")
        if "paper notes" in missing:
            manual_evidence_needed.append(f"paper notes {accept.get('paper_notes_started')}/{accept.get('minimum_paper_notes')}")
        if "taxonomy boundary" in missing:
            manual_evidence_needed.append(f"taxonomy checks on {taxonomy_needs_by_claim[claim_id]} dossier rows")
        if "artifact checks" in missing:
            manual_evidence_needed.append(f"artifact checks on {artifact_needs_by_claim[claim_id]} candidate rows")
        rows.append(
            {
                "claim_id": claim_id,
                "theme": claim.get("theme", ""),
                "thesis_role": thesis_row.get("thesis_role", ""),
                "decision": accept.get("decision", ""),
                "risk_tier": tier,
                "allowed_next_use": accept.get("allowed_next_use", ""),
                "statement_under_test": claim.get("statement", ""),
                "current_evidence": claim.get("evidence", ""),
                "primary_caveat": claim.get("caveats", ""),
                "weakest_assumption": guidance["weakest_assumption"],
                "falsification_test": guidance["falsification_test"],
                "counterevidence_to_seek": guidance["counterevidence_to_seek"],
                "missing_for_promotion": missing,
                "manual_evidence_needed": "; ".join(manual_evidence_needed) if manual_evidence_needed else "none",
                "pre_review_bucket_mix": "; ".join(f"{key}:{value}" for key, value in sorted(bucket_mix.items())) or "none",
                "evidence_confidence_mix": "; ".join(f"{key}:{value}" for key, value in sorted(confidence_by_claim[claim_id].items())) or "none",
                "taxonomy_review_rows": taxonomy_needs_by_claim[claim_id],
                "artifact_candidate_rows": artifact_needs_by_claim[claim_id],
                "special_check": accept.get("special_check", ""),
                "next_decision_action": decision_row.get("next_decision_action", ""),
                "first_papers_to_read": top_briefs(briefs, claim_id),
                "first_briefs_to_open": brief_paths(briefs, claim_id),
            }
        )

    fieldnames = [
        "claim_id",
        "theme",
        "thesis_role",
        "decision",
        "risk_tier",
        "allowed_next_use",
        "statement_under_test",
        "current_evidence",
        "primary_caveat",
        "weakest_assumption",
        "falsification_test",
        "counterevidence_to_seek",
        "missing_for_promotion",
        "manual_evidence_needed",
        "pre_review_bucket_mix",
        "evidence_confidence_mix",
        "taxonomy_review_rows",
        "artifact_candidate_rows",
        "special_check",
        "next_decision_action",
        "first_papers_to_read",
        "first_briefs_to_open",
    ]
    write_csv(PROCESSED / "icml2026_claim_risk_register.csv", rows, fieldnames)
    write_report(rows)
    print(f"Wrote {PROCESSED / 'icml2026_claim_risk_register.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_claim_risk_register.md'}")
    return 0


def write_report(rows: list[dict[str, object]]) -> None:
    tier_counts = Counter(str(row["risk_tier"]) for row in rows)
    decision_counts = Counter(str(row["decision"]) for row in rows)
    lines = [
        "# ICML 2026 Claim Risk Register",
        "",
        "Falsification-oriented register for the headline synthesis claims.",
        "Use this before promoting any claim into the overview report or presentation.",
        "",
        "## Snapshot",
        "",
        f"- Claims tracked: {len(rows)}",
        f"- Risk tiers: {', '.join(f'{key}: {value}' for key, value in tier_counts.most_common())}",
        f"- Decisions: {', '.join(f'{key}: {value}' for key, value in decision_counts.most_common())}",
        "",
        "## Risk Register",
        "",
        "| Claim | Risk | Decision | Weakest assumption | Falsification test | First papers |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| `{row['claim_id']}` {row['theme']} | {row['risk_tier']} | {row['decision']} | "
            f"{row['weakest_assumption']} | {row['falsification_test']} | {row['first_papers_to_read'] or 'none'} |"
        )

    lines.extend(["", "## Claim Details", ""])
    for row in rows:
        lines.extend(
            [
                f"### {row['claim_id']}: {row['theme']}",
                "",
                f"- Allowed use now: {row['allowed_next_use']}",
                f"- Statement under test: {row['statement_under_test']}",
                f"- Current evidence: {row['current_evidence']}",
                f"- Primary caveat: {row['primary_caveat']}",
                f"- Counterevidence to seek: {row['counterevidence_to_seek']}",
                f"- Manual evidence needed: {row['manual_evidence_needed']}",
                f"- Pre-review bucket mix: {row['pre_review_bucket_mix']}",
                f"- Evidence confidence mix: {row['evidence_confidence_mix']}",
                f"- Special check: {row['special_check']}",
                f"- Next decision action: {row['next_decision_action']}",
                f"- Briefs to open: {row['first_briefs_to_open'] or 'none'}",
                "",
            ]
        )
    lines.extend(
        [
            "## Outputs",
            "",
            "- `data/processed/icml2026_claim_risk_register.csv`",
            "- `reports/icml2026_claim_risk_register.md`",
        ]
    )
    (REPORTS / "icml2026_claim_risk_register.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
