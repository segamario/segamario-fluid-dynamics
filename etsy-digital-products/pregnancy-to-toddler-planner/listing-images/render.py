import os
from playwright.sync_api import sync_playwright

DIR = os.path.dirname(os.path.abspath(__file__))
PAGES = ["hero", "whats-inside", "features"]

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    page = browser.new_page(viewport={"width": 2000, "height": 2000}, device_scale_factor=1)
    for name in PAGES:
        html_path = os.path.join(DIR, f"{name}.html")
        png_path = os.path.join(DIR, f"{name}.png")
        page.goto(f"file://{html_path}")
        page.screenshot(path=png_path, clip={"x": 0, "y": 0, "width": 2000, "height": 2000})
        print(f"wrote {png_path}")
    browser.close()
