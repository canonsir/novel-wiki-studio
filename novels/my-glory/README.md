# 我的荣耀

本目录由项目模板生成。先填写 `novel.yaml`，再将原稿放入 `raw/manuscript/`，随后执行导入流程。

## 当前阶段

- [ ] 原稿已保存且未修改
- [ ] 来源权利已确认，可用于重构与发布
- [ ] 已确认最终目标为用户主导的原创小说成品
- [ ] `novel.yaml` 已填写
- [ ] 已完成全文导入
- [ ] 已确认核心命题、目标读者和结局边界
- [ ] 已生成首轮结构诊断
- [ ] 已完成原创性检查，不是换词、调序、拼接或可识别模仿
- [ ] 已运行 Wiki 静态检查
- [ ] 已生成 `graph/story-graph.json` 并通过闭环检查

## 闭环图谱

每次新增或修改人物、地点、势力、事件、术语、章节后运行：

```bash
python3 scripts/build_story_graph.py novels/my-glory
python3 scripts/lint_story_graph.py novels/my-glory
```

公共查看器通过 `npm run dev` 启动。图谱必须覆盖完整正文全部章节和全部正式
Wiki 实体，且孤点为 0。
