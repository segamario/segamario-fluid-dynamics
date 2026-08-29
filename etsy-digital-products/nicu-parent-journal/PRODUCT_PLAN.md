# A NICU Journal — Product Plan & Etsy Listing

## What this is
A 16-page printable PDF journal for parents with a baby in the NICU: welcome/permission
page, baby & NICU details, a duplicable daily log, questions-for-the-care-team tracker,
care team contacts, feeding/pumping log, NICU-specific milestones (unordered, no pressure),
two unprompted "space for feelings" pages, support & self-care reminders, a siblings-at-home
page, logistics (parking/insurance/social worker), discharge prep, and a quiet closing page.

## Tone — read this before editing copy
This is the most sensitive product in the shop and it is designed differently on purpose:
- **Palette**: muted lavender / sage / slate / dusty rose only. No bright pink, yellow, or
  peach, no cheerful emoji, no "yay!" energy anywhere in the file.
- **No outcome assumptions.** Nothing implies the stay ends a certain way or on a certain
  timeline. Milestones are explicitly framed as "in your own order," not a race.
- **Not medical advice.** The Welcome page states plainly that this isn't a medical record
  and doesn't replace the care team. Keep that framing in the Etsy description too.
- Before changing any copy in `build_journal.py`, reread it out loud — if a line would feel
  presumptuous or falsely upbeat to someone having the worst week of their life, cut it.

## Files
- `build_journal.py` — generates `nicu_journal.html` and renders `A-NICU-Journal.pdf` via
  Playwright. Uses its own `CALM` palette dict (separate from the shop's main `PASTEL`
  dict used in the other three products) — intentionally not shared, don't merge them.
- `A-NICU-Journal.pdf` — upload this directly as the Etsy digital file.
- `listing-images/hero.png`, `listing-images/pages-preview.png` — 2000x2000 listing photos,
  also deliberately quieter than the other listings' image style.

## Etsy listing copy

**Title:**
`A NICU Journal | Printable Journal for NICU Parents, Daily Log, Milestones & Feelings Pages, Preemie Gift, Instant Download PDF`

**13 tags:**
nicu journal, nicu gift, preemie journal, nicu parent gift, preemie gift, nicu tracker, hospital journal baby, preemie mom gift, nicu log printable, newborn hospital journal, preemie milestone, nicu support gift, micro preemie gift

**Category:** Paper & Party Supplies > Paper > Journals & Notebooks

**Suggested price:** $14–18 USD. This is a low-competition, high-emotional-value niche —
price it above the shop's other printables rather than matching them.

**Listing description (draft — deliberately understated, no exclamation points):**

> **A quiet place to keep track, and to feel what you're feeling.**
>
> This 16-page printable journal was made for parents with a baby in the NICU. It's not a
> medical record, and it won't replace anything your care team documents — it's a place for
> the rest: the questions you don't want to forget to ask, the names of everyone caring for
> your baby, the small milestones that happen in whatever order they happen in, and the
> feelings that don't always fit neatly into a day.
>
> **What's inside:**
> - A daily log (duplicate the page for a longer stay)
> - Questions for the care team
> - Care team & contacts tracker
> - Feeding & pumping log
> - NICU milestones — in your own order, at your own pace
> - Two open, lightly-prompted pages for feelings
> - Support & self-care reminders
> - A siblings-at-home page, if that applies to you
> - Logistics: parking, insurance, hospital resources
> - Discharge prep, for whenever that day comes
>
> **How it works:** instant PDF download — print at home or at a print shop. Skip pages
> freely. There's no correct way to use this.
>
> *However this chapter is going for you, we're glad you have somewhere to put it.*

## What NOT to do with this listing
- Don't cross-promote the other shop products inside this listing's description — the
  baby-shower / milestone-celebration framing of the rest of the shop is tonally wrong here.
  If a customer messages asking about the rest of the shop, that's fine to answer directly,
  but don't push it in the copy itself.
- Don't add urgency language ("limited time," "sells fast") to this listing — ever.
- If you ever add a review-solicitation message for this product specifically, keep it
  gentle and optional, not templated with the same energy as the other three.
