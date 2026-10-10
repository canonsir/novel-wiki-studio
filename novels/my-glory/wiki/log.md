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

## [2026-10-10] decision | 青帮 → 青龙帮（DEC-004）

- Sources:
  - 用户决议：青帮 → 青龙帮
  - 合规约束：national-redlines §48 / platform-redfruit §49（真实历史组织名"青帮"必须虚构化）
- Added:
  - wiki/factions/青龙帮.md（id: fac-qinglong-bang, slug: 青龙帮；新增"四堂"分部与"三不"门规）
  - decisions/DEC-20261010-004-qingbang-to-qinglong-bang.md（accepted）
- Updated:
  - wiki/characters/{厉擎苍, 秦枭, 厉天鸿, 宁云疏}.md 内文"青帮"→"青龙帮"
  - wiki/factions/天一集团.md、wiki/index.md、novel.yaml 同步
  - wiki/continuity/continuity-naming-map.md 对账追加
  - reports/REP-20261010-004-qingbang-rename.md 追加「用户决议」小节
- Deleted:
  - wiki/factions/青帮.md
- Contradictions: 无
- Decisions needed: 本条已完成；REP-003 §3 剩余 3 项（天下会 / 天一集团 / 神龙基地）仍挂起但非必改

## [2026-10-10] decision | 创作定调：逆袭+升级+爽文+后宫（画面感代偿）DEC-005

- Sources:
  - 用户决议：红线必须守住，但用"画面感+点到即可"替代一刀切；创作重心推向"主角逆袭+打怪升级+爽文+后宫"
  - wiki/world/敏感红线预防清单·开写前.md（原稿敏感规模统计）
  - common/constraints/genre-profiles/urban-male.md
- Added:
  - decisions/DEC-20261010-005-creative-pivot-rush-harem.md（accepted）
  - wiki/world/爽点节奏保障方案.md（四联坐标系 + 单章爽点模板 + 打脸类型六分法 + 后宫张力管理 + 画面感代偿笔法库 + 每章 lint 清单 + 每卷节奏总把关）
- Updated:
  - wiki/world/敏感红线预防清单·开写前.md §2.9 新增"画面感代偿笔法"章节（统一收敛哲学 / 对比样本表 / 关门镜头六法 / 独占不碰身原则 / 爽点加码补偿规则）
  - novel.yaml narrative.tone 增加"画面感收敛 / 后宫张力 / 逆袭打脸 / 打怪升级"；reader_promise 升级为"都市逆袭+打怪升级+后宫爽文"；core 新增 creative_pivot 块（四轴 + 代偿模式）
  - wiki/overview.md 读者承诺段改写为四联坐标 + 收敛哲学三条
  - wiki/index.md 新页上架；Reports/Open Questions 更新 DEC-004/005 已 ACK
- Contradictions: 无
- Decisions needed:
  - author-agent 开写时必须 reference 爽点节奏方案 + 敏感红线清单两份
  - reviewer-agent 发布前对照"画面感收敛是否到位 / 爽点节奏是否达标"

## [2026-10-10] expand | S1 c001 正式开写 + 人物称谓防漏改索引

- Sources:
  - 用户决议：进入正式改编；特别要求"上下文/钩子/伏笔要逻辑严谨+人物别名(小名/外号/简称)不得漏改"
  - raw/manuscript/我的荣耀_原稿封板版.md 第 1 章原稿
  - DEC-20261010-005 创作定调（画面感 + 爽文四联）
- Added:
  - wiki/continuity/人物称谓全索引·防漏改.md：按主角/亲族/女主/兄弟/反派/鬼组/组织/地点 列全称谓 + 禁止词 + 乱入高危词清单；S1 定稿前必 0 命中的禁词 grep 清单
  - wiki/characters/温景同.md：温书宁父亲人物页（新定名）；S1 麦高芬 500 万赌债载体；下毒戒毒走关门镜头
  - drafts/chapters/s1-city-south/c001-漂流瓶.md：S1 第 1 章正式改编稿 3700 字
- Updated:
  - drafts/manuscript/latest.md：S1 第 1 章正文入库
  - wiki/characters/温书宁.md：父亲名定为"温景同"（原"温父"占位名废弃）；延伸链指向新页
  - wiki/index.md 挂新页（Continuity + Characters 段）
  - graph/story-graph.json 重建（100 nodes / 108 edges / 1 chapter / 0 orphans / closed）
- Contradictions: 无
- Decisions needed:
  - c002 续写方向：温书宁递的叠纸条内容揭开 + 咖啡厅里"九头兽戒指"反派（厉擎苍）露面
  - 伏笔链"九头兽戒指"（相柳意象）与"北辰 + 杀破狼"命盘主轴的衔接方式（editor-agent 待压测）
