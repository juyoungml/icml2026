# The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes

- Sprint: `sprint_01` rank 7
- Global review rank: 7
- Event ID: `60766`
- Area: Safety, Governance, Privacy, and Society / Adversarial safety, attacks, and security
- Target claims: C03
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: oral; Outstanding Paper Honorable Mention; votes=14; github_stars=13; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/60766) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.15515) / [GitHub](https://github.com/AlignmentResearch/obfuscation-atlas)

## Where To Record Judgments

- Claim overlay keys: C03::60766
- Area overlay keys: Safety, Governance, Privacy, and Society::60766
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c03-program-committee-attention.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c03-program-committee-attention.md)
- Area packet: [area packet](../validation_packets/safety-governance-privacy-and-society.md)
- Area briefing: [area briefing](../area_briefing_cards/safety-governance-privacy-and-society.md)

## What To Verify

- Contribution: Position / conceptual: We introduce a taxonomy of possible outcomes when training against a deception detector.
- Method: Tags: RL / policy optimization; LLM post-training; setting: language/llm; abstract cues: gradient.
- Evidence: metrics: reward
- Taxonomy: Identify the technical reason for high program signal and whether public attention misses it.
- Claim implication: C03 (Program committee attention): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness.

## Abstract Excerpt

Training against white-box deception detectors has been proposed as a way to make AI systems honest. However, such training risks models learning to obfuscate their deception to evade the detector. Prior work has studied obfuscation only in artificial settings where models were directly rewarded for harmful output. We construct a realistic coding environment where reward hacking via hardcoding test cases naturally occurs, and show that obfuscation emerges in this setting. We introduce a taxonomy of possible outcomes when training against a deception detector. The model either remains honest, or becomes deceptive via two possible obfuscation strategies. (i) *Obfuscated activations*: the...

## Suggested Note Seed

Contribution: Position / conceptual: We introduce a taxonomy of possible outcomes when training against a deception detector. Evidence to verify: metrics: reward Claim implication: C03 (Program committee attention): decide supports / weakens / complicates / not_applicable.

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