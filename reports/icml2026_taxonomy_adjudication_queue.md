# ICML 2026 Taxonomy Adjudication Queue

Cluster-level queue for resolving taxonomy boundaries before using subarea-level landscape claims.
This does not change the taxonomy; it prioritizes what a human should adjudicate first.

## Snapshot

- Clusters needing adjudication: 21
- Queued paper-review rows covered: 78
- Area mix: LLM Reasoning, Post-Training, and RLVR: 5, AI for Science, Health, and Neuro: 4, Data-Centric, Causal, and Federated ML: 3, Theory, Optimization, and Algorithms: 3, Agents, Code, and Tool Use: 2, Graphs, Geometry, and Representation Learning: 2, Systems and Efficient Foundation Models: 1, Multimodal, Vision, and Perception: 1

## Top Adjudication Targets

| Rank | Cluster | Current area/subarea | Why review | Queued papers | Decision prompt |
| ---: | --- | --- | --- | ---: | --- |
| 1 | 24: language / language models / llms / large language | LLM Reasoning, Post-Training, and RLVR / General LLM training, evaluation, and alignment | manual confidence not high; split across lexical clusters | 5 | Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood. |
| 2 | 10: continual / forgetting / continual learning / task | Data-Centric, Causal, and Federated ML / Continual learning, forgetting, and task adaptation | manual confidence not high; split across lexical clusters | 9 | Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood. |
| 3 | 11: reasoning / language / large language / language models | LLM Reasoning, Post-Training, and RLVR / Reasoning models and chain-of-thought behavior | split across lexical clusters | 3 | Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood. |
| 4 | 26: networks / training / deep / gradient | Systems and Efficient Foundation Models / Large-scale training, optimizers, and model architecture | manual confidence not high; split across lexical clusters | 8 | Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood. |
| 5 | 20: transformers / attention / transformer / softmax | Theory, Optimization, and Algorithms / Transformer theory and attention expressivity | manual confidence not high | 7 | Decide whether current area/subarea is central enough or should be relabeled. |
| 6 | 2: reward / reinforcement learning / reinforcement / rewards | LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training | split across lexical clusters | 5 | Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood. |
| 7 | 30: agent / multi / search / agents | Agents, Code, and Tool Use / Multi-agent search, planning, and coordination | split across lexical clusters | 5 | Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood. |
| 8 | 13: dynamics / networks / latent / dynamical | AI for Science, Health, and Neuro / Latent dynamics, neuroscience, and dynamical systems | manual confidence not high; split across lexical clusters | 5 | Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood. |
| 9 | 14: decoding / diffusion / language / language models | LLM Reasoning, Post-Training, and RLVR / Diffusion language models and decoding | split across lexical clusters | 2 | Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood. |
| 10 | 18: geometric / representation / geometry / representations | Graphs, Geometry, and Representation Learning / Geometric representation learning and manifolds | split across lexical clusters | 8 | Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood. |
| 11 | 36: detection / vision / image / robustness | Multimodal, Vision, and Perception / Vision robustness, detection, and adversarial perception | manual confidence not high; split across lexical clusters | 4 | Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood. |
| 12 | 39: time series / series / forecasting / time | AI for Science, Health, and Neuro / Time series and forecasting applications | manual confidence not high | 4 | Decide whether current area/subarea is central enough or should be relabeled. |
| 13 | 27: protein / molecular / chemistry / applications | AI for Science, Health, and Neuro / Protein, molecule, and biological modeling | split across lexical clusters | 3 | Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood. |
| 14 | 7: theory / regression / bounds / risk | Theory, Optimization, and Algorithms / Statistical learning theory and regression | split across lexical clusters | 2 | Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood. |
| 15 | 21: language / large language / language models / large | LLM Reasoning, Post-Training, and RLVR / LLM preference tuning and alignment training | manual confidence not high; split across lexical clusters | 0 | Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood. |
| 16 | 17: label / labels / machine / machine learning | Data-Centric, Causal, and Federated ML / Labels, datasets, and supervised data quality | manual confidence not high; split across lexical clusters | 2 | Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood. |
| 17 | 41: graph / networks / neural networks / graph neural | Graphs, Geometry, and Representation Learning / Equivariant graph and geometric networks | small cluster | 4 | Small cluster: decide whether to merge into a broader subarea or keep as distinct. |
| 18 | 6: code / language / llms / verification | Agents, Code, and Tool Use / Code LLMs, verification, and software tasks | manual confidence not high; split across lexical clusters | 0 | Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood. |
| 19 | 38: quantum / matrix / optimization / algorithm | Theory, Optimization, and Algorithms / Quantum, matrix, and numerical optimization | manual confidence not high; small cluster | 0 | Decide whether current area/subarea is central enough or should be relabeled. |
| 20 | 1: spiking / snns / spiking neural / spike | AI for Science, Health, and Neuro / Spiking neural networks and neural signals | manual confidence not high; small cluster | 1 | Decide whether current area/subarea is central enough or should be relabeled. |

