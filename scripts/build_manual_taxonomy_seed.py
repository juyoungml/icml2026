#!/usr/bin/env python3
"""Build a manually curated taxonomy seed from semantic clusters."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"


TAXONOMY = {
    0: ("Multimodal, Vision, and Perception", "Multimodal representation and cross-modal alignment", "high"),
    1: ("AI for Science, Health, and Neuro", "Spiking neural networks and neural signals", "medium"),
    2: ("LLM Reasoning, Post-Training, and RLVR", "Reward modeling, preference feedback, and RL post-training", "high"),
    3: ("Systems and Efficient Foundation Models", "Long-context attention and KV-cache compression", "high"),
    4: ("Reinforcement Learning and Control", "Core RL, offline RL, and policy optimization", "high"),
    5: ("Data-Centric, Causal, and Federated ML", "Causal inference and causal discovery", "high"),
    6: ("Agents, Code, and Tool Use", "Code LLMs, verification, and software tasks", "medium"),
    7: ("Theory, Optimization, and Algorithms", "Statistical learning theory and regression", "high"),
    8: ("Generative Modeling", "Diffusion sampling, transport, and inverse problems", "high"),
    9: ("AI for Science, Health, and Neuro", "Physical sciences, chemistry, and climate", "high"),
    10: ("Data-Centric, Causal, and Federated ML", "Continual learning, forgetting, and task adaptation", "medium"),
    11: ("LLM Reasoning, Post-Training, and RLVR", "Reasoning models and chain-of-thought behavior", "high"),
    12: ("Safety, Governance, Privacy, and Society", "Adversarial safety, attacks, and security", "high"),
    13: ("AI for Science, Health, and Neuro", "Latent dynamics, neuroscience, and dynamical systems", "medium"),
    14: ("LLM Reasoning, Post-Training, and RLVR", "Diffusion language models and decoding", "high"),
    15: ("Graphs, Geometry, and Representation Learning", "Graph neural networks and graph learning", "high"),
    16: ("Robotics, Embodiment, and World Models", "Vision-language-action models and robotic manipulation", "high"),
    17: ("Data-Centric, Causal, and Federated ML", "Labels, datasets, and supervised data quality", "medium"),
    18: ("Graphs, Geometry, and Representation Learning", "Geometric representation learning and manifolds", "high"),
    19: ("Systems and Efficient Foundation Models", "Quantization and low-precision training/inference", "high"),
    20: ("Theory, Optimization, and Algorithms", "Transformer theory and attention expressivity", "medium"),
    21: ("LLM Reasoning, Post-Training, and RLVR", "LLM preference tuning and alignment training", "medium"),
    22: ("Multimodal, Vision, and Perception", "Vision-language reasoning and video understanding", "high"),
    23: ("Safety, Governance, Privacy, and Society", "Privacy, differential privacy, and unlearning", "high"),
    24: ("LLM Reasoning, Post-Training, and RLVR", "General LLM training, evaluation, and alignment", "medium"),
    25: ("Multimodal, Vision, and Perception", "3D, video, motion, and spatial understanding", "high"),
    26: ("Systems and Efficient Foundation Models", "Large-scale training, optimizers, and model architecture", "medium"),
    27: ("AI for Science, Health, and Neuro", "Protein, molecule, and biological modeling", "high"),
    28: ("Theory, Optimization, and Algorithms", "Convex, stochastic, and nonconvex optimization", "high"),
    29: ("Systems and Efficient Foundation Models", "Serving, GPU memory, MoE, and throughput", "high"),
    30: ("Agents, Code, and Tool Use", "Multi-agent search, planning, and coordination", "high"),
    31: ("Data-Centric, Causal, and Federated ML", "Federated learning and distributed clients", "high"),
    32: ("Theory, Optimization, and Algorithms", "Bayesian and probabilistic methods", "high"),
    33: ("Theory, Optimization, and Algorithms", "Online learning, bandits, and regret", "high"),
    34: ("Generative Modeling", "Image/video diffusion and flow generation", "high"),
    35: ("LLM Reasoning, Post-Training, and RLVR", "RL for reasoning models and verifiable rewards", "high"),
    36: ("Multimodal, Vision, and Perception", "Vision robustness, detection, and adversarial perception", "medium"),
    37: ("Safety, Governance, Privacy, and Society", "Position papers, policy, and social impacts", "high"),
    38: ("Theory, Optimization, and Algorithms", "Quantum, matrix, and numerical optimization", "medium"),
    39: ("AI for Science, Health, and Neuro", "Time series and forecasting applications", "medium"),
    40: ("Agents, Code, and Tool Use", "Agent evaluation, tool use, and agentic workflows", "high"),
    41: ("Graphs, Geometry, and Representation Learning", "Equivariant graph and geometric networks", "high"),
}


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


def floatish(value: str) -> float:
    try:
        return float(value or 0)
    except ValueError:
        return 0.0


def split_pipe(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split("|") if part.strip()]


def top_join(counter: Counter[str], n: int = 6) -> str:
    return "; ".join(f"{name} ({count})" for name, count in counter.most_common(n))


def cluster_review_status(row: dict[str, str], confidence: str) -> tuple[str, str]:
    count = intish(row["paper_count"])
    lexical_overlap = row.get("top_lexical_clusters", "")
    top_share = 0.0
    if lexical_overlap:
        first = lexical_overlap.split(";")[0]
        if "(" in first and ")" in first:
            top_count = intish(first.rsplit("(", 1)[-1].rstrip(")"))
            top_share = top_count / count if count else 0
    reasons = []
    if confidence != "high":
        reasons.append("manual confidence not high")
    if count < 75:
        reasons.append("small cluster")
    if top_share and top_share < 0.45:
        reasons.append("split across lexical clusters")
    if not reasons:
        return "stable_seed", ""
    return "needs_review", "; ".join(reasons)


def main() -> int:
    cluster_rows = read_csv(PROCESSED / "icml2026_semantic_cluster_summary.csv")
    assignment_rows = read_csv(PROCESSED / "icml2026_semantic_cluster_assignments.csv")
    repro_rows = read_csv(PROCESSED / "icml2026_reproducibility_papers.csv")
    repro_by_title = {row["title"]: row for row in repro_rows}

    cluster_taxonomy_rows = []
    cluster_lookup = {}
    for row in cluster_rows:
        cluster_id = intish(row["semantic_cluster_id"])
        if cluster_id not in TAXONOMY:
            raise SystemExit(f"Missing taxonomy mapping for semantic cluster {cluster_id}")
        area, subarea, confidence = TAXONOMY[cluster_id]
        status, notes = cluster_review_status(row, confidence)
        output = {
            "semantic_cluster_id": cluster_id,
            "area": area,
            "subarea": subarea,
            "taxonomy_confidence": confidence,
            "review_status": status,
            "review_notes": notes,
            "semantic_cluster_label": row["semantic_cluster_label"],
            "paper_count": intish(row["paper_count"]),
            "oral_count": intish(row["oral_count"]),
            "award_count": intish(row["award_count"]),
            "votes_per_paper": row["votes_per_paper"],
            "oral_enrichment": row["oral_enrichment"],
            "top_terms": row["top_terms"],
            "top_topic_groups": row["top_topic_groups"],
            "top_themes": row["top_themes"],
            "top_lexical_clusters": row["top_lexical_clusters"],
            "central_papers": row["central_papers"],
            "high_signal_papers": row["high_signal_papers"],
        }
        cluster_taxonomy_rows.append(output)
        cluster_lookup[str(cluster_id)] = output

    paper_rows = []
    area_groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in assignment_rows:
        cluster_info = cluster_lookup[row["semantic_cluster_id"]]
        repro = repro_by_title.get(row["title"], {})
        output = {
            "event_id": row["event_id"],
            "title": row["title"],
            "area": cluster_info["area"],
            "subarea": cluster_info["subarea"],
            "semantic_cluster_id": row["semantic_cluster_id"],
            "semantic_cluster_label": row["semantic_cluster_label"],
            "taxonomy_confidence": cluster_info["taxonomy_confidence"],
            "review_status": cluster_info["review_status"],
            "topic_group": row["topic_group"],
            "topic": row["topic"],
            "themes": row["themes"],
            "is_oral": row["is_oral"],
            "award": row["award"],
            "public_total_votes": intish(row["public_total_votes"]),
            "visits_last_7_days": intish(row["visits_last_7_days"]),
            "github_url": repro.get("github_url", ""),
            "artifact_confidence": repro.get("artifact_confidence", ""),
            "url": row["url"],
            "alphaxiv_url": row["alphaxiv_url"],
        }
        paper_rows.append(output)
        area_groups[str(cluster_info["area"])].append(output)

    area_rows = []
    for area, rows in area_groups.items():
        topic_counter = Counter(str(row["topic_group"]) for row in rows)
        subarea_counter = Counter(str(row["subarea"]) for row in rows)
        cluster_counter = Counter(str(row["semantic_cluster_id"]) for row in rows)
        oral_count = sum(row["is_oral"] == "true" for row in rows)
        award_count = sum(bool(row["award"]) for row in rows)
        total_votes = sum(int(row["public_total_votes"]) for row in rows)
        github_count = sum(bool(row["github_url"]) for row in rows)
        high_signal = sorted(
            rows,
            key=lambda r: (
                bool(r["award"]),
                r["is_oral"] == "true",
                int(r["public_total_votes"]),
                int(r["visits_last_7_days"]),
            ),
            reverse=True,
        )[:12]
        area_rows.append(
            {
                "area": area,
                "paper_count": len(rows),
                "share": round(len(rows) / len(paper_rows), 4),
                "oral_count": oral_count,
                "oral_rate": round(oral_count / len(rows), 4) if rows else 0,
                "award_count": award_count,
                "total_public_votes": total_votes,
                "votes_per_paper": round(total_votes / len(rows), 2) if rows else 0,
                "github_url_count": github_count,
                "github_url_share": round(github_count / len(rows), 4) if rows else 0,
                "subareas": top_join(subarea_counter, 12),
                "semantic_clusters": top_join(cluster_counter, 12),
                "top_topic_groups": top_join(topic_counter, 8),
                "representative_papers": " | ".join(str(row["title"]) for row in high_signal[:8]),
            }
        )

    cluster_taxonomy_rows.sort(key=lambda row: int(row["semantic_cluster_id"]))
    area_rows.sort(key=lambda row: (-int(row["paper_count"]), str(row["area"])))
    paper_rows.sort(key=lambda row: (str(row["area"]), str(row["subarea"]), -int(row["public_total_votes"]), str(row["title"])))

    write_csv(
        PROCESSED / "icml2026_manual_taxonomy_clusters.csv",
        cluster_taxonomy_rows,
        [
            "semantic_cluster_id", "area", "subarea", "taxonomy_confidence", "review_status",
            "review_notes", "semantic_cluster_label", "paper_count", "oral_count", "award_count",
            "votes_per_paper", "oral_enrichment", "top_terms", "top_topic_groups", "top_themes",
            "top_lexical_clusters", "central_papers", "high_signal_papers",
        ],
    )
    write_csv(
        PROCESSED / "icml2026_manual_taxonomy_areas.csv",
        area_rows,
        [
            "area", "paper_count", "share", "oral_count", "oral_rate", "award_count",
            "total_public_votes", "votes_per_paper", "github_url_count", "github_url_share",
            "subareas", "semantic_clusters", "top_topic_groups", "representative_papers",
        ],
    )
    write_csv(
        PROCESSED / "icml2026_manual_taxonomy_papers.csv",
        paper_rows,
        [
            "event_id", "title", "area", "subarea", "semantic_cluster_id", "semantic_cluster_label",
            "taxonomy_confidence", "review_status", "topic_group", "topic", "themes",
            "is_oral", "award", "public_total_votes", "visits_last_7_days", "github_url",
            "artifact_confidence", "url", "alphaxiv_url",
        ],
    )

    stable_clusters = sum(row["review_status"] == "stable_seed" for row in cluster_taxonomy_rows)
    lines = [
        "# ICML 2026 Manual Taxonomy Seed",
        "",
        "This is a curated seed taxonomy built on top of transformer semantic clusters.",
        "It is designed for researcher review, not as a final ontology.",
        "",
        "## Snapshot",
        "",
        f"- Papers assigned: {len(paper_rows):,}",
        f"- Semantic clusters mapped: {len(cluster_taxonomy_rows):,}",
        f"- Research areas: {len(area_rows):,}",
        f"- Stable seed clusters: {stable_clusters:,}",
        f"- Clusters needing review: {len(cluster_taxonomy_rows) - stable_clusters:,}",
        "",
        "## Area Map",
        "",
    ]
    for area in area_rows:
        lines.append(f"### {area['area']}")
        lines.append(
            f"- Size: {area['paper_count']} papers ({float(area['share']) * 100:.1f}%); "
            f"orals: {area['oral_count']}; awards: {area['award_count']}; "
            f"votes/paper: {area['votes_per_paper']}; GitHub URL share: {float(area['github_url_share']) * 100:.1f}%"
        )
        lines.append(f"- Subareas: {area['subareas']}")
        lines.append(f"- Topic groups: {area['top_topic_groups']}")
        lines.append("- Representative papers:")
        for title in split_pipe(str(area["representative_papers"]))[:6]:
            lines.append(f"  - {title}")
        lines.append("")

    lines.extend(["## Clusters Needing Manual Review", ""])
    for row in [row for row in cluster_taxonomy_rows if row["review_status"] != "stable_seed"]:
        lines.append(
            f"- Cluster {row['semantic_cluster_id']} -> {row['area']} / {row['subarea']}: "
            f"{row['review_notes']} ({row['paper_count']} papers; auto label: {row['semantic_cluster_label']})"
        )

    lines.extend(
        [
            "",
            "## How To Use This",
            "",
            "- Treat `area` as the current report-level taxonomy and `subarea` as a review queue.",
            "- Start manual review with clusters marked `needs_review`, especially medium-confidence clusters that split across lexical clusters.",
            "- When a subarea is renamed or moved, edit the `TAXONOMY` mapping in `scripts/build_manual_taxonomy_seed.py` and regenerate outputs.",
            "- Do not cite this taxonomy as ground truth without manual paper review of representative and boundary papers.",
        ]
    )
    report_path = REPORTS / "icml2026_manual_taxonomy_seed.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {PROCESSED / 'icml2026_manual_taxonomy_clusters.csv'}")
    print(f"Wrote {PROCESSED / 'icml2026_manual_taxonomy_areas.csv'}")
    print(f"Wrote {PROCESSED / 'icml2026_manual_taxonomy_papers.csv'}")
    print(f"Wrote {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
