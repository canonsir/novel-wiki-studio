#!/usr/bin/env python3
"""Build framework-level & per-volume topology graphs for the story-graph app.

生成 7 个 NovelGraphDataset JSON:
- qing-xian-meinv-laoshi-framework.json  整部 6 部框架图
- qing-xian-meinv-laoshi-s1.json ... s6.json  每部拓扑图

数据手工定义（而非从 wiki 扫描），用于高层 review，不替代完整图谱。
"""
from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "apps" / "story-graph" / "public" / "data"
NOVEL_ID = "qing-xian-meinv-laoshi"
NOW = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def node(nid: str, title: str, kind: str, summary: str, x: int, y: int, canon: str = "proposed", status: str = "active") -> dict:
    return {
        "id": nid,
        "type": "novel-node",
        "meta": {"position": {"x": x, "y": y}},
        "data": {
            "title": title,
            "kind": kind,
            "summary": summary,
            "canon": canon,
            "status": status,
            "sourcePath": "reports/novel-framework-overview.md",
        },
    }


def edge(src: str, tgt: str, relation: str, weight: float = 1.0) -> dict:
    return {
        "sourceNodeID": src,
        "targetNodeID": tgt,
        "data": {"relation": relation, "weight": weight},
    }


def dataset(ident_suffix: str, title: str, nodes: list, edges: list) -> dict:
    return {
        "schemaVersion": 1,
        "novel": {
            "id": f"{NOVEL_ID}-{ident_suffix}",
            "title": title,
            "generatedAt": NOW,
        },
        "coverage": {
            "wikiPages": 0,
            "indexedPages": 0,
            "chapters": 0,
            "rewrittenChapters": 0,
            "linkedChapters": 0,
            "nodes": len(nodes),
            "edges": len(edges),
            "orphanNodes": 0,
        },
        "nodes": nodes,
        "edges": edges,
    }


# ============================================================
# 1) 整部 6 部框架图
# ============================================================
def build_framework() -> dict:
    nodes: list[dict] = []
    edges: list[dict] = []

    # 顶层根节点
    nodes.append(node("novel:root", "我的江湖（6部框架）", "root",
                      "6 部 / 747 章 / 205-225 万字", 0, 0, "confirmed"))

    # 三条增长曲线
    curves = [
        ("curve:romance",  "艳遇曲线",  "多关系叠加，每段承载不同情绪/资源/风险",  -1200, -600),
        ("curve:power",    "势力曲线",  "校园→场所→组织→跨城→跨境→家族→退离", -1200, 0),
        ("curve:patron",   "后台曲线",  "海哥→林老爷子→林青朝→苏云→卜立国→秦老头", -1200, 600),
    ]
    for cid, ct, cs, x, y in curves:
        nodes.append(node(cid, ct, "system", cs, x, y, "confirmed"))
        edges.append(edge("novel:root", cid, "贯穿"))

    # 6 部
    volumes = [
        ("vol:s1", "S1 边界之外", "大学屌丝→海迪新人", "霍凯 / 肥猫",
         "海哥眼神异常",  "沈雪瑶入场 / 林悦 / 徐甜", "16-20 集", 0, -1200),
        ("vol:s2", "S2 立规矩",   "狼舞经营者，组织者雏形", "肥猫夺权 / 狼舞风暴",
         "林老爷子神秘资金", "娜娜 / 顾雨晴 / 柳园", "18-24 集", 0, -800),
        ("vol:s3", "S3 会长",     "天下会成立，自己人处决", "海迪旧部 / 疯鹰 / 鬼组密信",
         "林青朝完整揭示", "林悦质疑 / 徐甜合作 / 白姐暧昧", "20-24 集", 0, -400),
        ("vol:s4", "S4 镜中人",   "承认自己与敌人相似", "霍寒 / 段婉清 / 鬼组",
         "鬼组正式出场 / 父辈线索", "沈雪瑶盟友 / 林悦回归 / 段婉清边界", "22-26 集", 0, 0),
        ("vol:s5", "S5 棋子",     "发现自己是棋子", "五大家族 / 鬼组高层 / 跨境武装",
         "卜立国 / 身世揭一半", "苏凝 / 雨姐 / 四女失联", "22-26 集", 0, 400),
        ("vol:s6", "S6 回家",     "主动退离权力中心", "鬼组最高层 / 秦老头考验",
         "秦老头完整现身", "沈雪瑶孩子 / 林悦事业 / 其余各归位", "20-24 集", 0, 800),
    ]
    for vid, vt, summ, oppo, patron, romance, drama, x, y in volumes:
        nodes.append(node(vid, vt, "category", summ, x, y, "confirmed"))
        edges.append(edge("novel:root", vid, "包含", 1.5))

        # 对手节点
        oid = f"{vid}:oppo"
        nodes.append(node(oid, f"对手: {oppo}", "faction", oppo, x + 500, y - 100))
        edges.append(edge(vid, oid, "外部冲突"))
        edges.append(edge("curve:power", vid, "推进"))

        # 后台节点
        pid = f"{vid}:patron"
        nodes.append(node(pid, f"后台: {patron}", "character", patron, x + 500, y + 100))
        edges.append(edge(vid, pid, "后台层级"))
        edges.append(edge("curve:patron", vid, "推进"))

        # 艳遇节点
        rid = f"{vid}:romance"
        nodes.append(node(rid, f"关系: {romance}", "character", romance, x - 500, y))
        edges.append(edge(vid, rid, "关系演化"))
        edges.append(edge("curve:romance", vid, "推进"))

        # 短剧集数
        did = f"{vid}:drama"
        nodes.append(node(did, drama, "term", f"短剧对应 {drama}", x, y + 180))
        edges.append(edge(vid, did, "短剧映射"))

    # 部间递进
    for i in range(5):
        edges.append(edge(volumes[i][0], volumes[i + 1][0], "承接", 2.0))

    return dataset("framework", "我的江湖 · 6 部整体框架", nodes, edges)


