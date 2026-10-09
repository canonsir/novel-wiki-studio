---
id: dec-20261009-013-v4-renaming-approval
type: decision
title: 批准全书人物换名方案 V4 并执行批量迁移
status: approved
canon: confirmed
source_refs:
  - 用户确认 2026-10-09
  - reports/full-renaming-plan-v4-20261009.md
updated: 2026-10-09
tags: [decision, renaming, characters, v4, approval]
---

# 决策：批准 V4 全书换名并批量迁移

## 决策

用户于 2026-10-09 明确“批准 V4 方案，开始批量执行迁移”。
`reports/full-renaming-plan-v4-20261009.md` 状态由 proposed 升级为 approved/confirmed，作为本次迁移的完整映射依据。

## 迁移范围（已执行）

- `wiki/` 全部实体页：实体 ID、双链、frontmatter、标签与正式中文名；共物理重命名 88 个文件（74 人物 + 1 势力 + 1 物件 + 12 事件）。
- `drafts/chapters/` 全部重构章节与 arc：ID、双链与正式名同步。
- `scripts/build_framework_graphs.py`：人物名称同步（含“哈察将军”统一）。
- 每个迁移人物页顶部加入 V4 迁移说明（旧名→新名 + 本决策引用）。

## 关键规则

- **绰号保护**：绰号（如肥猫、白姐、雷哥、修罗、夜叉、秦老头、黄毛等）在正文中保留；人物页正式名按 V4 更新（胡胖、白玥、雷东、江凌、孟北、秦铮、王海等），清单见迁移脚本 `PROTECTED`。
- **ID 保留、中文名变化**：俞洋（`char-yu-yang`）、周建人（`char-zhou-jianren`）、付延林（`char-fu-yanlin`）、文天强（`char-wen-tianqiang`）、谢庭（`char-xie-ting`）、江东华（`char-jiang-donghua`）。
- **不动旧名基线**：`raw/` 永久只读；`drafts/manuscript/latest.md` 保留原稿旧名，随正式重写逐章替换。
- deprecated 页（夏梓妍、夏建国、陈照南）只更新迁移指针，正文历史不动。

## 新增设定（proposed，待正文采用）

- 张家族长原稿未具名，V4 补名 **张烈山**，新建 `wiki/characters/char-zhang-lieshan.md`。
- 主角家乡 **陈家果园**，新建 `wiki/locations/loc-chen-family-orchard.md`，作为陈远山隐居符号与身份伏笔。

## 与旧决策的关系

- `dec-20261009-006`：男主名沿用；女主“沈知微”被“沈雪瑶”取代。
- `dec-20261009-007`：父亲不再保留“夏启明/随母姓”，改为父女同姓的“沈启明”。
- `dec-20261009-012`：简介候选 B 已确认，名称与本方案一致。

## 迁移中查明并修正的事项

- **张震是族长之子，不是其孙**：原稿第 747 章原文“因为你有个讨厌的儿子……这是为张晟威那孙子打的”，“孙子”为骂人话。此前“张震是支脉、非继承人”的推断（依据第 331 章）标记为 contradicted，以原文为准，待精读查证其生母身份。
- V4 映射漏项“林青朝→林寒”已对 Wiki、重构章节、图谱脚本补替换；`char-lin-han.md` 页正文按迁移说明规则保留旧名。
- 删除两个无独立戏份的占位角色页：`char-chen-director-nephew`（并入 c017 场景文字）、`char-wang-counselor`（引用点同步清理）。

## 待确认

1. “张烈山”姓名及年龄外形细节（proposed）。
2. 霍凯、霍寒之父在 V4 霍家的正式名（原稿“李建国”仅在 deprecated 页出现）。
3. 果园的省份方位、与帝都/成都的路程距离。
