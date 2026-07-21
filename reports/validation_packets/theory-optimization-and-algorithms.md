# Theory, Optimization, and Algorithms

Manual validation packet for representative and boundary papers.

## Area Context

Headline: The theory track is balancing classical guarantees with explanations of transformer-era behavior.

Fault lines:
- Asymptotic or idealized guarantees versus phenomena observed in current large-scale models.
- Optimization theory for convex/stochastic settings versus practical deep-network training dynamics.
- Probabilistic and Bayesian rigor versus scalable approximate inference.

What to read for:
- Which assumptions are doing the real work?
- Does the theorem explain a contemporary empirical pattern or stand as a separate mathematical result?
- Are constants, dimensions, and compute requirements meaningful at modern model scales?

## Queue Summary

- Papers: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, program_signal_low_public_attention=4, taxonomy_boundary_cluster=2
- Papers from taxonomy-review clusters: 9
- Papers with GitHub URLs: 5

## Papers

### 1. To Grok Grokking: Provable Grokking in Ridge Regression

Flags: fault_line_representative, oral, Outstanding Paper Honorable Mention, taxonomy-review, evidence-low

- Subarea: Statistical learning theory and regression
- Votes: 7
- ICML URL: https://icml.cc/virtual/2026/poster/66206
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.19791
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: none
- Evaluation settings: theory/synthetic
- Result claim cues: negative / limitation
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

We study *grokking* - the onset of generalization long after overfitting - in a classical ridge regression setting. We prove end-to-end grokking results for learning over-parameterized linear regression models using gradient descent with weight decay. Specifically, we prove that the following stages occur: (i) the model overfits the training data early during training; (ii) poor generalization persists long after overfitting has manifested; and (iii) the generalization error eventually becomes arbitrarily small. Moreover, we show, both theoretically and empirically, that grokking can be amplified or eliminated in a principled manner through proper hyperparameter tuning. To the best of our knowledge, these are the first rigorous quantitative bounds on the generalization delay (which we refer to as the "grokking time") in terms of training hyperparameters. Lastly, going beyond the linear setting, we empirically demonstrate that our quantitative bounds also capture the behavior of grokking on non-linear neural networks. Our results suggest that grokking is not an inherent failure mode of deep learning, but rather a consequence of specific training conditions, and thus does not require fundamental changes to the model architecture or learning algorithm to avoid.

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

### 2. Equivalence of Context and Parameter Updates in Modern Transformer Blocks

Flags: fault_line_representative, oral, taxonomy-review

- Subarea: Transformer theory and attention expressivity
- Votes: 24
- ICML URL: https://icml.cc/virtual/2026/poster/63048
- AlphaXiv URL: https://www.alphaxiv.org/abs/2511.17864
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: Transformer / attention
- Evaluation settings: language/llm; theory/synthetic
- Result claim cues: scaling / efficiency
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Recent research has established that the impact of context in a vanilla transformer can be represented implicitly by forming a token-dependent, rank-1 patch to its MLP weights. This work extends that foundational theory to the diverse architectures of modern Large Language Models. We first demonstrate a precise, analytical solution for a Gemma-style transformer block, proving that the entire effect of a context can be perfectly mapped to rank-1 patches on its MLP weight matrices and a patch to the RMSNorm scale. We then generalize this result, providing a constructive proof and algorithm for multi-layer models. To unify these findings, we introduce a general framework centered on two core properties: input controllability and output controllability. We prove that a perfect implicit weight patch is possible for any MLP block where the inner function is input-controllable and the outer function is output-controllable. This provides a simpler and more powerful lens for understanding how transformer models transmute prompts into effective weights. This setup generalizes to a wide range of modern LLM architectures including gating, pre-/post-norm, mixture of experts and sequential/parallel transformer blocks.

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

### 3. Non-Euclidean Gradient Descent Operates at the Edge of Stability

Flags: fault_line_representative, oral

- Subarea: Convex, stochastic, and nonconvex optimization
- Votes: 15
- ICML URL: https://icml.cc/virtual/2026/poster/61486
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.05002
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: Graphs / geometry
- Evaluation settings: theory/synthetic
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

The Edge of Stability (EoS) is a phenomenon where the sharpness (largest eigenvalue) of the Hessian converges to $2/\eta$ during training with gradient descent (GD) with a step-size $\eta$. Despite violating classical smoothness assumptions, EoS has been widely observed in deep learning, but its theoretical foundations remain incomplete. We propose a framework for analyzing EoS of non-Euclidean GD using directional smoothness (Mishkin et al., 2024), which naturally extends to non-Euclidean norms. This approach allows us to characterize EoS beyond the standard Euclidean setting, encompassing methods such as $\ell_{\infty}$-descent, Block CD, Spectral GD, and Muon without momentum. We derive the appropriate measure of the generalized sharpness under an arbitrary norm. Our generalized sharpness measure includes previously studied vanilla GD and preconditioned GD as special cases. Through analytical results and experiments on neural networks, we show that non-Euclidean GD also exhibits progressive sharpening followed by oscillations around the threshold $2/\eta$. Practically, our framework provides a single, geometry-aware spectral measure that works across optimizers, bridging the gap between empirical observations and deep learning theory.

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

### 4. Markov Chain Monte Carlo without Evaluating the Target: an Auxiliary Variable Approach

Flags: fault_line_representative, oral

- Subarea: Bayesian and probabilistic methods
- Votes: 6
- ICML URL: https://icml.cc/virtual/2026/poster/62793
- AlphaXiv URL: https://www.alphaxiv.org/abs/2406.05242
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Method / algorithm
- Method families: Diffusion / flow; Bayesian / probabilistic
- Evaluation settings: theory/synthetic
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

In sampling tasks, it is common for target distributions to be known up to a normalizing constant. However, in many situations, even evaluating the unnormalized distribution can be costly or infeasible. This issue arises in scenarios such as sampling from the Bayesian posterior for tall datasets and the 'doubly-intractable' distributions. In this paper, we begin by observing that seemingly different Markov chain Monte Carlo (MCMC) algorithms, such as the exchange algorithm, PoissonMH, and TunaMH, can be unified under a simple common procedure. We then extend this procedure into a novel framework that allows the use of auxiliary variables in both the proposal and the acceptance--rejection step. Several new MCMC algorithms emerge from this framework that uses estimated gradients to guide the proposal moves. They have demonstrated significantly better performance than existing methods on both synthetic and real datasets. We also develop theory for the new framework and use it to simplify and extend results for existing algorithms.

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

### 5. Optimal Decision-Making Based on Prediction Sets

Flags: fault_line_representative, oral, taxonomy-review, github

- Subarea: Statistical learning theory and regression
- Votes: 6
- ICML URL: https://icml.cc/virtual/2026/poster/63638
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.00989
- GitHub URL: https://github.com/salma123456789123456789-dotcom/Pneumonia-Detection-using-Chest-X-Ray-images
- Artifact confidence: github_url_no_stars
- Cluster review: needs_review; split across lexical clusters

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Application / domain study; Method / algorithm
- Method families: RL / policy optimization; Bayesian / probabilistic
- Evaluation settings: science/domain; security/safety; theory/synthetic
- Result claim cues: robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Prediction sets can wrap around any ML model to cover unknown test outcomes with a guaranteed probability. Yet, it remains unclear how to use them optimally for downstream decision-making. Here, we propose a decision-theoretic framework that seeks to minimize the expected loss (risk) against a worst-case distribution consistent with the prediction set's coverage guarantee. We first characterize the minimax optimal policy for a fixed prediction set, showing that it balances the worst-case loss inside the set with a penalty for potential losses outside the set. Building on this, we derive the optimal prediction set construction that minimizes the resulting robust risk subject to a coverage constraint. Finally, we introduce Risk-Optimal Conformal Prediction (ROCP), a practical algorithm that targets these risk-minimizing sets while maintaining finite-sample distribution-free marginal coverage. Empirical evaluations on medical diagnosis and safety-critical decision-making tasks demonstrate that ROCP reduces critical mistakes compared to baselines, particularly when out-of-set errors are costly.

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

### 6. Rational Transductors

Flags: fault_line_representative, oral, taxonomy-review

- Subarea: Transformer theory and attention expressivity
- Votes: 4
- ICML URL: https://icml.cc/virtual/2026/poster/61046
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.07599
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: Reasoning / test-time compute; Transformer / attention
- Evaluation settings: theory/synthetic
- Result claim cues: negative / limitation; robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Standard Transformers excel at semantic modeling but struggle with rigid sequential logic and state tracking. Theoretical work establishes that self-attention is limited to $\AC^0$ (under hard attention) or $\TC^0$ (under soft attention), complexity classes that often fail to support robust length generalization on sequential problems without intermediate chain-of-thought \citep{hahn2020theoretical, merrill2022saturated}. In this work, we introduce \emph{Rational Transductors}, a dual-stream architecture that augments the Transformer with a matrix-valued recurrence derived from Weighted Finite Automata (WFA). By injecting rational state information into the attention mechanism via a \emph{Deep Rational Injection} scheme, our framework strictly generalizes Transformers to capture all Regular Languages, $\NC^1$-complete problems (such as Boolean Formula Evaluation), and fundamental separations like Parity and Modular Counting, while preserving $O(\log T)$ parallel training efficiency. Theoretical analysis and empirical results demonstrate that Rational Transductors solve the "Regular Gap," enabling robust length generalization on algorithmic tasks where standard Transformers fail, without the sequential computational bottlenecks of traditional RNNs.

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

### 7. Unifying and Optimizing Data Values for Selection via Sequential Decision-Making

Flags: public_attention_not_program_signal, github

- Subarea: Online learning, bandits, and regret
- Votes: 271
- ICML URL: https://icml.cc/virtual/2026/poster/65157
- AlphaXiv URL: https://www.alphaxiv.org/abs/2502.04554
- GitHub URL: https://github.com/frankhlchi/SequentialDataVal
- Artifact confidence: github_url_no_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Theory / proof; Method / algorithm
- Method families: LLM post-training; Causal / data-centric; Graphs / geometry
- Evaluation settings: math/code/verifiable; language/llm; theory/synthetic
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Data selection has emerged as a crucial downstream application of data valuation, yet the theoretical foundations for using data values in selection remain underexplored. We reformulate data selection as a sequential decision-making problem where the optimal selection sequence arises from dynamic programming, and data values can be understood as encodings of this optimal sequence. This framework unifies and reinterprets existing methods like Data Shapley through the lens of approximate dynamic programming, revealing them as myopic linear approximations to the sequential problem. We further analyze how selection optimality degrades with utility curvature under submodularity, explaining when and why these approximations fail. To bridge theory and practice, we propose an efficient bipartite graph-based surrogate that preserves submodular structure while enabling scalable greedy selection with provable guarantees. Experiments on classical ML benchmarks and large-scale LLM fine-tuning data selection demonstrate substantial improvements over existing methods.

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

### 8. Dimensional Collapse in Transformer Attention Outputs: A Challenge for Sparse Dictionary Learning

Flags: public_attention_not_program_signal, taxonomy-review

- Subarea: Transformer theory and attention expressivity
- Votes: 160
- ICML URL: https://icml.cc/virtual/2026/poster/64760
- AlphaXiv URL: https://www.alphaxiv.org/abs/2508.16929
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Application / domain study; Method / algorithm
- Method families: Agents / tool use; Transformer / attention; Compression / efficiency; Graphs / geometry
- Evaluation settings: math/code/verifiable; language/llm
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Transformer architectures, and their attention mechanisms in particular, form the foundation of modern large language models. While transformer models are widely believed to operate in high-dimensional hidden spaces, we show that attention outputs are confined to a surprisingly low-dimensional subspace, with an effective dimensionality of only about 60\% of the full space---a phenomenon that is consistently observed across diverse model families and datasets, and is strongly influenced by the attention output projection matrix. Critically, we find this low-rank structure as a key factor of the prevalent dead feature problem in sparse dictionary learning, where it creates a mismatch between randomly initialized features and the intrinsic geometry of the activation space. Building on this insight, we propose a subspace-constrained training method for sparse autoencoders (SAEs), initializing feature directions into the active subspace of activations. Our approach reduces dead features from 87\% to below 1\% in Attention Output SAEs with 1M features, and can further extend to other sparse dictionary learning methods. Our findings provide both new insights into the geometry of attention and practical tools for improving sparse dictionary learning in large language models. Code is available at \url{https://anonymous.4open.science/r/Language-Model-SAEs-C015}.

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

### 9. Weight-sparse transformers have interpretable circuits

Flags: public_attention_not_program_signal, taxonomy-review, github

- Subarea: Transformer theory and attention expressivity
- Votes: 137
- ICML URL: https://icml.cc/virtual/2026/poster/63567
- AlphaXiv URL: https://www.alphaxiv.org/abs/2511.13653
- GitHub URL: https://github.com/alihan-ozturk/L0-Weight-Sparse-Reinforcement-Learning-PPO
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: Transformer / attention; Compression / efficiency
- Evaluation settings: language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Finding human-understandable circuits in language models is a central goal of the field of mechanistic interpretability. We train models to have more understandable circuits by constraining most of their weights to be zeros, so that each neuron only has a few connections. To recover fine-grained circuits underlying each of several hand-crafted tasks, we prune the models to isolate the part responsible for the task. These circuits often contain neurons and residual channels that correspond to natural concepts, with a small number of straightforwardly interpretable connections between them. We study how these models scale and find that making weights sparser trades off capability for interpretability, and scaling model size improves the capability-interpretability frontier. However, scaling sparse models beyond tens of millions of nonzero parameters while preserving interpretability remains a challenge. In addition to training weight-sparse models de novo, we show preliminary results suggesting our method can also be adapted to explain existing dense models. Our work produces circuits that achieve an unprecedented level of human understandability and validates them with considerable rigor.

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

### 10. You Need Better Attention Priors

Flags: public_attention_not_program_signal, taxonomy-review, github

- Subarea: Transformer theory and attention expressivity
- Votes: 78
- ICML URL: https://icml.cc/virtual/2026/poster/64188
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.15380
- GitHub URL: https://github.com/anupamabedi/Top-MPPSC-Coaching-in-Indore-with-Fee-Structure
- Artifact confidence: github_url_with_stars
- Cluster review: needs_review; manual confidence not high

Heuristic evidence codes:
- Primary contribution: System / infrastructure
- Contribution types: System / infrastructure; Method / algorithm
- Method families: Transformer / attention
- Evaluation settings: vision/video
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

We generalize the attention mechanism by viewing it through the lens of Entropic Optimal Transport, revealing that standard attention corresponds to a transport problem regularized by an implicit uniform prior. We introduce Generalized Optimal transport Attention with Trainable priors (GOAT), a new attention mechanism that replaces this naive assumption with a learnable, continuous prior. This prior maintains full compatibility with optimized kernels such as FlashAttention. GOAT also provides an EOT-based explanation of attention sinks and materializes a solution for them, avoiding the representational trade-offs of standard attention. Finally, by absorbing spatial information into the core attention computation, GOAT learns an extrapolatable prior that combines the flexibility of learned positional embeddings with the length generalization of fixed encodings.

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

### 11. Path-dependent Discrete Amortized Inference

Flags: program_signal_low_public_attention, oral, evidence-low

- Subarea: Bayesian and probabilistic methods
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/60879
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Theory / proof; Method / algorithm
- Method families: RL / policy optimization; Diffusion / flow; Bayesian / probabilistic
- Evaluation settings: none
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

We consider the problem of sampling compositional and discrete objects from a given unnormalized posterior distribution. Notably, recent studies have shown that this problem can be efficiently solved by learning a deterministic Markov Decision Process (MDP) that progressively builds each object in proportion to the posterior. In this work, however, we demonstrate that the Markovian assumption can both hamper signal propagation during training and catastrophically reduce the learned sampler's expressivity due to state aliasing. To address these issues, we propose lifting the MDP with a learnable latent dynamics that allows the underlying policy to depend on the entire past trajectory---and not only on the current state. In view of this, we refer to the resulting method as \emph{path-dependent discrete amortized inference}. Importantly, we provably extend existing learning algorithms for amortized samplers to our setting. In experiments on standard benchmark problems, we also show that our approach often leads to faster learning convergence and improved state space exploration relatively to prior techniques.

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

### 12. Robust Contextual Optimization with Missing Covariates

Flags: program_signal_low_public_attention, oral, evidence-low

- Subarea: Bayesian and probabilistic methods
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/66499
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Theory / proof; Method / algorithm
- Method families: none
- Evaluation settings: none
- Result claim cues: robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Modern decision-making increasingly relies on contextual features (covariates) to improve optimization under uncertainty. In practice, however, such covariates are often only partially observed due to, e.g., data source heterogeneity or costly data collection. Nonetheless, most existing methods assume fully observed historical data and can become unreliable when this assumption is violated. We address this gap by proposing a distributionally robust optimization approach that exploits incomplete covariates to produce robust decisions without imputing a complete dataset. Our method builds ambiguity sets from the observed partial data and incorporates the general structure of the missingness mechanism, ensuring candidate distributions remain consistent with what is observed. Across settings with discrete or continuous covariates and outcomes, we derive tractable reformulations and establish finite-sample out-of-sample performance guarantees. Empirical results across a range of contextual decision-making tasks demonstrate that the proposed integrated approach consistently outperforms state-of-the-art baselines, including various impute-then-optimize pipelines, in both out-of-sample performance and reliability.

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

### 13. DPO Unchained: Your Training Algorithm is Secretly Disentangled in Human Choice Theory (and Its Loss' Convexity is Dispensable)

Flags: program_signal_low_public_attention, oral

- Subarea: Online learning, bandits, and regret
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/62171
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: RL / policy optimization; LLM post-training
- Evaluation settings: theory/synthetic
- Result claim cues: robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: reward

Abstract:

Normative theories allow one to elicit key parts of a ML algorithm from first principles, which is crucial at a time of championed scrutiny for ML work. Direct Preference Optimization (DPO) cleverly bypasses reward modeling by making an explicit link with a specific normative model of human choice. Our paper elevates this connection to the full generality of DPO's normative framework. Getting there requires reworking social choice theory's textbook path for a better RLHF/ML fit. It elevates the connection to a remarkably broad viewpoint on preference optimization, considering the current panorama of DPO follow-ups. It also unveils unexpected riches for ML, chief among which the support for *non-convex* losses, the fact that *any* compliant ML analytical choice can be embedded with *any* human choice model, and a normative framework's umbrella wide enough to safeguard DPO's *extensions* (margins, length correction, ...). A *toy* experiment ``far away'' from the DPO crowd is given.

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

### 14. Equilibrium Pricing in Oligopolistic Data Markets

Flags: program_signal_low_public_attention, oral, evidence-low

- Subarea: Online learning, bandits, and regret
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/63852
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Theory / proof
- Method families: none
- Evaluation settings: none
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: accuracy

Abstract:

We study equilibrium pricing in oligopolistic data markets with budget-constrained buyers (e.g., ML companies purchasing data to improve model accuracy) and strategic data sellers. Sellers compete by setting prices for their datasets, giving rise to a pricing game whose pure Nash equilibria correspond to equilibrium prices. While equilibrium prices are guaranteed for rivalrous goods via competitive equilibrium, we show that the non-rivalry of data fundamentally alters this picture: an exact Nash equilibrium need not exist, and in fact no 1.364-approximate equilibrium exists under uniform pricing. We therefore investigate relaxed equilibrium notions. Allowing sellers to use beyond-uniform pricing—specifically, piecewise-linear convex pricing functions—guarantees approximate stability within a constant factor: there exists a pricing profile in which no seller can improve revenue by a factor of two by deviating to any uniform price (a 2-approximate Nash equilibrium). Finally, our simulations demonstrate fast convergence and empirical approximation guarantees that outperform the worst-case bound of 2.

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

### 15. Do Transformers Need Three Projections? Systematic Study of QKV Variants

Flags: taxonomy_boundary_cluster, taxonomy-review, github

- Subarea: Transformer theory and attention expressivity
- Votes: 74
- ICML URL: https://icml.cc/virtual/2026/poster/63430
- AlphaXiv URL: https://www.alphaxiv.org/abs/2606.04032
- GitHub URL: https://github.com/alikayyam/Do-Transformers-Need-3-Projections
- Artifact confidence: github_url_no_stars
- Cluster review: needs_review; manual confidence not high

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; System / infrastructure; Method / algorithm
- Method families: Transformer / attention
- Evaluation settings: vision/video; language/llm; theory/synthetic
- Result claim cues: scaling / efficiency
- Benchmarks: GQA; MQA; GQA-4
- Datasets: none
- Metrics: perplexity; memory

Abstract:

Transformers have become the standard solution for various AI tasks, with the query, key, and value (QKV) attention formulation playing a central role. However, the individual contribution of these three projections and the impact of omitting some remain poorly understood. We systematically evaluate three projection sharing constraints: a) Q-K=V (shared key-value), b) Q=K-V (shared query-key), and c) Q=K=V (single projection). The last two variants produce symmetric attention maps; to address this, we also explore asymmetric attention via 2D positional encodings. Through experiments spanning synthetic tasks, vision (MNIST, CIFAR, TinyImageNet, anomaly), and language modeling (300M and 1.2B parameter models on 10B tokens), we discovered that our transformers perform on par or occasionally better than the QKV transformer. In language modeling, Q-K=V projection sharing achieves 50\% KV cache reduction with only 3.1% perplexity degradation. Crucially, projection sharing is complementary to head sharing (GQA/MQA): combining Q-K=V with GQA-4 yields 87.5% cache reduction, while Q-K=V + MQA achieves 96.9%—enabling practical on-device inference. We further show that Q--K=V preserves quality because keys and values can share representational space, whereas Q=K-V breaks attention directionality. Our results establish projection sharing as a new optimization axis for memory-efficient transformers, especially for edge deployment.

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

### 16. Patterning: The Dual of Interpretability

Flags: taxonomy_boundary_cluster, taxonomy-review

- Subarea: Transformer theory and attention expressivity
- Votes: 55
- ICML URL: https://icml.cc/virtual/2026/poster/65584
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.13548
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: needs_review; manual confidence not high

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: Bayesian / probabilistic
- Evaluation settings: language/llm; theory/synthetic
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: accuracy

Abstract:

Mechanistic interpretability aims to understand how neural networks generalize beyond their training data by reverse-engineering their internal structures. We introduce patterning as the dual problem: given a desired form of generalization, determine what training data produces it. Our approach is based on susceptibilities, which measure how posterior expectation values of observables respond to infinitesimal shifts in the data distribution. Inverting this linear response relationship yields the data intervention that steers the model toward a target internal configuration. We demonstrate patterning in a small language model, showing that re-weighting training data along principal susceptibility directions can accelerate or delay the formation of structure, such as the induction circuit. In a synthetic parentheses balancing task where multiple algorithms achieve perfect training accuracy, we show that patterning can select which algorithm the model learns by targeting the local learning coefficient of each solution. These results establish that the same mathematical framework used to read internal structure can be inverted to write it.

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
