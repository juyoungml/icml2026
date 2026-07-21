# LLM Reasoning, Post-Training, and RLVR

Reasoning progress is splitting between reward-driven post-training, test-time search, and alternative sequence modeling.

## Signal Snapshot

- Papers: 1,099 (16.6% of corpus)
- Oral enrichment: 1.29x
- Public-attention enrichment: 2.03x
- Historical accepted-paper delta: +2.9 pp
- GitHub URL share: 32.1%
- Manual area-review progress: 0/16 rows reviewed; 16 remaining
- Trust tier: `high_review_need` - 5 taxonomy clusters need review; historical baseline contrast is material; 70 low-confidence evidence-code rows in full area

## Fault Lines

- Process supervision and reward models versus search, verification, and extra test-time compute.
- Verifiable math/code-style tasks versus open-ended research, planning, and multimodal reasoning.
- Autoregressive reasoning versus diffusion or arbitrary-order language generation.

## Read For

- Does the paper optimize final answers, intermediate traces, rubrics, or verifier signals?
- Are gains robust outside tasks with cheap correctness checks?
- Does extra inference compute change capability, reliability, or only benchmark score?

## Shape Of The Area

- Top subareas: General LLM training, evaluation, and alignment (290); Reasoning models and chain-of-thought behavior (211); Reward modeling, preference feedback, and RL post-training (164); RL for reasoning models and verifiable rewards (161); Diffusion language models and decoding (145); LLM preference tuning and alignment training (128)
- Method-family cues: Reasoning / test-time compute (608); RL / policy optimization (468); LLM post-training (468); Agents / tool use (290); Diffusion / flow (234); Compression / efficiency (180); Transformer / attention (154); Graphs / geometry (119)
- Evaluation-setting cues: language/llm (1019); math/code/verifiable (308); theory/synthetic (226); robotics/embodied (120); security/safety (117); vision/video (66); science/domain (31)
- Contribution mix: Benchmark / evaluation (460); Method / algorithm (192); Dataset / data resource (142); Position / conceptual (112); Theory / proof (94); System / infrastructure (42); Uncoded (32); Application / domain study (25)
- Evidence confidence: medium (1029); low (70)

## Start Here

- How much can language models memorize? (Outstanding Paper Honorable Mention; oral; votes=271; github_stars=2; taxonomy-review)
- The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (Outstanding Paper Award; oral; votes=92; github_stars=212; taxonomy-review)
- Maximum Likelihood Reinforcement Learning (oral; votes=259; github_stars=194; taxonomy-review)
- Reinforcement Learning with Evolving Rubrics for Deep Research (oral; votes=201; github_stars=682; taxonomy-review)
- Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers (oral; votes=75; taxonomy-review)
- WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference (oral; votes=60; github_stars=644; taxonomy-review)

## Public Attention Not Program-Selected

- Process Reward Models That Think (votes=1815; github_stars=89)
- Reinforcement Learning via Self-Distillation (votes=718; github_stars=1008; taxonomy-review)
- Agent Learning via Early Experience (votes=532; github_stars=148; taxonomy-review)
- GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (votes=507; github_stars=489; taxonomy-review)
- On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language Models (votes=456; github_stars=160)
- Latent Collaboration in Multi-Agent Systems (votes=402; github_stars=1048; taxonomy-review)

## Artifact-Visible Papers To Inspect

- Vision-aligned Latent Reasoning for Multi-Modal Large Language Model (votes=56; github_stars=6773; taxonomy-review) manual-check
- DFlash: Block Diffusion for Flash Speculative Decoding (votes=153; github_stars=5451; taxonomy-review)
- AuTAgent: A Reinforcement Learning Framework for Tool-Augmented Audio Reasoning (votes=8; github_stars=5063; taxonomy-review) manual-check
- Autoregressive Direct Preference Optimization (votes=6; github_stars=5063; taxonomy-review) manual-check
- SpecExit: Accelerating Large Reasoning Model via Speculative Exit (votes=16; github_stars=1399; taxonomy-review)
- Latent Collaboration in Multi-Agent Systems (votes=402; github_stars=1048; taxonomy-review)

## Boundary / Taxonomy Review Candidates

- Reinforcement Learning via Self-Distillation (votes=718; github_stars=1008; taxonomy-review)
- Agent Learning via Early Experience (votes=532; github_stars=148; taxonomy-review)
- GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (votes=507; github_stars=489; taxonomy-review)
- Latent Collaboration in Multi-Agent Systems (votes=402; github_stars=1048; taxonomy-review)
- Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models (votes=351; github_stars=463; taxonomy-review)
- How much can language models memorize? (Outstanding Paper Honorable Mention; oral; votes=271; github_stars=2; taxonomy-review)

## What Could Break This Area Story

- The area taxonomy is generated from semantic clusters and curated mappings, not full manual paper reading.
- Public attention is AlphaXiv attention; it can reflect sharing dynamics rather than technical importance.
- GitHub URL share is artifact visibility, not runnable reproducibility.
- Evidence-code labels are heuristic and should be checked against the paper before making benchmark, dataset, metric, or result-character claims.