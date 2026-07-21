# Systems and Efficient Foundation Models

Efficiency papers increasingly claim capability relevance, not just lower cost.

## Signal Snapshot

- Papers: 515 (7.8% of corpus)
- Oral enrichment: 0.69x
- Public-attention enrichment: 1.31x
- Historical accepted-paper delta: +2.1 pp
- GitHub URL share: 24.7%
- Manual area-review progress: 0/16 rows reviewed; 16 remaining
- Trust tier: `high_review_need` - 1 taxonomy clusters need review; public attention exceeds program signal; historical baseline contrast is material; 77 low-confidence evidence-code rows in full area

## Fault Lines

- Training/inference cost reduction versus preservation of reasoning, calibration, and safety behavior.
- Kernel or hardware-specific wins versus algorithmic improvements that transfer across deployments.
- Long-context memory, KV-cache, quantization, MoE, and serving throughput as separate bottlenecks.

## Read For

- Are results measured at realistic batch sizes, sequence lengths, hardware, and latency budgets?
- What capability regresses under compression or cache pruning?
- Is the speedup end-to-end or only for an isolated kernel/subroutine?

## Shape Of The Area

- Top subareas: Large-scale training, optimizers, and model architecture (198); Serving, GPU memory, MoE, and throughput (116); Long-context attention and KV-cache compression (113); Quantization and low-precision training/inference (88)
- Method-family cues: Compression / efficiency (266); Transformer / attention (164); Agents / tool use (138); LLM post-training (130); Reasoning / test-time compute (68); Graphs / geometry (57); Diffusion / flow (52); RL / policy optimization (31)
- Evaluation-setting cues: language/llm (324); theory/synthetic (129); math/code/verifiable (105); vision/video (69); security/safety (33); robotics/embodied (24); science/domain (8)
- Contribution mix: Benchmark / evaluation (135); Theory / proof (103); System / infrastructure (98); Method / algorithm (72); Dataset / data resource (45); Position / conceptual (37); Application / domain study (19); Uncoded (6)
- Evidence confidence: medium (438); low (77)

## Start Here

- Controlled LLM Training on Spectral Sphere (oral; votes=115; github_stars=130; taxonomy-review)
- POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation (oral; votes=19)
- FlashSinkhorn: IO-Aware Entropic Optimal Transport on GPU (oral; votes=5; github_stars=207)
- ECHO: Elastic Speculative Decoding with Sparse Gating for High-Concurrency Scenarios (oral; votes=3; github_stars=2)
- FlashSketch: Sketch-Kernel Co-Design for Fast Sparse Sketching on GPUs (oral; votes=1)
- ReQAT: Achieving Full-Precision Reasoning Accuracy with 4-bit Floating-Point Quantization-Aware Training (oral; votes=0)

## Public Attention Not Program-Selected

- mHC: Manifold-Constrained Hyper-Connections (votes=696; github_stars=367; taxonomy-review)
- xKV: Cross-Layer KV-Cache Compression via Aligned Singular Vector Extraction (votes=518; github_stars=52)
- Evolution Strategies at the Hyperscale (votes=405; github_stars=346; taxonomy-review)
- Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights (votes=365; github_stars=627; taxonomy-review)
- SimpleMem: Efficient Lifelong Memory for LLM Agents (votes=214; github_stars=3641)
- Fast KV Compaction via Attention Matching (votes=176; github_stars=253)

## Artifact-Visible Papers To Inspect

- When RL Meets Adaptive Speculative Training: A Unified Training-Serving System (votes=17; github_stars=30219)
- SimpleMem: Efficient Lifelong Memory for LLM Agents (votes=214; github_stars=3641)
- DITRON: Distributed Multi-level Tiling Compiler for Parallel Tensor Programs (votes=8; github_stars=1486)
- SpecForge: A Flexible and Efficient Open-Source Training Framework for Speculative Decoding (votes=11; github_stars=985)
- TriAttention: Efficient Long Reasoning with Trigonometric KV Compression (votes=139; github_stars=815)
- Doc-to-LoRA: Learning to Instantly Internalize Contexts (votes=87; github_stars=779)

## Boundary / Taxonomy Review Candidates

- mHC: Manifold-Constrained Hyper-Connections (votes=696; github_stars=367; taxonomy-review)
- Evolution Strategies at the Hyperscale (votes=405; github_stars=346; taxonomy-review)
- Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights (votes=365; github_stars=627; taxonomy-review)
- Controlled LLM Training on Spectral Sphere (oral; votes=115; github_stars=130; taxonomy-review)
- NorMuon: Making Muon more efficient and scalable (votes=61; github_stars=82; taxonomy-review)
- GradientStabilizer: Fix the Norm, Not the Gradient (votes=43; github_stars=28; taxonomy-review)

## What Could Break This Area Story

- The area taxonomy is generated from semantic clusters and curated mappings, not full manual paper reading.
- Public attention is AlphaXiv attention; it can reflect sharing dynamics rather than technical importance.
- GitHub URL share is artifact visibility, not runnable reproducibility.
- Evidence-code labels are heuristic and should be checked against the paper before making benchmark, dataset, metric, or result-character claims.