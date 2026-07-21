#!/usr/bin/env python3
"""Build a researcher-facing question agenda for understanding ICML 2026."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"


QUESTION_SPECS = [
    {
        "question_id": "Q01",
        "priority": 1,
        "question": "Is ICML 2026 genuinely centered on LLM reasoning and post-training?",
        "related_claims": ["C01"],
        "related_areas": ["LLM Reasoning, Post-Training, and RLVR"],
        "why_it_matters": "This is the strongest candidate for the report's central thesis, but it is also boundary-sensitive.",
    },
    {
        "question_id": "Q02",
        "priority": 2,
        "question": "Are systems, efficiency, agents, and code/tool papers a coherent infrastructure shift?",
        "related_claims": ["C02"],
        "related_areas": ["Systems and Efficient Foundation Models", "Agents, Code, and Tool Use"],
        "why_it_matters": "The workspace shows neighboring-venue overweight signals, but a researcher needs to know whether this is one movement or several unrelated pockets.",
    },
    {
        "question_id": "Q03",
        "priority": 3,
        "question": "What does the ICML program emphasize that public attention misses?",
        "related_claims": ["C03"],
        "related_areas": ["Theory, Optimization, and Algorithms", "Safety, Governance, Privacy, and Society"],
        "why_it_matters": "This separates committee-visible importance from AlphaXiv visibility and helps avoid popularity-as-quality errors.",
    },
    {
        "question_id": "Q04",
        "priority": 4,
        "question": "Why do robotics and world-model papers attract public attention despite small corpus share?",
        "related_claims": ["C04"],
        "related_areas": ["Robotics, Embodiment, and World Models"],
        "why_it_matters": "This is a clear public/program mismatch and could reflect demo visibility, VLA excitement, or reusable benchmark/model work.",
    },
    {
        "question_id": "Q05",
        "priority": 5,
        "question": "Is multimodal/vision really underweight at ICML 2026, or is that a baseline/classifier artifact?",
        "related_claims": ["C05"],
        "related_areas": ["Multimodal, Vision, and Perception"],
        "why_it_matters": "This is the riskiest neighboring-venue contrast because arXiv growth and accepted-paper baselines point in different directions.",
    },
    {
        "question_id": "Q06",
        "priority": 6,
        "question": "Do visible artifact links correspond to runnable, reproducible work?",
        "related_claims": ["C07"],
        "related_areas": ["Agents, Code, and Tool Use", "LLM Reasoning, Post-Training, and RLVR", "Systems and Efficient Foundation Models"],
        "why_it_matters": "The corpus has many GitHub links, but repository visibility is not the same as reproducibility.",
        "first_artifacts_override": "reports/icml2026_artifact_audit_queue.md ; reports/icml2026_github_artifact_live_check.md ; reports/icml2026_reproducibility_lens.md",
    },
    {
        "question_id": "Q07",
        "priority": 7,
        "question": "Which taxonomy boundaries could change the top-level landscape story?",
        "related_claims": ["C01", "C02", "C05"],
        "related_areas": ["LLM Reasoning, Post-Training, and RLVR", "Theory, Optimization, and Algorithms", "AI for Science, Health, and Neuro"],
        "why_it_matters": "Area-ranking and subarea conclusions can be distorted by boundary clusters before manual adjudication.",
    },
    {
        "question_id": "Q08",
        "priority": 8,
        "question": "How should arXiv trend signals be used without implying venue quality or causality?",
        "related_claims": ["C06"],
        "related_areas": ["Multimodal, Vision, and Perception", "LLM Reasoning, Post-Training, and RLVR", "Safety, Governance, Privacy, and Society"],
        "why_it_matters": "Broad arXiv queries are useful context, but they are overlapping and should not become field-quality claims.",
        "first_artifacts_override": "reports/icml2026_baseline_sensitivity_queue.md ; reports/arxiv_taxonomy_trends.md ; reports/historical_accepted_paper_baseline.md",
    },
    {
        "question_id": "Q09",
        "priority": 9,
        "question": "Which area summaries are safe to use now, and which need stronger caveats?",
        "related_claims": ["C08"],
        "related_areas": [],
        "why_it_matters": "A researcher needs practical wording rules before turning exploratory EDA into report or presentation language.",
        "first_artifacts_override": "reports/icml2026_safe_statement_register.md ; reports/icml2026_area_risk_register.md ; reports/icml2026_claim_risk_register.md",
    },
    {
        "question_id": "Q10",
        "priority": 10,
        "question": "Which papers should be read first to validate or weaken the whole thesis?",
        "related_claims": ["C01", "C02", "C03", "C04", "C05", "C07"],
        "related_areas": [],
        "why_it_matters": "The fastest path to a stronger brief is not more plots; it is reading the papers that can move claim decisions.",
        "first_artifacts_override": "reports/icml2026_researcher_action_plan.md ; reports/icml2026_sprint_reading_brief_index.md ; reports/icml2026_claim_decision_board.md",
    },
]


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


def split_list(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def join(items: list[str], limit: int | None = None) -> str:
    if limit is not None:
        items = items[:limit]
    return " ; ".join(item for item in items if item)


def first_briefs(
    briefs: list[dict[str, str]],
    related_claims: list[str],
    related_areas: list[str],
    limit: int = 4,
) -> tuple[str, str]:
    selected = []
    for row in briefs:
        row_claims = split_list(row.get("target_claims", ""))
        if any(claim in row_claims for claim in related_claims) or row.get("area", "") in related_areas:
            selected.append(row)
    selected.sort(key=lambda row: (row.get("sprint", ""), int(float(row.get("sprint_rank", 999) or 999))))
    papers = [
        f"{row.get('sprint')} #{row.get('sprint_rank')}: {row.get('title')} ({row.get('event_id')})"
        for row in selected[:limit]
    ]
    paths = [row.get("brief_path", "") for row in selected[:limit]]
    return join(papers), join(paths)


def claim_field(claims: dict[str, dict[str, str]], claim_ids: list[str], field: str, limit: int = 2) -> str:
    return join([claims[claim_id].get(field, "") for claim_id in claim_ids if claim_id in claims], limit)


def area_field(areas: dict[str, dict[str, str]], area_names: list[str], field: str, limit: int = 2) -> str:
    return join([areas[area].get(field, "") for area in area_names if area in areas], limit)


def main() -> int:
    claim_risk = {row["claim_id"]: row for row in read_csv(PROCESSED / "icml2026_claim_risk_register.csv")}
    area_risk = {row["area"]: row for row in read_csv(PROCESSED / "icml2026_area_risk_register.csv")}
    safe = {row["id"]: row for row in read_csv(PROCESSED / "icml2026_safe_statement_register.csv")}
    briefs = read_csv(PROCESSED / "icml2026_sprint_reading_briefs.csv")
    baseline = {row["area"]: row for row in read_csv(PROCESSED / "icml2026_baseline_sensitivity_queue.csv")}
    artifact_queue = read_csv(PROCESSED / "icml2026_artifact_audit_queue.csv")

    rows: list[dict[str, object]] = []
    for spec in QUESTION_SPECS:
        related_claims = list(spec["related_claims"])
        related_areas = list(spec["related_areas"])
        papers, paths = first_briefs(briefs, related_claims, related_areas)
        if spec["question_id"] == "Q06":
            papers = join(
                [
                    f"artifact #{row.get('audit_rank')}: {row.get('title')} ({row.get('event_id')})"
                    for row in artifact_queue[:4]
                ]
            )
        evidence = claim_field(claim_risk, related_claims, "current_evidence")
        if not evidence:
            evidence = area_field(area_risk, related_areas, "main_risk_driver")
        falsification = claim_field(claim_risk, related_claims, "falsification_test", 1)
        if not falsification:
            falsification = area_field(area_risk, related_areas, "falsification_test", 1)
        safe_wording = claim_field(safe, related_claims, "allowed_wording", 1)
        if not safe_wording and related_areas:
            safe_wording = area_field(safe, related_areas, "allowed_wording", 1)
        baseline_checks = area_field(baseline, related_areas, "check_question", 1)
        next_action = claim_field(claim_risk, related_claims, "next_decision_action", 1)
        if not next_action:
            next_action = area_field(area_risk, related_areas, "recommended_first_checks", 1)
        rows.append(
            {
                "question_id": spec["question_id"],
                "priority": spec["priority"],
                "question": spec["question"],
                "why_it_matters": spec["why_it_matters"],
                "current_answer_status": status_for_question(related_claims, related_areas, claim_risk, area_risk),
                "related_claims": "; ".join(related_claims),
                "related_areas": "; ".join(related_areas) if related_areas else "cross_area",
                "evidence_basis": evidence,
                "safe_current_wording": safe_wording,
                "falsification_test": falsification,
                "baseline_check": baseline_checks,
                "first_papers_to_read": papers,
                "first_artifacts_to_open": spec.get("first_artifacts_override") or paths or first_artifacts(related_claims, related_areas),
                "next_action": next_action,
            }
        )

    fieldnames = [
        "question_id",
        "priority",
        "question",
        "why_it_matters",
        "current_answer_status",
        "related_claims",
        "related_areas",
        "evidence_basis",
        "safe_current_wording",
        "falsification_test",
        "baseline_check",
        "first_papers_to_read",
        "first_artifacts_to_open",
        "next_action",
    ]
    write_csv(PROCESSED / "icml2026_research_questions_agenda.csv", rows, fieldnames)
    write_report(rows)
    print(f"Wrote {PROCESSED / 'icml2026_research_questions_agenda.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_research_questions_agenda.md'}")
    return 0


def status_for_question(
    related_claims: list[str],
    related_areas: list[str],
    claim_risk: dict[str, dict[str, str]],
    area_risk: dict[str, dict[str, str]],
) -> str:
    claim_tiers = {claim_risk[claim].get("risk_tier", "") for claim in related_claims if claim in claim_risk}
    area_tiers = {area_risk[area].get("risk_tier", "") for area in related_areas if area in area_risk}
    if "critical" in claim_tiers or "critical" in area_tiers:
        return "high_value_hypothesis_needs_review"
    if "high" in claim_tiers or "high" in area_tiers:
        return "directional_needs_spot_check"
    return "context_or_workflow_question"


def first_artifacts(related_claims: list[str], related_areas: list[str]) -> str:
    artifacts = []
    if related_claims:
        artifacts.append("reports/icml2026_claim_risk_register.md")
    if related_areas:
        artifacts.append("reports/icml2026_area_risk_register.md")
    artifacts.append("reports/icml2026_safe_statement_register.md")
    return join(artifacts)


def write_report(rows: list[dict[str, object]]) -> None:
    lines = [
        "# ICML 2026 Research Questions Agenda",
        "",
        "Prioritized questions for using the workspace as a ML researcher rather than only as an EDA artifact collection.",
        "",
        "## Agenda",
        "",
        "| Priority | Question | Current status | First artifacts |",
        "| ---: | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['priority']} | {row['question']} | {row['current_answer_status']} | {row['first_artifacts_to_open']} |"
        )
    lines.extend(["", "## Question Details", ""])
    for row in rows:
        lines.extend(
            [
                f"### {row['question_id']}: {row['question']}",
                "",
                f"- Why it matters: {row['why_it_matters']}",
                f"- Related claims: {row['related_claims']}",
                f"- Related areas: {row['related_areas']}",
                f"- Evidence basis: {row['evidence_basis'] or 'see linked artifacts'}",
                f"- Safe current wording: {row['safe_current_wording'] or 'Use only as a review question until safe wording is available.'}",
                f"- Falsification test: {row['falsification_test'] or 'Review linked packets and area risk rows.'}",
                f"- Baseline check: {row['baseline_check'] or 'not primary'}",
                f"- First papers: {row['first_papers_to_read'] or 'see linked artifacts'}",
                f"- Next action: {row['next_action'] or 'Open the linked artifacts and fill manual review notes.'}",
                "",
            ]
        )
    lines.extend(
        [
            "## Outputs",
            "",
            "- `data/processed/icml2026_research_questions_agenda.csv`",
            "- `reports/icml2026_research_questions_agenda.md`",
        ]
    )
    (REPORTS / "icml2026_research_questions_agenda.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
