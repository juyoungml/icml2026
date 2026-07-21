# C07: Artifact visibility

Review question: Which high-visibility GitHub links appear to be real research artifacts rather than templates, indexes, or project pages?

## Queue Summary

- Papers: 16
- Selection mix: artifact_high_star=9, artifact_manual_check=7
- Oral/award papers: 1
- Taxonomy-review papers: 4
- GitHub-linked papers: 16

## Papers

### 1. From geometry to dynamics: Learning overdamped Langevin dynamics from sparse observations with geometric constraints

Flags: artifact_manual_check, github

- Review focus: Determine whether the GitHub link is a real paper artifact or a template/index/project page.
- Area/subarea: AI for Science, Health, and Neuro / Physical sciences, chemistry, and climate
- Cluster: 9 - physics / chemistry / earth / applications chemistry
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=2; 7d visits=1
- Artifact: https://github.com/academicpages/academicpages.github.io; stars=17294; manual-check=template_or_index_like_url
- Evidence tags: contribution=Benchmark / evaluation; methods=Compression / efficiency; Graphs / geometry; eval=robotics/embodied; science/domain; theory/synthetic
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/60982
- AlphaXiv URL: https://www.alphaxiv.org/abs/2512.23566

Abstract:

How can we learn the laws underlying the dynamics of stochastic systems when their trajectories are sampled sparsely in time? Existing methods either require temporally resolved high-frequency observations, or rely on geometric arguments that apply only to conservative systems, limiting the range of dynamics they can recover. Here, we present a new framework that reconciles these two perspectives by reformulating inference as a stochastic control problem. Our method uses geometry-driven path augmentation, guided by structure in the system’s invariant density to reconstruct likely trajectories and infer the underlying dynamics without assuming specific parametric models. Applied to overdamped Langevin systems, our approach accurately recovers stochastic dynamics even from severely undersampled data, outperforming existing methods in synthetic benchmarks. This work demonstrates the effectiveness of incorporating geometric inductive biases into stochastic system identification methods, with broad applications across physics, biology, and control.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 2. Vision-aligned Latent Reasoning for Multi-Modal Large Language Model

Flags: artifact_manual_check, taxonomy-review, github

- Review focus: Determine whether the GitHub link is a real paper artifact or a template/index/project page.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / Reasoning models and chain-of-thought behavior
- Cluster: 11 - reasoning / language / large language / language models
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=false; award=none; votes=56; 7d visits=29
- Artifact: https://github.com/awesome-NeRF/awesome-NeRF; stars=6773; manual-check=template_or_index_like_url
- Evidence tags: contribution=Benchmark / evaluation; methods=Reasoning / test-time compute; Transformer / attention; eval=vision/video; language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/61382
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.04476

Abstract:

Despite recent advancements in Multi-modal Large Language Models (MLLMs) on diverse understanding tasks, these models struggle to solve problems which require extensive multi-step reasoning. This is primarily due to the progressive dilution of visual information during long-context generation, which hinders their ability to fully exploit test-time scaling. To address this issue, we introduce Vision-aligned Latent Reasoning (VaLR), a simple, yet effective reasoning framework that dynamically generates vision-aligned latent tokens before each Chain of Thought reasoning step, guiding the model to reason based on perceptual cues in the latent space. Specifically, VaLR is trained to preserve visual knowledge during reasoning by aligning intermediate embeddings of MLLM with those from vision encoders. Empirical results demonstrate that VaLR consistently outperforms existing approaches across a wide range of benchmarks requiring long-context understanding or precise visual perception, while exhibiting test-time scaling behavior not observed in prior MLLMs. In particular, VaLR improves the performance significantly from 33.0\% to 52.9\% on VSI-Bench, achieving a 19.9\%p gain over Qwen2.5-VL.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 3. Self-Prompting Diffusion Transformer for Open-Vocabulary Scene Text Edit via In-Context Learning

Flags: artifact_manual_check, github