## Cluster Details

### 1. Cluster 24: language / language models / llms / large language

- Current mapping: LLM Reasoning, Post-Training, and RLVR / General LLM training, evaluation, and alignment
- Review notes: manual confidence not high; split across lexical clusters
- Papers: 290; orals: 14; awards: 0; votes/paper: 8.76
- Top terms: language; language models; llms; large language; large; llm; models llms; alignment; learning large; training; evaluation; data; fine; knowledge; deep learning; tuning
- Top topic groups: Deep Learning (143); Social Aspects (65); Applications (32); General Machine Learning (21); Unknown (21)
- Queued papers to read: Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers | Diffract: Spectral View of LLM Domain Adaptation | FlatLand: Personalized Graph Federated Learning via Tailored Lorentz Space | Information Flow Reveals When to Trust Language Models | On the Limits of LLM Adaptability: Impact of LLM Pre-Training on Annotation Task Performance
- High-signal papers: Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers | Prescriptive Scaling Reveals the Evolution of Language Model Capabilities | Less is Enough: Synthesizing Diverse Data in Feature Space of LLMs | Mechanistic Data Attribution: Tracing the Training Origins of Interpretable LLM Units | Simultaneous Speech-to-Speech Translation Without Aligned Data | Procedural Pretraining: Warming Up Language Models with Abstract Data | TokSuite: Measuring the Impact of Tokenizer Choice on Language Model Behavior | VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment in Large Language Models
- Decision prompt: Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood.

### 2. Cluster 10: continual / forgetting / continual learning / task

- Current mapping: Data-Centric, Causal, and Federated ML / Continual learning, forgetting, and task adaptation
- Review notes: manual confidence not high; split across lexical clusters
- Papers: 138; orals: 4; awards: 0; votes/paper: 16.38
- Top terms: continual; forgetting; continual learning; task; knowledge; tasks; attention; catastrophic forgetting; catastrophic; plasticity; memory; new; parameter; updates; transfer; performance
- Top topic groups: Deep Learning (68); General Machine Learning (37); Unknown (15); Theory (7); Applications (7)
- Queued papers to read: Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning | Midtraining Bridges Pretraining and Posttraining Distributions | Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models | Self-Distillation Enables Continual Learning | Understanding LoRA as Knowledge Memory: An Empirical Analysis | ATLAS: Learning to Optimally Memorize the Context at Test Time | Retaining by Doing: The Role of On-Policy Data in Mitigating Forgetting | Detecting the Semantic Fixed Point: A Geometric Framework for Efficient Inference
- High-signal papers: Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning | Midtraining Bridges Pretraining and Posttraining Distributions | Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models | Detecting the Semantic Fixed Point: A Geometric Framework for Efficient Inference | Self-Distillation Enables Continual Learning | Understanding LoRA as Knowledge Memory: An Empirical Analysis | ATLAS: Learning to Optimally Memorize the Context at Test Time | Retaining by Doing: The Role of On-Policy Data in Mitigating Forgetting
- Decision prompt: Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood.

### 3. Cluster 11: reasoning / language / large language / language models

- Current mapping: LLM Reasoning, Post-Training, and RLVR / Reasoning models and chain-of-thought behavior
- Review notes: split across lexical clusters
- Papers: 211; orals: 10; awards: 1; votes/paper: 18.32
- Top terms: reasoning; language; large language; language models; large; llms; learning large; thought; deep; deep learning; cot; reasoning models; chain; latent; tasks; chain thought
- Top topic groups: Deep Learning (152); Applications (18); Unknown (17); Social Aspects (14); General Machine Learning (7)
- Queued papers to read: The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models | Latent Collaboration in Multi-Agent Systems | Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models
- High-signal papers: The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models | Learning to Theorize the World from Observation | Characterizing, Evaluating, and Optimizing Complex Reasoning | Towards Long-Horizon Interpretability: Efficient and Faithful Multi-Token Attribution for Reasoning LLMs | Skip a Layer or Loop It? Learning Program-of-Layers in LLMs | The Signal is in the Steps: Local Scoring for Reasoning Data Selection | Modeling Hierarchical Thinking in Large Reasoning Models | Evaluating Robustness of Reasoning Models on Parameterized Logical Problems
- Decision prompt: Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood.

