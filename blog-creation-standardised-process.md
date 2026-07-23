# DFS Blog Page Creation Process (Standardised)

**Status:** Established 2026-07-11
**Last Updated:** 2026-07-23 (SVG icon styling fix added)
**Purpose:** Ensure all new blog pages meet DFS quality, compliance, and design standards

⚠️ **CRITICAL UPDATE (2026-07-23):** Metadata SVG icons require explicit CSS styling. See Verification checklist below.

---

## Pre-Creation Phase

### 1. Content Brief
- Define target keywords (research via Semrush)
- Identify landing page it supports
- Confirm keyword volume, difficulty, search intent
- Note Semrush date for records

### 2. Design Direction (Frontend-Design Thinking)
Before coding, commit to ONE aesthetic direction:
- **Tone options:** refined/luxury, editorial/magazine, progressive, organic, brutalist, playful, minimal
- **Typography:** Pick distinctive display + body font pair (NOT generic Manrope-only)
- **Color strategy:** Dominant color + sharp accents (DFS palette: navy, blue, teal)
- **Spatial composition:** Will you use asymmetry, grid-breaking, diagonal flow, generous negative space?
- **Visual depth:** Gradients, layered backgrounds, textures, decorative elements?
- **Micro-interactions:** Page load stagger, hover effects, scroll triggers?
- **Differentiation:** What's ONE memorable thing about this page's design?

**Document the vision before coding.**

---

## Build Phase

### 3. HTML Structure (Standardised)

**Required elements in order:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Meta & SEO -->
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Keyword-rich title] | DFS</title>
  <meta name="description" content="[150-160 chars, includes keyword, qualified claims]">
  <link rel="canonical" href="https://digitalfinancesolutions.com.au/[slug]">
  
  <!-- Fonts & External CSS -->
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link href="https://corryc.github.io/dfs-assets/dfs-styles.css" rel="stylesheet">
  
  <!-- NAV LOADER (MANDATORY) -->
  <script src="https://corryc.github.io/dfs-assets/dfs-nav-loader.js"></script>
  
  <!-- Page-specific CSS & JSON-LD -->
  <style>...</style>
  <script type="application/ld+json">...</script>
</head>
<body>

<!-- HERO SECTION -->
<div class="blog-hero">
  <h1>[Main headline]</h1>
  <p>[Subheading/benefit summary]</p>
  <div class="cta-group">
    <button class="btn-primary" onclick="...">Primary CTA</button>
  </div>
</div>

<!-- MAIN CONTENT (blog-body container) -->
<div class="blog-body">
  <!-- Sections with h2, p, ul, li -->
  
  <!-- Tip cards / Grid sections -->
  
  <!-- CTA Bands -->
  
  <!-- Forms (hero form 3-field + full form 6-field) -->
  
  <!-- FAQ Accordion -->
  
  <!-- Compliance note -->
</div>

<!-- FAQ Handler Script -->
<script>
document.querySelectorAll('.faq-q').forEach(q => {
  q.addEventListener('click', () => {
    q.closest('.faq-item').classList.toggle('open');
  });
});
</script>

<!-- FOOTER LOADER (MANDATORY) -->
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

### 6. Forms (Two Required)

**Hero Form (3 fields):**
- Name, Email, Phone (or similar quick capture)

**Full Form (6 fields):**
- Name, Email, Phone, Loan Type (select), Loan Amount, Goal/Challenge
- Include AFSL credit representative number in fine print

### 7. Compliance (Mandatory)

**Language:**
- All benefit claims qualified: "may", "could", "subject to eligibility"
- Never absolute statements (no "guaranteed", "certain", "avoid all LMI")

**Footer compliance note:**
- General advice disclaimer
- Credit Representative Number 532405 of Beagle Pty Ltd (AFSL 391237)

---

## Pre-Publication Checklist

### 8. Verification

- [ ] Nav loader script present in `<head>`
- [ ] Footer loader script present before `</body>` (NOT hardcoded footer)
- [ ] Canonical URL correct (non-www format)
- [ ] Meta description 150-160 chars, includes keyword
- [ ] All forms submit-able (no validation errors)
- [ ] FAQ accordion opens/closes smoothly
- [ ] All CTA buttons link to correct targets
- [ ] Schema markup valid (use Google's structured data tester)
- [ ] Compliance disclaimers present
- [ ] AFSL number on form visible
- [ ] **Metadata SVG icons render correctly** (clock, document, calendar — NOT black circles)
  - MUST include CSS rule: `.blog-meta-item svg { width: 15px; height: 15px; stroke: rgba(255,255,255,0.4); fill: none; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; flex-shrink: 0; }`
- [ ] Mobile responsive (test at 375px, 768px, 1280px)

### 9. Frontend-Design QA

- [ ] Typography hierarchy visually clear (h1 > h2 > p)
- [ ] Color palette cohesive (dominant + accent colors used consistently)
- [ ] Hover effects smooth and memorable (cards lift, buttons glow, arrow rotates)
- [ ] Spacing generous and intentional (no cramped sections)
- [ ] Visual depth present (gradients, shadows, layered elements)
- [ ] Design feels intentional, not generic

### 10. Compliance Audit

Run `/dfs-ad-compliance` (if available) or manual check:
- All benefit claims qualified
- No banned phrases
- Contact phone correct: 0419 891 983
- AFSL line exact: "Credit Representative Number 532405 of Beagle Pty Ltd (Australian Credit Licence No. 391237)"
- General advice disclaimer included

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

## Key Rules (Non-negotiable)

1. **No hardcoded nav/footer.** Always use loaders (dfs-nav-loader.js + dfs-footer-loader.js)
2. **Canonical URLs non-www.** All canonicals: `https://digitalfinancesolutions.com.au/[slug]` (no www)
3. **Compliance first.** Qualified language, AFSL visible, disclaimer present
4. **Frontend-design always.** Distinctive aesthetic direction, not generic
5. **Schema required.** Article + FAQPage + BreadcrumbList on every post
6. **Two forms minimum.** Hero form (3-field) + Full form (6-field)
7. **SVG metadata icon styling required.** Hero metadata icons MUST have `.blog-meta-item svg` CSS rule (see Verification checklist)
8. **Testing before publish.** Mobile responsive, forms work, loaders load, schema valid

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
