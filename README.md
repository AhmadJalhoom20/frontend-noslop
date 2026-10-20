# frontend-noslop

A production-grade design and engineering skill pack for AI coding agents. Enforces intentional visual direction, curated component libraries, OKLCH color science, and strict verification gates to eliminate generic AI-generated interfaces.

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg?style=flat-square)](LICENSE)
[![Skills.sh](https://img.shields.io/badge/skills.sh-certified-black?style=flat-square)](https://skills.sh)
[![Compatible with Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-black?style=flat-square)](https://anthropic.com)
[![Compatible with Antigravity](https://img.shields.io/badge/Antigravity-Native-black?style=flat-square)](https://github.com)

---

## The Problem: Median AI UI

Language models sample the statistical average of web code in their training datasets. Without explicit constraints, agents default to predictable clichés:

- Indiscriminate dark mode with purple-to-cyan linear gradients and radial blur orbs.
- Identical 3-column feature cards with pastel-backed icons.
- Placeholder marketing copy stuffed with empty buzzwords (*"seamlessly streamline next-gen workflows"*).
- Gratuitous magic sparkle icons on primary action buttons.
- Fragile code: root-level `"use client"`, layout jumps (CLS), and missing loading or error states.

`frontend-noslop` operates as an orchestration layer over the agent's workflow, enforcing the standards of senior design-engineers before any code is generated or delivered.

---

## Unified Architecture

`frontend-noslop` integrates eight established frontend and craft skills into a unified pipeline:

| Skill | Author / Source | Role in Pipeline |
|---|---|---|
| `impeccable` | Paul Bakaus | Craft floor enforcement and automated review commands (`/critique`, `/polish`, `/audit`). |
| `frontend-design` | Anthropic | Mandates an explicit aesthetic direction before generating markup. |
| `design-taste-frontend` | Leonxlnx | Optical balance, whitespace calibration, and typography scales. |
| `frontend-design-deslop` | Samber | Eliminates median Tailwind presets, establishes OKLCH tokens and `DESIGN.md`. |
| `antislop-ui` | Miqdad Badjuber | Concrete visual rules banning cliché treatments and template cards. |
| `no-ai-slop` | Peter Yang | Edits UX copy and headings to remove AI jargon and throat-clearing openers. |
| `pick-ui-library` | Emil Kowalski | Curated selection of unstyled, accessible component primitives. |
| `react-best-practices` | Vercel Engineering | Server Components architecture, streaming boundaries, and performance patterns. |

---

## Five-Phase Workflow

Every interface task passes through five sequential stages:

```
[ Phase 1: Aesthetic Stance ]  → Define domain-specific visual direction (frontend-design)
             ↓
[ Phase 2: Design Tokens ]     → Establish OKLCH color palette and modular type scale (antislop-ui)
             ↓
[ Phase 3: Library Selection ] → Pick accessible, unstyled primitives (pick-ui-library)
             ↓
[ Phase 4: Implementation ]    → Enforce Server Components and all 5 component states (react-best-practices)
             ↓
[ Phase 5: Verification Gate ] → Run craft audit and remove copy slop (impeccable + no-ai-slop)
```

---

## Installation

### Skills CLI (Universal)
Installs into Claude Code, Cursor, Copilot, Antigravity, Cline, and Codex:

```bash
npx skills add AhmadJalhoom20/frontend-noslop -g -y
```

### Google Antigravity / Gemini CLI
Clone directly into your global config directory:

```bash
git clone https://github.com/AhmadJalhoom20/frontend-noslop.git ~/.gemini/config/plugins/frontend-noslop
```

### Claude Code Marketplace
```bash
/plugin marketplace add AhmadJalhoom20/frontend-noslop
/plugin install frontend-noslop
```

---

## Direct Comparison

| Aspect | Default AI Output | With `frontend-noslop` |
|---|---|---|
| **Palette** | `bg-gradient-to-r from-purple-500 to-indigo-600` | Curated OKLCH palette with WCAG 2.1 AA contrast compliance. |
| **Structure** | Centered heading + 3 identical cards | Asymmetrical layouts, contextual demos, dense data tables. |
| **Typography** | Default sans-serif with arbitrary pixel sizes | Calibrated modular scale with tight headline tracking and proportional leading. |
| **Copy** | *"Empower teams with cutting-edge synergy"* | Direct, factual descriptions of functionality and metrics. |
| **State Handling** | Blank screen while fetching, sudden layout shift | Layout-reserved skeletons for loading, plus explicit empty and error states. |
| **Components** | Unsemantic `div` tags with `onClick` | Semantic HTML with accessible primitives (Radix UI / Base UI). |

---

## Recommended Component Stack

Based on Emil Kowalski's curated recommendations for interactive web applications:

- **Primitives & Accessibility:** Radix UI (`@radix-ui/*`) or Base UI (`@base-ui-components/react`)
- **Toasts:** Sonner (`sonner`)
- **Drawers & Bottom Sheets:** Vaul (`vaul`)
- **Command Menu:** CMDK (`cmdk`)
- **Motion:** Motion / Framer Motion (`motion`)
- **Virtualization:** React Virtuoso (`react-virtuoso`)

---

## Verification Checklist

Before code is approved, all five criteria must be satisfied:

1. **Color Purpose:** No unmotivated purple or cyan gradients. Color choices must serve optical hierarchy.
2. **State Coverage:** All five states implemented: Empty, Loading, Populated, Error with retry, and Disabled.
3. **Accessibility:** Navigable via keyboard (`Tab`), visible focus rings, valid ARIA labels.
4. **Responsive Layout:** Tested from 360px mobile viewport up to widescreen displays without horizontal overflow.
5. **Copy Precision:** Zero marketing clichés (*"seamless"*, *"elevate"*, *"unlock"*, *"next-gen"*).

---

## References

Detailed guides included in this repository:

- [`references/slop-hall-of-shame.md`](references/slop-hall-of-shame.md) — Catalog of common AI design clichés and their structural fixes.
- [`references/craft-floor.md`](references/craft-floor.md) — Specifications for typography, OKLCH color, and component states.
- [`references/curated-libraries.md`](references/curated-libraries.md) — Rationale for selected frontend dependencies.
- [`references/delivery-gate.md`](references/delivery-gate.md) — Step-by-step audit procedure prior to merging code.

---

## Contributing

Pull requests and issue reports are welcome. When proposing changes to anti-slop rules, include concrete before-and-after code examples demonstrating the failure pattern and its resolution.

## License

MIT © [Ahmad Jalhoom](https://github.com/AhmadJalhoom20)
