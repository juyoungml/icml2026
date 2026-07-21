# Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers

- Sprint: `sprint_01` rank 13
- Global review rank: 13
- Event ID: `65446`
- Area: LLM Reasoning, Post-Training, and RLVR / General LLM training, evaluation, and alignment
- Target claims: C01
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: oral; votes=75; taxonomy_review; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/65446) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.15674)

## Where To Record Judgments

- Claim overlay keys: C01::65446
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::65446
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c01-llm-reasoning-center-of-gravity.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md)
- Area packet: [area packet](../validation_packets/llm-reasoning-post-training-and-rlvr.md)
- Area briefing: [area briefing](../area_briefing_cards/llm-reasoning-post-training-and-rlvr.md)

## What To Verify

- Contribution: Position / conceptual: We find that AOs can recover information fine-tuned into a model (e.g., biographical knowledge or malign propensities) that does not appear in the input text, despite never being trained with activations from a fine-tuned model.
- Method: Tags: LLM post-training; setting: language/llm; abstract cues: dataset.
- Evidence: benchmarks: LatentQA; LatentQA-trained; check theorem assumptions and empirical/theory split
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Check whether this is genuinely LLM reasoning/post-training or a broader LLM/system/safety paper.
- Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable.
- Artifact: No obvious artifact link; record none/not_applicable unless PDF shows a release.
- Warning: Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. Taxonomy assignment may be unstable.

## Abstract Excerpt

Large language model (LLM) activations are notoriously difficult to understand, with most existing techniques using complex, specialized methods for interpreting them. Recent work has proposed a simpler approach known as LatentQA: training LLMs to directly accept LLM activations as inputs and answer arbitrary questions about them in natural language. However, prior work has focused on narrow task settings for both training and evaluation. In this paper, we instead take a generalist perspective. We evaluate LatentQA-trained models, which we call Activation Oracles (AOs), in far out-of-distribution settings and examine how performance scales with training data diversity. We find that AOs...

## Suggested Note Seed

Contribution: Position / conceptual: We find that AOs can recover information fine-tuned into a model (e.g., biographical knowledge or malign propensities) that does not appear in the input text, despite never being trained with activations from a fine-tuned model. Evidence to verify: benchmarks: LatentQA; LatentQA-trained; check theorem assumptions and empirical/theory split Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable.

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