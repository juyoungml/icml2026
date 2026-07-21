# ICML 2026 Claim Risk Register

Falsification-oriented register for the headline synthesis claims.
Use this before promoting any claim into the overview report or presentation.

## Snapshot

- Claims tracked: 8
- Risk tiers: critical: 3, high: 3, process: 2
- Decisions: not_ready: 6, context_or_workflow_only: 2

## Risk Register

| Claim | Risk | Decision | Weakest assumption | Falsification test | First papers |
| --- | --- | --- | --- | --- | --- |
| `C01` LLM reasoning center of gravity | critical | not_ready | The large LLM/post-training area is not inflated by broad LLM infrastructure, generic evaluation, or diffusion-language boundary papers. | Review boundary papers and relabel any that are mainly systems, safety, or general language-model evaluation; recompute whether LLM reasoning still leads the landscape. | sprint_01 #1: How much can language models memorize? (62989) ; sprint_01 #3: The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (61998) ; sprint_01 #5: Maximum Likelihood Reinforcement Learning (65332) ; sprint_01 #10: Reinforcement Learning with Evolving Rubrics for Deep Research (65886) |
| `C02` Infrastructure and agentic workloads | critical | not_ready | Systems, agents, and code/tool-use papers form a coherent infrastructure shift rather than several unrelated pockets. | Read representative systems and agents/code papers and check whether the mechanism is reusable infrastructure, benchmark packaging, or ordinary model training. | sprint_01 #4: Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights (65901) ; sprint_01 #6: PaperBanana: Automating Academic Illustration for AI Scientists (65206) ; sprint_01 #11: Controlled LLM Training on Spectral Sphere (66212) ; sprint_01 #15: mHC: Manifold-Constrained Hyper-Connections (61870) |
| `C03` Program committee attention | critical | not_ready | Oral/award selection reflects concrete technical or conceptual importance, not just position-paper salience or topic timeliness. | Compare low-public/high-program papers against their abstracts/PDFs and label the committee-selection rationale. | sprint_01 #2: To Grok Grokking: Provable Grokking in Ridge Regression (66206) ; sprint_01 #7: The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (60766) ; sprint_01 #8: Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII) (67084) ; sprint_01 #9: Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit (67118) |
| `C04` Public attention mismatch | high | not_ready | Public attention around robotics/world models reflects a recognizable mismatch with program selection rather than metadata or community-size artifacts. | Classify high-attention robotics papers as benchmark, demo, reusable model, or core algorithmic contribution and compare with oral/award status. | sprint_02 #8: World Guidance: World Modeling in Condition Space for Action Generation (61757) ; sprint_02 #9: Temporal Straightening for Latent Planning (64904) ; sprint_02 #11: LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries (65457) ; sprint_02 #12: Vision-Language-Action Pretraining from Large-Scale Human Videos (62813) |
| `C05` Neighboring-venue contrast | high | not_ready | The neighboring-venue contrast is meaningful after multimodal/vision is split into video, 3D/spatial, VLA, robustness, and generic vision-language submodes. | Break the sprint-02 multimodal/vision papers into submodes before interpreting the aggregate underweight/overweight signal. | sprint_02 #1: Motion Attribution for Video Generation (60542) ; sprint_02 #2: Multimodal Nested Learning for Decoupled and Coordinated Optimization (65954) ; sprint_02 #3: ExSkill: Continual Learning from Experience and Skills in Multimodal Agents (65729) ; sprint_02 #4: BabyVision: Visual Reasoning Beyond Language (63195) |
| `C06` External trend context | process | context_or_workflow_only | External arXiv and neighboring-venue baselines are useful context without implying venue policy or causal field momentum. | Run sensitivity checks on broad query terms and accepted-paper baselines before using any trend language. | sprint_01 #4: Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights (65901) ; sprint_01 #12: Reinforcement Learning via Self-Distillation (64121) ; sprint_01 #14: GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (63333) ; sprint_01 #15: mHC: Manifold-Constrained Hyper-Connections (61870) |
| `C07` Artifact visibility | high | not_ready | Visible repository links imply meaningful reproducibility rather than project pages, stale code, missing data, or unrunnable releases. | Open linked repositories for high-signal papers and record license, release state, data/checkpoints, dependencies, and runnable example. | sprint_01 #6: PaperBanana: Automating Academic Illustration for AI Scientists (65206) ; sprint_01 #20: From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model (66596) ; sprint_01 #27: Vision-aligned Latent Reasoning for Multi-Modal Large Language Model (61382) ; sprint_01 #28: AuTAgent: A Reinforcement Learning Framework for Tool-Augmented Audio Reasoning (64128) |
| `C08` Validation priority | process | context_or_workflow_only | The validation workflow is explicit enough to prevent directional heuristics from being promoted as settled conclusions. | Audit every report headline against reviewed rows, paper notes, acceptance criteria, and manual caveats before presentation use. | sprint_01 #1: How much can language models memorize? (62989) ; sprint_01 #2: To Grok Grokking: Provable Grokking in Ridge Regression (66206) ; sprint_01 #3: The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (61998) ; sprint_01 #5: Maximum Likelihood Reinforcement Learning (65332) |

