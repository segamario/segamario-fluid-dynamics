# Toddler Potty Training Tracker — Product Plan & Etsy Listing

## What this is
A Google Sheets digital tracker for potty training ages 2–4: a readiness checklist, a daily
potty log (successes/accidents, duplicable), a reward/sticker chart with a reward menu,
a separate nighttime training log, a regression log, an accident-pattern log with an
auto-updating chart (accidents by time of day), a milestones checklist, and a one-page
dashboard. Same pastel design system and tab structure pattern as Bump to Toddler Planner —
9 tabs total.

## Positioning
This is the natural sequel purchase for anyone who already owns Bump to Toddler Planner (it
ends at 24 months, right where potty training usually begins) — the single strongest
cross-sell in the shop. Tone matters as much as content here: potty training content on
Etsy skews either clinical or shame-y ("stop accidents fast!"); this one leads with "no
rush, no single right age, regressions are normal" throughout, which is also just accurate
child-development guidance.

## How to produce the sellable master
`build_potty_tracker_xlsx.py` — openpyxl, same helper pattern as
`pregnancy-to-toddler-planner/build_planner_xlsx.py`. Produces
`Toddler_Potty_Training_Tracker.xlsx` locally.

**To finish setup (do this manually — Drive sharing to "Anyone with the link" can't be done
via the available tools, only per-email sharing):**
1. A destination folder already exists in Drive: **"Little Milestone Co - Toddler Potty
   Training Tracker"** (created this session, same parent as the other product folders,
   currently empty).
2. Upload `Toddler_Potty_Training_Tracker.xlsx` into that folder, then File > Save as Google
   Sheets (or just open it — Drive auto-offers the conversion).
3. Share > General access > Anyone with the link > **Viewer**. Copy that link.
4. Select each "Done"/"Achieved"/"Sticker Earned"/"Dry Overnight"/"Reward Given"/"Reward
   Redeemed" column and use Insert > Checkbox to make them interactive (same one-time step
   as the flagship planner).
5. Spot-check that the two charts (Accident Patterns' bar chart, Dashboard's line + bar
   charts) survived the xlsx→Sheets conversion.
6. Re-run the delivery PDF with the real link:
   `python3 delivery-pdf/render.py "<the share link>"` — this overwrites
   `delivery-pdf/How-To-Get-Your-Tracker.pdf` with the real link baked in. **That PDF is
   the actual Etsy digital file** — the placeholder version currently in the repo has a
   dummy link and is not upload-ready yet.

## Etsy listing copy

**Title:**
`Toddler Potty Training Tracker | Google Sheets Printable, Reward Chart, Daily Log, Readiness Checklist, Digital Download`

**13 tags:**
potty training tracker, potty training chart, toddler reward chart, sticker chart potty, potty training printable, google sheets toddler, potty training checklist, toddler behavior chart, potty training gift, daycare potty log, toilet training tracker, potty chart printable, new mom digital planner

**Category:** Paper & Party Supplies > Paper > Planners & Organizers (Digital Planners)

**Suggested price:** $9–12 USD. Comparable to the flagship planner's bracket; this one has
fewer tabs (9 vs 11) so price slightly under it rather than matching.

**Listing description (draft):**

> **A calm, encouraging potty training tracker — for you and your toddler.**
>
> No pressure, no shame, no single "right" age to start. This 9-tab Google Sheet keeps the
> readiness signs, daily log, reward chart, and milestones all in one place — so you can
> actually see the trend instead of just the hard days.
>
> **What's inside (9 tabs):**
> - ✅ Readiness Checklist — physical, behavioral & skill signs, not a deadline
> - 📝 Daily Potty Log — one row a day, dates fill in automatically
> - ⭐ Reward Chart — sticker tracker plus a reward menu you build with your child
> - 🌙 Nighttime Training — a separate, later-stage log
> - 🔄 Regression Log — for the setbacks that come with life's big changes
> - 📍 Accident Patterns — auto-charted by time of day, so you can plan ahead
> - 🎉 Milestones — the bigger checkpoints, in whatever order they happen
> - 📊 Dashboard — successes vs. accidents and progress, on one page
> - Welcome & How-To-Use guide
>
> **How it works:** click the link in your download, then File > Make a copy to save it to
> your own Google Drive. Fully editable, yours forever, no expiration.
>
> *Requires a free Google account. Works on desktop and the Google Sheets mobile app.*

## Cross-sell note
Mention this listing from the Bump to Toddler Planner's description once both are live
("planner ends at 24 months — continue with our Potty Training Tracker") and vice versa.
This pair is the shop's most natural bundle; consider an Etsy "frequently bought together"
style callout once there are reviews on both.
