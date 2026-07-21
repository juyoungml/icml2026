# ICML 2026 Data Dictionary

Generated schema and row-count reference for processed CSV files.

## Summary

- Processed CSV files: 96
- Total CSV rows across processed files: 137,762

## `data/processed/alphaxiv_icml2026_joined.csv`

- Rows: 6628
- Columns: 24
- Description: Official ICML rows joined with AlphaXiv public-attention and GitHub metadata.

Columns:
- `alphaxiv_rank`
- `icml_id`
- `title`
- `authors`
- `topic_group`
- `topic`
- `session`
- `scheduled_at`
- `icml_url`
- `alphaxiv_url`
- `arxiv_id`
- `paper_group_id`
- `public_total_votes`
- `total_votes`
- `visits_all`
- `visits_last_7_days`
- `github_stars`
- `github_url`
- `organizations`
- `abstract`
- `matched_icml`
- `is_oral`
- `is_position`
- `award`

## `data/processed/alphaxiv_icml2026_papers.csv`

- Rows: 6628
- Columns: 20

Columns:
- `alphaxiv_rank`
- `icml_id`
- `title`
- `authors`
- `topic_group`
- `topic`
- `session`
- `scheduled_at`
- `icml_url`
- `alphaxiv_url`
- `arxiv_id`
- `paper_group_id`
- `public_total_votes`
- `total_votes`
- `visits_all`
- `visits_last_7_days`
- `github_stars`
- `github_url`
- `organizations`
- `abstract`

## `data/processed/arxiv_taxonomy_trend_counts.csv`

- Rows: 36
- Columns: 6

Columns:
- `area`
- `year`
- `arxiv_count`
- `query_terms`
- `query`
- `status`

## `data/processed/arxiv_taxonomy_trend_summary.csv`

- Rows: 12
- Columns: 10
- Description: Broad arXiv query-count trend summary by taxonomy area.

Columns:
- `area`
- `arxiv_2024`
- `arxiv_2025`
- `arxiv_2026_ytd`
- `growth_2025_vs_2024`
- `growth_2026_ytd_vs_2025`
- `status_complete`
- `icml2026_taxonomy_papers`
- `icml2026_area_share`
- `query_terms`

## `data/processed/historical_accepted_papers_classified.csv`

- Rows: 21293
- Columns: 23
- Description: Accepted papers from ICML 2026/ICML 2025/NeurIPS 2025/ICLR 2026 classified with a shared keyword scorer.

Columns:
- `venue`
- `year`
- `event_id`
- `event_type`
- `title`
- `decision`
- `topic`
- `topic_group`
- `authors`
- `institutions`
- `author_count`
- `institution_count`
- `abstract_available`
- `url`
- `paper_url`
- `area`
- `area_score`
- `second_area`
- `second_score`
- `score_margin`
- `confidence`
- `matched_terms`
- `all_area_scores`

## `data/processed/historical_venue_area_summary.csv`

- Rows: 52
- Columns: 11

Columns:
- `venue`
- `year`
- `area`
- `paper_count`
- `share`
- `high_confidence_count`
- `medium_confidence_count`
- `low_confidence_count`
- `uncoded_count`
- `abstract_available_count`
- `representative_titles`

## `data/processed/historical_venue_delta_summary.csv`

- Rows: 12
- Columns: 9
- Description: ICML 2026 area-share deltas versus neighboring accepted-paper baselines.

Columns:
- `area`
- `icml2026_count`
- `icml2026_share`
- `icml2025_share`
- `neurips2025_share`
- `iclr2026_share`
- `baseline_avg_share`
- `delta_vs_baseline_avg`
- `relative_to_baseline_avg`

## `data/processed/icml2026_area_briefing_cards.csv`

- Rows: 12
- Columns: 23
- Description: Compact per-area briefing cards with signals, trust tiers, and reading starts.

Columns:
- `area`
- `brief_path`
- `trust_tier`
- `trust_reason`
- `paper_count`
- `taxonomy_share`
- `oral_enrichment`
- `public_attention_enrichment`
- `historical_delta_vs_baseline`
- `github_url_share`
- `review_rows`
- `reviewed_rows`
- `remaining_rows`
- `headline`
- `fault_lines`
- `read_for`
- `top_subareas`
- `top_methods`
- `top_evaluations`
- `program_papers`
- `public_non_program_papers`
- `artifact_papers`
- `boundary_papers`

## `data/processed/icml2026_area_evidence_summary.csv`

- Rows: 12
- Columns: 17
- Description: Area-level aggregation of heuristic evidence tags.

Columns:
- `area`
- `paper_count`
- `github_url_count`
- `github_url_share`
- `benchmark_mention_count`
- `benchmark_mention_share`
- `dataset_mention_count`
- `dataset_mention_share`
- `metric_mention_count`
- `metric_mention_share`
- `top_primary_contribution_types`
- `top_all_contribution_types`
- `top_method_families`
- `top_evaluation_settings`
- `top_result_claim_types`
- `evidence_confidence_mix`
- `high_signal_examples`

## `data/processed/icml2026_area_fault_lines.csv`

- Rows: 12
- Columns: 21

Columns:
- `area`
- `paper_count`
- `oral_count`
- `award_count`
- `votes_per_paper`
- `github_url_share`
- `taxonomy_clusters`
- `clusters_needing_review`
- `headline`
- `fault_lines`
- `read_for`
- `evidence`
- `top_subareas`
- `top_themes`
- `top_primary_contribution_types`
- `top_method_families`
- `top_evaluation_settings`
- `top_result_claim_types`
- `representative_papers`
- `public_not_program_papers`
- `program_not_public_papers`

## `data/processed/icml2026_area_program_calibration.csv`

- Rows: 12
- Columns: 19
- Description: Area-level oral/award/public-attention calibration.

Columns:
- `group`
- `paper_count`
- `paper_share`
- `oral_count`
- `oral_rate`
- `oral_share`
- `oral_enrichment`
- `award_count`
- `award_rate`
- `award_share`
- `award_enrichment`
- `total_public_votes`
- `votes_per_paper`
- `public_vote_share`
- `public_attention_enrichment`
- `program_vs_public_delta`
- `high_signal_papers`
- `public_not_program_papers`
- `program_low_public_papers`

## `data/processed/icml2026_area_risk_register.csv`

- Rows: 12
- Columns: 23
- Description: Area-level reliability, falsification, and safe-language register.

