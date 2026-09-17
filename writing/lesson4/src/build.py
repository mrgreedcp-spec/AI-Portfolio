# -*- coding: utf-8 -*-
"""生成第四课课堂练习材料与课后巩固（两份 DOCX）。

复用第二/三节课讲义的样式表，页眉改为 IELTS WRITING。
"""

import os
import sys

_SRC = os.path.dirname(os.path.abspath(__file__))
_LESSON = os.path.dirname(_SRC)
_WRITING = os.path.dirname(_LESSON)
sys.path.insert(0, _SRC)
sys.path.insert(0, os.path.join(os.path.dirname(_WRITING), "lesson3", "src"))

import docx_kit as K                                          # noqa: E402
import vocab_bank as VB                                       # noqa: E402
import translation as TR                                      # noqa: E402
import essays as ES                                           # noqa: E402

K.TEMPLATE = os.path.join(_WRITING, "assets", "handout_template.docx")

OUT_CLASS = os.path.join(_LESSON, "第四课课堂练习_雅思写作.docx")
OUT_HW = os.path.join(_LESSON, "第四课课后巩固_雅思写作.docx")

HDR = "IELTS WRITING 第四课 • 舒同学专用"


def blank_lines(doc, n=2, width=K.FULL_W):
    """留白书写区：n 行下划线。"""
    K.grid(doc, None, [("",)] * n, [width], size=10)


def part_class():
    doc = K.load(header=HDR)

    # ---------------------------------------------------------- 封面与导语
    K.para(doc, "LESSON 4 • 从词到句到段", style="Guide Kicker")
    K.para(doc, "雅思写作 · 第四课课堂练习材料", style="Heading 1")
    K.para(doc, "中译英驱动的表达组装：把“蹦出来的想法”装进英文句子，再装进逻辑段落。",
           style="Guide Lead")

    K.para(doc, "这节课为什么这样设计", style="Heading 2")
    for line in [
        "你的强项是想法多、反应快——课上总能蹦出不错的论点和关键词。",
        "卡住的地方不在“想不出”，而在“装不进去”：想法是中文的，句子是中式的，段落是散的。",
        "所以本节课不练“想”，只练“装”：词组 → 句子 → 段落，三级组装，全部用中译英驱动。",
        "本次课堂练习量刻意做满：60 组搭配 + 57 题中译英 + 40 句高分例句 + 2 篇范文 + 3 段组装。",
    ]:
        K.para(doc, line, style="Guide Detail")

    K.note_box(doc, "本课流程",
               "① 搭配库（20 分钟）→ ② 中译英 L1 词组（15 分钟）→ ③ 中译英 L2 句子（25 分钟）"
               "→ ④ 高分例句库（15 分钟）→ ⑤ 范文精读 ×2（25 分钟）"
               "→ ⑥ 段落组装（15 分钟）→ ⑦ 中译英 L3 段落（15 分钟）")

    K.note_box(doc, "一条规矩",
               "所有中译英都先自己写，写完再看参考译文。看了再写＝白练。"
               "参考译文只是“一种好写法”，不是唯一答案；只要搭配对、结构对，你的版本同样得分。",
               fill=K.FILL_SOFT)

    # -------------------------------------------------------------- 模块 1
    K.page_break(doc)
    K.para(doc, "模块 1", style="Guide Kicker")
    K.para(doc, "词汇搭配库：60 组“能直接用进作文”的搭配", style="Heading 1")
    K.para(doc, "只收你会想、但写不对的那一类。第三列是中式陷阱——那正是你现在最容易写出来的版本。",
           style="Guide Lead")
    for topic, items in VB.COLLOCATIONS:
        K.para(doc, topic, style="Heading 3")
        K.grid(doc, ("中文", "英文搭配", "中式陷阱 / 提示", "例句"),
               items, [1250, 2200, 2400, 4016], size=8.5)

    # -------------------------------------------------------------- 模块 2
    K.page_break(doc)
    K.para(doc, "模块 2 · 中译英 Level 1", style="Guide Kicker")
    K.para(doc, "词组级：30 题", style="Heading 1")
    K.para(doc, "目标：把零星想法固化成可以直接搬进句子的英文积木。先遮住右侧两列。",
           style="Guide Lead")
    K.grid(doc, ("#", "中文", "我的译文", "参考译文", "中式陷阱"),
           [(str(i), cn, "", en, trap) for i, (cn, en, trap) in enumerate(TR.L1, 1)],
           [580, 1820, 2100, 2560, 2806], size=8.5, first_bold=True)

    # -------------------------------------------------------------- 模块 3
    K.page_break(doc)
    K.para(doc, "模块 3 · 中译英 Level 2", style="Guide Kicker")
    K.para(doc, "句子级：24 题，四组高分句式", style="Heading 1")
    K.para(doc, "每组锁定一个句式。写之前先问自己：这句话的主语该是什么？——"
                "中式英语的第一个错，几乎都错在主语。", style="Guide Lead")
    for name, pattern, note, items in TR.L2:
        K.para(doc, f"{name}｜{pattern}", style="Heading 3")
        K.para(doc, note, style="Passage Note")
        K.grid(doc, ("中文", "我的译文", "参考译文", "写作提示"),
               [(cn, "", en, tip) for cn, en, tip in items],
               [2300, 2200, 3100, 2266], size=8.5)

    # -------------------------------------------------------------- 模块 4
    K.page_break(doc)
    K.para(doc, "模块 4", style="Guide Kicker")
    K.para(doc, "高分例句库：40 句，按功能分类", style="Heading 1")
    K.para(doc, "用法：每个功能挑 2 句抄进你的句型本，下次作文强制用上。"
                "不要全背——背不完，也用不上。", style="Guide Lead")
    for func, items in VB.MODEL_SENTENCES:
        K.para(doc, func, style="Heading 3")
        K.grid(doc, ("高分例句", "中文", "为什么高分"),
               items, [4200, 2600, 3066], size=8.5)

    # -------------------------------------------------------------- 模块 5
    for e in ES.ESSAYS:
        K.page_break(doc)
        K.para(doc, f"模块 5 · 范文 {e['no']}", style="Guide Kicker")
        K.para(doc, f"范文精读 {e['no']}：{e['kind']}", style="Heading 1")
        K.note_box(doc, "题目", f"{e['prompt']}\n{e['prompt_cn']}")

        K.para(doc, "范文全文", style="Heading 3")
        for tag, text in e["paras"]:
            K.para(doc, tag, style="Question Text", bold=True, space_after=1)
            K.para(doc, text, style="Passage Text")

        K.para(doc, "骨架拆解（这是要模仿的东西，不是背句子）", style="Heading 3")
        K.grid(doc, ("段落", "功能", "首句", "展开方式", "过渡词"),
               e["skeleton"], [900, 1500, 2700, 3200, 1566], size=8.5, first_bold=True)

        K.para(doc, "高分表达标注", style="Heading 3")
        K.grid(doc, ("表达", "为什么值得学"),
               e["highlights"], [4200, 5666], size=8.5, first_bold=True)

    # -------------------------------------------------------------- 模块 6
    K.page_break(doc)
    K.para(doc, "模块 6", style="Guide Kicker")
    K.para(doc, "段落组装：给你零散的词，写成有逻辑的段", style="Heading 1")
    K.para(doc, "这一模块直接对着你的瓶颈：课上你能蹦出这些词，但它们躺在纸上串不起来。"
                "现在练的就是串。", style="Guide Lead")
    for i, a in enumerate(TR.ASSEMBLY, 1):
        K.para(doc, f"练习 {i} · {a['topic']}", style="Heading 3")
        K.note_box(doc, "关键词", "　｜　".join(a["keywords"]), fill=K.FILL_SOFT)
        K.para(doc, a["task"], style="Question Text")
        K.para(doc, "我的段落：", style="Question Text", bold=True, space_after=2)
        blank_lines(doc, 5)
        K.para(doc, "参考段落", style="Question Text", bold=True, space_after=2)
        K.para(doc, a["model"], style="Passage Text")
        K.para(doc, "提示：" + a["note"], style="Passage Note")

    # -------------------------------------------------------------- 模块 7
    K.page_break(doc)
    K.para(doc, "模块 7 · 中译英 Level 3", style="Guide Kicker")
    K.para(doc, "段落级：3 段", style="Heading 1")
    K.para(doc, "到这一层，考的已经不是单词，是连接词和逻辑链。"
                "翻译前先在中文上标出：哪句是主题句，哪句是原因，哪句是结果。", style="Guide Lead")
    for title, cn, en, chain in TR.L3:
        K.para(doc, title, style="Heading 3")
        K.para(doc, cn, style="Passage Text")
        K.para(doc, "我的译文：", style="Question Text", bold=True, space_after=2)
        blank_lines(doc, 5)
        K.para(doc, "参考译文", style="Question Text", bold=True, space_after=2)
        K.para(doc, en, style="Passage Text")
        K.para(doc, "逻辑链：" + chain, style="Passage Note")

    # ---------------------------------------------------------------- 收尾
    K.page_break(doc)
    K.para(doc, "EXIT CHECK", style="Guide Kicker")
    K.para(doc, "下课前五分钟自查", style="Heading 1")
    K.grid(doc, ("自查项", "达标了吗"), [
        ("我能不看提示说出 10 组今天学的搭配", ""),
        ("我知道“名词化主语”是什么，并能当场造一句", ""),
        ("我能说出范文 1 每一段的功能（不是内容）", ""),
        ("我知道 Admittedly...; however,... 用在哪一段", ""),
        ("我能解释为什么 in turn 能让论证多出一层", ""),
        ("我今天写的段落里，至少有 3 个不同的过渡表达", ""),
    ], [6800, 3066], size=10, first_bold=True)

    K.note_box(doc, "带走一句话",
               "你的想法不需要更多，需要的是通道。中译英就是通道：先把意思钉死，再逼出结构。"
               "这周把课后巩固做完，下节课我们直接用你的译文改写成整篇作文。")

    doc.save(OUT_CLASS)
    print("OK ", OUT_CLASS)


