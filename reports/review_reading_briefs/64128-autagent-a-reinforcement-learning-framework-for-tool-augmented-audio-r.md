# AuTAgent: A Reinforcement Learning Framework for Tool-Augmented Audio Reasoning

- Sprint: `sprint_01` rank 28
- Global review rank: 28
- Event ID: `64128`
- Area: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Target claims: C07
- Review phase: `artifact_and_reproducibility`
- Note status: `not_started`
- Signals: votes=8; github_stars=5063; taxonomy_review; artifact_manual_check; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/64128) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.13685) / [GitHub](https://github.com/eliahuhorwitz/Academic-project-page-template)

## Where To Record Judgments

- Claim overlay keys: C07::64128
- Area overlay keys: none
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c07-artifact-visibility.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c07-artifact-visibility.md)
- Area packet: none
- Area briefing: [area briefing](../area_briefing_cards/llm-reasoning-post-training-and-rlvr.md)

## What To Verify

- Contribution: Benchmark / evaluation: To address this, we propose **AuTAgent** (**Au**dio **T**ool **Agent**), a reinforcement learning framework that learns when and which tools to invoke.
- Method: Tags: RL / policy optimization; Reasoning / test-time compute; Agents / tool use; Compression / efficiency; setting: math/code/verifiable; language/llm; abstract cues: reinforcement learning; benchmark; agent; tool.
- Evidence: metrics: accuracy; reward; check theorem assumptions and empirical/theory split
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Determine whether the GitHub link is a real paper artifact or a template/index/project page.
- Claim implication: C07 (Artifact visibility): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Taxonomy assignment may be unstable.

## Abstract Excerpt

Large Audio Language Models (LALMs) excel at perception but struggle with complex reasoning requiring precise acoustic measurements. While external tools can extract fine-grained features like exact tempo or pitch, effective integration remains challenging: naively using all tools causes information overload, while prompt-based selection fails to assess context-dependent utility. To address this, we propose **AuTAgent** (**Au**dio **T**ool **Agent**), a reinforcement learning framework that learns when and which tools to invoke. By employing a sparse-feedback training strategy with a novel Differential Reward mechanism, the agent learns to filter out irrelevant tools and invokes external...

## Suggested Note Seed

Contribution: Benchmark / evaluation: To address this, we propose **AuTAgent** (**Au**dio **T**ool **Agent**), a reinforcement learning framework that learns when and which tools to invoke. Evidence to verify: metrics: accuracy; reward; check theorem assumptions and empirical/theory split Claim implication: C07 (Artifact visibility): decide supports / weakens / complicates / not_applicable.

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