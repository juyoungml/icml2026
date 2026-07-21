#!/usr/bin/env python3
"""Build accepted-paper venue baselines against the ICML 2026 taxonomy."""

from __future__ import annotations

import csv
import html
import json
import re
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "historical"
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"

VENUES = [
    {
        "venue": "ICML 2025",
        "year": "2025",
        "base_url": "https://icml.cc",
        "events_url": "https://icml.cc/static/virtual/data/icml-2025-orals-posters.json",
        "abstracts_url": "https://icml.cc/static/virtual/data/icml-2025-abstracts.json",
        "source_scope": "official virtual JSON; abstracts unavailable from static endpoint",
    },
    {
        "venue": "NeurIPS 2025",
        "year": "2025",
        "base_url": "https://neurips.cc",
        "events_url": "https://neurips.cc/static/virtual/data/neurips-2025-orals-posters.json",
        "abstracts_url": "https://neurips.cc/static/virtual/data/neurips-2025-abstracts.json",
        "source_scope": "official virtual JSON; abstracts unavailable from static endpoint",
    },
    {
        "venue": "ICLR 2026",
        "year": "2026",
        "base_url": "https://iclr.cc",
        "events_url": "https://iclr.cc/static/virtual/data/iclr-2026-orals-posters.json",
        "abstracts_url": "https://iclr.cc/static/virtual/data/iclr-2026-abstracts.json",
        "source_scope": "official virtual JSON plus static abstracts",
    },
]

ICML_2026_SOURCE = {
    "venue": "ICML 2026",
    "year": "2026",
    "base_url": "https://icml.cc",
    "source_scope": "local official ICML 2026 processed table with abstracts",
}

AREA_TERMS = {
    "LLM Reasoning, Post-Training, and RLVR": [
        "large language model", "llm", "language model", "reasoning", "chain of thought", "cot",
        "preference", "rlhf", "rlvr", "reward model", "post training", "alignment tuning",
        "instruction tuning", "verifiable", "inference time", "test time compute",
    ],
    "Multimodal, Vision, and Perception": [
        "multimodal", "multi modal", "vision language", "vision-language", "video", "visual",
        "image", "perception", "3d", "detection", "segmentation", "scene", "spatial",
        "object", "camera", "rendering",
    ],
    "Theory, Optimization, and Algorithms": [
        "learning theory", "generalization", "optimization", "convex", "nonconvex", "regret",
        "bandit", "bayesian", "probabilistic", "statistical", "proof", "theorem", "sample complexity",
        "stochastic optimization", "gradient descent", "matrix", "quantum", "online learning",
    ],
    "AI for Science, Health, and Neuro": [
        "protein", "molecule", "molecular", "chemistry", "physics", "climate", "weather",
        "genomics", "medical", "clinical", "health", "neuro", "brain", "spiking", "dynamics",
        "time series", "forecasting", "science", "biology", "drug", "pde",
    ],
    "Data-Centric, Causal, and Federated ML": [
        "causal", "causality", "data selection", "data valuation",
        "continual learning", "federated", "unlearning", "domain adaptation", "active learning",
        "distribution shift", "missing data", "synthetic data", "data-centric",
    ],
    "Systems and Efficient Foundation Models": [
        "quantization", "compression", "pruning", "kv cache", "serving", "throughput", "latency",
        "gpu memory", "efficient inference", "efficient training", "efficiency", "moe",
        "mixture of experts", "long context", "inference serving", "gpu", "kernel", "scaling law",
    ],
    "Safety, Governance, Privacy, and Society": [
        "safety", "alignment", "jailbreak", "privacy", "fairness", "governance", "bias",
        "security", "attack", "adversarial", "robustness", "toxicity", "memorization",
        "watermark", "copyright", "deepfake", "society", "policy", "trustworthy",
    ],
    "Agents, Code, and Tool Use": [
        "agent", "agents", "tool use", "tool-use", "software engineering", "code", "coding",
        "programming", "program synthesis", "web agent", "multi-agent", "multi agent", "planning",
        "workflow", "verification", "repository", "compiler",
    ],
    "Graphs, Geometry, and Representation Learning": [
        "graph neural network", "gnn", "graph", "equivariant", "geometric", "geometry",
        "manifold", "representation learning", "embedding", "contrastive", "invariant",
        "symmetry", "topological", "topology",
    ],
    "Generative Modeling": [
        "diffusion", "flow matching", "generative", "score based", "score-based", "image generation",
        "video generation", "denoising", "vae", "gan", "autoregressive generation", "transport",
        "consistency model",
    ],
    "Reinforcement Learning and Control": [
        "reinforcement learning", "rl", "offline rl", "control", "policy", "mdp", "q-learning",
        "actor critic", "actor-critic", "bandit", "decision process", "trajectory",
        "imitation learning", "exploration",
    ],
    "Robotics, Embodiment, and World Models": [
        "robot", "robotics", "embodied", "embodiment", "world model", "vision language action",
        "vision-language-action", "vla", "manipulation", "navigation", "locomotion", "sim2real",
        "simulation", "control policy",
    ],
}


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