- Review focus: Determine whether the GitHub link is a real paper artifact or a template/index/project page.
- Area/subarea: Generative Modeling / Image/video diffusion and flow generation
- Cluster: 34 - diffusion / generative / image / generative models
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=6; 7d visits=1
- Artifact: https://github.com/eliahuhorwitz/Academic-project-page-template; stars=5069; manual-check=template_or_index_like_url
- Evidence tags: contribution=Dataset / data resource; methods=Diffusion / flow; Transformer / attention; eval=vision/video; language/llm
- Benchmark/data/metric cues: none / none / accuracy
- ICML URL: https://icml.cc/virtual/2026/poster/60814
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.15523

Abstract:

Scene text editing aims to modify text in a target region of an image while preserving its background style and texture. Existing methods rely solely on image background information while neglecting the visual details of target regions, which discards stylistic features in the original text and essentially degrades the task to text rendering. Moreover, the conditions imposed by pre-trained glyph encoder limit the scope of editable text. To address these issues, this paper proposes a self-prompting scene text editing method, which constructs style and glyph prompts directly from the original image without additional style or glyph encoders. We employ a two-stage training strategy, where the diffusion transformer is first trained on large-scale self-supervised datasets and subsequently refined with a small set of paired images. By leveraging the in-context learning capability of FLUX-Fill, it achieves open-vocabulary and style-consistent text editing. Experimental results on various languages demonstrate that our method achieves the state-of-the-art performance in both text accuracy and style consistency.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 4. From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model

Flags: artifact_manual_check, oral, github

- Review focus: Determine whether the GitHub link is a real paper artifact or a template/index/project page.
- Area/subarea: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Cluster: 16 - action / robotics / vla / applications robotics
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=14; 7d visits=39
- Artifact: https://github.com/eliahuhorwitz/Academic-project-page-template; stars=5069; manual-check=template_or_index_like_url
- Evidence tags: contribution=Application / domain study; methods=LLM post-training; Causal / data-centric; eval=vision/video; robotics/embodied; language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/66596
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.22671

Abstract:

Vision-Language-Action (VLA) models often suffer from performance degradation under distribution shifts, as they struggle to learn generalized behavior representations across varying environments. While existing approaches attempt to construct behavior representations through action-centric latent variables, they are often limited by short-horizon temporal fragmentation and static execution-alignment, leading to inconsistent behaviors in complex scenarios. To address these limitations, we propose \textbf{BehaviorVLA}, a framework that facilitates robust manipulation through the learning of a temporally coherent behavioral representations. Our approach features two symmetric components: (1) the \textbf{Visuomotor Behavior Encoder (VBE)}, which utilizes a causal Mamba-based architecture to aggregate long-horizon trajectory information into a unified behavior representation; and (2) the \textbf{Phase-conditioned Behavior Decoder (PBD)}, which decodes this representation into precise actions by dynamically aligning task-level priors with real-time execution progress. Experiments on RoboTwin 2.0, LIBERO, and CALVIN demonstrate state-of-the-art success rates of 58\%, 98\%, and 4.36 (Avg. Len), respectively. Notably, in real-world sim-to-real transfer, BehaviorVLA matches the performance of OpenVLA-OFT using only 50\% of the demonstration data, showcasing its superior data efficiency and generalization.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 5. Autoregressive Direct Preference Optimization

Flags: artifact_manual_check, taxonomy-review, github

- Review focus: Determine whether the GitHub link is a real paper artifact or a template/index/project page.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / LLM preference tuning and alignment training
- Cluster: 21 - language / large language / language models / large
- Cluster review: needs_review; manual confidence not high; split across lexical clusters
- Program/public: oral=false; award=none; votes=6; 7d visits=0
- Artifact: https://github.com/eliahuhorwitz/Academic-project-page-template; stars=5063; manual-check=template_or_index_like_url
- Evidence tags: contribution=Method / algorithm; methods=RL / policy optimization; LLM post-training; eval=language/llm; theory/synthetic
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/65423
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.09533

Abstract:

Direct preference optimization (DPO) has emerged as a promising approach for aligning large language models (LLMs) with human preferences. However, the widespread reliance on the response-level Bradley-Terry (BT) model may limit its full potential, as the reference and learnable models are assumed to be autoregressive only after deriving the objective function. Motivated by this limitation, we revisit the theoretical foundations of DPO and propose a novel formulation that explicitly introduces the autoregressive assumption prior to applying the BT model. By reformulating and extending DPO, we derive a novel variant, termed \textbf{Autoregressive DPO (ADPO)}, that explicitly integrates autoregressive modeling into the preference optimization framework. Without violating the theoretical foundations, the derived loss takes an elegant form: it shifts the summation operation in the DPO objective outside the log-sigmoid function. Furthermore, through theoretical analysis of ADPO, we show that there exist two length measures to be considered when designing DPO-based algorithms: the token length $\mu$ and the feedback length $\mu'$. To the best of our knowledge, we are the first to explicitly distinguish these two measures and analyze their implications for preference optimization in LLMs.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 6. AuTAgent: A Reinforcement Learning Framework for Tool-Augmented Audio Reasoning

Flags: artifact_manual_check, taxonomy-review, github

- Review focus: Determine whether the GitHub link is a real paper artifact or a template/index/project page.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Cluster: 2 - reward / reinforcement learning / reinforcement / rewards
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=false; award=none; votes=8; 7d visits=3
- Artifact: https://github.com/eliahuhorwitz/Academic-project-page-template; stars=5063; manual-check=template_or_index_like_url
- Evidence tags: contribution=Benchmark / evaluation; methods=RL / policy optimization; Reasoning / test-time compute; Agents / tool use; Compression / efficiency; eval=math/code/verifiable; language/llm
- Benchmark/data/metric cues: none / none / accuracy; reward
- ICML URL: https://icml.cc/virtual/2026/poster/64128
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.13685

Abstract:

Large Audio Language Models (LALMs) excel at perception but struggle with complex reasoning requiring precise acoustic measurements. While external tools can extract fine-grained features like exact tempo or pitch, effective integration remains challenging: naively using all tools causes information overload, while prompt-based selection fails to assess context-dependent utility. To address this, we propose **AuTAgent** (**Au**dio **T**ool **Agent**), a reinforcement learning framework that learns when and which tools to invoke. By employing a sparse-feedback training strategy with a novel Differential Reward mechanism, the agent learns to filter out irrelevant tools and invokes external assistance only when it yields a net performance gain over the base model. Experimental results confirm that AuTAgent complements the representation bottleneck of LALMs by providing verifiable acoustic evidence. It improves accuracy by 4.20% / 6.20% and 9.80% / 8.00% for open-source and closed-source backbones on the MMAU Test-mini and the MMAR benchmarks, respectively. In addition, further experiments demonstrate exceptional transferability. We highlight the complementary role of external tools in augmenting audio model reasoning.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 7. PanoWorld-X: Generating Explorable Panoramic Worlds via Sphere-Aware Video Diffusion

Flags: artifact_manual_check, github

- Review focus: Determine whether the GitHub link is a real paper artifact or a template/index/project page.
- Area/subarea: Multimodal, Vision, and Perception / 3D, video, motion, and spatial understanding
- Cluster: 25 - 3d / video / motion / applications computer
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=12; 7d visits=10
- Artifact: https://github.com/eliahuhorwitz/Academic-project-page-template; stars=5063; manual-check=template_or_index_like_url
- Evidence tags: contribution=Method / algorithm; methods=Diffusion / flow; Transformer / attention; Graphs / geometry; eval=vision/video; robotics/embodied
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/60719
- AlphaXiv URL: https://www.alphaxiv.org/abs/2509.24997

Abstract:

Achieving a complete and explorable 360-degree visual world is a cornerstone of immersive content creation. While recent advances in video generation have achieved impressive results, they follow a 2D paradigm that treats content generation as transitions of 2D pixels, lacking an intrinsic understanding of the physical 3D world, resulting in frequent geometric inconsistencies. To achieve an explorable and physical-consistent visual world, the generation process should shift to a 3D paradigm: the visual content is governed by the physical relationships of the entire 3D environment together with 3D motion signals. However, under this setting, the conventional modeling methods and control signals, such as spatial attention computation in a 2D space, become unsuitable and ineffective. To address this, we propose PanoWorld-X for explorable 3D scene video generation. Our framework is built on the panoramic representation, which naturally maps a 3D scene into a standard format and provides an ideal basis for consistency. Specifically, we first develop a data curation pipeline to produce high-quality and large-motion 3D scene evolution with movement trajectories. To achieve precise control, we design the Exploration Panoramic Plücker Embedding (PPE), a guidance signal tailored for 3D motion. Furthermore, leveraging the spherical geometric properties of panoramic data, we propose a sphere-aware attention mechanism, which can capture true geometric adjacency by reprojecting features onto a spherical surface. Extensive experiments demonstrate that PanoWorld-X achieves superior performance in motion range, control precision, and visual quality, underscoring its potential for real-world applications.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 8. PaperBanana: Automating Academic Illustration for AI Scientists

Flags: artifact_high_star, github

- Review focus: Check artifact type, license/readme quality, and whether reproduction assets are present.
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

### 9. DFlash: Block Diffusion for Flash Speculative Decoding

Flags: artifact_high_star, taxonomy-review, github

- Review focus: Check artifact type, license/readme quality, and whether reproduction assets are present.
- Area/subarea: LLM Reasoning, Post-Training, and RLVR / Diffusion language models and decoding
- Cluster: 14 - decoding / diffusion / language / language models
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=false; award=none; votes=153; 7d visits=272
- Artifact: https://github.com/z-lab/dflash; stars=5451; manual-check=none
- Evidence tags: contribution=System / infrastructure; methods=Reasoning / test-time compute; Diffusion / flow; eval=language/llm
- Benchmark/data/metric cues: none / none / latency
- ICML URL: https://icml.cc/virtual/2026/poster/64301
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.06036

Abstract:

Autoregressive large language models (LLMs) deliver strong performance but require inherently sequential decoding, leading to high inference latency and poor GPU utilization. Speculative decoding mitigates this bottleneck by using a fast draft model whose outputs are verified in parallel by the target LLM. However, existing methods still rely on *autoregressive drafting*, which remains sequential and constrains practical speedups. Diffusion LLMs offer a promising alternative by enabling parallel generation, but current diffusion models typically underperform compared with autoregressive models. In this paper, we introduce **DFlash**, a speculative decoding framework that employs a lightweight block diffusion model for parallel drafting. We show that speculative decoding provides a natural and effective setting for diffusion models. By generating draft tokens in a single forward pass, DFlash enables efficient drafting, and by conditioning the draft model on context features extracted from the target model, it achieves high-quality drafts with improved acceptance rates. Experiments demonstrate that DFlash achieves more than 6$\times$ lossless acceleration across a range of models and tasks, delivering up to 2.5$\times$ higher speedup than the state-of-the-art speculative decoding method EAGLE-3.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 10. Boosting Monocular Metric Depth Estimation via Bokeh Rendering

Flags: artifact_high_star, github

- Review focus: Check artifact type, license/readme quality, and whether reproduction assets are present.
- Area/subarea: Multimodal, Vision, and Perception / 3D, video, motion, and spatial understanding
- Cluster: 25 - 3d / video / motion / applications computer
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=4; 7d visits=1
- Artifact: https://github.com/eliahuhorwitz/Academic-project-page-template; stars=5063; manual-check=template_or_index_like_url
- Evidence tags: contribution=Method / algorithm; methods=Diffusion / flow; Graphs / geometry; eval=vision/video; theory/synthetic
- Benchmark/data/metric cues: none / none / accuracy
- ICML URL: https://icml.cc/virtual/2026/poster/65700
- AlphaXiv URL: https://www.alphaxiv.org/abs/2512.12425

Abstract:

Bokeh rendering and depth estimation share a fundamental optical connection, yet existing methods fail to fully exploit this reciprocity. Conventional bokeh pipelines rely heavily on noisy depth maps that inevitably introduce visual artifacts. Conversely, existing monocular depth models typically follow two flawed paradigms. Generative diffusion-based frameworks often lack consistent metric scale. Meanwhile, feed-forward metric depth models frequently fail in textureless or distant regions where defocus blur can provide geometric information. We propose BokehDepth, a two-stage framework that treats synthetic defocus as a supervision-free geometric signal. In the first stage, a physically grounded generative model produces calibrated bokeh stacks from a single sharp input without requiring prior depth input. Subsequently, a lightweight defocus-aware aggregation module integrates these stacks into the encoder of a depth estimation framework. This mechanism allows the model to extract consistent geometric features from the defocus dimension while keeping the decoder architecture unchanged. Experiments demonstrate that BokehDepth achieves superior visual bokeh fidelity compared to depth-dependent rendering baselines and consistently enhances the metric accuracy of state-of-the-art monocular depth models.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 11. AudioChat: Unified Audio Storytelling, Editing, and Understanding with Transfusion Forcing

Flags: artifact_high_star, github

- Review focus: Check artifact type, license/readme quality, and whether reproduction assets are present.
- Area/subarea: Multimodal, Vision, and Perception / Multimodal representation and cross-modal alignment
- Cluster: 0 - multimodal / visual / modal / modality
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=14; 7d visits=4
- Artifact: https://github.com/eliahuhorwitz/Academic-project-page-template; stars=5063; manual-check=template_or_index_like_url
- Evidence tags: contribution=Theory / proof; methods=Reasoning / test-time compute; Agents / tool use; eval=language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/66763
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.17097

Abstract:

Despite recent breakthroughs, audio foundation models struggle in processing complex multi-source acoustic scenes. We refer to this challenging domain as audio stories, which can have multiple speakers and background/foreground sound effects. Compared to traditional audio processing tasks, audio stories introduce new layers of semantic, temporal, and physical complexity. To address this challenge, we propose AudioChat, a framework for developing audio foundation models that can generate, edit, and understand audio stories. AudioChat introduces a new paradigm in which LLM-based toolcalling agents simulate interactions between users and the system, and these simulated dialogues are used as training data. We also introduce a novel Audio Transfusion Forcing objective to train the AudioChat model, allowing it to simultaneously decompose high-level instructions via structured chain-of-thought reasoning and perform interactive multi-turn audio understanding/generation. To evaluate generation and editing performance, we develop three new metrics that directly measure task performance instead of relying upon distribution-based scoring. We highly encourage readers to visit our demo to better understand the capabilities of AudioChat: https://audiochat-icml-2026.github.io/.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 12. From Correspondence to Actions: Human-Like Multi-Image Spatial Reasoning in Multi-modal Large Language Models

Flags: artifact_high_star, github

- Review focus: Check artifact type, license/readme quality, and whether reproduction assets are present.
- Area/subarea: Multimodal, Vision, and Perception / Vision-language reasoning and video understanding
- Cluster: 22 - visual / vision / reasoning / video
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=12; 7d visits=2
- Artifact: https://github.com/eliahuhorwitz/Academic-project-page-template; stars=5063; manual-check=template_or_index_like_url
- Evidence tags: contribution=Benchmark / evaluation; methods=LLM post-training; Reasoning / test-time compute; eval=vision/video; robotics/embodied; language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/60836
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.08735

Abstract:

While multimodal large language models (MLLMs) have made substantial progress in single-image spatial reasoning, multi-image spatial reasoning, which requires integration of information from multiple viewpoints, remains challenging. Cognitive studies suggest that humans address such tasks through two mechanisms: *cross-view correspondence*, which identifies regions across different views that correspond to the same physical locations, and *stepwise viewpoint transformation*, which composes relative viewpoint changes sequentially. However, existing studies incorporate these mechanisms only partially and often implicitly, without explicit supervision for both. We propose Human-Aware Training for Cross-view correspondence and viewpoint cHange (HATCH), a training framework with two complementary objectives: (1) Patch-Level Spatial Alignment, which encourages patch representations to align across views for spatially corresponding regions, and (2) Action-then-Answer Reasoning, which requires the model to generate explicit viewpoint transition actions before predicting the final answer. Experiments on three benchmarks demonstrate that \method consistently outperforms baselines of comparable size by a clear margin and achieves competitive results against much larger models, while preserving single-image reasoning capabilities.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 13. LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model