Columns:
- `area`
- `risk_tier`
- `trust_tier`
- `readiness_tier`
- `paper_count`
- `taxonomy_share`
- `oral_enrichment`
- `public_attention_enrichment`
- `historical_delta_vs_baseline`
- `baseline_risk_tier`
- `baseline_issue_types`
- `reviewed_rows`
- `review_rows`
- `taxonomy_clusters_to_adjudicate`
- `low_confidence_rows`
- `program_or_award_rows`
- `github_rows`
- `main_risk_driver`
- `falsification_test`
- `safe_language`
- `recommended_first_checks`
- `brief_path`
- `baseline_safe_language`

## `data/processed/icml2026_area_validation_reviewed.csv`

- Rows: 192
- Columns: 42
- Description: Area validation queue merged with manual review overlays.

Columns:
- `area`
- `area_review_rank`
- `selection_reason`
- `event_id`
- `title`
- `subarea`
- `semantic_cluster_id`
- `cluster_review_status`
- `cluster_review_notes`
- `is_oral`
- `award`
- `public_total_votes`
- `github_url`
- `artifact_confidence`
- `heuristic_primary_contribution_type`
- `heuristic_contribution_types`
- `heuristic_method_families`
- `heuristic_evaluation_settings`
- `heuristic_result_claim_types`
- `heuristic_benchmark_mentions`
- `heuristic_dataset_mentions`
- `heuristic_metric_mentions`
- `heuristic_evidence_confidence`
- `manual_validated`
- `manual_primary_contribution_type`
- `manual_method_family`
- `manual_benchmarks`
- `manual_datasets`
- `manual_metrics`
- `manual_artifact_status`
- `manual_result_character`
- `manual_fault_line_relevance`
- `manual_notes`
- `url`
- `alphaxiv_url`
- `abstract`
- `review_overlay_present`
- `review_overlay_filled_fields`
- `reviewed`
- `reviewer`
- `review_date`
- `review_source`

## `data/processed/icml2026_artifact_audit_queue.csv`

- Rows: 160
- Columns: 23
- Description: Paper-level artifact audit queue for reproducibility and repository-link checks.

Columns:
- `audit_rank`
- `audit_priority_score`
- `audit_category`
- `event_id`
- `title`
- `topic_group`
- `is_oral`
- `award`
- `public_total_votes`
- `github_url`
- `github_repo`
- `alphaxiv_github_stars`
- `artifact_confidence`
- `needs_manual_check_reason`
- `live_status`
- `live_qa_flags`
- `live_license_spdx`
- `live_pushed_at`
- `live_pushed_age_days`
- `audit_reason`
- `manual_checks`
- `alphaxiv_url`
- `icml_url`

## `data/processed/icml2026_audience_reading_paths.csv`

- Rows: 250
- Columns: 21
- Description: Role-specific paper reading tracks.

Columns:
- `audience`
- `phase`
- `rank`
- `title`
- `why_read`
- `award`
- `is_oral`
- `public_total_votes`
- `visits_last_7_days`
- `github_stars`
- `reading_score`
- `themes`
- `cluster_id`
- `cluster_label`
- `official_topic`
- `sector_mix`
- `authors`
- `canonical_institutions`
- `url`
- `alphaxiv_url`
- `github_url`

## `data/processed/icml2026_author_collaboration_edges.csv`

- Rows: 1000
- Columns: 3

Columns:
- `author_a`
- `author_b`
- `shared_paper_count`

## `data/processed/icml2026_author_counts.csv`

- Rows: 25919
- Columns: 14

Columns:
- `author`
- `paper_count`
- `oral_count`
- `award_count`
- `public_total_votes`
- `votes_per_paper`
- `visits_last_7_days`
- `unique_coauthor_count`
- `coauthor_pagerank`
- `top_topic_groups`
- `top_themes`
- `top_clusters`
- `top_institutions`
- `top_coauthors`

## `data/processed/icml2026_awards.csv`

- Rows: 10
- Columns: 4

Columns:
- `award`
- `title`
- `authors`
- `url`

## `data/processed/icml2026_baseline_sensitivity_queue.csv`

- Rows: 12
- Columns: 17
- Description: Area-level spot-check queue for using historical venue baselines and arXiv query trends responsibly.

Columns:
- `area`
- `risk_tier`
- `issue_types`
- `icml2026_papers`
- `icml2026_share`
- `baseline_avg_share`
- `historical_delta_pp`
- `historical_relative_to_baseline`
- `arxiv_2025_vs_2024_growth`
- `arxiv_query_terms`
- `historical_comparison_papers`
- `signal_tags`
- `check_question`
- `recommended_action`
- `safe_language`
- `icml2026_examples`
- `historical_examples`

## `data/processed/icml2026_canonical_institution_counts.csv`

- Rows: 300
- Columns: 4

Columns:
- `canonical_institution`
- `paper_count`
- `sector`
- `common_raw_forms`

## `data/processed/icml2026_claim_acceptance_criteria.csv`

- Rows: 8
- Columns: 20
- Description: Explicit promotion gates for synthesis claims using reviewed rows, paper notes, taxonomy checks, and artifact checks.

Columns:
- `claim_id`
- `theme`
- `thesis_role`
- `decision`
- `review_gate`
- `support_gate`
- `paper_note_gate`
- `taxonomy_gate`
- `artifact_gate`
- `minimum_reviewed_rows`
- `reviewed_rows`
- `minimum_support_rows`
- `support_rows`
- `weakening_rows`
- `minimum_paper_notes`
- `paper_notes_started`
- `artifact_rows_checked`
- `missing_for_promotion`
- `special_check`
- `allowed_next_use`

## `data/processed/icml2026_claim_decision_board.csv`

- Rows: 8
- Columns: 27
- Description: Claim-level operating board combining acceptance gates, sprint coverage, and overlay transfer actions.

Columns:
- `claim_id`
- `theme`
- `thesis_role`
- `decision`
- `readiness_tier`
- `allowed_next_use`
- `statement`
- `evidence`
- `primary_caveat`
- `reviewed_rows`
- `minimum_reviewed_rows`
- `support_rows`
- `minimum_support_rows`
- `paper_notes_started`
- `minimum_paper_notes`
- `missing_for_promotion`
- `claim_bridge_rows`
- `bridge_pending_notes`
- `bridge_started_needs_decision`
- `bridge_ready_to_transfer`
- `sprint_claim_papers`
- `sprint_02_claim_papers`
- `sprint_02_bridge_rows`
- `next_decision_action`
- `first_overlay_actions`
- `top_papers_to_read`
- `special_check`

## `data/processed/icml2026_claim_evidence_dossiers.csv`

- Rows: 118
- Columns: 27
- Description: Paper-level claim pre-review buckets, rationales, and abstract excerpts.

