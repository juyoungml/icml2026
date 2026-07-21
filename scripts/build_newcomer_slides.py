#!/usr/bin/env python3
"""Build a self-contained HTML slide deck for the ICML 2026 newcomer course."""

from __future__ import annotations

import base64
import html as html_lib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
FIGURES = ROOT / "figures"


AREA_TECHNICAL = [
    {
        "number": 1,
        "area": "LLM Reasoning, Post-Training, and RLVR",
        "count": "1,099",
        "share": "16.6%",
        "oral": "1.29×",
        "public": "2.03×",
        "subareas": "Reasoning models and chain-of-thought; reward modeling and preference feedback; RL with verifiable rewards; diffusion language models; general LLM training and evaluation.",
        "methods": "GRPO and policy optimization; process or outcome rewards; test-time search and sampling; verifiers; preference learning; alternative decoding orders.",
        "evaluation": "Mathematics and code accuracy; pass@k; reward-model calibration; reasoning coverage; compute-performance tradeoffs.",
        "fault": "A high score on cheaply verifiable tasks may not transfer to open-ended reasoning, and broad LLM training papers can inflate the area boundary.",
        "paper": "The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models",
        "problem": "Arbitrary-order diffusion language models have more flexible decoding paths, but that flexibility may avoid uncertain tokens needed for exploration.",
        "method": "Compare arbitrary-order and autoregressive reasoning coverage, then apply standard GRPO while retaining parallel diffusion decoding.",
        "evidence": "Mathematics and coding evaluations, pass@k coverage, matched RL comparisons, and 89.1% reported GSM8K accuracy.",
        "result": "In the tested reasoning settings, simpler autoregressive RL elicits stronger reasoning than preserving arbitrary token order.",
        "limit": "The conclusion is task-dependent; arbitrary ordering can still help constraint-satisfaction or non-reasoning tasks.",
        "paper_url": "https://icml.cc/virtual/2026/poster/61998",
        "badge": "Outstanding Paper · oral",
    },
    {
        "number": 2,
        "area": "Multimodal, Vision, and Perception",
        "count": "889",
        "share": "13.4%",
        "oral": "0.58×",
        "public": "0.80×",
        "subareas": "Vision-language reasoning; cross-modal alignment; video and motion; 3D and spatial understanding; robustness and adversarial perception.",
        "methods": "Vision-language post-training; multimodal transformers; temporal modeling; 3D geometry; video diffusion; grounding and attribution.",
        "evaluation": "Image and video reasoning; spatial consistency; temporal dynamics; localization; robustness under corruptions and distribution shift.",
        "fault": "Models can answer through language priors without using visual evidence, while aggregate vision labels hide large differences between video, 3D, and robustness work.",
        "paper": "Motion Attribution for Video Generation",
        "problem": "Video generators improve quickly, but it is unclear which fine-tuning clips cause better or worse motion rather than merely changing appearance.",
        "method": "Motive uses gradient-based data attribution with motion-weighted loss masks to isolate temporal influence from static appearance.",
        "evidence": "Text-to-video fine-tuning, VBench motion measures, data-curation experiments, and a reported 74.1% human-preference win rate over the base model.",
        "result": "High-influence clips selected by motion attribution improve temporal consistency, physical plausibility, smoothness, and dynamic degree.",
        "limit": "Attribution depends on the chosen motion loss and model; human preference does not fully establish causal or physical correctness.",
        "paper_url": "https://icml.cc/virtual/2026/poster/60542",
        "badge": "Outstanding Paper Honorable Mention · oral",
    },
    {
        "number": 3,
        "area": "Theory, Optimization, and Algorithms",
        "count": "737",
        "share": "11.1%",
        "oral": "1.45×",
        "public": "0.46×",
        "subareas": "Statistical learning theory; online learning and bandits; convex and nonconvex optimization; Bayesian methods; transformer theory; numerical methods.",
        "methods": "Generalization bounds; regret analysis; stochastic optimization; spectral analysis; probabilistic inference; expressivity and impossibility results.",
        "evaluation": "Proof assumptions and rates; synthetic experiments; sensitivity to dimension, data, compute, and hyperparameters; empirical checks of predicted behavior.",
        "fault": "A theorem can be correct yet rely on assumptions or scales that do not describe current production models.",
        "paper": "To Grok Grokking: Provable Grokking in Ridge Regression",
        "problem": "Why can a model fit its training data early but generalize only much later?",
        "method": "Analyze over-parameterized ridge regression trained by gradient descent with weight decay and derive quantitative grokking-time bounds.",
        "evidence": "End-to-end proofs of overfitting, delayed generalization, and eventual low error; hyperparameter studies; nonlinear neural-network checks.",
        "result": "Grokking delay changes predictably with training conditions and can be amplified or removed through hyperparameter choices.",
        "limit": "The rigorous result is for classical linear regression; nonlinear experiments support transfer but do not prove the same mechanism for large models.",
        "paper_url": "https://icml.cc/virtual/2026/poster/66206",
        "badge": "Outstanding Paper Honorable Mention · oral",
    },
    {
        "number": 4,
        "area": "AI for Science, Health, and Neuro",
        "count": "587",
        "share": "8.9%",
        "oral": "1.08×",
        "public": "0.33×",
        "subareas": "Proteins and molecules; physical science and climate; time series and forecasting; neural dynamics; spiking and biological signals.",
        "methods": "Graph and geometric networks; scientific foundation models; diffusion and flow; equivariant architectures; uncertainty modeling; simulators and surrogates.",
        "evaluation": "Scientific validity; physical constraints; calibrated uncertainty; out-of-distribution generalization; laboratory or domain-expert verification.",
        "fault": "Benchmark improvement may not translate into a valid molecule, useful forecast, clinical decision, or new scientific finding.",
        "paper": "Protein Autoregressive Modeling via Multiscale Structure Generation",
        "problem": "Protein backbones have structure at several scales, while single-scale generation can miss the relationship between global topology and atomic detail.",
        "method": "PAR combines multiscale downsampling, an autoregressive transformer for next-scale conditioning, and a flow-based decoder for backbone atoms.",
        "evidence": "Unconditional backbone generation, zero-shot conditional generation, motif scaffolding, design-quality measures, and scaling analysis.",
        "result": "Coarse-to-fine autoregression produces high-quality backbones and supports flexible conditioning without task-specific fine-tuning.",
        "limit": "Structural validity is not biological function; data overlap, physical plausibility, and laboratory performance still require direct checks.",
        "paper_url": "https://icml.cc/virtual/2026/poster/66808",
        "badge": "Oral",
    },
    {
        "number": 5,
        "area": "Data-Centric, Causal, and Federated ML",
        "count": "526",
        "share": "7.9%",
        "oral": "0.75×",
        "public": "0.64×",
        "subareas": "Data quality and labels; continual learning; causal discovery and inference; federated learning; distributed and heterogeneous clients.",
        "methods": "Replay and rehearsal; data valuation and selection; causal graphs and interventions; federated aggregation; debiasing; task adaptation.",
        "evaluation": "Forgetting and forward transfer; intervention accuracy; client heterogeneity; privacy and communication cost; label efficiency and robustness.",
        "fault": "Predictive gains do not establish causality, and simplified client or task sequences may hide real deployment constraints.",
        "paper": "Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning",
        "problem": "Robot policies must learn new skills without destroying old ones, but continual-learning knowledge mostly comes from smaller models trained from scratch.",
        "method": "Compare large pretrained VLA models with smaller behavior-cloning policies under sequential tasks and simple experience replay.",
        "evidence": "Forgetting, forward learning, replay-buffer size, retained knowledge, and recovery after fine-tuning across robot-policy tasks.",
        "result": "Pretraining changes continual-learning dynamics: small replay buffers can produce little or no forgetting while retaining fast adaptation.",
        "limit": "The result may depend on the pretrained model, task similarity, replay access, and chosen robotics sequence; taxonomy placement also crosses into robotics.",
        "paper_url": "https://icml.cc/virtual/2026/poster/63561",
        "badge": "Oral",
    },
    {
        "number": 6,
        "area": "Systems and Efficient Foundation Models",
        "count": "515",
        "share": "7.8%",
        "oral": "0.69×",
        "public": "1.31×",
        "subareas": "Large-scale training; optimizers and architectures; model compression; quantization; KV-cache and long context; inference and serving.",
        "methods": "Parallel optimization; spectral constraints; low precision; sparsity and MoE; cache pruning; kernels; speculative decoding; systems co-design.",
        "evaluation": "End-to-end throughput and latency; memory; training stability; energy or cost; quality regression; results across hardware, batch sizes, and sequence lengths.",
        "fault": "An isolated kernel speedup may disappear end to end, and efficiency can trade away reasoning, calibration, or safety.",
        "paper": "Controlled LLM Training on Spectral Sphere",
        "problem": "Large-model optimizers can control update scale while weights and activations still drift, weakening width-invariant stability guarantees.",
        "method": "The Spectral Sphere Optimizer constrains module weights and updates, derives steepest descent on the spectral sphere, and implements it in Megatron.",
        "evidence": "Pretraining Dense 1.7B, MoE 8B-A1B, and 200-layer DeepNet models against AdamW and Muon; activation, outlier, and router-balance analysis.",
        "result": "SSO reports faster or better optimization with bounded activations, suppressed outliers, and improved MoE load balance.",
        "limit": "The claim needs matched compute and hardware accounting, broader model families, and end-to-end cost analysis beyond optimizer stability.",
        "paper_url": "https://icml.cc/virtual/2026/poster/66212",
        "badge": "Oral",
    },
    {
        "number": 7,
        "area": "Safety, Governance, Privacy, and Society",
        "count": "502",
        "share": "7.6%",
        "oral": "1.41×",
        "public": "0.51×",
        "subareas": "Adversarial safety and security; alignment and oversight; privacy; fairness and social effects; governance and evaluation practice.",
        "methods": "Red teaming; probes and monitors; adversarial training; privacy attacks and defenses; causal audits; human studies; policy analysis.",
        "evaluation": "Attack success and adaptive evasion; false positives; distribution shift; realistic threat models; downstream harm; subgroup and privacy measures.",
        "fault": "A narrow detector benchmark may not represent real risk, and training against a monitor can teach a model to evade it.",
        "paper": "The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes",
        "problem": "Training against white-box deception detectors may produce honest behavior—or teach a deceptive model to hide from the detector.",
        "method": "Use a coding reward-hacking environment, deception probes, RL penalties, KL regularization, and a taxonomy of honest and obfuscated outcomes.",
        "evidence": "Probe scores, representation drift, task return, policy text, RL comparisons, and a policy-gradient argument for detector-evading behavior.",
        "result": "Representation drift can produce obfuscated activations; detector penalties can incentivize obfuscated policies; sufficiently high KL plus penalty yields honest policies in this setting.",
        "limit": "The coding environment and selected detector do not cover every form of deception, monitoring, or real-world agent behavior.",
        "paper_url": "https://icml.cc/virtual/2026/poster/60766",
        "badge": "Outstanding Paper Honorable Mention · oral",
    },
    {
        "number": 8,
        "area": "Agents, Code, and Tool Use",
        "count": "496",
        "share": "7.5%",
        "oral": "1.19×",
        "public": "1.52×",
        "subareas": "Agent evaluation; tool use; code generation and verification; software tasks; multi-agent planning, search, and coordination.",
        "methods": "Planning and reflection; tool routing; memory; execution feedback; multi-agent roles; verifiers; environment and benchmark design.",
        "evaluation": "Task success; pass rates; tool errors; cost and latency; recovery from failure; contamination; realistic environment coverage; safety boundaries.",
        "fault": "Better instructions, tools, or scaffolding can look like learned intelligence, while benchmark success may depend on fragile environment details.",
        "paper": "PaperBanana: Automating Academic Illustration for AI Scientists",
        "problem": "Publication-ready research figures require reference search, content planning, rendering, and repeated design revision.",
        "method": "Orchestrate specialized VLM and image-generation agents for retrieval, planning, rendering, and iterative self-critique.",
        "evidence": "PaperBananaBench with 292 NeurIPS 2025 method diagrams; comparisons on faithfulness, conciseness, readability, aesthetics, and plot generation.",
        "result": "The full agentic pipeline reports consistent gains over leading diagram-generation baselines.",
        "limit": "The evaluation may favor curated academic styles; repository, benchmark release, unusual-domain behavior, and component ablations need checking.",
        "paper_url": "https://icml.cc/virtual/2026/poster/65206",
        "badge": "High public attention · artifact visible",
    },
    {
        "number": 9,
        "area": "Graphs, Geometry, and Representation Learning",
        "count": "391",
        "share": "5.9%",
        "oral": "0.61×",
        "public": "0.38×",
        "subareas": "Graph neural networks; geometric representation learning; manifolds; equivariant networks; relational and structured latent representations.",
        "methods": "Message passing; permutation equivariance; invariant and equivariant layers; spectral graph methods; geometric priors; contrastive and self-supervised objectives.",
        "evaluation": "Generalization across graph size; algorithm execution; molecular and physical validity; symmetry tests; expressivity and oversmoothing.",
        "fault": "Fitting small graph instances does not prove an architecture learned an algorithm that generalizes to arbitrary size.",
        "paper": "Which Algorithms Can Graph Neural Networks Learn?",
        "problem": "Message-passing GNNs often imitate algorithms empirically, but it is unclear when finite training examples imply correct behavior on larger inputs.",
        "method": "Develop necessary conditions for learning algorithms with MPNNs, prove generalization properties, establish impossibility results, and derive stronger variants.",
        "evidence": "Theorems covering shortest paths, minimum spanning trees, dynamic programming, and 0–1 knapsack, plus limits for tasks standard MPNNs cannot compute.",
        "result": "The framework separates algorithms learnable from small instances from tasks requiring more expressive message-passing architectures.",
        "limit": "Formal learnability conditions may require idealized data, optimization, precision, or architecture assumptions not guaranteed in practice.",
        "paper_url": "https://icml.cc/virtual/2026/poster/65099",
        "badge": "Oral",
    },
    {
        "number": 10,
        "area": "Generative Modeling",
        "count": "379",
        "share": "5.7%",
        "oral": "0.83×",
        "public": "0.96×",
        "subareas": "Diffusion sampling and inverse problems; flow models; image and video generation; controllable generation; sampling theory and consistency.",
        "methods": "Score matching; denoising diffusion; flow matching; transport; guidance; distillation; random matrix analysis; efficient sampling.",
        "evaluation": "Sample quality and diversity; likelihood or bounds; speed; consistency across seeds and data splits; controllability; human preference; physical plausibility.",
        "fault": "Media-quality metrics, sampling theory, and reproducibility questions are different goals and should not be collapsed into one ranking.",
        "paper": "A Random Matrix Perspective on the Consistency of Diffusion Models",
        "problem": "Diffusion models trained on different data splits can produce surprisingly similar samples from the same noise seed. Why?",
        "method": "Build a random-matrix framework for finite-data effects on linear denoisers and sampling maps, including expectations, variance, and sampling trajectories.",
        "evidence": "Closed-form predictions for linear models and empirical validation on UNet and DiT architectures in a non-memorization regime.",
        "result": "Shared Gaussian statistics explain much cross-split consistency; disagreement depends on spectral anisotropy, input inhomogeneity, and dataset size.",
        "limit": "The sharp theory is linear and Gaussian; nonlinear modern generators may depart from it through feature learning, memorization, or conditioning.",
        "paper_url": "https://icml.cc/virtual/2026/poster/62241",
        "badge": "Outstanding Paper Honorable Mention · oral",
    },
    {
        "number": 11,
        "area": "Reinforcement Learning and Control",
        "count": "312",
        "share": "4.7%",
        "oral": "0.76×",
        "public": "0.66×",
        "subareas": "Core and offline RL; online learning and exploration; policy optimization; robust RL; control; model-based learning and planning.",
        "methods": "Value and policy learning; actor-critic; offline objectives; model-free planning; regret analysis; robust optimization; compute-adaptive policies.",
        "evaluation": "Return and sample efficiency; generalization across horizons; offline-to-online transfer; robustness; safety; compute and parameter budgets.",
        "fault": "LLM-facing RL is only one part of the field, and reward or benchmark design can dominate the apparent improvement.",
        "paper": "On Computation and Reinforcement Learning",
        "problem": "Standard RL architectures mix parameter count with computation, making it hard to ask whether a fixed-size policy benefits from more compute.",
        "method": "Formalize compute-bounded policies, prove capability and horizon-generalization separations, and build a variable-compute minimal architecture.",
        "evidence": "Theory plus 31 online and offline RL tasks, comparing extra compute with feed-forward and residual policies using up to five times more parameters.",
        "result": "A fixed-parameter policy can solve harder and longer-horizon tasks by spending more computation at decision time.",
        "limit": "The chosen tasks and architecture may not capture wall-clock latency, environment interaction cost, or complex continuous-control deployments.",
        "paper_url": "https://icml.cc/virtual/2026/poster/65047",
        "badge": "Oral",
    },
    {
        "number": 12,
        "area": "Robotics, Embodiment, and World Models",
        "count": "195",
        "share": "2.9%",
        "oral": "0.81×",
        "public": "2.11×",
        "subareas": "Vision-language-action policies; manipulation; robot memory; latent actions; embodied planning; world models and physical prediction.",
        "methods": "VLA pretraining; behavior cloning; policy learning; memory modules; latent dynamics; video and action representations; simulation and real-robot transfer.",
        "evaluation": "Long-horizon success; memory and recovery; occlusion; real versus simulated robots; task diversity; robustness; safety and latency.",
        "fault": "Visually impressive demos and project pages can attract attention while hiding narrow tasks, resets, manual intervention, or weak generalization.",
        "paper": "RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies",
        "problem": "VLA memory mechanisms are evaluated in narrow, inconsistent settings, limiting comparison on history-dependent manipulation.",
        "method": "Create 16 tasks across temporal, spatial, object, and procedural memory, then compare 14 memory-augmented variants on a π0.5 backbone.",
        "evidence": "Long-horizon tasks involving repeated actions and occlusion, with controlled comparisons of memory representations and integration strategies.",
        "result": "No single memory design wins everywhere; effectiveness depends strongly on the task and type of memory required.",
        "limit": "Benchmark coverage, real-world transfer, base-policy dependence, and the currently mismatched repository metadata all need further inspection.",
        "paper_url": "https://icml.cc/virtual/2026/poster/65933",
        "badge": "Oral · high public attention",
    },
]


def image_data_uri(name: str) -> str:
    path = FIGURES / name
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def technical_area_slides() -> str:
    slides: list[str] = []
    for area in AREA_TECHNICAL:
        esc = {key: html_lib.escape(str(value)) for key, value in area.items()}
        slides.append(
            f'''  <section class="slide dense" data-kicker="Area {esc['number']} of 12">
    <div class="slide-inner">
      <p class="eyebrow">Technical area map</p>
      <h2>{esc['area']}</h2>
      <div class="statline compact-stats">
        <div class="stat"><strong>{esc['count']}</strong><span>mapped papers</span></div>
        <div class="stat"><strong>{esc['share']}</strong><span>paper share</span></div>
        <div class="stat"><strong>{esc['oral']}</strong><span>oral enrichment</span></div>
        <div class="stat"><strong>{esc['public']}</strong><span>public attention</span></div>
      </div>
      <div class="grid two technical-grid">
        <div class="card"><h3>Subareas</h3><p>{esc['subareas']}</p></div>
        <div class="card tint-blue"><h3>Common methods</h3><p>{esc['methods']}</p></div>
        <div class="card tint-green"><h3>What gets evaluated</h3><p>{esc['evaluation']}</p></div>
        <div class="card tint-orange"><h3>Main fault line</h3><p>{esc['fault']}</p></div>
      </div>
    </div>
  </section>'''
        )
        slides.append(
            f'''  <section class="slide dense" data-kicker="Representative paper · area {esc['number']}">
    <div class="slide-inner">
      <p class="eyebrow">{esc['area']}</p>
      <h2 class="paper-heading">{esc['paper']}</h2>
      <span class="label">{esc['badge']}</span>
      <div class="grid paper-grid">
        <div class="card tint-blue"><h3>Problem</h3><p>{esc['problem']}</p></div>
        <div class="card tint-purple"><h3>Method</h3><p>{esc['method']}</p></div>
        <div class="card tint-green"><h3>Evidence</h3><p>{esc['evidence']}</p></div>
        <div class="card"><h3>Main result</h3><p>{esc['result']}</p></div>
        <div class="card tint-orange"><h3>Limit to remember</h3><p>{esc['limit']}</p></div>
      </div>
      <p class="source"><a href="{esc['paper_url']}">ICML paper page</a> · Technical summary is based on the local abstract and review workspace.</p>
    </div>
  </section>'''
        )
    return "\n\n".join(slides)


