#!/usr/bin/env python3
"""Analyze AlphaXiv ICML community signals and join ICML flags."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def normalize_title(title: str) -> str:
    title = title.lower()
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def main() -> int:
    alpha = read_csv(PROCESSED / "alphaxiv_icml2026_papers.csv")
    icml = read_csv(PROCESSED / "icml2026_papers.csv")
    awards = read_csv(PROCESSED / "icml2026_awards.csv")

    icml_by_title = {normalize_title(row["title"]): row for row in icml}
    icml_by_event_id = {row["event_id"]: row for row in icml}
    award_titles = {normalize_title(row["title"]): row["award"] for row in awards}

    for row in alpha:
        match = icml_by_event_id.get(row.get("icml_id", "")) or icml_by_title.get(normalize_title(row["title"]))
        row["matched_icml"] = "true" if match else "false"
        row["is_oral"] = match.get("is_oral", "false") if match else "false"
        row["is_position"] = match.get("is_position", "false") if match else "false"
        row["award"] = award_titles.get(normalize_title(row["title"]), "")

    top_votes = sorted(alpha, key=lambda r: int(r["public_total_votes"] or 0), reverse=True)[:25]
    top_recent = sorted(alpha, key=lambda r: int(r["visits_last_7_days"] or 0), reverse=True)[:25]
    topic_counts = Counter(row["topic_group"] or "Unknown" for row in alpha)
    matched_count = sum(row["matched_icml"] == "true" for row in alpha)
    oral_count = sum(row["is_oral"] == "true" for row in alpha)
    award_overlap = [row for row in alpha if row["award"]]

    joined_path = PROCESSED / "alphaxiv_icml2026_joined.csv"
    with joined_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(alpha[0].keys()))
        writer.writeheader()
        writer.writerows(alpha)

    lines = [
        "# AlphaXiv ICML 2026 Community-Signal EDA",
        "",
        "Source: AlphaXiv `GET /papers/v3/icml-feed` and official ICML virtual corpus.",
        "",
        "## Corpus",
        "",
        f"- AlphaXiv ICML rows: {len(alpha):,}",
        f"- Matched to official ICML titles: {matched_count:,}",
        f"- Oral-designated among AlphaXiv rows: {oral_count:,}",
        f"- Official award overlap: {len(award_overlap):,}",
        "",
        "## Topic Groups",
        "",
    ]
    for topic, count in topic_counts.most_common():
        lines.append(f"- {topic}: {count:,}")

    lines.extend(["", "## Top Papers by Public Votes", ""])
    for idx, row in enumerate(top_votes, start=1):
        flags = []
        if row["is_oral"] == "true":
            flags.append("oral")
        if row["award"]:
            flags.append(row["award"])
        flag_text = f" ({'; '.join(flags)})" if flags else ""
        lines.append(
            f"{idx}. {row['title']}{flag_text} - {row['public_total_votes']} public votes, "
            f"{row['visits_all']} all-time visits, topic: {row['topic_group']}"
        )

    lines.extend(["", "## Top Papers by Last-7-Day Visits", ""])
    for idx, row in enumerate(top_recent, start=1):
        lines.append(
            f"{idx}. {row['title']} - {row['visits_last_7_days']} visits in last 7 days, "
            f"{row['public_total_votes']} public votes"
        )

    lines.extend(["", "## Official Award Overlap", ""])
    if award_overlap:
        for row in award_overlap:
            lines.append(f"- {row['title']} - {row['award']}; {row['public_total_votes']} public votes")
    else:
        lines.append("- No official award papers matched in the current AlphaXiv ICML feed.")

    lines.extend(
        [
            "",
            "## Interpretation Seeds",
            "",
            "- AlphaXiv's ICML feed has rich topic labels and community metrics, useful for public-attention analysis.",
            "- `public_total_votes` and visits should be presented as attention signals, not paper quality.",
            "- Compare high-vote papers against oral and award flags to surface community/committee divergence.",
            "- The current feed order is not assumed to be a vote ranking; explicit rank analyses should sort by the desired metric.",
        ]
    )

    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "alphaxiv_icml2026_eda.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {joined_path}")
    print(f"Wrote {REPORTS / 'alphaxiv_icml2026_eda.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
