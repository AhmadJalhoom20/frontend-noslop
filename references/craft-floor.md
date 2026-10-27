# The 50-Point Craft Floor & Self-Critique Rubric (v4.0)

Before delivering any frontend UI code or declaring a task complete, evaluate your output across these 5 core dimensions. **Every dimension is scored from 0 to 10 points. Minimum passing score is 45/50.** Any score below 45 requires an immediate refactor turn before presenting code to the user.

---

### Dimension 1: Chromatic Discipline & Contrast (10 Points)
* [ ] **Zero Gradient Text (3 pts):** All headlines, titles, and body copy use solid, legible typography.
* [ ] **Single Brand Hue (3 pts):** Exactly one accent hue is active. No clashing purple/cyan/pink/yellow combinations.
* [ ] **90/10 Ratio (2 pts):** At least 90% of screen surface area is composed of neutral, calm backgrounds and cards.
* [ ] **Physical Elevation (2 pts):** Depth is created with 1px border subtleties (`border-white/[0.08]`) and surface luminance, NOT colored glowing box-shadows.

---

### Dimension 2: Domain Realism & Layout Anatomy (10 Points)
* [ ] **Industry Benchmark Grounding (4 pts):** The interface visually mirrors leaders in that exact vertical (e.g., Nike/WHOOP for fitness, SSENSE/Apple for retail, Stripe/Wise for fintech).
* [ ] **Anti-3-Card Enforcement (3 pts):** No uniform 3-card grid with pastel-boxed icons. Layout is asymmetrical (bento, split hero, live telemetry rail).
* [ ] **Whitespace & Spacing Grid (3 pts):** Strict mathematical 8px spacing rhythm (`gap-2`, `gap-4`, `gap-6`, `gap-8`) with proportional hierarchy.

---

### Dimension 3: Complete 5-State Architecture (10 Points)
* [ ] **Loading Skeleton (3 pts):** Dimension-matched skeleton screens that prevent Cumulative Layout Shift (CLS = 0).
* [ ] **Empty State (2 pts):** Friendly, actionable empty state with a clear next step (no dead blank space).
* [ ] **Error Boundary (3 pts):** Empathetic, human error messaging with a functional retry mechanism.
* [ ] **Disabled & Pending Feedback (2 pts):** Explicit busy indicators (`aria-busy="true"`) and reduced opacity during mutations.

---

### Dimension 4: Semantic Accessibility & WCAG 2.1 AA (10 Points)
* [ ] **Semantic Elements (3 pts):** Buttons are `<button type="button">`, navigation is `<nav>`, dialogs use `<dialog>` or Radix Dialog. Zero `<div onClick>`.
* [ ] **Visible Focus Rings (3 pts):** Every interactive button, link, and input has high-visibility focus states (`focus-visible:ring-2 focus-visible:ring-ring`).
* [ ] **Color Contrast (2 pts):** All text passes minimum 4.5:1 contrast against its background (WCAG AA).
* [ ] **Keyboard Navigation (2 pts):** Complete Escape-key handling for modals, Tab-trapping in drawers, and arrow-key menu navigation.

---

### Dimension 5: Human Voice & Copy Precision (10 Points)
* [ ] **Zero Marketing Slop (4 pts):** Completely eliminated robotic filler (*"streamline your synergy"*, *"unlock the power"*, *"next-gen"*).
* [ ] **Factual Technical Specificity (3 pts):** Mentions exact facts, numbers, and capabilities (e.g. *"Sub-millisecond p99 latency"*, *"AES-256 encryption"*).
* [ ] **Active Action Verbs (3 pts):** Buttons name the concrete action (*"Deploy Cluster"*, *"Create Project"*, *"Export CSV"*), never vague words (*"Submit"*, *"OK"*, *"Click Here"*).

---

## 🏆 Scoring Gate

| Total Score | Status | Required Agent Action |
|---|---|---|
| **45 – 50** | **APPROVED (Studio Grade)** | Code is production-ready. Deliver to user with confidence. |
| **38 – 44** | **NEEDS POLISH** | Run one automatic refactor turn to fix the lowest-scoring dimension. |
| **< 38** | **REJECTED (AI Slop Detected)** | Total redesign required. Re-read `references/code-recipes.md` and rebuild. |
