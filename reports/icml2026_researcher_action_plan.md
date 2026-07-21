# ICML 2026 Researcher Action Plan

Time-budgeted execution plan for turning the current workspace into a stronger ICML 2026 research brief.

## Priority Context

- Critical claims: C01, C02, C03
- High-risk claims: C04, C05, C07
- Critical areas: LLM Reasoning, Post-Training, and RLVR, Multimodal, Vision, and Perception, Theory, Optimization, and Algorithms, AI for Science, Health, and Neuro, Data-Centric, Causal, and Federated ML, Systems and Efficient Foundation Models, Agents, Code, and Tool Use
- Public/program divergence papers queued: 111

## Time-Budgeted Plan

| Budget | Mode | Objective | Primary actions | Stop condition |
| --- | --- | --- | --- | --- |
| 30_minutes | orientation | Understand what can and cannot be safely said right now. | Read the safe statement register, review execution dashboard, and claim risk register snapshots. | Can explain why 3 claims are hypothesis-only and why no claim is headline-ready. |
| 2_hours | claim_triage | Start validating the core thesis claims without trying to review the whole corpus. | Read first briefs for critical claims: sprint_01 #1: How much can language models memorize? ; sprint_01 #2: To Grok Grokking: Provable Grokking in Ridge Regression ; sprint_01 #3: The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models ; sprint_01 #4: Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights ; sprint_01 #5: Maximum Likelihood Reinforcement Learning ; sprint_01 #6: PaperBanana: Automating Academic Illustration for AI Scientists. | At least 4 first-sprint paper notes have contribution, evidence, limitations, taxonomy, and claim-implication fields filled. |
| half_day | risk_reduction | Reduce the biggest ways the landscape could be misleading. | Adjudicate top taxonomy clusters 24, 10, 11; review high-risk areas LLM Reasoning, Post-Training, and RLVR, Multimodal, Vision, and Perception, Theory, Optimization, and Algorithms; inspect top artifact queue entries 66675, 60982, 68817. | Can state whether the top area-ranking and artifact-visibility signals survived first manual checks. |
| 1_day | claim_coverage | Cover every active claim action with at least initial paper notes. | Work through sprint 01 core claims and sprint 02 C04/C05 papers: sprint_02 #1: Motion Attribution for Video Generation ; sprint_02 #2: Multimodal Nested Learning for Decoupled and Coordinated Optimization ; sprint_02 #3: ExSkill: Continual Learning from Experience and Skills in Multimodal Agents ; sprint_02 #4: BabyVision: Visual Reasoning Beyond Language ; sprint_02 #5: Causal-JEPA: Learning World Models through Object-Level Latent Interventions ; sprint_02 #6: A Very Big Video Reasoning Suite. | Every active claim action has paper-note progress: 6 active claim actions tracked. |
| full_review_sprint | promotion_readiness | Convert notes into reviewed overlays and determine which claims can be promoted, demoted, or kept as context. | Fill overlay rows from paper-note bridges, run the value linter, rebuild reviewed tables, acceptance criteria, decision board, safe statements, and validation. | Validation stays green and manual progress moves beyond dashboard status mix {'not_started': 6, 'pass': 3}. |

## Detailed Steps

### 30_minutes: orientation

- Objective: Understand what can and cannot be safely said right now.
- Open:
  - `reports/icml2026_safe_statement_register.md`
  - `reports/icml2026_review_execution_dashboard.md`
  - `reports/icml2026_claim_risk_register.md`
- Expected output: A short list of allowed hypotheses, unsafe wording, and the first claims to review.
- Stop condition: Can explain why 3 claims are hypothesis-only and why no claim is headline-ready.
- Risk if skipped: The overview seed may be read as final prose even though all promotion gates are still closed.

### 2_hours: claim_triage

- Objective: Start validating the core thesis claims without trying to review the whole corpus.
- Open:
  - `reports/icml2026_sprint_reading_brief_index.md`
  - `data/manual/icml2026_review_sprint_01_paper_notes.csv`
- Expected output: Initial paper notes for the highest-priority sprint-01 papers and clear uncertainty notes for C01/C02/C03/C07.
- Stop condition: At least 4 first-sprint paper notes have contribution, evidence, limitations, taxonomy, and claim-implication fields filled.
- Risk if skipped: Claims remain title/abstract-derived and cannot move toward promotion.

### half_day: risk_reduction

- Objective: Reduce the biggest ways the landscape could be misleading.
- Open:
  - `reports/icml2026_area_risk_register.md`
  - `reports/icml2026_taxonomy_adjudication_queue.md`
  - `reports/icml2026_artifact_audit_queue.md`
- Expected output: Boundary decisions for top clusters, artifact notes for top repositories, and updated caveats for the riskiest areas.
- Stop condition: Can state whether the top area-ranking and artifact-visibility signals survived first manual checks.
- Risk if skipped: Area shares, subarea claims, and reproducibility language may overstate heuristic metadata.

### 1_day: claim_coverage

- Objective: Cover every active claim action with at least initial paper notes.
- Open:
  - `reports/icml2026_sprint_reading_brief_index.md`
  - `data/manual/icml2026_review_sprint_02_paper_notes.csv`
  - `reports/icml2026_claim_decision_board.md`
- Expected output: Paper-note coverage for C01/C02/C03/C04/C05/C07 and a regenerated decision board.
- Stop condition: Every active claim action has paper-note progress: 6 active claim actions tracked.
- Risk if skipped: C04/C05 remain uncovered and the report cannot responsibly discuss public/program and neighboring-venue contrasts.

### full_review_sprint: promotion_readiness

- Objective: Convert notes into reviewed overlays and determine which claims can be promoted, demoted, or kept as context.
- Open:
  - `reports/icml2026_paper_note_overlay_bridge.md`
  - `reports/icml2026_sprint_02_overlay_bridge.md`
  - `reports/icml2026_claim_acceptance_criteria.md`
- Expected output: A checked thesis map with promoted, demoted, and caveated claims plus updated safe wording.
- Stop condition: Validation stays green and manual progress moves beyond dashboard status mix {'not_started': 6, 'pass': 3}.
- Risk if skipped: Manual notes remain isolated and never update the actual claim/area evidence gates.

## Outputs

- `data/processed/icml2026_researcher_action_plan.csv`
- `reports/icml2026_researcher_action_plan.md`