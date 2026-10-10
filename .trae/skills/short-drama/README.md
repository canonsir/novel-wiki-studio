# skills/short-drama/

小说到短剧的改编类技能（短剧改编视角）。

## 定位

小说正文完成后，面向红果漫剧 / 短剧 AI 正片 / 投放素材的改编环节。
对应 Agent：`common/agents/adapter-agent.md`。

## 规划中

- `shot-breakdown` — 把章节拆成分镜（镜号 / 景别 / 时长 / 角色动作 / 环境 / 对白 / 情绪转折）
- `drama-reviewer` — 短剧单集 review（时长、钩子强度、AI 可生成资产可行性）
- `visual-asset-planner` — AI 可复用资产清单（人物 look / 场景光影 / 关键道具）生成

## 当前状态

骨架目录，尚未实装具体 skill。待小说改编主流程稳定后，按红果规范（`common/platform-profiles/redfruit-ai-material.md`）与改编 agent 要求补齐。

## 加入新 skill 的最低要求

同 `writing/README.md`，且必须声明：
1. 输入形态（章节 md / 场景卡 / arc 规划）。
2. 输出形态（分镜表 / 剧本页 / 资产清单）。
3. 对应 `common/platform-profiles/redfruit-ai-material.md` 的具体章节。
