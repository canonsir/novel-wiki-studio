#!/usr/bin/env python3
"""Create a novel workspace from _template without external dependencies."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import sys
from pathlib import Path

TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".txt", ".json"}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a new novel wiki workspace")
    parser.add_argument("title", help="Human-readable novel title")
    parser.add_argument("--slug", required=True, help="ASCII kebab-case directory name")
    parser.add_argument("--dry-run", action="store_true", help="Validate and print target only")
    return parser.parse_args()


def replace_placeholders(root: Path, title: str, slug: str, today: str) -> None:
    replacements = {
        "{{NOVEL_TITLE}}": title,
        "{{NOVEL_SLUG}}": slug,
        "{{DATE}}": today,
    }
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        for old, new in replacements.items():
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")


def main() -> int:
    args = parse_args()
    if not args.title.strip():
        print("error: title cannot be empty", file=sys.stderr)
        return 2
    if not SLUG_RE.fullmatch(args.slug):
        print("error: --slug must be lowercase ASCII kebab-case", file=sys.stderr)
        return 2

    repo_root = Path(__file__).resolve().parents[1]
    template = repo_root / "_template"
    target = repo_root / "novels" / args.slug

    if not template.is_dir():
        print(f"error: missing template: {template}", file=sys.stderr)
        return 2
    if target.exists():
        print(f"error: target already exists: {target}", file=sys.stderr)
        return 2

    print(f"title: {args.title.strip()}")
    print(f"slug: {args.slug}")
    print(f"target: {target}")
    if args.dry_run:
        print("dry-run: no files created")
        return 0

    shutil.copytree(template, target)
    replace_placeholders(target, args.title.strip(), args.slug, dt.date.today().isoformat())
    print("created: novel workspace ready")
    print(f"next: put source files in {target / 'raw' / 'manuscript'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