Columns:
- `claim_id`
- `claim_theme`
- `claim_strength`
- `priority_claim`
- `claim_review_rank`
- `event_id`
- `title`
- `area`
- `subarea`
- `selection_reason`
- `pre_review_bucket`
- `pre_review_rationale`
- `keyword_hits`
- `is_oral`
- `award`
- `public_total_votes`
- `github_url`
- `github_stars`
- `needs_manual_check_reason`
- `taxonomy_review_status`
- `evidence_confidence`
- `abstract_excerpt`
- `manual_claim_support`
- `manual_taxonomy_judgment`
- `manual_artifact_judgment`
- `url`
- `alphaxiv_url`

## `data/processed/icml2026_claim_risk_register.csv`

- Rows: 8
- Columns: 22
- Description: Falsification-oriented risk register for headline synthesis claims.

Columns:
- `claim_id`
- `theme`
- `thesis_role`
- `decision`
- `risk_tier`
- `allowed_next_use`
- `statement_under_test`
- `current_evidence`
- `primary_caveat`
- `weakest_assumption`
- `falsification_test`
- `counterevidence_to_seek`
- `missing_for_promotion`
- `manual_evidence_needed`
- `pre_review_bucket_mix`
- `evidence_confidence_mix`
- `taxonomy_review_rows`
- `artifact_candidate_rows`
- `special_check`
- `next_decision_action`
- `first_papers_to_read`
- `first_briefs_to_open`

## `data/processed/icml2026_claim_validation_queue.csv`

- Rows: 118
- Columns: 39
- Description: Paper-level review queue for synthesis claims.

Columns:
- `claim_id`
- `claim_theme`
- `claim_statement`
- `claim_strength`
- `claim_review_question`
- `claim_review_rank`
- `selection_reason`
- `review_focus`
- `event_id`
- `title`
- `area`
- `subarea`
- `semantic_cluster_id`
- `semantic_cluster_label`
- `taxonomy_confidence`
- `review_status`
- `cluster_review_notes`
- `is_oral`
- `award`
- `public_total_votes`
- `visits_last_7_days`
- `github_url`
- `github_repo`
- `github_stars`
- `needs_manual_check_reason`
- `primary_contribution_type`
- `method_families`
- `evaluation_settings`
- `benchmark_mentions`
- `dataset_mentions`
- `metric_mentions`
- `evidence_confidence`
- `manual_claim_support`
- `manual_taxonomy_judgment`
- `manual_artifact_judgment`
- `manual_notes`
- `url`
- `alphaxiv_url`
- `abstract`

## `data/processed/icml2026_claim_validation_reviewed.csv`

- Rows: 118
- Columns: 45
- Description: Claim validation queue merged with manual review overlays.

Columns:
- `claim_id`
- `claim_theme`
- `claim_statement`
- `claim_strength`
- `claim_review_question`
- `claim_review_rank`
- `selection_reason`
- `review_focus`
- `event_id`
- `title`
- `area`
- `subarea`
- `semantic_cluster_id`
- `semantic_cluster_label`
- `taxonomy_confidence`
- `review_status`
- `cluster_review_notes`
- `is_oral`
- `award`
- `public_total_votes`
- `visits_last_7_days`
- `github_url`
- `github_repo`
- `github_stars`
- `needs_manual_check_reason`
- `primary_contribution_type`
- `method_families`
- `evaluation_settings`
- `benchmark_mentions`
- `dataset_mentions`
- `metric_mentions`
- `evidence_confidence`
- `manual_claim_support`
- `manual_taxonomy_judgment`
- `manual_artifact_judgment`
- `manual_notes`
- `url`
- `alphaxiv_url`
- `abstract`
- `review_overlay_present`
- `review_overlay_filled_fields`
- `reviewed`
- `reviewer`
- `review_date`
- `review_source`

## `data/processed/icml2026_cluster_assignments.csv`

- Rows: 6628
- Columns: 18

Columns:
- `event_id`
- `cluster_id`
- `cluster_label`
- `title`
- `topic`
- `topic_group`
- `themes`
- `is_oral`
- `award`
- `public_total_votes`
- `visits_last_7_days`
- `github_stars`
- `composite_score`
- `cluster_distance`
- `cluster_centrality`
- `attention_score`
- `url`
- `alphaxiv_url`

## `data/processed/icml2026_cluster_diagnostics.csv`

- Rows: 5
- Columns: 4

Columns:
- `k`
- `sample_silhouette_cosine`
- `min_cluster_size`
- `max_cluster_size`

## `data/processed/icml2026_cluster_program_calibration.csv`

- Rows: 42
- Columns: 23

Columns:
- `semantic_cluster_id`
- `area`
- `subarea`
- `review_status`
- `group`
- `paper_count`
- `paper_share`
- `oral_count`
- `oral_rate`
- `oral_share`
- `oral_enrichment`
- `award_count`
- `award_rate`
- `award_share`
- `award_enrichment`
- `total_public_votes`
- `votes_per_paper`
- `public_vote_share`
- `public_attention_enrichment`
- `program_vs_public_delta`
- `high_signal_papers`
- `public_not_program_papers`
- `program_low_public_papers`

## `data/processed/icml2026_cluster_summary.csv`

- Rows: 30
- Columns: 17

Columns:
- `cluster_id`
- `cluster_label`
- `paper_count`
- `share`
- `oral_count`
- `award_count`
- `oral_rate`
- `oral_enrichment`
- `total_public_votes`
- `votes_per_paper`
- `public_vote_share`
- `recent_visits_7d`
- `top_terms`
- `top_topic_groups`
- `top_themes`
- `central_papers`
- `high_signal_papers`

## `data/processed/icml2026_collaboration_summary.csv`

- Rows: 11
- Columns: 2

Columns:
- `metric`
- `value`

## `data/processed/icml2026_events.csv`

- Rows: 6796
- Columns: 12

Columns:
- `event_id`
- `event_type`
- `title`
- `decision`
- `topic`
- `session`
- `starttime`
- `endtime`
- `url`
- `paper_url`
- `authors`
- `institutions`

## `data/processed/icml2026_github_artifact_live_check.csv`

- Rows: 50
- Columns: 26

Columns:
- `github_repo`
- `github_url`
- `live_status`
- `http_status`
- `qa_flags`
- `suspicious_reason`
- `paper_titles`
- `sources`
- `max_public_votes`
- `alphaxiv_github_stars`
- `live_stargazers_count`
- `live_forks_count`
- `open_issues_count`
- `archived`
- `disabled`
- `fork`
- `license_spdx`
- `default_branch`
- `created_at`
- `updated_at`
- `pushed_at`
- `pushed_age_days`
- `description`
- `homepage`
- `api_fetched_utc`
- `api_error`

