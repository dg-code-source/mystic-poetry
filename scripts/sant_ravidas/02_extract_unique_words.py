# -*- coding: utf-8 -*-
"""
Extracts all unique vocabulary tokens across the 208 works of Sant Ravidas Ji
(40 Shabad, 117 Padaavali, 51 Dohe).
Normalizes punctuation and numeric dandas.
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_DIR = os.path.join(BASE_DIR, "data", "sant_ravidas", "raw")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "words_to_translate.json")

all_words = set()

for fn in ["shabad.json", "padaavali.json", "dohe.json"]:
    path = os.path.join(RAW_DIR, fn)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for item in data:
        for l in item.get("lines", []):
            words = re.findall(r'[\u0900-\u097F]+', l)
            for w in words:
                cw = re.sub(r'[\s।॥,\.\?\!\:\-\(\)\"\'०-९0-9]+', '', w).strip()
                if cw:
                    all_words.add(cw)

sorted_words = sorted(list(all_words))
print(f"Total unique vocabulary tokens in Sant Ravidas works: {len(sorted_words)}")

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(sorted_words, f, ensure_ascii=False, indent=2)

print(f"Saved unique vocabulary list to {OUTPUT_PATH}")
