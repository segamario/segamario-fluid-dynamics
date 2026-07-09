# Bump to Toddler Planner — Product Plan & Etsy Listing

## What this is
A Google Sheets digital planner covering pregnancy prep through a toddler's 2nd birthday:
trimester checklists, a prenatal health/nutrition tracker, a hospital bag checklist, a
postpartum mom recovery tracker, a newborn daily care log, a baby weekly log (3-24mo),
a growth tracker with an auto-updating chart, a developmental milestones checklist,
a vaccination schedule reference, and a one-page dashboard. Pastel color system throughout
(soft pink / blue / mint / lavender / peach / yellow), 11 tabs total.

## Positioning
Most Etsy "pregnancy planner" or "baby tracker" listings cover *one* phase (either pregnancy
or 0-12 months). This one spans conception prep through age 2 in a single file, so it can be
bought once as a baby-shower gift and used continuously for two years — that's the differentiator
to lead with in the listing photos and description.

## How to produce the sellable master
Two ways to build it — either works, both live in this folder:
1. `build_planner.gs` — Google Apps Script, paste into Extensions > Apps Script on a blank
   sheet and run `buildPregnancyToToddlerPlanner`.
2. `build_planner_xlsx.py` — openpyxl, produces `Bump_to_Toddler_Planner.xlsx` locally; upload
   to Drive and File > Save as Google Sheets to convert. **This is the version actually in use.**

**Master sheet (live):**
https://docs.google.com/spreadsheets/d/1FBUiBwmqy3yc18-WGoC_S6V1wuKqc-E06j3stGpsbuM/edit?usp=sharing
— stored in Drive folder "Little Milestone Co - Bump to Toddler Planner", sharing already set to
Anyone with the link / Viewer. This is the exact link baked into
`delivery-pdf/How-To-Get-Your-Planner.pdf`.

Remaining one-time setup on the master (xlsx route only, ~10 columns): select each
"Done"/"Achieved"/"Given" column and use Insert > Checkbox so they render as clickable
checkboxes instead of TRUE/FALSE text — see the exact column list in the chat history / repeat
below. Also spot-check that the Growth Tracker and Dashboard charts came through the xlsx→Sheets
conversion correctly.

Take screenshots of each tab (Welcome, Prenatal Health with its chart area, Newborn Daily
Log, Dashboard with the 3 charts) for the Etsy listing photos — these sell the product far
more than the description text does.

## Etsy listing copy

**Title** (under 140 characters):
`Pregnancy to Toddler Planner | Google Sheets Baby Tracker, Prenatal & Postpartum Log, Milestones, Growth Chart, Digital Download`

**13 tags:**
pregnancy planner, baby tracker, postpartum planner, newborn checklist, google sheets baby,
baby milestone log, pregnancy checklist, hospital bag list, baby feeding log, new mom planner,
digital baby planner, baby shower gift, baby growth chart

**Category:** Paper & Party Supplies > Paper > Planners & Organizers (Digital Planners)

**Suggested price:** $12–15 USD (intro price $9 for the first ~2 weeks to seed reviews).
Comparable multi-tab Google Sheets planners on Etsy sell in the $8–18 range; this one is more
comprehensive (11 tabs, 2-year span) than most single-phase competitors, which supports the
higher end once you have reviews.

**Listing description (draft):**

> **Bump to Toddler: your pregnancy-to-age-2 planner, all in one Google Sheet.**
>
> From your first prenatal appointment to your toddler's 2nd birthday, this planner keeps
> every checklist, tracker, and milestone in one pastel-pretty Google Sheet — no app to
> download, no subscription, works instantly on your phone, tablet, or laptop.
>
> **What's inside (11 tabs):**
> - 🤰 Pregnancy Prep Checklist — trimester by trimester
> - 🥗 Prenatal Health & Nutrition Tracker — weekly log, dates fill in automatically from your due date
> - 🎒 Hospital Bag Checklist — for mom, baby, and your support person
> - 💗 Postpartum Recovery Tracker — daily log for the first 6 weeks
> - 🍼 Newborn Daily Care Log — feeding, diapers, sleep, temperature (0-3 months)
> - 📅 Baby Weekly Log — a lighter check-in from 3-24 months
> - 📏 Growth Tracker — weight & height with an auto-updating growth chart
> - 🧠 Developmental Milestones — 0-24 months, by age band
> - 💉 Vaccination Schedule — general reference checklist
> - 📊 Dashboard — all your charts on one page
>
> **How it works:** click the link in your download, then File > Make a copy to save it to
> your own Google Drive. Fully editable, yours forever, no expiration.
>
> ⚠️ This planner is for organizational purposes only and doesn't replace medical advice —
> always follow your OB/GYN's or pediatrician's guidance.
>
> *Requires a free Google account. Works on desktop and the Google Sheets mobile app.*

## Delivery mechanics on Etsy
Etsy digital downloads are files, not links, so the standard approach:
1. Make a 1-page PDF ("Click here to get your planner") containing the shareable View link
   and a short "File > Make a copy" instruction with a screenshot. Upload that PDF as the
   Etsy digital file.
2. Never share the *editable* link — always share the "Viewer" link so buyers must make
   their own copy rather than all editing your master simultaneously.

## Content disclaimer note
Two tabs carry real liability surface: **Vaccination Schedule** and the health-threshold
conditional formatting (fever, bleeding, wet-diaper counts) on Prenatal/Postpartum/Newborn
tabs. Both already include an in-sheet disclaimer directing users to their provider — keep
those disclaimers in any edits, and consider repeating the disclaimer in the Etsy listing
description itself (included in the draft above).
