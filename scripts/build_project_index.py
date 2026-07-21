#!/usr/bin/env python3
"""Generate project navigation, artifact inventory, and data dictionary docs."""

from __future__ import annotations

import csv
import json
import struct
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
MANUAL = ROOT / "data" / "manual"
REPORTS = ROOT / "reports"
FIGURES = ROOT / "figures"
SCRIPTS = ROOT / "scripts"
DOCS = ROOT / "docs"


READING_ORDER = [
    (
        "Newcomer Learning Path",
        [
            ("Friendly ICML 2026 roadmap", "docs/icml2026_newcomer_roadmap.md", "Step-by-step quick, standard, and deep routes for understanding the conference landscape."),
            ("Self-contained HTML slides", "docs/icml2026_newcomer_slides.html", "Offline browser presentation with embedded figures, keyboard navigation, and knowledge checks."),
            ("Plain-language glossary", "docs/newcomer_glossary.md", "Short explanations of the technical and evidence terms used in the learning path."),
            ("Newcomer area tour", "reports/icml2026_newcomer_area_tour.md", "Friendly guide to the 12 broad research areas, their questions, connections, and common misunderstandings."),
            ("Six trend lessons", "reports/icml2026_newcomer_trend_lessons.md", "Evidence, examples, caveats, and checkpoints for the main ICML 2026 patterns."),
            ("12-paper newcomer course", "reports/icml2026_newcomer_paper_course.md", "Small representative paper course connecting the area map to real research."),
            ("Final newcomer quiz", "reports/icml2026_newcomer_final_quiz.md", "Open-book 100-point assessment of concepts, evidence interpretation, paper reading, and synthesis."),
            ("Quiz answer and review guide", "reports/icml2026_newcomer_quiz_answer_key.md", "Model answers, scoring rubric, serious-error rules, and targeted review paths."),
            ("Five-minute briefing template", "reports/icml2026_newcomer_briefing_template.md", "A guided final activity for explaining ICML 2026 clearly and cautiously."),
            ("Course quality audit", "reports/icml2026_newcomer_course_audit.md", "Coverage, clarity, link, assessment, and evidence-safety checks for the learning path."),
        ],
    ),
    (
        "Start Here",
        [
            ("Static dashboard", "docs/dashboard.html", "Self-contained explorer for areas, papers, claims, figures, and validation examples."),
            ("Overview report seed", "reports/icml2026_overview_report_seed.md", "Long-form narrative scaffold with claims, figures, caveats, and validation hooks."),
            ("Safe statement register", "reports/icml2026_safe_statement_register.md", "Allowed wording, unsafe wording, and caveats for claims and area summaries."),
            ("Landscape synthesis", "reports/icml2026_landscape_synthesis.md", "Fast cross-source claims and caveats."),
            ("Story outline seed", "reports/icml2026_story_outline_seed.md", "Compact narrative arc for a future briefing or presentation."),
            ("Researcher audit", "reports/icml2026_researcher_audit.md", "What is solid, weak, and next."),
            ("Researcher readiness audit", "reports/icml2026_researcher_readiness_audit.md", "Claim and area trust map for what can be used now versus what needs review."),
            ("Researcher thesis map", "reports/icml2026_researcher_thesis_map.md", "Conservative claim hierarchy with permitted wording and blocking checks."),
            ("Claim acceptance criteria", "reports/icml2026_claim_acceptance_criteria.md", "Explicit promotion gates for each synthesis claim."),
            ("Claim decision board", "reports/icml2026_claim_decision_board.md", "Claim-level operating board for what can be used now and what review action unlocks it."),
            ("Claim risk register", "reports/icml2026_claim_risk_register.md", "Falsification tests and weakest assumptions for each headline synthesis claim."),
            ("Review execution dashboard", "reports/icml2026_review_execution_dashboard.md", "Operational view of review progress, quality gates, and next claim actions."),
            ("Researcher action plan", "reports/icml2026_researcher_action_plan.md", "Time-budgeted plan for using the workspace from 30 minutes to a full review sprint."),
            ("Research questions agenda", "reports/icml2026_research_questions_agenda.md", "Prioritized ML-research questions with evidence, falsification tests, and first papers."),
            ("Review decision tasks", "reports/icml2026_review_decision_tasks.md", "Paper-by-claim decision matrix for turning sprint reading into support, weakening, taxonomy, and artifact judgments."),
            ("Paper source access map", "reports/icml2026_paper_source_access_map.md", "OpenReview, arXiv/PDF, artifact, local-context, and extraction checklist map for sprint papers."),
            ("PDF extraction probe", "reports/icml2026_pdf_extraction_probe.md", "Bounded source-readiness probe for downloading and extracting prioritized sprint PDFs."),
            ("PDF review cards", "reports/icml2026_pdf_review_cards.md", "Page-level PDF navigation cards for the bounded priority review subset."),
            ("PDF review worksheet", "reports/icml2026_pdf_review_worksheet.md", "Reviewer-ready worksheet joining PDF pages, claim tests, source links, and blank paper-note fields."),
            ("PDF review transfer checklist", "reports/icml2026_pdf_review_transfer_checklist.md", "Focused transfer checklist from bounded PDF worksheet rows to claim and area overlays."),
            ("Researcher gap audit", "reports/icml2026_researcher_gap_audit.md", "Critical feedback on what remains before the workspace becomes a high-confidence ML landscape brief."),
            ("Manual review progress", "reports/manual_review_progress.md", "Review completion status across claim and area validation queues."),
            ("Researcher review plan", "reports/icml2026_researcher_review_plan.md", "De-duplicated ranked paper-reading workflow across claim and area queues."),
            ("Review sprint 01", "reports/icml2026_review_sprint_01.md", "First manual-review worksheet for the top-ranked papers."),
            ("Review sprint 02", "reports/icml2026_review_sprint_02.md", "Second manual-review worksheet for claims missing first-sprint coverage."),
            ("Sprint reading briefs", "reports/icml2026_sprint_reading_brief_index.md", "Consolidated per-paper reading desk for sprint 01 and sprint 02 review."),
            ("Sprint pre-review suggestions", "reports/icml2026_sprint_prereview_suggestions.md", "Machine-generated prompts for first-sprint paper reading."),
            ("Sprint 02 pre-review suggestions", "reports/icml2026_sprint_02_prereview_suggestions.md", "Machine-generated prompts for the uncovered-claim sprint."),
            ("Paper note workspace", "reports/icml2026_paper_note_workspace.md", "Human-editable top-40 paper-note sheet for novelty, method, evidence, limitations, and report use."),
            ("Sprint 02 paper note workspace", "reports/icml2026_sprint_02_paper_note_workspace.md", "Human-editable paper-note sheet for the uncovered-claim sprint."),
            ("Manual review codebook", "reports/icml2026_manual_review_codebook.md", "Canonical coded values and transfer rules for paper notes and overlays."),
            ("Manual review value lint", "reports/icml2026_manual_review_value_lint.md", "Checks manual coded values against the canonical codebook."),
            ("Paper note overlay bridge", "reports/icml2026_paper_note_overlay_bridge.md", "Transfer checklist from first-sprint paper notes into claim and area review overlays."),
            ("Sprint 02 overlay bridge", "reports/icml2026_sprint_02_overlay_bridge.md", "Transfer checklist from sprint 02 paper notes into claim and area review overlays."),
            ("Manual review workspace", "reports/manual_review_workspace.md", "Human-editable overlay files for claim and area judgments."),
            ("Reviewed validation tables", "reports/reviewed_validation_tables.md", "Generated merge of validation queues with human review overlays."),
            ("Claim evidence dossiers", "reports/icml2026_claim_evidence_dossier_index.md", "Abstract/title-based pre-review aids for the synthesis claim packets."),
            ("Claim validation packet index", "reports/icml2026_claim_validation_packet_index.md", "Paper-level checks behind the synthesis claims."),
        ],
    ),
    (
        "Core Landscape",
        [
            ("Manual taxonomy seed", "reports/icml2026_manual_taxonomy_seed.md", "Curated 12-area map over semantic clusters."),
            ("Taxonomy adjudication queue", "reports/icml2026_taxonomy_adjudication_queue.md", "Cluster-level queue for resolving unstable taxonomy boundaries."),
            ("Area fault lines", "reports/icml2026_area_fault_lines.md", "Researcher-facing synthesis by area."),
            ("Area briefing cards", "reports/icml2026_area_briefing_card_index.md", "Compact per-area cards for reading starts, signal interpretation, and caveats."),
            ("Area risk register", "reports/icml2026_area_risk_register.md", "Area-level reliability, falsification, and safe-language register."),
            ("Program calibration", "reports/icml2026_program_signal_calibration.md", "Oral/award/public attention divergence."),
            ("Public/program divergence set", "reports/icml2026_public_program_divergence_set.md", "Paper-level reading set for calibrating AlphaXiv attention against oral/award signal."),
            ("Historical accepted-paper baseline", "reports/historical_accepted_paper_baseline.md", "ICML 2026 versus ICML 2025, NeurIPS 2025, ICLR 2026."),
            ("Baseline sensitivity queue", "reports/icml2026_baseline_sensitivity_queue.md", "Area-level QA queue for historical-baseline and arXiv-trend claims."),
        ],
    ),
    (
        "How To Read Papers",
        [
            ("Audience reading paths", "reports/icml2026_audience_reading_paths.md", "Role-specific paper tracks."),
            ("Manual validation queue", "reports/icml2026_manual_validation_queue.md", "Balanced area-level review queue."),
            ("Validation packet index", "reports/icml2026_validation_packet_index.md", "Area-specific review worksheets."),
        ],
    ),
    (
        "Evidence And Reproducibility",
        [
            ("Evidence codes", "reports/icml2026_paper_evidence_codes.md", "Heuristic contribution/method/evaluation tags."),
            ("Reproducibility lens", "reports/icml2026_reproducibility_lens.md", "AlphaXiv GitHub artifact view."),
            ("Artifact audit queue", "reports/icml2026_artifact_audit_queue.md", "Paper-level queue for checking artifact and repository claims."),
            ("GitHub live artifact check", "reports/icml2026_github_artifact_live_check.md", "Bounded live GitHub API check for high-signal repos."),
        ],
    ),
    (
        "Exploration Layers",
        [
            ("Semantic cluster landscape", "reports/icml2026_semantic_cluster_landscape.md", "Transformer embedding clusters."),
            ("Cluster landscape", "reports/icml2026_cluster_landscape.md", "Lexical TF-IDF/SVD clusters."),
            ("Collaboration landscape", "reports/icml2026_collaboration_landscape.md", "Authors, institutions, sectors, collaboration hubs."),
            ("Visual EDA index", "reports/icml2026_visual_eda_index.md", "Generated figures and caveats."),
            ("Workspace validation", "reports/workspace_validation.md", "Automated structural QA over generated artifacts."),
        ],
    ),
]

