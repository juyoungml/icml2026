# ICML 2026 Title-Level EDA

This is an initial exploratory pass over the official ICML virtual `papers.html` corpus.

## Corpus

- Rows parsed: 6,628
- Posters: 6,628
- Oral-designated papers matched by title: 168
- Position-prefixed titles: 213

Note: the official `papers.html` fallback lists paper pages as poster links. Oral designations are joined from the separate official oral-events page by normalized title.

## Top Title Terms

- `learning`: 1155
- `models`: 871
- `language`: 469
- `reasoning`: 465
- `diffusion`: 391
- `model`: 343
- `llm`: 328
- `optimization`: 322
- `generation`: 302
- `efficient`: 299
- `reinforcement`: 297
- `large`: 276
- `data`: 255
- `neural`: 243
- `llms`: 235
- `position`: 221
- `framework`: 212
- `alignment`: 211
- `multimodal`: 199
- `agents`: 188
- `robust`: 183
- `training`: 171
- `graph`: 171
- `adaptive`: 166
- `modeling`: 161

## Top Title Bigrams

- `language models`: 319
- `reinforcement learning`: 283
- `large language`: 199
- `diffusion models`: 112
- `time series`: 107
- `neural networks`: 96
- `language model`: 79
- `policy optimization`: 67
- `flow matching`: 67
- `vision-language models`: 60
- `llm agents`: 56
- `foundation models`: 49
- `representation learning`: 47
- `continual learning`: 45
- `diffusion language`: 45
- `optimal transport`: 42
- `federated learning`: 40
- `series forecasting`: 39
- `llm reasoning`: 37
- `vision language`: 31
- `anomaly detection`: 31
- `reasoning models`: 30
- `world models`: 30
- `contrastive learning`: 29
- `video generation`: 29

## Topic Buckets

- LLMs / language / agents: 2,160 (32.6%)
- Unbucketed / other: 1,707 (25.8%)
- Multimodal / vision / video: 1,129 (17.0%)
- Theory / optimization / statistics: 919 (13.9%)
- Reinforcement learning: 903 (13.6%)
- Systems / efficiency / compression: 899 (13.6%)
- Diffusion / generative models: 856 (12.9%)
- Privacy / fairness / safety: 552 (8.3%)
- AI for science / health: 150 (2.3%)
- Causality: 129 (1.9%)

## Oral-Designated Topic Buckets

- LLMs / language / agents: 58 (34.5%)
- Unbucketed / other: 43 (25.6%)
- Theory / optimization / statistics: 29 (17.3%)
- Systems / efficiency / compression: 23 (13.7%)
- Multimodal / vision / video: 23 (13.7%)
- Reinforcement learning: 18 (10.7%)
- Diffusion / generative models: 14 (8.3%)
- Privacy / fairness / safety: 13 (7.7%)
- Causality: 5 (3.0%)
- AI for science / health: 4 (2.4%)

## Example Titles by Topic

### LLMs / language / agents
- TVI-CoT: Text-Visual Interleaved Chain-of-Thought Reasoning for Multimodal Understanding
- ProjQ: Project-and-Quantize for Adapter-Aware LLM Compression
- SafeSearch: Automated Red-Teaming of LLM-Based Search Agents
- SpreadsheetArena: Decomposing Preference in LLM Generation of Spreadsheet Workbooks
- Query Circuits: Explaining How Language Models Answer User Prompts

### Reinforcement learning
- TVI-CoT: Text-Visual Interleaved Chain-of-Thought Reasoning for Multimodal Understanding
- Latent Spherical Flow Policy for Reinforcement Learning with Combinatorial Actions
- Compositional Transduction with Latent Analogies for Offline Goal-Conditioned Reinforcement Learning
- T$^2$PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning
- Tracking Drift: Variation-Aware Entropy Scheduling for Non-Stationary Reinforcement Learning

