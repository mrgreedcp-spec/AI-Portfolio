# 逐题讲解的内容字段

每个 `teach_*.py` 导出三样东西：`MAP`、`STRATEGY`、`SUMMARY`、`Q`。

## 篇级字段

```python
MAP = [                       # 文章地图，恰好三栏
    ("P1–P3", ["古代玩偶", "木制玩偶", "欧洲生产中心"]),
    ("P4–P8", ["composition", "wax / porcelain", "rag / cloth"]),
    ("P9–P10", ["celluloid", "plastic / vinyl", "现代收藏玩偶"]),
]

STRATEGY = [                  # 题型策略，2–4 条，每条一个元组
    ("Q1–6 填空题：空格前后先判断词性。",),
    ("Q7–13 判断题：比较方向、范围限定是主要陷阱。",),
]

SUMMARY = [                   # 小结，三栏，结构同 MAP
    ("材料关系", ["made of", "with", "wrapped / covered"]),
    ("比较方向", ["more than", "not as ... as", "more durable"]),
    ("范围边界", ["commercially", "subset", "collectible ≠ collector"]),
]
```

## 题级字段

```python
dict(
  n=1,                        # 题号，必须与 questions.py 的答案键一致
  kind="TFNG",                # TFNG / FILL / MCQ / SHORT / TABLE / MATCH / SUMMARY
  # ---- 第一页：逐题标准精讲 ----
  title="P1 Q1｜date from：把“大约1900”对回原文时间",   # 页标题，格式固定为 "<前缀> Q<号>｜<考点>"
  stem="Modern official athletic records date from about 1900.",   # 题干原文
  options=[...],              # 仅 kind="MCQ" 需要，4 个选项，不带 A/B/C/D 前缀
  entry=["锚点：official records / about 1900。",
         "判断题先问：记录从何时开始？"],                 # ① 入口，2 条短句最佳
  ev="P1 S1: Since the early years of the twentieth century, ...",  # ② 原文证据，必须带 P/S
  logic=["official records ↔ ... began keeping records。",
         "about 1900 ↔ the early years of the twentieth century。",
         "主体一致、时间一致 → 支持。"],                  # ③ 同义替换 / 判断逻辑，2–3 条
  ans="TRUE",                 # ④ 答案，必须与 questions.py 完全相同的字符串
  ansnote=["时间与主体双对应。", "近似说法≠矛盾。"],       # 答案下方的两行小字
  # ---- 第二页：长难句拆解 + 随题词汇 ----
  stitle="P1 Q1｜when 定语从句 + 三个 how 从句",          # 页标题
  sent="Since the early years of ... through space.",   # 原句（可跨句，用 ... 连接）
  core="There has been a steady improvement.",          # 核心主干，越短越好
  layers=["Since ... century 是时间状语，划定全文起点。",
          "when 引导定语从句...",
          "how fast / how high / how far 三个从句并列。",
          "themselves included 是插入语，先跳过。"],       # 层层拆解，3–4 条
  cn="自20世纪初国际田联开始保存记录以来，……",              # 课堂表达（中文翻译）
  vocab=["steady 稳定的 ↔ continuous；hurl 投掷 ↔ throw",
         "date from = 始于；keep records = 保存记录"],     # 随题词汇，2 行
)
```

## 写作要求

- `title` / `stitle` 的 `Q<号>｜` 前缀是 `verify.py` 抓答案用的，**格式不能改**。
- `ev` 必须以 `P<n> S<n>:` 开头，讲义的"定位"列直接从这里切出来。
- `entry` 每条 ≤ 26 个中文字符；`logic` 每条 ≤ 30；`cn` 整段 ≤ 70。超了会被自动缩字，可读性下降。
- `ansnote` 写"为什么是这个答案"的一句话提示，**不要重复选项字母**（页面上方已有 `Answer: C`）。
- `core` 是去掉所有修饰后的主干，能一行写完；不确定就先写主谓宾再删。
- `layers` 的最后一条建议写"做题动作"（如"判断题遇到 but，答案几乎总在 but 之后"）。

## 与题库的对应

`questions.py` 里每篇一个 `*_ANSWERS` 字典，键为题号、值为答案字符串。
`teach_*.py` 的 `ans` 必须与之**逐字相同**（含 `NOT GIVEN` 的空格、`(airborne) flying fish` 的括号）。
`verify.check_pool()` 会逐题比对。
