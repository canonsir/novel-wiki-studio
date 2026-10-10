#!/usr/bin/env python3
"""Validate that a generated story graph covers the canonical Wiki and manuscript."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from build_story_graph import build, chapter_source, parse_chapters


def load_expected_arcs(novel: Path) -> set[str]:
    """Read expected arc slugs from the arc split structure page (preferred)
    or fall back to the volume-level structure-plot.md.

    Looks for slugs that appear in a Markdown table cell between pipes, so
    narrative phrases like "S1-S6" won't be miscounted.
    """
    candidates = [
        novel / "wiki" / "plot" / "短剧Arc分段骨架.md",
        novel / "wiki" / "plot" / "structure-plot.md",
    ]
    slug_re = re.compile(r"\|\s*(s[1-9][a-z]?-[a-z][a-z0-9-]+)\s*\|")
    arcs: set[str] = set()
    for plot in candidates:
        if not plot.is_file():
            continue
        for line in plot.read_text(encoding="utf-8").splitlines():
            for match in slug_re.finditer(line):
                arcs.add(match.group(1))
    return arcs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("novel", type=Path)
    args = parser.parse_args()
    novel = args.novel.resolve()
    graph_path = novel / "graph" / "story-graph.json"
    if not graph_path.is_file():
        print(f"ERROR: missing {graph_path}", file=sys.stderr)
        return 2

    saved = json.loads(graph_path.read_text(encoding="utf-8"))
    rebuilt = build(novel)
    issues = []
    wiki_pages = [
        path
        for path in (novel / "wiki").rglob("*.md")
        if path.name not in {"index.md", "log.md"}
        and not path.name.startswith("_")
        and "template" not in path.stem.lower()
    ]
    chapters = parse_chapters(chapter_source(novel))
    chapter_root = novel / "drafts" / "chapters"
    actual_arcs = {path.name for path in chapter_root.iterdir() if path.is_dir()}
    rewrite_count = 0
    for path in chapter_root.rglob("c*.md"):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        head = text.split("---", 2)[1] if text.count("---") >= 2 else ""
        if "status: deprecated" in head or "canon: deprecated" in head:
            continue
        rewrite_count += 1
    coverage = saved.get("coverage", {})
    if chapter_source(novel) != novel / "drafts" / "manuscript" / "latest.md":
        issues.append("latest manuscript must be drafts/manuscript/latest.md")
    expected_arcs = load_expected_arcs(novel)
    if expected_arcs and actual_arcs != expected_arcs:
        issues.append(
            f"chapter arcs mismatch: missing={sorted(expected_arcs - actual_arcs)}, "
            f"extra={sorted(actual_arcs - expected_arcs)}"
        )
    if coverage.get("wikiPages") != len(wiki_pages):
        issues.append(f"wiki coverage {coverage.get('wikiPages')} != {len(wiki_pages)}")
    if coverage.get("indexedPages") != len(wiki_pages):
        issues.append(f"index coverage {coverage.get('indexedPages')} != {len(wiki_pages)}")
    if coverage.get("chapters") != len(chapters):
        issues.append(f"chapter coverage {coverage.get('chapters')} != {len(chapters)}")
    if coverage.get("rewrittenChapters") != rewrite_count:
        issues.append(
            f"rewrite coverage {coverage.get('rewrittenChapters')} != {rewrite_count}"
        )
    if coverage.get("orphanNodes") != 0:
        issues.append(f"orphan nodes: {coverage.get('orphanNodes')}")
    if len(saved.get("nodes", [])) != coverage.get("nodes"):
        issues.append("node count does not match coverage")
    if len(saved.get("edges", [])) != coverage.get("edges"):
        issues.append("edge count does not match coverage")
    if saved != rebuilt:
        issues.append("graph is stale; run scripts/build_story_graph.py")

    if issues:
        for issue in issues:
            print(f"ERROR: {issue}")
        return 1
    print(
        f"graph: {coverage['nodes']} nodes | {coverage['edges']} edges | "
        f"{coverage['wikiPages']} wiki pages | {coverage['chapters']} chapters | "
        f"{coverage['rewrittenChapters']} rewrites | closed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
