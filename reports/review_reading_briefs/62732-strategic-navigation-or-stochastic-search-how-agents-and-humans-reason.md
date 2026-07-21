# Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections

- Sprint: `sprint_01` rank 39
- Global review rank: 39
- Event ID: `62732`
- Area: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Target claims: C02
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: oral; votes=26; github_stars=1; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/62732) / [AlphaXiv](https://www.alphaxiv.org/abs/2603.12180) / [GitHub](https://github.com/Snowflake-Labs/MADQA)

## Where To Record Judgments

- Claim overlay keys: C02::62732
- Area overlay keys: Agents, Code, and Tool Use::62732
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c02-infrastructure-and-agentic-workloads.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md)
- Area packet: [area packet](../validation_packets/agents-code-and-tool-use.md)
- Area briefing: [area briefing](../area_briefing_cards/agents-code-and-tool-use.md)

## What To Verify

- Contribution: Benchmark / evaluation: To address this, we introduce Agentic Document VQA, a benchmark of 2,250 human-authored questions grounded in 800 heterogeneous PDF documents.
- Method: Tags: Reasoning / test-time compute; Agents / tool use; setting: language/llm; theory/synthetic; abstract cues: benchmark; theory; dataset; agent; multimodal.
- Evidence: benchmarks: VQA; metrics: accuracy; check human-study or user-evaluation setup
- Taxonomy: Check whether program-selected papers substantiate systems/agents emphasis.
- Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness.

## Abstract Excerpt

Multimodal agents offer a compelling path to automating complex document-intensive workflows, yet a critical question remains: do these architectures demonstrate genuine strategic reasoning, or simply conduct stochastic trial-and-error search? To address this, we introduce Agentic Document VQA, a benchmark of 2,250 human-authored questions grounded in 800 heterogeneous PDF documents. Guided by *Classical Test Theory*, we design it to maximize discriminative power and reliably differentiate between varying levels of agent capability. To rigorously assess agentic behaviour, we introduce a novel evaluation protocol for measuring the accuracy-effort trade-off. Using this framework, we find...

## Suggested Note Seed

Contribution: Benchmark / evaluation: To address this, we introduce Agentic Document VQA, a benchmark of 2,250 human-authored questions grounded in 800 heterogeneous PDF documents. Evidence to verify: benchmarks: VQA; metrics: accuracy; check human-study or user-evaluation setup Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable.

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