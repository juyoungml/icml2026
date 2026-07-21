# Multimodal, Vision, and Perception

Manual validation packet for representative and boundary papers.

## Area Context

Headline: Vision-language work is moving from recognition toward grounded reasoning, spatial understanding, and video/world structure.

Fault lines:
- Perception as feature extraction versus perception as an active reasoning bottleneck.
- Static image benchmarks versus long-video, 3D, spatial, and embodied settings.
- Generative visual models versus discriminative robustness and hallucination control.

What to read for:
- Can the method localize the visual evidence behind an answer?
- Does it evaluate temporal, 3D, or physical consistency rather than only caption-style accuracy?
- Are robustness claims tested under realistic corruptions, adversarial prompts, and distribution shift?

## Queue Summary

- Papers: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, program_signal_low_public_attention=4, taxonomy_boundary_cluster=2
- Papers from taxonomy-review clusters: 4
- Papers with GitHub URLs: 8

## Papers

### 1. Motion Attribution for Video Generation

Flags: fault_line_representative, oral, Outstanding Paper Honorable Mention

- Subarea: 3D, video, motion, and spatial understanding
- Votes: 67
- ICML URL: https://icml.cc/virtual/2026/poster/60542
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.08828
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; Method / algorithm
- Method families: LLM post-training; Causal / data-centric
- Evaluation settings: vision/video; language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: VBench
- Datasets: none
- Metrics: win_rate

Abstract:

Despite the rapid progress of video generation models, the role of data in influencing motion is poorly understood. We present Motive (MOTIon attribution for Video gEneration), a motion-centric, gradient-based data attribution framework that scales to modern, large, high-quality video datasets and models. We use this to study which fine-tuning clips improve or degrade temporal dynamics. Motive isolates temporal dynamics from static appearance via motion-weighted loss masks, yielding efficient and scalable motion-specific influence computation. On text-to-video models, Motive identifies clips that strongly affect motion and guides data curation that improves temporal consistency and physical plausibility. With Motive-selected high-influence data, we improve both motion smoothness and dynamic degree on VBench, achieving a 74.1% human preference win rate compared with the pretrained base model. To our knowledge, this is the first framework to attribute motion rather than visual appearance in video generative models and to use it to curate fine-tuning data.

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

### 2. Holi-Spatial: Evolving Video Streams into Holistic 3D Spatial Intelligence

Flags: fault_line_representative, oral, github

- Subarea: 3D, video, motion, and spatial understanding
- Votes: 52
- ICML URL: https://icml.cc/virtual/2026/poster/63725
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.07660
- GitHub URL: https://github.com/Visionary-Laboratory/Holi-Spatial
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; Theory / proof; Method / algorithm
- Method families: LLM post-training; Reasoning / test-time compute; Agents / tool use; Graphs / geometry
- Evaluation settings: vision/video; language/llm
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

The pursuit of spatial intelligence fundamentally relies on access to large-scale, fine-grained 3D data. However, existing approaches predominantly construct spatial understanding benchmarks by generating question–answer (QA) pairs from a limited number of manually annotated datasets, rather than systematically annotating new large-scale 3D scenes from raw web data. As a result, their scalability is severely constrained, and model performance is further hindered by domain gaps inherent in these narrowly curated datasets. In this work, we propose \textbf{Holi-Spatial}, the first fully automated, large-scale, spatially-aware multimodal dataset, constructed from raw video inputs without human intervention, using the proposed data curation pipeline. Holi-Spatial supports multi-level spatial supervision, ranging from geometrically accurate 3D Gaussian Splatting (3DGS) reconstructions with rendered depth maps to object-level and relational semantic annotations, together with corresponding spatial Question–Answer (QA) pairs. Following a principled and systematic pipeline, we further construct \textbf{Holi-Spatial-4M}, the first large-scale, high-quality 3D semantic dataset, containing 12K optimized 3DGS scenes, 1.3M 2D masks, 320K 3D bounding boxes, 320K instance captions, 1.2M 3D grounding instances, and 1.2M spatial QA pairs spanning diverse geometric, relational, and semantic reasoning tasks. Holi-Spatial demonstrates exceptional performance in data curation quality, significantly outperforming existing feed-forward and per-scene optimized methods on datasets such as ScanNet, ScanNet++, and DL3DV. Furthermore, fine-tuning Vision-Language Models (VLMs) on spatial reasoning tasks using this dataset has also led to substantial improvements in model performance.

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

