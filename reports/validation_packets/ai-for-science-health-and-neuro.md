# AI for Science, Health, and Neuro

Manual validation packet for representative and boundary papers.

## Area Context

Headline: Scientific ML is broadening from surrogate modeling into foundation models for biological, physical, temporal, and neural data.

Fault lines:
- General ML architecture contribution versus domain-specific modeling contribution.
- Benchmark performance versus scientific validity, uncertainty, and deployability.
- Foundation-model pretraining versus small-data, mechanistic, or simulation-grounded methods.

What to read for:
- Is the evaluation tied to a real scientific decision or only a proxy benchmark?
- Are domain constraints, units, symmetries, and uncertainty modeled explicitly?
- Does the method improve discovery or forecasting under realistic data scarcity?

## Queue Summary

- Papers: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, program_signal_low_public_attention=4, taxonomy_boundary_cluster=2
- Papers from taxonomy-review clusters: 13
- Papers with GitHub URLs: 9

## Papers

### 1. Protein Autoregressive Modeling via Multiscale Structure Generation

Flags: fault_line_representative, oral, taxonomy-review, github

- Subarea: Protein, molecule, and biological modeling
- Votes: 31
- ICML URL: https://icml.cc/virtual/2026/poster/66808
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.04883
- GitHub URL: https://github.com/Ali2500/BURST-benchmark
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Application / domain study; Method / algorithm
- Method families: LLM post-training; Diffusion / flow; Transformer / attention
- Evaluation settings: science/domain; security/safety
- Result claim cues: scaling / efficiency; robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

We present protein autoregressive modeling (PAR), the first multi-scale autoregressive framework for protein backbone generation via coarse-to-fine next-scale prediction. Using the hierarchical nature of proteins, PAR generates structures that mimic sculpting a statue, forming a coarse topology and refining structural details over scales. To achieve this, PAR consists of three key components: (i) multi-scale downsampling operations that represent protein structures across multiple scales during training; (ii) an autoregressive transformer that encodes multi-scale information and produces conditional embeddings to guide structure generation; (iii) a flow-based backbone decoder that generates backbone atoms conditioned on these embeddings. Moreover, autoregressive models suffer from exposure bias, caused by the training and the generation procedure mismatch, and substantially degrades structure generation quality. We effectively alleviate this issue by adopting noisy context learning and scheduled sampling, enabling robust backbone generation. Notably, PAR exhibits strong zero-shot generalization, supporting flexible human-prompted conditional generation and motif scaffolding without requiring fine-tuning. On the unconditional generation benchmark, PAR effectively learns protein distributions and produces backbones of high design quality, and exhibits favorable scaling behavior. Together, these properties establish PAR as a promising framework for protein structure generation.

Validation checklist:
- [ ] Contribution type checked
- [ ] Method family checked
- [ ] Benchmarks/datasets/metrics checked
- [ ] Artifact status checked
- [ ] Fault-line relevance written

Manual notes:

- Primary contribution type:
- Method family:
- Benchmarks:
- Datasets:
- Metrics:
- Artifact status:
- Result character:
- Fault-line relevance:
- Notes:

### 2. dnaHNet: A Scalable and Hierarchical Foundation Model for Genomic Sequence Learning

Flags: fault_line_representative, oral, taxonomy-review

- Subarea: Protein, molecule, and biological modeling
- Votes: 20
- ICML URL: https://icml.cc/virtual/2026/poster/66118
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.10603
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Application / domain study
- Contribution types: Application / domain study; Method / algorithm
- Method families: Transformer / attention; Compression / efficiency
- Evaluation settings: science/domain
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: accuracy; flop

Abstract:

Genomic foundation models have the potential to decode DNA syntax, yet face a fundamental tradeoff. Standard subword tokenizers fragment biologically meaningful motifs such as codons and regulatory elements, while nucleotide-level models preserve biological coherence but incur prohibitive computational costs for long contexts. We introduce dnaHNet, a state-of-the-art tokenizer-free autoregressive model that segments and models genomic sequences end to end. Using a differentiable dynamic chunking mechanism, dnaHNet compresses raw nucleotides into latent tokens adaptively, balancing compression with predictive accuracy. Pretrained on prokaryotic genomes, dnaHNet outperforms leading architectures including StripedHyena2 in scaling and efficiency. This recursive chunking yields quadratic FLOP reductions, enabling $>3 \times$ inference speedup over Transformers. On zero-shot tasks, dnaHNet achieves superior performance in predicting protein variant fitness and gene essentiality, while automatically discovering hierarchical biological structures without supervision. These results establish dnaHNet as a scalable, interpretable framework for next-generation genomic modeling.

Validation checklist:
- [ ] Contribution type checked
- [ ] Method family checked
- [ ] Benchmarks/datasets/metrics checked
- [ ] Artifact status checked
- [ ] Fault-line relevance written

Manual notes:

- Primary contribution type:
- Method family:
- Benchmarks:
- Datasets:
- Metrics:
- Artifact status:
- Result character:
- Fault-line relevance:
- Notes:

### 3. Orthogonal Concept Erasure for Diffusion Models

Flags: fault_line_representative, oral, taxonomy-review, github

- Subarea: Latent dynamics, neuroscience, and dynamical systems
- Votes: 9
- ICML URL: https://icml.cc/virtual/2026/poster/63634
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.28902
- GitHub URL: https://github.com/HansSunY/OCE
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Method / algorithm
- Method families: Diffusion / flow; Graphs / geometry
- Evaluation settings: robotics/embodied; security/safety
- Result claim cues: negative / limitation; scaling / efficiency; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Concept erasure has emerged as a promising approach to mitigate undesired or unsafe content in diffusion models, yet existing methods still face significant limitations. While training-based methods are effective, their high computational cost limits scalability. Editing-based methods are more efficient and deployment-friendly, yet they struggle to simultaneously achieve precise concept erasure and preserve overall generative capacity. We identify this core limitation of the editing-based methods as reliance on additive parameter updates. Our empirical analysis reveals that concept semantics primarily depend on *neuron direction* rather than *neuron magnitude*, while overall generative capacity relies on the *angular geometry* of neurons. As additive updates inherently entangle direction, magnitude, and angular geometry, they inevitably introduce unintended interference between concept erasure and overall generation performance. To address this, we propose **Orthogonal Concept Erasure (OCE)**, which reformulates editing-based erasure as multiplicative parameter updates from a geometric perspective. Specifically, OCE applies layer-wise orthogonal transformations derived from a closed-form solution to the parameters, enabling precise concept erasure while preserving the neuron magnitude and angular geometry. Furthermore, to address conflicting constraints in multi-concept erasure, OCE introduces a subspace-level objective with structured subspace manipulation, yielding a more effective and scalable erasure. Extensive experiments on single- and multi-concept erasure demonstrate that OCE outperforms existing methods in concept erasure and non-target preservation, erasing up to 100 concepts in 4.3 s.

Validation checklist:
- [ ] Contribution type checked
- [ ] Method family checked
- [ ] Benchmarks/datasets/metrics checked
- [ ] Artifact status checked
- [ ] Fault-line relevance written

Manual notes:

- Primary contribution type:
- Method family:
- Benchmarks:
- Datasets:
- Metrics:
- Artifact status:
- Result character:
- Fault-line relevance:
- Notes:

### 4. LASER: Learning Active Sensing for Continuum Field Reconstruction

Flags: fault_line_representative, oral

- Subarea: Physical sciences, chemistry, and climate
- Votes: 4
- ICML URL: https://icml.cc/virtual/2026/poster/62307
- AlphaXiv URL: https://www.alphaxiv.org/abs/2604.19355
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: RL / policy optimization; Compression / efficiency
- Evaluation settings: none
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: reward

Abstract:

High-fidelity measurements of continuum physical fields are essential for scientific discovery and engineering design but remain challenging under sparse and constrained sensing. Conventional reconstruction methods typically rely on fixed sensor layouts, which cannot adapt to evolving physical states. We propose LASER, a unified, closed-loop framework that formulates active sensing as a Partially Observable Markov Decision Process (POMDP). At its core, LASER employs a continuum field latent world model that captures the underlying physical dynamics and provides intrinsic reward feedback. This enables a reinforcement learning policy to simulate ''what-if'' sensing scenarios within a latent imagination space. By conditioning sensor movements on predicted latent states, LASER navigates toward potentially high-information regions beyond current observations. Our experiments demonstrate that LASER consistently outperforms static and offline-optimized strategies, achieving high-fidelity reconstruction under sparsity across diverse continuum fields.

Validation checklist:
- [ ] Contribution type checked
- [ ] Method family checked
- [ ] Benchmarks/datasets/metrics checked
- [ ] Artifact status checked
- [ ] Fault-line relevance written

Manual notes:

- Primary contribution type:
- Method family:
- Benchmarks:
- Datasets:
- Metrics:
- Artifact status:
- Result character:
- Fault-line relevance:
- Notes:

### 5. From Text to Forecasts: Bridging Modality Gap with Temporal Evolution Semantic Space

Flags: fault_line_representative, oral, taxonomy-review

- Subarea: Time series and forecasting applications
- Votes: 4
- ICML URL: https://icml.cc/virtual/2026/poster/63982
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.12664
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Application / domain study; Method / algorithm
- Method families: Agents / tool use
- Evaluation settings: math/code/verifiable; language/llm; theory/synthetic
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Incorporating textual information into time-series forecasting holds promise for addressing event-driven non-stationarity; however, a fundamental modality gap hinders effective fusion: textual descriptions express temporal impacts implicitly and qualitatively, whereas forecasting models rely on explicit and quantitative signals. Through controlled semi-synthetic experiments, we show that existing methods over-attend to redundant tokens and struggle to reliably translate textual semantics into usable numerical cues. To bridge this gap, we propose \method{}, which introduces a Temporal Evolution Semantic Space as an intermediate bottleneck between modalities. This space consists of interpretable, numerically grounded temporal primitives—mean shift, volatility, shape, and lag—extracted from text by an LLM via structured prompting and filtered through confidence-aware gating. Experiments on four real-world datasets demonstrate up to a 29\% reduction in forecasting error compared to state-of-the-art uni-modal and multimodal baselines. The code is available at https://anonymous.4open.science/r/MMTSF.

Validation checklist:
- [ ] Contribution type checked
- [ ] Method family checked
- [ ] Benchmarks/datasets/metrics checked
- [ ] Artifact status checked
- [ ] Fault-line relevance written

Manual notes:

- Primary contribution type:
- Method family:
- Benchmarks:
- Datasets:
- Metrics:
- Artifact status:
- Result character:
- Fault-line relevance:
- Notes:

### 6. Protein Fold Classification at Scale: Benchmarking and Pretraining

Flags: fault_line_representative, oral, taxonomy-review, github

- Subarea: Protein, molecule, and biological modeling
- Votes: 2
- ICML URL: https://icml.cc/virtual/2026/poster/62145
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.18552
- GitHub URL: https://github.com/BorgwardtLab/TEDBench
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; Application / domain study; Method / algorithm
- Method families: none
- Evaluation settings: science/domain
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: TEDBench
- Datasets: TEDBench
- Metrics: none

Abstract:

Classifying protein topology is essential for deciphering biological function, but progress is held back by the lack of large-scale benchmarks that avoid duplicates and by models that do not scale well. We introduce TEDBench, a large-scale, non-redundant benchmark for protein fold classification constructed from the Encyclopedia of Domains (TED) and Foldseek-clustered AlphaFold structures. We show that on TEDBench, current protein representation learning methods either require very large models or fail to deliver strong performance. To address this challenge, we propose Masked Invariant Autoencoders (MiAE), a self-supervised framework for protein structure representation learning. MiAE uses an extremely high masking ratio of up to 90% with an $\mathrm{SE(3)}$-invariant encoder and a lightweight decoder that reconstructs backbone coordinates from the latent representation and mask tokens. MiAE scales well and outperforms supervised counterparts and state-of-the-art baselines on TEDBench, establishing a strong recipe for protein fold classification. To test transfer beyond AlphaFold structures, we further benchmark on a curated dataset from experimental structures of CATH 4.4. We will release TEDBench and model checkpoints.

