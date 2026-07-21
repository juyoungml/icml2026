#!/usr/bin/env python3
"""Title-level EDA for the ICML 2026 paper corpus."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "by", "can", "for", "from", "in", "is", "it",
    "of", "on", "or", "the", "to", "via", "with", "without", "towards", "toward",
    "using", "through", "under", "over", "between", "beyond", "into", "its", "their",
}

TOPIC_RULES = {
    "LLMs / language / agents": [
        "llm", "llms", "language model", "large language", "reasoning", "agent", "agents",
        "chain-of-thought", "cot", "prompt", "token", "alignment", "reward model",
    ],
    "Diffusion / generative models": [
        "diffusion", "generative", "generation", "video generation", "flow matching",
        "score-based", "denoising",
    ],
    "Reinforcement learning": [
        "reinforcement learning", "policy", "rl", "markov decision", "ppo", "grpo", "reward",
        "offline goal", "bandit",
    ],
    "Theory / optimization / statistics": [
        "theorem", "provable", "optimal", "optimization", "convex", "regret", "bound",
        "sampling", "bayesian", "matrix", "gradient", "generalization",
    ],
    "Causality": ["causal", "causality", "intervention", "confounder"],
    "Privacy / fairness / safety": [
        "privacy", "private", "fairness", "safe", "safety", "robust", "robustness",
        "bias", "risk", "deception", "deepfake", "non-consensual",
    ],
    "Multimodal / vision / video": [
        "multimodal", "multi-modal", "vision", "video", "image", "visual", "speech",
        "3d", "segmentation", "detection",
    ],
    "Systems / efficiency / compression": [
        "efficient", "efficiency", "compression", "quantization", "sparse", "inference",
        "hardware", "accelerated", "moe", "adapter", "lora",
    ],
    "AI for science / health": [
        "protein", "molecule", "drug", "health", "medical", "biophysical", "neural data",
        "antibody", "physiological", "neuro",
    ],
}


def load_rows() -> list[dict[str, str]]:
    path = PROCESSED / "icml2026_papers.csv"
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def tokenize(title: str) -> list[str]:
    title = title.lower()
    title = re.sub(r"[^a-z0-9$+\- ]+", " ", title)
    return [tok for tok in title.split() if len(tok) > 2 and tok not in STOPWORDS]


def topic_hits(title: str) -> list[str]:
    lower = title.lower()
    hits = []
    for topic, needles in TOPIC_RULES.items():
        if any(needle in lower for needle in needles):
            hits.append(topic)
    return hits or ["Unbucketed / other"]


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    rows = load_rows()
    token_counts = Counter()
    bigram_counts = Counter()
    topic_counts = Counter()
    topic_examples: dict[str, list[str]] = defaultdict(list)

    for row in rows:
        tokens = tokenize(row["title"])
        token_counts.update(tokens)
        bigram_counts.update(" ".join(pair) for pair in zip(tokens, tokens[1:]))
        for topic in topic_hits(row["title"]):
            topic_counts[topic] += 1
            if len(topic_examples[topic]) < 5:
                topic_examples[topic].append(row["title"])

    keyword_rows = [
        {"term": term, "count": count, "kind": "unigram"}
        for term, count in token_counts.most_common(100)
    ] + [
        {"term": term, "count": count, "kind": "bigram"}
        for term, count in bigram_counts.most_common(100)
    ]
    topic_rows = [
        {
            "topic": topic,
            "count": count,
            "share": round(count / len(rows), 4),
        }
        for topic, count in topic_counts.most_common()
    ]

    write_csv(PROCESSED / "icml2026_keyword_counts.csv", keyword_rows, ["term", "count", "kind"])
    write_csv(PROCESSED / "icml2026_topic_counts.csv", topic_rows, ["topic", "count", "share"])

    event_type_counts = Counter(row["event_type"] for row in rows)
    position_count = sum(row["is_position"] == "true" for row in rows)
    oral_count = sum(row.get("is_oral") == "true" for row in rows)
    oral_topic_counts = Counter()
    for row in rows:
        if row.get("is_oral") == "true":
            oral_topic_counts.update(topic_hits(row["title"]))

    report_lines = [
        "# ICML 2026 Title-Level EDA",
        "",
        "This is an initial exploratory pass over the official ICML virtual `papers.html` corpus.",
        "",
        "## Corpus",
        "",
        f"- Rows parsed: {len(rows):,}",
        f"- Posters: {event_type_counts.get('poster', 0):,}",
        f"- Oral-designated papers matched by title: {oral_count:,}",
        f"- Position-prefixed titles: {position_count:,}",
        "",
        "Note: the official `papers.html` fallback lists paper pages as poster links. Oral designations are joined from the separate official oral-events page by normalized title.",
        "",
        "## Top Title Terms",
        "",
    ]
    for term, count in token_counts.most_common(25):
        report_lines.append(f"- `{term}`: {count}")

    report_lines.extend(["", "## Top Title Bigrams", ""])
    for term, count in bigram_counts.most_common(25):
        report_lines.append(f"- `{term}`: {count}")

    report_lines.extend(["", "## Topic Buckets", ""])
    for row in topic_rows:
        pct = row["share"] * 100
        report_lines.append(f"- {row['topic']}: {row['count']:,} ({pct:.1f}%)")

    report_lines.extend(["", "## Oral-Designated Topic Buckets", ""])
    for topic, count in oral_topic_counts.most_common():
        pct = count / oral_count * 100 if oral_count else 0
        report_lines.append(f"- {topic}: {count:,} ({pct:.1f}%)")

    report_lines.extend(["", "## Example Titles by Topic", ""])
    for topic, examples in topic_examples.items():
        report_lines.append(f"### {topic}")
        for title in examples:
            report_lines.append(f"- {title}")
        report_lines.append("")

    report_lines.extend(
        [
            "## Interpretation Seeds",
            "",
            "- Title-level evidence should be treated as directional; abstracts are needed for a stronger topic model.",
            "- LLM, reasoning, reward, agent, and alignment terms should be compared against non-title metadata because titles often understate application area.",
            "- Position papers can be isolated by the `Position:` prefix for governance and policy-theme analysis.",
            "- Award papers over-index on diffusion, theory/sampling, safety/alignment, memorization, video attribution, and grokking.",
        ]
    )

    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "icml2026_title_eda.md").write_text("\n".join(report_lines), encoding="utf-8")
    (PROCESSED / "icml2026_topic_examples.json").write_text(
        json.dumps(topic_examples, indent=2), encoding="utf-8"
    )

    print(f"Analyzed {len(rows)} title rows")
    print(f"Wrote {REPORTS / 'icml2026_title_eda.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
