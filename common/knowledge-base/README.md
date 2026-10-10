# common/knowledge-base/

Novel Wiki Studio 的**真实世界知识底盘**。所有小说在写作、审核、改编时都应引用这里的权威条目，减少凭空臆造，提升虚实结合的质量。

## 使用总规则

### 1. 虚实结合的三条底线

- **真实世界的地点**：首次在小说出现必须按 `china/geography-folk/real-to-fictional-map.md` 做虚构化处理（北京→帝都、上海→魔都、广州→南都、重庆→雾都、成都→蓉城……）。
- **真实世界的机构 / 品牌 / 法律**：可引用知识层概念，但在小说正文中必须虚构化具体名称或模糊化到行业。
- **真实世界的历史事件 / 人物**：可以借用时代底色和公认史实，但不得对真实人物做诽谤性、未经授权的塑造。

### 2. 条目的 3 层结构

每个知识页**不写长篇百科**，而是：

```
---
status: active
updated: YYYY-MM-DD
tags: [knowledge-base, <分类>]
---

# <概念>

## 定义
一句话定义（给非专业读者）。

## 关键事实清单
- 要点 1（可用于小说细节）
- 要点 2
...

## 常见误用（AI 容易写错的地方）
- 误用 A → 正确写法
- 误用 B → 正确写法

## 小说应用建议
- 什么场景适合用
- 什么人物适合挂此标签
- 可延伸的戏剧冲突

## 可查文献 / 原典
- 书名《作者》
- 公开资料链接（不直接外链私域）
```

### 3. 更新与引用

- 任何 Agent 发现误用，先更新本知识页，再回去修小说。
- 小说 wiki 内部**不得复制**知识层事实，只引用：`参见 common/knowledge-base/china/philosophy/wangyangming.md`。
- 新增概念先登记 `status: proposed`，经过至少一次使用后可升级 `active`。

## 目录

```
knowledge-base/
├── README.md                    # 本文
├── china/                       # 中国文化圈
│   ├── philosophy/              # 儒释道法 / 心学 / 兵家 / 诸子 / 神话风水
│   │   ├── confucianism.md
│   │   ├── buddhism.md
│   │   ├── daoism.md
│   │   ├── legalism.md
│   │   ├── wangyangming.md
│   │   ├── bingjia-strategy.md
│   │   ├── mohism-and-others.md
│   │   └── mythology-and-folk-belief.md
│   ├── history/                 # 古代 / 清末 / 民国 / 建国改开 / 当代
│   │   ├── ancient-dynasties.md
│   │   ├── late-qing.md
│   │   ├── republican-china.md
│   │   ├── prc-and-reform.md
│   │   └── contemporary-2010s.md
│   ├── geography-folk/          # 虚构映射 / 分区民俗 / 节气 / 茶酒饮食
│   │   ├── real-to-fictional-map.md
│   │   ├── regional-overview.md
│   │   ├── festivals-calendar.md
│   │   └── tea-wine-cuisine.md
│   ├── jianghu/                 # 门派 / 会党 / 礼节 / 现代地下经济
│   │   ├── secret-societies.md
│   │   ├── martial-schools.md
│   │   ├── etiquette-and-rules.md
│   │   └── underground-economy.md
│   └── law-enforcement/         # 扫黑 / 公安日常
│       ├── anti-mafia.md
│       └── police-daily.md
├── world/                       # 其他文化圈
│   ├── religion-philosophy.md
│   ├── history-overview.md
│   └── cultural-tropes.md
└── crafts/                      # 跨文化工艺与硬设定
    ├── martial-arts.md
    ├── weapons.md
    ├── medicine-pharmacology.md
    ├── finance-business.md
    ├── vehicles.md
    ├── luxury-fashion.md
    ├── art-antiques.md
    └── technology-hacking.md
```

## 当前成熟度

| 条目 | 状态 | 备注 |
|---|---|---|
| `china/geography-folk/real-to-fictional-map.md` | active | 全局硬约束 |
| `china/philosophy/*` | active | 儒释道法 / 心学 / 兵家 / 诸子 / 神话风水 共 8 篇 |
| `china/history/*` | active | 古代 / 清末 / 民国 / 建国改开 / 当代 共 5 篇 |
| `china/geography-folk/*` | active | 映射 / 民俗 / 节气 / 茶酒 共 4 篇 |
| `china/jianghu/*` | active | 门派 / 会党 / 礼节 / 地下经济 共 4 篇 |
| `china/law-enforcement/*` | active | 扫黑 / 公安日常 共 2 篇 |
| `world/*` | active | 宗教 / 世界史 / 跨文化原型 共 3 篇 |
| `crafts/*` | active | 武学 / 枪械 / 医药 / 金融 / 车辆 / 奢侈品 / 古玩 / 科技 共 8 篇 |

**约定**：stub 条目的 `TODO:` 区标注"用到再补"是允许的，但首次需要用到时**必须**先写满再写入小说。
