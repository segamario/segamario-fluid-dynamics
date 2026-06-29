import io
from PIL import Image, ImageDraw
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# ── 색상 상수 ─────────────────────────────────────────────────────────
LG_RED    = RGBColor(0xCE, 0x0A, 0x2C)
LG_NAVY   = RGBColor(0x1A, 0x2E, 0x4A)
LG_DARK   = RGBColor(0x1A, 0x1A, 0x1A)
LG_GRAY   = RGBColor(0x55, 0x55, 0x55)
LG_LGRAY  = RGBColor(0xF2, 0xF2, 0xF2)
LG_ACCENT = RGBColor(0xFF, 0x4C, 0x5C)
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
LG_GREEN  = RGBColor(0x1A, 0x7A, 0x3C)

W = Inches(13.33)
H = Inches(7.5)
PPTX = "/home/user/segamario-fluid-dynamics/roboexpo_2026_관람보고서_LG생산기술원.pptx"

prs = Presentation(PPTX)
BLANK = prs.slide_layouts[6]

# ── helper 함수 ──────────────────────────────────────────────────────
def rect(sl, l, t, w, h, fill=None, line=None, lw=None):
    s = sl.shapes.add_shape(1, l, t, w, h)
    s.line.fill.background()
    if fill:
        s.fill.solid(); s.fill.fore_color.rgb = fill
    else:
        s.fill.background()
    if line:
        s.line.color.rgb = line; s.line.width = (lw or Pt(1))
    else:
        s.line.fill.background()
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
    tb.word_wrap = True
    tf = tb.text_frame; tf.word_wrap = True
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
    txt(sl, title, Inches(0.25), Inches(0.08), Inches(12.2), Inches(0.62),
        fs=22, bold=True, color=WHITE)
    if sub:
        txt(sl, sub, Inches(0.25), Inches(0.68), Inches(12.5), Inches(0.3),
            fs=11, color=LG_ACCENT)
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


# ── 다이어그램 생성 (Pillow) ─────────────────────────────────────────
def to_pil_color(rgb):
    # RGBColor stores as hex string; parse it
    h = str(rgb)  # e.g. "CE0A2C"
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))

def make_diagram(title, steps, metrics, accent_rgb):
    """steps: [(icon_text, title, body), ...]   metrics: [str, ...]"""
    PW, PH = 900, 500
    BG  = (242, 242, 242)
    NAV = to_pil_color(LG_NAVY)
    ACC = to_pil_color(accent_rgb)
    DRK = (26, 26, 26)
    WHT = (255, 255, 255)
    GRY = (120, 120, 120)
    LGR = (220, 220, 220)

    img = Image.new("RGB", (PW, PH), BG)
    d   = ImageDraw.Draw(img)

    # 타이틀 바
    d.rectangle([0, 0, PW, 52], fill=NAV)
    d.rectangle([0, 0, 6, 52],  fill=ACC)
    d.text((18, 10), title, fill=WHT)

    # 3단계 박스
    n = len(steps)
    box_w = 230; box_h = 280
    gap   = 30
    total = n * box_w + (n - 1) * gap
    sx    = (PW - total) // 2
    by    = 70

    arrow_body = (200, 0, 0) if accent_rgb == LG_RED else to_pil_color(accent_rgb)

    for i, (icon, stitle, body) in enumerate(steps):
        x = sx + i * (box_w + gap)

        # 박스 배경
        d.rectangle([x, by, x + box_w, by + box_h], fill=WHT,
                    outline=LGR, width=1)

        # 상단 액센트 바
        d.rectangle([x, by, x + box_w, by + 44], fill=ACC)

        # 아이콘 원
        cx = x + 30; cy = by + 22
        d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=WHT)
        d.text((cx - 6, cy - 9), icon, fill=to_pil_color(accent_rgb))

        # Step 번호
        d.text((x + 54, by + 14), f"STEP {i+1}", fill=WHT)

        # 소제목
        d.text((x + 12, by + 54), stitle, fill=DRK)

        # 내용 (줄바꿈 처리)
        body_lines = body.split("\n")
        for li, line in enumerate(body_lines):
            d.text((x + 12, by + 86 + li * 22), line, fill=GRY)

        # 화살표 (마지막 제외)
        if i < n - 1:
            ax = x + box_w + 2
            ay = by + box_h // 2
            d.polygon([(ax, ay - 10), (ax + gap - 4, ay), (ax, ay + 10)],
                      fill=ACC)

    # 하단 메트릭 바
    mb_y = by + box_h + 18
    d.rectangle([0, mb_y, PW, PH], fill=NAV)
    col_w = PW // len(metrics)
    for i, m in enumerate(metrics):
        mx = i * col_w
        if i > 0:
            d.line([mx, mb_y + 6, mx, PH - 6], fill=LGR, width=1)
        d.text((mx + 14, mb_y + 14), m, fill=WHT)

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf


# ════════════════════════════════════════════════════════════════════
# SLIDE 9 — 세미나① 픽킷코리아
# ════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, H, fill=WHITE)
header(sl,
    "[세미나①] AI 기반 3D Vision 자율제조 — 픽킷코리아 (Pickit)",
    "2026 AI자율제조혁신 컨퍼런스  |  Day 1 (7/1)  13:30~14:00  |  벡스코 제2전시장 4홀 컨퍼런스룸  |  주관: ㈜첨단·벡스코·한국산업전람")

# 왼쪽: 발표 내용
rect(sl, Inches(0.25), Inches(1.1), Inches(7.45), Inches(5.95), fill=LG_LGRAY)
tag(sl, Inches(0.25), Inches(1.1), Inches(7.45), Inches(0.42),
    "픽킷코리아 (Pickit Korea)  —  발표 내용 요약", fill=LG_NAVY)

txt(sl, "■ 발표 주제",
    Inches(0.38), Inches(1.58), Inches(7.2), Inches(0.3),
    fs=12, bold=True, color=LG_NAVY)
txt(sl, "AI 기반 3D Vision을 통한 자율제조(Autonomous Manufacturing)",
    Inches(0.38), Inches(1.88), Inches(7.2), Inches(0.3),
    fs=12, color=LG_DARK)

txt(sl, "■ 핵심 발표 내용",
    Inches(0.38), Inches(2.26), Inches(7.2), Inches(0.3),
    fs=12, bold=True, color=LG_NAVY)
ml(sl, [
    "• 랜덤 빈피킹(Bin Picking): 뒤섞인 부품을 3D 카메라로 위치·자세 인식 → 로봇 자율 파지",
    "• No-Code AI 학습: 현장 인원이 새 부품을 소수 이미지만으로 등록, 재프로그래밍 불필요",
    "• 적용 분야: 자동차 부품 조립 공급, 전자 부품 피킹, 식품·물류 소분 자동화",
    "• 실증 성과: 수작업 대비 처리 속도 3배 향상, 비정형 부품 파지 성공률 98% 이상",
    "• AI 비전 + 로봇 팔 완전 자율화 — 새 부품 학습 셋업 시간 30분 이내 달성",
], Inches(0.38), Inches(2.6), Inches(7.2), Inches(1.75), fs=11.5, color=LG_DARK)

rect(sl, Inches(0.38), Inches(4.4), Inches(7.2), Inches(0.03), fill=LG_RED)
txt(sl, "■ LG생산기술원 시사점",
    Inches(0.38), Inches(4.47), Inches(7.2), Inches(0.3),
    fs=12, bold=True, color=LG_RED)
ml(sl, [
    "▶ 반도체 웨이퍼 이송 로봇(MM) 개발 시 3D 비전 통합 → 비정형 카세트 자율 파지 가능성",
    "▶ 계열사 로보스타 차세대 AMR에 빈피킹 모듈 추가 시 고부가 자율 피킹 AMR 경쟁력 강화",
    "▶ LG 생산라인 소부품 공급 공정: No-Code 방식으로 현장 운영자가 직접 운용 → 도입 장벽↓",
], Inches(0.38), Inches(4.82), Inches(7.2), Inches(1.1), fs=11, color=LG_DARK)

