---
name: ielts-lesson-deck
description: 生成"雅思阅读精讲班"的课堂 PPT 与学生打印讲义，版式沿用第二节课的设计系统（深色底 + 顶部蓝条 + 四色面板），每题两页逐题讲解。当需要做第 N 节课的课件、讲义、逐题精讲、长难句拆解页，或要给某篇雅思阅读真题出一套课堂材料时使用。Use when building IELTS reading lesson slides, teacher decks, or student handouts for this course.
---

# 雅思阅读精讲班 · 出片流程

给定一篇（或几篇）雅思阅读真题 + 题目 + 答案，产出两份材料：

| 产物 | 版式来源 | 结构 |
| --- | --- | --- |
| `第N节课PPT_雅思阅读精讲.pptx` | 第二节课 PPT | 每题两页：逐题标准精讲 + 长难句拆解/随题词汇 |
| `第N节课打印资料_雅思阅读精讲.docx` | `lesson3/assets/lesson2_template.docx` | 原文标注 P/S + 题目 + 答案速查 + 词汇与长难句 |

## 铁律

1. **题目和答案一律照抄原卷**，不得改写、不得重新编号。原卷的印刷错误（如 `can be soften`）原样保留，需要说明就加注。
2. **答案唯一事实来源是 `questions.py`**，PPT 与讲义都从它读取，绝不各写一份。
3. **出片后必须跑 `verify.py`**，三项检查（面板溢出 / 两份文件答案一致 / 与题库一致）全绿才算完成。
4. 答案若原卷未附，**先从原文逐题推导并把证据句写进 `ev` 字段**，不要凭印象填。

## 目录约定

```
lessonN/
  src/
    passages.py     原文，按 [P#][S#] 切分（段落编号需与答案解析的 Paragraph 编号对齐）
    questions.py    题目与答案 —— 唯一事实来源
    teach_p*.py     各篇逐题讲解内容（字段见 reference/content-schema.md）
    vocab.py        词汇表与长难句表
    build_pptx.py   出 PPT
    build_docx.py   出讲义
  assets/           模板与图片
  第N节课PPT_....pptx
  第N节课打印资料_....docx
```

## 做一节新课的步骤

1. **读材料**：原文 PDF → 用 `pypdf` 抽文本；有图（流程图、平面图、图形配对）时用 `pypdfium2` 渲染出来看，**不要靠猜**。
2. **切原文**：写进 `passages.py`，段落编号务必与原卷答案解析里的 `Paragraph n` 对齐。
3. **抄题目**：写进 `questions.py`，表格题逐格照抄。
4. **定答案**：原卷有答案页就照抄；没有就逐题推导，并在 `teach_*.py` 的 `ev` 里留下证据句。
5. **写讲解**：每题填满 `reference/content-schema.md` 里的字段。
6. **出片**：`python3 build_pptx.py && python3 build_docx.py`
7. **校验**：`python3 verify.py <pptx> <docx>`，再用 LibreOffice 转 PDF 抽查几页版式。

```bash
# 环境（首次）
pip install python-pptx python-docx pypdf pypdfium2 openpyxl Pillow
apt-get install -y libreoffice-impress libreoffice-writer   # 转 PDF 抽查用
```

## 引擎用法

```python
import sys; sys.path.insert(0, ".claude/skills/ielts-lesson-deck")
from deck import Deck

d = Deck(footer="雅思阅读精讲 · 第四节 · 黄玉蕾 Renee")

d.slide("IELTS ACADEMIC READING", "雅思阅读精讲班 · 第四节课")     # 空白骨架页
d.three_col("文章地图", "PASSAGE 1 · ...", cols)                  # 三栏卡片
d.bullets("题型策略", "Passage 1 题型策略", blocks)                # 整幅长条
d.divider("SECTION", "第二部分：表格填空")                          # 章节分隔
d.qa_pair(q, footer, progress="第 3 / 13 题")                     # 一题两页
d.passage_block(teach_p1, 1, "英文标题", "中文小结", footer)        # 一整篇
d.save("第四节课PPT_雅思阅读精讲.pptx")
```

`passage_block()` 会自动完成：文章地图 → 题型策略 → 逐题两页（带进度）→ 小结。
选择题（`kind="MCQ"`）自动多出一栏选项区，无需另写代码。

## 关于自动缩字

引擎用字符宽度模型估算行数来选字号，同时给每个文本框写入 PowerPoint 的
`normAutofit`。两者是**互补**关系，不是二选一：

- 估算模型负责让字号一开始就合理（不会满页 11pt）；
- `normAutofit` 是兜底——PowerPoint 里字体度量和估算不完全一致时，由 PowerPoint 自己缩。

注意：`normAutofit` 的 `fontScale` 由 PowerPoint 在**编辑时**才重算，某些查看器
（含 LibreOffice）打开时不会立即生效。所以**不能只靠它**，`verify.py` 的溢出检查仍须跑。

## 常见坑

- **东亚字体**：只设 `font.name` 不够，必须同时写 `<a:ea>` 和 `<a:cs>`，否则 PowerPoint 回退成默认字体。引擎已处理。
- **LibreOffice 转 PDF 报 "source file could not be loaded"**：多半是只装了 `libreoffice-core`，需补装 `libreoffice-impress` / `libreoffice-writer`。
- **Word 列宽不生效**：必须同时写 `tblW` / `tblLayout=fixed` / `tblGrid` / `tcW` 四处，只设 `cell.width` 在 LibreOffice 下会被忽略。见 `lesson3/src/docx_kit.py`。
- **答案速查表跨页断开**：答案表用 6 列（题号+答案 ×3），一篇 13 题只占 5 行，整节课的答案能压在一页内。
- **`pdfplumber` / `pypdf` 报 `_cffi_backend` 缺失**：`pip install --ignore-installed cffi cryptography`。

## 参考

- `reference/content-schema.md` —— 每题需要填哪些字段
- `reference/design-tokens.md` —— 颜色、字号、坐标
