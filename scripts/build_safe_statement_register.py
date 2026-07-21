#!/usr/bin/env python3
"""Build wording guardrails for claims and area summaries."""

from __future__ import annotations

import csv
from collections import Counter
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


def pct(value: object) -> str:
    return f"{to_float(value) * 100:.1f}%"


def pp(value: object) -> str:
    value = to_float(value)
    return f"{value * 100:+.1f} pp"


def claim_wording_status(decision: str, risk_tier: str) -> str:
    if decision == "promote_candidate":
        return "candidate_for_headline"
    if decision == "context_or_workflow_only":
        return "context_only"
    if risk_tier == "critical":
        return "hypothesis_only"
    return "directional_only"


def area_wording_status(risk_tier: str, reviewed_rows: int) -> str:
    if reviewed_rows > 0 and risk_tier in {"watch", "moderate"}:
        return "orientation_with_examples"
    if risk_tier == "critical":
        return "orientation_only"
    return "directional_only"


def claim_allowed(row: dict[str, str]) -> str:
    status = claim_wording_status(row.get("decision", ""), row.get("risk_tier", ""))
    statement = row.get("statement_under_test", "")
    if status == "context_only":
        return f"As context only: {statement}"
    if status == "hypothesis_only":
        return f"Hypothesis from current metadata: {statement}"
    if status == "candidate_for_headline":
        return statement
    return f"Directional signal: {statement}"


def claim_unsafe(row: dict[str, str]) -> str:
    if row.get("decision") == "context_or_workflow_only":
        return "Do not present this as a paper-quality or venue-quality conclusion."
    return "Do not state as settled, paper-validated, causal, or quality-ranked until acceptance gates pass."


def area_allowed(row: dict[str, str], briefing: dict[str, str]) -> str:
    status = area_wording_status(row.get("risk_tier", ""), int(float(row.get("reviewed_rows", 0) or 0)))
    area = row.get("area", "")
    share = pct(row.get("taxonomy_share"))
    headline = briefing.get("headline", "")
    if status == "orientation_only":
        return f"For orientation: {area} accounts for {share} of the corpus; treat the area narrative as unreviewed and risk-sensitive."
    if status == "orientation_with_examples":
        return f"{area} can be summarized with reviewed examples and caveats: {headline}"
    return f"Directional area signal: {headline}"


def area_unsafe(row: dict[str, str]) -> str:
    if row.get("risk_tier") == "critical":
        return "Do not rank this area, make subarea-share claims, or use baseline contrasts as conclusions before first checks are done."
    return "Do not make fine-grained subarea, quality, or reproducibility claims without reviewed papers."