Validation checklist:
- [ ] Contribution type checked
- [ ] Method family checked
- [ ] Benchmarks/datasets/metrics checked
- [ ] Artifact status checked
- [ ] Fault-line relevance written

Manual notes:

- Primary contribution type:
- Method family:
- Benchmarks:
- Datasets:
- Metrics:
- Artifact status:
- Result character:
- Fault-line relevance:
- Notes:

### 7. GeoPT: Scaling Physics Simulation via Lifted Geometric Pre-Training

Flags: public_attention_not_program_signal, github

- Subarea: Physical sciences, chemistry, and climate
- Votes: 72
- ICML URL: https://icml.cc/virtual/2026/poster/62854
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.20399
- GitHub URL: https://github.com/Physics-Scaling/GeoPT
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; Theory / proof; Method / algorithm
- Method families: Graphs / geometry
- Evaluation settings: science/domain; theory/synthetic
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Neural simulators promise efficient surrogates for physics simulation, but scaling them is bottlenecked by the prohibitive cost of generating high-fidelity training data. Pre-training on abundant off-the-shelf geometries offers a natural alternative, yet faces a fundamental gap: supervision on static geometry alone ignores dynamics and can lead to negative transfer on physics tasks. We present GeoPT, a unified pre-trained model for general physics simulation based on lifted geometric pre-training. The core idea is to augment geometry with synthetic dynamics, enabling dynamics-aware self-supervision without physics labels. Pre-trained on over one million samples, GeoPT consistently improves industrial-fidelity benchmarks spanning fluid mechanics for cars, aircraft, and ships, and solid mechanics in crash simulation, reducing labeled data requirements by 20-60% and accelerating convergence by 2$\times$. These results show that lifting with synthetic dynamics bridges the geometry-physics gap, unlocking a scalable path for neural simulation.

Validation checklist:
- [ ] Contribution type checked
- [ ] Method family checked
- [ ] Benchmarks/datasets/metrics checked
- [ ] Artifact status checked
- [ ] Fault-line relevance written

Manual notes:

- Primary contribution type:
- Method family:
- Benchmarks:
- Datasets:
- Metrics:
- Artifact status:
- Result character:
- Fault-line relevance:
- Notes:

### 8. TSRBench: A Comprehensive Multi-task Multi-modal Time Series Reasoning Benchmark for Generalist Models

Flags: public_attention_not_program_signal, taxonomy-review, github

- Subarea: Time series and forecasting applications
- Votes: 65
- ICML URL: https://icml.cc/virtual/2026/poster/63969
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.18744
- GitHub URL: https://github.com/tianyi-lab/TSRBench
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Theory / proof
- Method families: Reasoning / test-time compute
- Evaluation settings: robotics/embodied; language/llm
- Result claim cues: negative / limitation; scaling / efficiency
- Benchmarks: TSRBench
- Datasets: none
- Metrics: none

Abstract:

Time series data is ubiquitous in real-world scenarios and crucial for critical applications ranging from energy management to traffic control. Consequently, the ability to reason over time series is a fundamental skill for generalist models to solve complex problems. However, current benchmarks for generalist models largely overlook this dimension. To bridge this gap, we introduce TSRBench, a comprehensive multi-modal benchmark designed to stress-test the full spectrum of time series reasoning capabilities. TSRBench features: i) a diverse set of 4125 problems from 14 domains, and is categorized into 4 major dimensions: Perception, Reasoning, Prediction, and Decision-Making. ii) 15 tasks from the 4 dimensions evaluating essential reasoning capabilities (e.g., numerical reasoning). Through extensive experiments, we evaluated over 30 leading proprietary and open-source LLMs, VLMs, and TSLLMs within TSRBench. Our findings reveal that: i) scaling laws hold for perception and reasoning but break down for prediction; ii) strong reasoning does not guarantee accurate context-aware forecasting, indicating a decoupling between semantic understanding and numerical prediction; and iii) despite the complementary nature of textual and visual forms of time series as inputs, current multimodal models fail to effectively fuse them for reciprocal performance gains. TSRBench provides a standardized evaluation platform that not only highlights existing challenges but also offers valuable insights to advance generalist models.

