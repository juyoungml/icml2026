# C03: Program committee attention Evidence Dossier

This is an abstract/title-based pre-review aid. It does not fill or replace the manual validation fields.

## Claim

Theory and safety/governance receive more program signal than their public-attention signal would predict.

- Strength label: `strong_for_triage`
- Evidence summary: Theory oral enrichment 1.45x vs public enrichment 0.46x; Safety oral enrichment 1.41x and 3 awards vs public enrichment 0.51x.
- Caveat: Oral/award counts are program signals, not full quality labels; award counts are small and volatile.
- Next validation: Review low-public/high-program papers to extract the technical reasons for committee interest.
- Manual review progress: 0/14 rows reviewed; 14 remaining

## Pre-Review Summary

- Bucket mix: likely_supports: 14
- Selection mix: program_high_public_lower: 14
- Area mix: Safety, Governance, Privacy, and Society: 9, Theory, Optimization, and Algorithms: 5

## Adjudication Questions

- Does the abstract directly support the claim, or only share vocabulary with the claim?
- Is the assigned taxonomy area central to the paper, or just one application/context?
- If the paper is high-attention, is the attention driven by a reusable result, a benchmark, a demo, or a social trend?
- If the paper has a GitHub link, is it a real paper artifact and what reproduction claim can be safely made?

## Papers To Read First

- **The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes** (`likely_supports`; Outstanding Paper Honorable Mention, oral, github): Program-selected paper in theory or safety/governance area.
- **To Grok Grokking: Provable Grokking in Ridge Regression** (`likely_supports`; Outstanding Paper Honorable Mention, oral, taxonomy-review): Program-selected paper in theory or safety/governance area.
- **Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit** (`likely_supports`; Outstanding Position Paper Award, oral): Program-selected paper in theory or safety/governance area.
- **Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII)** (`likely_supports`; Outstanding Position Paper Honorable Mention, oral): Program-selected paper in theory or safety/governance area.
- **Equivalence of Context and Parameter Updates in Modern Transformer Blocks** (`likely_supports`; oral, taxonomy-review): Program-selected paper in theory or safety/governance area.
- **Non-Euclidean Gradient Descent Operates at the Edge of Stability** (`likely_supports`; oral): Program-selected paper in theory or safety/governance area.

## Paper-Level Pre-Review

| Rank | Paper | Bucket | Area | Signals | Why It Matters |
| ---: | --- | --- | --- | --- | --- |
| 1 | The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | likely_supports | Safety, Governance, Privacy, and Society | Outstanding Paper Honorable Mention; oral; votes=14; github_stars=13 | Program-selected paper in theory or safety/governance area. |
| 2 | To Grok Grokking: Provable Grokking in Ridge Regression | likely_supports | Theory, Optimization, and Algorithms | Outstanding Paper Honorable Mention; oral; votes=7; taxonomy-review | Program-selected paper in theory or safety/governance area. |
| 3 | Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit | likely_supports | Safety, Governance, Privacy, and Society | Outstanding Position Paper Award; oral; votes=0 | Program-selected paper in theory or safety/governance area. |
| 4 | Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII) | likely_supports | Safety, Governance, Privacy, and Society | Outstanding Position Paper Honorable Mention; oral; votes=0 | Program-selected paper in theory or safety/governance area. |
| 5 | Equivalence of Context and Parameter Updates in Modern Transformer Blocks | likely_supports | Theory, Optimization, and Algorithms | oral; votes=24; taxonomy-review | Program-selected paper in theory or safety/governance area. |
| 6 | Non-Euclidean Gradient Descent Operates at the Edge of Stability | likely_supports | Theory, Optimization, and Algorithms | oral; votes=15 | Program-selected paper in theory or safety/governance area. |
| 7 | Position: Stop Automating Peer Review Without Rigorous Evaluation | likely_supports | Safety, Governance, Privacy, and Society | oral; votes=13 | Program-selected paper in theory or safety/governance area. |
| 8 | Position: Anthropomorphic Misalignment Research Needs Stronger Evidence | likely_supports | Safety, Governance, Privacy, and Society | oral; votes=13 | Program-selected paper in theory or safety/governance area. |
| 9 | Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking | likely_supports | Safety, Governance, Privacy, and Society | oral; votes=9; github_stars=158 | Program-selected paper in theory or safety/governance area. |
| 10 | When the Prompt Becomes Visual: Vision-Centric Jailbreak Attacks for Large Image Editing Models | likely_supports | Safety, Governance, Privacy, and Society | oral; votes=8; github_stars=25 | Program-selected paper in theory or safety/governance area. |
| 11 | Quantifying Frontier LLM Capabilities for Container Sandbox Escape | likely_supports | Safety, Governance, Privacy, and Society | oral; votes=8 | Program-selected paper in theory or safety/governance area. |
| 12 | Optimal Decision-Making Based on Prediction Sets | likely_supports | Theory, Optimization, and Algorithms | oral; votes=6; github_stars=0; taxonomy-review | Program-selected paper in theory or safety/governance area. |
| 13 | Markov Chain Monte Carlo without Evaluating the Target: an Auxiliary Variable Approach | likely_supports | Theory, Optimization, and Algorithms | oral; votes=6 | Program-selected paper in theory or safety/governance area. |
| 14 | Is Your LLM Overcharging You? Tokenization, Transparency, and Incentives | likely_supports | Safety, Governance, Privacy, and Society | oral; votes=6; github_stars=5 | Program-selected paper in theory or safety/governance area. |

