# Robotics, Embodiment, and World Models

Manual validation packet for representative and boundary papers.

## Area Context

Headline: Robotics is becoming a high-attention testbed for VLA models, memory, latent actions, and world models.

Fault lines:
- Vision-language-action pretraining versus robot-specific policy learning.
- Latent action/world-model abstractions versus real-world manipulation reliability.
- Benchmark scaling versus sim-to-real and long-horizon generalization.

What to read for:
- Does the model actually improve physical task success or only representation quality?
- Are actions, memory, and world states evaluated under distribution shift?
- How much depends on synthetic data, simulation, or curated demonstrations?

## Queue Summary

- Papers: 16
- Selection mix: fault_line_representative=6, low_evidence_code_confidence=6, public_attention_not_program_signal=4
- Papers from taxonomy-review clusters: 0
- Papers with GitHub URLs: 8

## Papers

### 1. RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies

Flags: fault_line_representative, oral, github

- Subarea: Vision-language-action models and robotic manipulation
- Votes: 66
- ICML URL: https://icml.cc/virtual/2026/poster/65933
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.04639
- GitHub URL: https://github.com/sled-group/navchat
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Benchmark / evaluation; System / infrastructure; Application / domain study
- Method families: Agents / tool use
- Evaluation settings: math/code/verifiable; vision/video; robotics/embodied; language/llm
- Result claim cues: negative / limitation; scaling / efficiency
- Benchmarks: RoboMME
- Datasets: none
- Metrics: memory

Abstract:

Memory is critical for long-horizon and history-dependent robotic manipulation. Such tasks often involve counting repeated actions or manipulating objects that become temporarily occluded. Recent vision-language-action (VLA) models have begun to incorporate memory mechanisms; however, their evaluations remain confined to narrow, non-standardized settings. This limits their systematic understanding, comparison, and progress measurement. To address these challenges, we introduce **RoboMME**: a large-scale standardized benchmark for evaluating and advancing VLA models in long-horizon, history-dependent scenarios. Our benchmark comprises 16 manipulation tasks constructed under a carefully designed taxonomy that evaluates temporal, spatial, object, and procedural memory. We further develop a suite of 14 memory-augmented VLA variants built on the $\pi_{0.5}$ backbone to systematically explore different memory representations across multiple integration strategies. We show that the effectiveness of memory representations is highly task-dependent, with each design offering distinct advantages and limitations across different tasks. Videos and code can be found in https://anonymtest1.github.io

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

### 2. From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models

Flags: fault_line_representative, oral, github

- Subarea: Vision-language-action models and robotic manipulation
- Votes: 30
- ICML URL: https://icml.cc/virtual/2026/poster/63621
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.04678
- GitHub URL: https://github.com/RUCKBReasoning/From_Pixels_to_Tokens
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Application / domain study; Method / algorithm
- Method families: Reasoning / test-time compute
- Evaluation settings: vision/video; robotics/embodied; language/llm
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Latent actions serve as an intermediate representation that enables consistent modeling of vision-language-action (VLA) models across heterogeneous datasets. However, approaches to supervising VLAs with latent actions are fragmented and lack a systematic comparison. This work structures the study of latent action supervision from two perspectives: (i) regularizing the trajectory via image-based latent actions, and (ii) unifying the target space with action-based latent actions. Under a unified VLA baseline, we instantiate and compare four representative integration strategies. Our results reveal a formulation-task correspondence: image-based latent actions benefit long-horizon reasoning, whereas action-based latent actions excel at complex motor coordination. Furthermore, we find that directly supervising the VLM with discrete latent action tokens yields the most effective performance. Finally, our experiments offer initial insights into the benefits of latent action supervision in mixed-data, suggesting a promising direction for VLA training.

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

### 3. XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations

Flags: fault_line_representative, oral