# ============================================================
# 2) 每部拓扑图
# ============================================================
VOLUME_SPECS = {
    "s1": {
        "title": "我的江湖 S1 · 边界之外",
        "chapters": "原稿第 1-30 章",
        "chen_state_in": "大二屌丝 / 果园少年",
        "chen_state_out": "海迪新人 / 普通身份破裂",
        "events": [
            ("evt:匹配",          "Soul 匿名约见",      "第 1 章揭面身份错位",         "character"),
            ("evt:雨夜宾馆",      "宾馆亲密试探",       "第 3 章风险临界",             "event"),
            ("evt:破门",          "霍凯破门",         "第 4 章控制曝光",             "event"),
            ("evt:反杀",          "酒瓶绝境反杀",       "第 5 章大高潮 ①",             "event"),
            ("evt:圈套",          "周斌诱捕",           "第 7-9 章",                   "event"),
            ("evt:染毒",          "强制染毒五天",       "第 9 章创伤源头",             "event"),
            ("evt:污点",          "调查停课",           "第 10-11 章",                 "event"),
            ("evt:留置",          "拘留结识海哥",       "第 12 章伏笔",                "event"),
            ("evt:围堵",          "海迪围堵",           "第 14-16 章",                 "event"),
            ("evt:清场",          "海哥一分钟清场",     "第 17 章大高潮 ②",            "event"),
            ("evt:入局",          "主动要求入局",       "第 18 章选择",                "event"),
            ("evt:皇城",          "皇城追债第一次动刀", "第 25 章代价显影",            "event"),
            ("evt:白姐",          "白姐登场",           "第 30 章新世界入口",          "event"),
        ],
        "characters": [
            ("char:陈浩南",   "男主 / POV",       "character"),
            ("char:沈雪瑶",   "青年教师 / 禁忌理想", "character"),
            ("char:周斌",     "室友 / 兄弟",       "character"),
            ("char:林悦",     "同学 / 现实锚点",   "character"),
            ("char:霍凯",   "本地富二代反派",    "character"),
            ("char:吕海",   "海哥 / 引路人",     "character"),
            ("char:徐甜",   "校园对手",          "character"),
            ("char:白姐",     "海迪经营者",        "character"),
            ("char:沈启明",   "沈雪瑶父 / 债务线", "character"),
        ],
        "locations": [
            ("loc:光速网咖",  "开场失意",   "location"),
            ("loc:红屋咖啡厅", "身份揭面",   "location"),
            ("loc:开频宾馆",  "宾馆破门",   "location"),
            ("loc:海迪",      "地下秩序入口", "location"),
            ("loc:皇城赌场",  "霍家资源",   "location"),
        ],
    },
    "s2": {
        "title": "我的江湖 S2 · 立规矩",
        "chapters": "原稿第 31-120 章",
        "chen_state_in": "海迪新人",
        "chen_state_out": "狼舞经营者 / 组织者雏形",
        "events": [
            ("evt:格斗训练", "雷哥训练营",         "成长蒙太奇",     "event"),
            ("evt:狼舞试营业", "酒瓶顶住肥猫手下", "大高潮 ①",       "event"),
            ("evt:狼舞风暴", "包厢客人死亡",       "外部布局危机",   "event"),
            ("evt:三天军令状", "分工 2 成把握",   "大高潮 ② 组织者转变", "event"),
            ("evt:柳园", "破局钥匙少女",         "纯净锚点",       "event"),
            ("evt:娜娜",   "主动投怀",             "差异化艳遇",     "event"),
            ("evt:顾雨晴",   "冷漠断绝",             "关系对照组",     "event"),
            ("evt:林爷资金", "来路不明的钱",       "后台第二层",     "event"),
            ("evt:断腿", "第一次主动断腿立规矩",   "白姐递纸巾",     "event"),
        ],
        "characters": [
            ("char:陈浩南", "场所经营者", "character"),
            ("char:雷哥", "格斗教练", "character"),
            ("char:张亮", "兄弟班底", "character"),
            ("char:乌龟罩", "分析成员", "character"),
            ("char:孙一刀", "打手", "character"),
            ("char:娜娜", "差异化艳遇", "character"),
            ("char:顾雨晴", "关系对照组", "character"),
            ("char:柳园", "破局钥匙", "character"),
            ("char:疯鹰", "肥猫猛将", "character"),
            ("char:林老爷子", "后台中层", "character"),
        ],
        "locations": [
            ("loc:狼舞", "舞厅 / 第一个自己的场所", "location"),
            ("loc:景程火锅", "日常场景", "location"),
            ("loc:皇城赌场", "霍家资源", "location"),
            ("loc:崔家巷", "柳巷周边", "location"),
        ],
    },
    "s3": {
        "title": "我的江湖 S3 · 会长",
        "chapters": "原稿第 121-220 章",
        "chen_state_in": "狼舞经营者",
        "chen_state_out": "天下会会长",
        "events": [
            ("evt:海哥之死", "深夜爆炸", "权力真空", "event"),
            ("evt:龙头选举", "天台 / 扔疯鹰下楼", "大高潮 ①", "event"),
            ("evt:天下会成立宴", "多关系桌次扫描", "大高潮 ②", "event"),
            ("evt:林青朝身份", "后台第三层揭示", "条件逐渐清晰", "event"),
            ("evt:处决自己人", "贪场子钱兄弟 / 林悦收拾行李", "道德代价", "event"),
            ("evt:鬼组密信", "林青朝在卖你", "S4 伏笔", "event"),
            ("evt:段婉清出场", "检察官 / 我知道你", "S4 伏笔", "event"),
            ("evt:父亲照片", "你爸还活着", "身世伏笔", "event"),
        ],
        "characters": [
            ("char:陈浩南", "会长身份", "character"),
            ("char:苏云", "后台中层新面孔", "character"),
            ("char:段婉清", "检察官 / 法与情", "character"),
            ("char:林青朝", "完整揭示", "character"),
            ("char:疯鹰", "军事夺权被压", "character"),
            ("char:林悦", "质疑想离开", "character"),
            ("char:徐甜", "有限合作", "character"),
            ("char:白姐", "暧昧保持距离", "character"),
        ],
        "locations": [
            ("loc:天下会总部", "装修中", "location"),
            ("loc:天龙大酒店", "成立宴", "location"),
        ],
    },
    "s4": {
        "title": "我的江湖 S4 · 镜中人",
        "chapters": "原稿第 221-423 章",
        "chen_state_in": "天下会会长",
        "chen_state_out": "城南统一 / 跨城联盟入口",
        "events": [
            ("evt:泰峰峰会", "一杯酒泼霍寒", "大高潮 ①", "event"),
            ("evt:段婉清抉择", "放你走 / 迟早让你后悔", "法与情", "event"),
            ("evt:城南统一", "最后堂口陷落 / 冯建的老婆孩子", "大高潮 ②", "event"),
            ("evt:霍凯孤注", "绑架沈雪瑶 / 打断腿", "第二次大冲突", "event"),
            ("evt:张亮重伤", "鬼组伏击 / 失控", "联盟危机", "event"),
            ("evt:帝都邀请函", "五大家族联席", "S5 入口", "event"),
            ("evt:父亲档案", "秦老头名字", "身世推进", "event"),
        ],
        "characters": [
            ("char:陈浩南", "城南之王", "character"),
            ("char:霍寒", "魔都房产大亨", "character"),
            ("char:段婉清", "法与情边界", "character"),
            ("char:冯建", "最后堂口对手", "character"),
            ("char:雨姐", "跨境伏笔", "character"),
            ("char:张亮", "重伤 / 关系震荡", "character"),
            ("char:沈雪瑶", "盟友关系确立", "character"),
            ("char:林悦", "回归承诺", "character"),
        ],
        "locations": [
            ("loc:泰峰大酒店", "峰会", "location"),
            ("loc:皇都大厦", "霍家总部", "location"),
            ("loc:城南堂口", "多场所切换", "location"),
        ],
    },
    "s5": {
        "title": "我的江湖 S5 · 棋子",
        "chapters": "原稿第 424-633 章",
        "chen_state_in": "城南之王",
        "chen_state_out": "家族棋局入场 / 身世揭一半",
        "events": [
            ("evt:帝都庄园", "五大家族第一次会面", "大高潮 ①", "event"),
            ("evt:魔都追逐", "滨江 / 沈雪瑶律师身份掩护", "跨城压力", "event"),
            ("evt:雾都困局", "坡道立交 / 空间上被压制", "新地图冲突", "event"),
            ("evt:暹罗联盟", "哈查将军 / 金三角", "大高潮 ②", "event"),
            ("evt:身世揭一半", "父亲与秦老头有关", "身世推进", "event"),
            ("evt:四女失联", "五千万勒索 / 两条线都救", "密集危机", "event"),
            ("evt:霍凯终局", "霍寒灭口 / 我跟你不一样", "镜中人反驳", "event"),
            ("evt:沈雪瑶怀孕", "你到底是谁的儿子", "S6 入口", "event"),
        ],
        "characters": [
            ("char:陈浩南", "全国级玩家", "character"),
            ("char:苏凝", "罗刹女 / 智性艳遇", "character"),
            ("char:雨姐", "跨境情报", "character"),
            ("char:骆璃", "帝都家族内部关系", "character"),
            ("char:哈查将军", "暹罗武装", "character"),
            ("char:卜立国", "顶层后台之一", "character"),
            ("char:霍寒", "家族棋局中清除弟弟", "character"),
            ("char:霍凯", "终局祭品", "character"),
        ],
        "locations": [
            ("loc:帝都庄园", "家族棋局入场", "location"),
            ("loc:魔都滨江", "追逐战", "location"),
            ("loc:雾都立交", "新地图", "location"),
            ("loc:暹罗边境", "跨境联盟", "location"),
        ],
    },
    "s6": {
        "title": "我的江湖 S6 · 回家",
        "chapters": "原稿第 634-747 章",
        "chen_state_in": "家族棋局入场",
        "chen_state_out": "主动退离 / 合法生意",
        "events": [
            ("evt:蓉城收束", "交交给张亮打理", "权力让渡", "event"),
            ("evt:神龙极训", "荒漠训练通过选拔", "大高潮 ①", "event"),
            ("evt:帝都清算", "秦老头亲自下场", "大高潮 ②", "event"),
            ("evt:陈浩南的选择", "拒绝顶级 offer / 收缩合法", "核心主题落地", "event"),
            ("evt:多关系承诺", "逐一告别或承诺", "情感回收", "event"),
            ("evt:龙王桥终局", "江边与沈雪瑶牵孩子相逢", "开篇对照镜头", "event"),
        ],
        "characters": [
            ("char:陈浩南", "主动退离者", "character"),
            ("char:秦老头", "终极后台首次完整现身", "character"),
            ("char:沈雪瑶", "孩子 / 独立执业", "character"),
            ("char:林悦", "留下 / 自己的事业", "character"),
            ("char:张亮", "接管天下会", "character"),
        ],
        "locations": [
            ("loc:神龙基地", "特殊组织 / 完成资格后退离", "location"),
            ("loc:帝都晚宴", "终局清算", "location"),
            ("loc:蓉城家庭居所", "新场景 / 开篇对照", "location"),
            ("loc:龙王桥", "开篇对照镜头", "location"),
        ],
    },
}


def build_volume(key: str, spec: dict) -> dict:
    nodes: list[dict] = []
    edges: list[dict] = []

    root_id = f"vol:{key}"
    nodes.append(node(root_id, spec["title"], "root",
                      f"{spec['chapters']}；{spec['chen_state_in']} → {spec['chen_state_out']}",
                      0, 0, "confirmed"))

    # 事件中轴（按出场顺序垂直排列）
    for i, (eid, title, summ, kind) in enumerate(spec["events"]):
        nodes.append(node(eid, title, "event", summ, 0, -500 + i * 180))
        edges.append(edge(root_id, eid, "事件链", 2.0))
        if i > 0:
            edges.append(edge(spec["events"][i - 1][0], eid, "承接", 1.5))

    # 人物（左侧）
    for i, (cid, summ, kind) in enumerate(spec["characters"]):
        nodes.append(node(cid, cid.split(":", 1)[-1], "character", summ,
                          -900, -500 + i * 150))
        edges.append(edge(root_id, cid, "出场人物"))

    # 地点（右侧）
    for i, (lid, summ, kind) in enumerate(spec["locations"]):
        nodes.append(node(lid, lid.split(":", 1)[-1], "location", summ,
                          900, -400 + i * 180))
        edges.append(edge(root_id, lid, "主要场所"))

    return dataset(key, spec["title"], nodes, edges)


