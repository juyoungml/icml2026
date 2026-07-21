# ICML 2026 Manual Validation Queue

This queue selects papers for human validation of taxonomy boundaries and evidence codes.
It is designed to turn heuristic tags into trustworthy report claims.

## Snapshot

- Queue size: 192
- Areas covered: 12
- Target papers per area: up to 16
- Default quotas: 6 representative, 4 public-only, 4 program-only, then boundary/low-confidence fill
- Papers from taxonomy clusters needing review: 78
- Oral/award papers in queue: 103
- Papers with GitHub URLs in queue: 93

## Selection Reasons

- fault_line_representative: 72
- public_attention_not_program_signal: 48
- program_signal_low_public_attention: 33
- taxonomy_boundary_cluster: 21
- low_evidence_code_confidence: 18

## Area Queues

### LLM Reasoning, Post-Training, and RLVR
- Papers selected: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, program_signal_low_public_attention=4, taxonomy_boundary_cluster=2
  - How much can language models memorize? (fault_line_representative; oral; Outstanding Paper Honorable Mention; taxonomy-review; votes 271)
  - The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (fault_line_representative; oral; Outstanding Paper Award; taxonomy-review; votes 92)
  - Maximum Likelihood Reinforcement Learning (fault_line_representative; oral; taxonomy-review; votes 259)
  - Reinforcement Learning with Evolving Rubrics for Deep Research (fault_line_representative; oral; taxonomy-review; votes 201)
  - Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers (fault_line_representative; oral; taxonomy-review; votes 75)
  - WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference (fault_line_representative; oral; taxonomy-review; votes 60)
  - Process Reward Models That Think (public_attention_not_program_signal; votes 1815)
  - Reinforcement Learning via Self-Distillation (public_attention_not_program_signal; taxonomy-review; votes 718)

### Multimodal, Vision, and Perception
- Papers selected: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, program_signal_low_public_attention=4, taxonomy_boundary_cluster=2
  - Motion Attribution for Video Generation (fault_line_representative; oral; Outstanding Paper Honorable Mention; votes 67)
  - Holi-Spatial: Evolving Video Streams into Holistic 3D Spatial Intelligence (fault_line_representative; oral; votes 52)
  - Bad Seeing or Bad Thinking? Rewarding Perception for Multimodal Reasoning (fault_line_representative; oral; votes 21)
  - Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination (fault_line_representative; oral; votes 16)
  - 3ViewSense: Spatial and Mental Perspective Reasoning from Orthographic Views in Vision-Language Models (fault_line_representative; oral; votes 11)
  - CLEAR: Context-Aware Learning with End-to-End Mask-Free Inference for Adaptive Subtitle Removal (fault_line_representative; oral; votes 2)
  - A Very Big Video Reasoning Suite (public_attention_not_program_signal; votes 159)
  - Causal-JEPA: Learning World Models through Object-Level Latent Interventions (public_attention_not_program_signal; votes 150)

### Theory, Optimization, and Algorithms
- Papers selected: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, program_signal_low_public_attention=4, taxonomy_boundary_cluster=2
  - To Grok Grokking: Provable Grokking in Ridge Regression (fault_line_representative; oral; Outstanding Paper Honorable Mention; taxonomy-review; votes 7)
  - Equivalence of Context and Parameter Updates in Modern Transformer Blocks (fault_line_representative; oral; taxonomy-review; votes 24)
  - Non-Euclidean Gradient Descent Operates at the Edge of Stability (fault_line_representative; oral; votes 15)
  - Markov Chain Monte Carlo without Evaluating the Target: an Auxiliary Variable Approach (fault_line_representative; oral; votes 6)
  - Optimal Decision-Making Based on Prediction Sets (fault_line_representative; oral; taxonomy-review; votes 6)
  - Rational Transductors (fault_line_representative; oral; taxonomy-review; votes 4)
  - Unifying and Optimizing Data Values for Selection via Sequential Decision-Making (public_attention_not_program_signal; votes 271)
  - Dimensional Collapse in Transformer Attention Outputs: A Challenge for Sparse Dictionary Learning (public_attention_not_program_signal; taxonomy-review; votes 160)

### AI for Science, Health, and Neuro
- Papers selected: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, program_signal_low_public_attention=4, taxonomy_boundary_cluster=2
  - Protein Autoregressive Modeling via Multiscale Structure Generation (fault_line_representative; oral; taxonomy-review; votes 31)
  - dnaHNet: A Scalable and Hierarchical Foundation Model for Genomic Sequence Learning (fault_line_representative; oral; taxonomy-review; votes 20)
  - Orthogonal Concept Erasure for Diffusion Models (fault_line_representative; oral; taxonomy-review; votes 9)
  - LASER: Learning Active Sensing for Continuum Field Reconstruction (fault_line_representative; oral; votes 4)
  - From Text to Forecasts: Bridging Modality Gap with Temporal Evolution Semantic Space (fault_line_representative; oral; taxonomy-review; votes 4)
  - Protein Fold Classification at Scale: Benchmarking and Pretraining (fault_line_representative; oral; taxonomy-review; votes 2)
  - GeoPT: Scaling Physics Simulation via Lifted Geometric Pre-Training (public_attention_not_program_signal; votes 72)
  - TSRBench: A Comprehensive Multi-task Multi-modal Time Series Reasoning Benchmark for Generalist Models (public_attention_not_program_signal; taxonomy-review; votes 65)

