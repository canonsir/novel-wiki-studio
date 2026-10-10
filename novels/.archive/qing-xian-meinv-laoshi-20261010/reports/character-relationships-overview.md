---
id: character-relationships-overview
type: report
title: 核心人物关系图（改版后）
status: active
canon: proposed
source_refs:
  - decisions/dec-20261009-006-protagonist-renaming.md
  - graph/story-graph.json
updated: 2026-10-09
tags: [relationships, overview, flow-graph]
---

# 核心人物关系图（改版后）

> **完整图谱**：1024 节点 / 7838 边 / 0 孤点 / closed，由 `scripts/build_story_graph.py` 从 `wiki/` + S1 重构稿生成到 `graph/story-graph.json`。在本地浏览器通过 `packages/novel-flow-graph` 启动器查看。
>
> **本页**：从完整图谱中抽取 S1 核心人物子集，用 Mermaid 可读视图呈现，便于 review。

## S1 核心关系子图

```mermaid
flowchart TB
    HN[陈浩南<br/>男主 大二 果园少年]
    ZW[沈知微<br/>女主 青年教师 练散打]
    ZX[张星<br/>男主室友 兄弟]
    LL[罗莉<br/>男主同学 现实锚点]
    ZB[李振北<br/>反派 控制狂]
    RH[吕润海<br/>海哥 地下引路人]
    MM[徐苗苗<br/>校园对手→后期协作]
    QM[夏启明/沈启明?<br/>女主父 待确认CON-009]
    SM[男主父母<br/>果园老家]
    BJ[白姐<br/>海迪经营者 S1末登场]

    HN -- 匿名约见 --> ZW
    HN -- 发小 过命兄弟 --> ZX
    HN -- 同学→亲密关系 --> LL
    HN -- 外部镜像仇敌 --> ZB
    HN -- 主动选择的引路人 --> RH
    HN -- 校园对手→合作 --> MM
    HN -- 家庭纽带 --> SM
    HN -- S1末新世界入口 --> BJ

    ZW -- 债务控制 被追求 --> ZB
    ZW -- 父女 债务源头 --> QM
    ZW -. 后期有竞争有共鸣 .-> LL

    ZB -- 利用其设局 --> MM
    ZB -. 债务链 .-> QM

    RH -- 场域规矩 收编 --> HN
    RH -- 老板-管理 --> BJ

    classDef protagonist fill:#ff9800,stroke:#e65100,color:#fff
    classDef heroine fill:#e91e63,stroke:#880e4f,color:#fff
    classDef ally fill:#4caf50,stroke:#1b5e20,color:#fff
    classDef villain fill:#f44336,stroke:#b71c1c,color:#fff
    classDef mentor fill:#2196f3,stroke:#0d47a1,color:#fff
    classDef family fill:#9c27b0,stroke:#4a148c,color:#fff
    classDef pending fill:#9e9e9e,stroke:#424242,color:#fff

    class HN protagonist
    class ZW heroine
    class ZX,LL,MM ally
    class ZB villain
    class RH,BJ mentor
    class SM family
    class QM pending
```

## 核心关系说明表

| 关系 | 当前状态 | S1 期末预期 | 关键伏笔 |
|---|---|---|---|
| 陈浩南—沈知微 | Soul 匿名约见身份错位 | 互相欠命的秘密盟友，保持边界 | sou"烦"瞬间（clue-xia-debt）；声音耳熟（clue-xia-voice 已回收） |
| 陈浩南—张星 | 嘴贱室友 | 过命兄弟，但张星保留退出权 | 张星是最后"普通人锚点"，不能死 |
| 陈浩南—罗莉 | 有共同经历的普通同学 | 建立亲密关系后出现第一道裂缝 | 主角对罗莉的隐瞒与暴力 |
| 陈浩南—李振北 | 偶发情敌（第 3 章正式触发） | 人格摧毁为目标的镜像仇敌 | clue-mirror（主角逐渐采用相同逻辑） |
| 陈浩南—吕润海 | 第 12 章留置区偶遇 | 主角主动选择的引路人，非无条件后台 | clue-hai-motive（海哥为何扶持） |
| 陈浩南—徐苗苗 | 第 14 章校园对手 | 制造证据筹码阶段 | clue-xu-notebook |
| 陈浩南—白姐 | 第 30 章登场 | 让主角看到权力依赖经营 | 第 30 章章末钩子 |
| 沈知微—父亲 | 父女 | 债务线核心触发 | **CON-009 父亲姓氏待定** |
| 沈知微—李振北 | 债务逼婚控制 | 主动调查其资产网络 | clue-zhao-debt-chain |

## 后台与势力曲线（第 1 部末兑现）

```mermaid
flowchart LR
    PE[校园]
    LJ[李家]
    HD[海迪]
    FM[肥猫 外部压力]
    QS[秦姓强者/父辈 延后]

    PE -- 处分 舆论 身份污点 --> HN2[陈浩南 S1]
    LJ -- 钱 保镖 皇城债务 --> HN2
    HD -- 场所规矩→现金流经营 --> HN2
    FM -- 举报 围堵 --> HD
    QS -. 本部不兑现 .-> HN2

    HN2[陈浩南 S1 期末 状态]
```

## 相比原稿的关系线差异（本次重构）

| 差异点 | 原稿 | V2 |
|---|---|---|
| 女主独立性 | 被救援的对象 | 主动调查债务、能拒绝救援式占有 |
| 罗莉—主角关系 | 多次原谅 | 至少一次真实离开 |
| 徐苗苗情报 | 近万能 | 条件忠诚（主角承认她的能力） |
| 海哥扶持动机 | 看一眼认天命 | 场所规矩 + 肥猫冲突 + 留置观察三者叠加 |
| 终局后台 | 秦姓强者一键清场 | 第 1 部只兑现吕润海；父辈身世延后 |

## 在 FlowGram 查看完整图谱

```bash
cd /Users/bytedance/WorkBuddy\ AI/2026-10-08-17-33-38
npm --prefix packages/novel-flow-graph run dev
# 浏览器打开本地启动地址，加载 novels/qing-xian-meinv-laoshi/graph/story-graph.json
```

完整图谱覆盖：242 个 Wiki 页节点 + 747 章节点 + 22 条 S1 重写章节 + 全部双链关系，闭环无孤点。
