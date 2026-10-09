---
id: dec-20261009-007-naming-and-father-surname
type: decision
title: 文件命名规则 C 方案 & 女主父亲姓氏保留
status: approved
canon: confirmed
updated: 2026-10-09
tags: [decision, convention, naming]
---

# 决策

## 1. 文件命名规则：方案 C（中文名__ID.md 双段式）

用户选 C。所有 Wiki 页、决策、报告、章节草稿、场景卡文件名统一为：

```text
<中文名>__<原 ID>.md
```

示例：
- `characters/陈浩南__char-chen-haonan.md`
- `events/匿名约见__evt-anonymous-date.md`
- `scenes/S1-C01-匹配__scn-s1-c001-main.md`
- `locations/红屋咖啡厅__loc-hongwukafeiting.md`
- `factions/海迪__fac-haidi.md`
- `clues/夏父债务链__clue-zhao-debt-chain.md`
- `decisions/20261009-主角换名__dec-20261009-006.md`
- `chapters/S1-C01-匹配__c001.md`

### 迁移范围与成本

| 范围 | 文件数 | 风险 |
|---|---|---|
| wiki/ 全部 | ~244 | 低（脚本 glob 不解析文件名）|
| drafts/chapters/ | ~22 | 低 |
| decisions/ | 7 | 低 |
| reports/ | ~10 | 低 |

### 迁移执行计划（待用户 go/no-go）

因 ~280 文件 Git rename、Obsidian 双链、图谱重建需串行跑一遍，建议**单次一次性迁移**：

1. 写迁移脚本 `scripts/migrate_filenames_to_c_scheme.py`，根据 frontmatter `id` + `title` 生成新文件名并 `git mv`。
2. 更新 `scripts/rebuild_index.py`、`scripts/build_story_graph.py` 中硬编码 `char-*.md` glob（若有）。
3. 运行一次全量 rebuild + lint + graph，确认 0 错 0 警。
4. 文件内的 `[[characters/char-xxx|...]]` 双链语法会自动跟随（glob 不认），**但为了可读性建议同步**：`[[characters/陈浩南__char-chen-haonan|陈浩南]]`。

**本轮暂不执行迁移**。先把框架和拓扑图落完再统一迁，避免大 diff 掩盖正文变化。

## 2. 女主父亲姓氏：保留"夏启明"

### 依据

- 五大家族经核验是 **陈、林、苏、杨、张**（见 `fac-wudajiazu.md`），没有"沈"也没有"夏"。
- 女主父亲在原稿命中 145 次，是家庭债务线核心，不是家族棋局成员。
- 父亲姓氏与后续五大家族剧情**无关**。

### 结论

- 女主：**沈知微**（保持用户选定）
- 父亲：**保留"夏启明"**，剧情中由女主沈知微解释为"随母姓"——母亲"沈"姓，母亲早逝。母亲这条线既能解释姓氏，也能呼应女主已有的"妈妈的银戒指"关键道具（见 `char-shen-zhiwei.md`），为后续增加情感厚度。
- CON-009 关闭：三方案中选"路径 2 保留夏启明 + 母亲姓沈"。

## 本次落地

- `char-shen-zhiwei.md`：在“秘密与信息状态”中强化母亲姓沈设定；frontmatter 增加 `mother_surname: 沈`。
- `char-xia-qiming.md`：在“关系”段补充“女儿随母姓‘沈’”。
- `continuity-contradictions.md` CON-009：状态改为 resolved。

## V4 追加（2026-10-09）

本决策第 2 部分被 `decisions/dec-20261009-013-v4-renaming-approval.md` 取代：

- 女主“沈知微”V4 更名“沈雪瑶”（ID `char-shen-xueyao`）。
- 父亲不再“保留夏启明 + 随母姓”，V4 决定父女同姓，最终定名“沈启明”（ID `char-shen-qiming`）。
- 本文件第 1 部分（文件命名方案 C）在此前目录重构中已被现行 `ID` 文件名体系取代，历史内容保留。
