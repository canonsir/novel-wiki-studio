# skills/knowledge/

知识库维护类技能（资料管理员视角）：维护 `common/knowledge-base/` 的真实世界知识条目，保证虚实结合、索引同步。

## 当前技能

- `kb-extender/` — 按统一模板新增知识条目，并同步 README / AGENTS 索引、校验合规底线。
  - 入口：`SKILL.md`
  - 模板：`assets/entry-template.md`（新条目复制此模板）
  - 典型调用场景：用户要求扩展 / 补充知识库，或写作中发现高频领域无条目可依

## 加入新 skill 的最低要求

同 `writing/README.md`，且必须声明：
1. 维护对象（知识库条目 / 目录 / 索引）。
2. 与 `common/knowledge-base/README.md` 虚实底线的一致性。
3. 写入后必须同步的索引清单。
