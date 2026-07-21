# Graphs, Geometry, and Representation Learning

Manual validation packet for representative and boundary papers.

## Area Context

Headline: Graph and geometric methods remain a bridge between structure-aware theory and domain-specific representations.

Fault lines:
- Equivariance and invariance as architectural priors versus learned latent geometry.
- Graph foundation/generalization claims versus task-specific message-passing improvements.
- Theoretical expressivity versus scalability on real graph and geometric data.

What to read for:
- Which symmetries or structural assumptions are encoded, and are they valid for the data?
- Does the method scale beyond curated graph benchmarks?
- Are representation claims validated by transfer, robustness, or interpretability?

## Queue Summary

- Papers: 16
- Selection mix: fault_line_representative=6, taxonomy_boundary_cluster=6, public_attention_not_program_signal=4
- Papers from taxonomy-review clusters: 12
- Papers with GitHub URLs: 6

## Papers

### 1. Which Algorithms Can Graph Neural Networks Learn?

Flags: fault_line_representative, oral, github

- Subarea: Graph neural networks and graph learning
- Votes: 7
- ICML URL: https://icml.cc/virtual/2026/poster/65099
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.13106
- GitHub URL: https://github.com/Timo-SH/exact_nar
- Artifact confidence: github_url_no_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: Reasoning / test-time compute; Compression / efficiency; Graphs / geometry
- Evaluation settings: math/code/verifiable; theory/synthetic
- Result claim cues: negative / limitation
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

In recent years, there has been growing interest in understanding neural architectures' ability to learn to execute discrete algorithms, a line of work often referred to as neural algorithmic reasoning. The goal is to integrate algorithmic reasoning capabilities into larger neural pipelines. Many such architectures are based on (message-passing) graph neural networks (MPNNs), owing to their permutation equivariance and ability to deal with sparsity and variable-sized inputs. However, existing work is either largely empirical and lacks formal guarantees or it focuses solely on expressivity, leaving open the question of when and how such architectures generalize beyond a finite training set. In this work, we propose a general theoretical framework that characterizes the necessary conditions under which MPNNs can learn an algorithm from a training set of small instances and provably approximate its behavior on inputs of arbitrary size. Our framework applies to a broad class of algorithms, including single-source shortest paths, minimum spanning trees, and general dynamic programming problems, such as the $0$-$1$ knapsack problem. In addition, we establish impossibility results for a wide range of algorithmic tasks, showing that standard MPNN cannot compute them. We derive more expressive MPNN-like architectures that overcome these limitations. Finally, we refine our analysis for the Bellman–Ford algorithm, yielding substantially smaller required training sets and significantly extending the recent work of Nerem et al., 2025 by allowing for a differentiable regularization loss. Empirical results largely support our theoretical findings.

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

### 2. Foundations of Equivariant Deep Learning: Unifying Graph and Sheaf Neural Networks

Flags: fault_line_representative, oral, taxonomy-review

- Subarea: Equivariant graph and geometric networks
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/63078
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; small cluster

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: Graphs / geometry
- Evaluation settings: theory/synthetic
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

We develop order-equivariant neural networks (OENN), which generalize standard graph message passing and sheaf neural networks via the face-poset viewpoint. We (i) characterize all linear order-equivariant maps, (ii) build OENN layers, and (iii) prove a universal approximation theorem (UAT) for continuous order-equivariant maps, which is a new result even when restricted to sheaf neural networks (for which no UAT was known before). We illustrate the framework on graph and sheaf models. Our results can also be seen as extending the UAT for graph neural networks to a more general setting that subsumes sheaf neural networks as well.

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

### 3. Necessary Conditions for Compositional Generalization of Embedding Models

Flags: fault_line_representative, oral, taxonomy-review

- Subarea: Geometric representation learning and manifolds
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/65761
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Dataset / data resource; Theory / proof; System / infrastructure; Method / algorithm
- Method families: Graphs / geometry
- Evaluation settings: theory/synthetic
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: clip

Abstract:

Compositional generalization, the ability to recognize familiar parts in novel contexts, is a defining property of intelligent systems. Modern models are trained on massive datasets, yet these are vanishingly small compared to the full combinatorial space of possible data, raising the question of whether models can reliably generalize to unseen combinations. To formalize what this requires, we propose a set of practically motivated desiderata that any compositionally generalizing system must satisfy, and analyze their implications under standard training with linear classification heads. We show that these desiderata necessitate \emph{linear factorization}, where representations decompose additively into per-concept components, and further imply near-orthogonality across factors. We establish dimension bounds that link the number of concepts to the geometry of representations. Empirically, we survey CLIP and SigLIP families, finding strong evidence for linear factorization, approximate orthogonality, and a tight correlation between the quality of factorization and compositional generalization. Together, our results identify the structural conditions that embeddings must satisfy for compositional generalization, and provide both theoretical clarity and empirical diagnostics for developing foundation models that generalize compositionally.

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

### 4. MV-FGAD: Towards Efficient and Effective Federated Graph Anomaly Detection via Multi-view Learning

Flags: fault_line_representative, oral, evidence-low

- Subarea: Graph neural networks and graph learning
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/60641
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Method / algorithm
- Method families: Graphs / geometry
- Evaluation settings: none
- Result claim cues: negative / limitation; scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Federated graph anomaly detection (GAD) aims to identify abnormal nodes in distributed subgraphs through collaborative learning. However, existing methods suffer from two limitations. 1) Their reliance on neighborhood aggregation assumes that anomalous information can be sufficiently captured, which often fails in federated learning with partitioned client subgraphs. 2) They overlook the detection bottleneck caused by weak attribute or structural anomalies. To tackle these challenges, we revisit federated GAD and reveal that weak anomalies exhibit harder-to-detect signals compared to strong anomalies. Specifically, we propose MV-FGAD, an efficient and effective federated GAD framework based on multi-view learning designed to mine anomalies of varying strengths. MV-FGAD introduces a federated knowledge learning module to aggregate and broadcast shared knowledge, which is further exploited to optimize local topological structures. Moreover, it designs a multi-view learning mechanism to capture diverse anomaly patterns, and adopts Mahalanobis distance–based scoring strategy to quantify node abnormality across views. Extensive experiments on real-world datasets of varying types and scales demonstrate MV-FGAD's efficiency and effectiveness.

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

### 5. PhenoBrain: Phenotype-Conditioned Long-Range Communication for Multi-Modal Brain Network Analysis

Flags: fault_line_representative, oral

- Subarea: Graph neural networks and graph learning
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/65858
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; System / infrastructure; Method / algorithm
- Method families: Reasoning / test-time compute; Transformer / attention; Graphs / geometry
- Evaluation settings: vision/video
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Multi-modal brain network analysis aims to predict neuropsychiatric status from functional connectomes with heterogeneous phenotypes. However, most existing methods treat phenotypes as auxiliary features and perform late fusion, implicitly assuming that the connectome representation should be learned in the same way regardless of phenotype. However, in clinical neuroscience the same functional connectivity pattern may support different conclusions under different phenotype contexts. To bridge this gap, we propose PhenoBrain, a novel framework for multi-modal brain network analysis that injects phenotype information at the mechanism level rather than only at the classifier level. Specifically, we propose a phenotype-conditioned long-range routing mechanism, which learns a subject-specific multi-hop communication kernel to model long-range connectome interactions. Furthermore, we propose a phenotypic-guided attention mechanism regulation method, which uses phenotypic information as a conditional prior to regulate the learning process of attention in brain networks. To verify the effectiveness of our method, we constructed two multi-modal brain network analysis datasets based on open-source image data. Extensive experiments demonstrate that PhenoBrain achieves state-of-the-art performance.

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

### 6. Towards Hierarchy–Uniformity Equilibrium: Recovering Semantic Depth in Hypergraph Contrastive Learning

Flags: fault_line_representative, oral, evidence-low

- Subarea: Graph neural networks and graph learning
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/65990
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Method / algorithm
- Method families: LLM post-training; Graphs / geometry
- Evaluation settings: none
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Hypergraph contrastive learning is an effective paradigm for representation learning on higher-order relational data, yet existing methods largely ignore that hyperedges link nodes with multi-level semantics. Standard contrastive objectives emphasize instance discrimination via hyperspherical uniformity and tend to push embeddings apart in an indiscriminate manner. We show that this leads to a *Hierarchy–Uniformity Conflict*, whose geometric manifestation is *Semantic Flattening*, where the semantic depth of hyperedges collapses into a nearly flat cloud of instances. To address this issue, we introduce **HyperDepth**, a hypergraph contrastive learning framework that moves representations towards a hierarchy–uniformity equilibrium by jointly coordinating spectral and geometric signals. HyperDepth employs a decoupled spectral encoding scheme with adaptive gating so that high-frequency components focus on local instance discrimination while low-frequency components capture global hierarchical structure. On top of this, an energy-based hierarchical Alignment module attaches a learnable prototype tree to the representation space and minimizes an interpretable energy functional to recover the semantic depth of hyperedges. Theoretically, under a mild frequency-separation assumption, we show that the local contrastive and global hierarchical objectives operate on orthogonal spectral components and admit equilibrium embeddings that preserve semantic depth while still retaining instance-level discrimination. Experiments on 15 hypergraph datasets and 17 supervised and self-supervised baselines, spanning homophilic and heterophilic regimes, show that HyperDepth attains strong performance with the best average rank.

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

### 7. Deep sequence models tend to memorize geometrically; it is unclear why.

Flags: public_attention_not_program_signal, taxonomy-review

- Subarea: Geometric representation learning and manifolds
- Votes: 76
- ICML URL: https://icml.cc/virtual/2026/poster/65556
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.26745
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; System / infrastructure; Method / algorithm
- Method families: Reasoning / test-time compute; Transformer / attention; Graphs / geometry
- Evaluation settings: security/safety; theory/synthetic
- Result claim cues: scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: memory

Abstract:

Deep sequence models are said to store atomic facts predominantly in the form of associative memory: a brute-force lookup of co-occurring entities. We identify a dramatically different form of storage of atomic facts that we term as geometric memory. Here, the model has synthesized embeddings encoding novel global relationships between all entities, including ones that do not co-occur in training. Such storage is powerful: for instance, we show how it transforms a hard reasoning task involving an $\ell$-fold composition into an easy-to-learn $1$-step navigation task. From this phenomenon, we extract fundamental aspects of neural embedding geometries that are hard to explain. We argue that the rise of such a geometry, as against a lookup of local associations, cannot be straightforwardly attributed to typical supervisory, architectural, or optimizational pressures. Counterintuitively, a geometry is learned even when it is more complex than the brute-force lookup. Then, by analyzing a connection to Node2Vec, we demonstrate how the geometry stems from a spectral bias that---in contrast to prevailing theories---indeed arises naturally despite the lack of various pressures. This analysis also points out to practitioners a visible headroom to make Transformer memory more strongly geometric. We hope the geometric view of parametric memory encourages revisiting the default intuitions that guide researchers in areas like knowledge acquisition, capacity, discovery, and unlearning.

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

### 8. Who Said Neural Networks Aren't Linear?

Flags: public_attention_not_program_signal, taxonomy-review, evidence-low, github

- Subarea: Equivariant graph and geometric networks
- Votes: 74
- ICML URL: https://icml.cc/virtual/2026/poster/65316
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.08570
- GitHub URL: https://github.com/assafshocher/Linearizer
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; small cluster

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: Diffusion / flow
- Evaluation settings: none
- Result claim cues: scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Neural networks are famously nonlinear. However, linearity is defined relative to a pair of vector spaces, $f:\mathcal{X}\to\mathcal{Y}$. Leveraging the algebraic concept of transport of structure, we propose a method to explicitly identify non-standard vector spaces where a neural network acts as a linear operator. When sandwiching a linear operator $A$ between two invertible neural networks, $f(x)=g_y^{-1}(A g_x(x))$, the corresponding vector spaces $\mathcal{X}$ and $\mathcal{Y}$ are induced by newly defined addition and scaling actions derived from $g_x$ and $g_y$. We term this kind of architecture a Linearizer. This framework makes the entire arsenal of linear algebra, including SVD, pseudo-inverse, orthogonal projection and more, applicable to nonlinear mappings. Furthermore, we show that the composition of two Linearizers that share a neural network is also a Linearizer. We leverage this property and demonstrate that training diffusion models using our architecture makes the hundreds of sampling steps collapse into a single step. We further utilize our framework to enforce idempotency (i.e.\ $f(f(x))=f(x)$) on networks leading to a globally projective generative model and to demonstrate modular style transfer.

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

### 9. Thinking with Geometry: Active Geometry Integration for Spatial Reasoning

Flags: public_attention_not_program_signal, taxonomy-review, github

- Subarea: Geometric representation learning and manifolds
- Votes: 70
- ICML URL: https://icml.cc/virtual/2026/poster/66536
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.06037
- GitHub URL: https://github.com/Li-Hao-yuan/GeoThinker
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: Reasoning / test-time compute; Transformer / attention; Graphs / geometry
- Evaluation settings: vision/video; robotics/embodied; language/llm
- Result claim cues: negative / limitation; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Recent progress in spatial reasoning with Multimodal Large Language Models (MLLMs) increasingly leverages geometric priors from 3D encoders. However, most existing integration strategies remain passive: geometry is exposed as a global stream and fused in an indiscriminate manner, which often induces semantic-geometry misalignment and redundant signals. We propose GeoThinker, a framework that shifts the paradigm from passive fusion to active perception. Instead of feature mixing, GeoThinker enables the model to selectively retrieve geometric evidence conditioned on its internal reasoning demands. GeoThinker achieves this through Spatial-Grounded Fusion applied at carefully selected VLM layers, where semantic visual priors selectively query and integrate task-relevant geometry via frame-strict cross-attention, further calibrated by Importance Gating that biases per-frame attention toward task-relevant structures. Comprehensive evaluation results show that GeoThinker sets a new state-of-the-art in spatial intelligence, achieving a peak score of 72.6 on the VSI-Bench. Furthermore, GeoThinker demonstrates robust generalization and significantly improved spatial perception across complex downstream scenarios, including embodied referring and autonomous driving. Our results indicate that the ability to actively integrate spatial structures is essential for next-generation spatial intelligence.

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

### 10. From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers

Flags: public_attention_not_program_signal, taxonomy-review

- Subarea: Geometric representation learning and manifolds
- Votes: 62
- ICML URL: https://icml.cc/virtual/2026/poster/62200
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.06923
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: Transformer / attention
- Evaluation settings: vision/video; theory/synthetic
- Result claim cues: negative / limitation; robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Vafa et al. recently showed that a transformer fails to acquire an internal Newtonian world model when trained on synthetic planetary-motion data. How can we fix this problem? We find that inductive biases are key to learning the veridical world model: (1) **Spatial smoothness** is required for any world model to be learned. However, naive tokenization may disrupt smoothness since two close points in physical space may be far apart in token embedding space without sufficient training or data. We fix this by formulating the prediction problem as regression instead of classification. (2) **Spatial stability** makes the prediction robust to noise, which is not guaranteed by default, but can be taught via correcting in-context noise perturbations. (3) With both spatial smoothness and stability built in, further imposing **temporal locality** induces a Newtonian world model, while the lack of this knowledge induces a Keplerian world model -- fitting elliptical parameters instead of computing gravitational forces. Our results suggest that even simple general inductive biases are powerful enough to induce correct and specific world models. The inductive biases do not need to know that much about the underlying law to be learned, but without them, it is impossible to learn.

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

### 11. Revisiting the Platonic Representation Hypothesis: An Aristotelian View

Flags: taxonomy_boundary_cluster, taxonomy-review, evidence-low, github

- Subarea: Geometric representation learning and manifolds
- Votes: 62
- ICML URL: https://icml.cc/virtual/2026/poster/60968
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.14486
- GitHub URL: https://github.com/mlbio-epfl/Aristotelian
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: none
- Evaluation settings: none
- Result claim cues: scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

The Platonic Representation Hypothesis suggests that representations from neural networks are converging to a common statistical model of reality. We show that the existing metrics used to measure representational similarity are *confounded by network scale*: increasing model depth or width can systematically inflate representational similarity scores. To correct these effects, we introduce a permutation-based null-calibration framework that transforms any representational similarity metric into a calibrated score with statistical guarantees. We revisit the Platonic Representation Hypothesis with our calibration framework, which reveals a nuanced picture: the apparent convergence reported by global spectral measures largely disappears after calibration, while local neighborhood similarity, but not local distances, retains significant agreement across different modalities. Based on these findings, we propose the *Aristotelian Representation Hypothesis*: representations in neural networks are converging to shared local neighborhood relationships.

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

### 12. A Deep Learning Model of Mental Rotation Informed by Interactive VR Experiments

Flags: taxonomy_boundary_cluster, taxonomy-review, github

- Subarea: Geometric representation learning and manifolds
- Votes: 46
- ICML URL: https://icml.cc/virtual/2026/poster/61927
- AlphaXiv URL: https://www.alphaxiv.org/abs/2512.13517
- GitHub URL: https://github.com/rkhz/menrot
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Application / domain study
- Contribution types: Application / domain study
- Method families: Reasoning / test-time compute; Agents / tool use; Graphs / geometry
- Evaluation settings: vision/video; theory/synthetic
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Mental rotation—the ability to compare objects seen from different viewpoints—is a fundamental example of mental simulation and spatial world modeling in humans. Here we propose a mechanistic model of human mental rotation, leveraging recent advances in deep, equivariant, and neuro-symbolic learning. Our model consists of three stacked components: (1) an equivariant neural encoder, producing 3D spatial representations of objects from images, (2) a neuro-symbolic object encoder, deriving symbolic objects descriptions from these spatial representations, and (3) a neural decision agent, comparing these symbolic descriptions to prescribe rotation simulations in 3D latent space via a recurrent pathway. Our model design is guided by the abundant experimental literature on mental rotation, which we complemented with experiments in VR where participants could at times manipulate the objects to compare. Our model captures well the performance, response times and behavior of participants in our and others' experiments, and through ablation studies we demonstrate the necessity of each component. Our work adds to a recent collection of deep neural models of human spatial reasoning, further demonstrating the potency of integrating deep, equivariant, and symbolic representations to model the human mind.

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

### 13. Semantic Tube Prediction: Beating LLM Data Efficiency with JEPA

Flags: taxonomy_boundary_cluster, taxonomy-review, github

- Subarea: Geometric representation learning and manifolds
- Votes: 44
- ICML URL: https://icml.cc/virtual/2026/poster/64567
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.22617
- GitHub URL: https://github.com/galilai-group/llm-jepa
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: Graphs / geometry
- Evaluation settings: language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: accuracy

Abstract:

Large Language Models (LLMs) obey consistent scaling laws---empirical power-law fits that predict how loss decreases with compute, data, and parameters. While predictive, these laws are descriptive rather than prescriptive: they characterize typical training, not optimal training. Surprisingly few works have successfully challenged the data-efficiency bounds implied by these laws---which is our primary focus. To that end, we introduce the Geodesic Hypothesis, positing that token sequences trace geodesics on a smooth semantic manifold and are therefore locally linear. Building on this principle, we propose a novel Semantic Tube Prediction (STP) task, a JEPA-style regularizer that confines hidden-state trajectories to a tubular neighborhood of the geodesic. STP generalizes JEPA to language without requiring explicit multi-view augmentations. We show this constraint improves signal-to-noise ratio, and consequently preserves diversity by preventing trajectory collisions during inference. Empirically, STP allows LLMs to match baseline accuracy with 16$\times$ less training data, directly violating the data term of Chinchilla-style scaling laws and demonstrating that principled geometric priors can surpass brute-force scaling.

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

### 14. Dynamics Reveals Structure: Challenging the Linear Propagation Assumption

Flags: taxonomy_boundary_cluster, taxonomy-review

- Subarea: Equivariant graph and geometric networks
- Votes: 41
- ICML URL: https://icml.cc/virtual/2026/poster/64453
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.21601
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; small cluster

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof
- Method families: Reasoning / test-time compute; Graphs / geometry
- Evaluation settings: theory/synthetic
- Result claim cues: negative / limitation
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Neural networks adapt through first-order parameter updates, yet it remains unclear whether such updates preserve logical coherence. We investigate the geometric limits of the Linear Propagation Assumption (LPA), the premise that local updates coherently propagate to logical consequences. To formalize this, we adopt relation algebra and study three core operations on relations: negation flips truth values, converse swaps argument order, and composition chains relations. For negation and converse, we prove that guaranteeing direction-agnostic first-order propagation necessitates a tensor factorization separating entity-pair context from relation content. However, for composition, we identify a fundamental obstruction. We show that composition reduces to conjunction, and prove that any conjunction well-defined on linear features must be bilinear. Since bilinearity is incompatible with negation, this forces the feature map to collapse. These results suggest that failures in knowledge editing, the reversal curse, and multi-hop reasoning may stem from common structural limitations inherent to the LPA.

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

### 15. Learning Multi-Agent Coordination via Sheaf-ADMM

Flags: taxonomy_boundary_cluster, taxonomy-review

- Subarea: Equivariant graph and geometric networks
- Votes: 39
- ICML URL: https://icml.cc/virtual/2026/poster/62363
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.31005
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; small cluster

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: Agents / tool use; Graphs / geometry
- Evaluation settings: vision/video
- Result claim cues: robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

We present a differentiable optimization framework for multi-agent coordination. An input is decomposed into overlapping local views, each processed by an agent that solves a convex subproblem parametrized by a neural encoder. Agents coordinate through the Alternating Direction Method of Multipliers (ADMM) with inter-agent constraints specified by a cellular sheaf. The sheaf specifies which aspects of neighboring solutions must agree. Backpropagating through the unrolled optimization jointly trains encoders, decoders, and sheaf structure. We evaluate on maze pathfinding, image classification, and Sudoku, where agents with individually insufficient local views coordinate to produce correct global outputs. We show that this locality also yields improved robustness to distribution shifts (padding, missing patches, and noise) when evaluated against a standard CNN on MNIST, while exposing interpretable primal/consensus/dual variables that make the coordination dynamics directly inspectable.

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

### 16. From Directions to Regions: Decomposing Activations in Language Models via Local Geometry

Flags: taxonomy_boundary_cluster, taxonomy-review

- Subarea: Geometric representation learning and manifolds
- Votes: 29
- ICML URL: https://icml.cc/virtual/2026/poster/63757
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.02464
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation
- Method families: Compression / efficiency; Graphs / geometry
- Evaluation settings: robotics/embodied; language/llm
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Activation decomposition methods in language models are tightly coupled to geometric assumptions on how concepts are realized in activation space. Existing approaches search for individual global directions, implicitly assuming linear separability, which overlooks concepts with nonlinear or multi-dimensional structure. In this work, we leverage Mixture of Factor Analyzers (MFA) as a scalable, unsupervised alternative that models the activation space as a collection of Gaussian regions with their *local* covariance structure. MFA decomposes activations into two compositional geometric objects: the region's centroid in activation space, and the local variation from the centroid. We train large-scale MFAs for Llama-3.1-8B and Gemma-2-2B, and show they capture complex, nonlinear structures in activation space. Moreover, evaluations on localization and steering benchmarks show that MFA outperforms unsupervised baselines, is competitive with supervised localization methods, and often achieves stronger steering performance than sparse autoencoders. Together, our findings position local geometry, expressed through subspaces, as a promising unit of analysis for scalable concept discovery and model control, accounting for complex structures that isolated directions fail to capture.

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
