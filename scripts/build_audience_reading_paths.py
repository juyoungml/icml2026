#!/usr/bin/env python3
"""Build audience-specific ICML 2026 reading paths."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"


AUDIENCES = [
    {
        "audience": "LLM Reasoning Researcher",
        "why": "Track test-time compute, process rewards, reasoning data, and evaluation around large language models.",
        "themes": ["LLM reasoning and test-time compute", "RL for LLMs and verifiable rewards"],
        "clusters": ["1", "6", "13", "24"],
        "topics": ["Large Language Models", "Foundation Models"],
        "keywords": [
            "reasoning", "test-time", "test time", "process reward", "verifiable",
            "rubric", "chain-of-thought", "cot", "policy optimization", "grpo",
        ],
    },
    {
        "audience": "RL Researcher",
        "why": "Separate classical RL, RLVR/post-training, preference optimization, and control-oriented work.",
        "themes": ["RL for LLMs and verifiable rewards", "Theory, optimization, and sampling"],
        "clusters": ["7", "6", "24", "9"],
        "topics": ["Reinforcement Learning"],
        "keywords": [
            "reinforcement learning", "policy", "offline rl", "reward", "value function",
            "bandit", "regret", "inverse reinforcement", "preference optimization",
        ],
    },
    {
        "audience": "Agents and Tool-Use Researcher",
        "why": "Focus on agents, software tasks, GUI/mobile/web use, multi-agent systems, and evaluation harnesses.",
        "themes": ["Agents, tools, and computer use", "Memorization, evaluation, and generalization"],
        "clusters": ["11", "20", "13", "1"],
        "topics": ["Large Language Models", "Everything Else"],
        "keywords": [
            "agent", "agents", "tool", "software engineering", "gui", "mobile",
            "web", "multi-agent", "environment", "benchmark", "task",
        ],
    },
    {
        "audience": "Systems and Efficiency Builder",
        "why": "Prioritize inference, long context, quantization, KV cache, attention, LoRA, and scalable training.",
        "themes": ["Systems, efficiency, and compression", "LLM reasoning and test-time compute"],
        "clusters": ["21", "14", "12", "13"],
        "topics": ["Large Scale", "Hardware and Software", "Attention Mechanisms"],
        "keywords": [
            "quantization", "kv", "cache", "inference", "decoding", "attention",
            "lora", "fine-tuning", "serving", "memory", "compression", "long context",
        ],
    },
    {
        "audience": "Diffusion and Generative Modeling Researcher",
        "why": "Connect diffusion language models, video/image generation, flow matching, and sampling theory.",
        "themes": ["Diffusion, flow, and generative modeling", "Diffusion language models"],
        "clusters": ["3", "0", "13", "9"],
        "topics": ["Generative Models", "Monte Carlo", "Computer Vision"],
        "keywords": [
            "diffusion", "flow matching", "score", "sampling", "denoising",
            "video generation", "image generation", "masked", "arbitrary order",
        ],
    },
    {
        "audience": "Multimodal and Robotics Researcher",
        "why": "Cover VLMs, video, 3D, VLA/action policies, embodied agents, and robotics benchmarks.",
        "themes": ["Multimodal, vision-language, and video", "Robotics and world models"],
        "clusters": ["4", "19", "10", "0"],
        "topics": ["Computer Vision", "Robotics"],
        "keywords": [
            "vision-language", "multimodal", "video", "3d", "robot", "robotics",
            "vla", "action", "world model", "embodied", "manipulation",
        ],
    },
    {
        "audience": "Safety, Alignment, and Governance Researcher",
        "why": "Track alignment, jailbreaks, privacy, fairness, interpretability, risk, and position papers.",
        "themes": ["Safety, alignment, governance, and risk", "Interpretability and mechanistic analysis"],
        "clusters": ["2", "23", "28", "1"],
        "topics": ["Social Aspects", "Alignment", "Safety", "Privacy", "Fairness"],
        "keywords": [
            "safety", "alignment", "jailbreak", "deception", "privacy", "fairness",
            "risk", "governance", "interpretability", "transparency", "accountability",
        ],
    },
    {
        "audience": "Theory and Optimization Researcher",
        "why": "Highlight learning theory, optimization, regret, sampling, gradients, and provable guarantees.",
        "themes": ["Theory, optimization, and sampling"],
        "clusters": ["9", "22", "16", "17"],
        "topics": ["Theory", "Optimization", "Probabilistic Methods"],
        "keywords": [
            "theory", "provable", "bound", "convergence", "optimization", "gradient",
            "regret", "bandit", "sampling", "monte carlo", "convex",
        ],
    },
    {
        "audience": "AI for Science Researcher",
        "why": "Find science, biology, chemistry, physics, health, PDE/operator learning, and scientific foundation model work.",
        "themes": ["AI for science, health, and biology"],
        "clusters": ["15", "16", "27", "18"],
        "topics": ["Chemistry", "Physics", "Earth Sciences", "Health", "Neuroscience"],
        "keywords": [
            "protein", "molecule", "chemistry", "physics", "pde", "operator",
            "health", "medical", "biology", "genomic", "neuroscience", "time series",
        ],
    },
    {
        "audience": "Executive / Broad Landscape Reader",
        "why": "A compact path through award, oral, public-attention, and field-balance signals.",
        "max_per_cluster": 3,
        "award_bonus": 8.0,
        "oral_bonus": 2.0,
        "themes": [
            "LLM reasoning and test-time compute",
            "Diffusion, flow, and generative modeling",
            "Safety, alignment, governance, and risk",
            "Systems, efficiency, and compression",
        ],
        "clusters": ["6", "13", "11", "3", "28", "21"],
        "topics": ["Deep Learning", "Social Aspects", "Applications", "Theory"],
        "keywords": [
            "reasoning", "diffusion", "agent", "safety", "alignment", "inference",
            "benchmark", "position", "scaling", "language model",
        ],
    },
]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"Missing required input: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def normalize_title(title: str) -> str:
    title = title.lower()
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def split_values(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def intish(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def floatish(value: str) -> float:
    try:
        return float(value or 0)
    except ValueError:
        return 0.0


def keyword_hits(text: str, keywords: list[str]) -> list[str]:
    lower = text.lower()
    return [keyword for keyword in keywords if keyword.lower() in lower]


def rank_paper(row: dict[str, str], audience: dict[str, object], max_votes: int, max_recent: int, max_stars: int) -> tuple[float, list[str]]:
    reasons = []
    score = 0.0
    themes = set(split_values(row.get("themes", "")))
    wanted_themes = set(audience["themes"])
    theme_overlap = sorted(themes & wanted_themes)
    if theme_overlap:
        score += 2.0 * len(theme_overlap)
        reasons.append("theme: " + ", ".join(theme_overlap[:3]))

    if row.get("cluster_id") in set(audience["clusters"]):
        score += 1.6
        reasons.append(f"cluster: {row.get('cluster_id')} {row.get('cluster_label')}")

    topic_text = " ".join([row.get("official_topic", ""), row.get("topic_group", ""), row.get("topic", "")]).lower()
    topic_hits = [topic for topic in audience["topics"] if topic.lower() in topic_text]
    if topic_hits:
        score += 1.0
        reasons.append("topic: " + ", ".join(topic_hits[:2]))

    hits = keyword_hits(" ".join([row.get("title", ""), row.get("abstract", "")]), audience["keywords"])
    if hits:
        score += min(1.5, 0.35 * len(hits))
        reasons.append("keywords: " + ", ".join(hits[:4]))

    if row.get("award"):
        score += float(audience.get("award_bonus", 2.5))
        reasons.append("official award")
    if row.get("is_oral") == "true":
        score += float(audience.get("oral_bonus", 1.0))
        reasons.append("oral")

    votes = intish(row.get("public_total_votes", "0"))
    recent = intish(row.get("visits_last_7_days", "0"))
    stars = intish(row.get("github_stars", "0"))
    if max_votes:
        score += 1.2 * (votes / max_votes)
    if max_recent:
        score += 0.7 * (recent / max_recent)
    if max_stars:
        score += 0.4 * (stars / max_stars)

    score += 0.4 * floatish(row.get("cluster_centrality", "0"))
    return score, reasons


def phase_for_rank(rank: int) -> str:
    if rank <= 5:
        return "start_here"
    if rank <= 12:
        return "core_depth"
    if rank <= 18:
        return "adjacent_context"
    return "optional_deep_cut"


def main() -> int:
    theme_rows = read_csv(PROCESSED / "icml2026_theme_matrix.csv")
    cluster_rows = read_csv(PROCESSED / "icml2026_cluster_assignments.csv")
    alpha_rows = read_csv(PROCESSED / "alphaxiv_icml2026_joined.csv")
    collab_rows = read_csv(PROCESSED / "icml2026_paper_collaboration_features.csv")

    cluster_by_title = {normalize_title(row["title"]): row for row in cluster_rows}
    alpha_by_title = {normalize_title(row["title"]): row for row in alpha_rows}
    collab_by_title = {normalize_title(row["title"]): row for row in collab_rows}

    merged = []
    for row in theme_rows:
        key = normalize_title(row["title"])
        cluster = cluster_by_title.get(key, {})
        alpha = alpha_by_title.get(key, {})
        collab = collab_by_title.get(key, {})
        merged.append(
            {
                **row,
                "cluster_id": cluster.get("cluster_id", ""),
                "cluster_label": cluster.get("cluster_label", ""),
                "cluster_centrality": cluster.get("cluster_centrality", "0"),
                "abstract": alpha.get("abstract", ""),
                "authors": alpha.get("authors", collab.get("authors", "")),
                "organizations": alpha.get("organizations", ""),
                "github_url": alpha.get("github_url", ""),
                "sector_mix": collab.get("sector_mix", ""),
                "canonical_institutions": collab.get("canonical_institutions", ""),
            }
        )

    max_votes = max([intish(row.get("public_total_votes", "0")) for row in merged] or [1])
    max_recent = max([intish(row.get("visits_last_7_days", "0")) for row in merged] or [1])
    max_stars = max([intish(row.get("github_stars", "0")) for row in merged] or [1])

    output_rows = []
    for audience in AUDIENCES:
        scored = []
        for row in merged:
            score, reasons = rank_paper(row, audience, max_votes, max_recent, max_stars)
            if score >= 1.5:
                scored.append((score, reasons, row))
        scored.sort(
            key=lambda item: (
                item[0],
                bool(item[2].get("award")),
                item[2].get("is_oral") == "true",
                intish(item[2].get("public_total_votes", "0")),
                intish(item[2].get("visits_last_7_days", "0")),
            ),
            reverse=True,
        )

        seen_titles = set()
        cluster_counts = Counter()
        max_per_cluster = int(audience.get("max_per_cluster", 8))
        selected = []
        for score, reasons, row in scored:
            title_key = normalize_title(row["title"])
            if title_key in seen_titles:
                continue
            cluster_id = row.get("cluster_id", "")
            if cluster_id and cluster_counts[cluster_id] >= max_per_cluster:
                continue
            seen_titles.add(title_key)
            if cluster_id:
                cluster_counts[cluster_id] += 1
            selected.append((score, reasons, row))
            if len(selected) == 25:
                break

        for rank, (score, reasons, row) in enumerate(selected, start=1):
            output_rows.append(
                {
                    "audience": audience["audience"],
                    "phase": phase_for_rank(rank),
                    "rank": rank,
                    "title": row["title"],
                    "why_read": "; ".join(reasons[:5]),
                    "award": row.get("award", ""),
                    "is_oral": row.get("is_oral", ""),
                    "public_total_votes": row.get("public_total_votes", "0"),
                    "visits_last_7_days": row.get("visits_last_7_days", "0"),
                    "github_stars": row.get("github_stars", "0"),
                    "reading_score": round(score, 4),
                    "themes": row.get("themes", ""),
                    "cluster_id": row.get("cluster_id", ""),
                    "cluster_label": row.get("cluster_label", ""),
                    "official_topic": row.get("official_topic", ""),
                    "sector_mix": row.get("sector_mix", ""),
                    "authors": row.get("authors", ""),
                    "canonical_institutions": row.get("canonical_institutions", ""),
                    "url": row.get("url", ""),
                    "alphaxiv_url": row.get("alphaxiv_url", ""),
                    "github_url": row.get("github_url", ""),
                }
            )

    write_csv(
        PROCESSED / "icml2026_audience_reading_paths.csv",
        output_rows,
        [
            "audience", "phase", "rank", "title", "why_read", "award", "is_oral",
            "public_total_votes", "visits_last_7_days", "github_stars", "reading_score",
            "themes", "cluster_id", "cluster_label", "official_topic", "sector_mix",
            "authors", "canonical_institutions", "url", "alphaxiv_url", "github_url",
        ],
    )

    lines = [
        "# ICML 2026 Audience Reading Paths",
        "",
        "This report turns the ICML 2026 EDA into practical reading tracks for different researcher goals.",
        "Each path is ranked by explicit audience relevance plus official awards/orals, AlphaXiv attention, GitHub stars, and cluster centrality.",
        "",
        "Phases: `start_here` = first five papers; `core_depth` = next seven; `adjacent_context` = next six; `optional_deep_cut` = remaining suggestions.",
        "",
    ]
    by_audience = {audience["audience"]: [] for audience in AUDIENCES}
    for row in output_rows:
        by_audience[row["audience"]].append(row)

    for audience in AUDIENCES:
        name = audience["audience"]
        rows = by_audience[name]
        phase_counts = Counter(row["phase"] for row in rows)
        lines.extend([f"## {name}", "", audience["why"], ""])
        lines.append(
            "Track size: "
            + ", ".join(f"{phase} {phase_counts[phase]}" for phase in ["start_here", "core_depth", "adjacent_context", "optional_deep_cut"])
            + "."
        )
        current_phase = None
        for row in rows:
            if row["phase"] != current_phase:
                current_phase = row["phase"]
                lines.extend(["", f"### {current_phase}", ""])
            flags = [flag for flag in [row["award"], "oral" if row["is_oral"] == "true" else ""] if flag]
            flag_text = f" ({'; '.join(flags)})" if flags else ""
            lines.append(
                f"{row['rank']}. {row['title']}{flag_text} - "
                f"score {row['reading_score']}; votes {row['public_total_votes']}; "
                f"cluster {row['cluster_id']}: {row['cluster_label']}"
            )
            lines.append(f"   - Why: {row['why_read']}")
        lines.append("")

    lines.extend(
        [
            "## Caveats",
            "",
            "- These tracks are generated heuristically and should be manually edited before becoming a final syllabus or slide narrative.",
            "- AlphaXiv public signal is not a quality label; it is used only as one prioritization input.",
            "- Papers can appear in multiple tracks because ICML 2026 work often spans method, application, and evaluation categories.",
            "- The ranking favors relevance and signal, not comprehensive coverage of every subtopic.",
        ]
    )
    report_path = REPORTS / "icml2026_audience_reading_paths.md"
    REPORTS.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {PROCESSED / 'icml2026_audience_reading_paths.csv'}")
    print(f"Wrote {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
