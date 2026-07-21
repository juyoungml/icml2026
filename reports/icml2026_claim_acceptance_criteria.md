# ICML 2026 Claim Acceptance Criteria

Explicit promotion gates for synthesis claims.
This report turns semantic validation into checkable criteria rather than relying on broad structural validation.

## Snapshot

- Claims evaluated: 8
- Promotion candidates: 0
- Decision mix: context_or_workflow_only: 2, not_ready: 6

## Criteria Table

| Claim | Decision | Review | Support | Notes | Taxonomy | Artifact | Missing |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `C01` LLM reasoning center of gravity | not_ready | 0/8 | 0/5 | 0/4 | not_met | pass | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| `C02` Infrastructure and agentic workloads | not_ready | 0/8 | 0/5 | 0/4 | not_met | pass | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| `C03` Program committee attention | not_ready | 0/8 | 0/5 | 0/4 | not_met | pass | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| `C04` Public attention mismatch | not_ready | 0/6 | 0/4 | 0/3 | pass | pass | reviewed rows 0/6; support rows 0/4 with 0 weakening rows; paper notes 0/3 |
| `C05` Neighboring-venue contrast | not_ready | 0/7 | 0/4 | 0/3 | not_met | pass | reviewed rows 0/7; support rows 0/4 with 0 weakening rows; paper notes 0/3; taxonomy boundary unresolved |
| `C06` External trend context | context_or_workflow_only | 0/0 | 0/0 | 0/0 | pass | pass | none |
| `C07` Artifact visibility | not_ready | 0/8 | 0/5 | 0/4 | pass | not_met | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; artifact checks 0/5 |
| `C08` Validation priority | context_or_workflow_only | 0/0 | 0/0 | 0/0 | pass | pass | none |

## Claim-Specific Checks

### C01: LLM reasoning center of gravity

- Thesis role: `core_thesis_candidate`
- Decision: `not_ready`
- Allowed next use: Use as directional hypothesis or reading guide only.
- Special check: Boundary papers must confirm this is LLM reasoning/post-training rather than broad LLM infrastructure spillover.
- Missing for promotion: reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved

### C02: Infrastructure and agentic workloads

- Thesis role: `core_thesis_candidate`
- Decision: `not_ready`
- Allowed next use: Use as directional hypothesis or reading guide only.
- Special check: Historical-delta interpretation must survive a spot check of systems and agents/code examples.
- Missing for promotion: reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved

### C03: Program committee attention

- Thesis role: `core_thesis_candidate`
- Decision: `not_ready`
- Allowed next use: Use as directional hypothesis or reading guide only.
- Special check: Low-public/high-program papers must yield concrete technical reasons for committee attention.
- Missing for promotion: reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved

### C04: Public attention mismatch

- Thesis role: `supporting_hypothesis`
- Decision: `not_ready`
- Allowed next use: Use as directional hypothesis or reading guide only.
- Special check: High-attention robotics papers must be labeled as benchmark, demo, reusable model, or core algorithmic contribution.
- Missing for promotion: reviewed rows 0/6; support rows 0/4 with 0 weakening rows; paper notes 0/3

### C05: Neighboring-venue contrast

- Thesis role: `supporting_hypothesis`
- Decision: `not_ready`
- Allowed next use: Use as directional hypothesis or reading guide only.
- Special check: Multimodal/vision aggregate must be broken into submodes before interpreting the neighboring-venue contrast.
- Missing for promotion: reviewed rows 0/7; support rows 0/4 with 0 weakening rows; paper notes 0/3; taxonomy boundary unresolved

### C06: External trend context

- Thesis role: `context_frame`
- Decision: `context_or_workflow_only`
- Allowed next use: Use as context or workflow framing, not as a field-quality conclusion.
- Special check: Use only as external context; do not promote to a venue-quality or acceptance trend claim.
- Missing for promotion: none

### C07: Artifact visibility

- Thesis role: `supporting_hypothesis`
- Decision: `not_ready`
- Allowed next use: Use as directional hypothesis or reading guide only.
- Special check: Repository links must be manually inspected for runnable code, data/checkpoints, license, and stale/broken state.
- Missing for promotion: reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; artifact checks 0/5

### C08: Validation priority

- Thesis role: `workflow_claim`
- Decision: `context_or_workflow_only`
- Allowed next use: Use as context or workflow framing, not as a field-quality conclusion.
- Special check: Keep as a process/workflow claim; acceptance means the validation workflow remains explicit and auditable.
- Missing for promotion: none

## How To Use

- Do not promote a headline claim unless `decision` is `promote_candidate`.
- Treat `context_or_workflow_only` claims as framing, even when their criteria are structurally satisfied.
- When overlays and paper notes are filled, rerun this report before editing the overview seed.

## Outputs

- `data/processed/icml2026_claim_acceptance_criteria.csv`
- `reports/icml2026_claim_acceptance_criteria.md`