FILE_DESCRIPTIONS = {
    "icml2026_papers.csv": "Authoritative ICML 2026 paper/poster table parsed from official virtual-site JSON.",
    "alphaxiv_icml2026_joined.csv": "Official ICML rows joined with AlphaXiv public-attention and GitHub metadata.",
    "icml2026_manual_taxonomy_areas.csv": "Curated 12-area taxonomy summary.",
    "icml2026_manual_taxonomy_clusters.csv": "Semantic cluster to curated taxonomy mapping with review flags.",
    "icml2026_manual_taxonomy_papers.csv": "Paper-level curated taxonomy assignments.",
    "icml2026_taxonomy_adjudication_queue.csv": "Cluster-level queue for adjudicating unstable semantic cluster area/subarea mappings.",
    "icml2026_landscape_signal_matrix.csv": "Area-level cross-source synthesis matrix.",
    "icml2026_landscape_claim_register.csv": "Major synthesis claims, evidence, caveats, and next validation.",
    "icml2026_claim_validation_queue.csv": "Paper-level review queue for synthesis claims.",
    "icml2026_claim_validation_reviewed.csv": "Claim validation queue merged with manual review overlays.",
    "icml2026_area_validation_reviewed.csv": "Area validation queue merged with manual review overlays.",
    "icml2026_researcher_readiness_audit.csv": "Claim and area readiness tiers for researcher use.",
    "icml2026_researcher_thesis_map.csv": "Conservative thesis hierarchy with claim roles, permitted wording, blocking checks, and first papers to read.",
    "icml2026_claim_acceptance_criteria.csv": "Explicit promotion gates for synthesis claims using reviewed rows, paper notes, taxonomy checks, and artifact checks.",
    "icml2026_claim_decision_board.csv": "Claim-level operating board combining acceptance gates, sprint coverage, and overlay transfer actions.",
    "icml2026_claim_risk_register.csv": "Falsification-oriented risk register for headline synthesis claims.",
    "icml2026_safe_statement_register.csv": "Allowed wording, unsafe wording, and caveats for claims and area summaries.",
    "icml2026_review_execution_dashboard.csv": "Operational metrics for review progress, quality gates, and claim promotion readiness.",
    "icml2026_review_execution_claim_actions.csv": "Claim-level next actions for executing manual review sprints.",
    "icml2026_researcher_action_plan.csv": "Time-budgeted plan for using the workspace from 30 minutes to a full review sprint.",
    "icml2026_research_questions_agenda.csv": "Prioritized ML-research questions with evidence, falsification tests, and first papers.",
    "icml2026_review_decision_tasks.csv": "Paper-by-claim decision matrix for turning sprint reading into support, weakening, taxonomy, and artifact judgments.",
    "icml2026_paper_source_access_map.csv": "OpenReview, arXiv/PDF, artifact, local-context, and extraction checklist map for sprint papers.",
    "icml2026_pdf_extraction_probe.csv": "Bounded source-readiness probe for downloading and extracting prioritized sprint PDFs.",
    "icml2026_pdf_review_cards.csv": "Page-level PDF navigation cards for the bounded priority review subset.",
    "icml2026_pdf_page_cues.csv": "Page-level section and evidence-cue counts for probed priority PDFs.",
    "icml2026_pdf_review_worksheet.csv": "Reviewer-ready worksheet joining PDF pages, claim tests, source links, and blank paper-note fields.",
    "icml2026_pdf_review_transfer_checklist.csv": "Focused transfer checklist from bounded PDF worksheet rows to claim and area overlays.",
    "icml2026_researcher_gap_audit.csv": "Ranked critical gaps and next actions for turning the workspace into a stronger ML landscape brief.",
    "icml2026_claim_evidence_dossiers.csv": "Paper-level claim pre-review buckets, rationales, and abstract excerpts.",
    "icml2026_researcher_review_plan.csv": "De-duplicated ranked manual review plan across claim and area queues.",
    "icml2026_review_sprint_01.csv": "First-sprint manual review worksheet with overlay keys and field prompts.",
    "icml2026_review_sprint_02.csv": "Second manual review worksheet for C04/C05 claims missing first-sprint coverage.",
    "icml2026_sprint_reading_briefs.csv": "Consolidated per-paper reading briefs for sprint 01 and sprint 02 manual review.",
    "icml2026_sprint_prereview_suggestions.csv": "Machine-generated first-sprint paper-reading prompts from abstracts, evidence tags, and linked claims.",
    "icml2026_sprint_02_prereview_suggestions.csv": "Machine-generated paper-reading prompts for the uncovered-claim sprint.",
    "icml2026_review_sprint_01_paper_notes.csv": "Human-editable first-sprint paper notes for novelty, method, evidence, limitations, and report use.",
    "icml2026_review_sprint_02_paper_notes.csv": "Human-editable sprint 02 paper notes for claims missing first-sprint coverage.",
    "icml2026_manual_review_codebook.csv": "Canonical coded values and transfer rules for paper notes and manual overlays.",
    "icml2026_manual_review_value_lint.csv": "Invalid manual coded values found by the codebook linter.",
    "icml2026_manual_review_value_lint_summary.csv": "Per-file summary from the manual coded-value linter.",
    "icml2026_paper_note_overlay_bridge.csv": "Transfer checklist from first-sprint paper notes into claim and area review overlay rows.",
    "icml2026_sprint_02_overlay_bridge.csv": "Transfer checklist from sprint 02 paper notes into claim and area review overlay rows.",
    "icml2026_area_briefing_cards.csv": "Compact per-area briefing cards with signals, trust tiers, and reading starts.",
    "icml2026_area_risk_register.csv": "Area-level reliability, falsification, and safe-language register.",
    "icml2026_paper_explorer.csv": "Compact paper-level search table for area, program, artifact, and evidence exploration.",
    "icml2026_manual_validation_queue.csv": "Paper-level review queue for area evidence and taxonomy boundaries.",
    "icml2026_paper_evidence_codes.csv": "Heuristic paper-level contribution/method/evaluation/artifact evidence tags.",
    "icml2026_area_evidence_summary.csv": "Area-level aggregation of heuristic evidence tags.",
    "icml2026_area_program_calibration.csv": "Area-level oral/award/public-attention calibration.",
    "icml2026_public_program_divergence_set.csv": "Paper-level reading set for public-attention versus oral/award program-signal divergence.",
    "historical_venue_delta_summary.csv": "ICML 2026 area-share deltas versus neighboring accepted-paper baselines.",
    "historical_accepted_papers_classified.csv": "Accepted papers from ICML 2026/ICML 2025/NeurIPS 2025/ICLR 2026 classified with a shared keyword scorer.",
    "arxiv_taxonomy_trend_summary.csv": "Broad arXiv query-count trend summary by taxonomy area.",
    "icml2026_baseline_sensitivity_queue.csv": "Area-level spot-check queue for using historical venue baselines and arXiv query trends responsibly.",
    "icml2026_reproducibility_papers.csv": "Paper-level artifact metadata derived from AlphaXiv GitHub fields.",
    "icml2026_reproducibility_summary.csv": "Artifact availability summaries by corpus, topic, cluster, theme, and audience path.",
    "icml2026_artifact_audit_queue.csv": "Paper-level artifact audit queue for reproducibility and repository-link checks.",
    "icml2026_audience_reading_paths.csv": "Role-specific paper reading tracks.",
    "workspace_validation_checks.csv": "Machine-readable workspace validation results.",
    "project_artifact_inventory.csv": "Machine-readable inventory of generated data, reports, figures, scripts, and docs.",
    "manual_review_progress.csv": "Manual review completion summary by claim and by area.",
    "claim_review_overrides.csv": "Human-editable claim-review overlay file.",
    "area_review_overrides.csv": "Human-editable area-review overlay file.",
    "dashboard.html": "Self-contained static dashboard for scanning area signals, paper search, claims, figures, and validation examples.",
    "icml2026_newcomer_roadmap.md": "Step-by-step quick, standard, and deep learning routes for ICML 2026 newcomers.",
    "icml2026_newcomer_slides.html": "Self-contained offline slide deck for the ICML 2026 newcomer course.",
    "newcomer_glossary.md": "Plain-language definitions for the newcomer learning path.",
    "newcomer_learning_goal.md": "Goal, learning outcomes, assessment design, and success criteria for the newcomer course.",
    "icml2026_newcomer_area_tour.md": "Friendly guide to the 12 broad ICML 2026 research areas.",
    "icml2026_newcomer_trend_lessons.md": "Six evidence-based lessons on the main conference patterns.",
    "icml2026_newcomer_paper_course.md": "Twelve-paper course linking conference trends to representative research examples.",
    "icml2026_newcomer_final_quiz.md": "Open-book assessment of broad ICML 2026 landscape understanding.",
    "icml2026_newcomer_quiz_answer_key.md": "Quiz model answers, scoring rubric, and targeted review routes.",
    "icml2026_newcomer_briefing_template.md": "Guided template for a balanced five-minute conference briefing.",
    "icml2026_newcomer_course_audit.md": "Coverage, clarity, navigation, and evidence-safety audit for the newcomer course.",
    "icml2026_pdf_review_seed_paper_notes.csv": "Suggestion-only paper judgments derived from the bounded eight-PDF review subset.",
    "icml2026_pdf_review_seed_claim_overrides.csv": "Suggestion-only claim judgments derived from the bounded eight-PDF review subset.",
    "icml2026_pdf_review_seed_area_overrides.csv": "Suggestion-only area judgments derived from the bounded eight-PDF review subset.",
}


