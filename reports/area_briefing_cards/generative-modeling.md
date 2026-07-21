# Generative Modeling

Diffusion and flow models are splitting into practical media generation, language alternatives, and sampling theory.

## Signal Snapshot

- Papers: 379 (5.7% of corpus)
- Oral enrichment: 0.83x
- Public-attention enrichment: 0.96x
- Historical accepted-paper delta: +0.5 pp
- GitHub URL share: 31.1%
- Manual area-review progress: 0/16 rows reviewed; 16 remaining
- Trust tier: `moderate_review_need` - 50 low-confidence evidence-code rows in full area

## Fault Lines

- Sampling-theory guarantees versus image/video generation quality and latency.
- Autoregressive generation versus diffusion or flow-based sequence generation.
- Better visual fidelity versus controllability, consistency, and editing reliability.

## Read For

- Do speedups preserve quality under realistic inference budgets?
- Are theoretical sampling improvements visible in practical model behavior?
- Does generation remain consistent over long videos, edits, or conditional controls?

## Shape Of The Area

- Top subareas: Image/video diffusion and flow generation (243); Diffusion sampling, transport, and inverse problems (136)
- Method-family cues: Diffusion / flow (333); Graphs / geometry (91); Bayesian / probabilistic (89); LLM post-training (82); Transformer / attention (72); Compression / efficiency (60); Agents / tool use (46); RL / policy optimization (39)
- Evaluation-setting cues: vision/video (220); theory/synthetic (120); language/llm (83); robotics/embodied (49); security/safety (39); science/domain (36); math/code/verifiable (33)
- Contribution mix: Method / algorithm (101); Benchmark / evaluation (80); Dataset / data resource (65); Theory / proof (59); Position / conceptual (31); System / infrastructure (19); Application / domain study (14); Uncoded (10)
- Evidence confidence: medium (329); low (50)

## Start Here

- A Random Matrix Perspective on the Consistency of Diffusion Models (Outstanding Paper Honorable Mention; oral; votes=14)
- High-accuracy sampling for diffusion models and log-concave distributions (Outstanding Paper Award; oral; votes=9)
- High-accuracy and dimension-free sampling with diffusions (oral; votes=21)
- Transforming Weather Data from Pixel to Latent Space (oral; votes=11)
- Rex: A Family of Reversible Exponential (Stochastic) Runge-Kutta Solvers (oral; votes=6)
- Error Propagation Mechanisms and Compensation Strategies for Quantized Diffusion Models (oral; votes=3)

## Public Attention Not Program-Selected

- One-step Latent-free Image Generation with Pixel Mean Flows (votes=214; github_stars=267)
- Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Video Generation (votes=152; github_stars=850)
- Dimension-free convergence of diffusion models for approximate Gaussian mixtures (votes=124)
- Latent Forcing: Reordering the Diffusion Trajectory for Pixel-Space Image Generation (votes=104; github_stars=133)
- Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression (votes=104; github_stars=133)
- Categorical Flow Maps (votes=87; github_stars=67)

## Artifact-Visible Papers To Inspect

- Self-Prompting Diffusion Transformer for Open-Vocabulary Scene Text Edit via In-Context Learning (votes=6; github_stars=5069) manual-check
- Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Video Generation (votes=152; github_stars=850)
- Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis (votes=64; github_stars=531)
- DyPE: Dynamic Position Extrapolation for Ultra High Resolution Diffusion (votes=21; github_stars=356)
- Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution (votes=6; github_stars=282)
- DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation (votes=13; github_stars=271)

## Boundary / Taxonomy Review Candidates

- No high-signal `needs_review` papers in this area briefing sample.

## What Could Break This Area Story

- The area taxonomy is generated from semantic clusters and curated mappings, not full manual paper reading.
- Public attention is AlphaXiv attention; it can reflect sharing dynamics rather than technical importance.
- GitHub URL share is artifact visibility, not runnable reproducibility.
- Evidence-code labels are heuristic and should be checked against the paper before making benchmark, dataset, metric, or result-character claims.