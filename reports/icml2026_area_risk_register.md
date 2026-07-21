# ICML 2026 Area Risk Register

Area-level reliability register for deciding which landscape summaries are safe to use and which need more review.

## Snapshot

- Areas tracked: 12
- Risk tiers: critical: 7, high: 5
- Areas with no reviewed validation rows: 12

## Register

| Risk | Area | Review | Baseline risk | Taxonomy clusters | Main risk driver | Falsification test |
| --- | --- | ---: | --- | ---: | --- | --- |
| critical | LLM Reasoning, Post-Training, and RLVR | 0/16 | high | 5 | 5 taxonomy clusters need adjudication; high baseline sensitivity | Verify that LLM Reasoning, Post-Training, and RLVR is genuinely over-represented versus nearby accepted venues, not a classifier keyword effect. |
| critical | Multimodal, Vision, and Perception | 0/16 | high | 1 | 1 taxonomy clusters need adjudication; high baseline sensitivity; 1 low-confidence evidence-code rows | Check whether the venue-share direction and arXiv-growth direction are describing different phenomena, or whether one is an artifact of broad query terms/classifier boundaries. |
| critical | Theory, Optimization, and Algorithms | 0/16 | context | 3 | 3 taxonomy clusters need adjudication; program signal exceeds public attention; 4 low-confidence evidence-code rows | Adjudicate boundary clusters before making subarea-share or area-rank claims about Theory, Optimization, and Algorithms. |
| critical | AI for Science, Health, and Neuro | 0/16 | context | 4 | 4 taxonomy clusters need adjudication; 1 low-confidence evidence-code rows | Adjudicate boundary clusters before making subarea-share or area-rank claims about AI for Science, Health, and Neuro. |
| critical | Data-Centric, Causal, and Federated ML | 0/16 | context | 3 | 3 taxonomy clusters need adjudication; 1 low-confidence evidence-code rows | Adjudicate boundary clusters before making subarea-share or area-rank claims about Data-Centric, Causal, and Federated ML. |
| critical | Systems and Efficient Foundation Models | 0/16 | moderate | 1 | 1 taxonomy clusters need adjudication; moderate baseline sensitivity; public attention exceeds program signal; 2 low-confidence evidence-code rows | Read high-public, non-program papers and decide whether attention reflects novelty, demo visibility, or hype. |
| critical | Agents, Code, and Tool Use | 0/16 | context | 2 | 2 taxonomy clusters need adjudication; 1 low-confidence evidence-code rows | Review representative area-validation papers before turning orientation signals into prose claims. |
| high | Safety, Governance, Privacy, and Society | 0/16 | moderate | 0 | moderate baseline sensitivity; program signal exceeds public attention; 4 low-confidence evidence-code rows | Read program-forward, low-public papers and verify the technical rationale for committee attention. |
| high | Graphs, Geometry, and Representation Learning | 0/16 | context | 2 | 2 taxonomy clusters need adjudication; 4 low-confidence evidence-code rows | Review representative area-validation papers before turning orientation signals into prose claims. |
| high | Generative Modeling | 0/16 | context | 0 | 4 low-confidence evidence-code rows | Review representative area-validation papers before turning orientation signals into prose claims. |
| high | Reinforcement Learning and Control | 0/16 | context | 0 | 6 low-confidence evidence-code rows | Review representative area-validation papers before turning orientation signals into prose claims. |
| high | Robotics, Embodiment, and World Models | 0/16 | context | 0 | public attention exceeds program signal; 8 low-confidence evidence-code rows | Read high-public, non-program papers and decide whether attention reflects novelty, demo visibility, or hype. |

## Area Details

### LLM Reasoning, Post-Training, and RLVR

- Safe language: Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done.
- Trust tier: `high_review_need`; readiness tier: `high`
- Size/signals: 1099 papers (16.6%); oral 1.29x; public 2.03x; historical delta +2.9 pp
- Baseline issue types: historical_delta_sensitive; arxiv_query_sensitive
- Low-confidence evidence rows: 0
- Program/award rows in review queue: 10; GitHub rows: 11
- Recommended first checks: adjudicate taxonomy cluster(s) 24, 11, 2; sample historical high-confidence and low-margin classifications; rerun narrower and broader arXiv query variants; read program examples: How much can language models memorize? | The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models; read public-attention examples: Process Reward Models That Think | Reinforcement Learning via Self-Distillation; read boundary examples: How much can language models memorize? | The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models
- Briefing card: `reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md`

### Multimodal, Vision, and Perception

