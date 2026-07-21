# ICML 2026 Researcher Thesis Map

A claim hierarchy for turning the ICML 2026 EDA workspace into a coherent ML landscape report.
This is intentionally conservative: unreviewed claims remain thesis candidates or hypotheses, not publication-ready conclusions.

## Snapshot

- Claims mapped: 8
- Role mix: context_frame: 1, core_thesis_candidate: 3, supporting_hypothesis: 3, workflow_claim: 1
- Claim-review rows checked: 0/118
- First-sprint paper notes started across claim links: 0/59

## Recommended Thesis Hierarchy

| Claim | Role | Readiness | Allowed wording | Blocking checks |
| --- | --- | --- | --- | --- |
| `C01` LLM reasoning center of gravity | core_thesis_candidate | high_priority_unreviewed | Phrase as a landscape signal, not a settled paper-level conclusion. | 14 claim-review rows unreviewed; 12 taxonomy-boundary rows; 1 low-confidence evidence rows |
| `C02` Infrastructure and agentic workloads | core_thesis_candidate | high_priority_unreviewed | Phrase as a landscape signal, not a settled paper-level conclusion. | 14 claim-review rows unreviewed; 5 taxonomy-boundary rows; 1 low-confidence evidence rows; historical/arXiv baseline sensitivity |
| `C03` Program committee attention | core_thesis_candidate | high_priority_unreviewed | Phrase as a landscape signal, not a settled paper-level conclusion. | 14 claim-review rows unreviewed; 3 taxonomy-boundary rows; 3 low-confidence evidence rows |
| `C04` Public attention mismatch | supporting_hypothesis | directional_unreviewed | Use as a hypothesis until the linked papers and artifacts are checked. | 12 claim-review rows unreviewed; 2 low-confidence evidence rows |
| `C05` Neighboring-venue contrast | supporting_hypothesis | directional_unreviewed | Use as a hypothesis until the linked papers and artifacts are checked. | 14 claim-review rows unreviewed; 1 taxonomy-boundary rows; 1 low-confidence evidence rows; historical/arXiv baseline sensitivity |
| `C07` Artifact visibility | supporting_hypothesis | directional_unreviewed | Use as a hypothesis until the linked papers and artifacts are checked. | 16 claim-review rows unreviewed; 4 taxonomy-boundary rows; repository links need live/manual inspection |
| `C06` External trend context | context_frame | context_only_unreviewed | Frame as external context with clear source limitations. | 16 claim-review rows unreviewed; 6 taxonomy-boundary rows; 1 low-confidence evidence rows; historical/arXiv baseline sensitivity |
| `C08` Validation priority | workflow_claim | workflow_claim_unreviewed | Use to explain what remains unchecked, not as a field trend. | 18 claim-review rows unreviewed; 18 taxonomy-boundary rows; 3 low-confidence evidence rows |

## Claim Detail

### C01: LLM reasoning center of gravity

- Role: `core_thesis_candidate`
- Status: Central to the report thesis, but currently directional because manual review is empty.
- Statement: LLM reasoning/post-training is the largest ICML 2026 area and is also overweight relative to nearby accepted-paper baselines.
- Evidence: 1099 taxonomy papers (16.6%); historical delta +2.9 pp; public-attention enrichment 2.03x.
- Caveats: Area boundaries include general LLM training/evaluation and some diffusion-language papers; paper-level taxonomy still needs review.
- Review progress: 0/14 claim rows; 0/12 linked first-sprint notes started
- Pre-review bucket mix: likely_supports: 14
- Papers to read first: 1. How much can language models memorize? (62989) | 3. The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (61998) | 5. Maximum Likelihood Reinforcement Learning (65332) | 10. Reinforcement Learning with Evolving Rubrics for Deep Research (65886) | 12. Reinforcement Learning via Self-Distillation (64121)
- Next validation: Manually inspect boundary clusters 14, 21, and 24 before making subarea-level claims.
- Acceptance decision: `not_ready`

### C02: Infrastructure and agentic workloads

