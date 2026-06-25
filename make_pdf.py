from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os, glob

# ── page size (16:9 widescreen)
W = 33.87 * cm   # 960pt equiv
H = 19.05 * cm   # 540pt equiv

# ── Hanwha brand colors
ORANGE  = HexColor("#FF6600")
ORANGE2 = HexColor("#FF9933")
NAVY    = HexColor("#1A2E4A")
DARK    = HexColor("#1A1A1A")
GRAY    = HexColor("#555555")
LGRAY   = HexColor("#F2F2F2")
MGRAY   = HexColor("#CCCCCC")
WHITE_C = HexColor("#FFFFFF")
CREAM   = HexColor("#FFEEDD")

# ── font: try to use NanumGothic, fallback to Helvetica
FONT_REGULAR = "Helvetica"
FONT_BOLD    = "Helvetica-Bold"

NANUM_PATHS = glob.glob("/usr/share/fonts/**/Nanum*.ttf", recursive=True) + \
              glob.glob("/usr/share/fonts/**/*Gothic*Bold*.ttf", recursive=True)
try:
    for p in NANUM_PATHS:
        if "Bold" in p:
            pdfmetrics.registerFont(TTFont("KorBold", p))
            FONT_BOLD = "KorBold"
        else:
            pdfmetrics.registerFont(TTFont("KorReg", p))
            FONT_REGULAR = "KorReg"
    if FONT_BOLD == "Helvetica-Bold":
        raise Exception("not found")
except Exception:
    # search more broadly
    for path in glob.glob("/usr/share/fonts/**/*.ttf", recursive=True):
        name = os.path.basename(path).lower()
        if "gothic" in name or "nanum" in name or "malgun" in name:
            try:
                pdfmetrics.registerFont(TTFont("KorReg", path))
                FONT_REGULAR = FONT_BOLD = "KorReg"
                break
            except Exception:
                pass

print(f"Fonts: regular={FONT_REGULAR}, bold={FONT_BOLD}")

OUT = "/home/user/segamario-fluid-dynamics/한화시스템_면접발표_홍창기.pdf"
c = canvas.Canvas(OUT, pagesize=(W, H))

# ════════════════════════════════════
# helpers
# ════════════════════════════════════
def rect(x, y, w, h, fill=None, stroke=None):
    if fill:
        c.setFillColor(fill)
        if stroke:
            c.setStrokeColor(stroke)
            c.rect(x, y, w, h, fill=1, stroke=1)
        else:
            c.rect(x, y, w, h, fill=1, stroke=0)
    elif stroke:
        c.setStrokeColor(stroke)
        c.rect(x, y, w, h, fill=0, stroke=1)

def txt(text, x, y, size=12, bold=False, color=DARK, align="left", maxw=None):
    c.setFillColor(color)
    font = FONT_BOLD if bold else FONT_REGULAR
    c.setFont(font, size)
    if align == "center" and maxw:
        tw = c.stringWidth(text, font, size)
        x = x + (maxw - tw) / 2
    elif align == "right" and maxw:
        tw = c.stringWidth(text, font, size)
        x = x + maxw - tw
    c.drawString(x, y, text)

def mtxt(lines, x, y, size=12, bold=False, color=DARK, lh=None, align="left", maxw=None):
    """Multi-line text, top-to-bottom (PDF coords are bottom-up so we go downward)."""
    if lh is None:
        lh = size * 1.5
    cy = y
    for line in lines:
        if line == "":
            cy -= lh * 0.6
            continue
        txt(line, x, cy, size=size, bold=bold, color=color, align=align, maxw=maxw)
        cy -= lh
    return cy

def header_bar(title, subtitle=None):
    """Navy top bar."""
    bar_h = 1.5 * cm
    rect(0, H - bar_h, W, bar_h, fill=NAVY)
    rect(0, H - bar_h, 0.15*cm, bar_h, fill=ORANGE)
    c.setFillColor(WHITE_C)
    c.setFont(FONT_BOLD, 20)
    c.drawString(0.4*cm, H - bar_h + 0.55*cm, title)
    if subtitle:
        c.setFont(FONT_REGULAR, 11)
        c.setFillColor(ORANGE2)
        c.drawString(0.4*cm, H - bar_h + 0.18*cm, subtitle)
    # bottom bar
    rect(0, 0, W, 0.45*cm, fill=NAVY)
    c.setFont(FONT_REGULAR, 8)
    c.setFillColor(WHITE_C)
    c.drawString(0.3*cm, 0.15*cm, "홍창기  |  한화시스템 전략부문")
    c.setFillColor(WHITE_C)
    c.setFont(FONT_REGULAR, 8)
    c.drawRightString(W - 0.3*cm, 0.15*cm, "2026")

def tag_box(x, y, w, h, text, bg=NAVY, fg=WHITE_C, fs=11):
    rect(x, y, w, h, fill=bg)
    c.setFillColor(fg)
    c.setFont(FONT_BOLD, fs)
    tw = c.stringWidth(text, FONT_BOLD, fs)
    c.drawString(x + (w - tw)/2, y + (h - fs*0.35)/2, text)

def kpi_box(x, y, w, h, number, label):
    rect(x, y, w, h, fill=NAVY)
    rect(x, y, 0.1*cm, h, fill=ORANGE)
    c.setFillColor(ORANGE2)
    c.setFont(FONT_BOLD, 18)
    tw = c.stringWidth(number, FONT_BOLD, 18)
    c.drawString(x + (w-tw)/2, y + h - 0.85*cm, number)
    c.setFillColor(WHITE_C)
    c.setFont(FONT_REGULAR, 9)
    tw = c.stringWidth(label, FONT_REGULAR, 9)
    c.drawString(x + (w-tw)/2, y + 0.18*cm, label)

# ════════════════════════════════════
# SLIDE 1 — Title
# ════════════════════════════════════
rect(0, 0, W, H, fill=NAVY)
rect(0, 0, 0.35*cm, H, fill=ORANGE)
rect(W*0.72, 0, W*0.28, H*0.25, fill=ORANGE)

c.setFillColor(ORANGE2)
c.setFont(FONT_BOLD, 13)
c.drawString(0.7*cm, H - 2.0*cm, "한화시스템 전략부문 지원")

c.setFillColor(WHITE_C)
c.setFont(FONT_BOLD, 36)
c.drawString(0.7*cm, H - 3.8*cm, "AI Factory 전략 전문가")
c.setFont(FONT_BOLD, 40)
c.drawString(0.7*cm, H - 5.0*cm, "홍 창 기")

subs = [
    "LG전자 생산기술원 전략담당  |  제조혁신 Task Leader (2018~현재)",
    "성균관대학교 기계공학 박사 (CFD/열유체)",
    "그룹 AX Factory 전략 수립 → C-Level 보고 전 사이클 경험",
]
c.setFont(FONT_REGULAR, 11)
c.setFillColor(MGRAY)
for i, s in enumerate(subs):
    c.drawString(0.7*cm, H - 6.5*cm - i*0.55*cm, s)

# KPI boxes
kpis = [("30일→15분","AI 설계 예측"), ("90% 감소","인정시험"), ("10시간→1분","사출 해석")]
for i,(n,l) in enumerate(kpis):
    kpi_box(0.7*cm + i*11.0*cm, 0.7*cm, 10.0*cm, 1.8*cm, n, l)

c.showPage()

# ════════════════════════════════════
# SLIDE 2 — 자기소개
# ════════════════════════════════════
rect(0, 0, W, H, fill=WHITE_C)
header_bar("자기소개", "기술에서 전략으로 — 8년의 여정")

# timeline line
tl_y = H * 0.45
rect(0.5*cm, tl_y - 0.04*cm, W - 1.0*cm, 0.08*cm, fill=ORANGE)

steps = [
    ("박사 과정\n2011~2018",
     ["성균관대 기계공학 (CFD)", "오일샌드 국책과제", "국토부 장관표창"]),
    ("기술 전문가\n2018~2021",
     ["LG전자 생산기술원", "CFD 해석 → AI 모델", "성능예측 시스템 구축"]),
    ("전략 기획\n2022~2024",
     ["LG그룹 스마트팩토리 2.0", "EY컨설팅 협업", "VIP/사장단 보고"]),
    ("MI Task Leader\n2025~현재",
     ["그룹 제조혁신협의회 총괄", "Physical AI 전략", "AX Factory 로드맵"]),
]

bgs   = [LGRAY, LGRAY, CREAM, ORANGE]
fgs   = [DARK,  DARK,  DARK,  WHITE_C]
col_w = (W - 1.0*cm) / 4

for i, (title, body) in enumerate(steps):
    x = 0.5*cm + i * col_w
    bx_h = H * 0.40
    bx_y = tl_y - bx_h - 0.1*cm

    # dot on timeline
    c.setFillColor(ORANGE)
    c.circle(x + col_w/2, tl_y, 0.18*cm, fill=1, stroke=0)

    # card
    rect(x + 0.08*cm, bx_y, col_w - 0.15*cm, bx_h, fill=bgs[i])
    # title header inside card
    rect(x + 0.08*cm, bx_y + bx_h - 0.65*cm, col_w - 0.15*cm, 0.65*cm,
         fill=NAVY if i < 3 else HexColor("#CC4400"))
    c.setFillColor(WHITE_C)
    c.setFont(FONT_BOLD, 10)
    lines_t = title.split("\n")
    c.drawString(x + 0.22*cm, bx_y + bx_h - 0.27*cm, lines_t[0])
    c.setFont(FONT_REGULAR, 9)
    c.drawString(x + 0.22*cm, bx_y + bx_h - 0.52*cm, lines_t[1] if len(lines_t)>1 else "")

    c.setFillColor(fgs[i])
    c.setFont(FONT_REGULAR, 10)
    for j, bl in enumerate(body):
        c.drawString(x + 0.22*cm, bx_y + bx_h - 0.9*cm - j*0.45*cm, "• " + bl)

# competency bar at bottom
rect(0.4*cm, 0.55*cm, W - 0.8*cm, 0.7*cm, fill=LGRAY)
txt("핵심 역량: CAE(CFX/Fluent) · AI/ML/DL · 그룹 전략 기획 · C-Level 보고 · 계열사 코디네이션",
    0.4*cm, 0.75*cm, size=11, bold=True, color=NAVY, align="center", maxw=W-0.8*cm)

c.showPage()

# ════════════════════════════════════
# SLIDE 3 — 지원 동기
# ════════════════════════════════════
rect(0, 0, W, H, fill=WHITE_C)
header_bar("지원 동기", "왜 한화시스템인가 — 위기 속 기회")

panels = [
    ("⚠  시장 위기", LGRAY, DARK, NAVY,
     ["국내 소비재·가전 제조업", "중국의 '규모의 경제'에", "글로벌 시장 지위 위협", "",
      "단순 원가 경쟁 한계"]),
    ("→  대응 전략", CREAM, DARK, HexColor("#993300"),
     ["단기 추격 불가능한", "고신뢰성 산업 집중", "(방산·항공·바이오)", "",
      "AI Factory + 실용 제조혁신"]),
    ("✓  기여 포인트", ORANGE, WHITE_C, WHITE_C,
     ["트렌드 센싱", "계열사 코디네이션", "임원진 소통", "",
      "LG 검증 방법론 즉시 적용"]),
]

panel_w = (W - 1.0*cm) / 3
panel_y = 0.55*cm
panel_h = H - 2.2*cm

for i, (title, bg, fg, hdr_bg, lines) in enumerate(panels):
    x = 0.5*cm + i * panel_w
    pw = panel_w - 0.15*cm
    rect(x, panel_y, pw, panel_h, fill=bg)
    rect(x, panel_y + panel_h - 0.7*cm, pw, 0.7*cm, fill=hdr_bg)
    c.setFillColor(WHITE_C)
    c.setFont(FONT_BOLD, 13)
    tw = c.stringWidth(title, FONT_BOLD, 13)
    c.drawString(x + (pw-tw)/2, panel_y + panel_h - 0.28*cm, title)
    c.setFillColor(fg)
    c.setFont(FONT_REGULAR, 12)
    for j, line in enumerate(lines):
        if line == "":
            continue
        c.drawString(x + 0.3*cm, panel_y + panel_h - 1.2*cm - j*0.52*cm, line)

# quote
rect(0.4*cm, panel_y - 0.0*cm, W - 0.8*cm, 0.0*cm, fill=CREAM)
txt('"소비재를 넘어, 더 높은 신뢰성이 요구되는 방산·항공에서 AI Factory를 완성하고 싶습니다."',
    0, 0.72*cm, size=11, bold=True, color=NAVY, align="center", maxw=W)

c.showPage()

# ════════════════════════════════════
# SLIDE 4 — AI 성과 3건
# ════════════════════════════════════
rect(0, 0, W, H, fill=WHITE_C)
header_bar("핵심 성과 ①  AI Factory 현장 실증", "전략이 아닌 수치로 증명한 AI 제조 혁신")

cases = [
    {
        "tag": "TV Stand",
        "kpi": "30일 → 15분",
        "sub": "CAE 성능예측 시간",
        "tech": "AI Inverse Net. (Generative Design)",
        "detail": ["• TV 낙하 해석 자동화 (Altair협업)",
                   "• Forward Net → Inverse Net 개발",
                   "• 1,000개 이상 형상 자동 추천",
                   "• CAE 엔지니어 고부가 업무 전환"],
    },
    {
        "tag": "김치냉장고",
        "kpi": "인정시험 90%↓",
        "sub": "1만 Case → 800건 이내",
        "tech": "AI Surrogate Model (시험 데이터 기반)",
        "detail": ["• 외기조건·제어신호·센서온도 학습",
                   "• 80%+ 정확도 예측",
                   "• Grid Search 최소 시험조건 도출",
                   "• 챔버 유휴 활용률 증가"],
    },
    {
        "tag": "사출성형",
        "kpi": "10시간 → 1분",
        "sub": "사출 CAE 해석 시간",
        "tech": "GCNN + MLOps (3D CAD 기반)",
        "detail": ["• 3D CAD + Moldflow 데이터 파싱",
                   "• Geodesic CNN (Scale 불변)",
                   "• MLOps 지속 업데이트 시스템",
                   "• CAE 엔지니어 역할 재정의"],
    },
]

card_w = (W - 1.0*cm) / 3
card_y = 0.55*cm
card_h = H - 2.1*cm

for i, case in enumerate(cases):
    x = 0.5*cm + i * card_w
    cw = card_w - 0.15*cm

    rect(x, card_y, cw, card_h, fill=LGRAY)
    # tag
    rect(x, card_y + card_h - 0.6*cm, cw, 0.6*cm, fill=NAVY)
    c.setFillColor(WHITE_C); c.setFont(FONT_BOLD, 12)
    tw = c.stringWidth(case["tag"], FONT_BOLD, 12)
    c.drawString(x + (cw-tw)/2, card_y + card_h - 0.22*cm, case["tag"])

    # KPI
    c.setFillColor(ORANGE); c.setFont(FONT_BOLD, 22)
    tw = c.stringWidth(case["kpi"], FONT_BOLD, 22)
    c.drawString(x + (cw-tw)/2, card_y + card_h - 1.3*cm, case["kpi"])
    c.setFillColor(GRAY); c.setFont(FONT_REGULAR, 10)
    tw = c.stringWidth(case["sub"], FONT_REGULAR, 10)
    c.drawString(x + (cw-tw)/2, card_y + card_h - 1.75*cm, case["sub"])

    # tech badge
    rect(x + 0.2*cm, card_y + card_h - 2.5*cm, cw - 0.4*cm, 0.55*cm, fill=NAVY)
    c.setFillColor(WHITE_C); c.setFont(FONT_BOLD, 9)
    tw = c.stringWidth(case["tech"], FONT_BOLD, 9)
    c.drawString(x + (cw-tw)/2, card_y + card_h - 2.15*cm, case["tech"])

    # details
    c.setFillColor(DARK); c.setFont(FONT_REGULAR, 10)
    for j, d in enumerate(case["detail"]):
        c.drawString(x + 0.25*cm, card_y + card_h - 3.1*cm - j*0.48*cm, d)

# bottom
rect(0.4*cm, 0.0*cm, W-0.8*cm, 0.58*cm, fill=CREAM)
txt("한화 적용 → 방산 품질검사  ·  항공 구조 해석 대체  ·  ICT 공정 최적화에 동일 방법론 즉시 적용 가능",
    0, 0.18*cm, size=11, bold=True, color=NAVY, align="center", maxw=W)

c.showPage()

# ════════════════════════════════════
# SLIDE 5 — 그룹 전략 기획 트랙
# ════════════════════════════════════
rect(0, 0, W, H, fill=WHITE_C)
header_bar("핵심 성과 ②  그룹 전략 기획 & C-Level 소통", "기술을 전략 언어로 번역해 임원진을 움직인 경험")

