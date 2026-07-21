# Safety, Governance, Privacy, and Society

Manual validation packet for representative and boundary papers.

## Area Context

Headline: Safety and society papers are programmatically central, but vary sharply in executable evidence.

Fault lines:
- Technical safety benchmarks versus position papers about governance, harms, and conference norms.
- Attack/defense papers versus measurement validity and reproducibility of threat models.
- Privacy and unlearning guarantees versus practical utility and auditability.

What to read for:
- Is the harm or threat model operationalized precisely enough to test?
- Can the benchmark, attack, or defense be independently reproduced?
- Does the paper separate empirical evidence from normative argument?

## Queue Summary

- Papers: 16
- Selection mix: fault_line_representative=6, public_attention_not_program_signal=4, program_signal_low_public_attention=4, low_evidence_code_confidence=2
- Papers from taxonomy-review clusters: 0
- Papers with GitHub URLs: 4

## Papers

### 1. The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes

Flags: fault_line_representative, oral, Outstanding Paper Honorable Mention, github

- Subarea: Adversarial safety, attacks, and security
- Votes: 14
- ICML URL: https://icml.cc/virtual/2026/poster/60766
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.15515
- GitHub URL: https://github.com/AlignmentResearch/obfuscation-atlas
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Method / algorithm
- Method families: RL / policy optimization; LLM post-training
- Evaluation settings: language/llm
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: reward

Abstract:

Training against white-box deception detectors has been proposed as a way to make AI systems honest. However, such training risks models learning to obfuscate their deception to evade the detector. Prior work has studied obfuscation only in artificial settings where models were directly rewarded for harmful output. We construct a realistic coding environment where reward hacking via hardcoding test cases naturally occurs, and show that obfuscation emerges in this setting. We introduce a taxonomy of possible outcomes when training against a deception detector. The model either remains honest, or becomes deceptive via two possible obfuscation strategies. (i) *Obfuscated activations*: the model outputs deceptive text while its activations change to no longer trigger the detector. (ii) *Obfuscated policy*: the model produces detector-evading deceptive text, typically by including a justification for the reward hack. Empirically, obfuscated activations arise from representation drift during RL, with or without a detector penalty. The penalty only incentivizes obfuscated policies: we theoretically show this is expected for policy gradient methods. Sufficiently high KL regularization and detector penalty reliably yield honest policies, establishing white-box deception detectors as viable training signals for tasks prone to reward hacking.

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

### 2. Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII)

Flags: fault_line_representative, oral, Outstanding Position Paper Honorable Mention

- Subarea: Position papers, policy, and social impacts
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/67084
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual
- Method families: Agents / tool use
- Evaluation settings: vision/video; security/safety; theory/synthetic
- Result claim cues: negative / limitation; robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

AI-generated non-consensual intimate imagery (AIG-NCII) is not adequately addressed in AI/ML literature regarding AI-generated media, commonly referred to as "deepfakes". While research on deepfakes currently focuses on its epistemic harms—or harms relating to truth and authenticity—this is misaligned with the dominant reality of generative AI abuse involving sexualized imagery. We conduct a landscape analysis of highly-cited works to demonstrate that technical interventions addressing deepfakes almost entirely ignore AIG-NCII, limiting the research ecosystem to authenticity detection tools. In this position paper, we argue that existing interventions address viewer-centric epistemic harms, such as fraud or scams, but ignore subject-centric dignity harms, such as AIG-NCII. We illustrate that knowing an image is synthetic does not mitigate harms to subjects and may, in some cases, even exacerbate them. We conclude by offering recommendations to realign the field, including updating threat models to consider subject-centered harms and addressing AIG-NCII in AI safety research. Finally, we caution that researchers should only engage in this high-risk domain if they implement safety guardrails for both subjects and researchers and establish partnerships with domain experts in sexual violence prevention.

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

### 3. Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit

Flags: fault_line_representative, oral, Outstanding Position Paper Award

- Subarea: Position papers, policy, and social impacts
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/67118
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual
- Method families: LLM post-training; Agents / tool use
- Evaluation settings: robotics/embodied; security/safety
- Result claim cues: robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

This position paper argues that modern alignment methods – originally designed to prevent harmful output – are dual-use technologies that may easily be misused by malicious actors for censorship and manipulation. By mapping current alignment techniques to the possibility and actual cases of misuse, we show that the quest for a ''perfectly aligned'' model inadvertently also provides malicious actors with an ever-improving tool for informational dominance. We need to discuss this dual-use potential *now*, as its risk is exacerbated by rapid user adoption of AI as information provider and a political landscape that increasingly shifts towards authoritarianism. We conclude by urging the community to consider the intentional misuse of safety mechanisms and propose mitigation strategies to safeguard against this dual-use potential.

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

### 4. Position: Anthropomorphic Misalignment Research Needs Stronger Evidence

Flags: fault_line_representative, oral

- Subarea: Position papers, policy, and social impacts
- Votes: 13
- ICML URL: https://icml.cc/virtual/2026/poster/67238
- AlphaXiv URL: https://www.alphaxiv.org/abs/2606.07612
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Dataset / data resource; Method / algorithm
- Method families: LLM post-training; Causal / data-centric
- Evaluation settings: robotics/embodied; security/safety
- Result claim cues: negative / limitation; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

We argue that many Anthropomorphized Misalignment Research (AMR) studies need stronger evidence to ensure that they can provide a robust foundation for critical safety decisions, such as model deployment and regulation. By evaluating failure modes across different misalignment concepts, such as deception, emergent misalignment, and sycophancy, we show how conceptual ambiguity, non-robust datasets and experimental design, and insufficient causal interventions can lead to overinterpretation of model behaviors. This position paper aims to offer guidance on evidentiary considerations that can help improve methodological rigor in AMR. To achieve this, we provide a clear call to action through a proposed framework of evidence levels and a diagnostic checklist. These shared standards will enable more productive scientific discourse and ensure that claims about AI risks rest on solid empirical foundations.

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

### 5. Position: Stop Automating Peer Review Without Rigorous Evaluation

Flags: fault_line_representative, oral, evidence-low

- Subarea: Position papers, policy, and social impacts
- Votes: 13
- ICML URL: https://icml.cc/virtual/2026/poster/67247
- AlphaXiv URL: https://www.alphaxiv.org/abs/2605.03202
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Application / domain study
- Method families: none
- Evaluation settings: language/llm
- Result claim cues: robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Large language models offer a tempting solution to address the peer review crisis. This position paper argues that **today's AI systems should not be used to produce paper reviews**. We ground this positing in an empirical comparison of human- versus AI-generated ICLR 2026 reviews and an evaluation of the effect of automated paper rewriting on different AI reviewers. We identify two critical issues: 1) AI reviewers exhibit a *hivemind effect* of excessive agreement within and across papers that reduces perspective diversity. 2) AI review scores are trivially gameable through *paper laundering*: prompting an LLM to rewrite a paper could significantly increase the scores from AI reviewers, demonstrating that LLM reviewers are easy to game through stylistic changes rather than scientific results. However, non-gameability and review diversity are *necessary but not sufficient* conditions for automation. We argue that **addressing the peer review crisis requires a science of peer review automation**---not general-purpose LLMs deployed without rigorous evaluation.

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

### 6. Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking

Flags: fault_line_representative, oral, github

- Subarea: Adversarial safety, attacks, and security
- Votes: 9
- ICML URL: https://icml.cc/virtual/2026/poster/65657
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.24009
- GitHub URL: https://github.com/OpenSQZ/Jailbreak-Foundry
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Dataset / data resource; System / infrastructure
- Method families: Agents / tool use
- Evaluation settings: math/code/verifiable; language/llm; security/safety
- Result claim cues: scaling / efficiency; robustness / safety
- Benchmarks: AdvBench
- Datasets: none
- Metrics: success_rate

Abstract:

Jailbreak techniques for large language models (LLMs) evolve faster than benchmarks, making robustness estimates stale and difficult to compare across papers due to drift in datasets, harnesses, and judging protocols. We introduce **JAILBREAK FOUNDRY (JBF)**, a system that addresses this gap via a multi-agent workflow to translate jailbreak papers into executable modules for immediate evaluation within a unified harness. JBF features three core components: (i) *JBF-LIB* for shared contracts and reusable utilities; (ii) *JBF-FORGE* for the multi-agent paper-to-module translation; and (iii) *JBF-EVAL* for standardizing evaluations. Across 30 reproduced attacks, JBF achieves high fidelity with a mean (reproduced$-$reported) attack success rate (ASR) deviation of $+0.26$ percentage points. By leveraging shared infrastructure, JBF reduces attack-specific implementation code by nearly half relative to original repositories and achieves an 82.5% mean reused-code ratio. This system enables a standardized AdvBench evaluation of all 30 attacks across 10 victim models using a consistent GPT-4o judge. By automating both attack integration and standardized evaluation, JBF offers a scalable solution for creating living benchmarks that keep pace with the rapidly shifting security landscape.

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

### 7. Chain-of-Thought Reasoning In The Wild Is Not Always Faithful

Flags: public_attention_not_program_signal, github

- Subarea: Position papers, policy, and social impacts
- Votes: 253
- ICML URL: https://icml.cc/virtual/2026/poster/64450
- AlphaXiv URL: https://www.alphaxiv.org/abs/2503.08679
- GitHub URL: https://github.com/jettjaniak/chainscope
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Dataset / data resource
- Contribution types: Dataset / data resource
- Method families: Reasoning / test-time compute; Agents / tool use
- Evaluation settings: math/code/verifiable; security/safety
- Result claim cues: robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Recent studies indicate that when faced with explicit biases in prompts, models often omit mentioning these biases in their Chain-of-Thought (CoT) output, revealing that verbalized reasoning can give an incorrect picture of how models arrive at conclusions (unfaithfulness). In this work, we show that unfaithful CoT also occurs on naturally worded, non-adversarial prompts without adding artificial biases or editing model outputs. We find that when separately presented with the questions "Is X bigger than Y?" and "Is Y bigger than X?", models sometimes produce superficially coherent arguments to justify systematically answering Yes to both questions or No to both questions, despite such responses being logically contradictory. We present preliminary evidence that this is due to models' implicit biases towards Yes or No, labeling this *Implicit Post-Hoc Rationalization*. Our results reveal rates up to 13% for production models, and while frontier models are more faithful, none are entirely so, including thinking models like DeepSeek R1 (0.37%) and Sonnet 3.7 with thinking (0.04%). We also investigate *Unfaithful Illogical Shortcuts*, where models use subtly illogical reasoning to make speculative answers to hard math problems seem rigorously proven. Our findings indicate that while CoT can be useful for assessing outputs, it is not a complete account of a model's internal reasoning and should be used with caution in agentic or safety-critical settings.

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

### 8. The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models

Flags: public_attention_not_program_signal

- Subarea: Adversarial safety, attacks, and security
- Votes: 127
- ICML URL: https://icml.cc/virtual/2026/poster/61446
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.10387
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: LLM post-training
- Evaluation settings: language/llm
- Result claim cues: none
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Large language models can represent a variety of personas but typically default to a helpful Assistant identity cultivated during post-training. Across several different models, we find an “Assistant Axis" in their activation space, which captures the extent to which a model is operating in its default Assistant mode. Steering towards the Assistant direction reinforces helpful and harmless behavior; steering away increases the model’s tendency to identify as other entities. Measuring deviations along the Assistant Axis predicts “persona drift,” a phenomenon where models slip into exhibiting harmful or bizarre behaviors that are uncharacteristic of their typical persona. We find that persona drift is often driven by conversations demanding meta-reflection on the model’s processes or featuring emotionally vulnerable users. We show that restricting activations to a fixed region along the Assistant Axis can stabilize model behavior in these scenarios—and also in the face of adversarial persona-based jailbreaks. Our results suggest that post-training steers models toward a particular region of persona space but only loosely tethers them to it, motivating work on training and steering strategies that more deeply anchor models to a coherent persona.

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