- Role: `core_thesis_candidate`
- Status: Central to the report thesis, but currently directional because manual review is empty.
- Statement: Systems/efficiency and agents/code look smaller than LLM reasoning by paper count, but both are clear ICML 2026 overweights versus the neighboring-venue baseline.
- Evidence: Systems historical delta +2.1 pp, relative 1.68x; Agents historical delta +2.1 pp, relative 1.44x.
- Caveats: Historical comparison uses a keyword scorer; ICML 2025 and NeurIPS 2025 lack static abstracts in the current pull.
- Review progress: 0/14 claim rows; 0/14 linked first-sprint notes started
- Pre-review bucket mix: likely_supports: 14
- Papers to read first: 4. Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights (65901) | 6. PaperBanana: Automating Academic Illustration for AI Scientists (65206) | 11. Controlled LLM Training on Spectral Sphere (66212) | 15. mHC: Manifold-Constrained Hyper-Connections (61870) | 16. Evolution Strategies at the Hyperscale (62943)
- Next validation: Read top positive-delta papers and check whether deltas reflect real venue emphasis or metadata/topic-label differences.
- Acceptance decision: `not_ready`

### C03: Program committee attention

- Role: `core_thesis_candidate`
- Status: Central to the report thesis, but currently directional because manual review is empty.
- Statement: Theory and safety/governance receive more program signal than their public-attention signal would predict.
- Evidence: Theory oral enrichment 1.45x vs public enrichment 0.46x; Safety oral enrichment 1.41x and 3 awards vs public enrichment 0.51x.
- Caveats: Oral/award counts are program signals, not full quality labels; award counts are small and volatile.
- Review progress: 0/14 claim rows; 0/9 linked first-sprint notes started
- Pre-review bucket mix: likely_supports: 14
- Papers to read first: 2. To Grok Grokking: Provable Grokking in Ridge Regression (66206) | 7. The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (60766) | 8. Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII) (67084) | 9. Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit (67118) | 22. Equivalence of Context and Parameter Updates in Modern Transformer Blocks (63048)
- Next validation: Review low-public/high-program papers to extract the technical reasons for committee interest.
- Acceptance decision: `not_ready`

### C04: Public attention mismatch

- Role: `supporting_hypothesis`
- Status: Useful as a reading lens and contrast case.
- Statement: Robotics/embodiment is small by taxonomy count but unusually strong in public attention.
- Evidence: 195 papers (2.9%); public-attention enrichment 2.11x vs oral enrichment 0.81x.
- Caveats: AlphaXiv likely overweights shareable VLA/world-model work and project-page traffic.
- Review progress: 0/12 claim rows; 0/0 linked first-sprint notes started
- Pre-review bucket mix: possible_support: 12
- Papers to read first: 81. World Guidance: World Modeling in Condition Space for Action Generation (61757) | 82. Temporal Straightening for Latent Planning (64904) | 105. LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries (65457) | 106. Vision-Language-Action Pretraining from Large-Scale Human Videos (62813) | 107. From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models (63621)
- Next validation: Inspect whether the high-attention papers are benchmarks, demos, or reusable models rather than core ICML program emphasis.
- Acceptance decision: `not_ready`

### C05: Neighboring-venue contrast

- Role: `supporting_hypothesis`
- Status: Useful as a reading lens and contrast case.
- Statement: Multimodal/vision is large inside ICML 2026 but underweight relative to NeurIPS 2025 and ICLR 2026 accepted-paper baselines.
- Evidence: 889 taxonomy papers (13.4%); historical delta -3.1 pp, relative 0.82x.
- Caveats: This is the area most sensitive to venue scope and title/topic classification; ICLR/NeurIPS vision-heavy shares may dominate the baseline average.
- Review progress: 0/14 claim rows; 0/0 linked first-sprint notes started
- Pre-review bucket mix: possible_support: 14
- Papers to read first: 58. Motion Attribution for Video Generation (60542) | 59. Multimodal Nested Learning for Decoupled and Coordinated Optimization (65954) | 74. ExSkill: Continual Learning from Experience and Skills in Multimodal Agents (65729) | 75. BabyVision: Visual Reasoning Beyond Language (63195) | 76. Causal-JEPA: Learning World Models through Object-Level Latent Interventions (63623)
- Next validation: Break multimodal into vision-language reasoning, video, 3D, and robustness before interpreting the aggregate underweight.
- Acceptance decision: `not_ready`

