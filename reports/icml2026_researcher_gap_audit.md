# ICML 2026 Researcher Gap Audit

Critical feedback on what remains before this workspace becomes a high-confidence ML research landscape brief.

## Snapshot

- Official corpus rows: 6628
- Manual validation reviewed: 0/310 (0.0%)
- Manual review codebook rows: 81
- Manual review invalid coded values: 0
- Review execution metrics tracked: 9
- Active review execution claim actions queued: 6/8
- Unique papers in the review plan: 224
- Paper-by-claim decision tasks queued: 75
- Sprint papers with source-access rows: 56
- Priority PDFs probed for extractability: 8
- Page-level PDF review cards: 8
- PDF review worksheet rows: 8
- Focused PDF review transfer rows: 23
- First-sprint paper notes started: 0/40
- Paper-note overlay transfer rows queued: 94
- Sprint 02 uncovered-claim papers queued: 16
- Sprint 02 overlay transfer rows queued: 35
- High-priority unreviewed claims: 3
- High-risk areas: 11
- Structural validation failures: 0
- Claims passing acceptance criteria: 0/8
- Claims with first-sprint decision-board bridge rows: 6/8
- Public/program divergence papers queued: 111
- Taxonomy clusters queued for adjudication: 21
- Artifact audit papers queued: 160
- Baseline sensitivity rows queued: 12

## Critical Feedback

| Priority | Gap | Why it matters | Current signal | Next action |
| ---: | --- | --- | --- | --- |
| 1 | No human judgments have been merged yet | The workspace is broad, but paper-level support for synthesis claims is still unverified. | 0/310 reviewed rows (0.0%); 81 canonical codebook rows available; 0 invalid coded values | Complete the first 40-paper review sprint, then rerun reviewed tables, progress, readiness, and validation. |
| 2 | Abstract/title evidence is not enough for novelty and method claims | A researcher needs to know what is technically new, what is borrowed, and what is only benchmark packaging. | 224 unique papers queued; 75 paper-by-claim decision tasks defined; 56 sprint papers have source-access rows; 8 priority PDFs probed for extractability; 8 page-level PDF review cards generated; 8 reviewer worksheet rows prepared; 23 focused transfer rows prepared; 0/40 first-sprint paper notes started; 94 sprint-01 transfer rows and 35 sprint-02 transfer rows queued | For the top-ranked papers, extract the claimed contribution, core method, baselines, ablations, and failure cases from the PDF. |
| 3 | Area taxonomy is useful but still partially heuristic | The 12-area map is readable, but boundary clusters can distort area shares and trend claims. | 11 high-risk area rows; 21 semantic clusters queued for adjudication | Resolve taxonomy-boundary rows before making subarea share claims or ranking areas by importance. |
| 4 | AlphaXiv votes are attention, not quality | Popular papers may be demos, infrastructure, or already-famous topics rather than the strongest technical work. | AlphaXiv is joined to all official paper rows; 111 papers queued for public/program calibration reading. | Read the public/program divergence set and label whether attention tracks novelty, utility, accessibility, or hype. |
| 5 | Reproducibility is still URL visibility | A GitHub link is not evidence that code runs, data are available, or results are reproducible. | Artifact fields are useful for triage; 160 papers queued for artifact/repository audit. | Manually inspect high-signal GitHub-linked papers before writing reproducibility claims. |
| 6 | Historical and arXiv baselines are context, not causal evidence | Accepted-paper baselines and broad arXiv queries can show direction, but they can mislead on venue policy or field momentum. | Trend and historical reports exist; 12 area-level baseline sensitivity rows queued for spot-checking. | Spot-check largest positive/negative deltas and test alternate query terms before using trend claims. |
| 7 | The thesis hierarchy exists, but it is still mostly unpromoted | The project has many artifacts; a reader needs a small number of defensible claims with clear evidence status. | 8 claims mapped; 3 high-priority unreviewed claims; 6/8 active claim actions queued; 6/8 claims have first-sprint bridge rows; 16 sprint-02 papers cover C04/C05 | After the first sprint, promote only checked claims into the overview seed and demote the rest to hypotheses. |
| 8 | Semantic validation gates exist, but no claim passes them yet | Passing row-count and coverage checks does not prove the interpretations are correct. | 274 automated checks, 0 failures; 9 execution metrics tracked; 0/8 claims promotable | Keep structural validation, but add claim-level acceptance criteria once manual review fields are filled. |

## Researcher-Grade Target State

- A checked thesis map where every headline claim points to reviewed paper rows.
- Paper notes for the first sprint that separate novelty, method, evidence, limitations, and artifact status.
- A resolved taxonomy-boundary log for the areas most likely to drive the report narrative.
- Explicit calibration for public attention versus program selection.
- Reproducibility claims based on repository inspection, not link existence.

## Outputs

- `data/processed/icml2026_researcher_gap_audit.csv`
- `reports/icml2026_researcher_gap_audit.md`