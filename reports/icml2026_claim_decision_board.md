# ICML 2026 Claim Decision Board

Claim-level operating view for deciding what can be used now and what review action unlocks it.

## Snapshot

- Claims tracked: 8
- Decision mix: not_ready: 6, context_or_workflow_only: 2
- Claim overlay bridge rows: 59
- Sprint 02 claim papers: 16
- Ready-to-transfer bridge rows: 0

## Board

| Claim | Role | Decision | Review | Notes | Sprint 01 bridge | Sprint 02 papers | Next action |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| `C01` LLM reasoning center of gravity | core_thesis_candidate | not_ready | 0/8 | 0/4 | 0/12 ready | 0 | Fill first-sprint paper notes, then transfer decisions through the overlay bridge. |
| `C02` Infrastructure and agentic workloads | core_thesis_candidate | not_ready | 0/8 | 0/4 | 0/14 ready | 0 | Fill first-sprint paper notes, then transfer decisions through the overlay bridge. |
| `C03` Program committee attention | core_thesis_candidate | not_ready | 0/8 | 0/4 | 0/9 ready | 0 | Fill first-sprint paper notes, then transfer decisions through the overlay bridge. |
| `C04` Public attention mismatch | supporting_hypothesis | not_ready | 0/6 | 0/3 | 0/0 ready | 8 | Use sprint 02 paper notes, then transfer decisions through the sprint 02 overlay bridge. |
| `C05` Neighboring-venue contrast | supporting_hypothesis | not_ready | 0/7 | 0/3 | 0/0 ready | 8 | Use sprint 02 paper notes, then transfer decisions through the sprint 02 overlay bridge. |
| `C07` Artifact visibility | supporting_hypothesis | not_ready | 0/8 | 0/4 | 0/6 ready | 0 | Fill first-sprint paper notes, then transfer decisions through the overlay bridge. |
| `C06` External trend context | context_frame | context_or_workflow_only | 0/0 | 0/0 | 0/8 ready | 0 | Keep as framing/context; do not promote as a paper-quality claim. |
| `C08` Validation priority | workflow_claim | context_or_workflow_only | 0/0 | 0/0 | 0/10 ready | 0 | Keep as framing/context; do not promote as a paper-quality claim. |

## First Actions By Claim

### C01: LLM reasoning center of gravity

- Allowed use now: Use as directional hypothesis or reading guide only.
- Missing for promotion: reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved
- Special check: Boundary papers must confirm this is LLM reasoning/post-training rather than broad LLM infrastructure spillover.
- First overlay actions: 1. How much can language models memorize? (62989) -> C01::62989 | 3. The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (61998) -> C01::61998 | 5. Maximum Likelihood Reinforcement Learning (65332) -> C01::65332 | 10. Reinforcement Learning with Evolving Rubrics for Deep Research (65886) -> C01::65886 | 12. Reinforcement Learning via Self-Distillation (64121) -> C01::64121

### C02: Infrastructure and agentic workloads

- Allowed use now: Use as directional hypothesis or reading guide only.
- Missing for promotion: reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved
- Special check: Historical-delta interpretation must survive a spot check of systems and agents/code examples.
- First overlay actions: 4. Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights (65901) -> C02::65901 | 6. PaperBanana: Automating Academic Illustration for AI Scientists (65206) -> C02::65206 | 11. Controlled LLM Training on Spectral Sphere (66212) -> C02::66212 | 15. mHC: Manifold-Constrained Hyper-Connections (61870) -> C02::61870 | 16. Evolution Strategies at the Hyperscale (62943) -> C02::62943

### C03: Program committee attention

- Allowed use now: Use as directional hypothesis or reading guide only.
- Missing for promotion: reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; taxonomy boundary unresolved
- Special check: Low-public/high-program papers must yield concrete technical reasons for committee attention.
- First overlay actions: 2. To Grok Grokking: Provable Grokking in Ridge Regression (66206) -> C03::66206 | 7. The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (60766) -> C03::60766 | 8. Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII) (67084) -> C03::67084 | 9. Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit (67118) -> C03::67118 | 22. Equivalence of Context and Parameter Updates in Modern Transformer Blocks (63048) -> C03::63048

### C04: Public attention mismatch

- Allowed use now: Use as directional hypothesis or reading guide only.
- Missing for promotion: reviewed rows 0/6; support rows 0/4 with 0 weakening rows; paper notes 0/3
- Special check: High-attention robotics papers must be labeled as benchmark, demo, reusable model, or core algorithmic contribution.
- First overlay actions: No sprint overlay target in bridge.

### C05: Neighboring-venue contrast

- Allowed use now: Use as directional hypothesis or reading guide only.
- Missing for promotion: reviewed rows 0/7; support rows 0/4 with 0 weakening rows; paper notes 0/3; taxonomy boundary unresolved
- Special check: Multimodal/vision aggregate must be broken into submodes before interpreting the neighboring-venue contrast.
- First overlay actions: No sprint overlay target in bridge.

### C07: Artifact visibility

- Allowed use now: Use as directional hypothesis or reading guide only.
- Missing for promotion: reviewed rows 0/8; support rows 0/5 with 0 weakening rows; paper notes 0/4; artifact checks 0/5
- Special check: Repository links must be manually inspected for runnable code, data/checkpoints, license, and stale/broken state.
- First overlay actions: 6. PaperBanana: Automating Academic Illustration for AI Scientists (65206) -> C07::65206 | 20. From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model (66596) -> C07::66596 | 27. Vision-aligned Latent Reasoning for Multi-Modal Large Language Model (61382) -> C07::61382 | 28. AuTAgent: A Reinforcement Learning Framework for Tool-Augmented Audio Reasoning (64128) -> C07::64128 | 29. Autoregressive Direct Preference Optimization (65423) -> C07::65423

### C06: External trend context

- Allowed use now: Use as context or workflow framing, not as a field-quality conclusion.
- Missing for promotion: none
- Special check: Use only as external context; do not promote to a venue-quality or acceptance trend claim.
- First overlay actions: 4. Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights (65901) -> C06::65901 | 12. Reinforcement Learning via Self-Distillation (64121) -> C06::64121 | 14. GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (63333) -> C06::63333 | 15. mHC: Manifold-Constrained Hyper-Connections (61870) -> C06::61870 | 16. Evolution Strategies at the Hyperscale (62943) -> C06::62943

### C08: Validation priority

- Allowed use now: Use as context or workflow framing, not as a field-quality conclusion.
- Missing for promotion: none
- Special check: Keep as a process/workflow claim; acceptance means the validation workflow remains explicit and auditable.
- First overlay actions: 1. How much can language models memorize? (62989) -> C08::62989 | 2. To Grok Grokking: Provable Grokking in Ridge Regression (66206) -> C08::66206 | 3. The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (61998) -> C08::61998 | 5. Maximum Likelihood Reinforcement Learning (65332) -> C08::65332 | 10. Reinforcement Learning with Evolving Rubrics for Deep Research (65886) -> C08::65886

## Outputs

- `data/processed/icml2026_claim_decision_board.csv`
- `reports/icml2026_claim_decision_board.md`