#!/usr/bin/env python3
"""Build one evidence-backed Wiki page per novel entity."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOVEL = ROOT / "novels" / "qing-xian-meinv-laoshi"
MANUSCRIPT = NOVEL / "drafts" / "complete" / "qing-xian-meinv-laoshi-reconstructed-v2-proofread.md"
WIKI = NOVEL / "wiki"

# slug: (Chinese name, aliases, positioning)
CHARACTERS = {
    "chen-zhaonan": ("陈照南", [], "主角；从普通大学生成长为天下会领袖并进入神龙部队"),
    "xia-ziyan": ("夏梓妍", ["梓妍"], "青年教师；开篇核心关系人物与李振北控制线中心"),
    "luo-li": ("罗莉", [], "陈照南早期女友；普通生活、家庭归属与承诺线核心"),
    "xu-miaomiao": ("徐苗苗", ["苗苗"], "学生会成员转经营者与天下会谋士"),
    "li-zhenbei": ("李振北", [], "贯穿长线的核心对手；以财富、家族和组织资源实施控制"),
    "zhang-xing": ("张星", [], "陈照南室友；普通青春和校园原点"),
    "wang-liang": ("王亮", [], "陈照南早期执行型兄弟；忠诚与牺牲线"),
    "lv-runhai": ("吕润海", ["海哥"], "海迪领袖；陈照南进入地下秩序的引路人"),
    "bai-jie": ("白姐", [], "海迪经营核心；掌握人心、场所与吕润海秘密"),
    "lei-ge": ("雷哥", [], "海迪前辈和退伍军人；地方规矩与格斗训练引路人"),
    "li-nana": ("李娜娜", ["娜娜", "小护士"], "护士；医疗、照护和生活感关系线"),
    "shen-qing": ("沈晴", [], "酒店职业女性；经营、执行与成熟关系线"),
    "liu-yuanyuan": ("刘园园", ["园园"], "困难家庭少女；教育、成长和保护线"),
    "zhao-banxian": ("赵半闲", ["破军"], "陈照南核心军师与高阶搭档；杀破狼中的破军"),
    "lin-qingchao": ("林青朝", [], "青花会领袖；陈照南的盟友、兄长与竞争者"),
    "su-qiqi": ("苏柒柒", ["罗刹女", "罗刹"], "苏家与鬼组关键人物；高能力战友和关系人物"),
    "luo-meng": ("洛梦", ["洛神"], "公众明星；连接帝都圈层、杨家与苏越"),
    "duan-chenwei": ("段晨薇", [], "警察；法律秩序与陈照南地下身份的冲突中心"),
    "yu-jie": ("雨姐", ["美女医生"], "神医与顶级高手；连接杨家、武学和神龙部队"),
    "jiang-yuwei": ("蒋雨薇", [], "神龙部队阶段人物；纪律、战友和训练线"),
    "cao-jie": ("曹姐", [], "成熟商业女性；连锁产业与家庭网络人物"),
    "zhou-ying": ("周颖", [], "后期危险关系人物；飙车、失控与救赎线"),
    "lin-qingxue": ("林清雪", [], "林家人物；家族、门第与赵半闲关系线"),
    "yang-lulu": ("杨璐璐", [], "校园后期关系人物；连接重庆事件与成长支线"),
    "zhu-anke": ("朱安珂", [], "天下会执行和管理骨干"),
    "qian-kai": ("钱凯", [], "魔影核心与战术负责人"),
    "lin-zhiheng": ("林志衡", [], "鬼组成员；组织使命与私人交情线"),
    "da-niu": ("大牛", [], "天下会正面战力与可靠执行者"),
    "wang-chen": ("王晨", [], "天下会中后期高频成员"),
    "yu-yang": ("于洋", [], "陈照南阵营成员；参与多次行动与救援"),
    "su-qinghou": ("苏轻侯", [], "苏家和鬼组高层；家族身份与组织入口"),
    "bai-liguo": ("白立国", [], "白袍会领袖和城北教父"),
    "chen-zhengkun": ("陈正坤", [], "陈照南父亲；陈家身世和父辈旧事核心"),
    "chen-shouxin": ("陈守信", [], "陈家上一代关键人物；忠信帮历史源头"),
    "lin-laoyezi": ("林老爷子", [], "林家与忠信帮旧秩序代表"),
    "hacha-jiangjun": ("哈察将军", ["哈察"], "跨境武装领袖；泰国与金三角资源入口"),
    "qin-laotou": ("秦老头", [], "顶级后台人物；神龙阶段的资格与格局检验者"),
    "su-yue": ("苏越", [], "苏家后辈；洛梦追求者与神龙入口人物"),
    "yang-yi": ("杨一", [], "杨家高手；神龙部队与顶级武力线"),
    "yang-zhikai": ("杨志锴", [], "神龙部队人物；训练与竞争线"),
    "xiao-yuanzhang": ("肖院长", [], "神龙学院管理者和训练体系权威"),
    "zhang-shengwei": ("张晟威", [], "张家与鬼组相关对手；擅长代理冲突和组织布局"),
    "xiuluo": ("修罗", [], "鬼组及高阶战力线的重要强敌"),
    "yecha": ("夜叉", ["叉"], "鬼组成员；海外经历与特殊行动骨干"),
    "gu-feihong": ("顾飞鸿", [], "飞鸿帮领袖；资本化地方势力代表"),
    "zhao-zihan": ("赵子涵", [], "校园阶层和面子冲突代表"),
    "zhao-wei": ("赵伟", [], "狼舞停业危机中的分局关系人物"),
    "xie-ting": ("谢廷", [], "地方扩张阶段的重要对手"),
    "liu-haisheng": ("刘海生", [], "罗莉前任相关人物；校园感情冲突角色"),
    "xiao-zhifei": ("萧志飞", [], "早期校园与情感冲突人物"),
    "fu-yanlin": ("付燕林", [], "校园及地方冲突人物"),
    "yang-hongguo": ("杨宏国", [], "忠信帮西堂堂主和地方旧势力人物"),
    "xia-qiming": ("夏启明", [], "夏梓妍父亲；家庭债务与控制链人物"),
    "badun": ("巴顿", [], "跨境阶段高频人物"),
    "liu-jiang": ("刘江", [], "中后期势力冲突人物"),
    "wang-xi": ("王曦", [], "中后期关系和事件人物"),
    "leng-qingfeng": ("冷清风", [], "神龙阶段人物"),
    "han-chun": ("韩春", [], "地方组织阶段人物"),
    "ye-qing": ("叶青", [], "中后期高阶人物"),
    "mofeisi": ("墨菲斯", [], "海外阶段人物"),
    "dong-xiao": ("董潇", [], "中后期事件人物"),
    "jiang-donghua": ("蒋东华", [], "东华帮相关人物"),
    "lie-hu": ("烈虎", [], "高阶战力人物"),
    "hu-kebing": ("胡科兵", [], "天下会与地方冲突人物"),
    "geng-dazhong": ("耿大忠", [], "地方势力阶段人物"),
    "xiaoman": ("小曼", [], "上海逃亡阶段救助陈照南的人物"),
    "song-hubing": ("宋胡冰", [], "南天集团商业核心；七杀候选人物"),
    "luo-chen": ("罗臣", [], "罗莉家族人物；后期资源与关系线"),
    "ling-zhi": ("凌芝", [], "中后期高频关系人物"),
    "jiang-lin": ("江琳", [], "中后期关系与事件人物"),
    "wen-tianqiang": ("闻天强", [], "地方势力阶段人物"),
    "wang-longbin": ("王龙斌", [], "飞鸿帮相关行动人物"),
    "chen-mufan": ("陈慕凡", [], "陈家后期人物"),
    "li-dong": ("李东", [], "地方组织阶段人物"),
    "shamu": ("沙姆", [], "海外与神龙阶段人物"),
    "zhao-liner": ("赵琳儿", [], "后期关系人物"),
    "sun-yidao": ("孙一刀", [], "海迪及狼舞阶段成员"),
    "miao-wenlong": ("苗文龙", [], "中后期组织人物"),
    "sun-peng": ("孙鹏", [], "地方势力阶段人物"),
    "fang-xun": ("方寻", [], "中后期事件人物"),
    "feng-jianheng": ("冯建恒", [], "海迪和地方组织阶段人物"),
    "xu-le": ("许乐", [], "中后期事件人物"),
    "zhou-jianren": ("周贱人", [], "校园阶段以绰号出现的冲突人物"),
    "wang-shaochuan": ("王绍川", [], "后期组织人物"),
    "xu-mingkang": ("许明康", [], "后期事件人物"),
    "a-guang": ("阿光", [], "徐苗苗相关事件与陈照南早期布局人物"),
    "fei-mao": ("肥猫", ["飞猫"], "海迪早期主要对手"),
    "wugui-zhao": ("乌龟罩", [], "海迪阶段成员和分析型人物"),
}

FACTIONS = {
    "haidi": ("海迪", "陈照南进入地下秩序的第一站和吕润海的核心场所"),
    "langwu": ("狼舞", "陈照南经营、扬名并建立个人班底的夜场"),
    "tianxiahui": ("天下会", "陈照南建立的核心组织"),
    "qinghuahui": ("青花会", "林青朝领导的成熟城市级组织"),
    "baipaohui": ("白袍会", "白立国长期经营的城北势力"),
    "feihongbang": ("飞鸿帮", "以资本、关系和跨区扩张为特征的敌对组织"),
    "xuelangbang": ("血狼帮", "以强硬执行和地盘战争为特征的组织"),
    "kuangdaobang": ("狂刀帮", "地方扩张阶段的帮派势力"),
    "zhongxinbang": ("忠信帮", "陈守信、林老爷子和地方旧秩序相关组织"),
    "huangqihui": ("黄旗会", "天下会扩张阶段的地方组织"),
    "langyabang": ("狼牙帮", "城南洗牌阶段的敌对帮派"),
    "donghuabang": ("东华帮", "城南洗牌阶段的敌对帮派"),
    "qingbang": ("青帮", "中后期城市冲突中的帮派组织"),
    "guizu": ("鬼组", "苏家相关的隐秘行动组织"),
    "shewang": ("蛇王组织", "重庆及跨境行动线中的杀手组织"),
    "shenlongbudui": ("神龙部队", "故事最高等级的训练、任务和荣耀组织"),
    "moying": ("魔影", "天下会训练形成的专业执行队伍"),
    "xuelongwei": ("血龙卫", "神龙体系中的高阶荣誉和战力单位"),
    "wudajiazu": ("五大家族", "陈、林、苏、杨、张五家构成的帝都权力网络"),
    "nantianjituan": ("南天集团", "陈照南阵营后期的合法商业载体"),
    "nantianbaoan": ("南天保安公司", "夏梓妍推动建立的组织合法化载体"),
    "shenlongxueyuan": ("神龙学院", "神龙部队的训练、积分和挑战空间"),
    "tianyijituan": ("天一集团", "城市商业竞争中的集团组织"),
    "donghuijituan": ("东辉集团", "城市商业竞争中的集团组织"),
    "lantianjituan": ("蓝天集团", "后期商业网络中的集团组织"),
}

LOCATIONS = {
    "dazhuanxiaoyuan": ("大专校园", ["学校", "校园"], "陈照南普通学生身份和早期冲突的起点"),
    "longwangqiao": ("龙王桥", [], "校园周边生活圈和匿名约见地理锚点"),
    "hongwukafeiting": ("红屋咖啡厅", [], "陈照南与夏梓妍确认彼此身份的开篇场所"),
    "kaipinbinguan": ("开篇宾馆", ["宾馆"], "李振北闯入并引爆主冲突的场所"),
    "huangchengduchang": ("皇城赌场", [], "债务、赌局和李振北资源线场所"),
    "baileduchang": ("百乐赌场", [], "地方帮派与经营冲突场所"),
    "alongshengdian": ("阿龙盛典", [], "狼舞停业危机的对手场所"),
    "cuijiaxiang": ("崔家巷", [], "刘园园家庭与底层生活线的重要地点"),
    "taifengdajiudian": ("泰峰大酒店", [], "地方峰会、联盟和公开交锋场所"),
    "nantiandajiudian": ("南天大酒店", [], "天下会后期总部和商业升级象征"),
    "chengdu": ("成都", [], "天下会、青花会等城市势力竞争的主舞台"),
    "shanghai": ("上海", [], "夏梓妍、鬼组、张晟威与身世线舞台"),
    "chongqing": ("重庆", [], "蛇王组织、追踪和地方行动舞台"),
    "didu": ("帝都", [], "五大家族和顶层后台权力中心"),
    "taiguo": ("泰国", [], "哈察将军和海外冲突舞台"),
    "jinsanjiao": ("金三角", [], "跨境武装、资源和退路想象的舞台"),
    "shenlongjidi": ("神龙基地", ["神龙部队", "学院"], "陈照南后期训练和挑战的封闭空间"),
    "guangrongxiaoqu": ("光荣小区", [], "王亮、娜娜和沈晴早期生活线地点"),
    "jingchenghuoguo": ("景程火锅", ["景程火锅店"], "陈照南、娜娜和沈晴首次聚餐冲突场所"),
    "tianxiadajiudian": ("天下大酒店", [], "中后期酒店与势力活动场所"),
    "litiandajiudian": ("立天大酒店", [], "中后期酒店场所"),
    "shenghuidajiudian": ("盛辉大酒店", [], "中后期酒店场所"),
}

TERMS = {
    "daojia-shier-duanjin": ("道家十二段锦", "陈照南后期使用的呼吸、恢复和身体控制方法"),
    "sha-po-lang": ("杀破狼", "贪狼、破军、七杀三星汇聚的命理框架"),
    "tanlang": ("贪狼", "杀破狼三星之一；与陈照南欲望和开创性相关"),
    "pojun": ("破军", "杀破狼三星之一；赵半闲的定位和称号"),
    "qisha": ("七杀", "杀破狼三星之一；后期寻找和判断的重要伏笔"),
    "shichong-tiangong": ("十重天宫", "后期武学和能力层级相关专有名词"),
    "yiji-yaoji": ("一级药剂", "神龙阶段用于身体强化的稀缺资源"),
    "jifen": ("神龙积分", ["积分"], "神龙学院用于宿舍、训练和资源兑换的制度"),
    "tiaozhansai": ("挑战赛", [], "神龙阶段决定名次、积分和资格的竞争机制"),
    "piaoliuping": ("漂流瓶", [], "开篇匿名社交机制和主冲突触发物"),
    "luoshenfu": ("洛神赋", "洛梦新专辑及其公众形象的重要符号"),
    "mingshi": ("名器", "原稿中的成人身体标签；重构时不得决定女性人格与忠诚"),
    "shenqi": ("神器", "原稿中对男性身体能力的成人化称谓"),
    "nantian": ("南天", "后期酒店、集团和保安公司共用的品牌名称"),
    "longtou": ("龙头", "地方组织最高领导称谓和权力资格"),
}

EVENTS = {
    "anonymous-date": ("匿名约见", ["漂流瓶", "约会"], "陈照南通过漂流瓶约见夏梓妍，核心故事由此启动"),
    "li-zhenbei-breaks-in": ("李振北闯入", ["李振北", "宾馆"], "匿名约见转化为生存冲突和长期仇恨"),
    "li-zhenbei-revenge": ("李振北报复", ["报复", "李振北"], "李振北利用个人和家庭资源持续压制陈照南"),
    "enter-haidi": ("进入海迪", ["海迪", "加入"], "陈照南离开普通校园规则，进入吕润海的地方秩序"),
    "feimao-defeat": ("飞猫覆灭", ["飞猫", "肥猫"], "陈照南通过布局和行动建立早期威望"),
    "langwu-closure": ("狼舞停业危机", ["狼舞", "停业"], "死亡事件和关系封锁共同威胁海迪现金流"),
    "liu-yuanyuan-evidence": ("刘园园证据链", ["刘园园", "阿龙盛典"], "陈照南从死者家庭找到狼舞危机的幕后线索"),
    "chen-zhaonan-drops-out": ("陈照南退学", ["退学"], "陈照南正式失去普通学生身份"),
    "lv-runhai-death": ("吕润海死亡", ["海哥死了", "吕润海"], "海迪失去领袖并出现接班权力真空"),
    "wang-liang-sacrifice": ("王亮牺牲", ["王亮", "陨"], "早期核心兄弟死亡，推动陈照南争夺领导权"),
    "dragon-head-election": ("龙头选举", ["选举龙头", "龙头大哥"], "海迪旧部和新势力重新分配最高权力"),
    "tianxiahui-founded": ("天下会成立", ["君临天下", "天下会"], "陈照南建立自己的正式组织"),
    "taifeng-summit": ("泰峰峰会", ["泰峰", "峰会"], "地方组织公开谈判和重新站队"),
    "chengnan-unification": ("统一城南", ["城南", "统一"], "天下会从堂口扩张为城区级势力"),
    "xia-ziyan-shot": ("夏梓妍中枪", ["夏梓妍", "中枪"], "上海追杀将情感线与高层组织冲突合流"),
    "lineage-revealed": ("陈照南身世揭露", ["身世", "陈家"], "草根成长与五大家族、父辈历史发生连接"),
    "zhao-banxian-injured": ("赵半闲重伤", ["赵半闲", "重伤"], "核心军师受创，测试组织在主角之外的运转能力"),
    "nantian-founded": ("南天集团成立", ["南天集团"], "天下会尝试建立合法商业载体"),
    "chengdu-unification": ("成都统一", ["统一成都", "成都"], "天下会、青花会与各城市势力完成阶段性重组"),
    "three-stars-gather": ("三星汇聚", ["贪狼", "破军", "七杀"], "杀破狼命理伏笔进入集中兑现阶段"),
    "shewang-destroyed": ("蛇王组织覆灭", ["蛇王组织", "连根拔起"], "陈照南阵营跨城打击重庆杀手组织"),
    "join-shenlong": ("加入神龙部队", ["神龙部队", "进入"], "陈照南从地方领袖重新成为特殊组织新人"),
    "extreme-training": ("神龙极限训练", ["极限", "训练"], "陈照南通过体能、积分和挑战赛升级能力"),
    "qin-laotou-test": ("秦老头考验", ["秦老头", "钓鱼", "下棋"], "顶级后台通过日常行为检验陈照南的选择和格局"),
    "final-settlement": ("终局清算", ["大结局", "荣耀"], "家族、组织、关系和荣耀主题完成最终结算"),
}


def chapters(text: str) -> list[tuple[int, str, str]]:
    matches = list(re.finditer(r"^## 第(\d+)章\s+(.+)$", text, re.MULTILINE))
    result = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result.append((int(match.group(1)), match.group(2).strip(), text[match.end():end]))
    return result


def evidence(items: list[tuple[int, str, str]], names: list[str]) -> tuple[int, list[tuple[int, str]]]:
    hits = []
    total = 0
    for number, title, body in items:
        count = sum(body.count(name) for name in names)
        if count:
            hits.append((number, title))
            total += count
    return total, hits


def frontmatter(entity_id: str, entity_type: str, title: str, canon: str = "inferred") -> str:
    return f"""---