def markdown_link(path: str) -> str:
    return f"[`{path}`](../{path})"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def csv_info(path: Path) -> dict[str, object]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = sum(1 for _ in reader)
        columns = reader.fieldnames or []
    return {"rows": rows, "columns": columns}


def json_info(path: Path) -> dict[str, object]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"json_type": "invalid", "top_level_count": ""}
    if isinstance(payload, list):
        return {"json_type": "list", "top_level_count": len(payload)}
    if isinstance(payload, dict):
        return {"json_type": "dict", "top_level_count": len(payload)}
    return {"json_type": type(payload).__name__, "top_level_count": ""}


def png_dimensions(path: Path) -> tuple[int | str, int | str]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) >= 24 and header[:8] == b"\x89PNG\r\n\x1a\n":
        width, height = struct.unpack(">II", header[16:24])
        return width, height
    return "", ""


def artifact_inventory() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for base, kind in [(PROCESSED, "processed_data"), (MANUAL, "manual_data"), (REPORTS, "report"), (FIGURES, "figure"), (SCRIPTS, "script"), (DOCS, "doc")]:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if not path.is_file():
                continue
            item: dict[str, object] = {
                "path": rel(path),
                "kind": kind,
                "extension": path.suffix.lower().lstrip("."),
                "size_bytes": path.stat().st_size,
                "row_count": "",
                "column_count": "",
                "columns": "",
                "json_type": "",
                "top_level_count": "",
                "image_width": "",
                "image_height": "",
                "description": FILE_DESCRIPTIONS.get(path.name, ""),
            }
            if path.suffix.lower() == ".csv":
                info = csv_info(path)
                item["row_count"] = info["rows"]
                item["column_count"] = len(info["columns"])
                item["columns"] = "; ".join(str(col) for col in info["columns"])
            elif path.suffix.lower() == ".json":
                item.update(json_info(path))
            elif path.suffix.lower() == ".png":
                width, height = png_dimensions(path)
                item["image_width"] = width
                item["image_height"] = height
            rows.append(item)
    return rows


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_project_index(inventory: list[dict[str, object]]) -> None:
    report_count = sum(row["kind"] == "report" for row in inventory)
    data_count = sum(row["kind"] == "processed_data" for row in inventory)
    figure_count = sum(row["kind"] == "figure" for row in inventory)
    script_count = sum(row["kind"] == "script" for row in inventory)
    lines = [
        "# ICML 2026 Project Index",
        "",
        "Generated navigation for the ICML 2026 EDA workspace.",
        "",
        "## Snapshot",
        "",
        f"- Processed data files: {data_count}",
        f"- Reports: {report_count}",
        f"- Figures: {figure_count}",
        f"- Scripts: {script_count}",
        "",
        "## Recommended Reading Order",
        "",
    ]
    for section, items in READING_ORDER:
        lines.append(f"### {section}")
        lines.append("")
        for title, path, description in items:
            lines.append(f"- [{title}](../{path}) - {description}")
        lines.append("")

    lines.extend(
        [
            "## Key Data Products",
            "",
            "| File | Rows | Description |",
            "| --- | ---: | --- |",
        ]
    )
    key_names = [
        "icml2026_papers.csv",
        "alphaxiv_icml2026_joined.csv",
        "icml2026_manual_taxonomy_papers.csv",
        "icml2026_taxonomy_adjudication_queue.csv",
        "icml2026_landscape_signal_matrix.csv",
        "icml2026_landscape_claim_register.csv",
        "icml2026_claim_validation_queue.csv",
        "icml2026_claim_validation_reviewed.csv",
        "icml2026_area_validation_reviewed.csv",
        "icml2026_researcher_readiness_audit.csv",
        "icml2026_researcher_thesis_map.csv",
        "icml2026_claim_acceptance_criteria.csv",
        "icml2026_claim_decision_board.csv",
        "icml2026_claim_risk_register.csv",
        "icml2026_safe_statement_register.csv",
        "icml2026_review_execution_dashboard.csv",
        "icml2026_review_execution_claim_actions.csv",
        "icml2026_researcher_action_plan.csv",
        "icml2026_research_questions_agenda.csv",
        "icml2026_review_decision_tasks.csv",
        "icml2026_paper_source_access_map.csv",
        "icml2026_pdf_extraction_probe.csv",
        "icml2026_pdf_review_cards.csv",
        "icml2026_pdf_page_cues.csv",
        "icml2026_pdf_review_worksheet.csv",
        "icml2026_pdf_review_transfer_checklist.csv",
        "icml2026_researcher_gap_audit.csv",
        "icml2026_claim_evidence_dossiers.csv",
        "icml2026_researcher_review_plan.csv",
        "icml2026_review_sprint_01.csv",
        "icml2026_review_sprint_02.csv",
        "icml2026_sprint_reading_briefs.csv",
        "icml2026_sprint_prereview_suggestions.csv",
        "icml2026_sprint_02_prereview_suggestions.csv",
        "icml2026_review_sprint_01_paper_notes.csv",
        "icml2026_review_sprint_02_paper_notes.csv",
        "icml2026_manual_review_codebook.csv",
        "icml2026_manual_review_value_lint.csv",
        "icml2026_manual_review_value_lint_summary.csv",
        "icml2026_paper_note_overlay_bridge.csv",
        "icml2026_sprint_02_overlay_bridge.csv",
        "icml2026_area_briefing_cards.csv",
        "icml2026_area_risk_register.csv",
        "manual_review_progress.csv",
        "claim_review_overrides.csv",
        "area_review_overrides.csv",
        "icml2026_paper_explorer.csv",
        "icml2026_paper_evidence_codes.csv",
        "icml2026_public_program_divergence_set.csv",
        "icml2026_artifact_audit_queue.csv",
        "historical_accepted_papers_classified.csv",
        "historical_venue_delta_summary.csv",
        "arxiv_taxonomy_trend_summary.csv",
    ]
    by_name = {Path(str(row["path"])).name: row for row in inventory}
    for name in key_names:
        row = by_name.get(name)
        if not row:
            continue
        lines.append(f"| {markdown_link(str(row['path']))} | {row['row_count']} | {row['description']} |")

    lines.extend(
        [
            "",
            "## Most Useful Figures",
            "",
            "- [Historical venue area deltas](../figures/historical_venue_area_deltas.png) - ICML 2026 area-share deltas against nearby accepted-paper baselines.",
            "- [Program signal calibration](../figures/program_signal_calibration.png) - Oral-selection and public-attention enrichment by area.",
            "- [Semantic cluster map](../figures/semantic_cluster_map.png) - Transformer embedding map of the ICML 2026 corpus.",
            "- [Manual taxonomy area sizes](../figures/manual_taxonomy_area_sizes.png) - Curated area sizes and artifact visibility.",
            "- [arXiv taxonomy trends](../figures/arxiv_taxonomy_trends.png) - Broad external trend context by area.",
            "",
            "## Trust Levels",
            "",
            "- **Most authoritative**: official ICML virtual-site paper rows, oral flags, award seed rows, and generated counts derived directly from them.",
            "- **Good for landscape triage**: curated taxonomy, program calibration, historical accepted-paper deltas, audience paths, and synthesis claims.",
            "- **Needs manual review before publication claims**: heuristic evidence codes, taxonomy boundary clusters, arXiv query trends, AlphaXiv attention, and GitHub artifact/reproducibility signals.",
            "",
            "## Generated Companion Files",
            "",
            "- [`data/processed/project_artifact_inventory.csv`](../data/processed/project_artifact_inventory.csv) - machine-readable artifact inventory.",
            "- [`docs/data_dictionary.md`](data_dictionary.md) - CSV schemas, row counts, and known descriptions.",
        ]
    )
    (DOCS / "project_index.md").write_text("\n".join(lines), encoding="utf-8")