## `data/processed/icml2026_institution_collaboration.csv`

- Rows: 3769
- Columns: 14

Columns:
- `canonical_institution`
- `sector`
- `paper_count`
- `oral_count`
- `award_count`
- `public_total_votes`
- `votes_per_paper`
- `visits_last_7_days`
- `unique_partner_count`
- `collaboration_pagerank`
- `top_topic_groups`
- `top_themes`
- `top_clusters`
- `top_partners`

## `data/processed/icml2026_institution_collaboration_edges.csv`

- Rows: 1000
- Columns: 3

Columns:
- `institution_a`
- `institution_b`
- `shared_paper_count`

## `data/processed/icml2026_institution_counts.csv`

- Rows: 200
- Columns: 2

Columns:
- `institution`
- `paper_count`

## `data/processed/icml2026_keyword_counts.csv`

- Rows: 200
- Columns: 3

Columns:
- `term`
- `count`
- `kind`

## `data/processed/icml2026_landscape_claim_register.csv`

- Rows: 8
- Columns: 7
- Description: Major synthesis claims, evidence, caveats, and next validation.

Columns:
- `claim_id`
- `theme`
- `statement`
- `evidence`
- `strength`
- `caveats`
- `next_validation`

## `data/processed/icml2026_landscape_signal_matrix.csv`

- Rows: 12
- Columns: 17
- Description: Area-level cross-source synthesis matrix.

Columns:
- `area`
- `taxonomy_papers`
- `taxonomy_share`
- `oral_enrichment`
- `award_count`
- `public_attention_enrichment`
- `votes_per_paper`
- `historical_delta_vs_baseline`
- `historical_relative_to_baseline`
- `arxiv_2025_vs_2024_growth`
- `github_url_share`
- `benchmark_mention_share`
- `metric_mention_share`
- `likely_code_share`
- `manual_check_artifact_share`
- `signal_tags`
- `representative_papers`

## `data/processed/icml2026_manual_review_codebook.csv`

- Rows: 81
- Columns: 7
- Description: Canonical coded values and transfer rules for paper notes and manual overlays.

Columns:
- `table`
- `field`
- `allowed_value`
- `counts_as_review`
- `meaning`
- `when_to_use`
- `promotion_effect`

## `data/processed/icml2026_manual_review_value_lint.csv`

- Rows: 0
- Columns: 8
- Description: Invalid manual coded values found by the codebook linter.

Columns:
- `path`
- `table`
- `row_number`
- `key`
- `field`
- `value`
- `allowed_values`
- `message`

## `data/processed/icml2026_manual_review_value_lint_summary.csv`

- Rows: 4
- Columns: 7
- Description: Per-file summary from the manual coded-value linter.

Columns:
- `path`
- `table`
- `rows`
- `coded_fields`
- `rows_with_coded_values`
- `checked_values`
- `invalid_values`

## `data/processed/icml2026_manual_taxonomy_areas.csv`

- Rows: 12
- Columns: 14
- Description: Curated 12-area taxonomy summary.

Columns:
- `area`
- `paper_count`
- `share`
- `oral_count`
- `oral_rate`
- `award_count`
- `total_public_votes`
- `votes_per_paper`
- `github_url_count`
- `github_url_share`
- `subareas`
- `semantic_clusters`
- `top_topic_groups`
- `representative_papers`

## `data/processed/icml2026_manual_taxonomy_clusters.csv`

- Rows: 42
- Columns: 18
- Description: Semantic cluster to curated taxonomy mapping with review flags.

Columns:
- `semantic_cluster_id`
- `area`
- `subarea`
- `taxonomy_confidence`
- `review_status`
- `review_notes`
- `semantic_cluster_label`
- `paper_count`
- `oral_count`
- `award_count`
- `votes_per_paper`
- `oral_enrichment`
- `top_terms`
- `top_topic_groups`
- `top_themes`
- `top_lexical_clusters`
- `central_papers`
- `high_signal_papers`

## `data/processed/icml2026_manual_taxonomy_papers.csv`

- Rows: 6628
- Columns: 19
- Description: Paper-level curated taxonomy assignments.

Columns:
- `event_id`
- `title`
- `area`
- `subarea`
- `semantic_cluster_id`
- `semantic_cluster_label`
- `taxonomy_confidence`
- `review_status`
- `topic_group`
- `topic`
- `themes`
- `is_oral`
- `award`
- `public_total_votes`
- `visits_last_7_days`
- `github_url`
- `artifact_confidence`
- `url`
- `alphaxiv_url`

## `data/processed/icml2026_manual_validation_queue.csv`

- Rows: 192
- Columns: 36
- Description: Paper-level review queue for area evidence and taxonomy boundaries.

Columns:
- `area`
- `area_review_rank`
- `selection_reason`
- `event_id`
- `title`
- `subarea`
- `semantic_cluster_id`
- `cluster_review_status`
- `cluster_review_notes`
- `is_oral`
- `award`
- `public_total_votes`
- `github_url`
- `artifact_confidence`
- `heuristic_primary_contribution_type`
- `heuristic_contribution_types`
- `heuristic_method_families`
- `heuristic_evaluation_settings`
- `heuristic_result_claim_types`
- `heuristic_benchmark_mentions`
- `heuristic_dataset_mentions`
- `heuristic_metric_mentions`
- `heuristic_evidence_confidence`
- `manual_validated`
- `manual_primary_contribution_type`
- `manual_method_family`
- `manual_benchmarks`
- `manual_datasets`
- `manual_metrics`
- `manual_artifact_status`
- `manual_result_character`
- `manual_fault_line_relevance`
- `manual_notes`
- `url`
- `alphaxiv_url`
- `abstract`

## `data/processed/icml2026_orals.csv`

- Rows: 168
- Columns: 3

Columns:
- `oral_event_id`
- `title`
- `oral_url`

## `data/processed/icml2026_paper_collaboration_features.csv`

- Rows: 6628
- Columns: 19

Columns:
- `event_id`
- `title`
- `author_count`
- `canonical_institution_count`
- `sector_mix`
- `has_industry`
- `has_academia`
- `has_research_institute`
- `has_industry_academia`
- `cluster_id`
- `cluster_label`
- `themes`
- `is_oral`
- `award`
- `public_total_votes`
- `visits_last_7_days`
- `canonical_institutions`
- `authors`
- `url`

## `data/processed/icml2026_paper_evidence_codes.csv`

- Rows: 6628
- Columns: 24
- Description: Heuristic paper-level contribution/method/evaluation/artifact evidence tags.

