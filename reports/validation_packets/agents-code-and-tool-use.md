# Agents, Code, and Tool Use

Manual validation packet for representative and boundary papers.

## Area Context

Headline: Agents are shifting from impressive demos toward evaluation harnesses, tool environments, and software/security tasks.

Fault lines:
- Better scaffolding and prompting versus actual learned agent capability.
- Static benchmarks versus dynamic environments with hidden state, long horizons, and recovery from failure.
- Code and security agents as practical systems versus brittle benchmark optimizers.

What to read for:
- Does the environment prevent leakage and reward shortcut behavior?
- Is improvement coming from model training, search, memory, tools, or evaluation-loop design?
- Are failures categorized by planning, perception, tool use, memory, or execution?

## Queue Summary

- Papers: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, program_signal_low_public_attention=4, taxonomy_boundary_cluster=2
- Papers from taxonomy-review clusters: 5
- Papers with GitHub URLs: 13

## Papers

### 1. $\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment

Flags: fault_line_representative, oral, github

- Subarea: Agent evaluation, tool use, and agentic workflows
- Votes: 89
- ICML URL: https://icml.cc/virtual/2026/poster/64377
- AlphaXiv URL: https://www.alphaxiv.org/abs/2506.07982
- GitHub URL: https://github.com/sierra-research/tau2-bench
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Theory / proof
- Method families: Reasoning / test-time compute; Agents / tool use
- Evaluation settings: math/code/verifiable; robotics/embodied; language/llm; theory/synthetic
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Existing benchmarks for conversational AI agents simulate *single-control* environments, where only the AI agent can use tools to interact with the world, while the user remains a passive information provider. This differs from real-world scenarios like technical support, where users need to actively participate in modifying the state of the (shared) world. In order to address this gap, we introduce $\tau^2$-bench, with four key contributions: 1. A novel **Telecom dual-control domain** modeled as a Dec-POMDP, where both agent and user make use of tools to act in a shared, dynamic environment that tests both agent coordination and communication, 2. A **compositional task generator** that programmatically creates diverse, verifiable tasks from atomic components, ensuring domain coverage and controlled complexity, 3. A **reliable user simulator** tightly coupled with the environment, whose behavior is constrained by tools and observable states, improving simulation fidelity, 4. **fine-grained analysis of agent performance** through multiple ablations including separating errors arising from reasoning vs communication/coordination. In particular, our experiments show significant performance drops when agents shift from no-user to dual-control, highlighting the challenges of guiding users. Overall, $\tau^2$-bench provides a controlled testbed for agents that must both reason effectively and guide user actions.

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

### 2. Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning

Flags: fault_line_representative, oral, github

- Subarea: Agent evaluation, tool use, and agentic workflows
- Votes: 89
- ICML URL: https://icml.cc/virtual/2026/poster/63095
- AlphaXiv URL: https://www.alphaxiv.org/abs/2511.19900
- GitHub URL: https://github.com/aiming-lab/Agent0
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource
- Method families: RL / policy optimization; Reasoning / test-time compute; Agents / tool use; Graphs / geometry
- Evaluation settings: vision/video; language/llm
- Result claim cues: negative / limitation; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: reward

Abstract:

Large Vision-Language Models (LVLMs) have achieved remarkable progress in multimodal reasoning tasks; however, their learning remains constrained by the limitations of human-annotated supervision. Recent self-rewarding approaches attempt to overcome this constraint by allowing models to act as their own critics or reward providers. Yet, purely text-based self-evaluation struggles to verify complex visual reasoning steps and often suffers from evaluation hallucinations. To address these challenges, inspired by recent advances in tool-integrated reasoning, we propose Agent0-VL, a self-evolving vision-language agent that achieves continual improvement with tool-integrated reasoning. Agent0-VL incorporates tool usage not only into reasoning but also into self-evaluation and self-repair, enabling the model to introspect, verify, and refine its reasoning through evidence-grounded analysis. It unifies two synergistic roles within a single LVLM: a Solver that performs multi-turn tool-integrated reasoning, and a Verifier that generates structured feedback and fine-grained self-rewards through tool-grounded critique. These roles interact through a Self-Evolving Reasoning Cycle, where tool-based verification and reinforcement learning jointly align the reasoning and evaluation distributions for stable self-improvement. Through this zero-external-reward evolution, Agent0-VL aligns its reasoning and verification behaviors without any human annotation or external reward models, achieving continual self-improvement. Experiments on chart reasoning, geometric problem solving, and visual scientific analysis show that Agent0-VL achieves an 12.5% improvement over the Qwen-VL base model.

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

