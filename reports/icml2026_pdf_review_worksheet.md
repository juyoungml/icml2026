# ICML 2026 PDF Review Worksheet

Reviewer-ready worksheet for the bounded PDF subset. It joins source links, page-level navigation, claim decision tests, and blank paper-note fields.

This is not a completed review. Blank judgment fields are intentional and should be filled after reading the PDF pages.

## Snapshot

- Worksheet rows: 8
- Claims covered: 6
- Rows with artifact checks: 7

## Review Order

1. Open the PDF review card.
2. Read method pages, then evidence pages, then limitation pages.
3. Inspect artifact pages and repository when applicable.
4. Fill the blank judgment fields in the worksheet or the canonical paper-note file.
5. Transfer claim and taxonomy judgments through the overlay bridge.

## Worksheet Rows

| Sprint | Rank | Paper | Claims | Pages | Writeback |
| --- | ---: | --- | --- | --- | --- |
| sprint_01 | 1 | [How much can language models memorize?](pdf_review_cards/62989.md) | C01; C08 | method p1; p2; p3; evidence p1; p2; p3; limitations p12; p20 | `data/manual/icml2026_review_sprint_01_paper_notes.csv` |
| sprint_01 | 2 | [To Grok Grokking: Provable Grokking in Ridge Regression](pdf_review_cards/66206.md) | C03; C08 | method p1; p2; p3; evidence p1; p2; p3; limitations p8 | `data/manual/icml2026_review_sprint_01_paper_notes.csv` |
| sprint_01 | 3 | [The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models](pdf_review_cards/61998.md) | C01; C08 | method p1; p2; p3; evidence p2; p3; p4; limitations p12 | `data/manual/icml2026_review_sprint_01_paper_notes.csv` |
| sprint_01 | 4 | [Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights](pdf_review_cards/65901.md) | C02; C06 | method p1; p2; p6; evidence p1; p2; p3; limitations p14 | `data/manual/icml2026_review_sprint_01_paper_notes.csv` |
| sprint_01 | 5 | [Maximum Likelihood Reinforcement Learning](pdf_review_cards/65332.md) | C01; C08 | method p1; p2; p4; evidence p1; p2; p5; limitations p12; p13; p36 | `data/manual/icml2026_review_sprint_01_paper_notes.csv` |
| sprint_01 | 6 | [PaperBanana: Automating Academic Illustration for AI Scientists](pdf_review_cards/65206.md) | C02; C07 | method p1; p2; p3; evidence p1; p2; p3; limitations p10; p11; p12 | `data/manual/icml2026_review_sprint_01_paper_notes.csv` |
| sprint_01 | 7 | [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](pdf_review_cards/60766.md) | C03 | method p1; p3; p4; evidence p4; p5; p6; limitations p9 | `data/manual/icml2026_review_sprint_01_paper_notes.csv` |
| sprint_01 | 10 | [Reinforcement Learning with Evolving Rubrics for Deep Research](pdf_review_cards/65886.md) | C01; C08 | method p2; p3; p5; evidence p1; p2; p3; limitations p2; p9; p11 | `data/manual/icml2026_review_sprint_01_paper_notes.csv` |

## Coded Values

Use `reports/icml2026_manual_review_codebook.md` for allowed values. Do not invent coded values in `paper_read_status`, `novelty_judgment`, `evidence_strength`, `artifact_status_checked`, `taxonomy_correction`, or `final_report_use`.

## Outputs

- `data/processed/icml2026_pdf_review_worksheet.csv`
- `reports/icml2026_pdf_review_worksheet.md`