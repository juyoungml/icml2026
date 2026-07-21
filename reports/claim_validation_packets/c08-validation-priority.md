# C08: Validation priority

Review question: Which taxonomy boundary clusters most urgently need manual relabeling before publication claims?

## Queue Summary

- Papers: 18
- Selection mix: taxonomy_boundary_cluster_anchor=12, taxonomy_boundary_program_public_fill=6
- Oral/award papers: 7
- Taxonomy-review papers: 18
- GitHub-linked papers: 13

## Papers

### 1. Reinforcement Learning via Self-Distillation

Flags: taxonomy_boundary_cluster_anchor, taxonomy-review, github

- Review focus: Decide whether this cluster should remain in the assigned area/subarea or be relabeled.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Cluster: 2 - reward / reinforcement learning / reinforcement / rewards
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=false; award=none; votes=718; 7d visits=334
- Artifact: https://github.com/lasgroup/SDPO; stars=1008; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=RL / policy optimization; LLM post-training; Reasoning / test-time compute; Agents / tool use; Diffusion / flow; eval=math/code/verifiable; language/llm
- Benchmark/data/metric cues: LiveCodeBench / none / accuracy; reward
- ICML URL: https://icml.cc/virtual/2026/poster/64121
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.20802

Abstract:

Large language models are increasingly post-trained with reinforcement learning in verifiable domains such as code and math. Yet, current methods for reinforcement learning with verifiable rewards (RLVR) learn only from a scalar outcome reward per attempt, creating a severe credit-assignment bottleneck. Many verifiable environments actually provide rich textual feedback, such as runtime errors or judge evaluations, that explain *why* an attempt failed. We formalize this setting as reinforcement learning with rich feedback and introduce **Self-Distillation Policy Optimization** (**SDPO**), which converts tokenized feedback into a dense learning signal without any external teacher or explicit reward model. SDPO treats the current model conditioned on feedback as a self-teacher and distills its feedback-informed next-token predictions back into the policy. In this way, SDPO leverages the model's ability to retrospectively identify its own mistakes in-context. Across scientific reasoning, tool use, and competitive programming on LiveCodeBench v6, SDPO improves sample efficiency and final accuracy over strong RLVR baselines. Notably, SDPO also outperforms baselines in standard RLVR environments that only return scalar feedback by using successful rollouts as implicit feedback for failed attempts. Finally, applying SDPO to individual questions at test time accelerates discovery on difficult binary-reward tasks, achieving the same discovery probability as best-of-k sampling or multi-turn conversations with 3x fewer attempts.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 2. mHC: Manifold-Constrained Hyper-Connections

Flags: taxonomy_boundary_cluster_anchor, taxonomy-review, github

- Review focus: Decide whether this cluster should remain in the assigned area/subarea or be relabeled.
- Area/subarea: Systems and Efficient Foundation Models / Large-scale training, optimizers, and model architecture
- Cluster: 26 - networks / training / deep / gradient
- Cluster review: needs_review; manual confidence not high; split across lexical clusters
- Program/public: oral=false; award=none; votes=696; 7d visits=173
- Artifact: https://github.com/tokenbender/mHC-manifold-constrained-hyper-connections; stars=367; manual-check=none
- Evidence tags: contribution=System / infrastructure; methods=Graphs / geometry; eval=language/llm
- Benchmark/data/metric cues: none / none / memory
- ICML URL: https://icml.cc/virtual/2026/poster/61870
- AlphaXiv URL: https://www.alphaxiv.org/abs/2512.24880

Abstract:

Recently, studies exemplified by Hyper-Connections (HC) have extended the ubiquitous residual connection paradigm established over the past decade by expanding the residual stream width and diversifying connectivity patterns. While yielding substantial performance gains, this diversification fundamentally compromises the identity mapping property intrinsic to the residual connection, which causes severe training instability and restricted scalability, and additionally incurs notable memory access overhead. To address these challenges, we propose Manifold-Constrained Hyper-Connections (mHC), a general framework that projects the residual connection space of HC onto a specific manifold to restore the identity mapping property, while incorporating rigorous infrastructure optimization to ensure efficiency. Empirical experiments demonstrate that mHC is effective for training at scale, offering tangible performance improvements and superior scalability. We anticipate that mHC, as a flexible and practical extension of HC, will contribute to a deeper understanding of topological architecture design and suggest promising directions for the evolution of foundational models.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 3. Self-Distillation Enables Continual Learning

