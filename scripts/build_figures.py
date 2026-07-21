#!/usr/bin/env python3
"""Generate static figures for the ICML 2026 EDA workspace."""

from __future__ import annotations

import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
FIGURES = ROOT / "figures"
REPORTS = ROOT / "reports"

TEXT = "#1f2933"
GRID = "#d9dee7"
BLUE = "#2f6f9f"
GREEN = "#40826d"
ORANGE = "#c77d2f"
RED = "#b44d4d"
PURPLE = "#6f5aa7"
GRAY = "#6b7280"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"Missing required input: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def to_int(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def to_float(value: str) -> float:
    try:
        return float(value or 0)
    except ValueError:
        return 0.0


def prep_ax(ax, title: str, xlabel: str = "", ylabel: str = "") -> None:
    ax.set_title(title, loc="left", fontsize=14, fontweight="bold", color=TEXT, pad=10)
    ax.set_xlabel(xlabel, color=TEXT)
    ax.set_ylabel(ylabel, color=TEXT)
    ax.tick_params(colors=TEXT, labelsize=9)
    ax.grid(axis="x", color=GRID, linewidth=0.8, alpha=0.8)
    ax.set_axisbelow(True)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color(GRID)
    ax.spines["bottom"].set_color(GRID)


def save(fig, filename: str) -> Path:
    FIGURES.mkdir(parents=True, exist_ok=True)
    path = FIGURES / filename
    fig.tight_layout()
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return path


def horizontal_bar(rows, label_key, value_key, filename, title, xlabel, color=BLUE, limit=15, value_fmt="{:,}") -> Path:
    selected = rows[:limit][::-1]
    labels = [row[label_key] for row in selected]
    values = [to_float(row[value_key]) for row in selected]
    fig, ax = plt.subplots(figsize=(10, max(5, 0.34 * len(selected) + 1.5)))
    ax.barh(labels, values, color=color)
    prep_ax(ax, title, xlabel=xlabel)
    xmax = max(values) if values else 1
    for i, value in enumerate(values):
        ax.text(value + xmax * 0.01, i, value_fmt.format(int(value) if float(value).is_integer() else value), va="center", fontsize=8, color=TEXT)
    return save(fig, filename)


def compact_cluster_label(row: dict[str, str], max_terms: int = 3) -> str:
    terms = [part.strip() for part in row["cluster_label"].split("/") if part.strip()]
    label = " / ".join(terms[:max_terms])
    if len(label) > 58:
        label = label[:55].rstrip() + "..."
    return f"{row['cluster_id']}: {label}"


def topic_group_figure() -> Path:
    papers = read_csv(PROCESSED / "icml2026_papers.csv")
    counts = {}
    for row in papers:
        group = row.get("topic_group") or "Unknown"
        counts[group] = counts.get(group, 0) + 1
    rows = [{"topic_group": k, "count": v} for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)]
    return horizontal_bar(
        rows,
        "topic_group",
        "count",
        "topic_group_distribution.png",
        "Official ICML Topic Groups",
        "paper count",
        BLUE,
        12,
    )


def theme_figure() -> Path:
    rows = read_csv(PROCESSED / "icml2026_theme_counts.csv")
    selected = rows[:15][::-1]
    labels = [row["theme"] for row in selected]
    counts = np.array([to_int(row["count"]) for row in selected])
    oral = np.array([to_int(row["oral_count"]) for row in selected])
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.barh(labels, counts, color=BLUE, label="papers")
    ax.barh(labels, oral, color=ORANGE, label="oral-designated")
    prep_ax(ax, "Rule-Based Research Themes", xlabel="paper count")
    ax.legend(frameon=False, loc="lower right")
    return save(fig, "theme_counts_orals.png")


