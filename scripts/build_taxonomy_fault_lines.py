#!/usr/bin/env python3
"""Build area-level technical fault-line briefs from the curated taxonomy."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"


AREA_SYNTHESIS = {
    "LLM Reasoning, Post-Training, and RLVR": {
        "headline": "Reasoning progress is splitting between reward-driven post-training, test-time search, and alternative sequence modeling.",
        "fault_lines": [
            "Process supervision and reward models versus search, verification, and extra test-time compute.",
            "Verifiable math/code-style tasks versus open-ended research, planning, and multimodal reasoning.",
            "Autoregressive reasoning versus diffusion or arbitrary-order language generation.",
        ],
        "read_for": [
            "Does the paper optimize final answers, intermediate traces, rubrics, or verifier signals?",
            "Are gains robust outside tasks with cheap correctness checks?",
            "Does extra inference compute change capability, reliability, or only benchmark score?",
        ],
    },
    "Multimodal, Vision, and Perception": {
        "headline": "Vision-language work is moving from recognition toward grounded reasoning, spatial understanding, and video/world structure.",
        "fault_lines": [
            "Perception as feature extraction versus perception as an active reasoning bottleneck.",
            "Static image benchmarks versus long-video, 3D, spatial, and embodied settings.",
            "Generative visual models versus discriminative robustness and hallucination control.",
        ],
        "read_for": [
            "Can the method localize the visual evidence behind an answer?",
            "Does it evaluate temporal, 3D, or physical consistency rather than only caption-style accuracy?",
            "Are robustness claims tested under realistic corruptions, adversarial prompts, and distribution shift?",
        ],
    },
    "Theory, Optimization, and Algorithms": {
        "headline": "The theory track is balancing classical guarantees with explanations of transformer-era behavior.",
        "fault_lines": [
            "Asymptotic or idealized guarantees versus phenomena observed in current large-scale models.",
            "Optimization theory for convex/stochastic settings versus practical deep-network training dynamics.",
            "Probabilistic and Bayesian rigor versus scalable approximate inference.",
        ],
        "read_for": [
            "Which assumptions are doing the real work?",
            "Does the theorem explain a contemporary empirical pattern or stand as a separate mathematical result?",
            "Are constants, dimensions, and compute requirements meaningful at modern model scales?",
        ],
    },
    "AI for Science, Health, and Neuro": {
        "headline": "Scientific ML is broadening from surrogate modeling into foundation models for biological, physical, temporal, and neural data.",
        "fault_lines": [
            "General ML architecture contribution versus domain-specific modeling contribution.",
            "Benchmark performance versus scientific validity, uncertainty, and deployability.",
            "Foundation-model pretraining versus small-data, mechanistic, or simulation-grounded methods.",
        ],
        "read_for": [
            "Is the evaluation tied to a real scientific decision or only a proxy benchmark?",
            "Are domain constraints, units, symmetries, and uncertainty modeled explicitly?",
            "Does the method improve discovery or forecasting under realistic data scarcity?",
        ],
    },
    "Data-Centric, Causal, and Federated ML": {
        "headline": "Data quality, causality, and distributed learning are converging around what supervision is trustworthy.",
        "fault_lines": [
            "More data versus better selected, relabeled, distilled, or causally grounded data.",
            "Predictive correlations versus causal mechanisms and intervention validity.",
            "Centralized training assumptions versus privacy, federation, heterogeneity, and client incentives.",
        ],
        "read_for": [
            "Does the method improve data selection or merely add a new scoring heuristic?",
            "Are causal assumptions identifiable from the available data?",
            "Does the federated setup model realistic client drift, incentives, and system constraints?",
        ],
    },
    "Systems and Efficient Foundation Models": {
        "headline": "Efficiency papers increasingly claim capability relevance, not just lower cost.",
        "fault_lines": [
            "Training/inference cost reduction versus preservation of reasoning, calibration, and safety behavior.",
            "Kernel or hardware-specific wins versus algorithmic improvements that transfer across deployments.",
            "Long-context memory, KV-cache, quantization, MoE, and serving throughput as separate bottlenecks.",
        ],
        "read_for": [
            "Are results measured at realistic batch sizes, sequence lengths, hardware, and latency budgets?",
            "What capability regresses under compression or cache pruning?",
            "Is the speedup end-to-end or only for an isolated kernel/subroutine?",
        ],
    },
    "Safety, Governance, Privacy, and Society": {
        "headline": "Safety and society papers are programmatically central, but vary sharply in executable evidence.",
        "fault_lines": [
            "Technical safety benchmarks versus position papers about governance, harms, and conference norms.",
            "Attack/defense papers versus measurement validity and reproducibility of threat models.",
            "Privacy and unlearning guarantees versus practical utility and auditability.",
        ],
        "read_for": [
            "Is the harm or threat model operationalized precisely enough to test?",
            "Can the benchmark, attack, or defense be independently reproduced?",
            "Does the paper separate empirical evidence from normative argument?",
        ],
    },
    "Agents, Code, and Tool Use": {
        "headline": "Agents are shifting from impressive demos toward evaluation harnesses, tool environments, and software/security tasks.",
        "fault_lines": [
            "Better scaffolding and prompting versus actual learned agent capability.",
            "Static benchmarks versus dynamic environments with hidden state, long horizons, and recovery from failure.",
            "Code and security agents as practical systems versus brittle benchmark optimizers.",
        ],
        "read_for": [
            "Does the environment prevent leakage and reward shortcut behavior?",
            "Is improvement coming from model training, search, memory, tools, or evaluation-loop design?",
            "Are failures categorized by planning, perception, tool use, memory, or execution?",
        ],
    },
    "Graphs, Geometry, and Representation Learning": {
        "headline": "Graph and geometric methods remain a bridge between structure-aware theory and domain-specific representations.",
        "fault_lines": [
            "Equivariance and invariance as architectural priors versus learned latent geometry.",
            "Graph foundation/generalization claims versus task-specific message-passing improvements.",
            "Theoretical expressivity versus scalability on real graph and geometric data.",
        ],
        "read_for": [
            "Which symmetries or structural assumptions are encoded, and are they valid for the data?",
            "Does the method scale beyond curated graph benchmarks?",
            "Are representation claims validated by transfer, robustness, or interpretability?",
        ],
    },
    "Generative Modeling": {
        "headline": "Diffusion and flow models are splitting into practical media generation, language alternatives, and sampling theory.",
        "fault_lines": [
            "Sampling-theory guarantees versus image/video generation quality and latency.",
            "Autoregressive generation versus diffusion or flow-based sequence generation.",
            "Better visual fidelity versus controllability, consistency, and editing reliability.",
        ],
        "read_for": [
            "Do speedups preserve quality under realistic inference budgets?",
            "Are theoretical sampling improvements visible in practical model behavior?",
            "Does generation remain consistent over long videos, edits, or conditional controls?",
        ],
    },
    "Reinforcement Learning and Control": {
        "headline": "Core RL is active but less publicly amplified than LLM-facing RL, with emphasis on offline learning, control, and computation.",
        "fault_lines": [
            "Classical RL/control objectives versus foundation-model-era policy learning.",
            "Offline and preference-based RL versus online exploration and sample efficiency.",
            "Theoretical computation limits versus practical robotic/control deployment.",
        ],
        "read_for": [
            "Does the method require online interaction or strong simulator assumptions?",
            "How are stability, exploration, and reward misspecification handled?",
            "Is the contribution algorithmic, theoretical, or a new evaluation/control setting?",
        ],
    },
    "Robotics, Embodiment, and World Models": {
        "headline": "Robotics is becoming a high-attention testbed for VLA models, memory, latent actions, and world models.",
        "fault_lines": [
            "Vision-language-action pretraining versus robot-specific policy learning.",
            "Latent action/world-model abstractions versus real-world manipulation reliability.",
            "Benchmark scaling versus sim-to-real and long-horizon generalization.",
        ],
        "read_for": [
            "Does the model actually improve physical task success or only representation quality?",
            "Are actions, memory, and world states evaluated under distribution shift?",
            "How much depends on synthetic data, simulation, or curated demonstrations?",
        ],
    },
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


def split_values(value: str, delimiter: str = ";") -> list[str]:
    return [part.strip() for part in (value or "").split(delimiter) if part.strip()]


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z][a-z0-9\-]{2,}", text.lower())


def compact_join(items: list[str], limit: int = 5) -> str:
    return " | ".join(items[:limit])


def counter_join(counter: Counter[str], limit: int = 8) -> str:
    return "; ".join(f"{key} ({value})" for key, value in counter.most_common(limit))


def main() -> int:
    areas = read_csv(PROCESSED / "icml2026_manual_taxonomy_areas.csv")
    papers = read_csv(PROCESSED / "icml2026_manual_taxonomy_papers.csv")
    clusters = read_csv(PROCESSED / "icml2026_manual_taxonomy_clusters.csv")
    evidence_rows = read_csv(PROCESSED / "icml2026_area_evidence_summary.csv") if (PROCESSED / "icml2026_area_evidence_summary.csv").exists() else []
    evidence_by_area = {row["area"]: row for row in evidence_rows}

    papers_by_area: dict[str, list[dict[str, str]]] = defaultdict(list)
    clusters_by_area: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in papers:
        papers_by_area[row["area"]].append(row)
    for row in clusters:
        clusters_by_area[row["area"]].append(row)

    missing = sorted(set(row["area"] for row in areas) - set(AREA_SYNTHESIS))
    if missing:
        raise SystemExit(f"Missing area synthesis templates: {', '.join(missing)}")

    corpus_papers = sum(intish(row["paper_count"]) for row in areas)
    corpus_oral_rate = sum(intish(row["oral_count"]) for row in areas) / corpus_papers
    corpus_github_rate = sum(intish(row["github_url_count"]) for row in areas) / corpus_papers
    corpus_votes_per_paper = sum(intish(row["total_public_votes"]) for row in areas) / corpus_papers

    area_rows = []
    lines = [
        "# ICML 2026 Area Fault Lines",
        "",
        "This report uses the curated manual taxonomy as the organizing spine.",
        "It is meant to guide researcher reading and presentation narrative, not to replace paper-level review.",
        "",
        "## Corpus Baselines",
        "",
        f"- Papers: {corpus_papers:,}",
        f"- Corpus oral rate: {corpus_oral_rate * 100:.1f}%",
        f"- Corpus GitHub URL share: {corpus_github_rate * 100:.1f}%",
        f"- Corpus AlphaXiv public votes per paper: {corpus_votes_per_paper:.2f}",
        "",
        "## Area Briefs",
        "",
    ]

    for area in areas:
        area_name = area["area"]
        synthesis = AREA_SYNTHESIS[area_name]
        evidence_summary = evidence_by_area.get(area_name, {})
        area_papers = papers_by_area[area_name]
        area_clusters = clusters_by_area[area_name]
        subareas = Counter(row["subarea"] for row in area_papers)
        cluster_review = Counter(row["review_status"] for row in area_clusters)
        themes = Counter()
        title_terms = Counter()
        for row in area_papers:
            for theme in split_values(row.get("themes", "")):
                themes[theme] += 1
            title_terms.update(tokenize(row["title"]))
        high_signal = sorted(
            area_papers,
            key=lambda r: (
                bool(r["award"]),
                r["is_oral"] == "true",
                intish(r["public_total_votes"]),
                intish(r["visits_last_7_days"]),
            ),
            reverse=True,
        )
        high_public_not_oral = [
            row for row in sorted(area_papers, key=lambda r: intish(r["public_total_votes"]), reverse=True)
            if row["is_oral"] != "true" and not row["award"]
        ][:8]
        oral_low_public = [
            row for row in sorted(area_papers, key=lambda r: intish(r["public_total_votes"]))
            if row["is_oral"] == "true" or row["award"]
        ][:8]

        paper_count = intish(area["paper_count"])
        oral_rate = floatish(area["oral_rate"])
        github_share = floatish(area["github_url_share"])
        votes_per_paper = floatish(area["votes_per_paper"])
        evidence = [
            f"{paper_count:,} papers ({floatish(area['share']) * 100:.1f}% of corpus)",
            f"{intish(area['oral_count'])} orals and {intish(area['award_count'])} awards",
            f"{votes_per_paper:.2f} AlphaXiv public votes/paper",
            f"{github_share * 100:.1f}% GitHub URL share",
            f"{cluster_review.get('needs_review', 0)} of {len(area_clusters)} semantic clusters still need taxonomy review",
        ]
        if evidence_summary:
            evidence.append(f"primary contribution mix: {evidence_summary['top_primary_contribution_types']}")
            evidence.append(f"method-family cues: {evidence_summary['top_method_families']}")
            evidence.append(f"evaluation-setting cues: {evidence_summary['top_evaluation_settings']}")
        if oral_rate > corpus_oral_rate * 1.25:
            evidence.append("above-baseline oral density")
        if votes_per_paper > corpus_votes_per_paper * 1.25:
            evidence.append("above-baseline public attention density")
        if github_share > corpus_github_rate * 1.25:
            evidence.append("above-baseline GitHub URL availability")

        area_rows.append(
            {
                "area": area_name,
                "paper_count": paper_count,
                "oral_count": intish(area["oral_count"]),
                "award_count": intish(area["award_count"]),
                "votes_per_paper": votes_per_paper,
                "github_url_share": github_share,
                "taxonomy_clusters": len(area_clusters),
                "clusters_needing_review": cluster_review.get("needs_review", 0),
                "headline": synthesis["headline"],
                "fault_lines": " | ".join(synthesis["fault_lines"]),
                "read_for": " | ".join(synthesis["read_for"]),
                "evidence": " | ".join(evidence),
                "top_subareas": counter_join(subareas, 8),
                "top_themes": counter_join(themes, 8),
                "top_primary_contribution_types": evidence_summary.get("top_primary_contribution_types", ""),
                "top_method_families": evidence_summary.get("top_method_families", ""),
                "top_evaluation_settings": evidence_summary.get("top_evaluation_settings", ""),
                "top_result_claim_types": evidence_summary.get("top_result_claim_types", ""),
                "representative_papers": compact_join([row["title"] for row in high_signal], 8),
                "public_not_program_papers": compact_join([row["title"] for row in high_public_not_oral], 8),
                "program_not_public_papers": compact_join([row["title"] for row in oral_low_public], 8),
            }
        )

        lines.append(f"### {area_name}")
        lines.append("")
        lines.append(synthesis["headline"])
        lines.append("")
        lines.append("Evidence:")
        for item in evidence:
            lines.append(f"- {item}")
        lines.append("")
        lines.append("Fault lines:")
        for item in synthesis["fault_lines"]:
            lines.append(f"- {item}")
        lines.append("")
        lines.append("What to read for:")
        for item in synthesis["read_for"]:
            lines.append(f"- {item}")
        lines.append("")
        lines.append(f"Subareas: {counter_join(subareas, 8)}")
        lines.append(f"Top themes: {counter_join(themes, 8)}")
        if evidence_summary:
            lines.append(f"Evidence-coded contribution types: {evidence_summary['top_primary_contribution_types']}")
            lines.append(f"Evidence-coded method families: {evidence_summary['top_method_families']}")
            lines.append(f"Evidence-coded evaluation settings: {evidence_summary['top_evaluation_settings']}")
        lines.append("")
        lines.append("Representative/high-signal papers:")
        for row in high_signal[:6]:
            flags = [flag for flag in [row["award"], "oral" if row["is_oral"] == "true" else ""] if flag]
            flag_text = f" ({'; '.join(flags)})" if flags else ""
            lines.append(f"- {row['title']}{flag_text}; votes {row['public_total_votes']}")
        lines.append("")
        lines.append("Public-attention candidates not marked oral/award:")
        for row in high_public_not_oral[:4]:
            lines.append(f"- {row['title']}; votes {row['public_total_votes']}")
        lines.append("")
        lines.append("Program-signal candidates with lower public attention:")
        for row in oral_low_public[:4]:
            flags = [flag for flag in [row["award"], "oral" if row["is_oral"] == "true" else ""] if flag]
            flag_text = f" ({'; '.join(flags)})" if flags else ""
            lines.append(f"- {row['title']}{flag_text}; votes {row['public_total_votes']}")
        lines.append("")

    lines.extend(
        [
            "## Cross-Area Takeaways",
            "",
            "- Public attention concentrates in LLM reasoning/RLVR, robotics/VLA, agents, and systems; program signal is more evenly spread across theory, safety, science, and generative modeling.",
            "- GitHub URL availability is highest in applied foundation-model areas and weakest in theory-heavy areas, so artifact coverage should not be interpreted as field quality.",
            "- The highest-value manual review work is no longer finding clusters; it is resolving boundary clusters and turning these fault lines into paper-level claims.",
            "",
            "## Caveats",
            "",
            "- Fault lines are synthesis prompts grounded in taxonomy statistics and representative titles, not final literature-review conclusions.",
            "- AlphaXiv public votes are attention signals, not quality labels.",
            "- Oral/award labels are program signals, but they do not exhaust paper quality or importance.",
            "- Taxonomy areas inherit the `needs_review` flags from the manual taxonomy seed.",
        ]
    )

    write_csv(
        PROCESSED / "icml2026_area_fault_lines.csv",
        area_rows,
        [
            "area", "paper_count", "oral_count", "award_count", "votes_per_paper",
            "github_url_share", "taxonomy_clusters", "clusters_needing_review", "headline",
            "fault_lines", "read_for", "evidence", "top_subareas", "top_themes",
            "top_primary_contribution_types", "top_method_families", "top_evaluation_settings",
            "top_result_claim_types", "representative_papers", "public_not_program_papers",
            "program_not_public_papers",
        ],
    )
    report_path = REPORTS / "icml2026_area_fault_lines.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {PROCESSED / 'icml2026_area_fault_lines.csv'}")
    print(f"Wrote {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
