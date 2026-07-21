# Reinforcement Learning via Self-Distillation

- Sprint: `sprint_01` rank 12
- Global review rank: 12
- Event ID: `64121`
- Area: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Target claims: C01; C06; C08
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: votes=718; github_stars=1008; taxonomy_review; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/64121) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.20802) / [GitHub](https://github.com/lasgroup/SDPO)

## Where To Record Judgments

- Claim overlay keys: C01::64121 | C06::64121 | C08::64121
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::64121
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet 1](../claim_validation_packets/c01-llm-reasoning-center-of-gravity.md), [claim packet 2](../claim_validation_packets/c06-external-trend-context.md), [claim packet 3](../claim_validation_packets/c08-validation-priority.md)
- Claim dossiers: [claim dossier 1](../claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md), [claim dossier 2](../claim_evidence_dossiers/c06-external-trend-context.md), [claim dossier 3](../claim_evidence_dossiers/c08-validation-priority.md)
- Area packet: [area packet](../validation_packets/llm-reasoning-post-training-and-rlvr.md)
- Area briefing: [area briefing](../area_briefing_cards/llm-reasoning-post-training-and-rlvr.md)

## What To Verify

- Contribution: Benchmark / evaluation: Large language models are increasingly post-trained with reinforcement learning in verifiable domains such as code and math.
- Method: Tags: RL / policy optimization; LLM post-training; Reasoning / test-time compute; Agents / tool use; Diffusion / flow; setting: math/code/verifiable; language/llm; abstract cues: reinforcement learning; tool.
- Evidence: benchmarks: LiveCodeBench; metrics: accuracy; reward; check theorem assumptions and empirical/theory split
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Check whether high attention supports the center-of-gravity claim. | Check whether broad arXiv-growth terms correspond to the paper's actual contribution. | Decide whether this cluster should remain in the assigned area/subarea or be relabeled.
- Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable. C06 (External trend context): decide supports / weakens / complicates / not_applicable. C08 (Validation priority): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Taxonomy assignment may be unstable.

## Abstract Excerpt

Large language models are increasingly post-trained with reinforcement learning in verifiable domains such as code and math. Yet, current methods for reinforcement learning with verifiable rewards (RLVR) learn only from a scalar outcome reward per attempt, creating a severe credit-assignment bottleneck. Many verifiable environments actually provide rich textual feedback, such as runtime errors or judge evaluations, that explain *why* an attempt failed. We formalize this setting as reinforcement learning with rich feedback and introduce **Self-Distillation Policy Optimization** (**SDPO**), which converts tokenized feedback into a dense learning signal without any external teacher or...

## Suggested Note Seed

Contribution: Benchmark / evaluation: Large language models are increasingly post-trained with reinforcement learning in verifiable domains such as code and math. Evidence to verify: benchmarks: LiveCodeBench; metrics: accuracy; reward; check theorem assumptions and empirical/theory split Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable. C06 (External trend context): decide supports / weakens / complicates / not_applicable. C08 (Validation priority): decide supports / weakens / complicates / not_applicable.

## Minimum Manual Fields

- `paper_read_status`
- `contribution_summary`
- `novelty_judgment`
- `method_summary`
- `evidence_strength`
- `baselines_checked`, `datasets_checked`, `metrics_checked`
- `limitations`
- `artifact_status_checked`
- `claim_implications`
- `taxonomy_correction`
- `final_report_use`