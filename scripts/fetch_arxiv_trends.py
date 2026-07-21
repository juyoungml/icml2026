#!/usr/bin/env python3
"""Fetch coarse arXiv trend counts for ICML 2026 taxonomy areas."""

from __future__ import annotations

import argparse
import csv
import json
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"
CACHE_PATH = RAW / "arxiv_trend_counts_cache.json"

YEARS = [2024, 2025, 2026]

AREA_QUERIES = {
    "LLM Reasoning, Post-Training, and RLVR": [
        '"large language model"', "reasoning", '"chain of thought"', '"reinforcement learning from human feedback"',
        '"preference optimization"', "RLVR",
    ],
    "Multimodal, Vision, and Perception": [
        "multimodal", '"vision language"', '"video understanding"', '"visual reasoning"', '"3D vision"',
    ],
    "Theory, Optimization, and Algorithms": [
        '"learning theory"', "optimization", "regret", "bandit", "bayesian", "probabilistic",
    ],
    "AI for Science, Health, and Neuro": [
        "protein", "molecule", "chemistry", "physics", "genomics", "medical", '"time series"',
    ],
    "Data-Centric, Causal, and Federated ML": [
        "causal", "causality", '"data selection"', '"continual learning"', '"federated learning"',
    ],
    "Systems and Efficient Foundation Models": [
        "quantization", "compression", '"KV cache"', "serving", "throughput", "latency", "MoE",
    ],
    "Safety, Governance, Privacy, and Society": [
        "safety", "alignment", "jailbreak", "privacy", "fairness", "governance", "bias",
    ],
    "Agents, Code, and Tool Use": [
        "agent", "agents", '"tool use"', '"software engineering"', "code", '"web agent"',
    ],
    "Graphs, Geometry, and Representation Learning": [
        '"graph neural network"', "GNN", "equivariant", "geometric", "manifold", "representation",
    ],
    "Generative Modeling": [
        "diffusion", '"flow matching"', '"generative model"', '"score based"', '"image generation"', '"video generation"',
    ],
    "Reinforcement Learning and Control": [
        '"reinforcement learning"', '"offline reinforcement learning"', "control", "policy", "MDP",
    ],
    "Robotics, Embodiment, and World Models": [
        "robot", "robotics", "embodied", '"world model"', '"vision language action"', "manipulation",
    ],
}


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def load_cache() -> dict[str, object]:
    if not CACHE_PATH.exists():
        return {}
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_cache(cache: dict[str, object]) -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, indent=2, sort_keys=True), encoding="utf-8")


def query_for_terms(terms: list[str], year: int) -> str:
    term_query = " OR ".join(f"all:{term}" for term in terms)
    start = f"{year}01010000"
    end = f"{year}12312359"
    if year == 2026:
        end = "202607142359"
    return f"({term_query}) AND submittedDate:[{start} TO {end}]"