## Claim Details

### C01: LLM reasoning center of gravity

- Allowed use now: Use as directional hypothesis or reading guide only.
- Statement under test: LLM reasoning/post-training is the largest ICML 2026 area and is also overweight relative to nearby accepted-paper baselines.
- Current evidence: 1099 taxonomy papers (16.6%); historical delta +2.9 pp; public-attention enrichment 2.03x.
- Primary caveat: Area boundaries include general LLM training/evaluation and some diffusion-language papers; paper-level taxonomy still needs review.
- Counterevidence to seek: Strong papers whose main contribution is infrastructure, safety, or generic modeling despite being counted as LLM reasoning/post-training.
- Manual evidence needed: review rows 0/8; support rows 0/5; paper notes 0/4; taxonomy checks on 12 dossier rows
- Pre-review bucket mix: likely_supports:14
- Evidence confidence mix: low:1; medium:13
- Special check: Boundary papers must confirm this is LLM reasoning/post-training rather than broad LLM infrastructure spillover.
- Next decision action: Fill first-sprint paper notes, then transfer decisions through the overlay bridge.
- Briefs to open: reports/review_reading_briefs/62989-how-much-can-language-models-memorize.md ; reports/review_reading_briefs/61998-the-flexibility-trap-rethinking-the-value-of-arbitrary-order-in-diffus.md ; reports/review_reading_briefs/65332-maximum-likelihood-reinforcement-learning.md ; reports/review_reading_briefs/65886-reinforcement-learning-with-evolving-rubrics-for-deep-research.md

### C02: Infrastructure and agentic workloads

- Allowed use now: Use as directional hypothesis or reading guide only.
- Statement under test: Systems/efficiency and agents/code look smaller than LLM reasoning by paper count, but both are clear ICML 2026 overweights versus the neighboring-venue baseline.
- Current evidence: Systems historical delta +2.1 pp, relative 1.68x; Agents historical delta +2.1 pp, relative 1.44x.
- Primary caveat: Historical comparison uses a keyword scorer; ICML 2025 and NeurIPS 2025 lack static abstracts in the current pull.
- Counterevidence to seek: Papers tagged as infrastructure where the actual contribution is narrow evaluation, dataset construction, or a non-agentic method.
- Manual evidence needed: review rows 0/8; support rows 0/5; paper notes 0/4; taxonomy checks on 5 dossier rows
- Pre-review bucket mix: likely_supports:14
- Evidence confidence mix: low:1; medium:13
- Special check: Historical-delta interpretation must survive a spot check of systems and agents/code examples.
- Next decision action: Fill first-sprint paper notes, then transfer decisions through the overlay bridge.
- Briefs to open: reports/review_reading_briefs/65901-neural-thickets-diverse-task-experts-are-dense-around-pretrained-weigh.md ; reports/review_reading_briefs/65206-paperbanana-automating-academic-illustration-for-ai-scientists.md ; reports/review_reading_briefs/66212-controlled-llm-training-on-spectral-sphere.md ; reports/review_reading_briefs/61870-mhc-manifold-constrained-hyper-connections.md

### C03: Program committee attention