## Abstract Excerpts

### 1. The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes

- Bucket: `likely_supports`
- Keyword hits: risk; deception
- URLs: [ICML](https://icml.cc/virtual/2026/poster/60766) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.15515)

Training against white-box deception detectors has been proposed as a way to make AI systems honest. However, such training risks models learning to obfuscate their deception to evade the detector. Prior work has studied obfuscation only in artificial settings where models were directly rewarded for harmful output. We construct a realistic coding environment where reward hacking via hardcoding test cases naturally occurs, and show that obfuscation emerges in this setting. We introduce a taxonomy of possible...

### 2. To Grok Grokking: Provable Grokking in Ridge Regression

- Bucket: `likely_supports`
- Keyword hits: theory
- URLs: [ICML](https://icml.cc/virtual/2026/poster/66206) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.19791)

We study *grokking* - the onset of generalization long after overfitting - in a classical ridge regression setting. We prove end-to-end grokking results for learning over-parameterized linear regression models using gradient descent with weight decay. Specifically, we prove that the following stages occur: (i) the model overfits the training data early during training; (ii) poor generalization persists long after overfitting has manifested; and (iii) the generalization error eventually becomes arbitrarily...

### 3. Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit

- Bucket: `likely_supports`
- Keyword hits: safety; alignment; position; risk
- URLs: [ICML](https://icml.cc/virtual/2026/poster/67118)

This position paper argues that modern alignment methods – originally designed to prevent harmful output – are dual-use technologies that may easily be misused by malicious actors for censorship and manipulation. By mapping current alignment techniques to the possibility and actual cases of misuse, we show that the quest for a ''perfectly aligned'' model inadvertently also provides malicious actors with an ever-improving tool for informational dominance. We need to discuss this dual-use potential *now*, as its...

### 4. Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII)

- Bucket: `likely_supports`
- Keyword hits: theory; safety; position; risk
- URLs: [ICML](https://icml.cc/virtual/2026/poster/67084)

AI-generated non-consensual intimate imagery (AIG-NCII) is not adequately addressed in AI/ML literature regarding AI-generated media, commonly referred to as "deepfakes". While research on deepfakes currently focuses on its epistemic harms—or harms relating to truth and authenticity—this is misaligned with the dominant reality of generative AI abuse involving sexualized imagery. We conduct a landscape analysis of highly-cited works to demonstrate that technical interventions addressing deepfakes almost entirely...

### 5. Equivalence of Context and Parameter Updates in Modern Transformer Blocks

- Bucket: `likely_supports`
- Keyword hits: theory; proof
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63048) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.17864)

Recent research has established that the impact of context in a vanilla transformer can be represented implicitly by forming a token-dependent, rank-1 patch to its MLP weights. This work extends that foundational theory to the diverse architectures of modern Large Language Models. We first demonstrate a precise, analytical solution for a Gemma-style transformer block, proving that the entire effect of a context can be perfectly mapped to rank-1 patches on its MLP weight matrices and a patch to the RMSNorm...

### 6. Non-Euclidean Gradient Descent Operates at the Edge of Stability

- Bucket: `likely_supports`
- Keyword hits: theory
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61486) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.05002)

The Edge of Stability (EoS) is a phenomenon where the sharpness (largest eigenvalue) of the Hessian converges to $2/\eta$ during training with gradient descent (GD) with a step-size $\eta$. Despite violating classical smoothness assumptions, EoS has been widely observed in deep learning, but its theoretical foundations remain incomplete. We propose a framework for analyzing EoS of non-Euclidean GD using directional smoothness (Mishkin et al., 2024), which naturally extends to non-Euclidean norms. This approach...

### 7. Position: Stop Automating Peer Review Without Rigorous Evaluation