def part_homework():
    doc = K.load(header=HDR)

    K.para(doc, "LESSON 4 • HOMEWORK", style="Guide Kicker")
    K.para(doc, "雅思写作 · 第四课课后巩固", style="Heading 1")
    K.para(doc, ES.HW_INTRO, style="Guide Lead")
    K.note_box(doc, "总量",
               "A 搭配默写 40 题　·　B 句子中译英 20 题　·　C 段落中译英 2 段　"
               "·　D 范文仿写 1 篇　·　E 限时独立写作 1 篇")

    # A
    K.para(doc, "A｜搭配默写（40 题）", style="Heading 2")
    K.para(doc, "遮住右列，先默写。错的用红笔抄三遍，并造一个句子。", style="Question Instruction")
    half = (len(ES.HW_A) + 1) // 2
    rows = []
    for i in range(half):
        l = ES.HW_A[i]
        r = ES.HW_A[i + half] if i + half < len(ES.HW_A) else ("", "")
        rows.append((str(i + 1), l[0], "", str(i + half + 1) if r[0] else "", r[0], ""))
    K.grid(doc, ("#", "中文", "英文", "#", "中文", "英文"), rows,
           [560, 1460, 1900, 560, 1460, 3926], size=8.5)
    K.para(doc, "答案（对完再看）", style="Heading 3")
    ans_rows = [tuple(f"{i + j * 10}. {ES.HW_A[i + j * 10 - 1][1]}" for j in range(4))
                for i in range(1, 11)]
    K.grid(doc, None, ans_rows, [2466] * 4, size=8)

    # B
    K.page_break(doc)
    K.para(doc, "B｜句子中译英（20 题）", style="Heading 2")
    K.para(doc, "每题右侧标了目标句式，写的时候必须用上。不用这个句式＝这题没做。",
           style="Question Instruction")
    K.grid(doc, ("#", "中文", "我的译文", "目标句式"),
           [(str(i), cn, "", pat) for i, (cn, en, pat) in enumerate(ES.HW_B, 1)],
           [560, 2900, 4300, 2106], size=8.5, first_bold=True)
    K.para(doc, "参考译文", style="Heading 3")
    K.grid(doc, ("#", "参考译文"),
           [(str(i), en) for i, (cn, en, pat) in enumerate(ES.HW_B, 1)],
           [560, 9306], size=8.5, first_bold=True)

    # C
    K.page_break(doc)
    K.para(doc, "C｜段落中译英（2 段）", style="Heading 2")
    K.para(doc, "翻译前先在中文上标出主题句、原因句、结果句，再动笔。",
           style="Question Instruction")
    for title, cn, en in ES.HW_C:
        K.para(doc, title, style="Heading 3")
        K.para(doc, cn, style="Passage Text")
        K.para(doc, "我的译文：", style="Question Text", bold=True, space_after=2)
        blank_lines(doc, 6)
        K.para(doc, "参考译文", style="Question Text", bold=True, space_after=2)
        K.para(doc, en, style="Passage Text")

    # D
    K.page_break(doc)
    d = ES.HW_D
    K.para(doc, d["title"], style="Heading 2")
    K.note_box(doc, "题目", f"{d['prompt']}\n{d['prompt_cn']}")
    K.para(doc, f"仿写对象：{d['base']}", style="Question Text", bold=True)
    K.para(doc, "要求", style="Heading 3")
    for i, r in enumerate(d["rules"], 1):
        K.para(doc, f"{i}. {r}", style="Question Text")
    K.para(doc, "作文（可另附纸）", style="Heading 3")
    blank_lines(doc, 16)

    # E
    K.page_break(doc)
    e = ES.HW_E
    K.para(doc, e["title"], style="Heading 2")
    K.note_box(doc, "题目", f"{e['prompt']}\n{e['prompt_cn']}")
    K.para(doc, "要求", style="Heading 3")
    for i, r in enumerate(e["rules"], 1):
        K.para(doc, f"{i}. {r}", style="Question Text")
    K.para(doc, "提纲（先写中文主题句，5 分钟）", style="Heading 3")
    blank_lines(doc, 4)
    K.para(doc, "作文（可另附纸）", style="Heading 3")
    blank_lines(doc, 16)
    K.para(doc, "写完自评清单", style="Heading 3")
    K.grid(doc, ("自评项", "是 / 否", "要改的地方"),
           [(c, "", "") for c in e["checklist"]],
           [4600, 1200, 4066], size=9, first_bold=True)

    # 错题本
    K.page_break(doc)
    K.para(doc, "ERROR LOG", style="Guide Kicker")
    K.para(doc, "错题本（本周至少记 15 条）", style="Heading 1")
    K.para(doc, "只记“我写的和参考不一样”的地方。错因写清楚是哪一类——"
                "一个月后翻回来，你会看到自己反复错在同一类上。", style="Guide Lead")
    K.grid(doc, ES.ERROR_LOG_COLS, [("", "", "", "")] * 18,
           [2300, 2600, 2400, 2566], size=9)

    doc.save(OUT_HW)
    print("OK ", OUT_HW)


if __name__ == "__main__":
    part_class()
    part_homework()
