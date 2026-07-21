# The 12-Paper ICML 2026 Newcomer Course

This course connects the conference map to real papers. It is not a “best papers” ranking. The papers were chosen because together they show major trends, different kinds of evidence, and important classification problems.

The first eight lessons use locally inspected PDF pages. Their notes are still conservative seed judgments, not completed human review. The final four are wider-view spotlights based on conference metadata and briefing cards. Read the full paper before making a technical claim from those four.

## How to Read Each Paper

Ask five questions:

1. What problem is being solved?
2. What is the main contribution?
3. What evidence supports it?
4. What is one important limit?
5. Why does it matter for the conference map?

## Course Order

| Lesson | Paper | Main reason to read |
| ---: | --- | --- |
| 1 | How much can language models memorize? | Learn why area boundaries matter. |
| 2 | To Grok Grokking | See why theory can receive strong program attention. |
| 3 | The Flexibility Trap | Study reasoning, diffusion language models, and post-training together. |
| 4 | Neural Thickets | Explore the border between optimization, efficiency, and post-training. |
| 5 | Maximum Likelihood Reinforcement Learning | Compare broad RL with LLM-facing RL. |
| 6 | PaperBanana | See an agentic workflow and learn to question artifact claims. |
| 7 | The Obfuscation Atlas | Connect post-training with safety and deception. |
| 8 | Reinforcement Learning with Evolving Rubrics for Deep Research | Study reward design for open-ended work. |
| 9 | Motion Attribution for Video Generation | Connect causal questions with video generation. |
| 10 | Which Algorithms Can Graph Neural Networks Learn? | Connect graph learning with theory. |
| 11 | RoboMME | Study memory and evaluation for robotic generalist policies. |
| 12 | Protein Autoregressive Modeling via Multiscale Structure Generation | See how foundation-model ideas enter scientific ML. |

## Lesson 1: How Much Can Language Models Memorize?

**Area in the current map:** LLM Reasoning, Post-Training, and RLVR

**The problem:** Large language models can both generalize and memorize. The paper asks how much information they can memorize and how that changes with model and dataset size.

**The contribution:** It defines a way to estimate memorization and studies many controlled model and data settings.

**The evidence:** Synthetic bitstrings, real text, model-size sweeps, training and test loss, memorization bits, and membership-inference behavior.

**The limit:** This is central LLM capability work, but it is not mainly about reasoning or RL with verifiable rewards.

**Why it matters:** It is an excellent warning that a broad area count can contain papers from a neighboring topic. The paper supports learning about model capacity while weakening an overly narrow label for its subarea.

**Read next:** [PDF review card](pdf_review_cards/62989.md)

**Checkpoint:** Would you keep this paper in the broad LLM area? Would you change its subarea? Explain both choices.

## Lesson 2: To Grok Grokking: Provable Grokking in Ridge Regression

**Area:** Theory, Optimization, and Algorithms

**The problem:** Grokking describes delayed generalization: a model first fits the training data and only later improves on unseen data. The paper asks whether this behavior can be explained mathematically.

**The contribution:** It develops a theoretical account of grokking in ridge regression and gives bounds on when generalization appears.

**The evidence:** Proofs in an over-parameterized linear setting, simulations, and checks beyond the core linear model.

**The limit:** A clean result in ridge regression does not automatically explain every large neural network.

**Why it matters:** The paper shows one reason theory may receive strong program attention even when it receives less public attention. It offers depth that is harder to see from a short demo.

**Read next:** [PDF review card](pdf_review_cards/66206.md)

**Checkpoint:** What would you need to test before applying this paper’s explanation directly to large language models?

## Lesson 3: The Flexibility Trap

**Full title:** The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models

**Area:** LLM Reasoning, Post-Training, and RLVR

**The problem:** Diffusion language models can generate tokens in flexible orders. The paper asks whether that flexibility actually helps reasoning.

**The contribution:** It argues that arbitrary-order generation can reduce reasoning potential in the checked settings and studies a simpler autoregressive reinforcement-learning approach.

**The evidence:** Mathematics and coding tasks, pass-at-k comparisons, reasoning accuracy, and matched training comparisons.

**The limit:** Results from reasoning and coding do not show that arbitrary-order generation is unhelpful for every task.

**Why it matters:** It connects a major reasoning trend with generative-model design and shows why method details matter more than broad labels.