- Allowed use now: Use as directional hypothesis or reading guide only.
- Statement under test: Theory and safety/governance receive more program signal than their public-attention signal would predict.
- Current evidence: Theory oral enrichment 1.45x vs public enrichment 0.46x; Safety oral enrichment 1.41x and 3 awards vs public enrichment 0.51x.
- Primary caveat: Oral/award counts are program signals, not full quality labels; award counts are small and volatile.
- Counterevidence to seek: Program-forward papers with weak technical novelty, unclear evidence, or primarily policy/editorial contribution.
- Manual evidence needed: review rows 0/8; support rows 0/5; paper notes 0/4; taxonomy checks on 3 dossier rows
- Pre-review bucket mix: likely_supports:14
- Evidence confidence mix: low:3; medium:11
- Special check: Low-public/high-program papers must yield concrete technical reasons for committee attention.
- Next decision action: Fill first-sprint paper notes, then transfer decisions through the overlay bridge.
- Briefs to open: reports/review_reading_briefs/66206-to-grok-grokking-provable-grokking-in-ridge-regression.md ; reports/review_reading_briefs/60766-the-obfuscation-atlas-mapping-where-honesty-emerges-in-rlvr-with-decep.md ; reports/review_reading_briefs/67084-position-ai-ml-deepfake-research-is-misaligned-with-ai-generated-non-c.md ; reports/review_reading_briefs/67118-position-the-alignment-community-is-unintentionally-building-a-censors.md

### C04: Public attention mismatch

- Allowed use now: Use as directional hypothesis or reading guide only.
- Statement under test: Robotics/embodiment is small by taxonomy count but unusually strong in public attention.
- Current evidence: 195 papers (2.9%); public-attention enrichment 2.11x vs oral enrichment 0.81x.
- Primary caveat: AlphaXiv likely overweights shareable VLA/world-model work and project-page traffic.
- Counterevidence to seek: High-vote robotics papers that are also clearly program-significant, technically deep, and not merely demo-visible.
- Manual evidence needed: review rows 0/6; support rows 0/4; paper notes 0/3
- Pre-review bucket mix: possible_support:12
- Evidence confidence mix: low:1; medium:10; very_low:1
- Special check: High-attention robotics papers must be labeled as benchmark, demo, reusable model, or core algorithmic contribution.
- Next decision action: Use sprint 02 paper notes, then transfer decisions through the sprint 02 overlay bridge.
- Briefs to open: reports/review_reading_briefs/61757-world-guidance-world-modeling-in-condition-space-for-action-generation.md ; reports/review_reading_briefs/64904-temporal-straightening-for-latent-planning.md ; reports/review_reading_briefs/65457-langforce-bayesian-decomposition-of-vision-language-action-models-via-.md ; reports/review_reading_briefs/62813-vision-language-action-pretraining-from-large-scale-human-videos.md

### C05: Neighboring-venue contrast

- Allowed use now: Use as directional hypothesis or reading guide only.
- Statement under test: Multimodal/vision is large inside ICML 2026 but underweight relative to NeurIPS 2025 and ICLR 2026 accepted-paper baselines.
- Current evidence: 889 taxonomy papers (13.4%); historical delta -3.1 pp, relative 0.82x.
- Primary caveat: This is the area most sensitive to venue scope and title/topic classification; ICLR/NeurIPS vision-heavy shares may dominate the baseline average.
- Counterevidence to seek: Submodes that are strong at ICML 2026 even if the aggregate multimodal/vision area looks underweight versus baselines.
- Manual evidence needed: review rows 0/7; support rows 0/4; paper notes 0/3; taxonomy checks on 1 dossier rows
- Pre-review bucket mix: possible_support:14
- Evidence confidence mix: low:1; medium:13
- Special check: Multimodal/vision aggregate must be broken into submodes before interpreting the neighboring-venue contrast.
- Next decision action: Use sprint 02 paper notes, then transfer decisions through the sprint 02 overlay bridge.
- Briefs to open: reports/review_reading_briefs/60542-motion-attribution-for-video-generation.md ; reports/review_reading_briefs/65954-multimodal-nested-learning-for-decoupled-and-coordinated-optimization.md ; reports/review_reading_briefs/65729-exskill-continual-learning-from-experience-and-skills-in-multimodal-ag.md ; reports/review_reading_briefs/63195-babyvision-visual-reasoning-beyond-language.md

### C06: External trend context

