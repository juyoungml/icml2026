# Latent Collaboration in Multi-Agent Systems

- Sprint: `sprint_01` rank 21
- Global review rank: 21
- Event ID: `61180`
- Area: LLM Reasoning, Post-Training, and RLVR / Reasoning models and chain-of-thought behavior
- Target claims: C01; C08
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: votes=402; github_stars=1048; taxonomy_review; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/61180) / [AlphaXiv](https://www.alphaxiv.org/abs/2511.20639) / [GitHub](https://github.com/Gen-Verse/LatentMAS)

## Where To Record Judgments

- Claim overlay keys: C01::61180 | C08::61180
- Area overlay keys: LLM Reasoning, Post-Training, and RLVR::61180
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet 1](../claim_validation_packets/c01-llm-reasoning-center-of-gravity.md), [claim packet 2](../claim_validation_packets/c08-validation-priority.md)
- Claim dossiers: [claim dossier 1](../claim_evidence_dossiers/c01-llm-reasoning-center-of-gravity.md), [claim dossier 2](../claim_evidence_dossiers/c08-validation-priority.md)
- Area packet: [area packet](../validation_packets/llm-reasoning-post-training-and-rlvr.md)
- Area briefing: [area briefing](../area_briefing_cards/llm-reasoning-post-training-and-rlvr.md)

## What To Verify

- Contribution: Benchmark / evaluation: We introduce LatentMAS, an end-to-end training-free framework that enables pure latent collaboration among LLM agents.
- Method: Tags: Reasoning / test-time compute; Agents / tool use; setting: math/code/verifiable; language/llm; theory/synthetic; abstract cues: benchmark; agent.
- Evidence: metrics: accuracy; memory
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Check whether high attention supports the center-of-gravity claim. | Decide whether this cluster should remain in the assigned area/subarea or be relabeled.
- Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable. C08 (Validation priority): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality. Taxonomy assignment may be unstable.

## Abstract Excerpt

Multi-agent systems (MAS) extend large language models (LLMs) from independent single-model reasoning to coordinative system-level intelligence. While existing LLM agents depend on text-based mediation for reasoning and communication, we take a step forward by enabling models to collaborate directly within the continuous latent space. We introduce LatentMAS, an end-to-end training-free framework that enables pure latent collaboration among LLM agents. In LatentMAS, each agent first performs auto-regressive latent thoughts generation through last-layer hidden embeddings instead of text. Then, a shared latent working memory preserves and transfers each agent's internal representations and...

## Suggested Note Seed

Contribution: Benchmark / evaluation: We introduce LatentMAS, an end-to-end training-free framework that enables pure latent collaboration among LLM agents. Evidence to verify: metrics: accuracy; memory Claim implication: C01 (LLM reasoning center of gravity): decide supports / weakens / complicates / not_applicable. C08 (Validation priority): decide supports / weakens / complicates / not_applicable.

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