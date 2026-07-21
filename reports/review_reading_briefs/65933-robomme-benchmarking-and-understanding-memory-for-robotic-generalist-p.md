# RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies

- Sprint: `sprint_02` rank 14
- Global review rank: 108
- Event ID: `65933`
- Area: Robotics, Embodiment, and World Models / Vision-language-action models and robotic manipulation
- Target claims: C04
- Review phase: `breadth_and_sanity_checks`
- Note status: `not_started`
- Signals: oral; votes=66; github_stars=31; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/65933) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.04639) / [GitHub](https://github.com/sled-group/navchat)

## Where To Record Judgments

- Claim overlay keys: C04::65933
- Area overlay keys: Robotics, Embodiment, and World Models::65933
- Paper-note file: `data/manual/icml2026_review_sprint_02_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c04-public-attention-mismatch.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c04-public-attention-mismatch.md)
- Area packet: [area packet](../validation_packets/robotics-embodiment-and-world-models.md)
- Area briefing: [area briefing](../area_briefing_cards/robotics-embodiment-and-world-models.md)

## What To Verify

- Contribution: Label whether this robotics/world-model paper is mainly benchmark, demo, reusable model, or core algorithmic contribution.
- Method: Agents / tool use
- Evidence: Check baselines, datasets, metrics, ablations, negative cases, and whether artifact links support the claim.
- Taxonomy: Compare public-heavy robotics papers against program-selected anchors.
- Claim implication: Decide supports / weakens / complicates / not_applicable for C04.
- Artifact: Open GitHub/project link and record code/data/checkpoint/runnable status.

## Abstract Excerpt

Memory is critical for long-horizon and history-dependent robotic manipulation. Such tasks often involve counting repeated actions or manipulating objects that become temporarily occluded. Recent vision-language-action (VLA) models have begun to incorporate memory mechanisms; however, their evaluations remain confined to narrow, non-standardized settings. This limits their systematic understanding, comparison, and progress measurement. To address these challenges, we introduce **RoboMME**: a...

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