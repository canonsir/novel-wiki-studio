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
TYPE_LABELS = {
    "character": "人物",
    "faction": "势力",
    "location": "地点",
    "event": "事件",
    "term": "专有名词",
    "system": "系统",
    "world": "世界",
    "plot": "剧情",
    "timeline": "时间线",
    "relationship": "关系",
    "clue": "伏笔",
    "scene": "场景",
    "theme": "主题",
    "style": "文风",
    "structure": "结构",
    "continuity": "连续性",
    "object": "关键物件",
    "reference": "创作参考",
    "report": "分析报告",
}


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
    sections: dict[Path, list[tuple[str, str, str, str]]] = defaultdict(list)
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
        sections[path.parent].append((title, page_id, canon, rel))

    lines = [START, "", "## Generated catalog", ""]
    for page_type in sorted(groups):
        label = TYPE_LABELS.get(page_type, page_type)
        lines.extend([f"### {label}", "", *groups[page_type], ""])
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
    for directory, entries in sorted(sections.items()):
        if directory == wiki:
            continue
        section_types = sorted(
            {
                field(TYPE_RE, (wiki / f"{rel}.md").read_text(encoding="utf-8"), "other")
                for _, _, _, rel in entries
            }
        )
        labels = " / ".join(TYPE_LABELS.get(item, item) for item in section_types)
        section_lines = [
            f"# {labels}索引",
            "",
            "> 本页由 `scripts/rebuild_index.py` 根据正式 Wiki frontmatter 生成。",
            "",
        ]
        for title, page_id, canon, rel in sorted(entries):
            section_lines.append(f"- [[{rel}|{title}]] — `{page_id}` · {canon}")
        (directory / "_index.md").write_text(
            "\n".join(section_lines) + "\n", encoding="utf-8"
        )
    print(f"updated: {index}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
