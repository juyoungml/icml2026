# Robotics, Embodiment, and World Models

Robotics is becoming a high-attention testbed for VLA models, memory, latent actions, and world models.

## Signal Snapshot

- Papers: 195 (2.9% of corpus)
- Oral enrichment: 0.81x
- Public-attention enrichment: 2.11x
- Historical accepted-paper delta: +0.4 pp
- GitHub URL share: 38.0%
- Manual area-review progress: 0/16 rows reviewed; 16 remaining
- Trust tier: `moderate_review_need` - public attention exceeds program signal; 9 low-confidence evidence-code rows in full area

## Fault Lines

- Vision-language-action pretraining versus robot-specific policy learning.
- Latent action/world-model abstractions versus real-world manipulation reliability.
- Benchmark scaling versus sim-to-real and long-horizon generalization.

## Read For

- Does the model actually improve physical task success or only representation quality?
- Are actions, memory, and world states evaluated under distribution shift?
- How much depends on synthetic data, simulation, or curated demonstrations?

## Shape Of The Area

- Top subareas: Vision-language-action models and robotic manipulation (195)
- Method-family cues: RL / policy optimization (104); Agents / tool use (81); Reasoning / test-time compute (59); Diffusion / flow (44); LLM post-training (42); Graphs / geometry (22); Compression / efficiency (21); Transformer / attention (21)
- Evaluation-setting cues: robotics/embodied (171); vision/video (130); language/llm (103); theory/synthetic (55); math/code/verifiable (33); security/safety (19); science/domain (17)
- Contribution mix: Benchmark / evaluation (91); Application / domain study (34); Dataset / data resource (24); Method / algorithm (15); Position / conceptual (10); System / infrastructure (10); Theory / proof (9); Uncoded (2)
- Evidence confidence: medium (186); low (8); very_low (1)

## Start Here

- RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies (oral; votes=66; github_stars=31)
- From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models (oral; votes=30; github_stars=35)
- XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations (oral; votes=19)
- From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model (oral; votes=14; github_stars=5069)
- Learning Latent Action World Models In The Wild (votes=273)
- Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies (votes=204; github_stars=69)

## Public Attention Not Program-Selected

- Learning Latent Action World Models In The Wild (votes=273)
- Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies (votes=204; github_stars=69)
- Temporal Straightening for Latent Planning (votes=202; github_stars=92)
- LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries (votes=189; github_stars=69)
- Vision-Language-Action Pretraining from Large-Scale Human Videos (votes=144; github_stars=52)
- World Guidance: World Modeling in Condition Space for Action Generation (votes=108; github_stars=147)

## Artifact-Visible Papers To Inspect

- From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model (oral; votes=14; github_stars=5069) manual-check
- LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model (votes=73; github_stars=5063) manual-check
- Hydra-Nav: Object Navigation via Adaptive Dual-Process Reasoning (votes=15; github_stars=5063) manual-check
- RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation (votes=91; github_stars=2562)
- VLANeXt: Recipes for Building Strong VLA Models (votes=74; github_stars=833) manual-check
- RDT2: Exploring the Scaling Limit of UMI Data Towards Zero-Shot Cross-Embodiment Generalization (votes=86; github_stars=792)

## Boundary / Taxonomy Review Candidates

- No high-signal `needs_review` papers in this area briefing sample.

## What Could Break This Area Story

- The area taxonomy is generated from semantic clusters and curated mappings, not full manual paper reading.
- Public attention is AlphaXiv attention; it can reflect sharing dynamics rather than technical importance.
- GitHub URL share is artifact visibility, not runnable reproducibility.
- Evidence-code labels are heuristic and should be checked against the paper before making benchmark, dataset, metric, or result-character claims.