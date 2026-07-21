# ICML 2026 Unsupervised Cluster Landscape

Method: TF-IDF over title, official topic, and abstract; TruncatedSVD latent semantic projection; normalized k-means clustering.
Selected cluster count: 30 from candidates 14, 18, 22, 26, 30, based on sampled cosine silhouette.

## Diagnostics

- k=14: silhouette=0.0719, size range=120-737
- k=18: silhouette=0.08, size range=182-662
- k=22: silhouette=0.084, size range=112-836
- k=26: silhouette=0.0962, size range=98-568
- k=30: silhouette=0.1075, size range=86-653 selected

## Cluster Map

### Cluster 17: representation / machine learning / machine / general
- Size: 536 papers (8.1%); orals: 16; awards: 0; public votes: 3269
- Top terms: data; representation; machine learning; machine; methods; general; general machine; representations; prediction; based; representation learning; latent; probabilistic; space; distribution
- Topic groups: General Machine Learning (184); Deep Learning (95); Probabilistic Methods (70); Applications (59); Unknown (49)
- Rule themes: Theory, optimization, and sampling (297); Memorization, evaluation, and generalization (230); Safety, alignment, governance, and risk (206); Systems, efficiency, and compression (146); Interpretability and mechanistic analysis (110)
- Central papers:
  - On the Power of Source Screening for Learning Shared Feature Extractors
  - Mixing Configurations for Downstream Prediction
  - Explicitly Modeling Censoring Produces Superior Survival Predictors
  - Hierarchical Retrieval at Scale: Bridging Transparency and Efficiency
  - Geometrically Constrained Outlier Synthesis
- High-signal papers:
  - Learning to Theorize the World from Observation
  - A Systematic Study of Behavioral Cloning for Scientific Data Annotation
  - Less is Enough: Synthesizing Diverse Data in Feature Space of LLMs
  - dnaHNet: A Scalable and Hierarchical Foundation Model for Genomic Sequence Learning
  - Exact Functional ANOVA Decomposition for Categorical Inputs

### Cluster 1: language / language models / llms / large language
- Size: 405 papers (6.1%); orals: 12; awards: 0; public votes: 3497
- Top terms: language; language models; llms; large language; large; llm; reasoning; learning large; models llms; deep learning; deep; evaluation; generation; knowledge; training
- Topic groups: Deep Learning (293); Social Aspects (29); General Machine Learning (25); Unknown (24); Applications (21)
- Rule themes: LLM reasoning and test-time compute (323); Memorization, evaluation, and generalization (245); Safety, alignment, governance, and risk (153); Theory, optimization, and sampling (142); Agents, tools, and computer use (121)
- Central papers:
  - LLMInertia: Adaptive Counter-Inertial Reasoning to Improve Evidence Faithfulness in Large Language Models
  - Learning Rewrite-Invariant Reasoning with Targeted Alternation Training
  - ToMAP: Training Opponent-Aware LLM Persuaders with Theory of Mind
  - Select to Think: Unlocking SLM Potential with Local Sufficiency
  - Benchmarking at the Edge of Comprehension
- High-signal papers:
  - Skip a Layer or Loop It? Learning Program-of-Layers in LLMs
  - Mechanistic Data Attribution: Tracing the Training Origins of Interpretable LLM Units
  - Procedural Pretraining: Warming Up Language Models with Abstract Data
  - Midtraining Bridges Pretraining and Posttraining Distributions
  - TokSuite: Measuring the Impact of Tokenizer Choice on Language Model Behavior

### Cluster 3: diffusion / generative / diffusion models / generative models
- Size: 403 papers (6.1%); orals: 7; awards: 1; public votes: 3641
- Top terms: diffusion; generative; diffusion models; generative models; autoencoders; generation; learning generative; models autoencoders; image; flow; sampling; matching; training; flow matching; guidance
- Topic groups: Deep Learning (268); Applications (42); Unknown (35); Probabilistic Methods (20); Social Aspects (17)
- Rule themes: Diffusion, flow, and generative modeling (399); Multimodal, vision-language, and video (238); Theory, optimization, and sampling (229); Agents, tools, and computer use (140); Systems, efficiency, and compression (136)
- Central papers:
  - Overclocking Electrostatic Generative Models
  - Efficient Generative Modeling beyond Memoryless Diffusion via Adjoint Schrödinger Bridge Matching
  - Temporal Score Rescaling for Temperature Sampling in Diffusion and Flow Models
  - Ambient Dataloops: Generative Models for Dataset Refinement
  - Rex: A Family of Reversible Exponential (Stochastic) Runge-Kutta Solvers
- High-signal papers:
  - A Random Matrix Perspective on the Consistency of Diffusion Models
  - Any-Order GPT as Masked Diffusion Model: Decoupling Formulation and Architecture
  - Orthogonal Concept Erasure for Diffusion Models
  - High-accuracy and dimension-free sampling with diffusions
  - Error Propagation Mechanisms and Compensation Strategies for Quantized Diffusion Models

### Cluster 9: theory / algorithm / optimal / regret
- Size: 372 papers (5.6%); orals: 15; awards: 1; public votes: 760
- Top terms: theory; algorithm; optimal; regret; bounds; online; problem; optimization; algorithms; bound; bandits; mathcal; setting; linear; convergence
- Topic groups: Theory (178); Optimization (59); General Machine Learning (41); Probabilistic Methods (36); Unknown (27)
- Rule themes: Theory, optimization, and sampling (358); LLM reasoning and test-time compute (104); Safety, alignment, governance, and risk (97); Systems, efficiency, and compression (80); Memorization, evaluation, and generalization (80)
- Central papers:
  - Randomized Feasibility Methods for Constrained Optimization with Adaptive Step Sizes
  - Learning the Best Under Constraints: A Duality-Based Framework
  - Decentralized Online Convex Optimization with Efficient Communication: Improved Algorithm and Lower Bounds
  - Optimal Design for Multinomial Logit Model with Applications to Best Assortment Identification
  - The Optimal Sample Complexity of Linear Contracts