### 3. Bad Seeing or Bad Thinking? Rewarding Perception for Multimodal Reasoning

Flags: fault_line_representative, oral

- Subarea: Vision-language reasoning and video understanding
- Votes: 21
- ICML URL: https://icml.cc/virtual/2026/poster/62726
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.14054
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Theory / proof; Method / algorithm
- Method families: RL / policy optimization; Reasoning / test-time compute; Agents / tool use
- Evaluation settings: vision/video; language/llm
- Result claim cues: negative / limitation; scaling / efficiency; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: reward

Abstract:

Achieving robust perception-reasoning synergy is a central goal for advanced Vision-Language Models (VLMs). Recent advancements have pursued this goal via architectural designs or agentic workflows. However, these approaches are often limited by static textual reasoning or complicated by the significant compute and engineering burden of external agentic complexity. Worse, this heavy investment does not yield proportional gains, often witnessing a "seesaw effect" on perception and reasoning. This motivates a fundamental rethinking of the true bottleneck. In this paper, we argue that the root cause of this trade-off is an ambiguity in modality credit assignment: when a VLM fails, is it due to flawed perception ("bad seeing") or flawed logic ("bad thinking")? To resolve this, we introduce a reinforcement learning framework that improves perception-reasoning synergy by reliably rewarding the perception fidelity. We explicitly decompose the generation process into interleaved perception and reasoning steps. This decoupling enables targeted supervision on perception. Crucially, we introduce Perception Verification (PV), leveraging a "blindfolded reasoning" proxy to reward perceptual fidelity independently of reasoning outcomes. Furthermore, to scale training across free-form VL tasks, we propose Structured Verbal Verification, which replaces high-variance LLM judging with structured algorithmic execution. These techniques are integrated into a Modality-Aware Credit Assignment (MoCA) mechanism, which routes rewards to the specific source of error -- either bad seeing or bad thinking -- enabling a single VLM to achieve simultaneous performance gains across a wide task spectrum.

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

### 4. Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination

Flags: fault_line_representative, oral, github

- Subarea: Vision-language reasoning and video understanding
- Votes: 16
- ICML URL: https://icml.cc/virtual/2026/poster/65441
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.15864
- GitHub URL: https://github.com/visualswap/visualswap
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Method / algorithm
- Method families: Reasoning / test-time compute; Transformer / attention
- Evaluation settings: vision/video; language/llm
- Result claim cues: negative / limitation; scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: accuracy

Abstract:

Vision-Language Models (VLMs) frequently generate self-reflective statements during reasoning, such as ``let me check the figure again.'' Do such statements trigger genuine visual re-examination, or merely represent learned textual patterns? We investigate this question through VisualSwap, an image-swap probing framework: after a model generates reasoning for an image, we replace it with a visually similar but semantically different image and test whether the model detects the change. We introduce VS-Bench, a benchmark of $800$ image pairs curated from MathVista, MathVerse, MathVision, and MMMU-Pro. Experiments across Qwen3-VL, Kimi-VL, and ERNIE-VL families reveal a striking failure: models overwhelmingly fail to detect image changes, with accuracy dropping by up to 60\%. Counterintuitively, thinking models exhibit nearly 3$\times$ greater vulnerability than their instructed counterparts, and scaling provides no mitigation. However, multi-turn interaction with user instructions can restore visual grounding, while self-generated reflective statements during continuous generation cannot. Attention analysis reveals the underlying mechanism: self-reflection does not increase attention to visual tokens, whereas user instructions substantially elevate it. Our findings reveal that current VLMs tend to say rather than actually see when claiming visual re-examination.

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

### 5. 3ViewSense: Spatial and Mental Perspective Reasoning from Orthographic Views in Vision-Language Models

Flags: fault_line_representative, oral

- Subarea: Vision-language reasoning and video understanding
- Votes: 11
- ICML URL: https://icml.cc/virtual/2026/poster/65015
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.07751
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Benchmark / evaluation; Method / algorithm
- Method families: Reasoning / test-time compute; Graphs / geometry
- Evaluation settings: vision/video; language/llm
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Current Large Language Models have achieved Olympiad-level logic, yet Vision-Language Models paradoxically falter on elementary spatial tasks like block counting. This capability mismatch reveals a critical "spatial intelligence gap," where models fail to construct coherent 3D mental representations from 2D observations. We uncover this gap via diagnostic analyses showing the bottleneck is a missing view-consistent spatial interface rather than insufficient visual features or weak reasoning. To bridge this, we introduce **3ViewSense**, a framework that grounds spatial reasoning in Orthographic Views. Drawing on engineering cognition, we propose a "Simulate-and-Reason" mechanism that decomposes complex scenes into canonical orthographic projections to resolve geometric ambiguities. By aligning egocentric perceptions with these allocentric references, our method facilitates explicit mental rotation and reconstruction. Empirical results on spatial reasoning benchmarks demonstrate that our method significantly outperforms existing baselines, with consistent gains on occlusion-heavy counting and view-consistent spatial reasoning. The framework also improves the stability and consistency of spatial descriptions, offering a scalable path toward stronger spatial intelligence in multimodal systems.

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

### 6. CLEAR: Context-Aware Learning with End-to-End Mask-Free Inference for Adaptive Subtitle Removal

Flags: fault_line_representative, oral, github

- Subarea: Vision-language reasoning and video understanding
- Votes: 2
- ICML URL: https://icml.cc/virtual/2026/poster/65005
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.21901
- GitHub URL: https://github.com/silent-commit/CLEAR
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Theory / proof; Method / algorithm
- Method families: LLM post-training; Diffusion / flow; Compression / efficiency
- Evaluation settings: vision/video; language/llm
- Result claim cues: negative / limitation; scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Video subtitle removal is essential for content localization and media re-editing, yet existing mask-guided diffusion methods face critical limitations: training inefficiency requiring extensive annotations and full model fine-tuning, inference complexity demanding explicit mask sequences, and static prior utilization unable to adapt to quality variations. We present CLEAR (Context-aware Learning for End-to-end Adaptive subtitle Removal), a lightweight adapter-based framework addressing these challenges through three technical innovations. First, self-supervised prior learning (Stage I) extracts occlusion guidance from video pairs using pixel differences as weak supervision, eliminating annotation dependency while learning generalizable subtitle features across languages. Second, LoRA-based adaptive refinement (Stage II) enables parameter-efficient training that preserves pre-trained visual priors while achieving true mask-free end-to-end inference without external detection modules. Third, adaptive focal weighting dynamically adjusts prior influence based on local quality assessment, effectively handling diverse subtitle styles and noisy guidance signals. Extensive experiments demonstrate CLEAR's superior performance in multilingual subtitle removal while requiring only 0.77% trainable parameters, establishing a new paradigm for efficient video text removal without inference-time mask dependencies.

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

### 7. A Very Big Video Reasoning Suite

Flags: public_attention_not_program_signal, github

- Subarea: Vision-language reasoning and video understanding
- Votes: 159
- ICML URL: https://icml.cc/virtual/2026/poster/65709
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.20159
- GitHub URL: https://github.com/Video-Reason/VBVR-Wan2.2
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; Method / algorithm
- Method families: Reasoning / test-time compute; Agents / tool use; Causal / data-centric
- Evaluation settings: math/code/verifiable; vision/video; language/llm
- Result claim cues: scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Video reasoning grounds intelligence in spatiotemporally consistent visual environments that go beyond what text can naturally capture, enabling intuitive reasoning over motion, interaction, and causality. Rapid progress in video models has focused primarily on visual quality. Systematically studying video reasoning and its scaling behavior suffers from a lack of video reasoning (training) data. To address this gap, we introduce the Very Big Video Reasoning (VBVR) Dataset, an unprecedentedly large-scale resource spanning 200 curated reasoning tasks and over one million video clips—approximately three orders of magnitude larger than existing datasets. We further present VBVR-Bench, a verifiable evaluation framework that moves beyond model-based judging by incorporating rule-based, human-aligned scorers, enabling reproducible and interpretable diagnosis of video reasoning capabilities. Leveraging the VBVR suite, we conduct one of the first large-scale scaling studies of video reasoning and observe early signs of emergent generalization to unseen reasoning tasks. Together, VBVR lays a foundation for the next stage of research in generalizable video reasoning. The data, toolkit, and models will be released publicly.

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

### 8. Causal-JEPA: Learning World Models through Object-Level Latent Interventions

Flags: public_attention_not_program_signal, github

- Subarea: Vision-language reasoning and video understanding
- Votes: 150
- ICML URL: https://icml.cc/virtual/2026/poster/63623
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.11389
- GitHub URL: https://github.com/galilai-group/cjepa
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: Reasoning / test-time compute; Agents / tool use; Causal / data-centric
- Evaluation settings: math/code/verifiable; vision/video; robotics/embodied; security/safety
- Result claim cues: scaling / efficiency; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

World models require robust relational understanding to support prediction, reasoning, and control. While object-centric representations provide a useful abstraction, they are not sufficient to capture interaction-dependent dynamics. We therefore propose C-JEPA, a simple and flexible object-centric world model that extends masked joint embedding prediction from image patches to object-centric representations. By applying object-level masking that requires an object’s state to be inferred from other objects, C-JEPA induces latent interventions with counterfactual-like effects and prevents shortcut solutions, making interaction reasoning essential. Empirically, C-JEPA leads to consistent gains in visual question answering, with an absolute improvement of about 20\% in counterfactual reasoning over the same architecture without object-level masking. On agent control tasks, C-JEPA enables substantially more efficient planning by using only 1\% of the total latent input features required by patch-based world models, while achieving comparable performance. Finally, we provide a formal analysis demonstrating that object-level masking induces a causal inductive bias via latent interventions. Code will be available at *anonymous*.

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

### 9. ExSkill: Continual Learning from Experience and Skills in Multimodal Agents

Flags: public_attention_not_program_signal, github

- Subarea: Multimodal representation and cross-modal alignment
- Votes: 147
- ICML URL: https://icml.cc/virtual/2026/poster/65729
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.12056
- GitHub URL: https://github.com/XSkill-Agent/XSkill
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Method / algorithm
- Method families: Reasoning / test-time compute; Agents / tool use
- Evaluation settings: robotics/embodied
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: accuracy

Abstract:

Multimodal agents demonstrate impressive problem-solving capabilities but typically operate in isolated episodes without leveraging past experiences. Recent methods address this through dynamic retrieval of textual insights or predefined skill documents, yet face critical challenges: visual modalities are neglected during knowledge extraction, stored insights lack executable structure, and manually crafted skills fail to scale. We propose \textsc{ExSkill}, a framework combining task-level Skills (structured workflows and tool templates) with action-level Experiences (context-specific tactical insights) through automated accumulation from agent trajectories. Our approach employs visually-grounded summarization to extract knowledge integrating visual observations and textual reasoning, hierarchical consolidation to maintain quality and diversity, and context-aware adaptation to tailor knowledge to current visual contexts. Evaluated on five diverse benchmarks spanning visual tool use and multimodal search, \textsc{ExSkill} achieves average gains of 4.1-6.5 points over strong baselines across different backbone models, with superior zero-shot transferability and strategic improvements in tool selection and execution accuracy. These results demonstrate that our framework enables transferable continual learning for multimodal agents in real-world scenarios without parametric training, offering broad applicability for practical deployment.

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