Columns:
- `event_id`
- `title`
- `area`
- `subarea`
- `semantic_cluster_id`
- `is_oral`
- `award`
- `public_total_votes`
- `github_url`
- `artifact_confidence`
- `primary_contribution_type`
- `contribution_types`
- `method_families`
- `evaluation_settings`
- `result_claim_types`
- `benchmark_mentions`
- `dataset_mentions`
- `metric_mentions`
- `artifact_type`
- `evidence_text_available`
- `evidence_confidence`
- `abstract`
- `url`
- `alphaxiv_url`

## `data/processed/icml2026_paper_explorer.csv`

- Rows: 6628
- Columns: 31
- Description: Compact paper-level search table for area, program, artifact, and evidence exploration.

Columns:
- `event_id`
- `title`
- `area`
- `subarea`
- `semantic_cluster_id`
- `semantic_cluster_label`
- `taxonomy_confidence`
- `review_status`
- `topic_group`
- `topic`
- `is_oral`
- `award`
- `public_total_votes`
- `visits_last_7_days`
- `github_url`
- `github_repo`
- `github_stars`
- `artifact_confidence`
- `needs_manual_check_reason`
- `primary_contribution_type`
- `method_families`
- `evaluation_settings`
- `benchmark_mentions`
- `dataset_mentions`
- `metric_mentions`
- `evidence_confidence`
- `author_count`
- `institution_count`
- `url`
- `alphaxiv_url`
- `signal_score`

## `data/processed/icml2026_paper_note_overlay_bridge.csv`

- Rows: 94
- Columns: 24
- Description: Transfer checklist from first-sprint paper notes into claim and area review overlay rows.

Columns:
- `target_type`
- `target_file`
- `overlay_key`
- `target_present`
- `event_id`
- `sprint_rank`
- `title`
- `area`
- `subarea`
- `claim_id`
- `note_status`
- `blocking_gap`
- `source_fields_to_read`
- `overlay_fields_to_update`
- `allowed_values`
- `transfer_instruction`
- `claim_implication_prompt`
- `taxonomy_question`
- `artifact_check_prompt`
- `note_claim_implications`
- `note_taxonomy_correction`
- `note_evidence_strength`
- `note_artifact_status_checked`
- `note_final_report_use`

## `data/processed/icml2026_paper_source_access_map.csv`

- Rows: 56
- Columns: 23
- Description: OpenReview, arXiv/PDF, artifact, local-context, and extraction checklist map for sprint papers.

Columns:
- `event_id`
- `sprint`
- `sprint_rank`
- `title`
- `area`
- `subarea`
- `target_claims`
- `task_focuses`
- `icml_url`
- `openreview_url`
- `alphaxiv_url`
- `arxiv_id`
- `arxiv_abs_url`
- `arxiv_pdf_url`
- `github_url`
- `source_status`
- `source_gap`
- `brief_path`
- `paper_note_file`
- `local_context`
- `required_extraction_fields`
- `pdf_review_checklist`
- `artifact_check_needed`

## `data/processed/icml2026_papers.csv`

- Rows: 6628
- Columns: 25
- Description: Authoritative ICML 2026 paper/poster table parsed from official virtual-site JSON.

Columns:
- `event_id`
- `event_type`
- `title`
- `url`
- `paper_url`
- `openreview_url`
- `decision`
- `topic`
- `topic_group`
- `topic_subtopic`
- `session`
- `starttime`
- `poster_position`
- `authors`
- `institutions`
- `author_count`
- `institution_count`
- `abstract`
- `is_position`
- `is_oral`
- `oral_event_id`
- `oral_url`
- `oral_session`
- `oral_starttime`
- `oral_decision`

## `data/processed/icml2026_pdf_extraction_probe.csv`

- Rows: 8
- Columns: 19
- Description: Bounded source-readiness probe for downloading and extracting prioritized sprint PDFs.

Columns:
- `event_id`
- `sprint`
- `sprint_rank`
- `title`
- `target_claims`
- `task_focuses`
- `arxiv_id`
- `arxiv_pdf_url`
- `local_pdf_path`
- `download_status`
- `pdf_bytes`
- `download_error`
- `extract_status`
- `page_count`
- `sample_text_chars`
- `detected_sections`
- `evidence_cue_counts`
- `extraction_error`
- `manual_review_next_step`

## `data/processed/icml2026_pdf_page_cues.csv`

- Rows: 272
- Columns: 26
- Description: Page-level section and evidence-cue counts for probed priority PDFs.

Columns:
- `event_id`
- `sprint`
- `sprint_rank`
- `title`
- `page_number`
- `text_chars`
- `section_hits`
- `section_introduction`
- `section_related_work`
- `section_method`
- `section_experiment`
- `section_result`
- `section_ablation`
- `section_limitation`
- `section_conclusion`
- `cue_baseline`
- `cue_ablation`
- `cue_dataset`
- `cue_metric`
- `cue_limitation`
- `cue_theorem`
- `cue_artifact`
- `method_score`
- `evidence_score`
- `limitation_score`
- `artifact_score`

## `data/processed/icml2026_pdf_review_cards.csv`

- Rows: 8
- Columns: 18
- Description: Page-level PDF navigation cards for the bounded priority review subset.

Columns:
- `event_id`
- `sprint`
- `sprint_rank`
- `title`
- `target_claims`
- `task_ids`
- `page_count`
- `local_pdf_path`
- `paper_note_file`
- `brief_path`
- `method_pages`
- `evidence_pages`
- `limitation_pages`
- `artifact_pages`
- `artifact_check_needed`
- `required_manual_fields`
- `review_sequence`
- `review_flags`

## `data/processed/icml2026_pdf_review_seed_area_overrides.csv`

- Rows: 8
- Columns: 14
- Description: Suggestion-only area judgments derived from the bounded eight-PDF review subset.

Columns:
- `area`
- `event_id`
- `title`
- `manual_validated_suggestion`
- `manual_primary_contribution_type_suggestion`
- `manual_method_family_seed`
- `manual_benchmarks_seed`
- `manual_datasets_seed`
- `manual_metrics_seed`
- `manual_artifact_status_suggestion`
- `manual_result_character_seed`
- `manual_fault_line_relevance_suggestion`
- `manual_notes_seed`
- `seed_status`

## `data/processed/icml2026_pdf_review_seed_claim_overrides.csv`

- Rows: 15
- Columns: 8
- Description: Suggestion-only claim judgments derived from the bounded eight-PDF review subset.

Columns:
- `claim_id`
- `event_id`
- `title`
- `manual_claim_support_suggestion`
- `manual_taxonomy_judgment_suggestion`
- `manual_artifact_judgment_suggestion`
- `manual_notes_seed`
- `seed_status`

## `data/processed/icml2026_pdf_review_seed_paper_notes.csv`

