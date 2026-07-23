# DFS Blog Post Creation Process (Standardized)

**Status:** Established 2026-07-23  
**Template Locked:** All DFS blog posts MUST follow this exact specification

---

## FINALIZED BLOG TEMPLATE SPECIFICATION

### Font Stack
- **Font:** Manrope only (weights: 400, 500, 600, 700, 800)
- **H1:** clamp(28px, 4vw, 46px), weight 800, line-height 1.15
- **H2:** clamp(20px, 2.5vw, 26px), weight 800, line-height 1.2
- **Body:** 16px, weight 400-500, line-height 1.7
- **Form buttons:** 15px, weight 700

### Color Palette (CSS Variables)
```css
:root {
  --navy:        #0d1b2e;      /* Hero background, text-dark */
  --blue:        #0052cc;      /* Primary CTAs, sidebar */
  --blue-dark:   #003d99;      /* CTA hover state */
  --blue-light:  #e8f0ff;      /* Intro box background */
  --teal:        #00a896;      /* Icons, callouts, highlights */
  --teal-light:  #e6f7f5;      /* Callout backgrounds */
  --amber:       #f59e0b;      /* Warning boxes */
  --amber-light: #fffbeb;      /* Warning backgrounds */
  --white:       #ffffff;
  --off-white:   #f5f7fa;
  --light-grey:  #eef1f6;
  --border:      #dde3ed;
  --text-dark:   #0d1b2e;
  --text-mid:    #3d4f6b;
  --text-light:  #6b7c99;
}
```

### HTML Skeleton Template (Copy-Paste Ready)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="page-type" content="blog-post">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Page Title] | DFS</title>
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
    --white: #ffffff; --off-white: #f5f7fa; --light-grey: #eef1f6; --border: #dde3ed;
    --text-dark: #0d1b2e; --text-mid: #3d4f6b; --text-light: #6b7c99;
    --navy: #0d1b2e; --blue: #0052cc; --blue-dark: #003d99; --blue-light: #e8f0ff;
    --teal: #00a896; --teal-light: #e6f7f5; --amber: #f59e0b; --amber-light: #fffbeb;
  }
  /* ... (include all CSS from layout specifications) ... */
  .blog-meta-item svg { width: 15px; height: 15px; stroke: rgba(255,255,255,0.4); fill: none; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; flex-shrink: 0; }
  </style>

  <script src="https://corryc.github.io/dfs-assets/dfs-nav-loader.js"></script>
  <link rel="canonical" href="https://digitalfinancesolutions.com.au/[slug]">
</head>
<body>

<!-- NAV injected by loader -->

<section class="blog-hero">
  <div class="blog-hero-inner">
    <div class="blog-category"><span class="blog-category-dot"></span>[Category]</div>
    <h1>[Main Headline with <span class="accent">Accent</span>]</h1>
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

<div class="blog-body">
  <main class="article">
    <!-- Intro box, content sections, internal-link-block, FAQ -->
  </main>
  <aside class="sidebar">
    <!-- Sidebar CTA + quick facts -->
  </aside>
</div>

<!-- Form section -->
<!-- Final CTA band -->

<script>
document.querySelectorAll('.faq-q').forEach(q => {
  q.addEventListener('click', () => {
    q.closest('.faq-item').classList.toggle('open');
  });
});
</script>

<script src="https://corryc.github.io/dfs-assets/dfs-footer-loader.js"></script>

