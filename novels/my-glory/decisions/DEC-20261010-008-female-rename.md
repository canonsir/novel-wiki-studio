# DEC-20261010-008｜女性角色改名：霍惊鸿→霍凝烟 / 季繁星→季婉宁 / 穆清→穆清岚

- **Status**: accepted
- **Date**: 2026-10-10
- **Context**:
  用户决议："**霍惊鸿这个名字我以为是个男的，类似的问题，都需改一下**"。

  见 `reports/REP-20261010-005-female-naming-review.md` 完整评估：

  - **霍惊鸿**：三字连读韵律硬朗 + 武侠文脉"惊鸿"常作男性字号（陆小凤风），性别读感偏男
  - **季繁星**：繁星二字中性
  - **穆清**：二字名 + "於穆清庙"（《诗经·周颂》）出处偏庙堂男性

  用户 ACK：**霍 → 霍凝烟 / 整体方案 B 全部改**

- **Options Evaluated**: 见 REP-005 §3

- **Decision**:
  执行方案 B 全部改：

  | 旧名 | 新名 | id 迁移 | slug 迁移 |
  |---|---|---|---|
  | 霍惊鸿 | **霍凝烟** | char-huo-jinghong → char-huo-ningyan | 霍惊鸿 → 霍凝烟 |
  | 季繁星 | **季婉宁** | char-ji-fanxing → char-ji-wanning | 季繁星 → 季婉宁 |
  | 穆清 | **穆清岚** | char-mu-qing → char-mu-qinglan | 穆清 → 穆清岚 |

- **Rationale**:
  - **霍凝烟**：
    - "凝"字 + "烟"字 → 鬼魅型 / 杀手气质
    - 保留"霍"姓（霍家 = 五大家族内务府皇商 / 军医系）
    - 保留鬼组代号"叉"的反差（名字柔雅 + 代号凌厉）
    - 女性识别度 ★★★★★
  - **季婉宁**：
    - "婉"字直接出自艺名"洛神"所出《洛神赋》"**翩若惊鸿，婉若游龙**"的下半句
    - 名实呼应："书中洛神"的娱乐圈身份与本名古典婉约气质统一
    - 女性识别度 ★★★★★
  - **穆清岚**：
    - 保留"穆清"主体（minimal change）
    - "岚"字强化女警清冽气质（山岚之清）
    - 女性识别度 ★★★★★

- **Consequences**:
  - **文件重命名**：
    - `wiki/characters/霍惊鸿.md` → `wiki/characters/霍凝烟.md`（git mv）
    - `wiki/characters/季繁星.md` → `wiki/characters/季婉宁.md`（git mv）
    - `wiki/characters/穆清.md` → `wiki/characters/穆清岚.md`（git mv）
  - **全文替换**：
    - 27 个文件内 `霍惊鸿`→`霍凝烟` / `季繁星`→`季婉宁` / `穆清`→`穆清岚`
    - 典故保护：单独的"惊鸿"（《洛神赋》"翩若惊鸿"）**未替换**
  - **更新**：
    - `wiki/continuity/continuity-naming-map.md`：追加本次改名对账
    - `wiki/continuity/人物称谓全索引·防漏改.md`：旧名加入禁词清单
    - `novel.yaml` `ending_reconstruction.harem_outcome`：三个人物名已改
    - `wiki/overview.md`：读者承诺段三个人物名已改
    - `wiki/plot/短剧Arc分段骨架.md` + `wiki/plot/arcs/Arc1-女神与仙人跳-图谱.md`：三人提及改名
    - `wiki/factions/霍家.md` / `鬼组.md`：相关引用改名
    - `wiki/objects/霍家八宝玉令.md` / `鬼组通讯耳钉.md`：道具归属改名
    - 其他 wiki / drafts / reports / decisions 全部改名
  - **保护**：
    - c001 正文零影响（三人均未在 c001 出场）
    - raw/ 封板稿只读，不改

- **References**:
  - REP-20261010-005 女性角色命名评估报告
  - DEC-20261010-001 主角与五家族命名
  - DEC-20261010-007 结尾方向定稿（后宫归属锁定）
  - 《洛神赋》曹植（婉宁命名出处）
  - 《文选》卷十九

- **Risk & Mitigation**:
  - 风险：有已写内容残留旧名 → 用 grep 全扫 + 禁词清单固化（已做）
  - 风险："翩若惊鸿"典故被误伤 → 用典故独立 grep 验证（已做，4 处典故保留）
  - 风险：读者初次见"季婉宁"仍不知道是"洛神"→ Arc 1 不涉她；S2 出场时首次介绍即给艺名"洛神"