def write_data_dictionary(inventory: list[dict[str, object]]) -> None:
    csv_rows = [row for row in inventory if row["kind"] == "processed_data" and row["extension"] == "csv"]
    lines = [
        "# ICML 2026 Data Dictionary",
        "",
        "Generated schema and row-count reference for processed CSV files.",
        "",
        "## Summary",
        "",
        f"- Processed CSV files: {len(csv_rows)}",
        f"- Total CSV rows across processed files: {sum(int(row['row_count'] or 0) for row in csv_rows):,}",
        "",
    ]
    for row in sorted(csv_rows, key=lambda item: str(item["path"])):
        columns = [col for col in str(row["columns"]).split("; ") if col]
        lines.append(f"## `{row['path']}`")
        lines.append("")
        lines.append(f"- Rows: {row['row_count']}")
        lines.append(f"- Columns: {row['column_count']}")
        if row["description"]:
            lines.append(f"- Description: {row['description']}")
        lines.append("")
        lines.append("Columns:")
        for col in columns:
            lines.append(f"- `{col}`")
        lines.append("")
    (DOCS / "data_dictionary.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    inventory = artifact_inventory()
    # First pass creates generated docs/inventory if they do not exist yet.
    write_csv(
        PROCESSED / "project_artifact_inventory.csv",
        inventory,
        [
            "path", "kind", "extension", "size_bytes", "row_count", "column_count", "columns",
            "json_type", "top_level_count", "image_width", "image_height", "description",
        ],
    )
    write_project_index(inventory)
    write_data_dictionary(inventory)

    # Second pass makes the inventory self-consistent by including generated outputs.
    inventory = artifact_inventory()
    write_csv(
        PROCESSED / "project_artifact_inventory.csv",
        inventory,
        [
            "path", "kind", "extension", "size_bytes", "row_count", "column_count", "columns",
            "json_type", "top_level_count", "image_width", "image_height", "description",
        ],
    )
    write_project_index(inventory)
    write_data_dictionary(inventory)
    print(f"Wrote {PROCESSED / 'project_artifact_inventory.csv'} ({len(inventory)} rows)")
    print(f"Wrote {DOCS / 'project_index.md'}")
    print(f"Wrote {DOCS / 'data_dictionary.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
