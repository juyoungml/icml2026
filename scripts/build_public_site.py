#!/usr/bin/env python3
"""Assemble the self-contained GitHub Pages artifact."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "_site"
PUBLIC_FILES = ("LICENSE", "NOTICE.md", "CONTRIBUTING.md")
REWRITES = {
    "../figures/": "figures/",
    "../reports/": "reports/",
    "../LICENSE": "LICENSE",
}


def safe_output_path(raw_path: str) -> Path:
    """Resolve the build target and reject paths outside this repository."""
    output = Path(raw_path)
    if not output.is_absolute():
        output = ROOT / output
    output = output.resolve()
    if output == ROOT or ROOT not in output.parents:
        raise ValueError("The site output must be a child directory of the repository root.")
    return output


def copy_directory_contents(source: Path, destination: Path) -> None:
    for item in source.iterdir():
        target = destination / item.name
        if item.is_dir():
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)


def rewrite_site_links(output: Path) -> None:
    for html_path in output.rglob("*.html"):
        content = html_path.read_text(encoding="utf-8")
        for old, new in REWRITES.items():
            content = content.replace(old, new)
        html_path.write_text(content, encoding="utf-8")


def build_site(output: Path) -> None:
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    copy_directory_contents(ROOT / "docs", output)
    shutil.copytree(ROOT / "figures", output / "figures")
    shutil.copytree(ROOT / "reports", output / "reports")
    for filename in PUBLIC_FILES:
        shutil.copy2(ROOT / filename, output / filename)

    rewrite_site_links(output)
    (output / ".nojekyll").touch()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="Build directory inside the repository (default: _site).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output = safe_output_path(args.output)
    build_site(output)
    print(f"Built public site: {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
