---
name: using-frontend-noslop
description: Use when designing, building, reviewing, or styling any frontend UI, web app, landing page, dashboard, or component. Enforces studio-grade industrial design discipline, automated anti-slop linting, zero stupid gradients, active domain inspiration, and production code recipes.
user-invocable: true
license: MIT
metadata:
  version: "5.0.0"
  type: "meta-orchestrator"
  integrated_skills:
    - impeccable
    - frontend-design
    - design-taste-frontend
    - frontend-design-deslop
    - antislop-ui
    - no-ai-slop
    - pick-ui-library
    - react-best-practices
---

# using-frontend-noslop (v5.0: The Complete Domain-Tailored Studio Engine)

The authoritative, production-grade frontend engineering and design engine for AI coding agents. It enforces **bespoke, domain-tailored visual DNA for every industry** (Fitness, E-Commerce, Fintech, DevTools, Medical, Real Estate, Food, Education) while completely eliminating generic AI templates, stupid gradients, clown-car colors, asymmetrical side-borders, and layout shifts.

---

## 🧭 The 5-Phase Production Pipeline

Every interface task must execute this strict 5-phase pipeline:

```
[ Phase 0: Domain DNA Lockdown ]    → Detect industry vertical and apply exact colors, fonts & components.
                 ↓
[ Phase 1: Palette & Typography ]   → 90/10 Neutral rule. Exactly ONE domain accent. ZERO gradient text.
                 ↓
[ Phase 2: Architectural Recipes ]  → Asymmetrical Bento, Metric Hero, or Drawer Cart (NO generic 3-card grid).
                 ↓
[ Phase 3: 5-State Production Code] → Shimmer Skeletons (CLS=0), Empty, Error+Retry, Disabled, Populated.
                 ↓
[ Phase 4: Automated Craft Audit ]  → Run scripts/audit-noslop.py + 50-Point Craft Floor (Score >= 45/50).
```

---

## 🏛️ Phase 0: Mandatory Domain DNA Lockdown

When tasked with building for ANY domain, you MUST NOT guess or default to generic SaaS cards. You MUST load and enforce the exact **Domain DNA Blueprint** from `references/domain-design-playbooks.md`:

| Industry / Domain | Premier Benchmarks | Exact Palette Formula | Typography Stack | Mandatory Signature Components | Domain Skeleton Spec |
|---|---|---|---|---|---|
| **Fitness / Athletics** | WHOOP, Nike Training, Gymshark | Carbon `#08090A` + Laser Volt `#CCFF00` or Infrared `#FF2A2A` | Condensed Grotesque (`font-black uppercase`) + Mono data | Biometric Telemetry HUD, Workout routine timeline, 7-day volume heatmap | Circular gauge shimmer + tabular metric line skeletons |
| **High-End E-Commerce** | SSENSE, Apple Store, Arc'teryx, Aesop | Warm Bone `#F7F7F5` or Velvet Black + Carbon `#111111` | High-fashion Serif or Neo-Grotesque (`Geist`) + micro-labels | Slide-over drawer cart (`vaul`), Aspect-locked gallery (`aspect-[3/4]`), Tactile size pills | Aspect-locked photo card skeleton + price/title skeletons |
| **Fintech & Banking** | Stripe, Wise, Mercury, Ramp | Vault Obsidian `#08090C` or Bank White + Cobalt `#2563EB` | Swiss Grotesque (`Inter`) with strict `tabular-nums` | Dual-currency live converter card, Virtual debit card visualizer, Virtualized ledger | Fixed-width tabular row skeletons with status pills |
| **Developer Tools** | Linear, Vercel, Supabase, Raycast | Deep Space Obsidian `#08090B` + Monochrome White | Monospace font (`Geist Mono`, `JetBrains Mono`) | Interactive CLI snippet with copy feedback, `CMDK` (⌘K) search palette | Monospaced code line skeletons with varying widths |
| **Healthcare & Medical** | Oscar Health, One Medical, Mayo Clinic | Sterile White `#FAFBFC` + Medical Sapphire `#0284C7` | Humanist Sans (`Plus Jakarta Sans`) for maximum trust | Appointment slot stepper with doctor photo, HIPAA security badge | Doctor avatar circle skeleton + specialty pill |
| **Real Estate & Architecture**| The Agency, Sotheby's, AD | Travertine `#F5F2EB` or Marble `#0D0D0E` + Bronze `#92400E` | Architectural Sans (`Cabinet Grotesk`) or Serif | Interactive SVG floorplan viewer, Widescreen photo slider (`aspect-[16/10]`) | Widescreen photo skeleton (`aspect-[16/10]`) |
| **Food & Culinary Arts** | Blue Bottle Coffee, Noma, Toast POS | Warm Oat Milk `#F5F2EB` + Roasted Espresso + Terracotta `#C85A32` | Expressive Culinary Serif (`Fraunces`) + clean body | Flavor notes radar, 1-click dietary filter pills, Table reservation wheel | Menu item row skeleton with price & description |
| **Education & E-Learning** | MasterClass, Brilliant, Khan Academy | Campus Cream `#FDFCF7` or Study Navy + Amber `#D97706` | High-focus reading sans (`Inter`, `Public Sans`) | Curriculum syllabus tree accordion, Daily progress streak, Quiz check card | Expandable syllabus module tree skeleton |

