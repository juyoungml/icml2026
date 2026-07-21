# C02: Infrastructure and agentic workloads

Review question: Do systems/efficiency and agents/code overweights reflect real ICML 2026 emphasis rather than classifier artifacts?

## Queue Summary

- Papers: 14
- Selection mix: systems_agents_program_signal=7, systems_agents_public_signal=7
- Oral/award papers: 7
- Taxonomy-review papers: 5
- GitHub-linked papers: 14

## Papers

### 1. Controlled LLM Training on Spectral Sphere

Flags: systems_agents_program_signal, oral, taxonomy-review, github

- Review focus: Check whether program-selected papers substantiate systems/agents emphasis.
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

### 2. Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning

Flags: systems_agents_program_signal, oral, github

- Review focus: Check whether program-selected papers substantiate systems/agents emphasis.
- Area/subarea: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Cluster: 40 - agents / agent / evaluation / agentic
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=89; 7d visits=40
- Artifact: https://github.com/aiming-lab/Agent0; stars=1228; manual-check=none
- Evidence tags: contribution=Dataset / data resource; methods=RL / policy optimization; Reasoning / test-time compute; Agents / tool use; Graphs / geometry; eval=vision/video; language/llm
- Benchmark/data/metric cues: none / none / reward
- ICML URL: https://icml.cc/virtual/2026/poster/63095
- AlphaXiv URL: https://www.alphaxiv.org/abs/2511.19900

Abstract:

Large Vision-Language Models (LVLMs) have achieved remarkable progress in multimodal reasoning tasks; however, their learning remains constrained by the limitations of human-annotated supervision. Recent self-rewarding approaches attempt to overcome this constraint by allowing models to act as their own critics or reward providers. Yet, purely text-based self-evaluation struggles to verify complex visual reasoning steps and often suffers from evaluation hallucinations. To address these challenges, inspired by recent advances in tool-integrated reasoning, we propose Agent0-VL, a self-evolving vision-language agent that achieves continual improvement with tool-integrated reasoning. Agent0-VL incorporates tool usage not only into reasoning but also into self-evaluation and self-repair, enabling the model to introspect, verify, and refine its reasoning through evidence-grounded analysis. It unifies two synergistic roles within a single LVLM: a Solver that performs multi-turn tool-integrated reasoning, and a Verifier that generates structured feedback and fine-grained self-rewards through tool-grounded critique. These roles interact through a Self-Evolving Reasoning Cycle, where tool-based verification and reinforcement learning jointly align the reasoning and evaluation distributions for stable self-improvement. Through this zero-external-reward evolution, Agent0-VL aligns its reasoning and verification behaviors without any human annotation or external reward models, achieving continual self-improvement. Experiments on chart reasoning, geometric problem solving, and visual scientific analysis show that Agent0-VL achieves an 12.5% improvement over the Qwen-VL base model.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 3. $\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment

Flags: systems_agents_program_signal, oral, github

- Review focus: Check whether program-selected papers substantiate systems/agents emphasis.
- Area/subarea: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Cluster: 40 - agents / agent / evaluation / agentic
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=89; 7d visits=91
- Artifact: https://github.com/sierra-research/tau2-bench; stars=1569; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=Reasoning / test-time compute; Agents / tool use; eval=math/code/verifiable; robotics/embodied; language/llm; theory/synthetic
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/64377
- AlphaXiv URL: https://www.alphaxiv.org/abs/2506.07982

Abstract:

Existing benchmarks for conversational AI agents simulate *single-control* environments, where only the AI agent can use tools to interact with the world, while the user remains a passive information provider. This differs from real-world scenarios like technical support, where users need to actively participate in modifying the state of the (shared) world. In order to address this gap, we introduce $\tau^2$-bench, with four key contributions: 1. A novel **Telecom dual-control domain** modeled as a Dec-POMDP, where both agent and user make use of tools to act in a shared, dynamic environment that tests both agent coordination and communication, 2. A **compositional task generator** that programmatically creates diverse, verifiable tasks from atomic components, ensuring domain coverage and controlled complexity, 3. A **reliable user simulator** tightly coupled with the environment, whose behavior is constrained by tools and observable states, improving simulation fidelity, 4. **fine-grained analysis of agent performance** through multiple ablations including separating errors arising from reasoning vs communication/coordination. In particular, our experiments show significant performance drops when agents shift from no-user to dual-control, highlighting the challenges of guiding users. Overall, $\tau^2$-bench provides a controlled testbed for agents that must both reason effectively and guide user actions.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 4. daVinci-Dev: Agent-native Mid-training for Software Engineering

