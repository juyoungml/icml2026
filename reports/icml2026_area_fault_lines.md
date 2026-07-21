# ICML 2026 Area Fault Lines

This report uses the curated manual taxonomy as the organizing spine.
It is meant to guide researcher reading and presentation narrative, not to replace paper-level review.

## Corpus Baselines

- Papers: 6,628
- Corpus oral rate: 2.5%
- Corpus GitHub URL share: 24.4%
- Corpus AlphaXiv public votes per paper: 9.12

## Area Briefs

### LLM Reasoning, Post-Training, and RLVR

Reasoning progress is splitting between reward-driven post-training, test-time search, and alternative sequence modeling.

Evidence:
- 1,099 papers (16.6% of corpus)
- 36 orals and 2 awards
- 18.55 AlphaXiv public votes/paper
- 31.8% GitHub URL share
- 5 of 6 semantic clusters still need taxonomy review
- primary contribution mix: Benchmark / evaluation (460); Method / algorithm (192); Dataset / data resource (142); Position / conceptual (112); Theory / proof (94); System / infrastructure (42); Uncoded (32); Application / domain study (25)
- method-family cues: Reasoning / test-time compute (608); RL / policy optimization (468); LLM post-training (468); Agents / tool use (290); Diffusion / flow (234); Compression / efficiency (180); Transformer / attention (154); Graphs / geometry (119)
- evaluation-setting cues: language/llm (1019); math/code/verifiable (308); theory/synthetic (226); robotics/embodied (120); security/safety (117); vision/video (66); science/domain (31)
- above-baseline oral density
- above-baseline public attention density
- above-baseline GitHub URL availability

Fault lines:
- Process supervision and reward models versus search, verification, and extra test-time compute.
- Verifiable math/code-style tasks versus open-ended research, planning, and multimodal reasoning.
- Autoregressive reasoning versus diffusion or arbitrary-order language generation.

What to read for:
- Does the paper optimize final answers, intermediate traces, rubrics, or verifier signals?
- Are gains robust outside tasks with cheap correctness checks?
- Does extra inference compute change capability, reliability, or only benchmark score?

Subareas: General LLM training, evaluation, and alignment (290); Reasoning models and chain-of-thought behavior (211); Reward modeling, preference feedback, and RL post-training (164); RL for reasoning models and verifiable rewards (161); Diffusion language models and decoding (145); LLM preference tuning and alignment training (128)
Top themes: LLM reasoning and test-time compute (810); Memorization, evaluation, and generalization (618); Theory, optimization, and sampling (524); RL for LLMs and verifiable rewards (522); Safety, alignment, governance, and risk (413); Systems, efficiency, and compression (409); Agents, tools, and computer use (377); Diffusion, flow, and generative modeling (243)
Evidence-coded contribution types: Benchmark / evaluation (460); Method / algorithm (192); Dataset / data resource (142); Position / conceptual (112); Theory / proof (94); System / infrastructure (42); Uncoded (32); Application / domain study (25)
Evidence-coded method families: Reasoning / test-time compute (608); RL / policy optimization (468); LLM post-training (468); Agents / tool use (290); Diffusion / flow (234); Compression / efficiency (180); Transformer / attention (154); Graphs / geometry (119)
Evidence-coded evaluation settings: language/llm (1019); math/code/verifiable (308); theory/synthetic (226); robotics/embodied (120); security/safety (117); vision/video (66); science/domain (31)

Representative/high-signal papers:
- How much can language models memorize? (Outstanding Paper Honorable Mention; oral); votes 271
- The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (Outstanding Paper Award; oral); votes 92
- Maximum Likelihood Reinforcement Learning (oral); votes 259
- Reinforcement Learning with Evolving Rubrics for Deep Research (oral); votes 201
- Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers (oral); votes 75
- WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference (oral); votes 60

Public-attention candidates not marked oral/award:
- Process Reward Models That Think; votes 1815
- Reinforcement Learning via Self-Distillation; votes 718
- Agent Learning via Early Experience; votes 532
- GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization; votes 507

Program-signal candidates with lower public attention:
- Diffract: Spectral View of LLM Domain Adaptation (oral); votes 0
- FlatLand: Personalized Graph Federated Learning via Tailored Lorentz Space (oral); votes 0
- Information Flow Reveals When to Trust Language Models (oral); votes 0
- On the Limits of LLM Adaptability: Impact of LLM Pre-Training on Annotation Task Performance (oral); votes 0

### Multimodal, Vision, and Perception

Vision-language work is moving from recognition toward grounded reasoning, spatial understanding, and video/world structure.

Evidence:
- 889 papers (13.4% of corpus)
- 13 orals and 1 awards
- 7.25 AlphaXiv public votes/paper
- 29.5% GitHub URL share
- 1 of 4 semantic clusters still need taxonomy review
- primary contribution mix: Benchmark / evaluation (436); Dataset / data resource (141); Method / algorithm (126); Position / conceptual (76); Theory / proof (49); System / infrastructure (35); Application / domain study (16); Uncoded (10)
- method-family cues: Reasoning / test-time compute (297); LLM post-training (277); Agents / tool use (231); Graphs / geometry (217); Transformer / attention (189); Diffusion / flow (179); Compression / efficiency (138); RL / policy optimization (127)
- evaluation-setting cues: vision/video (763); language/llm (468); math/code/verifiable (181); security/safety (133); robotics/embodied (124); theory/synthetic (93); science/domain (58)

Fault lines:
- Perception as feature extraction versus perception as an active reasoning bottleneck.
- Static image benchmarks versus long-video, 3D, spatial, and embodied settings.
- Generative visual models versus discriminative robustness and hallucination control.

What to read for:
- Can the method localize the visual evidence behind an answer?
- Does it evaluate temporal, 3D, or physical consistency rather than only caption-style accuracy?
- Are robustness claims tested under realistic corruptions, adversarial prompts, and distribution shift?

