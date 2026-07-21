#!/usr/bin/env python3
"""Build a spot-check queue for historical and arXiv baseline claims."""

from __future__ import annotations

import csv
from collections import defaultdict
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


def pct(value: float) -> str:
    return f"{value * 100:.1f}%"


def pp(value: float) -> str:
    sign = "+" if value > 0 else ""
    return f"{sign}{value * 100:.1f} pp"


def first_titles(value: str, limit: int = 4) -> str:
    titles = [part.strip() for part in (value or "").split("|") if part.strip()]
    return " | ".join(titles[:limit])


def historical_examples(rows: list[dict[str, str]], area: str, limit: int = 4) -> str:
    preferred = [row for row in rows if row.get("area") == area and row.get("venue") != "ICML 2026"]
    preferred.sort(
        key=lambda row: (
            row.get("confidence") != "high",
            row.get("venue", ""),
            -to_float(row.get("area_score")),
            row.get("title", ""),
        )
    )
    return " | ".join(row.get("title", "") for row in preferred[:limit] if row.get("title"))


def risk_label(delta: float, rel: float, growth: float, signal_tags: str) -> tuple[str, str]:
    tags = {tag.strip() for tag in (signal_tags or "").split(";") if tag.strip()}
    issues: list[str] = []
    if abs(delta) >= 0.025 or rel >= 1.5 or rel <= 0.75:
        issues.append("historical_delta_sensitive")
    if growth >= 0.5:
        issues.append("arxiv_query_sensitive")
    if ("venue_underweight" in tags and growth >= 0.35) or ("venue_overweight" in tags and growth <= 0.15):
        issues.append("baseline_disagreement")
    if not issues:
        issues.append("classifier_spot_check")

    if "baseline_disagreement" in issues or len(issues) >= 2:
        tier = "high"
    elif "historical_delta_sensitive" in issues or "arxiv_query_sensitive" in issues:
        tier = "moderate"
    else:
        tier = "context"
    return tier, "; ".join(issues)


def check_question(area: str, issue_types: str, delta: float, growth: float) -> str:
    if "baseline_disagreement" in issue_types:
        return (
            "Check whether the venue-share direction and arXiv-growth direction are describing different phenomena, "
            "or whether one is an artifact of broad query terms/classifier boundaries."
        )
    if "historical_delta_sensitive" in issue_types and delta > 0:
        return f"Verify that {area} is genuinely over-represented versus nearby accepted venues, not a classifier keyword effect."
    if "historical_delta_sensitive" in issue_types and delta < 0:
        return f"Verify that {area} is genuinely under-represented versus nearby accepted venues, not a missed-title/abstract effect."
    if "arxiv_query_sensitive" in issue_types and growth > 0:
        return "Test alternate arXiv query terms and inspect whether generic terms are inflating the growth estimate."
    return "Spot-check representative titles and boundary papers before using this as more than directional context."


def recommended_action(issue_types: str) -> str:
    actions = []
    if "historical_delta_sensitive" in issue_types:
        actions.append("sample historical high-confidence and low-margin classifications")
    if "arxiv_query_sensitive" in issue_types:
        actions.append("rerun narrower and broader arXiv query variants")
    if "baseline_disagreement" in issue_types:
        actions.append("write a caveat separating ICML program mix from field-wide preprint momentum")
    if not actions:
        actions.append("review classifier hits for representative titles")
    return "; ".join(actions)


def safe_language(tier: str, issue_types: str) -> str:
    if tier == "high":
        return "Use only as a hypothesis until spot checks confirm direction and query robustness."
    if "arxiv_query_sensitive" in issue_types:
        return "Phrase as broad preprint-query momentum, not field growth."
    if "historical_delta_sensitive" in issue_types:
        return "Phrase as a neighboring-venue comparison, not a causal venue-policy claim."
    return "Use as directional background with classifier caveats."