- High-signal papers:
  - High-accuracy sampling for diffusion models and log-concave distributions
  - Mixtures Closest To A Given Measure: A Semidefinite Programming Approach
  - Markov Chain Monte Carlo without Evaluating the Target: an Auxiliary Variable Approach
  - Optimal Decision-Making Based on Prediction Sets
  - Minimax Optimal Strategy for Delayed Observations in Online Reinforcement Learning

### Cluster 25: cross / semantic / label / extensive
- Size: 368 papers (5.5%); orals: 2; awards: 0; public votes: 664
- Top terms: cross; semantic; methods; label; extensive; class; multi; extensive experiments; feature; modal; data; detection; experiments; alignment; existing
- Topic groups: Applications (138); General Machine Learning (95); Deep Learning (62); Unknown (41); Social Aspects (19)
- Rule themes: Memorization, evaluation, and generalization (225); Multimodal, vision-language, and video (225); Safety, alignment, governance, and risk (206); Theory, optimization, and sampling (134); Agents, tools, and computer use (130)
- Central papers:
  - MAGIC: Multi-Granularity Language-Informed Image Clustering
  - Bridging the Perceptual Gap: Residual-Enhanced Downscaling and Manifold-Aware Perception Alignment Adaptation for NR-IQA
  - From Coarse to Fine: Deep Prototype Refinement Network for Few-Shot Point Cloud Semantic Segmentation
  - [CLS] is Not Enough: Multi-Label Recognition via Patch-Level Inference and Adaptive Aggregation
  - PhaseAlign: Complex Phase Alignment for Stable Open-Vocabulary Semantic Segmentation
- High-signal papers:
  - DroneDINO: Towards Heterogeneous Routed Mixture of Experts for Drone-based Unified Object Detection
  - Multimodal Nested Learning for Decoupled and Coordinated Optimization
  - Unifying Heterogeneous Multi-Modal Remote Sensing Detection Via Language-Pivoted Pretraining
  - MUSE: Resolving Manifold Misalignment in Visual Tokenization via Topological Orthogonality
  - Is Training Necessary for Anomaly Detection?

### Cluster 11: agent / agents / multi agent / multi
- Size: 362 papers (5.5%); orals: 11; awards: 0; public votes: 6185
- Top terms: agent; agents; multi agent; multi; llm; agentic; llm agents; language; task; reasoning; large; execution; evaluation; benchmark; large language
- Topic groups: Deep Learning (119); Applications (64); Reinforcement Learning (52); Social Aspects (46); Unknown (40)
- Rule themes: Agents, tools, and computer use (359); Memorization, evaluation, and generalization (259); LLM reasoning and test-time compute (229); RL for LLMs and verifiable rewards (160); Safety, alignment, governance, and risk (120)
- Central papers:
  - Investigating Component Contributions in Multi-Agent ML Systems
  - LLawCo: Learning Laws of Cooperation for Modeling Embodied Multi-Agent Behavior
  - More Capable, Less Cooperative? When LLMs Fail at Zero-Cost Collaboration
  - Agora: Toward Autonomous Bug Detection in Production-Level Consensus Protocols with LLM Agents
  - VeRO: An Evaluation Harness for Agents to Optimize Agents
- High-signal papers:
  - $\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment
  - VenusBench-Mobile: A Challenging and User-Centric Benchmark for Mobile GUI Agents with Capability Diagnostics
  - CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability
  - daVinci-Dev: Agent-native Mid-training for Software Engineering
  - Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections

### Cluster 7: reinforcement learning / reinforcement / policy / rl
- Size: 295 papers (4.5%); orals: 7; awards: 0; public votes: 1731
- Top terms: reinforcement learning; reinforcement; policy; rl; policies; offline; value; deep rl; action; reward; learning rl; control; critic; based; learning reinforcement
- Topic groups: Reinforcement Learning (229); Theory (27); Unknown (13); Applications (11); Deep Learning (8)
- Rule themes: RL for LLMs and verifiable rewards (292); Theory, optimization, and sampling (157); Agents, tools, and computer use (153); Memorization, evaluation, and generalization (144); Systems, efficiency, and compression (128)
- Central papers:
  - Harmonized Dual Policy Improvement for Model-based Reinforcement Learning
  - Policy-Driven World Model Adaptation for Robust Offline Model-based Reinforcement Learning
  - What Makes Value Learning Efficient in Residual Reinforcement Learning?
  - Performative Policy Gradient: Optimality in Performative Reinforcement Learning
  - On Computation and Reinforcement Learning
- High-signal papers:
  - Maximum Likelihood Reinforcement Learning
  - Distributional Inverse Reinforcement Learning
  - On Computation and Reinforcement Learning
  - Learning Human-Robot Collaboration via Heterogeneous-Agent Lyapunov Policy Optimization
  - LASER: Learning Active Sensing for Continuum Field Reconstruction

### Cluster 4: visual / multimodal / reasoning / vision
- Size: 290 papers (4.4%); orals: 6; awards: 0; public votes: 2925
- Top terms: visual; multimodal; reasoning; vision; language; mllms; language models; vision language; large; multimodal large; image; understanding; large language; perception; text
- Topic groups: Deep Learning (136); Applications (92); Unknown (31); General Machine Learning (14); Social Aspects (11)
- Rule themes: Multimodal, vision-language, and video (290); Memorization, evaluation, and generalization (207); LLM reasoning and test-time compute (206); Agents, tools, and computer use (119); RL for LLMs and verifiable rewards (110)
- Central papers:
  - Do Vision and Text Cues Exhibit Evidential Coupling? UFO: A Benchmark for Compositional Multimodal Reasoning in Unified Models
  - Look on Demand: A Cognitive Scheduling Framework for Visual Evidence Acquisition in Multimodal Reasoning
  - IVQA-LD: Inclusive Multimodal Understanding for Population with Limb-Deficiency
  - MoDA: Modulation Adapter for Fine-Grained Visual Understanding in Instructional MLLMs
  - DiffThinker: Towards Generative Multimodal Reasoning with Diffusion Models
