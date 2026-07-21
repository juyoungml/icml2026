# Agents, Code, and Tool Use

Agents are shifting from impressive demos toward evaluation harnesses, tool environments, and software/security tasks.

## Signal Snapshot

- Papers: 496 (7.5% of corpus)
- Oral enrichment: 1.19x
- Public-attention enrichment: 1.52x
- Historical accepted-paper delta: +2.1 pp
- GitHub URL share: 32.9%
- Manual area-review progress: 0/16 rows reviewed; 16 remaining
- Trust tier: `high_review_need` - 2 taxonomy clusters need review; historical baseline contrast is material; 30 low-confidence evidence-code rows in full area

## Fault Lines

- Better scaffolding and prompting versus actual learned agent capability.
- Static benchmarks versus dynamic environments with hidden state, long horizons, and recovery from failure.
- Code and security agents as practical systems versus brittle benchmark optimizers.

## Read For

- Does the environment prevent leakage and reward shortcut behavior?
- Is improvement coming from model training, search, memory, tools, or evaluation-loop design?
- Are failures categorized by planning, perception, tool use, memory, or execution?

## Shape Of The Area

- Top subareas: Agent evaluation, tool use, and agentic workflows (207); Multi-agent search, planning, and coordination (150); Code LLMs, verification, and software tasks (139)
- Method-family cues: Agents / tool use (412); Reasoning / test-time compute (271); RL / policy optimization (150); LLM post-training (100); Graphs / geometry (63); Diffusion / flow (41); Compression / efficiency (35); Transformer / attention (24)
- Evaluation-setting cues: language/llm (414); math/code/verifiable (213); theory/synthetic (90); robotics/embodied (79); security/safety (43); vision/video (30); science/domain (15)
- Contribution mix: Benchmark / evaluation (276); Position / conceptual (55); Method / algorithm (48); Dataset / data resource (41); Theory / proof (35); System / infrastructure (27); Application / domain study (7); Uncoded (7)
- Evidence confidence: medium (466); low (30)

## Start Here

- $\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment (oral; votes=89; github_stars=1569)
- Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning (oral; votes=89; github_stars=1228)
- daVinci-Dev: Agent-native Mid-training for Software Engineering (oral; votes=52; github_stars=9)
- Monitoring Monitorability (oral; votes=28; github_stars=2786)
- Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections (oral; votes=26; github_stars=1)
- CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability (oral; votes=21; github_stars=139)

## Public Attention Not Program-Selected

- Learning to Discover at Test Time (votes=529; github_stars=297; taxonomy-review)
- PaperBanana: Automating Academic Illustration for AI Scientists (votes=420; github_stars=6765)
- ToolOrchestra: Elevating Intelligence via Efficient Model and Tool Orchestration (votes=260; github_stars=745)
- MemEvolve: Meta-Evolution of Agent Memory Systems (votes=194; github_stars=253; taxonomy-review)
- Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning (votes=184; github_stars=408)
- Scaling Long-Horizon Agent via Context Folding (votes=171; github_stars=172; taxonomy-review)

## Artifact-Visible Papers To Inspect

- PaperBanana: Automating Academic Illustration for AI Scientists (votes=420; github_stars=6765)
- DeepAnalyze: Agentic Large Language Models for Autonomous Data Science (votes=146; github_stars=4355)
- Monitoring Monitorability (oral; votes=28; github_stars=2786)
- $\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment (oral; votes=89; github_stars=1569)
- $\tau$-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge (votes=13; github_stars=1569)
- $\tau$-Voice: Benchmarking Full-Duplex Voice Agents on Real-World Domains (votes=23; github_stars=1556)

## Boundary / Taxonomy Review Candidates

- Learning to Discover at Test Time (votes=529; github_stars=297; taxonomy-review)
- MemEvolve: Meta-Evolution of Agent Memory Systems (votes=194; github_stars=253; taxonomy-review)
- Scaling Long-Horizon Agent via Context Folding (votes=171; github_stars=172; taxonomy-review)
- Meta Context Engineering via Agentic Skill Evolution (votes=132; github_stars=135; taxonomy-review)
- Evolution Strategies at Scale: LLM Fine-Tuning Beyond Reinforcement Learning (votes=126; github_stars=368; taxonomy-review)
- Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning (votes=112; github_stars=580; taxonomy-review)

## What Could Break This Area Story

- The area taxonomy is generated from semantic clusters and curated mappings, not full manual paper reading.
- Public attention is AlphaXiv attention; it can reflect sharing dynamics rather than technical importance.
- GitHub URL share is artifact visibility, not runnable reproducibility.
- Evidence-code labels are heuristic and should be checked against the paper before making benchmark, dataset, metric, or result-character claims.