id: {entity_id}
type: {entity_type}
title: {title}
status: active
canon: {canon}
source_refs:
  - SRC-20261008-001
updated: 2026-10-08
tags: [{entity_type}, entity]
---
"""


def source_summary(total: int, hits: list[tuple[int, str]]) -> str:
    if not hits:
        return "- 当前自动扫描未找到稳定命中，需人工核验别名或来源写法。"
    first = hits[0]
    last = hits[-1]
    samples = "、".join(f"第{number}章《{title}》" for number, title in hits[:3])
    return (
        f"- 正文称谓命中约 {total} 次，涉及 {len(hits)} 章。\n"
        f"- 首次命中：第{first[0]}章《{first[1]}》；末次命中：第{last[0]}章《{last[1]}》。\n"
        f"- 前段证据：{samples}。"
    )


def write_character(slug: str, data: tuple[str, list[str], str], items: list[tuple[int, str, str]]) -> None:
    name, aliases, role = data
    names = [name, *aliases]
    total, hits = evidence(items, names)
    alias_text = "、".join(aliases) if aliases else "无稳定别名"
    content = f"""{frontmatter(f"char-{slug}", "character", name)}
# {name}

## 一句话定位

{role}。

## 称谓与身份

- 正式名称：{name}
- 稳定别名/称谓：{alias_text}
- 状态：原稿存在，具体年龄、职业和阶段变化需逐章核验。