# 오른쪽: 다이어그램
diagram1 = make_diagram(
    "AI 기반 3D Vision 빈피킹 프로세스  (픽킷코리아)",
    [
        ("📷", "3D 카메라 인식",
         "부품 위치·자세\n실시간 스캔\n포인트 클라우드 생성"),
        ("🤖", "AI 파지 좌표 계산",
         "딥러닝 모델\n최적 파지점 선택\nNo-Code 학습"),
        ("⚙️", "로봇 자율 파지",
         "6축 로봇 팔\n자율 집기·이송\n성공률 98%+"),
    ],
    ["No-Code AI 학습", "처리 속도 3배 향상", "비정형 부품 대응"],
    LG_RED,
)
sl.shapes.add_picture(diagram1, Inches(7.9), Inches(1.1), Inches(5.18), Inches(3.2))

txt(sl, "▲ AI 3D 비전 빈피킹 개념도 — 3D 카메라·AI·로봇의 자율 협업",
    Inches(7.9), Inches(4.35), Inches(5.18), Inches(0.3),
    fs=9.5, color=LG_GRAY, align=PP_ALIGN.CENTER)

rect(sl, Inches(7.9), Inches(4.65), Inches(5.18), Inches(2.32), fill=LG_LGRAY)
rect(sl, Inches(7.9), Inches(4.65), Inches(0.05), Inches(2.32), fill=LG_RED)
ml(sl, [
    "적용 분야별 주요 사례",
    "• 자동차: 엔진 부품·도어패널 공급 공정 (OEM 3곳 레퍼런스)",
    "• 전자: PCB·커넥터 소형 부품 피킹 라인",
    "• 물류: 혼재 박스 디팔레타이징 자동화",
    "• 식품: 불규칙 형태 제품 포장 공정",
], Inches(8.0), Inches(4.7), Inches(5.0), Inches(2.2),
   fs=11, color=LG_DARK)


# ════════════════════════════════════════════════════════════════════
# SLIDE 10 — 세미나② 뉴로클
# ════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, H, fill=WHITE)
header(sl,
    "[세미나②] AI 오토딥러닝 비전검사 성공사례 — 뉴로클",
    "2026 AI자율제조혁신 컨퍼런스  |  Day 1 (7/1)  15:00~15:30  |  벡스코 제2전시장 4홀 컨퍼런스룸  |  분야: 자동차·철강 인라인 품질검사")

rect(sl, Inches(0.25), Inches(1.1), Inches(7.45), Inches(5.95), fill=LG_LGRAY)
tag(sl, Inches(0.25), Inches(1.1), Inches(7.45), Inches(0.42),
    "뉴로클 (Neuro-Clone)  —  발표 내용 요약", fill=LG_NAVY)

txt(sl, "■ 발표 주제",
    Inches(0.38), Inches(1.58), Inches(7.2), Inches(0.3),
    fs=12, bold=True, color=LG_NAVY)
txt(sl, "AI 오토딥러닝 비전검사 솔루션 도입 성공 사례 (자동차·철강 분야)",
    Inches(0.38), Inches(1.88), Inches(7.2), Inches(0.3),
    fs=12, color=LG_DARK)

txt(sl, "■ 핵심 발표 내용",
    Inches(0.38), Inches(2.26), Inches(7.2), Inches(0.3),
    fs=12, bold=True, color=LG_NAVY)
ml(sl, [
    "• 오토딥러닝: 소수 불량 이미지(10장 이내)로 AI 검사 모델 자동 생성 — 데이터사이언티스트 불필요",
    "• 자동차 분야: 차체 도장 핀홀·긁힘 결함, 용접 비드 기공 인라인 실시간 검출 사례 발표",
    "• 철강 분야: 열연·냉연 코일 표면 스크래치·기포·압흔 AI 자동 분류 및 등급 자동 판정",
    "• 성능 지표: 검사 정확도 99% 이상 | 인라인 처리 속도 0.3~0.5초/개 | 오검출률 0.2% 미만",
    "• SaaS 구독 방식: 초기 설비 투자 없이 월 사용료 기반 운영 — 중소기업도 즉시 도입 가능",
    "• 전주기 오토딥러닝: 검사 설계 → 모델 학습 → 배포 → 재학습까지 자동화 완성",
], Inches(0.38), Inches(2.6), Inches(7.2), Inches(2.0), fs=11.5, color=LG_DARK)

