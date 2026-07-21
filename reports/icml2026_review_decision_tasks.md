# ICML 2026 Review Decision Tasks

Paper-by-claim task matrix for converting sprint reading into explicit claim decisions.

This is a routing layer, not a review result. All rows still require PDF/paper inspection before any claim is promoted.

## Snapshot

- Decision tasks: 75
- Papers covered: 56
- Claims covered: 8
- Task focuses: artifact_reproducibility=6, baseline_taxonomy_sensitivity=8, boundary_check_llm_reasoning=12, infrastructure_coherence=14, program_attention_explanation=9, public_attention_calibration=8, trend_context_guardrail=8, workflow_validation=10

## Claim Coverage

| Claim | Tasks | First papers | Blocking risk |
| --- | ---: | --- | --- |
| C01 | 12 | sprint_01 #1: How much can language models memorize? ; sprint_01 #3: The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models ; sprint_01 #5: Maximum Likelihood Reinforcement Learning ; sprint_01 #10: Reinforcement Learning with Evolving Rubrics for Deep Research | Boundary papers must confirm this is LLM reasoning/post-training rather than broad LLM infrastructure spillover. |
| C02 | 14 | sprint_01 #4: Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights ; sprint_01 #6: PaperBanana: Automating Academic Illustration for AI Scientists ; sprint_01 #11: Controlled LLM Training on Spectral Sphere ; sprint_01 #15: mHC: Manifold-Constrained Hyper-Connections | Historical-delta interpretation must survive a spot check of systems and agents/code examples. |
| C03 | 9 | sprint_01 #2: To Grok Grokking: Provable Grokking in Ridge Regression ; sprint_01 #7: The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes ; sprint_01 #8: Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII) ; sprint_01 #9: Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit | Low-public/high-program papers must yield concrete technical reasons for committee attention. |
| C04 | 8 | sprint_02 #8: World Guidance: World Modeling in Condition Space for Action Generation ; sprint_02 #9: Temporal Straightening for Latent Planning ; sprint_02 #11: LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries ; sprint_02 #12: Vision-Language-Action Pretraining from Large-Scale Human Videos | High-attention robotics papers must be labeled as benchmark, demo, reusable model, or core algorithmic contribution. |
| C05 | 8 | sprint_02 #1: Motion Attribution for Video Generation ; sprint_02 #2: Multimodal Nested Learning for Decoupled and Coordinated Optimization ; sprint_02 #3: ExSkill: Continual Learning from Experience and Skills in Multimodal Agents ; sprint_02 #4: BabyVision: Visual Reasoning Beyond Language | Multimodal/vision aggregate must be broken into submodes before interpreting the neighboring-venue contrast. |
| C06 | 8 | sprint_01 #4: Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights ; sprint_01 #12: Reinforcement Learning via Self-Distillation ; sprint_01 #14: GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization ; sprint_01 #15: mHC: Manifold-Constrained Hyper-Connections | Use only as external context; do not promote to a venue-quality or acceptance trend claim. |
| C07 | 6 | sprint_01 #6: PaperBanana: Automating Academic Illustration for AI Scientists ; sprint_01 #20: From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model ; sprint_01 #27: Vision-aligned Latent Reasoning for Multi-Modal Large Language Model ; sprint_01 #28: AuTAgent: A Reinforcement Learning Framework for Tool-Augmented Audio Reasoning | Repository links must be manually inspected for runnable code, data/checkpoints, license, and stale/broken state. |
| C08 | 10 | sprint_01 #1: How much can language models memorize? ; sprint_01 #2: To Grok Grokking: Provable Grokking in Ridge Regression ; sprint_01 #3: The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models ; sprint_01 #5: Maximum Likelihood Reinforcement Learning | Keep as a process/workflow claim; acceptance means the validation workflow remains explicit and auditable. |

## First 20 Tasks

