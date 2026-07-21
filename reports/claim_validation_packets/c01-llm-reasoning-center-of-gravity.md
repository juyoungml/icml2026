# C01: LLM reasoning center of gravity

Review question: Are the LLM reasoning/post-training papers genuinely central, or are boundary clusters inflating the area?

## Queue Summary

- Papers: 14
- Selection mix: llm_boundary_cluster=8, llm_high_attention_core=6
- Oral/award papers: 8
- Taxonomy-review papers: 12
- GitHub-linked papers: 11

## Papers

### 1. How much can language models memorize?

Flags: llm_boundary_cluster, oral, Outstanding Paper Honorable Mention, taxonomy-review, github

- Review focus: Check whether this is genuinely LLM reasoning/post-training or a broader LLM/system/safety paper.
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

### 2. The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models

Flags: llm_boundary_cluster, oral, Outstanding Paper Award, taxonomy-review, github

- Review focus: Check whether this is genuinely LLM reasoning/post-training or a broader LLM/system/safety paper.
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

### 3. Maximum Likelihood Reinforcement Learning

Flags: llm_boundary_cluster, oral, taxonomy-review, github

- Review focus: Check whether this is genuinely LLM reasoning/post-training or a broader LLM/system/safety paper.
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

### 4. Reinforcement Learning with Evolving Rubrics for Deep Research

Flags: llm_boundary_cluster, oral, taxonomy-review, github

- Review focus: Check whether this is genuinely LLM reasoning/post-training or a broader LLM/system/safety paper.
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

### 5. Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers

Flags: llm_boundary_cluster, oral, taxonomy-review

- Review focus: Check whether this is genuinely LLM reasoning/post-training or a broader LLM/system/safety paper.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / General LLM training, evaluation, and alignment
- Cluster: 24 - language / language models / llms / large language
- Cluster review: needs_review; manual confidence not high; split across lexical clusters
- Program/public: oral=true; award=none; votes=75; 7d visits=49
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Position / conceptual; methods=LLM post-training; eval=language/llm
- Benchmark/data/metric cues: LatentQA; LatentQA-trained / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/65446
- AlphaXiv URL: https://www.alphaxiv.org/abs/2512.15674

Abstract:

Large language model (LLM) activations are notoriously difficult to understand, with most existing techniques using complex, specialized methods for interpreting them. Recent work has proposed a simpler approach known as LatentQA: training LLMs to directly accept LLM activations as inputs and answer arbitrary questions about them in natural language. However, prior work has focused on narrow task settings for both training and evaluation. In this paper, we instead take a generalist perspective. We evaluate LatentQA-trained models, which we call Activation Oracles (AOs), in far out-of-distribution settings and examine how performance scales with training data diversity. We find that AOs can recover information fine-tuned into a model (e.g., biographical knowledge or malign propensities) that does not appear in the input text, despite never being trained with activations from a fine-tuned model. Our main evaluations are four downstream tasks where we can compare to prior white- and black-box techniques. We find that even narrowly-trained LatentQA models can generalize well, and that adding additional training datasets (such as classification tasks and a self-supervised context prediction task) yields consistent further improvements. Our best AOs match or exceed white-box baselines on all four tasks and the best overall baseline on 3 of 4. These results suggest that diversified training to answer natural-language queries imparts a general capability to verbalize information about LLM activations.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 6. WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference

Flags: llm_boundary_cluster, oral, taxonomy-review, github

- Review focus: Check whether this is genuinely LLM reasoning/post-training or a broader LLM/system/safety paper.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / Diffusion language models and decoding
- Cluster: 14 - decoding / diffusion / language / language models
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=true; award=none; votes=60; 7d visits=17
- Artifact: https://github.com/Tencent/WeDLM; stars=644; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=Reasoning / test-time compute; Diffusion / flow; Transformer / attention; Causal / data-centric; eval=language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/64095
- AlphaXiv URL: https://www.alphaxiv.org/abs/2512.22737

Abstract:

Autoregressive (AR) generation is the standard decoding paradigm for Large Language Models (LLMs), but its token-by-token nature limits parallelism at inference time. Diffusion Language Models (DLLMs) offer parallel decoding by recovering multiple masked tokens per step; however, in practice they often fail to translate this parallelism into speed gains over optimized AR engines (e.g., vLLM). A key reason is that many DLLMs rely on bidirectional attention, which breaks standard prefix KV caching. We propose WeDLM, a diffusion decoding framework built entirely on standard causal attention to make parallel generation prefix-cache friendly. The core idea is to let each masked position condition on all observed tokens while keeping a causal mask, achieved by Topological Reordering that moves observed tokens to the physical prefix while preserving their logical positions. Building on this, we introduce a streaming decoding procedure that continuously commits confident tokens into a growing left-to-right prefix, avoiding the stop-and-wait behavior common in block diffusion methods. Experiments show that WeDLM preserves the quality of strong AR backbones while delivering substantial speedups, approaching 3× on challenging reasoning benchmarks and up to 10× in low-entropy generation regimes; critically, our comparisons are against AR baselines served by vLLM under matched deployment settings.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 7. OPUS: Towards Efficient and Principled Data Selection in Large Language Model Pre-training in Every Iteration

Flags: llm_boundary_cluster, oral, taxonomy-review

- Review focus: Check whether this is genuinely LLM reasoning/post-training or a broader LLM/system/safety paper.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / Diffusion language models and decoding
- Cluster: 14 - decoding / diffusion / language / language models
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=true; award=none; votes=57; 7d visits=73
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Method / algorithm; methods=Diffusion / flow; Causal / data-centric; eval=language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/61926
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.05400

Abstract:

As high-quality public text approaches exhaustion, a phenomenon known as the Data Wall—LLM pre-training is shifting from more tokens to better tokens. However, existing methods either rely on heuristic static filters that ignore training dynamics, or use dynamic yet optimizer-agnostic criteria based on raw gradients. We propose OPUS (Optimizer-induced Projected Utility Selection), a dynamic framework that defines utility in the optimizer-induced update space. OPUS scores candidates by projecting their effective updates, shaped by modern optimizers, onto a target direction derived from a stable, in-distribution proxy. To ensure scalability, we employ Ghost technique with CountSketch for computational efficiency, and Boltzmann sampling for data diversity, incurring only 4.7% additional compute overhead. OPUS achieves remarkable results across diverse corpora, quality tiers, optimizers, and model scales. In pre-training of GPT-2 Large/XL on FineWeb and FineWeb-Edu with 30B tokens, OPUS outperforms industrial-level baselines and even full 200B-token training. Moreover, when combined with industrial-level static filters, OPUS further improves pre-training efficiency, even with lower-quality data. Furthermore, in continued pre-training of Qwen3-8B-Base on SciencePedia, OPUS achieves superior performance using only 0.5B tokens compared to full training with 3B tokens, demonstrating significant data efficiency gains in specialized domains.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 8. Learning to Theorize the World from Observation

Flags: llm_boundary_cluster, oral, taxonomy-review

- Review focus: Check whether this is genuinely LLM reasoning/post-training or a broader LLM/system/safety paper.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / Reasoning models and chain-of-thought behavior
- Cluster: 11 - reasoning / language / large language / language models
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=true; award=none; votes=56; 7d visits=94
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=System / infrastructure; methods=none; eval=math/code/verifiable; vision/video; language/llm; theory/synthetic
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/60765
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.03413

Abstract:

What does it mean to understand the world? Is it simply to predict future video frames? Developmental cognitive science suggests that understanding the world is fundamentally the process of constructing internal theories of how it works rather than mere prediction, even before language is acquired. However, in machine learning, it remains unclear how to endow AI systems with such theory-building capability from raw, non-textual observation alone. In this paper, we introduce Learning-to-Theorize (L2T), a learning paradigm in which an AI system acquires the ability to construct theories represented as executable programs directly from observation alone. To instantiate this paradigm, we propose the Neural Language-of-Thought Programmer, a neural model that induces and executes latent programs as explanations rather than task-specific predictors or policies. In experiments, we show that this formulation enables explanation-driven generalization, allowing observations to be understood in terms of the programs that generate them.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 9. Process Reward Models That Think

Flags: llm_high_attention_core, github

