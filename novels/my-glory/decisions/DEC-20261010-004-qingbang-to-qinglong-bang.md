# DEC-20261010-004｜青帮 → 青龙帮

- **Status**: accepted
- **Date**: 2026-10-10
- **Context**: 原稿与改编第一版沿用"青帮"原名。但"青帮"作为近代真实历史组织（黄金荣 / 杜月笙时期上海青帮）在国家红线（`common/constraints/national-redlines-checklist.md` L48）与红果平台（`platform-redfruit-checklist.md` L49）下属于必须虚构化的真实组织名——以其名义进行犯罪 / 跨城打手 / 走私叙事存在合规风险。REP-20261010-003 §3 曾推荐"沪社"；REP-20261010-004 扩充 12 候选 + 4 推荐（相柳堂 / 大通社 / 乾字门 / 河山会）。
- **Options Evaluated**:
  1. 保留"青帮"（否决：合规风险）
  2. 相柳堂 / 大通社 / 乾字门 / 河山会 / 沪社（REP-003 / REP-004 的推荐，均非用户最终选择）
  3. **"青龙帮"（用户选择）**：延续"青"字识别感，加"龙"字加强江湖气；非真实历史组织名；与本作已有命名（天下会 / 鬼组 / 海迪 / 狼舞 / 飞鸿帮 / 忠信帮 / 白袍会 / 青花会 / 天一集团）气质一致
- **Decision**: 采用 **"青龙帮"**（id: `fac-qinglong-bang`）
- **Rationale**:
  - 合规：无真实历史组织影射；读者无需联想到真实上海青帮
  - 记忆成本：保留"青"字，对已有读者认知最小调整
  - 命名一致性：与"白袍会 / 青花会 / 忠信帮 / 飞鸿帮"同气质
  - 短剧视觉锚点可做：**青色腰带 + 青龙刺青（左肩）+ 匕首为制式兵刃**
- **Consequences**:
  - 全书涉"青帮"活跃引用统一改为"青龙帮"
  - 新增"四堂"分部结构（青堂情报 / 龙堂武力 / 水堂走私 / 门堂外事）充实组织骨架
  - 门规核心加 "三不"（不卖国 / 不碰未成年 / 不打盟友）为后续"主角清算其松动门规"做叙事铺垫
- **Files updated**:
  - 新建 `wiki/factions/青龙帮.md`（id: fac-qinglong-bang, slug: 青龙帮）
  - 删除 `wiki/factions/青帮.md`
  - 活跃页替换"青帮"→"青龙帮"（天一集团 / 厉擎苍 / 秦枭 / 厉天鸿 / 宁云疏 / index / novel.yaml）
  - 对账记录追加到 `wiki/continuity/continuity-naming-map.md`
  - REP-20261010-004 追加「用户决议」小节
  - log 追加 decision 条目
- **不改**：
  - `raw/`（只读源）
  - `graph/story-graph.json`（下次重建时自动更新）
  - 历史 reports §1-§5（审计保留）
  - DEC-20261010-002（当时锁定的"组织名保留原名"决定被本决策**部分 supersede**：仅青帮项被更新，其他组织名不变）
- **References**:
  - REP-20261010-003 §3 命名复评（历史分析）
  - REP-20261010-004 青帮改名候选扩充（12 候选）
  - common/constraints/national-redlines-checklist.md L48
  - common/constraints/platform-redfruit-checklist.md L49
