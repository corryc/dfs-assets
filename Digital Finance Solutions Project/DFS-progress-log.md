# DFS Progress Log

---

## 2026-06-23 — First Supporting Blog Live

### What was built
- **Supporting blog template** — reusable HTML file for 1 blog/day
  - File: `posts/2026-06-23-supporting-blog-template.html`
  - Live example: "Can Doctors Get a Home Loan With No LMI?"
  - Structure: 4 sections + internal link block + CTA
  - Every swappable element marked with `<!-- TEMPLATE: ... -->` comments
  - Author removed — shows "Digital Finance Solutions"

### Compliance
- Ran ASIC RG 234 compliance check via `/dfs-ad-compliance`
- Fixes applied: qualified LMI savings claim, qualified deposit % claim, closing CTA softened
- Credit rep line confirmed in footer

### Published
- URL: `https://www.digitalfinancesolutions.com.au/can-doctors-get-home-loan-no-lmi`
- Supports landing page: `/no-lmi-home-loan-doctors-melbourne`
- Published: 2026-06-23

### Process documented
- `DFS-blog-publishing-process.md` — full step-by-step for daily blog production

---

## 2026-06-26 — Three Blog Posts Live

### Published today
- **Dentists No-LMI** — https://www.digitalfinancesolutions.com.au/dentists-no-lmi-home-loan
- **Doctor Borrowing Capacity** — https://www.digitalfinancesolutions.com.au/how-much-can-doctor-borrow-home-loan
- **Trust Blog Rewrite** — https://www.digitalfinancesolutions.com.au/buying-property-through-a-trust

All three confirmed live 2026-06-26.

---

## 2026-06-26 — Trust Blog Rewrite Live

### What was built
- Full rewrite of `/blog/buying-property-through-a-trust` using `/frontend-design` skill approach
- File: `posts/blog/live/2026-06-26-buying-property-through-a-trust-v2.html`
- Lean CSS architecture — short class names, no GSAP, CSS-only. File size: **30.2kb** (well under 50k Webflow limit)
- New content: 2026 Federal Budget changes incorporated — proposed 30% min tax on discretionary trusts, negative gearing quarantine, CGT indexation replacement
- Schema: Article + FAQPage (4 Q&As) + BreadcrumbList — all mandatory as of this session
- Components added: `.warn` (amber budget warning box), `.pc` pros/cons grid, sidebar budget update card

### Design standard change
- **GSAP removed from all future DFS blog HTML** — caused 52.9kb bloat on original trust file, exceeding Webflow 50k limit
- `/frontend-design` skill approach adopted as standard going forward
- Canonical template: `posts/blog/live/2026-06-26-buying-property-through-a-trust-v2.html`

### Published
- URL: https://www.digitalfinancesolutions.com.au/buying-property-through-a-trust
- Published: 2026-06-26

### Tomorrow (2026-06-24)
- Batch create next week's supporting blog posts
- Use template + same compliance + publish process
- Source topics from `2026-06-23-weekly-content-calendar.md`
