# ICML 2026 Manual Review Progress

This report tracks whether the manual review queues have actually been filled.
A blank manual field means the relevant claim, evidence tag, taxonomy assignment, or artifact judgment is still unchecked.

## Snapshot

- Claim-validation rows reviewed: 0/118 (0.0%)
- Area-validation rows reviewed: 0/192 (0.0%)
- Total remaining review rows: 310

## Claim Review Progress

| Claim | Rows | Reviewed | Remaining | Program/Award | Taxonomy Review | GitHub |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| C08 | 18 | 0 | 18 | 7 | 18 | 13 |
| C06 | 16 | 0 | 16 | 0 | 6 | 14 |
| C07 | 16 | 0 | 16 | 1 | 4 | 16 |
| C01 | 14 | 0 | 14 | 8 | 12 | 11 |
| C02 | 14 | 0 | 14 | 7 | 5 | 14 |
| C03 | 14 | 0 | 14 | 14 | 3 | 5 |
| C05 | 14 | 0 | 14 | 4 | 1 | 9 |
| C04 | 12 | 0 | 12 | 3 | 0 | 9 |

## Area Review Progress

| Area | Rows | Reviewed | Remaining | Program/Award | Taxonomy Review | GitHub |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| AI for Science, Health, and Neuro | 16 | 0 | 16 | 10 | 13 | 9 |
| Agents, Code, and Tool Use | 16 | 0 | 16 | 10 | 5 | 13 |
| Data-Centric, Causal, and Federated ML | 16 | 0 | 16 | 10 | 12 | 8 |
| Generative Modeling | 16 | 0 | 16 | 8 | 0 | 6 |
| Graphs, Geometry, and Representation Learning | 16 | 0 | 16 | 6 | 12 | 6 |
| LLM Reasoning, Post-Training, and RLVR | 16 | 0 | 16 | 10 | 15 | 11 |
| Multimodal, Vision, and Perception | 16 | 0 | 16 | 10 | 4 | 8 |
| Reinforcement Learning and Control | 16 | 0 | 16 | 6 | 0 | 6 |
| Robotics, Embodiment, and World Models | 16 | 0 | 16 | 4 | 0 | 8 |
| Safety, Governance, Privacy, and Society | 16 | 0 | 16 | 10 | 0 | 4 |
| Systems and Efficient Foundation Models | 16 | 0 | 16 | 9 | 8 | 9 |
| Theory, Optimization, and Algorithms | 16 | 0 | 16 | 10 | 9 | 5 |

## Unreviewed Selection Mix

Claim-validation reasons:
- fast_arxiv_area_sample: 16
- program_high_public_lower: 14
- taxonomy_boundary_cluster_anchor: 12
- multimodal_high_attention: 10
- robotics_public_not_program: 9
- artifact_high_star: 9
- llm_boundary_cluster: 8
- systems_agents_program_signal: 7
- systems_agents_public_signal: 7
- artifact_manual_check: 7
- llm_high_attention_core: 6
- taxonomy_boundary_program_public_fill: 6
- multimodal_subarea_anchor: 4
- robotics_program_anchor: 3

Area-validation reasons:
- fault_line_representative: 72
- public_attention_not_program_signal: 48
- program_signal_low_public_attention: 33
- taxonomy_boundary_cluster: 21
- low_evidence_code_confidence: 18

## Recommended Review Order

1. Claim packets C01, C02, C03, and C07 because they support the main narrative and artifact claims.
2. Area packets for LLM Reasoning, Systems, Safety/Governance, Theory, and Multimodal/Vision because they anchor the report thesis.
3. Taxonomy-review rows before any subarea-level publication claim.
4. GitHub-linked rows with high stars or manual-check reasons before any reproducibility claim.

## Outputs

- `data/processed/manual_review_progress.csv`
- `data/processed/icml2026_claim_validation_reviewed.csv`
- `data/processed/icml2026_area_validation_reviewed.csv`
- `reports/manual_review_progress.md`