- Rows: 8
- Columns: 24
- Description: Suggestion-only paper judgments derived from the bounded eight-PDF review subset.

Columns:
- `event_id`
- `sprint`
- `sprint_rank`
- `title`
- `target_claims`
- `local_pdf_path`
- `pdf_card_path`
- `evidence_pages_checked`
- `paper_read_status_suggestion`
- `contribution_summary_seed`
- `novelty_judgment_suggestion`
- `method_summary_seed`
- `evidence_strength_suggestion`
- `baselines_checked_seed`
- `datasets_checked_seed`
- `metrics_checked_seed`
- `limitations_seed`
- `artifact_status_checked_suggestion`
- `reproducibility_notes_seed`
- `claim_implications_seed`
- `taxonomy_correction_suggestion`
- `final_report_use_suggestion`
- `reviewer_caveat`
- `seed_status`

## `data/processed/icml2026_pdf_review_transfer_checklist.csv`

- Rows: 23
- Columns: 19
- Description: Focused transfer checklist from bounded PDF worksheet rows to claim and area overlays.

Columns:
- `event_id`
- `sprint_rank`
- `title`
- `target_type`
- `overlay_key`
- `target_file`
- `target_present`
- `claim_id`
- `pdf_card_path`
- `worksheet_path`
- `paper_note_file`
- `page_pass`
- `source_fields_to_read`
- `overlay_fields_to_update`
- `allowed_values`
- `current_note_status`
- `current_blocking_gap`
- `transfer_instruction`
- `post_transfer_commands`

## `data/processed/icml2026_pdf_review_worksheet.csv`

- Rows: 8
- Columns: 41
- Description: Reviewer-ready worksheet joining PDF pages, claim tests, source links, and blank paper-note fields.

Columns:
- `event_id`
- `sprint`
- `sprint_rank`
- `title`
- `target_claims`
- `task_ids`
- `task_focuses`
- `local_pdf_path`
- `pdf_card_path`
- `brief_path`
- `paper_note_file`
- `icml_url`
- `openreview_url`
- `arxiv_pdf_url`
- `github_url`
- `method_pages`
- `evidence_pages`
- `limitation_pages`
- `artifact_pages`
- `claim_questions`
- `support_tests`
- `weakening_tests`
- `blocking_risks`
- `required_manual_fields`
- `read_order`
- `paper_read_status`
- `contribution_summary`
- `novelty_judgment`
- `method_summary`
- `evidence_strength`
- `baselines_checked`
- `datasets_checked`
- `metrics_checked`
- `limitations`
- `artifact_status_checked`
- `reproducibility_notes`
- `claim_implications`
- `taxonomy_correction`
- `representative_quote_or_result`
- `final_report_use`
- `reviewer_notes`

## `data/processed/icml2026_public_program_divergence_set.csv`

- Rows: 111
- Columns: 25
- Description: Paper-level reading set for public-attention versus oral/award program-signal divergence.

Columns:
- `category`
- `divergence_score`
- `public_vote_rank`
- `event_id`
- `title`
- `area`
- `subarea`
- `is_oral`
- `award`
- `public_total_votes`
- `visits_last_7_days`
- `github_url`
- `github_stars`
- `review_plan_rank`
- `review_phase`
- `claim_ids`
- `taxonomy_review_status`
- `evidence_confidence`
- `primary_contribution_type`
- `method_families`
- `evaluation_settings`
- `calibration_question`
- `suggested_first_check`
- `url`
- `alphaxiv_url`

## `data/processed/icml2026_reproducibility_papers.csv`

- Rows: 6628
- Columns: 20
- Description: Paper-level artifact metadata derived from AlphaXiv GitHub fields.

Columns:
- `event_id`
- `title`
- `topic_group`
- `topic`
- `themes`
- `cluster_id`
- `cluster_label`
- `audience_paths`
- `is_oral`
- `award`
- `public_total_votes`
- `visits_last_7_days`
- `github_url`
- `github_repo`
- `github_stars`
- `has_github_url`
- `artifact_confidence`
- `needs_manual_check_reason`
- `alphaxiv_url`
- `icml_url`

## `data/processed/icml2026_reproducibility_summary.csv`

- Rows: 66
- Columns: 10
- Description: Artifact availability summaries by corpus, topic, cluster, theme, and audience path.

Columns:
- `group_type`
- `group`
- `paper_count`
- `github_url_count`
- `github_url_share`
- `likely_code_count`
- `likely_code_share`
- `needs_manual_check_count`
- `total_github_stars`
- `top_artifact_papers`

## `data/processed/icml2026_research_questions_agenda.csv`

- Rows: 10
- Columns: 14
- Description: Prioritized ML-research questions with evidence, falsification tests, and first papers.

Columns:
- `question_id`
- `priority`
- `question`
- `why_it_matters`
- `current_answer_status`
- `related_claims`
- `related_areas`
- `evidence_basis`
- `safe_current_wording`
- `falsification_test`
- `baseline_check`
- `first_papers_to_read`
- `first_artifacts_to_open`
- `next_action`

## `data/processed/icml2026_researcher_action_plan.csv`

- Rows: 5
- Columns: 8
- Description: Time-budgeted plan for using the workspace from 30 minutes to a full review sprint.

Columns:
- `time_budget`
- `mode`
- `objective`
- `primary_actions`
- `artifacts_to_open`
- `expected_output`
- `stop_condition`
- `risk_if_skipped`

## `data/processed/icml2026_researcher_gap_audit.csv`

- Rows: 8
- Columns: 6
- Description: Ranked critical gaps and next actions for turning the workspace into a stronger ML landscape brief.

Columns:
- `priority`
- `gap`
- `why_it_matters`
- `current_signal`
- `recommended_artifact`
- `next_action`

## `data/processed/icml2026_researcher_readiness_audit.csv`

- Rows: 20
- Columns: 16
- Description: Claim and area readiness tiers for researcher use.

Columns:
- `audit_type`
- `id`
- `name`
- `readiness_tier`
- `researcher_use`
- `review_rows`
- `reviewed_rows`
- `remaining_rows`
- `taxonomy_review_rows`
- `low_confidence_rows`
- `program_or_award_rows`
- `github_rows`
- `primary_risk`
- `evidence_summary`
- `next_action`
- `selection_mix`

## `data/processed/icml2026_researcher_review_plan.csv`

- Rows: 224
- Columns: 33
- Description: De-duplicated ranked manual review plan across claim and area queues.

