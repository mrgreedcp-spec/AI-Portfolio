# -*- coding: utf-8 -*-
"""生成《雅思阅读精讲班 · 第三节课》PPT。

版式与第二节课 PPT 完全一致：每题两页
    ① 逐题标准精讲   —— 题干 / 入口 / 原文证据 / 同义替换 / 答案
    ② 长难句拆解 + 随题词汇 —— 原句 / 主干 / 分层 / 中文 / 词汇
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from deck import Deck, PAL                                    # noqa: E402
import questions as QS                                        # noqa: E402
import teach_p1, teach_p2, teach_p3, teach_p4, teach_pencil   # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "第三节课PPT_雅思阅读精讲.pptx")

LETTERS = "ABCDE"


# --------------------------------------------------------------- 逐题两页
def question_pair(d, q, foot):
    """一题两页：逐题标准精讲 + 长难句拆解 / 随题词汇。"""
    # ---------- 第一页：逐题标准精讲
    s = d.slide("逐题标准精讲", q["title"], foot)
    is_mcq = q["kind"] == "MCQ"

    if is_mcq:
        d.panel(s, 0.72, 1.40, 11.90, 0.58, [q["stem"]], "cream", bold=True,
                sizes=(23, 21, 19, 18, 17))
        opts = [f"{LETTERS[i]}  {o}" for i, o in enumerate(q["options"])]
        d.panel(s, 0.72, 2.06, 11.90, 1.34, opts, "amber", bold=False,
                sizes=(18, 17, 16, 15, 14), anchor=None)
        y2, h2 = 3.56, 1.28
        y3, h3 = 5.38, 1.16
    else:
        d.panel(s, 0.72, 1.42, 11.90, 1.02, [q["stem"]], "cream", bold=True,
                sizes=(24, 22, 20, 18, 17, 16))
        y2, h2 = 2.72, 1.52
        y3, h3 = 4.86, 1.62

    d.labelled(s, 0.78, y2, 3.55, h2, "① 入口", q["entry"], "purple", lw=2.4)
    d.labelled(s, 4.70, y2, 7.85, h2, "② 原文证据", [q["ev"]], "blue", lw=2.4)
    d.labelled(s, 0.78, y3, 7.30, h3, "③ 同义替换 / 判断逻辑", q["logic"], "green", lw=3.4)
    d.labelled(s, 8.45, y3, 4.10, h3, "④ 答案",
               [f"Answer: {q['ans']}"] + list(q["ansnote"]), "amber",
               bold=True, sizes=(21, 20, 19, 18, 17, 16), lw=2.4)

    # ---------- 第二页：长难句拆解 + 随题词汇
    s = d.slide("长难句拆解 + 随题词汇", q["stitle"], foot)
    d.panel(s, 0.72, 1.42, 11.90, 1.32, [q["sent"]], "cream", bold=True,
            sizes=(20.5, 19, 18, 17, 16, 15, 14))
    d.labelled(s, 0.78, 2.92, 3.24, 2.12, "核心主干", [q["core"]], "red",
               bold=True, sizes=(20, 19, 18, 17, 16, 15, 14), lw=2.0)
    d.labelled(s, 4.32, 2.92, 4.42, 2.12, "层层拆解",
               [f"· {x}" for x in q["layers"]], "blue",
               sizes=(18.8, 18, 17, 16, 15, 14, 13), lw=2.0)
    d.labelled(s, 9.04, 2.92, 3.51, 2.12, "课堂表达", [q["cn"]], "green",
               sizes=(19.2, 18, 17, 16, 15, 14, 13), lw=2.0)
    d.labelled(s, 0.78, 5.55, 11.77, 1.00, "随题词汇 / 同义替换", q["vocab"], "amber",
               bold=True, sizes=(18.5, 17.5, 16.5, 15.5, 14.5), lw=3.4)


def diagram_slide(d, foot):
    """Q30–32 三个轮子的图形对照页。"""
    s = d.slide("Q30–32 图形对照", "先看清三个轮子：轮辐画法决定运动类型", foot)
    d.panel(s, 0.78, 1.42, 11.77, 0.60,
            ["原文 P4 列出五种画法；题目只考三个图，另外两种正是干扰项的来源。"],
            "cream", bold=True, sizes=(19, 18, 17))
    board = d._box(s, 0.78, 2.20, 11.77, 3.05, "F8FAFC", "94A3B8")
    for cx, no, style, cap in ((2.86, 30, "extend", "直线且伸出轮圈"),
                               (6.66, 31, "dashed", "虚线／断续线"),
                               (10.46, 32, "curved", "弧形弯曲")):
        d.wheel(s, cx, 3.42, 0.78, style)
        lab = d._box(s, cx - 1.55, 4.42, 3.10, 0.62)
        d._write(lab, [f"{no}　{cap}"], 19, "0F172A", bold=True,
                 align=1, inset=0.0)
    d.panel(s, 0.78, 5.45, 11.77, 1.10,
            ["五组对照（原文顺序）：curved → steady spinning；wavy → wobbling；bent → jerking；",
             "extending beyond perimeter → use of brakes；dashed → rapid spinning。"],
            "green", bold=True, sizes=(19, 18, 17, 16))
    return s


def passage_block(d, mod, no, title_en, title_cn, foot, hooks=None):
    """一篇文章：文章地图 → 题型策略 → 逐题两页 → 小结。"""
    hooks = hooks or {}
    d.three_col("文章地图", f"PASSAGE {no} · {title_en}", mod.MAP)
    d.bullets("题型策略", f"Passage {no} 题型策略",
              [(t[0], tone) for t, tone in
               zip(mod.STRATEGY, ["cream", "blue", "purple", "green"])])
    for q in mod.Q:
        if q["n"] in hooks:
            hooks[q["n"]](d, foot)
        question_pair(d, q, foot)
    d.three_col("小结", f"Passage {no} 小结：{title_cn}", mod.SUMMARY)


def build():
    d = Deck()

    # ============================================================ 开场
    s = d.slide("IELTS ACADEMIC READING", "雅思阅读精讲班 · 第三节课")
    d.panel(s, 0.72, 1.78, 11.90, 0.72, ["题型拓展 × 逐题精讲 × 长难句"], "green",
            bold=True, sizes=(36, 32, 28))
    d.panel(s, 0.72, 2.80, 11.90, 1.20,
            ["本节新增题型：选择题 · 表格填空 · 简答题 · 图形配对 · 词库摘要",
             "延续第二节课：四步拆句法继续用在每一道题的“命中句”上"],
            "blue", bold=True, sizes=(22, 20, 18, 17))
    d.panel(s, 0.72, 4.35, 11.90, 0.95,
            ["材料：Athletics + Whales + Blind（Q1–40）+ Weather Forecasting（课后）"],
            "cream", bold=True, sizes=(24, 22, 20, 18))
    d.panel(s, 0.72, 5.55, 11.90, 0.95,
            ["课前延迟检索：Pencil 流程图版 Q1–8（第二节课留题）"],
            "purple", bold=True, sizes=(22, 20, 18, 17))

    d.three_col("ROADMAP", "今天的认知路线：从“会拆句”到“会拆题型”", [
        ("1 延迟检索", ["Pencil Q1–8", "先做再讲", "检验方法留存"]),
        ("2 题型拓展", ["选择题四步", "表格 / 简答", "图形 + 词库摘要"]),
        ("3 逐题精讲", ["一题两页", "第一页答案链", "第二页句法链"]),
    ])

    d.three_col("REVIEW", "第二课复盘：四步拆句法", [
        ("① 减法", ["圈有限谓语", "盖插入语", "先抓 S-V-O"]),
        ("② 分层", ["从句修饰谁", "状语说明什么", "代词指向谁"]),
        ("③ 回题", ["题干关系", "是否完整对应", "是否被偷换"]),
    ])

    d.three_col("LESSON GOALS", "第三课目标：题型不同，动作相同", [
        ("看得懂题型", ["题干先划限定", "空格先定词性", "选项先找差异"]),
        ("找得到证据", ["写 P/S", "一题一句", "跨段要连读"]),
        ("判得稳答案", ["核对比较方向", "核对范围程度", "核对词数形式"]),
    ])

    # ============================================== 课前延迟检索：Pencil Q1–8
    d.bullets("DELAYED RETRIEVAL", "课前延迟检索：Pencil 流程图版 Q1–8", [
        (teach_pencil.NOTE, "cream"),
        (["作答要求", "1 限时 6 分钟，不查词典、不讨论。",
          "2 每题写出 P/S 定位，再写答案。",
          "3 判断题必须写“支持 / 矛盾 / 未提”三选一。"], "green"),
        (["为什么隔一周再做", "当场做对＝短期记忆；隔一周做对＝方法真的留下来了。",
          "错在定位，还是错在同义替换？这一步决定你今天该练什么。"], "blue"),
    ])

    pen_foot = "Pencil Flow-chart Version · 延迟检索 Q1–8"
    for grp, rng in (("Q1–3 · Notes Completion", (1, 3)),
                     ("Q4–8 · TRUE / FALSE / NOT GIVEN", (4, 8))):
        items = [it for it in teach_pencil.ITEMS if rng[0] <= it[0] <= rng[1]]
        for no, kind, ans, loc, ev, expl in items:
            s = d.slide("延迟检索逐题复盘", f"Pencil {grp.split(' ·')[0]}｜Q{no}　答案：{ans}",
                        pen_foot)
            d.labelled(s, 0.78, 1.50, 11.77, 1.55, "① 原文证据", [f"{loc}: {ev}"],
                       "blue", sizes=(19, 18, 17, 16, 15), lw=2.4)
            d.labelled(s, 0.78, 3.45, 7.60, 1.85, "② 定位 + 同义替换 / 判断逻辑",
                       [expl], "green", sizes=(19, 18, 17, 16, 15), lw=4.0)
            d.labelled(s, 8.72, 3.45, 3.83, 1.85, "③ 答案",
                       [f"Answer: {ans}", f"题型：{kind}", f"定位：{loc}"], "amber",
                       bold=True, sizes=(21, 20, 19, 18, 17), lw=2.4)
            d.panel(s, 0.78, 5.70, 11.77, 0.85,
                    ["订正动作：先写 P/S，再写题干与原文的同义替换，最后写错因（定位错 / 替换错 / 范围错）。"],
                    "cream", bold=True, sizes=(18.5, 17.5, 16.5, 15.5))

    d.three_col("RETRIEVAL REVIEW", "延迟检索小结：错因只有三类", teach_pencil.REVIEW_POINTS)

    # ============================================================ 新题型方法
    d.bullets("NEW TYPES", "本节新增题型总览：先认动作，再做题", [
        ("选择题 MCQ：题干先划限定词 → 回原文找唯一支持句 → 四个选项逐个排除。", "cream"),
        ("表格填空 Table：表格＝原文顺序地图，先读行列标题定“该填什么词性”。", "blue"),
        ("简答题 Short-answer：疑问词决定答案词性，Which sense→感官名，Which species→物种名。", "purple"),
        ("图形配对 + 词库摘要：先在原文把所有对照关系配好，再回题面选；词库允许重复使用。", "green"),
    ])

    d.three_col("MCQ METHOD", "选择题四步：题干限定 → 唯一句 → 排除 → 复核", [
        ("① 划限定", ["first paragraph", "the writer found", "because / in order to"]),
        ("② 找唯一句", ["只允许一句支持", "跨段要连读", "写下 P/S"]),
        ("③ 排除", ["原文没说", "程度太强", "偷换对象"]),
    ])

    d.bullets("TABLE / SHORT-ANSWER", "表格题与简答题：把“词性”想在前面", [
        (["表格填空三查", "① 该空在哪一列？SPECIES 列填物种名，COMMENTS 列填方向 / 频率。",
          "② 词数上限是多少？NO MORE THAN THREE WORDS 就绝不能写四个词。",
          "③ 单复数与原文是否一致？frequencies / waters 都要保留复数。"], "blue"),
        (["简答题三查", "① 疑问词是什么？Which sense / Which species / What 决定答案词性。",
          "② 答案能不能压到 3 词以内？能压则压，不要抄整句。",
          "③ 是否照抄了原文拼写？简答题不需要自己改写。"], "green"),
    ])

    d.bullets("DIAGRAM & SUMMARY", "图形配对与词库摘要：先建对照表，再动笔", [
        (["图形配对", "原文若列出五种画法，就先把五组“画法 → 含义”全部写出来；",
          "题目只考三个图，另外两组正是干扰项的来源。"], "cream"),
        (["词库摘要（NB You may use any word more than once）", "① 先给每个空标词性：名词 / 形容词 / 人群词。",
          "② 同一个词可以重复使用（本篇 sighted 就用了两次）。",
          "③ 最后核对程度：resembled 只能选 similar，不能选 identical。"], "purple"),
    ])

    d.three_col("VOCAB INTEGRATION", "随题词汇：只背“这道题用得上”的替换", [
        ("题干 → 原文", ["respected → reputation", "supported → not impressed", "good time → right moment"]),
        ("名词化 ↔ 从句", ["introduction of X", "= X was introduced", "考点常在这一步"]),
        ("程度与方向", ["at least as ... as", "more ... than", "only / all / fully"]),
    ])

    # ============================================================ 四篇文章
    passage_block(d, teach_p1, 1, "How much higher? How much faster?",
                  "判断 + 填空 + 选择三件套", "Passage 1 · How much higher? How much faster?")
    passage_block(d, teach_p2, 2, "What Do Whales Feel?",
                  "表格与简答的定位纪律", "Passage 2 · What Do Whales Feel?")
    passage_block(d, teach_p3, 3, "Visual Symbols and the Blind",
                  "选择 / 配对 / 词库摘要", "Passage 3 · Visual Symbols and the Blind",
                  hooks={30: diagram_slide})

    d.bullets("HOMEWORK", "课后作业：The Origins of Weather Forecasting", [
        ("限时 15 分钟完成 Q1–13，先做题，再用四步拆句法订正，最后核对答案。", "cream"),
        (["订正要求", "1 每题写出 P/S 定位与题干↔原文的同义替换。",
          "2 判断题写清“支持 / 矛盾 / 未提”，NOT GIVEN 要说明缺了哪一层关系。",
          "3 填空题检查 ONE WORD ONLY、单复数与原文拼写。"], "green"),
        ("以下逐题精讲用于自主订正；先做完再看，不要边做边翻。", "purple"),
    ])
    passage_block(d, teach_p4, 4, "The Origins of Weather Forecasting",
                  "判断题看评价词，填空题看名词化",
                  "Passage 4 · The Origins of Weather Forecasting")

    # ============================================================ 收尾
    d.three_col("FINAL METHOD", "本节课最终方法：题型会变，动作不变", [
        ("读题", ["先划限定词", "先定词性 / 词数", "先看选项差异"]),
        ("定位", ["写 P/S", "一题一句", "跨段连读"]),
        ("核对", ["比较方向", "范围程度", "拼写与单复数"]),
    ])

    s = d.slide("EXIT TICKET", "两分钟出口检测：证明你已经会拆题型")
    d.panel(s, 0.82, 1.55, 11.72, 3.75, [
        "1  用一句话说明：Passage 1 Q3 为什么是 FALSE，而不是 NOT GIVEN。",
        "",
        "2  写出 Passage 2 Q25 的比较方向（谁的视觉更有用？为什么）。",
        "",
        "3  解释 Passage 3 Q39 为什么只能填 similar，不能填 identical。",
        "",
        "4  写出一组“名词化 ↔ 从句”的转换（提示：Passage 4 Q9）。",
    ], "cream", bold=True, sizes=(22, 20, 19, 18, 17))
    d.panel(s, 0.82, 5.62, 11.72, 0.95,
            ["课后要求：完成 Weather Forecasting Q1–13，并为每篇文章各挑 3 道错题，"
             "重写 P/S、题干锚点、原文证据与错因。"],
            "blue", bold=True, sizes=(19, 18, 17, 16))

    d.save(OUT)
    print(f"OK  {OUT}")
    print(f"    slides = {d.n}")
    return d.n


if __name__ == "__main__":
    build()
