# Data-Centric, Causal, and Federated ML

Manual validation packet for representative and boundary papers.

## Area Context

Headline: Data quality, causality, and distributed learning are converging around what supervision is trustworthy.

Fault lines:
- More data versus better selected, relabeled, distilled, or causally grounded data.
- Predictive correlations versus causal mechanisms and intervention validity.
- Centralized training assumptions versus privacy, federation, heterogeneity, and client incentives.

What to read for:
- Does the method improve data selection or merely add a new scoring heuristic?
- Are causal assumptions identifiable from the available data?
- Does the federated setup model realistic client drift, incentives, and system constraints?

## Queue Summary

- Papers: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, program_signal_low_public_attention=4, taxonomy_boundary_cluster=2
- Papers from taxonomy-review clusters: 12
- Papers with GitHub URLs: 8

## Papers

### 1. Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning

Flags: fault_line_representative, oral, taxonomy-review

- Subarea: Continual learning, forgetting, and task adaptation
- Votes: 98
- ICML URL: https://icml.cc/virtual/2026/poster/63561
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.03818
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Application / domain study
- Contribution types: Application / domain study
- Method families: RL / policy optimization
- Evaluation settings: vision/video; robotics/embodied; language/llm
- Result claim cues: scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Continual learning is a long-standing challenge in robot policy learning, where a policy must acquire new skills over time without catastrophically forgetting previously learned ones. While prior work has extensively studied continual learning in relatively small behavior cloning (BC) policy models trained from scratch, its behavior in modern large-scale pretrained Vision-Language-Action (VLA) models remains underexplored. In this work, we find that pretrained VLAs are remarkably resistant to forgetting compared with smaller policy models trained from scratch. Simple Experience Replay (ER) works surprisingly well on VLAs, sometimes achieving zero forgetting even with a small replay data size. Our analysis reveals that pretraining plays a critical role in downstream continual learning performance: large pretrained models mitigate forgetting with a small replay buffer size while maintaining strong forward learning capabilities. Furthermore, we find that VLAs can retain relevant knowledge from prior tasks despite performance degradation during learning new tasks. This knowledge retention enables rapid recovery of seemingly forgotten skills through finetuning. Together, these insights imply that large-scale pretraining fundamentally changes the dynamics of continual learning, enabling models to continually acquire new skills over time with simple replay.

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

### 2. Midtraining Bridges Pretraining and Posttraining Distributions

Flags: fault_line_representative, oral, taxonomy-review, github

- Subarea: Continual learning, forgetting, and task adaptation
- Votes: 47
- ICML URL: https://icml.cc/virtual/2026/poster/66254
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.14865
- GitHub URL: https://github.com/nightingal3/midtraining
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: Agents / tool use
- Evaluation settings: math/code/verifiable; language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Midtraining, the practice of mixing specialized data with more general pretraining data in an intermediate training phase, has become widespread in language model development, yet there is little understanding of what makes it effective. We propose that midtraining functions as distributional bridging by providing better initialization for posttraining. We conduct controlled pretraining experiments, and find that midtraining benefits are largest for domains distant from general pretraining data, such as code and math, and scale with the proximity advantage the midtraining data provides toward the target distribution. In these domains, midtraining consistently outperforms continued pretraining on specialized data alone both in-domain and in terms of mitigating forgetting. We further conduct an investigation on the starting time and mixture weight of midtraining data, using code as a case study, and find that time of introduction and mixture weight interact strongly such that early introduction of specialized data is amenable to high mixture weights, while late introduction requires lower ones. This suggests that late introduction of specialized data outside a plasticity window cannot be compensated for by increasing data mixtures later in training. Beyond midtraining itself, this suggests that distributional transitions between any training phases may benefit from similar bridging strategies.

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

### 3. Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models

Flags: fault_line_representative, oral, taxonomy-review, github

- Subarea: Continual learning, forgetting, and task adaptation
- Votes: 5
- ICML URL: https://icml.cc/virtual/2026/poster/66000
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.08859
- GitHub URL: https://github.com/SprocketLab/hybrid-expressivity
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; System / infrastructure
- Method families: Transformer / attention
- Evaluation settings: theory/synthetic
- Result claim cues: negative / limitation; scaling / efficiency; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: memory

