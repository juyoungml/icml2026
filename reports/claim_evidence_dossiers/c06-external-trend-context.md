# C06: External trend context Evidence Dossier

This is an abstract/title-based pre-review aid. It does not fill or replace the manual validation fields.

## Claim

The fastest broad arXiv growth areas are multimodal/vision, LLM reasoning, and safety/governance, but ICML 2026 does not mirror this ranking exactly.

- Strength label: `context_only`
- Evidence summary: Multimodal, Vision, and Perception: 94.6%; LLM Reasoning, Post-Training, and RLVR: 59.9%; Safety, Governance, Privacy, and Society: 53.6%; Systems and Efficient Foundation Models: 43.3%
- Caveat: arXiv queries are broad, overlapping, and not acceptance or quality signals.
- Next validation: Use accepted-paper corpora, not arXiv counts, for publication-ready year-over-year venue claims.
- Manual review progress: 0/16 rows reviewed; 16 remaining

## Pre-Review Summary

- Bucket mix: possible_support: 14, unclear: 2
- Selection mix: fast_arxiv_area_sample: 16
- Area mix: Multimodal, Vision, and Perception: 4, LLM Reasoning, Post-Training, and RLVR: 4, Safety, Governance, Privacy, and Society: 4, Systems and Efficient Foundation Models: 4

## Adjudication Questions

- Does the abstract directly support the claim, or only share vocabulary with the claim?
- Is the assigned taxonomy area central to the paper, or just one application/context?
- If the paper is high-attention, is the attention driven by a reusable result, a benchmark, a demo, or a social trend?
- If the paper has a GitHub link, is it a real paper artifact and what reproduction claim can be safely made?

## Papers To Read First

- **Process Reward Models That Think** (`unclear`; github): No strong abstract/title cue for the claim.
- **Reinforcement Learning via Self-Distillation** (`possible_support`; taxonomy-review, github): Keyword overlap with the claim, but human reading is needed.
- **mHC: Manifold-Constrained Hyper-Connections** (`possible_support`; taxonomy-review, github): Keyword overlap with the claim, but human reading is needed.
- **Agent Learning via Early Experience** (`possible_support`; taxonomy-review, github): Keyword overlap with the claim, but human reading is needed.
- **xKV: Cross-Layer KV-Cache Compression via Aligned Singular Vector Extraction** (`possible_support`; github): Keyword overlap with the claim, but human reading is needed.
- **GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization** (`possible_support`; taxonomy-review, github): Keyword overlap with the claim, but human reading is needed.

## Paper-Level Pre-Review

| Rank | Paper | Bucket | Area | Signals | Why It Matters |
| ---: | --- | --- | --- | --- | --- |
| 1 | A Very Big Video Reasoning Suite | possible_support | Multimodal, Vision, and Perception | votes=159; github_stars=25 | Keyword overlap with the claim, but human reading is needed. |
| 2 | Causal-JEPA: Learning World Models through Object-Level Latent Interventions | possible_support | Multimodal, Vision, and Perception | votes=150; github_stars=206 | Keyword overlap with the claim, but human reading is needed. |
| 3 | ExSkill: Continual Learning from Experience and Skills in Multimodal Agents | possible_support | Multimodal, Vision, and Perception | votes=147; github_stars=234 | Keyword overlap with the claim, but human reading is needed. |
| 4 | BabyVision: Visual Reasoning Beyond Language | possible_support | Multimodal, Vision, and Perception | votes=134; github_stars=227 | Keyword overlap with the claim, but human reading is needed. |
| 5 | Process Reward Models That Think | unclear | LLM Reasoning, Post-Training, and RLVR | votes=1815; github_stars=89 | No strong abstract/title cue for the claim. |
| 6 | Reinforcement Learning via Self-Distillation | possible_support | LLM Reasoning, Post-Training, and RLVR | votes=718; github_stars=1008; taxonomy-review | Keyword overlap with the claim, but human reading is needed. |
| 7 | Agent Learning via Early Experience | possible_support | LLM Reasoning, Post-Training, and RLVR | votes=532; github_stars=148; taxonomy-review | Keyword overlap with the claim, but human reading is needed. |
| 8 | GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization | possible_support | LLM Reasoning, Post-Training, and RLVR | votes=507; github_stars=489; taxonomy-review | Keyword overlap with the claim, but human reading is needed. |
| 9 | Chain-of-Thought Reasoning In The Wild Is Not Always Faithful | possible_support | Safety, Governance, Privacy, and Society | votes=253; github_stars=35 | Keyword overlap with the claim, but human reading is needed. |
| 10 | The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models | possible_support | Safety, Governance, Privacy, and Society | votes=127 | Keyword overlap with the claim, but human reading is needed. |
| 11 | Reasoning Models Struggle to Control their Chains of Thought | possible_support | Safety, Governance, Privacy, and Society | votes=75; github_stars=50 | Keyword overlap with the claim, but human reading is needed. |
| 12 | Towards a Science of AI Agent Reliability | possible_support | Safety, Governance, Privacy, and Society | votes=72 | Keyword overlap with the claim, but human reading is needed. |
| 13 | mHC: Manifold-Constrained Hyper-Connections | possible_support | Systems and Efficient Foundation Models | votes=696; github_stars=367; taxonomy-review | Keyword overlap with the claim, but human reading is needed. |
| 14 | xKV: Cross-Layer KV-Cache Compression via Aligned Singular Vector Extraction | possible_support | Systems and Efficient Foundation Models | votes=518; github_stars=52 | Keyword overlap with the claim, but human reading is needed. |
| 15 | Evolution Strategies at the Hyperscale | possible_support | Systems and Efficient Foundation Models | votes=405; github_stars=346; taxonomy-review | Keyword overlap with the claim, but human reading is needed. |
| 16 | Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights | unclear | Systems and Efficient Foundation Models | votes=365; github_stars=627; taxonomy-review | No strong abstract/title cue for the claim. |

