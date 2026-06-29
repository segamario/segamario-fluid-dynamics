from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

LG_RED    = RGBColor(0xCE, 0x0A, 0x2C)
LG_NAVY   = RGBColor(0x1A, 0x2E, 0x4A)
LG_DARK   = RGBColor(0x1A, 0x1A, 0x1A)
LG_GRAY   = RGBColor(0x55, 0x55, 0x55)
LG_LGRAY  = RGBColor(0xF2, 0xF2, 0xF2)
LG_ACCENT = RGBColor(0xFF, 0x4C, 0x5C)
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)

W = Inches(13.33)
H = Inches(7.5)

prs = Presentation()
prs.slide_width  = W
prs.slide_height = H
BLANK = prs.slide_layouts[6]

# ── helpers ──────────────────────────────────────────────────────────
def rect(sl, l, t, w, h, fill=None, line=None, lw=None):
    s = sl.shapes.add_shape(1, l, t, w, h)
    s.line.fill.background()
    if fill: s.fill.solid(); s.fill.fore_color.rgb = fill
    else: s.fill.background()
    if line: s.line.color.rgb = line; s.line.width = (lw or Pt(1))
    else: s.line.fill.background()
    return s

def txt(sl, text, l, t, w, h, fs=14, bold=False,
        color=LG_DARK, align=PP_ALIGN.LEFT):
    tb = sl.shapes.add_textbox(l, t, w, h)
    tb.word_wrap = True
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.alignment = align
    r = p.add_run(); r.text = text
    r.font.size = Pt(fs); r.font.bold = bold
    r.font.color.rgb = color; r.font.name = "맑은 고딕"
    return tb

def ml(sl, lines, l, t, w, h, fs=13, bold=False,
       color=LG_DARK, align=PP_ALIGN.LEFT):
    tb = sl.shapes.add_textbox(l, t, w, h)
    tb.word_wrap = True; tf = tb.text_frame; tf.word_wrap = True
    first = True
    for line in lines:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False; p.alignment = align; p.space_after = Pt(2)
        r = p.add_run(); r.text = line
        r.font.size = Pt(fs); r.font.bold = bold
        r.font.color.rgb = color; r.font.name = "맑은 고딕"

def header(sl, title, sub=None):
    rect(sl, 0, 0, W, Inches(1.0), fill=LG_NAVY)
    rect(sl, 0, 0, Inches(0.08), Inches(1.0), fill=LG_RED)
    txt(sl, title, Inches(0.25), Inches(0.08), Inches(10), Inches(0.62),
        fs=25, bold=True, color=WHITE)
    if sub:
        txt(sl, sub, Inches(0.25), Inches(0.68), Inches(10.5), Inches(0.3),
            fs=12, color=LG_ACCENT)
    rect(sl, 0, Inches(7.2), W, Inches(0.3), fill=LG_NAVY)
    txt(sl, "LG전자 생산기술원  |  2026 부산로봇엑스포 관람 보고서",
        Inches(0.2), Inches(7.22), Inches(9), Inches(0.25), fs=10, color=WHITE)
    txt(sl, "2026. 7. 3.",
        Inches(12.0), Inches(7.22), Inches(1.2), Inches(0.25),
        fs=10, color=WHITE, align=PP_ALIGN.RIGHT)

def tag(sl, l, t, w, h, text, fill=LG_RED, tc=WHITE, fs=12):
    rect(sl, l, t, w, h, fill=fill)
    txt(sl, text, l, t, w, h, fs=fs, bold=True, color=tc,
        align=PP_ALIGN.CENTER)

def kpi(sl, l, t, w, h, number, label):
    rect(sl, l, t, w, h, fill=LG_NAVY)
    rect(sl, l, t, Inches(0.06), h, fill=LG_RED)
    txt(sl, number, l+Inches(0.15), t+Inches(0.06),
        w-Inches(0.2), Inches(0.58),
        fs=26, bold=True, color=LG_ACCENT, align=PP_ALIGN.CENTER)
    txt(sl, label, l+Inches(0.1), t+Inches(0.63),
        w-Inches(0.15), Inches(0.33),
        fs=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER)


# ══════════════════════════════════════════════════════════════════════
# SLIDE 1 — 표지
# ══════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, H, fill=LG_NAVY)
rect(sl, 0, 0, Inches(0.28), H, fill=LG_RED)
rect(sl, Inches(8.8), Inches(5.0), Inches(4.53), Inches(2.5), fill=LG_RED)

txt(sl, "LG전자 생산기술원", Inches(0.6), Inches(0.85), Inches(10), Inches(0.45),
    fs=17, color=LG_ACCENT)