# ============================================================
# 主流程
# ============================================================
def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    outputs: dict[str, dict] = {
        "framework": build_framework(),
    }
    for k, spec in VOLUME_SPECS.items():
        outputs[k] = build_volume(k, spec)

    manifest_entries = []
    for key, data in outputs.items():
        fname = f"{NOVEL_ID}-{key}.json"
        (OUT / fname).write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        manifest_entries.append({
            "id": data["novel"]["id"],
            "title": data["novel"]["title"],
            "file": fname,
            "coverage": data["coverage"],
        })

    # 读旧 manifest，保留原图谱
    mpath = OUT / "manifest.json"
    manifest = json.loads(mpath.read_text(encoding="utf-8"))
    kept = [n for n in manifest.get("novels", []) if not n["id"].startswith(f"{NOVEL_ID}-")]
    manifest["novels"] = kept + manifest_entries
    # 确保原总图谱排第一
    manifest["novels"].sort(key=lambda e: (
        0 if e["id"] == NOVEL_ID else
        1 if e["id"] == f"{NOVEL_ID}-framework" else
        2 if e["id"].startswith(f"{NOVEL_ID}-s") else 3
    ))
    mpath.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"wrote {len(outputs)} graphs → {OUT}")
    for key, data in outputs.items():
        print(f"  {key:10s}  {data['coverage']['nodes']:3d} nodes / {data['coverage']['edges']:3d} edges")


if __name__ == "__main__":
    main()