</body>
</html>
```

### Layout Structure (No Exceptions)

1. **Hero Section**
   - Background: Navy (`--navy`)
   - Padding: 72px top/bottom, 32px sides
   - Category badge with teal dot
   - H1 with accent color (#7eb3ff)
   - Subtitle (hero-sub)
   - **Metadata with SVG icons** — MUST include CSS:
     ```css
     .blog-meta-item svg {
       width: 15px; height: 15px;
       stroke: rgba(255,255,255,0.4);
       fill: none;
       stroke-width: 2;
       stroke-linecap: round;
       stroke-linejoin: round;
       flex-shrink: 0;
     }
     ```
   - Three metadata items: clock (read time), document (author), calendar (date)

2. **Blog Body Grid**
   - Max-width: 1200px
   - Padding: 64px vertical, 32px horizontal
   - Two-column layout: article + 300px sidebar
   - Gap: 56px

3. **Intro Box**
   - Background: Blue-light
   - Border-left: 4px solid blue
   - Border-radius: 0 10px 10px 0
   - Padding: 22px 26px

4. **Content Sections**
   - H2 headings
   - Paragraphs with body styling
   - Callout boxes (teal-light background)
   - Warning boxes (amber-light background)
   - Checklists (with teal checkmark icons)
   - Pros/cons cards (2-column grid)

5. **Internal Link Block**
   - Background: off-white
   - Border: 1.5px solid border color
   - Border-radius: 12px
   - Padding: 24px 26px
   - Flexbox: left-aligned icon (40x40px, blue-light bg) + content
   - Content: H4 title, description paragraph, arrow link
   - Purpose: Link to related landing page
   - Example: "Expert Self-Employed Lending" → landing page URL

6. **FAQ Accordion**
   - 3+ questions matching schema
   - `.faq-item` with `.open` state
   - Smooth max-height animation (0.25s ease)
   - Arrow indicator (down arrow, rotates on open)

7. **Sidebar** (sticky at top: 96px)
   - CTA card (blue background, white text)
     - "Book Free Call" button (.btn-white)
     - Eyebrow label
   - Quick facts card
     - List with teal dots

8. **Contact Form Section**
   - Background: off-white
   - 6 fields (in order):
     1. Full name (required)
     2. Email (required)
     3. Phone (required)
     4. Loan type/category (text field)
     5. Loan amount (text field)
     6. Additional questions/notes (text field)
   - Netlify form with honeypot protection
   - Submit button (blue background)
   - AFSL disclaimer line visible

9. **Final CTA Band**
   - Background: Blue
   - Padding: 80px vertical, 32px horizontal
   - Text-align: center
   - Eyebrow label
   - H2 heading
   - Paragraph
   - Two buttons side-by-side:
     - `.btn-white-solid`: "Book Free Call" → https://digitalfinancesolutions.com.au/contact-us
     - `.btn-whatsapp`: "Chat on WhatsApp" → https://wa.me/610419891983?text=Hi, I'd like to get quick mortgage advice about my mortgage options. Can we chat?

### Button Styles

**Primary Button (.btn-primary)**
- Background: blue
- Color: white
- Padding: 14px 32px
- Shadow: 0 2px 8px rgba(0,82,204,0.3)
- Hover: blue-dark, translateY(-1px)

**White Solid Button (.btn-white-solid)**
- Background: white
- Color: blue
- Padding: 14px 28px
- Shadow: 0 2px 12px rgba(0,0,0,0.15)
- Hover: off-white, translateY(-1px)

**WhatsApp Button (.btn-whatsapp)**
- Background: #25d366 (WhatsApp green)
- Color: white
- Padding: 14px 28px
- Shadow: 0 2px 12px rgba(37, 211, 102, 0.25)
- Hover: #20ba58, translateY(-1px), box-shadow: 0 4px 16px rgba(37, 211, 102, 0.35)

### Mobile Responsive Breakpoints

```css
/* Tablet & below: sidebar moves below article */
@media (max-width: 960px) {
  .blog-body { grid-template-columns: 1fr; gap: 40px; }
  .sidebar { position: static; order: -1; }
  .sidebar-cta { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; align-items: center; }
}

/* Mobile: reduce padding, stack buttons */
@media (max-width: 600px) {
  .blog-hero { padding: 48px 20px 40px; }
  .blog-body { padding: 40px 20px; }
  .closing-cta { padding: 56px 20px; }
  .closing-cta-buttons { flex-direction: column; align-items: center; }
}
```

### Navigation & Footer (Mandatory)

- **Nav loader:** `<script src="https://corryc.github.io/dfs-assets/dfs-nav-loader.js"></script>` in `<head>`
- **Footer loader:** `<script src="https://corryc.github.io/dfs-assets/dfs-footer-loader.js"></script>` before `</body>`
- **Never hardcode** nav or footer HTML
- Footer handles universal compliance language

### Schema Markup (Required)

Include three schema types in `<script type="application/ld+json">`:

1. **Article**
   - headline, description
   - datePublished, dateModified
   - author (Organization: Digital Finance Solutions)
   - publisher (with logo)
   - mainEntityOfPage (@id = canonical URL)
   - articleSection: "Home Loans"
   - keywords array

2. **FAQPage**
   - mainEntity array with 3+ questions
   - Each question has acceptedAnswer
   - Must match accordion questions in HTML

3. **BreadcrumbList**
   - Home → Blog → This Page
   - Non-www URLs: https://digitalfinancesolutions.com.au/[slug]

### Contact Form (6 Fields)

```html
<form name="[slug]-enquiry" method="POST" data-netlify="true" netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="[slug]-enquiry">
  <p style="display:none"><label><input name="bot-field"></label></p>
  
  <!-- Full name -->
  <div class="dfs-field">
    <label>Full name *</label>
    <input type="text" name="full_name" required>
  </div>
  
  <!-- Email -->
  <div class="dfs-field">
    <label>Email *</label>
    <input type="email" name="email" required>
  </div>
  
  <!-- Phone -->
  <div class="dfs-field">
    <label>Phone *</label>
    <input type="tel" name="phone" required>
  </div>
  
  <!-- Loan type/category -->
  <div class="dfs-field">
    <label>Loan type</label>
    <input type="text" name="loan_type">
  </div>
  
  <!-- Loan amount -->
  <div class="dfs-field">
    <label>Approximate amount</label>
    <input type="text" name="loan_amount">
  </div>
  
  <!-- Notes -->
  <div class="dfs-field">
    <label>Additional questions</label>
    <input type="text" name="notes">
  </div>
  
  <button type="submit">Send Enquiry</button>
  <p class="dfs-form-note">
    We respond within 24 hours. No obligation. 
    Credit Representative Number 532405 of Beagle Pty Ltd (Australian Credit Licence No. 391237)
  </p>
