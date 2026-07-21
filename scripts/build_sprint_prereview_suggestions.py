#!/usr/bin/env python3
"""Generate machine pre-review prompts for the first ICML 2026 review sprint."""

from __future__ import annotations

import csv
import re
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


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def sentences(text: str) -> list[str]:
    text = clean(text)
    if not text:
        return []
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(])", text)
    return [part.strip() for part in parts if part.strip()]


def clip(text: str, limit: int = 320) -> str:
    text = clean(text)
    if len(text) <= limit:
        return text
    return text[: limit - 3].rsplit(" ", 1)[0] + "..."


def split_list(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def contribution_hypothesis(abstract: str, contribution_type: str) -> str:
    priority_patterns = [
        r"\bwe (propose|introduce|present|develop|show|prove|study|find|demonstrate)\b",
        r"\bthis paper (proposes|introduces|presents|develops|shows|proves|studies|finds)\b",
        r"\bour (method|framework|approach|algorithm|analysis|results?)\b",
    ]
    for sentence in sentences(abstract):
        lowered = sentence.lower()
        if any(re.search(pattern, lowered) for pattern in priority_patterns):
            return f"{contribution_type or 'Unclassified'}: {clip(sentence)}"
    first = sentences(abstract)[:1]
    return f"{contribution_type or 'Unclassified'}: {clip(first[0]) if first else 'Read abstract/PDF to identify the claimed contribution.'}"


def method_hypothesis(row: dict[str, str], abstract: str) -> str:
    families = row.get("method_families") or "no method-family tag"
    setting = row.get("evaluation_settings") or "no evaluation-setting tag"
    cues = []
    lowered = abstract.lower()
    for cue in ["reinforcement learning", "diffusion", "transformer", "benchmark", "theory", "gradient", "dataset", "agent", "tool", "multimodal", "safety"]:
        if cue in lowered:
            cues.append(cue)
    cue_text = "; ".join(cues[:6]) if cues else "no obvious abstract keyword cue"
    return f"Tags: {families}; setting: {setting}; abstract cues: {cue_text}."


def evidence_prompt(row: dict[str, str], abstract: str) -> str:
    checks = []
    if row.get("benchmark_mentions"):
        checks.append(f"benchmarks: {row['benchmark_mentions']}")
    if row.get("dataset_mentions"):
        checks.append(f"datasets: {row['dataset_mentions']}")
    if row.get("metric_mentions"):
        checks.append(f"metrics: {row['metric_mentions']}")
    lowered = abstract.lower()
    if "ablation" in lowered:
        checks.append("look for ablations")
    if "theorem" in lowered or "prove" in lowered or "provable" in lowered:
        checks.append("check theorem assumptions and empirical/theory split")
    if "human" in lowered or "user" in lowered:
        checks.append("check human-study or user-evaluation setup")
    if "real-world" in lowered or "robot" in lowered:
        checks.append("check sim-to-real or deployment evidence")
    if not checks:
        checks.append("identify baselines, datasets, metrics, ablations, and negative cases from the PDF")
    return "; ".join(checks)


def taxonomy_prompt(row: dict[str, str]) -> str:
    prompts = []
    if "taxonomy boundary" in row.get("signals", "").lower() or "taxonomy boundary" in row.get("why_first", "").lower():
        prompts.append("Resolve whether the assigned area/subarea is truly the main contribution.")
    if row.get("review_focus"):
        prompts.append(row["review_focus"])
    if not prompts:
        prompts.append("Check whether title/abstract evidence matches assigned area and subarea.")
    return " ".join(prompts)


def claim_implication(row: dict[str, str], claim_lookup: dict[str, str]) -> str:
    parts = []
    for claim_id in split_list(row.get("claim_ids", "")):
        theme = claim_lookup.get(claim_id, claim_id)
        parts.append(f"{claim_id} ({theme}): decide supports / weakens / complicates / not_applicable.")
    return " ".join(parts) if parts else "No linked synthesis claim; use for area validation only."


def artifact_prompt(row: dict[str, str]) -> str:
    if row.get("github_url"):
        return "Open GitHub link; record whether it is code, dataset, checkpoint, benchmark, project page, broken, or non-reproducible."
    if "artifact" in row.get("why_first", "").lower():
        return "Artifact was flagged but no GitHub URL is present; inspect ICML/AlphaXiv page for project or code links."
    return "No obvious artifact link; record none/not_applicable unless PDF shows a release."


def reviewer_warning(row: dict[str, str]) -> str:
    warnings = []
    why = row.get("why_first", "").lower()
    signals = row.get("signals", "").lower()
    if "high alphaxiv" in why or "votes=" in signals:
        warnings.append("Do not treat AlphaXiv attention as quality.")
    if "award" in signals or "oral" in signals:
        warnings.append("Program signal is not the same as paper-level correctness.")
    if "low-confidence" in why or "evidence=low" in signals:
        warnings.append("Heuristic evidence tag is low confidence.")
    if "taxonomy_review" in signals:
        warnings.append("Taxonomy assignment may be unstable.")
    return " ".join(warnings) if warnings else "No special warning beyond normal abstract/PDF verification."


def main() -> int:
    sprint = read_csv(PROCESSED / "icml2026_review_sprint_01.csv")
    papers = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_papers.csv")}
    explorer = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_paper_explorer.csv")}
    claims = {row["claim_id"]: row["theme"] for row in read_csv(PROCESSED / "icml2026_landscape_claim_register.csv")}

    rows: list[dict[str, object]] = []
    for row in sprint:
        event_id = row["event_id"]
        paper = papers.get(event_id, {})
        explore = explorer.get(event_id, {})
        abstract = paper.get("abstract", "") or row.get("abstract_excerpt", "")
        merged = {**row, **explore}
        rows.append(
            {
                "sprint_rank": row["sprint_rank"],
                "event_id": event_id,
                "title": row["title"],
                "area": row["area"],
                "subarea": row["subarea"],
                "claim_ids": row["claim_ids"],
                "contribution_hypothesis": contribution_hypothesis(abstract, explore.get("primary_contribution_type", "")),
                "method_hypothesis": method_hypothesis(merged, abstract),
                "evidence_to_verify": evidence_prompt(explore, abstract),
                "taxonomy_question": taxonomy_prompt(row),
                "claim_implication_prompt": claim_implication(row, claims),
                "artifact_check_prompt": artifact_prompt(row),
                "reviewer_warning": reviewer_warning(row),
                "suggested_note_seed": clip(
                    f"Contribution: {contribution_hypothesis(abstract, explore.get('primary_contribution_type', ''))} "
                    f"Evidence to verify: {evidence_prompt(explore, abstract)} "
                    f"Claim implication: {claim_implication(row, claims)}",
                    700,
                ),
                "abstract_basis": clip(abstract, 900),
            }
        )

    fieldnames = [
        "sprint_rank",
        "event_id",
        "title",
        "area",
        "subarea",
        "claim_ids",
        "contribution_hypothesis",
        "method_hypothesis",
        "evidence_to_verify",
        "taxonomy_question",
        "claim_implication_prompt",
        "artifact_check_prompt",
        "reviewer_warning",
        "suggested_note_seed",
        "abstract_basis",
    ]
    write_csv(PROCESSED / "icml2026_sprint_prereview_suggestions.csv", rows, fieldnames)

    lines = [
        "# ICML 2026 Sprint Pre-Review Suggestions",
        "",
        "Machine-generated prompts for the first review sprint.",
        "These are not manual judgments; use them to accelerate PDF reading and paper-note entry.",
        "",
        "## Snapshot",
        "",
        f"- Sprint papers covered: {len(rows)}",
        f"- Papers with claim links: {sum(bool(row['claim_ids']) for row in rows)}",
        f"- Papers with artifact prompts: {sum('GitHub' in str(row['artifact_check_prompt']) for row in rows)}",
        "",
        "## First Papers",
        "",
        "| Rank | Paper | Contribution hypothesis | Evidence to verify | Warning |",
        "| ---: | --- | --- | --- | --- |",
    ]
    for row in rows[:15]:
        lines.append(
            f"| {row['sprint_rank']} | {row['title']} | {row['contribution_hypothesis']} | "
            f"{row['evidence_to_verify']} | {row['reviewer_warning']} |"
        )
    lines.extend(
        [
            "",
            "## How To Use",
            "",
            "- Copy useful parts into `data/manual/icml2026_review_sprint_01_paper_notes.csv` only after reading the paper source.",
            "- Treat every suggestion as a hypothesis derived from title/abstract/tags.",
            "- Prefer the PDF over these suggestions when they disagree.",
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_sprint_prereview_suggestions.csv`",
            "- `reports/icml2026_sprint_prereview_suggestions.md`",
        ]
    )
    (REPORTS / "icml2026_sprint_prereview_suggestions.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {PROCESSED / 'icml2026_sprint_prereview_suggestions.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_sprint_prereview_suggestions.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
