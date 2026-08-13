# -*- coding: utf-8 -*-
"""生成 Passage 3 Q30–32 的三个轮子示意图（供打印资料内嵌）。

三种轮辐画法与原书插图一致：
    30 直线且伸出轮圈   31 虚线   32 弧形弯曲
"""

import math
import os

from PIL import Image, ImageDraw

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "assets", "wheels_q30_32.png")

S = 4                      # 超采样倍数，缩小后边缘更平滑
W, H = 1500 * S, 370 * S
INK = (17, 24, 39)
LW = 3 * S


def dashed_line(dr, p0, p1, width, dash=13 * S, gap=9 * S):
    x0, y0 = p0
    x1, y1 = p1
    total = math.hypot(x1 - x0, y1 - y0)
    if total == 0:
        return
    ux, uy = (x1 - x0) / total, (y1 - y0) / total
    d = 0.0
    while d < total:
        e = min(d + dash, total)
        dr.line([(x0 + ux * d, y0 + uy * d), (x0 + ux * e, y0 + uy * e)],
                fill=INK, width=width)
        d = e + gap


def wheel(dr, cx, cy, r, style, spokes=6):
    dr.ellipse([cx - r, cy - r, cx + r, cy + r], outline=INK, width=LW)
    for i in range(spokes):
        a = math.pi * 2 * i / spokes
        if style == "curved":
            pts = []
            for j in range(41):
                t = j / 40
                ang = a + 0.62 * t
                pts.append((cx + r * t * math.cos(ang), cy + r * t * math.sin(ang)))
            dr.line(pts, fill=INK, width=LW, joint="curve")
        else:
            ext = 1.34 if style == "extend" else 1.0
            p1 = (cx + r * ext * math.cos(a), cy + r * ext * math.sin(a))
            if style == "dashed":
                dashed_line(dr, (cx, cy), p1, LW)
            else:
                dr.line([(cx, cy), p1], fill=INK, width=LW)


def build():
    img = Image.new("RGB", (W, H), "white")
    dr = ImageDraw.Draw(img)
    r = 120 * S
    for k, (cx, style) in enumerate(((260 * S, "extend"),
                                     (750 * S, "dashed"),
                                     (1240 * S, "curved"))):
        wheel(dr, cx, 185 * S, r, style)
        # 题号用简单的粗线条数字太麻烦，改由 Word 侧的表格给出编号
    img = img.resize((W // S, H // S), Image.LANCZOS)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, dpi=(300, 300))
    print("OK ", OUT)
    return OUT


if __name__ == "__main__":
    build()