## Abstract Excerpts

### 1. A Very Big Video Reasoning Suite

- Bucket: `possible_support`
- Keyword hits: foundation
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65709) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.20159)

Video reasoning grounds intelligence in spatiotemporally consistent visual environments that go beyond what text can naturally capture, enabling intuitive reasoning over motion, interaction, and causality. Rapid progress in video models has focused primarily on visual quality. Systematically studying video reasoning and its scaling behavior suffers from a lack of video reasoning (training) data. To address this gap, we introduce the Very Big Video Reasoning (VBVR) Dataset, an unprecedentedly large-scale...

### 2. Causal-JEPA: Learning World Models through Object-Level Latent Interventions

- Bucket: `possible_support`
- Keyword hits: safety
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63623) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.11389)

World models require robust relational understanding to support prediction, reasoning, and control. While object-centric representations provide a useful abstraction, they are not sufficient to capture interaction-dependent dynamics. We therefore propose C-JEPA, a simple and flexible object-centric world model that extends masked joint embedding prediction from image patches to object-centric representations. By applying object-level masking that requires an object’s state to be inferred from other objects,...

### 3. ExSkill: Continual Learning from Experience and Skills in Multimodal Agents

- Bucket: `possible_support`
- Keyword hits: multimodal
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65729) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.12056)

Multimodal agents demonstrate impressive problem-solving capabilities but typically operate in isolated episodes without leveraging past experiences. Recent methods address this through dynamic retrieval of textual insights or predefined skill documents, yet face critical challenges: visual modalities are neglected during knowledge extraction, stored insights lack executable structure, and manually crafted skills fail to scale. We propose \textsc{ExSkill}, a framework combining task-level Skills (structured...

### 4. BabyVision: Visual Reasoning Beyond Language

- Bucket: `possible_support`
- Keyword hits: multimodal
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63195) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.06521)

While humans develop core visual skills long before acquiring language, contemporary Multimodal LLMs (MLLMs) still rely heavily on linguistic priors to compensate for their fragile visual understanding. We uncovered a crucial fact: state-of-the-art MLLMs consistently fail on basic visual tasks that humans, even 3-year-olds, can solve effortlessly. To systematically investigate this gap, we introduce BabyVision, a benchmark designed to assess core visual abilities independent of linguistic knowledge for MLLMs....

### 5. Process Reward Models That Think

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/68817) / [AlphaXiv](https://www.alphaxiv.org/abs/2504.16828)

Step-by-step verifiers—also known as process reward models (PRMs)—are a key ingredient for test-time scaling, but training them requires expensive step-level supervision. This work aims to build data-efficient PRMs as verbalized step-wise reward models that verify every step in the solution by generating a verification chain-of-thought (CoT). We propose ThinkPRM, a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. Our approach capitalizes on the...

### 6. Reinforcement Learning via Self-Distillation

- Bucket: `possible_support`
- Keyword hits: language model
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64121) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.20802)

Large language models are increasingly post-trained with reinforcement learning in verifiable domains such as code and math. Yet, current methods for reinforcement learning with verifiable rewards (RLVR) learn only from a scalar outcome reward per attempt, creating a severe credit-assignment bottleneck. Many verifiable environments actually provide rich textual feedback, such as runtime errors or judge evaluations, that explain *why* an attempt failed. We formalize this setting as reinforcement learning with...

### 7. Agent Learning via Early Experience

- Bucket: `possible_support`
- Keyword hits: foundation
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64488) / [AlphaXiv](https://www.alphaxiv.org/abs/2510.08558)

A long-term goal of language agents is to learn and improve through their own experience, ultimately outperforming humans in complex, real-world tasks. However, training agents from experience data with reinforcement learning remains difficult in many environments, which either lack verifiable rewards (e.g., websites) or require inefficient long-horizon rollouts (e.g., multi-turn tool use). As a result, most current agents rely on supervised fine-tuning on expert data, which is challenging to scale and...

### 8. GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization

- Bucket: `possible_support`
- Keyword hits: language model
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63333) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.05242)

As language models become increasingly capable, users expect them to provide not only accurate responses but also behaviors aligned with diverse human preferences across a variety of scenarios. To achieve this, Reinforcement learning (RL) pipelines have begun incorporating multiple rewards, each capturing a distinct preference, to guide models toward these desired behaviors. However, recent work has defaulted to apply Group Relative Policy Optimization (GRPO) under multi-reward setting without examining its...

### 9. Chain-of-Thought Reasoning In The Wild Is Not Always Faithful

- Bucket: `possible_support`
- Keyword hits: safety
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64450) / [AlphaXiv](https://www.alphaxiv.org/abs/2503.08679)

Recent studies indicate that when faced with explicit biases in prompts, models often omit mentioning these biases in their Chain-of-Thought (CoT) output, revealing that verbalized reasoning can give an incorrect picture of how models arrive at conclusions (unfaithfulness). In this work, we show that unfaithful CoT also occurs on naturally worded, non-adversarial prompts without adding artificial biases or editing model outputs. We find that when separately presented with the questions "Is X bigger than Y?" and...

### 10. The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models

- Bucket: `possible_support`
- Keyword hits: language model
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61446) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.10387)

Large language models can represent a variety of personas but typically default to a helpful Assistant identity cultivated during post-training. Across several different models, we find an “Assistant Axis" in their activation space, which captures the extent to which a model is operating in its default Assistant mode. Steering towards the Assistant direction reinforces helpful and harmless behavior; steering away increases the model’s tendency to identify as other entities. Measuring deviations along the...

### 11. Reasoning Models Struggle to Control their Chains of Thought

- Bucket: `possible_support`
- Keyword hits: safety
- URLs: [ICML](https://icml.cc/virtual/2026/poster/66446) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.05706)

Instruction following in LLMs captures models' ability to change their visible behaviors as requested by users. Instead, we study models' ability to control their chain-of-thought (CoT). This capability -- CoT controllability -- is undesirable because it could allow models to suppress signs of misbehavior in their CoT, thereby undermining our ability to monitor them. To measure this, we introduce the \emph{CoT-Control} evaluation suite. We show that reasoning models are less able to follow instructions in their...

### 12. Towards a Science of AI Agent Reliability

- Bucket: `possible_support`
- Keyword hits: safety
- URLs: [ICML](https://icml.cc/virtual/2026/poster/66364) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.16666)

AI agents are increasingly deployed for consequential tasks. Yet existing benchmarks evaluate only task success rates, ignoring whether agents behave consistently, remain robust to perturbations, fail predictably, or bound error severity. We propose a framework for measuring agent reliability grounded in safety-critical engineering practice, decomposing reliability into four dimensions: consistency, robustness, predictability, and safety. Applying these metrics to 12 frontier models across two complementary...

### 13. mHC: Manifold-Constrained Hyper-Connections

- Bucket: `possible_support`
- Keyword hits: foundation
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61870) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.24880)

Recently, studies exemplified by Hyper-Connections (HC) have extended the ubiquitous residual connection paradigm established over the past decade by expanding the residual stream width and diversifying connectivity patterns. While yielding substantial performance gains, this diversification fundamentally compromises the identity mapping property intrinsic to the residual connection, which causes severe training instability and restricted scalability, and additionally incurs notable memory access overhead. To...

### 14. xKV: Cross-Layer KV-Cache Compression via Aligned Singular Vector Extraction

- Bucket: `possible_support`
- Keyword hits: language model
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63436) / [AlphaXiv](https://www.alphaxiv.org/abs/2503.18893)

Long-context Large Language Models (LLMs) enable powerful applications but incur high memory costs due to the key–value states (KV-Cache). Recent studies attempt to share KV-Cache across layers, but these approaches either require expensive pretraining or rely on per-token cross-layer cosine similarity that is often limited in practice. We show, via Centered Kernel Alignment (CKA), that the dominant singular vectors of KV-Cache are well aligned across layers. Motivated by this observation, we propose xKV, a...

### 15. Evolution Strategies at the Hyperscale

- Bucket: `possible_support`
- Keyword hits: language model
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62943) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.16652)

Evolution Strategies (ES) is a class of powerful black-box optimisation methods that are highly parallelisable and can handle non-differentiable and noisy objectives. However, naïve ES becomes prohibitively expensive at scale on GPUs due to the low arithmetic intensity of batched matrix multiplications with unstructured random perturbations. We introduce Evolution Guided GeneRal Optimisation via Low-rank Learning (EGGROLL), which improves arithmetic intensity by structuring individual perturbations as rank-$r$...

### 16. Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights

- Bucket: `unclear`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65901) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.12228)

Pretraining produces a learned parameter vector that is typically treated as a starting point for further iterative adaptation. In this work, we instead view the outcome of pretraining as a distribution over parameter vectors, whose support already contains task-specific experts. We show that in smaller or insufficiently trained models such expert solutions occupy a negligible fraction of the volume of this distribution, making their discovery reliant on structured optimization methods such as gradient descent....
