# ICML 2026 EDA Plan

## Questions

1. How large is ICML 2026 by public paper/event count, and how does that compare with earlier years?
2. Which research themes dominate titles and abstracts?
3. Which themes are overrepresented among award papers, oral papers, spotlight posters, and position papers?
4. Which papers receive unusually high public attention on AlphaXiv relative to official recognition?
5. How much of ICML 2026 appears to be LLM/agent/reasoning work versus traditional ML areas?
6. Which terms indicate emerging topics: diffusion language models, test-time adaptation, mechanistic interpretability, AI safety, reward models, data attribution, and AI for science?

## Data Layers

### Layer 1: Title Corpus

Fields:

- `event_id`
- `event_type`
- `title`
- `url`
- `is_position`
- keyword flags

Analyses:

- count by event type
- title n-grams
- keyword/topic buckets
- position paper share
- LLM / diffusion / RL / causal / privacy / federated / multimodal / AI-for-science shares

### Layer 2: Enriched ICML Event Metadata

Fields:

- authors
- abstract
- poster/session links
- oral/spotlight/award relationship
- schedule/session

Analyses:

- abstract topic modeling
- author/institution extraction if available
- award vs corpus topic comparison
- oral/spotlight topic mix

### Layer 3: AlphaXiv Community Signal

Fields:

- alphaxiv URL
- title
- arXiv ID
- vote count
- discussion/comment count
- rank/trending page
- snapshot date

Analyses:

- top-voted papers
- overlap with official awards
- attention outliers
- topic skew of public voting

## First EDA Outputs

- `reports/icml2026_title_eda.md`: title-level corpus statistics and trend notes.
- `reports/icml2026_awards_seed.md`: award paper summaries and analytical hooks.
- `data/processed/icml2026_topic_counts.csv`: topic bucket counts.
- `data/processed/icml2026_keyword_counts.csv`: frequent keyword counts.

## Presentation-Ready Later

Possible slide-ready charts once data is enriched:

- ICML 2026 paper corpus composition
- top title terms
- topic bucket distribution
- official award themes
- AlphaXiv top-voted vs ICML award overlap
- public attention outliers