### 3. daVinci-Dev: Agent-native Mid-training for Software Engineering

Flags: fault_line_representative, oral, github

- Subarea: Agent evaluation, tool use, and agentic workflows
- Votes: 52
- ICML URL: https://icml.cc/virtual/2026/poster/63099
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.18418
- GitHub URL: https://github.com/sii-research/GAIR
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; Method / algorithm
- Method families: RL / policy optimization; LLM post-training; Reasoning / test-time compute; Agents / tool use; Diffusion / flow
- Evaluation settings: math/code/verifiable; language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Recently, the frontier of Large Language Model (LLM) capabilities has shifted from single-turn code generation to agentic software engineering—a paradigm where models autonomously navigate, edit, and test complex repositories. While post-training methods have become the de facto approach for code agents, *agentic mid-training*—mid-training (MT) on large-scale data that mirrors authentic agentic workflows—remains critically underexplored due to substantial resource requirements, despite offering a more scalable path to instilling foundational agentic behaviors than relying solely on expensive reinforcement learning. A central challenge in realizing effective agentic mid-training is the distribution mismatch between static training data and the dynamic, feedback-rich environment of real development. To address this, we present a systematic study of agentic mid-training, establishing both the data synthesis principles and training methodology for effective agent development at scale. Central to our approach is *agent-native data*—supervision comprising two complementary types of trajectories: *contextually-native trajectories* that preserve the complete information flow an agent experiences, offering broad coverage and diversity; and *environmentally-native trajectories* collected from executable repositories where observations stem from actual tool invocations and test executions, providing depth and interaction authenticity. We verify the model’s agentic capabilities on `SWE-Bench Verified`. We demonstrate our superiority over the previous open software engineering mid-training recipe `Kimi-Dev` under two post-training settings with an aligned base model and agentic scaffold, while using less than half mid-training tokens (73.1B). Besides relative advantage, our best performing 32B and 72B models achieve **56.1%** and **58.5%** resolution rates, respectively, which are state-of-the-art among open training recipes using agentic scaffolds under their model sizes, despite starting from non-coder `Qwen2.5-Base` base models. Beyond these agentic capabilities, we also observe performance gains on general code generation and scientific benchmarks. We plan to open-source a significant portion of our datasets, recipes, and model checkpoints—resources representing substantial computational investment typically unavailable to the broader community—to facilitate further research in this underexplored paradigm.

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

### 4. Monitoring Monitorability

Flags: fault_line_representative, oral, github

- Subarea: Agent evaluation, tool use, and agentic workflows
- Votes: 28
- ICML URL: https://icml.cc/virtual/2026/poster/62992
- AlphaXiv URL: https://www.alphaxiv.org/abs/2512.18311
- GitHub URL: https://github.com/nightscout/cgm-remote-monitor
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; System / infrastructure; Method / algorithm
- Method families: Reasoning / test-time compute; Agents / tool use
- Evaluation settings: robotics/embodied
- Result claim cues: negative / limitation; scaling / efficiency; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Safe deployment of increasingly capable AI agents may require visibility into how they make decisions. Chain-of-thought (CoT) monitoring can detect misbehavior in today’s reasoning models, but this “monitorability” may be fragile under different training procedures, data sources, or continued system scaling. We propose three evaluation archetypes (intervention, process, and outcome-property), a new monitorability metric, and a broad evaluation suite. We show CoT monitoring outperforms action-only monitoring in practical settings, and that frontier models are generally—but not perfectly—monitorable. We study scaling trends with pre-training model size and inference-time compute, finding longer CoTs are typically more monitorable. We find that, for a fixed capability level, using a smaller model at higher reasoning effort can yield higher monitorability, at greater inference compute cost. We further find that increasing a weak monitor’s test-time compute when monitoring a strong agent improves monitorability, and giving the monitor access to the CoT both boosts monitorability and steepens the compute–to-monitorability scaling trend. Finally, we show monitorability can be improved by asking follow-up questions and giving the follow-up CoT to the monitor.

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

### 5. Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections

Flags: fault_line_representative, oral, github

- Subarea: Agent evaluation, tool use, and agentic workflows
- Votes: 26
- ICML URL: https://icml.cc/virtual/2026/poster/62732
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.12180
- GitHub URL: https://github.com/Snowflake-Labs/MADQA
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; Method / algorithm
- Method families: Reasoning / test-time compute; Agents / tool use
- Evaluation settings: language/llm; theory/synthetic
- Result claim cues: negative / limitation; scaling / efficiency
- Benchmarks: VQA
- Datasets: none
- Metrics: accuracy

