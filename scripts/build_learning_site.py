#!/usr/bin/env python3
"""Generate the public foundations, area lessons, and synthesis course."""

from __future__ import annotations

import csv
import html
import json
import re
from pathlib import Path

from build_newcomer_slides import AREA_TECHNICAL
from learning_content import AREA_LESSONS, COMPARISON_PAPERS, FOUNDATION_QUIZ, PAPER_CASES, SYNTHESIS_QUIZ


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LESSON_DIR = DOCS / "learn"
BRIEFINGS = ROOT / "data" / "processed" / "icml2026_area_briefing_cards.csv"
EXPLORER = ROOT / "data" / "processed" / "icml2026_paper_explorer.csv"


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def page_shell(title: str, body: str, *, depth: int = 1, description: str = "") -> str:
    prefix = "../" * depth
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description or title)}">
  <meta name="theme-color" content="#1f5f8b">
  <title>{esc(title)} · ICML 2026 Landscape</title>
  <link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
  <link rel="manifest" href="{prefix}site.webmanifest">
  <link rel="stylesheet" href="{prefix}assets/site.css">
</head>
<body class="course-page">
  <a class="skip-link" href="#main">Skip to lesson</a>
  <header class="site-header"><div class="nav-wrap"><a class="brand" href="{prefix}index.html"><span class="brand-mark">26</span> ICML Landscape</a><button class="nav-toggle" aria-expanded="false" aria-label="Open navigation">Menu</button><nav class="site-nav" aria-label="Main navigation"><a href="{prefix}index.html">Home</a><a href="{prefix}learn.html" aria-current="page">Learn</a><a href="{prefix}icml2026_newcomer_slides.html">Slides</a><a href="{prefix}quiz.html">Quiz</a><a href="{prefix}dashboard.html">Explore</a><a href="{prefix}about.html">About</a></nav></div></header>
{body}
  <footer class="site-footer"><div class="footer-wrap"><div><strong>ICML 2026 Landscape</strong><p class="muted">Learn the idea, inspect the evidence, test your understanding.</p></div><div class="footer-links"><a href="{prefix}learn.html">Course map</a><a href="{prefix}quiz.html">Final quiz</a><a href="https://github.com/juyoungml/icml2026">GitHub</a></div></div></footer>
  <script src="{prefix}assets/site.js"></script>
  <script src="{prefix}assets/lesson.js"></script>
</body>
</html>
'''


def quiz_markup(module: str, questions: list[dict[str, object]]) -> str:
    encoded = esc(json.dumps(questions, ensure_ascii=False))
    return f'''
<section class="lesson-section mastery" id="checkpoint" data-lesson-quiz data-module="{esc(module)}" data-questions="{encoded}">
  <p class="eyebrow">Mastery checkpoint</p>
  <h2>Prove the map is usable</h2>
  <p>Answer four questions. A score of 3/4 marks this lesson complete. Explanations appear immediately.</p>
  <div class="lesson-quiz" data-quiz-stage></div>
