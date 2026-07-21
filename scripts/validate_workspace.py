#!/usr/bin/env python3
"""Validate core invariants for the ICML 2026 EDA workspace."""

from __future__ import annotations

import csv
import json
import re
import struct
import sys
from collections import Counter
from pathlib import Path

from build_newcomer_slides import AREA_TECHNICAL
from learning_content import COMPARISON_PAPERS, PAPER_CASES


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
MANUAL = ROOT / "data" / "manual"
REPORTS = ROOT / "reports"
FIGURES = ROOT / "figures"
DOCS = ROOT / "docs"

EXPECTED_FIGURES = [
    "topic_group_distribution.png",
    "theme_counts_orals.png",
    "cluster_vote_density_oral_enrichment.png",
    "cluster_public_vs_program_signal.png",
    "alphaxiv_attention_distributions.png",
    "top_canonical_institutions.png",
    "sector_mix_papers.png",
    "institution_collaboration_hubs.png",
    "team_size_distribution.png",
    "semantic_cluster_map.png",
    "semantic_cluster_vote_density.png",
    "manual_taxonomy_area_sizes.png",
    "evidence_contribution_mix.png",
    "program_signal_calibration.png",
    "arxiv_taxonomy_trends.png",
    "historical_venue_area_deltas.png",
]

