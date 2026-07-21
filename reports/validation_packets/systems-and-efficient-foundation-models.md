# Systems and Efficient Foundation Models

Manual validation packet for representative and boundary papers.

## Area Context

Headline: Efficiency papers increasingly claim capability relevance, not just lower cost.

Fault lines:
- Training/inference cost reduction versus preservation of reasoning, calibration, and safety behavior.
- Kernel or hardware-specific wins versus algorithmic improvements that transfer across deployments.
- Long-context memory, KV-cache, quantization, MoE, and serving throughput as separate bottlenecks.

What to read for:
- Are results measured at realistic batch sizes, sequence lengths, hardware, and latency budgets?
- What capability regresses under compression or cache pruning?
- Is the speedup end-to-end or only for an isolated kernel/subroutine?

## Queue Summary

- Papers: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, program_signal_low_public_attention=3, taxonomy_boundary_cluster=3
- Papers from taxonomy-review clusters: 8
- Papers with GitHub URLs: 9

## Papers

### 1. Controlled LLM Training on Spectral Sphere

Flags: fault_line_representative, oral, taxonomy-review, github

- Subarea: Large-scale training, optimizers, and model architecture
- Votes: 115
- ICML URL: https://icml.cc/virtual/2026/poster/66212
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.08393
- GitHub URL: https://github.com/Unakar/Spectral-Sphere-Optimizer
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: Compression / efficiency
- Evaluation settings: robotics/embodied; language/llm; theory/synthetic
- Result claim cues: negative / limitation; scaling / efficiency; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Scaling large models requires optimization strategies that ensure rapid convergence grounded in stability. Maximal Update Parametrization ($\boldsymbol{\mu}$P) provides a theoretical safeguard for width-invariant $\Theta(1)$ activation control, whereas emerging optimizers like Muon are only "half-aligned" with these constraints: they control updates but allow weights to drift. To address this limitation, we introduce the **Spectral Sphere Optimizer (SSO)**, which enforces strict module-wise spectral constraints on both weights and their updates. By deriving the steepest descent direction on the spectral sphere, SSO realizes a fully $\boldsymbol{\mu}$P-aligned optimization process. To enable large‑scale training, we implement SSO as an efficient parallel algorithm within Megatron. Through extensive pretraining on diverse architectures, including Dense 1.7B, MoE 8B-A1B, and 200-layer DeepNet models, SSO consistently outperforms AdamW and Muon. Furthermore, we observe significant practical stability benefits, including improved MoE router load balancing, suppressed outliers, and strictly bounded activations.

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

### 2. POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation

Flags: fault_line_representative, oral

- Subarea: Serving, GPU memory, MoE, and throughput
- Votes: 19
- ICML URL: https://icml.cc/virtual/2026/poster/62626
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.05500
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: System / infrastructure
- Contribution types: System / infrastructure; Method / algorithm
- Method families: none
- Evaluation settings: language/llm
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: throughput; memory

Abstract:

Efficient and stable training of large language models (LLMs) remains a core challenge in modern machine learning systems. We tackle this problem with Reparameterized Orthogonal Equivalence Training (POET), a spectrum-preserving framework that optimizes each weight matrix through orthogonal equivalence transformation. Although POET provides strong training stability, its original implementation incurs high memory consumption and computational overhead due to intensive matrix multiplications. To overcome these limitations, we introduce POET-X, a scalable and memory-efficient variant that performs orthogonal equivalence transformations with significantly reduced computational cost. POET-X maintains the generalization and stability benefits of POET while achieving substantial improvements in throughput and memory efficiency. In experiments, POET-X enables the pretraining of billion-parameter LLMs on a single Nvidia H100 GPU, and in contrast, standard optimizers such as AdamW run out of memory under the same settings.

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

### 3. FlashSinkhorn: IO-Aware Entropic Optimal Transport on GPU

Flags: fault_line_representative, oral, github

- Subarea: Serving, GPU memory, MoE, and throughput
- Votes: 5
- ICML URL: https://icml.cc/virtual/2026/poster/63564
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.03067
- GitHub URL: https://github.com/ot-triton-lab/ot_triton
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: System / infrastructure
- Contribution types: System / infrastructure; Method / algorithm
- Method families: Transformer / attention
- Evaluation settings: none
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: memory

Abstract:

Entropic optimal transport (EOT) via Sinkhorn iterations is widely used in modern machine learning, yet GPU solvers remain inefficient at scale. Tensorized implementations suffer quadratic HBM traffic from dense $n\times m$ interactions, while existing online backends avoid storing dense matrices but still rely on generic tiled map-reduce reduction kernels with limited fusion. We present **FlashSinkhorn**, an IO-aware EOT solver for squared Euclidean cost that rewrites stabilized log-domain Sinkhorn updates as row-wise LogSumExp reductions of biased dot-product scores, the same normalization as transformer attention. This enables FlashAttention-style fusion and tiling: fused Triton kernels stream tiles through on-chip SRAM and update dual potentials in a single pass, substantially reducing HBM IO per iteration while retaining linear-memory operations. We further provide streaming kernels for transport application, enabling scalable first- and second-order optimization. On A100 GPUs, FlashSinkhorn achieves up to $32\times$ forward-pass and $161\times$ end-to-end speedups over state-of-the-art online baselines on point-cloud OT, improves scalability on OT-based downstream tasks.

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

### 4. ECHO: Elastic Speculative Decoding with Sparse Gating for High-Concurrency Scenarios

Flags: fault_line_representative, oral, github

- Subarea: Serving, GPU memory, MoE, and throughput
- Votes: 3
- ICML URL: https://icml.cc/virtual/2026/poster/64670
- AlphaXiv URL: https://www.alphaxiv.org/abs/2604.09603
- GitHub URL: https://github.com/Sylvan820/ECHO_transformers
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; System / infrastructure; Method / algorithm
- Method families: Reasoning / test-time compute; Compression / efficiency
- Evaluation settings: language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Speculative Decodin promises to accelerate Large Language Model inference, yet its efficacy often degrades in production-grade scenarios. Existing evaluations typically overlook the compute-bound nature of high-concurrency regimes, where verification compute becomes the dominant bottleneck. Consequently, prior methods face a dilemma: static trees incur massive verification waste, while dynamic trees suffer from cumulative misjudgments and kernel incompatibility. To bridge this gap, we introduce ECHO, a high concurrency-oriented framework integrated into SGLang that reformulates speculative execution as a budgeted scheduling problem. Crucially, ECHO employs sparse confidence gating to manage the batch as a unified super-tree, elastically pivoting budget between depth and width to co-optimize the trade-off between reducing global verification steps and maximizing per-step efficiency. Extensive evaluations across diverse model scales—particularly the industrial-grade Qwen3-235B—demonstrate that ECHO consistently outperforms state-of-the-art baselines in both low-load and high-load scenarios, achieving up to 5.35$\times$ walltime speedup and delivering over 20\% relative speedup gain against the strongest baselines.

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

### 5. FlashSketch: Sketch-Kernel Co-Design for Fast Sparse Sketching on GPUs

Flags: fault_line_representative, oral

- Subarea: Serving, GPU memory, MoE, and throughput
- Votes: 1
- ICML URL: https://icml.cc/virtual/2026/poster/62887
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.06071
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Theory / proof; System / infrastructure; Method / algorithm
- Method families: Agents / tool use; Compression / efficiency; Causal / data-centric
- Evaluation settings: theory/synthetic
- Result claim cues: scaling / efficiency; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: memory

Abstract:

Sparse sketches such as the sparse Johnson–Lindenstrauss transform are a core primitive in randomized numerical linear algebra because they leverage random sparsity to reduce the arithmetic cost of sketching, while still offering strong approximation guarantees. Their random sparsity, however, is at odds with efficient implementations on modern GPUs, since it leads to irregular memory access patterns that degrade memory bandwidth utilization. Motivated by this tension, we pursue a sketch–kernel co-design approach: we design a new family of sparse sketches, BlockPerm-SJLT, whose sparsity structure is chosen to enable FlashSketch, a corresponding optimized CUDA kernel that implements these sketches efficiently. The design of BlockPerm-SJLT introduces a tunable parameter that explicitly trades off the tension between GPU-efficiency and sketching robustness. We provide theoretical guarantees for BlockPerm-SJLT under the oblivious subspace embedding (OSE) framework, and also analyze the effect of the tunable parameter on sketching quality. We empirically evaluate FlashSketch on standard RandNLA benchmarks, as well as an end-to-end ML data attribution pipeline called GraSS. FlashSketch pushes the Pareto frontier of sketching quality versus speed, across a range of regimes and tasks, and achieves a global geomean speedup of roughly $1.7 \times$ over the prior state-of-the-art GPU sketches.

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

