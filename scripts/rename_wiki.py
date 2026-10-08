#!/usr/bin/env python3
"""wiki/ 目录和文件中文重命名脚本。

执行顺序：
1. 重命名文件（英文目录+英文名 → 英文目录+中文名，目录此时还是英文）
2. 重命名子目录（英文→中文）
3. 批量更新所有 .md 中的 wikilink（英文目录前缀→中文目录前缀）
"""

import os
import re
import shutil
from pathlib import Path

BASE = Path("/Users/dongyanyang/Documents/工程/随便玩玩/novel-wiki-studio/novels/qing-xian-meinv-laoshi")
WIKI = BASE / "wiki"
REWRITTEN = BASE / "drafts/chapters/rewritten"

# ========== 目录重命名映射 ==========
DIR_RENAME = {
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

# ========== 特殊文件重命名 ==========
SPECIAL_FILE_RENAME = {
    # 人物/
    "characters/character-arc-bible.md": "人物线总圣经.md",
    # 势力/
    "factions/faction-power-map.md": "势力版图.md",
    # 地点/
    "locations/location-asset-atlas.md": "地点资产图谱.md",
    # 事件/
    "events/event-spine.md": "事件骨架.md",
    # 剧情/
    "plot/structure.md": "故事结构.md",
    "plot/short-drama-roadmap.md": "短剧路线.md",
    # 关系/
    "relationships/relationship-matrix.md": "关系矩阵.md",
    "relationships/relationship-overview.md": "关系总表.md",
    # 伏笔/
    "clues/clue-ledger.md": "伏笔账本.md",
    # 时间线/
    "timeline/master-timeline.md": "主时间线.md",
    # 风格/
    "style/style-bible.md": "文风圣经.md",
    # 系统/
    "systems/system-three-growth-engines.md": "三线增长系统.md",
    "systems/system-video-visual-bible.md": "视觉圣经.md",
    "systems/system-ability-and-combat.md": "能力与战力.md",
    # 世界/
    "world/world-bible.md": "世界圣经.md",
    "world/location-mapping.md": "地点映射.md",
    # 矛盾/
    "continuity/contradictions.md": "矛盾登记.md",
    # 结构/
    "structure/novel-volumes.md": "分卷规划.md",
    # 场景/
    "scenes/scene-rules.md": "场景规则.md",
}

# Template 文件保留原名
TEMPLATE_FILES = {
    "characters/_character-template.md",
    "factions/_faction-template.md",
    "locations/_location-template.md",
    "events/_event-template.md",
    "systems/_system-template.md",
    "terms/_term-template.md",
    "themes/_theme-template.md",
    "scenes/_scene-template.md",
}

# 根目录文件保留原名
ROOT_FILES = {"overview.md", "index.md", "log.md"}


def parse_index_for_names():
    """从 index.md 提取所有文件的 {旧路径: 中文名} 映射。"""
    names = {}
    index_path = WIKI / "index.md"
    text = index_path.read_text(encoding="utf-8")
    for m in re.finditer(r'\[\[([^\]|]+)\|([^\]]+)\]\]', text):
        old_path = m.group(1).replace("\\", "/")
        display = m.group(2)
        if "/" in old_path:
            names[old_path] = display
    return names


def build_full_file_mapping(index_names):
    """构建 {旧相对路径: 新文件名} 映射（目录名保持英文，只改文件名）。"""
    mapping = {}
    
    for root, dirs, files in os.walk(WIKI):
        for f in files:
            if not f.endswith(".md"):
                continue
            
            full = Path(root) / f
            rel = full.relative_to(WIKI)
            rel_str = str(rel).replace("\\", "/")
            
            # 跳过根目录文件
            if "/" not in rel_str:
                continue
            
            # Template 文件保留原名
            if rel_str in TEMPLATE_FILES:
                continue
            
            # 特殊文件
            if rel_str in SPECIAL_FILE_RENAME:
                mapping[rel_str] = SPECIAL_FILE_RENAME[rel_str]
                continue
            
            # 从 index.md 找
            idx_key = rel_str
            if idx_key in index_names:
                mapping[rel_str] = index_names[idx_key] + ".md"
                continue
            
            # 从 frontmatter title 提取
            try:
                content = full.read_text(encoding="utf-8")
                title_match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
                if title_match:
                    title = title_match.group(1).strip().strip('"').strip("'")
                    mapping[rel_str] = title + ".md"
                    continue
            except Exception:
                pass
            
            # 兜底：保留原名（不加入 mapping）
    
    return mapping


def step1_rename_files(file_mapping):
    """重命名文件：目录保持英文，只改文件名为中文名。"""
    print("\n=== Step 1: 重命名文件（目录保持英文）===")
    renamed = 0
    skipped = 0
    for old_rel, new_name in sorted(file_mapping.items()):
        old_full = WIKI / old_rel
        if not old_full.exists():
            print(f"  SKIP (不存在): {old_rel}")
            skipped += 1
            continue
        
        old_parent = old_full.parent
        new_full = old_parent / new_name
        
        if old_full.name == new_name:
            skipped += 1
            continue
        
        if new_full.exists():
            print(f"  SKIP (目标已存在): {old_rel} → {new_name}")
            skipped += 1
            continue
        
        # 确保目标路径没有冲突
        if old_full == new_full:
            continue
        
        print(f"  {old_rel} → {old_full.parent.name}/{new_name}")
        shutil.move(str(old_full), str(new_full))
        renamed += 1
    
    print(f"  重命名 {renamed} 个文件，跳过 {skipped} 个")
    return renamed


def step2_rename_dirs():
    """重命名子目录：英文 → 中文。"""
    print("\n=== Step 2: 重命名子目录 ===")
    count = 0
    for en, zh in DIR_RENAME.items():
        en_path = WIKI / en
        zh_path = WIKI / zh
        if en_path.exists() and not zh_path.exists():
            print(f"  {en}/ → {zh}/")
            shutil.move(str(en_path), str(zh_path))
            count += 1
        elif zh_path.exists():
            print(f"  SKIP: {zh}/ 已存在")
        else:
            print(f"  SKIP: {en}/ 不存在")
    print(f"  重命名 {count} 个目录")
    return count


def step3_update_links(search_dirs):
    """批量更新 wikilink：英文目录前缀 → 中文目录前缀。"""
    print("\n=== Step 3: 更新 wikilink 中的目录前缀 ===")
    
    # 构建替换对
    repl_pairs = []
    for en, zh in DIR_RENAME.items():
        repl_pairs.append((f"[[{en}/", f"[[{zh}/"))
        # 也处理可能在其他地方出现的纯路径引用
        repl_pairs.append((f">{en}/", f">{zh}/"))
        repl_pairs.append((f"({en}/", f"({zh}/"))
    
    total_files = 0
    total_repl = 0
    
    for search_dir in search_dirs:
        if not search_dir.exists():
            continue
        for md_file in search_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            original = content
            file_repl = 0
            
            for old, new in repl_pairs:
                n = content.count(old)
                if n > 0:
                    content = content.replace(old, new)
                    file_repl += n
            
            if content != original:
                md_file.write_text(content, encoding="utf-8")
                total_files += 1
                total_repl += file_repl
    
    print(f"  共更新 {total_files} 个文件，{total_repl} 处链接")
    return total_files, total_repl


def main():
    print("=" * 60)
    print("Wiki 中文重命名脚本 v2（先文件后目录）")
    print("=" * 60)
    
    # 1. 解析 index.md 获取中文名映射
    print("\n解析 index.md ...")
    index_names = parse_index_for_names()
    print(f"  从 index.md 提取 {len(index_names)} 个中文名映射")
    
    # 2. 构建完整文件映射
    file_mapping = build_full_file_mapping(index_names)
    print(f"  构建 {len(file_mapping)} 个文件的重命名映射")
    
    # 3. 先重命名文件
    step1_rename_files(file_mapping)
    
    # 4. 再重命名目录
    step2_rename_dirs()
    
    # 5. 更新所有 wikilink
    step3_update_links([WIKI, REWRITTEN])
    
    print("\n" + "=" * 60)
    print("重命名 + 链接更新完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
