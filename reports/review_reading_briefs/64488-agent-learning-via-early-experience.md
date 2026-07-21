# Agent Learning via Early Experience

- Sprint: `sprint_01` rank 18
- Global review rank: 18
- Event ID: `64488`
- Area: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Target claims: C01; C06
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: votes=532; github_stars=148; taxonomy_review; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/64488) / [AlphaXiv](https://www.alphaxiv.org/abs/2510.08558) / [GitHub](https://github.com/jettbrains/-L-)

## Where To Record Judgments

- Claim overlay keys: C01::64488 | C06::64488
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::64488
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet 1](../claim_validation_packets/c01-llm-reasoning-center-of-gravity.md), [claim packet 2](../claim_validation_packets/c06-external-trend-context.md)
- Claim dossiers: [claim dossier 1](../claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md), [claim dossier 2](../claim_evidence_dossiers/c06-external-trend-context.md)
- Area packet: [area packet](../validation_packets/llm-reasoning-post-training-and-rlvr.md)
- Area briefing: [area briefing](../area_briefing_cards/llm-reasoning-post-training-and-rlvr.md)

## What To Verify

- Contribution: Method / algorithm: Within this paradigm, we study two strategies of using such data: (1) implicit world modeling, which uses collected states to ground the policy in environment dynamics; and (2) self-reflection, where the agent learns from its suboptimal actions to improve reasoning and decision-making.
- Method: Tags: RL / policy optimization; LLM post-training; Reasoning / test-time compute; Agents / tool use; setting: math/code/verifiable; language/llm; abstract cues: reinforcement learning; agent; tool.
- Evidence: metrics: reward; check theorem assumptions and empirical/theory split; check human-study or user-evaluation setup; check sim-to-real or deployment evidence
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Check whether high attention supports the center-of-gravity claim. | Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable. C06 (External trend context): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Taxonomy assignment may be unstable.

## Abstract Excerpt

A long-term goal of language agents is to learn and improve through their own experience, ultimately outperforming humans in complex, real-world tasks. However, training agents from experience data with reinforcement learning remains difficult in many environments, which either lack verifiable rewards (e.g., websites) or require inefficient long-horizon rollouts (e.g., multi-turn tool use). As a result, most current agents rely on supervised fine-tuning on expert data, which is challenging to scale and generalizes poorly. This limitation stems from the nature of expert demonstrations: they capture only a narrow range of scenarios, and expose the agent to limited environment diversity. We...

## Suggested Note Seed

Contribution: Method / algorithm: Within this paradigm, we study two strategies of using such data: (1) implicit world modeling, which uses collected states to ground the policy in environment dynamics; and (2) self-reflection, where the agent learns from its suboptimal actions to improve reasoning and decision-making. Evidence to verify: metrics: reward; check theorem assumptions and empirical/theory split; check human-study or user-evaluation setup; check sim-to-real or deployment evidence Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable. C06 (External trend context): decide supports / weakens / complicates / not_applicable.

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