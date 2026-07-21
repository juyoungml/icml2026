#!/usr/bin/env python3
"""Build a paper-level artifact audit queue for ICML 2026."""

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


def optional_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    return read_csv(path)


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def intish(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def audit_category(row: dict[str, str], live: dict[str, str]) -> tuple[str, str]:
    if row.get("github_url") and live.get("qa_flags"):
        return "repo_flagged_live_check", f"GitHub API QA flags: {live['qa_flags']}"
    if row.get("artifact_confidence") == "needs_manual_check":
        return "metadata_suspicious_link", "AlphaXiv link looks like a template, homepage, awesome list, or index repository."
    if row.get("github_url") and not live:
        return "linked_unchecked_live_status", "GitHub URL exists but is outside the bounded live-check set."
    if row.get("github_url"):
        return "linked_needs_repro_check", "GitHub URL exists; inspect runnable code, data/checkpoints, license, and reproduction instructions."
    if row.get("award") or row.get("is_oral") == "true" or intish(row.get("public_total_votes", "")) >= 100:
        return "high_signal_no_github", "High-signal paper has no GitHub URL in AlphaXiv metadata."
    return "context", "Lower priority."


def priority(row: dict[str, str], live: dict[str, str], category: str) -> int:
    score = intish(row.get("public_total_votes", ""))
    score += intish(row.get("github_stars", "")) // 10
    if row.get("award"):
        score += 800
    if row.get("is_oral") == "true":
        score += 400
    if category in {"repo_flagged_live_check", "metadata_suspicious_link"}:
        score += 500
    if category == "high_signal_no_github":
        score += 250
    if live.get("license_spdx") in {"", "NOASSERTION"} and row.get("github_url"):
        score += 75
    return score


def manual_checks(category: str) -> str:
    common = [
        "artifact_type",
        "license",
        "install_or_run_instructions",
        "data_or_checkpoint_access",
        "result_reproduction_path",
    ]
    if category == "high_signal_no_github":
        return "search paper/pdf/supplement for code, data, project page, or delayed release statement"
    if category in {"repo_flagged_live_check", "metadata_suspicious_link"}:
        return "; ".join(["confirm link belongs to the paper", "reject template/index/star-inflated repo"] + common)
    return "; ".join(common)


def main() -> int:
    papers = read_csv(PROCESSED / "icml2026_reproducibility_papers.csv")
    live_rows = optional_csv(PROCESSED / "icml2026_github_artifact_live_check.csv")
    live_by_repo = {row["github_repo"]: row for row in live_rows}

    rows: list[dict[str, object]] = []
    for row in papers:
        live = live_by_repo.get(row.get("github_repo", ""), {})
        category, reason = audit_category(row, live)
        if category == "context":
            continue
        score = priority(row, live, category)
        if category == "linked_unchecked_live_status" and score < 150:
            continue
        rows.append(
            {
                "audit_rank": 0,
                "audit_priority_score": score,
                "audit_category": category,
                "event_id": row["event_id"],
                "title": row["title"],
                "topic_group": row["topic_group"],
                "is_oral": row["is_oral"],
                "award": row["award"],
                "public_total_votes": row["public_total_votes"],
                "github_url": row["github_url"],
                "github_repo": row["github_repo"],
                "alphaxiv_github_stars": row["github_stars"],
                "artifact_confidence": row["artifact_confidence"],
                "needs_manual_check_reason": row["needs_manual_check_reason"],
                "live_status": live.get("live_status", ""),
                "live_qa_flags": live.get("qa_flags", ""),
                "live_license_spdx": live.get("license_spdx", ""),
                "live_pushed_at": live.get("pushed_at", ""),
                "live_pushed_age_days": live.get("pushed_age_days", ""),
                "audit_reason": reason,
                "manual_checks": manual_checks(category),
                "alphaxiv_url": row["alphaxiv_url"],
                "icml_url": row["icml_url"],
            }
        )

    rows.sort(key=lambda row: (-int(row["audit_priority_score"]), str(row["title"])))
    rows = rows[:160]
    for idx, row in enumerate(rows, start=1):
        row["audit_rank"] = idx

    fieldnames = [
        "audit_rank",
        "audit_priority_score",
        "audit_category",
        "event_id",
        "title",
        "topic_group",
        "is_oral",
        "award",
        "public_total_votes",
        "github_url",
        "github_repo",
        "alphaxiv_github_stars",
        "artifact_confidence",
        "needs_manual_check_reason",
        "live_status",
        "live_qa_flags",
        "live_license_spdx",
        "live_pushed_at",
        "live_pushed_age_days",
        "audit_reason",
        "manual_checks",
        "alphaxiv_url",
        "icml_url",
    ]
    write_csv(PROCESSED / "icml2026_artifact_audit_queue.csv", rows, fieldnames)
    write_report(rows)
    print(f"Wrote {PROCESSED / 'icml2026_artifact_audit_queue.csv'} ({len(rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_artifact_audit_queue.md'}")
    return 0


def write_report(rows: list[dict[str, object]]) -> None:
    counts = Counter(str(row["audit_category"]) for row in rows)
    lines = [
        "# ICML 2026 Artifact Audit Queue",
        "",
        "Paper-level queue for checking whether artifact links support reproducibility claims.",
        "This uses AlphaXiv GitHub metadata plus the bounded GitHub live-check output when available.",
        "",
        "## Snapshot",
        "",
        f"- Papers queued: {len(rows)}",
        f"- Category mix: {', '.join(f'{k}: {v}' for k, v in sorted(counts.items()))}",
        "",
        "## Top Audit Targets",
        "",
        "| Rank | Category | Paper | Signal | Repository | Reason |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for row in rows[:40]:
        signal = []
        if row["award"]:
            signal.append(str(row["award"]))
        if row["is_oral"] == "true":
            signal.append("oral")
        signal.append(f"votes {row['public_total_votes']}")
        if row["alphaxiv_github_stars"]:
            signal.append(f"stars {row['alphaxiv_github_stars']}")
        lines.append(
            f"| {row['audit_rank']} | {row['audit_category']} | {row['title']} | "
            f"{'; '.join(signal)} | {row['github_repo'] or 'none'} | {row['audit_reason']} |"
        )
    lines.extend(
        [
            "",
            "## Required Manual Checks",
            "",
            "- Confirm the linked repository belongs to the paper.",
            "- Identify artifact type: code, benchmark, dataset, checkpoint, project page, index/list, or none.",
            "- Check license and release state.",
            "- Check install/run instructions and whether a minimal example exists.",
            "- Check data/checkpoint availability and whether results can plausibly be reproduced.",
            "",
            "## Outputs",
            "",
            "- `data/processed/icml2026_artifact_audit_queue.csv`",
            "- `reports/icml2026_artifact_audit_queue.md`",
        ]
    )
    (REPORTS / "icml2026_artifact_audit_queue.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