## 原稿出场证据

{source_summary(total, hits)}

## 欲望、资源与冲突

- 个人欲望：待按首次出场、关键选择和终局逐章补全。
- 可用资源：以正文展示为准，不从称谓反推能力。
- 核心冲突：与陈照南、所属组织及个人关系之间的目标差异。
- 行为边界：不能因阵营或亲密关系自动失去个人判断。

## 人物线

- 初始状态：以首次命中章节为起点。
- 关键转折：待从全部出场章节提取选择、伤势、关系和阵营变化。
- 终局状态：以末次出场附近正文核验，不以缺席自动推定死亡或离开。

## AI短剧资产

- 固定面部、身形、声音和动作基线待建立。
- 不同势力阶段使用不同服装版本。
- 每次出场需锁定年龄、伤势、关系状态、携带物和所在地点。

## 待核验

- 本页完成实体拆分和出场证据定位，不代表已完成全部相关章节的语义精读。
- 同名、别名和称谓是否指向同一人，需要结合具体场景持续校验。
"""
    path = WIKI / "characters" / f"char-{slug}.md"
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def write_faction(slug: str, data: tuple[str, str], items: list[tuple[int, str, str]]) -> None:
    name, role = data
    total, hits = evidence(items, [name])
    content = f"""{frontmatter(f"fac-{slug}", "faction", name)}
