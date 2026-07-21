# To Grok Grokking: Provable Grokking in Ridge Regression

- Sprint: `sprint_01` rank 2
- Global review rank: 2
- Event ID: `66206`
- Area: Theory, Optimization, and Algorithms / Statistical learning theory and regression
- Target claims: C03; C08
- Review phase: `main_thesis_claims`
- Note status: `not_started`
- Signals: oral; Outstanding Paper Honorable Mention; votes=7; taxonomy_review; evidence=low
- Links: [ICML](https://icml.cc/virtual/2026/poster/66206) / [AlphaXiv](https://www.alphaxiv.org/abs/2601.19791)

## Where To Record Judgments

- Claim overlay keys: C03::66206 | C08::66206
- Area overlay keys: Theory, Optimization, and Algorithms::66206
- Paper-note file: `data/manual/icml2026_review_sprint_01_paper_notes.csv`

## Local Context

- Claim packets: [claim packet 1](../claim_validation_packets/c03-program-committee-attention.md), [claim packet 2](../claim_validation_packets/c08-validation-priority.md)
- Claim dossiers: [claim dossier 1](../claim_evidence_dossiers/c03-program-committee-attention.md), [claim dossier 2](../claim_evidence_dossiers/c08-validation-priority.md)
- Area packet: [area packet](../validation_packets/theory-optimization-and-algorithms.md)
- Area briefing: [area briefing](../area_briefing_cards/theory-optimization-and-algorithms.md)

## What To Verify

- Contribution: Theory / proof: We study *grokking* - the onset of generalization long after overfitting - in a classical ridge regression setting.
- Method: Tags: no method-family tag; setting: theory/synthetic; abstract cues: gradient.
- Evidence: check theorem assumptions and empirical/theory split
- Taxonomy: Resolve whether the assigned area/subarea is truly the main contribution. Identify the technical reason for high program signal and whether public attention misses it. | Use high-signal papers to stress-test taxonomy boundaries.
- Claim implication: C03 (Program committee attention): decide supports / weakens / complicates / not_applicable. C08 (Validation priority): decide supports / weakens / complicates / not_applicable.
- Artifact: No obvious artifact link; record none/not_applicable unless PDF shows a release.
- Warning: Do not treat AlphaXiv attention as quality. Program signal is not the same as paper-level correctness. Heuristic evidence tag is low confidence. Taxonomy assignment may be unstable.

## Abstract Excerpt

We study *grokking* - the onset of generalization long after overfitting - in a classical ridge regression setting. We prove end-to-end grokking results for learning over-parameterized linear regression models using gradient descent with weight decay. Specifically, we prove that the following stages occur: (i) the model overfits the training data early during training; (ii) poor generalization persists long after overfitting has manifested; and (iii) the generalization error eventually becomes arbitrarily small. Moreover, we show, both theoretically and empirically, that grokking can be amplified or eliminated in a principled manner through proper hyperparameter tuning. To the best of...

## Suggested Note Seed

Contribution: Theory / proof: We study *grokking* - the onset of generalization long after overfitting - in a classical ridge regression setting. Evidence to verify: check theorem assumptions and empirical/theory split Claim implication: C03 (Program committee attention): decide supports / weakens / complicates / not_applicable. C08 (Validation priority): decide supports / weakens / complicates / not_applicable.

## Minimum Manual Fields

- `paper_read_status`
- `contribution_summary`
- `novelty_judgment`
- `method_summary`
- `evidence_strength`
- `baselines_checked`, `datasets_checked`, `metrics_checked`
- `limitations`
- `artifact_status_checked`
- `claim_implications`
- `taxonomy_correction`
- `final_report_use`