- Allowed use now: Use as context or workflow framing, not as a field-quality conclusion.
- Statement under test: The fastest broad arXiv growth areas are multimodal/vision, LLM reasoning, and safety/governance, but ICML 2026 does not mirror this ranking exactly.
- Current evidence: Multimodal, Vision, and Perception: 94.6%; LLM Reasoning, Post-Training, and RLVR: 59.9%; Safety, Governance, Privacy, and Society: 53.6%; Systems and Efficient Foundation Models: 43.3%
- Primary caveat: arXiv queries are broad, overlapping, and not acceptance or quality signals.
- Counterevidence to seek: Query variants or neighboring venues that reverse the claimed direction for the same area.
- Manual evidence needed: none
- Pre-review bucket mix: possible_support:14; unclear:2
- Evidence confidence mix: low:1; medium:15
- Special check: Use only as external context; do not promote to a venue-quality or acceptance trend claim.
- Next decision action: Keep as framing/context; do not promote as a paper-quality claim.
- Briefs to open: reports/review_reading_briefs/65901-neural-thickets-diverse-task-experts-are-dense-around-pretrained-weigh.md ; reports/review_reading_briefs/64121-reinforcement-learning-via-self-distillation.md ; reports/review_reading_briefs/63333-gdpo-group-reward-decoupled-normalization-policy-optimization-for-mult.md ; reports/review_reading_briefs/61870-mhc-manifold-constrained-hyper-connections.md

### C07: Artifact visibility

- Allowed use now: Use as directional hypothesis or reading guide only.
- Statement under test: Artifacts are most visible in agents/code, LLM reasoning, systems, and multimodal/vision, while theory remains much less artifact-linked.
- Current evidence: Robotics, Embodiment, and World Models: GitHub URL share 38.0%; Agents, Code, and Tool Use: GitHub URL share 32.9%; LLM Reasoning, Post-Training, and RLVR: GitHub URL share 32.1%; Generative Modeling: GitHub URL share 31.1%
- Primary caveat: GitHub metadata comes from AlphaXiv and does not prove runnable reproduction; some high-star links are templates or index repos.
- Counterevidence to seek: High-visibility papers whose repository is missing, stale, non-runnable, data-free, or not actually tied to the paper.
- Manual evidence needed: review rows 0/8; support rows 0/5; paper notes 0/4; artifact checks on 16 candidate rows
- Pre-review bucket mix: high_risk_artifact:12; high_visibility_artifact:4
- Evidence confidence mix: medium:16
- Special check: Repository links must be manually inspected for runnable code, data/checkpoints, license, and stale/broken state.
- Next decision action: Fill first-sprint paper notes, then transfer decisions through the overlay bridge.
- Briefs to open: reports/review_reading_briefs/65206-paperbanana-automating-academic-illustration-for-ai-scientists.md ; reports/review_reading_briefs/66596-from-abstraction-to-instantiation-learning-behavioral-representation-f.md ; reports/review_reading_briefs/61382-vision-aligned-latent-reasoning-for-multi-modal-large-language-model.md ; reports/review_reading_briefs/64128-autagent-a-reinforcement-learning-framework-for-tool-augmented-audio-r.md

### C08: Validation priority

- Allowed use now: Use as context or workflow framing, not as a field-quality conclusion.
- Statement under test: The biggest remaining quality jump is not more plotting; it is paper-level validation of boundary clusters and high-impact claims.
- Current evidence: 21 of 42 semantic clusters are marked needs_review; validation queue contains 192 papers across 12 areas.
- Primary caveat: The queue organizes review but does not mean evidence fields have been checked.
- Counterevidence to seek: Any final-report claim that lacks reviewed paper rows, has unresolved taxonomy boundaries, or cites AlphaXiv/GitHub as quality evidence.
- Manual evidence needed: none
- Pre-review bucket mix: possible_support:1; unclear:17
- Evidence confidence mix: low:3; medium:15
- Special check: Keep as a process/workflow claim; acceptance means the validation workflow remains explicit and auditable.
- Next decision action: Keep as framing/context; do not promote as a paper-quality claim.
- Briefs to open: reports/review_reading_briefs/62989-how-much-can-language-models-memorize.md ; reports/review_reading_briefs/66206-to-grok-grokking-provable-grokking-in-ridge-regression.md ; reports/review_reading_briefs/61998-the-flexibility-trap-rethinking-the-value-of-arbitrary-order-in-diffus.md ; reports/review_reading_briefs/65332-maximum-likelihood-reinforcement-learning.md

## Outputs

- `data/processed/icml2026_claim_risk_register.csv`
- `reports/icml2026_claim_risk_register.md`