# C08: Validation priority Evidence Dossier

This is an abstract/title-based pre-review aid. It does not fill or replace the manual validation fields.

## Claim

The biggest remaining quality jump is not more plotting; it is paper-level validation of boundary clusters and high-impact claims.

- Strength label: `process_claim`
- Evidence summary: 21 of 42 semantic clusters are marked needs_review; validation queue contains 192 papers across 12 areas.
- Caveat: The queue organizes review but does not mean evidence fields have been checked.
- Next validation: Fill validation packets and reconcile reviewed fields back into a checked CSV.
- Manual review progress: 0/18 rows reviewed; 18 remaining

## Pre-Review Summary

- Bucket mix: unclear: 17, possible_support: 1
- Selection mix: taxonomy_boundary_cluster_anchor: 12, taxonomy_boundary_program_public_fill: 6
- Area mix: LLM Reasoning, Post-Training, and RLVR: 8, Data-Centric, Causal, and Federated ML: 3, Systems and Efficient Foundation Models: 2, Theory, Optimization, and Algorithms: 2, Graphs, Geometry, and Representation Learning: 2, Agents, Code, and Tool Use: 1

## Adjudication Questions

- Does the abstract directly support the claim, or only share vocabulary with the claim?
- Is the assigned taxonomy area central to the paper, or just one application/context?
- If the paper is high-attention, is the attention driven by a reusable result, a benchmark, a demo, or a social trend?
- If the paper has a GitHub link, is it a real paper artifact and what reproduction claim can be safely made?

## Papers To Read First

- **How much can language models memorize?** (`unclear`; Outstanding Paper Honorable Mention, oral, taxonomy-review, github): No strong abstract/title cue for the claim.
- **The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models** (`unclear`; Outstanding Paper Award, oral, taxonomy-review, github): No strong abstract/title cue for the claim.
- **To Grok Grokking: Provable Grokking in Ridge Regression** (`unclear`; Outstanding Paper Honorable Mention, oral, taxonomy-review): No strong abstract/title cue for the claim.
- **Maximum Likelihood Reinforcement Learning** (`unclear`; oral, taxonomy-review, github): No strong abstract/title cue for the claim.
- **Reinforcement Learning with Evolving Rubrics for Deep Research** (`unclear`; oral, taxonomy-review, github): No strong abstract/title cue for the claim.
- **Controlled LLM Training on Spectral Sphere** (`unclear`; oral, taxonomy-review, github): No strong abstract/title cue for the claim.

## Paper-Level Pre-Review

