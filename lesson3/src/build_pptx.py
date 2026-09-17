# -*- coding: utf-8 -*-
"""生成《雅思阅读精讲班 · 第三节课》PPT。

版式与第二节课 PPT 完全一致：每题两页
    ① 逐题标准精讲   —— 题干 / 入口 / 原文证据 / 同义替换 / 答案
    ② 长难句拆解 + 随题词汇 —— 原句 / 主干 / 分层 / 中文 / 词汇
"""

import os
import sys

_SRC = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_SRC))
sys.path.insert(0, _SRC)
# 版式引擎来自共享 skill，各课共用一份
sys.path.insert(0, os.path.join(_ROOT, ".claude", "skills", "ielts-lesson-deck"))

from deck import Deck                                         # noqa: E402
import questions as QS                                        # noqa: E402
import teach_p0, teach_p1, teach_p2, teach_p3, teach_p4       # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "第三节课PPT_雅思阅读精讲.pptx")

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
            ["开场作业复盘：The Development of Plastics Q1–13（第二节课作业）"],
            "purple", bold=True, sizes=(22, 20, 18, 17))

    d.three_col("ROADMAP", "今天的认知路线：从“会拆句”到“会拆题型”", [
        ("1 作业复盘", ["Plastics Q1–13", "表格 + 判断", "先对答案再讲错因"]),
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

    # ================================ 作业复盘：The Development of Plastics
    d.bullets("HOMEWORK REVIEW", "开场作业复盘：The Development of Plastics Q1–13", [
        (QS.P0_LEAD, "cream"),
        (["复盘要求", "1 先对答案，标出对错，但不要立刻看讲解。",
          "2 每道错题写出 P/S 定位，再写题干与原文的同义替换。",
          "3 最后写错因：定位错 / 替换错 / 范围与方向错。"], "green"),
        (["为什么用作业开场", "作业是隔了一周之后做的，它检验的不是记忆，而是方法有没有留下来。",
          "错在哪一步，决定你今天这节课该重点练什么。"], "blue"),
    ])
    d.passage_block(teach_p0, 0, "The Development of Plastics",
                  "表格按材料行推进，判断题看化学关系",
                  "第二节课作业 · The Development of Plastics",
                  label="作业", head="HOMEWORK · The Development of Plastics")

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
    d.passage_block(teach_p1, 1, "How much higher? How much faster?",
                  "判断 + 填空 + 选择三件套", "Passage 1 · How much higher? How much faster?")
    d.passage_block(teach_p2, 2, "What Do Whales Feel?",
                  "表格与简答的定位纪律", "Passage 2 · What Do Whales Feel?")
    d.passage_block(teach_p3, 3, "Visual Symbols and the Blind",
                  "选择 / 配对 / 词库摘要", "Passage 3 · Visual Symbols and the Blind",
                  hooks={30: diagram_slide})

    d.bullets("HOMEWORK", "课后作业：The Origins of Weather Forecasting", [
        ("限时 15 分钟完成 Q1–13，先做题，再用四步拆句法订正，最后核对答案。", "cream"),
        (["订正要求", "1 每题写出 P/S 定位与题干↔原文的同义替换。",
          "2 判断题写清“支持 / 矛盾 / 未提”，NOT GIVEN 要说明缺了哪一层关系。",
          "3 填空题检查 ONE WORD ONLY、单复数与原文拼写。"], "green"),
        ("以下逐题精讲用于自主订正；先做完再看，不要边做边翻。", "purple"),
    ])
    d.passage_block(teach_p4, 4, "The Origins of Weather Forecasting",
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