- Safe language: Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done.
- Trust tier: `high_review_need`; readiness tier: `moderate_to_high`
- Size/signals: 889 papers (13.4%); oral 0.58x; public 0.80x; historical delta -3.1 pp
- Baseline issue types: historical_delta_sensitive; arxiv_query_sensitive; baseline_disagreement
- Low-confidence evidence rows: 1
- Program/award rows in review queue: 10; GitHub rows: 8
- Recommended first checks: adjudicate taxonomy cluster(s) 36; sample historical high-confidence and low-margin classifications; rerun narrower and broader arXiv query variants; write a caveat separating ICML program mix from field-wide preprint momentum; read program examples: Motion Attribution for Video Generation | Holi-Spatial: Evolving Video Streams into Holistic 3D Spatial Intelligence; read public-attention examples: A Very Big Video Reasoning Suite | Causal-JEPA: Learning World Models through Object-Level Latent Interventions; read boundary examples: DroneDINO: Towards Heterogeneous Routed Mixture of Experts for Drone-based Unified Object Detection | Privacy-Aware Video Anomaly Detection: Guided Orthogonal Projection and a Comprehensive Evaluation Framework
- Briefing card: `reports/area_briefing_cards/multimodal-vision-and-perception.md`

### Theory, Optimization, and Algorithms

- Safe language: Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done.
- Trust tier: `high_review_need`; readiness tier: `high`
- Size/signals: 737 papers (11.1%); oral 1.45x; public 0.46x; historical delta +0.8 pp
- Baseline issue types: classifier_spot_check
- Low-confidence evidence rows: 4
- Program/award rows in review queue: 10; GitHub rows: 5
- Recommended first checks: adjudicate taxonomy cluster(s) 20, 7, 38; read program examples: To Grok Grokking: Provable Grokking in Ridge Regression | Equivalence of Context and Parameter Updates in Modern Transformer Blocks; read public-attention examples: Unifying and Optimizing Data Values for Selection via Sequential Decision-Making | Dimensional Collapse in Transformer Attention Outputs: A Challenge for Sparse Dictionary Learning; read boundary examples: To Grok Grokking: Provable Grokking in Ridge Regression | Equivalence of Context and Parameter Updates in Modern Transformer Blocks
- Briefing card: `reports/area_briefing_cards/theory-optimization-and-algorithms.md`

### AI for Science, Health, and Neuro

- Safe language: Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done.
- Trust tier: `high_review_need`; readiness tier: `high`
- Size/signals: 587 papers (8.9%); oral 1.08x; public 0.33x; historical delta +0.9 pp
- Baseline issue types: classifier_spot_check
- Low-confidence evidence rows: 1
- Program/award rows in review queue: 10; GitHub rows: 9
- Recommended first checks: adjudicate taxonomy cluster(s) 13, 39, 27; read program examples: Protein Autoregressive Modeling via Multiscale Structure Generation | dnaHNet: A Scalable and Hierarchical Foundation Model for Genomic Sequence Learning; read public-attention examples: GeoPT: Scaling Physics Simulation via Lifted Geometric Pre-Training | TSRBench: A Comprehensive Multi-task Multi-modal Time Series Reasoning Benchmark for Generalist Models; read boundary examples: Protein Autoregressive Modeling via Multiscale Structure Generation | dnaHNet: A Scalable and Hierarchical Foundation Model for Genomic Sequence Learning
- Briefing card: `reports/area_briefing_cards/ai-for-science-health-and-neuro.md`

### Data-Centric, Causal, and Federated ML

- Safe language: Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done.
- Trust tier: `high_review_need`; readiness tier: `high`
- Size/signals: 526 papers (7.9%); oral 0.75x; public 0.64x; historical delta -0.5 pp
- Baseline issue types: classifier_spot_check
- Low-confidence evidence rows: 1
- Program/award rows in review queue: 10; GitHub rows: 8
- Recommended first checks: adjudicate taxonomy cluster(s) 10, 17, 31; read program examples: Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning | Midtraining Bridges Pretraining and Posttraining Distributions; read public-attention examples: Self-Distillation Enables Continual Learning | Understanding LoRA as Knowledge Memory: An Empirical Analysis; read boundary examples: Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning | Midtraining Bridges Pretraining and Posttraining Distributions
- Briefing card: `reports/area_briefing_cards/data-centric-causal-and-federated-ml.md`

### Systems and Efficient Foundation Models

- Safe language: Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done.
- Trust tier: `high_review_need`; readiness tier: `high`
- Size/signals: 515 papers (7.8%); oral 0.69x; public 1.31x; historical delta +2.1 pp
- Baseline issue types: historical_delta_sensitive
- Low-confidence evidence rows: 2
- Program/award rows in review queue: 9; GitHub rows: 9
- Recommended first checks: adjudicate taxonomy cluster(s) 26; sample historical high-confidence and low-margin classifications; read program examples: Controlled LLM Training on Spectral Sphere | POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation; read public-attention examples: mHC: Manifold-Constrained Hyper-Connections | xKV: Cross-Layer KV-Cache Compression via Aligned Singular Vector Extraction; read boundary examples: Controlled LLM Training on Spectral Sphere | MuonSSM: Orthogonalizing State Space Models for Sequence Modeling
- Briefing card: `reports/area_briefing_cards/systems-and-efficient-foundation-models.md`

### Agents, Code, and Tool Use

- Safe language: Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done.
- Trust tier: `high_review_need`; readiness tier: `high`
- Size/signals: 496 papers (7.5%); oral 1.19x; public 1.52x; historical delta +2.1 pp
- Baseline issue types: classifier_spot_check
- Low-confidence evidence rows: 1
- Program/award rows in review queue: 10; GitHub rows: 13
- Recommended first checks: adjudicate taxonomy cluster(s) 30, 6; read program examples: $\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment | Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning; read public-attention examples: Learning to Discover at Test Time | PaperBanana: Automating Academic Illustration for AI Scientists; read boundary examples: Learning to Discover at Test Time | MemEvolve: Meta-Evolution of Agent Memory Systems
- Briefing card: `reports/area_briefing_cards/agents-code-and-tool-use.md`

### Safety, Governance, Privacy, and Society

- Safe language: Use as a directional area signal with explicit taxonomy/baseline caveats.
- Trust tier: `moderate_review_need`; readiness tier: `high`
- Size/signals: 502 papers (7.6%); oral 1.41x; public 0.51x; historical delta +1.3 pp
- Baseline issue types: arxiv_query_sensitive
- Low-confidence evidence rows: 4
- Program/award rows in review queue: 10; GitHub rows: 4
- Recommended first checks: rerun narrower and broader arXiv query variants; read program examples: The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit; read public-attention examples: Chain-of-Thought Reasoning In The Wild Is Not Always Faithful | The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models
- Briefing card: `reports/area_briefing_cards/safety-governance-privacy-and-society.md`

### Graphs, Geometry, and Representation Learning

- Safe language: Use as a directional area signal with explicit taxonomy/baseline caveats.
- Trust tier: `moderate_review_need`; readiness tier: `high`
- Size/signals: 391 papers (5.9%); oral 0.61x; public 0.38x; historical delta +1.2 pp
- Baseline issue types: classifier_spot_check
- Low-confidence evidence rows: 4
- Program/award rows in review queue: 6; GitHub rows: 6
- Recommended first checks: adjudicate taxonomy cluster(s) 18, 41; read program examples: Which Algorithms Can Graph Neural Networks Learn? | Towards Hierarchy–Uniformity Equilibrium: Recovering Semantic Depth in Hypergraph Contrastive Learning; read public-attention examples: Deep sequence models tend to memorize geometrically; it is unclear why. | Who Said Neural Networks Aren't Linear?; read boundary examples: Foundations of Equivariant Deep Learning: Unifying Graph and Sheaf Neural Networks | Necessary Conditions for Compositional Generalization of Embedding Models
- Briefing card: `reports/area_briefing_cards/graphs-geometry-and-representation-learning.md`

### Generative Modeling

- Safe language: Use as a directional area signal with explicit taxonomy/baseline caveats.
- Trust tier: `moderate_review_need`; readiness tier: `high`
- Size/signals: 379 papers (5.7%); oral 0.83x; public 0.96x; historical delta +0.5 pp
- Baseline issue types: classifier_spot_check
- Low-confidence evidence rows: 4
- Program/award rows in review queue: 8; GitHub rows: 6
- Recommended first checks: read program examples: A Random Matrix Perspective on the Consistency of Diffusion Models | High-accuracy sampling for diffusion models and log-concave distributions; read public-attention examples: One-step Latent-free Image Generation with Pixel Mean Flows | Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Video Generation
- Briefing card: `reports/area_briefing_cards/generative-modeling.md`

### Reinforcement Learning and Control

- Safe language: Use as a directional area signal with explicit taxonomy/baseline caveats.
- Trust tier: `moderate_review_need`; readiness tier: `high`
- Size/signals: 312 papers (4.7%); oral 0.76x; public 0.66x; historical delta +0.9 pp
- Baseline issue types: classifier_spot_check
- Low-confidence evidence rows: 6
- Program/award rows in review queue: 6; GitHub rows: 6
- Recommended first checks: read program examples: On Computation and Reinforcement Learning | Learning Human-Robot Collaboration via Heterogeneous-Agent Lyapunov Policy Optimization; read public-attention examples: Reinforcement Learning with Verifiable Rewards: GRPO's Loss, Dynamics, and Success Amplification | Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers
- Briefing card: `reports/area_briefing_cards/reinforcement-learning-and-control.md`

### Robotics, Embodiment, and World Models

- Safe language: Use as a directional area signal with explicit taxonomy/baseline caveats.
- Trust tier: `moderate_review_need`; readiness tier: `high`
- Size/signals: 195 papers (2.9%); oral 0.81x; public 2.11x; historical delta +0.4 pp
- Baseline issue types: classifier_spot_check
- Low-confidence evidence rows: 8
- Program/award rows in review queue: 4; GitHub rows: 8
- Recommended first checks: read program examples: RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies | From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models; read public-attention examples: Learning Latent Action World Models In The Wild | Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies
- Briefing card: `reports/area_briefing_cards/robotics-embodiment-and-world-models.md`

## Outputs

- `data/processed/icml2026_area_risk_register.csv`
- `reports/icml2026_area_risk_register.md`