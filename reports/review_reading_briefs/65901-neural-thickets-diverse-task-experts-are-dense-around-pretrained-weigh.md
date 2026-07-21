# Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights

- Sprint: `sprint_01` rank 4
- Global review rank: 4
- Event ID: `65901`
- Area: Systems and Efficient Foundation Models / Large-scale training, optimizers, and model architecture
- Target claims: C02; C06
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: votes=365; github_stars=627; taxonomy_review; evidence=low
- Links: [ICML](https://icml.cc/virtual/2026/poster/65901) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.12228) / [GitHub](https://github.com/sunrainyg/RandOpt)

## Where To Record Judgments

- Claim overlay keys: C02::65901 | C06::65901
- Area overlay keys: Systems and Efficient Foundation Models::65901
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet 1](../claim_validation_packets/c02-infrastructure-and-agentic-workloads.md), [claim packet 2](../claim_validation_packets/c06-external-trend-context.md)
- Claim dossiers: [claim dossier 1](../claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md), [claim dossier 2](../claim_evidence_dossiers/c06-external-trend-context.md)
- Area packet: [area packet](../validation_packets/systems-and-efficient-foundation-models.md)
- Area briefing: [area briefing](../area_briefing_cards/systems-and-efficient-foundation-models.md)

## What To Verify

- Contribution: Position / conceptual: We show that in smaller or insufficiently trained models such expert solutions occupy a negligible fraction of the volume of this distribution, making their discovery reliant on structured optimization methods such as gradient descent.
- Method: Tags: RL / policy optimization; LLM post-training; setting: no evaluation-setting tag; abstract cues: gradient.
- Evidence: identify baselines, datasets, metrics, ablations, and negative cases from the PDF
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Check whether public signal reflects core infrastructure/agent workloads or broad LLM spillover. | Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable. C06 (External trend context): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Heuristic evidence tag is low confidence. Taxonomy assignment may be unstable.

## Abstract Excerpt

Pretraining produces a learned parameter vector that is typically treated as a starting point for further iterative adaptation. In this work, we instead view the outcome of pretraining as a distribution over parameter vectors, whose support already contains task-specific experts. We show that in smaller or insufficiently trained models such expert solutions occupy a negligible fraction of the volume of this distribution, making their discovery reliant on structured optimization methods such as gradient descent. In contrast, in large, well-pretrained models the density of task-experts increases dramatically, so that diverse specialists populate a substantial fraction of the neighborhood...

## Suggested Note Seed

Contribution: Position / conceptual: We show that in smaller or insufficiently trained models such expert solutions occupy a negligible fraction of the volume of this distribution, making their discovery reliant on structured optimization methods such as gradient descent. Evidence to verify: identify baselines, datasets, metrics, ablations, and negative cases from the PDF Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable. C06 (External trend context): decide supports / weakens / complicates / not_applicable.

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