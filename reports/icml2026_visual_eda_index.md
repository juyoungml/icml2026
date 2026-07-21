# ICML 2026 Visual EDA Index

Static figures generated from processed CSVs. These are designed as report/presentation seed visuals, not final publication graphics.

## Figures

### topic_group_distribution.png

Official ICML topic-group balance across all 6,628 paper rows.

![topic_group_distribution.png](../figures/topic_group_distribution.png)

### theme_counts_orals.png

Rule-based cross-cutting theme counts with oral-designated counts overlaid.

![theme_counts_orals.png](../figures/theme_counts_orals.png)

### cluster_vote_density_oral_enrichment.png

Clusters ranked by AlphaXiv public votes per paper, with oral enrichment shown as a second axis.

![cluster_vote_density_oral_enrichment.png](../figures/cluster_vote_density_oral_enrichment.png)

### cluster_public_vs_program_signal.png

Cluster-level divergence between public attention and program-committee signal.

![cluster_public_vs_program_signal.png](../figures/cluster_public_vs_program_signal.png)

### alphaxiv_attention_distributions.png

Long-tailed AlphaXiv vote and recent-visit distributions.

![alphaxiv_attention_distributions.png](../figures/alphaxiv_attention_distributions.png)

### top_canonical_institutions.png

Top canonical institutions after alias cleanup.

![top_canonical_institutions.png](../figures/top_canonical_institutions.png)

### sector_mix_papers.png

Paper-level sector mixes from canonical institution sectors.

![sector_mix_papers.png](../figures/sector_mix_papers.png)

### institution_collaboration_hubs.png

Institution collaboration hubs by paper co-occurrence PageRank.

![institution_collaboration_hubs.png](../figures/institution_collaboration_hubs.png)

### team_size_distribution.png

Distribution of author counts per ICML paper.

![team_size_distribution.png](../figures/team_size_distribution.png)

### semantic_cluster_map.png

Transformer embedding map of the ICML corpus, projected to two PCA dimensions and labeled by the largest semantic clusters.

![semantic_cluster_map.png](../figures/semantic_cluster_map.png)

### semantic_cluster_vote_density.png

Semantic clusters ranked by AlphaXiv public votes per paper, with oral enrichment shown as a second axis.

![semantic_cluster_vote_density.png](../figures/semantic_cluster_vote_density.png)

### manual_taxonomy_area_sizes.png

Curated report-level taxonomy area sizes, with GitHub URL share shown as a reproducibility proxy.

![manual_taxonomy_area_sizes.png](../figures/manual_taxonomy_area_sizes.png)

### evidence_contribution_mix.png

Heuristic primary contribution-type mix across curated taxonomy areas.

![evidence_contribution_mix.png](../figures/evidence_contribution_mix.png)

### program_signal_calibration.png

Oral-selection enrichment compared with AlphaXiv public-attention enrichment across taxonomy areas.

![program_signal_calibration.png](../figures/program_signal_calibration.png)

### arxiv_taxonomy_trends.png

Coarse arXiv query-count growth by taxonomy area, compared with ICML 2026 taxonomy share.

![arxiv_taxonomy_trends.png](../figures/arxiv_taxonomy_trends.png)

### historical_venue_area_deltas.png

ICML 2026 area-share deltas against accepted-paper baselines from ICML 2025, NeurIPS 2025, and ICLR 2026.

![historical_venue_area_deltas.png](../figures/historical_venue_area_deltas.png)

## Caveats

- Theme labels are rule-based and intentionally broad.
- Cluster labels come from TF-IDF terms, not manual semantic names.
- Semantic-map coordinates are a 2D PCA projection of transformer embeddings, so local neighborhoods are more meaningful than precise axis positions.
- Manual taxonomy areas are curated seed labels over semantic clusters, not a final ontology.
- Evidence contribution mixes are keyword/regex-derived triage labels, not verified paper annotations.
- Program-signal enrichment uses oral/award labels as conference-program signals, not complete quality labels.
- arXiv trend counts are broad overlapping query counts, not prior-conference acceptance trends.
- Historical venue deltas use a shared keyword scorer over accepted-paper metadata, with weaker title/topic-only coverage for venues whose static abstracts were unavailable.
- AlphaXiv metrics are public-attention signals, not quality labels.
- Institution and author figures inherit the canonicalization and name-disambiguation caveats in the collaboration report.