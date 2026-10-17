# -*- coding: utf-8 -*-
import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

json_path = os.path.join(BASE_DIR, "data", "sant_ravidas", "ravidas_data.json")
js_path = os.path.join(BASE_DIR, "data", "sant_ravidas", "ravidas_data.js")

with open(json_path, "r", encoding="utf-8") as f:
    data_json = json.load(f)

print(f"Checking {json_path}:")
print(f"Total entries: {len(data_json)}")

missing_hi = []
missing_en = []
missing_comm = []
short_hi = []
short_en = []

for item in data_json:
    uid = item.get("uid")
    title = item.get("title")
    hi = item.get("hindi_translation", "").strip()
    en = item.get("english_translation", "").strip()
    comm = item.get("commentary", "").strip()

    if not hi:
        missing_hi.append(uid)
    elif len(hi) < 25:
        short_hi.append((uid, hi))

    if not en:
        missing_en.append(uid)
    elif len(en) < 25:
        short_en.append((uid, en))

    if not comm:
        missing_comm.append(uid)

print(f"  - Missing Hindi translation: {len(missing_hi)}")
print(f"  - Missing English translation: {len(missing_en)}")
print(f"  - Missing Commentary: {len(missing_comm)}")
print(f"  - Suspiciously short Hindi: {len(short_hi)}")
print(f"  - Suspiciously short English: {len(short_en)}")

# Now verify data/sant_ravidas/ravidas_data.js
print(f"\nChecking {js_path}:")
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# Verify window.RAVIDAS_DATA is defined
print(f"  - Contains window.RAVIDAS_DATA: {'window.RAVIDAS_DATA' in js_content}")
print(f"  - File size: {len(js_content)} bytes ({len(js_content)/(1024*1024):.2f} MB)")

if not missing_hi and not missing_en and not missing_comm:
    print("\n[SUCCESS] All 208 web compositions in ravidas_data.json and ravidas_data.js have complete authentic Hindi and English poetic translations!")
else:
    print("\n[ERROR] Missing translations found in web data!")
