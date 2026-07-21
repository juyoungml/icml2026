# ICML 2026 Review Sprint 01

Focused manual-review packet for the top 40 papers in the researcher review plan.
This is a reading worksheet; judgments should be entered in `data/manual/claim_review_overrides.csv` and `data/manual/area_review_overrides.csv`.

## Sprint Snapshot

- Papers: 40
- Papers touching claim overlays: 40
- Papers touching area overlays: 35
- Phase mix: main_thesis_claims: 35, artifact_and_reproducibility: 5

## Execution Checklist

1. Read the paper abstract and, when needed, the ICML/AlphaXiv page.
2. Open the linked claim packet/dossier or area packet/card.
3. Fill the overlay keys listed for that paper in `data/manual/`.
4. Use `manual_notes` for concise evidence, corrections, and caveats.
5. Re-run the progress/readiness pipeline after the sprint.

## Papers

### 1. How much can language models memorize?

- Phase: `main_thesis_claims`
- Area: LLM Reasoning, Post-Training, and RLVR / Diffusion language models and decoding
- Claims: C01; C08
- Why first: in claim-validation queue; supports priority claim(s) C01; in area-validation queue; priority report area; award paper; oral/program signal; taxonomy boundary needs review; artifact-visible; high AlphaXiv attention
- Signals: oral; Outstanding Paper Honorable Mention; votes=271; github_stars=2; taxonomy_review; evidence=medium
- Claim overlay keys: C01::62989 | C08::62989
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::62989
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c01-llm-reasoning-center-of-gravity.md; reports/claim_validation_packets/c08-validation-priority.md
- Claim dossiers: reports/claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md; reports/claim_evidence_dossiers/c08-validation-priority.md
- Area packet: reports/validation_packets/llm-reasoning-post-training-and-rlvr.md
- Area briefing: reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62989) / [AlphaXiv](https://www.alphaxiv.org/abs/2505.24832)

Abstract excerpt:

We propose a new method for estimating how much a model knows about a datapoint and use it to measure the capacity of modern language models. Prior studies of language model memorization have struggled to disentangle memorization from generalization. We formally separate memorization into two components: unintended memorization, the information a model contains about a specific dataset, and generalization, the information a model contains about the true data-generation process. When we completely eliminate generalization, we can compute the total memorization, which provides an estimate of model capacity: our measurements estimate that GPT-style models have a capacity of approximately...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 2. To Grok Grokking: Provable Grokking in Ridge Regression

- Phase: `main_thesis_claims`
- Area: Theory, Optimization, and Algorithms / Statistical learning theory and regression
- Claims: C03; C08
- Why first: in claim-validation queue; supports priority claim(s) C03; in area-validation queue; priority report area; award paper; oral/program signal; taxonomy boundary needs review; low-confidence evidence code
- Signals: oral; Outstanding Paper Honorable Mention; votes=7; taxonomy_review; evidence=low
- Claim overlay keys: C03::66206 | C08::66206
- Area overlay keys: Theory, Optimization, and Algorithms::66206
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c03-program-committee-attention.md; reports/claim_validation_packets/c08-validation-priority.md
- Claim dossiers: reports/claim_evidence_dossiers/c03-program-committee-attention.md; reports/claim_evidence_dossiers/c08-validation-priority.md
- Area packet: reports/validation_packets/theory-optimization-and-algorithms.md
- Area briefing: reports/area_briefing_cards/theory-optimization-and-algorithms.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/66206) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.19791)

Abstract excerpt:

We study *grokking* - the onset of generalization long after overfitting - in a classical ridge regression setting. We prove end-to-end grokking results for learning over-parameterized linear regression models using gradient descent with weight decay. Specifically, we prove that the following stages occur: (i) the model overfits the training data early during training; (ii) poor generalization persists long after overfitting has manifested; and (iii) the generalization error eventually becomes arbitrarily small. Moreover, we show, both theoretically and empirically, that grokking can be amplified or eliminated in a principled manner through proper hyperparameter tuning. To the best of...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 3. The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models

- Phase: `main_thesis_claims`
- Area: LLM Reasoning, Post-Training, and RLVR / Reasoning models and chain-of-thought behavior
- Claims: C01; C08
- Why first: in claim-validation queue; supports priority claim(s) C01; in area-validation queue; priority report area; award paper; oral/program signal; taxonomy boundary needs review; artifact-visible; moderate AlphaXiv attention
- Signals: oral; Outstanding Paper Award; votes=92; github_stars=212; taxonomy_review; evidence=medium
- Claim overlay keys: C01::61998 | C08::61998
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::61998
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c01-llm-reasoning-center-of-gravity.md; reports/claim_validation_packets/c08-validation-priority.md
- Claim dossiers: reports/claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md; reports/claim_evidence_dossiers/c08-validation-priority.md
- Area packet: reports/validation_packets/llm-reasoning-post-training-and-rlvr.md
- Area briefing: reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61998) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.15165)

Abstract excerpt:

Diffusion Large Language Models (dLLMs) break the rigid left-to-right constraint of traditional LLMs, enabling token generation in arbitrary orders. Intuitively, this flexibility implies a solution space that strictly supersets the fixed autoregressive trajectory, theoretically unlocking superior reasoning potential. Indeed, for specific constraint satisfaction tasks (e.g., sudoku puzzles), this capability has proven to be highly advantageous. However, in this paper, we reveal that for general reasoning tasks (e.g., mathematics and coding), arbitrary order generation may in fact limit the reasoning potential of dLLMs. We find that dLLMs tend to exploit this order flexibility to bypass...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 4. Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights

- Phase: `main_thesis_claims`
- Area: Systems and Efficient Foundation Models / Large-scale training, optimizers, and model architecture
- Claims: C02; C06
- Why first: in claim-validation queue; supports priority claim(s) C02; in area-validation queue; priority report area; taxonomy boundary needs review; low-confidence evidence code; artifact-visible; high AlphaXiv attention; public attention without program signal
- Signals: votes=365; github_stars=627; taxonomy_review; evidence=low
- Claim overlay keys: C02::65901 | C06::65901
- Area overlay keys: Systems and Efficient Foundation Models::65901
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md; reports/claim_validation_packets/c06-external-trend-context.md
- Claim dossiers: reports/claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md; reports/claim_evidence_dossiers/c06-external-trend-context.md
- Area packet: reports/validation_packets/systems-and-efficient-foundation-models.md
- Area briefing: reports/area_briefing_cards/systems-and-efficient-foundation-models.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65901) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.12228)

Abstract excerpt:

Pretraining produces a learned parameter vector that is typically treated as a starting point for further iterative adaptation. In this work, we instead view the outcome of pretraining as a distribution over parameter vectors, whose support already contains task-specific experts. We show that in smaller or insufficiently trained models such expert solutions occupy a negligible fraction of the volume of this distribution, making their discovery reliant on structured optimization methods such as gradient descent. In contrast, in large, well-pretrained models the density of task-experts increases dramatically, so that diverse specialists populate a substantial fraction of the neighborhood...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 5. Maximum Likelihood Reinforcement Learning