- Review focus: Check whether high attention supports the center-of-gravity claim.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / RL for reasoning models and verifiable rewards
- Cluster: 35 - reasoning / rl / reinforcement / reinforcement learning
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=1815; 7d visits=361
- Artifact: https://github.com/mukhal/thinkprm; stars=89; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=RL / policy optimization; LLM post-training; Reasoning / test-time compute; eval=math/code/verifiable; language/llm
- Benchmark/data/metric cues: ProcessBench; GPQA-Diamond; LiveCodeBench / none / reward
- ICML URL: https://icml.cc/virtual/2026/poster/68817
- AlphaXiv URL: https://www.alphaxiv.org/abs/2504.16828

Abstract:

Step-by-step verifiers—also known as process reward models (PRMs)—are a key ingredient for test-time scaling, but training them requires expensive step-level supervision. This work aims to build data-efficient PRMs as verbalized step-wise reward models that verify every step in the solution by generating a verification chain-of-thought (CoT). We propose ThinkPRM, a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. Our approach capitalizes on the inherent reasoning abilities of long CoT models, and outperforms LLM-as-a-Judge and discriminative verifiers—using only 1% of the process labels in PRM800K—across several challenging benchmarks. Specifically, ThinkPRM beats the baselines on ProcessBench, MATH-500, and AIME ’24 under best-of-N selection and reward-guided search. In an out-of-domain evaluation over subsets of GPQA-Diamond and LiveCodeBench, our PRM surpasses discriminative verifiers trained with the full PRM800K by 8% and 4.5%, respectively. Lastly, under the same token budget, ThinkPRM scales up verification compute more effectively compared to LLM-as-a-Judge, outperforming it by 7.2% on a subset of ProcessBench. This work highlights the value of generative, long CoT PRMs that can scale test-time compute for verification while requiring minimal supervision for training.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 10. Reinforcement Learning via Self-Distillation

Flags: llm_high_attention_core, taxonomy-review, github

- Review focus: Check whether high attention supports the center-of-gravity claim.
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

### 11. Agent Learning via Early Experience

Flags: llm_high_attention_core, taxonomy-review, github

- Review focus: Check whether high attention supports the center-of-gravity claim.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Cluster: 2 - reward / reinforcement learning / reinforcement / rewards
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=false; award=none; votes=532; 7d visits=122
- Artifact: https://github.com/jettbrains/-L-; stars=148; manual-check=none
- Evidence tags: contribution=Method / algorithm; methods=RL / policy optimization; LLM post-training; Reasoning / test-time compute; Agents / tool use; eval=math/code/verifiable; language/llm
- Benchmark/data/metric cues: none / none / reward
- ICML URL: https://icml.cc/virtual/2026/poster/64488
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.08558

Abstract:

A long-term goal of language agents is to learn and improve through their own experience, ultimately outperforming humans in complex, real-world tasks. However, training agents from experience data with reinforcement learning remains difficult in many environments, which either lack verifiable rewards (e.g., websites) or require inefficient long-horizon rollouts (e.g., multi-turn tool use). As a result, most current agents rely on supervised fine-tuning on expert data, which is challenging to scale and generalizes poorly. This limitation stems from the nature of expert demonstrations: they capture only a narrow range of scenarios, and expose the agent to limited environment diversity. We address this limitation with a middle-ground paradigm we call *early experience*: interaction data generated by the agent's own actions, where the resulting future states serve as supervision without reward signals. Within this paradigm, we study two strategies of using such data: (1) implicit world modeling, which uses collected states to ground the policy in environment dynamics; and (2) self-reflection, where the agent learns from its suboptimal actions to improve reasoning and decision-making. Evaluation across eight diverse environments and multiple model families shows that our approaches consistently improve effectiveness and out-of-domain generalization, highlighting the value of early experience. Moreover, in environments with verifiable rewards, our results provide promising signals that early experience offers a strong foundation for subsequent reinforcement learning, making it a practical bridge between imitation learning and fully experience-driven agents.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 12. GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization

Flags: llm_high_attention_core, taxonomy-review, github

