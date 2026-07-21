# Scripts

All Python commands run through the locked `uv` environment. Run them from the
repository root.

## Public Experience

```bash
uv sync --locked
uv run python scripts/project.py site
uv run python scripts/project.py validate
```

Use `uv sync --locked --extra semantic` only when rebuilding transformer
embeddings. This keeps the normal website setup small and fast.

## Data Collection

- `fetch_icml_virtual.py`
- `fetch_alphaxiv_icml.py`
- `fetch_arxiv_trends.py`

## Landscape Analysis

- `analyze_icml_titles.py`
- `analyze_alphaxiv_icml.py`
- `build_cluster_landscape.py`
- `build_semantic_landscape.py`
- `build_manual_taxonomy_seed.py`
- `build_researcher_landscape.py`
- `build_collaboration_landscape.py`

## Evidence and Comparisons

- `build_paper_evidence_codes.py`
- `build_program_calibration.py`
- `build_historical_venue_baselines.py`
- `build_reproducibility_lens.py`
- `build_landscape_synthesis.py`

## Manual Review Workflow

- `build_researcher_review_plan.py`
- `build_review_sprint_packet.py`
- `build_manual_review_workspace.py`
- `build_reviewed_validation_tables.py`
- `build_review_progress.py`
- `lint_manual_review_values.py`

## Navigation and QA

- `build_project_index.py`
- `validate_workspace.py`

Individual scripts remain available for focused work. Prefer `project.py` for
the common build and validation paths so local runs and continuous integration
use the same commands.