Flags: artifact_high_star, github

- Review focus: Check artifact type, license/readme quality, and whether reproduction assets are present.
- Area/subarea: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Cluster: 16 - action / robotics / vla / applications robotics
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=73; 7d visits=25
- Artifact: https://github.com/eliahuhorwitz/Academic-project-page-template; stars=5063; manual-check=template_or_index_like_url
- Evidence tags: contribution=System / infrastructure; methods=Reasoning / test-time compute; Transformer / attention; eval=vision/video; robotics/embodied; language/llm
- Benchmark/data/metric cues: none / none / latency
- ICML URL: https://icml.cc/virtual/2026/poster/61887
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.05248

Abstract:

Vision-Language-Action (VLA) models have recently shown strong generalization, with some approaches seeking to explicitly generate linguistic reasoning traces or predict future observations prior to execution. However, explicit reasoning typically incurs non-negligible inference latency, which constrains the temporal resolution required for robotic manipulation. Moreover, such reasoning is confined to the linguistic space, imposing a representational bottleneck that struggles to faithfully capture ineffable physical attributes. To mitigate these limitations, we propose LaST$_0$, a framework that enables efficient reasoning before acting through a Latent Spatio-Temporal Chain-of-Thought (CoT), capturing fine-grained physical and robotic dynamics that are often difficult to verbalize. Specifically, we introduce a token-efficient latent CoT space that models future visual dynamics, 3D structural information, and robot proprioceptive states, and further extends these representations across time to enable temporally consistent implicit reasoning trajectories. Furthermore, LaST$_0$ adopts a dual-system architecture implemented via a Mixture-of-Transformers design, where a reasoning expert conducts low-frequency latent inference and an acting expert generates high-frequency actions conditioned on robotics-oriented latent representations. To facilitate coordination, LaST$_0$ is trained with heterogeneous operation frequencies, enabling adaptive switching during deployment. Across 10 real-world tasks spanning tabletop, mobile, and dexterous hand manipulation, LaST$_0$ improves mean success rates by 13%, 14% and 14% over prior SOTA VLA methods, respectively.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 14. Hydra-Nav: Object Navigation via Adaptive Dual-Process Reasoning

Flags: artifact_high_star, github

- Review focus: Check artifact type, license/readme quality, and whether reproduction assets are present.
- Area/subarea: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Cluster: 16 - action / robotics / vla / applications robotics
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=15; 7d visits=3
- Artifact: https://github.com/eliahuhorwitz/Academic-project-page-template; stars=5063; manual-check=template_or_index_like_url
- Evidence tags: contribution=Benchmark / evaluation; methods=LLM post-training; Reasoning / test-time compute; Agents / tool use; eval=vision/video; robotics/embodied; language/llm
- Benchmark/data/metric cues: none / none / memory
- ICML URL: https://icml.cc/virtual/2026/poster/61357
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.09972

Abstract:

While large vision-language models (VLMs) show promise for object goal navigation, current methods still struggle with low success rates and inefficient localization of unseen objects—failures primarily attributed to weak temporal-spatial reasoning. Meanwhile, recent attempts to inject reasoning into VLM-based agents improve success rates but incur substantial computational overhead. To address both the ineffectiveness and inefficiency of existing approaches, we introduce Hydra-Nav, a unified VLM architecture that adaptively switches between a deliberative "slow system" for analyzing exploration history and formulating high-level plans, and a reactive "fast system" for efficient execution. We train Hydra-Nav through a three-stage curriculum: (i) spatial-action alignment to strengthen trajectory planning, (ii) memory-reasoning integration to enhance temporal-spatial reasoning over long-horizon exploration, and (iii) iterative rejection fine-tuning to enable selective reasoning at critical decision points. Extensive experiments demonstrate that Hydra-Nav achieves state-of-the-art performance on the HM3D, MP3D, and OVON benchmarks, outperforming the second-best methods by 11.1\%, 17.4\%, and 21.2\%, respectively. Furthermore, we introduce SOT (Success weighted by Operation Time), a new metric to measure search efficiency across VLMs with varying reasoning intensity. Results show that adaptive reasoning significantly enhances search efficiency over fixed-frequency baselines.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 15. Turbo4DGen: Ultra-Fast Acceleration for 4D Generation

Flags: artifact_high_star, github

- Review focus: Check artifact type, license/readme quality, and whether reproduction assets are present.
- Area/subarea: Multimodal, Vision, and Perception / 3D, video, motion, and spatial understanding
- Cluster: 25 - 3d / video / motion / applications computer
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=0; 7d visits=0
- Artifact: https://github.com/ArthurBrussee/brush; stars=4818; manual-check=none
- Evidence tags: contribution=Dataset / data resource; methods=Diffusion / flow; Transformer / attention; Compression / efficiency; eval=vision/video
- Benchmark/data/metric cues: none / none / memory
- ICML URL: https://icml.cc/virtual/2026/poster/62276
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.29572

Abstract:

4D generation, or dynamic 3D content generation, integrates spatial, temporal, and view dimensions to model realistic dynamic scenes, playing a foundational role in advancing world models and physical AI. However, maintaining long-chain consistency across both frames and viewpoints through the unique spatio-camera-motion (SCM) attention mechanism introduces substantial computational and memory overhead, often leading to out-of-memory (OOM) failures and prohibitive generation times. To address these challenges, we propose Turbo4DGen, an ultra-fast acceleration framework for diffusion-based multi-view 4D content generation. Turbo4DGen introduces a spatiotemporal cache mechanism that persistently reuses intermediate attention across denoising steps, combined with dynamically semantic-aware attention pruning and an adaptive SCM chain bypass scheduler, to drastically reduce redundant SCM attention computation. Our experimental results show that Turbo4DGen achieves an average 9.7$\times$ speedup without quality degradation on the ObjaverseDy and Consistent4D datasets. To the best of our knowledge, Turbo4DGen is the first dedicated acceleration framework for 4D generation.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 16. DeepAnalyze: Agentic Large Language Models for Autonomous Data Science

Flags: artifact_high_star, github

- Review focus: Check artifact type, license/readme quality, and whether reproduction assets are present.
- Area/subarea: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Cluster: 40 - agents / agent / evaluation / agentic
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=146; 7d visits=25
- Artifact: https://github.com/ruc-datalab/DeepAnalyze; stars=4355; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=Agents / tool use; eval=language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/61106
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.16872

Abstract:

Autonomous data science on the structured data has been a long-standing challenge, and is now becoming feasible with the emergence of powerful large language models (LLMs). Recent workflowbased data agents have shown promising results on specific data tasks but remain fundamentally limited in achieving full autonomy due to their reliance on predefined workflows. In this paper, we introduce DeepAnalyze, the first agentic LLM for autonomous data science, capable of automatically completing the end-to-end data science from structured data to analyst-grade research reports. To tackle high-complexity data science tasks, we propose a curriculum-based agentic training paradigm that emulates the learning trajectory of human data scientists, enabling LLMs to progressively acquire and integrate multiple capabilities in real-world environments. Accordingly, we contribute a data-grounded trajectory synthesis framework to constructs high-quality data science training data. Through training in real-world environment, DeepAnalyze learns to perform a broad spectrum of data tasks, ranging from data question answering to open-ended data research. Experiments on 13 benchmarks demonstrate that, with only 8B parameters, DeepAnalyze outperforms previous workflow-based agents built on most advanced proprietary LLMs.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:
