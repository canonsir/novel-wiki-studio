# Wiki Log

> 仅追加，不覆写。标题格式必须保持可解析。

## [2026-10-08] setup | 初始化小说 Wiki
- Sources: none
- Added: template structure
- Updated: none
- Contradictions: none
- Decisions needed: genre, audience, POV, core promise

## [2026-10-08] ingest | 导入首部待重构小说并建立结构基线
- Sources: SRC-20261008-001; SHA-256 86895912be4af16d394e3b698ed62cdee904b4d30fea5740433b22768d7337c0
- Added: source inventory, five character pages, reconstruction decision, ingest report
- Updated: novel config, overview, plot, timeline, relationships, clues, style, continuity
- Contradictions: missing chapters, duplicate/malformed chapter numbers, genre drift, external-rescuer ending, unconfirmed source rights
- Decisions needed: source rights, primary genre, core romance, ending consequences, target platform and length

## [2026-10-08] decision | 确认三线爽点为核心商业结构
- Sources: user confirmation; DEC-20261008-001
- Added: 三线爽点增长系统
- Updated: novel config, overview, plot, protagonist page, continuity report, ingest report
- Contradictions: corrected the prior over-constrained recommendation that would remove core escalation
- Decisions needed: relationship roster, escalation ceiling, patron boundaries, target platform

## [2026-10-08] query | 建立人物世界观与AI短剧知识层
- Sources: SRC-20261008-001; DEC-20261008-001; full-title and occurrence evidence scan
- Added: character arc bible, faction power map, location asset atlas, event spine, ability system, video visual bible, short-drama roadmap
- Updated: world bible, relationship matrix, overview
- Contradictions: detailed ages, injuries and chapter-level state transitions still require batch close reading
- Decisions needed: city fictionalization, visual casting direction, power-system realism, episode format and target platform

## [2026-10-08] expand | 补齐缺章并生成747章连续版本
- Sources: SRC-20261008-001; user ownership and authorization confirmation
- Added: reconstructed chapters 98, 100, 102, 557; numbered LLM views; complete continuity-restored manuscript
- Updated: source rights, reconstruction decision, continuity status, project README
- Contradictions: raw remains incomplete by design; reconstructed V1 has no missing or duplicate chapter numbers
- Decisions needed: target platform, deep-rewrite batch order, final relationship roster and power ceiling

## [2026-10-08] lint | 全文格式校订与中文知识视图重整
- Sources: reconstructed V1; author request
- Added: proofread V2, 747-chapter ledger, full editorial review
- Updated: numbered directories now contain readable Chinese world, character, plot, timeline, scene and video content instead of link-only indexes
- Contradictions: text-level fixes completed; plot-level reconstruction remains in 30 close-reading batches
- Decisions needed: target platform, relationship end state, power ceiling, city fictionalization

## [2026-10-08] ingest | 全量实体拆页
- Sources: proofread V2 full-text entity and occurrence scan
- Added: 88 character pages, 25 faction pages, 22 location pages, 15 term pages, 25 major event pages and five Chinese catalogs
- Updated: world, character and plotline entry pages; generated Wiki index
- Contradictions: ambiguous aliases are merged only when identity is stable; low-frequency candidates remain subject to close-reading verification
- Decisions needed: whether minor unnamed roles and one-scene businesses should receive persistent IDs

## [2026-10-08] query | 完善世界圣经、势力体系和关系线总表
- Sources: SRC-20261008-001; DEC-20261008-001; 全文实体扫描证据
- Added: 三层权力结构、经济四层体系、蓉城四区地理政治、地下规则与禁忌、15 个专有名词故事依据表；13 个主要势力的完整属性（创建时间、范围、核心人物、经济来源、规矩、弱点、关系）；主角核心关系线总表（6 条核心关系 + 兄弟群像，含阶段、转折点、潜在冲突）
- Updated: world-bible.md（完全重写）、faction-power-map.md（完全重写）、wiki/index.md
- Contradictions:
  - 术语名冲突：用户提及的"洛神符"与 Wiki 现有 term-luoshenfu.md 的"洛神赋"可能为同一原稿名词的不同写法，需逐章核验原文
  - 势力缺失：用户提及的"青龙会"在现有 25 个 faction 扫描中未找到对应条目，逐章精读时需重新扫描
  - 李家城西家族：有明确故事依据（李振北开篇动用城西势力），但缺少独立 faction 文件
  - 各区地盘边界：城东/城南/城北/城西的具体边界为推断，需逐章核验原文
  - 多处 canon 标注为 proposed 的推断需要后续精读确认
