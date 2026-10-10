---
id: report-initialization
type: report
title: 《我的荣耀》自动化初始化报告（待 review）
status: active
canon: proposed
updated: 2026-10-10
tags: [report, initialization, review-required]
---

# 《我的荣耀》自动化初始化报告

> 本报告供用户 review；确认后在 `decisions/` 中 ACK 对应条目，所有 `proposed` 项统一升 `confirmed`，正式进入 editor-agent 搭 arc 阶段。

## 1. 输入材料

| 材料 | 位置 | 规模 / 指纹 | 处理 |
|---|---|---|---|
| 原稿 .md | `raw/manuscript/我的荣耀_全文原稿.md` | 747 章 / 5.7 MB / md5 `6ae0ab68...` | 只读导入 |
| 原稿 .txt | `raw/manuscript/我的荣耀_全文原稿.txt` | 5.7 MB / md5 `53c6f91c...` | 只读导入 |
| 飞书设定 | `raw/references/REF-20261010-001-...` | docx `Wc6gdR6Q...` revision 13 | 快照存档，视为 proposed |

> 原稿内容与归档书《情陷美女老师》同一文脉（主角原名陈照南、女主夏梓妍、反派李振北、兄弟张星——归档书用 V4"陈浩南/沈雪瑶"方案已不迁移，本次按飞书"顾北辰"方案重做）。

## 2. 已完成的 harness 初始化

### 2.1 新小说目录
- `novels/my-glory/`（从 `_template/` 冷启动，slug `my-glory`）。

### 2.2 novel.yaml 配置
- 填充：genre / target_platforms / content_rating / planned_length (250 万字) / planned_volumes (6)
- `creative_goal.source_rights`：**用户自有或已获合法授权（最终确认待签字）** ← 待 ACK
- `boundaries.must_keep` / `must_avoid` / `ending_constraints` 已落地
- `kb_dependencies`：接入 **19 条**知识库条目（紫微斗数 / 道家 / 淮军湘军 / 洪门袍哥 / 军事 / 医药 / 金融 / 娱乐圈 / 真实地名虚构化等）
- `genre_profile`：`urban-male.md`
- `raw_manuscript`：登记指纹

### 2.3 Wiki 初稿（18 内容页，canon: proposed）
- `overview.md` — 一句话故事 + 读者承诺 + 分幕 + 人物弧 + 悬念 + 待确认决策
- `sources/source-inventory.md` — SRC & REF 登记
- `world/structure-naming-map.md` — **全书原名→新名硬映射**（lint-required）
- `plot/structure-plot.md` — S1-S6 分卷骨架（含 arc slug）
- `factions/fac-five-families-council.md` — 五家议会（顾/霍/裴/秦/韩 + 真实历史根基）
- `locations/loc-rong-city.md` — 蓉城（原型成都，虚构化）
- `characters/`：顾北辰 / 温书宁 / 厉擎苍 / 程星野 四个核心人物页
- `index.md` — 全部页面上架

### 2.4 决策登记（proposed，等待 ACK）
- **DEC-20261010-001** 主角定名顾北辰 + 五大家族真实文脉（淮军/湘军/漕运/内务府/北洋）
- **DEC-20261010-002** 组织名保留原名 + 补真实渊源（天下会/鬼组/海迪/狼舞/白袍会/忠信帮/飞鸿帮/天一集团/神龙基地/青帮）
- **DEC-20261010-003** 分卷 S1-S6 骨架

### 2.5 Drafts 骨架
- `drafts/manuscript/latest.md` — 重构稿占位（author-agent 持写权限）
- `drafts/chapters/s1-city-south/` 至 `s6-glory-endgame/` 六个空卷

### 2.6 Harness 轻微修复
- `scripts/lint_story_graph.py`：原来硬编码的 arc 列表（上一本《情陷美女老师》的 s1-boundary-beyond 等）改为**从 `wiki/plot/structure-plot.md` 的 arc slug 表格自动读取**，支持多书。

### 2.7 校验结果
| 检查 | 结果 |
|---|---|
| `lint_wiki.py novels/my-glory` | 18 页 / 0 errors / 0 warnings |
| `build_story_graph.py novels/my-glory` | 26 nodes / 34 edges / 0 orphans |
| `lint_story_graph.py novels/my-glory` | ✅ closed |

## 3. 关键改编要点（简版，详见 Wiki）

