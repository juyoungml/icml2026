# ICML 2026 Manual Taxonomy Seed

This is a curated seed taxonomy built on top of transformer semantic clusters.
It is designed for researcher review, not as a final ontology.

## Snapshot

- Papers assigned: 6,628
- Semantic clusters mapped: 42
- Research areas: 12
- Stable seed clusters: 21
- Clusters needing review: 21

## Area Map

### LLM Reasoning, Post-Training, and RLVR
- Size: 1099 papers (16.6%); orals: 36; awards: 2; votes/paper: 18.55; GitHub URL share: 31.8%
- Subareas: General LLM training, evaluation, and alignment (290); Reasoning models and chain-of-thought behavior (211); Reward modeling, preference feedback, and RL post-training (164); RL for reasoning models and verifiable rewards (161); Diffusion language models and decoding (145); LLM preference tuning and alignment training (128)
- Topic groups: Deep Learning (668); Social Aspects (101); Unknown (98); Applications (78); Reinforcement Learning (77); General Machine Learning (45); Theory (19); Probabilistic Methods (9)
- Representative papers:
  - How much can language models memorize?
  - The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models
  - Maximum Likelihood Reinforcement Learning
  - Reinforcement Learning with Evolving Rubrics for Deep Research
  - Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers
  - WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference

### Multimodal, Vision, and Perception
- Size: 889 papers (13.4%); orals: 13; awards: 1; votes/paper: 7.25; GitHub URL share: 29.5%
- Subareas: Vision-language reasoning and video understanding (272); Multimodal representation and cross-modal alignment (237); 3D, video, motion, and spatial understanding (203); Vision robustness, detection, and adversarial perception (177)
- Topic groups: Applications (430); Deep Learning (265); Unknown (81); General Machine Learning (52); Social Aspects (51); Reinforcement Learning (6); Optimization (2); Theory (2)
- Representative papers:
  - Motion Attribution for Video Generation
  - Holi-Spatial: Evolving Video Streams into Holistic 3D Spatial Intelligence
  - Bad Seeing or Bad Thinking? Rewarding Perception for Multimodal Reasoning
  - Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination
  - 3ViewSense: Spatial and Mental Perspective Reasoning from Orthographic Views in Vision-Language Models
  - CLEAR: Context-Aware Learning with End-to-End Mask-Free Inference for Adaptive Subtitle Removal

### Theory, Optimization, and Algorithms
- Size: 737 papers (11.1%); orals: 27; awards: 1; votes/paper: 4.21; GitHub URL share: 11.8%
- Subareas: Statistical learning theory and regression (180); Online learning, bandits, and regret (172); Convex, stochastic, and nonconvex optimization (127); Bayesian and probabilistic methods (125); Transformer theory and attention expressivity (98); Quantum, matrix, and numerical optimization (35)
- Topic groups: Theory (233); Optimization (105); Probabilistic Methods (101); Deep Learning (100); General Machine Learning (92); Unknown (55); Social Aspects (23); Applications (18)
- Representative papers:
  - To Grok Grokking: Provable Grokking in Ridge Regression
  - Equivalence of Context and Parameter Updates in Modern Transformer Blocks
  - Non-Euclidean Gradient Descent Operates at the Edge of Stability
  - Markov Chain Monte Carlo without Evaluating the Target: an Auxiliary Variable Approach
  - Optimal Decision-Making Based on Prediction Sets
  - Rational Transductors

### AI for Science, Health, and Neuro
- Size: 587 papers (8.9%); orals: 16; awards: 0; votes/paper: 3.01; GitHub URL share: 19.4%
- Subareas: Time series and forecasting applications (160); Protein, molecule, and biological modeling (148); Physical sciences, chemistry, and climate (128); Latent dynamics, neuroscience, and dynamical systems (84); Spiking neural networks and neural signals (67)
- Topic groups: Applications (384); Deep Learning (103); General Machine Learning (37); Unknown (26); Probabilistic Methods (12); Theory (12); Social Aspects (9); Optimization (3)
- Representative papers:
  - Protein Autoregressive Modeling via Multiscale Structure Generation
  - dnaHNet: A Scalable and Hierarchical Foundation Model for Genomic Sequence Learning
  - Orthogonal Concept Erasure for Diffusion Models
  - LASER: Learning Active Sensing for Continuum Field Reconstruction
  - From Text to Forecasts: Bridging Modality Gap with Temporal Evolution Semantic Space
  - Protein Fold Classification at Scale: Benchmarking and Pretraining

### Data-Centric, Causal, and Federated ML
- Size: 526 papers (7.9%); orals: 10; awards: 0; votes/paper: 5.82; GitHub URL share: 16.4%
- Subareas: Labels, datasets, and supervised data quality (192); Continual learning, forgetting, and task adaptation (138); Causal inference and causal discovery (111); Federated learning and distributed clients (85)
- Topic groups: General Machine Learning (227); Deep Learning (110); Social Aspects (53); Applications (52); Unknown (45); Theory (18); Optimization (11); Probabilistic Methods (7)
- Representative papers:
  - Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning
  - Midtraining Bridges Pretraining and Posttraining Distributions
  - Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models
  - DISCO: Mitigating Bias in Deep Learning with Conditional Distance Correlation
  - Exact Functional ANOVA Decomposition for Categorical Inputs
  - A Recursive Decomposition Framework for Causal Structure Learning in the Presence of Latent Variables

### Systems and Efficient Foundation Models
- Size: 515 papers (7.8%); orals: 9; awards: 0; votes/paper: 11.97; GitHub URL share: 24.5%
- Subareas: Large-scale training, optimizers, and model architecture (198); Serving, GPU memory, MoE, and throughput (116); Long-context attention and KV-cache compression (113); Quantization and low-precision training/inference (88)
- Topic groups: Deep Learning (314); General Machine Learning (53); Unknown (52); Optimization (40); Applications (29); Theory (16); Social Aspects (8); Reinforcement Learning (2)
- Representative papers:
  - Controlled LLM Training on Spectral Sphere
  - POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation
  - FlashSinkhorn: IO-Aware Entropic Optimal Transport on GPU
  - ECHO: Elastic Speculative Decoding with Sparse Gating for High-Concurrency Scenarios
  - FlashSketch: Sketch-Kernel Co-Design for Fast Sparse Sketching on GPUs
  - MuonSSM: Orthogonalizing State Space Models for Sequence Modeling

### Safety, Governance, Privacy, and Society
- Size: 502 papers (7.6%); orals: 18; awards: 3; votes/paper: 4.64; GitHub URL share: 19.9%
- Subareas: Adversarial safety, attacks, and security (245); Position papers, policy, and social impacts (173); Privacy, differential privacy, and unlearning (84)
- Topic groups: Social Aspects (349); Deep Learning (48); Unknown (43); Applications (25); General Machine Learning (20); Theory (10); Reinforcement Learning (6); Probabilistic Methods (1)
- Representative papers:
  - The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes
  - Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit
  - Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII)
  - Position: Anthropomorphic Misalignment Research Needs Stronger Evidence
  - Position: Stop Automating Peer Review Without Rigorous Evaluation
  - Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking

### Agents, Code, and Tool Use
- Size: 496 papers (7.5%); orals: 15; awards: 0; votes/paper: 13.87; GitHub URL share: 32.9%
- Subareas: Agent evaluation, tool use, and agentic workflows (207); Multi-agent search, planning, and coordination (150); Code LLMs, verification, and software tasks (139)
- Topic groups: Deep Learning (198); Applications (88); General Machine Learning (64); Unknown (60); Reinforcement Learning (32); Social Aspects (23); Optimization (22); Probabilistic Methods (5)
- Representative papers:
  - $\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment
  - Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning
  - daVinci-Dev: Agent-native Mid-training for Software Engineering
  - Monitoring Monitorability
  - Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections
  - CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability

### Graphs, Geometry, and Representation Learning
- Size: 391 papers (5.9%); orals: 6; awards: 0; votes/paper: 3.51; GitHub URL share: 19.4%
- Subareas: Graph neural networks and graph learning (166); Geometric representation learning and manifolds (160); Equivariant graph and geometric networks (65)
- Topic groups: Deep Learning (210); General Machine Learning (66); Applications (46); Unknown (34); Optimization (13); Social Aspects (12); Theory (8); Probabilistic Methods (2)
- Representative papers:
  - Which Algorithms Can Graph Neural Networks Learn?
  - MV-FGAD: Towards Efficient and Effective Federated Graph Anomaly Detection via Multi-view Learning
  - PhenoBrain: Phenotype-Conditioned Long-Range Communication for Multi-Modal Brain Network Analysis
  - Necessary Conditions for Compositional Generalization of Embedding Models
  - Towards Hierarchy–Uniformity Equilibrium: Recovering Semantic Depth in Hypergraph Contrastive Learning
  - Foundations of Equivariant Deep Learning: Unifying Graph and Sheaf Neural Networks

### Generative Modeling
- Size: 379 papers (5.7%); orals: 8; awards: 2; votes/paper: 8.76; GitHub URL share: 30.3%
- Subareas: Image/video diffusion and flow generation (243); Diffusion sampling, transport, and inverse problems (136)
- Topic groups: Deep Learning (203); Applications (71); Unknown (33); Probabilistic Methods (27); Theory (16); General Machine Learning (11); Social Aspects (10); Optimization (8)
- Representative papers:
  - A Random Matrix Perspective on the Consistency of Diffusion Models
  - High-accuracy sampling for diffusion models and log-concave distributions
  - High-accuracy and dimension-free sampling with diffusions
  - Transforming Weather Data from Pixel to Latent Space
  - Rex: A Family of Reversible Exponential (Stochastic) Runge-Kutta Solvers
  - Error Propagation Mechanisms and Compensation Strategies for Quantized Diffusion Models

### Reinforcement Learning and Control
- Size: 312 papers (4.7%); orals: 6; awards: 0; votes/paper: 6.01; GitHub URL share: 20.5%
- Subareas: Core RL, offline RL, and policy optimization (312)
- Topic groups: Reinforcement Learning (222); Theory (34); Applications (18); Unknown (18); Deep Learning (7); General Machine Learning (4); Optimization (4); Social Aspects (3)
- Representative papers:
  - On Computation and Reinforcement Learning
  - Learning Human-Robot Collaboration via Heterogeneous-Agent Lyapunov Policy Optimization
  - Distributional Inverse Reinforcement Learning
  - Chebyshev Policies and the Mountain Car Problem: Reinforcement Learning for Low-dimensional Control Tasks
  - Stabilizing the Q-Gradient Field for Policy Smoothness in Actor-Critic Methods
  - Video-Based Optimal Transport for Feedback-Efficient Offline Preference-Based Reinforcement Learning

### Robotics, Embodiment, and World Models
- Size: 195 papers (2.9%); orals: 4; awards: 0; votes/paper: 19.19; GitHub URL share: 37.4%
- Subareas: Vision-language-action models and robotic manipulation (195)
- Topic groups: Applications (135); Unknown (23); Reinforcement Learning (17); Deep Learning (15); General Machine Learning (3); Social Aspects (1); Theory (1)
- Representative papers:
  - RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies
  - From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models
  - XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations
  - From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model
  - Learning Latent Action World Models In The Wild
  - Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies

## Clusters Needing Manual Review

