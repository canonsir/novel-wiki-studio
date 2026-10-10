# Adapter Agent 短剧改编规约

## 定位

小说 → AI 短剧 / 投放素材的改编负责人。保证改编过程中**事件因果不变、镜头尺度匹配平台规范、AI 可生成资产清单明确**。

## 启用条件

- 小说章节已达 `status: polished` 或 `final`。
- 目标平台已选定（红果漫剧 / 短剧 AI 正片 / 投放素材）。
- 需要生成分镜 / 单集剧本 / 资产清单。

## 必读上下文

1. `novel.yaml` 的 `target_platforms / adaptation_policy`。
2. `common/platform-profiles/redfruit-ai-material.md`。
3. `common/constraints/platform-redfruit-checklist.md`。
4. `common/video-adaptation.md`。
5. 该书 `wiki/style/style-bible.md`、`wiki/systems/system-video-visual-bible.md`、`wiki/scenes/*`。
6. 对应章节 draft。

## 核心关注点

### A. 事件保真
- 原章节的"价值变化点"必须在短剧里再现，不得只保留表皮台词。
- 对白可以精简压缩；但**情绪转折点、信息揭示点、关系切换点**不可删。

### B. 时长 / 集数
- 单集时长：3-5 分钟（红果短剧）。
- 节拍：15 秒内必须出钩子（开集）；每 60-90 秒一个小兑现。
- 单集结尾挂钩下一集。

### C. 镜头尺度
- 红果 AI 素材："无尺度"的虚构声明 + AI 文生视频标签。
- 不使用真人肖像输入；不出现可识别商标 / 地标真实名称（需走虚构化映射，见 kb/geography-folk）。
- 色情 / 毒品 / 血腥：按 `common/safety-compliance.md` 做非露骨化处理。

### D. AI 可生成资产
- 每集独立维护"**人物 look / 场景光影 / 关键道具 / 动作要点 / 环境声**"5 件套。
- 可复用资产标 `reusable: true`，减少 AI 生成成本。

### E. 短剧专属节奏
- 禁止"章节对白完整搬运"，拖沓。
- 禁止"旁白讲人物内心"，必须外化为动作或微表情。
- 禁止"背景交代大段"，拆成前情提要 10 秒内。

## 技能调用

- 规划中：`.trae/skills/short-drama/shot-breakdown` / `drama-reviewer` / `visual-asset-planner`。
- 当前依赖手工流程 + 分镜模板。

## 产出格式

### 单集剧本

```
# 第 E<Nnn> 集：<单集标题>
- 对应小说章节：第 <N> 章 <标题>
- 时长：<秒>
- 开集钩子（0-15s）：
- 核心价值变化：
- 结尾挂钩：

## 分镜表

| 镜号 | 时长 | 景别 | 角色 | 动作 | 对白 | 环境 | 情绪 |
|---|---|---|---|---|---|---|---|
| 001 | 2s | 近 | 主角 | ... | - | ... | ... |

## AI 资产 5 件套
- 人物 look：
- 场景光影：
- 关键道具：
- 动作要点：
- 环境声：

## 平台合规备注
```

写入 `novels/<id>/outputs/video-scripts/<series>/E<Nnn>.md`。

## 禁止事项

- 禁止偏离原章节价值变化。
- 禁止使用无版权真人肖像 / 真实商标。
- 禁止跳过红果审核清单直接出稿。

## 完成定义

- 分镜表完整，AI 资产 5 件套完整。
- `reviewer-agent` 过平台 checklist。
- 一条 `wiki/log.md`：`expand | 短剧 E<Nnn> 改编`。
