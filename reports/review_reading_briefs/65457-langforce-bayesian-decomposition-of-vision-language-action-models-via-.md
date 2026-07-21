# LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries

- Sprint: `sprint_02` rank 11
- Global review rank: 105
- Event ID: `65457`
- Area: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Target claims: C04
- Review phase: `public_program_divergence`
- Note status: `not_started`
- Signals: votes=189; github_stars=69; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/65457) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.15197) / [GitHub](https://github.com/ZGC-EmbodyAI/LangForce)

## Where To Record Judgments

- Claim overlay keys: C04::65457
- Area overlay keys: Robotics, Embodiment, and World Models::65457
- Paper-note file: `data/manual/icml2026_review_sprint_02_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c04-public-attention-mismatch.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c04-public-attention-mismatch.md)
- Area packet: [area packet](../validation_packets/robotics-embodiment-and-world-models.md)
- Area briefing: [area briefing](../area_briefing_cards/robotics-embodiment-and-world-models.md)

## What To Verify

- Contribution: Label whether this robotics/world-model paper is mainly benchmark, demo, reusable model, or core algorithmic contribution.
- Method: RL / policy optimization; Bayesian / probabilistic
- Evidence: Check baselines, datasets, metrics, ablations, negative cases, and whether artifact links support the claim.
- Taxonomy: Classify the source of public attention: benchmark, demo, artifact, model release, or hype.
- Claim implication: Decide supports / weakens / complicates / not_applicable for C04.
- Artifact: Open GitHub/project link and record code/data/checkpoint/runnable status.

## Abstract Excerpt

Vision-Language-Action (VLA) models have shown promise in robot manipulation but often struggle to generalize to new instructions or complex multi-task scenarios. We identify a critical pathology in current training paradigms where goal-driven data collection creates a dataset bias. In such datasets, language instructions are highly predictable from visual observations alone, causing the conditional mutual information between instructions and actions to vanish, a phenomenon we term...

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