# ICML 2026 Safe Statement Register

Wording guardrails for using the current workspace in reports, memos, or presentations.
This register separates what can be said now from what must remain a hypothesis until manual review is filled.

## Snapshot

- Statements tracked: 20
- Type mix: claim: 8, area: 12
- Wording status mix: directional_only: 8, orientation_only: 7, hypothesis_only: 3, context_only: 2

## Claim Guardrails

| ID | Status | Allowed wording | Unsafe wording | Promotion condition |
| --- | --- | --- | --- | --- |
| `C01` LLM reasoning center of gravity | hypothesis_only | Hypothesis from current metadata: LLM reasoning/post-training is the largest ICML 2026 area and is also overweight relative to nearby accepted-paper baselines. | Do not state as settled, paper-validated, causal, or quality-ranked until acceptance gates pass. | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| `C02` Infrastructure and agentic workloads | hypothesis_only | Hypothesis from current metadata: Systems/efficiency and agents/code look smaller than LLM reasoning by paper count, but both are clear ICML 2026 overweights versus the neighboring-venue baseline. | Do not state as settled, paper-validated, causal, or quality-ranked until acceptance gates pass. | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| `C03` Program committee attention | hypothesis_only | Hypothesis from current metadata: Theory and safety/governance receive more program signal than their public-attention signal would predict. | Do not state as settled, paper-validated, causal, or quality-ranked until acceptance gates pass. | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved |
| `C04` Public attention mismatch | directional_only | Directional signal: Robotics/embodiment is small by taxonomy count but unusually strong in public attention. | Do not state as settled, paper-validated, causal, or quality-ranked until acceptance gates pass. | reviewed rows 0/6; support rows 0/4 with 0 weakening rows; paper notes 0/3 |
| `C05` Neighboring-venue contrast | directional_only | Directional signal: Multimodal/vision is large inside ICML 2026 but underweight relative to NeurIPS 2025 and ICLR 2026 accepted-paper baselines. | Do not state as settled, paper-validated, causal, or quality-ranked until acceptance gates pass. | reviewed rows 0/7; support rows 0/4 with 0 weakening rows; paper notes 0/3; taxonomy boundary unresolved |
| `C06` External trend context | context_only | As context only: The fastest broad arXiv growth areas are multimodal/vision, LLM reasoning, and safety/governance, but ICML 2026 does not mirror this ranking exactly. | Do not present this as a paper-quality or venue-quality conclusion. | none |
| `C07` Artifact visibility | directional_only | Directional signal: Artifacts are most visible in agents/code, LLM reasoning, systems, and multimodal/vision, while theory remains much less artifact-linked. | Do not state as settled, paper-validated, causal, or quality-ranked until acceptance gates pass. | reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; artifact checks 0/5 |
| `C08` Validation priority | context_only | As context only: The biggest remaining quality jump is not more plotting; it is paper-level validation of boundary clusters and high-impact claims. | Do not present this as a paper-quality or venue-quality conclusion. | none |

## Area Guardrails

