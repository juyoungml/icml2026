# ICML 2026 EDA Workspace

This workspace is for exploratory data analysis, research notes, and seed documents for an ICML 2026 overview report.

New to ICML 2026? Start with `docs/icml2026_newcomer_roadmap.md`. It provides friendly quick, standard, and deep learning routes, a 12-area tour, trend lessons, a small paper course, and a comprehensive quiz.

Prefer a presentation? Open `docs/icml2026_newcomer_slides.html`. It is a self-contained 47-slide technical deck with embedded figures, two slides for each research area, representative-paper deep dives, keyboard navigation, and knowledge checks.

For the full research workspace, use `docs/project_index.md` for the recommended reading order, key data products, trust levels, and generated data dictionary.

## Structure

- `data/raw/` - downloaded source HTML/JSON snapshots.
- `data/processed/` - normalized CSV/JSON tables used by analysis.
- `scripts/` - repeatable fetch, parse, and analysis scripts.
- `reports/` - markdown reports and EDA summaries.
- `docs/` - source notes, methodology, and writing seeds.
- `figures/` - generated charts.
- `notebooks/` - optional notebooks.

## Quick Start

```bash
python3 scripts/fetch_icml_virtual.py
python3 scripts/analyze_icml_titles.py
python3 scripts/fetch_alphaxiv_icml.py --all --page-size 100
python3 scripts/analyze_alphaxiv_icml.py
python3 scripts/build_researcher_landscape.py
python3 scripts/build_cluster_landscape.py
python3 scripts/build_semantic_landscape.py
python3 scripts/build_manual_taxonomy_seed.py
python3 scripts/build_taxonomy_adjudication_queue.py
python3 scripts/build_paper_evidence_codes.py
python3 scripts/build_taxonomy_fault_lines.py
python3 scripts/build_area_briefing_cards.py
python3 scripts/build_area_risk_register.py
python3 scripts/build_manual_validation_queue.py
python3 scripts/build_validation_packets.py
python3 scripts/build_program_calibration.py
python3 scripts/build_public_program_divergence_set.py
python3 scripts/fetch_arxiv_trends.py
python3 scripts/build_historical_venue_baselines.py
python3 scripts/build_baseline_sensitivity_queue.py
python3 scripts/build_collaboration_landscape.py
python3 scripts/build_audience_reading_paths.py
python3 scripts/build_reproducibility_lens.py
python3 scripts/build_artifact_audit_queue.py
python3 scripts/build_paper_explorer.py
python3 scripts/build_landscape_synthesis.py
python3 scripts/build_claim_validation_queue.py
python3 scripts/build_researcher_review_plan.py
python3 scripts/build_manual_review_workspace.py
python3 scripts/build_manual_review_codebook.py
python3 scripts/lint_manual_review_values.py
python3 scripts/build_reviewed_validation_tables.py
python3 scripts/build_review_progress.py
python3 scripts/build_researcher_readiness_audit.py
python3 scripts/build_researcher_thesis_map.py
python3 scripts/build_claim_acceptance_criteria.py
python3 scripts/build_claim_evidence_dossiers.py
python3 scripts/build_review_sprint_packet.py
python3 scripts/build_sprint_prereview_suggestions.py
python3 scripts/build_paper_note_workspace.py
python3 scripts/build_paper_note_overlay_bridge.py
python3 scripts/build_review_sprint_02_uncovered_claims.py
python3 scripts/build_sprint_reading_briefs.py
python3 scripts/build_claim_decision_board.py
python3 scripts/build_claim_risk_register.py
python3 scripts/build_safe_statement_register.py
python3 scripts/build_review_execution_dashboard.py
python3 scripts/build_researcher_action_plan.py
python3 scripts/build_research_questions_agenda.py
python3 scripts/build_review_decision_tasks.py
python3 scripts/build_paper_source_access_map.py
python3 scripts/build_pdf_extraction_probe.py --limit 8
python3 scripts/build_pdf_review_cards.py
python3 scripts/build_pdf_review_worksheet.py
python3 scripts/build_pdf_review_transfer_checklist.py
python3 scripts/build_pdf_review_seed_judgments.py
python3 scripts/build_researcher_gap_audit.py
python3 scripts/build_newcomer_slides.py
python3 scripts/build_overview_report_seed.py
python3 scripts/build_figures.py
python3 scripts/build_static_dashboard.py
python3 scripts/build_project_index.py
python3 scripts/validate_workspace.py
```

