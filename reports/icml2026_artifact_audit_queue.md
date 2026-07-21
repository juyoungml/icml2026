# ICML 2026 Artifact Audit Queue

Paper-level queue for checking whether artifact links support reproducibility claims.
This uses AlphaXiv GitHub metadata plus the bounded GitHub live-check output when available.

## Snapshot

- Papers queued: 160
- Category mix: high_signal_no_github: 117, linked_needs_repro_check: 18, linked_unchecked_live_status: 4, metadata_suspicious_link: 1, repo_flagged_live_check: 20

## Top Audit Targets

| Rank | Category | Paper | Signal | Repository | Reason |
| ---: | --- | --- | --- | --- | --- |
| 1 | linked_needs_repro_check | When RL Meets Adaptive Speculative Training:  A Unified Training-Serving System | votes 17; stars 30219 | sgl-project/sglang | GitHub URL exists; inspect runnable code, data/checkpoints, license, and reproduction instructions. |
| 2 | repo_flagged_live_check | From geometry to dynamics: Learning overdamped Langevin dynamics from sparse observations with geometric constraints | votes 2; stars 17294 | academicpages/academicpages.github.io | GitHub API QA flags: suspicious_template_or_index |
| 3 | linked_needs_repro_check | Process Reward Models That Think | votes 1815; stars 89 | mukhal/thinkprm | GitHub URL exists; inspect runnable code, data/checkpoints, license, and reproduction instructions. |
| 4 | linked_needs_repro_check | How much can language models memorize? | Outstanding Paper Honorable Mention; oral; votes 271; stars 2 | SimonCao1207/LLM-Capacity | GitHub URL exists; inspect runnable code, data/checkpoints, license, and reproduction instructions. |
| 5 | high_signal_no_github | Motion Attribution for Video Generation | Outstanding Paper Honorable Mention; oral; votes 67; stars 0 | none | High-signal paper has no GitHub URL in AlphaXiv metadata. |
| 6 | repo_flagged_live_check | From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model | oral; votes 14; stars 5069 | eliahuhorwitz/Academic-project-page-template | GitHub API QA flags: suspicious_template_or_index |
| 7 | high_signal_no_github | A Random Matrix Perspective on the Consistency of Diffusion Models | Outstanding Paper Honorable Mention; oral; votes 14; stars 0 | none | High-signal paper has no GitHub URL in AlphaXiv metadata. |
| 8 | high_signal_no_github | High-accuracy sampling for diffusion models and log-concave distributions | Outstanding Paper Award; oral; votes 9; stars 0 | none | High-signal paper has no GitHub URL in AlphaXiv metadata. |
| 9 | high_signal_no_github | To Grok Grokking: Provable Grokking in Ridge Regression | Outstanding Paper Honorable Mention; oral; votes 7; stars 0 | none | High-signal paper has no GitHub URL in AlphaXiv metadata. |
| 10 | high_signal_no_github | Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII) | Outstanding Position Paper Honorable Mention; oral; votes 0; stars 0 | none | High-signal paper has no GitHub URL in AlphaXiv metadata. |
| 11 | high_signal_no_github | Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit | Outstanding Position Paper Award; oral; votes 0; stars 0 | none | High-signal paper has no GitHub URL in AlphaXiv metadata. |
| 12 | linked_unchecked_live_status | The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models | Outstanding Paper Award; oral; votes 92; stars 212 | LeapLabTHU/JustGRPO | GitHub URL exists but is outside the bounded live-check set. |
| 13 | repo_flagged_live_check | Vision-aligned Latent Reasoning for Multi-Modal Large Language Model | votes 56; stars 6773 | awesome-NeRF/awesome-NeRF | GitHub API QA flags: suspicious_template_or_index |
| 14 | linked_unchecked_live_status | The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | Outstanding Paper Honorable Mention; oral; votes 14; stars 13 | AlignmentResearch/obfuscation-atlas | GitHub URL exists but is outside the bounded live-check set. |
| 15 | repo_flagged_live_check | LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model | votes 73; stars 5063 | eliahuhorwitz/Academic-project-page-template | GitHub API QA flags: suspicious_template_or_index |
| 16 | repo_flagged_live_check | Learning to Discover at Test Time | votes 529; stars 297 | sayantann11/all-classification-templetes-for-ML | GitHub API QA flags: stale_pushed_at |
| 17 | repo_flagged_live_check | Hydra-Nav: Object Navigation via Adaptive Dual-Process Reasoning | votes 15; stars 5063 | eliahuhorwitz/Academic-project-page-template | GitHub API QA flags: suspicious_template_or_index |
| 18 | linked_needs_repro_check | PaperBanana: Automating Academic Illustration for AI Scientists | votes 420; stars 6765 | dwzhu-pku/PaperBanana | GitHub URL exists; inspect runnable code, data/checkpoints, license, and reproduction instructions. |
| 19 | repo_flagged_live_check | AudioChat: Unified Audio Storytelling, Editing, and Understanding with Transfusion Forcing | votes 14; stars 5063 | eliahuhorwitz/Academic-project-page-template | GitHub API QA flags: suspicious_template_or_index |
| 20 | repo_flagged_live_check | From Correspondence to Actions: Human-Like Multi-Image Spatial Reasoning in Multi-modal Large Language Models | votes 12; stars 5063 | eliahuhorwitz/Academic-project-page-template | GitHub API QA flags: suspicious_template_or_index |
| 21 | repo_flagged_live_check | PanoWorld-X: Generating Explorable Panoramic Worlds via Sphere-Aware Video Diffusion | votes 12; stars 5063 | eliahuhorwitz/Academic-project-page-template | GitHub API QA flags: suspicious_template_or_index |
| 22 | repo_flagged_live_check | AuTAgent: A Reinforcement Learning Framework for Tool-Augmented Audio Reasoning | votes 8; stars 5063 | eliahuhorwitz/Academic-project-page-template | GitHub API QA flags: suspicious_template_or_index |
| 23 | repo_flagged_live_check | Autoregressive Direct Preference Optimization | votes 6; stars 5063 | eliahuhorwitz/Academic-project-page-template | GitHub API QA flags: suspicious_template_or_index |
| 24 | repo_flagged_live_check | Self-Prompting Diffusion Transformer for Open-Vocabulary Scene Text Edit via In-Context Learning | votes 6; stars 5069 | eliahuhorwitz/Academic-project-page-template | GitHub API QA flags: suspicious_template_or_index |
| 25 | repo_flagged_live_check | Boosting Monocular Metric Depth Estimation via Bokeh Rendering | votes 4; stars 5063 | eliahuhorwitz/Academic-project-page-template | GitHub API QA flags: suspicious_template_or_index |
| 26 | repo_flagged_live_check | Agent Learning via Early Experience | votes 532; stars 148 | jettbrains/-L- | GitHub API QA flags: stale_pushed_at |
| 27 | repo_flagged_live_check | Unifying and Optimizing Data Values for Selection via Sequential Decision-Making | votes 271; stars 0 | frankhlchi/SequentialDataVal | GitHub API QA flags: not_live_or_api_error |
| 28 | linked_needs_repro_check | Reinforcement Learning via Self-Distillation | votes 718; stars 1008 | lasgroup/SDPO | GitHub URL exists; inspect runnable code, data/checkpoints, license, and reproduction instructions. |
| 29 | high_signal_no_github | Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning | oral; votes 98; stars 0 | none | High-signal paper has no GitHub URL in AlphaXiv metadata. |
| 30 | repo_flagged_live_check | VLANeXt: Recipes for Building Strong VLA Models | votes 74; stars 833 | DravenALG/awesome-vla | GitHub API QA flags: suspicious_template_or_index |
| 31 | linked_needs_repro_check | mHC: Manifold-Constrained Hyper-Connections | votes 696; stars 367 | tokenbender/mHC-manifold-constrained-hyper-connections | GitHub URL exists; inspect runnable code, data/checkpoints, license, and reproduction instructions. |
| 32 | linked_needs_repro_check | Self-Distillation Enables Continual Learning | votes 590; stars 653 | idanshen/Self-Distillation | GitHub URL exists; inspect runnable code, data/checkpoints, license, and reproduction instructions. |
| 33 | high_signal_no_github | Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers | oral; votes 75; stars 0 | none | High-signal paper has no GitHub URL in AlphaXiv metadata. |
| 34 | repo_flagged_live_check | Alterbute: Editing Intrinsic Attributes of Objects in Images | votes 23; stars 1969 | google/nerfies | GitHub API QA flags: archived; stale_pushed_at |
| 35 | high_signal_no_github | OPUS: Towards Efficient and Principled Data Selection in Large Language Model Pre-training in Every Iteration | oral; votes 57; stars 0 | none | High-signal paper has no GitHub URL in AlphaXiv metadata. |
| 36 | high_signal_no_github | Learning to Theorize the World from Observation | oral; votes 56; stars 0 | none | High-signal paper has no GitHub URL in AlphaXiv metadata. |
| 37 | linked_needs_repro_check | Monitoring Monitorability | oral; votes 28; stars 2786 | nightscout/cgm-remote-monitor | GitHub URL exists; inspect runnable code, data/checkpoints, license, and reproduction instructions. |
| 38 | repo_flagged_live_check | DADP: Domain Adaptive Diffusion Policy | votes 5; stars 1969 | google/nerfies | GitHub API QA flags: archived; stale_pushed_at |
| 39 | linked_needs_repro_check | DFlash: Block Diffusion for Flash Speculative Decoding | votes 153; stars 5451 | z-lab/dflash | GitHub URL exists; inspect runnable code, data/checkpoints, license, and reproduction instructions. |
| 40 | high_signal_no_github | Less is Enough: Synthesizing Diverse Data in Feature Space of LLMs | oral; votes 48; stars 0 | none | High-signal paper has no GitHub URL in AlphaXiv metadata. |

## Required Manual Checks

- Confirm the linked repository belongs to the paper.
- Identify artifact type: code, benchmark, dataset, checkpoint, project page, index/list, or none.
- Check license and release state.
- Check install/run instructions and whether a minimal example exists.
- Check data/checkpoint availability and whether results can plausibly be reproduced.

## Outputs

- `data/processed/icml2026_artifact_audit_queue.csv`
- `reports/icml2026_artifact_audit_queue.md`