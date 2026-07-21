# ICML 2026 Manual Review Codebook

Canonical value guide for paper notes and manual review overlays.
Use these values when filling `data/manual/` files so downstream acceptance gates interpret the review consistently.

## Quick Rules

- Use `partial_support`, not `mixed`, for a claim that is directionally supportive but too broad.
- Use `linked_unchecked`, `live_checked`, `runnable`, or `broken` for artifacts; avoid free-text artifact states in coded fields.
- Put nuance, caveats, and direct evidence in `manual_notes` or `paper_note` rather than inventing new coded values.
- A row can be reviewed but still not support promotion; `unclear`, `not_applicable`, `weakens`, and `contradicts` are valid reviewed outcomes.

## Field Values

### `area_overlay.manual_artifact_status`

| Value | Meaning | When to use | Promotion effect |
| --- | --- | --- | --- |
| `none` | No artifact found. | Use after checking. | Weakens artifact claims. |
| `linked_unchecked` | Artifact link exists but was not inspected. | Use as temporary state. | Does not satisfy artifact inspection. |
| `live_checked` | Artifact link is live. | Use after opening the link. | Supports artifact visibility, not reproducibility. |
| `runnable` | Artifact appears runnable or reproducible. | Use after inspecting setup/data/checkpoints. | Strong artifact support. |
| `broken` | Artifact is stale, private, or unusable. | Use after failed direct check. | Weakens artifact claims. |
| `not_applicable` | Artifact is irrelevant to paper type. | Use for pure theory/position papers. | Neutral. |

### `area_overlay.manual_fault_line_relevance`

| Value | Meaning | When to use | Promotion effect |
| --- | --- | --- | --- |
| `headline` | Paper is strong enough to anchor an area fault line. | Use sparingly for best examples. | Candidate report example. |
| `supporting` | Paper supports but should not anchor the fault line. | Use for secondary examples. | Supports area synthesis. |
| `caveat` | Paper mainly adds a caveat or boundary condition. | Use for limitations, failures, or mixed evidence. | Improves critical analysis. |
| `not_relevant` | Paper should not be used for this area fault line. | Use for irrelevant/misclassified rows. | Does not support area synthesis. |
| `unclear` | Fault-line relevance is unresolved. | Use when another review pass is needed. | Does not support promotion. |

### `area_overlay.manual_primary_contribution_type`

| Value | Meaning | When to use | Promotion effect |
| --- | --- | --- | --- |
| `method` | Main contribution is an algorithm, architecture, model, or training method. | Use for mechanism-first papers. | Helps contribution-mix analysis. |
| `theory` | Main contribution is formal analysis/proof. | Use for theory papers. | Helps program-attention analysis. |
| `system` | Main contribution is infrastructure, serving, tooling, or integrated system. | Use for systems/agents workflows. | Helps systems/agentic workload claims. |
| `dataset` | Main contribution is data collection, dataset, or resource. | Use when data resource is central. | Helps benchmark/data claims. |
| `benchmark` | Main contribution is benchmark/evaluation suite. | Use for evaluation-package papers. | Important for C04/C05 interpretation. |
| `analysis` | Main contribution is empirical or conceptual analysis. | Use for diagnostic/measurement papers. | Often supports caveats or fault lines. |
| `application` | Main contribution is an applied use case. | Use when method novelty is secondary. | Supports area breadth, not necessarily core method claims. |
| `survey_or_position` | Main contribution is position, survey, or argument. | Use for position papers. | Useful for context, not empirical support. |
| `unclear` | Contribution type cannot be decided. | Use when review is inconclusive. | Does not support contribution-type claims. |

### `area_overlay.manual_result_character`

| Value | Meaning | When to use | Promotion effect |
| --- | --- | --- | --- |
| `positive` | Results primarily strengthen the area/fault-line story. | Use for clear wins or validated results. | Supports area synthesis. |
| `negative` | Results primarily show failures or limits. | Use for negative or cautionary papers. | Supports caveats. |
| `mixed` | Results are mixed across settings. | Use when paper should narrow a claim. | Supports nuanced claims. |
| `theoretical` | Result is mainly theoretical. | Use for theory/proof papers. | Useful for program/theory synthesis. |
| `benchmark_only` | Result is mainly benchmark/data packaging. | Use for dataset/benchmark papers. | Useful for evaluation landscape claims. |
| `unclear` | Result character cannot be decided. | Use when additional reading is needed. | Does not support promotion. |

### `area_overlay.manual_validated`

| Value | Meaning | When to use | Promotion effect |
| --- | --- | --- | --- |
| `yes` | Paper validates assigned area/subarea and area claim use. | Use when assignment and evidence are clear. | Supports area-level use. |
| `partial` | Paper partly validates area use but needs caveat. | Use for boundary papers. | Supports area use with caveat. |
| `no` | Paper should not validate the assigned area/fault line. | Use for misclassified or irrelevant examples. | Weakens area claim. |
| `unclear` | Area validation is unresolved. | Use when more review is needed. | Does not support promotion. |

### `claim_overlay.manual_artifact_judgment`

| Value | Meaning | When to use | Promotion effect |
| --- | --- | --- | --- |
| `not_applicable` | Artifact check is irrelevant to this claim/paper. | Use for theory/position or non-artifact claims. | Neutral. |
| `none` | No artifact found. | Use after checking source links. | Does not satisfy artifact gate. |
| `linked_unchecked` | Artifact link exists but was not inspected. | Use as a temporary state. | Does not satisfy artifact gate. |
| `live_checked` | Artifact link was opened and is live. | Use after a live check. | Counts toward artifact gate. |
| `runnable` | Artifact appears runnable/reproducible. | Use after inspecting setup or examples. | Counts toward artifact gate. |
| `broken` | Artifact link or repository is unusable. | Use after direct inspection. | Counts as checked but weakens artifact claim. |

### `claim_overlay.manual_claim_support`

| Value | Meaning | When to use | Promotion effect |
| --- | --- | --- | --- |
| `supports` | Paper materially supports the linked synthesis claim. | Use when reviewed evidence directly supports the claim wording. | Counts as support in acceptance criteria. |
| `partial_support` | Paper supports a narrower or caveated version of the claim. | Use when the claim is directionally right but too broad. | Counts as support, but manual_notes should carry caveat. |
| `weakens` | Paper complicates or weakens the linked claim. | Use for contrary evidence, scope limits, or mismatch. | Counts as weakening; blocks promotion while unresolved. |
| `contradicts` | Paper directly contradicts the linked claim. | Use for clear counterexamples. | Counts as weakening; should trigger claim revision. |
| `not_applicable` | Paper should not be used for this claim. | Use when paper is in queue but does not bear on the claim. | Reviewed but not support. |
| `unclear` | Reviewer cannot decide claim relationship. | Use when further review is needed. | Reviewed but not support. |

### `claim_overlay.manual_taxonomy_judgment`

| Value | Meaning | When to use | Promotion effect |
| --- | --- | --- | --- |
| `correct` | Taxonomy assignment is acceptable for this claim. | Use when area/subarea supports the claim linkage. | Helps taxonomy gates pass. |
| `too_broad` | Claim/taxonomy grouping is overly broad for this paper. | Use when the paper fits only a narrower slice. | Blocks taxonomy-sensitive promotion. |
| `too_narrow` | Claim/taxonomy grouping misses broader relevance. | Use when paper spans more than assigned category. | Requires caveat or taxonomy revision. |
| `wrong_area` | Report-level area assignment is wrong. | Use for clear area mismatch. | Blocks taxonomy-sensitive promotion. |
| `wrong_subarea` | Subarea assignment is wrong but area may be acceptable. | Use for subarea mismatch. | Blocks subarea claims and adds caveat to area claims. |
| `unclear` | Taxonomy relationship is unresolved. | Use when taxonomy needs another reviewer. | Blocks taxonomy-sensitive promotion. |

### `paper_notes.artifact_status_checked`

| Value | Meaning | When to use | Promotion effect |
| --- | --- | --- | --- |
| `none` | No artifact link or release was found. | Use after checking metadata/PDF sufficiently. | Weakens artifact-visibility claims when a release is expected. |
| `linked_unchecked` | Artifact link exists but was not opened or inspected. | Use only as a triage state. | Does not satisfy artifact check gates. |
| `live_checked` | Artifact/repository link was opened and exists. | Use after checking live status, license/release details optional. | Counts toward artifact inspection but not runnable status. |
| `runnable` | Artifact appears runnable or includes clear reproduction instructions. | Use only after inspecting repository contents. | Strongest artifact support. |
| `broken` | Artifact link is stale, private, missing, or unusable. | Use after a direct check. | Weakens artifact/reproducibility claims. |
| `not_applicable` | Artifact is not expected for this paper type. | Use for pure theory/position papers or cases where release is irrelevant. | Neutral for artifact claims. |

### `paper_notes.evidence_strength`

| Value | Meaning | When to use | Promotion effect |
| --- | --- | --- | --- |
| `strong` | Claim is backed by credible baselines, metrics, ablations, and limitations. | Use when evidence would survive direct citation in a report. | Good candidate for support_rows when claim implication supports the claim. |
| `moderate` | Evidence is useful but has gaps or limited scope. | Default for credible but not definitive papers. | Can support claims with caveats. |
| `weak` | Evidence is thin, undercompared, or mostly qualitative. | Use when paper should be a caveat or low-confidence example. | Usually should not count as strong support. |
| `negative_or_mixed` | Evidence complicates, narrows, or contradicts a simple claim. | Use when results show limits, failure modes, or mixed outcomes. | May become a weakening row or caveat example. |
| `unclear` | Evidence could not be classified. | Use when source did not provide enough information in checked sections. | Blocks promotion for that row. |

