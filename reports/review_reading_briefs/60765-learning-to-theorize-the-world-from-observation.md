# Learning to Theorize the World from Observation

- Sprint: `sprint_01` rank 30
- Global review rank: 30
- Event ID: `60765`
- Area: LLM Reasoning, Post-Training, and RLVR / Reasoning models and chain-of-thought behavior
- Target claims: C01
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: oral; votes=56; taxonomy_review; evidence=low
- Links: [ICML](https://icml.cc/virtual/2026/poster/60765) / [AlphaXiv](https://www.alphaxiv.org/abs/2605.03413)

## Where To Record Judgments

- Claim overlay keys: C01::60765
- Area overlay keys: none
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c01-llm-reasoning-center-of-gravity.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md)
- Area packet: none
- Area briefing: [area briefing](../area_briefing_cards/llm-reasoning-post-training-and-rlvr.md)

## What To Verify

- Contribution: System / infrastructure: In this paper, we introduce Learning-to-Theorize (L2T), a learning paradigm in which an AI system acquires the ability to construct theories represented as executable programs directly from observation alone.
- Method: Tags: no method-family tag; setting: math/code/verifiable; vision/video; language/llm; theory/synthetic; abstract cues: theory.
- Evidence: identify baselines, datasets, metrics, ablations, and negative cases from the PDF
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Check whether this is genuinely LLM reasoning/post-training or a broader LLM/system/safety paper.
- Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable.
- Artifact: No obvious artifact link; record none/not_applicable unless PDF shows a release.
- Warning: Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. Heuristic evidence tag is low confidence. Taxonomy assignment may be unstable.

## Abstract Excerpt

What does it mean to understand the world? Is it simply to predict future video frames? Developmental cognitive science suggests that understanding the world is fundamentally the process of constructing internal theories of how it works rather than mere prediction, even before language is acquired. However, in machine learning, it remains unclear how to endow AI systems with such theory-building capability from raw, non-textual observation alone. In this paper, we introduce Learning-to-Theorize (L2T), a learning paradigm in which an AI system acquires the ability to construct theories represented as executable programs directly from observation alone. To instantiate this paradigm, we...

## Suggested Note Seed

Contribution: System / infrastructure: In this paper, we introduce Learning-to-Theorize (L2T), a learning paradigm in which an AI system acquires the ability to construct theories represented as executable programs directly from observation alone. Evidence to verify: identify baselines, datasets, metrics, ablations, and negative cases from the PDF Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable.

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