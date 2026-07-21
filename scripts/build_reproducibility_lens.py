#!/usr/bin/env python3
"""Build a reproducibility and artifact-availability lens for ICML 2026."""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"


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


def github_repo_slug(url: str) -> str:
    if not url:
        return ""
    parsed = urlparse(url)
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) >= 2:
        return "/".join(parts[:2])
    return parsed.netloc + parsed.path


def is_likely_template_or_index(url: str) -> bool:
    lower = url.lower()
    return any(pattern in lower for pattern in SUSPICIOUS_REPO_PATTERNS)


def has_code_artifact(row: dict[str, str]) -> bool:
    return bool(row.get("github_url"))


def artifact_confidence(row: dict[str, str]) -> str:
    url = row.get("github_url", "")
    if not url:
        return "no_github_url"
    if is_likely_template_or_index(url):
        return "needs_manual_check"
    if intish(row.get("github_stars", "0")) > 0:
        return "github_url_with_stars"
    return "github_url_no_stars"


def summarize_group(rows: list[dict[str, str]], group_name: str, group_value: str) -> dict[str, object]:
    total = len(rows)
    with_url = [row for row in rows if row["has_github_url"] == "true"]
    likely_code = [row for row in rows if row["artifact_confidence"] in {"github_url_with_stars", "github_url_no_stars"}]
    needs_check = [row for row in rows if row["artifact_confidence"] == "needs_manual_check"]
    stars = sum(intish(row["github_stars"]) for row in rows)
    top = sorted(rows, key=lambda row: (intish(row["github_stars"]), intish(row["public_total_votes"])), reverse=True)[:5]
    return {
        "group_type": group_name,
        "group": group_value,
        "paper_count": total,
        "github_url_count": len(with_url),
        "github_url_share": round(len(with_url) / total, 4) if total else 0,
        "likely_code_count": len(likely_code),
        "likely_code_share": round(len(likely_code) / total, 4) if total else 0,
        "needs_manual_check_count": len(needs_check),
        "total_github_stars": stars,
        "top_artifact_papers": " | ".join(f"{row['title']} ({row['github_stars']} stars)" for row in top if row.get("github_url")),
    }


def main() -> int:
    alpha = read_csv(PROCESSED / "alphaxiv_icml2026_joined.csv")
    theme_rows = read_csv(PROCESSED / "icml2026_theme_matrix.csv")
    cluster_rows = read_csv(PROCESSED / "icml2026_cluster_assignments.csv")
    audience_rows = read_csv(PROCESSED / "icml2026_audience_reading_paths.csv")

    theme_by_title = {normalize_title(row["title"]): row for row in theme_rows}
    cluster_by_title = {normalize_title(row["title"]): row for row in cluster_rows}
    audience_by_title = defaultdict(list)
    for row in audience_rows:
        audience_by_title[normalize_title(row["title"])].append(row["audience"])

    paper_rows = []
    for row in alpha:
        key = normalize_title(row["title"])
        theme = theme_by_title.get(key, {})
        cluster = cluster_by_title.get(key, {})
        confidence = artifact_confidence(row)
        paper_rows.append(
            {
                "event_id": row.get("icml_id", ""),
                "title": row.get("title", ""),
                "topic_group": row.get("topic_group", "") or "Unknown",
                "topic": row.get("topic", ""),
                "themes": theme.get("themes", ""),
                "cluster_id": cluster.get("cluster_id", ""),
                "cluster_label": cluster.get("cluster_label", ""),
                "audience_paths": "; ".join(sorted(set(audience_by_title.get(key, [])))),
                "is_oral": row.get("is_oral", ""),
                "award": row.get("award", ""),
                "public_total_votes": intish(row.get("public_total_votes", "0")),
                "visits_last_7_days": intish(row.get("visits_last_7_days", "0")),
                "github_url": row.get("github_url", ""),
                "github_repo": github_repo_slug(row.get("github_url", "")),
                "github_stars": intish(row.get("github_stars", "0")),
                "has_github_url": str(has_code_artifact(row)).lower(),
                "artifact_confidence": confidence,
                "needs_manual_check_reason": "template_or_index_like_url" if confidence == "needs_manual_check" else "",
                "alphaxiv_url": row.get("alphaxiv_url", ""),
                "icml_url": row.get("icml_url", ""),
            }
        )

    write_csv(
        PROCESSED / "icml2026_reproducibility_papers.csv",
        paper_rows,
        [
            "event_id", "title", "topic_group", "topic", "themes", "cluster_id", "cluster_label",
            "audience_paths", "is_oral", "award", "public_total_votes", "visits_last_7_days",
            "github_url", "github_repo", "github_stars", "has_github_url", "artifact_confidence",
            "needs_manual_check_reason", "alphaxiv_url", "icml_url",
        ],
    )

    summary_rows = []
    summary_rows.append(summarize_group(paper_rows, "corpus", "all"))

    by_topic = defaultdict(list)
    by_theme = defaultdict(list)
    by_cluster = defaultdict(list)
    by_audience = defaultdict(list)
    for row in paper_rows:
        by_topic[row["topic_group"]].append(row)
        for theme in split_values(row["themes"]):
            by_theme[theme].append(row)
        cluster_key = f"{row['cluster_id']}: {row['cluster_label']}" if row["cluster_id"] else "Unknown"
        by_cluster[cluster_key].append(row)
        for audience in split_values(row["audience_paths"]):
            by_audience[audience].append(row)

    for group, rows in sorted(by_topic.items()):
        summary_rows.append(summarize_group(rows, "topic_group", group))
    for group, rows in sorted(by_theme.items()):
        summary_rows.append(summarize_group(rows, "theme", group))
    for group, rows in sorted(by_cluster.items()):
        summary_rows.append(summarize_group(rows, "cluster", group))
    for group, rows in sorted(by_audience.items()):
        summary_rows.append(summarize_group(rows, "audience_path", group))

    write_csv(
        PROCESSED / "icml2026_reproducibility_summary.csv",
        summary_rows,
        [
            "group_type", "group", "paper_count", "github_url_count", "github_url_share",
            "likely_code_count", "likely_code_share", "needs_manual_check_count",
            "total_github_stars", "top_artifact_papers",
        ],
    )

    top_github = sorted(
        [row for row in paper_rows if row["github_url"]],
        key=lambda row: (intish(row["github_stars"]), intish(row["public_total_votes"])),
        reverse=True,
    )[:50]
    write_csv(
        PROCESSED / "icml2026_top_github_artifacts.csv",
        top_github,
        [
            "event_id", "title", "topic_group", "topic", "themes", "cluster_id", "cluster_label",
            "audience_paths", "is_oral", "award", "public_total_votes", "visits_last_7_days",
            "github_url", "github_repo", "github_stars", "has_github_url", "artifact_confidence",
            "needs_manual_check_reason", "alphaxiv_url", "icml_url",
        ],
    )

    corpus = summary_rows[0]
    needs_check = [row for row in paper_rows if row["artifact_confidence"] == "needs_manual_check"]
    no_url_high_signal = sorted(
        [
            row for row in paper_rows
            if row["has_github_url"] != "true" and (row["award"] or row["is_oral"] == "true" or intish(row["public_total_votes"]) >= 100)
        ],
        key=lambda row: (bool(row["award"]), row["is_oral"] == "true", intish(row["public_total_votes"])),
        reverse=True,
    )[:40]

    lines = [
        "# ICML 2026 Reproducibility and Artifact Lens",
        "",
        "This report uses AlphaXiv GitHub metadata as a lightweight artifact-availability signal.",
        "It does not clone repositories, execute code, verify licenses, or confirm that linked repositories reproduce the paper.",
        "",
        "## Corpus Snapshot",
        "",
        f"- Papers: {corpus['paper_count']:,}",
        f"- Papers with GitHub URL: {corpus['github_url_count']:,} ({float(corpus['github_url_share']) * 100:.1f}%)",
        f"- Papers with likely code URL after simple template/index filtering: {corpus['likely_code_count']:,} ({float(corpus['likely_code_share']) * 100:.1f}%)",
        f"- GitHub URLs needing manual check: {corpus['needs_manual_check_count']:,}",
        f"- Total GitHub stars reported by AlphaXiv: {corpus['total_github_stars']:,}",
        "",
        "## Highest-Star GitHub Links",
        "",
    ]
    for row in top_github[:25]:
        caveat = " [manual-check]" if row["artifact_confidence"] == "needs_manual_check" else ""
        lines.append(
            f"- {row['title']} - {row['github_stars']} stars{caveat}; "
            f"{row['github_url']}"
        )

    lines.extend(["", "## Artifact Availability by Audience Path", ""])
    for row in sorted(
        [row for row in summary_rows if row["group_type"] == "audience_path"],
        key=lambda row: float(row["likely_code_share"]),
        reverse=True,
    ):
        lines.append(
            f"- {row['group']}: {row['github_url_count']}/{row['paper_count']} with GitHub URL "
            f"({float(row['github_url_share']) * 100:.1f}%); likely-code share {float(row['likely_code_share']) * 100:.1f}%"
        )

    lines.extend(["", "## Artifact Availability by Cluster", ""])
    for row in sorted(
        [row for row in summary_rows if row["group_type"] == "cluster"],
        key=lambda row: (float(row["likely_code_share"]), int(row["paper_count"])),
        reverse=True,
    )[:15]:
        lines.append(
            f"- {row['group']}: {row['github_url_count']}/{row['paper_count']} with GitHub URL; "
            f"likely-code share {float(row['likely_code_share']) * 100:.1f}%"
        )

    lines.extend(["", "## High-Signal Papers Without GitHub URL", ""])
    for row in no_url_high_signal[:30]:
        flags = [flag for flag in [row["award"], "oral" if row["is_oral"] == "true" else ""] if flag]
        flag_text = f" ({'; '.join(flags)})" if flags else ""
        lines.append(f"- {row['title']}{flag_text} - votes {row['public_total_votes']}; topic {row['topic_group']}")

    lines.extend(["", "## GitHub URLs Needing Manual Check", ""])
    for row in sorted(needs_check, key=lambda row: intish(row["github_stars"]), reverse=True)[:25]:
        lines.append(f"- {row['title']} - {row['github_stars']} stars; {row['github_url']}")

    lines.extend(
        [
            "",
            "## Caveats",
            "",
            "- GitHub metadata comes from AlphaXiv and is time-sensitive.",
            "- `needs_manual_check` flags links that look like project-page templates, awesome lists, homepages, or index repositories.",
            "- A GitHub URL does not imply runnable code, complete experiments, trained checkpoints, data release, or license clarity.",
            "- Missing GitHub URL does not imply non-reproducibility; code may be on another site, supplementary material, or released later.",
        ]
    )
    report_path = REPORTS / "icml2026_reproducibility_lens.md"
    REPORTS.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {PROCESSED / 'icml2026_reproducibility_papers.csv'}")
    print(f"Wrote {PROCESSED / 'icml2026_reproducibility_summary.csv'}")
    print(f"Wrote {PROCESSED / 'icml2026_top_github_artifacts.csv'}")
    print(f"Wrote {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
