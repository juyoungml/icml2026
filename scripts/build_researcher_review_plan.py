#!/usr/bin/env python3
"""Build a de-duplicated researcher review plan across claim and area queues."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"

PRIORITY_CLAIMS = {"C01", "C02", "C03", "C07"}
PRIORITY_AREAS = {
    "LLM Reasoning, Post-Training, and RLVR",
    "Systems and Efficient Foundation Models",
    "Agents, Code, and Tool Use",
    "Safety, Governance, Privacy, and Society",
    "Theory, Optimization, and Algorithms",
    "Multimodal, Vision, and Perception",
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


def fnum(value: str) -> float:
    try:
        return float(value or 0)
    except ValueError:
        return 0.0


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def packet_link_for_area(area: str) -> str:
    return f"reports/validation_packets/{slugify(area)}.md"


def claim_packet_link(claim_id: str, claim_theme: str) -> str:
    return f"reports/claim_validation_packets/{claim_id.lower()}-{slugify(claim_theme)}.md"


def claim_dossier_link(claim_id: str, claim_theme: str) -> str:
    return f"reports/claim_evidence_dossiers/{claim_id.lower()}-{slugify(claim_theme)}.md"


def area_card_link(area: str) -> str:
    return f"reports/area_briefing_cards/{slugify(area)}.md"


def phase_for(row: dict[str, object]) -> str:
    claim_ids = set(str(row["claim_ids"]).split("; ")) if row["claim_ids"] else set()
    area = str(row["area"])
    reasons = str(row["area_selection_reasons"] + "; " + row["claim_selection_reasons"])
    if claim_ids & {"C01", "C02", "C03"}:
        return "main_thesis_claims"
    if "artifact" in reasons or row["needs_manual_check_reason"]:
        return "artifact_and_reproducibility"
    if row["taxonomy_review_status"] == "needs_review" or "taxonomy_boundary" in reasons:
        return "taxonomy_boundaries"
    if "public_attention_not_program_signal" in reasons or "program_signal_low_public_attention" in reasons:
        return "public_program_divergence"
    if area in PRIORITY_AREAS:
        return "priority_area_depth"
    return "breadth_and_sanity_checks"


def score_entry(entry: dict[str, object]) -> tuple[float, list[str]]:
    score = 0.0
    reasons: list[str] = []
    claim_ids = set(str(entry["claim_ids"]).split("; ")) if entry["claim_ids"] else set()
    area = str(entry["area"])
    selection = str(entry["claim_selection_reasons"] + "; " + entry["area_selection_reasons"])

    if claim_ids:
        score += 10
        reasons.append("in claim-validation queue")
    priority_claims = sorted(claim_ids & PRIORITY_CLAIMS)
    if priority_claims:
        score += 20 + 4 * len(priority_claims)
        reasons.append("supports priority claim(s) " + ", ".join(priority_claims))
    if entry["in_area_queue"] == "true":
        score += 8
        reasons.append("in area-validation queue")
    if area in PRIORITY_AREAS:
        score += 6
        reasons.append("priority report area")
    if entry["award"]:
        score += 12
        reasons.append("award paper")
    if entry["is_oral"] == "true":
        score += 8
        reasons.append("oral/program signal")
    if entry["taxonomy_review_status"] == "needs_review":
        score += 7
        reasons.append("taxonomy boundary needs review")
    if entry["evidence_confidence"] in {"low", "very_low"}:
        score += 5
        reasons.append("low-confidence evidence code")
    if entry["needs_manual_check_reason"]:
        score += 8
        reasons.append("GitHub artifact needs manual check")
    if entry["github_url"]:
        score += min(6, inum(str(entry["github_stars"])) / 1000)
        reasons.append("artifact-visible")
    votes = inum(str(entry["public_total_votes"]))
    if votes >= 250:
        score += 7
        reasons.append("high AlphaXiv attention")
    elif votes >= 75:
        score += 4
        reasons.append("moderate AlphaXiv attention")
    if "program_signal_low_public_attention" in selection:
        score += 4
        reasons.append("program signal with low public attention")
    if "public_attention_not_program_signal" in selection:
        score += 4
        reasons.append("public attention without program signal")
    return round(score, 3), reasons


def build_entries() -> list[dict[str, object]]:
    claim_rows = read_csv(PROCESSED / "icml2026_claim_validation_queue.csv")
    area_rows = read_csv(PROCESSED / "icml2026_manual_validation_queue.csv")
    papers = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_paper_explorer.csv")}

    claim_by_event: dict[str, list[dict[str, str]]] = defaultdict(list)
    area_by_event: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in claim_rows:
        claim_by_event[row["event_id"]].append(row)
    for row in area_rows:
        area_by_event[row["event_id"]].append(row)

    event_ids = sorted(set(claim_by_event) | set(area_by_event))
    entries: list[dict[str, object]] = []
    for event_id in event_ids:
        paper = papers.get(event_id, {})
        claims = claim_by_event.get(event_id, [])
        areas = area_by_event.get(event_id, [])
        seed = claims[0] if claims else areas[0]
        area = paper.get("area") or seed.get("area", "")
        claim_ids = sorted({row["claim_id"] for row in claims})
        claim_themes = {row["claim_id"]: row.get("claim_theme", "") for row in claims}
        claim_links = [
            claim_packet_link(claim_id, claim_themes.get(claim_id, ""))
            for claim_id in claim_ids
        ]
        dossier_links = [
            claim_dossier_link(claim_id, claim_themes.get(claim_id, ""))
            for claim_id in claim_ids
        ]
        area_link = packet_link_for_area(area)
        entry: dict[str, object] = {
            "event_id": event_id,
            "title": paper.get("title") or seed.get("title", ""),
            "area": area,
            "subarea": paper.get("subarea") or seed.get("subarea", ""),
            "claim_ids": "; ".join(claim_ids),
            "claim_themes": "; ".join(claim_themes[claim_id] for claim_id in claim_ids),
            "in_claim_queue": "true" if claims else "false",
            "in_area_queue": "true" if areas else "false",
            "claim_selection_reasons": "; ".join(sorted({row.get("selection_reason", "") for row in claims if row.get("selection_reason")})),
            "area_selection_reasons": "; ".join(sorted({row.get("selection_reason", "") for row in areas if row.get("selection_reason")})),
            "review_focus": " | ".join(row.get("review_focus", "") for row in claims if row.get("review_focus")),
            "is_oral": paper.get("is_oral") or seed.get("is_oral", ""),
            "award": paper.get("award") or seed.get("award", ""),
            "public_total_votes": paper.get("public_total_votes") or seed.get("public_total_votes", ""),
            "github_url": paper.get("github_url") or seed.get("github_url", ""),
            "github_stars": paper.get("github_stars") or seed.get("github_stars", ""),
            "needs_manual_check_reason": paper.get("needs_manual_check_reason") or seed.get("needs_manual_check_reason", ""),
            "taxonomy_review_status": paper.get("review_status") or seed.get("review_status") or seed.get("cluster_review_status", ""),
            "evidence_confidence": paper.get("evidence_confidence") or seed.get("evidence_confidence") or seed.get("heuristic_evidence_confidence", ""),
            "primary_contribution_type": paper.get("primary_contribution_type") or seed.get("primary_contribution_type") or seed.get("heuristic_primary_contribution_type", ""),
            "method_families": paper.get("method_families") or seed.get("method_families") or seed.get("heuristic_method_families", ""),
            "evaluation_settings": paper.get("evaluation_settings") or seed.get("evaluation_settings") or seed.get("heuristic_evaluation_settings", ""),
            "claim_packet_links": "; ".join(claim_links),
            "claim_dossier_links": "; ".join(dossier_links),
            "area_packet_link": area_link if areas else "",
            "area_briefing_link": area_card_link(area),
            "icml_url": paper.get("url") or seed.get("url", ""),
            "alphaxiv_url": paper.get("alphaxiv_url") or seed.get("alphaxiv_url", ""),
        }
        score, reasons = score_entry(entry)
        entry["review_priority_score"] = score
        entry["priority_reason"] = "; ".join(reasons)
        entry["review_phase"] = phase_for(entry)
        entry["manual_fields_to_fill"] = "; ".join(
            [
                "claim: manual_claim_support/manual_taxonomy_judgment/manual_artifact_judgment" if claims else "",
                "area: manual_validated/manual_primary_contribution_type/manual_method_family/manual_artifact_status/manual_fault_line_relevance" if areas else "",
            ]
        ).strip("; ")
        entries.append(entry)

    entries.sort(
        key=lambda row: (
            -float(row["review_priority_score"]),
            0 if row["review_phase"] == "main_thesis_claims" else 1,
            str(row["area"]),
            str(row["title"]),
        )
    )
    for rank, row in enumerate(entries, start=1):
        row["global_review_rank"] = rank
    return entries


def write_report(rows: list[dict[str, object]]) -> None:
    phase_counts = Counter(str(row["review_phase"]) for row in rows)
    area_counts = Counter(str(row["area"]) for row in rows)
    claim_counts = Counter()
    for row in rows:
        for claim_id in str(row["claim_ids"]).split("; "):
            if claim_id:
                claim_counts[claim_id] += 1
    overlap = sum(row["in_claim_queue"] == "true" and row["in_area_queue"] == "true" for row in rows)

    lines = [
        "# ICML 2026 Researcher Review Plan",
        "",
        "This plan de-duplicates the claim and area validation queues into one ranked paper-reading workflow.",
        "It is a work plan for manual review, not evidence that the review has already been done.",
        "",
        "## Snapshot",
        "",
        f"- Unique papers to review: {len(rows)}",
        f"- Papers appearing in both claim and area queues: {overlap}",
        f"- Claim-queue papers represented: {sum(row['in_claim_queue'] == 'true' for row in rows)}",
        f"- Area-queue papers represented: {sum(row['in_area_queue'] == 'true' for row in rows)}",
        f"- Review phases: {', '.join(f'{name}: {count}' for name, count in phase_counts.most_common())}",
        "",
        "## First 40 Papers To Read",
        "",
        "| Rank | Phase | Paper | Area | Claims | Why First |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for row in rows[:40]:
        lines.append(
            f"| {row['global_review_rank']} | {row['review_phase']} | {row['title']} | {row['area']} | "
            f"{row['claim_ids'] or '-'} | {row['priority_reason']} |"
        )

    lines.extend(
        [
            "",
            "## Phase Guide",
            "",
            "- `main_thesis_claims`: read first; these papers move C01/C02/C03 and the core landscape thesis.",
            "- `artifact_and_reproducibility`: inspect GitHub/artifact claims before saying anything stronger than URL visibility.",
            "- `taxonomy_boundaries`: resolve area/subarea assignments before subarea-level claims.",
            "- `public_program_divergence`: compare community attention against oral/award selection.",
            "- `priority_area_depth`: fill high-impact area packets once thesis claims are checked.",
            "- `breadth_and_sanity_checks`: preserve coverage outside the headline areas.",
            "",
            "## Claim Coverage",
            "",
            "| Claim | Unique Papers |",
            "| --- | ---: |",
        ]
    )
    for claim_id, count in sorted(claim_counts.items()):
        lines.append(f"| {claim_id} | {count} |")

    lines.extend(
        [
            "",
            "## Area Coverage",
            "",
            "| Area | Unique Papers |",
            "| --- | ---: |",
        ]
    )
    for area, count in area_counts.most_common():
        lines.append(f"| {area} | {count} |")

    lines.extend(
        [
            "",
            "## How To Execute The Review",
            "",
            "1. Work down `data/processed/icml2026_researcher_review_plan.csv` by `global_review_rank`.",
            "2. For claim rows, open the listed claim packet and claim evidence dossier, then fill the claim manual fields.",
            "3. For area rows, open the area packet and area briefing card, then fill the area manual fields.",
            "4. Re-run `build_review_progress.py`, `build_researcher_readiness_audit.py`, and this review-plan script after manual fields are updated.",
            "5. Only promote a synthesis claim from directional to publication-ready after its supporting rows have manual judgments.",
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_researcher_review_plan.csv`",
            "- `reports/icml2026_researcher_review_plan.md`",
        ]
    )
    (REPORTS / "icml2026_researcher_review_plan.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    rows = build_entries()
    fieldnames = [
        "global_review_rank", "review_priority_score", "review_phase", "priority_reason",
        "event_id", "title", "area", "subarea", "claim_ids", "claim_themes",
        "in_claim_queue", "in_area_queue", "claim_selection_reasons",
        "area_selection_reasons", "review_focus", "is_oral", "award",
        "public_total_votes", "github_url", "github_stars", "needs_manual_check_reason",
        "taxonomy_review_status", "evidence_confidence", "primary_contribution_type",
        "method_families", "evaluation_settings", "manual_fields_to_fill",
        "claim_packet_links", "claim_dossier_links", "area_packet_link",
        "area_briefing_link", "icml_url", "alphaxiv_url",
    ]
    write_csv(PROCESSED / "icml2026_researcher_review_plan.csv", rows, fieldnames)
    write_report(rows)
    print(f"Wrote {PROCESSED / 'icml2026_researcher_review_plan.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_researcher_review_plan.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
