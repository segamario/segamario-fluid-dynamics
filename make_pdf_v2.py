"""
한화시스템 면접 발표 PDF v2
- 수정된 PPT 6슬라이드 내용 반영
- 전략 문서 기반 신규 2슬라이드 추가 (총 8슬라이드)
"""
from weasyprint import HTML, CSS
import os

ORANGE  = "#FF6600"
ORANGE2 = "#FF9933"
NAVY    = "#1A2E4A"
DARK    = "#1A1A1A"
GRAY    = "#555555"
LGRAY   = "#F2F2F2"
CREAM   = "#FFEEDD"
WHITE   = "#FFFFFF"
DGRAY   = "#2A3A50"

BASE_CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
body {
  font-family: 'Noto Sans CJK KR', 'Noto Sans KR', sans-serif;
  font-size: 13px; color: #1A1A1A; background: white;
}
.page {
  width: 960px; height: 540px;
  position: relative; overflow: hidden;
  page-break-after: always; background: white;
}
.page:last-child { page-break-after: avoid; }
.kpi-val { font-size:26px; font-weight:bold; color:#FF6600; line-height:1.1; }
.kpi-sub { font-size:10px; color:#555555; }
"""

def footer():
    return (
        '<div style="position:absolute;bottom:0;left:0;right:0;height:18px;'
        'background:#1A2E4A;display:flex;align-items:center;padding:0 12px;">'
        '<span style="color:white;font-size:8px;">홍창기 &nbsp;|&nbsp; 한화시스템 전략부문</span>'
        '<span style="color:white;font-size:8px;margin-left:auto;">2026</span></div>'
    )

def header(title, sub=""):
    sub_html = ''
    if sub:
        sub_html = ('<div style="position:absolute;top:36px;left:18px;'
                    'color:#FF9933;font-size:11px;">' + sub + '</div>')
    return (
        '<div style="position:absolute;top:0;left:0;right:0;height:56px;background:#1A2E4A;">'
        '<div style="position:absolute;top:0;left:0;bottom:0;width:6px;background:#FF6600;"></div>'
        '<div style="position:absolute;top:8px;left:18px;color:white;font-size:18px;font-weight:bold;">'
        + title + '</div>' + sub_html + '</div>'
    )

# ══════════════════════════════════════════
# SLIDE 1 — 타이틀 (수정 반영)
# ══════════════════════════════════════════
kpi_boxes = ""
for n, l in [("30일 → 15분","AI 설계 예측"), ("인정시험 90%↓","인정시험 감소"), ("10h → 1분","사출 해석")]:
    kpi_boxes += (
        '<div style="background:#1A2E4A;border-left:4px solid #FF6600;'
        'padding:8px 14px;margin-right:8px;">'
        '<div style="color:#FF9933;font-size:18px;font-weight:bold;">' + n + '</div>'
        '<div style="color:white;font-size:9px;margin-top:3px;">' + l + '</div></div>'
    )
strategy_box = (
    '<div style="background:#1A2E4A;border-left:4px solid #FF6600;'
    'padding:8px 14px;margin-right:8px;">'
    '<div style="color:#FF9933;font-size:13px;font-weight:bold;line-height:1.6;">'
    'c4협의회 / 제조혁신사무국 운영<br>Beyond China / 제조혁신 전략 수립</div></div>'
)

s1 = (
    '<div class="page" style="background:#1A2E4A;">'
    '<div style="position:absolute;top:0;left:0;bottom:0;width:8px;background:#FF6600;"></div>'
    '<div style="position:absolute;bottom:0;right:0;width:260px;height:110px;background:#FF6600;"></div>'
    '<div style="position:absolute;top:48px;left:30px;">'
    '<div style="color:#FF9933;font-size:13px;font-weight:bold;margin-bottom:10px;">한화시스템 전략부문</div>'
    '<div style="color:white;font-size:34px;font-weight:bold;line-height:1.3;">'
    'AI Factory 전략 전문가<br>홍 창 기</div>'
    '<div style="margin-top:14px;color:#BBBBBB;font-size:11px;line-height:2.0;">'
    'LG전자 생산기술원 전략담당 &nbsp;|&nbsp; 제조혁신 Task Leader (2025~현재)<br>'
    '성균관대학교 기계공학 박사 (CFD/열유체)<br>'
    '그룹 AX Factory 전략 수립 → C-Level 보고 전 사이클 경험<br>'
    '울산산업정보원 (스마트팩토리) / 국토교통과학기술진흥원 자문 위원</div></div>'
    '<div style="position:absolute;bottom:25px;left:30px;display:flex;align-items:stretch;">'
    + kpi_boxes + strategy_box +
    '</div></div>'
)

# ══════════════════════════════════════════
# SLIDE 2 — 자기소개 (수정 반영)
# ══════════════════════════════════════════
tl_data = [
    ("박사 과정", "2011~2018", LGRAY, DARK, NAVY,
     ["성균관대 기계공학 (CFD)", "ADD과제 (화생방 가상검증)", "오일샌드 국책과제", "국토부 장관표창", "ICOG 2014~2019 사무국"]),
    ("기술 전문가", "2018~2021", LGRAY, DARK, NAVY,
     ["LG전자 생산기술원", "CFD 기반 가상검증 개발", "Data Driven 성능예측 모델", "(TV Stand/김치냉장고/사출)", "그룹 C4협의회 운영"]),
    ("전략 기획", "2022~2024", CREAM, DARK, "#993300",
     ["스마트팩토리 2.0 전략 수립", "(엔솔/전자/공정혁신, VIP보고)", "그룹 생산기술협의회 운영", "Beyond China 제조전략", "(w.EY컨설팅)"]),
    ("MI Task Leader", "2025~현재", ORANGE, WHITE, "#CC4400",
     ["그룹 제조혁신협의회 사무국", "제조 BM 프로그램 운영", "제조 Physical AI 전략 수립", "AX Factory 전략 수립", "VIP 보고"]),
]

tl_cols = ""
for title, year, bg, fg, hbg, bullets in tl_data:
    bullet_html = "".join("• " + b + "<br>" for b in bullets)
    tl_cols += (
        '<div style="flex:1;background:' + bg + ';margin-right:4px;">'
        '<div style="background:' + hbg + ';padding:5px 8px;">'
        '<div style="color:white;font-weight:bold;font-size:12px;">' + title + '</div>'
        '<div style="color:#FF9933;font-size:10px;">' + year + '</div></div>'
        '<div style="padding:8px 10px;color:' + fg + ';font-size:10.5px;line-height:1.7;">'
        + bullet_html + '</div></div>'
    )

s2 = (
    '<div class="page">' + header("자기소개", "기술에서 전략으로 — 8년의 여정") + footer() +
    '<div style="position:absolute;top:56px;left:14px;right:14px;bottom:18px;padding:10px 0;">'
    '<div style="height:3px;background:#FF6600;margin:6px 0 10px;"></div>'
    '<div style="display:flex;height:310px;">' + tl_cols + '</div>'
    '<div style="background:#F2F2F2;padding:7px 12px;margin-top:8px;text-align:center;">'
    '<span style="font-weight:bold;color:#1A2E4A;font-size:11px;">'
    '핵심 역량: CAE (CFX/Fluent) &nbsp;·&nbsp; AI/ML/DL &nbsp;·&nbsp; '
    '그룹 전략 기획 &nbsp;·&nbsp; C-Level 보고 &nbsp;·&nbsp; 계열사 코디네이션'
    '</span></div></div></div>'
)

# ══════════════════════════════════════════
# SLIDE 3 — AI 성과 (수정 반영)
# ══════════════════════════════════════════
case_data = [
    ("TV Stand", "30일 → 15분", "CAE 성능예측 시간",
     "AI Inverse Net. (Generative Design)",
     ["TV 낙하 해석 자동화, ROM (Altair협업)", "Forward Net → Inverse Net 개발",
      "1,000개 이상 형상 자동 추천", "CAE 엔지니어 고부가 업무 전환"]),
    ("김치냉장고", "인정시험 90%↓", "1만 Case → 800건 → 120건 이내",
     "AI Surrogate Model (시험 데이터 기반)",
     ["외기조건·제어신호·센서온도 학습", "80%+ 정확도 예측",
      "Grid Search 최소 시험조건 도출", "챔버 유휴 활용률 증가"]),
    ("사출성형", "10시간 → 1분", "사출 CAE 해석 시간",
     "GCNN + MLOps (3D CAD 기반)",
     ["3D CAD + Moldflow 데이터 파싱", "Geodesic CNN (Scale 불변)",
      "Advanced Sampling 기법 개발", "ROM기반 Real time Simulation"]),
]

case_cols = ""
for tag, kpi, sub, tech, details in case_data:
    detail_html = "".join("• " + d + "<br>" for d in details)
    case_cols += (
        '<div style="flex:1;background:#F2F2F2;margin-right:6px;">'
        '<div style="background:#1A2E4A;padding:7px;text-align:center;'
        'font-weight:bold;color:white;font-size:13px;">' + tag + '</div>'
        '<div style="text-align:center;padding:8px 6px 4px;">'
        '<div class="kpi-val">' + kpi + '</div>'
        '<div class="kpi-sub">' + sub + '</div></div>'
        '<div style="background:#1A2E4A;margin:0 10px 6px;padding:5px;text-align:center;'
        'color:white;font-size:10px;font-weight:bold;">' + tech + '</div>'
        '<div style="padding:8px 12px;font-size:11px;line-height:1.8;color:#1A1A1A;">'
        + detail_html + '</div></div>'
    )

s3 = (
    '<div class="page">' +
    header("핵심 성과 ①  AI Factory 현장 실증", "전략이 아닌 수치로 증명한 AI 제조 혁신") +
    footer() +
    '<div style="position:absolute;top:56px;left:14px;right:14px;bottom:18px;padding:10px 0;">'
    '<div style="display:flex;height:368px;">' + case_cols + '</div>'
    '<div style="margin-top:6px;padding:7px;background:#FFEEDD;text-align:center;'
    'font-weight:bold;color:#1A2E4A;font-size:11px;">'
    '한화 적용 → 방산 부품 품질검사 &nbsp;·&nbsp; 항공 구조 해석 대체 &nbsp;·&nbsp; '
    'ICT 공정 최적화에 동일 방법론 즉시 적용 가능'
    '</div></div></div>'
)

# ══════════════════════════════════════════
# SLIDE 4 — 그룹 전략 기획 (수정 반영)
# ══════════════════════════════════════════
track_data = [
    ("2020~2021", "그룹 C4협의회",
     ["전자·엔솔·이노텍·디스플레이·CNS", "Tangible Asset 4건 계열사 확산"], False),
    ("2023", "공정혁신 기반 Smart Factory VIP 보고",
     ["CAPEX/OPEX 절감 전략", "(w.EY컨설팅) 사장단협의회 보고", "그룹 생산기술협의회 운영"], False),
    ("2024", "그룹 제조혁신전략 / Beyond China",
     ["AI기반 전략, VIP 보고", "중국 SCM 활용 전략 도출", "엔솔/CNS/생산기술원 Co-Task 간사"], False),
    ("2025~", "MI Task Leader",
     ["그룹제조혁신 협의회 사무국", "생산기술/공정기술/C4 통합→협의회 발족",
      "Physical AI·DT 신규 분과 기획", "Autonomous Factory 전략 수립"], True),
]

t_cols = ""
for year, title, body, hi in track_data:
    bg  = NAVY    if hi else LGRAY
    fg  = WHITE   if hi else DARK
    hbg = ORANGE  if hi else GRAY
    tfg = "#FF9933" if hi else NAVY
    body_html = "".join("• " + b + "<br>" for b in body)
    t_cols += (
        '<div style="flex:1;background:' + bg + ';margin-right:4px;">'
        '<div style="background:' + hbg + ';padding:5px 8px;text-align:center;'
        'font-weight:bold;color:white;font-size:11px;">' + year + '</div>'
        '<div style="padding:7px 10px;font-weight:bold;color:' + tfg + ';font-size:12px;'
        'border-bottom:1px solid ' + ('#334466' if hi else '#DDDDDD') + ';">' + title + '</div>'
        '<div style="padding:7px 10px;color:' + fg + ';font-size:10.5px;line-height:1.7;">'
        + body_html + '</div></div>'
    )

s4 = (
    '<div class="page">' +
    header("핵심 성과 ②  그룹 전략 기획 & C-Level 소통", "기술을 전략 언어로 번역해 임원진을 움직인 경험") +
    footer() +
    '<div style="position:absolute;top:56px;left:14px;right:14px;bottom:18px;padding:10px 0;">'
    '<div style="display:flex;height:368px;">' + t_cols + '</div>'
    '<div style="margin-top:6px;padding:7px;background:#1A2E4A;text-align:center;'
    'font-weight:bold;color:white;font-size:11px;">'
    'EY컨설팅 협업 &nbsp;·&nbsp; 7개 계열사 이해관계 조율 &nbsp;·&nbsp; '
    'VIP/사장단 보고 반복 &nbsp;→&nbsp; 한화 AX 협의체 설계 즉시 수행 가능'
    '</div></div></div>'
)

# ══════════════════════════════════════════
# SLIDE 5 — [NEW] 한화그룹 AI Factory 마스터 전략
# ══════════════════════════════════════════
s5 = (
    '<div class="page">' +
    header("한화그룹 AI Factory 마스터 전략", "The Neural Factory — Smart에서 Autonomous로의 패러다임 전환") +
    footer() +
    '<div style="position:absolute;top:56px;left:0;right:0;bottom:18px;">'

    # 상단: Smart → AI Factory 비교
    '<div style="display:flex;margin:10px 14px 8px;gap:6px;">'

    '<div style="flex:1;background:#F2F2F2;border-top:3px solid #888888;padding:8px 12px;">'
    '<div style="font-weight:bold;color:#555;font-size:12px;margin-bottom:6px;">Smart Factory (현재)</div>'
    '<div style="font-size:11px;color:#333;line-height:1.8;">'
    '• 운영: 사전 정의 시나리오 기반 효율 최적화<br>'
    '• 의사결정: 사람 중심 판단, Rule 기반 최적화<br>'
    '• 추진: 수동형 분석/예측 (AI Assistant)'
    '</div></div>'

    '<div style="flex:0 0 40px;display:flex;align-items:center;justify-content:center;">'
    '<div style="font-size:24px;color:#FF6600;font-weight:bold;">→</div></div>'

    '<div style="flex:1;background:#1A2E4A;border-top:3px solid #FF6600;padding:8px 12px;">'
    '<div style="font-weight:bold;color:#FF9933;font-size:12px;margin-bottom:6px;">AI Factory (목표)</div>'
    '<div style="font-size:11px;color:white;line-height:1.8;">'
    '• 운영: 목표 기반 자율 판단 및 적용 (End-to-End)<br>'
    '• 의사결정: AI 주도, Model/Policy 기반 Closed Loop 제어<br>'
    '• 추진: 능동형 무결점 자율제조 (Physical AI·Agentic AI)'
    '</div></div>'
    '</div>'

    # 하단: 3대 축
    '<div style="display:flex;margin:0 14px;gap:6px;height:195px;">'

    '<div style="flex:1;background:#FFEEDD;border-left:4px solid #FF6600;padding:10px 12px;">'
    '<div style="font-weight:bold;color:#FF6600;font-size:13px;">AX (Process)</div>'
    '<div style="font-size:10px;color:#993300;margin-bottom:6px;">인지의 지능화</div>'
    '<div style="font-size:11px;color:#333;line-height:1.7;">'
    '사람 중심에서 AI 의사결정으로<br>분절된 업무 흐름을 단일화<br>Multi Agent System 구현'
    '</div></div>'

    '<div style="flex:1;background:#F2F2F2;border-left:4px solid #1A2E4A;padding:10px 12px;">'
    '<div style="font-weight:bold;color:#1A2E4A;font-size:13px;">RX (Physical)</div>'
    '<div style="font-size:10px;color:#555;margin-bottom:6px;">물리적 제어</div>'
    '<div style="font-size:11px;color:#333;line-height:1.7;">'
    '고정된 펜스를 벗어난 유연 로봇<br>현장 신호를 스스로 판단<br>Adaptive Control 구현'
    '</div></div>'

    '<div style="flex:1;background:#1A2E4A;border-left:4px solid #FF6600;padding:10px 12px;">'
    '<div style="font-weight:bold;color:#FF9933;font-size:13px;">VX (System)</div>'
    '<div style="font-size:10px;color:#FF9933;margin-bottom:6px;">가상 시뮬레이션</div>'
    '<div style="font-size:11px;color:white;line-height:1.7;">'
    '디지털 트윈으로 모든 변수 가상 검증<br>Closed-Loop으로 현실과 동기화<br>Software-Defined Factory 기반'
    '</div></div>'

    '<div style="flex:1;background:#2A3A50;border-left:4px solid #FF9933;padding:10px 12px;">'
    '<div style="font-weight:bold;color:#FF9933;font-size:13px;">양대 엔진</div>'
    '<div style="font-size:10px;color:#FF9933;margin-bottom:6px;">인지 + 물리 결합</div>'
    '<div style="font-size:11px;color:white;line-height:1.7;">'
    '<span style="color:#FF9933;">LLM Agent</span>: 자연어 처리,<br>도면/언어 해석, 지시·통합<br>'
    '<span style="color:#FF9933;">Physical AI</span>: 실시간 진동/<br>열변형 연산, 적응 제어'
    '</div></div>'

    '</div>'
    '</div></div>'
)

# ══════════════════════════════════════════
# SLIDE 6 — [NEW] 계열사별 AX 전략 (16대 시나리오)
# ══════════════════════════════════════════
affiliates = [
    ("#FF6600", "한화오션", "조선·해양",
     "다국적 통역 Agent<br>용접 비드 품질 가이드 AI",
     "아드 블록 자율 오케스트레이션<br>물리-정밀 용접 하이브리드 로봇"),
    ("#1A2E4A", "한화에어로스페이스", "우주항공·방산",
     "조립 AI 정석 Agent<br>MRO 부품 식별 웨어러블",
     "디지털 성적서 자동 발행<br>CNC 난삭재 채터링 능동 상쇄"),
    ("#334455", "한화모멘텀", "기계·자동화",
     "설계 변경 이력 역추적<br>물류 자율 보정",
     "CFD 대리모델 → PLC Code 자동 생성<br>무인 오케스트레이션·가상 시뮬런"),
    ("#993300", "한화솔루션", "에너지·소재",
     "이상 징후/DCS 연동<br>불량 원인 자율 추적",
     "PINN 기반 콤플렉스 유동 제어<br>실시간 MPC 최적화 Agent"),
]

aff_cols = ""
for color, name, sector, micro, macro in affiliates:
    aff_cols += (
        '<div style="flex:1;margin-right:5px;display:flex;flex-direction:column;">'
        # 헤더
        '<div style="background:' + color + ';padding:7px 10px;">'
        '<div style="color:white;font-weight:bold;font-size:13px;">' + name + '</div>'
        '<div style="color:rgba(255,255,255,0.8);font-size:10px;">' + sector + '</div>'
        '</div>'
        # Micro
        '<div style="background:#F2F2F2;padding:8px 10px;flex:1;border-bottom:1px solid #ddd;">'
        '<div style="color:#FF6600;font-weight:bold;font-size:10px;margin-bottom:4px;">▶ Micro (현장 즉착형 ROI)</div>'
        '<div style="font-size:11px;color:#333;line-height:1.7;">' + micro + '</div>'
        '</div>'
        # Macro
        '<div style="background:#1A2E4A;padding:8px 10px;flex:1;">'
        '<div style="color:#FF9933;font-weight:bold;font-size:10px;margin-bottom:4px;">▶ Macro (미래 준비형 SDF)</div>'
        '<div style="font-size:11px;color:white;line-height:1.7;">' + macro + '</div>'
        '</div>'
        '</div>'
    )

s6 = (
    '<div class="page">' +
    header("한화그룹 계열사별 AX 전략", "16대 마스터 시나리오 — Micro(즉착형 ROI) + Macro(미래 준비형 SDF)") +
    footer() +
    '<div style="position:absolute;top:56px;left:14px;right:14px;bottom:18px;padding:10px 0;">'
    '<div style="display:flex;height:380px;">' + aff_cols + '</div>'
    '<div style="margin-top:7px;padding:7px 14px;background:#FF6600;'
    'display:flex;align-items:center;justify-content:center;">'
    '<span style="color:white;font-weight:bold;font-size:11px;">'
    '현장 즉착형 ROI로 조기 성과 확보 → SDF(Software-Defined Factory) 전환으로 Autonomous Factory 완성'
    '</span></div></div></div>'
)

# ══════════════════════════════════════════
# SLIDE 7 — 기여 방안 (기존 유지)
# ══════════════════════════════════════════
contrib_data = [
    ("① AX 로드맵 설계",
     ["한화에어로스페이스·한화오션·한화솔루션 등", "계열사 특성별 AX Factory 로드맵 수립",
      "", "ROI 기반 우선순위 설정", "→ 맹목적 자동화 방지", "→ LCC/고신뢰 공장 차별화"]),
    ("② 기술 ↔ 전략 브릿지",
     ["CAE·AI·Digital Twin을 전략 언어로 번역", "",
      "현장 엔지니어 ↔ 임원 가교", "실현 가능성 기반 전략 설계",
      "→ 투자 실패 리스크 최소화", ""]),
    ("③ Physical AI 선제 적용",
     ["2026년 직접 수립한", "Physical AI·Agentic AI·DT 전략을", "방산·항공 제조에 적용",
      "", "무인화·AI 의사결정 체계 구축", "→ 한화 AX Factory 선도"]),
]

c_cols = ""
for title, lines in contrib_data:
    body_html = "".join((l if l else "&nbsp;") + "<br>" for l in lines)
    c_cols += (
        '<div style="flex:1;background:#F2F2F2;margin-right:6px;'
        'border-left:5px solid #FF6600;">'
        '<div style="background:#1A2E4A;padding:8px 12px;font-weight:bold;'
        'color:white;font-size:13px;">' + title + '</div>'
        '<div style="padding:12px;font-size:12px;line-height:1.9;color:#1A1A1A;">'
        + body_html + '</div></div>'
    )

s7 = (
    '<div class="page">' +
    header("한화 AX Factory 기여 방안", "LG에서 증명한 것을 한화에서 더 빠르게") +
    footer() +
    '<div style="position:absolute;top:56px;left:14px;right:14px;bottom:18px;padding:10px 0;">'
    '<div style="display:flex;height:368px;">' + c_cols + '</div>'
    '<div style="margin-top:6px;padding:9px;background:#FF6600;text-align:center;'
    'font-weight:bold;color:white;font-size:11px;">'
    "차별점: '그룹 전략 수립 → 계열사 실행 → 성과 측정 → VIP 보고' 전 사이클 경험 → 한화에서 학습 없이 즉시 실행"
    '</div></div></div>'
)

# ══════════════════════════════════════════
# SLIDE 8 — 클로징
# ══════════════════════════════════════════
bullets_html = ""
for head, body in [
    ("기술 실증력", "수치로 증명된 AI 모델 (30일→15분, 인정시험 90%↓, 10h→1분)"),
    ("전략 기획력", "LG그룹 VIP·사장단 보고, EY컨설팅 공동 전략 수립"),
    ("실행 추진력", "'몽골 코뿔소' — 단기·중장기 프로젝트를 뚝심으로 완수"),
]:
    bullets_html += (
        '<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">'
        '<div style="width:10px;height:10px;background:white;flex-shrink:0;"></div>'
        '<span style="color:#FF9933;font-weight:bold;font-size:13px;min-width:90px;">' + head + '</span>'
        '<span style="color:white;font-size:13px;">' + body + '</span></div>'
    )

s8 = (
    '<div class="page" style="background:#1A2E4A;">'
    '<div style="position:absolute;top:0;left:0;bottom:0;width:8px;background:#FF6600;"></div>'
    '<div style="position:absolute;bottom:0;left:0;right:0;height:70px;background:#FF6600;"></div>'
    '<div style="position:absolute;top:36px;left:30px;right:30px;">'
    '<div style="color:#FF9933;font-size:14px;font-weight:bold;margin-bottom:12px;">맺음말</div>'
    '<div style="color:white;font-size:20px;font-weight:bold;line-height:1.7;margin-bottom:20px;">'
    "저는 AI Factory를 '개념'이 아닌 '성과'로 만들어 왔습니다.<br>"
    'LG그룹 8년간 전략 수립부터 현장 실증까지 전 과정을 경험했고,<br>'
    '그 역량을 한화그룹 AX Factory 가속화에 즉시 투입하겠습니다.</div>'
    + bullets_html +
    '</div>'
    '<div style="position:absolute;bottom:20px;left:30px;color:#1A2E4A;'
    'font-weight:bold;font-size:13px;">'
    '홍 창 기 &nbsp;|&nbsp; 한화시스템 전략부문 지원 &nbsp;|&nbsp; 2026</div>'
    '</div>'
)

# ══════════════════════════════════════════
# 조합 & 렌더링
# ══════════════════════════════════════════
HTML_FULL = (
    '<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><style>'
    + BASE_CSS +
    '@page { size: 960px 540px; margin: 0; }'
    '</style></head><body>'
    + s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 +
    '</body></html>'
)

html_path = "/tmp/hanwha_slides_v2.html"
pdf_path  = "/home/user/segamario-fluid-dynamics/한화시스템_면접발표_홍창기_v2.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(HTML_FULL)

HTML(html_path).write_pdf(
    pdf_path,
    stylesheets=[CSS(string="@page { size: 960px 540px; margin:0; }")]
)
print("PDF saved:", pdf_path)
print("Size:", os.path.getsize(pdf_path) // 1024, "KB")
