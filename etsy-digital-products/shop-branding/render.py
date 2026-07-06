import os
from playwright.sync_api import sync_playwright
from PIL import Image

DIR = os.path.dirname(os.path.abspath(__file__))
TARGETS = [("icon", 500, 500), ("banner", 3360, 840)]

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    for name, w, h in TARGETS:
        page = browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
        page.goto(f"file://{os.path.join(DIR, name)}.html")
        png_path = os.path.join(DIR, f"{name}.png")
        page.screenshot(path=png_path, clip={"x": 0, "y": 0, "width": w, "height": h})
        page.close()

        jpg_path = os.path.join(DIR, f"{name}.jpg")
        im = Image.open(png_path).convert("RGB")
        quality = 92
        im.save(jpg_path, "JPEG", quality=quality)
        while os.path.getsize(jpg_path) > 1_000_000 and quality > 40:
            quality -= 8
            im.save(jpg_path, "JPEG", quality=quality)
        print(name, "png+jpg written, jpg size:", os.path.getsize(jpg_path), "quality:", quality)
    browser.close()
