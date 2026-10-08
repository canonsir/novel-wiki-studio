#!/usr/bin/env python3
"""为每个中文子目录生成 _index.md AI 导航文件。"""
import re
from pathlib import Path

BASE = Path("/Users/dongyanyang/Documents/工程/随便玩玩/novel-wiki-studio/novels/qing-xian-meinv-laoshi")
WIKI = BASE / "wiki"

DIRS = {
    "人物": ("character", "人物档案（含主角、反派、配角）", "核心人物、势力归属、关联事件"),
    "势力": ("faction", "势力档案（帮派、集团、组织）", "势力层级、核心人物、地盘分布"),
    "地点": ("location", "地点档案（场所、城市、基地）", "拍摄地点、所属势力、发生事件"),
    "事件": ("event", "关键事件档案", "事件时间线、涉及人物、前因后果"),
    "关系": ("relationship", "人物关系图谱", "关系矩阵、核心关系线"),
    "伏笔": ("clue", "伏笔账本", "已埋伏笔、回收状态、关联章节"),
    "剧情": ("plot", "剧情结构与改编路线", "故事结构、短剧改编规划"),
    "时间线": ("timeline", "主时间线", "按时间顺序排列的关键事件节点"),
    "术语": ("term", "专有名词与术语", "世界观内的特定概念与黑话"),
    "系统": ("system", "世界观内的系统规则", "能力体系、增长机制、视觉圣经"),
    "世界": ("world", "世界观设定", "世界圣经、地点映射参考"),
    "场景": ("scene", "场景规则与模板", "场景写作规范、视频改编参考"),
    "风格": ("style", "文风圣经", "叙事风格、语言调性、描写规范"),
    "矛盾": ("continuity", "连续性矛盾登记", "设定冲突、需要解决的不一致"),
    "结构": ("structure", "分卷与整体结构规划", "小说分卷方案"),
    "主题": ("theme", "主题规划", "核心主题与表达方向"),
}


def parse_frontmatter(text):
    """提取 frontmatter 里的 id、title、canon、status。"""
    fm = {}
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if m:
        block = m.group(1)
        for key in ("id", "title", "canon", "status"):
            km = re.search(rf'^{key}:\s*(.+)$', block, re.MULTILINE)
            if km:
                fm[key] = km.group(1).strip().strip('"').strip("'")
    return fm


def generate_index(dir_name):
    zh_dir = WIKI / dir_name
    if not zh_dir.exists():
        return None
    
    type_key, desc, focus = DIRS.get(dir_name, ("other", "", ""))
    
    entries = []
    for f in sorted(zh_dir.iterdir()):
        if f.suffix != ".md":
            continue
        if f.name.startswith("_"):
            continue
        if f.name == "_index.md":
            continue
        
        text = f.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        
        title = fm.get("title", f.stem)
        item_id = fm.get("id", "")
        canon = fm.get("canon", "unknown")
        status = fm.get("status", "unknown")
        
        entries.append({
            "file": f.name,
            "stem": f.stem,
            "title": title,
            "id": item_id,
            "canon": canon,
            "status": status,
        })
    
    # 按确认状态分组
    confirmed = [e for e in entries if e["canon"] == "confirmed"]
    others = [e for e in entries if e["canon"] != "confirmed"]
    
    lines = []
    lines.append(f"# {dir_name}目录 AI 索引")
    lines.append("")
    lines.append(f"> {desc}。{focus}。")
    lines.append(">")
    lines.append(f"> **文件数**：{len(entries)} 个（confirmed {len(confirmed)} / other {len(others)}）")
    lines.append("")
    
    # 核心列表（confirmed）
    if confirmed:
        lines.append("## 核心条目（confirmed）")
        lines.append("")
        for e in confirmed[:20]:  # 最多 20 个
            id_str = f" · `{e['id']}`" if e["id"] else ""
            lines.append(f"- [[{dir_name}/{e['stem']}|{e['title']}]]{id_str}")
        if len(confirmed) > 20:
            lines.append(f"- *... 还有 {len(confirmed)-20} 个 confirmed*")
        lines.append("")
    
    # 完整索引表（精简）
    lines.append("## 完整文件索引")
    lines.append("")
    lines.append("| 文件名 | canon | 原英文ID |")
    lines.append("|---|---|---|")
    for e in entries:
        id_str = e["id"] if e["id"] else ""
        lines.append(f"| [{e['title']}]({e['stem']}.md) | {e['canon']} | `{id_str}` |")
    lines.append("")
    
    # 关联目录
    related = []
    if dir_name == "人物":
        related = ["势力", "事件", "关系", "地点"]
    elif dir_name == "势力":
        related = ["人物", "地点", "事件"]
    elif dir_name == "地点":
        related = ["势力", "事件"]
    elif dir_name == "事件":
        related = ["人物", "势力", "地点", "时间线"]
    elif dir_name == "关系":
        related = ["人物"]
    elif dir_name == "伏笔":
        related = ["事件", "剧情"]
    elif dir_name == "剧情":
        related = ["事件", "伏笔", "时间线", "风格"]
    elif dir_name == "时间线":
        related = ["事件", "剧情"]
    elif dir_name == "术语":
        related = ["世界", "系统"]
    elif dir_name == "系统":
        related = ["世界", "术语"]
    elif dir_name == "世界":
        related = ["系统", "术语", "地点"]
    elif dir_name == "场景":
        related = ["事件", "风格", "剧情"]
    elif dir_name == "风格":
        related = ["剧情", "场景"]
    elif dir_name == "矛盾":
        related = ["人物", "势力", "事件"]
    elif dir_name == "结构":
        related = ["剧情", "时间线"]
    elif dir_name == "主题":
        related = ["剧情", "风格"]
    
    if related:
        lines.append("## 关联目录")
        lines.append("")
        for r in related:
            if (WIKI / r / "_index.md").exists() or (WIKI / r).exists():
                lines.append(f"- [[{r}/|{r}目录]]")
        lines.append("")
    
    return "\n".join(lines)


def main():
    created = 0
    for dir_name in DIRS:
        content = generate_index(dir_name)
        if content:
            target = WIKI / dir_name / "_index.md"
            target.write_text(content, encoding="utf-8")
            print(f"  创建 {dir_name}/_index.md")
            created += 1
    
    print(f"\n共创建 {created} 个 _index.md")


if __name__ == "__main__":
    main()