Flags: systems_agents_program_signal, oral, github

- Review focus: Check whether program-selected papers substantiate systems/agents emphasis.
- Area/subarea: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Cluster: 40 - agents / agent / evaluation / agentic
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=52; 7d visits=48
- Artifact: https://github.com/sii-research/GAIR; stars=9; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=RL / policy optimization; LLM post-training; Reasoning / test-time compute; Agents / tool use; Diffusion / flow; eval=math/code/verifiable; language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/63099
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.18418

Abstract:

Recently, the frontier of Large Language Model (LLM) capabilities has shifted from single-turn code generation to agentic software engineering—a paradigm where models autonomously navigate, edit, and test complex repositories. While post-training methods have become the de facto approach for code agents, *agentic mid-training*—mid-training (MT) on large-scale data that mirrors authentic agentic workflows—remains critically underexplored due to substantial resource requirements, despite offering a more scalable path to instilling foundational agentic behaviors than relying solely on expensive reinforcement learning. A central challenge in realizing effective agentic mid-training is the distribution mismatch between static training data and the dynamic, feedback-rich environment of real development. To address this, we present a systematic study of agentic mid-training, establishing both the data synthesis principles and training methodology for effective agent development at scale. Central to our approach is *agent-native data*—supervision comprising two complementary types of trajectories: *contextually-native trajectories* that preserve the complete information flow an agent experiences, offering broad coverage and diversity; and *environmentally-native trajectories* collected from executable repositories where observations stem from actual tool invocations and test executions, providing depth and interaction authenticity. We verify the model’s agentic capabilities on `SWE-Bench Verified`. We demonstrate our superiority over the previous open software engineering mid-training recipe `Kimi-Dev` under two post-training settings with an aligned base model and agentic scaffold, while using less than half mid-training tokens (73.1B). Besides relative advantage, our best performing 32B and 72B models achieve **56.1%** and **58.5%** resolution rates, respectively, which are state-of-the-art among open training recipes using agentic scaffolds under their model sizes, despite starting from non-coder `Qwen2.5-Base` base models. Beyond these agentic capabilities, we also observe performance gains on general code generation and scientific benchmarks. We plan to open-source a significant portion of our datasets, recipes, and model checkpoints—resources representing substantial computational investment typically unavailable to the broader community—to facilitate further research in this underexplored paradigm.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 5. Monitoring Monitorability

Flags: systems_agents_program_signal, oral, github

- Review focus: Check whether program-selected papers substantiate systems/agents emphasis.
- Area/subarea: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Cluster: 40 - agents / agent / evaluation / agentic
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=28; 7d visits=17
- Artifact: https://github.com/nightscout/cgm-remote-monitor; stars=2786; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=Reasoning / test-time compute; Agents / tool use; eval=robotics/embodied
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/62992
- AlphaXiv URL: https://www.alphaxiv.org/abs/2512.18311

Abstract:

Safe deployment of increasingly capable AI agents may require visibility into how they make decisions. Chain-of-thought (CoT) monitoring can detect misbehavior in today’s reasoning models, but this “monitorability” may be fragile under different training procedures, data sources, or continued system scaling. We propose three evaluation archetypes (intervention, process, and outcome-property), a new monitorability metric, and a broad evaluation suite. We show CoT monitoring outperforms action-only monitoring in practical settings, and that frontier models are generally—but not perfectly—monitorable. We study scaling trends with pre-training model size and inference-time compute, finding longer CoTs are typically more monitorable. We find that, for a fixed capability level, using a smaller model at higher reasoning effort can yield higher monitorability, at greater inference compute cost. We further find that increasing a weak monitor’s test-time compute when monitoring a strong agent improves monitorability, and giving the monitor access to the CoT both boosts monitorability and steepens the compute–to-monitorability scaling trend. Finally, we show monitorability can be improved by asking follow-up questions and giving the follow-up CoT to the monitor.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 6. Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections

Flags: systems_agents_program_signal, oral, github

- Review focus: Check whether program-selected papers substantiate systems/agents emphasis.
- Area/subarea: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Cluster: 40 - agents / agent / evaluation / agentic
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=26; 7d visits=45
- Artifact: https://github.com/Snowflake-Labs/MADQA; stars=1; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=Reasoning / test-time compute; Agents / tool use; eval=language/llm; theory/synthetic
- Benchmark/data/metric cues: VQA / none / accuracy
- ICML URL: https://icml.cc/virtual/2026/poster/62732
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.12180

Abstract:

Multimodal agents offer a compelling path to automating complex document-intensive workflows, yet a critical question remains: do these architectures demonstrate genuine strategic reasoning, or simply conduct stochastic trial-and-error search? To address this, we introduce Agentic Document VQA, a benchmark of 2,250 human-authored questions grounded in 800 heterogeneous PDF documents. Guided by *Classical Test Theory*, we design it to maximize discriminative power and reliably differentiate between varying levels of agent capability. To rigorously assess agentic behaviour, we introduce a novel evaluation protocol for measuring the accuracy-effort trade-off. Using this framework, we find that humans show strong metacognitive calibration, adapting or abandoning failed strategies, whereas frontier agents often persist in unproductive loops with diminishing returns. We release the dataset, evaluation harness, and leaderboard to help facilitate the transition from brute-force retrieval to calibrated, efficient reasoning.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 7. CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability

Flags: systems_agents_program_signal, oral, github

- Review focus: Check whether program-selected papers substantiate systems/agents emphasis.
- Area/subarea: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Cluster: 40 - agents / agent / evaluation / agentic
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=21; 7d visits=41
- Artifact: https://github.com/livecvebench/CVE-Factory; stars=139; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=LLM post-training; Reasoning / test-time compute; Agents / tool use; Compression / efficiency; eval=math/code/verifiable; security/safety
- Benchmark/data/metric cues: LiveCVEBench / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/65622
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.03012

Abstract:

Evaluating and improving the security capabilities of code agents requires high-quality, executable vulnerability tasks. However, existing works rely on costly, unscalable manual reproduction and suffer from outdated data distributions. To address these, we present CVE-Factory, the first multi-agent framework to achieve expert-level quality in automatically transforming sparse CVE metadata into fully executable agentic tasks. Cross-validation against human expert reproductions shows that CVE-Factory achieves 95\% solution correctness and 96\% environment fidelity, confirming its expert-level quality. It is also evaluated on the latest realistic vulnerabilities and achieves a 66.2\% verified success. This automation enables two downstream contributions. First, we construct LiveCVEBench, a continuously updated benchmark of 190 tasks spanning 14 languages and 153 repositories that captures emerging threats including AI-tooling vulnerabilities. Second, we synthesize over 1,000 executable training environments, the first large-scale scaling of agentic tasks in code security. Fine-tuned Qwen3-32B improves from 5.3\% to 35.8\% on LiveCVEBench, surpassing Claude 4.5 Sonnet, with gains generalizing to Terminal Bench (12.5\% to 31.3\%). We open-source all code, data, and models.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 8. mHC: Manifold-Constrained Hyper-Connections

Flags: systems_agents_public_signal, taxonomy-review, github

- Review focus: Check whether public signal reflects core infrastructure/agent workloads or broad LLM spillover.
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

### 9. Learning to Discover at Test Time

Flags: systems_agents_public_signal, taxonomy-review, github

- Review focus: Check whether public signal reflects core infrastructure/agent workloads or broad LLM spillover.
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

### 10. xKV: Cross-Layer KV-Cache Compression via Aligned Singular Vector Extraction

Flags: systems_agents_public_signal, github

- Review focus: Check whether public signal reflects core infrastructure/agent workloads or broad LLM spillover.
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