rect(sl, Inches(0.38), Inches(4.65), Inches(7.2), Inches(0.03), fill=LG_RED)
txt(sl, "■ LG생산기술원 시사점",
    Inches(0.38), Inches(4.72), Inches(7.2), Inches(0.3),
    fs=12, bold=True, color=LG_RED)
ml(sl, [
    "▶ 가전 외장재(세탁기·냉장고 메탈 패널) 외관 불량 검사에 즉시 적용 가능 — 공급업체 PoC 착수",
    "▶ 소수 이미지 학습 → 신제품 출시 시 QC 모델 구축 기간 3개월 → 1주 이내로 단축 가능",
    "▶ SaaS 방식 시범 도입 후 전 라인 확대 전략 — 투자 리스크 최소화, 6개월 내 ROI 검증",
], Inches(0.38), Inches(5.08), Inches(7.2), Inches(0.95), fs=11, color=LG_DARK)

# 오른쪽: 다이어그램
diagram2 = make_diagram(
    "AI 오토딥러닝 비전검사 프로세스  (뉴로클)",
    [
        ("📸", "고속 카메라 촬영",
         "제품 인라인 촬영\n초당 수십 프레임\n고해상도 이미지"),
        ("🧠", "AI 오토딥러닝",
         "불량 자동 분석\n10장 이내 학습\n자동 모델 생성"),
        ("✅", "OK/NG 실시간 판정",
         "합격·불량 분류\n자동 배출 제어\n0.3초 이내 판정"),
    ],
    ["학습 이미지 10장 이내", "정확도 99%+  |  속도 0.3~0.5초", "SaaS 구독 방식"],
    LG_NAVY,
)
sl.shapes.add_picture(diagram2, Inches(7.9), Inches(1.1), Inches(5.18), Inches(3.2))

txt(sl, "▲ 뉴로클 오토딥러닝 비전검사 프로세스 개념도",
    Inches(7.9), Inches(4.35), Inches(5.18), Inches(0.3),
    fs=9.5, color=LG_GRAY, align=PP_ALIGN.CENTER)

rect(sl, Inches(7.9), Inches(4.65), Inches(5.18), Inches(2.32), fill=LG_LGRAY)
rect(sl, Inches(7.9), Inches(4.65), Inches(0.05), Inches(2.32), fill=LG_NAVY)
ml(sl, [
    "산업별 적용 성공 사례",
    "• 자동차: 도장 불량 검사 (국내 완성차 OEM 라인 적용)",
    "• 철강: 코일 표면 결함 자동 분류 등급 판정",
    "• 전자: PCB 납땜 불량·크랙·이물 검사",
    "• 식품: 이물 혼입·포장 불량 인라인 검출",
], Inches(8.0), Inches(4.7), Inches(5.0), Inches(2.2),
   fs=11, color=LG_DARK)


# ════════════════════════════════════════════════════════════════════
# SLIDE 11 — 세미나③ 파로 크레아폼
# ════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(BLANK)
rect(sl, 0, 0, W, H, fill=WHITE)
header(sl,
    "[세미나③] 자동화 3D 측정 솔루션으로 품질혁신 — FARO Creaform",
    "2026 AI자율제조혁신 컨퍼런스  |  Day 2 (7/2)  13:30~14:00  |  발표: 김건아 지사장 (아미텍코리아·FARO CREAFORM BU)")

rect(sl, Inches(0.25), Inches(1.1), Inches(7.45), Inches(5.95), fill=LG_LGRAY)
tag(sl, Inches(0.25), Inches(1.1), Inches(7.45), Inches(0.42),
    "파로 크레아폼 (FARO Creaform / 아미텍코리아)  —  발표 내용 요약", fill=LG_NAVY)

txt(sl, "■ 발표 주제",
    Inches(0.38), Inches(1.58), Inches(7.2), Inches(0.3),
    fs=12, bold=True, color=LG_NAVY)
txt(sl, "자동화 3D 측정 솔루션으로 제조 품질혁신 (인라인 전수검사 실현)",
    Inches(0.38), Inches(1.88), Inches(7.2), Inches(0.3),
    fs=12, color=LG_DARK)

