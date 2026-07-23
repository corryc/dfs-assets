# Compact Keyword Page System

Templated generator for producing DFS "compact keyword" pages fast: short,
purchase-intent landing pages (~400-500 words) targeting narrow, high-intent
searches, as distinct from the longer blog/explainer content elsewhere in
this repo.

Background: see `WORKLOG.md` 2026-07-24 for the research behind this
(Edward Sturm's "Compact Keywords" method - narrow purchase-intent pages
outperform broad blog content for conversion. Revenue claims from that
course's own marketing are unverified; the underlying principle - narrow
intent-matched pages beat broad explainers - is standard SEO practice
independent of the course).

## Files

- `templates/compact-keyword-template.html` - master template with
  `{{TOKEN}}` placeholders. Built from the real DFS design system
  (`dfs-content-production/references/design-system.md`) and compliance
  rules (`dfs-content-production/references/compliance.md`), not invented
  from scratch.
- `scripts/generate_compact_pages.py` - reads a CSV, fills the template,
  validates each row, writes one `.html` file per row.
- `data/compact-keywords.csv` - example data file with one real sample row
  (SMSF property loan broker, Boronia).
- `generated/` - output folder. Not deployed. Draft pages land here for
  review, not root.

## Usage

```
python3 scripts/generate_compact_pages.py data/compact-keywords.csv
```

Add a row per page to the CSV (see column headers in the sample file),
re-run, and one HTML file is generated per row into `generated/`.

## What the generator checks automatically

- Title length (target 50-60 chars)
- Meta description length (target 155-160 chars)
- Smart quotes / em dashes (catches the mojibake pattern from T012/T013)
- A first-pass scan for the highest-risk unqualified compliance phrases
  from `compliance.md` (e.g. unqualified "no LMI", "guaranteed", specific
  rates or borrowing ranges) - this is a fast pre-check, NOT a substitute
  for the full `/dfs-ad-compliance` skill review
- Rough word count floor (~250 words minimum across the filled fields)

## What the generator does NOT do — mandatory manual gates, unchanged

**Compliance is not optional, for any page this system produces.**

1. Every generated page still requires a full `/dfs-ad-compliance` run
   before it can be considered for publishing. A clean validator pass is
   not a compliance pass - they check different things.
2. Every page still requires a proof/preview and Corry's explicit approval
   before pushing, per standing DFS process.
3. The script never pushes to GitHub or triggers a Netlify deploy. Output
   lands in `generated/` only. Pushing approved pages to repo ROOT (never
   `posts/.../live/` - confirmed non-deployed, see `_redirects` and
   WORKLOG 2026-07-24) and adding the new slug to `sitemap.xml` are
   separate, explicit steps after approval.

## Page structure (deliberately leaner than the full landing-page template)

Compact-keyword pages are shorter than the existing landing-page structure
in `design-system.md` (which has a 4-step "How it Works" grid, two-column
eligibility section, and 6-question FAQ). This template uses:

- Hero (same component as existing landing pages, "Book Free Call" scrolls
  to the on-page form - no phone number in the page's own content)
- Intro box + 3 criteria points (not a 4-step grid)
- 3-question FAQ (not 6)
- One internal link block to a related core service or suburb page
- On-page lead capture form (first name, last name, email, phone, optional
  message) - copied verbatim from the working `contact-us.html` Netlify
  Forms pattern (`data-netlify="true"` + hidden `form-name` field +
  honeypot). All compact-keyword pages share one form name
  (`compact-keyword-enquiry`) so submissions land in one place in the
  Netlify Forms dashboard, with a hidden `source_page` field identifying
  which page each lead came from.
- Closing CTA band with disclaimer, also scrolling to the same form

This keeps pages in the ~400-500 word range the method targets, rather
than reusing the fuller landing-page structure that runs longer.

**No phone number in the page's own body content or CTAs, by explicit
decision (2026-07-24).** The shared site-wide footer still shows the
phone number as normal on every page - that's unrelated and unaffected.

## Two new CSS classes, not yet in shared dfs-styles.css

`.criteria-list` and `.criteria-item` are defined inline in the template
(see comment in the `<head>`) rather than added to the shared stylesheet.
The lead-capture form CSS (`.book-form-card` and related classes) is also
inlined - it's copied from `contact-us.html`'s own page-specific styles,
which are likewise not in the shared stylesheet. If compact-keyword pages
become a permanent page type, consider moving both blocks into
`dfs-styles.css` once, to avoid repeating them on every generated page.
