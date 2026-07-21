# Development Guide

## Requirements

- [`uv`](https://docs.astral.sh/uv/) 0.11.7 or newer
- Python 3.12, installed and managed by `uv`
- GitHub CLI for publishing and repository administration

Install the exact locked environment:

```bash
uv sync --locked
```

## Rebuild the Public Experience

```bash
uv run python scripts/project.py site
uv run python scripts/project.py validate
```

For transformer-based semantic embeddings, opt into the heavy dependencies:

```bash
uv sync --locked --extra semantic
uv run python scripts/build_semantic_landscape.py
```

## Main Analysis Stages

1. Fetch and normalize official ICML metadata.
2. Join AlphaXiv attention and visible artifact metadata.
3. Build lexical and semantic clusters.
4. Map clusters into the 12-area project taxonomy.
5. Generate evidence tags, comparisons, and reading queues.
6. Build reports, figures, dashboard, course, and public site.
7. Run structural and learning-product validation.

The complete command catalog is documented in [`scripts/README.md`](../scripts/README.md).

## Validation

```bash
uv run ruff check scripts
uv run python scripts/project.py validate
```

The validator checks corpus invariants, taxonomy coverage, report and figure presence, learning-path structure, quiz coverage, slide structure, public-site assets, and navigation links.

The course pages are generated from `scripts/learning_content.py`, the shared
area and paper catalog, and processed briefing tables. Edit the structured
teaching source, then rebuild; do not hand-edit files under `docs/learn/`.

The release criteria are documented in [`QUALITY_STANDARDS.md`](QUALITY_STANDARDS.md).

## Generated and Manual Files

- Edit files under `data/manual/` when recording human paper judgments.
- Avoid directly editing generated CSVs and reports unless you are changing their generator.
- Rebuild downstream artifacts after changing taxonomy rules or manual overlays.
- Raw downloads and cached PDFs are intentionally excluded from Git.
