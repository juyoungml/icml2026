#!/usr/bin/env python3
"""Build paper-by-claim decision tasks for the ICML 2026 review sprints."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"


CLAIM_FOCUS = {
    "C01": "boundary_check_llm_reasoning",
    "C02": "infrastructure_coherence",
    "C03": "program_attention_explanation",
    "C04": "public_attention_calibration",
    "C05": "baseline_taxonomy_sensitivity",
    "C06": "trend_context_guardrail",
    "C07": "artifact_reproducibility",
    "C08": "workflow_validation",
}

SUPPORT_TESTS = {
    "C01": "Supports if the paper's main contribution is genuinely LLM reasoning, post-training, RLVR, or closely adjacent language-model capability work rather than a generic system/evaluation spillover.",
    "C02": "Supports if the paper contributes reusable infrastructure, efficiency, optimization, agent/tool/code workflow machinery, or a workload shift that is not just ordinary model training.",
    "C03": "Supports if the paper gives a concrete technical reason for oral/award/program attention that is not captured by public votes alone.",
    "C04": "Supports if high public attention tracks robotics/world-model/VLA utility, demos, benchmarks, or reusable embodied-model work despite low area share.",
    "C05": "Supports if the paper confirms multimodal/vision is a large but differently composed ICML area, or clarifies why neighboring-venue baselines make it look underweight.",
    "C06": "Supports only as context if the paper illustrates why arXiv/venue trend language must be caveated; do not treat as quality evidence.",
    "C07": "Supports if the linked artifact is real and inspectable, with enough code/data/checkpoints/examples to strengthen artifact-visibility claims.",
    "C08": "Supports if the paper exposes a taxonomy, claim, or evidence ambiguity that validates the need for manual review gates.",
}

WEAKENING_TESTS = {
    "C01": "Weakens if the assigned LLM reasoning/post-training label is secondary, wrong, or too broad for the paper's actual contribution.",
    "C02": "Weakens if the paper is mainly a narrow model result, benchmark, or theoretical claim with little infrastructure/agent relevance.",
    "C03": "Weakens if program signal appears unrelated to technical novelty, or if the paper is not actually program-ahead-of-public after inspection.",
    "C04": "Weakens if attention is driven mainly by title/project-page effects and not by substantive robotics/world-model contribution.",
    "C05": "Weakens if the paper belongs to a submode that makes the aggregate multimodal/vision comparison misleading or non-comparable.",
    "C06": "Weakens unsafe trend language if the paper shows arXiv query terms do not map cleanly to the accepted-paper taxonomy.",
    "C07": "Weakens if the repository is absent, stale, non-runnable, only a project page, lacks license/data/checkpoints, or cannot reproduce the claimed result.",
    "C08": "Weakens workflow confidence if the paper is easy to classify and does not touch any high-risk boundary or claim ambiguity.",
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


def split_semicolon(value: str) -> list[str]:
    return [part.strip() for part in (value or "").replace("|", ";").split(";") if part.strip()]


def task_priority(row: dict[str, str], claim: dict[str, str]) -> int:
    sprint_offset = 0 if row.get("sprint") == "sprint_01" else 1000
    try:
        rank = int(row.get("sprint_rank") or row.get("global_review_rank") or 999)
    except ValueError:
        rank = 999
    role_weight = {
        "core_thesis_candidate": 0,
        "supporting_hypothesis": 100,
        "context_frame": 200,
        "workflow_claim": 300,
    }.get(claim.get("thesis_role", ""), 400)
    return sprint_offset + rank + role_weight


def source_artifacts(row: dict[str, str], claim_id: str) -> str:
    artifacts = [
        row.get("brief_path", ""),
        *split_semicolon(row.get("claim_packet_links", "")),
        *split_semicolon(row.get("claim_dossier_links", "")),
        row.get("area_briefing_link", ""),
    ]
    filtered = []
    for artifact in artifacts:
        if artifact and artifact not in filtered:
            if claim_id.lower() in artifact.lower() or "claim_" not in artifact:
                filtered.append(artifact)
    return " ; ".join(filtered[:5])


def note_file_for_sprint(sprint: str) -> str:
    if sprint == "sprint_02":
        return "data/manual/icml2026_review_sprint_02_paper_notes.csv"
    return "data/manual/icml2026_review_sprint_01_paper_notes.csv"


def build_tasks() -> list[dict[str, object]]:
    briefs = read_csv(PROCESSED / "icml2026_sprint_reading_briefs.csv")
    claims = {row["claim_id"]: row for row in read_csv(PROCESSED / "icml2026_claim_decision_board.csv")}
    criteria = {row["claim_id"]: row for row in read_csv(PROCESSED / "icml2026_claim_acceptance_criteria.csv")}

    rows: list[dict[str, object]] = []
    seen: set[tuple[str, str]] = set()
    for brief in briefs:
        for claim_id in split_semicolon(brief.get("target_claims", "")):
            if claim_id not in claims:
                continue
            key = (brief.get("event_id", ""), claim_id)
            if key in seen:
                continue
            seen.add(key)
            claim = claims[claim_id]
            gate = criteria.get(claim_id, claim)
            overlay_key = f"{claim_id}::{brief.get('event_id', '')}"
            required_fields = [
                "contribution_summary",
                "novelty_judgment",
                "method_summary",
                "evidence_strength",
                "baselines_checked",
                "limitations",
                "claim_implications",
                "taxonomy_correction",
                "final_report_use",
            ]
            if brief.get("github_url", "").strip() or claim_id == "C07":
                required_fields.extend(["artifact_status_checked", "reproducibility_notes"])
            rows.append(
                {
                    "task_id": f"{claim_id}-{brief.get('event_id', '')}",
                    "priority_score": task_priority(brief, claim),
                    "sprint": brief.get("sprint", ""),
                    "sprint_rank": brief.get("sprint_rank", ""),
                    "event_id": brief.get("event_id", ""),
                    "title": brief.get("title", ""),
                    "claim_id": claim_id,
                    "claim_theme": claim.get("theme", ""),
                    "thesis_role": claim.get("thesis_role", ""),
                    "claim_decision": claim.get("decision", ""),
                    "readiness_tier": claim.get("readiness_tier", ""),
                    "area": brief.get("area", ""),
                    "subarea": brief.get("subarea", ""),
                    "task_focus": CLAIM_FOCUS.get(claim_id, "claim_validation"),
                    "why_this_paper": brief.get("signals", "") or brief.get("reviewer_warning", ""),
                    "claim_question": brief.get("claim_prompt", ""),
                    "minimum_decision_needed": gate.get("missing_for_promotion", "none"),
                    "what_to_extract": " ; ".join(
                        part
                        for part in [
                            brief.get("contribution_prompt", ""),
                            brief.get("method_prompt", ""),
                            brief.get("evidence_prompt", ""),
                            brief.get("taxonomy_prompt", ""),
                            brief.get("artifact_prompt", ""),
                        ]
                        if part
                    ),
                    "support_signal": SUPPORT_TESTS.get(claim_id, ""),
                    "weakening_signal": WEAKENING_TESTS.get(claim_id, ""),
                    "blocking_risk": gate.get("special_check", "") or claim.get("special_check", ""),
                    "required_manual_fields": " ; ".join(required_fields),
                    "source_artifacts": source_artifacts(brief, claim_id),
                    "writeback_targets": f"{note_file_for_sprint(brief.get('sprint', ''))} ; data/manual/claim_review_overrides.csv::{overlay_key}",
                    "next_action": "Read PDF, fill paper-note fields, then transfer claim support/taxonomy/artifact judgment through the overlay bridge.",
                }
            )
    rows.sort(key=lambda row: (int(row["priority_score"]), str(row["claim_id"]), str(row["event_id"])))
    for idx, row in enumerate(rows, start=1):
        row["priority_rank"] = idx
    return rows


def write_report(rows: list[dict[str, object]]) -> None:
    by_claim: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_focus = Counter(str(row["task_focus"]) for row in rows)
    for row in rows:
        by_claim[str(row["claim_id"])].append(row)

    lines = [
        "# ICML 2026 Review Decision Tasks",
        "",
        "Paper-by-claim task matrix for converting sprint reading into explicit claim decisions.",
        "",
        "This is a routing layer, not a review result. All rows still require PDF/paper inspection before any claim is promoted.",
        "",
        "## Snapshot",
        "",
        f"- Decision tasks: {len(rows)}",
        f"- Papers covered: {len({row['event_id'] for row in rows})}",
        f"- Claims covered: {len(by_claim)}",
        f"- Task focuses: {', '.join(f'{focus}={count}' for focus, count in sorted(by_focus.items()))}",
        "",
        "## Claim Coverage",
        "",
        "| Claim | Tasks | First papers | Blocking risk |",
        "| --- | ---: | --- | --- |",
    ]
    for claim_id in sorted(by_claim):
        claim_rows = by_claim[claim_id]
        first_papers = " ; ".join(f"{row['sprint']} #{row['sprint_rank']}: {row['title']}" for row in claim_rows[:4])
        blocking_risk = str(claim_rows[0].get("blocking_risk", ""))
        lines.append(f"| {claim_id} | {len(claim_rows)} | {first_papers} | {blocking_risk} |")

    lines.extend(
        [
            "",
            "## First 20 Tasks",
            "",
            "| Rank | Task | Focus | Paper | Decision needed |",
            "| ---: | --- | --- | --- | --- |",
        ]
    )
    for row in rows[:20]:
        lines.append(
            f"| {row['priority_rank']} | {row['task_id']} | {row['task_focus']} | {row['title']} | {row['minimum_decision_needed']} |"
        )

    lines.extend(["", "## Claim-Specific Tests", ""])
    for claim_id in sorted(by_claim):
        row = by_claim[claim_id][0]
        lines.extend(
            [
                f"### {claim_id}: {row['claim_theme']}",
                "",
                f"- Support signal: {row['support_signal']}",
                f"- Weakening signal: {row['weakening_signal']}",
                f"- Required manual fields: {row['required_manual_fields']}",
                f"- First source artifacts: {row['source_artifacts']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Outputs",
            "",
            "- `data/processed/icml2026_review_decision_tasks.csv`",
            "- `reports/icml2026_review_decision_tasks.md`",
        ]
    )
    (REPORTS / "icml2026_review_decision_tasks.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    rows = build_tasks()
    fieldnames = [
        "priority_rank",
        "task_id",
        "priority_score",
        "sprint",
        "sprint_rank",
        "event_id",
        "title",
        "claim_id",
        "claim_theme",
        "thesis_role",
        "claim_decision",
        "readiness_tier",
        "area",
        "subarea",
        "task_focus",
        "why_this_paper",
        "claim_question",
        "minimum_decision_needed",
        "what_to_extract",
        "support_signal",
        "weakening_signal",
        "blocking_risk",
        "required_manual_fields",
        "source_artifacts",
        "writeback_targets",
        "next_action",
    ]
    write_csv(PROCESSED / "icml2026_review_decision_tasks.csv", rows, fieldnames)
    write_report(rows)
    print(f"Wrote {PROCESSED / 'icml2026_review_decision_tasks.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_review_decision_tasks.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
