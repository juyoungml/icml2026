# From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models

- Sprint: `sprint_02` rank 13
- Global review rank: 107
- Event ID: `63621`
- Area: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Target claims: C04
- Review phase: `breadth_and_sanity_checks`
- Note status: `not_started`
- Signals: oral; votes=30; github_stars=35; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/63621) / [AlphaXiv](https://www.alphaxiv.org/abs/2605.04678) / [GitHub](https://github.com/RUCKBReasoning/From_Pixels_to_Tokens)

## Where To Record Judgments

- Claim overlay keys: C04::63621
- Area overlay keys: Robotics, Embodiment, and World Models::63621
- Paper-note file: `data/manual/icml2026_review_sprint_02_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c04-public-attention-mismatch.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c04-public-attention-mismatch.md)
- Area packet: [area packet](../validation_packets/robotics-embodiment-and-world-models.md)
- Area briefing: [area briefing](../area_briefing_cards/robotics-embodiment-and-world-models.md)

## What To Verify

- Contribution: Label whether this robotics/world-model paper is mainly benchmark, demo, reusable model, or core algorithmic contribution.
- Method: Reasoning / test-time compute
- Evidence: Check baselines, datasets, metrics, ablations, negative cases, and whether artifact links support the claim.
- Taxonomy: Compare public-heavy robotics papers against program-selected anchors.
- Claim implication: Decide supports / weakens / complicates / not_applicable for C04.
- Artifact: Open GitHub/project link and record code/data/checkpoint/runnable status.

## Abstract Excerpt

Latent actions serve as an intermediate representation that enables consistent modeling of vision-language-action (VLA) models across heterogeneous datasets. However, approaches to supervising VLAs with latent actions are fragmented and lack a systematic comparison. This work structures the study of latent action supervision from two perspectives: (i) regularizing the trajectory via image-based latent actions, and (ii) unifying the target space with action-based latent actions. Under a...

## Suggested Note Seed

Contribution check: Label whether this robotics/world-model paper is mainly benchmark, demo, reusable model, or core algorithmic contribution. Evidence: inspect baselines, data, metrics, and limitations. Claim implication: decide supports / weakens / complicates / not_applicable for C04.

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