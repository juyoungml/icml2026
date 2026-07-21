#!/usr/bin/env python3
"""Build a self-contained static HTML dashboard for the ICML 2026 workspace."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
DOCS = ROOT / "docs"


FIGURES = [
    ("Area Sizes", "../figures/manual_taxonomy_area_sizes.png", "Curated taxonomy area sizes and GitHub URL share."),
    ("Program vs Public", "../figures/program_signal_calibration.png", "Oral enrichment compared with public-attention enrichment."),
    ("Historical Deltas", "../figures/historical_venue_area_deltas.png", "ICML 2026 area-share deltas versus neighboring venues."),
    ("arXiv Trends", "../figures/arxiv_taxonomy_trends.png", "Broad arXiv query growth by taxonomy area."),
    ("Semantic Map", "../figures/semantic_cluster_map.png", "Transformer embedding map of the corpus."),
    ("Evidence Mix", "../figures/evidence_contribution_mix.png", "Heuristic contribution-type mix by area."),
]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"Missing required input: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def fnum(value: str) -> float:
    try:
        return float(value or 0)
    except ValueError:
        return 0.0


def inum(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def pct(value: str) -> str:
    return f"{fnum(value) * 100:.1f}%"


def compact_queue_rows(rows: list[dict[str, str]], limit: int = 36) -> list[dict[str, str]]:
    selected = []
    for row in rows[:limit]:
        selected.append(
            {
                "claim_id": row["claim_id"],
                "rank": row["claim_review_rank"],
                "title": row["title"],
                "area": row["area"],
                "reason": row["selection_reason"],
                "focus": row["review_focus"],
                "oral": row["is_oral"],
                "award": row["award"],
                "votes": row["public_total_votes"],
                "cluster": row["semantic_cluster_id"],
                "review_status": row["review_status"],
                "url": row["url"],
                "alphaxiv_url": row["alphaxiv_url"],
            }
        )
    return selected


def compact_paper_rows(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    selected = []
    for row in rows:
        selected.append(
            {
                "event_id": row["event_id"],
                "title": row["title"],
                "area": row["area"],
                "subarea": row["subarea"],
                "cluster": row["semantic_cluster_id"],
                "topic_group": row["topic_group"],
                "oral": row["is_oral"],
                "award": row["award"],
                "votes": inum(row["public_total_votes"]),
                "visits": inum(row["visits_last_7_days"]),
                "github": row["github_url"],
                "github_stars": inum(row["github_stars"]),
                "review_status": row["review_status"],
                "contribution": row["primary_contribution_type"],
                "methods": row["method_families"],
                "eval": row["evaluation_settings"],
                "score": inum(row["signal_score"]),
                "url": row["url"],
                "alphaxiv_url": row["alphaxiv_url"],
            }
        )
    return selected


def build_payload() -> dict[str, object]:
    papers = read_csv(PROCESSED / "icml2026_papers.csv")
    paper_explorer = read_csv(PROCESSED / "icml2026_paper_explorer.csv")
    areas = read_csv(PROCESSED / "icml2026_landscape_signal_matrix.csv")
    claims = read_csv(PROCESSED / "icml2026_landscape_claim_register.csv")
    queue = read_csv(PROCESSED / "icml2026_claim_validation_queue.csv")
    review_progress = read_csv(PROCESSED / "manual_review_progress.csv")
    checks = read_csv(PROCESSED / "workspace_validation_checks.csv")
    pdf_probe = read_csv(PROCESSED / "icml2026_pdf_extraction_probe.csv")
    pdf_cards = read_csv(PROCESSED / "icml2026_pdf_review_cards.csv")
    pdf_worksheet = read_csv(PROCESSED / "icml2026_pdf_review_worksheet.csv")
    pdf_transfer = read_csv(PROCESSED / "icml2026_pdf_review_transfer_checklist.csv")

    total_votes = sum(inum(row.get("public_total_votes", "")) for row in areas)
    validation_failures = sum(row["status"] != "pass" for row in checks)
    review_total = sum(inum(row["review_rows"]) for row in review_progress)
    review_done = sum(inum(row["reviewed_rows"]) for row in review_progress)
    top_area = max(areas, key=lambda row: fnum(row["taxonomy_share"]))
    top_public = max(areas, key=lambda row: fnum(row["public_attention_enrichment"]))
    top_program = max(areas, key=lambda row: fnum(row["oral_enrichment"]))

    clean_areas = []
    for row in areas:
        clean_areas.append(
            {
                **row,
                "taxonomy_share_fmt": pct(row["taxonomy_share"]),
                "historical_delta_fmt": f"{fnum(row['historical_delta_vs_baseline']) * 100:+.1f} pp",
                "arxiv_growth_fmt": pct(row["arxiv_2025_vs_2024_growth"]),
                "github_share_fmt": pct(row["github_url_share"]),
                "tags": [part.strip() for part in row["signal_tags"].split(";") if part.strip()],
            }
        )
    bounded_claims = sorted(
        {
            claim_id
            for row in pdf_worksheet
            for claim_id in [part.strip() for part in row.get("target_claims", "").split(";") if part.strip()]
        }
    )

    return {
        "kpis": {
            "papers": len(papers),
            "areas": len(areas),
            "claims": len(claims),
            "claimQueueRows": len(queue),
            "reviewRows": review_total,
            "reviewedRows": review_done,
            "validationFailures": validation_failures,
            "totalAreaVotes": total_votes,
            "topArea": top_area["area"],
            "topPublic": top_public["area"],
            "topProgram": top_program["area"],
        },
        "areas": clean_areas,
        "papers": compact_paper_rows(paper_explorer),
        "claims": claims,
        "reviewProgress": review_progress,
        "boundedReview": {
            "pdfs": len(pdf_probe),
            "extractablePdfs": sum(row.get("extract_status") == "ok" for row in pdf_probe),
            "cards": len(pdf_cards),
            "worksheetRows": len(pdf_worksheet),
            "transferRows": len(pdf_transfer),
            "claims": bounded_claims,
        },
        "queue": compact_queue_rows(queue),
        "figures": [{"title": title, "src": src, "description": desc} for title, src, desc in FIGURES],
        "links": {
            "projectIndex": "project_index.md",
            "newcomerRoadmap": "icml2026_newcomer_roadmap.md",
            "newcomerSlides": "icml2026_newcomer_slides.html",
            "overviewSeed": "../reports/icml2026_overview_report_seed.md",
            "landscapeSynthesis": "../reports/icml2026_landscape_synthesis.md",
            "areaBriefings": "../reports/icml2026_area_briefing_card_index.md",
            "claimPackets": "../reports/icml2026_claim_validation_packet_index.md",
            "claimDossiers": "../reports/icml2026_claim_evidence_dossier_index.md",
            "reviewPlan": "../reports/icml2026_researcher_review_plan.md",
            "reviewSprint": "../reports/icml2026_review_sprint_01.md",
            "reviewDecisionTasks": "../reports/icml2026_review_decision_tasks.md",
            "manualReviewWorkspace": "../reports/manual_review_workspace.md",
            "paperSourceAccess": "../reports/icml2026_paper_source_access_map.md",
            "pdfExtractionProbe": "../reports/icml2026_pdf_extraction_probe.md",
            "pdfReviewCards": "../reports/icml2026_pdf_review_cards.md",
            "pdfReviewWorksheet": "../reports/icml2026_pdf_review_worksheet.md",
            "pdfReviewTransfer": "../reports/icml2026_pdf_review_transfer_checklist.md",
            "readinessAudit": "../reports/icml2026_researcher_readiness_audit.md",
            "reviewProgress": "../reports/manual_review_progress.md",
            "validation": "../reports/workspace_validation.md",
            "dataDictionary": "data_dictionary.md",
        },
    }


def render_html(payload: dict[str, object]) -> str:
    payload_json = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>ICML 2026 Landscape Dashboard</title>
  <style>
    :root {{
      --bg: #f7f8fb;
      --panel: #ffffff;
      --text: #1f2933;
      --muted: #5f6b7a;
      --line: #d8dee8;
      --blue: #2f6f9f;
      --green: #3d8067;
      --red: #b44d4d;
      --amber: #b9792c;
      --ink: #111827;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif;
      color: var(--text);
      background: var(--bg);
      line-height: 1.45;
    }}
    header {{
      padding: 24px 28px 16px;
      background: var(--panel);
      border-bottom: 1px solid var(--line);
      position: sticky;
      top: 0;
      z-index: 5;
    }}
    h1 {{
      margin: 0 0 6px;
      font-size: 24px;
      letter-spacing: 0;
    }}
    .subtitle {{
      margin: 0;
      color: var(--muted);
      max-width: 980px;
      font-size: 14px;
    }}
    nav {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-top: 14px;
    }}
    nav a, .link-button {{
      border: 1px solid var(--line);
      background: #f9fafc;
      color: var(--text);
      padding: 7px 10px;
      text-decoration: none;
      border-radius: 6px;
      font-size: 13px;
    }}
    main {{ padding: 20px 28px 36px; }}
    section {{ margin: 0 auto 24px; max-width: 1280px; }}
    h2 {{ margin: 0 0 12px; font-size: 18px; }}
    .kpis {{
      display: grid;
      grid-template-columns: repeat(5, minmax(130px, 1fr));
      gap: 10px;
    }}
    .kpi, .panel, .claim, .figure-card, .callout {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
    }}
    .kpi {{ padding: 14px; min-height: 86px; }}
    .kpi .value {{ font-size: 24px; font-weight: 700; color: var(--ink); }}
    .kpi .label {{ color: var(--muted); font-size: 12px; margin-top: 4px; }}
    .toolbar {{
      display: flex;
      gap: 10px;
      align-items: center;
      margin-bottom: 10px;
      flex-wrap: wrap;
    }}
    input, select {{
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 8px 10px;
      min-height: 36px;
      background: var(--panel);
      color: var(--text);
      font-size: 14px;
    }}
    input {{ min-width: 260px; }}
    table {{
      width: 100%;
      border-collapse: collapse;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      overflow: hidden;
    }}
    th, td {{
      padding: 9px 10px;
      border-bottom: 1px solid var(--line);
      text-align: left;
      vertical-align: top;
      font-size: 13px;
    }}
    th {{
      background: #eef2f7;
      color: var(--ink);
      cursor: pointer;
      white-space: nowrap;
    }}
    tr:last-child td {{ border-bottom: 0; }}
    .tag {{
      display: inline-block;
      border: 1px solid #cbd5e1;
      background: #f8fafc;
      border-radius: 999px;
      padding: 2px 7px;
      margin: 1px 2px 1px 0;
      font-size: 11px;
      color: #334155;
      white-space: nowrap;
    }}
    .claims-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(280px, 1fr));
      gap: 12px;
    }}
    .claim {{ padding: 14px; }}
    .claim h3 {{ margin: 0 0 6px; font-size: 15px; }}
    .claim p {{ margin: 6px 0; font-size: 13px; }}
    .strength {{ color: var(--blue); font-weight: 700; }}
    .figures {{
      display: grid;
      grid-template-columns: repeat(2, minmax(300px, 1fr));
      gap: 14px;
    }}
    .figure-card {{ padding: 12px; }}
    .figure-card h3 {{ margin: 0 0 6px; font-size: 15px; }}
    .figure-card img {{
      width: 100%;
      height: auto;
      display: block;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: white;
    }}
    .figure-card p {{ color: var(--muted); font-size: 13px; }}
    .queue-list {{
      display: grid;
      grid-template-columns: repeat(3, minmax(240px, 1fr));
      gap: 10px;
    }}
    .queue-item {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
      min-height: 150px;
    }}
    .queue-item h3 {{ margin: 0 0 6px; font-size: 14px; }}
    .queue-item p {{ margin: 5px 0; color: var(--muted); font-size: 12px; }}
    .small-links {{ display: flex; gap: 8px; flex-wrap: wrap; margin-top: 8px; }}
    .small-links a {{ color: var(--blue); font-size: 12px; }}
    .callout {{ padding: 14px; margin-bottom: 12px; font-size: 13px; }}
    .callout .subtitle {{ margin-top: 8px; }}
    footer {{
      max-width: 1280px;
      margin: 16px auto 0;
      color: var(--muted);
      font-size: 12px;
    }}
    @media (max-width: 900px) {{
      header, main {{ padding-left: 16px; padding-right: 16px; }}
      .kpis {{ grid-template-columns: repeat(2, minmax(130px, 1fr)); }}
      .claims-grid, .figures, .queue-list {{ grid-template-columns: 1fr; }}
      table {{ display: block; overflow-x: auto; }}
      input {{ min-width: 100%; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>ICML 2026 Landscape Dashboard</h1>
    <p class=\"subtitle\">Static explorer for the ICML 2026 EDA workspace. Signals are navigation aids, not final publication claims; use the validation packets before asserting subarea-level conclusions.</p>
    <nav>
      <a id=\"newcomerLink\" href=\"#\">Newcomer Roadmap</a>
      <a id=\"newcomerSlidesLink\" href=\"#\">Newcomer Slides</a>
      <a href=\"#areas\">Areas</a>
      <a href=\"#claims\">Claims</a>
      <a href=\"#papers\">Papers</a>
      <a href=\"#review\">Review</a>
      <a href=\"#figures\">Figures</a>
      <a href=\"#validation\">Validation Queue</a>
      <a id=\"projectLink\" href=\"#\">Project Index</a>
      <a id=\"overviewLink\" href=\"#\">Report Seed</a>
      <a id=\"areaBriefingLink\" href=\"#\">Area Briefs</a>
      <a id=\"readinessLink\" href=\"#\">Readiness Audit</a>
      <a id=\"reviewPlanLink\" href=\"#\">Review Plan</a>
      <a id=\"reviewSprintLink\" href=\"#\">Sprint 01</a>
      <a id=\"manualReviewLink\" href=\"#\">Review Workspace</a>
      <a id=\"pdfWorksheetLink\" href=\"#\">PDF Worksheet</a>
      <a id=\"pdfCardsLink\" href=\"#\">PDF Cards</a>
      <a id=\"pdfTransferLink\" href=\"#\">Transfer Checklist</a>
      <a id=\"dossierLink\" href=\"#\">Claim Dossiers</a>
      <a id=\"validationLink\" href=\"#\">QA Report</a>
    </nav>
  </header>
  <main>
    <section class=\"kpis\" id=\"kpis\"></section>

    <section id=\"areas\">
      <h2>Area Signal Matrix</h2>
      <div class=\"toolbar\">
        <input id=\"areaSearch\" type=\"search\" placeholder=\"Search area or tag\">
        <select id=\"areaSort\">
          <option value=\"taxonomy_share\">Sort by paper share</option>
          <option value=\"public_attention_enrichment\">Sort by public enrichment</option>
          <option value=\"oral_enrichment\">Sort by oral enrichment</option>
          <option value=\"historical_delta_vs_baseline\">Sort by venue delta</option>
          <option value=\"arxiv_2025_vs_2024_growth\">Sort by arXiv growth</option>
          <option value=\"github_url_share\">Sort by GitHub share</option>
        </select>
      </div>
      <div id=\"areaTable\"></div>
    </section>

    <section id=\"claims\">
      <h2>Synthesis Claims</h2>
      <div class=\"claims-grid\" id=\"claimsGrid\"></div>
    </section>

    <section id=\"papers\">
      <h2>Paper Explorer</h2>
      <div class=\"toolbar\">
        <input id=\"paperSearch\" type=\"search\" placeholder=\"Search title, area, method, contribution\">
        <select id=\"paperArea\"><option value=\"all\">All areas</option></select>
        <select id=\"paperFilter\">
          <option value=\"all\">All papers</option>
          <option value=\"program\">Oral or award</option>
          <option value=\"github\">Has GitHub</option>
          <option value=\"review\">Taxonomy review</option>
        </select>
        <select id=\"paperSort\">
          <option value=\"score\">Sort by signal score</option>
          <option value=\"votes\">Sort by votes</option>
          <option value=\"visits\">Sort by 7d visits</option>
          <option value=\"github_stars\">Sort by GitHub stars</option>
        </select>
      </div>
      <div id=\"paperTable\"></div>
    </section>

    <section id=\"figures\">
      <h2>Figure Gallery</h2>
      <div class=\"figures\" id=\"figureGrid\"></div>
    </section>

    <section id=\"review\">
      <h2>Manual Review Progress</h2>
      <div id=\"boundedReview\"></div>
      <div id=\"reviewProgress\"></div>
    </section>

    <section id=\"validation\">
      <h2>Claim Validation Queue Preview</h2>
      <div class=\"toolbar\">
        <select id=\"claimFilter\"><option value=\"all\">All claims</option></select>
      </div>
      <div class=\"queue-list\" id=\"queueList\"></div>
    </section>

    <footer>
      Generated from local processed CSVs. See the workspace validation report for structural QA status.
    </footer>
  </main>
  <script id=\"payload\" type=\"application/json\">{payload_json}</script>
  <script>
    const data = JSON.parse(document.getElementById('payload').textContent);
    const fmtPct = value => `${{(Number(value || 0) * 100).toFixed(1)}}%`;
    const fmtDelta = value => `${{(Number(value || 0) * 100).toFixed(1)}} pp`;
    document.getElementById('newcomerLink').href = data.links.newcomerRoadmap;
    document.getElementById('newcomerSlidesLink').href = data.links.newcomerSlides;
    document.getElementById('projectLink').href = data.links.projectIndex;
    document.getElementById('overviewLink').href = data.links.overviewSeed;
    document.getElementById('areaBriefingLink').href = data.links.areaBriefings;
    document.getElementById('readinessLink').href = data.links.readinessAudit;
    document.getElementById('reviewPlanLink').href = data.links.reviewPlan;
    document.getElementById('reviewSprintLink').href = data.links.reviewSprint;
    document.getElementById('manualReviewLink').href = data.links.manualReviewWorkspace;
    document.getElementById('pdfWorksheetLink').href = data.links.pdfReviewWorksheet;
    document.getElementById('pdfCardsLink').href = data.links.pdfReviewCards;
    document.getElementById('pdfTransferLink').href = data.links.pdfReviewTransfer;
    document.getElementById('dossierLink').href = data.links.claimDossiers;
    document.getElementById('validationLink').href = data.links.validation;

    function renderKpis() {{
      const k = data.kpis;
      const items = [
        [k.papers.toLocaleString(), 'official ICML paper rows'],
        [k.areas, 'curated taxonomy areas'],
        [k.claims, 'synthesis claims'],
        [k.claimQueueRows, 'claim-review rows'],
        [`${{k.reviewedRows}} / ${{k.reviewRows}}`, 'manual rows reviewed'],
        [k.validationFailures, 'validation failures'],
        [k.topArea, 'largest area'],
        [k.topPublic, 'highest public attention'],
        [k.topProgram, 'highest oral enrichment'],
      ];
      document.getElementById('kpis').innerHTML = items.map(([value, label]) => `
        <div class=\"kpi\"><div class=\"value\">${{value}}</div><div class=\"label\">${{label}}</div></div>
      `).join('');
    }}

    function renderAreas() {{
      const query = document.getElementById('areaSearch').value.toLowerCase();
      const sortKey = document.getElementById('areaSort').value;
      const rows = data.areas
        .filter(row => (row.area + ' ' + row.signal_tags).toLowerCase().includes(query))
        .sort((a, b) => Number(b[sortKey] || 0) - Number(a[sortKey] || 0));
      document.getElementById('areaTable').innerHTML = `
        <table>
          <thead><tr>
            <th>Area</th><th>Papers</th><th>Share</th><th>Oral</th><th>Public</th><th>Venue Delta</th><th>arXiv Growth</th><th>GitHub</th><th>Tags</th>
          </tr></thead>
          <tbody>
            ${{rows.map(row => `<tr>
              <td><strong>${{row.area}}</strong></td>
              <td>${{row.taxonomy_papers}}</td>
              <td>${{row.taxonomy_share_fmt}}</td>
              <td>${{Number(row.oral_enrichment).toFixed(2)}}x</td>
              <td>${{Number(row.public_attention_enrichment).toFixed(2)}}x</td>
              <td>${{row.historical_delta_fmt}}</td>
              <td>${{row.arxiv_growth_fmt}}</td>
              <td>${{row.github_share_fmt}}</td>
              <td>${{row.tags.map(tag => `<span class=\"tag\">${{tag}}</span>`).join('') || '<span class=\"tag\">none</span>'}}</td>
            </tr>`).join('')}}
          </tbody>
        </table>`;
    }}

    function renderClaims() {{
      document.getElementById('claimsGrid').innerHTML = data.claims.map(claim => `
        <article class=\"claim\">
          <h3>${{claim.claim_id}}: ${{claim.theme}}</h3>
          <p>${{claim.statement}}</p>
          <p><strong>Evidence:</strong> ${{claim.evidence}}</p>
          <p><span class=\"strength\">${{claim.strength}}</span></p>
          <p><strong>Caveat:</strong> ${{claim.caveats}}</p>
          <p><strong>Next:</strong> ${{claim.next_validation}}</p>
        </article>
      `).join('');
    }}

    function setupPaperAreaFilter() {{
      const select = document.getElementById('paperArea');
      [...new Set(data.papers.map(row => row.area))].sort().forEach(area => {{
        const option = document.createElement('option');
        option.value = area;
        option.textContent = area;
        select.appendChild(option);
      }});
      select.addEventListener('change', renderPapers);
      document.getElementById('paperSearch').addEventListener('input', renderPapers);
      document.getElementById('paperFilter').addEventListener('change', renderPapers);
      document.getElementById('paperSort').addEventListener('change', renderPapers);
    }}

    function renderPapers() {{
      const query = document.getElementById('paperSearch').value.toLowerCase();
      const area = document.getElementById('paperArea').value;
      const filter = document.getElementById('paperFilter').value;
      const sortKey = document.getElementById('paperSort').value;
      let rows = data.papers.filter(row => {{
        const haystack = [row.title, row.area, row.subarea, row.contribution, row.methods, row.eval, row.topic_group].join(' ').toLowerCase();
        if (query && !haystack.includes(query)) return false;
        if (area !== 'all' && row.area !== area) return false;
        if (filter === 'program' && !(row.oral === 'true' || row.award)) return false;
        if (filter === 'github' && !row.github) return false;
        if (filter === 'review' && row.review_status !== 'needs_review') return false;
        return true;
      }});
      rows = rows.sort((a, b) => Number(b[sortKey] || 0) - Number(a[sortKey] || 0)).slice(0, 80);
      document.getElementById('paperTable').innerHTML = `
        <table>
          <thead><tr>
            <th>Paper</th><th>Area</th><th>Signals</th><th>Evidence</th><th>Links</th>
          </tr></thead>
          <tbody>
            ${{rows.map(row => `<tr>
              <td><strong>${{row.title}}</strong><br><span class=\"tag\">cluster ${{row.cluster}}</span> <span class=\"tag\">${{row.topic_group || 'Unknown'}}</span></td>
              <td>${{row.area}}<br><span class=\"tag\">${{row.subarea}}</span></td>
              <td>votes ${{row.votes}}<br>7d ${{row.visits}}<br>${{row.oral === 'true' ? '<span class=\"tag\">oral</span>' : ''}} ${{row.award ? `<span class=\"tag\">${{row.award}}</span>` : ''}} ${{row.review_status === 'needs_review' ? '<span class=\"tag\">taxonomy-review</span>' : ''}}</td>
              <td>${{row.contribution || 'uncoded'}}<br>${{row.methods || ''}}<br>${{row.eval || ''}}</td>
              <td><a href=\"${{row.url}}\">ICML</a>${{row.alphaxiv_url ? ` · <a href=\"${{row.alphaxiv_url}}\">AlphaXiv</a>` : ''}}${{row.github ? ` · <a href=\"${{row.github}}\">GitHub</a>` : ''}}${{row.github_stars ? `<br>${{row.github_stars}} stars` : ''}}</td>
            </tr>`).join('')}}
          </tbody>
        </table>
        <p class=\"subtitle\">Showing top ${{rows.length}} matching papers by selected sort.</p>`;
    }}

    function renderFigures() {{
      document.getElementById('figureGrid').innerHTML = data.figures.map(fig => `
        <article class=\"figure-card\">
          <h3>${{fig.title}}</h3>
          <p>${{fig.description}}</p>
          <a href=\"${{fig.src}}\"><img src=\"${{fig.src}}\" alt=\"${{fig.title}}\"></a>
        </article>
      `).join('');
    }}

    function renderReviewProgress() {{
      const bounded = data.boundedReview;
      document.getElementById('boundedReview').innerHTML = `
        <div class=\"callout\">
          <strong>Bounded PDF review path:</strong>
          ${{bounded.extractablePdfs}}/${{bounded.pdfs}} probe PDFs extract cleanly, with ${{bounded.cards}} review cards,
          ${{bounded.worksheetRows}} worksheet rows, and ${{bounded.transferRows}} transfer decisions ready for manual review.
          <div class=\"small-links\">
            <a href=\"${{data.links.paperSourceAccess}}\">source access</a>
            <a href=\"${{data.links.pdfExtractionProbe}}\">PDF probe</a>
            <a href=\"${{data.links.pdfReviewCards}}\">cards</a>
            <a href=\"${{data.links.pdfReviewWorksheet}}\">worksheet</a>
            <a href=\"${{data.links.pdfReviewTransfer}}\">transfer checklist</a>
            <a href=\"${{data.links.reviewDecisionTasks}}\">decision tasks</a>
          </div>
          <p class=\"subtitle\">Claims touched by this bounded pass: ${{bounded.claims.join(', ') || 'none'}}.</p>
        </div>`;
      const rows = data.reviewProgress;
      document.getElementById('reviewProgress').innerHTML = `
        <table>
          <thead><tr>
            <th>Queue</th><th>Group</th><th>Rows</th><th>Reviewed</th><th>Remaining</th><th>Program/Award</th><th>Taxonomy Review</th><th>GitHub</th>
          </tr></thead>
          <tbody>
            ${{rows.map(row => `<tr>
              <td>${{row.queue_type}}</td>
              <td><strong>${{row.group}}</strong></td>
              <td>${{row.review_rows}}</td>
              <td>${{row.reviewed_rows}} (${{(Number(row.completion_rate || 0) * 100).toFixed(1)}}%)</td>
              <td>${{row.remaining_rows}}</td>
              <td>${{row.program_or_award_rows}}</td>
              <td>${{row.taxonomy_review_rows}}</td>
              <td>${{row.github_rows}}</td>
            </tr>`).join('')}}
          </tbody>
        </table>
        <p class=\"subtitle\">Manual fields are intentionally blank until a human review is completed. See <a href=\"${{data.links.reviewProgress}}\">manual review progress</a>.</p>`;
    }}

    function setupClaimFilter() {{
      const select = document.getElementById('claimFilter');
      data.claims.forEach(claim => {{
        const option = document.createElement('option');
        option.value = claim.claim_id;
        option.textContent = `${{claim.claim_id}}: ${{claim.theme}}`;
        select.appendChild(option);
      }});
      select.addEventListener('change', renderQueue);
    }}

    function renderQueue() {{
      const filter = document.getElementById('claimFilter').value;
      const rows = data.queue.filter(row => filter === 'all' || row.claim_id === filter);
      document.getElementById('queueList').innerHTML = rows.map(row => `
        <article class=\"queue-item\">
          <h3>${{row.claim_id}}.${{row.rank}} ${{row.title}}</h3>
          <p>${{row.area}}</p>
          <p><strong>Reason:</strong> ${{row.reason}}</p>
          <p><strong>Focus:</strong> ${{row.focus}}</p>
          <p>Votes: ${{row.votes}} · Oral: ${{row.oral}} · Cluster: ${{row.cluster}} · ${{row.review_status}}</p>
          <div class=\"small-links\">
            <a href=\"${{row.url}}\">ICML</a>
            ${{row.alphaxiv_url ? `<a href=\"${{row.alphaxiv_url}}\">AlphaXiv</a>` : ''}}
          </div>
        </article>
      `).join('');
    }}

    document.getElementById('areaSearch').addEventListener('input', renderAreas);
    document.getElementById('areaSort').addEventListener('change', renderAreas);
    renderKpis();
    renderAreas();
    renderClaims();
    setupPaperAreaFilter();
    renderPapers();
    renderFigures();
    renderReviewProgress();
    setupClaimFilter();
    renderQueue();
  </script>
</body>
</html>
"""


def main() -> int:
    payload = build_payload()
    html_text = render_html(payload)
    DOCS.mkdir(parents=True, exist_ok=True)
    path = DOCS / "dashboard.html"
    path.write_text(html_text, encoding="utf-8")
    print(f"Wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
