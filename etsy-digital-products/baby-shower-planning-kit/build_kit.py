"""
Baby Shower Planning Kit — printable PDF (budget, guest list, gift/thank-you tracker,
vendor checklist, menu, decor, shopping list, games planner, day-of timeline, registry
essentials, contacts, notes). Same Little Milestone Co. pastel design system as the other
two products in this shop.
"""
import os
from playwright.sync_api import sync_playwright

DIR = os.path.dirname(os.path.abspath(__file__))

PASTEL = {
    'pink': '#FBD8E5', 'pinkDark': '#F4AFC9',
    'blue': '#D6E8F7', 'blueDark': '#AFD3EF',
    'mint': '#D9F2E6', 'mintDark': '#AEE4C9',
    'lavender': '#E6DFF7', 'lavenderDark': '#C9B8ED',
    'yellow': '#FFF3CE', 'yellowDark': '#FBE192',
    'peach': '#FDE3D3', 'peachDark': '#F8C39E',
    'text': '#4A4A4A', 'sub': '#8a8a8a',
}

PAGES = []


def brand_footer(pagenum):
    return (f'<div style="position:absolute;bottom:26px;left:60px;right:60px;display:flex;'
            f'justify-content:space-between;align-items:center;">'
            f'<div style="font-size:12px;color:#B8779A;font-weight:bold;letter-spacing:2px;">LITTLE MILESTONE CO.</div>'
            f'<div style="font-size:12px;color:#b9b9b9;">{pagenum}</div></div>')


def page(inner, bg="#FFFDFB", pagenum=""):
    PAGES.append(
        f'<div class="page" style="background:{bg};">'
        f'<div style="position:absolute;top:0;left:0;right:0;bottom:0;padding:56px 56px 66px 56px;">{inner}</div>'
        f'{brand_footer(pagenum) if pagenum else ""}'
        f'</div>'
    )


def heading(text, sub=None, accent=PASTEL['pinkDark']):
    h = (f'<div style="height:7px;width:70px;border-radius:4px;background:{accent};margin-bottom:16px;"></div>'
         f'<div style="font-family:Georgia,\'Liberation Serif\',serif;font-size:32px;font-weight:bold;color:#4A4A4A;">{text}</div>')
    if sub:
        h += f'<div style="font-size:14px;color:{PASTEL["sub"]};margin-top:6px;margin-bottom:22px;">{sub}</div>'
    else:
        h += '<div style="margin-bottom:22px;"></div>'
    return h


def table(headers, widths, n_rows=10, rows=None, header_bg=PASTEL['pink']):
    col_html = "".join(f'<col style="width:{w}">' for w in widths)
    head_html = "".join(f'<th style="padding:10px 12px;text-align:left;">{h}</th>' for h in headers)
    body_rows = rows if rows else [[""] * len(headers) for _ in range(n_rows)]
    body_html = ""
    for r in body_rows:
        cells = "".join(f'<td style="padding:17px 12px;border-bottom:1px solid #EFE6EA;">{c}</td>' for c in r)
        body_html += f'<tr>{cells}</tr>'
    return (f'<table style="width:100%;border-collapse:collapse;font-size:13.5px;color:#4A4A4A;">'
            f'<colgroup>{col_html}</colgroup>'
            f'<thead><tr style="background:{header_bg};">{head_html}</tr></thead>'
            f'<tbody>{body_html}</tbody></table>')


def fill_line(label, width="100%"):
    return (f'<div style="width:{width};margin-bottom:18px;">'
            f'<div style="font-size:12px;color:#B8779A;font-weight:bold;letter-spacing:.5px;margin-bottom:5px;">{label.upper()}</div>'
            f'<div style="border-bottom:2px solid #E9DCE3;height:24px;"></div></div>')


def lined_area(n=10, h=30):
    lines = "".join(f'<div style="border-bottom:1.5px solid #E9DCE3;height:{h}px;"></div>' for _ in range(n))
    return f'<div>{lines}</div>'


