---
name: using-frontend-noslop
description: Use when designing, building, reviewing, or styling any frontend UI, web app, landing page, dashboard, or component, or when seeking to eliminate generic "AI-slop" aesthetics, cookie-cutter templates, and uninspired design defaults.
user-invocable: true
license: MIT
metadata:
  version: "1.0.0"
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

# using-frontend-noslop

An orchestration skill that integrates `impeccable`, `frontend-design`, `design-taste-frontend`, `frontend-design-deslop`, `antislop-ui`, `no-ai-slop`, `pick-ui-library`, and `react-best-practices` into a single, cohesive frontend design and engineering pipeline.

---

## Core Rule: The Anti-Slop Floor

Do not output median AI code. Language models default to the statistical average of their training data: dark slate backgrounds, rounded-2xl cards with glowing borders, purple-to-cyan gradients, and generic marketing copy.

Every interface must have an intentional aesthetic direction, accessible semantics, responsive geometry, and complete state handling.

---

## Orchestration Workflow

Follow this sequence for any UI development task:

```
[ Phase 1: Aesthetic Stance ]  → frontend-design + frontend-design-deslop
             ↓
[ Phase 2: Design Tokens ]     → antislop-ui + DESIGN.md (OKLCH, Typography)
             ↓
[ Phase 3: Library Selection ] → pick-ui-library (Curated Primitives)
             ↓
[ Phase 4: Production Code ]   → react-best-practices + Incremental TDD
             ↓
[ Phase 5: Verification Gate ] → impeccable (/critique, /polish) + no-ai-slop
```

---

### Phase 1: Formulate the Aesthetic Stance
*Required:* `frontend-design` and `frontend-design-deslop`

1. Define the interface purpose before writing code. Determine who uses the interface and what problem it solves.
2. Declare an explicit, named visual direction derived from the domain (e.g. Editorial Brutalism, Swiss International, Luxury Utilitarian, Retro-Futurist, Technical Density).
3. Do not default to generic SaaS dark mode or unmotivated gradients. If requirements are ambiguous, prompt the user for direction before implementing.

---

### Phase 2: Design Tokens and Color Palette
*Required:* `antislop-ui` and `frontend-design-deslop`

1. Color:
   - Prefer OKLCH tokens for consistent perceptual lightness.
   - Do not use blue-to-purple or purple-to-pink gradients as default visual treatments.
   - Gradients are permitted only when serving a structural hierarchy function (such as depth elevation or state change).
2. Typography:
   - Choose a distinct font pairing matched to the aesthetic stance.
   - Adhere to a strict modular type scale with controlled line heights and tracking.
3. Whitespace:
   - Maintain proportional spacing rhythm using a mathematical 4px/8px grid.

---

### Phase 3: Component and Library Selection
*Required:* `pick-ui-library`

Use tested, unstyled, accessible primitives:

| Requirement | Recommended Library | Rationale |
|---|---|---|
| Primitives / Accessibility | Radix UI / Base UI | Unstyled, fully accessible, keyboard-first |
| Toasts / Notifications | Sonner | Stacked micro-interactions, responsive |
| Drawers / Bottom Sheets | Vaul | Fluid drag-to-dismiss physics |
| Command Menu | CMDK | Fast, keyboard-first fuzzy filtering |
| Motion / Animations | Motion (Framer Motion) | Spring physics, layout morphing |
| Virtualization | React Virtuoso | High-performance dynamic list handling |

---

### Phase 4: Production Architecture
*Required:* `react-best-practices`

1. Server Components by default; isolate `"use client"` to interactive leaves of the component tree.
2. Reserve aspect ratios and dimensions to prevent layout shifts (zero CLS).
3. Implement all five fundamental component states:
   - Initial / Empty
   - Loading (dimension-matched skeleton)
   - Populated
   - Error (with retry mechanism)
   - Disabled / Pending

---

### Phase 5: Verification Gate
*Required:* `impeccable` and `no-ai-slop`

Before completing the task, verify the implementation against this checklist:

- [ ] Palette Purpose: No arbitrary purple/cyan gradients.
- [ ] Structural Variety: No generic 3-card feature grids with placeholder icons.
- [ ] Copy Precision: All placeholder text replaced with direct, human wording.
- [ ] Accessibility: WCAG 2.1 AA contrast verified, full keyboard navigation with visible focus rings.
- [ ] Viewport Integrity: Tested at 360px mobile width without horizontal overflow.

Invoke `/critique` or `/polish` when available to verify optical alignment and hierarchy.

---

## Red Flags

| Rationalization | Reality |
|---|---|
| "A dark card with a subtle glow looks modern." | It is a common AI cliché. Build an intentional palette based on the product. |
| "I will add the loading state later." | Unhandled states cause layout jumps and broken UX. Build them now. |
| "The copy is just placeholder for now." | Generic AI copy undermines interface quality. Write clear, direct text. |
| "A 3-column card section is standard." | It indicates unconsidered layout design. Match layout to content requirements. |

---

## Direct Invocations

- `/impeccable` — Run the full craft floor and audit engine.
- `/frontend-design` — Generate intentional visual directions.
- `/design-taste-frontend` — Audit typography scale and spacing tension.
- `/frontend-design-deslop` — Strip median templates and create OKLCH tokens.
- `/antislop-ui` — Reference specific UI pattern rules.
- `/no-ai-slop` — Edit text and microcopy for clarity.
- `/pick-ui-library` — Select curated frontend packages.
- `/react-best-practices` — Enforce React and Next.js architecture standards.
