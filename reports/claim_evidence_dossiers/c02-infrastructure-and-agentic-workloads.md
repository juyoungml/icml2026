# C02: Infrastructure and agentic workloads Evidence Dossier

This is an abstract/title-based pre-review aid. It does not fill or replace the manual validation fields.

## Claim

Systems/efficiency and agents/code look smaller than LLM reasoning by paper count, but both are clear ICML 2026 overweights versus the neighboring-venue baseline.

- Strength label: `moderate_to_strong`
- Evidence summary: Systems historical delta +2.1 pp, relative 1.68x; Agents historical delta +2.1 pp, relative 1.44x.
- Caveat: Historical comparison uses a keyword scorer; ICML 2025 and NeurIPS 2025 lack static abstracts in the current pull.
- Next validation: Read top positive-delta papers and check whether deltas reflect real venue emphasis or metadata/topic-label differences.
- Manual review progress: 0/14 rows reviewed; 14 remaining

## Pre-Review Summary

- Bucket mix: likely_supports: 14
- Selection mix: systems_agents_program_signal: 7, systems_agents_public_signal: 7
- Area mix: Agents, Code, and Tool Use: 9, Systems and Efficient Foundation Models: 5

## Adjudication Questions

- Does the abstract directly support the claim, or only share vocabulary with the claim?
- Is the assigned taxonomy area central to the paper, or just one application/context?
- If the paper is high-attention, is the attention driven by a reusable result, a benchmark, a demo, or a social trend?
- If the paper has a GitHub link, is it a real paper artifact and what reproduction claim can be safely made?

## Papers To Read First

- **Controlled LLM Training on Spectral Sphere** (`likely_supports`; oral, taxonomy-review, github): Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads.
- **Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning** (`likely_supports`; oral, github): Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads.
- **$\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment** (`likely_supports`; oral, github): Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads.
- **daVinci-Dev: Agent-native Mid-training for Software Engineering** (`likely_supports`; oral, github): Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads.
- **Monitoring Monitorability** (`likely_supports`; oral, github): Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads.
- **Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections** (`likely_supports`; oral, github): Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads.

## Paper-Level Pre-Review

| Rank | Paper | Bucket | Area | Signals | Why It Matters |
| ---: | --- | --- | --- | --- | --- |
| 1 | Controlled LLM Training on Spectral Sphere | likely_supports | Systems and Efficient Foundation Models | oral; votes=115; github_stars=130; taxonomy-review | Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads. |
| 2 | Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning | likely_supports | Agents, Code, and Tool Use | oral; votes=89; github_stars=1228 | Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads. |
| 3 | $\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment | likely_supports | Agents, Code, and Tool Use | oral; votes=89; github_stars=1569 | Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads. |
| 4 | daVinci-Dev: Agent-native Mid-training for Software Engineering | likely_supports | Agents, Code, and Tool Use | oral; votes=52; github_stars=9 | Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads. |
| 5 | Monitoring Monitorability | likely_supports | Agents, Code, and Tool Use | oral; votes=28; github_stars=2786 | Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads. |
| 6 | Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections | likely_supports | Agents, Code, and Tool Use | oral; votes=26; github_stars=1 | Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads. |
| 7 | CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability | likely_supports | Agents, Code, and Tool Use | oral; votes=21; github_stars=139 | Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads. |
| 8 | mHC: Manifold-Constrained Hyper-Connections | likely_supports | Systems and Efficient Foundation Models | votes=696; github_stars=367; taxonomy-review | Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads. |
| 9 | Learning to Discover at Test Time | likely_supports | Agents, Code, and Tool Use | votes=529; github_stars=297; taxonomy-review | Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads. |
| 10 | xKV: Cross-Layer KV-Cache Compression via Aligned Singular Vector Extraction | likely_supports | Systems and Efficient Foundation Models | votes=518; github_stars=52 | Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads. |
| 11 | PaperBanana: Automating Academic Illustration for AI Scientists | likely_supports | Agents, Code, and Tool Use | votes=420; github_stars=6765 | Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads. |
| 12 | Evolution Strategies at the Hyperscale | likely_supports | Systems and Efficient Foundation Models | votes=405; github_stars=346; taxonomy-review | Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads. |
| 13 | Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights | likely_supports | Systems and Efficient Foundation Models | votes=365; github_stars=627; taxonomy-review | Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads. |
| 14 | ToolOrchestra: Elevating Intelligence via Efficient Model and Tool Orchestration | likely_supports | Agents, Code, and Tool Use | votes=260; github_stars=745 | Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads. |

## Abstract Excerpts

### 1. Controlled LLM Training on Spectral Sphere

- Bucket: `likely_supports`
- Keyword hits: efficient; training; optimization
- URLs: [ICML](https://icml.cc/virtual/2026/poster/66212) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.08393)

Scaling large models requires optimization strategies that ensure rapid convergence grounded in stability. Maximal Update Parametrization ($\boldsymbol{\mu}$P) provides a theoretical safeguard for width-invariant $\Theta(1)$ activation control, whereas emerging optimizers like Muon are only "half-aligned" with these constraints: they control updates but allow weights to drift. To address this limitation, we introduce the **Spectral Sphere Optimizer (SSO)**, which enforces strict module-wise spectral constraints...

### 2. Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning

- Bucket: `likely_supports`
- Keyword hits: agent; tool; optimization
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63095) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.19900)

Large Vision-Language Models (LVLMs) have achieved remarkable progress in multimodal reasoning tasks; however, their learning remains constrained by the limitations of human-annotated supervision. Recent self-rewarding approaches attempt to overcome this constraint by allowing models to act as their own critics or reward providers. Yet, purely text-based self-evaluation struggles to verify complex visual reasoning steps and often suffers from evaluation hallucinations. To address these challenges, inspired by...

### 3. $\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment

- Bucket: `likely_supports`
- Keyword hits: agent; tool; code
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64377) / [AlphaXiv](https://www.alphaxiv.org/abs/2506.07982)

Existing benchmarks for conversational AI agents simulate *single-control* environments, where only the AI agent can use tools to interact with the world, while the user remains a passive information provider. This differs from real-world scenarios like technical support, where users need to actively participate in modifying the state of the (shared) world. In order to address this gap, we introduce $\tau^2$-bench, with four key contributions: 1. A novel **Telecom dual-control domain** modeled as a Dec-POMDP,...

### 4. daVinci-Dev: Agent-native Mid-training for Software Engineering

- Bucket: `likely_supports`
- Keyword hits: system; training; agent; tool; software; code; optimization
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63099) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.18418)

Recently, the frontier of Large Language Model (LLM) capabilities has shifted from single-turn code generation to agentic software engineering—a paradigm where models autonomously navigate, edit, and test complex repositories. While post-training methods have become the de facto approach for code agents, *agentic mid-training*—mid-training (MT) on large-scale data that mirrors authentic agentic workflows—remains critically underexplored due to substantial resource requirements, despite offering a more scalable...

### 5. Monitoring Monitorability

- Bucket: `likely_supports`
- Keyword hits: system; inference; training; agent; tool
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62992) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.18311)

Safe deployment of increasingly capable AI agents may require visibility into how they make decisions. Chain-of-thought (CoT) monitoring can detect misbehavior in today’s reasoning models, but this “monitorability” may be fragile under different training procedures, data sources, or continued system scaling. We propose three evaluation archetypes (intervention, process, and outcome-property), a new monitorability metric, and a broad evaluation suite. We show CoT monitoring outperforms action-only monitoring in...

### 6. Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections

- Bucket: `likely_supports`
- Keyword hits: efficient; agent; tool
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62732) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.12180)

Multimodal agents offer a compelling path to automating complex document-intensive workflows, yet a critical question remains: do these architectures demonstrate genuine strategic reasoning, or simply conduct stochastic trial-and-error search? To address this, we introduce Agentic Document VQA, a benchmark of 2,250 human-authored questions grounded in 800 heterogeneous PDF documents. Guided by *Classical Test Theory*, we design it to maximize discriminative power and reliably differentiate between varying...

### 7. CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability

- Bucket: `likely_supports`
- Keyword hits: training; agent; tool; code
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65622) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.03012)

Evaluating and improving the security capabilities of code agents requires high-quality, executable vulnerability tasks. However, existing works rely on costly, unscalable manual reproduction and suffer from outdated data distributions. To address these, we present CVE-Factory, the first multi-agent framework to achieve expert-level quality in automatically transforming sparse CVE metadata into fully executable agentic tasks. Cross-validation against human expert reproductions shows that CVE-Factory achieves...

