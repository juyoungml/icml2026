#!/usr/bin/env python3
"""Fetch and parse ICML 2026 official virtual-site seed data."""

from __future__ import annotations

import csv
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "icml"
PROCESSED = ROOT / "data" / "processed"

ICML_PAPERS_URL = "https://icml.cc/virtual/2026/papers.html"
ICML_ORALS_URL = "https://icml.cc/virtual/2026/events/oral"
ICML_EVENTS_JSON_URL = "https://icml.cc/static/virtual/data/icml-2026-orals-posters.json"
ICML_ABSTRACTS_JSON_URL = "https://icml.cc/static/virtual/data/icml-2026-abstracts.json"
ICML_AWARDS_URL = "https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/"
ICML_BASE = "https://icml.cc"


AWARDS = [
    {
        "award": "Outstanding Paper Award",
        "title": "The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models",
        "authors": "Zanlin Ni; Shenzhi Wang; Yang Yue; Tianyu Yu; Weilin Zhao; Yeguo Hua; Tianyi Chen; Jun Song; Cheng Yu; Bo Zheng; Gao Huang",
        "url": "https://icml.cc/virtual/2026/oral/71086",
    },
    {
        "award": "Outstanding Paper Award",
        "title": "High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions",
        "authors": "Fan Chen; Sinho Chewi; Constantinos Daskalakis; Alexander Rakhlin",
        "url": "https://icml.cc/virtual/2026/oral/71132",
    },
    {
        "award": "Outstanding Position Paper Award",
        "title": "Position: The Alignment Community is Unintentionally Building a Censor's Toolkit",
        "authors": "Sarah Ball; Phil Hackemann",
        "url": "https://icml.cc/virtual/2026/oral/71119",
    },
    {
        "award": "Outstanding Paper Honorable Mention",
        "title": "The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes",
        "authors": "Mohammad Taufeeque; Stefan Heimersheim; Adam Gleave; Chris Cundy",
        "url": "https://icml.cc/virtual/2026/oral/71065",
    },
    {
        "award": "Outstanding Paper Honorable Mention",
        "title": "Motion Attribution for Video Generation",
        "authors": "Xindi Wu; Despoina Paschalidou; Jun Gao; Antonio Torralba; Laura Leal-Taixe; Olga Russakovsky; Sanja Fidler; Jonathan Lorraine",
        "url": "https://icml.cc/virtual/2026/oral/71049",
    },
    {
        "award": "Outstanding Paper Honorable Mention",
        "title": "How much can language models memorize?",
        "authors": "John Xavier Morris; Chawin Sitawarin; Narine Kokhlikyan; Chuan Guo; G. Edward Suh; Alexander M Rush; Kamalika Chaudhuri; Saeed Mahloujifar",
        "url": "https://icml.cc/virtual/2026/oral/71168",
    },
    {
        "award": "Outstanding Paper Honorable Mention",
        "title": "A Random Matrix Perspective on the Consistency of Diffusion Models",
        "authors": "Binxu Wang; Jacob A Zavatone-Veth; Cengiz Pehlevan",
        "url": "https://icml.cc/virtual/2026/oral/71191",
    },
    {
        "award": "Outstanding Paper Honorable Mention",
        "title": "To Grok Grokking: Provable Grokking in Ridge Regression",
        "authors": "Mingyue Xu; Gal Vardi; Itay Safran",
        "url": "https://icml.cc/virtual/2026/oral/71134",
    },
    {
        "award": "Outstanding Position Paper Honorable Mention",
        "title": "Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII)",
        "authors": "Li Qiwei; Wells Lucas Santo; Sarita Schoenebeck; Eric Gilbert",
        "url": "https://icml.cc/virtual/2026/oral/71187",
    },
    {
        "award": "Test of Time Award",
        "title": "Asynchronous Methods for Deep Reinforcement Learning",
        "authors": "Volodymyr Mnih; Adria Puigdomenech Badia; Mehdi Mirza; Alex Graves; Timothy P. Lillicrap; Tim Harley; David Silver; Koray Kavukcuoglu",
        "url": "https://proceedings.mlr.press/v48/mniha16.html",
    },
]