### 11. PaperBanana: Automating Academic Illustration for AI Scientists

Flags: systems_agents_public_signal, github

- Review focus: Check whether public signal reflects core infrastructure/agent workloads or broad LLM spillover.
- Area/subarea: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Cluster: 40 - agents / agent / evaluation / agentic
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=420; 7d visits=123
- Artifact: https://github.com/dwzhu-pku/PaperBanana; stars=6765; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=Agents / tool use; eval=vision/video; language/llm
- Benchmark/data/metric cues: PaperBananaBench / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/65206
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.23265

Abstract:

Despite rapid advances in autonomous AI scientists powered by language models, generating publication-ready illustrations remains a labor-intensive bottleneck in the research workflow. To lift this burden, we introduce PaperBanana, an agentic framework for automated generation of publication-ready academic illustrations. Powered by state-of-the-art VLMs and image generation models, PaperBanana orchestrates specialized agents to retrieve references, plan content and style, render images, and iteratively refine via self-critique. To rigorously evaluate our framework, we introduce PaperBananaBench, comprising 292 test cases for methodology diagrams curated from NeurIPS 2025 publications, covering diverse research domains and illustration styles. Comprehensive experiments demonstrate that PaperBanana consistently outperforms leading baselines in faithfulness, conciseness, readability, and aesthetics. We further show that our method effectively extends to the generation of high-quality statistical plots. Collectively, PaperBanana paves the way for the automated generation of publication-ready illustrations.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 12. Evolution Strategies at the Hyperscale

Flags: systems_agents_public_signal, taxonomy-review, github

- Review focus: Check whether public signal reflects core infrastructure/agent workloads or broad LLM spillover.
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

### 13. Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights

Flags: systems_agents_public_signal, taxonomy-review, github

- Review focus: Check whether public signal reflects core infrastructure/agent workloads or broad LLM spillover.
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

### 14. ToolOrchestra: Elevating Intelligence via Efficient Model and Tool Orchestration

Flags: systems_agents_public_signal, github

- Review focus: Check whether public signal reflects core infrastructure/agent workloads or broad LLM spillover.
- Area/subarea: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Cluster: 40 - agents / agent / evaluation / agentic
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=260; 7d visits=17
- Artifact: https://github.com/NVlabs/ToolOrchestra; stars=745; manual-check=none
- Evidence tags: contribution=Theory / proof; methods=RL / policy optimization; LLM post-training; Reasoning / test-time compute; Agents / tool use; eval=language/llm
- Benchmark/data/metric cues: none / none / accuracy
- ICML URL: https://icml.cc/virtual/2026/poster/62794
- AlphaXiv URL: https://www.alphaxiv.org/abs/2511.21689

Abstract:

Large language models are powerful generalists, yet solving deep and complex problems such as those of the Humanity’s Last Exam (HLE) remains both conceptually challenging and computationally expensive. We show that small orchestrators managing other models and a variety of tools are able to both push the upper bound of intelligence and improve efficiency in solving difficult agentic tasks. We introduce ToolOrchestra, a method for training small orchestrators that coordinate the use of intelligent tools. ToolOrchestra makes explicit use of reinforcement learning with outcome-, efficiency-, and user-preference-aware rewards. Using ToolOrchestra, we produce Orchestrator, an 8B model that achieves higher accuracy at lower cost than previous tool-use agents while aligning with user preferences on which tools are to be used for a given query. On HLE, Orchestrator achieves a score of 37.1%, outperforming GPT-5 (35.1%) while being 2.5x more efficient. On $\tau ^2$-Bench and FRAMES, Orchestrator surpasses GPT-5 by a wide margin while using only about 30% of the cost. Extensive analysis shows that Orchestrator achieves the best trade-off between performance and cost under multiple metrics, and generalizes robustly to previously unseen tools. These results demonstrate that composing diverse tools with a lightweight orchestration model is both more efficient and more effective than existing methods, paving the way for practical and scalable tool-augmented reasoning systems. These results demonstrate that orchestrating diverse tools with lightweight agents is not only more efficient, but also more effective, paving the way for practical and scalable tool-augmented reasoning systems.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:
