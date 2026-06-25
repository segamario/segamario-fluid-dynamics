from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import copy

# Hanwha brand colors
HW_ORANGE = RGBColor(0xFF, 0x66, 0x00)   # Hanwha orange
HW_NAVY   = RGBColor(0x1A, 0x2E, 0x4A)   # dark navy
HW_DARK   = RGBColor(0x1A, 0x1A, 0x1A)
HW_GRAY   = RGBColor(0x55, 0x55, 0x55)
HW_LGRAY  = RGBColor(0xF2, 0xF2, 0xF2)
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
HW_ACCENT = RGBColor(0xFF, 0x99, 0x33)   # lighter orange

W = Inches(13.33)  # widescreen 16:9
H = Inches(7.5)

prs = Presentation()
prs.slide_width  = W
prs.slide_height = H

BLANK = prs.slide_layouts[6]  # completely blank

# ─────────────────────────────────────────────
# helpers
# ─────────────────────────────────────────────
def add_rect(slide, l, t, w, h, fill_rgb=None, line_rgb=None, line_width=None):
    shape = slide.shapes.add_shape(1, l, t, w, h)
    shape.line.fill.background()
    if fill_rgb:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_rgb
    else:
        shape.fill.background()
    if line_rgb:
        shape.line.color.rgb = line_rgb
        if line_width:
            shape.line.width = line_width
    else:
        shape.line.fill.background()
    return shape

def add_text(slide, text, l, t, w, h,
             font_size=18, bold=False, color=HW_DARK,
             align=PP_ALIGN.LEFT, wrap=True):
    txb = slide.shapes.add_textbox(l, t, w, h)
    txb.word_wrap = wrap
    tf  = txb.text_frame
    tf.word_wrap = wrap
    p   = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = "맑은 고딕"
    return txb

def add_multiline(slide, lines, l, t, w, h,
                  font_size=16, bold=False, color=HW_DARK,
                  align=PP_ALIGN.LEFT, line_spacing=1.2):
    txb = slide.shapes.add_textbox(l, t, w, h)
    txb.word_wrap = True
    tf  = txb.text_frame
    tf.word_wrap = True
    first = True
    for line_text in lines:
        if first:
            p = tf.paragraphs[0]
            first = False
        else:
            p = tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(4)
        run = p.add_run()
        run.text = line_text
        run.font.size = Pt(font_size)
        run.font.bold = bold
        run.font.color.rgb = color
        run.font.name = "맑은 고딕"
    return txb

def slide_header(slide, title, subtitle=None, accent_bar=True):
    """Top navy bar + title."""
    # navy header bar
    add_rect(slide, 0, 0, W, Inches(1.1), fill_rgb=HW_NAVY)
    # orange accent left strip
    if accent_bar:
        add_rect(slide, 0, 0, Inches(0.08), Inches(1.1), fill_rgb=HW_ORANGE)
    # title
    add_text(slide, title,
             Inches(0.25), Inches(0.12), Inches(10), Inches(0.7),
             font_size=28, bold=True, color=WHITE)
    if subtitle:
        add_text(slide, subtitle,
                 Inches(0.25), Inches(0.75), Inches(10), Inches(0.35),
                 font_size=14, bold=False, color=HW_ACCENT)
    # slide bottom bar
    add_rect(slide, 0, Inches(7.2), W, Inches(0.3), fill_rgb=HW_NAVY)
    add_text(slide, "홍창기 | 한화시스템 전략부문",
             Inches(0.2), Inches(7.22), Inches(6), Inches(0.25),
             font_size=10, color=WHITE, align=PP_ALIGN.LEFT)
    add_text(slide, "2026",
             Inches(12.5), Inches(7.22), Inches(0.8), Inches(0.25),
             font_size=10, color=WHITE, align=PP_ALIGN.RIGHT)

