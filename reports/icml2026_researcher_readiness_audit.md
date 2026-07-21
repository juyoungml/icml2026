# ICML 2026 Researcher Readiness Audit

This audit translates the EDA workspace into a practical research judgment map.
It separates directional landscape signals from claims that are ready for publication-grade use.

## Snapshot

- Audited claims: 8
- Audited areas: 12
- Manual review completed: 0/310 (0.0%)
- Claim readiness tiers: context_only_unreviewed: 1, directional_unreviewed: 3, high_priority_unreviewed: 3, workflow_claim_unreviewed: 1
- Area risk tiers: high: 11, moderate_to_high: 1

## What A Researcher Can Safely Use Now

- Official corpus counts, oral flags, award flags, and generated joins are safe as descriptive metadata.
- Area-level patterns are useful for triage when phrased as directional signals rather than final causal claims.
- Public-attention results should be described as AlphaXiv attention, not paper quality.
- Historical deltas should be treated as accepted-paper baseline contrasts, not definitive venue-policy conclusions.

## What Is Not Defensible Yet

- Paper-level support for the eight synthesis claims is not complete because the claim packet manual fields are still blank.
- Subarea-level conclusions are not publication-ready while boundary clusters remain in the review queues.
- Reproducibility claims should not go beyond GitHub URL visibility unless the relevant repositories have been manually checked.
- Benchmark, dataset, metric, and negative-result claims are still heuristic evidence-code outputs.

## Claim Readiness

| Claim | Tier | Rows | Reviewed | Taxonomy Review | Low Confidence | Researcher Use |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| C01 - LLM reasoning center of gravity | high_priority_unreviewed | 14 | 0 | 12 | 1 | Use only as a directional landscape claim until the packet is reviewed. |
| C02 - Infrastructure and agentic workloads | high_priority_unreviewed | 14 | 0 | 5 | 1 | Use only as a directional landscape claim until the packet is reviewed. |
| C03 - Program committee attention | high_priority_unreviewed | 14 | 0 | 3 | 3 | Use only as a directional landscape claim until the packet is reviewed. |
| C04 - Public attention mismatch | directional_unreviewed | 12 | 0 | 0 | 2 | Use as a hypothesis or reading guide. |
| C05 - Neighboring-venue contrast | directional_unreviewed | 14 | 0 | 1 | 1 | Use as a hypothesis or reading guide. |
| C06 - External trend context | context_only_unreviewed | 16 | 0 | 6 | 1 | Use as background context, not as a main thesis. |
| C07 - Artifact visibility | directional_unreviewed | 16 | 0 | 4 | 0 | Use as a hypothesis or reading guide. |
| C08 - Validation priority | workflow_claim_unreviewed | 18 | 0 | 18 | 3 | Use to describe the validation workflow, not the paper landscape. |

## Highest-Priority Claim Packets

- `C01`: Manually inspect boundary clusters 14, 21, and 24 before making subarea-level claims. Risk: Area boundaries include general LLM training/evaluation and some diffusion-language papers; paper-level taxonomy still needs review.
- `C02`: Read top positive-delta papers and check whether deltas reflect real venue emphasis or metadata/topic-label differences. Risk: Historical comparison uses a keyword scorer; ICML 2025 and NeurIPS 2025 lack static abstracts in the current pull.
- `C03`: Review low-public/high-program papers to extract the technical reasons for committee interest. Risk: Oral/award counts are program signals, not full quality labels; award counts are small and volatile.

## Area Risk Map

