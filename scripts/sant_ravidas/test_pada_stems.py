# -*- coding: utf-8 -*-
import json
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MISSING_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "padaavali_unresolved.json")
MASTER_PATH = os.path.join(BASE_DIR, "data", "master_complete_bilingual_lexicon.json")
LEX_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "shabad_dohe_lexicon.json")

missing = json.load(open(MISSING_PATH, encoding='utf-8'))
master = json.load(open(MASTER_PATH, encoding='utf-8'))
lex = json.load(open(LEX_PATH, encoding='utf-8'))

combined = dict(lex)
for k, v in master.items():
    if k not in combined:
        combined[k] = v

direct_master = [w for w in missing if w in master]
print(f"Direct match in master lexicon: {len(direct_master)}")

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

stemmed = []
for w in missing:
    if w in direct_master:
        continue
    for pat, sfx_hi, sfx_en in STEM_RULES:
        if re.search(pat, w) and len(w) > 2:
            base_w = re.sub(pat, '', w)
            if base_w in combined:
                stemmed.append((w, base_w, sfx_hi, sfx_en))
                break

print(f"Stem match in combined: {len(stemmed)}")
unresolved = [w for w in missing if w not in direct_master and w not in [x[0] for x in stemmed]]
print(f"Remaining after master + stems: {len(unresolved)}")