Abstract:

Hybrid sequence models—combining Transformer and state-space model layers—seek to gain the expressive versatility of attention as well as the computational efficiency of state-space model layers. Despite burgeoning interest in hybrid models, we lack a basic understanding of the settings where—and underlying mechanisms through which—they offer benefits over their constituent models. In this paper, we study this question, focusing on a broad family of core synthetic tasks. For this family of tasks, we prove the existence of fundamental limitations for non-hybrid models. Specifically, any Transformer or state-space model that solves the underlying task requires either a large number of parameters or a large working memory. On the other hand, for two prototypical tasks within this family—namely selective copying and associative recall—we construct hybrid models of small size and working memory that provably solve these tasks, thus achieving the best of both worlds. Our experimental evaluation empirically validates our theoretical findings. Importantly, going beyond the settings in our theoretical analysis, we empirically show that learned—rather than constructed—hybrids outperform non-hybrid models with up to $6 \times$ as many parameters. We additionally demonstrate that hybrid models exhibit stronger length generalization and out-of-distribution robustness than non-hybrids.

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

### 4. DISCO: Mitigating Bias in Deep Learning with Conditional Distance Correlation

Flags: fault_line_representative, oral

- Subarea: Causal inference and causal discovery
- Votes: 4
- ICML URL: https://icml.cc/virtual/2026/poster/63808
- AlphaXiv URL: https://www.alphaxiv.org/abs/2506.11653
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Method / algorithm
- Method families: Agents / tool use; Causal / data-centric
- Evaluation settings: security/safety; theory/synthetic
- Result claim cues: scaling / efficiency; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Dataset bias often leads deep learning models to exploit spurious correlations instead of task-relevant signals. We introduce the Standard Anti-Causal Model (SAM), a unifying causal framework that characterizes bias mechanisms and yields a conditional independence criterion for causal stability. Building on this theory, we propose DISCO$_m$ and sDISCO, efficient and scalable estimators of conditional distance correlation that enable independence regularization in black-box models. Across six diverse datasets, our methods consistently outperform or are competitive in existing bias mitigation approaches, while requiring fewer hyperparameters and scaling seamlessly to multi-bias scenarios. This work bridges causal theory and practical deep learning, providing both a principled foundation and effective tools for robust prediction.

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

### 5. Exact Functional ANOVA Decomposition for Categorical Inputs

Flags: fault_line_representative, oral, evidence-low

- Subarea: Causal inference and causal discovery
- Votes: 2
- ICML URL: https://icml.cc/virtual/2026/poster/61430
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.02673
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: Diffusion / flow
- Evaluation settings: none
- Result claim cues: negative / limitation; scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Functional ANOVA offers a principled framework for interpretability by decomposing a model’s prediction into main effects and higher-order interactions. For independent features, this decomposition is well-defined, strongly linked with SHAP values, and serves as a cornerstone of additive explainability. However, the lack of an explicit closed-form expression for general dependent distributions has forced practitioners to rely on costly sampling-based approximations. We completely resolve this limitation for categorical inputs. By bridging functional analysis with the extension of discrete Fourier analysis, we derive a closed-form decomposition without any assumption. Our formulation is computationally very efficient. It seamlessly recovers the classical independent case and extends to arbitrary dependence structures, including distributions with non-rectangular support. Furthermore, leveraging the intrinsic link between SHAP and ANOVA under independence, our framework yields a natural generalization of SHAP values for the general categorical setting.

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

### 6. A Recursive Decomposition Framework for Causal Structure Learning in the Presence of Latent Variables

Flags: fault_line_representative, oral, github

