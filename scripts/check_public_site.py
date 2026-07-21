#!/usr/bin/env python3
"""Check local links and essential markup in the assembled public site."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.has_main = False
        self.has_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if element_id := attributes.get("id"):
            self.ids.add(element_id)
        if tag == "main":
            self.has_main = True
        if tag == "title":
            self.has_title = True
        for name in ("href", "src"):
            if value := attributes.get(name):
                self.links.append(value)


def parse_pages(site: Path) -> dict[Path, PageParser]:
    pages: dict[Path, PageParser] = {}
    for path in site.rglob("*.html"):
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8"))
        pages[path.resolve()] = parser
    return pages


def target_path(page: Path, site: Path, raw_link: str) -> tuple[Path, str]:
    parsed = urlparse(raw_link)
    relative_path = unquote(parsed.path)
    if not relative_path:
        return page.resolve(), parsed.fragment
    if relative_path.startswith("/"):
        target = site / relative_path.lstrip("/")
    else:
        target = page.parent / relative_path
    if target.is_dir():
        target /= "index.html"
    return target.resolve(), parsed.fragment


def check_site(site: Path) -> list[str]:
    pages = parse_pages(site)
    failures: list[str] = []

    for page, parser in pages.items():
        label = page.relative_to(site)
        if not parser.has_title:
            failures.append(f"{label}: missing <title>")
        if page.name not in {"404.html", "icml2026_newcomer_slides.html", "dashboard.html"} and not parser.has_main:
            failures.append(f"{label}: missing <main>")

        for raw_link in parser.links:
            parsed = urlparse(raw_link)
            if parsed.scheme in {"http", "https", "mailto", "data"} or raw_link.startswith("//"):
                continue
            target, fragment = target_path(page, site, raw_link)
            if not target.exists():
                failures.append(f"{label}: missing target {raw_link}")
                continue
            if fragment and target.suffix == ".html":
                target_parser = pages.get(target)
                if target_parser is not None and fragment not in target_parser.ids:
                    failures.append(f"{label}: missing anchor {raw_link}")

    return failures


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", nargs="?", default="_site", help="Assembled site directory.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    site = (ROOT / args.site).resolve() if not Path(args.site).is_absolute() else Path(args.site).resolve()
    if not site.is_dir():
        print(f"Site directory does not exist: {site}")
        return 1
    failures = check_site(site)
    if failures:
        print("Public site check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"Public site check passed: {len(list(site.rglob('*.html')))} HTML pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
