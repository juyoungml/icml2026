# ICML 2026 Workspace Validation

Automated structural QA for the generated EDA workspace.

## Summary

- Checks: 324
- Passed: 324
- Failed: 0
- Error failures: 0
- Warning failures: 0

## All Checks

| Check | Status | Severity | Expected | Actual |
| --- | --- | --- | --- | --- |
| `corpus.paper_count` | pass | error | 6628 | 6628 |
| `corpus.alphaxiv_join_count` | pass | error | 6628 | 6628 |
| `corpus.taxonomy_paper_count` | pass | error | 6628 | 6628 |
| `corpus.evidence_count` | pass | error | 6628 | 6628 |
| `corpus.paper_explorer_count` | pass | error | 6628 | 6628 |
| `corpus.taxonomy_event_ids` | pass | error | 6628 | 6628 |
| `corpus.evidence_event_ids` | pass | error | 6628 | 6628 |
| `corpus.paper_explorer_event_ids` | pass | error | 6628 | 6628 |
| `taxonomy.area_count` | pass | error | 12 | 12 |
| `area_briefings.row_count` | pass | error | 12 | 12 |
| `area_briefings.coverage` | pass | error | 12 | 12 |
| `area_risk_register.row_count` | pass | error | 12 | 12 |
| `area_risk_register.coverage` | pass | error | 12 | 12 |
| `area_risk_register.risk_mix` | pass | error | critical/high risk tiers | ['critical', 'high'] |
| `area_risk_register.falsification_tests` | pass | error | all present | all present |
| `public_program_divergence.row_count` | pass | error | >=100 | 111 |
| `public_program_divergence.category_mix` | pass | error | public/program categories | ['program_ahead_of_public', 'public_ahead_of_program', 'public_and_program_aligned'] |
| `artifact_audit.row_count` | pass | error | >=100 | 160 |
| `artifact_audit.category_mix` | pass | error | artifact audit categories | ['high_signal_no_github', 'linked_needs_repro_check', 'linked_unchecked_live_status', 'metadata_suspicious_link', 'repo_flagged_live_check'] |
| `baseline_sensitivity.row_count` | pass | error | 12 | 12 |
| `baseline_sensitivity.area_coverage` | pass | error | 12 | 12 |
| `baseline_sensitivity.risk_mix` | pass | error | high/moderate risk rows | ['context', 'high', 'moderate'] |
| `taxonomy.semantic_cluster_count` | pass | error | 42 | 42 |
| `taxonomy_adjudication.row_count` | pass | error | 21 | 21 |
| `taxonomy_adjudication.cluster_coverage` | pass | error | 21 | 21 |
| `taxonomy.area_coverage` | pass | error | 12 | 12 |
| `taxonomy.area_sum` | pass | error | 6628 | 6628 |
| `claims.register_count` | pass | error | 8 | 8 |
| `claims.queue_count` | pass | error | 118 | 118 |
| `reviewed_tables.claim_row_count` | pass | error | 118 | 118 |
| `reviewed_tables.area_row_count` | pass | error | 192 | 192 |
| `reviewed_tables.claim_key_coverage` | pass | error | 118 | 118 |
| `reviewed_tables.area_key_coverage` | pass | error | 192 | 192 |
| `claim_dossiers.row_count` | pass | error | 118 | 118 |
| `claim_dossiers.claim_coverage` | pass | error | 8 | 8 |
| `review_plan.row_count` | pass | error | 224 | 224 |
| `review_plan.event_coverage` | pass | error | 224 | 224 |
| `review_sprint.row_count` | pass | error | 40 | 40 |
| `review_sprint.top40_alignment` | pass | error | top 40 review plan IDs | aligned |
| `review_sprint_02.row_count` | pass | error | 16 | 16 |
| `review_sprint_02.target_claims` | pass | error | C04>=8, C05>=8 | {'C05': 8, 'C04': 8} |
| `sprint_reading_briefs.row_count` | pass | error | 56 | 56 |
| `sprint_reading_briefs.sprint_alignment` | pass | error | sprint 01 + sprint 02 event IDs | aligned |
| `sprint_reading_briefs.file_paths` | pass | error | all present | all present |
| `paper_notes.row_count` | pass | error | 40 | 40 |
| `paper_notes.sprint_alignment` | pass | error | sprint event IDs | aligned |
| `prereview_suggestions.row_count` | pass | error | 40 | 40 |
| `prereview_suggestions.sprint_alignment` | pass | error | sprint event IDs | aligned |
| `paper_notes_02.row_count` | pass | error | 16 | 16 |
| `paper_notes_02.sprint_alignment` | pass | error | sprint 02 event IDs | aligned |
| `prereview_suggestions_02.row_count` | pass | error | 16 | 16 |
| `prereview_suggestions_02.sprint_alignment` | pass | error | sprint 02 event IDs | aligned |
| `manual_codebook.row_count` | pass | error | >=75 | 81 |
| `manual_codebook.critical_fields` | pass | error | critical field set | [('area_overlay', 'manual_artifact_status'), ('area_overlay', 'manual_fault_line_relevance'), ('area_overlay', 'manual_primary_contribution_type'), ('area_overlay', 'manual_result_character'), ('area_overlay', 'manual_validated'), ('claim_overlay', 'manual_artifact_judgment'), ('claim_overlay', 'manual_claim_support'), ('claim_overlay', 'manual_taxonomy_judgment'), ('paper_notes', 'artifact_status_checked'), ('paper_notes', 'evidence_strength'), ('paper_notes', 'final_report_use'), ('paper_notes', 'novelty_judgment'), ('paper_notes', 'paper_read_status'), ('paper_notes', 'taxonomy_correction')] |
| `manual_codebook.claim_support_values` | pass | error | canonical support values | ['contradicts', 'not_applicable', 'partial_support', 'supports', 'unclear', 'weakens'] |
| `manual_codebook.artifact_values` | pass | error | canonical artifact values | ['broken', 'linked_unchecked', 'live_checked', 'none', 'not_applicable', 'runnable'] |
| `manual_value_lint.no_invalid_values` | pass | error | 0 | 0 |
| `manual_value_lint.summary_count` | pass | error | 4 | 4 |
| `paper_note_bridge.row_count` | pass | error | 94 | 94 |
| `paper_note_bridge.target_mix` | pass | error | claim and area | {'area': 35, 'claim': 59} |
| `paper_note_bridge.targets_present` | pass | error | all true | Counter({'true': 94}) |
| `paper_note_bridge_02.row_count` | pass | error | 35 | 35 |
| `paper_note_bridge_02.target_mix` | pass | error | claim and area | {'claim': 20, 'area': 15} |
| `paper_note_bridge_02.targets_present` | pass | error | all true | Counter({'true': 35}) |
| `manual_overlays.claim_row_count` | pass | error | 118 | 118 |
| `manual_overlays.area_row_count` | pass | error | 192 | 192 |
| `manual_overlays.claim_key_coverage` | pass | error | 118 | 118 |
| `manual_overlays.area_key_coverage` | pass | error | 192 | 192 |
| `review_progress.summary_count` | pass | error | 20 | 20 |
| `readiness_audit.row_count` | pass | error | 20 | 20 |
| `thesis_map.row_count` | pass | error | 8 | 8 |
| `thesis_map.claim_coverage` | pass | error | 8 | 8 |
| `acceptance_criteria.row_count` | pass | error | 8 | 8 |
| `acceptance_criteria.claim_coverage` | pass | error | 8 | 8 |
| `claim_decision_board.row_count` | pass | error | 8 | 8 |
| `claim_decision_board.claim_coverage` | pass | error | 8 | 8 |
| `claim_decision_board.decision_alignment` | pass | error | same decisions | aligned |
| `claim_risk_register.row_count` | pass | error | 8 | 8 |
| `claim_risk_register.claim_coverage` | pass | error | 8 | 8 |
| `claim_risk_register.risk_mix` | pass | error | critical/high risk tiers | ['critical', 'high', 'process'] |
| `claim_risk_register.falsification_tests` | pass | error | all present | all present |
| `safe_statement_register.row_count` | pass | error | 20 | 20 |
| `safe_statement_register.type_mix` | pass | error | claim=8, area=12 | {'claim': 8, 'area': 12} |
| `safe_statement_register.no_promoted_claims` | pass | error | no candidate_for_headline | ['context_only', 'directional_only', 'hypothesis_only'] |
| `safe_statement_register.caveats_present` | pass | error | all present | all present |
| `review_execution_dashboard.row_count` | pass | error | >=8 | 9 |
| `review_execution_dashboard.metric_mix` | pass | error | manual_review/quality_gate/claim_gate | ['claim_gate', 'manual_review', 'quality_gate'] |
| `review_execution_actions.row_count` | pass | error | 8 | 8 |
| `review_execution_actions.claim_coverage` | pass | error | 8 | 8 |
| `review_execution_actions.priority_mix` | pass | error | priorities 1 and 2 | ['1', '2', '4'] |
| `researcher_action_plan.row_count` | pass | error | 5 | 5 |
| `researcher_action_plan.budget_coverage` | pass | error | ['1_day', '2_hours', '30_minutes', 'full_review_sprint', 'half_day'] | ['1_day', '2_hours', '30_minutes', 'full_review_sprint', 'half_day'] |
| `researcher_action_plan.stop_conditions` | pass | error | all present | all present |
| `research_questions.row_count` | pass | error | 10 | 10 |
| `research_questions.priority_coverage` | pass | error | 1..10 | ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] |
| `research_questions.falsification_tests` | pass | error | all present | all present |
| `research_questions.first_artifacts` | pass | error | all present | all present |
| `review_decision_tasks.row_count` | pass | error | 75 | 75 |
| `review_decision_tasks.key_coverage` | pass | error | 75 | 75 |
| `review_decision_tasks.claim_coverage` | pass | error | 8 | 8 |
| `review_decision_tasks.manual_fields` | pass | error | all present | all present |
| `paper_source_access.row_count` | pass | error | 56 | 56 |
| `paper_source_access.event_coverage` | pass | error | 56 | 56 |
| `paper_source_access.icml_urls` | pass | error | all present | all present |
| `paper_source_access.pdf_coverage` | pass | error | >=50 | 53 |
| `paper_source_access.extraction_fields` | pass | error | all present | all present |
| `pdf_extraction_probe.row_count` | pass | error | >=8 | 8 |
| `pdf_extraction_probe.priority_alignment` | pass | error | prefix of source-access PDF rows | aligned |
| `pdf_extraction_probe.downloads` | pass | error | downloaded/cached | ['cached'] |
| `pdf_extraction_probe.extractable` | pass | error | ok and >=500 chars | all extractable |
| `pdf_review_cards.row_count` | pass | error | 8 | 8 |
| `pdf_review_cards.event_coverage` | pass | error | 8 | 8 |
| `pdf_review_cards.page_cue_coverage` | pass | error | 8 | 8 |
| `pdf_review_cards.method_evidence_pages` | pass | error | all present | all present |
| `pdf_review_cards.card_file_count` | pass | error | 8 | 8 |
| `pdf_review_worksheet.row_count` | pass | error | 8 | 8 |
| `pdf_review_worksheet.event_coverage` | pass | error | 8 | 8 |
| `pdf_review_worksheet.blank_judgments` | pass | error | blank generated fields | blank |
| `pdf_review_worksheet.navigation_fields` | pass | error | all present | all present |
| `pdf_review_transfer.row_count` | pass | error | >=16 | 23 |
| `pdf_review_transfer.event_coverage` | pass | error | 8 | 8 |
| `pdf_review_transfer.target_mix` | pass | error | claim and area | {'area': 8, 'claim': 15} |
| `pdf_review_transfer.targets_present` | pass | error | all true | all true |
| `gap_audit.row_count` | pass | error | >=8 | 8 |
| `readiness_audit.type_mix` | pass | error | claim=8, area=12 | {'area': 12, 'claim': 8} |
| `review_progress.remaining_total` | pass | warning | 310 | 310 |
| `claims.queue_covers_all_claims` | pass | error | 8 | 8 |
| `claims.manual_fields_blank` | pass | warning | all blank | all blank |
| `packets.claim_packet_count` | pass | error | 8 | 8 |
| `packets.claim_evidence_dossier_count` | pass | error | 8 | 8 |
| `packets.area_briefing_card_count` | pass | error | 12 | 12 |
| `packets.area_packet_count` | pass | error | 12 | 12 |
| `trends.arxiv_area_count` | pass | error | 12 | 12 |
| `trends.arxiv_complete` | pass | error | all true | all true |
| `trends.historical_delta_count` | pass | error | 12 | 12 |
| `figures.topic_group_distribution.png` | pass | error | valid PNG | (1779, 882) |
| `figures.theme_counts_orals.png` | pass | error | valid PNG | (1960, 1242) |
| `figures.cluster_vote_density_oral_enrichment.png` | pass | error | valid PNG | (1960, 1422) |
| `figures.cluster_public_vs_program_signal.png` | pass | error | valid PNG | (1780, 1242) |
| `figures.alphaxiv_attention_distributions.png` | pass | error | valid PNG | (2141, 882) |
| `figures.top_canonical_institutions.png` | pass | error | valid PNG | (1780, 1782) |
| `figures.sector_mix_papers.png` | pass | error | valid PNG | (1780, 972) |
| `figures.institution_collaboration_hubs.png` | pass | error | valid PNG | (1780, 1242) |
| `figures.team_size_distribution.png` | pass | error | valid PNG | (1781, 972) |
| `figures.semantic_cluster_map.png` | pass | error | valid PNG | (1960, 1422) |
| `figures.semantic_cluster_vote_density.png` | pass | error | valid PNG | (1959, 1422) |
| `figures.manual_taxonomy_area_sizes.png` | pass | error | valid PNG | (1966, 1242) |
| `figures.evidence_contribution_mix.png` | pass | error | valid PNG | (2140, 1220) |
| `figures.program_signal_calibration.png` | pass | error | valid PNG | (1960, 1242) |
| `figures.arxiv_taxonomy_trends.png` | pass | error | valid PNG | (1967, 1242) |
| `figures.historical_venue_area_deltas.png` | pass | error | valid PNG | (1967, 1242) |
| `reports.icml2026_newcomer_area_tour.md` | pass | error | >200 bytes | 13677 |
| `reports.icml2026_newcomer_trend_lessons.md` | pass | error | >200 bytes | 7612 |
| `reports.icml2026_newcomer_paper_course.md` | pass | error | >200 bytes | 15401 |
| `reports.icml2026_newcomer_final_quiz.md` | pass | error | >200 bytes | 7080 |
| `reports.icml2026_newcomer_quiz_answer_key.md` | pass | error | >200 bytes | 11768 |
| `reports.icml2026_newcomer_briefing_template.md` | pass | error | >200 bytes | 1167 |
| `reports.icml2026_newcomer_course_audit.md` | pass | error | >200 bytes | 4747 |
| `reports.icml2026_pdf_review_seed_judgments.md` | pass | error | >200 bytes | 5378 |
| `reports.icml2026_landscape_synthesis.md` | pass | error | >200 bytes | 8793 |
| `reports.icml2026_overview_report_seed.md` | pass | error | >200 bytes | 15229 |
| `reports.icml2026_story_outline_seed.md` | pass | error | >200 bytes | 7148 |
| `reports.icml2026_researcher_audit.md` | pass | error | >200 bytes | 8062 |
| `reports.icml2026_researcher_readiness_audit.md` | pass | error | >200 bytes | 8745 |
| `reports.icml2026_researcher_thesis_map.md` | pass | error | >200 bytes | 13218 |
| `reports.icml2026_claim_acceptance_criteria.md` | pass | error | >200 bytes | 5435 |
| `reports.icml2026_claim_decision_board.md` | pass | error | >200 bytes | 7773 |
| `reports.icml2026_claim_risk_register.md` | pass | error | >200 bytes | 18214 |
| `reports.icml2026_safe_statement_register.md` | pass | error | >200 bytes | 21582 |
| `reports.icml2026_review_execution_dashboard.md` | pass | error | >200 bytes | 3628 |
| `reports.icml2026_researcher_action_plan.md` | pass | error | >200 bytes | 6453 |
| `reports.icml2026_research_questions_agenda.md` | pass | error | >200 bytes | 18751 |
| `reports.icml2026_review_decision_tasks.md` | pass | error | >200 bytes | 16273 |
| `reports.icml2026_paper_source_access_map.md` | pass | error | >200 bytes | 7811 |
| `reports.icml2026_pdf_extraction_probe.md` | pass | error | >200 bytes | 2791 |
| `reports.icml2026_pdf_review_cards.md` | pass | error | >200 bytes | 2109 |
| `reports.icml2026_pdf_review_worksheet.md` | pass | error | >200 bytes | 3138 |
| `reports.icml2026_pdf_review_transfer_checklist.md` | pass | error | >200 bytes | 7126 |
| `reports.icml2026_researcher_gap_audit.md` | pass | error | >200 bytes | 5202 |
| `reports.icml2026_researcher_review_plan.md` | pass | error | >200 bytes | 15836 |
| `reports.icml2026_review_sprint_01.md` | pass | error | >200 bytes | 95438 |
| `reports.icml2026_review_sprint_02.md` | pass | error | >200 bytes | 21143 |
| `reports.icml2026_sprint_reading_brief_index.md` | pass | error | >200 bytes | 14220 |
| `reports.icml2026_sprint_prereview_suggestions.md` | pass | error | >200 bytes | 7967 |
| `reports.icml2026_sprint_02_prereview_suggestions.md` | pass | error | >200 bytes | 3780 |
| `reports.icml2026_paper_note_workspace.md` | pass | error | >200 bytes | 2470 |
| `reports.icml2026_sprint_02_paper_note_workspace.md` | pass | error | >200 bytes | 641 |
| `reports.icml2026_manual_review_codebook.md` | pass | error | >200 bytes | 15384 |
| `reports.icml2026_manual_review_value_lint.md` | pass | error | >200 bytes | 1043 |
| `reports.icml2026_paper_note_overlay_bridge.md` | pass | error | >200 bytes | 9561 |
| `reports.icml2026_sprint_02_overlay_bridge.md` | pass | error | >200 bytes | 300 |
| `reports.manual_review_workspace.md` | pass | error | >200 bytes | 1807 |
| `reports.reviewed_validation_tables.md` | pass | error | >200 bytes | 702 |
| `reports.icml2026_claim_evidence_dossier_index.md` | pass | error | >200 bytes | 2257 |
| `reports.icml2026_area_briefing_card_index.md` | pass | error | >200 bytes | 3000 |
| `reports.icml2026_area_risk_register.md` | pass | error | >200 bytes | 16715 |
| `reports.icml2026_claim_validation_packet_index.md` | pass | error | >200 bytes | 1540 |
| `reports.icml2026_validation_packet_index.md` | pass | error | >200 bytes | 2008 |
| `reports.icml2026_program_signal_calibration.md` | pass | error | >200 bytes | 24806 |
| `reports.icml2026_public_program_divergence_set.md` | pass | error | >200 bytes | 11646 |
| `reports.icml2026_taxonomy_adjudication_queue.md` | pass | error | >200 bytes | 41343 |
| `reports.icml2026_artifact_audit_queue.md` | pass | error | >200 bytes | 10132 |
| `reports.icml2026_baseline_sensitivity_queue.md` | pass | error | >200 bytes | 5476 |
| `reports.historical_accepted_paper_baseline.md` | pass | error | >200 bytes | 3696 |
| `reports.arxiv_taxonomy_trends.md` | pass | error | >200 bytes | 2442 |
| `reports.icml2026_visual_eda_index.md` | pass | error | >200 bytes | 4348 |
| `newcomer.routes` | pass | error | ['Quick Tour', 'Standard Route', 'Deep Route'] | ['Quick Tour', 'Standard Route', 'Deep Route'] |
| `newcomer.roadmap_lessons` | pass | error | 7 | 7 |
| `newcomer.area_lessons` | pass | error | 12 | 12 |
| `newcomer.area_quick_checks` | pass | error | 12 | 12 |
| `newcomer.trend_lessons` | pass | error | 6 | 6 |
| `newcomer.trend_caveats` | pass | error | 6 | 6 |
| `newcomer.paper_lessons` | pass | error | 12 | 12 |
| `newcomer.quiz_parts` | pass | error | 5 | 5 |
| `newcomer.quiz_points` | pass | error | 100 | 100 |
| `newcomer.answer_key` | pass | error | A-E coverage | complete |
| `newcomer.review_paths` | pass | error | >=5 | 5 |
| `newcomer.slides_exists` | pass | error | >1 MB | 1817392 |
| `newcomer.slides_count` | pass | error | 47 | 47 |
| `newcomer.slides_area_depth` | pass | error | 12 area maps + 12 paper slides | 12 area maps + 12 paper slides |
| `newcomer.slides_figures` | pass | error | 4 | 4 |
| `newcomer.slides_self_contained` | pass | error | no external assets | no external assets |
| `newcomer.slides_controls` | pass | error | all controls | complete |
| `inventory.docs/project_index.md` | pass | error | present | present |
| `inventory.docs/dashboard.html` | pass | error | present | present |
| `inventory.docs/data_dictionary.md` | pass | error | present | present |
| `inventory.data/processed/project_artifact_inventory.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_claim_validation_reviewed.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_area_validation_reviewed.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_researcher_thesis_map.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_claim_acceptance_criteria.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_claim_decision_board.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_claim_risk_register.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_safe_statement_register.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_review_execution_dashboard.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_review_execution_claim_actions.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_researcher_action_plan.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_research_questions_agenda.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_review_decision_tasks.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_paper_source_access_map.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_pdf_extraction_probe.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_pdf_review_cards.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_pdf_page_cues.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_pdf_review_worksheet.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_pdf_review_transfer_checklist.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_researcher_gap_audit.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_sprint_prereview_suggestions.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_review_sprint_02.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_sprint_reading_briefs.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_sprint_02_prereview_suggestions.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_manual_review_codebook.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_manual_review_value_lint.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_manual_review_value_lint_summary.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_paper_note_overlay_bridge.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_sprint_02_overlay_bridge.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_area_risk_register.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_public_program_divergence_set.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_taxonomy_adjudication_queue.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_artifact_audit_queue.csv` | pass | error | present | present |
| `inventory.data/processed/icml2026_baseline_sensitivity_queue.csv` | pass | error | present | present |
| `inventory.data/manual/claim_review_overrides.csv` | pass | error | present | present |
| `inventory.data/manual/area_review_overrides.csv` | pass | error | present | present |
| `inventory.data/manual/icml2026_review_sprint_01_paper_notes.csv` | pass | error | present | present |
| `inventory.data/manual/icml2026_review_sprint_02_paper_notes.csv` | pass | error | present | present |
| `inventory.reports/icml2026_landscape_synthesis.md` | pass | error | present | present |
| `inventory.reports/icml2026_claim_validation_packet_index.md` | pass | error | present | present |
| `inventory.reports/manual_review_progress.md` | pass | error | present | present |
| `inventory.reports/manual_review_workspace.md` | pass | error | present | present |
| `inventory.reports/reviewed_validation_tables.md` | pass | error | present | present |
| `inventory.reports/icml2026_researcher_readiness_audit.md` | pass | error | present | present |
| `inventory.reports/icml2026_researcher_thesis_map.md` | pass | error | present | present |
| `inventory.reports/icml2026_claim_acceptance_criteria.md` | pass | error | present | present |
| `inventory.reports/icml2026_claim_decision_board.md` | pass | error | present | present |
| `inventory.reports/icml2026_claim_risk_register.md` | pass | error | present | present |
| `inventory.reports/icml2026_safe_statement_register.md` | pass | error | present | present |
| `inventory.reports/icml2026_review_execution_dashboard.md` | pass | error | present | present |
| `inventory.reports/icml2026_researcher_action_plan.md` | pass | error | present | present |
| `inventory.reports/icml2026_research_questions_agenda.md` | pass | error | present | present |
| `inventory.reports/icml2026_review_decision_tasks.md` | pass | error | present | present |
| `inventory.reports/icml2026_paper_source_access_map.md` | pass | error | present | present |
| `inventory.reports/icml2026_pdf_extraction_probe.md` | pass | error | present | present |
| `inventory.reports/icml2026_pdf_review_cards.md` | pass | error | present | present |
| `inventory.reports/icml2026_pdf_review_worksheet.md` | pass | error | present | present |
| `inventory.reports/icml2026_pdf_review_transfer_checklist.md` | pass | error | present | present |
| `inventory.reports/icml2026_researcher_gap_audit.md` | pass | error | present | present |
| `inventory.reports/icml2026_researcher_review_plan.md` | pass | error | present | present |
| `inventory.reports/icml2026_review_sprint_01.md` | pass | error | present | present |
| `inventory.reports/icml2026_review_sprint_02.md` | pass | error | present | present |
| `inventory.reports/icml2026_sprint_reading_brief_index.md` | pass | error | present | present |
| `inventory.reports/icml2026_sprint_prereview_suggestions.md` | pass | error | present | present |
| `inventory.reports/icml2026_sprint_02_prereview_suggestions.md` | pass | error | present | present |
| `inventory.reports/icml2026_paper_note_workspace.md` | pass | error | present | present |
| `inventory.reports/icml2026_sprint_02_paper_note_workspace.md` | pass | error | present | present |
| `inventory.reports/icml2026_manual_review_codebook.md` | pass | error | present | present |
| `inventory.reports/icml2026_manual_review_value_lint.md` | pass | error | present | present |
| `inventory.reports/icml2026_paper_note_overlay_bridge.md` | pass | error | present | present |
| `inventory.reports/icml2026_sprint_02_overlay_bridge.md` | pass | error | present | present |
| `inventory.reports/icml2026_public_program_divergence_set.md` | pass | error | present | present |
| `inventory.reports/icml2026_taxonomy_adjudication_queue.md` | pass | error | present | present |
| `inventory.reports/icml2026_artifact_audit_queue.md` | pass | error | present | present |
| `inventory.reports/icml2026_baseline_sensitivity_queue.md` | pass | error | present | present |
| `inventory.reports/icml2026_claim_evidence_dossier_index.md` | pass | error | present | present |
| `inventory.reports/icml2026_area_briefing_card_index.md` | pass | error | present | present |
| `inventory.reports/icml2026_area_risk_register.md` | pass | error | present | present |
| `inventory.docs/icml2026_newcomer_roadmap.md` | pass | error | present | present |
| `inventory.docs/newcomer_glossary.md` | pass | error | present | present |
| `inventory.docs/newcomer_learning_goal.md` | pass | error | present | present |
| `inventory.docs/icml2026_newcomer_slides.html` | pass | error | present | present |
| `inventory.reports/icml2026_newcomer_area_tour.md` | pass | error | present | present |
| `inventory.reports/icml2026_newcomer_trend_lessons.md` | pass | error | present | present |
| `inventory.reports/icml2026_newcomer_paper_course.md` | pass | error | present | present |
| `inventory.reports/icml2026_newcomer_final_quiz.md` | pass | error | present | present |
| `inventory.reports/icml2026_newcomer_quiz_answer_key.md` | pass | error | present | present |
| `inventory.reports/icml2026_newcomer_briefing_template.md` | pass | error | present | present |
| `inventory.reports/icml2026_newcomer_course_audit.md` | pass | error | present | present |
| `dashboard.exists` | pass | error | >1000 bytes | 4341841 |
| `dashboard.payload` | pass | error | papers=6628, areas=12, claims=8, review=20, figures>=6, newcomer_link=true, newcomer_slides_link=true, readiness_link=true, dossier_link=true, area_briefings_link=true, review_plan_link=true, review_sprint_link=true, manual_review_link=true, pdf_cards=8, pdf_worksheet=8, pdf_transfer=23, pdf_links=true | papers=6628, areas=12, claims=8, review=20, figures=6, readiness_link=True, newcomer_link=True, newcomer_slides_link=True, dossier_link=True, area_briefings_link=True, review_plan_link=True, review_sprint_link=True, manual_review_link=True, pdf_cards=8, pdf_worksheet=8, pdf_transfer=23, pdf_cards_link=True, pdf_worksheet_link=True, pdf_transfer_link=True |
| `public.pages` | pass | error | all core pages | complete |
| `public.learning_path` | pass | error | 18 lessons, including 12 areas | 18 lessons, including 12 areas |
| `public.interactive_quiz` | pass | error | 24 MCQs + keyboard + retry | 24 MCQs; keyboard=True; retry=True |
| `public.readme_length` | pass | error | at most 100 lines | 55 |
| `python.uv_project` | pass | error | pyproject + uv.lock + dev group | lock=True; configured=True |
| `python.uv_commands` | pass | error | uv commands only | complete |
| `public.pages_workflow` | pass | error | uv build + Pages deploy | complete |