def checklist(items, cols=1):
    cell = lambda t: (f'<div style="display:flex;gap:10px;align-items:center;margin-bottom:12px;">'
                       f'<div style="width:18px;height:18px;border:2px solid #D9B8CE;border-radius:5px;flex:0 0 auto;"></div>'
                       f'<div style="font-size:14px;color:#4A4A4A;">{t}</div></div>')
    if cols == 1:
        return "".join(cell(i) for i in items)
    half = (len(items) + 1) // 2
    left = "".join(cell(i) for i in items[:half])
    right = "".join(cell(i) for i in items[half:])
    return f'<div style="display:flex;gap:40px;"><div style="flex:1;">{left}</div><div style="flex:1;">{right}</div></div>'


# ---------- 1. Cover ----------
page(f'''
<div style="position:absolute;top:70px;left:70px;width:180px;height:180px;border-radius:50%;background:{PASTEL["yellow"]};opacity:.6;"></div>
<div style="position:absolute;bottom:90px;right:50px;width:220px;height:220px;border-radius:50%;background:{PASTEL["blue"]};opacity:.55;"></div>
<div style="position:relative;text-align:center;padding-top:160px;">
  <div style="font-size:20px;letter-spacing:5px;color:#B8779A;font-weight:bold;">LITTLE MILESTONE CO.</div>
  <div style="font-family:Georgia,'Liberation Serif',serif;font-size:56px;font-weight:bold;color:#4A4A4A;margin-top:26px;">Baby Shower<br>Planning Kit</div>
  <div style="font-size:20px;color:#6a6a6a;margin-top:18px;">Everything you need to host a beautiful, stress-free shower</div>
  <div style="margin-top:60px;font-size:18px;color:#4A4A4A;">Planned for</div>
  <div style="width:420px;margin:14px auto 0;border-bottom:2px solid #D9B8CE;height:34px;"></div>
  <div style="margin-top:40px;font-size:18px;color:#4A4A4A;">Shower date</div>
  <div style="width:420px;margin:14px auto 0;border-bottom:2px solid #D9B8CE;height:34px;"></div>
</div>
''', bg="#FFF8F5")

# ---------- 2. Planning timeline ----------
timeline = [
    ("8 weeks before", ["Pick a date &amp; guest of honor's preferences", "Choose venue", "Set the budget (next page)", "Draft the guest list"]),
    ("6 weeks before", ["Send invitations", "Book caterer / plan menu", "Choose a theme &amp; color palette", "Order decorations"]),
    ("3 weeks before", ["Plan games &amp; activities", "Order or bake the cake/desserts", "Buy party favors", "Confirm RSVPs so far"]),
    ("1 week before", ["Confirm final headcount with venue/caterer", "Buy remaining supplies (shopping list page)", "Prep playlist", "Assign helpers for setup/cleanup"]),
    ("Day before", ["Prep food that can be made ahead", "Set up decorations if venue allows", "Charge camera/phone, pack the day-of bag"]),
    ("Day of", ["Follow the Day-Of Timeline page", "Enjoy it — you planned well!"]),
]
tl_html = ""
for label, items in timeline:
    tl_html += (f'<div style="display:flex;gap:24px;margin-bottom:20px;">'
                f'<div style="flex:0 0 150px;font-weight:bold;color:#B8779A;font-size:14px;padding-top:2px;">{label}</div>'
                f'<div style="flex:1;">{checklist(items)}</div></div>')
page(f'''
{heading("Planning Timeline", "A stress-free countdown to the big day")}
{tl_html}
''')

# ---------- 3. Budget tracker ----------
budget_rows = [[c, "", "", ""] for c in
               ["Venue", "Invitations", "Decorations", "Food &amp; drinks", "Cake / desserts",
                "Games &amp; prizes", "Favors", "Photography", "Miscellaneous"]]
budget_rows.append(["<b>Total</b>", "", "", ""])
page(f'''
{heading("Budget Tracker", "Keep the spending as lovely as the party")}
{table(["Category", "Budgeted", "Actual", "Notes"], ["28%", "18%", "18%", "36%"], rows=budget_rows)}
''')

