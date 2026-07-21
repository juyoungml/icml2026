# LLM Reasoning, Post-Training, and RLVR

Manual validation packet for representative and boundary papers.

## Area Context

Headline: Reasoning progress is splitting between reward-driven post-training, test-time search, and alternative sequence modeling.

Fault lines:
- Process supervision and reward models versus search, verification, and extra test-time compute.
- Verifiable math/code-style tasks versus open-ended research, planning, and multimodal reasoning.
- Autoregressive reasoning versus diffusion or arbitrary-order language generation.

What to read for:
- Does the paper optimize final answers, intermediate traces, rubrics, or verifier signals?
- Are gains robust outside tasks with cheap correctness checks?
- Does extra inference compute change capability, reliability, or only benchmark score?

## Queue Summary

- Papers: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, program_signal_low_public_attention=4, taxonomy_boundary_cluster=2
- Papers from taxonomy-review clusters: 15
- Papers with GitHub URLs: 11

## Papers

### 1. How much can language models memorize?

Flags: fault_line_representative, oral, Outstanding Paper Honorable Mention, taxonomy-review, github

- Subarea: Diffusion language models and decoding
- Votes: 271
- ICML URL: https://icml.cc/virtual/2026/poster/62989
- AlphaXiv URL: https://www.alphaxiv.org/abs/2505.24832
- GitHub URL: https://github.com/SimonCao1207/LLM-Capacity
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Method / algorithm
- Method families: Transformer / attention
- Evaluation settings: language/llm
- Result claim cues: scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

We propose a new method for estimating how much a model knows about a datapoint and use it to measure the capacity of modern language models. Prior studies of language model memorization have struggled to disentangle memorization from generalization. We formally separate memorization into two components: unintended memorization, the information a model contains about a specific dataset, and generalization, the information a model contains about the true data-generation process. When we completely eliminate generalization, we can compute the total memorization, which provides an estimate of model capacity: our measurements estimate that GPT-style models have a capacity of approximately 3.6 bits per parameter. We train language models on datasets of increasing size and observe that models memorize until their capacity fills, at which point unintended memorization decreases as models begin to generalize. We train hundreds of transformer language models ranging from 500K to 1.5B parameters and produce a series of scaling laws relating model capacity and data size to membership inference.

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

### 2. The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models

Flags: fault_line_representative, oral, Outstanding Paper Award, taxonomy-review, github

- Subarea: Reasoning models and chain-of-thought behavior
- Votes: 92
- ICML URL: https://icml.cc/virtual/2026/poster/61998
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.15165
- GitHub URL: https://github.com/LeapLabTHU/JustGRPO
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: RL / policy optimization; Reasoning / test-time compute; Diffusion / flow
- Evaluation settings: language/llm
- Result claim cues: negative / limitation
- Benchmarks: none
- Datasets: none
- Metrics: accuracy

Abstract:

Diffusion Large Language Models (dLLMs) break the rigid left-to-right constraint of traditional LLMs, enabling token generation in arbitrary orders. Intuitively, this flexibility implies a solution space that strictly supersets the fixed autoregressive trajectory, theoretically unlocking superior reasoning potential. Indeed, for specific constraint satisfaction tasks (e.g., sudoku puzzles), this capability has proven to be highly advantageous. However, in this paper, we reveal that for general reasoning tasks (e.g., mathematics and coding), arbitrary order generation may in fact limit the reasoning potential of dLLMs. We find that dLLMs tend to exploit this order flexibility to bypass high-uncertainty tokens that are crucial for exploration, leading to a premature collapse of solution coverage. This observation motivates a rethink of RL approaches for dLLMs, where considerable complexities, such as handling combinatorial trajectories and intractable likelihoods, are often devoted to preserving this flexibility. We demonstrate that effective reasoning can be better elicited by simply forgoing arbitrary order and applying standard Group Relative Policy Optimization (GRPO) instead. Our approach, **JustGRPO**, is minimalist yet surprisingly effective (e.g., 89.1% accuracy on GSM8K) while fully retaining the parallel decoding ability of dLLMs.

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

### 3. Maximum Likelihood Reinforcement Learning

Flags: fault_line_representative, oral, taxonomy-review, github

- Subarea: Reward modeling, preference feedback, and RL post-training
- Votes: 259
- ICML URL: https://icml.cc/virtual/2026/poster/65332
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.02710
- GitHub URL: https://github.com/tajwarfahim/maxrl
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: RL / policy optimization; Diffusion / flow
- Evaluation settings: language/llm
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: pass@k; reward

Abstract:

Maximum likelihood is fundamental to supervised learning but it cannot be directly applied in correctness-based problems with non-differentiable sampling. In these settings, reinforcement learning (RL) is typically used to maximize expected reward. We show that for binary correctness tasks, expected-reward RL is a first-order approximation of the maximum likelihood objective, yielding vanishing learning signal on low-success inputs. We introduce **Maximum Likelihood Reinforcement Learning (MaxRL)**, a compute-indexed family of sampling-based objectives derived from a pass@k expansion of the likelihood, which interpolates between standard RL and exact maximum likelihood as compute increases. MaxRL admits a simple unbiased policy-gradient estimator whose optimized objective improves with additional compute. Across multiple domains, MaxRL consistently outperforms standard RL and GRPO, achieving higher $pass@1$ and substantially improved $pass@k$.

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

### 4. Reinforcement Learning with Evolving Rubrics for Deep Research

Flags: fault_line_representative, oral, taxonomy-review, github

- Subarea: Reward modeling, preference feedback, and RL post-training
- Votes: 201
- ICML URL: https://icml.cc/virtual/2026/poster/65886
- AlphaXiv URL: https://www.alphaxiv.org/abs/2511.19399
- GitHub URL: https://github.com/rlresearch/dr-tulu
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Application / domain study; Method / algorithm
- Method families: RL / policy optimization; Reasoning / test-time compute; Agents / tool use
- Evaluation settings: math/code/verifiable; language/llm
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Deep research agents perform multi-step research to produce long-form, well-attributed answers. However, most open deep research agents are trained on easily verifiable short-form QA tasks via reinforcement learning with verifiable rewards, which does not extend to realistic long-form tasks. We address this with **Reinforcement Learning with Evolving Rubrics (RLER)**, where rubrics are constructed and maintained to *co-evolve* with the policy model during training. This allows the rubrics to incorporate newly explored information from search and contrasting model responses, enabling better fact checking and more discriminative on-policy feedback. Using RLER, we develop **Deep Research Tulu (DR Tulu-8B)**, the first fully open model that is directly trained for open-ended, long-form deep research. Across four long-form deep research benchmarks in science, healthcare, and general domains, DR Tulu-8B substantially outperforms existing open deep research agents (by 15.6% over Tongyi DR on average) and matches or exceeds proprietary deep research agents (by 0.7% over OpenAI DR on average), while being significantly smaller and cheaper per query (1000x cheaper than OpenAI DR per query).

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

### 5. Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers

Flags: fault_line_representative, oral, taxonomy-review

- Subarea: General LLM training, evaluation, and alignment
- Votes: 75
- ICML URL: https://icml.cc/virtual/2026/poster/65446
- AlphaXiv URL: https://www.alphaxiv.org/abs/2512.15674
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Benchmark / evaluation; Dataset / data resource; Method / algorithm
- Method families: LLM post-training
- Evaluation settings: language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: LatentQA; LatentQA-trained
- Datasets: none
- Metrics: none

Abstract:

Large language model (LLM) activations are notoriously difficult to understand, with most existing techniques using complex, specialized methods for interpreting them. Recent work has proposed a simpler approach known as LatentQA: training LLMs to directly accept LLM activations as inputs and answer arbitrary questions about them in natural language. However, prior work has focused on narrow task settings for both training and evaluation. In this paper, we instead take a generalist perspective. We evaluate LatentQA-trained models, which we call Activation Oracles (AOs), in far out-of-distribution settings and examine how performance scales with training data diversity. We find that AOs can recover information fine-tuned into a model (e.g., biographical knowledge or malign propensities) that does not appear in the input text, despite never being trained with activations from a fine-tuned model. Our main evaluations are four downstream tasks where we can compare to prior white- and black-box techniques. We find that even narrowly-trained LatentQA models can generalize well, and that adding additional training datasets (such as classification tasks and a self-supervised context prediction task) yields consistent further improvements. Our best AOs match or exceed white-box baselines on all four tasks and the best overall baseline on 3 of 4. These results suggest that diversified training to answer natural-language queries imparts a general capability to verbalize information about LLM activations.

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

### 6. WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference

Flags: fault_line_representative, oral, taxonomy-review, github