Validation checklist:
- [ ] Contribution type checked
- [ ] Method family checked
- [ ] Benchmarks/datasets/metrics checked
- [ ] Artifact status checked
- [ ] Fault-line relevance written

Manual notes:

- Primary contribution type:
- Method family:
- Benchmarks:
- Datasets:
- Metrics:
- Artifact status:
- Result character:
- Fault-line relevance:
- Notes:

### 9. Understanding Self-Supervised Learning via Latent Distribution Matching

Flags: public_attention_not_program_signal, taxonomy-review, github

- Subarea: Time series and forecasting applications
- Votes: 33
- ICML URL: https://icml.cc/virtual/2026/poster/61214
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.03517
- GitHub URL: https://github.com/fmi-basel/latent_distribution_matching
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: LLM post-training; Diffusion / flow; Bayesian / probabilistic
- Evaluation settings: theory/synthetic
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Self-supervised learning (SSL) excels at finding general-purpose latent representations from complex data, yet lacks a unifying theoretical framework that explains the diverse existing methods and guides the design of new ones. We cast SSL as latent distribution matching (DM): learning representations that maximize their log-probability under an assumed latent model (alignment), while maximizing latent entropy to prevent collapse (uniformity). This view unifies independent component analysis with contrastive, non-contrastive, and predictive SSL methods, including stop-gradient approaches. Leveraging DM, we derive a nonlinear, sampling-free Bayesian filtering model with a Kalman-based predictor for high-dimensional timeseries. We further prove that predictive DM yields identifiable latent representations under mild assumptions, even with nonlinear predictors. Overall, DM clarifies the assumptions behind established SSL methods and provides principled guidance for developing new approaches.

Validation checklist:
- [ ] Contribution type checked
- [ ] Method family checked
- [ ] Benchmarks/datasets/metrics checked
- [ ] Artifact status checked
- [ ] Fault-line relevance written

Manual notes:

- Primary contribution type:
- Method family:
- Benchmarks:
- Datasets:
- Metrics:
- Artifact status:
- Result character:
- Fault-line relevance:
- Notes:

### 10. OpenTSLM: Time-Series Language Models for Reasoning over Multivariate Medical Text- and Time-Series Data

Flags: public_attention_not_program_signal, taxonomy-review, github

- Subarea: Time series and forecasting applications
- Votes: 32
- ICML URL: https://icml.cc/virtual/2026/poster/65261
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.02410
- GitHub URL: https://github.com/StanfordBDHG/OpenTSLM
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; System / infrastructure; Application / domain study
- Method families: LLM post-training; Reasoning / test-time compute; Agents / tool use; Transformer / attention
- Evaluation settings: math/code/verifiable; language/llm; science/domain
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: memory

Abstract:

Large Language Models (LLMs) have shown strong capability in interpreting multimodal data but remain limited in their ability to natively handle time-series data. Addressing this limitation could enable the translation of longitudinal and wearable sensing data into actionable insights and patient-facing digital health applications. We propose OpenTSLM, a family of Time Series Language Models that integrate time-series as a native modality into pretrained LLMs, enabling natural-language prompting and reasoning over multiple time-series. We implement two OpenTSLM variants based on soft prompting (OpenTSLM-SP) and cross-attention (OpenTSLM-Flamingo). To conduct comprehensive experiments on reasoning over medical text and time-series, we introduce three chain of thought (CoT) datasets: HAR-CoT (human activity recognition), Sleep-CoT (sleep staging), and ECG-QA-CoT (electrocardiogram question answering). Across tasks, OpenTSLM models consistently outperform baselines. OpenTSLMs with time-series encoders trained from scratch achieve 69.88% in sleep staging and 65.44% in HAR, while OpenTSLM combined with time series foundation models (TSFMs) achieve 68.33% and 67.64%, compared to 9.05% and 60.44% for fine-tuned text-only baselines. Additionally, we conduct expert evaluations with cardiologists, which show that OpenTSLMs exhibit strong reasoning capabilities and temporal understanding on raw sensor data for ECG-QA. We further show that OpenTSLM-Flamingo models scale better in memory as the number and length of time-series increase. To facilitate further research, we release all code, datasets, and models as open-source resources.

Validation checklist:
- [ ] Contribution type checked
- [ ] Method family checked
- [ ] Benchmarks/datasets/metrics checked
- [ ] Artifact status checked
- [ ] Fault-line relevance written

Manual notes:

- Primary contribution type:
- Method family:
- Benchmarks:
- Datasets:
- Metrics:
- Artifact status:
- Result character:
- Fault-line relevance:
- Notes:

### 11. AI Engram: In Search of Memory Traces in Artificial Intelligence

Flags: program_signal_low_public_attention, oral, taxonomy-review

- Subarea: Latent dynamics, neuroscience, and dynamical systems
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/64138
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: System / infrastructure
- Contribution types: System / infrastructure; Application / domain study; Method / algorithm
- Method families: Causal / data-centric; Graphs / geometry
- Evaluation settings: robotics/embodied; language/llm; theory/synthetic
- Result claim cues: scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: memory

Abstract:

Memory formation is fundamental to intelligence, yet whether deep neural networks preserve identifiable memory traces—analogous to biological memory units—remains an open question. This work introduces a geometric framework to identify such "AI engrams," by formalizing the neuroscientific criteria of specificity, reactivation, sufficiency, and necessity into a constrained inverse problem. We derive a closed-form estimator that isolates individual memory traces from globally entangled parameters. Theoretical analysis reveals that this biologically-derived solution corresponds to a natural gradient update on the parameter manifold. AI engrams enable surgical manipulation of learned knowledge: any subset of memories can be composed or erased through linear arithmetic, without iterative optimization. Experiments ranging from simple MLPs to LLMs demonstrate the causal validity and substantial scalability of AI engrams. Together, these results bridge theories of biological memory and artificial representation learning, offering geometric insight into how deep networks simultaneously support functional specificity within distributed storage.

Validation checklist:
- [ ] Contribution type checked
- [ ] Method family checked
- [ ] Benchmarks/datasets/metrics checked
- [ ] Artifact status checked
- [ ] Fault-line relevance written

Manual notes:

- Primary contribution type:
- Method family:
- Benchmarks:
- Datasets:
- Metrics:
- Artifact status:
- Result character:
- Fault-line relevance:
- Notes:

### 12. CoEvol-NO: State and Coordinate Co-Evolution with an Error-Driven Predictor-Corrector Paradigm for Neural Operator Transformer

Flags: program_signal_low_public_attention, oral, taxonomy-review

- Subarea: Latent dynamics, neuroscience, and dynamical systems
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/61526
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Theory / proof; Method / algorithm
- Method families: Transformer / attention
- Evaluation settings: theory/synthetic
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Despite the fast progress in neural operator learning, long-sequence modeling still is a standing challenge whereby latent states have been introduced with techniques well derived. Diverging from existing methods that treat latent states as transient variables or decoupled representations, CoEvol-NO introduces a {persistent state} to establish a {co-evolutionary framework}, where the latent state and mesh sequence are updated jointly and bidirectionally. Inspired by classical numerical methods, we model the layer-wise state evolution as a {Predictor-Corrector (PC)} process. Specifically, a ``Predictor'' generates a tentative target, followed by a ``Corrector'' that refines the persistent state via an {error-driven update mechanism}. Furthermore, our theoretical analysis reveals that the widely used \textit{direct substitution} and \textit{residual update} paradigms are essentially {first-order approximations} of this error-driven correction under different loss assumptions. We theoretically prove that CoEvol-NO achieves strict {linear time complexity}. Extensive experiments on five standard benchmarks and two large-scale industrial design tasks demonstrate that CoEvol-NO consistently achieves {state-of-the-art (SOTA)} performance.