txt(sl, "전시회 관람 보고서",
    Inches(0.6), Inches(1.45), Inches(11), Inches(0.68),
    fs=38, bold=True, color=WHITE)
txt(sl, "2026 부산 오토매뉴팩·로봇엑스포·빅테크쇼",
    Inches(0.6), Inches(2.22), Inches(11), Inches(0.52),
    fs=21, bold=True, color=LG_ACCENT)
txt(sl, "AUTOMANUFAC × ROBOT EXPO × BIG TECH SHOW BUSAN 2026",
    Inches(0.6), Inches(2.82), Inches(11), Inches(0.38),
    fs=13, color=RGBColor(0xAA, 0xBB, 0xCC))
rect(sl, Inches(0.6), Inches(3.3), Inches(7.8), Inches(0.04), fill=LG_RED)
ml(sl, [
    "장  소: 부산 벡스코(BEXCO) 제2전시장 4홀 (B·C·D·E·F관)",
    "기  간: 2026. 7. 1(수) ~ 7. 3(금)",
    "규  모: 5개국, 363개 부스(8,352㎡)",
    "주  관: 한국산업전람",
], Inches(0.6), Inches(3.42), Inches(9), Inches(1.0),
   fs=14, color=RGBColor(0xCC, 0xCC, 0xCC))
for i, (num, lbl) in enumerate([("5개국", "참가국"),
                                  ("363부스", "전시 규모"),
                                  ("8,352㎡", "전시 면적")]):
    kpi(sl, Inches(0.6 + i*2.85), Inches(5.1), Inches(2.6), Inches(1.05), num, lbl)
txt(sl, "관람일: 2026. 7. 1  |  작성: LG전자 생산기술원",
    Inches(0.6), Inches(6.85), Inches(8), Inches(0.35),
    fs=12, color=RGBColor(0x88, 0x99, 0xAA))


# ══════════════════════════════════════════════════════════════════════
# SLIDE 2 — 전시회 개요 & 홀 구성
# ══════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, H, fill=WHITE)
header(sl, "전시회 개요",
       "벡스코 제2전시장 4홀 — 3개 전문 전시회 통합 운영")

