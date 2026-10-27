---
name: using-frontend-noslop
description: Use when designing, building, reviewing, or styling any frontend UI, web app, landing page, dashboard, or component. Enforces studio-grade industrial design discipline, automated anti-slop linting, zero stupid gradients, active domain inspiration, and production code recipes.
user-invocable: true
license: MIT
metadata:
  version: "4.0.0"
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

# using-frontend-noslop (v4.0: Production-Grade Studio Engine)

The authoritative, production-grade frontend engineering and design engine for AI coding agents. It eliminates median AI defaults, stupid gradients, clown-car colors, and cookie-cutter templates through **active real-world domain benchmarking**, **battle-tested code recipes**, **automated craft linting**, and an **uncompromising 50-point quality floor**.

---

## 🧭 The 5-Phase Production Pipeline

Every interface task must progress through this strict 5-phase pipeline:

```
[ Phase 0: Domain Reconnaissance ]  → Extract visual DNA from industry leaders (Nike, Apple, Stripe, Linear).
                 ↓
[ Phase 1: Palette & Typography ]   → 90/10 Neutral rule. Exactly ONE accent. ZERO gradient text.
                 ↓
[ Phase 2: Architectural Recipes ]  → Asymmetrical Bento, Metric Hero, or Drawer Cart (NO generic 3-card grid).
                 ↓
[ Phase 3: 5-State Production Code] → Loading (CLS=0), Empty, Error+Retry, Disabled, Populated.
                 ↓
[ Phase 4: Automated Craft Audit ]  → Run scripts/audit-noslop.py + 50-Point Craft Floor (Score >= 45/50).
```

---

## 🏛️ Phase 0: Domain Reconnaissance & Real-World Benchmarking

When given a niche, do NOT invent layout concepts. Anchor directly to premier industry benchmarks:

| Vertical | Premier World Benchmarks | Visual Tone & Mood | Accent & Surfaces | Typography Anchor | Signature Components |
|---|---|---|---|---|---|
| **Fitness / Athletics** | WHOOP, Nike Training, Gymshark, Strava | Kinetic, high-energy, dark-biased | Deep Carbon (`#0A0A0C`) + Laser Volt (`#CCFF00`) | Condensed Grotesque (`font-black`) + Mono data | Biometric Telemetry HUD, Workout routine timeline, Volume heatmaps |
| **High-End E-Commerce** | SSENSE, Apple Store, Arc'teryx, Aesop | Restrained, editorial, museum-quality | Warm Bone (`#F7F7F5`) / Pure Black + Charcoal | High-fashion Serif or Neo-Grotesque (`Geist`) | Slide-over drawer cart (`vaul`), Multi-angle aspect-locked gallery (`aspect-[3/4]`) |
| **Fintech & Banking** | Stripe, Wise, Mercury, Ramp | Crystalline precision, cryptographic security | Deep Obsidian (`#08090C`) + Industrial Cobalt (`#2563EB`) | Swiss grid with `tabular-nums` for all values | Dual-currency split card, Virtualized ledger, Interactive card visualizer |
| **Developer Tools** | Linear, Vercel, Supabase, Raycast | High-density, keyboard-first telemetry | Deep Space Obsidian (`#08090B`) + Monochrome White | Monospace font (`Geist Mono`, `Consolas`) | Interactive CLI snippet with copy feedback, `CMDK` (⌘K) palette |
| **Food & Culinary** | Blue Bottle Coffee, Noma, Toast POS | Warm, organic, tactile, authentic | Warm Oatmeal (`#F5F2EB`) + Roasted Espresso (`#1A1615`) | Warm serif headlines (`Fraunces`) + Clean body | Origin flavor notes meter, Single-click dietary pills, Table reservation wheel |

*(For comprehensive industry blueprints, consult `references/domain-design-playbooks.md`).*

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

---

## 🎨 The Iron Rule of Color: 90/10 & The Single Accent

* **90%+ Neutral Canvas**: 90% or more of all screen pixels MUST consist of calm, neutral surfaces (Obsidian `#08090C`, Carbon `#0A0A0C`, Graphite, Slate-gray, or Warm Bone `#F7F7F5`).
* **The Rule of One**: Pick **EXACTLY ONE** accent hue for the entire interface (e.g. Pure White `#FFFFFF`, Industrial Cobalt `#2563EB`, Laser Volt `#CCFF00`, or Precision Emerald `#10B981`). Never mix competing chromatic accents.

### Pre-Baked Calibrated Palettes:
* **Obsidian Monolith (Linear/Vercel Dark):** Canvas `#08090C`, Surface `#101216`, Elevated `#161920`, Border `rgba(255,255,255,0.08)`, Text Primary `#EDEDED`.
* **Swiss Editorial (Stripe/Apple Light):** Canvas `#FBFBFC`, Surface `#FFFFFF`, Border `#E6E8EC`, Text Primary `#111215`.
* **Industrial Titanium (High-Density Dark):** Canvas `#0C0D0E`, Surface `#151719`, Border `#24272B`, Text Primary `#F0F2F5`.

---

## 📦 Production Code Recipes & 5-State Architecture

Every component MUST implement all five states:
1. **Initial / Empty**: Clear, helpful prompt (no dead blank space).
2. **Loading**: Dimension-matched skeleton with zero Cumulative Layout Shift (CLS = 0).
3. **Populated**: Real, human data layout.
4. **Error Boundary**: Specific error message with actionable retry button.
5. **Disabled / Pending**: Opacity feedback with explicit pending state (`aria-busy`).

*(See `references/code-recipes.md` for copy-pasteable React 19 / Next.js 15 implementations of Data Containers, Metric Heroes, and Asymmetrical Bentos).*

---

## 🧪 Automated Craft Audit & 50-Point Quality Gate

Before completing any frontend task, verify your code against:
1. **Automated Linter:** Run `python scripts/audit-noslop.py <path-to-file>` to automatically catch gradient text, blur blobs, and missing accessibility.
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