- Subarea: Causal inference and causal discovery
- Votes: 1
- ICML URL: https://icml.cc/virtual/2026/poster/62126
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.10651
- GitHub URL: https://github.com/zhengli0060/DiCoLa-ICML2026
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Method / algorithm
- Method families: Causal / data-centric
- Evaluation settings: theory/synthetic
- Result claim cues: negative / limitation; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Constraint-based causal discovery is widely used for learning causal structures, but heavy reliance on conditional independence (CI) testing makes it computationally expensive in high-dimensional settings. To mitigate this limitation, many divide-and-conquer frameworks have been proposed, but most assume causal sufficiency, i.e., no latent variables. In this paper, we show that divide-and-conquer strategies can be theoretically generalized beyond causal sufficiency to settings with latent variables. Specifically, we propose a recursive decomposition framework, termed DiCoLa, that enables divide-and-conquer causal discovery in the presence of latent variables. It recursively decomposes the global learning task into smaller subproblems and integrates their solutions through a principled reconstruction step to recover the global structure. We theoretically establish the soundness and completeness of the proposed framework. Extensive experiments on synthetic data demonstrate that our approach significantly improves computational efficiency across a range of causal discovery algorithms, while experiments on a real-world dataset further illustrate its practical effectiveness.

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

### 7. Self-Distillation Enables Continual Learning

Flags: public_attention_not_program_signal, taxonomy-review, github

- Subarea: Continual learning, forgetting, and task adaptation
- Votes: 590
- ICML URL: https://icml.cc/virtual/2026/poster/61434
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.19897
- GitHub URL: https://github.com/idanshen/Self-Distillation
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: RL / policy optimization; LLM post-training
- Evaluation settings: none
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: accuracy; reward

Abstract:

Continual learning, enabling models to acquire new skills and knowledge without degrading existing capabilities, remains a fundamental challenge for foundation models. While on-policy reinforcement learning can reduce forgetting, it requires explicit reward functions that are often unavailable. Learning from expert demonstrations, the primary alternative, is dominated by supervised fine-tuning (SFT), which is inherently off-policy. We introduce Self-Distillation Fine-Tuning (SDFT), a simple method that enables on-policy learning directly from demonstrations. SDFT leverages in-context learning by using a demonstration-conditioned model as its own teacher, generating on-policy training signals that preserve prior capabilities while acquiring new skills. Across skill learning and knowledge acquisition tasks, SDFT consistently outperforms SFT, achieving higher new-task accuracy while substantially reducing catastrophic forgetting. In sequential learning experiments, SDFT enables a single model to accumulate multiple skills over time without performance regression, establishing on-policy distillation as a practical path to continual learning from demonstrations.

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

### 8. Understanding LoRA as Knowledge Memory: An Empirical Analysis

Flags: public_attention_not_program_signal, taxonomy-review

- Subarea: Continual learning, forgetting, and task adaptation
- Votes: 262
- ICML URL: https://icml.cc/virtual/2026/poster/66786
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.01097
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; System / infrastructure; Method / algorithm
- Method families: Reasoning / test-time compute; Transformer / attention; Compression / efficiency
- Evaluation settings: language/llm
- Result claim cues: scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: memory

Abstract:

Continuous knowledge updating for pre-trained large language models (LLMs) is increasingly necessary yet remains challenging. Although inference-time methods like In-Context Learning (ICL) and Retrieval-Augmented Generation (RAG) are popular, they face constraints in context budgets, costs, and retrieval fragmentation. Departing from these context-dependent paradigms, this work investigates a parametric approach using Low-Rank Adaptation (LoRA) as a modular knowledge memory. Although few recent works examine this concept, the fundamental mechanics governing its capacity and composability remain largely unexplored. We bridge this gap through the first systematic empirical study mapping the design space of LoRA-based memory, ranging from characterizing storage capacity and optimizing internalization to scaling multi-module systems and evaluating long-context reasoning. Rather than proposing a single architecture, we provide practical guidance on the operational boundaries of LoRA memory. Overall, our findings position LoRA as the complementary axis of memory alongside RAG and ICL, offering distinct advantages.

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

### 9. ATLAS: Learning to Optimally Memorize the Context at Test Time

Flags: public_attention_not_program_signal, taxonomy-review, github

- Subarea: Continual learning, forgetting, and task adaptation
- Votes: 168
- ICML URL: https://icml.cc/virtual/2026/poster/65037
- AlphaXiv URL: https://www.alphaxiv.org/abs/2505.23735
- GitHub URL: https://github.com/bhoener/atlas
- Artifact confidence: github_url_no_stars
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; System / infrastructure; Method / algorithm
- Method families: Reasoning / test-time compute; Transformer / attention
- Evaluation settings: language/llm
- Result claim cues: negative / limitation; scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: memory

