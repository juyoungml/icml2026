#!/usr/bin/env python3
"""Build conservative seed judgments for the bounded PDF review subset."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"


PAPER_ROWS = [
    {
        "event_id": "62989",
        "evidence_pages_checked": "p1; p2; p3; p12; p20",
        "paper_read_status_suggestion": "skimmed",
        "contribution_summary_seed": "Estimates language-model memorization capacity by separating unintended memorization from generalization and measuring capacity across many transformer language models.",
        "novelty_judgment_suggestion": "new_method",
        "method_summary_seed": "Defines a memorization estimator, trains transformer language models over controlled data/model-size sweeps, and relates model capacity, dataset size, grokking, and membership inference behavior.",
        "evidence_strength_suggestion": "strong",
        "baselines_checked_seed": "Controlled synthetic and real-text model/data-size sweeps; membership-inference scaling analysis.",
        "datasets_checked_seed": "Synthetic bitstrings and real text training sets.",
        "metrics_checked_seed": "Total memorization bits, bits per parameter, train/test loss, membership inference behavior.",
        "limitations_seed": "Strong for memorization/capacity, but it is not primarily a reasoning, RLVR, or diffusion-language-model paper.",
        "artifact_status_checked_suggestion": "linked_unchecked",
        "reproducibility_notes_seed": "GitHub URL is present in metadata but was not inspected in this seed pass.",
        "claim_implications_seed": "Good caveat for C01: it is central LLM capability work but not a reasoning/post-training exemplar. Supports C08 because it exposes a taxonomy-boundary risk.",
        "taxonomy_correction_suggestion": "relabel_subarea",
        "final_report_use_suggestion": "caveat_example",
        "reviewer_caveat": "Use as a boundary example unless a reviewer broadens C01 beyond reasoning/post-training.",
    },
    {
        "event_id": "66206",
        "evidence_pages_checked": "p1; p2; p3; p8",
        "paper_read_status_suggestion": "skimmed",
        "contribution_summary_seed": "Provides an end-to-end theoretical account of grokking in ridge regression, including quantitative grokking-time bounds and empirical checks beyond the linear setting.",
        "novelty_judgment_suggestion": "stronger_theory",
        "method_summary_seed": "Analyzes over-parameterized linear regression trained with gradient descent and weight decay, proving delayed generalization phases and hyperparameter dependencies.",
        "evidence_strength_suggestion": "strong",
        "baselines_checked_seed": "Prior grokking explanations and empirical simulations are positioned as comparison context.",
        "datasets_checked_seed": "Teacher-student linear regression setup plus non-linear neural-network experiments.",
        "metrics_checked_seed": "Generalization delay, training/test error phases, hyperparameter-dependent grokking time.",
        "limitations_seed": "Core proof is in a classical regression setting, so direct foundation-model landscape claims should be caveated.",
        "artifact_status_checked_suggestion": "not_applicable",
        "reproducibility_notes_seed": "No repository link in the bounded source map; theory paper does not require an artifact for the current claim use.",
        "claim_implications_seed": "Supports C03 as a clear technical reason for program attention that public-vote metrics might miss. Supports C08 as a high-value theory boundary check.",
        "taxonomy_correction_suggestion": "keep",
        "final_report_use_suggestion": "headline_example",
        "reviewer_caveat": "Use for program-signal calibration, not as evidence of empirical trend size.",
    },
    {
        "event_id": "61998",
        "evidence_pages_checked": "p1; p2; p3; p4; p12",
        "paper_read_status_suggestion": "skimmed",
        "contribution_summary_seed": "Argues that arbitrary-order diffusion language-model generation can reduce reasoning potential, and proposes using standard autoregressive GRPO as a simpler RL scaffold.",
        "novelty_judgment_suggestion": "new_method",
        "method_summary_seed": "Compares arbitrary-order and autoregressive decoding using pass@k reasoning coverage, then trains diffusion LMs with a simplified GRPO-style procedure.",
        "evidence_strength_suggestion": "moderate",
        "baselines_checked_seed": "Compares against diffusion-specific RL adaptations and reproduced matched configurations where available.",
        "datasets_checked_seed": "Reasoning tasks including mathematics and coding evaluations.",
        "metrics_checked_seed": "Pass@k, reasoning accuracy, matched RL training comparisons.",
        "limitations_seed": "The argument is task-scope dependent: arbitrary-order generation may still matter outside the checked reasoning/coding settings.",
        "artifact_status_checked_suggestion": "linked_unchecked",
        "reproducibility_notes_seed": "GitHub URL is present in metadata but was not inspected in this seed pass.",
        "claim_implications_seed": "Supports C01 as a direct LLM reasoning/post-training example. Supports C08 because it validates the need to read method details before accepting broad diffusion-LM claims.",
        "taxonomy_correction_suggestion": "keep",
        "final_report_use_suggestion": "headline_example",
        "reviewer_caveat": "Promote only with a caveat that the finding is about eliciting reasoning in dLLMs, not a universal rejection of arbitrary-order generation.",
    },
    {
        "event_id": "65901",
        "evidence_pages_checked": "p1; p2; p3; p6; p14",
        "paper_read_status_suggestion": "skimmed",
        "contribution_summary_seed": "Finds that pretrained large models can have dense neighborhoods of useful task-specific perturbations and proposes RandOpt as a cheap random-search post-training method.",
        "novelty_judgment_suggestion": "new_method",
        "method_summary_seed": "Samples Gaussian weight perturbations around pretrained weights, studies solution density across model sizes and tasks, and ensembles promising random adaptations.",
        "evidence_strength_suggestion": "moderate",
        "baselines_checked_seed": "Compares RandOpt with gradient/RL-style optimization baselines in selected tasks.",
        "datasets_checked_seed": "Tasks named in the checked pages include math, writing, programming, chemistry, Countdown, and synthetic signal pretraining probes.",
        "metrics_checked_seed": "Solution density, task-improving perturbation rate, training-step and FLOP efficiency, converged accuracy.",
        "limitations_seed": "Infrastructure relevance is indirect: this is efficient post-training/optimization, not an agentic workflow or serving-system paper.",
        "artifact_status_checked_suggestion": "linked_unchecked",
        "reproducibility_notes_seed": "GitHub URL is present in metadata but was not inspected in this seed pass.",
        "claim_implications_seed": "Partially supports C02 through efficient adaptation infrastructure, but weakens any overly broad agentic-workload framing. Supports C06 as a caveat that trend labels can blur optimization, systems, and model-behavior work.",
        "taxonomy_correction_suggestion": "split_boundary",
        "final_report_use_suggestion": "caveat_example",
        "reviewer_caveat": "Good example of taxonomy ambiguity between efficient foundation models, optimization, and post-training.",
    },
    {
        "event_id": "65332",
        "evidence_pages_checked": "p1; p2; p4; p5; p12",
        "paper_read_status_suggestion": "skimmed",
        "contribution_summary_seed": "Introduces Maximum Likelihood Reinforcement Learning, a sampling-based framework that targets likelihood objectives for binary outcome feedback tasks.",
        "novelty_judgment_suggestion": "new_method",
        "method_summary_seed": "Shows classical RL optimizes a first-order approximation of maximum likelihood, then defines compute-indexed sample objectives and policy-gradient estimators approaching ML with more sampling.",
        "evidence_strength_suggestion": "moderate",
        "baselines_checked_seed": "Compares against standard RL/pass@1-style optimization and evaluates Pareto behavior in sampling-based tasks.",
        "datasets_checked_seed": "Examples include navigation, code generation, and mathematical problem solving; detailed task list requires a fuller appendix pass.",
        "metrics_checked_seed": "Pass@k-style success, likelihood approximation behavior, Pareto efficiency.",
        "limitations_seed": "It is RL for sampling-based generation broadly, not specifically an LLM reasoning center-of-gravity paper unless scoped through code/math generation.",
        "artifact_status_checked_suggestion": "linked_unchecked",
        "reproducibility_notes_seed": "GitHub URL is present in metadata but was not inspected in this seed pass.",
        "claim_implications_seed": "Partial support for C01 because it is relevant to RL-based reasoning tasks, but the taxonomy should mark it as a boundary with general RL/optimization. Supports C08 as a classification stress test.",
        "taxonomy_correction_suggestion": "split_boundary",
        "final_report_use_suggestion": "supporting_example",
        "reviewer_caveat": "Do not use as a pure LLM post-training headline without checking experiments and artifact.",
    },
    {
        "event_id": "65206",
        "evidence_pages_checked": "p1; p2; p3; p10; p11",
        "paper_read_status_suggestion": "skimmed",
        "contribution_summary_seed": "Presents an agentic framework for automating publication-ready academic illustrations and a benchmark for evaluating methodology-diagram generation.",
        "novelty_judgment_suggestion": "better_system",
        "method_summary_seed": "Orchestrates specialized agents for reference retrieval, planning, rendering, and self-critique, then evaluates outputs on a curated academic-illustration benchmark.",
        "evidence_strength_suggestion": "moderate",
        "baselines_checked_seed": "Compares with leading diagram/illustration generation baselines.",
        "datasets_checked_seed": "PaperBananaBench with 292 methodology-diagram cases curated from NeurIPS 2025 publications.",
        "metrics_checked_seed": "Faithfulness, conciseness, readability, aesthetics, and plot-generation quality.",
        "limitations_seed": "Artifact and benchmark availability need direct repository inspection before using this as a reproducibility claim.",
        "artifact_status_checked_suggestion": "linked_unchecked",
        "reproducibility_notes_seed": "GitHub URL is present in metadata but was not inspected in this seed pass.",
        "claim_implications_seed": "Supports C02 as an agentic research-workflow tool paper. Only partially supports C07 until repository contents and benchmark release are inspected.",
        "taxonomy_correction_suggestion": "keep",
        "final_report_use_suggestion": "headline_example",
        "reviewer_caveat": "Strong landscape example for AI-scientist workflow automation, but artifact claim remains unchecked.",
    },
    {
        "event_id": "60766",
        "evidence_pages_checked": "p1; p3; p4; p5; p6",
        "paper_read_status_suggestion": "skimmed",
        "contribution_summary_seed": "Studies whether RL training against deception detectors causes models to obfuscate, using a realistic coding reward-hacking setup and a taxonomy of outcomes.",
        "novelty_judgment_suggestion": "new_problem",
        "method_summary_seed": "Constructs deception probes, classifies policy outcomes into honest, blatant deception, obfuscated policy, and obfuscated activations, and analyzes RL/KL effects.",
        "evidence_strength_suggestion": "strong",
        "baselines_checked_seed": "Compares detector-penalty behavior, representation drift, and KL-regularized training outcomes.",
        "datasets_checked_seed": "Coding environment with reward hacking via hardcoded test cases.",
        "metrics_checked_seed": "Probe score, representation change, task return, policy class outcomes.",
        "limitations_seed": "Safety-specific and not a broad landscape trend-size estimator; should be used to explain technical salience rather than volume.",
        "artifact_status_checked_suggestion": "linked_unchecked",
        "reproducibility_notes_seed": "GitHub URL is present in metadata but was not inspected in this seed pass.",
        "claim_implications_seed": "Supports C03 by giving a concrete technical reason for program attention: RLVR safety, deception probes, and monitor-evasion failure modes.",
        "taxonomy_correction_suggestion": "keep",
        "final_report_use_suggestion": "headline_example",
        "reviewer_caveat": "Useful as a program-ahead-of-public example if the program/public divergence row confirms the signal pattern.",
    },
    {
        "event_id": "65886",
        "evidence_pages_checked": "p1; p2; p3; p5; p9",
        "paper_read_status_suggestion": "skimmed",
        "contribution_summary_seed": "Introduces reinforcement learning with evolving rubrics for long-form deep-research models, using search-grounded rubrics that co-evolve with the policy.",
        "novelty_judgment_suggestion": "new_method",
        "method_summary_seed": "Samples search-augmented rollouts, generates instance-specific rubrics from privileged information, scores responses, and updates both policy and rubric buffer.",
        "evidence_strength_suggestion": "strong",
        "baselines_checked_seed": "Compares DR Tulu-8B against open deep-research models and proprietary systems in reported tables.",
        "datasets_checked_seed": "SQAv2, DeepResearchBench, ResearchQA, and HealthBench.",
        "metrics_checked_seed": "Benchmark scores, average performance, and cost per query.",
        "limitations_seed": "Repository/artifact still needs inspection, and proprietary-system comparisons should be caveated by evaluation protocol differences.",
        "artifact_status_checked_suggestion": "linked_unchecked",
        "reproducibility_notes_seed": "GitHub URL is present in metadata but was not inspected in this seed pass.",
        "claim_implications_seed": "Supports C01 as a direct post-training/RL example for long-form research. Supports C08 because it links method, evaluation, and artifact gates.",
        "taxonomy_correction_suggestion": "keep",
        "final_report_use_suggestion": "headline_example",
        "reviewer_caveat": "Good headline example after artifact and benchmark protocol checks.",
    },
]


CLAIM_ROWS = [
    ("C01", "62989", "partial_support", "wrong_subarea", "linked_unchecked", "Central LLM memorization/capacity work, but not primarily reasoning/post-training; use as a boundary caveat for C01."),
    ("C08", "62989", "supports", "wrong_subarea", "linked_unchecked", "Validates the workflow need: high-signal paper has a subarea mismatch that would be missed by aggregate statistics."),
    ("C03", "66206", "supports", "correct", "not_applicable", "Rigorous grokking theory gives a concrete technical rationale for program attention beyond public votes."),
    ("C08", "66206", "supports", "correct", "not_applicable", "Useful theory-boundary check for the review workflow and safe-claim gates."),
    ("C01", "61998", "supports", "correct", "linked_unchecked", "Directly studies diffusion LMs, reasoning, and RL elicitation; supports C01 with a task-scope caveat."),
    ("C08", "61998", "supports", "correct", "linked_unchecked", "Shows why method-page review matters before making broad diffusion-LM claims."),
    ("C02", "65901", "partial_support", "too_broad", "linked_unchecked", "Efficient adaptation/post-training infrastructure is relevant, but not clearly an agentic-workload paper."),
    ("C06", "65901", "partial_support", "too_broad", "linked_unchecked", "Good guardrail for trend interpretation because the paper spans optimization, systems, and model behavior."),
    ("C01", "65332", "partial_support", "too_broad", "linked_unchecked", "Relevant to RL for code/math generation, but broader than LLM reasoning/post-training alone."),
    ("C08", "65332", "supports", "too_broad", "linked_unchecked", "Validates boundary-review workflow for RL/optimization papers assigned to LLM reasoning."),
    ("C02", "65206", "supports", "correct", "linked_unchecked", "Direct agentic workflow/system for automating a research-production task."),
    ("C07", "65206", "partial_support", "correct", "linked_unchecked", "Artifact visibility is plausible from metadata, but repository and benchmark contents are not yet inspected."),
    ("C03", "60766", "supports", "correct", "linked_unchecked", "Concrete RLVR safety/deception-probe contribution explains likely program attention."),
    ("C01", "65886", "supports", "correct", "linked_unchecked", "Direct post-training/RL method for long-form deep-research models with strong benchmark claims."),
    ("C08", "65886", "supports", "correct", "linked_unchecked", "Good workflow-validation row because evidence, benchmark protocol, and artifact checks all matter."),
]


AREA_ROWS = [
    ("62989", "LLM Reasoning, Post-Training, and RLVR", "partial", "analysis", "Transformer / attention; memorization measurement", "synthetic and real text sweeps", "synthetic bitstrings; real text", "memorization bits; bits per parameter; membership inference", "linked_unchecked", "scaling/measurement", "caveat", "Validate area broadly but correct subarea before using as diffusion-language-model evidence."),
    ("66206", "Theory, Optimization, and Algorithms", "yes", "theory", "ridge regression; gradient descent; weight decay", "teacher-student regression; non-linear network simulations", "synthetic regression", "grokking time; generalization error", "not_applicable", "proof/theory", "headline", "Strong theory/program-attention example."),
    ("61998", "LLM Reasoning, Post-Training, and RLVR", "yes", "method", "diffusion LMs; GRPO; autoregressive scaffold", "reasoning and coding tasks", "math/coding evaluations", "pass@k; reasoning accuracy", "linked_unchecked", "empirical method", "headline", "Clear LLM reasoning/post-training row, with caveat about task scope."),
    ("65901", "Systems and Efficient Foundation Models", "partial", "method", "random weight perturbation; efficient adaptation; ensembling", "LLM tasks and synthetic probes", "math; writing; programming; chemistry; Countdown; synthetic signals", "solution density; FLOP efficiency; accuracy", "linked_unchecked", "efficiency/optimization", "caveat", "Boundary row: efficient foundation-model adaptation more than systems infrastructure."),
    ("65332", "LLM Reasoning, Post-Training, and RLVR", "partial", "method", "maximum likelihood RL; sample-based objectives", "sampling-based binary outcome tasks", "navigation; code generation; math problem solving", "pass@k; likelihood approximation; Pareto efficiency", "linked_unchecked", "objective/method", "supporting", "Boundary row spanning RL optimization and LLM/code/math generation."),
    ("65206", "Agents, Code, and Tool Use", "yes", "system", "multi-agent illustration generation workflow", "PaperBananaBench and baseline comparisons", "292 NeurIPS 2025 methodology-diagram cases", "faithfulness; conciseness; readability; aesthetics", "linked_unchecked", "system/benchmark", "headline", "Strong agentic workflow example after repository/benchmark check."),
    ("60766", "Safety, Governance, Privacy, and Society", "yes", "analysis", "deception probes; RLVR; coding reward hacking", "detector penalties and KL-regularized RL runs", "coding reward-hacking environment", "probe score; representation change; task return", "linked_unchecked", "safety empirical analysis", "headline", "Strong safety/program-attention example."),
    ("65886", "LLM Reasoning, Post-Training, and RLVR", "yes", "method", "RL with evolving rubrics; search-augmented verification", "deep-research benchmark suite", "SQAv2; DeepResearchBench; ResearchQA; HealthBench", "benchmark scores; average performance; query cost", "linked_unchecked", "empirical method/system", "headline", "Strong LLM post-training example after artifact and protocol checks."),
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_paper_rows() -> list[dict[str, str]]:
    worksheet = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_pdf_review_worksheet.csv")}
    rows = []
    for seed in PAPER_ROWS:
        base = worksheet[seed["event_id"]]
        rows.append(
            {
                "event_id": seed["event_id"],
                "sprint": base["sprint"],
                "sprint_rank": base["sprint_rank"],
                "title": base["title"],
                "target_claims": base["target_claims"],
                "local_pdf_path": base["local_pdf_path"],
                "pdf_card_path": base["pdf_card_path"],
                "evidence_pages_checked": seed["evidence_pages_checked"],
                "paper_read_status_suggestion": seed["paper_read_status_suggestion"],
                "contribution_summary_seed": seed["contribution_summary_seed"],
                "novelty_judgment_suggestion": seed["novelty_judgment_suggestion"],
                "method_summary_seed": seed["method_summary_seed"],
                "evidence_strength_suggestion": seed["evidence_strength_suggestion"],
                "baselines_checked_seed": seed["baselines_checked_seed"],
                "datasets_checked_seed": seed["datasets_checked_seed"],
                "metrics_checked_seed": seed["metrics_checked_seed"],
                "limitations_seed": seed["limitations_seed"],
                "artifact_status_checked_suggestion": seed["artifact_status_checked_suggestion"],
                "reproducibility_notes_seed": seed["reproducibility_notes_seed"],
                "claim_implications_seed": seed["claim_implications_seed"],
                "taxonomy_correction_suggestion": seed["taxonomy_correction_suggestion"],
                "final_report_use_suggestion": seed["final_report_use_suggestion"],
                "reviewer_caveat": seed["reviewer_caveat"],
                "seed_status": "suggestion_only_not_manual_review",
            }
        )
    return sorted(rows, key=lambda row: int(row["sprint_rank"]))


def build_claim_rows() -> list[dict[str, str]]:
    worksheet = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_pdf_review_worksheet.csv")}
    rows = []
    for claim_id, event_id, support, taxonomy, artifact, notes in CLAIM_ROWS:
        base = worksheet[event_id]
        rows.append(
            {
                "claim_id": claim_id,
                "event_id": event_id,
                "title": base["title"],
                "manual_claim_support_suggestion": support,
                "manual_taxonomy_judgment_suggestion": taxonomy,
                "manual_artifact_judgment_suggestion": artifact,
                "manual_notes_seed": notes,
                "seed_status": "suggestion_only_not_manual_review",
            }
        )
    return rows


def build_area_rows() -> list[dict[str, str]]:
    worksheet = {row["event_id"]: row for row in read_csv(PROCESSED / "icml2026_pdf_review_worksheet.csv")}
    rows = []
    for (
        event_id,
        area,
        validated,
        contribution_type,
        method_family,
        benchmarks,
        datasets,
        metrics,
        artifact,
        result_character,
        fault_line,
        notes,
    ) in AREA_ROWS:
        base = worksheet[event_id]
        rows.append(
            {
                "area": area,
                "event_id": event_id,
                "title": base["title"],
                "manual_validated_suggestion": validated,
                "manual_primary_contribution_type_suggestion": contribution_type,
                "manual_method_family_seed": method_family,
                "manual_benchmarks_seed": benchmarks,
                "manual_datasets_seed": datasets,
                "manual_metrics_seed": metrics,
                "manual_artifact_status_suggestion": artifact,
                "manual_result_character_seed": result_character,
                "manual_fault_line_relevance_suggestion": fault_line,
                "manual_notes_seed": notes,
                "seed_status": "suggestion_only_not_manual_review",
            }
        )
    return rows


def write_report(paper_rows: list[dict[str, str]], claim_rows: list[dict[str, str]], area_rows: list[dict[str, str]]) -> None:
    claim_support_counts = {}
    for row in claim_rows:
        claim_support_counts[row["manual_claim_support_suggestion"]] = claim_support_counts.get(row["manual_claim_support_suggestion"], 0) + 1
    area_counts = {}
    for row in area_rows:
        area_counts[row["manual_validated_suggestion"]] = area_counts.get(row["manual_validated_suggestion"], 0) + 1

    lines = [
        "# ICML 2026 PDF Review Seed Judgments",
        "",
        "Conservative seed judgments for the bounded 8-paper PDF subset. These are generated suggestions from the cached PDFs and are not written into the canonical manual review overlays.",
        "",
        "## Snapshot",
        "",
        f"- Paper-note seed rows: {len(paper_rows)}",
        f"- Claim-overlay seed rows: {len(claim_rows)}",
        f"- Area-overlay seed rows: {len(area_rows)}",
        f"- Claim support suggestions: {claim_support_counts}",
        f"- Area validation suggestions: {area_counts}",
        "",
        "## How To Use",
        "",
        "1. Open the corresponding PDF review card and source PDF.",
        "2. Check the seed row against the cited pages.",
        "3. If the reviewer agrees, transfer only the coded values and concise notes into the manual paper-note, claim-overlay, and area-overlay CSVs.",
        "4. Run the post-transfer validation commands from the PDF transfer checklist.",
        "",
        "## Paper-Level Seeds",
        "",
        "| Rank | Paper | Claims | Evidence | Taxonomy | Report use | Caveat |",
        "| ---: | --- | --- | --- | --- | --- | --- |",
    ]
    for row in paper_rows:
        lines.append(
            f"| {row['sprint_rank']} | {row['title']} | {row['target_claims']} | "
            f"{row['evidence_strength_suggestion']} | {row['taxonomy_correction_suggestion']} | "
            f"{row['final_report_use_suggestion']} | {row['reviewer_caveat']} |"
        )

    lines.extend(["", "## Claim Seeds", "", "| Claim | Event | Support | Taxonomy | Artifact | Notes |", "| --- | --- | --- | --- | --- | --- |"])
    for row in claim_rows:
        lines.append(
            f"| {row['claim_id']} | {row['event_id']} | {row['manual_claim_support_suggestion']} | "
            f"{row['manual_taxonomy_judgment_suggestion']} | {row['manual_artifact_judgment_suggestion']} | {row['manual_notes_seed']} |"
        )

    lines.extend(["", "## Outputs", "", "- `data/processed/icml2026_pdf_review_seed_paper_notes.csv`", "- `data/processed/icml2026_pdf_review_seed_claim_overrides.csv`", "- `data/processed/icml2026_pdf_review_seed_area_overrides.csv`"])
    (REPORTS / "icml2026_pdf_review_seed_judgments.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    paper_rows = build_paper_rows()
    claim_rows = build_claim_rows()
    area_rows = build_area_rows()

    write_csv(PROCESSED / "icml2026_pdf_review_seed_paper_notes.csv", paper_rows, list(paper_rows[0].keys()))
    write_csv(PROCESSED / "icml2026_pdf_review_seed_claim_overrides.csv", claim_rows, list(claim_rows[0].keys()))
    write_csv(PROCESSED / "icml2026_pdf_review_seed_area_overrides.csv", area_rows, list(area_rows[0].keys()))
    write_report(paper_rows, claim_rows, area_rows)

    print(f"Wrote {PROCESSED / 'icml2026_pdf_review_seed_paper_notes.csv'} ({len(paper_rows)} rows)")
    print(f"Wrote {PROCESSED / 'icml2026_pdf_review_seed_claim_overrides.csv'} ({len(claim_rows)} rows)")
    print(f"Wrote {PROCESSED / 'icml2026_pdf_review_seed_area_overrides.csv'} ({len(area_rows)} rows)")
    print(f"Wrote {REPORTS / 'icml2026_pdf_review_seed_judgments.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