The first script downloads/parses the official ICML 2026 virtual paper list and creates:

- `data/processed/icml2026_papers.csv`
- `data/processed/icml2026_papers.json`
- `data/processed/icml2026_awards.csv`

The second script creates keyword/topic EDA outputs:

- `data/processed/icml2026_topic_counts.csv`
- `data/processed/icml2026_keyword_counts.csv`
- `reports/icml2026_title_eda.md`

The AlphaXiv scripts create a community-signal table:

- `data/processed/alphaxiv_icml2026_papers.csv`
- `data/processed/alphaxiv_icml2026_joined.csv`
- `reports/alphaxiv_icml2026_eda.md`

The researcher landscape script creates the main synthesis layer:

- `data/processed/icml2026_theme_matrix.csv`
- `data/processed/icml2026_theme_counts.csv`
- `data/processed/icml2026_institution_counts.csv`
- `data/processed/icml2026_canonical_institution_counts.csv`
- `data/processed/icml2026_sector_counts.csv`
- `data/processed/icml2026_theme_reading_map.csv`
- `reports/icml2026_researcher_landscape.md`
- `reports/icml2026_theme_reading_map.md`
- `reports/icml2026_researcher_audit.md`

The cluster landscape script creates an unsupervised map over titles, topics, and abstracts:

- `data/processed/icml2026_cluster_assignments.csv`
- `data/processed/icml2026_cluster_summary.csv`
- `data/processed/icml2026_cluster_diagnostics.csv`
- `reports/icml2026_cluster_landscape.md`
- `reports/icml2026_fault_lines_seed.md`

The semantic landscape script creates a transformer-embedding cluster map and comparison against the lexical cluster baseline:

- `data/processed/icml2026_semantic_embeddings.npy`
- `data/processed/icml2026_semantic_embeddings_metadata.json`
- `data/processed/icml2026_semantic_cluster_assignments.csv`
- `data/processed/icml2026_semantic_cluster_summary.csv`
- `data/processed/icml2026_semantic_cluster_diagnostics.csv`
- `data/processed/icml2026_semantic_vs_lexical_cluster_overlap.csv`
- `reports/icml2026_semantic_cluster_landscape.md`

The manual taxonomy seed script turns semantic clusters into curated report-level areas and review queues:

- `data/processed/icml2026_manual_taxonomy_clusters.csv`
- `data/processed/icml2026_manual_taxonomy_areas.csv`
- `data/processed/icml2026_manual_taxonomy_papers.csv`
- `reports/icml2026_manual_taxonomy_seed.md`

The taxonomy adjudication queue ranks unstable semantic clusters for human boundary review:

- `data/processed/icml2026_taxonomy_adjudication_queue.csv`
- `reports/icml2026_taxonomy_adjudication_queue.md`

The paper evidence coding script adds heuristic evidence tags for benchmarks, datasets, metrics, methods, settings, and contribution type:

- `data/processed/icml2026_paper_evidence_codes.csv`
- `data/processed/icml2026_area_evidence_summary.csv`
- `reports/icml2026_paper_evidence_codes.md`

The taxonomy fault-line script turns the curated areas into researcher-facing synthesis briefs:

- `data/processed/icml2026_area_fault_lines.csv`
- `reports/icml2026_area_fault_lines.md`

The area briefing card script creates compact per-area guides for reading and caveat tracking:

- `data/processed/icml2026_area_briefing_cards.csv`
- `reports/icml2026_area_briefing_card_index.md`
- `reports/area_briefing_cards/*.md`

The area risk register turns each area into reliability tier, falsification test, first checks, and safe language:

- `data/processed/icml2026_area_risk_register.csv`
- `reports/icml2026_area_risk_register.md`