- Subarea: Diffusion language models and decoding
- Votes: 60
- ICML URL: https://icml.cc/virtual/2026/poster/64095
- AlphaXiv URL: https://www.alphaxiv.org/abs/2512.22737
- GitHub URL: https://github.com/Tencent/WeDLM
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; System / infrastructure; Method / algorithm
- Method families: Reasoning / test-time compute; Diffusion / flow; Transformer / attention; Causal / data-centric
- Evaluation settings: language/llm
- Result claim cues: negative / limitation
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Autoregressive (AR) generation is the standard decoding paradigm for Large Language Models (LLMs), but its token-by-token nature limits parallelism at inference time. Diffusion Language Models (DLLMs) offer parallel decoding by recovering multiple masked tokens per step; however, in practice they often fail to translate this parallelism into speed gains over optimized AR engines (e.g., vLLM). A key reason is that many DLLMs rely on bidirectional attention, which breaks standard prefix KV caching. We propose WeDLM, a diffusion decoding framework built entirely on standard causal attention to make parallel generation prefix-cache friendly. The core idea is to let each masked position condition on all observed tokens while keeping a causal mask, achieved by Topological Reordering that moves observed tokens to the physical prefix while preserving their logical positions. Building on this, we introduce a streaming decoding procedure that continuously commits confident tokens into a growing left-to-right prefix, avoiding the stop-and-wait behavior common in block diffusion methods. Experiments show that WeDLM preserves the quality of strong AR backbones while delivering substantial speedups, approaching 3× on challenging reasoning benchmarks and up to 10× in low-entropy generation regimes; critically, our comparisons are against AR baselines served by vLLM under matched deployment settings.

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

### 7. Process Reward Models That Think

Flags: public_attention_not_program_signal, github

- Subarea: RL for reasoning models and verifiable rewards
- Votes: 1815
- ICML URL: https://icml.cc/virtual/2026/poster/68817
- AlphaXiv URL: https://www.alphaxiv.org/abs/2504.16828
- GitHub URL: https://github.com/mukhal/thinkprm
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; Method / algorithm
- Method families: RL / policy optimization; LLM post-training; Reasoning / test-time compute
- Evaluation settings: math/code/verifiable; language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: ProcessBench; GPQA-Diamond; LiveCodeBench
- Datasets: none
- Metrics: reward

Abstract:

Step-by-step verifiers—also known as process reward models (PRMs)—are a key ingredient for test-time scaling, but training them requires expensive step-level supervision. This work aims to build data-efficient PRMs as verbalized step-wise reward models that verify every step in the solution by generating a verification chain-of-thought (CoT). We propose ThinkPRM, a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. Our approach capitalizes on the inherent reasoning abilities of long CoT models, and outperforms LLM-as-a-Judge and discriminative verifiers—using only 1% of the process labels in PRM800K—across several challenging benchmarks. Specifically, ThinkPRM beats the baselines on ProcessBench, MATH-500, and AIME ’24 under best-of-N selection and reward-guided search. In an out-of-domain evaluation over subsets of GPQA-Diamond and LiveCodeBench, our PRM surpasses discriminative verifiers trained with the full PRM800K by 8% and 4.5%, respectively. Lastly, under the same token budget, ThinkPRM scales up verification compute more effectively compared to LLM-as-a-Judge, outperforming it by 7.2% on a subset of ProcessBench. This work highlights the value of generative, long CoT PRMs that can scale test-time compute for verification while requiring minimal supervision for training.

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

### 8. Reinforcement Learning via Self-Distillation

Flags: public_attention_not_program_signal, taxonomy-review, github

- Subarea: Reward modeling, preference feedback, and RL post-training
- Votes: 718
- ICML URL: https://icml.cc/virtual/2026/poster/64121
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.20802
- GitHub URL: https://github.com/lasgroup/SDPO
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Method / algorithm
- Method families: RL / policy optimization; LLM post-training; Reasoning / test-time compute; Agents / tool use; Diffusion / flow
- Evaluation settings: math/code/verifiable; language/llm
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: LiveCodeBench
- Datasets: none
- Metrics: accuracy; reward

Abstract:

Large language models are increasingly post-trained with reinforcement learning in verifiable domains such as code and math. Yet, current methods for reinforcement learning with verifiable rewards (RLVR) learn only from a scalar outcome reward per attempt, creating a severe credit-assignment bottleneck. Many verifiable environments actually provide rich textual feedback, such as runtime errors or judge evaluations, that explain *why* an attempt failed. We formalize this setting as reinforcement learning with rich feedback and introduce **Self-Distillation Policy Optimization** (**SDPO**), which converts tokenized feedback into a dense learning signal without any external teacher or explicit reward model. SDPO treats the current model conditioned on feedback as a self-teacher and distills its feedback-informed next-token predictions back into the policy. In this way, SDPO leverages the model's ability to retrospectively identify its own mistakes in-context. Across scientific reasoning, tool use, and competitive programming on LiveCodeBench v6, SDPO improves sample efficiency and final accuracy over strong RLVR baselines. Notably, SDPO also outperforms baselines in standard RLVR environments that only return scalar feedback by using successful rollouts as implicit feedback for failed attempts. Finally, applying SDPO to individual questions at test time accelerates discovery on difficult binary-reward tasks, achieving the same discovery probability as best-of-k sampling or multi-turn conversations with 3x fewer attempts.

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

### 9. Agent Learning via Early Experience

Flags: public_attention_not_program_signal, taxonomy-review, github

- Subarea: Reward modeling, preference feedback, and RL post-training
- Votes: 532
- ICML URL: https://icml.cc/virtual/2026/poster/64488
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.08558
- GitHub URL: https://github.com/jettbrains/-L-
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: RL / policy optimization; LLM post-training; Reasoning / test-time compute; Agents / tool use
- Evaluation settings: math/code/verifiable; language/llm
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: reward

Abstract:

A long-term goal of language agents is to learn and improve through their own experience, ultimately outperforming humans in complex, real-world tasks. However, training agents from experience data with reinforcement learning remains difficult in many environments, which either lack verifiable rewards (e.g., websites) or require inefficient long-horizon rollouts (e.g., multi-turn tool use). As a result, most current agents rely on supervised fine-tuning on expert data, which is challenging to scale and generalizes poorly. This limitation stems from the nature of expert demonstrations: they capture only a narrow range of scenarios, and expose the agent to limited environment diversity. We address this limitation with a middle-ground paradigm we call *early experience*: interaction data generated by the agent's own actions, where the resulting future states serve as supervision without reward signals. Within this paradigm, we study two strategies of using such data: (1) implicit world modeling, which uses collected states to ground the policy in environment dynamics; and (2) self-reflection, where the agent learns from its suboptimal actions to improve reasoning and decision-making. Evaluation across eight diverse environments and multiple model families shows that our approaches consistently improve effectiveness and out-of-domain generalization, highlighting the value of early experience. Moreover, in environments with verifiable rewards, our results provide promising signals that early experience offers a strong foundation for subsequent reinforcement learning, making it a practical bridge between imitation learning and fully experience-driven agents.

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

### 10. GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization

Flags: public_attention_not_program_signal, taxonomy-review, github

- Subarea: Reward modeling, preference feedback, and RL post-training
- Votes: 507
- ICML URL: https://icml.cc/virtual/2026/poster/63333
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.05242
- GitHub URL: https://github.com/NVlabs/GDPO
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: RL / policy optimization; LLM post-training; Reasoning / test-time compute; Agents / tool use
- Evaluation settings: math/code/verifiable; language/llm
- Result claim cues: negative / limitation; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: accuracy; reward

Abstract:

As language models become increasingly capable, users expect them to provide not only accurate responses but also behaviors aligned with diverse human preferences across a variety of scenarios. To achieve this, Reinforcement learning (RL) pipelines have begun incorporating multiple rewards, each capturing a distinct preference, to guide models toward these desired behaviors. However, recent work has defaulted to apply Group Relative Policy Optimization (GRPO) under multi-reward setting without examining its suitability. In this paper, we demonstrate that directly applying GRPO to normalize distinct rollout reward combinations causes them to collapse into identical advantage values, reducing the resolution of the training signal and resulting in suboptimal convergence and, in some cases, early training failure. We then introduce Group reward-Decoupled Normalization Policy Optimization (GDPO), a new policy optimization method to resolve these issues by decoupling the normalization of individual rewards, more faithfully preserving their relative differences and enabling more accurate multi-reward optimization, along with substantially improved training stability. We compare GDPO with GRPO across three tasks: tool calling, math reasoning, and coding reasoning, evaluating both correctness metrics (accuracy, bug ratio) and constraint adherence metrics (format, length). Across all settings, GDPO consistently outperforms GRPO, demonstrating its effectiveness and generalizability for multi-reward reinforcement learning optimization.

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

### 11. Diffract: Spectral View of LLM Domain Adaptation

Flags: program_signal_low_public_attention, oral, taxonomy-review

- Subarea: General LLM training, evaluation, and alignment
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/63441
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Method / algorithm
- Method families: Agents / tool use; Transformer / attention
- Evaluation settings: math/code/verifiable; language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: accuracy

