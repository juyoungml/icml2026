# daVinci-Dev: Agent-native Mid-training for Software Engineering

- Sprint: `sprint_01` rank 38
- Global review rank: 38
- Event ID: `63099`
- Area: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Target claims: C02
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: oral; votes=52; github_stars=9; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/63099) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.18418) / [GitHub](https://github.com/sii-research/GAIR)

## Where To Record Judgments

- Claim overlay keys: C02::63099
- Area overlay keys: Agents, Code, and Tool Use::63099
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c02-infrastructure-and-agentic-workloads.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md)
- Area packet: [area packet](../validation_packets/agents-code-and-tool-use.md)
- Area briefing: [area briefing](../area_briefing_cards/agents-code-and-tool-use.md)

## What To Verify

- Contribution: Benchmark / evaluation: To address this, we present a systematic study of agentic mid-training, establishing both the data synthesis principles and training methodology for effective agent development at scale.
- Method: Tags: RL / policy optimization; LLM post-training; Reasoning / test-time compute; Agents / tool use; Diffusion / flow; setting: math/code/verifiable; language/llm; abstract cues: reinforcement learning; benchmark; dataset; agent; tool.
- Evidence: identify baselines, datasets, metrics, ablations, and negative cases from the PDF
- Taxonomy: Check whether program-selected papers substantiate systems/agents emphasis.
- Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness.

## Abstract Excerpt

Recently, the frontier of Large Language Model (LLM) capabilities has shifted from single-turn code generation to agentic software engineering—a paradigm where models autonomously navigate, edit, and test complex repositories. While post-training methods have become the de facto approach for code agents, *agentic mid-training*—mid-training (MT) on large-scale data that mirrors authentic agentic workflows—remains critically underexplored due to substantial resource requirements, despite offering a more scalable path to instilling foundational agentic behaviors than relying solely on expensive reinforcement learning. A central challenge in realizing effective agentic mid-training is the...

## Suggested Note Seed

Contribution: Benchmark / evaluation: To address this, we present a systematic study of agentic mid-training, establishing both the data synthesis principles and training methodology for effective agent development at scale. Evidence to verify: identify baselines, datasets, metrics, ablations, and negative cases from the PDF Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable.

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