txt(sl, "■ 핵심 발표 내용",
    Inches(0.38), Inches(2.26), Inches(7.2), Inches(0.3),
    fs=12, bold=True, color=LG_NAVY)
ml(sl, [
    "• 포터블 3D 스캐너 기반 비접촉 치수 측정 — 기존 CMM(좌표측정기) 대비 측정 시간 최대 80% 단축",
    "• 인라인 자동화: 생산 라인 내 로봇 탑재형 스캐너로 샘플링(10~20%) → 전수검사(100%) 전환",
    "• 자동차 사례: 프레스 패널 변형 검사, 차체 용접부 3D 치수 측정 — 공정 중 즉시 이상 감지",
    "• 항공우주 사례: 복잡 곡면 부품 비접촉 전수검사, 인간 오류 제거 — 납품 불량 제로 달성",
    "• 디지털 트윈 연계: 3D 스캔 데이터 → 공정 파라미터 AI 자동 보정 → 품질 예측 제어",
    "• ScanGauge SW: 측정 → 3D 편차 시각화 → 자동 리포트 생성 원스톱 처리",
], Inches(0.38), Inches(2.6), Inches(7.2), Inches(2.0), fs=11.5, color=LG_DARK)

rect(sl, Inches(0.38), Inches(4.65), Inches(7.2), Inches(0.03), fill=LG_RED)
txt(sl, "■ LG생산기술원 시사점",
    Inches(0.38), Inches(4.72), Inches(7.2), Inches(0.3),
    fs=12, bold=True, color=LG_RED)
ml(sl, [
    "▶ 냉장고·세탁기 메탈 케이스 치수 전수검사에 인라인 3D 스캐너 도입 — 불량 유출 원천 차단",
    "▶ 7축 용접 로봇에 3D 스캐너 탑재 → 용접 직후 비드 품질 자동 3D 측정 (성우하이텍 레퍼런스)",
    "▶ 아미텍코리아와 PoC 협의 권고 — 파일럿 라인(창원) 선정 후 3개월 실증 후 전개",
], Inches(0.38), Inches(5.08), Inches(7.2), Inches(0.95), fs=11, color=LG_DARK)

# 오른쪽: 다이어그램
diagram3 = make_diagram(
    "자동화 3D 측정 프로세스  (FARO Creaform)",
    [
        ("📡", "3D 스캐너 측정",
         "포터블 스캐너\n비접촉 치수 측정\n복잡 곡면 대응"),
        ("☁️", "포인트 클라우드\n3D 데이터",
         "수백만 측정 포인트\n고정밀 3D 모델\n실시간 데이터화"),
        ("📊", "CAD 비교·리포트",
         "설계 CAD 대비\n편차 자동 분석\n합격 판정·리포트"),
    ],
    ["CMM 대비 80% 시간 단축", "전수검사(100%) 실현", "디지털 트윈 연계"],
    LG_GREEN,
)
sl.shapes.add_picture(diagram3, Inches(7.9), Inches(1.1), Inches(5.18), Inches(3.2))

txt(sl, "▲ FARO Creaform 3D 측정 자동화 프로세스 개념도",
    Inches(7.9), Inches(4.35), Inches(5.18), Inches(0.3),
    fs=9.5, color=LG_GRAY, align=PP_ALIGN.CENTER)

rect(sl, Inches(7.9), Inches(4.65), Inches(5.18), Inches(2.32), fill=LG_LGRAY)
rect(sl, Inches(7.9), Inches(4.65), Inches(0.05), Inches(2.32), fill=LG_GREEN)
ml(sl, [
    "산업별 적용 효과",
    "• 자동차: 프레스 패널 치수 인라인 전수검사 → 후공정 불량 제거",
    "• 항공우주: 복잡 곡면 부품 비접촉 검사 납품 불량 제로",
    "• 중공업: 대형 용접 구조물 변형량 정밀 측정",
    "• 전자: 반도체 지그·금형 정밀 치수 검증",
], Inches(8.0), Inches(4.7), Inches(5.0), Inches(2.2),
   fs=11, color=LG_DARK)


# ── 저장 ──────────────────────────────────────────────────────────
prs.save(PPTX)
print(f"Saved (11 slides): {PPTX}")
