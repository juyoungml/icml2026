# ICML 2026 Baseline Sensitivity Queue

Spot-check queue for using historical accepted-paper baselines and broad arXiv query trends responsibly.

## Summary

- Areas queued: 12
- High-risk areas: 2
- Moderate-risk areas: 2
- Context-only areas: 8

## How To Use

- Treat this as a QA layer, not a final source of truth.
- Prioritize high-risk rows before writing claims about field momentum or venue emphasis.
- Keep historical-baseline claims separate from arXiv-preprint claims unless both survive spot checks.

## Queue

| Risk | Area | Historical delta | arXiv growth | Issue types | Check question |
| --- | --- | ---: | ---: | --- | --- |
| high | Multimodal, Vision, and Perception | -3.1 pp | 94.6% | historical_delta_sensitive; arxiv_query_sensitive; baseline_disagreement | Check whether the venue-share direction and arXiv-growth direction are describing different phenomena, or whether one is an artifact of broad query terms/classifier boundaries. |
| high | LLM Reasoning, Post-Training, and RLVR | +2.9 pp | 59.9% | historical_delta_sensitive; arxiv_query_sensitive | Verify that LLM Reasoning, Post-Training, and RLVR is genuinely over-represented versus nearby accepted venues, not a classifier keyword effect. |
| moderate | Systems and Efficient Foundation Models | +2.1 pp | 43.3% | historical_delta_sensitive | Verify that Systems and Efficient Foundation Models is genuinely over-represented versus nearby accepted venues, not a classifier keyword effect. |
| moderate | Safety, Governance, Privacy, and Society | +1.3 pp | 53.6% | arxiv_query_sensitive | Test alternate arXiv query terms and inspect whether generic terms are inflating the growth estimate. |
| context | Agents, Code, and Tool Use | +2.1 pp | 33.0% | classifier_spot_check | Spot-check representative titles and boundary papers before using this as more than directional context. |
| context | Graphs, Geometry, and Representation Learning | +1.2 pp | 29.3% | classifier_spot_check | Spot-check representative titles and boundary papers before using this as more than directional context. |
| context | Reinforcement Learning and Control | +0.9 pp | 42.1% | classifier_spot_check | Spot-check representative titles and boundary papers before using this as more than directional context. |
| context | AI for Science, Health, and Neuro | +0.9 pp | 14.9% | classifier_spot_check | Spot-check representative titles and boundary papers before using this as more than directional context. |
| context | Theory, Optimization, and Algorithms | +0.8 pp | 30.0% | classifier_spot_check | Spot-check representative titles and boundary papers before using this as more than directional context. |
| context | Data-Centric, Causal, and Federated ML | -0.5 pp | 27.9% | classifier_spot_check | Spot-check representative titles and boundary papers before using this as more than directional context. |
| context | Generative Modeling | +0.5 pp | 32.1% | classifier_spot_check | Spot-check representative titles and boundary papers before using this as more than directional context. |
| context | Robotics, Embodiment, and World Models | +0.4 pp | 23.7% | classifier_spot_check | Spot-check representative titles and boundary papers before using this as more than directional context. |

## High-Risk Detail

### Multimodal, Vision, and Perception

- ICML 2026 share: 13.4%; historical baseline share: 17.0%.
- Recommended action: sample historical high-confidence and low-margin classifications; rerun narrower and broader arXiv query variants; write a caveat separating ICML program mix from field-wide preprint momentum.
- Safe language: Use only as a hypothesis until spot checks confirm direction and query robustness.
- ICML 2026 examples: Motion Attribution for Video Generation | Holi-Spatial: Evolving Video Streams into Holistic 3D Spatial Intelligence | Bad Seeing or Bad Thinking? Rewarding Perception for Multimodal Reasoning | Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination
- Historical examples: MoCa: Modeling Object Consistency for 3D Camera Control in Video Generation | 3D Scene Prompting for Scene-Consistent Camera-Controllable Video Generation | Beyond Visual Reconstruction Quality: Object Perception-aware 3D Gaussian Splatting for Autonomous Driving | Vid-LLM: A Compact Video-based 3D Multimodal LLM with Reconstruction–Reasoning Synergy

### LLM Reasoning, Post-Training, and RLVR

- ICML 2026 share: 16.6%; historical baseline share: 9.9%.
- Recommended action: sample historical high-confidence and low-margin classifications; rerun narrower and broader arXiv query variants.
- Safe language: Use only as a hypothesis until spot checks confirm direction and query robustness.
- ICML 2026 examples: How much can language models memorize? | The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models | Maximum Likelihood Reinforcement Learning | Reinforcement Learning with Evolving Rubrics for Deep Research
- Historical examples: Plan-Answer-Refine-on-Graph: Structured Planning and Self-Refinement for Large Language Model Reasoning on Knowledge Graphs | Quantile Advantage Estimation: Stabilizing RLVR for LLM Reasoning | Towards Understanding Valuable Preference Data for Large Language Model Alignment | Beyond Magnitude: Leveraging Direction of RLVR Updates for LLM Reasoning

## Outputs

- `data/processed/icml2026_baseline_sensitivity_queue.csv`
- `reports/icml2026_baseline_sensitivity_queue.md`