# 왼쪽: 기본정보
rect(sl, Inches(0.25), Inches(1.1), Inches(5.6), Inches(5.9), fill=LG_LGRAY)
tag(sl, Inches(0.25), Inches(1.1), Inches(5.6), Inches(0.42), "행사 기본 정보", fill=LG_NAVY)
rows = [
    ("전시 기간", "2026. 7. 1(수) ~ 7. 3(금), 3일간"),
    ("전시 장소", "부산 벡스코(BEXCO) 제2전시장 4홀"),
    ("관람 시간", "7/1~7/2  10:00~17:00  /  7/3  10:00~16:00"),
    ("참가 규모", "5개국, 363개 부스(8,352㎡)"),
    ("참가국",   "한국 · 독일 · 일본 · 중국 · 말레이시아"),
    ("주관",     "한국산업전람 (031-380-6806)"),
    ("전시 주제", "로봇 AI 기반 기술과 혁신이\n만드는 새로운 부산의 물결"),
]
for i, (lab, val) in enumerate(rows):
    y = Inches(1.6 + i*0.62)
    rect(sl, Inches(0.25), y, Inches(1.55), Inches(0.55), fill=LG_NAVY)
    txt(sl, lab, Inches(0.28), y+Inches(0.05), Inches(1.48), Inches(0.45),
        fs=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    txt(sl, val, Inches(1.83), y+Inches(0.07), Inches(3.9), Inches(0.48),
        fs=11, color=LG_DARK)

# 오른쪽: 홀 구성
rect(sl, Inches(6.1), Inches(1.1), Inches(6.98), Inches(5.9), fill=LG_LGRAY)
tag(sl, Inches(6.1), Inches(1.1), Inches(6.98), Inches(0.42),
    "제2전시장 4홀 — 3개 전시회 구성", fill=LG_RED)

expos = [
    ("ROBOT EXPO\n부산로봇엑스포",
     LG_RED,
     ["▸ 유니트리 로보틱스(Unitree Robotics)",
      "  - G1·R1 휴머노이드, B2 사족보행 로봇",
      "▸ DJI",
      "  - 산업용·물류·수상 드론",
      "▸ 서비스 로봇, 부품·센서 전문업체",
      "▸ 휴머노이드 AI 제어 플랫폼 기업군"]),
    ("AUTOMANUFAC\n부산오토매뉴팩",
     LG_NAVY,
     ["▸ 성우하이텍",
      "  - 차체 부품 제조 자동화, 용접 라인",
      "▸ BorgWarner(보그워너)",
      "  - 전기차 파워트레인·전장 부품",
      "▸ 7축 로봇 용접기 전문 중소기업군",
      "▸ 반송용 설비기계, 프레스 자동화"]),
    ("BIG TECH SHOW\n로봇물류제조자동화산업대전",
     RGBColor(0x1A, 0x7A, 0x3C),
     ["▸ 쿳션(CUTSHION) — 부스 4D0705",
      "  - 제조·물류·F&B·교육 로봇 솔루션",
      "▸ AMR / AGV 자율물류 기업군",
      "▸ AI 스마트팩토리 솔루션사",
      "▸ 디지털 트윈 · MES · ERP 연동 업체",
      "▸ 2026 AI자율제조혁신 컨퍼런스 병행"]),
]
for i, (title, color, items) in enumerate(expos):
    y = Inches(1.62 + i * 1.78)
    rect(sl, Inches(6.1), y, Inches(6.98), Inches(0.38), fill=color)
    txt(sl, title, Inches(6.18), y+Inches(0.04), Inches(3.0), Inches(0.32),
        fs=12, bold=True, color=WHITE)
    ml(sl, items, Inches(6.15), y+Inches(0.42), Inches(6.8), Inches(1.28),
       fs=11, color=LG_DARK)


# ══════════════════════════════════════════════════════════════════════
# SLIDE 3 — 유니트리 로보틱스 (Unitree Robotics)
# ══════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, H, fill=WHITE)
header(sl, "[로봇엑스포] 유니트리 로보틱스 (Unitree Robotics)",
       "중국 — 이번 전시 최대 주목 부스 / 휴머노이드 G1·R1 및 사족보행 B2 실물 시연")

# 제품별 3분할
products = [
    {
        "name": "G1 휴머노이드 로봇",
        "tag": "출시 · 상용화 단계",
        "tag_color": LG_RED,
        "specs": [
            "신장 127cm / 중량 35kg",
            "자유도(DOF) 23축 — 정밀 손가락 관절 포함",
            "배터리 1회 충전 2시간 연속 작동",
            "가격: 약 $16,000(약 2,200만원)",
        ],
        "demo": [
            "부품 집기·이송·조립 동작 시연",
            "계단 오르내리기, 장애물 회피",
            "실시간 AI 제어로 돌발 상황 대응",
            "공장 순찰 시나리오 소개",
        ],
    },
    {
        "name": "R1 휴머노이드 로봇",
        "tag": "차세대 신형 모델",
        "tag_color": LG_NAVY,
        "specs": [
            "G1 대비 상체 자유도 대폭 향상",
            "양팔 협력 작업 최적화 설계",
            "고속 동작·넘어짐 복원 개선",
            "2026년 하반기 상용 출하 예정",
        ],
        "demo": [
            "양팔로 박스 들어올리기·적재 시연",
            "사람과의 물체 전달 협업 시연",
            "비정형 부품 피킹(Vision+AI 연동)",
            "산업 현장 투입 데모 영상 상영",
        ],
    },
    {
        "name": "B2 사족보행 로봇",
        "tag": "산업 현장 투입 모델",
        "tag_color": RGBColor(0x1A, 0x7A, 0x3C),
        "specs": [
            "적재 하중 40kg, 최고속도 6m/s",
            "IP67 방수방진 — 야외·거친 환경 적합",
            "라이다+비전 센서 융합 자율 맵핑",
            "가격: 약 $30,000 (산업용 기준)",
        ],
        "demo": [
            "공장·야외 지형 자율주행 시연",
            "설비 점검 패트롤 시나리오",
            "센서 데이터 실시간 모니터링",
            "사람 추종·경로 안내 데모",
        ],
    },
]
for i, p in enumerate(products):
    x = Inches(0.25 + i * 4.35)
    rect(sl, x, Inches(1.1), Inches(4.1), Inches(5.9), fill=LG_LGRAY)
    tag(sl, x, Inches(1.1), Inches(4.1), Inches(0.4), p["name"],
        fill=p["tag_color"])
    tag(sl, x, Inches(1.5), Inches(4.1), Inches(0.32),
        p["tag"], fill=LG_DARK, fs=10)
    txt(sl, "■ 주요 사양",
        x+Inches(0.12), Inches(1.88), Inches(3.85), Inches(0.28),
        fs=12, bold=True, color=LG_NAVY)
    ml(sl, p["specs"], x+Inches(0.14), Inches(2.18), Inches(3.84), Inches(1.45),
       fs=11, color=LG_DARK)
    rect(sl, x+Inches(0.12), Inches(3.68), Inches(3.84), Inches(0.03),
         fill=p["tag_color"])
    txt(sl, "■ 전시장 시연 내용",
        x+Inches(0.12), Inches(3.74), Inches(3.85), Inches(0.28),
        fs=12, bold=True, color=p["tag_color"])
    ml(sl, p["demo"], x+Inches(0.14), Inches(4.04), Inches(3.84), Inches(1.7),
       fs=11, color=LG_DARK)

# 하단 시사점 바
rect(sl, Inches(0.25), Inches(7.08), Inches(12.83), Inches(0.08), fill=LG_RED)
rect(sl, Inches(0.25), Inches(7.08), Inches(12.83), Inches(0.38), fill=RGBColor(0xFD, 0xE8, 0xEB))
txt(sl, "LG생산기술원 시사점  중국산 휴머노이드의 가격 충격($16K) — 도입 검토 시점이 '언제'가 아닌 '어떤 공정부터'로 이미 전환됨",
    Inches(0.35), Inches(7.11), Inches(12.6), Inches(0.33),
    fs=11, bold=True, color=LG_RED)


# ══════════════════════════════════════════════════════════════════════
# SLIDE 4 — DJI
# ══════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, H, fill=WHITE)
header(sl, "[로봇엑스포] DJI",
       "중국 — 산업용 드론에서 대형 물류운반 드론·수상 드론까지")

# 왼쪽: 전시 제품 소개
rect(sl, Inches(0.25), Inches(1.1), Inches(7.7), Inches(5.9), fill=LG_LGRAY)
tag(sl, Inches(0.25), Inches(1.1), Inches(7.7), Inches(0.42),
    "전시 제품 및 시연 시나리오", fill=LG_NAVY)

dji_products = [
    ("산업용 점검 드론",
     ["공장 설비 상공 자율 비행 → 열화상·비전 카메라 점검",
      "Matrice 4 시리즈 — AI 장애물 회피, 실내외 겸용",
      "정밀 호버링으로 좁은 설비 사이 촬영 시연",
      "생산라인 비가동 설비 이상 감지 실시간 알림"]),
    ("대형 물류운반 드론",
     ["30~50kg 화물 이송 가능한 멀티로터 플랫폼",
      "공장 동 간(棟間) 부품·반제품 공중 이송 시나리오",
      "AGV 대비 바닥 레이아웃 제약 없음 — 3D 동선 확보",
      "배터리 스왑 스테이션 자율 귀환 운용 데모"]),
    ("수상 드론",
     ["해양 모니터링·해상 물류 전용 플랫폼",
      "방수 IP68 등급, 수면 착수·이수 자율 운용",
      "항만·선박 접안 설비 점검 시나리오 소개",
      "LiDAR+카메라 융합 3D 매핑 데모"]),
]
for i, (title, items) in enumerate(dji_products):
    y = Inches(1.62 + i * 1.78)
    rect(sl, Inches(0.25), y, Inches(7.7), Inches(0.36), fill=LG_RED)
    txt(sl, title, Inches(0.35), y+Inches(0.05), Inches(7.4), Inches(0.28),
        fs=13, bold=True, color=WHITE)
    ml(sl, items, Inches(0.35), y+Inches(0.4), Inches(7.5), Inches(1.3),
       fs=12, color=LG_DARK)

# 오른쪽: 시사점
rect(sl, Inches(8.2), Inches(1.1), Inches(4.88), Inches(5.9), fill=LG_LGRAY)
tag(sl, Inches(8.2), Inches(1.1), Inches(4.88), Inches(0.42),
    "LG생산기술원 시사점", fill=LG_RED)
ml(sl, [
    "① 공장 내 수직 물류 동선 가능성",
    "  AGV/AMR이 담당하는 수평 이송에",
    "  드론 기반 수직 동선 추가 시",
    "  층간·동간 이송 효율 획기적 개선",
    "",
    "② 설비 점검 자동화",
    "  사람이 직접 접근하기 어려운",
    "  대형 설비·고소 공간 정기 점검에",
    "  드론 도입 즉시 적용 가능",
    "",
    "③ 국내 규제 현황 확인 필요",
    "  공장 내 실내 드론 비행은",
    "  현행 항공안전법 예외 적용 가능",
    "  → 법무팀과 사전 검토 착수 권고",
    "",
    "④ 단기 파일럿 대상",
    "  창원 공장 동간 부품 이송",
    "  라인 or 구미 공장 점검 드론",
    "  시범 도입 검토 (2027 상반기)",
], Inches(8.3), Inches(1.6), Inches(4.68), Inches(5.2),
   fs=11, color=LG_DARK)


# ══════════════════════════════════════════════════════════════════════
# SLIDE 5 — 성우하이텍 & BorgWarner (오토매뉴팩)
# ══════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, H, fill=WHITE)
header(sl, "[오토매뉴팩] 성우하이텍 & BorgWarner",
       "한국 · 글로벌 — 자동차·전장 제조 자동화 벤치마킹 포인트")

# 왼쪽: 성우하이텍
rect(sl, Inches(0.25), Inches(1.1), Inches(6.2), Inches(5.9), fill=LG_LGRAY)
tag(sl, Inches(0.25), Inches(1.1), Inches(6.2), Inches(0.42),
    "성우하이텍 (Sungwoo Hitech)", fill=LG_NAVY)
txt(sl, "국내 / 차체 부품·도어·범퍼 등 프레스·용접 제조 전문",
    Inches(0.35), Inches(1.55), Inches(6.0), Inches(0.32),
    fs=11, color=LG_GRAY)
txt(sl, "■ 전시 주요 내용",
    Inches(0.35), Inches(1.9), Inches(6.0), Inches(0.3),
    fs=12, bold=True, color=LG_NAVY)
ml(sl, [
    "• 차체 패널·범퍼 제조 자동화 라인 모형 전시",
    "• 6축 다관절 로봇 용접 셀 시연 영상 상영",
    "• AI 비전 기반 용접 비드(Bead) 품질 실시간 검사",
    "• 프레스-로봇-검사 일괄 자동화 공정 플로우 소개",
    "• 스마트 제조 MES 대시보드 실시간 공정 모니터링",
    "• 단일 셀 내 7축 로봇으로 복잡 곡면 용접 적용 사례",
], Inches(0.35), Inches(2.25), Inches(6.0), Inches(2.0), fs=12, color=LG_DARK)
rect(sl, Inches(0.35), Inches(4.3), Inches(6.0), Inches(0.03), fill=LG_RED)
txt(sl, "■ LG생산기술원 시사점",
    Inches(0.35), Inches(4.35), Inches(6.0), Inches(0.3),
    fs=12, bold=True, color=LG_RED)
ml(sl, [
    "▶ 가전 외장재(세탁기·냉장고) 금속 프레임 용접 공정에",
    "  7축 로봇 적용 타당성 검토 — 복잡 곡면 대응력 확인",
    "▶ AI 비전 용접 검사 솔루션 → 인라인 QC 즉시 도입 검토",
    "▶ MES 연동 실시간 모니터링 방식을 당사 생산라인에 적용",
    "▶ 성우하이텍 자동화팀과 기술 교류 협력 가능성 타진 권고",
], Inches(0.35), Inches(4.7), Inches(6.0), Inches(2.1), fs=11, color=LG_DARK)

# 오른쪽: BorgWarner
rect(sl, Inches(6.7), Inches(1.1), Inches(6.38), Inches(5.9), fill=LG_LGRAY)
tag(sl, Inches(6.7), Inches(1.1), Inches(6.38), Inches(0.42),
    "BorgWarner(보그워너)", fill=RGBColor(0x1A, 0x7A, 0x3C))
txt(sl, "글로벌 / 전기차 파워트레인·전장 부품 전문 (미국 본사)",
    Inches(6.8), Inches(1.55), Inches(6.18), Inches(0.32),
    fs=11, color=LG_GRAY)
txt(sl, "■ 전시 주요 내용",
    Inches(6.8), Inches(1.9), Inches(6.18), Inches(0.3),
    fs=12, bold=True, color=LG_NAVY)
ml(sl, [
    "• 전기차 구동모터·인버터·온보드 충전기(OBC) 제품 전시",
    "• EV 파워트레인 제조 자동화 공정 영상 및 데이터 소개",
    "• 배터리 열관리 모듈(BTM) 조립 자동화 라인 사례 공개",
    "• 전장 부품 불량 zero 목표의 AI 검사 통합 시스템 소개",
    "• 한국 공장(이천) 스마트팩토리 적용 현황 발표",
    "• 글로벌 서플라이체인 내 자동화 표준화 전략 공유",
], Inches(6.8), Inches(2.25), Inches(6.18), Inches(2.0), fs=12, color=LG_DARK)
rect(sl, Inches(6.8), Inches(4.3), Inches(6.0), Inches(0.03), fill=LG_RED)
txt(sl, "■ LG생산기술원 시사점",
    Inches(6.8), Inches(4.35), Inches(6.18), Inches(0.3),
    fs=12, bold=True, color=LG_RED)
ml(sl, [
    "▶ EV 전장 부품 제조 자동화 벤치마킹 — LG이노텍 협업",
    "  가능성 검토 (전장 부품 품질 자동화 표준 공유)",
    "▶ 배터리 열관리 모듈 조립 자동화는 LG에너지솔루션",
    "  제조 혁신 로드맵과 직접 연계 가능한 레퍼런스",
    "▶ 보그워너 한국 공장 스마트팩토리 사례 → 현장 방문",
    "  벤치마킹 협의 권고 (이천 공장)",
], Inches(6.8), Inches(4.7), Inches(6.18), Inches(2.1), fs=11, color=LG_DARK)


# ══════════════════════════════════════════════════════════════════════
# SLIDE 6 — 쿳션(CUTSHION) & 빅테크쇼 주요 솔루션
# ══════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, H, fill=WHITE)
header(sl, "[빅테크쇼] 쿳션(CUTSHION) & 자율제조 솔루션 기업군",
       "BIG TECH SHOW 2026 — 로봇·물류·제조자동화 약 300개사·500부스")

# 상단: 쿳션 집중 분석
rect(sl, Inches(0.25), Inches(1.1), Inches(12.83), Inches(2.58), fill=LG_LGRAY)
rect(sl, Inches(0.25), Inches(1.1), Inches(0.06), Inches(2.58), fill=LG_RED)
tag(sl, Inches(0.25), Inches(1.1), Inches(4.5), Inches(0.42),
    "쿳션 (CUTSHION)  —  부스 4D0705", fill=LG_RED)
txt(sl, "국내 / 제조·물류·F&B·교육 분야 실용 로봇 솔루션 전문",
    Inches(0.35), Inches(1.55), Inches(6.0), Inches(0.3),
    fs=11, color=LG_GRAY)
ml(sl, [
    "• 단순 판매 아닌 '로봇이 어떻게 현장에서 쓰이는지' 실사용 시나리오 중심 전시",
    "• 제조 라인 내 협동로봇 보조 작업, 물류 내 AMR 연계, F&B 서빙·조리 자동화 패키지",
    "• 교육기관 대상 로봇 교육 플랫폼 및 RaaS(Robot as a Service) 모델 소개",
    "• 소규모 제조기업도 즉시 도입 가능한 저비용 로봇화 솔루션 제안 → 중소기업 타겟",
], Inches(0.35), Inches(1.9), Inches(8.5), Inches(1.62), fs=12, color=LG_DARK)
txt(sl, "시사점  RaaS 구독 모델 확산 — '로봇 구매' 아닌 '로봇 사용권'으로 초기 투자 부담 해소. LG생산기술원 계열 중소 협력사 스마트화 지원 프로그램과 연계 검토",
    Inches(8.9), Inches(1.18), Inches(4.0), Inches(2.4),
    fs=11, bold=False, color=LG_DARK)
rect(sl, Inches(8.85), Inches(1.15), Inches(0.05), Inches(2.45), fill=LG_RED)

# 하단: 빅테크쇼 전반 관찰
rect(sl, Inches(0.25), Inches(3.8), Inches(12.83), Inches(0.04), fill=LG_RED)
tag(sl, Inches(0.25), Inches(3.84), Inches(12.83), Inches(0.4),
    "빅테크쇼(BIG TECH SHOW) 전반 관찰 — AMR·협동로봇·스마트팩토리·AI 검사 기업군",
    fill=LG_NAVY)

categories = [
    ("AMR / AGV\n자율물류 기업군",
     LG_RED,
     ["SLAM 기반 자율 맵핑\n고정 레일 없이 공장 자율 운용",
      "다중 로봇 Fleet\nManagement SW 완성도 향상",
      "MES 연동 실시간\n동선 재설정 가능"]),
    ("협동로봇(Cobot)\n솔루션 기업군",
     LG_NAVY,
     ["직접 교시(Direct Teaching)\nUI 보편화 확인",
      "힘·토크 센서 내장\n복잡 조립 대응 가능",
      "다품종 소량 전환 시\n프로그래밍 無 재설정"]),
    ("AI 스마트팩토리\n솔루션 기업군",
     RGBColor(0x1A, 0x7A, 0x3C),
     ["GPU 엣지 AI 비전 검사\n인라인 실시간 불량 검출",
      "디지털 트윈 기반\n공정 파라미터 AI 최적화",
      "AI자율제조혁신 컨퍼런스\n(빅테크쇼 공식 부대행사)"]),
    ("로봇 부품·센서\n전문 기업군",
     RGBColor(0x7B, 0x3F, 0x9A),
     ["감속기·모터드라이브\n국산화 현황 확인",
      "비전·힘토크·라이다 센서\n원스톱 공급 가능 업체 확인",
      "엔드이펙터(그리퍼) 전문사\n다품종 파지 솔루션"]),
]
for i, (title, color, items) in enumerate(categories):
    x = Inches(0.25 + i * 3.22)
    rect(sl, x, Inches(4.28), Inches(3.1), Inches(2.65), fill=LG_LGRAY)
    tag(sl, x, Inches(4.28), Inches(3.1), Inches(0.5), title, fill=color, fs=11)
    ml(sl, items, x+Inches(0.12), Inches(4.82), Inches(2.88), Inches(2.0),
       fs=11, color=LG_DARK)


# ══════════════════════════════════════════════════════════════════════
# SLIDE 7 — 종합 시사점 (LG생산기술원 관점)
# ══════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, H, fill=WHITE)
header(sl, "LG전자 생산기술원 — 종합 시사점",
       "전시회 관찰을 LG 생산 현장과 직접 연결한 실행 관점 분석")

# 5개 핵심 발견 카드
insights = [
    ("① 휴머노이드 도입\n시점 재검토 필요",
     LG_RED,
     ["유니트리 G1, $16K — 기존 예상 가격의",
      "  1/10 수준. 3~5년 내 상용화 현실화",
      "단기: 물류·자재 이송(비정밀) 파일럿",
      "중기: 조립 보조·검사(반정밀) 확대",
      "→ 2027년 파일럿 라인 구성 착수 권고"]),
    ("② AMR 전환\n가속화 시점",
     LG_NAVY,
     ["SLAM 기반 AMR 완성도 상용 수준 도달",
      "창원·구미 공장 AGV → AMR 전환",
      "  로드맵 재수립 (2027년 착수)",
      "계열사 로보스타 AMR 솔루션과",
      "  연계 강화로 비용 최소화"]),
    ("③ 드론 물류\n신규 검토 항목",
     RGBColor(0x1A, 0x7A, 0x3C),
     ["DJI 물류드론 — 동간(棟間) 이송 가능",
      "AGV 사각지대(층간·이격동) 해소",
      "국내 공장 내 실내 드론 비행",
      "  항공안전법 예외 규정 사전 확인",
      "→ 법무팀 검토 → 2027 파일럿"]),
    ("④ AI 인라인\n품질검사 즉시 도입",
     RGBColor(0x7B, 0x3F, 0x9A),
     ["GPU 엣지 AI 비전 검사 상용 성숙",
      "성우하이텍·BorgWarner 적용 사례",
      "  실제 공정 레퍼런스 확인",
      "LG 생산라인 인라인 QC 전환",
      "  → 공급업체 비교 평가 즉시 착수"]),
    ("⑤ 벤치마킹\n후속 협력 채널",
     RGBColor(0xC8, 0x70, 0x00),
     ["성우하이텍 자동화팀 기술 교류 협의",
      "BorgWarner 이천 공장 벤치마킹 방문",
      "쿳션(CUTSHION) RaaS 모델 → LG",
      "  협력사 스마트화 지원 연계 검토",
      "한국산업전람 차기 전시 참가 검토"]),
]
for i, (title, color, items) in enumerate(insights):
    x = Inches(0.22 + (i % 3) * 4.35) if i < 3 else Inches(0.22 + (i-3) * 6.5 + 0.1)
    y = Inches(1.1) if i < 3 else Inches(4.25)
    w_card = Inches(4.1) if i < 3 else Inches(6.1)
    h_card = Inches(2.95) if i < 3 else Inches(2.75)
    rect(sl, x, y, w_card, h_card, fill=LG_LGRAY)
    tag(sl, x, y, w_card, Inches(0.48), title, fill=color, fs=12)
    ml(sl, items, x+Inches(0.12), y+Inches(0.52), w_card-Inches(0.2),
       h_card-Inches(0.62), fs=11, color=LG_DARK)


# ══════════════════════════════════════════════════════════════════════
# SLIDE 8 — 단기 실행 과제 & 결론
# ══════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, H, fill=WHITE)
header(sl, "단기 실행 과제 & 결론",
       "관찰 → 분석 → 행동 — LG전자 생산기술원 제언")

# 단기 실행 과제 테이블
tag(sl, Inches(0.25), Inches(1.1), Inches(12.83), Inches(0.42),
    "단기 실행 과제 (6개월 이내)", fill=LG_RED)
tasks = [
    ("1", "협동로봇 파일럿 공정 선정 및 PoC 기획",    "공정자동화팀",   "쿳션·국내 Cobot사",    LG_RED),
    ("2", "AMR 도입 대상 공장(창원·구미) 타당성 분석",  "물류혁신팀",    "계열사 로보스타",     LG_NAVY),
    ("3", "AI 비전 인라인 검사 솔루션 공급업체 비교평가", "품질기술팀",   "성우하이텍 사례 참고", RGBColor(0x1A,0x7A,0x3C)),
    ("4", "공장 내 드론 비행 법규 검토 착수",          "법무·안전팀",   "DJI 기술 문서 활용",  RGBColor(0x7B,0x3F,0x9A)),
    ("5", "BorgWarner 이천 공장 벤치마킹 방문 협의",    "전략기획팀",    "보그워너 한국법인",   RGBColor(0xC8,0x70,0x00)),
]
for i, (rank, task, dept, ref, color) in enumerate(tasks):
    y = Inches(1.6 + i * 0.52)
    rect(sl, Inches(0.25), y, Inches(0.6), Inches(0.45), fill=color)
    txt(sl, rank, Inches(0.25), y+Inches(0.05), Inches(0.6), Inches(0.38),
        fs=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    rect(sl, Inches(0.87), y, Inches(6.5), Inches(0.45), fill=LG_LGRAY)
    txt(sl, task, Inches(0.95), y+Inches(0.07), Inches(6.3), Inches(0.35),
        fs=12, color=LG_DARK)
    rect(sl, Inches(7.4), y, Inches(2.5), Inches(0.45), fill=LG_LGRAY)
    txt(sl, dept, Inches(7.45), y+Inches(0.07), Inches(2.4), Inches(0.35),
        fs=11, color=LG_GRAY)
    rect(sl, Inches(9.93), y, Inches(3.15), Inches(0.45), fill=LG_LGRAY)
    txt(sl, ref, Inches(9.98), y+Inches(0.07), Inches(3.05), Inches(0.35),
        fs=11, color=LG_GRAY)

# 컬럼 레이블
for lbl, x, w_c in [("과제", 0.87, 6.5), ("담당", 7.4, 2.5), ("참고기업", 9.93, 3.15)]:
    rect(sl, Inches(x), Inches(1.52), Inches(w_c), Inches(0.08), fill=LG_NAVY)

# 결론 박스
rect(sl, Inches(0.25), Inches(4.42), Inches(12.83), Inches(0.04), fill=LG_RED)
rect(sl, Inches(0.25), Inches(4.5), Inches(12.83), Inches(2.5), fill=LG_LGRAY)
rect(sl, Inches(0.25), Inches(4.5), Inches(0.06), Inches(2.5), fill=LG_RED)
txt(sl, "결론",
    Inches(0.45), Inches(4.55), Inches(12.5), Inches(0.38),
    fs=15, bold=True, color=LG_RED)
ml(sl, [
    "2026 부산 오토매뉴팩·로봇엑스포·빅테크쇼는 로봇·자동화·드론 기술의 현재 수준을 한 자리에서 확인할 수 있는",
    "유의미한 전시회였습니다. 유니트리 로보틱스(G1·R1 휴머노이드, B2 사족보행), DJI(물류·산업용 드론), 성우하이텍",
    "(용접·조립 자동화), BorgWarner(전장 자동화), 쿳션(RaaS 로봇 솔루션) 등 주요 전시 내용을 직접 확인한 결과,",
    "",
    "  ▸ 중국 휴머노이드의 가격 충격($16K) 으로 '도입 여부'가 아닌 '어떤 공정부터' 의 논의로 즉시 전환이 필요하며,",
    "  ▸ AMR·AI 품질검사는 이미 상용 도입 가능 수준에 도달한 것을 현장에서 직접 확인하였습니다.",
    "  ▸ 위 5개 단기 실행 과제를 6개월 이내 착수하여 LG전자 생산기술원의 제조 자동화 역량을 가속화할 것을 제언합니다.",
], Inches(0.45), Inches(4.95), Inches(12.5), Inches(2.0),
   fs=12, color=LG_DARK)


# ── Save ──────────────────────────────────────────────────────────────
out = "/home/user/segamario-fluid-dynamics/roboexpo_2026_관람보고서_LG생산기술원.pptx"
prs.save(out)
print(f"Saved: {out}")
