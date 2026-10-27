# The Definitive Domain Design Playbooks (v5.0)

When tasked with designing or building for ANY industry, you MUST NOT invent generic layouts or use one-size-fits-all SaaS cards. You must strictly load and enforce the exact **Domain DNA** specified below.

---

## 🏋️ 1. Fitness, Athletics & High-Performance Training
* **Premier Benchmarks:** WHOOP, Nike Training Club, Gymshark, Peloton, Strava, Apple Fitness+.
* **Visual Tone & Mood:** Kinetic, disciplined, high-voltage contrast, dark-mode biased, muscular geometry.
* **Exact Color Palette:**
  - `Canvas Background:` `#08090A` (Deep carbon obsidian)
  - `Card Surface:` `#121316` (Clean matte armor)
  - `Border:` `rgba(255, 255, 255, 0.08)` (Subtle 360° perimeter)
  - `Text Primary:` `#FFFFFF` (High contrast pure white)
  - `Text Secondary:` `#8E929E` (Muted athletic gray)
  - `Domain Accent (Pick ONE):` **Laser Volt** (`#CCFF00`) OR **Infrared Neon** (`#FF2A2A`) OR **Electric Cyan** (`#00F0FF`).
* **Typography Stack:**
  - Headings: Condensed, heavy, impactful grotesque (`Anton`, `Bebas Neue`, or `Inter` with `uppercase font-black tracking-tight`).
  - Metrics & Data: Monospaced numeric telemetry with `font-mono tabular-nums`.
* **Signature Components (MANDATORY):**
  - **Biometric Telemetry HUD:** Circular/linear progress rings tracking Heart Rate, Strain, Recovery Score, and Caloric burn.
  - **Workout Routine Timeline:** Asymmetrical vertical sequence showing rest intervals, set rep ranges, and weight loads.
  - **Weekly Volume Heatmap:** 7-day muscle group density grid (visualizing chest, back, legs, core strain).
  - **Personal Record (PR) Badge:** Discrete high-contrast pill with micro-spark icon and date timestamp.
* **Domain Skeleton Loader:**
  - Shimmering circular gauge skeleton (`h-24 w-24 rounded-full`) + tabular metric line skeletons.
* **Copy Tone & Forbidden Words:**
  - *Tone:* Relentless, disciplined, performance-first, metric-driven.
  - *Keywords:* Reps, Sets, Time Under Tension, Split, Strain, Recovery, P90 Output.
  - *Banned:* "Unlock your potential", "Get fit easy", "Magic workout", "Lose belly fat fast".

---

## 🛍️ 2. High-End E-Commerce & Modern Retail
* **Premier Benchmarks:** SSENSE, Apple Store, Arc'teryx, Aesop, Glossier, Shopify Plus flagships.
* **Visual Tone & Mood:** Restrained, editorial, museum-quality product staging, frictionless conversion.
* **Exact Color Palette:**
  - `Canvas Background:` `#F7F7F5` (Warm Bone Paper) OR `#0A0A0C` (Luxury Velvet Black)
  - `Card Surface:` `#FFFFFF` (Pure Gallery White) OR `#121214`
  - `Border:` `#E6E8EC` (Light mode) OR `rgba(255, 255, 255, 0.08)` (Dark mode)
  - `Text Primary:` `#111111` (Carbon Black) OR `#EDEDED`
  - `Text Secondary:` `#666666` OR `#888888`
  - `Domain Accent (Pick ONE):` **Deep Obsidian Black** (`#111111`) OR **Terracotta** (`#C25E40`) OR **Forest Pine** (`#1B3B2B`).
* **Typography Stack:**
  - Headings: Refined Neo-Grotesque (`Geist`, `Inter`) or High-Fashion Editorial Serif (`Playfair Display`, `Cormorant Garamond`).
  - Labels & Microcopy: Spaced uppercase micro-labels (`tracking-widest text-xs uppercase font-medium`).
