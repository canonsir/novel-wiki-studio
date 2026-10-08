#!/usr/bin/env python3
"""Rebuild the generated section of wiki/index.md from page frontmatter."""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

ID_RE = re.compile(r"^id:\s*[\"']?([^\"'\n]+)", re.MULTILINE)
TYPE_RE = re.compile(r"^type:\s*[\"']?([^\"'\n]+)", re.MULTILINE)
TITLE_RE = re.compile(r"^title:\s*[\"']?([^\"'\n]+)", re.MULTILINE)
CANON_RE = re.compile(r"^canon:\s*[\"']?([^\"'\n]+)", re.MULTILINE)
START = "<!-- GENERATED:START -->"
END = "<!-- GENERATED:END -->"


def field(regex: re.Pattern[str], text: str, default: str) -> str:
    match = regex.search(text)
    return match.group(1).strip() if match else default


def main() -> int:
    parser = argparse.ArgumentParser(description="Rebuild wiki index")
    parser.add_argument("novel", type=Path)
    args = parser.parse_args()
    novel = args.novel.resolve()
    wiki = novel / "wiki"
    index = wiki / "index.md"
    if not index.is_file():
        print(f"error: missing {index}", file=sys.stderr)
        return 2

    groups: dict[str, list[str]] = defaultdict(list)
    for path in sorted(wiki.rglob("*.md")):
        if path.name.startswith("_") or path.name in {"index.md", "log.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        page_type = field(TYPE_RE, text, "other")
        title = field(TITLE_RE, text, path.stem)
        page_id = field(ID_RE, text, "missing-id")
        canon = field(CANON_RE, text, "unknown")
        rel = path.relative_to(wiki).with_suffix("").as_posix()
        groups[page_type].append(f"- [[{rel}|{title}]] — `{page_id}` · {canon}")

    lines = [START, "", "## Generated catalog", ""]
    for page_type in sorted(groups):
        lines.extend([f"### {page_type}", "", *groups[page_type], ""])
    lines.append(END)
    generated = "\n".join(lines)

    original = index.read_text(encoding="utf-8")
    if START in original and END in original:
        before, rest = original.split(START, 1)
        _, after = rest.split(END, 1)
        updated = before.rstrip() + "\n\n" + generated + after
    else:
        updated = original.rstrip() + "\n\n" + generated + "\n"
    index.write_text(updated, encoding="utf-8")
    print(f"updated: {index}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
