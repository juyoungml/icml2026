#!/usr/bin/env python3
"""Build a transformer-embedding semantic cluster landscape for ICML 2026."""

from __future__ import annotations

import csv
import json
import math
import os
import re
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score, silhouette_score
from sklearn.preprocessing import normalize


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
RANDOM_STATE = 2026
K_CANDIDATES = [18, 24, 30, 36, 42]
EMBEDDING_CACHE = PROCESSED / "icml2026_semantic_embeddings.npy"
EMBEDDING_META = PROCESSED / "icml2026_semantic_embeddings_metadata.json"

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")


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


def floatish(value: str) -> float:
    try:
        return float(value or 0)
    except ValueError:
        return 0.0


def paper_text(row: dict[str, str]) -> str:
    title = row.get("title", "")
    topic = row.get("topic", "")
    abstract = row.get("abstract", "")
    return f"{title}. {topic}. {abstract}".strip()


def short_label(terms: list[str]) -> str:
    blocked = {"learning", "model", "models", "data", "method", "methods", "neural", "using"}
    kept = []
    for term in terms:
        if term in blocked:
            continue
        kept.append(term)
        if len(kept) == 4:
            break
    return " / ".join(kept) if kept else "mixed semantic cluster"


def cache_valid(papers: list[dict[str, str]]) -> bool:
    if not EMBEDDING_CACHE.exists() or not EMBEDDING_META.exists():
        return False
    try:
        meta = json.loads(EMBEDDING_META.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    titles = [row.get("title", "") for row in papers]
    return (
        meta.get("model_name") == MODEL_NAME
        and meta.get("paper_count") == len(papers)
        and meta.get("first_title") == (titles[0] if titles else "")
        and meta.get("last_title") == (titles[-1] if titles else "")
    )


def mean_pool(last_hidden_state, attention_mask):
    import torch

    mask = attention_mask.unsqueeze(-1).expand(last_hidden_state.size()).float()
    summed = torch.sum(last_hidden_state * mask, dim=1)
    counts = torch.clamp(mask.sum(dim=1), min=1e-9)
    return summed / counts


def build_transformer_embeddings(docs: list[str]) -> tuple[np.ndarray, dict[str, object]]:
    import torch
    from transformers import AutoModel, AutoTokenizer

    device = "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModel.from_pretrained(MODEL_NAME).to(device)
    model.eval()

    batches = []
    batch_size = 64
    with torch.no_grad():
        for start in range(0, len(docs), batch_size):
            batch_docs = docs[start:start + batch_size]
            encoded = tokenizer(
                batch_docs,
                padding=True,
                truncation=True,
                max_length=256,
                return_tensors="pt",
            )
            encoded = {key: value.to(device) for key, value in encoded.items()}
            output = model(**encoded)
            pooled = mean_pool(output.last_hidden_state, encoded["attention_mask"])
            pooled = torch.nn.functional.normalize(pooled, p=2, dim=1)
            batches.append(pooled.cpu().numpy())
    embeddings = np.vstack(batches)
    meta = {
        "embedding_source": "transformer",
        "model_name": MODEL_NAME,
        "device": device,
        "embedding_dim": int(embeddings.shape[1]),
        "max_length": 256,
    }
    return embeddings, meta


def load_or_build_embeddings(papers: list[dict[str, str]], docs: list[str]) -> tuple[np.ndarray, dict[str, object]]:
    if cache_valid(papers):
        embeddings = np.load(EMBEDDING_CACHE)
        meta = json.loads(EMBEDDING_META.read_text(encoding="utf-8"))
        meta["loaded_from_cache"] = True
        return embeddings, meta

    embeddings, meta = build_transformer_embeddings(docs)
    np.save(EMBEDDING_CACHE, embeddings)
    meta.update(
        {
            "paper_count": len(papers),
            "first_title": papers[0].get("title", "") if papers else "",
            "last_title": papers[-1].get("title", "") if papers else "",
            "loaded_from_cache": False,
        }
    )
    EMBEDDING_META.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return embeddings, meta


def choose_k(embeddings: np.ndarray) -> tuple[int, list[dict[str, object]]]:
    rng = np.random.default_rng(RANDOM_STATE)
    sample_size = min(2200, embeddings.shape[0])
    sample_idx = rng.choice(embeddings.shape[0], size=sample_size, replace=False)
    best_k = K_CANDIDATES[0]
    best_score = -1.0
    diagnostics = []
    for k in K_CANDIDATES:
        model = MiniBatchKMeans(
            n_clusters=k,
            random_state=RANDOM_STATE,
            batch_size=768,
            n_init=12,
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


def cluster_top_terms(tfidf_matrix, labels: np.ndarray, feature_names: np.ndarray, top_n: int = 16) -> dict[int, list[str]]:
    output = {}
    for cluster_id in sorted(set(labels)):
        mask = labels == cluster_id
        mean_tfidf = np.asarray(tfidf_matrix[mask].mean(axis=0)).ravel()
        top_idx = mean_tfidf.argsort()[::-1][:top_n]
        output[int(cluster_id)] = [str(feature_names[i]) for i in top_idx if mean_tfidf[i] > 0]
    return output


def split_semicolon(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def main() -> int:
    papers = read_csv(PROCESSED / "icml2026_papers.csv")
    theme_rows = read_csv(PROCESSED / "icml2026_theme_matrix.csv")
    alpha_rows = read_csv(PROCESSED / "alphaxiv_icml2026_joined.csv")
    lexical_rows = read_csv(PROCESSED / "icml2026_cluster_assignments.csv")
    if not papers:
        raise SystemExit("Run scripts/fetch_icml_virtual.py first.")
    if not theme_rows:
        raise SystemExit("Run scripts/build_researcher_landscape.py first.")
    if not lexical_rows:
        raise SystemExit("Run scripts/build_cluster_landscape.py first.")

    theme_by_title = {normalize_title(row["title"]): row for row in theme_rows}
    alpha_by_title = {normalize_title(row["title"]): row for row in alpha_rows}
    lexical_by_title = {normalize_title(row["title"]): row for row in lexical_rows}
    docs = [paper_text(row) for row in papers]

    embeddings, embedding_meta = load_or_build_embeddings(papers, docs)
    embeddings = normalize(embeddings)

    best_k, diagnostics = choose_k(embeddings)
    cluster_model = MiniBatchKMeans(
        n_clusters=best_k,
        random_state=RANDOM_STATE,
        batch_size=768,
        n_init=30,
        reassignment_ratio=0.01,
    )
    labels = cluster_model.fit_predict(embeddings)
    distances = cluster_model.transform(embeddings)

    pca = PCA(n_components=2, random_state=RANDOM_STATE)
    coords = pca.fit_transform(embeddings)

    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        ngram_range=(1, 2),
        min_df=5,
        max_df=0.45,
        max_features=50000,
        sublinear_tf=True,
    )
    tfidf = vectorizer.fit_transform(docs)
    terms_by_cluster = cluster_top_terms(tfidf, labels, vectorizer.get_feature_names_out())

    max_votes = max([intish(row.get("public_total_votes", "0")) for row in alpha_rows] or [1])
    max_recent = max([intish(row.get("visits_last_7_days", "0")) for row in alpha_rows] or [1])
    corpus_oral_rate = sum(row.get("is_oral") == "true" for row in papers) / len(papers)
    corpus_votes = sum(intish(row.get("public_total_votes", "0")) for row in alpha_rows)

    assignments = []
    cluster_to_rows: dict[int, list[dict[str, object]]] = defaultdict(list)
    lexical_labels = []
    semantic_labels = []
    for idx, (paper, cluster_id) in enumerate(zip(papers, labels)):
        key = normalize_title(paper["title"])
        theme_row = theme_by_title.get(key, {})
        alpha_row = alpha_by_title.get(key, {})
        lexical_row = lexical_by_title.get(key, {})
        votes = intish(alpha_row.get("public_total_votes", "0"))
        recent = intish(alpha_row.get("visits_last_7_days", "0"))
        distance = float(distances[idx, cluster_id])
        row = {
            "event_id": paper.get("event_id", ""),
            "semantic_cluster_id": int(cluster_id),
            "semantic_cluster_label": short_label(terms_by_cluster[int(cluster_id)]),
            "lexical_cluster_id": lexical_row.get("cluster_id", ""),
            "lexical_cluster_label": lexical_row.get("cluster_label", ""),
            "title": paper.get("title", ""),
            "topic": paper.get("topic", ""),
            "topic_group": paper.get("topic_group", "") or "Unknown",
            "themes": theme_row.get("themes", ""),
            "is_oral": paper.get("is_oral", "false"),
            "award": theme_row.get("award", ""),
            "public_total_votes": votes,
            "visits_last_7_days": recent,
            "github_stars": intish(alpha_row.get("github_stars", "0")),
            "composite_score": floatish(theme_row.get("score", "0")),
            "semantic_distance": round(distance, 5),
            "semantic_centrality": round(1 / (1 + distance), 5),
            "semantic_x": round(float(coords[idx, 0]), 6),
            "semantic_y": round(float(coords[idx, 1]), 6),
            "attention_score": round((votes / max_votes if max_votes else 0) + 0.5 * (recent / max_recent if max_recent else 0), 5),
            "url": paper.get("url", ""),
            "alphaxiv_url": alpha_row.get("alphaxiv_url", ""),
        }
        assignments.append(row)
        cluster_to_rows[int(cluster_id)].append(row)
        if lexical_row.get("cluster_id", "") != "":
            lexical_labels.append(int(lexical_row["cluster_id"]))
            semantic_labels.append(int(cluster_id))

    cluster_rows = []
    for cluster_id in sorted(cluster_to_rows):
        items = cluster_to_rows[cluster_id]
        topic_groups = Counter(str(row["topic_group"]) for row in items)
        themes = Counter()
        lexical_clusters = Counter(str(row["lexical_cluster_id"]) for row in items if str(row["lexical_cluster_id"]) != "")
        for row in items:
            for theme in split_semicolon(str(row["themes"])):
                themes[theme] += 1
        oral_count = sum(row["is_oral"] == "true" for row in items)
        award_count = sum(bool(row["award"]) for row in items)
        total_votes = sum(int(row["public_total_votes"]) for row in items)
        recent_visits = sum(int(row["visits_last_7_days"]) for row in items)
        oral_rate = oral_count / len(items)
        votes_per_paper = total_votes / len(items)
        central = sorted(items, key=lambda row: float(row["semantic_distance"]))[:8]
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
                "semantic_cluster_id": cluster_id,
                "semantic_cluster_label": short_label(terms_by_cluster[cluster_id]),
                "paper_count": len(items),
                "share": round(len(items) / len(papers), 4),
                "oral_count": oral_count,
                "oral_rate": round(oral_rate, 4),
                "oral_enrichment": round(oral_rate / corpus_oral_rate, 2) if corpus_oral_rate else "",
                "award_count": award_count,
                "total_public_votes": total_votes,
                "votes_per_paper": round(votes_per_paper, 2),
                "public_vote_share": round(total_votes / corpus_votes, 4) if corpus_votes else 0,
                "recent_visits_7d": recent_visits,
                "top_terms": "; ".join(terms_by_cluster[cluster_id][:16]),
                "top_topic_groups": "; ".join(f"{k} ({v})" for k, v in topic_groups.most_common(5)),
                "top_themes": "; ".join(f"{k} ({v})" for k, v in themes.most_common(5)),
                "top_lexical_clusters": "; ".join(f"{k} ({v})" for k, v in lexical_clusters.most_common(5)),
                "central_papers": " | ".join(str(row["title"]) for row in central),
                "high_signal_papers": " | ".join(str(row["title"]) for row in high_signal),
            }
        )
    cluster_rows.sort(key=lambda row: (-int(row["paper_count"]), int(row["semantic_cluster_id"])))

    overlap_rows = []
    for sem_id in sorted(cluster_to_rows):
        items = cluster_to_rows[sem_id]
        lex_counts = Counter(str(row["lexical_cluster_id"]) for row in items if str(row["lexical_cluster_id"]) != "")
        for lex_id, count in lex_counts.most_common(5):
            lex_label = next((row["lexical_cluster_label"] for row in items if str(row["lexical_cluster_id"]) == lex_id), "")
            overlap_rows.append(
                {
                    "semantic_cluster_id": sem_id,
                    "semantic_cluster_label": short_label(terms_by_cluster[sem_id]),
                    "lexical_cluster_id": lex_id,
                    "lexical_cluster_label": lex_label,
                    "overlap_count": count,
                    "semantic_cluster_share": round(count / len(items), 4),
                }
            )

    ari = adjusted_rand_score(lexical_labels, semantic_labels) if lexical_labels else 0.0
    nmi = normalized_mutual_info_score(lexical_labels, semantic_labels) if lexical_labels else 0.0
    diagnostics.append(
        {
            "k": "selected",
            "sample_silhouette_cosine": "",
            "min_cluster_size": min(Counter(labels).values()),
            "max_cluster_size": max(Counter(labels).values()),
            "selected_k": best_k,
            "lexical_adjusted_rand": round(float(ari), 4),
            "lexical_normalized_mutual_info": round(float(nmi), 4),
            "embedding_source": embedding_meta.get("embedding_source", ""),
            "model_name": embedding_meta.get("model_name", ""),
            "loaded_from_cache": embedding_meta.get("loaded_from_cache", ""),
        }
    )

    write_csv(
        PROCESSED / "icml2026_semantic_cluster_assignments.csv",
        assignments,
        [
            "event_id", "semantic_cluster_id", "semantic_cluster_label",
            "lexical_cluster_id", "lexical_cluster_label", "title", "topic", "topic_group",
            "themes", "is_oral", "award", "public_total_votes", "visits_last_7_days",
            "github_stars", "composite_score", "semantic_distance", "semantic_centrality",
            "semantic_x", "semantic_y", "attention_score", "url", "alphaxiv_url",
        ],
    )
    write_csv(
        PROCESSED / "icml2026_semantic_cluster_summary.csv",
        cluster_rows,
        [
            "semantic_cluster_id", "semantic_cluster_label", "paper_count", "share",
            "oral_count", "oral_rate", "oral_enrichment", "award_count",
            "total_public_votes", "votes_per_paper", "public_vote_share", "recent_visits_7d",
            "top_terms", "top_topic_groups", "top_themes", "top_lexical_clusters",
            "central_papers", "high_signal_papers",
        ],
    )
    write_csv(
        PROCESSED / "icml2026_semantic_cluster_diagnostics.csv",
        diagnostics,
        [
            "k", "sample_silhouette_cosine", "min_cluster_size", "max_cluster_size",
            "selected_k", "lexical_adjusted_rand", "lexical_normalized_mutual_info",
            "embedding_source", "model_name", "loaded_from_cache",
        ],
    )
    write_csv(
        PROCESSED / "icml2026_semantic_vs_lexical_cluster_overlap.csv",
        overlap_rows,
        [
            "semantic_cluster_id", "semantic_cluster_label", "lexical_cluster_id",
            "lexical_cluster_label", "overlap_count", "semantic_cluster_share",
        ],
    )

    lines = [
        "# ICML 2026 Semantic Cluster Landscape",
        "",
        f"Method: transformer sentence embeddings from `{MODEL_NAME}`, normalized k-means clustering, and TF-IDF terms used only for cluster labels.",
        f"Selected semantic cluster count: {best_k} from candidates {', '.join(map(str, K_CANDIDATES))}.",
        f"Embedding cache: `{EMBEDDING_CACHE.relative_to(ROOT)}`.",
        "",
        "## Diagnostics",
        "",
    ]
    for row in diagnostics:
        if row["k"] == "selected":
            continue
        chosen = " selected" if int(row["k"]) == best_k else ""
        lines.append(
            f"- k={row['k']}: silhouette={row['sample_silhouette_cosine']}, "
            f"size range={row['min_cluster_size']}-{row['max_cluster_size']}{chosen}"
        )
    lines.extend(
        [
            f"- Semantic-vs-lexical adjusted Rand index: {ari:.4f}",
            f"- Semantic-vs-lexical normalized mutual information: {nmi:.4f}",
            "",
            "Low agreement is not automatically bad. It marks where vocabulary clusters and semantic neighborhoods disagree, which is useful for manual landscape review.",
            "",
            "## Largest Semantic Clusters",
            "",
        ]
    )

    for row in cluster_rows[:18]:
        lines.append(f"### Semantic Cluster {row['semantic_cluster_id']}: {row['semantic_cluster_label']}")
        lines.append(
            f"- Size: {row['paper_count']} papers ({float(row['share']) * 100:.1f}%); "
            f"orals: {row['oral_count']}; awards: {row['award_count']}; votes/paper: {row['votes_per_paper']}"
        )
        lines.append(f"- Top terms: {row['top_terms']}")
        lines.append(f"- Topic groups: {row['top_topic_groups']}")
        lines.append(f"- Rule themes: {row['top_themes']}")
        lines.append(f"- Lexical overlaps: {row['top_lexical_clusters']}")
        lines.append("- Central papers:")
        for title in str(row["central_papers"]).split(" | ")[:4]:
            lines.append(f"  - {title}")
        lines.append("- High-signal papers:")
        for title in str(row["high_signal_papers"]).split(" | ")[:4]:
            lines.append(f"  - {title}")
        lines.append("")

    lines.extend(["## Highest Program Signal", ""])
    for row in sorted(cluster_rows, key=lambda r: (float(r["oral_enrichment"]), int(r["oral_count"])), reverse=True)[:10]:
        lines.append(
            f"- Semantic cluster {row['semantic_cluster_id']} ({row['semantic_cluster_label']}): "
            f"{float(row['oral_rate']) * 100:.1f}% oral, {row['oral_enrichment']}x corpus baseline, {row['paper_count']} papers"
        )

    lines.extend(["", "## Highest Public Attention Density", ""])
    for row in sorted(cluster_rows, key=lambda r: float(r["votes_per_paper"]), reverse=True)[:10]:
        lines.append(
            f"- Semantic cluster {row['semantic_cluster_id']} ({row['semantic_cluster_label']}): "
            f"{row['votes_per_paper']} votes/paper, {float(row['public_vote_share']) * 100:.1f}% of public votes, {row['paper_count']} papers"
        )

    lines.extend(
        [
            "",
            "## Researcher Use",
            "",
            "- Use semantic clusters to identify neighborhoods that the lexical TF-IDF/SVD baseline may split by surface vocabulary.",
            "- Use the semantic-vs-lexical overlap table to find unstable areas that need manual naming before slide or report use.",
            "- Do not treat cluster IDs as final taxonomy labels. The IDs are stable only for this snapshot and script configuration.",
        ]
    )
    report_path = REPORTS / "icml2026_semantic_cluster_landscape.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Selected semantic k={best_k}")
    print(f"Wrote {PROCESSED / 'icml2026_semantic_cluster_assignments.csv'}")
    print(f"Wrote {PROCESSED / 'icml2026_semantic_cluster_summary.csv'}")
    print(f"Wrote {PROCESSED / 'icml2026_semantic_cluster_diagnostics.csv'}")
    print(f"Wrote {PROCESSED / 'icml2026_semantic_vs_lexical_cluster_overlap.csv'}")
    print(f"Wrote {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