</form>
```

---

## Pre-Publication Checklist

### Technical Verification
- [ ] Nav loader script present in `<head>`
- [ ] Footer loader script present before `</body>`
- [ ] Canonical URL correct (non-www format)
- [ ] Meta description 150-160 chars, includes keyword
- [ ] All forms submit-able (no validation errors)
- [ ] FAQ accordion opens/closes smoothly
- [ ] All CTA buttons link to correct targets
- [ ] Schema markup valid (test with Google's structured data tester)
- [ ] Compliance disclaimers present
- [ ] AFSL number visible on form
- [ ] **Metadata SVG icons render correctly** (clock, document, calendar — not black circles)
  - Verify `.blog-meta-item svg` CSS rule is present with correct styling
- [ ] Mobile responsive (test at 375px, 768px, 1280px)

### Content Quality
- [ ] Typography hierarchy visually clear (H1 > H2 > body)
- [ ] Color palette cohesive and consistent
- [ ] Hover effects smooth (buttons, accordion arrow)
- [ ] Spacing intentional and generous
- [ ] Design feels intentional, not generic

### Compliance

**Qualified Language (Required):**
- All benefit claims qualified: "may", "could", "might", "subject to eligibility", "could be eligible"
- Example: "You may be eligible to avoid LMI" NOT "Avoid LMI"

**Banned Phrases (NEVER use):**
- ❌ "guaranteed" / "guarantees approval"
- ❌ "certain" / "certainty of approval"
- ❌ "always" / "never" (absolute statements)
- ❌ "avoid all LMI" (unqualified benefit claim)
- ❌ "no fees" (unqualified claim)
- ❌ "best rates" (unqualified claim)
- ❌ "fastest approval" (unqualified claim)
- ❌ Any specific interest rates or percentage claims
- ❌ "Australian Credit Licence No. 391237" (must include full ACL line, see below)

**Required Compliance Lines:**
- [ ] Phone: `0419 891 983` or `tel:0419891983`
- [ ] AFSL line exact: `Credit Representative Number 532405 of Beagle Pty Ltd (Australian Credit Licence No. 391237)`
- [ ] General advice disclaimer: "The information in this article is general in nature and does not constitute financial or credit advice."

---

## File Naming & Git Workflow

**File location:** Blog posts in dfs-assets repo root as `[slug].html`

**Git workflow:**
```bash
git pull origin main          # Always pull first
git add [slug].html
git commit -m "[BLOG] Add [page-title]
  
Target keyphrase: [keyword]
Search volume: [volume]/mo
Semrush date: [date]

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"

git push origin main
```

**Post-publication:**
1. Submit URL to Google Search Console for manual indexing
2. Monitor GSC inspection (expect within 48 hours)
3. Verify canonical tag resolves
4. Test form submission end-to-end

---

## Critical Rules (Non-negotiable)

1. **No hardcoded nav/footer** — Always use loaders
2. **Canonical URLs non-www** — https://digitalfinancesolutions.com.au/[slug]
3. **Compliance first** — Qualified language, AFSL visible, disclaimer present
4. **Template consistency** — Design, fonts, colors, layout locked
5. **Schema required** — Article + FAQPage + BreadcrumbList on every post
6. **Metadata SVG styling mandatory** — `.blog-meta-item svg` rule MUST be present
7. **Form always 6 fields** — name, email, phone, category, amount, notes
8. **Testing before publish** — Mobile responsive, forms work, loaders load, schema valid

---

## Recent Fixes (2026-07-23)

**Issue:** Metadata SVG icons rendering as black circles/blocks instead of proper clock/document/calendar icons

**Root cause:** Missing `.blog-meta-item svg` CSS rule in 4 of 5 blogs

**Solution:** Added SVG styling rule to standardized CSS (see Layout Structure, Hero Section)

**Affected blogs fixed:**
- self-employed-home-loan.html
- low-doc-home-loans.html
- home-loans-doctors.html
- house-land-packages-melbourne.html

**Prevention:** This CSS rule is now required in the FINALIZED TEMPLATE SPECIFICATION. Include it in every new blog post.
