---
id: report-second-pass
type: report
title: 《我的荣耀》第二轮初始化报告（原稿封板 + 名词 Wiki 批量 + 去对照化）
status: active
canon: proposed
updated: 2026-10-10
tags: [report, review-required]
---

# 第二轮初始化报告

> 响应用户三条要求：**原稿封板**、**名词 Wiki 全量详化**、**改编版正文禁用"原××"对照**。

## 1. 原稿封板（AGENTS §2 兼容做法）

AGENTS.md §2 规定 `raw/` 永久只读，不得改原稿。所以采取"**保留原始指纹 + 产出封板版**"的做法：

- **SRC-20261010-001 原稿·初始导入版**（永久只读审计锚点）
  - `raw/manuscript/我的荣耀_全文原稿.md/.txt`
  - md5：`6ae0ab68...` / `53c6f91c...`
  - 不用于改编，用于版权 / 法律溯源
- **SRC-20261010-002 原稿·封板版**（改编工作唯一事实源）
  - `raw/manuscript/我的荣耀_原稿封板版.md`
  - md5：`0ddae7c5c2b1aabd055e65408575a732`
  - 747 章 / 2,009,562 字符
  - **封板后只读**

### 清洗清单（可审计，共 65 行真实变更）

1. **章节标题中的作者话括号**（12 处删除；保留"（1）/（大结局）"等结构化括号）
   - 第 20 / 24 / 37 / 59 / 60 / 61 / 64 / 78 / 80 / 90 / 113 / 604 章
2. **行内免责提示**（1 处删除）
   - 原第 708 行末 "（郑重提示……切记！切记！）"
3. **异常标点规范化**（6 条规则，~5 处触发）
   - `！{4,}` → `！！！`；`？{4,}` → `？？？`；`。{4,}` → `。`；`…{7,}` → `……`；`、{3,}` → `、`；`，{2,}` → `，`
4. **行末空白与多余空行**（纯格式整理）

**未动**：所有正文叙事、对白、人物称谓、剧情事件、章节编号与标题（除上述括号）；"我去年买了个表 / 厚颜无耻 / 半三更" 等人物口头禅与叙述习惯保留，作为人物声线资产。

## 2. 名词 Wiki 全量详化（83 内容页）

每个名词单独文件 + 详细背景。所有页 `canon: proposed`，等 ACK 后统一升级。

| 类别 | 数量 | 覆盖 |
|---|---|---|
| 核心人物 | 24 | 主角 / 父母 / 四女主 / 兄弟团 / 军师 / 鬼组 / 五大反派 / 项老 / 女警 |
| 组织 | 17 | 天下会 / 鬼组 / 海迪 / 狼舞 / 白袍会 / 忠信帮 / 飞鸿帮 / 天一集团 / 神龙基地 / 青帮 / 青花会 / 五大家族 + 议会 |
| 地点 | 10 | 蓉城全域 + 蓉城五区 + 青城山 + 神龙基地 + 京畿胡同 + 听澜轩 |
| 术语 / 系统 | 10 | 紫微斗数 / 杀破狼 / 北辰 / 十二段锦 / 十重天宫 / 一级药剂 / 洛神赋 / 灵魂 App / 吃讲茶 / 挑战赛积分 |
| 物件 | 11 | 乌银手链 / 十二段锦注 / 黄铜算盘 / 红酒瓶残片 / 五家令牌 / 龙鳞袖章 / 鬼组耳钉 |

### 每页包含的详化维度（short-drama 友好）

- **人物页**：身份 / 年龄 / 身高 / 体格 / 外貌（含标识疤 / 装束）/ 职业 / 原生家庭 / 背景故事 / 性格剖面 / 口头禅 / 能力线（分阶段）/ 弧线（S1-S6）/ 短剧改编锚点（外形 / 动作 / 声线 / 道具）
- **组织页**：历史渊源（引用 kb）/ 故事定位 / 创立者 / 大本营 / 组织结构 / 门规 / 规模 / 识别标志 / 短剧改编锚点
- **地点页**：真实原型（kb 虚构化规则）/ 故事定位 / 关键细节 / 短剧改编锚点
- **术语 / 系统页**：类型 / 真实依据（kb 文献）/ 本作设定
- **物件页**：用途 / 定位 / 细节 / 戏剧功能

### 覆盖知识库

人物与组织页的背景字段都在适当位置引用了 `common/knowledge-base/`：
- 紫微斗数 → `philosophy/mythology-and-folk-belief.md`
- 道家十二段锦 → `philosophy/daoism.md`
- 淮军 / 湘军 / 漕运 / 内务府 → `history/late-qing.md`
- 北洋军统 → `history/republican-china.md`
- 洪门 / 青帮 / 哥老会 → `jianghu/secret-societies.md`
- 吃讲茶 → `jianghu/etiquette-and-rules.md`
- 军事 → `crafts/military-special-forces.md`
- 医药上限 → `crafts/medicine-pharmacology.md`
- 武学硬上限 → `crafts/martial-arts.md`
- 真实地名虚构化 → `geography-folk/real-to-fictional-map.md`

## 3. 改编版去对照化（代入性要求）

**彻底去除"原××"对照** 的范围：

- ✅ wiki/overview.md
- ✅ wiki/characters/*（23 个人物页，全部按"全新小说"叙述）
- ✅ wiki/factions/*（17 个组织页）
- ✅ wiki/locations/*（10 个地点页）
- ✅ wiki/terms/*、wiki/objects/*
- ✅ decisions/DEC-001 / 002 / 003（决策记录体裁必须的"从什么改到什么"句式已抽象化）
- ✅ reports/REP-20261010-001 已有的内容结合第二轮重写

**保留"原××"对照** 的位置（**不进 review 视野**）：

- `wiki/continuity/continuity-naming-map.md`（标注 `internal-only`；仅供 continuity-agent 对账与 lint 使用；S1 稳定后迁入 `.archive/`）
- `wiki/log.md`（审计日志，合规必要）
- `wiki/sources/source-inventory.md`（源指纹，审计必要）

## 4. 校验结果

| 检查 | 结果 |
|---|---|
| wiki lint | 83 内容页 / 92 total / **0 errors / 0 warnings** |
| story graph | 93 nodes / 92 edges / **0 orphans** / closed |
| 对照残留扫描 | 仅 continuity-naming-map / log / source-refs 三处（审计必要） |

## 5. Review 入口建议

**先按角色层级 review**，再按组织、再地点、再术语。建议入口：

1. **主角组**：[顾北辰](file:///../characters/char-gu-beichen.md) → 父亲 顾崇岳 → 母亲 裴云归
2. **情感线**：[温书宁](file:///../characters/char-wen-shuning.md) → 叶浅浅 → 霍凝烟 → 裴青鸾 → 季婉宁
3. **兄弟团 / 军师**：[程星野](file:///../characters/char-cheng-xingye.md) → 贺九思 → 洪四海 → 宁云疏 → 卜立国 → 贺飞鸿
4. **反派**：[厉擎苍](file:///../characters/char-li-qingcang.md) → 厉天鸿 → 秦枭 → 韩啸天 → 肥猫
5. **核心组织**：[五家议会](file:///../factions/fac-five-families-council.md) → 顾/霍/裴/秦/韩 五家 → 天下会 → 鬼组 → 神龙基地 → 青花会

## 6. 待 ACK（与第一轮一致，不重复）

- DEC-001 主角定名顾北辰 + 五大家族文脉
- DEC-002 组织名保留 + 补渊源
- DEC-003 S1-S6 分卷骨架
- 原稿封板版（SRC-002）作为改编唯一事实源
- 原稿权利状态最终确认
