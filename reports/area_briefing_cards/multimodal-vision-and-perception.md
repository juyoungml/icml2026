# Multimodal, Vision, and Perception

Vision-language work is moving from recognition toward grounded reasoning, spatial understanding, and video/world structure.

## Signal Snapshot

- Papers: 889 (13.4% of corpus)
- Oral enrichment: 0.58x
- Public-attention enrichment: 0.80x
- Historical accepted-paper delta: -3.1 pp
- GitHub URL share: 29.8%
- Manual area-review progress: 0/16 rows reviewed; 16 remaining
- Trust tier: `high_review_need` - 1 taxonomy clusters need review; historical baseline contrast is material; 89 low-confidence evidence-code rows in full area

## Fault Lines

- Perception as feature extraction versus perception as an active reasoning bottleneck.
- Static image benchmarks versus long-video, 3D, spatial, and embodied settings.
- Generative visual models versus discriminative robustness and hallucination control.

## Read For

- Can the method localize the visual evidence behind an answer?
- Does it evaluate temporal, 3D, or physical consistency rather than only caption-style accuracy?
- Are robustness claims tested under realistic corruptions, adversarial prompts, and distribution shift?

## Shape Of The Area

- Top subareas: Vision-language reasoning and video understanding (272); Multimodal representation and cross-modal alignment (237); 3D, video, motion, and spatial understanding (203); Vision robustness, detection, and adversarial perception (177)
- Method-family cues: Reasoning / test-time compute (297); LLM post-training (277); Agents / tool use (231); Graphs / geometry (217); Transformer / attention (189); Diffusion / flow (179); Compression / efficiency (138); RL / policy optimization (127)
- Evaluation-setting cues: vision/video (763); language/llm (468); math/code/verifiable (181); security/safety (133); robotics/embodied (124); theory/synthetic (93); science/domain (58)
- Contribution mix: Benchmark / evaluation (436); Dataset / data resource (141); Method / algorithm (126); Position / conceptual (76); Theory / proof (49); System / infrastructure (35); Application / domain study (16); Uncoded (10)
- Evidence confidence: medium (800); low (89)

## Start Here

- Motion Attribution for Video Generation (Outstanding Paper Honorable Mention; oral; votes=67)
- Holi-Spatial: Evolving Video Streams into Holistic 3D Spatial Intelligence (oral; votes=52; github_stars=356)
- Bad Seeing or Bad Thinking? Rewarding Perception for Multimodal Reasoning (oral; votes=21)
- Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination (oral; votes=16; github_stars=12)
- 3ViewSense: Spatial and Mental Perspective Reasoning from Orthographic Views in Vision-Language Models (oral; votes=11)
- CLEAR: Context-Aware Learning with End-to-End Mask-Free Inference for Adaptive Subtitle Removal (oral; votes=2; github_stars=20)

## Public Attention Not Program-Selected

- A Very Big Video Reasoning Suite (votes=159; github_stars=25)
- Causal-JEPA: Learning World Models through Object-Level Latent Interventions (votes=150; github_stars=206)
- ExSkill: Continual Learning from Experience and Skills in Multimodal Agents (votes=147; github_stars=234)
- BabyVision: Visual Reasoning Beyond Language (votes=134; github_stars=227)
- Utonia: Toward One Encoder for All Point Clouds (votes=118; github_stars=710)
- World-R1: Reinforcing 3D Constraints for Text-to-Video Generation (votes=116; github_stars=406)

## Artifact-Visible Papers To Inspect

- AudioChat: Unified Audio Storytelling, Editing, and Understanding with Transfusion Forcing (votes=14; github_stars=5063) manual-check
- PanoWorld-X: Generating Explorable Panoramic Worlds via Sphere-Aware Video Diffusion (votes=12; github_stars=5063) manual-check
- From Correspondence to Actions: Human-Like Multi-Image Spatial Reasoning in Multi-modal Large Language Models (votes=12; github_stars=5063) manual-check
- Boosting Monocular Metric Depth Estimation via Bokeh Rendering (votes=4; github_stars=5063) manual-check
- Turbo4DGen: Ultra-Fast Acceleration for 4D Generation (votes=0; github_stars=4818)
- SAM Audio: Segment Anything in Audio (votes=65; github_stars=3567)

## Boundary / Taxonomy Review Candidates

- Rectified LpJEPA: Joint-Embedding Predictive Architectures with Sparse and Maximum-Entropy Representations (votes=55; github_stars=79; taxonomy-review)
- On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression (votes=32; taxonomy-review)
- Beyond Accuracy: What Matters in Designing Well-Behaved Image Classification Models? (votes=27; github_stars=20; taxonomy-review)
- Is Training Necessary for Anomaly Detection? (votes=24; github_stars=78; taxonomy-review)
- Alterbute: Editing Intrinsic Attributes of Objects in Images (votes=23; github_stars=1969; taxonomy-review)
- From Per-Image Low-Rank to Encoding Mismatch: Rethinking Feature Distillation in Vision Transformers (votes=19; taxonomy-review)

## What Could Break This Area Story

- The area taxonomy is generated from semantic clusters and curated mappings, not full manual paper reading.
- Public attention is AlphaXiv attention; it can reflect sharing dynamics rather than technical importance.
- GitHub URL share is artifact visibility, not runnable reproducibility.
- Evidence-code labels are heuristic and should be checked against the paper before making benchmark, dataset, metric, or result-character claims.