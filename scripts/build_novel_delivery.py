#!/usr/bin/env python3
"""Build numbered LLM-Wiki views and a continuity-restored complete manuscript."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOVEL = ROOT / "novels" / "qing-xian-meinv-laoshi"
SOURCE = NOVEL / "raw" / "manuscript" / "SRC-20261008-001-original-manuscript.md"
OUTPUT = NOVEL / "drafts" / "complete" / "qing-xian-meinv-laoshi-reconstructed-v1.md"
MISSING = NOVEL / "drafts" / "chapters" / "reconstructed-missing"

VIEWS = {
    "00-admin/README.md": """# 00 Admin

项目控制台，不复制权威事实。

- [小说配置](../novel.yaml)
- [故事总览](../wiki/overview.md)
- [已确认决策](../decisions/DEC-20261008-001-original-reconstruction.md)
- [Wiki 索引](../wiki/index.md)
- [变更日志](../wiki/log.md)
- [连续性冲突](../wiki/continuity/contradictions.md)
- [重构进度](reconstruction-progress.md)
""",
    "00-admin/reconstruction-progress.md": """# 重构进度

| 交付层 | 状态 | 说明 |
|---|---|---|
| 来源登记与哈希 | complete | raw 保持只读 |
| 章节结构扫描 | complete | 747 个标题 |
| 缺失正文修复 | complete | 第98、100、102、557章为 proposed 补章 |
| 错号统一 | complete | 完整基线版按标题实际顺序编号1–747 |
| 全局 Wiki | complete | 人物、世界、势力、地点、视频规则 |
| 全文深度原创重写 | in_progress | 需按30批逐章重构，不能以机械整理冒充 |
| 连续可读基线版 | complete | `drafts/complete/` |

当前完整稿是“连续性重构基线版”：保留授权原稿正文，补齐缺章并统一编号。
后续每批深度重写采用后，替换对应章节并同步 Wiki。
""",
    "01-world/README.md": """# 01 World

- [世界圣经](../wiki/world/world-bible.md)
- [势力版图与等级](../wiki/factions/faction-power-map.md)
- [能力、战力与行动规则](../wiki/systems/system-ability-and-combat.md)
- [三线爽点增长系统](../wiki/systems/system-three-growth-engines.md)
- [地点与资产图谱](../wiki/locations/location-asset-atlas.md)
""",
    "02-characters/README.md": """# 02 Characters

- [人物线总圣经](../wiki/characters/character-arc-bible.md)
- [人物关系矩阵](../wiki/relationships/relationship-matrix.md)
- [陈照南](../wiki/characters/char-chen-zhaonan.md)
- [夏梓妍](../wiki/characters/char-xia-ziyan.md)
- [罗莉](../wiki/characters/char-luo-li.md)
- [徐苗苗](../wiki/characters/char-xu-miaomiao.md)
- [李振北](../wiki/characters/char-li-zhenbei.md)
""",
    "03-plotlines/README.md": """# 03 Plotlines

- [故事结构](../wiki/plot/structure.md)
- [主线事件骨架](../wiki/events/event-spine.md)
- [伏笔账本](../wiki/clues/clue-ledger.md)
- [AI短剧长线改编路线](../wiki/plot/short-drama-roadmap.md)
- [首轮诊断报告](../reports/lint/2026-10-08-ingest-report.md)
""",
    "04-timeline/README.md": """# 04 Timeline

- [主时间线](../wiki/timeline/master-timeline.md)
- [连续性冲突](../wiki/continuity/contradictions.md)
- [来源章节目录](../reports/ingest/2026-10-08-source-inventory.md)
""",
    "05-sources/README.md": """# 05 Sources

- [来源登记](../raw/README.md)
- [只读原稿](../raw/manuscript/SRC-20261008-001-original-manuscript.md)
- [来源结构清单](../reports/ingest/2026-10-08-source-inventory.md)
- [补章目录](../drafts/chapters/reconstructed-missing/)

raw 不可改写。重构内容只进入 drafts、wiki 和 outputs。
""",
    "06-scenes/README.md": """# 06 Scenes

- [场景模板](../wiki/scenes/_scene-template.md)
- [地点资产图谱](../wiki/locations/location-asset-atlas.md)
- [完整连续性基线版](../drafts/complete/qing-xian-meinv-laoshi-reconstructed-v1.md)

逐章深度重构时，每个场景先登记 POV、目标、阻力、转折、关系变化与视频抓手。
""",
    "07-video/README.md": """# 07 Video

- [AI短剧视觉与声音圣经](../wiki/systems/system-video-visual-bible.md)
- [长线改编路线](../wiki/plot/short-drama-roadmap.md)
- [地点资产图谱](../wiki/locations/location-asset-atlas.md)
- [视频脚本模板](../outputs/video-scripts/_video-script-template.md)

生成前必须锁定角色阶段、服装、伤势、地点版本、道具与关系状态。
""",
    "08-questions/README.md": """# 08 Questions

## 阻断发布

无。用户已确认来源为本人作品且已授权。

## 待确认创作决策

1. 目标平台和单集时长。
2. 现实城市名是否全面架空。
3. 多关系最终名单及公开规则。
4. 特殊体质、药剂和神龙战力的上限。
5. 主角终局需要支付何种不可逆代价。
6. 第一人称是否保留到重构终稿。

决策确认后写入 `decisions/`，不得只留在聊天中。
""",
    "99-archive/README.md": """# 99 Archive

存放被正式替代的旧方案、旧索引和废弃草稿。移动到此处时必须：

1. 保留原文件名和日期；
2. 标记 `deprecated` 或 `superseded`；
3. 指向替代文件；
4. 不存放 raw 原稿。
""",
}


def write_views() -> None:
    for relative, content in VIEWS.items():
        path = NOVEL / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def normalized_title(index: int, heading: str) -> str:
    title = heading.strip()
    title = re.sub(r"^（第\d+章[^）]*）$", "", title)
    title = re.sub(r"^(?:第|帝)\s*\d+\s*(?:章|节)?\s*", "", title)
    if not title:
        return f"连续性补章"
    return title


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
            replacement = replacements[index].read_text(encoding="utf-8").strip()
            replacement = re.sub(r"^##\s+.+\n+", "", replacement)
            title_match = re.search(r"^##\s+(.+)$", replacements[index].read_text(encoding="utf-8"), re.MULTILINE)
            title = normalized_title(index, title_match.group(1) if title_match else "")
            body = clean_body(replacement)
        else:
            title = normalized_title(index, match.group(1))
            body = clean_body(text[match.end() : end])
        sections.extend([f"## 第{index}章 {title}".rstrip(), "", body, ""])
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(sections).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    write_views()
    build_complete()
    print(f"views: {len(VIEWS)}")
    print(f"complete manuscript: {OUTPUT}")


if __name__ == "__main__":
    main()
