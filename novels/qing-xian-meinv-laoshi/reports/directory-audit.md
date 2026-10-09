# 小说目录整理报告

日期：2026-10-09

## 整理原则

- `raw/` 只保存不可变来源；
- `wiki/` 只保存当前有效知识页；
- `drafts/manuscript/latest.md` 是唯一完整阅读稿；
- `drafts/chapters/` 保存比完整稿更先进的分章重构；
- 历史版本由 Git 保存，不在小说目录复制归档；
- `graph/` 只保存从当前 Wiki 和最新正文生成的派生图谱。

## 已删除的冗余

| 原目录/文件 | 原因 | 当前替代 |
|---|---|---|
| `99-archive/` | 与正式 Wiki 重复，形成第二事实源 | Git 历史 |
| `drafts/complete/*-v1.md` | 已被校订稿替代 | `drafts/manuscript/latest.md` |
| `drafts/重写正文/` | 与分章稿、补章完全重复 | `drafts/chapters/` |
| `00-admin/` | 管理说明与 README、报告重复 | 根 README + `reports/reconstruction-status.md` |
| `05-sources/` | 空目录且与 `raw/` 重复 | `raw/` |
| `drafts/volumes/` | 空目录，分部规划已在 Wiki | `wiki/structure/` |
| 小说内 `_*-template.md` | 模板不是小说事实 | 仓库根 `_template/` |

## 已修复的断层

- 六部目录从不连续的 S1/S2/S5 补齐为 S1-S6；
- S1第1-18章统一使用小写 kebab-case 文件名；
- S2/S5补章补齐状态 frontmatter；
- 198个既有 Wiki 页面迁移为标准类型目录和稳定 ID 文件名；
- 补充S1缺失人物、地点、天悦集团、主题、5个独立伏笔、4个关键物件；
- 从S1最新重构稿生成18个章级场景卡；
- 分类索引改为根据 frontmatter 自动生成；
- 图谱生成器改为只读取 `drafts/manuscript/latest.md` 和 `drafts/chapters/`。

## 仍未完成

- S1第19-30章尚未重构；
- S2-S6尚未完成逐章原创重构；
- “夏建国/夏启明”姓名冲突已于 2026-10-09 按用户决定统一为“夏启明”（CON-006 resolved）；
- 18个S1章级场景卡进入短剧生产前还需继续拆成地点级场景。
