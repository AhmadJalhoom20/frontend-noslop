---
name: using-frontend-noslop
description: Use when designing, building, reviewing, or styling any frontend UI, web app, landing page, dashboard, or component, or when seeking to eliminate generic "AI-slop" aesthetics, stupid gradients, clown-car colors, and cookie-cutter templates through real-world domain inspiration.
user-invocable: true
license: MIT
metadata:
  version: "3.0.0"
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

# using-frontend-noslop (v3.0: Domain Inspiration & Zero-Slop Engine)

An elite orchestration skill that enforces world-class industrial design discipline. It eliminates generic AI aesthetics, stupid gradients, and cookie-cutter templates by **actively extracting visual DNA from premier real-world industry benchmarks** (e.g. Nike/Gymshark for Fitness, SSENSE/Apple for E-Commerce, Stripe/Mercury for Fintech, Linear/Vercel for DevTools).

---

## 🧭 Phase 0: Domain Inspiration Reconnaissance (The Industry Archetype Engine)

Before writing any code or choosing components, identify the project's **industry vertical** and anchor your design to the visual DNA of world-class benchmarks:

### 1. Benchmark Identification Matrix

| Industry / Niche | World-Class Benchmarks | Visual Tone & Mood | Signature Accent & Surfaces | Typography Anchor |
|---|---|---|---|---|
| **Fitness, Gym & Athletics** | WHOOP, Nike Training, Gymshark, Peloton, Strava | Kinetic, high-energy, aggressive, dark-biased | Deep Carbon (`#0A0A0C`) + Laser Volt (`#CCFF00`) or Infrared (`#FF3B30`) | Condensed bold grotesque (`font-black uppercase`) + mono metrics |
| **High-End E-Commerce & Retail** | SSENSE, Apple Store, Arc'teryx, Aesop, Shopify Plus | Restrained, editorial, museum-grade product staging | Warm Bone (`#F7F7F5`) / Pure Black + Single Carbon (`#111111`) or Terracotta | Refined Neo-Grotesque (`Geist`) or high-fashion serif (`Playfair`) |
| **Fintech, Banking & Crypto** | Stripe, Wise, Mercury, Ramp, Cash App | Crystalline precision, cryptographic security, ultra-high trust | Deep Obsidian (`#08090C`) or Bank White + Cobalt (`#2563EB`) or Mint | High-contrast Swiss grid with `tabular-nums` for all figures |
| **Developer Tools & Cloud Infra** | Linear, Vercel, Supabase, Raycast, GitHub | Keyboard-first, high-density, terminal telemetry | Deep Space Obsidian (`#08090B`) + Monochrome White / Cyan focus | Monospace font (`Geist Mono`, `JetBrains Mono`) for commands |
| **Food, Dining & Culinary** | Blue Bottle Coffee, Noma, Sweetgreen, Toast POS | Warm, organic, tactile, appetizing, authentic textures | Warm Oatmeal (`#F5F2EB`) + Roasted Espresso (`#1A1615`) + Terracotta | Warm serif headlines (`Fraunces`) paired with geometric body |
| **Creative Agencies & Portfolios** | Pentagram, ReadCV, Apple Design Awards, Are.na | Bold, confident, unexpected spatial rhythm, scale | Pure Stark Monochrome (`#000000` & `#FFFFFF`) + Single signature tint | Dramatic typographic scale contrast (huge titles vs micro labels) |

*(For full industry breakdown, see `references/domain-design-playbooks.md`).*

### 2. Domain Inspiration Protocol (When Requirements Are Set)
1. **Identify the Benchmarks**: Name 2-3 premier products that dominate that exact vertical.
2. **Search Real References if Needed**: If the niche is unique, query `search_web` or Mobbin (`search_screens` / `search_sections`) to extract real-world navigation rails, card densities, and color schemes.
3. **Build Domain-Specific Signature Components**:
   - For **Fitness**: Build a Biometric Telemetry HUD, workout routine split timeline, and volume heatmaps (NOT generic 3-card pricing).
   - For **E-Commerce**: Build a slide-over drawer cart (`vaul`), multi-angle gallery with fixed aspect ratios (`aspect-[3/4]`), and tactile size pill selectors.
   - For **Fintech**: Build a dual-currency exchange split card, virtual card visualizer, and virtualized transaction ledger.
   - For **DevTools**: Build an interactive CLI snippet with copy feedback, a `CMDK` command palette, and a real-time service latency meter.

---

## ⛔ Absolute Invariants: The Color & Gradient Ban Floor

Before writing any CSS, Tailwind classes, or design tokens, you MUST comply with these 6 non-negotiable negative constraints. Any violation is an immediate code rejection:

| Prohibited Pattern (AI Slop) | Why It Is Banned | Required Replacement |
|---|---|---|
| **Gradient Text (`bg-clip-text text-transparent`)** | The #1 lazy AI cliché. Cheapens typography and ruins readability. | **Solid, high-contrast typography**: `#EDEDED` / `#FFFFFF` on dark; `#111111` on light. |
| **Multi-Color Gradients (`from-purple via-pink to-cyan`)** | Looks like an uncurated 2021 crypto template. Visual noise. | **Zero multi-hue gradients**. Solid surfaces or subtle monochromatic single-step luminance shifts only. |
| **Ambient Blur Blobs (`blur-3xl bg-purple-500/20`)** | Meaningless glowing circles placed to mask empty layouts. | **Deliberate layout geometry**, structural gridlines, subtle borders, or tangible card surfaces. |
| **Neon Colored Drop-Shadows (`shadow-indigo-500/50`)** | Makes interfaces look like arcade games rather than software. | **Physical 1px border contrast** (`border-white/[0.08]` or `border-black/[0.08]`) and subtle micro-shadows. |
| **Candy / Rainbow Badges** | Green, purple, orange, blue pills scattered on the same screen. | **Muted, monochrome tags**: `bg-white/[0.04] text-neutral-300 border-white/[0.08]`. |
| **Generic Dark Slate (`#0f172a` + glowing rounded-2xl cards)** | Median AI training average. Looks dated and uninspired. | **Intentional deep obsidian (`#08090C`), graphite, warm bone, or crisp monochrome**. |

---

## 🎨 The Iron Rule of Color: 90/10 & The Single Accent

1. **The 90/10 Surface-to-Accent Ratio**:
   - **90%+ of all pixels** must consist of calm, neutral surfaces (Black, Graphite, Charcoal, Stone, Slate-gray, or Warm Bone/Paper).
   - **Less than 10%** of pixels may carry an accent hue, reserved **STRICTLY** for primary action affordances (primary button, active navigation indicator, focus ring).

2. **The Single-Hue Rule (Rule of One)**:
   - Pick **ONE single brand/accent hue** for the entire interface (e.g. Pure Electric Cobalt `#2563EB`, or Signal Amber `#F59E0B`, or Precision Emerald `#10B981`, or Monochromatic High-Contrast `#FFFFFF`).
   - **NEVER mix competing chromatic hues** (e.g. do NOT combine purple buttons with cyan cards and yellow badges).

---

## 📐 Pre-Baked Industrial Palettes

Do not invent arbitrary hex colors. Use one of these three calibrated palettes:

### Palette 1: The Obsidian Monolith (Linear / Vercel Dark Standard)
*Best for: Developer tools, SaaS platforms, high-performance dashboards, modern web apps.*
```css
/* Background & Surfaces */
--bg-canvas: #08090C;        /* Deep obsidian void, NOT washed-out navy */
--bg-surface: #101216;       /* Clean matte surface */
--bg-elevated: #161920;      /* Elevated dialog / dropdown */
--bg-muted: rgba(255, 255, 255, 0.04);

/* Borders (Physical depth over glowing shadows) */
--border-subtle: rgba(255, 255, 255, 0.07);
--border-strong: rgba(255, 255, 255, 0.14);

/* Typography (High optical contrast) */
--text-primary: #EDEDED;     /* Crisp white with zero harsh glare */
--text-secondary: #94969E;   /* Readable neutral secondary */
--text-muted: #5E616B;       /* Calm tertiary */

/* Single Accent (Choose EXACTLY ONE) */
--accent-primary: #FFFFFF;   /* High-contrast Monochrome (Preferred) */
/* OR: --accent-primary: #3B82F6 (Clean Cobalt) */
/* OR: --accent-primary: #10B981 (Precision Emerald) */
```

### Palette 2: The Swiss Editorial (Stripe / Apple Light Standard)
*Best for: Documentation, fintech, publishing, clean marketing, e-commerce.*
```css
/* Background & Surfaces */
--bg-canvas: #FBFBFC;        /* Crisp off-white / bone paper */
--bg-surface: #FFFFFF;       /* Pure white card surface */
--bg-elevated: #FFFFFF;
--bg-muted: #F2F3F5;

/* Borders */
--border-subtle: #E6E8EC;
--border-strong: #D1D5DB;

/* Typography */
--text-primary: #111215;     /* Deep carbon black */
--text-secondary: #5A5E67;
--text-muted: #8B909A;

/* Single Accent */
--accent-primary: #0F172A;   /* Deep Slate/Carbon (Sophisticated) */
/* OR: --accent-primary: #2563EB (Industrial Blue) */
```