- High-signal papers:
  - Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning
  - Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination
  - Bad Seeing or Bad Thinking? Rewarding Perception for Multimodal Reasoning
  - PhotoAgent: Exploratory Visual Aesthetic Planning with Large Vision Models
  - DOUBT: Decoupled Object-level Understanding and Bridging via vMF-based Trustworthiness for Hallucination Detection in MLLMs

### Cluster 21: quantization / kv / memory / cache
- Size: 260 papers (3.9%); orals: 8; awards: 0; public votes: 3108
- Top terms: quantization; kv; memory; cache; inference; decoding; kv cache; language; bit; language models; large language; large; token; llm; times
- Topic groups: Deep Learning (170); Unknown (38); General Machine Learning (27); Applications (16); Optimization (7)
- Rule themes: Systems, efficiency, and compression (222); LLM reasoning and test-time compute (152); Theory, optimization, and sampling (107); Memorization, evaluation, and generalization (96); RL for LLMs and verifiable rewards (75)
- Central papers:
  - RaBitQCache: Rotated Binary Quantization for KVCache in Long Context LLM Inference
  - S-Quant: Rethinking Weight Quantization with Seed-Based Generation
  - Faster Than Flash: Exploiting Attention Sparsity for Efficient Long-Context Decoding
  - ASTRA: Communication-Efficient Acceleration for Multi-Device Transformer Inference
  - QTALE: Quantization-Robust Token-Adaptive Layer Execution for LLMs
- High-signal papers:
  - WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference
  - FlashSinkhorn: IO-Aware Entropic Optimal Transport on GPU
  - ECHO: Elastic Speculative Decoding with Sparse Gating for High-Concurrency Scenarios
  - POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation
  - FlashSketch: Sketch-Kernel Co-Design for Fast Sparse Sketching on GPUs

### Cluster 6: reasoning / reinforcement / rl / reinforcement learning
- Size: 253 papers (3.8%); orals: 5; awards: 1; public votes: 8329
- Top terms: reasoning; reinforcement; rl; reinforcement learning; policy; grpo; policy optimization; rewards; reward; language; large language; large; training; language models; optimization
- Topic groups: Deep Learning (162); Reinforcement Learning (38); Unknown (29); Applications (13); Theory (4)
- Rule themes: LLM reasoning and test-time compute (239); RL for LLMs and verifiable rewards (234); Theory, optimization, and sampling (184); Memorization, evaluation, and generalization (156); Systems, efficiency, and compression (129)
- Central papers:
  - Experience Augmented Policy Optimization for LLM Reasoning
  - EAPO: Enhancing Policy Optimization with On-Demand Expert Assistance
  - SetPO: Set-Level Policy Optimization for Diversity-Preserving LLM Reasoning
  - Prioritize the Process, Not Just the Outcome: Rewarding Latent Thought Trajectories Improves Reasoning in Looped Language Models
  - GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization
- High-signal papers:
  - The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models
  - Reinforcement Learning with Evolving Rubrics for Deep Research
  - Characterizing, Evaluating, and Optimizing Complex Reasoning
  - The Signal is in the Steps: Local Scoring for Reasoning Data Selection
  - Modeling Hierarchical Thinking in Large Reasoning Models

### Cluster 22: gradient / networks / optimization / neural networks
- Size: 248 papers (3.7%); orals: 7; awards: 1; public votes: 1752
- Top terms: gradient; networks; neural; optimization; neural networks; descent; stochastic; convergence; theory; training; gradient descent; theoretical; deep; network; loss
- Topic groups: Deep Learning (77); Optimization (69); Theory (48); General Machine Learning (20); Unknown (19)
- Rule themes: Theory, optimization, and sampling (217); Memorization, evaluation, and generalization (78); Safety, alignment, governance, and risk (78); Systems, efficiency, and compression (77); Interpretability and mechanistic analysis (57)
- Central papers:
  - Safeguarded Stochastic Polyak Step Sizes for Non-smooth Optimization: Robust Performance Without Small (Sub)Gradients
  - Rethinking Neural Network Learning Rates: A Stackelberg Perspective
  - On the Convergence of Steepest Descent and Adaptive Gradient Methods under Non-Uniform Smoothness
  - Adaptive Momentum and Nonlinear Damping for Neural Network Training
  - Gradient Descent as a Perceptron Algorithm: Understanding Dynamics and Implicit Acceleration
- High-signal papers:
  - To Grok Grokking: Provable Grokking in Ridge Regression
  - Controlled LLM Training on Spectral Sphere
  - SoftJAX & SoftTorch: Empowering Automatic Differentiation Libraries with Informative Gradients
  - Non-Euclidean Gradient Descent Operates at the Edge of Stability
  - On the Convergence Rate of LoRA Gradient Descent

### Cluster 12: tuning / fine tuning / fine / lora
- Size: 220 papers (3.3%); orals: 5; awards: 0; public votes: 2886
- Top terms: tuning; fine tuning; fine; lora; rank; language; low rank; language models; low; large; parameter; large language; adaptation; training; rank adaptation
- Topic groups: Deep Learning (131); Unknown (23); General Machine Learning (20); Optimization (16); Social Aspects (10)
- Rule themes: Systems, efficiency, and compression (134); LLM reasoning and test-time compute (120); Theory, optimization, and sampling (107); Memorization, evaluation, and generalization (103); Safety, alignment, governance, and risk (73)
- Central papers:
  - Low-cost Full Fine-tuning: Learning What to Update for LLMs
  - NaRA: Noise-Aware LoRA for Parameter-Efficient Fine-Tuning of Diffusion LLMs
  - Learning in the Fisher Subspace: A Guided Initialization for LoRA Fine-Tuning
  - Fine-Tuning of Transformer models with Frames
  - PLoRA: Efficient Concurrent LoRA Training for Large Language Models
