# C05: Neighboring-venue contrast Evidence Dossier

This is an abstract/title-based pre-review aid. It does not fill or replace the manual validation fields.

## Claim

Multimodal/vision is large inside ICML 2026 but underweight relative to NeurIPS 2025 and ICLR 2026 accepted-paper baselines.

- Strength label: `moderate`
- Evidence summary: 889 taxonomy papers (13.4%); historical delta -3.1 pp, relative 0.82x.
- Caveat: This is the area most sensitive to venue scope and title/topic classification; ICLR/NeurIPS vision-heavy shares may dominate the baseline average.
- Next validation: Break multimodal into vision-language reasoning, video, 3D, and robustness before interpreting the aggregate underweight.
- Manual review progress: 0/14 rows reviewed; 14 remaining

## Pre-Review Summary

- Bucket mix: possible_support: 14
- Selection mix: multimodal_high_attention: 10, multimodal_subarea_anchor: 4
- Area mix: Multimodal, Vision, and Perception: 14

## Adjudication Questions

- Does the abstract directly support the claim, or only share vocabulary with the claim?
- Is the assigned taxonomy area central to the paper, or just one application/context?
- If the paper is high-attention, is the attention driven by a reusable result, a benchmark, a demo, or a social trend?
- If the paper has a GitHub link, is it a real paper artifact and what reproduction claim can be safely made?

## Papers To Read First

- **Motion Attribution for Video Generation** (`possible_support`; Outstanding Paper Honorable Mention, oral): Keyword overlap with the claim, but human reading is needed.
- **Bad Seeing or Bad Thinking? Rewarding Perception for Multimodal Reasoning** (`possible_support`; oral): Keyword overlap with the claim, but human reading is needed.
- **Mind Your Margin and Boundary: Are Your Distilled Datasets Truly Robust?** (`possible_support`; oral, taxonomy-review): Keyword overlap with the claim, but human reading is needed.
- **Multimodal Nested Learning for Decoupled and Coordinated Optimization** (`possible_support`; oral): Keyword overlap with the claim, but human reading is needed.
- **A Very Big Video Reasoning Suite** (`possible_support`; github): Keyword overlap with the claim, but human reading is needed.
- **Causal-JEPA: Learning World Models through Object-Level Latent Interventions** (`possible_support`; github): Keyword overlap with the claim, but human reading is needed.

## Paper-Level Pre-Review

| Rank | Paper | Bucket | Area | Signals | Why It Matters |
| ---: | --- | --- | --- | --- | --- |
| 1 | Motion Attribution for Video Generation | possible_support | Multimodal, Vision, and Perception | Outstanding Paper Honorable Mention; oral; votes=67 | Keyword overlap with the claim, but human reading is needed. |
| 2 | Bad Seeing or Bad Thinking? Rewarding Perception for Multimodal Reasoning | possible_support | Multimodal, Vision, and Perception | oral; votes=21 | Keyword overlap with the claim, but human reading is needed. |
| 3 | Mind Your Margin and Boundary: Are Your Distilled Datasets Truly Robust? | possible_support | Multimodal, Vision, and Perception | oral; votes=2; taxonomy-review | Keyword overlap with the claim, but human reading is needed. |
| 4 | Multimodal Nested Learning for Decoupled and Coordinated Optimization | possible_support | Multimodal, Vision, and Perception | oral; votes=0 | Keyword overlap with the claim, but human reading is needed. |
| 5 | A Very Big Video Reasoning Suite | possible_support | Multimodal, Vision, and Perception | votes=159; github_stars=25 | Keyword overlap with the claim, but human reading is needed. |
| 6 | Causal-JEPA: Learning World Models through Object-Level Latent Interventions | possible_support | Multimodal, Vision, and Perception | votes=150; github_stars=206 | Keyword overlap with the claim, but human reading is needed. |
| 7 | ExSkill: Continual Learning from Experience and Skills in Multimodal Agents | possible_support | Multimodal, Vision, and Perception | votes=147; github_stars=234 | Keyword overlap with the claim, but human reading is needed. |
| 8 | BabyVision: Visual Reasoning Beyond Language | possible_support | Multimodal, Vision, and Perception | votes=134; github_stars=227 | Keyword overlap with the claim, but human reading is needed. |
| 9 | Utonia: Toward One Encoder for All Point Clouds | possible_support | Multimodal, Vision, and Perception | votes=118; github_stars=710 | Keyword overlap with the claim, but human reading is needed. |
| 10 | World-R1: Reinforcing 3D Constraints for Text-to-Video Generation | possible_support | Multimodal, Vision, and Perception | votes=116; github_stars=406 | Keyword overlap with the claim, but human reading is needed. |
| 11 | DiffThinker: Towards Generative Multimodal Reasoning with Diffusion Models | possible_support | Multimodal, Vision, and Perception | votes=111; github_stars=186 | Keyword overlap with the claim, but human reading is needed. |
| 12 | WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling | possible_support | Multimodal, Vision, and Perception | votes=98 | Keyword overlap with the claim, but human reading is needed. |
| 13 | Self-Refining Video Sampling | possible_support | Multimodal, Vision, and Perception | votes=81; github_stars=181 | Keyword overlap with the claim, but human reading is needed. |
| 14 | Zooming without Zooming: Region-to-Image Distillation for Fine-Grained Multimodal Perception | possible_support | Multimodal, Vision, and Perception | votes=67; github_stars=169 | Keyword overlap with the claim, but human reading is needed. |