### Data-Centric, Causal, and Federated ML
- Papers selected: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, program_signal_low_public_attention=4, taxonomy_boundary_cluster=2
  - Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning (fault_line_representative; oral; taxonomy-review; votes 98)
  - Midtraining Bridges Pretraining and Posttraining Distributions (fault_line_representative; oral; taxonomy-review; votes 47)
  - Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models (fault_line_representative; oral; taxonomy-review; votes 5)
  - DISCO: Mitigating Bias in Deep Learning with Conditional Distance Correlation (fault_line_representative; oral; votes 4)
  - Exact Functional ANOVA Decomposition for Categorical Inputs (fault_line_representative; oral; votes 2)
  - A Recursive Decomposition Framework for Causal Structure Learning in the Presence of Latent Variables (fault_line_representative; oral; votes 1)
  - Self-Distillation Enables Continual Learning (public_attention_not_program_signal; taxonomy-review; votes 590)
  - Understanding LoRA as Knowledge Memory: An Empirical Analysis (public_attention_not_program_signal; taxonomy-review; votes 262)

### Systems and Efficient Foundation Models
- Papers selected: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, program_signal_low_public_attention=3, taxonomy_boundary_cluster=3
  - Controlled LLM Training on Spectral Sphere (fault_line_representative; oral; taxonomy-review; votes 115)
  - POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation (fault_line_representative; oral; votes 19)
  - FlashSinkhorn: IO-Aware Entropic Optimal Transport on GPU (fault_line_representative; oral; votes 5)
  - ECHO: Elastic Speculative Decoding with Sparse Gating for High-Concurrency Scenarios (fault_line_representative; oral; votes 3)
  - FlashSketch: Sketch-Kernel Co-Design for Fast Sparse Sketching on GPUs (fault_line_representative; oral; votes 1)
  - MuonSSM: Orthogonalizing State Space Models for Sequence Modeling (fault_line_representative; oral; taxonomy-review; votes 0)
  - mHC: Manifold-Constrained Hyper-Connections (public_attention_not_program_signal; taxonomy-review; votes 696)
  - xKV: Cross-Layer KV-Cache Compression via Aligned Singular Vector Extraction (public_attention_not_program_signal; votes 518)

### Safety, Governance, Privacy, and Society
- Papers selected: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, program_signal_low_public_attention=4, low_evidence_code_confidence=2
  - The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (fault_line_representative; oral; Outstanding Paper Honorable Mention; votes 14)
  - Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII) (fault_line_representative; oral; Outstanding Position Paper Honorable Mention; votes 0)
  - Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit (fault_line_representative; oral; Outstanding Position Paper Award; votes 0)
  - Position: Anthropomorphic Misalignment Research Needs Stronger Evidence (fault_line_representative; oral; votes 13)
  - Position: Stop Automating Peer Review Without Rigorous Evaluation (fault_line_representative; oral; votes 13)
  - Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking (fault_line_representative; oral; votes 9)
  - Chain-of-Thought Reasoning In The Wild Is Not Always Faithful (public_attention_not_program_signal; votes 253)
  - The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models (public_attention_not_program_signal; votes 127)

### Agents, Code, and Tool Use
- Papers selected: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, program_signal_low_public_attention=4, taxonomy_boundary_cluster=2
  - $\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment (fault_line_representative; oral; votes 89)
  - Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning (fault_line_representative; oral; votes 89)
  - daVinci-Dev: Agent-native Mid-training for Software Engineering (fault_line_representative; oral; votes 52)
  - Monitoring Monitorability (fault_line_representative; oral; votes 28)
  - Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections (fault_line_representative; oral; votes 26)
  - CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability (fault_line_representative; oral; votes 21)
  - Learning to Discover at Test Time (public_attention_not_program_signal; taxonomy-review; votes 529)
  - PaperBanana: Automating Academic Illustration for AI Scientists (public_attention_not_program_signal; votes 420)

