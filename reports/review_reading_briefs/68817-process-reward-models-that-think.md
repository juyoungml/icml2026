# Process Reward Models That Think

- Sprint: `sprint_01` rank 32
- Global review rank: 32
- Event ID: `68817`
- Area: LLM Reasoning, Post-Training, and RLVR / RL for reasoning models and verifiable rewards
- Target claims: C01; C06
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: votes=1815; github_stars=89; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/68817) / [AlphaXiv](https://www.alphaxiv.org/abs/2504.16828) / [GitHub](https://github.com/mukhal/thinkprm)

## Where To Record Judgments

- Claim overlay keys: C01::68817 | C06::68817
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::68817
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet 1](../claim_validation_packets/c01-llm-reasoning-center-of-gravity.md), [claim packet 2](../claim_validation_packets/c06-external-trend-context.md)
- Claim dossiers: [claim dossier 1](../claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md), [claim dossier 2](../claim_evidence_dossiers/c06-external-trend-context.md)
- Area packet: [area packet](../validation_packets/llm-reasoning-post-training-and-rlvr.md)
- Area briefing: [area briefing](../area_briefing_cards/llm-reasoning-post-training-and-rlvr.md)

## What To Verify

- Contribution: Benchmark / evaluation: We propose ThinkPRM, a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs.
- Method: Tags: RL / policy optimization; LLM post-training; Reasoning / test-time compute; setting: math/code/verifiable; language/llm; abstract cues: benchmark.
- Evidence: benchmarks: ProcessBench; GPQA-Diamond; LiveCodeBench; metrics: reward
- Taxonomy: Check whether high attention supports the center-of-gravity claim. | Check whether broad arXiv-growth terms correspond to the paper's actual contribution.
- Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable. C06 (External trend context): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality.

## Abstract Excerpt

Step-by-step verifiers—also known as process reward models (PRMs)—are a key ingredient for test-time scaling, but training them requires expensive step-level supervision. This work aims to build data-efficient PRMs as verbalized step-wise reward models that verify every step in the solution by generating a verification chain-of-thought (CoT). We propose ThinkPRM, a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. Our approach capitalizes on the inherent reasoning abilities of long CoT models, and outperforms LLM-as-a-Judge and discriminative verifiers—using only 1% of the process labels in PRM800K—across several...

## Suggested Note Seed

Contribution: Benchmark / evaluation: We propose ThinkPRM, a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. Evidence to verify: benchmarks: ProcessBench; GPQA-Diamond; LiveCodeBench; metrics: reward Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable. C06 (External trend context): decide supports / weakens / complicates / not_applicable.

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