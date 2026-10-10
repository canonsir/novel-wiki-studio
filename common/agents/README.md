# common/agents/

多视角 Agent 规约库。所有小说创作都以此为**人格切换入口**：主笔 → 编辑 → 连续性 → 平台审核 → 读者 → 短剧改编，循环闭合。

## 调用总规则

1. **一个任务一次只以一个 Agent 身份工作**，切换 Agent 必须显式声明，避免视角混杂。
2. **Agent 之间通过 Wiki 与 decisions 交接**，不通过聊天记录传话；重要结论必须回写到 `wiki/` 或 `decisions/`。
3. **Agent 可以调用技能**（`.trae/skills/`），但不得冒充技能。
4. **Agent 的权限边界以 `AGENTS.md` 第 2 节三层真相为准**：`raw/` 只读、`wiki/` 可写、`drafts/outputs/` 可迭代。
5. **冲突优先级**：法律与安全 > 已确认用户决策 > Agent 内部判断。

## Agent 清单

| 文件 | 视角 | 典型调用场景 |
|---|---|---|
| `author-agent.md` | 主笔 | 新章节撰写、润色、风格统一 |
| `editor-agent.md` | 故事编辑 | 方案评审、arc 规划、章节节奏诊断 |
| `continuity-agent.md` | 连续性编辑 | 时间线/伤势/物件/地名一致性复核 |
| `reviewer-agent.md` | 平台审核员 | 发布前合规闸门：番茄 + 红果 + 国家红线 |
| `reader-agent.md` | 读者/观看者 | 代入目标用户画像评估爽点、钩子、追读率 |
| `adapter-agent.md` | 短剧改编 | 小说 → 分镜 → 单集剧本 → AI 资产清单 |
| `grill-agent.md` | 质询者 | 关键决策定稿前的逻辑压力测试 |

## Agent 交接流程（标准闭环）

```
author → editor → continuity → reviewer → reader → (loop) → adapter
       ↑                                                    │
       └────────── 发现问题回退重写 ───────────────────────┘
```

每次交接的最小载体是**一次 wiki 页面更新 + 一行 wiki/log.md**。
