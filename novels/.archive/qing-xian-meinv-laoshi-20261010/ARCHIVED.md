# 归档说明

此目录为 2026-10-10 从 `novels/qing-xian-meinv-laoshi/` 整体归档的历史产物，状态：**paused / archived**。

## 归档原因

- 用户决定暂停该书的改编，优先完善 novel-wiki-studio harness（真实世界知识库、多视角 Agent、题材 profile 等）。
- 当前改编（S1 c001–c018 分章、V4 换名、全文校订版、Wiki 等）保留为**只读参考样本**，用于后续新书创作时查阅既往决策与风格探索。
- Git tag `archive/qing-xian-meinv-laoshi-20261010` 指向本次归档前的最后一次提交，可随时还原。

## 使用约束

- 不再作为生产基线：图谱/索引/lint 均不覆盖本目录（`novels/.archive/` 已在相关脚本中排除或忽略）。
- 不再新增改编内容：如要重启，请从 harness 更新后的最新 `_template/` 新建小说目录。
- `raw/` 原稿按项目规约仍保持只读；两份完整 747 章原稿（.md / .txt）在 `raw/` 根目录。
- 决策文件（`decisions/dec-20261009-*`）记录了命名、题材、平台策略等讨论，可作为 harness 建设的输入素材。

## 关键产物速览

- `drafts/manuscript/latest.md`：1–747 章连续校订稿。
- `drafts/chapters/s1-boundary-beyond/c001-c018`：S1 分章精修稿（V4 换名）。
- `wiki/`：V4 换名后 249 内容页、247 ID。
- `reports/full-renaming-plan-v4-20261009.md`：V4 换名完整映射。
- `decisions/dec-20261009-013-v4-renaming-approval.md`：V4 批准决策与迁移记录。