The manual validation queue script creates a balanced review set for converting heuristic tags into checked claims:

- `data/processed/icml2026_manual_validation_queue.csv`
- `reports/icml2026_manual_validation_queue.md`

The validation packet script turns the queue into area-specific markdown review worksheets:

- `reports/icml2026_validation_packet_index.md`
- `reports/validation_packets/*.md`

The program calibration script compares taxonomy size with oral/award selection and public attention:

- `data/processed/icml2026_area_program_calibration.csv`
- `data/processed/icml2026_cluster_program_calibration.csv`
- `reports/icml2026_program_signal_calibration.md`

The public/program divergence script creates a paper-level reading set for calibrating AlphaXiv attention against oral/award signal:

- `data/processed/icml2026_public_program_divergence_set.csv`
- `reports/icml2026_public_program_divergence_set.md`

The arXiv trend script creates a cached external trend baseline by taxonomy area:

- `data/raw/arxiv_trend_counts_cache.json`
- `data/processed/arxiv_taxonomy_trend_counts.csv`
- `data/processed/arxiv_taxonomy_trend_summary.csv`
- `reports/arxiv_taxonomy_trends.md`

The historical venue baseline script compares ICML 2026 against accepted-paper corpora from nearby conferences:

- `data/raw/historical/*_orals_posters.json`
- `data/processed/historical_accepted_papers_classified.csv`
- `data/processed/historical_venue_area_summary.csv`
- `data/processed/historical_venue_delta_summary.csv`
- `reports/historical_accepted_paper_baseline.md`

The baseline sensitivity queue turns historical and arXiv context into an area-level QA checklist:

- `data/processed/icml2026_baseline_sensitivity_queue.csv`
- `reports/icml2026_baseline_sensitivity_queue.md`

The collaboration landscape script creates author-name and institution co-occurrence views:

- `data/processed/icml2026_author_counts.csv`
- `data/processed/icml2026_author_collaboration_edges.csv`
- `data/processed/icml2026_institution_collaboration.csv`
- `data/processed/icml2026_institution_collaboration_edges.csv`
- `data/processed/icml2026_paper_collaboration_features.csv`
- `data/processed/icml2026_sector_mix_counts.csv`
- `data/processed/icml2026_sector_collaboration_counts.csv`
- `reports/icml2026_collaboration_landscape.md`

The audience reading-path script creates role-specific paper tracks:

- `data/processed/icml2026_audience_reading_paths.csv`
- `reports/icml2026_audience_reading_paths.md`

The reproducibility lens script creates code/artifact availability views from AlphaXiv GitHub metadata:

- `data/processed/icml2026_reproducibility_papers.csv`
- `data/processed/icml2026_reproducibility_summary.csv`
- `data/processed/icml2026_top_github_artifacts.csv`
- `reports/icml2026_reproducibility_lens.md`

The artifact audit queue ranks papers whose artifact/repository claims need manual inspection:

- `data/processed/icml2026_artifact_audit_queue.csv`
- `reports/icml2026_artifact_audit_queue.md`

The paper explorer script creates a compact paper-level search table for the dashboard:

- `data/processed/icml2026_paper_explorer.csv`

The landscape synthesis script creates a researcher-facing signal matrix and claim register:

- `data/processed/icml2026_landscape_signal_matrix.csv`
- `data/processed/icml2026_landscape_claim_register.csv`
- `reports/icml2026_landscape_synthesis.md`

The claim validation script turns the synthesis claims into paper-level review packets:

- `data/processed/icml2026_claim_validation_queue.csv`
- `reports/icml2026_claim_validation_queue.md`
- `reports/icml2026_claim_validation_packet_index.md`
- `reports/claim_validation_packets/*.md`

The manual review workspace script creates human-editable overlay files that are preserved by default:

- `data/manual/claim_review_overrides.csv`
- `data/manual/area_review_overrides.csv`
- `reports/manual_review_workspace.md`

The reviewed validation table script merges generated queues with the manual overlays into auditable reviewed views:

- `data/processed/icml2026_claim_validation_reviewed.csv`
- `data/processed/icml2026_area_validation_reviewed.csv`
- `reports/reviewed_validation_tables.md`