track = [
    ("2020~2021", "그룹 C4협의회",
     ["전자·에솔·이노텍·디스플레이·CNS", "Tangible Asset 4건 계열사 확산"]),
    ("2023", "Smart Factory 2.0 VIP보고",
     ["EY컨설팅 협업", "CAPEX/OPEX 절감 전략", "사장단협의회 보고"]),
    ("2024", "그룹 제조혁신전략\nBeyond China 전략",
     ["AI기반 전략 VIP 보고", "중국 SCM 활용 전략", "로봇 포함 AI요소기술 분석"]),
    ("2025~", "MI Task Leader\n그룹협의회 통합",
     ["7개 계열사 조율", "C-Level 직접 보고", "Physical AI·DT 신규 분과 운영"]),
]

step_w = (W - 1.0*cm) / 4
step_y = 0.55*cm
step_h = H - 2.15*cm

for i, (year, title, body) in enumerate(track):
    x = 0.5*cm + i * step_w
    sw = step_w - 0.15*cm
    is_last = (i == len(track)-1)
    card_bg = NAVY if is_last else LGRAY
    head_bg = ORANGE if is_last else GRAY

    rect(x, step_y, sw, step_h, fill=card_bg)
    # year tag
    rect(x, step_y + step_h - 0.5*cm, sw, 0.5*cm, fill=head_bg)
    c.setFillColor(WHITE_C); c.setFont(FONT_BOLD, 10)
    tw = c.stringWidth(year, FONT_BOLD, 10)
    c.drawString(x + (sw-tw)/2, step_y + step_h - 0.18*cm, year)

    # title
    title_color = WHITE_C if is_last else NAVY
    c.setFillColor(title_color); c.setFont(FONT_BOLD, 11)
    for j, tl in enumerate(title.split("\n")):
        c.drawString(x + 0.2*cm, step_y + step_h - 0.95*cm - j*0.42*cm, tl)

    # body
    body_color = WHITE_C if is_last else DARK
    c.setFillColor(body_color); c.setFont(FONT_REGULAR, 10)
    offset = 0.5*cm * (len(title.split("\n")))
    for j, bl in enumerate(body):
        c.drawString(x + 0.2*cm,
                     step_y + step_h - 1.35*cm - offset - j*0.45*cm, "• " + bl)

    # arrow
    if i < len(track)-1:
        ax = x + sw + 0.06*cm
        ay = step_y + step_h/2
        c.setFillColor(ORANGE)
        c.setFont(FONT_BOLD, 16)
        c.drawString(ax, ay, "▶")

# summary
rect(0.4*cm, 0.0*cm, W-0.8*cm, 0.58*cm, fill=NAVY)
c.setFillColor(WHITE_C); c.setFont(FONT_BOLD, 10)
tw = c.stringWidth("EY컨설팅 협업  ·  7개 계열사 이해관계 조율  ·  VIP/사장단 보고 반복  →  한화 AX 협의체 설계 즉시 수행 가능",
                   FONT_BOLD, 10)
c.drawString((W-tw)/2, 0.18*cm,
             "EY컨설팅 협업  ·  7개 계열사 이해관계 조율  ·  VIP/사장단 보고 반복  →  한화 AX 협의체 설계 즉시 수행 가능")

c.showPage()

# ════════════════════════════════════
# SLIDE 6 — 기여 방안
# ════════════════════════════════════
rect(0, 0, W, H, fill=WHITE_C)
header_bar("한화 AX Factory 기여 방안", "LG에서 증명한 것을 한화에서 더 빠르게")

contribs = [
    ("① AX 로드맵 설계",
     ["한화에어로스페이스·한화오션",
      "·한화솔루션 등 계열사",
      "특성별 AX Factory 로드맵",
      "",
      "ROI 기반 우선순위 설정",
      "→ 맹목적 자동화 방지",
      "→ LCC/고신뢰 공장 차별화"]),
    ("② 기술 ↔ 전략 브릿지",
     ["CAE·AI·Digital Twin을",
      "전략 언어로 번역",
      "",
      "현장 엔지니어 ↔ 임원 가교",
      "실현 가능성 기반 전략",
      "→ 투자 실패 리스크 최소화",
      ""]),
    ("③ Physical AI 선제 적용",
     ["2026년 직접 수립한",
      "Physical AI·Agentic AI·DT",
      "전략을 방산·항공에 적용",
      "",
      "무인화·AI 의사결정 체계",
      "→ 한화 AX Factory 선도",
      ""]),
]

