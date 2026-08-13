# -*- coding: utf-8 -*-
"""生成《雅思阅读精讲 · 第三节课打印资料》。

结构与第二节课打印资料一致：
    本节材料怎么用 → 方法卡 → 课前延迟检索 → 四篇文章（标注 P/S 的原文 + 题目 +
    长难句拆解区）→ 答案速查 → 词汇与长难句讲解
题目、题号与答案全部照抄所给材料，未作改动。
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import docx_kit as K                                          # noqa: E402
import passages as P                                          # noqa: E402
import questions as QS                                        # noqa: E402
import vocab as V                                             # noqa: E402
import teach_p1, teach_p2, teach_p3, teach_p4, teach_pencil   # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "第三节课打印资料_雅思阅读精讲.docx")

LETTERS = "ABCD"

WHEELS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                      "assets", "wheels_q30_32.png")


# ------------------------------------------------------------------ 小工具
def passage_body(doc, paras):
    """输出 [P1] [S1] ... 形式的原文。"""
    for line in P.annotated(paras):
        K.para(doc, line, style="Passage Text")


def mcq(doc, num, stem, options):
    K.para(doc, f"{num}  {stem}", style="Question Text", space_after=2)
    for i, o in enumerate(options):
        K.para(doc, f"　　{LETTERS[i]}　{o}", style="Question Text",
               size=10, space_after=1)


def tfng_list(doc, items):
    for n, s in items:
        K.para(doc, f"{n}  {s}", style="Question Text", space_after=3)


def notes_list(doc, items):
    for kind, text in items:
        if kind == "H":
            K.para(doc, text, style="Question Text", bold=True, space_after=2)
        else:
            K.para(doc, f"　•  {text}", style="Question Text", space_after=2)


def qhead(doc, head, ins=None):
    K.para(doc, head, style="Heading 3")
    if ins:
        K.para(doc, ins, style="Question Instruction")


def analysis_zone(doc, key):
    K.para(doc, "长难句拆解区", style="Heading 3")
    K.para(doc, "每句按“谓语 → 主语 → 从句/非谓语 → 逻辑关系 → 简化主干”的顺序拆解。"
                "课堂先自己画，再跟随讲解修正。", style="Passage Note")
    K.blank_analysis_table(doc, [s[0] for s in V.LONG[key][:3]])


# ------------------------------------------------------------------ 各部分
def part_intro(doc):
    K.para(doc, "LESSON 3 • QUESTION-TYPE TOOLKIT", style="Guide Kicker")
    K.para(doc, "雅思阅读精讲 · 第三节课打印资料", style="Heading 1")
    K.para(doc, "题型拓展 × 逐题精讲 × 长难句：选择题 · 表格填空 · 简答题 · 图形配对 · 词库摘要",
           style="Guide Lead")

    K.para(doc, "本节材料怎么用", style="Heading 2")
    for line in [
        "0. 课前延迟检索：Pencil 流程图版 Q1–8（第二节课留题），建议限时 6 分钟，先做再讲。",
        "1. How much higher? How much faster?：课堂精讲，判断 + 句子填空 + 选择三种题型一次打通。",
        "2. What Do Whales Feel?：课堂精讲，练表格填空的“行列定位”与简答题的“疑问词定词性”。",
        "3. Visual Symbols and the Blind：课堂精讲，新增图形配对与带词库的摘要填空。",
        "4. The Origins of Weather Forecasting：课后独立作业，建议 15 分钟；本讲义附逐题精讲，做完再看。",
    ]:
        K.para(doc, line, style="Guide Detail")

    K.note_box(doc, "使用建议",
               "先按顺序做题，再看答案。订正时对每道错题写三件事：①原文 P/S 定位；"
               "②题干与原文的同义替换；③错因属于“定位错 / 替换错 / 范围与方向错”中的哪一类。"
               "文末的词汇与长难句讲解用于课后复习，不要在做题时翻看。")


def part_method(doc):
    K.para(doc, "新题型方法卡：先认动作，再做题", style="Heading 1")

    K.para(doc, "1｜选择题 Multiple Choice", style="Heading 3")
    K.grid(doc, ("步骤", "动作", "本节例题"), [
        ("① 划限定", "题干里的范围词先圈出：first paragraph / the writer found / because",
         "P3 Q27 限定在第一段"),
        ("② 找唯一句", "回原文找一句能独立支持答案的句子，写下 P/S",
         "P1 Q11 → P7 S3"),
        ("③ 排除", "原文没说 / 程度太强 / 偷换对象，三类干扰逐个划掉",
         "P3 Q29 排除 D（“更好”）"),
        ("④ 复核", "把选中的选项放回题干，确认与原文关系完全一致",
         "P1 Q12 too ... to 是否定"),
    ], [1200, 5100, 3566], first_bold=True)

    K.para(doc, "2｜表格填空 Table / 简答题 Short-answer", style="Heading 3")
    K.grid(doc, ("题型", "先做的判断", "最后的检查"), [
        ("表格填空", "该空在哪一列？SPECIES 列填物种名，COMMENTS 列填方向 / 频率等",
         "词数上限、单复数、原文拼写"),
        ("简答题", "疑问词是什么？Which sense → 感官名；Which species → 物种名；What → 名词",
         "能否压到 3 词以内，不要抄整句"),
    ], [1400, 5300, 3166], first_bold=True)

    K.para(doc, "3｜图形配对 Diagram / 词库摘要 Summary with a box", style="Heading 3")
    K.grid(doc, ("题型", "关键动作"), [
        ("图形配对", "原文列出几种画法就先全部配好（本篇是五组），题目只考三个图，"
                     "另外两组正是干扰项的来源；先配原文，再看图。"),
        ("词库摘要", "①先给每个空标词性（名词 / 形容词 / 人群词）；②注意 NB You may use any word "
                     "more than once，同一个词可以重复使用；③最后核对程度词——"
                     "closely resembled 只能选 similar，不能选 identical。"),
    ], [1400, 8466], first_bold=True)

    K.note_box(doc, "贯穿全节",
               "题型会变，动作不变：读题（划限定 / 定词性）→ 定位（写 P/S，一题一句）→ "
               "核对（比较方向、范围程度、拼写与单复数）。", fill=K.FILL_SOFT)


def part_pencil(doc):
    K.page_break(doc)
    K.para(doc, "课前延迟检索", style="Guide Kicker")
    K.para(doc, "The History of the Pencil — Flow-chart Version（Q1–8）", style="Heading 1")
    K.para(doc, teach_pencil.NOTE, style="Guide Lead")
    K.note_box(doc, "作答要求",
               "限时 6 分钟，不查词典、不讨论。每题先写 P/S 定位再写答案；"
               "判断题必须写出“支持 / 矛盾 / 未提”三选一。原文见第二节课打印资料 Passage 3。")

    qhead(doc, QS.PEN_Q1_3_HEAD, QS.PEN_Q1_3_INS)
    notes_list(doc, QS.PEN_NOTES)
    qhead(doc, QS.PEN_Q4_8_HEAD, "Write TRUE, FALSE or NOT GIVEN. 每题同时记录 P/S。")
    tfng_list(doc, QS.PEN_Q4_8)

    K.para(doc, "逐题精讲（做完再看）", style="Heading 3")
    K.grid(doc, ("题号", "答案", "定位", "原文证据", "讲解"),
           [(str(n), a, loc, ev, expl)
            for n, kind, a, loc, ev, expl in teach_pencil.ITEMS],
           [560, 1160, 860, 3700, 3586], size=8.5, first_bold=True)


def part_passage(doc, no, title_en, title_cn, sub, paras, key, lead, advice,
                 questions_fn, kicker, footnote=None):
    K.page_break(doc)
    K.para(doc, f"PASSAGE {no} • {kicker}", style="Guide Kicker")
    K.para(doc, title_en, style="Heading 1")
    K.para(doc, title_cn, style="Heading 3")
    if sub:
        K.para(doc, sub, style="Guide Lead")
    K.para(doc, lead, style="Passage Note")
    K.note_box(doc, "建议", advice)

    passage_body(doc, paras)
    if footnote:
        K.para(doc, footnote, style="Passage Note")

    questions_fn(doc)
    analysis_zone(doc, key)


def q_passage1(doc):
    qhead(doc, QS.P1_Q1_6_HEAD, QS.P1_Q1_6_INS)
    tfng_list(doc, QS.P1_Q1_6)
    qhead(doc, QS.P1_Q7_10_HEAD, QS.P1_Q7_10_INS)
    tfng_list(doc, QS.P1_Q7_10)
    qhead(doc, QS.P1_Q11_13_HEAD, QS.P1_Q11_13_INS)
    for n, stem, opts in QS.P1_Q11_13:
        mcq(doc, n, stem, opts)


def q_passage2(doc):
    qhead(doc, QS.P2_Q15_21_HEAD, QS.P2_Q15_21_INS)
    K.grid(doc, QS.P2_TABLE[0], QS.P2_TABLE[1:], [1100, 2400, 1300, 5066], size=9)
    K.para(doc, QS.P2_TABLE_NOTE, style="Passage Note")
    qhead(doc, QS.P2_Q22_26_HEAD, QS.P2_Q22_26_INS)
    tfng_list(doc, QS.P2_Q22_26)


def q_passage3(doc):
    qhead(doc, QS.P3_Q27_29_HEAD, QS.P3_Q27_29_INS)
    for n, stem, opts in QS.P3_Q27_29:
        mcq(doc, n, stem, opts)

    qhead(doc, QS.P3_Q30_32_HEAD, QS.P3_Q30_32_INS)
    K.image(doc, WHEELS, width_in=6.3)
    K.grid(doc, None, [("30", "31", "32")], [3288, 3289, 3289], size=10,
           align=K.CENTER)
    K.grid(doc, ("题号", "图示（轮辐画法）", "English description"),
           [(str(n), cn, en) for n, cn, en in QS.P3_DIAGRAMS],
           [700, 4200, 4966], size=9, first_bold=True)
    K.para(doc, "List of types of movement：" +
           "　".join(f"{a}  {b}" for a, b in QS.P3_MOVE_LIST),
           style="Question Text")

    qhead(doc, QS.P3_Q33_39_HEAD, QS.P3_Q33_39_INS)
    K.para(doc, QS.P3_SUMMARY, style="Question Text")
    K.grid(doc, None, [QS.P3_WORD_BOX[i:i + 5] for i in range(0, 15, 5)],
           [1973] * 5, size=9, body_fill=K.FILL_SOFT)

    qhead(doc, QS.P3_Q40_HEAD, QS.P3_Q40_INS)
    mcq(doc, QS.P3_Q40[0], QS.P3_Q40[1], QS.P3_Q40[2])


def q_passage4(doc):
    qhead(doc, QS.P4_Q1_5_HEAD, QS.P4_Q1_5_INS)
    tfng_list(doc, QS.P4_Q1_5)
    qhead(doc, QS.P4_Q6_13_HEAD, QS.P4_Q6_13_INS)
    notes_list(doc, QS.P4_NOTES)


def part_answers(doc):
    K.page_break(doc)
    K.para(doc, "ANSWER KEY", style="Guide Kicker")
    K.para(doc, "所有文章答案速查", style="Heading 1")
    K.note_box(doc, "使用规则", "课堂练习结束前不要翻到本页。订正时先找到证据 P/S，再看答案。")

    def two_col(title, answers, order, per_row=3):
        """每行放 per_row 组「题号 + 答案」，整块答案尽量不跨页。"""
        K.para(doc, title, style="Heading 3")
        cells = [(str(n), answers[n]) for n in order]
        rows = []
        for i in range(0, len(cells), per_row):
            chunk = cells[i:i + per_row]
            row = []
            for num, ans in chunk:
                row += [num, ans]
            row += [""] * ((per_row - len(chunk)) * 2)
            rows.append(tuple(row))
        w = [520, 2769] * per_row
        w[-1] = K.FULL_W - sum(w[:-1])
        K.grid(doc, None, rows, w, size=9.5, first_bold=False)

    two_col("课前延迟检索 · Pencil Flow-chart Version（Q1–8）",
            QS.PEN_ANSWERS, sorted(QS.PEN_ANSWERS))
    two_col("Passage 1 · How much higher? How much faster?",
            QS.P1_ANSWERS, sorted(QS.P1_ANSWERS))
    two_col("Passage 2 · What Do Whales Feel?",
            QS.P2_ANSWERS, sorted(QS.P2_ANSWERS))
    two_col("Passage 3 · Visual Symbols and the Blind",
            QS.P3_ANSWERS, sorted(QS.P3_ANSWERS))
    two_col("Passage 4 · The Origins of Weather Forecasting（课后作业）",
            QS.P4_ANSWERS, sorted(QS.P4_ANSWERS))

    K.para(doc, "* Passage 2 Q21：原表印作 “bowhead whales and humpback whales”，"
                "编号空 21 只考第一个词 bowhead，第二处点线是原书 humpback 的印刷位置。",
           style="Passage Note")
    K.para(doc, "* Passage 2 Q26：hearing 与 acoustic sense 均可，注意不超过三个词。",
           style="Passage Note")


def part_explain(doc):
    """每篇文章的逐题精讲表（答案 + 定位 + 同义替换）。"""
    K.page_break(doc)
    K.para(doc, "QUESTION-BY-QUESTION", style="Guide Kicker")
    K.para(doc, "逐题精讲：答案 · 定位 · 同义替换", style="Heading 1")
    K.para(doc, "与课堂 PPT 完全对应；课后订正时先自己写一遍，再对照本表。", style="Guide Lead")

    for title, mod in (("Passage 1 · How much higher? How much faster?", teach_p1),
                       ("Passage 2 · What Do Whales Feel?", teach_p2),
                       ("Passage 3 · Visual Symbols and the Blind", teach_p3),
                       ("Passage 4 · The Origins of Weather Forecasting", teach_p4)):
        K.para(doc, title, style="Heading 2")
        rows = []
        for q in mod.Q:
            loc = q["ev"].split(":")[0]
            rows.append((str(q["n"]), q["ans"], loc,
                         "\n".join(q["entry"]), "\n".join(q["logic"])))
        K.grid(doc, ("题号", "答案", "定位", "入口（题干怎么读）", "同义替换 / 判断逻辑"),
               rows, [560, 1300, 900, 3106, 4000], size=8.5, first_bold=True)


def part_vocab(doc):
    K.page_break(doc)
    K.para(doc, "VOCABULARY & LONG SENTENCES", style="Guide Kicker")
    K.para(doc, "词汇与长难句讲解", style="Heading 1")
    K.para(doc, "复习顺序：原句 → 自己找主干 → 再核对翻译与简化后的主干意思。",
           style="Guide Lead")
    K.note_box(doc, "使用建议",
               "同义替换不要求全部背诵；优先做到“看到题干表达时，能在原文认出另一种说法”。"
               "长难句复习时先遮住翻译，只做两步：①找主语 + 核心谓语 + 必要宾语/补语；"
               "②用简洁中文说出主干意思。")

    titles = {
        "P1": "1. How much higher? How much faster?｜人类运动表现的极限",
        "P2": "2. What Do Whales Feel?｜鲸类的感官",
        "P3": "3. Visual Symbols and the Blind｜视觉符号与盲人",
        "P4": "4. The Origins of Weather Forecasting｜天气预报的起源",
    }
    for key in ("P1", "P2", "P3", "P4"):
        K.para(doc, titles[key], style="Heading 2")

        K.para(doc, "A｜重点雅思词汇与同义替换", style="Heading 3")
        K.grid(doc, ("词汇 · 核心义", "IELTS 同义替换（优先常用表达）", "记忆方法",
                     "迁移例句 + 中文翻译"),
               V.VOCAB[key], [1900, 2900, 2100, 2966], size=8.5)

        K.para(doc, "B｜长难句：先抓主干，再理解完整句", style="Heading 3")
        for i, (src, cn, core, simple) in enumerate(V.LONG[key], 1):
            K.para(doc, f"长难句 {i}", style="Heading 4"
                   if "Heading 4" in [s.name for s in doc.styles] else "Heading 3")
            K.grid(doc, None, [
                ("原句", src), ("原句理解翻译", cn),
                ("句子主干", core), ("简化后的主干意思", simple),
            ], [1700, 8166], size=8.5, first_bold=True)


# ------------------------------------------------------------------ main
def build():
    doc = K.load()

    part_intro(doc)
    part_method(doc)
    part_pencil(doc)

    part_passage(doc, 1, P.P1_TITLE, P.P1_CN, P.P1_SUB, P.P1_PARAS, "P1",
                 "课堂精讲：判断题看比较方向与全称词；句子填空用介词预测词性；"
                 "选择题先划题干限定再排除。",
                 "限时 20 分钟完成 Q1–13；不查词典。判断题写出“支持 / 矛盾 / 未提”，"
                 "填空题先写词性。", q_passage1, "IN-CLASS ANALYSIS")

    part_passage(doc, 2, P.P2_TITLE, P.P2_CN, P.P2_SUB, P.P2_PARAS, "P2",
                 "课堂精讲：表格是原文顺序的地图，按行找段、按列定词性；"
                 "简答题用疑问词决定答案词性。",
                 "限时 20 分钟完成 Q15–26；表格题注意 NO MORE THAN THREE WORDS，"
                 "简答题注意单复数与原文拼写。", q_passage2, "IN-CLASS ANALYSIS",
                 footnote="1. echolocation: " + P.P2_FOOTNOTE.split(": ", 1)[1])

    part_passage(doc, 3, P.P3_TITLE, P.P3_CN, None, P.P3_PARAS, "P3",
                 "课堂精讲：Part 1 为图形配对与实验结论，Part 2 为词库摘要；"
                 "注意 P1–P5 属 Part 1，P6–P8 属 Part 2。",
                 "限时 20 分钟完成 Q27–40；图形配对先在原文配好五组对照，"
                 "词库摘要注意同一个词可以重复使用。", q_passage3, "IN-CLASS ANALYSIS")

    part_passage(doc, 4, P.P4_TITLE, P.P4_CN, P.P4_SUB, P.P4_PARAS, "P4",
                 "课后独立作业：判断题陷阱集中在评价词，笔记填空按 P6 → P8 顺序推进。",
                 "限时 15 分钟完成 Q1–13；完成后先自己订正，再看文末的逐题精讲与答案。",
                 q_passage4, "HOMEWORK")

    part_answers(doc)
    part_explain(doc)
    part_vocab(doc)

    doc.save(OUT)
    print(f"OK  {OUT}")
    return OUT


if __name__ == "__main__":
    build()
