# DFS Supporting Blog — Daily Publishing Process

## Overview
One supporting blog per day. Each post targets one long-tail keyword and funnels traffic to a landing page via an internal link block. You manually click Publish in Webflow each day.

---

## Step 1 — Generate the Blog HTML

Use `2026-06-23-supporting-blog-template.html` as the base template.
Every swappable element has a `<!-- TEMPLATE: ... -->` comment.

Structure (4 sections, 700–1200 words):
- What is [topic]
- Why [mechanism]
- Who qualifies / what applies
- What to watch out for
- Internal link block → target landing page
- Closing CTA

---

## Step 2 — Compliance Check

Run `/dfs-ad-compliance` on the draft content.

Key watch points (ASIC RG 234):
- No unqualified savings claims (e.g. "save $20,000") — must add "exact amount depends on lender, loan size, and LVR"
- No unqualified deposit claims (e.g. "5% deposit") — must add "subject to lender eligibility"
- Credit rep line must appear: "Digital Finance Solutions is an authorised Credit Representative (532405) of Beagle Finance Pty Ltd (ACL 391237)"
- No "30+ lenders" or similar unverified claims without qualification

Apply all fixes before publishing.

---

## Step 3 — Output Page Settings

Before creating the Webflow page, output these fields ready to paste:

| Field | Value |
|-------|-------|
| **Title** | [Post title — plain, no brand suffix] |
| **Slug** | `kebab-case-slug` |
| **SEO Title** | [Post title] \| Digital Finance Solutions |
| **Meta Description** | 1–2 sentences, 150–160 chars, includes primary keyword |
| **OG Title** | Same as post title |
| **OG Description** | Same as meta description |

---

## Step 4 — Create Webflow Page

1. Webflow Designer → Pages → New Page
2. Paste Title and Slug from Step 3
3. Add an **Embed** element to the page body
4. Open the HTML file → `Ctrl+A` → Copy → Paste into the embed
5. Go to Page Settings → SEO tab → paste SEO Title and Meta Description
6. Set page to **Draft**
7. Save

---

## Step 5 — Publish

Manually click **Publish** in Webflow each morning for the scheduled post.

---

## Slug Convention

- Blog posts: `/can-[topic]-[qualifier]` or descriptive keyword slug
- Landing pages: `/[product]-[location]` (e.g. `/no-lmi-home-loan-doctors-melbourne`)
- Blog slugs must NOT match landing page slugs — they support each other but are separate pages

---

## File Naming

All HTML files saved to:
`Digital Finance Solutions Project/posts/YYYY-MM-DD-post-slug.html`

Template file:
`Digital Finance Solutions Project/posts/2026-06-23-supporting-blog-template.html`

---

## Notes
- Do not use Webflow CMS Blog collection — blogs are standalone static pages with HTML embed
- Designer MCP connector can be used but is unreliable — manual paste is the preferred method
- Author name removed from blog meta — shows "Digital Finance Solutions" instead
