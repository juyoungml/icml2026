# C06: External trend context

Review question: Do fast arXiv-growth areas map to actual ICML 2026 paper themes, or only to broad query terms?

## Queue Summary

- Papers: 16
- Selection mix: fast_arxiv_area_sample=16
- Oral/award papers: 0
- Taxonomy-review papers: 6
- GitHub-linked papers: 14

## Papers

### 1. A Very Big Video Reasoning Suite

Flags: fast_arxiv_area_sample, github

- Review focus: Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Area/subarea: Multimodal, Vision, and Perception / Vision-language reasoning and video understanding
- Cluster: 22 - visual / vision / reasoning / video
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=159; 7d visits=25
- Artifact: https://github.com/Video-Reason/VBVR-Wan2.2; stars=25; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=Reasoning / test-time compute; Agents / tool use; Causal / data-centric; eval=math/code/verifiable; vision/video; language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/65709
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.20159

Abstract:

Video reasoning grounds intelligence in spatiotemporally consistent visual environments that go beyond what text can naturally capture, enabling intuitive reasoning over motion, interaction, and causality. Rapid progress in video models has focused primarily on visual quality. Systematically studying video reasoning and its scaling behavior suffers from a lack of video reasoning (training) data. To address this gap, we introduce the Very Big Video Reasoning (VBVR) Dataset, an unprecedentedly large-scale resource spanning 200 curated reasoning tasks and over one million video clips—approximately three orders of magnitude larger than existing datasets. We further present VBVR-Bench, a verifiable evaluation framework that moves beyond model-based judging by incorporating rule-based, human-aligned scorers, enabling reproducible and interpretable diagnosis of video reasoning capabilities. Leveraging the VBVR suite, we conduct one of the first large-scale scaling studies of video reasoning and observe early signs of emergent generalization to unseen reasoning tasks. Together, VBVR lays a foundation for the next stage of research in generalizable video reasoning. The data, toolkit, and models will be released publicly.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 2. Causal-JEPA: Learning World Models through Object-Level Latent Interventions

Flags: fast_arxiv_area_sample, github

- Review focus: Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Area/subarea: Multimodal, Vision, and Perception / Vision-language reasoning and video understanding
- Cluster: 22 - visual / vision / reasoning / video
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=150; 7d visits=99
- Artifact: https://github.com/galilai-group/cjepa; stars=206; manual-check=none
- Evidence tags: contribution=Method / algorithm; methods=Reasoning / test-time compute; Agents / tool use; Causal / data-centric; eval=math/code/verifiable; vision/video; robotics/embodied; security/safety
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/63623
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.11389

Abstract:

World models require robust relational understanding to support prediction, reasoning, and control. While object-centric representations provide a useful abstraction, they are not sufficient to capture interaction-dependent dynamics. We therefore propose C-JEPA, a simple and flexible object-centric world model that extends masked joint embedding prediction from image patches to object-centric representations. By applying object-level masking that requires an object’s state to be inferred from other objects, C-JEPA induces latent interventions with counterfactual-like effects and prevents shortcut solutions, making interaction reasoning essential. Empirically, C-JEPA leads to consistent gains in visual question answering, with an absolute improvement of about 20\% in counterfactual reasoning over the same architecture without object-level masking. On agent control tasks, C-JEPA enables substantially more efficient planning by using only 1\% of the total latent input features required by patch-based world models, while achieving comparable performance. Finally, we provide a formal analysis demonstrating that object-level masking induces a causal inductive bias via latent interventions. Code will be available at *anonymous*.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 3. ExSkill: Continual Learning from Experience and Skills in Multimodal Agents

Flags: fast_arxiv_area_sample, github

- Review focus: Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Area/subarea: Multimodal, Vision, and Perception / Multimodal representation and cross-modal alignment
- Cluster: 0 - multimodal / visual / modal / modality
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=147; 7d visits=62
- Artifact: https://github.com/XSkill-Agent/XSkill; stars=234; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=Reasoning / test-time compute; Agents / tool use; eval=robotics/embodied
- Benchmark/data/metric cues: none / none / accuracy
- ICML URL: https://icml.cc/virtual/2026/poster/65729
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.12056

Abstract:

Multimodal agents demonstrate impressive problem-solving capabilities but typically operate in isolated episodes without leveraging past experiences. Recent methods address this through dynamic retrieval of textual insights or predefined skill documents, yet face critical challenges: visual modalities are neglected during knowledge extraction, stored insights lack executable structure, and manually crafted skills fail to scale. We propose \textsc{ExSkill}, a framework combining task-level Skills (structured workflows and tool templates) with action-level Experiences (context-specific tactical insights) through automated accumulation from agent trajectories. Our approach employs visually-grounded summarization to extract knowledge integrating visual observations and textual reasoning, hierarchical consolidation to maintain quality and diversity, and context-aware adaptation to tailor knowledge to current visual contexts. Evaluated on five diverse benchmarks spanning visual tool use and multimodal search, \textsc{ExSkill} achieves average gains of 4.1-6.5 points over strong baselines across different backbone models, with superior zero-shot transferability and strategic improvements in tool selection and execution accuracy. These results demonstrate that our framework enables transferable continual learning for multimodal agents in real-world scenarios without parametric training, offering broad applicability for practical deployment.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 4. BabyVision: Visual Reasoning Beyond Language