### 9. Reasoning Models Struggle to Control their Chains of Thought

Flags: public_attention_not_program_signal, github

- Subarea: Position papers, policy, and social impacts
- Votes: 75
- ICML URL: https://icml.cc/virtual/2026/poster/66446
- AlphaXiv URL: https://www.alphaxiv.org/abs/2603.05706
- GitHub URL: https://github.com/YuehHanChen/CoTControl
- Artifact confidence: github_url_with_stars
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Method / algorithm
- Method families: RL / policy optimization; Reasoning / test-time compute
- Evaluation settings: robotics/embodied; language/llm; security/safety
- Result claim cues: negative / limitation; robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Instruction following in LLMs captures models' ability to change their visible behaviors as requested by users. Instead, we study models' ability to control their chain-of-thought (CoT). This capability -- CoT controllability -- is undesirable because it could allow models to suppress signs of misbehavior in their CoT, thereby undermining our ability to monitor them. To measure this, we introduce the \emph{CoT-Control} evaluation suite. We show that reasoning models are less able to follow instructions in their CoT than in their outputs: on instructions like reasoning about a genetics problem without mentioning the word ``chromosome", Claude-Sonnet-4.5 complies only 5\% of the time. We also find that CoT controllability is higher for larger models and decreases with more RL training, test-time compute, and increased problem difficulty. CoT controllability failures extend even to situations in which models are given incentives (as opposed to direct requests) to evade CoT monitors, although models that are told they're being monitored exhibit slightly higher controllability. Similarly, eliciting controllability by adversarially optimizing prompts doesn’t meaningfully increase controllability. Our results leave us cautiously optimistic: reasoning models generally seem characterized by low CoT controllability. However, the mechanism behind this phenomenon is not well understood. Given its importance for maintaining CoT monitorability, we recommend that frontier labs keep tracking controllability for future models.

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

### 10. Towards a Science of AI Agent Reliability

Flags: public_attention_not_program_signal

- Subarea: Position papers, policy, and social impacts
- Votes: 72
- ICML URL: https://icml.cc/virtual/2026/poster/66364
- AlphaXiv URL: https://www.alphaxiv.org/abs/2602.16666
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Theory / proof; Application / domain study; Method / algorithm
- Method families: Reasoning / test-time compute; Agents / tool use
- Evaluation settings: security/safety
- Result claim cues: negative / limitation; robustness / safety; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: accuracy

Abstract:

AI agents are increasingly deployed for consequential tasks. Yet existing benchmarks evaluate only task success rates, ignoring whether agents behave consistently, remain robust to perturbations, fail predictably, or bound error severity. We propose a framework for measuring agent reliability grounded in safety-critical engineering practice, decomposing reliability into four dimensions: consistency, robustness, predictability, and safety. Applying these metrics to 12 frontier models across two complementary benchmarks, we find that recent capability gains have produced minimal improvement in reliability: agents remain inconsistent across runs, brittle to prompt rephrasings, and poorly calibrated in their self-assessments, even as accuracy improves. Our metrics complement accuracy-focused evaluation by offering tools for reasoning about how agents perform, degrade, and fail under uncertainty.

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

### 11. Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models

Flags: program_signal_low_public_attention, oral