Subareas: Vision-language reasoning and video understanding (272); Multimodal representation and cross-modal alignment (237); 3D, video, motion, and spatial understanding (203); Vision robustness, detection, and adversarial perception (177)
Top themes: Multimodal, vision-language, and video (850); Memorization, evaluation, and generalization (525); Safety, alignment, governance, and risk (384); Agents, tools, and computer use (352); LLM reasoning and test-time compute (327); Systems, efficiency, and compression (276); Theory, optimization, and sampling (249); Diffusion, flow, and generative modeling (227)
Evidence-coded contribution types: Benchmark / evaluation (436); Dataset / data resource (141); Method / algorithm (126); Position / conceptual (76); Theory / proof (49); System / infrastructure (35); Application / domain study (16); Uncoded (10)
Evidence-coded method families: Reasoning / test-time compute (297); LLM post-training (277); Agents / tool use (231); Graphs / geometry (217); Transformer / attention (189); Diffusion / flow (179); Compression / efficiency (138); RL / policy optimization (127)
Evidence-coded evaluation settings: vision/video (763); language/llm (468); math/code/verifiable (181); security/safety (133); robotics/embodied (124); theory/synthetic (93); science/domain (58)

Representative/high-signal papers:
- Motion Attribution for Video Generation (Outstanding Paper Honorable Mention; oral); votes 67
- Holi-Spatial: Evolving Video Streams into Holistic 3D Spatial Intelligence (oral); votes 52
- Bad Seeing or Bad Thinking? Rewarding Perception for Multimodal Reasoning (oral); votes 21
- Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination (oral); votes 16
- 3ViewSense: Spatial and Mental Perspective Reasoning from Orthographic Views in Vision-Language Models (oral); votes 11
- CLEAR: Context-Aware Learning with End-to-End Mask-Free Inference for Adaptive Subtitle Removal (oral); votes 2

Public-attention candidates not marked oral/award:
- A Very Big Video Reasoning Suite; votes 159
- Causal-JEPA: Learning World Models through Object-Level Latent Interventions; votes 150
- ExSkill: Continual Learning from Experience and Skills in Multimodal Agents; votes 147
- BabyVision: Visual Reasoning Beyond Language; votes 134

Program-signal candidates with lower public attention:
- Multimodal Nested Learning for Decoupled and Coordinated Optimization (oral); votes 0
- DroneDINO: Towards Heterogeneous Routed Mixture of Experts for Drone-based Unified Object Detection (oral); votes 0
- Privacy-Aware Video Anomaly Detection: Guided Orthogonal Projection and a Comprehensive Evaluation Framework (oral); votes 0
- DOUBT: Decoupled Object-level Understanding and Bridging via vMF-based Trustworthiness for Hallucination Detection in MLLMs (oral); votes 0

### Theory, Optimization, and Algorithms

The theory track is balancing classical guarantees with explanations of transformer-era behavior.

Evidence:
- 737 papers (11.1% of corpus)
- 27 orals and 1 awards
- 4.21 AlphaXiv public votes/paper
- 11.8% GitHub URL share
- 3 of 6 semantic clusters still need taxonomy review
- primary contribution mix: Theory / proof (372); Dataset / data resource (101); Benchmark / evaluation (99); Method / algorithm (78); Position / conceptual (53); Uncoded (15); System / infrastructure (12); Application / domain study (7)
- method-family cues: Bayesian / probabilistic (188); Transformer / attention (121); Diffusion / flow (115); Graphs / geometry (98); Agents / tool use (86); Compression / efficiency (82); RL / policy optimization (76); LLM post-training (52)
- evaluation-setting cues: theory/synthetic (475); language/llm (88); robotics/embodied (72); security/safety (65); math/code/verifiable (53); vision/video (45); science/domain (17)
- above-baseline oral density

Fault lines:
- Asymptotic or idealized guarantees versus phenomena observed in current large-scale models.
- Optimization theory for convex/stochastic settings versus practical deep-network training dynamics.
- Probabilistic and Bayesian rigor versus scalable approximate inference.

What to read for:
- Which assumptions are doing the real work?
- Does the theorem explain a contemporary empirical pattern or stand as a separate mathematical result?
- Are constants, dimensions, and compute requirements meaningful at modern model scales?

Subareas: Statistical learning theory and regression (180); Online learning, bandits, and regret (172); Convex, stochastic, and nonconvex optimization (127); Bayesian and probabilistic methods (125); Transformer theory and attention expressivity (98); Quantum, matrix, and numerical optimization (35)
Top themes: Theory, optimization, and sampling (647); Safety, alignment, governance, and risk (229); Memorization, evaluation, and generalization (219); LLM reasoning and test-time compute (181); Systems, efficiency, and compression (174); Agents, tools, and computer use (124); Diffusion, flow, and generative modeling (119); Interpretability and mechanistic analysis (106)
Evidence-coded contribution types: Theory / proof (372); Dataset / data resource (101); Benchmark / evaluation (99); Method / algorithm (78); Position / conceptual (53); Uncoded (15); System / infrastructure (12); Application / domain study (7)
Evidence-coded method families: Bayesian / probabilistic (188); Transformer / attention (121); Diffusion / flow (115); Graphs / geometry (98); Agents / tool use (86); Compression / efficiency (82); RL / policy optimization (76); LLM post-training (52)
Evidence-coded evaluation settings: theory/synthetic (475); language/llm (88); robotics/embodied (72); security/safety (65); math/code/verifiable (53); vision/video (45); science/domain (17)

Representative/high-signal papers:
- To Grok Grokking: Provable Grokking in Ridge Regression (Outstanding Paper Honorable Mention; oral); votes 7
- Equivalence of Context and Parameter Updates in Modern Transformer Blocks (oral); votes 24
- Non-Euclidean Gradient Descent Operates at the Edge of Stability (oral); votes 15
- Markov Chain Monte Carlo without Evaluating the Target: an Auxiliary Variable Approach (oral); votes 6
- Optimal Decision-Making Based on Prediction Sets (oral); votes 6
- Rational Transductors (oral); votes 4

Public-attention candidates not marked oral/award:
- Unifying and Optimizing Data Values for Selection via Sequential Decision-Making; votes 271
- Dimensional Collapse in Transformer Attention Outputs: A Challenge for Sparse Dictionary Learning; votes 160
- Weight-sparse transformers have interpretable circuits; votes 137
- You Need Better Attention Priors; votes 78

Program-signal candidates with lower public attention:
- Path-dependent Discrete Amortized Inference (oral); votes 0
- Robust Contextual Optimization with Missing Covariates (oral); votes 0
- DPO Unchained: Your Training Algorithm is Secretly Disentangled in Human Choice Theory (and Its Loss' Convexity is Dispensable) (oral); votes 0
- Equilibrium Pricing in Oligopolistic Data Markets (oral); votes 0

### AI for Science, Health, and Neuro

Scientific ML is broadening from surrogate modeling into foundation models for biological, physical, temporal, and neural data.

Evidence:
- 587 papers (8.9% of corpus)
- 16 orals and 0 awards
- 3.01 AlphaXiv public votes/paper
- 19.4% GitHub URL share
- 4 of 5 semantic clusters still need taxonomy review
- primary contribution mix: Benchmark / evaluation (194); Dataset / data resource (115); Method / algorithm (76); Theory / proof (63); System / infrastructure (47); Application / domain study (46); Position / conceptual (38); Uncoded (8)
- method-family cues: Diffusion / flow (180); Graphs / geometry (146); Transformer / attention (135); Agents / tool use (118); Compression / efficiency (110); LLM post-training (79); Bayesian / probabilistic (63); Reasoning / test-time compute (53)
- evaluation-setting cues: science/domain (252); theory/synthetic (169); vision/video (132); math/code/verifiable (93); language/llm (92); security/safety (58); robotics/embodied (48)

Fault lines:
- General ML architecture contribution versus domain-specific modeling contribution.
- Benchmark performance versus scientific validity, uncertainty, and deployability.
- Foundation-model pretraining versus small-data, mechanistic, or simulation-grounded methods.

What to read for:
- Is the evaluation tied to a real scientific decision or only a proxy benchmark?
- Are domain constraints, units, symmetries, and uncertainty modeled explicitly?
- Does the method improve discovery or forecasting under realistic data scarcity?

Subareas: Time series and forecasting applications (160); Protein, molecule, and biological modeling (148); Physical sciences, chemistry, and climate (128); Latent dynamics, neuroscience, and dynamical systems (84); Spiking neural networks and neural signals (67)
Top themes: AI for science, health, and biology (392); Memorization, evaluation, and generalization (288); Theory, optimization, and sampling (239); Systems, efficiency, and compression (186); Safety, alignment, governance, and risk (175); Diffusion, flow, and generative modeling (163); Agents, tools, and computer use (133); Multimodal, vision-language, and video (127)
Evidence-coded contribution types: Benchmark / evaluation (194); Dataset / data resource (115); Method / algorithm (76); Theory / proof (63); System / infrastructure (47); Application / domain study (46); Position / conceptual (38); Uncoded (8)
Evidence-coded method families: Diffusion / flow (180); Graphs / geometry (146); Transformer / attention (135); Agents / tool use (118); Compression / efficiency (110); LLM post-training (79); Bayesian / probabilistic (63); Reasoning / test-time compute (53)
Evidence-coded evaluation settings: science/domain (252); theory/synthetic (169); vision/video (132); math/code/verifiable (93); language/llm (92); security/safety (58); robotics/embodied (48)

Representative/high-signal papers:
- Protein Autoregressive Modeling via Multiscale Structure Generation (oral); votes 31
- dnaHNet: A Scalable and Hierarchical Foundation Model for Genomic Sequence Learning (oral); votes 20
- Orthogonal Concept Erasure for Diffusion Models (oral); votes 9
- LASER: Learning Active Sensing for Continuum Field Reconstruction (oral); votes 4
- From Text to Forecasts: Bridging Modality Gap with Temporal Evolution Semantic Space (oral); votes 4
- Protein Fold Classification at Scale: Benchmarking and Pretraining (oral); votes 2

Public-attention candidates not marked oral/award:
- GeoPT: Scaling Physics Simulation via Lifted Geometric Pre-Training; votes 72
- TSRBench: A Comprehensive Multi-task Multi-modal Time Series Reasoning Benchmark for Generalist Models; votes 65
- Understanding Self-Supervised Learning via Latent Distribution Matching; votes 33
- OpenTSLM: Time-Series Language Models for Reasoning over Multivariate Medical Text- and Time-Series Data; votes 32

Program-signal candidates with lower public attention:
- AI Engram: In Search of Memory Traces in Artificial Intelligence (oral); votes 0
- CoEvol-NO: State and Coordinate Co-Evolution with an Error-Driven Predictor-Corrector Paradigm for Neural Operator Transformer (oral); votes 0
- Geometric Flow Grounding: A Unified Manifold Decoupling Framework for Dynamics Discovery and Verification (oral); votes 0
- ReViT: Rotational-equivariant Vision Transformers for Neural PDE Solvers (oral); votes 0

### Data-Centric, Causal, and Federated ML

Data quality, causality, and distributed learning are converging around what supervision is trustworthy.

Evidence:
- 526 papers (7.9% of corpus)
- 10 orals and 0 awards
- 5.82 AlphaXiv public votes/paper
- 16.4% GitHub URL share
- 3 of 4 semantic clusters still need taxonomy review
- primary contribution mix: Benchmark / evaluation (166); Dataset / data resource (143); Method / algorithm (68); Theory / proof (61); Position / conceptual (54); System / infrastructure (14); Application / domain study (12); Uncoded (8)
- method-family cues: Causal / data-centric (127); LLM post-training (126); Compression / efficiency (83); Agents / tool use (79); Graphs / geometry (78); Reasoning / test-time compute (65); Transformer / attention (56); Bayesian / probabilistic (51)
- evaluation-setting cues: theory/synthetic (200); language/llm (170); security/safety (112); vision/video (80); math/code/verifiable (50); robotics/embodied (31); science/domain (26)

Fault lines:
- More data versus better selected, relabeled, distilled, or causally grounded data.
- Predictive correlations versus causal mechanisms and intervention validity.
- Centralized training assumptions versus privacy, federation, heterogeneity, and client incentives.

What to read for:
- Does the method improve data selection or merely add a new scoring heuristic?
- Are causal assumptions identifiable from the available data?
- Does the federated setup model realistic client drift, incentives, and system constraints?

Subareas: Labels, datasets, and supervised data quality (192); Continual learning, forgetting, and task adaptation (138); Causal inference and causal discovery (111); Federated learning and distributed clients (85)
Top themes: Safety, alignment, governance, and risk (261); Memorization, evaluation, and generalization (255); Theory, optimization, and sampling (238); Causality and data-centric ML (163); Systems, efficiency, and compression (151); LLM reasoning and test-time compute (117); Agents, tools, and computer use (110); Interpretability and mechanistic analysis (102)
Evidence-coded contribution types: Benchmark / evaluation (166); Dataset / data resource (143); Method / algorithm (68); Theory / proof (61); Position / conceptual (54); System / infrastructure (14); Application / domain study (12); Uncoded (8)
Evidence-coded method families: Causal / data-centric (127); LLM post-training (126); Compression / efficiency (83); Agents / tool use (79); Graphs / geometry (78); Reasoning / test-time compute (65); Transformer / attention (56); Bayesian / probabilistic (51)
Evidence-coded evaluation settings: theory/synthetic (200); language/llm (170); security/safety (112); vision/video (80); math/code/verifiable (50); robotics/embodied (31); science/domain (26)

Representative/high-signal papers:
- Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning (oral); votes 98
- Midtraining Bridges Pretraining and Posttraining Distributions (oral); votes 47
- Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models (oral); votes 5
- DISCO: Mitigating Bias in Deep Learning with Conditional Distance Correlation (oral); votes 4
- Exact Functional ANOVA Decomposition for Categorical Inputs (oral); votes 2
- A Recursive Decomposition Framework for Causal Structure Learning in the Presence of Latent Variables (oral); votes 1

Public-attention candidates not marked oral/award:
- Self-Distillation Enables Continual Learning; votes 590
- Understanding LoRA as Knowledge Memory: An Empirical Analysis; votes 262
- ATLAS: Learning to Optimally Memorize the Context at Test Time; votes 168
- Retaining by Doing: The Role of On-Policy Data in Mitigating Forgetting; votes 96

Program-signal candidates with lower public attention:
- On the Identifiability of Poisson Branching Structural Causal Model Under Latent Confounding (oral); votes 0
- Detecting the Semantic Fixed Point: A Geometric Framework for Efficient Inference (oral); votes 0
- On the Difficulty of Learning a Meta-network for Training Data Selection (oral); votes 0
- A Recursive Decomposition Framework for Causal Structure Learning in the Presence of Latent Variables (oral); votes 1

### Systems and Efficient Foundation Models

Efficiency papers increasingly claim capability relevance, not just lower cost.

Evidence:
- 515 papers (7.8% of corpus)
- 9 orals and 0 awards
- 11.97 AlphaXiv public votes/paper
- 24.5% GitHub URL share
- 1 of 4 semantic clusters still need taxonomy review
- primary contribution mix: Benchmark / evaluation (135); Theory / proof (103); System / infrastructure (98); Method / algorithm (72); Dataset / data resource (45); Position / conceptual (37); Application / domain study (19); Uncoded (6)
- method-family cues: Compression / efficiency (266); Transformer / attention (164); Agents / tool use (138); LLM post-training (130); Reasoning / test-time compute (68); Graphs / geometry (57); Diffusion / flow (52); RL / policy optimization (31)
- evaluation-setting cues: language/llm (324); theory/synthetic (129); math/code/verifiable (105); vision/video (69); security/safety (33); robotics/embodied (24); science/domain (8)
- above-baseline public attention density

Fault lines:
- Training/inference cost reduction versus preservation of reasoning, calibration, and safety behavior.
- Kernel or hardware-specific wins versus algorithmic improvements that transfer across deployments.
- Long-context memory, KV-cache, quantization, MoE, and serving throughput as separate bottlenecks.

What to read for:
- Are results measured at realistic batch sizes, sequence lengths, hardware, and latency budgets?
- What capability regresses under compression or cache pruning?
- Is the speedup end-to-end or only for an isolated kernel/subroutine?

Subareas: Large-scale training, optimizers, and model architecture (198); Serving, GPU memory, MoE, and throughput (116); Long-context attention and KV-cache compression (113); Quantization and low-precision training/inference (88)
Top themes: Systems, efficiency, and compression (345); Theory, optimization, and sampling (259); LLM reasoning and test-time compute (222); Memorization, evaluation, and generalization (184); RL for LLMs and verifiable rewards (116); Safety, alignment, governance, and risk (116); Interpretability and mechanistic analysis (104); Agents, tools, and computer use (96)
Evidence-coded contribution types: Benchmark / evaluation (135); Theory / proof (103); System / infrastructure (98); Method / algorithm (72); Dataset / data resource (45); Position / conceptual (37); Application / domain study (19); Uncoded (6)
Evidence-coded method families: Compression / efficiency (266); Transformer / attention (164); Agents / tool use (138); LLM post-training (130); Reasoning / test-time compute (68); Graphs / geometry (57); Diffusion / flow (52); RL / policy optimization (31)
Evidence-coded evaluation settings: language/llm (324); theory/synthetic (129); math/code/verifiable (105); vision/video (69); security/safety (33); robotics/embodied (24); science/domain (8)

Representative/high-signal papers:
- Controlled LLM Training on Spectral Sphere (oral); votes 115
- POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation (oral); votes 19
- FlashSinkhorn: IO-Aware Entropic Optimal Transport on GPU (oral); votes 5
- ECHO: Elastic Speculative Decoding with Sparse Gating for High-Concurrency Scenarios (oral); votes 3
- FlashSketch: Sketch-Kernel Co-Design for Fast Sparse Sketching on GPUs (oral); votes 1
- MuonSSM: Orthogonalizing State Space Models for Sequence Modeling (oral); votes 0

Public-attention candidates not marked oral/award:
- mHC: Manifold-Constrained Hyper-Connections; votes 696
- xKV: Cross-Layer KV-Cache Compression via Aligned Singular Vector Extraction; votes 518
- Evolution Strategies at the Hyperscale; votes 405
- Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights; votes 365

Program-signal candidates with lower public attention:
- MuonSSM: Orthogonalizing State Space Models for Sequence Modeling (oral); votes 0
- CAT-Q: Cost-efficient and Accurate Ternary Quantization for LLMs (oral); votes 0
- ReQAT: Achieving Full-Precision Reasoning Accuracy with 4-bit Floating-Point Quantization-Aware Training (oral); votes 0
- Faster Activation Functions at the Edge for Post-Training Speedups (oral); votes 0

### Safety, Governance, Privacy, and Society

Safety and society papers are programmatically central, but vary sharply in executable evidence.

Evidence:
- 502 papers (7.6% of corpus)
- 18 orals and 3 awards
- 4.64 AlphaXiv public votes/paper
- 19.9% GitHub URL share
- 0 of 3 semantic clusters still need taxonomy review
- primary contribution mix: Position / conceptual (153); Benchmark / evaluation (101); Method / algorithm (88); Dataset / data resource (71); Theory / proof (43); System / infrastructure (21); Uncoded (15); Application / domain study (10)
- method-family cues: Agents / tool use (169); LLM post-training (145); Reasoning / test-time compute (129); RL / policy optimization (79); Diffusion / flow (39); Transformer / attention (36); Compression / efficiency (34); Graphs / geometry (31)
- evaluation-setting cues: security/safety (360); language/llm (287); theory/synthetic (109); robotics/embodied (75); math/code/verifiable (65); vision/video (54); science/domain (9)
- above-baseline oral density

Fault lines:
- Technical safety benchmarks versus position papers about governance, harms, and conference norms.
- Attack/defense papers versus measurement validity and reproducibility of threat models.
- Privacy and unlearning guarantees versus practical utility and auditability.

What to read for:
- Is the harm or threat model operationalized precisely enough to test?
- Can the benchmark, attack, or defense be independently reproduced?
- Does the paper separate empirical evidence from normative argument?

Subareas: Adversarial safety, attacks, and security (245); Position papers, policy, and social impacts (173); Privacy, differential privacy, and unlearning (84)
Top themes: Safety, alignment, governance, and risk (461); Agents, tools, and computer use (215); Memorization, evaluation, and generalization (207); Theory, optimization, and sampling (149); Interpretability and mechanistic analysis (137); Systems, efficiency, and compression (127); LLM reasoning and test-time compute (125); RL for LLMs and verifiable rewards (110)
Evidence-coded contribution types: Position / conceptual (153); Benchmark / evaluation (101); Method / algorithm (88); Dataset / data resource (71); Theory / proof (43); System / infrastructure (21); Uncoded (15); Application / domain study (10)
Evidence-coded method families: Agents / tool use (169); LLM post-training (145); Reasoning / test-time compute (129); RL / policy optimization (79); Diffusion / flow (39); Transformer / attention (36); Compression / efficiency (34); Graphs / geometry (31)
Evidence-coded evaluation settings: security/safety (360); language/llm (287); theory/synthetic (109); robotics/embodied (75); math/code/verifiable (65); vision/video (54); science/domain (9)

Representative/high-signal papers:
- The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (Outstanding Paper Honorable Mention; oral); votes 14
- Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII) (Outstanding Position Paper Honorable Mention; oral); votes 0
- Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit (Outstanding Position Paper Award; oral); votes 0
- Position: Anthropomorphic Misalignment Research Needs Stronger Evidence (oral); votes 13
- Position: Stop Automating Peer Review Without Rigorous Evaluation (oral); votes 13
- Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking (oral); votes 9

Public-attention candidates not marked oral/award:
- Chain-of-Thought Reasoning In The Wild Is Not Always Faithful; votes 253
- The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models; votes 127
- Reasoning Models Struggle to Control their Chains of Thought; votes 75
- Towards a Science of AI Agent Reliability; votes 72

Program-signal candidates with lower public attention:
- Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models (oral); votes 0
- Position: AI Should Facilitate Democratic Deliberation at Scale (oral); votes 0
- Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII) (Outstanding Position Paper Honorable Mention; oral); votes 0
- Position: Don't Just "Fix it in Post'': A Science of AI Must Study Learning Dynamics (oral); votes 0

### Agents, Code, and Tool Use

Agents are shifting from impressive demos toward evaluation harnesses, tool environments, and software/security tasks.

Evidence:
- 496 papers (7.5% of corpus)
- 15 orals and 0 awards
- 13.87 AlphaXiv public votes/paper
- 32.9% GitHub URL share
- 2 of 3 semantic clusters still need taxonomy review
- primary contribution mix: Benchmark / evaluation (276); Position / conceptual (55); Method / algorithm (48); Dataset / data resource (41); Theory / proof (35); System / infrastructure (27); Uncoded (7); Application / domain study (7)
- method-family cues: Agents / tool use (412); Reasoning / test-time compute (271); RL / policy optimization (150); LLM post-training (100); Graphs / geometry (63); Diffusion / flow (41); Compression / efficiency (35); Transformer / attention (24)
- evaluation-setting cues: language/llm (414); math/code/verifiable (213); theory/synthetic (90); robotics/embodied (79); security/safety (43); vision/video (30); science/domain (15)
- above-baseline public attention density
- above-baseline GitHub URL availability

