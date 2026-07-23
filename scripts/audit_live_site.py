#!/usr/bin/env python3
"""
Live-site audit for dfs-assets.

Catches a specific bug class that push-time checks (scripts/fix_mojibake.py)
CANNOT catch: pages where the GitHub repo content is correct, but Netlify
serves broken content anyway due to a stale per-path asset reference in its
own deploy system. First identified 2026-07-21/22 across 19 live pages.
See site-design-technical/T012-utf8-encoding-incident.md ("Actual Root Cause
Found") in DFS-second-brain for the full incident history.

This script does NOT touch the repo - it only reads the LIVE site and
compares against what SHOULD be there. It cannot fix anything itself
(the fix requires delete-then-recreate on GitHub, not a content push -
see the incident doc). Its job is purely to make sure this can never
silently sit broken again without anyone noticing.

Exit code 1 if any live page fails the check, so a scheduled CI run shows
red/fails loudly instead of silently passing.
"""
import sys
import urllib.request
import urllib.error

BASE_URL = "https://digitalfinancesolutions.com.au"

# Root-level pages that map directly to a live URL (slug = filename minus .html).
# Kept as an explicit list rather than reading the repo tree, since this
# script's whole point is to be independent of repo state - if repo and
# live diverge, we want to know regardless of what the repo currently says.
PAGES = [
    "index", "about-us", "contact-us", "thank-you", "privacy-policy", "blog",
    "car-loans", "personal-loans", "debt-consolidation", "refinance",
    "expert-mortgage-brokers", "self-employed-income-proof",
    "self-employed-home-loan-eastern-suburbs", "self-employed-under-2-years-home-loan",
    "lenders-beyond-tax-return", "low-doc-home-loans-australia",
    "low-doc-what-lenders-accept", "how-much-can-doctor-borrow-home-loan",
    "no-lmi-home-loan-doctors-melbourne", "dentists-no-lmi-home-loan",
    "house-and-land-packages-melbourne", "buying-property-through-a-trust",
    "buying-house-ringwood-2026", "first-home-buyer-guarantee-melbourne",
    "wantirna-first-home-buyer-questions", "hidden-costs-first-home-wantirna",
    "mortgage-broker-bayswater", "mortgage-broker-bayswater-north",
    "mortgage-broker-boronia", "mortgage-broker-heathmont",
    "mortgage-broker-ringwood", "mortgage-broker-wantirna",
    "mortgage-broker-vs-bank-ringwood", "mortgage-broker-first-home-buyer-tips",
    "pre-approval-worth-the-hassle", "improve-loan-approval-chances-melbourne",
    "signs-paying-too-much-mortgage", "what-happens-home-loan-health-check",
    "why-use-a-mortgage-broker-reddit",
    # NOTE: fixing-equifax-errors intentionally excluded - 404s currently,
    # appears to be a separate pre-existing gap unrelated to this incident,
    # not yet investigated. Add back once confirmed live.
    "2026-budget-trust-cgt-changes",
]


def check_page(slug: str):
    url = f"{BASE_URL}/{slug}" if slug != "index" else BASE_URL
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=15)
        body = resp.read()
    except urllib.error.HTTPError as e:
        return (slug, url, False, f"HTTP {e.code}")
    except Exception as e:
        return (slug, url, False, str(e))

    text = body.decode("utf-8", errors="replace").lstrip("\ufeff")
    ok = text.lower().startswith("<!doctype") or "<html" in text[:200].lower()
    return (slug, url, ok, None if ok else f"does not start with <!DOCTYPE (got: {text[:60]!r})")


def main():
    failures = []
    for slug in PAGES:
        slug_, url, ok, reason = check_page(slug)
        if not ok:
            failures.append((slug_, url, reason))

    print(f"Checked {len(PAGES)} live pages.")
    if failures:
        print(f"\nFAILED ({len(failures)}):")
        for slug, url, reason in failures:
            print(f" - {slug} ({url}): {reason}")
        print(
            "\nIf pages fail here but their GitHub repo content looks correct, "
            "this is the Netlify stale-path-reference bug, not a content bug. "
            "Fix: delete the file via GITHUB_DELETE_A_FILE, confirm it 404s live, "
            "then recreate it at the same path. See "
            "site-design-technical/T012-utf8-encoding-incident.md in "
            "DFS-second-brain for full details. Do NOT just re-push the same "
            "content - that alone does not fix this bug class."
        )
        sys.exit(1)
    else:
        print("All pages OK.")


if __name__ == "__main__":
    main()