def cluster_signal_figure() -> Path:
    rows = read_csv(PROCESSED / "icml2026_cluster_summary.csv")
    rows = sorted(rows, key=lambda row: to_float(row["votes_per_paper"]), reverse=True)[:18]
    labels = [compact_cluster_label(row) for row in rows][::-1]
    votes = [to_float(row["votes_per_paper"]) for row in rows][::-1]
    oral = [to_float(row["oral_enrichment"]) for row in rows][::-1]
    y = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(11, 8))
    bars = ax.barh(y, votes, color=BLUE)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    prep_ax(ax, "Clusters With Highest AlphaXiv Vote Density", xlabel="public votes per paper")
    ax2 = ax.twiny()
    ax2.plot(oral, y, color=ORANGE, marker="o", linewidth=1.8, label="oral enrichment")
    ax2.set_xlabel("oral enrichment vs corpus baseline", color=ORANGE)
    ax2.tick_params(axis="x", colors=ORANGE, labelsize=9)
    ax2.spines["top"].set_color(ORANGE)
    for bar, value in zip(bars, votes):
        ax.text(value + max(votes) * 0.01, bar.get_y() + bar.get_height() / 2, f"{value:.1f}", va="center", fontsize=8, color=TEXT)
    return save(fig, "cluster_vote_density_oral_enrichment.png")


def cluster_scatter_figure() -> Path:
    rows = read_csv(PROCESSED / "icml2026_cluster_summary.csv")
    x = np.array([to_float(row["votes_per_paper"]) for row in rows])
    y = np.array([to_float(row["oral_enrichment"]) for row in rows])
    sizes = np.array([max(20, to_int(row["paper_count"]) * 1.5) for row in rows])
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.scatter(x, y, s=sizes, color=PURPLE, alpha=0.55, edgecolor="white", linewidth=0.8)
    prep_ax(ax, "Program Signal vs Public Attention by Cluster", xlabel="public votes per paper", ylabel="oral enrichment")
    ax.axhline(1.0, color=GRAY, linestyle="--", linewidth=1)
    for row in rows:
        if to_float(row["votes_per_paper"]) >= 20 or to_float(row["oral_enrichment"]) >= 1.5:
            ax.annotate(
                str(row["cluster_id"]),
                (to_float(row["votes_per_paper"]), to_float(row["oral_enrichment"])),
                fontsize=9,
                color=TEXT,
            )
    ax.text(0.01, 0.01, "point size = cluster paper count; labels = cluster id", transform=ax.transAxes, fontsize=8, color=GRAY)
    return save(fig, "cluster_public_vs_program_signal.png")


def alphaxiv_distribution_figure() -> Path:
    rows = read_csv(PROCESSED / "alphaxiv_icml2026_joined.csv")
    votes = np.array([to_int(row["public_total_votes"]) for row in rows])
    recent = np.array([to_int(row["visits_last_7_days"]) for row in rows])
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].hist(np.log1p(votes), bins=40, color=BLUE)
    prep_ax(axes[0], "AlphaXiv Public Votes", xlabel="log(1 + votes)", ylabel="paper count")
    axes[1].hist(np.log1p(recent), bins=40, color=GREEN)
    prep_ax(axes[1], "AlphaXiv Recent Visits", xlabel="log(1 + 7-day visits)", ylabel="paper count")
    return save(fig, "alphaxiv_attention_distributions.png")


def top_institutions_figure() -> Path:
    rows = read_csv(PROCESSED / "icml2026_canonical_institution_counts.csv")
    return horizontal_bar(
        rows,
        "canonical_institution",
        "paper_count",
        "top_canonical_institutions.png",
        "Most Frequent Canonical Institutions",
        "paper-institution count",
        GREEN,
        25,
    )


def sector_mix_figure() -> Path:
    rows = read_csv(PROCESSED / "icml2026_sector_mix_counts.csv")
    rows = rows[:10]
    labels = [row["sector_mix"] for row in rows][::-1]
    values = [to_int(row["paper_count"]) for row in rows][::-1]
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.barh(labels, values, color=ORANGE)
    prep_ax(ax, "Paper-Level Sector Mix", xlabel="paper count")
    return save(fig, "sector_mix_papers.png")


def institution_collaboration_figure() -> Path:
    rows = read_csv(PROCESSED / "icml2026_institution_collaboration.csv")
    rows = sorted(rows, key=lambda row: to_float(row["collaboration_pagerank"]), reverse=True)[:20][::-1]
    labels = [row["canonical_institution"] for row in rows]
    values = [to_float(row["collaboration_pagerank"]) for row in rows]
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.barh(labels, values, color=PURPLE)
    prep_ax(ax, "Institution Collaboration Hubs", xlabel="paper co-occurrence PageRank")
    return save(fig, "institution_collaboration_hubs.png")


def author_team_size_figure() -> Path:
    rows = read_csv(PROCESSED / "icml2026_paper_collaboration_features.csv")
    sizes = np.array([to_int(row["author_count"]) for row in rows])
    capped = np.clip(sizes, 1, 20)
    bins = np.arange(1, 22) - 0.5
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.hist(capped, bins=bins, color=BLUE, edgecolor="white")
    ax.set_xticks(range(1, 21))
    ax.set_xticklabels([str(i) for i in range(1, 20)] + ["20+"])
    prep_ax(ax, "Team Size Distribution", xlabel="authors per paper", ylabel="paper count")
    return save(fig, "team_size_distribution.png")


def semantic_cluster_map_figure() -> Path:
    rows = read_csv(PROCESSED / "icml2026_semantic_cluster_assignments.csv")
    summary = {
        row["semantic_cluster_id"]: row
        for row in read_csv(PROCESSED / "icml2026_semantic_cluster_summary.csv")
    }
    xs = np.array([to_float(row["semantic_x"]) for row in rows])
    ys = np.array([to_float(row["semantic_y"]) for row in rows])
    clusters = [row["semantic_cluster_id"] for row in rows]
    votes = np.array([math.log1p(to_int(row["public_total_votes"])) for row in rows])
    unique = sorted(set(clusters), key=lambda value: int(value))
    palette = plt.get_cmap("tab20", len(unique))
    color_lookup = {cluster: palette(i) for i, cluster in enumerate(unique)}
    colors = [color_lookup[cluster] for cluster in clusters]
    sizes = 8 + 12 * (votes / max(votes.max(), 1))

    fig, ax = plt.subplots(figsize=(11, 8))
    ax.scatter(xs, ys, s=sizes, c=colors, alpha=0.48, linewidth=0)
    prep_ax(ax, "Transformer Semantic Map", xlabel="PCA 1", ylabel="PCA 2")
    ax.grid(False)
    largest = sorted(summary.values(), key=lambda row: to_int(row["paper_count"]), reverse=True)[:12]
    for row in largest:
        cluster_id = row["semantic_cluster_id"]
        members = [item for item in rows if item["semantic_cluster_id"] == cluster_id]
        if not members:
            continue
        cx = np.mean([to_float(item["semantic_x"]) for item in members])
        cy = np.mean([to_float(item["semantic_y"]) for item in members])
        label = str(row["semantic_cluster_label"]).split("/")[0].strip()
        ax.annotate(
            f"{cluster_id}: {label}",
            (cx, cy),
            fontsize=8,
            color=TEXT,
            bbox={"boxstyle": "round,pad=0.2", "facecolor": "white", "edgecolor": GRID, "alpha": 0.82},
        )
    ax.text(0.01, 0.01, "point size = log(1 + AlphaXiv public votes); labels = largest semantic clusters", transform=ax.transAxes, fontsize=8, color=GRAY)
    return save(fig, "semantic_cluster_map.png")


