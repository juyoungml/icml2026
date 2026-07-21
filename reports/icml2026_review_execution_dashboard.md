# ICML 2026 Review Execution Dashboard

Operational dashboard for moving manual paper review into validated claim decisions.

## Snapshot

- Metrics tracked: 9
- Metric status mix: not_started: 6, pass: 3
- Claims needing sprint execution: 6

## Metrics

| Area | Metric | Current | Target | Rate | Status | Next action |
| --- | --- | ---: | ---: | ---: | --- | --- |
| manual_review | `reviewed_validation_rows` | 0 | 310 | 0.0% | not_started | Fill claim and area overlay rows after paper-note review. |
| manual_review | `sprint_01_notes_started` | 0 | 40 | 0.0% | not_started | Start with sprint 01 notes for C01/C02/C03/C07 and transfer decisions through the bridge. |
| manual_review | `sprint_02_notes_started` | 0 | 16 | 0.0% | not_started | Use sprint 02 to unblock C04 and C05. |
| manual_review | `sprint_01_bridge_ready` | 0 | 94 | 0.0% | not_started | After notes are filled, rebuild bridge and transfer ready rows into overlays. |
| manual_review | `sprint_02_bridge_ready` | 0 | 35 | 0.0% | not_started | After sprint 02 notes are filled, transfer C04/C05 rows into overlays. |
| quality_gate | `invalid_coded_values` | 0 | 0 | 0.0% | pass | Fix invalid coded values before rebuilding reviewed tables. |
| quality_gate | `coded_values_checked` | 0 | 0 | 0.0% | pass | Run the linter after every manual edit. |
| quality_gate | `codebook_rows` | 81 | 75 | 108.0% | pass | Use canonical values from the codebook for all coded fields. |
| claim_gate | `promote_candidate_claims` | 0 | 8 | 0.0% | not_started | Promote no claim until acceptance criteria pass. |

## Claim Actions

| Priority | Claim | Decision | Sprint | Review | Notes | Next action |
| ---: | --- | --- | --- | ---: | ---: | --- |
| 1 | `C01` LLM reasoning center of gravity | not_ready | sprint_01 | 0/8 | 0/4 | Fill first-sprint paper notes, then transfer decisions through the overlay bridge. |
| 1 | `C02` Infrastructure and agentic workloads | not_ready | sprint_01 | 0/8 | 0/4 | Fill first-sprint paper notes, then transfer decisions through the overlay bridge. |
| 1 | `C03` Program committee attention | not_ready | sprint_01 | 0/8 | 0/4 | Fill first-sprint paper notes, then transfer decisions through the overlay bridge. |
| 1 | `C07` Artifact visibility | not_ready | sprint_01 | 0/8 | 0/4 | Fill first-sprint paper notes, then transfer decisions through the overlay bridge. |
| 2 | `C04` Public attention mismatch | not_ready | sprint_02 | 0/6 | 0/3 | Use sprint 02 paper notes, then transfer decisions through the sprint 02 overlay bridge. |
| 2 | `C05` Neighboring-venue contrast | not_ready | sprint_02 | 0/7 | 0/3 | Use sprint 02 paper notes, then transfer decisions through the sprint 02 overlay bridge. |
| 4 | `C06` External trend context | context_or_workflow_only | sprint_01 | 0/0 | 0/0 | Keep as framing/context; do not promote as a paper-quality claim. |
| 4 | `C08` Validation priority | context_or_workflow_only | sprint_01 | 0/0 | 0/0 | Keep as framing/context; do not promote as a paper-quality claim. |

## Execution Order

1. Fill sprint 01 paper notes for C01, C02, C03, and C07.
2. Run `python3 scripts/build_paper_note_overlay_bridge.py` and `python3 scripts/lint_manual_review_values.py`.
3. Transfer ready sprint 01 rows into claim and area overlays.
4. Fill sprint 02 notes for C04 and C05, then rebuild its overlay bridge.
5. Rebuild reviewed tables, progress, readiness, acceptance criteria, decision board, and validation.

## Outputs

- `data/processed/icml2026_review_execution_dashboard.csv`
- `data/processed/icml2026_review_execution_claim_actions.csv`
- `reports/icml2026_review_execution_dashboard.md`