# ICML 2026 Semantic Cluster Landscape

Method: transformer sentence embeddings from `sentence-transformers/all-MiniLM-L6-v2`, normalized k-means clustering, and TF-IDF terms used only for cluster labels.
Selected semantic cluster count: 42 from candidates 18, 24, 30, 36, 42.
Embedding cache: `data/processed/icml2026_semantic_embeddings.npy`.

## Diagnostics

- k=18: silhouette=0.0476, size range=174-592
- k=24: silhouette=0.0454, size range=108-457
- k=30: silhouette=0.0419, size range=84-391
- k=36: silhouette=0.0434, size range=1-274
- k=42: silhouette=0.053, size range=1-315 selected
- Semantic-vs-lexical adjusted Rand index: 0.2558
- Semantic-vs-lexical normalized mutual information: 0.4824

Low agreement is not automatically bad. It marks where vocabulary clusters and semantic neighborhoods disagree, which is useful for manual landscape review.

## Largest Semantic Clusters

### Semantic Cluster 4: reinforcement learning / reinforcement / policy / rl
- Size: 312 papers (4.7%); orals: 6; awards: 0; votes/paper: 6.01
- Top terms: reinforcement learning; reinforcement; policy; rl; policies; offline; value; agent; control; action; based; learning rl; learning reinforcement; critic; reward; deep rl
- Topic groups: Reinforcement Learning (222); Theory (34); Applications (18); Unknown (18); Deep Learning (7)
- Rule themes: RL for LLMs and verifiable rewards (301); Theory, optimization, and sampling (188); Agents, tools, and computer use (176); Memorization, evaluation, and generalization (137); Systems, efficiency, and compression (134)
- Lexical overlaps: 7 (232); 11 (21); 9 (13); 6 (11); 24 (8)
- Central papers:
  - Reparameterization Flow Policy Optimization
  - Generative Online Reinforcement Learning
  - Sample Efficient Full-Finetuning of Generative Control Policies
  - Prioritized Model Experience Replay
- High-signal papers:
  - Distributional Inverse Reinforcement Learning
  - On Computation and Reinforcement Learning
  - Learning Human-Robot Collaboration via Heterogeneous-Agent Lyapunov Policy Optimization
  - Chebyshev Policies and the Mountain Car Problem: Reinforcement Learning for Low-dimensional Control Tasks

### Semantic Cluster 24: language / language models / llms / large language
- Size: 290 papers (4.4%); orals: 14; awards: 0; votes/paper: 8.76
- Top terms: language; language models; llms; large language; large; llm; models llms; alignment; learning large; training; evaluation; data; fine; knowledge; deep learning; tuning
- Topic groups: Deep Learning (143); Social Aspects (65); Applications (32); General Machine Learning (21); Unknown (21)
- Rule themes: Safety, alignment, governance, and risk (169); Memorization, evaluation, and generalization (158); LLM reasoning and test-time compute (157); Interpretability and mechanistic analysis (106); Theory, optimization, and sampling (90)
- Lexical overlaps: 1 (130); 12 (33); 23 (30); 29 (23); 20 (12)
- Central papers:
  - Bridging the Knowledge-Prediction Gap in LLMs on Multiple-Choice Questions
  - Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers
  - Harnessing Non-Adversarial Robustness in Large Language Models
  - Learning Self-Interpretation from Interpretability Artifacts: Training Lightweight Adapters on Vector-Label Pairs
- High-signal papers:
  - Simultaneous Speech-to-Speech Translation Without Aligned Data
  - Mechanistic Data Attribution: Tracing the Training Origins of Interpretable LLM Units
  - Procedural Pretraining: Warming Up Language Models with Abstract Data
  - TokSuite: Measuring the Impact of Tokenizer Choice on Language Model Behavior

