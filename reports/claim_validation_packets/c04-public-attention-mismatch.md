# C04: Public attention mismatch

Review question: Is robotics/world-model public attention driven by substantive research artifacts, benchmarks, demos, or hype?

## Queue Summary

- Papers: 12
- Selection mix: robotics_public_not_program=9, robotics_program_anchor=3
- Oral/award papers: 3
- Taxonomy-review papers: 0
- GitHub-linked papers: 9

## Papers

### 1. Learning Latent Action World Models In The Wild

Flags: robotics_public_not_program

- Review focus: Classify the source of public attention: benchmark, demo, artifact, model release, or hype.
- Area/subarea: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Cluster: 16 - action / robotics / vla / applications robotics
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=273; 7d visits=105
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Dataset / data resource; methods=RL / policy optimization; Agents / tool use; Compression / efficiency; eval=vision/video; robotics/embodied
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/65056
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.05230

Abstract:

Agents that can reason and plan in the real world must be able to predict the consequences of their actions. World models possess this capability but require action annotations that can be complex to obtain at scale. Latent action models address this issue by learning an action space from videos alone. Our work studies the training of latent action world models on in-the-wild videos, expanding the scope of existing works that focus on simple robotics simulations, video games, or manipulation data. While diverse videos enable modeling richer actions, they introduce challenges of environmental noise and lack of a common embodiment across videos. To address these, we carefully study the design and evaluation of latent actions. We find that constrained continuous latent actions are better suited for complex in-the-wild videos, compared to vector quantization. For example, actions specific to in-the-wild videos such as humans entering the room, can be modeled and then transferred across videos. However, in the absence of a common embodiment, learned latent actions are localized in space, relative to the camera. Nonetheless, we are able to train a controller that maps known actions to latent ones, allowing us to use latent actions as a universal interface to solve planning tasks on par with action-conditioned baselines.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 2. Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies

Flags: robotics_public_not_program, github

- Review focus: Classify the source of public attention: benchmark, demo, artifact, model release, or hype.
- Area/subarea: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Cluster: 16 - action / robotics / vla / applications robotics
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=204; 7d visits=35
- Artifact: https://github.com/Liang-ZX/DiscreteDiffusionVLA; stars=69; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=RL / policy optimization; Diffusion / flow; Transformer / attention; eval=vision/video; robotics/embodied; language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/62902
- AlphaXiv URL: https://www.alphaxiv.org/abs/2508.20072

Abstract:

Vision–Language–Action (VLA) models adapt large vision–language backbones to map images and instructions into robot actions. However, prevailing VLAs either generate actions autoregressively in a fixed left-to-right order or attach separate diffusion heads outside the backbone, fragmenting information pathways and hindering unified, scalable architectures. We present Discrete Diffusion VLA, a unified-transformer policy that models discretized action chunks with discrete diffusion retaining progressive refinement inside the VLM backbone. Our method achieves an adaptive decoding order that resolves high-confidence (easy) action elements before harder ones and employs secondary re-masking to revisit uncertain predictions, enabling robust error correction. This design preserves pretrained vision-language priors, supports parallel decoding, and improves the efficiency. Discrete Diffusion VLA achieves 96.5% avg.~success on LIBERO, 71.2% visual matching on SimplerEnv-Fractal, and 54.2% overall on SimplerEnv-Bridge. On out-of-distribution benchmarks, our method exhibits only 1.4% language degradation versus 8.0% for parallel decoding, and 21.0% vision degradation versus 29.0% for continuous diffusion, demonstrating well retention of pretrained vision-language capabilities. Visualization analysis confirms the learned decoding order adaptively prioritizes high-confidence tokens, validating our refinement strategy.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 3. Temporal Straightening for Latent Planning

Flags: robotics_public_not_program, github

- Review focus: Classify the source of public attention: benchmark, demo, artifact, model release, or hype.
- Area/subarea: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Cluster: 16 - action / robotics / vla / applications robotics
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=202; 7d visits=56
- Artifact: https://github.com/agentic-learning-ai-lab/temporal-straightening; stars=92; manual-check=none
- Evidence tags: contribution=Uncoded; methods=none; eval=none
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/64904
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.12231

