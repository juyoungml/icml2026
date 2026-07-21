# Generative Modeling

Manual validation packet for representative and boundary papers.

## Area Context

Headline: Diffusion and flow models are splitting into practical media generation, language alternatives, and sampling theory.

Fault lines:
- Sampling-theory guarantees versus image/video generation quality and latency.
- Autoregressive generation versus diffusion or flow-based sequence generation.
- Better visual fidelity versus controllability, consistency, and editing reliability.

What to read for:
- Do speedups preserve quality under realistic inference budgets?
- Are theoretical sampling improvements visible in practical model behavior?
- Does generation remain consistent over long videos, edits, or conditional controls?

## Queue Summary

- Papers: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, low_evidence_code_confidence=4, program_signal_low_public_attention=2
- Papers from taxonomy-review clusters: 0
- Papers with GitHub URLs: 6

## Papers

### 1. A Random Matrix Perspective on the Consistency of Diffusion Models

Flags: fault_line_representative, oral, Outstanding Paper Honorable Mention

- Subarea: Diffusion sampling, transport, and inverse problems
- Votes: 14
- ICML URL: https://icml.cc/virtual/2026/poster/62241
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.02908
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Dataset / data resource; Method / algorithm
- Method families: Agents / tool use; Diffusion / flow
- Evaluation settings: theory/synthetic
- Result claim cues: negative / limitation; scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Diffusion models trained on different, non-overlapping subsets of a dataset often produce strikingly similar outputs when given the same noise seed. We trace this consistency to a simple linear effect: the shared Gaussian statistics across splits already predict much of the generated images. To formalize this, we develop a random matrix theory (RMT) framework that quantifies how finite datasets shape the expectation and variance of the learned denoiser and sampling map in the linear setting. For expectations, sampling variability acts as a renormalization of the noise level through a self-consistent relation $\sigma^2\to\kappa(\sigma^2)$, explaining why limited data overshrink low-variance directions and pull samples toward the dataset mean. For fluctuations, our variance formulas reveal three key factors behind cross-split disagreement: \textit{anisotropy} across eigenmodes, \textit{inhomogeneity} across inputs, and overall scaling with dataset size. Extending deterministic-equivalence tools to fractional matrix powers further allows us to analyze entire sampling trajectories. The theory sharply predicts the behavior of linear diffusion models, and we validate its predictions on UNet and DiT architectures in their non-memorization regime, identifying where and how samples deviates across training data split. This provides a principled baseline for reproducibility in diffusion training, linking spectral properties of data to the stability of generative outputs.

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

### 2. High-accuracy sampling for diffusion models and log-concave distributions

Flags: fault_line_representative, oral, Outstanding Paper Award

- Subarea: Diffusion sampling, transport, and inverse problems
- Votes: 9
- ICML URL: https://icml.cc/virtual/2026/poster/65132
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.01338
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: Diffusion / flow; Bayesian / probabilistic
- Evaluation settings: none
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: accuracy

Abstract:

We present algorithms for diffusion model sampling which obtain $\delta$-error in $\mathrm{polylog}(1/\delta)$ steps, given access to $\widetilde O(\delta)$-accurate score estimates in $L^2$. This is an exponential improvement over all previous results. Specifically, under minimal data assumptions, the complexity is $\widetilde O(d\mathrm{polylog}(1/\delta))$ where $d$ is the dimension of the data; under a non-uniform $L$-Lipschitz condition, the complexity is $\widetilde O(\sqrt{dL}\mathrm{polylog}(1/\delta))$; and if the data distribution has intrinsic dimension $d_\star$, then the complexity reduces to $\widetilde O(d_\star\mathrm{polylog}(1/\delta))$. Our approach also yields the first $\mathrm{polylog}(1/\delta)$ complexity sampler for general log-concave distributions using only gradient evaluations.

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

### 3. High-accuracy and dimension-free sampling with diffusions

Flags: fault_line_representative, oral

- Subarea: Diffusion sampling, transport, and inverse problems
- Votes: 21
- ICML URL: https://icml.cc/virtual/2026/poster/63314
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.10708
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: Diffusion / flow
- Evaluation settings: none
- Result claim cues: scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: accuracy

