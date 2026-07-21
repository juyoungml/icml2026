# ICML 2026 PDF Review Seed Judgments

Conservative seed judgments for the bounded 8-paper PDF subset. These are generated suggestions from the cached PDFs and are not written into the canonical manual review overlays.

## Snapshot

- Paper-note seed rows: 8
- Claim-overlay seed rows: 15
- Area-overlay seed rows: 8
- Claim support suggestions: {'partial_support': 5, 'supports': 10}
- Area validation suggestions: {'partial': 3, 'yes': 5}

## How To Use

1. Open the corresponding PDF review card and source PDF.
2. Check the seed row against the cited pages.
3. If the reviewer agrees, transfer only the coded values and concise notes into the manual paper-note, claim-overlay, and area-overlay CSVs.
4. Run the post-transfer validation commands from the PDF transfer checklist.

## Paper-Level Seeds

| Rank | Paper | Claims | Evidence | Taxonomy | Report use | Caveat |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | How much can language models memorize? | C01; C08 | strong | relabel_subarea | caveat_example | Use as a boundary example unless a reviewer broadens C01 beyond reasoning/post-training. |
| 2 | To Grok Grokking: Provable Grokking in Ridge Regression | C03; C08 | strong | keep | headline_example | Use for program-signal calibration, not as evidence of empirical trend size. |
| 3 | The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models | C01; C08 | moderate | keep | headline_example | Promote only with a caveat that the finding is about eliciting reasoning in dLLMs, not a universal rejection of arbitrary-order generation. |
| 4 | Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights | C02; C06 | moderate | split_boundary | caveat_example | Good example of taxonomy ambiguity between efficient foundation models, optimization, and post-training. |
| 5 | Maximum Likelihood Reinforcement Learning | C01; C08 | moderate | split_boundary | supporting_example | Do not use as a pure LLM post-training headline without checking experiments and artifact. |
| 6 | PaperBanana: Automating Academic Illustration for AI Scientists | C02; C07 | moderate | keep | headline_example | Strong landscape example for AI-scientist workflow automation, but artifact claim remains unchecked. |
| 7 | The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | C03 | strong | keep | headline_example | Useful as a program-ahead-of-public example if the program/public divergence row confirms the signal pattern. |
| 10 | Reinforcement Learning with Evolving Rubrics for Deep Research | C01; C08 | strong | keep | headline_example | Good headline example after artifact and benchmark protocol checks. |

## Claim Seeds

| Claim | Event | Support | Taxonomy | Artifact | Notes |
| --- | --- | --- | --- | --- | --- |
| C01 | 62989 | partial_support | wrong_subarea | linked_unchecked | Central LLM memorization/capacity work, but not primarily reasoning/post-training; use as a boundary caveat for C01. |
| C08 | 62989 | supports | wrong_subarea | linked_unchecked | Validates the workflow need: high-signal paper has a subarea mismatch that would be missed by aggregate statistics. |
| C03 | 66206 | supports | correct | not_applicable | Rigorous grokking theory gives a concrete technical rationale for program attention beyond public votes. |
| C08 | 66206 | supports | correct | not_applicable | Useful theory-boundary check for the review workflow and safe-claim gates. |
| C01 | 61998 | supports | correct | linked_unchecked | Directly studies diffusion LMs, reasoning, and RL elicitation; supports C01 with a task-scope caveat. |
| C08 | 61998 | supports | correct | linked_unchecked | Shows why method-page review matters before making broad diffusion-LM claims. |
| C02 | 65901 | partial_support | too_broad | linked_unchecked | Efficient adaptation/post-training infrastructure is relevant, but not clearly an agentic-workload paper. |
| C06 | 65901 | partial_support | too_broad | linked_unchecked | Good guardrail for trend interpretation because the paper spans optimization, systems, and model behavior. |
| C01 | 65332 | partial_support | too_broad | linked_unchecked | Relevant to RL for code/math generation, but broader than LLM reasoning/post-training alone. |
| C08 | 65332 | supports | too_broad | linked_unchecked | Validates boundary-review workflow for RL/optimization papers assigned to LLM reasoning. |
| C02 | 65206 | supports | correct | linked_unchecked | Direct agentic workflow/system for automating a research-production task. |
| C07 | 65206 | partial_support | correct | linked_unchecked | Artifact visibility is plausible from metadata, but repository and benchmark contents are not yet inspected. |
| C03 | 60766 | supports | correct | linked_unchecked | Concrete RLVR safety/deception-probe contribution explains likely program attention. |
| C01 | 65886 | supports | correct | linked_unchecked | Direct post-training/RL method for long-form deep-research models with strong benchmark claims. |
| C08 | 65886 | supports | correct | linked_unchecked | Good workflow-validation row because evidence, benchmark protocol, and artifact checks all matter. |

## Outputs

- `data/processed/icml2026_pdf_review_seed_paper_notes.csv`
- `data/processed/icml2026_pdf_review_seed_claim_overrides.csv`
- `data/processed/icml2026_pdf_review_seed_area_overrides.csv`