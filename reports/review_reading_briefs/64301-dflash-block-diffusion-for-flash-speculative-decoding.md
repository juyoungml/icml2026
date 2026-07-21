# DFlash: Block Diffusion for Flash Speculative Decoding

- Sprint: `sprint_01` rank 35
- Global review rank: 35
- Event ID: `64301`
- Area: LLM Reasoning, Post-Training, and RLVR / Diffusion language models and decoding
- Target claims: C07
- Review phase: `artifact_and_reproducibility`
- Note status: `not_started`
- Signals: votes=153; github_stars=5451; taxonomy_review; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/64301) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.06036) / [GitHub](https://github.com/z-lab/dflash)

## Where To Record Judgments

- Claim overlay keys: C07::64301
- Area overlay keys: none
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c07-artifact-visibility.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c07-artifact-visibility.md)
- Area packet: none
- Area briefing: [area briefing](../area_briefing_cards/llm-reasoning-post-training-and-rlvr.md)

## What To Verify

- Contribution: System / infrastructure: In this paper, we introduce **DFlash**, a speculative decoding framework that employs a lightweight block diffusion model for parallel drafting.
- Method: Tags: Reasoning / test-time compute; Diffusion / flow; setting: language/llm; abstract cues: diffusion.
- Evidence: metrics: latency; check theorem assumptions and empirical/theory split
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Check artifact type, license/readme quality, and whether reproduction assets are present.
- Claim implication: C07 (Artifact visibility): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Taxonomy assignment may be unstable.

## Abstract Excerpt

Autoregressive large language models (LLMs) deliver strong performance but require inherently sequential decoding, leading to high inference latency and poor GPU utilization. Speculative decoding mitigates this bottleneck by using a fast draft model whose outputs are verified in parallel by the target LLM. However, existing methods still rely on *autoregressive drafting*, which remains sequential and constrains practical speedups. Diffusion LLMs offer a promising alternative by enabling parallel generation, but current diffusion models typically underperform compared with autoregressive models. In this paper, we introduce **DFlash**, a speculative decoding framework that employs a...

## Suggested Note Seed

Contribution: System / infrastructure: In this paper, we introduce **DFlash**, a speculative decoding framework that employs a lightweight block diffusion model for parallel drafting. Evidence to verify: metrics: latency; check theorem assumptions and empirical/theory split Claim implication: C07 (Artifact visibility): decide supports / weakens / complicates / not_applicable.

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