def fetch_json(url: str, dest: Path) -> dict:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        return json.loads(dest.read_text(encoding="utf-8"))
    req = urllib.request.Request(url, headers={"User-Agent": "icml2026-eda/0.1"})
    with urllib.request.urlopen(req, timeout=60) as response:
        payload = json.loads(response.read().decode("utf-8"))
    dest.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return payload


def try_fetch_json(url: str, dest: Path) -> tuple[dict[str, str], str]:
    try:
        payload = fetch_json(url, dest)
        return {str(key): clean_text(value) for key, value in payload.items()}, "ok"
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return {}, "404"
        raise


def clean_text(value: object) -> str:
    text = html.unescape(str(value or ""))
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize(value: str) -> str:
    value = html.unescape(value).lower()
    value = re.sub(r"[^a-z0-9+#.-]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def contains_term(text: str, term: str) -> bool:
    needle = normalize(term)
    if not needle:
        return False
    pattern = r"(?<![a-z0-9])" + re.escape(needle) + r"(?![a-z0-9])"
    return re.search(pattern, text) is not None


def classify(title: str, topic: str, abstract: str) -> dict[str, object]:
    fields = [(normalize(title), 3), (normalize(topic), 2), (normalize(abstract), 1)]
    scores: dict[str, int] = {}
    matched: dict[str, list[str]] = {}
    for area, terms in AREA_TERMS.items():
        score = 0
        hits: list[str] = []
        for term in terms:
            term_score = 0
            for text, weight in fields:
                if contains_term(text, term):
                    term_score += weight
            if term_score:
                score += term_score
                hits.append(term)
        scores[area] = score
        matched[area] = hits

    ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    best_area, best_score = ranked[0]
    second_score = ranked[1][1] if len(ranked) > 1 else 0
    if best_score == 0:
        return {
            "area": "Uncoded / Other",
            "area_score": 0,
            "second_area": "",
            "second_score": 0,
            "score_margin": 0,
            "confidence": "uncoded",
            "matched_terms": "",
            "all_area_scores": "",
        }
    margin = best_score - second_score
    if best_score >= 8 and margin >= 3:
        confidence = "high"
    elif best_score >= 4 and margin >= 1:
        confidence = "medium"
    else:
        confidence = "low"
    return {
        "area": best_area,
        "area_score": best_score,
        "second_area": ranked[1][0] if len(ranked) > 1 and second_score else "",
        "second_score": second_score,
        "score_margin": margin,
        "confidence": confidence,
        "matched_terms": "; ".join(matched[best_area][:12]),
        "all_area_scores": "; ".join(f"{area}={score}" for area, score in ranked if score > 0),
    }


def accepted_poster_events(events: list[dict], base_url: str, abstracts: dict[str, str], venue: str, year: str) -> list[dict[str, object]]:
    rows = []
    for event in events:
        if event.get("eventtype") != "Poster":
            continue
        event_id = str(event.get("id") or "")
        title = clean_text(event.get("name") or "")
        topic = clean_text(event.get("topic") or "")
        abstract = abstracts.get(event_id, "")
        authors = "; ".join(clean_text(author.get("fullname")) for author in event.get("authors") or [] if author.get("fullname"))
        institutions = "; ".join(sorted({clean_text(author.get("institution")) for author in event.get("authors") or [] if author.get("institution")}))
        classification = classify(title, topic, abstract)
        rows.append(
            {
                "venue": venue,
                "year": year,
                "event_id": event_id,
                "event_type": "Poster",
                "title": title,
                "decision": clean_text(event.get("decision") or ""),
                "topic": topic,
                "topic_group": topic.split("->", 1)[0] if topic else "",
                "authors": authors,
                "institutions": institutions,
                "author_count": len([part for part in authors.split("; ") if part]),
                "institution_count": len([part for part in institutions.split("; ") if part]),
                "abstract_available": str(bool(abstract)).lower(),
                "url": base_url + clean_text(event.get("virtualsite_url") or ""),
                "paper_url": clean_text(event.get("paper_url") or ""),
                **classification,
            }
        )
    return rows


def icml2026_rows() -> list[dict[str, object]]:
    rows = []
    for row in read_csv(PROCESSED / "icml2026_papers.csv"):
        classification = classify(row.get("title", ""), row.get("topic", ""), row.get("abstract", ""))
        rows.append(
            {
                "venue": "ICML 2026",
                "year": "2026",
                "event_id": row.get("event_id", ""),
                "event_type": row.get("event_type", ""),
                "title": row.get("title", ""),
                "decision": row.get("decision", ""),
                "topic": row.get("topic", ""),
                "topic_group": row.get("topic_group", ""),
                "authors": row.get("authors", ""),
                "institutions": row.get("institutions", ""),
                "author_count": row.get("author_count", ""),
                "institution_count": row.get("institution_count", ""),
                "abstract_available": str(bool(row.get("abstract", ""))).lower(),
                "url": row.get("url", ""),
                "paper_url": row.get("paper_url", ""),
                **classification,
            }
        )
    return rows


def summarize_area(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    totals = Counter()
    for row in rows:
        venue = str(row["venue"])
        groups[(venue, str(row["area"]))].append(row)
        totals[venue] += 1

    venue_year = {str(row["venue"]): str(row["year"]) for row in rows}
    output = []
    for (venue, area), items in groups.items():
        count = len(items)
        confidence_counter = Counter(str(row["confidence"]) for row in items)
        abstract_count = sum(str(row["abstract_available"]) == "true" for row in items)
        examples = sorted(items, key=lambda row: (str(row["confidence"]) == "high", int(row["area_score"]), str(row["title"])), reverse=True)[:8]
        output.append(
            {
                "venue": venue,
                "year": venue_year.get(venue, ""),
                "area": area,
                "paper_count": count,
                "share": round(count / totals[venue], 4) if totals[venue] else 0,
                "high_confidence_count": confidence_counter["high"],
                "medium_confidence_count": confidence_counter["medium"],
                "low_confidence_count": confidence_counter["low"],
                "uncoded_count": confidence_counter["uncoded"],
                "abstract_available_count": abstract_count,
                "representative_titles": " | ".join(str(row["title"]) for row in examples),
            }
        )
    return sorted(output, key=lambda row: (str(row["venue"]), -int(row["paper_count"]), str(row["area"])))


def build_delta_rows(area_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    share_by = {(str(row["venue"]), str(row["area"])): float(row["share"]) for row in area_rows}
    count_by = {(str(row["venue"]), str(row["area"])): int(row["paper_count"]) for row in area_rows}
    areas = sorted({area for _, area in share_by if area != "Uncoded / Other"})
    baselines = ["ICML 2025", "NeurIPS 2025", "ICLR 2026"]
    output = []
    for area in areas:
        baseline_shares = [share_by.get((venue, area), 0.0) for venue in baselines]
        baseline_avg = sum(baseline_shares) / len(baseline_shares)
        icml2026 = share_by.get(("ICML 2026", area), 0.0)
        output.append(
            {
                "area": area,
                "icml2026_count": count_by.get(("ICML 2026", area), 0),
                "icml2026_share": round(icml2026, 4),
                "icml2025_share": round(share_by.get(("ICML 2025", area), 0.0), 4),
                "neurips2025_share": round(share_by.get(("NeurIPS 2025", area), 0.0), 4),
                "iclr2026_share": round(share_by.get(("ICLR 2026", area), 0.0), 4),
                "baseline_avg_share": round(baseline_avg, 4),
                "delta_vs_baseline_avg": round(icml2026 - baseline_avg, 4),
                "relative_to_baseline_avg": round(icml2026 / baseline_avg, 2) if baseline_avg else "",
            }
        )
    return sorted(output, key=lambda row: float(row["delta_vs_baseline_avg"]), reverse=True)


def write_report(paper_rows: list[dict[str, object]], area_rows: list[dict[str, object]], delta_rows: list[dict[str, object]], source_status: list[dict[str, str]]) -> None:
    totals = Counter(str(row["venue"]) for row in paper_rows)
    uncoded = Counter(str(row["venue"]) for row in paper_rows if row["area"] == "Uncoded / Other")
    high_medium = Counter(str(row["venue"]) for row in paper_rows if row["confidence"] in {"high", "medium"})
    top_positive = delta_rows[:6]
    top_negative = [row for row in sorted(delta_rows, key=lambda row: float(row["delta_vs_baseline_avg"])) if float(row["delta_vs_baseline_avg"]) < 0][:6]

    lines = [
        "# Historical Accepted-Paper Baseline Against ICML 2026",
        "",
        "This report compares ICML 2026 against accepted-paper corpora from ICML 2025, NeurIPS 2025, and ICLR 2026 using the same transparent keyword scorer over titles, topics, and available abstracts.",
        "",
        "## Source Coverage",
        "",
        "| Source | Paper rows | Abstract coverage | Notes |",
        "| --- | ---: | ---: | --- |",
    ]
    for source in ["ICML 2026", "ICML 2025", "NeurIPS 2025", "ICLR 2026"]:
        total = totals[source]
        abstract_count = sum(1 for row in paper_rows if row["venue"] == source and row["abstract_available"] == "true")
        status = next((item for item in source_status if item["venue"] == source), {})
        notes = status.get("source_scope", "")
        lines.append(f"| {source} | {total:,} | {abstract_count:,} ({abstract_count / total:.1%}) | {notes} |")

    lines.extend(
        [
            "",
            "## Classification Health",
            "",
            "| Venue | High/medium-confidence rows | Uncoded rows |",
            "| --- | ---: | ---: |",
        ]
    )
    for venue in ["ICML 2026", "ICML 2025", "NeurIPS 2025", "ICLR 2026"]:
        total = totals[venue]
        lines.append(f"| {venue} | {high_medium[venue]:,} ({high_medium[venue] / total:.1%}) | {uncoded[venue]:,} ({uncoded[venue] / total:.1%}) |")

    lines.extend(
        [
            "",
            "## Largest ICML 2026 Overweights vs Baseline Average",
            "",
            "| Area | ICML 2026 share | Baseline avg | Delta | Relative |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in top_positive:
        lines.append(
            f"| {row['area']} | {float(row['icml2026_share']):.1%} | {float(row['baseline_avg_share']):.1%} | {float(row['delta_vs_baseline_avg']):+.1%} | {row['relative_to_baseline_avg']}x |"
        )

    lines.extend(
        [
            "",
            "## Largest ICML 2026 Underweights vs Baseline Average",
            "",
            "| Area | ICML 2026 share | Baseline avg | Delta | Relative |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in top_negative:
        lines.append(
            f"| {row['area']} | {float(row['icml2026_share']):.1%} | {float(row['baseline_avg_share']):.1%} | {float(row['delta_vs_baseline_avg']):+.1%} | {row['relative_to_baseline_avg']}x |"
        )
    if not top_negative:
        lines.append("| No negative deltas under this classifier |  |  |  |  |")

    lines.extend(
        [
            "",
            "## Venue Shares by Area",
            "",
            "| Area | ICML 2026 | ICML 2025 | NeurIPS 2025 | ICLR 2026 |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in sorted(delta_rows, key=lambda item: float(item["icml2026_share"]), reverse=True):
        lines.append(
            f"| {row['area']} | {float(row['icml2026_share']):.1%} | {float(row['icml2025_share']):.1%} | {float(row['neurips2025_share']):.1%} | {float(row['iclr2026_share']):.1%} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation Notes",
            "",
            "- This is an accepted-paper baseline, not an arXiv-volume baseline. It answers a different question from `reports/arxiv_taxonomy_trends.md`.",
            "- The comparison uses one common keyword scorer for all venues, so ICML 2026 shares here will differ from the semantic-cluster manual taxonomy shares.",
            "- ICML 2025 and NeurIPS 2025 static endpoints did not expose abstracts from the probed URL, so their classifications rely on title and topic metadata.",
            "- Broad terms such as `optimization`, `policy`, `graph`, `visual`, and `generative` can create false positives. Treat deltas as triage signals for manual review, not as final claims.",
            "- The most publication-ready use is to identify where to inspect papers manually: large positive deltas suggest ICML 2026 emphasis; large negative deltas suggest areas stronger in neighboring venues.",
        ]
    )

    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "historical_accepted_paper_baseline.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    source_status = [ICML_2026_SOURCE]
    paper_rows = icml2026_rows()

    for venue in VENUES:
        slug = venue["venue"].lower().replace(" ", "_")
        events_payload = fetch_json(venue["events_url"], RAW / f"{slug}_orals_posters.json")
        abstracts, abstract_status = try_fetch_json(venue["abstracts_url"], RAW / f"{slug}_abstracts.json")
        source_status.append({**venue, "abstract_status": abstract_status})
        paper_rows.extend(
            accepted_poster_events(
                events_payload.get("results", []),
                venue["base_url"],
                abstracts,
                venue["venue"],
                venue["year"],
            )
        )

    paper_rows.sort(key=lambda row: (str(row["venue"]), str(row["area"]), -int(row["area_score"]), str(row["title"])))
    area_rows = summarize_area(paper_rows)
    delta_rows = build_delta_rows(area_rows)

    paper_fields = [
        "venue", "year", "event_id", "event_type", "title", "decision", "topic", "topic_group",
        "authors", "institutions", "author_count", "institution_count", "abstract_available",
        "url", "paper_url", "area", "area_score", "second_area", "second_score", "score_margin",
        "confidence", "matched_terms", "all_area_scores",
    ]
    write_csv(PROCESSED / "historical_accepted_papers_classified.csv", paper_rows, paper_fields)
    write_csv(
        PROCESSED / "historical_venue_area_summary.csv",
        area_rows,
        [
            "venue", "year", "area", "paper_count", "share", "high_confidence_count",
            "medium_confidence_count", "low_confidence_count", "uncoded_count",
            "abstract_available_count", "representative_titles",
        ],
    )
    write_csv(
        PROCESSED / "historical_venue_delta_summary.csv",
        delta_rows,
        [
            "area", "icml2026_count", "icml2026_share", "icml2025_share", "neurips2025_share",
            "iclr2026_share", "baseline_avg_share", "delta_vs_baseline_avg",
            "relative_to_baseline_avg",
        ],
    )
    write_report(paper_rows, area_rows, delta_rows, source_status)

    print(f"Wrote {PROCESSED / 'historical_accepted_papers_classified.csv'} ({len(paper_rows):,} rows)")
    print(f"Wrote {PROCESSED / 'historical_venue_area_summary.csv'} ({len(area_rows):,} rows)")
    print(f"Wrote {PROCESSED / 'historical_venue_delta_summary.csv'} ({len(delta_rows):,} rows)")
    print(f"Wrote {REPORTS / 'historical_accepted_paper_baseline.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