**Read next:** [PDF review card](pdf_review_cards/61998.md)

**Checkpoint:** Rewrite the paper’s implication twice: once as an unsafe universal claim and once as a careful task-limited claim.

## Lesson 4: Neural Thickets

**Full title:** Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights

**Area in the current map:** Systems and Efficient Foundation Models

**The problem:** Adapting a large pretrained model can be expensive. The paper asks whether useful task-specific models already exist near the pretrained weights.

**The contribution:** It samples weight changes, studies the density of useful solutions, and proposes a random-search adaptation method called RandOpt.

**The evidence:** Tasks in mathematics, writing, programming, chemistry, and synthetic settings; solution-density and computing-efficiency measurements; selected optimization comparisons.

**The limit:** Its connection to infrastructure is indirect. It may fit optimization or post-training as well as systems.

**Why it matters:** It is a boundary paper. The lesson is not only what the method does, but how the same paper can support several conference stories.

**Read next:** [PDF review card](pdf_review_cards/65901.md)

**Checkpoint:** Give the best argument for placing this paper in systems and the best argument for placing it in optimization.

## Lesson 5: Maximum Likelihood Reinforcement Learning

**Area in the current map:** LLM Reasoning, Post-Training, and RLVR

**The problem:** Standard reinforcement learning objectives may not directly optimize the likelihood of success across repeated samples.

**The contribution:** The paper develops a sampling-based maximum-likelihood view of reinforcement learning for binary outcome tasks.

**The evidence:** Mathematical analysis and examples including navigation, code generation, and mathematical problem solving. Reported measures include pass-at-k-style success and computing tradeoffs.

**The limit:** The method is broader than language-model reasoning. Its classification should acknowledge the border with general reinforcement learning and optimization.

**Why it matters:** It prevents the newcomer from assuming that every RL paper involving code or mathematics belongs only to the LLM trend.

**Read next:** [PDF review card](pdf_review_cards/65332.md)

**Checkpoint:** Which parts of the paper are specific to language models, and which parts appear to apply more broadly?

## Lesson 6: PaperBanana

**Full title:** PaperBanana: Automating Academic Illustration for AI Scientists

**Area:** Agents, Code, and Tool Use

**The problem:** Creating a clear academic method figure takes design work, domain understanding, and repeated revision.

**The contribution:** The paper builds an agentic workflow for reference retrieval, planning, rendering, and self-review. It also introduces PaperBananaBench with 292 methodology-diagram examples.

**The evidence:** Comparisons with diagram-generation systems and measures of faithfulness, conciseness, readability, and appearance.

**The limit:** The repository and benchmark still need direct inspection. Good scores also do not settle how well the system handles unusual research ideas.

**Why it matters:** It is a clear example of agents moving into real research workflows. It also teaches the difference between a visible artifact and a checked artifact.

**Read next:** [PDF review card](pdf_review_cards/65206.md)

**Checkpoint:** Design one test that checks the agent system rather than only the final image.

## Lesson 7: The Obfuscation Atlas

**Full title:** The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes

**Area:** Safety, Governance, Privacy, and Society

**The problem:** If a model is trained against a deception detector, will it become honest or learn to hide its behavior?

**The contribution:** The paper creates deception probes and a set of outcome categories, including honest behavior, obvious deception, and forms of obfuscation.

**The evidence:** A coding reward-hacking environment, probe scores, model-representation changes, task returns, and comparisons involving detector penalties and regularized training.

**The limit:** A focused coding environment cannot measure every form of deception or real-world safety risk.

**Why it matters:** It connects two visible trends: RL-based post-training and technical safety. It also gives a concrete reason why safety research can receive strong program attention.

**Read next:** [PDF review card](pdf_review_cards/60766.md)

**Checkpoint:** Why would lower detector scores fail to prove that a model became honest?

## Lesson 8: Reinforcement Learning with Evolving Rubrics for Deep Research

**Area:** LLM Reasoning, Post-Training, and RLVR

**The problem:** Open-ended research answers are harder to score than mathematics problems with one checkable answer.

**The contribution:** The paper uses search-grounded rubrics that change along with the policy during reinforcement learning.

**The evidence:** Deep-research benchmarks including SQAv2, DeepResearchBench, ResearchQA, and HealthBench; reported performance and cost measures; comparisons with open and proprietary systems.

