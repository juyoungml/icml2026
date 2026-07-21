# Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning

- Sprint: `sprint_01` rank 25
- Global review rank: 25
- Event ID: `63095`
- Area: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Target claims: C02
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: oral; votes=89; github_stars=1228; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/63095) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.19900) / [GitHub](https://github.com/aiming-lab/Agent0)

## Where To Record Judgments

- Claim overlay keys: C02::63095
- Area overlay keys: Agents, Code, and Tool Use::63095
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c02-infrastructure-and-agentic-workloads.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md)
- Area packet: [area packet](../validation_packets/agents-code-and-tool-use.md)
- Area briefing: [area briefing](../area_briefing_cards/agents-code-and-tool-use.md)

## What To Verify

- Contribution: Dataset / data resource: To address these challenges, inspired by recent advances in tool-integrated reasoning, we propose Agent0-VL, a self-evolving vision-language agent that achieves continual improvement with tool-integrated reasoning.
- Method: Tags: RL / policy optimization; Reasoning / test-time compute; Agents / tool use; Graphs / geometry; setting: vision/video; language/llm; abstract cues: reinforcement learning; agent; tool; multimodal.
- Evidence: metrics: reward; check theorem assumptions and empirical/theory split; check human-study or user-evaluation setup
- Taxonomy: Check whether program-selected papers substantiate systems/agents emphasis.
- Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness.

## Abstract Excerpt

Large Vision-Language Models (LVLMs) have achieved remarkable progress in multimodal reasoning tasks; however, their learning remains constrained by the limitations of human-annotated supervision. Recent self-rewarding approaches attempt to overcome this constraint by allowing models to act as their own critics or reward providers. Yet, purely text-based self-evaluation struggles to verify complex visual reasoning steps and often suffers from evaluation hallucinations. To address these challenges, inspired by recent advances in tool-integrated reasoning, we propose Agent0-VL, a self-evolving vision-language agent that achieves continual improvement with tool-integrated reasoning....

## Suggested Note Seed

Contribution: Dataset / data resource: To address these challenges, inspired by recent advances in tool-integrated reasoning, we propose Agent0-VL, a self-evolving vision-language agent that achieves continual improvement with tool-integrated reasoning. Evidence to verify: metrics: reward; check theorem assumptions and empirical/theory split; check human-study or user-evaluation setup Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable.

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