Columns:
- `global_review_rank`
- `review_priority_score`
- `review_phase`
- `priority_reason`
- `event_id`
- `title`
- `area`
- `subarea`
- `claim_ids`
- `claim_themes`
- `in_claim_queue`
- `in_area_queue`
- `claim_selection_reasons`
- `area_selection_reasons`
- `review_focus`
- `is_oral`
- `award`
- `public_total_votes`
- `github_url`
- `github_stars`
- `needs_manual_check_reason`
- `taxonomy_review_status`
- `evidence_confidence`
- `primary_contribution_type`
- `method_families`
- `evaluation_settings`
- `manual_fields_to_fill`
- `claim_packet_links`
- `claim_dossier_links`
- `area_packet_link`
- `area_briefing_link`
- `icml_url`
- `alphaxiv_url`

## `data/processed/icml2026_researcher_thesis_map.csv`

- Rows: 8
- Columns: 18
- Description: Conservative thesis hierarchy with claim roles, permitted wording, blocking checks, and first papers to read.

Columns:
- `claim_id`
- `theme`
- `thesis_role`
- `readiness_tier`
- `current_status`
- `allowed_wording`
- `statement`
- `evidence`
- `caveats`
- `review_rows`
- `reviewed_rows`
- `remaining_rows`
- `sprint_papers`
- `sprint_notes_started`
- `pre_review_bucket_mix`
- `top_papers_to_read`
- `blocking_checks`
- `next_validation`

## `data/processed/icml2026_review_decision_tasks.csv`

- Rows: 75
- Columns: 26
- Description: Paper-by-claim decision matrix for turning sprint reading into support, weakening, taxonomy, and artifact judgments.

Columns:
- `priority_rank`
- `task_id`
- `priority_score`
- `sprint`
- `sprint_rank`
- `event_id`
- `title`
- `claim_id`
- `claim_theme`
- `thesis_role`
- `claim_decision`
- `readiness_tier`
- `area`
- `subarea`
- `task_focus`
- `why_this_paper`
- `claim_question`
- `minimum_decision_needed`
- `what_to_extract`
- `support_signal`
- `weakening_signal`
- `blocking_risk`
- `required_manual_fields`
- `source_artifacts`
- `writeback_targets`
- `next_action`

## `data/processed/icml2026_review_execution_claim_actions.csv`

- Rows: 8
- Columns: 15
- Description: Claim-level next actions for executing manual review sprints.

Columns:
- `action_priority`
- `claim_id`
- `theme`
- `decision`
- `reviewed_rows`
- `minimum_reviewed_rows`
- `paper_notes_started`
- `minimum_paper_notes`
- `assigned_sprint`
- `sprint_01_papers`
- `sprint_02_papers`
- `bridge_ready`
- `missing_for_promotion`
- `next_action`
- `first_overlay_actions`

## `data/processed/icml2026_review_execution_dashboard.csv`

- Rows: 9
- Columns: 8
- Description: Operational metrics for review progress, quality gates, and claim promotion readiness.

Columns:
- `area`
- `metric`
- `current`
- `target`
- `completion_rate`
- `status`
- `next_action`
- `source`

## `data/processed/icml2026_review_sprint_01.csv`

- Rows: 40
- Columns: 24
- Description: First-sprint manual review worksheet with overlay keys and field prompts.

Columns:
- `sprint_rank`
- `event_id`
- `title`
- `review_phase`
- `area`
- `subarea`
- `claim_ids`
- `why_first`
- `claim_overlay_keys`
- `area_overlay_keys`
- `claim_fields_to_fill`
- `area_fields_to_fill`
- `review_focus`
- `claim_packet_links`
- `claim_dossier_links`
- `area_packet_link`
- `area_briefing_link`
- `signals`
- `method_families`
- `evaluation_settings`
- `abstract_excerpt`
- `icml_url`
- `alphaxiv_url`
- `github_url`

## `data/processed/icml2026_review_sprint_02.csv`

- Rows: 16
- Columns: 26
- Description: Second manual review worksheet for C04/C05 claims missing first-sprint coverage.

Columns:
- `sprint_rank`
- `global_review_rank`
- `target_claims`
- `event_id`
- `title`
- `review_phase`
- `area`
- `subarea`
- `claim_ids`
- `why_in_sprint`
- `claim_overlay_keys`
- `area_overlay_keys`
- `claim_fields_to_fill`
- `area_fields_to_fill`
- `review_focus`
- `claim_packet_links`
- `claim_dossier_links`
- `area_packet_link`
- `area_briefing_link`
- `signals`
- `method_families`
- `evaluation_settings`
- `abstract_excerpt`
- `icml_url`
- `alphaxiv_url`
- `github_url`

## `data/processed/icml2026_safe_statement_register.csv`

- Rows: 20
- Columns: 13
- Description: Allowed wording, unsafe wording, and caveats for claims and area summaries.

Columns:
- `statement_type`
- `id`
- `name`
- `wording_status`
- `risk_tier`
- `decision`
- `allowed_wording`
- `unsafe_wording`
- `required_caveat`
- `evidence_basis`
- `promotion_condition`
- `falsification_test`
- `first_artifact_to_open`

## `data/processed/icml2026_sector_collaboration_counts.csv`

- Rows: 10
- Columns: 2

Columns:
- `sector_pair`
- `institution_edge_count`

## `data/processed/icml2026_sector_counts.csv`

- Rows: 4
- Columns: 2

Columns:
- `sector`
- `paper_institution_mentions`

## `data/processed/icml2026_sector_mix_counts.csv`

- Rows: 16
- Columns: 2

Columns:
- `sector_mix`
- `paper_count`

## `data/processed/icml2026_semantic_cluster_assignments.csv`

- Rows: 6628
- Columns: 22

Columns:
- `event_id`
- `semantic_cluster_id`
- `semantic_cluster_label`
- `lexical_cluster_id`
- `lexical_cluster_label`
- `title`
- `topic`
- `topic_group`
- `themes`
- `is_oral`
- `award`
- `public_total_votes`
- `visits_last_7_days`
- `github_stars`
- `composite_score`
- `semantic_distance`
- `semantic_centrality`
- `semantic_x`
- `semantic_y`
- `attention_score`
- `url`
- `alphaxiv_url`

## `data/processed/icml2026_semantic_cluster_diagnostics.csv`

- Rows: 6
- Columns: 10

Columns:
- `k`
- `sample_silhouette_cosine`
- `min_cluster_size`
- `max_cluster_size`
- `selected_k`
- `lexical_adjusted_rand`
- `lexical_normalized_mutual_info`
- `embedding_source`
- `model_name`
- `loaded_from_cache`

## `data/processed/icml2026_semantic_cluster_summary.csv`

- Rows: 42
- Columns: 18

