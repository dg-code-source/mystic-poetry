# -*- coding: utf-8 -*-
"""
Compiles and audits the final, complete Shabad & Dohe Lexicon for Sant Ravidas Ji.
Ensures 100% token coverage for all 1,859 unique tokens across 40 Shabad and 51 Dohe.
Guarantees:
- 0 placeholders ('प्रभु-वचन' or 'holy word')
- 0 Devanagari in English gloss
- 0 self-repeating words in Hindi gloss
- 100% coverage
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(BASE_DIR, "scripts", "sant_ravidas"))

from vocab_slice1 import VOCAB_SLICE1
from vocab_slice2 import VOCAB_SLICE2
from vocab_slice3 import VOCAB_SLICE3
from vocab_slice4 import VOCAB_SLICE4
from vocab_extra_77 import VOCAB_EXTRA_77, FIXED_PARTICLES_19

# Load CORE_DICT
spec_path = os.path.join(BASE_DIR, "scripts", "sant_ravidas", "build_complete_ravidas_dictionary.py")
import importlib.util
spec = importlib.util.spec_from_file_location("build_dict", spec_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
core = mod.CORE_DICT

WORDS_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "words_shabad_dohe.json")
OLD_SD_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "shabad_dohe_lexicon.json")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "shabad_dohe_lexicon.json")

words = json.load(open(WORDS_PATH, encoding='utf-8'))
old_sd = json.load(open(OLD_SD_PATH, encoding='utf-8'))

# Clean old_sd to keep only genuine non-placeholder entries
valid_old = {}
for k, v in old_sd.items():
    hi = v.get("hi", "")
    en = v.get("en", "")
    if "प्रभु-वचन" not in hi and "holy word" not in en and hi != k and not re.search(r'[\u0900-\u097F]', en):
        valid_old[k] = v

print(f"Loaded {len(valid_old)} valid entries from previous lexicon.")

final_lex = {}

# 1. Base from valid_old
for k, v in valid_old.items():
    final_lex[k] = v

# 2. Add CORE_DICT
for k, (rom, hi, en) in core.items():
    final_lex[k] = {"roman": rom, "hi": hi, "en": en}

# 3. Add Slices 1 to 4
for s in [VOCAB_SLICE1, VOCAB_SLICE2, VOCAB_SLICE3, VOCAB_SLICE4]:
    for k, (rom, hi, en) in s.items():
        final_lex[k] = {"roman": rom, "hi": hi, "en": en}

# 4. Add Extra 77
for k, (rom, hi, en) in VOCAB_EXTRA_77.items():
    final_lex[k] = {"roman": rom, "hi": hi, "en": en}

# 5. Add/override Fixed Particles 19
for k, (rom, hi, en) in FIXED_PARTICLES_19.items():
    final_lex[k] = {"roman": rom, "hi": hi, "en": en}

print(f"Total entries in compiled lexicon: {len(final_lex)}")

# Verify coverage for all target words
missing = [w for w in words if w not in final_lex]
print(f"Missing tokens in Shabad + Dohe: {len(missing)}")

# Quality audit across all Shabad + Dohe words
errs = []
for w in words:
    if w not in final_lex:
        errs.append(f"{w}: Missing entirely")
        continue
    item = final_lex[w]
    hi = item.get("hi", "")
    en = item.get("en", "")
    rom = item.get("roman", "")
    if not hi or not en or not rom:
        errs.append(f"{w}: Incomplete entry")
    if hi == w:
        errs.append(f"{w}: hi == token ({hi})")
    if "प्रभु-वचन" in hi:
        errs.append(f"{w}: placeholder in hi")
    if "holy word" in en:
        errs.append(f"{w}: placeholder in en")
    if re.search(r'[\u0900-\u097F]', en):
        errs.append(f"{w}: Devanagari in en ({en})")

print(f"\n--- AUDIT RESULTS FOR ALL {len(words)} SHABAD & DOHE WORDS ---")
if errs:
    print(f"ERRORS DETECTED ({len(errs)}):")
    for e in errs[:30]:
        print(f"  {e}")
    sys.exit(1)
else:
    print("SUCCESS: 100% of all 1,859 Shabad & Dohe tokens verified with 0 errors!")
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(final_lex, f, ensure_ascii=False, indent=2)
    print(f"Saved verified lexicon to {OUTPUT_PATH}")
