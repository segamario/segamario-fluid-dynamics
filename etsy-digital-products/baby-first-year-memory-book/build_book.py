"""
Baby's First Year Memory Book — printable keepsake album.
Generates one long HTML file (one .page div per printed page, 816x1056 = Letter @96dpi)
then renders it to a paginated PDF with Playwright. Matches the Little Milestone Co.
pastel design system used across the shop.
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
MONTH_THEME = [PASTEL['pink'], PASTEL['blue'], PASTEL['mint'], PASTEL['lavender'],
               PASTEL['peach'], PASTEL['yellow']] * 2  # 12 months, cycling 6 colors

PAGES = []


def photo_box(width="100%", height="360px", label="add a photo here", icon="📷"):
    return (f'<div style="width:{width};height:{height};border:3px dashed #D9B8CE;border-radius:18px;'
            f'display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;'
            f'background:rgba(255,255,255,.5);">'
            f'<div style="font-size:38px;">{icon}</div>'
            f'<div style="font-size:15px;color:#9a8a95;">{label}</div></div>')


def fill_line(label, width="100%"):
    return (f'<div style="width:{width};margin-bottom:22px;">'
            f'<div style="font-size:13px;color:#B8779A;font-weight:bold;letter-spacing:.5px;margin-bottom:6px;">{label.upper()}</div>'
            f'<div style="border-bottom:2px solid #E9DCE3;height:26px;"></div></div>')


def lined_area(n=10):
    lines = "".join('<div style="border-bottom:1.5px solid #E9DCE3;height:34px;"></div>' for _ in range(n))
    return f'<div>{lines}</div>'


def brand_footer(pagenum):
    return (f'<div style="position:absolute;bottom:26px;left:60px;right:60px;display:flex;'
            f'justify-content:space-between;align-items:center;">'
            f'<div style="font-size:12px;color:#B8779A;font-weight:bold;letter-spacing:2px;">LITTLE MILESTONE CO.</div>'
            f'<div style="font-size:12px;color:#b9b9b9;">{pagenum}</div></div>')


def page(inner, bg="#FFFDFB", pagenum=""):
    PAGES.append(
        f'<div class="page" style="background:{bg};">'
        f'<div style="position:absolute;top:0;left:0;right:0;bottom:0;padding:64px 60px 70px 60px;">{inner}</div>'
        f'{brand_footer(pagenum) if pagenum else ""}'
        f'</div>'
    )


def heading(text, sub=None, color=PASTEL['text']):
    h = f'<div style="font-family:Georgia,\'Liberation Serif\',serif;font-size:34px;font-weight:bold;color:{color};">{text}</div>'
    if sub:
        h += f'<div style="font-size:15px;color:{PASTEL["sub"]};margin-top:6px;margin-bottom:28px;">{sub}</div>'
    else:
        h += '<div style="margin-bottom:28px;"></div>'
    return h


# ---------- 1. Cover ----------
page(f'''
<div style="position:absolute;top:60px;left:60px;width:180px;height:180px;border-radius:50%;background:{PASTEL["yellow"]};opacity:.6;"></div>
<div style="position:absolute;bottom:80px;right:40px;width:220px;height:220px;border-radius:50%;background:{PASTEL["mint"]};opacity:.6;"></div>
<div style="position:relative;text-align:center;padding-top:60px;">
  <div style="font-size:20px;letter-spacing:5px;color:#B8779A;font-weight:bold;">LITTLE MILESTONE CO.</div>
  <div style="font-family:Georgia,'Liberation Serif',serif;font-size:52px;font-weight:bold;color:#4A4A4A;margin-top:26px;">My First Year</div>
  <div style="font-size:20px;color:#6a6a6a;margin-top:10px;">A Baby Memory &amp; Growth Book</div>
  <div style="margin:44px auto 0;width:520px;">{photo_box(height="420px")}</div>
  <div style="margin-top:40px;font-size:22px;color:#4A4A4A;">This book belongs to</div>
  <div style="width:400px;margin:14px auto 0;border-bottom:2px solid #D9B8CE;height:34px;"></div>
</div>
''', bg="#FFF8F5")

# ---------- 2. How to use ----------
page(f'''
{heading("How to Use This Book", "A few tips before you dive in")}
<div style="display:flex;flex-direction:column;gap:22px;font-size:16px;line-height:1.6;color:#5a5a5a;">
  <div>🖨️ <b>Print on cardstock</b> if you can — it holds up much better to little hands and glue than regular paper.</div>
  <div>📎 <b>Binding:</b> punch holes and use a ring binder, or take the PDF to a print shop for spiral binding — either works beautifully.</div>
  <div>📷 <b>Photos:</b> each dashed box is sized for a standard 4×4in or 4×6in print — tape or glue your favorite shot right in.</div>
  <div>✏️ <b>Fill it in slowly.</b> This isn't a race — some parents finish a page a week, some catch up all at once at the first birthday. Both are perfectly fine.</div>
  <div>💛 <b>There's no wrong way to keep this book.</b> Skip pages, add your own, spill a little coffee on it — it's meant to be lived-in, not perfect.</div>
</div>
''')

# ---------- 3. Baby details ----------
page(f'''
{heading("Baby Details", "The basics, for the record")}
<div style="display:flex;gap:40px;">
  <div style="flex:1;">
    {fill_line("Full name")}
    {fill_line("Nickname")}
    {fill_line("Date of birth")}
    {fill_line("Time of birth")}
    {fill_line("Weight")}
    {fill_line("Length")}
    {fill_line("Hospital / place of birth")}
    {fill_line("Delivering doctor / midwife")}
  </div>
  <div style="flex:0 0 280px;">{photo_box(height="500px")}</div>
</div>
''')

# ---------- 4. Family tree ----------
def box(label, h="110px"):
    return (f'<div style="flex:1;height:{h};border-radius:16px;background:#fff;border:2px solid #E9DCE3;'
            f'display:flex;align-items:center;justify-content:center;text-align:center;padding:10px;">'
            f'<span style="font-size:14px;color:#8a8a8a;">{label}</span></div>')

page(f'''
{heading("Family Tree", "Who's welcoming you")}
<div style="display:flex;flex-direction:column;align-items:stretch;gap:22px;margin-top:20px;">
  <div style="display:flex;gap:20px;">{box("Grandparent")}{box("Grandparent")}{box("Grandparent")}{box("Grandparent")}</div>
  <div style="text-align:center;font-size:22px;color:#B8779A;">↓</div>
  <div style="display:flex;gap:20px;padding:0 100px;">{box("Parent")}{box("Parent")}</div>
  <div style="text-align:center;font-size:22px;color:#B8779A;">↓</div>
  <div style="display:flex;justify-content:center;">
    <div style="width:220px;height:130px;border-radius:16px;background:{PASTEL['pink']};display:flex;align-items:center;justify-content:center;">
      <span style="font-size:16px;color:#4A4A4A;font-weight:bold;">Baby 👶</span>
    </div>
  </div>
</div>
''')

# ---------- 5. Birth story ----------
page(f'''
{heading("Your Birth Story", "The day you arrived")}
<div style="margin-bottom:26px;">{photo_box(height="220px")}</div>
{lined_area(9)}
''')

# ---------- 6. Coming home ----------
page(f'''
{heading("Coming Home", "The start of everything")}
<div style="display:flex;gap:40px;">
  <div style="flex:1;">
    {fill_line("Date we came home")}
    {fill_line("Who was there to greet you")}
    {fill_line("Your first outfit")}
    {fill_line("Your first visitors")}
    {fill_line("The first song we sang you")}
  </div>
  <div style="flex:0 0 280px;">{photo_box(height="420px")}</div>
</div>
''')

# ---------- 7. Firsts ----------
firsts = ["First smile", "First laugh", "First word", "First tooth", "First solid food",
          "First haircut", "First steps", "First holiday", "First trip", "First time in snow/rain",
          "First time at the beach/pool", "First sleepover away from home"]
firsts_html = "".join(fill_line(f) for f in firsts)
page(f'''
{heading("Your Firsts", "Big and small")}
<div style="columns:2;column-gap:40px;">{firsts_html}</div>
''')

# ---------- 8-19. Monthly pages ----------
month_prompts = [
    ("Month 1", "Newborn days"),
    ("Month 2", "Finding a rhythm"),
    ("Month 3", "Hello, smiles"),
    ("Month 4", "Getting curious"),
    ("Month 5", "Almost sitting up"),
    ("Month 6", "Halfway to one!"),
    ("Month 7", "On the move"),
    ("Month 8", "Chatting away"),
    ("Month 9", "Exploring everything"),
    ("Month 10", "Standing tall"),
    ("Month 11", "Almost a toddler"),
    ("Month 12", "Happy 1st birthday!"),
]
for i, (title, sub) in enumerate(month_prompts):
    theme = MONTH_THEME[i]
    page(f'''
    <div style="height:8px;border-radius:4px;background:{theme};margin-bottom:20px;"></div>
    <div style="display:flex;justify-content:space-between;align-items:baseline;">
      <div style="font-family:Georgia,\'Liberation Serif\',serif;font-size:34px;font-weight:bold;color:#4A4A4A;">{title}</div>
      <div style="font-size:16px;color:#8a8a8a;font-style:italic;">{sub}</div>
    </div>
    <div style="margin:22px 0 26px;height:230px;border:3px dashed {theme};border-radius:18px;
      display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;background:rgba(255,255,255,.5);">
      <div style="font-size:38px;">📷</div><div style="font-size:15px;color:#9a8a95;">add a photo here</div>
    </div>
    <div style="display:flex;gap:30px;margin-bottom:22px;">
      <div style="flex:1;">{fill_line("Weight")}</div>
      <div style="flex:1;">{fill_line("Length / height")}</div>
      <div style="flex:1;">{fill_line("Favorite thing this month")}</div>
    </div>
    <div style="font-size:13px;color:#B8779A;font-weight:bold;letter-spacing:.5px;margin-bottom:8px;">THIS MONTH YOU...</div>
    {lined_area(4)}
    ''', bg="#FFFDFB")

# ---------- 20. Hand/footprints ----------
page(f'''
{heading("Handprints &amp; Footprints", "A little bit of you, forever")}
<div style="display:flex;gap:40px;">
  <div style="flex:1;text-align:center;">
    <div style="font-size:15px;color:#8a8a8a;margin-bottom:12px;">HANDPRINT</div>
    {photo_box(height="380px", label="press here", icon="🖐️")}
  </div>
  <div style="flex:1;text-align:center;">
    <div style="font-size:15px;color:#8a8a8a;margin-bottom:12px;">FOOTPRINT</div>
    {photo_box(height="380px", label="press here", icon="🦶")}
  </div>
</div>
''')

# ---------- 21. First birthday ----------
page(f'''
{heading("Your First Birthday", "One whole year of you")}
<div style="display:flex;gap:40px;">
  <div style="flex:1;">
    {fill_line("Party theme")}
    {fill_line("Where we celebrated")}
    {fill_line("Who came")}
    {fill_line("Your favorite gift")}
    {fill_line("How you reacted to cake")}
  </div>
  <div style="flex:0 0 280px;">{photo_box(height="420px", label="cake smash photo")}</div>
</div>
''')

# ---------- 22 & 23. Letters ----------
for n in ("One", "Two"):
    page(f'''
    {heading(f"A Letter to You", f"Written by ______, on your first birthday")}
    {lined_area(13)}
    ''')

# ---------- 24. Closing ----------
page(f'''
<div style="text-align:center;padding-top:120px;">
  <div style="font-size:44px;">💛</div>
  <div style="font-family:Georgia,'Liberation Serif',serif;font-size:32px;font-weight:bold;color:#4A4A4A;margin-top:20px;">
    Here's to every year after this one.
  </div>
  <div style="font-size:16px;color:#8a8a8a;margin-top:14px;">Thank you for keeping this book.</div>
  <div style="font-size:14px;color:#B8779A;font-weight:bold;letter-spacing:2px;margin-top:60px;">LITTLE MILESTONE CO.</div>
</div>
''', bg="#FFF8F5")


HTML = f'''<!doctype html>
<html><head><meta charset="utf-8"><style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ font-family: 'Liberation Sans', Helvetica, Arial, sans-serif; }}
  .page {{ width:816px; height:1056px; position:relative; overflow:hidden; page-break-after:always; }}
  .page:last-child {{ page-break-after:avoid; }}
</style></head>
<body>
{"".join(PAGES)}
</body></html>
'''

html_path = os.path.join(DIR, "memory_book.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"wrote {html_path} ({len(PAGES)} pages)")

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    pg = browser.new_page(viewport={"width": 816, "height": 1056})
    pg.goto(f"file://{html_path}")
    pg.pdf(path=os.path.join(DIR, "Babys-First-Year-Memory-Book.pdf"), width="816px", height="1056px", print_background=True)
    browser.close()
print("wrote Babys-First-Year-Memory-Book.pdf")
