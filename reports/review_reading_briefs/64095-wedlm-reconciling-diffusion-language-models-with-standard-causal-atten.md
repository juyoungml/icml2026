# WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference

- Sprint: `sprint_01` rank 19
- Global review rank: 19
- Event ID: `64095`
- Area: LLM Reasoning, Post-Training, and RLVR / Diffusion language models and decoding
- Target claims: C01
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: oral; votes=60; github_stars=644; taxonomy_review; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/64095) / [AlphaXiv](https://www.alphaxiv.org/abs/2512.22737) / [GitHub](https://github.com/Tencent/WeDLM)

## Where To Record Judgments

- Claim overlay keys: C01::64095
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::64095
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet](../claim_validation_packets/c01-llm-reasoning-center-of-gravity.md)
- Claim dossiers: [claim dossier](../claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md)
- Area packet: [area packet](../validation_packets/llm-reasoning-post-training-and-rlvr.md)
- Area briefing: [area briefing](../area_briefing_cards/llm-reasoning-post-training-and-rlvr.md)

## What To Verify

- Contribution: Benchmark / evaluation: We propose WeDLM, a diffusion decoding framework built entirely on standard causal attention to make parallel generation prefix-cache friendly.
- Method: Tags: Reasoning / test-time compute; Diffusion / flow; Transformer / attention; Causal / data-centric; setting: language/llm; abstract cues: diffusion; benchmark.
- Evidence: identify baselines, datasets, metrics, ablations, and negative cases from the PDF
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Check whether this is genuinely LLM reasoning/post-training or a broader LLM/system/safety paper.
- Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. Taxonomy assignment may be unstable.

## Abstract Excerpt

Autoregressive (AR) generation is the standard decoding paradigm for Large Language Models (LLMs), but its token-by-token nature limits parallelism at inference time. Diffusion Language Models (DLLMs) offer parallel decoding by recovering multiple masked tokens per step; however, in practice they often fail to translate this parallelism into speed gains over optimized AR engines (e.g., vLLM). A key reason is that many DLLMs rely on bidirectional attention, which breaks standard prefix KV caching. We propose WeDLM, a diffusion decoding framework built entirely on standard causal attention to make parallel generation prefix-cache friendly. The core idea is to let each masked position...

## Suggested Note Seed

Contribution: Benchmark / evaluation: We propose WeDLM, a diffusion decoding framework built entirely on standard causal attention to make parallel generation prefix-cache friendly. Evidence to verify: identify baselines, datasets, metrics, ablations, and negative cases from the PDF Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable.

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