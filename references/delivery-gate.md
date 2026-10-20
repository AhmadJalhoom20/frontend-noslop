# The "No-Slop" Delivery Gate Checklist

Before submitting frontend code to production or delivering to the user, run this mandatory pass:

---

### Step 1: Slop Audit
- [ ] No unmotivated purple/cyan gradients anywhere on the page.
- [ ] No generic 3-card feature grid with placeholder icons.
- [ ] No generic AI buzzwords ("Seamlessly elevate", "Next-gen synergy").
- [ ] No missing error or loading skeletons.

### Step 2: Architecture Audit
- [ ] `"use client"` is isolated only where client interactivity is required.
- [ ] All images have `width`, `height`, and `alt` tags to prevent layout shift.
- [ ] Fonts are loaded via `next/font` with font-display swap.

### Step 3: Polish Pass
- [ ] Mobile viewport tested down to 360px width without horizontal overflow.
- [ ] Focus rings are visible when navigating using `Tab`.
- [ ] Micro-interactions have spring damping (not sluggish linear animations).
