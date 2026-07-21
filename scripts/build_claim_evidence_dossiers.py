#!/usr/bin/env python3
"""Build claim-level evidence dossiers to accelerate manual review."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"
DOSSIER_DIR = REPORTS / "claim_evidence_dossiers"

PRIORITY_CLAIMS = {"C01", "C02", "C03", "C07"}


CLAIM_KEYWORDS = {
    "C01": [
        "language model", "llm", "reasoning", "post-training", "reinforcement learning",
        "reward", "grpo", "pre-training", "diffusion language", "memorization",
    ],
    "C02": [
        "system", "efficient", "inference", "training", "cache", "agent", "tool",
        "software", "code", "latency", "throughput", "optimization",
    ],
    "C03": [
        "theory", "proof", "convergence", "safety", "alignment", "governance",
        "privacy", "position", "risk", "deception", "jailbreak",
    ],
    "C04": ["robot", "embodied", "world model", "vision-language-action", "vla", "policy", "simulation"],
    "C05": ["vision", "multimodal", "video", "3d", "perception", "image", "spatial"],
    "C06": ["arxiv", "trend", "growth", "foundation", "language model", "multimodal", "safety"],
    "C07": ["github", "code", "repository", "implementation", "benchmark", "dataset", "open-source", "artifact"],
    "C08": ["taxonomy", "boundary", "cluster", "subarea", "classification", "label"],
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


def inum(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def excerpt(text: str, limit: int = 520) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) <= limit:
        return text
    return text[: limit - 3].rsplit(" ", 1)[0] + "..."


def keyword_hits(claim_id: str, row: dict[str, str]) -> list[str]:
    haystack = " ".join([row.get("title", ""), row.get("abstract", ""), row.get("method_families", ""), row.get("evaluation_settings", "")]).lower()
    return [word for word in CLAIM_KEYWORDS.get(claim_id, []) if word in haystack]


def pre_review_bucket(claim_id: str, row: dict[str, str], hits: list[str]) -> tuple[str, str]:
    title = row.get("title", "").lower()
    abstract = row.get("abstract", "").lower()
    area = row.get("area", "")
    if claim_id == "C01":
        if area == "LLM Reasoning, Post-Training, and RLVR" and any(hit in hits for hit in ["language model", "llm", "reasoning", "reinforcement learning", "reward", "diffusion language", "memorization"]):
            return "likely_supports", "Abstract/title centrally discuss LLMs, reasoning, memorization, diffusion language models, or RL/post-training."
        if "pre-training" in hits or "data selection" in title:
            return "boundary_case", "Looks LLM-related but may be data-centric or systems/pretraining rather than reasoning/post-training."
    if claim_id == "C02":
        if area in {"Systems and Efficient Foundation Models", "Agents, Code, and Tool Use"} and any(hit in hits for hit in ["efficient", "inference", "training", "cache", "agent", "tool", "software", "code"]):
            return "likely_supports", "Abstract/title is directly about systems efficiency, agents, tools, or software/code workloads."
    if claim_id == "C03":
        if area in {"Theory, Optimization, and Algorithms", "Safety, Governance, Privacy, and Society"} and row.get("is_oral") == "true":
            return "likely_supports", "Program-selected paper in theory or safety/governance area."
        if "position" in title:
            return "likely_supports", "Position-paper framing supports the governance/program-signal part of the claim."
    if claim_id == "C07":
        if row.get("needs_manual_check_reason"):
            return "high_risk_artifact", "GitHub URL is explicitly flagged for manual artifact checking."
        if row.get("github_url") and inum(row.get("github_stars", "")) >= 100:
            return "high_visibility_artifact", "GitHub-linked paper with high star count; needs artifact-type review."
    if hits:
        return "possible_support", "Keyword overlap with the claim, but human reading is needed."
    if not abstract:
        return "insufficient_text", "No abstract text available in the local evidence table."
    return "unclear", "No strong abstract/title cue for the claim."


def score_row(row: dict[str, str]) -> tuple[int, int, int, str]:
    return (
        1 if row.get("award") else 0,
        1 if row.get("is_oral") == "true" else 0,
        inum(row.get("public_total_votes", "")),
        row.get("title", ""),
    )


def load_inputs() -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, dict[str, str]]]:
    claims = read_csv(PROCESSED / "icml2026_landscape_claim_register.csv")
    queue = read_csv(PROCESSED / "icml2026_claim_validation_queue.csv")
    progress = {row["group"]: row for row in read_csv(PROCESSED / "manual_review_progress.csv") if row["queue_type"] == "claim_validation"}
    return claims, queue, progress


def build_dossier_rows(claims: list[dict[str, str]], queue: list[dict[str, str]]) -> list[dict[str, object]]:
    claim_meta = {row["claim_id"]: row for row in claims}
    out: list[dict[str, object]] = []
    for row in queue:
        claim_id = row["claim_id"]
        hits = keyword_hits(claim_id, row)
        bucket, rationale = pre_review_bucket(claim_id, row, hits)
        out.append(
            {
                "claim_id": claim_id,
                "claim_theme": claim_meta.get(claim_id, {}).get("theme", row.get("claim_theme", "")),
                "claim_strength": row.get("claim_strength", ""),
                "priority_claim": "true" if claim_id in PRIORITY_CLAIMS else "false",
                "claim_review_rank": row.get("claim_review_rank", ""),
                "event_id": row.get("event_id", ""),
                "title": row.get("title", ""),
                "area": row.get("area", ""),
                "subarea": row.get("subarea", ""),
                "selection_reason": row.get("selection_reason", ""),
                "pre_review_bucket": bucket,
                "pre_review_rationale": rationale,
                "keyword_hits": "; ".join(hits),
                "is_oral": row.get("is_oral", ""),
                "award": row.get("award", ""),
                "public_total_votes": row.get("public_total_votes", ""),
                "github_url": row.get("github_url", ""),
                "github_stars": row.get("github_stars", ""),
                "needs_manual_check_reason": row.get("needs_manual_check_reason", ""),
                "taxonomy_review_status": row.get("review_status", ""),
                "evidence_confidence": row.get("evidence_confidence", ""),
                "abstract_excerpt": excerpt(row.get("abstract", "")),
                "manual_claim_support": row.get("manual_claim_support", ""),
                "manual_taxonomy_judgment": row.get("manual_taxonomy_judgment", ""),
                "manual_artifact_judgment": row.get("manual_artifact_judgment", ""),
                "url": row.get("url", ""),
                "alphaxiv_url": row.get("alphaxiv_url", ""),
            }
        )
    out.sort(key=lambda item: (str(item["claim_id"]), int(str(item["claim_review_rank"]) or 0)))
    return out


def write_claim_dossier(claim: dict[str, str], rows: list[dict[str, object]], progress: dict[str, dict[str, str]]) -> Path:
    claim_id = claim["claim_id"]
    path = DOSSIER_DIR / f"{claim_id.lower()}-{slugify(claim['theme'])}.md"
    bucket_counts = Counter(str(row["pre_review_bucket"]) for row in rows)
    reason_counts = Counter(str(row["selection_reason"]) for row in rows)
    area_counts = Counter(str(row["area"]) for row in rows)
    remaining = progress.get(claim_id, {}).get("remaining_rows", str(len(rows)))
    reviewed = progress.get(claim_id, {}).get("reviewed_rows", "0")

    lines = [
        f"# {claim_id}: {claim['theme']} Evidence Dossier",
        "",
        "This is an abstract/title-based pre-review aid. It does not fill or replace the manual validation fields.",
        "",
        "## Claim",
        "",
        claim["statement"],
        "",
        f"- Strength label: `{claim['strength']}`",
        f"- Evidence summary: {claim['evidence']}",
        f"- Caveat: {claim['caveats']}",
        f"- Next validation: {claim['next_validation']}",
        f"- Manual review progress: {reviewed}/{len(rows)} rows reviewed; {remaining} remaining",
        "",
        "## Pre-Review Summary",
        "",
        f"- Bucket mix: {', '.join(f'{name}: {count}' for name, count in bucket_counts.most_common())}",
        f"- Selection mix: {', '.join(f'{name}: {count}' for name, count in reason_counts.most_common())}",
        f"- Area mix: {', '.join(f'{name}: {count}' for name, count in area_counts.most_common())}",
        "",
        "## Adjudication Questions",
        "",
        "- Does the abstract directly support the claim, or only share vocabulary with the claim?",
        "- Is the assigned taxonomy area central to the paper, or just one application/context?",
        "- If the paper is high-attention, is the attention driven by a reusable result, a benchmark, a demo, or a social trend?",
        "- If the paper has a GitHub link, is it a real paper artifact and what reproduction claim can be safely made?",
        "",
        "## Papers To Read First",
        "",
    ]
    top = sorted(rows, key=lambda row: score_row({k: str(v) for k, v in row.items()}), reverse=True)[:6]
    for row in top:
        flags = []
        if row["award"]:
            flags.append(str(row["award"]))
        if row["is_oral"] == "true":
            flags.append("oral")
        if row["taxonomy_review_status"] == "needs_review":
            flags.append("taxonomy-review")
        if row["github_url"]:
            flags.append("github")
        lines.append(f"- **{row['title']}** (`{row['pre_review_bucket']}`; {', '.join(flags) or 'no flags'}): {row['pre_review_rationale']}")

    lines.extend(
        [
            "",
            "## Paper-Level Pre-Review",
            "",
            "| Rank | Paper | Bucket | Area | Signals | Why It Matters |",
            "| ---: | --- | --- | --- | --- | --- |",
        ]
    )
    for row in rows:
        signals = []
        if row["award"]:
            signals.append(str(row["award"]))
        if row["is_oral"] == "true":
            signals.append("oral")
        if row["public_total_votes"]:
            signals.append(f"votes={row['public_total_votes']}")
        if row["github_url"]:
            signals.append(f"github_stars={row['github_stars'] or '0'}")
        if row["taxonomy_review_status"] == "needs_review":
            signals.append("taxonomy-review")
        lines.append(
            f"| {row['claim_review_rank']} | {row['title']} | {row['pre_review_bucket']} | "
            f"{row['area']} | {'; '.join(signals)} | {row['pre_review_rationale']} |"
        )

    lines.extend(["", "## Abstract Excerpts", ""])
    for row in rows:
        lines.extend(
            [
                f"### {row['claim_review_rank']}. {row['title']}",
                "",
                f"- Bucket: `{row['pre_review_bucket']}`",
                f"- Keyword hits: {row['keyword_hits'] or 'none'}",
                f"- URLs: [ICML]({row['url']})" + (f" / [AlphaXiv]({row['alphaxiv_url']})" if row["alphaxiv_url"] else ""),
                "",
                str(row["abstract_excerpt"]) or "No abstract excerpt available.",
                "",
            ]
        )

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_index(claims: list[dict[str, str]], dossier_rows: list[dict[str, object]], progress: dict[str, dict[str, str]]) -> None:
    by_claim: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in dossier_rows:
        by_claim[str(row["claim_id"])].append(row)

    lines = [
        "# ICML 2026 Claim Evidence Dossiers",
        "",
        "These dossiers are abstract/title-based pre-review aids for the synthesis claim packets.",
        "They are designed to help a researcher decide what to read first; they do not complete manual validation.",
        "",
        "## Snapshot",
        "",
        f"- Claim rows summarized: {len(dossier_rows)}",
        f"- Priority claim rows summarized: {sum(row['priority_claim'] == 'true' for row in dossier_rows)}",
        f"- Dossier files: {len(claims)}",
        "",
        "## Claim Dossier Index",
        "",
        "| Claim | Priority | Rows | Reviewed | Pre-Review Buckets | Dossier |",
        "| --- | --- | ---: | ---: | --- | --- |",
    ]
    for claim in claims:
        rows = by_claim[claim["claim_id"]]
        bucket_counts = Counter(str(row["pre_review_bucket"]) for row in rows)
        reviewed = progress.get(claim["claim_id"], {}).get("reviewed_rows", "0")
        path = DOSSIER_DIR / f"{claim['claim_id'].lower()}-{slugify(claim['theme'])}.md"
        rel_path = path.relative_to(REPORTS)
        lines.append(
            f"| {claim['claim_id']} - {claim['theme']} | {'yes' if claim['claim_id'] in PRIORITY_CLAIMS else 'no'} | "
            f"{len(rows)} | {reviewed} | {', '.join(f'{name}: {count}' for name, count in bucket_counts.most_common())} | "
            f"[open]({rel_path}) |"
        )

    lines.extend(
        [
            "",
            "## How To Use",
            "",
            "1. Start with C01, C02, C03, and C07.",
            "2. Read the papers marked `likely_supports`, `boundary_case`, `high_risk_artifact`, or `high_visibility_artifact` first.",
            "3. Fill the manual fields in `data/processed/icml2026_claim_validation_queue.csv` only after reading the paper or authoritative artifact page.",
            "4. Re-run `build_review_progress.py`, `build_researcher_readiness_audit.py`, and this script after manual fields are filled.",
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_claim_evidence_dossiers.csv`",
            "- `reports/icml2026_claim_evidence_dossier_index.md`",
            "- `reports/claim_evidence_dossiers/*.md`",
        ]
    )
    (REPORTS / "icml2026_claim_evidence_dossier_index.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    claims, queue, progress = load_inputs()
    DOSSIER_DIR.mkdir(parents=True, exist_ok=True)
    for path in DOSSIER_DIR.glob("*.md"):
        path.unlink()

    rows = build_dossier_rows(claims, queue)
    fieldnames = [
        "claim_id", "claim_theme", "claim_strength", "priority_claim", "claim_review_rank",
        "event_id", "title", "area", "subarea", "selection_reason", "pre_review_bucket",
        "pre_review_rationale", "keyword_hits", "is_oral", "award", "public_total_votes",
        "github_url", "github_stars", "needs_manual_check_reason", "taxonomy_review_status",
        "evidence_confidence", "abstract_excerpt", "manual_claim_support",
        "manual_taxonomy_judgment", "manual_artifact_judgment", "url", "alphaxiv_url",
    ]
    write_csv(PROCESSED / "icml2026_claim_evidence_dossiers.csv", rows, fieldnames)

    by_claim: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_claim[str(row["claim_id"])].append(row)
    for claim in claims:
        write_claim_dossier(claim, by_claim[claim["claim_id"]], progress)
    write_index(claims, rows, progress)

    print(f"Wrote {PROCESSED / 'icml2026_claim_evidence_dossiers.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_claim_evidence_dossier_index.md'}")
    print(f"Wrote {DOSSIER_DIR} ({len(list(DOSSIER_DIR.glob('*.md')))} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
