# 我的江湖（原创重构项目，暂定名）

本目录只保留当前有效结构。历史版本由 Git 管理，不在小说目录中复制归档。

## 唯一入口

- 最新完整阅读稿：[`drafts/manuscript/latest.md`](drafts/manuscript/latest.md)
- 最新分章重构：[`drafts/chapters/`](drafts/chapters/)
- LLM-Wiki：[`wiki/index.md`](wiki/index.md)
- 重构状态：[`reports/reconstruction-status.md`](reports/reconstruction-status.md)
- 目录整理报告：[`reports/directory-audit.md`](reports/directory-audit.md)
- 闭环图谱：[`graph/story-graph.json`](graph/story-graph.json)
- 已确认决策：[`decisions/`](decisions/)

## 真相层级

| 层级 | 职责 | 写权限 |
|---|---|---|
| `raw/` | 作者授权原稿与来源证据 | 只读 |
| `wiki/` | 人物、地点、势力、事件、场景、伏笔、物件和规则 | AI持续维护 |
| `drafts/manuscript/latest.md` | 当前唯一完整阅读基线 | 可迭代 |
| `drafts/chapters/` | 比完整基线更先进的分章原创重构 | 可迭代 |
| `graph/` | 从 Wiki 和最新正文生成的派生视图 | 只生成，不手改 |

## 当前状态

- 747章完整校订稿连续可读，缺失的98、100、102、557章已补齐。
- S1 第1-18章已有原创重构稿，状态为 `proposed`，尚未合并进完整阅读基线。
- S2和S5仅有连续性补章；S3、S4、S6尚未开始逐章重构。
- 人物、地点、势力、事件和术语已拆为独立 Wiki 页面。
- S1 已补充章级场景卡、关键伏笔与关键物件页。
- 结局、核心关系归宿和主角最终命运仍待用户确认。

## 检查命令

```bash
python3 scripts/rebuild_index.py novels/qing-xian-meinv-laoshi
python3 scripts/build_story_graph.py novels/qing-xian-meinv-laoshi
python3 scripts/lint_wiki.py novels/qing-xian-meinv-laoshi
python3 scripts/lint_story_graph.py novels/qing-xian-meinv-laoshi
```
