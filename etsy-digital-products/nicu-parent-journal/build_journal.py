"""
A NICU Journal — printable PDF for parents with a baby in the NICU.
Deliberately calmer than the rest of the Little Milestone Co. line: muted
lavender / sage / slate palette instead of bright pink & yellow, minimal
emoji, no language that presumes an outcome or timeline. Not a medical
record — an organizing and feeling-through-it tool only.
"""
import os
from playwright.sync_api import sync_playwright

DIR = os.path.dirname(os.path.abspath(__file__))

CALM = {
    'bg': '#F6F4F7',
    'lavender': '#DCD3EF', 'lavenderDark': '#B4A0DE',
    'sage': '#D7E5DA', 'sageDark': '#A9C7B0',
    'slate': '#D7E1EC', 'slateDark': '#9FB6CE',
    'rose': '#E3D2D8', 'roseDark': '#C79FB0',
    'text': '#454045', 'sub': '#8D8390',
}
ACCENTS = [CALM['lavenderDark'], CALM['sageDark'], CALM['slateDark'], CALM['roseDark']]

PAGES = []


def brand_footer(pagenum):
    return (f'<div style="position:absolute;bottom:26px;left:60px;right:60px;display:flex;'
            f'justify-content:space-between;align-items:center;">'
            f'<div style="font-size:11px;color:{CALM["sub"]};font-weight:600;letter-spacing:2px;">LITTLE MILESTONE CO.</div>'
            f'<div style="font-size:12px;color:#c2bcc4;">{pagenum}</div></div>')


def page(inner, bg="#FFFFFF", pagenum=""):
    PAGES.append(
        f'<div class="page" style="background:{bg};">'
        f'<div style="position:absolute;top:0;left:0;right:0;bottom:0;padding:56px 56px 66px 56px;">{inner}</div>'
        f'{brand_footer(pagenum) if pagenum else ""}'
        f'</div>'
    )


def heading(text, sub=None, accent=CALM['lavenderDark']):
    h = (f'<div style="height:6px;width:60px;border-radius:4px;background:{accent};margin-bottom:16px;"></div>'
         f'<div style="font-family:Georgia,\'Liberation Serif\',serif;font-size:30px;font-weight:bold;color:{CALM["text"]};">{text}</div>')
    if sub:
        h += f'<div style="font-size:14px;color:{CALM["sub"]};margin-top:7px;margin-bottom:22px;font-style:italic;">{sub}</div>'
    else:
        h += '<div style="margin-bottom:22px;"></div>'
    return h


def table(headers, widths, n_rows=10, rows=None, header_bg=CALM['lavender']):
    col_html = "".join(f'<col style="width:{w}">' for w in widths)
    head_html = "".join(f'<th style="padding:10px 12px;text-align:left;">{h}</th>' for h in headers)
    body_rows = rows if rows else [[""] * len(headers) for _ in range(n_rows)]
    body_html = ""
    for r in body_rows:
        cells = "".join(f'<td style="padding:15px 12px;border-bottom:1px solid #ECE7EE;">{c}</td>' for c in r)
        body_html += f'<tr>{cells}</tr>'
    return (f'<table style="width:100%;border-collapse:collapse;font-size:13px;color:{CALM["text"]};">'
            f'<colgroup>{col_html}</colgroup>'
            f'<thead><tr style="background:{header_bg};">{head_html}</tr></thead>'
            f'<tbody>{body_html}</tbody></table>')


def fill_line(label, width="100%"):
    return (f'<div style="width:{width};margin-bottom:18px;">'
            f'<div style="font-size:11.5px;color:{CALM["roseDark"]};font-weight:600;letter-spacing:.4px;margin-bottom:5px;">{label.upper()}</div>'
            f'<div style="border-bottom:1.5px solid #E3DCE6;height:24px;"></div></div>')


