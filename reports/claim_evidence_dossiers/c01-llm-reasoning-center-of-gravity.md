# C01: LLM reasoning center of gravity Evidence Dossier

This is an abstract/title-based pre-review aid. It does not fill or replace the manual validation fields.

## Claim

LLM reasoning/post-training is the largest ICML 2026 area and is also overweight relative to nearby accepted-paper baselines.

- Strength label: `strong_for_landscape`
- Evidence summary: 1099 taxonomy papers (16.6%); historical delta +2.9 pp; public-attention enrichment 2.03x.
- Caveat: Area boundaries include general LLM training/evaluation and some diffusion-language papers; paper-level taxonomy still needs review.
- Next validation: Manually inspect boundary clusters 14, 21, and 24 before making subarea-level claims.
- Manual review progress: 0/14 rows reviewed; 14 remaining

## Pre-Review Summary

- Bucket mix: likely_supports: 14
- Selection mix: llm_boundary_cluster: 8, llm_high_attention_core: 6
- Area mix: LLM Reasoning, Post-Training, and RLVR: 14

## Adjudication Questions

- Does the abstract directly support the claim, or only share vocabulary with the claim?
- Is the assigned taxonomy area central to the paper, or just one application/context?
- If the paper is high-attention, is the attention driven by a reusable result, a benchmark, a demo, or a social trend?
- If the paper has a GitHub link, is it a real paper artifact and what reproduction claim can be safely made?

## Papers To Read First

- **How much can language models memorize?** (`likely_supports`; Outstanding Paper Honorable Mention, oral, taxonomy-review, github): Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training.
- **The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models** (`likely_supports`; Outstanding Paper Award, oral, taxonomy-review, github): Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training.
- **Maximum Likelihood Reinforcement Learning** (`likely_supports`; oral, taxonomy-review, github): Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training.
- **Reinforcement Learning with Evolving Rubrics for Deep Research** (`likely_supports`; oral, taxonomy-review, github): Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training.
- **Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers** (`likely_supports`; oral, taxonomy-review): Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training.
- **WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference** (`likely_supports`; oral, taxonomy-review, github): Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training.

## Paper-Level Pre-Review

| Rank | Paper | Bucket | Area | Signals | Why It Matters |
| ---: | --- | --- | --- | --- | --- |
| 1 | How much can language models memorize? | likely_supports | LLM Reasoning, Post-Training, and RLVR | Outstanding Paper Honorable Mention; oral; votes=271; github_stars=2; taxonomy-review | Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training. |
| 2 | The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models | likely_supports | LLM Reasoning, Post-Training, and RLVR | Outstanding Paper Award; oral; votes=92; github_stars=212; taxonomy-review | Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training. |
| 3 | Maximum Likelihood Reinforcement Learning | likely_supports | LLM Reasoning, Post-Training, and RLVR | oral; votes=259; github_stars=194; taxonomy-review | Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training. |
| 4 | Reinforcement Learning with Evolving Rubrics for Deep Research | likely_supports | LLM Reasoning, Post-Training, and RLVR | oral; votes=201; github_stars=682; taxonomy-review | Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training. |
| 5 | Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers | likely_supports | LLM Reasoning, Post-Training, and RLVR | oral; votes=75; taxonomy-review | Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training. |
| 6 | WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference | likely_supports | LLM Reasoning, Post-Training, and RLVR | oral; votes=60; github_stars=644; taxonomy-review | Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training. |
| 7 | OPUS: Towards Efficient and Principled Data Selection in Large Language Model Pre-training in Every Iteration | likely_supports | LLM Reasoning, Post-Training, and RLVR | oral; votes=57; taxonomy-review | Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training. |
| 8 | Learning to Theorize the World from Observation | likely_supports | LLM Reasoning, Post-Training, and RLVR | oral; votes=56; taxonomy-review | Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training. |
| 9 | Process Reward Models That Think | likely_supports | LLM Reasoning, Post-Training, and RLVR | votes=1815; github_stars=89 | Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training. |
| 10 | Reinforcement Learning via Self-Distillation | likely_supports | LLM Reasoning, Post-Training, and RLVR | votes=718; github_stars=1008; taxonomy-review | Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training. |
| 11 | Agent Learning via Early Experience | likely_supports | LLM Reasoning, Post-Training, and RLVR | votes=532; github_stars=148; taxonomy-review | Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training. |
| 12 | GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization | likely_supports | LLM Reasoning, Post-Training, and RLVR | votes=507; github_stars=489; taxonomy-review | Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training. |
| 13 | On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language Models | likely_supports | LLM Reasoning, Post-Training, and RLVR | votes=456; github_stars=160 | Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training. |
| 14 | Latent Collaboration in Multi-Agent Systems | likely_supports | LLM Reasoning, Post-Training, and RLVR | votes=402; github_stars=1048; taxonomy-review | Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training. |

