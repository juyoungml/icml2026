# How much can language models memorize?

- Sprint: `sprint_01` rank 1
- Global review rank: 1
- Event ID: `62989`
- Area: LLM Reasoning, Post-Training, and RLVR / Diffusion language models and decoding
- Target claims: C01; C08
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: oral; Outstanding Paper Honorable Mention; votes=271; github_stars=2; taxonomy_review; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/62989) / [AlphaXiv](https://www.alphaxiv.org/abs/2505.24832) / [GitHub](https://github.com/SimonCao1207/LLM-Capacity)

## Where To Record Judgments

- Claim overlay keys: C01::62989 | C08::62989
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::62989
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet 1](../claim_validation_packets/c01-llm-reasoning-center-of-gravity.md), [claim packet 2](../claim_validation_packets/c08-validation-priority.md)
- Claim dossiers: [claim dossier 1](../claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md), [claim dossier 2](../claim_evidence_dossiers/c08-validation-priority.md)
- Area packet: [area packet](../validation_packets/llm-reasoning-post-training-and-rlvr.md)
- Area briefing: [area briefing](../area_briefing_cards/llm-reasoning-post-training-and-rlvr.md)

## What To Verify

- Contribution: Dataset / data resource: We propose a new method for estimating how much a model knows about a datapoint and use it to measure the capacity of modern language models.
- Method: Tags: Transformer / attention; setting: language/llm; abstract cues: transformer; dataset.
- Evidence: identify baselines, datasets, metrics, ablations, and negative cases from the PDF
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Check whether this is genuinely LLM reasoning/post-training or a broader LLM/system/safety paper. | Decide whether this cluster should remain in the assigned area/subarea or be relabeled.
- Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable. C08 (Validation priority): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. Taxonomy assignment may be unstable.

## Abstract Excerpt

We propose a new method for estimating how much a model knows about a datapoint and use it to measure the capacity of modern language models. Prior studies of language model memorization have struggled to disentangle memorization from generalization. We formally separate memorization into two components: unintended memorization, the information a model contains about a specific dataset, and generalization, the information a model contains about the true data-generation process. When we completely eliminate generalization, we can compute the total memorization, which provides an estimate of model capacity: our measurements estimate that GPT-style models have a capacity of approximately...

## Suggested Note Seed

Contribution: Dataset / data resource: We propose a new method for estimating how much a model knows about a datapoint and use it to measure the capacity of modern language models. Evidence to verify: identify baselines, datasets, metrics, ablations, and negative cases from the PDF Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable. C08 (Validation priority): decide supports / weakens / complicates / not_applicable.

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