# {name}

## 定位

{role}。

## 原稿出场证据

{source_summary(total, hits)}

## 权力来源

- 人员、资产、地盘、情报、合法身份和后台的具体组成待逐章核验。
- 组织影响力不能仅用个人武力替代。

## 结构与规则

- 领袖、骨干、基层成员、加入方式和退出代价待补。
- 对外称谓、礼仪、徽记、固定空间和行动边界待补。

## 剧情变化

- 初始状态、扩张、联盟、损失和终局状态以相关章节为准。
- 组织覆灭或合并后仍需记录人员、资产、债务和敌对关系去向。

## AI短剧资产

- 建立独立主色、材质、徽记、成员轮廓和空间礼仪。
- 不与其他组织仅靠名称区分。
"""
    (WIKI / "factions" / f"fac-{slug}.md").write_text(content, encoding="utf-8")


def write_location(slug: str, data: tuple[str, list[str], str], items: list[tuple[int, str, str]]) -> None:
    name, aliases, role = data
    total, hits = evidence(items, [name, *aliases])
    content = f"""{frontmatter(f"loc-{slug}", "location", name)}
# {name}

## 一句话识别

{role}。

## 原稿出场证据

{source_summary(total, hits)}

## 地理与交通

- 与相邻地点的方向、距离和交通时间待从具体行动章节核验。
- 跨城和跨境移动必须记录时间，不允许人物瞬移。

## 空间与秩序

- 入口、出口、主要房间、监控、障碍和人群规则待建立平面关系。
- 权属和使用者随剧情变化时建立地点版本。

## 感官与视频资产

- 光线、材质、声音、气味、天气和固定构图待从场景提取。
- 动作场生成前必须锁定人物站位、危险道具和撤退方向。

## 状态变化

- 首次出场、受袭、停业、易主、修复和终局状态分别记录，不覆盖历史。
"""
    (WIKI / "locations" / f"loc-{slug}.md").write_text(content, encoding="utf-8")


def write_term(slug: str, data: tuple, items: list[tuple[int, str, str]]) -> None:
    name, description, *rest = data
    aliases = rest[0] if rest else []
    total, hits = evidence(items, [name, *aliases])
    content = f"""{frontmatter(f"term-{slug}", "term", name)}
# {name}

## 定义

{description}。

## 原稿出场证据

{source_summary(total, hits)}

## 使用规则

- 含义、适用对象、起源和社会认知以正文展示为准。
- 若属于能力或制度，必须明确触发条件、上限、代价和失败模式。
- 若属于原稿成人化标签，重构时不得替代人物人格、同意和关系选择。

## 连续性要求

- 首次解释后保持含义稳定；新增能力不得临时扩张。
- AI短剧中优先用可见动作、道具和制度结果表现，不依赖旁白解释。
"""
    path = WIKI / "terms" / f"term-{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_event(slug: str, data: tuple[str, list[str], str], items: list[tuple[int, str, str]]) -> None:
    name, keywords, description = data
    total, hits = evidence(items, keywords)
    content = f"""{frontmatter(f"evt-{slug}", "event", name)}
