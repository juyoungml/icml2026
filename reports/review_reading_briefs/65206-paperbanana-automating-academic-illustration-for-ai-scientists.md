# PaperBanana: Automating Academic Illustration for AI Scientists

- Sprint: `sprint_01` rank 6
- Global review rank: 6
- Event ID: `65206`
- Area: Agents, Code, and Tool Use / Agent evaluation, tool use, and agentic workflows
- Target claims: C02; C07
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: votes=420; github_stars=6765; evidence=medium
- Links: [ICML](https://icml.cc/virtual/2026/poster/65206) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.23265) / [GitHub](https://github.com/dwzhu-pku/PaperBanana)

## Where To Record Judgments

- Claim overlay keys: C02::65206 | C07::65206
- Area overlay keys: Agents, Code, and Tool Use::65206
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet 1](../claim_validation_packets/c02-infrastructure-and-agentic-workloads.md), [claim packet 2](../claim_validation_packets/c07-artifact-visibility.md)
- Claim dossiers: [claim dossier 1](../claim_evidence_dossiers/c02-infrastructure-and-agentic-workloads.md), [claim dossier 2](../claim_evidence_dossiers/c07-artifact-visibility.md)
- Area packet: [area packet](../validation_packets/agents-code-and-tool-use.md)
- Area briefing: [area briefing](../area_briefing_cards/agents-code-and-tool-use.md)

## What To Verify

- Contribution: Benchmark / evaluation: To lift this burden, we introduce PaperBanana, an agentic framework for automated generation of publication-ready academic illustrations.
- Method: Tags: Agents / tool use; setting: vision/video; language/llm; abstract cues: agent.
- Evidence: benchmarks: PaperBananaBench
- Taxonomy: Check whether public signal reflects core infrastructure/agent workloads or broad LLM spillover. | Check artifact type, license/readme quality, and whether reproduction assets are present.
- Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable. C07 (Artifact visibility): decide supports / weakens / complicates / not_applicable.
- Artifact: Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible.
- Warning: Do not treat AlphaXiv attention as quality.

## Abstract Excerpt

Despite rapid advances in autonomous AI scientists powered by language models, generating publication-ready illustrations remains a labor-intensive bottleneck in the research workflow. To lift this burden, we introduce PaperBanana, an agentic framework for automated generation of publication-ready academic illustrations. Powered by state-of-the-art VLMs and image generation models, PaperBanana orchestrates specialized agents to retrieve references, plan content and style, render images, and iteratively refine via self-critique. To rigorously evaluate our framework, we introduce PaperBananaBench, comprising 292 test cases for methodology diagrams curated from NeurIPS 2025 publications,...

## Suggested Note Seed

Contribution: Benchmark / evaluation: To lift this burden, we introduce PaperBanana, an agentic framework for automated generation of publication-ready academic illustrations. Evidence to verify: benchmarks: PaperBananaBench Claim implication: C02 (Infrastructure and agentic workloads): decide supports / weakens / complicates / not_applicable. C07 (Artifact visibility): decide supports / weakens / complicates / not_applicable.

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