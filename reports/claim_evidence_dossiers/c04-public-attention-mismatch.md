# C04: Public attention mismatch Evidence Dossier

This is an abstract/title-based pre-review aid. It does not fill or replace the manual validation fields.

## Claim

Robotics/embodiment is small by taxonomy count but unusually strong in public attention.

- Strength label: `moderate`
- Evidence summary: 195 papers (2.9%); public-attention enrichment 2.11x vs oral enrichment 0.81x.
- Caveat: AlphaXiv likely overweights shareable VLA/world-model work and project-page traffic.
- Next validation: Inspect whether the high-attention papers are benchmarks, demos, or reusable models rather than core ICML program emphasis.
- Manual review progress: 0/12 rows reviewed; 12 remaining

## Pre-Review Summary

- Bucket mix: possible_support: 12
- Selection mix: robotics_public_not_program: 9, robotics_program_anchor: 3
- Area mix: Robotics, Embodiment, and World Models: 12

## Adjudication Questions

- Does the abstract directly support the claim, or only share vocabulary with the claim?
- Is the assigned taxonomy area central to the paper, or just one application/context?
- If the paper is high-attention, is the attention driven by a reusable result, a benchmark, a demo, or a social trend?
- If the paper has a GitHub link, is it a real paper artifact and what reproduction claim can be safely made?

## Papers To Read First

- **RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies** (`possible_support`; oral, github): Keyword overlap with the claim, but human reading is needed.
- **From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models** (`possible_support`; oral, github): Keyword overlap with the claim, but human reading is needed.
- **XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations** (`possible_support`; oral): Keyword overlap with the claim, but human reading is needed.
- **Learning Latent Action World Models In The Wild** (`possible_support`; no flags): Keyword overlap with the claim, but human reading is needed.
- **Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies** (`possible_support`; github): Keyword overlap with the claim, but human reading is needed.
- **Temporal Straightening for Latent Planning** (`possible_support`; github): Keyword overlap with the claim, but human reading is needed.

## Paper-Level Pre-Review

| Rank | Paper | Bucket | Area | Signals | Why It Matters |
| ---: | --- | --- | --- | --- | --- |
| 1 | Learning Latent Action World Models In The Wild | possible_support | Robotics, Embodiment, and World Models | votes=273 | Keyword overlap with the claim, but human reading is needed. |
| 2 | Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies | possible_support | Robotics, Embodiment, and World Models | votes=204; github_stars=69 | Keyword overlap with the claim, but human reading is needed. |
| 3 | Temporal Straightening for Latent Planning | possible_support | Robotics, Embodiment, and World Models | votes=202; github_stars=92 | Keyword overlap with the claim, but human reading is needed. |
| 4 | LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries | possible_support | Robotics, Embodiment, and World Models | votes=189; github_stars=69 | Keyword overlap with the claim, but human reading is needed. |
| 5 | Vision-Language-Action Pretraining from Large-Scale Human Videos | possible_support | Robotics, Embodiment, and World Models | votes=144; github_stars=52 | Keyword overlap with the claim, but human reading is needed. |
| 6 | World Guidance: World Modeling in Condition Space for Action Generation | possible_support | Robotics, Embodiment, and World Models | votes=108; github_stars=147 | Keyword overlap with the claim, but human reading is needed. |
| 7 | RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation | possible_support | Robotics, Embodiment, and World Models | votes=91; github_stars=2562 | Keyword overlap with the claim, but human reading is needed. |
| 8 | CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation | possible_support | Robotics, Embodiment, and World Models | votes=86 | Keyword overlap with the claim, but human reading is needed. |
| 9 | RDT2: Exploring the Scaling Limit of UMI Data Towards Zero-Shot Cross-Embodiment Generalization | possible_support | Robotics, Embodiment, and World Models | votes=86; github_stars=792 | Keyword overlap with the claim, but human reading is needed. |
| 10 | RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies | possible_support | Robotics, Embodiment, and World Models | oral; votes=66; github_stars=31 | Keyword overlap with the claim, but human reading is needed. |
| 11 | From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models | possible_support | Robotics, Embodiment, and World Models | oral; votes=30; github_stars=35 | Keyword overlap with the claim, but human reading is needed. |
| 12 | XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations | possible_support | Robotics, Embodiment, and World Models | oral; votes=19 | Keyword overlap with the claim, but human reading is needed. |

## Abstract Excerpts

### 1. Learning Latent Action World Models In The Wild

- Bucket: `possible_support`
- Keyword hits: robot; embodied; world model; policy; simulation
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65056) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.05230)

Agents that can reason and plan in the real world must be able to predict the consequences of their actions. World models possess this capability but require action annotations that can be complex to obtain at scale. Latent action models address this issue by learning an action space from videos alone. Our work studies the training of latent action world models on in-the-wild videos, expanding the scope of existing works that focus on simple robotics simulations, video games, or manipulation data. While diverse...

### 2. Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies

- Bucket: `possible_support`
- Keyword hits: robot; embodied; vision-language-action; vla; policy
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62902) / [AlphaXiv](https://www.alphaxiv.org/abs/2508.20072)

Vision–Language–Action (VLA) models adapt large vision–language backbones to map images and instructions into robot actions. However, prevailing VLAs either generate actions autoregressively in a fixed left-to-right order or attach separate diffusion heads outside the backbone, fragmenting information pathways and hindering unified, scalable architectures. We present Discrete Diffusion VLA, a unified-transformer policy that models discretized action chunks with discrete diffusion retaining progressive...

### 3. Temporal Straightening for Latent Planning

- Bucket: `possible_support`
- Keyword hits: world model
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64904) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.12231)

Learning good representations is essential for latent planning with world models. While pretrained visual encoders provide strong visual features, they are not tailored to planning and contain substantial information which is irrelevant to planning. Inspired by the perceptual straightening hypothesis in human visual processing, we introduce temporal straightening for representation learning in latent planning. We add a lightweight projector on top of a pretrained visual encoder to map to a lower-dimensional...

### 4. LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries

- Bucket: `possible_support`
- Keyword hits: robot; embodied; vision-language-action; vla; policy
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65457) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.15197)

Vision-Language-Action (VLA) models have shown promise in robot manipulation but often struggle to generalize to new instructions or complex multi-task scenarios. We identify a critical pathology in current training paradigms where goal-driven data collection creates a dataset bias. In such datasets, language instructions are highly predictable from visual observations alone, causing the conditional mutual information between instructions and actions to vanish, a phenomenon we term Information Collapse....

### 5. Vision-Language-Action Pretraining from Large-Scale Human Videos

- Bucket: `possible_support`
- Keyword hits: robot; embodied; vision-language-action; vla
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62813) / [AlphaXiv](https://www.alphaxiv.org/abs/2507.15597)

Existing Vision-Language-Action (VLA) models struggle with complex manipulation tasks requiring high dexterity and generalization, primarily due to their reliance on synthetic data with significant sim-to-real gaps or limited teleoperated demonstrations. To address this bottleneck, we propose leveraging human hands as a manipulator template, capitalizing on the rich dexterity and scalability present in web data of human manipulation. Our approach introduces physical instruction tuning, a novel training paradigm...

### 6. World Guidance: World Modeling in Condition Space for Action Generation

- Bucket: `possible_support`
- Keyword hits: robot; embodied; world model; vision-language-action; vla; simulation
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61757) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.22010)

Leveraging future observation modeling to facilitate action generation presents a promising avenue for enhancing the capabilities of Vision-Language-Action (VLA) models. However, existing approaches struggle to strike a balance between maintaining efficient, predictable future representations and preserving sufficient fine-grained information to guide precise action generation. To address this limitation, we propose WoG (World Guidance), a framework that maps future observations into compact conditions by...

### 7. RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation

- Bucket: `possible_support`
- Keyword hits: robot; embodied; vision-language-action; vla; simulation
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62192) / [AlphaXiv](https://www.alphaxiv.org/abs/2506.18088)

Simulation-based data synthesis has emerged as a powerful paradigm for enhancing real-world robotic manipulation. However, existing synthetic datasets remain insufficient for robust bimanual manipulation due to two key challenges: (1) the lack of an autonomous self-correcting mechanism to resolve execution failures in complex coordination tasks, and (2) the scarcity of diverse visual and spatial variations required to bridge the sim-to-real gap. To this end, we present RoboTwin 2.0, a scalable simulation...

### 8. CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation

- Bucket: `possible_support`
- Keyword hits: robot; embodied; vla; policy; simulation
- URLs: [ICML](https://icml.cc/virtual/2026/poster/66369) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.22435)

“Code-as-Policy” considers how executable code can complement data-intensive Vision-LanguageAction (VLA) methods, yet their effectiveness as autonomous controllers for embodied manipulation remains underexplored. We present CaPX, an open-access framework for systematically studying Code-as-Policy agents in robot manipulation. At its core is CaP-Gym, an interactive environment in which agents control robots by synthesizing and executing programs that compose perception and control primitives. Building on this...

### 9. RDT2: Exploring the Scaling Limit of UMI Data Towards Zero-Shot Cross-Embodiment Generalization

- Bucket: `possible_support`
- Keyword hits: robot; embodied; vision-language-action; vla
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65782) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.03310)

Vision-Language-Action (VLA) models hold promise for generalist robotics but currently struggle with data scarcity, architectural inefficiencies, and the inability to generalize across different hardware platforms. We introduce RDT2, a robotic foundation model built upon a 7B parameter VLM designed to enable zero-shot deployment on novel embodiments for open-vocabulary tasks. To achieve this, we collected one of the largest open-source robotic datasets—over $10,000$ hours of demonstrations in diverse...

### 10. RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies

- Bucket: `possible_support`
- Keyword hits: robot; embodied; vision-language-action; vla
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65933) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.04639)

Memory is critical for long-horizon and history-dependent robotic manipulation. Such tasks often involve counting repeated actions or manipulating objects that become temporarily occluded. Recent vision-language-action (VLA) models have begun to incorporate memory mechanisms; however, their evaluations remain confined to narrow, non-standardized settings. This limits their systematic understanding, comparison, and progress measurement. To address these challenges, we introduce **RoboMME**: a large-scale...

### 11. From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models

- Bucket: `possible_support`
- Keyword hits: robot; embodied; vision-language-action; vla
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63621) / [AlphaXiv](https://www.alphaxiv.org/abs/2605.04678)

Latent actions serve as an intermediate representation that enables consistent modeling of vision-language-action (VLA) models across heterogeneous datasets. However, approaches to supervising VLAs with latent actions are fragmented and lack a systematic comparison. This work structures the study of latent action supervision from two perspectives: (i) regularizing the trajectory via image-based latent actions, and (ii) unifying the target space with action-based latent actions. Under a unified VLA baseline, we...

### 12. XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations

- Bucket: `possible_support`
- Keyword hits: robot; embodied; vision-language-action; vla; policy
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64826) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.02776)

Recent progress in large-scale robotic datasets and vision-language models (VLMs) has advanced research on vision-language-action (VLA) models. However, existing VLA models still face two fundamental challenges: (\textit{i}) producing precise low-level actions from high-dimensional observations, (\textit{ii}) bridging domain gaps across heterogeneous data sources, including diverse robot embodiments and human demonstrations. Existing methods often encode latent variables from either visual dynamics or robotic...
