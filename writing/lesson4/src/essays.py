# -*- coding: utf-8 -*-
"""第四课 · 范文精读（2 篇）与课后巩固。

范文选两篇不同题型（Discuss both views / Agree or disagree），
重点不在读懂，而在"拆骨架 → 仿骨架"，对应第三课布置的"刻意模仿范文"。
"""

# ================================================================ 范文
ESSAYS = [
dict(
  no=1,
  kind="Discuss both views and give your own opinion",
  prompt="Some people believe that university students should specialise in a single subject, "
         "while others think they should study a wide range of subjects. "
         "Discuss both views and give your own opinion.",
  prompt_cn="有人认为大学生应专攻一个学科，也有人认为应广泛涉猎多门学科。"
            "讨论双方观点并给出你的看法。",
  paras=[
   ("P1 引言",
    "Universities have long debated whether depth or breadth better prepares young people for "
    "adult life. While a narrow focus undoubtedly produces expertise, I am firmly of the view "
    "that a broad education equips graduates more effectively for a world in which careers "
    "rarely follow a straight line."),
   ("P2 支持专精",
    "Those who favour specialisation argue, reasonably, that mastery takes time. A medical "
    "student who divides her attention between anatomy and art history is unlikely to qualify "
    "as a surgeon. Employers, too, increasingly recruit for specific competencies rather than "
    "general promise, and a solid grounding in one discipline signals precisely that. In "
    "technical fields, where knowledge is deep and cumulative, this argument is difficult to "
    "dispute."),
   ("P3 支持广博",
    "The case for breadth, however, rests on a longer time horizon. Few graduates now remain in "
    "a single occupation for life; most will change field several times, and the skills that "
    "transfer between them — reasoning, writing, the ability to learn quickly — are cultivated "
    "across subjects rather than within one. A student who studies only engineering may design "
    "an efficient bridge but fail to ask whether it should be built at all. Broad study, in "
    "other words, supplies the judgement that technical training alone cannot."),
   ("P4 结论",
    "In the final analysis, the two aims are less opposed than they appear. The most useful "
    "degree combines a specialist core with genuine exposure to other ways of thinking. "
    "Universities should therefore resist the pressure to narrow their curricula, since the "
    "graduates they produce will need not only to do a job well, but to decide which job is "
    "worth doing."),
  ],
  skeleton=[
   ("P1 引言", "背景 + 让步 + 表态",
    "Universities have long debated whether...",
    "背景一句 → While 让步一句 → I am firmly of the view that 表态",
    "While / undoubtedly / firmly of the view"),
   ("P2 让步方", "先站对方，再限定范围",
    "Those who favour specialisation argue, reasonably, that...",
    "论点 → 具体的人做例子 → 补第二个理由（Employers, too）→ 限定 In technical fields",
    "reasonably / too / in technical fields"),
   ("P3 己方", "转折 + 换时间尺度",
    "The case for breadth, however, rests on a longer time horizon.",
    "转折 → 事实（Few graduates...）→ 反例（A student who studies only...）→ 小结（in other words）",
    "however / in other words"),
   ("P4 结论", "调和 + 给出行动",
    "In the final analysis, the two aims are less opposed than they appear.",
    "调和双方 → 提出方案 → 用 not only...but 收尾",
    "In the final analysis / less...than / therefore"),
  ],
  highlights=[
   ("I am firmly of the view that", "表态，比 I think 高三档"),
   ("argue, reasonably, that", "插入语 reasonably 表示你承认对方合理——考官很看重这个"),
   ("a solid grounding in one discipline", "学科打底知识，固定搭配"),
   ("rests on a longer time horizon", "换时间尺度来反驳，是高级论证手法"),
   ("the skills that transfer between them", "可迁移能力，避免写 useful skills"),
   ("less opposed than they appear", "less A than B 对比结构"),
   ("not only to do a job well, but to decide which job is worth doing", "结尾对仗，有余味"),
  ],
),

dict(
  no=2,
  kind="To what extent do you agree or disagree",
  prompt="Some people think that the increasing use of computers and mobile phones for "
         "communication has had a negative effect on young people's reading and writing skills. "
         "To what extent do you agree or disagree?",
  prompt_cn="有人认为，越来越多地使用电脑和手机进行交流，对年轻人的读写能力产生了负面影响。"
            "你在多大程度上同意或不同意？",
  paras=[
   ("P1 引言",
    "As digital devices become embedded in everyday life, concerns have grown that they are "
    "eroding the literacy of the young. I largely agree that reading and writing have suffered, "
    "though I would contend that the damage lies less in the technology itself than in the habits "
    "it encourages."),
   ("P2 负面 · 阅读",
    "The clearest casualty is sustained reading. The constant stream of notifications has "
    "measurably shortened the average attention span, and reading online has become fragmented: "
    "users skim, click away and rarely finish a long article. This habit in turn undermines the "
    "capacity for deep concentration that serious reading demands. What is lost is not merely "
    "patience, but the ability to follow an extended argument at all."),
   ("P3 负面 · 写作 + 让步",
    "Writing has been affected differently. Admittedly, instant messaging means that young people "
    "write more than ever before; the volume of text they produce daily would astonish an earlier "
    "generation. However, almost all of it is brief, informal and unstructured, and predictive "
    "text removes even the need to spell. Consequently, while writing has increased in quantity, "
    "the ability to organise a formal argument has declined."),
   ("P4 结论",
    "Technology, then, is not the villain it is often made out to be; a device that delivers an "
    "entire library to a pocket could equally strengthen literacy. The decisive factor is how it "
    "is used. Until schools and parents teach young people to read at length and write with "
    "structure, the tools will continue to be blamed for choices that are, in the end, ours."),
  ],
  skeleton=[
   ("P1 引言", "背景 + 限定式表态",
    "As digital devices become embedded in everyday life...",
    "As 背景状语 → 现象 → largely agree（不写死）→ though 补一层限定",
    "As... / largely agree / I would contend that / less...than"),
   ("P2 论证一", "锁定一个方面，做出两层因果",
    "The clearest casualty is sustained reading.",
    "论点 → 名词化主语给原因 → in turn 制造第二层 → 收束（What is lost is...）",
    "in turn / not merely...but"),
   ("P3 论证二", "先让步再转折，承认反面事实",
    "Writing has been affected differently.",
    "Admittedly 承认写得更多 → However 指出质量 → Consequently 给结论",
    "Admittedly / However / Consequently / while"),
   ("P4 结论", "为技术翻案 + 给条件",
    "Technology, then, is not the villain it is often made out to be...",
    "否定极端 → 指出真正变量 → Until 从句给出条件与出路",
    "then / The decisive factor is / Until..."),
  ],
  highlights=[
   ("become embedded in everyday life", "融入日常生活，比 be widely used 生动"),
   ("I largely agree ... though I would contend that", "限定式表态，比全盘同意稳"),
   ("The clearest casualty is", "最明显的牺牲品——段首点题的好写法"),
   ("has measurably shortened", "measurably 暗示有数据支撑，显得克制可信"),
   ("in turn undermines", "连锁反应，论证第二层"),
   ("is not the villain it is often made out to be", "为某物翻案的固定表达"),
   ("Until schools and parents teach..., the tools will continue to be blamed", "Until 引导条件，结尾有行动指向"),
  ],
),
]


