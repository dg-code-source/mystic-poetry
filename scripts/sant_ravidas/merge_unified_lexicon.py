# -*- coding: utf-8 -*-
import json
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SD_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "shabad_dohe_lexicon.json")
PADA_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "padaavali_lexicon.json")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "ravidas_lexicon.json")

sd = json.load(open(SD_PATH, encoding='utf-8'))
pada = json.load(open(PADA_PATH, encoding='utf-8'))

unified = {}
# Padaavali first, then override with hand-tuned Shabad-Dohe
for k, v in pada.items():
    unified[k] = v
for k, v in sd.items():
    unified[k] = v

FIXES = {
    "द्रौपदी": {"roman": "draupadee", "hi": "भक्त द्रौपदी जी", "en": "devotee Draupadi"},
    "किस": {"roman": "kis", "hi": "किस जन को/किसको", "en": "unto whom/whom"},
    "कहाँ": {"roman": "kahaan", "hi": "किस स्थान पर/कहाँ", "en": "in what place/where"},
    "यह": {"roman": "yah", "hi": "यह संसार/यह देह", "en": "this realm/this body"},
    "ऊपर": {"roman": "oopar", "hi": "ऊपर/मस्तक पर", "en": "above/upon"},
    "किन": {"roman": "kin", "hi": "किन लोगों ने/किनको", "en": "by whom/unto whom"},
}
for k, v in FIXES.items():
    unified[k] = v

print(f"Unified Ravidas Lexicon total tokens: {len(unified)}")

# Run global audit
errs = []
for k, v in unified.items():
    hi = v.get("hi", "")
    en = v.get("en", "")
    rom = v.get("roman", "")
    if not hi or not en or not rom:
        errs.append(f"{k}: missing field")
    if hi == k:
        errs.append(f"{k}: hi == token")
    if re.search(r'[\u0900-\u097F]', en):
        errs.append(f"{k}: Devanagari in en ({en})")

print(f"Total validation errors in Unified Ravidas Lexicon: {len(errs)}")
if errs:
    print(errs[:20])
else:
    print("SUCCESS: Unified Ravidas Lexicon passed 100% with 0 errors!")
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(unified, f, ensure_ascii=False, indent=2)
    print(f"Saved unified lexicon to {OUTPUT_PATH}")
