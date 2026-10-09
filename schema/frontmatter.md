# Wiki Frontmatter 规范

```yaml
---
id: char-example
type: character
title: 示例人物
status: active
canon: proposed
source_refs:
  - SRC-YYYYMMDD-001#L1-L20
confidence: medium
updated: YYYY-MM-DD
tags: [protagonist]
---
```

## 必填字段

- `id`：仓库内唯一、稳定，重命名标题时不改 ID。
- `type`：character/location/event/scene/faction/system/theme/clue/object/timeline/style/structure/continuity/reference/report/decision。
- `title`：人类可读标题。
- `status`：active/deprecated/merged/archived。
- `canon`：confirmed/inferred/proposed/contradicted。
- `source_refs`：原稿或决定引用；没有来源的提案写 `AI-PROPOSAL-日期`。
- `updated`：最后实质更新日期。
- `tags`：用于检索，不替代页面层级。

## 可选字段

`aliases`、`confidence`、`pov`、`date_start`、`date_end`、`location_refs`、`character_refs`、`clue_refs`、`decision_refs`、`supersedes`。

## 引用格式

文本来源尽量引用 `source_id#章节/段落/行`；若原文件不支持稳定行号，记录章节标题与摘录摘要。不要依靠“原文某处”。