Flags: fast_arxiv_area_sample, github

- Review focus: Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Area/subarea: Multimodal, Vision, and Perception / Vision-language reasoning and video understanding
- Cluster: 22 - visual / vision / reasoning / video
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=134; 7d visits=35
- Artifact: https://github.com/UniPat-AI/BabyVision; stars=227; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=Reasoning / test-time compute; Agents / tool use; eval=math/code/verifiable; language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/63195
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.06521

Abstract:

While humans develop core visual skills long before acquiring language, contemporary Multimodal LLMs (MLLMs) still rely heavily on linguistic priors to compensate for their fragile visual understanding. We uncovered a crucial fact: state-of-the-art MLLMs consistently fail on basic visual tasks that humans, even 3-year-olds, can solve effortlessly. To systematically investigate this gap, we introduce BabyVision, a benchmark designed to assess core visual abilities independent of linguistic knowledge for MLLMs. BabyVision spans a wide range of tasks, with 388 items divided into 22 subclasses across four key categories. Empirical results and human evaluation reveal that leading MLLMs perform significantly below human baselines. Gemini3-Pro-Preview scores 49.7, lagging behind 6-year-old humans and falling well behind the average adult score of 94.1. These results show despite excelling in knowledge-heavy evaluations, current MLLMs still lack fundamental visual primitives. Progress in BabyVision represents a step toward human-level visual perception and reasoning capabilities. We also explore solving visual reasoning with generation models by proposing Babyvision-Gen and automatic evaluation toolkit. Our code and benchmark data are released at https://anonymous.4open.science/r/BabyVision-E88F/ for reproduction.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 5. Process Reward Models That Think

Flags: fast_arxiv_area_sample, github

- Review focus: Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
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

### 6. Reinforcement Learning via Self-Distillation

Flags: fast_arxiv_area_sample, taxonomy-review, github

- Review focus: Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
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

### 7. Agent Learning via Early Experience

Flags: fast_arxiv_area_sample, taxonomy-review, github

- Review focus: Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
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

### 8. GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization

Flags: fast_arxiv_area_sample, taxonomy-review, github

- Review focus: Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
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

### 9. Chain-of-Thought Reasoning In The Wild Is Not Always Faithful

Flags: fast_arxiv_area_sample, github

- Review focus: Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Area/subarea: Safety, Governance, Privacy, and Society / Position papers, policy, and social impacts
- Cluster: 37 - ai / position / social / position paper
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=253; 7d visits=32
- Artifact: https://github.com/jettjaniak/chainscope; stars=35; manual-check=none
- Evidence tags: contribution=Dataset / data resource; methods=Reasoning / test-time compute; Agents / tool use; eval=math/code/verifiable; security/safety
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/64450
- AlphaXiv URL: https://www.alphaxiv.org/abs/2503.08679

Abstract:

Recent studies indicate that when faced with explicit biases in prompts, models often omit mentioning these biases in their Chain-of-Thought (CoT) output, revealing that verbalized reasoning can give an incorrect picture of how models arrive at conclusions (unfaithfulness). In this work, we show that unfaithful CoT also occurs on naturally worded, non-adversarial prompts without adding artificial biases or editing model outputs. We find that when separately presented with the questions "Is X bigger than Y?" and "Is Y bigger than X?", models sometimes produce superficially coherent arguments to justify systematically answering Yes to both questions or No to both questions, despite such responses being logically contradictory. We present preliminary evidence that this is due to models' implicit biases towards Yes or No, labeling this *Implicit Post-Hoc Rationalization*. Our results reveal rates up to 13% for production models, and while frontier models are more faithful, none are entirely so, including thinking models like DeepSeek R1 (0.37%) and Sonnet 3.7 with thinking (0.04%). We also investigate *Unfaithful Illogical Shortcuts*, where models use subtly illogical reasoning to make speculative answers to hard math problems seem rigorously proven. Our findings indicate that while CoT can be useful for assessing outputs, it is not a complete account of a model's internal reasoning and should be used with caution in agentic or safety-critical settings.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 10. The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models

Flags: fast_arxiv_area_sample

- Review focus: Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Area/subarea: Safety, Governance, Privacy, and Society / Adversarial safety, attacks, and security
- Cluster: 12 - safety / attacks / attack / social aspects
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=127; 7d visits=78
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Method / algorithm; methods=LLM post-training; eval=language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/61446
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.10387

