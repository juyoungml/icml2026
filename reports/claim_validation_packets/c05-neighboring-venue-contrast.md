# C05: Neighboring-venue contrast

Review question: Is multimodal/vision truly underweight versus neighboring venues, or is the aggregate hiding subarea differences?

## Queue Summary

- Papers: 14
- Selection mix: multimodal_high_attention=10, multimodal_subarea_anchor=4
- Oral/award papers: 4
- Taxonomy-review papers: 1
- GitHub-linked papers: 9

## Papers

### 1. Motion Attribution for Video Generation

Flags: multimodal_subarea_anchor, oral, Outstanding Paper Honorable Mention

- Review focus: Check whether each subarea behaves differently from the aggregate underweight claim.
- Area/subarea: Multimodal, Vision, and Perception / 3D, video, motion, and spatial understanding
- Cluster: 25 - 3d / video / motion / applications computer
- Cluster review: stable_seed; none
- Program/public: oral=true; award=Outstanding Paper Honorable Mention; votes=67; 7d visits=208
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=LLM post-training; Causal / data-centric; eval=vision/video; language/llm
- Benchmark/data/metric cues: VBench / none / win_rate
- ICML URL: https://icml.cc/virtual/2026/poster/60542
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.08828

Abstract:

Despite the rapid progress of video generation models, the role of data in influencing motion is poorly understood. We present Motive (MOTIon attribution for Video gEneration), a motion-centric, gradient-based data attribution framework that scales to modern, large, high-quality video datasets and models. We use this to study which fine-tuning clips improve or degrade temporal dynamics. Motive isolates temporal dynamics from static appearance via motion-weighted loss masks, yielding efficient and scalable motion-specific influence computation. On text-to-video models, Motive identifies clips that strongly affect motion and guides data curation that improves temporal consistency and physical plausibility. With Motive-selected high-influence data, we improve both motion smoothness and dynamic degree on VBench, achieving a 74.1% human preference win rate compared with the pretrained base model. To our knowledge, this is the first framework to attribute motion rather than visual appearance in video generative models and to use it to curate fine-tuning data.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 2. Bad Seeing or Bad Thinking? Rewarding Perception for Multimodal Reasoning

Flags: multimodal_subarea_anchor, oral

- Review focus: Check whether each subarea behaves differently from the aggregate underweight claim.
- Area/subarea: Multimodal, Vision, and Perception / Vision-language reasoning and video understanding
- Cluster: 22 - visual / vision / reasoning / video
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=21; 7d visits=27
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Position / conceptual; methods=RL / policy optimization; Reasoning / test-time compute; Agents / tool use; eval=vision/video; language/llm
- Benchmark/data/metric cues: none / none / reward
- ICML URL: https://icml.cc/virtual/2026/poster/62726
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.14054

Abstract:

Achieving robust perception-reasoning synergy is a central goal for advanced Vision-Language Models (VLMs). Recent advancements have pursued this goal via architectural designs or agentic workflows. However, these approaches are often limited by static textual reasoning or complicated by the significant compute and engineering burden of external agentic complexity. Worse, this heavy investment does not yield proportional gains, often witnessing a "seesaw effect" on perception and reasoning. This motivates a fundamental rethinking of the true bottleneck. In this paper, we argue that the root cause of this trade-off is an ambiguity in modality credit assignment: when a VLM fails, is it due to flawed perception ("bad seeing") or flawed logic ("bad thinking")? To resolve this, we introduce a reinforcement learning framework that improves perception-reasoning synergy by reliably rewarding the perception fidelity. We explicitly decompose the generation process into interleaved perception and reasoning steps. This decoupling enables targeted supervision on perception. Crucially, we introduce Perception Verification (PV), leveraging a "blindfolded reasoning" proxy to reward perceptual fidelity independently of reasoning outcomes. Furthermore, to scale training across free-form VL tasks, we propose Structured Verbal Verification, which replaces high-variance LLM judging with structured algorithmic execution. These techniques are integrated into a Modality-Aware Credit Assignment (MoCA) mechanism, which routes rewards to the specific source of error -- either bad seeing or bad thinking -- enabling a single VLM to achieve simultaneous performance gains across a wide task spectrum.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 3. Mind Your Margin and Boundary: Are Your Distilled Datasets Truly Robust?

Flags: multimodal_subarea_anchor, oral, taxonomy-review

- Review focus: Check whether each subarea behaves differently from the aggregate underweight claim.
- Area/subarea: Multimodal, Vision, and Perception / Vision robustness, detection, and adversarial perception
- Cluster: 36 - detection / vision / image / robustness
- Cluster review: needs_review; manual confidence not high; split across lexical clusters
- Program/public: oral=true; award=none; votes=2; 7d visits=3
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Position / conceptual; methods=Causal / data-centric; eval=vision/video; security/safety; theory/synthetic
- Benchmark/data/metric cues: none / none / accuracy
- ICML URL: https://icml.cc/virtual/2026/poster/63330
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.20606