- Phase: `main_thesis_claims`
- Area: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Claims: C01; C08
- Why first: in claim-validation queue; supports priority claim(s) C01; in area-validation queue; priority report area; oral/program signal; taxonomy boundary needs review; artifact-visible; high AlphaXiv attention
- Signals: oral; votes=259; github_stars=194; taxonomy_review; evidence=medium
- Claim overlay keys: C01::65332 | C08::65332
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::65332
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c01-llm-reasoning-center-of-gravity.md; reports/claim_validation_packets/c08-validation-priority.md
- Claim dossiers: reports/claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md; reports/claim_evidence_dossiers/c08-validation-priority.md
- Area packet: reports/validation_packets/llm-reasoning-post-training-and-rlvr.md
- Area briefing: reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65332) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.02710)

Abstract excerpt:

Maximum likelihood is fundamental to supervised learning but it cannot be directly applied in correctness-based problems with non-differentiable sampling. In these settings, reinforcement learning (RL) is typically used to maximize expected reward. We show that for binary correctness tasks, expected-reward RL is a first-order approximation of the maximum likelihood objective, yielding vanishing learning signal on low-success inputs. We introduce **Maximum Likelihood Reinforcement Learning (MaxRL)**, a compute-indexed family of sampling-based objectives derived from a pass@k expansion of the likelihood, which interpolates between standard RL and exact maximum likelihood as compute...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 6. PaperBanana: Automating Academic Illustration for AI Scientists

- Phase: `main_thesis_claims`
- Area: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Claims: C02; C07
- Why first: in claim-validation queue; supports priority claim(s) C02, C07; in area-validation queue; priority report area; artifact-visible; high AlphaXiv attention; public attention without program signal
- Signals: votes=420; github_stars=6765; evidence=medium
- Claim overlay keys: C02::65206 | C07::65206
- Area overlay keys: Agents, Code, and Tool Use::65206
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md; reports/claim_validation_packets/c07-artifact-visibility.md
- Claim dossiers: reports/claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md; reports/claim_evidence_dossiers/c07-artifact-visibility.md
- Area packet: reports/validation_packets/agents-code-and-tool-use.md
- Area briefing: reports/area_briefing_cards/agents-code-and-tool-use.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65206) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.23265)

Abstract excerpt:

Despite rapid advances in autonomous AI scientists powered by language models, generating publication-ready illustrations remains a labor-intensive bottleneck in the research workflow. To lift this burden, we introduce PaperBanana, an agentic framework for automated generation of publication-ready academic illustrations. Powered by state-of-the-art VLMs and image generation models, PaperBanana orchestrates specialized agents to retrieve references, plan content and style, render images, and iteratively refine via self-critique. To rigorously evaluate our framework, we introduce PaperBananaBench, comprising 292 test cases for methodology diagrams curated from NeurIPS 2025 publications,...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 7. The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes

- Phase: `main_thesis_claims`
- Area: Safety, Governance, Privacy, and Society / Adversarial safety, attacks, and security
- Claims: C03
- Why first: in claim-validation queue; supports priority claim(s) C03; in area-validation queue; priority report area; award paper; oral/program signal; artifact-visible
- Signals: oral; Outstanding Paper Honorable Mention; votes=14; github_stars=13; evidence=medium
- Claim overlay keys: C03::60766
- Area overlay keys: Safety, Governance, Privacy, and Society::60766
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c03-program-committee-attention.md
- Claim dossiers: reports/claim_evidence_dossiers/c03-program-committee-attention.md
- Area packet: reports/validation_packets/safety-governance-privacy-and-society.md
- Area briefing: reports/area_briefing_cards/safety-governance-privacy-and-society.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/60766) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.15515)

Abstract excerpt:

Training against white-box deception detectors has been proposed as a way to make AI systems honest. However, such training risks models learning to obfuscate their deception to evade the detector. Prior work has studied obfuscation only in artificial settings where models were directly rewarded for harmful output. We construct a realistic coding environment where reward hacking via hardcoding test cases naturally occurs, and show that obfuscation emerges in this setting. We introduce a taxonomy of possible outcomes when training against a deception detector. The model either remains honest, or becomes deceptive via two possible obfuscation strategies. (i) *Obfuscated activations*: the...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 8. Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII)

- Phase: `main_thesis_claims`
- Area: Safety, Governance, Privacy, and Society / Position papers, policy, and social impacts
- Claims: C03
- Why first: in claim-validation queue; supports priority claim(s) C03; in area-validation queue; priority report area; award paper; oral/program signal
- Signals: oral; Outstanding Position Paper Honorable Mention; votes=0; evidence=medium
- Claim overlay keys: C03::67084
- Area overlay keys: Safety, Governance, Privacy, and Society::67084
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c03-program-committee-attention.md
- Claim dossiers: reports/claim_evidence_dossiers/c03-program-committee-attention.md
- Area packet: reports/validation_packets/safety-governance-privacy-and-society.md
- Area briefing: reports/area_briefing_cards/safety-governance-privacy-and-society.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/67084)

Abstract excerpt:

AI-generated non-consensual intimate imagery (AIG-NCII) is not adequately addressed in AI/ML literature regarding AI-generated media, commonly referred to as "deepfakes". While research on deepfakes currently focuses on its epistemic harms—or harms relating to truth and authenticity—this is misaligned with the dominant reality of generative AI abuse involving sexualized imagery. We conduct a landscape analysis of highly-cited works to demonstrate that technical interventions addressing deepfakes almost entirely ignore AIG-NCII, limiting the research ecosystem to authenticity detection tools. In this position paper, we argue that existing interventions address viewer-centric epistemic...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 9. Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit

- Phase: `main_thesis_claims`
- Area: Safety, Governance, Privacy, and Society / Position papers, policy, and social impacts
- Claims: C03
- Why first: in claim-validation queue; supports priority claim(s) C03; in area-validation queue; priority report area; award paper; oral/program signal
- Signals: oral; Outstanding Position Paper Award; votes=0; evidence=medium
- Claim overlay keys: C03::67118
- Area overlay keys: Safety, Governance, Privacy, and Society::67118
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c03-program-committee-attention.md
- Claim dossiers: reports/claim_evidence_dossiers/c03-program-committee-attention.md
- Area packet: reports/validation_packets/safety-governance-privacy-and-society.md
- Area briefing: reports/area_briefing_cards/safety-governance-privacy-and-society.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/67118)

Abstract excerpt:

This position paper argues that modern alignment methods – originally designed to prevent harmful output – are dual-use technologies that may easily be misused by malicious actors for censorship and manipulation. By mapping current alignment techniques to the possibility and actual cases of misuse, we show that the quest for a ''perfectly aligned'' model inadvertently also provides malicious actors with an ever-improving tool for informational dominance. We need to discuss this dual-use potential *now*, as its risk is exacerbated by rapid user adoption of AI as information provider and a political landscape that increasingly shifts towards authoritarianism. We conclude by urging the...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 10. Reinforcement Learning with Evolving Rubrics for Deep Research

- Phase: `main_thesis_claims`
- Area: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Claims: C01; C08
- Why first: in claim-validation queue; supports priority claim(s) C01; in area-validation queue; priority report area; oral/program signal; taxonomy boundary needs review; artifact-visible; moderate AlphaXiv attention
- Signals: oral; votes=201; github_stars=682; taxonomy_review; evidence=medium
- Claim overlay keys: C01::65886 | C08::65886
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::65886
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c01-llm-reasoning-center-of-gravity.md; reports/claim_validation_packets/c08-validation-priority.md
- Claim dossiers: reports/claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md; reports/claim_evidence_dossiers/c08-validation-priority.md
- Area packet: reports/validation_packets/llm-reasoning-post-training-and-rlvr.md
- Area briefing: reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65886) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.19399)