### 10. BabyVision: Visual Reasoning Beyond Language

Flags: public_attention_not_program_signal, github

- Subarea: Vision-language reasoning and video understanding
- Votes: 134
- ICML URL: https://icml.cc/virtual/2026/poster/63195
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.06521
- GitHub URL: https://github.com/UniPat-AI/BabyVision
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Application / domain study
- Method families: Reasoning / test-time compute; Agents / tool use
- Evaluation settings: math/code/verifiable; language/llm
- Result claim cues: negative / limitation; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

While humans develop core visual skills long before acquiring language, contemporary Multimodal LLMs (MLLMs) still rely heavily on linguistic priors to compensate for their fragile visual understanding. We uncovered a crucial fact: state-of-the-art MLLMs consistently fail on basic visual tasks that humans, even 3-year-olds, can solve effortlessly. To systematically investigate this gap, we introduce BabyVision, a benchmark designed to assess core visual abilities independent of linguistic knowledge for MLLMs. BabyVision spans a wide range of tasks, with 388 items divided into 22 subclasses across four key categories. Empirical results and human evaluation reveal that leading MLLMs perform significantly below human baselines. Gemini3-Pro-Preview scores 49.7, lagging behind 6-year-old humans and falling well behind the average adult score of 94.1. These results show despite excelling in knowledge-heavy evaluations, current MLLMs still lack fundamental visual primitives. Progress in BabyVision represents a step toward human-level visual perception and reasoning capabilities. We also explore solving visual reasoning with generation models by proposing Babyvision-Gen and automatic evaluation toolkit. Our code and benchmark data are released at https://anonymous.4open.science/r/BabyVision-E88F/ for reproduction.

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

### 11. Multimodal Nested Learning for Decoupled and Coordinated Optimization

Flags: program_signal_low_public_attention, oral, evidence-low

- Subarea: Multimodal representation and cross-modal alignment
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/65954
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; System / infrastructure; Method / algorithm
- Method families: none
- Evaluation settings: none
- Result claim cues: negative / limitation; scaling / efficiency; robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: memory

Abstract:

Multimodal learning aims to integrate multi-sensor data to exploit their complementary information, embracing a more comprehensive real-world perception and understanding. However, heterogeneous discrepancies across modalities consistently trigger imbalanced multimodal optimization, restricting the joint learning performance. Although existing methods mitigate this issue through optimization modulation and conflict alleviation, they still suffer from entangled optimization and uniform learning pace in conventional monolithic frameworks, limiting the effectiveness of multimodal learning. To address this issue, we propose a novel Multimodal Nested Learning Framework (MoNet), which reformulates the monolithic framework into nested sub-processes, decoupling and coordinating multimodal learning. To achieve this, we present a Decoupled Multimodal Stable Memory block (DMSM) as the outermost nested level, which decouples multimodal learning into independent optimization streams for semantic exploitation across modalities. Additionally, we develop an Adaptive Multimodal Coordinated Fusion block (AMCF), which constitutes the inner nested level. It attempts to coordinate multimodal information integration across multi-timescale nested memories, balancing multimodal fusion. Extensive experimental results on eight datasets across three tasks demonstrate the superiority of MoNet.

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

### 12. DroneDINO: Towards Heterogeneous Routed Mixture of Experts for Drone-based Unified Object Detection

Flags: program_signal_low_public_attention, oral, taxonomy-review

