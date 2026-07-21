# C07: Artifact visibility Evidence Dossier

This is an abstract/title-based pre-review aid. It does not fill or replace the manual validation fields.

## Claim

Artifacts are most visible in agents/code, LLM reasoning, systems, and multimodal/vision, while theory remains much less artifact-linked.

- Strength label: `moderate`
- Evidence summary: Robotics, Embodiment, and World Models: GitHub URL share 38.0%; Agents, Code, and Tool Use: GitHub URL share 32.9%; LLM Reasoning, Post-Training, and RLVR: GitHub URL share 32.1%; Generative Modeling: GitHub URL share 31.1%
- Caveat: GitHub metadata comes from AlphaXiv and does not prove runnable reproduction; some high-star links are templates or index repos.
- Next validation: Clone/check high-signal repositories and separate code, benchmark, dataset, checkpoint, and project-page links.
- Manual review progress: 0/16 rows reviewed; 16 remaining

## Pre-Review Summary

- Bucket mix: high_risk_artifact: 12, high_visibility_artifact: 4
- Selection mix: artifact_high_star: 9, artifact_manual_check: 7
- Area mix: Multimodal, Vision, and Perception: 5, LLM Reasoning, Post-Training, and RLVR: 4, Robotics, Embodiment, and World Models: 3, Agents, Code, and Tool Use: 2, AI for Science, Health, and Neuro: 1, Generative Modeling: 1

## Adjudication Questions

- Does the abstract directly support the claim, or only share vocabulary with the claim?
- Is the assigned taxonomy area central to the paper, or just one application/context?
- If the paper is high-attention, is the attention driven by a reusable result, a benchmark, a demo, or a social trend?
- If the paper has a GitHub link, is it a real paper artifact and what reproduction claim can be safely made?

## Papers To Read First

- **From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model** (`high_risk_artifact`; oral, github): GitHub URL is explicitly flagged for manual artifact checking.
- **PaperBanana: Automating Academic Illustration for AI Scientists** (`high_visibility_artifact`; github): GitHub-linked paper with high star count; needs artifact-type review.
- **DFlash: Block Diffusion for Flash Speculative Decoding** (`high_visibility_artifact`; taxonomy-review, github): GitHub-linked paper with high star count; needs artifact-type review.
- **DeepAnalyze: Agentic Large Language Models for Autonomous Data Science** (`high_visibility_artifact`; github): GitHub-linked paper with high star count; needs artifact-type review.
- **LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model** (`high_risk_artifact`; github): GitHub URL is explicitly flagged for manual artifact checking.
- **Vision-aligned Latent Reasoning for Multi-Modal Large Language Model** (`high_risk_artifact`; taxonomy-review, github): GitHub URL is explicitly flagged for manual artifact checking.

## Paper-Level Pre-Review

| Rank | Paper | Bucket | Area | Signals | Why It Matters |
| ---: | --- | --- | --- | --- | --- |
| 1 | From geometry to dynamics: Learning overdamped Langevin dynamics from sparse observations with geometric constraints | high_risk_artifact | AI for Science, Health, and Neuro | votes=2; github_stars=17294 | GitHub URL is explicitly flagged for manual artifact checking. |
| 2 | Vision-aligned Latent Reasoning for Multi-Modal Large Language Model | high_risk_artifact | LLM Reasoning, Post-Training, and RLVR | votes=56; github_stars=6773; taxonomy-review | GitHub URL is explicitly flagged for manual artifact checking. |
| 3 | Self-Prompting Diffusion Transformer for Open-Vocabulary Scene Text Edit via In-Context Learning | high_risk_artifact | Generative Modeling | votes=6; github_stars=5069 | GitHub URL is explicitly flagged for manual artifact checking. |
| 4 | From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model | high_risk_artifact | Robotics, Embodiment, and World Models | oral; votes=14; github_stars=5069 | GitHub URL is explicitly flagged for manual artifact checking. |
| 5 | Autoregressive Direct Preference Optimization | high_risk_artifact | LLM Reasoning, Post-Training, and RLVR | votes=6; github_stars=5063; taxonomy-review | GitHub URL is explicitly flagged for manual artifact checking. |
| 6 | AuTAgent: A Reinforcement Learning Framework for Tool-Augmented Audio Reasoning | high_risk_artifact | LLM Reasoning, Post-Training, and RLVR | votes=8; github_stars=5063; taxonomy-review | GitHub URL is explicitly flagged for manual artifact checking. |
| 7 | PanoWorld-X: Generating Explorable Panoramic Worlds via Sphere-Aware Video Diffusion | high_risk_artifact | Multimodal, Vision, and Perception | votes=12; github_stars=5063 | GitHub URL is explicitly flagged for manual artifact checking. |
| 8 | PaperBanana: Automating Academic Illustration for AI Scientists | high_visibility_artifact | Agents, Code, and Tool Use | votes=420; github_stars=6765 | GitHub-linked paper with high star count; needs artifact-type review. |
| 9 | DFlash: Block Diffusion for Flash Speculative Decoding | high_visibility_artifact | LLM Reasoning, Post-Training, and RLVR | votes=153; github_stars=5451; taxonomy-review | GitHub-linked paper with high star count; needs artifact-type review. |
| 10 | Boosting Monocular Metric Depth Estimation via Bokeh Rendering | high_risk_artifact | Multimodal, Vision, and Perception | votes=4; github_stars=5063 | GitHub URL is explicitly flagged for manual artifact checking. |
| 11 | AudioChat: Unified Audio Storytelling, Editing, and Understanding with Transfusion Forcing | high_risk_artifact | Multimodal, Vision, and Perception | votes=14; github_stars=5063 | GitHub URL is explicitly flagged for manual artifact checking. |
| 12 | From Correspondence to Actions: Human-Like Multi-Image Spatial Reasoning in Multi-modal Large Language Models | high_risk_artifact | Multimodal, Vision, and Perception | votes=12; github_stars=5063 | GitHub URL is explicitly flagged for manual artifact checking. |
| 13 | LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model | high_risk_artifact | Robotics, Embodiment, and World Models | votes=73; github_stars=5063 | GitHub URL is explicitly flagged for manual artifact checking. |
| 14 | Hydra-Nav: Object Navigation via Adaptive Dual-Process Reasoning | high_risk_artifact | Robotics, Embodiment, and World Models | votes=15; github_stars=5063 | GitHub URL is explicitly flagged for manual artifact checking. |
| 15 | Turbo4DGen: Ultra-Fast Acceleration for 4D Generation | high_visibility_artifact | Multimodal, Vision, and Perception | votes=0; github_stars=4818 | GitHub-linked paper with high star count; needs artifact-type review. |
| 16 | DeepAnalyze: Agentic Large Language Models for Autonomous Data Science | high_visibility_artifact | Agents, Code, and Tool Use | votes=146; github_stars=4355 | GitHub-linked paper with high star count; needs artifact-type review. |

## Abstract Excerpts

### 1. From geometry to dynamics: Learning overdamped Langevin dynamics from sparse observations with geometric constraints

- Bucket: `high_risk_artifact`
- Keyword hits: benchmark
- URLs: [ICML](https://icml.cc/virtual/2026/poster/60982) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.23566)

How can we learn the laws underlying the dynamics of stochastic systems when their trajectories are sampled sparsely in time? Existing methods either require temporally resolved high-frequency observations, or rely on geometric arguments that apply only to conservative systems, limiting the range of dynamics they can recover. Here, we present a new framework that reconciles these two perspectives by reformulating inference as a stochastic control problem. Our method uses geometry-driven path augmentation,...

### 2. Vision-aligned Latent Reasoning for Multi-Modal Large Language Model

- Bucket: `high_risk_artifact`
- Keyword hits: code; benchmark
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61382) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.04476)

Despite recent advancements in Multi-modal Large Language Models (MLLMs) on diverse understanding tasks, these models struggle to solve problems which require extensive multi-step reasoning. This is primarily due to the progressive dilution of visual information during long-context generation, which hinders their ability to fully exploit test-time scaling. To address this issue, we introduce Vision-aligned Latent Reasoning (VaLR), a simple, yet effective reasoning framework that dynamically generates...

### 3. Self-Prompting Diffusion Transformer for Open-Vocabulary Scene Text Edit via In-Context Learning

- Bucket: `high_risk_artifact`
- Keyword hits: code; dataset
- URLs: [ICML](https://icml.cc/virtual/2026/poster/60814) / [AlphaXiv](https://www.alphaxiv.org/abs/2605.15523)

Scene text editing aims to modify text in a target region of an image while preserving its background style and texture. Existing methods rely solely on image background information while neglecting the visual details of target regions, which discards stylistic features in the original text and essentially degrades the task to text rendering. Moreover, the conditions imposed by pre-trained glyph encoder limit the scope of editable text. To address these issues, this paper proposes a self-prompting scene text...

### 4. From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model

- Bucket: `high_risk_artifact`
- Keyword hits: code
- URLs: [ICML](https://icml.cc/virtual/2026/poster/66596) / [AlphaXiv](https://www.alphaxiv.org/abs/2605.22671)

Vision-Language-Action (VLA) models often suffer from performance degradation under distribution shifts, as they struggle to learn generalized behavior representations across varying environments. While existing approaches attempt to construct behavior representations through action-centric latent variables, they are often limited by short-horizon temporal fragmentation and static execution-alignment, leading to inconsistent behaviors in complex scenarios. To address these limitations, we propose...

### 5. Autoregressive Direct Preference Optimization

- Bucket: `high_risk_artifact`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65423) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.09533)

Direct preference optimization (DPO) has emerged as a promising approach for aligning large language models (LLMs) with human preferences. However, the widespread reliance on the response-level Bradley-Terry (BT) model may limit its full potential, as the reference and learnable models are assumed to be autoregressive only after deriving the objective function. Motivated by this limitation, we revisit the theoretical foundations of DPO and propose a novel formulation that explicitly introduces the...

### 6. AuTAgent: A Reinforcement Learning Framework for Tool-Augmented Audio Reasoning

- Bucket: `high_risk_artifact`
- Keyword hits: code; benchmark; open-source
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64128) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.13685)

Large Audio Language Models (LALMs) excel at perception but struggle with complex reasoning requiring precise acoustic measurements. While external tools can extract fine-grained features like exact tempo or pitch, effective integration remains challenging: naively using all tools causes information overload, while prompt-based selection fails to assess context-dependent utility. To address this, we propose **AuTAgent** (**Au**dio **T**ool **Agent**), a reinforcement learning framework that learns when and...

### 7. PanoWorld-X: Generating Explorable Panoramic Worlds via Sphere-Aware Video Diffusion

- Bucket: `high_risk_artifact`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/60719) / [AlphaXiv](https://www.alphaxiv.org/abs/2509.24997)

Achieving a complete and explorable 360-degree visual world is a cornerstone of immersive content creation. While recent advances in video generation have achieved impressive results, they follow a 2D paradigm that treats content generation as transitions of 2D pixels, lacking an intrinsic understanding of the physical 3D world, resulting in frequent geometric inconsistencies. To achieve an explorable and physical-consistent visual world, the generation process should shift to a 3D paradigm: the visual content...

### 8. PaperBanana: Automating Academic Illustration for AI Scientists

- Bucket: `high_visibility_artifact`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65206) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.23265)

Despite rapid advances in autonomous AI scientists powered by language models, generating publication-ready illustrations remains a labor-intensive bottleneck in the research workflow. To lift this burden, we introduce PaperBanana, an agentic framework for automated generation of publication-ready academic illustrations. Powered by state-of-the-art VLMs and image generation models, PaperBanana orchestrates specialized agents to retrieve references, plan content and style, render images, and iteratively refine...

### 9. DFlash: Block Diffusion for Flash Speculative Decoding

- Bucket: `high_visibility_artifact`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64301) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.06036)

Autoregressive large language models (LLMs) deliver strong performance but require inherently sequential decoding, leading to high inference latency and poor GPU utilization. Speculative decoding mitigates this bottleneck by using a fast draft model whose outputs are verified in parallel by the target LLM. However, existing methods still rely on *autoregressive drafting*, which remains sequential and constrains practical speedups. Diffusion LLMs offer a promising alternative by enabling parallel generation, but...

### 10. Boosting Monocular Metric Depth Estimation via Bokeh Rendering

- Bucket: `high_risk_artifact`
- Keyword hits: code; artifact
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65700) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.12425)

