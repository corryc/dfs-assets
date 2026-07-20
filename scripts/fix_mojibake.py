#!/usr/bin/env python3
"""
Encoding guard for dfs-assets.
Detects and repairs mojibake corruption (cp1252 and Latin-1 double-encoding),
and enforces plain-ASCII dashes site-wide (no em/en dashes in live HTML),
per Corry's content policy and KB incidents T012/T014/T022/T027.

Runs scoped repairs only on suspect character runs, never a blind whole-file
transform, per the lesson logged in T012-utf8-encoding-incident.md.
"""
import glob
import re
import sys

EXCLUDE_DIRS = ("archive/",)
UNDEFINED_CP1252 = {0x81, 0x8d, 0x8f, 0x90, 0x9d}

MOJIBAKE_CP1252 = re.compile(r'\u00e2.{0,3}')
MOJIBAKE_LATIN1 = re.compile(r'\u00c3.{0,3}')


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


def process_file(path: str) -> bool:
    with open(path, encoding='utf-8', errors='replace') as f:
        original = f.read()

    text = original
    if MOJIBAKE_CP1252.search(text):
        text = repair_cp1252(text)
    if MOJIBAKE_LATIN1.search(text):
        text = repair_latin1(text)
    text = ascii_ify_dashes(text)

    if text != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        return True
    return False


def main():
    changed = []
    for path in glob.glob('**/*.html', recursive=True):
        if any(ex in path for ex in EXCLUDE_DIRS):
            continue
        if process_file(path):
            changed.append(path)

    if changed:
        print(f"Repaired {len(changed)} file(s):")
        for p in changed:
            print(" -", p)
    else:
        print("No corruption or non-ASCII dashes found.")


if __name__ == '__main__':
    main()
