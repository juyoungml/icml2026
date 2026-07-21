# Reinforcement Learning and Control

Core RL is active but less publicly amplified than LLM-facing RL, with emphasis on offline learning, control, and computation.

## Signal Snapshot

- Papers: 312 (4.7% of corpus)
- Oral enrichment: 0.76x
- Public-attention enrichment: 0.66x
- Historical accepted-paper delta: +0.9 pp
- GitHub URL share: 20.5%
- Manual area-review progress: 0/16 rows reviewed; 16 remaining
- Trust tier: `moderate_review_need` - 38 low-confidence evidence-code rows in full area

## Fault Lines

- Classical RL/control objectives versus foundation-model-era policy learning.
- Offline and preference-based RL versus online exploration and sample efficiency.
- Theoretical computation limits versus practical robotic/control deployment.

## Read For

- Does the method require online interaction or strong simulator assumptions?
- How are stability, exploration, and reward misspecification handled?
- Is the contribution algorithmic, theoretical, or a new evaluation/control setting?

## Shape Of The Area

- Top subareas: Core RL, offline RL, and policy optimization (312)
- Method-family cues: RL / policy optimization (305); Agents / tool use (116); Diffusion / flow (82); Graphs / geometry (48); Compression / efficiency (45); Reasoning / test-time compute (38); LLM post-training (36); Bayesian / probabilistic (27)
- Evaluation-setting cues: robotics/embodied (154); theory/synthetic (109); security/safety (50); math/code/verifiable (33); language/llm (30); vision/video (24); science/domain (1)
- Contribution mix: Benchmark / evaluation (105); Theory / proof (82); Method / algorithm (53); Position / conceptual (26); System / infrastructure (15); Application / domain study (14); Dataset / data resource (12); Uncoded (5)
- Evidence confidence: medium (274); low (38)

## Start Here

- On Computation and Reinforcement Learning (oral; votes=11; github_stars=168)
- Learning Human-Robot Collaboration via Heterogeneous-Agent Lyapunov Policy Optimization (oral; votes=10)
- Distributional Inverse Reinforcement Learning (oral; votes=5; github_stars=474)
- Chebyshev Policies and the Mountain Car Problem: Reinforcement Learning for Low-dimensional Control Tasks (oral; votes=3)
- Stabilizing the Q-Gradient Field for Policy Smoothness in Actor-Critic Methods (oral; votes=2)
- Video-Based Optimal Transport for Feedback-Efficient Offline Preference-Based Reinforcement Learning (oral; votes=0)

## Public Attention Not Program-Selected

- Reinforcement Learning with Verifiable Rewards: GRPO's Loss, Dynamics, and Success Amplification (votes=305)
- Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers (votes=135)
- How Does the Lagrangian Guide Safe Reinforcement Learning through Diffusion Models? (votes=119; github_stars=13)
- Just-In-Time Reinforcement Learning: Continual Learning in LLM Agents Without Gradient Updates (votes=61; github_stars=59)
- T$^2$PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning (votes=56; github_stars=45)
- Parallel Stochastic Gradient-Based Planning for World Models (votes=44)

## Artifact-Visible Papers To Inspect

- DADP: Domain Adaptive Diffusion Policy (votes=5; github_stars=1969)
- Distributional Inverse Reinforcement Learning (oral; votes=5; github_stars=474)
- Chunk-Guided Q-Learning (votes=12; github_stars=435)
- RulePlanner: All-in-One Reinforcement Learner for Unifying Design Rules in 3D Floorplanning (votes=1; github_stars=314)
- Optimizing Return Distributions with Distributional Dynamic Programming (votes=8; github_stars=292)
- Distributional Active Inference (votes=6; github_stars=292)

## Boundary / Taxonomy Review Candidates

- No high-signal `needs_review` papers in this area briefing sample.

## What Could Break This Area Story

- The area taxonomy is generated from semantic clusters and curated mappings, not full manual paper reading.
- Public attention is AlphaXiv attention; it can reflect sharing dynamics rather than technical importance.
- GitHub URL share is artifact visibility, not runnable reproducibility.
- Evidence-code labels are heuristic and should be checked against the paper before making benchmark, dataset, metric, or result-character claims.