panel_w = (W - 1.0*cm) / 3
panel_y = 0.65*cm
panel_h = H - 2.2*cm

for i, (title, lines) in enumerate(contribs):
    x = 0.5*cm + i * panel_w
    pw = panel_w - 0.15*cm

    rect(x, panel_y, pw, panel_h, fill=LGRAY)
    rect(x, panel_y, 0.1*cm, panel_h, fill=ORANGE)
    rect(x, panel_y + panel_h - 0.65*cm, pw, 0.65*cm, fill=NAVY)
    c.setFillColor(WHITE_C); c.setFont(FONT_BOLD, 13)
    tw = c.stringWidth(title, FONT_BOLD, 13)
    c.drawString(x + (pw-tw)/2, panel_y + panel_h - 0.25*cm, title)

    c.setFillColor(DARK); c.setFont(FONT_REGULAR, 11)
    for j, line in enumerate(lines):
        if line == "": continue
        c.drawString(x + 0.3*cm, panel_y + panel_h - 1.1*cm - j*0.5*cm, line)

# differentiator
rect(0.4*cm, 0.0*cm, W-0.8*cm, 0.65*cm, fill=ORANGE)
c.setFillColor(WHITE_C); c.setFont(FONT_BOLD, 11)
msg = "차별점: '그룹 전략 수립 → 계열사 실행 → 성과 측정 → VIP 보고' 전 사이클 경험 → 한화에서 학습 없이 즉시 실행"
tw = c.stringWidth(msg, FONT_BOLD, 11)
c.drawString((W-tw)/2, 0.22*cm, msg)

c.showPage()

# ════════════════════════════════════
# SLIDE 7 — 클로징
# ════════════════════════════════════
rect(0, 0, W, H, fill=NAVY)
rect(0, 0, 0.35*cm, H, fill=ORANGE)
rect(0, 0, W, 2.2*cm, fill=ORANGE)

c.setFillColor(ORANGE2); c.setFont(FONT_BOLD, 14)
c.drawString(0.7*cm, H - 1.8*cm, "맺음말")

quotes = [
    "저는 AI Factory를 '개념'이 아닌 '성과'로 만들어 왔습니다.",
    "",
    "LG그룹 8년간 전략 수립부터 현장 실증까지 전 과정을 경험했고,",
    "그 역량을 한화그룹 AX Factory 가속화에 즉시 투입하겠습니다.",
]
c.setFillColor(WHITE_C); c.setFont(FONT_BOLD, 20)
for i, q in enumerate(quotes):
    if q == "": continue
    c.drawString(0.7*cm, H - 2.8*cm - i*0.75*cm, q)

bullets = [
    ("기술 실증력", "수치로 증명된 AI 모델 (30일→15분, 90%↓, 10h→1분)"),
    ("전략 기획력", "LG그룹 VIP·사장단 보고, EY컨설팅 공동 전략 수립"),
    ("실행 추진력", "'몽골 코뿔소' — 단기·중장기 프로젝트를 뚝심으로 완수"),
]
for i, (bhead, btext) in enumerate(bullets):
    by = 3.5*cm - i*0.7*cm
    rect(0.7*cm, by - 0.05*cm, 0.35*cm, 0.42*cm, fill=WHITE_C)
    c.setFillColor(ORANGE2); c.setFont(FONT_BOLD, 12)
    c.drawString(1.2*cm, by + 0.1*cm, bhead + "  ")
    c.setFillColor(WHITE_C); c.setFont(FONT_REGULAR, 12)
    tw = c.stringWidth(bhead + "  ", FONT_BOLD, 12)
    c.drawString(1.2*cm + tw, by + 0.1*cm, btext)

c.setFillColor(NAVY); c.setFont(FONT_BOLD, 13)
c.drawString(0.7*cm, 1.5*cm, "홍 창 기  |  한화시스템 전략부문 지원  |  2026")

c.showPage()

c.save()
print(f"PDF saved: {OUT}")
