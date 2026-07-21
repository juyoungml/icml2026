# Monitoring Monitorability

- Sprint: `sprint_01` rank 34
- Global review rank: 34
- Event ID: `62992`
- Area: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Target claims: C02
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: oral; votes=28; github_stars=2786; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/62992) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.18311) / [GitHub](https://github.com/nightscout/cgm-remote-monitor)

## Where To Record Judgments

- Claim overlay keys: C02::62992
- Area overlay keys: Agents, Code, and Tool Use::62992
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c02-infrastructure-and-agentic-workloads.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md)
- Area packet: [area packet](../validation_packets/agents-code-and-tool-use.md)
- Area briefing: [area briefing](../area_briefing_cards/agents-code-and-tool-use.md)

## What To Verify

- Contribution: Benchmark / evaluation: We propose three evaluation archetypes (intervention, process, and outcome-property), a new monitorability metric, and a broad evaluation suite.
- Method: Tags: Reasoning / test-time compute; Agents / tool use; setting: robotics/embodied; abstract cues: agent.
- Evidence: check theorem assumptions and empirical/theory split
- Taxonomy: Check whether program-selected papers substantiate systems/agents emphasis.
- Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness.

## Abstract Excerpt

Safe deployment of increasingly capable AI agents may require visibility into how they make decisions. Chain-of-thought (CoT) monitoring can detect misbehavior in today’s reasoning models, but this “monitorability” may be fragile under different training procedures, data sources, or continued system scaling. We propose three evaluation archetypes (intervention, process, and outcome-property), a new monitorability metric, and a broad evaluation suite. We show CoT monitoring outperforms action-only monitoring in practical settings, and that frontier models are generally—but not perfectly—monitorable. We study scaling trends with pre-training model size and inference-time compute, finding...

## Suggested Note Seed

Contribution: Benchmark / evaluation: We propose three evaluation archetypes (intervention, process, and outcome-property), a new monitorability metric, and a broad evaluation suite. Evidence to verify: check theorem assumptions and empirical/theory split Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable.

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