Fault lines:
- Better scaffolding and prompting versus actual learned agent capability.
- Static benchmarks versus dynamic environments with hidden state, long horizons, and recovery from failure.
- Code and security agents as practical systems versus brittle benchmark optimizers.

What to read for:
- Does the environment prevent leakage and reward shortcut behavior?
- Is improvement coming from model training, search, memory, tools, or evaluation-loop design?
- Are failures categorized by planning, perception, tool use, memory, or execution?

Subareas: Agent evaluation, tool use, and agentic workflows (207); Multi-agent search, planning, and coordination (150); Code LLMs, verification, and software tasks (139)
Top themes: Agents, tools, and computer use (375); Memorization, evaluation, and generalization (350); LLM reasoning and test-time compute (328); RL for LLMs and verifiable rewards (177); Theory, optimization, and sampling (177); Systems, efficiency, and compression (151); Safety, alignment, governance, and risk (135); AI for science, health, and biology (62)
Evidence-coded contribution types: Benchmark / evaluation (276); Position / conceptual (55); Method / algorithm (48); Dataset / data resource (41); Theory / proof (35); System / infrastructure (27); Uncoded (7); Application / domain study (7)
Evidence-coded method families: Agents / tool use (412); Reasoning / test-time compute (271); RL / policy optimization (150); LLM post-training (100); Graphs / geometry (63); Diffusion / flow (41); Compression / efficiency (35); Transformer / attention (24)
Evidence-coded evaluation settings: language/llm (414); math/code/verifiable (213); theory/synthetic (90); robotics/embodied (79); security/safety (43); vision/video (30); science/domain (15)