def lined_area(n=10, h=32):
    lines = "".join(f'<div style="border-bottom:1.3px solid #E3DCE6;height:{h}px;"></div>' for _ in range(n))
    return f'<div>{lines}</div>'


def soft_checklist(items, note_lines=False):
    note_html = '<div style="border-bottom:1.3px solid #ECE7EE;height:20px;margin-top:6px;width:220px;"></div>'
    rows = ""
    for it in items:
        extra = note_html if note_lines else ""
        rows += (f'<div style="display:flex;gap:12px;align-items:flex-start;margin-bottom:16px;">'
                 f'<div style="width:16px;height:16px;border:1.5px solid {CALM["slateDark"]};border-radius:50%;flex:0 0 auto;margin-top:2px;"></div>'
                 f'<div style="flex:1;"><div style="font-size:14px;color:{CALM["text"]};">{it}</div>'
                 f'{extra}'
                 f'</div></div>')
    return rows


def callout(text, bg=CALM['slate']):
    return (f'<div style="background:{bg};border-radius:14px;padding:20px 24px;font-size:13.5px;'
            f'color:{CALM["text"]};line-height:1.6;">{text}</div>')


# ---------- 1. Cover ----------
page(f'''
<div style="position:absolute;top:80px;left:80px;width:160px;height:160px;border-radius:50%;background:{CALM["sage"]};opacity:.7;"></div>
<div style="position:absolute;bottom:100px;right:60px;width:200px;height:200px;border-radius:50%;background:{CALM["slate"]};opacity:.6;"></div>
<div style="position:relative;text-align:center;padding-top:200px;">
  <div style="font-size:16px;letter-spacing:5px;color:{CALM["roseDark"]};font-weight:600;">LITTLE MILESTONE CO.</div>
  <div style="font-family:Georgia,'Liberation Serif',serif;font-size:48px;font-weight:bold;color:{CALM["text"]};margin-top:24px;">A NICU Journal</div>
  <div style="font-size:17px;color:{CALM["sub"]};margin-top:16px;font-style:italic;">For the hardest, most love-filled days</div>
  <div style="margin-top:70px;font-size:16px;color:{CALM["text"]};">For</div>
  <div style="width:360px;margin:12px auto 0;border-bottom:1.5px solid #DCD3E6;height:30px;"></div>
  <div style="margin-top:36px;font-size:16px;color:{CALM["text"]};">Held by</div>
  <div style="width:360px;margin:12px auto 0;border-bottom:1.5px solid #DCD3E6;height:30px;"></div>
</div>
''', bg=CALM['bg'])

# ---------- 2. Welcome ----------
page(f'''
{heading("Before You Begin", None, accent=CALM['lavenderDark'])}
<div style="font-size:14.5px;color:{CALM['text']};line-height:1.75;">
This journal is just a tool — not one more thing you have to get right. Fill in what helps,
skip what doesn't, come back to a page a week later if that's what today allows. There's no
correct order and no finish line to rush toward.
<br><br>
It isn't a medical record. It won't replace what your baby's care team documents, and nothing
here should stand in for their guidance — it's simply a place to keep track of what matters to
<i>you</i>: the questions, the small moments, the people helping you, and how you're actually doing.
<br><br>
However long you're here, and however this chapter goes — we're glad you have this to hold onto.
</div>
<div style="margin-top:32px;">{callout("If you need someone to talk to, your NICU's social worker or chaplain is there for exactly this — you don't have to be in crisis to reach out to them.")}</div>
''')

# ---------- 3. Baby & NICU details ----------
page(f'''
{heading("A Few Details", "For your own reference", accent=CALM['sageDark'])}
<div style="display:flex;gap:40px;">
  <div style="flex:1;">
    {fill_line("Baby's name")}
    {fill_line("Date of birth")}
    {fill_line("Gestational age at birth")}
    {fill_line("Birth weight")}
  </div>
  <div style="flex:1;">
    {fill_line("Hospital / NICU")}
    {fill_line("Admission date")}
    {fill_line("Primary attending")}
    {fill_line("Our NICU nickname for this journey")}
  </div>
</div>
''')