### 8. mHC: Manifold-Constrained Hyper-Connections

- Bucket: `likely_supports`
- Keyword hits: training; optimization
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61870) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.24880)

Recently, studies exemplified by Hyper-Connections (HC) have extended the ubiquitous residual connection paradigm established over the past decade by expanding the residual stream width and diversifying connectivity patterns. While yielding substantial performance gains, this diversification fundamentally compromises the identity mapping property intrinsic to the residual connection, which causes severe training instability and restricted scalability, and additionally incurs notable memory access overhead. To...

### 9. Learning to Discover at Test Time

- Bucket: `likely_supports`
- Keyword hits: training; agent; tool; code; optimization
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65888) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.16175)

How can we use AI to discover a new state of the art for a scientific problem? Prior work in test-time scaling, such as AlphaEvolve, performs search by prompting a frozen LLM. We perform reinforcement learning at test time, so the LLM can continue to train, but now with experience specific to the test problem. This form of continual learning is quite special, because its goal is to produce one great solution rather than many good ones on average, and to solve this very problem rather than generalize to other...

### 10. xKV: Cross-Layer KV-Cache Compression via Aligned Singular Vector Extraction

- Bucket: `likely_supports`
- Keyword hits: inference; training; cache; agent; tool; code; latency; throughput
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63436) / [AlphaXiv](https://www.alphaxiv.org/abs/2503.18893)

Long-context Large Language Models (LLMs) enable powerful applications but incur high memory costs due to the key–value states (KV-Cache). Recent studies attempt to share KV-Cache across layers, but these approaches either require expensive pretraining or rely on per-token cross-layer cosine similarity that is often limited in practice. We show, via Centered Kernel Alignment (CKA), that the dominant singular vectors of KV-Cache are well aligned across layers. Motivated by this observation, we propose xKV, a...

### 11. PaperBanana: Automating Academic Illustration for AI Scientists

- Bucket: `likely_supports`
- Keyword hits: agent; tool
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65206) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.23265)

Despite rapid advances in autonomous AI scientists powered by language models, generating publication-ready illustrations remains a labor-intensive bottleneck in the research workflow. To lift this burden, we introduce PaperBanana, an agentic framework for automated generation of publication-ready academic illustrations. Powered by state-of-the-art VLMs and image generation models, PaperBanana orchestrates specialized agents to retrieve references, plan content and style, render images, and iteratively refine...

### 12. Evolution Strategies at the Hyperscale

- Bucket: `likely_supports`
- Keyword hits: inference; training; throughput; optimization
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62943) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.16652)

Evolution Strategies (ES) is a class of powerful black-box optimisation methods that are highly parallelisable and can handle non-differentiable and noisy objectives. However, naïve ES becomes prohibitively expensive at scale on GPUs due to the low arithmetic intensity of batched matrix multiplications with unstructured random perturbations. We introduce Evolution Guided GeneRal Optimisation via Low-rank Learning (EGGROLL), which improves arithmetic intensity by structuring individual perturbations as rank-$r$...

### 13. Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights

- Bucket: `likely_supports`
- Keyword hits: training; optimization
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65901) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.12228)

Pretraining produces a learned parameter vector that is typically treated as a starting point for further iterative adaptation. In this work, we instead view the outcome of pretraining as a distribution over parameter vectors, whose support already contains task-specific experts. We show that in smaller or insufficiently trained models such expert solutions occupy a negligible fraction of the volume of this distribution, making their discovery reliant on structured optimization methods such as gradient descent....

### 14. ToolOrchestra: Elevating Intelligence via Efficient Model and Tool Orchestration

- Bucket: `likely_supports`
- Keyword hits: system; efficient; training; agent; tool; optimization
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62794) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.21689)

Large language models are powerful generalists, yet solving deep and complex problems such as those of the Humanity’s Last Exam (HLE) remains both conceptually challenging and computationally expensive. We show that small orchestrators managing other models and a variety of tools are able to both push the upper bound of intelligence and improve efficiency in solving difficult agentic tasks. We introduce ToolOrchestra, a method for training small orchestrators that coordinate the use of intelligent tools....
