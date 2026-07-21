# Learning to Discover at Test Time

- Sprint: `sprint_01` rank 17
- Global review rank: 17
- Event ID: `65888`
- Area: Agents, Code, and Tool Use / Multi-agent search, planning, and coordination
- Target claims: C02; C08
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: votes=529; github_stars=297; taxonomy_review; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/65888) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.16175) / [GitHub](https://github.com/sayantann11/all-classification-templetes-for-ML)

## Where To Record Judgments

- Claim overlay keys: C02::65888 | C08::65888
- Area overlay keys: Agents, Code, and Tool Use::65888
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet 1](../claim_validation_packets/c02-infrastructure-and-agentic-workloads.md), [claim packet 2](../claim_validation_packets/c08-validation-priority.md)
- Claim dossiers: [claim dossier 1](../claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md), [claim dossier 2](../claim_evidence_dossiers/c08-validation-priority.md)
- Area packet: [area packet](../validation_packets/agents-code-and-tool-use.md)
- Area briefing: [area briefing](../area_briefing_cards/agents-code-and-tool-use.md)

## What To Verify

- Contribution: System / infrastructure: All our results are achieved with an open model, OpenAI gpt-oss-120b, and can be reproduced with our publicly available code, in contrast to previous best results that required closed frontier models.
- Method: Tags: RL / policy optimization; Reasoning / test-time compute; Agents / tool use; Diffusion / flow; setting: math/code/verifiable; language/llm; abstract cues: reinforcement learning.
- Evidence: identify baselines, datasets, metrics, ablations, and negative cases from the PDF
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Check whether public signal reflects core infrastructure/agent workloads or broad LLM spillover. | Decide whether this cluster should remain in the assigned area/subarea or be relabeled.
- Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable. C08 (Validation priority): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Taxonomy assignment may be unstable.

## Abstract Excerpt

How can we use AI to discover a new state of the art for a scientific problem? Prior work in test-time scaling, such as AlphaEvolve, performs search by prompting a frozen LLM. We perform reinforcement learning at test time, so the LLM can continue to train, but now with experience specific to the test problem. This form of continual learning is quite special, because its goal is to produce one great solution rather than many good ones on average, and to solve this very problem rather than generalize to other problems. Therefore, our learning objective and search subroutine are designed to prioritize the most promising solutions. We call this method Test-Time Training to Discover...

## Suggested Note Seed

Contribution: System / infrastructure: All our results are achieved with an open model, OpenAI gpt-oss-120b, and can be reproduced with our publicly available code, in contrast to previous best results that required closed frontier models. Evidence to verify: identify baselines, datasets, metrics, ablations, and negative cases from the PDF Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable. C08 (Validation priority): decide supports / weakens / complicates / not_applicable.

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