### 主角定名
- **顾北辰（北哥）** — 出自《论语·为政》"北辰居其所而众星共之"；紫微斗数紫微帝星；命盘杀破狼聚齐构成"杀破狼为将、北辰为帝"伏笔。
- 道上称"北哥"（原"南哥" → 南北对转）。

### 五大家族（文脉版）
| 家 | 历史根基 | 现代业务 |
|---|---|---|
| 顾 | 淮军"铭"字营 + 洋务轮船招商局 | 中东能源 / 港口 / 煤炭矿产（主角本家） |
| 霍 | 清内务府皇商 / 御医 | 顶级医院 / 军医 / 医疗器械 |
| 裴 | 漕运世家 + 晋商票号 | 金融私募 / 文化传媒 / 拍卖 |
| 秦 | 北洋奉系 + 军统 | 安保 / 情报 / 雇佣兵 |
| 韩 | 湘军 曾国藩部曲 | 医药生物 / 临床审批 |

### 组织（保留原名+真实渊源）
天下会（洪门）/ 鬼组（锦衣卫粘杆处）/ 白袍会（袍哥）/ 青帮（上海）/ 神龙基地（黄埔式）等。

### 分卷
S1 蓉城·城南少年 → S2 城东三方 → S3 天下会 → S4 神龙身世 → S5 帝都门阀 → S6 荣耀终局。

### 人物命名（节选）
陈照南→顾北辰 / 夏梓妍→温书宁 / 杨雨诗→霍惊鸿 / 李振北→厉擎苍 / 张星→程星野 / 吕润海→洪四海（海哥，保留）/ 洛梦→季繁星。

### 地名
成都→蓉城 / 北京→帝都，按 `common/knowledge-base/china/geography-folk/real-to-fictional-map.md` 全面虚构化。

## 4. 已识别的矛盾与风险（continuity 需要回填）

- 原稿第 1 章使用真实地名"龙王桥"等 — 待建立蓉城虚构地名映射。
- 原稿主角母亲姓氏（赵）与改编版（裴云归）冲突 — 已登记。
- 原稿存在可复刻违法细节（下毒、老千、暴力威胁话术）— 已继承三层发布收敛策略，待 reviewer-agent 过 checklist。
- 女性物化 / 地域歧视表达（原稿语气）— 全书去 AI 化 + 去冒犯化改写，必须对齐番茄红线。

## 5. 需要用户 review 后 ACK 的事项

| # | 事项 | 关联决策 | 影响 |
|---|---|---|---|
| 1 | 主角名"顾北辰 / 北哥"方案 | DEC-001 | 全书人物称呼基线 |
| 2 | 五大家族"淮军 / 湘军 / 漕运 / 内务府 / 北洋"文脉锁定 | DEC-001 | 门阀世界观基线 |
| 3 | 组织名全部保留 + 补真实渊源 | DEC-002 | 全书组织辨识度 |
| 4 | S1-S6 分卷骨架（6 卷结构） | DEC-003 | 后续细纲规划起点 |
| 5 | 原稿权利状态确认 | novel.yaml.source_rights | 发布版路径 |
| 6 | 三层发布版本策略（番茄 / 红果漫剧 / 红果无尺度素材） | boundaries | 全书合规框架 |

## 6. ACK 后的下一步

1. 把三个 DEC 从 `proposed` 升 `confirmed`，Wiki 相关页同步升级。
2. 切 **editor-agent**：按 S1 骨架搭 30 章细纲。
3. 切 **grill-agent**：对 S1 细纲做压力测试（人物动机 / 资源来源 / 对手策略 / 代价 / 信息控制 / 连续性）。
4. 用户确认后切 **author-agent**：调用 `.trae/skills/writing/chinese-novelist/` 开写 c001。
5. 每章完成后：continuity-agent → reader-agent → reviewer-agent 的闭环检查。

## 7. 风险与边界

- **文学判断保留**：主题 / 结局 / 核心人物命运未在初始化阶段被锁定；DEC-003 的卷结构允许在细纲阶段微调（需另立 supersede）。
- **原稿爽感资产保留**：按 AGENTS.md §6 "原稿爽点属于待评估的剧情资产，不默认整段删除"，所有敏感段落走"降露骨 + 明确成年 + 自愿边界 + 弱化违法细节 + 补代价 + 调整镜头"的收敛路径。
- **知识库未就位领域**：紫微斗数专题目前靠 `philosophy/mythology-and-folk-belief.md` 兜底，S4 命盘线深入时如需单独条目，由 kb-extender 补。