Abstract:

Dataset distillation (DD) compresses a large training set into a small synthetic set for efficient training, but most DD methods optimize only clean accuracy and leave robustness uncontrolled. Recent robust DD methods improve robustness, yet they often suffer from a poor accuracy–robustness trade-off because they (i) treat all adversarially perturbed examples uniformly, despite robust risk being dominated by near-zero robust margins, and (ii) do not explicitly increase inter-class separation in the decision boundary where attacks concentrate. We present Contrastive Curriculum for Robust Dataset Distillation (C$^2$R), a margin-centric framework that couples an attack-aware curriculum with a contrastive robustness objective. From a robust-margin perspective, we derive a perturbation score that approximates each sample’s robust hinge, enabling a curriculum that prioritizes the smallest-margin adversaries that most directly drive robust error. In parallel, a class-balanced contrastive robustness loss enforces adversarial invariance while explicitly widening boundary separation across classes. Experiments on CIFAR-10/100, Tiny-ImageNet, and multiple ImageNet-1K subsets under six attacks show that C$^2$R achieves the best robust accuracy, outperforming prior robust DD methods by $2.8$\% on average. Under PGD, C$^2$R also reduces the average drop rate (DR) below $66.8$\% across datasets, indicating a stronger accuracy–robustness balance.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 4. Multimodal Nested Learning for Decoupled and Coordinated Optimization

Flags: multimodal_subarea_anchor, oral

- Review focus: Check whether each subarea behaves differently from the aggregate underweight claim.
- Area/subarea: Multimodal, Vision, and Perception / Multimodal representation and cross-modal alignment
- Cluster: 0 - multimodal / visual / modal / modality
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=0; 7d visits=0
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Dataset / data resource; methods=none; eval=none
- Benchmark/data/metric cues: none / none / memory
- ICML URL: https://icml.cc/virtual/2026/poster/65954
- AlphaXiv URL: none

Abstract:

Multimodal learning aims to integrate multi-sensor data to exploit their complementary information, embracing a more comprehensive real-world perception and understanding. However, heterogeneous discrepancies across modalities consistently trigger imbalanced multimodal optimization, restricting the joint learning performance. Although existing methods mitigate this issue through optimization modulation and conflict alleviation, they still suffer from entangled optimization and uniform learning pace in conventional monolithic frameworks, limiting the effectiveness of multimodal learning. To address this issue, we propose a novel Multimodal Nested Learning Framework (MoNet), which reformulates the monolithic framework into nested sub-processes, decoupling and coordinating multimodal learning. To achieve this, we present a Decoupled Multimodal Stable Memory block (DMSM) as the outermost nested level, which decouples multimodal learning into independent optimization streams for semantic exploitation across modalities. Additionally, we develop an Adaptive Multimodal Coordinated Fusion block (AMCF), which constitutes the inner nested level. It attempts to coordinate multimodal information integration across multi-timescale nested memories, balancing multimodal fusion. Extensive experimental results on eight datasets across three tasks demonstrate the superiority of MoNet.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 5. A Very Big Video Reasoning Suite

Flags: multimodal_high_attention, github

- Review focus: Check whether high-attention ICML multimodal papers look more like ICLR/NeurIPS-style vision work or ICML-style ML methods.
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

### 6. Causal-JEPA: Learning World Models through Object-Level Latent Interventions

Flags: multimodal_high_attention, github

- Review focus: Check whether high-attention ICML multimodal papers look more like ICLR/NeurIPS-style vision work or ICML-style ML methods.
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

### 7. ExSkill: Continual Learning from Experience and Skills in Multimodal Agents

Flags: multimodal_high_attention, github

- Review focus: Check whether high-attention ICML multimodal papers look more like ICLR/NeurIPS-style vision work or ICML-style ML methods.
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

### 8. BabyVision: Visual Reasoning Beyond Language

Flags: multimodal_high_attention, github

- Review focus: Check whether high-attention ICML multimodal papers look more like ICLR/NeurIPS-style vision work or ICML-style ML methods.
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

### 9. Utonia: Toward One Encoder for All Point Clouds

Flags: multimodal_high_attention, github

- Review focus: Check whether high-attention ICML multimodal papers look more like ICLR/NeurIPS-style vision work or ICML-style ML methods.
- Area/subarea: Multimodal, Vision, and Perception / 3D, video, motion, and spatial understanding
- Cluster: 25 - 3d / video / motion / applications computer
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=118; 7d visits=27
- Artifact: https://github.com/Pointcept/Utonia; stars=710; manual-check=none
- Evidence tags: contribution=Application / domain study; methods=Reasoning / test-time compute; Transformer / attention; Compression / efficiency; eval=vision/video; robotics/embodied; language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/62613
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.03283