Abstract:

Large language models can represent a variety of personas but typically default to a helpful Assistant identity cultivated during post-training. Across several different models, we find an “Assistant Axis" in their activation space, which captures the extent to which a model is operating in its default Assistant mode. Steering towards the Assistant direction reinforces helpful and harmless behavior; steering away increases the model’s tendency to identify as other entities. Measuring deviations along the Assistant Axis predicts “persona drift,” a phenomenon where models slip into exhibiting harmful or bizarre behaviors that are uncharacteristic of their typical persona. We find that persona drift is often driven by conversations demanding meta-reflection on the model’s processes or featuring emotionally vulnerable users. We show that restricting activations to a fixed region along the Assistant Axis can stabilize model behavior in these scenarios—and also in the face of adversarial persona-based jailbreaks. Our results suggest that post-training steers models toward a particular region of persona space but only loosely tethers them to it, motivating work on training and steering strategies that more deeply anchor models to a coherent persona.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 11. Reasoning Models Struggle to Control their Chains of Thought

Flags: fast_arxiv_area_sample, github

- Review focus: Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Area/subarea: Safety, Governance, Privacy, and Society / Position papers, policy, and social impacts
- Cluster: 37 - ai / position / social / position paper
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=75; 7d visits=23
- Artifact: https://github.com/YuehHanChen/CoTControl; stars=50; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=RL / policy optimization; Reasoning / test-time compute; eval=robotics/embodied; language/llm; security/safety
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/66446
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.05706

Abstract:

Instruction following in LLMs captures models' ability to change their visible behaviors as requested by users. Instead, we study models' ability to control their chain-of-thought (CoT). This capability -- CoT controllability -- is undesirable because it could allow models to suppress signs of misbehavior in their CoT, thereby undermining our ability to monitor them. To measure this, we introduce the \emph{CoT-Control} evaluation suite. We show that reasoning models are less able to follow instructions in their CoT than in their outputs: on instructions like reasoning about a genetics problem without mentioning the word ``chromosome", Claude-Sonnet-4.5 complies only 5\% of the time. We also find that CoT controllability is higher for larger models and decreases with more RL training, test-time compute, and increased problem difficulty. CoT controllability failures extend even to situations in which models are given incentives (as opposed to direct requests) to evade CoT monitors, although models that are told they're being monitored exhibit slightly higher controllability. Similarly, eliciting controllability by adversarially optimizing prompts doesn’t meaningfully increase controllability. Our results leave us cautiously optimistic: reasoning models generally seem characterized by low CoT controllability. However, the mechanism behind this phenomenon is not well understood. Given its importance for maintaining CoT monitorability, we recommend that frontier labs keep tracking controllability for future models.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 12. Towards a Science of AI Agent Reliability

Flags: fast_arxiv_area_sample

- Review focus: Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Area/subarea: Safety, Governance, Privacy, and Society / Position papers, policy, and social impacts
- Cluster: 37 - ai / position / social / position paper
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=72; 7d visits=16
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=Reasoning / test-time compute; Agents / tool use; eval=security/safety
- Benchmark/data/metric cues: none / none / accuracy
- ICML URL: https://icml.cc/virtual/2026/poster/66364
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.16666

Abstract:

AI agents are increasingly deployed for consequential tasks. Yet existing benchmarks evaluate only task success rates, ignoring whether agents behave consistently, remain robust to perturbations, fail predictably, or bound error severity. We propose a framework for measuring agent reliability grounded in safety-critical engineering practice, decomposing reliability into four dimensions: consistency, robustness, predictability, and safety. Applying these metrics to 12 frontier models across two complementary benchmarks, we find that recent capability gains have produced minimal improvement in reliability: agents remain inconsistent across runs, brittle to prompt rephrasings, and poorly calibrated in their self-assessments, even as accuracy improves. Our metrics complement accuracy-focused evaluation by offering tools for reasoning about how agents perform, degrade, and fail under uncertainty.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 13. mHC: Manifold-Constrained Hyper-Connections

Flags: fast_arxiv_area_sample, taxonomy-review, github

- Review focus: Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
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

### 14. xKV: Cross-Layer KV-Cache Compression via Aligned Singular Vector Extraction

Flags: fast_arxiv_area_sample, github

- Review focus: Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Area/subarea: Systems and Efficient Foundation Models / Long-context attention and KV-cache compression
- Cluster: 3 - attention / kv / context / cache
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=518; 7d visits=48
- Artifact: https://github.com/abdelfattah-lab/xKV; stars=52; manual-check=none
- Evidence tags: contribution=System / infrastructure; methods=LLM post-training; Agents / tool use; Transformer / attention; Compression / efficiency; eval=math/code/verifiable; language/llm
- Benchmark/data/metric cues: none / none / accuracy; latency; throughput; memory
- ICML URL: https://icml.cc/virtual/2026/poster/63436
- AlphaXiv URL: https://www.alphaxiv.org/abs/2503.18893

Abstract:

Long-context Large Language Models (LLMs) enable powerful applications but incur high memory costs due to the key–value states (KV-Cache). Recent studies attempt to share KV-Cache across layers, but these approaches either require expensive pretraining or rely on per-token cross-layer cosine similarity that is often limited in practice. We show, via Centered Kernel Alignment (CKA), that the dominant singular vectors of KV-Cache are well aligned across layers. Motivated by this observation, we propose xKV, a post-training compression method that jointly factorizes grouped-layer KV-Cache into a shared low-rank subspace, substantially reducing KV-Cache memory. Across widely used LLMs, xKV achieves up to 8× KV-Cache compression while preserving accuracy on long-context tasks and in multi-turn settings. To further improve efficiency, we introduce Selective Reconstruction (SR) at decode time. Combined with SR, xKV achieves up to 4.23× end-to-end speedup, surpassing notable baselines with 30% higher throughput under a similar accuracy level. Overall, xKV provides a plug-and-play approach to reduce both memory and latency for long-context LLM inference. Our code will be open-sourced.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 15. Evolution Strategies at the Hyperscale

Flags: fast_arxiv_area_sample, taxonomy-review, github

- Review focus: Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Area/subarea: Systems and Efficient Foundation Models / Large-scale training, optimizers, and model architecture
- Cluster: 26 - networks / training / deep / gradient
- Cluster review: needs_review; manual confidence not high; split across lexical clusters
- Program/public: oral=false; award=none; votes=405; 7d visits=116
- Artifact: https://github.com/ESHyperscale/HyperscaleES; stars=346; manual-check=none
- Evidence tags: contribution=System / infrastructure; methods=RL / policy optimization; LLM post-training; Reasoning / test-time compute; eval=language/llm; theory/synthetic
- Benchmark/data/metric cues: none / none / throughput
- ICML URL: https://icml.cc/virtual/2026/poster/62943
- AlphaXiv URL: https://www.alphaxiv.org/abs/2511.16652

Abstract:

Evolution Strategies (ES) is a class of powerful black-box optimisation methods that are highly parallelisable and can handle non-differentiable and noisy objectives. However, naïve ES becomes prohibitively expensive at scale on GPUs due to the low arithmetic intensity of batched matrix multiplications with unstructured random perturbations. We introduce Evolution Guided GeneRal Optimisation via Low-rank Learning (EGGROLL), which improves arithmetic intensity by structuring individual perturbations as rank-$r$ matrices, resulting in a hundredfold increase in training speed for billion-parameter models at large population sizes, achieving up to 91\% of the throughput of pure batch inference. We provide a rigorous theoretical analysis of ES for high-dimensional parameter objectives, investigating conditions needed for ES updates to converge in high dimensions, revealing a linearising effect, and proving consistency between EGGROLL and ES as parameter dimension increases. Our experiments show that EGGROLL: (1) enables the stable pretraining of nonlinear recurrent language models that operate purely in integer datatypes, (2) is competitive with GRPO for post-training LLMs on reasoning tasks, and (3) does not compromise performance compared to ES in tabula rasa RL settings, despite being faster.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 16. Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights

Flags: fast_arxiv_area_sample, taxonomy-review, github

- Review focus: Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Area/subarea: Systems and Efficient Foundation Models / Large-scale training, optimizers, and model architecture
- Cluster: 26 - networks / training / deep / gradient
- Cluster review: needs_review; manual confidence not high; split across lexical clusters
- Program/public: oral=false; award=none; votes=365; 7d visits=133
- Artifact: https://github.com/sunrainyg/RandOpt; stars=627; manual-check=none
- Evidence tags: contribution=Position / conceptual; methods=RL / policy optimization; LLM post-training; eval=none
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/65901
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.12228

Abstract:

Pretraining produces a learned parameter vector that is typically treated as a starting point for further iterative adaptation. In this work, we instead view the outcome of pretraining as a distribution over parameter vectors, whose support already contains task-specific experts. We show that in smaller or insufficiently trained models such expert solutions occupy a negligible fraction of the volume of this distribution, making their discovery reliant on structured optimization methods such as gradient descent. In contrast, in large, well-pretrained models the density of task-experts increases dramatically, so that diverse specialists populate a substantial fraction of the neighborhood around the pretrained weights. Motivated by this perspective, we explore a simple, fully parallel post-training method that samples $N$ parameter vectors at random, selects the top $K$, and ensembles them via majority vote to combine complementary expertise. Despite its simplicity, this approach is competitive with standard post-training methods such as PPO, GRPO, and ES for contemporary large-scale models.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:
