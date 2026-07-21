#!/usr/bin/env python3
"""Build an area-level reliability and risk register for ICML 2026 landscape use."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
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


def to_float(value: object, default: float = 0.0) -> float:
    try:
        if value is None or str(value).strip() == "":
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def to_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except (TypeError, ValueError):
        return 0


def pct(value: object) -> str:
    return f"{to_float(value) * 100:.1f}%"


def pp(value: object) -> str:
    val = to_float(value)
    return f"{val * 100:+.1f} pp"


def split_pipe(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split("|") if part.strip()]


def area_risk_tier(
    briefing: dict[str, str],
    baseline: dict[str, str],
    taxonomy_clusters: int,
    low_confidence_rows: int,
    reviewed_rows: int,
    review_rows: int,
) -> str:
    if reviewed_rows == 0 and (
        briefing.get("trust_tier") == "high_review_need"
        or baseline.get("risk_tier") == "high"
        or taxonomy_clusters >= 3
    ):
        return "critical"
    if baseline.get("risk_tier") in {"high", "moderate"} or taxonomy_clusters > 0 or low_confidence_rows > 0:
        return "high"
    if review_rows and reviewed_rows < review_rows:
        return "moderate"
    return "watch"


def main_risk_driver(
    baseline: dict[str, str],
    taxonomy_clusters: int,
    low_confidence_rows: int,
    oral_enrichment: float,
    public_enrichment: float,
) -> str:
    drivers = []
    if taxonomy_clusters:
        drivers.append(f"{taxonomy_clusters} taxonomy clusters need adjudication")
    if baseline.get("risk_tier") in {"high", "moderate"}:
        drivers.append(f"{baseline.get('risk_tier')} baseline sensitivity")
    if oral_enrichment >= 1.2 and public_enrichment < 0.8:
        drivers.append("program signal exceeds public attention")
    if public_enrichment >= 1.2 and oral_enrichment < 1.0:
        drivers.append("public attention exceeds program signal")
    if low_confidence_rows:
        drivers.append(f"{low_confidence_rows} low-confidence evidence-code rows")
    return "; ".join(drivers) if drivers else "manual review still incomplete"


def falsification_test(area: str, baseline: dict[str, str], taxonomy_clusters: int, oral_enrichment: float, public_enrichment: float) -> str:
    if baseline.get("risk_tier") == "high":
        return baseline.get("check_question", "")
    if taxonomy_clusters >= 3:
        return f"Adjudicate boundary clusters before making subarea-share or area-rank claims about {area}."
    if oral_enrichment >= 1.2 and public_enrichment < 0.8:
        return "Read program-forward, low-public papers and verify the technical rationale for committee attention."
    if public_enrichment >= 1.2 and oral_enrichment < 1.0:
        return "Read high-public, non-program papers and decide whether attention reflects novelty, demo visibility, or hype."
    return "Review representative area-validation papers before turning orientation signals into prose claims."


def safe_language(row: dict[str, object]) -> str:
    tier = str(row["risk_tier"])
    if tier == "critical":
        return "Use for orientation only; avoid area-ranking or subarea conclusions until manual review and risk checks are done."
    if tier == "high":
        return "Use as a directional area signal with explicit taxonomy/baseline caveats."
    if tier == "moderate":
        return "Use for area-level orientation; avoid fine-grained claims without reviewed examples."
    return "Use for orientation, still cite caveats and representative checked papers."


def main() -> int:
    briefings = {row["area"]: row for row in read_csv(PROCESSED / "icml2026_area_briefing_cards.csv")}
    readiness = {
        row["id"]: row
        for row in read_csv(PROCESSED / "icml2026_researcher_readiness_audit.csv")
        if row.get("audit_type") == "area"
    }
    baseline = {row["area"]: row for row in read_csv(PROCESSED / "icml2026_baseline_sensitivity_queue.csv")}
    taxonomy_queue = read_csv(PROCESSED / "icml2026_taxonomy_adjudication_queue.csv")
    reviewed = read_csv(PROCESSED / "icml2026_area_validation_reviewed.csv")

    taxonomy_by_area: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in taxonomy_queue:
        taxonomy_by_area[row.get("current_area", "")].append(row)

    reviewed_by_area: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in reviewed:
        reviewed_by_area[row.get("area", "")].append(row)

    rows: list[dict[str, object]] = []
    for area, briefing in briefings.items():
        ready = readiness.get(area, {})
        base = baseline.get(area, {})
        area_review_rows = reviewed_by_area.get(area, [])
        reviewed_rows = sum(row.get("reviewed") == "true" for row in area_review_rows)
        review_rows = len(area_review_rows)
        low_confidence_rows = to_int(ready.get("low_confidence_rows", ""))
        taxonomy_clusters = len(taxonomy_by_area.get(area, []))
        oral_enrichment = to_float(briefing.get("oral_enrichment"))
        public_enrichment = to_float(briefing.get("public_attention_enrichment"))
        tier = area_risk_tier(briefing, base, taxonomy_clusters, low_confidence_rows, reviewed_rows, review_rows)
        row: dict[str, object] = {
            "area": area,
            "risk_tier": tier,
            "trust_tier": briefing.get("trust_tier", ""),
            "readiness_tier": ready.get("readiness_tier", ""),
            "paper_count": briefing.get("paper_count", ""),
            "taxonomy_share": briefing.get("taxonomy_share", ""),
            "oral_enrichment": briefing.get("oral_enrichment", ""),
            "public_attention_enrichment": briefing.get("public_attention_enrichment", ""),
            "historical_delta_vs_baseline": briefing.get("historical_delta_vs_baseline", ""),
            "baseline_risk_tier": base.get("risk_tier", "context"),
            "baseline_issue_types": base.get("issue_types", ""),
            "reviewed_rows": reviewed_rows,
            "review_rows": review_rows,
            "taxonomy_clusters_to_adjudicate": taxonomy_clusters,
            "low_confidence_rows": low_confidence_rows,
            "program_or_award_rows": ready.get("program_or_award_rows", ""),
            "github_rows": ready.get("github_rows", ""),
            "main_risk_driver": main_risk_driver(base, taxonomy_clusters, low_confidence_rows, oral_enrichment, public_enrichment),
            "falsification_test": falsification_test(area, base, taxonomy_clusters, oral_enrichment, public_enrichment),
            "safe_language": "",
            "recommended_first_checks": first_checks(area, briefing, base, taxonomy_by_area.get(area, []), area_review_rows),
            "brief_path": briefing.get("brief_path", ""),
            "baseline_safe_language": base.get("safe_language", ""),
        }
        row["safe_language"] = safe_language(row)
        rows.append(row)

    rows.sort(
        key=lambda row: (
            {"critical": 0, "high": 1, "moderate": 2, "watch": 3}.get(str(row["risk_tier"]), 9),
            -to_float(row["taxonomy_share"]),
            row["area"],
        )
    )

    fieldnames = [
        "area",
        "risk_tier",
        "trust_tier",
        "readiness_tier",
        "paper_count",
        "taxonomy_share",
        "oral_enrichment",
        "public_attention_enrichment",
        "historical_delta_vs_baseline",
        "baseline_risk_tier",
        "baseline_issue_types",
        "reviewed_rows",
        "review_rows",
        "taxonomy_clusters_to_adjudicate",
        "low_confidence_rows",
        "program_or_award_rows",
        "github_rows",
        "main_risk_driver",
        "falsification_test",
        "safe_language",
        "recommended_first_checks",
        "brief_path",
        "baseline_safe_language",
    ]
    write_csv(PROCESSED / "icml2026_area_risk_register.csv", rows, fieldnames)
    write_report(rows)
    print(f"Wrote {PROCESSED / 'icml2026_area_risk_register.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_area_risk_register.md'}")
    return 0


def first_checks(
    area: str,
    briefing: dict[str, str],
    baseline: dict[str, str],
    taxonomy_rows: list[dict[str, str]],
    area_review_rows: list[dict[str, str]],
) -> str:
    checks = []
    if taxonomy_rows:
        clusters = ", ".join(row.get("semantic_cluster_id", "") for row in taxonomy_rows[:3])
        checks.append(f"adjudicate taxonomy cluster(s) {clusters}")
    if baseline.get("risk_tier") in {"high", "moderate"}:
        checks.append(baseline.get("recommended_action", "run baseline sensitivity checks"))
    program_examples = split_pipe(briefing.get("program_papers", ""))[:2]
    public_examples = split_pipe(briefing.get("public_non_program_papers", ""))[:2]
    boundary_examples = [
        row.get("title", "")
        for row in area_review_rows
        if row.get("cluster_review_status") == "needs_review"
    ][:2]
    if program_examples:
        checks.append("read program examples: " + " | ".join(program_examples))
    if public_examples:
        checks.append("read public-attention examples: " + " | ".join(public_examples))
    if boundary_examples:
        checks.append("read boundary examples: " + " | ".join(boundary_examples))
    return "; ".join(checks) if checks else f"review representative validation rows for {area}"


def write_report(rows: list[dict[str, object]]) -> None:
    tier_counts = Counter(str(row["risk_tier"]) for row in rows)
    lines = [
        "# ICML 2026 Area Risk Register",
        "",
        "Area-level reliability register for deciding which landscape summaries are safe to use and which need more review.",
        "",
        "## Snapshot",
        "",
        f"- Areas tracked: {len(rows)}",
        f"- Risk tiers: {', '.join(f'{key}: {value}' for key, value in tier_counts.most_common())}",
        f"- Areas with no reviewed validation rows: {sum(to_int(row['reviewed_rows']) == 0 for row in rows)}",
        "",
        "## Register",
        "",
        "| Risk | Area | Review | Baseline risk | Taxonomy clusters | Main risk driver | Falsification test |",
        "| --- | --- | ---: | --- | ---: | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['risk_tier']} | {row['area']} | {row['reviewed_rows']}/{row['review_rows']} | "
            f"{row['baseline_risk_tier']} | {row['taxonomy_clusters_to_adjudicate']} | "
            f"{row['main_risk_driver']} | {row['falsification_test']} |"
        )

    lines.extend(["", "## Area Details", ""])
    for row in rows:
        lines.extend(
            [
                f"### {row['area']}",
                "",
                f"- Safe language: {row['safe_language']}",
                f"- Trust tier: `{row['trust_tier']}`; readiness tier: `{row['readiness_tier']}`",
                f"- Size/signals: {row['paper_count']} papers ({pct(row['taxonomy_share'])}); oral {float(row['oral_enrichment']):.2f}x; public {float(row['public_attention_enrichment']):.2f}x; historical delta {pp(row['historical_delta_vs_baseline'])}",
                f"- Baseline issue types: {row['baseline_issue_types'] or 'none'}",
                f"- Low-confidence evidence rows: {row['low_confidence_rows']}",
                f"- Program/award rows in review queue: {row['program_or_award_rows']}; GitHub rows: {row['github_rows']}",
                f"- Recommended first checks: {row['recommended_first_checks']}",
                f"- Briefing card: `{row['brief_path']}`",
                "",
            ]
        )
    lines.extend(
        [
            "## Outputs",
            "",
            "- `data/processed/icml2026_area_risk_register.csv`",
            "- `reports/icml2026_area_risk_register.md`",
        ]
    )
    (REPORTS / "icml2026_area_risk_register.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
