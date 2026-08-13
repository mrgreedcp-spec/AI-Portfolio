# -*- coding: utf-8 -*-
"""第三节课 PPT 的版式引擎 —— 完全沿用第二节课 PPT 的设计令牌。"""

import math
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ----------------------------------------------------------------- 设计令牌
SLIDE_W, SLIDE_H = 13.333, 7.5
BG = "0B1220"
BAR = "38BDF8"
KICKER_C = "38BDF8"
TITLE_C = "FFFFFF"
FOOT_C = "94A3B8"
INK = "0F172A"

CJK = "微软雅黑"
LAT = "Arial"

# (面板底色, 边框色, 标签色)
PAL = {
    "blue":   ("DBEAFE", "38BDF8", "38BDF8"),
    "purple": ("F3E8FF", "A78BFA", "C4B5FD"),
    "green":  ("DCFCE7", "22C55E", "86EFAC"),
    "amber":  ("FEF3C7", "F59E0B", "FDE68A"),
    "cream":  ("FFFBEB", "F59E0B", "FDE68A"),
    "red":    ("FEE2E2", "F87171", "FCA5A5"),
}

FOOTER_DEFAULT = "雅思阅读精讲 · 第三节 · 黄玉蕾 Renee"


def _rgb(h):
    return RGBColor.from_string(h)


def _text_width_em(s):
    """按字符估算宽度（单位：em）。CJK/全角 1.0，ASCII 约 0.55。"""
    w = 0.0
    for ch in s:
        o = ord(ch)
        if o > 0x2E7F and o not in (0x2019, 0x2018, 0x201C, 0x201D):
            w += 1.0          # CJK、全角标点、破折号等
        elif o > 0x2000:
            w += 0.55         # 常用西文标点（… — ‘ ’ 等按半角处理）
        else:
            w += 0.55
    return w


def _lines_needed(paras, width_in, size_pt):
    """给定宽度与字号，估算需要的总行数。"""
    em = size_pt / 72.0
    usable = max(width_in - 0.14, 0.4)
    total = 0
    for p in paras:
        if not p.strip():
            total += 1
            continue
        need = _text_width_em(p) * em
        total += max(1, math.ceil(need / usable - 1e-6))
    return total


def fit_size(paras, width_in, height_in, sizes):
    """从 sizes（由大到小）中挑出第一个放得下的字号。"""
    for s in sizes:
        if _lines_needed(paras, width_in, s) * (s / 72.0) * 1.26 <= height_in:
            return s
    return sizes[-1]


