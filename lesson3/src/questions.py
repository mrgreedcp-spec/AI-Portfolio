# -*- coding: utf-8 -*-
"""第三节课题目与答案（题目、编号、答案均与所给材料完全一致，未做任何改动）。

题号严格沿用 PDF 讲义：
    Passage 1  Q1–13
    Passage 2  Q15–26        （PDF 该篇标注为 Questions 15–26）
    Passage 3  Q27–40
    Passage 4  Q1–13         （课后作业，另起编号）
    Pencil 流程图版 Q1–8      （第二节课留作第三节课课前延迟检索）
"""

# =============================================================== PASSAGE 1
P1_Q1_6_HEAD = "Questions 1–6 · TRUE / FALSE / NOT GIVEN"
P1_Q1_6_INS = ("Do the following statements agree with the information given in Reading Passage 1? "
               "Write TRUE if the statement agrees with the information, FALSE if the statement "
               "contradicts the information, NOT GIVEN if there is no information on this.")
P1_Q1_6 = [
    (1, "Modern official athletic records date from about 1900."),
    (2, "There was little improvement in athletic performance before the twentieth century."),
    (3, "Performance has improved most greatly in events requiring an intensive burst of energy."),
    (4, "Improvements in athletic performance can be fully explained by genetics."),
    (5, "The parents of top athletes have often been successful athletes themselves."),
    (6, "The growing international importance of athletics means that gifted athletes can be recognised at a younger age."),
]

P1_Q7_10_HEAD = "Questions 7–10 · Sentence Completion"
P1_Q7_10_INS = ("Complete the sentences below with words taken from Reading Passage 1. "
                "Use ONE WORD for each answer.")
P1_Q7_10 = [
    (7, "According to Professor Yessis, American runners are relying for their current success on ……………"),
    (8, "Yessis describes a training approach from the former Soviet Union that aims to develop an athlete's ……………"),
    (9, "Yessis links an inadequate diet to ……………"),
    (10, "Yessis claims that the key to setting new records is better ……………"),
]

P1_Q11_13_HEAD = "Questions 11–13 · Multiple Choice"
P1_Q11_13_INS = "Choose the correct letter, A, B, C or D."
P1_Q11_13 = [
    (11, "Biomechanics films are proving particularly useful because they enable trainers to",
     ["highlight areas for improvement in athletes.", "assess the fitness levels of athletes.",
      "select top athletes.", "predict the success of athletes."]),
    (12, "Biomechanics specialists used theoretical models to",
     ["soften the Fosbury flop.", "create the Fosbury flop.",
      "correct the Fosbury flop.", "explain the Fosbury flop."]),
    (13, "John S. Raglin believes our current knowledge of athletics is",
     ["mistaken.", "basic.", "diverse.", "theoretical."]),
]

P1_ANSWERS = {
    1: "TRUE", 2: "NOT GIVEN", 3: "FALSE", 4: "FALSE", 5: "NOT GIVEN", 6: "TRUE",
    7: "genetics", 8: "power", 9: "injuries", 10: "training",
    11: "A", 12: "D", 13: "B",
}

# =============================================================== PASSAGE 2
P2_Q15_21_HEAD = "Questions 15–21 · Table Completion"
P2_Q15_21_INS = ("Complete the table below. Choose NO MORE THAN THREE WORDS from Reading Passage 2 "
                 "for each answer.")
# (SENSE, SPECIES, ABILITY, COMMENTS) —— 与 PDF 表格逐格一致
P2_TABLE = [
    ("SENSE", "SPECIES", "ABILITY", "COMMENTS"),
    ("Smell", "toothed", "no", "evidence from brain structure"),
    ("", "baleen", "not certain", "related brain structures are present"),
    ("Taste", "some types", "poor", "nerves linked to their 15 …………… are underdeveloped"),
    ("Touch", "all", "yes", "region around the blowhole very sensitive"),
    ("Vision", "16 ……………", "yes", "probably do not have stereoscopic vision"),
    ("", "dolphins, porpoises", "yes", "probably have stereoscopic vision 17 …………… and ……………"),
    ("", "18 ……………", "yes", "probably have stereoscopic vision forward and upward"),
    ("", "bottlenose dolphins", "yes", "exceptional in 19 …………… and good in air-water interface"),
    ("", "boutu and beiji", "poor", "have limited vision"),
    ("", "Indian susus", "no", "probably only sense direction and intensity of light"),
    ("Hearing", "most large baleen", "yes", "usually use 20 ……………; repertoire limited"),
    ("", "21 …………… whales and …………… whales", "yes", "song-like"),
    ("", "toothed", "yes", "use more of frequency spectrum; have wider repertoire"),
]
P2_TABLE_NOTE = ("注：第 21 行原书印作 “bowhead whales and humpback whales”，只有第一个空编号为 21；"
                 "第二处点线是原书 humpback 的印刷位置，不是考点。")

P2_Q22_26_HEAD = "Questions 22–26 · Short-answer Questions"
P2_Q22_26_INS = "Answer the questions below using NO MORE THAN THREE WORDS from the passage for each answer."
P2_Q22_26 = [
    (22, "Which of the senses is described here as being involved in mating?"),
    (23, "Which species swims upside down while eating?"),
    (24, "What can bottlenose dolphins follow from under the water?"),
    (25, "Which type of habitat is related to good visual ability?"),
    (26, "Which of the senses is best developed in cetaceans?"),
]

P2_ANSWERS = {
    15: "taste buds", 16: "baleen whales", 17: "forward and downward",
    18: "freshwater dolphins", 19: "water", 20: "lower frequencies", 21: "bowhead",
    22: "touch", 23: "freshwater dolphins", 24: "(airborne) flying fish",
    25: "clear open waters", 26: "hearing / acoustic sense",
}

# =============================================================== PASSAGE 3
P3_Q27_29_HEAD = "Questions 27–29 · Multiple Choice"
P3_Q27_29_INS = "Choose the correct letter, A, B, C or D."
P3_Q27_29 = [
    (27, "In the first paragraph the writer makes the point that blind people",
     ["may be interested in studying art.", "can draw outlines of different objects and surfaces.",
      "can recognise conventions such as perspective.", "can draw accurately."]),
    (28, "The writer was surprised because the blind woman",
     ["drew a circle on her own initiative.", "did not understand what a wheel looked like.",
      "included a symbol representing movement.", "was the first person to use lines of motion."]),
    (29, "From the experiment described in Part 1, the writer found that the blind subjects",
     ["had good understanding of symbols representing movement.",
      "could control the movement of wheels very accurately.",
      "worked together well as a group in solving problems.",
      "got better results than the sighted undergraduates."]),
]

P3_Q30_32_HEAD = "Questions 30–32 · Diagram Matching"
P3_Q30_32_INS = ("Look at the following diagrams (Questions 30–32), and the list of types of movement below. "
                 "Match each diagram to the type of movement A–E generally assigned to it in the experiment.")
# 图示描述（原图为三个轮子，轮辐画法不同）
P3_DIAGRAMS = [
    (30, "轮辐为直线，且伸出轮圈之外", "spokes drawn as straight lines extending beyond the rim"),
    (31, "轮辐为虚线（断续线）", "spokes drawn as dashed lines"),
    (32, "轮辐为弯曲的弧线", "spokes drawn as curved lines"),
]
P3_MOVE_LIST = [
    ("A", "steady spinning"), ("B", "jerky movement"), ("C", "rapid spinning"),
    ("D", "wobbling movement"), ("E", "use of brakes"),
]

P3_Q33_39_HEAD = "Questions 33–39 · Summary Completion (word box)"
P3_Q33_39_INS = "Complete the summary below using words from the box. NB You may use any word more than once."
P3_SUMMARY = (
    "In the experiment described in Part 2, a set of word 33 …… was used to investigate whether blind and "
    "sighted people perceived the symbolism in abstract 34 …… in the same way. Subjects were asked which "
    "word fitted best with a circle and which with a square. From the 35 …… volunteers, everyone thought a "
    "circle fitted 'soft' while a square fitted 'hard'. However, only 51% of the 36 …… volunteers assigned a "
    "circle to 37 ……. When the test was later repeated with 38 …… volunteers, it was found that they made "
    "39 …… choices."
)
P3_WORD_BOX = ["associations", "blind", "deep", "hard", "hundred", "identical", "pairs",
               "shapes", "sighted", "similar", "shallow", "soft", "words"]

P3_Q40_HEAD = "Question 40 · Multiple Choice"
P3_Q40_INS = "Choose the correct letter, A, B, C or D."
P3_Q40 = (40, "Which of the following statements best summarises the writer's general conclusion?",
          ["The blind represent some aspects of reality differently from sighted people.",
           "The blind comprehend visual metaphors in similar ways to sighted people.",
           "The blind may create unusual and effective symbols to represent reality.",
           "The blind may be successful artists if given the right training."])

P3_ANSWERS = {
    27: "C", 28: "C", 29: "A",
    30: "E", 31: "C", 32: "A",
    33: "pairs", 34: "shapes", 35: "sighted", 36: "sighted", 37: "deep",
    38: "blind", 39: "similar",
    40: "B",
}

# =============================================================== PASSAGE 4
P4_Q1_5_HEAD = "Questions 1–5 · TRUE / FALSE / NOT GIVEN"
P4_Q1_5_INS = ("Do the following statements agree with the information given in Reading Passage 1? "
               "Write TRUE, FALSE or NOT GIVEN.")
