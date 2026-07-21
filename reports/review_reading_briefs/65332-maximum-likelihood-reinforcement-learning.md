# Maximum Likelihood Reinforcement Learning

- Sprint: `sprint_01` rank 5
- Global review rank: 5
- Event ID: `65332`
- Area: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Target claims: C01; C08
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: oral; votes=259; github_stars=194; taxonomy_review; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/65332) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.02710) / [GitHub](https://github.com/tajwarfahim/maxrl)

## Where To Record Judgments

- Claim overlay keys: C01::65332 | C08::65332
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::65332
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet 1](../claim_validation_packets/c01-llm-reasoning-center-of-gravity.md), [claim packet 2](../claim_validation_packets/c08-validation-priority.md)
- Claim dossiers: [claim dossier 1](../claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md), [claim dossier 2](../claim_evidence_dossiers/c08-validation-priority.md)
- Area packet: [area packet](../validation_packets/llm-reasoning-post-training-and-rlvr.md)
- Area briefing: [area briefing](../area_briefing_cards/llm-reasoning-post-training-and-rlvr.md)

## What To Verify

- Contribution: Method / algorithm: We show that for binary correctness tasks, expected-reward RL is a first-order approximation of the maximum likelihood objective, yielding vanishing learning signal on low-success inputs.
- Method: Tags: RL / policy optimization; Diffusion / flow; setting: language/llm; abstract cues: reinforcement learning; gradient.
- Evidence: metrics: pass@k; reward; check theorem assumptions and empirical/theory split
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Check whether this is genuinely LLM reasoning/post-training or a broader LLM/system/safety paper. | Use high-signal papers to stress-test taxonomy boundaries.
- Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable. C08 (Validation priority): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. Taxonomy assignment may be unstable.

## Abstract Excerpt

Maximum likelihood is fundamental to supervised learning but it cannot be directly applied in correctness-based problems with non-differentiable sampling. In these settings, reinforcement learning (RL) is typically used to maximize expected reward. We show that for binary correctness tasks, expected-reward RL is a first-order approximation of the maximum likelihood objective, yielding vanishing learning signal on low-success inputs. We introduce **Maximum Likelihood Reinforcement Learning (MaxRL)**, a compute-indexed family of sampling-based objectives derived from a pass@k expansion of the likelihood, which interpolates between standard RL and exact maximum likelihood as compute...

## Suggested Note Seed

Contribution: Method / algorithm: We show that for binary correctness tasks, expected-reward RL is a first-order approximation of the maximum likelihood objective, yielding vanishing learning signal on low-success inputs. Evidence to verify: metrics: pass@k; reward; check theorem assumptions and empirical/theory split Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable. C08 (Validation priority): decide supports / weakens / complicates / not_applicable.

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