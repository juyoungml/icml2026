# ICML 2026 Landscape Synthesis

This is the researcher-facing synthesis layer: a claim register plus the strongest cross-source signals from the ICML 2026 EDA workspace.
It is designed to be read before the longer area reports and validation packets.

## Fast Read

- **LLM reasoning center of gravity**: LLM reasoning/post-training is the largest ICML 2026 area and is also overweight relative to nearby accepted-paper baselines. Evidence: 1099 taxonomy papers (16.6%); historical delta +2.9 pp; public-attention enrichment 2.03x.
- **Infrastructure and agentic workloads**: Systems/efficiency and agents/code look smaller than LLM reasoning by paper count, but both are clear ICML 2026 overweights versus the neighboring-venue baseline. Evidence: Systems historical delta +2.1 pp, relative 1.68x; Agents historical delta +2.1 pp, relative 1.44x.
- **Program committee attention**: Theory and safety/governance receive more program signal than their public-attention signal would predict. Evidence: Theory oral enrichment 1.45x vs public enrichment 0.46x; Safety oral enrichment 1.41x and 3 awards vs public enrichment 0.51x.
- **Public attention mismatch**: Robotics/embodiment is small by taxonomy count but unusually strong in public attention. Evidence: 195 papers (2.9%); public-attention enrichment 2.11x vs oral enrichment 0.81x.
- **Neighboring-venue contrast**: Multimodal/vision is large inside ICML 2026 but underweight relative to NeurIPS 2025 and ICLR 2026 accepted-paper baselines. Evidence: 889 taxonomy papers (13.4%); historical delta -3.1 pp, relative 0.82x.

## Signal Matrix Highlights

### Largest ICML 2026 Taxonomy Areas
- LLM Reasoning, Post-Training, and RLVR: 1099 papers (16.6%); votes/paper 18.55; tags: large_area; program_overweight; public_overweight; venue_overweight; fast_arxiv_growth; high_artifact_visibility
- Multimodal, Vision, and Perception: 889 papers (13.4%); votes/paper 7.25; tags: large_area; venue_underweight; fast_arxiv_growth
- Theory, Optimization, and Algorithms: 737 papers (11.1%); votes/paper 4.21; tags: large_area; program_overweight
- AI for Science, Health, and Neuro: 587 papers (8.9%); votes/paper 3.01; tags: 
- Data-Centric, Causal, and Federated ML: 526 papers (7.9%); votes/paper 5.82; tags: 

### Highest Program-Signal Enrichment
- Theory, Optimization, and Algorithms: oral enrichment 1.45x; awards 1; public enrichment 0.46x
- Safety, Governance, Privacy, and Society: oral enrichment 1.41x; awards 3; public enrichment 0.51x
- LLM Reasoning, Post-Training, and RLVR: oral enrichment 1.29x; awards 2; public enrichment 2.03x
- Agents, Code, and Tool Use: oral enrichment 1.19x; awards 0; public enrichment 1.52x
- AI for Science, Health, and Neuro: oral enrichment 1.08x; awards 0; public enrichment 0.33x

### Highest Public-Attention Enrichment
- Robotics, Embodiment, and World Models: public enrichment 2.11x; oral enrichment 0.81x; votes/paper 19.19
- LLM Reasoning, Post-Training, and RLVR: public enrichment 2.03x; oral enrichment 1.29x; votes/paper 18.55
- Agents, Code, and Tool Use: public enrichment 1.52x; oral enrichment 1.19x; votes/paper 13.87
- Systems and Efficient Foundation Models: public enrichment 1.31x; oral enrichment 0.69x; votes/paper 11.97
- Generative Modeling: public enrichment 0.96x; oral enrichment 0.83x; votes/paper 8.76

### ICML 2026 Overweights vs Accepted-Paper Baseline
- LLM Reasoning, Post-Training, and RLVR: +2.9 pp; relative 1.29x
- Systems and Efficient Foundation Models: +2.1 pp; relative 1.68x
- Agents, Code, and Tool Use: +2.1 pp; relative 1.44x
- Safety, Governance, Privacy, and Society: +1.3 pp; relative 1.17x
- Graphs, Geometry, and Representation Learning: +1.2 pp; relative 1.2x

### Fastest arXiv Query Growth
- Multimodal, Vision, and Perception: 2025 vs 2024 growth 94.6%
- LLM Reasoning, Post-Training, and RLVR: 2025 vs 2024 growth 59.9%
- Safety, Governance, Privacy, and Society: 2025 vs 2024 growth 53.6%
- Systems and Efficient Foundation Models: 2025 vs 2024 growth 43.3%
- Reinforcement Learning and Control: 2025 vs 2024 growth 42.1%

### Highest Artifact Visibility
- Robotics, Embodiment, and World Models: GitHub URL share 38.0%; likely-code share 35.9%
- Agents, Code, and Tool Use: GitHub URL share 32.9%; likely-code share 32.7%
- LLM Reasoning, Post-Training, and RLVR: GitHub URL share 32.1%; likely-code share 31.9%
- Generative Modeling: GitHub URL share 31.1%; likely-code share 30.9%
- Multimodal, Vision, and Perception: GitHub URL share 29.8%; likely-code share 29.4%

## Claim Register

| Claim | Strength | Evidence | Caveat | Next validation |
| --- | --- | --- | --- | --- |
| C01: LLM reasoning center of gravity | strong_for_landscape | 1099 taxonomy papers (16.6%); historical delta +2.9 pp; public-attention enrichment 2.03x. | Area boundaries include general LLM training/evaluation and some diffusion-language papers; paper-level taxonomy still needs review. | Manually inspect boundary clusters 14, 21, and 24 before making subarea-level claims. |
| C02: Infrastructure and agentic workloads | moderate_to_strong | Systems historical delta +2.1 pp, relative 1.68x; Agents historical delta +2.1 pp, relative 1.44x. | Historical comparison uses a keyword scorer; ICML 2025 and NeurIPS 2025 lack static abstracts in the current pull. | Read top positive-delta papers and check whether deltas reflect real venue emphasis or metadata/topic-label differences. |
| C03: Program committee attention | strong_for_triage | Theory oral enrichment 1.45x vs public enrichment 0.46x; Safety oral enrichment 1.41x and 3 awards vs public enrichment 0.51x. | Oral/award counts are program signals, not full quality labels; award counts are small and volatile. | Review low-public/high-program papers to extract the technical reasons for committee interest. |
| C04: Public attention mismatch | moderate | 195 papers (2.9%); public-attention enrichment 2.11x vs oral enrichment 0.81x. | AlphaXiv likely overweights shareable VLA/world-model work and project-page traffic. | Inspect whether the high-attention papers are benchmarks, demos, or reusable models rather than core ICML program emphasis. |
| C05: Neighboring-venue contrast | moderate | 889 taxonomy papers (13.4%); historical delta -3.1 pp, relative 0.82x. | This is the area most sensitive to venue scope and title/topic classification; ICLR/NeurIPS vision-heavy shares may dominate the baseline average. | Break multimodal into vision-language reasoning, video, 3D, and robustness before interpreting the aggregate underweight. |
| C06: External trend context | context_only | Multimodal, Vision, and Perception: 94.6%; LLM Reasoning, Post-Training, and RLVR: 59.9%; Safety, Governance, Privacy, and Society: 53.6%; Systems and Efficient Foundation Models: 43.3% | arXiv queries are broad, overlapping, and not acceptance or quality signals. | Use accepted-paper corpora, not arXiv counts, for publication-ready year-over-year venue claims. |
| C07: Artifact visibility | moderate | Robotics, Embodiment, and World Models: GitHub URL share 38.0%; Agents, Code, and Tool Use: GitHub URL share 32.9%; LLM Reasoning, Post-Training, and RLVR: GitHub URL share 32.1%; Generative Modeling: GitHub URL share 31.1% | GitHub metadata comes from AlphaXiv and does not prove runnable reproduction; some high-star links are templates or index repos. | Clone/check high-signal repositories and separate code, benchmark, dataset, checkpoint, and project-page links. |
| C08: Validation priority | process_claim | 21 of 42 semantic clusters are marked needs_review; validation queue contains 192 papers across 12 areas. | The queue organizes review but does not mean evidence fields have been checked. | Fill validation packets and reconcile reviewed fields back into a checked CSV. |

## How To Use This

- Use `data/processed/icml2026_landscape_signal_matrix.csv` for sorting/filtering areas by signal type.
- Use `data/processed/icml2026_landscape_claim_register.csv` as the backbone for a report outline or slide narrative.
- Use `reports/icml2026_claim_validation_packet_index.md` to review the paper-level evidence behind each major claim.
- Treat claims marked `context_only`, `moderate`, or `process_claim` as prompts for manual review, not final assertions.

## Caveats

- The 12-area taxonomy is a curated seed over semantic clusters; several clusters remain marked `needs_review`.
- Historical accepted-paper deltas use a shared keyword scorer, not the semantic-cluster taxonomy.
- arXiv trends are broad query-count context, not venue acceptance trends.
- AlphaXiv votes and GitHub metadata are public-attention/artifact proxies, not quality or reproducibility proof.
- Program signal means oral/award selection only; it does not capture reviewer scores or full committee deliberation.