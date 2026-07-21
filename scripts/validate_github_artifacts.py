#!/usr/bin/env python3
"""Validate a bounded set of GitHub artifact links via the GitHub API."""

from __future__ import annotations

import argparse
import csv
import json
import re
import time
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
RAW = ROOT / "data" / "raw"
REPORTS = ROOT / "reports"
CACHE_PATH = RAW / "github_artifact_validation_cache.json"

SUSPICIOUS_REPO_PATTERNS = [
    "academic-project-page-template",
    "academicpages",
    "awesome-",
    "project-page",
    "homepage",
    "website",
    "template",
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


def intish(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def repo_slug(url: str) -> str:
    if not url:
        return ""
    parsed = urlparse(url)
    if parsed.netloc.lower() not in {"github.com", "www.github.com"}:
        return ""
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2:
        return ""
    return f"{parts[0]}/{parts[1]}"


def suspicious_reason(slug: str, url: str) -> str:
    lower = f"{slug} {url}".lower()
    matches = [pattern for pattern in SUSPICIOUS_REPO_PATTERNS if pattern in lower]
    return "; ".join(matches)


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


def github_api_get(slug: str) -> dict[str, object]:
    url = f"https://api.github.com/repos/{slug}"
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "icml2026-eda-artifact-validator",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            data = json.loads(response.read().decode("utf-8"))
            return {
                "status": "ok",
                "http_status": response.status,
                "rate_limit_remaining": response.headers.get("x-ratelimit-remaining", ""),
                "fetched_utc": datetime.now(timezone.utc).isoformat(),
                "data": data,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")[:500]
        return {
            "status": "http_error",
            "http_status": exc.code,
            "error": body,
            "fetched_utc": datetime.now(timezone.utc).isoformat(),
        }
    except Exception as exc:  # noqa: BLE001 - script should keep auditing other repos.
        return {
            "status": "error",
            "http_status": "",
            "error": f"{type(exc).__name__}: {exc}",
            "fetched_utc": datetime.now(timezone.utc).isoformat(),
        }


def select_candidates(limit: int) -> list[dict[str, str]]:
    top_rows = read_csv(PROCESSED / "icml2026_top_github_artifacts.csv")
    validation_rows = read_csv(PROCESSED / "icml2026_manual_validation_queue.csv")
    selected: dict[str, dict[str, object]] = {}

    def add(row: dict[str, str], source: str) -> None:
        slug = row.get("github_repo") or repo_slug(row.get("github_url", ""))
        if not slug:
            return
        item = selected.setdefault(
            slug,
            {
                "github_repo": slug,
                "github_url": row.get("github_url", f"https://github.com/{slug}"),
                "sources": set(),
                "paper_titles": [],
                "max_public_votes": 0,
                "max_alphaxiv_stars": 0,
                "artifact_confidence": row.get("artifact_confidence", ""),
            },
        )
        item["sources"].add(source)
        title = row.get("title", "")
        if title and title not in item["paper_titles"]:
            item["paper_titles"].append(title)
        item["max_public_votes"] = max(int(item["max_public_votes"]), intish(row.get("public_total_votes", "0")))
        item["max_alphaxiv_stars"] = max(int(item["max_alphaxiv_stars"]), intish(row.get("github_stars", "0")))
        if not item.get("artifact_confidence"):
            item["artifact_confidence"] = row.get("artifact_confidence", "")

    for row in top_rows:
        add(row, "top_github_artifacts")
        if len(selected) >= limit:
            break

    for row in sorted(validation_rows, key=lambda r: intish(r.get("public_total_votes", "0")), reverse=True):
        if len(selected) >= limit:
            break
        add(row, "manual_validation_queue")

    output = []
    for item in selected.values():
        row = dict(item)
        row["sources"] = "; ".join(sorted(row["sources"]))
        row["paper_titles"] = " | ".join(row["paper_titles"][:8])
        output.append(row)
    output.sort(key=lambda row: (int(row["max_alphaxiv_stars"]), int(row["max_public_votes"])), reverse=True)
    return output[:limit]


def repo_age_days(value: str) -> int | str:
    if not value:
        return ""
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return ""
    return (datetime.now(timezone.utc) - dt).days


def row_from_result(candidate: dict[str, object], result: dict[str, object]) -> dict[str, object]:
    slug = str(candidate["github_repo"])
    data = result.get("data") if isinstance(result.get("data"), dict) else {}
    license_data = data.get("license") if isinstance(data.get("license"), dict) else {}
    pushed_at = str(data.get("pushed_at", "") or "")
    updated_at = str(data.get("updated_at", "") or "")
    suspicious = suspicious_reason(slug, str(candidate["github_url"]))
    live_status = "live" if result.get("status") == "ok" else f"{result.get('status')}:{result.get('http_status')}"
    qa_flags = []
    if suspicious:
        qa_flags.append("suspicious_template_or_index")
    if data.get("archived"):
        qa_flags.append("archived")
    if data.get("disabled"):
        qa_flags.append("disabled")
    if data.get("fork"):
        qa_flags.append("fork")
    pushed_age = repo_age_days(pushed_at)
    if isinstance(pushed_age, int) and pushed_age > 730:
        qa_flags.append("stale_pushed_at")
    if result.get("status") != "ok":
        qa_flags.append("not_live_or_api_error")
    return {
        "github_repo": slug,
        "github_url": candidate["github_url"],
        "live_status": live_status,
        "http_status": result.get("http_status", ""),
        "qa_flags": "; ".join(qa_flags),
        "suspicious_reason": suspicious,
        "paper_titles": candidate["paper_titles"],
        "sources": candidate["sources"],
        "max_public_votes": candidate["max_public_votes"],
        "alphaxiv_github_stars": candidate["max_alphaxiv_stars"],
        "live_stargazers_count": data.get("stargazers_count", ""),
        "live_forks_count": data.get("forks_count", ""),
        "open_issues_count": data.get("open_issues_count", ""),
        "archived": str(bool(data.get("archived"))).lower() if data else "",
        "disabled": str(bool(data.get("disabled"))).lower() if data else "",
        "fork": str(bool(data.get("fork"))).lower() if data else "",
        "license_spdx": license_data.get("spdx_id", "") if license_data else "",
        "default_branch": data.get("default_branch", ""),
        "created_at": data.get("created_at", ""),
        "updated_at": updated_at,
        "pushed_at": pushed_at,
        "pushed_age_days": pushed_age,
        "description": data.get("description", ""),
        "homepage": data.get("homepage", ""),
        "api_fetched_utc": result.get("fetched_utc", ""),
        "api_error": result.get("error", ""),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=50, help="Maximum unique GitHub repos to validate.")
    parser.add_argument("--refresh", action="store_true", help="Ignore cached GitHub API responses.")
    parser.add_argument("--sleep", type=float, default=0.25, help="Seconds to sleep between uncached API calls.")
    args = parser.parse_args()

    candidates = select_candidates(args.limit)
    cache = load_cache()
    rows = []
    fetched = 0
    for candidate in candidates:
        slug = str(candidate["github_repo"])
        if not args.refresh and slug in cache:
            result = cache[slug]
        else:
            result = github_api_get(slug)
            cache[slug] = result
            fetched += 1
            time.sleep(args.sleep)
        rows.append(row_from_result(candidate, result))
    save_cache(cache)

    write_csv(
        PROCESSED / "icml2026_github_artifact_live_check.csv",
        rows,
        [
            "github_repo", "github_url", "live_status", "http_status", "qa_flags",
            "suspicious_reason", "paper_titles", "sources", "max_public_votes",
            "alphaxiv_github_stars", "live_stargazers_count", "live_forks_count",
            "open_issues_count", "archived", "disabled", "fork", "license_spdx",
            "default_branch", "created_at", "updated_at", "pushed_at", "pushed_age_days",
            "description", "homepage", "api_fetched_utc", "api_error",
        ],
    )

    live_count = sum(row["live_status"] == "live" for row in rows)
    flagged = [row for row in rows if row["qa_flags"]]
    lines = [
        "# ICML 2026 GitHub Artifact Live Check",
        "",
        "This is a bounded live QA pass over high-signal GitHub artifact links.",
        "It uses the GitHub repository API and does not clone repositories, install dependencies, or run code.",
        "",
        "## Snapshot",
        "",
        f"- Repositories checked: {len(rows)}",
        f"- API responses fetched this run: {fetched}",
        f"- Live repositories: {live_count}",
        f"- Repositories with QA flags: {len(flagged)}",
        f"- Cache file: `{CACHE_PATH.relative_to(ROOT)}`",
        "",
        "## Flagged Repositories",
        "",
    ]
    for row in flagged[:30]:
        lines.append(
            f"- {row['github_repo']}: {row['qa_flags']}; "
            f"papers: {str(row['paper_titles']).split(' | ')[0]}"
        )
    if not flagged:
        lines.append("- None.")

    lines.extend(["", "## Highest Live-Star Repositories", ""])
    for row in sorted(rows, key=lambda r: intish(str(r["live_stargazers_count"])), reverse=True)[:20]:
        lines.append(
            f"- {row['github_repo']}: {row['live_stargazers_count']} stars; "
            f"license {row['license_spdx'] or 'unknown'}; pushed {row['pushed_at'] or 'unknown'}"
        )

    lines.extend(
        [
            "",
            "## Caveats",
            "",
            "- A live repository does not imply runnable code, complete data, trained checkpoints, or reproducibility.",
            "- GitHub API metadata is time-sensitive.",
            "- Template, homepage, and awesome-list repositories are flagged because they can inflate star-based artifact signals.",
            "- This script intentionally validates only a bounded candidate set to avoid GitHub API rate-limit surprises.",
        ]
    )
    report_path = REPORTS / "icml2026_github_artifact_live_check.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {PROCESSED / 'icml2026_github_artifact_live_check.csv'}")
    print(f"Wrote {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
