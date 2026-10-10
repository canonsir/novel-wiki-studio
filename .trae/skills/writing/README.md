# skills/writing/

创作类技能（主笔视角）：从策划、章节撰写到润色去 AI 化。所有写作 Agent（见 `common/agents/author-agent.md`）调用。

## 当前技能

- `chinese-novelist/` — 中文长篇小说分章创作，强调"展示而非讲述、冲突驱动、章末钩子"。
  - 入口：`SKILL.md`
  - 参考：`references/flows/`（4 阶段流程）、`references/guides/`（角色/钩子/对白/章节模板）
  - 工具：`scripts/check_chapter_wordcount.py`

## 加入新 skill 的最低要求

1. 在根目录放 `SKILL.md`，包含 `name / description / 触发条件`。
2. 在本 README 增加一行说明。
3. 列出该技能依赖的 `common/` 文件（如 `common/writing-rules.md`）。
4. 不得与 `review/`（审核）或 `short-drama/`（改编）职责重叠。
