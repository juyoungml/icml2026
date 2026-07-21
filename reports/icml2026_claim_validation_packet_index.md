# ICML 2026 Claim Validation Packet Index

These packets convert the synthesis claim register into paper-level review tasks.
They are designed to answer: what exactly should a researcher read before trusting each landscape claim?

## Packets

- [C01: LLM reasoning center of gravity](claim_validation_packets/c01-llm-reasoning-center-of-gravity.md) - 14 papers
- [C02: Infrastructure and agentic workloads](claim_validation_packets/c02-infrastructure-and-agentic-workloads.md) - 14 papers
- [C03: Program committee attention](claim_validation_packets/c03-program-committee-attention.md) - 14 papers
- [C04: Public attention mismatch](claim_validation_packets/c04-public-attention-mismatch.md) - 12 papers
- [C05: Neighboring-venue contrast](claim_validation_packets/c05-neighboring-venue-contrast.md) - 14 papers
- [C06: External trend context](claim_validation_packets/c06-external-trend-context.md) - 16 papers
- [C07: Artifact visibility](claim_validation_packets/c07-artifact-visibility.md) - 16 papers
- [C08: Validation priority](claim_validation_packets/c08-validation-priority.md) - 18 papers

## Review Guidance

- Mark whether each paper supports, weakens, or is irrelevant to the associated synthesis claim.
- For boundary clusters, record whether the area/subarea should change.
- For artifact claims, distinguish runnable code, benchmark/data release, project page, template/index, and unavailable links.
- After review, copy checked judgments into `data/processed/icml2026_claim_validation_queue.csv` or a reviewed derivative.