Flags: taxonomy_boundary_cluster_anchor, taxonomy-review, github

- Review focus: Decide whether this cluster should remain in the assigned area/subarea or be relabeled.
- Area/subarea: Data-Centric, Causal, and Federated ML / Continual learning, forgetting, and task adaptation
- Cluster: 10 - continual / forgetting / continual learning / task
- Cluster review: needs_review; manual confidence not high; split across lexical clusters
- Program/public: oral=false; award=none; votes=590; 7d visits=311
- Artifact: https://github.com/idanshen/Self-Distillation; stars=653; manual-check=none
- Evidence tags: contribution=Method / algorithm; methods=RL / policy optimization; LLM post-training; eval=none
- Benchmark/data/metric cues: none / none / accuracy; reward
- ICML URL: https://icml.cc/virtual/2026/poster/61434
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.19897

Abstract:

Continual learning, enabling models to acquire new skills and knowledge without degrading existing capabilities, remains a fundamental challenge for foundation models. While on-policy reinforcement learning can reduce forgetting, it requires explicit reward functions that are often unavailable. Learning from expert demonstrations, the primary alternative, is dominated by supervised fine-tuning (SFT), which is inherently off-policy. We introduce Self-Distillation Fine-Tuning (SDFT), a simple method that enables on-policy learning directly from demonstrations. SDFT leverages in-context learning by using a demonstration-conditioned model as its own teacher, generating on-policy training signals that preserve prior capabilities while acquiring new skills. Across skill learning and knowledge acquisition tasks, SDFT consistently outperforms SFT, achieving higher new-task accuracy while substantially reducing catastrophic forgetting. In sequential learning experiments, SDFT enables a single model to accumulate multiple skills over time without performance regression, establishing on-policy distillation as a practical path to continual learning from demonstrations.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 4. Learning to Discover at Test Time

Flags: taxonomy_boundary_cluster_anchor, taxonomy-review, github

- Review focus: Decide whether this cluster should remain in the assigned area/subarea or be relabeled.
- Area/subarea: Agents, Code, and Tool Use / Multi-agent search, planning, and coordination
- Cluster: 30 - agent / multi / search / agents
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=false; award=none; votes=529; 7d visits=174
- Artifact: https://github.com/sayantann11/all-classification-templetes-for-ML; stars=297; manual-check=none
- Evidence tags: contribution=System / infrastructure; methods=RL / policy optimization; Reasoning / test-time compute; Agents / tool use; Diffusion / flow; eval=math/code/verifiable; language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/65888
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.16175

Abstract:

How can we use AI to discover a new state of the art for a scientific problem? Prior work in test-time scaling, such as AlphaEvolve, performs search by prompting a frozen LLM. We perform reinforcement learning at test time, so the LLM can continue to train, but now with experience specific to the test problem. This form of continual learning is quite special, because its goal is to produce one great solution rather than many good ones on average, and to solve this very problem rather than generalize to other problems. Therefore, our learning objective and search subroutine are designed to prioritize the most promising solutions. We call this method Test-Time Training to Discover (TTT-Discover). Following prior work, we focus on problems with continuous rewards. We report results for every problem we attempted, across mathematics, GPU kernel engineering, algorithm design, and biology. TTT-Discover sets the new state of the art in almost all of them: (i) Erdős' minimum overlap problem and an autocorrelation inequality; (ii) a GPUMode kernel competition (up to 2× faster than prior art); (iii) past AtCoder algorithm competitions; and (iv) denoising problem in single-cell analysis. Our solutions are reviewed by experts or the organizers. All our results are achieved with an open model, OpenAI gpt-oss-120b, and can be reproduced with our publicly available code, in contrast to previous best results that required closed frontier models. Our test-time training runs are performed using Tinker, an API by Thinking Machines, with a cost of only a few hundred dollars per problem.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 5. Latent Collaboration in Multi-Agent Systems