## Abstract Excerpts

### 1. Motion Attribution for Video Generation

- Bucket: `possible_support`
- Keyword hits: vision; video
- URLs: [ICML](https://icml.cc/virtual/2026/poster/60542) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.08828)

Despite the rapid progress of video generation models, the role of data in influencing motion is poorly understood. We present Motive (MOTIon attribution for Video gEneration), a motion-centric, gradient-based data attribution framework that scales to modern, large, high-quality video datasets and models. We use this to study which fine-tuning clips improve or degrade temporal dynamics. Motive isolates temporal dynamics from static appearance via motion-weighted loss masks, yielding efficient and scalable...

### 2. Bad Seeing or Bad Thinking? Rewarding Perception for Multimodal Reasoning

- Bucket: `possible_support`
- Keyword hits: vision; multimodal; video; perception
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62726) / [AlphaXiv](https://www.alphaxiv.org/abs/2605.14054)

Achieving robust perception-reasoning synergy is a central goal for advanced Vision-Language Models (VLMs). Recent advancements have pursued this goal via architectural designs or agentic workflows. However, these approaches are often limited by static textual reasoning or complicated by the significant compute and engineering burden of external agentic complexity. Worse, this heavy investment does not yield proportional gains, often witnessing a "seesaw effect" on perception and reasoning. This motivates a...

### 3. Mind Your Margin and Boundary: Are Your Distilled Datasets Truly Robust?

- Bucket: `possible_support`
- Keyword hits: vision; video; image
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63330) / [AlphaXiv](https://www.alphaxiv.org/abs/2605.20606)

Dataset distillation (DD) compresses a large training set into a small synthetic set for efficient training, but most DD methods optimize only clean accuracy and leave robustness uncontrolled. Recent robust DD methods improve robustness, yet they often suffer from a poor accuracy–robustness trade-off because they (i) treat all adversarially perturbed examples uniformly, despite robust risk being dominated by near-zero robust margins, and (ii) do not explicitly increase inter-class separation in the decision...

### 4. Multimodal Nested Learning for Decoupled and Coordinated Optimization

- Bucket: `possible_support`
- Keyword hits: multimodal; perception
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65954)

Multimodal learning aims to integrate multi-sensor data to exploit their complementary information, embracing a more comprehensive real-world perception and understanding. However, heterogeneous discrepancies across modalities consistently trigger imbalanced multimodal optimization, restricting the joint learning performance. Although existing methods mitigate this issue through optimization modulation and conflict alleviation, they still suffer from entangled optimization and uniform learning pace in...

### 5. A Very Big Video Reasoning Suite

- Bucket: `possible_support`
- Keyword hits: vision; video
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65709) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.20159)

Video reasoning grounds intelligence in spatiotemporally consistent visual environments that go beyond what text can naturally capture, enabling intuitive reasoning over motion, interaction, and causality. Rapid progress in video models has focused primarily on visual quality. Systematically studying video reasoning and its scaling behavior suffers from a lack of video reasoning (training) data. To address this gap, we introduce the Very Big Video Reasoning (VBVR) Dataset, an unprecedentedly large-scale...

### 6. Causal-JEPA: Learning World Models through Object-Level Latent Interventions

- Bucket: `possible_support`
- Keyword hits: vision; video; image
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63623) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.11389)

World models require robust relational understanding to support prediction, reasoning, and control. While object-centric representations provide a useful abstraction, they are not sufficient to capture interaction-dependent dynamics. We therefore propose C-JEPA, a simple and flexible object-centric world model that extends masked joint embedding prediction from image patches to object-centric representations. By applying object-level masking that requires an object’s state to be inferred from other objects,...

### 7. ExSkill: Continual Learning from Experience and Skills in Multimodal Agents

