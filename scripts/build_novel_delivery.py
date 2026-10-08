#!/usr/bin/env python3
"""Build the continuity-restored manuscript without modifying knowledge views."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOVEL = ROOT / "novels" / "qing-xian-meinv-laoshi"
SOURCE = NOVEL / "raw" / "manuscript" / "SRC-20261008-001-original-manuscript.md"
OUTPUT = NOVEL / "drafts" / "complete" / "qing-xian-meinv-laoshi-reconstructed-v1.md"
MISSING = NOVEL / "drafts" / "chapters" / "reconstructed-missing"


def normalized_title(heading: str) -> str:
    title = heading.strip()
    title = re.sub(r"^（第\d+章[^）]*）$", "", title)
    title = re.sub(r"^(?:第|帝)\s*\d+\s*(?:章|节)?\s*", "", title)
    return title or "连续性补章"


def clean_body(body: str) -> str:
    return "\n".join(line.rstrip() for line in body.splitlines()).strip()


def build_complete() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    matches = list(re.finditer(r"^##\s+(.+)$", text, re.MULTILINE))
    replacements = {
        98: MISSING / "chapter-098.md",
        100: MISSING / "chapter-100.md",
        102: MISSING / "chapter-102.md",
        557: MISSING / "chapter-557.md",
    }
    sections: list[str] = [
        "# 情陷美女老师：连续性重构基线版",
        "",
        "> 基于作者本人授权原稿生成。保留原稿主体，补齐缺失章节并统一错乱章号。",
        "> 四篇补章为重构提案；全文深度原创重写按重构账本持续替换。",
        "",
    ]
    for index, match in enumerate(matches, 1):
        end = matches[index].start() if index < len(matches) else len(text)
        if index in replacements:
            replacement_text = replacements[index].read_text(encoding="utf-8")
            body = re.sub(r"^##\s+.+\n+", "", replacement_text).strip()
            title_match = re.search(r"^##\s+(.+)$", replacement_text, re.MULTILINE)
            title = normalized_title(title_match.group(1) if title_match else "")
        else:
            title = normalized_title(match.group(1))
            body = text[match.end() : end]
        sections.extend(
            [f"## 第{index}章 {title}".rstrip(), "", clean_body(body), ""]
        )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(sections).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    build_complete()
    print(f"complete manuscript: {OUTPUT}")


if __name__ == "__main__":
    main()
