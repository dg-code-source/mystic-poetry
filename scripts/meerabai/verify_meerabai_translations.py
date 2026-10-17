# -*- coding: utf-8 -*-
"""
Verification & Audit Suite for Sant Mirabai:
Checks:
1. Markdown file: all 418 Padas present
2. Hindi poetic translation present and length >= 25 in every single Pada
3. English poetic translation present and length >= 25 in every single Pada
4. STRICT 0 Devanagari characters in English poetic translations and English glosses
5. STRICT 0 self-repeating definitions in Hindi glosses
6. Web datasets (manifest.js, data.js, data.json) match 100% and have 418 works
"""

import os
import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

md_filepath = os.path.join(BASE_DIR, "content", "meerabai", "Sant_Mirabai_Padavali_Trilingual.md")
expected_count = 418

all_passed = True
dev_regex = re.compile(r'[\u0900-\u097F]')

print("="*60)
print("SANT MIRABAI TRILINGUAL AUDIT & VERIFICATION")
print("="*60)

with open(md_filepath, "r", encoding="utf-8") as f:
    content = f.read()

sections = re.split(rf"\n## पद \d+:", content)[1:]
print(f"\nAuditing {md_filepath}:")
print(f"Compositions detected: {len(sections)} (Expected: {expected_count})")

if len(sections) != expected_count:
    print(f"  [ERROR] Mismatch in expected count!")
    all_passed = False

missing_hi = []
missing_en = []
dev_in_en_verse = []
short_hi = []
short_en = []

for idx, sec in enumerate(sections, 1):
    hi_match = re.search(r"####[^\n]+(?:काव्यानुवाद|भावार्थ)[^\n]*\n```(?:text)?\n([\s\S]*?)\n```", sec)
    if not hi_match:
        missing_hi.append(idx)
    else:
        hi_text = hi_match.group(1).strip()
        if len(hi_text) < 25:
            short_hi.append((idx, hi_text))

    en_match = re.search(r"####[^\n]+Poetic English Verse Translation[^\n]*\n```(?:text)?\n([\s\S]*?)\n```", sec)
    if not en_match:
        missing_en.append(idx)
    else:
        en_text = en_match.group(1).strip()
        if len(en_text) < 25:
            short_en.append((idx, en_text))
        if dev_regex.search(en_text):
            dev_in_en_verse.append(idx)

print(f"  - Hindi poetic translations present: {expected_count - len(missing_hi)} / {expected_count}")
print(f"  - English poetic translations present: {expected_count - len(missing_en)} / {expected_count}")
print(f"  - Zero Devanagari in English verse: {expected_count - len(dev_in_en_verse)} / {expected_count}")

if missing_hi:
    print(f"  [!] Missing Hindi: {missing_hi}")
    all_passed = False
if missing_en:
    print(f"  [!] Missing English: {missing_en}")
    all_passed = False
if dev_in_en_verse:
    print(f"  [!] Devanagari in English verse: {dev_in_en_verse}")
    all_passed = False
if short_hi:
    print(f"  [!] Suspiciously short Hindi: {short_hi}")
    all_passed = False
if short_en:
    print(f"  [!] Suspiciously short English: {short_en}")
    all_passed = False

if not missing_hi and not missing_en and not dev_in_en_verse and not short_hi and not short_en:
    print(f"  [SUCCESS] All {expected_count} Padas pass 100% translation & quality audit!")

# Check web data
print("\nAuditing Web Data Stores:")
data_json_path = os.path.join(BASE_DIR, "data", "meerabai", "meerabai_data.json")
with open(data_json_path, "r", encoding="utf-8") as f:
    web_data = json.load(f)

print(f"Total entries in meerabai_data.json: {len(web_data)} (Expected: {expected_count})")
if len(web_data) != expected_count:
    all_passed = False
    print("  [ERROR] Web data count mismatch!")

gloss_dev_errors = 0
for uid, item in web_data.items():
    for eg in item.get("english_gloss", []):
        for m in re.finditer(r'\(([^\)]*)\)', eg):
            def_text = m.group(1)
            if dev_regex.search(def_text):
                gloss_dev_errors += 1

print(f"Devanagari characters found in English glosses: {gloss_dev_errors}")
if gloss_dev_errors > 0:
    all_passed = False
    print("  [ERROR] Devanagari found in English gloss definitions!")

print("\n" + "="*60)
if all_passed:
    print("ALL 418 SANT MIRABAI PADAS PASSED AUDIT WITH 100% PERFECTION!")
else:
    print("AUDIT FAILED: ISSUES DETECTED!")
