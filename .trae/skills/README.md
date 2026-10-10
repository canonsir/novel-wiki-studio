# .trae/skills/

Novel Wiki Studio 公共技能库。按**职责**分组，不按作者或来源分组。

## 分组

| 分组 | 定位 | 典型 Agent |
|---|---|---|
| `writing/` | 创作：策划、撰写、润色 | author-agent |
| `review/` | 审查：方案质询、平台审核、读者代入 | editor-agent / reviewer-agent / reader-agent / continuity-agent |
| `short-drama/` | 小说转短剧改编：分镜、单集 review、AI 资产 | adapter-agent |
| `knowledge/` | 知识库维护：新增知识条目、同步索引 | 资料管理员 |

## 使用总规则

1. **按视角触发**：Agent 规约（`common/agents/`）决定何时启用哪个 skill，不由 skill 自己揽活。
2. **只读 common**：skill 只允许读 `common/`、`schema/`、`novels/<id>/wiki|decisions`，不得写入 `raw/`，写入 `drafts/` 和 `wiki/` 必须走 Agent 流程登记。
3. **分组互斥**：同一 skill 不得跨分组承担职责；若职责交叉，拆成两个 skill。
4. **引用知识库**：涉及真实世界事实的 skill，必须引用 `common/knowledge-base/` 相应条目，不得自行百科。

## 新增 skill 流程

1. 判定分组 → 在对应分组目录内 `mkdir <skill-name>/`。
2. 写 `SKILL.md`（含 `name / description / trigger / 依赖的 common 文件 / 输入输出`）。
3. 更新分组 README 一行说明。
4. 若引入新的 Agent 职责，同步在 `common/agents/` 补充规约。
5. 若涉及约束勾选，同步在 `common/constraints/` 新增或补齐 checklist。
