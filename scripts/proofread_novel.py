#!/usr/bin/env python3
"""Create a readable proofread edition and a chapter-level editorial ledger."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOVEL = ROOT / "novels" / "qing-xian-meinv-laoshi"
SOURCE = NOVEL / "drafts" / "complete" / "qing-xian-meinv-laoshi-reconstructed-v1.md"
OUTPUT = NOVEL / "drafts" / "complete" / "qing-xian-meinv-laoshi-reconstructed-v2-proofread.md"
REPORT = NOVEL / "reports" / "lint" / "2026-10-08-chapter-proofread-ledger.md"

PLATFORM_MARKERS = (
    "求推荐", "求打赏", "求订阅", "求钻石", "求金钻", "加更", "第更",
    "更送到", "更完成", "点击破", "推荐票", "捧场", "豪赏", "欢迎贴吧",
    "兄弟们久等", "大家久等", "新年快乐", "除夕快乐", "国庆节快乐",
    "元旦快乐", "生日快乐", "不想看啪", "可不订阅", "可不填",
)

EXACT_REPLACEMENTS = {
    "得确": "的确",
    "再这里": "在这里",
    "在一次来": "再一次来",
    "在一次回来": "再一次回来",
    "在一次给": "再一次给",
    "脑袋一下子当机了，，": "脑袋一下子当机了，",
    "我是一名光荣的屌丝大学狗。.": "我是一名光荣的屌丝大学狗。",
    "响，我在罗莉": "响。我在罗莉",
    "走没在学院里面走过": "还没在学院里面走过",
    "医院节雨姐": "医院接雨姐",
    "机场节雨姐": "机场接雨姐",
    "紧紧只到了": "仅仅只到了",
    "再也睡意": "再也没有睡意",
    "倒下啊眼镜蛇": "倒下的眼镜蛇",
    "他也应该是没有想到": "他应该也没有想到",
}


@dataclass
class ChangeCounts:
    punctuation: int = 0
    typos: int = 0
    headings: int = 0
    splits: int = 0


def clean_title(title: str, counts: ChangeCounts) -> str:
    original = title.strip()
    title = original
    title = re.sub(r"\s*[（(][^）)]*(?:求|更|推荐|打赏|订阅|快乐|贴吧|点击)[^）)]*[）)]\s*$", "", title)
    suffix_patterns = (
        r"\s*第[一二三四五六七八九十]+更(?:了)?[！!。.]?$",
        r"\s+感谢.*$",
        r"\s+祝.*$",
        r"\s+(?:除夕|新年|元旦|国庆节)快乐.*$",
        r"\s+大家新春快乐.*$",
        r"\s+喜迎\d+.*$",
        r"\s+(?:为|如为)\S+加更.*$",
        r"\s+第五更求钻石.*$",
    )
    for pattern in suffix_patterns:
        title = re.sub(pattern, "", title)
    for marker in PLATFORM_MARKERS:
        pos = title.find(marker)
        if pos >= 0:
            prefix = title[:pos].rstrip(" ，。！!？?：:")
            if "为" in prefix[-18:]:
                prefix = re.sub(r"\s+为\S*$", "", prefix)
            title = prefix
            break
    title = re.sub(r"\s+为(?:18K纯牛奶|宋哥|Anko|Curtis_Q|狼舞春秋|季末更丶寂默|万年潜水党|土豪的寂寞|浪荡中的莮秂)\S*$", "", title)
    title = title.strip(" ，。")
    if title != original:
        counts.headings += 1
    return title or original


def normalize_text(text: str, counts: ChangeCounts) -> str:
    for old, new in EXACT_REPLACEMENTS.items():
        occurrences = text.count(old)
        if occurrences:
            text = text.replace(old, new)
            counts.typos += occurrences

    rules = (
        (r"，{2,}", "，"),
        (r"。{2,}", "。"),
        (r"[，。]*\.(?=\s|$|[”’])", "。"),
        (r"，。|。，|，；", "。"),
        (r"：，", "："),
        (r"，，", "，"),
        (r"！。|。！", "！"),
        (r"？。|。？", "？"),
        (r"\s+([，。！？；：])", r"\1"),
        (r"([，。！？；：])(?=[“])", r"\1"),
        (r"\*{5}\.?", "\n---\n"),
        (r"\.(?=。)", ""),
        (r"。\.(?=\S)", "。"),
        (r"(?<=[\u4e00-\u9fff”’])\.(?=[\u4e00-\u9fff“‘])", "。"),
    )
    for pattern, replacement in rules:
        text, number = re.subn(pattern, replacement, text)
        counts.punctuation += number

    ascii_rules = {
        ",": "，",
        "!": "！",
        "?": "？",
        ";": "；",
        ":": "：",
    }
    for old, new in ascii_rules.items():
        pattern = rf"(?<=[\u4e00-\u9fff”’])\{old}(?=[\u4e00-\u9fff“‘])"
        text, number = re.subn(pattern, new, text)
        counts.punctuation += number

    text, number = re.subn(r'"([^"\n]{1,160})"', r"“\1”", text)
    counts.punctuation += number
    text, number = re.subn(r"。{2,}", "。", text)
    counts.punctuation += number
    return text.strip()


def split_long_paragraph(text: str, counts: ChangeCounts, limit: int = 180) -> list[str]:
    if len(text) <= limit or text.startswith(("#", ">", "|", "---")):
        return [text]
    sentences = re.split(r"(?<=[。！？])", text)
    if len(sentences) == 1:
        return [text]
    paragraphs: list[str] = []
    current = ""
    for sentence in sentences:
        if current and len(current) + len(sentence) > limit:
            paragraphs.append(current.strip())
            current = sentence
        else:
            current += sentence
    if current.strip():
        paragraphs.append(current.strip())
    if len(paragraphs) > 1:
        counts.splits += len(paragraphs) - 1
    return paragraphs


def classify_chapter(title: str, body: str, char_count: int) -> list[str]:
    flags: list[str] = []
    if char_count < 1200:
        flags.append("篇幅偏短")
    elif char_count > 4500:
        flags.append("篇幅偏长")
    if re.search(r"未成年|十[五六七]岁|高中", body) and re.search(r"开房|亲|胸|性|处女|床", body):
        flags.append("未成年相关内容需人工复核")
    if re.search(r"绑架|中枪|杀|枪战|强行|下药|迷药", title + body):
        flags.append("动作/伤势/法律后果需核对")
    if re.search(r"一血|名器|xxOO|啪啪啪|车震|榨干|开房", title + body, re.I):
        flags.append("成人内容需按短剧尺度重构")
    if re.search(r"神秘|身份|身世|后台|老道士|五大家族|神龙", title + body):
        flags.append("伏笔与后台兑现需核对")
    if not flags:
        flags.append("常规语言校对")
    return flags


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    intro, *raw_chapters = re.split(r"(?=^## 第\d+章 )", source, flags=re.MULTILINE)
    intro = intro.replace("连续性重构基线版", "全文校订版")
    intro = intro.replace(
        "> 四篇补章为重构提案；全文深度原创重写按重构账本持续替换。",
        "> 四篇补章为重构提案。本版已统一标题、标点和段落；剧情级深度重写按重构账本持续替换。",
    )
    output_parts = [intro.strip()]
    report_rows: list[str] = []
    total = ChangeCounts()

    for raw in raw_chapters:
        heading, _, body = raw.partition("\n")
        match = re.match(r"## 第(\d+)章\s*(.*)", heading)
        if not match:
            continue
        number = int(match.group(1))
        title = clean_title(match.group(2), total)
        chapter_counts = ChangeCounts()
        cleaned = normalize_text(body, chapter_counts)
        paragraphs: list[str] = []
        for line in cleaned.splitlines():
            line = line.strip()
            if not line:
                continue
            paragraphs.extend(split_long_paragraph(line, chapter_counts))
        output_parts.append(f"## 第{number}章 {title}\n\n" + "\n\n".join(paragraphs))

        total.punctuation += chapter_counts.punctuation
        total.typos += chapter_counts.typos
        total.splits += chapter_counts.splits
        flags = "；".join(classify_chapter(title, cleaned, len(cleaned)))
        report_rows.append(
            f"| {number} | {title.replace('|', '／')} | {len(cleaned)} | {len(paragraphs)} | "
            f"{chapter_counts.typos} | {chapter_counts.punctuation} | {chapter_counts.splits} | {flags} |"
        )

    OUTPUT.write_text("\n\n".join(output_parts).rstrip() + "\n", encoding="utf-8")
    report = [
        "# 747章逐章审校台账",
        "",
        "本台账记录机器可确定的文本修复和需要人工剧情重构的风险。标记风险不等于已经判定剧情错误。",
        "",
        "## 自动修复汇总",
        "",
        f"- 标题平台噪声清理：{total.headings}",
        f"- 确定性错字修复：{total.typos}",
        f"- 标点修复：{total.punctuation}",
        f"- 长段拆分：{total.splits}",
        "- Markdown段落：所有小说段落之间加入空行，确保阅读器正确分段。",
        "",
        "## 逐章记录",
        "",
        "| 章 | 标题 | 字符 | 段落 | 错字 | 标点 | 拆段 | 剧情/短剧复核项 |",
        "|---:|---|---:|---:|---:|---:|---:|---|",
        *report_rows,
        "",
    ]
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"proofread: {OUTPUT}")
    print(f"ledger: {REPORT}")
    print(total)


if __name__ == "__main__":
    main()