# ---------- 4. Guest list ----------
page(f'''
{heading("Guest List", "Who's celebrating with you")}
{table(["Name", "Invited", "RSVP", "Plus One", "Dietary Notes"], ["34%", "13%", "13%", "13%", "27%"], n_rows=22)}
''')

# ---------- 5. Gift & thank-you tracker ----------
page(f'''
{heading("Gift &amp; Thank-You Tracker", "So no one gets missed")}
{table(["Guest", "Gift Given", "Thank-You Sent"], ["38%", "42%", "20%"], n_rows=22)}
''')

# ---------- 6. Venue & vendor checklist ----------
vendor_rows = [[c, "", "", "", ""] for c in
               ["Venue", "Caterer", "Baker", "Photographer", "Florist / Decorator", "Rental company", "Other"]]
page(f'''
{heading("Venue &amp; Vendor Checklist", "Contacts, all in one place")}
{table(["Category", "Vendor / Contact", "Phone", "Booked", "Notes"], ["20%", "26%", "16%", "12%", "26%"], rows=vendor_rows)}
''')

# ---------- 7. Menu planner ----------
page(f'''
{heading("Menu Planner", "What everyone will be talking about")}
<div style="display:flex;gap:34px;">
  <div style="flex:1;">
    <div style="font-size:13px;color:#B8779A;font-weight:bold;margin-bottom:8px;">APPETIZERS</div>{lined_area(4)}
    <div style="font-size:13px;color:#B8779A;font-weight:bold;margin:20px 0 8px;">MAIN / SAVORY</div>{lined_area(4)}
  </div>
  <div style="flex:1;">
    <div style="font-size:13px;color:#B8779A;font-weight:bold;margin-bottom:8px;">DESSERTS / CAKE</div>{lined_area(4)}
    <div style="font-size:13px;color:#B8779A;font-weight:bold;margin:20px 0 8px;">DRINKS</div>{lined_area(4)}
  </div>
</div>
<div style="font-size:13px;color:#B8779A;font-weight:bold;margin:20px 0 8px;">DIETARY RESTRICTIONS TO PLAN AROUND</div>
{lined_area(3)}
''')

# ---------- 8. Theme & decor ----------
page(f'''
{heading("Theme &amp; Decor", "Set the mood")}
<div style="display:flex;gap:40px;margin-bottom:30px;">
  <div style="flex:1;">{fill_line("Theme")}{fill_line("Color palette")}</div>
  <div style="flex:0 0 260px;">
    <div style="font-size:12px;color:#B8779A;font-weight:bold;margin-bottom:8px;">COLOR SWATCHES</div>
    <div style="display:flex;gap:10px;">
      <div style="width:44px;height:44px;border-radius:10px;background:{PASTEL['pink']};"></div>
      <div style="width:44px;height:44px;border-radius:10px;background:{PASTEL['blue']};"></div>
      <div style="width:44px;height:44px;border-radius:10px;background:{PASTEL['mint']};"></div>
      <div style="width:44px;height:44px;border-radius:10px;background:{PASTEL['lavender']};"></div>
      <div style="width:44px;height:44px;border-radius:10px;background:{PASTEL['yellow']};"></div>
    </div>
  </div>
</div>
{checklist(["Balloons / balloon arch", "Banner / backdrop", "Table centerpieces", "Table linens", "Welcome sign",
            "Dessert table styling", "Favor table display", "String lights / candles", "Photo booth props",
            "Guest book / wishes for baby cards"], cols=2)}
''')

# ---------- 9. Shopping list ----------
page(f'''
{heading("Shopping &amp; Supplies List", "One trip, everything covered")}
<div style="display:flex;gap:34px;">
  <div style="flex:1;">
    <div style="font-size:13px;color:#B8779A;font-weight:bold;margin-bottom:10px;">DECOR</div>{lined_area(5)}
    <div style="font-size:13px;color:#B8779A;font-weight:bold;margin:18px 0 10px;">FOOD &amp; DRINKS</div>{lined_area(5)}
  </div>
  <div style="flex:1;">
    <div style="font-size:13px;color:#B8779A;font-weight:bold;margin-bottom:10px;">GAMES &amp; FAVORS</div>{lined_area(5)}
    <div style="font-size:13px;color:#B8779A;font-weight:bold;margin:18px 0 10px;">MISCELLANEOUS</div>{lined_area(5)}
  </div>
</div>
''')

# ---------- 10. Games & activities ----------
page(f'''
{heading("Games &amp; Activities", "A few favorites to get you started")}
{table(["Game", "Supplies Needed", "Prize", "Time Needed"], ["28%", "34%", "20%", "18%"],
       rows=[["Guess the baby food", "", "", ""], ["Baby word scramble", "", "", ""],
             ["Guess the belly size", "", "", ""], ["Diaper raffle", "", "", ""],
             ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
             ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
             ["", "", "", ""], ["", "", "", ""]])}
''')

# ---------- 11. Day-of timeline ----------
page(f'''
{heading("Day-Of Timeline", "So you can actually enjoy it")}
{table(["Time", "What's Happening"], ["22%", "78%"],
       rows=[["", "Setup begins"], ["", "Guests arrive"], ["", "Welcome &amp; mingling"],
             ["", "Games / activities"], ["", "Food &amp; cake"], ["", "Gift opening"],
             ["", "Favors &amp; goodbyes"], ["", "Cleanup"]])}
''')

# ---------- 12. Registry essentials ----------
page(f'''
{heading("Registry Essentials", "A gentle reference list for guests")}
<div style="display:flex;gap:34px;">
  <div style="flex:1;">
    <div style="font-size:13px;color:#B8779A;font-weight:bold;margin-bottom:10px;">NURSERY</div>
    {checklist(["Crib &amp; mattress", "Sheets", "Sound machine", "Changing pad"])}
    <div style="font-size:13px;color:#B8779A;font-weight:bold;margin:16px 0 10px;">FEEDING</div>
    {checklist(["Bottles", "Burp cloths", "High chair", "Nursing pillow"])}
  </div>
  <div style="flex:1;">
    <div style="font-size:13px;color:#B8779A;font-weight:bold;margin-bottom:10px;">DIAPERING &amp; BATH</div>
    {checklist(["Diapers (all sizes)", "Wipes", "Baby bathtub", "Towels &amp; washcloths"])}
    <div style="font-size:13px;color:#B8779A;font-weight:bold;margin:16px 0 10px;">TRAVEL &amp; CLOTHING</div>
    {checklist(["Car seat", "Stroller", "Onesies (multiple sizes)", "Swaddles / sleep sacks"])}
  </div>
</div>
''')

# ---------- 13. Contacts ----------
page(f'''
{heading("Key Contacts", "Everyone you might need to call")}
{table(["Name", "Role", "Phone"], ["34%", "33%", "33%"], n_rows=19)}
''')

# ---------- 14. Notes / closing ----------
page(f'''
{heading("Notes &amp; To-Dos", "Anything else on your mind")}
{lined_area(13)}
<div style="text-align:center;margin-top:50px;">
  <div style="font-size:34px;">🎈</div>
  <div style="font-family:Georgia,'Liberation Serif',serif;font-size:22px;color:#4A4A4A;margin-top:10px;">Here's to a beautiful day.</div>
</div>
''', bg="#FFF8F5")


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

html_path = os.path.join(DIR, "shower_kit.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"wrote {html_path} ({len(PAGES)} pages)")

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    pg = browser.new_page(viewport={"width": 816, "height": 1056})
    pg.goto(f"file://{html_path}")
    pg.pdf(path=os.path.join(DIR, "Baby-Shower-Planning-Kit.pdf"), width="816px", height="1056px", print_background=True)
    browser.close()
print("wrote Baby-Shower-Planning-Kit.pdf")