def main() -> int:
    taxonomy = {row["area"]: row for row in read_csv(PROCESSED / "icml2026_manual_taxonomy_areas.csv")}
    historical = {row["area"]: row for row in read_csv(PROCESSED / "historical_venue_delta_summary.csv")}
    arxiv = {row["area"]: row for row in read_csv(PROCESSED / "arxiv_taxonomy_trend_summary.csv")}
    signal = {row["area"]: row for row in read_csv(PROCESSED / "icml2026_landscape_signal_matrix.csv")}
    historical_classified = read_csv(PROCESSED / "historical_accepted_papers_classified.csv")

    venue_counts: dict[str, int] = defaultdict(int)
    for row in historical_classified:
        if row.get("venue") != "ICML 2026" and row.get("area") != "Uncoded / Other":
            venue_counts[row.get("area", "")] += 1

    rows: list[dict[str, object]] = []
    for area in taxonomy:
        hist = historical.get(area, {})
        arx = arxiv.get(area, {})
        sig = signal.get(area, {})
        delta = to_float(hist.get("delta_vs_baseline_avg"))
        rel = to_float(hist.get("relative_to_baseline_avg"), 1.0)
        growth = to_float(arx.get("growth_2025_vs_2024"))
        tier, issues = risk_label(delta, rel, growth, sig.get("signal_tags", ""))
        rows.append(
            {
                "area": area,
                "risk_tier": tier,
                "issue_types": issues,
                "icml2026_papers": taxonomy[area].get("paper_count", ""),
                "icml2026_share": taxonomy[area].get("share", ""),
                "baseline_avg_share": hist.get("baseline_avg_share", ""),
                "historical_delta_pp": round(delta * 100, 2),
                "historical_relative_to_baseline": hist.get("relative_to_baseline_avg", ""),
                "arxiv_2025_vs_2024_growth": arx.get("growth_2025_vs_2024", ""),
                "arxiv_query_terms": arx.get("query_terms", ""),
                "historical_comparison_papers": venue_counts.get(area, 0),
                "signal_tags": sig.get("signal_tags", ""),
                "check_question": check_question(area, issues, delta, growth),
                "recommended_action": recommended_action(issues),
                "safe_language": safe_language(tier, issues),
                "icml2026_examples": first_titles(taxonomy[area].get("representative_papers", "")),
                "historical_examples": historical_examples(historical_classified, area),
            }
        )

    rows.sort(
        key=lambda row: (
            {"high": 0, "moderate": 1, "context": 2}.get(str(row["risk_tier"]), 9),
            -abs(to_float(row["historical_delta_pp"])),
            row["area"],
        )
    )

    fieldnames = [
        "area",
        "risk_tier",
        "issue_types",
        "icml2026_papers",
        "icml2026_share",
        "baseline_avg_share",
        "historical_delta_pp",
        "historical_relative_to_baseline",
        "arxiv_2025_vs_2024_growth",
        "arxiv_query_terms",
        "historical_comparison_papers",
        "signal_tags",
        "check_question",
        "recommended_action",
        "safe_language",
        "icml2026_examples",
        "historical_examples",
    ]
    write_csv(PROCESSED / "icml2026_baseline_sensitivity_queue.csv", rows, fieldnames)

    tier_counts = defaultdict(int)
    for row in rows:
        tier_counts[str(row["risk_tier"])] += 1

    lines = [
        "# ICML 2026 Baseline Sensitivity Queue",
        "",
        "Spot-check queue for using historical accepted-paper baselines and broad arXiv query trends responsibly.",
        "",
        "## Summary",
        "",
        f"- Areas queued: {len(rows)}",
        f"- High-risk areas: {tier_counts['high']}",
        f"- Moderate-risk areas: {tier_counts['moderate']}",
        f"- Context-only areas: {tier_counts['context']}",
        "",
        "## How To Use",
        "",
        "- Treat this as a QA layer, not a final source of truth.",
        "- Prioritize high-risk rows before writing claims about field momentum or venue emphasis.",
        "- Keep historical-baseline claims separate from arXiv-preprint claims unless both survive spot checks.",
        "",
        "## Queue",
        "",
        "| Risk | Area | Historical delta | arXiv growth | Issue types | Check question |",
        "| --- | --- | ---: | ---: | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['risk_tier']} | {row['area']} | {pp(to_float(row['historical_delta_pp']) / 100)} | "
            f"{pct(to_float(row['arxiv_2025_vs_2024_growth']))} | {row['issue_types']} | {row['check_question']} |"
        )

    lines.extend(["", "## High-Risk Detail", ""])
    for row in rows:
        if row["risk_tier"] != "high":
            continue
        lines.extend(
            [
                f"### {row['area']}",
                "",
                f"- ICML 2026 share: {pct(to_float(row['icml2026_share']))}; historical baseline share: {pct(to_float(row['baseline_avg_share']))}.",
                f"- Recommended action: {row['recommended_action']}.",
                f"- Safe language: {row['safe_language']}",
                f"- ICML 2026 examples: {row['icml2026_examples']}",
                f"- Historical examples: {row['historical_examples']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Outputs",
            "",
            "- `data/processed/icml2026_baseline_sensitivity_queue.csv`",
            "- `reports/icml2026_baseline_sensitivity_queue.md`",
        ]
    )
    (REPORTS / "icml2026_baseline_sensitivity_queue.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {PROCESSED / 'icml2026_baseline_sensitivity_queue.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_baseline_sensitivity_queue.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
