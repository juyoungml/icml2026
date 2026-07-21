# xKV: Cross-Layer KV-Cache Compression via Aligned Singular Vector Extraction

- Sprint: `sprint_01` rank 33
- Global review rank: 33
- Event ID: `63436`
- Area: Systems and Efficient Foundation Models / Long-context attention and KV-cache compression
- Target claims: C02; C06
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: votes=518; github_stars=52; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/63436) / [AlphaXiv](https://www.alphaxiv.org/abs/2503.18893) / [GitHub](https://github.com/abdelfattah-lab/xKV)

## Where To Record Judgments

- Claim overlay keys: C02::63436 | C06::63436
- Area overlay keys: Systems and Efficient Foundation Models::63436
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet 1](../claim_validation_packets/c02-infrastructure-and-agentic-workloads.md), [claim packet 2](../claim_validation_packets/c06-external-trend-context.md)
- Claim dossiers: [claim dossier 1](../claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md), [claim dossier 2](../claim_evidence_dossiers/c06-external-trend-context.md)
- Area packet: [area packet](../validation_packets/systems-and-efficient-foundation-models.md)
- Area briefing: [area briefing](../area_briefing_cards/systems-and-efficient-foundation-models.md)

## What To Verify

- Contribution: System / infrastructure: We show, via Centered Kernel Alignment (CKA), that the dominant singular vectors of KV-Cache are well aligned across layers.
- Method: Tags: LLM post-training; Agents / tool use; Transformer / attention; Compression / efficiency; setting: math/code/verifiable; language/llm; abstract cues: no obvious abstract keyword cue.
- Evidence: metrics: accuracy; latency; throughput; memory; check theorem assumptions and empirical/theory split
- Taxonomy: Check whether public signal reflects core infrastructure/agent workloads or broad LLM spillover. | Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable. C06 (External trend context): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality.

## Abstract Excerpt

Long-context Large Language Models (LLMs) enable powerful applications but incur high memory costs due to the key–value states (KV-Cache). Recent studies attempt to share KV-Cache across layers, but these approaches either require expensive pretraining or rely on per-token cross-layer cosine similarity that is often limited in practice. We show, via Centered Kernel Alignment (CKA), that the dominant singular vectors of KV-Cache are well aligned across layers. Motivated by this observation, we propose xKV, a post-training compression method that jointly factorizes grouped-layer KV-Cache into a shared low-rank subspace, substantially reducing KV-Cache memory. Across widely used LLMs, xKV...

## Suggested Note Seed

Contribution: System / infrastructure: We show, via Centered Kernel Alignment (CKA), that the dominant singular vectors of KV-Cache are well aligned across layers. Evidence to verify: metrics: accuracy; latency; throughput; memory; check theorem assumptions and empirical/theory split Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable. C06 (External trend context): decide supports / weakens / complicates / not_applicable.

## Minimum Manual Fields

- `paper_read_status`
- `contribution_summary`
- `novelty_judgment`
- `method_summary`
- `evidence_strength`
- `baselines_checked`, `datasets_checked`, `metrics_checked`
- `limitations`
- `artifact_status_checked`
- `claim_implications`
- `taxonomy_correction`
- `final_report_use`