* **Signature Components (MANDATORY):**
  - **Frictionless Slide-Over Cart (Drawer):** Built with `vaul`, showing line items, shipping thresholds, and 1-click checkout.
  - **Multi-Angle Gallery with Aspect Lock:** Asymmetrical 2-column image mosaic with fixed aspect ratios (`aspect-[3/4]`), zero CLS.
  - **Tactile Variant Selectors:** Pill-based size matrix with strike-through sold-out states and low-stock urgency badges.
  - **Collapsible Specification Accordions:** Materials, sizing guide, and provenance details via Radix Accordion.
* **Domain Skeleton Loader:**
  - Aspect-locked image skeleton (`aspect-[3/4] rounded-lg`) + two clean text line skeletons.
* **Copy Tone & Forbidden Words:**
  - *Tone:* Understated, material-focused, sensory, confident.
  - *Keywords:* Raw materials, Weight (GSM), Tailored silhouette, Origin, Responsibly sourced.
  - *Banned:* "HURRY 50% OFF FLASH SALE", "Best deal ever", "Cheap prices", "Must buy now".

---

## 💳 3. Fintech, Banking & Modern Payments
* **Premier Benchmarks:** Stripe, Wise, Mercury, Ramp, Cash App, Brex.
* **Visual Tone & Mood:** Crystalline clarity, cryptographic security, ultra-high trust, Swiss alignment.
* **Exact Color Palette:**
  - `Canvas Background:` `#08090C` (Deep Vault Obsidian) OR `#F9FAFC` (Clean Bank White)
  - `Card Surface:` `#101216` OR `#FFFFFF`
  - `Border:` `rgba(255, 255, 255, 0.08)` OR `#E5E7EB`
  - `Text Primary:` `#EDEDED` OR `#0F172A`
  - `Text Secondary:` `#8B909A` OR `#64748B`
  - `Domain Accent (Pick ONE):` **Industrial Cobalt** (`#2563EB`) OR **Alpine Mint** (`#00D084`) OR **Deep Slate** (`#0F172A`).
* **Typography Stack:**
  - Swiss Grotesque (`Inter`, `Geist`) with strict `tabular-nums` for all financial figures.
  - Decimal hierarchy: Currency symbol and cents rendered at 70% opacity and slightly smaller font size.
* **Signature Components (MANDATORY):**
  - **Dual-Currency Conversion Split Card:** Interactive currency converter with live exchange rate ticker and transparent fee calculation.
  - **Interactive Ledger / Transaction Table:** Virtualized rows with status chips (`Settled`, `Pending`, `Refunded`) and downloadable CSV receipts.
  - **Virtual Debit Card Visualizer:** Sleek physical card mockup with chip, masked card number, and toggleable freeze switch.
* **Domain Skeleton Loader:**
  - Tabular table row skeletons with fixed column widths and pill-shaped status skeletons.
* **Copy Tone & Forbidden Words:**
  - *Tone:* Crystalline, transparent, unambiguous, secure.
  - *Keywords:* Settlement, Liquidity, Interbank rate, FDIC-insured, Cryptographic audit, Zero hidden markup.
  - *Banned:* "Get rich quick", "Magic money", "Crypto moon", "Revolutionize your wallet".

---

## 💻 4. Developer Tools, Cloud Platforms & Terminals
* **Premier Benchmarks:** Linear, Vercel, Supabase, Raycast, GitHub, Cloudflare.
* **Visual Tone & Mood:** High-density, keyboard-first, ultra-responsive, monochromatic with surgical laser accents.
* **Exact Color Palette:**
  - `Canvas Background:` `#08090B` (Deep Space Obsidian)
  - `Card Surface:` `#101216` (Engine Room Matte)
  - `Border:` `rgba(255, 255, 255, 0.08)`
  - `Text Primary:` `#EDEDED` (Crisp terminal white)
  - `Text Secondary:` `#7A808C`
  - `Domain Accent (Pick ONE):` **High-Contrast Pure White** (`#FFFFFF`) OR **Laser Cyan** (`#38BDF8`) OR **Electric Indigo** (`#6366F1`).
* **Typography Stack:**
  - Code & Commands: `JetBrains Mono`, `Geist Mono`, `Consolas`.
  - Body & Labels: Dense compact type scale: 12px labels, 14px body, 20px headers.
* **Signature Components (MANDATORY):**
  - **Interactive CLI / Shell Preview:** Code block with one-click copy, branch indicator, and syntax highlighting.
  - **Command Palette (`CMDK`):** Global `⌘K` fuzzy search with keyboard shortcut chips (`<kbd>`).
  - **Live Service Status Grid:** Real-time latency graph with pulse indicators (P99 latency, 99.99% uptime).
* **Domain Skeleton Loader:**
  - Monospaced code line skeletons with varying widths (40%, 65%, 85%, 30%).
* **Copy Tone & Forbidden Words:**
  - *Tone:* Terse, technical, deterministic, developer-first.
  - *Keywords:* p99 latency, AST, Ephemeral nodes, Zero cold-start, Deterministic, GitOps.
  - *Banned:* "Revolutionize your coding", "Effortless AI magic", "Simple 1-click wizard".

---

## 🩺 5. Healthcare, Medical & Clinical Technology
* **Premier Benchmarks:** Oscar Health, One Medical, Mayo Clinic Digital, Alto Pharmacy, Headway.
* **Visual Tone & Mood:** Reassuring, clinically precise, certified, calm, accessible (AAA contrast).
* **Exact Color Palette:**
  - `Canvas Background:` `#FAFBFC` (Sterile Clean White) OR `#080C10` (Clinical Night Mode)
  - `Card Surface:` `#FFFFFF` OR `#0F151C`
  - `Border:` `#E2E8F0` OR `rgba(255, 255, 255, 0.08)`
  - `Text Primary:` `#0F172A` OR `#F8FAFC`
  - `Text Secondary:` `#475569` OR `#94A3B8`
  - `Domain Accent (Pick ONE):` **Medical Sapphire** (`#0284C7`) OR **Clinical Teal** (`#0D9488`).
* **Typography Stack:**
  - Humanist Sans (`Plus Jakarta Sans`, `Inter`) for maximum legibility and friendliness.
* **Signature Components (MANDATORY):**
  - **Appointment Slot Stepper:** Visual time-slot matrix showing doctor photo, specialty, and certified availability.
  - **HIPAA-Compliant Security Seal:** Verified encryption badge with certificate fingerprint.
  - **Interactive Symptom Triage Flow:** Multi-step accessible questionnaire with clear progress bar.
* **Domain Skeleton Loader:**
  - Doctor avatar circle skeleton (`h-12 w-12 rounded-full`) + specialty pill + date slot grid.
* **Copy Tone & Forbidden Words:**
  - *Tone:* Empathetic, reassuring, clinically precise, verified.
  - *Keywords:* Board-certified, HIPAA compliant, Dosage, Clinical outcome, Confidential.
  - *Banned:* "Miracle cure", "Guaranteed healing", "Instant wellness fix".

---

## 🏛️ 6. Real Estate, Architecture & Spatial Living
* **Premier Benchmarks:** The Agency, Sotheby's International Realty, Architectural Digest, Airbnb Luxe.
* **Visual Tone & Mood:** Spatial, evocative, architectural, photographic grandeur, generous whitespace.
* **Exact Color Palette:**
  - `Canvas Background:` `#F5F2EB` (Warm Travertine) OR `#0D0D0E` (Obsidian Marble)
  - `Card Surface:` `#FFFFFF` OR `#141416`
  - `Border:` `#E4DFD5` OR `rgba(255, 255, 255, 0.08)`
  - `Text Primary:` `#1C1917` OR `#F5F5F4`
  - `Text Secondary:` `#78716C` OR `#A8A29E`
  - `Domain Accent (Pick ONE):` **Warm Bronze** (`#92400E`) OR **Deep Charcoal** (`#1C1917`).
* **Typography Stack:**
  - Architectural Neo-Grotesque (`Cabinet Grotesk`, `Syne`) or Refined Serif (`Cormorant Garamond`).
* **Signature Components (MANDATORY):**
  - **Interactive Floorplan Hotspot Viewer:** SVG architectural floorplan with hoverable room dimensions.
  - **Fullscreen Architectural Photo Slider:** Ultra-widescreen photo cards with aspect-ratio preservation (`aspect-[16/10]`).
  - **Property Dimension Matrix:** Tabular square footage, lot size, bedroom count, and price-per-sqft.
* **Domain Skeleton Loader:**
  - Large photographic skeleton (`aspect-[16/10] w-full rounded-xl`) + title & price skeletons.
* **Copy Tone & Forbidden Words:**
  - *Tone:* Spatial, evocative, architectural, discerning.
  - *Keywords:* Custom millwork, Terrazzo, Exposure, Cantilevered, Private loggia, Ceilings (12ft).
  - *Banned:* "Cheap house", "Budget starter home", "Crazy low prices".

---

## 🍽️ 7. Food, Dining & Culinary Arts
* **Premier Benchmarks:** Blue Bottle Coffee, Noma, Toast POS, Sweetgreen, Tartine Bakery.
* **Visual Tone & Mood:** Warm, tactile, organic, appetizing, generous typography, authentic textures.
* **Exact Color Palette:**
  - `Canvas Background:` `#F5F2EB` (Warm Oat Milk) OR `#181514` (Roasted Espresso)
  - `Card Surface:` `#FFFFFF` OR `#241F1E`
  - `Border:` `#E5DFC9` OR `rgba(255, 255, 255, 0.08)`
  - `Text Primary:` `#1F1A17` OR `#F7F4EE`
  - `Text Secondary:` `#6E6259` OR `#9C8F85`
  - `Domain Accent (Pick ONE):` **Warm Terracotta** (`#C85A32`) OR **Olive Leaf** (`#4A5844`) OR **Deep Wine** (`#722F37`).
* **Typography Stack:**
  - Expressive Culinary Serif (`Fraunces`, `Playfair Display`) paired with clean geometric body sans.
* **Signature Components (MANDATORY):**
  - **Ingredient Provenance Radar:** Tasting flavor notes radar (Acidity, Body, Sweetness, Roast Level).
  - **Interactive Dietary Pill Bar:** 1-click filters for Gluten-Free, Vegan, Halal, Nut-Free with active checkmarks.
  - **Table Reservation Slot Wheel:** Visual dining room time selector with party size count.
* **Domain Skeleton Loader:**
  - Menu row skeleton with dish title, price pill, and two-line ingredient description skeleton.
* **Copy Tone & Forbidden Words:**
  - *Tone:* Sensory, tactile, appetizing, origin-focused.
  - *Keywords:* Heirloom, Single-origin, House-fermented, Direct trade, Small-batch, Seasonal harvest.
  - *Banned:* "Yummy food", "Fast junk", "Cheap meals", "Finger-licking".

---

## 🎓 8. Education, Learning & Knowledge Platforms
* **Premier Benchmarks:** MasterClass, Brilliant.org, Duolingo, Khan Academy, Maven.
* **Visual Tone & Mood:** Focused, encouraging, structured, milestone-oriented, distraction-free.
* **Exact Color Palette:**
  - `Canvas Background:` `#FDFCF7` (Campus Cream) OR `#0A0F1D` (Study Midnight)
  - `Card Surface:` `#FFFFFF` OR `#111827`
  - `Border:` `#E5E7EB` OR `rgba(255, 255, 255, 0.08)`
  - `Text Primary:` `#111827` OR `#F9FAFB`
  - `Text Secondary:` `#4B5563` OR `#9CA3AF`
  - `Domain Accent (Pick ONE):` **Academic Amber** (`#D97706`) OR **Deep Indigo** (`#4F46E5`).
* **Typography Stack:**
  - Ultra-clear reading sans (`Inter`, `Public Sans`) with generous line-height (`leading-relaxed`).
* **Signature Components (MANDATORY):**
  - **Interactive Curriculum Tree:** Expandable module accordion with duration chips and lesson completion checkboxes.
  - **Progress Streak Indicator:** Daily activity tracker with motivational milestone badge.
  - **Knowledge Check Quiz Card:** Single-choice question with instant visual feedback and step-by-step reasoning.
* **Domain Skeleton Loader:**
  - Module tree skeleton with expanding child node skeletons.
* **Copy Tone & Forbidden Words:**
  - *Tone:* Pedagogical, encouraging, clear, milestone-driven.
  - *Keywords:* Curriculum, Prerequisite, Milestone, Learning objective, Applied project, Mastery.
  - *Banned:* "Learn in 5 minutes without effort", "Lazy shortcut", "Cheat your exam".
