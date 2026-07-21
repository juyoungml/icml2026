#!/usr/bin/env python3
"""Build an unsupervised ICML 2026 cluster landscape from titles and abstracts."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import silhouette_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"


K_CANDIDATES = [14, 18, 22, 26, 30]
RANDOM_STATE = 2026


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


def intish(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def paper_text(row: dict[str, str]) -> str:
    title = row.get("title", "")
    topic = row.get("topic", "")
    abstract = row.get("abstract", "")
    return f"{title}. {title}. {topic}. {abstract}".strip()


def short_label(terms: list[str]) -> str:
    cleaned = []
    blocked = {"learning", "model", "models", "data", "method", "methods", "neural"}
    for term in terms:
        if term in blocked:
            continue
        cleaned.append(term)
        if len(cleaned) == 4:
            break
    return " / ".join(cleaned) if cleaned else "mixed cluster"


def choose_k(embeddings: np.ndarray) -> tuple[int, list[dict[str, object]]]:
    rng = np.random.default_rng(RANDOM_STATE)
    sample_size = min(1800, embeddings.shape[0])
    sample_idx = rng.choice(embeddings.shape[0], size=sample_size, replace=False)
    diagnostics = []
    best_k = K_CANDIDATES[0]
    best_score = -1.0
    for k in K_CANDIDATES:
        model = MiniBatchKMeans(
            n_clusters=k,
            random_state=RANDOM_STATE,
            batch_size=512,
            n_init=10,
            reassignment_ratio=0.01,
        )
        labels = model.fit_predict(embeddings)
        score = silhouette_score(embeddings[sample_idx], labels[sample_idx], metric="cosine")
        counts = Counter(labels)
        diagnostics.append(
            {
                "k": k,
                "sample_silhouette_cosine": round(float(score), 4),
                "min_cluster_size": min(counts.values()),
                "max_cluster_size": max(counts.values()),
            }
        )
        if score > best_score:
            best_score = score
            best_k = k
    return best_k, diagnostics


def cluster_top_terms(tfidf_matrix, labels: np.ndarray, feature_names: np.ndarray, top_n: int = 15) -> dict[int, list[str]]:
    output = {}
    for cluster_id in sorted(set(labels)):
        mask = labels == cluster_id
        mean_tfidf = np.asarray(tfidf_matrix[mask].mean(axis=0)).ravel()
        top_idx = mean_tfidf.argsort()[::-1][:top_n]
        output[int(cluster_id)] = [str(feature_names[i]) for i in top_idx if mean_tfidf[i] > 0]
    return output


def main() -> int:
    papers = read_csv(PROCESSED / "icml2026_papers.csv")
    theme_rows = read_csv(PROCESSED / "icml2026_theme_matrix.csv")
    alpha_rows = read_csv(PROCESSED / "alphaxiv_icml2026_joined.csv")
    if not papers:
        raise SystemExit("Run scripts/fetch_icml_virtual.py first.")
    if not theme_rows:
        raise SystemExit("Run scripts/build_researcher_landscape.py first.")

    theme_by_title = {normalize_title(row["title"]): row for row in theme_rows}
    alpha_by_title = {normalize_title(row["title"]): row for row in alpha_rows}
    docs = [paper_text(row) for row in papers]

    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        ngram_range=(1, 2),
        min_df=5,
        max_df=0.45,
        max_features=45000,
        sublinear_tf=True,
    )
    tfidf = vectorizer.fit_transform(docs)
    n_components = min(160, tfidf.shape[1] - 1)
    lsa = make_pipeline(TruncatedSVD(n_components=n_components, random_state=RANDOM_STATE), Normalizer(copy=False))
    embeddings = lsa.fit_transform(tfidf)

    best_k, diagnostics = choose_k(embeddings)
    cluster_model = MiniBatchKMeans(
        n_clusters=best_k,
        random_state=RANDOM_STATE,
        batch_size=512,
        n_init=30,
        reassignment_ratio=0.01,
    )
    labels = cluster_model.fit_predict(embeddings)
    distances = cluster_model.transform(embeddings)
    feature_names = vectorizer.get_feature_names_out()
    terms_by_cluster = cluster_top_terms(tfidf, labels, feature_names)

    assignments = []
    cluster_rows = []
    cluster_to_rows: dict[int, list[dict[str, object]]] = defaultdict(list)
    max_votes = max([intish(row.get("public_total_votes", "0")) for row in alpha_rows] or [1])
    max_recent = max([intish(row.get("visits_last_7_days", "0")) for row in alpha_rows] or [1])
    corpus_oral_rate = sum(row.get("is_oral") == "true" for row in papers) / len(papers)
    corpus_votes = sum(intish(row.get("public_total_votes", "0")) for row in alpha_rows)

    for paper, cluster_id, distance in zip(papers, labels, distances[np.arange(len(papers)), labels]):
        key = normalize_title(paper["title"])
        theme_row = theme_by_title.get(key, {})
        alpha_row = alpha_by_title.get(key, {})
        votes = intish(alpha_row.get("public_total_votes", "0"))
        recent = intish(alpha_row.get("visits_last_7_days", "0"))
        score = float(theme_row.get("score", 0) or 0)
        row = {
            "event_id": paper.get("event_id", ""),
            "cluster_id": int(cluster_id),
            "cluster_label": short_label(terms_by_cluster[int(cluster_id)]),
            "title": paper.get("title", ""),
            "topic": paper.get("topic", ""),
            "topic_group": paper.get("topic_group", "") or "Unknown",
            "themes": theme_row.get("themes", ""),
            "is_oral": paper.get("is_oral", "false"),
            "award": theme_row.get("award", ""),
            "public_total_votes": votes,
            "visits_last_7_days": recent,
            "github_stars": intish(alpha_row.get("github_stars", "0")),
            "composite_score": score,
            "cluster_distance": round(float(distance), 5),
            "cluster_centrality": round(float(1 / (1 + distance)), 5),
            "attention_score": round((votes / max_votes if max_votes else 0) + 0.5 * (recent / max_recent if max_recent else 0), 5),
            "url": paper.get("url", ""),
            "alphaxiv_url": alpha_row.get("alphaxiv_url", ""),
        }
        assignments.append(row)
        cluster_to_rows[int(cluster_id)].append(row)

    for cluster_id in sorted(cluster_to_rows):
        items = cluster_to_rows[cluster_id]
        topic_groups = Counter(str(row["topic_group"]) for row in items)
        themes = Counter()
        for row in items:
            for theme in str(row["themes"]).split("; "):
                if theme:
                    themes[theme] += 1
        oral_count = sum(row["is_oral"] == "true" for row in items)
        award_count = sum(bool(row["award"]) for row in items)
        total_votes = sum(int(row["public_total_votes"]) for row in items)
        recent_visits = sum(int(row["visits_last_7_days"]) for row in items)
        oral_rate = oral_count / len(items)
        votes_per_paper = total_votes / len(items)
        vote_share = total_votes / corpus_votes if corpus_votes else 0
        central = sorted(items, key=lambda row: row["cluster_distance"])[:8]
        high_signal = sorted(
            items,
            key=lambda row: (
                bool(row["award"]),
                row["is_oral"] == "true",
                float(row["composite_score"]),
                int(row["public_total_votes"]),
                int(row["visits_last_7_days"]),
            ),
            reverse=True,
        )[:8]
        cluster_rows.append(
            {
                "cluster_id": cluster_id,
                "cluster_label": short_label(terms_by_cluster[cluster_id]),
                "paper_count": len(items),
                "share": round(len(items) / len(papers), 4),
                "oral_count": oral_count,
                "oral_rate": round(oral_rate, 4),
                "oral_enrichment": round(oral_rate / corpus_oral_rate, 2) if corpus_oral_rate else "",
                "award_count": award_count,
                "total_public_votes": total_votes,
                "votes_per_paper": round(votes_per_paper, 2),
                "public_vote_share": round(vote_share, 4),
                "recent_visits_7d": recent_visits,
                "top_terms": "; ".join(terms_by_cluster[cluster_id][:15]),
                "top_topic_groups": "; ".join(f"{k} ({v})" for k, v in topic_groups.most_common(5)),
                "top_themes": "; ".join(f"{k} ({v})" for k, v in themes.most_common(5)),
                "central_papers": " | ".join(row["title"] for row in central),
                "high_signal_papers": " | ".join(row["title"] for row in high_signal),
            }
        )

    cluster_rows.sort(key=lambda row: (-int(row["paper_count"]), int(row["cluster_id"])))
    write_csv(
        PROCESSED / "icml2026_cluster_assignments.csv",
        assignments,
        [
            "event_id", "cluster_id", "cluster_label", "title", "topic", "topic_group", "themes",
            "is_oral", "award", "public_total_votes", "visits_last_7_days", "github_stars",
            "composite_score", "cluster_distance", "cluster_centrality", "attention_score", "url", "alphaxiv_url",
        ],
    )
    write_csv(
        PROCESSED / "icml2026_cluster_summary.csv",
        cluster_rows,
        [
            "cluster_id", "cluster_label", "paper_count", "share", "oral_count", "award_count",
            "oral_rate", "oral_enrichment", "total_public_votes", "votes_per_paper",
            "public_vote_share", "recent_visits_7d", "top_terms", "top_topic_groups",
            "top_themes", "central_papers", "high_signal_papers",
        ],
    )
    write_csv(
        PROCESSED / "icml2026_cluster_diagnostics.csv",
        diagnostics,
        ["k", "sample_silhouette_cosine", "min_cluster_size", "max_cluster_size"],
    )

    lines = [
        "# ICML 2026 Unsupervised Cluster Landscape",
        "",
        "Method: TF-IDF over title, official topic, and abstract; TruncatedSVD latent semantic projection; normalized k-means clustering.",
        f"Selected cluster count: {best_k} from candidates {', '.join(map(str, K_CANDIDATES))}, based on sampled cosine silhouette.",
        "",
        "## Diagnostics",
        "",
    ]
    for row in diagnostics:
        chosen = " selected" if int(row["k"]) == best_k else ""
        lines.append(
            f"- k={row['k']}: silhouette={row['sample_silhouette_cosine']}, "
            f"size range={row['min_cluster_size']}-{row['max_cluster_size']}{chosen}"
        )

    lines.extend(["", "## Cluster Map", ""])
    for row in cluster_rows:
        lines.append(f"### Cluster {row['cluster_id']}: {row['cluster_label']}")
        lines.append(
            f"- Size: {row['paper_count']} papers ({float(row['share']) * 100:.1f}%); "
            f"orals: {row['oral_count']}; awards: {row['award_count']}; public votes: {row['total_public_votes']}"
        )
        lines.append(f"- Top terms: {row['top_terms']}")
        lines.append(f"- Topic groups: {row['top_topic_groups']}")
        lines.append(f"- Rule themes: {row['top_themes']}")
        lines.append("- Central papers:")
        for title in str(row["central_papers"]).split(" | ")[:5]:
            lines.append(f"  - {title}")
        lines.append("- High-signal papers:")
        for title in str(row["high_signal_papers"]).split(" | ")[:5]:
            lines.append(f"  - {title}")
        lines.append("")

    lines.extend(["", "## Signal Calibration", ""])
    lines.append(
        f"Corpus oral rate: {corpus_oral_rate * 100:.2f}%. "
        "Oral enrichment compares each cluster oral rate against that corpus baseline."
    )
    lines.extend(["", "### Highest Oral Enrichment", ""])
    for row in sorted(cluster_rows, key=lambda r: (float(r["oral_enrichment"]), int(r["oral_count"])), reverse=True)[:10]:
        lines.append(
            f"- Cluster {row['cluster_id']} ({row['cluster_label']}): "
            f"{float(row['oral_rate']) * 100:.1f}% oral, {row['oral_enrichment']}x baseline, "
            f"{row['paper_count']} papers"
        )
    lines.extend(["", "### Highest Public Attention Per Paper", ""])
    for row in sorted(cluster_rows, key=lambda r: float(r["votes_per_paper"]), reverse=True)[:10]:
        lines.append(
            f"- Cluster {row['cluster_id']} ({row['cluster_label']}): "
            f"{row['votes_per_paper']} votes/paper, {float(row['public_vote_share']) * 100:.1f}% of public votes, "
            f"{row['paper_count']} papers"
        )

    lines.extend(
        [
            "## Researcher Interpretation Notes",
            "",
            "- Use clusters as a second opinion against the rule-based theme map. Agreement means the topic is robust; disagreement marks papers worth manual review.",
            "- Large mixed clusters usually indicate broad methodological language rather than a coherent subfield. Split them manually before using in a presentation.",
            "- Small clusters with high oral or award density are often more interesting than large clusters with high public attention.",
            "- This is not a transformer embedding map. It is a lightweight local baseline that should be replaced or benchmarked against sentence embeddings for a final 9.5/10 report.",
        ]
    )

    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "icml2026_cluster_landscape.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Selected k={best_k}")
    print(f"Wrote {PROCESSED / 'icml2026_cluster_assignments.csv'}")
    print(f"Wrote {PROCESSED / 'icml2026_cluster_summary.csv'}")
    print(f"Wrote {PROCESSED / 'icml2026_cluster_diagnostics.csv'}")
    print(f"Wrote {REPORTS / 'icml2026_cluster_landscape.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