- Decisions needed:
  - 蓉城 vs 成都 架空名正式化决策
  - "洛神符/洛神赋"术语名统一
  - 是否为李家城西家族、青龙会创建独立 faction 文件
  - 五大家族差异化产业/价值观细节的精读确认
  - 所有 proposed 推断的精读核验

## [2026-10-08] expand | 第一批深度重写（第1-5章风格标杆）
- Sources: reconstructed V2 baseline; batch-01-plan
- Added: batch-01-plan (30章重写方案); 第1-5章深度重写稿（rewritten/batch-01-chapter-01~05.md）
- Updated: reconstruction-progress.md 进度台账，增加批次追踪和重写原则
- Contradictions:
  - 原稿"仙人跳"低俗设定改为李振北直接动用家族权力，事件因果完全重织
  - 主角与夏梓妍的关系从"荷尔蒙驱动"改为"互相需要、平等合作"
  - 海哥登场从"天降大哥"改为"有规矩的交易者，投名状机制"
  - 原稿第3章暴打高富帅的爽点被替换为学校层面的系统性打压（处分、律师、校董），更真实也让主角困境更复杂
- Decisions needed:
  - 用户确认重写方向和风格后，继续推进第6-30章
  - 海哥与夏母的旧交具体性质（恩人？恋人？债主？）
  - 主角父亲的家庭经济线是否要在第1-30章中持续铺垫
  - 罗莉的家庭背景和她与主角关系的发展节奏

## [2026-10-08] lint | 目录冗余审计与顶层瘦身
- Sources: 目录树审计；wiki/ 与顶层数字目录重叠检查
- Added: wiki/scenes/scene-rules.md（从 06-scenes/README.md 迁移，原内容为 wiki/scenes/ 没有的场景与章节拆解规则）
- Updated: 删除 01-world/、02-characters/、03-plotlines/、04-timeline/、05-sources/、06-scenes/、07-video/、08-questions/、99-archive/ 共 9 个顶层目录
- Contradictions:
  - 01-world/README.md（320 行世界观总览）与 wiki/world/world-bible.md（171 行）重叠；world-bible.md 更精炼且有 canon 标注，采用后者
  - 02-characters/README.md（229 行人物线总览）与 wiki/characters/character-arc-bible.md（97 行表格版）重叠；character-arc-bible.md 更规范且有视频识别钩子，采用后者
  - 03-plotlines/README.md（201 行剧情线）与 wiki/structure/novel-volumes.md（338 行）重叠；novel-volumes.md 更详尽，采用后者
  - 04-timeline/README.md（186 行详细时间线）与 wiki/timeline/master-timeline.md（42 行表格）重叠；master-timeline.md 为权威时间索引，采用后者
  - 05-sources/README.md 与 raw/ 和 reports/ingest/ 重叠；07-video/README.md 与 wiki/systems/system-video-visual-bible.md 和 wiki/plot/short-drama-roadmap.md 重叠；08-questions/README.md 已在 wiki/overview.md 的"关键待确认决策"部分覆盖
  - 所有 01-world/、02-characters/、03-plotlines/ 下的索引文件均为纯链接索引（链接到 wiki/ 实体页），删除后不损失信息
- Decisions needed:
  - 是否需要在 wiki/ 各子目录下补建 index.md 作为目录入口（如 wiki/world/index.md、wiki/characters/index.md）
  - 顶层 README.md 是否需要更新以反映新的目录结构

## [2026-10-09] expand | 高频人物档案深度扩充（TOP 17 剩余 10 个）
- Sources: SRC-20261008-001 全文实体扫描 + /tmp/char_contexts/ 共 17 个人物 40 处上下文证据文件
- Added: 雷哥（雷达）、张晟威、王亮（亮子）、王晨、杨志锴、沈晴、洛梦（洛神）、刘园园、杨璐璐、曹姐（曹柔）共 10 个档案的专业级扩充。每个档案均采用"一句话定位→戏剧功能→已确认事实→外形→行为基线→声音指纹→欲望-需要-恐惧→能力资源→秘密→关系→人物弧→场景→矛盾→视频资产"标准模板
- Updated:
  - char-lei-ge.md：退伍军人→海迪悍将→送陈照南蝴蝶刀引路人，重构建议含秘密退伍原因+可能开面馆结局
  - char-zhang-shengwei.md：三重身份（恒丰少董+青帮堂主+鬼组副组长）→陈照南镜像反派→追夏梓妍→被搞砸订婚宴
  - char-wang-liang.md：陈照南结拜兄弟→好色豪爽→搞徐苗苗计划执行主力→跟陈照南一起上神龙学院
  - char-wang-chen.md：百乐赌场二把手+智囊→被陈照南离间→后期被挖来天下会→善用离间和明哲保身策略
  - char-yang-zhikai.md：神龙学院天字班+杨家少爷→肖院长第一个兵→给陈照南讲学院规则→一句话镇住莽牛
  - char-shen-qing.md：酒店大堂经理+娜娜合租姐姐→成熟风韵→火锅店面对混混骚扰→陈照南反差戏
  - char-luo-meng.md：洛神（粉丝尊称）→出道一年红透→被杨家小霸王内定→成都宣传会+陈照南保安公司线索
  - char-liu-yuanyuan.md：困难家庭高三少女→父亲吸毒死→弟弟欠债→绿毛逼债→陈照南认干妹妹+给十万块+找房子
  - char-yang-lulu.md：罗莉好姐妹+平民系花→骂陈照南直男教育→告诉陈照南罗莉回老家→全书最精彩情感导师
  - char-cao-jie.md：绿云江南老总+三年30店+寡妇+双胞胎女儿（姐死妹学坏）→火锅店偶遇→南天酒店救菲儿→名片揭示身份