Abstract:

We dream of a future where point clouds from all domains can come together to shape a single model that benefits them all. Toward this goal, we present Utonia, a first step toward training a single self-supervised point transformer encoder across heterogeneous domains, spanning remote sensing, outdoor LiDAR, indoor RGB-D sequences, object-centric CAD models, and point clouds lifted from RGB-only videos. Despite their distinct sensing geometries, densities, and priors, Utonia learns a consistent representation space that transfers across domains. This unification improves perception capability while revealing intriguing emergent behaviors that arise only when domains are trained jointly. Beyond perception, we observe that Utonia representations can also benefit embodied and multimodal reasoning: conditioning vision-language-action policies on Utonia features improves robotic manipulation, and integrating them into vision-language models yields gains on spatial reasoning. We hope Utonia can serve as a step toward foundation models for sparse 3D data, and support downstream applications in AR/VR, robotics, and autonomous driving.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 10. World-R1: Reinforcing 3D Constraints for Text-to-Video Generation

Flags: multimodal_high_attention, github

- Review focus: Check whether high-attention ICML multimodal papers look more like ICLR/NeurIPS-style vision work or ICML-style ML methods.
- Area/subarea: Multimodal, Vision, and Perception / 3D, video, motion, and spatial understanding
- Cluster: 25 - 3d / video / motion / applications computer
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=116; 7d visits=45
- Artifact: https://github.com/microsoft/World-R1; stars=406; manual-check=none
- Evidence tags: contribution=Dataset / data resource; methods=RL / policy optimization; LLM post-training; Diffusion / flow; Graphs / geometry; eval=vision/video; language/llm; theory/synthetic
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/61916
- AlphaXiv URL: https://www.alphaxiv.org/abs/2604.24764

Abstract:

Recent video foundation models demonstrate impressive visual synthesis but frequently suffer from geometric inconsistencies. While existing methods attempt to inject 3D priors via architectural modifications, they often incur high computational costs and limit scalability. We propose World-R1, a framework that aligns video generation with 3D constraints through reinforcement learning. To facilitate this alignment, we introduce a specialized pure text dataset tailored for world simulation. Utilizing Flow-GRPO, we optimize the model using feedback from pre-trained 3D foundation models and vision-language models to enforce structural coherence without altering the underlying architecture. We further employ a periodic decoupled training strategy to balance rigid geometric consistency with dynamic scene fluidity. Extensive evaluations reveal that our approach significantly enhances 3D consistency while preserving the original visual quality of the foundation model, effectively bridging the gap between video generation and scalable world simulation.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 11. DiffThinker: Towards Generative Multimodal Reasoning with Diffusion Models

Flags: multimodal_high_attention, github

- Review focus: Check whether high-attention ICML multimodal papers look more like ICLR/NeurIPS-style vision work or ICML-style ML methods.
- Area/subarea: Multimodal, Vision, and Perception / Multimodal representation and cross-modal alignment
- Cluster: 0 - multimodal / visual / modal / modality
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=111; 7d visits=6
- Artifact: https://github.com/lcqysl/DiffThinker; stars=186; manual-check=none
- Evidence tags: contribution=Method / algorithm; methods=LLM post-training; Reasoning / test-time compute; Diffusion / flow; eval=vision/video; language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/62143
- AlphaXiv URL: https://www.alphaxiv.org/abs/2512.24165

Abstract:

While recent Multimodal Large Language Models (MLLMs) have attained significant strides in multimodal reasoning, their reasoning processes remain predominantly text-centric and fail to visualize and track intermediate visual states during the reasoning process, leading to suboptimal performance in complex long-horizon, vision-centric tasks. Moving beyond the constraints of text-centric reasoning, we establish Generative Multimodal Reasoning as a novel paradigm and introduce DiffThinker, a diffusion-based reasoning framework. Conceptually, DiffThinker reformulates multimodal reasoning as a native generative image-to-image task, where the iterative denoising trajectory naturally serves as a visual reasoning path. This enables the model to track the evolution of visual information throughout the reasoning process. We perform a systematic comparison between DiffThinker and MLLMs, providing the first in-depth investigation into the intrinsic characteristics of this paradigm, revealing four core properties: efficiency, controllability, native parallelism, and collaboration. Extensive experiments across seven tasks demonstrate that DiffThinker significantly outperforms leading closed-source models, including GPT-5 (+314.2%) and Gemini-3-Flash (+111.6%), as well as the fine-tuned Qwen3-VL-32B baseline (+39.0%), highlighting Generative Multimodal Reasoning as a promising approach for vision-centric reasoning.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 12. WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling

Flags: multimodal_high_attention

- Review focus: Check whether high-attention ICML multimodal papers look more like ICLR/NeurIPS-style vision work or ICML-style ML methods.
- Area/subarea: Multimodal, Vision, and Perception / 3D, video, motion, and spatial understanding
- Cluster: 25 - 3d / video / motion / applications computer
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=98; 7d visits=27
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=System / infrastructure; methods=Diffusion / flow; Graphs / geometry; eval=vision/video; robotics/embodied
- Benchmark/data/metric cues: none / none / memory
- ICML URL: https://icml.cc/virtual/2026/poster/65111
- AlphaXiv URL: https://www.alphaxiv.org/abs/2512.14614

Abstract:

This paper presents WorldPlay, a streaming video diffusion model that enables real-time, interactive world modeling with long-term geometric consistency, resolving the trade-off between speed and memory that limits current methods. WorldPlay draws power from three key innovations. 1) We use a Dual Action Representation to enable robust action control in response to the user's keyboard and mouse inputs. 2) To enforce long-term consistency, our Reconstituted Context Memory dynamically rebuilds context from past frames and uses temporal reframing to keep geometrically important but long-past frames accessible, effectively alleviating memory attenuation. 3) We also propose Context Forcing, a novel distillation method designed for memory-aware model. Aligning memory context between the teacher and student preserves the student's capacity to use long-range information, enabling real-time speeds while preventing error drift. Taken together, WorldPlay generates long-horizon streaming 720p video at 24 FPS with superior consistency, comparing favorably with existing techniques and showing strong generalization across diverse scenes.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 13. Self-Refining Video Sampling

Flags: multimodal_high_attention, github

- Review focus: Check whether high-attention ICML multimodal papers look more like ICLR/NeurIPS-style vision work or ICML-style ML methods.
- Area/subarea: Multimodal, Vision, and Perception / 3D, video, motion, and spatial understanding
- Cluster: 25 - 3d / video / motion / applications computer
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=81; 7d visits=16
- Artifact: https://github.com/agwmon/self-refine-video; stars=181; manual-check=none
- Evidence tags: contribution=Dataset / data resource; methods=LLM post-training; Reasoning / test-time compute; Diffusion / flow; eval=vision/video; science/domain
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/61169
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.18577

Abstract:

Modern video generators still struggle with complex physical dynamics, often falling short of physical realism. Existing approaches address this using external verifiers or additional training on augmented data, which is computationally expensive and still limited in capturing fine-grained motion. In this work, we present self-refining video sampling, a simple method that uses a pre-trained video generator trained on large-scale datasets as its own self-refiner. By interpreting the generator as a denoising autoencoder, we enable iterative inner-loop refinement at inference time without any external verifier or additional training. We further introduce an uncertainty-aware refinement strategy that selectively refines regions based on self-consistency, which prevents artifacts caused by over-refinement. Experiments on state-of-the-art video generators demonstrate significant improvements in motion coherence and physics alignment, achieving over 70% human preference compared to the default sampler and guidance-based sampler.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 14. Zooming without Zooming: Region-to-Image Distillation for Fine-Grained Multimodal Perception

Flags: multimodal_high_attention, github

- Review focus: Check whether high-attention ICML multimodal papers look more like ICLR/NeurIPS-style vision work or ICML-style ML methods.
- Area/subarea: Multimodal, Vision, and Perception / Vision-language reasoning and video understanding
- Cluster: 22 - visual / vision / reasoning / video
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=67; 7d visits=64
- Artifact: https://github.com/inclusionAI/Zooming-without-Zooming; stars=169; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=Agents / tool use; eval=vision/video; language/llm
- Benchmark/data/metric cues: VQA / none / latency
- ICML URL: https://icml.cc/virtual/2026/poster/62952
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.11858

Abstract:

Multimodal Large Language Models (MLLMs) excel at broad visual understanding but still struggle with fine-grained perception, where decisive evidence is small and easily overwhelmed by global context. Recent "Thinking-with-Images" methods alleviate this by iteratively zooming into regions of interest during inference, but incur high latency due to repeated tool calls and visual re-encoding. To address this, we propose Region-to-Image Distillation, which transforms zooming from an inference-time tool into a training-time primitive, thereby internalizing the benefits of agentic zooming into a single forward pass. In particular, we first zoom in to micro-cropped regions to let strong teacher models generate high-quality VQA data, and then distill this region-grounded supervision back to the full image. After training on such data, the smaller student model improves "single-glance" fine-grained perception without tool use. To rigorously evaluate this capability, we further present MicroPercept, a hybrid-annotated benchmark of 845 VQA data spanning six fine-grained perceptual dimensions, together with a dual-view protocol that quantifies the global-regional "zooming gap". Experiments show that our model achieves consistent gains across multiple fine-grained perception benchmarks, surpasses state-of-the-art agentic models while eliminating their inference latency, and improves out-of-distribution generalization.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:
