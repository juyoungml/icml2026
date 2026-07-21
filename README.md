# ICML 2026 Landscape

A guided, evidence-aware introduction to the major research directions represented at ICML 2026.

This project turns 6,628 conference paper records into a friendly learning experience with a technical slide deck, an interactive quiz, a searchable dashboard, and reproducible analysis scripts.

## Start Here

- **Public website:** [juyoungml.github.io/icml2026](https://juyoungml.github.io/icml2026/)
- **Technical slides:** [47-slide HTML deck](docs/icml2026_newcomer_slides.html)
- **Interactive quiz:** [Multiple-choice knowledge check](docs/quiz.html)
- **Landscape explorer:** [Searchable dashboard](docs/dashboard.html)
- **Technical course:** [Foundations, 12 area lessons, synthesis, and mastery checks](docs/learn.html)

## What You Will Learn

- The 12 broad research areas in the current project taxonomy
- Six patterns shaping the ICML 2026 story
- How paper share, program selection, public attention, venue comparison, and artifact visibility differ
- How representative papers support—or complicate—conference-level claims
- How to discuss uncertainty without losing the main story

## Repository Map

| Path | Purpose |
| --- | --- |
| [`docs/`](docs/) | Public website, slides, roadmap, and quiz |
| [`reports/`](reports/) | Research synthesis, validation packets, and paper briefs |
| [`data/`](data/) | Manual overlays and processed analysis tables |
| [`figures/`](figures/) | Generated charts used by the site and reports |
| [`scripts/`](scripts/) | Repeatable collection, analysis, site, and validation tools |

See [Project Structure](docs/PROJECT_STRUCTURE.md) for a detailed guide and [Development Guide](docs/DEVELOPMENT.md) for rebuilding the workspace.

Python is managed entirely with `uv`. The standard local check is:

```bash
uv sync --locked
uv run python scripts/project.py validate
```

## Evidence Status

Official corpus counts and program labels are the strongest evidence in the project. Taxonomy boundaries, AlphaXiv attention, historical comparisons, heuristic evidence tags, and repository visibility require more care.

The manual claim and area review queues are not complete. The public materials therefore distinguish checked facts, directional patterns, and open questions.

## Contributing

Corrections, clearer explanations, accessibility improvements, paper suggestions, and validation work are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request.

## License and Data Notice

Original code and project-authored material are released under the [MIT License](LICENSE). Conference metadata, paper text, and third-party resources remain subject to their original terms. See [NOTICE.md](NOTICE.md).
