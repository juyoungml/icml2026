# $\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment

- Sprint: `sprint_01` rank 24
- Global review rank: 24
- Event ID: `64377`
- Area: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Target claims: C02
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: oral; votes=89; github_stars=1569; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/64377) / [AlphaXiv](https://www.alphaxiv.org/abs/2506.07982) / [GitHub](https://github.com/sierra-research/tau2-bench)

## Where To Record Judgments

- Claim overlay keys: C02::64377
- Area overlay keys: Agents, Code, and Tool Use::64377
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c02-infrastructure-and-agentic-workloads.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md)
- Area packet: [area packet](../validation_packets/agents-code-and-tool-use.md)
- Area briefing: [area briefing](../area_briefing_cards/agents-code-and-tool-use.md)

## What To Verify

- Contribution: Benchmark / evaluation: In order to address this gap, we introduce $\tau^2$-bench, with four key contributions: 1.
- Method: Tags: Reasoning / test-time compute; Agents / tool use; setting: math/code/verifiable; robotics/embodied; language/llm; theory/synthetic; abstract cues: benchmark; agent; tool.
- Evidence: look for ablations; check human-study or user-evaluation setup; check sim-to-real or deployment evidence
- Taxonomy: Check whether program-selected papers substantiate systems/agents emphasis.
- Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness.

## Abstract Excerpt

Existing benchmarks for conversational AI agents simulate *single-control* environments, where only the AI agent can use tools to interact with the world, while the user remains a passive information provider. This differs from real-world scenarios like technical support, where users need to actively participate in modifying the state of the (shared) world. In order to address this gap, we introduce $\tau^2$-bench, with four key contributions: 1. A novel **Telecom dual-control domain** modeled as a Dec-POMDP, where both agent and user make use of tools to act in a shared, dynamic environment that tests both agent coordination and communication, 2. A **compositional task generator** that...

## Suggested Note Seed

Contribution: Benchmark / evaluation: In order to address this gap, we introduce $\tau^2$-bench, with four key contributions: 1. Evidence to verify: look for ablations; check human-study or user-evaluation setup; check sim-to-real or deployment evidence Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable.

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