# ---------- 4. Daily NICU Log ----------
headers = ['Date', 'Day of Life', 'Corrected Age', 'Weight', 'Feeds', "Today's Update", 'How I\'m Feeling']
page(f'''
{heading("Daily Log", "One row a day, or whenever you have a moment", accent=CALM['slateDark'])}
{table(headers, ["11%", "11%", "12%", "10%", "12%", "24%", "20%"], n_rows=15)}
''')
page(f'''
{heading("Daily Log", "Continued — duplicate this page for a longer stay", accent=CALM['slateDark'])}
{table(headers, ["11%", "11%", "12%", "10%", "12%", "24%", "20%"], n_rows=15)}
''')

# ---------- 5. Questions for the care team ----------
page(f'''
{heading("Questions for the Care Team", "Jot them down the moment you think of them — rounds move fast", accent=CALM['roseDark'])}
{table(["Date", "Question", "Answer"], ["16%", "42%", "42%"], n_rows=16)}
''')

# ---------- 6. Care team & contacts ----------
page(f'''
{heading("Care Team &amp; Contacts", "So many names — a place to keep them straight", accent=CALM['lavenderDark'])}
{table(["Name", "Role", "Notes"], ["28%", "28%", "44%"], n_rows=15)}
''')

# ---------- 7. Feeding & pumping log ----------
page(f'''
{heading("Feeding &amp; Pumping Log", "Daily totals — as exact or as approximate as you need", accent=CALM['sageDark'])}
{table(["Date", "Sessions", "Total Output", "Feeding Method", "Notes"], ["16%", "14%", "16%", "22%", "32%"], n_rows=15)}
''')

# ---------- 8. NICU Milestones ----------
milestones = [
    "First time being held", "First skin-to-skin (kangaroo care)", "Off CPAP / ventilator",
    "First bottle or breastfeeding", "Moved to a new room or pod", "First bath",
    "First outfit", "A weight milestone that mattered to us", "Discharge planning begins",
]
ms_html = ""
for m in milestones:
    ms_html += (f'<div style="display:flex;justify-content:space-between;align-items:center;'
                f'padding:13px 0;border-bottom:1px solid #ECE7EE;">'
                f'<div style="font-size:14px;color:{CALM["text"]};">{m}</div>'
                f'<div style="width:160px;border-bottom:1.3px solid #DCD3E6;height:22px;"></div></div>')
page(f'''
{heading("Milestones", "In your own time, in your own order — check off only what applies to you", accent=CALM['slateDark'])}
{ms_html}
''')

# ---------- 9-10. A Space for Feelings ----------
prompts = [
    "Today I want to remember...",
    "Something I'm carrying today...",
]
for p_text in prompts:
    page(f'''
    {heading("A Space for Feelings", None, accent=CALM['roseDark'])}
    <div style="font-size:15px;font-style:italic;color:{CALM['sub']};margin-bottom:20px;">{p_text}</div>
    {lined_area(13)}
    ''')

# ---------- 11. Support & self-care ----------
reminders = [
    "Eat something today, even if it's small.",
    "It's okay to leave the room. It's okay to stay.",
    "Ask someone to bring you a change of clothes.",
    "You're allowed to have a hard day — or a hard hour, inside a good day.",
    "Let someone else answer texts for you today, if you want to.",
    "Rest counts, even in small pieces.",
]
page(f'''
{heading("Support &amp; Self-Care", "Gentle reminders, not a to-do list", accent=CALM['sageDark'])}
{soft_checklist(reminders)}
<div style="margin-top:10px;font-size:12px;color:{CALM['roseDark']};font-weight:600;letter-spacing:.4px;">PEOPLE HELPING US RIGHT NOW</div>
{lined_area(4)}
''')

