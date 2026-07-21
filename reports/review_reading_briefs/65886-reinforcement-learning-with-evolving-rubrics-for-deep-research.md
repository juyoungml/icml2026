# Reinforcement Learning with Evolving Rubrics for Deep Research

- Sprint: `sprint_01` rank 10
- Global review rank: 10
- Event ID: `65886`
- Area: LLM Reasoning, Post-Training, and RLVR / Reward modeling, preference feedback, and RL post-training
- Target claims: C01; C08
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: oral; votes=201; github_stars=682; taxonomy_review; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/65886) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.19399) / [GitHub](https://github.com/rlresearch/dr-tulu)

## Where To Record Judgments

- Claim overlay keys: C01::65886 | C08::65886
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::65886
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet 1](../claim_validation_packets/c01-llm-reasoning-center-of-gravity.md), [claim packet 2](../claim_validation_packets/c08-validation-priority.md)
- Claim dossiers: [claim dossier 1](../claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md), [claim dossier 2](../claim_evidence_dossiers/c08-validation-priority.md)
- Area packet: [area packet](../validation_packets/llm-reasoning-post-training-and-rlvr.md)
- Area briefing: [area briefing](../area_briefing_cards/llm-reasoning-post-training-and-rlvr.md)

## What To Verify

- Contribution: Benchmark / evaluation: Using RLER, we develop **Deep Research Tulu (DR Tulu-8B)**, the first fully open model that is directly trained for open-ended, long-form deep research.
- Method: Tags: RL / policy optimization; Reasoning / test-time compute; Agents / tool use; setting: math/code/verifiable; language/llm; abstract cues: reinforcement learning; benchmark; agent.
- Evidence: identify baselines, datasets, metrics, ablations, and negative cases from the PDF
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Check whether this is genuinely LLM reasoning/post-training or a broader LLM/system/safety paper. | Use high-signal papers to stress-test taxonomy boundaries.
- Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable. C08 (Validation priority): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. Taxonomy assignment may be unstable.

## Abstract Excerpt

Deep research agents perform multi-step research to produce long-form, well-attributed answers. However, most open deep research agents are trained on easily verifiable short-form QA tasks via reinforcement learning with verifiable rewards, which does not extend to realistic long-form tasks. We address this with **Reinforcement Learning with Evolving Rubrics (RLER)**, where rubrics are constructed and maintained to *co-evolve* with the policy model during training. This allows the rubrics to incorporate newly explored information from search and contrasting model responses, enabling better fact checking and more discriminative on-policy feedback. Using RLER, we develop **Deep Research...

## Suggested Note Seed

Contribution: Benchmark / evaluation: Using RLER, we develop **Deep Research Tulu (DR Tulu-8B)**, the first fully open model that is directly trained for open-ended, long-form deep research. Evidence to verify: identify baselines, datasets, metrics, ablations, and negative cases from the PDF Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable. C08 (Validation priority): decide supports / weakens / complicates / not_applicable.

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