Abstract:

Transformers have been established as the most popular backbones in sequence modeling, mainly due to their effectiveness in in-context retrieval tasks and the ability to learn at scale. Their quadratic memory and time complexity, however, bound their applicability in longer sequences and so has motivated researchers to explore effective alternative architectures such as modern recurrent neural networks (a.k.a long-term recurrent memory module). Despite their recent success in diverse downstream tasks, they struggle in tasks that requires long context understanding and extrapolation to longer sequences. We observe that these shortcomings come from three disjoint aspects in their design: (1) limited memory capacity that is bounded by the architecture of memory and feature mapping of the input; (2) online nature of update, i.e., optimizing the memory only with respect to the last input; and (3) less expressive management of their fixed-size memory. To enhance all these three aspects, we present Atlas, a long-term memory module with high capacity that learns to memorize the context by optimizing the memory based on the current and past tokens, overcoming the online nature of long-term memory models. Our experimental results on language modeling, common-sense reasoning, recall-intensive, and long-context understanding tasks support the effectiveness of Atlas compared to other modern recurrent neural networks.

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

### 10. Retaining by Doing: The Role of On-Policy Data in Mitigating Forgetting

Flags: public_attention_not_program_signal, taxonomy-review, github

- Subarea: Continual learning, forgetting, and task adaptation
- Votes: 96
- ICML URL: https://icml.cc/virtual/2026/poster/64375
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.18874
- GitHub URL: https://github.com/princeton-pli/retaining-by-doing
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: RL / policy optimization; LLM post-training; Reasoning / test-time compute
- Evaluation settings: language/llm
- Result claim cues: scaling / efficiency; robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Adapting language models (LMs) to new tasks via post-training carries the risk of degrading existing capabilities -- a phenomenon classically known as catastrophic forgetting. In this paper, toward identifying guidelines for mitigating this phenomenon, we systematically compare the forgetting patterns of two widely adopted post-training methods: supervised fine-tuning (SFT) and reinforcement learning (RL). Our experiments reveal a consistent trend across LM families (Llama, Qwen) and tasks (instruction following, general knowledge, and arithmetic reasoning): RL leads to less forgetting than SFT while achieving comparable or higher target task performance. To investigate the cause for this difference, we consider a simplified setting in which the LM is modeled as a mixture of two distributions, one corresponding to prior knowledge and the other to the target task. We identify that the mode-seeking nature of RL, which stems from its use of on-policy data, enables keeping prior knowledge intact when learning the target task. We then verify this insight by demonstrating that the use on-policy data underlies the robustness of RL to forgetting in practical settings, as opposed to other algorithmic choices such as the KL regularization or advantage estimation. Lastly, as a practical implication, our results highlight the potential of mitigating forgetting using approximately on-policy data, which can be substantially more efficient to obtain than fully on-policy data.

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

### 11. On the Identifiability of Poisson Branching Structural Causal Model Under Latent Confounding

Flags: program_signal_low_public_attention, oral

- Subarea: Causal inference and causal discovery
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/66099
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Theory / proof; Method / algorithm
- Method families: Causal / data-centric
- Evaluation settings: security/safety; theory/synthetic
- Result claim cues: negative / limitation
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Causal discovery from observational count data poses unique challenges, particularly when the data exhibit inherent branching structures, e.g., an upstream event (e.g., an ad impression) triggers a downstream event (e.g., a purchase) with a certain probability. Such branching dynamics are naturally captured by thinning operators (for the branching structure) and an independent Poisson distribution (for exogenous noise), constituting the Poisson Branching Structural Causal Model (PB-SCM). However, existing approaches based on PB-SCM rely on the restrictive assumption of causal sufficiency, failing to account for ubiquitous latent confounders that can bias estimation. In this work, we propose the Latent Confounding Poisson Branching Structural Causal Model (LC-PB-SCM) to bridge this gap. We leverage Probability Generating Functions (PGFs) to characterize the complex dependencies introduced by latent confounding. Then, we establish a Trie representation theorem that maps the branching causal mechanisms to the algebraic properties of PGF monomials. Based on local PGFs, we establish a complete identifiability condition for local 3-variables that covers all causal patterns distinguishable up to monomial equivalence. Finally, we propose a practical algorithm to learn causal structures under latent confounding and demonstrate its effectiveness through experiments on both synthetic and real-world datasets.

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

