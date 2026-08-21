# -*- coding: utf-8 -*-
"""托福基础写作 Academic Discussion 第2课 · 课堂PPT
官方题源：TOEFL iBT Writing — Write for an Academic Discussion（Dr. Gupta / sociology）
        TOEFL iBT Writing — Write for an Academic Discussion（Dr. Diaz / marketing）
        ETS TOEFL iBT Writing Practice Set 2 & 4 官方 Response Tips / Sample Responses
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck_engine import *
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

D = Deck()

# ============================================================================
# 官方题目原文（逐字引用，不改写）
# ============================================================================
Q_PROF = ("For the past few classes, we have been discussing the concept of social "
          "mobility which refers to the ability of individuals or families to move up "
          "or down the social hierarchy. Some argue that education is the key to social "
          "mobility, while others believe that networking and personal connections are "
          "more important. Which viewpoint do you agree with? Why?")
Q_KELLY = ("I believe that education is the key to social mobility. With a good education, "
           "individuals can acquire the knowledge and skills needed to access better job "
           "opportunities and improve their social status. We have always been taught that "
           "education provides a foundation for long-term success and upward mobility.")
Q_ANDREW = ("In my opinion, networking and personal connections are more crucial for social "
            "mobility. Knowing the right people can open doors to opportunities that education "
            "alone might not provide. Therefore, personal connections can lead to job offers, "
            "mentorship, and other advantages that help individuals climb the social ladder.")

HW_PROF = ("Next week we'll be discussing the role of social media influencers in marketing "
           "campaigns. Some marketers believe that influencers are essential for marketing "
           "products. Others argue that traditional advertising methods are more effective "
           "than social media influencers. What are your thoughts on this issue?")
HW_KELLY = ("I believe that social media influencers are essential for reaching target audiences. "
            "Influencers have a loyal following and their recommendations can be very persuasive. "
            "This personal connection makes influencer marketing a powerful tool for promoting "
            "products and increasing brand awareness.")
HW_ANDREW = ("I think traditional advertising methods are still more reliable. While influencers "
             "can be effective, there is a risk of their followers being skeptical of sponsored "
             "content. Traditional advertising methods, such as TV and print ads, have proven "
             "track records and can reach a broader audience.")

SRC = "题源：TOEFL iBT® Writing · Write for an Academic Discussion（官方题目原文，未改写）"

RESP_A = ("I agree with Kelly. I think education is more important for social mobility. "
          "Education is very useful for people. When people study in school, they can learn "
          "many things, and it can help them find a good job. A good job can make their life "
          "better. Andrew says personal connections are important, but I think education is "
          "more important. Not everyone can know important people, but everyone can go to "
          "school. So I think education is the key to social mobility because it is good for "
          "people's future.")

RESP_B = ("In my view, education matters more than personal connections for social mobility. "
          "One important reason is that education gives people skills that employers can "
          "actually check. A degree or a certificate shows that a person has completed real "
          "training, so a company is willing to interview them even if they know no one "
          "inside. For example, a student from a small town who finishes a nursing program "
          "can apply to a city hospital without knowing anyone there. I understand Andrew's "
          "point that connections open doors, but connections usually help people who already "
          "have the qualifications.")

RESP_C1 = ("I would argue that education matters more, although the two are not really "
           "separate. One important reason is that education is the one advantage a person "
           "can build without already belonging to a network. Skills can be earned by "
           "studying, while connections usually have to be inherited or introduced. This "
           "matters because students from ordinary families simply have no one to introduce "
           "them.")
RESP_C2 = ("For example, a student whose parents are farmers can finish an accounting "
           "qualification, pass a company's entrance test, and be hired by a firm where she "
           "knows nobody. As a result, her first job then becomes her first network. I agree "
           "with Andrew that connections open doors, but I would add that education is usually "
           "what gets a person into the room where those connections are formed.")
RESP_C = RESP_C1 + " " + RESP_C2


# ============================================================================
# 0 · 开场
# ============================================================================
D.part = "开场"

s = D.slide(footer=False, bg=TEAL)
D.rect(s, 0, 0, SW, 0.42, fill=ACCENT, line=None)
D.rect(s, 0.95, 1.45, 0.07, 3.5, fill=ACCENT, line=None)
t = D.tb(s, 1.32, 1.42, 10.6, 0.4)
D.p(t, "TOEFL iBT  ·  WRITING  ·  ACADEMIC DISCUSSION", size=19, bold=True,
    color=RGBColor(0x9E, 0xC6, 0xCE), space_after=10)
t = D.tb(s, 1.32, 1.95, 11.0, 1.6)
D.p(t, "托福基础写作", size=50, bold=True, color=WHITE, space_after=2, line_spacing=1.0)
D.p(t, "Academic Discussion 第 2 课", size=50, bold=True, color=WHITE, space_after=0, line_spacing=1.0)
t = D.tb(s, 1.32, 3.62, 11.0, 0.6)
D.p(t, "从一个熟悉的题目，迁移到一道全新的官方真题", size=25, color=RGBColor(0xC9, 0xDE, 0xE3), space_after=0)
D.line(s, 1.32, 4.55, 6.4, 4.55, RGBColor(0x3E, 0x77, 0x84), 1.5)
t = D.tb(s, 1.32, 4.75, 11.0, 1.2)
D.p(t, "本课官方题目 · TOEFL iBT Writing｜Write for an Academic Discussion", size=19,
    color=WHITE, space_after=4)
D.p(t, "Dr. Gupta（sociology）：Education or personal connections — which is the key to social mobility?",
    size=19, color=RGBColor(0xC9, 0xDE, 0xE3), space_after=0)
D.tag(s, 1.32, 6.15, "4 人小班", fill=ACCENT, size=17, h=0.42)
D.tag(s, 3.0, 6.15, "2 小时", fill=RGBColor(0x2A, 0x7E, 0x8E), size=17, h=0.42)
D.tag(s, 4.5, 6.15, "6 个环节", fill=RGBColor(0x2A, 0x7E, 0x8E), size=17, h=0.42)
D.notes(s, "开场30秒：今天不再讲 Internship。今天要证明一件事——第1课学的流程，换任何一道官方题都能用。")

# --- 今天的一句话目标
s = D.slide()
D.part = "开场"
y = D.header(s, "今天这节课，只解决一件事", "TODAY'S ONE THING")
D.rect(s, ML, y + 0.05, CW, 1.35, fill=ACCENT_PALE, line=None, rounded=True)
t = D.tb(s, ML + 0.4, y + 0.32, CW - 0.8, 0.9)
D.p(t, "看到一道完全没见过的官方 AD 题，你也能在 10 分钟内写出 100 词以上、有理由、有例子、有回应的 response。",
    size=25, bold=True, color=ACCENT, space_after=0, line_spacing=1.2)
y2 = y + 1.65
cols = [
    ("不是今天的目标", GREY, TEAL_TINT, ["背一篇范文", "背一套万能模板", "把 Internship 那题写得更好"]),
    ("是今天的目标", GREEN, GREEN_PALE, ["拿到新题 → 找到争议点", "一个理由 → 展开成 4 句", "对同学的观点 → 加新信息"]),
]
for i, (ttl, col, bg, items) in enumerate(cols):
    x = ML + i * (CW / 2 + 0.15)
    w = CW / 2 - 0.15
    cy = D.card(s, x, y2, w, 2.85, ttl, fill=bg, line=LINE, title_color=col, title_size=22)
    tt = D.tb(s, x + 0.34, cy + 0.14, w - 0.68, 2.0)
    for it in items:
        D.p(tt, it, size=BODY, color=INK if i else GREY, space_after=13, bullet="×" if i == 0 else "√")
D.notes(s, "把'不是目标'先说掉，学生会松一口气：今天不考背诵。")

# --- 上节课回顾
s = D.slide()
y = D.header(s, "上一节课，我们已经拿到的东西", "RECALL · 30 秒")
box = [("题型", "教授提问 + 两位同学发言 + 你加入讨论"),
       ("时间", "10 分钟 · 至少 100 词"),
       ("官方指令", "Express and support your opinion；make a contribution to the discussion in your own words"),
       ("结构", "Position → Reason → Why → Example → Result")]
yy = y + 0.1
for k, v in box:
    D.rect(s, ML, yy, CW, 0.92, fill=TEAL_TINT, line=LINE, rounded=True)
    D.rect(s, ML, yy, 0.07, 0.92, fill=TEAL_MID, line=None)
    tt = D.tb(s, ML + 0.34, yy + 0.16, 1.9, 0.5)
    D.p(tt, k, size=20, bold=True, color=TEAL, space_after=0)
    tt = D.tb(s, ML + 2.35, yy + 0.17, CW - 2.75, 0.6)
    D.p(tt, v, size=BODY, color=INK, space_after=0)
    yy += 1.05
D.notes(s, "只念，不展开。学生若答不出'官方指令'，直接给出，不要停留。")

# --- 路线图
s = D.slide()
y = D.header(s, "今天的路线图", "ROADMAP")
parts = [
    ("1", "Warm-up", "把上节课的方法叫醒", "10′", TEAL_MID),
    ("2", "官方新题", "读懂题，找到争议", "20′", TEAL_MID),
    ("3", "3 / 4 / 5 分", "看见差距在哪里", "25′", ACCENT),
    ("4", "Reason 展开", "一个理由写成一段", "30′", ACCENT),
    ("5", "Contribution", "回应同学，加新信息", "20′", GOLD),
    ("6", "Full Writing", "10 分钟完整写作", "20′", GREEN),
]
x = ML
w = (CW - 0.5) / 6
for num, ttl, sub, mins, col in parts:
    D.rect(s, x, y + 0.25, w, 4.25, fill=WHITE, line=LINE, rounded=True)
    D.rect(s, x, y + 0.25, w, 0.62, fill=col, line=None, rounded=True)
    D.rect(s, x, y + 0.65, w, 0.22, fill=col, line=None)
    tt = D.tb(s, x, y + 0.36, w, 0.4)
    D.p(tt, f"PART {num}", size=16, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
    tt = D.tb(s, x + 0.14, y + 1.05, w - 0.28, 0.9)
    D.p(tt, ttl, size=21, bold=True, color=INK, align=PP_ALIGN.CENTER, space_after=8, line_spacing=1.05)
    tt = D.tb(s, x + 0.14, y + 2.05, w - 0.28, 1.0)
    D.p(tt, sub, size=BODY, color=GREY, align=PP_ALIGN.CENTER, space_after=0, line_spacing=1.15)
    tt = D.tb(s, x + 0.14, y + 3.90, w - 0.28, 0.4)
    D.p(tt, mins, size=20, bold=True, color=col, align=PP_ALIGN.CENTER, space_after=0)
    x += w + 0.1
D.notes(s, "指着 Part 3 说：今天最重要的一屏在这里——你会亲眼看到 3 分和 5 分差在哪。")

# --- 核心流程闭环
s = D.slide()
y = D.header(s, "今天要装进脑子的，是这条流程", "THE ONE PROCESS")
chain = ["读题\n找争议", "选一边\nPosition", "找理由\nReason", "解释\nWHY", "举例子\nExample", "给结果\nResult", "回应同学\nContribution"]
x = ML
bw = (CW - 6 * 0.26) / 7
for i, c in enumerate(chain):
    col = TEAL if i < 2 else (ACCENT if i < 6 else GOLD)
    D.rect(s, x, y + 0.75, bw, 1.5, fill=WHITE, line=col, lw=2.0, rounded=True)
    tt = D.tb(s, x + 0.06, y + 1.0, bw - 0.12, 1.1)
    for ln in c.split("\n"):
        D.p(tt, ln, size=BODY, bold=True, color=col, align=PP_ALIGN.CENTER, space_after=2, line_spacing=1.1)
    if i < 6:
        tt = D.tb(s, x + bw, y + 1.28, 0.26, 0.4)
        D.p(tt, "▶", size=16, color=LINE, align=PP_ALIGN.CENTER, space_after=0)
    x += bw + 0.26
D.rect(s, ML, y + 2.75, CW, 1.5, fill=TEAL_TINT, line=LINE, rounded=True)
tt = D.tb(s, ML + 0.4, y + 3.0, CW - 0.8, 1.1)
D.p(tt, "第 1 课我们用 Internship 走了一遍。今天换一道你从没见过的官方题，再走一遍。", size=22, bold=True, color=TEAL, space_after=8)
D.p(tt, "如果两道完全不同的题都能走通，说明你拿到的是方法，不是范文。", size=BODY, color=INK, space_after=0)
D.rect(s, ML, y + 4.35, CW, 0.62, fill=GOLD_PALE, line=None, rounded=True)
tt = D.tb(s, ML + 0.34, y + 4.50, CW - 0.7, 0.42)
D.p(tt, "任务：在上面这条链条里，圈出你上次写 Internship 时最卡的那一环。", size=19, bold=True, color=GOLD, space_after=0)
D.notes(s, "这张图今天会反复回来。每个 Part 结束时指一次：我们现在在链条的哪一环。学生圈的位置就是今天要盯的人。")


# ============================================================================
# 可复用版式
# ============================================================================
def demo_card(s, x, y, w, rows, title="老师示范  WORKED EXAMPLE", fill=GREEN_PALE,
              accent=GREEN, row_gap=0.52, label_w=1.55, size=BODY):
    """rows: list of (label, text) — 逐步升级示范"""
    h = 0.66 + len(rows) * row_gap + 0.12
    D.rect(s, x, y, w, h, fill=fill, line=None, rounded=True)
    D.rect(s, x, y, 0.07, h, fill=accent, line=None)
    tt = D.tb(s, x + 0.3, y + 0.2, w - 0.6, 0.34)
    D.p(tt, title, size=LABEL, bold=True, color=accent, space_after=0)
    yy = y + 0.62
    for lab, txt in rows:
        tl = D.tb(s, x + 0.3, yy, label_w, 0.4)
        D.p(tl, lab, size=18, bold=True, color=accent, space_after=0)
        tv = D.tb(s, x + 0.3 + label_w, yy - 0.03, w - 0.65 - label_w, 0.5)
        D.p(tv, txt, size=size, color=INK, space_after=0, line_spacing=1.1)
        yy += row_gap
    return y + h


def ask_row(s, x, y, w, num, prompt, hint=None, lines=1, gap=0.42, prompt_size=BODY,
            num_color=ACCENT):
    """一道练习：编号 + 题干 + 提示 + 书写线"""
    ph = max(0.40, est_h(prompt, prompt_size, w - 0.62, 1.10))
    D.rect(s, x, y, 0.42, 0.42, fill=num_color, line=None, rounded=True, adj=0.5)
    tn = D.tb(s, x, y + 0.055, 0.42, 0.4)
    D.p(tn, str(num), size=17, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
    tt = D.tb(s, x + 0.56, y + 0.01, w - 0.56, ph)
    D.p(tt, prompt, size=prompt_size, bold=True, color=INK, space_after=0, line_spacing=1.10)
    yy = y + ph + 0.05
    if hint:
        hh = max(0.32, est_h(hint, 19, w - 0.62, 1.10))
        th = D.tb(s, x + 0.56, yy, w - 0.56, hh)
        D.p(th, hint, size=19, color=ACCENT, space_after=0, line_spacing=1.10)
        yy += hh + 0.02
    yy += 0.14
    for i in range(lines):
        D.line(s, x + 0.56, yy + i * gap, x + w, yy + i * gap, LINE, 1.0)
    return yy + (lines - 1) * gap + 0.22


def output_slide(title, kicker, task, rules, timing, extra=None):
    s = D.slide()
    y = D.header(s, title, kicker, color=GOLD)
    D.rect(s, ML, y + 0.1, CW, 1.25, fill=GOLD_PALE, line=None, rounded=True)
    D.rect(s, ML, y + 0.1, 0.07, 1.25, fill=GOLD, line=None)
    tt = D.tb(s, ML + 0.36, y + 0.34, CW - 0.8, 0.9)
    D.p(tt, task, size=24, bold=True, color=GOLD, space_after=0, line_spacing=1.15)
    yy = y + 1.62
    for i, r in enumerate(rules):
        D.rect(s, ML, yy, CW, 0.72, fill=WHITE, line=LINE, rounded=True)
        tn = D.tb(s, ML + 0.28, yy + 0.16, 0.5, 0.4)
        D.p(tn, f"{i+1}", size=19, bold=True, color=GOLD, space_after=0)
        tt = D.tb(s, ML + 0.82, yy + 0.16, CW - 1.2, 0.5)
        D.p(tt, r, size=BODY, color=INK, space_after=0)
        yy += 0.82
    D.tag(s, ML, yy + 0.12, timing, fill=GOLD, size=17, h=0.42)
    if extra:
        tt = D.tb(s, ML + 2.1, yy + 0.18, CW - 2.2, 0.5)
        D.p(tt, extra, size=BODY, color=GREY, space_after=0)
    return s


def official_card(s, x, y, w, speaker, role, text, color=TEAL, fill=TEAL_TINT,
                  size=BODY, h=None, lines=None):
    th = est_h(text, size, w - 0.56, 1.18)
    h = h or (0.74 + th + 0.14)
    D.rect(s, x, y, w, h, fill=fill, line=LINE, rounded=True)
    D.rect(s, x, y, w, 0.5, fill=color, line=None, rounded=True)
    D.rect(s, x, y + 0.28, w, 0.22, fill=color, line=None)
    tt = D.tb(s, x + 0.28, y + 0.11, w - 0.5, 0.36)
    D.p(tt, f"{speaker}   {role}", size=LABEL, bold=True, color=WHITE, space_after=0)
    tv = D.tb(s, x + 0.28, y + 0.64, w - 0.56, th)
    D.p(tv, text, size=size, color=INK, space_after=0, line_spacing=1.18)
    return y + h


def quote_bar(s, x, y, w, speaker, text, color=TEAL_MID, fill=TEAL_TINT, note=None):
    """一行原文回顾条（完整原文见 Part 2 / 讲义）"""
    tw = 2.30
    th = est_h(text, 19, w - tw - 0.7, 1.12)
    h = max(0.86, th + 0.42)
    D.rect(s, x, y, w, h, fill=fill, line=None, rounded=True)
    D.rect(s, x, y, 0.07, h, fill=color, line=None)
    tt = D.tb(s, x + 0.28, y + 0.2, tw, 0.4)
    D.p(tt, speaker, size=20, bold=True, color=color, space_after=0)
    tv = D.tb(s, x + tw + 0.4, y + 0.2, w - tw - 0.7, th)
    D.p(tv, text, size=19, italic=True, color=INK, space_after=0, line_spacing=1.12)
    if note:
        tn = D.tb(s, x + 0.28, y + 0.56, tw, 0.32)
        D.p(tn, note, size=19, color=GREY, space_after=0)
    return y + h + 0.14


# ============================================================================
# PART 1 · Warm-up（10 分钟）
# ============================================================================
D.part = "Part 1 · Warm-up"
D.section("Warm-up", "把上一节课的方法叫醒", 10,
          "不重讲理论，只做一件事——把一个空句子补成一条完整的理由链。",
          ["一个句子", "三个空", "每人一条"], "PART 1")

s = D.slide()
y = D.header(s, "一个句子，三个空", "WARM-UP · 规则")
D.rect(s, ML, y + 0.1, CW, 1.1, fill=TEAL, line=None, rounded=True)
tt = D.tb(s, ML + 0.4, y + 0.36, CW - 0.8, 0.6)
D.p(tt, "______________ is beneficial because ______________.", size=28, bold=True,
    color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
yy = y + 1.5
items = [("Reason", "理由是什么？（不许写 it is good）", ACCENT),
         ("Why", "为什么会这样？它是怎么发生的？", ACCENT),
         ("Example", "谁 + 做了什么 + 结果怎样？", ACCENT)]
for lab, q, col in items:
    D.rect(s, ML, yy, CW, 0.88, fill=WHITE, line=LINE, rounded=True)
    D.rect(s, ML, yy, 1.55, 0.88, fill=ACCENT_PALE, line=None, rounded=True)
    tl = D.tb(s, ML, yy + 0.22, 1.55, 0.45)
    D.p(tl, lab, size=20, bold=True, color=col, align=PP_ALIGN.CENTER, space_after=0)
    tv = D.tb(s, ML + 1.8, yy + 0.24, CW - 2.2, 0.5)
    D.p(tv, q, size=BODY, color=INK, space_after=0)
    yy += 1.0
D.notes(s, "不要解释理论。直接说：填这三个空，就是第1课全部内容。")

s = D.slide()
y = D.header(s, "先把三个词对齐", "先说清楚 · 免得各写各的")
defs = [("Reason", "理由", "回答「为什么你这么认为」。一句话，必须有具体内容。",
         "Because it gives students something a textbook cannot.", TEAL),
        ("Example", "例子", "一个具体的人 + 他做的一件具体的事 + 结果。不是「很多人」。",
         "A student who joins a club has to ask three classmates for help.", ACCENT),
        ("Contribution", "贡献", "在同学说过的话之外，再加一个他没说过的信息。",
         "I agree with Kelly, and I would also add that ______.", GOLD)]
yy = y + 0.15
for en, cn, meaning, ex, col in defs:
    D.rect(s, ML, yy, CW, 1.42, fill=WHITE, line=col, lw=1.8, rounded=True)
    D.rect(s, ML, yy, 2.9, 1.42, fill=col, line=None, rounded=True)
    tn = D.tb(s, ML + 0.12, yy + 0.32, 2.66, 0.5)
    D.p(tn, en, size=21, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=2)
    D.p(tn, cn, size=19, color=RGBColor(0xEC, 0xF2, 0xF4), align=PP_ALIGN.CENTER, space_after=0)
    tt = D.tb(s, ML + 3.2, yy + 0.22, CW - 3.5, 0.45)
    D.p(tt, meaning, size=19, bold=True, color=INK, space_after=0)
    tt = D.tb(s, ML + 3.2, yy + 0.78, CW - 3.5, 0.45)
    D.p(tt, ex, size=19, italic=True, color=col, space_after=0)
    yy += 1.54
D.notes(s, "这一页是为第一次上 AD 课的同学准备的。老生只需 30 秒确认，不要展开讲。")

s = D.slide()
y = D.header(s, "先看老师怎么填", "WARM-UP · 示范")
demo_card(s, ML, y + 0.08, CW, [
    ("句子", "Joining a campus club is beneficial because it gives students a regular reason to talk to strangers."),
    ("Reason", "it gives students a regular reason to talk to strangers"),
    ("Why", "This matters because most first-year students never speak to anyone outside their own class."),
    ("Example", "For example, a shy student who joins a photography club has to ask three classmates to help carry equipment."),
    ("Result", "As a result, by the end of the term she has people to eat lunch with."),
], row_gap=0.60, label_w=1.35, size=BODY)
D.rect(s, ML, y + 4.05, CW, 0.75, fill=ACCENT_PALE, line=None, rounded=True)
tt = D.tb(s, ML + 0.34, y + 4.24, CW - 0.7, 0.5)
D.p(tt, "注意：Reason 里没有一个 good / important / useful。", size=BODY, bold=True, color=ACCENT, space_after=0)
D.notes(s, "念一遍，让学生指出：哪一句是 WHY，哪一句是 Example。30 秒。")

s = D.slide()
y = D.header(s, "轮到你 · 练习 1", "WARM-UP · 学生输出")
D.rect(s, ML, y + 0.02, CW, 0.62, fill=TEAL_PALE, line=None, rounded=True)
tt = D.tb(s, ML + 0.3, y + 0.17, CW - 0.6, 0.45)
D.p(tt, "把下面两句补完整：Reason 一行，Why 一行，Example 一行。", size=BODY, bold=True, color=TEAL, space_after=0)
yy = y + 0.86
yy = ask_row(s, ML, yy, CW, 1, "Doing a part-time job is beneficial because ______.",
             "Why 提示：time management / talking to real customers / getting paid for mistakes", lines=3)
ask_row(s, ML, yy + 0.12, CW, 2, "Taking online courses is beneficial because ______.",
        "Why 提示：students who work / recorded lectures / study at night", lines=3)
D.notes(s, "限时 3 分钟。走动，只看有没有写 useful/good 这类空词，看到就画圈。")

s = D.slide()
y = D.header(s, "轮到你 · 练习 2（换个方向）", "WARM-UP · 学生输出")
D.rect(s, ML, y + 0.02, CW, 0.62, fill=TEAL_PALE, line=None, rounded=True)
tt = D.tb(s, ML + 0.3, y + 0.17, CW - 0.6, 0.45)
D.p(tt, "同样三行。这两句离今天的正题更近一点。", size=BODY, bold=True, color=TEAL, space_after=0)
yy = y + 0.86
yy = ask_row(s, ML, yy, CW, 3, "Knowing the right people is beneficial because ______.",
             "Why 提示：hear about a job early / someone introduces you / get advice", lines=3)
ask_row(s, ML, yy + 0.12, CW, 4, "Finishing a university degree is beneficial because ______.",
        "Why 提示：proof for strangers / a company that has never met you", lines=3)
D.notes(s, "这两句是今天官方题的两个方向。先埋下去，Part 2 揭晓。")

output_slide("每人读一条", "OUTPUT · 30 秒 × 4 人", "读你写的其中一条：Reason + Why + Example，一口气读完。",
             ["读完后，其他人只回答一个问题：这条 Reason 里有没有 good / important / useful？",
              "如果有——现场换掉那个词，不要下课再改。",
              "如果例子里没有'谁'，补一个人进去。"],
             "3 分钟", "彭子骞第一个读——先给最短的那条。")
D.notes(D.prs.slides[-1], "新生第一个读，压力最小；老生随后读长的。")

s = D.slide()
y = D.header(s, "Warm-up 小结：三个空里最难的永远是 WHY", "WARM-UP · 收")
cols = [("Reason", "大多数人能写", "但常常是空词", GREY),
        ("Example", "教一次就会", "只要记住'谁+做什么+结果'", TEAL),
        ("WHY", "最容易被跳过", "也是 3 分和 5 分的分水岭", ACCENT)]
x = ML
w = (CW - 0.4) / 3
for ttl, a, b, col in cols:
    D.rect(s, x, y + 0.35, w, 2.7, fill=WHITE, line=col, lw=2.0, rounded=True)
    tt = D.tb(s, x + 0.25, y + 0.65, w - 0.5, 0.5)
    D.p(tt, ttl, size=26, bold=True, color=col, align=PP_ALIGN.CENTER, space_after=10)
    tt = D.tb(s, x + 0.25, y + 1.35, w - 0.5, 1.4)
    D.p(tt, a, size=BODY, bold=True, color=INK, align=PP_ALIGN.CENTER, space_after=10, line_spacing=1.15)
    D.p(tt, b, size=BODY, color=GREY, align=PP_ALIGN.CENTER, space_after=0, line_spacing=1.15)
    x += w + 0.2
D.rect(s, ML, y + 3.35, CW, 0.95, fill=TEAL, line=None, rounded=True)
tt = D.tb(s, ML + 0.4, y + 3.58, CW - 0.8, 0.6)
D.p(tt, "接下来：把这三个空，搬到一道你从没见过的官方真题上。", size=23, bold=True,
    color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
D.notes(s, "过渡句必须说出来：换题不换流程。")


# ============================================================================
# PART 2 · Homework Skill Transfer（20 分钟）
# ============================================================================
D.part = "Part 2 · 官方新题"
D.section("官方新题 · Skill Transfer", "读懂一道你没见过的官方真题", 20,
          "拿到新题的前 60 秒，先做三件事：找问题、数选项、看两个人分别站哪边。",
          ["读题", "填表", "定立场"], "PART 2")

s = D.slide()
y = D.header(s, "换题不换流程", "TRANSFER · 这一步为什么重要")
D.rect(s, ML, y + 0.15, CW / 2 - 0.2, 2.0, fill=TEAL_TINT, line=LINE, rounded=True)
tt = D.tb(s, ML + 0.32, y + 0.42, CW / 2 - 0.85, 1.5)
D.p(tt, "第 1 课", size=20, bold=True, color=GREY, space_after=8)
D.p(tt, "Internship 要不要成为毕业要求", size=BODY, color=INK, space_after=8)
D.p(tt, "你写过、改过、讲过——所以看起来会写。", size=BODY, color=GREY, space_after=0)
D.rect(s, ML + CW / 2 + 0.2, y + 0.15, CW / 2 - 0.2, 2.0, fill=ACCENT_PALE, line=None, rounded=True)
tt = D.tb(s, ML + CW / 2 + 0.52, y + 0.42, CW / 2 - 0.85, 1.5)
D.p(tt, "今天", size=20, bold=True, color=ACCENT, space_after=8)
D.p(tt, "一道全新的官方题（sociology）", size=BODY, bold=True, color=ACCENT, space_after=8)
D.p(tt, "没写过、没改过、没背过——这才叫会写。", size=BODY, color=INK, space_after=0)
tt = D.tb(s, ML + CW / 2 - 0.32, y + 0.95, 0.7, 0.5)
D.p(tt, "▶", size=26, color=LINE, align=PP_ALIGN.CENTER, space_after=0)
D.rect(s, ML, y + 2.45, CW, 1.55, fill=TEAL, line=None, rounded=True)
tt = D.tb(s, ML + 0.45, y + 2.72, CW - 0.9, 1.1)
D.p(tt, "考场上你遇到的一定是没见过的题。", size=23, bold=True, color=WHITE, space_after=10)
D.p(tt, "所以今天真正练的不是这道题，而是「拿到任何一道题以后的前 60 秒」。", size=BODY,
    color=RGBColor(0xC9, 0xDE, 0xE3), space_after=0)
D.notes(s, "如果学生问'这题会考吗'——回答：题不会重复，流程会重复。")

s = D.slide()
y = D.header(s, "官方指令原文（逐字）", "OFFICIAL DIRECTIONS")
D.rect(s, ML, y + 0.1, CW, 3.35, fill=WHITE, line=TEAL, lw=1.6, rounded=True)
tt = D.tb(s, ML + 0.45, y + 0.42, CW - 0.9, 2.9)
D.p(tt, "Your professor is teaching a class on sociology. Write a post responding to the professor's question.",
    size=21, bold=True, color=INK, space_after=14, line_spacing=1.2)
D.p(tt, "In your response, you should do the following.", size=21, bold=True, color=TEAL, space_after=8)
D.p(tt, "Express and support your opinion.", size=21, color=INK, space_after=6, bullet="•")
D.p(tt, "Make a contribution to the discussion in your own words.", size=21, color=INK, space_after=12, bullet="•")
D.p(tt, "An effective response will contain at least 100 words.", size=21, bold=True, color=ACCENT, space_after=0)
yy = y + 3.65
for i, (k, v) in enumerate([("10 分钟", "从看到题到交卷"), ("100 词", "官方写明的最低量"),
                            ("2 件事", "表明观点 + 加入讨论")]):
    x = ML + i * (CW / 3)
    D.rect(s, x, yy, CW / 3 - 0.2, 0.85, fill=ACCENT_PALE, line=None, rounded=True)
    tt = D.tb(s, x + 0.28, yy + 0.14, CW / 3 - 0.7, 0.6)
    D.p(tt, k, size=21, bold=True, color=ACCENT, space_after=2)
    D.p(tt, v, size=19, color=INK, space_after=0)
D.notes(s, "重点圈两处：in your own words / at least 100 words。这是评分官第一眼看的东西。")

s = D.slide()
y = D.header(s, "第一屏：只给教授的问题", "OFFICIAL QUESTION · Dr. Gupta")
official_card(s, ML, y + 0.1, CW, "Dr. Gupta", "sociology · 教授提问", Q_PROF,
              color=TEAL, fill=WHITE, size=21, lines=5)
D.rect(s, ML, y + 2.55, CW, 1.55, fill=TEAL_TINT, line=LINE, rounded=True)
tt = D.tb(s, ML + 0.4, y + 2.78, CW - 0.8, 1.15)
D.p(tt, "先不看两位同学说了什么。", size=21, bold=True, color=TEAL, space_after=8)
D.p(tt, "考场上很多人的错误就是：先读同学的话，然后被带着走，最后忘了教授到底问什么。",
    size=BODY, color=INK, space_after=0, line_spacing=1.18)
tt = D.tb(s, ML, 6.42, CW, 0.4)
D.p(tt, SRC, size=19, color=GREY, space_after=0)
D.notes(s, "让学生用手遮住下半屏。先读教授问题两遍。")

s = D.slide()
y = D.header(s, "读题任务 · 60 秒", "TASK · 学生输出", color=GOLD)
D.rect(s, ML, y + 0.05, CW, 0.72, fill=GOLD_PALE, line=None, rounded=True)
tt = D.tb(s, ML + 0.34, y + 0.22, CW - 0.7, 0.5)
D.p(tt, "不写句子，只回答这三个问题。写在讲义第 1 页。", size=BODY, bold=True, color=GOLD, space_after=0)
yy = y + 1.0
qs = ["题目在问什么？（用中文一句话说出来）",
      "一共有几个选择？分别是什么？",
      "这题允许「两个都重要」吗？为什么？"]
for i, q in enumerate(qs):
    D.rect(s, ML, yy, CW, 1.12, fill=WHITE, line=LINE, rounded=True)
    D.rect(s, ML, yy, 0.06, 1.12, fill=GOLD, line=None)
    tt = D.tb(s, ML + 0.34, yy + 0.16, CW - 0.7, 0.45)
    D.p(tt, f"{i+1}.  {q}", size=BODY, bold=True, color=INK, space_after=0)
    D.line(s, ML + 0.5, yy + 0.88, ML + CW - 0.3, yy + 0.88, LINE, 1.0)
    yy += 1.24
D.notes(s, "第3问是核心：这题只能选一个更重要，不能和稀泥。")

s = D.slide()
y = D.header(s, "两位同学的原文", "STUDENT A · STUDENT B")
official_card(s, ML, y + 0.05, CW, "Kelly", "Student A · 教育派", Q_KELLY,
              color=TEAL_MID, fill=TEAL_TINT, size=BODY, lines=4)
official_card(s, ML, y + 2.35, CW, "Andrew", "Student B · 人脉派", Q_ANDREW,
              color=ACCENT, fill=ACCENT_PALE, size=BODY, lines=4)
D.notes(s, "让学生各读一段。读完立刻问：Kelly 的关键词是什么？Andrew 的关键词是什么？")

s = D.slide()
y = D.header(s, "把整道题压缩成一张表", "TASK · 填表 · 学生输出", color=GOLD)
rows = [("Topic", "这场讨论在争什么？（中文即可）"),
        ("Student A · Kelly", "她站哪边？她的理由是什么？"),
        ("Student B · Andrew", "他站哪边？他的理由是什么？"),
        ("My position", "我站哪边？（现在就定，不许犹豫）")]
yy = y + 0.15
for i, (k, v) in enumerate(rows):
    col = GOLD if i == 3 else TEAL
    D.rect(s, ML, yy, CW, 1.02, fill=GOLD_PALE if i == 3 else WHITE, line=LINE, rounded=True)
    tt = D.tb(s, ML + 0.3, yy + 0.14, 3.0, 0.45)
    D.p(tt, k, size=BODY, bold=True, color=col, space_after=2)
    tt2 = D.tb(s, ML + 0.3, yy + 0.55, 3.0, 0.4)
    D.p(tt2, v.split("？")[0][:0] or "", size=19, color=GREY, space_after=0)
    tt3 = D.tb(s, ML + 3.4, yy + 0.16, CW - 3.8, 0.4)
    D.p(tt3, v, size=19, color=GREY, space_after=0)
    D.line(s, ML + 3.4, yy + 0.80, ML + CW - 0.3, yy + 0.80, LINE, 1.0)
    yy += 1.14
D.notes(s, "限时 90 秒。My position 必须写，不许写'both'。")

s = D.slide()
y = D.header(s, "对照一下：老师的表长这样", "ANSWER KEY · 填表")
rows = [("Topic", "社会阶层向上流动，靠教育还是靠人脉？", TEAL),
        ("Student A · Kelly", "教育。理由：教育给知识和技能 → 拿到更好的工作机会", TEAL_MID),
        ("Student B · Andrew", "人脉。理由：认识对的人 → 打开教育给不了的门（工作机会、导师）", ACCENT),
        ("My position", "教育（今天全班统一走这一边，先把方法练熟）", GOLD)]
yy = y + 0.15
for k, v, col in rows:
    D.rect(s, ML, yy, CW, 0.98, fill=WHITE, line=col, lw=1.6, rounded=True)
    tt = D.tb(s, ML + 0.32, yy + 0.26, 3.1, 0.5)
    D.p(tt, k, size=BODY, bold=True, color=col, space_after=0)
    tt = D.tb(s, ML + 3.5, yy + 0.24, CW - 3.9, 0.6)
    D.p(tt, v, size=BODY, color=INK, space_after=0, line_spacing=1.12)
    yy += 1.1
D.rect(s, ML, yy + 0.06, CW, 0.72, fill=TEAL_TINT, line=None, rounded=True)
tt = D.tb(s, ML + 0.34, yy + 0.24, CW - 0.7, 0.5)
D.p(tt, "今天统一选 education，是为了集中练展开。作业里你可以选另一边。", size=BODY, bold=True, color=TEAL, space_after=0)
D.notes(s, "统一立场是教学决定，要说清理由，否则学生以为教育就是标准答案。")

s = D.slide()
y = D.header(s, "争议点在哪里", "THE REAL QUESTION")
D.rect(s, ML, y + 0.35, CW / 2 - 0.35, 1.9, fill=TEAL_TINT, line=TEAL_MID, lw=1.8, rounded=True)
tt = D.tb(s, ML + 0.35, y + 0.62, CW / 2 - 1.05, 1.4)
D.p(tt, "EDUCATION", size=22, bold=True, color=TEAL, space_after=8)
D.p(tt, "你自己能挣来的东西：知识、技能、文凭、证书", size=BODY, color=INK, space_after=0, line_spacing=1.15)
D.rect(s, ML + CW / 2 + 0.35, y + 0.35, CW / 2 - 0.35, 1.9, fill=ACCENT_PALE, line=ACCENT, lw=1.8, rounded=True)
tt = D.tb(s, ML + CW / 2 + 0.7, y + 0.62, CW / 2 - 1.05, 1.4)
D.p(tt, "CONNECTIONS", size=22, bold=True, color=ACCENT, space_after=8)
D.p(tt, "别人给你的东西：介绍、机会、导师、内部消息", size=BODY, color=INK, space_after=0, line_spacing=1.15)
tt = D.tb(s, ML + CW / 2 - 0.35, y + 1.05, 0.7, 0.5)
D.p(tt, "VS", size=24, bold=True, color=GREY, align=PP_ALIGN.CENTER, space_after=0)
D.rect(s, ML, y + 2.6, CW, 1.5, fill=WHITE, line=ACCENT, lw=2.0, rounded=True)
tt = D.tb(s, ML + 0.42, y + 2.85, CW - 0.85, 1.1)
D.p(tt, "题目问的不是「教育重不重要」——那没人反对。", size=21, bold=True, color=ACCENT, space_after=8)
D.p(tt, "题目问的是：当两个都有用的时候，哪一个才是 the key（真正起决定作用的那个）。", size=BODY, color=INK, space_after=0)
D.notes(s, "这是本节课最容易跑题的地方。写'教育很重要'的人会全部掉到 3 分。")

s = D.slide()
y = D.header(s, "三个会让你掉分的读题错误", "TRAPS")
traps = [("写成「两个都重要」", "官方问 which viewpoint do you agree with——它要一个选择。",
          "先选一边，再在最后一句承认另一边有道理。"),
         ("只写「教育很重要」", "这是常识，不是观点。所有人都同意的句子不产生分数。",
          "写成「教育比人脉更关键，因为……」。"),
         ("把 Kelly 的话换个词再说一遍", "官方原话：make a contribution … in your own words。重复不算贡献。",
          "同意她之后，必须再加一个她没说过的信息。")]
yy = y + 0.15
for i, (bad, why, fix) in enumerate(traps):
    D.rect(s, ML, yy, CW, 1.5, fill=WHITE, line=LINE, rounded=True)
    D.rect(s, ML, yy, 0.06, 1.5, fill=ACCENT, line=None)
    tt = D.tb(s, ML + 0.34, yy + 0.16, CW - 0.7, 0.45)
    D.rich(tt, [("×  ", {"bold": True, "color": ACCENT, "size": 20}), (bad, {"bold": True, "size": 20})])
    tt = D.tb(s, ML + 0.34, yy + 0.62, CW - 0.7, 0.4)
    D.p(tt, why, size=19, color=GREY, space_after=0)
    tt = D.tb(s, ML + 0.34, yy + 1.02, CW - 0.7, 0.4)
    D.rich(tt, [("√  ", {"bold": True, "color": GREEN, "size": 19}), (fix, {"color": GREEN, "size": 19, "bold": True})])
    yy += 1.62
D.notes(s, "第三条留到 Part 5 再深挖，这里只提一句。")

output_slide("定立场 · 一句话", "OUTPUT · 每人一句", "现在写下你的第一句话：立场句。不许超过两行。",
             ["句型可用：I would argue that … / In my view, … / I believe that …",
              "句子里必须出现比较：more … than … 或 the key",
              "写完举手，老师逐个念，只判断一件事：这句有没有选边"],
             "3 分钟", "示范：I would argue that education matters more than personal connections.")

s = D.slide()
y = D.header(s, "Part 2 小结：前 60 秒该做的事", "PART 2 · 收")
steps = [("① 读教授问题", "问什么？几个选项？"),
         ("② 读两位同学", "各站哪边？各给了什么理由？"),
         ("③ 选边", "写一句立场句，含比较"),
         ("④ 留一个空", "等会儿要回应谁——先想好")]
x = ML
w = (CW - 0.45) / 4
for ttl, sub in steps:
    D.rect(s, x, y + 0.5, w, 2.1, fill=TEAL_TINT, line=LINE, rounded=True)
    tt = D.tb(s, x + 0.24, y + 0.78, w - 0.48, 0.6)
    D.p(tt, ttl, size=21, bold=True, color=TEAL, space_after=10, line_spacing=1.1)
    tt = D.tb(s, x + 0.24, y + 1.55, w - 0.48, 0.9)
    D.p(tt, sub, size=BODY, color=INK, space_after=0, line_spacing=1.15)
    x += w + 0.15
D.rect(s, ML, y + 3.0, CW, 1.0, fill=ACCENT, line=None, rounded=True)
tt = D.tb(s, ML + 0.42, y + 3.25, CW - 0.85, 0.6)
D.p(tt, "接下来：同一道题，三份不同水平的回答。你来给分。", size=23, bold=True, color=WHITE, space_after=0)
D.notes(s, "Part 2 结束应该在第 30 分钟左右。落后就砍掉'三个陷阱'那一页的讨论。")


# ============================================================================
# PART 3 · 官方题目的 3 / 4 / 5 分示范（25 分钟）
# ============================================================================
SAMPLE_NOTE = "Teacher-created sample based on ETS rubric｜依据 ETS 评分标准编写的教学模拟范文"

def sample_slide(title, kicker, paras, sizes=None, top_gap=0.08):
    s = D.slide()
    y = D.header(s, title, kicker)
    sizes = sizes or [21] * len(paras)
    D.rect(s, ML, y + top_gap, CW, 6.28 - y - top_gap, fill=WHITE, line=TEAL, lw=1.6, rounded=True)
    tt = D.tb(s, ML + 0.45, y + top_gap + 0.3, CW - 0.9, 6.0 - y)
    for para, sz in zip(paras, sizes):
        D.p(tt, para, size=sz, color=INK, space_after=10, line_spacing=1.24)
    tn = D.tb(s, ML, 6.44, CW, 0.4)
    D.p(tn, SAMPLE_NOTE, size=19, color=GREY, space_after=0)
    return s


def score_task_slide(label, focus):
    s = D.slide()
    y = D.header(s, f"{label} · 你来圈，你来打分", "TASK · 学生输出", color=GOLD)
    D.rect(s, ML, y + 0.05, CW, 0.72, fill=GOLD_PALE, line=None, rounded=True)
    tt = D.tb(s, ML + 0.34, y + 0.22, CW - 0.7, 0.5)
    D.p(tt, "在讲义上圈出五要素，找不到就写「无」。然后写一个分数。", size=BODY, bold=True, color=GOLD, space_after=0)
    yy = y + 1.0
    rows = [("P", "Position 立场", TEAL), ("R", "Reason 理由", TEAL_MID),
            ("W", "Why 解释", ACCENT), ("Ex", "Example 例子", ACCENT), ("C", "Contribution 贡献", GOLD)]
    for code, name, col in rows:
        D.rect(s, ML, yy, CW * 0.62, 0.62, fill=WHITE, line=LINE, rounded=True)
        D.rect(s, ML, yy, 0.72, 0.62, fill=col, line=None, rounded=True)
        tn = D.tb(s, ML, yy + 0.12, 0.72, 0.4)
        D.p(tn, code, size=19, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
        tt = D.tb(s, ML + 0.92, yy + 0.13, 2.6, 0.4)
        D.p(tt, name, size=19, bold=True, color=col, space_after=0)
        D.line(s, ML + 3.7, yy + 0.46, ML + CW * 0.62 - 0.22, yy + 0.46, LINE, 1.0)
        yy += 0.72
    bx = ML + CW * 0.66
    bw = CW - CW * 0.66
    D.rect(s, bx, y + 1.0, bw, 1.5, fill=ACCENT_PALE, line=None, rounded=True)
    tt = D.tb(s, bx + 0.3, y + 1.22, bw - 0.6, 0.5)
    D.p(tt, "我给这篇", size=BODY, bold=True, color=ACCENT, space_after=6)
    tt = D.tb(s, bx + 0.3, y + 1.72, bw - 0.6, 0.6)
    D.p(tt, "________  分", size=26, bold=True, color=ACCENT, space_after=0)
    D.rect(s, bx, y + 2.65, bw, 2.42, fill=WHITE, line=LINE, rounded=True)
    tt = D.tb(s, bx + 0.3, y + 2.87, bw - 0.6, 2.0)
    D.p(tt, "打分之前先看：", size=19, bold=True, color=TEAL, space_after=8)
    D.p(tt, focus, size=19, color=INK, space_after=0, line_spacing=1.2)
    return s


def verdict_slide(label, score, headline, haves, lacks, color):
    s = D.slide()
    y = D.header(s, f"{label} · 讲评", f"约 {score} 分", color=color)
    hh = est_h(headline, 22, CW - 0.85, 1.14)
    bar = max(0.80, hh + 0.36)
    D.rect(s, ML, y + 0.02, CW, bar, fill=color, line=None, rounded=True)
    tt = D.tb(s, ML + 0.4, y + 0.02 + (bar - hh) / 2, CW - 0.85, hh)
    D.p(tt, headline, size=22, bold=True, color=WHITE, space_after=0, line_spacing=1.14)
    yy = y + 0.02 + bar + 0.16
    inner = CW / 2 - 0.95
    panels = [("它已经做到的", haves, GREEN, GREEN_PALE, "√", ML),
              ("它缺的东西（丢分点）", lacks, ACCENT, ACCENT_PALE, "×", ML + CW / 2 + 0.15)]
    hs = []
    for _, items, _, _, _, _ in panels:
        hs.append(0.64 + sum(max(0.44, est_h(it, 19, inner, 1.14)) + 0.14 for it in items) + 0.10)
    hmax = max(hs)
    for ttl, items, col, bg, mark, x in panels:
        D.rect(s, x, yy, CW / 2 - 0.15, hmax, fill=bg, line=None, rounded=True)
        tt = D.tb(s, x + 0.32, yy + 0.2, CW / 2 - 0.8, 0.4)
        D.p(tt, ttl, size=20, bold=True, color=col, space_after=0)
        ty = yy + 0.68
        for it in items:
            ih = max(0.44, est_h(it, 19, inner, 1.14))
            tt = D.tb(s, x + 0.32, ty, CW / 2 - 0.8, ih)
            D.rich(tt, [(mark + "  ", {"bold": True, "color": col, "size": 19}), (it, {"size": 19})],
                   space_after=0, line_spacing=1.14)
            ty += ih + 0.14
    return s


D.part = "Part 3 · 3/4/5 分"
D.section("3 / 4 / 5 分示范", "同一道题，三份不同水平的回答", 25,
          "不背范文，只看差距：把三篇放在一起，你会自己看出 WHY 和 Example 值多少分。",
          ["圈五要素", "自己打分", "对照讲评"], "PART 3")

s = D.slide()
y = D.header(s, "先说清楚这三篇是什么", "重要声明")
D.rect(s, ML, y + 0.1, CW, 1.7, fill=ACCENT_PALE, line=ACCENT, lw=1.6, rounded=True)
tt = D.tb(s, ML + 0.42, y + 0.38, CW - 0.85, 1.3)
D.p(tt, "Teacher-created sample based on ETS rubric", size=23, bold=True, color=ACCENT, space_after=10)
D.p(tt, "这三篇是老师依据 ETS Academic Discussion 评分标准写的教学模拟范文，不是 ETS 官方已经评分的真实考生作文。",
    size=BODY, color=INK, space_after=0, line_spacing=1.2)
yy = y + 2.1
for k, v in [("为什么还要看它？", "因为它们控制了变量——同一道题、长度接近，差别只在展开质量。"),
             ("那官方的东西在哪里？", "官方题目原文、官方指令、官方对 contribution 的说明，本课全部逐字引用。"),
             ("你该怎么用？", "不要背句子。只记住：从 A 到 C，每一步多加了什么。")]:
    D.rect(s, ML, yy, CW, 0.98, fill=WHITE, line=LINE, rounded=True)
    tt = D.tb(s, ML + 0.32, yy + 0.24, 3.5, 0.5)
    D.p(tt, k, size=BODY, bold=True, color=TEAL, space_after=0)
    tt = D.tb(s, ML + 3.95, yy + 0.24, CW - 4.3, 0.5)
    D.p(tt, v, size=19, color=INK, space_after=0)
    yy += 1.1
D.notes(s, "这页不能跳。学生一旦以为是官方范文，就会去背。")

s = D.slide()
y = D.header(s, "圈画符号：五个要素", "MARKING CODE")
rows = [("P", "Position", "我站哪边", "圈出那一句", TEAL),
        ("R", "Reason", "为什么这么认为", "画横线", TEAL_MID),
        ("W", "Why", "为什么这个理由成立 / 它是怎么发生的", "画波浪线", ACCENT),
        ("Ex", "Example", "谁 + 做什么 + 结果", "打方框", ACCENT),
        ("C", "Contribution", "对同学的观点加了什么新信息", "标星号", GOLD)]
yy = y + 0.18
for code, en, cn, how, col in rows:
    D.rect(s, ML, yy, CW, 0.86, fill=WHITE, line=LINE, rounded=True)
    D.rect(s, ML, yy, 0.86, 0.86, fill=col, line=None, rounded=True)
    tn = D.tb(s, ML, yy + 0.22, 0.86, 0.45)
    D.p(tn, code, size=22, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
    tt = D.tb(s, ML + 1.1, yy + 0.24, 2.2, 0.45)
    D.p(tt, en, size=20, bold=True, color=col, space_after=0)
    tt = D.tb(s, ML + 3.4, yy + 0.25, CW - 6.0, 0.45)
    D.p(tt, cn, size=19, color=INK, space_after=0)
    tt = D.tb(s, ML + CW - 2.4, yy + 0.25, 2.2, 0.45)
    D.p(tt, how, size=19, color=GREY, space_after=0)
    yy += 0.96
D.notes(s, "五个符号今天会用四次（A/B/C + 自己的作文）。让学生写在讲义封面上。")

s = D.slide()
y = D.header(s, "官方到底在看什么", "WHAT THE SCORE LOOKS AT")
D.rect(s, ML, y + 0.02, CW, 1.42, fill=WHITE, line=TEAL, lw=1.6, rounded=True)
tt = D.tb(s, ML + 0.42, y + 0.22, CW - 0.85, 1.1)
D.p(tt, "“A well-developed response will contain clearly appropriate reasons, examples, and details — ones that do a good job supporting or illustrating your own viewpoint.”",
    size=19, bold=True, color=TEAL, space_after=6, line_spacing=1.16)
D.p(tt, "— ETS, TOEFL iBT Writing Practice Set 2 · Response Tips", size=19, color=GREY, space_after=0)
yy = y + 1.62
四 = [("① 有没有自己的观点", "而且是能被支持的观点，不是常识", TEAL),
      ("② 有没有真正的展开", "reasons / examples / details 三样都要有", ACCENT),
      ("③ 有没有对讨论的贡献", "不是重复别人说过的话", GOLD),
      ("④ 句子和词准不准", "官方原文：语言的质量与准确度同样计入分数", GREEN)]
for k, v, col in 四:
    D.rect(s, ML, yy, CW, 0.82, fill=WHITE, line=LINE, rounded=True)
    D.rect(s, ML, yy, 0.06, 0.82, fill=col, line=None)
    tt = D.tb(s, ML + 0.34, yy + 0.20, 4.4, 0.45)
    D.p(tt, k, size=20, bold=True, color=col, space_after=0)
    tt = D.tb(s, ML + 4.95, yy + 0.20, CW - 5.3, 0.45)
    D.p(tt, v, size=19, color=INK, space_after=0)
    yy += 0.92
D.notes(s, "④ 常被忽略：官方明确写了语言准确度计入分数，所以低级错误确实会扣分。")

sample_slide("Response A", "SAMPLE · 先不给分数", [RESP_A], sizes=[22])
D.notes(D.prs.slides[-1], "让学生默读 40 秒，不许说话。")
score_task_slide("Response A", "① 有没有一句真正解释 WHY？\n② 例子里有没有一个具体的人？\n③ 提到 Andrew 之后，有没有加新东西？")
verdict_slide("Response A", 3, "它回答了问题，也选了边——但它整篇都在换词重复同一个意思。",
              ["有明确立场：I agree with Kelly", "提到了 Andrew，知道要回应讨论", "字数接近 100 词，句子基本正确"],
              ["Reason 全是空词：useful / good / many things",
               "没有一句 WHY——没解释教育「怎么」帮到人",
               "没有具体例子：没有人、没有场景、没有结果",
               "回应 Andrew 只是重申立场，没有新信息"], ACCENT)

s = D.slide()
y = D.header(s, "Response A 的病根：三个空词", "DIAGNOSIS")
pairs = [("Education is very useful for people.", "空词。谁？在什么事情上有用？"),
         ("They can learn many things.", "空词。学到什么？学了以后能做什么？"),
         ("A good job can make their life better.", "空词。怎么变好？变好在哪里？")]
yy = y + 0.2
for bad, cmt in pairs:
    D.rect(s, ML, yy, CW, 1.18, fill=WHITE, line=LINE, rounded=True)
    D.rect(s, ML, yy, 0.06, 1.18, fill=ACCENT, line=None)
    tt = D.tb(s, ML + 0.34, yy + 0.18, CW - 0.7, 0.45)
    D.p(tt, bad, size=21, bold=True, color=INK, space_after=0)
    tt = D.tb(s, ML + 0.34, yy + 0.68, CW - 0.7, 0.42)
    D.p(tt, cmt, size=19, color=ACCENT, space_after=0)
    yy += 1.3
D.rect(s, ML, yy + 0.05, CW, 0.92, fill=TEAL, line=None, rounded=True)
tt = D.tb(s, ML + 0.42, yy + 0.27, CW - 0.85, 0.55)
D.p(tt, "一个判断标准：这句话换成任何一个话题，是不是照样成立？成立 = 空词。", size=21, bold=True, color=WHITE, space_after=0)
D.notes(s, "现场演示：把 Education 换成 Sports，句子照样通顺——说明这句什么都没说。")

sample_slide("Response B", "SAMPLE · 先不给分数", [RESP_B], sizes=[21])
score_task_slide("Response B", "① Reason 具体了吗？具体在哪个词上？\n② 例子里的那个人是谁？她做了什么？\n③ 例子后面有没有写「结果」？")
verdict_slide("Response B", 4, "理由具体了，也有真例子——但链条到例子就停了。",
              ["Reason 具体：skills that employers can actually check",
               "有 WHY：a degree shows real training, so a company is willing to interview",
               "有真例子：a student from a small town / a nursing program / a city hospital",
               "回应了 Andrew，并做了区分（connections 帮的是已经有资格的人）"],
              ["例子后面缺一句 RESULT——这件事最后带来什么？",
               "Contribution 偏「让步 + 重申立场」，新角度还不够明显",
               "立场比较平，没有处理「两者其实相关」这层"], TEAL_MID)

sample_slide("Response C（上半）", "SAMPLE · 先不给分数", [RESP_C1], sizes=[22])
sample_slide("Response C（下半）", "SAMPLE · 先不给分数", [RESP_C2], sizes=[22])
score_task_slide("Response C", "① 立场句里那个 although 起什么作用？\n② 例子里出现了几个动作？\n③ 最后一句给讨论加了什么 Kelly 和 Andrew 都没说过的东西？")
verdict_slide("Response C", 5, "同一个理由被推到了底：具体 → 解释 → 例子 → 结果 → 新角度。",
              ["立场有条件，不是非黑即白",
               "理由更深：不必先有人脉就能挣到",
               "WHY 说清了：普通家庭没人可介绍",
               "例子有动作链：finish → pass → hired",
               "有 RESULT，也有全新角度"],
              ["还可以再补一句对 Kelly 的回应",
               "时间紧时可省，但 RESULT 不能省"], GREEN)

s = D.slide()
y = D.header(s, "揭晓：3 / 4 / 5", "SCORES")
data = [("Response A", "≈ 3 分", ACCENT, ["立场有", "理由空", "无 WHY", "无例子", "回应=重复"]),
        ("Response B", "≈ 4 分", TEAL_MID, ["立场有", "理由具体", "有 WHY", "有例子", "缺 RESULT"]),
        ("Response C", "≈ 5 分", GREEN, ["立场有条件", "理由更深", "有 WHY", "例子有动作链", "有 RESULT + 新角度"])]
x = ML
w = (CW - 0.4) / 3
for name, sc, col, feats in data:
    D.rect(s, x, y + 0.2, w, 4.05, fill=WHITE, line=col, lw=2.0, rounded=True)
    D.rect(s, x, y + 0.2, w, 0.95, fill=col, line=None, rounded=True)
    D.rect(s, x, y + 0.75, w, 0.4, fill=col, line=None)
    tt = D.tb(s, x, y + 0.34, w, 0.6)
    D.p(tt, name, size=20, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
    tt = D.tb(s, x, y + 1.3, w, 0.6)
    D.p(tt, sc, size=32, bold=True, color=col, align=PP_ALIGN.CENTER, space_after=0)
    ty = y + 2.1
    for f in feats:
        tt = D.tb(s, x + 0.22, ty, w - 0.44, 0.4)
        D.p(tt, f, size=19, color=INK, align=PP_ALIGN.CENTER, space_after=0)
        ty += 0.4
    x += w + 0.2
D.notes(s, "问一句：你刚才给 B 打了几分？打 5 分的人举手——然后讲下一页。")

s = D.slide()
y = D.header(s, "3 → 4 到底变了什么", "THE JUMP · 一次只变一件事")
rows = [("理由", "Education is very useful for people.",
         "Education gives people skills that employers can actually check."),
        ("解释", "（没有）",
         "A degree shows that a person has completed real training, so a company is willing to interview them."),
        ("例子", "They can learn many things.",
         "A student from a small town who finishes a nursing program can apply to a city hospital."),
        ("回应", "Andrew says connections are important, but I think education is more important.",
         "Connections usually help people who already have the qualifications.")]
yy = y + 0.12
D.rect(s, ML + 1.55, yy, (CW - 1.65) / 2 - 0.08, 0.44, fill=ACCENT, line=None, rounded=True)
tt = D.tb(s, ML + 1.55, yy + 0.06, (CW - 1.65) / 2 - 0.08, 0.4)
D.p(tt, "Response A（3 分）", size=19, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
D.rect(s, ML + 1.65 + (CW - 1.65) / 2, yy, (CW - 1.65) / 2, 0.44, fill=TEAL_MID, line=None, rounded=True)
tt = D.tb(s, ML + 1.65 + (CW - 1.65) / 2, yy + 0.06, (CW - 1.65) / 2, 0.4)
D.p(tt, "Response B（4 分）", size=19, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
yy += 0.56
for k, a, b in rows:
    h = 1.0
    D.rect(s, ML, yy, CW, h, fill=WHITE, line=LINE, rounded=True)
    tt = D.tb(s, ML + 0.22, yy + 0.3, 1.3, 0.45)
    D.p(tt, k, size=20, bold=True, color=TEAL, space_after=0)
    tt = D.tb(s, ML + 1.62, yy + 0.16, (CW - 1.65) / 2 - 0.2, 0.8)
    D.p(tt, a, size=19, color=GREY, space_after=0, line_spacing=1.1)
    tt = D.tb(s, ML + 1.75 + (CW - 1.65) / 2, yy + 0.16, (CW - 1.65) / 2 - 0.2, 0.8)
    D.p(tt, b, size=19, color=INK, space_after=0, line_spacing=1.1)
    yy += 1.08
D.notes(s, "重点：4 分不是词更难，是信息更多。")

s = D.slide()
y = D.header(s, "4 → 5 到底变了什么", "THE JUMP · 更难的那一步")
items = [("① 理由再深一层",
          "B：教育给可验证的技能。 →  C：教育是「不必先有人脉就能自己挣到」的那个优势。"),
         ("② 例子多一个动作链",
          "B：finishes a program → applies。   C：finishes → passes a test → is hired where she knows nobody。"),
         ("③ 补一句 RESULT",
          "As a result, her first job then becomes her first network."),
         ("④ Contribution 给出新角度",
          "education is what gets a person into the room where connections are formed.")]
yy = y + 0.15
for k, v in items:
    D.rect(s, ML, yy, CW, 1.08, fill=GREEN_PALE if k.startswith("④") else WHITE, line=LINE, rounded=True)
    D.rect(s, ML, yy, 0.06, 1.08, fill=GREEN, line=None)
    tt = D.tb(s, ML + 0.34, yy + 0.13, CW - 0.7, 0.45)
    D.p(tt, k, size=20, bold=True, color=GREEN, space_after=0)
    tt = D.tb(s, ML + 0.34, yy + 0.60, CW - 0.7, 0.45)
    D.p(tt, v, size=19, color=INK, space_after=0, line_spacing=1.12)
    yy += 1.2
D.notes(s, "④ 是今天 Part 5 的预告：contribution 决定 4 和 5。")

s = D.slide()
y = D.header(s, "同一个想法的三个版本", "ONE IDEA · THREE LEVELS")
levels = [("3 分", "Education is useful for people.", ACCENT, "换成任何话题都成立"),
          ("4 分", "Education gives people skills that employers can actually check.", TEAL_MID, "有了具体内容"),
          ("5 分", "Education is the one advantage a person can build without already belonging to a network.",
           GREEN, "回应了这道题的争议点")]
yy = y + 0.18
for sc, txt, col, cmt in levels:
    D.rect(s, ML, yy, CW, 1.42, fill=WHITE, line=col, lw=2.0, rounded=True)
    D.rect(s, ML, yy, 1.35, 1.42, fill=col, line=None, rounded=True)
    tn = D.tb(s, ML, yy + 0.48, 1.35, 0.5)
    D.p(tn, sc, size=22, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
    tt = D.tb(s, ML + 1.62, yy + 0.18, CW - 2.0, 0.7)
    D.p(tt, txt, size=20, bold=True, color=INK, space_after=6, line_spacing=1.12)
    tt2 = D.tb(s, ML + 1.62, yy + 0.98, CW - 2.0, 0.4)
    D.p(tt2, cmt, size=19, color=col, space_after=0)
    yy += 1.54
D.notes(s, "让学生指出：从第二行到第三行，多了哪个词？（network / belonging）")

s = D.slide()
y = D.header(s, "官方自己怎么说「贡献」", "ETS OFFICIAL · Response Tips")
D.rect(s, ML, y + 0.1, CW, 1.9, fill=WHITE, line=TEAL, lw=1.6, rounded=True)
tt = D.tb(s, ML + 0.45, y + 0.38, CW - 0.9, 1.4)
D.p(tt, "“Be sure to add your own perspective to the discussion, not merely repeat ideas that have already been stated.”",
    size=22, bold=True, color=TEAL, space_after=10, line_spacing=1.2)
D.p(tt, "— ETS, TOEFL iBT Writing Practice Set 2（Academic Discussion）Response Tips", size=19, color=GREY, space_after=0)
D.rect(s, ML, y + 2.3, CW, 1.85, fill=ACCENT_PALE, line=None, rounded=True)
tt = D.tb(s, ML + 0.42, y + 2.55, CW - 0.85, 1.4)
D.p(tt, "翻译成人话：", size=20, bold=True, color=ACCENT, space_after=8)
D.p(tt, "把同学说过的话换个词再说一遍 = 0 分贡献。读完你这句，讨论里必须多出一个新信息。",
    size=21, bold=True, color=INK, space_after=6, line_spacing=1.15)
D.p(tt, "Response A 失败在这里；Response C 拿分也在这里。", size=19, color=GREY, space_after=0)
D.notes(s, "这句官方原话贴在教室墙上都不过分。Part 5 会整段练。")

output_slide("把 3 分句升级成 4 分句", "OUTPUT · 每人一句", "拿 Response A 里的这句：Education is very useful for people.",
             ["第一步：把 useful 换掉，写出教育到底给了什么（不许用 good / important / useful）",
              "第二步：加一句 This matters because …",
              "写完两句就停，不要写例子——例子是 Part 4 的事"],
             "4 分钟", "老师会随机抽两条投影出来一起改。")

s = D.slide()
y = D.header(s, "Part 3 小结：分数差在哪里", "PART 3 · 收")
D.rect(s, ML, y + 0.3, CW, 1.25, fill=TEAL, line=None, rounded=True)
tt = D.tb(s, ML + 0.45, y + 0.58, CW - 0.9, 0.8)
D.p(tt, "3 分和 5 分的差距，不在词汇难度，在同一个理由被推了几层。", size=25, bold=True,
    color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
layers = ["Reason 具体", "+ WHY", "+ Example", "+ Result", "+ Contribution"]
x = ML
w = (CW - 4 * 0.16) / 5
for i, l in enumerate(layers):
    col = [ACCENT, ACCENT, TEAL_MID, TEAL_MID, GOLD][i]
    D.rect(s, x, y + 2.0, w, 1.0, fill=WHITE, line=col, lw=2.0, rounded=True)
    tt = D.tb(s, x + 0.1, y + 2.32, w - 0.2, 0.5)
    D.p(tt, l, size=19, bold=True, color=col, align=PP_ALIGN.CENTER, space_after=0)
    x += w + 0.16
D.rect(s, ML, y + 3.3, CW, 0.95, fill=ACCENT_PALE, line=None, rounded=True)
tt = D.tb(s, ML + 0.42, y + 3.54, CW - 0.85, 0.55)
D.p(tt, "接下来 30 分钟：把这条链条，一层一层练出来。", size=23, bold=True, color=ACCENT, space_after=0)
D.notes(s, "Part 3 应在第 55 分钟结束。")


# ============================================================================
# PART 4 · 高分展开训练（30 分钟）
# ============================================================================
def bad_good_strip(s, x, y, w, bad, good, label="示范  EXAMPLE"):
    inner = w - 0.98
    hb = max(0.30, est_h(bad, 19, inner, 1.08))
    hg = max(0.30, est_h(good, 19, inner, 1.08))
    h = 0.34 + hb + hg + 0.10
    D.rect(s, x, y, w, h, fill=GREEN_PALE, line=None, rounded=True)
    D.rect(s, x, y, 0.07, h, fill=GREEN, line=None)
    tt = D.tb(s, x + 0.3, y + 0.05, 2.6, 0.30)
    D.p(tt, label, size=LABEL, bold=True, color=GREEN, space_after=0)
    tt = D.tb(s, x + 0.3, y + 0.33, w - 0.6, hb)
    D.rich(tt, [("×  ", {"bold": True, "color": ACCENT, "size": 19}),
                (bad, {"size": 19, "color": GREY})], space_after=0, line_spacing=1.08)
    tt = D.tb(s, x + 0.3, y + 0.33 + hb, w - 0.6, hg)
    D.rich(tt, [("√  ", {"bold": True, "color": GREEN, "size": 19}),
                (good, {"size": 19, "bold": True, "color": INK})], space_after=0, line_spacing=1.08)
    return y + h + 0.14


def drill_slide(title, kicker, level, instruction, demo, items, lines=1, level_color=ACCENT):
    """items: list of (prompt, hint)"""
    s = D.slide()
    y = D.header(s, title, kicker)
    tw = D.tag(s, ML, y - 0.02, level, fill=level_color, size=17, h=0.38)
    tt = D.tb(s, ML + tw + 0.24, y + 0.03, CW - tw - 0.3, 0.4)
    D.p(tt, instruction, size=19, bold=True, color=INK, space_after=0)
    yy = y + 0.52
    if demo:
        yy = bad_good_strip(s, ML, yy, CW, demo[0], demo[1])
    for i, (prompt, hint) in enumerate(items):
        yy = ask_row(s, ML, yy, CW, i + 1, prompt, hint, lines=lines)
    return s


D.part = "Part 4 · 展开训练"
D.section("高分展开训练", "把一个理由，写成一整段", 30,
          "不要停在 X is good。三步走：具体理由 → 为什么 → 例子 → 结果。",
          ["基础：补 WHY", "中等：补 Example", "提高：完整链条"], "PART 4")

s = D.slide()
y = D.header(s, "为什么 X is good 永远拿不到分", "THE PROBLEM")
D.rect(s, ML, y + 0.1, CW, 1.15, fill=WHITE, line=ACCENT, lw=2.0, rounded=True)
tt = D.tb(s, ML + 0.45, y + 0.36, CW - 0.9, 0.6)
D.p(tt, "Education is good.   Networking is important.   Part-time jobs are useful.",
    size=23, bold=True, color=GREY, align=PP_ALIGN.CENTER, space_after=0)
yy = y + 1.55
reasons = [("没有信息量", "读完之后，读者对这个话题的了解一点没增加。"),
           ("换个话题照样成立", "把 Education 换成 Sports、Music、Travel——句子还是通顺的。"),
           ("阅卷人无法判断你会不会英语", "因为这句话初中生也写得出来。")]
for k, v in reasons:
    D.rect(s, ML, yy, CW, 1.05, fill=TEAL_TINT, line=LINE, rounded=True)
    tt = D.tb(s, ML + 0.34, yy + 0.16, CW - 0.7, 0.42)
    D.p(tt, k, size=20, bold=True, color=TEAL, space_after=0)
    tt = D.tb(s, ML + 0.34, yy + 0.6, CW - 0.7, 0.4)
    D.p(tt, v, size=19, color=INK, space_after=0)
    yy += 1.16
D.notes(s, "现场做一次替换实验，比讲十遍有用。")

s = D.slide()
y = D.header(s, "三步走：把空句子变成一段话", "THE METHOD")
steps = [("STEP 1", "Specific Reason", "把空词换成具体内容", "It helps ______ develop ______.", ACCENT),
         ("STEP 2", "WHY", "解释为什么 / 怎么发生", "This matters because ______.", TEAL_MID),
         ("STEP 3", "Example + Result", "谁 + 做什么 + 结果", "For example, ______. As a result, ______.", GREEN)]
yy = y + 0.25
for tag, en, cn, pat, col in steps:
    D.rect(s, ML, yy, CW, 1.36, fill=WHITE, line=col, lw=1.8, rounded=True)
    D.rect(s, ML, yy, 1.5, 1.36, fill=col, line=None, rounded=True)
    tn = D.tb(s, ML, yy + 0.46, 1.5, 0.45)
    D.p(tn, tag, size=19, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
    tt = D.tb(s, ML + 1.78, yy + 0.2, 4.2, 0.9)
    D.p(tt, en, size=21, bold=True, color=col, space_after=4)
    D.p(tt, cn, size=19, color=GREY, space_after=0)
    tt = D.tb(s, ML + 6.2, yy + 0.44, CW - 6.5, 0.5)
    D.p(tt, pat, size=19, bold=True, color=INK, space_after=0)
    yy += 1.5
D.notes(s, "这三步今天会重复六次。学生记住 STEP 编号即可。")

s = D.slide()
y = D.header(s, "STEP 1 · 把空词换成具体理由", "WORKED EXAMPLE")
demo_card(s, ML, y + 0.08, CW, [
    ("空句", "Education is useful."),
    ("问自己", "有用在什么事情上？它到底给了人什么？"),
    ("具体版", "Education gives people skills that employers can actually check."),
    ("再深一层", "Education is the one advantage a person can build without already knowing anyone."),
], row_gap=0.58, label_w=1.35)
D.rect(s, ML, y + 3.15, CW, 1.5, fill=TEAL_TINT, line=LINE, rounded=True)
tt = D.tb(s, ML + 0.36, y + 3.38, CW - 0.75, 1.1)
D.p(tt, "可直接套用的四个句型：", size=20, bold=True, color=TEAL, space_after=8)
D.p(tt, "It helps ______ develop ______.    It gives ______ the ______ needed to ______.", size=19, color=INK, space_after=6)
D.p(tt, "It lets ______ do ______ without ______.    It is the one ______ that ______.", size=19, color=INK, space_after=0)
D.notes(s, "第四个句型（It is the one … that …）是 5 分句的常见起手式。")

drill_slide("练习 1 · 把空词换成具体理由", "DRILL 1 · 学生输出", "基础",
            "每题只写一行，句子里不许出现 good / important / useful。",
            ("Networking is helpful.", "Networking helps people hear about jobs before they are advertised."),
            [("Networking helps people ______.", "提示：hear about jobs / before they are advertised"),
             ("A university degree lets a student ______.", "提示：prove real training / to a stranger"),
             ("A part-time job helps a student ______.", "提示：deal with real customers / real money")])
D.notes(D.prs.slides[-1], "限时 4 分钟。走一圈，看到空词直接画圈让他当场改。")

drill_slide("练习 1（续）· 换一个方向", "DRILL 1 · 学生输出", "基础",
            "同样一行。这两句和今天的官方题直接相关。",
            ("A mentor is important.", "A mentor helps a young worker avoid mistakes nobody warns you about."),
            [("Knowing the right people helps someone ______.", "提示：be introduced / be trusted faster"),
             ("A scholarship lets a student ______.", "提示：study without / pay for"),
             ("A professional certificate gives a person ______.", "提示：proof / stranger / hire")])

s = D.slide()
y = D.header(s, "STEP 2 · WHY 的三个提问法", "WORKED EXAMPLE")
qs = [("为什么这件事重要？", "Why does this matter?"),
      ("它到底是怎么发生的？", "How does it actually happen?"),
      ("谁最需要它？", "Who needs it most?")]
x = ML
w = (CW - 0.4) / 3
for cn, en in qs:
    D.rect(s, x, y + 0.1, w, 1.15, fill=ACCENT_PALE, line=None, rounded=True)
    tt = D.tb(s, x + 0.24, y + 0.3, w - 0.48, 0.8)
    D.p(tt, cn, size=20, bold=True, color=ACCENT, align=PP_ALIGN.CENTER, space_after=6)
    D.p(tt, en, size=19, color=INK, align=PP_ALIGN.CENTER, space_after=0)
    x += w + 0.2
demo_card(s, ML, y + 1.45, CW, [
    ("Reason", "Education gives people skills that employers can actually check."),
    ("WHY ①", "This matters because a company cannot judge a stranger in a ten-minute interview."),
    ("WHY ②", "A certificate is the only proof a stranger will accept."),
], row_gap=0.58, label_w=1.35)
D.rect(s, ML, y + 3.75, CW, 0.78, fill=WHITE, line=ACCENT, lw=1.6, rounded=True)
tt = D.tb(s, ML + 0.36, y + 3.95, CW - 0.75, 0.45)
D.p(tt, "禁止：because it is helpful / because it is good for them —— 这是把理由再说一遍，不是 WHY。",
    size=19, bold=True, color=ACCENT, space_after=0)
D.notes(s, "WHY 是全课最难的一步，示范要慢，念两遍。")

drill_slide("练习 2 · 补一句 WHY", "DRILL 2 · 学生输出", "基础",
            "用 This matters because … 起头，一句话写完。",
            ("Networking helps people hear about jobs early, because it is useful.",
             "This matters because many good jobs are filled before anyone sees the advertisement."),
            [("A degree lets a student prove real training to a stranger.  →  This matters because ______.",
              "提问：招聘的人从没见过你，他凭什么相信你？"),
             ("A part-time job teaches a student how a workplace really runs.  →  This matters because ______.",
              "提问：课堂上学不到的到底是哪一部分？")])

drill_slide("练习 2（续）· 再补两句 WHY", "DRILL 2 · 学生输出", "基础",
            "还是一句话。这两条直接可以用进今天的作文。",
            ("Education is important because education is very useful.",
             "This matters because students from ordinary families have no one to introduce them."),
            [("Knowing the right people helps someone be trusted faster.  →  This matters because ______.",
              "提问：陌生人凭什么信任你？中间人起了什么作用？"),
             ("A certificate gives a person proof that a stranger will accept.  →  This matters because ______.",
              "提问：如果没有这张证书，这个人要花多久才能证明自己？")])

output_slide("读你的 WHY", "OUTPUT · 每人一条", "读出你写的任意一句 This matters because …",
             ["其他人只判断一件事：这句是不是把理由换个词又说了一遍？",
              "如果是——现场改，加入一个新信息（一个人、一个场景、一个障碍）",
              "彭子骞可以只读练习 2 的第 1 题"],
             "4 分钟", "老师把最好的两条抄在白板上，Part 6 写作时可以直接用。")

s = D.slide()
y = D.header(s, "STEP 3 · 例子 = 谁 + 做什么 + 结果", "WORKED EXAMPLE")
D.rect(s, ML, y + 0.08, CW, 1.0, fill=WHITE, line=ACCENT, lw=1.8, rounded=True)
x = ML + 0.4
for lab, cn in [("WHO", "一个具体的人"), ("ACTION", "他做了什么"), ("RESULT", "最后怎么样")]:
    D.rect(s, x, y + 0.24, 3.3, 0.68, fill=ACCENT_PALE, line=None, rounded=True)
    tt = D.tb(s, x, y + 0.36, 3.3, 0.45)
    D.rich(tt, [(lab + "  ", {"bold": True, "color": ACCENT, "size": 19}), (cn, {"size": 19})],
           align=PP_ALIGN.CENTER, space_after=0)
    x += 3.7
demo_card(s, ML, y + 1.28, CW, [
    ("坏例子", "Many people can get a good job after studying."),
    ("问题", "没有人、没有动作、没有结果——等于什么都没说。"),
    ("好例子", "A student from a small town who finishes a nursing program can apply to a city hospital without knowing anyone there."),
    ("加结果", "As a result, her family's situation no longer decides where she can work."),
], row_gap=0.58, label_w=1.35)
D.notes(s, "强调 without knowing anyone there —— 这一句直接回应了 Andrew。")

drill_slide("练习 3 · 补一个例子", "DRILL 3 · 学生输出", "中等",
            "用 For example, a student who … 起头。必须出现一个人和一个动作。",
            ("For example, education can help many people find jobs.",
             "For example, a student who finishes an accounting course can pass a company's test."),
            [("Reason：Education gives people skills employers can check.  →  For example, ______.",
              "关键词：accounting course / entrance test / hired"),
             ("Reason：Networking helps people hear about jobs early.  →  For example, ______.",
              "关键词：her uncle / a small company / before the job was posted")], lines=2)

drill_slide("练习 3（续）· 再补一个例子", "DRILL 3 · 学生输出", "中等",
            "同样要求：一个人 + 一个动作。写两行。",
            ("For example, part-time jobs teach students many useful things.",
             "For example, a student in a café must apologize to a customer whose order is late."),
            [("Reason：A part-time job teaches a student how a workplace really runs.  →  For example, ______.",
              "关键词：café / late order / angry customer / manager"),
             ("Reason：A mentor helps a young worker avoid mistakes.  →  For example, ______.",
              "关键词：first report / her manager / rewrite before sending")], lines=2)

drill_slide("练习 4 · 补一句结果", "DRILL 4 · 学生输出", "中等",
            "用 As a result, … 起头。结果要看得见，不要写 it is very good。",
            ("As a result, it is very good for her future.",
             "As a result, her family's situation no longer decides where she can work."),
            [("……a student passes a company's entrance test and is hired.  →  As a result, ______.",
              "提问：她的人生因此改变了什么？（钱？城市？下一份工作？）"),
             ("……a student hears about a job from her uncle before it is advertised.  →  As a result, ______.",
              "提问：其他求职者晚了多久？她省下了什么？"),
             ("……a student calms down an angry customer at a café.  →  As a result, ______.",
              "提问：这件事让她学会了什么，下次能做什么？")])

output_slide("读一条完整的三句话", "OUTPUT · 每人一条", "Reason → WHY → Example → Result，四句连读。",
             ["读之前先在心里数：我这四句里有几个具体名词？",
              "少于三个 —— 说明还不够具体",
              "同伴只回答一个问题：你听完之后，脑子里有没有出现一个画面？"],
             "5 分钟", "彭子骞读三句即可（Reason + WHY + Example）。")

s = D.slide()
y = D.header(s, "完整链条示范 · 支持 education", "FULL CHAIN · A")
demo_card(s, ML, y + 0.08, CW, [
    ("REASON", "Education is the one advantage a person can build without already knowing anyone."),
    ("WHY", "This matters because students from ordinary families have no one to introduce them."),
    ("EXAMPLE", "For example, a student whose parents are farmers can finish an accounting qualification and pass a company's entrance test."),
    ("RESULT", "As a result, she is hired by a firm where she knows nobody."),
    ("CONTRIBUTION", "Education is usually what gets a person into the room where connections are formed."),
], row_gap=0.60, label_w=1.85, title="老师示范 · 这就是 Part 3 里 Response C 的骨架")
D.notes(s, "把这张和 Response C 并排看：学生会发现范文其实就是这五行。")

s = D.slide()
y = D.header(s, "完整链条示范 · 支持 connections", "FULL CHAIN · B")
demo_card(s, ML, y + 0.08, CW, [
    ("REASON", "Personal connections decide who even hears about an opportunity in the first place."),
    ("WHY", "This matters because most good positions are filled before they are ever advertised."),
    ("EXAMPLE", "For example, a graduate whose neighbour works in a design studio is told about an opening two weeks early."),
    ("RESULT", "As a result, she applies while there are still three candidates instead of three hundred."),
    ("CONTRIBUTION", "A degree gets you considered; a connection gets you considered first."),
], row_gap=0.60, label_w=1.85, title="老师示范 · 作业里如果你想选另一边，用这条", fill=ACCENT_PALE, accent=ACCENT)
D.notes(s, "给作业留出口：不选 education 也能写好，方法一样。")

s = D.slide()
y = D.header(s, "练习 5 · 自己写一条完整链条", "DRILL 5 · 学生输出", color=GOLD)
tw = D.tag(s, ML, y - 0.02, "提高", fill=GOLD, size=17, h=0.38)
tt = D.tb(s, ML + tw + 0.24, y + 0.03, CW - tw - 0.3, 0.4)
D.p(tt, "支持 education。不许照抄示范，Reason 必须换一个。", size=19, bold=True, color=INK, space_after=0)
yy = y + 0.6
for lab, hint in [("REASON", "教育还给了人什么？（时间？选择权？语言？信心？）"),
                  ("WHY", "This matters because ______"),
                  ("EXAMPLE", "For example, a student who ______"),
                  ("RESULT", "As a result, ______")]:
    D.rect(s, ML, yy, 1.85, 0.5, fill=GOLD, line=None, rounded=True)
    tn = D.tb(s, ML, yy + 0.09, 1.85, 0.4)
    D.p(tn, lab, size=19, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
    tt = D.tb(s, ML + 2.05, yy + 0.06, CW - 2.1, 0.4)
    D.p(tt, hint, size=19, color=GREY, space_after=0)
    D.line(s, ML + 2.05, yy + 0.52, ML + CW, yy + 0.52, LINE, 1.0)
    D.line(s, ML + 2.05, yy + 0.94, ML + CW, yy + 0.94, LINE, 1.0)
    yy += 1.18
D.notes(s, "限时 6 分钟。这一条链条 Part 6 直接搬进作文里。")

s = D.slide()
y = D.header(s, "练习 6 · 换到对面去写", "DRILL 6 · 学生输出", color=GOLD)
tw = D.tag(s, ML, y - 0.02, "提高 · 无支架", fill=GOLD, size=17, h=0.38)
tt = D.tb(s, ML + tw + 0.24, y + 0.03, CW - tw - 0.3, 0.4)
D.p(tt, "这次支持 Andrew（connections）。四行，不给句型。", size=19, bold=True, color=INK, space_after=0)
D.rect(s, ML, y + 0.58, CW, 0.86, fill=TEAL_TINT, line=LINE, rounded=True)
tt = D.tb(s, ML + 0.34, y + 0.76, CW - 0.7, 0.55)
D.p(tt, "为什么要练对面？因为考场上你可能拿到一道你并不同意的题——方法必须和立场无关。",
    size=19, bold=True, color=TEAL, space_after=0)
D.writing_lines(s, ML, y + 1.85, CW, 7, gap=0.52)
D.notes(s, "只给 5 分钟，写不完也停。目的是证明流程可迁移。")

s = D.slide()
y = D.header(s, "展开时最常见的 5 个错误", "TOP 5 MISTAKES")
mistakes = [("Reason 里还留着 good / important / useful", "→ 换成一个具体动词短语"),
            ("WHY 只是把 Reason 换个词说一遍", "→ 加一个障碍或一个对比"),
            ("例子里没有人，只有 many students", "→ 改成 a student who …"),
            ("例子写完就结束，没有结果", "→ 补一句 As a result, …"),
            ("三个理由各写两句", "→ 一个理由写六句，分数更高")]
yy = y + 0.15
for bad, fix in mistakes:
    D.rect(s, ML, yy, CW, 0.86, fill=WHITE, line=LINE, rounded=True)
    D.rect(s, ML, yy, 0.06, 0.86, fill=ACCENT, line=None)
    tt = D.tb(s, ML + 0.34, yy + 0.22, CW * 0.55, 0.45)
    D.p(tt, bad, size=19, bold=True, color=INK, space_after=0)
    tt = D.tb(s, ML + CW * 0.58, yy + 0.22, CW * 0.42 - 0.3, 0.45)
    D.p(tt, fix, size=19, color=GREEN, space_after=0)
    yy += 0.96
D.notes(s, "最后一条最反直觉：少写理由，多写展开。")

s = D.slide()
y = D.header(s, "本题专用替换词库", "WORD BANK · social mobility")
pairs = [("good / useful", "valuable · practical · reliable"),
         ("important", "decisive · essential · the key to"),
         ("help", "enable · allow · make it possible for"),
         ("get a job", "be hired · land a position · be offered a role"),
         ("skills", "qualifications · training · credentials"),
         ("know people", "personal connections · a professional network"),
         ("rich / poor family", "an ordinary family · a well-connected family")]
yy = y + 0.1
D.rect(s, ML, yy, CW, 0.5, fill=TEAL, line=None, rounded=True)
tt = D.tb(s, ML + 0.3, yy + 0.09, 4.0, 0.4)
D.p(tt, "空词", size=19, bold=True, color=WHITE, space_after=0)
tt = D.tb(s, ML + 4.6, yy + 0.09, CW - 4.9, 0.4)
D.p(tt, "换成", size=19, bold=True, color=WHITE, space_after=0)
yy += 0.58
for a, b in pairs:
    D.rect(s, ML, yy, CW, 0.56, fill=WHITE, line=LINE, rounded=True)
    tt = D.tb(s, ML + 0.3, yy + 0.12, 4.0, 0.4)
    D.p(tt, a, size=19, color=GREY, space_after=0)
    tt = D.tb(s, ML + 4.6, yy + 0.12, CW - 4.9, 0.4)
    D.p(tt, b, size=19, bold=True, color=INK, space_after=0)
    yy += 0.64
D.notes(s, "让学生在讲义上圈三个今天一定要用的词。")

output_slide("链条展示 · 全班过一遍", "OUTPUT · 4 人各一条",
             "读出你在练习 5 或练习 6 里写的完整链条（Reason → WHY → Example → Result）。",
             ["听的人手上拿笔，只做一件事：数一数这条链条有几层",
              "四层齐了就说「四层」；缺哪一层就直接说缺哪一层",
              "缺 RESULT 的当场补一句，不要等回家改"],
             "5 分钟", "老师记下每个人缺的那一层——Part 6 写作时点名提醒。")

s = D.slide()
y = D.header(s, "Part 4 小结：一个理由，六句话", "PART 4 · 收")
D.rect(s, ML, y + 0.25, CW, 1.3, fill=TEAL, line=None, rounded=True)
tt = D.tb(s, ML + 0.45, y + 0.55, CW - 0.9, 0.8)
D.p(tt, "与其写三个理由各两句，不如写一个理由六句。", size=25, bold=True, color=WHITE,
    align=PP_ALIGN.CENTER, space_after=0)
yy = y + 1.85
for k, v in [("多数 3 分作文", "三个理由 × 两句 = 六句，但每一句都可以换话题使用"),
             ("多数 5 分作文", "一个理由 × 六句，每一句都只能用在这道题上")]:
    D.rect(s, ML, yy, CW, 1.02, fill=TEAL_TINT if k.startswith("多数 3") else GREEN_PALE, line=LINE, rounded=True)
    tt = D.tb(s, ML + 0.34, yy + 0.26, 3.6, 0.45)
    D.p(tt, k, size=20, bold=True, color=GREY if k.startswith("多数 3") else GREEN, space_after=0)
    tt = D.tb(s, ML + 4.1, yy + 0.26, CW - 4.4, 0.45)
    D.p(tt, v, size=19, color=INK, space_after=0)
    yy += 1.14
D.rect(s, ML, yy + 0.06, CW, 0.8, fill=ACCENT_PALE, line=None, rounded=True)
tt = D.tb(s, ML + 0.42, yy + 0.24, CW - 0.85, 0.5)
D.p(tt, "接下来 20 分钟：把这条链条接到 Kelly 和 Andrew 身上。", size=21, bold=True, color=ACCENT, space_after=0)
D.notes(s, "Part 4 应在第 85 分钟结束。")


# ============================================================================
# PART 5 · Contribution 训练（20 分钟）
# ============================================================================
D.part = "Part 5 · Contribution"
D.section("Contribution 训练", "回应同学，而不是重复同学", 20,
          "官方要求 make a contribution … in your own words。这一步直接决定 4 分还是 5 分。",
          ["Agree + Add ×2", "Disagree + Explain ×2"], "PART 5")

s = D.slide()
y = D.header(s, "Contribution 到底是什么", "DEFINITION")
D.rect(s, ML, y + 0.05, CW, 1.35, fill=WHITE, line=TEAL, lw=1.8, rounded=True)
tt = D.tb(s, ML + 0.45, y + 0.28, CW - 0.9, 0.95)
D.p(tt, "Make a contribution to the discussion in your own words.", size=23, bold=True, color=TEAL, space_after=8)
D.p(tt, "— TOEFL iBT 官方指令原文", size=19, color=GREY, space_after=0)
yy = y + 1.7
for k, v, col, bg in [("不是 contribution", "把 Kelly 或 Andrew 说过的话，换几个词再说一遍。", ACCENT, ACCENT_PALE),
                      ("是 contribution", "读完你这一句，讨论里多出了一个之前没有的信息。", GREEN, GREEN_PALE)]:
    D.rect(s, ML, yy, CW, 1.12, fill=bg, line=None, rounded=True)
    D.rect(s, ML, yy, 0.07, 1.12, fill=col, line=None)
    tt = D.tb(s, ML + 0.36, yy + 0.2, CW - 0.75, 0.45)
    D.p(tt, k, size=21, bold=True, color=col, space_after=4)
    tt = D.tb(s, ML + 0.36, yy + 0.66, CW - 0.75, 0.4)
    D.p(tt, v, size=19, color=INK, space_after=0)
    yy += 1.28
D.notes(s, "回到 Part 3 的官方 Response Tips 那一页对照。")

s = D.slide()
y = D.header(s, "一个判断标准", "THE TEST")
D.rect(s, ML, y + 0.15, CW, 1.25, fill=TEAL, line=None, rounded=True)
tt = D.tb(s, ML + 0.45, y + 0.42, CW - 0.9, 0.7)
D.p(tt, "把你这一句删掉，这场讨论会少掉什么？", size=27, bold=True, color=WHITE,
    align=PP_ALIGN.CENTER, space_after=0)
yy = y + 1.75
for a, b, col in [("答案是「什么都不少」", "→ 这是重复，0 分贡献", ACCENT),
                  ("答案是「少了一个具体的人 / 一个新原因 / 一个新角度」", "→ 这是贡献", GREEN)]:
    D.rect(s, ML, yy, CW, 1.05, fill=WHITE, line=col, lw=1.8, rounded=True)
    tt = D.tb(s, ML + 0.36, yy + 0.28, CW * 0.62, 0.45)
    D.p(tt, a, size=20, bold=True, color=INK, space_after=0)
    tt = D.tb(s, ML + CW * 0.66, yy + 0.28, CW * 0.34 - 0.3, 0.45)
    D.p(tt, b, size=20, bold=True, color=col, space_after=0)
    yy += 1.2
D.notes(s, "让学生把自己 Part 2 写的立场句拿出来，用这个标准测一遍。")

s = D.slide()
y = D.header(s, "重复 vs 贡献 · 三组对照", "COMPARE")
rows = [("Kelly 说：education gives knowledge and skills.",
         "I agree that education gives knowledge and skills.",
         "I agree with Kelly, and I would add that a certificate is the only proof a stranger will accept."),
        ("Andrew 说：knowing the right people opens doors.",
         "Andrew is right that connections open doors.",
         "Andrew is right that connections open doors, but someone has to be qualified before that door is worth opening."),
        ("Kelly 说：education is a foundation for success.",
         "Education is really the foundation of success.",
         "Education also decides who a person meets, because classmates become the first professional network.")]
yy = y + 0.08
D.rect(s, ML, yy, CW * 0.30, 0.44, fill=TEAL, line=None, rounded=True)
tt = D.tb(s, ML + 0.14, yy + 0.06, CW * 0.30, 0.4)
D.p(tt, "同学说了什么", size=19, bold=True, color=WHITE, space_after=0)
D.rect(s, ML + CW * 0.31, yy, CW * 0.30, 0.44, fill=ACCENT, line=None, rounded=True)
tt = D.tb(s, ML + CW * 0.31 + 0.14, yy + 0.06, CW * 0.30, 0.4)
D.p(tt, "× 重复", size=19, bold=True, color=WHITE, space_after=0)
D.rect(s, ML + CW * 0.62, yy, CW * 0.38, 0.44, fill=GREEN, line=None, rounded=True)
tt = D.tb(s, ML + CW * 0.62 + 0.14, yy + 0.06, CW * 0.38, 0.4)
D.p(tt, "√ 贡献", size=19, bold=True, color=WHITE, space_after=0)
yy += 0.52
for said, bad, good in rows:
    h = 1.36
    D.rect(s, ML, yy, CW, h, fill=WHITE, line=LINE, rounded=True)
    tt = D.tb(s, ML + 0.14, yy + 0.16, CW * 0.29, 1.1)
    D.p(tt, said, size=19, color=GREY, space_after=0, line_spacing=1.1)
    tt = D.tb(s, ML + CW * 0.31 + 0.14, yy + 0.16, CW * 0.29, 1.1)
    D.p(tt, bad, size=19, color=ACCENT, space_after=0, line_spacing=1.1)
    tt = D.tb(s, ML + CW * 0.62 + 0.14, yy + 0.16, CW * 0.37, 1.1)
    D.p(tt, good, size=19, bold=True, color=INK, space_after=0, line_spacing=1.1)
    yy += h + 0.08
D.notes(s, "第三组最值得讲：它把 Kelly 的话接到了 Andrew 的领域里，这是最漂亮的贡献方式。")

s = D.slide()
y = D.header(s, "模板 1 · Agree + Add", "TEMPLATE")
D.rect(s, ML, y + 0.1, CW, 1.5, fill=GREEN_PALE, line=None, rounded=True)
tt = D.tb(s, ML + 0.45, y + 0.36, CW - 0.9, 1.1)
D.p(tt, "I agree with ______ that ______.", size=25, bold=True, color=GREEN, space_after=8)
D.p(tt, "I would also add that ______ because ______.", size=25, bold=True, color=GREEN, space_after=0)
yy = y + 1.85
for k, v in [("第一句", "先说清楚你同意他哪一点——只写一句，不要复述整段。"),
             ("第二句", "加一个他没说过的东西：一个新原因、一个具体的人、一个反面情况。"),
             ("最后半句", "because 后面必须解释，否则这个 add 还是空的。")]:
    D.rect(s, ML, yy, CW, 0.92, fill=WHITE, line=LINE, rounded=True)
    tt = D.tb(s, ML + 0.32, yy + 0.24, 2.2, 0.45)
    D.p(tt, k, size=20, bold=True, color=GREEN, space_after=0)
    tt = D.tb(s, ML + 2.7, yy + 0.24, CW - 3.05, 0.45)
    D.p(tt, v, size=19, color=INK, space_after=0)
    yy += 1.02
D.notes(s, "强调：I agree with Kelly. 之后如果直接换话题，也不算贡献。")

s = D.slide()
y = D.header(s, "Agree + Add 示范", "WORKED EXAMPLE")
yq = quote_bar(s, ML, y + 0.05, CW, "Kelly 原话",
               "“… education provides a foundation for long-term success and upward mobility.”",
               color=TEAL_MID, fill=TEAL_TINT, note="节选")
demo_card(s, ML, yq + 0.08, CW, [
    ("Agree", "I agree with Kelly that education provides a foundation for long-term success."),
    ("Add", "I would also add that education is the only advantage a student can build alone,"),
    ("Because", "because nobody can choose the family they are born into."),
], row_gap=0.58, label_w=1.35, title="老师示范 · 新信息在哪一句？")
D.rect(s, ML, yq + 2.52, CW, 0.66, fill=ACCENT_PALE, line=None, rounded=True)
tt = D.tb(s, ML + 0.34, yq + 2.71, CW - 0.7, 0.4)
D.p(tt, "新信息 = 「不能选择出身」。Kelly 全段都没提过这一点。", size=19, bold=True, color=ACCENT, space_after=0)
D.notes(s, "让学生指出新信息，别自己说。")

drill_slide("练习 A1 · Agree + Add（回应 Kelly）", "DRILL · 学生输出", "Agree + Add",
            "两句话。第二句必须出现 Kelly 没说过的信息。",
            ("I agree with Kelly that education is very important for people.",
             "I agree with Kelly that education opens job opportunities. I would also add that it decides who a student meets every day, because classmates become the first professional network."),
            [("I agree with Kelly that ______. I would also add that ______ because ______.",
              "可用新角度：同学就是第一批人脉 / 教育让人敢开口 / 教育给的是第二次机会")], lines=3)

drill_slide("练习 A2 · Agree + Add（回应 Andrew）", "DRILL · 学生输出", "Agree + Add",
            "这次同意 Andrew。注意：同意他，不等于放弃你的立场。",
            ("I agree with Andrew because connections are also useful.",
             "I agree with Andrew that connections open doors. I would also add that they mostly work for people who already have something to show, because a friend can recommend you but cannot do the job for you."),
            [("I agree with Andrew that ______. I would also add that ______ because ______.",
              "可用新角度：人脉决定谁先听到消息 / 人脉救不了没准备的人 / 人脉本身也来自学校")], lines=3)

s = D.slide()
y = D.header(s, "模板 2 · Disagree + Explain", "TEMPLATE")
D.rect(s, ML, y + 0.1, CW, 1.5, fill=ACCENT_PALE, line=None, rounded=True)
tt = D.tb(s, ML + 0.45, y + 0.36, CW - 0.9, 1.1)
D.p(tt, "Although ______ argues that ______,", size=25, bold=True, color=ACCENT, space_after=8)
D.p(tt, "I believe ______ because ______.", size=25, bold=True, color=ACCENT, space_after=0)
yy = y + 1.85
for k, v in [("先承认", "Although 后面必须准确复述对方的观点——不能歪曲。"),
             ("再反驳", "I believe 后面写你的立场，必须和对方形成真正的对立。"),
             ("礼貌", "官方明确写：disagree in a respectful way。不要写 Andrew is wrong。")]:
    D.rect(s, ML, yy, CW, 0.92, fill=WHITE, line=LINE, rounded=True)
    tt = D.tb(s, ML + 0.32, yy + 0.24, 2.2, 0.45)
    D.p(tt, k, size=20, bold=True, color=ACCENT, space_after=0)
    tt = D.tb(s, ML + 2.7, yy + 0.24, CW - 3.05, 0.45)
    D.p(tt, v, size=19, color=INK, space_after=0)
    yy += 1.02
D.notes(s, "礼貌那一条来自 ETS 官方 Response Tips，可以直接告诉学生这是官方要求。")

s = D.slide()
y = D.header(s, "Disagree + Explain 示范", "WORKED EXAMPLE")
yq = quote_bar(s, ML, y + 0.05, CW, "Andrew 原话",
               "“Knowing the right people can open doors to opportunities that education alone might not provide.”",
               color=ACCENT, fill=ACCENT_PALE, note="节选")
demo_card(s, ML, yq + 0.08, CW, [
    ("Although", "Although Andrew argues that personal connections are more crucial,"),
    ("I believe", "I believe education matters more,"),
    ("Because", "because connections usually help people who already have the qualifications."),
], row_gap=0.58, label_w=1.55, title="老师示范 · 这一句为什么有力？", fill=TEAL_TINT, accent=TEAL)
D.rect(s, ML, yq + 2.52, CW, 0.66, fill=TEAL_PALE, line=None, rounded=True)
tt = D.tb(s, ML + 0.34, yq + 2.71, CW - 0.7, 0.4)
D.p(tt, "因为它没有否认人脉有用，而是指出了人脉起作用的前提条件。", size=19, bold=True, color=TEAL, space_after=0)
D.notes(s, "高分反驳的共同点：不否认对方，而是限定对方成立的范围。")

drill_slide("练习 D1 · Disagree + Explain（反驳 Andrew）", "DRILL · 学生输出", "Disagree + Explain",
            "两句话。Although 后面必须准确复述 Andrew 的观点。",
            ("Andrew is wrong because education is better than connections.",
             "Although Andrew argues that connections open doors, I believe education matters more, because a recommendation only works if the person can actually do the job."),
            [("Although Andrew argues that ______, I believe ______ because ______.",
              "可用角度：人脉需要先有资格 / 人脉不可复制 / 没人脉的人靠什么起步")], lines=3)

drill_slide("练习 D2 · Disagree + Explain（反驳 Kelly）", "DRILL · 学生输出", "Disagree + Explain",
            "这次反驳 Kelly。练的是方法，不是立场。",
            ("Kelly is not right because many people study but are still poor.",
             "Although Kelly argues that education guarantees upward mobility, I believe the effect depends on where a student studies, because two people with the same degree can face very different opportunities."),
            [("Although Kelly argues that ______, I believe ______ because ______.",
              "可用角度：同样的学历回报不同 / 教育需要时间和金钱 / 教育解决不了信息差")], lines=3)

s = D.slide()
y = D.header(s, "新角度从哪里来？三个抽屉", "WHERE NEW IDEAS COME FROM")
drawers = [("① 换一个人", "同样一件事，对谁最重要？", "对没有人脉的学生来说，教育是唯一的入口。", TEAL),
           ("② 换一个条件", "什么情况下对方说的才成立？", "人脉起作用的前提是你已经有资格。", ACCENT),
           ("③ 换一个时间", "短期和长期一样吗？", "人脉能让你更快听到消息，教育决定你能留多久。", GOLD)]
yy = y + 0.15
for k, q, ex, col in drawers:
    D.rect(s, ML, yy, CW, 1.35, fill=WHITE, line=col, lw=1.8, rounded=True)
    D.rect(s, ML, yy, 2.3, 1.35, fill=col, line=None, rounded=True)
    tn = D.tb(s, ML + 0.1, yy + 0.44, 2.1, 0.5)
    D.p(tn, k, size=20, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
    tt = D.tb(s, ML + 2.6, yy + 0.2, CW - 2.95, 0.45)
    D.p(tt, q, size=20, bold=True, color=col, space_after=6)
    tt2 = D.tb(s, ML + 2.6, yy + 0.72, CW - 2.95, 0.45)
    D.p(tt2, ex, size=19, color=INK, space_after=0)
    yy += 1.48
D.notes(s, "考场上写不出新角度时，就按这三个抽屉一个个试。")

output_slide("每人一条 Contribution", "OUTPUT · 4 人各一条", "读你写的其中一条：Agree + Add 或 Disagree + Explain。",
             ["听的人只回答：这句话删掉，讨论会少什么？",
              "如果答案是「什么都不少」——现场加一个具体的人或一个条件",
              "彭子骞读 A1，其余三人各读一条不同的"],
             "5 分钟", "这一条待会儿直接写进 Part 6 的作文。")

s = D.slide()
y = D.header(s, "Part 5 小结：4 分和 5 分的分界线", "PART 5 · 收")
D.rect(s, ML, y + 0.25, CW, 1.3, fill=GOLD, line=None, rounded=True)
tt = D.tb(s, ML + 0.45, y + 0.55, CW - 0.9, 0.8)
D.p(tt, "同样写了 100 词，有没有新信息，是完全不同的两个分数。", size=25, bold=True, color=WHITE,
    align=PP_ALIGN.CENTER, space_after=0)
yy = y + 1.85
for k, v, col in [("必须做到 ①", "明确提到 Kelly 或 Andrew 的名字与观点", TEAL),
                  ("必须做到 ②", "在同意 / 反驳之后，再加一句他没说过的话", GREEN),
                  ("尽量做到", "这句新话本身也有 because 或一个具体的人", GOLD)]:
    D.rect(s, ML, yy, CW, 0.92, fill=WHITE, line=col, lw=1.6, rounded=True)
    tt = D.tb(s, ML + 0.32, yy + 0.24, 2.3, 0.45)
    D.p(tt, k, size=20, bold=True, color=col, space_after=0)
    tt = D.tb(s, ML + 2.8, yy + 0.24, CW - 3.15, 0.45)
    D.p(tt, v, size=19, color=INK, space_after=0)
    yy += 1.02
D.notes(s, "Part 5 应在第 105 分钟结束，留够 20 分钟写作。")


# ============================================================================
# PART 6 · Full Writing（15–20 分钟）
# ============================================================================
def exam_screen(title, kicker, prof, prof_role, prof_text, a, a_text, b, b_text,
                source=SRC, size=19):
    """官方讨论区原样呈现：教授 + 两位同学，同一块面板里三条发言。"""
    s = D.slide()
    t = D.tb(s, ML, 0.38, CW * 0.72, 0.6)
    D.p(t, title, size=29, bold=True, color=TEAL, space_after=0, line_spacing=1.05)
    t = D.tb(s, ML + CW * 0.72, 0.48, CW * 0.28, 0.4)
    D.p(t, kicker, size=19, bold=True, color=ACCENT, align=PP_ALIGN.RIGHT, space_after=0)
    D.line(s, ML, 1.12, ML + 2.1, 1.12, ACCENT, 3.0)
    y = 1.30
    inner = CW - 0.95
    entries = [(f"{prof}（{prof_role}）：", prof_text, TEAL),
               (f"{a}（Student A）：", a_text, TEAL_MID),
               (f"{b}（Student B）：", b_text, ACCENT)]
    hs = [est_h(lab + txt, size, inner, 1.16) for lab, txt, _ in entries]
    panel_h = 0.40 + sum(hs) + 2 * 0.17 + 0.08
    D.rect(s, ML, y + 0.05, CW, panel_h, fill=WHITE, line=TEAL, lw=1.6, rounded=True)
    yy = y + 0.24
    for i, ((lab, txt, col), hh) in enumerate(zip(entries, hs)):
        D.rect(s, ML + 0.24, yy + 0.06, 0.055, hh - 0.06, fill=col, line=None)
        tt = D.tb(s, ML + 0.48, yy, inner, hh)
        D.rich(tt, [(lab, {"bold": True, "color": col, "size": size}),
                    (txt, {"size": size, "color": INK})], space_after=0, line_spacing=1.16)
        yy += hh + 0.17
        if i < 2:
            D.line(s, ML + 0.48, yy - 0.09, ML + CW - 0.32, yy - 0.09, LINE, 1.0)
    tn = D.tb(s, ML, y + 0.05 + panel_h + 0.11, CW, 0.4)
    D.p(tn, source, size=19, color=GREY, space_after=0)
    return s


D.part = "Part 6 · Full Writing"
D.section("Full Writing", "10 分钟，一次写完", 20,
          "今天所有练习，现在合成一篇。先填 Planning Box，再动笔。",
          ["Planning 2′", "写作 10′", "自查 3′", "互评 3′"], "PART 6")

exam_screen("题目回到眼前 · 完整官方题", "OFFICIAL PROMPT",
            "Dr. Gupta", "sociology", Q_PROF, "Kelly", Q_KELLY, "Andrew", Q_ANDREW)
D.notes(D.prs.slides[-1], "这一屏保持投影，学生写作全程可看。")

s = D.slide()
y = D.header(s, "写之前，先填这五行", "PLANNING BOX · 2 分钟", color=GOLD)
D.rect(s, ML, y + 0.02, CW, 0.6, fill=GOLD_PALE, line=None, rounded=True)
tt = D.tb(s, ML + 0.32, y + 0.16, CW - 0.65, 0.4)
D.p(tt, "只写关键词，不写完整句。填不满就说明想法还不够。", size=19, bold=True, color=GOLD, space_after=0)
yy = y + 0.78
rows = [("POSITION", "我站哪边？（education / connections）"),
        ("REASON", "一个具体理由（不许 good / important / useful）"),
        ("WHY", "This matters because …"),
        ("EXAMPLE", "谁 + 做什么 + 结果"),
        ("CONTRIBUTION", "回应 Kelly 还是 Andrew？我要加的新信息是什么？")]
for lab, hint in rows:
    D.rect(s, ML, yy, 2.4, 0.5, fill=GOLD, line=None, rounded=True)
    tn = D.tb(s, ML, yy + 0.09, 2.4, 0.4)
    D.p(tn, lab, size=19, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
    tt = D.tb(s, ML + 2.62, yy + 0.06, CW - 2.7, 0.4)
    D.p(tt, hint, size=19, color=GREY, space_after=0)
    D.line(s, ML + 2.62, yy + 0.54, ML + CW, yy + 0.54, LINE, 1.0)
    yy += 0.94
D.notes(s, "严格 2 分钟。填不完的直接开始写，不要拖。")

s = D.slide()
y = D.header(s, "老师的 Planning Box（60 秒版）", "WORKED EXAMPLE")
rows = [("POSITION", "education"),
        ("REASON", "the only advantage you can build without knowing anyone"),
        ("WHY", "ordinary families → nobody to introduce you"),
        ("EXAMPLE", "farmer's daughter → accounting exam → hired, knows nobody"),
        ("CONTRIBUTION", "→ Andrew：education gets you into the room where connections form")]
yy = y + 0.15
for lab, v in rows:
    D.rect(s, ML, yy, CW, 0.76, fill=WHITE, line=LINE, rounded=True)
    D.rect(s, ML, yy, 2.4, 0.76, fill=GREEN, line=None, rounded=True)
    tn = D.tb(s, ML, yy + 0.19, 2.4, 0.4)
    D.p(tn, lab, size=19, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
    tt = D.tb(s, ML + 2.66, yy + 0.19, CW - 2.95, 0.45)
    D.p(tt, v, size=19, bold=True, color=INK, space_after=0)
    yy += 0.84
D.rect(s, ML, yy + 0.05, CW, 0.72, fill=TEAL_TINT, line=None, rounded=True)
tt = D.tb(s, ML + 0.34, yy + 0.23, CW - 0.7, 0.42)
D.p(tt, "全是关键词，没有一个完整句子——Planning 的目的是定方向，不是先写一遍。", size=19, bold=True, color=TEAL, space_after=0)
D.notes(s, "边说边填，让学生看到 60 秒真的够。")

s = D.slide()
y = D.header(s, "现在开始 · 10 分钟", "WRITE", color=ACCENT)
D.rect(s, ML, y + 0.15, CW, 1.5, fill=ACCENT, line=None, rounded=True)
tt = D.tb(s, ML + 0.45, y + 0.45, CW - 0.9, 0.9)
D.p(tt, "10:00", size=42, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
yy = y + 1.95
for k, v in [("不查词典", "写不出来的词先用中文括号标记，写完再查。"),
             ("不回头改语法", "写完再改。中途回头会写不完 100 词。"),
             ("最后 2 分钟", "数一次词数，并确认自己提到了 Kelly 或 Andrew。")]:
    D.rect(s, ML, yy, CW, 1.0, fill=WHITE, line=LINE, rounded=True)
    D.rect(s, ML, yy, 0.06, 1.0, fill=ACCENT, line=None)
    tt = D.tb(s, ML + 0.34, yy + 0.14, CW - 0.7, 0.42)
    D.p(tt, k, size=20, bold=True, color=ACCENT, space_after=0)
    tt = D.tb(s, ML + 0.34, yy + 0.56, CW - 0.7, 0.4)
    D.p(tt, v, size=19, color=INK, space_after=0)
    yy += 1.1
D.notes(s, "计时开始就不要再说话。老师只在教室里走动。")

s = D.slide()
y = D.header(s, "支架版 · 给第一次写 AD 的同学", "SCAFFOLD · 彭子骞")
D.rect(s, ML, y + 0.02, CW, 0.6, fill=TEAL_PALE, line=None, rounded=True)
tt = D.tb(s, ML + 0.32, y + 0.16, CW - 0.65, 0.4)
D.p(tt, "把下面五句填完，就是一篇合格的 AD。填完还有时间，再加一句 As a result。", size=19, bold=True, color=TEAL, space_after=0)
yy = y + 0.72
frames = ["I would argue that ______ matters more than ______.",
          "One important reason is that ______.",
          "This matters because ______.",
          "For example, a student who ______ can ______.",
          "I agree with ______ that ______, but I would also add that ______."]
for i, f in enumerate(frames):
    D.rect(s, ML, yy, CW, 0.78, fill=WHITE, line=LINE, rounded=True)
    D.rect(s, ML, yy, 0.52, 0.78, fill=TEAL_MID, line=None, rounded=True)
    tn = D.tb(s, ML, yy + 0.19, 0.52, 0.4)
    D.p(tn, str(i + 1), size=19, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
    tt = D.tb(s, ML + 0.78, yy + 0.19, CW - 1.05, 0.45)
    D.p(tt, f, size=20, bold=True, color=INK, space_after=0)
    yy += 0.86
D.notes(s, "只发给彭子骞。其他三人不给，避免退回模板。")

s = D.slide()
y = D.header(s, "挑战版 · 给已经写过 AD 的同学", "CHALLENGE · 韩 / 刘 / 钟")
tasks = [("必须 120 词以上", "不是凑字数，是把一个理由推到 Result。"),
         ("必须出现一次 Although 或 At the same time", "训练让步句，让立场更成熟。"),
         ("例子里必须出现一个具体职业或场景", "nursing / accounting / café / design studio 都可以。"),
         ("Contribution 必须是三个抽屉之一", "换一个人 / 换一个条件 / 换一个时间。")]
yy = y + 0.2
for k, v in tasks:
    D.rect(s, ML, yy, CW, 1.08, fill=WHITE, line=GOLD, lw=1.6, rounded=True)
    tt = D.tb(s, ML + 0.34, yy + 0.18, CW - 0.7, 0.42)
    D.rich(tt, [("□  ", {"bold": True, "color": GOLD, "size": 20}), (k, {"bold": True, "size": 20})], space_after=0)
    tt = D.tb(s, ML + 0.34, yy + 0.62, CW - 0.7, 0.4)
    D.p(tt, v, size=19, color=GREY, space_after=0)
    yy += 1.2
D.notes(s, "四条打勾，缺一条就退回改。")

s = D.slide()
y = D.header(s, "写完 3 分钟 · 自查清单", "SELF-CHECK", color=GREEN)
checks = ["我有没有明确回应这场讨论（提到 Kelly 或 Andrew 的观点）？",
          "我有没有加入自己的新观点，而不是把别人的话重复一遍？",
          "我有没有一句真正解释 WHY 的话？",
          "我的例子里有没有一个具体的人和一个具体动作？",
          "我有没有写到 100 词以上？（数一次，写下来）"]
yy = y + 0.2
for i, c in enumerate(checks):
    D.rect(s, ML, yy, CW, 0.80, fill=GREEN_PALE if i % 2 == 0 else WHITE, line=LINE, rounded=True)
    D.rect(s, ML + 0.3, yy + 0.21, 0.38, 0.38, fill=WHITE, line=GREEN, lw=1.6)
    tt = D.tb(s, ML + 0.95, yy + 0.20, CW - 1.3, 0.45)
    D.p(tt, c, size=20, color=INK, space_after=0)
    yy += 0.88
tt = D.tb(s, ML, yy + 0.08, CW, 0.4)
D.p(tt, "字数：__________ 词        自评：__________ 分", size=20, bold=True, color=GREEN, space_after=0)
D.notes(s, "五条全部打勾才算完成。没打勾的当场补写，不要等下课。")

s = D.slide()
y = D.header(s, "同伴互评 · 只找三样东西", "PEER REVIEW · 3 分钟", color=GOLD)
D.rect(s, ML, y + 0.05, CW, 0.62, fill=GOLD_PALE, line=None, rounded=True)
tt = D.tb(s, ML + 0.32, y + 0.19, CW - 0.65, 0.4)
D.p(tt, "交换讲义。不许改语法，只找这三样，用铅笔标出来。", size=19, bold=True, color=GOLD, space_after=0)
yy = y + 0.9
finds = [("① 找立场句", "圈出来。找不到 → 在旁边写「无立场」。", TEAL),
         ("② 找例子里的那个人", "画方框。如果只有 many students → 写「没有人」。", ACCENT),
         ("③ 找新信息", "标星号。如果只是重复 Kelly / Andrew → 写「重复」。", GOLD)]
for k, v, col in finds:
    D.rect(s, ML, yy, CW, 1.25, fill=WHITE, line=col, lw=1.8, rounded=True)
    D.rect(s, ML, yy, 2.9, 1.25, fill=col, line=None, rounded=True)
    tn = D.tb(s, ML + 0.1, yy + 0.4, 2.7, 0.5)
    D.p(tn, k, size=21, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
    tt = D.tb(s, ML + 3.2, yy + 0.4, CW - 3.5, 0.5)
    D.p(tt, v, size=19, color=INK, space_after=0)
    yy += 1.4
D.notes(s, "互评只找这三样，超出范围的意见一律不写——否则会变成互相改语法。")

s = D.slide()
y = D.header(s, "今天这条链条，你已经走了两遍", "CLOSING THE LOOP")
chain = ["读题\n找争议", "选一边", "具体\nReason", "WHY", "Example", "Result", "Contribution"]
x = ML
bw = (CW - 6 * 0.24) / 7
for i, c in enumerate(chain):
    col = TEAL if i < 2 else (ACCENT if i < 6 else GOLD)
    D.rect(s, x, y + 0.5, bw, 1.35, fill=col, line=None, rounded=True)
    tt = D.tb(s, x + 0.06, y + 0.72, bw - 0.12, 1.0)
    for ln in c.split("\n"):
        D.p(tt, ln, size=19, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=2, line_spacing=1.05)
    x += bw + 0.24
D.rect(s, ML, y + 2.3, CW, 1.0, fill=TEAL_TINT, line=LINE, rounded=True)
tt = D.tb(s, ML + 0.4, y + 2.55, CW - 0.8, 0.5)
D.p(tt, "第 1 遍：Internship（上节课）        第 2 遍：Social mobility（今天）", size=21, bold=True, color=TEAL, space_after=0)
D.rect(s, ML, y + 3.45, CW, 1.0, fill=ACCENT, line=None, rounded=True)
tt = D.tb(s, ML + 0.4, y + 3.7, CW - 0.8, 0.5)
D.p(tt, "第 3 遍：今晚的作业（一道新的官方题）——这一遍没有人在旁边提醒你。", size=21, bold=True, color=WHITE, space_after=0)
D.notes(s, "把作业说成'第三遍'，学生更容易接受。")


# ============================================================================
# 作业 & 收尾
# ============================================================================
D.part = "作业 & 收尾"

s = D.slide()
y = D.header(s, "今晚的作业 · 分两层", "HOMEWORK")
cols = [("彭子骞", "打基础", TEAL, ["Reason → Why → Example 练习 12 题",
                                  "带框架的 AD 一篇（用支架版五句）",
                                  "题目：今天课上这道 social mobility",
                                  "不限时，可以查词典"]),
        ("韩 / 刘 / 钟", "上强度", ACCENT, ["一道全新的官方 TPO AD 题",
                                         "严格 10 分钟，一次完成",
                                         "至少一次 Contribution",
                                         "至少一个具体 Example，100 词以上"])]
x = ML
w = (CW - 0.3) / 2
for name, sub, col, items in cols:
    D.rect(s, x, y + 0.15, w, 4.2, fill=WHITE, line=col, lw=2.0, rounded=True)
    D.rect(s, x, y + 0.15, w, 0.95, fill=col, line=None, rounded=True)
    D.rect(s, x, y + 0.75, w, 0.35, fill=col, line=None)
    tt = D.tb(s, x + 0.3, y + 0.3, w - 0.6, 0.6)
    D.rich(tt, [(name + "   ", {"bold": True, "color": WHITE, "size": 23}),
                (sub, {"color": RGBColor(0xE6, 0xEE, 0xF0), "size": 19})], space_after=0)
    ty = y + 1.3
    for it in items:
        tt = D.tb(s, x + 0.34, ty, w - 0.68, 0.7)
        D.rich(tt, [("•  ", {"bold": True, "color": col, "size": 19}), (it, {"size": 19})],
               space_after=0, line_spacing=1.14)
        ty += 0.72
    x += w + 0.3
D.notes(s, "分层要当众说清楚，避免彭子骞觉得被区别对待——说明这是'第一次'的标准动作。")

exam_screen("作业题（韩 / 刘 / 钟）· 官方原题", "HOMEWORK PROMPT",
            "Dr. Diaz", "marketing", HW_PROF, "Kelly", HW_KELLY, "Andrew", HW_ANDREW,
            source="题源：TOEFL iBT® Writing · Write for an Academic Discussion（官方题目原文，未改写）")
D.notes(D.prs.slides[-1], "这道题话题更熟悉，但争议结构和今天完全一样：两个选项，必须选一个。")

s = D.slide()
y = D.header(s, "作业怎么写才不白写", "HOW TO DO IT")
steps = [("① 先填 Planning Box", "五行填完再动笔。不填直接写 = 白写。"),
         ("② 严格计时 10 分钟", "手机开计时器。写不完就交，写不完本身就是信息。"),
         ("③ 写完先自评", "用课上那五条自查清单，自己打一个分数。"),
         ("④ 标出你最不确定的一句", "下次课我们只讲你标出来的句子。")]
yy = y + 0.2
for k, v in steps:
    D.rect(s, ML, yy, CW, 1.1, fill=TEAL_TINT if k.startswith("①") or k.startswith("③") else WHITE,
           line=LINE, rounded=True)
    D.rect(s, ML, yy, 0.06, 1.1, fill=TEAL, line=None)
    tt = D.tb(s, ML + 0.34, yy + 0.18, CW - 0.7, 0.45)
    D.p(tt, k, size=20, bold=True, color=TEAL, space_after=0)
    tt = D.tb(s, ML + 0.34, yy + 0.63, CW - 0.7, 0.4)
    D.p(tt, v, size=19, color=INK, space_after=0)
    yy += 1.22
D.notes(s, "第④条最重要：它让下次课有真实素材，而不是老师猜。")

s = D.slide()
y = D.header(s, "一页带走 · 遇到任何 AD 题都这么走", "TAKE THIS HOME")
D.rect(s, ML, y + 0.08, CW, 4.5, fill=TEAL_TINT, line=TEAL, lw=1.6, rounded=True)
items = [("1", "读教授问题两遍", "它问什么？有几个选择？"),
         ("2", "读两位同学", "各站哪边？各给了什么理由？"),
         ("3", "选一边，写立场句", "I would argue that ______ matters more than ______."),
         ("4", "写一个具体理由", "不许 good / important / useful"),
         ("5", "补一句 WHY", "This matters because ______."),
         ("6", "补一个例子", "谁 + 做什么 + 结果"),
         ("7", "回应一位同学", "同意 + 加新信息，或者 Although + 我的看法")]
yy = y + 0.32
for n, k, v in items:
    D.rect(s, ML + 0.32, yy, 0.44, 0.44, fill=TEAL, line=None, rounded=True, adj=0.5)
    tn = D.tb(s, ML + 0.32, yy + 0.07, 0.44, 0.4)
    D.p(tn, n, size=19, bold=True, color=WHITE, align=PP_ALIGN.CENTER, space_after=0)
    tt = D.tb(s, ML + 1.0, yy + 0.06, 3.4, 0.4)
    D.p(tt, k, size=20, bold=True, color=INK, space_after=0)
    tt = D.tb(s, ML + 4.6, yy + 0.06, CW - 5.0, 0.4)
    D.p(tt, v, size=19, color=GREY, space_after=0)
    yy += 0.58
D.notes(s, "让学生拍照。这一页就是全部方法。")

s = D.slide()
y = D.header(s, "Exit Ticket · 下课前写完交给我", "EXIT TICKET", color=GOLD)
qs = ["今天我最大的发现是：",
      "我写作里最弱的一环是（Reason / WHY / Example / Contribution）：",
      "下一篇 AD 我一定会做的一件事是："]
yy = y + 0.25
for i, q in enumerate(qs):
    D.rect(s, ML, yy, CW, 1.32, fill=GOLD_PALE if i % 2 == 0 else WHITE, line=LINE, rounded=True)
    tt = D.tb(s, ML + 0.34, yy + 0.18, CW - 0.7, 0.42)
    D.p(tt, q, size=20, bold=True, color=GOLD if i % 2 == 0 else INK, space_after=0)
    D.line(s, ML + 0.34, yy + 1.02, ML + CW - 0.34, yy + 1.02, LINE, 1.0)
    yy += 1.44
D.notes(s, "Exit ticket 决定下次课的开场——第二问的统计结果直接变成下节课的重点。")

s = D.slide(footer=False, bg=TEAL)
D.rect(s, 0, 0, SW, 0.42, fill=ACCENT, line=None)
D.rect(s, 0.95, 2.15, 0.07, 2.6, fill=ACCENT, line=None)
t = D.tb(s, 1.32, 2.1, 11.0, 1.4)
D.p(t, "题会变，流程不会变。", size=44, bold=True, color=WHITE, space_after=10, line_spacing=1.05)
t = D.tb(s, 1.32, 3.35, 11.0, 1.2)
D.p(t, "找争议 → 选观点 → 具体理由 → 解释 WHY → 加例子 → 给结果 → 回应讨论", size=23,
    color=RGBColor(0xC9, 0xDE, 0xE3), space_after=10)
D.p(t, "下次课：把今天的作业，逐句改成 5 分句。", size=BODY, color=RGBColor(0x9E, 0xC6, 0xCE), space_after=0)
D.notes(s, "结束语只说一句：今天你没有背任何一句话，但你已经能写了。")


# ============================================================================
if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "托福基础写作-AD第2课-课堂PPT.pptx")
    D.save(out)
    noted = sum(1 for sl in D.prs.slides if sl.has_notes_slide
                and sl.notes_slide.notes_text_frame.text.strip())
    print(f"saved {out}")
    print(f"slides: {D.n}   speaker notes: {noted}")