- Bucket: `likely_supports`
- Keyword hits: position
- URLs: [ICML](https://icml.cc/virtual/2026/poster/67247) / [AlphaXiv](https://www.alphaxiv.org/abs/2605.03202)

Large language models offer a tempting solution to address the peer review crisis. This position paper argues that **today's AI systems should not be used to produce paper reviews**. We ground this positing in an empirical comparison of human- versus AI-generated ICLR 2026 reviews and an evaluation of the effect of automated paper rewriting on different AI reviewers. We identify two critical issues: 1) AI reviewers exhibit a *hivemind effect* of excessive agreement within and across papers that reduces...

### 8. Position: Anthropomorphic Misalignment Research Needs Stronger Evidence

- Bucket: `likely_supports`
- Keyword hits: safety; alignment; position; risk; deception
- URLs: [ICML](https://icml.cc/virtual/2026/poster/67238) / [AlphaXiv](https://www.alphaxiv.org/abs/2606.07612)

We argue that many Anthropomorphized Misalignment Research (AMR) studies need stronger evidence to ensure that they can provide a robust foundation for critical safety decisions, such as model deployment and regulation. By evaluating failure modes across different misalignment concepts, such as deception, emergent misalignment, and sycophancy, we show how conceptual ambiguity, non-robust datasets and experimental design, and insufficient causal interventions can lead to overinterpretation of model behaviors....

### 9. Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking

- Bucket: `likely_supports`
- Keyword hits: safety; jailbreak
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65657) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.24009)

Jailbreak techniques for large language models (LLMs) evolve faster than benchmarks, making robustness estimates stale and difficult to compare across papers due to drift in datasets, harnesses, and judging protocols. We introduce **JAILBREAK FOUNDRY (JBF)**, a system that addresses this gap via a multi-agent workflow to translate jailbreak papers into executable modules for immediate evaluation within a unified harness. JBF features three core components: (i) *JBF-LIB* for shared contracts and reusable...

### 10. When the Prompt Becomes Visual: Vision-Centric Jailbreak Attacks for Large Image Editing Models

- Bucket: `likely_supports`
- Keyword hits: safety; risk; jailbreak
- URLs: [ICML](https://icml.cc/virtual/2026/poster/60813) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.10179)

Recent advances in large image editing models have shifted the paradigm from text-driven instructions to vision-prompt editing, where user intent is inferred directly from visual inputs such as marks, arrows, and visual–text prompts. While this paradigm greatly expands usability, it also introduces a critical and underexplored safety risk: the attack surface itself becomes visual. In this work, we propose Vision-Centric Jailbreak Attack (VJA), the first visual-to-visual jailbreak attack that conveys malicious...

### 11. Quantifying Frontier LLM Capabilities for Container Sandbox Escape

- Bucket: `likely_supports`
- Keyword hits: safety; risk
- URLs: [ICML](https://icml.cc/virtual/2026/poster/66709) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.02277)

Large Language Models (LLMs) increasingly act as autonomous agents with tool use, ability to execute code, file I/O, and network access. These capabilities create novel security risks. To mitigate these risks, agents are often deployed and evaluated in isolated environments commonly referred to as sandboxes, with Docker or OCI as one of the most popular container runtimes for sandbox implementations. We introduce SandboxEscapeBench, an open benchmark that safely measures an LLM's capacity to break out of these...

### 12. Optimal Decision-Making Based on Prediction Sets

- Bucket: `likely_supports`
- Keyword hits: theory; safety; risk
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63638) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.00989)

Prediction sets can wrap around any ML model to cover unknown test outcomes with a guaranteed probability. Yet, it remains unclear how to use them optimally for downstream decision-making. Here, we propose a decision-theoretic framework that seeks to minimize the expected loss (risk) against a worst-case distribution consistent with the prediction set's coverage guarantee. We first characterize the minimax optimal policy for a fixed prediction set, showing that it balances the worst-case loss inside the set...

### 13. Markov Chain Monte Carlo without Evaluating the Target: an Auxiliary Variable Approach

- Bucket: `likely_supports`
- Keyword hits: theory
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62793) / [AlphaXiv](https://www.alphaxiv.org/abs/2406.05242)

In sampling tasks, it is common for target distributions to be known up to a normalizing constant. However, in many situations, even evaluating the unnormalized distribution can be costly or infeasible. This issue arises in scenarios such as sampling from the Bayesian posterior for tall datasets and the 'doubly-intractable' distributions. In this paper, we begin by observing that seemingly different Markov chain Monte Carlo (MCMC) algorithms, such as the exchange algorithm, PoissonMH, and TunaMH, can be unified...

### 14. Is Your LLM Overcharging You? Tokenization, Transparency, and Incentives

- Bucket: `likely_supports`
- Keyword hits: theory; proof
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63083) / [AlphaXiv](https://www.alphaxiv.org/abs/2505.21627)

State-of-the-art large language models require specialized hardware and substantial energy to operate. Consequently, cloud-based services that provide access to these models have become very popular. In these services, the price users pay depends on the number of tokens a model uses to generate an output–they pay a fixed price per token. In this work, we show that this pricing mechanism creates a financial incentive for providers to strategize and misreport the (number of) tokens a model used to generate an...
