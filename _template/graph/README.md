# 小说闭环图谱

`story-graph.json` 由 `scripts/build_story_graph.py` 生成，供公共 FlowGram 查看器读取。
它是 `novel.yaml`、正式 `wiki/`、完整正文和重构章节的派生索引，不是事实源。

每次更新 Wiki 或正文后必须重新生成并运行 `scripts/lint_story_graph.py`。
