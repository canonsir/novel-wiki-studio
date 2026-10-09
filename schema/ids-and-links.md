# ID 与链接约定

| 类型 | 前缀 | 示例 |
|---|---|---|
| source | `src-` | `src-20261008-001` |
| character | `char-` | `char-lin-ye` |
| location | `loc-` | `loc-old-station` |
| faction | `fac-` | `fac-night-watch` |
| event | `evt-` | `evt-station-fire` |
| scene | `scn-` | `scn-v01-c003-002` |
| clue | `clue-` | `clue-broken-watch` |
| object | `obj-` | `obj-broken-watch` |
| system | `sys-` | `sys-memory-trade` |
| decision | `dec-` | `dec-20261008-ending` |

ID 使用小写 ASCII kebab-case。标题可中文。ID 一经被引用不应随标题改动；合并页面时保留旧页并写 `status: merged` 与目标链接。

双链使用相对于 `wiki/` 的实际页面路径，例如
`[[characters/char-lin-ye|林野]]`。目录使用规范英文类型名，文件名使用稳定 ID；
自动化工具仍以 frontmatter `type` 和 `id` 为准，不从显示标题推断实体类型。
普通 Markdown 阅读器不解析双链时，仍可通过索引导航。