Abstract:

Multimodal agents offer a compelling path to automating complex document-intensive workflows, yet a critical question remains: do these architectures demonstrate genuine strategic reasoning, or simply conduct stochastic trial-and-error search? To address this, we introduce Agentic Document VQA, a benchmark of 2,250 human-authored questions grounded in 800 heterogeneous PDF documents. Guided by *Classical Test Theory*, we design it to maximize discriminative power and reliably differentiate between varying levels of agent capability. To rigorously assess agentic behaviour, we introduce a novel evaluation protocol for measuring the accuracy-effort trade-off. Using this framework, we find that humans show strong metacognitive calibration, adapting or abandoning failed strategies, whereas frontier agents often persist in unproductive loops with diminishing returns. We release the dataset, evaluation harness, and leaderboard to help facilitate the transition from brute-force retrieval to calibrated, efficient reasoning.

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

### 6. CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability

Flags: fault_line_representative, oral, github

- Subarea: Agent evaluation, tool use, and agentic workflows
- Votes: 21
- ICML URL: https://icml.cc/virtual/2026/poster/65622
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.03012
- GitHub URL: https://github.com/livecvebench/CVE-Factory
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Method / algorithm
- Method families: LLM post-training; Reasoning / test-time compute; Agents / tool use; Compression / efficiency
- Evaluation settings: math/code/verifiable; security/safety
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: LiveCVEBench
- Datasets: none
- Metrics: none

Abstract:

Evaluating and improving the security capabilities of code agents requires high-quality, executable vulnerability tasks. However, existing works rely on costly, unscalable manual reproduction and suffer from outdated data distributions. To address these, we present CVE-Factory, the first multi-agent framework to achieve expert-level quality in automatically transforming sparse CVE metadata into fully executable agentic tasks. Cross-validation against human expert reproductions shows that CVE-Factory achieves 95\% solution correctness and 96\% environment fidelity, confirming its expert-level quality. It is also evaluated on the latest realistic vulnerabilities and achieves a 66.2\% verified success. This automation enables two downstream contributions. First, we construct LiveCVEBench, a continuously updated benchmark of 190 tasks spanning 14 languages and 153 repositories that captures emerging threats including AI-tooling vulnerabilities. Second, we synthesize over 1,000 executable training environments, the first large-scale scaling of agentic tasks in code security. Fine-tuned Qwen3-32B improves from 5.3\% to 35.8\% on LiveCVEBench, surpassing Claude 4.5 Sonnet, with gains generalizing to Terminal Bench (12.5\% to 31.3\%). We open-source all code, data, and models.

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

### 7. Learning to Discover at Test Time

Flags: public_attention_not_program_signal, taxonomy-review, github

- Subarea: Multi-agent search, planning, and coordination
- Votes: 529
- ICML URL: https://icml.cc/virtual/2026/poster/65888
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.16175
- GitHub URL: https://github.com/sayantann11/all-classification-templetes-for-ML
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: System / infrastructure
- Contribution types: System / infrastructure; Method / algorithm
- Method families: RL / policy optimization; Reasoning / test-time compute; Agents / tool use; Diffusion / flow
- Evaluation settings: math/code/verifiable; language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

How can we use AI to discover a new state of the art for a scientific problem? Prior work in test-time scaling, such as AlphaEvolve, performs search by prompting a frozen LLM. We perform reinforcement learning at test time, so the LLM can continue to train, but now with experience specific to the test problem. This form of continual learning is quite special, because its goal is to produce one great solution rather than many good ones on average, and to solve this very problem rather than generalize to other problems. Therefore, our learning objective and search subroutine are designed to prioritize the most promising solutions. We call this method Test-Time Training to Discover (TTT-Discover). Following prior work, we focus on problems with continuous rewards. We report results for every problem we attempted, across mathematics, GPU kernel engineering, algorithm design, and biology. TTT-Discover sets the new state of the art in almost all of them: (i) Erdős' minimum overlap problem and an autocorrelation inequality; (ii) a GPUMode kernel competition (up to 2× faster than prior art); (iii) past AtCoder algorithm competitions; and (iv) denoising problem in single-cell analysis. Our solutions are reviewed by experts or the organizers. All our results are achieved with an open model, OpenAI gpt-oss-120b, and can be reproduced with our publicly available code, in contrast to previous best results that required closed frontier models. Our test-time training runs are performed using Tinker, an API by Thinking Machines, with a cost of only a few hundred dollars per problem.

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

### 8. PaperBanana: Automating Academic Illustration for AI Scientists

Flags: public_attention_not_program_signal, github

- Subarea: Agent evaluation, tool use, and agentic workflows
- Votes: 420
- ICML URL: https://icml.cc/virtual/2026/poster/65206
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.23265
- GitHub URL: https://github.com/dwzhu-pku/PaperBanana
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Method / algorithm
- Method families: Agents / tool use
- Evaluation settings: vision/video; language/llm
- Result claim cues: state-of-the-art / improvement
- Benchmarks: PaperBananaBench
- Datasets: none
- Metrics: none

Abstract:

Despite rapid advances in autonomous AI scientists powered by language models, generating publication-ready illustrations remains a labor-intensive bottleneck in the research workflow. To lift this burden, we introduce PaperBanana, an agentic framework for automated generation of publication-ready academic illustrations. Powered by state-of-the-art VLMs and image generation models, PaperBanana orchestrates specialized agents to retrieve references, plan content and style, render images, and iteratively refine via self-critique. To rigorously evaluate our framework, we introduce PaperBananaBench, comprising 292 test cases for methodology diagrams curated from NeurIPS 2025 publications, covering diverse research domains and illustration styles. Comprehensive experiments demonstrate that PaperBanana consistently outperforms leading baselines in faithfulness, conciseness, readability, and aesthetics. We further show that our method effectively extends to the generation of high-quality statistical plots. Collectively, PaperBanana paves the way for the automated generation of publication-ready illustrations.

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

### 9. ToolOrchestra: Elevating Intelligence via Efficient Model and Tool Orchestration

Flags: public_attention_not_program_signal, github

- Subarea: Agent evaluation, tool use, and agentic workflows
- Votes: 260
- ICML URL: https://icml.cc/virtual/2026/poster/62794
- AlphaXiv URL: https://www.alphaxiv.org/abs/2511.21689
- GitHub URL: https://github.com/NVlabs/ToolOrchestra
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: RL / policy optimization; LLM post-training; Reasoning / test-time compute; Agents / tool use
- Evaluation settings: language/llm
- Result claim cues: scaling / efficiency; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: accuracy

Abstract:

Large language models are powerful generalists, yet solving deep and complex problems such as those of the Humanity’s Last Exam (HLE) remains both conceptually challenging and computationally expensive. We show that small orchestrators managing other models and a variety of tools are able to both push the upper bound of intelligence and improve efficiency in solving difficult agentic tasks. We introduce ToolOrchestra, a method for training small orchestrators that coordinate the use of intelligent tools. ToolOrchestra makes explicit use of reinforcement learning with outcome-, efficiency-, and user-preference-aware rewards. Using ToolOrchestra, we produce Orchestrator, an 8B model that achieves higher accuracy at lower cost than previous tool-use agents while aligning with user preferences on which tools are to be used for a given query. On HLE, Orchestrator achieves a score of 37.1%, outperforming GPT-5 (35.1%) while being 2.5x more efficient. On $\tau ^2$-Bench and FRAMES, Orchestrator surpasses GPT-5 by a wide margin while using only about 30% of the cost. Extensive analysis shows that Orchestrator achieves the best trade-off between performance and cost under multiple metrics, and generalizes robustly to previously unseen tools. These results demonstrate that composing diverse tools with a lightweight orchestration model is both more efficient and more effective than existing methods, paving the way for practical and scalable tool-augmented reasoning systems. These results demonstrate that orchestrating diverse tools with lightweight agents is not only more efficient, but also more effective, paving the way for practical and scalable tool-augmented reasoning systems.

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

### 10. MemEvolve: Meta-Evolution of Agent Memory Systems

Flags: public_attention_not_program_signal, taxonomy-review, github

- Subarea: Multi-agent search, planning, and coordination
- Votes: 194
- ICML URL: https://icml.cc/virtual/2026/poster/61379
- AlphaXiv URL: https://www.alphaxiv.org/abs/2512.18746
- GitHub URL: https://github.com/bingreeky/MemEvolve
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; System / infrastructure; Method / algorithm
- Method families: Agents / tool use
- Evaluation settings: language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: memory

Abstract:

Self-evolving memory systems are rapidly reshaping the evolutionary paradigm of large language model (LLM)-based agents. Prior work has predominantly relied on manually engineered memory architectures to store trajectories, distill experience, and synthesize reusable tools, enabling agents to evolve on the fly within environment interactions. However, this paradigm is fundamentally constrained by the \textit{staticity} of the memory system itself: while memory facilitates agent-level evolving, the underlying memory architecture cannot be meta-adapted to diverse task contexts. To address this gap, we propose MemEvolve, a meta-evolutionary framework that jointly evolves agents’ experiential knowledge and their memory architecture, allowing agent systems not only to accumulate experience but also to progressively refine how they learn from it. To ground MemEvolve in prior work and promote openness in future self-evolving systems, we introduce EvolveLab, a unified memory codebase that distills twelve representative memory systems into a modular design space (\textit{encode}, \textit{store}, \textit{retrieve}, \textit{manage}), providing a standardized implementation substrate and a fair experimental arena. Extensive evaluations on four challenging agentic benchmarks show that MemEvolve delivers (i) substantial performance gains, improving frameworks such as SmolAgent and Flash-Searcher by up to $17.06\%$, and (ii) strong cross-task and cross-LLM generalization, yielding memory architectures that transfer effectively across diverse benchmarks and backbones.

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

### 11. CausalGame: Benchmarking Causal Thinking of LLM Agents in Games

Flags: program_signal_low_public_attention, oral

- Subarea: Agent evaluation, tool use, and agentic workflows
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/63530
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation
- Method families: Agents / tool use; Transformer / attention; Causal / data-centric
- Evaluation settings: language/llm; security/safety
- Result claim cues: negative / limitation
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Recently, it has received growing attention in building AI Scientist agents with Large Language Models (LLMs). Since scientific discovery fundamentally relies on uncovering causal relationships from observations, the capability of causal thinking that distinguish causation from correlation and hidden biases, is essential to LLM agents. Despite a number of existing benchmarks for AI scientists, none of them are designed with the consideration of hidden biases and confounders, that widely exist in real-world scientific discovery. To this end, we present CausalGame, a benchmark that evaluates the causal thinking capabilities of LLM agents through interactive games. More specifically, we ask LLM agents to actively design experimental protocols, collect observation data and derive a final solution with an explanation report. To emulate realistic scientific discovery challenges, we design 14 game settings with the incorporation of selection bias, noisy measurements, and hidden confounders. The results with 16 frontier LLM agents show that they consistently fail to reason about and recover the underlying causal relationships required to solve the games. CausalGame provides a rigorous measurement of capabilities essential to AI Scientist agents.

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

### 12. Characterizing Agents in Production

Flags: program_signal_low_public_attention, oral

- Subarea: Agent evaluation, tool use, and agentic workflows
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/61834
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: System / infrastructure
- Contribution types: System / infrastructure
- Method families: Agents / tool use
- Evaluation settings: language/llm
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

LLM-based agents already operate in production across many industries, yet we lack a clear understanding of which technical methods make these deployments successful. We present the first systematic study of Characterizing Agents in Production (CAP) using first-hand data from agent developers. We conducted 20 in-depth case studies through interviews and surveyed 306 practitioners across 26 domains. We examine why organizations build agents, how they build them, how they evaluate them, and the key challenges they face in deployment. Our findings show that production agents rely on simple, controllable approaches: 68% execute at most 10 steps before human intervention, 70% rely on prompting off-the-shelf models rather than weight tuning, and 74% depend primarily on human evaluation. Reliability—defined as consistent correct behavior over time—emerges as the dominant challenge, which practitioners address through system-level design choices. CAP documents the current state of production agents, providing the research community with visibility into real-world deployment practices and underexplored research opportunities.

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

### 13. VenusBench-Mobile: A Challenging and User-Centric Benchmark for Mobile GUI Agents with Capability Diagnostics

Flags: program_signal_low_public_attention, oral, github

- Subarea: Agent evaluation, tool use, and agentic workflows
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/62831
- AlphaXiv URL: https://www.alphaxiv.org/abs/2604.06182
- GitHub URL: https://github.com/inclusionAI/UI-Venus
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; System / infrastructure
- Method families: Agents / tool use
- Evaluation settings: none
- Result claim cues: negative / limitation; scaling / efficiency; robustness / safety; state-of-the-art / improvement
- Benchmarks: VenusBench-Mobile
- Datasets: none
- Metrics: memory

Abstract:

Existing online benchmarks for mobile GUI agents remain largely app-centric and task-homogeneous, failing to reflect the diversity and instability of real-world mobile usage. To this end, we introduce VenusBench-Mobile, a challenging online benchmark for evaluating general-purpose mobile GUI agents under realistic, user-centric conditions. VenusBench-Mobile builds two core evaluation pillars: defining what to evaluate via user-intent-driven task design that reflects real mobile usage, and how to evaluate through a capability-oriented annotation scheme for fine-grained agent behavior analysis. Extensive evaluation of state-of-the-art mobile GUI agents reveals large performance gaps relative to prior benchmarks, indicating that VenusBench-Mobile poses substantially more challenging and realistic tasks and that current agents remain far from reliable real-world deployment. Diagnostic analysis further shows that failures are dominated by deficiencies in perception and memory, which are largely obscured by coarse-grained evaluations. Moreover, even the strongest agents exhibit near-zero success under environment variations, highlighting their brittleness in realistic settings. Based on these insights, we believe VenusBench-Mobile provides an important stepping stone toward robust real-world deployment of mobile GUI agents.

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

### 14. Unsupervised Partner Design Enables Robust Ad-hoc Teamwork

Flags: program_signal_low_public_attention, oral, taxonomy-review, evidence-low

- Subarea: Multi-agent search, planning, and coordination
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/66728
- AlphaXiv URL: https://www.alphaxiv.org/abs/2508.06336
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: RL / policy optimization; Agents / tool use
- Evaluation settings: none
- Result claim cues: robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

We introduce Unsupervised Partner Design (UPD), a population-free multi-agent reinforcement learning method for robust ad-hoc teamwork. UPD generates training partners on-the-fly and selects them adaptively based on a learnability criterion, removing the need for pre-trained partner populations or manual parameter tuning. We show that this simple mechanism enables effective partner diversity and can be extended to joint partner-environment selection when a procedural level generator is available. Across Level-Based Foraging, Overcooked-AI, and the Overcooked Generalisation Challenge, UPD consistently outperforms both population-based and population-free baselines. In a human-AI user study, agents trained with UPD achieve higher returns and are rated as more adaptive, more human-like, and less frustrating than existing approaches.

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

### 15. Scaling Long-Horizon Agent via Context Folding

Flags: taxonomy_boundary_cluster, taxonomy-review, github

- Subarea: Multi-agent search, planning, and coordination
- Votes: 171
- ICML URL: https://icml.cc/virtual/2026/poster/61950
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.11967
- GitHub URL: https://github.com/sunnweiwei/FoldAgent
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: RL / policy optimization; Agents / tool use
- Evaluation settings: language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Large language model (LLM) agents are fundamentally constrained by context length on long-horizon tasks. Existing agent frameworks usually rely on manually defined context engineering pipelines, such as multi-agent or post-hoc summary. We introduce Context Folding, a framework that empowers agents to actively manage their working context. An agent can procedurally branch into a sub-trajectory to handle a subtask and then fold it upon completion, collapsing the intermediate steps while retaining a concise summary of the outcome. To make this behavior learnable, we propose FoldPO, an end-to-end reinforcement learning framework with specific process rewards to encourage effective task decomposition and context management. On complex long-horizon tasks, our agent matches the performance of baselines while using an active context up to 10x smaller, and significantly outperforms models constrained to the same context size.

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

### 16. Meta Context Engineering via Agentic Skill Evolution

Flags: taxonomy_boundary_cluster, taxonomy-review, github

- Subarea: Multi-agent search, planning, and coordination
- Votes: 132
- ICML URL: https://icml.cc/virtual/2026/poster/64296
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.21557
- GitHub URL: https://github.com/metaevo-ai/meta-context-engineering
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: Agents / tool use
- Evaluation settings: math/code/verifiable; language/llm
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

The operational efficacy of large language models relies heavily on their inference-time context. This has established Context Engineering (CE) as a formal discipline for optimizing these inputs. Current CE methods rely on manually crafted harnesses, such as rigid generation-reflection workflows and predefined context schemas. They impose structural biases and restrict context optimization to a narrow, intuition-bound design space. To address this, we introduce Meta Context Engineering (MCE), a bi-level framework that supersedes static CE heuristics by co-evolving CE skills and context artifacts. In MCE iterations, a meta-level agent refines engineering skills via agentic crossover, a deliberative search over the history of skills, their executions, and evaluations. A base-level agent executes these skills, learns from training rollouts, and optimizes context as flexible files and code. We evaluate MCE across five disparate domains under offline and online settings. MCE demonstrates consistent performance gains, achieving 5.6--53.8% relative improvement over state-of-the-art agentic CE methods (mean of 16.9%), while maintaining superior context adaptability, transferability, and efficiency in both context usage and training.

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