### `paper_notes.final_report_use`

| Value | Meaning | When to use | Promotion effect |
| --- | --- | --- | --- |
| `headline_example` | Paper can anchor a report claim. | Use only when contribution and evidence are clear. | Strong candidate for final narrative. |
| `supporting_example` | Paper supports a claim but should not anchor it. | Use for useful but less central examples. | Good support row with caveats. |
| `caveat_example` | Paper mainly complicates or narrows a claim. | Use when it exposes limits or counterexamples. | Useful for critical analysis; may weaken promotion. |
| `exclude` | Paper should not be used in final report synthesis. | Use for irrelevant, weak, or misclassified examples. | Does not support promotion. |
| `undecided` | Reviewer has not decided report role. | Use when additional review is needed. | Weak support until resolved. |

### `paper_notes.novelty_judgment`

| Value | Meaning | When to use | Promotion effect |
| --- | --- | --- | --- |
| `new_problem` | Paper primarily opens or reframes a problem. | Use when contribution is mostly problem definition, benchmark framing, or position. | Can support trend/fault-line claims but not necessarily method-strength claims. |
| `new_method` | Paper introduces a new mechanism, algorithm, architecture, or training recipe. | Use when the technical mechanism is the main contribution. | Can support method-centered synthesis claims. |
| `stronger_theory` | Paper primarily contributes theorem/proof/analysis strength. | Use for theory or formal-analysis papers. | Useful for program-attention and theory-area claims. |
| `better_system` | Paper primarily improves efficiency, scale, tooling, or systems integration. | Use for infrastructure, serving, tooling, or agent workflow papers. | Useful for systems/agentic workload claims. |
| `benchmark_package` | Paper primarily contributes benchmark/data/evaluation packaging. | Use when benchmark/data are central rather than a side artifact. | Can support public-attention or reproducibility claims with caveats. |
| `incremental` | Contribution appears mostly incremental relative to cited baselines. | Use when evidence does not justify headline-example status. | Usually weakens headline use. |
| `unclear` | Reviewer cannot confidently classify novelty. | Use when the paper needs a second read or specialist review. | Blocks promotion unless other reviewed rows are strong. |

### `paper_notes.paper_read_status`

| Value | Meaning | When to use | Promotion effect |
| --- | --- | --- | --- |
| `abstract_only` | Only abstract/title/metadata were checked; use only for triage. | Use when the PDF was not opened but the paper remains in the sprint. | Counts as a started note, but is weak evidence for claim promotion. |
| `skimmed` | Main paper was skimmed but not fully checked. | Use after checking intro/method/results enough to summarize the contribution. | Counts as a note; reviewer should mark evidence_strength conservatively. |
| `read_main` | Main paper body was read; appendix may remain unchecked. | Default target for sprint review. | Good enough for most claim/area overlay decisions. |
| `read_full` | Main paper and relevant appendix/artifact details were checked. | Use for artifact, theory, benchmark, or controversial claim examples. | Strongest paper-note status. |
| `blocked` | Paper could not be reviewed because source access or content was unavailable. | Use only with a reason in paper_note. | Does not support promotion. |

### `paper_notes.taxonomy_correction`

| Value | Meaning | When to use | Promotion effect |
| --- | --- | --- | --- |
| `keep` | Current area/subarea assignment is acceptable. | Use when taxonomy evidence matches the paper's main contribution. | Helps satisfy taxonomy gates. |
| `relabel_area` | Paper belongs in a different report-level area. | Use for clear area mismatch. | Blocks taxonomy-sensitive claim promotion until resolved. |
| `relabel_subarea` | Area is acceptable but subarea should change. | Use for boundary or submode corrections. | Caveat for subarea-level claims. |
| `split_boundary` | Paper genuinely spans multiple areas/subareas. | Use when no single assignment is clearly dominant. | Use as a caveat for aggregate area claims. |
| `unclear` | Taxonomy cannot be decided from reviewed material. | Use when reviewer needs more context. | Blocks taxonomy-sensitive promotion. |

## Transfer Pattern

1. Fill paper-note fields from the PDF/ICML page/repository.
2. Rebuild the relevant overlay bridge.
3. Copy only coded decisions into overlay fields.
4. Put sentence-level evidence and caveats in `manual_notes`.
5. Rebuild reviewed tables, progress, readiness, acceptance criteria, decision board, and validation.

## Outputs

- `data/processed/icml2026_manual_review_codebook.csv`
- `reports/icml2026_manual_review_codebook.md`