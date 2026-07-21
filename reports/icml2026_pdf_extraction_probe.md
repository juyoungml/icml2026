# ICML 2026 PDF Extraction Probe

Bounded source-extraction probe for prioritized sprint papers with arXiv PDF URLs.

This is not a paper review and does not promote any claim. It checks whether the workflow can obtain PDFs and extract enough structure to support manual review.

## Snapshot

- Probe rows: 8
- Download statuses: cached=8
- Extraction statuses: ok=8
- Extracted text rows: 8

## Probed Papers

| Sprint | Rank | Paper | Claims | Download | Pages | Sections | Evidence cues |
| --- | ---: | --- | --- | --- | ---: | --- | --- |
| sprint_01 | 1 | How much can language models memorize? | C01; C08 | cached / ok | 21 | introduction; method; experiment; result; conclusion | baseline=0; ablation=0; dataset=21; metric=0; limitation=0; theorem=1; artifact=0 |
| sprint_01 | 2 | To Grok Grokking: Provable Grokking in Ridge Regression | C03; C08 | cached / ok | 23 | introduction; related_work; method; experiment; result; conclusion | baseline=0; ablation=0; dataset=3; metric=1; limitation=0; theorem=8; artifact=0 |
| sprint_01 | 3 | The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models | C01; C08 | cached / ok | 19 | introduction; method; result | baseline=1; ablation=0; dataset=0; metric=15; limitation=0; theorem=0; artifact=1 |
| sprint_01 | 4 | Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights | C02; C06 | cached / ok | 30 | introduction; method; experiment; result | baseline=3; ablation=0; dataset=0; metric=9; limitation=0; theorem=1; artifact=3 |
| sprint_01 | 5 | Maximum Likelihood Reinforcement Learning | C01; C08 | cached / ok | 44 | introduction; method; result | baseline=0; ablation=0; dataset=0; metric=6; limitation=0; theorem=0; artifact=3 |
| sprint_01 | 6 | PaperBanana: Automating Academic Illustration for AI Scientists | C02; C07 | cached / ok | 49 | introduction; method; experiment | baseline=3; ablation=0; dataset=0; metric=0; limitation=0; theorem=0; artifact=4 |
| sprint_01 | 7 | The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | C03 | cached / ok | 30 | introduction; related_work; method; experiment; result | baseline=0; ablation=0; dataset=5; metric=2; limitation=0; theorem=0; artifact=8 |
| sprint_01 | 10 | Reinforcement Learning with Evolving Rubrics for Deep Research | C01; C08 | cached / ok | 56 | introduction; method; experiment; result; ablation | baseline=1; ablation=1; dataset=5; metric=1; limitation=0; theorem=0; artifact=4 |

## Use

Use this as a source-readiness check only. Actual judgments still belong in the sprint paper-note CSVs and manual overlay files.

## Outputs

- `data/processed/icml2026_pdf_extraction_probe.csv`
- `reports/icml2026_pdf_extraction_probe.md`
- `data/raw/pdf_probe/*.pdf` for cached probe PDFs