### 6. MuonSSM: Orthogonalizing State Space Models for Sequence Modeling

Flags: fault_line_representative, oral, taxonomy-review

- Subarea: Large-scale training, optimizers, and model architecture
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/65102
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Theory / proof; System / infrastructure; Method / algorithm
- Method families: Transformer / attention; Graphs / geometry
- Evaluation settings: vision/video; language/llm; theory/synthetic
- Result claim cues: scaling / efficiency; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: accuracy; memory

Abstract:

State-space models (SSMs) have emerged as efficient linear-time alternatives to attention for long-sequence modeling. However, existing SSMs often suffer from instability and memory degradation over extended horizons due to poorly conditioned first-order updates and uncontrolled spectral geometry. We introduce MuonSSM, a general framework that stabilizes SSM training by explicitly conditioning the geometry of memory updates rather than the recurrent transition matrix. MuonSSM augments standard SSMs with a momentum-based pathway and lightweight Newton–Schulz iterations on low-rank input injections, yielding approximately norm-preserving and spectrally balanced updates while preserving parallel scan complexity. Theoretical analysis demonstrates substantial improvements in gradient propagation and mitigation of vanishing gradients over long horizons. Extensive experiments across language, vision, and time-series benchmarks show consistent gains in accuracy, robustness, and long-context performance when integrated into diverse SSM backbones. These results establish geometric conditioning of updates as a principled pathway to stable, scalable sequence modeling.

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

### 7. mHC: Manifold-Constrained Hyper-Connections

Flags: public_attention_not_program_signal, taxonomy-review, github

- Subarea: Large-scale training, optimizers, and model architecture
- Votes: 696
- ICML URL: https://icml.cc/virtual/2026/poster/61870
- AlphaXiv URL: https://www.alphaxiv.org/abs/2512.24880
- GitHub URL: https://github.com/tokenbender/mHC-manifold-constrained-hyper-connections
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: System / infrastructure
- Contribution types: System / infrastructure; Method / algorithm
- Method families: Graphs / geometry
- Evaluation settings: language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: memory

Abstract:

Recently, studies exemplified by Hyper-Connections (HC) have extended the ubiquitous residual connection paradigm established over the past decade by expanding the residual stream width and diversifying connectivity patterns. While yielding substantial performance gains, this diversification fundamentally compromises the identity mapping property intrinsic to the residual connection, which causes severe training instability and restricted scalability, and additionally incurs notable memory access overhead. To address these challenges, we propose Manifold-Constrained Hyper-Connections (mHC), a general framework that projects the residual connection space of HC onto a specific manifold to restore the identity mapping property, while incorporating rigorous infrastructure optimization to ensure efficiency. Empirical experiments demonstrate that mHC is effective for training at scale, offering tangible performance improvements and superior scalability. We anticipate that mHC, as a flexible and practical extension of HC, will contribute to a deeper understanding of topological architecture design and suggest promising directions for the evolution of foundational models.

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

### 8. xKV: Cross-Layer KV-Cache Compression via Aligned Singular Vector Extraction

Flags: public_attention_not_program_signal, github

- Subarea: Long-context attention and KV-cache compression
- Votes: 518
- ICML URL: https://icml.cc/virtual/2026/poster/63436
- AlphaXiv URL: https://www.alphaxiv.org/abs/2503.18893
- GitHub URL: https://github.com/abdelfattah-lab/xKV
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: System / infrastructure
- Contribution types: System / infrastructure; Method / algorithm
- Method families: LLM post-training; Agents / tool use; Transformer / attention; Compression / efficiency
- Evaluation settings: math/code/verifiable; language/llm
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: accuracy; latency; throughput; memory

Abstract:

Long-context Large Language Models (LLMs) enable powerful applications but incur high memory costs due to the key–value states (KV-Cache). Recent studies attempt to share KV-Cache across layers, but these approaches either require expensive pretraining or rely on per-token cross-layer cosine similarity that is often limited in practice. We show, via Centered Kernel Alignment (CKA), that the dominant singular vectors of KV-Cache are well aligned across layers. Motivated by this observation, we propose xKV, a post-training compression method that jointly factorizes grouped-layer KV-Cache into a shared low-rank subspace, substantially reducing KV-Cache memory. Across widely used LLMs, xKV achieves up to 8× KV-Cache compression while preserving accuracy on long-context tasks and in multi-turn settings. To further improve efficiency, we introduce Selective Reconstruction (SR) at decode time. Combined with SR, xKV achieves up to 4.23× end-to-end speedup, surpassing notable baselines with 30% higher throughput under a similar accuracy level. Overall, xKV provides a plug-and-play approach to reduce both memory and latency for long-context LLM inference. Our code will be open-sourced.

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

### 9. Evolution Strategies at the Hyperscale

Flags: public_attention_not_program_signal, taxonomy-review, github

- Subarea: Large-scale training, optimizers, and model architecture
- Votes: 405
- ICML URL: https://icml.cc/virtual/2026/poster/62943
- AlphaXiv URL: https://www.alphaxiv.org/abs/2511.16652
- GitHub URL: https://github.com/ESHyperscale/HyperscaleES
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: System / infrastructure
- Contribution types: System / infrastructure; Method / algorithm
- Method families: RL / policy optimization; LLM post-training; Reasoning / test-time compute
- Evaluation settings: language/llm; theory/synthetic
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: throughput

Abstract:

Evolution Strategies (ES) is a class of powerful black-box optimisation methods that are highly parallelisable and can handle non-differentiable and noisy objectives. However, naïve ES becomes prohibitively expensive at scale on GPUs due to the low arithmetic intensity of batched matrix multiplications with unstructured random perturbations. We introduce Evolution Guided GeneRal Optimisation via Low-rank Learning (EGGROLL), which improves arithmetic intensity by structuring individual perturbations as rank-$r$ matrices, resulting in a hundredfold increase in training speed for billion-parameter models at large population sizes, achieving up to 91\% of the throughput of pure batch inference. We provide a rigorous theoretical analysis of ES for high-dimensional parameter objectives, investigating conditions needed for ES updates to converge in high dimensions, revealing a linearising effect, and proving consistency between EGGROLL and ES as parameter dimension increases. Our experiments show that EGGROLL: (1) enables the stable pretraining of nonlinear recurrent language models that operate purely in integer datatypes, (2) is competitive with GRPO for post-training LLMs on reasoning tasks, and (3) does not compromise performance compared to ES in tabula rasa RL settings, despite being faster.

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

### 10. Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights

Flags: public_attention_not_program_signal, taxonomy-review, evidence-low, github

- Subarea: Large-scale training, optimizers, and model architecture
- Votes: 365
- ICML URL: https://icml.cc/virtual/2026/poster/65901
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.12228
- GitHub URL: https://github.com/sunrainyg/RandOpt
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Method / algorithm
- Method families: RL / policy optimization; LLM post-training
- Evaluation settings: none
- Result claim cues: scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Pretraining produces a learned parameter vector that is typically treated as a starting point for further iterative adaptation. In this work, we instead view the outcome of pretraining as a distribution over parameter vectors, whose support already contains task-specific experts. We show that in smaller or insufficiently trained models such expert solutions occupy a negligible fraction of the volume of this distribution, making their discovery reliant on structured optimization methods such as gradient descent. In contrast, in large, well-pretrained models the density of task-experts increases dramatically, so that diverse specialists populate a substantial fraction of the neighborhood around the pretrained weights. Motivated by this perspective, we explore a simple, fully parallel post-training method that samples $N$ parameter vectors at random, selects the top $K$, and ensembles them via majority vote to combine complementary expertise. Despite its simplicity, this approach is competitive with standard post-training methods such as PPO, GRPO, and ES for contemporary large-scale models.

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

### 11. CAT-Q: Cost-efficient and Accurate Ternary Quantization for LLMs

Flags: program_signal_low_public_attention, oral

- Subarea: Quantization and low-precision training/inference
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/65816
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Theory / proof; Method / algorithm
- Method families: LLM post-training; Agents / tool use; Compression / efficiency
- Evaluation settings: math/code/verifiable; language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

In this paper, we present CAT-Q, **C**ost-efficient and **A**ccurate **T**ernary **Q**uantization, to compress LLMs. Unlike current state-of-the-art ternary quantization methods that rely on data-intensive and costly quantization-aware training to mitigate severe performance degradation, CAT-Q employs a simple yet effective post-training quantization scheme, thereby is easily applicable to LLMs with diverse architectures and model sizes. It has two key components, learnable modulation (LM) and softened ternarization (ST), which are coupled from an optimization perspective. LM leverages a composition of learnable factors to modulate the distribution of high-precision weights and the ternary threshold, making them less sensitive to ternarization. ST further introduces a novel transition function to guide the ternarization process toward stable convergence. We show that, for pre-trained LLMs with 1.7B to 8B parameters, CAT-Q can quantize them into ternary models using merely 512 calibration samples, while achieving competitive performance to the seminal BitNet 1.58-bit v1 and v2 families (with 1.3B to 7B parameters) trained with 100B tokens, yielding about a 100,000x reduction in training tokens. Moreover, we show for the first time that CAT-Q can quantize even larger pre-trained LLMs having 14B to 235B parameters into leading ternary models within 8 to 60 hours on 8 A100-80GB GPUs. Code will be made publicly available.

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

### 12. ReQAT: Achieving Full-Precision Reasoning Accuracy with 4-bit Floating-Point Quantization-Aware Training

Flags: program_signal_low_public_attention, oral

- Subarea: Quantization and low-precision training/inference
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/63073
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; System / infrastructure; Method / algorithm
- Method families: LLM post-training; Reasoning / test-time compute; Diffusion / flow; Transformer / attention; Compression / efficiency
- Evaluation settings: language/llm
- Result claim cues: negative / limitation; scaling / efficiency
- Benchmarks: ReQAT
- Datasets: none
- Metrics: accuracy; throughput

Abstract:

Large Reasoning Models (LRMs) achieve strong problem-solving through long chain-of-thought, but their deployment is constrained by the high cost of full-precision inference and growing KV cache footprints. Microscaled FP4 formats enable efficient FP4 deployment; however, fully quantizing weights, activations, and KV caches (W4A4KV4) causes severe reasoning degradation that existing PTQ and QAT fail to recover. We identify that FP4 failures concentrate on low-entropy tokens—precise symbolic commitments such as digits and operators—where quantization noise inflates sampling errors that cascade through reasoning traces. Based on this insight, we propose ReQAT, a reasoning-centric FP4 training framework with three components: (i) Trace-Aligned QAT (TAQ), which revisits identical reasoning traces to focus updates on critical low-entropy decisions; (ii) Selective Entropy Minimization (SEM), which reinforces confidence at low-entropy positions; and (iii) Q-FIT, a quantization-friendly initialization that jointly calibrates RoPE-consistent KV cache transformations to stabilize QAT. Under the same training budget, ReQAT not only recovers but surpasses BF16 fine-tuning accuracy—achieving while delivering up to $3.9\times$ throughput speedup on NVIDIA DGX Spark and $3.1\times$ on B200. This is the first demonstration that FP4 QAT can exceed full-precision accuracy for LRMs with over 3× speedup on production hardware.

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

### 13. Faster Activation Functions at the Edge for Post-Training Speedups

Flags: program_signal_low_public_attention, oral

- Subarea: Serving, GPU memory, MoE, and throughput
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/61061
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: System / infrastructure
- Contribution types: System / infrastructure; Method / algorithm
- Method families: LLM post-training; Transformer / attention
- Evaluation settings: none
- Result claim cues: negative / limitation; scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: accuracy; latency

Abstract:

On-device AI has gained significant attention for enabling efficient, low-latency inference on edge devices. However, tight resource constraints on these platforms make the deployment of accurate and lightweight deep learning models challenging. In particular, advanced activation functions (AFs) like Swish and GELU often incur high inference overhead due to the lack of hardware fast-paths for exponentiation and division, restricting edge-ML applications to simple AFs like ReLU, limiting model accuracy. To address this, we propose FFCC, a compiler that automatically generates efficient approximations of AFs through floating-point reinterpretation. These functions don’t require hardware fast-paths meaning they remain fast on edge devices. They do not incur great accurate losses, and allowing use as post-training replacements without negatively impacting model final accuracy. FFCC takes a specification of AFs using basic floating-point operators and applies derivation rules to lower these expressions into efficient instruction sequences. Our experiments show that we can provide fast approximations of AFs, achieving order-of-magnitude speed ups over accurate baselines on Arm M7, delivering performance on-par with Hardswish, while beating it on accuracy. Additionally, we show that our approximations – unlike Hardswish – can be used as drop-in replacements of exact version post-training without loss of model accuracy.

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

### 14. NorMuon: Making Muon more efficient and scalable

Flags: taxonomy_boundary_cluster, taxonomy-review, github

- Subarea: Large-scale training, optimizers, and model architecture
- Votes: 61
- ICML URL: https://icml.cc/virtual/2026/poster/61880
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.05491
- GitHub URL: https://github.com/zichongli5/NorMuon.git
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: System / infrastructure
- Contribution types: System / infrastructure; Method / algorithm
- Method families: Graphs / geometry
- Evaluation settings: language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: memory