- Cluster 1 -> AI for Science, Health, and Neuro / Spiking neural networks and neural signals: manual confidence not high; small cluster (67 papers; auto label: spiking / snns / spiking neural / spike)
- Cluster 2 -> LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training: split across lexical clusters (164 papers; auto label: reward / reinforcement learning / reinforcement / rewards)
- Cluster 6 -> Agents, Code, and Tool Use / Code LLMs, verification, and software tasks: manual confidence not high; split across lexical clusters (139 papers; auto label: code / language / llms / verification)
- Cluster 7 -> Theory, Optimization, and Algorithms / Statistical learning theory and regression: split across lexical clusters (180 papers; auto label: theory / regression / bounds / risk)
- Cluster 10 -> Data-Centric, Causal, and Federated ML / Continual learning, forgetting, and task adaptation: manual confidence not high; split across lexical clusters (138 papers; auto label: continual / forgetting / continual learning / task)
- Cluster 11 -> LLM Reasoning, Post-Training, and RLVR / Reasoning models and chain-of-thought behavior: split across lexical clusters (211 papers; auto label: reasoning / language / large language / language models)
- Cluster 13 -> AI for Science, Health, and Neuro / Latent dynamics, neuroscience, and dynamical systems: manual confidence not high; split across lexical clusters (84 papers; auto label: dynamics / networks / latent / dynamical)
- Cluster 14 -> LLM Reasoning, Post-Training, and RLVR / Diffusion language models and decoding: split across lexical clusters (145 papers; auto label: decoding / diffusion / language / language models)
- Cluster 17 -> Data-Centric, Causal, and Federated ML / Labels, datasets, and supervised data quality: manual confidence not high; split across lexical clusters (192 papers; auto label: label / labels / machine / machine learning)
- Cluster 18 -> Graphs, Geometry, and Representation Learning / Geometric representation learning and manifolds: split across lexical clusters (160 papers; auto label: geometric / representation / geometry / representations)
- Cluster 20 -> Theory, Optimization, and Algorithms / Transformer theory and attention expressivity: manual confidence not high (98 papers; auto label: transformers / attention / transformer / softmax)
- Cluster 21 -> LLM Reasoning, Post-Training, and RLVR / LLM preference tuning and alignment training: manual confidence not high; split across lexical clusters (128 papers; auto label: language / large language / language models / large)
- Cluster 24 -> LLM Reasoning, Post-Training, and RLVR / General LLM training, evaluation, and alignment: manual confidence not high; split across lexical clusters (290 papers; auto label: language / language models / llms / large language)
- Cluster 26 -> Systems and Efficient Foundation Models / Large-scale training, optimizers, and model architecture: manual confidence not high; split across lexical clusters (198 papers; auto label: networks / training / deep / gradient)
- Cluster 27 -> AI for Science, Health, and Neuro / Protein, molecule, and biological modeling: split across lexical clusters (148 papers; auto label: protein / molecular / chemistry / applications)
- Cluster 30 -> Agents, Code, and Tool Use / Multi-agent search, planning, and coordination: split across lexical clusters (150 papers; auto label: agent / multi / search / agents)
- Cluster 31 -> Data-Centric, Causal, and Federated ML / Federated learning and distributed clients: split across lexical clusters (85 papers; auto label: federated / federated learning / clients / client)
- Cluster 36 -> Multimodal, Vision, and Perception / Vision robustness, detection, and adversarial perception: manual confidence not high; split across lexical clusters (177 papers; auto label: detection / vision / image / robustness)
- Cluster 38 -> Theory, Optimization, and Algorithms / Quantum, matrix, and numerical optimization: manual confidence not high; small cluster (35 papers; auto label: quantum / matrix / optimization / algorithm)
- Cluster 39 -> AI for Science, Health, and Neuro / Time series and forecasting applications: manual confidence not high (160 papers; auto label: time series / series / forecasting / time)
- Cluster 41 -> Graphs, Geometry, and Representation Learning / Equivariant graph and geometric networks: small cluster (65 papers; auto label: graph / networks / neural networks / graph neural)

## How To Use This

- Treat `area` as the current report-level taxonomy and `subarea` as a review queue.
- Start manual review with clusters marked `needs_review`, especially medium-confidence clusters that split across lexical clusters.
- When a subarea is renamed or moved, edit the `TAXONOMY` mapping in `scripts/build_manual_taxonomy_seed.py` and regenerate outputs.
- Do not cite this taxonomy as ground truth without manual paper review of representative and boundary papers.