# ICML 2026 Paper Note Workspace

Human-editable paper-note sheet for the first review sprint.
Use this to capture researcher judgments that are too rich for the claim and area overlay fields.

## Snapshot

- Sprint papers: 40
- Paper notes started: 0/40
- Manual field values preserved during rebuild: 0
- Force overwrite used: no

## File

- `data/manual/icml2026_review_sprint_01_paper_notes.csv`
- Suggested starting prompts: `data/processed/icml2026_sprint_prereview_suggestions.csv`
- Overlay transfer checklist: `data/processed/icml2026_paper_note_overlay_bridge.csv`
- Canonical codebook: `reports/icml2026_manual_review_codebook.md`

## Fields To Fill

- `paper_read_status`: abstract_only, skimmed, read_main, read_full, blocked.
- `contribution_summary`: one or two sentences on what the paper actually contributes.
- `novelty_judgment`: new_problem, new_method, stronger_theory, better_system, benchmark_package, incremental, unclear.
- `method_summary`: compact mechanism-level description, not just the title phrasing.
- `evidence_strength`: strong, moderate, weak, negative_or_mixed, unclear.
- `baselines_checked`, `datasets_checked`, `metrics_checked`: what was actually compared or measured.
- `limitations`: stated or inferred limitations that should affect the report narrative.
- `artifact_status_checked`: none, linked_unchecked, live_checked, runnable, broken, not_applicable.
- `claim_implications`: how the paper changes the linked synthesis claim(s).
- `taxonomy_correction`: keep, relabel_area, relabel_subarea, split_boundary, unclear.
- `final_report_use`: headline_example, supporting_example, caveat_example, exclude, undecided.

## How This Fits The Workflow

1. Fill paper notes while reading the top-40 sprint papers.
2. Use the pre-review suggestions as hypotheses, not as checked judgments.
3. Rebuild the paper-note overlay bridge.
4. Transfer direct claim/area judgments into the overlay files listed in the bridge rows.
5. Rebuild reviewed tables, progress, readiness, gap audit, dashboard, and validation.

```bash
python3 scripts/build_manual_review_codebook.py
python3 scripts/build_paper_note_overlay_bridge.py
python3 scripts/lint_manual_review_values.py
python3 scripts/build_reviewed_validation_tables.py
python3 scripts/build_review_progress.py
python3 scripts/build_researcher_readiness_audit.py
python3 scripts/build_researcher_gap_audit.py
python3 scripts/build_project_index.py
python3 scripts/validate_workspace.py
```