# A Friendly Roadmap to ICML 2026

Welcome. This course is for people who want to understand the shape of ICML 2026 without reading thousands of papers.

If you prefer a visual introduction, open the [self-contained HTML slide deck](icml2026_newcomer_slides.html). It works offline and includes embedded figures and short knowledge checks.

You do not need to know every method or remember every number. Your goal is to build a useful mental map. By the end, you should know what the main research areas are, which trends stand out, how the evidence was collected, and where the evidence is still weak.

## Your Finish Line

You are ready to explore ICML 2026 on your own when you can:

- describe the 12 broad research areas in everyday language;
- explain six major patterns in the conference;
- tell the difference between paper volume, program selection, public attention, historical comparison, and visible artifacts;
- connect a small set of papers to the wider landscape;
- point out uncertainty instead of hiding it;
- give a balanced five-minute briefing about the conference.

This is what this course means by understanding about 80% of the landscape. It means knowing most of the map and knowing how to explore what remains. It does not mean mastering the technical details of 80% of the papers.

## Before You Begin

You should know the basic meaning of a model, training, a dataset, and evaluation. Everything else is explained as it appears. If a word is unfamiliar, use the [plain-language glossary](newcomer_glossary.md).

The current workspace contains 6,628 papers. It groups them into 12 broad areas. These groups are useful for navigation, but they are not final truth. Half of the finer semantic clusters are still marked for human review. Treat exact paper counts as strong descriptive evidence and the wider trend explanations as informed, cautious interpretations.

## Choose Your Route

### Quick Tour: 3 to 4 Hours

Choose this route if you need a useful overview today.

