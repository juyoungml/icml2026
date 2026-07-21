#!/usr/bin/env python3
"""Build narrative report and story-outline seeds for the ICML 2026 landscape."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"
DOCS = ROOT / "docs"


FIGURE_MAP = {
    "C01": ["figures/manual_taxonomy_area_sizes.png", "figures/historical_venue_area_deltas.png", "figures/arxiv_taxonomy_trends.png"],
    "C02": ["figures/historical_venue_area_deltas.png", "figures/program_signal_calibration.png"],
    "C03": ["figures/program_signal_calibration.png", "figures/cluster_public_vs_program_signal.png"],
    "C04": ["figures/program_signal_calibration.png", "figures/manual_taxonomy_area_sizes.png"],
    "C05": ["figures/historical_venue_area_deltas.png", "figures/arxiv_taxonomy_trends.png"],
    "C06": ["figures/arxiv_taxonomy_trends.png", "figures/historical_venue_area_deltas.png"],
    "C07": ["figures/manual_taxonomy_area_sizes.png", "figures/alphaxiv_attention_distributions.png"],
    "C08": ["figures/semantic_cluster_map.png", "figures/evidence_contribution_mix.png"],
}

CLAIM_PACKET = {
    "C01": "reports/claim_validation_packets/c01-llm-reasoning-center-of-gravity.md",
    "C02": "reports/claim_validation_packets/c02-infrastructure-and-agentic-workloads.md",
    "C03": "reports/claim_validation_packets/c03-program-committee-attention.md",
    "C04": "reports/claim_validation_packets/c04-public-attention-mismatch.md",
    "C05": "reports/claim_validation_packets/c05-neighboring-venue-contrast.md",
    "C06": "reports/claim_validation_packets/c06-external-trend-context.md",
    "C07": "reports/claim_validation_packets/c07-artifact-visibility.md",
    "C08": "reports/claim_validation_packets/c08-validation-priority.md",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"Missing required input: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def pct(value: str) -> str:
    try:
        return f"{float(value) * 100:.1f}%"
    except ValueError:
        return "n/a"


def pp(value: str) -> str:
    try:
        return f"{float(value) * 100:+.1f} pp"
    except ValueError:
        return "n/a"


def link(path: str, label: str | None = None) -> str:
    label = label or path
    return f"[{label}](../{path})"


def load_inputs() -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, dict[str, str]], list[dict[str, str]]]:
    claims = read_csv(PROCESSED / "icml2026_landscape_claim_register.csv")
    matrix = read_csv(PROCESSED / "icml2026_landscape_signal_matrix.csv")
    matrix_by_area = {row["area"]: row for row in matrix}
    validation = read_csv(PROCESSED / "workspace_validation_checks.csv")
    return claims, matrix, matrix_by_area, validation


def write_report_seed(claims: list[dict[str, str]], matrix: list[dict[str, str]], validation: list[dict[str, str]]) -> None:
    validation_failures = sum(row["status"] != "pass" for row in validation)
    rows_by_share = sorted(matrix, key=lambda row: float(row["taxonomy_share"]), reverse=True)
    lines = [
        "# ICML 2026 Overview Report Seed",
        "",
        "A long-form report blueprint grounded in the current EDA workspace.",
        "This is not a finished publication: it is a structured draft scaffold with claims, evidence, figures, caveats, and validation tasks.",
        "",
        "## Working Thesis",
        "",
        "ICML 2026 appears to be organized around foundation-model reasoning and post-training, with adjacent pressure from systems/efficiency and agentic workloads. Program signal remains more favorable to theory and safety/governance than public attention alone suggests, while robotics/world-model work shows the opposite pattern: small area share, high public attention. Multimodal/vision is large in absolute ICML volume but appears underweight relative to neighboring NeurIPS/ICLR accepted-paper baselines.",
        "",
        "## Workspace QA",
        "",
        f"- Current automated validation failures: {validation_failures}",
        f"- Validation report: {link('reports/workspace_validation.md', 'workspace_validation.md')}",
        f"- Claim validation packets: {link('reports/icml2026_claim_validation_packet_index.md', 'claim packet index')}",
        f"- Wording guardrails: {link('reports/icml2026_safe_statement_register.md', 'safe statement register')}",
        "",
        "Read the safe statement register before turning the working thesis or executive bullets into final prose.",
        "",
        "## Executive Summary Bullets",
        "",
    ]
    for claim in claims[:5]:
        lines.append(f"- **{claim['theme']}**: {claim['statement']} Evidence: {claim['evidence']}")

    lines.extend(
        [
            "",
            "## Section 1: Corpus And Method",
            "",
            "Purpose: establish what is counted, where signals come from, and what should not be overinterpreted.",
            "",
            "Core evidence:",
            "- Official ICML 2026 virtual-site corpus: 6,628 paper rows.",
            "- AlphaXiv joined snapshot: 6,628 rows matched to official ICML papers.",
            "- Manual taxonomy: 12 report-level areas over 42 semantic clusters.",
            "- Historical baseline: ICML 2025, NeurIPS 2025, and ICLR 2026 accepted-paper corpora classified with a shared keyword scorer.",
            "",
            "Use these figures:",
            f"- {link('figures/topic_group_distribution.png')}",
            f"- {link('figures/semantic_cluster_map.png')}",
            f"- {link('figures/manual_taxonomy_area_sizes.png')}",
            "",
            "Caveat to keep visible: taxonomy and evidence codes are strong for navigation but still need paper-level validation for publication claims.",
            "",
            "## Section 2: The Area Map",
            "",
            "Purpose: show the high-level shape of ICML 2026 before discussing attention or program signal.",
            "",
            "| Area | Papers | Share | Signal Tags |",
            "| --- | ---: | ---: | --- |",
        ]
    )
    for row in rows_by_share:
        lines.append(f"| {row['area']} | {row['taxonomy_papers']} | {pct(row['taxonomy_share'])} | {row['signal_tags'] or 'none'} |")

    lines.extend(
        [
            "",
            "Use these figures:",
            f"- {link('figures/manual_taxonomy_area_sizes.png')}",
            f"- {link('figures/semantic_cluster_map.png')}",
            "",
            "## Section 3: Claims To Build The Narrative Around",
            "",
        ]
    )
    for claim in claims:
        claim_id = claim["claim_id"]
        lines.extend(
            [
                f"### {claim_id}: {claim['theme']}",
                "",
                f"Claim: {claim['statement']}",
                "",
                f"Evidence: {claim['evidence']}",
                "",
                f"Strength: `{claim['strength']}`",
                "",
                f"Caveat: {claim['caveats']}",
                "",
                "Suggested figures:",
            ]
        )
        for figure in FIGURE_MAP.get(claim_id, []):
            lines.append(f"- {link(figure)}")
        lines.extend(
            [
                "",
                f"Validation packet: {link(CLAIM_PACKET[claim_id])}",
                "",
                f"Next validation: {claim['next_validation']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Section 4: Program Signal vs Public Attention",
            "",
            "Purpose: separate committee-visible importance from public/shareable attention.",
            "",
            "Main contrast to explain:",
            "- Theory and safety/governance are stronger in program signal than public attention.",
            "- Robotics/world models, LLM reasoning, systems, and agents are stronger in public attention.",
            "",
            "Use these figures:",
            f"- {link('figures/program_signal_calibration.png')}",
            f"- {link('figures/cluster_public_vs_program_signal.png')}",
            "",
            "## Section 5: External Baselines",
            "",
            "Purpose: prevent ICML-only analysis from confusing venue emphasis with field-wide trends.",
            "",
            "Use these figures:",
            f"- {link('figures/historical_venue_area_deltas.png')}",
            f"- {link('figures/arxiv_taxonomy_trends.png')}",
            "",
            "Interpretation guardrail: historical accepted-paper deltas are closer to venue comparison than arXiv counts; arXiv counts are broad trend context only.",
            "",
            "## Section 6: Reproducibility And Artifact Signals",
            "",
            "Purpose: distinguish artifact visibility from actual reproducibility.",
            "",
            "Use these reports:",
            f"- {link('reports/icml2026_reproducibility_lens.md')}",
            f"- {link('reports/icml2026_github_artifact_live_check.md')}",
            f"- {link('reports/claim_validation_packets/c07-artifact-visibility.md')}",
            "",
            "Interpretation guardrail: a GitHub URL is not runnable code, and a high-star repository can be a template, homepage, or unrelated index.",
            "",
            "## Section 7: What Must Be Manually Checked Before Publication",
            "",
            "- Boundary clusters in LLM reasoning, systems, data-centric ML, and AI-for-science.",
            "- Public-heavy but non-program robotics/world-model papers.",
            "- Program-heavy but low-public theory and safety/governance papers.",
            "- High-star GitHub links and template/index repositories.",
            "- Benchmark/dataset/metric tags generated from heuristics.",
            "",
            "Primary review entry points:",
            f"- {link('reports/icml2026_claim_validation_packet_index.md')}",
            f"- {link('reports/icml2026_validation_packet_index.md')}",
            f"- {link('data/processed/icml2026_claim_validation_queue.csv')}",
            f"- {link('data/processed/icml2026_manual_validation_queue.csv')}",
            "",
            "## Recommended Final Report Structure",
            "",
            "1. Corpus and signal sources",
            "2. ICML 2026 area map",
            "3. Foundation-model reasoning as center of gravity",
            "4. Systems and agents as adjacent overweights",
            "5. Program signal versus public attention",
            "6. Historical and arXiv baselines",
            "7. Artifact and reproducibility lens",
            "8. Caveats and validation agenda",
        ]
    )
    (REPORTS / "icml2026_overview_report_seed.md").write_text("\n".join(lines), encoding="utf-8")


def write_story_outline(claims: list[dict[str, str]]) -> None:
    lines = [
        "# ICML 2026 Story Outline Seed",
        "",
        "Compact narrative outline for a future presentation or executive briefing. This is not a generated slide deck.",
        "",
        "## 12-Part Story Arc",
        "",
        "| Step | Message | Figure / Evidence | Validation Hook |",
        "| ---: | --- | --- | --- |",
        "| 1 | What corpus are we analyzing? | `icml2026_papers.csv`: 6,628 rows; `alphaxiv_icml2026_joined.csv`: 6,628 rows | `workspace_validation.md` |",
        "| 2 | ICML 2026 needs a curated taxonomy, not only official topics. | `manual_taxonomy_area_sizes.png`; 12 areas over 42 semantic clusters | `icml2026_manual_taxonomy_seed.md` |",
        "| 3 | LLM reasoning/post-training is the center of gravity. | C01; area share 16.6%; public enrichment 2.03x | C01 claim packet |",
        "| 4 | Systems and agents are the adjacent applied pressure. | C02; historical deltas +2.1 pp each | C02 claim packet |",
        "| 5 | Program signal and public signal disagree. | `program_signal_calibration.png` | C03/C04 packets |",
        "| 6 | Theory and safety are more program-visible than public-visible. | C03; oral enrichments 1.45x and 1.41x | Review low-public/high-program papers |",
        "| 7 | Robotics/world models are public-heavy but small. | C04; 2.9% share; public enrichment 2.11x | Review robotics high-attention papers |",
        "| 8 | Multimodal/vision is big but not uniquely ICML-overweight. | C05; historical delta -3.1 pp | Break down subareas |",
        "| 9 | arXiv growth and accepted-paper baselines answer different questions. | `arxiv_taxonomy_trends.png`; `historical_venue_area_deltas.png` | C06 packet |",
        "| 10 | Artifact visibility is uneven and noisy. | C07; GitHub URL shares; live-check report | C07 packet |",
        "| 11 | The project is strongest as a navigational atlas today. | Claim register + validation queues | C08 packet |",
        "| 12 | The next jump is manual validation, not more charts. | 118 claim-review rows; 192 area-review rows | Reconcile reviewed CSVs |",
        "",
        "## Claim-To-Slide Mapping",
        "",
    ]
    for claim in claims:
        claim_id = claim["claim_id"]
        lines.append(f"### {claim_id}: {claim['theme']}")
        lines.append("")
        lines.append(f"- Message: {claim['statement']}")
        lines.append(f"- Evidence: {claim['evidence']}")
        lines.append(f"- Caveat: {claim['caveats']}")
        lines.append(f"- Figures: {', '.join(FIGURE_MAP.get(claim_id, []))}")
        lines.append(f"- Review packet: {CLAIM_PACKET[claim_id]}")
        lines.append("")
    lines.extend(
        [
            "## Presentation Guardrails",
            "",
            "- Do not present AlphaXiv votes as quality.",
            "- Do not present GitHub URLs as reproducibility.",
            "- Do not present arXiv query growth as accepted-paper growth.",
            "- Do not make subarea-level claims for `needs_review` clusters without manual packet review.",
            "- Keep program signal language precise: oral/award labels are committee-visible signals, not exhaustive quality labels.",
        ]
    )
    (REPORTS / "icml2026_story_outline_seed.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    claims, matrix, _matrix_by_area, validation = load_inputs()
    write_report_seed(claims, matrix, validation)
    write_story_outline(claims)
    print(f"Wrote {REPORTS / 'icml2026_overview_report_seed.md'}")
    print(f"Wrote {REPORTS / 'icml2026_story_outline_seed.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
