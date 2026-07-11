---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality
type: skill
---

# Frontend-Design Skill Guide

Use `/frontend-design` when building web components, pages, or applications that need exceptional design quality and avoid generic "AI slop" aesthetics.

---

## Design Thinking Framework

Before coding, understand the context and commit to a **BOLD aesthetic direction**:

### 1. Purpose & Audience
- **What problem does this interface solve?**
- **Who uses it?**
- **What's the context?**

### 2. Aesthetic Direction (Pick ONE)
Choose an extreme — don't blend:
- **Brutally minimal** — restraint, precision, subtle details
- **Maximalist chaos** — elaborate code, extensive animations, layered complexity
- **Retro-futuristic** — nostalgic + modern blend
- **Organic/natural** — flowing, soft, nature-inspired
- **Luxury/refined** — elegant, sophisticated, premium feel
- **Playful/toy-like** — fun, whimsical, delightful
- **Editorial/magazine** — strong hierarchy, authoritative
- **Brutalist/raw** — bold typography, high contrast, minimal ornamentation
- **Art deco/geometric** — geometric shapes, symmetric or rhythmic patterns
- **Soft/pastel** — gentle colors, smooth transitions
- **Industrial/utilitarian** — functional, raw materials, technical feel

**CRITICAL:** Choose a clear direction and execute it with precision. Bold maximalism and refined minimalism both work — the key is **intentionality, not intensity**.

### 3. Differentiation
**What makes this UNFORGETTABLE?** What's the ONE thing someone will remember about this design?

---

## Frontend Aesthetics Guidelines

### Typography
- **Avoid:** Arial, Inter, Roboto, system fonts (generic, dated)
- **Choose:** Distinctive, beautiful, unique fonts that elevate the design
- **Pair:** Display font (memorable) + Body font (readable)
- **Never converge:** Don't use Space Grotesk everywhere; vary your choices

### Color & Theme
- **Commit:** Choose a cohesive aesthetic, don't mix conflicting palettes
- **Use CSS variables:** Consistency across the design
- **Dominant + accents:** One strong color + sharp accents outperform timid, evenly-distributed palettes
- **Avoid:** Clichéd palettes (especially purple gradients on white)

### Motion & Animations
- **High-impact moments:** One well-orchestrated page load with staggered reveals (animation-delay) > scattered micro-interactions
- **CSS-only for HTML:** Prioritize CSS animations
- **React/Vue:** Use Motion library when available
- **Scroll-triggering:** Engage as user scrolls
- **Hover states:** Surprise and delight

### Spatial Composition
- **Unexpected layouts:** Break conventions
- **Asymmetry:** Not everything needs to be balanced
- **Overlap:** Layers create depth
- **Diagonal flow:** Guide the eye
- **Grid-breaking:** Don't be a slave to the grid
- **Generous negative space OR controlled density:** Pick one direction

### Backgrounds & Visual Details
- **Avoid:** Flat solid colors
- **Create atmosphere:** Depth, texture, context-specific effects
- **Techniques:**
  - Gradient meshes
  - Noise textures
  - Geometric patterns
  - Layered transparencies
  - Dramatic shadows
  - Decorative borders
  - Custom cursors
  - Grain overlays

---

## Implementation Strategy

Match implementation complexity to your aesthetic vision:

### Maximalist Designs
- Elaborate code with extensive animations
- Complex component interactions
- Layered visual effects
- Intricate hover states

### Refined/Minimalist Designs
- Restraint and precision
- Careful attention to spacing
- Subtle, memorable details
- Elegant execution

---

## What NOT to Do

🚫 **Generic AI-Generated Aesthetics:**
- Overused font families (Inter, Roboto, Arial, system fonts)
- Clichéd color schemes (purple gradients on white)
- Predictable layouts and component patterns
- Cookie-cutter design lacking context-specific character
- Same design repeated across projects

🚫 **Lazy Decisions:**
- "It's fine" aesthetics
- No clear visual direction
- Mixing conflicting styles
- Timid color choices

---

## The Core Principle

**Claude is capable of extraordinary creative work. Don't hold back. Show what can truly be created when thinking outside the box and committing fully to a distinctive vision.**

Interpret creatively. Make unexpected choices that feel genuinely designed for YOUR context, not a template. Vary between light and dark themes, different fonts, different aesthetics. Be intentional.

---

## How to Use in DFS Blog Pages

When creating blog pages, combine `/frontend-design` with the standardised blog creation process:

1. **Design Direction Phase** (before coding)
   - Pick aesthetic direction
   - Document the vision
   - Identify differentiation

2. **Frontend-Design Implementation**
   - Use distinctive fonts (not just Manrope)
   - Apply color strategy (dominant + accents)
   - Add spatial innovation (asymmetry, grid-breaking)
   - Implement micro-interactions (staggered reveals, hover effects)
   - Create visual depth (gradients, shadows, layered backgrounds)

3. **Combine with Standardised Process**
   - Standardised loaders (nav + footer)
   - Compliance requirements
   - Schema markup
   - Forms
   - Responsive design

**Result:** Production-grade pages that are distinctive, memorable, and aligned with DFS brand.

---

## Related Documentation

- [[blog-creation-standardised-process]] — Full workflow for DFS blog pages
- [[dfs-seo-performance]] — Design must support SEO goals
