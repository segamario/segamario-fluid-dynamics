import os
import sys
from playwright.sync_api import sync_playwright

DIR = os.path.dirname(os.path.abspath(__file__))
link = sys.argv[1] if len(sys.argv) > 1 else "PASTE YOUR GOOGLE SHEET SHARE LINK HERE"

html = open(os.path.join(DIR, "delivery.html"), encoding="utf-8").read()
html = html.replace("{{SHEET_LINK}}", link)
tmp_path = os.path.join(DIR, "_delivery_rendered.html")
with open(tmp_path, "w", encoding="utf-8") as f:
    f.write(html)

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    page = browser.new_page(viewport={"width": 816, "height": 1056})
    page.goto(f"file://{tmp_path}")
    page.pdf(path=os.path.join(DIR, "How-To-Get-Your-Tracker.pdf"), width="816px", height="1056px", print_background=True)
    browser.close()

os.remove(tmp_path)
print("wrote How-To-Get-Your-Tracker.pdf with link:", link)
