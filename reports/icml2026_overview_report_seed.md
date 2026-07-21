# ICML 2026 Overview Report Seed

A long-form report blueprint grounded in the current EDA workspace.
This is not a finished publication: it is a structured draft scaffold with claims, evidence, figures, caveats, and validation tasks.

## Working Thesis

ICML 2026 appears to be organized around foundation-model reasoning and post-training, with adjacent pressure from systems/efficiency and agentic workloads. Program signal remains more favorable to theory and safety/governance than public attention alone suggests, while robotics/world-model work shows the opposite pattern: small area share, high public attention. Multimodal/vision is large in absolute ICML volume but appears underweight relative to neighboring NeurIPS/ICLR accepted-paper baselines.

## Workspace QA

- Current automated validation failures: 0
- Validation report: [workspace_validation.md](../reports/workspace_validation.md)
- Claim validation packets: [claim packet index](../reports/icml2026_claim_validation_packet_index.md)
- Wording guardrails: [safe statement register](../reports/icml2026_safe_statement_register.md)

Read the safe statement register before turning the working thesis or executive bullets into final prose.

## Executive Summary Bullets

- **LLM reasoning center of gravity**: LLM reasoning/post-training is the largest ICML 2026 area and is also overweight relative to nearby accepted-paper baselines. Evidence: 1099 taxonomy papers (16.6%); historical delta +2.9 pp; public-attention enrichment 2.03x.
- **Infrastructure and agentic workloads**: Systems/efficiency and agents/code look smaller than LLM reasoning by paper count, but both are clear ICML 2026 overweights versus the neighboring-venue baseline. Evidence: Systems historical delta +2.1 pp, relative 1.68x; Agents historical delta +2.1 pp, relative 1.44x.
- **Program committee attention**: Theory and safety/governance receive more program signal than their public-attention signal would predict. Evidence: Theory oral enrichment 1.45x vs public enrichment 0.46x; Safety oral enrichment 1.41x and 3 awards vs public enrichment 0.51x.
- **Public attention mismatch**: Robotics/embodiment is small by taxonomy count but unusually strong in public attention. Evidence: 195 papers (2.9%); public-attention enrichment 2.11x vs oral enrichment 0.81x.
- **Neighboring-venue contrast**: Multimodal/vision is large inside ICML 2026 but underweight relative to NeurIPS 2025 and ICLR 2026 accepted-paper baselines. Evidence: 889 taxonomy papers (13.4%); historical delta -3.1 pp, relative 0.82x.

## Section 1: Corpus And Method

Purpose: establish what is counted, where signals come from, and what should not be overinterpreted.

Core evidence:
- Official ICML 2026 virtual-site corpus: 6,628 paper rows.
- AlphaXiv joined snapshot: 6,628 rows matched to official ICML papers.
- Manual taxonomy: 12 report-level areas over 42 semantic clusters.
- Historical baseline: ICML 2025, NeurIPS 2025, and ICLR 2026 accepted-paper corpora classified with a shared keyword scorer.

Use these figures:
- [figures/topic_group_distribution.png](../figures/topic_group_distribution.png)
- [figures/semantic_cluster_map.png](../figures/semantic_cluster_map.png)
- [figures/manual_taxonomy_area_sizes.png](../figures/manual_taxonomy_area_sizes.png)

Caveat to keep visible: taxonomy and evidence codes are strong for navigation but still need paper-level validation for publication claims.

## Section 2: The Area Map

Purpose: show the high-level shape of ICML 2026 before discussing attention or program signal.

| Area | Papers | Share | Signal Tags |
| --- | ---: | ---: | --- |
| LLM Reasoning, Post-Training, and RLVR | 1099 | 16.6% | large_area; program_overweight; public_overweight; venue_overweight; fast_arxiv_growth; high_artifact_visibility |
| Multimodal, Vision, and Perception | 889 | 13.4% | large_area; venue_underweight; fast_arxiv_growth |
| Theory, Optimization, and Algorithms | 737 | 11.1% | large_area; program_overweight |
| AI for Science, Health, and Neuro | 587 | 8.9% | none |
| Data-Centric, Causal, and Federated ML | 526 | 7.9% | none |
| Systems and Efficient Foundation Models | 515 | 7.8% | public_overweight; venue_overweight |
| Safety, Governance, Privacy, and Society | 502 | 7.6% | program_overweight; fast_arxiv_growth |
| Agents, Code, and Tool Use | 496 | 7.5% | public_overweight; venue_overweight; high_artifact_visibility; benchmark_heavy |
| Graphs, Geometry, and Representation Learning | 391 | 5.9% | none |
| Generative Modeling | 379 | 5.7% | high_artifact_visibility |
| Reinforcement Learning and Control | 312 | 4.7% | none |
| Robotics, Embodiment, and World Models | 195 | 2.9% | public_overweight; high_artifact_visibility |

Use these figures:
- [figures/manual_taxonomy_area_sizes.png](../figures/manual_taxonomy_area_sizes.png)
- [figures/semantic_cluster_map.png](../figures/semantic_cluster_map.png)

## Section 3: Claims To Build The Narrative Around

### C01: LLM reasoning center of gravity

Claim: LLM reasoning/post-training is the largest ICML 2026 area and is also overweight relative to nearby accepted-paper baselines.

Evidence: 1099 taxonomy papers (16.6%); historical delta +2.9 pp; public-attention enrichment 2.03x.

Strength: `strong_for_landscape`

Caveat: Area boundaries include general LLM training/evaluation and some diffusion-language papers; paper-level taxonomy still needs review.

Suggested figures:
- [figures/manual_taxonomy_area_sizes.png](../figures/manual_taxonomy_area_sizes.png)
- [figures/historical_venue_area_deltas.png](../figures/historical_venue_area_deltas.png)
- [figures/arxiv_taxonomy_trends.png](../figures/arxiv_taxonomy_trends.png)

Validation packet: [reports/claim_validation_packets/c01-llm-reasoning-center-of-gravity.md](../reports/claim_validation_packets/c01-llm-reasoning-center-of-gravity.md)

Next validation: Manually inspect boundary clusters 14, 21, and 24 before making subarea-level claims.

### C02: Infrastructure and agentic workloads

Claim: Systems/efficiency and agents/code look smaller than LLM reasoning by paper count, but both are clear ICML 2026 overweights versus the neighboring-venue baseline.

Evidence: Systems historical delta +2.1 pp, relative 1.68x; Agents historical delta +2.1 pp, relative 1.44x.

Strength: `moderate_to_strong`

Caveat: Historical comparison uses a keyword scorer; ICML 2025 and NeurIPS 2025 lack static abstracts in the current pull.

Suggested figures:
- [figures/historical_venue_area_deltas.png](../figures/historical_venue_area_deltas.png)
- [figures/program_signal_calibration.png](../figures/program_signal_calibration.png)

Validation packet: [reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md](../reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md)

Next validation: Read top positive-delta papers and check whether deltas reflect real venue emphasis or metadata/topic-label differences.

### C03: Program committee attention

Claim: Theory and safety/governance receive more program signal than their public-attention signal would predict.

Evidence: Theory oral enrichment 1.45x vs public enrichment 0.46x; Safety oral enrichment 1.41x and 3 awards vs public enrichment 0.51x.

Strength: `strong_for_triage`

Caveat: Oral/award counts are program signals, not full quality labels; award counts are small and volatile.

Suggested figures:
- [figures/program_signal_calibration.png](../figures/program_signal_calibration.png)
- [figures/cluster_public_vs_program_signal.png](../figures/cluster_public_vs_program_signal.png)

Validation packet: [reports/claim_validation_packets/c03-program-committee-attention.md](../reports/claim_validation_packets/c03-program-committee-attention.md)

Next validation: Review low-public/high-program papers to extract the technical reasons for committee interest.

### C04: Public attention mismatch

Claim: Robotics/embodiment is small by taxonomy count but unusually strong in public attention.

Evidence: 195 papers (2.9%); public-attention enrichment 2.11x vs oral enrichment 0.81x.

Strength: `moderate`

Caveat: AlphaXiv likely overweights shareable VLA/world-model work and project-page traffic.

Suggested figures:
- [figures/program_signal_calibration.png](../figures/program_signal_calibration.png)
- [figures/manual_taxonomy_area_sizes.png](../figures/manual_taxonomy_area_sizes.png)

Validation packet: [reports/claim_validation_packets/c04-public-attention-mismatch.md](../reports/claim_validation_packets/c04-public-attention-mismatch.md)

Next validation: Inspect whether the high-attention papers are benchmarks, demos, or reusable models rather than core ICML program emphasis.

### C05: Neighboring-venue contrast

Claim: Multimodal/vision is large inside ICML 2026 but underweight relative to NeurIPS 2025 and ICLR 2026 accepted-paper baselines.

Evidence: 889 taxonomy papers (13.4%); historical delta -3.1 pp, relative 0.82x.

Strength: `moderate`

Caveat: This is the area most sensitive to venue scope and title/topic classification; ICLR/NeurIPS vision-heavy shares may dominate the baseline average.

Suggested figures:
- [figures/historical_venue_area_deltas.png](../figures/historical_venue_area_deltas.png)
- [figures/arxiv_taxonomy_trends.png](../figures/arxiv_taxonomy_trends.png)

Validation packet: [reports/claim_validation_packets/c05-neighboring-venue-contrast.md](../reports/claim_validation_packets/c05-neighboring-venue-contrast.md)

Next validation: Break multimodal into vision-language reasoning, video, 3D, and robustness before interpreting the aggregate underweight.

### C06: External trend context

Claim: The fastest broad arXiv growth areas are multimodal/vision, LLM reasoning, and safety/governance, but ICML 2026 does not mirror this ranking exactly.

Evidence: Multimodal, Vision, and Perception: 94.6%; LLM Reasoning, Post-Training, and RLVR: 59.9%; Safety, Governance, Privacy, and Society: 53.6%; Systems and Efficient Foundation Models: 43.3%

Strength: `context_only`

Caveat: arXiv queries are broad, overlapping, and not acceptance or quality signals.

Suggested figures:
- [figures/arxiv_taxonomy_trends.png](../figures/arxiv_taxonomy_trends.png)
- [figures/historical_venue_area_deltas.png](../figures/historical_venue_area_deltas.png)

Validation packet: [reports/claim_validation_packets/c06-external-trend-context.md](../reports/claim_validation_packets/c06-external-trend-context.md)

Next validation: Use accepted-paper corpora, not arXiv counts, for publication-ready year-over-year venue claims.

### C07: Artifact visibility

Claim: Artifacts are most visible in agents/code, LLM reasoning, systems, and multimodal/vision, while theory remains much less artifact-linked.

Evidence: Robotics, Embodiment, and World Models: GitHub URL share 38.0%; Agents, Code, and Tool Use: GitHub URL share 32.9%; LLM Reasoning, Post-Training, and RLVR: GitHub URL share 32.1%; Generative Modeling: GitHub URL share 31.1%

Strength: `moderate`

Caveat: GitHub metadata comes from AlphaXiv and does not prove runnable reproduction; some high-star links are templates or index repos.

Suggested figures:
- [figures/manual_taxonomy_area_sizes.png](../figures/manual_taxonomy_area_sizes.png)
- [figures/alphaxiv_attention_distributions.png](../figures/alphaxiv_attention_distributions.png)

Validation packet: [reports/claim_validation_packets/c07-artifact-visibility.md](../reports/claim_validation_packets/c07-artifact-visibility.md)

Next validation: Clone/check high-signal repositories and separate code, benchmark, dataset, checkpoint, and project-page links.

### C08: Validation priority

Claim: The biggest remaining quality jump is not more plotting; it is paper-level validation of boundary clusters and high-impact claims.

Evidence: 21 of 42 semantic clusters are marked needs_review; validation queue contains 192 papers across 12 areas.

Strength: `process_claim`

Caveat: The queue organizes review but does not mean evidence fields have been checked.

Suggested figures:
- [figures/semantic_cluster_map.png](../figures/semantic_cluster_map.png)
- [figures/evidence_contribution_mix.png](../figures/evidence_contribution_mix.png)

Validation packet: [reports/claim_validation_packets/c08-validation-priority.md](../reports/claim_validation_packets/c08-validation-priority.md)

Next validation: Fill validation packets and reconcile reviewed fields back into a checked CSV.

## Section 4: Program Signal vs Public Attention

Purpose: separate committee-visible importance from public/shareable attention.

Main contrast to explain:
- Theory and safety/governance are stronger in program signal than public attention.
- Robotics/world models, LLM reasoning, systems, and agents are stronger in public attention.

Use these figures:
- [figures/program_signal_calibration.png](../figures/program_signal_calibration.png)
- [figures/cluster_public_vs_program_signal.png](../figures/cluster_public_vs_program_signal.png)

## Section 5: External Baselines

Purpose: prevent ICML-only analysis from confusing venue emphasis with field-wide trends.

Use these figures:
- [figures/historical_venue_area_deltas.png](../figures/historical_venue_area_deltas.png)
- [figures/arxiv_taxonomy_trends.png](../figures/arxiv_taxonomy_trends.png)

Interpretation guardrail: historical accepted-paper deltas are closer to venue comparison than arXiv counts; arXiv counts are broad trend context only.

## Section 6: Reproducibility And Artifact Signals

Purpose: distinguish artifact visibility from actual reproducibility.

Use these reports:
- [reports/icml2026_reproducibility_lens.md](../reports/icml2026_reproducibility_lens.md)
- [reports/icml2026_github_artifact_live_check.md](../reports/icml2026_github_artifact_live_check.md)
- [reports/claim_validation_packets/c07-artifact-visibility.md](../reports/claim_validation_packets/c07-artifact-visibility.md)

Interpretation guardrail: a GitHub URL is not runnable code, and a high-star repository can be a template, homepage, or unrelated index.

## Section 7: What Must Be Manually Checked Before Publication

- Boundary clusters in LLM reasoning, systems, data-centric ML, and AI-for-science.
- Public-heavy but non-program robotics/world-model papers.
- Program-heavy but low-public theory and safety/governance papers.
- High-star GitHub links and template/index repositories.
- Benchmark/dataset/metric tags generated from heuristics.

Primary review entry points:
- [reports/icml2026_claim_validation_packet_index.md](../reports/icml2026_claim_validation_packet_index.md)
- [reports/icml2026_validation_packet_index.md](../reports/icml2026_validation_packet_index.md)
- [data/processed/icml2026_claim_validation_queue.csv](../data/processed/icml2026_claim_validation_queue.csv)
- [data/processed/icml2026_manual_validation_queue.csv](../data/processed/icml2026_manual_validation_queue.csv)

## Recommended Final Report Structure

1. Corpus and signal sources
2. ICML 2026 area map
3. Foundation-model reasoning as center of gravity
4. Systems and agents as adjacent overweights
5. Program signal versus public attention
6. Historical and arXiv baselines
7. Artifact and reproducibility lens
8. Caveats and validation agenda