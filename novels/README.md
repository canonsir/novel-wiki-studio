# Novels

每部小说占用一个 kebab-case 目录，例如：

```text
novels/the-last-lighthouse/
novels/city-under-rain/
```

请不要直接复制后忘记替换 ID；使用：

```bash
python3 scripts/new_novel.py "最后的灯塔" --slug the-last-lighthouse
```

小说之间默认互不共享世界观。若属于同一宇宙，请在各自 `novel.yaml` 的 `shared_universe` 填入同一 ID，并把真正共享的设定提升到未来的 `universes/<id>/`，避免相互复制后漂移。
