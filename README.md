# frontend-noslop

A production-grade design and engineering skill pack for AI coding agents. Enforces intentional visual direction, curated component libraries, OKLCH color science, and strict verification gates to eliminate generic AI-generated interfaces.

<p align="left">
  <a href="#english">English</a> • <a href="README.ar.md">العربية (Arabic)</a>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg?style=flat-square)](LICENSE)
[![Skills.sh](https://img.shields.io/badge/skills.sh-certified-black?style=flat-square)](https://skills.sh)
[![Compatible with Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-black?style=flat-square)](https://anthropic.com)
[![Compatible with Antigravity](https://img.shields.io/badge/Antigravity-Native-black?style=flat-square)](https://github.com)

```bash
# Install across all agents in one command
npx skills add AhmadJalhoom20/frontend-noslop -g -y
```

---

<a name="english"></a>
## Overview

Language models default to the statistical median of their training data. When asked to generate a UI, they default to predictable tropes:

1. **The Median Palette:** Indiscriminate dark mode paired with unmotivated `from-purple-500 to-cyan-500` gradients.
2. **The 3-Card Template:** Identical 3-column feature grids with pastel-boxed icons.
3. **Empty Jargon:** Generic filler copy (*"Unlock next-generation synergy"*).
4. **Missing States:** Completely omitting loading skeletons, empty states, and error recovery handlers.
5. **Div Soups:** Unsemantic `div` elements with `onClick` handlers, ignoring keyboard accessibility and ARIA semantics.

`frontend-noslop` acts as an orchestrator across the agent's generation cycle. It replaces generic defaults with an enforced design-engineer workflow.

---

## Code Comparison

### Default AI Output (Median Slop)
```tsx
// Typical unconstrained model output
export default function Hero() {
  return (
    <div className="min-h-screen bg-slate-950 text-white flex flex-col items-center justify-center p-8">
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-purple-500/20 blur-3xl rounded-full" />
      <h1 className="text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
        Streamline Your Workflow
      </h1>
      <p className="mt-4 text-slate-400 max-w-md text-center">
        Unlock next-gen efficiency with our cutting-edge AI-powered platform.
      </p>
      <button className="mt-6 px-6 py-3 rounded-xl bg-purple-600 hover:bg-purple-500 transition shadow-lg shadow-purple-500/25">
        Get Started Free ✨
      </button>
    </div>
  );
}
```

### With `frontend-noslop` (Studio-Grade Craft)
```tsx
// Enforced through frontend-noslop: intentional tokens, semantic HTML, accessible states
import { ArrowRight } from "lucide-react";

export default function Hero() {
  return (
    <section className="relative mx-auto max-w-5xl px-6 py-24 sm:py-32">
      <header className="max-w-2xl">
        <p className="font-mono text-xs uppercase tracking-widest text-[var(--color-muted)]">
          Audit & Compliance Infrastructure
        </p>
        <h1 className="mt-4 font-serif text-4xl sm:text-6xl tracking-tight text-[var(--color-foreground)] leading-[1.08]">
          Deterministic ledger verification for high-throughput systems.
        </h1>
        <p className="mt-6 text-base sm:text-lg leading-relaxed text-[var(--color-muted)]">
          Cryptographically verify data pipelines down to the millisecond. Zero runtime overhead, native OpenTelemetry export.
        </p>
      </header>

      <div className="mt-10 flex flex-wrap items-center gap-4">
        <a
          href="/docs"
          className="inline-flex h-11 items-center justify-center rounded-sm bg-[var(--color-primary)] px-5 text-sm font-medium text-[var(--color-primary-contrast)] transition-colors hover:bg-[var(--color-primary-hover)] focus-visible:outline-2 focus-visible:outline-offset-2"
        >
          Read the Architecture Spec
          <ArrowRight className="ml-2 h-4 w-4" aria-hidden="true" />
        </a>
      </div>
    </section>
  );
}
```

---

## Architecture: The 8 Integrated Engines

`frontend-noslop` does not reinvent established methodologies. It fuses eight verified tools into a single execution pipeline:

```
[ Phase 1: Aesthetic Stance ]  → frontend-design + frontend-design-deslop
             ↓
[ Phase 2: Design Tokens ]     → antislop-ui + DESIGN.md (OKLCH, Typography)
             ↓
[ Phase 3: Library Selection ] → pick-ui-library (Curated Primitives)
             ↓
[ Phase 4: Implementation ]    → react-best-practices + 5-State Coverage
             ↓
[ Phase 5: Verification Gate ] → impeccable (/critique, /polish) + no-ai-slop
```

| Engine | Origin | Purpose |
|---|---|---|
| `impeccable` | Paul Bakaus (ex-Google) | Enforces the non-negotiable craft floor and review commands (`/critique`, `/polish`, `/audit`). |
| `frontend-design` | Anthropic | Mandates an explicit aesthetic direction (e.g. Editorial Brutalism, Luxury Minimal) before writing code. |
| `design-taste-frontend` | Leonxlnx | Calibrates typographic scale, optical alignment, and whitespace tension. |
| `frontend-design-deslop` | Samber | Strips median Tailwind presets, establishes OKLCH tokens and `DESIGN.md`. |
| `antislop-ui` | Miqdad Badjuber | Enforces visual rules banning unmotivated purple gradients and generic card grids. |
| `no-ai-slop` | Peter Yang | Edits UX copy, headings, and microcopy to sound human and direct. |
| `pick-ui-library` | Emil Kowalski | Recommends unstyled, production-grade interactive libraries. |
| `react-best-practices` | Vercel Engineering | Enforces React Server Components, zero-CLS skeleton reservation, and streaming patterns. |

---

## Curated Frontend Stack

We enforce Emil Kowalski's curated component toolchain:

- **Primitives & Accessibility:** [Radix UI](https://www.radix-ui.com/) / [Base UI](https://base-ui.com/)
- **Toasts:** [Sonner](https://sonner.emilkowal.ski/)
- **Drawers & Bottom Sheets:** [Vaul](https://vaul.emilkowal.ski/)
- **Command Palette:** [CMDK](https://cmdk.paco.me/)
- **Motion & Physics:** [Motion (Framer)](https://motion.dev/)
- **Virtualization:** [React Virtuoso](https://virtuoso.dev/)

---

## Installation & Setup

### 1. Global Installation (Any Agent Harness)
Installs into Claude Code, Cursor, Copilot, Antigravity, Cline, and Codex:

```bash
npx skills add AhmadJalhoom20/frontend-noslop -g -y
```

### 2. Google Antigravity / Gemini CLI
```bash
git clone https://github.com/AhmadJalhoom20/frontend-noslop.git ~/.gemini/config/plugins/frontend-noslop
```

### 3. Claude Code Marketplace
```bash
/plugin marketplace add AhmadJalhoom20/frontend-noslop
/plugin install frontend-noslop
```

---

## Verification Gate

Before code is marked complete, five conditions must pass:

1. **Palette Purpose:** No unmotivated gradients. All colors derive from semantic design tokens.
2. **State Coverage:** All 5 states implemented (Empty, Loading Skeleton, Populated, Error with retry, Disabled).
3. **Accessibility:** Navigable via keyboard (`Tab`), focus indicators visible, WCAG 2.1 AA contrast verified.
4. **Viewport Integrity:** Fluid layout tested from 360px mobile width up to widescreen monitors.
5. **Copy Precision:** Zero marketing clichés (*"seamless"*, *"elevate"*, *"next-gen"*, *"unlock"*).

---

## Contributing

Contributions, ruleset additions, and issue reports are welcome. When proposing new constraints, provide before-and-after code samples demonstrating the pattern and its resolution.

## License

MIT © [Ahmad Jalhoom](https://github.com/AhmadJalhoom20)
