# ICML 2026 Sprint Pre-Review Suggestions

Machine-generated prompts for the first review sprint.
These are not manual judgments; use them to accelerate PDF reading and paper-note entry.

## Snapshot

- Sprint papers covered: 40
- Papers with claim links: 40
- Papers with artifact prompts: 32

## First Papers

| Rank | Paper | Contribution hypothesis | Evidence to verify | Warning |
| ---: | --- | --- | --- | --- |
| 1 | How much can language models memorize? | Dataset / data resource: We propose a new method for estimating how much a model knows about a datapoint and use it to measure the capacity of modern language models. | identify baselines, datasets, metrics, ablations, and negative cases from the PDF | Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. Taxonomy assignment may be unstable. |
| 2 | To Grok Grokking: Provable Grokking in Ridge Regression | Theory / proof: We study *grokking* - the onset of generalization long after overfitting - in a classical ridge regression setting. | check theorem assumptions and empirical/theory split | Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. Heuristic evidence tag is low confidence. Taxonomy assignment may be unstable. |
| 3 | The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models | Method / algorithm: We find that dLLMs tend to exploit this order flexibility to bypass high-uncertainty tokens that are crucial for exploration, leading to a premature collapse of solution coverage. | metrics: accuracy; check theorem assumptions and empirical/theory split | Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. Taxonomy assignment may be unstable. |
| 4 | Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights | Position / conceptual: We show that in smaller or insufficiently trained models such expert solutions occupy a negligible fraction of the volume of this distribution, making their discovery reliant on structured optimization methods such as gradient descent. | identify baselines, datasets, metrics, ablations, and negative cases from the PDF | Do not treat AlphaXiv attention as quality. Heuristic evidence tag is low confidence. Taxonomy assignment may be unstable. |
| 5 | Maximum Likelihood Reinforcement Learning | Method / algorithm: We show that for binary correctness tasks, expected-reward RL is a first-order approximation of the maximum likelihood objective, yielding vanishing learning signal on low-success inputs. | metrics: pass@k; reward; check theorem assumptions and empirical/theory split | Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. Taxonomy assignment may be unstable. |
| 6 | PaperBanana: Automating Academic Illustration for AI Scientists | Benchmark / evaluation: To lift this burden, we introduce PaperBanana, an agentic framework for automated generation of publication-ready academic illustrations. | benchmarks: PaperBananaBench | Do not treat AlphaXiv attention as quality. |
| 7 | The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | Position / conceptual: We introduce a taxonomy of possible outcomes when training against a deception detector. | metrics: reward | Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. |
| 8 | Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII) | Position / conceptual: AI-generated non-consensual intimate imagery (AIG-NCII) is not adequately addressed in AI/ML literature regarding AI-generated media, commonly referred to as "deepfakes". | identify baselines, datasets, metrics, ablations, and negative cases from the PDF | Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. |
| 9 | Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit | Position / conceptual: By mapping current alignment techniques to the possibility and actual cases of misuse, we show that the quest for a ''perfectly aligned'' model inadvertently also provides malicious actors with an ever-improving tool for informational dominance. | check human-study or user-evaluation setup | Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. |
| 10 | Reinforcement Learning with Evolving Rubrics for Deep Research | Benchmark / evaluation: Using RLER, we develop **Deep Research Tulu (DR Tulu-8B)**, the first fully open model that is directly trained for open-ended, long-form deep research. | identify baselines, datasets, metrics, ablations, and negative cases from the PDF | Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. Taxonomy assignment may be unstable. |
| 11 | Controlled LLM Training on Spectral Sphere | Theory / proof: To address this limitation, we introduce the **Spectral Sphere Optimizer (SSO)**, which enforces strict module-wise spectral constraints on both weights and their updates. | check theorem assumptions and empirical/theory split | Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. Taxonomy assignment may be unstable. |
| 12 | Reinforcement Learning via Self-Distillation | Benchmark / evaluation: Large language models are increasingly post-trained with reinforcement learning in verifiable domains such as code and math. | benchmarks: LiveCodeBench; metrics: accuracy; reward; check theorem assumptions and empirical/theory split | Do not treat AlphaXiv attention as quality. Taxonomy assignment may be unstable. |
| 13 | Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers | Position / conceptual: We find that AOs can recover information fine-tuned into a model (e.g., biographical knowledge or malign propensities) that does not appear in the input text, despite never being trained with activations from a fine-tuned model. | benchmarks: LatentQA; LatentQA-trained; check theorem assumptions and empirical/theory split | Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. Taxonomy assignment may be unstable. |
| 14 | GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization | Theory / proof: In this paper, we demonstrate that directly applying GRPO to normalize distinct rollout reward combinations causes them to collapse into identical advantage values, reducing the resolution of the training signal and resulting in suboptimal convergence and, in some cases, early training failure. | metrics: accuracy; reward; check theorem assumptions and empirical/theory split; check human-study or user-evaluation setup | Do not treat AlphaXiv attention as quality. Taxonomy assignment may be unstable. |
| 15 | mHC: Manifold-Constrained Hyper-Connections | System / infrastructure: To address these challenges, we propose Manifold-Constrained Hyper-Connections (mHC), a general framework that projects the residual connection space of HC onto a specific manifold to restore the identity mapping property, while incorporating rigorous infrastructure optimization to ensure efficiency. | metrics: memory; check theorem assumptions and empirical/theory split | Do not treat AlphaXiv attention as quality. Taxonomy assignment may be unstable. |

## How To Use

- Copy useful parts into `data/manual/icml2026_review_sprint_01_paper_notes.csv` only after reading the paper source.
- Treat every suggestion as a hypothesis derived from title/abstract/tags.
- Prefer the PDF over these suggestions when they disagree.

## Outputs

- `data/processed/icml2026_sprint_prereview_suggestions.csv`
- `reports/icml2026_sprint_prereview_suggestions.md`