Flags: taxonomy_boundary_cluster_anchor, taxonomy-review, github

- Review focus: Decide whether this cluster should remain in the assigned area/subarea or be relabeled.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / Reasoning models and chain-of-thought behavior
- Cluster: 11 - reasoning / language / large language / language models
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=false; award=none; votes=402; 7d visits=149
- Artifact: https://github.com/Gen-Verse/LatentMAS; stars=1048; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=Reasoning / test-time compute; Agents / tool use; eval=math/code/verifiable; language/llm; theory/synthetic
- Benchmark/data/metric cues: none / none / accuracy; memory
- ICML URL: https://icml.cc/virtual/2026/poster/61180
- AlphaXiv URL: https://www.alphaxiv.org/abs/2511.20639

Abstract:

Multi-agent systems (MAS) extend large language models (LLMs) from independent single-model reasoning to coordinative system-level intelligence. While existing LLM agents depend on text-based mediation for reasoning and communication, we take a step forward by enabling models to collaborate directly within the continuous latent space. We introduce LatentMAS, an end-to-end training-free framework that enables pure latent collaboration among LLM agents. In LatentMAS, each agent first performs auto-regressive latent thoughts generation through last-layer hidden embeddings instead of text. Then, a shared latent working memory preserves and transfers each agent's internal representations and latent thoughts, ensuring lossless information exchange without re-encoding. We provide detailed theoretical analyses showing that LatentMAS achieves higher expressiveness and lossless information preservation with lower overall complexity than standard text-based MAS. In addition, empirical evaluations across 9 comprehensive benchmarks spanning math and science reasoning, commonsense understanding, and code generation show that LatentMAS outperforms advanced single agents and text-based MAS baselines, achieving up to 14.6\% higher accuracy, reducing output token usage by 70.8\%-83.7\%, and providing 4$\times$-4.3$\times$ faster end-to-end inference. These results demonstrate that our new latent collaboration framework enhances system-level reasoning quality while providing consistent efficiency gains.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 6. How much can language models memorize?

Flags: taxonomy_boundary_cluster_anchor, oral, Outstanding Paper Honorable Mention, taxonomy-review, github

- Review focus: Decide whether this cluster should remain in the assigned area/subarea or be relabeled.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / Diffusion language models and decoding
- Cluster: 14 - decoding / diffusion / language / language models
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=true; award=Outstanding Paper Honorable Mention; votes=271; 7d visits=374
- Artifact: https://github.com/SimonCao1207/LLM-Capacity; stars=2; manual-check=none
- Evidence tags: contribution=Dataset / data resource; methods=Transformer / attention; eval=language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/62989
- AlphaXiv URL: https://www.alphaxiv.org/abs/2505.24832

Abstract:

We propose a new method for estimating how much a model knows about a datapoint and use it to measure the capacity of modern language models. Prior studies of language model memorization have struggled to disentangle memorization from generalization. We formally separate memorization into two components: unintended memorization, the information a model contains about a specific dataset, and generalization, the information a model contains about the true data-generation process. When we completely eliminate generalization, we can compute the total memorization, which provides an estimate of model capacity: our measurements estimate that GPT-style models have a capacity of approximately 3.6 bits per parameter. We train language models on datasets of increasing size and observe that models memorize until their capacity fills, at which point unintended memorization decreases as models begin to generalize. We train hundreds of transformer language models ranging from 500K to 1.5B parameters and produce a series of scaling laws relating model capacity and data size to membership inference.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 7. How to Correctly Report LLM-as-a-Judge Evaluations

Flags: taxonomy_boundary_cluster_anchor, taxonomy-review, github

- Review focus: Decide whether this cluster should remain in the assigned area/subarea or be relabeled.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / General LLM training, evaluation, and alignment
- Cluster: 24 - language / language models / llms / large language
- Cluster review: needs_review; manual confidence not high; split across lexical clusters
- Program/public: oral=false; award=none; votes=267; 7d visits=55
- Artifact: https://github.com/UW-Madison-Lee-Lab/LLM-judge-reporting; stars=81; manual-check=none
- Evidence tags: contribution=Dataset / data resource; methods=none; eval=language/llm; security/safety
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/63607
- AlphaXiv URL: https://www.alphaxiv.org/abs/2511.21140