class Deck:
    def __init__(self, footer=FOOTER_DEFAULT):
        self.prs = Presentation()
        self.prs.slide_width = Emu(int(SLIDE_W * 914400))
        self.prs.slide_height = Emu(int(SLIDE_H * 914400))
        self.blank = self.prs.slide_layouts[6]
        self.footer = footer
        self.n = 0

    # ---------------------------------------------------------- 低层绘制
    def _box(self, slide, x, y, w, h, fill=None, line=None):
        sp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y),
                                    Inches(w), Inches(h))
        sp.shadow.inherit = False
        if fill:
            sp.fill.solid()
            sp.fill.fore_color.rgb = _rgb(fill)
        else:
            sp.fill.background()
        if line:
            sp.line.color.rgb = _rgb(line)
            sp.line.width = Pt(1)
        else:
            sp.line.fill.background()
        return sp

    def _write(self, sp, paras, size, color, bold=False, align=PP_ALIGN.LEFT,
               anchor=MSO_ANCHOR.MIDDLE, inset=0.06, latin=CJK):
        tf = sp.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = anchor
        tf.margin_left = Inches(inset)
        tf.margin_right = Inches(inset)
        tf.margin_top = Inches(0.03)
        tf.margin_bottom = Inches(0.03)
        for i, ptxt in enumerate(paras):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.alignment = align
            r = p.add_run()
            r.text = ptxt
            f = r.font
            f.size = Pt(size)
            f.bold = bold
            f.color.rgb = _rgb(color)
            f.name = latin
            # 中日韩字体也要显式设置，否则 PowerPoint 会回退
            rPr = r._r.get_or_add_rPr()
            for tag in ("a:ea", "a:cs"):
                el = rPr.makeelement(
                    "{http://schemas.openxmlformats.org/drawingml/2006/main}" + tag.split(":")[1],
                    {"typeface": latin})
                rPr.append(el)
        return sp

    def _label(self, slide, x, y, text, color, w=3.4):
        sp = self._box(slide, x, y, w, 0.30)
        self._write(sp, [text], 18.5, color, bold=True, inset=0.0)
        return sp

    def panel(self, slide, x, y, w, h, paras, tone, size=None, bold=False,
              sizes=(19, 18, 17, 16, 15, 14, 13, 12, 11), anchor=None):
        fill, line, _ = PAL[tone]
        sp = self._box(slide, x, y, w, h, fill, line)
        s = size or fit_size(paras, w, h, list(sizes))
        if anchor is None:
            # 内容明显短于面板时垂直居中，避免下方留出大片空白
            used = _lines_needed(paras, w, s) * (s / 72.0) * 1.26
            anchor = MSO_ANCHOR.MIDDLE if used < h * 0.72 else MSO_ANCHOR.TOP
        self._write(sp, paras, s, INK, bold=bold, anchor=anchor)
        return sp

    def labelled(self, slide, x, y, w, h, label, paras, tone, bold=False,
                 sizes=(19, 18, 17, 16, 15, 14, 13, 12, 11), lw=None, anchor=None):
        _, _, lab = PAL[tone]
        self._label(slide, x, y, label, lab, w=lw or w)
        return self.panel(slide, x, y + 0.34, w, h, paras, tone, bold=bold,
                          sizes=sizes, anchor=anchor)

    # ------------------------------------------------------- 轮子示意图
    def wheel(self, slide, cx, cy, r, style, color="0F172A", spokes=6):
        """画一个轮子。style: 'extend' 伸出轮圈 / 'dashed' 虚线 / 'curved' 弧线。"""
        from pptx.enum.shapes import MSO_CONNECTOR
        from pptx.enum.dml import MSO_LINE_DASH_STYLE

        ring = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx - r), Inches(cy - r),
                                      Inches(2 * r), Inches(2 * r))
        ring.shadow.inherit = False
        ring.fill.background()
        ring.line.color.rgb = _rgb(color)
        ring.line.width = Pt(1.75)

        for i in range(spokes):
            a = math.pi * 2 * i / spokes
            dx, dy = math.cos(a), math.sin(a)
            if style == "curved":
                # 用多段折线近似一条向同一方向渐扫的弧形轮辐
                pts = []
                steps = 10
                for j in range(steps + 1):
                    t = j / steps
                    ang = a + 0.62 * t                 # 越靠外，偏转越大
                    pts.append((cx + r * t * math.cos(ang), cy + r * t * math.sin(ang)))
                ff = slide.shapes.build_freeform(Inches(pts[0][0]), Inches(pts[0][1]))
                ff.add_line_segments([(Inches(x), Inches(y)) for x, y in pts[1:]],
                                     close=False)
                sp = ff.convert_to_shape()
                sp.shadow.inherit = False
                sp.fill.background()
                sp.line.color.rgb = _rgb(color)
                sp.line.width = Pt(1.75)
            else:
                ext = 1.34 if style == "extend" else 1.0
                cn = slide.shapes.add_connector(
                    MSO_CONNECTOR.STRAIGHT, Inches(cx), Inches(cy),
                    Inches(cx + r * ext * dx), Inches(cy + r * ext * dy))
                cn.shadow.inherit = False
                cn.line.color.rgb = _rgb(color)
                cn.line.width = Pt(1.75)
                if style == "dashed":
                    cn.line.dash_style = MSO_LINE_DASH_STYLE.DASH

    # ------------------------------------------------------------ 版式
    def slide(self, kicker, title, footer=None):
        s = self.prs.slides.add_slide(self.blank)
        self.n += 1
        self._box(s, 0, 0, SLIDE_W, SLIDE_H, BG, BG)
        self._box(s, 0, 0, SLIDE_W, 0.13, BAR, BAR)
        k = self._box(s, 0.62, 0.34, 8.6, 0.32)
        self._write(k, [kicker], 18.5, KICKER_C, bold=True, inset=0.0, latin=LAT)
        t = self._box(s, 0.62, 0.74, 12.05, 0.66)
        ts = fit_size([title], 12.05, 0.66, [30, 27, 24, 22, 20])
        self._write(t, [title], ts, TITLE_C, bold=True, inset=0.0)
        f = self._box(s, 0.62, 7.06, 8.2, 0.30)
        self._write(f, [footer or self.footer], 15, FOOT_C, inset=0.0)
        pn = self._box(s, 12.15, 7.06, 0.55, 0.30)
        self._write(pn, [str(self.n)], 15, FOOT_C, align=PP_ALIGN.RIGHT,
                    inset=0.0, latin=LAT)
        return s

    def three_col(self, kicker, title, cols, footer=None):
        """三栏卡片版（文章地图 / 目标 / 小结通用）。"""
        s = self.slide(kicker, title, footer)
        tones = ["blue", "purple", "green"]
        xs = [0.72, 4.74, 8.76]
        for (head, items), x, tone in zip(cols, xs, tones):
            self._label(s, x, 1.62, head, PAL[tone][2])
            self.panel(s, x, 2.00, 3.75, 3.95,
                       [f"· {i}" for i in items], tone, bold=True,
                       sizes=(22, 20, 18, 17, 16, 15, 14))
        return s

    def bullets(self, kicker, title, blocks, footer=None):
        """整幅若干长条（方法页通用）。blocks = [(text, tone), ...]"""
        s = self.slide(kicker, title, footer)
        n = len(blocks)
        top, bottom = 1.55, 6.85
        gap = 0.22
        h = (bottom - top - gap * (n - 1)) / n
        y = top
        for text, tone in blocks:
            paras = text if isinstance(text, list) else [text]
            self.panel(s, 0.80, y, 11.75, h, paras, tone, bold=True,
                       sizes=(23, 21, 20, 19, 18, 17, 16, 15))
            y += h + gap
        return s

    def save(self, path):
        self.prs.save(path)
        return path
