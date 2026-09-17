# -*- coding: utf-8 -*-
"""第四课 · 中译英三级训练（课堂）。

设计逻辑针对舒同学：
  L1 词组级 —— 解决"中文蹦得出、英文写不出"，把零星想法固化成可用的英文积木
  L2 句子级 —— 解决"句子是中式语序"，每组锁定一个高分句式
  L3 段落级 —— 解决"句子连不成段"，逼出过渡词与逻辑链
"""

# ==================================================== L1 词组级（30 题）
# (中文, 参考译文, 中式陷阱)
L1 = [
 ("缩小贫富差距", "narrow the gap between rich and poor", "✗ reduce the distance of rich and poor"),
 ("拓宽视野", "broaden one's horizons", "✗ widen the view"),
 ("培养批判性思维", "cultivate critical thinking", "✗ train critical thinking"),
 ("打下扎实的基础", "lay a solid foundation", "✗ build a strong base"),
 ("适应不断变化的就业市场", "adapt to a changing job market", "✗ fit the changing of job market"),
 ("学以致用", "apply what they have learned", "✗ use the knowledge into practice"),
 ("减轻学业压力", "ease academic pressure", "✗ reduce study stress"),
 ("跟不上同龄人", "fall behind their peers", "✗ can not follow their classmates"),
 ("激发求知欲", "spark intellectual curiosity", "✗ cause the desire of knowledge"),
 ("应试教育", "exam-oriented education", "✗ exam education"),
 ("沉迷于社交媒体", "be addicted to social media", "✗ indulge in social media"),
 ("注意力持续时间变短", "a shorter attention span", "✗ short attention time"),
 ("削弱写作能力", "undermine writing skills", "✗ make writing ability weak"),
 ("依赖拼写检查", "rely on spell-checkers", "✗ depend on the spelling check"),
 ("信息过载", "information overload", "✗ too many informations"),
 ("虚假信息的传播", "the spread of misinformation", "✗ the spreading of fake informations"),
 ("保护个人隐私", "safeguard personal privacy", "✗ protect personal secret"),
 ("面对面交流", "face-to-face communication", "✗ face to face talking"),
 ("提高工作效率", "boost productivity", "✗ improve the work efficiency"),
 ("限制屏幕使用时间", "limit screen time", "✗ limit the time of using screen"),
 ("归根结底", "in the final analysis", "✗ in the last analysis"),
 ("从长远来看", "in the long run", "✗ in the long future"),
 ("就……而言", "when it comes to", "✗ speaking of（偏口语）"),
 ("起到关键作用", "play a pivotal role in", "✗ take an important effect"),
 ("对……产生深远影响", "have a profound impact on", "✗ give a deep influence to"),
 ("权衡利弊", "weigh the pros and cons", "✗ balance the advantage and disadvantage"),
 ("利大于弊", "the benefits outweigh the drawbacks", "✗ the advantages are more than disadvantages"),
 ("承担责任", "shoulder the responsibility", "✗ take the duty"),
 ("解决问题的根源", "tackle the root cause", "✗ solve the basic reason"),
 ("以牺牲……为代价", "at the expense of", "✗ with the price of"),
]


# ==================================================== L2 句子级（24 题）
# (组名, 目标句式, 讲解, [(中文, 参考译文, 升级提示), ...])
L2 = [

("第 1 组 · 名词化主语", "抽象名词短语作主语 + 有力动词",
 "舒同学最典型的中式句：Because many students only care about the exam result, so they... "
 "——中文有“因为…所以…”，英文只能留一个。更高级的做法是把原因压成名词短语当主语。",
 [
  ("对考试成绩的过度关注，使学生几乎没有空间发展创造力。",
   "An excessive focus on examination results leaves students little room to develop creativity.",
   "先写 Because many students focus too much on exams, they cannot develop creativity，再压缩成名词主语。"),
  ("社交媒体的广泛使用大大缩短了年轻人的注意力持续时间。",
   "The widespread use of social media has significantly shortened young people's attention span.",
   "「The + 形容词 + use of X」是万能名词主语。"),
  ("政府投入不足是农村学校落后的主要原因。",
   "Inadequate government investment is the main reason rural schools lag behind.",
   "reason 后面直接跟从句，不要写 the reason why...is because。"),
  ("父母的过高期望给青少年带来了巨大的心理压力。",
   "Excessive parental expectations place enormous psychological pressure on teenagers.",
   "place / impose pressure on sb，别用 give pressure to。"),
  ("技术的快速发展使许多传统职业面临消失的风险。",
   "Rapid technological advances have put many traditional occupations at risk of disappearing.",
   "put sth at risk of doing 是高分搭配。"),
  ("缺乏面对面交流削弱了年轻人的社交能力。",
   "A lack of face-to-face communication has undermined young people's social skills.",
   "A lack of... 作主语，比 Because there is no... 干净得多。"),
 ]),

("第 2 组 · 让步与转折", "Although / While / Admittedly ... , 主句",
 "她课上常有两个相反的想法，但写下来变成两个并列句。让步结构能把它们装进一句里，逻辑立刻清楚。",
 [
  ("尽管在线课程成本更低，它们无法复制课堂讨论的活力。",
   "Although online courses are cheaper, they cannot replicate the energy of classroom discussion.",
   "replicate 比 copy 学术；注意 Although 后不能再加 but。"),
  ("诚然，专业化能让毕业生更快就业；然而这也窄化了他们的知识面。",
   "Admittedly, specialisation helps graduates find work sooner; however, it narrows their intellectual range.",
   "分号 + however + 逗号，是标准写法。"),
  ("虽然这一论点乍看很有说服力，它却忽略了一个关键因素。",
   "Although this argument seems convincing at first glance, it overlooks a crucial factor.",
   "at first glance 是加分插入语。"),
  ("批评者可能会反驳说改革成本太高，但不作为的代价更大。",
   "Critics may object that reform is too costly, yet the price of inaction is greater.",
   "先替对方说话再推翻——7 分作文的标志动作。"),
  ("与许多人的看法相反，考试分数并不能可靠地预测职业成功。",
   "Contrary to popular belief, examination scores do not reliably predict career success.",
   "Contrary to popular belief 直接起一句，很有力。"),
  ("这并不是说传统教学毫无价值；恰恰相反，它应被有选择地保留。",
   "This is not to say that traditional teaching is worthless; rather, it should be retained selectively.",
   "防止自己的观点被读成极端，考官很吃这一套。"),
 ]),

("第 3 组 · 非谓语结构", "分词 / 不定式作状语与后置定语",
 "中文爱用短句并列：“学生做兼职，他们学到技能，这帮助他们找工作。”英文要把次要动作降级成分词。",
 [
  ("学生通过做兼职获得实用技能，从而提高了就业前景。",
   "Students acquire practical skills by taking part-time jobs, thereby improving their employment prospects.",
   "thereby + doing 表结果，替代 and this improves...。"),
  ("面对激烈的竞争，许多毕业生选择继续深造。",
   "Faced with fierce competition, many graduates choose to pursue further study.",
   "Faced with... 过去分词作状语，句首。"),
  ("政府投入巨资改善公共交通，希望以此减少拥堵。",
   "The government has invested heavily in public transport, hoping to reduce congestion.",
   "现在分词表伴随，比 and hopes to 自然。"),
  ("在网上长大的孩子往往难以长时间专注。",
   "Children raised online often struggle to concentrate for long periods.",
   "raised online 是过去分词后置定语，省掉 who are。"),
  ("为了跟上技术变革，员工必须不断更新技能。",
   "To keep pace with technological change, employees must continually update their skills.",
   "不定式作目的状语放句首，比 In order that... 简洁。"),
  ("越来越多的家长把孩子送进补习班，认为这样能提高成绩。",
   "A growing number of parents enrol their children in tutoring classes, believing this will raise their grades.",
   "believing 表原因/看法，避免又起一句 They think that...。"),
 ]),

("第 4 组 · 形式主语与比较结构", "It is ... that / less A than B / not A but B",
 "这一组解决“想说的意思很绕、写出来很平”。三个句式能把复杂逻辑压进一句。",
 [
  ("不可否认，生活水平在过去三十年里显著提高了。",
   "It is undeniable that living standards have risen markedly over the past three decades.",
   "It is undeniable that + 完整句；markedly 比 greatly 高级。"),
  ("问题与其说出在技术本身，不如说出在使用方式上。",
   "The problem lies less in technology itself than in the way it is used.",
   "less in A than in B——两个介词必须对称。"),
  ("教育的目的应是培养思考者，而非仅仅培养高分者。",
   "The aim of education should be to produce thinkers, not merely high scorers.",
   "not merely A but B；merely 比 only 书面。"),
  ("正是缺乏监管，而不是技术本身，导致了隐私泄露。",
   "It is the absence of regulation, rather than technology itself, that has led to privacy breaches.",
   "It is ... that ... 强调句，rather than 插在中间。"),
  ("与其禁止手机，学校不如教学生如何合理使用。",
   "Rather than banning mobile phones, schools would do better to teach students how to use them wisely.",
   "would do better to do 是很地道的建议句式。"),
  ("城市居民的平均通勤时间几乎是农村居民的两倍。",
   "City dwellers spend almost twice as long commuting as their rural counterparts.",
   "twice as long as；counterparts 避免重复 residents。"),
 ]),
]


