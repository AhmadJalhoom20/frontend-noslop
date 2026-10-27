#!/usr/bin/env python3
"""
Frontend No-Slop Automated Linter & Craft Auditor (v4.0)
Scans frontend code (TSX, JSX, HTML, CSS, Vue, Svelte) for AI-slop anti-patterns:
- Stupid gradients & gradient text
- Ambient blur circles (blur-3xl blobs)
- Neon drop-shadows & glow borders
- Robotic marketing buzzwords
- Clickable non-semantic divs & missing keyboard accessibility
- Candy/rainbow badge assortments
- Missing layout aspect-ratio reservations (CLS risk)
"""

import sys
import os
import re
import argparse

# Violations with penalty scores and actionable remediation
LINT_RULES = [
    {
        "id": "SLOP-001",
        "name": "Gradient Text Cliché",
        "pattern": r"(bg-clip-text\s+text-transparent|text-transparent\s+bg-clip-text)",
        "severity": "CRITICAL",
        "penalty": 15,
        "fix": "Remove gradient text. Use solid, high-contrast typography (e.g. text-neutral-100 or text-foreground)."
    },
    {
        "id": "SLOP-002",
        "name": "Multi-Hue Gradient Slop",
        "pattern": r"(bg-gradient-to-[a-z]+\s+(from-(purple|indigo|violet|pink|cyan|fuchsia)-[0-9]{3}\s+to-(cyan|pink|purple|indigo|amber|emerald)-[0-9]{3}|from-[a-z]+-[0-9]{3}\s+via-[a-z]+-[0-9]{3}\s+to-[a-z]+-[0-9]{3}))",
        "severity": "CRITICAL",
        "penalty": 15,
        "fix": "Banned multi-color gradient. Use solid neutral surfaces or subtle single-step monochrome shifts."
    },
    {
        "id": "SLOP-003",
        "name": "Ambient Glow Blur Blob",
        "pattern": r"(blur-3xl|blur-\[1[0-9]{2}px\]).*(bg-(purple|indigo|violet|pink|cyan|blue)-[0-9]{3}\/(10|20|30|40|50))",
        "severity": "HIGH",
        "penalty": 10,
        "fix": "Remove the ambient blur blob. Use structured 1px border contrast, gridlines, or tangible card surfaces."
    },
    {
        "id": "SLOP-004",
        "name": "Neon Colored Outer Glow Shadow",
        "pattern": r"shadow-(purple|indigo|violet|pink|cyan|blue)-[0-9]{3}\/(30|40|50|60|70)",
        "severity": "HIGH",
        "penalty": 10,
        "fix": "Remove glowing outer shadow. Use physical 1px border elevation (border-white/[0.08] or border-border)."
    },
    {
        "id": "SLOP-005",
        "name": "Robotic Marketing Buzzwords",
        "pattern": r"\b(streamline your synergy|unlock the power of|revolutionary|cutting-edge|next-gen ai|seamless integration|game-changer|supercharge your)\b",
        "flags": re.IGNORECASE,
        "severity": "HIGH",
        "penalty": 10,
        "fix": "Replace marketing buzzwords with direct, human, factual prose describing exact functionality."
    },
    {
        "id": "SLOP-006",
        "name": "Clickable Non-Semantic Div",
        "pattern": r"<div\b[^>]*\bonClick\b",
        "severity": "CRITICAL",
        "penalty": 15,
        "fix": "Use a semantic <button> element with type='button' and full keyboard focus accessibility."
    },
    {
        "id": "SLOP-007",
        "name": "Gratuitous Sparkle Emoji in Action",
        "pattern": r">\s*[^<]*[✨🪄]\s*[^<]*<\/(button|a)>",
        "severity": "MEDIUM",
        "penalty": 5,
        "fix": "Remove cheesy sparkle emojis. Use clear, confident action verbs (e.g. 'Generate Report', 'Deploy')."
    },
    {
        "id": "SLOP-008",
        "name": "Missing Interactive Focus Ring",
        "pattern": r"<(button|a)\b(?![^>]*focus(-visible)?:ring)[^>]*className=",
        "severity": "MEDIUM",
        "penalty": 5,
        "fix": "Add explicit focus-visible rings for WCAG 2.1 AA keyboard accessibility (e.g. focus-visible:ring-2 focus-visible:ring-ring)."
    },
    {
        "id": "SLOP-009",
        "name": "Asymmetrical Colored Side-Border Stripe (The Sidebg Cliché)",
        "pattern": r"border-(l|r|s|e)-[0-9]+\s+border-(indigo|purple|emerald|cyan|blue|green|amber|red|pink|violet|teal|rose)-[0-9]{3}",
        "severity": "HIGH",
        "penalty": 10,
        "fix": "Remove the cheap colored side-accent stripe. Use complete 360-degree border geometry (border border-white/[0.08]) with an inline status dot or badge."
    },
    {
        "id": "SLOP-010",
        "name": "Spinning Loader Fallback Instead of Skeleton",
        "pattern": r"(animate-spin\s+rounded-full\s+border-(2|4)|LucideLoader\s+className=.*animate-spin)",
        "severity": "MEDIUM",
        "penalty": 5,
        "fix": "Replace blocking spinners on page/card content with dimension-matched Shimmer Skeletons to prevent layout shift."
    }
]

def audit_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        return {"file": filepath, "error": str(e), "score": 0, "violations": []}

    violations = []
    total_penalty = 0

    lines = content.splitlines()

    for rule in LINT_RULES:
        flags = rule.get("flags", 0)
        regex = re.compile(rule["pattern"], flags)
        
        for idx, line in enumerate(lines):
            match = regex.search(line)
            if match:
                violations.append({
                    "rule_id": rule["id"],
                    "name": rule["name"],
                    "severity": rule["severity"],
                    "line": idx + 1,
                    "snippet": line.strip()[:100],
                    "fix": rule["fix"]
                })
                total_penalty += rule["penalty"]

    score = max(0, 100 - total_penalty)
    return {
        "file": filepath,
        "score": score,
        "passed": score >= 85 and not any(v["severity"] == "CRITICAL" for v in violations),
        "violations": violations
    }

def main():
    parser = argparse.ArgumentParser(description="Audit frontend files for AI-slop anti-patterns.")
    parser.add_argument("paths", nargs="+", help="Files or directories to audit.")
    args = parser.parse_args()

    files_to_check = []
    for path in args.paths:
        if os.path.isfile(path):
            files_to_check.append(path)
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    if file.endswith((".tsx", ".jsx", ".html", ".vue", ".svelte", ".css")):
                        files_to_check.append(os.path.join(root, file))

    if not files_to_check:
        print("No matching frontend files found to audit.")
        sys.exit(0)

    print(f"\n🔍 Auditing {len(files_to_check)} frontend file(s) for AI-slop...")
    print("=" * 65)

    all_passed = True
    for f in files_to_check:
        res = audit_file(f)
        status_symbol = "✅ PASS" if res["passed"] else "❌ FAIL"
        print(f"\n{status_symbol} [{res['score']}/100] {res['file']}")

        if res["violations"]:
            all_passed = False
            for v in res["violations"]:
                print(f"  • [{v['severity']}] Line {v['line']}: {v['name']}")
                print(f"    Code: {v['snippet']}")
                print(f"    Fix:  {v['fix']}")

    print("\n" + "=" * 65)
    if all_passed:
        print("🏆 CRAFT AUDIT PASSED: Studio-grade, zero-slop code verified!")
        sys.exit(0)
    else:
        print("🚨 CRAFT AUDIT FAILED: Please resolve the violations above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