- Subarea: Vision robustness, detection, and adversarial perception
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/60907
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; Method / algorithm
- Method families: Compression / efficiency
- Evaluation settings: vision/video
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Recently, the rapid development of low-altitude aerial applications has driven the need for drone-based unified detectors. In contrast to task-specific detectors that suffer from poor scalability across diverse scenarios, existing unified detectors leverage the Mixture-of-Experts (MoE) architecture to learn task-aware features from diverse datasets. However, the imbalanced multi-task data distribution leads to over-activation of experts for dominant tasks and under-activation for others. To enable balanced feature learning, this paper combines three detection paradigms (RGB, IR, and RGB-IR) into a unified framework termed DroneDINO. DroneDINO extends DINO by introducing heterogeneous routed MoEs that organize experts into three functional groups: shared, task-specific, and dynamic. Unlike conventional dynamic experts where the top-$k$ experts are activated for each input, the shared expert is activated for all inputs, while each task-specific expert is activated exclusively for the matching task. To ensure inputs are routed to appropriate experts and yield task-discriminative features, we propose a task-recognition auxiliary training strategy to penalize features with low task-discriminability. Experiments demonstrate the effectiveness and generalizability of DroneDINO, which consistently outperforms state-of-the-art unified and task-specific detectors across multiple drone-based detection benchmarks.

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

### 13. Privacy-Aware Video Anomaly Detection: Guided Orthogonal Projection and a Comprehensive Evaluation Framework

Flags: program_signal_low_public_attention, oral, taxonomy-review

- Subarea: Vision robustness, detection, and adversarial perception
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/62535
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: LLM post-training
- Evaluation settings: vision/video; security/safety
- Result claim cues: robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: accuracy

Abstract:

Video anomaly detection (VAD) is critical for surveillance systems, but current methods prioritize accuracy while ignoring the ethical risks of encoding sensitive biometric information. This neglect poses significant privacy concerns for real-world deployment. To bridge this gap, we introduce the Guided Orthogonal Projection Layer (G-OPL), a lightweight module designed to geometrically decouple and suppress sensitive attributes from latent features to produce representations focused on anomaly-relevant cues. We specifically target facial information as the primary sensitive attribute. Unlike gait or body pose, faces act as unique biometric identifiers that are tightly regulated and pose immediate risks of misuse, yet are rarely necessary for identifying abnormal behaviors. To achieve this, G-OPL utilizes a stable, QR-decomposition-based orthogonal projection mechanism guided by weak supervision (e.g., face presence) to actively filter privacy-sensitive subspaces while preserving task-relevant anomalies. we further propose a novel privacy-aware evaluation framework to rigorously quantify the trade-off between model utility and ethical alignment. Our analysis uncovers how projection layers filter sensitive information, why this improves transparency, and under what conditions ethical design also enhances robustness. Extensive experiments demonstrate that our approach effectively minimizes privacy risks without compromising anomaly detection performance, offering a principled path toward trustworthy video analysis.

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

### 14. DOUBT: Decoupled Object-level Understanding and Bridging via vMF-based Trustworthiness for Hallucination Detection in MLLMs

Flags: program_signal_low_public_attention, oral

- Subarea: Vision-language reasoning and video understanding
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/64161
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Method / algorithm
- Method families: Reasoning / test-time compute
- Evaluation settings: vision/video; language/llm
- Result claim cues: robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Multimodal Large Language Models (MLLMs) frequently produce hallucinations (i.e., assertions that contradict the image or facts), undermining reliability in high-risk applications. Existing detection approaches typically feed images and texts jointly and estimate hallucination scores by measuring the consistency of model outputs. However, because the visual module often lags behind the language module in understanding and reasoning, MLLMs can repeatedly produce similar yet incorrect answers, yielding deceptively high measured trustworthiness and therefore missed detections. To address this, we propose a simple yet effective model-agnostic method, dubbed Decoupled Object-level Understanding and Bridging via vMF-based Trustworthiness (DOUBT). DOUBT i) elicits richer object-aware responses by decoupling object recognition from relational reasoning via a two-step prompting scheme (Object-level Understanding and Bridging, OUB), and ii) measures reliability with a von Mises–Fisher (vMF)-based trustworthiness metric that is more stable than semantic-entropy metrics under small-sample regimes. Specifically, OUB first prompts the model to list recognized objects, and then conditions chain-of-thought reasoning on those objects to produce object-bridged responses. For trustworthiness estimation, we replace conventional measures with the proposed vMF-based metric, which is robust even under low-sample settings and exhibits smoother behavior than prior techniques. Extensive experiments and ablation studies across multiple benchmarks demonstrate that DOUBT consistently outperforms state-of-the-art baselines, offering a robust and generalizable solution for hallucination detection in MLLMs.

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

### 15. Rectified LpJEPA: Joint-Embedding Predictive Architectures with Sparse and Maximum-Entropy Representations

Flags: taxonomy_boundary_cluster, taxonomy-review, github

- Subarea: Vision robustness, detection, and adversarial perception
- Votes: 55
- ICML URL: https://icml.cc/virtual/2026/poster/65573
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.01456
- GitHub URL: https://github.com/YilunKuang/rectified-lp-jepa
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation
- Method families: Compression / efficiency
- Evaluation settings: vision/video; robotics/embodied
- Result claim cues: negative / limitation; scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Joint-Embedding Predictive Architectures (JEPA) learn view-invariant representations and admit projection-based distribution matching for collapse preventions. Existing approaches regularize representations towards isotropic Gaussian distributions, but inherently favor dense representations and fail to capture the key property of sparsity observed in efficient representations. We introduce Rectified Distribution Matching Regularization (RDMReg), a sliced two-sample distribution-matching loss that aligns representations to a Rectified Generalized Gaussian (RGG) distribution. RGG enables explicit control over expected $\ell_p$ norms and induces $\ell_0$ sparsity through rectifications, while preserving maximum entropy up to rescaling under sparsity constraints. Equipping JEPAs with RDMReg yields Rectified LpJEPA, which strictly generalizes prior Gaussian-based JEPAs. Empirically, Rectified LpJEPA learns sparse, non-negative representations with favorable sparsity–performance trade-offs and competitive downstream performance on image classification benchmarks, demonstrating that RDMReg effectively enforces sparsity while preserving task-relevant information.

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

### 16. On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression

Flags: taxonomy_boundary_cluster, taxonomy-review

- Subarea: Vision robustness, detection, and adversarial perception
- Votes: 32
- ICML URL: https://icml.cc/virtual/2026/poster/61440
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.21531
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Method / algorithm
- Method families: LLM post-training; Compression / efficiency
- Evaluation settings: vision/video; language/llm; security/safety
- Result claim cues: scaling / efficiency; robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: accuracy

Abstract:

Visual token compression is widely used to accelerate large vision-language models (LVLMs) by pruning or merging visual tokens, yet its adversarial robustness remains unexplored. We show that existing encoder-based attacks can substantially overestimate the robustness of compressed LVLMs, due to an optimization-inference mismatch: perturbations are optimized on the full-token representation, while inference is performed through a token-compression bottleneck. To address this gap, we propose the Compression-AliGnEd attack (CAGE), which aligns perturbation optimization with compression inference without assuming access to the deployed compression mechanism or its token budget. CAGE combines (i) expected feature disruption, which concentrates distortion on tokens likely to survive across plausible budgets, and (ii) rank distortion alignment, which actively aligns token distortions with rank scores to promote the retention of highly distorted evidence. Across diverse representative plug-and-play compression mechanisms and datasets, our results show that CAGE consistently achieves lower robust accuracy than the baseline. This work highlights that robustness assessments ignoring compression can be overly optimistic, calling for compression-aware security evaluation and defenses for efficient LVLMs.

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
