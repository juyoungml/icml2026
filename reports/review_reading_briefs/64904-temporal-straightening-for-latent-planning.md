# Temporal Straightening for Latent Planning

- Sprint: `sprint_02` rank 9
- Global review rank: 82
- Event ID: `64904`
- Area: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Target claims: C04
- Review phase: `public_program_divergence`
- Note status: `not_started`
- Signals: votes=202; github_stars=92; evidence=very_low
- Links: [ICML](https://icml.cc/virtual/2026/poster/64904) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.12231) / [GitHub](https://github.com/agentic-learning-ai-lab/temporal-straightening)

## Where To Record Judgments

- Claim overlay keys: C04::64904
- Area overlay keys: Robotics, Embodiment, and World Models::64904
- Paper-note file: `data/manual/icml2026_review_sprint_02_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c04-public-attention-mismatch.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c04-public-attention-mismatch.md)
- Area packet: [area packet](../validation_packets/robotics-embodiment-and-world-models.md)
- Area briefing: [area briefing](../area_briefing_cards/robotics-embodiment-and-world-models.md)

## What To Verify

- Contribution: Label whether this robotics/world-model paper is mainly benchmark, demo, reusable model, or core algorithmic contribution.
- Method: Identify core method family and whether it matches the metadata tags.
- Evidence: Check baselines, datasets, metrics, ablations, negative cases, and whether artifact links support the claim.
- Taxonomy: Classify the source of public attention: benchmark, demo, artifact, model release, or hype.
- Claim implication: Decide supports / weakens / complicates / not_applicable for C04.
- Artifact: Open GitHub/project link and record code/data/checkpoint/runnable status.

## Abstract Excerpt

Learning good representations is essential for latent planning with world models. While pretrained visual encoders provide strong visual features, they are not tailored to planning and contain substantial information which is irrelevant to planning. Inspired by the perceptual straightening hypothesis in human visual processing, we introduce temporal straightening for representation learning in latent planning. We add a lightweight projector on top of a pretrained visual encoder to map to a...

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