### C07: Artifact visibility

- Role: `supporting_hypothesis`
- Status: Useful as a reading lens and contrast case.
- Statement: Artifacts are most visible in agents/code, LLM reasoning, systems, and multimodal/vision, while theory remains much less artifact-linked.
- Evidence: Robotics, Embodiment, and World Models: GitHub URL share 38.0%; Agents, Code, and Tool Use: GitHub URL share 32.9%; LLM Reasoning, Post-Training, and RLVR: GitHub URL share 32.1%; Generative Modeling: GitHub URL share 31.1%
- Caveats: GitHub metadata comes from AlphaXiv and does not prove runnable reproduction; some high-star links are templates or index repos.
- Review progress: 0/16 claim rows; 0/6 linked first-sprint notes started
- Pre-review bucket mix: high_risk_artifact: 12; high_visibility_artifact: 4
- Papers to read first: 6. PaperBanana: Automating Academic Illustration for AI Scientists (65206) | 20. From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model (66596) | 27. Vision-aligned Latent Reasoning for Multi-Modal Large Language Model (61382) | 28. AuTAgent: A Reinforcement Learning Framework for Tool-Augmented Audio Reasoning (64128) | 29. Autoregressive Direct Preference Optimization (65423)
- Next validation: Clone/check high-signal repositories and separate code, benchmark, dataset, checkpoint, and project-page links.
- Acceptance decision: `not_ready`

### C06: External trend context

- Role: `context_frame`
- Status: Useful background context, not a headline claim.
- Statement: The fastest broad arXiv growth areas are multimodal/vision, LLM reasoning, and safety/governance, but ICML 2026 does not mirror this ranking exactly.
- Evidence: Multimodal, Vision, and Perception: 94.6%; LLM Reasoning, Post-Training, and RLVR: 59.9%; Safety, Governance, Privacy, and Society: 53.6%; Systems and Efficient Foundation Models: 43.3%
- Caveats: arXiv queries are broad, overlapping, and not acceptance or quality signals.
- Review progress: 0/16 claim rows; 0/8 linked first-sprint notes started
- Pre-review bucket mix: possible_support: 14; unclear: 2
- Papers to read first: 4. Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights (65901) | 12. Reinforcement Learning via Self-Distillation (64121) | 14. GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (63333) | 15. mHC: Manifold-Constrained Hyper-Connections (61870) | 16. Evolution Strategies at the Hyperscale (62943)
- Next validation: Use accepted-paper corpora, not arXiv counts, for publication-ready year-over-year venue claims.
- Acceptance decision: `context_or_workflow_only`

### C08: Validation priority

- Role: `workflow_claim`
- Status: Describes the project validation workflow.
- Statement: The biggest remaining quality jump is not more plotting; it is paper-level validation of boundary clusters and high-impact claims.
- Evidence: 21 of 42 semantic clusters are marked needs_review; validation queue contains 192 papers across 12 areas.
- Caveats: The queue organizes review but does not mean evidence fields have been checked.
- Review progress: 0/18 claim rows; 0/10 linked first-sprint notes started
- Pre-review bucket mix: unclear: 17; possible_support: 1
- Papers to read first: 1. How much can language models memorize? (62989) | 2. To Grok Grokking: Provable Grokking in Ridge Regression (66206) | 3. The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (61998) | 5. Maximum Likelihood Reinforcement Learning (65332) | 10. Reinforcement Learning with Evolving Rubrics for Deep Research (65886)
- Next validation: Fill validation packets and reconcile reviewed fields back into a checked CSV.
- Acceptance decision: `context_or_workflow_only`

## How To Use This Map

- Lead with `core_thesis_candidate` claims only as directional signals until their paper rows are reviewed.
- Use `supporting_hypothesis` claims to structure reading, not to make final assertions.
- Keep `context_frame` and `workflow_claim` rows out of headline result slides.
- Promote claims only after reviewed rows and paper notes support the exact wording.
- Use `reports/icml2026_claim_acceptance_criteria.md` as the promotion gate before editing the overview seed.

## Outputs

- `data/processed/icml2026_researcher_thesis_map.csv`
- `reports/icml2026_researcher_thesis_map.md`