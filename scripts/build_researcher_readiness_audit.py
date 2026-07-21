#!/usr/bin/env python3
"""Build a researcher-facing readiness audit for ICML 2026 synthesis claims."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
MANUAL = ROOT / "data" / "manual"
REPORTS = ROOT / "reports"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"Missing required input: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def apply_manual_overrides(rows: list[dict[str, str]], path: Path, key_fields: list[str], manual_fields: list[str]) -> list[dict[str, str]]:
    if not path.exists():
        return rows
    overrides = read_csv(path)
    by_key = {
        tuple(row.get(field, "") for field in key_fields): row
        for row in overrides
    }
    merged = []
    for row in rows:
        out = dict(row)
        override = by_key.get(tuple(row.get(field, "") for field in key_fields))
        if override:
            for field in manual_fields:
                value = (override.get(field, "") or "").strip()
                if value:
                    out[field] = value
        merged.append(out)
    return merged


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def fnum(value: str) -> float:
    try:
        return float(value or 0)
    except ValueError:
        return 0.0


def inum(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def pct(done: int, total: int) -> str:
    return f"{done / total * 100:.1f}%" if total else "0.0%"


def claim_review_complete(row: dict[str, str]) -> bool:
    return any(
        (row.get(field, "") or "").strip()
        for field in ["manual_claim_support", "manual_taxonomy_judgment", "manual_artifact_judgment", "manual_notes"]
    )


def area_review_complete(row: dict[str, str]) -> bool:
    return any(
        (row.get(field, "") or "").strip()
        for field in [
            "manual_validated",
            "manual_primary_contribution_type",
            "manual_method_family",
            "manual_benchmarks",
            "manual_datasets",
            "manual_metrics",
            "manual_artifact_status",
            "manual_result_character",
            "manual_fault_line_relevance",
            "manual_notes",
        ]
    )


def claim_tier(strength: str, reviewed: int, total: int, taxonomy_review_rows: int, low_confidence_rows: int) -> tuple[str, str]:
    if total and reviewed == total and low_confidence_rows == 0 and taxonomy_review_rows == 0:
        return "publication_ready_seed", "Use as a paper-level claim after final prose review."
    if reviewed:
        return "partially_checked", "Use with explicit caveats and cite the reviewed packet rows."
    if strength in {"strong_for_landscape", "strong_for_triage", "moderate_to_strong"}:
        return "high_priority_unreviewed", "Use only as a directional landscape claim until the packet is reviewed."
    if strength == "context_only":
        return "context_only_unreviewed", "Use as background context, not as a main thesis."
    if strength == "process_claim":
        return "workflow_claim_unreviewed", "Use to describe the validation workflow, not the paper landscape."
    return "directional_unreviewed", "Use as a hypothesis or reading guide."


def area_risk(row: dict[str, str], review_rows: list[dict[str, str]]) -> tuple[str, str]:
    tags = {part.strip() for part in row.get("signal_tags", "").split(";") if part.strip()}
    taxonomy_rows = sum(item.get("cluster_review_status") == "needs_review" for item in review_rows)
    low_confidence_rows = sum(item.get("heuristic_evidence_confidence") in {"low", "very_low"} for item in review_rows)
    public_program_gap = abs(fnum(row.get("public_attention_enrichment", "")) - fnum(row.get("oral_enrichment", "")))
    reasons = []
    if taxonomy_rows:
        reasons.append(f"{taxonomy_rows} queued taxonomy-boundary rows")
    if low_confidence_rows:
        reasons.append(f"{low_confidence_rows} low-confidence evidence rows")
    if "venue_underweight" in tags or "venue_overweight" in tags:
        reasons.append("historical baseline interpretation needed")
    if public_program_gap >= 0.9:
        reasons.append("large public/program signal gap")
    if not reasons:
        return "moderate", "No single dominant risk, but paper-level validation is still open."
    if taxonomy_rows >= 5 or low_confidence_rows >= 3 or public_program_gap >= 1.2:
        return "high", "; ".join(reasons)
    return "moderate_to_high", "; ".join(reasons)


def build_claim_rows(claims: list[dict[str, str]], queue: list[dict[str, str]]) -> list[dict[str, object]]:
    by_claim: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in queue:
        by_claim[row["claim_id"]].append(row)

    rows: list[dict[str, object]] = []
    for claim in claims:
        items = by_claim[claim["claim_id"]]
        reviewed = sum(claim_review_complete(row) for row in items)
        taxonomy_review = sum(row.get("review_status") == "needs_review" for row in items)
        low_confidence = sum(row.get("evidence_confidence") in {"low", "very_low"} for row in items)
        program = sum(row.get("is_oral") == "true" or bool(row.get("award")) for row in items)
        github = sum(bool(row.get("github_url")) for row in items)
        reasons = Counter(row["selection_reason"] for row in items)
        tier, use_guidance = claim_tier(
            claim["strength"],
            reviewed,
            len(items),
            taxonomy_review,
            low_confidence,
        )
        rows.append(
            {
                "audit_type": "claim",
                "id": claim["claim_id"],
                "name": claim["theme"],
                "readiness_tier": tier,
                "researcher_use": use_guidance,
                "review_rows": len(items),
                "reviewed_rows": reviewed,
                "remaining_rows": len(items) - reviewed,
                "taxonomy_review_rows": taxonomy_review,
                "low_confidence_rows": low_confidence,
                "program_or_award_rows": program,
                "github_rows": github,
                "primary_risk": claim["caveats"],
                "evidence_summary": claim["evidence"],
                "next_action": claim["next_validation"],
                "selection_mix": "; ".join(f"{reason}: {count}" for reason, count in reasons.most_common()),
            }
        )
    return rows


def build_area_rows(signal_matrix: list[dict[str, str]], area_queue: list[dict[str, str]]) -> list[dict[str, object]]:
    by_area: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in area_queue:
        by_area[row["area"]].append(row)

    rows: list[dict[str, object]] = []
    for row in signal_matrix:
        items = by_area[row["area"]]
        reviewed = sum(area_review_complete(item) for item in items)
        risk, risk_reason = area_risk(row, items)
        rows.append(
            {
                "audit_type": "area",
                "id": row["area"],
                "name": row["area"],
                "readiness_tier": risk,
                "researcher_use": "Use for area-level orientation; avoid subarea-level claims until queued papers are reviewed.",
                "review_rows": len(items),
                "reviewed_rows": reviewed,
                "remaining_rows": len(items) - reviewed,
                "taxonomy_review_rows": sum(item.get("cluster_review_status") == "needs_review" for item in items),
                "low_confidence_rows": sum(item.get("heuristic_evidence_confidence") in {"low", "very_low"} for item in items),
                "program_or_award_rows": sum(item.get("is_oral") == "true" or bool(item.get("award")) for item in items),
                "github_rows": sum(bool(item.get("github_url")) for item in items),
                "primary_risk": risk_reason,
                "evidence_summary": (
                    f"{inum(row['taxonomy_papers'])} papers; "
                    f"taxonomy share {fnum(row['taxonomy_share']) * 100:.1f}%; "
                    f"oral enrichment {fnum(row['oral_enrichment']):.2f}x; "
                    f"public enrichment {fnum(row['public_attention_enrichment']):.2f}x; "
                    f"historical delta {fnum(row['historical_delta_vs_baseline']) * 100:+.1f} pp"
                ),
                "next_action": "Review the area validation packet, starting with boundary, low-confidence, and public/program divergence rows.",
                "selection_mix": "; ".join(
                    f"{reason}: {count}" for reason, count in Counter(item["selection_reason"] for item in items).most_common()
                ),
            }
        )
    rows.sort(key=lambda item: (str(item["audit_type"]), str(item["readiness_tier"]), str(item["id"])))
    return rows


def write_report(rows: list[dict[str, object]]) -> None:
    claim_rows = [row for row in rows if row["audit_type"] == "claim"]
    area_rows = [row for row in rows if row["audit_type"] == "area"]
    total_review_rows = sum(int(row["review_rows"]) for row in rows)
    total_reviewed = sum(int(row["reviewed_rows"]) for row in rows)
    claim_tiers = Counter(str(row["readiness_tier"]) for row in claim_rows)
    area_tiers = Counter(str(row["readiness_tier"]) for row in area_rows)

    high_priority = [
        row for row in claim_rows
        if row["readiness_tier"] in {"high_priority_unreviewed", "partially_checked"}
    ]
    high_risk_areas = [row for row in area_rows if row["readiness_tier"] == "high"]

    lines = [
        "# ICML 2026 Researcher Readiness Audit",
        "",
        "This audit translates the EDA workspace into a practical research judgment map.",
        "It separates directional landscape signals from claims that are ready for publication-grade use.",
        "",
        "## Snapshot",
        "",
        f"- Audited claims: {len(claim_rows)}",
        f"- Audited areas: {len(area_rows)}",
        f"- Manual review completed: {total_reviewed}/{total_review_rows} ({pct(total_reviewed, total_review_rows)})",
        f"- Claim readiness tiers: {', '.join(f'{tier}: {count}' for tier, count in sorted(claim_tiers.items()))}",
        f"- Area risk tiers: {', '.join(f'{tier}: {count}' for tier, count in sorted(area_tiers.items()))}",
        "",
        "## What A Researcher Can Safely Use Now",
        "",
        "- Official corpus counts, oral flags, award flags, and generated joins are safe as descriptive metadata.",
        "- Area-level patterns are useful for triage when phrased as directional signals rather than final causal claims.",
        "- Public-attention results should be described as AlphaXiv attention, not paper quality.",
        "- Historical deltas should be treated as accepted-paper baseline contrasts, not definitive venue-policy conclusions.",
        "",
        "## What Is Not Defensible Yet",
        "",
        "- Paper-level support for the eight synthesis claims is not complete because the claim packet manual fields are still blank.",
        "- Subarea-level conclusions are not publication-ready while boundary clusters remain in the review queues.",
        "- Reproducibility claims should not go beyond GitHub URL visibility unless the relevant repositories have been manually checked.",
        "- Benchmark, dataset, metric, and negative-result claims are still heuristic evidence-code outputs.",
        "",
        "## Claim Readiness",
        "",
        "| Claim | Tier | Rows | Reviewed | Taxonomy Review | Low Confidence | Researcher Use |",
        "| --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in claim_rows:
        lines.append(
            f"| {row['id']} - {row['name']} | {row['readiness_tier']} | {row['review_rows']} | "
            f"{row['reviewed_rows']} | {row['taxonomy_review_rows']} | {row['low_confidence_rows']} | "
            f"{row['researcher_use']} |"
        )

    lines.extend(
        [
            "",
            "## Highest-Priority Claim Packets",
            "",
        ]
    )
    for row in high_priority[:6]:
        lines.append(f"- `{row['id']}`: {row['next_action']} Risk: {row['primary_risk']}")

    lines.extend(
        [
            "",
            "## Area Risk Map",
            "",
            "| Area | Risk | Rows | Reviewed | Taxonomy Review | Low Confidence | Evidence Summary |",
            "| --- | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in sorted(area_rows, key=lambda item: (-int(item["taxonomy_review_rows"]), -int(item["low_confidence_rows"]), str(item["id"]))):
        lines.append(
            f"| {row['name']} | {row['readiness_tier']} | {row['review_rows']} | {row['reviewed_rows']} | "
            f"{row['taxonomy_review_rows']} | {row['low_confidence_rows']} | {row['evidence_summary']} |"
        )

    lines.extend(
        [
            "",
            "## Most Fragile Areas To Read First",
            "",
        ]
    )
    for row in high_risk_areas:
        lines.append(f"- {row['name']}: {row['primary_risk']}")

    lines.extend(
        [
            "",
            "## Evidence Stream Risk",
            "",
            "| Evidence stream | Usefulness | Failure mode | Best next check |",
            "| --- | --- | --- | --- |",
            "| Official ICML metadata | High | Mostly structural; title/topic metadata may be sparse | Spot-check paper links and award/oral labels. |",
            "| Manual taxonomy seed | High for report structure | Boundary clusters and mixed semantic clusters | Review queued taxonomy-boundary papers. |",
            "| AlphaXiv votes/visits | Medium | Social attention and recency, not quality | Compare high-public/non-oral against abstracts and paper claims. |",
            "| Historical accepted-paper deltas | Medium | Keyword classifier and uneven abstract coverage | Read largest delta papers and recalibrate labels. |",
            "| arXiv trend queries | Low to medium | Broad overlapping search terms | Use only as external context, not venue evidence. |",
            "| GitHub artifact metadata | Medium for visibility | URL existence does not imply runnable reproduction | Manually inspect high-signal repos. |",
            "| Heuristic evidence codes | Medium for triage | Keyword false positives for methods, metrics, datasets | Fill validation packets and reconcile CSV fields. |",
            "",
            "## Recommended Research Workplan",
            "",
            "1. Review claim packets C01, C02, C03, and C07 before writing the main landscape thesis.",
            "2. Resolve taxonomy-boundary rows in LLM Reasoning, Systems, Multimodal/Vision, Safety/Governance, and Theory.",
            "3. Manually inspect high-public/non-program papers to decide whether they are community trends, demos, or genuine technical centers.",
            "4. Manually inspect low-public/high-program papers to extract the committee-valued technical ideas.",
            "5. Re-run this audit after filling manual fields; readiness tiers should move from unreviewed to partially checked or publication-ready seed.",
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_researcher_readiness_audit.csv`",
            "- `reports/icml2026_researcher_readiness_audit.md`",
        ]
    )
    (REPORTS / "icml2026_researcher_readiness_audit.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    claims = read_csv(PROCESSED / "icml2026_landscape_claim_register.csv")
    signal_matrix = read_csv(PROCESSED / "icml2026_landscape_signal_matrix.csv")
    reviewed_claims = PROCESSED / "icml2026_claim_validation_reviewed.csv"
    reviewed_areas = PROCESSED / "icml2026_area_validation_reviewed.csv"
    if reviewed_claims.exists() and reviewed_areas.exists():
        claim_queue = read_csv(reviewed_claims)
        area_queue = read_csv(reviewed_areas)
    else:
        claim_queue = read_csv(PROCESSED / "icml2026_claim_validation_queue.csv")
        area_queue = read_csv(PROCESSED / "icml2026_manual_validation_queue.csv")
        claim_queue = apply_manual_overrides(
            claim_queue,
            MANUAL / "claim_review_overrides.csv",
            ["claim_id", "event_id"],
            ["manual_claim_support", "manual_taxonomy_judgment", "manual_artifact_judgment", "manual_notes"],
        )
        area_queue = apply_manual_overrides(
            area_queue,
            MANUAL / "area_review_overrides.csv",
            ["area", "event_id"],
            [
                "manual_validated", "manual_primary_contribution_type", "manual_method_family",
                "manual_benchmarks", "manual_datasets", "manual_metrics", "manual_artifact_status",
                "manual_result_character", "manual_fault_line_relevance", "manual_notes",
            ],
        )

    rows = build_claim_rows(claims, claim_queue)
    rows.extend(build_area_rows(signal_matrix, area_queue))
    rows.sort(key=lambda row: (str(row["audit_type"]), str(row["id"])))

    fieldnames = [
        "audit_type",
        "id",
        "name",
        "readiness_tier",
        "researcher_use",
        "review_rows",
        "reviewed_rows",
        "remaining_rows",
        "taxonomy_review_rows",
        "low_confidence_rows",
        "program_or_award_rows",
        "github_rows",
        "primary_risk",
        "evidence_summary",
        "next_action",
        "selection_mix",
    ]
    write_csv(PROCESSED / "icml2026_researcher_readiness_audit.csv", rows, fieldnames)
    write_report(rows)
    print(f"Wrote {PROCESSED / 'icml2026_researcher_readiness_audit.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_researcher_readiness_audit.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