def fetch(url: str, dest: Path, force: bool = False) -> str:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and not force:
        return dest.read_text(encoding="utf-8", errors="replace")
    req = urllib.request.Request(url, headers={"User-Agent": "icml2026-eda/0.1"})
    with urllib.request.urlopen(req, timeout=30) as response:
        text = response.read().decode("utf-8", errors="replace")
    dest.write_text(text, encoding="utf-8")
    return text


def clean_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def parse_papers(page: str) -> list[dict[str, str]]:
    pattern = re.compile(
        r'<li><a href="(?P<href>/virtual/2026/(?P<kind>poster|oral)/(?P<event_id>\d+))">(?P<title>.*?)</a></li>',
        re.DOTALL,
    )
    rows = []
    seen = set()
    for match in pattern.finditer(page):
        event_id = match.group("event_id")
        if event_id in seen:
            continue
        seen.add(event_id)
        title = clean_text(match.group("title"))
        href = match.group("href")
        kind = match.group("kind")
        rows.append(
            {
                "event_id": event_id,
                "event_type": kind,
                "title": title,
                "url": ICML_BASE + href,
                "is_position": str(title.lower().startswith("position:")).lower(),
                "is_oral": "false",
                "oral_event_id": "",
                "oral_url": "",
            }
        )
    return rows


def parse_bulk_events(events_payload: dict, abstracts: dict[str, str]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    events = events_payload["results"]
    oral_by_poster_id = {}
    for event in events:
        if event.get("eventtype") != "Oral":
            continue
        for related_id in event.get("related_events_ids") or []:
            oral_by_poster_id[str(related_id)] = event

    event_rows = []
    paper_rows = []
    for event in events:
        event_id = str(event["id"])
        authors = event.get("authors") or []
        author_names = [a.get("fullname", "") for a in authors if a.get("fullname")]
        institutions = sorted({clean_text(a.get("institution", "")) for a in authors if a.get("institution")})
        event_rows.append(
            {
                "event_id": event_id,
                "event_type": event.get("eventtype") or "",
                "title": clean_text(event.get("name") or ""),
                "decision": event.get("decision") or "",
                "topic": event.get("topic") or "",
                "session": event.get("session") or "",
                "starttime": event.get("starttime") or "",
                "endtime": event.get("endtime") or "",
                "url": ICML_BASE + (event.get("virtualsite_url") or ""),
                "paper_url": event.get("paper_url") or "",
                "authors": "; ".join(author_names),
                "institutions": "; ".join(institutions),
            }
        )
        if event.get("eventtype") != "Poster":
            continue
        oral = oral_by_poster_id.get(event_id)
        paper_rows.append(
            {
                "event_id": event_id,
                "event_type": "poster",
                "title": clean_text(event.get("name") or ""),
                "url": ICML_BASE + (event.get("virtualsite_url") or ""),
                "paper_url": event.get("paper_url") or "",
                "openreview_url": event.get("paper_url") or "",
                "decision": event.get("decision") or "",
                "topic": event.get("topic") or "",
                "topic_group": (event.get("topic") or "").split("->", 1)[0] if event.get("topic") else "",
                "topic_subtopic": (event.get("topic") or "").split("->", 1)[1] if "->" in (event.get("topic") or "") else "",
                "session": event.get("session") or "",
                "starttime": event.get("starttime") or "",
                "poster_position": event.get("poster_position") or "",
                "authors": "; ".join(author_names),
                "institutions": "; ".join(institutions),
                "author_count": str(len(author_names)),
                "institution_count": str(len(institutions)),
                "abstract": clean_text(abstracts.get(event_id, "")),
                "is_position": str((event.get("name") or "").lower().startswith("position:")).lower(),
                "is_oral": str(oral is not None).lower(),
                "oral_event_id": str(oral.get("id")) if oral else "",
                "oral_url": ICML_BASE + (oral.get("virtualsite_url") or "") if oral else "",
                "oral_session": oral.get("session") if oral else "",
                "oral_starttime": oral.get("starttime") if oral else "",
                "oral_decision": oral.get("decision") if oral else "",
            }
        )
    return paper_rows, event_rows


def parse_orals(page: str) -> list[dict[str, str]]:
    pattern = re.compile(
        r'<h3 class="event-title">\s*<a href="(?P<href>/virtual/2026/oral/(?P<event_id>\d+))">(?P<title>.*?)</a>',
        re.DOTALL,
    )
    rows = []
    seen = set()
    for match in pattern.finditer(page):
        event_id = match.group("event_id")
        if event_id in seen:
            continue
        seen.add(event_id)
        href = match.group("href")
        rows.append(
            {
                "oral_event_id": event_id,
                "title": clean_text(match.group("title")),
                "oral_url": ICML_BASE + href,
            }
        )
    return rows


def normalize_title(title: str) -> str:
    title = html.unescape(title).lower()
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def add_oral_flags(papers: list[dict[str, str]], orals: list[dict[str, str]]) -> None:
    oral_by_title = {normalize_title(row["title"]): row for row in orals}
    for paper in papers:
        oral = oral_by_title.get(normalize_title(paper["title"]))
        if oral:
            paper["is_oral"] = "true"
            paper["oral_event_id"] = oral["oral_event_id"]
            paper["oral_url"] = oral["oral_url"]


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write: {path}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    RAW.mkdir(parents=True, exist_ok=True)
    PROCESSED.mkdir(parents=True, exist_ok=True)

    papers_html = fetch(ICML_PAPERS_URL, RAW / "icml2026_papers.html")
    orals_html = fetch(ICML_ORALS_URL, RAW / "icml2026_orals.html")
    events_json = json.loads(fetch(ICML_EVENTS_JSON_URL, RAW / "icml-2026-orals-posters.json"))
    abstracts_json = json.loads(fetch(ICML_ABSTRACTS_JSON_URL, RAW / "icml-2026-abstracts.json"))
    fetch(ICML_AWARDS_URL, RAW / "icml2026_awards.html")

    papers, events = parse_bulk_events(events_json, abstracts_json)
    if not papers:
        papers = parse_papers(papers_html)
    orals = parse_orals(orals_html)
    if not papers:
        print("No papers parsed from ICML virtual page.", file=sys.stderr)
        return 1
    if "is_oral" not in papers[0]:
        add_oral_flags(papers, orals)

    metadata = {
        "snapshot_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "sources": {
            "papers": ICML_PAPERS_URL,
            "orals": ICML_ORALS_URL,
            "events_json": ICML_EVENTS_JSON_URL,
            "abstracts_json": ICML_ABSTRACTS_JSON_URL,
            "awards": ICML_AWARDS_URL,
        },
        "paper_count": len(papers),
        "event_count": len(events),
        "oral_event_count": len(orals),
        "matched_oral_paper_count": sum(1 for row in papers if row["is_oral"] == "true"),
        "event_type_counts": {
            "poster": sum(1 for row in papers if row["event_type"] == "poster"),
            "oral_events": sum(1 for row in events if row["event_type"] == "Oral"),
        },
        "notes": [
            "Parsed from official ICML virtual bulk JSON, with noscript fallback available.",
            "One row per poster/paper; oral events are joined through related_events_ids.",
            "This is a public event/page corpus; reconcile with final proceedings counts before quoting acceptance statistics.",
        ],
    }

    write_csv(PROCESSED / "icml2026_papers.csv", papers)
    (PROCESSED / "icml2026_papers.json").write_text(json.dumps(papers, indent=2), encoding="utf-8")
    (PROCESSED / "icml2026_metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    write_csv(PROCESSED / "icml2026_events.csv", events)
    write_csv(PROCESSED / "icml2026_orals.csv", orals)
    write_csv(PROCESSED / "icml2026_awards.csv", AWARDS)

    print(f"Parsed {len(papers)} ICML 2026 paper/event rows")
    print(f"Parsed {len(orals)} oral event rows")
    print(f"Matched {metadata['matched_oral_paper_count']} oral papers by title")
    print(json.dumps(metadata["event_type_counts"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