- Subarea: Adversarial safety, attacks, and security
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/64633
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Benchmark / evaluation
- Contribution types: Benchmark / evaluation; Method / algorithm
- Method families: LLM post-training; Transformer / attention; Causal / data-centric
- Evaluation settings: language/llm; security/safety
- Result claim cues: robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Jailbreak attacks bypass LLM safety alignment, yet their mechanisms remain poorly understood. We provide evidence that attacks do not eliminate safety features but selectively suppress specific attention heads. We identify two functionally differentiated types: **Adversarially Compromised Heads (ACHs)** concentrated in early layers, which are suppressed under attacks; and **Safety-Aligned Heads (SAHs)** in mid-layers, which maintain robust activations even when attacks succeed. Ablation studies support their causal roles: suppressing a small number of ACHs is sufficient to induce jailbreak-like behavior on normally refused inputs, while removing SAHs substantially weakens mid-layer safety activations. Token-level attribution further shows that ACH suppression is driven specifically by attack-template tokens. This provides a mechanistic account of why attacks bypass refusal decisions through ACH suppression, yet may not fully eliminate the internal safety signals sustained by SAHs---a phenomenon we term **Robust Harmful Features**. To validate the practical significance of this robustness, we show that simply reading these persistent activations---without any training---yields a detection signal competitive with dedicated safety models on most benchmarks.

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

### 12. Position: AI Should Facilitate Democratic Deliberation at Scale

Flags: program_signal_low_public_attention, oral

- Subarea: Position papers, policy, and social impacts
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/67203
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Method / algorithm
- Method families: LLM post-training
- Evaluation settings: security/safety
- Result claim cues: scaling / efficiency; robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

AI systems can strengthen democracy by supporting deliberation at scale by addressing cognitive, social, platform-design, and market-driven frictions, while preserving human agency. Unlike proposals such as liquid democracy that restructure representation through vote delegation, in this position paper, we argue that AI-assisted deliberation offers a more promising path by lowering barriers to meaningful engagement without substituting machine judgment for human choice. Drawing on evidence from online platforms and experimental research, we identify four guiding principles: preserving agency and autonomy, encouraging mutual respect, promoting equality and inclusiveness, and augmenting rather than substituting active citizenship. We also address critical challenges, including alignment, sycophancy, training bias, and over-reliance on AI systems. We call on the machine learning community to develop deliberation-focused AI systems evaluated not on engagement metrics but on their capacity to facilitate informed, representative, and friction-robust discourse.

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

### 13. Position: Don't Just "Fix it in Post'': A Science of AI Must Study Learning Dynamics

Flags: program_signal_low_public_attention, oral, evidence-low

- Subarea: Position papers, policy, and social impacts
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/67142
- AlphaXiv URL: none
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual; Theory / proof; Application / domain study; Method / algorithm
- Method families: none
- Evaluation settings: language/llm; security/safety
- Result claim cues: scaling / efficiency; robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

What would it mean to have a *scientific* understanding of AI? Language models are not static objects—they are snapshots of time-evolving processes shaped by data, objectives, and optimization dynamics. Yet the field predominantly treats models as fixed artifacts, analyzing behaviors after training rather than asking *why* they emerge. **This position paper argues that AI research should move beyond *post hoc* fixes and study the learning dynamics of models.** We envision a hierarchy of scientific maturity: first *predict* outcomes from early training signals, then *intervene* when trajectories go wrong, ultimately *design* training procedures that guarantee desired properties. Scaling laws have reached the first level for loss; the challenge is extending all three levels to general capabilities, biases, and safety. We articulate requirements for such theories, survey progress across mechanistic interpretability, fairness, memorization, and learning dynamics, and identify concrete open problems. The path forward requires treating models as processes to be understood, not just artifacts to be patched.

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

### 14. Position: The AI Imperative: Scaling High-Quality Peer Review in Machine Learning

Flags: program_signal_low_public_attention, oral

- Subarea: Position papers, policy, and social impacts
- Votes: 0
- ICML URL: https://icml.cc/virtual/2026/poster/67249
- AlphaXiv URL: https://www.alphaxiv.org/abs/2506.08134
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual
- Method families: Reasoning / test-time compute
- Evaluation settings: language/llm
- Result claim cues: scaling / efficiency; state-of-the-art / improvement
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