### 4. Cluster 26: networks / training / deep / gradient

- Current mapping: Systems and Efficient Foundation Models / Large-scale training, optimizers, and model architecture
- Review notes: manual confidence not high; split across lexical clusters
- Papers: 198; orals: 2; awards: 0; votes/paper: 13.31
- Top terms: neural; networks; training; deep; gradient; optimization; deep learning; neural networks; network; architectures; layer; loss; optimizer; updates; low; muon
- Top topic groups: Deep Learning (109); Optimization (26); General Machine Learning (17); Unknown (16); Theory (14)
- Queued papers to read: Controlled LLM Training on Spectral Sphere | MuonSSM: Orthogonalizing State Space Models for Sequence Modeling | mHC: Manifold-Constrained Hyper-Connections | Evolution Strategies at the Hyperscale | Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights | NorMuon: Making Muon more efficient and scalable | GradientStabilizer: Fix the Norm, Not the Gradient | Why Do We Need Warm-up? A Theoretical Perspective
- High-signal papers: Controlled LLM Training on Spectral Sphere | MuonSSM: Orthogonalizing State Space Models for Sequence Modeling | mHC: Manifold-Constrained Hyper-Connections | Evolution Strategies at the Hyperscale | Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights | NorMuon: Making Muon more efficient and scalable | GradientStabilizer: Fix the Norm, Not the Gradient | Why Do We Need Warm-up? A Theoretical Perspective
- Decision prompt: Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood.

### 5. Cluster 20: transformers / attention / transformer / softmax

- Current mapping: Theory, Optimization, and Algorithms / Transformer theory and attention expressivity
- Review notes: manual confidence not high
- Papers: 98; orals: 5; awards: 0; votes/paper: 12.92
- Top terms: transformers; attention; transformer; softmax; theory; deep; deep learning; context; layer; length; language; results; softmax attention; training; scaling; layers
- Top topic groups: Deep Learning (64); Theory (20); Unknown (8); Social Aspects (3); General Machine Learning (2)
- Queued papers to read: Equivalence of Context and Parameter Updates in Modern Transformer Blocks | Rational Transductors | Dimensional Collapse in Transformer Attention Outputs: A Challenge for Sparse Dictionary Learning | Weight-sparse transformers have interpretable circuits | You Need Better Attention Priors | Do Transformers Need Three Projections? Systematic Study of QKV Variants | Patterning: The Dual of Interpretability
- High-signal papers: Equivalence of Context and Parameter Updates in Modern Transformer Blocks | Rational Transductors | Focus and Dilution: The Multi-stage Learning Process of Attention | On Minimum Depth and Width of Floating-Point Neural Networks for Representing Floating-Point Functions | The Expressivity Limits of Transformers | Dimensional Collapse in Transformer Attention Outputs: A Challenge for Sparse Dictionary Learning | Weight-sparse transformers have interpretable circuits | You Need Better Attention Priors
- Decision prompt: Decide whether current area/subarea is central enough or should be relabeled.

### 6. Cluster 2: reward / reinforcement learning / reinforcement / rewards

- Current mapping: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Review notes: split across lexical clusters
- Papers: 164; orals: 3; awards: 0; votes/paper: 27.48
- Top terms: reward; reinforcement learning; reinforcement; rewards; policy; rl; preference; feedback; training; language; optimization; human; large language; language models; reward models; large
- Top topic groups: Deep Learning (71); Reinforcement Learning (51); Unknown (14); Social Aspects (12); Applications (10)
- Queued papers to read: Maximum Likelihood Reinforcement Learning | Reinforcement Learning with Evolving Rubrics for Deep Research | Reinforcement Learning via Self-Distillation | Agent Learning via Early Experience | GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization
- High-signal papers: Maximum Likelihood Reinforcement Learning | Reinforcement Learning with Evolving Rubrics for Deep Research | Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling | Reinforcement Learning via Self-Distillation | Agent Learning via Early Experience | GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization | Training AI Co-Scientists Using Rubric Rewards | RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System
- Decision prompt: Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood.

### 7. Cluster 30: agent / multi / search / agents

- Current mapping: Agents, Code, and Tool Use / Multi-agent search, planning, and coordination
- Review notes: split across lexical clusters
- Papers: 150; orals: 4; awards: 0; votes/paper: 16.96
- Top terms: agent; multi; search; agents; optimization; llm; multi agent; language; large language; large; based; task; planning; language models; reinforcement; evolutionary
- Top topic groups: Deep Learning (78); Optimization (18); Reinforcement Learning (18); General Machine Learning (12); Unknown (12)
- Queued papers to read: Learning to Discover at Test Time | MemEvolve: Meta-Evolution of Agent Memory Systems | Unsupervised Partner Design Enables Robust Ad-hoc Teamwork | Scaling Long-Horizon Agent via Context Folding | Meta Context Engineering via Agentic Skill Evolution
- High-signal papers: OMAC: A Holistic Optimization Framework for LLM-Based Multi-Agent Collaboration | Guaranteed Optimal Compositional Explanations for Neurons | From Feasible to Practical: Pareto-Optimal Synthesis Planning | Unsupervised Partner Design Enables Robust Ad-hoc Teamwork | Learning to Discover at Test Time | MemEvolve: Meta-Evolution of Agent Memory Systems | Scaling Long-Horizon Agent via Context Folding | Meta Context Engineering via Agentic Skill Evolution
- Decision prompt: Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood.

### 8. Cluster 13: dynamics / networks / latent / dynamical

- Current mapping: AI for Science, Health, and Neuro / Latent dynamics, neuroscience, and dynamical systems
- Review notes: manual confidence not high; split across lexical clusters
- Papers: 84; orals: 4; awards: 0; votes/paper: 3.19
- Top terms: neural; dynamics; networks; latent; dynamical; time; structure; theory; neural networks; gradient; continuous; systems; linear; neuroscience; cognitive; flow
- Top topic groups: Deep Learning (27); Applications (25); Theory (9); General Machine Learning (9); Probabilistic Methods (5)
- Queued papers to read: Orthogonal Concept Erasure for Diffusion Models | AI Engram: In Search of Memory Traces in Artificial Intelligence | CoEvol-NO: State and Coordinate Co-Evolution with an Error-Driven Predictor-Corrector Paradigm for Neural Operator Transformer | Geometric Flow Grounding: A Unified Manifold Decoupling Framework for Dynamics Discovery and Verification | Universal Learning of Nonlinear Dynamics
- High-signal papers: Orthogonal Concept Erasure for Diffusion Models | AI Engram: In Search of Memory Traces in Artificial Intelligence | CoEvol-NO: State and Coordinate Co-Evolution with an Error-Driven Predictor-Corrector Paradigm for Neural Operator Transformer | Geometric Flow Grounding: A Unified Manifold Decoupling Framework for Dynamics Discovery and Verification | Universal Learning of Nonlinear Dynamics | Robust Filter Attention: Self-Attention as a Parallel State Estimator | The Geometric Mechanics of Contrastive Representation Learning: Alignment Potentials, Entropic Dispersion, and Cross-Modal Divergence | A Solvable High-Dimensional Model Where Nonlinear Autoencoders Learn Structure Invisible to PCA While Test Loss Misaligns With Generalization
- Decision prompt: Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood.

### 9. Cluster 14: decoding / diffusion / language / language models

- Current mapping: LLM Reasoning, Post-Training, and RLVR / Diffusion language models and decoding
- Review notes: split across lexical clusters
- Papers: 145; orals: 5; awards: 1; votes/paper: 14.32
- Top terms: decoding; diffusion; language; language models; token; tokens; generation; diffusion language; autoregressive; large language; dllms; parallel; large; masked; inference; deep learning
- Top topic groups: Deep Learning (111); Unknown (18); General Machine Learning (4); Applications (4); Probabilistic Methods (3)
- Queued papers to read: How much can language models memorize? | WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference
- High-signal papers: How much can language models memorize? | WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference | OPUS: Towards Efficient and Principled Data Selection in Large Language Model Pre-training in Every Iteration | Learning Unmasking Policies for Diffusion Language Models | Any-Order GPT as Masked Diffusion Model: Decoupling Formulation and Architecture | DFlash: Block Diffusion for Flash Speculative Decoding | Predicting the Order of Upcoming Tokens Improves Language Modeling | Coevolutionary Continuous Discrete Diffusion: Make Your Diffusion Language Model a Latent Reasoner
- Decision prompt: Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood.

### 10. Cluster 18: geometric / representation / geometry / representations