| Rank | Task | Focus | Paper | Decision needed |
| ---: | --- | --- | --- | --- |
| 1 | C01-62989 | boundary_check_llm_reasoning | How much can language models memorize? | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 2 | C03-66206 | program_attention_explanation | To Grok Grokking: Provable Grokking in Ridge Regression | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 3 | C01-61998 | boundary_check_llm_reasoning | The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 4 | C02-65901 | infrastructure_coherence | Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 5 | C01-65332 | boundary_check_llm_reasoning | Maximum Likelihood Reinforcement Learning | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 6 | C02-65206 | infrastructure_coherence | PaperBanana: Automating Academic Illustration for AI Scientists | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 7 | C03-60766 | program_attention_explanation | The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 8 | C03-67084 | program_attention_explanation | Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII) | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 9 | C03-67118 | program_attention_explanation | Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 10 | C01-65886 | boundary_check_llm_reasoning | Reinforcement Learning with Evolving Rubrics for Deep Research | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 11 | C02-66212 | infrastructure_coherence | Controlled LLM Training on Spectral Sphere | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 12 | C01-64121 | boundary_check_llm_reasoning | Reinforcement Learning via Self-Distillation | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 13 | C01-65446 | boundary_check_llm_reasoning | Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 14 | C01-63333 | boundary_check_llm_reasoning | GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 15 | C02-61870 | infrastructure_coherence | mHC: Manifold-Constrained Hyper-Connections | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 16 | C02-62943 | infrastructure_coherence | Evolution Strategies at the Hyperscale | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 17 | C02-65888 | infrastructure_coherence | Learning to Discover at Test Time | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 18 | C01-64488 | boundary_check_llm_reasoning | Agent Learning via Early Experience | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 19 | C01-64095 | boundary_check_llm_reasoning | WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| 20 | C01-61180 | boundary_check_llm_reasoning | Latent Collaboration in Multi-Agent Systems | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |

## Claim-Specific Tests

### C01: LLM reasoning center of gravity

- Support signal: Supports if the paper's main contribution is genuinely LLM reasoning, post-training, RLVR, or closely adjacent language-model capability work rather than a generic system/evaluation spillover.
- Weakening signal: Weakens if the assigned LLM reasoning/post-training label is secondary, wrong, or too broad for the paper's actual contribution.
- Required manual fields: contribution_summary ; novelty_judgment ; method_summary ; evidence_strength ; baselines_checked ; limitations ; claim_implications ; taxonomy_correction ; final_report_use ; artifact_status_checked ; reproducibility_notes
- First source artifacts: reports/review_reading_briefs/62989-how-much-can-language-models-memorize.md ; reports/claim_validation_packets/c01-llm-reasoning-center-of-gravity.md ; reports/claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md ; reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md

### C02: Infrastructure and agentic workloads

- Support signal: Supports if the paper contributes reusable infrastructure, efficiency, optimization, agent/tool/code workflow machinery, or a workload shift that is not just ordinary model training.
- Weakening signal: Weakens if the paper is mainly a narrow model result, benchmark, or theoretical claim with little infrastructure/agent relevance.
- Required manual fields: contribution_summary ; novelty_judgment ; method_summary ; evidence_strength ; baselines_checked ; limitations ; claim_implications ; taxonomy_correction ; final_report_use ; artifact_status_checked ; reproducibility_notes
- First source artifacts: reports/review_reading_briefs/65901-neural-thickets-diverse-task-experts-are-dense-around-pretrained-weigh.md ; reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md ; reports/claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md ; reports/area_briefing_cards/systems-and-efficient-foundation-models.md

### C03: Program committee attention

- Support signal: Supports if the paper gives a concrete technical reason for oral/award/program attention that is not captured by public votes alone.
- Weakening signal: Weakens if program signal appears unrelated to technical novelty, or if the paper is not actually program-ahead-of-public after inspection.
- Required manual fields: contribution_summary ; novelty_judgment ; method_summary ; evidence_strength ; baselines_checked ; limitations ; claim_implications ; taxonomy_correction ; final_report_use
- First source artifacts: reports/review_reading_briefs/66206-to-grok-grokking-provable-grokking-in-ridge-regression.md ; reports/claim_validation_packets/c03-program-committee-attention.md ; reports/claim_evidence_dossiers/c03-program-committee-attention.md ; reports/area_briefing_cards/theory-optimization-and-algorithms.md

### C04: Public attention mismatch

- Support signal: Supports if high public attention tracks robotics/world-model/VLA utility, demos, benchmarks, or reusable embodied-model work despite low area share.
- Weakening signal: Weakens if attention is driven mainly by title/project-page effects and not by substantive robotics/world-model contribution.
- Required manual fields: contribution_summary ; novelty_judgment ; method_summary ; evidence_strength ; baselines_checked ; limitations ; claim_implications ; taxonomy_correction ; final_report_use ; artifact_status_checked ; reproducibility_notes
- First source artifacts: reports/review_reading_briefs/61757-world-guidance-world-modeling-in-condition-space-for-action-generation.md ; reports/claim_validation_packets/c04-public-attention-mismatch.md ; reports/claim_evidence_dossiers/c04-public-attention-mismatch.md ; reports/area_briefing_cards/robotics-embodiment-and-world-models.md

### C05: Neighboring-venue contrast

- Support signal: Supports if the paper confirms multimodal/vision is a large but differently composed ICML area, or clarifies why neighboring-venue baselines make it look underweight.
- Weakening signal: Weakens if the paper belongs to a submode that makes the aggregate multimodal/vision comparison misleading or non-comparable.
- Required manual fields: contribution_summary ; novelty_judgment ; method_summary ; evidence_strength ; baselines_checked ; limitations ; claim_implications ; taxonomy_correction ; final_report_use
- First source artifacts: reports/review_reading_briefs/60542-motion-attribution-for-video-generation.md ; reports/claim_validation_packets/c05-neighboring-venue-contrast.md ; reports/claim_evidence_dossiers/c05-neighboring-venue-contrast.md ; reports/area_briefing_cards/multimodal-vision-and-perception.md

### C06: External trend context

- Support signal: Supports only as context if the paper illustrates why arXiv/venue trend language must be caveated; do not treat as quality evidence.
- Weakening signal: Weakens unsafe trend language if the paper shows arXiv query terms do not map cleanly to the accepted-paper taxonomy.
- Required manual fields: contribution_summary ; novelty_judgment ; method_summary ; evidence_strength ; baselines_checked ; limitations ; claim_implications ; taxonomy_correction ; final_report_use ; artifact_status_checked ; reproducibility_notes
- First source artifacts: reports/review_reading_briefs/65901-neural-thickets-diverse-task-experts-are-dense-around-pretrained-weigh.md ; reports/claim_validation_packets/c06-external-trend-context.md ; reports/claim_evidence_dossiers/c06-external-trend-context.md ; reports/area_briefing_cards/systems-and-efficient-foundation-models.md

### C07: Artifact visibility

- Support signal: Supports if the linked artifact is real and inspectable, with enough code/data/checkpoints/examples to strengthen artifact-visibility claims.
- Weakening signal: Weakens if the repository is absent, stale, non-runnable, only a project page, lacks license/data/checkpoints, or cannot reproduce the claimed result.
- Required manual fields: contribution_summary ; novelty_judgment ; method_summary ; evidence_strength ; baselines_checked ; limitations ; claim_implications ; taxonomy_correction ; final_report_use ; artifact_status_checked ; reproducibility_notes
- First source artifacts: reports/review_reading_briefs/65206-paperbanana-automating-academic-illustration-for-ai-scientists.md ; reports/claim_validation_packets/c07-artifact-visibility.md ; reports/claim_evidence_dossiers/c07-artifact-visibility.md ; reports/area_briefing_cards/agents-code-and-tool-use.md

### C08: Validation priority

- Support signal: Supports if the paper exposes a taxonomy, claim, or evidence ambiguity that validates the need for manual review gates.
- Weakening signal: Weakens workflow confidence if the paper is easy to classify and does not touch any high-risk boundary or claim ambiguity.
- Required manual fields: contribution_summary ; novelty_judgment ; method_summary ; evidence_strength ; baselines_checked ; limitations ; claim_implications ; taxonomy_correction ; final_report_use ; artifact_status_checked ; reproducibility_notes
- First source artifacts: reports/review_reading_briefs/62989-how-much-can-language-models-memorize.md ; reports/claim_validation_packets/c08-validation-priority.md ; reports/claim_evidence_dossiers/c08-validation-priority.md ; reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md

## Outputs

- `data/processed/icml2026_review_decision_tasks.csv`
- `reports/icml2026_review_decision_tasks.md`