Abstract:

We study continual pre-training (CPT) as a mechanism for adapting general-purpose large language models to specialized domains: mathematics, instruction, code, and natural text. Using singular value decomposition of weight matrices, we find that CPT leaves singular value spectra largely invariant, with adaptation driven mainly by changes in singular vectors. An analysis of attention-head projection matrices reveals strong, domain-dependent **head heterogeneity**, which we exploit to define a head-importance criterion: up to **60\%** of head updates can be removed without measurable quality loss. Selectively rewinding low-importance heads to their pre-trained state improves benchmark accuracy by up to **4\%** versus the fully trained baseline. Finally, we identify **domain connectivity**—linear interpolation between CPT checkpoints yields smooth domain-quality interpolation without notable degradation on either domain—and release Diffract, an open-source toolkit for scalable spectral analysis of billion-parameter models.

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

### 12. FlatLand: Personalized Graph Federated Learning via Tailored Lorentz Space

Flags: program_signal_low_public_attention, oral, taxonomy-review

- Subarea: General LLM training, evaluation, and alignment
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/65064
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Method / algorithm
- Method families: LLM post-training; Compression / efficiency; Graphs / geometry
- Evaluation settings: language/llm
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Personalization has become a pivotal field of study in contemporary intelligent systems. While large language models (LLMs) excel at general knowledge tasks, they often struggle with personalization, i.e., adapting their outputs to individual user expectations. Existing approaches that steer LLM behavior to meet users’ implicit preferences and behavior patterns, primarily relying on tune-free methods (e.g., RAG, PAG) or parameter fine-tuning methods (e.g., LoRA), face challenges in effectively balancing effectiveness and efficiency. Moreover, the mechanisms underlying personalized preferences remain underexplored. To address these challenges, we first uncover key patterns of user-specific information embedded in the representation space. Specifically, we find that (1) personalized information lies within a low-rank subspace represented by vectors, and (2) these vectors demonstrate both a collective shift shared across users and a personalized shift unique to each individual user. Building on these insights, we introduce PerFit, a novel two-stage solution that directly fine-tunes interventions in the hidden representation space by addressing both collective and user-specific shifts, thereby achieving precise steering of LLM with minimal parameter overhead. Experimental results demonstrate that \perfit delivers strong performance across six datasets while \cutting the number of parameters by an average of 92.3% compared to the state-of-the-art method.

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

### 13. Information Flow Reveals When to Trust Language Models

Flags: program_signal_low_public_attention, oral, taxonomy-review

- Subarea: General LLM training, evaluation, and alignment
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/60884
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: Diffusion / flow
- Evaluation settings: language/llm
- Result claim cues: negative / limitation
- Benchmarks: none
- Datasets: none
- Metrics: auroc

Abstract:

In retrieval-augmented generation, language models can generate incorrect responses if they fail to utilize query-relevant content from the retrieved evidence. This shifts the focus of uncertainty quantification (UQ) toward assessing contextual grounding, i.e., whether predictions are supported by query-relevant tokens. Recent UQ methods unpack language models to characterize how inputs are processed. Nevertheless, these methods focus on a few layers and overlook the whole progressive propagation within the model, thereby failing to fully capture the grounding dynamics essential for reliable uncertainty estimation. We use information flow to build a layer-wise trace that reveals each context token’s contribution to the output, providing an interpretable basis for assessing reliability. From this analysis, we introduce two measures to calibrate prediction confidence. The first, \textit{simulatability}, posits that a prediction is more likely to be correct when context token contributions align closely with their true relevance. The second, \textit{concentration}, asserts that a response is more likely to be correct when it is derived from a narrow, focused subset of tokens. Experiments show that our method achieves an average AUROC of 0.70, exceeding the runner-up performance of 0.65, while maintaining moderate computational cost.

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

### 14. On the Limits of LLM Adaptability: Impact of LLM Pre-Training on Annotation Task Performance

Flags: program_signal_low_public_attention, oral, taxonomy-review

- Subarea: General LLM training, evaluation, and alignment
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/61615
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Method / algorithm
- Method families: LLM post-training
- Evaluation settings: language/llm
- Result claim cues: negative / limitation
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Pre-trained Large Language Models (LLMs) are increasingly used for zero-shot annotation and LLM-as-a-judge tasks, yet their reliability hinges on how pre-trained priors interact with user-provided instructions. We investigate three dimensions of this interaction: (1) how an LLM’s familiarity with data and task definitions affects performance, (2) the extent to which additional information in prompts can correct zero-shot errors (“decision stickiness”), and (3) model susceptibility to misaligned task definitions. Through experiments on toxicity detection across diverse datasets (spanning social media, gaming, news, and forums) using both dense and mixture-of-experts models, we find that nearly two-thirds of zero-shot errors are resistant to correction, with an overall rescue rate (fraction of initial errors corrected by prompting) of only 36.4%. High-confidence errors prove especially resistant to correction. When given misaligned definitions, LLMs follow them while maintaining confidence levels unchanged from the aligned condition. Crucially, we introduce Definition-Specific Familiarity (DSF), a metric measuring alignment between a model’s internal concept and the task definition. After controlling for dataset-level confounds, DSF shows positive association with model performance (partial r = +0.34), while text memorization as measured by ROUGE-L shows no positive association (partial r = −0.19). Overall, these findings suggest clear limits on prompt-based correction in annotation tasks and underscore the importance of definition alignment over text-level memorization.

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

### 15. Latent Collaboration in Multi-Agent Systems

Flags: taxonomy_boundary_cluster, taxonomy-review, github

- Subarea: Reasoning models and chain-of-thought behavior
- Votes: 402
- ICML URL: https://icml.cc/virtual/2026/poster/61180
- AlphaXiv URL: https://www.alphaxiv.org/abs/2511.20639
- GitHub URL: https://github.com/Gen-Verse/LatentMAS
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Theory / proof; System / infrastructure; Application / domain study; Method / algorithm
- Method families: Reasoning / test-time compute; Agents / tool use
- Evaluation settings: math/code/verifiable; language/llm; theory/synthetic
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: accuracy; memory

Abstract:

Multi-agent systems (MAS) extend large language models (LLMs) from independent single-model reasoning to coordinative system-level intelligence. While existing LLM agents depend on text-based mediation for reasoning and communication, we take a step forward by enabling models to collaborate directly within the continuous latent space. We introduce LatentMAS, an end-to-end training-free framework that enables pure latent collaboration among LLM agents. In LatentMAS, each agent first performs auto-regressive latent thoughts generation through last-layer hidden embeddings instead of text. Then, a shared latent working memory preserves and transfers each agent's internal representations and latent thoughts, ensuring lossless information exchange without re-encoding. We provide detailed theoretical analyses showing that LatentMAS achieves higher expressiveness and lossless information preservation with lower overall complexity than standard text-based MAS. In addition, empirical evaluations across 9 comprehensive benchmarks spanning math and science reasoning, commonsense understanding, and code generation show that LatentMAS outperforms advanced single agents and text-based MAS baselines, achieving up to 14.6\% higher accuracy, reducing output token usage by 70.8\%-83.7\%, and providing 4$\times$-4.3$\times$ faster end-to-end inference. These results demonstrate that our new latent collaboration framework enhances system-level reasoning quality while providing consistent efficiency gains.

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

### 16. Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models

Flags: taxonomy_boundary_cluster, taxonomy-review, github

- Subarea: Reasoning models and chain-of-thought behavior
- Votes: 351
- ICML URL: https://icml.cc/virtual/2026/poster/64784
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.18734
- GitHub URL: https://github.com/siyan-zhao/OPSD
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; Method / algorithm
- Method families: RL / policy optimization; Reasoning / test-time compute
- Evaluation settings: language/llm
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Knowledge distillation improves large language model (LLM) reasoning by compressing the knowledge of a teacher LLM to train smaller LLMs. On-policy distillation advances this approach by having the student sample its own trajectories while a teacher LLM provides dense token-level supervision, addressing the distribution mismatch between training and inference in off-policy distillation methods. However, on-policy distillation typically requires a separate, often larger, teacher LLM and does not explicitly leverage ground-truth solutions available in reasoning datasets. Inspired by the intuition that a sufficiently capable LLM can rationalize external privileged reasoning traces and teach its weaker self (i.e., the version without access to privileged information), we introduce On-Policy Self-Distillation (OPSD), a framework where a single model acts as both teacher and student by conditioning on different contexts. The teacher policy conditions on privileged information (e.g., verified reasoning traces) while the student policy sees only the question; training minimizes the per-token divergence between these distributions over the student's own rollouts. We demonstrate the efficacy of our method on multiple mathematical reasoning benchmarks, achieving 4-8× token efficiency compared to reinforcement learning methods such as GRPO and superior performance over off-policy distillation methods.

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
