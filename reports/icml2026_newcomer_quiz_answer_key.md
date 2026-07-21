# ICML 2026 Newcomer Quiz: Answer Key and Review Guide

Use this guide after completing the quiz. Your words do not need to match these model answers. Award points when the answer shows the same understanding.

## How to Score

- Total: 100 points
- Pass: at least 80 overall
- Minimum section score: half of the points in every part
- Serious interpretation errors must be corrected before passing

For open answers, give full credit when the learner makes a supported claim, states an important limit, and explains the reasoning clearly.

## Part A Answers — 15 Points

### A1. Taxonomy — 3 Points

A taxonomy is a named system for organizing papers into areas. The 12-area map makes a very large conference easier to explore. It is not final truth because some papers cross boundaries, automated grouping can make mistakes, and many finer clusters still need manual review.

- 1 point: explains organization or grouping;
- 1 point: explains navigation value;
- 1 point: names a real limit.

### A2. Enrichment — 3 Points

Oral enrichment of 1.4 means papers from the area appear among oral selections about 1.4 times as often as expected from the area’s overall paper share. It does not mean that every paper is 40% better, or that oral selection is a complete quality measure.

### A3. Public Attention — 3 Points

It measures votes or visits on AlphaXiv. It may differ from scientific importance because visually striking demos, familiar topics, famous authors, strong project pages, or platform users’ interests can change attention.

Full credit requires naming AlphaXiv and at least two plausible differences.

### A4. Historical Baseline — 3 Points

A historical or venue baseline shows whether an area is unusually emphasized at ICML rather than simply large across machine learning. Limits include different venue scopes, uneven abstract coverage, and classification errors across collections.

### A5. Artifact Visibility — 3 Points

A visible link shows that the metadata points to a repository or other artifact. Reproducibility requires checking that the artifact belongs to the paper, contains the needed materials, can be installed or run, and can recreate relevant results under documented conditions.

## Part B Answers — 20 Points

### B1. — 2 Points

LLM Reasoning, Post-Training, and RLVR.

### B2. — 2 Points

Robotics, Embodiment, and World Models. Multimodal, Vision, and Perception is a reasonable neighboring area.

### B3. — 2 Points

Data-Centric, Causal, and Federated ML.

### B4. — 2 Points

LLM Reasoning, Post-Training, and RLVR plus Reinforcement Learning and Control. Safety or Agents may also be involved, but the first two are the most direct answer.

### B5. — 2 Points

Scientific and medical claims may require physical validity, uncertainty, realistic data conditions, biological function, clinical relevance, or laboratory testing. A general benchmark score may measure only a proxy.

### B6. — 2 Points

Systems work usually focuses on practical computing behavior such as speed, memory, hardware, serving, and end-to-end cost. Theory and optimization often focus on mathematical properties, guarantees, assumptions, or general algorithms. Strong answers may note that some papers sit between them.

### B7. — 2 Points

Reinforcement learning also includes control, exploration, offline learning, online decision-making, robustness, and general policy learning. LLM post-training is only one application and often has special reward and sampling settings.

### B8. — 2 Points

Safety, Governance, Privacy, and Society. It may overlap with LLM Reasoning and Post-Training because the deception can emerge during RL training, or with Agents when tool use is involved.

### B9. — 2 Points

Graphs, Geometry, and Representation Learning. AI for Science is a likely application neighbor for molecules.

### B10. — 2 Points

Several answers work. Examples:

- *Neural Thickets*: systems, optimization, or post-training;
- *Maximum Likelihood Reinforcement Learning*: general RL, optimization, or LLM post-training;
- *How much can language models memorize?*: broad LLM study versus the narrower reasoning label.

Full credit requires a real reason for the boundary, not only two area names.

## Part C Answers — 25 Points

Each answer receives:

- 2 points for what is supported;
- 2 points for rejecting the overclaim or naming the limit;
- 1 point for a useful next check.

### C1. Robotics Attention — 5 Points

**Supported:** Robotics is small by paper share and receives unusually high AlphaXiv attention for its size.

**Not supported:** The numbers do not prove it is the most important, highest-quality, or most influential area.

**Next check:** Inspect high-attention papers to see whether attention comes from technical advances, benchmarks, demos, models, or project-page visibility. Compare with program selection and citations later.

### C2. Theory Signals — 5 Points

**Supported:** Theory receives below-average AlphaXiv attention and above-average oral representation in this snapshot.

**Not supported:** Low platform attention does not show that theory did not matter. The oral signal points in the opposite direction.

**Next check:** Read low-public, high-program theory papers and identify the technical contribution that may explain selection.

### C3. Multimodal Baseline — 5 Points

The area is large because 889 ICML papers fall into it. It is underweight because its share of ICML is lower than its share in the nearby conference baseline. “Large” describes its size inside ICML. “Underweight” describes a comparison with other venues.

A strong answer also notes that the comparison depends on venue scope and consistent classification.

### C4. Repository Link — 5 Points

**Supported:** A popular repository link is visible in the collected metadata.

**Not supported:** Stars and a URL do not establish that the repository matches the paper, contains all materials, runs, or reproduces results. They also do not show that independent people reproduced the work.

