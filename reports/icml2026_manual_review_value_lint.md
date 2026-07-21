# ICML 2026 Manual Review Value Lint

Checks non-empty coded manual review fields against `data/processed/icml2026_manual_review_codebook.csv`.
Blank fields are allowed and mean the row has not been reviewed yet.

## Summary

- Files checked: 4
- Coded values checked: 0
- Invalid coded values: 0

## Files

| File | Table | Rows | Coded fields | Rows with coded values | Checked values | Invalid values |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `data/manual/claim_review_overrides.csv` | claim_overlay | 118 | 3 | 0 | 0 | 0 |
| `data/manual/area_review_overrides.csv` | area_overlay | 192 | 5 | 0 | 0 | 0 |
| `data/manual/icml2026_review_sprint_01_paper_notes.csv` | paper_notes | 40 | 6 | 0 | 0 | 0 |
| `data/manual/icml2026_review_sprint_02_paper_notes.csv` | paper_notes | 16 | 6 | 0 | 0 | 0 |

## Invalid Values

No invalid coded values found.

## Outputs

- `data/processed/icml2026_manual_review_value_lint.csv`
- `data/processed/icml2026_manual_review_value_lint_summary.csv`
- `reports/icml2026_manual_review_value_lint.md`