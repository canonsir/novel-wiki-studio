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
| system | `sys-` | `sys-memory-trade` |
| decision | `dec-` | `dec-20261008-ending` |

ID 使用小写 ASCII kebab-case。标题可中文。ID 一经被引用不应随标题改动；合并页面时保留旧页并写 `status: merged` 与目标链接。

双链使用相对于 `wiki/` 的实际页面路径，例如
`[[人物/林野|林野]]` 或 `[[characters/lin-ye|林野]]`。目录和文件可以使用中文或英文；
稳定身份由 frontmatter `id` 提供，自动化工具不得从目录名推断实体类型。
普通 Markdown 阅读器不解析双链时，仍可通过索引导航。
