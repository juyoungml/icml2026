#!/usr/bin/env python3
"""Friendly command runner for common project tasks."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_script(filename: str, *arguments: str) -> None:
    command = [sys.executable, str(ROOT / "scripts" / filename), *arguments]
    subprocess.run(command, cwd=ROOT, check=True)


def build_public_experience(output: str) -> None:
    run_script("build_newcomer_slides.py")
    run_script("build_static_dashboard.py")
    run_script("build_public_site.py", "--output", output)
    run_script("check_public_site.py", output)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build and check the ICML 2026 learning project through stable commands."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    site_parser = subparsers.add_parser("site", help="Build slides, dashboard, and deployable site.")
    site_parser.add_argument("--output", default="_site", help="Site output directory.")

    subparsers.add_parser("validate", help="Run workspace and public-product checks.")
    check_parser = subparsers.add_parser("check-site", help="Check an assembled site's local links.")
    check_parser.add_argument("site", nargs="?", default="_site", help="Assembled site directory.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.command == "site":
        build_public_experience(args.output)
    elif args.command == "validate":
        run_script("validate_workspace.py")
    elif args.command == "check-site":
        run_script("check_public_site.py", args.site)


if __name__ == "__main__":
    main()