EXPECTED_REPORTS = [
    "icml2026_newcomer_area_tour.md",
    "icml2026_newcomer_trend_lessons.md",
    "icml2026_newcomer_paper_course.md",
    "icml2026_newcomer_final_quiz.md",
    "icml2026_newcomer_quiz_answer_key.md",
    "icml2026_newcomer_briefing_template.md",
    "icml2026_newcomer_course_audit.md",
    "icml2026_pdf_review_seed_judgments.md",
    "icml2026_landscape_synthesis.md",
    "icml2026_overview_report_seed.md",
    "icml2026_story_outline_seed.md",
    "icml2026_researcher_audit.md",
    "icml2026_researcher_readiness_audit.md",
    "icml2026_researcher_thesis_map.md",
    "icml2026_claim_acceptance_criteria.md",
    "icml2026_claim_decision_board.md",
    "icml2026_claim_risk_register.md",
    "icml2026_safe_statement_register.md",
    "icml2026_review_execution_dashboard.md",
    "icml2026_researcher_action_plan.md",
    "icml2026_research_questions_agenda.md",
    "icml2026_review_decision_tasks.md",
    "icml2026_paper_source_access_map.md",
    "icml2026_pdf_extraction_probe.md",
    "icml2026_pdf_review_cards.md",
    "icml2026_pdf_review_worksheet.md",
    "icml2026_pdf_review_transfer_checklist.md",
    "icml2026_researcher_gap_audit.md",
    "icml2026_researcher_review_plan.md",
    "icml2026_review_sprint_01.md",
    "icml2026_review_sprint_02.md",
    "icml2026_sprint_reading_brief_index.md",
    "icml2026_sprint_prereview_suggestions.md",
    "icml2026_sprint_02_prereview_suggestions.md",
    "icml2026_paper_note_workspace.md",
    "icml2026_sprint_02_paper_note_workspace.md",
    "icml2026_manual_review_codebook.md",
    "icml2026_manual_review_value_lint.md",
    "icml2026_paper_note_overlay_bridge.md",
    "icml2026_sprint_02_overlay_bridge.md",
    "manual_review_workspace.md",
    "reviewed_validation_tables.md",
    "icml2026_claim_evidence_dossier_index.md",
    "icml2026_area_briefing_card_index.md",
    "icml2026_area_risk_register.md",
    "icml2026_claim_validation_packet_index.md",
    "icml2026_validation_packet_index.md",
    "icml2026_program_signal_calibration.md",
    "icml2026_public_program_divergence_set.md",
    "icml2026_taxonomy_adjudication_queue.md",
    "icml2026_artifact_audit_queue.md",
    "icml2026_baseline_sensitivity_queue.md",
    "historical_accepted_paper_baseline.md",
    "arxiv_taxonomy_trends.md",
    "icml2026_visual_eda_index.md",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def png_dimensions(path: Path) -> tuple[int, int] | None:
    if not path.exists():
        return None
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", header[16:24])


class Validator:
    def __init__(self) -> None:
        self.rows: list[dict[str, object]] = []

    def check(self, check_id: str, status: str, message: str, expected: object = "", actual: object = "", severity: str = "error") -> None:
        self.rows.append(
            {
                "check_id": check_id,
                "status": status,
                "severity": severity,
                "expected": expected,
                "actual": actual,
                "message": message,
            }
        )

    def expect(self, check_id: str, condition: bool, message: str, expected: object = "", actual: object = "", severity: str = "error") -> None:
        self.check(check_id, "pass" if condition else "fail", message, expected, actual, severity)


def validate() -> tuple[list[dict[str, object]], int]:
    v = Validator()

    papers = read_csv(PROCESSED / "icml2026_papers.csv")
    alphaxiv = read_csv(PROCESSED / "alphaxiv_icml2026_joined.csv")
    taxonomy_papers = read_csv(PROCESSED / "icml2026_manual_taxonomy_papers.csv")
    taxonomy_areas = read_csv(PROCESSED / "icml2026_manual_taxonomy_areas.csv")
    taxonomy_adjudication = read_csv(PROCESSED / "icml2026_taxonomy_adjudication_queue.csv")
    semantic_clusters = read_csv(PROCESSED / "icml2026_semantic_cluster_summary.csv")
    evidence = read_csv(PROCESSED / "icml2026_paper_evidence_codes.csv")
    paper_explorer = read_csv(PROCESSED / "icml2026_paper_explorer.csv")
    claim_register = read_csv(PROCESSED / "icml2026_landscape_claim_register.csv")
    claim_queue = read_csv(PROCESSED / "icml2026_claim_validation_queue.csv")
    area_queue = read_csv(PROCESSED / "icml2026_manual_validation_queue.csv")
    reviewed_claim_queue = read_csv(PROCESSED / "icml2026_claim_validation_reviewed.csv")
    reviewed_area_queue = read_csv(PROCESSED / "icml2026_area_validation_reviewed.csv")
    review_progress = read_csv(PROCESSED / "manual_review_progress.csv")
    readiness_audit = read_csv(PROCESSED / "icml2026_researcher_readiness_audit.csv")
    thesis_map = read_csv(PROCESSED / "icml2026_researcher_thesis_map.csv")
    acceptance_criteria = read_csv(PROCESSED / "icml2026_claim_acceptance_criteria.csv")
    claim_decision_board = read_csv(PROCESSED / "icml2026_claim_decision_board.csv")
    claim_risk_register = read_csv(PROCESSED / "icml2026_claim_risk_register.csv")
    safe_statement_register = read_csv(PROCESSED / "icml2026_safe_statement_register.csv")
    review_execution_dashboard = read_csv(PROCESSED / "icml2026_review_execution_dashboard.csv")
    review_execution_actions = read_csv(PROCESSED / "icml2026_review_execution_claim_actions.csv")
    researcher_action_plan = read_csv(PROCESSED / "icml2026_researcher_action_plan.csv")
    research_questions = read_csv(PROCESSED / "icml2026_research_questions_agenda.csv")
    review_decision_tasks = read_csv(PROCESSED / "icml2026_review_decision_tasks.csv")
    paper_source_access = read_csv(PROCESSED / "icml2026_paper_source_access_map.csv")
    pdf_extraction_probe = read_csv(PROCESSED / "icml2026_pdf_extraction_probe.csv")
    pdf_review_cards = read_csv(PROCESSED / "icml2026_pdf_review_cards.csv")
    pdf_page_cues = read_csv(PROCESSED / "icml2026_pdf_page_cues.csv")
    pdf_review_worksheet = read_csv(PROCESSED / "icml2026_pdf_review_worksheet.csv")
    pdf_review_transfer = read_csv(PROCESSED / "icml2026_pdf_review_transfer_checklist.csv")
    gap_audit = read_csv(PROCESSED / "icml2026_researcher_gap_audit.csv")
    claim_dossiers = read_csv(PROCESSED / "icml2026_claim_evidence_dossiers.csv")
    review_plan = read_csv(PROCESSED / "icml2026_researcher_review_plan.csv")
    review_sprint = read_csv(PROCESSED / "icml2026_review_sprint_01.csv")
    review_sprint_02 = read_csv(PROCESSED / "icml2026_review_sprint_02.csv")
    sprint_reading_briefs = read_csv(PROCESSED / "icml2026_sprint_reading_briefs.csv")
    prereview_suggestions = read_csv(PROCESSED / "icml2026_sprint_prereview_suggestions.csv")
    prereview_suggestions_02 = read_csv(PROCESSED / "icml2026_sprint_02_prereview_suggestions.csv")
    paper_notes = read_csv(MANUAL / "icml2026_review_sprint_01_paper_notes.csv")
    paper_notes_02 = read_csv(MANUAL / "icml2026_review_sprint_02_paper_notes.csv")
    manual_codebook = read_csv(PROCESSED / "icml2026_manual_review_codebook.csv")
    manual_value_lint = read_csv(PROCESSED / "icml2026_manual_review_value_lint.csv")
    manual_value_lint_summary = read_csv(PROCESSED / "icml2026_manual_review_value_lint_summary.csv")
    paper_note_bridge = read_csv(PROCESSED / "icml2026_paper_note_overlay_bridge.csv")
    paper_note_bridge_02 = read_csv(PROCESSED / "icml2026_sprint_02_overlay_bridge.csv")
    area_briefings = read_csv(PROCESSED / "icml2026_area_briefing_cards.csv")
    area_risk_register = read_csv(PROCESSED / "icml2026_area_risk_register.csv")
    divergence_set = read_csv(PROCESSED / "icml2026_public_program_divergence_set.csv")
    artifact_audit = read_csv(PROCESSED / "icml2026_artifact_audit_queue.csv")
    baseline_sensitivity = read_csv(PROCESSED / "icml2026_baseline_sensitivity_queue.csv")
    claim_overrides = read_csv(MANUAL / "claim_review_overrides.csv")
    area_overrides = read_csv(MANUAL / "area_review_overrides.csv")
    arxiv = read_csv(PROCESSED / "arxiv_taxonomy_trend_summary.csv")
    historical = read_csv(PROCESSED / "historical_venue_delta_summary.csv")
    inventory = read_csv(PROCESSED / "project_artifact_inventory.csv")

    v.expect("corpus.paper_count", len(papers) == 6628, "Official ICML paper table should have 6,628 rows.", 6628, len(papers))
    v.expect("corpus.alphaxiv_join_count", len(alphaxiv) == len(papers), "AlphaXiv joined table should cover all official ICML papers.", len(papers), len(alphaxiv))
    v.expect("corpus.taxonomy_paper_count", len(taxonomy_papers) == len(papers), "Manual taxonomy paper table should cover all official ICML papers.", len(papers), len(taxonomy_papers))
    v.expect("corpus.evidence_count", len(evidence) == len(papers), "Evidence-code table should cover all official ICML papers.", len(papers), len(evidence))
    v.expect("corpus.paper_explorer_count", len(paper_explorer) == len(papers), "Paper explorer table should cover all official ICML papers.", len(papers), len(paper_explorer))

    paper_ids = {row["event_id"] for row in papers}
    taxonomy_ids = {row["event_id"] for row in taxonomy_papers}
    evidence_ids = {row["event_id"] for row in evidence}
    explorer_ids = {row["event_id"] for row in paper_explorer}
    v.expect("corpus.taxonomy_event_ids", taxonomy_ids == paper_ids, "Taxonomy event IDs should match official paper event IDs.", len(paper_ids), len(taxonomy_ids))
    v.expect("corpus.evidence_event_ids", evidence_ids == paper_ids, "Evidence-code event IDs should match official paper event IDs.", len(paper_ids), len(evidence_ids))
    v.expect("corpus.paper_explorer_event_ids", explorer_ids == paper_ids, "Paper explorer event IDs should match official paper event IDs.", len(paper_ids), len(explorer_ids))

    selected_comparisons = [selection for number in sorted(COMPARISON_PAPERS) for selection in COMPARISON_PAPERS[number]]
    selected_titles = [selection["title"] for selection in selected_comparisons]
    explorer_by_title = {row["title"]: row for row in paper_explorer}
    area_names = {int(area["number"]): str(area["area"]) for area in AREA_TECHNICAL}
    v.expect(
        "learning.selection_structure",
        set(COMPARISON_PAPERS) == set(range(1, 13))
        and all(len(COMPARISON_PAPERS[number]) == 2 for number in range(1, 13))
        and len(set(selected_titles)) == 24
        and all(selection.get("role", "").strip() for selection in selected_comparisons),
        "The course should select two distinct, purpose-labeled comparison papers for every area.",
        "12 areas, 24 unique cases, all roles present",
        f"{len(COMPARISON_PAPERS)} areas, {len(set(selected_titles))} unique cases",
    )
    v.expect(
        "learning.selection_content",
        set(PAPER_CASES) == set(selected_titles) and all(title in explorer_by_title for title in selected_titles),
        "The teaching-case catalog should exactly match the selected comparison papers, with official explorer metadata for every case.",
        "24 selected cases, no unused cases, all metadata records present",
        sum(title in PAPER_CASES and title in explorer_by_title for title in selected_titles),
    )
    v.expect(
        "learning.selection_taxonomy_confidence",
        all(explorer_by_title.get(title, {}).get("taxonomy_confidence") == "high" for title in selected_titles),
        "Selected comparison papers should have high-confidence area assignments.",
        "24 high-confidence selections",
        sum(explorer_by_title.get(title, {}).get("taxonomy_confidence") == "high" for title in selected_titles),
    )
    v.expect(
        "learning.selection_area_fit",
        all(
            explorer_by_title.get(selection["title"], {}).get("area") == area_names[number]
            for number, selections in COMPARISON_PAPERS.items()
            for selection in selections
        ),
        "Every comparison paper should belong to the area lesson where it is taught.",
        "24 area-aligned selections",
        sum(
            explorer_by_title.get(selection["title"], {}).get("area") == area_names[number]
            for number, selections in COMPARISON_PAPERS.items()
            for selection in selections
        ),
    )

    area_counts = Counter(row["area"] for row in taxonomy_papers)
    v.expect("taxonomy.area_count", len(taxonomy_areas) == 12, "Manual taxonomy should contain 12 report-level areas.", 12, len(taxonomy_areas))
    v.expect("area_briefings.row_count", len(area_briefings) == 12, "Area briefing card CSV should contain 12 area rows.", 12, len(area_briefings))
    v.expect("area_briefings.coverage", {row.get("area", "") for row in area_briefings} == {row["area"] for row in taxonomy_areas}, "Area briefing cards should cover every taxonomy area.", len(taxonomy_areas), len({row.get("area", "") for row in area_briefings}))
    v.expect("area_risk_register.row_count", len(area_risk_register) == len(taxonomy_areas), "Area risk register should contain one row per taxonomy area.", len(taxonomy_areas), len(area_risk_register))
    v.expect("area_risk_register.coverage", {row.get("area", "") for row in area_risk_register} == {row["area"] for row in taxonomy_areas}, "Area risk register should cover every taxonomy area.", len(taxonomy_areas), len({row.get("area", "") for row in area_risk_register}))
    v.expect("area_risk_register.risk_mix", {"critical", "high"}.intersection({row.get("risk_tier", "") for row in area_risk_register}) != set(), "Area risk register should identify at least one critical or high-risk area.", "critical/high risk tiers", sorted({row.get("risk_tier", "") for row in area_risk_register}))
    v.expect("area_risk_register.falsification_tests", all(row.get("falsification_test", "").strip() for row in area_risk_register), "Every area risk row should include a falsification test.", "all present", "all present" if all(row.get("falsification_test", "").strip() for row in area_risk_register) else "missing")
    v.expect("public_program_divergence.row_count", len(divergence_set) >= 100, "Public/program divergence reading set should contain a focused but substantial paper-level calibration set.", ">=100", len(divergence_set))
    v.expect("public_program_divergence.category_mix", {"public_ahead_of_program", "program_ahead_of_public"}.issubset({row.get("category", "") for row in divergence_set}), "Public/program divergence set should include both public-ahead and program-ahead categories.", "public/program categories", sorted({row.get("category", "") for row in divergence_set}))
    v.expect("artifact_audit.row_count", len(artifact_audit) >= 100, "Artifact audit queue should contain a substantial paper-level reproducibility inspection set.", ">=100", len(artifact_audit))
    v.expect("artifact_audit.category_mix", {"high_signal_no_github", "linked_needs_repro_check"}.intersection({row.get("audit_category", "") for row in artifact_audit}) != set(), "Artifact audit queue should include artifact-linked or high-signal missing-artifact categories.", "artifact audit categories", sorted({row.get("audit_category", "") for row in artifact_audit}))
    v.expect("baseline_sensitivity.row_count", len(baseline_sensitivity) == len(taxonomy_areas), "Baseline sensitivity queue should contain one row per taxonomy area.", len(taxonomy_areas), len(baseline_sensitivity))
    v.expect("baseline_sensitivity.area_coverage", {row.get("area", "") for row in baseline_sensitivity} == {row["area"] for row in taxonomy_areas}, "Baseline sensitivity queue should cover every taxonomy area.", len(taxonomy_areas), len({row.get("area", "") for row in baseline_sensitivity}))
    v.expect("baseline_sensitivity.risk_mix", {"high", "moderate"}.intersection({row.get("risk_tier", "") for row in baseline_sensitivity}) != set(), "Baseline sensitivity queue should identify at least one high or moderate risk baseline row.", "high/moderate risk rows", sorted({row.get("risk_tier", "") for row in baseline_sensitivity}))
    v.expect("taxonomy.semantic_cluster_count", len(semantic_clusters) == 42, "Semantic cluster summary should contain 42 clusters.", 42, len(semantic_clusters))
    needs_review_clusters = {row["semantic_cluster_id"] for row in read_csv(PROCESSED / "icml2026_manual_taxonomy_clusters.csv") if row.get("review_status") == "needs_review"}
    v.expect("taxonomy_adjudication.row_count", len(taxonomy_adjudication) == len(needs_review_clusters), "Taxonomy adjudication queue should contain one row per cluster needing review.", len(needs_review_clusters), len(taxonomy_adjudication))
    v.expect("taxonomy_adjudication.cluster_coverage", {row.get("semantic_cluster_id", "") for row in taxonomy_adjudication} == needs_review_clusters, "Taxonomy adjudication queue should cover every cluster needing review.", len(needs_review_clusters), len({row.get("semantic_cluster_id", "") for row in taxonomy_adjudication}))
    v.expect("taxonomy.area_coverage", set(area_counts) == {row["area"] for row in taxonomy_areas}, "Taxonomy paper areas should match taxonomy area summary.", len(taxonomy_areas), len(area_counts))
    v.expect("taxonomy.area_sum", sum(area_counts.values()) == len(papers), "Taxonomy area counts should sum to corpus size.", len(papers), sum(area_counts.values()))

    v.expect("claims.register_count", len(claim_register) == 8, "Landscape claim register should contain 8 synthesis claims.", 8, len(claim_register))
    v.expect("claims.queue_count", len(claim_queue) == 118, "Claim validation queue should contain 118 paper-review rows.", 118, len(claim_queue))
    v.expect("reviewed_tables.claim_row_count", len(reviewed_claim_queue) == len(claim_queue), "Reviewed claim table should have one row per claim queue row.", len(claim_queue), len(reviewed_claim_queue))
    v.expect("reviewed_tables.area_row_count", len(reviewed_area_queue) == len(area_queue), "Reviewed area table should have one row per area queue row.", len(area_queue), len(reviewed_area_queue))
    reviewed_claim_keys = {(row.get("claim_id", ""), row.get("event_id", "")) for row in reviewed_claim_queue}
    reviewed_area_keys = {(row.get("area", ""), row.get("event_id", "")) for row in reviewed_area_queue}
    v.expect("reviewed_tables.claim_key_coverage", reviewed_claim_keys == {(row.get("claim_id", ""), row.get("event_id", "")) for row in claim_queue}, "Reviewed claim table keys should match claim queue keys.", len(claim_queue), len(reviewed_claim_keys))
    v.expect("reviewed_tables.area_key_coverage", reviewed_area_keys == {(row.get("area", ""), row.get("event_id", "")) for row in area_queue}, "Reviewed area table keys should match area queue keys.", len(area_queue), len(reviewed_area_keys))
    v.expect("claim_dossiers.row_count", len(claim_dossiers) == len(claim_queue), "Claim evidence dossier CSV should cover every claim validation queue row.", len(claim_queue), len(claim_dossiers))
    dossier_claims = Counter(row.get("claim_id", "") for row in claim_dossiers)
    v.expect("claim_dossiers.claim_coverage", set(dossier_claims) == {row["claim_id"] for row in claim_register}, "Claim evidence dossier CSV should cover every registered claim.", len(claim_register), len(dossier_claims))
    expected_review_ids = {row["event_id"] for row in claim_queue} | {row["event_id"] for row in area_queue}
    plan_ids = {row.get("event_id", "") for row in review_plan}
    v.expect("review_plan.row_count", len(review_plan) == len(expected_review_ids), "Researcher review plan should de-duplicate the union of claim and area review queues.", len(expected_review_ids), len(review_plan))
    v.expect("review_plan.event_coverage", plan_ids == expected_review_ids, "Researcher review plan event IDs should match the union of claim and area review queues.", len(expected_review_ids), len(plan_ids))
    sprint_ids = [row.get("event_id", "") for row in review_sprint]
    expected_sprint_ids = [row.get("event_id", "") for row in review_plan[:40]]
    v.expect("review_sprint.row_count", len(review_sprint) == 40, "Review sprint 01 should contain the top 40 review-plan papers.", 40, len(review_sprint))
    v.expect("review_sprint.top40_alignment", sprint_ids == expected_sprint_ids, "Review sprint 01 should align with the top 40 review-plan event IDs.", "top 40 review plan IDs", "aligned" if sprint_ids == expected_sprint_ids else "mismatch")
    sprint_02_ids = [row.get("event_id", "") for row in review_sprint_02]
    sprint_02_target_counts = Counter(
        claim_id
        for row in review_sprint_02
        for claim_id in [part.strip() for part in row.get("target_claims", "").split(";") if part.strip()]
    )
    v.expect("review_sprint_02.row_count", len(review_sprint_02) == 16, "Review sprint 02 should contain 16 uncovered-claim papers.", 16, len(review_sprint_02))
    v.expect("review_sprint_02.target_claims", sprint_02_target_counts.get("C04", 0) >= 8 and sprint_02_target_counts.get("C05", 0) >= 8, "Review sprint 02 should cover at least 8 papers each for C04 and C05.", "C04>=8, C05>=8", dict(sprint_02_target_counts))
    reading_brief_ids = [row.get("event_id", "") for row in sprint_reading_briefs]
    expected_reading_brief_ids = sprint_ids + sprint_02_ids
    v.expect("sprint_reading_briefs.row_count", len(sprint_reading_briefs) == len(review_sprint) + len(review_sprint_02), "Sprint reading briefs should contain one row per sprint 01 and sprint 02 paper.", len(review_sprint) + len(review_sprint_02), len(sprint_reading_briefs))
    v.expect("sprint_reading_briefs.sprint_alignment", reading_brief_ids == expected_reading_brief_ids, "Sprint reading brief event IDs should align with sprint 01 followed by sprint 02.", "sprint 01 + sprint 02 event IDs", "aligned" if reading_brief_ids == expected_reading_brief_ids else "mismatch")
    v.expect("sprint_reading_briefs.file_paths", all((ROOT / row.get("brief_path", "")).exists() for row in sprint_reading_briefs), "Every sprint reading brief row should point to an existing Markdown brief.", "all present", "all present" if all((ROOT / row.get("brief_path", "")).exists() for row in sprint_reading_briefs) else "missing")
    note_ids = [row.get("event_id", "") for row in paper_notes]
    note_02_ids = [row.get("event_id", "") for row in paper_notes_02]
    suggestion_ids = [row.get("event_id", "") for row in prereview_suggestions]
    suggestion_02_ids = [row.get("event_id", "") for row in prereview_suggestions_02]
    v.expect("paper_notes.row_count", len(paper_notes) == len(review_sprint), "Paper-note workspace should contain one row per first-sprint paper.", len(review_sprint), len(paper_notes))
    v.expect("paper_notes.sprint_alignment", note_ids == sprint_ids, "Paper-note workspace event IDs should align with review sprint 01.", "sprint event IDs", "aligned" if note_ids == sprint_ids else "mismatch")
    v.expect("prereview_suggestions.row_count", len(prereview_suggestions) == len(review_sprint), "Pre-review suggestions should contain one row per first-sprint paper.", len(review_sprint), len(prereview_suggestions))
    v.expect("prereview_suggestions.sprint_alignment", suggestion_ids == sprint_ids, "Pre-review suggestion event IDs should align with review sprint 01.", "sprint event IDs", "aligned" if suggestion_ids == sprint_ids else "mismatch")
    v.expect("paper_notes_02.row_count", len(paper_notes_02) == len(review_sprint_02), "Sprint 02 paper-note workspace should contain one row per sprint 02 paper.", len(review_sprint_02), len(paper_notes_02))
    v.expect("paper_notes_02.sprint_alignment", note_02_ids == sprint_02_ids, "Sprint 02 paper-note workspace event IDs should align with review sprint 02.", "sprint 02 event IDs", "aligned" if note_02_ids == sprint_02_ids else "mismatch")
    v.expect("prereview_suggestions_02.row_count", len(prereview_suggestions_02) == len(review_sprint_02), "Sprint 02 pre-review suggestions should contain one row per sprint 02 paper.", len(review_sprint_02), len(prereview_suggestions_02))
    v.expect("prereview_suggestions_02.sprint_alignment", suggestion_02_ids == sprint_02_ids, "Sprint 02 pre-review suggestion event IDs should align with review sprint 02.", "sprint 02 event IDs", "aligned" if suggestion_02_ids == sprint_02_ids else "mismatch")
    codebook_fields = {(row.get("table", ""), row.get("field", "")) for row in manual_codebook}
    v.expect("manual_codebook.row_count", len(manual_codebook) >= 75, "Manual review codebook should contain detailed coded-value guidance.", ">=75", len(manual_codebook))
    v.expect(
        "manual_codebook.critical_fields",
        {
            ("paper_notes", "paper_read_status"),
            ("paper_notes", "evidence_strength"),
            ("paper_notes", "taxonomy_correction"),
            ("claim_overlay", "manual_claim_support"),
            ("claim_overlay", "manual_artifact_judgment"),
            ("area_overlay", "manual_validated"),
            ("area_overlay", "manual_primary_contribution_type"),
            ("area_overlay", "manual_artifact_status"),
        }.issubset(codebook_fields),
        "Manual review codebook should cover critical paper-note, claim-overlay, and area-overlay fields.",
        "critical field set",
        sorted(codebook_fields),
    )
    claim_support_values = {
        row.get("allowed_value", "")
        for row in manual_codebook
        if row.get("table") == "claim_overlay" and row.get("field") == "manual_claim_support"
    }
    artifact_values = {
        row.get("allowed_value", "")
        for row in manual_codebook
        if row.get("table") == "claim_overlay" and row.get("field") == "manual_artifact_judgment"
    }
    v.expect("manual_codebook.claim_support_values", {"supports", "partial_support", "weakens", "contradicts", "not_applicable", "unclear"}.issubset(claim_support_values), "Manual codebook should use claim-support values recognized by acceptance criteria.", "canonical support values", sorted(claim_support_values))
    v.expect("manual_codebook.artifact_values", {"linked_unchecked", "live_checked", "runnable", "broken", "none", "not_applicable"}.issubset(artifact_values), "Manual codebook should use artifact values recognized by acceptance criteria.", "canonical artifact values", sorted(artifact_values))
    v.expect("manual_value_lint.no_invalid_values", len(manual_value_lint) == 0, "Manual review coded values should all be codebook-valid.", 0, len(manual_value_lint))
    v.expect("manual_value_lint.summary_count", len(manual_value_lint_summary) == 4, "Manual value lint summary should cover claim overlay, area overlay, and both paper-note files.", 4, len(manual_value_lint_summary))
    expected_bridge_count = sum(
        len([part for part in row.get("claim_overlay_keys", "").split("|") if part.strip()])
        + len([part for part in row.get("area_overlay_keys", "").split("|") if part.strip()])
        for row in paper_notes
    )
    bridge_types = Counter(row.get("target_type", "") for row in paper_note_bridge)
    v.expect("paper_note_bridge.row_count", len(paper_note_bridge) == expected_bridge_count, "Paper-note overlay bridge should contain one row per claim/area overlay key in the sprint notes.", expected_bridge_count, len(paper_note_bridge))
    v.expect("paper_note_bridge.target_mix", {"claim", "area"}.issubset(set(bridge_types)), "Paper-note overlay bridge should include claim and area targets.", "claim and area", dict(bridge_types))
    v.expect("paper_note_bridge.targets_present", all(row.get("target_present") == "true" for row in paper_note_bridge), "Paper-note overlay bridge keys should all resolve to existing overlay rows.", "all true", Counter(row.get("target_present", "") for row in paper_note_bridge))
    expected_bridge_02_count = sum(
        len([part for part in row.get("claim_overlay_keys", "").split("|") if part.strip()])
        + len([part for part in row.get("area_overlay_keys", "").split("|") if part.strip()])
        for row in paper_notes_02
    )
    bridge_02_types = Counter(row.get("target_type", "") for row in paper_note_bridge_02)
    v.expect("paper_note_bridge_02.row_count", len(paper_note_bridge_02) == expected_bridge_02_count, "Sprint 02 overlay bridge should contain one row per claim/area overlay key in sprint 02 notes.", expected_bridge_02_count, len(paper_note_bridge_02))
    v.expect("paper_note_bridge_02.target_mix", {"claim", "area"}.issubset(set(bridge_02_types)), "Sprint 02 overlay bridge should include claim and area targets.", "claim and area", dict(bridge_02_types))
    v.expect("paper_note_bridge_02.targets_present", all(str(row.get("target_present", "")).lower() == "true" for row in paper_note_bridge_02), "Sprint 02 overlay bridge keys should all resolve to existing overlay rows.", "all true", Counter(row.get("target_present", "") for row in paper_note_bridge_02))
    v.expect("manual_overlays.claim_row_count", len(claim_overrides) == len(claim_queue), "Claim review overlay should have one row per claim validation queue row.", len(claim_queue), len(claim_overrides))
    v.expect("manual_overlays.area_row_count", len(area_overrides) == len(area_queue), "Area review overlay should have one row per area validation queue row.", len(area_queue), len(area_overrides))
    claim_override_keys = {(row.get("claim_id", ""), row.get("event_id", "")) for row in claim_overrides}
    claim_queue_keys = {(row.get("claim_id", ""), row.get("event_id", "")) for row in claim_queue}
    area_override_keys = {(row.get("area", ""), row.get("event_id", "")) for row in area_overrides}
    area_queue_keys = {(row.get("area", ""), row.get("event_id", "")) for row in area_queue}
    v.expect("manual_overlays.claim_key_coverage", claim_override_keys == claim_queue_keys, "Claim review overlay keys should match claim validation queue keys.", len(claim_queue_keys), len(claim_override_keys))
    v.expect("manual_overlays.area_key_coverage", area_override_keys == area_queue_keys, "Area review overlay keys should match area validation queue keys.", len(area_queue_keys), len(area_override_keys))
    v.expect("review_progress.summary_count", len(review_progress) == 20, "Review progress should summarize 8 claims and 12 areas.", 20, len(review_progress))
    v.expect("readiness_audit.row_count", len(readiness_audit) == 20, "Researcher readiness audit should summarize 8 claims and 12 areas.", 20, len(readiness_audit))
    v.expect("thesis_map.row_count", len(thesis_map) == len(claim_register), "Researcher thesis map should contain one row per registered claim.", len(claim_register), len(thesis_map))
    v.expect("thesis_map.claim_coverage", {row.get("claim_id", "") for row in thesis_map} == {row["claim_id"] for row in claim_register}, "Researcher thesis map should cover every registered claim.", len(claim_register), len({row.get("claim_id", "") for row in thesis_map}))
    v.expect("acceptance_criteria.row_count", len(acceptance_criteria) == len(claim_register), "Claim acceptance criteria should contain one row per registered claim.", len(claim_register), len(acceptance_criteria))
    v.expect("acceptance_criteria.claim_coverage", {row.get("claim_id", "") for row in acceptance_criteria} == {row["claim_id"] for row in claim_register}, "Claim acceptance criteria should cover every registered claim.", len(claim_register), len({row.get("claim_id", "") for row in acceptance_criteria}))
    v.expect("claim_decision_board.row_count", len(claim_decision_board) == len(claim_register), "Claim decision board should contain one row per registered claim.", len(claim_register), len(claim_decision_board))
    v.expect("claim_decision_board.claim_coverage", {row.get("claim_id", "") for row in claim_decision_board} == {row["claim_id"] for row in claim_register}, "Claim decision board should cover every registered claim.", len(claim_register), len({row.get("claim_id", "") for row in claim_decision_board}))
    acceptance_decisions = {row.get("claim_id", ""): row.get("decision", "") for row in acceptance_criteria}
    board_decisions = {row.get("claim_id", ""): row.get("decision", "") for row in claim_decision_board}
    v.expect("claim_decision_board.decision_alignment", board_decisions == acceptance_decisions, "Claim decision board decisions should match claim acceptance criteria.", "same decisions", "aligned" if board_decisions == acceptance_decisions else "mismatch")
    v.expect("claim_risk_register.row_count", len(claim_risk_register) == len(claim_register), "Claim risk register should contain one row per registered claim.", len(claim_register), len(claim_risk_register))
    v.expect("claim_risk_register.claim_coverage", {row.get("claim_id", "") for row in claim_risk_register} == {row["claim_id"] for row in claim_register}, "Claim risk register should cover every registered claim.", len(claim_register), len({row.get("claim_id", "") for row in claim_risk_register}))
    v.expect("claim_risk_register.risk_mix", {"critical", "high"}.issubset({row.get("risk_tier", "") for row in claim_risk_register}), "Claim risk register should identify critical and high-risk claims.", "critical/high risk tiers", sorted({row.get("risk_tier", "") for row in claim_risk_register}))
    v.expect("claim_risk_register.falsification_tests", all(row.get("falsification_test", "").strip() for row in claim_risk_register), "Every claim risk row should include a falsification test.", "all present", "all present" if all(row.get("falsification_test", "").strip() for row in claim_risk_register) else "missing")
    safe_statement_types = Counter(row.get("statement_type", "") for row in safe_statement_register)
    v.expect("safe_statement_register.row_count", len(safe_statement_register) == len(claim_register) + len(taxonomy_areas), "Safe statement register should contain claim and area wording rows.", len(claim_register) + len(taxonomy_areas), len(safe_statement_register))
    v.expect("safe_statement_register.type_mix", safe_statement_types == {"claim": len(claim_register), "area": len(taxonomy_areas)}, "Safe statement register should include all claim and area statements.", f"claim={len(claim_register)}, area={len(taxonomy_areas)}", dict(safe_statement_types))
    v.expect("safe_statement_register.no_promoted_claims", "candidate_for_headline" not in {row.get("wording_status", "") for row in safe_statement_register if row.get("statement_type") == "claim"}, "No claim should be marked headline-ready while acceptance criteria have zero promote candidates.", "no candidate_for_headline", sorted({row.get("wording_status", "") for row in safe_statement_register if row.get("statement_type") == "claim"}))
    v.expect("safe_statement_register.caveats_present", all(row.get("required_caveat", "").strip() for row in safe_statement_register), "Every safe statement row should include a required caveat.", "all present", "all present" if all(row.get("required_caveat", "").strip() for row in safe_statement_register) else "missing")
    v.expect("review_execution_dashboard.row_count", len(review_execution_dashboard) >= 8, "Review execution dashboard should contain operational review metrics.", ">=8", len(review_execution_dashboard))
    v.expect("review_execution_dashboard.metric_mix", {"manual_review", "quality_gate", "claim_gate"}.issubset({row.get("area", "") for row in review_execution_dashboard}), "Review execution dashboard should include manual review, quality gate, and claim gate metrics.", "manual_review/quality_gate/claim_gate", sorted({row.get("area", "") for row in review_execution_dashboard}))
    v.expect("review_execution_actions.row_count", len(review_execution_actions) == len(claim_register), "Review execution claim actions should contain one row per registered claim.", len(claim_register), len(review_execution_actions))
    v.expect("review_execution_actions.claim_coverage", {row.get("claim_id", "") for row in review_execution_actions} == {row["claim_id"] for row in claim_register}, "Review execution claim actions should cover every registered claim.", len(claim_register), len({row.get("claim_id", "") for row in review_execution_actions}))
    v.expect("review_execution_actions.priority_mix", {"1", "2"}.issubset({str(row.get("action_priority", "")) for row in review_execution_actions}), "Review execution claim actions should include sprint-01 and sprint-02 priorities.", "priorities 1 and 2", sorted({str(row.get("action_priority", "")) for row in review_execution_actions}))
    expected_action_budgets = {"30_minutes", "2_hours", "half_day", "1_day", "full_review_sprint"}
    v.expect("researcher_action_plan.row_count", len(researcher_action_plan) == len(expected_action_budgets), "Researcher action plan should contain the standard time-budget rows.", len(expected_action_budgets), len(researcher_action_plan))
    v.expect("researcher_action_plan.budget_coverage", {row.get("time_budget", "") for row in researcher_action_plan} == expected_action_budgets, "Researcher action plan should cover all intended time budgets.", sorted(expected_action_budgets), sorted({row.get("time_budget", "") for row in researcher_action_plan}))
    v.expect("researcher_action_plan.stop_conditions", all(row.get("stop_condition", "").strip() for row in researcher_action_plan), "Every researcher action plan row should include a stop condition.", "all present", "all present" if all(row.get("stop_condition", "").strip() for row in researcher_action_plan) else "missing")
    v.expect("research_questions.row_count", len(research_questions) == 10, "Research questions agenda should contain ten prioritized questions.", 10, len(research_questions))
    priority_values = {row.get("priority", "") for row in research_questions}
    priority_actual = [str(i) for i in range(1, 11) if str(i) in priority_values]
    priority_actual.extend(sorted(value for value in priority_values if value not in {str(i) for i in range(1, 11)}))
    v.expect("research_questions.priority_coverage", priority_values == {str(i) for i in range(1, 11)}, "Research questions agenda should cover priorities 1 through 10.", "1..10", priority_actual)
    v.expect("research_questions.falsification_tests", all(row.get("falsification_test", "").strip() for row in research_questions), "Every research question should include a falsification test.", "all present", "all present" if all(row.get("falsification_test", "").strip() for row in research_questions) else "missing")
    v.expect("research_questions.first_artifacts", all(row.get("first_artifacts_to_open", "").strip() for row in research_questions), "Every research question should include first artifacts to open.", "all present", "all present" if all(row.get("first_artifacts_to_open", "").strip() for row in research_questions) else "missing")
    expected_decision_keys = {
        (row.get("event_id", ""), claim_id)
        for row in sprint_reading_briefs
        for claim_id in [part.strip() for part in row.get("target_claims", "").split(";") if part.strip()]
    }
    decision_task_keys = {(row.get("event_id", ""), row.get("claim_id", "")) for row in review_decision_tasks}
    v.expect("review_decision_tasks.row_count", len(review_decision_tasks) == len(expected_decision_keys), "Review decision tasks should contain one row per sprint paper/claim pair.", len(expected_decision_keys), len(review_decision_tasks))
    v.expect("review_decision_tasks.key_coverage", decision_task_keys == expected_decision_keys, "Review decision task keys should match sprint reading brief paper/claim pairs.", len(expected_decision_keys), len(decision_task_keys))
    v.expect("review_decision_tasks.claim_coverage", {row.get("claim_id", "") for row in review_decision_tasks} == {row["claim_id"] for row in claim_register}, "Review decision tasks should cover every registered claim.", len(claim_register), len({row.get("claim_id", "") for row in review_decision_tasks}))
    v.expect("review_decision_tasks.manual_fields", all(row.get("required_manual_fields", "").strip() for row in review_decision_tasks), "Every review decision task should list required manual fields.", "all present", "all present" if all(row.get("required_manual_fields", "").strip() for row in review_decision_tasks) else "missing")
    source_access_ids = {row.get("event_id", "") for row in paper_source_access}
    sprint_brief_ids = {row.get("event_id", "") for row in sprint_reading_briefs}
    v.expect("paper_source_access.row_count", len(paper_source_access) == len(sprint_reading_briefs), "Paper source access map should contain one row per sprint reading brief.", len(sprint_reading_briefs), len(paper_source_access))
    v.expect("paper_source_access.event_coverage", source_access_ids == sprint_brief_ids, "Paper source access map should cover every sprint reading brief event ID.", len(sprint_brief_ids), len(source_access_ids))
    v.expect("paper_source_access.icml_urls", all(row.get("icml_url", "").strip() for row in paper_source_access), "Every paper source access row should include the ICML page URL.", "all present", "all present" if all(row.get("icml_url", "").strip() for row in paper_source_access) else "missing")
    v.expect("paper_source_access.pdf_coverage", sum(bool(row.get("arxiv_pdf_url", "").strip()) for row in paper_source_access) >= 50, "Most sprint papers should have arXiv PDF URLs when AlphaXiv metadata is available.", ">=50", sum(bool(row.get("arxiv_pdf_url", "").strip()) for row in paper_source_access))
    v.expect("paper_source_access.extraction_fields", all(row.get("required_extraction_fields", "").strip() for row in paper_source_access), "Every paper source access row should include extraction fields.", "all present", "all present" if all(row.get("required_extraction_fields", "").strip() for row in paper_source_access) else "missing")
    probed_ids = [row.get("event_id", "") for row in pdf_extraction_probe]
    source_order_with_pdfs = [row.get("event_id", "") for row in paper_source_access if row.get("arxiv_pdf_url", "").strip()]
    v.expect("pdf_extraction_probe.row_count", len(pdf_extraction_probe) >= 8, "PDF extraction probe should cover at least the first eight source-access papers with arXiv PDFs.", ">=8", len(pdf_extraction_probe))
    v.expect("pdf_extraction_probe.priority_alignment", probed_ids == source_order_with_pdfs[: len(probed_ids)], "PDF extraction probe should follow source-access priority order.", "prefix of source-access PDF rows", "aligned" if probed_ids == source_order_with_pdfs[: len(probed_ids)] else "mismatch")
    v.expect("pdf_extraction_probe.downloads", all(row.get("download_status") in {"downloaded", "cached"} for row in pdf_extraction_probe), "Every PDF extraction probe row should have a downloaded or cached PDF.", "downloaded/cached", sorted({row.get("download_status", "") for row in pdf_extraction_probe}))
    v.expect("pdf_extraction_probe.extractable", all(row.get("extract_status") == "ok" and int(float(row.get("sample_text_chars", 0) or 0)) >= 500 for row in pdf_extraction_probe), "Every PDF extraction probe row should extract at least 500 text characters.", "ok and >=500 chars", "all extractable" if all(row.get("extract_status") == "ok" and int(float(row.get("sample_text_chars", 0) or 0)) >= 500 for row in pdf_extraction_probe) else "not extractable")
    card_ids = {row.get("event_id", "") for row in pdf_review_cards}
    probe_ids = {row.get("event_id", "") for row in pdf_extraction_probe}
    page_cue_ids = {row.get("event_id", "") for row in pdf_page_cues}
    v.expect("pdf_review_cards.row_count", len(pdf_review_cards) == len(pdf_extraction_probe), "PDF review cards should contain one card per PDF extraction probe row.", len(pdf_extraction_probe), len(pdf_review_cards))
    v.expect("pdf_review_cards.event_coverage", card_ids == probe_ids, "PDF review cards should cover every probed PDF event ID.", len(probe_ids), len(card_ids))
    v.expect("pdf_review_cards.page_cue_coverage", page_cue_ids == probe_ids, "PDF page cue rows should cover every probed PDF event ID.", len(probe_ids), len(page_cue_ids))
    v.expect("pdf_review_cards.method_evidence_pages", all(row.get("method_pages", "").strip() and row.get("evidence_pages", "").strip() for row in pdf_review_cards), "Every PDF review card should include method and evidence page suggestions.", "all present", "all present" if all(row.get("method_pages", "").strip() and row.get("evidence_pages", "").strip() for row in pdf_review_cards) else "missing")
    card_files = sorted((REPORTS / "pdf_review_cards").glob("*.md"))
    v.expect("pdf_review_cards.card_file_count", len(card_files) == len(pdf_review_cards), "There should be one Markdown PDF review card per CSV card row.", len(pdf_review_cards), len(card_files))
    worksheet_ids = {row.get("event_id", "") for row in pdf_review_worksheet}
    v.expect("pdf_review_worksheet.row_count", len(pdf_review_worksheet) == len(pdf_review_cards), "PDF review worksheet should contain one row per PDF review card.", len(pdf_review_cards), len(pdf_review_worksheet))
    v.expect("pdf_review_worksheet.event_coverage", worksheet_ids == card_ids, "PDF review worksheet should cover every PDF review card event ID.", len(card_ids), len(worksheet_ids))
    worksheet_blank = all(
        not row.get("paper_read_status")
        and not row.get("contribution_summary")
        and not row.get("evidence_strength")
        and not row.get("claim_implications")
        for row in pdf_review_worksheet
    )
    v.expect("pdf_review_worksheet.blank_judgments", worksheet_blank, "PDF review worksheet generated judgment fields should remain blank until human review.", "blank generated fields", "blank" if worksheet_blank else "filled")
    v.expect("pdf_review_worksheet.navigation_fields", all(row.get("pdf_card_path", "").strip() and row.get("method_pages", "").strip() and row.get("evidence_pages", "").strip() and row.get("paper_note_file", "").strip() for row in pdf_review_worksheet), "Every PDF review worksheet row should include card path, method/evidence pages, and writeback file.", "all present", "all present" if all(row.get("pdf_card_path", "").strip() and row.get("method_pages", "").strip() and row.get("evidence_pages", "").strip() and row.get("paper_note_file", "").strip() for row in pdf_review_worksheet) else "missing")
    transfer_ids = {row.get("event_id", "") for row in pdf_review_transfer}
    transfer_types = Counter(row.get("target_type", "") for row in pdf_review_transfer)
    v.expect("pdf_review_transfer.row_count", len(pdf_review_transfer) >= len(pdf_review_worksheet) * 2, "PDF review transfer checklist should include claim and area transfer rows for worksheet papers.", f">={len(pdf_review_worksheet) * 2}", len(pdf_review_transfer))
    v.expect("pdf_review_transfer.event_coverage", transfer_ids == worksheet_ids, "PDF review transfer checklist should cover every PDF review worksheet event ID.", len(worksheet_ids), len(transfer_ids))
    v.expect("pdf_review_transfer.target_mix", {"claim", "area"}.issubset(set(transfer_types)), "PDF review transfer checklist should include both claim and area targets.", "claim and area", dict(transfer_types))
    v.expect("pdf_review_transfer.targets_present", all(row.get("target_present") == "true" for row in pdf_review_transfer), "Every PDF review transfer checklist row should point to an existing overlay target.", "all true", "all true" if all(row.get("target_present") == "true" for row in pdf_review_transfer) else "missing")
    v.expect("gap_audit.row_count", len(gap_audit) >= 8, "Researcher gap audit should contain ranked critical-feedback rows.", ">=8", len(gap_audit))
    audit_types = Counter(row.get("audit_type", "") for row in readiness_audit)
    v.expect("readiness_audit.type_mix", audit_types == {"claim": 8, "area": 12}, "Readiness audit should include 8 claim rows and 12 area rows.", "claim=8, area=12", dict(audit_types))
    remaining_total = sum(int(float(row.get("remaining_rows", 0) or 0)) for row in review_progress)
    v.expect("review_progress.remaining_total", remaining_total == 310, "Current manual review queue should have 310 remaining rows before human review.", 310, remaining_total, "warning")
    claim_counts = Counter(row["claim_id"] for row in claim_queue)
    v.expect("claims.queue_covers_all_claims", set(claim_counts) == {row["claim_id"] for row in claim_register}, "Claim validation queue should cover every registered claim.", len(claim_register), len(claim_counts))
    manual_blank = all(
        not row.get("manual_claim_support")
        and not row.get("manual_taxonomy_judgment")
        and not row.get("manual_artifact_judgment")
        for row in claim_queue
    )
    v.expect("claims.manual_fields_blank", manual_blank, "Claim validation manual fields should remain blank until human review.", "all blank", "all blank" if manual_blank else "some filled", "warning")

    claim_packets = sorted((REPORTS / "claim_validation_packets").glob("*.md"))
    claim_evidence_dossiers = sorted((REPORTS / "claim_evidence_dossiers").glob("*.md"))
    area_briefing_cards = sorted((REPORTS / "area_briefing_cards").glob("*.md"))
    area_packets = sorted((REPORTS / "validation_packets").glob("*.md"))
    v.expect("packets.claim_packet_count", len(claim_packets) == 8, "There should be 8 claim validation packets.", 8, len(claim_packets))
    v.expect("packets.claim_evidence_dossier_count", len(claim_evidence_dossiers) == 8, "There should be 8 claim evidence dossier files.", 8, len(claim_evidence_dossiers))
    v.expect("packets.area_briefing_card_count", len(area_briefing_cards) == 12, "There should be 12 area briefing card files.", 12, len(area_briefing_cards))
    v.expect("packets.area_packet_count", len(area_packets) == 12, "There should be 12 area validation packets.", 12, len(area_packets))

    v.expect("trends.arxiv_area_count", len(arxiv) == 12, "arXiv trend summary should contain 12 taxonomy areas.", 12, len(arxiv))
    arxiv_complete = all(row.get("status_complete") == "true" for row in arxiv)
    v.expect("trends.arxiv_complete", arxiv_complete, "All arXiv area trend rows should be complete.", "all true", "all true" if arxiv_complete else "incomplete rows")
    v.expect("trends.historical_delta_count", len(historical) == 12, "Historical venue delta summary should contain 12 areas.", 12, len(historical))

    for figure in EXPECTED_FIGURES:
        path = FIGURES / figure
        dims = png_dimensions(path)
        v.expect(f"figures.{figure}", dims is not None, f"Expected PNG figure exists and has valid dimensions: {figure}", "valid PNG", dims or "missing/invalid")

    for report in EXPECTED_REPORTS:
        path = REPORTS / report
        ok = path.exists() and path.stat().st_size > 200
        v.expect(f"reports.{report}", ok, f"Expected report exists and is non-empty: {report}", ">200 bytes", path.stat().st_size if path.exists() else "missing")

    newcomer_roadmap_path = DOCS / "icml2026_newcomer_roadmap.md"
    newcomer_roadmap = newcomer_roadmap_path.read_text(encoding="utf-8") if newcomer_roadmap_path.exists() else ""
    route_names = ["Quick Tour", "Standard Route", "Deep Route"]
    v.expect(
        "newcomer.routes",
        all(name in newcomer_roadmap for name in route_names),
        "Newcomer roadmap should provide quick, standard, and deep routes.",
        route_names,
        [name for name in route_names if name in newcomer_roadmap],
    )
    roadmap_lesson_count = len(re.findall(r"^## Lesson \d+:", newcomer_roadmap, re.M))
    v.expect("newcomer.roadmap_lessons", roadmap_lesson_count == 7, "Newcomer roadmap should contain seven numbered lessons.", 7, roadmap_lesson_count)

    area_tour_path = REPORTS / "icml2026_newcomer_area_tour.md"
    area_tour = area_tour_path.read_text(encoding="utf-8") if area_tour_path.exists() else ""
    area_lesson_count = len(re.findall(r"^## \d+\. ", area_tour, re.M))
    v.expect("newcomer.area_lessons", area_lesson_count == 12, "Newcomer area tour should contain one numbered lesson per taxonomy area.", 12, area_lesson_count)
    v.expect(
        "newcomer.area_quick_checks",
        area_tour.count("**Quick check:**") == 12,
        "Every newcomer area guide should end with a quick understanding check.",
        12,
        area_tour.count("**Quick check:**"),
    )

    trend_lesson_path = REPORTS / "icml2026_newcomer_trend_lessons.md"
    trend_lessons = trend_lesson_path.read_text(encoding="utf-8") if trend_lesson_path.exists() else ""
    trend_lesson_count = len(re.findall(r"^## Trend \d+:", trend_lessons, re.M))
    v.expect("newcomer.trend_lessons", trend_lesson_count == 6, "Newcomer trend guide should contain six evidence-and-caveat lessons.", 6, trend_lesson_count)
    v.expect(
        "newcomer.trend_caveats",
        trend_lessons.count("**Why to be careful:**") == 6,
        "Every newcomer trend lesson should explain why to be careful.",
        6,
        trend_lessons.count("**Why to be careful:**"),
    )

    paper_course_path = REPORTS / "icml2026_newcomer_paper_course.md"
    paper_course = paper_course_path.read_text(encoding="utf-8") if paper_course_path.exists() else ""
    paper_lesson_count = len(re.findall(r"^## Lesson \d+:", paper_course, re.M))
    v.expect("newcomer.paper_lessons", paper_lesson_count == 12, "Newcomer paper course should contain twelve paper lessons.", 12, paper_lesson_count)

    final_quiz_path = REPORTS / "icml2026_newcomer_final_quiz.md"
    final_quiz = final_quiz_path.read_text(encoding="utf-8") if final_quiz_path.exists() else ""
    quiz_parts = len(re.findall(r"^## Part [A-E]:", final_quiz, re.M))
    quiz_points = sum(int(value) for value in re.findall(r"^## Part [A-E]: .*?— (\d+) Points", final_quiz, re.M))
    v.expect("newcomer.quiz_parts", quiz_parts == 5, "Newcomer final quiz should test five skill groups.", 5, quiz_parts)
    v.expect("newcomer.quiz_points", quiz_points == 100, "Newcomer final quiz sections should total 100 points.", 100, quiz_points)

    answer_key_path = REPORTS / "icml2026_newcomer_quiz_answer_key.md"
    answer_key = answer_key_path.read_text(encoding="utf-8") if answer_key_path.exists() else ""
    v.expect(
        "newcomer.answer_key",
        all(label in answer_key for label in ["Part A Answers", "Part B Answers", "Part C Answers", "Part D Answers", "Part E Scoring Rubric"]),
        "Newcomer answer key should cover all quiz sections and the synthesis rubric.",
        "A-E coverage",
        "complete" if all(label in answer_key for label in ["Part A Answers", "Part B Answers", "Part C Answers", "Part D Answers", "Part E Scoring Rubric"]) else "incomplete",
    )
    v.expect(
        "newcomer.review_paths",
        answer_key.count("### If ") >= 5,
        "Newcomer answer key should provide targeted review paths for at least five mistake types.",
        ">=5",
        answer_key.count("### If "),
    )

    newcomer_slides_path = DOCS / "icml2026_newcomer_slides.html"
    newcomer_slides = newcomer_slides_path.read_text(encoding="utf-8") if newcomer_slides_path.exists() else ""
    slide_count = newcomer_slides.count('<section class="slide')
    embedded_figure_count = newcomer_slides.count('src="data:image/png;base64,')
    area_map_slide_count = len(re.findall(r'data-kicker="Area \d+ of 12"', newcomer_slides))
    area_paper_slide_count = newcomer_slides.count('data-kicker="Representative paper · area ')
    external_assets = bool(re.search(r'<(?:script|img)[^>]+src="(?:https?:)?//|<link[^>]+href="(?:https?:)?//', newcomer_slides, re.I))
    v.expect("newcomer.slides_exists", newcomer_slides_path.exists() and newcomer_slides_path.stat().st_size > 1_000_000, "Self-contained newcomer slide deck should exist and include embedded figures.", ">1 MB", newcomer_slides_path.stat().st_size if newcomer_slides_path.exists() else "missing")
    v.expect("newcomer.slides_count", slide_count == 47, "Newcomer slide deck should contain the complete 47-slide technical story.", 47, slide_count)
    v.expect("newcomer.slides_area_depth", area_map_slide_count == 12 and area_paper_slide_count == 12, "Newcomer slide deck should contain one technical map and one representative-paper slide for every area.", "12 area maps + 12 paper slides", f"{area_map_slide_count} area maps + {area_paper_slide_count} paper slides")
    v.expect("newcomer.slides_figures", embedded_figure_count == 4, "Newcomer slide deck should embed four figures as data URIs.", 4, embedded_figure_count)
    v.expect("newcomer.slides_self_contained", not external_assets, "Newcomer slide deck should not depend on external scripts, stylesheets, or images.", "no external assets", "external assets found" if external_assets else "no external assets")
    v.expect("newcomer.slides_controls", all(token in newcomer_slides for token in ["ArrowRight", "toggleOverview", "requestFullscreen", "window.print"]), "Newcomer slide deck should support keyboard navigation, overview, full screen, and printing.", "all controls", "complete" if all(token in newcomer_slides for token in ["ArrowRight", "toggleOverview", "requestFullscreen", "window.print"]) else "incomplete")

    inventory_paths = {row["path"] for row in inventory}
    for required in [
        "docs/project_index.md",
        "docs/dashboard.html",
        "docs/data_dictionary.md",
        "data/processed/project_artifact_inventory.csv",
        "data/processed/icml2026_claim_validation_reviewed.csv",
        "data/processed/icml2026_area_validation_reviewed.csv",
        "data/processed/icml2026_researcher_thesis_map.csv",
        "data/processed/icml2026_claim_acceptance_criteria.csv",
        "data/processed/icml2026_claim_decision_board.csv",
        "data/processed/icml2026_claim_risk_register.csv",
        "data/processed/icml2026_safe_statement_register.csv",
        "data/processed/icml2026_review_execution_dashboard.csv",
        "data/processed/icml2026_review_execution_claim_actions.csv",
        "data/processed/icml2026_researcher_action_plan.csv",
        "data/processed/icml2026_research_questions_agenda.csv",
        "data/processed/icml2026_review_decision_tasks.csv",
        "data/processed/icml2026_paper_source_access_map.csv",
        "data/processed/icml2026_pdf_extraction_probe.csv",
        "data/processed/icml2026_pdf_review_cards.csv",
        "data/processed/icml2026_pdf_page_cues.csv",
        "data/processed/icml2026_pdf_review_worksheet.csv",
        "data/processed/icml2026_pdf_review_transfer_checklist.csv",
        "data/processed/icml2026_researcher_gap_audit.csv",
        "data/processed/icml2026_sprint_prereview_suggestions.csv",
        "data/processed/icml2026_review_sprint_02.csv",
        "data/processed/icml2026_sprint_reading_briefs.csv",
        "data/processed/icml2026_sprint_02_prereview_suggestions.csv",
        "data/processed/icml2026_manual_review_codebook.csv",
        "data/processed/icml2026_manual_review_value_lint.csv",
        "data/processed/icml2026_manual_review_value_lint_summary.csv",
        "data/processed/icml2026_paper_note_overlay_bridge.csv",
        "data/processed/icml2026_sprint_02_overlay_bridge.csv",
        "data/processed/icml2026_area_risk_register.csv",
        "data/processed/icml2026_public_program_divergence_set.csv",
        "data/processed/icml2026_taxonomy_adjudication_queue.csv",
        "data/processed/icml2026_artifact_audit_queue.csv",
        "data/processed/icml2026_baseline_sensitivity_queue.csv",
        "data/manual/claim_review_overrides.csv",
        "data/manual/area_review_overrides.csv",
        "data/manual/icml2026_review_sprint_01_paper_notes.csv",
        "data/manual/icml2026_review_sprint_02_paper_notes.csv",
        "reports/icml2026_landscape_synthesis.md",
        "reports/icml2026_claim_validation_packet_index.md",
        "reports/manual_review_progress.md",
        "reports/manual_review_workspace.md",
        "reports/reviewed_validation_tables.md",
        "reports/icml2026_researcher_readiness_audit.md",
        "reports/icml2026_researcher_thesis_map.md",
        "reports/icml2026_claim_acceptance_criteria.md",
        "reports/icml2026_claim_decision_board.md",
        "reports/icml2026_claim_risk_register.md",
        "reports/icml2026_safe_statement_register.md",
        "reports/icml2026_review_execution_dashboard.md",
        "reports/icml2026_researcher_action_plan.md",
        "reports/icml2026_research_questions_agenda.md",
        "reports/icml2026_review_decision_tasks.md",
        "reports/icml2026_paper_source_access_map.md",
        "reports/icml2026_pdf_extraction_probe.md",
        "reports/icml2026_pdf_review_cards.md",
        "reports/icml2026_pdf_review_worksheet.md",
        "reports/icml2026_pdf_review_transfer_checklist.md",
        "reports/icml2026_researcher_gap_audit.md",
        "reports/icml2026_researcher_review_plan.md",
        "reports/icml2026_review_sprint_01.md",
        "reports/icml2026_review_sprint_02.md",
        "reports/icml2026_sprint_reading_brief_index.md",
        "reports/icml2026_sprint_prereview_suggestions.md",
        "reports/icml2026_sprint_02_prereview_suggestions.md",
        "reports/icml2026_paper_note_workspace.md",
        "reports/icml2026_sprint_02_paper_note_workspace.md",
        "reports/icml2026_manual_review_codebook.md",
        "reports/icml2026_manual_review_value_lint.md",
        "reports/icml2026_paper_note_overlay_bridge.md",
        "reports/icml2026_sprint_02_overlay_bridge.md",
        "reports/icml2026_public_program_divergence_set.md",
        "reports/icml2026_taxonomy_adjudication_queue.md",
        "reports/icml2026_artifact_audit_queue.md",
        "reports/icml2026_baseline_sensitivity_queue.md",
        "reports/icml2026_claim_evidence_dossier_index.md",
        "reports/icml2026_area_briefing_card_index.md",
        "reports/icml2026_area_risk_register.md",
        "docs/icml2026_newcomer_roadmap.md",
        "docs/newcomer_glossary.md",
        "docs/newcomer_learning_goal.md",
        "docs/icml2026_newcomer_slides.html",
        "reports/icml2026_newcomer_area_tour.md",
        "reports/icml2026_newcomer_trend_lessons.md",
        "reports/icml2026_newcomer_paper_course.md",
        "reports/icml2026_newcomer_final_quiz.md",
        "reports/icml2026_newcomer_quiz_answer_key.md",
        "reports/icml2026_newcomer_briefing_template.md",
        "reports/icml2026_newcomer_course_audit.md",
    ]:
        v.expect(f"inventory.{required}", required in inventory_paths, f"Inventory should include {required}.", "present", "present" if required in inventory_paths else "missing")

    dashboard = DOCS / "dashboard.html"
    dashboard_ok = dashboard.exists() and dashboard.stat().st_size > 1000
    v.expect("dashboard.exists", dashboard_ok, "Static dashboard should exist and be non-empty.", ">1000 bytes", dashboard.stat().st_size if dashboard.exists() else "missing")
    dashboard_payload_ok = False
    dashboard_payload_actual = "missing"
    if dashboard.exists():
        text = dashboard.read_text(encoding="utf-8")
        match = re.search(r'<script id="payload" type="application/json">(.*?)</script>', text, re.S)
        if match:
            try:
                payload = json.loads(match.group(1))
                dashboard_payload_actual = (
                    f"papers={len(payload.get('papers', []))}, areas={len(payload.get('areas', []))}, "
                    f"claims={len(payload.get('claims', []))}, review={len(payload.get('reviewProgress', []))}, "
                    f"figures={len(payload.get('figures', []))}, readiness_link={bool(payload.get('links', {}).get('readinessAudit'))}, "
                    f"area_lesson_links={sum(bool(row.get('lesson_url')) for row in payload.get('areas', []))}, "
                    f"newcomer_link={bool(payload.get('links', {}).get('newcomerRoadmap'))}, "
                    f"newcomer_slides_link={bool(payload.get('links', {}).get('newcomerSlides'))}, "
                    f"dossier_link={bool(payload.get('links', {}).get('claimDossiers'))}, "
                    f"area_briefings_link={bool(payload.get('links', {}).get('areaBriefings'))}, "
                    f"review_plan_link={bool(payload.get('links', {}).get('reviewPlan'))}, "
                    f"review_sprint_link={bool(payload.get('links', {}).get('reviewSprint'))}, "
                    f"manual_review_link={bool(payload.get('links', {}).get('manualReviewWorkspace'))}, "
                    f"pdf_cards={payload.get('boundedReview', {}).get('cards')}, "
                    f"pdf_worksheet={payload.get('boundedReview', {}).get('worksheetRows')}, "
                    f"pdf_transfer={payload.get('boundedReview', {}).get('transferRows')}, "
                    f"pdf_cards_link={bool(payload.get('links', {}).get('pdfReviewCards'))}, "
                    f"pdf_worksheet_link={bool(payload.get('links', {}).get('pdfReviewWorksheet'))}, "
                    f"pdf_transfer_link={bool(payload.get('links', {}).get('pdfReviewTransfer'))}"
                )
                dashboard_payload_ok = (
                    len(payload.get("areas", [])) == 12
                    and len(payload.get("claims", [])) == 8
                    and len(payload.get("papers", [])) == 6628
                    and len(payload.get("reviewProgress", [])) == 20
                    and len(payload.get("figures", [])) >= 6
                    and sum(bool(row.get("lesson_url")) for row in payload.get("areas", [])) == 12
                    and bool(payload.get("links", {}).get("newcomerRoadmap"))
                    and bool(payload.get("links", {}).get("newcomerSlides"))
                    and bool(payload.get("links", {}).get("readinessAudit"))
                    and bool(payload.get("links", {}).get("claimDossiers"))
                    and bool(payload.get("links", {}).get("areaBriefings"))
                    and bool(payload.get("links", {}).get("reviewPlan"))
                    and bool(payload.get("links", {}).get("reviewSprint"))
                    and bool(payload.get("links", {}).get("manualReviewWorkspace"))
                    and payload.get("boundedReview", {}).get("cards") == 8
                    and payload.get("boundedReview", {}).get("worksheetRows") == 8
                    and payload.get("boundedReview", {}).get("transferRows") == 23
                    and bool(payload.get("links", {}).get("pdfReviewCards"))
                    and bool(payload.get("links", {}).get("pdfReviewWorksheet"))
                    and bool(payload.get("links", {}).get("pdfReviewTransfer"))
                )
            except json.JSONDecodeError as exc:
                dashboard_payload_actual = f"JSONDecodeError: {exc}"
    v.expect("dashboard.payload", dashboard_payload_ok, "Static dashboard should embed parseable paper/area/claim/review/figure data plus course, area-lesson, broad-review, and bounded-PDF links.", "papers=6628, areas=12, claims=8, review=20, figures>=6, area_lesson_links=12, newcomer_link=true, newcomer_slides_link=true, readiness_link=true, dossier_link=true, area_briefings_link=true, review_plan_link=true, review_sprint_link=true, manual_review_link=true, pdf_cards=8, pdf_worksheet=8, pdf_transfer=23, pdf_links=true", dashboard_payload_actual)

    public_pages = ["index.html", "learn.html", "quiz.html", "about.html", "404.html"]
    missing_pages = [filename for filename in public_pages if not (DOCS / filename).exists()]
    v.expect(
        "public.pages",
        not missing_pages,
        "The public website should include its core visitor pages.",
        "all core pages",
        ", ".join(missing_pages) if missing_pages else "complete",
    )

    learn_page = (DOCS / "learn.html").read_text(encoding="utf-8") if (DOCS / "learn.html").exists() else ""
    lesson_directory = DOCS / "learn"
    lesson_pages = sorted(lesson_directory.glob("*.html")) if lesson_directory.exists() else []
    area_lesson_pages = [path for path in lesson_pages if path.name not in {"foundations.html", "synthesis.html"}]
    lesson_text = "\n".join(path.read_text(encoding="utf-8") for path in lesson_pages)
    paper_case_count = lesson_text.count('class="paper-card')
    mastery_question_count = lesson_text.count("&quot;question&quot;")
    v.expect(
        "public.learning_path",
        len(lesson_pages) == 14
        and len(area_lesson_pages) == 12
        and paper_case_count == 36
        and mastery_question_count == 56
        and all(token in learn_page for token in ["Orientation", "Core course", "Deep reading"]),
        "The guided course should include foundations, 12 technical area lessons, synthesis, paper cases, mastery checks, and three learning routes.",
        "14 modules, 12 areas, 36 paper cases, 56 mastery questions, 3 routes",
        f"{len(lesson_pages)} modules, {len(area_lesson_pages)} areas, {paper_case_count} paper cases, {mastery_question_count} mastery questions",
    )
    for lesson_path in area_lesson_pages:
        content = lesson_path.read_text(encoding="utf-8")
        required_sections = [
            "Start with intuition",
            "Technical core",
            "Worked example:",
            "Evaluation",
            "Paper lab",
            "Important limit",
            "Four-term glossary",
            "Mastery checkpoint",
        ]
        depth_ok = (
            all(section in content for section in required_sections)
            and content.count('class="paper-card') == 3
            and content.count("Abstract-based preview") == 2
            and content.count("<dt>Caution</dt>") == 2
            and content.count("<strong>Why selected:</strong>") == 2
            and "Pause and predict" in content
            and content.count("&quot;question&quot;") == 4
        )
        v.expect(
            f"public.lesson_depth.{lesson_path.stem}",
            depth_ok,
            "Every area module should contain the full teaching sequence, three deep paper cases with visible selection reasons, active prediction, and four mastery questions.",
            "all sections + 3 deep papers + 2 selection reasons + prediction + 4 questions",
            "complete" if depth_ok else "incomplete",
        )

    foundation_content = (lesson_directory / "foundations.html").read_text(encoding="utf-8") if (lesson_directory / "foundations.html").exists() else ""
    synthesis_content = (lesson_directory / "synthesis.html").read_text(encoding="utf-8") if (lesson_directory / "synthesis.html").exists() else ""
    v.expect(
        "public.foundations_depth",
        all(token in foundation_content for token in ["Mental model 1", "A metric answers one question", "A five-pass paper reading method", "Claim ladder", "Mastery checkpoint"]),
        "The foundations module should teach evidence interpretation and paper-reading practice before the area tour.",
        "mental models + evidence + reading protocol + claims + mastery",
        "complete" if foundation_content else "missing",
    )
    v.expect(
        "public.synthesis_depth",
        all(token in synthesis_content for token in ["Six evidence cards", "Six bridges", "Worked synthesis", "Capstone", "Mastery checkpoint"]),
        "The synthesis module should connect areas, evidence signals, and a capstone activity.",
        "trends + bridges + worked synthesis + capstone + mastery",
        "complete" if synthesis_content else "missing",
    )

    quiz_script = (DOCS / "assets" / "quiz.js").read_text(encoding="utf-8") if (DOCS / "assets" / "quiz.js").exists() else ""
    quiz_question_count = len(re.findall(r"^\s+category: '(?:Foundations|Area Map|Evidence|Paper Cases|Synthesis)'", quiz_script, re.M))
    v.expect(
        "public.interactive_quiz",
        quiz_question_count == 28
        and "QUESTION_MODULES" in quiz_script
        and "review-recommendations" in quiz_script
        and "retry-missed" in quiz_script
        and "keydown" in quiz_script,
        "The final assessment should contain 28 MCQs, course-linked recommendations, keyboard support, and missed-question retry.",
        "28 MCQs + module review + keyboard + retry",
        f"{quiz_question_count} MCQs; recommendations={('review-recommendations' in quiz_script)}; keyboard={('keydown' in quiz_script)}; retry={('retry-missed' in quiz_script)}",
    )

    home_page = (DOCS / "index.html").read_text(encoding="utf-8") if (DOCS / "index.html").exists() else ""
    v.expect(
        "public.coherent_journey",
        all(token in home_page for token in ["Build foundations", "Learn the areas", "Connect the map", "Demonstrate mastery", "36", "56"]),
        "The homepage should present the complete course journey and current learning-product depth.",
        "4 stages + 36 papers + 56 lesson checks",
        "complete" if home_page else "missing",
    )

    public_support_files = [DOCS / "favicon.svg", DOCS / "site.webmanifest", DOCS / "QUALITY_STANDARDS.md"]
    missing_support_files = [path.name for path in public_support_files if not path.exists()]
    v.expect(
        "public.product_support",
        not missing_support_files,
        "The public product should include install metadata, a recognizable icon, and a documented quality standard.",
        "favicon + manifest + quality standard",
        ", ".join(missing_support_files) if missing_support_files else "complete",
    )

    readme_lines = (ROOT / "README.md").read_text(encoding="utf-8").count("\n") + 1
    v.expect(
        "public.readme_length",
        readme_lines <= 100,
        "The README should remain a concise entry point.",
        "at most 100 lines",
        readme_lines,
    )

    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8") if (ROOT / "pyproject.toml").exists() else ""
    lock_exists = (ROOT / "uv.lock").exists()
    v.expect(
        "python.uv_project",
        lock_exists and 'required-version = ">=0.11.7"' in pyproject and "[dependency-groups]" in pyproject,
        "Python dependencies should be declared and locked through uv.",
        "pyproject + uv.lock + dev group",
        f"lock={lock_exists}; configured={bool(pyproject)}",
    )

    public_docs = [ROOT / "README.md", ROOT / "CONTRIBUTING.md", DOCS / "DEVELOPMENT.md", ROOT / "scripts" / "README.md"]
    legacy_python_commands = [str(path.relative_to(ROOT)) for path in public_docs if path.exists() and "python3 " in path.read_text(encoding="utf-8")]
    v.expect(
        "python.uv_commands",
        not legacy_python_commands,
        "Contributor-facing Python commands should use uv.",
        "uv commands only",
        ", ".join(legacy_python_commands) if legacy_python_commands else "complete",
    )

    pages_workflow = ROOT / ".github" / "workflows" / "pages.yml"
    pages_config = pages_workflow.read_text(encoding="utf-8") if pages_workflow.exists() else ""
    v.expect(
        "public.pages_workflow",
        all(token in pages_config for token in ["actions/deploy-pages@v4", "astral-sh/setup-uv@", "uv sync --locked", "build_public_site.py"]),
        "GitHub Pages should build the site from the locked uv environment and deploy it with the official action.",
        "uv build + Pages deploy",
        "complete" if pages_config else "missing",
    )

    failures = sum(1 for row in v.rows if row["status"] == "fail" and row["severity"] == "error")
    return v.rows, failures


def write_report(rows: list[dict[str, object]], failures: int) -> None:
    status_counts = Counter(str(row["status"]) for row in rows)
    severity_failures = Counter(str(row["severity"]) for row in rows if row["status"] == "fail")
    lines = [
        "# ICML 2026 Workspace Validation",
        "",
        "Automated structural QA for the generated EDA workspace.",
        "",
        "## Summary",
        "",
        f"- Checks: {len(rows)}",
        f"- Passed: {status_counts['pass']}",
        f"- Failed: {status_counts['fail']}",
        f"- Error failures: {failures}",
        f"- Warning failures: {severity_failures['warning']}",
        "",
    ]
    if failures:
        lines.extend(["## Error Failures", ""])
        for row in rows:
            if row["status"] == "fail" and row["severity"] == "error":
                lines.append(f"- `{row['check_id']}`: {row['message']} Expected `{row['expected']}`, got `{row['actual']}`.")
        lines.append("")
    warnings = [row for row in rows if row["status"] == "fail" and row["severity"] == "warning"]
    if warnings:
        lines.extend(["## Warning Failures", ""])
        for row in warnings:
            lines.append(f"- `{row['check_id']}`: {row['message']} Expected `{row['expected']}`, got `{row['actual']}`.")
        lines.append("")
    lines.extend(
        [
            "## All Checks",
            "",
            "| Check | Status | Severity | Expected | Actual |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in rows:
        lines.append(f"| `{row['check_id']}` | {row['status']} | {row['severity']} | {row['expected']} | {row['actual']} |")
    (REPORTS / "workspace_validation.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    rows, failures = validate()
    write_csv(
        PROCESSED / "workspace_validation_checks.csv",
        rows,
        ["check_id", "status", "severity", "expected", "actual", "message"],
    )
    write_report(rows, failures)
    print(f"Wrote {PROCESSED / 'workspace_validation_checks.csv'} ({len(rows)} checks)")
    print(f"Wrote {REPORTS / 'workspace_validation.md'}")
    if failures:
        print(f"Validation failed with {failures} error failure(s).", file=sys.stderr)
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
