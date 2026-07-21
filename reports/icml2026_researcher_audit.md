# ICML 2026 Researcher Audit

## What Is Solid Now

- Official corpus coverage is strong: 6,628 ICML paper rows and 168 oral-designated papers from the ICML virtual bulk metadata.
- AlphaXiv coverage is now complete for the snapshot: 6,628 community-signal rows joined to 6,628 official ICML rows.
- The project has three useful lenses: official topic distribution, AlphaXiv public-attention signals, and rule-based cross-cutting research themes.
- Institution analysis is much better than raw strings because common university, lab, and company aliases are canonicalized.
- The new theme reading map is the most useful researcher entry point: it gives a ranked triage list per area instead of one global popularity list.
- The unsupervised cluster landscape gives a second opinion against the rule-based theme map and surfaces program-vs-public-attention divergences.
- The semantic cluster landscape now adds transformer embeddings over titles/topics/abstracts, plus overlap metrics against the lexical TF-IDF/SVD baseline.
- The manual taxonomy seed turns 42 semantic clusters into 12 report-level areas, with review flags for unstable or lower-confidence clusters.
- The paper evidence coding layer now tags all 6,628 papers with heuristic contribution type, method-family, evaluation-setting, benchmark/dataset/metric cues, artifact state, and confidence.
- The area fault-line report now gives each curated area a headline, evidence bullets, contested assumptions, reading questions, representative papers, public-only candidates, and program-signal candidates.
- The manual validation queue now selects 192 papers, 16 per taxonomy area, spanning representative, public-only, program-only, boundary-cluster, and low-confidence evidence-code cases.
- The validation packet layer turns the 192-paper queue into area-specific markdown worksheets with abstracts, heuristic tags, links, and validation checklists.
- The program-signal calibration layer now quantifies taxonomy-area and semantic-cluster oral/award enrichment versus corpus share and AlphaXiv public-attention enrichment.
- The fault-lines seed starts converting EDA into research interpretation: reasoning/RL vs test-time compute, diffusion splits, agent evaluation, efficiency, safety/position papers, and science/theory visibility.
- The collaboration landscape adds author-name productivity, coauthorship edges, institution collaboration hubs, sector mixes, and high-signal industry-academia papers.
- The visual EDA layer now provides repeatable PNGs for topic balance, theme/oral mix, cluster signal calibration, AlphaXiv attention, institutions, sectors, collaboration hubs, and team sizes.
- Audience-specific reading paths now cover LLM reasoning, RL, agents, systems, diffusion, multimodal/robotics, safety/alignment, theory, AI-for-science, and executive overview readers.
- The reproducibility/artifact lens now estimates GitHub URL availability across the corpus, audience paths, and clusters, with a manual-check flag for likely template, homepage, and index repositories.
- The optional GitHub live artifact validator now checks bounded high-signal repositories for API liveness, stars, license metadata, archive/fork/disabled status, pushed timestamps, and suspicious template/index patterns.
- The arXiv trend baseline now provides cached 2024, 2025, and 2026-YTD query-count context for the 12 taxonomy areas.
- The historical accepted-paper baseline now compares ICML 2026 against ICML 2025, NeurIPS 2025, and ICLR 2026 using a shared keyword scorer over accepted virtual-site metadata.
- The landscape synthesis layer now provides a researcher-facing signal matrix and claim register that separates strong landscape claims from hypotheses requiring manual validation.
- The claim validation layer now turns the synthesis claims into 118 paper-level review rows and 8 claim-specific validation packets.

## Critical Gaps

- Theme labels are still heuristic. They are good enough for exploration, but too brittle for publication claims because broad keywords can over-label papers across unrelated areas.
- The manual taxonomy is still a seed. It provides cleaner report-level names, but 21 of 42 semantic clusters are explicitly marked as needing review.
- The composite reading score is transparent but hand-tuned. It mixes awards, oral status, votes, visits, and GitHub stars without validation.
- AlphaXiv is an attention proxy, not a quality proxy. It likely overweights LLM, RL, agents, and social-sharing dynamics.
- Institution counts are paper-level affiliation mentions, not contribution-weighted authorship. Multi-institution papers inflate every participating institution equally.
- Author-name analysis is not identity-disambiguated. Common names can merge multiple people, and spelling variants can split the same person.
- The accepted-paper delta layer exists now, but it is still a first-pass keyword baseline. It should be strengthened with abstracts where available, topic-specific manual review, and possibly a semantic classifier trained on the ICML 2026 taxonomy.
- The landscape synthesis is only as reliable as its upstream heuristic layers. It should be treated as a navigation and prioritization artifact, not a final paper without manual review.
- The claim validation packets make checking easier, but their manual fields are still blank. They do not yet prove or revise the synthesis claims.
- The area fault-line report now uses evidence-code summaries, but the evidence codes are heuristic and still need manual validation before publication-grade claims about benchmarks, datasets, metrics, and negative results.
- The manual validation queue has blank human-review fields; it organizes the work but does not itself validate the claims.
- Validation packets make review easier, but edits in packet checkboxes are not automatically reconciled into the CSV evidence table.
- GitHub artifact signals are only partially live-verified. The optional validator checks repository API metadata for a bounded set, but it does not clone repos, inspect code, identify dataset/checkpoint releases, or confirm runnable reproduction paths.
- The figures are report seeds, not final design assets. Cluster labels still need manual naming before slide use.

## What A ML Researcher Would Want Next

1. Review and refine the 21 `needs_review` taxonomy clusters, especially medium-confidence LLM, systems, data-centric, and AI-for-science boundaries.
2. Refine the historical delta view: add more abstracts, inspect the largest ICML 2026 over/underweights manually, and separate topic-label artifacts from real venue emphasis.
3. Fill the validation packets/manual queue for the 192 selected papers, then reconcile reviewed fields back into a checked CSV.
4. Community-vs-program-committee divergence follow-up: manually review papers high on AlphaXiv but not oral/award, and oral/award papers with low public attention.
5. Better institution QA: canonicalize long-tail labs, split company subsidiaries where needed, and add country/region normalization.
6. Stronger author/network QA: author identity disambiguation, cleaner long-tail institution aliases, lab-level grouping, and region/country normalization.
7. Deeper artifact QA: clone/check high-signal repositories, inspect README/license/data/checkpoint links, verify benchmark releases, and determine whether reproduction instructions actually run.
8. Manual editing of generated reading paths into a final syllabus/narrative with human-written transitions and exclusions.
9. Presentation-grade figure refinement: manual cluster names, consistent visual style, and hand-written captions tied to the main claims.
10. Extend historical comparison beyond one-year neighbors: ICML 2024/2025/2026, NeurIPS 2024/2025, ICLR 2025/2026, plus a manually reviewed taxonomy bridge.

## Best Immediate Next Step

Fill the validation packets, then reconcile reviewed fields back into a checked CSV. The next quality jump is to convert the 192 selected papers from heuristic evidence rows into trusted paper-level claims.
