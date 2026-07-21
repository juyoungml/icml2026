# Vision-Language-Action Pretraining from Large-Scale Human Videos

- Sprint: `sprint_02` rank 12
- Global review rank: 106
- Event ID: `62813`
- Area: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Target claims: C04
- Review phase: `public_program_divergence`
- Note status: `not_started`
- Signals: votes=144; github_stars=52; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/62813) / [AlphaXiv](https://www.alphaxiv.org/abs/2507.15597) / [GitHub](https://github.com/BeingBeyond/Being-H0)

## Where To Record Judgments

- Claim overlay keys: C04::62813
- Area overlay keys: Robotics, Embodiment, and World Models::62813
- Paper-note file: `data/manual/icml2026_review_sprint_02_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c04-public-attention-mismatch.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c04-public-attention-mismatch.md)
- Area packet: [area packet](../validation_packets/robotics-embodiment-and-world-models.md)
- Area briefing: [area briefing](../area_briefing_cards/robotics-embodiment-and-world-models.md)

## What To Verify

- Contribution: Label whether this robotics/world-model paper is mainly benchmark, demo, reusable model, or core algorithmic contribution.
- Method: LLM post-training; Reasoning / test-time compute; Agents / tool use
- Evidence: Check baselines, datasets, metrics, ablations, negative cases, and whether artifact links support the claim.
- Taxonomy: Classify the source of public attention: benchmark, demo, artifact, model release, or hype.
- Claim implication: Decide supports / weakens / complicates / not_applicable for C04.
- Artifact: Open GitHub/project link and record code/data/checkpoint/runnable status.

## Abstract Excerpt

Existing Vision-Language-Action (VLA) models struggle with complex manipulation tasks requiring high dexterity and generalization, primarily due to their reliance on synthetic data with significant sim-to-real gaps or limited teleoperated demonstrations. To address this bottleneck, we propose leveraging human hands as a manipulator template, capitalizing on the rich dexterity and scalability present in web data of human manipulation. Our approach introduces physical instruction tuning, a...

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