Abstract:

The choice of optimizer significantly impacts the training efficiency and computational costs of large language models (LLMs). Recently, the Muon optimizer has demonstrated promising results by orthogonalizing parameter updates, improving optimization geometry through better conditioning. Despite Muon’s emergence as a candidate successor to Adam, the potential for jointly leveraging their strengths—has not been systematically explored. In this work, we bridge this gap by proposing NorMuon (Neuron-wise Normalized Muon), an optimizer that synergistically combines orthogonalization with neuron-level adaptive learning rates. Our analysis reveals that while Muon effectively reduces condition numbers, the resulting updates exhibit highly non-uniform neuron norms, causing certain neurons to dominate the optimization process. NorMuon addresses this imbalance by maintaining second-order momentum statistics for each neuron and applying row-wise normalization after orthogonalization, ensuring balanced parameter utilization while preserving Muon's conditioning benefits. To enable practical deployment at scale, we develop an efficient distributed implementation under the FSDP2 framework that strategically distributes orthogonalization computations across devices. Experiments across multiple model scales demonstrate that NorMuon consistently outperforms both Adam and Muon, achieving 21.74\% better training efficiency than Adam and 11.31\% improvement over Muon on 1.1B pretraining setting, while maintaining a comparable memory footprint to Muon. Our findings suggest that orthogonalization and adaptive learning rates are complementary rather than competing approaches, opening new avenues for optimizer design in large-scale deep learning.

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

### 15. GradientStabilizer: Fix the Norm, Not the Gradient

Flags: taxonomy_boundary_cluster, taxonomy-review, github

- Subarea: Large-scale training, optimizers, and model architecture
- Votes: 43
- ICML URL: https://icml.cc/virtual/2026/poster/63695
- AlphaXiv URL: https://www.alphaxiv.org/abs/2502.17055
- GitHub URL: https://github.com/TianjinYellow/StableSPAM.git
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: RL / policy optimization; Compression / efficiency
- Evaluation settings: language/llm
- Result claim cues: negative / limitation; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Training instability in modern deep learning systems is frequently triggered by rare but extreme gradient-norm spikes, which can induce oversized parameter updates, corrupt optimizer state, and lead to slow recovery or divergence. Widely used safeguards such as gradient clipping mitigate these failures but require threshold tuning and indiscriminately truncate large updates. We propose **GradientStabilizer**, a lightweight, drop-in gradient transform that *preserves the instantaneous gradient direction* while replacing the update magnitude with a statistically stabilized estimate derived from running gradient-norm statistics. We prove that the resulting stabilized magnitude is uniformly bounded on spike steps, independent of the spike size, and show how this boundedness controls optimizer state evolution in adaptive methods. Across LLM pre-training (FP16), quantization-aware pre-training (FP4), ImageNet classification, reinforcement learning, and time-series forecasting, **GradientStabilizer** consistently improves training stability, widens stable learning-rate regions, and reduces divergence relative to clipping-based baselines, even substantially reducing Adam’s sensitivity to weight-decay strength.

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

### 16. Why Do We Need Warm-up? A Theoretical Perspective

Flags: taxonomy_boundary_cluster, taxonomy-review, evidence-low

- Subarea: Large-scale training, optimizers, and model architecture
- Votes: 35
- ICML URL: https://icml.cc/virtual/2026/poster/63104
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.03164
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Theory / proof; Method / algorithm
- Method families: none
- Evaluation settings: vision/video; language/llm; theory/synthetic
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Learning rate warm-up -- increasing the learning rate at the beginning of training -- has become a ubiquitous heuristic in modern deep learning, yet its theoretical foundations remain poorly understood. In this work, we provide a principled explanation for why warm-up improves training. We rely on a generalization of the $(L_0, L_1)$-smoothness condition, which bounds local curvature as a linear function of the loss sub-optimality and exhibits desirable closure properties. We show -- both theoretically and empirically -- that this condition is satisfied by common neural architectures and accurately captures the curvature of the optimization landscape early in training. Adapting the learning rate in response to this curvature condition naturally induces a warm-up–like schedule, and we show that this choice yields provably faster convergence guarantees than using a fixed learning rate. Finally, we validate our theoretical insights through experiments on language and vision models, confirming the agreement between our theoretically derived schedule and standard warm-up.

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
