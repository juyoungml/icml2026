#!/usr/bin/env python3
"""Build ICML 2026 author, institution, and collaboration landscape artifacts."""

from __future__ import annotations

import csv
import html
import itertools
import re
from collections import Counter, defaultdict
from pathlib import Path

import networkx as nx

from build_researcher_landscape import affiliation_sector, canonical_affiliation


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"


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


def normalize_title(title: str) -> str:
    title = title.lower()
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def split_semicolon(value: str) -> list[str]:
    value = html.unescape(html.unescape(value or ""))
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def normalize_author(name: str) -> str:
    name = html.unescape(html.unescape(name or ""))
    name = re.sub(r"\s+", " ", name).strip()
    name = name.replace(" ,", ",").replace(" .", ".")
    return name


def intish(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def weighted_degree_rows(graph: nx.Graph, key_a: str, key_b: str, limit: int) -> list[dict[str, object]]:
    rows = []
    for left, right, data in sorted(graph.edges(data=True), key=lambda item: item[2].get("weight", 0), reverse=True)[:limit]:
        rows.append({key_a: left, key_b: right, "shared_paper_count": data.get("weight", 0)})
    return rows


def top_counter(counter: Counter, limit: int = 5) -> str:
    return "; ".join(f"{key} ({value})" for key, value in counter.most_common(limit))


def main() -> int:
    papers = read_csv(PROCESSED / "icml2026_papers.csv")
    themes = read_csv(PROCESSED / "icml2026_theme_matrix.csv")
    clusters = read_csv(PROCESSED / "icml2026_cluster_assignments.csv")
    alpha = read_csv(PROCESSED / "alphaxiv_icml2026_joined.csv")
    if not papers:
        raise SystemExit("Run scripts/fetch_icml_virtual.py first.")
    if not themes:
        raise SystemExit("Run scripts/build_researcher_landscape.py first.")
    if not clusters:
        raise SystemExit("Run scripts/build_cluster_landscape.py first.")

    theme_by_title = {normalize_title(row["title"]): row for row in themes}
    cluster_by_title = {normalize_title(row["title"]): row for row in clusters}
    alpha_by_title = {normalize_title(row["title"]): row for row in alpha}

    author_stats: dict[str, dict[str, object]] = {}
    inst_stats: dict[str, dict[str, object]] = {}
    author_graph = nx.Graph()
    inst_graph = nx.Graph()
    sector_edge_counts = Counter()
    sector_mix_counts = Counter()
    paper_rows = []

    for paper in papers:
        key = normalize_title(paper["title"])
        theme_row = theme_by_title.get(key, {})
        cluster_row = cluster_by_title.get(key, {})
        alpha_row = alpha_by_title.get(key, {})
        authors = [normalize_author(author) for author in split_semicolon(paper.get("authors", ""))]
        authors = [author for author in authors if author]
        institutions = sorted(
            {
                canonical_affiliation(inst)
                for inst in split_semicolon(paper.get("institutions", ""))
                if canonical_affiliation(inst)
            }
        )
        sectors = sorted({affiliation_sector(inst) for inst in institutions})
        sector_mix_counts[" + ".join(sectors) if sectors else "Unknown"] += 1
        is_oral = paper.get("is_oral") == "true"
        award = theme_row.get("award", "")
        votes = intish(alpha_row.get("public_total_votes", "0"))
        recent = intish(alpha_row.get("visits_last_7_days", "0"))
        cluster_id = cluster_row.get("cluster_id", "")
        cluster_label = cluster_row.get("cluster_label", "")
        theme_values = [theme for theme in split_semicolon(theme_row.get("themes", "")) if theme]

        paper_rows.append(
            {
                "event_id": paper.get("event_id", ""),
                "title": paper.get("title", ""),
                "author_count": len(authors),
                "canonical_institution_count": len(institutions),
                "sector_mix": "; ".join(sectors),
                "has_industry": "Industry" in sectors,
                "has_academia": "Academia" in sectors,
                "has_research_institute": "Research institute" in sectors,
                "has_industry_academia": "Industry" in sectors and "Academia" in sectors,
                "cluster_id": cluster_id,
                "cluster_label": cluster_label,
                "themes": "; ".join(theme_values),
                "is_oral": str(is_oral).lower(),
                "award": award,
                "public_total_votes": votes,
                "visits_last_7_days": recent,
                "canonical_institutions": "; ".join(institutions),
                "authors": "; ".join(authors),
                "url": paper.get("url", ""),
            }
        )

        for author in authors:
            author_graph.add_node(author)
            stats = author_stats.setdefault(
                author,
                {
                    "paper_count": 0,
                    "oral_count": 0,
                    "award_count": 0,
                    "public_total_votes": 0,
                    "visits_last_7_days": 0,
                    "topics": Counter(),
                    "themes": Counter(),
                    "clusters": Counter(),
                    "institutions": Counter(),
                    "coauthors": Counter(),
                },
            )
            stats["paper_count"] += 1
            stats["oral_count"] += int(is_oral)
            stats["award_count"] += int(bool(award))
            stats["public_total_votes"] += votes
            stats["visits_last_7_days"] += recent
            stats["topics"][paper.get("topic_group", "") or "Unknown"] += 1
            for theme in theme_values:
                stats["themes"][theme] += 1
            if cluster_label:
                stats["clusters"][f"{cluster_id}: {cluster_label}"] += 1
            for inst in institutions:
                stats["institutions"][inst] += 1
            for coauthor in authors:
                if coauthor != author:
                    stats["coauthors"][coauthor] += 1

        for author_a, author_b in itertools.combinations(sorted(set(authors)), 2):
            if author_graph.has_edge(author_a, author_b):
                author_graph[author_a][author_b]["weight"] += 1
            else:
                author_graph.add_edge(author_a, author_b, weight=1)

        for inst in institutions:
            inst_graph.add_node(inst)
            stats = inst_stats.setdefault(
                inst,
                {
                    "paper_count": 0,
                    "oral_count": 0,
                    "award_count": 0,
                    "public_total_votes": 0,
                    "visits_last_7_days": 0,
                    "topics": Counter(),
                    "themes": Counter(),
                    "clusters": Counter(),
                    "partners": Counter(),
                    "sector": affiliation_sector(inst),
                },
            )
            stats["paper_count"] += 1
            stats["oral_count"] += int(is_oral)
            stats["award_count"] += int(bool(award))
            stats["public_total_votes"] += votes
            stats["visits_last_7_days"] += recent
            stats["topics"][paper.get("topic_group", "") or "Unknown"] += 1
            for theme in theme_values:
                stats["themes"][theme] += 1
            if cluster_label:
                stats["clusters"][f"{cluster_id}: {cluster_label}"] += 1

        for inst_a, inst_b in itertools.combinations(institutions, 2):
            if inst_graph.has_edge(inst_a, inst_b):
                inst_graph[inst_a][inst_b]["weight"] += 1
            else:
                inst_graph.add_edge(inst_a, inst_b, weight=1)
            inst_stats[inst_a]["partners"][inst_b] += 1
            inst_stats[inst_b]["partners"][inst_a] += 1
            sector_edge = " + ".join(sorted([affiliation_sector(inst_a), affiliation_sector(inst_b)]))
            sector_edge_counts[sector_edge] += 1

    author_pagerank = nx.pagerank(author_graph, weight="weight") if author_graph.number_of_edges() else {}
    inst_pagerank = nx.pagerank(inst_graph, weight="weight") if inst_graph.number_of_edges() else {}

    author_rows = []
    for author, stats in author_stats.items():
        paper_count = int(stats["paper_count"])
        author_rows.append(
            {
                "author": author,
                "paper_count": paper_count,
                "oral_count": stats["oral_count"],
                "award_count": stats["award_count"],
                "public_total_votes": stats["public_total_votes"],
                "votes_per_paper": round(stats["public_total_votes"] / paper_count, 2),
                "visits_last_7_days": stats["visits_last_7_days"],
                "unique_coauthor_count": len(stats["coauthors"]),
                "coauthor_pagerank": round(author_pagerank.get(author, 0), 8),
                "top_topic_groups": top_counter(stats["topics"]),
                "top_themes": top_counter(stats["themes"]),
                "top_clusters": top_counter(stats["clusters"], 3),
                "top_institutions": top_counter(stats["institutions"], 5),
                "top_coauthors": top_counter(stats["coauthors"], 5),
            }
        )
    author_rows.sort(
        key=lambda row: (
            -int(row["paper_count"]),
            -int(row["oral_count"]),
            -int(row["public_total_votes"]),
            str(row["author"]),
        )
    )

    inst_rows = []
    for inst, stats in inst_stats.items():
        paper_count = int(stats["paper_count"])
        inst_rows.append(
            {
                "canonical_institution": inst,
                "sector": stats["sector"],
                "paper_count": paper_count,
                "oral_count": stats["oral_count"],
                "award_count": stats["award_count"],
                "public_total_votes": stats["public_total_votes"],
                "votes_per_paper": round(stats["public_total_votes"] / paper_count, 2),
                "visits_last_7_days": stats["visits_last_7_days"],
                "unique_partner_count": len(stats["partners"]),
                "collaboration_pagerank": round(inst_pagerank.get(inst, 0), 8),
                "top_topic_groups": top_counter(stats["topics"]),
                "top_themes": top_counter(stats["themes"]),
                "top_clusters": top_counter(stats["clusters"], 3),
                "top_partners": top_counter(stats["partners"], 8),
            }
        )
    inst_rows.sort(
        key=lambda row: (
            -int(row["paper_count"]),
            -int(row["oral_count"]),
            -float(row["collaboration_pagerank"]),
            str(row["canonical_institution"]),
        )
    )

    industry_academia = [row for row in paper_rows if row["has_industry_academia"]]
    single_author = [row for row in paper_rows if int(row["author_count"]) == 1]
    large_team = [row for row in paper_rows if int(row["author_count"]) >= 12]
    collaboration_summary = [
        {"metric": "paper_count", "value": len(papers)},
        {"metric": "unique_author_names", "value": len(author_stats)},
        {"metric": "unique_canonical_institutions", "value": len(inst_stats)},
        {"metric": "coauthor_edges", "value": author_graph.number_of_edges()},
        {"metric": "institution_collaboration_edges", "value": inst_graph.number_of_edges()},
        {"metric": "single_author_papers", "value": len(single_author)},
        {"metric": "large_team_papers_12plus_authors", "value": len(large_team)},
        {"metric": "industry_academia_papers", "value": len(industry_academia)},
        {"metric": "industry_academia_share", "value": round(len(industry_academia) / len(papers), 4)},
        {"metric": "mean_authors_per_paper", "value": round(sum(int(row["author_count"]) for row in paper_rows) / len(paper_rows), 2)},
        {"metric": "median_authors_per_paper", "value": sorted(int(row["author_count"]) for row in paper_rows)[len(paper_rows) // 2]},
    ]

    write_csv(
        PROCESSED / "icml2026_author_counts.csv",
        author_rows,
        [
            "author", "paper_count", "oral_count", "award_count", "public_total_votes",
            "votes_per_paper", "visits_last_7_days", "unique_coauthor_count",
            "coauthor_pagerank", "top_topic_groups", "top_themes", "top_clusters",
            "top_institutions", "top_coauthors",
        ],
    )
    write_csv(
        PROCESSED / "icml2026_author_collaboration_edges.csv",
        weighted_degree_rows(author_graph, "author_a", "author_b", 1000),
        ["author_a", "author_b", "shared_paper_count"],
    )
    write_csv(
        PROCESSED / "icml2026_institution_collaboration.csv",
        inst_rows,
        [
            "canonical_institution", "sector", "paper_count", "oral_count", "award_count",
            "public_total_votes", "votes_per_paper", "visits_last_7_days", "unique_partner_count",
            "collaboration_pagerank", "top_topic_groups", "top_themes", "top_clusters", "top_partners",
        ],
    )
    write_csv(
        PROCESSED / "icml2026_institution_collaboration_edges.csv",
        weighted_degree_rows(inst_graph, "institution_a", "institution_b", 1000),
        ["institution_a", "institution_b", "shared_paper_count"],
    )
    write_csv(
        PROCESSED / "icml2026_paper_collaboration_features.csv",
        paper_rows,
        [
            "event_id", "title", "author_count", "canonical_institution_count", "sector_mix",
            "has_industry", "has_academia", "has_research_institute", "has_industry_academia",
            "cluster_id", "cluster_label", "themes", "is_oral", "award", "public_total_votes",
            "visits_last_7_days", "canonical_institutions", "authors", "url",
        ],
    )
    write_csv(
        PROCESSED / "icml2026_sector_collaboration_counts.csv",
        [{"sector_pair": key, "institution_edge_count": value} for key, value in sector_edge_counts.most_common()],
        ["sector_pair", "institution_edge_count"],
    )
    write_csv(
        PROCESSED / "icml2026_sector_mix_counts.csv",
        [{"sector_mix": key, "paper_count": value} for key, value in sector_mix_counts.most_common()],
        ["sector_mix", "paper_count"],
    )
    write_csv(
        PROCESSED / "icml2026_collaboration_summary.csv",
        collaboration_summary,
        ["metric", "value"],
    )

    lines = [
        "# ICML 2026 Collaboration Landscape",
        "",
        "This report analyzes author-name coauthorship and canonical-institution paper co-occurrence from the official ICML virtual corpus.",
        "",
        "## Corpus Collaboration Snapshot",
        "",
    ]
    for row in collaboration_summary:
        lines.append(f"- {row['metric']}: {row['value']}")

    lines.extend(["", "## Most Prolific Author Names", ""])
    for row in author_rows[:25]:
        lines.append(
            f"- {row['author']}: {row['paper_count']} papers, {row['oral_count']} orals, "
            f"{row['public_total_votes']} public votes; themes: {row['top_themes']}"
        )

    lines.extend(["", "## Author Names With High Public Attention Per Paper", ""])
    high_attention_authors = [
        row for row in author_rows
        if int(row["paper_count"]) >= 2
    ]
    for row in sorted(high_attention_authors, key=lambda r: float(r["votes_per_paper"]), reverse=True)[:20]:
        lines.append(
            f"- {row['author']}: {row['votes_per_paper']} votes/paper across {row['paper_count']} papers; "
            f"clusters: {row['top_clusters']}"
        )

    lines.extend(["", "## Most Connected Author Names", ""])
    for row in sorted(author_rows, key=lambda r: float(r["coauthor_pagerank"]), reverse=True)[:20]:
        lines.append(
            f"- {row['author']}: pagerank {row['coauthor_pagerank']}, "
            f"{row['unique_coauthor_count']} unique coauthors; top coauthors: {row['top_coauthors']}"
        )

    lines.extend(["", "## Institution Collaboration Hubs", ""])
    for row in sorted(inst_rows, key=lambda r: float(r["collaboration_pagerank"]), reverse=True)[:25]:
        lines.append(
            f"- {row['canonical_institution']} ({row['sector']}): {row['paper_count']} papers, "
            f"{row['unique_partner_count']} partners, pagerank {row['collaboration_pagerank']}; "
            f"top partners: {row['top_partners']}"
        )

    lines.extend(["", "## Strongest Institution Co-Publication Edges", ""])
    for row in weighted_degree_rows(inst_graph, "institution_a", "institution_b", 30):
        lines.append(f"- {row['institution_a']} + {row['institution_b']}: {row['shared_paper_count']} papers")

    lines.extend(["", "## Paper Sector Mix", ""])
    for mix, count in sector_mix_counts.most_common():
        lines.append(f"- {mix}: {count} papers")

    lines.extend(["", "## Institution-Edge Sector Mix", ""])
    for pair, count in sector_edge_counts.most_common():
        lines.append(f"- {pair}: {count} institution co-occurrence edges")

    lines.extend(["", "## Industry-Academia Papers With Highest Public Signal", ""])
    for row in sorted(
        industry_academia,
        key=lambda r: (int(r["public_total_votes"]), int(r["visits_last_7_days"])),
        reverse=True,
    )[:25]:
        lines.append(
            f"- {row['title']} - {row['public_total_votes']} votes; "
            f"{row['cluster_label']}; institutions: {row['canonical_institutions']}"
        )

    lines.extend(
        [
            "",
            "## Caveats",
            "",
            "- Author names are not disambiguated. Common names may merge different people, and name variants may split one person.",
            "- Institutions are paper-level affiliations, not per-author affiliation assignments.",
            "- Institution edges mean two canonical institutions co-occurred on a paper; they do not prove direct lab-to-lab collaboration.",
            "- Public votes and visits are AlphaXiv attention signals, not quality labels.",
        ]
    )

    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "icml2026_collaboration_landscape.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {PROCESSED / 'icml2026_author_counts.csv'}")
    print(f"Wrote {PROCESSED / 'icml2026_institution_collaboration.csv'}")
    print(f"Wrote {PROCESSED / 'icml2026_paper_collaboration_features.csv'}")
    print(f"Wrote {REPORTS / 'icml2026_collaboration_landscape.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
