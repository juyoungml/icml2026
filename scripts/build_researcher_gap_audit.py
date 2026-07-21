#!/usr/bin/env python3
"""Build a critical gap audit for turning the ICML 2026 workspace into a stronger research brief."""

from __future__ import annotations

import csv
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


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def pct(done: int, total: int) -> str:
    return f"{done / total * 100:.1f}%" if total else "0.0%"


def reviewed_count(rows: list[dict[str, str]]) -> int:
    return sum(row.get("reviewed") == "true" for row in rows)


def optional_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    return read_csv(path)


def note_started(row: dict[str, str]) -> bool:
    return any(
        (row.get(field, "") or "").strip()
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


def main() -> int:
    papers = read_csv(PROCESSED / "icml2026_papers.csv")
    claim_reviewed = read_csv(PROCESSED / "icml2026_claim_validation_reviewed.csv")
    area_reviewed = read_csv(PROCESSED / "icml2026_area_validation_reviewed.csv")
    review_plan = read_csv(PROCESSED / "icml2026_researcher_review_plan.csv")
    readiness = read_csv(PROCESSED / "icml2026_researcher_readiness_audit.csv")
    validation = read_csv(PROCESSED / "workspace_validation_checks.csv")
    paper_notes = optional_csv(MANUAL / "icml2026_review_sprint_01_paper_notes.csv")
    thesis_map = optional_csv(PROCESSED / "icml2026_researcher_thesis_map.csv")
    acceptance = optional_csv(PROCESSED / "icml2026_claim_acceptance_criteria.csv")
    decision_board = optional_csv(PROCESSED / "icml2026_claim_decision_board.csv")
    divergence = optional_csv(PROCESSED / "icml2026_public_program_divergence_set.csv")
    taxonomy_adjudication = optional_csv(PROCESSED / "icml2026_taxonomy_adjudication_queue.csv")
    artifact_audit = optional_csv(PROCESSED / "icml2026_artifact_audit_queue.csv")
    baseline_sensitivity = optional_csv(PROCESSED / "icml2026_baseline_sensitivity_queue.csv")
    paper_note_bridge = optional_csv(PROCESSED / "icml2026_paper_note_overlay_bridge.csv")
    review_sprint_02 = optional_csv(PROCESSED / "icml2026_review_sprint_02.csv")
    sprint_02_bridge = optional_csv(PROCESSED / "icml2026_sprint_02_overlay_bridge.csv")
    codebook = optional_csv(PROCESSED / "icml2026_manual_review_codebook.csv")
    value_lint = optional_csv(PROCESSED / "icml2026_manual_review_value_lint.csv")
    review_execution_dashboard = optional_csv(PROCESSED / "icml2026_review_execution_dashboard.csv")
    review_execution_actions = optional_csv(PROCESSED / "icml2026_review_execution_claim_actions.csv")
    review_decision_tasks = optional_csv(PROCESSED / "icml2026_review_decision_tasks.csv")
    paper_source_access = optional_csv(PROCESSED / "icml2026_paper_source_access_map.csv")
    pdf_extraction_probe = optional_csv(PROCESSED / "icml2026_pdf_extraction_probe.csv")
    pdf_review_cards = optional_csv(PROCESSED / "icml2026_pdf_review_cards.csv")
    pdf_review_worksheet = optional_csv(PROCESSED / "icml2026_pdf_review_worksheet.csv")
    pdf_review_transfer = optional_csv(PROCESSED / "icml2026_pdf_review_transfer_checklist.csv")

    claim_done = reviewed_count(claim_reviewed)
    area_done = reviewed_count(area_reviewed)
    total_done = claim_done + area_done
    total_review = len(claim_reviewed) + len(area_reviewed)
    notes_started = sum(note_started(row) for row in paper_notes)
    high_priority_claims = sum(row.get("readiness_tier") == "high_priority_unreviewed" for row in readiness)
    high_risk_areas = sum(row.get("readiness_tier") == "high" for row in readiness)
    validation_failures = sum(row.get("status") == "fail" for row in validation)
    promote_candidates = sum(row.get("decision") == "promote_candidate" for row in acceptance)
    current_sprint_unblockable = sum(int(float(row.get("claim_bridge_rows", 0) or 0)) > 0 for row in decision_board)
    active_claim_actions = sum(row.get("action_priority") in {"1", "2"} for row in review_execution_actions)

    rows: list[dict[str, object]] = [
        {
            "priority": 1,
            "gap": "No human judgments have been merged yet",
            "why_it_matters": "The workspace is broad, but paper-level support for synthesis claims is still unverified.",
            "current_signal": f"{total_done}/{total_review} reviewed rows ({pct(total_done, total_review)}); {len(codebook)} canonical codebook rows available; {len(value_lint)} invalid coded values",
            "recommended_artifact": "Filled claim and area overlay CSVs plus regenerated reviewed validation tables",
            "next_action": "Complete the first 40-paper review sprint, then rerun reviewed tables, progress, readiness, and validation.",
        },
        {
            "priority": 2,
            "gap": "Abstract/title evidence is not enough for novelty and method claims",
            "why_it_matters": "A researcher needs to know what is technically new, what is borrowed, and what is only benchmark packaging.",
            "current_signal": f"{len(review_plan)} unique papers queued; {len(review_decision_tasks)} paper-by-claim decision tasks defined; {len(paper_source_access)} sprint papers have source-access rows; {len(pdf_extraction_probe)} priority PDFs probed for extractability; {len(pdf_review_cards)} page-level PDF review cards generated; {len(pdf_review_worksheet)} reviewer worksheet rows prepared; {len(pdf_review_transfer)} focused transfer rows prepared; {notes_started}/{len(paper_notes)} first-sprint paper notes started; {len(paper_note_bridge)} sprint-01 transfer rows and {len(sprint_02_bridge)} sprint-02 transfer rows queued",
            "recommended_artifact": "Paper-note sheets with contribution, mechanism, evidence strength, and limitations fields",
            "next_action": "For the top-ranked papers, extract the claimed contribution, core method, baselines, ablations, and failure cases from the PDF.",
        },
        {
            "priority": 3,
            "gap": "Area taxonomy is useful but still partially heuristic",
            "why_it_matters": "The 12-area map is readable, but boundary clusters can distort area shares and trend claims.",
            "current_signal": f"{high_risk_areas} high-risk area rows; {len(taxonomy_adjudication)} semantic clusters queued for adjudication",
            "recommended_artifact": "Taxonomy adjudication log for boundary papers and mixed semantic clusters",
            "next_action": "Resolve taxonomy-boundary rows before making subarea share claims or ranking areas by importance.",
        },
        {
            "priority": 4,
            "gap": "AlphaXiv votes are attention, not quality",
            "why_it_matters": "Popular papers may be demos, infrastructure, or already-famous topics rather than the strongest technical work.",
            "current_signal": f"AlphaXiv is joined to all official paper rows; {len(divergence)} papers queued for public/program calibration reading.",
            "recommended_artifact": "Public-attention calibration notes for high-vote/non-oral and low-vote/oral papers",
            "next_action": "Read the public/program divergence set and label whether attention tracks novelty, utility, accessibility, or hype.",
        },
        {
            "priority": 5,
            "gap": "Reproducibility is still URL visibility",
            "why_it_matters": "A GitHub link is not evidence that code runs, data are available, or results are reproducible.",
            "current_signal": f"Artifact fields are useful for triage; {len(artifact_audit)} papers queued for artifact/repository audit.",
            "recommended_artifact": "Repository audit table with license, release state, dependencies, data access, and runnable example",
            "next_action": "Manually inspect high-signal GitHub-linked papers before writing reproducibility claims.",
        },
        {
            "priority": 6,
            "gap": "Historical and arXiv baselines are context, not causal evidence",
            "why_it_matters": "Accepted-paper baselines and broad arXiv queries can show direction, but they can mislead on venue policy or field momentum.",
            "current_signal": f"Trend and historical reports exist; {len(baseline_sensitivity)} area-level baseline sensitivity rows queued for spot-checking.",
            "recommended_artifact": "Classifier spot-check sheet and query sensitivity table",
            "next_action": "Spot-check largest positive/negative deltas and test alternate query terms before using trend claims.",
        },
        {
            "priority": 7,
            "gap": "The thesis hierarchy exists, but it is still mostly unpromoted",
            "why_it_matters": "The project has many artifacts; a reader needs a small number of defensible claims with clear evidence status.",
            "current_signal": f"{len(thesis_map)} claims mapped; {high_priority_claims} high-priority unreviewed claims; {active_claim_actions}/{len(review_execution_actions)} active claim actions queued; {current_sprint_unblockable}/{len(decision_board)} claims have first-sprint bridge rows; {len(review_sprint_02)} sprint-02 papers cover C04/C05",
            "recommended_artifact": "Thesis map with claim, evidence type, trust tier, representative papers, and caveats",
            "next_action": "After the first sprint, promote only checked claims into the overview seed and demote the rest to hypotheses.",
        },
        {
            "priority": 8,
            "gap": "Semantic validation gates exist, but no claim passes them yet",
            "why_it_matters": "Passing row-count and coverage checks does not prove the interpretations are correct.",
            "current_signal": f"{len(validation)} automated checks, {validation_failures} failures; {len(review_execution_dashboard)} execution metrics tracked; {promote_candidates}/{len(acceptance)} claims promotable",
            "recommended_artifact": "Semantic validation checklist tied to manual paper notes",
            "next_action": "Keep structural validation, but add claim-level acceptance criteria once manual review fields are filled.",
        },
    ]

    write_csv(
        PROCESSED / "icml2026_researcher_gap_audit.csv",
        rows,
        ["priority", "gap", "why_it_matters", "current_signal", "recommended_artifact", "next_action"],
    )

    lines = [
        "# ICML 2026 Researcher Gap Audit",
        "",
        "Critical feedback on what remains before this workspace becomes a high-confidence ML research landscape brief.",
        "",
        "## Snapshot",
        "",
        f"- Official corpus rows: {len(papers)}",
        f"- Manual validation reviewed: {total_done}/{total_review} ({pct(total_done, total_review)})",
        f"- Manual review codebook rows: {len(codebook)}",
        f"- Manual review invalid coded values: {len(value_lint)}",
        f"- Review execution metrics tracked: {len(review_execution_dashboard)}",
        f"- Active review execution claim actions queued: {active_claim_actions}/{len(review_execution_actions)}",
        f"- Unique papers in the review plan: {len(review_plan)}",
        f"- Paper-by-claim decision tasks queued: {len(review_decision_tasks)}",
        f"- Sprint papers with source-access rows: {len(paper_source_access)}",
        f"- Priority PDFs probed for extractability: {len(pdf_extraction_probe)}",
        f"- Page-level PDF review cards: {len(pdf_review_cards)}",
        f"- PDF review worksheet rows: {len(pdf_review_worksheet)}",
        f"- Focused PDF review transfer rows: {len(pdf_review_transfer)}",
        f"- First-sprint paper notes started: {notes_started}/{len(paper_notes)}",
        f"- Paper-note overlay transfer rows queued: {len(paper_note_bridge)}",
        f"- Sprint 02 uncovered-claim papers queued: {len(review_sprint_02)}",
        f"- Sprint 02 overlay transfer rows queued: {len(sprint_02_bridge)}",
        f"- High-priority unreviewed claims: {high_priority_claims}",
        f"- High-risk areas: {high_risk_areas}",
        f"- Structural validation failures: {validation_failures}",
        f"- Claims passing acceptance criteria: {promote_candidates}/{len(acceptance)}",
        f"- Claims with first-sprint decision-board bridge rows: {current_sprint_unblockable}/{len(decision_board)}",
        f"- Public/program divergence papers queued: {len(divergence)}",
        f"- Taxonomy clusters queued for adjudication: {len(taxonomy_adjudication)}",
        f"- Artifact audit papers queued: {len(artifact_audit)}",
        f"- Baseline sensitivity rows queued: {len(baseline_sensitivity)}",
        "",
        "## Critical Feedback",
        "",
        "| Priority | Gap | Why it matters | Current signal | Next action |",
        "| ---: | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['priority']} | {row['gap']} | {row['why_it_matters']} | "
            f"{row['current_signal']} | {row['next_action']} |"
        )

    lines.extend(
        [
            "",
            "## Researcher-Grade Target State",
            "",
            "- A checked thesis map where every headline claim points to reviewed paper rows.",
            "- Paper notes for the first sprint that separate novelty, method, evidence, limitations, and artifact status.",
            "- A resolved taxonomy-boundary log for the areas most likely to drive the report narrative.",
            "- Explicit calibration for public attention versus program selection.",
            "- Reproducibility claims based on repository inspection, not link existence.",
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_researcher_gap_audit.csv`",
            "- `reports/icml2026_researcher_gap_audit.md`",
        ]
    )
    (REPORTS / "icml2026_researcher_gap_audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {PROCESSED / 'icml2026_researcher_gap_audit.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_researcher_gap_audit.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
