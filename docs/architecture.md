# 架构说明

## 设计目标

把每部小说视为一套“可编译的叙事系统”：原稿是源码，Wiki 是语义模型，章节是构建产物，视频脚本是下游目标。这样，人物年龄、能力边界、线索状态、伤势与时间线不会散落在几十章里无人维护。

## 每部小说的目录

```text
novels/<slug>/
├── novel.yaml
├── raw/                 # 不可变来源
│   ├── manuscript/
│   ├── references/
│   └── assets/
├── wiki/                # AI 持续维护
│   ├── index.md
│   ├── log.md
│   ├── overview.md
│   ├── characters/
│   ├── factions/
│   ├── locations/
│   ├── world/
│   ├── systems/
│   ├── plot/
│   ├── timeline/
│   ├── events/
│   ├── scenes/
│   ├── relationships/
│   ├── clues/
│   ├── themes/
│   ├── continuity/
│   └── style/
├── drafts/              # 正文工作区
├── outputs/             # 视频脚本等衍生物
├── reports/             # 导入/质量/连续性报告
└── decisions/           # 用户确认的关键决策
```

## 权威来源矩阵

| 信息 | 权威页面 | 其他页面处理 |
|---|---|---|
| 人物身份、外形、欲望、秘密 | `wiki/characters/` | 链接引用 |
| 日期与先后顺序 | `wiki/timeline/master-timeline.md` + 事件页 | 不重复定义 |
| 世界规则/能力代价 | `wiki/systems/` | 场景页记录具体应用 |
| 地理、距离、动线 | `wiki/locations/` + 世界地图页 | 场景页引用 |
| 伏笔状态 | `wiki/clues/clue-ledger.md` | 章节页记录投放/回收 |
| 文风、禁用习惯 | `wiki/style/style-bible.md` | 草稿遵循 |
| 用户选择 | `decisions/` | 通过 decision ID 引用 |

## Wiki 页面最小结构

所有实体页包含 YAML frontmatter：`id/type/title/status/canon/source_refs/updated/tags`。正文至少包含：一句话摘要、已确认事实、证据、关系/依赖、矛盾与缺口、相关页面、变更影响。

## 增量维护

新增材料不是“再写一份摘要”，而是对现有语义图做补丁：

1. 识别受影响实体；
2. 对比现有声明；
3. 添加证据与置信度；
4. 标记冲突而非覆盖；
5. 更新跨页链接；
6. 更新索引和追加日志。

## 扩展策略

- 数百页面以内：`index.md` + 文件搜索足够。
- 超过约 500 页面：可引入全文/BM25/向量搜索，但不能替代 Wiki 维护。
- 大图、音视频：使用 Git LFS 或对象存储，Wiki 中保存稳定引用与版权信息。
- Obsidian 可作为浏览器，Git 是版本史，AI 是维护者。
