# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LEXICON_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "shabad_dohe_lexicon.json")

lex = json.load(open(LEXICON_PATH, encoding='utf-8'))
placeholders = [k for k, v in lex.items() if 'प्रभु-वचन' in v.get('hi', '') or 'holy word' in v.get('en', '')]
print(f"Total placeholder words in Shabad+Dohe: {len(placeholders)}")
print("Sample 50 placeholder words:")
for w in placeholders[:50]:
    print(f"  {w}")
