# 雅思阅读精讲班 · 第三节课材料

参照第二节课的 PPT 与打印资料生成，版式、方法论与命名习惯保持一致。

## 交付物

| 文件 | 说明 |
| --- | --- |
| `第三节课PPT_雅思阅读精讲.pptx` | 139 页课堂课件，逐题两页讲解 |
| `第三节课打印资料_雅思阅读精讲.docx` | 30 页学生讲义，原文标注 P/S + 题目 + 答案 + 词汇与长难句 |

## 本节内容

| 篇目 | 题号 | 定位 | 题型 |
| --- | --- | --- | --- |
| The History of the Pencil（Flow-chart） | Q1–8 | 课前延迟检索（第二节课留题） | 笔记填空 + 判断 |
| How much higher? How much faster? | Q1–13 | 课堂精讲 | 判断 + 句子填空 + 选择 |
| What Do Whales Feel? | Q15–26 | 课堂精讲 | 表格填空 + 简答 |
| Visual Symbols and the Blind | Q27–40 | 课堂精讲 | 选择 + 图形配对 + 词库摘要 |
| The Origins of Weather Forecasting | Q1–13 | 课后作业 | 判断 + 笔记填空 |

合计 60 题，全部逐题讲解。

## 与第二节课的衔接

- 第二节课打印资料写明「Pencil 流程图版 Q1–8 留作第三课课前延迟检索」，本节作为开场兑现。
- 第二节课主题是长难句四步拆句法；本节在此基础上扩展题型，每道题第二页仍回到句子拆解。
- PPT 设计令牌（深色底 `0B1220`、顶部蓝条 `38BDF8`、四色面板、页脚页码）与第二节课完全一致。
- 打印资料直接复用第二节课的样式表（`assets/lesson2_template.docx`），页眉改为「精讲第三课」。

## PPT 逐题两页结构

1. **逐题标准精讲**：题干 → ① 入口 → ② 原文证据（带 P/S）→ ③ 同义替换 / 判断逻辑 → ④ 答案
2. **长难句拆解 + 随题词汇**：原句 → 核心主干 → 层层拆解 → 课堂表达 → 随题词汇

选择题多一栏选项区；Q30–32 之前插入一页轮子图形对照。

## 源码

```
src/
  passages.py     四篇原文，按 P/S 切分
  questions.py    题目与答案（唯一事实来源，PPT 与讲义共用）
  teach_p1..p4.py 各篇逐题讲解内容
  teach_pencil.py 课前延迟检索 Q1–8 复盘
  vocab.py        词汇表与长难句表
  deck.py         PPT 版式引擎（设计令牌 + 自动字号适配）
  docx_kit.py     讲义排版工具（复用第二节课样式表）
  make_wheels.py  生成 Q30–32 轮子示意图
  build_pptx.py   生成 PPT
  build_docx.py   生成打印资料
```

重新生成：

```bash
cd src
python3 make_wheels.py && python3 build_pptx.py && python3 build_docx.py
```

## 答案一致性

`questions.py` 是答案的唯一来源，PPT 与讲义都从它读取。构建后校验：

- 60 题答案在 PPT 与讲义中逐题一致
- 55 条题干 / 选项与原始 PDF 讲义逐字一致（题目未作改动）
- 31 个填空类答案均可在本仓库转写的原文中检索到
- Passage 4 的 13 题答案与 PDF 自带答案解析完全一致

## 两处需要说明的地方

- **Passage 2 Q21**：原表印作 `bowhead whales and humpback whales`，只有第一个空编号为 21，答案 `bowhead`；第二处点线是原书 humpback 的印刷位置，不是考点。讲义中已加注。
- **Passage 2 题号**：所给 PDF 该篇标注为 Questions 15–26（无第 14 题），本材料照此沿用，未重新编号。
