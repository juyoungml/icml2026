# ICML 2026 Manual Review Workspace

This creates human-editable overlay files for manual review judgments.
Generated queue files in `data/processed/` should stay reproducible; fill the files in `data/manual/` instead.

## Files

- `data/manual/claim_review_overrides.csv` - 118 claim-review rows
- `data/manual/area_review_overrides.csv` - 192 area-review rows

## Current Write Status

- Claim overlay preserved
- Area overlay preserved

## Codebook

- Canonical values: `data/processed/icml2026_manual_review_codebook.csv`
- Human guide: `reports/icml2026_manual_review_codebook.md`

## How To Fill Claim Rows

- `manual_claim_support`: supports, partial_support, weakens, contradicts, not_applicable, unclear.
- `manual_taxonomy_judgment`: correct, too_broad, too_narrow, wrong_area, wrong_subarea, unclear.
- `manual_artifact_judgment`: not_applicable, none, linked_unchecked, live_checked, runnable, broken.
- `manual_notes`: concise evidence, caveat, or correction.

## How To Fill Area Rows

- `manual_validated`: yes, partial, no, unclear.
- `manual_primary_contribution_type`: method, theory, system, dataset, benchmark, analysis, application, survey_or_position, unclear.
- `manual_artifact_status`: none, linked_unchecked, live_checked, runnable, broken, not_applicable.
- `manual_fault_line_relevance`: headline, supporting, caveat, not_relevant, unclear.

## Rebuild After Editing

```bash
python3 scripts/lint_manual_review_values.py
python3 scripts/build_reviewed_validation_tables.py
python3 scripts/build_review_progress.py
python3 scripts/build_researcher_readiness_audit.py
python3 scripts/build_researcher_gap_audit.py
python3 scripts/build_area_briefing_cards.py
python3 scripts/build_static_dashboard.py
python3 scripts/build_project_index.py
python3 scripts/validate_workspace.py
```