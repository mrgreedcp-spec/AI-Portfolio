# -*- coding: utf-8 -*-
"""课件与讲义的构建后校验。

三项检查（出片后必跑，任一不通过就不要交付）：
    1. check_overflow  —— 有底色的内容面板是否放得下文字
    2. check_answers   —— PPT 与打印讲义的答案是否逐题一致
    3. check_pool      —— 题号与答案是否和题库（唯一事实来源）一致

用法：
    python3 verify.py <deck.pptx> [handout.docx]
"""

import re
import sys

from pptx import Presentation
from pptx.util import Emu

from deck import lines_needed

A_NS = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P_NS = "{http://schemas.openxmlformats.org/presentationml/2006/main}"


# ------------------------------------------------------------------ 溢出
def check_overflow(pptx_path, tolerance=0.02):
    """只检查有底色的内容面板；无底色的标签框本来就允许溢出（与第二课设计一致）。"""
    prs = Presentation(pptx_path)
    bad = []
    for i, s in enumerate(prs.slides, 1):
        for sh in s.shapes:
            if not sh.has_text_frame:
                continue
            spPr = sh._element.find(f".//{P_NS}spPr")
            if spPr is None or spPr.find(f"{A_NS}solidFill/{A_NS}srgbClr") is None:
                continue
            w, h = Emu(sh.width).inches, Emu(sh.height).inches
            if w > 13 or h > 7:            # 背景块
                continue
            paras = ["".join(r.text for r in p.runs) for p in sh.text_frame.paragraphs]
            if not any(paras):
                continue
            size = next((p.runs[0].font.size.pt for p in sh.text_frame.paragraphs
                         if p.runs and p.runs[0].font.size), None)
            if not size:
                continue
            need = lines_needed(paras, w, size) * (size / 72.0) * 1.26
            if need > h + tolerance:
                bad.append((i, round(need, 2), round(h, 2), size, paras[0][:46]))
    return bad


# ------------------------------------------------------------------ 答案
def deck_answers(pptx_path):
    """从课件里抓出 {(篇目标签, 题号): 答案}。"""
    prs = Presentation(pptx_path)
    out = {}
    for s in prs.slides:
        txt = [sh.text_frame.text for sh in s.shapes if sh.has_text_frame]
        title = next((t for t in txt if "｜" in t), "")
        line = next((t for t in txt if t.startswith("Answer:")), None)
        if not line:
            continue
        ans = line.split("\n")[0].replace("Answer:", "").strip()
        m = re.match(r"([^\sQ｜]+)\s*Q(\d+)｜", title)
        if m:
            out[(m.group(1), int(m.group(2)))] = ans
    return out


def handout_answers(docx_path, section_names):
    """从讲义的答案速查表抓出 {(篇目标签, 题号): 答案}。

    section_names: {讲义里的小标题前缀: 篇目标签}，与课件标题前缀对齐。
    """
    from docx import Document
    from docx.table import Table

    doc = Document(docx_path)
    out, cur = {}, None
    for block in doc.element.body:
        tag = block.tag.split("}")[1]
        if tag == "p":
            t = "".join(n.text or "" for n in block.iter() if n.tag.endswith("}t"))
            for prefix, label in section_names.items():
                if t.startswith(prefix):
                    cur = label
        elif tag == "tbl" and cur:
            tb = Table(block, doc)
            if len(tb.columns) != 6:       # 答案速查表固定 6 列（题号+答案 ×3）
                continue
            for r in tb.rows:
                c = [x.text.strip() for x in r.cells]
                for k in range(0, 6, 2):
                    if c[k].isdigit():
                        out[(cur, int(c[k]))] = c[k + 1]
            cur = None
    return out


def check_answers(pptx_path, docx_path, section_names):
    a, b = deck_answers(pptx_path), handout_answers(docx_path, section_names)
    keys = sorted(set(a) | set(b))
    return [(k, a.get(k), b.get(k)) for k in keys if a.get(k) != b.get(k)], len(a), len(b)


def check_pool(modules, answer_keys):
    """teach_*.py 的答案是否与 questions.py 的题库一致。

    modules / answer_keys 为等长列表，一一对应。
    """
    bad = []
    for mod, key in zip(modules, answer_keys):
        if [q["n"] for q in mod.Q] != sorted(key):
            bad.append(("题号不一致", mod.__name__))
        for q in mod.Q:
            if key.get(q["n"]) != q["ans"]:
                bad.append((mod.__name__, q["n"], q["ans"], key.get(q["n"])))
    return bad


# ------------------------------------------------------------------ 报告
def report(pptx_path, docx_path=None, section_names=None):
    ok = True
    over = check_overflow(pptx_path)
    print(f"[1] 面板溢出        : {len(over)} 处")
    for b in over[:10]:
        print("      !!", b)
    ok &= not over

    if docx_path and section_names:
        diff, na, nb = check_answers(pptx_path, docx_path, section_names)
        print(f"[2] 答案一致性      : PPT {na} 题 / 讲义 {nb} 题，不一致 {len(diff)} 处")
        for d in diff[:10]:
            print("      !!", d)
        ok &= not diff
    print("结果:", "通过" if ok else "未通过")
    return ok


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    sys.exit(0 if report(sys.argv[1],
                         sys.argv[2] if len(sys.argv) > 2 else None) else 1)
