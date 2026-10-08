#!/usr/bin/env python3
"""更新 index.md：英文标题→中文，英文文件名→中文名。"""
import re
from pathlib import Path

BASE = Path("/Users/dongyanyang/Documents/工程/随便玩玩/novel-wiki-studio/novels/qing-xian-meinv-laoshi")
WIKI = BASE / "wiki"
REWRITTEN = BASE / "drafts/chapters/rewritten"

# ========== 旧英文目录前缀 → 中文目录前缀（用于从链接推断中文名）==========
DIR_EN_TO_ZH = {
    "characters": "人物",
    "factions": "势力",
    "locations": "地点",
    "events": "事件",
    "relationships": "关系",
    "clues": "伏笔",
    "plot": "剧情",
    "timeline": "时间线",
    "terms": "术语",
    "systems": "系统",
    "world": "世界",
    "scenes": "场景",
    "style": "风格",
    "continuity": "矛盾",
    "structure": "结构",
    "themes": "主题",
}

# ========== 目录下的文件映射（旧英文名 → 新中文名）==========
# 从实际文件系统构建：遍历所有中文目录，读取每个 .md 的 frontmatter title
def build_file_renames():
    """返回 {中文目录/旧英文文件名.md: 中文名}。
    
    其实我们需要的是：对每个 [[中文目录/旧英文名|显示文字]]，
    把旧英文名换成（显示文字 + .md 去掉.md）作为新文件名。
    或者更直接：用显示文字作为文件名。
    """
    renames = {}
    
    for zh_dir in DIR_EN_TO_ZH.values():
        dir_path = WIKI / zh_dir
        if not dir_path.exists():
            continue
        for f in dir_path.iterdir():
            if f.suffix != ".md":
                continue
            # 旧英文名格式：char-xxx.md / fac-xxx.md / loc-xxx.md / evt-xxx.md 等
            old_style = f.name
            # 新名字就是当前文件名（已经是中文了，因为 step1 改过）
            renames[f"{zh_dir}/{old_style}"] = f"{zh_dir}/{f.stem}"
    
    return renames


def fix_index_md():
    index_path = WIKI / "index.md"
    text = index_path.read_text(encoding="utf-8")
    
    # 1. 更新 section 标题
    title_repls = [
        ("## Overview", "## 总览"),
        ("## Characters", "## 人物"),
        ("## Factions", "## 势力"),
        ("## Locations", "## 地点"),
        ("## World & Systems", "## 世界与系统"),
        ("## Plot & Timeline", "## 剧情与时间线"),
        ("## Events & Scenes", "## 事件与场景"),
        ("## Relationships", "## 关系"),
        ("## Clues", "## 伏笔"),
        ("## Themes & Style", "## 主题与风格"),
        ("## Continuity", "## 矛盾"),
        ("## Reports / Open Questions", "## 报告与待办"),
        ("## Generated catalog", "## 自动生成目录"),
    ]
    
    for old, new in title_repls:
        text = text.replace(old, new)
    
    # 2. 更新 ### 二级标题
    section_repls = [
        ("### character", "### 人物"),
        ("### clue", "### 伏笔"),
        ("### event", "### 事件"),
        ("### faction", "### 势力"),
        ("### location", "### 地点"),
        ("### overview", "### 总览"),
        ("### plot", "### 剧情"),
        ("### relationship", "### 关系"),
        ("### report", "### 报告"),
        ("### style", "### 风格"),
        ("### system", "### 系统"),
        ("### term", "### 术语"),
        ("### timeline", "### 时间线"),
        ("### world", "### 世界"),
    ]
    
    for old, new in section_repls:
        text = text.replace(old, new)
    
    # 3. 修复 wikilink 里的英文文件名 → 中文名
    # 匹配 [[目录/英文拼音|显示文字]] → [[目录/显示文字|显示文字]]
    # 同时要去掉文件名尾部的 .md（如果存在）
    def fix_link(m):
        full = m.group(0)
        path = m.group(1)  # 目录/文件名 或 目录/文件名.md
        display = m.group(2)  # 显示文字
        
        # 如果路径里已经没有英文目录前缀了，处理文件名
        # path 形如 "人物/char-a-guang" 或 "势力/fac-lijia"
        parts = path.split("/", 1)
        if len(parts) == 2:
            zh_dir = parts[0]
            file_part = parts[1]
            
            # 如果 file_part 还是英文拼音风格（char-, fac-, loc- 等开头）
            if re.match(r'^(char-|fac-|loc-|evt-|term-|system-)', file_part):
                # 直接用显示文字作为新的文件名
                new_path = f"{zh_dir}/{display}"
                return f"[[{new_path}|{display}]]"
        
        return full
    
    text = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', fix_link, text)
    
    # 4. 根目录文件（overview, index, log）保留原名，不动
    
    index_path.write_text(text, encoding="utf-8")
    print("index.md 已更新：标题中文化 + 文件名修复")


def fix_all_wikilinks_in_wiki():
    """对所有 wiki/ 下的 md 文件，修复残留的英文文件名链接。"""
    print("\n修复所有 wiki 文件中的英文文件名链接...")
    
    total_fixes = 0
    for md_file in WIKI.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        original = content
        
        def fix_link(m):
            nonlocal total_fixes
            full = m.group(0)
            path = m.group(1)
            display = m.group(2)
            
            parts = path.split("/", 1)
            if len(parts) == 2:
                zh_dir = parts[0]
                file_part = parts[1]
                
                if re.match(r'^(char-|fac-|loc-|evt-|term-|system-|scene-)', file_part):
                    new_path = f"{zh_dir}/{display}"
                    total_fixes += 1
                    return f"[[{new_path}|{display}]]"
            
            return full
        
        content = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', fix_link, content)
        
        if content != original:
            md_file.write_text(content, encoding="utf-8")
    
    print(f"  共修复 {total_fixes} 处英文文件名链接")


def fix_rewritten():
    """对重写稿也做同样处理。"""
    print("\n修复重写稿中的链接...")
    if not REWRITTEN.exists():
        return
    
    total_fixes = 0
    for md_file in REWRITTEN.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        original = content
        
        def fix_link(m):
            nonlocal total_fixes
            full = m.group(0)
            path = m.group(1)
            display = m.group(2)
            
            parts = path.split("/", 1)
            if len(parts) == 2:
                zh_dir = parts[0]
                file_part = parts[1]
                
                if re.match(r'^(char-|fac-|loc-|evt-|term-|system-|scene-)', file_part):
                    new_path = f"{zh_dir}/{display}"
                    total_fixes += 1
                    return f"[[{new_path}|{display}]]"
            
            return full
        
        content = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', fix_link, content)
        
        if content != original:
            md_file.write_text(content, encoding="utf-8")
    
    print(f"  共修复 {total_fixes} 处")


def main():
    fix_index_md()
    fix_all_wikilinks_in_wiki()
    fix_rewritten()
    print("\n完成！")


if __name__ == "__main__":
    main()