### Palette 3: The Industrial Titanium (Deep Matte Technical)
*Best for: High-density data apps, analytics, terminals, developer tools.*
```css
--bg-canvas: #0C0D0E;
--bg-surface: #151719;
--bg-elevated: #1E2023;
--border-subtle: #24272B;
--border-strong: #363A40;
--text-primary: #F0F2F5;
--text-secondary: #888E96;
--accent-primary: #38BDF8;   /* Precision Cyan strictly for active state */
```

---

## 🏛️ Layout Discipline: Anti-Slop Architecture

1. **Ban on the Cliché 3-Card Feature Grid**:
   - Never output a centered headline followed by 3 identical rounded cards, each containing a Lucide icon in a pastel square and two lines of filler text.
   - **Fix**: Use asymmetrical hierarchy matched to the domain (Bento grid, interactive telemetry, live code preview, or multi-angle product rail).

2. **Typography Scaling & Spacing Rhythm**:
   - Use a mathematical 8px spacing grid: `gap-2` (8px), `gap-4` (16px), `gap-6` (24px), `gap-8` (32px).
   - Line height tracking: Tighten titles (`tracking-tight leading-tight`), loosen body text (`leading-relaxed`).

3. **Complete 5-State Component Contract**:
   Every component MUST implement all five states without exception:
   - **Initial / Empty**: Clear, helpful prompt (no dead blank space).
   - **Loading**: Dimension-matched skeleton with zero Cumulative Layout Shift (CLS = 0).
   - **Populated**: Real, human data layout.
   - **Error Boundary**: Specific error message with actionable retry button.
   - **Disabled / Pending**: Opacity feedback with explicit pending state (`aria-busy`).

---

## 🛠️ Complete Orchestration Workflow

```
[ Phase 0: Domain Reconnaissance ] → Identify vertical benchmarks (Fitness, E-Commerce, Fintech, etc.)
                ↓
[ Phase 1: Visual DNA & Palette ]  → Enforce 90/10 neutral rule + single accent hue + zero gradient text.
                ↓
[ Phase 2: Domain Components ]     → Build signature domain components (HUD, Slide-over cart, Ledger, CLI).
                ↓
[ Phase 3: Accessible Engineering] → Radix/Base UI primitives + Strict TypeScript + 5 UI states.
                ↓
[ Phase 4: Anti-Slop Verification] → Verify against the Pre-Delivery Checklist below.
```

---

## ✅ The Anti-Slop Pre-Delivery Checklist

Before marking any UI code complete, check off every single item:

- [ ] **Domain Benchmark Grounding**: Interface clearly resembles industry leaders (e.g. WHOOP/Nike for fitness, SSENSE/Apple for retail), NOT generic SaaS templates.
- [ ] **Signature Domain Components**: Built custom components specific to the niche (e.g. telemetry HUD, slide-over cart), not 3 generic cards.
- [ ] **No Gradient Text**: All titles and headlines use solid typography.
- [ ] **No Multi-Color Gradients**: No purple-to-cyan or pink-to-yellow color transitions.
- [ ] **No Neon Glow Blobs**: No background `blur-3xl` colored circles.
- [ ] **Single Accent Color**: Exactly one primary accent hue used across the entire page.
- [ ] **Subtle 1px Borders**: Depth created via borders and elevation, NOT colored box-shadows.
- [ ] **Real Copy (No Marketing Slop)**: Zero buzzwords (*"seamless"*, *"unlock"*, *"next-gen"*).
- [ ] **Zero Layout Shift (CLS = 0)**: Skeletons match exact final populated dimensions.
- [ ] **WCAG 2.1 AA Compliance**: All text passes 4.5:1 contrast against its background.
- [ ] **Keyboard Accessible**: Visible focus rings on all interactive elements (`focus-visible:ring-2`).

---

## ⚡ Direct Invocations

- `/using-frontend-noslop` — Run the full Domain Inspiration & Anti-Slop engine.
- `/frontend-design` — Formulate domain-specific aesthetic direction.
- `/frontend-design-deslop` — Strip median templates and enforce 90/10 palettes.
- `/antislop-ui` — Reference specific UI component tokens.
- `/no-ai-slop` — Sanitize text and microcopy from robotic clichés.
- `/react-best-practices` — Enforce Server Components and performance patterns.
