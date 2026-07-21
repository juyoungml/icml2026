# Mind Your Margin and Boundary: Are Your Distilled Datasets Truly Robust?

- Sprint: `sprint_02` rank 10
- Global review rank: 83
- Event ID: `63330`
- Area: Multimodal, Vision, and Perception / Vision robustness, detection, and adversarial perception
- Target claims: C05
- Review phase: `taxonomy_boundaries`
- Note status: `not_started`
- Signals: oral; votes=2; taxonomy_review; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/63330) / [AlphaXiv](https://www.alphaxiv.org/abs/2605.20606)

## Where To Record Judgments

- Claim overlay keys: C05::63330
- Area overlay keys: none
- Paper-note file: `data/manual/icml2026_review_sprint_02_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c05-neighboring-venue-contrast.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c05-neighboring-venue-contrast.md)
- Area packet: none
- Area briefing: [area briefing](../area_briefing_cards/multimodal-vision-and-perception.md)

## What To Verify

- Contribution: Break the multimodal/vision contribution into submode: video, 3D/spatial, multimodal reasoning, robustness, or general vision-language.
- Method: Causal / data-centric
- Evidence: Check baselines, datasets, metrics, ablations, negative cases, and whether artifact links support the claim.
- Taxonomy: Check whether each subarea behaves differently from the aggregate underweight claim.
- Claim implication: Decide supports / weakens / complicates / not_applicable for C05.
- Artifact: No GitHub URL in metadata; record none/not_applicable unless the PDF shows a release.

## Abstract Excerpt

Dataset distillation (DD) compresses a large training set into a small synthetic set for efficient training, but most DD methods optimize only clean accuracy and leave robustness uncontrolled. Recent robust DD methods improve robustness, yet they often suffer from a poor accuracy–robustness trade-off because they (i) treat all adversarially perturbed examples uniformly, despite robust risk being dominated by near-zero robust margins, and (ii) do not explicitly increase inter-class separation...

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