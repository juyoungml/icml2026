# Autoregressive Direct Preference Optimization

- Sprint: `sprint_01` rank 29
- Global review rank: 29
- Event ID: `65423`
- Area: LLM Reasoning, Post-Training, and RLVR / LLM preference tuning and alignment training
- Target claims: C07
- Review phase: `artifact_and_reproducibility`
- Note status: `not_started`
- Signals: votes=6; github_stars=5063; taxonomy_review; artifact_manual_check; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/65423) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.09533) / [GitHub](https://github.com/eliahuhorwitz/Academic-project-page-template)

## Where To Record Judgments

- Claim overlay keys: C07::65423
- Area overlay keys: none
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c07-artifact-visibility.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c07-artifact-visibility.md)
- Area packet: none
- Area briefing: [area briefing](../area_briefing_cards/llm-reasoning-post-training-and-rlvr.md)

## What To Verify

- Contribution: Method / algorithm: Furthermore, through theoretical analysis of ADPO, we show that there exist two length measures to be considered when designing DPO-based algorithms: the token length $\mu$ and the feedback length $\mu'$.
- Method: Tags: RL / policy optimization; LLM post-training; setting: language/llm; theory/synthetic; abstract cues: no obvious abstract keyword cue.
- Evidence: check human-study or user-evaluation setup
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Determine whether the GitHub link is a real paper artifact or a template/index/project page.
- Claim implication: C07 (Artifact visibility): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Taxonomy assignment may be unstable.

## Abstract Excerpt

Direct preference optimization (DPO) has emerged as a promising approach for aligning large language models (LLMs) with human preferences. However, the widespread reliance on the response-level Bradley-Terry (BT) model may limit its full potential, as the reference and learnable models are assumed to be autoregressive only after deriving the objective function. Motivated by this limitation, we revisit the theoretical foundations of DPO and propose a novel formulation that explicitly introduces the autoregressive assumption prior to applying the BT model. By reformulating and extending DPO, we derive a novel variant, termed \textbf{Autoregressive DPO (ADPO)}, that explicitly integrates...

## Suggested Note Seed

Contribution: Method / algorithm: Furthermore, through theoretical analysis of ADPO, we show that there exist two length measures to be considered when designing DPO-based algorithms: the token length $\mu$ and the feedback length $\mu'$. Evidence to verify: check human-study or user-evaluation setup Claim implication: C07 (Artifact visibility): decide supports / weakens / complicates / not_applicable.

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