**Next check:** Confirm repository identity, inspect instructions and licenses, run the code in a clean environment, and compare reproduced outputs with the paper.

### C5. The Largest Area — 5 Points

**Safe headline example:** “LLM reasoning and post-training form the largest area in the project’s current ICML 2026 taxonomy, though several subarea boundaries still need review.”

**Unsafe headline example:** “ICML 2026 proves that reasoning is the most important and dominant future of machine learning.”

The safe version names the taxonomy and limit. The unsafe version changes a mapped count into a claim about importance and the future.

## Part D Answers — 20 Points

### D1. Tool-Using Coding Agent — 10 Points

1. **Area:** Agents, Code, and Tool Use. Systems may also matter because tools, memory, and execution infrastructure affect performance.
2. **Contribution:** Most likely a better system or scaffold. The base model is unchanged, while planning, memory, and tools were added.
3. **Supported:** The full configured system performs better than the stated comparison on one benchmark under the reported setup.
4. **Limits:** We do not know which component caused the gain, whether the result generalizes, whether costs are matched, whether failures are safe, or whether the artifact can be inspected.
5. **Trend:** Agents are moving toward tool environments and evaluation systems, but scaffolding must be separated from learned capability. Artifact visibility is also incomplete.

Award 2 points for each numbered element when the reasoning is clear.

### D2. Protein Design Model — 10 Points

1. **Area:** AI for Science, Health, and Neuro, overlapping with Generative Modeling.
2. **Contribution:** A multistage or multiscale generative method for protein structures.
3. **Supported:** It improves the reported structure-validity measures over three selected baselines on the public benchmark.
4. **Not established:** Laboratory function, biological usefulness, novelty beyond training data, safe design, or generalization to new protein families.
5. **Checks:** Examine training and test overlap; perform laboratory or high-quality simulation validation; compare with stronger or more recent baselines; test novelty and diversity; report uncertainty and failures.

Give full credit for any two strong additional checks.

## Part E Scoring Rubric — 20 Points

### Conference Map — 3 Points

- 3: Gives a clear one-sentence map and explains that areas are broad.
- 2: Gives a useful map but misses uncertainty.
- 1: Lists topics without an organizing idea.
- 0: Misstates the corpus or map.

### Three Trends — 5 Points

- 5: Explains three trends with accurate support and clear meaning.
- 3–4: Trends are mostly right but unevenly explained.
- 1–2: Mostly lists area sizes.
- 0: Major claims are unsupported.

### Numerical Evidence — 3 Points

- 3: Uses at least three relevant numbers and names the signal type.
- 2: Uses three numbers but leaves one source unclear.
- 1: Uses one or two useful numbers.
- 0: Uses no evidence or seriously misreads it.

### Program and Public Contrast — 2 Points

- 2: Clearly explains that the signals answer different questions.
- 1: Names the contrast but gives little interpretation.
- 0: Treats either signal as a complete quality score.

### Paper Examples — 2 Points

- 2: Uses at least two papers to make specific ideas concrete.
- 1: Names papers without explaining their relevance.
- 0: No paper examples.

### Caveats and Open Question — 3 Points

- 3: Includes at least two material caveats and one useful open question.
- 2: Includes caveats but they are generic.
- 1: Gives only one limit.
- 0: Presents the story as settled.

### Clarity — 2 Points

- 2: Friendly, direct, and understandable to a newcomer.
- 1: Mostly clear but uses unexplained terms or crowded sentences.
- 0: Difficult to follow.

## Result Levels

- **90–100: Ready to teach the map.** You can explain the landscape, use evidence carefully, and guide another learner.
- **80–89: Strong broad understanding.** You can explore independently and should choose an area for deeper study.
- **65–79: The map is forming.** Review the weak skill groups below, then try the relevant questions again.
- **Below 65: Rebuild the foundation.** Repeat Lessons 1 through 4 before returning to the paper course.

## Review Paths by Mistake Type

### If Terms Were Difficult

Review:

- [Plain-language glossary](../docs/newcomer_glossary.md)
- Roadmap Lesson 1

Retry A1 through A5.

### If the 12 Areas Blurred Together

Review:

- [12-area tour](icml2026_newcomer_area_tour.md)

Make one sentence and one example for every area. Retry B1 through B10.

### If You Misread Evidence

Review:

- Roadmap Lesson 4
- [Six trend lessons](icml2026_newcomer_trend_lessons.md)
- [Safe statement register](icml2026_safe_statement_register.md)

Retry C1 through C5. For each answer, explicitly write “supports” and “does not support.”

### If New Papers Were Hard to Place

Review:

- [12-paper course](icml2026_newcomer_paper_course.md)

Complete the six-field paper card for Lessons 4, 5, 9, and 12. Then retry Part D.

### If the Final Briefing Was Weak

Review:

- [Briefing template](icml2026_newcomer_briefing_template.md)
- Trend lesson recap

Use the structure “pattern → evidence → limit → example” for each paragraph.

## Final Mastery Check

Passing the quiz shows broad working understanding, not expert knowledge. A learner who passes should be able to explore new papers with good questions, explain the main landscape without exaggeration, and identify where more evidence is needed.

