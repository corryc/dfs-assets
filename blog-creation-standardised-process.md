# DFS Blog Page Creation Process (Standardised)

**Status:** Established 2026-07-11
**Last Updated:** 2026-07-23 (Template Locked Complete + Audit Fixes)
**Purpose:** Ensure all new blog pages meet DFS quality, compliance, and design standards

🔒 **LOCKED TEMPLATE (2026-07-23):** All DFS blogs now follow ONE standardised design. No custom variations. See template below for exact spec.

---

## Pre-Creation Phase

### 1. Content Brief
- Define target keywords (research via Semrush)
- Identify landing page it supports
- Confirm keyword volume, difficulty, search intent
- Note Semrush date for records

### 2. Design Direction (LOCKED TEMPLATE — No Variations)

⚠️ **DFS blogs now use ONE standardised design. Do NOT customize.**

All blogs must follow:
- **Typography:** Manrope only (weights: 400, 500, 600, 700, 800)
- **Color palette:** Navy (#0d1b2e), Blue (#0052cc), Teal (#00a896), Amber (#f59e0b)
- **Layout:** Hero (navy bg) → Article+Sidebar grid → Form → Final CTA band
- **Metadata:** Clock/document/calendar SVG icons in hero (MUST include CSS styling)
- **Buttons:** "Book Free Call" (.btn-white-solid) + "Chat on WhatsApp" (.btn-whatsapp #25d366)
- **Form:** 6 fields (name, email, phone, loan type, amount, notes) with Netlify honeypot
- **Schema:** Article + FAQPage + BreadcrumbList (3 schema types required)

See **Complete HTML Template** below for exact structure. Copy, paste, fill in content.

---

## Build Phase

### 3. Complete HTML Template (LOCKED — Copy & Use)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="page-type" content="blog-post">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[PAGE TITLE] | DFS</title>
  <meta name="description" content="[150-160 chars, includes keyword, qualified claims]">
  <meta property="og:title" content="[OG Title]">
  <meta property="og:description" content="[OG Description]">

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Article",
        "headline": "[Headline]",
        "description": "[Description]",
        "datePublished": "2026-07-23",
        "dateModified": "2026-07-23",
        "author": {"@type": "Organization", "name": "Digital Finance Solutions", "url": "https://www.digitalfinancesolutions.com.au"},
        "publisher": {"@type": "Organization", "name": "Digital Finance Solutions", "url": "https://www.digitalfinancesolutions.com.au", "logo": {"@type": "ImageObject", "url": "https://cdn.prod.website-files.com/61fc660e6a44456c36c97404/61fc660e6a4445dec6c974a5_Digital-Finance-Logo.svg"}},
        "mainEntityOfPage": {"@type": "WebPage", "@id": "https://digitalfinancesolutions.com.au/[slug]"},
        "articleSection": "Home Loans",
        "keywords": ["[kw1]", "[kw2]", "[kw3]"]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {"@type": "Question", "name": "[Q1]", "acceptedAnswer": {"@type": "Answer", "text": "[A1]"}},
          {"@type": "Question", "name": "[Q2]", "acceptedAnswer": {"@type": "Answer", "text": "[A2]"}},
          {"@type": "Question", "name": "[Q3]", "acceptedAnswer": {"@type": "Answer", "text": "[A3]"}}
        ]
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://digitalfinancesolutions.com.au/"},
          {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://digitalfinancesolutions.com.au/blog"},
          {"@type": "ListItem", "position": 3, "name": "[Page Title]", "item": "https://digitalfinancesolutions.com.au/[slug]"}
        ]
      }
    ]
  }
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
  :root {
    --navy: #0d1b2e; --blue: #0052cc; --blue-dark: #003d99; --blue-light: #e8f0ff;
    --teal: #00a896; --teal-light: #e6f7f5; --amber: #f59e0b; --amber-light: #fffbeb;
    --white: #ffffff; --off-white: #f5f7fa; --light-grey: #eef1f6; --border: #dde3ed;
    --text-dark: #0d1b2e; --text-mid: #3d4f6b; --text-light: #6b7c99;
  }
  /* CRITICAL: Include .blog-meta-item svg CSS rule below */
  .blog-meta-item svg { width: 15px; height: 15px; stroke: rgba(255,255,255,0.4); fill: none; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; flex-shrink: 0; }
  /* Add all other CSS from standardised template here... */
  @media (max-width: 960px) { .blog-body { grid-template-columns: 1fr; gap: 40px; } .sidebar { position: static; order: -1; } }
  @media (max-width: 600px) { .blog-hero { padding: 48px 20px 40px; } .blog-body { padding: 40px 20px; } .closing-cta { padding: 56px 20px; } .closing-cta-buttons { flex-direction: column; align-items: center; } }
  </style>

  <script src="https://corryc.github.io/dfs-assets/dfs-nav-loader.js"></script>
  <link rel="canonical" href="https://digitalfinancesolutions.com.au/[slug]">
</head>
<body>

<!-- HERO SECTION (Navy bg, metadata SVG icons, accent text) -->
<section class="blog-hero">
  <div class="blog-hero-inner">
    <div class="blog-category"><span class="blog-category-dot"></span>[Category]</div>
    <h1>[Headline with <span class="accent">Accent</span>]</h1>
    <p class="blog-hero-sub">[Subtitle]</p>
    <div class="blog-meta">
      <div class="blog-meta-item"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>[X] min read</div>
      <div class="blog-meta-divider" aria-hidden="true"></div>
      <div class="blog-meta-item"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>Digital Finance Solutions</div>
      <div class="blog-meta-divider" aria-hidden="true"></div>
      <div class="blog-meta-item"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 12a9 9 0 1 0 18 0 9 9 0 0 0-18 0"/><path d="M12 8v4l3 3"/></svg>July 2026</div>
    </div>
  </div>
</section>

<!-- ARTICLE + SIDEBAR LAYOUT -->
<div class="blog-body">
  <main class="article">
    <div class="intro-box"><p>[Intro paragraph]</p></div>
    <!-- Content sections with h2, p, callouts, checklists, pros/cons -->
    <!-- Internal link block (before FAQ) -->
    <!-- FAQ accordion with 3+ items -->
  </main>
  <aside class="sidebar">
    <!-- Blue CTA card: "Book Free Call" button -->
    <!-- Quick facts card with teal dots -->
  </aside>
</div>

<!-- 6-FIELD CONTACT FORM (Netlify) -->
<section style="background: var(--off-white); padding: 48px 24px; margin: 0;">
  <div style="max-width: 600px; margin: 0 auto;">
    <form name="[slug]-enquiry" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/thank-you">
      <input type="hidden" name="form-name" value="[slug]-enquiry">
      <p style="display:none"><label><input name="bot-field"></label></p>
      <div><label>Full name *</label><input type="text" name="full_name" required></div>
      <div><label>Email *</label><input type="email" name="email" required></div>
      <div><label>Phone *</label><input type="tel" name="phone" required></div>
      <div><label>Loan type</label><input type="text" name="loan_type"></div>
      <div><label>Loan amount</label><input type="text" name="loan_amount"></div>
      <div><label>Additional questions</label><input type="text" name="notes"></div>
      <button type="submit">Send Enquiry</button>
      <p style="font-size:12px; color: var(--text-light); margin-top: 12px; text-align: center;">
        We respond within 24 hours. Credit Representative Number 532405 of Beagle Pty Ltd (Australian Credit Licence No. 391237)
      </p>
    </form>
  </div>
</section>

<!-- FINAL CTA BAND (Blue, Book Free Call + Chat on WhatsApp buttons) -->
<section class="closing-cta">
  <div class="closing-cta-inner">
    <div class="closing-cta-eyebrow">Ready to Get Approved</div>
    <h2>[CTA Headline]</h2>
    <p>[CTA Description]</p>
    <div class="closing-cta-buttons">
      <a href="https://digitalfinancesolutions.com.au/contact-us" class="btn-white-solid">Book Free Call</a>
      <a href="https://wa.me/610419891983?text=Hi, I'd like to get quick mortgage advice about my mortgage options. Can we chat?" target="_blank" rel="noopener noreferrer" class="btn-whatsapp">Chat on WhatsApp</a>
    </div>
  </div>
</section>

<!-- FAQ ACCORDION JAVASCRIPT -->
<script>
document.querySelectorAll('.faq-q').forEach(q => {
  q.addEventListener('click', () => {
    q.closest('.faq-item').classList.toggle('open');
  });
});
</script>

<!-- FOOTER LOADER (Mandatory) -->
<script src="https://corryc.github.io/dfs-assets/dfs-footer-loader.js"></script>

</body>
</html>
```

### 4. Frontend-Design Implementation

**Apply the aesthetic direction you chose:**

- **Typography hierarchy:** Use distinctive fonts; size h1 56px+, h2 40px+, p 17px+
- **Color & gradients:** Implement accent colors, gradient backgrounds (hero + CTAs)
- **Visual depth:** Add ::before pseudo-elements (decorative circles), shadows, layered backgrounds
- **Spacing:** Increase section padding (100px), gaps (80px+), breathing room
- **Components:** Styled tip cards with hover effects, form inputs with focus states, smooth transitions
- **Interactive polish:** Cubic-bezier easing, transform animations, rotating FAQ arrow, card hover lift
- **Responsive:** Mobile breakpoints at 768px, adjust padding/font sizes

**CSS Strategy:**
- Use CSS variables for consistency (:root theme)
- Build component classes (tip-card, cta-band, form-block, etc.)
- Add hover/focus states for all interactive elements
- Include media queries for responsive design

### 5. Schema Markup (Mandatory)

Include three schema types in `<script type="application/ld+json">`:
- **Article:** headline, description, datePublished, author, publisher, mainEntityOfPage
- **FAQPage:** mainEntity array with questions + answers
- **BreadcrumbList:** Home → Blog → This Page

### 6. Contact Form (6 Fields — Netlify + Honeypot)

**Required Fields (In Order):**
1. Full name (text, required)
2. Email (email, required)
3. Phone (tel, required)
4. Loan type/category (text)
5. Loan amount (text)
6. Additional questions/notes (text)

**Form Attributes:**
- `method="POST" data-netlify="true" netlify-honeypot="bot-field"`
- `action="/thank-you"`
- Include hidden `form-name` input
- Include hidden honeypot field (display: none)

**Footer Line (EXACT TEXT):**
```
Credit Representative Number 532405 of Beagle Pty Ltd (Australian Credit Licence No. 391237)
```

### 7. Compliance (ASIC RG 234 — Mandatory)

**Qualified Language (Required):**
- "may be eligible", "could", "might", "subject to eligibility", "could help"
- Example: "You **may** be eligible to avoid LMI" ✅  NOT "Avoid LMI" ❌

**Banned Phrases (NEVER use):**
- ❌ "guaranteed" / "guarantees" / "guarantee approval"
- ❌ "certain" / "certainty"
- ❌ "always" / "never" (absolute statements)
- ❌ "avoid all LMI" (unqualified)
- ❌ "no fees"
- ❌ "best rates"
- ❌ "fastest approval"
- ❌ Any specific interest rates or percentage claims

**Required Compliance Lines:**
- Phone: `0419 891 983` (or `tel:0419891983`)
- AFSL line (exact): `Credit Representative Number 532405 of Beagle Pty Ltd (Australian Credit Licence No. 391237)`
- General advice disclaimer: `The information in this article is general in nature and does not constitute financial or credit advice.`

---

## Pre-Publication Checklist

### 8. Verification Checklist

**Technical:**
- [ ] Nav loader in `<head>`: `<script src="https://corryc.github.io/dfs-assets/dfs-nav-loader.js"></script>`
- [ ] Footer loader before `</body>`: `<script src="https://corryc.github.io/dfs-assets/dfs-footer-loader.js"></script>`
- [ ] NO hardcoded nav/footer HTML
- [ ] Canonical URL non-www: `https://digitalfinancesolutions.com.au/[slug]`
- [ ] Meta description 150-160 chars, includes keyword
- [ ] OG tags present (title + description)

**Forms & Interaction:**
- [ ] 6-field contact form all fields working
- [ ] Form honeypot protection: `netlify-honeypot="bot-field"`
- [ ] Form action: `/thank-you`
- [ ] FAQ accordion opens/closes smoothly (with animation)
- [ ] FAQ arrow rotates on open

**Design & Styling:**
- [ ] **SVG metadata icons render correctly** (clock, document, calendar — NOT black circles/blocks)
  - MUST have: `.blog-meta-item svg { width: 15px; height: 15px; stroke: rgba(255,255,255,0.4); fill: none; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; flex-shrink: 0; }`
- [ ] All buttons have correct styles and hover effects
- [ ] WhatsApp button is #25d366 green, not blue
- [ ] Internal link block present (between content and FAQ)
- [ ] Mobile responsive: test at 375px, 768px, 1280px
  - Check sidebar moves below article on mobile
  - Check buttons stack on mobile

**Schema & SEO:**
- [ ] Schema valid: test with Google's structured data tester
- [ ] Article schema has all fields
- [ ] FAQPage schema matches accordion questions
- [ ] BreadcrumbList has 3 items

**Compliance:**
- [ ] All benefit claims qualified ("may", "could", "subject to")
- [ ] No banned phrases (search for: "guaranteed", "certain", "avoid all")
- [ ] Phone number correct: `0419 891 983`
- [ ] AFSL line exact: "Credit Representative Number 532405 of Beagle Pty Ltd (Australian Credit Licence No. 391237)"
- [ ] General advice disclaimer present

**Buttons & CTAs:**
- [ ] "Book Free Call" button links to: `https://digitalfinancesolutions.com.au/contact-us`
- [ ] "Chat on WhatsApp" button links to: `https://wa.me/610419891983?text=Hi, I'd like to get quick mortgage advice about my mortgage options. Can we chat?`

### 9. Frontend-Design QA

- [ ] Typography hierarchy visually clear (h1 > h2 > p)
- [ ] Color palette cohesive (dominant + accent colors used consistently)
- [ ] Hover effects smooth and memorable (cards lift, buttons glow, arrow rotates)
- [ ] Spacing generous and intentional (no cramped sections)
- [ ] Visual depth present (gradients, shadows, layered elements)
- [ ] Design feels intentional, not generic

### 10. Compliance Audit (MANDATORY — Before Any Publish)

**ALWAYS run compliance check before publishing. Every time. No exceptions.**

Run `/dfs-ad-compliance` (if available) or manual check:
- [ ] All benefit claims qualified: "may", "could", "might", "subject to eligibility"
- [ ] No banned phrases: guaranteed, certain, avoid all, no fees, best rates, fastest, only
- [ ] No unqualified "certainty" language (use "clarity" or "transparency" instead)
- [ ] Contact phone correct: `0419 891 983`
- [ ] AFSL line exact: `Credit Representative Number 532405 of Beagle Pty Ltd (Australian Credit Licence No. 391237)`
- [ ] General advice disclaimer: `The information in this article is general in nature and does not constitute financial or credit advice.`

**If any issues found:** Fix, re-audit, then proceed to publish. Never publish without compliance pass.

---

## Publishing

### 11. File Naming & Location
- **Blog posts:** root directory, kebab-case
- Use kebab-case slugs matching URL path
- Example: `pre-approval-worth-the-hassle.html` → `/pre-approval-worth-the-hassle`

### 12. Git Workflow
- Add file to repo
- Commit with message: "[BLOG] Add [page-title] post"
- Include: keyword, target landing page, Semrush date in commit
- Push to GitHub
- Monitor GSC for indexing

### 13. Post-Publication
- Submit URL to Google Search Console for manual indexing
- Monitor GSC inspection (expect within 48 hours)
- Verify canonical tag resolves correctly
- Test forms submission

---

## Key Rules (Non-negotiable — Locked Template)

1. **NO CUSTOM DESIGN.** All blogs use IDENTICAL locked template
2. **NO hardcoded nav/footer.** Always use loaders (dfs-nav-loader.js + dfs-footer-loader.js)
3. **Canonical URLs non-www.** `https://digitalfinancesolutions.com.au/[slug]`
4. **SVG metadata icon styling MANDATORY.** Hero metadata MUST have CSS: `.blog-meta-item svg { width: 15px; height: 15px; stroke: rgba(255,255,255,0.4); fill: none; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; flex-shrink: 0; }`
5. **Form always 6 fields.** name, email, phone, loan_type, loan_amount, notes (with Netlify + honeypot)
6. **Schema required.** Article + FAQPage + BreadcrumbList (3 schema types)
7. **Compliance ASIC RG 234.** Qualified language, no banned phrases, AFSL + disclaimer visible
8. **Mobile responsive.** Test at 375px, 768px, 1280px with media queries
9. **Buttons exact.** "Book Free Call" (.btn-white-solid) + "Chat on WhatsApp" (.btn-whatsapp #25d366)
10. **Testing before publish.** Forms work, loaders load, schema valid, SVG icons render correctly

---

## Example Publications

### 2026-07-11 — Two pages published
- **Pre-Approval Worth the Hassle** → https://digitalfinancesolutions.com.au/pre-approval-worth-the-hassle
  - Keywords: "pre approval home loan" (1,900/mo, 30% KD), "home loan pre-approval" (1,600/mo, 53% KD)
  - Semrush data: 2026-07-11
  - Indexing requested to GSC
  
- **Improve Your Home Loan Approval Chances** → https://digitalfinancesolutions.com.au/improve-loan-approval-chances-melbourne
  - Keywords: "home loan approval" cluster (29,920/mo, 34% avg KD)
  - Semrush data: 2026-07-11
  - Indexing requested to GSC
