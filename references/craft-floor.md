# The Craft Floor (The Non-Negotiable Standard)

The **Craft Floor** defines the absolute quality baseline below which no agent output may ever fall.

---

## 1. Typography & Hierarchy
* **Scale Integrity:** Never use arbitrary font sizes (`text-[15px]`, `text-[22px]`). Stick strictly to your declared design tokens.
* **Line-height Calibration:** Headlines must have tight leading (`leading-tight` or `leading-none`). Long-form body copy must have comfortable reading room (`leading-relaxed`).
* **Letter Spacing:** Wide letter spacing (`tracking-widest`) is reserved for uppercase subheaders or tags; headlines should use optical negative tracking (`tracking-tight`).

---

## 2. Color Science (OKLCH)
* **Perceptual Uniformity:** Always prefer OKLCH or calibrated HSL tokens over uncurated Hex codes. OKLCH guarantees consistent lightness across hues.
* **Contrast Ratios:** Text must strictly meet **WCAG 2.1 AA** contrast ratios (minimum 4.5:1 for normal text, 3:1 for large text).
* **True Blacks:** Avoid pure `#000000` on white backgrounds unless practicing deliberate high-contrast Brutalism. Use rich, warm or cool charcoal undertones.

---

## 3. Spatial Tension & Rhythm
* **4px / 8px Grid Discipline:** Every padding, margin, and gap must adhere to a mathematical 4px/8px modular rhythm.
* **Optical Alignment:** Ensure icons and text align optically, not just mechanically. Use flexbox baseline alignment where appropriate.

---

## 4. The 5 Component States
No component is complete until all five states are implemented in code:
1. **Empty State:** Helpful, actionable, reassuring.
2. **Loading State:** Height-matched skeleton reservation; never an unexpected jump or empty flash.
3. **Populated (Ideal) State:** Clean, readable, balanced.
4. **Error / Recovery State:** Clear human explanation with an immediate retry button.
5. **Disabled / Pending State:** Visually distinct affordance preventing duplicate submissions.