- Current mapping: Graphs, Geometry, and Representation Learning / Geometric representation learning and manifolds
- Review notes: split across lexical clusters
- Papers: 160; orals: 1; awards: 0; votes/paper: 5.36
- Top terms: geometric; representation; geometry; representations; representation learning; manifold; spatial; alignment; space; learning representation; clustering; latent; embedding; structure; global; structures
- Top topic groups: Deep Learning (58); General Machine Learning (40); Applications (37); Unknown (15); Social Aspects (7)
- Queued papers to read: Necessary Conditions for Compositional Generalization of Embedding Models | Deep sequence models tend to memorize geometrically; it is unclear why. | Thinking with Geometry: Active Geometry Integration for Spatial Reasoning | From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers | Revisiting the Platonic Representation Hypothesis: An Aristotelian View | A Deep Learning Model of Mental Rotation Informed by Interactive VR Experiments | Semantic Tube Prediction: Beating LLM Data Efficiency with JEPA | From Directions to Regions: Decomposing Activations in Language Models via Local Geometry
- High-signal papers: Necessary Conditions for Compositional Generalization of Embedding Models | Deep sequence models tend to memorize geometrically; it is unclear why. | Thinking with Geometry: Active Geometry Integration for Spatial Reasoning | From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers | Revisiting the Platonic Representation Hypothesis: An Aristotelian View | A Deep Learning Model of Mental Rotation Informed by Interactive VR Experiments | Semantic Tube Prediction: Beating LLM Data Efficiency with JEPA | From Directions to Regions: Decomposing Activations in Language Models via Local Geometry
- Decision prompt: Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood.

### 11. Cluster 36: detection / vision / image / robustness

- Current mapping: Multimodal, Vision, and Perception / Vision robustness, detection, and adversarial perception
- Review notes: manual confidence not high; split across lexical clusters
- Papers: 177; orals: 3; awards: 0; votes/paper: 2.95
- Top terms: detection; vision; image; robustness; computer vision; computer; applications computer; adversarial; feature; semantic; methods; applications; images; extensive; features; performance
- Top topic groups: Applications (84); Deep Learning (39); Social Aspects (27); General Machine Learning (14); Unknown (12)
- Queued papers to read: DroneDINO: Towards Heterogeneous Routed Mixture of Experts for Drone-based Unified Object Detection | Privacy-Aware Video Anomaly Detection: Guided Orthogonal Projection and a Comprehensive Evaluation Framework | Rectified LpJEPA: Joint-Embedding Predictive Architectures with Sparse and Maximum-Entropy Representations | On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression
- High-signal papers: Mind Your Margin and Boundary: Are Your Distilled Datasets Truly Robust? | DroneDINO: Towards Heterogeneous Routed Mixture of Experts for Drone-based Unified Object Detection | Privacy-Aware Video Anomaly Detection: Guided Orthogonal Projection and a Comprehensive Evaluation Framework | Rectified LpJEPA: Joint-Embedding Predictive Architectures with Sparse and Maximum-Entropy Representations | On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression | Beyond Accuracy: What Matters in Designing Well-Behaved Image Classification Models? | Is Training Necessary for Anomaly Detection? | Alterbute: Editing Intrinsic Attributes of Objects in Images
- Decision prompt: Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood.

### 12. Cluster 39: time series / series / forecasting / time

- Current mapping: AI for Science, Health, and Neuro / Time series and forecasting applications
- Review notes: manual confidence not high
- Papers: 160; orals: 3; awards: 0; votes/paper: 3.11
- Top terms: time series; series; forecasting; time; series forecasting; temporal; applications time; applications; data; real; multivariate; real world; modeling; world; dynamics; datasets
- Top topic groups: Applications (96); Deep Learning (33); General Machine Learning (16); Unknown (7); Social Aspects (6)
- Queued papers to read: From Text to Forecasts: Bridging Modality Gap with Temporal Evolution Semantic Space | TSRBench: A Comprehensive Multi-task Multi-modal Time Series Reasoning Benchmark for Generalist Models | Understanding Self-Supervised Learning via Latent Distribution Matching | OpenTSLM: Time-Series Language Models for Reasoning over Multivariate Medical Text- and Time-Series Data
- High-signal papers: From Text to Forecasts: Bridging Modality Gap with Temporal Evolution Semantic Space | ConFlux: Multivariate Time Series in Flux, One Unified Forecast in Confluence | Scalable Event Cloud Network for Event-based Classification | TSRBench: A Comprehensive Multi-task Multi-modal Time Series Reasoning Benchmark for Generalist Models | Understanding Self-Supervised Learning via Latent Distribution Matching | OpenTSLM: Time-Series Language Models for Reasoning over Multivariate Medical Text- and Time-Series Data | Position: Why a Dynamical Systems Perspective is Needed to Advance Time Series Modeling | StarEmbed: Benchmarking Time Series Foundation Models on Astronomical Observations of Variable Stars
- Decision prompt: Decide whether current area/subarea is central enough or should be relabeled.