- High-signal papers:
  - Learning Unmasking Policies for Diffusion Language Models
  - Do We Need Adam? Surprisingly Strong and Sparse Reinforcement Learning with SGD in LLMs
  - Diffract: Spectral View of LLM Domain Adaptation
  - Don't Force the Fit: Bounded Log-Likelihood Loss for Enhanced Reasoning in Large Language Models
  - FlatLand: Personalized Graph Federated Learning via Tailored Lorentz Space

### Cluster 10: 3d / vision / applications computer / computer vision
- Size: 215 papers (3.2%); orals: 2; awards: 0; public votes: 1196
- Top terms: 3d; vision; applications computer; computer vision; computer; spatial; object; scene; geometric; applications; reconstruction; image; view; geometry; scenes
- Topic groups: Applications (180); Unknown (15); Deep Learning (15); General Machine Learning (4); Social Aspects (1)
- Rule themes: Multimodal, vision-language, and video (211); Memorization, evaluation, and generalization (115); Agents, tools, and computer use (92); Safety, alignment, governance, and risk (73); Systems, efficiency, and compression (65)
- Central papers:
  - Direct 3D-Aware Object Insertion via Decomposed Visual Proxies
  - G$^2$TAM: Geometry Grounded Track Anything Model
  - DGG-HMR: Multi-Person Human Mesh Recovery with Depth-Guided Geometric Anchoring
  - LaRI: Layered Ray Intersections for Single-view 3D Geometric Reasoning
  - Crowd4D: Scene-Aware Monocular 4D Crowd Reconstruction
- High-signal papers:
  - Holi-Spatial: Evolving Video Streams into Holistic 3D Spatial Intelligence
  - 3ViewSense: Spatial and Mental Perspective Reasoning from Orthographic Views in Vision-Language Models
  - Self-Prompting Diffusion Transformer for Open-Vocabulary Scene Text Edit via In-Context Learning
  - Boosting Monocular Metric Depth Estimation via Bokeh Rendering
  - Alterbute: Editing Intrinsic Attributes of Objects in Images

### Cluster 20: code / anonymous / 4open science / 4open
- Size: 210 papers (3.2%); orals: 0; awards: 0; public votes: 1541
- Top terms: code; anonymous; 4open science; 4open; anonymous 4open; https anonymous; science; https; available; llms; language; available https; large language; code available; llm
- Topic groups: Deep Learning (83); Applications (37); General Machine Learning (29); Unknown (23); Social Aspects (17)
- Rule themes: Memorization, evaluation, and generalization (124); LLM reasoning and test-time compute (123); Agents, tools, and computer use (102); Theory, optimization, and sampling (89); Safety, alignment, governance, and risk (78)
- Central papers:
  - A²RBench: An Automatic Paradigm for Formally Verifiable Abstract Reasoning Benchmark Generation
  - Bridging the Gap in Autonomous Science: The Corpus and Benchmark for Biological Protocol Reasoning
  - Rethinking Code Complexity Through the Lens of Large Language Models
  - AICrypto: Evaluating Cryptography Capabilities of Large Language Models
  - PlotCraft: Pushing the Limits of LLMs for Complex and Interactive Data Visualization
- High-signal papers:
  - PaperBanana: Automating Academic Illustration for AI Scientists
  - SpecExit: Accelerating Large Reasoning Model via Speculative Exit
  - Closing the Loop: Universal Repository Representation with RPG-Encoder
  - FrontierCS: Evolving Challenges for Evolving Intelligence
  - NL2Repo-Bench: Towards Long-Horizon Repository Generation Evaluation of Coding Agents

### Cluster 2: attacks / attack / safety / adversarial
- Size: 183 papers (2.8%); orals: 5; awards: 1; public votes: 587
- Top terms: attacks; attack; safety; adversarial; backdoor; defense; social aspects; aspects; social; harmful; defenses; jailbreak; robustness; benign; security
- Topic groups: Social Aspects (117); Deep Learning (41); Unknown (16); Applications (5); Theory (2)
- Rule themes: Safety, alignment, governance, and risk (178); Agents, tools, and computer use (73); Memorization, evaluation, and generalization (73); Theory, optimization, and sampling (70); Systems, efficiency, and compression (62)
- Central papers:
  - SpatialJB: How Text Distribution Art Becomes The "Jailbreak Key" for LLM Guardrails
  - Poison with Style: A Practical Poisoning Attack on Code Large Language Models
  - Disentangling Intent from Role: Adversarial Self-Play for Persona-Invariant Safety Alignment
  - A Theoretical Game of Attacks via Compositional Skills
  - From Poisoned to Aware: Fostering Backdoor Self-Awareness in LLMs
- High-signal papers:
  - The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes
  - Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking
  - When the Prompt Becomes Visual: Vision-Centric Jailbreak Attacks for Large Image Editing Models
  - Mind Your Margin and Boundary: Are Your Distilled Datasets Truly Robust?
  - Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models

### Cluster 14: attention / transformers / transformer / context
- Size: 178 papers (2.7%); orals: 7; awards: 0; public votes: 2317
- Top terms: attention; transformers; transformer; context; attention mechanisms; learning attention; mechanisms; softmax; linear; deep; deep learning; sequence; self attention; token; linear attention
- Topic groups: Deep Learning (126); Theory (20); Unknown (18); General Machine Learning (6); Applications (4)
- Rule themes: Theory, optimization, and sampling (78); LLM reasoning and test-time compute (70); Memorization, evaluation, and generalization (69); Systems, efficiency, and compression (65); Safety, alignment, governance, and risk (51)
- Central papers:
  - LUCID: Attention with Preconditioned Representations
  - Krause Synchronization Transformers
  - A Provable Expressiveness Hierarchy in Hybrid Linear-Full Attention
  - Induction Heads Interpolate N-Grams
  - Softplus Attention with Re-weighting Boosts Length Extrapolation in Large Language Models
- High-signal papers:
  - Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models
  - Equivalence of Context and Parameter Updates in Modern Transformer Blocks
  - DiScoFormer: Plug-In Density and Score Estimation with Transformers
  - Focus and Dilution: The Multi-stage Learning Process of Attention
  - Rational Transductors

### Cluster 28: position / ai / position paper / argues
- Size: 178 papers (2.7%); orals: 9; awards: 2; public votes: 707
- Top terms: position; ai; position paper; argues; paper argues; paper; argue; research; social; systems; community; social aspects; aspects; evaluation; human
- Topic groups: Social Aspects (87); Deep Learning (24); General Machine Learning (24); Applications (21); Unknown (15)
- Rule themes: Safety, alignment, governance, and risk (133); Agents, tools, and computer use (81); Memorization, evaluation, and generalization (74); RL for LLMs and verifiable rewards (58); LLM reasoning and test-time compute (42)
- Central papers:
  - Position: Irresponsible AI: big tech’s influence on AI research and associated impacts
  - Position: EU AI Act's Research Exemptions Can Break the Publication Norms of Major AI Conferences
  - Position: AI Welfare Is Bullshit
  - Position: AI Should Facilitate Democratic Deliberation at Scale
  - Position: Neglecting the Sustainability of AI is Fuelling a Global AI Arms Race
- High-signal papers:
  - Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit
  - Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII)
  - Position: Anthropomorphic Misalignment Research Needs Stronger Evidence
  - Position: Stop Automating Peer Review Without Rigorous Evaluation
  - Position: The AI Imperative: Scaling High-Quality Peer Review in Machine Learning

### Cluster 5: graph / graph neural / networks / neural networks
- Size: 177 papers (2.7%); orals: 5; awards: 0; public votes: 361
- Top terms: graph; graph neural; networks; neural networks; neural; learning graph; graphs; node; gnns; gnn; graph learning; deep; nodes; deep learning; message
- Topic groups: Deep Learning (139); Unknown (15); Optimization (8); General Machine Learning (7); Applications (3)
- Rule themes: Memorization, evaluation, and generalization (88); Theory, optimization, and sampling (82); Safety, alignment, governance, and risk (52); Systems, efficiency, and compression (45); Agents, tools, and computer use (39)
- Central papers:
  - Is Fixing Schema Graphs Necessary? Full-Resolution Graph Structure Learning for Relational Deep Learning
  - Scalable Topology-Preserving Graph Coarsening: Concepts and Algorithms
  - Unitary Convolutions for Message-passing and Positional Encodings on Directed Graphs
  - Graph Neural Networks Are Not Continuous Across Graph Resolutions
  - GI-GCN: Global Interacted Graph Convolutional Networks via Dominant Sets for Graph Classification
- High-signal papers:
  - Which Algorithms Can Graph Neural Networks Learn?
  - MV-FGAD: Towards Efficient and Effective Federated Graph Anomaly Detection via Multi-view Learning
  - PhenoBrain: Phenotype-Conditioned Long-Range Communication for Multi-Modal Brain Network Analysis
  - Towards Hierarchy–Uniformity Equilibrium: Recovering Semantic Depth in Hypergraph Contrastive Learning
  - Foundations of Equivariant Deep Learning: Unifying Graph and Sheaf Neural Networks

### Cluster 0: video / video generation / videos / temporal
- Size: 169 papers (2.5%); orals: 2; awards: 1; public votes: 2402
- Top terms: video; video generation; videos; temporal; generation; motion; visual; vision; applications computer; computer vision; computer; diffusion; frame; video understanding; long
- Topic groups: Applications (88); Deep Learning (56); Unknown (17); General Machine Learning (3); Social Aspects (3)
- Rule themes: Multimodal, vision-language, and video (168); Diffusion, flow, and generative modeling (107); Agents, tools, and computer use (85); Memorization, evaluation, and generalization (81); LLM reasoning and test-time compute (60)
- Central papers:
  - RealisMotion: Decomposed Human Motion Control and Video Generation in the World Space
  - HECTOR: Hybrid Editable Compositional Object References for Video Generation
  - MotiMotion: Motion-Controlled Video Generation with Visual Reasoning
  - Enhancing Train-Free Infinite-Frame Generation for Consistent Long Videos
  - ImmersePro: End-to-End Stereo Video Synthesis Via Implicit Disparity Learning
- High-signal papers:
  - Motion Attribution for Video Generation
  - CLEAR: Context-Aware Learning with End-to-End Mask-Free Inference for Adaptive Subtitle Removal
  - PanoWorld-X: Generating Explorable Panoramic Worlds via Sphere-Aware Video Diffusion
  - Turbo4DGen: Ultra-Fast Acceleration for 4D Generation
  - Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Video Generation

### Cluster 18: time series / series / time / forecasting
- Size: 154 papers (2.3%); orals: 2; awards: 0; public votes: 466
- Top terms: time series; series; time; forecasting; series forecasting; applications time; temporal; multivariate; applications; modeling; learning sequential; data; multivariate time; real world; world
- Topic groups: Applications (92); Deep Learning (35); General Machine Learning (19); Social Aspects (3); Unknown (3)
- Rule themes: Memorization, evaluation, and generalization (88); Safety, alignment, governance, and risk (60); Theory, optimization, and sampling (51); Systems, efficiency, and compression (46); Diffusion, flow, and generative modeling (36)
- Central papers:
  - Taming the Recent-Data Bias: Towards Robust Time Series Forecasting with Global Context
  - L-Drive: Beyond a Single Mapping—Latent Context Drives Time Series Forecasting
  - DAG: A Dual Correlation Network for Time Series Forecasting with Exogenous Variables
  - FlowState: Sampling-Rate‑Equivariant Time‑Series Forecasting
  - Winformer: Transcending Pairwise Similarity for Time-series Generation