1. Read Lesson 1 below.
2. Read the short version of the [12-area tour](../reports/icml2026_newcomer_area_tour.md#the-map-at-a-glance).
3. Complete Trend Lessons 1, 3, 4, and 6 in the [trend guide](../reports/icml2026_newcomer_trend_lessons.md).
4. Read Paper Lessons 2, 6, 7, and 11 in the [paper course](../reports/icml2026_newcomer_paper_course.md).
5. Take the checkpoint quiz at the end of each lesson.
6. Write the five-minute briefing in Lesson 7.

### Standard Route: 10 to 12 Hours

Choose this route if you want broad understanding and a reliable self-check.

1. Complete Lessons 1 through 7 in order.
2. Read all 12 area cards.
3. Complete all six trend lessons.
4. Study the 12-paper core course.
5. Complete the short checkpoint after every stage.
6. Take the [final quiz](../reports/icml2026_newcomer_final_quiz.md).
7. Use the answer key only after completing your first attempt.
8. If you score below 80, follow the review route suggested by your score.

### Deep Route: About 20 Hours

Choose this route if you plan to write, teach, or make research decisions from this material.

Complete the standard route, then:

- read the linked area briefing cards;
- open the source paper or PDF cards for every core paper;
- inspect at least one paper from each of the 12 areas;
- complete one artifact check;
- compare one ICML area with the historical venue baseline;
- write a one-page final briefing with evidence and caveats.

## How Every Lesson Works

Each lesson uses the same five moves:

> Learn the idea → see an example → compare the evidence → answer a check question → explain it in your own words.

Do not skip the final explanation. Saying an idea in your own words is one of the best ways to notice what you do not yet understand.

## Confidence Labels

You will see three labels throughout the course.

- **Checked fact:** Directly supported by official conference data or a simple generated count.
- **Directional pattern:** Supported by several signals, but still needs paper-level review before strong publication language.
- **Open question:** A useful possibility that the current evidence cannot settle.

These labels are part of the lesson, not a warning to ignore. Good research understanding includes knowing how certain a statement is.

## Lesson 1: Learn How the Map Was Built

**Time:** 35 minutes

**Goal:** Understand what the project counted and why the map is useful but imperfect.

The project begins with the official ICML 2026 virtual conference list. That gives 6,628 paper records. The records are joined with public attention and visible GitHub information from AlphaXiv. Titles, topics, abstracts, and semantic groups are then organized into 12 broad areas.

The project also compares several different signals:

- **Paper share:** How much of ICML falls into an area.
- **Program signal:** Whether an area appears more often among oral or award selections.
- **Public attention:** AlphaXiv votes and visits. This measures attention on that platform, not research quality.
- **Historical comparison:** How ICML 2026 area shares compare with nearby accepted-paper collections.
- **Artifact visibility:** Whether a GitHub link is visible in the collected metadata. This does not show that the code works.

No single signal answers “What is the best research?” Each signal answers a narrower question.

### Example

Robotics and world models make up only 2.9% of the mapped papers, but their public-attention enrichment is 2.11 times the conference baseline. This supports the statement that robotics receives unusually high AlphaXiv attention for its size. It does not show that robotics papers are twice as good as other papers.

### Checkpoint 1

Answer without looking back:

1. Why is the 12-area taxonomy useful?
2. Why is it not final truth?
3. What does public attention measure?
4. What does a visible GitHub link fail to prove?

**Ready to continue:** You can explain the difference between a navigation map and a final scientific judgment.

## Lesson 2: Tour the Conference

**Time:** 90 minutes

**Goal:** Build a simple mental map of all 12 research areas.

Open the [12-area tour](../reports/icml2026_newcomer_area_tour.md). First read “The Map at a Glance.” Then read each card.

Do not memorize the counts. For each area, write down only:

- the problem the area tries to solve;
- one question researchers are asking;
- one connection to another area;
- one warning about interpretation.

### Checkpoint 2

Choose four of the 12 areas. Explain each one in a single sentence without using the area’s exact title. Then explain one connection between two of your chosen areas.

**Ready to continue:** You can recognize all 12 areas and explain at least eight without help.

## Lesson 3: Learn the Main Conference Story

**Time:** 90 minutes

**Goal:** Understand the six patterns that organize the course.

Open the [six trend lessons](../reports/icml2026_newcomer_trend_lessons.md). For every trend, fill this small table in your notes:

| Question | Your answer |
| --- | --- |
| What is the pattern? | |
| Which evidence supports it? | |
| What could make it misleading? | |
| Which paper makes it concrete? | |

### Checkpoint 3

Pick three trends. Explain each using one number, one paper example, and one caveat.

**Ready to continue:** You can explain why the conference story is more than a ranking of area sizes.

## Lesson 4: Learn to Read Signals Carefully

**Time:** 60 minutes

**Goal:** Decide what a piece of evidence can and cannot support.

For each statement below, decide whether it is supported.

1. “Theory has lower public attention than average, so theory was not important at ICML.”
2. “Robotics has high public attention for its size on AlphaXiv.”
3. “A paper with a GitHub link can be reproduced.”
4. “Multimodal and vision is one of the largest areas inside ICML 2026.”
5. “Because an area has high oral enrichment, every paper in that area is high quality.”

Suggested answers:

1. Not supported. Theory has high program enrichment, and public attention is only one signal.
2. Supported, as long as AlphaXiv is named.
3. Not supported. The repository still needs inspection and testing.
4. Supported by the mapped paper count.
5. Not supported. Area-level enrichment says nothing certain about every paper.

### Checkpoint 4

Write one careful sentence about public attention, one about program selection, and one about artifacts. Include the limit of each signal in the same sentence.

**Ready to continue:** You can correct a claim that uses the right number but draws the wrong conclusion.

## Lesson 5: Connect the Map to Papers

**Time:** 3 to 4 hours

**Goal:** See how conference-level patterns appear—and sometimes break down—in real papers.

Work through the [12-paper core course](../reports/icml2026_newcomer_paper_course.md). The first eight lessons use locally inspected PDF pages. Four wider-view lessons use the project’s paper metadata and briefing cards and are clearly marked as needing a full paper read.

For each paper, complete a paper card:

| Prompt | Your notes |
| --- | --- |
| What problem is being solved? | |
| What is the main contribution? | |
| What evidence is used? | |
| What is one limit? | |
| Which area or trend does it connect to? | |
| Is the classification clear or uncertain? | |

### Checkpoint 5

Compare two papers from different areas. Explain how they use different evidence to make different kinds of claims.

**Ready to continue:** You can describe a paper without repeating only its title or abstract.

## Lesson 6: Find Tensions and Disagreements

**Time:** 60 minutes

**Goal:** Understand that research trends contain competing goals and open questions.

Choose one pair:

- better reasoning scores versus reliable reasoning;
- larger capability versus lower computing cost;
- useful agents versus safe tool access;
- exciting demos versus careful evaluation;
- broad benchmarks versus realistic use;
- visible code versus tested reproduction.

Write two short paragraphs. The first should explain one side. The second should explain the other. Use at least two sources from the course.

### Checkpoint 6

Finish this sentence: “The evidence does not simply say ___; it shows a tension between ___ and ___.”

**Ready to continue:** You can describe a disagreement fairly before stating your own view.

## Lesson 7: Build Your Own ICML 2026 Briefing

**Time:** 45 minutes

**Goal:** Turn the course into a clear explanation you could give to someone else.

Use the [briefing template](../reports/icml2026_newcomer_briefing_template.md). Your five-minute briefing should include:

1. one sentence describing the conference map;
2. three major trends;
3. one contrast between signals;
4. two important caveats;
5. three papers worth reading next.

Then take the [final quiz](../reports/icml2026_newcomer_final_quiz.md). The quiz is open-book. Using sources well is part of the skill being tested.

## What to Do After the Quiz

- **90–100:** Teach the map to someone else or begin the deep route.
- **80–89:** Choose one area for deeper reading.
- **65–79:** Use the score report to repeat the weak lessons, then try again.
- **Below 65:** Repeat Lessons 1 through 4 before returning to the paper course.

The goal is not to protect your first score. The goal is to leave with a reliable way to understand new research.

## Source and Safety Notes

The course is built from the local ICML 2026 workspace. Exact corpus counts and official program labels are the strongest evidence. Area assignments, historical comparisons, AlphaXiv signals, and visible artifact links are useful but need careful interpretation. The project’s 310 manual claim and area review rows are still unfilled, so the tutorial avoids presenting directional patterns as final publication claims.

For the full wording rules, read the [safe statement register](../reports/icml2026_safe_statement_register.md).