Abstract:

Diffusion models have shown remarkable empirical success in sampling from rich multi-modal distributions. Their inference relies on numerically solving a certain differential equation. This differential equation cannot be solved in closed form, and its resolution via discretization typically requires many small iterations to produce \emph{high-quality} samples. More precisely, prior works have shown that the iteration complexity of discretization methods for diffusion models scales polynomially in the ambient dimension and the inverse accuracy $1/\varepsilon$. In this work, we propose a new solver for diffusion models relying on a subtle interplay between low-degree approximation and the collocation method, and we prove that its iteration complexity scales *polylogarithmically* in $1/\varepsilon$, yielding the first "high-accuracy" guarantee for a diffusion-based sampler that only uses (approximate) access to the scores of the data distribution. In addition, our bound does not depend explicitly on the ambient dimension; more precisely, the dimension affects the complexity of our solver only through the *effective radius* of the support of the target distribution.

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

### 4. Transforming Weather Data from Pixel to Latent Space

Flags: fault_line_representative, oral

- Subarea: Image/video diffusion and flow generation
- Votes: 11
- ICML URL: https://icml.cc/virtual/2026/poster/64426
- AlphaXiv URL: https://www.alphaxiv.org/abs/2503.06623
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Application / domain study
- Method families: Compression / efficiency
- Evaluation settings: science/domain
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: accuracy

Abstract:

The increasing impact of climate change and extreme weather events has spurred growing interest in deep learning for weather research. However, existing studies often rely on weather data in pixel space, which presents several challenges such as smooth outputs in model outputs, limited applicability to a single pressure-variable subset (PVS), and high data storage and computational costs. To address these challenges, we propose a novel Weather Latent Autoencoder (WLA) that transforms weather data from pixel space to latent space, enabling efficient data representation. By decoupling weather reconstruction from downstream tasks, WLA improves the accuracy and sharpness of weather task model results. The incorporated Pressure-Variable Unified Module transforms multiple PVS into a unified representation, enhancing the adaptability of the model in multiple weather scenarios. Furthermore, weather tasks can be performed in a low-storage latent space of WLA rather than a high-storage pixel space, thus significantly reducing data storage and computational costs. Through extensive experimentation, we demonstrate its superior compression and reconstruction performance, enabling the creation of the ERA5-Latent dataset with unified representations of multiple PVS from ERA5 data. The compressed full PVS in the ERA5-Latent dataset reduces the original 244.34 TB of data to 0.43 TB. The downstream task further demonstrates that task models can apply to multiple PVS with low data costs in latent space and achieve superior performance compared to models in pixel space.

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

### 5. Rex: A Family of Reversible Exponential (Stochastic) Runge-Kutta Solvers

Flags: fault_line_representative, oral

- Subarea: Diffusion sampling, transport, and inverse problems
- Votes: 6
- ICML URL: https://icml.cc/virtual/2026/poster/66025
- AlphaXiv URL: https://www.alphaxiv.org/abs/2502.08834
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof
- Method families: Diffusion / flow
- Evaluation settings: vision/video; theory/synthetic
- Result claim cues: negative / limitation; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Deep generative models based on neural differential equations have quickly become the state-of-the-art for numerous generation tasks across many different applications. These models rely on ODE/SDE solvers which integrate from a prior distribution to the data distribution. In many applications it is highly desirable to then integrate in the other direction. The standard solvers, however, accumulate discretization errors which don’t align with the forward trajectory, thereby prohibiting an exact inversion. In applications where the precision of the generative model is paramount this inaccuracy in inversion is often unacceptable. Current approaches to solving the inversion of these models results in significant downstream issues with poor stability and low-order of convergence; moreover, they are strictly limited to the ODE domain. In this work, we propose a new family of reversible exponential (stochastic) Runge-Kutta solvers which we refer to as Rex developed by an application of Lawson methods to convert any explicit (stochastic) Runge-Kutta scheme into a reversible one. In addition to a rigorous theoretical analysis of the proposed solvers, we also empirically demonstrate the utility of Rex on improving the sample of Boltzmann distributions with flow models, and improving image generation and editing capabilities with diffusion models.

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

### 6. Error Propagation Mechanisms and Compensation Strategies for Quantized Diffusion Models

Flags: fault_line_representative, oral

- Subarea: Image/video diffusion and flow generation
- Votes: 3
- ICML URL: https://icml.cc/virtual/2026/poster/66340
- AlphaXiv URL: https://www.alphaxiv.org/abs/2508.12094
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; Method / algorithm
- Method families: LLM post-training; Agents / tool use; Diffusion / flow; Compression / efficiency
- Evaluation settings: vision/video; theory/synthetic
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Diffusion models have transformed image synthesis by establishing unprecedented quality and creativity benchmarks. Nevertheless, their large-scale deployment faces challenges due to computationally intensive iterative denoising processes. Although post-training quantization (PTQ) provides an effective pathway for accelerating sampling, the iterative nature of diffusion models causes stepwise quantization errors to accumulate progressively during generation, inevitably compromising output fidelity. To address this challenge, we develop a theoretical framework that mathematically formulates error propagation in Diffusion Models (DMs), deriving per-step quantization error propagation equations and establishing the first closed-form solution for cumulative error. Building on this theoretical foundation, we propose a timestep-aware cumulative error compensation scheme. Extensive experiments on multiple image datasets demonstrate that our compensation strategy effectively mitigates error propagation, significantly enhancing existing PTQ methods. Specifically, it achieves a 1.2 PSNR improvement over SVDQuant on SDXL W4A4, while incurring only an additional $<$ 0.5\% time overhead.

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

### 7. One-step Latent-free Image Generation with Pixel Mean Flows

Flags: public_attention_not_program_signal, github

- Subarea: Image/video diffusion and flow generation
- Votes: 214
- ICML URL: https://icml.cc/virtual/2026/poster/63515
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.22158
- GitHub URL: https://github.com/Lyy-iiis/pMF
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof
- Method families: Diffusion / flow; Graphs / geometry
- Evaluation settings: vision/video
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: fid

Abstract:

Modern diffusion/flow-based models for image generation typically exhibit two core characteristics: (i) using multi-step sampling, and (ii) operating in a latent space. Recent advances have made encouraging progress on each aspect individually, paving the way toward one-step diffusion/flow without latents. In this work, we take a further step towards this goal and propose "pixel MeanFlow" (pMF). Our core guideline is to formulate the network output space and the loss space separately. The network target is designed to be on a presumed low-dimensional image manifold (i.e., x-prediction), while the loss is defined via MeanFlow in the velocity space. We introduce a simple transformation between the image manifold and the average velocity field. In experiments, pMF achieves strong results for one-step latent-free generation on ImageNet at 256$\times$256 resolution (2.22 FID) and 512$\times$512 resolution (2.48 FID), filling a key missing piece in this regime. We hope that our study will further advance the boundaries of diffusion/flow-based generative models.

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

### 8. Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Video Generation

Flags: public_attention_not_program_signal, github

- Subarea: Image/video diffusion and flow generation
- Votes: 152
- ICML URL: https://icml.cc/virtual/2026/poster/65646
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.02214
- GitHub URL: https://github.com/thu-ml/Causal-Forcing
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: Diffusion / flow; Transformer / attention; Causal / data-centric
- Evaluation settings: vision/video
- Result claim cues: negative / limitation; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

To achieve real-time video generation, current approaches distill pretrained bidirectional video diffusion models into few-step autoregressive (AR) models. This process involves an *architectural gap*, as it converts full attention into causal attention. In this paper, we demonstrate that existing methods fail to bridge this gap theoretically, leading to suboptimal performance. Specifically, these methods employ ODE distillation to initialize the AR student, where a key requirement is *injectivity*. We figure out that for an AR student, *frame-level injectivity* must hold: each noisy frame must map to a unique clean frame under the PF-ODE of the *AR teacher*. We theoretically prove that existing methods, which distill an AR student from a bidirectional teacher, violate this frame-level injectivity. Consequently, the student fails to recover the teacher's flow map and instead learns a conditional expectation, resulting in subpar performance. To address this issue, we propose *Causal Forcing*, which employs an AR teacher for ODE initialization, thereby effectively bridging the architectural gap. Empirical results show that our method outperforms all baselines across all metrics, surpassing the SOTA Self-Forcing by 19.3\% in Dynamic Degree, 8.7\% in VisionReward, and 16.7\% in Instruction Following.

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

### 9. Dimension-free convergence of diffusion models for approximate Gaussian mixtures

Flags: public_attention_not_program_signal

- Subarea: Diffusion sampling, transport, and inverse problems
- Votes: 124
- ICML URL: https://icml.cc/virtual/2026/poster/65046
- AlphaXiv URL: https://www.alphaxiv.org/abs/2504.05300
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: Diffusion / flow; Bayesian / probabilistic
- Evaluation settings: theory/synthetic
- Result claim cues: scaling / efficiency; robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Diffusion models are distinguished by their exceptional generative performance, particularly in producing high-quality samples through iterative denoising. While current theory suggests that the number of denoising steps required for accurate sample generation should scale linearly with data dimension, this does not reflect the practical efficiency of widely used algorithms like Denoising Diffusion Probabilistic Models (DDPMs). This paper investigates the effectiveness of diffusion models in sampling complex high-dimensional distributions that can be well-approximated by Gaussian Mixture Models (GMMs). For these distributions, our main result shows that DDPM takes at most $\widetilde{O}(1/\varepsilon)$ iterations to attain an $\varepsilon$-accurate distribution in total variation (TV) distance, independent of both the ambient dimension $d$ and the number of components $K$, up to logarithmic factors. Furthermore, this result remains robust to score estimation errors. These findings highlight the remarkable effectiveness of diffusion models in high-dimensional settings given the universal approximation capability of GMMs, and provide theoretical insights into their practical success.

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

### 10. Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression

Flags: public_attention_not_program_signal, github

- Subarea: Image/video diffusion and flow generation
- Votes: 104
- ICML URL: https://icml.cc/virtual/2026/poster/62407
- AlphaXiv URL: https://www.alphaxiv.org/abs/2512.05081
- GitHub URL: https://github.com/cvlab-kaist/DeepForcing.git
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: System / infrastructure
- Contribution types: System / infrastructure; Method / algorithm
- Method families: LLM post-training; Diffusion / flow; Transformer / attention; Compression / efficiency
- Evaluation settings: vision/video
- Result claim cues: robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Recent advances in autoregressive video diffusion have enabled real-time frame streaming, yet existing solutions still suffer from temporal repetition, drift, and motion deceleration. We find that naïvely applying StreamingLLM-style attention sinks to video diffusion leads to fidelity degradation and motion stagnation. To overcome this, we introduce Deep Forcing, which consists of two training-free mechanisms that address this without any fine-tuning. Specifically, 1) Deep Sink dedicates half of the sliding window to persistent sink tokens and re-aligns their temporal RoPE phase to the current timeline, stabilizing global context during long rollouts. 2) Participative Compression performs importance-aware KV cache pruning that preserves only tokens actively participating in recent attention while safely discarding redundant and degraded history, minimizing error accumulation under out-of-distribution length generation. Together, these components enable over 12 times extrapolation (e.g. 5s-trained -> 60s+ generation) with better imaging quality and aesthetic quality, almost maintaining overall consistency, and substantial gains in dynamic degree, all while maintaining real-time generation. Our results demonstrate that training-free KV-cache management can match or exceed training-based approaches for autoregressively streaming long-video generation.

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

### 11. Lottery Prior: Randomized Neural Compression for Zero-Shot Inverse Problems

Flags: program_signal_low_public_attention, oral

- Subarea: Diffusion sampling, transport, and inverse problems
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/63286
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: Diffusion / flow; Compression / efficiency
- Evaluation settings: vision/video
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

We study zero-shot inverse problems, where a clean signal is recovered from a single degraded observation without external training data. Contrary to the common belief that such problems require highly complex models, we show that a lightweight neural network, when combined with entropy and complexity regularization in a compression-based formulation, is sufficient for high-quality restoration. We propose Lottery Prior, a compression-based inverse solver that leverages architectural priors from random networks and induces a family of implicit priors through randomness, enabling ensemble-based refinement. We further derive non-asymptotic error bounds for compression-based maximum-likelihood inverse solvers, revealing how rate–distortion constraints act as implicit regularizers. Experiments on denoising, noisy super-resolution, and inpainting demonstrate that our method achieves state-of-the-art with significantly fewer effective parameters.

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

### 12. Riemannian Metric Matching for Scalable Geometric Modeling of Distributions

Flags: program_signal_low_public_attention, oral

- Subarea: Diffusion sampling, transport, and inverse problems
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/64721
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Theory / proof; System / infrastructure; Method / algorithm
- Method families: Agents / tool use; Diffusion / flow; Bayesian / probabilistic; Graphs / geometry
- Evaluation settings: none
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: accuracy

Abstract:

High-dimensional datasets often concentrate near low-dimensional structures, but estimating their geometry from samples typically relies on graphs and kernels that scale poorly with dataset size and dimension. We propose **Riemannian metric matching**: a denoising probabilistic framework for learning the Riemannian geometry of data using neural networks. Specifically, we learn the *carré du champ* operator, which, using diffusion geometry, gives us access to the Riemannian geometry toolkit for downstream machine learning and statistical tasks. Our key observation is that the carré du champ operator can be formulated as a conditional expectation over random perturbations of the data, which can be exploited for sample-wise training and constant cost, amortized inference without explicit kernel construction. To the best of our knowledge, we provide the first neural surrogate that estimates the underlying Riemannian geometry of data with a provable consistency guarantee in the large data limit. Empirically, metric matching rivals or improves the accuracy of $k$-NN-based diffusion geometry estimators, while enabling amortized inference that is up to $400\times$ faster, and supports graph-free geometric analysis on high-dimensional images where nearest neighbors break down.

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

### 13. Conditional Diffusion Sampling

Flags: low_evidence_code_confidence, evidence-low, github

- Subarea: Diffusion sampling, transport, and inverse problems
- Votes: 32
- ICML URL: https://icml.cc/virtual/2026/poster/61932
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.04013
- GitHub URL: https://github.com/blt2114/twisted_diffusion_sampler
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: Diffusion / flow; Bayesian / probabilistic
- Evaluation settings: none
- Result claim cues: negative / limitation; scaling / efficiency; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Sampling from unnormalized multimodal distributions with limited density evaluations remains a fundamental challenge in machine learning and natural sciences. Successful approaches construct a bridge between a tractable reference and the target distribution. Parallel Tempering (PT) serves as the gold standard, while recent diffusion-based approaches offer a continuous alternative at the cost of neural training. In this work, we introduce Conditional Diffusion Sampling (CDS), a framework that combines these two paradigms. To this end, we derive Conditional Interpolants, a class of stochastic processes whose transport dynamics are governed by an exact, closed-form stochastic differential equation (SDE), requiring no neural approximation. Although these dynamics require sampling from a non-trivial initialization distribution, we show both theoretically and empirically that the cost of this initialization diminishes for sufficiently short diffusion times. CDS leverages this by a two-stage procedure: (1) PT is used to efficiently sample the initial distribution, and then (2) samples are transported via the transport SDE. This combination couples the robust global exploration of PT with efficient local transport. Experiments suggest that CDS has the potential to achieve a superior trade-off between sample quality and density evaluation cost compared to state-of-the-art samplers.

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

### 14. Evaluating the Representation Space of Diffusion Models via Self-Supervised Principles

Flags: low_evidence_code_confidence, evidence-low, github

- Subarea: Image/video diffusion and flow generation
- Votes: 18
- ICML URL: https://icml.cc/virtual/2026/poster/66522
- AlphaXiv URL: https://www.alphaxiv.org/abs/2606.09718
- GitHub URL: https://github.com/Heimine/Heimine.github.io
- Artifact confidence: github_url_no_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Method / algorithm
- Method families: Diffusion / flow; Graphs / geometry
- Evaluation settings: none
- Result claim cues: negative / limitation
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Diffusion models are effective generative frameworks with strong representation learning capabilities, yet the intrinsic properties that govern their semantic structure and generalization remain poorly understood. Drawing inspiration from self-supervised representation learning (SSL), we introduce an evaluation framework that decomposes diffusion features into a perturbation invariant component and a residual component induced by noise and augmentations. From this decomposition we derive the Invariant Contamination Ratio (ICR), a Fisher-based metric that measures how residual, augmentation-sensitive energy contaminates invariant signal in feature space. We use this framework to analyze both discriminative and generative behavior. On the representation side, we find invariance peaks at intermediate noise levels, which also yield the best downstream classification performance. On the generative side, we study how training transitions from genuine generalization to memorization in data-limited regimes, and find that $\mathrm{ICR}$ serves as a sensitive training time indicator of the early learning phenomenon: rising residual energy along Fisher directions marks the onset of memorization, detectable from training features alone without external evaluators or held-out test sets. Overall, our results show diffusion models can be monitored from a self-supervised perspective via the geometry of their learned representations.

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

### 15. Generation is Required for Data-Efficient Perception

Flags: low_evidence_code_confidence, evidence-low

- Subarea: Image/video diffusion and flow generation
- Votes: 17
- ICML URL: https://icml.cc/virtual/2026/poster/66665
- AlphaXiv URL: https://www.alphaxiv.org/abs/2512.08854
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Theory / proof; Method / algorithm
- Method families: none
- Evaluation settings: vision/video; theory/synthetic
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

It has been hypothesized that human-level visual perception requires a generative approach in which internal representations result from inverting a decoder. Yet today’s most successful vision models are non-generative, relying on an encoder that maps images to representations without decoder inversion. This raises the question of whether generation is, in fact, necessary for machines to achieve human-level visual perception. To address this, we study whether generative and non-generative methods can achieve compositional generalization, a hallmark of human perception. Under a compositional data generating process, we formalize the inductive biases required to guarantee compositional generalization in decoder-based (generative) and encoder-based (non-generative) methods. We then show theoretically that enforcing these inductive biases on encoders is generally infeasible using regularization or architectural constraints. In contrast, for generative methods, the inductive biases can be enforced straightforwardly, thereby enabling compositional generalization by constraining a decoder and inverting it. We highlight how this inversion can be performed efficiently, either online through gradient-based search or offline through generative replay. We examine the empirical implications of our theory by training a range of generative and non-generative methods on photorealistic image datasets. We find that, without the necessary inductive biases, non-generative methods often fail to generalize compositionally and require large-scale pretraining to improve generalization. By comparison, generative methods yield significant improvements in compositional generalization, without requiring additional data, by leveraging suitable inductive biases on a decoder along with search and replay.

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

### 16. Learning to Watermark in the Latent Space of Generative Models

Flags: low_evidence_code_confidence, evidence-low, github

- Subarea: Image/video diffusion and flow generation
- Votes: 16
- ICML URL: https://icml.cc/virtual/2026/poster/63642
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.16140
- GitHub URL: https://github.com/facebookresearch/distseal
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: Diffusion / flow
- Evaluation settings: none
- Result claim cues: scaling / efficiency; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Existing approaches for watermarking AI-generated images often rely on post-hoc methods applied in pixel space, introducing computational overhead and potential visual artifacts. In this work, we explore latent space watermarking and introduce DistSeal, a unified approach for latent watermarking that works across both diffusion and autoregressive models. Our approach works by training post-hoc watermarking models in the latent space of generative models. We demonstrate that these latent watermarkers can be effectively distilled either into the generative model itself or into the latent decoder, enabling in-model watermarking. The resulting latent watermarks achieve competitive robustness while offering similar imperceptibility and up to 20x speedup compared to pixel-space baselines. Our experiments further reveal that distilling latent watermarkers outperforms distilling pixel-space ones, providing a solution that is both more efficient and more robust.

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