| Area | Status | Allowed wording | Required caveat | First artifact |
| --- | --- | --- | --- | --- |
| LLM Reasoning, Post-Training, and RLVR | orientation_only | For orientation: LLM Reasoning, Post-Training, and RLVR accounts for 16.6% of the corpus; treat the area narrative as unreviewed and risk-sensitive. | Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done. | `reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md` |
| Multimodal, Vision, and Perception | orientation_only | For orientation: Multimodal, Vision, and Perception accounts for 13.4% of the corpus; treat the area narrative as unreviewed and risk-sensitive. | Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done. | `reports/area_briefing_cards/multimodal-vision-and-perception.md` |
| Theory, Optimization, and Algorithms | orientation_only | For orientation: Theory, Optimization, and Algorithms accounts for 11.1% of the corpus; treat the area narrative as unreviewed and risk-sensitive. | Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done. | `reports/area_briefing_cards/theory-optimization-and-algorithms.md` |
| AI for Science, Health, and Neuro | orientation_only | For orientation: AI for Science, Health, and Neuro accounts for 8.9% of the corpus; treat the area narrative as unreviewed and risk-sensitive. | Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done. | `reports/area_briefing_cards/ai-for-science-health-and-neuro.md` |
| Data-Centric, Causal, and Federated ML | orientation_only | For orientation: Data-Centric, Causal, and Federated ML accounts for 7.9% of the corpus; treat the area narrative as unreviewed and risk-sensitive. | Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done. | `reports/area_briefing_cards/data-centric-causal-and-federated-ml.md` |
| Systems and Efficient Foundation Models | orientation_only | For orientation: Systems and Efficient Foundation Models accounts for 7.8% of the corpus; treat the area narrative as unreviewed and risk-sensitive. | Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done. | `reports/area_briefing_cards/systems-and-efficient-foundation-models.md` |
| Agents, Code, and Tool Use | orientation_only | For orientation: Agents, Code, and Tool Use accounts for 7.5% of the corpus; treat the area narrative as unreviewed and risk-sensitive. | Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done. | `reports/area_briefing_cards/agents-code-and-tool-use.md` |
| Safety, Governance, Privacy, and Society | directional_only | Directional area signal: Safety and society papers are programmatically central, but vary sharply in executable evidence. | Use as a directional area signal with explicit taxonomy/baseline caveats. | `reports/area_briefing_cards/safety-governance-privacy-and-society.md` |
| Graphs, Geometry, and Representation Learning | directional_only | Directional area signal: Graph and geometric methods remain a bridge between structure-aware theory and domain-specific representations. | Use as a directional area signal with explicit taxonomy/baseline caveats. | `reports/area_briefing_cards/graphs-geometry-and-representation-learning.md` |
| Generative Modeling | directional_only | Directional area signal: Diffusion and flow models are splitting into practical media generation, language alternatives, and sampling theory. | Use as a directional area signal with explicit taxonomy/baseline caveats. | `reports/area_briefing_cards/generative-modeling.md` |
| Reinforcement Learning and Control | directional_only | Directional area signal: Core RL is active but less publicly amplified than LLM-facing RL, with emphasis on offline learning, control, and computation. | Use as a directional area signal with explicit taxonomy/baseline caveats. | `reports/area_briefing_cards/reinforcement-learning-and-control.md` |
| Robotics, Embodiment, and World Models | directional_only | Directional area signal: Robotics is becoming a high-attention testbed for VLA models, memory, latent actions, and world models. | Use as a directional area signal with explicit taxonomy/baseline caveats. | `reports/area_briefing_cards/robotics-embodiment-and-world-models.md` |

## Falsification Checks

### C01: LLM reasoning center of gravity

- Evidence basis: 1099 taxonomy papers (16.6%); historical delta +2.9 pp; public-attention enrichment 2.03x.
- Required caveat: Area boundaries include general LLM training/evaluation and some diffusion-language papers; paper-level taxonomy still needs review.
- Falsification test: Review boundary papers and relabel any that are mainly systems, safety, or general language-model evaluation; recompute whether LLM reasoning still leads the landscape.
- First artifact to open: `reports/review_reading_briefs/62989-how-much-can-language-models-memorize.md ; reports/review_reading_briefs/61998-the-flexibility-trap-rethinking-the-value-of-arbitrary-order-in-diffus.md ; reports/review_reading_briefs/65332-maximum-likelihood-reinforcement-learning.md ; reports/review_reading_briefs/65886-reinforcement-learning-with-evolving-rubrics-for-deep-research.md`

### C02: Infrastructure and agentic workloads

