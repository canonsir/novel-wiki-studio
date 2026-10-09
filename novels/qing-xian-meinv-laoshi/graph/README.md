# 《我的江湖》闭环图谱

`story-graph.json` 是从正式 `wiki/`、747 章完整校订稿和重构章节生成的
FlowGram 数据文件。它用于全局审阅，不替代 Wiki 权威事实。

```bash
python3 scripts/build_story_graph.py novels/qing-xian-meinv-laoshi
python3 scripts/lint_story_graph.py novels/qing-xian-meinv-laoshi
npm run dev
```

查看器支持主干、实体、章节和全量四种视图；单击节点可查看来源与状态。