- Subarea: Vision-language-action models and robotic manipulation
- Votes: 19
- ICML URL: https://icml.cc/virtual/2026/poster/64826
- AlphaXiv URL: https://www.alphaxiv.org/abs/2511.02776
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; System / infrastructure; Application / domain study; Method / algorithm
- Method families: RL / policy optimization; LLM post-training; Agents / tool use
- Evaluation settings: math/code/verifiable; vision/video; robotics/embodied; language/llm
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Recent progress in large-scale robotic datasets and vision-language models (VLMs) has advanced research on vision-language-action (VLA) models. However, existing VLA models still face two fundamental challenges: (\textit{i}) producing precise low-level actions from high-dimensional observations, (\textit{ii}) bridging domain gaps across heterogeneous data sources, including diverse robot embodiments and human demonstrations. Existing methods often encode latent variables from either visual dynamics or robotic actions to guide policy learning, but they fail to fully exploit the complementary multi-modal knowledge present in large-scale, heterogeneous datasets. In this work, we present \textbf{XR-1}, a novel framework for versatile and scalable VLA learning across diverse robots, tasks, and environments. At its core, XR-1 introduces the \emph{Unified Vision-Motion Codes (UVMC)}, a discrete latent representation learned via a dual-branch VQ-VAE that jointly encodes visual dynamics and robotic motion. UVMC addresses these challenges by (\textit{i}) serving as an intermediate representation between the observations and actions, and (\textit{ii}) aligning multimodal dynamic information from heterogeneous data sources to capture complementary knowledge. To effectively exploit UVMC, we propose a \emph{three-stage training paradigm}: (\textit{i}) self-supervised UVMC learning, (\textit{ii}) UVMC-guided pretraining on large-scale cross-embodiment robotic datasets, and (\textit{iii}) task-specific post-training. We validate XR-1 through extensive real-world experiments with more than 12,000 rollouts on six different robot embodiments, spanning over 120 diverse manipulation tasks. XR-1 consistently outperforms state-of-the-art baselines such as $\pi_0$ and GR00T-N1.5 while demonstrating strong generalization to novel objects, background variations, distractors, and illumination changes. Our project is at \href{https://xr-1-vla.github.io/}{https://xr-1-vla.github.io/}, and our code will be open-sourced.

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

### 4. From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model

Flags: fault_line_representative, oral, github

- Subarea: Vision-language-action models and robotic manipulation
- Votes: 14
- ICML URL: https://icml.cc/virtual/2026/poster/66596
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.22671
- GitHub URL: https://github.com/eliahuhorwitz/Academic-project-page-template
- Artifact confidence: needs_manual_check
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Application / domain study
- Contribution types: Application / domain study; Method / algorithm
- Method families: LLM post-training; Causal / data-centric
- Evaluation settings: vision/video; robotics/embodied; language/llm
- Result claim cues: negative / limitation; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Vision-Language-Action (VLA) models often suffer from performance degradation under distribution shifts, as they struggle to learn generalized behavior representations across varying environments. While existing approaches attempt to construct behavior representations through action-centric latent variables, they are often limited by short-horizon temporal fragmentation and static execution-alignment, leading to inconsistent behaviors in complex scenarios. To address these limitations, we propose \textbf{BehaviorVLA}, a framework that facilitates robust manipulation through the learning of a temporally coherent behavioral representations. Our approach features two symmetric components: (1) the \textbf{Visuomotor Behavior Encoder (VBE)}, which utilizes a causal Mamba-based architecture to aggregate long-horizon trajectory information into a unified behavior representation; and (2) the \textbf{Phase-conditioned Behavior Decoder (PBD)}, which decodes this representation into precise actions by dynamically aligning task-level priors with real-time execution progress. Experiments on RoboTwin 2.0, LIBERO, and CALVIN demonstrate state-of-the-art success rates of 58\%, 98\%, and 4.36 (Avg. Len), respectively. Notably, in real-world sim-to-real transfer, BehaviorVLA matches the performance of OpenVLA-OFT using only 50\% of the demonstration data, showcasing its superior data efficiency and generalization.

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

### 5. Learning Latent Action World Models In The Wild

Flags: fault_line_representative

- Subarea: Vision-language-action models and robotic manipulation
- Votes: 273
- ICML URL: https://icml.cc/virtual/2026/poster/65056
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.05230
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Application / domain study; Method / algorithm
- Method families: RL / policy optimization; Agents / tool use; Compression / efficiency
- Evaluation settings: vision/video; robotics/embodied
- Result claim cues: scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Agents that can reason and plan in the real world must be able to predict the consequences of their actions. World models possess this capability but require action annotations that can be complex to obtain at scale. Latent action models address this issue by learning an action space from videos alone. Our work studies the training of latent action world models on in-the-wild videos, expanding the scope of existing works that focus on simple robotics simulations, video games, or manipulation data. While diverse videos enable modeling richer actions, they introduce challenges of environmental noise and lack of a common embodiment across videos. To address these, we carefully study the design and evaluation of latent actions. We find that constrained continuous latent actions are better suited for complex in-the-wild videos, compared to vector quantization. For example, actions specific to in-the-wild videos such as humans entering the room, can be modeled and then transferred across videos. However, in the absence of a common embodiment, learned latent actions are localized in space, relative to the camera. Nonetheless, we are able to train a controller that maps known actions to latent ones, allowing us to use latent actions as a universal interface to solve planning tasks on par with action-conditioned baselines.

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

### 6. Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies

Flags: fault_line_representative, github

- Subarea: Vision-language-action models and robotic manipulation
- Votes: 204
- ICML URL: https://icml.cc/virtual/2026/poster/62902
- AlphaXiv URL: https://www.alphaxiv.org/abs/2508.20072
- GitHub URL: https://github.com/Liang-ZX/DiscreteDiffusionVLA
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Application / domain study; Method / algorithm
- Method families: RL / policy optimization; Diffusion / flow; Transformer / attention
- Evaluation settings: vision/video; robotics/embodied; language/llm
- Result claim cues: scaling / efficiency; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Vision–Language–Action (VLA) models adapt large vision–language backbones to map images and instructions into robot actions. However, prevailing VLAs either generate actions autoregressively in a fixed left-to-right order or attach separate diffusion heads outside the backbone, fragmenting information pathways and hindering unified, scalable architectures. We present Discrete Diffusion VLA, a unified-transformer policy that models discretized action chunks with discrete diffusion retaining progressive refinement inside the VLM backbone. Our method achieves an adaptive decoding order that resolves high-confidence (easy) action elements before harder ones and employs secondary re-masking to revisit uncertain predictions, enabling robust error correction. This design preserves pretrained vision-language priors, supports parallel decoding, and improves the efficiency. Discrete Diffusion VLA achieves 96.5% avg.~success on LIBERO, 71.2% visual matching on SimplerEnv-Fractal, and 54.2% overall on SimplerEnv-Bridge. On out-of-distribution benchmarks, our method exhibits only 1.4% language degradation versus 8.0% for parallel decoding, and 21.0% vision degradation versus 29.0% for continuous diffusion, demonstrating well retention of pretrained vision-language capabilities. Visualization analysis confirms the learned decoding order adaptively prioritizes high-confidence tokens, validating our refinement strategy.

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

### 7. Temporal Straightening for Latent Planning

Flags: public_attention_not_program_signal, evidence-very_low, github

- Subarea: Vision-language-action models and robotic manipulation
- Votes: 202
- ICML URL: https://icml.cc/virtual/2026/poster/64904
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.12231
- GitHub URL: https://github.com/agentic-learning-ai-lab/temporal-straightening
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Uncoded
- Contribution types: none
- Method families: none
- Evaluation settings: none
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Learning good representations is essential for latent planning with world models. While pretrained visual encoders provide strong visual features, they are not tailored to planning and contain substantial information which is irrelevant to planning. Inspired by the perceptual straightening hypothesis in human visual processing, we introduce temporal straightening for representation learning in latent planning. We add a lightweight projector on top of a pretrained visual encoder to map to a lower-dimensional space, trained with a curvature regularizer that encourages locally straightened latent trajectories. We show that reducing curvature improves the conditioning of the planning objective, making gradient-based planning more stable and yielding significantly higher success rates across four goal-reaching tasks.

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

### 8. LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries

Flags: public_attention_not_program_signal, github

- Subarea: Vision-language-action models and robotic manipulation
- Votes: 189
- ICML URL: https://icml.cc/virtual/2026/poster/65457
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.15197
- GitHub URL: https://github.com/ZGC-EmbodyAI/LangForce
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; Application / domain study; Method / algorithm
- Method families: RL / policy optimization; Bayesian / probabilistic
- Evaluation settings: vision/video; robotics/embodied; language/llm; security/safety
- Result claim cues: robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Vision-Language-Action (VLA) models have shown promise in robot manipulation but often struggle to generalize to new instructions or complex multi-task scenarios. We identify a critical pathology in current training paradigms where goal-driven data collection creates a dataset bias. In such datasets, language instructions are highly predictable from visual observations alone, causing the conditional mutual information between instructions and actions to vanish, a phenomenon we term Information Collapse. Consequently, models degenerate into vision-only policies that ignore language constraints. To address this, we propose LangForce, enforces instruction following via Bayesian decomposition. By introducing learnable Latent Action Queries, we construct a dual-branch architecture to estimate both a vision-only prior $p(a \mid v)$ and a language-conditioned posterior $\pi(a \mid v, \ell)$. We then optimize the policy to maximize the conditional Pointwise Mutual Information (PMI) between actions and instructions. This objective effectively penalizes the vision shortcut and rewards actions that explicitly explain the language command. Extensive experiments across on three benchmarks demonstrate substantial gains, including an 11.3\% improvement on the challenging OOD SimplerEnv benchmark, validating the ability of LangForce to robustly ground language in action.

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

### 9. Vision-Language-Action Pretraining from Large-Scale Human Videos

Flags: public_attention_not_program_signal, github

- Subarea: Vision-language-action models and robotic manipulation
- Votes: 144
- ICML URL: https://icml.cc/virtual/2026/poster/62813
- AlphaXiv URL: https://www.alphaxiv.org/abs/2507.15597
- GitHub URL: https://github.com/BeingBeyond/Being-H0
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Dataset / data resource; System / infrastructure; Application / domain study; Method / algorithm
- Method families: LLM post-training; Reasoning / test-time compute; Agents / tool use
- Evaluation settings: vision/video; robotics/embodied; language/llm; theory/synthetic
- Result claim cues: negative / limitation; scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: accuracy

Abstract:

Existing Vision-Language-Action (VLA) models struggle with complex manipulation tasks requiring high dexterity and generalization, primarily due to their reliance on synthetic data with significant sim-to-real gaps or limited teleoperated demonstrations. To address this bottleneck, we propose leveraging human hands as a manipulator template, capitalizing on the rich dexterity and scalability present in web data of human manipulation. Our approach introduces physical instruction tuning, a novel training paradigm that combines large-scale VLA pretraining from human videos, perspective spatial alignment for reasoning in a unified physical space, and post-training adaptation in physical environments. Additionally, we introduce a part-level motion tokenization method that achieves millimeter-level reconstruction accuracy to model precise hand trajectories serving as scalable motion primitives. To support our paradigm, we develop a comprehensive data curation pipeline that integrates heterogeneous sources into a large-scale dataset with millions of motion-based instructional instances. Empirically, our model demonstrates superior performance in hand motion generation and instruction following, adhering to favorable scaling laws with respect to model and data sizes. Importantly, we demonstrate promising capabilities to robotic dexterous manipulation, validating the effectiveness of bridging the human-robot embodiment gap.

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

### 10. World Guidance: World Modeling in Condition Space for Action Generation

Flags: public_attention_not_program_signal, evidence-low, github

- Subarea: Vision-language-action models and robotic manipulation
- Votes: 108
- ICML URL: https://icml.cc/virtual/2026/poster/61757
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.22010
- GitHub URL: https://github.com/Selen-Suyue/WoG
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Application / domain study
- Contribution types: Application / domain study; Method / algorithm
- Method families: none
- Evaluation settings: vision/video; robotics/embodied; language/llm; theory/synthetic
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Leveraging future observation modeling to facilitate action generation presents a promising avenue for enhancing the capabilities of Vision-Language-Action (VLA) models. However, existing approaches struggle to strike a balance between maintaining efficient, predictable future representations and preserving sufficient fine-grained information to guide precise action generation. To address this limitation, we propose WoG (World Guidance), a framework that maps future observations into compact conditions by injecting them into the action inference pipeline. The VLA is then trained to simultaneously predict these compressed conditions alongside future actions, thereby achieving effective world modeling within the condition space for action inference. We demonstrate that modeling and predicting this condition space not only facilitates fine-grained action generation but also exhibits superior generalization capabilities. Moreover, it learns effectively from substantial human manipulation videos. Extensive experiments across both simulation and real-world environments validate that WoG significantly outperforms existing methods based on future prediction.

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

### 11. Contrastive Representation Regularization for Vision-Language-Action Models

Flags: low_evidence_code_confidence, evidence-low

- Subarea: Vision-language-action models and robotic manipulation
- Votes: 20
- ICML URL: https://icml.cc/virtual/2026/poster/62819
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.01711
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Application / domain study; Method / algorithm
- Method families: none
- Evaluation settings: vision/video; robotics/embodied; language/llm
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Vision-Language-Action (VLA) models have shown strong capabilities in robot manipulation by leveraging rich representations from pre-trained Vision-Language Models (VLMs). However, their representations arguably remain suboptimal, lacking sensitivity to robotic signals such as control actions and proprioceptive information. To address the issue, we introduce Robot State-aware Contrastive Loss (RS-CL), a simple and effective representation regularization for VLA models, designed to bridge the gap between VLM representations and robotic signals. In particular, RS-CL aligns the representations more closely with the robot's proprioceptive states by using relative distances between the states as soft supervision. Complementing the original action prediction objective, RS-CL enhances control-relevant representation learning, while being lightweight and fully compatible with standard VLA training pipelines. Our empirical results demonstrate that RS-CL substantially improves the performance of state-of-the-art VLA models; it pushes the prior art to 69.7% achieving the state-of-the-art performance on the RoboCasa-Kitchen benchmark, and boosts success rates from 45.0% to 58.3% on challenging real-robot manipulation tasks.

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

### 12. Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language

Flags: low_evidence_code_confidence, evidence-low

- Subarea: Vision-language-action models and robotic manipulation
- Votes: 13
- ICML URL: https://icml.cc/virtual/2026/poster/65669
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.27886
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Application / domain study; Method / algorithm
- Method families: none
- Evaluation settings: vision/video; robotics/embodied; language/llm
- Result claim cues: scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Tactile sensing is essential for robots to achieve human-like gentle manipulation capabilities. However, existing Vision-Language-Action (VLA) models struggle to exploit tactile feedback for gentle manipulation due to the scarcity of aligned vision-tactile-language data and the lack of effective closed-loop force feedback mechanisms. To address these challenges, we introduce Tabero, a benchmark and model suite for gentle, language-conditioned robotic manipulation that demands fine-grained contact force perception. First, the Tabero benchmark addresses the scarcity of tactile data by presenting a data-efficient pipeline that repurposes open-source robot manipulation trajectories to generate a diverse set of vision-tactile-language tasks, and establishes a multidimensional evaluation protocol that measures task success alongside physical interaction quality. Second, we propose Tabero-VTLA, a Vision-Tactile-Language-Action architecture featuring a decoupled force-position command interface; the resulting force-position commands are executed by a fixed hybrid controller to enable real-time, force-aware manipulation. Evaluated on Tabero, our model maintains high task success while reducing average grip force by over 70% under gentle instructions, demonstrating its ability to modulate interaction forces based on multimodal experience.

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

### 13. SKETCH: Semantic Key-Point Conditioning for Long-Horizon Vessel Trajectory Prediction

Flags: low_evidence_code_confidence, evidence-low

- Subarea: Vision-language-action models and robotic manipulation
- Votes: 1
- ICML URL: https://icml.cc/virtual/2026/poster/64033
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.18537
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: none
- Evaluation settings: none
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: accuracy

Abstract:

Accurate long-horizon vessel trajectory prediction remains challenging due to compounded uncertainty from complex navigation behaviors and environmental factors. Existing methods often struggle to maintain global directional consistency, leading to drifting or implausible trajectories when extrapolated over long time horizons. To address this issue, we propose a semantic-key-point-conditioned trajectory modeling framework, in which future trajectories are predicted by conditioning on a high-level Next Key Point (NKP) that captures navigational intent. This formulation decomposes long-horizon prediction into global semantic decision-making and local motion modeling, effectively restricting the support of future trajectories to semantically feasible subsets. To efficiently estimate the NKP prior from historical observations, we adopt a pretrain-finetune strategy. Extensive experiments on real-world AIS data demonstrate that the proposed method consistently outperforms state-of-the-art approaches, particularly for long travel durations, directional accuracy, and fine-grained trajectory prediction.

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

### 14. Cross-Embodiment Robot Foundation World Models with Latent Actions

Flags: low_evidence_code_confidence, evidence-low

- Subarea: Vision-language-action models and robotic manipulation
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/63978
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Application / domain study
- Method families: none
- Evaluation settings: robotics/embodied
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

The diversity of robot embodiments and action spaces makes it challenging to build robot world models that generalize across different embodiments. We introduce a Latent Action Conditioned Robot World Model (LAC-WM), which operates within a learned unified latent action space shared across diverse embodiments. We show how this unified action space improves the world model’s performance when adapted to previously unseen robot embodiments. We compare LAC-WM to a baseline model, Explicit Action Conditioned World Model (EAC-WM) conditioned on explicit motion labels. Our results show that conditioning on explicit labels creates disjoint action spaces across embodiments, limiting downstream task performance when adapting to new robots. We evaluate both models on a dexterous manipulation task. The latent action-conditioned model LAC-WM achieves up to a 46.7% improvement in performance over EAC-WM. Crucially, the unified latent action space allows LAC-WM’s downstream performance to scale positively with the number of embodiments used during pretraining. In contrast, the disjoint action space in EAC-WM leads to decreased performance as the number of pretraining embodiments increases. These results highlights the importance of a unified action space for efficient cross-embodiment learning, addressing a key challenge in robotics.

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

### 15. Joint-Space Empowerment as a Theory of Dexterous Motor Coordination

Flags: low_evidence_code_confidence, evidence-low

- Subarea: Vision-language-action models and robotic manipulation
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/61426
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Uncoded
- Contribution types: none
- Method families: RL / policy optimization; Agents / tool use; Graphs / geometry
- Evaluation settings: robotics/embodied; theory/synthetic
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Searching for effective policies in high-dimensional action spaces is notoriously challenging. This difficulty is compounded in overactuated musculoskeletal systems, where multiple muscles span each joint, and individual muscles actuate multiple joints. Although this redundancy complicates naive policy search, it also implies that effective control can be captured by a low-dimensional action manifold. To identify such a manifold, we introduce *joint-space empowerment (JSE)*, a novel information-theoretic principle that quantifies how much control an agent has over its body. We use JSE to discover high-empowerment action manifolds, and demonstrate that manipulation policies learned on these manifolds show significantly enhanced dexterity, sample efficiency and improved generalization. These results suggest a general principle for motor coordination in high-dimensional, overactuated systems, with implications for both biological motor control and embodied artificial agents.

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

### 16. Learning to Move Before Learning to Do: Task-Agnostic pretraining for VLAs

Flags: low_evidence_code_confidence, evidence-low

- Subarea: Vision-language-action models and robotic manipulation
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/64730
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; Application / domain study; Method / algorithm
- Method families: none
- Evaluation settings: vision/video; robotics/embodied; language/llm
- Result claim cues: scaling / efficiency; robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Vision-Language-Action (VLA) models are bottlenecked by the scarcity of expert demonstrations—expensive triplets of observations, language instructions, and actions. We propose that learning ''how to move'' can be decoupled from learning ''what to do,'' and that the former requires no task labels at all. Our two-stage framework, **Task-Agnostic Pretraining (TAP)** first pre-trains on abundant, cheap *task-agnostic* data (discarded off-task trajectories or autonomous robot play) using an Inverse Dynamics objective that predicts actions from consecutive observations. This self-supervised phase instills physical affordances—grasping, contact dynamics, end-effector control—without human annotation. A lightweight second stage then aligns these physical priors with language instructions using minimal expert data. On the SIMPLER benchmark, our approach matches models trained on 1M+ expert trajectories while using orders of magnitude less labeled data, achieving a 10\% absolute gain over standard behavior cloning. In real-world WidowX experiments, it surpasses internet-scale baselines under visual distribution shifts (e.g., 25\% vs. 0\% under camera perturbations), demonstrating that task-agnostic pretraining yields robust, transferable physical representations for Embodied AI.

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