- Contradictions:
  - 张晟威三重身份的动机原稿未明（为什么同时做恒丰+青帮+鬼组？proposed 父亲双料+母亲鬼组背景）
  - 王晨早期经历原稿空白（什么出身走到黑道？proposed 大学毕业生+被许乐所救）
  - 曹姐丈夫和姐姐死因原稿未说（proposed 车祸+溺水）
  - 杨志锴后期走向原稿无交代（被家族放弃？跟着陈照南？proposed 成熟后自己选路）
  - 洛梦最终结局原稿无交代（跟杨家？逃走？proposed 在苏越或陈照南帮助下逃离）
- Decisions needed:
  - 高频档案扩充是否继续（如修罗、苏柒柒、白姐等已完成，剩余 71 个人物是否全部处理）
  - 上述 proposed 推断是否需要后续精读验证
  - 扩充后的档案是否需要统一 canon/status 标注（confirmed vs inferred vs proposed）

## [2026-10-08] decision | Wiki 目录与文件全量中文重命名
- Sources: 任务指令；index.md 已有链接文字；各文件 frontmatter title
- Added: 16 个中文目录（人物/势力/地点/事件/关系/伏笔/剧情/时间线/术语/系统/世界/场景/风格/矛盾/结构/主题）；16 个 _index.md AI 导航文件；刘起山.md stub（原始未导入）
- Updated: 206 个文件重命名（英文拼音→中文）；所有 wikilink 路径更新（约 362 处）；index.md 英文标题改中文
- Contradictions: overview.md 与 index.md 根目录文件保留原名（overview/index/log），其余全部中文化；苏柒柒（罗刹女）文件名与 index.md 显示文字存在不完全匹配，已用链接路径指向实际文件名解决
- Decisions needed: 是否将根目录 overview.md 也重命名为故事总览.md（目前保留 overview.md 原名以避免影响现有引用）

## [2026-10-09] lint | drafts/chapters 按 6 部分部方案重组目录结构
- Sources: 分卷规划.md（失控的约见/狼舞崛起/天下会/城南之王/家族棋局/神龙荣耀）
- Added: 6 个分部子目录（第一部-失控的约见 ~ 第六部-神龙荣耀）
- Updated:
  - 18 个重写稿 `rewritten/batch-01-chapter-01~18.md` → `drafts/chapters/第一部-失控的约见/`
  - 3 个补充章节 `reconstructed-missing/chapter-098/100/102.md` → `drafts/chapters/第二部-狼舞崛起/原稿补第98/100/102章.md`
  - 1 个补充章节 `reconstructed-missing/chapter-557.md` → `drafts/chapters/第五部-家族棋局/原稿补第557章.md`
- Removed: 旧的 `rewritten/` 和 `reconstructed-missing/` 子目录（已空）
- Contradictions: wiki_backup_20261008/ 保持原样不动，其中 log.md 仍引用旧路径
- Decisions needed: 旧路径引用仅存在于历史日志中，按"仅追加不覆写"原则保留

## [2026-10-09] lint | 建立全小说闭环图谱
- Sources: `novel.yaml`、正式 `wiki/`、完整校订稿、S1 重构章节
- Added: FlowGram 图谱生成器、974 节点与 7639 条关系的 `graph/story-graph.json`
- Updated: Wiki/章节覆盖检查；历史 Wiki 快照迁入 `99-archive/`
- Contradictions: 无新增设定冲突
- Decisions needed: 角色终局与核心关系仍按现有决策流程确认