### Semantic Cluster 22: visual / vision / reasoning / video
- Size: 272 papers (4.1%); orals: 7; awards: 0; votes/paper: 8.96
- Top terms: visual; vision; reasoning; video; vision language; language; multimodal; image; computer vision; vlms; computer; language models; applications computer; grounding; perception; object
- Topic groups: Applications (131); Deep Learning (88); Unknown (25); General Machine Learning (12); Social Aspects (10)
- Rule themes: Multimodal, vision-language, and video (268); Memorization, evaluation, and generalization (181); LLM reasoning and test-time compute (163); Agents, tools, and computer use (121); RL for LLMs and verifiable rewards (95)
- Lexical overlaps: 4 (126); 0 (61); 10 (22); 25 (22); 14 (4)
- Central papers:
  - Awakening Visual Reasoning: Mitigating Post-Training Failure in Vision-Text Compression
  - Focusing Where Vision Matters: Selective Training for Large Vision Language Models via Visual Information Gain
  - Chain-of-Glimpse: Search-Guided Progressive Object-Grounded Reasoning for Video Understanding
  - PGT: Procedurally Generated Tasks for improving fine-grained understanding in MLLMs
- High-signal papers:
  - CLEAR: Context-Aware Learning with End-to-End Mask-Free Inference for Adaptive Subtitle Removal
  - Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination
  - Bad Seeing or Bad Thinking? Rewarding Perception for Multimodal Reasoning
  - 3ViewSense: Spatial and Mental Perspective Reasoning from Orthographic Views in Vision-Language Models

### Semantic Cluster 12: safety / attacks / attack / social aspects
- Size: 245 papers (3.7%); orals: 5; awards: 1; votes/paper: 5.16
- Top terms: safety; attacks; attack; social aspects; aspects; social; security; adversarial; harmful; llms; language; benign; jailbreak; llm; defense; aspects safety
- Topic groups: Social Aspects (165); Deep Learning (44); Unknown (25); Applications (5); Theory (2)
- Rule themes: Safety, alignment, governance, and risk (234); Agents, tools, and computer use (115); Memorization, evaluation, and generalization (115); LLM reasoning and test-time compute (82); Systems, efficiency, and compression (74)
- Lexical overlaps: 2 (139); 11 (28); 23 (19); 1 (14); 20 (10)
- Central papers:
  - Internalizing Safety Understanding in Large Reasoning Models via Verification
  - Training with Honeypots: Reshaping How LLMs Fail
  - SafeHarbor: Defining Precise Decision Boundaries via Hierarchical Memory-Augmented Guardrail for LLM Agent Safety
  - A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness
- High-signal papers:
  - The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes
  - Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking
  - When the Prompt Becomes Visual: Vision-Centric Jailbreak Attacks for Large Image Editing Models
  - Quantifying Frontier LLM Capabilities for Container Sandbox Escape

### Semantic Cluster 34: diffusion / generative / image / generative models
- Size: 243 papers (3.7%); orals: 2; awards: 0; votes/paper: 10.62
- Top terms: diffusion; generative; image; generative models; generation; diffusion models; learning generative; models autoencoders; autoencoders; quality; flow; training; deep; latent; deep learning; matching
- Topic groups: Deep Learning (155); Applications (48); Unknown (19); Social Aspects (9); General Machine Learning (8)
- Rule themes: Diffusion, flow, and generative modeling (230); Multimodal, vision-language, and video (203); Theory, optimization, and sampling (117); Systems, efficiency, and compression (98); Safety, alignment, governance, and risk (94)
- Lexical overlaps: 3 (173); 0 (23); 10 (8); 25 (7); 17 (6)
- Central papers:
  - Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis
  - Both Semantics and Reconstruction Matter: Making Representation Encoders Ready for Text-to-Image Generation and Editing
  - Variational Flow Maps: Make Some Noise for One-Step Conditional Generation
  - Contrastive Flow Map Matching
- High-signal papers:
  - Transforming Weather Data from Pixel to Latent Space
  - Error Propagation Mechanisms and Compensation Strategies for Quantized Diffusion Models
  - Self-Prompting Diffusion Transformer for Open-Vocabulary Scene Text Edit via In-Context Learning
  - Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Video Generation

### Semantic Cluster 0: multimodal / visual / modal / modality
- Size: 237 papers (3.6%); orals: 1; awards: 0; votes/paper: 7.3
- Top terms: multimodal; visual; modal; modality; text; mllms; image; modalities; language; cross modal; semantic; vision; alignment; cross; understanding; audio
- Topic groups: Deep Learning (98); Applications (75); Unknown (24); General Machine Learning (24); Social Aspects (14)
- Rule themes: Multimodal, vision-language, and video (231); Memorization, evaluation, and generalization (153); Safety, alignment, governance, and risk (121); LLM reasoning and test-time compute (99); Agents, tools, and computer use (85)
- Lexical overlaps: 4 (107); 25 (51); 0 (13); 29 (13); 3 (11)
- Central papers:
  - Seeing is Understanding: Unlocking Causal Attention into Modality-Mutual Attention for Multimodal LLMs
  - Towards Unified Multimodal Pretraining
  - SEPS: Semantic-Enhanced Patch Slimming Framework for Fine-Grained Cross-Modal Alignment
  - Towards Understanding Modality Interaction in Multimodal Language Models via Partial Information Decomposition
- High-signal papers:
  - Multimodal Nested Learning for Decoupled and Coordinated Optimization
  - SAM Audio: Segment Anything in Audio
  - AudioChat: Unified Audio Storytelling, Editing, and Understanding with Transfusion Forcing
  - ExSkill: Continual Learning from Experience and Skills in Multimodal Agents

### Semantic Cluster 11: reasoning / language / large language / language models
- Size: 211 papers (3.2%); orals: 10; awards: 1; votes/paper: 18.32
- Top terms: reasoning; language; large language; language models; large; llms; learning large; thought; deep; deep learning; cot; reasoning models; chain; latent; tasks; chain thought
- Topic groups: Deep Learning (152); Applications (18); Unknown (17); Social Aspects (14); General Machine Learning (7)
- Rule themes: LLM reasoning and test-time compute (206); Memorization, evaluation, and generalization (129); Agents, tools, and computer use (94); Systems, efficiency, and compression (71); RL for LLMs and verifiable rewards (60)
- Lexical overlaps: 1 (76); 6 (30); 13 (19); 4 (17); 20 (14)
- Central papers:
  - Stop When Further Reasoning Won’t Help: Attention-State Adaptive Generation in Reasoning Models
  - DyCon: Dynamic Reasoning Control via Evolving Difficulty Modeling
  - Reasoning Compartmentalization: Bridging the Concretization Gap via Abstraction-based Routing
  - Which Reasoning Traces Are Worth Generating Further? Data Curation for Training Reasoning Models
- High-signal papers:
  - The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models
  - Skip a Layer or Loop It? Learning Program-of-Layers in LLMs
  - Characterizing, Evaluating, and Optimizing Complex Reasoning
  - Learning to Theorize the World from Observation

### Semantic Cluster 40: agents / agent / evaluation / agentic
- Size: 207 papers (3.1%); orals: 10; awards: 0; votes/paper: 16.88
- Top terms: agents; agent; evaluation; agentic; llm; language; reasoning; multi; benchmark; tool; multi agent; large; large language; task; tasks; execution
- Topic groups: Deep Learning (73); Applications (48); General Machine Learning (31); Unknown (29); Reinforcement Learning (12)
- Rule themes: Agents, tools, and computer use (196); Memorization, evaluation, and generalization (164); LLM reasoning and test-time compute (139); RL for LLMs and verifiable rewards (76); Systems, efficiency, and compression (57)
- Lexical overlaps: 11 (151); 20 (16); 1 (10); 28 (9); 13 (3)
- Central papers:
  - FT-Dojo: Towards Autonomous LLM Fine-Tuning with Language Agents
  - ScaleEnv: Scaling Environment Synthesis from Scratch for Generalist Interactive Tool-Use Agent Training
  - VeRO: An Evaluation Harness for Agents to Optimize Agents
  - Beyond the Final Answer: Evaluating the Reasoning Trajectories of Tool-Augmented Agents
- High-signal papers:
  - $\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment
  - Monitoring Monitorability
  - Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning
  - VenusBench-Mobile: A Challenging and User-Centric Benchmark for Mobile GUI Agents with Capability Diagnostics

### Semantic Cluster 25: 3d / video / motion / applications computer
- Size: 203 papers (3.1%); orals: 2; awards: 1; votes/paper: 8.67
- Top terms: 3d; video; motion; applications computer; computer vision; vision; computer; geometric; scene; applications; spatial; geometry; consistency; view; generation; object
- Topic groups: Applications (140); Deep Learning (40); Unknown (20); General Machine Learning (2); Reinforcement Learning (1)
- Rule themes: Multimodal, vision-language, and video (197); Agents, tools, and computer use (99); Diffusion, flow, and generative modeling (95); Memorization, evaluation, and generalization (87); Systems, efficiency, and compression (66)
- Lexical overlaps: 10 (118); 0 (53); 3 (14); 25 (6); 19 (4)
- Central papers:
  - CamGeo: Sparse Camera-Conditioned Image-to-Video Generation with 3D Geometry Priors
  - SceneDirector: Bridging Explicit Geometry and Generative Priors for Unified Driving Scene Editing
  - Fast-SAM3D: 3Dfy Anything in Images but Faster
  - MVISTA-4D: View-Consistent 4D World Model with Test-Time Action Inference for Robotic Manipulation
- High-signal papers:
  - Motion Attribution for Video Generation
  - Holi-Spatial: Evolving Video Streams into Holistic 3D Spatial Intelligence
  - PanoWorld-X: Generating Explorable Panoramic Worlds via Sphere-Aware Video Diffusion
  - Boosting Monocular Metric Depth Estimation via Bokeh Rendering

### Semantic Cluster 26: networks / training / deep / gradient
- Size: 198 papers (3.0%); orals: 2; awards: 0; votes/paper: 13.31
- Top terms: neural; networks; training; deep; gradient; optimization; deep learning; neural networks; network; architectures; layer; loss; optimizer; updates; low; muon
- Topic groups: Deep Learning (109); Optimization (26); General Machine Learning (17); Unknown (16); Theory (14)
- Rule themes: Theory, optimization, and sampling (132); Systems, efficiency, and compression (92); Memorization, evaluation, and generalization (67); Safety, alignment, governance, and risk (59); LLM reasoning and test-time compute (56)
- Lexical overlaps: 22 (80); 12 (27); 17 (23); 21 (12); 20 (11)
- Central papers:
  - Memory-Efficient LLMs Training with Dynamic Sparsity: From Stability to Practical Scaling
  - From Muon to Gluon: Bridging Theory and Practice of LMO-based Optimizers for LLMs
  - Exploiting weight-space symmetries for approximating curvature
  - Memory-Efficient LLM Pretraining via Minimalist Optimizer Design
- High-signal papers:
  - Controlled LLM Training on Spectral Sphere
  - MuonSSM: Orthogonalizing State Space Models for Sequence Modeling
  - mHC: Manifold-Constrained Hyper-Connections
  - Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights

### Semantic Cluster 16: action / robotics / vla / applications robotics
- Size: 195 papers (2.9%); orals: 4; awards: 0; votes/paper: 19.19
- Top terms: action; robotics; vla; applications robotics; manipulation; language action; robot; vision language; world; vision; robotic; embodied; real; task; vla models; actions
- Topic groups: Applications (135); Unknown (23); Reinforcement Learning (17); Deep Learning (15); General Machine Learning (3)
- Rule themes: Robotics and world models (165); Multimodal, vision-language, and video (149); Memorization, evaluation, and generalization (134); Agents, tools, and computer use (102); RL for LLMs and verifiable rewards (76)
- Lexical overlaps: 19 (114); 11 (15); 7 (12); 10 (10); 0 (8)
- Central papers:
  - FOCA: Future-Oriented Conditioning for Data-Efficient Vision-Language-Action Adaptation
  - XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations
  - UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning
  - Towards Practical World Model-based Reinforcement Learning for Vision-Language-Action Models
- High-signal papers:
  - From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model
  - RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies
  - From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models
  - XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations

### Semantic Cluster 17: label / labels / machine / machine learning
- Size: 192 papers (2.9%); orals: 1; awards: 0; votes/paper: 2.38
- Top terms: label; data; labels; machine; machine learning; general machine; class; general; methods; datasets; performance; training; samples; classification; supervised; based
- Topic groups: General Machine Learning (78); Applications (33); Social Aspects (27); Deep Learning (22); Unknown (17)
- Rule themes: Safety, alignment, governance, and risk (114); Memorization, evaluation, and generalization (107); Theory, optimization, and sampling (84); Agents, tools, and computer use (49); Interpretability and mechanistic analysis (49)
- Lexical overlaps: 25 (64); 17 (61); 23 (16); 1 (11); 29 (6)
- Central papers:
  - Convex Dataset Valuation for Post-Training
  - Class-Conditional Distribution Balancing for Group Robust Classification
  - Just Y-Prediction: Enabling Historical Cumulative Inconsistency in Label Diffusion for Learning with Noisy Label
  - Coupled Training with Privileged Features and Unlabeled Data
- High-signal papers:
  - On the Difficulty of Learning a Meta-network for Training Data Selection
  - A Semantically Consistent Dataset for Data-Efficient Query-Based Universal Sound Separation
  - OSF: On Pre-training and Scaling of Sleep Foundation Models
  - Building Social World Model with Large Language Models

### Semantic Cluster 7: theory / regression / bounds / risk
- Size: 180 papers (2.7%); orals: 4; awards: 1; votes/paper: 2.07
- Top terms: theory; regression; data; bounds; risk; sample; distribution; learning theory; machine; machine learning; error; theory learning; optimal; methods; bound; distributions
- Topic groups: Theory (73); General Machine Learning (49); Unknown (17); Deep Learning (17); Probabilistic Methods (14)
- Rule themes: Theory, optimization, and sampling (155); Safety, alignment, governance, and risk (88); Memorization, evaluation, and generalization (77); LLM reasoning and test-time compute (38); Systems, efficiency, and compression (31)
- Lexical overlaps: 17 (75); 9 (67); 22 (9); 25 (5); 13 (4)
- Central papers:
  - Generalization Bounds for Out-of-distribution Generalization
  - General Quantification of Covariate and Concept Shifts
  - Learning Partial Concept Classes and Universal Rates Under Massart Noise
  - Characterization of Gaussian Universality Breakdown in High-Dimensional Empirical Risk Minimization
- High-signal papers:
  - To Grok Grokking: Provable Grokking in Ridge Regression
  - Mixtures Closest To A Given Measure: A Semidefinite Programming Approach
  - Optimal Decision-Making Based on Prediction Sets
  - Joint Learning in the Gaussian Single Index Model

### Semantic Cluster 36: detection / vision / image / robustness
- Size: 177 papers (2.7%); orals: 3; awards: 0; votes/paper: 2.95
- Top terms: detection; vision; image; robustness; computer vision; computer; applications computer; adversarial; feature; semantic; methods; applications; images; extensive; features; performance
- Topic groups: Applications (84); Deep Learning (39); Social Aspects (27); General Machine Learning (14); Unknown (12)
- Rule themes: Multimodal, vision-language, and video (154); Safety, alignment, governance, and risk (109); Memorization, evaluation, and generalization (104); Theory, optimization, and sampling (63); Systems, efficiency, and compression (53)
- Lexical overlaps: 25 (75); 10 (25); 2 (22); 17 (10); 14 (7)
- Central papers:
  - Less Precise Can Be More Reliable: A Systematic Evaluation of Quantization’s Impact on VLMs Beyond Accuracy
  - Target-Agnostic Calibration under Distribution Shift with Frequency-Aware Gradient Rectification
  - Robust Vision-Language Models via Manifold-Adversarial Adapters
  - Self-Calibrated Consistency can Fight Back for Adversarial Robustness in Vision-Language Models
- High-signal papers:
  - Mind Your Margin and Boundary: Are Your Distilled Datasets Truly Robust?
  - DroneDINO: Towards Heterogeneous Routed Mixture of Experts for Drone-based Unified Object Detection
  - Privacy-Aware Video Anomaly Detection: Guided Orthogonal Projection and a Comprehensive Evaluation Framework
  - Alterbute: Editing Intrinsic Attributes of Objects in Images

