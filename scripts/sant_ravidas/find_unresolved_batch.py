# -*- coding: utf-8 -*-
import json
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORDS_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "words_to_translate.json")
MASTER_PATH = os.path.join(BASE_DIR, "data", "master_complete_bilingual_lexicon.json")
SD_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "shabad_dohe_lexicon.json")

words = json.load(open(WORDS_PATH, encoding='utf-8'))
master = json.load(open(MASTER_PATH, encoding='utf-8'))
sd = json.load(open(SD_PATH, encoding='utf-8'))
valid_sd = {k: v for k, v in sd.items() if 'प्रभु-वचन' not in v.get('hi', '') and 'holy word' not in v.get('en', '')}

# Import CORE_DICT from build_complete_ravidas_dictionary
import importlib.util
spec = importlib.util.spec_from_file_location("build_dict", os.path.join(BASE_DIR, "scripts", "sant_ravidas", "build_complete_ravidas_dictionary.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
core = mod.CORE_DICT

combined = {}
# 1. CORE
for k, v in core.items():
    combined[k] = {"roman": v[0], "hi": v[1], "en": v[2]}

# 2. Valid SD
for k, v in valid_sd.items():
    if k not in combined:
        combined[k] = v

# 3. Master direct
for k, v in master.items():
    if k not in combined and k in words:
        combined[k] = v

print(f"Directly resolved so far: {len([w for w in words if w in combined])} / {len(words)}")

# 4. Stem matching against combined
STEM_RULES = [
    (r'हु$', ' (से/द्वारा)', ' (from/by)'),
    (r'हि$', ' (को/में)', ' (unto/in)'),
    (r'ै$', ' (करता है/होता है)', ' (does/becomes)'),
    (r'उ$', '', ''),
    (r'ु$', '', ''),
    (r'ि$', ' (में/करके)', ' (in/having done)'),
    (r'इ$', ' (में/करके)', ' (in/having done)'),
    (r'ौ$', ' (को/ने)', ' (unto/by)'),
    (r'नि$', ' (के/में)', ' (of/in)'),
    (r'ां$', ' (बहुवचन)', ' (plural)'),
    (r'न$', ' (लोग/समूह)', ' (folk/plural)'),
    (r'ौं$', ' (करता हूँ)', ' (I do)'),
    (r'हिं$', ' (करते हैं)', ' (they do)'),
    (r'हीं$', ' (करते हैं)', ' (they do)'),
    (r'यो$', ' (किया/हुआ)', ' (done/happened)'),
    (r'या$', ' (किया/हुआ)', ' (done/happened)'),
    (r'त$', ' (करते हुए)', ' (while doing)'),
]

stem_resolved = 0
for w in words:
    if w in combined:
        continue
    for pat, sfx_hi, sfx_en in STEM_RULES:
        if re.search(pat, w) and len(w) > 2:
            base_w = re.sub(pat, '', w)
            cand = combined.get(base_w) or master.get(base_w)
            if cand:
                hi = cand.get('hi', '')
                en = cand.get('en', '')
                if hi and en and not re.search(r'[\u0900-\u097F]', en):
                    combined[w] = {
                        "roman": mod.romanize(w),
                        "hi": f"{hi}{sfx_hi}".strip(),
                        "en": f"{en}{sfx_en}".strip()
                    }
                    stem_resolved += 1
                    break

print(f"Resolved with stems: {len([w for w in words if w in combined])} / {len(words)} (stem added {stem_resolved})")

unresolved = [w for w in words if w not in combined]
print(f"Remaining unresolved: {len(unresolved)}")

with open(os.path.join(BASE_DIR, "data", "sant_ravidas", "still_unresolved.json"), "w", encoding="utf-8") as f:
    json.dump(unresolved, f, ensure_ascii=False, indent=2)
