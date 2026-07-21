# C03: Program committee attention

Review question: Why do theory and safety/governance receive stronger program signal than public attention?

## Queue Summary

- Papers: 14
- Selection mix: program_high_public_lower=14
- Oral/award papers: 14
- Taxonomy-review papers: 3
- GitHub-linked papers: 5

## Papers

### 1. The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes

Flags: program_high_public_lower, oral, Outstanding Paper Honorable Mention, github

- Review focus: Identify the technical reason for high program signal and whether public attention misses it.
- Area/subarea: Safety, Governance, Privacy, and Society / Adversarial safety, attacks, and security
- Cluster: 12 - safety / attacks / attack / social aspects
- Cluster review: stable_seed; none
- Program/public: oral=true; award=Outstanding Paper Honorable Mention; votes=14; 7d visits=71
- Artifact: https://github.com/AlignmentResearch/obfuscation-atlas; stars=13; manual-check=none
- Evidence tags: contribution=Position / conceptual; methods=RL / policy optimization; LLM post-training; eval=language/llm
- Benchmark/data/metric cues: none / none / reward
- ICML URL: https://icml.cc/virtual/2026/poster/60766
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.15515

Abstract:

Training against white-box deception detectors has been proposed as a way to make AI systems honest. However, such training risks models learning to obfuscate their deception to evade the detector. Prior work has studied obfuscation only in artificial settings where models were directly rewarded for harmful output. We construct a realistic coding environment where reward hacking via hardcoding test cases naturally occurs, and show that obfuscation emerges in this setting. We introduce a taxonomy of possible outcomes when training against a deception detector. The model either remains honest, or becomes deceptive via two possible obfuscation strategies. (i) *Obfuscated activations*: the model outputs deceptive text while its activations change to no longer trigger the detector. (ii) *Obfuscated policy*: the model produces detector-evading deceptive text, typically by including a justification for the reward hack. Empirically, obfuscated activations arise from representation drift during RL, with or without a detector penalty. The penalty only incentivizes obfuscated policies: we theoretically show this is expected for policy gradient methods. Sufficiently high KL regularization and detector penalty reliably yield honest policies, establishing white-box deception detectors as viable training signals for tasks prone to reward hacking.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 2. To Grok Grokking: Provable Grokking in Ridge Regression

Flags: program_high_public_lower, oral, Outstanding Paper Honorable Mention, taxonomy-review

- Review focus: Identify the technical reason for high program signal and whether public attention misses it.
- Area/subarea: Theory, Optimization, and Algorithms / Statistical learning theory and regression
- Cluster: 7 - theory / regression / bounds / risk
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=true; award=Outstanding Paper Honorable Mention; votes=7; 7d visits=105
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Theory / proof; methods=none; eval=theory/synthetic
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/66206
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.19791

Abstract:

We study *grokking* - the onset of generalization long after overfitting - in a classical ridge regression setting. We prove end-to-end grokking results for learning over-parameterized linear regression models using gradient descent with weight decay. Specifically, we prove that the following stages occur: (i) the model overfits the training data early during training; (ii) poor generalization persists long after overfitting has manifested; and (iii) the generalization error eventually becomes arbitrarily small. Moreover, we show, both theoretically and empirically, that grokking can be amplified or eliminated in a principled manner through proper hyperparameter tuning. To the best of our knowledge, these are the first rigorous quantitative bounds on the generalization delay (which we refer to as the "grokking time") in terms of training hyperparameters. Lastly, going beyond the linear setting, we empirically demonstrate that our quantitative bounds also capture the behavior of grokking on non-linear neural networks. Our results suggest that grokking is not an inherent failure mode of deep learning, but rather a consequence of specific training conditions, and thus does not require fundamental changes to the model architecture or learning algorithm to avoid.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 3. Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit

Flags: program_high_public_lower, oral, Outstanding Position Paper Award

- Review focus: Identify the technical reason for high program signal and whether public attention misses it.
- Area/subarea: Safety, Governance, Privacy, and Society / Position papers, policy, and social impacts
- Cluster: 37 - ai / position / social / position paper
- Cluster review: stable_seed; none
- Program/public: oral=true; award=Outstanding Position Paper Award; votes=0; 7d visits=0
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Position / conceptual; methods=LLM post-training; Agents / tool use; eval=robotics/embodied; security/safety
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/67118
- AlphaXiv URL: none

Abstract:

This position paper argues that modern alignment methods – originally designed to prevent harmful output – are dual-use technologies that may easily be misused by malicious actors for censorship and manipulation. By mapping current alignment techniques to the possibility and actual cases of misuse, we show that the quest for a ''perfectly aligned'' model inadvertently also provides malicious actors with an ever-improving tool for informational dominance. We need to discuss this dual-use potential *now*, as its risk is exacerbated by rapid user adoption of AI as information provider and a political landscape that increasingly shifts towards authoritarianism. We conclude by urging the community to consider the intentional misuse of safety mechanisms and propose mitigation strategies to safeguard against this dual-use potential.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 4. Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII)

Flags: program_high_public_lower, oral, Outstanding Position Paper Honorable Mention

- Review focus: Identify the technical reason for high program signal and whether public attention misses it.
- Area/subarea: Safety, Governance, Privacy, and Society / Position papers, policy, and social impacts
- Cluster: 37 - ai / position / social / position paper
- Cluster review: stable_seed; none
- Program/public: oral=true; award=Outstanding Position Paper Honorable Mention; votes=0; 7d visits=0
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Position / conceptual; methods=Agents / tool use; eval=vision/video; security/safety; theory/synthetic
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/67084
- AlphaXiv URL: none

Abstract:

AI-generated non-consensual intimate imagery (AIG-NCII) is not adequately addressed in AI/ML literature regarding AI-generated media, commonly referred to as "deepfakes". While research on deepfakes currently focuses on its epistemic harms—or harms relating to truth and authenticity—this is misaligned with the dominant reality of generative AI abuse involving sexualized imagery. We conduct a landscape analysis of highly-cited works to demonstrate that technical interventions addressing deepfakes almost entirely ignore AIG-NCII, limiting the research ecosystem to authenticity detection tools. In this position paper, we argue that existing interventions address viewer-centric epistemic harms, such as fraud or scams, but ignore subject-centric dignity harms, such as AIG-NCII. We illustrate that knowing an image is synthetic does not mitigate harms to subjects and may, in some cases, even exacerbate them. We conclude by offering recommendations to realign the field, including updating threat models to consider subject-centered harms and addressing AIG-NCII in AI safety research. Finally, we caution that researchers should only engage in this high-risk domain if they implement safety guardrails for both subjects and researchers and establish partnerships with domain experts in sexual violence prevention.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 5. Equivalence of Context and Parameter Updates in Modern Transformer Blocks

Flags: program_high_public_lower, oral, taxonomy-review

- Review focus: Identify the technical reason for high program signal and whether public attention misses it.
- Area/subarea: Theory, Optimization, and Algorithms / Transformer theory and attention expressivity
- Cluster: 20 - transformers / attention / transformer / softmax
- Cluster review: needs_review; manual confidence not high
- Program/public: oral=true; award=none; votes=24; 7d visits=10
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Theory / proof; methods=Transformer / attention; eval=language/llm; theory/synthetic
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/63048
- AlphaXiv URL: https://www.alphaxiv.org/abs/2511.17864

Abstract:

Recent research has established that the impact of context in a vanilla transformer can be represented implicitly by forming a token-dependent, rank-1 patch to its MLP weights. This work extends that foundational theory to the diverse architectures of modern Large Language Models. We first demonstrate a precise, analytical solution for a Gemma-style transformer block, proving that the entire effect of a context can be perfectly mapped to rank-1 patches on its MLP weight matrices and a patch to the RMSNorm scale. We then generalize this result, providing a constructive proof and algorithm for multi-layer models. To unify these findings, we introduce a general framework centered on two core properties: input controllability and output controllability. We prove that a perfect implicit weight patch is possible for any MLP block where the inner function is input-controllable and the outer function is output-controllable. This provides a simpler and more powerful lens for understanding how transformer models transmute prompts into effective weights. This setup generalizes to a wide range of modern LLM architectures including gating, pre-/post-norm, mixture of experts and sequential/parallel transformer blocks.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 6. Non-Euclidean Gradient Descent Operates at the Edge of Stability

Flags: program_high_public_lower, oral

- Review focus: Identify the technical reason for high program signal and whether public attention misses it.
- Area/subarea: Theory, Optimization, and Algorithms / Convex, stochastic, and nonconvex optimization
- Cluster: 28 - convergence / optimization / stochastic / convex
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=15; 7d visits=6
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Method / algorithm; methods=Graphs / geometry; eval=theory/synthetic
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/61486
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.05002

Abstract:

The Edge of Stability (EoS) is a phenomenon where the sharpness (largest eigenvalue) of the Hessian converges to $2/\eta$ during training with gradient descent (GD) with a step-size $\eta$. Despite violating classical smoothness assumptions, EoS has been widely observed in deep learning, but its theoretical foundations remain incomplete. We propose a framework for analyzing EoS of non-Euclidean GD using directional smoothness (Mishkin et al., 2024), which naturally extends to non-Euclidean norms. This approach allows us to characterize EoS beyond the standard Euclidean setting, encompassing methods such as $\ell_{\infty}$-descent, Block CD, Spectral GD, and Muon without momentum. We derive the appropriate measure of the generalized sharpness under an arbitrary norm. Our generalized sharpness measure includes previously studied vanilla GD and preconditioned GD as special cases. Through analytical results and experiments on neural networks, we show that non-Euclidean GD also exhibits progressive sharpening followed by oscillations around the threshold $2/\eta$. Practically, our framework provides a single, geometry-aware spectral measure that works across optimizers, bridging the gap between empirical observations and deep learning theory.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 7. Position: Stop Automating Peer Review Without Rigorous Evaluation

Flags: program_high_public_lower, oral

- Review focus: Identify the technical reason for high program signal and whether public attention misses it.
- Area/subarea: Safety, Governance, Privacy, and Society / Position papers, policy, and social impacts
- Cluster: 37 - ai / position / social / position paper
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=13; 7d visits=7
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Position / conceptual; methods=none; eval=language/llm
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/67247
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.03202

Abstract:

Large language models offer a tempting solution to address the peer review crisis. This position paper argues that **today's AI systems should not be used to produce paper reviews**. We ground this positing in an empirical comparison of human- versus AI-generated ICLR 2026 reviews and an evaluation of the effect of automated paper rewriting on different AI reviewers. We identify two critical issues: 1) AI reviewers exhibit a *hivemind effect* of excessive agreement within and across papers that reduces perspective diversity. 2) AI review scores are trivially gameable through *paper laundering*: prompting an LLM to rewrite a paper could significantly increase the scores from AI reviewers, demonstrating that LLM reviewers are easy to game through stylistic changes rather than scientific results. However, non-gameability and review diversity are *necessary but not sufficient* conditions for automation. We argue that **addressing the peer review crisis requires a science of peer review automation**---not general-purpose LLMs deployed without rigorous evaluation.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 8. Position: Anthropomorphic Misalignment Research Needs Stronger Evidence

Flags: program_high_public_lower, oral

- Review focus: Identify the technical reason for high program signal and whether public attention misses it.
- Area/subarea: Safety, Governance, Privacy, and Society / Position papers, policy, and social impacts
- Cluster: 37 - ai / position / social / position paper
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=13; 7d visits=9
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Position / conceptual; methods=LLM post-training; Causal / data-centric; eval=robotics/embodied; security/safety
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/67238
- AlphaXiv URL: https://www.alphaxiv.org/abs/2606.07612

Abstract:

We argue that many Anthropomorphized Misalignment Research (AMR) studies need stronger evidence to ensure that they can provide a robust foundation for critical safety decisions, such as model deployment and regulation. By evaluating failure modes across different misalignment concepts, such as deception, emergent misalignment, and sycophancy, we show how conceptual ambiguity, non-robust datasets and experimental design, and insufficient causal interventions can lead to overinterpretation of model behaviors. This position paper aims to offer guidance on evidentiary considerations that can help improve methodological rigor in AMR. To achieve this, we provide a clear call to action through a proposed framework of evidence levels and a diagnostic checklist. These shared standards will enable more productive scientific discourse and ensure that claims about AI risks rest on solid empirical foundations.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 9. Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking

Flags: program_high_public_lower, oral, github

- Review focus: Identify the technical reason for high program signal and whether public attention misses it.
- Area/subarea: Safety, Governance, Privacy, and Society / Adversarial safety, attacks, and security
- Cluster: 12 - safety / attacks / attack / social aspects
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=9; 7d visits=8
- Artifact: https://github.com/OpenSQZ/Jailbreak-Foundry; stars=158; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=Agents / tool use; eval=math/code/verifiable; language/llm; security/safety
- Benchmark/data/metric cues: AdvBench / none / success_rate
- ICML URL: https://icml.cc/virtual/2026/poster/65657
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.24009

Abstract:

Jailbreak techniques for large language models (LLMs) evolve faster than benchmarks, making robustness estimates stale and difficult to compare across papers due to drift in datasets, harnesses, and judging protocols. We introduce **JAILBREAK FOUNDRY (JBF)**, a system that addresses this gap via a multi-agent workflow to translate jailbreak papers into executable modules for immediate evaluation within a unified harness. JBF features three core components: (i) *JBF-LIB* for shared contracts and reusable utilities; (ii) *JBF-FORGE* for the multi-agent paper-to-module translation; and (iii) *JBF-EVAL* for standardizing evaluations. Across 30 reproduced attacks, JBF achieves high fidelity with a mean (reproduced$-$reported) attack success rate (ASR) deviation of $+0.26$ percentage points. By leveraging shared infrastructure, JBF reduces attack-specific implementation code by nearly half relative to original repositories and achieves an 82.5% mean reused-code ratio. This system enables a standardized AdvBench evaluation of all 30 attacks across 10 victim models using a consistent GPT-4o judge. By automating both attack integration and standardized evaluation, JBF offers a scalable solution for creating living benchmarks that keep pace with the rapidly shifting security landscape.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 10. When the Prompt Becomes Visual: Vision-Centric Jailbreak Attacks for Large Image Editing Models

Flags: program_high_public_lower, oral, github

- Review focus: Identify the technical reason for high program signal and whether public attention misses it.
- Area/subarea: Safety, Governance, Privacy, and Society / Adversarial safety, attacks, and security
- Cluster: 12 - safety / attacks / attack / social aspects
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=8; 7d visits=7
- Artifact: https://github.com/CSU-JPG/VJA; stars=25; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=Reasoning / test-time compute; eval=vision/video; language/llm; security/safety
- Benchmark/data/metric cues: IESBench / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/60813
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.10179

Abstract:

Recent advances in large image editing models have shifted the paradigm from text-driven instructions to vision-prompt editing, where user intent is inferred directly from visual inputs such as marks, arrows, and visual–text prompts. While this paradigm greatly expands usability, it also introduces a critical and underexplored safety risk: the attack surface itself becomes visual. In this work, we propose Vision-Centric Jailbreak Attack (VJA), the first visual-to-visual jailbreak attack that conveys malicious instructions purely through visual inputs. To systematically study this emerging threat, we introduce IESBench, a safety-oriented benchmark for image editing models. Extensive experiments on IESBench demonstrate that VJA effectively compromises state-of-the-art commercial models, achieving attack success rates of up to 80.9% on Nano Banana Pro and 70.1% on GPT-Image-1.5. To mitigate this vulnerability, we propose a training-free defense based on introspective multimodal reasoning, which substantially improves the safety of poorly aligned models to a level comparable with commercial systems, without auxiliary guard models and with negligible computational overhead. Our findings expose new vulnerabilities, provide both a benchmark and practical defense to advance safe and trustworthy modern image editing systems.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 11. Quantifying Frontier LLM Capabilities for Container Sandbox Escape

Flags: program_high_public_lower, oral

- Review focus: Identify the technical reason for high program signal and whether public attention misses it.
- Area/subarea: Safety, Governance, Privacy, and Society / Adversarial safety, attacks, and security
- Cluster: 12 - safety / attacks / attack / social aspects
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=8; 7d visits=7
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=Agents / tool use; eval=math/code/verifiable; language/llm; security/safety
- Benchmark/data/metric cues: SandboxEscapeBench / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/66709
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.02277

Abstract:

Large Language Models (LLMs) increasingly act as autonomous agents with tool use, ability to execute code, file I/O, and network access. These capabilities create novel security risks. To mitigate these risks, agents are often deployed and evaluated in isolated environments commonly referred to as sandboxes, with Docker or OCI as one of the most popular container runtimes for sandbox implementations. We introduce SandboxEscapeBench, an open benchmark that safely measures an LLM's capacity to break out of these sandboxes. The benchmark is implemented as an \texttt{Inspect AI} Capture the Flag (CTF) evaluation utilising a nested sandbox architecture with the outer layer containing the flag and no known vulnerabilities. Following a threat model of a motivated adversarial agent with shell access inside a container, \bench covers a spectrum of sandbox-escape mechanisms spanning misconfiguration, privilege allocation mistakes, kernel flaws, and runtime/orchestration weaknesses. We find that, when vulnerabilities are added, LLMs are able to identify and exploit them, showing that use of evaluation like \bench is needed to ensure sandboxing continues to provide the encapsulation needed for highly-capable models.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 12. Optimal Decision-Making Based on Prediction Sets

Flags: program_high_public_lower, oral, taxonomy-review, github

- Review focus: Identify the technical reason for high program signal and whether public attention misses it.
- Area/subarea: Theory, Optimization, and Algorithms / Statistical learning theory and regression
- Cluster: 7 - theory / regression / bounds / risk
- Cluster review: needs_review; split across lexical clusters
- Program/public: oral=true; award=none; votes=6; 7d visits=4
- Artifact: https://github.com/salma123456789123456789-dotcom/Pneumonia-Detection-using-Chest-X-Ray-images; stars=0; manual-check=none
- Evidence tags: contribution=Theory / proof; methods=RL / policy optimization; Bayesian / probabilistic; eval=science/domain; security/safety; theory/synthetic
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/63638
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.00989

Abstract:

Prediction sets can wrap around any ML model to cover unknown test outcomes with a guaranteed probability. Yet, it remains unclear how to use them optimally for downstream decision-making. Here, we propose a decision-theoretic framework that seeks to minimize the expected loss (risk) against a worst-case distribution consistent with the prediction set's coverage guarantee. We first characterize the minimax optimal policy for a fixed prediction set, showing that it balances the worst-case loss inside the set with a penalty for potential losses outside the set. Building on this, we derive the optimal prediction set construction that minimizes the resulting robust risk subject to a coverage constraint. Finally, we introduce Risk-Optimal Conformal Prediction (ROCP), a practical algorithm that targets these risk-minimizing sets while maintaining finite-sample distribution-free marginal coverage. Empirical evaluations on medical diagnosis and safety-critical decision-making tasks demonstrate that ROCP reduces critical mistakes compared to baselines, particularly when out-of-set errors are costly.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 13. Markov Chain Monte Carlo without Evaluating the Target: an Auxiliary Variable Approach

Flags: program_high_public_lower, oral

- Review focus: Identify the technical reason for high program signal and whether public attention misses it.
- Area/subarea: Theory, Optimization, and Algorithms / Bayesian and probabilistic methods
- Cluster: 32 - bayesian / probabilistic / posterior / probabilistic methods
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=6; 7d visits=7
- Artifact: none; stars=0; manual-check=none
- Evidence tags: contribution=Dataset / data resource; methods=Diffusion / flow; Bayesian / probabilistic; eval=theory/synthetic
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/62793
- AlphaXiv URL: https://www.alphaxiv.org/abs/2406.05242

Abstract:

In sampling tasks, it is common for target distributions to be known up to a normalizing constant. However, in many situations, even evaluating the unnormalized distribution can be costly or infeasible. This issue arises in scenarios such as sampling from the Bayesian posterior for tall datasets and the 'doubly-intractable' distributions. In this paper, we begin by observing that seemingly different Markov chain Monte Carlo (MCMC) algorithms, such as the exchange algorithm, PoissonMH, and TunaMH, can be unified under a simple common procedure. We then extend this procedure into a novel framework that allows the use of auxiliary variables in both the proposal and the acceptance--rejection step. Several new MCMC algorithms emerge from this framework that uses estimated gradients to guide the proposal moves. They have demonstrated significantly better performance than existing methods on both synthetic and real datasets. We also develop theory for the new framework and use it to simplify and extend results for existing algorithms.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:

### 14. Is Your LLM Overcharging You? Tokenization, Transparency, and Incentives

Flags: program_high_public_lower, oral, github

- Review focus: Identify the technical reason for high program signal and whether public attention misses it.
- Area/subarea: Safety, Governance, Privacy, and Society / Privacy, differential privacy, and unlearning
- Cluster: 23 - privacy / private / dp / aspects privacy
- Cluster review: stable_seed; none
- Program/public: oral=true; award=none; votes=6; 7d visits=3
- Artifact: https://github.com/Networks-Learning/token-pricing; stars=5; manual-check=none
- Evidence tags: contribution=Benchmark / evaluation; methods=none; eval=language/llm; theory/synthetic
- Benchmark/data/metric cues: none / none / none
- ICML URL: https://icml.cc/virtual/2026/poster/63083
- AlphaXiv URL: https://www.alphaxiv.org/abs/2505.21627

Abstract:

State-of-the-art large language models require specialized hardware and substantial energy to operate. Consequently, cloud-based services that provide access to these models have become very popular. In these services, the price users pay depends on the number of tokens a model uses to generate an output–they pay a fixed price per token. In this work, we show that this pricing mechanism creates a financial incentive for providers to strategize and misreport the (number of) tokens a model used to generate an output, and users cannot prove, or even know, whether a provider is overcharging them. However, we also show that, if an unfaithful provider is obliged to be transparent about the generative process used by the model, misreporting optimally without raising suspicion is hard. Nevertheless, as a proof-of-concept, we develop an efficient heuristic algorithm that allows providers to significantly overcharge users without raising suspicion. Crucially, the cost of running the algorithm is lower than the additional revenue from overcharging users, highlighting the vulnerability of users under the current pay-per-token pricing mechanism. Further, we show that, to eliminate the financial incentive to strategize, a pricing mechanism must price tokens linearly on their character count. While this makes a provider's profit margin vary across tokens, we introduce a simple prescription that allows a provider to maintain their average profit margin when transitioning to an incentive-compatible pricing mechanism. To complement our theoretical results, we conduct experiments with large language models from the $\texttt{Llama}$, $\texttt{Gemma}$ and $\texttt{Ministral}$ families, and prompts from a popular benchmarking platform.

Manual review:
- [ ] Claim support checked
- [ ] Taxonomy judgment checked
- [ ] Artifact judgment checked, if applicable
- Claim support:
- Taxonomy judgment:
- Artifact judgment:
- Notes:
