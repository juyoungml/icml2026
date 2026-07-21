# ICML 2026 Research Questions Agenda

Prioritized questions for using the workspace as a ML researcher rather than only as an EDA artifact collection.

## Agenda

| Priority | Question | Current status | First artifacts |
| ---: | --- | --- | --- |
| 1 | Is ICML 2026 genuinely centered on LLM reasoning and post-training? | high_value_hypothesis_needs_review | reports/review_reading_briefs/62989-how-much-can-language-models-memorize.md ; reports/review_reading_briefs/61998-the-flexibility-trap-rethinking-the-value-of-arbitrary-order-in-diffus.md ; reports/review_reading_briefs/65332-maximum-likelihood-reinforcement-learning.md ; reports/review_reading_briefs/65886-reinforcement-learning-with-evolving-rubrics-for-deep-research.md |
| 2 | Are systems, efficiency, agents, and code/tool papers a coherent infrastructure shift? | high_value_hypothesis_needs_review | reports/review_reading_briefs/65901-neural-thickets-diverse-task-experts-are-dense-around-pretrained-weigh.md ; reports/review_reading_briefs/65206-paperbanana-automating-academic-illustration-for-ai-scientists.md ; reports/review_reading_briefs/66212-controlled-llm-training-on-spectral-sphere.md ; reports/review_reading_briefs/61870-mhc-manifold-constrained-hyper-connections.md |
| 3 | What does the ICML program emphasize that public attention misses? | high_value_hypothesis_needs_review | reports/review_reading_briefs/66206-to-grok-grokking-provable-grokking-in-ridge-regression.md ; reports/review_reading_briefs/60766-the-obfuscation-atlas-mapping-where-honesty-emerges-in-rlvr-with-decep.md ; reports/review_reading_briefs/67084-position-ai-ml-deepfake-research-is-misaligned-with-ai-generated-non-c.md ; reports/review_reading_briefs/67118-position-the-alignment-community-is-unintentionally-building-a-censors.md |
| 4 | Why do robotics and world-model papers attract public attention despite small corpus share? | directional_needs_spot_check | reports/review_reading_briefs/66596-from-abstraction-to-instantiation-learning-behavioral-representation-f.md ; reports/review_reading_briefs/61757-world-guidance-world-modeling-in-condition-space-for-action-generation.md ; reports/review_reading_briefs/64904-temporal-straightening-for-latent-planning.md ; reports/review_reading_briefs/65457-langforce-bayesian-decomposition-of-vision-language-action-models-via-.md |
| 5 | Is multimodal/vision really underweight at ICML 2026, or is that a baseline/classifier artifact? | high_value_hypothesis_needs_review | reports/review_reading_briefs/60542-motion-attribution-for-video-generation.md ; reports/review_reading_briefs/65954-multimodal-nested-learning-for-decoupled-and-coordinated-optimization.md ; reports/review_reading_briefs/65729-exskill-continual-learning-from-experience-and-skills-in-multimodal-ag.md ; reports/review_reading_briefs/63195-babyvision-visual-reasoning-beyond-language.md |
| 6 | Do visible artifact links correspond to runnable, reproducible work? | high_value_hypothesis_needs_review | reports/icml2026_artifact_audit_queue.md ; reports/icml2026_github_artifact_live_check.md ; reports/icml2026_reproducibility_lens.md |
| 7 | Which taxonomy boundaries could change the top-level landscape story? | high_value_hypothesis_needs_review | reports/review_reading_briefs/62989-how-much-can-language-models-memorize.md ; reports/review_reading_briefs/66206-to-grok-grokking-provable-grokking-in-ridge-regression.md ; reports/review_reading_briefs/61998-the-flexibility-trap-rethinking-the-value-of-arbitrary-order-in-diffus.md ; reports/review_reading_briefs/65901-neural-thickets-diverse-task-experts-are-dense-around-pretrained-weigh.md |
| 8 | How should arXiv trend signals be used without implying venue quality or causality? | high_value_hypothesis_needs_review | reports/icml2026_baseline_sensitivity_queue.md ; reports/arxiv_taxonomy_trends.md ; reports/historical_accepted_paper_baseline.md |
| 9 | Which area summaries are safe to use now, and which need stronger caveats? | context_or_workflow_question | reports/icml2026_safe_statement_register.md ; reports/icml2026_area_risk_register.md ; reports/icml2026_claim_risk_register.md |
| 10 | Which papers should be read first to validate or weaken the whole thesis? | high_value_hypothesis_needs_review | reports/icml2026_researcher_action_plan.md ; reports/icml2026_sprint_reading_brief_index.md ; reports/icml2026_claim_decision_board.md |

