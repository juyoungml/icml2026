# Reinforcement Learning and Control

Manual validation packet for representative and boundary papers.

## Area Context

Headline: Core RL is active but less publicly amplified than LLM-facing RL, with emphasis on offline learning, control, and computation.

Fault lines:
- Classical RL/control objectives versus foundation-model-era policy learning.
- Offline and preference-based RL versus online exploration and sample efficiency.
- Theoretical computation limits versus practical robotic/control deployment.

What to read for:
- Does the method require online interaction or strong simulator assumptions?
- How are stability, exploration, and reward misspecification handled?
- Is the contribution algorithmic, theoretical, or a new evaluation/control setting?

## Queue Summary

- Papers: 16
- Selection mix: fault_line_representative=6, low_evidence_code_confidence=6, public_attention_not_program_signal=4
- Papers from taxonomy-review clusters: 0
- Papers with GitHub URLs: 6

## Papers

### 1. On Computation and Reinforcement Learning

Flags: fault_line_representative, oral, github

- Subarea: Core RL, offline RL, and policy optimization
- Votes: 11
- ICML URL: https://icml.cc/virtual/2026/poster/65047
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.05999
- GitHub URL: https://github.com/jordan8409212/RL-for-binary-computation-offloading-in-wireless-powered-MEC-networks
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: RL / policy optimization
- Evaluation settings: language/llm; theory/synthetic
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

How does the amount of compute available to a reinforcement learning (RL) policy affect its learning? Can policies using a fixed amount of parameters, still benefit from additional compute? The standard RL framework does not provide a language to answer these questions formally. Empirically, deep RL policies are often parameterized as neural networks with static architectures, conflating the amount of compute and the number of parameters. In this paper, we formalize compute bounded policies and prove that policies which use more compute can solve problems and generalize to longer-horizon tasks that are outside the scope of policies with less compute. Building on prior work in algorithmic learning and model-free planning, we propose a minimal architecture that can use a variable amount of compute. Our experiments complement our theory. On a set 31 different tasks spanning online and offline RL, we show that $(1)$ this architecture achieves stronger performance simply by using more compute, and $(2)$ stronger generalization on longer-horizon test tasks compared to standard feedforward networks or deep residual network using upto 5 times more parameters.

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

### 2. Learning Human-Robot Collaboration via Heterogeneous-Agent Lyapunov Policy Optimization

Flags: fault_line_representative, oral

- Subarea: Core RL, offline RL, and policy optimization
- Votes: 10
- ICML URL: https://icml.cc/virtual/2026/poster/61049
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.03741
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Application / domain study
- Contribution types: Application / domain study; Method / algorithm
- Method families: RL / policy optimization; Agents / tool use; Bayesian / probabilistic
- Evaluation settings: robotics/embodied
- Result claim cues: robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

To improve generalization and resilience in human–robot collaboration (HRC), robots must handle the combinatorial diversity of human behaviors and contexts, motivating multi-agent reinforcement learning (MARL). However, inherent heterogeneity between robots and humans creates a rationality gap (RG) in the learning process--a variational mismatch between decentralized best-response dynamics and centralized cooperative ascent. The resulting learning problem is a general-sum differentiable game, so independent policy-gradient updates can oscillate or diverge without added structure. We propose heterogeneous-agent Lyapunov policy optimization (HALyPO), which establishes formal stability directly in the policy-parameter space by enforcing a per-step Lyapunov decrease condition on a parameter-space disagreement metric. Unlike Lyapunov-based safe RL, which targets state/trajectory constraints in constrained Markov decision processes, HALyPO uses Lyapunov certification to stabilize decentralized policy learning. HALyPO rectifies decentralized gradients via optimal quadratic projections, ensuring monotonic contraction of RG and enabling effective exploration of open-ended interaction spaces. Extensive simulations and real-world humanoid-robot experiments show that this certified stability improves generalization and robustness in collaborative corner cases.

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

### 3. Distributional Inverse Reinforcement Learning

Flags: fault_line_representative, oral, github

