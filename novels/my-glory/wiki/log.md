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

## [2026-10-10] ingest | 原稿封板 + 名词 Wiki 批量落地（第二批）

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

## [2026-10-10] setup | 名词页中文文件名 + slug 索引字段

- Added:
  - scripts/lint_wiki.py 支持 slug 字段：若 frontmatter 含 slug 则 filename == slug，否则 filename == id
- Updated:
  - wiki/characters / factions / locations / terms / objects 共 71 页：文件名改为中文 title（如 顾北辰.md）；frontmatter 新增 slug 字段 == 文件名 stem；id 字段保留 kebab-case 作稳定索引（图谱 / AI 用）
  - 全 wiki 与 decisions 中的 wikilink 与路径引用同步到中文
  - wiki/index.md 重建到中文文件名
- Rationale: 中文文件名提升人工 review 效率；kebab-id 继续用作图谱和脚本的稳定键

## [2026-10-10] ingest | 山海经与玄幻武侠修炼知识库 + 命名候选桥页

- Sources:
  - common/knowledge-base/china/philosophy/shanhaijing.md（新增，九卷结构 / 主要神祇 / 异兽 / 地名 / 可取材命名清单）
  - common/knowledge-base/crafts/xianxia-xuanhuan-cultivation.md（新增，境界 / 功法 / 门派 / 法宝 / 丹药 / 阵法 / 剑意 骨架）
- Added:
  - wiki/world/命名候选·山海经与修炼体系.md：桥页，把 kb 的素材连接到本书人物外号 / 组织堂口 / 功法境界 / 法宝物件候选
- Updated:
  - novel.yaml kb_dependencies +shanhaijing +xianxia-xuanhuan-cultivation（共 23 条）
  - common/knowledge-base/README.md 目录树与成熟度表（philosophy 9 篇 / crafts 12 篇）
  - AGENTS.md §13.3 目录
  - wiki/index.md 加挂新桥页
- Contradictions: 无
- Decisions needed: 候选集中具体采信哪些外号 / 堂口名 / 功法名需用户 ACK 或 editor-agent 评审后入人物页 / 术语页

## [2026-10-10] decision | 嗖匹配 → 灵魂 App

- Sources:
  - 用户决议：嗖匹配是 Soul 音译拼音，怕平台识别；统一改为"灵魂 App"（直译）
  - 合规约束：common/constraints/national-redlines-checklist.md L48 / platform-redfruit-checklist.md L49 / platform-fanqie-checklist.md L17 / common/knowledge-base/crafts/entertainment-industry.md L16
- Added:
  - wiki/terms/灵魂App.md（id: term-soul-app, slug: 灵魂App）
- Updated:
  - wiki/characters/温书宁.md S1 Hook 段
  - wiki/overview.md 主线因果摘要
  - wiki/index.md terms 节
  - wiki/continuity/continuity-naming-map.md 对账记录
  - reports/REP-20261010-003-naming-review.md 追加「用户决议」与「迁移记录」小节
  - reports/REP-20261010-002-second-pass.md 术语清单
- Deleted:
  - wiki/terms/嗖匹配.md（过渡用名废弃）
- Contradictions: 无
- Decisions needed: 本条决议已完成；REP-003 §3 的另外 4 项（青帮 / 天下会 / 天一集团 / 神龙基地）仍挂起，S2 前必须决议青帮

## [2026-10-10] setup | 青帮改名候选扩充 + 开写前敏感红线预防清单

- Sources:
  - common/constraints/national-redlines-checklist.md 全量
  - common/constraints/platform-fanqie-checklist.md / platform-redfruit-checklist.md
  - raw/manuscript/我的荣耀_原稿封板版.md 全量敏感关键词扫描
- Added:
  - wiki/world/敏感红线预防清单·开写前.md：按 L1 不可触碰 / L2 必须收敛 / L2.5 风险场景三层整理；逐条给原稿样本 + 收敛策略 + 禁区示例 + 保留强度；并提供第 1-3 章 Hook 收敛样例
  - reports/REP-20261010-004-qingbang-rename.md：青帮改名候选扩充 12 个 + 我的新推荐 4 个（相柳堂 / 大通社 / 乾字门 / 河山会）
- Updated:
  - wiki/index.md 挂上两份新页
- Contradictions: 无
- Decisions needed:
  - 青帮改名：请从 REP-004 的 12 候选 or 4 推荐里挑选，或给自己的方案
  - 敏感红线清单仍 proposed，S1 开写前请你快速过一遍重点条目（见 §4 第 1-3 章 Hook 收敛样例）