## Question Details

### Q01: Is ICML 2026 genuinely centered on LLM reasoning and post-training?

- Why it matters: This is the strongest candidate for the report's central thesis, but it is also boundary-sensitive.
- Related claims: C01
- Related areas: LLM Reasoning, Post-Training, and RLVR
- Evidence basis: 1099 taxonomy papers (16.6%); historical delta +2.9 pp; public-attention enrichment 2.03x.
- Safe current wording: Hypothesis from current metadata: LLM reasoning/post-training is the largest ICML 2026 area and is also overweight relative to nearby accepted-paper baselines.
- Falsification test: Review boundary papers and relabel any that are mainly systems, safety, or general language-model evaluation; recompute whether LLM reasoning still leads the landscape.
- Baseline check: Verify that LLM Reasoning, Post-Training, and RLVR is genuinely over-represented versus nearby accepted venues, not a classifier keyword effect.
- First papers: sprint_01 #1: How much can language models memorize? (62989) ; sprint_01 #3: The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (61998) ; sprint_01 #5: Maximum Likelihood Reinforcement Learning (65332) ; sprint_01 #10: Reinforcement Learning with Evolving Rubrics for Deep Research (65886)
- Next action: Fill first-sprint paper notes, then transfer decisions through the overlay bridge.

### Q02: Are systems, efficiency, agents, and code/tool papers a coherent infrastructure shift?

- Why it matters: The workspace shows neighboring-venue overweight signals, but a researcher needs to know whether this is one movement or several unrelated pockets.
- Related claims: C02
- Related areas: Systems and Efficient Foundation Models; Agents, Code, and Tool Use
- Evidence basis: Systems historical delta +2.1 pp, relative 1.68x; Agents historical delta +2.1 pp, relative 1.44x.
- Safe current wording: Hypothesis from current metadata: Systems/efficiency and agents/code look smaller than LLM reasoning by paper count, but both are clear ICML 2026 overweights versus the neighboring-venue baseline.
- Falsification test: Read representative systems and agents/code papers and check whether the mechanism is reusable infrastructure, benchmark packaging, or ordinary model training.
- Baseline check: Verify that Systems and Efficient Foundation Models is genuinely over-represented versus nearby accepted venues, not a classifier keyword effect.
- First papers: sprint_01 #4: Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights (65901) ; sprint_01 #6: PaperBanana: Automating Academic Illustration for AI Scientists (65206) ; sprint_01 #11: Controlled LLM Training on Spectral Sphere (66212) ; sprint_01 #15: mHC: Manifold-Constrained Hyper-Connections (61870)
- Next action: Fill first-sprint paper notes, then transfer decisions through the overlay bridge.

### Q03: What does the ICML program emphasize that public attention misses?

- Why it matters: This separates committee-visible importance from AlphaXiv visibility and helps avoid popularity-as-quality errors.
- Related claims: C03
- Related areas: Theory, Optimization, and Algorithms; Safety, Governance, Privacy, and Society
- Evidence basis: Theory oral enrichment 1.45x vs public enrichment 0.46x; Safety oral enrichment 1.41x and 3 awards vs public enrichment 0.51x.
- Safe current wording: Hypothesis from current metadata: Theory and safety/governance receive more program signal than their public-attention signal would predict.
- Falsification test: Compare low-public/high-program papers against their abstracts/PDFs and label the committee-selection rationale.
- Baseline check: Spot-check representative titles and boundary papers before using this as more than directional context.
- First papers: sprint_01 #2: To Grok Grokking: Provable Grokking in Ridge Regression (66206) ; sprint_01 #7: The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (60766) ; sprint_01 #8: Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII) (67084) ; sprint_01 #9: Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit (67118)
- Next action: Fill first-sprint paper notes, then transfer decisions through the overlay bridge.

### Q04: Why do robotics and world-model papers attract public attention despite small corpus share?

- Why it matters: This is a clear public/program mismatch and could reflect demo visibility, VLA excitement, or reusable benchmark/model work.
- Related claims: C04
- Related areas: Robotics, Embodiment, and World Models
- Evidence basis: 195 papers (2.9%); public-attention enrichment 2.11x vs oral enrichment 0.81x.
- Safe current wording: Directional signal: Robotics/embodiment is small by taxonomy count but unusually strong in public attention.
- Falsification test: Classify high-attention robotics papers as benchmark, demo, reusable model, or core algorithmic contribution and compare with oral/award status.
- Baseline check: Spot-check representative titles and boundary papers before using this as more than directional context.
- First papers: sprint_01 #20: From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model (66596) ; sprint_02 #8: World Guidance: World Modeling in Condition Space for Action Generation (61757) ; sprint_02 #9: Temporal Straightening for Latent Planning (64904) ; sprint_02 #11: LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries (65457)
- Next action: Use sprint 02 paper notes, then transfer decisions through the sprint 02 overlay bridge.

### Q05: Is multimodal/vision really underweight at ICML 2026, or is that a baseline/classifier artifact?

- Why it matters: This is the riskiest neighboring-venue contrast because arXiv growth and accepted-paper baselines point in different directions.
- Related claims: C05
- Related areas: Multimodal, Vision, and Perception
- Evidence basis: 889 taxonomy papers (13.4%); historical delta -3.1 pp, relative 0.82x.
- Safe current wording: Directional signal: Multimodal/vision is large inside ICML 2026 but underweight relative to NeurIPS 2025 and ICLR 2026 accepted-paper baselines.
- Falsification test: Break the sprint-02 multimodal/vision papers into submodes before interpreting the aggregate underweight/overweight signal.
- Baseline check: Check whether the venue-share direction and arXiv-growth direction are describing different phenomena, or whether one is an artifact of broad query terms/classifier boundaries.
- First papers: sprint_02 #1: Motion Attribution for Video Generation (60542) ; sprint_02 #2: Multimodal Nested Learning for Decoupled and Coordinated Optimization (65954) ; sprint_02 #3: ExSkill: Continual Learning from Experience and Skills in Multimodal Agents (65729) ; sprint_02 #4: BabyVision: Visual Reasoning Beyond Language (63195)
- Next action: Use sprint 02 paper notes, then transfer decisions through the sprint 02 overlay bridge.

### Q06: Do visible artifact links correspond to runnable, reproducible work?

- Why it matters: The corpus has many GitHub links, but repository visibility is not the same as reproducibility.
- Related claims: C07
- Related areas: Agents, Code, and Tool Use; LLM Reasoning, Post-Training, and RLVR; Systems and Efficient Foundation Models
- Evidence basis: Robotics, Embodiment, and World Models: GitHub URL share 38.0%; Agents, Code, and Tool Use: GitHub URL share 32.9%; LLM Reasoning, Post-Training, and RLVR: GitHub URL share 32.1%; Generative Modeling: GitHub URL share 31.1%
- Safe current wording: Directional signal: Artifacts are most visible in agents/code, LLM reasoning, systems, and multimodal/vision, while theory remains much less artifact-linked.
- Falsification test: Open linked repositories for high-signal papers and record license, release state, data/checkpoints, dependencies, and runnable example.
- Baseline check: Spot-check representative titles and boundary papers before using this as more than directional context.
- First papers: artifact #1: When RL Meets Adaptive Speculative Training:  A Unified Training-Serving System (66675) ; artifact #2: From geometry to dynamics: Learning overdamped Langevin dynamics from sparse observations with geometric constraints (60982) ; artifact #3: Process Reward Models That Think (68817) ; artifact #4: How much can language models memorize? (62989)
- Next action: Fill first-sprint paper notes, then transfer decisions through the overlay bridge.

### Q07: Which taxonomy boundaries could change the top-level landscape story?

- Why it matters: Area-ranking and subarea conclusions can be distorted by boundary clusters before manual adjudication.
- Related claims: C01; C02; C05
- Related areas: LLM Reasoning, Post-Training, and RLVR; Theory, Optimization, and Algorithms; AI for Science, Health, and Neuro
- Evidence basis: 1099 taxonomy papers (16.6%); historical delta +2.9 pp; public-attention enrichment 2.03x. ; Systems historical delta +2.1 pp, relative 1.68x; Agents historical delta +2.1 pp, relative 1.44x.
- Safe current wording: Hypothesis from current metadata: LLM reasoning/post-training is the largest ICML 2026 area and is also overweight relative to nearby accepted-paper baselines.
- Falsification test: Review boundary papers and relabel any that are mainly systems, safety, or general language-model evaluation; recompute whether LLM reasoning still leads the landscape.
- Baseline check: Verify that LLM Reasoning, Post-Training, and RLVR is genuinely over-represented versus nearby accepted venues, not a classifier keyword effect.
- First papers: sprint_01 #1: How much can language models memorize? (62989) ; sprint_01 #2: To Grok Grokking: Provable Grokking in Ridge Regression (66206) ; sprint_01 #3: The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (61998) ; sprint_01 #4: Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights (65901)
- Next action: Fill first-sprint paper notes, then transfer decisions through the overlay bridge.

### Q08: How should arXiv trend signals be used without implying venue quality or causality?

- Why it matters: Broad arXiv queries are useful context, but they are overlapping and should not become field-quality claims.
- Related claims: C06
- Related areas: Multimodal, Vision, and Perception; LLM Reasoning, Post-Training, and RLVR; Safety, Governance, Privacy, and Society
- Evidence basis: Multimodal, Vision, and Perception: 94.6%; LLM Reasoning, Post-Training, and RLVR: 59.9%; Safety, Governance, Privacy, and Society: 53.6%; Systems and Efficient Foundation Models: 43.3%
- Safe current wording: As context only: The fastest broad arXiv growth areas are multimodal/vision, LLM reasoning, and safety/governance, but ICML 2026 does not mirror this ranking exactly.
- Falsification test: Run sensitivity checks on broad query terms and accepted-paper baselines before using any trend language.
- Baseline check: Check whether the venue-share direction and arXiv-growth direction are describing different phenomena, or whether one is an artifact of broad query terms/classifier boundaries.
- First papers: sprint_01 #1: How much can language models memorize? (62989) ; sprint_01 #3: The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (61998) ; sprint_01 #4: Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights (65901) ; sprint_01 #5: Maximum Likelihood Reinforcement Learning (65332)
- Next action: Keep as framing/context; do not promote as a paper-quality claim.

### Q09: Which area summaries are safe to use now, and which need stronger caveats?

- Why it matters: A researcher needs practical wording rules before turning exploratory EDA into report or presentation language.
- Related claims: C08
- Related areas: cross_area
- Evidence basis: 21 of 42 semantic clusters are marked needs_review; validation queue contains 192 papers across 12 areas.
- Safe current wording: As context only: The biggest remaining quality jump is not more plotting; it is paper-level validation of boundary clusters and high-impact claims.
- Falsification test: Audit every report headline against reviewed rows, paper notes, acceptance criteria, and manual caveats before presentation use.
- Baseline check: not primary
- First papers: sprint_01 #1: How much can language models memorize? (62989) ; sprint_01 #2: To Grok Grokking: Provable Grokking in Ridge Regression (66206) ; sprint_01 #3: The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (61998) ; sprint_01 #5: Maximum Likelihood Reinforcement Learning (65332)
- Next action: Keep as framing/context; do not promote as a paper-quality claim.

### Q10: Which papers should be read first to validate or weaken the whole thesis?

- Why it matters: The fastest path to a stronger brief is not more plots; it is reading the papers that can move claim decisions.
- Related claims: C01; C02; C03; C04; C05; C07
- Related areas: cross_area
- Evidence basis: 1099 taxonomy papers (16.6%); historical delta +2.9 pp; public-attention enrichment 2.03x. ; Systems historical delta +2.1 pp, relative 1.68x; Agents historical delta +2.1 pp, relative 1.44x.
- Safe current wording: Hypothesis from current metadata: LLM reasoning/post-training is the largest ICML 2026 area and is also overweight relative to nearby accepted-paper baselines.
- Falsification test: Review boundary papers and relabel any that are mainly systems, safety, or general language-model evaluation; recompute whether LLM reasoning still leads the landscape.
- Baseline check: not primary
- First papers: sprint_01 #1: How much can language models memorize? (62989) ; sprint_01 #2: To Grok Grokking: Provable Grokking in Ridge Regression (66206) ; sprint_01 #3: The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (61998) ; sprint_01 #4: Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights (65901)
- Next action: Fill first-sprint paper notes, then transfer decisions through the overlay bridge.

## Outputs

- `data/processed/icml2026_research_questions_agenda.csv`
- `reports/icml2026_research_questions_agenda.md`