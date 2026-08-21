# 托福基础写作 · Academic Discussion 第 2 课｜课堂 PPT

课堂投影用 PPT，101 页，按《AD 第2课 PPT + 打印材料生成 Prompt（官方TPO版本）》生成。

**产出文件：`托福基础写作-AD第2课-课堂PPT.pptx`**

---

## 一、官方题目来源（全部逐字引用，未自编、未改写）

| 用途 | 出处 | 题目 |
|---|---|---|
| 课堂主题（Part 2–6） | TOEFL iBT Writing · Write for an Academic Discussion（2026 TPO 官方界面截图，第 16 屏） | Dr. Gupta（sociology）：social mobility — education vs. networking / personal connections。Student A = Kelly（教育派），Student B = Andrew（人脉派） |
| 作业题（韩 / 刘 / 钟） | 同上，第 96 屏 | Dr. Diaz（marketing）：social media influencers vs. traditional advertising。Kelly / Andrew 原文 |
| 官方对 contribution 的说明 | ETS《TOEFL iBT Writing Practice Questions》Practice Set 2 · Response Tips | "Be sure to add your own perspective to the discussion, not merely repeat ideas that have already been stated." |
| 官方对展开与语言的要求 | 同上 | "A well-developed response will contain clearly appropriate reasons, examples, and details…" |

选题依据：Prompt 要求避开政治 / 抽象哲学 / 过于专业的科学，优先 education / society / student experience。
6 道官方 AD 题中，philosophy（free will）、economics（UBI）、anthropology（rituals）被排除，
sociology 这道「教育 vs 人脉」既在优先主题内，争议结构也最清晰，适合基础班。

**Part 3 的三篇 3 / 4 / 5 分范文是教学模拟范文**，每一页都标注
`Teacher-created sample based on ETS rubric`，PPT 里另有一整页声明它们不是 ETS 官方已评分考生作文。

## 二、课堂结构（125 分钟）

| Part | 页码 | 时长 | 内容 |
|---|---|---|---|
| 开场 | 1–5 | — | 目标 / 路线图 / 核心流程闭环 |
| Part 1 Warm-up | 6–13 | 10′ | 唤醒第 1 课方法，三个空（Reason / Why / Example） |
| Part 2 官方新题 | 14–25 | 20′ | 官方指令 → 教授问题 → Student A/B → 填表 → 定立场 |
| Part 3 3/4/5 分 | 26–47 | 25′ | 圈五要素 → 自己打分 → 讲评 → 3→4→5 的跳跃点 |
| Part 4 展开训练 | 48–70 | 30′ | 9 组练习，难度递进：具体理由 → WHY → Example → Result → 完整链条 |
| Part 5 Contribution | 71–85 | 20′ | Agree + Add ×2、Disagree + Explain ×2 |
| Part 6 Full Writing | 86–95 | 20′ | Planning Box → 10 分钟写作 → 自查 → 互评 |
| 作业 & 收尾 | 96–101 | — | 分层作业、官方作业题、一页带走、Exit Ticket |

## 三、对照 Prompt 的执行情况

- **100 页左右** → 101 页
- **正文字号 ≥ 18.5** → 所有正文 ≥ 19pt（`qa_check.py` 逐 run 校验）
- **每 5–8 页一次输出** → 40 个互动 / 输出页，最大间隔 8 页（脚本校验）
- **示例 → 模仿 → 迁移** → 每组练习前先给 `✕ 反例 / √ 正例`，不写「展开你的观点」这类抽象指令
- **Part 4 至少 6 组练习** → 9 组（练习 1、1续、2、2续、3、3续、4、5、6）
- **Part 5 至少 4 题** → 4 题（2 Agree + Add，2 Disagree + Explain）
- **分层** → 彭子骞：概念对齐页（Reason / Example / Contribution 是什么）＋ 五句支架版 ＋ 基础作业；
  韩 / 刘 / 钟：挑战版四条要求 ＋ 官方新题限时作业
- **不教背范文** → 全课围绕「同一个理由推几层」，范文只做对照，不做背诵材料

70 页带教师备注（讲法、限时、点名顺序、可砍环节），放映时按 `演示者视图` 查看。

## 四、重新生成

```bash
pip install python-pptx pillow
python3 build_deck.py          # 输出 pptx
python3 qa_check.py 托福基础写作-AD第2课-课堂PPT.pptx   # 版式与字号校验
python3 preview.py 托福基础写作-AD第2课-课堂PPT.pptx out 1,17,36   # 粗略位图预览
```

| 文件 | 作用 |
|---|---|
| `deck_engine.py` | 版式引擎：配色、标题、卡片、书写线、文本测量 |
| `build_deck.py` | 全部课程内容与逐页版式 |
| `qa_check.py` | 检查文字溢出、元素重叠、正文字号 < 18.5pt |
| `preview.py` | 无 LibreOffice 环境下的粗略位图预览 |

字体：正文 Segoe UI + 微软雅黑。换机器放映时若无微软雅黑，换成思源黑体 / 苹方即可。