- High-signal papers:
  - From Text to Forecasts: Bridging Modality Gap with Temporal Evolution Semantic Space
  - ConFlux: Multivariate Time Series in Flux, One Unified Forecast in Confluence
  - From geometry to dynamics: Learning overdamped Langevin dynamics from sparse observations with geometric constraints
  - OpenTSLM: Time-Series Language Models for Reasoning over Multivariate Medical Text- and Time-Series Data
  - MN-Diff: Diffusion Parameterized MoE-NCDE for Continuous Time Series Generation with Irregular Observations

### Cluster 13: scaling / test time / test / time
- Size: 152 papers (2.3%); orals: 5; awards: 1; public votes: 4870
- Top terms: scaling; test time; test; time; time scaling; compute; reasoning; language; language models; laws; scaling laws; training; large language; inference; large
- Topic groups: Deep Learning (100); Unknown (25); General Machine Learning (7); Applications (7); Theory (5)
- Rule themes: LLM reasoning and test-time compute (126); Memorization, evaluation, and generalization (76); Theory, optimization, and sampling (76); Systems, efficiency, and compression (70); Agents, tools, and computer use (52)
- Central papers:
  - EAGer: Entropy-Aware GEneRation for Adaptive Inference-Time Scaling
  - What If We Allocate Test-Time Compute Adaptively?
  - HyPER: Bridging Exploration and Exploitation for Scalable LLM Reasoning with Hypothesis Path Expansion and Reduction
  - Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens
  - V1: Unifying Generation and Self-Verification for Parallel Reasoners
- High-signal papers:
  - How much can language models memorize?
  - Monitoring Monitorability
  - ThreadWeaver: Adaptive Threading for Efficient Parallel Reasoning in Language Models
  - Prescriptive Scaling Reveals the Evolution of Language Model Capabilities
  - OPUS: Towards Efficient and Principled Data Selection in Large Language Model Pre-training in Every Iteration

### Cluster 23: interpretability / accountability / transparency / transparency interpretability
- Size: 146 papers (2.2%); orals: 4; awards: 0; public votes: 1462
- Top terms: interpretability; accountability; transparency; transparency interpretability; accountability transparency; aspects accountability; social aspects; aspects; social; explanations; concept; attribution; sparse; interpretable; concepts
- Topic groups: Social Aspects (141); Unknown (3); Applications (1); Deep Learning (1)
- Rule themes: Interpretability and mechanistic analysis (146); Safety, alignment, governance, and risk (142); Memorization, evaluation, and generalization (52); Theory, optimization, and sampling (38); LLM reasoning and test-time compute (36)
- Central papers:
  - Ideal Attribution and Faithful Watermarks for Language Models
  - What is Missing? Explaining Neurons Activated by Absent Concepts
  - Hidden in Plain Sight -- Class Competition Focuses Attribution Maps
  - Do Natural Language Interpretability Methods Convey Privileged Information?
  - Query Circuits: Explaining How Language Models Answer User Prompts
- High-signal papers:
  - Is Your LLM Overcharging You? Tokenization, Transparency, and Incentives
  - Guaranteed Optimal Compositional Explanations for Neurons
  - Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers
  - Towards Long-Horizon Interpretability: Efficient and Faithful Multi-Token Attribution for Reasoning LLMs
  - Chain-of-Thought Reasoning In The Wild Is Not Always Faithful

### Cluster 15: physics / chemistry / earth / applications chemistry
- Size: 145 papers (2.2%); orals: 6; awards: 0; public votes: 453
- Top terms: physics; chemistry; earth; applications chemistry; chemistry physics; physics earth; earth sciences; sciences; molecular; applications; dynamics; physical; prediction; based; data
- Topic groups: Applications (145)
- Rule themes: AI for science, health, and biology (145); Memorization, evaluation, and generalization (71); Theory, optimization, and sampling (62); Diffusion, flow, and generative modeling (58); Systems, efficiency, and compression (47)
- Central papers:
  - GenUnfold: Rapidly Predict Protein Mechanical Unfolding Trajectory via a Physics-Guided Diffusion Model
  - Coupled Cluster con MoLe: Molecular Orbital Learning for Neural Wavefunctions
  - DISSOLVR: An Interpretable and Fast Framework for Aqueous and Organic Solubility Prediction
  - MuCO: Generative Peptide Cyclization Empowered by Multi-stage Conformation Optimization
  - From Evaluation to Design: Using Potential Energy Surface Smoothness Metrics to Guide ML Interatomic Potential Architectures
- High-signal papers:
  - Protein Autoregressive Modeling via Multiscale Structure Generation
  - Protein Fold Classification at Scale: Benchmarking and Pretraining
  - Training-Free Bayesian Filtering with Generative Emulators
  - Transforming Weather Data from Pixel to Latent Space
  - From Feasible to Practical: Pareto-Optimal Synthesis Planning

### Cluster 24: preference / reward / preferences / preference optimization
- Size: 133 papers (2.0%); orals: 5; awards: 0; public votes: 852
- Top terms: preference; reward; preferences; preference optimization; human; alignment; dpo; optimization; rlhf; feedback; human feedback; human preferences; reinforcement learning; reinforcement; direct preference
- Topic groups: Deep Learning (46); Social Aspects (25); Reinforcement Learning (23); Applications (13); Unknown (9)
- Rule themes: RL for LLMs and verifiable rewards (114); Safety, alignment, governance, and risk (95); Theory, optimization, and sampling (92); Memorization, evaluation, and generalization (67); LLM reasoning and test-time compute (49)
- Central papers:
  - Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases
  - Reliability-Aware LLM Alignment from Inconsistent Human Feedback
  - Normalized Rewards for Preference Optimization
  - Unbiased Alignment for Large Language Models with Noisy Preferences
  - The Sign Estimator: Preference Modeling for LLM Alignment under Heterogeneity