- Evidence basis: Systems historical delta +2.1 pp, relative 1.68x; Agents historical delta +2.1 pp, relative 1.44x.
- Required caveat: Historical comparison uses a keyword scorer; ICML 2025 and NeurIPS 2025 lack static abstracts in the current pull.
- Falsification test: Read representative systems and agents/code papers and check whether the mechanism is reusable infrastructure, benchmark packaging, or ordinary model training.
- First artifact to open: `reports/review_reading_briefs/65901-neural-thickets-diverse-task-experts-are-dense-around-pretrained-weigh.md ; reports/review_reading_briefs/65206-paperbanana-automating-academic-illustration-for-ai-scientists.md ; reports/review_reading_briefs/66212-controlled-llm-training-on-spectral-sphere.md ; reports/review_reading_briefs/61870-mhc-manifold-constrained-hyper-connections.md`

### C03: Program committee attention

- Evidence basis: Theory oral enrichment 1.45x vs public enrichment 0.46x; Safety oral enrichment 1.41x and 3 awards vs public enrichment 0.51x.
- Required caveat: Oral/award counts are program signals, not full quality labels; award counts are small and volatile.
- Falsification test: Compare low-public/high-program papers against their abstracts/PDFs and label the committee-selection rationale.
- First artifact to open: `reports/review_reading_briefs/66206-to-grok-grokking-provable-grokking-in-ridge-regression.md ; reports/review_reading_briefs/60766-the-obfuscation-atlas-mapping-where-honesty-emerges-in-rlvr-with-decep.md ; reports/review_reading_briefs/67084-position-ai-ml-deepfake-research-is-misaligned-with-ai-generated-non-c.md ; reports/review_reading_briefs/67118-position-the-alignment-community-is-unintentionally-building-a-censors.md`

### C04: Public attention mismatch

- Evidence basis: 195 papers (2.9%); public-attention enrichment 2.11x vs oral enrichment 0.81x.
- Required caveat: AlphaXiv likely overweights shareable VLA/world-model work and project-page traffic.
- Falsification test: Classify high-attention robotics papers as benchmark, demo, reusable model, or core algorithmic contribution and compare with oral/award status.
- First artifact to open: `reports/review_reading_briefs/61757-world-guidance-world-modeling-in-condition-space-for-action-generation.md ; reports/review_reading_briefs/64904-temporal-straightening-for-latent-planning.md ; reports/review_reading_briefs/65457-langforce-bayesian-decomposition-of-vision-language-action-models-via-.md ; reports/review_reading_briefs/62813-vision-language-action-pretraining-from-large-scale-human-videos.md`

### C05: Neighboring-venue contrast

- Evidence basis: 889 taxonomy papers (13.4%); historical delta -3.1 pp, relative 0.82x.
- Required caveat: This is the area most sensitive to venue scope and title/topic classification; ICLR/NeurIPS vision-heavy shares may dominate the baseline average.
- Falsification test: Break the sprint-02 multimodal/vision papers into submodes before interpreting the aggregate underweight/overweight signal.
- First artifact to open: `reports/review_reading_briefs/60542-motion-attribution-for-video-generation.md ; reports/review_reading_briefs/65954-multimodal-nested-learning-for-decoupled-and-coordinated-optimization.md ; reports/review_reading_briefs/65729-exskill-continual-learning-from-experience-and-skills-in-multimodal-ag.md ; reports/review_reading_briefs/63195-babyvision-visual-reasoning-beyond-language.md`

### C06: External trend context

- Evidence basis: Multimodal, Vision, and Perception: 94.6%; LLM Reasoning, Post-Training, and RLVR: 59.9%; Safety, Governance, Privacy, and Society: 53.6%; Systems and Efficient Foundation Models: 43.3%
- Required caveat: arXiv queries are broad, overlapping, and not acceptance or quality signals.
- Falsification test: Run sensitivity checks on broad query terms and accepted-paper baselines before using any trend language.
- First artifact to open: `reports/review_reading_briefs/65901-neural-thickets-diverse-task-experts-are-dense-around-pretrained-weigh.md ; reports/review_reading_briefs/64121-reinforcement-learning-via-self-distillation.md ; reports/review_reading_briefs/63333-gdpo-group-reward-decoupled-normalization-policy-optimization-for-mult.md ; reports/review_reading_briefs/61870-mhc-manifold-constrained-hyper-connections.md`

### C07: Artifact visibility

- Evidence basis: Robotics, Embodiment, and World Models: GitHub URL share 38.0%; Agents, Code, and Tool Use: GitHub URL share 32.9%; LLM Reasoning, Post-Training, and RLVR: GitHub URL share 32.1%; Generative Modeling: GitHub URL share 31.1%
- Required caveat: GitHub metadata comes from AlphaXiv and does not prove runnable reproduction; some high-star links are templates or index repos.
- Falsification test: Open linked repositories for high-signal papers and record license, release state, data/checkpoints, dependencies, and runnable example.
- First artifact to open: `reports/review_reading_briefs/65206-paperbanana-automating-academic-illustration-for-ai-scientists.md ; reports/review_reading_briefs/66596-from-abstraction-to-instantiation-learning-behavioral-representation-f.md ; reports/review_reading_briefs/61382-vision-aligned-latent-reasoning-for-multi-modal-large-language-model.md ; reports/review_reading_briefs/64128-autagent-a-reinforcement-learning-framework-for-tool-augmented-audio-r.md`

### C08: Validation priority

- Evidence basis: 21 of 42 semantic clusters are marked needs_review; validation queue contains 192 papers across 12 areas.
- Required caveat: The queue organizes review but does not mean evidence fields have been checked.
- Falsification test: Audit every report headline against reviewed rows, paper notes, acceptance criteria, and manual caveats before presentation use.
- First artifact to open: `reports/review_reading_briefs/62989-how-much-can-language-models-memorize.md ; reports/review_reading_briefs/66206-to-grok-grokking-provable-grokking-in-ridge-regression.md ; reports/review_reading_briefs/61998-the-flexibility-trap-rethinking-the-value-of-arbitrary-order-in-diffus.md ; reports/review_reading_briefs/65332-maximum-likelihood-reinforcement-learning.md`

### LLM Reasoning, Post-Training, and RLVR: LLM Reasoning, Post-Training, and RLVR

- Evidence basis: 1099 papers (16.6%); oral 1.29x; public 2.03x; historical delta +2.9 pp
- Required caveat: Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done.
- Falsification test: Verify that LLM Reasoning, Post-Training, and RLVR is genuinely over-represented versus nearby accepted venues, not a classifier keyword effect.
- First artifact to open: `reports/area_briefing_cards/llm-reasoning-post-training-and-rlvr.md`

### Multimodal, Vision, and Perception: Multimodal, Vision, and Perception

- Evidence basis: 889 papers (13.4%); oral 0.58x; public 0.80x; historical delta -3.1 pp
- Required caveat: Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done.
- Falsification test: Check whether the venue-share direction and arXiv-growth direction are describing different phenomena, or whether one is an artifact of broad query terms/classifier boundaries.
- First artifact to open: `reports/area_briefing_cards/multimodal-vision-and-perception.md`

### Theory, Optimization, and Algorithms: Theory, Optimization, and Algorithms

- Evidence basis: 737 papers (11.1%); oral 1.45x; public 0.46x; historical delta +0.8 pp
- Required caveat: Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done.
- Falsification test: Adjudicate boundary clusters before making subarea-share or area-rank claims about Theory, Optimization, and Algorithms.
- First artifact to open: `reports/area_briefing_cards/theory-optimization-and-algorithms.md`

### AI for Science, Health, and Neuro: AI for Science, Health, and Neuro

- Evidence basis: 587 papers (8.9%); oral 1.08x; public 0.33x; historical delta +0.9 pp
- Required caveat: Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done.
- Falsification test: Adjudicate boundary clusters before making subarea-share or area-rank claims about AI for Science, Health, and Neuro.
- First artifact to open: `reports/area_briefing_cards/ai-for-science-health-and-neuro.md`