# ========================================================== 课后巩固
HW_INTRO = ("本次作业分五块，建议分两天完成：第一天做 A–C（约 60 分钟），"
            "第二天做 D–E（约 70 分钟）。所有中译英先自己写，写完再对答案，"
            "对完把错的抄进错题本并注明错因（搭配错 / 语序错 / 句式单一）。")

# A 搭配默写 (中文, 答案)
HW_A = [
 ("拓宽视野", "broaden one's horizons"),
 ("培养批判性思维", "cultivate critical thinking"),
 ("打下扎实的基础", "lay a solid foundation"),
 ("减轻学业压力", "ease academic pressure"),
 ("应试教育", "exam-oriented education"),
 ("跟不上同龄人", "fall behind their peers"),
 ("学以致用", "apply what they have learned"),
 ("就业前景", "employment prospects"),
 ("终身学习", "lifelong learning"),
 ("综合素质发展", "all-round development"),
 ("沉迷于社交媒体", "be addicted to social media"),
 ("注意力持续时间变短", "a shorter attention span"),
 ("削弱写作能力", "undermine writing skills"),
 ("信息过载", "information overload"),
 ("数字鸿沟", "the digital divide"),
 ("虚假信息的传播", "the spread of misinformation"),
 ("保护个人隐私", "safeguard personal privacy"),
 ("碎片化阅读", "fragmented reading"),
 ("限制屏幕使用时间", "limit screen time"),
 ("跟上技术变革", "keep pace with technological change"),
 ("归根结底", "in the final analysis"),
 ("从长远来看", "in the long run"),
 ("就……而言", "when it comes to"),
 ("起到关键作用", "play a pivotal role in"),
 ("对……产生深远影响", "have a profound impact on"),
 ("权衡利弊", "weigh the pros and cons"),
 ("利大于弊", "the benefits outweigh the drawbacks"),
 ("承担责任", "shoulder the responsibility"),
 ("解决问题的根源", "tackle the root cause"),
 ("以牺牲……为代价", "at the expense of"),
 ("采取切实措施", "take concrete steps"),
 ("这可归因于", "This can be attributed to"),
 ("不可否认", "It is undeniable that"),
 ("与此形成对比的是", "By contrast,"),
 ("一小部分人", "a small minority"),
 ("达成共识", "reach a consensus"),
 ("有充分理由认为", "there is good reason to believe that"),
 ("把资源投入到", "channel resources into"),
 ("提高工作效率", "boost productivity"),
 ("面对面交流", "face-to-face communication"),
]

# B 句子中译英 (中文, 参考译文, 目标句式)
HW_B = [
 ("对短期利润的过度追求损害了企业的长期声誉。",
  "An excessive pursuit of short-term profit has damaged companies' long-term reputation.",
  "名词化主语"),
 ("缺乏合格的教师是农村教育落后的主要原因。",
  "A shortage of qualified teachers is the main reason rural education lags behind.",
  "名词化主语 + reason + 从句"),
 ("政府补贴的减少使许多小型剧院面临倒闭。",
  "Cuts in government subsidies have put many small theatres at risk of closure.",
  "put sth at risk of"),
 ("尽管远程办公节省了通勤时间，它模糊了工作与生活的界限。",
  "Although remote work saves commuting time, it blurs the line between work and life.",
  "Although 让步"),
 ("诚然，旅游业创造了就业；然而它也加速了当地文化的商业化。",
  "Admittedly, tourism creates jobs; however, it also accelerates the commercialisation of local culture.",
  "Admittedly...; however,"),
 ("虽然这一政策初衷良好，它却忽略了低收入家庭的实际困难。",
  "Although the policy is well-intentioned, it overlooks the practical difficulties of low-income families.",
  "Although + overlook"),
 ("反对者可能会说罚款不公平，但污染的代价最终由所有人承担。",
  "Opponents may object that fines are unfair, yet the cost of pollution is ultimately borne by everyone.",
  "object that... yet..."),
 ("面对上涨的房价，越来越多的年轻人推迟结婚。",
  "Faced with rising house prices, a growing number of young people delay marriage.",
  "Faced with 分词状语"),
 ("城市大力投资绿地，希望以此改善居民健康。",
  "Cities have invested heavily in green space, hoping to improve residents' health.",
  "hoping to 伴随状语"),
 ("在数字环境中长大的儿童往往难以长时间专注。",
  "Children raised in a digital environment often struggle to concentrate for long periods.",
  "过去分词后置定语"),
 ("为了缩小城乡差距，政府必须优先改善农村交通。",
  "To narrow the urban-rural gap, the government must prioritise rural transport.",
  "不定式作目的状语"),
 ("许多父母把孩子送去学编程，认为这能保障他们的未来。",
  "Many parents send their children to coding classes, believing this will secure their future.",
  "believing 表看法"),
 ("不可否认，人均寿命在过去五十年里显著延长了。",
  "It is undeniable that life expectancy has risen markedly over the past fifty years.",
  "It is undeniable that"),
 ("问题与其说出在资金不足，不如说出在分配不均。",
  "The problem lies less in a lack of funding than in its uneven distribution.",
  "less in A than in B"),
 ("城市规划的目标应是服务居民，而不仅仅是吸引投资。",
  "The aim of urban planning should be to serve residents, not merely to attract investment.",
  "not merely A but B"),
 ("正是监管的缺失，而非技术本身，导致了数据滥用。",
  "It is the absence of regulation, rather than technology itself, that has led to data misuse.",
  "It is...that 强调句"),
 ("与其限制私家车，政府不如改善公共交通。",
  "Rather than restricting private cars, the government would do better to improve public transport.",
  "Rather than + would do better to"),
 ("大城市居民的平均通勤时间几乎是小城镇居民的两倍。",
  "Residents of large cities spend almost twice as long commuting as their small-town counterparts.",
  "twice as long as + counterparts"),
 ("只有当学校和家庭共同努力时，真正的改变才会发生。",
  "Only when schools and families work together will genuine change occur.",
  "Only when 引起部分倒装"),
 ("这一现象可归因于生活成本的持续上涨。",
  "This can be attributed to the continuous rise in living costs.",
  "be attributed to"),
]

# C 段落中译英 (标题, 中文, 参考译文)
HW_C = [
 ("段落 1 · 主体段",
  "远程办公最大的好处是它把时间还给了员工。通勤原本每天要消耗一到两个小时，"
  "而这段时间现在可以用于休息、运动或陪伴家人。结果是，许多人报告压力下降、"
  "工作满意度上升。更重要的是，这种安排让居住在小城市的人也能获得原本只属于大城市的工作机会。",
  "The greatest benefit of remote work is that it gives employees their time back. Commuting "
  "once consumed one or two hours a day, and this time can now be spent on rest, exercise or "
  "family. The consequence is that many people report lower stress and higher job satisfaction. "
  "More importantly, such arrangements give those living in smaller cities access to opportunities "
  "that were once confined to major urban centres."),
 ("段落 2 · 让步段",
  "诚然，博物馆免费开放会给政府带来财政压力。然而，把门票收入看作唯一的衡量标准过于狭隘。"
  "因此，尽管短期成本上升，社会长期获得的教育收益要大得多。换句话说，"
  "问题不在于我们是否负担得起免费博物馆，而在于我们是否负担得起没有它们。",
  "Admittedly, opening museums free of charge places a financial burden on governments. "
  "However, treating ticket revenue as the only measure of value is unduly narrow. "
  "Consequently, although short-term costs rise, the educational benefits society gains over "
  "time are far greater. In other words, the question is not whether we can afford free "
  "museums, but whether we can afford to be without them."),
]

# D 仿写任务
HW_D = dict(
  title="D｜范文仿写（骨架照搬，内容换新）",
  base="课堂范文 2（科技与读写能力）",
  prompt="Some people believe that the widespread use of online entertainment has reduced the "
         "amount of time young people spend on physical exercise. To what extent do you agree "
         "or disagree?",
  prompt_cn="有人认为，网络娱乐的普及减少了年轻人用于体育锻炼的时间。"
            "你在多大程度上同意或不同意？",
  rules=[
   "严格照搬范文 2 的四段骨架：引言（背景 + 限定式表态）→ 论证一（两层因果）→ "
   "论证二（Admittedly 让步 + However 转折）→ 结论（否定极端 + Until 条件）。",
   "每段第一句的功能必须与范文对应段一致，可以直接套用句型，只换内容词。",
   "必须用上课堂高分例句库里的 4 句（自选），并在句子下方画线标注。",
   "必须至少使用 2 个名词化主语、1 个 in turn、1 个 not merely...but。",
   "字数 260–300。",
  ],
)

# E 独立写作
HW_E = dict(
  title="E｜限时独立写作",
  prompt="Some people think that schools should teach practical skills such as cooking and money "
         "management, while others believe schools should focus on academic subjects. "
         "Discuss both views and give your own opinion.",
  prompt_cn="有人认为学校应教授烹饪、理财等实用技能，也有人认为学校应专注学术科目。"
            "讨论双方观点并给出你的看法。",
  rules=[
   "限时 40 分钟，不查词典、不看范文。写完再对照课堂范文 1 的骨架自评。",
   "先花 5 分钟列提纲：每段写一句中文主题句，再开始写英文。这一步不能省。",
   "字数 250 以上。",
  ],
  checklist=[
   "引言是否有明确表态？（不能只复述题目）",
   "每个主体段是否只讲一个论点？（一段一论点）",
   "每段是否有具体例子？（“一个具体的人”优于 many people）",
   "是否用了至少 3 个不同的过渡表达？（不能全是 and / but / so）",
   "是否有名词化主语？（数一数，少于 2 个就改写）",
   "结论是否给出了行动方向或条件？（不能只重复观点）",
  ],
)

# 错题本模板
ERROR_LOG_COLS = ("我写的", "参考表达", "错因（搭配 / 语序 / 句式单一 / 中式直译）", "重写一遍")
