# A Newcomer’s Tour of the 12 ICML 2026 Areas

This guide gives you a simple map of the conference. The areas are broad. Some papers belong near the border between two areas, so use the map to ask better questions rather than to force every paper into a perfect box.

## The Map at a Glance

| Area | Plain-language purpose | Papers | Share |
| --- | --- | ---: | ---: |
| LLM Reasoning, Post-Training, and RLVR | Help language models reason, learn from feedback, and use extra work while answering. | 1,099 | 16.6% |
| Multimodal, Vision, and Perception | Help models understand images, video, space, and information across several media. | 889 | 13.4% |
| Theory, Optimization, and Algorithms | Explain why learning methods work and develop mathematical tools for improving them. | 737 | 11.1% |
| AI for Science, Health, and Neuro | Apply and adapt machine learning to scientific, medical, biological, and neural data. | 587 | 8.9% |
| Data-Centric, Causal, and Federated ML | Improve data, reason about cause and effect, and learn across separate data owners. | 526 | 7.9% |
| Systems and Efficient Foundation Models | Make large models faster, smaller, cheaper, and easier to run. | 515 | 7.8% |
| Safety, Governance, Privacy, and Society | Study model risks, privacy, oversight, social effects, and responsible use. | 502 | 7.6% |
| Agents, Code, and Tool Use | Build and test models that plan, write code, and use tools. | 496 | 7.5% |
| Graphs, Geometry, and Representation Learning | Learn from structured relationships, shapes, symmetries, and useful internal representations. | 391 | 5.9% |
| Generative Modeling | Create and study models that generate data, including diffusion and flow models. | 379 | 5.7% |
| Reinforcement Learning and Control | Learn actions and policies through feedback in environments and control problems. | 312 | 4.7% |
| Robotics, Embodiment, and World Models | Connect perception, language, action, memory, and physical environments. | 195 | 2.9% |

These counts are **checked descriptive facts** within the current project taxonomy. The taxonomy assignments themselves still contain boundaries that need human review.

## 1. LLM Reasoning, Post-Training, and RLVR

**Simple idea:** This area asks how language models can solve harder problems after broad pretraining.

Researchers study reward models, reinforcement learning, reasoning traces, verifiers, extra test-time work, preference learning, and new ways to generate language.

**Questions to ask:** Does the method improve real reasoning or only a narrow benchmark? Can the answer be checked cheaply? Does extra computation improve reliability as well as score?

**Connection:** It overlaps with classical reinforcement learning, systems, agents, safety, and theory.

**Common misunderstanding:** Not every LLM training paper is a reasoning paper. This is the project’s largest area, but several of its finer groups need review.

**Start with:** *The Flexibility Trap* and *Reinforcement Learning with Evolving Rubrics for Deep Research* in the paper course.

**Quick check:** Explain one difference between pretraining, post-training, and extra work performed while answering.

## 2. Multimodal, Vision, and Perception

**Simple idea:** This area asks models to understand visual information and connect it with language, space, time, or other media.

Research is moving beyond object recognition toward video reasoning, three-dimensional understanding, grounding, robustness, and visual evidence for answers.

**Questions to ask:** Is the model actually using the image? Can it locate the evidence behind an answer? Does it remain reliable under changes in viewpoint, time, or image quality?

**Connection:** It feeds directly into robotics and also overlaps with generative models and multimodal agents.

**Common misunderstanding:** Being large inside ICML does not mean it is growing faster than every other area. It is large, but its share is lower than in the nearby venue baseline used by this project.

**Start with:** *Motion Attribution for Video Generation* or *Bad Seeing or Bad Thinking?*

**Quick check:** Give one test that could reveal whether a model used visual evidence rather than language shortcuts.

## 3. Theory, Optimization, and Algorithms

**Simple idea:** This area builds mathematical explanations and methods for learning, optimization, probability, and decision-making.

Some papers study classical settings. Others try to explain modern transformer behavior, grokking, attention, or large-scale optimization.

**Questions to ask:** Which assumptions make the result possible? Does the theorem describe the systems people actually use? What changes when model size or data size grows?

**Connection:** Theory supports every other area, but a clean theorem may not immediately predict real model behavior.

**Common misunderstanding:** Low public attention does not mean low conference importance. Theory has high oral enrichment in this workspace.

**Start with:** *To Grok Grokking: Provable Grokking in Ridge Regression*.

**Quick check:** Name one reason a mathematical result may be valuable even when its assumptions do not match a full production model.

## 4. AI for Science, Health, and Neuro

**Simple idea:** This area uses machine learning to understand scientific systems, biological data, health data, time series, and neural signals.

It includes proteins, molecules, climate, physics, medical time series, forecasting, and brain-related data.

**Questions to ask:** Is the evaluation connected to a real scientific decision? Are uncertainty and physical constraints included? Does the method work with limited or biased data?

**Connection:** It often uses graphs, geometry, diffusion models, foundation models, and scientific simulation.

**Common misunderstanding:** A better benchmark score is not automatically a scientific discovery or clinical improvement.

**Start with:** *Protein Autoregressive Modeling via Multiscale Structure Generation*.

**Quick check:** Name one form of scientific validation that a general benchmark score might miss.

## 5. Data-Centric, Causal, and Federated ML

**Simple idea:** This area asks whether learning can improve by changing the data, understanding causes, or training across separate data owners.

It includes data quality, labels, continual learning, causal discovery, and federated learning.

**Questions to ask:** Is the method selecting better data or only adding a new score? Are the causal assumptions justified? Does the federated setup reflect real clients and real constraints?

**Connection:** It touches privacy, safety, scientific validity, and model adaptation.

**Common misunderstanding:** More data is not always better data, and predictive association is not the same as cause.

**Start with:** *Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning*.

**Quick check:** Give an example where changing the data could help more than changing the model.

## 6. Systems and Efficient Foundation Models

**Simple idea:** This area tries to reduce the time, memory, energy, and hardware cost of training and running models.

It includes efficient training, inference, compression, quantization, long-context memory, caching, model architecture, and serving.

**Questions to ask:** Is the speedup measured end to end? Does the model lose reasoning or safety behavior? Does the result work outside one hardware setup?

**Connection:** Efficiency affects whether reasoning, agents, and multimodal systems can be used in practice.

**Common misunderstanding:** A faster kernel does not always make the full application faster.

**Start with:** *Neural Thickets* as a boundary example between efficient adaptation, optimization, and post-training.

**Quick check:** Explain why a faster isolated operation may not make the full model application faster.

## 7. Safety, Governance, Privacy, and Society

**Simple idea:** This area studies how models fail, how people can oversee them, and how ML affects privacy and society.

It includes deception, harmful behavior, privacy attacks, fairness, policy, evaluations, and model oversight.

**Questions to ask:** Is the risk demonstrated or only imagined? Does the test represent real use? Can the proposed safeguard itself be avoided or misused?

**Connection:** Safety questions appear in agents, LLM post-training, data systems, and public deployment.

**Common misunderstanding:** This area contains both technical experiments and broader social or governance arguments. They need different kinds of evidence.

**Start with:** *The Obfuscation Atlas*.

**Quick check:** Give one reason a safety test might fail to represent real-world risk.

## 8. Agents, Code, and Tool Use

**Simple idea:** This area studies systems that take several steps, use tools, write or inspect code, and interact with environments.

Researchers build better planners, tool interfaces, software tasks, agent benchmarks, and multi-agent systems.

**Questions to ask:** Did the model learn a new capability, or did better instructions and scaffolding do the work? Is the evaluation realistic? What happens when tools fail?

**Connection:** Agents combine language models, reinforcement learning, systems, security, and human-computer interaction.

**Common misunderstanding:** A convincing demo does not prove reliable general capability.

**Start with:** *PaperBanana: Automating Academic Illustration for AI Scientists*.

**Quick check:** Name one comparison that could separate better scaffolding from better learned capability.

## 9. Graphs, Geometry, and Representation Learning

**Simple idea:** This area helps models use relationships, shapes, symmetry, and structure.

It includes graph neural networks, geometric learning, manifolds, equivariance, and structured representations.

**Questions to ask:** Which structure is known before training? Does the method respect useful symmetries? Does the representation help outside the chosen benchmark?

**Connection:** These methods are important in molecules, physics, three-dimensional vision, and network data.

**Common misunderstanding:** Adding a graph or geometric layer does not guarantee the model has learned the right structure.

**Start with:** *Which Algorithms Can Graph Neural Networks Learn?*

**Quick check:** Name one kind of prior structure that a graph or geometric model could use.

## 10. Generative Modeling

**Simple idea:** This area studies how models create samples and how generation can become faster, more controllable, or better understood.

It includes diffusion models, flow models, sampling theory, image and video generation, and some alternatives to autoregressive language generation.

**Questions to ask:** What does generation quality mean for this task? How much computing is required? Does control improve without reducing diversity or correctness?

**Connection:** It overlaps heavily with vision, language models, scientific modeling, and theory.

**Common misunderstanding:** “Generative modeling” is not one method. Practical media generation and mathematical sampling theory may have very different goals.

**Start with:** *A Random Matrix Perspective on the Consistency of Diffusion Models*.

**Quick check:** Explain why two generative-model papers might need completely different evaluation measures.

## 11. Reinforcement Learning and Control

**Simple idea:** This area studies how an agent learns actions from feedback over time.

It includes online and offline RL, control, policy learning, exploration, robustness, and computation.

**Questions to ask:** Where does the reward come from? Can the agent explore safely? Does the method work when the environment changes?

**Connection:** Classical RL now sits beside LLM post-training and robotics, but the goals and assumptions can differ greatly.

**Common misunderstanding:** RL used for language-model training is not the whole reinforcement learning field.

**Start with:** *Maximum Likelihood Reinforcement Learning* as a boundary case, then *On Computation and Reinforcement Learning* for the broader area.

**Quick check:** Give one RL problem that does not involve a language model.

## 12. Robotics, Embodiment, and World Models

**Simple idea:** This area connects what a model sees and hears with actions in physical or simulated environments.

It includes vision-language-action models, robot manipulation, memory, latent actions, and world models.

**Questions to ask:** Does the system work outside the training setup? Does it remember enough to act over time? Are improvements tested on real robots or only simulations?

**Connection:** Robotics combines multimodal perception, reinforcement learning, generative world models, and systems constraints.

**Common misunderstanding:** High public attention for robotics does not show broad program dominance. It may partly reflect visually compelling demos and project pages.

**Start with:** *RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies*.

**Quick check:** Describe one robot task where success depends on remembering an earlier observation.

## Area Tour Checkpoint

Try these without looking at the table:

1. Which area studies learning across separate clients?
2. Which two areas most directly meet in a vision-language-action model?
3. Why might a paper belong near the border of theory, systems, and post-training?
4. Name one area where benchmark success may not directly show real-world success.
5. Explain why reinforcement learning appears in more than one area.

Good answers explain the reasoning. Exact wording is not required.
