# ICML 2026 GitHub Artifact Live Check

This is a bounded live QA pass over high-signal GitHub artifact links.
It uses the GitHub repository API and does not clone repositories, install dependencies, or run code.

## Snapshot

- Repositories checked: 50
- API responses fetched this run: 0
- Live repositories: 49
- Repositories with QA flags: 8
- Cache file: `data/raw/github_artifact_validation_cache.json`

## Flagged Repositories

- academicpages/academicpages.github.io: suspicious_template_or_index; papers: From geometry to dynamics: Learning overdamped Langevin dynamics from sparse observations with geometric constraints
- awesome-NeRF/awesome-NeRF: suspicious_template_or_index; papers: Vision-aligned Latent Reasoning for Multi-Modal Large Language Model
- eliahuhorwitz/Academic-project-page-template: suspicious_template_or_index; papers: From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model
- google/nerfies: archived; stale_pushed_at; papers: Alterbute: Editing Intrinsic Attributes of Objects in Images
- DravenALG/awesome-vla: suspicious_template_or_index; papers: VLANeXt: Recipes for Building Strong VLA Models
- jettbrains/-L-: stale_pushed_at; papers: Agent Learning via Early Experience
- sayantann11/all-classification-templetes-for-ML: stale_pushed_at; papers: Learning to Discover at Test Time
- frankhlchi/SequentialDataVal: not_live_or_api_error; papers: Unifying and Optimizing Data Values for Selection via Sequential Decision-Making

## Highest Live-Star Repositories

- sgl-project/sglang: 30284 stars; license Apache-2.0; pushed 2026-07-14T08:55:29Z
- academicpages/academicpages.github.io: 17296 stars; license MIT; pushed 2026-06-25T13:14:07Z
- dwzhu-pku/PaperBanana: 6775 stars; license Apache-2.0; pushed 2026-06-25T12:48:17Z
- awesome-NeRF/awesome-NeRF: 6773 stars; license MIT; pushed 2025-01-06T11:03:37Z
- z-lab/dflash: 5465 stars; license MIT; pushed 2026-05-10T09:53:33Z
- eliahuhorwitz/Academic-project-page-template: 5069 stars; license unknown; pushed 2025-09-04T19:11:15Z
- ArthurBrussee/brush: 4820 stars; license Apache-2.0; pushed 2026-07-01T21:10:35Z
- ruc-datalab/DeepAnalyze: 4359 stars; license MIT; pushed 2026-07-01T03:12:26Z
- aiming-lab/SimpleMem: 3642 stars; license MIT; pushed 2026-06-23T05:02:47Z
- facebookresearch/sam-audio: 3568 stars; license NOASSERTION; pushed 2026-05-26T05:38:19Z
- nightscout/cgm-remote-monitor: 2786 stars; license AGPL-3.0; pushed 2026-07-08T09:32:27Z
- RoboTwin-Platform/RoboTwin: 2573 stars; license MIT; pushed 2026-07-14T08:49:15Z
- google/nerfies: 1969 stars; license Apache-2.0; pushed 2024-04-22T20:43:02Z
- sierra-research/tau2-bench: 1576 stars; license MIT; pushed 2026-07-14T03:01:06Z
- ByteDance-Seed/Triton-distributed: 1487 stars; license MIT; pushed 2026-07-11T16:20:47Z
- bytedance/SALMONN: 1470 stars; license Apache-2.0; pushed 2026-07-13T08:38:48Z
- Tencent/AngelSlim: 1407 stars; license NOASSERTION; pushed 2026-07-14T08:35:42Z
- aiming-lab/Agent0: 1228 stars; license Apache-2.0; pushed 2026-07-10T07:54:20Z
- StanfordBDHG/OpenTSLM: 1184 stars; license MIT; pushed 2026-05-05T16:01:04Z
- Tencent-Hunyuan/HunyuanWorld-Mirror: 1155 stars; license NOASSERTION; pushed 2026-05-27T03:22:57Z

## Caveats

- A live repository does not imply runnable code, complete data, trained checkpoints, or reproducibility.
- GitHub API metadata is time-sensitive.
- Template, homepage, and awesome-list repositories are flagged because they can inflate star-based artifact signals.
- This script intentionally validates only a bounded candidate set to avoid GitHub API rate-limit surprises.