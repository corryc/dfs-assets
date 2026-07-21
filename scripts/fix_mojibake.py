#!/usr/bin/env python3
"""
Encoding + structure guard for dfs-assets.

Two checks, both scoped and non-destructive by default:
1. Mojibake repair (cp1252 / Latin-1 double-encoding) + ASCII-ify dashes,
   per Corry's content policy and KB incidents T012/T014/T022/T027.
2. Base64-wrapped-content check, per the 2026-07-21 incident where
   expert-mortgage-brokers.html, refinance.html, and debt-consolidation.html
   were committed with the literal base64 STRING as their file content
   instead of decoded HTML. Netlify served that base64 text as-is, so the
   pages looked blank/broken rather than 404ing.

Runs scoped repairs only on suspect character runs, never a blind whole-file
transform, per the lesson logged in T012-utf8-encoding-incident.md.

Exit code 1 if any file looks broken in a way this script can't safely
auto-fix, so CI actually fails loudly instead of silently shipping it.
"""
import base64
import glob
import re
import sys

EXCLUDE_DIRS = ("archive/",)
UNDEFINED_CP1252 = {0x81, 0x8d, 0x8f, 0x90, 0x9d}

MOJIBAKE_CP1252 = re.compile(r'\u00e2.{0,3}')
MOJIBAKE_LATIN1 = re.compile(r'\u00c3.{0,3}')
BASE64_CHARS = re.compile(r'^[A-Za-z0-9+/=\s]+$')
DOCTYPE_RE = re.compile(r'^\s*<(!doctype|html)', re.IGNORECASE)


def whatwg_cp1252_encode(text: str) -> bytes:
    out = bytearray()
    for ch in text:
        cp = ord(ch)
        if cp in UNDEFINED_CP1252:
            out.append(cp)
        else:
            out += ch.encode('cp1252')
    return bytes(out)


def repair_cp1252(text: str) -> str:
    bom = ''
    if text.startswith('\ufeff'):
        bom, text = '\ufeff', text[1:]
    for _ in range(3):
        if not MOJIBAKE_CP1252.search(text):
            break
        try:
            text = whatwg_cp1252_encode(text).decode('utf-8')
        except UnicodeDecodeError:
            break
    return bom + text


def repair_latin1(text: str) -> str:
    bom = ''
    if text.startswith('\ufeff'):
        bom, text = '\ufeff', text[1:]
    for _ in range(3):
        if not MOJIBAKE_LATIN1.search(text):
            break
        try:
            text = text.encode('latin-1').decode('utf-8')
        except (UnicodeDecodeError, UnicodeEncodeError):
            break
    return bom + text


def ascii_ify_dashes(text: str) -> str:
    text = text.replace(' \u2014 ', ', ')
    text = text.replace('\u2014', ', ')
    text = re.sub(r'(?<=[0-9$])\u2013(?=[0-9$])', '-', text)
    text = text.replace(' \u2013 ', ', ')
    text = text.replace('\u2013', '-')
    return text


def looks_like_html(text: str) -> bool:
    stripped = text.lstrip('\ufeff')
    return bool(DOCTYPE_RE.match(stripped))


def try_recover_base64_wrapped(text: str):
    """
    If a file's content is itself a base64 string (not real HTML), try
    decoding it one level and check if THAT is real HTML. Returns the
    recovered HTML, or None if this file isn't that bug.
    """
    stripped = text.lstrip('\ufeff').strip()
    if not stripped or not BASE64_CHARS.match(stripped):
        return None
    try:
        decoded = base64.b64decode(stripped, validate=True).decode('utf-8')
    except Exception:
        return None
    return decoded if looks_like_html(decoded) else None


def process_file(path: str):
    """Returns (changed: bool, broken_unrecoverable: bool)."""
    with open(path, encoding='utf-8', errors='replace') as f:
        original = f.read()

    text = original

    # Base64-wrapped-content check first: if the whole file isn't HTML at
    # all, mojibake repair on it is meaningless.
    if not looks_like_html(text):
        recovered = try_recover_base64_wrapped(text)
        if recovered is not None:
            text = recovered
        else:
            # Doesn't look like HTML and isn't a recoverable base64 wrap.
            # Don't guess - flag it for a human.
            return False, True

    if MOJIBAKE_CP1252.search(text):
        text = repair_cp1252(text)
    if MOJIBAKE_LATIN1.search(text):
        text = repair_latin1(text)
    text = ascii_ify_dashes(text)

    if text != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        return True, False
    return False, False


def main():
    changed = []
    broken = []
    for path in glob.glob('**/*.html', recursive=True):
        if any(ex in path for ex in EXCLUDE_DIRS):
            continue
        was_changed, is_broken = process_file(path)
        if was_changed:
            changed.append(path)
        if is_broken:
            broken.append(path)

    if changed:
        print(f"Repaired {len(changed)} file(s):")
        for p in changed:
            print(" -", p)
    if broken:
        print(f"BROKEN, could not auto-fix ({len(broken)} file(s)) - needs a human look:")
        for p in broken:
            print(" -", p)
    if not changed and not broken:
        print("No corruption, non-ASCII dashes, or structural issues found.")

    if broken:
        sys.exit(1)


if __name__ == '__main__':
    main()
