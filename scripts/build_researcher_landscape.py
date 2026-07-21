#!/usr/bin/env python3
"""Build researcher-facing ICML 2026 landscape report."""

from __future__ import annotations

import csv
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"


THEMES = {
    "LLM reasoning and test-time compute": [
        "reasoning", "chain-of-thought", "cot", "test-time", "test time", "verifier",
        "process reward", "large reasoning", "math", "aime", "thinking",
    ],
    "RL for LLMs and verifiable rewards": [
        "rlvr", "verifiable reward", "reinforcement learning", "grpo", "ppo", "policy optimization",
        "reward model", "reward-guided", "post-training", "preference optimization",
    ],
    "Agents, tools, and computer use": [
        "agent", "agents", "tool use", "tools", "computer-use", "gui", "web agent",
        "terminal", "software engineering", "planning",
    ],
    "Diffusion language models": [
        "diffusion language", "dllm", "unmasking", "block diffusion", "discrete diffusion",
        "arbitrary order", "mask",
    ],
    "Diffusion, flow, and generative modeling": [
        "diffusion", "flow matching", "score-based", "denoising", "generative model",
        "video generation", "image generation", "sampling",
    ],
    "Multimodal, vision-language, and video": [
        "multimodal", "multi-modal", "vision-language", "vlm", "mllm", "video",
        "visual", "image", "3d", "perception",
    ],
    "Interpretability and mechanistic analysis": [
        "interpretability", "interpretable", "mechanistic", "circuit", "probe", "probing",
        "explain", "explanation", "transparency", "activation",
    ],
    "Memorization, evaluation, and generalization": [
        "memorize", "memorization", "generalization", "evaluation", "benchmark", "benchmarking",
        "regurgitation", "contamination",
    ],
    "Safety, alignment, governance, and risk": [
        "safety", "alignment", "risk", "deception", "red-team", "jailbreak", "robustness",
        "deepfake", "misuse", "governance", "bias", "fairness", "privacy", "security",
    ],
    "AI for science, health, and biology": [
        "protein", "molecule", "chemistry", "physics", "health", "medicine", "medical",
        "biology", "genomic", "antibody", "neuro", "scientific",
    ],
    "Theory, optimization, and sampling": [
        "theory", "provable", "bound", "convergence", "convex", "optimization",
        "sampling", "random matrix", "bayesian", "monte carlo", "regret",
    ],
    "Systems, efficiency, and compression": [
        "efficient inference", "efficient training", "efficiency", "compression", "quantization",
        "kv-cache", "cache compression", "sparse attention", "hardware", "moe", "lora",
        "adapter", "serving", "memory-efficient",
    ],
    "Causality and data-centric ML": [
        "causal", "causality", "intervention", "confound", "data selection", "data attribution",
        "data value", "dataset distillation", "annotation",
    ],
    "Robotics and world models": [
        "robot", "robotics", "world model", "robot manipulation", "embodied", "locomotion",
        "robotic", "physical control",
    ],
}