*(Consult `references/domain-design-playbooks.md` for full implementation details, copy tones, and forbidden words).*

---

## ⛔ Absolute Invariants: The Zero-Tolerance Ban Floor

Any presence of these patterns triggers an immediate automatic rejection:

1. ❌ **NO Gradient Text (`bg-clip-text text-transparent`)**: Headings MUST be solid high-contrast typography (`#EDEDED` / `#FFFFFF` on dark; `#111111` on light).
2. ❌ **NO Multi-Color Gradients (`from-purple via-pink to-cyan`)**: Multi-hue gradients are strictly banned. Solid surfaces or subtle monochromatic shifts only.
3. ❌ **NO Ambient Blur Blobs (`blur-3xl bg-purple-500/20`)**: Build tangible layout surfaces and 1px border contrast instead of lazy background glowing circles.
4. ❌ **NO Neon Glowing Drop-Shadows (`shadow-indigo-500/50`)**: Depth is created with physical 1px border subtleties (`border-white/[0.08]`) and surface elevation.
5. ❌ **NO Candy/Rainbow Badges**: Badges must use calm neutral tokens (`bg-white/[0.04] text-neutral-300 border-white/[0.08]`).
6. ❌ **NO Generic 3-Card Clichés**: A centered title followed by 3 identical cards with icons in pastel squares is forbidden. Use asymmetrical hierarchy (Bento, live preview, data rail).
7. ❌ **NO Non-Semantic Clickable Divs**: Use `<button type="button">` with visible focus rings (`focus-visible:ring-2`).
8. ❌ **NO Asymmetrical Colored Side-Borders ("Sidebg" Cliché)**: Never use `border-l-4` or `border-r-4` with colored borders as an accent stick. Cards MUST have unified, symmetrical 360° perimeter borders (`border border-white/[0.08]`). Use an inline status dot/pill for indicators.
9. ❌ **NO Blocking Spinners in Place of Skeletons**: Never drop an isolated spinner on an empty screen. Content loading MUST implement dimension-matched **Shimmer Skeletons** (`references/code-recipes.md#4`) that reserve exact layout space (zero CLS).

---

## 🎨 The Iron Rule of Color: 90/10 & The Single Accent

* **90%+ Neutral Canvas**: 90% or more of all screen pixels MUST consist of calm, neutral surfaces (Obsidian `#08090C`, Carbon `#0A0A0C`, Graphite, Slate-gray, or Warm Bone `#F7F7F5`).
* **The Rule of One**: Pick **EXACTLY ONE** accent hue for the entire interface (matched to the domain). Never mix competing chromatic accents.

---

## 📦 Production Code Recipes & 5-State Architecture

Every component MUST implement all five states:
1. **Initial / Empty**: Clear, helpful prompt (no dead blank space).
2. **Loading**: Dimension-matched **Shimmer Skeleton** with zero Cumulative Layout Shift (CLS = 0).
3. **Populated**: Real, human data layout.
4. **Error Boundary**: Specific error message with actionable retry button.
5. **Disabled / Pending**: Opacity feedback with explicit pending state (`aria-busy`).

*(See `references/code-recipes.md` for copy-pasteable React 19 / Next.js 15 implementations of Data Containers, Metric Heroes, Asymmetrical Bentos, Shimmer Skeletons, and Symmetrical Status Cards).*

---

## 🧪 Automated Craft Audit & 50-Point Quality Gate

Before completing any frontend task, verify your code against:
1. **Automated Linter:** Run `python scripts/audit-noslop.py <path-to-file>` to automatically catch gradient text, blur blobs, sidebg stripes, and missing accessibility.
2. **50-Point Self-Critique Score:**
   - Chromatic Discipline (10 pts)
   - Domain Realism & Layout Anatomy (10 pts)
   - 5-State Architecture (10 pts)
   - Semantic Accessibility & WCAG 2.1 AA (10 pts)
   - Human Voice & Copy Precision (10 pts)
   **Threshold: Minimum 45/50 points required for delivery.**

---

## ⚡ Direct Invocations

- `/using-frontend-noslop` — Execute the full studio-grade anti-slop pipeline.
- `/frontend-design` — Formulate domain-specific aesthetic stance.
- `/antislop-ui` — Reference specific UI component tokens.
- `/no-ai-slop` — Sanitize text and microcopy from robotic clichés.
- `/react-best-practices` — Enforce Server Components and performance patterns.
