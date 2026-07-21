# Position: Stop Automating Peer Review Without Rigorous Evaluation

- Sprint: `sprint_01` rank 26
- Global review rank: 26
- Event ID: `67247`
- Area: Safety, Governance, Privacy, and Society / Position papers, policy, and social impacts
- Target claims: C03
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: oral; votes=13; evidence=low
- Links: [ICML](https://icml.cc/virtual/2026/poster/67247) / [AlphaXiv](https://www.alphaxiv.org/abs/2605.03202)

## Where To Record Judgments

- Claim overlay keys: C03::67247
- Area overlay keys: Safety, Governance, Privacy, and Society::67247
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c03-program-committee-attention.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c03-program-committee-attention.md)
- Area packet: [area packet](../validation_packets/safety-governance-privacy-and-society.md)
- Area briefing: [area briefing](../area_briefing_cards/safety-governance-privacy-and-society.md)

## What To Verify

- Contribution: Position / conceptual: Large language models offer a tempting solution to address the peer review crisis.
- Method: Tags: no method-family tag; setting: language/llm; abstract cues: no obvious abstract keyword cue.
- Evidence: check human-study or user-evaluation setup
- Taxonomy: Identify the technical reason for high program signal and whether public attention misses it.
- Claim implication: C03 (Program committee attention): decide supports / weakens / complicates / not_applicable.
- Artifact: No obvious artifact link; record none/not_applicable unless PDF shows a release.
- Warning: Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. Heuristic evidence tag is low confidence.

## Abstract Excerpt

Large language models offer a tempting solution to address the peer review crisis. This position paper argues that **today's AI systems should not be used to produce paper reviews**. We ground this positing in an empirical comparison of human- versus AI-generated ICLR 2026 reviews and an evaluation of the effect of automated paper rewriting on different AI reviewers. We identify two critical issues: 1) AI reviewers exhibit a *hivemind effect* of excessive agreement within and across papers that reduces perspective diversity. 2) AI review scores are trivially gameable through *paper laundering*: prompting an LLM to rewrite a paper could significantly increase the scores from AI reviewers,...

## Suggested Note Seed

Contribution: Position / conceptual: Large language models offer a tempting solution to address the peer review crisis. Evidence to verify: check human-study or user-evaluation setup Claim implication: C03 (Program committee attention): decide supports / weakens / complicates / not_applicable.

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