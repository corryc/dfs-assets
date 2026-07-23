#!/usr/bin/env python3
"""
DFS Compact Keyword Page Generator

Reads a CSV of compact-keyword page data (one row per page) and fills the
master template to produce ready-to-review HTML files.

This script generates DRAFTS ONLY. It does not push to GitHub or Netlify.
Per DFS standing process, every generated page must still pass:
  1. /dfs-ad-compliance check (COMPLIANT verdict)
  2. Corry's explicit approval on the proof
before being pushed live.

Usage:
    python3 generate_compact_pages.py data/compact-keywords.csv

Output:
    One .html file per row, written to generated/, plus a validation
    report printed to the console. Rows that fail validation are still
    generated but flagged clearly - fix and re-run before requesting
    compliance review.
"""

import csv
import sys
import re
import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
TEMPLATE_PATH = SCRIPT_DIR.parent / "templates" / "compact-keyword-template.html"
OUTPUT_DIR = SCRIPT_DIR.parent / "generated"

REQUIRED_COLUMNS = [
    "slug", "target_keyword", "service_category", "title", "meta_description",
    "h1", "hero_eyebrow", "hero_subtitle", "intro_paragraph",
    "criteria_1", "criteria_2", "criteria_3",
    "faq_q1", "faq_a1", "faq_q2", "faq_a2", "faq_q3", "faq_a3",
    "related_page_title", "related_page_slug", "related_page_blurb",
    "cta_subtitle",
]

# Phrases that must never appear unqualified, per compliance.md.
# This is a fast pre-check, not a substitute for the full /dfs-ad-compliance
# skill review - it only catches the highest-risk absolute claims.
BANNED_UNQUALIFIED_PHRASES = [
    r"\bno lmi\b(?!.*subject to eligibility)",
    r"\bguaranteed\b",
    r"\bwon't pay lmi\b",
    r"\bindependent\b",
    r"\bimpartial\b",
    r"\bunbiased\b",
    r"\bno credit check\b",
    r"\bfinancial counsel(l)?or\b",
    r"\$[\d,]+k?\s*(saving|in savings)\b",
    r"\brate(s)? (of |from )?\d+(\.\d+)?%",
]

SMART_CHARS = ['\u2018', '\u2019', '\u201c', '\u201d', '\u2013', '\u2014']


def load_template():
    return TEMPLATE_PATH.read_text(encoding="utf-8")


def validate_row(row):
    issues = []

    title_len = len(row["title"])
    if not (50 <= title_len <= 60):
        issues.append(f"Title length {title_len} chars (target 50-60)")

    meta_len = len(row["meta_description"])
    if not (155 <= meta_len <= 160):
        issues.append(f"Meta length {meta_len} chars (target 155-160)")

    full_text = " ".join(str(v) for v in row.values())

    for ch in SMART_CHARS:
        if ch in full_text:
            issues.append(f"Smart character found: {ch!r} - use straight quotes/hyphens only")

    for pattern in BANNED_UNQUALIFIED_PHRASES:
        if re.search(pattern, full_text, re.IGNORECASE):
            issues.append(f"Compliance flag: matched pattern {pattern!r} - review against compliance.md before publishing")

    word_count = len(re.sub(r"<[^>]+>", " ", full_text).split())
    if word_count < 250:
        issues.append(f"Body content looks thin ({word_count} words) - compact keyword target is ~400-500 words total on page")

    return issues


def fill_template(template, row, timestamp):
    filled = template
    token_map = {
        "SLUG": row["slug"],
        "TIMESTAMP": timestamp,
        "TITLE": row["title"],
        "META_DESCRIPTION": row["meta_description"],
        "H1": row["h1"],
        "HERO_EYEBROW": row["hero_eyebrow"],
        "HERO_SUBTITLE": row["hero_subtitle"],
        "INTRO_PARAGRAPH": row["intro_paragraph"],
        "CRITERIA_1": row["criteria_1"],
        "CRITERIA_2": row["criteria_2"],
        "CRITERIA_3": row["criteria_3"],
        "FAQ_Q1": row["faq_q1"], "FAQ_A1": row["faq_a1"],
        "FAQ_Q2": row["faq_q2"], "FAQ_A2": row["faq_a2"],
        "FAQ_Q3": row["faq_q3"], "FAQ_A3": row["faq_a3"],
        "RELATED_PAGE_TITLE": row["related_page_title"],
        "RELATED_PAGE_SLUG": row["related_page_slug"],
        "RELATED_PAGE_BLURB": row["related_page_blurb"],
        "CTA_SUBTITLE": row["cta_subtitle"],
        "TARGET_KEYWORD": row["target_keyword"],
        "SERVICE_CATEGORY": row["service_category"],
        "DATE_PUBLISHED": datetime.date.today().isoformat(),
    }
    for token, value in token_map.items():
        filled = filled.replace("{{" + token + "}}", value)
    return filled


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 generate_compact_pages.py <path-to-csv>")
        sys.exit(1)

    csv_path = Path(sys.argv[1])
    if not csv_path.exists():
        print(f"CSV not found: {csv_path}")
        sys.exit(1)

    OUTPUT_DIR.mkdir(exist_ok=True)
    template = load_template()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M")

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing_cols = [c for c in REQUIRED_COLUMNS if c not in reader.fieldnames]
        if missing_cols:
            print(f"CSV is missing required columns: {missing_cols}")
            sys.exit(1)

        rows_processed = 0
        rows_with_issues = 0

        print("=" * 70)
        print("DFS COMPACT KEYWORD PAGE GENERATOR")
        print("=" * 70)

        for row in reader:
            rows_processed += 1
            issues = validate_row(row)
            html = fill_template(template, row, timestamp)

            out_path = OUTPUT_DIR / f"{row['slug']}.html"
            out_path.write_text(html, encoding="utf-8")

            status = "NEEDS FIXES" if issues else "READY FOR COMPLIANCE REVIEW"
            print(f"\n[{row['slug']}] -> {out_path.name}  [{status}]")
            print(f"  Target keyword: {row['target_keyword']}")
            if issues:
                rows_with_issues += 1
                for issue in issues:
                    print(f"  - {issue}")

        print("\n" + "=" * 70)
        print(f"Generated {rows_processed} page(s) to {OUTPUT_DIR}/")
        print(f"{rows_with_issues} of {rows_processed} need fixes before compliance review")
        print("=" * 70)
        print("\nNEXT STEPS (unchanged from standard DFS process):")
        print("  1. Fix any flagged rows above and re-run")
        print("  2. Run /dfs-ad-compliance on each generated page")
        print("  3. Get proof approval before pushing")
        print("  4. Push approved pages to repo ROOT (not posts/.../live/)")
        print("  5. Add each new slug to sitemap.xml")


if __name__ == "__main__":
    main()
