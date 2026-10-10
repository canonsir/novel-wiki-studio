---
name: kb-extender
description: Add common/knowledge-base entries with the house template and sync all indexes. Use when asked to extend or supplement the knowledge base with new topics. Not for chapter writing, story queries, or one-off research.
---

# KB Extender（知识库扩展）

把"新增真实世界知识条目"的标准动作固化下来：**写条目 → 同步索引 → 校验 → 提交**。由资料管理员视角持有，产出是 `common/knowledge-base/` 下的权威条目，不是小说正文。

## 触发时机

- 用户说"扩展知识库""补充 XX 领域知识库""新增知识条目"。
- 写作 / 重构中发现某真实领域反复出现且现有条目无法支撑，先补条目再写正文。
- **不用于**：章节撰写（走 writing/chinese-novelist）、剧情问答、一次性网络调研。

## 标准流程

### 1. 准备（先读后写）

- 读 `common/knowledge-base/README.md`：三条虚实底线、条目结构、目录、成熟度表。
- 读与新主题**相邻 / 重叠**的已有条目，划清边界并确定交叉引用（例：军事篇引用 weapons、martial-arts、medicine-pharmacology）。
- 确定文件落点：
  - `china/philosophy|history|geography-folk|jianghu|law-enforcement/` — 中国文化圈。
  - `world/` — 其他文化圈。
  - `crafts/` — 跨文化工艺与行业硬设定。
- 一次可批量写多篇（如"军事、影视、医疗"），但每篇都要独立达标。

### 2. 按模板写条目

- 复制 `assets/entry-template.md` 到目标路径，文件名小写 kebab-case。
- 只写**常识级、可用于小说细节**的事实，用表格和清单组织，不写长篇百科。
- 每篇必备小节：定位、**合规红线（最高，置顶）**、关键事实清单、常见误用表、小说应用建议、可查文献、延伸条目。
- frontmatter：`status: active`、`updated: <当日>`、`tags: [knowledge-base, <分类>...]`。
- 新增概念若无使用先例，按 README 规则先记 `status: proposed`。

### 3. 合规底线（每条目都要过）

- **真实地名**首次出现即虚构化（北京→帝都等），引用 `china/geography-folk/real-to-fictional-map.md`。
- 真实机构 / 品牌 / 平台 / 奖项 / 院校 / 医院 / 部队番号一律虚构化或模糊到行业。
- 不影射、不丑化真实在世人物；可借公认史实与时代底色。
- 不写可直接复刻的违法细节（制毒制爆、武器改装、骗保、走私通道、攻击教程）。
- 违法行为作为剧情时必须呈现法律后果，不渲染、不教学。

### 4. 同步索引（漏一不可）

- 更新 `common/knowledge-base/README.md`：目录树新增文件、成熟度表对应分组篇数。
- 更新根 `AGENTS.md` 第 13.3 节目录树。
- 本次若新建了 skill 分组：更新 `.trae/skills/README.md` 分组表与 `AGENTS.md` 第 13.2 节。
- 若分组 README 存在（如 `crafts` 无独立 README 则跳过），补一行说明。

### 5. 校验与交付

- 结构完整：模板必备小节齐全，frontmatter 合法。
- 交叉引用双向可达：新条目"延伸条目"指向的页面，相关页面已有反向引用更佳。
- 无事实重复：同一事实只在权威条目写一次，其他条目引用不复制。
- 用户要求提交时：`git add` 指定文件（不用 `git add -A`）→ commit（信息含新增条目与索引同步）→ push。

## 判定某主题"该不该建条目"

- 该领域在目标题材中**高频复现**或错误代价高（合规、专业硬伤）→ 建条目。
- 纯模型通用知识、一次性桥段、冷门到全书只用一次 → 不建，避免知识库膨胀。
- 主题过大（如"军事"）→ 按写作需求拆成可操作的单篇（军事背景 / 武器 / 武学各自独立）。

## 参考文件

- 条目模板：`assets/entry-template.md`
- 全局规则：`common/knowledge-base/README.md`、根 `AGENTS.md` 第 13.3 节