### 13. Cluster 27: protein / molecular / chemistry / applications

- Current mapping: AI for Science, Health, and Neuro / Protein, molecule, and biological modeling
- Review notes: split across lexical clusters
- Papers: 148; orals: 5; awards: 0; votes/paper: 2.72
- Top terms: protein; molecular; chemistry; applications; physics; design; physics earth; earth sciences; applications chemistry; chemistry physics; earth; sciences; medicine; structure; applications health; health medicine
- Top topic groups: Applications (120); Deep Learning (13); Unknown (7); General Machine Learning (5); Optimization (1)
- Queued papers to read: Protein Autoregressive Modeling via Multiscale Structure Generation | dnaHNet: A Scalable and Hierarchical Foundation Model for Genomic Sequence Learning | Protein Fold Classification at Scale: Benchmarking and Pretraining
- High-signal papers: Protein Autoregressive Modeling via Multiscale Structure Generation | dnaHNet: A Scalable and Hierarchical Foundation Model for Genomic Sequence Learning | Protein Fold Classification at Scale: Benchmarking and Pretraining | FLIP2: Expanding Protein Fitness Landscape Benchmarks for Real-World Machine Learning Applications | Towards Sub-second Biological Foundation Model Infrastructure: A Quantized Consistency Diffusion Framework for Molecular Docking | Adaptive Protein Tokenization | Contrastive Geometric Learning Unlocks Unified Structure- and Ligand-Based Drug Design | PDFBench: A Benchmark for De Novo Protein Design from Function
- Decision prompt: Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood.

### 14. Cluster 7: theory / regression / bounds / risk

- Current mapping: Theory, Optimization, and Algorithms / Statistical learning theory and regression
- Review notes: split across lexical clusters
- Papers: 180; orals: 4; awards: 1; votes/paper: 2.07
- Top terms: theory; regression; data; bounds; risk; sample; distribution; learning theory; machine; machine learning; error; theory learning; optimal; methods; bound; distributions
- Top topic groups: Theory (73); General Machine Learning (49); Unknown (17); Deep Learning (17); Probabilistic Methods (14)
- Queued papers to read: To Grok Grokking: Provable Grokking in Ridge Regression | Optimal Decision-Making Based on Prediction Sets
- High-signal papers: To Grok Grokking: Provable Grokking in Ridge Regression | Optimal Decision-Making Based on Prediction Sets | Joint Learning in the Gaussian Single Index Model | Mixtures Closest To A Given Measure: A Semidefinite Programming Approach | Multi-Distribution Robust Conformal Prediction | Fast kernel methods: Sobolev, physics-informed, and additive models | Generalization of Gibbs and Langevin Monte Carlo Algorithms in the Interpolation Regime | Logit Distance Bounds Representational Similarity
- Decision prompt: Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood.

### 15. Cluster 21: language / large language / language models / large

- Current mapping: LLM Reasoning, Post-Training, and RLVR / LLM preference tuning and alignment training
- Review notes: manual confidence not high; split across lexical clusters
- Papers: 128; orals: 2; awards: 0; votes/paper: 9.02
- Top terms: language; large language; language models; large; preference; llm; training; llms; policy; learning large; optimization; data; deep learning; deep; dpo; optimal
- Top topic groups: Deep Learning (92); General Machine Learning (8); Unknown (8); Reinforcement Learning (5); Social Aspects (4)
- Queued papers to read: none in area queue
- High-signal papers: Do We Need Adam? Surprisingly Strong and Sparse Reinforcement Learning with SGD in LLMs | Reward-free Alignment for Conflicting Objectives | Rethinking the Trust Region in LLM Reinforcement Learning | Entropy-Aware On-Policy Distillation of Language Models | Autoregressive Language Models are Secretly Energy-Based Models: Insights into the Lookahead Capabilities of Next-Token Prediction | Hybrid Policy Distillation for LLMs | Token-Level LLM Collaboration via FusionRoute | Predictable Compression Failures: Order Sensitivity and Information Budgeting for Evidence-Grounded Binary Adjudication
- Decision prompt: Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood.