- High-signal papers:
  - Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling
  - Reward-free Alignment for Conflicting Objectives
  - VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment in Large Language Models
  - Video-Based Optimal Transport for Feedback-Efficient Offline Preference-Based Reinforcement Learning
  - DPO Unchained: Your Training Algorithm is Secretly Disentangled in Human Choice Theory (and Its Loss' Convexity is Dispensable)

### Cluster 19: action / vla / language action / vision language
- Size: 129 papers (1.9%); orals: 5; awards: 0; public votes: 2979
- Top terms: action; vla; language action; vision language; manipulation; robotics; applications robotics; vision; robotic; vla models; robot; world; action vla; action models; real
- Topic groups: Applications (102); Unknown (14); Deep Learning (5); General Machine Learning (3); Reinforcement Learning (3)
- Rule themes: Robotics and world models (126); Multimodal, vision-language, and video (111); Memorization, evaluation, and generalization (88); Agents, tools, and computer use (51); Systems, efficiency, and compression (49)
- Central papers:
  - FOCA: Future-Oriented Conditioning for Data-Efficient Vision-Language-Action Adaptation
  - XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations
  - TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments
  - A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots
  - VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model
- High-signal papers:
  - From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model
  - RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies
  - From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models
  - Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning
  - XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations

### Cluster 27: neuroscience / cognitive / neuroscience cognitive / applications neuroscience
- Size: 105 papers (1.6%); orals: 1; awards: 0; public votes: 268
- Top terms: neuroscience; cognitive; neuroscience cognitive; applications neuroscience; cognitive science; spiking; neural; brain; science; networks; snns; spiking neural; eeg; neural networks; spike
- Topic groups: Applications (86); Deep Learning (14); General Machine Learning (2); Unknown (2); Optimization (1)
- Rule themes: AI for science, health, and biology (99); Systems, efficiency, and compression (45); Memorization, evaluation, and generalization (42); Multimodal, vision-language, and video (41); Interpretability and mechanistic analysis (34)
- Central papers:
  - Bio-Vision-Inspired Spiking Neural Networks for Object Detection with Event Cameras
  - SmoothSpike: Spiking Transformer with Learnable Hadamard Transformation
  - Resolving the Timestep Scaling Paradox in Spiking Neural Networks with a Timestep-Scalable Neuron Model
  - Training Deep Spiking Neural Networks without Normalization
  - Bullet Trains: Parallelizing Training of Temporally Precise Spiking Neural Networks
- High-signal papers:
  - AI Engram: In Search of Memory Traces in Artificial Intelligence
  - Scaling Vision Transformers for Functional MRI with Flat Maps
  - EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation and Diagnostic Analyses of EEG Foundation Models
  - FOVI: A biologically-inspired foveated interface for deep vision models
  - Omni-fMRI: A Universal Atlas-Free fMRI Foundation Model

### Cluster 8: causal / causality / learning causality / treatment
- Size: 97 papers (1.5%); orals: 3; awards: 0; public votes: 223
- Top terms: causal; causality; learning causality; treatment; causal discovery; general machine; machine learning; machine; general; discovery; estimation; effect; effects; data; observational
- Topic groups: General Machine Learning (80); Unknown (8); Applications (4); Deep Learning (2); Social Aspects (2)
- Rule themes: Causality and data-centric ML (96); Safety, alignment, governance, and risk (44); Theory, optimization, and sampling (37); Memorization, evaluation, and generalization (28); AI for science, health, and biology (21)
- Central papers:
  - Local Covariate Selection for Average Causal Effect Estimation without Pretreatment and Causal Sufficiency Assumptions
  - On the Identifiability of Poisson Branching Structural Causal Model Under Latent Confounding
  - Addressing Instrument-Outcome Confounding in Mendelian Randomization through Representation Learning
  - Causal Effect Identifiability in the Presence of Latent Confounders Without Auxiliary Variables
  - Identifying Partially Observed Causal Models from Heterogeneous/Nonstationary Data
- High-signal papers:
  - A Recursive Decomposition Framework for Causal Structure Learning in the Presence of Latent Variables
  - DISCO: Mitigating Bias in Deep Learning with Conditional Distance Correlation
  - On the Identifiability of Poisson Branching Structural Causal Model Under Latent Confounding
  - CauScale: Neural Causal Discovery at Scale
  - Position: Causality is Key for Interpretability Claims to Generalise

### Cluster 16: physics / pde / equations / pdes
- Size: 86 papers (1.3%); orals: 3; awards: 0; public votes: 303
- Top terms: physics; neural; pde; equations; pdes; differential; differential equations; physics informed; operator; informed; operators; partial differential; physical; partial; sciences
- Topic groups: Applications (52); Deep Learning (11); Unknown (7); Probabilistic Methods (6); General Machine Learning (6)
- Rule themes: AI for science, health, and biology (69); Theory, optimization, and sampling (56); Memorization, evaluation, and generalization (50); Systems, efficiency, and compression (33); Diffusion, flow, and generative modeling (28)
- Central papers:
  - TINNs: Time-Induced Neural Networks for Solving Time-Dependent PDEs
  - Structure-Preserving Learning Improves Geometry Generalization in Neural PDEs
  - Imposing Boundary Conditions on Neural Operators via Learned Function Extensions
  - Deep Coupling Learning for Solving PDEs
  - Neural-HSS: Hierarchical Semi-Separable Neural PDE Solver
- High-signal papers:
  - ReViT: Rotational-equivariant Vision Transformers for Neural PDE Solvers
  - Lottery Prior: Randomized Neural Compression for Zero-Shot Inverse Problems
  - Solving Time-Dependent Differential Equations with Physical Dynamical Systems
  - GeoPT: Scaling Physics Simulation via Lifted Geometric Pre-Training
  - Mesh Based Simulations with Spatial and Temporal awareness

### Cluster 29: speech / audio / applications language / speech dialog
- Size: 80 papers (1.2%); orals: 1; awards: 0; public votes: 529
- Top terms: speech; audio; applications language; speech dialog; dialog; language speech; language; text; applications; acoustic; tts; deepfake; data; benchmark; training
- Topic groups: Applications (61); Deep Learning (10); Unknown (4); General Machine Learning (3); Social Aspects (2)
- Rule themes: Memorization, evaluation, and generalization (52); Safety, alignment, governance, and risk (35); Agents, tools, and computer use (34); Multimodal, vision-language, and video (26); Systems, efficiency, and compression (25)
- Central papers:
  - SAM Audio: Segment Anything in Audio
  - Evaluating and Rewarding LALMs for Expressive Role-Play TTS via Mean Continuation Log-Probability
  - A Semantically Consistent Dataset for Data-Efficient Query-Based Universal Sound Separation
  - SPEAR: A Unified SSL Framework for Learning Speech and Audio Representations
  - AudioChat: Unified Audio Storytelling, Editing, and Understanding with Transfusion Forcing
- High-signal papers:
  - Simultaneous Speech-to-Speech Translation Without Aligned Data
  - SAM Audio: Segment Anything in Audio
  - AudioChat: Unified Audio Storytelling, Editing, and Understanding with Transfusion Forcing
  - AuTAgent: A Reinforcement Learning Framework for Tool-Augmented Audio Reasoning
  - A Semantically Consistent Dataset for Data-Efficient Query-Based Universal Sound Separation

### Cluster 26: privacy / private / dp / aspects privacy
- Size: 79 papers (1.2%); orals: 2; awards: 0; public votes: 175
- Top terms: privacy; private; dp; aspects privacy; unlearning; differential privacy; differentially private; differentially; utility; differential; social aspects; social; aspects; data; sensitive
- Topic groups: Social Aspects (64); Unknown (5); Theory (3); General Machine Learning (3); Deep Learning (3)
- Rule themes: Safety, alignment, governance, and risk (79); Theory, optimization, and sampling (41); Systems, efficiency, and compression (28); Memorization, evaluation, and generalization (20); Agents, tools, and computer use (12)
- Central papers:
  - Differentially Private and Scalable Estimation of the Network Principal Component
  - Eliminating Solution Bias in Differentially Private Optimization
  - Efficient Public Verification of Private ML via Regularization
  - PrivCode++ : Latent-Conditioned Differentially Private Code Generation for Comprehensive Guarantees
  - Differentially Private Cross-Silo Recommendation from Implicit Feedback
- High-signal papers:
  - PRISM: Gauge-Invariant Tangent-Space Differentially Private LoRA
  - Privacy-Aware Video Anomaly Detection: Guided Orthogonal Projection and a Comprehensive Evaluation Framework
  - Privasis: Synthesizing the Largest "Public" Private Dataset from Scratch
  - Unlearning’s Blind Spots: Over‑Unlearning and Prototypical Relearning Attack
  - ZeroUnlearn: Few-Shot Knowledge Unlearning in Large Language Models


## Signal Calibration

Corpus oral rate: 2.53%. Oral enrichment compares each cluster oral rate against that corpus baseline.

### Highest Oral Enrichment

- Cluster 28 (position / ai / position paper / argues): 5.1% oral, 1.99x baseline, 178 papers
- Cluster 15 (physics / chemistry / earth / applications chemistry): 4.1% oral, 1.63x baseline, 145 papers
- Cluster 9 (theory / algorithm / optimal / regret): 4.0% oral, 1.59x baseline, 372 papers
- Cluster 14 (attention / transformers / transformer / context): 3.9% oral, 1.55x baseline, 178 papers
- Cluster 19 (action / vla / language action / vision language): 3.9% oral, 1.53x baseline, 129 papers
- Cluster 24 (preference / reward / preferences / preference optimization): 3.8% oral, 1.48x baseline, 133 papers
- Cluster 16 (physics / pde / equations / pdes): 3.5% oral, 1.38x baseline, 86 papers
- Cluster 13 (scaling / test time / test / time): 3.3% oral, 1.3x baseline, 152 papers
- Cluster 8 (causal / causality / learning causality / treatment): 3.1% oral, 1.22x baseline, 97 papers
- Cluster 21 (quantization / kv / memory / cache): 3.1% oral, 1.21x baseline, 260 papers

### Highest Public Attention Per Paper

- Cluster 6 (reasoning / reinforcement / rl / reinforcement learning): 32.92 votes/paper, 13.8% of public votes, 253 papers
- Cluster 13 (scaling / test time / test / time): 32.04 votes/paper, 8.1% of public votes, 152 papers
- Cluster 19 (action / vla / language action / vision language): 23.09 votes/paper, 4.9% of public votes, 129 papers
- Cluster 11 (agent / agents / multi agent / multi): 17.09 votes/paper, 10.2% of public votes, 362 papers
- Cluster 0 (video / video generation / videos / temporal): 14.21 votes/paper, 4.0% of public votes, 169 papers
- Cluster 12 (tuning / fine tuning / fine / lora): 13.12 votes/paper, 4.8% of public votes, 220 papers
- Cluster 14 (attention / transformers / transformer / context): 13.02 votes/paper, 3.8% of public votes, 178 papers
- Cluster 21 (quantization / kv / memory / cache): 11.95 votes/paper, 5.1% of public votes, 260 papers
- Cluster 4 (visual / multimodal / reasoning / vision): 10.09 votes/paper, 4.8% of public votes, 290 papers
- Cluster 23 (interpretability / accountability / transparency / transparency interpretability): 10.01 votes/paper, 2.4% of public votes, 146 papers
## Researcher Interpretation Notes

- Use clusters as a second opinion against the rule-based theme map. Agreement means the topic is robust; disagreement marks papers worth manual review.
- Large mixed clusters usually indicate broad methodological language rather than a coherent subfield. Split them manually before using in a presentation.
- Small clusters with high oral or award density are often more interesting than large clusters with high public attention.
- This is not a transformer embedding map. It is a lightweight local baseline that should be replaced or benchmarked against sentence embeddings for a final 9.5/10 report.