def main() -> int:
    claim_risk = read_csv(PROCESSED / "icml2026_claim_risk_register.csv")
    area_risk = read_csv(PROCESSED / "icml2026_area_risk_register.csv")
    area_briefings = {row["area"]: row for row in read_csv(PROCESSED / "icml2026_area_briefing_cards.csv")}

    rows: list[dict[str, object]] = []
    for row in claim_risk:
        status = claim_wording_status(row.get("decision", ""), row.get("risk_tier", ""))
        rows.append(
            {
                "statement_type": "claim",
                "id": row["claim_id"],
                "name": row["theme"],
                "wording_status": status,
                "risk_tier": row["risk_tier"],
                "decision": row["decision"],
                "allowed_wording": claim_allowed(row),
                "unsafe_wording": claim_unsafe(row),
                "required_caveat": row["primary_caveat"],
                "evidence_basis": row["current_evidence"],
                "promotion_condition": row["missing_for_promotion"],
                "falsification_test": row["falsification_test"],
                "first_artifact_to_open": row["first_briefs_to_open"] or "reports/icml2026_claim_risk_register.md",
            }
        )

    for row in area_risk:
        briefing = area_briefings.get(row["area"], {})
        reviewed_rows = int(float(row.get("reviewed_rows", 0) or 0))
        status = area_wording_status(row["risk_tier"], reviewed_rows)
        evidence = (
            f"{row['paper_count']} papers ({pct(row['taxonomy_share'])}); "
            f"oral {float(row['oral_enrichment']):.2f}x; public {float(row['public_attention_enrichment']):.2f}x; "
            f"historical delta {pp(row['historical_delta_vs_baseline'])}"
        )
        rows.append(
            {
                "statement_type": "area",
                "id": row["area"],
                "name": row["area"],
                "wording_status": status,
                "risk_tier": row["risk_tier"],
                "decision": "area_review_pending",
                "allowed_wording": area_allowed(row, briefing),
                "unsafe_wording": area_unsafe(row),
                "required_caveat": row["safe_language"],
                "evidence_basis": evidence,
                "promotion_condition": f"reviewed area rows {row['reviewed_rows']}/{row['review_rows']}; {row['main_risk_driver']}",
                "falsification_test": row["falsification_test"],
                "first_artifact_to_open": row["brief_path"] or "reports/icml2026_area_risk_register.md",
            }
        )

    fieldnames = [
        "statement_type",
        "id",
        "name",
        "wording_status",
        "risk_tier",
        "decision",
        "allowed_wording",
        "unsafe_wording",
        "required_caveat",
        "evidence_basis",
        "promotion_condition",
        "falsification_test",
        "first_artifact_to_open",
    ]
    write_csv(PROCESSED / "icml2026_safe_statement_register.csv", rows, fieldnames)
    write_report(rows)
    print(f"Wrote {PROCESSED / 'icml2026_safe_statement_register.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_safe_statement_register.md'}")
    return 0


def write_report(rows: list[dict[str, object]]) -> None:
    by_type = Counter(str(row["statement_type"]) for row in rows)
    by_status = Counter(str(row["wording_status"]) for row in rows)
    lines = [
        "# ICML 2026 Safe Statement Register",
        "",
        "Wording guardrails for using the current workspace in reports, memos, or presentations.",
        "This register separates what can be said now from what must remain a hypothesis until manual review is filled.",
        "",
        "## Snapshot",
        "",
        f"- Statements tracked: {len(rows)}",
        f"- Type mix: {', '.join(f'{key}: {value}' for key, value in by_type.items())}",
        f"- Wording status mix: {', '.join(f'{key}: {value}' for key, value in by_status.most_common())}",
        "",
        "## Claim Guardrails",
        "",
        "| ID | Status | Allowed wording | Unsafe wording | Promotion condition |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        if row["statement_type"] != "claim":
            continue
        lines.append(
            f"| `{row['id']}` {row['name']} | {row['wording_status']} | {row['allowed_wording']} | "
            f"{row['unsafe_wording']} | {row['promotion_condition']} |"
        )

    lines.extend(
        [
            "",
            "## Area Guardrails",
            "",
            "| Area | Status | Allowed wording | Required caveat | First artifact |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in rows:
        if row["statement_type"] != "area":
            continue
        lines.append(
            f"| {row['name']} | {row['wording_status']} | {row['allowed_wording']} | "
            f"{row['required_caveat']} | `{row['first_artifact_to_open']}` |"
        )

    lines.extend(["", "## Falsification Checks", ""])
    for row in rows:
        lines.extend(
            [
                f"### {row['id']}: {row['name']}",
                "",
                f"- Evidence basis: {row['evidence_basis']}",
                f"- Required caveat: {row['required_caveat']}",
                f"- Falsification test: {row['falsification_test']}",
                f"- First artifact to open: `{row['first_artifact_to_open']}`",
                "",
            ]
        )

    lines.extend(
        [
            "## Outputs",
            "",
            "- `data/processed/icml2026_safe_statement_register.csv`",
            "- `reports/icml2026_safe_statement_register.md`",
        ]
    )
    (REPORTS / "icml2026_safe_statement_register.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
