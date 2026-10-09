#!/usr/bin/env python3
"""Build a FlowGram-compatible, closed-loop story graph for one or all novels."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOVELS = ROOT / "novels"
PUBLIC_DATA = ROOT / "apps" / "story-graph" / "public" / "data"
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
FIELD_RE = re.compile(r"^([a-zA-Z_][\w-]*):\s*(.*)$", re.MULTILINE)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")
CHAPTER_RE = re.compile(r"^##\s+第(\d+)章\s*(.*)$", re.MULTILINE)
REWRITE_RE = re.compile(r"第(\d+)章")

KIND_MAP = {
    "overview": "root",
    "character": "character",
    "event": "event",
    "faction": "faction",
    "location": "location",
    "term": "term",
    "scene": "scene",
    "plot": "plot",
    "structure": "plot",
    "timeline": "event",
    "system": "system",
    "world": "system",
    "relationship": "plot",
    "clue": "plot",
}
KIND_ORDER = [
    "root",
    "plot",
    "character",
    "event",
    "faction",
    "location",
    "term",
    "system",
    "scene",
    "other",
]


def field(text: str, name: str, default: str = "") -> str:
    frontmatter = FRONTMATTER_RE.match(text)
    if not frontmatter:
        return default
    values = dict(FIELD_RE.findall(frontmatter.group(1)))
    return values.get(name, default).strip().strip("\"'")


def summary(text: str) -> str:
    body = FRONTMATTER_RE.sub("", text, count=1)
    paragraphs = [
        re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", lambda m: m.group(2) or m.group(1), part)
        for part in re.split(r"\n\s*\n", body)
        if part.strip() and not part.lstrip().startswith(("#", "-", "|", ">"))
    ]
    value = re.sub(r"\s+", " ", paragraphs[0]).strip() if paragraphs else ""
    return value[:180]


def node(node_id: str, data: dict, x: int, y: int) -> dict:
    return {
        "id": node_id,
        "type": "novel-node",
        "meta": {"position": {"x": x, "y": y}},
        "data": data,
    }


def edge(source: str, target: str, relation: str, weight: int = 1) -> dict:
    return {
        "sourceNodeID": source,
        "targetNodeID": target,
        "data": {"relation": relation, "weight": weight},
    }


def chapter_source(novel: Path) -> Path | None:
    complete = novel / "drafts" / "complete"
    candidates = sorted(complete.glob("*.md"))
    proofread = [path for path in candidates if "proofread" in path.name]
    return (proofread or candidates)[-1] if candidates else None


def resolve_wikilink(wiki: Path, page: Path, raw: str) -> Path | None:
    clean = raw.strip().lstrip("/")
    if clean.startswith("wiki/"):
        clean = clean[5:]
    candidates = [wiki / clean, page.parent / clean]
    for candidate in candidates:
        target = candidate if candidate.suffix == ".md" else candidate.with_suffix(".md")
        if target.is_file():
            return target.resolve()
    return None


def parse_chapters(path: Path | None) -> list[dict]:
    if path is None:
        return []
    text = path.read_text(encoding="utf-8")
    matches = list(CHAPTER_RE.finditer(text))
    chapters = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        number = int(match.group(1))
        title = match.group(2).strip() or f"第{number}章"
        chapters.append(
            {
                "number": number,
                "title": f"第{number}章 {title}",
                "body": text[match.end() : end],
                "source": path,
            }
        )
    return chapters


def build(novel: Path) -> dict:
    wiki = novel / "wiki"
    if not (novel / "novel.yaml").is_file() or not wiki.is_dir():
        raise ValueError(f"{novel} must contain novel.yaml and wiki/")

    config = (novel / "novel.yaml").read_text(encoding="utf-8")
    novel_id = field(f"---\n{config}\n---\n", "id", novel.name)
    novel_title = field(f"---\n{config}\n---\n", "title", novel.name)
    updated = field(f"---\n{config}\n---\n", "updated", "unknown")
    all_wiki_pages = sorted(wiki.rglob("*.md"))
    pages = [
        path
        for path in all_wiki_pages
        if path.name not in {"index.md", "log.md"}
        and not path.name.startswith("_")
        and "template" not in path.stem.lower()
    ]

    graph_nodes: list[dict] = []
    graph_edges: list[dict] = []
    page_nodes: dict[Path, str] = {}
    title_nodes: dict[str, str] = {}
    grouped: dict[str, list[tuple[Path, str, str, str, str, str]]] = defaultdict(list)

    for page in pages:
        text = page.read_text(encoding="utf-8")
        page_type = field(text, "type", "other")
        kind = KIND_MAP.get(page_type, "other")
        title = field(text, "title", page.stem)
        page_id = field(text, "id", page.relative_to(wiki).with_suffix("").as_posix())
        grouped[kind].append(
            (page, page_id, title, field(text, "canon", "unknown"), field(text, "status", "unknown"), text)
        )

    root_id = f"novel:{novel_id}"
    graph_nodes.append(
        node(
            root_id,
            {
                "title": novel_title,
                "kind": "root",
                "summary": "小说闭环知识图谱",
                "canon": "confirmed",
                "status": "active",
                "sourcePath": f"novels/{novel.name}/novel.yaml",
            },
            0,
            0,
        )
    )

    category_ids: dict[str, str] = {}
    x_spacing = 370
    for column, kind in enumerate(KIND_ORDER):
        entries = grouped.get(kind, [])
        if not entries:
            continue
        category_id = f"category:{kind}"
        category_ids[kind] = category_id
        x = (column - len(KIND_ORDER) / 2) * x_spacing
        graph_nodes.append(
            node(
                category_id,
                {
                    "title": {
                        "character": "人物",
                        "event": "事件与时间线",
                        "faction": "组织势力",
                        "location": "地点",
                        "term": "专有名词",
                        "plot": "剧情结构",
                        "system": "世界与规则",
                        "scene": "场景",
                        "root": "故事总览",
                        "other": "其他知识",
                    }.get(kind, kind),
                    "kind": "category",
                    "summary": f"{len(entries)} 个知识页面",
                    "canon": "derived",
                    "status": "active",
                    "sourcePath": f"novels/{novel.name}/wiki",
                    "evidenceCount": len(entries),
                },
                int(x),
                300,
            )
        )
        graph_edges.append(edge(root_id, category_id, "包含", len(entries)))
        for row, (page, page_id, title, canon, status, text) in enumerate(entries):
            graph_id = f"wiki:{page_id}"
            rel = page.relative_to(ROOT).as_posix()
            graph_nodes.append(
                node(
                    graph_id,
                    {
                        "title": title,
                        "kind": kind,
                        "summary": summary(text),
                        "canon": canon,
                        "status": status,
                        "sourcePath": rel,
                        "evidenceCount": len(re.findall(r"SRC-\d+-\d+", text)),
                        "completeness": min(100, max(10, len(text) // 20)),
                    },
                    int(x),
                    600 + row * 150,
                )
            )
            page_nodes[page.resolve()] = graph_id
            title_nodes[title] = graph_id
            graph_edges.append(edge(category_id, graph_id, "收录"))

    seen_links: Counter[tuple[str, str]] = Counter()
    for page, source_id in page_nodes.items():
        text = page.read_text(encoding="utf-8")
        for raw, _display in WIKILINK_RE.findall(text):
            target = resolve_wikilink(wiki, page, raw)
            if target and target in page_nodes and page_nodes[target] != source_id:
                seen_links[(source_id, page_nodes[target])] += 1
    for (source, target), weight in seen_links.items():
        graph_edges.append(edge(source, target, "Wiki 引用", weight))

    ordered_events = []
    for page, graph_id in page_nodes.items():
        data = next(item["data"] for item in graph_nodes if item["id"] == graph_id)
        if data["kind"] != "event":
            continue
        chapter_numbers = [
            int(number)
            for number in re.findall(r"(?:第|chapter[-_/]?)(\d+)章?", page.read_text(encoding="utf-8"))
        ]
        if chapter_numbers:
            ordered_events.append((min(chapter_numbers), graph_id))
    ordered_events.sort()
    for previous, current in zip(ordered_events, ordered_events[1:]):
        graph_edges.append(edge(previous[1], current[1], "事件后继"))

    chapters = parse_chapters(chapter_source(novel))
    chapter_category = "category:chapters"
    graph_nodes.append(
        node(
            chapter_category,
            {
                "title": "完整正文",
                "kind": "category",
                "summary": f"{len(chapters)} 章校订正文",
                "canon": "confirmed",
                "status": "active",
                "sourcePath": chapter_source(novel).relative_to(ROOT).as_posix() if chapter_source(novel) else "",
                "evidenceCount": len(chapters),
            },
            0,
            -300,
        )
    )
    graph_edges.append(edge(root_id, chapter_category, "正文"))

    linked_chapters = 0
    searchable_titles = sorted(
        ((title, graph_id) for title, graph_id in title_nodes.items() if len(title) >= 2),
        key=lambda item: len(item[0]),
        reverse=True,
    )
    for index, chapter in enumerate(chapters):
        chapter_id = f"chapter:{chapter['number']:04d}"
        graph_nodes.append(
            node(
                chapter_id,
                {
                    "title": chapter["title"],
                    "kind": "chapter",
                    "summary": re.sub(r"\s+", " ", chapter["body"]).strip()[:180],
                    "canon": "confirmed",
                    "status": "proofread",
                    "sourcePath": chapter["source"].relative_to(ROOT).as_posix(),
                    "chapter": chapter["number"],
                    "phase": "完整校订稿",
                },
                (index % 25) * 280 - 3360,
                -650 - (index // 25) * 145,
            )
        )
        if index == 0:
            graph_edges.append(edge(chapter_category, chapter_id, "起始章节"))
        else:
            graph_edges.append(edge(f"chapter:{chapters[index - 1]['number']:04d}", chapter_id, "下一章"))
        mentions = []
        for title, target_id in searchable_titles:
            count = chapter["body"].count(title)
            if count:
                mentions.append((count, title, target_id))
        if mentions:
            linked_chapters += 1
        else:
            graph_edges.append(edge(chapter_id, root_id, "属于故事"))
            linked_chapters += 1
        for count, _title, target_id in sorted(mentions, reverse=True)[:12]:
            graph_edges.append(edge(chapter_id, target_id, "正文提及", count))

    rewritten = sorted((novel / "drafts" / "chapters").rglob("第*章*.md"))
    for index, path in enumerate(rewritten):
        match = REWRITE_RE.search(path.name)
        number = int(match.group(1)) if match else None
        rewrite_id = f"rewrite:{path.relative_to(novel).as_posix()}"
        text = path.read_text(encoding="utf-8")
        graph_nodes.append(
            node(
                rewrite_id,
                {
                    "title": path.stem,
                    "kind": "chapter",
                    "summary": summary(text),
                    "canon": "proposed",
                    "status": "rewritten",
                    "sourcePath": path.relative_to(ROOT).as_posix(),
                    "chapter": number,
                    "phase": path.parent.name,
                },
                7200,
                -650 - index * 145,
            )
        )
        graph_edges.append(edge(chapter_category, rewrite_id, "原创重构"))
        if number and any(chapter["number"] == number for chapter in chapters):
            graph_edges.append(edge(f"chapter:{number:04d}", rewrite_id, "重构为"))

    inbound = Counter(item["targetNodeID"] for item in graph_edges)
    orphan_nodes = sum(
        item["id"] != root_id and inbound[item["id"]] == 0
        for item in graph_nodes
    )
    index_text = (wiki / "index.md").read_text(encoding="utf-8") if (wiki / "index.md").is_file() else ""
    indexed_pages = {
        target
        for raw, _display in WIKILINK_RE.findall(index_text)
        if (target := resolve_wikilink(wiki, wiki / "index.md", raw)) in page_nodes
    }
    return {
        "schemaVersion": 1,
        "novel": {
            "id": novel_id,
            "title": novel_title,
            "generatedAt": updated,
        },
        "coverage": {
            "wikiPages": len(pages),
            "indexedPages": len(indexed_pages),
            "chapters": len(chapters),
            "linkedChapters": linked_chapters,
            "nodes": len(graph_nodes),
            "edges": len(graph_edges),
            "orphanNodes": orphan_nodes,
        },
        "nodes": graph_nodes,
        "edges": graph_edges,
    }


def write_graph(novel: Path) -> dict:
    data = build(novel)
    graph_dir = novel / "graph"
    graph_dir.mkdir(exist_ok=True)
    graph_path = graph_dir / "story-graph.json"
    graph_path.write_text(
        json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    PUBLIC_DATA.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(graph_path, PUBLIC_DATA / f"{novel.name}.json")
    return {
        "id": data["novel"]["id"],
        "title": data["novel"]["title"],
        "file": f"{novel.name}.json",
        "coverage": data["coverage"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("novel", nargs="?", type=Path)
    parser.add_argument("--all", action="store_true", help="Build every novel under novels/")
    args = parser.parse_args()
    targets = (
        sorted(path for path in NOVELS.iterdir() if (path / "novel.yaml").is_file())
        if args.all
        else [args.novel.resolve() if args.novel else None]
    )
    if not targets or targets == [None]:
        parser.error("provide a novel path or --all")
    manifest = [write_graph(path) for path in targets if path]
    PUBLIC_DATA.mkdir(parents=True, exist_ok=True)
    (PUBLIC_DATA / "manifest.json").write_text(
        json.dumps({"novels": manifest}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    for item in manifest:
        coverage = item["coverage"]
        print(
            f"{item['id']}: {coverage['nodes']} nodes, {coverage['edges']} edges, "
            f"{coverage['chapters']} chapters, {coverage['orphanNodes']} orphans"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