Abstract:

Large language models (LLMs) are widely used as scalable evaluators of model responses in lieu of human annotators. However, imperfect sensitivity and specificity of the LLM judges induce bias in naive evaluation scores. We propose a simple plug-in framework that corrects this bias and enables statistically principled uncertainty quantification. Our framework constructs confidence intervals that account for uncertainty from both the test dataset and a human-labeled calibration dataset. Additionally it uses an adaptive strategy to allocate calibration samples for tighter intervals. Importantly, we characterize parameter regimes defined by the true evaluation score and the LLM judge’s sensitivity and specificity in which our LLM-based evaluation yields more reliable estimates than human-only evaluation. Moreover, we show that our framework remains unbiased under distribution shift between the test and calibration datasets, in contrast to existing approaches.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 8. Dimensional Collapse in Transformer Attention Outputs: A Challenge for Sparse Dictionary Learning

Flags: taxonomy_boundary_cluster_anchor, taxonomy-review

- Review focus: Decide whether this cluster should remain in the assigned area/subarea or be relabeled.
- Area/subarea: Theory, Optimization, and Algorithms / Transformer theory and attention expressivity
- Cluster: 20 - transformers / attention / transformer / softmax
- Cluster review: needs_review; manual confidence not high
- Program/public: oral=false; award=none; votes=160; 7d visits=5
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Dataset / data resource; methods=Agents / tool use; Transformer / attention; Compression / efficiency; Graphs / geometry; eval=math/code/verifiable; language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/64760
- AlphaXiv URL: https://www.alphaxiv.org/abs/2508.16929

Abstract:

Transformer architectures, and their attention mechanisms in particular, form the foundation of modern large language models. While transformer models are widely believed to operate in high-dimensional hidden spaces, we show that attention outputs are confined to a surprisingly low-dimensional subspace, with an effective dimensionality of only about 60\% of the full space---a phenomenon that is consistently observed across diverse model families and datasets, and is strongly influenced by the attention output projection matrix. Critically, we find this low-rank structure as a key factor of the prevalent dead feature problem in sparse dictionary learning, where it creates a mismatch between randomly initialized features and the intrinsic geometry of the activation space. Building on this insight, we propose a subspace-constrained training method for sparse autoencoders (SAEs), initializing feature directions into the active subspace of activations. Our approach reduces dead features from 87\% to below 1\% in Attention Output SAEs with 1M features, and can further extend to other sparse dictionary learning methods. Our findings provide both new insights into the geometry of attention and practical tools for improving sparse dictionary learning in large language models. Code is available at \url{https://anonymous.4open.science/r/Language-Model-SAEs-C015}.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 9. Rethinking the Trust Region in LLM Reinforcement Learning

Flags: taxonomy_boundary_cluster_anchor, taxonomy-review, github

- Review focus: Decide whether this cluster should remain in the assigned area/subarea or be relabeled.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / LLM preference tuning and alignment training
- Cluster: 21 - language / large language / language models / large
- Cluster review: needs_review; manual confidence not high; split across lexical clusters
- Program/public: oral=false; award=none; votes=103; 7d visits=30
- Artifact: https://github.com/sail-sg/Stable-RL; stars=61; manual-check=none
- Evidence tags: contribution=Position / conceptual; methods=RL / policy optimization; LLM post-training; eval=language/llm
- Benchmark/data/metric cues: none / none / memory
- ICML URL: https://icml.cc/virtual/2026/poster/62611
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.04879

Abstract:

Reinforcement learning (RL) has become a cornerstone for fine-tuning Large Language Models (LLMs), with Proximal Policy Optimization (PPO) serving as the de facto standard algorithm. Despite its ubiquity, we argue that the core ratio clipping mechanism in PPO is structurally ill-suited for the large vocabularies inherent to LLMs. PPO constrains policy updates based on the probability ratio of sampled tokens, which serves as a noisy single-sample Monte Carlo estimate of the true policy divergence. This creates a sub-optimal learning dynamic: updates to low-probability tokens are aggressively over-penalized, while potentially catastrophic shifts in high-probability tokens are under-constrained, leading to training inefficiency and instability. To address this, we propose Divergence Proximal Policy Optimization (DPPO), which substitutes heuristic clipping with a more principled constraint based on a direct estimate of policy divergence (e.g., Total Variation or KL). To avoid huge memory footprint, we introduce the efficient Binary and Top-K approximations to capture the essential divergence with negligible overhead. Extensive empirical evaluations demonstrate that DPPO achieves superior stability and efficiency compared to existing methods, offering a more robust foundation for RL-based LLM fine-tuning.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 10. Deep sequence models tend to memorize geometrically; it is unclear why.

Flags: taxonomy_boundary_cluster_anchor, taxonomy-review

- Review focus: Decide whether this cluster should remain in the assigned area/subarea or be relabeled.
- Area/subarea: Graphs, Geometry, and Representation Learning / Geometric representation learning and manifolds
- Cluster: 18 - geometric / representation / geometry / representations
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=false; award=none; votes=76; 7d visits=10
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Position / conceptual; methods=Reasoning / test-time compute; Transformer / attention; Graphs / geometry; eval=security/safety; theory/synthetic
- Benchmark/data/metric cues: none / none / memory
- ICML URL: https://icml.cc/virtual/2026/poster/65556
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.26745

Abstract:

Deep sequence models are said to store atomic facts predominantly in the form of associative memory: a brute-force lookup of co-occurring entities. We identify a dramatically different form of storage of atomic facts that we term as geometric memory. Here, the model has synthesized embeddings encoding novel global relationships between all entities, including ones that do not co-occur in training. Such storage is powerful: for instance, we show how it transforms a hard reasoning task involving an $\ell$-fold composition into an easy-to-learn $1$-step navigation task. From this phenomenon, we extract fundamental aspects of neural embedding geometries that are hard to explain. We argue that the rise of such a geometry, as against a lookup of local associations, cannot be straightforwardly attributed to typical supervisory, architectural, or optimizational pressures. Counterintuitively, a geometry is learned even when it is more complex than the brute-force lookup. Then, by analyzing a connection to Node2Vec, we demonstrate how the geometry stems from a spectral bias that---in contrast to prevailing theories---indeed arises naturally despite the lack of various pressures. This analysis also points out to practitioners a visible headroom to make Transformer memory more strongly geometric. We hope the geometric view of parametric memory encourages revisiting the default intuitions that guide researchers in areas like knowledge acquisition, capacity, discovery, and unlearning.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 11. Extracting alignment data in open models

Flags: taxonomy_boundary_cluster_anchor, taxonomy-review

- Review focus: Decide whether this cluster should remain in the assigned area/subarea or be relabeled.
- Area/subarea: Data-Centric, Causal, and Federated ML / Labels, datasets, and supervised data quality
- Cluster: 17 - label / labels / machine / machine learning
- Cluster review: needs_review; manual confidence not high; split across lexical clusters
- Program/public: oral=false; award=none; votes=74; 7d visits=15
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Position / conceptual; methods=RL / policy optimization; LLM post-training; Reasoning / test-time compute; Transformer / attention; eval=security/safety
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/66452
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.18554

Abstract:

In this work, we show that it is possible to extract significant amounts of alignment training data from a post-trained model -- useful to steer the model to improve certain capabilities such as long-context reasoning, safety, instruction following, and maths. While the majority of related work on memorisation has focused on measuring success of training data extraction through string matching, we argue that embedding models are better suited for our specific goals. Distances measured through a high quality embedding model can identify semantic similarities between strings that a different metric such as edit distance will struggle to capture. In fact, in our investigation, approximate string matching would have severely undercounted (by a conservative estimate of $10\times$) the amount of data that can be extracted due to trivial artifacts that deflate the metric. Interestingly, we find that models readily regurgitate training data that was used in post-training phases such as SFT or RL. We show that this data can be then used to train a base model, recovering a meaningful amount of the original performance. We believe our work exposes a possibly overlooked risk towards extracting alignment data. Finally, our work opens up an interesting discussion on the downstream effects of distillation practices: since models seem to be regurgitating aspects of their training set, distillation can therefore be thought of as indirectly training on the model's original dataset.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 12. Who Said Neural Networks Aren't Linear?

Flags: taxonomy_boundary_cluster_anchor, taxonomy-review, github

- Review focus: Decide whether this cluster should remain in the assigned area/subarea or be relabeled.
- Area/subarea: Graphs, Geometry, and Representation Learning / Equivariant graph and geometric networks
- Cluster: 41 - graph / networks / neural networks / graph neural
- Cluster review: needs_review; small cluster
- Program/public: oral=false; award=none; votes=74; 7d visits=11
- Artifact: https://github.com/assafshocher/Linearizer; stars=43; manual-check=none
- Evidence tags: contribution=Method / algorithm; methods=Diffusion / flow; eval=none
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/65316
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.08570

Abstract:

Neural networks are famously nonlinear. However, linearity is defined relative to a pair of vector spaces, $f:\mathcal{X}\to\mathcal{Y}$. Leveraging the algebraic concept of transport of structure, we propose a method to explicitly identify non-standard vector spaces where a neural network acts as a linear operator. When sandwiching a linear operator $A$ between two invertible neural networks, $f(x)=g_y^{-1}(A g_x(x))$, the corresponding vector spaces $\mathcal{X}$ and $\mathcal{Y}$ are induced by newly defined addition and scaling actions derived from $g_x$ and $g_y$. We term this kind of architecture a Linearizer. This framework makes the entire arsenal of linear algebra, including SVD, pseudo-inverse, orthogonal projection and more, applicable to nonlinear mappings. Furthermore, we show that the composition of two Linearizers that share a neural network is also a Linearizer. We leverage this property and demonstrate that training diffusion models using our architecture makes the hundreds of sampling steps collapse into a single step. We further utilize our framework to enforce idempotency (i.e.\ $f(f(x))=f(x)$) on networks leading to a globally projective generative model and to demonstrate modular style transfer.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 13. The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models

Flags: taxonomy_boundary_program_public_fill, oral, Outstanding Paper Award, taxonomy-review, github

- Review focus: Use high-signal papers to stress-test taxonomy boundaries.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / Reasoning models and chain-of-thought behavior
- Cluster: 11 - reasoning / language / large language / language models
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=true; award=Outstanding Paper Award; votes=92; 7d visits=588
- Artifact: https://github.com/LeapLabTHU/JustGRPO; stars=212; manual-check=none
- Evidence tags: contribution=Method / algorithm; methods=RL / policy optimization; Reasoning / test-time compute; Diffusion / flow; eval=language/llm
- Benchmark/data/metric cues: none / none / accuracy
- ICML URL: https://icml.cc/virtual/2026/poster/61998
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.15165

Abstract:

Diffusion Large Language Models (dLLMs) break the rigid left-to-right constraint of traditional LLMs, enabling token generation in arbitrary orders. Intuitively, this flexibility implies a solution space that strictly supersets the fixed autoregressive trajectory, theoretically unlocking superior reasoning potential. Indeed, for specific constraint satisfaction tasks (e.g., sudoku puzzles), this capability has proven to be highly advantageous. However, in this paper, we reveal that for general reasoning tasks (e.g., mathematics and coding), arbitrary order generation may in fact limit the reasoning potential of dLLMs. We find that dLLMs tend to exploit this order flexibility to bypass high-uncertainty tokens that are crucial for exploration, leading to a premature collapse of solution coverage. This observation motivates a rethink of RL approaches for dLLMs, where considerable complexities, such as handling combinatorial trajectories and intractable likelihoods, are often devoted to preserving this flexibility. We demonstrate that effective reasoning can be better elicited by simply forgoing arbitrary order and applying standard Group Relative Policy Optimization (GRPO) instead. Our approach, **JustGRPO**, is minimalist yet surprisingly effective (e.g., 89.1% accuracy on GSM8K) while fully retaining the parallel decoding ability of dLLMs.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 14. To Grok Grokking: Provable Grokking in Ridge Regression

Flags: taxonomy_boundary_program_public_fill, oral, Outstanding Paper Honorable Mention, taxonomy-review

- Review focus: Use high-signal papers to stress-test taxonomy boundaries.
- Area/subarea: Theory, Optimization, and Algorithms / Statistical learning theory and regression
- Cluster: 7 - theory / regression / bounds / risk
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=true; award=Outstanding Paper Honorable Mention; votes=7; 7d visits=105
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Theory / proof; methods=none; eval=theory/synthetic
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/66206
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.19791

Abstract:

We study *grokking* - the onset of generalization long after overfitting - in a classical ridge regression setting. We prove end-to-end grokking results for learning over-parameterized linear regression models using gradient descent with weight decay. Specifically, we prove that the following stages occur: (i) the model overfits the training data early during training; (ii) poor generalization persists long after overfitting has manifested; and (iii) the generalization error eventually becomes arbitrarily small. Moreover, we show, both theoretically and empirically, that grokking can be amplified or eliminated in a principled manner through proper hyperparameter tuning. To the best of our knowledge, these are the first rigorous quantitative bounds on the generalization delay (which we refer to as the "grokking time") in terms of training hyperparameters. Lastly, going beyond the linear setting, we empirically demonstrate that our quantitative bounds also capture the behavior of grokking on non-linear neural networks. Our results suggest that grokking is not an inherent failure mode of deep learning, but rather a consequence of specific training conditions, and thus does not require fundamental changes to the model architecture or learning algorithm to avoid.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 15. Maximum Likelihood Reinforcement Learning

Flags: taxonomy_boundary_program_public_fill, oral, taxonomy-review, github

- Review focus: Use high-signal papers to stress-test taxonomy boundaries.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Cluster: 2 - reward / reinforcement learning / reinforcement / rewards
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=true; award=none; votes=259; 7d visits=100
- Artifact: https://github.com/tajwarfahim/maxrl; stars=194; manual-check=none
- Evidence tags: contribution=Method / algorithm; methods=RL / policy optimization; Diffusion / flow; eval=language/llm
- Benchmark/data/metric cues: none / none / pass@k; reward
- ICML URL: https://icml.cc/virtual/2026/poster/65332
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.02710

Abstract:

Maximum likelihood is fundamental to supervised learning but it cannot be directly applied in correctness-based problems with non-differentiable sampling. In these settings, reinforcement learning (RL) is typically used to maximize expected reward. We show that for binary correctness tasks, expected-reward RL is a first-order approximation of the maximum likelihood objective, yielding vanishing learning signal on low-success inputs. We introduce **Maximum Likelihood Reinforcement Learning (MaxRL)**, a compute-indexed family of sampling-based objectives derived from a pass@k expansion of the likelihood, which interpolates between standard RL and exact maximum likelihood as compute increases. MaxRL admits a simple unbiased policy-gradient estimator whose optimized objective improves with additional compute. Across multiple domains, MaxRL consistently outperforms standard RL and GRPO, achieving higher $pass@1$ and substantially improved $pass@k$.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 16. Reinforcement Learning with Evolving Rubrics for Deep Research

Flags: taxonomy_boundary_program_public_fill, oral, taxonomy-review, github

- Review focus: Use high-signal papers to stress-test taxonomy boundaries.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Cluster: 2 - reward / reinforcement learning / reinforcement / rewards
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=true; award=none; votes=201; 7d visits=154
- Artifact: https://github.com/rlresearch/dr-tulu; stars=682; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=RL / policy optimization; Reasoning / test-time compute; Agents / tool use; eval=math/code/verifiable; language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/65886
- AlphaXiv URL: https://www.alphaxiv.org/abs/2511.19399

Abstract:

Deep research agents perform multi-step research to produce long-form, well-attributed answers. However, most open deep research agents are trained on easily verifiable short-form QA tasks via reinforcement learning with verifiable rewards, which does not extend to realistic long-form tasks. We address this with **Reinforcement Learning with Evolving Rubrics (RLER)**, where rubrics are constructed and maintained to *co-evolve* with the policy model during training. This allows the rubrics to incorporate newly explored information from search and contrasting model responses, enabling better fact checking and more discriminative on-policy feedback. Using RLER, we develop **Deep Research Tulu (DR Tulu-8B)**, the first fully open model that is directly trained for open-ended, long-form deep research. Across four long-form deep research benchmarks in science, healthcare, and general domains, DR Tulu-8B substantially outperforms existing open deep research agents (by 15.6% over Tongyi DR on average) and matches or exceeds proprietary deep research agents (by 0.7% over OpenAI DR on average), while being significantly smaller and cheaper per query (1000x cheaper than OpenAI DR per query).

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 17. Controlled LLM Training on Spectral Sphere

Flags: taxonomy_boundary_program_public_fill, oral, taxonomy-review, github

- Review focus: Use high-signal papers to stress-test taxonomy boundaries.
- Area/subarea: Systems and Efficient Foundation Models / Large-scale training, optimizers, and model architecture
- Cluster: 26 - networks / training / deep / gradient
- Cluster review: needs_review; manual confidence not high; split across lexical clusters
- Program/public: oral=true; award=none; votes=115; 7d visits=42
- Artifact: https://github.com/Unakar/Spectral-Sphere-Optimizer; stars=130; manual-check=none
- Evidence tags: contribution=Theory / proof; methods=Compression / efficiency; eval=robotics/embodied; language/llm; theory/synthetic
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/66212
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.08393

Abstract:

Scaling large models requires optimization strategies that ensure rapid convergence grounded in stability. Maximal Update Parametrization ($\boldsymbol{\mu}$P) provides a theoretical safeguard for width-invariant $\Theta(1)$ activation control, whereas emerging optimizers like Muon are only "half-aligned" with these constraints: they control updates but allow weights to drift. To address this limitation, we introduce the **Spectral Sphere Optimizer (SSO)**, which enforces strict module-wise spectral constraints on both weights and their updates. By deriving the steepest descent direction on the spectral sphere, SSO realizes a fully $\boldsymbol{\mu}$P-aligned optimization process. To enable large‑scale training, we implement SSO as an efficient parallel algorithm within Megatron. Through extensive pretraining on diverse architectures, including Dense 1.7B, MoE 8B-A1B, and 200-layer DeepNet models, SSO consistently outperforms AdamW and Muon. Furthermore, we observe significant practical stability benefits, including improved MoE router load balancing, suppressed outliers, and strictly bounded activations.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 18. Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning

Flags: taxonomy_boundary_program_public_fill, oral, taxonomy-review

- Review focus: Use high-signal papers to stress-test taxonomy boundaries.
- Area/subarea: Data-Centric, Causal, and Federated ML / Continual learning, forgetting, and task adaptation
- Cluster: 10 - continual / forgetting / continual learning / task
- Cluster review: needs_review; manual confidence not high; split across lexical clusters
- Program/public: oral=true; award=none; votes=98; 7d visits=48
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Application / domain study; methods=RL / policy optimization; eval=vision/video; robotics/embodied; language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/63561
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.03818

Abstract:

Continual learning is a long-standing challenge in robot policy learning, where a policy must acquire new skills over time without catastrophically forgetting previously learned ones. While prior work has extensively studied continual learning in relatively small behavior cloning (BC) policy models trained from scratch, its behavior in modern large-scale pretrained Vision-Language-Action (VLA) models remains underexplored. In this work, we find that pretrained VLAs are remarkably resistant to forgetting compared with smaller policy models trained from scratch. Simple Experience Replay (ER) works surprisingly well on VLAs, sometimes achieving zero forgetting even with a small replay data size. Our analysis reveals that pretraining plays a critical role in downstream continual learning performance: large pretrained models mitigate forgetting with a small replay buffer size while maintaining strong forward learning capabilities. Furthermore, we find that VLAs can retain relevant knowledge from prior tasks despite performance degradation during learning new tasks. This knowledge retention enables rapid recovery of seemingly forgotten skills through finetuning. Together, these insights imply that large-scale pretraining fundamentally changes the dynamics of continual learning, enabling models to continually acquire new skills over time with simple replay.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:
