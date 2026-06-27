# DFS Brain — Session Startup Document
**Digital Finance Solutions | digitalfinancesolutions.com.au**
*Read this file at the start of every session before doing anything else.*
Last updated: 2026-06-26

---

## WHO IS CORRY

Melbourne-based mortgage broker, eastern suburbs Knox corridor. Born 1986. Direct communicator — short sentences, dash bullets, no fluff. Confirms task completion before moving to the next step. Three active work areas:

- **DFS** — mortgage brokerage, building SEO and inbound inquiry
- **Travel Dayz** — travel blog with partner Ling (early stage, mirrored folder structure exists)
- **Options trading** — systematic iron condor strategies (started 2025)

---

## DFS BUSINESS OVERVIEW

**Target borrowers:** Doctors/medical professionals (no-LMI loans), self-employed + tradies, first home buyers, refinancers, future house-and-land segment.

**Geography focus:** Eastern suburbs — Knox corridor, Ringwood, Bayswater, Croydon, Maroondah, Lilydale, Mooroolbark.

**Key rule:** Lender names never appear on pages — protects Corry's intermediary role.

**Phone:** `0419 891 983` / `tel:0419891983`

**ACL line (exact — no variation):**
`Credit Representative Number 532405 of Beagle Pty Ltd (Australian Credit Licence No. 391237)`

---

## LIVE PAGES

| URL | Status | Date live |
|-----|--------|-----------|
| digitalfinancesolutions.com.au/can-doctors-get-home-loan-no-lmi | ✅ Live | 2026-06-23 |
| digitalfinancesolutions.com.au/buying-house-ringwood-2026 | ✅ Live | 2026-06-25 |
| digitalfinancesolutions.com.au/buying-property-through-a-trust | ✅ Live (rewrite) | 2026-06-26 |
| digitalfinancesolutions.com.au/how-much-can-doctor-borrow-home-loan | ✅ Live | 2026-06-26 |
| digitalfinancesolutions.com.au/dentists-no-lmi-home-loan | ✅ Live | 2026-06-26 |
| digitalfinancesolutions.com.au/signs-paying-too-much-mortgage | 🟡 Draft in Webflow — publish Fri 27 Jun | — |
| digitalfinancesolutions.com.au/what-happens-home-loan-health-check | 🟡 Draft in Webflow — publish Sun 29 Jun | — |

**FHBG landing page:** Draft page ID `6a3e206bf38953145b3fa55e` — HTML written and saved, embed BLOCKED by MCP auth.

**Landing pages (not yet built in Webflow — HTML stubs only in posts/landing-pages/):**
- `/no-lmi-home-loan-doctors-melbourne`
- `/home-loan-health-check`
- `/mortgage-broker-ringwood`
- `/first-home-buyer-guarantee-melbourne`

---

## PIPELINE — BLOCKED ITEMS

**Root cause:** Webflow MCP Bridge desktop app must be running for MCP auth. Closing it breaks the auth token (403). It is NOT a browser URL — `webflow.com/app/mcp-bridge` returns 404. Must be relaunched as a desktop app on Corry's machine.

**Workaround:** Manual HTML paste into Webflow Embed element.

| Task | Page | Webflow Draft ID (if known) |
|------|------|----------------------------|
| Publish when ready | Signs Paying Too Much | — (draft exists, publish Fri 27 Jun) |
| Publish when ready | Health Check Process | — (draft exists, publish Sun 29 Jun) |
| Inject embed + publish | FHBG Landing Page | `6a3e206bf38953145b3fa55e` |

**When MCP Bridge is back online — 5-step injection workflow:**
1. `data_pages_tool` → `create_page` (or use existing page ID)
2. `designer_tool` → `switch_page` to page ID
3. `data_element_tool` → `get_all_elements` (find body element ID)
4. `data_element_builder` → create `HtmlEmbed` (append to body)
5. `data_element_tool` → `set_settings` (key: `"code"`, value = full HTML string)

---

## WEBFLOW DETAILS

- **Site ID:** `61fc660e6a44456c36c97404`
- **Content approach:** Standalone static Pages with Code Embed blocks — NOT Webflow CMS Blog Collection (archived, retired June 2026)
- **Embed character limit:** 50,000 chars — always use external GitHub CSS, never inline styles
- **Designer MCP** (`designer_tool`) requires Designer active in foreground — unreliable. Manual paste preferred.
- **Data API** (`data_pages_tool`) works independently of Designer.

---

## GITHUB CSS + NAV SYSTEM

All pages reference external CSS and a shared nav/footer via GitHub Pages. Repo: `corryc/dfs-assets`

**CSS files:**
- `https://corryc.github.io/dfs-assets/dfs-styles.css`
- `https://corryc.github.io/dfs-assets/dfs-homepage.css`

**Nav loader (MANDATORY on every page):**
```html
<script src="https://corryc.github.io/dfs-assets/dfs-nav-loader.js"></script>
```
Add this to `<head>`. It fetches `dfs-nav.html` from GitHub and injects nav + footer automatically. **Never hardcode `<nav>` or `<footer>` in page HTML.** Edit `dfs-nav.html` on GitHub → all pages update instantly.

**Nav contents:** Services dropdown (Home Loans, Refinancing, Self Employed, Doctors No LMI, Debt Consolidation), Suburbs dropdown, Blog, About. CTA: "Book Free Call" (not "Book a Free Call").

**Local copies in project folder:**
- `dfs-nav.html` — source of truth for nav/footer HTML
- `dfs-nav-loader.js` — the loader script

---

## DFS DESIGN SYSTEM

**HTML approach: `/frontend-design` skill — lean CSS, no GSAP, target under 35kb**
Canonical template: `posts/blog/live/2026-06-26-buying-property-through-a-trust-v2.html`
Adopted 2026-06-26 after original trust blog exceeded Webflow 50k embed limit with GSAP included.

**Font:** Manrope (Google Fonts)

**Head block (every page):**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<script src="https://corryc.github.io/dfs-assets/dfs-nav-loader.js"></script>
```

**Schema markup (MANDATORY on every page — insert before font preconnect):**

Every HTML page must include a `<script type="application/ld+json">` block with all three types:

1. **Article** — headline, description, datePublished, dateModified, author (Organization), publisher (Organization + logo), mainEntityOfPage (@id = canonical URL), articleSection, keywords
2. **FAQPage** — 3–4 Q&As targeting the page's primary search queries. Answer text must be factual, qualified, and match on-page content. This is the most valuable schema for AI search and featured snippets.
3. **BreadcrumbList** — Home → Blog → [Page title] (or Home → [Page title] for landing pages)

**AI crawling optimisation notes:**
- FAQPage schema is the primary signal for AI search engines (Perplexity, ChatGPT Search, Gemini) — make Q&A text comprehensive and direct
- Use `dateModified` to keep content signals fresh — update when page is edited
- `keywords` array should match the GSC/Semrush target list for that page
- Never leave schema placeholder text — all fields must be populated with real page content

**CSS variables:**
```css
--navy: #0d1b2e
--blue: #0052cc
--blue-d: #003d99
--blue-l: #e8f0ff
--teal: #00a896
--teal-l: #e6f7f5
--amber: #f59e0b
--amber-l: #fffbeb
--off: #f5f7fa
--border: #dde3ed
```

**Page structure:**
- Blog posts: `posts/YYYY-MM-DD-slug.html`
- Landing pages: `posts/landing-pages/YYYY-MM-DD-slug.html`

---

## COMPLIANCE — ASIC RG 234 (NON-NEGOTIABLE)

Run `/dfs-ad-compliance` on every post before publishing.

**Qualified language rules:**
- LMI: "may be eligible to avoid LMI, subject to eligibility" — never "no LMI"
- Deposit: "may be able to purchase with as little as a 5% deposit, subject to lender approval and eligibility"
- Never quote borrowing capacity ranges
- Never quote specific interest rates
- Never quote income shading percentages

**Mandatory on every page:**
- ACL line (exact, see top of doc)
- General advice disclaimer: "The information in this article is general in nature and does not constitute financial or credit advice."

See `dfs-ad-compliance/SKILL.md` for full rules and the installed skill.

---

## INSTALLED SKILLS

| Skill | File | Purpose |
|-------|------|---------|
| `dfs-ad-compliance` | `dfs-ad-compliance.skill` + `dfs-ad-compliance/SKILL.md` | ASIC RG 234 compliance check |
| `dfs-content-production` | `dfs-content-production.skill` | Full content production workflow — design system, compliance, Webflow delivery |

---

## GOOGLE DRIVE RESOURCES (pre-Cowork history)

- **DFS root folder ID:** `1G-e-ak4V5E-cepZ1MwPCPA_khas26Q47`
- **DFS Brain doc (Drive version):** `1ivNsIFVKyg4ZMEnVOgnn8mP2Nq5dDpfOtPloi3FyawY` — may contain older history not yet migrated here
- **Subfolders:** Strategy, Landing Pages, SEO Research, Blog Content, Session Logs, Assets
- **19-post content plan** exists in Drive (predates Cowork migration)
- **"7 Easy Steps to Mortgage Freedom" ebook PDF** uploaded to Drive — not yet analyzed

---

## GSC + SEO STATUS (as of late June 2026)

- **Impressions:** Trending up, 300+/day, peaked at 386
- **Clicks:** Flat 0–2/day
- **Core problem:** Backlink profile dominated by `addgoodsites.com` link farm (~70% of profile)
- **Action needed:** Upload disavow file to GSC (file created, targeting `addgoodsites.com`) — must be done on desktop via GSC
- **Suburb pages:** Indexing with impressions but ~0.1% CTR — root cause is generic templated copy (suburb name swapped in, not differentiated)
- **Priority rewrites:** Ringwood and Bayswater suburb pages
- **Strategy:** Disavow first → build blog cluster → reassess after 4–6 weeks

**SEO principle:** Disavow first, then build. DA (blocked by link farm) is the primary lever. Blog cluster is second move.

---

## CONTACT FORM STATUS (pre-Cowork)

- SalesTreeker CRM iframe abandoned — Webflow sandboxing issues
- Replacement: custom HTML form posting to Google Forms in background
- **Google Form URL:** `https://docs.google.com/forms/d/e/1FAIpQLSecYLWifaaNwnUyzK0E_Kao3iywdFVV6YIuMXq493fCq-ZuPQ/viewform`
- **Status:** Stalled — needs Google Form entry IDs extracted (inspect form HTML for `entry.XXXXXXXXXX` fields)
- **Alternative:** Corry open to replacing Google Forms entirely

---

## CONTENT STRATEGY

**4 active keyword clusters:**

| Cluster | Landing page target | Primary kw | Vol | KD |
|---------|--------------------|-----------|----|-----|
| Doctors/Medical | /no-lmi-home-loan-doctors-melbourne | home loans for doctors | 1,000 | 23% |
| Health Check | /home-loan-health-check | home loan health check | 210 | 11% |
| Ringwood/Eastern Suburbs | /mortgage-broker-ringwood | home loans Ringwood | 50 | 6% |
| FHBG / 5% Deposit | /first-home-buyer-guarantee-melbourne | 5 deposit home loans | 1,300 | 38% |

**Scheme name note:** From Oct 2025 officially "Australian Government 5% Deposit Scheme." Searches still use FHBG/first home guarantee — target both phrasings. Do NOT rename landing page slug.

**Semrush:** Purchase deferred pending disavow results. Seeds still to run: first home guarantee, FHBG, no LMI home loan, mortgage broker eastern suburbs, refinance calculator, home loan broker croydon.

**RBA watch dates:** Aug 10–11, Sep 28–29, Nov 2–3, Dec 7–8. Week before each meeting: replace one scheduled post with RBA rate preview.

---

## WEEK 1 CONTENT CALENDAR (23–29 June)

| # | Date | Title | Status |
|---|------|-------|--------|
| 1 | Mon 23 | Can Doctors Get No LMI? | ✅ Live |
| 2 | Tue 24 | News Wrap | ⏭ Skipped |
| 3 | Wed 25 | How Much to Buy in Ringwood 2026? | ✅ Live |
| 4 | Thu 26 | How Much Can a Doctor Borrow? | 🟡 Publish today |
| 5 | Fri 27 | Signs You're Paying Too Much | 🟡 Publish tomorrow |
| 6 | Sat 28 | Do Dentists Qualify for No-LMI? | 🔴 Blocked |
| 7 | Sun 29 | What Happens in a Health Check? | 🔴 Blocked |

---

## FILE MAP

```
Digital Finance Solutions Project/
├── DFS-brain.md                          ← THIS FILE — read first every session
├── DFS-blog-publishing-process.md        ← Step-by-step publishing workflow
├── DFS-progress-log.md                   ← Session log (covers from 23 Jun)
├── 2026-06-23-weekly-content-calendar.md ← Week 1 plan + status
├── keyword-research-tracker.md           ← All Semrush data by cluster
├── dfs-nav.html                          ← Global nav/footer source (GitHub hosted)
├── dfs-nav-loader.js                     ← Nav loader script (GitHub hosted)
├── dfs-ad-compliance.skill               ← Installable compliance skill
├── dfs-content-production.skill          ← Installable content production skill
├── dfs-ad-compliance/
│   ├── SKILL.md                          ← Compliance skill definition
│   ├── test-cases.md
│   └── 2026-06-23-eval-results.html
├── assets/
│   └── css/
│       └── dfs-homepage.css              ← Pre-Cowork CSS (referenced by older pages)
├── data/
│   ├── gsc-raw/                          ← Raw GSC exports, never modified
│   │   ├── gsc-2026-06-13-15month.xlsx   ← 12 Mar 2025 – 11 Jun 2026
│   │   ├── gsc-2026-05-31-3month.xlsx    ← 1 Mar – 31 May 2026
│   │   └── gsc-2026-04-28-3month.zip     ← 26 Jan – 28 Apr 2026
│   ├── gsc-processed/                    ← Cleaned CSVs Claude generates
│   └── seo-tracker.md                    ← Per-page SEO log: keywords, snapshots, change log
├── docs/
│   ├── Fiverr-SEO-Specialist-Complete-Briefing.md
│   └── LOW-DOC-PUBLICATION-CHECKLIST.md
├── posts/
│   ├── blog/
│   │   ├── live/                         ← All published/draft blog posts
│   │   │   ├── 2026-06-25-buying-house-ringwood-2026.html
│   │   │   ├── 2026-06-26-how-much-can-doctor-borrow-home-loan.html
│   │   │   ├── 2026-06-27-signs-paying-too-much-mortgage.html
│   │   │   ├── 2026-06-28-dentists-no-lmi-home-loan.html
│   │   │   ├── 2026-06-29-what-happens-home-loan-health-check.html
│   │   │   ├── blog-self-employed-income-proof.html   ← pre-Cowork, live
│   │   │   └── blog-lenders-beyond-tax-return.html    ← pre-Cowork, live
│   │   └── archive/                      ← Old versions, templates, superseded drafts
│   └── landing-pages/
│       ├── live/                         ← All live landing pages
│       │   ├── 2026-06-26-first-home-buyer-guarantee-melbourne.html
│       │   ├── ringwood-final.html
│       │   ├── bayswater-final.html
│       │   ├── doctors-final.html
│       │   ├── self-employed-final.html
│       │   ├── home-loan-health-check.html
│       │   ├── low-doc-home-loans-australia.html
│       │   ├── mortgage-broker-boronia.html
│       │   ├── mortgage-broker-heathmont.html
│       │   ├── mortgage-broker-bayswater-north.html
│       │   └── contact-us-with-form.html
│       └── archive/                      ← Stubs and older versions
└── zi9C3Ai0                              ← skill zip artifact (ignore)
```

---

## AUTOMATIC DATA RULES (no direction needed from Corry)

### Keyword / SEO data
Any time Semrush or Answer the Public data is pasted or uploaded:
1. Extract all keywords, volumes, KD%, CPC, intent
2. Add to `keyword-research-tracker.md` under the correct cluster (create new cluster if needed)
3. Log the search in the Semrush Search Log (date, seed, tool, match type)
4. Update Rankings Log if position data is included

### GSC data
Any time a GSC file is uploaded (zip, xlsx, csv):
1. **Immediately save** raw file to `data/gsc-raw/` — rename to `gsc-YYYY-MM-DD-[period].zip/xlsx`
   - YYYY-MM-DD = export date
   - period = `7day`, `28day`, `3month`, `6month`, `15month`
   - Examples: `gsc-2026-07-10-7day.zip`, `gsc-2026-07-10-3month.zip`
2. Extract and read Pages.csv + Queries.csv
3. Update snapshot rows in `data/seo-tracker.md` for every matching page
4. Output performance table immediately — all Claude pages, gaps marked "—"
5. Flag any significant movements vs previous snapshot

### Rankings Log format (add to keyword-research-tracker.md per keyword)
| Date | Keyword | Position | Page | Clicks | Notes |

### Page update recommendations
Before recommending any page rewrite or SEO update:
1. Check `data/seo-tracker.md` for that page's Change Log
2. If updated within the last 6 weeks — do NOT recommend a rewrite. Note the last update date and say "wait for Google to reindex — check again [date]"
3. Only recommend changes on pages with no recent updates OR where GSC data shows a specific fixable problem (e.g. wrong keyword in title)
**Rule: Google needs 4–6 weeks to reindex after a change. Don't stack changes — let each one settle.**

### New blog post or landing page HTML
Save to correct folder automatically:
- Blog post → `posts/blog/live/YYYY-MM-DD-slug.html`
- Landing page → `posts/landing-pages/live/YYYY-MM-DD-slug.html`
- Run `/dfs-ad-compliance` before saving

---

## RESPONSE RULES (how Claude should behave)

- **Never wait for perfect data.** When asked about page performance, produce the best table possible from available data immediately. Mark gaps as "—" and note why they're missing. Do not ask for more data before showing what exists.
- **Never ask Corry to validate data Claude already has.** Cross-check screenshots against existing exports internally before responding.
- **Act on available information.** If something is partially known, produce the output with what's known and flag the gaps — don't stall.

## SESSION START CHECKLIST

1. Read this file
2. Check `2026-06-23-weekly-content-calendar.md` for today's post status
3. Check `keyword-research-tracker.md` for active cluster priorities
4. Confirm whether Webflow MCP Bridge is running before attempting injection
5. Run `/dfs-ad-compliance` on any new content before publishing

## SESSION END CHECKLIST

1. Update `DFS-progress-log.md` with what was built today
2. Update this brain doc if anything changed (live pages, blocked items, new files)
3. Update weekly content calendar statuses

---

## KNOWN GAPS (pre-Cowork history not yet documented here)

The project ran in Claude.ai Chat before moving to Cowork (migration date approx. mid-June 2026). The following are known to exist from that history but full details are in Google Drive:

- Full 19-post content plan (Drive)
- All suburb pages built before June 23 (Ringwood, Bayswater, others)
- Self-employed and tradie landing pages (status unknown)
- Original contact form work and SalesTreeker investigation
- Make.com Google Business Profile automation (set up and running)
- Disavow file creation (file ready — pending GSC upload)
- Earlier Semrush research sessions

**To fill this gap:** Read Drive Brain doc ID `1ivNsIFVKyg4ZMEnVOgnn8mP2Nq5dDpfOtPloi3FyawY` at session start if Google Drive MCP is connected.