### 12. Detecting the Semantic Fixed Point: A Geometric Framework for Efficient Inference

Flags: program_signal_low_public_attention, oral, taxonomy-review

- Subarea: Continual learning, forgetting, and task adaptation
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/65483
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: Reasoning / test-time compute; Transformer / attention; Graphs / geometry
- Evaluation settings: none
- Result claim cues: scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: accuracy; flops

Abstract:

Each layer of a Transformer refines the hidden state toward a prediction, an iterative process resembling fixed-point iteration. Yet when should this iteration terminate? Existing early exit methods rely on output confidence as a proxy for internal convergence. We take a more direct approach by examining the geometry of the hidden state trajectory. We find that layer-wise updates exhibit a two-phase structure: large, volatile updates in early layers, followed by small, aligned updates as the model propagates an already-formed representation. The transition is remarkably sharp. This yields a simple criterion: exit when step size vanishes and direction stabilizes. We track the normalized update norm and cosine similarity between consecutive updates, exiting when both indicate convergence. The overhead is $O(d)$ per layer, independent of vocabulary size, requiring no learned components or architectural modifications. On LLaMA-2-7B and LLaMA-2-13B across question answering and commonsense reasoning tasks, this geometric criterion reduces FLOPs by 30--35\% while retaining over 98\% of full-depth accuracy.

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

### 13. On the Difficulty of Learning a Meta-network for Training Data Selection

Flags: program_signal_low_public_attention, oral, taxonomy-review, github

- Subarea: Labels, datasets, and supervised data quality
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/63990
- AlphaXiv URL: https://www.alphaxiv.org/abs/2606.00571
- GitHub URL: https://github.com/ZILIN003/MTS
- Artifact confidence: github_url_no_stars
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; Method / algorithm
- Method families: Causal / data-centric
- Evaluation settings: vision/video; theory/synthetic
- Result claim cues: negative / limitation; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Synthetic data are increasingly used to train image classifiers, yet distributional mismatch with real data limits their effectiveness when used indiscriminately. A common strategy is to learn data weights via bi-level optimization, which we refer to as Meta-learning for Training-data Selection (MTS). Interestingly, in practice, MTS often performs below expectation. We identify two obstacles in properly training MTS: a poor gradient signal-to-noise ratio (GSNR), which causes optimization difficulties, and lack of informative features that correlates with data quality. We present a thorough mathematical analysis of MTS, which reveals the dynamics of normalized data weights and the relation between disparate data quality and poor GSNR. The analysis suggests a a simple yet effective solution: increasing the batch size. Further, we propose a set of informative features that capture the positions of training data in their distributions and training dynamics. Experiments across four benchmarks show consistent improvements, achieving average gains of 5.49\% over training without selection and 2.89\% over the strongest baseline.

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

### 14. Incentivizing Truthfulness and Collaborative Fairness in Bayesian Learning

Flags: program_signal_low_public_attention, oral, taxonomy-review

- Subarea: Federated learning and distributed clients
- Votes: 1
- ICML URL: https://icml.cc/virtual/2026/poster/63259
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.11889
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Theory / proof; Method / algorithm
- Method families: RL / policy optimization; Reasoning / test-time compute; Bayesian / probabilistic
- Evaluation settings: theory/synthetic
- Result claim cues: negative / limitation
- Benchmarks: none
- Datasets: none
- Metrics: reward

Abstract:

Collaborative machine learning involves training high-quality models using datasets from a number of sources. To incentivize sources to share data, existing data valuation methods fairly reward each source based on its data submitted as is. However, as these methods do not verify nor incentivize data truthfulness, the sources can manipulate their data (e.g., by submitting duplicated or noisy data) to artificially increase their valuations and rewards or prevent others from benefiting. This paper presents the first mechanism that provably ensures (**F**) collaborative fairness and incentivizes (**T**) truthfulness at equilibrium for Bayesian models. Our mechanism combines semivalues (e.g., Shapley value), which ensure fairness, and a truthful data valuation function (DVF) based on a validation set that is unknown to the sources. As semivalues are influenced by others' data, we introduce an additional condition to prove that a source can maximize its expected data values in coalitions and semivalues by submitting a dataset that captures its true knowledge. Additionally, we discuss the implications and suitable relaxations of (**F**) and (**T**) when the mediator has a limited budget for rewards or lacks a validation set. Our theoretical findings are validated on synthetic and real-world datasets.

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

### 15. Artificial Hippocampus Networks for Efficient Long-Context Modeling

Flags: taxonomy_boundary_cluster, taxonomy-review, github

- Subarea: Continual learning, forgetting, and task adaptation
- Votes: 80
- ICML URL: https://icml.cc/virtual/2026/poster/65210
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.07318
- GitHub URL: https://github.com/ByteDance-Seed/AHN
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Theory / proof; System / infrastructure; Application / domain study; Method / algorithm
- Method families: Transformer / attention
- Evaluation settings: language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: InfiniteBench
- Datasets: none
- Metrics: memory; flops

Abstract:

Long-sequence modeling faces a fundamental trade-off between the efficiency of compressive fixed-size memory in RNN-like models and the fidelity of lossless growing memory in attention-based Transformers. Inspired by the Multi-Store Model in cognitive science, we introduce a memory framework of artificial neural networks. Our method maintains a sliding window of the Transformer's KV cache as lossless short-term memory, while a learnable module termed Artificial Hippocampus Network (AHN) recurrently compresses out-of-window information into a fixed-size compact long-term memory. To validate this framework, we instantiate AHNs using modern RNN-like architectures, including Mamba2, DeltaNet, and GatedDeltaNet to augment open-weight base LLMs. We also propose an efficient self-distillation method where the base model' all parameters are frozen and only the parameters from AHNs are optimized. For inference, our method sets a default large sliding window size of 32k for attention, and AHNs activate only when the sequence length exceeds the 32k window, addressing the quadratic-complexity issue of attention that emerges at that scale. Extensive experiments on long-context benchmarks LV-Eval and InfiniteBench demonstrate that AHN-augmented models consistently outperform sliding window baselines and achieve performance comparable or even superior to full-attention models, while substantially reducing computational and memory requirements. For instance, augmenting the Qwen2.5-3B-Instruct with AHNs reduces inference FLOPs by 40.5% and memory cache by 74.0%, while improving its average score on LV-Eval (128k sequence length) from 4.41 to 5.88.

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

### 16. Extracting alignment data in open models

Flags: taxonomy_boundary_cluster, taxonomy-review

- Subarea: Labels, datasets, and supervised data quality
- Votes: 74
- ICML URL: https://icml.cc/virtual/2026/poster/66452
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.18554
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Dataset / data resource; Method / algorithm
- Method families: RL / policy optimization; LLM post-training; Reasoning / test-time compute; Transformer / attention
- Evaluation settings: security/safety
- Result claim cues: robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

In this work, we show that it is possible to extract significant amounts of alignment training data from a post-trained model -- useful to steer the model to improve certain capabilities such as long-context reasoning, safety, instruction following, and maths. While the majority of related work on memorisation has focused on measuring success of training data extraction through string matching, we argue that embedding models are better suited for our specific goals. Distances measured through a high quality embedding model can identify semantic similarities between strings that a different metric such as edit distance will struggle to capture. In fact, in our investigation, approximate string matching would have severely undercounted (by a conservative estimate of $10\times$) the amount of data that can be extracted due to trivial artifacts that deflate the metric. Interestingly, we find that models readily regurgitate training data that was used in post-training phases such as SFT or RL. We show that this data can be then used to train a base model, recovering a meaningful amount of the original performance. We believe our work exposes a possibly overlooked risk towards extracting alignment data. Finally, our work opens up an interesting discussion on the downstream effects of distillation practices: since models seem to be regurgitating aspects of their training set, distillation can therefore be thought of as indirectly training on the model's original dataset.

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