Representative/high-signal papers:
- $\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment (oral); votes 89
- Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning (oral); votes 89
- daVinci-Dev: Agent-native Mid-training for Software Engineering (oral); votes 52
- Monitoring Monitorability (oral); votes 28
- Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections (oral); votes 26
- CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability (oral); votes 21

Public-attention candidates not marked oral/award:
- Learning to Discover at Test Time; votes 529
- PaperBanana: Automating Academic Illustration for AI Scientists; votes 420
- ToolOrchestra: Elevating Intelligence via Efficient Model and Tool Orchestration; votes 260
- MemEvolve: Meta-Evolution of Agent Memory Systems; votes 194

Program-signal candidates with lower public attention:
- CausalGame: Benchmarking Causal Thinking of LLM Agents in Games (oral); votes 0
- Characterizing Agents in Production (oral); votes 0
- VenusBench-Mobile: A Challenging and User-Centric Benchmark for Mobile GUI Agents with Capability Diagnostics (oral); votes 0
- Unsupervised Partner Design Enables Robust Ad-hoc Teamwork (oral); votes 0

### Graphs, Geometry, and Representation Learning

Graph and geometric methods remain a bridge between structure-aware theory and domain-specific representations.

Evidence:
- 391 papers (5.9% of corpus)
- 6 orals and 0 awards
- 3.51 AlphaXiv public votes/paper
- 19.4% GitHub URL share
- 2 of 3 semantic clusters still need taxonomy review
- primary contribution mix: Benchmark / evaluation (104); Dataset / data resource (104); Method / algorithm (55); Theory / proof (51); Position / conceptual (44); System / infrastructure (15); Uncoded (10); Application / domain study (8)
- method-family cues: Graphs / geometry (331); LLM post-training (80); Transformer / attention (74); Diffusion / flow (73); Agents / tool use (62); Compression / efficiency (57); Reasoning / test-time compute (47); Bayesian / probabilistic (22)
- evaluation-setting cues: theory/synthetic (122); vision/video (108); language/llm (64); math/code/verifiable (48); security/safety (37); robotics/embodied (27); science/domain (21)

Fault lines:
- Equivariance and invariance as architectural priors versus learned latent geometry.
- Graph foundation/generalization claims versus task-specific message-passing improvements.
- Theoretical expressivity versus scalability on real graph and geometric data.

What to read for:
- Which symmetries or structural assumptions are encoded, and are they valid for the data?
- Does the method scale beyond curated graph benchmarks?
- Are representation claims validated by transfer, robustness, or interpretability?

Subareas: Graph neural networks and graph learning (166); Geometric representation learning and manifolds (160); Equivariant graph and geometric networks (65)
Top themes: Memorization, evaluation, and generalization (172); Theory, optimization, and sampling (160); Safety, alignment, governance, and risk (144); Multimodal, vision-language, and video (102); Systems, efficiency, and compression (98); Agents, tools, and computer use (90); LLM reasoning and test-time compute (78); Diffusion, flow, and generative modeling (75)
Evidence-coded contribution types: Benchmark / evaluation (104); Dataset / data resource (104); Method / algorithm (55); Theory / proof (51); Position / conceptual (44); System / infrastructure (15); Uncoded (10); Application / domain study (8)
Evidence-coded method families: Graphs / geometry (331); LLM post-training (80); Transformer / attention (74); Diffusion / flow (73); Agents / tool use (62); Compression / efficiency (57); Reasoning / test-time compute (47); Bayesian / probabilistic (22)
Evidence-coded evaluation settings: theory/synthetic (122); vision/video (108); language/llm (64); math/code/verifiable (48); security/safety (37); robotics/embodied (27); science/domain (21)

Representative/high-signal papers:
- Which Algorithms Can Graph Neural Networks Learn? (oral); votes 7
- Foundations of Equivariant Deep Learning: Unifying Graph and Sheaf Neural Networks (oral); votes 0
- Necessary Conditions for Compositional Generalization of Embedding Models (oral); votes 0
- MV-FGAD: Towards Efficient and Effective Federated Graph Anomaly Detection via Multi-view Learning (oral); votes 0
- PhenoBrain: Phenotype-Conditioned Long-Range Communication for Multi-Modal Brain Network Analysis (oral); votes 0
- Towards Hierarchy–Uniformity Equilibrium: Recovering Semantic Depth in Hypergraph Contrastive Learning (oral); votes 0

Public-attention candidates not marked oral/award:
- Deep sequence models tend to memorize geometrically; it is unclear why.; votes 76
- Who Said Neural Networks Aren't Linear?; votes 74
- Thinking with Geometry: Active Geometry Integration for Spatial Reasoning; votes 70
- From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers; votes 62

Program-signal candidates with lower public attention:
- Foundations of Equivariant Deep Learning: Unifying Graph and Sheaf Neural Networks (oral); votes 0
- Necessary Conditions for Compositional Generalization of Embedding Models (oral); votes 0
- MV-FGAD: Towards Efficient and Effective Federated Graph Anomaly Detection via Multi-view Learning (oral); votes 0
- PhenoBrain: Phenotype-Conditioned Long-Range Communication for Multi-Modal Brain Network Analysis (oral); votes 0