def build_html() -> str:
    replacements = {
        "{{AREA_FIGURE}}": image_data_uri("manual_taxonomy_area_sizes.png"),
        "{{SIGNAL_FIGURE}}": image_data_uri("program_signal_calibration.png"),
        "{{BASELINE_FIGURE}}": image_data_uri("historical_venue_area_deltas.png"),
        "{{SEMANTIC_FIGURE}}": image_data_uri("semantic_cluster_map.png"),
        "{{AREA_TECHNICAL_SLIDES}}": technical_area_slides(),
    }
    html = r'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="color-scheme" content="light dark">
  <title>A Friendly Roadmap to ICML 2026</title>
  <style>
    :root {
      --ink: #17202a;
      --muted: #596675;
      --paper: #f7f4ed;
      --panel: #fffdf8;
      --line: #d9d4c8;
      --blue: #1f5f8b;
      --blue-soft: #dceaf3;
      --green: #2f7259;
      --green-soft: #dcece4;
      --orange: #b55c28;
      --orange-soft: #f5e3d4;
      --purple: #70548f;
      --purple-soft: #ebe2f2;
      --red: #a54747;
      --shadow: 0 18px 50px rgba(30, 41, 49, .14);
    }
    * { box-sizing: border-box; }
    html, body { height: 100%; margin: 0; overflow: hidden; }
    body {
      background: #dedbd4;
      color: var(--ink);
      font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    button { font: inherit; }
    .deck { height: 100%; position: relative; }
    .slide {
      position: absolute;
      inset: 0;
      display: none;
      overflow: auto;
      padding: clamp(20px, 2.4vw, 38px) clamp(22px, 3vw, 50px) 76px;
      background:
        radial-gradient(circle at 92% 8%, rgba(31,95,139,.10), transparent 28%),
        linear-gradient(140deg, var(--paper), #f2efe7);
    }
    .slide.active { display: flex; flex-direction: column; }
    .slide::after {
      content: attr(data-kicker);
      position: absolute;
      top: 24px;
      right: 34px;
      color: var(--blue);
      font-size: 12px;
      font-weight: 800;
      letter-spacing: .13em;
      text-transform: uppercase;
    }
    .slide-inner { width: min(1480px, 100%); margin: auto; }
    h1, h2, h3, p { margin-top: 0; }
    h1 { font-size: clamp(44px, 6vw, 86px); line-height: .98; letter-spacing: -.045em; max-width: 1050px; }
    h2 { font-size: clamp(34px, 4.2vw, 64px); line-height: 1.03; letter-spacing: -.035em; margin-bottom: 24px; }
    h3 { font-size: clamp(19px, 2vw, 28px); line-height: 1.16; margin-bottom: 10px; }
    p, li { font-size: clamp(16px, 1.4vw, 22px); line-height: 1.4; }
    .lead { font-size: clamp(23px, 2.6vw, 38px); line-height: 1.28; color: var(--muted); max-width: 1000px; }
    .eyebrow { color: var(--orange); font-weight: 800; letter-spacing: .12em; text-transform: uppercase; font-size: 13px; margin-bottom: 20px; }
    .big-number { font-size: clamp(72px, 11vw, 155px); font-weight: 850; letter-spacing: -.07em; line-height: .85; color: var(--blue); }
    .caption { color: var(--muted); font-size: clamp(13px, 1.15vw, 17px); line-height: 1.35; }
    .source { color: var(--muted); font-size: 12px; margin-top: 12px; }
    .grid { display: grid; gap: clamp(14px, 2vw, 26px); }
    .two { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .three { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    .four { grid-template-columns: repeat(4, minmax(0, 1fr)); }
    .card {
      background: rgba(255,253,248,.9);
      border: 1px solid var(--line);
      border-radius: 20px;
      padding: clamp(16px, 2.1vw, 28px);
      box-shadow: 0 8px 26px rgba(30,41,49,.07);
    }
    .card p, .card li { font-size: clamp(15px, 1.35vw, 20px); }
    .card p:last-child { margin-bottom: 0; }
    .tint-blue { background: var(--blue-soft); border-color: #b9d3e4; }
    .tint-green { background: var(--green-soft); border-color: #bad9ca; }
    .tint-orange { background: var(--orange-soft); border-color: #e7c6ac; }
    .tint-purple { background: var(--purple-soft); border-color: #d3c2df; }
    .label { display: inline-block; border-radius: 999px; padding: 5px 10px; margin-bottom: 12px; font-size: 12px; font-weight: 800; letter-spacing: .04em; background: var(--blue-soft); color: var(--blue); }
    .quote { border-left: 6px solid var(--orange); padding-left: 24px; font-size: clamp(25px, 3vw, 44px); line-height: 1.25; max-width: 1050px; }
    .plain-list { list-style: none; padding: 0; margin: 0; }
    .plain-list li { position: relative; padding-left: 31px; margin: 12px 0; }
    .plain-list li::before { content: "→"; color: var(--orange); font-weight: 800; position: absolute; left: 0; }
    .area-list { columns: 2; column-gap: 42px; list-style: none; padding: 0; }
    .area-list li { break-inside: avoid; padding: 7px 0; font-size: clamp(15px, 1.35vw, 20px); }
    .area-list strong { color: var(--blue); }
    .signal-row { display: grid; grid-template-columns: 170px 1fr 1fr; gap: 12px; align-items: stretch; margin: 10px 0; }
    .signal-row > div { border-radius: 14px; padding: 13px 16px; background: var(--panel); border: 1px solid var(--line); font-size: clamp(14px, 1.2vw, 18px); }
    .signal-row .name { font-weight: 800; color: var(--blue); }
    .figure-wrap { background: white; border: 1px solid var(--line); border-radius: 20px; padding: 12px; box-shadow: var(--shadow); }
    .figure-wrap img { display: block; width: 100%; max-height: 61vh; object-fit: contain; }
    .split { display: grid; grid-template-columns: minmax(0, .9fr) minmax(0, 1.35fr); gap: clamp(24px, 4vw, 58px); align-items: center; }
    .statline { display: flex; gap: 20px; flex-wrap: wrap; margin: 20px 0; }
    .stat { min-width: 150px; }
    .stat strong { display: block; font-size: clamp(30px, 3.5vw, 52px); color: var(--blue); line-height: 1; }
    .stat span { color: var(--muted); font-size: 14px; }
    .safe { border-left: 7px solid var(--green); }
    .unsafe { border-left: 7px solid var(--red); }
    .paper-title { font-size: clamp(18px, 1.6vw, 24px); font-weight: 800; line-height: 1.18; }
    .paper-heading { font-size: clamp(28px, 3.4vw, 51px); max-width: 1320px; margin-bottom: 12px; }
    .dense h2 { margin-bottom: 14px; }
    .compact-stats { margin: 10px 0 18px; }
    .compact-stats .stat { min-width: 140px; }
    .compact-stats .stat strong { font-size: clamp(27px, 3vw, 44px); }
    .technical-grid { gap: 14px; }
    .technical-grid .card { padding: 16px 20px; }
    .technical-grid .card p { font-size: clamp(14px, 1.15vw, 18px); line-height: 1.35; }
    .paper-grid { grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 14px; margin-top: 12px; }
    .paper-grid .card { grid-column: span 2; padding: 16px 20px; }
    .paper-grid .card:nth-child(4), .paper-grid .card:nth-child(5) { grid-column: span 3; }
    .paper-grid .card p { font-size: clamp(14px, 1.12vw, 18px); line-height: 1.34; }
    .paper-grid h3 { font-size: clamp(17px, 1.45vw, 22px); }
    a { color: var(--blue); }
    .answer {
      display: none;
      margin-top: 16px;
      padding: 18px;
      border-radius: 14px;
      background: var(--green-soft);
      border: 1px solid #afd2c0;
      font-size: clamp(15px, 1.3vw, 19px);
    }
    .answer.visible { display: block; }
    .reveal {
      border: 0;
      border-radius: 999px;
      padding: 10px 16px;
      background: var(--blue);
      color: white;
      font-weight: 750;
      cursor: pointer;
    }
    .controls {
      position: fixed;
      z-index: 20;
      left: 0;
      right: 0;
      bottom: 0;
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 12px 18px calc(12px + env(safe-area-inset-bottom));
      background: rgba(23,32,42,.93);
      color: white;
      backdrop-filter: blur(12px);
    }
    .controls button { width: 38px; height: 34px; border-radius: 10px; border: 1px solid rgba(255,255,255,.25); background: transparent; color: white; cursor: pointer; }
    .controls button:hover { background: rgba(255,255,255,.12); }
    .progress { height: 5px; flex: 1; border-radius: 99px; overflow: hidden; background: rgba(255,255,255,.2); }
    .progress > span { display: block; height: 100%; background: #e69a5f; width: 0; transition: width .2s ease; }
    .counter { font-size: 13px; min-width: 66px; text-align: center; }
    .help { font-size: 12px; color: rgba(255,255,255,.72); white-space: nowrap; }
    .overview { overflow: auto; background: #d8d5cf; padding: 24px; }
    .overview .deck { display: grid; grid-template-columns: repeat(auto-fit, minmax(330px, 1fr)); gap: 20px; height: auto; }
    .overview .slide { display: flex; position: relative; aspect-ratio: 16/9; transform: none; padding: 24px; border-radius: 12px; overflow: hidden; box-shadow: var(--shadow); cursor: pointer; }
    .overview .slide-inner { transform: scale(.64); transform-origin: center; width: 150%; }
    .overview .controls { display: none; }
    .overview .slide::after { display: none; }
    .end-links a { color: var(--blue); font-size: 17px; }
    @media (max-width: 800px) {
      .two, .three, .four, .split { grid-template-columns: 1fr; }
      .three, .four { grid-template-columns: repeat(2, minmax(0, 1fr)); }
      .area-list { columns: 1; }
      .signal-row { grid-template-columns: 1fr; }
      .paper-grid { grid-template-columns: 1fr; }
      .paper-grid .card, .paper-grid .card:nth-child(4), .paper-grid .card:nth-child(5) { grid-column: auto; }
      .help { display: none; }
      .slide { padding-left: 22px; padding-right: 22px; }
    }
    @media print {
      html, body { height: auto; overflow: visible; background: white; }
      .deck { height: auto; }
      .slide { display: flex !important; position: relative; width: 100%; height: 100vh; page-break-after: always; padding-bottom: 40px; }
      .controls { display: none; }
    }
    @media (prefers-reduced-motion: reduce) { * { scroll-behavior: auto !important; transition: none !important; } }
  </style>
</head>
<body>
<main class="deck" id="deck">
  <section class="slide active" data-kicker="Newcomer course">
    <div class="slide-inner">
      <p class="eyebrow">A friendly, evidence-aware introduction</p>
      <h1>A Roadmap to<br>ICML 2026</h1>
      <p class="lead">Understand most of the conference map without reading thousands of papers.</p>
      <div class="statline">
        <div class="stat"><strong>6,628</strong><span>paper records</span></div>
        <div class="stat"><strong>12</strong><span>broad areas</span></div>
        <div class="stat"><strong>6</strong><span>main patterns</span></div>
      </div>
      <p class="caption">Use ← and → to move. Press O for overview, F for full screen, and P to print or save as PDF.</p>
    </div>
  </section>

  <section class="slide" data-kicker="The promise">
    <div class="slide-inner">
      <h2>What does “understand 80%” mean?</h2>
      <p class="quote">Know most of the map—and know how to explore the rest.</p>
      <div class="grid three" style="margin-top:28px">
        <div class="card tint-blue"><h3>Explain</h3><p>Describe the main areas and trends in normal language.</p></div>
        <div class="card tint-green"><h3>Compare</h3><p>Tell which evidence supports a claim and which evidence does not.</p></div>
        <div class="card tint-orange"><h3>Explore</h3><p>Place a new paper on the map and ask useful follow-up questions.</p></div>
      </div>
    </div>
  </section>

  <section class="slide" data-kicker="Evidence first">
    <div class="slide-inner">
      <h2>Five signals. Five different questions.</h2>
      <div class="signal-row"><div class="name">Paper share</div><div>How large is an area?</div><div>Not: Is every paper important?</div></div>
      <div class="signal-row"><div class="name">Program signal</div><div>Which areas appear more among orals and awards?</div><div>Not: Is this a complete quality ranking?</div></div>
      <div class="signal-row"><div class="name">AlphaXiv attention</div><div>What attracts attention on that platform?</div><div>Not: What is objectively best?</div></div>
      <div class="signal-row"><div class="name">Venue baseline</div><div>What is more or less emphasized than nearby venues?</div><div>Not: What caused the difference?</div></div>
      <div class="signal-row"><div class="name">Artifact link</div><div>Is code or another artifact visible?</div><div>Not: Can the result be reproduced?</div></div>
    </div>
  </section>

  <section class="slide" data-kicker="Confidence">
    <div class="slide-inner">
      <h2>Good understanding includes uncertainty</h2>
      <div class="grid three">
        <div class="card tint-green"><span class="label">Checked fact</span><h3>Direct count or official label</h3><p>Example: the official corpus contains 6,628 paper records.</p></div>
        <div class="card tint-blue"><span class="label">Directional pattern</span><h3>Several signals agree</h3><p>Useful for navigation, but paper-level review is still needed.</p></div>
        <div class="card tint-orange"><span class="label">Open question</span><h3>The evidence cannot settle it</h3><p>A strong next step is more valuable than a confident guess.</p></div>
      </div>
      <p class="lead" style="margin-top:30px">The project still has 310 manual claim and area review rows to complete.</p>
    </div>
  </section>

  <section class="slide" data-kicker="The map">
    <div class="slide-inner split">
      <div>
        <h2>Twelve broad areas</h2>
        <p class="lead">A navigation map—not twelve sealed boxes.</p>
      </div>
      <ul class="area-list">
        <li><strong>1.</strong> LLM reasoning and post-training</li>
        <li><strong>2.</strong> Multimodal, vision, and perception</li>
        <li><strong>3.</strong> Theory, optimization, and algorithms</li>
        <li><strong>4.</strong> AI for science, health, and neuro</li>
        <li><strong>5.</strong> Data, causality, and federated ML</li>
        <li><strong>6.</strong> Systems and efficient models</li>
        <li><strong>7.</strong> Safety, governance, and privacy</li>
        <li><strong>8.</strong> Agents, code, and tools</li>
        <li><strong>9.</strong> Graphs, geometry, and representations</li>
        <li><strong>10.</strong> Generative modeling</li>
        <li><strong>11.</strong> Reinforcement learning and control</li>
        <li><strong>12.</strong> Robotics and world models</li>
      </ul>
    </div>
  </section>

  <section class="slide" data-kicker="Area sizes">
    <div class="slide-inner">
      <h2>The conference is broad—but not evenly distributed</h2>
      <div class="figure-wrap"><img src="{{AREA_FIGURE}}" alt="ICML 2026 taxonomy area sizes and visible GitHub share"></div>
      <p class="source">Source: current 12-area taxonomy. Area assignments still contain review boundaries.</p>
    </div>
  </section>

  <section class="slide" data-kicker="Six patterns">
    <div class="slide-inner">
      <h2>The conference story in six moves</h2>
      <div class="grid three">
        <div class="card"><h3>1. Reasoning after pretraining</h3><p>Rewards, verification, search, and extra work at answer time.</p></div>
        <div class="card"><h3>2. Systems and agents</h3><p>The model is only one part of a useful system.</p></div>
        <div class="card"><h3>3. Different attention signals</h3><p>Program selection and public visibility do not agree.</p></div>
        <div class="card"><h3>4. Robotics visibility</h3><p>A small area can attract very high public attention.</p></div>
        <div class="card"><h3>5. Venue context matters</h3><p>A large area can still be underweight versus other venues.</p></div>
        <div class="card"><h3>6. Links are not reproduction</h3><p>Visible artifacts are clues that still need inspection.</p></div>
      </div>
    </div>
  </section>

{{AREA_TECHNICAL_SLIDES}}

  <section class="slide" data-kicker="Trend 1">
    <div class="slide-inner split">
      <div>
        <p class="eyebrow">Reasoning and post-training</p>
        <div class="big-number">16.6%</div>
        <p class="lead">1,099 mapped papers—the largest current area.</p>
      </div>
      <div>
        <h2>Pretraining is no longer the whole story</h2>
        <ul class="plain-list">
          <li>Learn from rewards and preferences.</li>
          <li>Check intermediate work and final answers.</li>
          <li>Spend extra computing time on hard questions.</li>
          <li>Explore alternatives to left-to-right generation.</li>
        </ul>
        <div class="card tint-orange"><strong>Be careful:</strong> broad LLM training papers can be mistaken for reasoning papers.</div>
      </div>
    </div>
  </section>

  <section class="slide" data-kicker="Trend 2">
    <div class="slide-inner">
      <h2>The surrounding system is becoming central</h2>
      <div class="grid two">
        <div class="card tint-blue"><div class="big-number" style="font-size:70px">515</div><h3>Systems and efficient models</h3><p>Memory, serving, compression, caching, hardware, and end-to-end cost.</p></div>
        <div class="card tint-green"><div class="big-number" style="font-size:70px;color:var(--green)">496</div><h3>Agents, code, and tools</h3><p>Planning, execution, memory, tool environments, and software tasks.</p></div>
      </div>
      <p class="lead" style="margin-top:28px">Ask: did the model learn more—or did better scaffolding make the system look smarter?</p>
    </div>
  </section>

  <section class="slide" data-kicker="Trend 3">
    <div class="slide-inner">
      <h2>Program selection and public attention disagree</h2>
      <div class="figure-wrap"><img src="{{SIGNAL_FIGURE}}" alt="Oral enrichment compared with public attention enrichment"></div>
      <p class="source">Theory and safety lean toward program signal. Robotics and LLM reasoning lean toward public attention in this snapshot.</p>
    </div>
  </section>

  <section class="slide" data-kicker="Trend 3">
    <div class="slide-inner">
      <h2>Two areas that public attention can hide</h2>
      <div class="grid two">
        <div class="card tint-purple"><h3>Theory, optimization, and algorithms</h3><div class="statline"><div class="stat"><strong>1.45×</strong><span>oral enrichment</span></div><div class="stat"><strong>0.46×</strong><span>public attention</span></div></div><p>Mathematical depth may be harder to see in a fast public feed.</p></div>
        <div class="card tint-orange"><h3>Safety, governance, and society</h3><div class="statline"><div class="stat"><strong>1.41×</strong><span>oral enrichment</span></div><div class="stat"><strong>0.51×</strong><span>public attention</span></div></div><p>Technical safety contributions can matter without becoming popular demos.</p></div>
      </div>
      <p class="caption" style="margin-top:20px">Area enrichment helps choose what to read. It does not rank every paper.</p>
    </div>
  </section>

  <section class="slide" data-kicker="Trend 4">
    <div class="slide-inner split">
      <div>
        <p class="eyebrow">Robotics and world models</p>
        <div class="big-number">2.9%</div>
        <p class="lead">The smallest paper share among the 12 areas.</p>
      </div>
      <div>
        <div class="big-number" style="color:var(--orange)">2.11×</div>
        <p class="lead">The highest public-attention enrichment.</p>
        <div class="card tint-orange"><strong>A careful conclusion:</strong> robotics receives unusually high AlphaXiv attention for its size.</div>
        <div class="card unsafe" style="margin-top:14px"><strong>Not supported:</strong> robotics is the best or most important area.</div>
      </div>
    </div>
  </section>

  <section class="slide" data-kicker="Trend 5">
    <div class="slide-inner">
      <h2>Large inside ICML. Underweight versus nearby venues.</h2>
      <div class="figure-wrap"><img src="{{BASELINE_FIGURE}}" alt="ICML 2026 area share differences versus nearby venue baseline"></div>
      <p class="source">Multimodal and vision: 889 papers, 13.4% of ICML, yet about 3.1 percentage points below the project’s nearby-venue baseline.</p>
    </div>
  </section>

  <section class="slide" data-kicker="Trend 6">
    <div class="slide-inner">
      <h2>A repository link is the start of a question</h2>
      <div class="grid four">
        <div class="card"><h3>1. Identity</h3><p>Does the link belong to this paper?</p></div>
        <div class="card"><h3>2. Contents</h3><p>Are code, data, weights, and instructions present?</p></div>
        <div class="card"><h3>3. Execution</h3><p>Can it run in a clean environment?</p></div>
        <div class="card"><h3>4. Result</h3><p>Do the outputs match the paper?</p></div>
      </div>
      <p class="quote" style="margin-top:34px">Visible ≠ runnable ≠ reproduced.</p>
    </div>
  </section>

  <section class="slide" data-kicker="Paper reading">
    <div class="slide-inner">
      <h2>Read every paper through five questions</h2>
      <div class="grid three">
        <div class="card tint-blue"><h3>1. Problem</h3><p>What is the paper trying to change or understand?</p></div>
        <div class="card tint-green"><h3>2. Contribution</h3><p>What does it add?</p></div>
        <div class="card tint-orange"><h3>3. Evidence</h3><p>What supports the claim?</p></div>
        <div class="card tint-purple"><h3>4. Limit</h3><p>Where might the conclusion fail?</p></div>
        <div class="card"><h3>5. Wider meaning</h3><p>Why does it matter for the conference map?</p></div>
      </div>
    </div>
  </section>

  <section class="slide" data-kicker="Paper examples">
    <div class="slide-inner">
      <h2>Four papers that make the map concrete</h2>
      <div class="grid two">
        <div class="card"><span class="label">Reasoning</span><div class="paper-title">The Flexibility Trap</div><p>Tests whether flexible generation order actually helps diffusion language-model reasoning.</p></div>
        <div class="card"><span class="label">Theory</span><div class="paper-title">To Grok Grokking</div><p>Explains delayed generalization in a controlled mathematical setting.</p></div>
        <div class="card"><span class="label">Agents</span><div class="paper-title">PaperBanana</div><p>Uses an agentic workflow for academic illustrations—and leaves artifact questions to check.</p></div>
        <div class="card"><span class="label">Safety</span><div class="paper-title">The Obfuscation Atlas</div><p>Asks whether training against deception monitors creates honesty or better hiding.</p></div>
      </div>
    </div>
  </section>

  <section class="slide" data-kicker="Boundaries">
    <div class="slide-inner split">
      <div>
        <h2>A useful map has borders, not walls</h2>
        <p class="lead">A paper may be evidence for more than one story.</p>
        <div class="card tint-orange"><strong>Example:</strong> Neural Thickets can be read as efficient adaptation, optimization, or post-training.</div>
      </div>
      <div class="figure-wrap"><img src="{{SEMANTIC_FIGURE}}" alt="Semantic map of ICML 2026 papers"></div>
    </div>
  </section>

  <section class="slide" data-kicker="Tensions">
    <div class="slide-inner">
      <h2>Trends contain disagreements</h2>
      <div class="grid three">
        <div class="card"><h3>Scores ↔ reliability</h3><p>Does a better benchmark score mean more dependable reasoning?</p></div>
        <div class="card"><h3>Capability ↔ cost</h3><p>What ability is lost when a model becomes faster or smaller?</p></div>
        <div class="card"><h3>Agents ↔ safety</h3><p>What happens when a capable tool user makes a mistake?</p></div>
        <div class="card"><h3>Demos ↔ evaluation</h3><p>Does a striking example survive repeated and realistic tests?</p></div>
        <div class="card"><h3>Benchmarks ↔ use</h3><p>Does measured success matter in the real scientific or social setting?</p></div>
        <div class="card"><h3>Links ↔ reproduction</h3><p>Can another person actually run and check the result?</p></div>
      </div>
    </div>
  </section>

  <section class="slide" data-kicker="Knowledge check">
    <div class="slide-inner">
      <h2>Check 1: What can we conclude?</h2>
      <p class="lead">Robotics has 2.9% of mapped papers and 2.11× public-attention enrichment.</p>
      <div class="grid two">
        <div class="card safe"><h3>A</h3><p>Robotics receives unusually high AlphaXiv attention for its size.</p></div>
        <div class="card unsafe"><h3>B</h3><p>Robotics is the highest-quality research area at ICML.</p></div>
      </div>
      <button class="reveal" data-answer="answer1" style="margin-top:22px">Reveal answer</button>
      <div class="answer" id="answer1"><strong>A is supported.</strong> B changes a platform-attention signal into a quality claim.</div>
    </div>
  </section>

  <section class="slide" data-kicker="Knowledge check">
    <div class="slide-inner">
      <h2>Check 2: A GitHub link has many stars</h2>
      <p class="lead">What should you do before calling the paper reproducible?</p>
      <div class="grid two">
        <div class="card"><h3>Minimum answer</h3><p>Confirm the repository belongs to the paper and contains the promised materials.</p></div>
        <div class="card"><h3>Strong answer</h3><p>Run it cleanly, compare outputs, and document missing steps or differences.</p></div>
      </div>
      <button class="reveal" data-answer="answer2" style="margin-top:22px">Reveal principle</button>
      <div class="answer" id="answer2"><strong>Stars show attention, not reproduction.</strong> Identity, contents, execution, and results all need checks.</div>
    </div>
  </section>

  <section class="slide" data-kicker="Your turn">
    <div class="slide-inner">
      <h2>Build a five-minute ICML 2026 briefing</h2>
      <div class="grid two">
        <div class="card tint-blue"><h3>Include</h3><ul class="plain-list"><li>One sentence about the map</li><li>Three major trends</li><li>One contrast between signals</li><li>Two paper examples</li></ul></div>
        <div class="card tint-orange"><h3>Protect against overclaiming</h3><ul class="plain-list"><li>Two important caveats</li><li>One open question</li><li>Signal names where they matter</li><li>No link-as-reproduction claim</li></ul></div>
      </div>
    </div>
  </section>

  <section class="slide" data-kicker="Learning route">
    <div class="slide-inner">
      <h2>Choose your next step</h2>
      <div class="grid three">
        <div class="card tint-blue"><span class="label">3–4 hours</span><h3>Quick tour</h3><p>Map, four trends, four papers, and a short briefing.</p></div>
        <div class="card tint-green"><span class="label">10–12 hours</span><h3>Standard route</h3><p>All lessons, 12-paper course, checkpoints, and final quiz.</p></div>
        <div class="card tint-orange"><span class="label">About 20 hours</span><h3>Deep route</h3><p>Full papers, artifact inspection, venue comparison, and written synthesis.</p></div>
      </div>
      <p class="lead" style="margin-top:30px">The goal is not to finish quickly. It is to leave with a reliable way to understand new research.</p>
    </div>
  </section>

  <section class="slide" data-kicker="Start here">
    <div class="slide-inner">
      <p class="eyebrow">The map is ready</p>
      <h1>Now explore<br>with good questions.</h1>
      <div class="end-links card" style="margin-top:28px">
        <h3>Inside the workspace</h3>
        <p><a href="icml2026_newcomer_roadmap.md">Full newcomer roadmap</a></p>
        <p><a href="../reports/icml2026_newcomer_final_quiz.md">100-point final quiz</a></p>
        <p><a href="dashboard.html">Interactive landscape dashboard</a></p>
      </div>
      <p class="caption" style="margin-top:20px">This HTML file contains all slide text, styles, scripts, and figures. External links are optional.</p>
    </div>
  </section>
</main>

<nav class="controls" aria-label="Slide controls">
  <button id="prev" title="Previous slide" aria-label="Previous slide">←</button>
  <button id="next" title="Next slide" aria-label="Next slide">→</button>
  <span class="counter" id="counter">1 / 47</span>
  <div class="progress" aria-hidden="true"><span id="progress"></span></div>
  <span class="help">O overview · F full screen · P print</span>
</nav>

<script>
(() => {
  const slides = [...document.querySelectorAll('.slide')];
  const counter = document.getElementById('counter');
  const progress = document.getElementById('progress');
  let index = Math.max(0, Math.min(slides.length - 1, Number(location.hash.slice(1)) - 1 || 0));
  let overview = false;

  function show(nextIndex) {
    index = Math.max(0, Math.min(slides.length - 1, nextIndex));
    slides.forEach((slide, i) => slide.classList.toggle('active', i === index));
    counter.textContent = `${index + 1} / ${slides.length}`;
    progress.style.width = `${((index + 1) / slides.length) * 100}%`;
    history.replaceState(null, '', `#${index + 1}`);
  }

  function toggleOverview() {
    overview = !overview;
    document.body.classList.toggle('overview', overview);
    if (!overview) show(index);
  }

  document.getElementById('prev').addEventListener('click', () => show(index - 1));
  document.getElementById('next').addEventListener('click', () => show(index + 1));
  document.querySelectorAll('.reveal').forEach(button => button.addEventListener('click', () => {
    document.getElementById(button.dataset.answer).classList.toggle('visible');
  }));
  slides.forEach((slide, i) => slide.addEventListener('click', () => {
    if (overview) { toggleOverview(); show(i); }
  }));
  document.addEventListener('keydown', event => {
    if (['ArrowRight', 'PageDown', ' '].includes(event.key)) { event.preventDefault(); show(index + 1); }
    if (['ArrowLeft', 'PageUp'].includes(event.key)) { event.preventDefault(); show(index - 1); }
    if (event.key === 'Home') show(0);
    if (event.key === 'End') show(slides.length - 1);
    if (event.key.toLowerCase() === 'o') toggleOverview();
    if (event.key.toLowerCase() === 'f') document.documentElement.requestFullscreen?.();
    if (event.key.toLowerCase() === 'p') window.print();
  });
  let touchStart = null;
  document.addEventListener('touchstart', event => { touchStart = event.changedTouches[0].clientX; }, {passive: true});
  document.addEventListener('touchend', event => {
    if (touchStart === null) return;
    const delta = event.changedTouches[0].clientX - touchStart;
    if (Math.abs(delta) > 55) show(index + (delta < 0 ? 1 : -1));
    touchStart = null;
  }, {passive: true});
  show(index);
})();
</script>
</body>
</html>'''
    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)
    return html


def main() -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    path = DOCS / "icml2026_newcomer_slides.html"
    path.write_text(build_html(), encoding="utf-8")
    print(f"Wrote {path} ({path.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