P4_Q1_5 = [
    (1, "In Robert FitzRoy's time, weather forecasting was a respected skill."),
    (2, "When FitzRoy retired from the navy, he had already had a successful career at sea."),
    (3, "FitzRoy faced competition from other applicants for the chief statistician's job."),
    (4, "The British Parliament supported the idea of regular weather forecasts in 1854."),
    (5, "Progress in technology made it a good time for publicly available weather forecasting to begin."),
]

P4_Q6_13_HEAD = "Questions 6–13 · Notes Completion"
P4_Q6_13_INS = "Complete the notes below. Choose ONE WORD ONLY from the passage for each answer."
P4_NOTES = [
    ("H", "February 1861: Storm warning service"),
    ("B", "FitzRoy received weather reports produced by ships using reliable 6 ………………"),
    ("B", "simultaneous weather reports were taken daily"),
    ("B", "storm warnings were telegraphed to 7 ……………… along the shore"),
    ("B", "signals for ships were displayed using raised 8 ………………"),
    ("B", "the storm warning service was the greatest development in sea safety since the 9 ……………… was introduced"),
    ("H", "August 1861: Public weather forecasting service"),
    ("B", "very popular in The Times newspaper"),
    ("B", "frequently used by the English Queen for safe trips to a favourite 10 ………………"),
    ("B", "FitzRoy's forecasts were popular with fishermen but not with boat 11 ………………"),
    ("B", "in modern times FitzRoy's 12 ……………… is used for a marine area"),
    ("B", "FitzRoy produced a 13 ……………… which was respected by the scientific community"),
]

P4_ANSWERS = {
    1: "FALSE", 2: "TRUE", 3: "NOT GIVEN", 4: "FALSE", 5: "TRUE",
    6: "instruments", 7: "ports", 8: "flags", 9: "lifeboat",
    10: "island", 11: "owners", 12: "name", 13: "book",
}

# ============================ 第二节课作业复盘：The Development of Plastics
P0_LEAD = ("The Development of Plastics 是第二节课布置的课后独立作业。"
           "本节课开场先复盘：表格填空考“属性 / 用途 / 国别”的行列定位，"
           "判断题考化学关系与程度词。")

P0_Q1_7_HEAD = "Questions 1–7 · Table Completion"
P0_Q1_7_INS = ("Complete the table below. Choose NO MORE THAN THREE WORDS from the passage "
               "for each answer.")
P0_TABLE_TITLE = "Early types of plastic"
# (Name, Date, Country of origin, Properties, Common uses) —— 与所给 PDF 逐格一致
P0_TABLE = [
    ("Name", "Date", "Country of origin", "Properties", "Common uses"),
    ("Celluloid", "1860s", "USA", "can be soften and reshaped by heat",
     "•  billiard balls (original use)\n•  cutlery\n•  clothing\n•  1 ………………"),
    ("2 ………………", "1907", "USA",
     "can't be softened after setting; good insulator; resistant to water and acid",
     "•  3 ………………\n•  household object"),
    ("Polythene", "1930s", "4 ………………", "can be softened and reshaped by heat",
     "•  bottles\n•  pipes\n•  plastic bags"),
    ("Polypropylene", "1950s", "", "", "•  bottles\n•  pipes\n•  plastic bags"),
    ("Rigid PVC", "", "", "is 5 ………………", "•  external piping"),
    ("Soft PVC", "", "", "", "•  outdoor clothing"),
    ("Polystyrene", "1930s", "Germany", "resembles 6 ………………",
     "•  food containers\n•  toy"),
    ("Polyurethane", "", "Germany", "usually manufactured as a 7 ………………", "•  insulation"),
]

P0_Q8_13_HEAD = "Questions 8–13 · TRUE / FALSE / NOT GIVEN"
P0_Q8_13_INS = ("Do the following statements agree with the information in Reading Passage 1? "
                "Write TRUE if the statement agrees with the information, FALSE if the statement "
                "contradicts the information, NOT GIVEN if there is no information about this.")
P0_Q8_13 = [
    (8, "The chemical structure of rubber is very different from that of plastics."),
    (9, "John Wesley Hyatt was an industrial chemist."),
    (10, "Celluloid and Bakelite react in the same way to heat."),
    (11, "If an object is made of several plastics, these prove hard to break down and reuse."),
    (12, "Adding starch to plastic makes it more durable."),
    (13, "Containers which are designed to decompose need particular storage conditions."),
]

P0_ANSWERS = {
    1: "photographic film", 2: "Bakelite", 3: "electrical switches", 4: "Britain",
    5: "fireproof", 6: "glass", 7: "foam",
    8: "FALSE", 9: "NOT GIVEN", 10: "FALSE", 11: "TRUE", 12: "FALSE", 13: "TRUE",
}
