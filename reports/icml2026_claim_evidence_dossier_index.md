# ICML 2026 Claim Evidence Dossiers

These dossiers are abstract/title-based pre-review aids for the synthesis claim packets.
They are designed to help a researcher decide what to read first; they do not complete manual validation.

## Snapshot

- Claim rows summarized: 118
- Priority claim rows summarized: 58
- Dossier files: 8

## Claim Dossier Index

| Claim | Priority | Rows | Reviewed | Pre-Review Buckets | Dossier |
| --- | --- | ---: | ---: | --- | --- |
| C01 - LLM reasoning center of gravity | yes | 14 | 0 | likely_supports: 14 | [open](claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md) |
| C02 - Infrastructure and agentic workloads | yes | 14 | 0 | likely_supports: 14 | [open](claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md) |
| C03 - Program committee attention | yes | 14 | 0 | likely_supports: 14 | [open](claim_evidence_dossiers/c03-program-committee-attention.md) |
| C04 - Public attention mismatch | no | 12 | 0 | possible_support: 12 | [open](claim_evidence_dossiers/c04-public-attention-mismatch.md) |
| C05 - Neighboring-venue contrast | no | 14 | 0 | possible_support: 14 | [open](claim_evidence_dossiers/c05-neighboring-venue-contrast.md) |
| C06 - External trend context | no | 16 | 0 | possible_support: 14, unclear: 2 | [open](claim_evidence_dossiers/c06-external-trend-context.md) |
| C07 - Artifact visibility | yes | 16 | 0 | high_risk_artifact: 12, high_visibility_artifact: 4 | [open](claim_evidence_dossiers/c07-artifact-visibility.md) |
| C08 - Validation priority | no | 18 | 0 | unclear: 17, possible_support: 1 | [open](claim_evidence_dossiers/c08-validation-priority.md) |

## How To Use

1. Start with C01, C02, C03, and C07.
2. Read the papers marked `likely_supports`, `boundary_case`, `high_risk_artifact`, or `high_visibility_artifact` first.
3. Fill the manual fields in `data/processed/icml2026_claim_validation_queue.csv` only after reading the paper or authoritative artifact page.
4. Re-run `build_review_progress.py`, `build_researcher_readiness_audit.py`, and this script after manual fields are filled.

## Outputs

- `data/processed/icml2026_claim_evidence_dossiers.csv`
- `reports/icml2026_claim_evidence_dossier_index.md`
- `reports/claim_evidence_dossiers/*.md`