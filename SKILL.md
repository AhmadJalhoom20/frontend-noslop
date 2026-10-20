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

> **The Sovereign Anti-Slop Frontend Engine.**
> An uncompromising meta-orchestrator that unifies the world's most battle-tested frontend design and craft skills (`impeccable`, `frontend-design`, `design-taste-frontend`, `frontend-design-deslop`, `antislop-ui`, `no-ai-slop`, `pick-ui-library`, and `react-best-practices`) into a single non-negotiable standard.

---

## 🚨 The Anti-Slop Mandate (Iron Law)

**DO NOT SHIP MEDIAN AI UI.**
By default, language models sample the statistical average of web code: dark slate backgrounds, rounded-2xl glassmorphism cards, purple/indigo radial glows, generic Lucide icons, and hollow marketing copy.

**Violating the spirit of craft is a failure.** You are an award-winning design-engineer, not a layout generator. Every interface you touch must feel deliberate, human-crafted, technically extraordinary, and specifically tailored to the product's subject matter.

---

## 🗺️ Master Orchestration Workflow

When building or polishing any user interface, execute these five phases in strict sequence:

```
[ Phase 1: Aesthetic Stance ]  → frontend-design + frontend-design-deslop
             ↓
[ Phase 2: Design Tokens ]     → antislop-ui + DESIGN.md (OKLCH, Typography)
             ↓
[ Phase 3: Library Selection ] → pick-ui-library (Emil Kowalski's Picks)
             ↓
[ Phase 4: Production Code ]   → react-best-practices + Incremental TDD
             ↓
[ Phase 5: Craft Audit & Gate] → impeccable (/critique, /polish) + no-ai-slop
```

---

### Phase 1: Formulate the Aesthetic Stance
*Required Sub-Skill:* **`frontend-design`** & **`frontend-design-deslop`**

1. **Strategy before aesthetics:** Never open an IDE or write CSS before determining who this interface is for and what problem it solves.
2. **Explicit Aesthetic Direction:** Choose and declare a distinct, non-generic visual stance derived directly from the domain:
   - *Examples:* Editorial Brutalism, Swiss International, Luxury Utilitarian, Retro-Futurist, Warm Monastic, Technical Density.
   - **Banned:** Generic SaaS Dark Mode, "Vercel-clone" defaults, unmotivated gradients.
3. If the user’s prompt is vague ("build a dashboard"), invoke **`interview-me`** or prompt for 2–4 distinct creative directions before coding.

---

### Phase 2: Foundation, Tokens & Color Palette
*Required Sub-Skill:* **`antislop-ui`** & **`frontend-design-deslop`**

1. **Color (OKLCH over Hex/RGB):**
   - Define a functional, high-contrast palette with purposeful contrast ratios.
   - **Strictly Banned:** Blue-to-purple / purple-to-pink gradients as the primary visual hook.
   - If a gradient is used, it must serve a structural hierarchy purpose (e.g. elevation or depth map), never decor without reason.
2. **Typography Scale:**
   - Pick an intentional, characterful font pairing (e.g., a bold serif header with a clean grotesque sans body, or monospace utility accents).
   - Establish a strict modular scale (`text-xs`, `text-sm`, `base`, `xl`, `3xl`, `6xl`) with controlled line heights and tracking.
3. **Spatial Rhythm & Whitespace:**
   - Maintain whitespace tension. Don't crowd elements, and don't float empty components in void without proportional relationship.

---

### Phase 3: Curated Component & Library Selection
*Required Sub-Skill:* **`pick-ui-library`**

Never install bloated or unmaintained UI libraries. Use Emil Kowalski's curated, taste-driven standard picks:

| Need | Primary Recommended Tool | Why |
|---|---|---|
| **Primitives / A11y** | **Radix UI** / **Base UI** | Unstyled, fully accessible, bulletproof |
| **Toasts / Notifications** | **Sonner** | Clean micro-interactions, responsive stacking |
| **Drawers / Bottom Sheets**| **Vaul** | Physics-based fluid gestures |
| **Command Menu (K-Bar)**  | **CMDK** | Fast, accessible, keyboard-first |
| **Animations / Transitions**| **Motion** (Framer Motion) | Spring physics, layout morphing |
| **Icons** | **Lucide** / **Heroicons** (Curated) | Never scatter random mismatched icons |

---

### Phase 4: Production Implementation & Performance
*Required Sub-Skill:* **`react-best-practices`**

1. **RSC Architecture:** Default to Server Components; push Client Components (`"use client"`) to the extreme leaves of the tree.
2. **No Layout Shifts (CLS):** Always reserve aspect ratio space for media, skeletons, and dynamic data.
3. **Full State Coverage:** Every interactive component must handle all 5 states:
   - `Initial / Empty`
   - `Loading / Skeleton` (never a bare spinner on a blank screen)
   - `Populated / Happy path`
   - `Error / Retry`
   - `Disabled / Pending`

---

### Phase 5: The "No-Slop" Delivery Gate
*Required Sub-Skill:* **`impeccable`** & **`no-ai-slop`**

Before delivering the code to the user, conduct the **Delivery Gate Audit**:

#### 1. The Slop Checklist (Must be 100% CLEAN):
- [ ] **No Default Purple/Cyan Gradients:** Is the color scheme derived from a real brand identity?
- [ ] **No Generic 3-Card Feature Grids:** Are features explained through contextual UI, interactive demos, or asymmetrical layouts?
- [ ] **No Sparkle Clichés:** Are action buttons free from gratuitous `✨ Magic` icons?
- [ ] **No Hollow Copy:** Has every "Unlock Next-Gen Potential" or "Streamline Your Workflow" been replaced with concrete, crisp human text?
- [ ] **Accessibility (WCAG 2.1 AA):** Are all inputs labeled, focus states visible, and color contrasts verified?
- [ ] **Responsive Integrity:** Does the layout breathe on 375px mobile just as gracefully as on 1440px desktop?

#### 2. Impeccable Inspection Passes:
* Invoke `/critique` or `/polish` to verify visual hierarchy, optical alignment, and micro-interaction fluidity.

---

## 🚫 Red Flags & Anti-Rationalizations

If you catch yourself thinking any of these, **STOP and re-align**:

| The Agent's Rationalization | Reality |
|---|---|
| *"A simple dark mode with purple glow looks modern and fast to build."* | It screams low-effort AI template. Build a palette with real identity. |
| *"I'll add the empty/error states later."* | Half of UX happens in non-ideal states. Build them now. |
| *"The copy doesn't matter, it's just placeholder."* | Generic AI copy ruins high-craft design. Use sharp, realistic wording. |
| *"A standard 3-column card section is what users expect."* | It's what lazy landing page templates do. Use layout hierarchy that matches the actual product. |
| *"This component is good enough, no need to audit."* | Run the Delivery Gate checklist before declaring done. |

---

## 🛠️ Sub-Skill Direct Invocations

When you need focused deep-dives during development:
- `/impeccable` — Run the full Paul Bakaus craft floor and audit engine.
- `/frontend-design` — Generate intentional design stances and eliminate cookie-cutter styles.
- `/design-taste-frontend` — Audit typography scale, optical balance, and visual tension.
- `/frontend-design-deslop` — Strip AI-slop traits and generate OKLCH token systems.
- `/antislop-ui` — Reference specific UI pattern fixes and color rules.
- `/no-ai-slop` — Polish marketing copy and microcopy to sound human.
- `/pick-ui-library` — Select curated, world-class UI packages.
- `/react-best-practices` — Enforce Next.js / React performance and architecture.
