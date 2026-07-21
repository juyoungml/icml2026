# BabyVision: Visual Reasoning Beyond Language

- Sprint: `sprint_02` rank 4
- Global review rank: 75
- Event ID: `63195`
- Area: Multimodal, Vision, and Perception / Vision-language reasoning and video understanding
- Target claims: C05
- Review phase: `public_program_divergence`
- Note status: `not_started`
- Signals: votes=134; github_stars=227; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/63195) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.06521) / [GitHub](https://github.com/UniPat-AI/BabyVision)

## Where To Record Judgments

- Claim overlay keys: C05::63195 | C06::63195
- Area overlay keys: Multimodal, Vision, and Perception::63195
- Paper-note file: `data/manual/icml2026_review_sprint_02_paper_notes.csv`

## Local Context

- Claim packets: [claim packet 1](../claim_validation_packets/c05-neighboring-venue-contrast.md), [claim packet 2](../claim_validation_packets/c06-external-trend-context.md)
- Claim dossiers: [claim dossier 1](../claim_evidence_dossiers/c05-neighboring-venue-contrast.md), [claim dossier 2](../claim_evidence_dossiers/c06-external-trend-context.md)
- Area packet: [area packet](../validation_packets/multimodal-vision-and-perception.md)
- Area briefing: [area briefing](../area_briefing_cards/multimodal-vision-and-perception.md)

## What To Verify

- Contribution: Break the multimodal/vision contribution into submode: video, 3D/spatial, multimodal reasoning, robustness, or general vision-language.
- Method: Reasoning / test-time compute; Agents / tool use
- Evidence: Check baselines, datasets, metrics, ablations, negative cases, and whether artifact links support the claim.
- Taxonomy: Check whether high-attention ICML multimodal papers look more like ICLR/NeurIPS-style vision work or ICML-style ML methods. | Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Claim implication: Decide supports / weakens / complicates / not_applicable for C05.
- Artifact: Open GitHub/project link and record code/data/checkpoint/runnable status.

## Abstract Excerpt

While humans develop core visual skills long before acquiring language, contemporary Multimodal LLMs (MLLMs) still rely heavily on linguistic priors to compensate for their fragile visual understanding. We uncovered a crucial fact: state-of-the-art MLLMs consistently fail on basic visual tasks that humans, even 3-year-olds, can solve effortlessly. To systematically investigate this gap, we introduce BabyVision, a benchmark designed to assess core visual abilities independent of linguistic...

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