### 16. Cluster 17: label / labels / machine / machine learning

- Current mapping: Data-Centric, Causal, and Federated ML / Labels, datasets, and supervised data quality
- Review notes: manual confidence not high; split across lexical clusters
- Papers: 192; orals: 1; awards: 0; votes/paper: 2.38
- Top terms: label; data; labels; machine; machine learning; general machine; class; general; methods; datasets; performance; training; samples; classification; supervised; based
- Top topic groups: General Machine Learning (78); Applications (33); Social Aspects (27); Deep Learning (22); Unknown (17)
- Queued papers to read: On the Difficulty of Learning a Meta-network for Training Data Selection | Extracting alignment data in open models
- High-signal papers: On the Difficulty of Learning a Meta-network for Training Data Selection | Extracting alignment data in open models | CorrSteer: Generation-Time LLM Steering via Correlated Sparse Autoencoder Features | Antidistillation Fingerprinting | Probably Approximately Correct Labels | Building Social World Model with Large Language Models | GENEB: Why Genomic Models Are Hard to Compare | MixtureVitae: Open Web-Scale Pretraining Dataset With High Quality Instruction and Reasoning Data Built from Permissive-First Text Sources
- Decision prompt: Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood.

### 17. Cluster 41: graph / networks / neural networks / graph neural

- Current mapping: Graphs, Geometry, and Representation Learning / Equivariant graph and geometric networks
- Review notes: small cluster
- Papers: 65; orals: 1; awards: 0; votes/paper: 4.51
- Top terms: graph; networks; neural; neural networks; graph neural; gnns; graphs; learning graph; node; network; equivariant; deep; gnn; deep learning; message; message passing
- Top topic groups: Deep Learning (45); Unknown (6); General Machine Learning (5); Applications (5); Theory (2)
- Queued papers to read: Foundations of Equivariant Deep Learning: Unifying Graph and Sheaf Neural Networks | Who Said Neural Networks Aren't Linear? | Dynamics Reveals Structure: Challenging the Linear Propagation Assumption | Learning Multi-Agent Coordination via Sheaf-ADMM
- High-signal papers: Foundations of Equivariant Deep Learning: Unifying Graph and Sheaf Neural Networks | Who Said Neural Networks Aren't Linear? | Dynamics Reveals Structure: Challenging the Linear Propagation Assumption | Learning Multi-Agent Coordination via Sheaf-ADMM | Discovering Symmetry Groups with Flow Matching | Rotary Position Encodings for Graphs | Smoothness Errors in Dynamics Models and How to Avoid Them | Transformers Provably Learn Algorithmic Solutions for Graph Connectivity, But Only with the Right Data
- Decision prompt: Small cluster: decide whether to merge into a broader subarea or keep as distinct.

### 18. Cluster 6: code / language / llms / verification

- Current mapping: Agents, Code, and Tool Use / Code LLMs, verification, and software tasks
- Review notes: manual confidence not high; split across lexical clusters
- Papers: 139; orals: 1; awards: 0; votes/paper: 6.04
- Top terms: code; language; llms; verification; large language; evaluation; llm; language models; large; program; formal; generation; benchmark; reasoning; automated; proof
- Top topic groups: Deep Learning (47); Applications (30); General Machine Learning (21); Unknown (19); Social Aspects (12)
- Queued papers to read: none in area queue
- High-signal papers: SoftJAX & SoftTorch: Empowering Automatic Differentiation Libraries with Informative Gradients | APE-Bench: Evaluating Automated Proof Engineering for Formal Math Libraries | Vibe Checker: Aligning Code Evaluation with Human Preference | SWE-Perf: Can Language Models Optimize Code Performance on Real-World Repositories? | Reasoning over Boundaries: Enhancing Specification Alignment via Test-time Deliberation | Training Language Model Agents to Find Vulnerabilities with CTF-Dojo | Propose, Solve, Verify: Self-Play Through Formal Verification | SERA: Soft-Verified Efficient Repository Agents
- Decision prompt: Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood.

### 19. Cluster 38: quantum / matrix / optimization / algorithm

