# Evolution Strategies at the Hyperscale

- Sprint: `sprint_01` rank 16
- Global review rank: 16
- Event ID: `62943`
- Area: Systems and Efficient Foundation Models / Large-scale training, optimizers, and model architecture
- Target claims: C02; C06
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: votes=405; github_stars=346; taxonomy_review; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/62943) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.16652) / [GitHub](https://github.com/ESHyperscale/HyperscaleES)

## Where To Record Judgments

- Claim overlay keys: C02::62943 | C06::62943
- Area overlay keys: Systems and Efficient Foundation Models::62943
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet 1](../claim_validation_packets/c02-infrastructure-and-agentic-workloads.md), [claim packet 2](../claim_validation_packets/c06-external-trend-context.md)
- Claim dossiers: [claim dossier 1](../claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md), [claim dossier 2](../claim_evidence_dossiers/c06-external-trend-context.md)
- Area packet: [area packet](../validation_packets/systems-and-efficient-foundation-models.md)
- Area briefing: [area briefing](../area_briefing_cards/systems-and-efficient-foundation-models.md)

## What To Verify

- Contribution: System / infrastructure: We introduce Evolution Guided GeneRal Optimisation via Low-rank Learning (EGGROLL), which improves arithmetic intensity by structuring individual perturbations as rank-$r$ matrices, resulting in a hundredfold increase in training speed for billion-parameter models at large population sizes, achieving up to 91\% of...
- Method: Tags: RL / policy optimization; LLM post-training; Reasoning / test-time compute; setting: language/llm; theory/synthetic; abstract cues: no obvious abstract keyword cue.
- Evidence: metrics: throughput; check theorem assumptions and empirical/theory split
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Check whether public signal reflects core infrastructure/agent workloads or broad LLM spillover. | Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable. C06 (External trend context): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Taxonomy assignment may be unstable.

## Abstract Excerpt

Evolution Strategies (ES) is a class of powerful black-box optimisation methods that are highly parallelisable and can handle non-differentiable and noisy objectives. However, naïve ES becomes prohibitively expensive at scale on GPUs due to the low arithmetic intensity of batched matrix multiplications with unstructured random perturbations. We introduce Evolution Guided GeneRal Optimisation via Low-rank Learning (EGGROLL), which improves arithmetic intensity by structuring individual perturbations as rank-$r$ matrices, resulting in a hundredfold increase in training speed for billion-parameter models at large population sizes, achieving up to 91\% of the throughput of pure batch...

## Suggested Note Seed

Contribution: System / infrastructure: We introduce Evolution Guided GeneRal Optimisation via Low-rank Learning (EGGROLL), which improves arithmetic intensity by structuring individual perturbations as rank-$r$ matrices, resulting in a hundredfold increase in training speed for billion-parameter models at large population sizes, achieving up to 91\% of... Evidence to verify: metrics: throughput; check theorem assumptions and empirical/theory split Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable. C06 (External trend context): decide supports / weakens / complicates / not_applicable.

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