### Generative Modeling

Diffusion and flow models are splitting into practical media generation, language alternatives, and sampling theory.

Evidence:
- 379 papers (5.7% of corpus)
- 8 orals and 2 awards
- 8.76 AlphaXiv public votes/paper
- 30.3% GitHub URL share
- 0 of 2 semantic clusters still need taxonomy review
- primary contribution mix: Method / algorithm (101); Benchmark / evaluation (80); Dataset / data resource (65); Theory / proof (59); Position / conceptual (31); System / infrastructure (19); Application / domain study (14); Uncoded (10)
- method-family cues: Diffusion / flow (333); Graphs / geometry (91); Bayesian / probabilistic (89); LLM post-training (82); Transformer / attention (72); Compression / efficiency (60); Agents / tool use (46); RL / policy optimization (39)
- evaluation-setting cues: vision/video (220); theory/synthetic (120); language/llm (83); robotics/embodied (49); security/safety (39); science/domain (36); math/code/verifiable (33)

Fault lines:
- Sampling-theory guarantees versus image/video generation quality and latency.
- Autoregressive generation versus diffusion or flow-based sequence generation.
- Better visual fidelity versus controllability, consistency, and editing reliability.

What to read for:
- Do speedups preserve quality under realistic inference budgets?
- Are theoretical sampling improvements visible in practical model behavior?
- Does generation remain consistent over long videos, edits, or conditional controls?

Subareas: Image/video diffusion and flow generation (243); Diffusion sampling, transport, and inverse problems (136)
Top themes: Diffusion, flow, and generative modeling (353); Multimodal, vision-language, and video (257); Theory, optimization, and sampling (225); Systems, efficiency, and compression (131); Memorization, evaluation, and generalization (126); Safety, alignment, governance, and risk (123); Agents, tools, and computer use (119); RL for LLMs and verifiable rewards (60)
Evidence-coded contribution types: Method / algorithm (101); Benchmark / evaluation (80); Dataset / data resource (65); Theory / proof (59); Position / conceptual (31); System / infrastructure (19); Application / domain study (14); Uncoded (10)
Evidence-coded method families: Diffusion / flow (333); Graphs / geometry (91); Bayesian / probabilistic (89); LLM post-training (82); Transformer / attention (72); Compression / efficiency (60); Agents / tool use (46); RL / policy optimization (39)
Evidence-coded evaluation settings: vision/video (220); theory/synthetic (120); language/llm (83); robotics/embodied (49); security/safety (39); science/domain (36); math/code/verifiable (33)

Representative/high-signal papers:
- A Random Matrix Perspective on the Consistency of Diffusion Models (Outstanding Paper Honorable Mention; oral); votes 14
- High-accuracy sampling for diffusion models and log-concave distributions (Outstanding Paper Award; oral); votes 9
- High-accuracy and dimension-free sampling with diffusions (oral); votes 21
- Transforming Weather Data from Pixel to Latent Space (oral); votes 11
- Rex: A Family of Reversible Exponential (Stochastic) Runge-Kutta Solvers (oral); votes 6
- Error Propagation Mechanisms and Compensation Strategies for Quantized Diffusion Models (oral); votes 3

Public-attention candidates not marked oral/award:
- One-step Latent-free Image Generation with Pixel Mean Flows; votes 214
- Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Video Generation; votes 152
- Dimension-free convergence of diffusion models for approximate Gaussian mixtures; votes 124
- Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression; votes 104

Program-signal candidates with lower public attention:
- Lottery Prior: Randomized Neural Compression for Zero-Shot Inverse Problems (oral); votes 0
- Riemannian Metric Matching for Scalable Geometric Modeling of Distributions (oral); votes 0
- Error Propagation Mechanisms and Compensation Strategies for Quantized Diffusion Models (oral); votes 3
- Rex: A Family of Reversible Exponential (Stochastic) Runge-Kutta Solvers (oral); votes 6

### Reinforcement Learning and Control

Core RL is active but less publicly amplified than LLM-facing RL, with emphasis on offline learning, control, and computation.

Evidence:
- 312 papers (4.7% of corpus)
- 6 orals and 0 awards
- 6.01 AlphaXiv public votes/paper
- 20.5% GitHub URL share
- 0 of 1 semantic clusters still need taxonomy review
- primary contribution mix: Benchmark / evaluation (105); Theory / proof (82); Method / algorithm (53); Position / conceptual (26); System / infrastructure (15); Application / domain study (14); Dataset / data resource (12); Uncoded (5)
- method-family cues: RL / policy optimization (305); Agents / tool use (116); Diffusion / flow (82); Graphs / geometry (48); Compression / efficiency (45); Reasoning / test-time compute (38); LLM post-training (36); Bayesian / probabilistic (27)
- evaluation-setting cues: robotics/embodied (154); theory/synthetic (109); security/safety (50); math/code/verifiable (33); language/llm (30); vision/video (24); science/domain (1)

Fault lines:
- Classical RL/control objectives versus foundation-model-era policy learning.
- Offline and preference-based RL versus online exploration and sample efficiency.
- Theoretical computation limits versus practical robotic/control deployment.

What to read for:
- Does the method require online interaction or strong simulator assumptions?
- How are stability, exploration, and reward misspecification handled?
- Is the contribution algorithmic, theoretical, or a new evaluation/control setting?

