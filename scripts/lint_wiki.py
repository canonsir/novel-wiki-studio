#!/usr/bin/env python3
"""Static checks for a novel wiki. Uses only the Python standard library."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

REQUIRED_FIELDS = {"id", "type", "title", "status", "canon", "source_refs", "updated", "tags"}
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
LOG_RE = re.compile(r"^## \[\d{4}-\d{2}-\d{2}\] (ingest|query|expand|lint|decision|setup) \| .+")
ID_RE = re.compile(r"^id:\s*[\"']?([^\"'\n]+)", re.MULTILINE)
KEY_RE = re.compile(r"^([a-zA-Z_][a-zA-Z0-9_-]*):", re.MULTILINE)


@dataclass
class Issue:
    severity: str
    path: Path
    message: str


def frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    return None if end < 0 else text[4:end]


def resolve_link(wiki_root: Path, raw: str) -> Path:
    rel = raw.strip().lstrip("/")
    if rel.startswith("wiki/"):
        rel = rel[5:]
    if rel.endswith("/"):
        return wiki_root / rel / "_index.md"
    target = wiki_root / rel
    if target.suffix != ".md":
        target = target.with_suffix(".md")
    return target


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Lint a novel wiki")
    parser.add_argument("novel", type=Path, help="Path such as novels/my-novel")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    novel = args.novel.resolve()
    wiki = novel / "wiki"
    issues: list[Issue] = []

    if not (novel / "novel.yaml").is_file() or not wiki.is_dir():
        print("error: path must contain novel.yaml and wiki/", file=sys.stderr)
        return 2

    pages = sorted(wiki.rglob("*.md"))
    content_pages = [p for p in pages if not p.name.startswith("_")]
    known = {p.resolve() for p in pages}
    ids: dict[str, list[Path]] = defaultdict(list)
    inbound: Counter[Path] = Counter()
    indexed: set[Path] = set()
    index_path = wiki / "index.md"

    for page in pages:
        text = page.read_text(encoding="utf-8")
        fm = frontmatter(text)
        if page in content_pages and page.name not in {"index.md", "log.md"}:
            if fm is None:
                issues.append(Issue("ERROR", page, "missing YAML frontmatter"))
            else:
                keys = set(KEY_RE.findall(fm))
                for key in sorted(REQUIRED_FIELDS - keys):
                    issues.append(Issue("ERROR", page, f"missing frontmatter field: {key}"))
                match = ID_RE.search(fm)
                if match:
                    ids[match.group(1).strip()].append(page)

        for raw_link in WIKILINK_RE.findall(text):
            target = resolve_link(wiki, raw_link)
            if target.resolve() not in known:
                issues.append(Issue("ERROR", page, f"broken wikilink: [[{raw_link}]]"))
            else:
                inbound[target.resolve()] += 1
                if page == index_path:
                    indexed.add(target.resolve())

    for entity_id, paths in sorted(ids.items()):
        if len(paths) > 1:
            joined = ", ".join(str(p.relative_to(novel)) for p in paths)
            issues.append(Issue("ERROR", novel, f"duplicate id {entity_id}: {joined}"))

    excluded_from_index = {index_path.resolve(), (wiki / "log.md").resolve()}
    for page in content_pages:
        resolved = page.resolve()
        if resolved not in excluded_from_index and resolved not in indexed:
            issues.append(Issue("WARN", page, "page is not linked from wiki/index.md"))
        if resolved not in excluded_from_index and inbound[resolved] == 0:
            issues.append(Issue("WARN", page, "orphan page: no inbound wikilinks"))

    log_path = wiki / "log.md"
    if log_path.is_file():
        for line_no, line in enumerate(log_path.read_text(encoding="utf-8").splitlines(), 1):
            if line.startswith("## [") and not LOG_RE.fullmatch(line):
                issues.append(Issue("ERROR", log_path, f"invalid log header at line {line_no}"))
    else:
        issues.append(Issue("ERROR", log_path, "missing wiki/log.md"))

    errors = sum(i.severity == "ERROR" for i in issues)
    warnings = sum(i.severity == "WARN" for i in issues)
    print(f"novel: {novel}")
    print(
        f"pages: {len(content_pages)} content / {len(pages)} total | "
        f"ids: {len(ids)} | errors: {errors} | warnings: {warnings}"
    )
    for issue in issues:
        try:
            rel = issue.path.relative_to(novel)
        except ValueError:
            rel = issue.path
        print(f"{issue.severity}: {rel}: {issue.message}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
