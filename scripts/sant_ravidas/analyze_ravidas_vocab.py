# -*- coding: utf-8 -*-
"""
Analyzes Sant Ravidas Ji's 4,273 unique vocabulary tokens:
- Identifies case endings (-हु, -हि, -इ, -उ, -ै)
- Maps to base Hindi & English
- Identifies top frequency words in Shabad, Padaavali, and Dohe
"""

import os
import sys
import json
import re
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_DIR = os.path.join(BASE_DIR, "data", "sant_ravidas", "raw")
WORDS_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "words_to_translate.json")

words = json.load(open(WORDS_PATH, encoding='utf-8'))
print(f"Total unique tokens: {len(words)}")

# Count token frequency across all poems
word_counts = Counter()
for fn in ["shabad.json", "padaavali.json", "dohe.json"]:
    data = json.load(open(os.path.join(RAW_DIR, fn), encoding='utf-8'))
    for item in data:
        for l in item.get("lines", []):
            toks = re.findall(r'[\u0900-\u097F]+', l)
            for t in toks:
                ct = re.sub(r'[\s।॥,\.\?\!\:\-\(\)\"\'०-९0-9]+', '', t).strip()
                if ct:
                    word_counts[ct] += 1

print("\nTop 50 most frequent words in Sant Ravidas works:")
for w, cnt in word_counts.most_common(50):
    print(f"  {w:15} -> {cnt} times")

# Classify suffixes
case_u = [w for w in words if w.endswith('ु') or w.endswith('उ')]
case_i = [w for w in words if w.endswith('ि') or w.endswith('इ')]
case_ai = [w for w in words if w.endswith('ै')]
case_hu = [w for w in words if w.endswith('हु')]
case_hi = [w for w in words if w.endswith('हि')]

print("\nGrammatical morphological patterns in Sant Ravidas:")
print(f"  - Ends with -उ/-ु (nominative/abstract noun marker): {len(case_u)}")
print(f"  - Ends with -इ/-ि (locative/oblique marker): {len(case_i)}")
print(f"  - Ends with -ै (present tense / ergative marker): {len(case_ai)}")
print(f"  - Ends with -हु (ablative/plural vocative): {len(case_hu)}")
print(f"  - Ends with -हि (accusative/dative/3rd pl.): {len(case_hi)}")