- Subarea: Core RL, offline RL, and policy optimization
- Votes: 5
- ICML URL: https://icml.cc/virtual/2026/poster/63146
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.03013
- GitHub URL: https://github.com/sudharsan13296/Deep-Reinforcement-Learning-With-Python
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Theory / proof; Method / algorithm
- Method families: RL / policy optimization
- Evaluation settings: robotics/embodied; theory/synthetic
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: reward

Abstract:

We propose a distributional framework for offline Inverse Reinforcement Learning (IRL) that jointly models uncertainty over reward functions and full distributions of returns. Unlike conventional IRL approaches that recover a deterministic reward estimate or match only expected returns, our method captures richer structure in expert behavior, particularly in learning the reward distribution, by minimizing first-order stochastic dominance (FSD) violations and thus integrating distortion risk measures (DRMs) into policy learning, enabling the recovery of both reward distributions and distribution-aware policies. This formulation is well-suited for behavior analysis and risk-aware imitation learning. Theoretical analysis show that the algorithm converge with $\mathcal{O}(\varepsilon^{-2})$ iteration complexity. Empirical results on synthetic benchmarks, real-world neurobehavioral data, and MuJoCo control tasks demonstrate that our method recovers expressive reward representations and achieves state-of-the-art imitation performance.

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

### 4. Chebyshev Policies and the Mountain Car Problem: Reinforcement Learning for Low-dimensional Control Tasks

Flags: fault_line_representative, oral

- Subarea: Core RL, offline RL, and policy optimization
- Votes: 3
- ICML URL: https://icml.cc/virtual/2026/poster/63070
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.22305
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Theory / proof
- Method families: RL / policy optimization; Agents / tool use
- Evaluation settings: robotics/embodied; theory/synthetic
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: regret

Abstract:

We analytically solve the Mountain Car problem, a canonical benchmark in RL, and derive an optimal control solution, closing a gap after 36 years. This enables us to reveal two surprising insights: The optimal control is quite simple, yet modern RL agents display a large gap to optimality. Motivated by the analysis of the optimal control, we introduce Chebyshev policies as a universal (i.e. dense) class of RL policies from first principles. They can be trained as drop-in replacements of neural nets, reducing the regret by a factor of 4.18, while requiring 268 times fewer parameters, fostering sample efficiency, explainability and real-time capability. Chebyshev policies are evaluated on further RL environments, including a real-world non-linear motion control testbed. They consistently improve performance over neural nets with PPO, ARS and REINFORCE. Our results demonstrate how Chebyshev policies offer a compelling and lightweight alternative or addition to neural nets for low-dimensional control tasks.

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

### 5. Stabilizing the Q-Gradient Field for Policy Smoothness in Actor-Critic Methods

Flags: fault_line_representative, oral

- Subarea: Core RL, offline RL, and policy optimization
- Votes: 2
- ICML URL: https://icml.cc/virtual/2026/poster/63664
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.22970
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Theory / proof; Method / algorithm
- Method families: RL / policy optimization; Graphs / geometry
- Evaluation settings: robotics/embodied; theory/synthetic
- Result claim cues: scaling / efficiency; robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Policies learned via continuous actor-critic methods often exhibit erratic, high-frequency oscillations, making them unsuitable for physical deployment. Current approaches attempt to enforce smoothness by directly regularizing the policy's output. We argue that this approach treats the symptom rather than the cause. In this work, we theoretically establish that policy non-smoothness is fundamentally governed by the differential geometry of the critic. By applying implicit differentiation to the actor-critic objective, we prove that the sensitivity of the optimal policy is bounded by the ratio of the Q-function's mixed-partial derivative (noise sensitivity) to its action-space curvature (signal distinctness). To empirically validate this theoretical insight, we introduce PAVE (Policy-Aware Value-field Equalization), a critic-centric regularization framework that treats the critic as a scalar field and stabilizes its induced action-gradient field. PAVE rectifies the learning signal by minimizing the Q-gradient volatility while preserving local curvature. Experimental results demonstrate that PAVE achieves smoothness and robustness comparable to policy-side smoothness regularization methods, while maintaining competitive task performance, without modifying the actor.

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

### 6. Video-Based Optimal Transport for Feedback-Efficient Offline Preference-Based Reinforcement Learning

Flags: fault_line_representative, oral

- Subarea: Core RL, offline RL, and policy optimization
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/65169
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; Application / domain study; Method / algorithm
- Method families: RL / policy optimization; LLM post-training; Agents / tool use
- Evaluation settings: vision/video; robotics/embodied
- Result claim cues: negative / limitation; scaling / efficiency; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: reward

Abstract:

Conveying complex objectives to reinforcement learning (RL) agents often requires meticulous reward engineering. Preference-based RL (PbRL) offers a promising alternative by learning reward functions from human feedback, but its scalability is hindered by high labeling costs. Inspired by advances in Video Foundation Models (ViFMs), we present Video-based Optimal Transport Preference (VOTP), a semi-supervised framework that learns effective reward functions from only a handful of labels. By leveraging optimal transport to align visual trajectories within the rich representation space of ViFMs, VOTP effectively generates high-fidelity pseudo-labels for large amounts of unlabeled data, substantially reducing human supervision. Extensive experiments across locomotion and manipulation benchmarks demonstrate the superiority of VOTP, which outperforms state-of-the-art offline PbRL methods under limited feedback budgets. We also showcase the robustness of VOTP in the presence of visual distractors and validate its utility on real robotic tasks, where it learns meaningful rewards with minimal human input.

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

### 7. Reinforcement Learning with Verifiable Rewards: GRPO's Loss, Dynamics, and Success Amplification

Flags: public_attention_not_program_signal

- Subarea: Core RL, offline RL, and policy optimization
- Votes: 305
- ICML URL: https://icml.cc/virtual/2026/poster/60548
- AlphaXiv URL: https://www.alphaxiv.org/abs/2503.06639
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource; Method / algorithm
- Method families: RL / policy optimization; Reasoning / test-time compute
- Evaluation settings: math/code/verifiable; language/llm; theory/synthetic
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: reward

Abstract:

Group Relative Policy Optimization (GRPO) was introduced recently and used to train DeepSeek\textendash R1 for promoting reasoning in LLMs under verifiable (binary) rewards. We show that the mean{+}variance calibration of these rewards induces a contrastive loss in which the contrastive samples are synthetic data drawn from the previous policy. While GRPO was originally paired with clipping to keep updates near the old policy, we analyze variants that differ in reward normalization (mean-only vs.\ mean{+}variance) and in how they regularize updates using KL divergence: either penalizing divergence from the previous model (\emph{mirror}), penalizing divergence from a fixed reference model $\pi_{\mathrm{ref}}$, or combining both forms of regularization. For each, the optimal policy $\pi_n$ admits an explicit form in terms of the binary reward and the first and second order statistics of the reward under $\pi_{n-1}$, as well as the policies $\pi_{n-1}$ and $\pi_{\mathrm{ref}}$. Iterating results in a sequence $\{\pi_n\}$ whose \emph{probability of success (PoS)} obeys a simple recurrence that converges to a fixed point determined by the reference PoS and the regularization strength. We further show that this fixed point exceeds the reference, demonstrating that GRPO amplifies the policy's probability of success.

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

### 8. Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers

Flags: public_attention_not_program_signal

- Subarea: Core RL, offline RL, and policy optimization
- Votes: 135
- ICML URL: https://icml.cc/virtual/2026/poster/63177
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.11370
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: RL / policy optimization; Compression / efficiency
- Evaluation settings: language/llm
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Reinforcement learning (RL) has emerged as a crucial approach for enhancing the capabilities of large language models. However, in Mixture-of-Experts (MoE) models, the routing mechanism often introduces instability, even leading to catastrophic RL training collapse. We analyze the training-inference consistency of MoE models and identify a notable discrepancy in routing behaviors between the two phases. To address this issue, we propose \textbf{Rollout Routing Replay (R3)}, a novel and effective method that records routing distributions from the inference engine and replays them during training. R3 significantly reduces training-inference policy KL divergence and mitigates extreme discrepancies without compromising training speed. Extensive experiments on various settings confirm that R3 succeeds in stabilizing RL training, preventing collapse and outperforming strong baselines. R3 is orthogonal to most policy optimization algorithm improvements, allowing it to be used in conjunction with them. We believe this work can offer a new solution for stabilizing RL in MoE model.

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

### 9. How Does the Lagrangian Guide Safe Reinforcement Learning through Diffusion Models?

Flags: public_attention_not_program_signal, github

- Subarea: Core RL, offline RL, and policy optimization
- Votes: 119
- ICML URL: https://icml.cc/virtual/2026/poster/61858
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.02924
- GitHub URL: https://github.com/Wenxuan52/ALGD
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: RL / policy optimization; Diffusion / flow
- Evaluation settings: robotics/embodied; security/safety; theory/synthetic
- Result claim cues: negative / limitation; robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: reward

Abstract:

Diffusion policy sampling enables reinforcement learning (RL) to represent multimodal action distributions beyond suboptimal unimodal Gaussian policies. However, existing diffusion-based RL methods primarily focus on offline setting for reward maximization, with limited consideration of safety in online settings. To address this gap, we propose Augmented Lagrangian-Guided Diffusion (ALGD), a novel algorithm for off-policy safe RL. By revisiting optimization theory and energy-based modeling, we show that the instability of primal–dual methods arises from the non-convex Lagrangian landscape. In diffusion-based safe RL, the Lagrangian can be interpreted as an energy function guiding the denoising dynamics; counter-intuitively, direct usage destabilizes both policy generation and training. ALGD resolves this issue by introducing an augmented Lagrangian that locally convexifies the energy landscape, yielding a stabilized policy generation and training, without altering the distribution of optimal policy. Theoretical analysis and extensive experiments demonstrate that ALGD is both theoretically grounded and empirically effective, achieving strong and stable performance across diverse environments.

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

### 10. Just-In-Time Reinforcement Learning: Continual Learning in LLM Agents Without Gradient Updates

Flags: public_attention_not_program_signal, github

- Subarea: Core RL, offline RL, and policy optimization
- Votes: 61
- ICML URL: https://icml.cc/virtual/2026/poster/61517
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.18510
- GitHub URL: https://github.com/liushiliushi/JitRL
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; System / infrastructure; Application / domain study; Method / algorithm
- Method families: RL / policy optimization; LLM post-training; Reasoning / test-time compute; Agents / tool use
- Evaluation settings: math/code/verifiable; robotics/embodied; language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: WebArena
- Datasets: none
- Metrics: memory

Abstract:

While Large Language Model (LLM) agents excel at general tasks, they inherently struggle with continual adaptation due to the frozen weights after deployment. Conventional reinforcement learning (RL) offers a solution but incurs prohibitive computational costs and the risk of catastrophic forgetting. We introduce Just-In-Time Reinforcement Learning (JitRL), a training-free framework that enables test-time policy optimization without any gradient updates. JitRL maintains a dynamic, non-parametric memory of experiences and retrieves relevant trajectories to estimate action advantages on-the-fly. These estimates are then used to directly modulate the LLM's output logits. We theoretically prove that this additive update rule is the exact closed-form solution to the KL-constrained policy optimization objective. Extensive experiments on WebArena and Jericho demonstrate that JitRL establishes a new state-of-the-art among training-free methods. Crucially, JitRL outperforms the performance of computationally expensive fine-tuning methods (e.g., WebRL) while reducing monetary costs by over 30 times, offering a scalable path for continual learning agents. The code is available at https://anonymous.4open.science/r/JitRL-D485.

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

### 11. What Does Flow-Matching Bring to TD-Learning?

Flags: low_evidence_code_confidence, evidence-low

- Subarea: Core RL, offline RL, and policy optimization
- Votes: 31
- ICML URL: https://icml.cc/virtual/2026/poster/62698
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.04333
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Method / algorithm
- Method families: RL / policy optimization; Reasoning / test-time compute; Diffusion / flow
- Evaluation settings: none
- Result claim cues: robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Recent work shows that flow-matching networks can be effective for value function estimation in reinforcement learning, but it remains unclear why they work well or whether flow-matching Q-functions differ fundamentally from standard critics. We show that their success is not explained by distributional RL: explicitly modeling return distributions often degrades performance. Instead, we argue that flow-matching Q-functions are effective because they couple a learned velocity field with an integration procedure that is used both during training and to read out Q-values at inference time. This coupling enables robust value prediction through \emph{test-time recovery} from imperfect intermediate estimates where errors dampen out as more integration steps are performed. This mechanism is absent in monolithic critics. Beyond test-time recovery, training with the integration procedure induces more \emph{plastic} representations, allowing critics to represent non-stationary future TD targets without overwriting previous features. We formalize these effects and validate them empirically, showing that flow-matching critics outperform monolithic critics by over $2\times$ in performance and achieve $5$–$10\times$ higher sample efficiency in high-UTD regimes.

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

### 12. Intentional Updates for Streaming Reinforcement Learning

Flags: low_evidence_code_confidence, evidence-low, github

- Subarea: Core RL, offline RL, and policy optimization
- Votes: 14
- ICML URL: https://icml.cc/virtual/2026/poster/64761
- AlphaXiv URL: https://www.alphaxiv.org/abs/2604.19033
- GitHub URL: https://github.com/sharifnassab/Intentional_RL
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof
- Method families: RL / policy optimization
- Evaluation settings: none
- Result claim cues: negative / limitation; scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

In gradient-based learning, a step size chosen in parameter units does not produce a predictable per-step change in the function output. This may lead to instability in the streaming setting (i.e., batch size=1), where stochasticity is not averaged out and update magnitudes can momentarily become arbitrarily big or small. Instead, we propose \emph{intentional updates}: first specify the \emph{intended outcome} of an update and then solve for the step size that approximately achieves it. This strategy has precedent in online supervised linear regression via normalized LMS, which selects a step size to yield a specified change in the function output proportional to the current error. We extend this principle to streaming reinforcement learning by defining appropriate intended outcomes: \emph{Intentional TD} aims for a fixed fractional reduction of the current TD error relative to the momentary bootstrap target, and \emph{Intentional Policy Gradient} aims for a bounded per-step change in the policy, limiting local KL divergence. We develop practical implementations integrating eligibility traces and diagonal scaling; our experiments show that these methods yield state-of-the-art streaming performance often comparable to batch and replay-buffer learning.

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

### 13. Offline Reinforcement Learning with Generative Trajectory Policies

Flags: low_evidence_code_confidence, evidence-low

- Subarea: Core RL, offline RL, and policy optimization
- Votes: 14
- ICML URL: https://icml.cc/virtual/2026/poster/64599
- AlphaXiv URL: https://www.alphaxiv.org/abs/2510.11499
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Benchmark / evaluation
- Method families: RL / policy optimization; Diffusion / flow
- Evaluation settings: none
- Result claim cues: negative / limitation; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Generative models have emerged as a powerful class of policies for offline reinforcement learning (RL) due to their ability to capture complex, multi-modal behaviors. However, existing methods face a stark trade-off: slow, iterative models like diffusion policies are computationally expensive, while fast, single-step models like consistency policies often suffer from degraded performance. In this paper, we demonstrate that it is possible to bridge this gap. The key to moving beyond the limitations of individual methods, we argue, lies in a unifying perspective that views modern generative models—including diffusion, flow matching, and consistency models—as specific instances of learning a continuous-time generative trajectory governed by an Ordinary Differential Equation (ODE). This principled foundation provides a clearer design space for generative policies in RL and allows us to propose *Generative Trajectory Policies* (GTPs), a new and more general policy paradigm that learns the entire solution map of the underlying ODE. To make this paradigm practical for offline RL, we further introduce two key theoretically principled adaptations. Empirical results demonstrate that GTP achieves state-of-the-art performance on D4RL benchmarks -- it significantly outperforms prior generative policies, achieving perfect scores on several notoriously hard AntMaze tasks.

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

### 14. Stable Deep Reinforcement Learning via Isotropic Gaussian Representations

Flags: low_evidence_code_confidence, evidence-low, github

- Subarea: Core RL, offline RL, and policy optimization
- Votes: 12
- ICML URL: https://icml.cc/virtual/2026/poster/62436
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.19373
- GitHub URL: https://github.com/asahebpa/IsoGaussian-DRL
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: RL / policy optimization
- Evaluation settings: none
- Result claim cues: state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Deep reinforcement learning systems often suffer from unstable training dynamics due to non-stationarity, where learning objectives and data distributions evolve over time. We show that under non-stationary targets, isotropic Gaussian embeddings are provably advantageous. In particular, they induce stable tracking of time-varying targets for linear readouts, achieve maximal entropy under a fixed variance budget, and encourage a balanced use of all representational dimensions. Building on this insight, we propose the use of Sketched Isotropic Gaussian Regularization for shaping representations toward an isotropic Gaussian during training. We demonstrate empirically, over a variety of domains, that this simple and computationally inexpensive method improves performance under non-stationarity while reducing representation collapse, neuron dormancy, and training instability.

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

### 15. BiTrajDiff: Bidirectional Trajectory Generation with Diffusion Models for Offline Reinforcement Learning

Flags: low_evidence_code_confidence, evidence-low

- Subarea: Core RL, offline RL, and policy optimization
- Votes: 11
- ICML URL: https://icml.cc/virtual/2026/poster/63499
- AlphaXiv URL: https://www.alphaxiv.org/abs/2506.05762
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; Method / algorithm
- Method families: RL / policy optimization; Diffusion / flow
- Evaluation settings: none
- Result claim cues: negative / limitation; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Offline Reinforcement Learning (RL) relies on static datasets and often enforces conservative constraints to mitigate out-of-distribution errors, but this inevitably gives rise to learning dataset biases and limited behavioral generalization. Recent Data Augmentation (DA) methods leverage generative models to enrich offline data, yet they mainly operate within a single rollout paradigm and tend to preserve the original trajectory-level connectivity of the dataset. As a result, such methods often introduce local variations and fail to recover connections between distinct behavior patterns. In this paper, we propose Bidirectional Trajectory Diffusion (BiTrajDiff), a novel DA framework that explicitly addresses this limitation. BiTrajDiff decomposes trajectory synthesis into two independent diffusion processes that generate forward-future and backward-history segments conditioned on shared intermediate anchor states. By stitching the generated segments at these anchors, BiTrajDiff can synthesize trajectories that bridge disconnected behavior patterns and recover global trajectory-level connectivity absent from the original data. Extensive experiments on the D4RL benchmark demonstrate that BiTrajDiff consistently outperforms advanced DA methods across a range of offline RL backbones.

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

### 16. Non-Uniform Noise-to-Signal Ratio in the REINFORCE Policy-Gradient Estimator

Flags: low_evidence_code_confidence, evidence-low

- Subarea: Core RL, offline RL, and policy optimization
- Votes: 7
- ICML URL: https://icml.cc/virtual/2026/poster/64321
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.01460
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Theory / proof
- Contribution types: Theory / proof; Method / algorithm
- Method families: RL / policy optimization
- Evaluation settings: none
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Policy-gradient methods are widely used in reinforcement learning, yet training often becomes unstable or slows down as learning progresses. We study this phenomenon through the noise-to-signal ratio (NSR) of a policy-gradient estimator, defined as the estimator variance (noise) normalized by the squared norm of the true gradient (signal). Our main result is that, for (i) finite-horizon linear systems with Gaussian policies and linear state-feedback, and (ii) finite-horizon polynomial systems with Gaussian policies and polynomial feedback, the NSR of the REINFORCE estimator can be characterized exactly—either in closed form or via numerical moment-evaluation algorithms—without approximation. For general nonlinear dynamics and expressive policies (including neural policies), we further derive a general upper bound on the variance. These characterizations enable a direct examination of how NSR varies across policy parameters and how it evolves along optimization trajectories (e.g. SGD and Adam). Across a range of examples, we find that the NSR landscape is highly non-uniform and typically increases as the policy approaches an optimum; in some regimes it blows up, which can trigger training instability and policy collapse.

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