### Multimodal / vision / video
- TVI-CoT: Text-Visual Interleaved Chain-of-Thought Reasoning for Multimodal Understanding
- SCRWKV: Ultra-Compact Structure-Calibrated Vision-RWKV for Topological Crack Segmentation
- A robust PPG foundation model using multimodal physiological supervision
- Hyper-ICL: Attention Calibration with Hyperbolic Anchor Distillation for Multimodal In-Context Learning
- Enhancing Multi-Modal LLMs Reasoning via Difficulty-Aware Group Normalization

### Privacy / fairness / safety
- RubricRobustness: A Simple Framework for Evaluating the Robustness of Rubrics-Based Benchmarks
- SafeSearch: Automated Red-Teaming of LLM-Based Search Agents
- Position: Generative Engine Optimization Creates Underexamined Risks, Governance Must Target Concentration, Disclosure, and Academic Blind Spots
- A robust PPG foundation model using multimodal physiological supervision
- Position: Token Taxes Can Mitigate AI's Economic Risks

### Unbucketed / other
- SAQNN: Spectral Adaptive Quantum Neural Network as a Universal Approximator
- Data Augmentation of Contrastive Learning is Estimating Positive-incentive Noise
- FastSESR: Fast Scene-level Explicit Surface Reconstruction
- VBA: Vector Bundle Attention for Intrinsically Geometric Representation Learning
- Dynamic Fractal Mamba: A Neural Renormalization Group Flow for Scale-Invariant Sequence Modeling

### Systems / efficiency / compression
- ProjQ: Project-and-Quantize for Adapter-Aware LLM Compression
- SSA: Sparse Sparse Attention by Aligning Full and Sparse Attention Outputs in Feature Space
- T$^2$PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning
- Beyond Test-Time Training: Learning to Reason via Hardware-Efficient Optimal Control
- CSPLoRA: Confidence-Guided Structure Planning for Low-Rank Adaptation

### Diffusion / generative models
- SpreadsheetArena: Decomposing Preference in LLM Generation of Spreadsheet Workbooks
- Position: Generative Engine Optimization Creates Underexamined Risks, Governance Must Target Concentration, Disclosure, and Academic Blind Spots
- Generalized Discrete Diffusion with Self-Correction
- Dual-View Predictive Diffusion: Lightweight Speech Enhancement via Spectrogram-Image Synergy
- Adaptive Generation of Bias-Eliciting Questions for LLMs

### Theory / optimization / statistics
- Position: Generative Engine Optimization Creates Underexamined Risks, Governance Must Target Concentration, Disclosure, and Academic Blind Spots
- Flat Minima and Generalization: Insights from Stochastic Convex Optimization
- Beyond Test-Time Training: Learning to Reason via Hardware-Efficient Optimal Control
- Fairness in Aggregation: Optimal Top-$k$ and Improved Full Ranking
- Partial Identification under High-Dimensional Potential Outcomes and Confounders via Optimal Transport

### AI for science / health
- A robust PPG foundation model using multimodal physiological supervision
- Learning Biophysical Models of Large-Scale Multineuronal Data To Enable Precise Neurostimulation
- DIYHealth Suite: Dataset, Model, and Benchmark for Health Management at Home
- Learning Protein Structure-Function Relationships through Knowledge-guided Representation Decomposition
- Explicit representation of germline and non-germline residues improves antibody language modeling

### Causality
- CauScale: Neural Causal Discovery at Scale
- Towards Completeness in Causal Discovery from Soft Interventions with Known Targets
- Partial Identification under High-Dimensional Potential Outcomes and Confounders via Optimal Transport
- Causal Discovery for Irregularly Time Series with Consistency Guarantees
- Multi-Adapter Representation Interventions via Energy Calibration

## Interpretation Seeds

- Title-level evidence should be treated as directional; abstracts are needed for a stronger topic model.
- LLM, reasoning, reward, agent, and alignment terms should be compared against non-title metadata because titles often understate application area.
- Position papers can be isolated by the `Position:` prefix for governance and policy-theme analysis.
- Award papers over-index on diffusion, theory/sampling, safety/alignment, memorization, video attribution, and grokking.