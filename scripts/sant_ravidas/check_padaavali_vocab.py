# -*- coding: utf-8 -*-
import json
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PADA_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "raw", "padaavali.json")
LEX_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "shabad_dohe_lexicon.json")

padas = json.load(open(PADA_PATH, encoding='utf-8'))
lex = json.load(open(LEX_PATH, encoding='utf-8'))

words_pada = set()
for p in padas:
    for l in p.get("lines", []):
        for w in re.findall(r'[\u0900-\u097F]+', l):
            cw = re.sub(r'[\s।॥,\.\?\!\:\-\(\)\"\'०-९0-9]+', '', w).strip()
            if cw:
                words_pada.add(cw)

print(f"Total unique tokens in Padaavali (117 Padas): {len(words_pada)}")
in_lex = [w for w in words_pada if w in lex]
missing = [w for w in words_pada if w not in lex]
print(f"Already covered by Shabad-Dohe lexicon: {len(in_lex)} / {len(words_pada)} ({len(in_lex)/len(words_pada)*100:.1f}%)")
print(f"Remaining Padaavali tokens: {len(missing)}")

with open(os.path.join(BASE_DIR, "data", "sant_ravidas", "padaavali_unresolved.json"), "w", encoding="utf-8") as f:
    json.dump(sorted(missing), f, ensure_ascii=False, indent=2)
