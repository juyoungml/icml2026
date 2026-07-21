# ICML 2026 Claim Validation Queue

This queue turns the landscape synthesis claim register into concrete paper-level review tasks.

## Snapshot

- Queue rows: 118
- Claims covered: 8
- Oral/award rows: 44
- Taxonomy-review rows: 49
- GitHub-linked rows: 91

## Claim Coverage

- C01 - LLM reasoning center of gravity: 14 papers
- C02 - Infrastructure and agentic workloads: 14 papers
- C03 - Program committee attention: 14 papers
- C04 - Public attention mismatch: 12 papers
- C05 - Neighboring-venue contrast: 14 papers
- C06 - External trend context: 16 papers
- C07 - Artifact visibility: 16 papers
- C08 - Validation priority: 18 papers

## Selection Reasons

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

## Outputs

- `data/processed/icml2026_claim_validation_queue.csv`
- `reports/icml2026_claim_validation_packet_index.md`
- `reports/claim_validation_packets/*.md`

## Caveats

- This is a review workflow artifact. Blank manual fields mean the claim has not been validated yet.
- Paper selections are designed for high-yield review, not statistical representativeness.
- Claim validation should be reconciled back into the claim register before publication or presentation.