Abstract:

Learning good representations is essential for latent planning with world models. While pretrained visual encoders provide strong visual features, they are not tailored to planning and contain substantial information which is irrelevant to planning. Inspired by the perceptual straightening hypothesis in human visual processing, we introduce temporal straightening for representation learning in latent planning. We add a lightweight projector on top of a pretrained visual encoder to map to a lower-dimensional space, trained with a curvature regularizer that encourages locally straightened latent trajectories. We show that reducing curvature improves the conditioning of the planning objective, making gradient-based planning more stable and yielding significantly higher success rates across four goal-reaching tasks.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 4. LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries

Flags: robotics_public_not_program, github

- Review focus: Classify the source of public attention: benchmark, demo, artifact, model release, or hype.
- Area/subarea: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Cluster: 16 - action / robotics / vla / applications robotics
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=189; 7d visits=44
- Artifact: https://github.com/ZGC-EmbodyAI/LangForce; stars=69; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=RL / policy optimization; Bayesian / probabilistic; eval=vision/video; robotics/embodied; language/llm; security/safety
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/65457
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.15197

Abstract:

Vision-Language-Action (VLA) models have shown promise in robot manipulation but often struggle to generalize to new instructions or complex multi-task scenarios. We identify a critical pathology in current training paradigms where goal-driven data collection creates a dataset bias. In such datasets, language instructions are highly predictable from visual observations alone, causing the conditional mutual information between instructions and actions to vanish, a phenomenon we term Information Collapse. Consequently, models degenerate into vision-only policies that ignore language constraints. To address this, we propose LangForce, enforces instruction following via Bayesian decomposition. By introducing learnable Latent Action Queries, we construct a dual-branch architecture to estimate both a vision-only prior $p(a \mid v)$ and a language-conditioned posterior $\pi(a \mid v, \ell)$. We then optimize the policy to maximize the conditional Pointwise Mutual Information (PMI) between actions and instructions. This objective effectively penalizes the vision shortcut and rewards actions that explicitly explain the language command. Extensive experiments across on three benchmarks demonstrate substantial gains, including an 11.3\% improvement on the challenging OOD SimplerEnv benchmark, validating the ability of LangForce to robustly ground language in action.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 5. Vision-Language-Action Pretraining from Large-Scale Human Videos

Flags: robotics_public_not_program, github

- Review focus: Classify the source of public attention: benchmark, demo, artifact, model release, or hype.
- Area/subarea: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Cluster: 16 - action / robotics / vla / applications robotics
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=144; 7d visits=18
- Artifact: https://github.com/BeingBeyond/Being-H0; stars=52; manual-check=none
- Evidence tags: contribution=Position / conceptual; methods=LLM post-training; Reasoning / test-time compute; Agents / tool use; eval=vision/video; robotics/embodied; language/llm; theory/synthetic
- Benchmark/data/metric cues: none / none / accuracy
- ICML URL: https://icml.cc/virtual/2026/poster/62813
- AlphaXiv URL: https://www.alphaxiv.org/abs/2507.15597

Abstract:

Existing Vision-Language-Action (VLA) models struggle with complex manipulation tasks requiring high dexterity and generalization, primarily due to their reliance on synthetic data with significant sim-to-real gaps or limited teleoperated demonstrations. To address this bottleneck, we propose leveraging human hands as a manipulator template, capitalizing on the rich dexterity and scalability present in web data of human manipulation. Our approach introduces physical instruction tuning, a novel training paradigm that combines large-scale VLA pretraining from human videos, perspective spatial alignment for reasoning in a unified physical space, and post-training adaptation in physical environments. Additionally, we introduce a part-level motion tokenization method that achieves millimeter-level reconstruction accuracy to model precise hand trajectories serving as scalable motion primitives. To support our paradigm, we develop a comprehensive data curation pipeline that integrates heterogeneous sources into a large-scale dataset with millions of motion-based instructional instances. Empirically, our model demonstrates superior performance in hand motion generation and instruction following, adhering to favorable scaling laws with respect to model and data sizes. Importantly, we demonstrate promising capabilities to robotic dexterous manipulation, validating the effectiveness of bridging the human-robot embodiment gap.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 6. World Guidance: World Modeling in Condition Space for Action Generation

