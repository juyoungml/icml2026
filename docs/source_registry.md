# Source Registry

Last updated: 2026-07-14.

## Official ICML

| Source | URL | Use | Reliability | Notes |
|---|---|---|---|---|
| ICML 2026 conference page | https://icml.cc/Conferences/2026 | Dates, venue, top-level conference metadata | High | Official conference source. |
| ICML 2026 Call for Papers | https://icml.cc/Conferences/2026/CallForPapers | Submission deadlines, review policy, policy changes | High | Official policy source. |
| ICML 2026 virtual papers | https://icml.cc/virtual/2026/papers.html | Public paper title/link corpus | High | Current parser uses noscript fallback links. |
| ICML 2026 awards blog | https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/ | Award papers, selection process, summaries | High | Official ICML blog. |
| OpenReview venue group | https://openreview.net/group?id=ICML.cc/2026/Conference | Venue metadata, review workflow fields | High | Notes API may be challenge-gated. |

## Historical Venue Baselines

| Source | URL | Use | Reliability | Notes |
|---|---|---|---|---|
| ICML 2025 virtual JSON | https://icml.cc/static/virtual/data/icml-2025-orals-posters.json | Accepted-paper baseline for ICML 2025 | High | Official virtual-site data. Static abstract endpoint was unavailable during the current pull. |
| NeurIPS 2025 virtual JSON | https://neurips.cc/static/virtual/data/neurips-2025-orals-posters.json | Accepted-paper baseline for NeurIPS 2025 | High | Official virtual-site data. Static abstract endpoint was unavailable during the current pull. |
| ICLR 2026 virtual JSON | https://iclr.cc/static/virtual/data/iclr-2026-orals-posters.json | Accepted-paper baseline for ICLR 2026 | High | Official virtual-site data. Joined with static abstracts where available. |
| ICLR 2026 abstracts JSON | https://iclr.cc/static/virtual/data/iclr-2026-abstracts.json | Abstract text for ICLR 2026 baseline classification | High | Official virtual-site data. |

## Community Signals

| Source | URL | Use | Reliability | Notes |
|---|---|---|---|---|
| AlphaXiv | https://www.alphaxiv.org/ | Vote/discussion/trending signal | Medium | Treat as public attention, not quality. Endpoint/scrape still to be finalized. |

## Derived Outputs

