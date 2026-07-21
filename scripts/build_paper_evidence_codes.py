#!/usr/bin/env python3
"""Heuristically code paper-level evidence for taxonomy fault-line synthesis."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"


CONTRIBUTION_PATTERNS = {
    "Benchmark / evaluation": [
        r"\bbenchmark\w*\b", r"\bevaluation\s+(suite|harness|benchmark|protocol)\b", r"\bdiagnostic\s+benchmark\b",
        r"\bsuite\b", r"\bleaderboard\b", r"\btestbed\b", r"\bharness\b",
    ],
    "Dataset / data resource": [
        r"\bdataset\w*\b", r"\bcorpus\b", r"\bdata\s+set\b", r"\bdata\s+engine\b",
        r"\bannotation\w*\b", r"\blabel\w*\b", r"\bsynthetic\s+data\b",
    ],
    "Method / algorithm": [
        r"\bmethod\b", r"\balgorithm\w*\b", r"\bframework\b", r"\bapproach\b",
        r"\btraining\b", r"\boptimiz\w+\b", r"\barchitecture\b",
    ],
    "Theory / proof": [
        r"\btheorem\b", r"\bproof\b", r"\bprovabl\w*\b", r"\bbound\w*\b",
        r"\bconvergence\b", r"\bregret\b", r"\bcomplexity\b", r"\bguarantee\w*\b",
    ],
    "System / infrastructure": [
        r"\bsystem\b", r"\bserving\b", r"\bthroughput\b", r"\blatency\b", r"\bgpu\b",
        r"\bkernels?\b", r"\bcompiler\b", r"\bmemory\b", r"\bcache\b",
    ],
    "Position / conceptual": [
        r"^position:", r"\bposition\s+paper\b", r"\bargue\w*\b", r"\bcall\s+for\b",
        r"\bperspective\b", r"\bsurvey\b", r"\btaxonomy\b",
    ],
    "Application / domain study": [
        r"\bprotein\b", r"\bmolecule\w*\b", r"\bmedical\b", r"\bgenomic\w*\b",
        r"\brobot\w*\b", r"\bclimate\b", r"\bweather\b", r"\bfinance\b", r"\bscience\b",
    ],
}

METHOD_PATTERNS = {
    "RL / policy optimization": [r"\breinforcement\b", r"\brl\b", r"\bpolicy\b", r"\breward\b", r"\bppo\b", r"\bgrpo\b"],
    "LLM post-training": [r"\bpost-training\b", r"\bfine-tun\w*\b", r"\balignment\b", r"\bpreference\b", r"\brlvr\b"],
    "Reasoning / test-time compute": [r"\breasoning\b", r"\bchain[- ]of[- ]thought\b", r"\bcot\b", r"\btest[- ]time\b", r"\bverif\w+\b"],
    "Agents / tool use": [r"\bagent\w*\b", r"\btool\w*\b", r"\bgui\b", r"\bweb\b", r"\bsoftware\b", r"\bcode\b"],
    "Diffusion / flow": [r"\bdiffusion\b", r"\bflow\b", r"\bscore-based\b", r"\bsampling\b", r"\bdenois\w+\b"],
    "Transformer / attention": [r"\btransformer\w*\b", r"\battention\b", r"\bkv[- ]?cache\b", r"\blong[- ]context\b"],
    "Compression / efficiency": [r"\bquantiz\w+\b", r"\bprun\w+\b", r"\bspars\w+\b", r"\bcompression\b", r"\bmoe\b", r"\blora\b"],
    "Causal / data-centric": [r"\bcausal\w*\b", r"\bdata\s+selection\b", r"\bdata\s+attribution\b", r"\bdataset\s+distillation\b"],
    "Bayesian / probabilistic": [r"\bbayesian\b", r"\bprobabilistic\b", r"\bposterior\b", r"\bvariational\b", r"\bmcmc\b"],
    "Graphs / geometry": [r"\bgraph\w*\b", r"\bgeometric\b", r"\bgeometry\b", r"\bequivariant\b", r"\bmanifold\b"],
}

EVALUATION_PATTERNS = {
    "math/code/verifiable": [r"\bmath\b", r"\bcode\b", r"\bprogram\w*\b", r"\bverifiable\b", r"\bunit\s+test\b"],
    "vision/video": [r"\bvision\b", r"\bimage\b", r"\bvideo\b", r"\b3d\b", r"\bspatial\b"],
    "robotics/embodied": [r"\brobot\w*\b", r"\bembodied\b", r"\bmanipulation\b", r"\baction\b", r"\bcontrol\b"],
    "language/llm": [r"\blanguage\b", r"\bllm\w*\b", r"\blarge\s+language\b", r"\btext\b"],
    "science/domain": [r"\bprotein\b", r"\bmolecule\w*\b", r"\bphysics\b", r"\bchemistry\b", r"\bmedical\b", r"\bweather\b"],
    "security/safety": [r"\bsafety\b", r"\battack\w*\b", r"\bjailbreak\b", r"\bprivacy\b", r"\bsecurity\b", r"\bbias\b"],
    "theory/synthetic": [r"\bsynthetic\b", r"\btheory\b", r"\btheoretical\b", r"\bproof\b", r"\bsimulation\b"],
}

RESULT_PATTERNS = {
    "negative / limitation": [r"\bfail\w*\b", r"\blimit\w*\b", r"\bnegative\b", r"\bnot\s+robust\b", r"\bmisalign\w*\b", r"\bfragil\w*\b"],
    "scaling / efficiency": [r"\bscal\w*\b", r"\befficient\b", r"\bfaster\b", r"\blatency\b", r"\bthroughput\b", r"\bmemory\b"],
    "robustness / safety": [r"\brobust\w*\b", r"\bsafe\w*\b", r"\bsecure\b", r"\bprivacy\b", r"\bdefen[cs]\w*\b"],
    "state-of-the-art / improvement": [r"\bstate[- ]of[- ]the[- ]art\b", r"\bsota\b", r"\boutperform\w*\b", r"\bimprov\w*\b"],
}

METRIC_PATTERNS = [
    r"\baccuracy\b", r"\bacc\b", r"\bf1\b", r"\bauroc\b", r"\bauprc\b", r"\bperplexity\b",
    r"\bpass@k\b", r"\bwin\s+rate\b", r"\bsuccess\s+rate\b", r"\breward\b", r"\bregret\b",
    r"\blatency\b", r"\bthroughput\b", r"\bmemory\b", r"\bflops?\b", r"\bfid\b", r"\bclip\b",
]

BENCHMARK_PATTERN = re.compile(r"\b[A-Z][A-Za-z0-9]*(?:Bench|Eval|Arena|Suite|QA|MME|MMLU|HumanEval|GSM8K|AIME|SWE-bench)[A-Za-z0-9\-]*\b")
DATASET_PATTERN = re.compile(r"\b[A-Z][A-Za-z0-9]*(?:Dataset|Set|Corpus|Data|DB)[A-Za-z0-9\-]*\b")


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


def intish(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def score_patterns(text: str, patterns: list[str]) -> int:
    return sum(1 for pattern in patterns if re.search(pattern, text, flags=re.IGNORECASE))


def tag_patterns(text: str, pattern_map: dict[str, list[str]], minimum: int = 1) -> list[str]:
    tags = []
    for tag, patterns in pattern_map.items():
        if score_patterns(text, patterns) >= minimum:
            tags.append(tag)
    return tags


def primary_contribution_type(title: str, text: str, benchmark_mentions: list[str], dataset_mentions: list[str]) -> tuple[str, list[str]]:
    tags = []
    if title.lower().startswith("position:") or score_patterns(text, CONTRIBUTION_PATTERNS["Position / conceptual"]):
        tags.append("Position / conceptual")
    if benchmark_mentions or score_patterns(text, CONTRIBUTION_PATTERNS["Benchmark / evaluation"]):
        tags.append("Benchmark / evaluation")
    if dataset_mentions or score_patterns(text, CONTRIBUTION_PATTERNS["Dataset / data resource"]):
        tags.append("Dataset / data resource")
    if score_patterns(text, CONTRIBUTION_PATTERNS["Theory / proof"]):
        tags.append("Theory / proof")
    if score_patterns(text, CONTRIBUTION_PATTERNS["System / infrastructure"]):
        tags.append("System / infrastructure")
    if score_patterns(text, CONTRIBUTION_PATTERNS["Application / domain study"]):
        tags.append("Application / domain study")
    if score_patterns(text, CONTRIBUTION_PATTERNS["Method / algorithm"]):
        tags.append("Method / algorithm")
    if not tags:
        return "Uncoded", []

    priority = [
        "Position / conceptual",
        "Benchmark / evaluation",
        "Dataset / data resource",
        "Theory / proof",
        "System / infrastructure",
        "Application / domain study",
        "Method / algorithm",
    ]
    tags = [tag for tag in priority if tag in tags]
    return tags[0], tags


def extract_terms(text: str, pattern: re.Pattern[str], limit: int = 8) -> list[str]:
    seen = []
    for match in pattern.findall(text):
        if match not in seen:
            seen.append(match)
        if len(seen) == limit:
            break
    return seen


def evidence_confidence(row: dict[str, object]) -> str:
    points = 0
    if row["contribution_types"]:
        points += 1
    if row["method_families"]:
        points += 1
    if row["evaluation_settings"]:
        points += 1
    if row["benchmark_mentions"] or row["metric_mentions"] or row["dataset_mentions"]:
        points += 1
    if len(str(row["abstract"])) > 400:
        points += 1
    if points >= 4:
        return "medium"
    if points >= 2:
        return "low"
    return "very_low"


def main() -> int:
    taxonomy_rows = read_csv(PROCESSED / "icml2026_manual_taxonomy_papers.csv")
    official_rows = read_csv(PROCESSED / "icml2026_papers.csv")
    official_by_title = {normalize_title(row["title"]): row for row in official_rows}

    coded_rows = []
    for row in taxonomy_rows:
        official = official_by_title.get(normalize_title(row["title"]), {})
        abstract = official.get("abstract", "")
        text = " ".join([row["title"], row.get("topic", ""), abstract])
        method_families = tag_patterns(text, METHOD_PATTERNS)
        evaluation_settings = tag_patterns(text, EVALUATION_PATTERNS)
        result_claims = tag_patterns(text, RESULT_PATTERNS)
        metric_mentions = []
        for pattern in METRIC_PATTERNS:
            for match in re.findall(pattern, text, flags=re.IGNORECASE):
                value = match.lower().replace(" ", "_")
                if value not in metric_mentions:
                    metric_mentions.append(value)
        benchmark_mentions = extract_terms(text, BENCHMARK_PATTERN)
        dataset_mentions = extract_terms(text, DATASET_PATTERN)
        primary_type, contribution_types = primary_contribution_type(row["title"], text, benchmark_mentions, dataset_mentions)
        artifact_type = "github_url" if row.get("github_url") else "no_github_url"
        coded = {
            "event_id": row["event_id"],
            "title": row["title"],
            "area": row["area"],
            "subarea": row["subarea"],
            "semantic_cluster_id": row["semantic_cluster_id"],
            "is_oral": row["is_oral"],
            "award": row["award"],
            "public_total_votes": intish(row["public_total_votes"]),
            "github_url": row["github_url"],
            "artifact_confidence": row["artifact_confidence"],
            "contribution_types": "; ".join(contribution_types),
            "primary_contribution_type": primary_type,
            "method_families": "; ".join(method_families),
            "evaluation_settings": "; ".join(evaluation_settings),
            "result_claim_types": "; ".join(result_claims),
            "benchmark_mentions": "; ".join(benchmark_mentions),
            "dataset_mentions": "; ".join(dataset_mentions),
            "metric_mentions": "; ".join(metric_mentions[:10]),
            "artifact_type": artifact_type,
            "evidence_text_available": str(bool(abstract)).lower(),
            "abstract": abstract,
            "url": row["url"],
            "alphaxiv_url": row["alphaxiv_url"],
        }
        coded["evidence_confidence"] = evidence_confidence(coded)
        coded_rows.append(coded)

    area_groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in coded_rows:
        area_groups[str(row["area"])].append(row)

    summary_rows = []
    for area, rows in sorted(area_groups.items()):
        contribution = Counter(str(row["primary_contribution_type"]) for row in rows)
        all_contrib = Counter()
        methods = Counter()
        evals = Counter()
        results = Counter()
        confidence = Counter(str(row["evidence_confidence"]) for row in rows)
        benchmark_count = 0
        dataset_count = 0
        metric_count = 0
        github_count = 0
        for row in rows:
            all_contrib.update(tag for tag in str(row["contribution_types"]).split("; ") if tag)
            methods.update(tag for tag in str(row["method_families"]).split("; ") if tag)
            evals.update(tag for tag in str(row["evaluation_settings"]).split("; ") if tag)
            results.update(tag for tag in str(row["result_claim_types"]).split("; ") if tag)
            benchmark_count += bool(row["benchmark_mentions"])
            dataset_count += bool(row["dataset_mentions"])
            metric_count += bool(row["metric_mentions"])
            github_count += bool(row["github_url"])
        high_signal = sorted(
            rows,
            key=lambda row: (
                bool(row["award"]),
                row["is_oral"] == "true",
                int(row["public_total_votes"]),
            ),
            reverse=True,
        )[:10]
        summary_rows.append(
            {
                "area": area,
                "paper_count": len(rows),
                "github_url_count": github_count,
                "github_url_share": round(github_count / len(rows), 4),
                "benchmark_mention_count": benchmark_count,
                "benchmark_mention_share": round(benchmark_count / len(rows), 4),
                "dataset_mention_count": dataset_count,
                "dataset_mention_share": round(dataset_count / len(rows), 4),
                "metric_mention_count": metric_count,
                "metric_mention_share": round(metric_count / len(rows), 4),
                "top_primary_contribution_types": "; ".join(f"{k} ({v})" for k, v in contribution.most_common(8)),
                "top_all_contribution_types": "; ".join(f"{k} ({v})" for k, v in all_contrib.most_common(8)),
                "top_method_families": "; ".join(f"{k} ({v})" for k, v in methods.most_common(8)),
                "top_evaluation_settings": "; ".join(f"{k} ({v})" for k, v in evals.most_common(8)),
                "top_result_claim_types": "; ".join(f"{k} ({v})" for k, v in results.most_common(8)),
                "evidence_confidence_mix": "; ".join(f"{k} ({v})" for k, v in confidence.most_common()),
                "high_signal_examples": " | ".join(str(row["title"]) for row in high_signal[:8]),
            }
        )

    write_csv(
        PROCESSED / "icml2026_paper_evidence_codes.csv",
        coded_rows,
        [
            "event_id", "title", "area", "subarea", "semantic_cluster_id", "is_oral", "award",
            "public_total_votes", "github_url", "artifact_confidence", "primary_contribution_type",
            "contribution_types", "method_families", "evaluation_settings", "result_claim_types",
            "benchmark_mentions", "dataset_mentions", "metric_mentions", "artifact_type",
            "evidence_text_available", "evidence_confidence", "abstract", "url", "alphaxiv_url",
        ],
    )
    write_csv(
        PROCESSED / "icml2026_area_evidence_summary.csv",
        summary_rows,
        [
            "area", "paper_count", "github_url_count", "github_url_share",
            "benchmark_mention_count", "benchmark_mention_share", "dataset_mention_count",
            "dataset_mention_share", "metric_mention_count", "metric_mention_share",
            "top_primary_contribution_types", "top_all_contribution_types", "top_method_families",
            "top_evaluation_settings", "top_result_claim_types", "evidence_confidence_mix",
            "high_signal_examples",
        ],
    )

    lines = [
        "# ICML 2026 Paper-Level Evidence Codes",
        "",
        "This report adds heuristic evidence tags to each paper using title, topic, and official abstract text.",
        "The tags are intended to guide manual review; they are not a substitute for reading the papers.",
        "",
        "## Snapshot",
        "",
        f"- Papers coded: {len(coded_rows):,}",
        f"- Areas summarized: {len(summary_rows):,}",
        f"- Papers with benchmark-like mentions: {sum(bool(row['benchmark_mentions']) for row in coded_rows):,}",
        f"- Papers with dataset-like mentions: {sum(bool(row['dataset_mentions']) for row in coded_rows):,}",
        f"- Papers with metric-like mentions: {sum(bool(row['metric_mentions']) for row in coded_rows):,}",
        "",
        "## Area Evidence Summary",
        "",
    ]
    for row in sorted(summary_rows, key=lambda r: int(r["paper_count"]), reverse=True):
        lines.append(f"### {row['area']}")
        lines.append(
            f"- Papers: {row['paper_count']}; benchmark mentions: {float(row['benchmark_mention_share']) * 100:.1f}%; "
            f"dataset mentions: {float(row['dataset_mention_share']) * 100:.1f}%; metric mentions: {float(row['metric_mention_share']) * 100:.1f}%; "
            f"GitHub URL share: {float(row['github_url_share']) * 100:.1f}%"
        )
        lines.append(f"- Primary contribution types: {row['top_primary_contribution_types']}")
        lines.append(f"- Method families: {row['top_method_families']}")
        lines.append(f"- Evaluation settings: {row['top_evaluation_settings']}")
        lines.append(f"- Result claim cues: {row['top_result_claim_types']}")
        lines.append(f"- Evidence confidence: {row['evidence_confidence_mix']}")
        lines.append("")

    lines.extend(
        [
            "## Caveats",
            "",
            "- Coding is regex/keyword based and intentionally conservative.",
            "- Benchmark and dataset mentions are extracted from naming patterns and will miss many plain-language references.",
            "- `evidence_confidence` measures how much text evidence and tag signal the heuristic found, not whether a paper is correct or important.",
            "- Publication-grade synthesis still requires manual paper review for representative and boundary papers.",
        ]
    )
    report_path = REPORTS / "icml2026_paper_evidence_codes.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {PROCESSED / 'icml2026_paper_evidence_codes.csv'}")
    print(f"Wrote {PROCESSED / 'icml2026_area_evidence_summary.csv'}")
    print(f"Wrote {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
