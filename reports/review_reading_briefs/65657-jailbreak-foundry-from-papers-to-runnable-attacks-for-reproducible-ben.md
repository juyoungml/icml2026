# Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking

- Sprint: `sprint_01` rank 36
- Global review rank: 36
- Event ID: `65657`
- Area: Safety, Governance, Privacy, and Society / Adversarial safety, attacks, and security
- Target claims: C03
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: oral; votes=9; github_stars=158; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/65657) / [AlphaXiv](https://www.alphaxiv.org/abs/2602.24009) / [GitHub](https://github.com/OpenSQZ/Jailbreak-Foundry)

## Where To Record Judgments

- Claim overlay keys: C03::65657
- Area overlay keys: Safety, Governance, Privacy, and Society::65657
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c03-program-committee-attention.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c03-program-committee-attention.md)
- Area packet: [area packet](../validation_packets/safety-governance-privacy-and-society.md)
- Area briefing: [area briefing](../area_briefing_cards/safety-governance-privacy-and-society.md)

## What To Verify

- Contribution: Benchmark / evaluation: We introduce **JAILBREAK FOUNDRY (JBF)**, a system that addresses this gap via a multi-agent workflow to translate jailbreak papers into executable modules for immediate evaluation within a unified harness.
- Method: Tags: Agents / tool use; setting: math/code/verifiable; language/llm; security/safety; abstract cues: benchmark; dataset; agent.
- Evidence: benchmarks: AdvBench; metrics: success_rate
- Taxonomy: Identify the technical reason for high program signal and whether public attention misses it.
- Claim implication: C03 (Program committee attention): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness.

## Abstract Excerpt

Jailbreak techniques for large language models (LLMs) evolve faster than benchmarks, making robustness estimates stale and difficult to compare across papers due to drift in datasets, harnesses, and judging protocols. We introduce **JAILBREAK FOUNDRY (JBF)**, a system that addresses this gap via a multi-agent workflow to translate jailbreak papers into executable modules for immediate evaluation within a unified harness. JBF features three core components: (i) *JBF-LIB* for shared contracts and reusable utilities; (ii) *JBF-FORGE* for the multi-agent paper-to-module translation; and (iii) *JBF-EVAL* for standardizing evaluations. Across 30 reproduced attacks, JBF achieves high fidelity...

## Suggested Note Seed

Contribution: Benchmark / evaluation: We introduce **JAILBREAK FOUNDRY (JBF)**, a system that addresses this gap via a multi-agent workflow to translate jailbreak papers into executable modules for immediate evaluation within a unified harness. Evidence to verify: benchmarks: AdvBench; metrics: success_rate Claim implication: C03 (Program committee attention): decide supports / weakens / complicates / not_applicable.

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