Flags: robotics_public_not_program, github

- Review focus: Classify the source of public attention: benchmark, demo, artifact, model release, or hype.
- Area/subarea: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Cluster: 16 - action / robotics / vla / applications robotics
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=108; 7d visits=33
- Artifact: https://github.com/Selen-Suyue/WoG; stars=147; manual-check=none
- Evidence tags: contribution=Application / domain study; methods=none; eval=vision/video; robotics/embodied; language/llm; theory/synthetic
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/61757
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.22010

Abstract:

Leveraging future observation modeling to facilitate action generation presents a promising avenue for enhancing the capabilities of Vision-Language-Action (VLA) models. However, existing approaches struggle to strike a balance between maintaining efficient, predictable future representations and preserving sufficient fine-grained information to guide precise action generation. To address this limitation, we propose WoG (World Guidance), a framework that maps future observations into compact conditions by injecting them into the action inference pipeline. The VLA is then trained to simultaneously predict these compressed conditions alongside future actions, thereby achieving effective world modeling within the condition space for action inference. We demonstrate that modeling and predicting this condition space not only facilitates fine-grained action generation but also exhibits superior generalization capabilities. Moreover, it learns effectively from substantial human manipulation videos. Extensive experiments across both simulation and real-world environments validate that WoG significantly outperforms existing methods based on future prediction.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 7. RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation

Flags: robotics_public_not_program, github

- Review focus: Classify the source of public attention: benchmark, demo, artifact, model release, or hype.
- Area/subarea: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Cluster: 16 - action / robotics / vla / applications robotics
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=91; 7d visits=55
- Artifact: https://github.com/RoboTwin-Platform/RoboTwin; stars=2562; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=Reasoning / test-time compute; Agents / tool use; eval=math/code/verifiable; vision/video; robotics/embodied; language/llm; theory/synthetic
- Benchmark/data/metric cues: none / none / success_rate
- ICML URL: https://icml.cc/virtual/2026/poster/62192
- AlphaXiv URL: https://www.alphaxiv.org/abs/2506.18088

Abstract:

Simulation-based data synthesis has emerged as a powerful paradigm for enhancing real-world robotic manipulation. However, existing synthetic datasets remain insufficient for robust bimanual manipulation due to two key challenges: (1) the lack of an autonomous self-correcting mechanism to resolve execution failures in complex coordination tasks, and (2) the scarcity of diverse visual and spatial variations required to bridge the sim-to-real gap. To this end, we present RoboTwin 2.0, a scalable simulation framework that enables closed-loop, automated, large-scale generation of diverse and realistic data, along with unified evaluation protocols for dual-arm manipulation. Built upon RoboTwin-OD, a foundational library of 731 instances across 147 categories with rich semantic annotations, our framework integrates Multimodal Large Language Models (MLLMs) with simulation-in-the-loop verification. This integration forms an automated feedback mechanism that significantly boosts the success rate of expert task program generation. To enhance robust sim-to-real transfer, RoboTwin 2.0 incorporates structured domain randomization along five axes: clutter, lighting, background, tabletop height and language instructions, thereby maximizing data diversity. We instantiate this framework across 50 dual-arm tasks spanning five robot embodiments. Empirical evaluations demonstrate that Vision-Language-Action (VLA) models pre-trained on our synthetic data achieve a 3.6x improvement in few-shot real-world transfer (over a 10-demo baseline) and a 2.2x gain in zero-shot generalization. We release the data generator, benchmark, pre-collected dataset, and code to support scalable research in robust bimanual manipulation.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 8. CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation

Flags: robotics_public_not_program

- Review focus: Classify the source of public attention: benchmark, demo, artifact, model release, or hype.
- Area/subarea: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Cluster: 16 - action / robotics / vla / applications robotics
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=86; 7d visits=106
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=RL / policy optimization; Reasoning / test-time compute; Agents / tool use; eval=math/code/verifiable; vision/video; robotics/embodied; language/llm; theory/synthetic
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/66369
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.22435

Abstract:

“Code-as-Policy” considers how executable code can complement data-intensive Vision-LanguageAction (VLA) methods, yet their effectiveness as autonomous controllers for embodied manipulation remains underexplored. We present CaPX, an open-access framework for systematically studying Code-as-Policy agents in robot manipulation. At its core is CaP-Gym, an interactive environment in which agents control robots by synthesizing and executing programs that compose perception and control primitives. Building on this foundation, CaP-Bench evaluates frontier language and vision-language models across varying levels of abstraction, interaction, and perceptual grounding. Across 7 simulation tasks and 12 models, CaP-Bench reveals a consistent trend: performance improves with human-crafted abstractions but degrades as these priors are removed, exposing a dependence on designer scaffolding. At the same time, we observe that this gap can be mitigated through scaling agentic test-time computation–through multi-turn interaction, structured execution feedback, visual differencing, automatic skill synthesis, and ensembled reasoning–substantially improves robustness even when agents operate over low-level primitives. These findings allow us to derive CaP-Agent0, a training-free framework that recovers human-level reliability on several manipulation tasks in simulation and on real embodiments. We further introduce CaP-RL, showing reinforcement learning with verifiable rewards improves success rates and transfers from sim2real with minimal gap. Together, CaP-X provides a principled, open-access platform for advancing embodied coding agents. Project page: https://cap-x-anonymous.github.io

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 9. RDT2: Exploring the Scaling Limit of UMI Data Towards Zero-Shot Cross-Embodiment Generalization

Flags: robotics_public_not_program, github

- Review focus: Classify the source of public attention: benchmark, demo, artifact, model release, or hype.
- Area/subarea: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Cluster: 16 - action / robotics / vla / applications robotics
- Cluster review: stable_seed; none
- Program/public: oral=false; award=none; votes=86; 7d visits=13
- Artifact: https://github.com/thu-ml/RDT2; stars=792; manual-check=none
- Evidence tags: contribution=Dataset / data resource; methods=Diffusion / flow; Compression / efficiency; eval=vision/video; robotics/embodied; language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/65782
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.03310

Abstract:

Vision-Language-Action (VLA) models hold promise for generalist robotics but currently struggle with data scarcity, architectural inefficiencies, and the inability to generalize across different hardware platforms. We introduce RDT2, a robotic foundation model built upon a 7B parameter VLM designed to enable zero-shot deployment on novel embodiments for open-vocabulary tasks. To achieve this, we collected one of the largest open-source robotic datasets—over $10,000$ hours of demonstrations in diverse families—using an enhanced, embodiment-agnostic Universal Manipulation Interface (UMI). Our approach employs a novel three-stage training recipe that aligns discrete linguistic knowledge with continuous control via Residual Vector Quantization (RVQ), flow-matching, and distillation for real-time inference. Consequently, RDT2 becomes one of the first models that simultaneously zero-shot generalizes to unseen objects, scenes, instructions, and even robotic platforms. Besides, it outperforms state-of-the-art baselines in dexterous, long-horizon, and dynamic downstream tasks like playing table tennis.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 10. RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies

Flags: robotics_program_anchor, oral, github

- Review focus: Compare public-heavy robotics papers against program-selected anchors.
- Area/subarea: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Cluster: 16 - action / robotics / vla / applications robotics
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=66; 7d visits=110
- Artifact: https://github.com/sled-group/navchat; stars=31; manual-check=none
- Evidence tags: contribution=Position / conceptual; methods=Agents / tool use; eval=math/code/verifiable; vision/video; robotics/embodied; language/llm
- Benchmark/data/metric cues: RoboMME / none / memory
- ICML URL: https://icml.cc/virtual/2026/poster/65933
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.04639

Abstract:

Memory is critical for long-horizon and history-dependent robotic manipulation. Such tasks often involve counting repeated actions or manipulating objects that become temporarily occluded. Recent vision-language-action (VLA) models have begun to incorporate memory mechanisms; however, their evaluations remain confined to narrow, non-standardized settings. This limits their systematic understanding, comparison, and progress measurement. To address these challenges, we introduce **RoboMME**: a large-scale standardized benchmark for evaluating and advancing VLA models in long-horizon, history-dependent scenarios. Our benchmark comprises 16 manipulation tasks constructed under a carefully designed taxonomy that evaluates temporal, spatial, object, and procedural memory. We further develop a suite of 14 memory-augmented VLA variants built on the $\pi_{0.5}$ backbone to systematically explore different memory representations across multiple integration strategies. We show that the effectiveness of memory representations is highly task-dependent, with each design offering distinct advantages and limitations across different tasks. Videos and code can be found in https://anonymtest1.github.io

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 11. From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models

Flags: robotics_program_anchor, oral, github

- Review focus: Compare public-heavy robotics papers against program-selected anchors.
- Area/subarea: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Cluster: 16 - action / robotics / vla / applications robotics
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=30; 7d visits=20
- Artifact: https://github.com/RUCKBReasoning/From_Pixels_to_Tokens; stars=35; manual-check=none
- Evidence tags: contribution=Dataset / data resource; methods=Reasoning / test-time compute; eval=vision/video; robotics/embodied; language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/63621
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.04678

Abstract:

Latent actions serve as an intermediate representation that enables consistent modeling of vision-language-action (VLA) models across heterogeneous datasets. However, approaches to supervising VLAs with latent actions are fragmented and lack a systematic comparison. This work structures the study of latent action supervision from two perspectives: (i) regularizing the trajectory via image-based latent actions, and (ii) unifying the target space with action-based latent actions. Under a unified VLA baseline, we instantiate and compare four representative integration strategies. Our results reveal a formulation-task correspondence: image-based latent actions benefit long-horizon reasoning, whereas action-based latent actions excel at complex motor coordination. Furthermore, we find that directly supervising the VLM with discrete latent action tokens yields the most effective performance. Finally, our experiments offer initial insights into the benefits of latent action supervision in mixed-data, suggesting a promising direction for VLA training.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 12. XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations

Flags: robotics_program_anchor, oral

- Review focus: Compare public-heavy robotics papers against program-selected anchors.
- Area/subarea: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Cluster: 16 - action / robotics / vla / applications robotics
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=19; 7d visits=28
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Dataset / data resource; methods=RL / policy optimization; LLM post-training; Agents / tool use; eval=math/code/verifiable; vision/video; robotics/embodied; language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/64826
- AlphaXiv URL: https://www.alphaxiv.org/abs/2511.02776

Abstract:

Recent progress in large-scale robotic datasets and vision-language models (VLMs) has advanced research on vision-language-action (VLA) models. However, existing VLA models still face two fundamental challenges: (\textit{i}) producing precise low-level actions from high-dimensional observations, (\textit{ii}) bridging domain gaps across heterogeneous data sources, including diverse robot embodiments and human demonstrations. Existing methods often encode latent variables from either visual dynamics or robotic actions to guide policy learning, but they fail to fully exploit the complementary multi-modal knowledge present in large-scale, heterogeneous datasets. In this work, we present \textbf{XR-1}, a novel framework for versatile and scalable VLA learning across diverse robots, tasks, and environments. At its core, XR-1 introduces the \emph{Unified Vision-Motion Codes (UVMC)}, a discrete latent representation learned via a dual-branch VQ-VAE that jointly encodes visual dynamics and robotic motion. UVMC addresses these challenges by (\textit{i}) serving as an intermediate representation between the observations and actions, and (\textit{ii}) aligning multimodal dynamic information from heterogeneous data sources to capture complementary knowledge. To effectively exploit UVMC, we propose a \emph{three-stage training paradigm}: (\textit{i}) self-supervised UVMC learning, (\textit{ii}) UVMC-guided pretraining on large-scale cross-embodiment robotic datasets, and (\textit{iii}) task-specific post-training. We validate XR-1 through extensive real-world experiments with more than 12,000 rollouts on six different robot embodiments, spanning over 120 diverse manipulation tasks. XR-1 consistently outperforms state-of-the-art baselines such as $\pi_0$ and GR00T-N1.5 while demonstrating strong generalization to novel objects, background variations, distractors, and illumination changes. Our project is at \href{https://xr-1-vla.github.io/}{https://xr-1-vla.github.io/}, and our code will be open-sourced.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:
