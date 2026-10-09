---
id: dec-20261009-006-protagonist-renaming
type: decision
title: 主角换名决策（男主→陈浩南 / 女主→沈知微）
status: approved
canon: confirmed
source_refs:
  - 用户确认 2026-10-09
updated: 2026-10-09
tags: [decision, renaming, protagonist]
---

# 决策：主角换名

## 决策

| 原名 | 新名 | 新 Wiki ID | 气质适配 |
|---|---|---|---|
| 陈～南（原"陈照南"） | **陈浩南** | `char-chen-haonan` | 用户指定，呼应《古惑仔》陈浩南的地下升级弧与"南哥"兄弟标签；保留"南哥"口语昵称无需改动 |
| 夏～妍（原"夏梓妍"） | **沈知微** | `char-shen-zhiwei` | 沈姓静水，"知微见著"调查者气质；贴合"主动调查债务、拒绝救援式占有"的重构弧线 |

## 保留与变更

### 保留
- 两位人物的全部已确认设定、戏剧功能、关系图、弧线、创伤线和场景出场。
- "南哥"昵称继续使用。
- 其他 97 位人物此次**不换名**。

### 变更
- 父亲（原"夏启明"）是否随女主改姓为"沈启明"由 CON-009 待确认，本次不动。
- 女主称谓：原女主名 → 沈知微；原"夏老师" → "沈老师"。
- 男主称谓：原男主名 → 陈浩南；口语"南哥"不变。

## 执行范围（本次落地）

**立即替换**（已完成，范围：`wiki/`、`drafts/chapters/`、`decisions/`、`reports/`、`outputs/`，共约 196 文件）：
- `wiki/characters/char-chen-haonan.md` 新建，`status: active / canon: confirmed`。
- `wiki/characters/char-shen-zhiwei.md` 新建，`status: active / canon: confirmed`。
- `wiki/characters/char-chen-zhaonan.md`、`char-xia-ziyan.md`：`status: deprecated`，顶部加迁移指针，正文保留历史迁移说明。
- 其他 Wiki 页中的旧 ID 双链和旧名文字全部更新。
- S1 第1章 `c001-sou-meeting.md` 正文中的旧名称谓同步替换；S1 c002–c018 旧稿（已 `rework-required`）仅字面同步，不改状态。
- 决策历史、报告、路线图中的旧名字面同步。

**暂不替换**（等后续批量正式扩写时统一）：
- `drafts/manuscript/latest.md` 完整校订版（旧名合计 3200+ 行）。
- `raw/` 原稿目录——**永久只读**，不替换。

**原因**：`latest.md` 是 S1 完整正文的真相基线，S1 V2 重写完成前，统一在扩写阶段换名；`raw/` 按项目规约永久保留原始证据。

## 待确认（CON-009）

1. 父亲“夏启明”是否随女主改姓为“沈启明”？
2. 其他 97 位人物中若有和主角辨识度冲突的（如 `char-shen-qing` 沈卿）是否需要调整？当前判断“沈卿”与“沈知微”同姓但名字差异大，不冲突。

## V4 追加（2026-10-09）

本决策部分被 `decisions/dec-20261009-013-v4-renaming-approval.md` 取代：

- 男主“陈浩南”及 ID `char-chen-haonan`：V4 沿用，仍然有效。
- 女主“沈知微” / ID `char-shen-zhiwei`：V4 最终定名为“沈雪瑶”，ID `char-shen-xueyao`。
- CON-009 父亲改姓：由 dec-013 决定为“沈启明”（父女同姓沈），本文件第 30、52 行的旧表述仅作历史保留。