- Current mapping: Theory, Optimization, and Algorithms / Quantum, matrix, and numerical optimization
- Review notes: manual confidence not high; small cluster
- Papers: 35; orals: 1; awards: 0; votes/paper: 3.09
- Top terms: quantum; matrix; optimization; algorithm; classical; algorithms; problem; quadratic; linear; quantum algorithm; problems; gradient; complexity; quantum computing; gpu; theory
- Top topic groups: Optimization (12); Theory (9); Unknown (4); Deep Learning (3); General Machine Learning (2)
- Queued papers to read: none in area queue
- High-signal papers: Optimal and Scalable MAPF via Multi-Marginal Optimal Transport and Schrödinger Bridges | Ultrafast On-Chip Online Learning via Spline Locality in Kolmogorov–Arnold Networks | Discrete Adjoint Schrödinger Bridge Sampler | Position: Quantum Deep Learning Still Needs a Quantum Leap | Gromov-Wasserstein at Scale, Beyond Squared Norms | Batched First-Order Methods for Parallel LP Solving in MIP | DASH: Faster Shampoo via Batched Block Preconditioning and Efficient Inverse-Root Solvers | A Penalty Approach For Differentiation Through Black-box Quadratic Programming Solvers
- Decision prompt: Decide whether current area/subarea is central enough or should be relabeled.

### 20. Cluster 1: spiking / snns / spiking neural / spike

- Current mapping: AI for Science, Health, and Neuro / Spiking neural networks and neural signals
- Review notes: manual confidence not high; small cluster
- Papers: 67; orals: 0; awards: 0; votes/paper: 1.28
- Top terms: spiking; snns; spiking neural; spike; neural; neuroscience; applications neuroscience; neuroscience cognitive; eeg; cognitive science; cognitive; neural networks; networks; snn; energy; brain
- Top topic groups: Applications (50); Deep Learning (13); General Machine Learning (2); Optimization (1); Unknown (1)
- Queued papers to read: Scaling Vision Transformers for Functional MRI with Flat Maps
- High-signal papers: Scaling Vision Transformers for Functional MRI with Flat Maps | Event2Vec: Processing neuromorphic events directly by representations in vector space | EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation and Diagnostic Analyses of EEG Foundation Models | Omni-fMRI: A Universal Atlas-Free fMRI Foundation Model | DuFal: Dual-Frequency-Aware Learning for High-Fidelity Extremely Sparse-view CBCT Reconstruction | Self-Supervised Foundation Model for Calcium-imaging Population Dynamics | Kuramoto Oscillatory Phase Encoding: Neuro-inspired Synchronization for Improved Learning Efficiency | NAACA: Training-Free NeuroAuditory Attentive Cognitive Architecture with Oscillatory Working Memory for Salience-Driven Attention Gating
- Decision prompt: Decide whether current area/subarea is central enough or should be relabeled.

### 21. Cluster 31: federated / federated learning / clients / client

- Current mapping: Data-Centric, Causal, and Federated ML / Federated learning and distributed clients
- Review notes: split across lexical clusters
- Papers: 85; orals: 1; awards: 0; votes/paper: 1.02
- Top terms: federated; federated learning; clients; client; fl; data; heterogeneity; aggregation; privacy; communication; local; global; learning fl; heterogeneous; personalized; decentralized
- Top topic groups: General Machine Learning (29); Deep Learning (19); Social Aspects (16); Optimization (10); Applications (5)
- Queued papers to read: Incentivizing Truthfulness and Collaborative Fairness in Bayesian Learning
- High-signal papers: Incentivizing Truthfulness and Collaborative Fairness in Bayesian Learning | Delayed Momentum Aggregation: Communication-efficient Byzantine-robust Federated Learning with Partial Participation | PluRel: Synthetic Data unlocks Scaling Laws for Relational Foundation Models | Can Recommender Systems Teach Themselves? A Recursive Self-Improving Framework with Fidelity Control | UB-SMoE: Universally Balanced Sparse Mixture-of-Experts for Resource-adaptive Federated Fine-tuning of Foundation Models | Social Hippocampus Memory Learning | Optimal Pricing for Data-Augmented AutoML Marketplaces | FedHPro: Federated Hyper-Prototype Learning via Gradient Matching
- Decision prompt: Decide whether this semantic cluster should be split into multiple report subareas or kept as one mixed neighborhood.

## How To Use

- Read queued papers first, then high-signal papers if the cluster remains ambiguous.
- Record paper-level judgments in `data/manual/area_review_overrides.csv`.
- If multiple papers support relabeling, update `TAXONOMY` in `scripts/build_manual_taxonomy_seed.py` and rebuild downstream artifacts.
- Do not use subarea-level claims for these clusters until adjudication is complete.

## Outputs

- `data/processed/icml2026_taxonomy_adjudication_queue.csv`
- `reports/icml2026_taxonomy_adjudication_queue.md`