def arxiv_total(search_query: str, retries: int = 3, retry_sleep: float = 5.0) -> tuple[int, str]:
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": search_query, "start": 0, "max_results": 1}
    )
    req = urllib.request.Request(url, headers={"User-Agent": "icml2026-eda-trends/0.1"})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()
            break
        except urllib.error.HTTPError as exc:
            if exc.code == 429 and attempt < retries - 1:
                time.sleep(retry_sleep * (attempt + 1))
                continue
            raise
    root = ET.fromstring(data)
    ns = {"opensearch": "http://a9.com/-/spec/opensearch/1.1/"}
    total = root.find("opensearch:totalResults", ns)
    if total is None:
        raise RuntimeError("arXiv response missing totalResults")
    return int(total.text or 0), url


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true", help="Refetch cached arXiv counts.")
    parser.add_argument("--retry-missing", action="store_true", help="Refetch only cached failures or missing counts.")
    parser.add_argument("--sleep", type=float, default=0.5, help="Seconds between uncached API calls.")
    args = parser.parse_args()

    cache = load_cache()
    rows = []
    fetched = 0
    for area, terms in AREA_QUERIES.items():
        for year in YEARS:
            key = f"{area}|{year}"
            query = query_for_terms(terms, year)
            cached = cache.get(key)
            should_use_cache = (
                not args.refresh
                and cached is not None
                and not (
                    args.retry_missing
                    and (cached.get("status") != "ok" or str(cached.get("count", "")).strip() == "")
                )
            )
            if should_use_cache:
                entry = cache[key]
            else:
                try:
                    total, url = arxiv_total(query)
                    entry = {"count": total, "query": query, "url": url, "status": "ok"}
                except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, RuntimeError) as exc:
                    entry = {"count": "", "query": query, "url": "", "status": f"{type(exc).__name__}: {exc}"}
                cache[key] = entry
                fetched += 1
                save_cache(cache)
                time.sleep(args.sleep)
            rows.append(
                {
                    "area": area,
                    "year": year,
                    "arxiv_count": entry.get("count", ""),
                    "query_terms": "; ".join(terms),
                    "query": entry.get("query", query),
                    "status": entry.get("status", ""),
                }
            )
    save_cache(cache)

    by_area = {}
    for row in rows:
        by_area.setdefault(row["area"], {})[int(row["year"])] = row

    summary_rows = []
    taxonomy_areas = {row["area"]: row for row in read_csv(PROCESSED / "icml2026_manual_taxonomy_areas.csv")}
    for area, year_rows in by_area.items():
        raw2024 = year_rows[2024]["arxiv_count"]
        raw2025 = year_rows[2025]["arxiv_count"]
        raw2026 = year_rows[2026]["arxiv_count"]
        c2024 = int(raw2024) if str(raw2024).strip() else None
        c2025 = int(raw2025) if str(raw2025).strip() else None
        c2026 = int(raw2026) if str(raw2026).strip() else None
        taxonomy = taxonomy_areas.get(area, {})
        summary_rows.append(
            {
                "area": area,
                "arxiv_2024": c2024 if c2024 is not None else "",
                "arxiv_2025": c2025 if c2025 is not None else "",
                "arxiv_2026_ytd": c2026 if c2026 is not None else "",
                "growth_2025_vs_2024": round((c2025 - c2024) / c2024, 4) if c2024 and c2025 is not None else "",
                "growth_2026_ytd_vs_2025": round((c2026 - c2025) / c2025, 4) if c2025 and c2026 is not None else "",
                "status_complete": str(all(value is not None for value in [c2024, c2025, c2026])).lower(),
                "icml2026_taxonomy_papers": taxonomy.get("paper_count", ""),
                "icml2026_area_share": taxonomy.get("share", ""),
                "query_terms": year_rows[2024]["query_terms"],
            }
        )
    summary_rows.sort(key=lambda row: int(row["arxiv_2026_ytd"] or -1), reverse=True)

    write_csv(
        PROCESSED / "arxiv_taxonomy_trend_counts.csv",
        rows,
        ["area", "year", "arxiv_count", "query_terms", "query", "status"],
    )
    write_csv(
        PROCESSED / "arxiv_taxonomy_trend_summary.csv",
        summary_rows,
        [
            "area", "arxiv_2024", "arxiv_2025", "arxiv_2026_ytd",
            "growth_2025_vs_2024", "growth_2026_ytd_vs_2025", "status_complete",
            "icml2026_taxonomy_papers", "icml2026_area_share", "query_terms",
        ],
    )

    lines = [
        "# arXiv Trend Baseline for ICML 2026 Taxonomy Areas",
        "",
        "This report provides a coarse arXiv query-count baseline for 2024, 2025, and 2026 year-to-date.",
        "It is not a prior-conference comparison; it is a broad external context signal for whether ICML 2026 areas align with wider arXiv activity.",
        "",
        "## Snapshot",
        "",
        f"- Areas queried: {len(AREA_QUERIES)}",
        f"- Area-year queries: {len(rows)}",
        f"- API responses fetched this run: {fetched}",
        f"- Cache: `{CACHE_PATH.relative_to(ROOT)}`",
        "",
        "## Area Trends",
        "",
    ]
    for row in summary_rows:
        growth = row["growth_2025_vs_2024"]
        growth_text = f"{float(growth) * 100:.1f}%" if growth != "" else "n/a"
        c2024 = f"{int(row['arxiv_2024']):,}" if row["arxiv_2024"] != "" else "missing"
        c2025 = f"{int(row['arxiv_2025']):,}" if row["arxiv_2025"] != "" else "missing"
        c2026 = f"{int(row['arxiv_2026_ytd']):,}" if row["arxiv_2026_ytd"] != "" else "missing"
        status = "" if row["status_complete"] == "true" else " [incomplete]"
        lines.append(
            f"- {row['area']}: 2024={c2024}, 2025={c2025}, "
            f"2026 YTD={c2026}; 2025 vs 2024 growth {growth_text}; "
            f"ICML taxonomy papers={row['icml2026_taxonomy_papers']}{status}"
        )
    lines.extend(
        [
            "",
            "## Caveats",
            "",
            "- Query terms are broad and overlapping; counts are not mutually exclusive.",
            "- arXiv search is not a conference-acceptance or quality signal.",
            "- 2026 is year-to-date through July 14, 2026, not a full-year count.",
            "- Counts should be used as context for trend hypotheses, then checked against actual prior conference corpora if publication claims depend on year-over-year change.",
        ]
    )
    report_path = REPORTS / "arxiv_taxonomy_trends.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {PROCESSED / 'arxiv_taxonomy_trend_counts.csv'}")
    print(f"Wrote {PROCESSED / 'arxiv_taxonomy_trend_summary.csv'}")
    print(f"Wrote {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