- Rush anchors（c001 落稿清单）:
  - [x] 画面感代偿：仙人跳威胁用"折叠刀侧挎包 + 后门绕前门 + 五秒停顿"外化（原稿裸写被改）
  - [x] 女性物化：主角内心独白对温书宁 0 处物化（与原稿第 1 章对比重大改动）
  - [x] 粗口上限：全章仅"我去年买了个表"口头禅 4 次；无三字性器官型辱骂
  - [x] 爽点锚点 ≥ 3：开场身份错位 / 识破仙人跳 / 认出美女老师 / 发现九头兽戒指
  - [x] 章末钩子：九头兽戒指（下章揭厉擎苍）
  - [x] 新名 lint：正文零命中禁词（对账说明段除外）

## [2026-10-10] expand | c001 叙事机制升级：漂流瓶 → 灵魂 App 瞬间三件套

- Sources:
  - 用户决议："不要用漂流瓶，不是已经规定好有灵魂 app 了吗？漂流瓶太老气了"
  - wiki/terms/灵魂App.md 已有虚构品牌定义
- Added:
  - 灵魂 App 核心玩法三件套定稿：**瞬间 + 星球广场 + 灵魂回响**，加 **灵魂约见** 中间坐标机制
  - 行星昵称体系（白鹿=温书宁、北辰=顾北辰默认未改、冥王星/土星头像）
- Updated:
  - wiki/terms/灵魂App.md：完整定义四件套玩法；新增"废弃叙事（禁用）"表格（漂流瓶 / 摇一摇 / 附近的人 / 回电话号码 均禁用）；叙事口径升级说明
  - wiki/continuity/人物称谓全索引·防漏改.md：禁止词清单追加"漂流瓶 / 捞瓶子 / 扔瓶子 / 摇一摇 / 附近的人 / 回电话号码"
  - drafts/chapters/s1-city-south/c001-白鹿的瞬间.md（重命名自 c001-漂流瓶.md）：全章重写入口机制
    * 原稿"捞漂流瓶"→改为"刷星球广场"
    * 原稿"回电话号码"→改为"按住灵魂回响录制键 60 秒"
    * 原稿电话约见→改为"接光 + 同轨 + 灵魂约见 + 中间坐标"
    * 新增爽点锚点：主角识破"中间坐标被操纵"（反派对灵魂 App 后台的某种访问权限）
    * 章末钩子加码：九头兽戒指的主人**同时也在刷那条瞬间**（屏幕扣下前"暗紫+星光蓝"配色一秒认出）
  - drafts/manuscript/latest.md：同步新文本
  - graph/story-graph.json 重建（100 nodes / 108 edges / 1 chapter / 0 orphans / closed）
- Contradictions: 无
- Decisions needed:
  - c002 续写：如何揭开"中间坐标被操纵"的技术线（厉家是否已入股灵魂 App 母公司"灵枢科技"？）；此伏笔对 S2-S3 "青龙帮技术线" 的连接
  - 鬼组霍凝烟后期用灵魂 App 接触主角时，代号从"叉"升级为行星昵称——是否沿用"叉"？（editor-agent 待压测）

## [2026-10-10] expand | S1-S6 拆为 16 Arc + Arc 1 剧情图谱 + 目录重排

- Sources:
  - 用户决议："按照故事情节分类，分为 n 部，根据文件夹分类，方便后续转 AI 短剧"
  - DEC-20261010-005 创作定调（短剧改编友好）
  - raw/manuscript/我的荣耀_原稿封板版.md 第 1-30 章
- Added:
  - wiki/plot/短剧Arc分段骨架.md：S1-S6 → 16 Arc 分段表（30 章/arc）+ 文件夹映射 + 短剧改编元数据规范
  - wiki/plot/arcs/Arc1-女神与仙人跳-图谱.md：Arc 1 剧情图谱（c001-c030）
    * mermaid 剧情主流程图（27 节点 / 开场 → 结局钩子）
    * mermaid 关系图（POV 圈 / 女主圈 / 反派圈 / 伏笔 / 道具 / 法律灰度）
    * 爽点锚点节奏表（30 章 7 次公开打脸 + 画面感代偿映射）
    * 短剧改编预估（10-12 集 + 拍摄锚点 + 可拍/不可拍清单）
  - drafts/chapters/s1a-encounter-trap/README.md：Arc 1 目录元数据
  - 15 个新 Arc 目录（s1a → s6c）
- Updated:
  - wiki/plot/structure-plot.md：卷级骨架标注"升级"，目录名权威转交给 arc 骨架页
  - wiki/index.md：挂上 arc 骨架 + Arc 1 图谱
  - drafts/chapters/*：旧 s1-city-south 等 6 卷级目录 → 16 arc 级目录
  - c001-白鹿的瞬间.md：从 s1-city-south 迁入 s1a-encounter-trap
  - scripts/lint_story_graph.py：load_expected_arcs 支持 arc 级 slug（s1a / s2b 等）+ 优先读 arc 骨架页
  - graph/story-graph.json 重建（102 nodes / 110 edges / 1 chapter / 0 orphans / closed）
- Deleted:
  - 6 个旧卷级目录（s1-city-south / s2-city-east / s3-tianxia-hui / s4-shenlong / s5-didu-menfa / s6-glory-endgame）及其 .gitkeep
- Contradictions: 无
- Decisions needed:
  - Arc 1 c002-c030 细纲（editor-agent 按 arc 内 30 章做 scene-level 展开）
  - Arc 1 → Arc 2 过渡逻辑：500 万代偿协议 + 顾崇岳帝都电话 的双钩子如何在 Arc 2 c031 启动

## [2026-10-10] decision | 原著烂尾授权：结尾完全重构 + 篇幅扩展（DEC-006）

- Sources:
  - 用户决议："原著的小说结尾是烂尾草草收尾的，所以我们这次改编重构小说完全可以丰富、扩展、合理的闭环小说故事"
  - raw/manuscript/我的荣耀_原稿封板版.md 第 700-747 章（原稿烂尾位）
- Added:
  - decisions/DEC-20261010-006-ending-reconstruction-authorized.md（accepted；三方向待 ACK）
  - wiki/plot/S5-S6结尾重构·方向简报.md：三方向 pitch（A 传统爽文 / B 真实文脉 / C 双层结局推荐）
- Updated:
  - novel.yaml:
    * planned_length_words: 2500000 → 3000000
    * planned_volumes 注释：章节区间非硬约束
    * boundaries.ending_constraints 新增：伏笔必闭 / 主题必答题 / 后宫明确归宿
    * boundaries.ending_reconstruction：三方向 + ACK pending
  - wiki/overview.md：Open Questions 增加 DEC-004/005/006 ACK 状态；新增"结尾重构授权"段
  - wiki/index.md：挂新页 + Open Questions 更新
- Contradictions: 无
- Decisions needed:
  - 用户选择结尾方向（A/B/C/自定义）
  - 用户 ACK 篇幅上限（300 万 vs 350 万）
  - 用户 ACK 后宫归属原则

## [2026-10-10] decision | 结尾方向定稿：方向 C 双层结局（DEC-007）

- Sources:
  - 用户 ACK："C 双层结局"
  - DEC-20261010-006 原著烂尾授权
  - wiki/plot/S5-S6结尾重构·方向简报.md 方向 C pitch
- Added:
  - decisions/DEC-20261010-007-ending-direction-C-finalized.md（accepted）
  - drafts/chapters/s6b-ghostorg-reform/（新增 Arc 15 目录）
  - drafts/chapters/s6d-council-reform/（新增 Arc 17 目录）
- Updated:
  - wiki/plot/短剧Arc分段骨架.md：S6 从 3 Arc 扩为 5 Arc；总 Arc 16 → 18；章节区间扩展到 c900
  - wiki/plot/structure-plot.md：卷级表 S6 更新为 5 Arc / c641-c900
  - wiki/overview.md：
    * 分卷幕结构表更新（新增 Arc 数列）
    * Open Questions 更新 DEC-004/005/006/007 ACK 状态
    * 新增"结尾方向定稿（DEC-007）"段：固化 终章场景 / 后宫归属 / 主题答题
  - novel.yaml:
    * ending_reconstruction.status: user_ack_pending → accepted
    * direction: C-双层结局
    * s6_arc_expansion（5 项）
    * harem_outcome（principal_wife=温书宁 / independent_partners / lifelong_bonds）
    * final_scene_lock（听澜轩阳台 + 顾北辰/温书宁/顾崇岳 + 九头兽戒指+北辰令合铸）
  - wiki/index.md Open Questions 更新
- Renamed:
  - drafts/chapters/s6b-hanxiaotian-end → s6c-hanxiaotian-end
  - drafts/chapters/s6c-glory → s6e-glory
- Contradictions: 无
- Decisions needed:
  - S6 五 Arc 的 scene-level 细纲（S5 完成后 editor-agent 推进）
  - 跨境雇佣兵组织命名（Arc 14 核心对手；可用虚构国家代号）
  - 国家监察机构命名（Arc 17 新引入角色所属）

## [2026-10-10] decision | 女性角色改名·性别读感修正（DEC-008）

- Sources:
  - 用户决议："霍惊鸿这个名字我以为是个男的，类似的问题，都需改一下"
  - 用户 ACK："1、霍凝烟 2、B（整体方案 B 全部改）"
  - REP-20261010-005 女性角色命名评估报告
- Added:
  - decisions/DEC-20261010-008-female-rename.md（accepted）
  - reports/REP-20261010-005-female-naming-review.md
- Renamed:
  - wiki/characters/霍惊鸿.md → wiki/characters/霍凝烟.md（id: char-huo-jinghong → char-huo-ningyan）
  - wiki/characters/季繁星.md → wiki/characters/季婉宁.md（id: char-ji-fanxing → char-ji-wanning）
  - wiki/characters/穆清.md → wiki/characters/穆清岚.md（id: char-mu-qing → char-mu-qinglan）
- Updated:
  - 27 个文件内全文替换：霍惊鸿→霍凝烟 / 季繁星→季婉宁 / 穆清→穆清岚
  - 典故保护：单独"惊鸿"（《洛神赋》"翩若惊鸿"4 处典故引用）**未**替换
  - wiki/characters/季婉宁.md 第 28 行：艺名立意升级为"翩若惊鸿，婉若游龙"全句，名实呼应婉宁
  - wiki/continuity/continuity-naming-map.md：追加本次改名条目
  - wiki/continuity/人物称谓全索引·防漏改.md：
    * 三人允许称谓重排（阿烟 / 阿婉 / 烟姐 / 婉姐 等）
    * 禁止词清单追加（霍惊鸿 / 惊鸿-人名 / 季繁星 / 繁星 / 穆清-单独）
- Contradictions: 无
- Decisions needed:
  - c002 开写前再做一次全库扫一遍，确认 0 残留

## [2026-10-10] expand | 全书大纲总览 + 占位页填实（开写前最后一张图）

- Sources:
  - 用户决议："小说整体大纲好了吗？人物大纲关系图、故事发展线、人物组织故事拓扑图等等，先看到完整的大概，然后进入改编"
  - 已固化决议 DEC-001 到 DEC-008
- Added:
  - wiki/plot/全书大纲总览.md：
    * 全书元参数固化表（10 条）
    * Mermaid 图 1 · 人物组织故事拓扑（主角圈 / 后宫 / 主角阵营 / 五家议会 / 反派 / 辅助势力，含血缘 / 情感 / 兄弟 / 阵营 / 家族 / 议会 / 反派链）
    * Mermaid 图 2 · 全书故事发展线（S1-S6 时间轴 + 终章）
    * 18 Arc 单元细节表（含每 arc 核心对手 / 新角色 / 结局钩子）
    * Mermaid 图 3 · 命盘杀破狼与伏笔收束（S1-S4 伏笔 → S5-S6 收束位置）
    * Mermaid 图 4 · 六位女主弧线归属（timeline 图）
    * 关键待确认事项（已 ACK / 可延后 ACK）
    * 开写路径建议
- Updated:
  - wiki/relationships/relationship-matrix.md：从 17 行占位页扩至完整
    * 主角圈内信任链（6 对）
    * 女主圈情感（9 对）
    * 反派圈对抗（7 对）
    * 兄弟 / 组织内部（5 对）
    * 关键 Arc 张力进场点表
  - wiki/clues/clue-ledger.md：从 17 行占位页扩至完整
    * Arc 1 c001 已种 6 条伏笔
    * S1 其他 Arc 待种 7 条
    * S2-S4 待种 6 条
    * S5-S6 终局 5 条
    * 共 24 条伏笔 + 收束检查矩阵
  - wiki/timeline/timeline-master.md：从 23 行占位页扩至完整
    * 骨架时间线 T-20Y → T+3.5Y（全书故事线 3.5 年）
    * 五家议会春分/秋分正会锁定
    * 真实历史背景节点
  - wiki/index.md：挂新页 + 升级 S5-S6 简报状态为 accepted(方向C)
- Contradictions: 无
- Decisions needed:
  - 用户 ACK 本总览图谱 → 开 c002
  - 可延后 ACK：贪狼/七杀人物 / 跨境雇佣兵名 / 国家监察机构名

## [2026-10-10] decision | 命盘三星 + 穷奇旅 + 玄鉴台 命名固化（DEC-009）+ 小说改名候选报告

- Sources:
  - 用户决议："不要延后，直接前期定好，后续可以补充修改"
  - 用户决议："小说名字帮我推荐重新起一个"
  - DEC-20261010-007 结尾方向 + 全书大纲总览第七节原延后项
- Added:
  - decisions/DEC-20261010-009-sanxing-mercenary-watch-naming.md（accepted）
    * 杀破狼三星定稿：破军=贺九思 / 贪狼=洪四海 / 七杀=程星野
    * 跨境雇佣兵：穷奇旅（山海经四凶之"穷奇"，善辨逆顺吃忠厚人）
    * 国家监察机构：玄鉴台（玄+鉴+台；暗合项玄冥"玄"字伏笔）
  - wiki/factions/穷奇旅.md：组织结构 + 剧情功能 + 短剧改编锚点
  - wiki/factions/玄鉴台.md：三司架构 + 项玄冥伏笔链 + Arc 17 进场
  - reports/REP-20261010-006-novel-rename-pitch.md：小说改名候选报告
    * 原名《我的荣耀》诊断（5 维度）
    * 15 个候选书名（命理/逆袭/组织/爽文四条路线）
    * 作者 TOP 3 强推（众星拱北辰 / 北辰令 / 老师北辰来接光了）
    * 推荐方案 B 双名双发（小说+短剧各一名）
- Updated:
  - wiki/terms/杀破狼.md：三星定稿表 + 入场章 + 聚齐节奏
  - wiki/plot/全书大纲总览.md：命盘图"★待定"→ 实名；第七节 ACK 清单升级
  - wiki/plot/短剧Arc分段骨架.md：Arc 14 核心对手"穷奇旅九尾"；Arc 17 新引入"玄鉴台代表+项玄冥呼应"
  - wiki/index.md：
    * Factions 段 新增 玄鉴台 / 穷奇旅
    * Open Questions 新增 DEC-009 已 ACK + REP-006 待 ACK
- Contradictions: 无
- Decisions needed:
  - 用户选小说新名（方案 A/B/C/D）

## [2026-10-10] expand | 番茄榜单命名规律参考 + 新候选书名 D 方案

- Sources:
  - 用户决议："参考下番茄平台的小说命名"
  - 番茄 web 榜单页抓取为空（SPA），改用番茄男频都市/爽文/后宫 2024-2026 爆款规律总结
- Added:
  - reports/REP-20261010-007-fanqie-naming-ref.md：
    * 番茄爆款命名 8 条规律（所属格 / 反差型 / 超长信息密度 / 身份转换 / 单字名 / 文脉前缀 / 后宫暗示 / 反问号）
    * 12 个按规律重新设计的候选书名（分 ABCDE 5 组）
    * 作者 TOP 3 新强推：
      1. 《北辰诀》（文脉爆款型，⭐⭐⭐⭐⭐）
      2. 《我爸把我扁担赶出家门，没想到我成了五家议会之首》（短剧爆款型）
      3. 《众星拱北辰》（后宫群像型）
    * 新方案 D：《北辰诀》正名 + 短剧长名双发
- Updated: n/a
- Contradictions: 无
- Decisions needed:
  - 用户在 A/B/C/D/E 中选小说新名

## [2026-10-10] expand | 书名重做·按读者点击动机驱动（REP-008）

- Sources:
  - 用户反馈："不好听，没有吸引力，读者看到后都没有动力点进来看"
  - 复盘：前两轮候选过度文脉化 / 无具体身份词 / 无情感钩 / 无反差冲突词
- Added:
  - reports/REP-20261010-008-naming-click-driven.md
    * 复盘前两轮推荐问题（4 条）
    * 本作核心点击钩子排序（师生/豪门隐藏/反杀/扁担/后宫）
    * 15 个按真爆款规律重做候选（A 师生/B 豪门隐藏/C 反杀/D 混合钩 4 组）
    * 作者 TOP 5 新强推：
      1. 《温老师的匿名瞬间，被我接光了》
      2. 《装了二十年废物，直到五家议会把我接回去》
      3. 《被爸用扁担赶出家门，没人知道我爸是京圈顾氏》
      4. 《在三流大专装了两年废物，直到老师给我发了条匿名瞬间》
      5. 《开局反杀校董之子，没想到我老师是他未婚妻》
    * 新方案 F/G/H（替代 A/B/C/D）
    * 方案 G 双名双发：番茄长篇型 + 红果短剧吸粉型
    * 前两轮文脉词（北辰诀 / 众星拱北辰 / 北辰令）转为内文卷名 / 章名 / 终章词 保留
- Updated: n/a
- Contradictions: 无
- Decisions needed:
  - 用户在 F/G/H/15 候选自选 / 自定义 中选小说新名