## Abstract Excerpts

### 1. How much can language models memorize?

- Bucket: `likely_supports`
- Keyword hits: language model; llm; memorization
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62989) / [AlphaXiv](https://www.alphaxiv.org/abs/2505.24832)

We propose a new method for estimating how much a model knows about a datapoint and use it to measure the capacity of modern language models. Prior studies of language model memorization have struggled to disentangle memorization from generalization. We formally separate memorization into two components: unintended memorization, the information a model contains about a specific dataset, and generalization, the information a model contains about the true data-generation process. When we completely eliminate...

### 2. The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models

- Bucket: `likely_supports`
- Keyword hits: language model; llm; reasoning; grpo; diffusion language
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61998) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.15165)

Diffusion Large Language Models (dLLMs) break the rigid left-to-right constraint of traditional LLMs, enabling token generation in arbitrary orders. Intuitively, this flexibility implies a solution space that strictly supersets the fixed autoregressive trajectory, theoretically unlocking superior reasoning potential. Indeed, for specific constraint satisfaction tasks (e.g., sudoku puzzles), this capability has proven to be highly advantageous. However, in this paper, we reveal that for general reasoning tasks...

### 3. Maximum Likelihood Reinforcement Learning

- Bucket: `likely_supports`
- Keyword hits: llm; reinforcement learning; reward; grpo
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65332) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.02710)

Maximum likelihood is fundamental to supervised learning but it cannot be directly applied in correctness-based problems with non-differentiable sampling. In these settings, reinforcement learning (RL) is typically used to maximize expected reward. We show that for binary correctness tasks, expected-reward RL is a first-order approximation of the maximum likelihood objective, yielding vanishing learning signal on low-success inputs. We introduce **Maximum Likelihood Reinforcement Learning (MaxRL)**, a...

### 4. Reinforcement Learning with Evolving Rubrics for Deep Research

- Bucket: `likely_supports`
- Keyword hits: llm; reasoning; reinforcement learning; reward
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65886) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.19399)

Deep research agents perform multi-step research to produce long-form, well-attributed answers. However, most open deep research agents are trained on easily verifiable short-form QA tasks via reinforcement learning with verifiable rewards, which does not extend to realistic long-form tasks. We address this with **Reinforcement Learning with Evolving Rubrics (RLER)**, where rubrics are constructed and maintained to *co-evolve* with the policy model during training. This allows the rubrics to incorporate newly...

### 5. Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers

- Bucket: `likely_supports`
- Keyword hits: language model; llm; post-training
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65446) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.15674)

Large language model (LLM) activations are notoriously difficult to understand, with most existing techniques using complex, specialized methods for interpreting them. Recent work has proposed a simpler approach known as LatentQA: training LLMs to directly accept LLM activations as inputs and answer arbitrary questions about them in natural language. However, prior work has focused on narrow task settings for both training and evaluation. In this paper, we instead take a generalist perspective. We evaluate...

### 6. WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference

- Bucket: `likely_supports`
- Keyword hits: language model; llm; reasoning; diffusion language
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64095) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.22737)

Autoregressive (AR) generation is the standard decoding paradigm for Large Language Models (LLMs), but its token-by-token nature limits parallelism at inference time. Diffusion Language Models (DLLMs) offer parallel decoding by recovering multiple masked tokens per step; however, in practice they often fail to translate this parallelism into speed gains over optimized AR engines (e.g., vLLM). A key reason is that many DLLMs rely on bidirectional attention, which breaks standard prefix KV caching. We propose...

### 7. OPUS: Towards Efficient and Principled Data Selection in Large Language Model Pre-training in Every Iteration

- Bucket: `likely_supports`
- Keyword hits: language model; llm; pre-training
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61926) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.05400)

As high-quality public text approaches exhaustion, a phenomenon known as the Data Wall—LLM pre-training is shifting from more tokens to better tokens. However, existing methods either rely on heuristic static filters that ignore training dynamics, or use dynamic yet optimizer-agnostic criteria based on raw gradients. We propose OPUS (Optimizer-induced Projected Utility Selection), a dynamic framework that defines utility in the optimizer-induced update space. OPUS scores candidates by projecting their effective...

### 8. Learning to Theorize the World from Observation

- Bucket: `likely_supports`
- Keyword hits: llm
- URLs: [ICML](https://icml.cc/virtual/2026/poster/60765) / [AlphaXiv](https://www.alphaxiv.org/abs/2605.03413)

What does it mean to understand the world? Is it simply to predict future video frames? Developmental cognitive science suggests that understanding the world is fundamentally the process of constructing internal theories of how it works rather than mere prediction, even before language is acquired. However, in machine learning, it remains unclear how to endow AI systems with such theory-building capability from raw, non-textual observation alone. In this paper, we introduce Learning-to-Theorize (L2T), a...

### 9. Process Reward Models That Think

- Bucket: `likely_supports`
- Keyword hits: llm; reasoning; post-training; reward
- URLs: [ICML](https://icml.cc/virtual/2026/poster/68817) / [AlphaXiv](https://www.alphaxiv.org/abs/2504.16828)

Step-by-step verifiers—also known as process reward models (PRMs)—are a key ingredient for test-time scaling, but training them requires expensive step-level supervision. This work aims to build data-efficient PRMs as verbalized step-wise reward models that verify every step in the solution by generating a verification chain-of-thought (CoT). We propose ThinkPRM, a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. Our approach capitalizes on the...

### 10. Reinforcement Learning via Self-Distillation

- Bucket: `likely_supports`
- Keyword hits: language model; llm; reasoning; post-training; reinforcement learning; reward
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64121) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.20802)

Large language models are increasingly post-trained with reinforcement learning in verifiable domains such as code and math. Yet, current methods for reinforcement learning with verifiable rewards (RLVR) learn only from a scalar outcome reward per attempt, creating a severe credit-assignment bottleneck. Many verifiable environments actually provide rich textual feedback, such as runtime errors or judge evaluations, that explain *why* an attempt failed. We formalize this setting as reinforcement learning with...

### 11. Agent Learning via Early Experience

- Bucket: `likely_supports`
- Keyword hits: llm; reasoning; post-training; reinforcement learning; reward
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64488) / [AlphaXiv](https://www.alphaxiv.org/abs/2510.08558)

A long-term goal of language agents is to learn and improve through their own experience, ultimately outperforming humans in complex, real-world tasks. However, training agents from experience data with reinforcement learning remains difficult in many environments, which either lack verifiable rewards (e.g., websites) or require inefficient long-horizon rollouts (e.g., multi-turn tool use). As a result, most current agents rely on supervised fine-tuning on expert data, which is challenging to scale and...

### 12. GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization

- Bucket: `likely_supports`
- Keyword hits: language model; llm; reasoning; post-training; reinforcement learning; reward; grpo
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63333) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.05242)

As language models become increasingly capable, users expect them to provide not only accurate responses but also behaviors aligned with diverse human preferences across a variety of scenarios. To achieve this, Reinforcement learning (RL) pipelines have begun incorporating multiple rewards, each capturing a distinct preference, to guide models toward these desired behaviors. However, recent work has defaulted to apply Group Relative Policy Optimization (GRPO) under multi-reward setting without examining its...

### 13. On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language Models

- Bucket: `likely_supports`
- Keyword hits: language model; llm; reasoning; post-training; reinforcement learning; reward; pre-training
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63850) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.07783)

Recent reinforcement learning (RL) techniques have yielded impressive reasoning improvements in language models, yet it remains unclear whether post-training truly extends a model’s reasoning ability beyond what it acquires during pre-training. A central challenge is the lack of control in modern training pipelines: large-scale pre-training corpora are opaque, mid-training is often underexamined, and RL objectives interact with unknown prior knowledge in complex ways. To resolve this ambiguity, we develop a...

### 14. Latent Collaboration in Multi-Agent Systems

- Bucket: `likely_supports`
- Keyword hits: language model; llm; reasoning
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61180) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.20639)

Multi-agent systems (MAS) extend large language models (LLMs) from independent single-model reasoning to coordinative system-level intelligence. While existing LLM agents depend on text-based mediation for reasoning and communication, we take a step forward by enabling models to collaborate directly within the continuous latent space. We introduce LatentMAS, an end-to-end training-free framework that enables pure latent collaboration among LLM agents. In LatentMAS, each agent first performs auto-regressive...
