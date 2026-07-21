# Historical Accepted-Paper Baseline Against ICML 2026

This report compares ICML 2026 against accepted-paper corpora from ICML 2025, NeurIPS 2025, and ICLR 2026 using the same transparent keyword scorer over titles, topics, and available abstracts.

## Source Coverage

| Source | Paper rows | Abstract coverage | Notes |
| --- | ---: | ---: | --- |
| ICML 2026 | 6,628 | 6,628 (100.0%) | local official ICML 2026 processed table with abstracts |
| ICML 2025 | 3,339 | 0 (0.0%) | official virtual JSON; abstracts unavailable from static endpoint |
| NeurIPS 2025 | 5,858 | 0 (0.0%) | official virtual JSON; abstracts unavailable from static endpoint |
| ICLR 2026 | 5,468 | 5,468 (100.0%) | official virtual JSON plus static abstracts |

## Classification Health

| Venue | High/medium-confidence rows | Uncoded rows |
| --- | ---: | ---: |
| ICML 2026 | 4,565 (68.9%) | 100 (1.5%) |
| ICML 2025 | 1,188 (35.6%) | 627 (18.8%) |
| NeurIPS 2025 | 2,615 (44.6%) | 771 (13.2%) |
| ICLR 2026 | 4,009 (73.3%) | 62 (1.1%) |

## Largest ICML 2026 Overweights vs Baseline Average

| Area | ICML 2026 share | Baseline avg | Delta | Relative |
| --- | ---: | ---: | ---: | ---: |
| LLM Reasoning, Post-Training, and RLVR | 12.8% | 9.9% | +2.9% | 1.29x |
| Systems and Efficient Foundation Models | 5.3% | 3.1% | +2.1% | 1.68x |
| Agents, Code, and Tool Use | 6.9% | 4.8% | +2.1% | 1.44x |
| Safety, Governance, Privacy, and Society | 9.1% | 7.8% | +1.3% | 1.17x |
| Graphs, Geometry, and Representation Learning | 7.5% | 6.3% | +1.2% | 1.2x |
| Reinforcement Learning and Control | 7.8% | 6.9% | +0.9% | 1.13x |

## Largest ICML 2026 Underweights vs Baseline Average

| Area | ICML 2026 share | Baseline avg | Delta | Relative |
| --- | ---: | ---: | ---: | ---: |
| Multimodal, Vision, and Perception | 13.9% | 17.0% | -3.1% | 0.82x |
| Data-Centric, Causal, and Federated ML | 3.9% | 4.4% | -0.5% | 0.89x |

## Venue Shares by Area

| Area | ICML 2026 | ICML 2025 | NeurIPS 2025 | ICLR 2026 |
| --- | ---: | ---: | ---: | ---: |
| Multimodal, Vision, and Perception | 13.9% | 8.3% | 20.7% | 22.0% |
| Theory, Optimization, and Algorithms | 12.8% | 14.7% | 11.7% | 9.8% |
| LLM Reasoning, Post-Training, and RLVR | 12.8% | 7.8% | 8.6% | 13.5% |
| AI for Science, Health, and Neuro | 9.4% | 9.0% | 8.4% | 8.3% |
| Safety, Governance, Privacy, and Society | 9.1% | 8.0% | 7.2% | 8.0% |
| Reinforcement Learning and Control | 7.8% | 6.1% | 6.2% | 8.3% |
| Graphs, Geometry, and Representation Learning | 7.5% | 7.2% | 5.9% | 5.7% |
| Generative Modeling | 7.3% | 7.0% | 6.0% | 7.7% |
| Agents, Code, and Tool Use | 6.9% | 4.1% | 3.6% | 6.6% |
| Systems and Efficient Foundation Models | 5.3% | 3.0% | 2.2% | 4.2% |
| Data-Centric, Causal, and Federated ML | 3.9% | 5.5% | 4.8% | 2.9% |
| Robotics, Embodiment, and World Models | 1.8% | 0.7% | 1.5% | 2.0% |

## Interpretation Notes

- This is an accepted-paper baseline, not an arXiv-volume baseline. It answers a different question from `reports/arxiv_taxonomy_trends.md`.
- The comparison uses one common keyword scorer for all venues, so ICML 2026 shares here will differ from the semantic-cluster manual taxonomy shares.
- ICML 2025 and NeurIPS 2025 static endpoints did not expose abstracts from the probed URL, so their classifications rely on title and topic metadata.
- Broad terms such as `optimization`, `policy`, `graph`, `visual`, and `generative` can create false positives. Treat deltas as triage signals for manual review, not as final claims.
- The most publication-ready use is to identify where to inspect papers manually: large positive deltas suggest ICML 2026 emphasis; large negative deltas suggest areas stronger in neighboring venues.