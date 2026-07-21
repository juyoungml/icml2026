# Project Structure

The repository has two layers: a small public learning surface and a larger reproducible research workspace.

## Public Learning Surface

| File | Purpose |
| --- | --- |
| `docs/index.html` | Public landing page |
| `docs/learn.html` | Course routes, progress, and module index |
| `docs/learn/` | Foundations, 12 generated area modules, and synthesis |
| `docs/quiz.html` | Interactive assessment with targeted module review |
| `docs/icml2026_newcomer_slides.html` | Self-contained technical slide deck |
| `docs/dashboard.html` | Searchable landscape explorer |
| `docs/about.html` | Method, evidence, and limitation notes |
| `docs/QUALITY_STANDARDS.md` | Public learning-product release rubric |
| `docs/assets/` | Shared site styles and scripts |

These are the files most visitors need.

## Research Workspace

### `data/`

- `manual/`: human-editable review overlays and paper notes
- `processed/`: normalized tables and generated analysis products
- `raw/`: downloaded source snapshots; excluded from GitHub because they are large and reproducible

### `reports/`

- newcomer teaching material
- landscape synthesis and area summaries
- claim and area validation packets
- paper-reading briefs
- review progress and quality audits

Start with [`reports/README.md`](../reports/README.md).

### `figures/`

Generated plots used by the dashboard, slides, and reports. See [`figures/README.md`](../figures/README.md).

### `scripts/`

Repeatable data collection, analysis, document generation, site generation, and validation tools. See [`scripts/README.md`](../scripts/README.md).

## Stable Generated Paths

Many generated reports remain in a flat directory because scripts and cross-report links depend on stable paths. Public visitors do not need to navigate that directory directly; the website and directory indexes provide the intended entry points.