### Semantic Cluster 37: ai / position / social / position paper
- Size: 173 papers (2.6%); orals: 10; awards: 2; votes/paper: 5.13
- Top terms: ai; position; social; position paper; aspects; social aspects; human; argues; research; paper; paper argues; argue; systems; safety; evaluation; agents
- Topic groups: Social Aspects (113); Applications (18); General Machine Learning (18); Unknown (13); Theory (6)
- Rule themes: Safety, alignment, governance, and risk (143); Agents, tools, and computer use (85); Memorization, evaluation, and generalization (70); Interpretability and mechanistic analysis (61); RL for LLMs and verifiable rewards (47)
- Lexical overlaps: 28 (109); 11 (20); 23 (16); 17 (9); 1 (7)
- Central papers:
  - Position: Preregister Experiments with AI Agents
  - Position: Reliable AI Needs to Externalize Implicit Knowledge: A Human–AI Collaboration Perspective
  - A Positive Case for Faithfulness: Explanations Help Predict Model Behavior
  - Position: The Age of AI Agents Demands A New Scientific Paradigm To Sustain Trustworthy Science
- High-signal papers:
  - Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit
  - Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII)
  - Position: Anthropomorphic Misalignment Research Needs Stronger Evidence
  - Position: Stop Automating Peer Review Without Rigorous Evaluation

### Semantic Cluster 33: regret / online / bandits / algorithm
- Size: 172 papers (2.6%); orals: 8; awards: 0; votes/paper: 3.67
- Top terms: regret; online; bandits; algorithm; optimal; theory; online learning; bound; learning bandits; problem; bounds; sqrt; algorithms; study; setting; mathcal
- Topic groups: Theory (97); General Machine Learning (27); Unknown (12); Social Aspects (11); Reinforcement Learning (9)
- Rule themes: Theory, optimization, and sampling (163); Agents, tools, and computer use (48); Safety, alignment, governance, and risk (44); LLM reasoning and test-time compute (43); RL for LLMs and verifiable rewards (37)
- Lexical overlaps: 9 (151); 7 (5); 17 (5); 24 (3); 23 (2)
- Central papers:
  - Improved Algorithms for Nash Welfare in Linear Bandits
  - Follow-the-Perturbed-Leader for Decoupled Bandits: Best-of-Both-Worlds and Practicality
  - Online Social Welfare Function-based Resource Allocation
  - Online Conformal Prediction via Universal Portfolio Algorithms
- High-signal papers:
  - Minimax Optimal Strategy for Delayed Observations in Online Reinforcement Learning
  - Nash Equilibria in Games with Playerwise Concave Coupling Constraints: Existence and Computation
  - Towards Fair Sequential Decision-Making: A Causal Decomposition Approach
  - What Preferences Can—and Cannot—Predict in Multi-Agent Online Learning

### Semantic Cluster 15: graph / graph neural / graphs / networks
- Size: 166 papers (2.5%); orals: 4; awards: 0; votes/paper: 1.33
- Top terms: graph; graph neural; graphs; networks; node; neural networks; learning graph; neural; nodes; structural; methods; datasets; structure; deep; deep learning; gnns
- Topic groups: Deep Learning (107); General Machine Learning (21); Unknown (13); Optimization (12); Applications (4)
- Rule themes: Memorization, evaluation, and generalization (75); Theory, optimization, and sampling (74); Safety, alignment, governance, and risk (53); Systems, efficiency, and compression (46); Agents, tools, and computer use (40)
- Lexical overlaps: 5 (121); 25 (12); 17 (10); 9 (6); 22 (3)
- Central papers:
  - View Space: Learning Representation across Arbitrary Graphs
  - GraphFLEx: Unsupervised Structure Learning $\underline{\text{F}}$ramework for $\underline{\text{L}}$arge $\underline{\text{Ex}}$panding $\underline{\text{Graph}}$s
  - Plain Transformers are Surprisingly Powerful Link Predictors
  - SFCLTA: Spectral Fusion Contrastive Learning with Topology-Adaptive Graph Augmentation
- High-signal papers:
  - Which Algorithms Can Graph Neural Networks Learn?
  - MV-FGAD: Towards Efficient and Effective Federated Graph Anomaly Detection via Multi-view Learning
  - PhenoBrain: Phenotype-Conditioned Long-Range Communication for Multi-Modal Brain Network Analysis
  - Towards Hierarchy–Uniformity Equilibrium: Recovering Semantic Depth in Hypergraph Contrastive Learning