- Bucket: `possible_support`
- Keyword hits: multimodal
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65729) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.12056)

Multimodal agents demonstrate impressive problem-solving capabilities but typically operate in isolated episodes without leveraging past experiences. Recent methods address this through dynamic retrieval of textual insights or predefined skill documents, yet face critical challenges: visual modalities are neglected during knowledge extraction, stored insights lack executable structure, and manually crafted skills fail to scale. We propose \textsc{ExSkill}, a framework combining task-level Skills (structured...

### 8. BabyVision: Visual Reasoning Beyond Language

- Bucket: `possible_support`
- Keyword hits: vision; multimodal; perception
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63195) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.06521)

While humans develop core visual skills long before acquiring language, contemporary Multimodal LLMs (MLLMs) still rely heavily on linguistic priors to compensate for their fragile visual understanding. We uncovered a crucial fact: state-of-the-art MLLMs consistently fail on basic visual tasks that humans, even 3-year-olds, can solve effortlessly. To systematically investigate this gap, we introduce BabyVision, a benchmark designed to assess core visual abilities independent of linguistic knowledge for MLLMs....

### 9. Utonia: Toward One Encoder for All Point Clouds

- Bucket: `possible_support`
- Keyword hits: vision; multimodal; video; 3d; perception; spatial
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62613) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.03283)

We dream of a future where point clouds from all domains can come together to shape a single model that benefits them all. Toward this goal, we present Utonia, a first step toward training a single self-supervised point transformer encoder across heterogeneous domains, spanning remote sensing, outdoor LiDAR, indoor RGB-D sequences, object-centric CAD models, and point clouds lifted from RGB-only videos. Despite their distinct sensing geometries, densities, and priors, Utonia learns a consistent representation...

### 10. World-R1: Reinforcing 3D Constraints for Text-to-Video Generation

- Bucket: `possible_support`
- Keyword hits: vision; video; 3d
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61916) / [AlphaXiv](https://www.alphaxiv.org/abs/2604.24764)

Recent video foundation models demonstrate impressive visual synthesis but frequently suffer from geometric inconsistencies. While existing methods attempt to inject 3D priors via architectural modifications, they often incur high computational costs and limit scalability. We propose World-R1, a framework that aligns video generation with 3D constraints through reinforcement learning. To facilitate this alignment, we introduce a specialized pure text dataset tailored for world simulation. Utilizing Flow-GRPO,...

### 11. DiffThinker: Towards Generative Multimodal Reasoning with Diffusion Models

- Bucket: `possible_support`
- Keyword hits: vision; multimodal; video; image
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62143) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.24165)

While recent Multimodal Large Language Models (MLLMs) have attained significant strides in multimodal reasoning, their reasoning processes remain predominantly text-centric and fail to visualize and track intermediate visual states during the reasoning process, leading to suboptimal performance in complex long-horizon, vision-centric tasks. Moving beyond the constraints of text-centric reasoning, we establish Generative Multimodal Reasoning as a novel paradigm and introduce DiffThinker, a diffusion-based...

### 12. WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling

- Bucket: `possible_support`
- Keyword hits: vision; video
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65111) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.14614)

This paper presents WorldPlay, a streaming video diffusion model that enables real-time, interactive world modeling with long-term geometric consistency, resolving the trade-off between speed and memory that limits current methods. WorldPlay draws power from three key innovations. 1) We use a Dual Action Representation to enable robust action control in response to the user's keyboard and mouse inputs. 2) To enforce long-term consistency, our Reconstituted Context Memory dynamically rebuilds context from past...

### 13. Self-Refining Video Sampling

- Bucket: `possible_support`
- Keyword hits: vision; video
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61169) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.18577)

Modern video generators still struggle with complex physical dynamics, often falling short of physical realism. Existing approaches address this using external verifiers or additional training on augmented data, which is computationally expensive and still limited in capturing fine-grained motion. In this work, we present self-refining video sampling, a simple method that uses a pre-trained video generator trained on large-scale datasets as its own self-refiner. By interpreting the generator as a denoising...

### 14. Zooming without Zooming: Region-to-Image Distillation for Fine-Grained Multimodal Perception

- Bucket: `possible_support`
- Keyword hits: vision; multimodal; video; perception; image
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62952) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.11858)

Multimodal Large Language Models (MLLMs) excel at broad visual understanding but still struggle with fine-grained perception, where decisive evidence is small and easily overwhelmed by global context. Recent "Thinking-with-Images" methods alleviate this by iteratively zooming into regions of interest during inference, but incur high latency due to repeated tool calls and visual re-encoding. To address this, we propose Region-to-Image Distillation, which transforms zooming from an inference-time tool into a...