### Graphs, Geometry, and Representation Learning
- Papers selected: 16
- Selection mix: fault_line_representative=6, taxonomy_boundary_cluster=6, public_attention_not_program_signal=4
  - Which Algorithms Can Graph Neural Networks Learn? (fault_line_representative; oral; votes 7)
  - Foundations of Equivariant Deep Learning: Unifying Graph and Sheaf Neural Networks (fault_line_representative; oral; taxonomy-review; votes 0)
  - Necessary Conditions for Compositional Generalization of Embedding Models (fault_line_representative; oral; taxonomy-review; votes 0)
  - MV-FGAD: Towards Efficient and Effective Federated Graph Anomaly Detection via Multi-view Learning (fault_line_representative; oral; votes 0)
  - PhenoBrain: Phenotype-Conditioned Long-Range Communication for Multi-Modal Brain Network Analysis (fault_line_representative; oral; votes 0)
  - Towards Hierarchy–Uniformity Equilibrium: Recovering Semantic Depth in Hypergraph Contrastive Learning (fault_line_representative; oral; votes 0)
  - Deep sequence models tend to memorize geometrically; it is unclear why. (public_attention_not_program_signal; taxonomy-review; votes 76)
  - Who Said Neural Networks Aren't Linear? (public_attention_not_program_signal; taxonomy-review; votes 74)

### Generative Modeling
- Papers selected: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, low_evidence_code_confidence=4, program_signal_low_public_attention=2
  - A Random Matrix Perspective on the Consistency of Diffusion Models (fault_line_representative; oral; Outstanding Paper Honorable Mention; votes 14)
  - High-accuracy sampling for diffusion models and log-concave distributions (fault_line_representative; oral; Outstanding Paper Award; votes 9)
  - High-accuracy and dimension-free sampling with diffusions (fault_line_representative; oral; votes 21)
  - Transforming Weather Data from Pixel to Latent Space (fault_line_representative; oral; votes 11)
  - Rex: A Family of Reversible Exponential (Stochastic) Runge-Kutta Solvers (fault_line_representative; oral; votes 6)
  - Error Propagation Mechanisms and Compensation Strategies for Quantized Diffusion Models (fault_line_representative; oral; votes 3)
  - One-step Latent-free Image Generation with Pixel Mean Flows (public_attention_not_program_signal; votes 214)
  - Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Video Generation (public_attention_not_program_signal; votes 152)

### Reinforcement Learning and Control
- Papers selected: 16
- Selection mix: fault_line_representative=6, low_evidence_code_confidence=6, public_attention_not_program_signal=4
  - On Computation and Reinforcement Learning (fault_line_representative; oral; votes 11)
  - Learning Human-Robot Collaboration via Heterogeneous-Agent Lyapunov Policy Optimization (fault_line_representative; oral; votes 10)
  - Distributional Inverse Reinforcement Learning (fault_line_representative; oral; votes 5)
  - Chebyshev Policies and the Mountain Car Problem: Reinforcement Learning for Low-dimensional Control Tasks (fault_line_representative; oral; votes 3)
  - Stabilizing the Q-Gradient Field for Policy Smoothness in Actor-Critic Methods (fault_line_representative; oral; votes 2)
  - Video-Based Optimal Transport for Feedback-Efficient Offline Preference-Based Reinforcement Learning (fault_line_representative; oral; votes 0)
  - Reinforcement Learning with Verifiable Rewards: GRPO's Loss, Dynamics, and Success Amplification (public_attention_not_program_signal; votes 305)
  - Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers (public_attention_not_program_signal; votes 135)

### Robotics, Embodiment, and World Models
- Papers selected: 16
- Selection mix: fault_line_representative=6, low_evidence_code_confidence=6, public_attention_not_program_signal=4
  - RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies (fault_line_representative; oral; votes 66)
  - From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models (fault_line_representative; oral; votes 30)
  - XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations (fault_line_representative; oral; votes 19)
  - From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model (fault_line_representative; oral; votes 14)
  - Learning Latent Action World Models In The Wild (fault_line_representative; votes 273)
  - Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies (fault_line_representative; votes 204)
  - Temporal Straightening for Latent Planning (public_attention_not_program_signal; votes 202)
  - LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries (public_attention_not_program_signal; votes 189)

## Manual Fields To Fill

- `manual_validated`: yes/no.
- `manual_primary_contribution_type`: benchmark, dataset, method, theory, system, position, application, other.
- `manual_method_family`: concise human-checked method label.
- `manual_benchmarks`, `manual_datasets`, `manual_metrics`: verified names or `none`.
- `manual_artifact_status`: none, linked, live-unchecked, live-checked, runnable, broken, not-applicable.
- `manual_result_character`: positive, negative, mixed, position, theory, benchmark, unclear.
- `manual_fault_line_relevance`: why this paper supports or challenges an area fault line.

## Caveats

- Selection is deterministic and heuristic; it is a review queue, not a final reading list.
- The queue intentionally includes public-only, program-signal, and boundary-cluster papers so manual review is not popularity-only.