AFFILIATION_ALIASES = [
    (r"\bmit\b|massachusetts institute of technology", "MIT"),
    (r"\buc berkeley\b|university of california[, ]+berkeley|berkeley ai research|\bbair\b", "UC Berkeley"),
    (r"carnegie mellon|\bcmu\b", "Carnegie Mellon University"),
    (r"stanford", "Stanford University"),
    (r"tsinghua", "Tsinghua University"),
    (r"peking university|\bpku\b", "Peking University"),
    (r"zhejiang university", "Zhejiang University"),
    (r"university of science and technology of china|\bustc\b", "University of Science and Technology of China"),
    (r"shanghai jiao ?tong|sjtu", "Shanghai Jiao Tong University"),
    (r"fudan", "Fudan University"),
    (r"national university of singapore|\bnus\b", "National University of Singapore"),
    (r"nanyang technological university|\bntu\b", "Nanyang Technological University"),
    (r"chinese university of hong kong|\bcuhk\b", "The Chinese University of Hong Kong"),
    (r"hong kong university of science and technology|\bhkust\b", "Hong Kong University of Science and Technology"),
    (r"the university of hong kong|university of hong kong|\bhku\b", "University of Hong Kong"),
    (r"university of oxford|oxford university|^oxford$", "University of Oxford"),
    (r"university of cambridge|cambridge university", "University of Cambridge"),
    (r"harvard", "Harvard University"),
    (r"georgia institute of technology|georgia tech", "Georgia Tech"),
    (r"eth zurich|eth zürich|ethz", "ETH Zurich"),
    (r"kaist|korea advanced institute of science", "KAIST"),
    (r"beihang university|beijing university of aeronautics", "Beihang University"),
    (r"^nanjing university$", "Nanjing University"),
    (r"university of chinese academy of sciences|university of the chinese academy of sciences", "University of Chinese Academy of Sciences"),
    (r"chinese academy of sciences|\bcas\b", "Chinese Academy of Sciences"),
    (r"university of toronto", "University of Toronto"),
    (r"university of washington", "University of Washington"),
    (r"university of illinois.*urbana|uiuc", "University of Illinois Urbana-Champaign"),
    (r"princeton", "Princeton University"),
    (r"cornell", "Cornell University"),
    (r"university of michigan", "University of Michigan"),
    (r"university of texas.*austin|ut austin", "University of Texas at Austin"),
    (r"google deepmind|deepmind", "Google DeepMind"),
    (r"google research|google brain|\bgoogle\b", "Google"),
    (r"microsoft research|\bmicrosoft\b", "Microsoft"),
    (r"meta ai|meta fair|fair at meta|meta superintelligence|facebook ai|facebook research|\bfacebook\b|\bfair\b|\bmeta\b", "Meta"),
    (r"openai", "OpenAI"),
    (r"anthropic", "Anthropic"),
    (r"nvidia", "NVIDIA"),
    (r"amazon|aws", "Amazon"),
    (r"apple", "Apple"),
    (r"alibaba|ant group|ant groupe", "Alibaba"),
    (r"bytedance|byte dance", "ByteDance"),
    (r"tencent", "Tencent"),
    (r"huawei", "Huawei"),
    (r"baidu", "Baidu"),
    (r"salesforce", "Salesforce"),
    (r"sensetime", "SenseTime"),
    (r"\bxai\b", "xAI"),
    (r"samsung", "Samsung"),
    (r"snap inc|snap research|\bsnap\b", "Snap"),
    (r"lg ai research", "LG AI Research"),
    (r"gray swan ai", "Gray Swan AI"),
    (r"snowflake", "Snowflake"),
    (r"tesla", "Tesla"),
    (r"\bmila\b|quebec ai institute|quebec artificial intelligence institute", "Mila"),
    (r"allen institute|ai2", "Allen Institute for AI"),
    (r"max planck|ellis institute|\bellis\b", "Max Planck / ELLIS"),
    (r"vector institute", "Vector Institute"),
    (r"mbzuai", "MBZUAI"),
    (r"shanghai ai lab|shanghai artificial intelligence laboratory", "Shanghai AI Laboratory"),
]

INDUSTRY_ORGS = {
    "Google", "Google DeepMind", "Microsoft", "Meta", "OpenAI", "Anthropic", "NVIDIA",
    "Amazon", "Apple", "Alibaba", "ByteDance", "Tencent", "Huawei", "Baidu", "Salesforce",
    "SenseTime", "xAI", "Samsung", "Snap", "LG AI Research", "Gray Swan AI", "Snowflake", "Tesla",
}

RESEARCH_INSTITUTES = {
    "Mila", "Allen Institute for AI", "MBZUAI", "Shanghai AI Laboratory",
    "Chinese Academy of Sciences", "Max Planck / ELLIS", "Vector Institute",
}

ACADEMIC_ORGS = {
    "MIT", "UC Berkeley", "ETH Zurich", "KAIST", "Georgia Tech",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def read_json(path: Path) -> dict[str, object]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_title(title: str) -> str:
    title = title.lower()
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def clean_affiliation(value: str) -> str:
    value = re.sub(r"\s+", " ", value or "").strip()
    value = value.replace("&amp;", "&").replace("&#x27;", "'")
    if value.lower() in {"none", "n/a", "na", "unknown", "anonymous"}:
        return ""
    parts = [part.strip() for part in value.split(",") if part.strip()]
    if len(parts) == 2 and parts[0].lower() == parts[1].lower():
        value = parts[0]
    return value.strip(" ;,")


def canonical_affiliation(value: str) -> str:
    cleaned = clean_affiliation(value)
    if not cleaned:
        return ""
    lower = cleaned.lower()
    for pattern, canonical in AFFILIATION_ALIASES:
        if re.search(pattern, lower):
            return canonical
    return cleaned


def affiliation_sector(canonical: str) -> str:
    if canonical in INDUSTRY_ORGS:
        return "Industry"
    if canonical in RESEARCH_INSTITUTES:
        return "Research institute"
    if canonical in ACADEMIC_ORGS:
        return "Academia"
    if any(token in canonical.lower() for token in ["university", "institute of technology", "college"]):
        return "Academia"
    return "Other / unknown"


def theme_hits_for_paper(paper: dict[str, str]) -> list[str]:
    text = " ".join([paper.get("title", ""), paper.get("abstract", ""), paper.get("topic", "")])
    lower = text.lower()
    topic = paper.get("topic", "")
    hits = set()

    if topic.startswith("Deep Learning->Large Language Models"):
        hits.add("LLM reasoning and test-time compute")
    if topic.startswith("Reinforcement Learning"):
        hits.add("RL for LLMs and verifiable rewards")
    if topic.startswith("Applications->Robotics"):
        hits.add("Robotics and world models")
    if topic.startswith("Applications->Computer Vision") or "vision" in topic.lower():
        hits.add("Multimodal, vision-language, and video")
    if topic.startswith("Applications->Chemistry") or topic.startswith("Applications->Health") or "Neuroscience" in topic:
        hits.add("AI for science, health, and biology")
    if topic.startswith("Social Aspects"):
        hits.add("Safety, alignment, governance, and risk")
    if topic.startswith("Theory") or topic.startswith("Optimization") or topic.startswith("Probabilistic Methods"):
        hits.add("Theory, optimization, and sampling")
    if "Causality" in topic:
        hits.add("Causality and data-centric ML")

    for theme, needles in THEMES.items():
        if any(n in lower for n in needles):
            hits.add(theme)
    hits = sorted(hits)
    return hits or ["Other / uncategorized"]


def intish(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def alpha_source_label(metadata: dict[str, object]) -> str:
    if metadata.get("is_complete_feed"):
        return "the complete AlphaXiv ICML feed"
    row_count = metadata.get("row_count")
    if row_count:
        return f"an AlphaXiv ICML seed snapshot ({row_count:,} rows)"
    return "an AlphaXiv ICML seed snapshot"


def paper_flags(row: dict[str, object]) -> str:
    flags = [f for f in [row["award"], "oral" if row["is_oral"] == "true" else ""] if f]
    return "; ".join(flags)


def main() -> int:
    icml = read_csv(PROCESSED / "icml2026_papers.csv")
    alpha = read_csv(PROCESSED / "alphaxiv_icml2026_joined.csv")
    awards = read_csv(PROCESSED / "icml2026_awards.csv")
    alpha_metadata = read_json(PROCESSED / "alphaxiv_icml2026_metadata.json")
    if not icml:
        raise SystemExit("Run scripts/fetch_icml_virtual.py first.")

    alpha_by_title = {normalize_title(row["title"]): row for row in alpha}
    awards_by_title = {normalize_title(row["title"]): row for row in awards}

    theme_counts = Counter()
    oral_theme_counts = Counter()
    topic_counts = Counter(row["topic"] or "Unknown" for row in icml)
    topic_group_counts = Counter(row["topic_group"] or "Unknown" for row in icml)
    institution_counts = Counter()
    canonical_institution_counts = Counter()
    sector_counts = Counter()
    canonical_examples = defaultdict(Counter)
    theme_examples = defaultdict(list)
    rows = []

    max_votes = max([intish(r.get("public_total_votes", "0")) for r in alpha] or [1])
    max_recent = max([intish(r.get("visits_last_7_days", "0")) for r in alpha] or [1])

    for paper in icml:
        key = normalize_title(paper["title"])
        alpha_row = alpha_by_title.get(key, {})
        award = awards_by_title.get(key, {}).get("award", "")
        text = " ".join([paper.get("title", ""), paper.get("abstract", ""), paper.get("topic", "")])
        themes = theme_hits_for_paper(paper)
        for theme in themes:
            theme_counts[theme] += 1
            if paper.get("is_oral") == "true":
                oral_theme_counts[theme] += 1
            if len(theme_examples[theme]) < 5:
                theme_examples[theme].append(paper["title"])
        paper_canonicals = set()
        for inst in [x.strip() for x in paper.get("institutions", "").split(";") if x.strip()]:
            institution_counts[inst] += 1
            canonical = canonical_affiliation(inst)
            paper_canonicals.add(canonical)
            canonical_examples[canonical][clean_affiliation(inst)] += 1
        for canonical in paper_canonicals:
            canonical_institution_counts[canonical] += 1
            sector_counts[affiliation_sector(canonical)] += 1
        for org in [x.strip() for x in alpha_row.get("organizations", "").split(";") if x.strip()]:
            canonical = canonical_affiliation(org)
            canonical_examples[canonical][clean_affiliation(org)] += 1

        votes = intish(alpha_row.get("public_total_votes", "0"))
        recent = intish(alpha_row.get("visits_last_7_days", "0"))
        score = (
            4.0 * bool(award)
            + 1.5 * (paper.get("is_oral") == "true")
            + 2.0 * (votes / max_votes if max_votes else 0)
            + 1.0 * (recent / max_recent if max_recent else 0)
            + 0.2 * math.log1p(intish(alpha_row.get("github_stars", "0")))
        )
        rows.append(
            {
                "event_id": paper["event_id"],
                "title": paper["title"],
                "themes": "; ".join(themes),
                "official_topic": paper.get("topic", ""),
                "topic_group": paper.get("topic_group", ""),
                "decision": paper.get("decision", ""),
                "is_oral": paper.get("is_oral", "false"),
                "award": award,
                "public_total_votes": votes,
                "visits_last_7_days": recent,
                "github_stars": intish(alpha_row.get("github_stars", "0")),
                "score": round(score, 4),
                "url": paper.get("url", ""),
                "alphaxiv_url": alpha_row.get("alphaxiv_url", ""),
            }
        )

    write_csv(
        PROCESSED / "icml2026_theme_matrix.csv",
        rows,
        [
            "event_id", "title", "themes", "official_topic", "topic_group", "decision", "is_oral",
            "award", "public_total_votes", "visits_last_7_days", "github_stars", "score", "url",
            "alphaxiv_url",
        ],
    )
    write_csv(
        PROCESSED / "icml2026_theme_counts.csv",
        [{"theme": k, "count": v, "share": round(v / len(icml), 4), "oral_count": oral_theme_counts[k]} for k, v in theme_counts.most_common()],
        ["theme", "count", "share", "oral_count"],
    )
    write_csv(
        PROCESSED / "icml2026_institution_counts.csv",
        [{"institution": k, "paper_count": v} for k, v in institution_counts.most_common(200)],
        ["institution", "paper_count"],
    )
    write_csv(
        PROCESSED / "icml2026_canonical_institution_counts.csv",
        [
            {
                "canonical_institution": k,
                "paper_count": v,
                "sector": affiliation_sector(k),
                "common_raw_forms": "; ".join(raw for raw, _ in canonical_examples[k].most_common(5)),
            }
            for k, v in canonical_institution_counts.most_common(300)
        ],
        ["canonical_institution", "paper_count", "sector", "common_raw_forms"],
    )
    write_csv(
        PROCESSED / "icml2026_sector_counts.csv",
        [{"sector": k, "paper_institution_mentions": v} for k, v in sector_counts.most_common()],
        ["sector", "paper_institution_mentions"],
    )

    reading = sorted(rows, key=lambda r: r["score"], reverse=True)[:60]
    theme_reading_rows = []
    for theme, _ in theme_counts.most_common():
        candidates = [row for row in rows if theme in row["themes"].split("; ")]
        for rank, row in enumerate(sorted(candidates, key=lambda r: r["score"], reverse=True)[:12], start=1):
            theme_reading_rows.append(
                {
                    "theme": theme,
                    "rank": rank,
                    "title": row["title"],
                    "award": row["award"],
                    "is_oral": row["is_oral"],
                    "public_total_votes": row["public_total_votes"],
                    "visits_last_7_days": row["visits_last_7_days"],
                    "github_stars": row["github_stars"],
                    "score": row["score"],
                    "official_topic": row["official_topic"],
                    "url": row["url"],
                    "alphaxiv_url": row["alphaxiv_url"],
                }
            )
    write_csv(
        PROCESSED / "icml2026_theme_reading_map.csv",
        theme_reading_rows,
        [
            "theme", "rank", "title", "award", "is_oral", "public_total_votes",
            "visits_last_7_days", "github_stars", "score", "official_topic", "url", "alphaxiv_url",
        ],
    )

    oral_rows = [r for r in rows if r["is_oral"] == "true"]
    award_rows = [r for r in rows if r["award"]]
    high_vote_non_award = [r for r in sorted(rows, key=lambda r: r["public_total_votes"], reverse=True) if not r["award"]][:25]
    award_low_vote = sorted(award_rows, key=lambda r: r["public_total_votes"])[:15]
    alpha_label = alpha_source_label(alpha_metadata)
    alpha_caveat = (
        "- AlphaXiv data is a complete feed pull for this snapshot, but vote and visit counts remain time-sensitive community attention signals."
        if alpha_metadata.get("is_complete_feed")
        else "- AlphaXiv data is a seed snapshot; run `fetch_alphaxiv_icml.py --all` before publication-grade community-signal claims."
    )

    lines = [
        "# ICML 2026 Researcher Landscape Report",
        "",
        f"This report uses the official ICML virtual bulk metadata plus {alpha_label}.",
        "",
        "## Corpus Snapshot",
        "",
        f"- Official ICML paper rows: {len(icml):,}",
        f"- Oral-designated papers: {len(oral_rows):,}",
        f"- Position-prefixed papers: {sum(r.get('is_position') == 'true' for r in icml):,}",
        f"- Award/test-of-time rows: {len(awards):,}",
        f"- AlphaXiv community rows joined: {len(alpha):,}",
        "",
        "## Official Topic Groups",
        "",
    ]
    for topic, count in topic_group_counts.most_common(15):
        lines.append(f"- {topic}: {count:,} ({count / len(icml) * 100:.1f}%)")

    lines.extend(["", "## Research Themes From Title + Abstract", ""])
    for theme, count in theme_counts.most_common():
        lines.append(
            f"- {theme}: {count:,} ({count / len(icml) * 100:.1f}%); oral-designated: {oral_theme_counts[theme]:,}"
        )

    lines.extend(["", "## Most Frequent Canonical Institutions", ""])
    for inst, count in canonical_institution_counts.most_common(25):
        lines.append(f"- {inst}: {count:,} ({affiliation_sector(inst)})")

    lines.extend(["", "## Affiliation Sector Mix", ""])
    total_sector_mentions = sum(sector_counts.values()) or 1
    for sector, count in sector_counts.most_common():
        lines.append(f"- {sector}: {count:,} paper-institution mentions ({count / total_sector_mentions * 100:.1f}%)")

    lines.extend(["", "## Most Frequent Raw Institution Strings", ""])
    for inst, count in institution_counts.most_common(25):
        lines.append(f"- {inst}: {count:,}")

    lines.extend(["", "## Reading List Seed: Highest Composite Signal", ""])
    for i, row in enumerate(reading[:30], start=1):
        flags = paper_flags(row)
        flag_text = f" ({flags})" if flags else ""
        lines.append(
            f"{i}. {row['title']}{flag_text} - themes: {row['themes']}; "
            f"votes: {row['public_total_votes']}; recent visits: {row['visits_last_7_days']}"
        )

    lines.extend(["", "## Theme Reading Map", ""])
    lines.append("Top-ranked papers per rule-based theme, scored by award/oral status plus AlphaXiv vote, visit, and GitHub signals.")
    for theme, _ in theme_counts.most_common():
        lines.append("")
        lines.append(f"### {theme}")
        theme_rows = [row for row in theme_reading_rows if row["theme"] == theme][:5]
        for row in theme_rows:
            flags = paper_flags(row)
            flag_text = f" ({flags})" if flags else ""
            lines.append(
                f"{row['rank']}. {row['title']}{flag_text} - "
                f"votes: {row['public_total_votes']}; recent visits: {row['visits_last_7_days']}; "
                f"topic: {row['official_topic'] or 'Unknown'}"
            )
    lines.append("")
    lines.append("Full table: `data/processed/icml2026_theme_reading_map.csv`.")

    lines.extend(["", "## Community-High, Not Official-Awarded", ""])
    for i, row in enumerate(high_vote_non_award[:20], start=1):
        lines.append(
            f"{i}. {row['title']} - {row['public_total_votes']} public votes; "
            f"{'oral; ' if row['is_oral'] == 'true' else ''}{row['themes']}"
        )

    lines.extend(["", "## Official Awards With Lower AlphaXiv Vote Signal", ""])
    for row in award_low_vote:
        lines.append(f"- {row['title']} - {row['award']}; {row['public_total_votes']} public votes")

    lines.extend(["", "## Theme Examples", ""])
    for theme, examples in theme_examples.items():
        lines.append(f"### {theme}")
        for title in examples:
            lines.append(f"- {title}")
        lines.append("")

    lines.extend(
        [
            "## Researcher Takeaways",
            "",
            "- ICML 2026 is heavily shaped by LLM reasoning, RL-style post-training, agents, and verification.",
            "- Diffusion remains central, but the interesting split is now language-model diffusion, sampling theory, and generative media.",
            "- Safety/alignment/governance is no longer peripheral; it appears both in technical papers and position papers.",
            "- AlphaXiv attention concentrates strongly on LLM/RL/agent work, so community signal should be compared against official topic balance.",
            "- The official topic taxonomy is valuable and should be preferred over title-only heuristics for high-level statistics.",
            "",
            "## Caveats",
            "",
            alpha_caveat,
            "- Canonical institution names use a hand-written alias map. This is better than raw strings, but final lab rankings still need manual QA.",
            "- Theme labels are rule-based over title+abstract; use embeddings or manual review before publication-grade claims.",
        ]
    )

    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "icml2026_researcher_landscape.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {REPORTS / 'icml2026_researcher_landscape.md'}")

    reading_lines = [
        "# ICML 2026 Theme Reading Map",
        "",
        f"Source: official ICML virtual metadata plus {alpha_label}.",
        "",
        "This is a researcher triage artifact: each theme is rule-labeled from title, abstract, and official topic, then ranked by a composite of official awards, oral status, AlphaXiv votes, recent visits, and GitHub stars.",
        "",
    ]
    for theme, _ in theme_counts.most_common():
        reading_lines.extend([f"## {theme}", ""])
        for row in [r for r in theme_reading_rows if r["theme"] == theme][:12]:
            flags = paper_flags(row)
            flag_text = f" ({flags})" if flags else ""
            reading_lines.append(
                f"{row['rank']}. {row['title']}{flag_text} - "
                f"votes: {row['public_total_votes']}; recent visits: {row['visits_last_7_days']}; "
                f"score: {row['score']}; topic: {row['official_topic'] or 'Unknown'}"
            )
        reading_lines.append("")
    reading_lines.extend(
        [
            "## Caveats",
            "",
            alpha_caveat,
            "- A paper can appear in multiple themes; this is intentional because many ICML 2026 papers span method, application, and evaluation categories.",
            "- The ranking is a reading-prioritization heuristic, not a quality ranking.",
        ]
    )
    (REPORTS / "icml2026_theme_reading_map.md").write_text("\n".join(reading_lines), encoding="utf-8")
    print(f"Wrote {REPORTS / 'icml2026_theme_reading_map.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
