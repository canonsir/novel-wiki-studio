# Novel Wiki Studio

一个把“小说”当作可持续维护知识工程的 Git 仓库。它借鉴 Karpathy 的 **LLM Wiki**：不让模型每次从原稿重新推理，而是把原稿、访谈、灵感等不可变素材持续编译为结构化、相互链接、可审计的小说 Wiki；创作、扩写和视频改编都建立在这个 Wiki 上。

## 核心分层

1. **Raw（素材真相层）**：原始小说、灵感、设定、参考图；只追加，不覆盖。
2. **Wiki（持续编译层）**：人物、世界观、地点、事件、时间线、场景、伏笔、冲突、主题等；由 AI 维护，人负责确认关键取舍。
3. **Drafts（文学表达层）**：卷、章、场景正文；由 Wiki 约束但允许艺术性表达。
4. **Outputs（衍生层）**：视频脚本、人物小传、提案、宣发文案等。
5. **Schema（规则层）**：`AGENTS.md`、`schema/`、`common/`；规定 AI 如何读、写、交叉引用和自检。

## 快速开始

```bash
python3 scripts/new_novel.py "小说名" --slug novel-slug
```

然后：

1. 将原稿放入 `novels/novel-slug/raw/manuscript/`，不要直接修改原稿。
2. 告诉 AI 按 `prompts/ingest-novel.md` 执行“导入”。
3. 阅读 AI 生成的 `wiki/overview.md`、`wiki/index.md` 和首轮诊断报告。
4. 确认题材、目标读者、叙事视角、尺度与结局边界。
5. 按 `prompts/expand-chapter.md` 重构或扩写。
6. 每次变更后运行：

```bash
python3 scripts/lint_wiki.py novels/novel-slug
```

## 仓库结构

```text
.
├── AGENTS.md                 # AI 总操作规约
├── common/                   # 所有小说共享的创作与合规规则
├── docs/                     # 架构、工作流、Git 使用说明
├── prompts/                  # 可复用的任务提示词
├── schema/                   # 页面元数据和 ID 约定
├── _template/                # 新小说模板
├── novels/                   # 每部小说一个独立 Wiki
└── scripts/                  # 建书、重建索引、静态检查
```

## 重要原则

- **原稿不可变**：保留作者最初表达和证据链。
- **事实、推断、提案分离**：Wiki 中明确标记 `confirmed / inferred / proposed / contradicted`。
- **一个事实一个权威页面**：其他页面使用 `[[双链]]` 引用，避免复制后失同步。
- **剧情变化必须传播**：改年龄、能力、动机或事件，就同步人物、时间线、事件、场景、伏笔和索引。
- **细节服务戏剧目的**：不为“详细”而堆砌；每个细节至少服务人物、氛围、冲突、线索或可视化。
- **人类掌舵**：重大主题、人物命运、价值判断与发布尺度必须由人确认。

## 当前状态

本仓库已提供完整骨架、公共规则、页面模板、导入/扩写/检查/视频脚本提示词，以及零依赖的创建和检查脚本。下一步只需把第一篇小说放进对应的 `raw/manuscript/`。

## 来源与说明

架构灵感来自 Karpathy 的 [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)。本项目是面向小说创作与影视衍生的领域化实现，不是原 Gist 的镜像。