| Rank | Paper | Bucket | Area | Signals | Why It Matters |
| ---: | --- | --- | --- | --- | --- |
| 1 | Reinforcement Learning via Self-Distillation | unclear | LLM Reasoning, Post-Training, and RLVR | votes=718; github_stars=1008; taxonomy-review | No strong abstract/title cue for the claim. |
| 2 | mHC: Manifold-Constrained Hyper-Connections | unclear | Systems and Efficient Foundation Models | votes=696; github_stars=367; taxonomy-review | No strong abstract/title cue for the claim. |
| 3 | Self-Distillation Enables Continual Learning | unclear | Data-Centric, Causal, and Federated ML | votes=590; github_stars=653; taxonomy-review | No strong abstract/title cue for the claim. |
| 4 | Learning to Discover at Test Time | unclear | Agents, Code, and Tool Use | votes=529; github_stars=297; taxonomy-review | No strong abstract/title cue for the claim. |
| 5 | Latent Collaboration in Multi-Agent Systems | unclear | LLM Reasoning, Post-Training, and RLVR | votes=402; github_stars=1048; taxonomy-review | No strong abstract/title cue for the claim. |
| 6 | How much can language models memorize? | unclear | LLM Reasoning, Post-Training, and RLVR | Outstanding Paper Honorable Mention; oral; votes=271; github_stars=2; taxonomy-review | No strong abstract/title cue for the claim. |
| 7 | How to Correctly Report LLM-as-a-Judge Evaluations | possible_support | LLM Reasoning, Post-Training, and RLVR | votes=267; github_stars=81; taxonomy-review | Keyword overlap with the claim, but human reading is needed. |
| 8 | Dimensional Collapse in Transformer Attention Outputs: A Challenge for Sparse Dictionary Learning | unclear | Theory, Optimization, and Algorithms | votes=160; taxonomy-review | No strong abstract/title cue for the claim. |
| 9 | Rethinking the Trust Region in LLM Reinforcement Learning | unclear | LLM Reasoning, Post-Training, and RLVR | votes=103; github_stars=61; taxonomy-review | No strong abstract/title cue for the claim. |
| 10 | Deep sequence models tend to memorize geometrically; it is unclear why. | unclear | Graphs, Geometry, and Representation Learning | votes=76; taxonomy-review | No strong abstract/title cue for the claim. |
| 11 | Extracting alignment data in open models | unclear | Data-Centric, Causal, and Federated ML | votes=74; taxonomy-review | No strong abstract/title cue for the claim. |
| 12 | Who Said Neural Networks Aren't Linear? | unclear | Graphs, Geometry, and Representation Learning | votes=74; github_stars=43; taxonomy-review | No strong abstract/title cue for the claim. |
| 13 | The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models | unclear | LLM Reasoning, Post-Training, and RLVR | Outstanding Paper Award; oral; votes=92; github_stars=212; taxonomy-review | No strong abstract/title cue for the claim. |
| 14 | To Grok Grokking: Provable Grokking in Ridge Regression | unclear | Theory, Optimization, and Algorithms | Outstanding Paper Honorable Mention; oral; votes=7; taxonomy-review | No strong abstract/title cue for the claim. |
| 15 | Maximum Likelihood Reinforcement Learning | unclear | LLM Reasoning, Post-Training, and RLVR | oral; votes=259; github_stars=194; taxonomy-review | No strong abstract/title cue for the claim. |
| 16 | Reinforcement Learning with Evolving Rubrics for Deep Research | unclear | LLM Reasoning, Post-Training, and RLVR | oral; votes=201; github_stars=682; taxonomy-review | No strong abstract/title cue for the claim. |
| 17 | Controlled LLM Training on Spectral Sphere | unclear | Systems and Efficient Foundation Models | oral; votes=115; github_stars=130; taxonomy-review | No strong abstract/title cue for the claim. |
| 18 | Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning | unclear | Data-Centric, Causal, and Federated ML | oral; votes=98; taxonomy-review | No strong abstract/title cue for the claim. |

## Abstract Excerpts

### 1. Reinforcement Learning via Self-Distillation

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64121) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.20802)

Large language models are increasingly post-trained with reinforcement learning in verifiable domains such as code and math. Yet, current methods for reinforcement learning with verifiable rewards (RLVR) learn only from a scalar outcome reward per attempt, creating a severe credit-assignment bottleneck. Many verifiable environments actually provide rich textual feedback, such as runtime errors or judge evaluations, that explain *why* an attempt failed. We formalize this setting as reinforcement learning with...

### 2. mHC: Manifold-Constrained Hyper-Connections

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61870) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.24880)

Recently, studies exemplified by Hyper-Connections (HC) have extended the ubiquitous residual connection paradigm established over the past decade by expanding the residual stream width and diversifying connectivity patterns. While yielding substantial performance gains, this diversification fundamentally compromises the identity mapping property intrinsic to the residual connection, which causes severe training instability and restricted scalability, and additionally incurs notable memory access overhead. To...

### 3. Self-Distillation Enables Continual Learning

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61434) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.19897)

Continual learning, enabling models to acquire new skills and knowledge without degrading existing capabilities, remains a fundamental challenge for foundation models. While on-policy reinforcement learning can reduce forgetting, it requires explicit reward functions that are often unavailable. Learning from expert demonstrations, the primary alternative, is dominated by supervised fine-tuning (SFT), which is inherently off-policy. We introduce Self-Distillation Fine-Tuning (SDFT), a simple method that enables...

