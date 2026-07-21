# Equivalence of Context and Parameter Updates in Modern Transformer Blocks

- Sprint: `sprint_01` rank 22
- Global review rank: 22
- Event ID: `63048`
- Area: Theory, Optimization, and Algorithms / Transformer theory and attention expressivity
- Target claims: C03
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: oral; votes=24; taxonomy_review; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/63048) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.17864)

## Where To Record Judgments

- Claim overlay keys: C03::63048
- Area overlay keys: Theory, Optimization, and Algorithms::63048
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c03-program-committee-attention.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c03-program-committee-attention.md)
- Area packet: [area packet](../validation_packets/theory-optimization-and-algorithms.md)
- Area briefing: [area briefing](../area_briefing_cards/theory-optimization-and-algorithms.md)

## What To Verify

- Contribution: Theory / proof: To unify these findings, we introduce a general framework centered on two core properties: input controllability and output controllability.
- Method: Tags: Transformer / attention; setting: language/llm; theory/synthetic; abstract cues: transformer; theory.
- Evidence: check theorem assumptions and empirical/theory split
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Identify the technical reason for high program signal and whether public attention misses it.
- Claim implication: C03 (Program committee attention): decide supports / weakens / complicates / not_applicable.
- Artifact: No obvious artifact link; record none/not_applicable unless PDF shows a release.
- Warning: Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. Taxonomy assignment may be unstable.

## Abstract Excerpt

Recent research has established that the impact of context in a vanilla transformer can be represented implicitly by forming a token-dependent, rank-1 patch to its MLP weights. This work extends that foundational theory to the diverse architectures of modern Large Language Models. We first demonstrate a precise, analytical solution for a Gemma-style transformer block, proving that the entire effect of a context can be perfectly mapped to rank-1 patches on its MLP weight matrices and a patch to the RMSNorm scale. We then generalize this result, providing a constructive proof and algorithm for multi-layer models. To unify these findings, we introduce a general framework centered on two...

## Suggested Note Seed

Contribution: Theory / proof: To unify these findings, we introduce a general framework centered on two core properties: input controllability and output controllability. Evidence to verify: check theorem assumptions and empirical/theory split Claim implication: C03 (Program committee attention): decide supports / weakens / complicates / not_applicable.

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