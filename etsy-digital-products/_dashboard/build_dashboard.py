import base64
import io
import os
from PIL import Image

DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(DIR)


def thumb_data_uri(path, size, quality=78):
    im = Image.open(path).convert("RGB")
    im = im.resize((size, size), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=quality)
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    return f"data:image/jpeg;base64,{b64}"


icon_uri = thumb_data_uri(os.path.join(ROOT, "shop-branding/icon.jpg"), 128, quality=85)
planner_uri = thumb_data_uri(os.path.join(ROOT, "pregnancy-to-toddler-planner/listing-images/hero.png"), 640)
book_uri = thumb_data_uri(os.path.join(ROOT, "baby-first-year-memory-book/listing-images/hero.png"), 640)
kit_uri = thumb_data_uri(os.path.join(ROOT, "baby-shower-planning-kit/listing-images/hero.png"), 640)

with open(os.path.join(DIR, "dashboard_template.html"), encoding="utf-8") as f:
    html = f.read()

html = (html
        .replace("{{ICON_IMG}}", icon_uri)
        .replace("{{PLANNER_IMG}}", planner_uri)
        .replace("{{BOOK_IMG}}", book_uri)
        .replace("{{KIT_IMG}}", kit_uri))

out_path = os.path.join(DIR, "dashboard.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

print("wrote", out_path, "-", os.path.getsize(out_path) / 1024, "KB")