### Data-Centric, Causal, and Federated ML: Data-Centric, Causal, and Federated ML

- Evidence basis: 526 papers (7.9%); oral 0.75x; public 0.64x; historical delta -0.5 pp
- Required caveat: Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done.
- Falsification test: Adjudicate boundary clusters before making subarea-share or area-rank claims about Data-Centric, Causal, and Federated ML.
- First artifact to open: `reports/area_briefing_cards/data-centric-causal-and-federated-ml.md`

### Systems and Efficient Foundation Models: Systems and Efficient Foundation Models

- Evidence basis: 515 papers (7.8%); oral 0.69x; public 1.31x; historical delta +2.1 pp
- Required caveat: Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done.
- Falsification test: Read high-public, non-program papers and decide whether attention reflects novelty, demo visibility, or hype.
- First artifact to open: `reports/area_briefing_cards/systems-and-efficient-foundation-models.md`

### Agents, Code, and Tool Use: Agents, Code, and Tool Use

- Evidence basis: 496 papers (7.5%); oral 1.19x; public 1.52x; historical delta +2.1 pp
- Required caveat: Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done.
- Falsification test: Review representative area-validation papers before turning orientation signals into prose claims.
- First artifact to open: `reports/area_briefing_cards/agents-code-and-tool-use.md`

### Safety, Governance, Privacy, and Society: Safety, Governance, Privacy, and Society

- Evidence basis: 502 papers (7.6%); oral 1.41x; public 0.51x; historical delta +1.3 pp
- Required caveat: Use as a directional area signal with explicit taxonomy/baseline caveats.
- Falsification test: Read program-forward, low-public papers and verify the technical rationale for committee attention.
- First artifact to open: `reports/area_briefing_cards/safety-governance-privacy-and-society.md`

### Graphs, Geometry, and Representation Learning: Graphs, Geometry, and Representation Learning

- Evidence basis: 391 papers (5.9%); oral 0.61x; public 0.38x; historical delta +1.2 pp
- Required caveat: Use as a directional area signal with explicit taxonomy/baseline caveats.
- Falsification test: Review representative area-validation papers before turning orientation signals into prose claims.
- First artifact to open: `reports/area_briefing_cards/graphs-geometry-and-representation-learning.md`

### Generative Modeling: Generative Modeling

- Evidence basis: 379 papers (5.7%); oral 0.83x; public 0.96x; historical delta +0.5 pp
- Required caveat: Use as a directional area signal with explicit taxonomy/baseline caveats.
- Falsification test: Review representative area-validation papers before turning orientation signals into prose claims.
- First artifact to open: `reports/area_briefing_cards/generative-modeling.md`

### Reinforcement Learning and Control: Reinforcement Learning and Control

- Evidence basis: 312 papers (4.7%); oral 0.76x; public 0.66x; historical delta +0.9 pp
- Required caveat: Use as a directional area signal with explicit taxonomy/baseline caveats.
- Falsification test: Review representative area-validation papers before turning orientation signals into prose claims.
- First artifact to open: `reports/area_briefing_cards/reinforcement-learning-and-control.md`

### Robotics, Embodiment, and World Models: Robotics, Embodiment, and World Models

- Evidence basis: 195 papers (2.9%); oral 0.81x; public 2.11x; historical delta +0.4 pp
- Required caveat: Use as a directional area signal with explicit taxonomy/baseline caveats.
- Falsification test: Read high-public, non-program papers and decide whether attention reflects novelty, demo visibility, or hype.
- First artifact to open: `reports/area_briefing_cards/robotics-embodiment-and-world-models.md`

## Outputs

- `data/processed/icml2026_safe_statement_register.csv`
- `reports/icml2026_safe_statement_register.md`