Abstract excerpt:

Deep research agents perform multi-step research to produce long-form, well-attributed answers. However, most open deep research agents are trained on easily verifiable short-form QA tasks via reinforcement learning with verifiable rewards, which does not extend to realistic long-form tasks. We address this with **Reinforcement Learning with Evolving Rubrics (RLER)**, where rubrics are constructed and maintained to *co-evolve* with the policy model during training. This allows the rubrics to incorporate newly explored information from search and contrasting model responses, enabling better fact checking and more discriminative on-policy feedback. Using RLER, we develop **Deep Research...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 11. Controlled LLM Training on Spectral Sphere

- Phase: `main_thesis_claims`
- Area: Systems and Efficient Foundation Models / Large-scale training, optimizers, and model architecture
- Claims: C02; C08
- Why first: in claim-validation queue; supports priority claim(s) C02; in area-validation queue; priority report area; oral/program signal; taxonomy boundary needs review; artifact-visible; moderate AlphaXiv attention
- Signals: oral; votes=115; github_stars=130; taxonomy_review; evidence=medium
- Claim overlay keys: C02::66212 | C08::66212
- Area overlay keys: Systems and Efficient Foundation Models::66212
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md; reports/claim_validation_packets/c08-validation-priority.md
- Claim dossiers: reports/claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md; reports/claim_evidence_dossiers/c08-validation-priority.md
- Area packet: reports/validation_packets/systems-and-efficient-foundation-models.md
- Area briefing: reports/area_briefing_cards/systems-and-efficient-foundation-models.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/66212) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.08393)

Abstract excerpt:

Scaling large models requires optimization strategies that ensure rapid convergence grounded in stability. Maximal Update Parametrization ($\boldsymbol{\mu}$P) provides a theoretical safeguard for width-invariant $\Theta(1)$ activation control, whereas emerging optimizers like Muon are only "half-aligned" with these constraints: they control updates but allow weights to drift. To address this limitation, we introduce the **Spectral Sphere Optimizer (SSO)**, which enforces strict module-wise spectral constraints on both weights and their updates. By deriving the steepest descent direction on the spectral sphere, SSO realizes a fully $\boldsymbol{\mu}$P-aligned optimization process. To...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 12. Reinforcement Learning via Self-Distillation

- Phase: `main_thesis_claims`
- Area: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Claims: C01; C06; C08
- Why first: in claim-validation queue; supports priority claim(s) C01; in area-validation queue; priority report area; taxonomy boundary needs review; artifact-visible; high AlphaXiv attention; public attention without program signal
- Signals: votes=718; github_stars=1008; taxonomy_review; evidence=medium
- Claim overlay keys: C01::64121 | C06::64121 | C08::64121
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::64121
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c01-llm-reasoning-center-of-gravity.md; reports/claim_validation_packets/c06-external-trend-context.md; reports/claim_validation_packets/c08-validation-priority.md
- Claim dossiers: reports/claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md; reports/claim_evidence_dossiers/c06-external-trend-context.md; reports/claim_evidence_dossiers/c08-validation-priority.md
- Area packet: reports/validation_packets/llm-reasoning-post-training-and-rlvr.md
- Area briefing: reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64121) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.20802)

Abstract excerpt:

Large language models are increasingly post-trained with reinforcement learning in verifiable domains such as code and math. Yet, current methods for reinforcement learning with verifiable rewards (RLVR) learn only from a scalar outcome reward per attempt, creating a severe credit-assignment bottleneck. Many verifiable environments actually provide rich textual feedback, such as runtime errors or judge evaluations, that explain *why* an attempt failed. We formalize this setting as reinforcement learning with rich feedback and introduce **Self-Distillation Policy Optimization** (**SDPO**), which converts tokenized feedback into a dense learning signal without any external teacher or...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 13. Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers

- Phase: `main_thesis_claims`
- Area: LLM Reasoning, Post-Training, and RLVR / General LLM training, evaluation, and alignment
- Claims: C01
- Why first: in claim-validation queue; supports priority claim(s) C01; in area-validation queue; priority report area; oral/program signal; taxonomy boundary needs review; moderate AlphaXiv attention
- Signals: oral; votes=75; taxonomy_review; evidence=medium
- Claim overlay keys: C01::65446
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::65446
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c01-llm-reasoning-center-of-gravity.md
- Claim dossiers: reports/claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md
- Area packet: reports/validation_packets/llm-reasoning-post-training-and-rlvr.md
- Area briefing: reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65446) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.15674)

Abstract excerpt:

Large language model (LLM) activations are notoriously difficult to understand, with most existing techniques using complex, specialized methods for interpreting them. Recent work has proposed a simpler approach known as LatentQA: training LLMs to directly accept LLM activations as inputs and answer arbitrary questions about them in natural language. However, prior work has focused on narrow task settings for both training and evaluation. In this paper, we instead take a generalist perspective. We evaluate LatentQA-trained models, which we call Activation Oracles (AOs), in far out-of-distribution settings and examine how performance scales with training data diversity. We find that AOs...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 14. GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization

- Phase: `main_thesis_claims`
- Area: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Claims: C01; C06
- Why first: in claim-validation queue; supports priority claim(s) C01; in area-validation queue; priority report area; taxonomy boundary needs review; artifact-visible; high AlphaXiv attention; public attention without program signal
- Signals: votes=507; github_stars=489; taxonomy_review; evidence=medium
- Claim overlay keys: C01::63333 | C06::63333
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::63333
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c01-llm-reasoning-center-of-gravity.md; reports/claim_validation_packets/c06-external-trend-context.md
- Claim dossiers: reports/claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md; reports/claim_evidence_dossiers/c06-external-trend-context.md
- Area packet: reports/validation_packets/llm-reasoning-post-training-and-rlvr.md
- Area briefing: reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63333) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.05242)

Abstract excerpt:

As language models become increasingly capable, users expect them to provide not only accurate responses but also behaviors aligned with diverse human preferences across a variety of scenarios. To achieve this, Reinforcement learning (RL) pipelines have begun incorporating multiple rewards, each capturing a distinct preference, to guide models toward these desired behaviors. However, recent work has defaulted to apply Group Relative Policy Optimization (GRPO) under multi-reward setting without examining its suitability. In this paper, we demonstrate that directly applying GRPO to normalize distinct rollout reward combinations causes them to collapse into identical advantage values,...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 15. mHC: Manifold-Constrained Hyper-Connections

- Phase: `main_thesis_claims`
- Area: Systems and Efficient Foundation Models / Large-scale training, optimizers, and model architecture
- Claims: C02; C06; C08
- Why first: in claim-validation queue; supports priority claim(s) C02; in area-validation queue; priority report area; taxonomy boundary needs review; artifact-visible; high AlphaXiv attention; public attention without program signal
- Signals: votes=696; github_stars=367; taxonomy_review; evidence=medium
- Claim overlay keys: C02::61870 | C06::61870 | C08::61870
- Area overlay keys: Systems and Efficient Foundation Models::61870
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md; reports/claim_validation_packets/c06-external-trend-context.md; reports/claim_validation_packets/c08-validation-priority.md
- Claim dossiers: reports/claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md; reports/claim_evidence_dossiers/c06-external-trend-context.md; reports/claim_evidence_dossiers/c08-validation-priority.md
- Area packet: reports/validation_packets/systems-and-efficient-foundation-models.md
- Area briefing: reports/area_briefing_cards/systems-and-efficient-foundation-models.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61870) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.24880)

Abstract excerpt:

Recently, studies exemplified by Hyper-Connections (HC) have extended the ubiquitous residual connection paradigm established over the past decade by expanding the residual stream width and diversifying connectivity patterns. While yielding substantial performance gains, this diversification fundamentally compromises the identity mapping property intrinsic to the residual connection, which causes severe training instability and restricted scalability, and additionally incurs notable memory access overhead. To address these challenges, we propose Manifold-Constrained Hyper-Connections (mHC), a general framework that projects the residual connection space of HC onto a specific manifold to...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 16. Evolution Strategies at the Hyperscale

- Phase: `main_thesis_claims`
- Area: Systems and Efficient Foundation Models / Large-scale training, optimizers, and model architecture
- Claims: C02; C06
- Why first: in claim-validation queue; supports priority claim(s) C02; in area-validation queue; priority report area; taxonomy boundary needs review; artifact-visible; high AlphaXiv attention; public attention without program signal
- Signals: votes=405; github_stars=346; taxonomy_review; evidence=medium
- Claim overlay keys: C02::62943 | C06::62943
- Area overlay keys: Systems and Efficient Foundation Models::62943
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md; reports/claim_validation_packets/c06-external-trend-context.md
- Claim dossiers: reports/claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md; reports/claim_evidence_dossiers/c06-external-trend-context.md
- Area packet: reports/validation_packets/systems-and-efficient-foundation-models.md
- Area briefing: reports/area_briefing_cards/systems-and-efficient-foundation-models.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62943) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.16652)

Abstract excerpt:

Evolution Strategies (ES) is a class of powerful black-box optimisation methods that are highly parallelisable and can handle non-differentiable and noisy objectives. However, naïve ES becomes prohibitively expensive at scale on GPUs due to the low arithmetic intensity of batched matrix multiplications with unstructured random perturbations. We introduce Evolution Guided GeneRal Optimisation via Low-rank Learning (EGGROLL), which improves arithmetic intensity by structuring individual perturbations as rank-$r$ matrices, resulting in a hundredfold increase in training speed for billion-parameter models at large population sizes, achieving up to 91\% of the throughput of pure batch...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 17. Learning to Discover at Test Time

- Phase: `main_thesis_claims`
- Area: Agents, Code, and Tool Use / Multi-agent search, planning, and coordination
- Claims: C02; C08
- Why first: in claim-validation queue; supports priority claim(s) C02; in area-validation queue; priority report area; taxonomy boundary needs review; artifact-visible; high AlphaXiv attention; public attention without program signal
- Signals: votes=529; github_stars=297; taxonomy_review; evidence=medium
- Claim overlay keys: C02::65888 | C08::65888
- Area overlay keys: Agents, Code, and Tool Use::65888
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md; reports/claim_validation_packets/c08-validation-priority.md
- Claim dossiers: reports/claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md; reports/claim_evidence_dossiers/c08-validation-priority.md
- Area packet: reports/validation_packets/agents-code-and-tool-use.md
- Area briefing: reports/area_briefing_cards/agents-code-and-tool-use.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65888) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.16175)

Abstract excerpt:

How can we use AI to discover a new state of the art for a scientific problem? Prior work in test-time scaling, such as AlphaEvolve, performs search by prompting a frozen LLM. We perform reinforcement learning at test time, so the LLM can continue to train, but now with experience specific to the test problem. This form of continual learning is quite special, because its goal is to produce one great solution rather than many good ones on average, and to solve this very problem rather than generalize to other problems. Therefore, our learning objective and search subroutine are designed to prioritize the most promising solutions. We call this method Test-Time Training to Discover...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 18. Agent Learning via Early Experience

- Phase: `main_thesis_claims`
- Area: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Claims: C01; C06
- Why first: in claim-validation queue; supports priority claim(s) C01; in area-validation queue; priority report area; taxonomy boundary needs review; artifact-visible; high AlphaXiv attention; public attention without program signal
- Signals: votes=532; github_stars=148; taxonomy_review; evidence=medium
- Claim overlay keys: C01::64488 | C06::64488
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::64488
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c01-llm-reasoning-center-of-gravity.md; reports/claim_validation_packets/c06-external-trend-context.md
- Claim dossiers: reports/claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md; reports/claim_evidence_dossiers/c06-external-trend-context.md
- Area packet: reports/validation_packets/llm-reasoning-post-training-and-rlvr.md
- Area briefing: reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64488) / [AlphaXiv](https://www.alphaxiv.org/abs/2510.08558)

Abstract excerpt:

A long-term goal of language agents is to learn and improve through their own experience, ultimately outperforming humans in complex, real-world tasks. However, training agents from experience data with reinforcement learning remains difficult in many environments, which either lack verifiable rewards (e.g., websites) or require inefficient long-horizon rollouts (e.g., multi-turn tool use). As a result, most current agents rely on supervised fine-tuning on expert data, which is challenging to scale and generalizes poorly. This limitation stems from the nature of expert demonstrations: they capture only a narrow range of scenarios, and expose the agent to limited environment diversity. We...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 19. WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference

- Phase: `main_thesis_claims`
- Area: LLM Reasoning, Post-Training, and RLVR / Diffusion language models and decoding
- Claims: C01
- Why first: in claim-validation queue; supports priority claim(s) C01; in area-validation queue; priority report area; oral/program signal; taxonomy boundary needs review; artifact-visible
- Signals: oral; votes=60; github_stars=644; taxonomy_review; evidence=medium
- Claim overlay keys: C01::64095
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::64095
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c01-llm-reasoning-center-of-gravity.md
- Claim dossiers: reports/claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md
- Area packet: reports/validation_packets/llm-reasoning-post-training-and-rlvr.md
- Area briefing: reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64095) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.22737)

Abstract excerpt:

Autoregressive (AR) generation is the standard decoding paradigm for Large Language Models (LLMs), but its token-by-token nature limits parallelism at inference time. Diffusion Language Models (DLLMs) offer parallel decoding by recovering multiple masked tokens per step; however, in practice they often fail to translate this parallelism into speed gains over optimized AR engines (e.g., vLLM). A key reason is that many DLLMs rely on bidirectional attention, which breaks standard prefix KV caching. We propose WeDLM, a diffusion decoding framework built entirely on standard causal attention to make parallel generation prefix-cache friendly. The core idea is to let each masked position...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 20. From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model

- Phase: `artifact_and_reproducibility`
- Area: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Claims: C07
- Why first: in claim-validation queue; supports priority claim(s) C07; in area-validation queue; oral/program signal; GitHub artifact needs manual check; artifact-visible
- Signals: oral; votes=14; github_stars=5069; artifact_manual_check; evidence=medium
- Claim overlay keys: C07::66596
- Area overlay keys: Robotics, Embodiment, and World Models::66596
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c07-artifact-visibility.md
- Claim dossiers: reports/claim_evidence_dossiers/c07-artifact-visibility.md
- Area packet: reports/validation_packets/robotics-embodiment-and-world-models.md
- Area briefing: reports/area_briefing_cards/robotics-embodiment-and-world-models.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/66596) / [AlphaXiv](https://www.alphaxiv.org/abs/2605.22671)

Abstract excerpt:

Vision-Language-Action (VLA) models often suffer from performance degradation under distribution shifts, as they struggle to learn generalized behavior representations across varying environments. While existing approaches attempt to construct behavior representations through action-centric latent variables, they are often limited by short-horizon temporal fragmentation and static execution-alignment, leading to inconsistent behaviors in complex scenarios. To address these limitations, we propose \textbf{BehaviorVLA}, a framework that facilitates robust manipulation through the learning of a temporally coherent behavioral representations. Our approach features two symmetric components:...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 21. Latent Collaboration in Multi-Agent Systems

- Phase: `main_thesis_claims`
- Area: LLM Reasoning, Post-Training, and RLVR / Reasoning models and chain-of-thought behavior
- Claims: C01; C08
- Why first: in claim-validation queue; supports priority claim(s) C01; in area-validation queue; priority report area; taxonomy boundary needs review; artifact-visible; high AlphaXiv attention
- Signals: votes=402; github_stars=1048; taxonomy_review; evidence=medium
- Claim overlay keys: C01::61180 | C08::61180
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::61180
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c01-llm-reasoning-center-of-gravity.md; reports/claim_validation_packets/c08-validation-priority.md
- Claim dossiers: reports/claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md; reports/claim_evidence_dossiers/c08-validation-priority.md
- Area packet: reports/validation_packets/llm-reasoning-post-training-and-rlvr.md
- Area briefing: reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61180) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.20639)

Abstract excerpt:

Multi-agent systems (MAS) extend large language models (LLMs) from independent single-model reasoning to coordinative system-level intelligence. While existing LLM agents depend on text-based mediation for reasoning and communication, we take a step forward by enabling models to collaborate directly within the continuous latent space. We introduce LatentMAS, an end-to-end training-free framework that enables pure latent collaboration among LLM agents. In LatentMAS, each agent first performs auto-regressive latent thoughts generation through last-layer hidden embeddings instead of text. Then, a shared latent working memory preserves and transfers each agent's internal representations and...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 22. Equivalence of Context and Parameter Updates in Modern Transformer Blocks

- Phase: `main_thesis_claims`
- Area: Theory, Optimization, and Algorithms / Transformer theory and attention expressivity
- Claims: C03
- Why first: in claim-validation queue; supports priority claim(s) C03; in area-validation queue; priority report area; oral/program signal; taxonomy boundary needs review
- Signals: oral; votes=24; taxonomy_review; evidence=medium
- Claim overlay keys: C03::63048
- Area overlay keys: Theory, Optimization, and Algorithms::63048
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c03-program-committee-attention.md
- Claim dossiers: reports/claim_evidence_dossiers/c03-program-committee-attention.md
- Area packet: reports/validation_packets/theory-optimization-and-algorithms.md
- Area briefing: reports/area_briefing_cards/theory-optimization-and-algorithms.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63048) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.17864)

Abstract excerpt:

Recent research has established that the impact of context in a vanilla transformer can be represented implicitly by forming a token-dependent, rank-1 patch to its MLP weights. This work extends that foundational theory to the diverse architectures of modern Large Language Models. We first demonstrate a precise, analytical solution for a Gemma-style transformer block, proving that the entire effect of a context can be perfectly mapped to rank-1 patches on its MLP weight matrices and a patch to the RMSNorm scale. We then generalize this result, providing a constructive proof and algorithm for multi-layer models. To unify these findings, we introduce a general framework centered on two...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 23. Optimal Decision-Making Based on Prediction Sets

- Phase: `main_thesis_claims`
- Area: Theory, Optimization, and Algorithms / Statistical learning theory and regression
- Claims: C03
- Why first: in claim-validation queue; supports priority claim(s) C03; in area-validation queue; priority report area; oral/program signal; taxonomy boundary needs review; artifact-visible
- Signals: oral; votes=6; github_stars=0; taxonomy_review; evidence=medium
- Claim overlay keys: C03::63638
- Area overlay keys: Theory, Optimization, and Algorithms::63638
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c03-program-committee-attention.md
- Claim dossiers: reports/claim_evidence_dossiers/c03-program-committee-attention.md
- Area packet: reports/validation_packets/theory-optimization-and-algorithms.md
- Area briefing: reports/area_briefing_cards/theory-optimization-and-algorithms.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63638) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.00989)

Abstract excerpt:

Prediction sets can wrap around any ML model to cover unknown test outcomes with a guaranteed probability. Yet, it remains unclear how to use them optimally for downstream decision-making. Here, we propose a decision-theoretic framework that seeks to minimize the expected loss (risk) against a worst-case distribution consistent with the prediction set's coverage guarantee. We first characterize the minimax optimal policy for a fixed prediction set, showing that it balances the worst-case loss inside the set with a penalty for potential losses outside the set. Building on this, we derive the optimal prediction set construction that minimizes the resulting robust risk subject to a coverage...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 24. $\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment

- Phase: `main_thesis_claims`
- Area: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Claims: C02
- Why first: in claim-validation queue; supports priority claim(s) C02; in area-validation queue; priority report area; oral/program signal; artifact-visible; moderate AlphaXiv attention
- Signals: oral; votes=89; github_stars=1569; evidence=medium
- Claim overlay keys: C02::64377
- Area overlay keys: Agents, Code, and Tool Use::64377
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md
- Claim dossiers: reports/claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md
- Area packet: reports/validation_packets/agents-code-and-tool-use.md
- Area briefing: reports/area_briefing_cards/agents-code-and-tool-use.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64377) / [AlphaXiv](https://www.alphaxiv.org/abs/2506.07982)

Abstract excerpt:

Existing benchmarks for conversational AI agents simulate *single-control* environments, where only the AI agent can use tools to interact with the world, while the user remains a passive information provider. This differs from real-world scenarios like technical support, where users need to actively participate in modifying the state of the (shared) world. In order to address this gap, we introduce $\tau^2$-bench, with four key contributions: 1. A novel **Telecom dual-control domain** modeled as a Dec-POMDP, where both agent and user make use of tools to act in a shared, dynamic environment that tests both agent coordination and communication, 2. A **compositional task generator** that...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 25. Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning

- Phase: `main_thesis_claims`
- Area: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Claims: C02
- Why first: in claim-validation queue; supports priority claim(s) C02; in area-validation queue; priority report area; oral/program signal; artifact-visible; moderate AlphaXiv attention
- Signals: oral; votes=89; github_stars=1228; evidence=medium
- Claim overlay keys: C02::63095
- Area overlay keys: Agents, Code, and Tool Use::63095
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md
- Claim dossiers: reports/claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md
- Area packet: reports/validation_packets/agents-code-and-tool-use.md
- Area briefing: reports/area_briefing_cards/agents-code-and-tool-use.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63095) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.19900)

