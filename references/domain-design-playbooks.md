# Domain Design Playbooks & Real-World Inspiration Engine

When building an interface for a specific industry or niche, you MUST NOT guess or default to generic SaaS cards. You must ground the design in the visual language, typography, and interaction patterns of the absolute world-class leaders in that space.

---

## 🏋️ 1. Fitness, Athletics & High Performance
* **World-Class Benchmarks:** WHOOP, Nike Training Club, Gymshark, Peloton, Strava, Apple Fitness+.
* **Visual Tone & Mood:** Kinetic, aggressive, disciplined, high-voltage contrast, dark-mode biased.
* **Palette Formula:**
  - Background: Deep carbon `#0A0A0C` or raw asphalt `#111215`.
  - Surface: `#18191E` with subtle `border-white/[0.08]`.
  - High-Voltage Accent (Pick ONE): Laser Volt (`#CCFF00` / `#D4F63C`) or Infrared Neon (`#FF3B30`) or Electric Cobalt (`#3B82F6`).
  - Text: Stark White `#FFFFFF` + Muted Graphite `#8E929E`.
* **Typography Anchor:**
  - Headings: Condensed, heavy, impactful grotesque (e.g. `Anton`, `Bebas Neue`, or uppercase `Inter` with `tracking-tight font-black`).
  - Body & Data: Monospaced numeric telemetry (`font-mono` / `tabular-nums`) for reps, heart rate, volume, and pace.
* **Signature Components (Build These, Not Generic Cards):**
  - **Biometric Telemetry HUD:** Circular or linear progress rings with micro-metric badges (BPM, Strain, Sleep Score).
  - **Workout Routine Timeline:** Asymmetrical vertical sequence showing rest intervals, set rep ranges, and weight loads.
  - **Volume Heatmap:** Week-over-week workout density matrix (like GitHub commit graph but for muscle groups).
* **Slop To Avoid:**
  - ❌ Stock photos of smiling people holding blue plastic dumbbells.
  - ❌ Cyan-to-purple gradient overlays on workout cards.
  - ❌ Generic 3-card pricing table ("Beginner, Intermediate, Elite").

---

## 🛍️ 2. High-End E-Commerce & Modern Retail
* **World-Class Benchmarks:** SSENSE, Apple Store, Arc'teryx, Aesop, Glossier, Shopify Plus flagships.
* **Visual Tone & Mood:** Restrained, editorial, museum-quality product staging, frictionless conversion.
* **Palette Formula:**
  - Background: Clean Bone Paper `#F7F7F5` or Warm Alabaster `#FAFAF8` (or Pitch Black for luxury streetwear).
  - Surface: Pure `#FFFFFF` or `#0F0F11`.
  - Accent: Sophisticated Carbon Black `#111111` or Deep Terracotta `#C25E40` or Forest Pine `#1B3B2B`.
* **Typography Anchor:**
  - Headings: Refined Neo-Grotesque (`Geist`, `Inter`) or high-end Editorial Serif (`Playfair Display`, `Cormorant Garamond`).
  - Body: Crisp, high-tracking uppercase labels (`tracking-widest text-xs font-medium uppercase`).
* **Signature Components (Build These):**
  - **Frictionless Slide-Over Cart (Drawer):** Built with `vaul`, showing line items, tax breakdown, and instant single-click Apple Pay / checkout button.
  - **Multi-Angle Gallery with Aspect Lock:** Asymmetrical 2-column image mosaic with fixed aspect ratios (`aspect-[3/4]`), zero layout shift.
  - **Tactile Variant Selectors:** Pill-based size matrix with strike-through sold-out states and low-stock urgency badges.
  - **Collapsible Specification Accordions:** Materials, sizing guide, and provenance details via Radix Accordion.
* **Slop To Avoid:**
  - ❌ Loud yellow "50% OFF FLASH SALE!!!" banners with countdown timers.
  - ❌ Star ratings with tacky yellow clip-art stars.
  - ❌ Cluttered grids of tiny square images with overlapping badges.

---

## 💳 3. Fintech, Banking & Modern Payments
* **World-Class Benchmarks:** Stripe, Wise, Mercury, Ramp, Cash App, Brex.
* **Visual Tone & Mood:** Crystalline clarity, cryptographic security, ultra-high trust, precision alignment.
* **Palette Formula:**
  - Background: Deep Obsidian `#08090C` or Clean Bank White `#F9FAFC`.
  - Surface: `#111318` or `#FFFFFF`.
  - Accent: High-trust Industrial Blue (`#2563EB`) or Alpine Mint (`#00D084`) or Deep Slate (`#0F172A`).
* **Typography Anchor:**
  - Strict alignment with `tabular-nums` for all financial figures.
  - Currency symbols smaller than integer numbers (`$4,820.00` where `$` and `.00` have `text-muted-foreground text-sm`).
* **Signature Components (Build These):**
  - **Dual-Currency Transfer Card:** Interactive split input with live exchange rate ticker and transparent fee calculator.
  - **Interactive Ledger / Transaction Table:** Virtualized rows with status chips (`Settled`, `Pending`, `Refunded`) and downloadable CSV receipts.
  - **Virtual Card Visualizer:** Sleek physical card mockup with chip, masked card number, and toggleable freeze switch.
* **Slop To Avoid:**
  - ❌ Floating 3D golden coins or cartoon piggy banks.
  - ❌ Gratuitous crypto neon glows.
  - ❌ Missing pending/disabled transaction states.

---

## 💻 4. Developer Tools, Cloud Platforms & Terminals
* **World-Class Benchmarks:** Linear, Vercel, Supabase, Raycast, GitHub, Cloudflare.
* **Visual Tone & Mood:** High-density, keyboard-first, ultra-responsive, monochromatic with surgical laser accents.
* **Palette Formula:**
  - Background: Deep Space Obsidian `#08090B`.
  - Surface: `#101216` with physical `border-white/[0.08]`.
  - Accent: Crisp White `#FFFFFF` or Electric Indigo `#6366F1` or Cyan Accent strictly for focus states.
* **Typography Anchor:**
  - Monospace font for commands, keys, and outputs (`JetBrains Mono`, `Geist Mono`, `Consolas`).
  - Dense compact type scale: 12px labels, 14px body, 20px headers.
* **Signature Components (Build These):**
  - **Interactive CLI / Shell Preview:** Code block with one-click copy, branch indicator, and syntax highlighting.
  - **Command Palette (`CMDK`):** Global `⌘K` fuzzy search with keyboard shortcut chips (`<kbd>`).
  - **Live Service Status Grid:** Real-time latency graph with pulse indicators (P99 latency, 99.99% uptime).
* **Slop To Avoid:**
  - ❌ Centered generic marketing cards with meaningless icons.
  - ❌ Code blocks with fake, non-functional copy buttons.
  - ❌ Rainbow gradient text on technical headings.

---

## 🍽️ 5. Food, Dining, Cafes & Culinary Experience
* **World-Class Benchmarks:** Blue Bottle Coffee, Noma, Sweetgreen, Toast POS, Tartine Bakery.
* **Visual Tone & Mood:** Warm, tactile, organic, appetizing, generous typography, authentic textures.
* **Palette Formula:**
  - Background: Warm Oatmeal `#F5F2EB` or Roasted Espresso `#1A1615`.
  - Surface: `#FFFFFF` or `#241F1E`.
  - Accent: Warm Terracotta `#C85A32` or Olive Leaf `#4A5844` or Deep Brass `#B8860B`.
* **Typography Anchor:**
  - Warm serif headlines (`Fraunces`, `Playfair Display`) paired with a clean geometric sans body (`Inter`).
* **Signature Components (Build These):**
  - **Ingredient Provenance Card:** Origin map, roast profile/flavor notes meter (Acidity, Body, Sweetness).
  - **Interactive Dietary Filter Bar:** Single-click pills for Gluten-Free, Vegan, Halal, Nut-Free.
  - **Table Reservation / Pickup Slot Selector:** Visual time-wheel with real-time seat availability.

---

## 🌐 6. Creative Agencies, Portfolios & Culture
* **World-Class Benchmarks:** Pentagram, Apple Design Awards, Awwwards Site of the Year winners, ReadCV, Are.na.
* **Visual Tone & Mood:** Bold, confident, unexpected spatial rhythm, editorial scale, confident whitespace.
* **Palette Formula:**
  - Pure Monochrome: `#000000` & `#FFFFFF` with intentional mid-gray `#737373`.
  - Or single daring signature tint (e.g. International Klein Blue `#002FA7` or Acid Green `#00FF66`).
* **Signature Components (Build These):**
  - **Fullscreen Project Showcase:** Hover-triggered video/image swap with client name, year, and role.
  - **Archive View Toggle:** Switch between high-impact visual mosaic and ultra-dense data list.
  - **Interactive Case Study Index:** Sticky timeline with milestone previews and live demo links.
