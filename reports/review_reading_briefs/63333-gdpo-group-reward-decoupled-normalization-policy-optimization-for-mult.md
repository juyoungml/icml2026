# GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization

- Sprint: `sprint_01` rank 14
- Global review rank: 14
- Event ID: `63333`
- Area: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Target claims: C01; C06
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: votes=507; github_stars=489; taxonomy_review; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/63333) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.05242) / [GitHub](https://github.com/NVlabs/GDPO)

## Where To Record Judgments

- Claim overlay keys: C01::63333 | C06::63333
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::63333
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet 1](../claim_validation_packets/c01-llm-reasoning-center-of-gravity.md), [claim packet 2](../claim_validation_packets/c06-external-trend-context.md)
- Claim dossiers: [claim dossier 1](../claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md), [claim dossier 2](../claim_evidence_dossiers/c06-external-trend-context.md)
- Area packet: [area packet](../validation_packets/llm-reasoning-post-training-and-rlvr.md)
- Area briefing: [area briefing](../area_briefing_cards/llm-reasoning-post-training-and-rlvr.md)

## What To Verify

- Contribution: Theory / proof: In this paper, we demonstrate that directly applying GRPO to normalize distinct rollout reward combinations causes them to collapse into identical advantage values, reducing the resolution of the training signal and resulting in suboptimal convergence and, in some cases, early training failure.
- Method: Tags: RL / policy optimization; LLM post-training; Reasoning / test-time compute; Agents / tool use; setting: math/code/verifiable; language/llm; abstract cues: reinforcement learning; tool.
- Evidence: metrics: accuracy; reward; check theorem assumptions and empirical/theory split; check human-study or user-evaluation setup
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Check whether high attention supports the center-of-gravity claim. | Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable. C06 (External trend context): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Taxonomy assignment may be unstable.

## Abstract Excerpt

As language models become increasingly capable, users expect them to provide not only accurate responses but also behaviors aligned with diverse human preferences across a variety of scenarios. To achieve this, Reinforcement learning (RL) pipelines have begun incorporating multiple rewards, each capturing a distinct preference, to guide models toward these desired behaviors. However, recent work has defaulted to apply Group Relative Policy Optimization (GRPO) under multi-reward setting without examining its suitability. In this paper, we demonstrate that directly applying GRPO to normalize distinct rollout reward combinations causes them to collapse into identical advantage values,...

## Suggested Note Seed

Contribution: Theory / proof: In this paper, we demonstrate that directly applying GRPO to normalize distinct rollout reward combinations causes them to collapse into identical advantage values, reducing the resolution of the training signal and resulting in suboptimal convergence and, in some cases, early training failure. Evidence to verify: metrics: accuracy; reward; check theorem assumptions and empirical/theory split; check human-study or user-evaluation setup Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable. C06 (External trend context): decide supports / weakens / complicates / not_applicable.

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