# -*- coding: utf-8 -*-
import json
import collections
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
base = os.path.join(BASE_DIR, 'data', 'sant_ravidas', 'raw', 'padaavali.json')
padas = json.load(open(base, encoding='utf-8'))
freq = collections.Counter()
for p in padas:
    for l in p.get('lines', []):
        for w in re.findall(r'[\u0900-\u097F]+', l):
            cw = re.sub(r'[\s।॥,\.\?\!\:\-\(\)\"\'०-९0-9]+', '', w).strip()
            if cw:
                freq[cw] += 1

missing = json.load(open(os.path.join(BASE_DIR, 'data', 'sant_ravidas', 'padaavali_unresolved.json'), encoding='utf-8'))
top = [(w, freq[w]) for w in missing if freq[w] >= 5]
print(f"Words with frequency >= 5: {len(top)}")
for w, c in sorted(top, key=lambda x: x[1], reverse=True)[:50]:
    print(f"  {w:15} -> {c}")
