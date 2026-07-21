# Contributing

Thank you for helping improve the ICML 2026 Landscape project.

## Good Contributions

- correct a paper classification or broken link;
- improve a plain-language explanation;
- add accessibility or mobile improvements;
- propose a better representative paper with evidence;
- complete a manual validation row;
- improve tests, data provenance, or reproducibility.

## Before Opening a Pull Request

1. Keep factual claims tied to a local data source or paper.
2. Separate checked facts, directional patterns, and open questions.
3. Do not describe AlphaXiv attention as research quality.
4. Do not describe an artifact link as reproducibility without inspection.
5. Run `uv sync --locked`.
6. Run `uv run ruff check scripts` and `uv run python scripts/project.py validate`.
6. Explain what changed, why it changed, and how it was checked.

For content corrections, an issue with the paper title, event ID, current statement, proposed statement, and supporting source is enough to begin.
