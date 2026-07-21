#!/usr/bin/env python3
"""Build a compact paper-level explorer table for ICML 2026."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"


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


def main() -> int:
    taxonomy = read_csv(PROCESSED / "icml2026_manual_taxonomy_papers.csv")
    evidence = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_paper_evidence_codes.csv")}
    repro = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_reproducibility_papers.csv")}
    official = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_papers.csv")}

    rows = []
    for row in taxonomy:
        ev = evidence.get(row["event_id"], {})
        rp = repro.get(row["event_id"], {})
        off = official.get(row["event_id"], {})
        has_github = row.get("github_url") or rp.get("github_url")
        needs_manual = rp.get("needs_manual_check_reason", "")
        signal_score = (
            (100000 if row.get("award") else 0)
            + (10000 if row.get("is_oral") == "true" else 0)
            + intish(row.get("public_total_votes"))
            + intish(row.get("visits_last_7_days"))
            + min(intish(rp.get("github_stars")), 5000)
        )
        rows.append(
            {
                "event_id": row["event_id"],
                "title": row["title"],
                "area": row["area"],
                "subarea": row["subarea"],
                "semantic_cluster_id": row["semantic_cluster_id"],
                "semantic_cluster_label": row["semantic_cluster_label"],
                "taxonomy_confidence": row["taxonomy_confidence"],
                "review_status": row["review_status"],
                "topic_group": row["topic_group"],
                "topic": row["topic"],
                "is_oral": row["is_oral"],
                "award": row["award"],
                "public_total_votes": intish(row["public_total_votes"]),
                "visits_last_7_days": intish(row["visits_last_7_days"]),
                "github_url": has_github,
                "github_repo": rp.get("github_repo", ""),
                "github_stars": intish(rp.get("github_stars", "")),
                "artifact_confidence": row.get("artifact_confidence") or rp.get("artifact_confidence", ""),
                "needs_manual_check_reason": needs_manual,
                "primary_contribution_type": ev.get("primary_contribution_type", ""),
                "method_families": ev.get("method_families", ""),
                "evaluation_settings": ev.get("evaluation_settings", ""),
                "benchmark_mentions": ev.get("benchmark_mentions", ""),
                "dataset_mentions": ev.get("dataset_mentions", ""),
                "metric_mentions": ev.get("metric_mentions", ""),
                "evidence_confidence": ev.get("evidence_confidence", ""),
                "author_count": off.get("author_count", ""),
                "institution_count": off.get("institution_count", ""),
                "url": row["url"],
                "alphaxiv_url": row["alphaxiv_url"],
                "signal_score": signal_score,
            }
        )

    rows.sort(key=lambda item: (-int(item["signal_score"]), str(item["area"]), str(item["title"])))
    write_csv(
        PROCESSED / "icml2026_paper_explorer.csv",
        rows,
        [
            "event_id", "title", "area", "subarea", "semantic_cluster_id", "semantic_cluster_label",
            "taxonomy_confidence", "review_status", "topic_group", "topic", "is_oral", "award",
            "public_total_votes", "visits_last_7_days", "github_url", "github_repo", "github_stars",
            "artifact_confidence", "needs_manual_check_reason", "primary_contribution_type",
            "method_families", "evaluation_settings", "benchmark_mentions", "dataset_mentions",
            "metric_mentions", "evidence_confidence", "author_count", "institution_count",
            "url", "alphaxiv_url", "signal_score",
        ],
    )
    print(f"Wrote {PROCESSED / 'icml2026_paper_explorer.csv'} ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