### Semantic Cluster 2: reward / reinforcement learning / reinforcement / rewards
- Size: 164 papers (2.5%); orals: 3; awards: 0; votes/paper: 27.48
- Top terms: reward; reinforcement learning; reinforcement; rewards; policy; rl; preference; feedback; training; language; optimization; human; large language; language models; reward models; large
- Topic groups: Deep Learning (71); Reinforcement Learning (51); Unknown (14); Social Aspects (12); Applications (10)
- Rule themes: RL for LLMs and verifiable rewards (158); Theory, optimization, and sampling (103); LLM reasoning and test-time compute (90); Memorization, evaluation, and generalization (79); Safety, alignment, governance, and risk (74)
- Lexical overlaps: 6 (59); 24 (49); 7 (25); 11 (7); 1 (7)
- Central papers:
  - REAL: Regression-Aware Reinforcement Learning for LLM-as-a-Judge
  - Implicit Actor Critic Coupling via a Supervised Learning Framework for RLVR
  - Real-Time Aligned Reward Model beyond Semantics
  - Alternating Reinforcement Learning for Rubric-Based Reward Modeling in Non-Verifiable LLM Post-Training
- High-signal papers:
  - Reinforcement Learning with Evolving Rubrics for Deep Research
  - Maximum Likelihood Reinforcement Learning
  - Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling
  - Reinforcement Learning via Self-Distillation

## Highest Program Signal

- Semantic cluster 37 (ai / position / social / position paper): 5.8% oral, 2.28x corpus baseline, 173 papers
- Semantic cluster 20 (transformers / attention / transformer / softmax): 5.1% oral, 2.01x corpus baseline, 98 papers
- Semantic cluster 40 (agents / agent / evaluation / agentic): 4.8% oral, 1.91x corpus baseline, 207 papers
- Semantic cluster 24 (language / language models / llms / large language): 4.8% oral, 1.9x corpus baseline, 290 papers
- Semantic cluster 32 (bayesian / probabilistic / posterior / probabilistic methods): 4.8% oral, 1.89x corpus baseline, 125 papers
- Semantic cluster 13 (dynamics / networks / latent / dynamical): 4.8% oral, 1.88x corpus baseline, 84 papers
- Semantic cluster 11 (reasoning / language / large language / language models): 4.7% oral, 1.87x corpus baseline, 211 papers
- Semantic cluster 33 (regret / online / bandits / algorithm): 4.7% oral, 1.83x corpus baseline, 172 papers
- Semantic cluster 8 (diffusion / sampling / diffusion models / generative): 4.4% oral, 1.74x corpus baseline, 136 papers
- Semantic cluster 29 (llm / memory / gpu / throughput): 4.3% oral, 1.7x corpus baseline, 116 papers

## Highest Public Attention Density

- Semantic cluster 35 (reasoning / rl / reinforcement / reinforcement learning): 38.76 votes/paper, 10.3% of public votes, 161 papers
- Semantic cluster 2 (reward / reinforcement learning / reinforcement / rewards): 27.48 votes/paper, 7.5% of public votes, 164 papers
- Semantic cluster 3 (attention / kv / context / cache): 20.77 votes/paper, 3.9% of public votes, 113 papers
- Semantic cluster 16 (action / robotics / vla / applications robotics): 19.19 votes/paper, 6.2% of public votes, 195 papers
- Semantic cluster 11 (reasoning / language / large language / language models): 18.32 votes/paper, 6.4% of public votes, 211 papers
- Semantic cluster 30 (agent / multi / search / agents): 16.96 votes/paper, 4.2% of public votes, 150 papers
- Semantic cluster 40 (agents / agent / evaluation / agentic): 16.88 votes/paper, 5.8% of public votes, 207 papers
- Semantic cluster 10 (continual / forgetting / continual learning / task): 16.38 votes/paper, 3.7% of public votes, 138 papers
- Semantic cluster 14 (decoding / diffusion / language / language models): 14.32 votes/paper, 3.4% of public votes, 145 papers
- Semantic cluster 26 (networks / training / deep / gradient): 13.31 votes/paper, 4.4% of public votes, 198 papers

## Researcher Use

- Use semantic clusters to identify neighborhoods that the lexical TF-IDF/SVD baseline may split by surface vocabulary.
- Use the semantic-vs-lexical overlap table to find unstable areas that need manual naming before slide or report use.
- Do not treat cluster IDs as final taxonomy labels. The IDs are stable only for this snapshot and script configuration.