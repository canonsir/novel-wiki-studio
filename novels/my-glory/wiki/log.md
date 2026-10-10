# Change Log

## [2026-10-10] ingest | 《我的荣耀》改编初始化

- Sources:
  - raw/manuscript/我的荣耀_全文原稿.md（747 章；md5 6ae0ab68dfe53c580958091d4e9f8da8）
  - raw/manuscript/我的荣耀_全文原稿.txt（md5 53c6f91cbb3e5c05960f8fb0e86d121d）
  - raw/references/REF-20261010-001-feishu-adaptation-guli-beichen.md（飞书 docx Wc6gdR6QKoIf1uxBJu0cEbGfnAc revision 13 快照）
- Added:
  - novels/my-glory/novel.yaml（填充 genre / platform / kb_dependencies / genre_profile=urban-male / raw_manuscript 指纹）
  - wiki/overview.md（初始化总览，canon: proposed）
  - wiki/sources/source-inventory.md
  - wiki/world/structure-naming-map.md（原名→新名总映射，lint-required）
  - wiki/characters/{char-gu-beichen, char-wen-shuning, char-li-qingcang, char-cheng-xingye}.md
  - wiki/factions/fac-five-families-council.md
  - wiki/locations/loc-rong-city.md
  - wiki/plot/structure.md（S1-S6 分卷骨架）
  - wiki/index.md（挂上所有新页）
  - decisions/DEC-20261010-001-protagonist-naming-guli-beichen.md（proposed）
  - decisions/DEC-20261010-002-organization-names-preserve.md（proposed）
  - decisions/DEC-20261010-003-volume-structure.md（proposed）
- Updated: n/a（首次初始化）
- Contradictions:
  - 原稿第 1 章使用真实地名"龙王桥"等——需按 kb/china/geography-folk/real-to-fictional-map.md 虚构化。
  - 原稿主角母亲姓氏（赵）与改编版（裴云归）冲突——由 DEC-20261010-001 调整，列为 continuity 项。
  - 原稿存在直接可复刻的违法细节（下毒、老千、暴力威胁话术）——继承《情陷美女老师》的三层发布收敛策略，待 reviewer-agent 过 checklist。
- Decisions needed（等用户 review 后 ACK，才升级 confirmed）:
  - DEC-20261010-001 主角定名顾北辰 + 五大家族文脉
  - DEC-20261010-002 组织名保留原名 + 补真实渊源
  - DEC-20261010-003 S1-S6 分卷骨架
  - 来源权利状态最终确认

## [2026-10-10] ingest / expand | 原稿封板 + 名词 Wiki 批量落地（第二批）

- Sources:
  - 新增 SRC-20261010-002：raw/manuscript/我的荣耀_原稿封板版.md（747 章 / md5 0ddae7c5c2b1aabd055e65408575a732）
- Added:
  - raw/manuscript/我的荣耀_原稿封板版.md（新封板版）
  - wiki/characters/*.md 新增 20 个（共 23 个核心人物页，每页含年龄/身高/外貌/职业/背景/性格/能力/弧线/短剧改编锚点）
  - wiki/factions/*.md 新增 17 个（天下会 / 鬼组 / 海迪 / 狼舞 / 白袍会 / 忠信帮 / 飞鸿帮 / 天一集团 / 神龙基地 / 青帮 / 青花会 / 顾霍裴秦韩 五家 / 五家议会）
  - wiki/locations/*.md 新增 10 个（蓉城全域 + 五区 + 青城山 + 神龙基地 + 京畿旧城胡同 + 听澜轩）
  - wiki/terms/*.md 新增 10 个（紫微斗数 / 杀破狼 / 北辰 / 道家十二段锦 / 十重天宫 / 一级药剂 / 洛神赋 / 嗖匹配 / 吃讲茶 / 挑战赛积分）
  - wiki/objects/*.md 新增 11 个（乌银手链 / 十二段锦注手抄本 / 黄铜算盘 / 红酒瓶残片 / 五家令牌 / 龙鳞袖章 / 鬼组耳钉）
- Updated:
  - wiki/sources/source-inventory.md（SRC-002 封板版登记，含清洗清单与 md5）
  - novel.yaml（raw_manuscript 升级为 initial_import + sealed 双指纹）
  - wiki/overview.md（彻底移除"原××"对照）
  - wiki/characters/char-gu-beichen / char-wen-shuning / char-li-qingcang / char-cheng-xingye（4 个核心人物页去对照化 + 详化）
  - wiki/world/structure-naming-map.md → wiki/continuity/continuity-naming-map.md（映射表降级为内部对账用，正文禁用）
  - wiki/index.md（按新结构全面重建；83 内容页上架）
  - decisions/DEC-20261010-001（Consequences 去对照化）
- Contradictions resolved:
  - "原××"对照全面退出 Wiki 正文、人物页与 overview（仅保留 continuity-naming-map 内部对账 + log 审计 + source-refs 文件名）
- Decisions needed:
  - 继续等 DEC-001 / DEC-002 / DEC-003 的用户 ACK
  - 原稿封板版（SRC-002）作为后续改编唯一事实源，等用户 ACK
