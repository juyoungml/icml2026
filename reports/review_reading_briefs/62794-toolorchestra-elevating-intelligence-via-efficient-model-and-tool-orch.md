# ToolOrchestra: Elevating Intelligence via Efficient Model and Tool Orchestration

- Sprint: `sprint_01` rank 31
- Global review rank: 31
- Event ID: `62794`
- Area: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Target claims: C02
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: votes=260; github_stars=745; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/62794) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.21689) / [GitHub](https://github.com/NVlabs/ToolOrchestra)

## Where To Record Judgments

- Claim overlay keys: C02::62794
- Area overlay keys: Agents, Code, and Tool Use::62794
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c02-infrastructure-and-agentic-workloads.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md)
- Area packet: [area packet](../validation_packets/agents-code-and-tool-use.md)
- Area briefing: [area briefing](../area_briefing_cards/agents-code-and-tool-use.md)

## What To Verify

- Contribution: Theory / proof: We show that small orchestrators managing other models and a variety of tools are able to both push the upper bound of intelligence and improve efficiency in solving difficult agentic tasks.
- Method: Tags: RL / policy optimization; LLM post-training; Reasoning / test-time compute; Agents / tool use; setting: language/llm; abstract cues: reinforcement learning; agent; tool.
- Evidence: metrics: accuracy; check theorem assumptions and empirical/theory split; check human-study or user-evaluation setup
- Taxonomy: Check whether public signal reflects core infrastructure/agent workloads or broad LLM spillover.
- Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality.

## Abstract Excerpt

Large language models are powerful generalists, yet solving deep and complex problems such as those of the Humanity’s Last Exam (HLE) remains both conceptually challenging and computationally expensive. We show that small orchestrators managing other models and a variety of tools are able to both push the upper bound of intelligence and improve efficiency in solving difficult agentic tasks. We introduce ToolOrchestra, a method for training small orchestrators that coordinate the use of intelligent tools. ToolOrchestra makes explicit use of reinforcement learning with outcome-, efficiency-, and user-preference-aware rewards. Using ToolOrchestra, we produce Orchestrator, an 8B model that...

## Suggested Note Seed

Contribution: Theory / proof: We show that small orchestrators managing other models and a variety of tools are able to both push the upper bound of intelligence and improve efficiency in solving difficult agentic tasks. Evidence to verify: metrics: accuracy; check theorem assumptions and empirical/theory split; check human-study or user-evaluation setup Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable.

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