# Git 工作流

## 分支建议

- `main`：已确认、可继续创作的稳定状态。
- `ingest/<source>`：导入新原稿或资料。
- `rewrite/<chapter>`：章节重构。
- `proposal/<idea>`：高风险新人物线、规则或结局实验。

## 提交粒度

一次提交尽量表达一个叙事变化，并同时包含正文与 Wiki 传播。例如：

```text
rewrite(ch03): strengthen the station confrontation
wiki(char-lin): record trust break and hand injury
lint: resolve timeline conflict after chapter 3 rewrite
```

避免把多章重写、世界观重构和格式整理塞进同一提交。

## 审阅重点

Git diff 不只看文句，还看：人物状态是否传播、时间线是否更新、伏笔是否登记、提案是否被错误标成 confirmed、raw 是否被修改。

## 合并前

运行静态检查，阅读报告，确认关键决定已写入 `decisions/`。`raw/` 的改动必须是新增来源，而不是覆盖旧原稿。
