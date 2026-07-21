# Motion Attribution for Video Generation

- Sprint: `sprint_02` rank 1
- Global review rank: 58
- Event ID: `60542`
- Area: Multimodal, Vision, and Perception / 3D, video, motion, and spatial understanding
- Target claims: C05
- Review phase: `priority_area_depth`
- Note status: `not_started`
- Signals: oral; Outstanding Paper Honorable Mention; votes=67; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/60542) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.08828)

## Where To Record Judgments

- Claim overlay keys: C05::60542
- Area overlay keys: Multimodal, Vision, and Perception::60542
- Paper-note file: `data/manual/icml2026_review_sprint_02_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c05-neighboring-venue-contrast.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c05-neighboring-venue-contrast.md)
- Area packet: [area packet](../validation_packets/multimodal-vision-and-perception.md)
- Area briefing: [area briefing](../area_briefing_cards/multimodal-vision-and-perception.md)

## What To Verify

- Contribution: Break the multimodal/vision contribution into submode: video, 3D/spatial, multimodal reasoning, robustness, or general vision-language.
- Method: LLM post-training; Causal / data-centric
- Evidence: Check baselines, datasets, metrics, ablations, negative cases, and whether artifact links support the claim.
- Taxonomy: Check whether each subarea behaves differently from the aggregate underweight claim.
- Claim implication: Decide supports / weakens / complicates / not_applicable for C05.
- Artifact: No GitHub URL in metadata; record none/not_applicable unless the PDF shows a release.

## Abstract Excerpt

Despite the rapid progress of video generation models, the role of data in influencing motion is poorly understood. We present Motive (MOTIon attribution for Video gEneration), a motion-centric, gradient-based data attribution framework that scales to modern, large, high-quality video datasets and models. We use this to study which fine-tuning clips improve or degrade temporal dynamics. Motive isolates temporal dynamics from static appearance via motion-weighted loss masks, yielding...

## Suggested Note Seed

Contribution check: Break the multimodal/vision contribution into submode: video, 3D/spatial, multimodal reasoning, robustness, or general vision-language. Evidence: inspect baselines, data, metrics, and limitations. Claim implication: decide supports / weakens / complicates / not_applicable for C05.

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