</section>'''


def lesson_navigation(current: int | str) -> str:
    links = [('foundations', '00', 'Foundations')]
    links.extend((slugify(area['area']), f"{area['number']:02}", area['area']) for area in AREA_TECHNICAL)
    links.append(('synthesis', '13', 'Synthesis'))
    items = []
    for slug, number, label in links:
        is_current = current == slug or current == int(number) if number.isdigit() else current == slug
        current_attr = ' aria-current="page"' if is_current else ''
        items.append(f'<a href="{slug}.html"{current_attr}><span>{number}</span>{esc(label)}<i data-module-state="{slug}" aria-label="Not yet mastered"></i></a>')
    return '<nav class="course-nav" aria-label="Course lessons"><h2>Course</h2>' + ''.join(items) + '</nav>'


def mobile_lesson_navigation(current: int | str) -> str:
    links = [("foundations", "00", "Foundations")]
    links.extend((slugify(area["area"]), f"{area['number']:02}", area["area"]) for area in AREA_TECHNICAL)
    links.append(("synthesis", "13", "Synthesis"))
    items = []
    for slug, number, label in links:
        current_marker = " · current" if current == slug or (number.isdigit() and current == int(number)) else ""
        items.append(f'<a href="{slug}.html"><span>{number}</span>{esc(label)}{current_marker}</a>')
    return '<details class="mobile-course-nav"><summary>Jump to another module</summary><nav aria-label="Mobile course lessons">' + "".join(items) + "</nav></details>"


def learning_index() -> str:
    cards = []
    for area in AREA_TECHNICAL:
        slug = slugify(area["area"])
        cards.append(f'''
        <a class="curriculum-card" href="learn/{slug}.html" data-course-card="{slug}">
          <span class="module-number">{area['number']:02}</span>
          <div><p class="module-meta">{area['count']} papers · {area['share']} · 10–12 min</p><h3>{esc(area['area'])}</h3><p>{esc(AREA_LESSONS[area['number']]['hook'])}</p></div>
          <span class="module-status" data-module-label="{slug}">Start</span>
        </a>''')
    body = f'''
  <main id="main">
    <section class="course-hero">
      <div><p class="eyebrow">The ICML field guide</p><h1>Build a technical map you can actually use.</h1><p class="lead">Learn shared foundations, work through 12 research areas, inspect real paper cases, and earn completion through short mastery checks.</p><div class="actions"><a class="button" href="learn/foundations.html" data-course-resume>Begin with foundations</a><a class="button secondary" href="#routes">Choose a route</a></div></div>
      <div class="course-progress-card"><span class="tag">Your progress</span><strong data-course-progress-number>0%</strong><div class="progress-shell" role="progressbar" aria-label="Course mastery" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"><span data-course-progress></span></div><p data-course-progress-label>0 of 14 modules mastered</p><small>Stored only in this browser</small><button class="text-button" type="button" data-reset-course>Reset course progress</button></div>
    </section>
    <section class="section compact" id="routes"><div class="section-head"><div><p class="eyebrow">Choose your depth</p><h2>Three honest learning routes</h2></div><p>You do not need to read every detail on your first visit.</p></div><div class="grid three route-grid">
      <div class="card tint-green"><span class="tag">45 minutes</span><h3>Orientation</h3><p>Foundations, the area summaries, synthesis, and the quick final quiz.</p><ol><li>Read foundations</li><li>Scan the 12 mental models</li><li>Study synthesis</li><li>Take quick quiz</li></ol></div>
      <div class="card tint-blue"><span class="tag">About 3 hours</span><h3>Core course</h3><p>Complete every worked example and area checkpoint.</p><ol><li>Foundations</li><li>All 12 area lessons</li><li>Synthesis</li><li>Full assessment</li></ol></div>
      <div class="card tint-purple"><span class="tag">8–12 hours</span><h3>Deep reading</h3><p>Open the three paper cases in every module and complete the reading prompts.</p><ol><li>Core course</li><li>36 paper cases</li><li>Compare methods</li><li>Write a field briefing</li></ol></div>
    </div></section>
    <section class="section compact"><div class="section-head"><div><p class="eyebrow">Stage 1</p><h2>Learn how to read the evidence</h2></div></div><a class="curriculum-card featured" href="learn/foundations.html" data-course-card="foundations"><span class="module-number">00</span><div><p class="module-meta">Required · 15 min</p><h3>Foundations: models, metrics, and claims</h3><p>Understand training versus inference, benchmarks, baselines, ablations, enrichment, and evidence limits before interpreting the field map.</p></div><span class="module-status" data-module-label="foundations">Start</span></a></section>
    <section class="section compact"><div class="section-head"><div><p class="eyebrow">Stage 2</p><h2>Learn the 12 research areas</h2></div><p>Every module includes an intuition, technical pipeline, worked example, three paper cases, limitations, and a mastery check.</p></div><div class="curriculum-list">{''.join(cards)}</div></section>
    <section class="section compact"><div class="section-head"><div><p class="eyebrow">Stage 3</p><h2>Connect the map</h2></div></div><a class="curriculum-card featured" href="learn/synthesis.html" data-course-card="synthesis"><span class="module-number">13</span><div><p class="module-meta">Required · 15 min</p><h3>Cross-area synthesis</h3><p>Compare program selection, public attention, venue baselines, systems, agents, multimodality, robotics, and artifact evidence without confusing their signals.</p></div><span class="module-status" data-module-label="synthesis">Start</span></a></section>
  </main>'''
    return page_shell("Learn", body, depth=0, description="A guided technical course through 12 ICML 2026 research areas, paper cases, and evidence-aware mastery checks.")


def foundations_page() -> str:
    body = f'''
  <main id="main" class="course-layout">
    <aside>{lesson_navigation('foundations')}</aside>
    <article class="lesson-content">
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="../learn.html">Course</a><span>/</span>Foundations</nav>{mobile_lesson_navigation('foundations')}
      <header class="lesson-hero"><p class="eyebrow">Module 00 · Required · 15 minutes</p><h1>Read models, metrics, and claims without getting fooled.</h1><p class="lead">This foundation turns conference numbers and paper results into careful conclusions. It is the prerequisite for every area lesson.</p><div class="lesson-goals"><strong>After this lesson, you can:</strong><ul><li>separate training, inference, and evaluation;</li><li>interpret baselines, ablations, and enrichment;</li><li>match the strength of a claim to its evidence.</li></ul></div></header>
      <section class="lesson-section"><p class="eyebrow">Mental model 1</p><h2>Training changes the model. Inference uses it.</h2><div class="concept-flow"><div><span>1</span><strong>Data</strong><p>Examples, demonstrations, preferences, or interactions.</p></div><b>→</b><div><span>2</span><strong>Training</strong><p>Update parameters to improve an objective.</p></div><b>→</b><div><span>3</span><strong>Inference</strong><p>Use fixed parameters to predict, generate, search, or act.</p></div><b>→</b><div><span>4</span><strong>Evaluation</strong><p>Measure behavior on defined tasks and conditions.</p></div></div><div class="callout"><strong>Common mistake</strong><p>More inference-time search can improve an answer without changing what the model learned during training.</p></div></section>
      <section class="lesson-section"><p class="eyebrow">Mental model 2</p><h2>A metric answers one question—not every question.</h2><div class="signal-table" role="table" aria-label="Evidence signals"><div role="row"><strong role="columnheader">Signal</strong><strong role="columnheader">Supports</strong><strong role="columnheader">Does not prove</strong></div><div role="row"><span>Paper share</span><span>How large an area is in this taxonomy</span><span>Importance or quality</span></div><div role="row"><span>Oral enrichment</span><span>Relative program representation</span><span>That every oral is better</span></div><div role="row"><span>Public attention</span><span>Visibility on AlphaXiv</span><span>Correctness or impact</span></div><div role="row"><span>Repository link</span><span>A possible artifact to inspect</span><span>Reproduction</span></div></div></section>
      <section class="lesson-section"><p class="eyebrow">Worked example</p><h2>Compute enrichment without turning it into a ranking.</h2><div class="worked-example"><div class="worked-question"><span>Given</span><p>An area contains <strong>10%</strong> of all papers and <strong>15%</strong> of oral papers.</p></div><div class="equation"><small>oral enrichment</small><strong>15% ÷ 10% = 1.5×</strong></div><ol><li><strong>Supported:</strong> the area appears among orals 1.5 times as often as its paper share suggests.</li><li><strong>Not supported:</strong> every paper in the area is 50% better.</li><li><strong>Next check:</strong> inspect counts, uncertainty, and which papers drive the contrast.</li></ol></div></section>
      <section class="lesson-section"><p class="eyebrow">Mental model 3</p><h2>Baselines and ablations answer different questions.</h2><div class="compare-grid"><div><h3>Baseline</h3><p>A credible existing method or simple reference.</p><strong>Question:</strong><p>Is the proposed system better than what we should reasonably compare against?</p></div><div><h3>Ablation</h3><p>The proposed system with a component removed or changed.</p><strong>Question:</strong><p>Which part of the system appears to cause the improvement?</p></div></div></section>
      <section class="lesson-section"><p class="eyebrow">A five-pass paper reading method</p><h2>Read for decisions, not for total recall.</h2><ol class="reading-protocol"><li><span>Problem</span><div><strong>What is difficult, and for whom?</strong><p>Rewrite the problem in one plain sentence.</p></div></li><li><span>Method</span><div><strong>What changed?</strong><p>Identify the new objective, architecture, data, or system component.</p></div></li><li><span>Evidence</span><div><strong>What was measured?</strong><p>List tasks, baselines, metrics, ablations, and resource conditions.</p></div></li><li><span>Result</span><div><strong>What improved, exactly?</strong><p>Keep the result tied to its measured setting.</p></div></li><li><span>Limit</span><div><strong>Where might the conclusion fail?</strong><p>Check assumptions, distribution shift, cost, safety, and missing comparisons.</p></div></li></ol></section>
      <section class="lesson-section"><p class="eyebrow">Claim ladder</p><h2>Use language that matches evidence strength.</h2><div class="claim-ladder"><div><span>Strongest</span><strong>Checked fact</strong><p>“The official corpus contains 6,628 paper records.”</p></div><div><span>Useful</span><strong>Directional pattern</strong><p>“Several signals suggest systems and agents are becoming more central.”</p></div><div><span>Needs work</span><strong>Open hypothesis</strong><p>“Public attention may be influenced by demos and visible artifacts.”</p></div><div><span>Avoid</span><strong>Unsupported universal</strong><p>“Robotics is the most important area.”</p></div></div></section>
      {quiz_markup('foundations', FOUNDATION_QUIZ)}
      <nav class="lesson-next"><span>Next module</span><a href="{slugify(AREA_TECHNICAL[0]['area'])}.html">01 · {esc(AREA_TECHNICAL[0]['area'])} →</a></nav>
    </article>
  </main>'''
    return page_shell("Foundations", body, description="Learn the evidence and paper-reading foundations needed to interpret the ICML 2026 landscape.")


def paper_reading_cards(area: dict[str, object], explorer: dict[str, dict[str, str]]) -> str:
    selections = COMPARISON_PAPERS[int(area["number"])]
    extra = []
    for index, selection in enumerate(selections, start=2):
        title = selection["title"]
        role = selection["role"]
        row = explorer.get(title, {})
        case = PAPER_CASES.get(title)
        if case is None:
            raise KeyError(f"Missing comparison-paper teaching case: {title}")
        methods = row.get("method_families", "Method details require paper inspection")
        evaluation = row.get("evaluation_settings", "Evaluation details require paper inspection")
        extra.append(f'''<article class="paper-card compact-paper"><div class="paper-top"><span class="paper-index">Paper {index} · Abstract-based preview</span><span class="tag">Comparison case</span></div><h3>{esc(title)}</h3><p class="selection-reason"><strong>Why selected:</strong> {esc(role)} broadens the core case and shows another important part of this area.</p><dl><div><dt>Problem</dt><dd>{esc(case['problem'])}</dd></div><div><dt>Approach</dt><dd>{esc(case['approach'])}</dd></div><div><dt>Evidence</dt><dd>{esc(case['evidence'])}</dd></div><div><dt>Takeaway</dt><dd>{esc(case['takeaway'])}</dd></div><div><dt>Caution</dt><dd>{esc(case['caution'])}</dd></div><div><dt>Metadata cues</dt><dd>{esc(methods)} · {esc(evaluation)}</dd></div></dl><p><strong>Reading prompt:</strong> Compare this paper’s evidence and limitation with the core case. Does it strengthen the area story or expose a boundary?</p><a href="{esc(row.get('url', '#'))}">Open ICML paper page ↗</a></article>''')
    primary = f'''<article class="paper-card primary-paper"><div class="paper-top"><span class="paper-index">Paper 1 · Core case</span><span class="tag">{esc(area['badge'])}</span></div><h3>{esc(area['paper'])}</h3><dl><div><dt>Problem</dt><dd>{esc(area['problem'])}</dd></div><div><dt>Method</dt><dd>{esc(area['method'])}</dd></div><div><dt>Evidence</dt><dd>{esc(area['evidence'])}</dd></div><div><dt>Main result</dt><dd>{esc(area['result'])}</dd></div><div><dt>Important limit</dt><dd>{esc(area['limit'])}</dd></div></dl><a class="button secondary" href="{esc(area['paper_url'])}">Open ICML paper page ↗</a></article>'''
    return primary + ''.join(extra)


def area_page(area: dict[str, object], detail: dict[str, object], brief: dict[str, str], explorer: dict[str, dict[str, str]]) -> str:
    number = int(area["number"])
    slug = slugify(str(area["area"]))
    prev_slug = "foundations" if number == 1 else slugify(str(AREA_TECHNICAL[number - 2]["area"]))
    next_slug = "synthesis" if number == 12 else slugify(str(AREA_TECHNICAL[number]["area"]))
    next_label = "Cross-area synthesis" if number == 12 else str(AREA_TECHNICAL[number]["area"])
    workflow = ''.join(f'<li><span>{index}</span>{esc(step)}</li>' for index, step in enumerate(detail["workflow"], start=1))
    example = ''.join(f'<li>{esc(step)}</li>' for step in detail["example"])
    glossary = ''.join(f'<div><dt>{esc(term)}</dt><dd>{esc(definition)}</dd></div>' for term, definition in detail["glossary"].items())
    paper_cards = paper_reading_cards(area, explorer)
    body = f'''
  <main id="main" class="course-layout">
    <aside>{lesson_navigation(number)}</aside>
    <article class="lesson-content">
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="../learn.html">Course</a><span>/</span>Area {number}</nav>{mobile_lesson_navigation(number)}
      <header class="lesson-hero"><p class="eyebrow">Module {number:02} · Area lesson · 10–12 minutes</p><h1>{esc(area['area'])}</h1><p class="lead">{esc(detail['hook'])}</p><div class="lesson-stats"><div><strong>{area['count']}</strong><span>mapped papers</span></div><div><strong>{area['share']}</strong><span>paper share</span></div><div><strong>{area['oral']}</strong><span>oral enrichment</span></div><div><strong>{area['public']}</strong><span>public attention</span></div></div><div class="lesson-goals"><strong>After this lesson, you can:</strong><ul><li>explain the area’s central technical problem;</li><li>trace a common method from input to evaluation;</li><li>read its representative paper without overstating the result.</li></ul></div></header>
      <section class="lesson-section"><p class="eyebrow">Start with intuition</p><h2>The mental model</h2><p class="big-idea">{esc(detail['mental_model'])}</p><div class="scope-box"><div><h3>Inside this area</h3><p>{esc(area['subareas'])}</p></div><div><h3>Common methods</h3><p>{esc(area['methods'])}</p></div></div></section>
      <section class="lesson-section"><p class="eyebrow">Technical core</p><h2>A common research pipeline</h2><ol class="technical-pipeline">{workflow}</ol><div class="equation"><small>{esc(detail['formula_title'])}</small><strong>{esc(detail['formula'])}</strong><p>{esc(detail['formula_explanation'])}</p></div></section>
      <section class="lesson-section"><p class="eyebrow">Make it concrete</p><h2>{esc(detail['example_title'])}</h2><div class="worked-example"><ol>{example}</ol></div><div class="pause-practice"><strong>Pause and predict</strong><p>{esc(brief['read_for'].split('|')[0].strip())}</p><details><summary>Show a strong answer</summary><p>Look for evidence tied to {esc(str(area['evaluation']).lower().rstrip('.'))}. Then check whether the result survives this limitation: {esc(area['fault'])}</p></details></div><div class="callout warning"><strong>Do not overclaim</strong><p>{esc(area['fault'])}</p></div></section>
      <section class="lesson-section"><p class="eyebrow">Evaluation</p><h2>How progress is tested</h2><p>{esc(area['evaluation'])}</p><div class="compare-note"><strong>Useful comparison</strong><p>{esc(detail['compare'])}</p></div></section>
      <section class="lesson-section"><p class="eyebrow">Paper lab</p><h2>Read three cases with a purpose</h2><p>The core paper receives a complete problem-to-limit walkthrough. The next two papers are comparison cases selected from this area’s program list.</p><div class="paper-stack">{paper_cards}</div><div class="evidence-note"><strong>Evidence note</strong><p>The core summary uses the local abstract and review workspace. Comparison cards expose metadata signals and a reading prompt; open the full paper before making a detailed technical claim.</p></div></section>
      <section class="lesson-section"><p class="eyebrow">Keep these terms</p><h2>Four-term glossary</h2><dl class="glossary-grid">{glossary}</dl></section>
      {quiz_markup(slug, detail['quiz'])}
      <nav class="lesson-next"><a class="previous" href="{prev_slug}.html">← Previous</a><span>Next module</span><a href="{next_slug}.html">{esc(next_label)} →</a></nav>
    </article>
  </main>'''
    return page_shell(str(area["area"]), body, description=f"A technical beginner-friendly lesson on {area['area']} with worked examples, papers, and a mastery check.")


def synthesis_page() -> str:
    trends = [
        ("Reasoning after pretraining", "1,099 mapped papers · 16.6%", "Reward-driven post-training, verification, search, and extra inference compute form the largest current area.", "The area boundary still includes general LLM work and needs paper-level review."),
        ("Systems and agents", "515 + 496 papers", "Both areas sit about 2.1 percentage points above this project’s nearby-venue baseline.", "A venue contrast does not explain why the difference exists."),
        ("Program versus public", "Theory: 1.45× oral · 0.46× public", "Official program selection and AlphaXiv attention emphasize different kinds of work.", "Neither signal is a complete quality ranking."),
        ("Robotics visibility", "2.9% share · 2.11× public", "A small area can receive unusually concentrated platform attention.", "The contrast does not establish importance, impact, or research quality."),
        ("Vision in venue context", "13.4% share · −3.1 pp vs baseline", "Multimodal research is large inside ICML while less represented than in nearby venues.", "The baseline is descriptive and depends on taxonomy alignment."),
        ("Artifact evidence", "Robotics visible-link share ≈38%", "Visible code and project pages make follow-up inspection easier.", "A link, stars, or a polished demo does not prove reproduction."),
    ]
    cards = ''.join(f'<article class="trend-evidence"><span class="tag">Trend {index}</span><h3>{esc(title)}</h3><strong>{esc(signal)}</strong><p><b>Supports:</b> {esc(supports)}</p><p><b>Does not prove:</b> {esc(limit)}</p></article>' for index, (title, signal, supports, limit) in enumerate(trends, start=1))
    body = f'''
  <main id="main" class="course-layout">
    <aside>{lesson_navigation('synthesis')}</aside>
    <article class="lesson-content">
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="../learn.html">Course</a><span>/</span>Synthesis</nav>{mobile_lesson_navigation('synthesis')}
      <header class="lesson-hero"><p class="eyebrow">Module 13 · Required · 15 minutes</p><h1>Connect the areas without mixing up the evidence.</h1><p class="lead">The conference story is not a list of twelve boxes. It comes from contrasts, shared methods, different evaluation cultures, and signals that answer different questions.</p><div class="lesson-goals"><strong>After this lesson, you can:</strong><ul><li>interpret the six central conference patterns;</li><li>connect neighboring areas through technical questions;</li><li>turn a statistical contrast into a careful reading plan.</li></ul></div></header>
      <section class="lesson-section"><p class="eyebrow">Six evidence cards</p><h2>Signal, interpretation, limitation</h2><div class="trend-grid">{cards}</div></section>
      <section class="lesson-section"><p class="eyebrow">Connections</p><h2>Six bridges worth remembering</h2><div class="bridge-list"><div><strong>Post-training ↔ RL</strong><p>Shared policy optimization ideas, but language reward design and verifiers create specialized settings.</p></div><div><strong>Multimodal ↔ Robotics</strong><p>Perception becomes action; evaluation gains temporal, physical, and safety constraints.</p></div><div><strong>Agents ↔ Systems</strong><p>Task success depends on tool reliability, latency, memory, and end-to-end cost.</p></div><div><strong>Graphs ↔ Science</strong><p>Relational and geometric priors encode molecular, physical, and structural knowledge.</p></div><div><strong>Generative models ↔ World models</strong><p>Both model distributions, but world models are judged by action-relevant dynamics and control.</p></div><div><strong>Theory ↔ Every area</strong><p>Formal results expose assumptions, limits, and scaling behavior behind empirical gains.</p></div></div></section>
      <section class="lesson-section"><p class="eyebrow">Worked synthesis</p><h2>From surprising number to research question</h2><div class="worked-example"><ol><li><strong>Observe:</strong> robotics has 2.9% paper share and 2.11× public-attention enrichment.</li><li><strong>Say safely:</strong> attention on AlphaXiv is concentrated relative to the area’s size.</li><li><strong>Generate hypotheses:</strong> demos, embodied tasks, accessible project pages, or a small number of highly visible papers may contribute.</li><li><strong>Test:</strong> inspect attention distribution, paper types, artifacts, and matched non-robotics examples.</li><li><strong>Do not say:</strong> robotics is objectively the best or fastest-growing field.</li></ol></div></section>
      <section class="lesson-section"><p class="eyebrow">Capstone</p><h2>Write a one-page field briefing</h2><div class="capstone"><ol><li>Choose one area and one neighboring area.</li><li>State the central problem of each in plain language.</li><li>Compare one method and one evaluation difference.</li><li>Use one conference-level signal correctly.</li><li>Explain one representative paper as problem → method → evidence → result → limit.</li><li>End with one open question rather than a universal prediction.</li></ol><a class="button secondary" href="../reports/icml2026_newcomer_briefing_template.md">Open briefing template</a></div></section>
      {quiz_markup('synthesis', SYNTHESIS_QUIZ)}
      <nav class="lesson-next"><a class="previous" href="{slugify(AREA_TECHNICAL[-1]['area'])}.html">← Previous</a><span>Course assessment</span><a href="../quiz.html">Take the full quiz →</a></nav>
    </article>
  </main>'''
    return page_shell("Cross-area synthesis", body, description="Connect the 12 ICML 2026 research areas through six evidence-aware conference trends.")


def build() -> None:
    LESSON_DIR.mkdir(parents=True, exist_ok=True)
    briefing_rows = {row["area"]: row for row in read_csv(BRIEFINGS)}
    explorer_rows = {row["title"]: row for row in read_csv(EXPLORER)}

    (DOCS / "learn.html").write_text(learning_index(), encoding="utf-8")
    (LESSON_DIR / "foundations.html").write_text(foundations_page(), encoding="utf-8")
    for area in AREA_TECHNICAL:
        number = int(area["number"])
        page = area_page(area, AREA_LESSONS[number], briefing_rows[str(area["area"])], explorer_rows)
        (LESSON_DIR / f"{slugify(str(area['area']))}.html").write_text(page, encoding="utf-8")
    (LESSON_DIR / "synthesis.html").write_text(synthesis_page(), encoding="utf-8")
    routes = [
        "",
        "learn.html",
        "quiz.html",
        "dashboard.html",
        "icml2026_newcomer_slides.html",
        "about.html",
        "learn/foundations.html",
        *(f"learn/{slugify(str(area['area']))}.html" for area in AREA_TECHNICAL),
        "learn/synthesis.html",
    ]
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sitemap.extend(f"  <url><loc>https://juyoungml.github.io/icml2026/{route}</loc></url>" for route in routes)
    sitemap.append("</urlset>")
    (DOCS / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")
    print(f"Wrote learning course: {LESSON_DIR.relative_to(ROOT)} (14 modules)")


if __name__ == "__main__":
    build()
