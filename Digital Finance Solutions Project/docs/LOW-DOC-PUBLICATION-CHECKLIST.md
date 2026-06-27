# LOW DOC HOME LOANS LANDING PAGE — PUBLICATION CHECKLIST

**Status:** Ready for Webflow publication  
**Date:** 21 June 2026  
**File:** low-doc-home-loans-australia.html (26 KB)

---

## PAGE SPECIFICATIONS

**URL Slug:** `/low-doc-home-loans-australia`

**SEO Title:** Low Doc Home Loans Australia | When You Need One | DFS  
**Meta Description:** Low doc home loans use alternative income verification when tax returns don't reflect what you earn. Compare 30+ lenders. Same-day response. Melbourne eastern suburbs.

**H1:** Low Doc Home Loans — For When Your Tax Return Doesn't Tell the Full Story

**Focus Keyphrase:** low doc home loans (1,900/mo, KD 21)

**Word Count:** ~1,250 words

---

## PAGE STRUCTURE

- Hero section with primary CTA
- 5 main content sections (What is low doc, Who uses it, vs full-doc, What docs needed, How much to borrow)
- Trust row (No broker fee, Same-day response, 30+ lenders)
- Verdict section (bottom line)
- 7-item FAQ with schema markup
- Sidebar CTA
- Full LocalBusiness + FAQPage JSON-LD schema

---

## PUBLICATION STEPS (WEBFLOW DESIGNER)

### 1. Create Page
- Open Webflow Designer on digitalfinancesolutions.com.au site
- Create new page: "Low Doc Home Loans Australia"
- Set slug to: `/low-doc-home-loans-australia`
- Set meta title and description (see above)

### 2. Add Code Embed
- Insert Code Embed component on the page
- Paste the full HTML content from `low-doc-home-loans-australia.html` **INSIDE the body only** (not the full HTML doc)
- The Code Embed should contain everything from `<nav>` through `</footer>`

**OR — Full Page Embed:**
- If using full HTML publish method, paste entire document as-is

### 3. SEO & Metadata (via Data API)
Once page is created, run this Webflow Data API call to lock in metadata:

```json
{
  "page_id": "[PAGE_ID_FROM_WEBFLOW]",
  "slug": "low-doc-home-loans-australia",
  "seo": {
    "title": "Low Doc Home Loans Australia | When You Need One | DFS",
    "description": "Low doc home loans use alternative income verification when tax returns don't reflect what you earn. Compare 30+ lenders. Same-day response. Melbourne eastern suburbs."
  }
}
```

### 4. Publishing
- Save as draft first
- Review in preview mode (check mobile responsiveness, CTAs functional, schema validates)
- Publish to custom domain: digitalfinancesolutions.com.au/low-doc-home-loans-australia

---

## TECHNICAL CHECKLIST

- [ ] Slug is exactly `/low-doc-home-loans-australia`
- [ ] SEO title and meta description match spec above
- [ ] H1 is visible and matches target keyphrase
- [ ] Focus keyphrase appears in first 100 words
- [ ] Internal links point to:
  - `/self-employed-home-loan-eastern-suburbs`
  - `/contact-us` (CTAs)
  - Sidebar CTA links to contact form
- [ ] JSON-LD schema is present (LocalBusiness + FAQPage)
- [ ] GSAP animation library loaded (smooth scroll reveals)
- [ ] GitHub CSS file loads: `https://corryc.github.io/dfs-assets/dfs-styles.css`
- [ ] Logo image loads from Webflow CDN
- [ ] Phone number is clickable: `tel:0419891983`
- [ ] All CTAs link to contact form or phone
- [ ] Mobile responsive (tested at 375px, 768px, 1024px viewports)
- [ ] Page loads under 3 seconds (Lighthouse check)
- [ ] No 404s on images or CSS

---

## POST-PUBLICATION

1. **Submit to GSC:** Add to Google Search Console sitemaps
2. **Monitor impressions:** Wait minimum 12 weeks before assessing ranking performance
3. **Create GBP post:** Once live, create corresponding Google Business Profile post via Make.com
4. **Supporting blog posts:** Start publishing 7-post cluster starting week of 28 June 2026 (one post per week)
5. **Internal linking:** Update existing pages (Self-Employed, Doctors) to link to this new page where relevant

---

## SUPPORTING BLOG CLUSTER TIMELINE

| Post # | Title | Target Keyword | Target Week | Status |
|---|---|---|---|---|
| 1 | Low Doc Home Loans — Do You Actually Need One? | low doc home loans | 28 Jun | Scheduled |
| 2 | Low Doc Home Loan: What Lenders Accept & How Much You Can Borrow | low doc home loan | 5 Jul | Scheduled |
| 3 | Low Doc Mortgage Loans for Self Employed | low doc mortgage loans | 12 Jul | Scheduled |
| 4 | How to Get Pre-Approved for a Low Doc Home Loan | low doc home loan australia | 19 Jul | Scheduled |
| 5 | Low Doc vs. Full Doc Home Loans — Which One is Right for You? | low doc loans | 26 Jul | Scheduled |
| 6 | Low Doc Home Loans for Business Owners | low doc business loan | 2 Aug | Scheduled |
| 7 | What Documents Do Lenders Need for a Low Doc Home Loan? | low doc loan | 9 Aug | Scheduled |

---

## NOTES FOR CORRY

**Webflow Data API Alternative (if Designer MCP unavailable):**
If you can't access Webflow Designer MCP, use the Data API directly to update page metadata after page creation:

```javascript
PUT /sites/61fc660e6a44456c36c97404/pages/[PAGE_ID]
{
  "slug": "low-doc-home-loans-australia",
  "seo": {
    "title": "Low Doc Home Loans Australia | When You Need One | DFS",
    "description": "Low doc home loans use alternative income verification when tax returns don't reflect what you earn. Compare 30+ lenders. Same-day response. Melbourne eastern suburbs."
  }
}
```

**Nav Update:** Remember to add Low Doc to the navigation dropdown on key pages (homepage, Self-Employed, this page) when you update nav next time.

**Next Action:** Open Webflow Designer, create page, embed HTML, publish, and confirm live URL is serving correctly.

