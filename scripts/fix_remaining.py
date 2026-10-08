#!/usr/bin/env python3
"""修复所有剩余断链。"""
import re
from pathlib import Path

BASE = Path("/Users/dongyanyang/Documents/工程/随便玩玩/novel-wiki-studio/novels/qing-xian-meinv-laoshi")
WIKI = BASE / "wiki"
REWRITTEN = BASE / "drafts/chapters/rewritten"

# ========== 精确的替换对 ==========
# 从 旧 wikilink 内部路径 → 新 wikilink 内部路径
# 注意：[[path|display]] 的 path 部分
REPLACEMENTS = [
    # overview.md 和 index.md 里的旧文件名链接
    ("剧情/short-drama-roadmap", "剧情/短剧路线"),
    ("剧情/structure", "剧情/故事结构"),
    ("事件/event-spine", "事件/事件骨架"),
    ("矛盾/contradictions", "矛盾/矛盾登记"),
    ("时间线/master-timeline", "时间线/主时间线"),
    ("系统/能力、战力与行动规则", "系统/能力与战力"),
    ("系统/AI短剧视觉与声音圣经", "系统/视觉圣经"),
    ("系统/三线爽点增长系统", "系统/三线增长系统"),
    
    # 人物别名问题
    ("人物/海哥", "人物/吕润海"),
    ("人物/李虎", "人物/李振东"),  # 李虎可能是李振东的别名？或者原始遗留
    ("人物/刘起山", None),  # 这个可能原始就没文件，标记处理
    
    # 苏柒柒 相关
    ("人物/苏柒柒（罗刹女）", "人物/苏柒柒（罗刹女）"),  # 已经正确了
    ("人物/苏柒柒（罗刹）", "人物/苏柒柒（罗刹女）"),
    
    # 苏轻侯
    ("人物/苏轻侯（鬼组组长）", "人物/苏轻侯"),
    
    # 许乐
    ("人物/许乐（许明康）", "人物/许乐"),
    
    # 雨姐/夜叉的别名
    ("人物/叉（雨姐）", "人物/夜叉"),
]


def fix_wikilinks(content):
    """替换 content 里的 wikilink 内部路径。"""
    original = content
    
    # 处理 [[path|display]] 格式
    def fix_inner(m):
        inner = m.group(1)
        if "|" in inner:
            path, display = inner.split("|", 1)
        else:
            path = inner
            display = None
        
        path = path.strip()
        
        # 精确匹配替换
        new_path = path
        for old, new in REPLACEMENTS:
            if new is None:
                continue
            if path == old or path.startswith(old) or path.replace(".md", "") == old:
                new_path = new
                break
        
        if new_path != path:
            if display:
                return f"[[{new_path}|{display}]]"
            else:
                return f"[[{new_path}|{new_path.split('/')[-1]}]]"
        
        return m.group(0)
    
    content = re.sub(r'\[\[([^\]]+)\]\]', fix_inner, content)
    return content


def main():
    all_dirs = [WIKI, REWRITTEN]
    
    total_files = 0
    total_repl = 0
    
    for search_dir in all_dirs:
        if not search_dir.exists():
            continue
        for md_file in search_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            new_content = fix_wikilinks(content)
            if new_content != content:
                md_file.write_text(new_content, encoding="utf-8")
                total_files += 1
    
    print(f"修复 {total_files} 个文件")
    
    # 验证
    print("\n--- 验证 ---")
    broken = []
    for md_file in WIKI.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        for m in re.finditer(r'\[\[([^\]]+)\]\]', content):
            inner = m.group(1)
            path = inner.split("|")[0].strip()
            
            if path == "overview" or path == "index" or path == "log":
                continue
            
            if "/" in path:
                target = WIKI / f"{path}.md"
                if not target.exists():
                    broken.append(f"{md_file.relative_to(BASE)} → {path}")
            else:
                target = WIKI / f"{path}.md"
                if not target.exists():
                    broken.append(f"{md_file.relative_to(BASE)} → {path}")
    
    print(f"断链: {len(broken)}")
    for b in broken[:30]:
        print(f"  {b}")


if __name__ == "__main__":
    main()