# ==================================================== L3 段落级（3 段）
# (标题, 中文段落, 参考译文, 逻辑链提示)
L3 = [
 ("段落 1 · 教育（主体段）",
  "应试教育最大的问题在于它奖励记忆而非理解。学生把大量时间花在背诵标准答案上，"
  "因为只有这些答案能拿到分数。结果是，他们在考试中表现出色，却往往无法解释自己所写内容的含义。"
  "更令人担忧的是，这种习惯会延续到大学，使他们在需要独立思考时不知所措。",
  "The greatest weakness of exam-oriented education is that it rewards memorisation rather than "
  "understanding. Students devote a great deal of time to reciting model answers, because only "
  "these answers earn marks. The consequence is that they perform impressively in examinations "
  "yet often cannot explain what their own writing means. More worryingly, this habit persists "
  "into university, leaving them at a loss when independent thought is required.",
  "主题句（rewards A rather than B）→ 原因（because）→ 结果（The consequence is that）"
  "→ 递进（More worryingly）。四句一段，每句一个连接点。"),

 ("段落 2 · 科技（让步段）",
  "诚然，即时通讯让年轻人比以往任何时候都写得更多。然而，这种写作几乎都是碎片化的："
  "缩写、表情符号和不完整的句子。因此，尽管书写量在增加，组织长篇论证的能力却在退化。"
  "换句话说，问题不在于年轻人写得少，而在于他们很少写得长。",
  "Admittedly, instant messaging means that young people write more than ever before. "
  "However, almost all of this writing is fragmented: abbreviations, emojis and incomplete "
  "sentences. Consequently, although the volume of writing has grown, the ability to organise "
  "an extended argument has declined. In other words, the problem is not that young people "
  "write less, but that they rarely write at length.",
  "让步（Admittedly）→ 转折（However）→ 结果（Consequently + although 让步）"
  "→ 澄清（In other words + not A but B）。"),

 ("段落 3 · 通用（结尾段）",
  "综上所述，双方的论点都建立在合理的关切之上。但在我看来，把责任完全推给个人或政府都过于简单。"
  "只有当两者共同行动时，真正的改变才可能发生。归根结底，需要改变的不只是政策，还有习惯。",
  "In conclusion, both sides of the debate rest on legitimate concerns. In my view, however, "
  "placing the responsibility entirely on individuals or on governments is too simplistic. "
  "Only when the two act together will genuine change become possible. In the final analysis, "
  "what must change is not merely policy but habit.",
  "总结（In conclusion）→ 立场（In my view）→ 条件倒装（Only when... will...）"
  "→ 收尾（not merely A but B）。注意 Only when 开头必须部分倒装。"),
]


# ============================================= 段落组装（直击篇章瓶颈）
# 给零散关键词，要求组装成逻辑段——这正是舒同学课上"蹦词"之后卡住的那一步。
ASSEMBLY = [
 dict(
   topic="教育 · 主体段",
   keywords=["exam-oriented", "memorise", "creativity", "job market",
             "practical skills", "fall behind"],
   task="用以上 6 个词，写一个 4–5 句的主体段，论证“应试教育不利于学生长期发展”。"
        "要求：第 1 句主题句，第 2–3 句解释与举例，第 4 句结果，第 5 句小结。",
   model="Exam-oriented education may raise scores, but it does little to prepare students for "
         "working life. Because marks depend on reproducing fixed answers, students learn to "
         "memorise rather than to question, and creativity is quietly squeezed out. A graduate "
         "who can recite every formula may still be unable to solve an unfamiliar problem at work. "
         "In a job market that rewards practical skills and adaptability, such students soon fall "
         "behind their more flexible peers. Education that stops at the examination hall, in short, "
         "leaves its work half done.",
   note="注意第 2 句用 Because 从句压住原因，第 3 句用“一个具体的人”举例——"
        "比 many students 有力得多。"),

 dict(
   topic="科技 · 主体段",
   keywords=["attention span", "fragmented reading", "deep concentration",
             "notifications", "undermine", "in turn"],
   task="用以上 6 个词，写一个 4–5 句的主体段，论证“智能手机削弱了深度阅读能力”。"
        "要求：至少用一个名词化主语，至少用一个 in turn。",
   model="The constant stream of notifications has measurably shortened the average attention "
         "span. Reading online has therefore become fragmented: users skim, click away and rarely "
         "finish a long article. This habit in turn undermines the capacity for deep concentration "
         "that serious reading demands. Over time, what is lost is not only patience but the ability "
         "to follow a sustained argument at all.",
   note="第 1 句 The constant stream of notifications 就是名词化主语；"
        "第 3 句 in turn 制造连锁反应，论证立刻有了第二层。"),

 dict(
   topic="社会 · 让步段",
   keywords=["Admittedly", "however", "individuals", "governments",
             "at the expense of", "concrete steps"],
   task="用以上 6 个词，写一个 4 句的让步段，承认“个人行动有限”，"
        "但论证“政府责任更大”。要求：Admittedly 开头，however 转折。",
   model="Admittedly, the actions of individuals alone cannot reverse climate change. However, "
         "this does not absolve governments of their far greater responsibility. Only the state "
         "can take the concrete steps — carbon pricing, public transport, industrial regulation — "
         "that no household could manage on its own. To leave the burden entirely with individuals "
         "is to protect industry at the expense of the planet.",
   note="破折号插入具体措施，是把抽象论点落地的快捷办法；"
        "最后一句 To do... is to do... 句式很有力量。"),
]