| Output | Producer | Description |
|---|---|---|
| `data/processed/icml2026_papers.csv` | `scripts/fetch_icml_virtual.py` | Paper/event links and titles from official ICML virtual list. |
| `data/processed/icml2026_awards.csv` | `scripts/fetch_icml_virtual.py` | Seed award table from official awards page. |
| `reports/icml2026_title_eda.md` | `scripts/analyze_icml_titles.py` | Title-level EDA and trend notes. |
| `data/processed/historical_accepted_papers_classified.csv` | `scripts/build_historical_venue_baselines.py` | ICML 2026 plus nearby accepted-paper corpora classified into the shared 12-area taxonomy with a keyword scorer. |
| `data/processed/historical_venue_delta_summary.csv` | `scripts/build_historical_venue_baselines.py` | ICML 2026 area-share deltas against ICML 2025, NeurIPS 2025, and ICLR 2026 accepted-paper baselines. |
| `reports/historical_accepted_paper_baseline.md` | `scripts/build_historical_venue_baselines.py` | Report summarizing source coverage, classification health, venue shares, and largest deltas. |
| `data/processed/icml2026_baseline_sensitivity_queue.csv` | `scripts/build_baseline_sensitivity_queue.py` | Area-level spot-check queue for using historical accepted-paper baselines and broad arXiv trends responsibly. |
| `reports/icml2026_baseline_sensitivity_queue.md` | `scripts/build_baseline_sensitivity_queue.py` | Report summarizing baseline-risk tiers, check questions, and safe language for venue/arXiv trend claims. |
| `data/processed/icml2026_landscape_signal_matrix.csv` | `scripts/build_landscape_synthesis.py` | Area-level synthesis table combining taxonomy size, program signal, public attention, arXiv growth, historical deltas, and artifact visibility. |
| `data/processed/icml2026_landscape_claim_register.csv` | `scripts/build_landscape_synthesis.py` | Claim register separating strong landscape claims from hypotheses and validation tasks. |
| `reports/icml2026_landscape_synthesis.md` | `scripts/build_landscape_synthesis.py` | Researcher-facing synthesis report for orienting before deeper area reports. |
| `data/processed/icml2026_paper_explorer.csv` | `scripts/build_paper_explorer.py` | Compact paper-level search table for title/area/subarea/program/artifact/evidence exploration. |
| `data/processed/icml2026_area_briefing_cards.csv` | `scripts/build_area_briefing_cards.py` | Per-area briefing-card summaries with trust tiers, reading starts, public/program divergence, and caveats. |
| `reports/icml2026_area_briefing_card_index.md` | `scripts/build_area_briefing_cards.py` | Index of compact area briefing cards. |
| `reports/area_briefing_cards/*.md` | `scripts/build_area_briefing_cards.py` | One markdown briefing card per curated taxonomy area. |
| `data/processed/icml2026_area_risk_register.csv` | `scripts/build_area_risk_register.py` | Area-level reliability, falsification, and safe-language register. |
| `reports/icml2026_area_risk_register.md` | `scripts/build_area_risk_register.py` | Human-readable register for which area summaries are safe to use and which need more review. |
| `data/processed/icml2026_taxonomy_adjudication_queue.csv` | `scripts/build_taxonomy_adjudication_queue.py` | Cluster-level queue for adjudicating unstable semantic cluster to area/subarea mappings. |
| `reports/icml2026_taxonomy_adjudication_queue.md` | `scripts/build_taxonomy_adjudication_queue.py` | Human-readable taxonomy boundary adjudication guide. |
| `data/processed/icml2026_public_program_divergence_set.csv` | `scripts/build_public_program_divergence_set.py` | Paper-level reading set for calibrating AlphaXiv public attention against ICML oral/award program signal. |
| `reports/icml2026_public_program_divergence_set.md` | `scripts/build_public_program_divergence_set.py` | Human-readable public/program divergence reading set and calibration questions. |
| `data/processed/icml2026_artifact_audit_queue.csv` | `scripts/build_artifact_audit_queue.py` | Paper-level queue for checking whether artifact links support reproducibility claims. |
| `reports/icml2026_artifact_audit_queue.md` | `scripts/build_artifact_audit_queue.py` | Human-readable artifact audit queue with required manual checks. |
| `data/processed/icml2026_claim_validation_queue.csv` | `scripts/build_claim_validation_queue.py` | Paper-level queue for checking whether synthesis claims are supported, weakened, or need taxonomy/artifact correction. |
| `reports/icml2026_claim_validation_packet_index.md` | `scripts/build_claim_validation_queue.py` | Index of claim-specific validation worksheets. |
| `reports/claim_validation_packets/*.md` | `scripts/build_claim_validation_queue.py` | Claim-specific paper review packets with abstracts, evidence tags, and manual checklists. |
| `data/manual/claim_review_overrides.csv` | `scripts/build_manual_review_workspace.py` | Human-editable claim review overlay; preserved unless regenerated with `--force`. |
| `data/manual/area_review_overrides.csv` | `scripts/build_manual_review_workspace.py` | Human-editable area review overlay; preserved unless regenerated with `--force`. |
| `reports/manual_review_workspace.md` | `scripts/build_manual_review_workspace.py` | Instructions for filling manual review overlays and rebuilding progress/readiness outputs. |
| `data/processed/icml2026_claim_validation_reviewed.csv` | `scripts/build_reviewed_validation_tables.py` | Claim validation queue merged with human review overlay fields and reviewed flags. |
| `data/processed/icml2026_area_validation_reviewed.csv` | `scripts/build_reviewed_validation_tables.py` | Area validation queue merged with human review overlay fields and reviewed flags. |
| `reports/reviewed_validation_tables.md` | `scripts/build_reviewed_validation_tables.py` | Report describing reviewed-table inputs, outputs, and current reviewed counts. |
| `data/processed/manual_review_progress.csv` | `scripts/build_review_progress.py` | Manual review completion summary by claim and by area. |
| `reports/manual_review_progress.md` | `scripts/build_review_progress.py` | Human-readable review progress report and recommended review order. |
| `data/processed/icml2026_researcher_readiness_audit.csv` | `scripts/build_researcher_readiness_audit.py` | Claim and area readiness tiers for deciding what is directional, fragile, or publication-ready. |
| `reports/icml2026_researcher_readiness_audit.md` | `scripts/build_researcher_readiness_audit.py` | Researcher-facing trust/risk map across synthesis claims, area signals, and evidence streams. |
| `data/processed/icml2026_researcher_thesis_map.csv` | `scripts/build_researcher_thesis_map.py` | Conservative thesis hierarchy with claim roles, permitted wording, blocking checks, and first papers to read. |
| `reports/icml2026_researcher_thesis_map.md` | `scripts/build_researcher_thesis_map.py` | Researcher-facing thesis map for turning claims into report structure. |
| `data/processed/icml2026_claim_acceptance_criteria.csv` | `scripts/build_claim_acceptance_criteria.py` | Explicit promotion gates for every synthesis claim using reviewed rows, paper notes, taxonomy checks, and artifact checks. |
| `reports/icml2026_claim_acceptance_criteria.md` | `scripts/build_claim_acceptance_criteria.py` | Human-readable claim acceptance criteria and current promotion decisions. |
| `data/processed/icml2026_claim_decision_board.csv` | `scripts/build_claim_decision_board.py` | Claim-level operating board combining acceptance gates, sprint coverage, and overlay transfer actions. |
| `reports/icml2026_claim_decision_board.md` | `scripts/build_claim_decision_board.py` | Human-readable board for deciding what claims can be used now and what review action unlocks them. |
| `data/processed/icml2026_claim_risk_register.csv` | `scripts/build_claim_risk_register.py` | Falsification-oriented risk register for headline synthesis claims. |
| `reports/icml2026_claim_risk_register.md` | `scripts/build_claim_risk_register.py` | Human-readable weakest-assumption, falsification-test, and counterevidence register for each claim. |
| `data/processed/icml2026_safe_statement_register.csv` | `scripts/build_safe_statement_register.py` | Allowed wording, unsafe wording, and required caveats for claims and area summaries. |
| `reports/icml2026_safe_statement_register.md` | `scripts/build_safe_statement_register.py` | Human-readable wording guardrail for reports, memos, and presentation drafts. |
| `data/processed/icml2026_review_execution_dashboard.csv` | `scripts/build_review_execution_dashboard.py` | Operational metrics for review progress, quality gates, and claim promotion readiness. |
| `data/processed/icml2026_review_execution_claim_actions.csv` | `scripts/build_review_execution_dashboard.py` | Claim-level next actions for executing manual review sprints. |
| `reports/icml2026_review_execution_dashboard.md` | `scripts/build_review_execution_dashboard.py` | Human-readable execution dashboard for manual review and claim promotion workflow. |
| `data/processed/icml2026_researcher_action_plan.csv` | `scripts/build_researcher_action_plan.py` | Time-budgeted plan for using the workspace from 30 minutes to a full review sprint. |
| `reports/icml2026_researcher_action_plan.md` | `scripts/build_researcher_action_plan.py` | Human-readable action plan with objectives, artifacts, expected outputs, and stop conditions. |
| `data/processed/icml2026_research_questions_agenda.csv` | `scripts/build_research_questions_agenda.py` | Prioritized ML-research questions with evidence, falsification tests, and first papers. |
| `reports/icml2026_research_questions_agenda.md` | `scripts/build_research_questions_agenda.py` | Human-readable research agenda for understanding the ICML 2026 landscape. |
| `data/processed/icml2026_review_decision_tasks.csv` | `scripts/build_review_decision_tasks.py` | Paper-by-claim decision matrix for turning sprint reading into support, weakening, taxonomy, and artifact judgments. |
| `reports/icml2026_review_decision_tasks.md` | `scripts/build_review_decision_tasks.py` | Human-readable review decision task matrix for PDF reading and overlay writeback. |
| `data/processed/icml2026_paper_source_access_map.csv` | `scripts/build_paper_source_access_map.py` | OpenReview, arXiv/PDF, artifact, local-context, and extraction checklist map for sprint papers. |
| `reports/icml2026_paper_source_access_map.md` | `scripts/build_paper_source_access_map.py` | Human-readable source-access and source-gap queue for sprint paper review. |
| `data/processed/icml2026_pdf_extraction_probe.csv` | `scripts/build_pdf_extraction_probe.py` | Bounded source-readiness probe for downloading and extracting prioritized sprint PDFs. |
| `reports/icml2026_pdf_extraction_probe.md` | `scripts/build_pdf_extraction_probe.py` | Human-readable PDF extraction readiness report for the priority review subset. |
| `data/processed/icml2026_pdf_review_cards.csv` | `scripts/build_pdf_review_cards.py` | Page-level PDF navigation cards for the bounded priority review subset. |
| `data/processed/icml2026_pdf_page_cues.csv` | `scripts/build_pdf_review_cards.py` | Page-level section and evidence-cue counts for probed priority PDFs. |
| `reports/icml2026_pdf_review_cards.md` | `scripts/build_pdf_review_cards.py` | Human-readable index of PDF review navigation cards. |
| `reports/pdf_review_cards/*.md` | `scripts/build_pdf_review_cards.py` | Per-paper page-level navigation cards for PDF review. |
| `data/processed/icml2026_pdf_review_worksheet.csv` | `scripts/build_pdf_review_worksheet.py` | Reviewer-ready worksheet joining PDF pages, claim tests, source links, and blank paper-note fields. |
| `reports/icml2026_pdf_review_worksheet.md` | `scripts/build_pdf_review_worksheet.py` | Human-readable PDF review worksheet for the bounded priority subset. |
| `data/processed/icml2026_pdf_review_transfer_checklist.csv` | `scripts/build_pdf_review_transfer_checklist.py` | Focused transfer checklist from bounded PDF worksheet rows to claim and area overlays. |
| `reports/icml2026_pdf_review_transfer_checklist.md` | `scripts/build_pdf_review_transfer_checklist.py` | Human-readable transfer checklist for moving PDF worksheet judgments into overlays. |
| `data/processed/icml2026_researcher_gap_audit.csv` | `scripts/build_researcher_gap_audit.py` | Ranked critical gaps between the current workspace and a high-confidence ML landscape brief. |
| `reports/icml2026_researcher_gap_audit.md` | `scripts/build_researcher_gap_audit.py` | Researcher-facing critical feedback and next-action map for improving the workspace. |
| `data/processed/icml2026_claim_evidence_dossiers.csv` | `scripts/build_claim_evidence_dossiers.py` | Paper-level pre-review buckets, rationales, and abstract excerpts for synthesis-claim review. |
| `reports/icml2026_claim_evidence_dossier_index.md` | `scripts/build_claim_evidence_dossiers.py` | Index of claim evidence dossiers for accelerating manual review. |
| `reports/claim_evidence_dossiers/*.md` | `scripts/build_claim_evidence_dossiers.py` | Claim-level abstract/title evidence dossiers with paper-level triage tables and excerpts. |
| `data/processed/icml2026_researcher_review_plan.csv` | `scripts/build_researcher_review_plan.py` | De-duplicated ranked manual review plan across claim and area validation queues. |
| `reports/icml2026_researcher_review_plan.md` | `scripts/build_researcher_review_plan.py` | Human-readable review sprint plan with first papers, phase guide, and coverage tables. |
| `data/processed/icml2026_review_sprint_01.csv` | `scripts/build_review_sprint_packet.py` | Top-ranked first-sprint review worksheet with overlay keys and field prompts. |
| `reports/icml2026_review_sprint_01.md` | `scripts/build_review_sprint_packet.py` | Human-readable first-sprint packet for the top review-plan papers. |
| `data/processed/icml2026_sprint_prereview_suggestions.csv` | `scripts/build_sprint_prereview_suggestions.py` | Machine-generated first-sprint reading prompts from titles, abstracts, evidence tags, claim links, and artifact signals. |
| `reports/icml2026_sprint_prereview_suggestions.md` | `scripts/build_sprint_prereview_suggestions.py` | Human-readable pre-review prompts for accelerating first-sprint paper notes. |
| `data/manual/icml2026_review_sprint_01_paper_notes.csv` | `scripts/build_paper_note_workspace.py` | Human-editable top-40 paper-note sheet for novelty, method, evidence, limitations, artifact checks, and final report use. |
| `reports/icml2026_paper_note_workspace.md` | `scripts/build_paper_note_workspace.py` | Instructions for filling the first-sprint paper-note workspace and propagating judgments into overlays. |
| `data/processed/icml2026_manual_review_codebook.csv` | `scripts/build_manual_review_codebook.py` | Canonical coded values and transfer rules for paper notes and manual overlays. |
| `reports/icml2026_manual_review_codebook.md` | `scripts/build_manual_review_codebook.py` | Human-readable manual review codebook for consistent paper-note and overlay decisions. |
| `data/processed/icml2026_manual_review_value_lint.csv` | `scripts/lint_manual_review_values.py` | Invalid non-empty coded manual review values found against the codebook. |
| `data/processed/icml2026_manual_review_value_lint_summary.csv` | `scripts/lint_manual_review_values.py` | Per-file manual coded-value lint summary. |
| `reports/icml2026_manual_review_value_lint.md` | `scripts/lint_manual_review_values.py` | Human-readable manual review value lint report. |
| `data/processed/icml2026_paper_note_overlay_bridge.csv` | `scripts/build_paper_note_overlay_bridge.py` | Transfer checklist from first-sprint paper notes into claim and area review overlay rows. |
| `reports/icml2026_paper_note_overlay_bridge.md` | `scripts/build_paper_note_overlay_bridge.py` | Human-readable checklist for moving completed paper-note decisions into overlay files. |
| `data/processed/icml2026_review_sprint_02.csv` | `scripts/build_review_sprint_02_uncovered_claims.py` | Second review sprint for C04/C05 claims missing first-sprint coverage. |
| `data/processed/icml2026_sprint_02_prereview_suggestions.csv` | `scripts/build_review_sprint_02_uncovered_claims.py` | Machine-generated paper-reading prompts for sprint 02. |
| `data/manual/icml2026_review_sprint_02_paper_notes.csv` | `scripts/build_review_sprint_02_uncovered_claims.py` | Human-editable sprint 02 paper-note sheet for uncovered claims. |
| `data/processed/icml2026_sprint_02_overlay_bridge.csv` | `scripts/build_review_sprint_02_uncovered_claims.py` | Transfer checklist from sprint 02 paper notes into claim and area review overlay rows. |
| `reports/icml2026_review_sprint_02.md` | `scripts/build_review_sprint_02_uncovered_claims.py` | Human-readable second sprint packet for uncovered claims. |
| `reports/icml2026_sprint_02_prereview_suggestions.md` | `scripts/build_review_sprint_02_uncovered_claims.py` | Human-readable pre-review prompts for sprint 02. |
| `reports/icml2026_sprint_02_paper_note_workspace.md` | `scripts/build_review_sprint_02_uncovered_claims.py` | Instructions and pointers for filling sprint 02 paper notes. |
| `reports/icml2026_sprint_02_overlay_bridge.md` | `scripts/build_review_sprint_02_uncovered_claims.py` | Human-readable sprint 02 transfer checklist summary. |
| `data/processed/icml2026_sprint_reading_briefs.csv` | `scripts/build_sprint_reading_briefs.py` | Consolidated per-paper reading briefs for sprint 01 and sprint 02 manual review. |
| `reports/icml2026_sprint_reading_brief_index.md` | `scripts/build_sprint_reading_briefs.py` | Index of paper-by-paper reading briefs for executing the manual review sprints. |
| `reports/review_reading_briefs/*.md` | `scripts/build_sprint_reading_briefs.py` | Individual paper reading briefs with claim context, prompts, overlay keys, and links. |
| `reports/icml2026_overview_report_seed.md` | `scripts/build_overview_report_seed.py` | Long-form report scaffold with thesis, claims, evidence, figures, caveats, and validation hooks. |
| `reports/icml2026_story_outline_seed.md` | `scripts/build_overview_report_seed.py` | Compact narrative/story outline for a future briefing or presentation. |
| `docs/dashboard.html` | `scripts/build_static_dashboard.py` | Self-contained static dashboard for scanning area signals, paper search, claims, figures, and validation queue examples. |
| `data/processed/project_artifact_inventory.csv` | `scripts/build_project_index.py` | Machine-readable inventory of processed data, reports, figures, scripts, and docs. |
| `docs/project_index.md` | `scripts/build_project_index.py` | Generated reading-order guide and front door for the project. |
| `docs/data_dictionary.md` | `scripts/build_project_index.py` | Generated row counts and schemas for processed CSV files. |
| `data/processed/workspace_validation_checks.csv` | `scripts/validate_workspace.py` | Machine-readable validation results for core workspace invariants. |
| `reports/workspace_validation.md` | `scripts/validate_workspace.py` | Human-readable validation report for corpus counts, joins, packets, figures, and generated indexes. |
