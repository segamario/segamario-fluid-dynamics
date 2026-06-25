"""
한화시스템 면접 발표 PDF — HTML → weasyprint → PDF
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

BASE_CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
body {
  font-family: 'Noto Sans CJK KR', 'Noto Sans KR', sans-serif;
  font-size: 13px;
  color: #1A1A1A;
  background: white;
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

# ── SLIDE 1
kpi_boxes = ""
for n, l in [("30일 → 15분", "AI 설계 예측"), ("인정시험 90%↓", "김치냉장고"), ("10시간 → 1분", "사출 해석")]:
    kpi_boxes += (
        '<div style="background:#1A2E4A;border-left:4px solid #FF6600;'
        'padding:10px 16px;min-width:180px;margin-right:10px;">'
        '<div style="color:#FF9933;font-size:20px;font-weight:bold;">' + n + '</div>'
        '<div style="color:white;font-size:10px;margin-top:4px;">' + l + '</div></div>'
    )

s1 = (
    '<div class="page" style="background:#1A2E4A;">'
    '<div style="position:absolute;top:0;left:0;bottom:0;width:8px;background:#FF6600;"></div>'
    '<div style="position:absolute;bottom:0;right:0;width:270px;height:120px;background:#FF6600;"></div>'
    '<div style="position:absolute;top:55px;left:30px;">'
    '<div style="color:#FF9933;font-size:14px;font-weight:bold;margin-bottom:12px;">한화시스템 전략부문 지원</div>'
    '<div style="color:white;font-size:36px;font-weight:bold;line-height:1.3;">'
    'AI Factory 전략 전문가<br>홍 창 기</div>'
    '<div style="margin-top:18px;color:#BBBBBB;font-size:12px;line-height:2.1;">'
    'LG전자 생산기술원 전략담당 &nbsp;|&nbsp; 제조혁신 Task Leader (2018~현재)<br>'
    '성균관대학교 기계공학 박사 (CFD/열유체)<br>'
    '그룹 AX Factory 전략 수립 → C-Level 보고 전 사이클 경험</div></div>'
    '<div style="position:absolute;bottom:28px;left:30px;display:flex;">' + kpi_boxes + '</div>'
    '</div>'
)

# ── SLIDE 2
tl_data = [
    ("박사 과정", "2011~2018", LGRAY, DARK, NAVY,
     ["성균관대 기계공학 (CFD)", "오일샌드 국책과제", "국토부 장관표창"]),
    ("기술 전문가", "2018~2021", LGRAY, DARK, NAVY,
     ["LG전자 생산기술원", "CFD 해석 → AI 모델", "성능예측 시스템 구축"]),
    ("전략 기획", "2022~2024", CREAM, DARK, "#993300",
     ["LG그룹 스마트팩토리 2.0", "EY컨설팅 협업", "VIP/사장단 보고"]),
    ("MI Task Leader", "2025~현재", ORANGE, WHITE, "#CC4400",
     ["그룹 제조혁신협의회 총괄", "Physical AI 전략", "AX Factory 로드맵"]),
]

tl_cols = ""
for title, year, bg, fg, hbg, bullets in tl_data:
    bullet_html = "".join("• " + b + "<br>" for b in bullets)
    tl_cols += (
        '<div style="flex:1;background:' + bg + ';margin-right:4px;">'
        '<div style="background:' + hbg + ';padding:6px 10px;">'
        '<div style="color:white;font-weight:bold;font-size:12px;">' + title + '</div>'
        '<div style="color:#FF9933;font-size:10px;">' + year + '</div></div>'
        '<div style="padding:10px;color:' + fg + ';font-size:11px;line-height:1.8;">'
        + bullet_html + '</div></div>'
    )

s2 = (
    '<div class="page">' + header("자기소개", "기술에서 전략으로 — 8년의 여정") + footer() +
    '<div style="position:absolute;top:56px;left:14px;right:14px;bottom:18px;padding:12px 0;">'
    '<div style="height:3px;background:#FF6600;margin:8px 0 12px;"></div>'
    '<div style="display:flex;height:305px;">' + tl_cols + '</div>'
    '<div style="background:#F2F2F2;padding:8px 12px;margin-top:10px;text-align:center;">'
    '<span style="font-weight:bold;color:#1A2E4A;font-size:11px;">'
    '핵심 역량: CAE(CFX/Fluent) &nbsp;·&nbsp; AI/ML/DL &nbsp;·&nbsp; '
    '그룹 전략 기획 &nbsp;·&nbsp; C-Level 보고 &nbsp;·&nbsp; 계열사 코디네이션'
    '</span></div></div></div>'
)

# ── SLIDE 3
motive_data = [
    ("⚠&nbsp; 시장 위기", LGRAY, DARK, NAVY,
     ["국내 소비재·가전 제조업", "중국의 '규모의 경제'에", "글로벌 시장 지위 위협", "", "단순 원가 경쟁 → 한계"]),
    ("→&nbsp; 대응 전략", CREAM, DARK, "#993300",
     ["단기 추격 불가능한", "고신뢰성 산업 집중", "(방산·항공·바이오)", "", "AI Factory + 실용 제조혁신"]),
    ("✓&nbsp; 기여 포인트", ORANGE, WHITE, "#CC4400",
     ["트렌드 센싱", "계열사 코디네이션", "임원진 소통", "", "LG 검증 방법론 즉시 적용"]),
]

m_cols = ""
for title, bg, fg, hbg, lines in motive_data:
    body_html = "".join(l + "<br>" for l in lines)
    m_cols += (
        '<div style="flex:1;background:' + bg + ';margin-right:6px;">'
        '<div style="background:' + hbg + ';padding:8px 12px;font-weight:bold;'
        'color:white;font-size:13px;">' + title + '</div>'
        '<div style="padding:12px;color:' + fg + ';font-size:12px;line-height:1.9;">'
        + body_html + '</div></div>'
    )

s3 = (
    '<div class="page">' + header("지원 동기", "왜 한화시스템인가 — 위기 속 기회") + footer() +
    '<div style="position:absolute;top:56px;left:14px;right:14px;bottom:18px;padding:12px 0;">'
    '<div style="display:flex;height:355px;">' + m_cols + '</div>'
    '<div style="margin-top:8px;padding:8px;background:#FFEEDD;text-align:center;'
    'font-weight:bold;color:#1A2E4A;font-size:12px;">'
    '"소비재를 넘어, 더 높은 신뢰성이 요구되는 방산·항공에서 AI Factory를 완성하고 싶습니다."'
    '</div></div></div>'
)

# ── SLIDE 4
case_data = [
    ("TV Stand", "30일 → 15분", "CAE 성능예측 시간",
     "AI Inverse Net. (Generative Design)",
     ["TV 낙하 해석 자동화 (Altair협업)", "Forward Net → Inverse Net 개발",
      "1,000개 이상 형상 자동 추천", "CAE 엔지니어 고부가 업무 전환"]),
    ("김치냉장고", "인정시험 90%↓", "1만 Case → 800건 이내",
     "AI Surrogate Model (시험 데이터 기반)",
     ["외기조건·제어신호·센서온도 학습", "80%+ 정확도 예측",
      "Grid Search 최소 시험조건 도출", "챔버 유휴 활용률 증가"]),
    ("사출성형", "10시간 → 1분", "사출 CAE 해석 시간",
     "GCNN + MLOps (3D CAD 기반)",
     ["3D CAD + Moldflow 데이터 파싱", "Geodesic CNN (Scale 불변)",
      "MLOps 지속 업데이트 시스템", "CAE 엔지니어 역할 재정의"]),
]

case_cols = ""
for tag, kpi, sub, tech, details in case_data:
    detail_html = "".join("• " + d + "<br>" for d in details)
    case_cols += (
        '<div style="flex:1;background:#F2F2F2;margin-right:6px;">'
        '<div style="background:#1A2E4A;padding:7px;text-align:center;'
        'font-weight:bold;color:white;font-size:13px;">' + tag + '</div>'
        '<div style="text-align:center;padding:10px 6px 4px;">'
        '<div class="kpi-val">' + kpi + '</div>'
        '<div class="kpi-sub">' + sub + '</div></div>'
        '<div style="background:#1A2E4A;margin:0 10px 6px;padding:5px;text-align:center;'
        'color:white;font-size:10px;font-weight:bold;">' + tech + '</div>'
        '<div style="padding:8px 12px;font-size:11px;line-height:1.9;color:#1A1A1A;">'
        + detail_html + '</div></div>'
    )

s4 = (
    '<div class="page">' +
    header("핵심 성과 ①  AI Factory 현장 실증", "전략이 아닌 수치로 증명한 AI 제조 혁신") +
    footer() +
    '<div style="position:absolute;top:56px;left:14px;right:14px;bottom:18px;padding:12px 0;">'
    '<div style="display:flex;height:365px;">' + case_cols + '</div>'
    '<div style="margin-top:6px;padding:8px;background:#FFEEDD;text-align:center;'
    'font-weight:bold;color:#1A2E4A;font-size:11px;">'
    '한화 적용 → 방산 부품 품질검사 &nbsp;·&nbsp; 항공 구조 해석 대체 &nbsp;·&nbsp; '
    'ICT 공정 최적화에 동일 방법론 즉시 적용 가능'
    '</div></div></div>'
)

# ── SLIDE 5
track_data = [
    ("2020~2021", "그룹 C4협의회",
     ["전자·에솔·이노텍·디스플레이·CNS", "Tangible Asset 4건 계열사 확산"], False),
    ("2023", "Smart Factory 2.0 VIP보고",
     ["EY컨설팅 협업", "CAPEX/OPEX 절감 전략", "사장단협의회 보고"], False),
    ("2024", "그룹 제조혁신전략 / Beyond China",
     ["AI기반 전략 VIP 보고", "중국 SCM 활용 전략", "로봇 포함 AI요소기술 분석"], False),
    ("2025~", "MI Task Leader 그룹협의회 통합",
     ["7개 계열사 조율", "C-Level 직접 보고", "Physical AI·DT 신규 분과 운영"], True),
]

t_cols = ""
for year, title, body, hi in track_data:
    bg   = NAVY    if hi else LGRAY
    fg   = WHITE   if hi else DARK
    hbg  = ORANGE  if hi else GRAY
    tfg  = "#FF9933" if hi else NAVY
    body_html = "".join("• " + b + "<br>" for b in body)
    t_cols += (
        '<div style="flex:1;background:' + bg + ';margin-right:4px;">'
        '<div style="background:' + hbg + ';padding:5px 8px;text-align:center;'
        'font-weight:bold;color:white;font-size:11px;">' + year + '</div>'
        '<div style="padding:8px 10px;font-weight:bold;color:' + tfg + ';font-size:12px;'
        'border-bottom:1px solid ' + ('#334466' if hi else '#DDDDDD') + ';">' + title + '</div>'
        '<div style="padding:8px 10px;color:' + fg + ';font-size:11px;line-height:1.9;">'
        + body_html + '</div></div>'
    )

s5 = (
    '<div class="page">' +
    header("핵심 성과 ②  그룹 전략 기획 & C-Level 소통", "기술을 전략 언어로 번역해 임원진을 움직인 경험") +
    footer() +
    '<div style="position:absolute;top:56px;left:14px;right:14px;bottom:18px;padding:12px 0;">'
    '<div style="display:flex;height:365px;">' + t_cols + '</div>'
    '<div style="margin-top:6px;padding:8px;background:#1A2E4A;text-align:center;'
    'font-weight:bold;color:white;font-size:11px;">'
    'EY컨설팅 협업 &nbsp;·&nbsp; 7개 계열사 이해관계 조율 &nbsp;·&nbsp; '
    'VIP/사장단 보고 반복 &nbsp;→&nbsp; 한화 AX 협의체 설계 즉시 수행 가능'
    '</div></div></div>'
)

# ── SLIDE 6
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

s6 = (
    '<div class="page">' +
    header("한화 AX Factory 기여 방안", "LG에서 증명한 것을 한화에서 더 빠르게") +
    footer() +
    '<div style="position:absolute;top:56px;left:14px;right:14px;bottom:18px;padding:12px 0;">'
    '<div style="display:flex;height:365px;">' + c_cols + '</div>'
    '<div style="margin-top:6px;padding:9px;background:#FF6600;text-align:center;'
    'font-weight:bold;color:white;font-size:11px;">'
    "차별점: '그룹 전략 수립 → 계열사 실행 → 성과 측정 → VIP 보고' 전 사이클 경험 → 한화에서 학습 없이 즉시 실행"
    '</div></div></div>'
)

# ── SLIDE 7
bullets_html = ""
for head, body in [
    ("기술 실증력", "수치로 증명된 AI 모델 (30일→15분, 인정시험 90%↓, 10h→1분)"),
    ("전략 기획력", "LG그룹 VIP·사장단 보고, EY컨설팅 공동 전략 수립"),
    ("실행 추진력", "'몽골 코뿔소' — 단기·중장기 프로젝트를 뚝심으로 완수"),
]:
    bullets_html += (
        '<div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">'
        '<div style="width:10px;height:10px;background:white;flex-shrink:0;"></div>'
        '<span style="color:#FF9933;font-weight:bold;font-size:13px;min-width:90px;">' + head + '</span>'
        '<span style="color:white;font-size:13px;">' + body + '</span></div>'
    )

s7 = (
    '<div class="page" style="background:#1A2E4A;">'
    '<div style="position:absolute;top:0;left:0;bottom:0;width:8px;background:#FF6600;"></div>'
    '<div style="position:absolute;bottom:0;left:0;right:0;height:70px;background:#FF6600;"></div>'
    '<div style="position:absolute;top:38px;left:30px;right:30px;">'
    '<div style="color:#FF9933;font-size:14px;font-weight:bold;margin-bottom:14px;">맺음말</div>'
    '<div style="color:white;font-size:20px;font-weight:bold;line-height:1.7;margin-bottom:22px;">'
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

# ── 최종 조합
HTML_FULL = (
    '<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><style>'
    + BASE_CSS +
    '@page { size: 960px 540px; margin: 0; }'
    '</style></head><body>'
    + s1 + s2 + s3 + s4 + s5 + s6 + s7 +
    '</body></html>'
)

html_path = "/tmp/hanwha_slides.html"
pdf_path  = "/home/user/segamario-fluid-dynamics/한화시스템_면접발표_홍창기.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(HTML_FULL)

HTML(html_path).write_pdf(
    pdf_path,
    stylesheets=[CSS(string="@page { size: 960px 540px; margin:0; }")]
)
print("PDF saved:", pdf_path)
print("Size:", os.path.getsize(pdf_path) // 1024, "KB")