Abstract excerpt:

Large Vision-Language Models (LVLMs) have achieved remarkable progress in multimodal reasoning tasks; however, their learning remains constrained by the limitations of human-annotated supervision. Recent self-rewarding approaches attempt to overcome this constraint by allowing models to act as their own critics or reward providers. Yet, purely text-based self-evaluation struggles to verify complex visual reasoning steps and often suffers from evaluation hallucinations. To address these challenges, inspired by recent advances in tool-integrated reasoning, we propose Agent0-VL, a self-evolving vision-language agent that achieves continual improvement with tool-integrated reasoning....

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 26. Position: Stop Automating Peer Review Without Rigorous Evaluation

- Phase: `main_thesis_claims`
- Area: Safety, Governance, Privacy, and Society / Position papers, policy, and social impacts
- Claims: C03
- Why first: in claim-validation queue; supports priority claim(s) C03; in area-validation queue; priority report area; oral/program signal; low-confidence evidence code
- Signals: oral; votes=13; evidence=low
- Claim overlay keys: C03::67247
- Area overlay keys: Safety, Governance, Privacy, and Society::67247
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c03-program-committee-attention.md
- Claim dossiers: reports/claim_evidence_dossiers/c03-program-committee-attention.md
- Area packet: reports/validation_packets/safety-governance-privacy-and-society.md
- Area briefing: reports/area_briefing_cards/safety-governance-privacy-and-society.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/67247) / [AlphaXiv](https://www.alphaxiv.org/abs/2605.03202)

Abstract excerpt:

Large language models offer a tempting solution to address the peer review crisis. This position paper argues that **today's AI systems should not be used to produce paper reviews**. We ground this positing in an empirical comparison of human- versus AI-generated ICLR 2026 reviews and an evaluation of the effect of automated paper rewriting on different AI reviewers. We identify two critical issues: 1) AI reviewers exhibit a *hivemind effect* of excessive agreement within and across papers that reduces perspective diversity. 2) AI review scores are trivially gameable through *paper laundering*: prompting an LLM to rewrite a paper could significantly increase the scores from AI reviewers,...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 27. Vision-aligned Latent Reasoning for Multi-Modal Large Language Model

- Phase: `artifact_and_reproducibility`
- Area: LLM Reasoning, Post-Training, and RLVR / Reasoning models and chain-of-thought behavior
- Claims: C07
- Why first: in claim-validation queue; supports priority claim(s) C07; priority report area; taxonomy boundary needs review; GitHub artifact needs manual check; artifact-visible
- Signals: votes=56; github_stars=6773; taxonomy_review; artifact_manual_check; evidence=medium
- Claim overlay keys: C07::61382
- Area overlay keys: none
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: none
- Claim packets: reports/claim_validation_packets/c07-artifact-visibility.md
- Claim dossiers: reports/claim_evidence_dossiers/c07-artifact-visibility.md
- Area packet: none
- Area briefing: reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/61382) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.04476)

Abstract excerpt:

Despite recent advancements in Multi-modal Large Language Models (MLLMs) on diverse understanding tasks, these models struggle to solve problems which require extensive multi-step reasoning. This is primarily due to the progressive dilution of visual information during long-context generation, which hinders their ability to fully exploit test-time scaling. To address this issue, we introduce Vision-aligned Latent Reasoning (VaLR), a simple, yet effective reasoning framework that dynamically generates vision-aligned latent tokens before each Chain of Thought reasoning step, guiding the model to reason based on perceptual cues in the latent space. Specifically, VaLR is trained to preserve...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 28. AuTAgent: A Reinforcement Learning Framework for Tool-Augmented Audio Reasoning

- Phase: `artifact_and_reproducibility`
- Area: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Claims: C07
- Why first: in claim-validation queue; supports priority claim(s) C07; priority report area; taxonomy boundary needs review; GitHub artifact needs manual check; artifact-visible
- Signals: votes=8; github_stars=5063; taxonomy_review; artifact_manual_check; evidence=medium
- Claim overlay keys: C07::64128
- Area overlay keys: none
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: none
- Claim packets: reports/claim_validation_packets/c07-artifact-visibility.md
- Claim dossiers: reports/claim_evidence_dossiers/c07-artifact-visibility.md
- Area packet: none
- Area briefing: reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64128) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.13685)

Abstract excerpt:

Large Audio Language Models (LALMs) excel at perception but struggle with complex reasoning requiring precise acoustic measurements. While external tools can extract fine-grained features like exact tempo or pitch, effective integration remains challenging: naively using all tools causes information overload, while prompt-based selection fails to assess context-dependent utility. To address this, we propose **AuTAgent** (**Au**dio **T**ool **Agent**), a reinforcement learning framework that learns when and which tools to invoke. By employing a sparse-feedback training strategy with a novel Differential Reward mechanism, the agent learns to filter out irrelevant tools and invokes external...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 29. Autoregressive Direct Preference Optimization

- Phase: `artifact_and_reproducibility`
- Area: LLM Reasoning, Post-Training, and RLVR / LLM preference tuning and alignment training
- Claims: C07
- Why first: in claim-validation queue; supports priority claim(s) C07; priority report area; taxonomy boundary needs review; GitHub artifact needs manual check; artifact-visible
- Signals: votes=6; github_stars=5063; taxonomy_review; artifact_manual_check; evidence=medium
- Claim overlay keys: C07::65423
- Area overlay keys: none
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: none
- Claim packets: reports/claim_validation_packets/c07-artifact-visibility.md
- Claim dossiers: reports/claim_evidence_dossiers/c07-artifact-visibility.md
- Area packet: none
- Area briefing: reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65423) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.09533)

Abstract excerpt:

Direct preference optimization (DPO) has emerged as a promising approach for aligning large language models (LLMs) with human preferences. However, the widespread reliance on the response-level Bradley-Terry (BT) model may limit its full potential, as the reference and learnable models are assumed to be autoregressive only after deriving the objective function. Motivated by this limitation, we revisit the theoretical foundations of DPO and propose a novel formulation that explicitly introduces the autoregressive assumption prior to applying the BT model. By reformulating and extending DPO, we derive a novel variant, termed \textbf{Autoregressive DPO (ADPO)}, that explicitly integrates...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 30. Learning to Theorize the World from Observation

- Phase: `main_thesis_claims`
- Area: LLM Reasoning, Post-Training, and RLVR / Reasoning models and chain-of-thought behavior
- Claims: C01
- Why first: in claim-validation queue; supports priority claim(s) C01; priority report area; oral/program signal; taxonomy boundary needs review; low-confidence evidence code
- Signals: oral; votes=56; taxonomy_review; evidence=low
- Claim overlay keys: C01::60765
- Area overlay keys: none
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: none
- Claim packets: reports/claim_validation_packets/c01-llm-reasoning-center-of-gravity.md
- Claim dossiers: reports/claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md
- Area packet: none
- Area briefing: reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/60765) / [AlphaXiv](https://www.alphaxiv.org/abs/2605.03413)

Abstract excerpt:

What does it mean to understand the world? Is it simply to predict future video frames? Developmental cognitive science suggests that understanding the world is fundamentally the process of constructing internal theories of how it works rather than mere prediction, even before language is acquired. However, in machine learning, it remains unclear how to endow AI systems with such theory-building capability from raw, non-textual observation alone. In this paper, we introduce Learning-to-Theorize (L2T), a learning paradigm in which an AI system acquires the ability to construct theories represented as executable programs directly from observation alone. To instantiate this paradigm, we...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 31. ToolOrchestra: Elevating Intelligence via Efficient Model and Tool Orchestration

- Phase: `main_thesis_claims`
- Area: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Claims: C02
- Why first: in claim-validation queue; supports priority claim(s) C02; in area-validation queue; priority report area; artifact-visible; high AlphaXiv attention; public attention without program signal
- Signals: votes=260; github_stars=745; evidence=medium
- Claim overlay keys: C02::62794
- Area overlay keys: Agents, Code, and Tool Use::62794
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md
- Claim dossiers: reports/claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md
- Area packet: reports/validation_packets/agents-code-and-tool-use.md
- Area briefing: reports/area_briefing_cards/agents-code-and-tool-use.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62794) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.21689)

Abstract excerpt:

Large language models are powerful generalists, yet solving deep and complex problems such as those of the Humanity’s Last Exam (HLE) remains both conceptually challenging and computationally expensive. We show that small orchestrators managing other models and a variety of tools are able to both push the upper bound of intelligence and improve efficiency in solving difficult agentic tasks. We introduce ToolOrchestra, a method for training small orchestrators that coordinate the use of intelligent tools. ToolOrchestra makes explicit use of reinforcement learning with outcome-, efficiency-, and user-preference-aware rewards. Using ToolOrchestra, we produce Orchestrator, an 8B model that...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 32. Process Reward Models That Think

- Phase: `main_thesis_claims`
- Area: LLM Reasoning, Post-Training, and RLVR / RL for reasoning models and verifiable rewards
- Claims: C01; C06
- Why first: in claim-validation queue; supports priority claim(s) C01; in area-validation queue; priority report area; artifact-visible; high AlphaXiv attention; public attention without program signal
- Signals: votes=1815; github_stars=89; evidence=medium
- Claim overlay keys: C01::68817 | C06::68817
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::68817
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c01-llm-reasoning-center-of-gravity.md; reports/claim_validation_packets/c06-external-trend-context.md
- Claim dossiers: reports/claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md; reports/claim_evidence_dossiers/c06-external-trend-context.md
- Area packet: reports/validation_packets/llm-reasoning-post-training-and-rlvr.md
- Area briefing: reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/68817) / [AlphaXiv](https://www.alphaxiv.org/abs/2504.16828)

Abstract excerpt:

Step-by-step verifiers—also known as process reward models (PRMs)—are a key ingredient for test-time scaling, but training them requires expensive step-level supervision. This work aims to build data-efficient PRMs as verbalized step-wise reward models that verify every step in the solution by generating a verification chain-of-thought (CoT). We propose ThinkPRM, a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. Our approach capitalizes on the inherent reasoning abilities of long CoT models, and outperforms LLM-as-a-Judge and discriminative verifiers—using only 1% of the process labels in PRM800K—across several...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 33. xKV: Cross-Layer KV-Cache Compression via Aligned Singular Vector Extraction

- Phase: `main_thesis_claims`
- Area: Systems and Efficient Foundation Models / Long-context attention and KV-cache compression
- Claims: C02; C06
- Why first: in claim-validation queue; supports priority claim(s) C02; in area-validation queue; priority report area; artifact-visible; high AlphaXiv attention; public attention without program signal
- Signals: votes=518; github_stars=52; evidence=medium
- Claim overlay keys: C02::63436 | C06::63436
- Area overlay keys: Systems and Efficient Foundation Models::63436
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md; reports/claim_validation_packets/c06-external-trend-context.md
- Claim dossiers: reports/claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md; reports/claim_evidence_dossiers/c06-external-trend-context.md
- Area packet: reports/validation_packets/systems-and-efficient-foundation-models.md
- Area briefing: reports/area_briefing_cards/systems-and-efficient-foundation-models.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63436) / [AlphaXiv](https://www.alphaxiv.org/abs/2503.18893)

Abstract excerpt:

Long-context Large Language Models (LLMs) enable powerful applications but incur high memory costs due to the key–value states (KV-Cache). Recent studies attempt to share KV-Cache across layers, but these approaches either require expensive pretraining or rely on per-token cross-layer cosine similarity that is often limited in practice. We show, via Centered Kernel Alignment (CKA), that the dominant singular vectors of KV-Cache are well aligned across layers. Motivated by this observation, we propose xKV, a post-training compression method that jointly factorizes grouped-layer KV-Cache into a shared low-rank subspace, substantially reducing KV-Cache memory. Across widely used LLMs, xKV...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 34. Monitoring Monitorability

- Phase: `main_thesis_claims`
- Area: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Claims: C02
- Why first: in claim-validation queue; supports priority claim(s) C02; in area-validation queue; priority report area; oral/program signal; artifact-visible
- Signals: oral; votes=28; github_stars=2786; evidence=medium
- Claim overlay keys: C02::62992
- Area overlay keys: Agents, Code, and Tool Use::62992
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md
- Claim dossiers: reports/claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md
- Area packet: reports/validation_packets/agents-code-and-tool-use.md
- Area briefing: reports/area_briefing_cards/agents-code-and-tool-use.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62992) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.18311)

Abstract excerpt:

Safe deployment of increasingly capable AI agents may require visibility into how they make decisions. Chain-of-thought (CoT) monitoring can detect misbehavior in today’s reasoning models, but this “monitorability” may be fragile under different training procedures, data sources, or continued system scaling. We propose three evaluation archetypes (intervention, process, and outcome-property), a new monitorability metric, and a broad evaluation suite. We show CoT monitoring outperforms action-only monitoring in practical settings, and that frontier models are generally—but not perfectly—monitorable. We study scaling trends with pre-training model size and inference-time compute, finding...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 35. DFlash: Block Diffusion for Flash Speculative Decoding

- Phase: `artifact_and_reproducibility`
- Area: LLM Reasoning, Post-Training, and RLVR / Diffusion language models and decoding
- Claims: C07
- Why first: in claim-validation queue; supports priority claim(s) C07; priority report area; taxonomy boundary needs review; artifact-visible; moderate AlphaXiv attention
- Signals: votes=153; github_stars=5451; taxonomy_review; evidence=medium
- Claim overlay keys: C07::64301
- Area overlay keys: none
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: none
- Claim packets: reports/claim_validation_packets/c07-artifact-visibility.md
- Claim dossiers: reports/claim_evidence_dossiers/c07-artifact-visibility.md
- Area packet: none
- Area briefing: reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/64301) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.06036)

Abstract excerpt:

Autoregressive large language models (LLMs) deliver strong performance but require inherently sequential decoding, leading to high inference latency and poor GPU utilization. Speculative decoding mitigates this bottleneck by using a fast draft model whose outputs are verified in parallel by the target LLM. However, existing methods still rely on *autoregressive drafting*, which remains sequential and constrains practical speedups. Diffusion LLMs offer a promising alternative by enabling parallel generation, but current diffusion models typically underperform compared with autoregressive models. In this paper, we introduce **DFlash**, a speculative decoding framework that employs a...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 36. Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking

- Phase: `main_thesis_claims`
- Area: Safety, Governance, Privacy, and Society / Adversarial safety, attacks, and security
- Claims: C03
- Why first: in claim-validation queue; supports priority claim(s) C03; in area-validation queue; priority report area; oral/program signal; artifact-visible
- Signals: oral; votes=9; github_stars=158; evidence=medium
- Claim overlay keys: C03::65657
- Area overlay keys: Safety, Governance, Privacy, and Society::65657
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c03-program-committee-attention.md
- Claim dossiers: reports/claim_evidence_dossiers/c03-program-committee-attention.md
- Area packet: reports/validation_packets/safety-governance-privacy-and-society.md
- Area briefing: reports/area_briefing_cards/safety-governance-privacy-and-society.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65657) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.24009)

Abstract excerpt:

Jailbreak techniques for large language models (LLMs) evolve faster than benchmarks, making robustness estimates stale and difficult to compare across papers due to drift in datasets, harnesses, and judging protocols. We introduce **JAILBREAK FOUNDRY (JBF)**, a system that addresses this gap via a multi-agent workflow to translate jailbreak papers into executable modules for immediate evaluation within a unified harness. JBF features three core components: (i) *JBF-LIB* for shared contracts and reusable utilities; (ii) *JBF-FORGE* for the multi-agent paper-to-module translation; and (iii) *JBF-EVAL* for standardizing evaluations. Across 30 reproduced attacks, JBF achieves high fidelity...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 37. CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability

- Phase: `main_thesis_claims`
- Area: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Claims: C02
- Why first: in claim-validation queue; supports priority claim(s) C02; in area-validation queue; priority report area; oral/program signal; artifact-visible
- Signals: oral; votes=21; github_stars=139; evidence=medium
- Claim overlay keys: C02::65622
- Area overlay keys: Agents, Code, and Tool Use::65622
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md
- Claim dossiers: reports/claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md
- Area packet: reports/validation_packets/agents-code-and-tool-use.md
- Area briefing: reports/area_briefing_cards/agents-code-and-tool-use.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/65622) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.03012)

Abstract excerpt:

Evaluating and improving the security capabilities of code agents requires high-quality, executable vulnerability tasks. However, existing works rely on costly, unscalable manual reproduction and suffer from outdated data distributions. To address these, we present CVE-Factory, the first multi-agent framework to achieve expert-level quality in automatically transforming sparse CVE metadata into fully executable agentic tasks. Cross-validation against human expert reproductions shows that CVE-Factory achieves 95\% solution correctness and 96\% environment fidelity, confirming its expert-level quality. It is also evaluated on the latest realistic vulnerabilities and achieves a 66.2\%...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 38. daVinci-Dev: Agent-native Mid-training for Software Engineering

- Phase: `main_thesis_claims`
- Area: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Claims: C02
- Why first: in claim-validation queue; supports priority claim(s) C02; in area-validation queue; priority report area; oral/program signal; artifact-visible
- Signals: oral; votes=52; github_stars=9; evidence=medium
- Claim overlay keys: C02::63099
- Area overlay keys: Agents, Code, and Tool Use::63099
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md
- Claim dossiers: reports/claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md
- Area packet: reports/validation_packets/agents-code-and-tool-use.md
- Area briefing: reports/area_briefing_cards/agents-code-and-tool-use.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/63099) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.18418)

Abstract excerpt:

Recently, the frontier of Large Language Model (LLM) capabilities has shifted from single-turn code generation to agentic software engineering—a paradigm where models autonomously navigate, edit, and test complex repositories. While post-training methods have become the de facto approach for code agents, *agentic mid-training*—mid-training (MT) on large-scale data that mirrors authentic agentic workflows—remains critically underexplored due to substantial resource requirements, despite offering a more scalable path to instilling foundational agentic behaviors than relying solely on expensive reinforcement learning. A central challenge in realizing effective agentic mid-training is the...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 39. Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections

- Phase: `main_thesis_claims`
- Area: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Claims: C02
- Why first: in claim-validation queue; supports priority claim(s) C02; in area-validation queue; priority report area; oral/program signal; artifact-visible
- Signals: oral; votes=26; github_stars=1; evidence=medium
- Claim overlay keys: C02::62732
- Area overlay keys: Agents, Code, and Tool Use::62732
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md
- Claim dossiers: reports/claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md
- Area packet: reports/validation_packets/agents-code-and-tool-use.md
- Area briefing: reports/area_briefing_cards/agents-code-and-tool-use.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/62732) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.12180)

Abstract excerpt:

Multimodal agents offer a compelling path to automating complex document-intensive workflows, yet a critical question remains: do these architectures demonstrate genuine strategic reasoning, or simply conduct stochastic trial-and-error search? To address this, we introduce Agentic Document VQA, a benchmark of 2,250 human-authored questions grounded in 800 heterogeneous PDF documents. Guided by *Classical Test Theory*, we design it to maximize discriminative power and reliably differentiate between varying levels of agent capability. To rigorously assess agentic behaviour, we introduce a novel evaluation protocol for measuring the accuracy-effort trade-off. Using this framework, we find...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

### 40. Position: Anthropomorphic Misalignment Research Needs Stronger Evidence

- Phase: `main_thesis_claims`
- Area: Safety, Governance, Privacy, and Society / Position papers, policy, and social impacts
- Claims: C03
- Why first: in claim-validation queue; supports priority claim(s) C03; in area-validation queue; priority report area; oral/program signal
- Signals: oral; votes=13; evidence=medium
- Claim overlay keys: C03::67238
- Area overlay keys: Safety, Governance, Privacy, and Society::67238
- Claim fields: manual_claim_support; manual_taxonomy_judgment; manual_artifact_judgment; manual_notes
- Area fields: manual_validated; manual_primary_contribution_type; manual_method_family; manual_artifact_status; manual_fault_line_relevance; manual_notes
- Claim packets: reports/claim_validation_packets/c03-program-committee-attention.md
- Claim dossiers: reports/claim_evidence_dossiers/c03-program-committee-attention.md
- Area packet: reports/validation_packets/safety-governance-privacy-and-society.md
- Area briefing: reports/area_briefing_cards/safety-governance-privacy-and-society.md
- URLs: [ICML](https://icml.cc/virtual/2026/poster/67238) / [AlphaXiv](https://www.alphaxiv.org/abs/2606.07612)

Abstract excerpt:

We argue that many Anthropomorphized Misalignment Research (AMR) studies need stronger evidence to ensure that they can provide a robust foundation for critical safety decisions, such as model deployment and regulation. By evaluating failure modes across different misalignment concepts, such as deception, emergent misalignment, and sycophancy, we show how conceptual ambiguity, non-robust datasets and experimental design, and insufficient causal interventions can lead to overinterpretation of model behaviors. This position paper aims to offer guidance on evidentiary considerations that can help improve methodological rigor in AMR. To achieve this, we provide a clear call to action through...

Manual judgment prompts:
- Does this paper support, weaken, or complicate the associated claim(s)?
- Is the area/subarea assignment correct enough for report use?
- Are artifact and benchmark/data/metric signals real after checking the source?
- What exact sentence-level caveat should be carried into the final report?

## Outputs

- `data/processed/icml2026_review_sprint_01.csv`
- `reports/icml2026_review_sprint_01.md`