### 4. Learning to Discover at Test Time

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65888) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.16175)

How can we use AI to discover a new state of the art for a scientific problem? Prior work in test-time scaling, such as AlphaEvolve, performs search by prompting a frozen LLM. We perform reinforcement learning at test time, so the LLM can continue to train, but now with experience specific to the test problem. This form of continual learning is quite special, because its goal is to produce one great solution rather than many good ones on average, and to solve this very problem rather than generalize to other...

### 5. Latent Collaboration in Multi-Agent Systems

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61180) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.20639)

Multi-agent systems (MAS) extend large language models (LLMs) from independent single-model reasoning to coordinative system-level intelligence. While existing LLM agents depend on text-based mediation for reasoning and communication, we take a step forward by enabling models to collaborate directly within the continuous latent space. We introduce LatentMAS, an end-to-end training-free framework that enables pure latent collaboration among LLM agents. In LatentMAS, each agent first performs auto-regressive...

### 6. How much can language models memorize?

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62989) / [AlphaXiv](https://www.alphaxiv.org/abs/2505.24832)

We propose a new method for estimating how much a model knows about a datapoint and use it to measure the capacity of modern language models. Prior studies of language model memorization have struggled to disentangle memorization from generalization. We formally separate memorization into two components: unintended memorization, the information a model contains about a specific dataset, and generalization, the information a model contains about the true data-generation process. When we completely eliminate...

### 7. How to Correctly Report LLM-as-a-Judge Evaluations

- Bucket: `possible_support`
- Keyword hits: label
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63607) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.21140)

Large language models (LLMs) are widely used as scalable evaluators of model responses in lieu of human annotators. However, imperfect sensitivity and specificity of the LLM judges induce bias in naive evaluation scores. We propose a simple plug-in framework that corrects this bias and enables statistically principled uncertainty quantification. Our framework constructs confidence intervals that account for uncertainty from both the test dataset and a human-labeled calibration dataset. Additionally it uses an...

### 8. Dimensional Collapse in Transformer Attention Outputs: A Challenge for Sparse Dictionary Learning

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64760) / [AlphaXiv](https://www.alphaxiv.org/abs/2508.16929)

Transformer architectures, and their attention mechanisms in particular, form the foundation of modern large language models. While transformer models are widely believed to operate in high-dimensional hidden spaces, we show that attention outputs are confined to a surprisingly low-dimensional subspace, with an effective dimensionality of only about 60\% of the full space---a phenomenon that is consistently observed across diverse model families and datasets, and is strongly influenced by the attention output...

### 9. Rethinking the Trust Region in LLM Reinforcement Learning

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62611) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.04879)

Reinforcement learning (RL) has become a cornerstone for fine-tuning Large Language Models (LLMs), with Proximal Policy Optimization (PPO) serving as the de facto standard algorithm. Despite its ubiquity, we argue that the core ratio clipping mechanism in PPO is structurally ill-suited for the large vocabularies inherent to LLMs. PPO constrains policy updates based on the probability ratio of sampled tokens, which serves as a noisy single-sample Monte Carlo estimate of the true policy divergence. This creates a...

### 10. Deep sequence models tend to memorize geometrically; it is unclear why.

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65556) / [AlphaXiv](https://www.alphaxiv.org/abs/2510.26745)

Deep sequence models are said to store atomic facts predominantly in the form of associative memory: a brute-force lookup of co-occurring entities. We identify a dramatically different form of storage of atomic facts that we term as geometric memory. Here, the model has synthesized embeddings encoding novel global relationships between all entities, including ones that do not co-occur in training. Such storage is powerful: for instance, we show how it transforms a hard reasoning task involving an $\ell$-fold...

### 11. Extracting alignment data in open models

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/66452) / [AlphaXiv](https://www.alphaxiv.org/abs/2510.18554)

In this work, we show that it is possible to extract significant amounts of alignment training data from a post-trained model -- useful to steer the model to improve certain capabilities such as long-context reasoning, safety, instruction following, and maths. While the majority of related work on memorisation has focused on measuring success of training data extraction through string matching, we argue that embedding models are better suited for our specific goals. Distances measured through a high quality...

### 12. Who Said Neural Networks Aren't Linear?

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65316) / [AlphaXiv](https://www.alphaxiv.org/abs/2510.08570)

Neural networks are famously nonlinear. However, linearity is defined relative to a pair of vector spaces, $f:\mathcal{X}\to\mathcal{Y}$. Leveraging the algebraic concept of transport of structure, we propose a method to explicitly identify non-standard vector spaces where a neural network acts as a linear operator. When sandwiching a linear operator $A$ between two invertible neural networks, $f(x)=g_y^{-1}(A g_x(x))$, the corresponding vector spaces $\mathcal{X}$ and $\mathcal{Y}$ are induced by newly defined...

### 13. The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61998) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.15165)

Diffusion Large Language Models (dLLMs) break the rigid left-to-right constraint of traditional LLMs, enabling token generation in arbitrary orders. Intuitively, this flexibility implies a solution space that strictly supersets the fixed autoregressive trajectory, theoretically unlocking superior reasoning potential. Indeed, for specific constraint satisfaction tasks (e.g., sudoku puzzles), this capability has proven to be highly advantageous. However, in this paper, we reveal that for general reasoning tasks...

### 14. To Grok Grokking: Provable Grokking in Ridge Regression

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/66206) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.19791)

We study *grokking* - the onset of generalization long after overfitting - in a classical ridge regression setting. We prove end-to-end grokking results for learning over-parameterized linear regression models using gradient descent with weight decay. Specifically, we prove that the following stages occur: (i) the model overfits the training data early during training; (ii) poor generalization persists long after overfitting has manifested; and (iii) the generalization error eventually becomes arbitrarily...

### 15. Maximum Likelihood Reinforcement Learning

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65332) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.02710)

Maximum likelihood is fundamental to supervised learning but it cannot be directly applied in correctness-based problems with non-differentiable sampling. In these settings, reinforcement learning (RL) is typically used to maximize expected reward. We show that for binary correctness tasks, expected-reward RL is a first-order approximation of the maximum likelihood objective, yielding vanishing learning signal on low-success inputs. We introduce **Maximum Likelihood Reinforcement Learning (MaxRL)**, a...

### 16. Reinforcement Learning with Evolving Rubrics for Deep Research

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65886) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.19399)

Deep research agents perform multi-step research to produce long-form, well-attributed answers. However, most open deep research agents are trained on easily verifiable short-form QA tasks via reinforcement learning with verifiable rewards, which does not extend to realistic long-form tasks. We address this with **Reinforcement Learning with Evolving Rubrics (RLER)**, where rubrics are constructed and maintained to *co-evolve* with the policy model during training. This allows the rubrics to incorporate newly...

### 17. Controlled LLM Training on Spectral Sphere

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/66212) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.08393)

Scaling large models requires optimization strategies that ensure rapid convergence grounded in stability. Maximal Update Parametrization ($\boldsymbol{\mu}$P) provides a theoretical safeguard for width-invariant $\Theta(1)$ activation control, whereas emerging optimizers like Muon are only "half-aligned" with these constraints: they control updates but allow weights to drift. To address this limitation, we introduce the **Spectral Sphere Optimizer (SSO)**, which enforces strict module-wise spectral constraints...

### 18. Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63561) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.03818)

Continual learning is a long-standing challenge in robot policy learning, where a policy must acquire new skills over time without catastrophically forgetting previously learned ones. While prior work has extensively studied continual learning in relatively small behavior cloning (BC) policy models trained from scratch, its behavior in modern large-scale pretrained Vision-Language-Action (VLA) models remains underexplored. In this work, we find that pretrained VLAs are remarkably resistant to forgetting...