# ---------- 12. Siblings at home ----------
page(f'''
{heading("Siblings at Home", "If this applies to your family", accent=CALM['lavenderDark'])}
<div style="display:flex;gap:40px;">
  <div style="flex:1;">{fill_line("Who's caring for them")}{fill_line("How they're doing")}</div>
  <div style="flex:1;">{fill_line("What they understand so far")}{fill_line("Something that's helped them")}</div>
</div>
<div style="margin-top:6px;font-size:12px;color:{CALM['roseDark']};font-weight:600;letter-spacing:.4px;">NOTES</div>
{lined_area(6)}
''')

# ---------- 13. Logistics ----------
page(f'''
{heading("Logistics", "The unglamorous but necessary things", accent=CALM['slateDark'])}
<div style="display:flex;gap:34px;">
  <div style="flex:1;">
    <div style="font-size:12px;color:{CALM['roseDark']};font-weight:600;margin-bottom:8px;letter-spacing:.4px;">PARKING &amp; HOSPITAL LOGISTICS</div>
    {lined_area(4)}
    <div style="font-size:12px;color:{CALM['roseDark']};font-weight:600;margin:18px 0 8px;letter-spacing:.4px;">SOCIAL WORKER / FINANCIAL COUNSELOR</div>
    {lined_area(3)}
  </div>
  <div style="flex:1;">
    <div style="font-size:12px;color:{CALM['roseDark']};font-weight:600;margin-bottom:8px;letter-spacing:.4px;">INSURANCE &amp; BILLING NOTES</div>
    {lined_area(4)}
    <div style="font-size:12px;color:{CALM['roseDark']};font-weight:600;margin:18px 0 8px;letter-spacing:.4px;">HOSPITAL RESOURCES WORTH KNOWING ABOUT</div>
    {lined_area(3)}
  </div>
</div>
''')

# ---------- 14. Discharge prep ----------
discharge_items = [
    "Car seat test completed", "Newborn screening completed", "Pediatrician chosen",
    "First follow-up appointment scheduled", "Home equipment arranged, if needed",
    "Feeding plan for home confirmed", "Going-home outfit ready",
]
page(f'''
{heading("Discharge Prep", "Whenever that day comes", accent=CALM['sageDark'])}
{soft_checklist(discharge_items)}
''')

# ---------- 15. Closing ----------
page(f'''
<div style="text-align:center;padding-top:160px;">
  <div style="width:14px;height:14px;border-radius:50%;background:{CALM['sageDark']};margin:0 auto;"></div>
  <div style="font-family:Georgia,'Liberation Serif',serif;font-size:26px;color:{CALM['text']};margin-top:26px;line-height:1.5;">
    However this chapter reads,<br>you showed up for it.
  </div>
  <div style="font-size:14px;color:{CALM['sub']};margin-top:18px;font-style:italic;">That counts for everything.</div>
  <div style="font-size:12px;color:{CALM['roseDark']};font-weight:600;letter-spacing:2px;margin-top:70px;">LITTLE MILESTONE CO.</div>
</div>
''', bg=CALM['bg'])


HTML = f'''<!doctype html>
<html><head><meta charset="utf-8"><style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ font-family: 'Liberation Sans', Helvetica, Arial, sans-serif; }}
  .page {{ width:816px; height:1056px; position:relative; overflow:hidden; page-break-after:always; }}
  .page:last-child {{ page-break-after:avoid; }}
  table th, table td {{ vertical-align:top; }}
</style></head>
<body>
{"".join(PAGES)}
</body></html>
'''

html_path = os.path.join(DIR, "nicu_journal.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"wrote {html_path} ({len(PAGES)} pages)")

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    pg = browser.new_page(viewport={"width": 816, "height": 1056})
    pg.goto(f"file://{html_path}")
    pg.pdf(path=os.path.join(DIR, "A-NICU-Journal.pdf"), width="816px", height="1056px", print_background=True)
    browser.close()
print("wrote A-NICU-Journal.pdf")