Validation checklist:
- [ ] Contribution type checked
- [ ] Method family checked
- [ ] Benchmarks/datasets/metrics checked
- [ ] Artifact status checked
- [ ] Fault-line relevance written

Manual notes:

- Primary contribution type:
- Method family:
- Benchmarks:
- Datasets:
- Metrics:
- Artifact status:
- Result character:
- Fault-line relevance:
- Notes:

### 13. Geometric Flow Grounding: A Unified Manifold Decoupling Framework for Dynamics Discovery and Verification

Flags: program_signal_low_public_attention, oral, taxonomy-review

- Subarea: Latent dynamics, neuroscience, and dynamical systems
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/64932
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: Reasoning / test-time compute; Diffusion / flow; Compression / efficiency; Graphs / geometry
- Evaluation settings: vision/video; theory/synthetic
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Modeling complex dynamics from observational data is fundamental to scientific discovery and artificial intelligence. However, existing approaches ranging from Neural ODEs to diffusion models are often plagued by the entanglement of static state representations and instantaneous motion, leading to accumulated errors and off-manifold hallucinations where predicted trajectories violate intrinsic geometric constraints. To address this, we propose Geometric Flow Grounding, a unified framework that enforces dynamic evolution strictly along the tangent bundle of the learned data manifold via a differentiable Neural Tangent Projection Layer. By geometrically decoupling state representation from tangential dynamics, our method generalizes across diverse data regimes. In the context of scientific discovery, we demonstrate that the projection layer eliminates numerical aliasing in sparse dynamical systems and recovers interpretable gene regulatory motifs from single-cell data by disentangling states from developmental velocities. Bridging to trustworthy AI, we further repurpose the geometric projection residual as a zero-shot metric for deepfake video detection, identifying generative inconsistencies against the implicit flow of pre-trained world models. Our results establish manifold-constrained projection as a universal operator for both discovering natural laws and verifying synthetic content.

Validation checklist:
- [ ] Contribution type checked
- [ ] Method family checked
- [ ] Benchmarks/datasets/metrics checked
- [ ] Artifact status checked
- [ ] Fault-line relevance written

Manual notes:

- Primary contribution type:
- Method family:
- Benchmarks:
- Datasets:
- Metrics:
- Artifact status:
- Result character:
- Fault-line relevance:
- Notes:

### 14. ReViT: Rotational-equivariant Vision Transformers for Neural PDE Solvers

Flags: program_signal_low_public_attention, oral

- Subarea: Physical sciences, chemistry, and climate
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/62510
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Method / algorithm
- Method families: Transformer / attention; Graphs / geometry
- Evaluation settings: vision/video; science/domain
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Physics obeys strict symmetries like rotational equivariance. However, the standard Transformer architectures widely used in physics foundation models do not enforce these constraints by construction. We introduce ReViT, a rotationally equivariant Vision Transformer framework for neural PDE solvers operating on grid-based physical fields that strictly enforces rotational equivariance. ReViT maps scalar and vector inputs into locally invariant representations derived from physics-based canonical bases, enabling the use of standard self-attention without symmetry violations. Built on a hierarchical Swin-style backbone with a precomputed reference basis pyramid, ReViT preserves equivariance across multi-scale operations. We evaluate ReViT on a wide range of 2D and 3D PDE benchmarks, such as Magnetohydrodynamics and Turbulent Channel Flows, demonstrating significant gains over state-of-the-art baselines. ReViT exhibits strong generalization, and reduces MSE by up to 65\% compared with the best-performing alternatives.

Validation checklist:
- [ ] Contribution type checked
- [ ] Method family checked
- [ ] Benchmarks/datasets/metrics checked
- [ ] Artifact status checked
- [ ] Fault-line relevance written

Manual notes:

- Primary contribution type:
- Method family:
- Benchmarks:
- Datasets:
- Metrics:
- Artifact status:
- Result character:
- Fault-line relevance:
- Notes:

### 15. Universal Learning of Nonlinear Dynamics

Flags: taxonomy_boundary_cluster, taxonomy-review, evidence-low, github

- Subarea: Latent dynamics, neuroscience, and dynamical systems
- Votes: 30
- ICML URL: https://icml.cc/virtual/2026/poster/65255
- AlphaXiv URL: https://www.alphaxiv.org/abs/2508.11990
- GitHub URL: https://github.com/conancarrow/Lusch
- Artifact confidence: github_url_no_stars
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: System / infrastructure
- Contribution types: System / infrastructure; Method / algorithm
- Method families: none
- Evaluation settings: robotics/embodied
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

We study the fundamental problem of one-step prediction of a marginally stable unknown nonlinear dynamical system. We describe an algorithm for this problem, based on the technique of spectral filtering, which learns a mapping from past observations to the next based on a spectral representation of the system. Using techniques from online convex optimization, we prove vanishing prediction error for any nonlinear dynamical system that has finitely many marginally stable modes, with rates governed by a novel quantitative control-theoretic notion of learnability. The main technical component of our method is a new spectral filtering algorithm for linear dynamical systems, which incorporates past observations and applies to general noisy and marginally stable systems. This significantly generalizes the original spectral filtering algorithm to both asymmetric dynamics as well as incorporating noise correction, and is of independent interest.

Validation checklist:
- [ ] Contribution type checked
- [ ] Method family checked
- [ ] Benchmarks/datasets/metrics checked
- [ ] Artifact status checked
- [ ] Fault-line relevance written

Manual notes:

- Primary contribution type:
- Method family:
- Benchmarks:
- Datasets:
- Metrics:
- Artifact status:
- Result character:
- Fault-line relevance:
- Notes:

### 16. Scaling Vision Transformers for Functional MRI with Flat Maps

Flags: taxonomy_boundary_cluster, taxonomy-review, github

- Subarea: Spiking neural networks and neural signals
- Votes: 21
- ICML URL: https://icml.cc/virtual/2026/poster/61249
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.13768
- GitHub URL: https://github.com/MedARC-AI/fmri-fm
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high; small cluster

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Application / domain study; Method / algorithm
- Method families: Agents / tool use; Transformer / attention
- Evaluation settings: math/code/verifiable; vision/video
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

We propose a simple strategy for training a foundation model on functional MRI (fMRI) data: we adapt the standard Vision Transformer to fMRI by first converting each 3D fMRI volume to a 2D map using a standard cortical flat map projection. We train spatiotemporal masked autoencoders (MAE) on 2.3K hours of fMRI flat map videos. Our model (CortexMAE) outperforms identical MAE models trained on parcel-averaged or native volume data. We perform the first quantitative scaling analyses for fMRI and observe strict power law scaling. Finally, we develop the first open evaluation suite for fMRI foundation models and use it to perform a comprehensive comparison. On cognitive state decoding, our model outperforms all models by a wide margin. On clinical trait prediction, however, we report an important mixed result: all models show inconsistent performance (including our own). We hope that by introducing reproducible benchmarks and a strong, simple baseline, we can help establish a clear frontier for fMRI foundation models. Code is available at \url{https://anonymous.4open.science/r/cortex_mae}.

Validation checklist:
- [ ] Contribution type checked
- [ ] Method family checked
- [ ] Benchmarks/datasets/metrics checked
- [ ] Artifact status checked
- [ ] Fault-line relevance written

Manual notes:

- Primary contribution type:
- Method family:
- Benchmarks:
- Datasets:
- Metrics:
- Artifact status:
- Result character:
- Fault-line relevance:
- Notes:
