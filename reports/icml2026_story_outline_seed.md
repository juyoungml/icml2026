# ICML 2026 Story Outline Seed

Compact narrative outline for a future presentation or executive briefing. This is not a generated slide deck.

## 12-Part Story Arc

| Step | Message | Figure / Evidence | Validation Hook |
| ---: | --- | --- | --- |
| 1 | What corpus are we analyzing? | `icml2026_papers.csv`: 6,628 rows; `alphaxiv_icml2026_joined.csv`: 6,628 rows | `workspace_validation.md` |
| 2 | ICML 2026 needs a curated taxonomy, not only official topics. | `manual_taxonomy_area_sizes.png`; 12 areas over 42 semantic clusters | `icml2026_manual_taxonomy_seed.md` |
| 3 | LLM reasoning/post-training is the center of gravity. | C01; area share 16.6%; public enrichment 2.03x | C01 claim packet |
| 4 | Systems and agents are the adjacent applied pressure. | C02; historical deltas +2.1 pp each | C02 claim packet |
| 5 | Program signal and public signal disagree. | `program_signal_calibration.png` | C03/C04 packets |
| 6 | Theory and safety are more program-visible than public-visible. | C03; oral enrichments 1.45x and 1.41x | Review low-public/high-program papers |
| 7 | Robotics/world models are public-heavy but small. | C04; 2.9% share; public enrichment 2.11x | Review robotics high-attention papers |
| 8 | Multimodal/vision is big but not uniquely ICML-overweight. | C05; historical delta -3.1 pp | Break down subareas |
| 9 | arXiv growth and accepted-paper baselines answer different questions. | `arxiv_taxonomy_trends.png`; `historical_venue_area_deltas.png` | C06 packet |
| 10 | Artifact visibility is uneven and noisy. | C07; GitHub URL shares; live-check report | C07 packet |
| 11 | The project is strongest as a navigational atlas today. | Claim register + validation queues | C08 packet |
| 12 | The next jump is manual validation, not more charts. | 118 claim-review rows; 192 area-review rows | Reconcile reviewed CSVs |

## Claim-To-Slide Mapping

### C01: LLM reasoning center of gravity

- Message: LLM reasoning/post-training is the largest ICML 2026 area and is also overweight relative to nearby accepted-paper baselines.
- Evidence: 1099 taxonomy papers (16.6%); historical delta +2.9 pp; public-attention enrichment 2.03x.
- Caveat: Area boundaries include general LLM training/evaluation and some diffusion-language papers; paper-level taxonomy still needs review.
- Figures: figures/manual_taxonomy_area_sizes.png, figures/historical_venue_area_deltas.png, figures/arxiv_taxonomy_trends.png
- Review packet: reports/claim_validation_packets/c01-llm-reasoning-center-of-gravity.md

### C02: Infrastructure and agentic workloads

- Message: Systems/efficiency and agents/code look smaller than LLM reasoning by paper count, but both are clear ICML 2026 overweights versus the neighboring-venue baseline.
- Evidence: Systems historical delta +2.1 pp, relative 1.68x; Agents historical delta +2.1 pp, relative 1.44x.
- Caveat: Historical comparison uses a keyword scorer; ICML 2025 and NeurIPS 2025 lack static abstracts in the current pull.
- Figures: figures/historical_venue_area_deltas.png, figures/program_signal_calibration.png
- Review packet: reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md

### C03: Program committee attention

- Message: Theory and safety/governance receive more program signal than their public-attention signal would predict.
- Evidence: Theory oral enrichment 1.45x vs public enrichment 0.46x; Safety oral enrichment 1.41x and 3 awards vs public enrichment 0.51x.
- Caveat: Oral/award counts are program signals, not full quality labels; award counts are small and volatile.
- Figures: figures/program_signal_calibration.png, figures/cluster_public_vs_program_signal.png
- Review packet: reports/claim_validation_packets/c03-program-committee-attention.md

### C04: Public attention mismatch

- Message: Robotics/embodiment is small by taxonomy count but unusually strong in public attention.
- Evidence: 195 papers (2.9%); public-attention enrichment 2.11x vs oral enrichment 0.81x.
- Caveat: AlphaXiv likely overweights shareable VLA/world-model work and project-page traffic.
- Figures: figures/program_signal_calibration.png, figures/manual_taxonomy_area_sizes.png
- Review packet: reports/claim_validation_packets/c04-public-attention-mismatch.md

### C05: Neighboring-venue contrast

- Message: Multimodal/vision is large inside ICML 2026 but underweight relative to NeurIPS 2025 and ICLR 2026 accepted-paper baselines.
- Evidence: 889 taxonomy papers (13.4%); historical delta -3.1 pp, relative 0.82x.
- Caveat: This is the area most sensitive to venue scope and title/topic classification; ICLR/NeurIPS vision-heavy shares may dominate the baseline average.
- Figures: figures/historical_venue_area_deltas.png, figures/arxiv_taxonomy_trends.png
- Review packet: reports/claim_validation_packets/c05-neighboring-venue-contrast.md

### C06: External trend context

- Message: The fastest broad arXiv growth areas are multimodal/vision, LLM reasoning, and safety/governance, but ICML 2026 does not mirror this ranking exactly.
- Evidence: Multimodal, Vision, and Perception: 94.6%; LLM Reasoning, Post-Training, and RLVR: 59.9%; Safety, Governance, Privacy, and Society: 53.6%; Systems and Efficient Foundation Models: 43.3%
- Caveat: arXiv queries are broad, overlapping, and not acceptance or quality signals.
- Figures: figures/arxiv_taxonomy_trends.png, figures/historical_venue_area_deltas.png
- Review packet: reports/claim_validation_packets/c06-external-trend-context.md

### C07: Artifact visibility

- Message: Artifacts are most visible in agents/code, LLM reasoning, systems, and multimodal/vision, while theory remains much less artifact-linked.
- Evidence: Robotics, Embodiment, and World Models: GitHub URL share 38.0%; Agents, Code, and Tool Use: GitHub URL share 32.9%; LLM Reasoning, Post-Training, and RLVR: GitHub URL share 32.1%; Generative Modeling: GitHub URL share 31.1%
- Caveat: GitHub metadata comes from AlphaXiv and does not prove runnable reproduction; some high-star links are templates or index repos.
- Figures: figures/manual_taxonomy_area_sizes.png, figures/alphaxiv_attention_distributions.png
- Review packet: reports/claim_validation_packets/c07-artifact-visibility.md

### C08: Validation priority

- Message: The biggest remaining quality jump is not more plotting; it is paper-level validation of boundary clusters and high-impact claims.
- Evidence: 21 of 42 semantic clusters are marked needs_review; validation queue contains 192 papers across 12 areas.
- Caveat: The queue organizes review but does not mean evidence fields have been checked.
- Figures: figures/semantic_cluster_map.png, figures/evidence_contribution_mix.png
- Review packet: reports/claim_validation_packets/c08-validation-priority.md

## Presentation Guardrails

- Do not present AlphaXiv votes as quality.
- Do not present GitHub URLs as reproducibility.
- Do not present arXiv query growth as accepted-paper growth.
- Do not make subarea-level claims for `needs_review` clusters without manual packet review.
- Keep program signal language precise: oral/award labels are committee-visible signals, not exhaustive quality labels.