def semantic_signal_figure() -> Path:
    rows = read_csv(PROCESSED / "icml2026_semantic_cluster_summary.csv")
    rows = sorted(rows, key=lambda row: to_float(row["votes_per_paper"]), reverse=True)[:18]
    labels = [
        f"{row['semantic_cluster_id']}: {' / '.join(row['semantic_cluster_label'].split('/')[:3]).strip()}"
        for row in rows
    ][::-1]
    votes = [to_float(row["votes_per_paper"]) for row in rows][::-1]
    oral = [to_float(row["oral_enrichment"]) for row in rows][::-1]
    y = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(11, 8))
    bars = ax.barh(y, votes, color=GREEN)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    prep_ax(ax, "Semantic Clusters With Highest Vote Density", xlabel="public votes per paper")
    ax2 = ax.twiny()
    ax2.plot(oral, y, color=ORANGE, marker="o", linewidth=1.8)
    ax2.set_xlabel("oral enrichment vs corpus baseline", color=ORANGE)
    ax2.tick_params(axis="x", colors=ORANGE, labelsize=9)
    ax2.spines["top"].set_color(ORANGE)
    for bar, value in zip(bars, votes):
        ax.text(value + max(votes) * 0.01, bar.get_y() + bar.get_height() / 2, f"{value:.1f}", va="center", fontsize=8, color=TEXT)
    return save(fig, "semantic_cluster_vote_density.png")


def taxonomy_area_figure() -> Path:
    rows = read_csv(PROCESSED / "icml2026_manual_taxonomy_areas.csv")
    rows = rows[::-1]
    labels = [row["area"] for row in rows]
    papers = [to_int(row["paper_count"]) for row in rows]
    github_share = [to_float(row["github_url_share"]) * 100 for row in rows]
    y = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(11, 7))
    bars = ax.barh(y, papers, color=BLUE)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    prep_ax(ax, "Curated Taxonomy Area Sizes", xlabel="paper count")
    ax2 = ax.twiny()
    ax2.plot(github_share, y, color=GREEN, marker="o", linewidth=1.8)
    ax2.set_xlabel("GitHub URL share (%)", color=GREEN)
    ax2.tick_params(axis="x", colors=GREEN, labelsize=9)
    ax2.spines["top"].set_color(GREEN)
    for bar, value in zip(bars, papers):
        ax.text(value + max(papers) * 0.01, bar.get_y() + bar.get_height() / 2, f"{value:,}", va="center", fontsize=8, color=TEXT)
    return save(fig, "manual_taxonomy_area_sizes.png")


def evidence_contribution_mix_figure() -> Path:
    rows = read_csv(PROCESSED / "icml2026_area_evidence_summary.csv")
    categories = [
        "Benchmark / evaluation",
        "Dataset / data resource",
        "Method / algorithm",
        "Theory / proof",
        "System / infrastructure",
        "Position / conceptual",
        "Application / domain study",
        "Uncoded",
    ]
    labels = [row["area"] for row in rows][::-1]
    data = {category: [] for category in categories}
    for row in rows[::-1]:
        counts = {}
        for part in row["top_primary_contribution_types"].split("; "):
            if " (" not in part:
                continue
            name, count = part.rsplit(" (", 1)
            counts[name] = to_int(count.rstrip(")"))
        total = max(1, to_int(row["paper_count"]))
        for category in categories:
            data[category].append(100 * counts.get(category, 0) / total)

    colors = [BLUE, GREEN, ORANGE, PURPLE, RED, "#7a8699", "#9a6f3f", GRAY]
    y = np.arange(len(labels))
    left = np.zeros(len(labels))
    fig, ax = plt.subplots(figsize=(12, 7))
    for category, color in zip(categories, colors):
        values = np.array(data[category])
        ax.barh(y, values, left=left, color=color, label=category)
        left += values
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    prep_ax(ax, "Heuristic Primary Contribution Mix by Area", xlabel="share of area papers (%)")
    ax.legend(frameon=False, loc="lower center", bbox_to_anchor=(0.5, -0.28), ncol=2, fontsize=8)
    return save(fig, "evidence_contribution_mix.png")


def program_calibration_figure() -> Path:
    rows = read_csv(PROCESSED / "icml2026_area_program_calibration.csv")
    rows = sorted(rows, key=lambda row: to_float(row["oral_enrichment"]), reverse=True)
    labels = [row["group"] for row in rows][::-1]
    oral = [to_float(row["oral_enrichment"]) for row in rows][::-1]
    public = [to_float(row["public_attention_enrichment"]) for row in rows][::-1]
    y = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.barh(y - 0.18, oral, height=0.36, color=ORANGE, label="oral enrichment")
    ax.barh(y + 0.18, public, height=0.36, color=BLUE, label="public-attention enrichment")
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    prep_ax(ax, "Program Signal vs Public Attention by Area", xlabel="enrichment vs area paper share")
    ax.axvline(1.0, color=GRAY, linestyle="--", linewidth=1)
    ax.legend(frameon=False, loc="lower right")
    return save(fig, "program_signal_calibration.png")


def arxiv_trend_figure() -> Path:
    rows = read_csv(PROCESSED / "arxiv_taxonomy_trend_summary.csv")
    rows = sorted(rows, key=lambda row: to_float(row["growth_2025_vs_2024"]), reverse=True)
    labels = [row["area"] for row in rows][::-1]
    growth = [to_float(row["growth_2025_vs_2024"]) * 100 for row in rows][::-1]
    icml_share = [to_float(row["icml2026_area_share"]) * 100 for row in rows][::-1]
    y = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(11, 7))
    bars = ax.barh(y, growth, color=GREEN)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    prep_ax(ax, "arXiv Query Growth by ICML Taxonomy Area", xlabel="2025 vs 2024 query-count growth (%)")
    ax.axvline(0, color=GRAY, linewidth=1)
    ax2 = ax.twiny()
    ax2.plot(icml_share, y, color=ORANGE, marker="o", linewidth=1.8)
    ax2.set_xlabel("ICML 2026 taxonomy share (%)", color=ORANGE)
    ax2.tick_params(axis="x", colors=ORANGE, labelsize=9)
    ax2.spines["top"].set_color(ORANGE)
    for bar, value in zip(bars, growth):
        ax.text(value + max(growth) * 0.01, bar.get_y() + bar.get_height() / 2, f"{value:.1f}%", va="center", fontsize=8, color=TEXT)
    return save(fig, "arxiv_taxonomy_trends.png")


def historical_venue_delta_figure() -> Path:
    rows = read_csv(PROCESSED / "historical_venue_delta_summary.csv")
    rows = sorted(rows, key=lambda row: to_float(row["delta_vs_baseline_avg"]))
    labels = [row["area"] for row in rows]
    deltas = [to_float(row["delta_vs_baseline_avg"]) * 100 for row in rows]
    colors = [RED if value < 0 else GREEN for value in deltas]
    fig, ax = plt.subplots(figsize=(11, 7))
    bars = ax.barh(labels, deltas, color=colors)
    prep_ax(ax, "ICML 2026 Area Share vs Prior-Venue Baseline", xlabel="percentage-point delta vs ICML 2025 / NeurIPS 2025 / ICLR 2026 average")
    ax.axvline(0, color=GRAY, linewidth=1)
    xmax = max(abs(value) for value in deltas) if deltas else 1
    for bar, value in zip(bars, deltas):
        offset = xmax * 0.02
        x = value + offset if value >= 0 else value - offset
        ha = "left" if value >= 0 else "right"
        ax.text(x, bar.get_y() + bar.get_height() / 2, f"{value:+.1f} pp", va="center", ha=ha, fontsize=8, color=TEXT)
    return save(fig, "historical_venue_area_deltas.png")


