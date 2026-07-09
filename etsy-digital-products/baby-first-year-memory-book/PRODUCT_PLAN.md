# My First Year — Baby Memory & Growth Book — Product Plan & Etsy Listing

## What this is
A 24-page printable PDF keepsake book covering baby's first year: cover, printing tips,
baby details, family tree, birth story, coming home, a "firsts" checklist, 12 monthly
check-in pages (photo box + weight/height + prompts), handprint/footprint page, first
birthday page, two blank letter pages, and a closing page. Same pastel design system as
the Bump to Toddler Planner, so it cross-sells naturally to the same buyers.

## Positioning
This is a **print-and-fill** product, not a spreadsheet — different buyer intent than the
planner (gift-giving, keepsake, gets done by hand). Pairs naturally as an upsell/bundle
with the Bump to Toddler Planner: "finish the planner during pregnancy, start the memory
book once baby arrives."

## Files
- `build_book.py` — generates `memory_book.html` (24 `.page` divs) and renders it to
  `Babys-First-Year-Memory-Book.pdf` via Playwright. Edit the `PAGES` list / helper calls
  to change content; palette is the same `PASTEL` dict used across the shop.
- `Babys-First-Year-Memory-Book.pdf` — the file to upload as the Etsy digital download.
- `listing-images/hero.png`, `listing-images/pages-preview.png` — 2000x2000 listing photos.

## Etsy listing copy

**Title:**
`My First Year Baby Memory Book | Printable Baby Milestone Journal, Growth Album, Baby Shower Gift, Instant Download PDF`

**13 tags:**
baby memory book, first year book, baby milestone book, printable baby book, baby shower gift, new baby gift, baby journal printable, monthly baby book, baby growth album, keepsake baby book, handprint footprint, letter to baby, newborn keepsake

**Category:** Paper & Party Supplies > Paper > Albums & Scrapbooks (or Planners & Organizers — check which ranks better once live)

**Suggested price:** $10–14 USD. Printable keepsake books on Etsy commonly sell $8–20; 24
pages with monthly tracking + letters + hand/footprint page supports the middle-upper end.

**Listing description (draft):**

> **My First Year — a printable memory book for the year that changes everything.**
>
> 24 pastel, ready-to-print pages to capture every part of baby's first year: the birth
> story, monthly photos and milestones, firsts, hand and footprint, and letters you'll
> both cherish reading back one day.
>
> **What's inside:**
> - 📖 Baby details, family tree, birth story & coming home pages
> - ✅ A "firsts" checklist (first smile, first steps, first word, and more)
> - 📅 12 monthly check-in pages — photo, weight/height, and a favorite moment
> - 🖐️ Handprint & footprint page
> - 🎂 First birthday page
> - 💌 Two blank letter pages, for whoever wants to write to baby
>
> **How it works:** instant PDF download — print at home on cardstock, or take it to a
> print shop for spiral binding. No app, no login, yours to keep and reprint forever.
>
> *Pairs beautifully with our Bump to Toddler Planner — start the planner during
> pregnancy, start this book the day baby arrives.*

## Cross-sell note
Once both listings are live, add each as a "you may also like" mention in the other's
description, and consider a small bundle discount — that's the highest-leverage move for
a two-product shop (higher AOV without new production cost).