Peer review, the bedrock of scientific advancement in machine learning (ML), is strained by a crisis of scale. Exponential growth in manuscript submissions to premier ML venues such as NeurIPS, ICML, and ICLR is outpacing the finite capacity of qualified reviewers, leading to concerns about review quality, consistency, and reviewer fatigue. This position paper argues that AI-assisted peer review must become an urgent research and infrastructure priority. We advocate for a comprehensive AI-augmented ecosystem, leveraging Large Language Models (LLMs) not as replacements for human judgment, but as sophisticated collaborators for authors, reviewers, and Area Chairs (ACs). We propose specific roles for AI in enhancing factual verification, guiding reviewer performance, assisting authors in quality improvement, and supporting ACs in decision-making. Crucially, we contend that the development of such systems hinges on access to more granular, structured, and ethically-sourced peer review process data. We outline a research agenda, including illustrative experiments, to develop and validate these AI assistants, and discuss significant technical and ethical challenges. We call upon the ML community to proactively build this AI-assisted future, ensuring the continued integrity and scalability of scientific validation, while maintaining high standards of peer review.

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

### 15. Who’s in Charge? Disempowerment Patterns in Real-World LLM Usage

Flags: low_evidence_code_confidence, evidence-low

- Subarea: Position papers, policy, and social impacts
- Votes: 52
- ICML URL: https://icml.cc/virtual/2026/poster/62751
- AlphaXiv URL: https://www.alphaxiv.org/abs/2601.19062
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Method / algorithm
- Contribution types: Method / algorithm
- Method families: none
- Evaluation settings: language/llm; security/safety
- Result claim cues: negative / limitation; scaling / efficiency; robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

We present the first large-scale empirical analysis of disempowerment patterns in real-world AI assistant interactions, analyzing 1.5 million consumer Claude.ai conversations using a privacy-preserving approach. We focus on situational dis-empowerment potential, which occurs when AI assistant interactions risk leading users to form distorted perceptions of reality, make inauthentic value judgments, or act in ways misaligned with their values. Quantitatively, we find that severe forms of disempowerment potential occur in fewer than one in a thousand conversations, though rates are substantially higher in personal domains like relationships and lifestyle. Qualitatively, we uncover several concerning patterns, such as validation of persecution narratives and grandiose identities with emphatic sycophantic language, definitive moral judgments about third parties, and complete scripting of value-laden personal communications that users appear to implement verbatim. Analysis of historical trends reveals an increase in the prevalence of disempowerment potential over time. We also find that interactions with greater disempowerment potential receive higher user approval ratings, possibly suggesting a tension between short-term user preferences and long-term human empowerment.

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

### 16. Position: Adversarial ML for LLMs Is Not Making Any Progress

Flags: low_evidence_code_confidence, evidence-low

- Subarea: Adversarial safety, attacks, and security
- Votes: 34
- ICML URL: https://icml.cc/virtual/2026/poster/67187
- AlphaXiv URL: https://www.alphaxiv.org/abs/2502.02260
- GitHub URL: none
- Artifact confidence: no_github_url
- Cluster review: stable_seed; none

Heuristic evidence codes:
- Primary contribution: Position / conceptual
- Contribution types: Position / conceptual
- Method families: none
- Evaluation settings: language/llm
- Result claim cues: negative / limitation; robustness / safety
- Benchmarks: none
- Datasets: none
- Metrics: none

Abstract:

In the past decade, considerable research effort has been devoted to securing machine learning (ML) models that operate in adversarial settings. Yet, progress has been slow even for simple "toy" problems (e.g., robustness to small adversarial perturbations) and is often hindered by non-rigorous evaluations. Today, adversarial ML research has shifted towards studying larger, general-purpose language models. In this position paper, we argue that the situation is now even worse: in the era of LLMs, the field of adversarial ML studies problems that are (1) less clearly defined, (2) harder to solve, and (3) even more challenging to evaluate. As a result, we caution that yet another decade of work on adversarial ML may be failing to produce meaningful progress.

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
