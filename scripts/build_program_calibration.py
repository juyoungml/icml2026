#!/usr/bin/env python3
"""Calibrate ICML program signal against taxonomy size and public attention."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"


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


def ratio(value: float, baseline: float) -> float:
    if baseline <= 0:
        return 0.0
    return value / baseline


def summarize_group(
    name: str,
    rows: list[dict[str, str]],
    corpus_count: int,
    corpus_oral_count: int,
    corpus_award_count: int,
    corpus_votes: int,
) -> dict[str, object]:
    paper_count = len(rows)
    oral_count = sum(row["is_oral"] == "true" for row in rows)
    award_count = sum(bool(row["award"]) for row in rows)
    votes = sum(intish(row["public_total_votes"]) for row in rows)
    paper_share = paper_count / corpus_count if corpus_count else 0
    oral_share = oral_count / corpus_oral_count if corpus_oral_count else 0
    award_share = award_count / corpus_award_count if corpus_award_count else 0
    vote_share = votes / corpus_votes if corpus_votes else 0
    oral_rate = oral_count / paper_count if paper_count else 0
    award_rate = award_count / paper_count if paper_count else 0
    votes_per_paper = votes / paper_count if paper_count else 0
    high_signal = sorted(
        rows,
        key=lambda row: (
            bool(row["award"]),
            row["is_oral"] == "true",
            intish(row["public_total_votes"]),
        ),
        reverse=True,
    )[:8]
    public_not_program = [
        row for row in sorted(rows, key=lambda r: intish(r["public_total_votes"]), reverse=True)
        if row["is_oral"] != "true" and not row["award"]
    ][:8]
    program_low_public = [
        row for row in sorted(rows, key=lambda r: intish(r["public_total_votes"]))
        if row["is_oral"] == "true" or row["award"]
    ][:8]
    return {
        "group": name,
        "paper_count": paper_count,
        "paper_share": round(paper_share, 4),
        "oral_count": oral_count,
        "oral_rate": round(oral_rate, 4),
        "oral_share": round(oral_share, 4),
        "oral_enrichment": round(ratio(oral_share, paper_share), 2) if paper_share else 0,
        "award_count": award_count,
        "award_rate": round(award_rate, 4),
        "award_share": round(award_share, 4),
        "award_enrichment": round(ratio(award_share, paper_share), 2) if paper_share else 0,
        "total_public_votes": votes,
        "votes_per_paper": round(votes_per_paper, 2),
        "public_vote_share": round(vote_share, 4),
        "public_attention_enrichment": round(ratio(vote_share, paper_share), 2) if paper_share else 0,
        "program_vs_public_delta": round(ratio(oral_share, paper_share) - ratio(vote_share, paper_share), 2) if paper_share else 0,
        "high_signal_papers": " | ".join(row["title"] for row in high_signal),
        "public_not_program_papers": " | ".join(row["title"] for row in public_not_program),
        "program_low_public_papers": " | ".join(row["title"] for row in program_low_public),
    }


def main() -> int:
    papers = read_csv(PROCESSED / "icml2026_manual_taxonomy_papers.csv")
    clusters = read_csv(PROCESSED / "icml2026_manual_taxonomy_clusters.csv")
    cluster_meta = {row["semantic_cluster_id"]: row for row in clusters}
    corpus_count = len(papers)
    corpus_oral_count = sum(row["is_oral"] == "true" for row in papers)
    corpus_award_count = sum(bool(row["award"]) for row in papers)
    corpus_votes = sum(intish(row["public_total_votes"]) for row in papers)

    by_area: dict[str, list[dict[str, str]]] = defaultdict(list)
    by_cluster: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in papers:
        by_area[row["area"]].append(row)
        by_cluster[row["semantic_cluster_id"]].append(row)

    area_rows = [
        summarize_group(area, rows, corpus_count, corpus_oral_count, corpus_award_count, corpus_votes)
        for area, rows in sorted(by_area.items())
    ]
    area_rows.sort(key=lambda row: (-float(row["oral_enrichment"]), -int(row["oral_count"]), str(row["group"])))

    cluster_rows = []
    for cluster_id, rows in sorted(by_cluster.items(), key=lambda item: int(item[0])):
        summary = summarize_group(
            f"{cluster_id}: {cluster_meta.get(cluster_id, {}).get('semantic_cluster_label', '')}",
            rows,
            corpus_count,
            corpus_oral_count,
            corpus_award_count,
            corpus_votes,
        )
        summary["semantic_cluster_id"] = cluster_id
        summary["area"] = cluster_meta.get(cluster_id, {}).get("area", "")
        summary["subarea"] = cluster_meta.get(cluster_id, {}).get("subarea", "")
        summary["review_status"] = cluster_meta.get(cluster_id, {}).get("review_status", "")
        cluster_rows.append(summary)
    cluster_rows.sort(key=lambda row: (-float(row["oral_enrichment"]), -int(row["oral_count"]), str(row["group"])))

    fieldnames = [
        "group", "paper_count", "paper_share", "oral_count", "oral_rate", "oral_share",
        "oral_enrichment", "award_count", "award_rate", "award_share", "award_enrichment",
        "total_public_votes", "votes_per_paper", "public_vote_share",
        "public_attention_enrichment", "program_vs_public_delta",
        "high_signal_papers", "public_not_program_papers", "program_low_public_papers",
    ]
    write_csv(PROCESSED / "icml2026_area_program_calibration.csv", area_rows, fieldnames)
    write_csv(
        PROCESSED / "icml2026_cluster_program_calibration.csv",
        cluster_rows,
        ["semantic_cluster_id", "area", "subarea", "review_status"] + fieldnames,
    )

    award_counts = Counter(row["award"] for row in papers if row["award"])
    lines = [
        "# ICML 2026 Program Signal Calibration",
        "",
        "This report compares program signal (oral/award selection) against taxonomy size and AlphaXiv public attention.",
        "",
        "## Corpus Baselines",
        "",
        f"- Papers: {corpus_count:,}",
        f"- Oral-designated papers: {corpus_oral_count:,} ({corpus_oral_count / corpus_count * 100:.2f}%)",
        f"- Award rows: {corpus_award_count:,}",
        "- Award calibration excludes the Test of Time Award because it is not an ICML 2026 paper-row in the taxonomy.",
        f"- Public votes: {corpus_votes:,}",
        f"- Award mix: {', '.join(f'{k}: {v}' for k, v in award_counts.items())}",
        "",
        "## Area Calibration",
        "",
    ]
    for row in area_rows:
        lines.append(f"### {row['group']}")
        lines.append(
            f"- Papers: {row['paper_count']} ({float(row['paper_share']) * 100:.1f}%); "
            f"orals: {row['oral_count']} ({float(row['oral_rate']) * 100:.1f}%); "
            f"awards: {row['award_count']}; votes/paper: {row['votes_per_paper']}"
        )
        lines.append(
            f"- Oral enrichment: {row['oral_enrichment']}x; award enrichment: {row['award_enrichment']}x; "
            f"public-attention enrichment: {row['public_attention_enrichment']}x; "
            f"program-vs-public delta: {row['program_vs_public_delta']}"
        )
        lines.append(f"- High-signal papers: {row['high_signal_papers']}")
        lines.append("")

    lines.extend(["## Highest Oral-Enriched Semantic Clusters", ""])
    for row in [row for row in cluster_rows if int(row["oral_count"]) > 0][:15]:
        lines.append(
            f"- {row['group']} ({row['area']}): {row['oral_enrichment']}x oral enrichment, "
            f"{row['oral_count']} orals / {row['paper_count']} papers; votes/paper {row['votes_per_paper']}"
        )

    lines.extend(["", "## Public Attention Ahead Of Program Signal", ""])
    for row in sorted(area_rows, key=lambda r: float(r["public_attention_enrichment"]) - float(r["oral_enrichment"]), reverse=True)[:8]:
        lines.append(
            f"- {row['group']}: public enrichment {row['public_attention_enrichment']}x vs oral enrichment {row['oral_enrichment']}x; "
            f"examples: {row['public_not_program_papers']}"
        )

    lines.extend(["", "## Program Signal Ahead Of Public Attention", ""])
    for row in sorted(area_rows, key=lambda r: float(r["program_vs_public_delta"]), reverse=True)[:8]:
        lines.append(
            f"- {row['group']}: oral enrichment {row['oral_enrichment']}x vs public enrichment {row['public_attention_enrichment']}x; "
            f"examples: {row['program_low_public_papers']}"
        )

    lines.extend(
        [
            "",
            "## Caveats",
            "",
            "- Oral and award labels are program signals, not complete quality labels.",
            "- Award counts are small, so award enrichment is volatile.",
            "- AlphaXiv public votes are attention signals and are biased toward shareable LLM/agent/systems work.",
            "- Taxonomy assignments are curated seeds; clusters marked `needs_review` should be checked before using fine-grained calibration claims.",
        ]
    )
    report_path = REPORTS / "icml2026_program_signal_calibration.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {PROCESSED / 'icml2026_area_program_calibration.csv'}")
    print(f"Wrote {PROCESSED / 'icml2026_cluster_program_calibration.csv'}")
    print(f"Wrote {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