def kpi_box(slide, l, t, w, h, number, label, sublabel=""):
    add_rect(slide, l, t, w, h, fill_rgb=HW_NAVY)
    add_rect(slide, l, t, Inches(0.06), h, fill_rgb=HW_ORANGE)
    add_text(slide, number, l+Inches(0.15), t+Inches(0.08), w-Inches(0.2), Inches(0.6),
             font_size=30, bold=True, color=HW_ACCENT, align=PP_ALIGN.CENTER)
    add_text(slide, label, l+Inches(0.1), t+Inches(0.65), w-Inches(0.15), Inches(0.4),
             font_size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    if sublabel:
        add_text(slide, sublabel, l+Inches(0.1), t+Inches(1.0), w-Inches(0.15), Inches(0.4),
                 font_size=11, color=HW_ACCENT, align=PP_ALIGN.CENTER)

def tag_box(slide, l, t, w, h, text, fill=HW_ORANGE, txt_color=WHITE, fs=13):
    add_rect(slide, l, t, w, h, fill_rgb=fill)
    add_text(slide, text, l, t, w, h, font_size=fs, bold=True,
             color=txt_color, align=PP_ALIGN.CENTER)

# ═══════════════════════════════════════════════════
# SLIDE 1 — Title
# ═══════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)

# full navy background
add_rect(sl, 0, 0, W, H, fill_rgb=HW_NAVY)
# orange left bar
add_rect(sl, 0, 0, Inches(0.25), H, fill_rgb=HW_ORANGE)
# large orange accent block bottom-right
add_rect(sl, Inches(9.5), Inches(5.5), Inches(3.83), Inches(2.0), fill_rgb=HW_ORANGE)

add_text(sl, "한화시스템 전략부문",
         Inches(0.5), Inches(1.2), Inches(10), Inches(0.6),
         font_size=20, color=HW_ACCENT)

add_text(sl, "AI Factory 전략 전문가\n홍 창 기",
         Inches(0.5), Inches(1.9), Inches(11), Inches(1.8),
         font_size=46, bold=True, color=WHITE)

add_multiline(sl, [
    "LG전자 생산기술원 전략담당 | 제조혁신 Task Leader (2018~현재)",
    "성균관대학교 기계공학 박사 (CFD/열유체)",
    "그룹 AX Factory 전략 수립 → C-Level 보고 전 사이클 경험",
], Inches(0.5), Inches(3.9), Inches(9), Inches(1.5),
   font_size=16, color=RGBColor(0xCC, 0xCC, 0xCC))

# KPIs bottom
for i, (num, lbl) in enumerate([
    ("30일→15분", "AI 설계 예측"),
    ("90% ↓", "인정시험 감소"),
    ("10h→1분", "사출 해석"),
]):
    kpi_box(sl,
            Inches(0.5 + i*3.1), Inches(5.6),
            Inches(2.8), Inches(1.3),
            num, lbl)

# ═══════════════════════════════════════════════════
# SLIDE 2 — 자기소개 / 경력 타임라인
# ═══════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)
add_rect(sl, 0, 0, W, H, fill_rgb=WHITE)
slide_header(sl, "자기소개", "기술에서 전략으로 — 8년의 여정")

# timeline bar
add_rect(sl, Inches(0.3), Inches(3.4), Inches(12.5), Inches(0.06), fill_rgb=HW_ORANGE)

timeline = [
    ("박사 과정\n2011~2018", "성균관대\n기계공학 (CFD)\n오일샌드 국책과제\n국토부 장관표창"),
    ("기술 전문가\n2018~2021", "LG전자\n생산기술원\nCFD 해석 → AI\n성능예측 모델"),
    ("전략 기획\n2022~2024", "LG그룹\n스마트팩토리 2.0\nEY컨설팅 협업\nVIP 보고"),
    ("MI Task Leader\n2025~현재", "그룹 제조혁신\n협의회 총괄\nPhysical AI 전략\nAX Factory 로드맵"),
]

colors = [HW_LGRAY, HW_LGRAY, RGBColor(0xFF, 0xEE, 0xDD), HW_ORANGE]
txt_colors = [HW_DARK, HW_DARK, HW_DARK, WHITE]

for i, (title, body) in enumerate(timeline):
    x = Inches(0.4 + i * 3.15)
    # dot on timeline
    dot = sl.shapes.add_shape(9, x + Inches(1.2), Inches(3.25), Inches(0.22), Inches(0.22))
    dot.fill.solid(); dot.fill.fore_color.rgb = HW_ORANGE
    dot.line.fill.background()
    # box
    add_rect(sl, x, Inches(3.6), Inches(2.9), Inches(2.8), fill_rgb=colors[i])
    add_text(sl, title, x+Inches(0.1), Inches(3.65), Inches(2.7), Inches(0.55),
             font_size=13, bold=True, color=txt_colors[i])
    add_multiline(sl, body.split("\n"),
                  x+Inches(0.1), Inches(4.2), Inches(2.7), Inches(1.9),
                  font_size=12, color=txt_colors[i])

add_text(sl, "핵심 역량: CAE (CFX/Fluent) · AI/ML/DL · 그룹 전략 기획 · C-Level 보고 · 계열사 코디네이션",
         Inches(0.4), Inches(6.55), Inches(12.5), Inches(0.5),
         font_size=13, bold=True, color=HW_NAVY, align=PP_ALIGN.CENTER)
add_rect(sl, Inches(0.4), Inches(6.5), Inches(12.5), Inches(0.55),
         fill_rgb=HW_LGRAY)
add_text(sl, "핵심 역량: CAE (CFX/Fluent) · AI/ML/DL · 그룹 전략 기획 · C-Level 보고 · 계열사 코디네이션",
         Inches(0.4), Inches(6.55), Inches(12.5), Inches(0.5),
         font_size=13, bold=True, color=HW_NAVY, align=PP_ALIGN.CENTER)

# ═══════════════════════════════════════════════════
# SLIDE 3 — 지원 동기
# ═══════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)
add_rect(sl, 0, 0, W, H, fill_rgb=WHITE)
slide_header(sl, "지원 동기", "왜 한화시스템인가 — 위기 속 기회")

boxes = [
    ("⚠ 시장 위기", HW_LGRAY, HW_DARK,
     ["국내 소비재·가전 제조업",
      "중국의 '규모의 경제'에",
      "글로벌 시장 지위 위협",
      "",
      "단순 원가 경쟁 → 한계"]),
    ("→ 대응 전략", RGBColor(0xFF, 0xEE, 0xDD), HW_DARK,
     ["단기 추격 불가능한",
      "고신뢰성 산업 집중",
      "(방산·항공·바이오)",
      "",
      "AI Factory + 실용주의\n제조혁신 융합"]),
    ("✓ 기여 포인트", HW_ORANGE, WHITE,
     ["트렌드 센싱",
      "계열사 코디네이션",
      "임원진 소통",
      "",
      "LG 검증 방법론을\n한화에 즉시 적용"]),
]

for i, (title, bg, tc, lines) in enumerate(boxes):
    x = Inches(0.4 + i*4.28)
    add_rect(sl, x, Inches(1.3), Inches(4.0), Inches(5.6), fill_rgb=bg)
    add_rect(sl, x, Inches(1.3), Inches(4.0), Inches(0.55), fill_rgb=HW_NAVY if i<2 else RGBColor(0xCC,0x44,0x00))
    add_text(sl, title, x+Inches(0.15), Inches(1.33), Inches(3.7), Inches(0.5),
             font_size=16, bold=True, color=WHITE)
    add_multiline(sl, lines, x+Inches(0.2), Inches(2.0), Inches(3.6), Inches(3.5),
                  font_size=14, color=tc, line_spacing=1.4)

add_text(sl,
         "\"소비재를 넘어, 더 높은 신뢰성이 요구되는 방산·항공에서 AI Factory를 완성하고 싶습니다.\"",
         Inches(0.5), Inches(6.8), Inches(12.3), Inches(0.5),
         font_size=14, bold=True, color=HW_NAVY, align=PP_ALIGN.CENTER)

# ═══════════════════════════════════════════════════
# SLIDE 4 — AI 성과 3건 (숫자 강조)
# ═══════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)
add_rect(sl, 0, 0, W, H, fill_rgb=WHITE)
slide_header(sl, "핵심 성과 ①  AI Factory 현장 실증", "전략이 아닌 수치로 증명한 AI 제조 혁신")

cases = [
    {
        "tag": "TV Stand",
        "kpi": "30일 → 15분",
        "sub": "CAE 성능예측 시간",
        "tech": "AI Inverse Net.\n(Generative Design)",
        "detail": ["• TV 낙하 해석 자동화 (Altair협업)",
                   "• Forward Net → Inverse Net 개발",
                   "• 1,000개 이상 형상 자동 추천",
                   "• CAE 엔지니어 고부가 업무 전환"],
    },
    {
        "tag": "김치냉장고",
        "kpi": "인정시험 90%↓",
        "sub": "1만 Case → 800건 이내",
        "tech": "AI Surrogate Model\n(시험 데이터 기반)",
        "detail": ["• 외기조건·제어신호·센서온도 학습",
                   "• 80%+ 정확도 예측",
                   "• Grid Search 최소 시험조건 도출",
                   "• 챔버 유휴 활용률 증가"],
    },
    {
        "tag": "사출성형",
        "kpi": "10시간 → 1분",
        "sub": "사출 CAE 해석 시간",
        "tech": "GCNN + MLOps\n(3D CAD 기반)",
        "detail": ["• 3D CAD + Moldflow 데이터 파싱",
                   "• Geodesic CNN (Scale 불변)",
                   "• MLOps 지속 업데이트 시스템",
                   "• CAE 엔지니어 역할 재정의"],
    },
]

for i, c in enumerate(cases):
    x = Inches(0.35 + i*4.35)
    # card bg
    add_rect(sl, x, Inches(1.25), Inches(4.1), Inches(5.65), fill_rgb=HW_LGRAY)
    # tag
    tag_box(sl, x, Inches(1.25), Inches(4.1), Inches(0.45), c["tag"], fill=HW_NAVY)
    # KPI
    add_text(sl, c["kpi"], x+Inches(0.1), Inches(1.75), Inches(3.9), Inches(0.75),
             font_size=28, bold=True, color=HW_ORANGE, align=PP_ALIGN.CENTER)
    add_text(sl, c["sub"], x+Inches(0.1), Inches(2.45), Inches(3.9), Inches(0.35),
             font_size=12, color=HW_GRAY, align=PP_ALIGN.CENTER)
    # tech badge
    add_rect(sl, x+Inches(0.2), Inches(2.85), Inches(3.7), Inches(0.6),
             fill_rgb=HW_NAVY)
    add_text(sl, c["tech"], x+Inches(0.2), Inches(2.87), Inches(3.7), Inches(0.6),
             font_size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    # detail
    add_multiline(sl, c["detail"], x+Inches(0.15), Inches(3.55), Inches(3.8), Inches(2.5),
                  font_size=12, color=HW_DARK)

add_text(sl,
         "한화 적용 → 방산 부품 품질검사 · 항공 구조 해석 대체 · ICT 공정 최적화에 동일 방법론 즉시 적용 가능",
         Inches(0.4), Inches(6.8), Inches(12.5), Inches(0.4),
         font_size=12, bold=True, color=HW_NAVY, align=PP_ALIGN.CENTER)
add_rect(sl, Inches(0.4), Inches(6.75), Inches(12.5), Inches(0.42),
         fill_rgb=RGBColor(0xFF,0xEE,0xDD))
add_text(sl,
         "한화 적용 → 방산 부품 품질검사 · 항공 구조 해석 대체 · ICT 공정 최적화에 동일 방법론 즉시 적용 가능",
         Inches(0.4), Inches(6.78), Inches(12.5), Inches(0.4),
         font_size=12, bold=True, color=HW_NAVY, align=PP_ALIGN.CENTER)

# ═══════════════════════════════════════════════════
# SLIDE 5 — 그룹 전략 기획 트랙
# ═══════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)
add_rect(sl, 0, 0, W, H, fill_rgb=WHITE)
slide_header(sl, "핵심 성과 ②  그룹 전략 기획 & C-Level 소통", "기술을 전략 언어로 번역해 임원진을 움직인 경험")

steps = [
    ("2020~2021", "그룹 C4협의회", "전자·에솔·이노텍·\n디스플레이·CNS\nTangible Asset\n4건 계열사 확산"),
    ("2023", "Smart Factory 2.0\nVIP 보고", "EY컨설팅 협업\nCAPEX/OPEX\n절감 전략\n사장단협의회"),
    ("2024", "그룹 제조혁신\n전략 / Beyond China", "AI기반 전략\nVIP 보고\n중국 SCM 활용\n대응전략 도출"),
    ("2025~", "MI Task Leader\n그룹협의회 통합", "7개 계열사 조율\nC-Level 직접 보고\nPhysical AI·DT\n신규 분과 운영"),
]

arrow_y = Inches(3.2)
for i, (year, title, body) in enumerate(steps):
    x = Inches(0.3 + i * 3.2)
    is_last = (i == len(steps)-1)
    bg = HW_ORANGE if is_last else HW_NAVY
    # year tag
    tag_box(sl, x, Inches(1.3), Inches(2.8), Inches(0.42), year,
            fill=HW_ORANGE if is_last else HW_GRAY,
            txt_color=WHITE, fs=12)
    # box
    add_rect(sl, x, Inches(1.72), Inches(2.8), Inches(4.1), fill_rgb=HW_NAVY if is_last else HW_LGRAY)
    add_text(sl, title, x+Inches(0.1), Inches(1.78), Inches(2.6), Inches(0.75),
             font_size=13, bold=True, color=WHITE if is_last else HW_NAVY)
    add_multiline(sl, body.split("\n"), x+Inches(0.12), Inches(2.55), Inches(2.6), Inches(2.8),
                  font_size=12, color=WHITE if is_last else HW_DARK)
    # arrow
    if i < len(steps)-1:
        arr = sl.shapes.add_shape(13,
            x+Inches(2.85), Inches(3.1), Inches(0.35), Inches(0.35))
        arr.fill.solid(); arr.fill.fore_color.rgb = HW_ORANGE
        arr.line.fill.background()

# bottom summary
add_rect(sl, Inches(0.3), Inches(6.1), Inches(12.7), Inches(0.85), fill_rgb=HW_NAVY)
add_multiline(sl, [
    "EY컨설팅 협업  ·  7개 계열사 이해관계 조율  ·  VIP/사장단 보고 반복 경험",
    "→ 한화그룹 AX 협의체 설계 및 계열사 확산 전략 즉시 수행 가능",
], Inches(0.5), Inches(6.15), Inches(12.3), Inches(0.8),
   font_size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

# ═══════════════════════════════════════════════════
# SLIDE 6 — 한화 AX Factory 기여 방안
# ═══════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)
add_rect(sl, 0, 0, W, H, fill_rgb=WHITE)
slide_header(sl, "한화 AX Factory 기여 방안", "LG에서 증명한 것을 한화에서 더 빠르게")

contribs = [
    ("① AX 로드맵 설계",
     ["한화에어로스페이스·한화오션·\n한화솔루션 등 계열사 특성별",
      "AX Factory 로드맵 수립",
      "",
      "ROI 기반 우선순위 설정",
      "→ 맹목적 자동화 방지",
      "→ LCC/고신뢰 공장 차별 전략"]),
    ("② 기술 ↔ 전략 브릿지",
     ["CAE·AI·Digital Twin 기술을",
      "전략 언어로 번역",
      "",
      "현장 엔지니어 ↔ 임원 가교",
      "실현 가능성 기반 전략 설계",
      "→ 투자 실패 리스크 최소화"]),
    ("③ Physical AI 선제 적용",
     ["2026년 직접 수립한",
      "Physical AI · Agentic AI · DT",
      "전략을 방산·항공 제조에 적용",
      "",
      "무인화 · AI 의사결정 체계",
      "→ 한화 AX Factory 선도"]),
]

for i, (title, lines) in enumerate(contribs):
    x = Inches(0.35 + i*4.35)
    add_rect(sl, x, Inches(1.25), Inches(4.1), Inches(5.2), fill_rgb=HW_LGRAY)
    add_rect(sl, x, Inches(1.25), Inches(0.08), Inches(5.2), fill_rgb=HW_ORANGE)
    tag_box(sl, x, Inches(1.25), Inches(4.1), Inches(0.5), title,
            fill=HW_NAVY, txt_color=WHITE, fs=14)
    add_multiline(sl, lines, x+Inches(0.15), Inches(1.85), Inches(3.8), Inches(4.0),
                  font_size=13, color=HW_DARK, line_spacing=1.3)

# differentiator box
add_rect(sl, Inches(0.35), Inches(6.55), Inches(12.6), Inches(0.62), fill_rgb=HW_ORANGE)
add_text(sl,
         "차별점: LG에서 '그룹 전략 수립 → 계열사 실행 → 성과 측정 → VIP 보고' 전 사이클 직접 경험 → 한화에서 학습 없이 즉시 실행",
         Inches(0.5), Inches(6.6), Inches(12.2), Inches(0.55),
         font_size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

# ═══════════════════════════════════════════════════
# SLIDE 7 — 클로징
# ═══════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)
add_rect(sl, 0, 0, W, H, fill_rgb=HW_NAVY)
add_rect(sl, 0, 0, Inches(0.25), H, fill_rgb=HW_ORANGE)
add_rect(sl, 0, Inches(5.8), W, Inches(1.7), fill_rgb=HW_ORANGE)

add_text(sl, "맺음말",
         Inches(0.5), Inches(0.8), Inches(10), Inches(0.5),
         font_size=18, color=HW_ACCENT)

add_multiline(sl, [
    "저는 AI Factory를 '개념'이 아닌 '성과'로 만들어 왔습니다.",
    "",
    "LG그룹 8년간 전략 수립부터 현장 실증까지 전 과정을 경험했고,",
    "그 역량을 한화그룹 AX Factory 가속화에 즉시 투입하겠습니다.",
], Inches(0.5), Inches(1.5), Inches(12.3), Inches(2.5),
   font_size=26, bold=True, color=WHITE)

# 3 bullets
for i, txt in enumerate([
    "기술 실증력 — 수치로 증명된 AI 모델 (30일→15분, 90%↓, 10h→1분)",
    "전략 기획력 — LG그룹 VIP·사장단 보고, EY컨설팅 공동 전략 수립",
    "실행 추진력 — 단기·중장기 프로젝트를 뚝심으로 완수하는 'MI Task Leader'",
]):
    add_rect(sl, Inches(0.5), Inches(4.2 + i*0.45), Inches(0.3), Inches(0.35),
             fill_rgb=WHITE)
    add_text(sl, txt,
             Inches(0.95), Inches(4.22 + i*0.45), Inches(11.8), Inches(0.35),
             font_size=15, color=WHITE)

add_text(sl, "홍 창 기  |  한화시스템 전략부문 지원  |  2026",
         Inches(0.5), Inches(6.0), Inches(10), Inches(0.45),
         font_size=14, bold=True, color=HW_NAVY)

# ─────────────────────────────────────────────
# Save
# ─────────────────────────────────────────────
out = "/home/user/segamario-fluid-dynamics/한화시스템_면접발표_홍창기.pptx"
prs.save(out)
print(f"Saved: {out}")