Subareas: Core RL, offline RL, and policy optimization (312)
Top themes: RL for LLMs and verifiable rewards (301); Theory, optimization, and sampling (188); Agents, tools, and computer use (176); Memorization, evaluation, and generalization (137); Systems, efficiency, and compression (134); Safety, alignment, governance, and risk (109); Diffusion, flow, and generative modeling (79); Robotics and world models (58)
Evidence-coded contribution types: Benchmark / evaluation (105); Theory / proof (82); Method / algorithm (53); Position / conceptual (26); System / infrastructure (15); Application / domain study (14); Dataset / data resource (12); Uncoded (5)
Evidence-coded method families: RL / policy optimization (305); Agents / tool use (116); Diffusion / flow (82); Graphs / geometry (48); Compression / efficiency (45); Reasoning / test-time compute (38); LLM post-training (36); Bayesian / probabilistic (27)
Evidence-coded evaluation settings: robotics/embodied (154); theory/synthetic (109); security/safety (50); math/code/verifiable (33); language/llm (30); vision/video (24); science/domain (1)

Representative/high-signal papers:
- On Computation and Reinforcement Learning (oral); votes 11
- Learning Human-Robot Collaboration via Heterogeneous-Agent Lyapunov Policy Optimization (oral); votes 10
- Distributional Inverse Reinforcement Learning (oral); votes 5
- Chebyshev Policies and the Mountain Car Problem: Reinforcement Learning for Low-dimensional Control Tasks (oral); votes 3
- Stabilizing the Q-Gradient Field for Policy Smoothness in Actor-Critic Methods (oral); votes 2
- Video-Based Optimal Transport for Feedback-Efficient Offline Preference-Based Reinforcement Learning (oral); votes 0

Public-attention candidates not marked oral/award:
- Reinforcement Learning with Verifiable Rewards: GRPO's Loss, Dynamics, and Success Amplification; votes 305
- Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers; votes 135
- How Does the Lagrangian Guide Safe Reinforcement Learning through Diffusion Models?; votes 119
- Just-In-Time Reinforcement Learning: Continual Learning in LLM Agents Without Gradient Updates; votes 61

Program-signal candidates with lower public attention:
- Video-Based Optimal Transport for Feedback-Efficient Offline Preference-Based Reinforcement Learning (oral); votes 0
- Stabilizing the Q-Gradient Field for Policy Smoothness in Actor-Critic Methods (oral); votes 2
- Chebyshev Policies and the Mountain Car Problem: Reinforcement Learning for Low-dimensional Control Tasks (oral); votes 3
- Distributional Inverse Reinforcement Learning (oral); votes 5

### Robotics, Embodiment, and World Models

Robotics is becoming a high-attention testbed for VLA models, memory, latent actions, and world models.

Evidence:
- 195 papers (2.9% of corpus)
- 4 orals and 0 awards
- 19.19 AlphaXiv public votes/paper
- 37.4% GitHub URL share
- 0 of 1 semantic clusters still need taxonomy review
- primary contribution mix: Benchmark / evaluation (91); Application / domain study (34); Dataset / data resource (24); Method / algorithm (15); Position / conceptual (10); System / infrastructure (10); Theory / proof (9); Uncoded (2)
- method-family cues: RL / policy optimization (104); Agents / tool use (81); Reasoning / test-time compute (59); Diffusion / flow (44); LLM post-training (42); Graphs / geometry (22); Compression / efficiency (21); Transformer / attention (21)
- evaluation-setting cues: robotics/embodied (171); vision/video (130); language/llm (103); theory/synthetic (55); math/code/verifiable (33); security/safety (19); science/domain (17)
- above-baseline public attention density
- above-baseline GitHub URL availability

Fault lines:
- Vision-language-action pretraining versus robot-specific policy learning.
- Latent action/world-model abstractions versus real-world manipulation reliability.
- Benchmark scaling versus sim-to-real and long-horizon generalization.

What to read for:
- Does the model actually improve physical task success or only representation quality?
- Are actions, memory, and world states evaluated under distribution shift?
- How much depends on synthetic data, simulation, or curated demonstrations?

Subareas: Vision-language-action models and robotic manipulation (195)
Top themes: Robotics and world models (165); Multimodal, vision-language, and video (149); Memorization, evaluation, and generalization (134); Agents, tools, and computer use (102); RL for LLMs and verifiable rewards (76); Systems, efficiency, and compression (71); LLM reasoning and test-time compute (70); Safety, alignment, governance, and risk (53)
Evidence-coded contribution types: Benchmark / evaluation (91); Application / domain study (34); Dataset / data resource (24); Method / algorithm (15); Position / conceptual (10); System / infrastructure (10); Theory / proof (9); Uncoded (2)
Evidence-coded method families: RL / policy optimization (104); Agents / tool use (81); Reasoning / test-time compute (59); Diffusion / flow (44); LLM post-training (42); Graphs / geometry (22); Compression / efficiency (21); Transformer / attention (21)
Evidence-coded evaluation settings: robotics/embodied (171); vision/video (130); language/llm (103); theory/synthetic (55); math/code/verifiable (33); security/safety (19); science/domain (17)

Representative/high-signal papers:
- RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies (oral); votes 66
- From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models (oral); votes 30
- XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations (oral); votes 19
- From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model (oral); votes 14
- Learning Latent Action World Models In The Wild; votes 273
- Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies; votes 204

Public-attention candidates not marked oral/award:
- Learning Latent Action World Models In The Wild; votes 273
- Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies; votes 204
- Temporal Straightening for Latent Planning; votes 202
- LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries; votes 189

Program-signal candidates with lower public attention:
- From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model (oral); votes 14
- XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations (oral); votes 19
- From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models (oral); votes 30
- RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies (oral); votes 66

## Cross-Area Takeaways

- Public attention concentrates in LLM reasoning/RLVR, robotics/VLA, agents, and systems; program signal is more evenly spread across theory, safety, science, and generative modeling.
- GitHub URL availability is highest in applied foundation-model areas and weakest in theory-heavy areas, so artifact coverage should not be interpreted as field quality.
- The highest-value manual review work is no longer finding clusters; it is resolving boundary clusters and turning these fault lines into paper-level claims.

## Caveats

- Fault lines are synthesis prompts grounded in taxonomy statistics and representative titles, not final literature-review conclusions.
- AlphaXiv public votes are attention signals, not quality labels.
- Oral/award labels are program signals, but they do not exhaust paper quality or importance.
- Taxonomy areas inherit the `needs_review` flags from the manual taxonomy seed.