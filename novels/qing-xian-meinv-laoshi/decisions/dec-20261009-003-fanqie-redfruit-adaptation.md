# dec-20261009-003｜番茄小说与红果AI改编双层规范

- Status: accepted
- Context: 用户指定番茄小说为正文发布平台，并要求后续AI短剧/漫剧适配红果素材规范；
  同时要求故事完整、人物丰富、持续制造好奇与爽感。
- Sources:
  - 番茄《平台不允许发布的内容》，2022-07-26更新：
    https://fanqienovel.com/writer/zone/help/article?rank1=10019&rank2=10061&rank3=0
  - 番茄《平台内容发布规范》，2025-02-26更新：
    https://fanqienovel.com/writer/zone/help/article?rank1=10019&rank2=10222&rank3=0
  - 飞书《红果漫剧素材规范》，revision 1059：
    https://bytedance.larkoffice.com/wiki/QrgPwp5LVisuhykz5T5cXXLonY1
- Decision:
  - 小说正文按“番茄发布版”创作：允许犯罪、欲望、暴力和毒品作为负面冲突，
    但不得宣扬淫秽色情、赌博、吸毒，不渲染暴力恐怖，不教唆犯罪或传授方法。
  - AI短剧正片按“红果漫剧版”外化：保留事件、关系和地位逆转，
    敏感过程用遮挡、声效、反应、道具状态和事后后果表达。
  - 宣发/投放素材单独按“红果无尺度素材版”制作，不把最敏感镜头作为吸睛卖点。
  - 三层版本共享同一事件、人物状态和因果，不允许为过审随意删掉主线，
    也不允许宣传素材虚构正文不存在的反转。
- Redfruit requirements:
  - 剧目素材对应内容应满足总时长不少于20分钟、剧集不少于10集；
  - 素材纯内容片段全程展示“本故事纯属虚构”；
  - AI生成素材全程增加AI提示语，并标记“AI文生视频，无真人肖像输入”；
  - 警示语字号大于25px，建议约28px；
  - 竖版安全区：左右各44px、上147px、下103px；
  - 素材尺度标签统一选择“无尺度”。
- Narrative consequences:
  - S1采用16集、单集3–5分钟，总时长48–80分钟，满足基础时长与集数要求；
  - 每集前15秒建立异常或危险，中段至少一次信息反转，结尾留下行动型钩子；
  - 强制染毒保留为反派伤害和长期创伤，不出现药物制备、使用步骤、快感描写；
  - 宾馆与亲密戏保留成年人欲望和关系选择，不出现裸露、敏感部位、挑逗姿势或胁迫浪漫化；
  - 动作戏保留反杀和地位逆转，不出现血腥特写、肢解、虐杀或武器使用教程；
  - 夜场和亲密线所有角色必须明确成年，未成年角色只进入成长、教育和保护线。
- Files to update:
  - common/safety-compliance.md
  - common/platform-profiles/fanqie.md
  - common/platform-profiles/redfruit-ai-material.md
  - novels/qing-xian-meinv-laoshi/novel.yaml
  - novels/qing-xian-meinv-laoshi/wiki/systems/system-video-visual-bible.md
  - novels/qing-xian-meinv-laoshi/wiki/plot/plot-short-drama-roadmap.md
  - novels/qing-xian-meinv-laoshi/wiki/scenes/scene-rules.md
  - novels/qing-xian-meinv-laoshi/drafts/chapters/s1-boundary-beyond/arc.md
  - novels/qing-xian-meinv-laoshi/outputs/video-scripts/_video-script-template.md
  - novels/qing-xian-meinv-laoshi/wiki/log.md
