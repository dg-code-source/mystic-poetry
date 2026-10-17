# -*- coding: utf-8 -*-
import json
import collections
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'data/sant_ravidas/raw'
freq = collections.Counter()
for fn in ['shabad.json', 'padaavali.json', 'dohe.json']:
    data = json.load(open(os.path.join(base, fn), encoding='utf-8'))
    for item in data:
        for l in item.get('lines', []):
            words = re.findall(r'[\u0900-\u097F]+', l)
            for w in words:
                cw = re.sub(r'[\s।॥,\.\?\!\:\-\(\)\"\'०-९0-9]+', '', w).strip()
                if cw:
                    freq[cw] += 1

unresolved = set(json.load(open('data/sant_ravidas/unresolved_tokens.json', encoding='utf-8')))
top_unresolved = [(w, c) for w, c in freq.most_common() if w in unresolved]
print(f"Total unresolved: {len(unresolved)}")
print(f"Top 50 most frequent unresolved words:")
for w, c in top_unresolved[:60]:
    print(f"  {w}: {c}")