Bokeh rendering and depth estimation share a fundamental optical connection, yet existing methods fail to fully exploit this reciprocity. Conventional bokeh pipelines rely heavily on noisy depth maps that inevitably introduce visual artifacts. Conversely, existing monocular depth models typically follow two flawed paradigms. Generative diffusion-based frameworks often lack consistent metric scale. Meanwhile, feed-forward metric depth models frequently fail in textureless or distant regions where defocus blur...

### 11. AudioChat: Unified Audio Storytelling, Editing, and Understanding with Transfusion Forcing

- Bucket: `high_risk_artifact`
- Keyword hits: github
- URLs: [ICML](https://icml.cc/virtual/2026/poster/66763) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.17097)

Despite recent breakthroughs, audio foundation models struggle in processing complex multi-source acoustic scenes. We refer to this challenging domain as audio stories, which can have multiple speakers and background/foreground sound effects. Compared to traditional audio processing tasks, audio stories introduce new layers of semantic, temporal, and physical complexity. To address this challenge, we propose AudioChat, a framework for developing audio foundation models that can generate, edit, and understand...

### 12. From Correspondence to Actions: Human-Like Multi-Image Spatial Reasoning in Multi-modal Large Language Models

- Bucket: `high_risk_artifact`
- Keyword hits: benchmark
- URLs: [ICML](https://icml.cc/virtual/2026/poster/60836) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.08735)

While multimodal large language models (MLLMs) have made substantial progress in single-image spatial reasoning, multi-image spatial reasoning, which requires integration of information from multiple viewpoints, remains challenging. Cognitive studies suggest that humans address such tasks through two mechanisms: *cross-view correspondence*, which identifies regions across different views that correspond to the same physical locations, and *stepwise viewpoint transformation*, which composes relative viewpoint...

### 13. LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model

- Bucket: `high_risk_artifact`
- Keyword hits: none
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61887) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.05248)

Vision-Language-Action (VLA) models have recently shown strong generalization, with some approaches seeking to explicitly generate linguistic reasoning traces or predict future observations prior to execution. However, explicit reasoning typically incurs non-negligible inference latency, which constrains the temporal resolution required for robotic manipulation. Moreover, such reasoning is confined to the linguistic space, imposing a representational bottleneck that struggles to faithfully capture ineffable...

### 14. Hydra-Nav: Object Navigation via Adaptive Dual-Process Reasoning

- Bucket: `high_risk_artifact`
- Keyword hits: benchmark
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61357) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.09972)

While large vision-language models (VLMs) show promise for object goal navigation, current methods still struggle with low success rates and inefficient localization of unseen objects—failures primarily attributed to weak temporal-spatial reasoning. Meanwhile, recent attempts to inject reasoning into VLM-based agents improve success rates but incur substantial computational overhead. To address both the ineffectiveness and inefficiency of existing approaches, we introduce Hydra-Nav, a unified VLM architecture...

### 15. Turbo4DGen: Ultra-Fast Acceleration for 4D Generation

- Bucket: `high_visibility_artifact`
- Keyword hits: dataset
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62276) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.29572)

4D generation, or dynamic 3D content generation, integrates spatial, temporal, and view dimensions to model realistic dynamic scenes, playing a foundational role in advancing world models and physical AI. However, maintaining long-chain consistency across both frames and viewpoints through the unique spatio-camera-motion (SCM) attention mechanism introduces substantial computational and memory overhead, often leading to out-of-memory (OOM) failures and prohibitive generation times. To address these challenges,...

### 16. DeepAnalyze: Agentic Large Language Models for Autonomous Data Science

- Bucket: `high_visibility_artifact`
- Keyword hits: benchmark
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61106) / [AlphaXiv](https://www.alphaxiv.org/abs/2510.16872)

Autonomous data science on the structured data has been a long-standing challenge, and is now becoming feasible with the emergence of powerful large language models (LLMs). Recent workflowbased data agents have shown promising results on specific data tasks but remain fundamentally limited in achieving full autonomy due to their reliance on predefined workflows. In this paper, we introduce DeepAnalyze, the first agentic LLM for autonomous data science, capable of automatically completing the end-to-end data...