- Review focus: Check whether high attention supports the center-of-gravity claim.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Cluster: 2 - reward / reinforcement learning / reinforcement / rewards
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=false; award=none; votes=507; 7d visits=79
- Artifact: https://github.com/NVlabs/GDPO; stars=489; manual-check=none
- Evidence tags: contribution=Theory / proof; methods=RL / policy optimization; LLM post-training; Reasoning / test-time compute; Agents / tool use; eval=math/code/verifiable; language/llm
- Benchmark/data/metric cues: none / none / accuracy; reward
- ICML URL: https://icml.cc/virtual/2026/poster/63333
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.05242

Abstract:

As language models become increasingly capable, users expect them to provide not only accurate responses but also behaviors aligned with diverse human preferences across a variety of scenarios. To achieve this, Reinforcement learning (RL) pipelines have begun incorporating multiple rewards, each capturing a distinct preference, to guide models toward these desired behaviors. However, recent work has defaulted to apply Group Relative Policy Optimization (GRPO) under multi-reward setting without examining its suitability. In this paper, we demonstrate that directly applying GRPO to normalize distinct rollout reward combinations causes them to collapse into identical advantage values, reducing the resolution of the training signal and resulting in suboptimal convergence and, in some cases, early training failure. We then introduce Group reward-Decoupled Normalization Policy Optimization (GDPO), a new policy optimization method to resolve these issues by decoupling the normalization of individual rewards, more faithfully preserving their relative differences and enabling more accurate multi-reward optimization, along with substantially improved training stability. We compare GDPO with GRPO across three tasks: tool calling, math reasoning, and coding reasoning, evaluating both correctness metrics (accuracy, bug ratio) and constraint adherence metrics (format, length). Across all settings, GDPO consistently outperforms GRPO, demonstrating its effectiveness and generalizability for multi-reward reinforcement learning optimization.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 13. On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language Models

Flags: llm_high_attention_core, github

- Review focus: Check whether high attention supports the center-of-gravity claim.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / RL for reasoning models and verifiable rewards
- Cluster: 35 - reasoning / rl / reinforcement / reinforcement learning
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=456; 7d visits=67
- Artifact: https://github.com/Interplay-LM-Reasoning/Interplay-LM-Reasoning; stars=160; manual-check=none
- Evidence tags: contribution=Theory / proof; methods=RL / policy optimization; LLM post-training; Reasoning / test-time compute; Causal / data-centric; eval=robotics/embodied; language/llm; theory/synthetic
- Benchmark/data/metric cues: none / none / reward
- ICML URL: https://icml.cc/virtual/2026/poster/63850
- AlphaXiv URL: https://www.alphaxiv.org/abs/2512.07783

Abstract:

Recent reinforcement learning (RL) techniques have yielded impressive reasoning improvements in language models, yet it remains unclear whether post-training truly extends a model’s reasoning ability beyond what it acquires during pre-training. A central challenge is the lack of control in modern training pipelines: large-scale pre-training corpora are opaque, mid-training is often underexamined, and RL objectives interact with unknown prior knowledge in complex ways. To resolve this ambiguity, we develop a fully controlled experimental framework that isolates the causal contributions of pre-training, mid-training, and RL-based post-training. Our approach employs synthetic reasoning tasks with explicit atomic operations, parseable step-by-step reasoning traces, and systematic manipulation of training distributions. We evaluate models along two axes: extrapolative generalization to more complex compositions and contextual generalization across surface contexts. Using this framework, we reconcile competing views on RL’s effectiveness. We show that: 1) RL produces true capability gains (pass@128) only when pre-training leaves sufficient headroom and when RL data target the model’s edge of competence, tasks at the boundary that are difficult but not yet out of reach. 2) Contextual generalization requires minimal yet sufficient pre-training exposure, after which RL can reliably transfer. 3) Mid-training significantly enhances performance under fixed compute compared with RL only, demonstrating its central but underexplored role in training pipelines. 4) Process-level rewards reduce reward hacking and improve reasoning fidelity. Together, these results clarify the interplay between pre-training, mid-training, and RL, offering a foundation for understanding and improving reasoning LM training strategies.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 14. Latent Collaboration in Multi-Agent Systems

Flags: llm_high_attention_core, taxonomy-review, github

- Review focus: Check whether high attention supports the center-of-gravity claim.
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
