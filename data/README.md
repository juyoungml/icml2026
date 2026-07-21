# Data

## `manual/`

Human-editable claim, area, and paper-review overlays. These are the authoritative place for manual judgments.

## `processed/`

Normalized tables and generated analysis products used by reports, figures, the dashboard, and validation.

Useful starting points:

- `icml2026_papers.csv`: official paper table
- `icml2026_manual_taxonomy_papers.csv`: paper-to-area mapping
- `icml2026_landscape_signal_matrix.csv`: area-level evidence summary
- `icml2026_paper_explorer.csv`: compact paper search table
- `workspace_validation_checks.csv`: machine-readable QA results

## `raw/`

Downloaded snapshots and cached PDFs. These files are reproducible, large, and excluded from GitHub.

See [`docs/data_dictionary.md`](../docs/data_dictionary.md) for generated schemas and row counts.

