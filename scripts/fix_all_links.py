#!/usr/bin/env python3
"""终极断链修复脚本：基于实际文件系统构建完整映射，修复所有 md 文件中的链接。"""
import re
from pathlib import Path

BASE = Path("/Users/dongyanyang/Documents/工程/随便玩玩/novel-wiki-studio/novels/qing-xian-meinv-laoshi")
WIKI = BASE / "wiki"
REWRITTEN = BASE / "drafts/chapters/rewritten"

# 目录映射（英文→中文）
DIR_EN_TO_ZH = {
    "characters": "人物", "factions": "势力", "locations": "地点",
    "events": "事件", "relationships": "关系", "clues": "伏笔",
    "plot": "剧情", "timeline": "时间线", "terms": "术语",
    "systems": "系统", "world": "世界", "scenes": "场景",
    "style": "风格", "continuity": "矛盾", "structure": "结构",
    "themes": "主题",
}


def build_path_aliases():
    """构建所有可能的路径别名映射。
    
    返回 {旧路径字符串: 新路径字符串}，用于直接替换。
    旧路径可能是各种格式：
      characters/char-chen-zhaonan
      characters/char-chen-zhaonan.md
      人物/char-chen-zhaonan
      人物/陈照南.md
    新路径统一为：人物/陈照南（不带 .md 后缀）
    """
    aliases = {}
    
    # 遍历中文目录下的所有实际 .md 文件
    for zh_dir in DIR_EN_TO_ZH.values():
        dir_path = WIKI / zh_dir
        if not dir_path.exists():
            continue
        
        for f in dir_path.iterdir():
            if f.suffix != ".md":
                continue
            
            zh_name = f.stem  # 中文名（不带 .md）
            
            # 新路径（标准格式）
            new_path = f"{zh_dir}/{zh_name}"
            
            # 别名1: 英文目录/英文名（不带 .md）
            # 英文名 = f 被重命名之前的名字 = 从什么变成了 zh_name？
            # 我们需要从 backup 或文件名推断... 
            # 更简单的办法：读 frontmatter 的 id 字段！
            content = f.read_text(encoding="utf-8")
            id_match = re.search(r'^id:\s*(.+)$', content, re.MULTILINE)
            if id_match:
                file_id = id_match.group(1).strip()  # 如 char-chen-zhaonan
                # 提取英文前缀（去掉 char-/fac- 等）
                en_prefix = None
                for en, zh in DIR_EN_TO_ZH.items():
                    if zh == zh_dir:
                        en_prefix = en
                        break
                if en_prefix:
                    # 别名: 英文目录/id, 英文目录/id.md, 中文目录/id, 中文目录/id.md
                    aliases[f"{en_prefix}/{file_id}"] = new_path
                    aliases[f"{en_prefix}/{file_id}.md"] = new_path
                    aliases[f"{zh_dir}/{file_id}"] = new_path
                    aliases[f"{zh_dir}/{file_id}.md"] = new_path
            
            # 别名2: 特殊文件名（比如 faction-power-map, master-timeline 等）
            # 这些的 id 和文件名前缀不同
            # 从 backup 里的旧文件名推断... 或者直接用 frontmatter 里可能有的旧名字
            # 简化处理：对每个文件，把所有知道的旧路径格式都注册为别名
    
    # 根目录文件
    aliases["overview"] = "overview"
    aliases["overview.md"] = "overview"
    aliases["index"] = "index"
    aliases["index.md"] = "index"
    aliases["log"] = "log"
    aliases["log.md"] = "log"
    
    return aliases


def fix_all_links(search_dirs):
    """对指定目录下所有 md 文件，修复所有 wikilink。"""
    aliases = build_path_aliases()
    print(f"构建了 {len(aliases)} 个别名映射")
    
    total_files = 0
    total_repl = 0
    
    for search_dir in search_dirs:
        if not search_dir.exists():
            continue
        
        for md_file in search_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            original = content
            file_repl = 0
            
            # 处理 [[path|display]] 和 [[path]] 两种格式
            def fix_link(m):
                nonlocal file_repl
                full = m.group(0)
                inner = m.group(1)  # 里面的 path 部分
                
                if "|" in inner:
                    path, display = inner.split("|", 1)
                else:
                    path = inner
                    display = None
                
                path = path.strip()
                
                # 查别名表
                # 先精确匹配，再模糊匹配
                new_path = None
                if path in aliases:
                    new_path = aliases[path]
                elif f"{path}.md" in aliases:
                    new_path = aliases[f"{path}.md"]
                else:
                    # 检查 path 是否已经是标准格式且文件真实存在
                    target = WIKI / f"{path}.md"
                    if target.exists() or (WIKI / path).exists():
                        return full  # 已经是对的
                    
                    # 模糊匹配：尝试各种组合
                    for alias_old, alias_new in aliases.items():
                        if path == alias_old or path.startswith(alias_old):
                            new_path = alias_new
                            break
                
                if new_path and new_path != path:
                    file_repl += 1
                    if display:
                        return f"[[{new_path}|{display}]]"
                    else:
                        # 没有 display，用新文件名作为 display
                        new_display = new_path.split("/")[-1]
                        return f"[[{new_path}|{new_display}]]"
                
                return full
            
            content = re.sub(r'\[\[([^\]]+)\]\]', fix_link, content)
            
            if content != original:
                md_file.write_text(content, encoding="utf-8")
                total_files += 1
                total_repl += file_repl
    
    print(f"更新 {total_files} 个文件，{total_repl} 处链接")
    return total_files, total_repl


def verify_links():
    """检查所有 wikilink 是否指向真实存在的文件。"""
    broken = []
    
    for md_file in WIKI.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        for m in re.finditer(r'\[\[([^\]]+)\]\]', content):
            inner = m.group(1)
            path = inner.split("|")[0].strip()
            
            if "/" in path:
                # 子目录文件
                target = WIKI / f"{path}.md"
                if not target.exists():
                    # 也可能是子路径（指向子目录的 _index.md？但我们还没创建）
                    target_dir = WIKI / path
                    if not target_dir.exists():
                        broken.append(f"{md_file.relative_to(BASE)} → {path}")
            else:
                # 根目录文件
                target = WIKI / f"{path}.md"
                if not target.exists():
                    broken.append(f"{md_file.relative_to(BASE)} → {path}")
    
    return broken


def main():
    print("=" * 60)
    print("终极断链修复")
    print("=" * 60)
    
    fix_all_links([WIKI, REWRITTEN])
    
    print("\n--- 验证 ---")
    broken = verify_links()
    print(f"断链: {len(broken)}")
    for b in broken[:30]:
        print(f"  {b}")
    
    if len(broken) > 30:
        print(f"  ... 还有 {len(broken)-30} 个")


if __name__ == "__main__":
    main()
