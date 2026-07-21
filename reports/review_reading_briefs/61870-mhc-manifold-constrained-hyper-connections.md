# mHC: Manifold-Constrained Hyper-Connections

- Sprint: `sprint_01` rank 15
- Global review rank: 15
- Event ID: `61870`
- Area: Systems and Efficient Foundation Models / Large-scale training, optimizers, and model architecture
- Target claims: C02; C06; C08
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: votes=696; github_stars=367; taxonomy_review; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/61870) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.24880) / [GitHub](https://github.com/tokenbender/mHC-manifold-constrained-hyper-connections)

## Where To Record Judgments

- Claim overlay keys: C02::61870 | C06::61870 | C08::61870
- Area overlay keys: Systems and Efficient Foundation Models::61870
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet 1](../claim_validation_packets/c02-infrastructure-and-agentic-workloads.md), [claim packet 2](../claim_validation_packets/c06-external-trend-context.md), [claim packet 3](../claim_validation_packets/c08-validation-priority.md)
- Claim dossiers: [claim dossier 1](../claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md), [claim dossier 2](../claim_evidence_dossiers/c06-external-trend-context.md), [claim dossier 3](../claim_evidence_dossiers/c08-validation-priority.md)
- Area packet: [area packet](../validation_packets/systems-and-efficient-foundation-models.md)
- Area briefing: [area briefing](../area_briefing_cards/systems-and-efficient-foundation-models.md)

## What To Verify

- Contribution: System / infrastructure: To address these challenges, we propose Manifold-Constrained Hyper-Connections (mHC), a general framework that projects the residual connection space of HC onto a specific manifold to restore the identity mapping property, while incorporating rigorous infrastructure optimization to ensure efficiency.
- Method: Tags: Graphs / geometry; setting: language/llm; abstract cues: no obvious abstract keyword cue.
- Evidence: metrics: memory; check theorem assumptions and empirical/theory split
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Check whether public signal reflects core infrastructure/agent workloads or broad LLM spillover. | Check whether broad arXiv-growth terms correspond to the paper's actual contribution. | Decide whether this cluster should remain in the assigned area/subarea or be relabeled.
- Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable. C06 (External trend context): decide supports / weakens / complicates / not_applicable. C08 (Validation priority): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Taxonomy assignment may be unstable.

## Abstract Excerpt

Recently, studies exemplified by Hyper-Connections (HC) have extended the ubiquitous residual connection paradigm established over the past decade by expanding the residual stream width and diversifying connectivity patterns. While yielding substantial performance gains, this diversification fundamentally compromises the identity mapping property intrinsic to the residual connection, which causes severe training instability and restricted scalability, and additionally incurs notable memory access overhead. To address these challenges, we propose Manifold-Constrained Hyper-Connections (mHC), a general framework that projects the residual connection space of HC onto a specific manifold to...

## Suggested Note Seed

Contribution: System / infrastructure: To address these challenges, we propose Manifold-Constrained Hyper-Connections (mHC), a general framework that projects the residual connection space of HC onto a specific manifold to restore the identity mapping property, while incorporating rigorous infrastructure optimization to ensure efficiency. Evidence to verify: metrics: memory; check theorem assumptions and empirical/theory split Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable. C06 (External trend context): decide supports / weakens / complicates / not_applicable. C08 (Validation priority): decide supports / weakens /...

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