# {name}

## 事件定位

{description}。

## 原稿证据范围

{source_summary(total, hits)}

## 参与者

- 核心行动者、对手、受影响者和见证者待按事件场景逐项链接。

## 起因—行动—结果

- 起因：待从事件前置章节提取直接诱因和长期压力。
- 行动：待区分主角主动选择、对手反制和偶发因素。
- 结果：待记录人物关系、组织资源、伤势、法律和舆论变化。

## 连续性与短剧

- 事件前后人物地点、服装、道具、伤势和信息状态必须衔接。
- 改编时以可见选择和状态变化为核心，不只用旁白概括。
- 若事件跨多章，拆为触发、升级、高潮和后果四类场景卡。
"""
    path = WIKI / "events" / f"evt-{slug}.md"
    path.write_text(content, encoding="utf-8")


def write_catalog(path: Path, title: str, entries: list[tuple[str, str, str]]) -> None:
    lines = [
        f"# {title}",
        "",
        "每个实体均有独立权威页面；索引只负责查找，详细事实写在实体页中。",
        "",
    ]
    for name, relative, description in sorted(entries, key=lambda item: item[0]):
        lines.append(f"- [{name}]({relative})：{description}。")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")
    items = chapters(text)
    for slug, data in CHARACTERS.items():
        write_character(slug, data, items)
    for slug, data in FACTIONS.items():
        write_faction(slug, data, items)
    for slug, data in LOCATIONS.items():
        write_location(slug, data, items)
    for slug, data in TERMS.items():
        write_term(slug, data, items)
    for slug, data in EVENTS.items():
        write_event(slug, data, items)
    write_catalog(
        NOVEL / "02-characters" / "人物索引.md",
        "人物索引",
        [(data[0], f"../wiki/characters/char-{slug}.md", data[2]) for slug, data in CHARACTERS.items()],
    )
    write_catalog(
        NOVEL / "01-world" / "组织索引.md",
        "组织索引",
        [(data[0], f"../wiki/factions/fac-{slug}.md", data[1]) for slug, data in FACTIONS.items()],
    )
    write_catalog(
        NOVEL / "01-world" / "地点索引.md",
        "地点索引",
        [(data[0], f"../wiki/locations/loc-{slug}.md", data[2]) for slug, data in LOCATIONS.items()],
    )
    write_catalog(
        NOVEL / "01-world" / "专有名词索引.md",
        "专有名词索引",
        [(data[0], f"../wiki/terms/term-{slug}.md", data[1]) for slug, data in TERMS.items()],
    )
    write_catalog(
        NOVEL / "03-plotlines" / "事件索引.md",
        "事件索引",
        [(data[0], f"../wiki/events/evt-{slug}.md", data[2]) for slug, data in EVENTS.items()],
    )
    print(
        f"entities: {len(CHARACTERS)} characters, {len(FACTIONS)} factions, "
        f"{len(LOCATIONS)} locations, {len(TERMS)} terms, {len(EVENTS)} events"
    )


if __name__ == "__main__":
    main()
