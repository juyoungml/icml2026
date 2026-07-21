#!/usr/bin/env python3
"""Fetch AlphaXiv ICML 2026 community-signal data."""

from __future__ import annotations

import csv
import argparse
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "alphaxiv"
PROCESSED = ROOT / "data" / "processed"

API_BASE = "https://api.alphaxiv.org"
ICML_FEED = f"{API_BASE}/papers/v3/icml-feed"
ICML_TOPICS = f"{API_BASE}/papers/v3/icml-topics"


def fetch_json(url: str, retries: int = 3, timeout: int = 30) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "icml2026-eda/0.1"})
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except (TimeoutError, urllib.error.URLError) as exc:
            last_error = exc
            if attempt == retries:
                break
            time.sleep(1.5 * attempt)
    raise RuntimeError(f"Failed to fetch {url}: {last_error}")


def get_nested(obj: dict, path: list[str], default=None):
    cur = obj
    for key in path:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(key)
    return default if cur is None else cur


def fetch_pages(page_size: int = 30, max_pages: int | None = 10) -> tuple[list[dict], dict[str, dict], list[dict]]:
    items: list[dict] = []
    feed_by_group: dict[str, dict] = {}
    page_manifest: list[dict] = []
    page = 0
    while True:
        query = urllib.parse.urlencode({"page": page, "pageSize": page_size})
        print(f"Fetching AlphaXiv ICML page {page}...", flush=True)
        payload = fetch_json(f"{ICML_FEED}?{query}")
        (RAW / f"alphaxiv_icml_feed_page_{page:03d}.json").write_text(
            json.dumps(payload), encoding="utf-8"
        )
        page_manifest.append(
            {
                "page": payload.get("page", page),
                "items": len(payload.get("items", [])),
                "feed_papers": len(payload.get("feedPapers", [])),
                "has_more": bool(payload.get("hasMore")),
            }
        )
        items.extend(payload.get("items", []))
        for paper in payload.get("feedPapers", []):
            feed_by_group[paper.get("paper_group_id", "")] = paper
        if not payload.get("hasMore"):
            break
        if max_pages is not None and len(page_manifest) >= max_pages:
            break
        page = int(payload.get("page", page)) + 1
        time.sleep(0.15)
    return items, feed_by_group, page_manifest


def normalize_rows(items: list[dict], feed_by_group: dict[str, dict]) -> list[dict[str, object]]:
    rows = []
    for rank, item in enumerate(items, start=1):
        paper = feed_by_group.get(item.get("paperGroupId"), {})
        metrics = paper.get("metrics", {})
        visits = metrics.get("visits_count", {}) if isinstance(metrics, dict) else {}
        organizations = paper.get("organization_info") or []
        org_names = [org.get("name", "") for org in organizations if org.get("name")]
        rows.append(
            {
                "alphaxiv_rank": rank,
                "icml_id": item.get("icmlId"),
                "title": item.get("title", ""),
                "authors": "; ".join(item.get("authors") or []),
                "topic_group": item.get("topicGroup") or "",
                "topic": item.get("topic") or "",
                "session": item.get("session") or "",
                "scheduled_at": item.get("scheduledAt") or "",
                "icml_url": item.get("icmlUrl") or "",
                "alphaxiv_url": f"https://www.alphaxiv.org/abs/{item.get('universalId')}" if item.get("universalId") else "",
                "arxiv_id": item.get("universalId") or "",
                "paper_group_id": item.get("paperGroupId") or "",
                "public_total_votes": get_nested(paper, ["metrics", "public_total_votes"], 0),
                "total_votes": get_nested(paper, ["metrics", "total_votes"], 0),
                "visits_all": visits.get("all", 0),
                "visits_last_7_days": visits.get("last_7_days", 0),
                "github_stars": paper.get("github_stars") or 0,
                "github_url": paper.get("github_url") or "",
                "organizations": "; ".join(org_names),
                "abstract": item.get("abstract", ""),
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write: {path}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--page-size", type=int, default=30)
    parser.add_argument("--max-pages", type=int, default=10)
    parser.add_argument("--all", action="store_true", help="Fetch every AlphaXiv ICML feed page.")
    args = parser.parse_args()

    RAW.mkdir(parents=True, exist_ok=True)
    PROCESSED.mkdir(parents=True, exist_ok=True)

    topics = fetch_json(ICML_TOPICS)
    max_pages = None if args.all else args.max_pages
    items, feed_by_group, page_manifest = fetch_pages(page_size=args.page_size, max_pages=max_pages)
    rows = normalize_rows(items, feed_by_group)

    (RAW / "alphaxiv_icml_topics.json").write_text(json.dumps(topics, indent=2), encoding="utf-8")
    (RAW / "alphaxiv_icml_feed_pages_manifest.json").write_text(
        json.dumps(page_manifest, indent=2), encoding="utf-8"
    )
    write_csv(PROCESSED / "alphaxiv_icml2026_papers.csv", rows)
    (PROCESSED / "alphaxiv_icml2026_papers.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")

    metadata = {
        "snapshot_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "sources": {"feed": ICML_FEED, "topics": ICML_TOPICS},
        "row_count": len(rows),
        "page_size": args.page_size,
        "max_pages": max_pages,
        "pages_fetched": len(page_manifest),
        "is_complete_feed": bool(page_manifest and not page_manifest[-1].get("has_more")),
        "topic_group_count": len(topics.get("topicGroups", [])),
        "notes": [
            "AlphaXiv rank is page/feed order from /papers/v3/icml-feed at fetch time.",
            "Default run is a seed snapshot. Use --all for a complete feed fetch.",
            "Vote and visit counts are community attention signals, not quality labels.",
        ],
    }
    (PROCESSED / "alphaxiv_icml2026_metadata.json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8"
    )

    print(f"Fetched {len(rows)} AlphaXiv ICML rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
