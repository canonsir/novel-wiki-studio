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
│   ├── philosophy/              # 儒释道法 / 心学 / 兵家 / 法家
│   ├── history/                 # 清末 / 民国 / 建国初 / 改革开放 分期
│   ├── geography-folk/          # 真实→虚构映射、省市方言民俗
│   ├── jianghu/                 # 江湖 / 门派 / 武学 / 黑帮礼仪
│   └── law-enforcement/         # 公安司法程序 / 涉黑办案 / 法律边界
├── world/                       # 其他文化圈
│   ├── religion-philosophy.md
│   ├── history-overview.md
│   └── cultural-tropes.md
└── crafts/                      # 跨文化工艺与硬设定
    ├── martial-arts.md
    ├── finance-business.md
    ├── medicine-pharmacology.md
    └── weapons.md
```

## 当前成熟度

| 条目 | 状态 | 备注 |
|---|---|---|
| `china/geography-folk/real-to-fictional-map.md` | active | 全局硬约束 |
| `china/philosophy/*` | 部分 active | 儒释道心学已写详细 |
| `china/history/*` | 部分 active | 清末 / 民国 / 改开已写 |
| `china/jianghu/*` | active | 门派 / 武学 / 黑帮礼节 |
| `china/law-enforcement/*` | active | 公安 / 涉黑程序 |
| `world/*` | stub | 用到再补 |
| `crafts/*` | 部分 active | 武学 / 枪械 / 医药 / 金融 |

**约定**：stub 条目的 `TODO:` 区标注"用到再补"是允许的，但首次需要用到时**必须**先写满再写入小说。