| Area | Risk | Rows | Reviewed | Taxonomy Review | Low Confidence | Evidence Summary |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| LLM Reasoning, Post-Training, and RLVR | high | 16 | 0 | 15 | 0 | 1099 papers; taxonomy share 16.6%; oral enrichment 1.29x; public enrichment 2.03x; historical delta +2.9 pp |
| AI for Science, Health, and Neuro | high | 16 | 0 | 13 | 1 | 587 papers; taxonomy share 8.9%; oral enrichment 1.08x; public enrichment 0.33x; historical delta +0.9 pp |
| Graphs, Geometry, and Representation Learning | high | 16 | 0 | 12 | 4 | 391 papers; taxonomy share 5.9%; oral enrichment 0.61x; public enrichment 0.38x; historical delta +1.2 pp |
| Data-Centric, Causal, and Federated ML | high | 16 | 0 | 12 | 1 | 526 papers; taxonomy share 7.9%; oral enrichment 0.75x; public enrichment 0.64x; historical delta -0.5 pp |
| Theory, Optimization, and Algorithms | high | 16 | 0 | 9 | 4 | 737 papers; taxonomy share 11.1%; oral enrichment 1.45x; public enrichment 0.46x; historical delta +0.8 pp |
| Systems and Efficient Foundation Models | high | 16 | 0 | 8 | 2 | 515 papers; taxonomy share 7.8%; oral enrichment 0.69x; public enrichment 1.31x; historical delta +2.1 pp |
| Agents, Code, and Tool Use | high | 16 | 0 | 5 | 1 | 496 papers; taxonomy share 7.5%; oral enrichment 1.19x; public enrichment 1.52x; historical delta +2.1 pp |
| Multimodal, Vision, and Perception | moderate_to_high | 16 | 0 | 4 | 1 | 889 papers; taxonomy share 13.4%; oral enrichment 0.58x; public enrichment 0.80x; historical delta -3.1 pp |
| Robotics, Embodiment, and World Models | high | 16 | 0 | 0 | 8 | 195 papers; taxonomy share 2.9%; oral enrichment 0.81x; public enrichment 2.11x; historical delta +0.4 pp |
| Reinforcement Learning and Control | high | 16 | 0 | 0 | 6 | 312 papers; taxonomy share 4.7%; oral enrichment 0.76x; public enrichment 0.66x; historical delta +0.9 pp |
| Generative Modeling | high | 16 | 0 | 0 | 4 | 379 papers; taxonomy share 5.7%; oral enrichment 0.83x; public enrichment 0.96x; historical delta +0.5 pp |
| Safety, Governance, Privacy, and Society | high | 16 | 0 | 0 | 4 | 502 papers; taxonomy share 7.6%; oral enrichment 1.41x; public enrichment 0.51x; historical delta +1.3 pp |

## Most Fragile Areas To Read First

- AI for Science, Health, and Neuro: 13 queued taxonomy-boundary rows; 1 low-confidence evidence rows
- Agents, Code, and Tool Use: 5 queued taxonomy-boundary rows; 1 low-confidence evidence rows; historical baseline interpretation needed
- Data-Centric, Causal, and Federated ML: 12 queued taxonomy-boundary rows; 1 low-confidence evidence rows
- Generative Modeling: 4 low-confidence evidence rows
- Graphs, Geometry, and Representation Learning: 12 queued taxonomy-boundary rows; 4 low-confidence evidence rows
- LLM Reasoning, Post-Training, and RLVR: 15 queued taxonomy-boundary rows; historical baseline interpretation needed
- Reinforcement Learning and Control: 6 low-confidence evidence rows
- Robotics, Embodiment, and World Models: 8 low-confidence evidence rows; large public/program signal gap
- Safety, Governance, Privacy, and Society: 4 low-confidence evidence rows
- Systems and Efficient Foundation Models: 8 queued taxonomy-boundary rows; 2 low-confidence evidence rows; historical baseline interpretation needed
- Theory, Optimization, and Algorithms: 9 queued taxonomy-boundary rows; 4 low-confidence evidence rows; large public/program signal gap

## Evidence Stream Risk

| Evidence stream | Usefulness | Failure mode | Best next check |
| --- | --- | --- | --- |
| Official ICML metadata | High | Mostly structural; title/topic metadata may be sparse | Spot-check paper links and award/oral labels. |
| Manual taxonomy seed | High for report structure | Boundary clusters and mixed semantic clusters | Review queued taxonomy-boundary papers. |
| AlphaXiv votes/visits | Medium | Social attention and recency, not quality | Compare high-public/non-oral against abstracts and paper claims. |
| Historical accepted-paper deltas | Medium | Keyword classifier and uneven abstract coverage | Read largest delta papers and recalibrate labels. |
| arXiv trend queries | Low to medium | Broad overlapping search terms | Use only as external context, not venue evidence. |
| GitHub artifact metadata | Medium for visibility | URL existence does not imply runnable reproduction | Manually inspect high-signal repos. |
| Heuristic evidence codes | Medium for triage | Keyword false positives for methods, metrics, datasets | Fill validation packets and reconcile CSV fields. |

## Recommended Research Workplan

1. Review claim packets C01, C02, C03, and C07 before writing the main landscape thesis.
2. Resolve taxonomy-boundary rows in LLM Reasoning, Systems, Multimodal/Vision, Safety/Governance, and Theory.
3. Manually inspect high-public/non-program papers to decide whether they are community trends, demos, or genuine technical centers.
4. Manually inspect low-public/high-program papers to extract the committee-valued technical ideas.
5. Re-run this audit after filling manual fields; readiness tiers should move from unreviewed to partially checked or publication-ready seed.

## Outputs

- `data/processed/icml2026_researcher_readiness_audit.csv`
- `reports/icml2026_researcher_readiness_audit.md`