The review progress script summarizes manual validation completion:

- `data/processed/manual_review_progress.csv`
- `reports/manual_review_progress.md`

The researcher readiness audit turns the claim register, validation queues, and area signals into a practical trust/risk map:

- `data/processed/icml2026_researcher_readiness_audit.csv`
- `reports/icml2026_researcher_readiness_audit.md`

The researcher thesis map turns synthesis claims into a conservative thesis hierarchy:

- `data/processed/icml2026_researcher_thesis_map.csv`
- `reports/icml2026_researcher_thesis_map.md`

The claim acceptance criteria script turns semantic validation into explicit promotion gates:

- `data/processed/icml2026_claim_acceptance_criteria.csv`
- `reports/icml2026_claim_acceptance_criteria.md`

The claim decision board combines acceptance gates, sprint coverage, and overlay transfer actions:

- `data/processed/icml2026_claim_decision_board.csv`
- `reports/icml2026_claim_decision_board.md`

The claim risk register turns each headline synthesis claim into weakest assumptions, falsification tests, and counterevidence to seek:

- `data/processed/icml2026_claim_risk_register.csv`
- `reports/icml2026_claim_risk_register.md`

The safe statement register defines what wording is currently allowed or unsafe for claims and area summaries:

- `data/processed/icml2026_safe_statement_register.csv`
- `reports/icml2026_safe_statement_register.md`

The researcher gap audit ranks what still separates the workspace from a high-confidence ML landscape brief:

- `data/processed/icml2026_researcher_gap_audit.csv`
- `reports/icml2026_researcher_gap_audit.md`

The claim evidence dossier script creates abstract/title-based pre-review aids for the synthesis claim packets:

- `data/processed/icml2026_claim_evidence_dossiers.csv`
- `reports/icml2026_claim_evidence_dossier_index.md`
- `reports/claim_evidence_dossiers/*.md`

The researcher review plan de-duplicates claim and area queues into one ranked manual-reading workflow:

- `data/processed/icml2026_researcher_review_plan.csv`
- `reports/icml2026_researcher_review_plan.md`

The review sprint packet turns the top-ranked papers into a concise worksheet for the first manual review pass:

- `data/processed/icml2026_review_sprint_01.csv`
- `reports/icml2026_review_sprint_01.md`

The sprint pre-review suggestion script creates machine-generated prompts for first-sprint paper reading:

- `data/processed/icml2026_sprint_prereview_suggestions.csv`
- `reports/icml2026_sprint_prereview_suggestions.md`

The paper-note workspace turns the first review sprint into a human-editable research note sheet:

- `data/manual/icml2026_review_sprint_01_paper_notes.csv`
- `reports/icml2026_paper_note_workspace.md`

The paper-note overlay bridge turns completed sprint notes into a transfer checklist for claim and area review overlays:

- `data/processed/icml2026_paper_note_overlay_bridge.csv`
- `reports/icml2026_paper_note_overlay_bridge.md`

The uncovered-claim sprint script creates a second review sprint for C04 and C05, which are not covered by sprint 01:

- `data/processed/icml2026_review_sprint_02.csv`
- `data/processed/icml2026_sprint_02_prereview_suggestions.csv`
- `data/manual/icml2026_review_sprint_02_paper_notes.csv`
- `data/processed/icml2026_sprint_02_overlay_bridge.csv`
- `reports/icml2026_review_sprint_02.md`
- `reports/icml2026_sprint_02_prereview_suggestions.md`
- `reports/icml2026_sprint_02_paper_note_workspace.md`
- `reports/icml2026_sprint_02_overlay_bridge.md`

The sprint reading brief script creates consolidated paper-by-paper review briefs for both manual review sprints:

- `data/processed/icml2026_sprint_reading_briefs.csv`
- `reports/icml2026_sprint_reading_brief_index.md`
- `reports/review_reading_briefs/*.md`

The manual review codebook standardizes coded values for paper notes and overlays:

- `data/processed/icml2026_manual_review_codebook.csv`
- `reports/icml2026_manual_review_codebook.md`