Columns:
- `semantic_cluster_id`
- `semantic_cluster_label`
- `paper_count`
- `share`
- `oral_count`
- `oral_rate`
- `oral_enrichment`
- `award_count`
- `total_public_votes`
- `votes_per_paper`
- `public_vote_share`
- `recent_visits_7d`
- `top_terms`
- `top_topic_groups`
- `top_themes`
- `top_lexical_clusters`
- `central_papers`
- `high_signal_papers`

## `data/processed/icml2026_semantic_vs_lexical_cluster_overlap.csv`

- Rows: 210
- Columns: 6

Columns:
- `semantic_cluster_id`
- `semantic_cluster_label`
- `lexical_cluster_id`
- `lexical_cluster_label`
- `overlap_count`
- `semantic_cluster_share`

## `data/processed/icml2026_sprint_02_overlay_bridge.csv`

- Rows: 35
- Columns: 13
- Description: Transfer checklist from sprint 02 paper notes into claim and area review overlay rows.

Columns:
- `target_type`
- `target_file`
- `overlay_key`
- `target_present`
- `event_id`
- `sprint_rank`
- `title`
- `target_claims`
- `claim_id`
- `note_status`
- `blocking_gap`
- `source_fields_to_read`
- `overlay_fields_to_update`

## `data/processed/icml2026_sprint_02_prereview_suggestions.csv`

- Rows: 16
- Columns: 12
- Description: Machine-generated paper-reading prompts for the uncovered-claim sprint.

Columns:
- `sprint_rank`
- `event_id`
- `title`
- `target_claims`
- `area`
- `subarea`
- `contribution_check`
- `evidence_to_verify`
- `taxonomy_question`
- `artifact_check_prompt`
- `suggested_note_seed`
- `abstract_basis`

## `data/processed/icml2026_sprint_prereview_suggestions.csv`

- Rows: 40
- Columns: 15
- Description: Machine-generated first-sprint paper-reading prompts from abstracts, evidence tags, and linked claims.

Columns:
- `sprint_rank`
- `event_id`
- `title`
- `area`
- `subarea`
- `claim_ids`
- `contribution_hypothesis`
- `method_hypothesis`
- `evidence_to_verify`
- `taxonomy_question`
- `claim_implication_prompt`
- `artifact_check_prompt`
- `reviewer_warning`
- `suggested_note_seed`
- `abstract_basis`

## `data/processed/icml2026_sprint_reading_briefs.csv`

- Rows: 56
- Columns: 32
- Description: Consolidated per-paper reading briefs for sprint 01 and sprint 02 manual review.

Columns:
- `sprint`
- `sprint_rank`
- `global_review_rank`
- `event_id`
- `title`
- `area`
- `subarea`
- `target_claims`
- `review_phase`
- `note_status`
- `claim_overlay_keys`
- `area_overlay_keys`
- `contribution_prompt`
- `method_prompt`
- `evidence_prompt`
- `taxonomy_prompt`
- `claim_prompt`
- `artifact_prompt`
- `reviewer_warning`
- `suggested_note_seed`
- `signals`
- `method_families`
- `evaluation_settings`
- `abstract_excerpt`
- `claim_packet_links`
- `claim_dossier_links`
- `area_packet_link`
- `area_briefing_link`
- `icml_url`
- `alphaxiv_url`
- `github_url`
- `brief_path`

## `data/processed/icml2026_taxonomy_adjudication_queue.csv`

- Rows: 21
- Columns: 24
- Description: Cluster-level queue for adjudicating unstable semantic cluster area/subarea mappings.

Columns:
- `adjudication_rank`
- `priority_score`
- `semantic_cluster_id`
- `current_area`
- `current_subarea`
- `taxonomy_confidence`
- `review_status`
- `review_notes`
- `paper_count`
- `oral_count`
- `award_count`
- `votes_per_paper`
- `queued_papers`
- `semantic_cluster_label`
- `top_terms`
- `top_topic_groups`
- `top_themes`
- `top_lexical_clusters`
- `central_papers`
- `high_signal_papers`
- `queued_papers_to_read`
- `decision_prompt`
- `allowed_decisions`
- `manual_decision_destination`

## `data/processed/icml2026_theme_counts.csv`

- Rows: 15
- Columns: 4

Columns:
- `theme`
- `count`
- `share`
- `oral_count`

## `data/processed/icml2026_theme_matrix.csv`

- Rows: 6628
- Columns: 14

Columns:
- `event_id`
- `title`
- `themes`
- `official_topic`
- `topic_group`
- `decision`
- `is_oral`
- `award`
- `public_total_votes`
- `visits_last_7_days`
- `github_stars`
- `score`
- `url`
- `alphaxiv_url`

## `data/processed/icml2026_theme_reading_map.csv`

- Rows: 180
- Columns: 12

Columns:
- `theme`
- `rank`
- `title`
- `award`
- `is_oral`
- `public_total_votes`
- `visits_last_7_days`
- `github_stars`
- `score`
- `official_topic`
- `url`
- `alphaxiv_url`

## `data/processed/icml2026_top_github_artifacts.csv`

- Rows: 50
- Columns: 20

Columns:
- `event_id`
- `title`
- `topic_group`
- `topic`
- `themes`
- `cluster_id`
- `cluster_label`
- `audience_paths`
- `is_oral`
- `award`
- `public_total_votes`
- `visits_last_7_days`
- `github_url`
- `github_repo`
- `github_stars`
- `has_github_url`
- `artifact_confidence`
- `needs_manual_check_reason`
- `alphaxiv_url`
- `icml_url`

## `data/processed/icml2026_topic_counts.csv`

- Rows: 10
- Columns: 3

Columns:
- `topic`
- `count`
- `share`

## `data/processed/manual_review_progress.csv`

- Rows: 20
- Columns: 9
- Description: Manual review completion summary by claim and by area.

Columns:
- `queue_type`
- `group`
- `review_rows`
- `reviewed_rows`
- `remaining_rows`
- `completion_rate`
- `program_or_award_rows`
- `taxonomy_review_rows`
- `github_rows`

## `data/processed/project_artifact_inventory.csv`

- Rows: 379
- Columns: 12
- Description: Machine-readable inventory of generated data, reports, figures, scripts, and docs.

Columns:
- `path`
- `kind`
- `extension`
- `size_bytes`
- `row_count`
- `column_count`
- `columns`
- `json_type`
- `top_level_count`
- `image_width`
- `image_height`
- `description`

## `data/processed/workspace_validation_checks.csv`

- Rows: 316
- Columns: 6
- Description: Machine-readable workspace validation results.

Columns:
- `check_id`
- `status`
- `severity`
- `expected`
- `actual`
- `message`