**The limit:** Repository contents and evaluation protocols still need checking. Comparisons with proprietary systems may not use perfectly matched conditions.

**Why it matters:** It shows how RL is expanding from easily checked answers toward longer and more open-ended work.

**Read next:** [PDF review card](pdf_review_cards/65886.md)

**Checkpoint:** Why is reward design harder for a research report than for a simple arithmetic answer?

## Lesson 9: Motion Attribution for Video Generation

**Evidence level for this lesson:** Metadata and briefing-card spotlight. Read the full paper before making a technical claim.

**Area:** Multimodal, Vision, and Perception

**What the metadata suggests:** The work links video generation with motion attribution and is classified as a benchmark or evaluation contribution. It is an oral paper and received an Outstanding Paper Honorable Mention.

**Why it matters:** The paper offers a route into the shift from static recognition toward motion, time, and causal structure in video.

**What to inspect in the full paper:** How motion causes are defined, whether the benchmark separates appearance from motion, which baselines are used, and what the evaluation misses.

**Paper page:** [ICML virtual poster](https://icml.cc/virtual/2026/poster/60542)

**Checkpoint:** What would count as evidence that a model understands why an object moves rather than only predicting the next frame?

## Lesson 10: Which Algorithms Can Graph Neural Networks Learn?

**Evidence level for this lesson:** Metadata and briefing-card spotlight.

**Area:** Graphs, Geometry, and Representation Learning

**What the metadata suggests:** The paper studies graph neural networks through a theory or proof contribution and uses theoretical or synthetic evaluation settings.

**Why it matters:** It connects structural representation learning with a fundamental question: which procedures can a learned graph model represent and execute?

**What to inspect in the full paper:** First, check how the paper defines “learn” and which algorithms it considers. Then check its assumptions about graph size and whether the result extends to larger or different graphs.

**Paper page:** [ICML virtual poster](https://icml.cc/virtual/2026/poster/65099)

**Checkpoint:** Why is fitting examples from an algorithm different from learning the algorithm itself?

## Lesson 11: RoboMME

**Full title:** RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies

**Evidence level for this lesson:** Metadata and briefing-card spotlight.

**Area:** Robotics, Embodiment, and World Models

**What the metadata suggests:** The paper centers on memory and benchmarking for robotic generalist policies. It is an oral paper and has strong public attention relative to many papers.

**Why it matters:** A robot must connect observations and actions across time. Memory can be the difference between reacting to the current frame and completing a long task.

**What to inspect in the full paper:** Check the kinds of memory, task length, real versus simulated settings, and failure cases. Also check whether the visible GitHub link belongs to this paper and supports its results. The collected repository metadata appears mismatched and needs manual review.

**Paper page:** [ICML virtual poster](https://icml.cc/virtual/2026/poster/65933)

**Checkpoint:** Design one task where a robot can succeed without memory and one where memory is essential.

## Lesson 12: Protein Autoregressive Modeling via Multiscale Structure Generation

**Evidence level for this lesson:** Metadata and briefing-card spotlight.

**Area:** AI for Science, Health, and Neuro

**What the metadata suggests:** The paper brings autoregressive and multiscale generation ideas to protein structure. It is an oral paper in the scientific ML area.

**Why it matters:** Scientific systems have structure at several scales. A useful model may need to connect local molecular detail with larger shapes and biological constraints.

**What to inspect in the full paper:** Check what the model generates at each scale and how the paper measures physical validity. Check the protein data, the novelty test, and whether the visible GitHub metadata matches the paper. The collected repository metadata appears mismatched and needs manual review.

**Paper page:** [ICML virtual poster](https://icml.cc/virtual/2026/poster/66808)

**Checkpoint:** Why can a visually plausible generated protein still be scientifically invalid?

## Final Paper-Course Activity

Choose any two papers and complete this comparison:

| Question | Paper A | Paper B |
| --- | --- | --- |
| Main problem | | |
| Contribution | | |
| Evidence | | |
| Main limit | | |
| Conference trend | | |
| Confidence in classification | | |

Then answer:

1. Which paper makes the narrower claim?
2. Which paper uses stronger evidence for the claim it makes?
3. What extra evidence would most change your view?

There is no single correct paper choice. A strong answer matches the evidence to the claim and states uncertainty clearly.