The manual review value linter checks non-empty coded manual fields against the codebook:

- `data/processed/icml2026_manual_review_value_lint.csv`
- `data/processed/icml2026_manual_review_value_lint_summary.csv`
- `reports/icml2026_manual_review_value_lint.md`

The review execution dashboard combines progress, lint status, sprint coverage, and claim next actions:

- `data/processed/icml2026_review_execution_dashboard.csv`
- `data/processed/icml2026_review_execution_claim_actions.csv`
- `reports/icml2026_review_execution_dashboard.md`

The researcher action plan turns the review workflow into time-budgeted execution blocks:

- `data/processed/icml2026_researcher_action_plan.csv`
- `reports/icml2026_researcher_action_plan.md`

The research questions agenda turns the workspace into prioritized ML-research questions with first readings and falsification checks:

- `data/processed/icml2026_research_questions_agenda.csv`
- `reports/icml2026_research_questions_agenda.md`

The review decision task matrix turns sprint papers into explicit paper-by-claim decisions:

- `data/processed/icml2026_review_decision_tasks.csv`
- `reports/icml2026_review_decision_tasks.md`

The paper source access map collects OpenReview, arXiv/PDF, artifact, local-context, and extraction-checklist links for sprint papers:

- `data/processed/icml2026_paper_source_access_map.csv`
- `reports/icml2026_paper_source_access_map.md`

The PDF extraction probe checks a bounded priority subset for download and text-extraction readiness:

- `data/processed/icml2026_pdf_extraction_probe.csv`
- `reports/icml2026_pdf_extraction_probe.md`
- `data/raw/pdf_probe/*.pdf`

The PDF review cards turn the probed PDFs into page-level navigation aids without storing paper prose:

- `data/processed/icml2026_pdf_review_cards.csv`
- `data/processed/icml2026_pdf_page_cues.csv`
- `reports/icml2026_pdf_review_cards.md`
- `reports/pdf_review_cards/*.md`

The PDF review worksheet joins card pages, source links, claim tests, and blank paper-note fields for the bounded priority subset:

- `data/processed/icml2026_pdf_review_worksheet.csv`
- `reports/icml2026_pdf_review_worksheet.md`

The PDF review transfer checklist maps completed worksheet rows back to canonical claim and area overlays:

- `data/processed/icml2026_pdf_review_transfer_checklist.csv`
- `reports/icml2026_pdf_review_transfer_checklist.md`

The overview report seed script creates narrative scaffolds for a report or future presentation:

- `reports/icml2026_overview_report_seed.md`
- `reports/icml2026_story_outline_seed.md`

The optional GitHub artifact validator checks a bounded set of high-signal repositories through the live GitHub API:

```bash
python3 scripts/validate_github_artifacts.py --limit 50
```

It creates:

- `data/raw/github_artifact_validation_cache.json`
- `data/processed/icml2026_github_artifact_live_check.csv`
- `reports/icml2026_github_artifact_live_check.md`

The figure script creates static visual EDA outputs:

- `figures/topic_group_distribution.png`
- `figures/theme_counts_orals.png`
- `figures/cluster_vote_density_oral_enrichment.png`
- `figures/cluster_public_vs_program_signal.png`
- `figures/alphaxiv_attention_distributions.png`
- `figures/top_canonical_institutions.png`
- `figures/sector_mix_papers.png`
- `figures/institution_collaboration_hubs.png`
- `figures/team_size_distribution.png`
- `figures/semantic_cluster_map.png`
- `figures/semantic_cluster_vote_density.png`
- `figures/manual_taxonomy_area_sizes.png`
- `figures/evidence_contribution_mix.png`
- `figures/program_signal_calibration.png`
- `figures/arxiv_taxonomy_trends.png`
- `figures/historical_venue_area_deltas.png`
- `reports/icml2026_visual_eda_index.md`

The static dashboard script creates a self-contained local HTML explorer:

- `docs/dashboard.html`

The project index script creates generated navigation and schema references:

- `docs/project_index.md`
- `docs/data_dictionary.md`
- `data/processed/project_artifact_inventory.csv`