def main() -> int:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.facecolor": "white",
        }
    )
    figure_paths = [
        topic_group_figure(),
        theme_figure(),
        cluster_signal_figure(),
        cluster_scatter_figure(),
        alphaxiv_distribution_figure(),
        top_institutions_figure(),
        sector_mix_figure(),
        institution_collaboration_figure(),
        author_team_size_figure(),
        semantic_cluster_map_figure(),
        semantic_signal_figure(),
        taxonomy_area_figure(),
        evidence_contribution_mix_figure(),
        program_calibration_figure(),
        arxiv_trend_figure(),
        historical_venue_delta_figure(),
    ]

    lines = [
        "# ICML 2026 Visual EDA Index",
        "",
        "Static figures generated from processed CSVs. These are designed as report/presentation seed visuals, not final publication graphics.",
        "",
        "## Figures",
        "",
    ]
    descriptions = {
        "topic_group_distribution.png": "Official ICML topic-group balance across all 6,628 paper rows.",
        "theme_counts_orals.png": "Rule-based cross-cutting theme counts with oral-designated counts overlaid.",
        "cluster_vote_density_oral_enrichment.png": "Clusters ranked by AlphaXiv public votes per paper, with oral enrichment shown as a second axis.",
        "cluster_public_vs_program_signal.png": "Cluster-level divergence between public attention and program-committee signal.",
        "alphaxiv_attention_distributions.png": "Long-tailed AlphaXiv vote and recent-visit distributions.",
        "top_canonical_institutions.png": "Top canonical institutions after alias cleanup.",
        "sector_mix_papers.png": "Paper-level sector mixes from canonical institution sectors.",
        "institution_collaboration_hubs.png": "Institution collaboration hubs by paper co-occurrence PageRank.",
        "team_size_distribution.png": "Distribution of author counts per ICML paper.",
        "semantic_cluster_map.png": "Transformer embedding map of the ICML corpus, projected to two PCA dimensions and labeled by the largest semantic clusters.",
        "semantic_cluster_vote_density.png": "Semantic clusters ranked by AlphaXiv public votes per paper, with oral enrichment shown as a second axis.",
        "manual_taxonomy_area_sizes.png": "Curated report-level taxonomy area sizes, with GitHub URL share shown as a reproducibility proxy.",
        "evidence_contribution_mix.png": "Heuristic primary contribution-type mix across curated taxonomy areas.",
        "program_signal_calibration.png": "Oral-selection enrichment compared with AlphaXiv public-attention enrichment across taxonomy areas.",
        "arxiv_taxonomy_trends.png": "Coarse arXiv query-count growth by taxonomy area, compared with ICML 2026 taxonomy share.",
        "historical_venue_area_deltas.png": "ICML 2026 area-share deltas against accepted-paper baselines from ICML 2025, NeurIPS 2025, and ICLR 2026.",
    }
    for path in figure_paths:
        rel = f"../figures/{path.name}"
        lines.append(f"### {path.name}")
        lines.append("")
        lines.append(descriptions[path.name])
        lines.append("")
        lines.append(f"![{path.name}]({rel})")
        lines.append("")

    lines.extend(
        [
            "## Caveats",
            "",
            "- Theme labels are rule-based and intentionally broad.",
            "- Cluster labels come from TF-IDF terms, not manual semantic names.",
            "- Semantic-map coordinates are a 2D PCA projection of transformer embeddings, so local neighborhoods are more meaningful than precise axis positions.",
            "- Manual taxonomy areas are curated seed labels over semantic clusters, not a final ontology.",
            "- Evidence contribution mixes are keyword/regex-derived triage labels, not verified paper annotations.",
            "- Program-signal enrichment uses oral/award labels as conference-program signals, not complete quality labels.",
            "- arXiv trend counts are broad overlapping query counts, not prior-conference acceptance trends.",
            "- Historical venue deltas use a shared keyword scorer over accepted-paper metadata, with weaker title/topic-only coverage for venues whose static abstracts were unavailable.",
            "- AlphaXiv metrics are public-attention signals, not quality labels.",
            "- Institution and author figures inherit the canonicalization and name-disambiguation caveats in the collaboration report.",
        ]
    )
    REPORTS.mkdir(parents=True, exist_ok=True)
    report_path = REPORTS / "icml2026_visual_eda_index.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    for path in figure_paths:
        print(f"Wrote {path}")
    print(f"Wrote {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
