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
│   ├── events/
│   ├── scenes/
│   ├── objects/
│   ├── clues/
│   ├── terms/
│   └── <其他类型目录>/
├── graph/
│   └── story-graph.json  # FlowGram 全量闭环图谱（生成文件）
├── drafts/
│   ├── manuscript/
│   │   └── latest.md     # 唯一完整阅读稿
│   └── chapters/         # 六部最新分章重构稿
├── outputs/             # 视频脚本等衍生物
├── reports/             # 导入/质量/连续性报告
└── decisions/           # 用户确认的关键决策
```

## 权威来源矩阵

| 信息 | 权威页面 | 其他页面处理 |
|---|---|---|
| 人物身份、外形、欲望、秘密 | `type: character` 页面 | 链接引用 |
| 日期与先后顺序 | `type: timeline/event` 页面 | 不重复定义 |
| 世界规则/能力代价 | `type: world/system` 页面 | 场景页记录具体应用 |
| 地理、距离、动线 | `type: location` 页面 | 场景页引用 |
| 伏笔状态 | `type: clue` 页面 | 章节页记录投放/回收 |
| 文风、禁用习惯 | `type: style` 页面 | 草稿遵循 |
| 用户选择 | `decisions/` | 通过 decision ID 引用 |

目录使用规范英文类型名，页面文件名与稳定 ID 一致；中文标题写在 frontmatter。
脚本仍必须读取 frontmatter `type`，不能把目录名当作唯一事实来源。

## 闭环图谱

每部小说必须生成 `graph/story-graph.json`。图谱至少包含：

- `novel.yaml` 根节点和 Wiki 分类节点；
- 全部正式 Wiki 实体页；
- 完整正文的全部章节及章节顺序；
- 正式重构章节及其原章节映射；
- Wiki 双链、章节正文提及和显式时序关系；
- Wiki、索引、章节、关联章节、节点、边和孤点覆盖率。

`packages/novel-flow-graph/` 是公共 FlowGram 组件，`apps/story-graph/` 是统一查看器。
图谱是 Wiki 与正文的派生视图，不是新的事实编辑入口。

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