The workspace validator checks core artifact invariants and writes a QA report:

- `data/processed/workspace_validation_checks.csv`
- `reports/workspace_validation.md`

By default, `fetch_alphaxiv_icml.py` fetches the first 10 AlphaXiv ICML feed pages. Use this only for quick iteration, because it overwrites the processed AlphaXiv table with a seed snapshot:

```bash
python3 scripts/fetch_alphaxiv_icml.py
```

Use this for a complete, slower feed pull. The current processed snapshot uses the complete pull and contains 6,628 AlphaXiv ICML rows joined to 6,628 official ICML paper rows.

```bash
python3 scripts/fetch_alphaxiv_icml.py --all --page-size 100
```

## Current Caveats

- OpenReview note queries may require challenge verification. The official ICML virtual site is the first authoritative corpus source.
- AlphaXiv vote/ranking data is fetched from `https://api.alphaxiv.org/papers/v3/icml-feed`; the checked-in processed snapshot is complete as of the recorded `snapshot_utc`, but votes and visits are time-sensitive.
- ICML data is parsed from official virtual bulk JSON. It currently normalizes one row per poster/paper and joins oral events through related-event IDs.
- Institution names now have a hand-written canonicalization layer for common universities, labs, and companies. Final lab rankings still need manual QA before publication.
- The lexical cluster map is a lightweight TF-IDF plus SVD baseline. The semantic cluster map adds transformer embeddings, but final cluster names and claims still need manual paper review.
- The manual taxonomy is a curated seed over semantic clusters. It is useful for report structure, but individual boundary clusters marked `needs_review` still require paper-level review.
- The area fault-line report is a synthesis aid grounded in taxonomy statistics and representative titles. Its claims should be tightened with manual paper reading before publication.
- Area briefing cards are compact navigation aids. They summarize where to start reading, but do not replace area validation packets or manual paper review.
- Paper evidence codes are keyword/regex based. They are useful for triage and coverage checks, but should not be treated as verified benchmark, dataset, or metric annotations.
- The manual validation queue is a review workflow artifact with blank human-validation fields. It does not mean the selected evidence has already been checked.
- Validation packets duplicate queue content into human-readable worksheets; their checkboxes are not synchronized back to CSV automatically.
- Program-signal calibration treats oral and award labels as conference-program signals, not final quality labels. Award enrichment excludes the Test of Time Award because it is not an ICML 2026 paper-row in the taxonomy.
- arXiv trend counts are broad overlapping query counts and should be treated as external context, not prior-conference deltas or quality signals.
- Historical venue deltas use accepted-paper virtual-site metadata from ICML 2025, NeurIPS 2025, and ICLR 2026. The comparison uses a shared keyword scorer rather than the ICML 2026 semantic taxonomy, and ICML 2025/NeurIPS 2025 classifications are weaker because their probed static abstract endpoints were unavailable.
- The landscape synthesis report is a claim register for prioritization. It intentionally distinguishes strong landscape claims from hypotheses requiring manual validation.
- Claim validation packets are review worksheets. Their blank manual fields do not mean the claims have been checked.
- Manual review overlays in `data/manual/` are the intended place for human judgments. Generated queues in `data/processed/` should remain reproducible.
- The researcher readiness audit is a decision aid for what can be used now versus what needs review. It is not a substitute for filling the manual validation fields.
- Claim evidence dossiers are pre-review aids generated from local titles, abstracts, and heuristic tags. They prioritize reading but do not count as manual validation.
- The researcher review plan ranks papers for manual review, but it does not itself validate any claim or evidence field.
- Review sprint packets are worksheets for entering judgments into `data/manual/`; they do not count as completed review until overlay fields are filled.
- Author collaboration uses raw author names from the official corpus. It is useful for exploration, but not identity-disambiguated.
- GitHub artifact metadata is AlphaXiv-derived. The reproducibility lens flags obvious template/index repositories, and the optional live validator checks bounded GitHub API metadata, but neither clones repos nor verifies runnable code, datasets, checkpoints, or reproduction instructions.
