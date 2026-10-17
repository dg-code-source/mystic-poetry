# -*- coding: utf-8 -*-
import json
import collections
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
base = os.path.join(BASE_DIR, 'data', 'sant_ravidas', 'raw')
freq = collections.Counter()
for fn in ['shabad.json', 'padaavali.json', 'dohe.json']:
    data = json.load(open(os.path.join(base, fn), encoding='utf-8'))
    for item in data:
        for l in item.get('lines', []):
            for w in re.findall(r'[\u0900-\u097F]+', l):
                cw = re.sub(r'[\s।॥,\.\?\!\:\-\(\)\"\'०-९0-9]+', '', w).strip()
                if cw:
                    freq[cw] += 1

unresolved = set(json.load(open(os.path.join(BASE_DIR, 'data', 'sant_ravidas', 'still_unresolved.json'), encoding='utf-8')))
top = [(w, c) for w, c in freq.most_common() if w in unresolved]
print('Top 50 most frequent still unresolved:')
for w, c in top[:50]:
    print(f'  {w}: {c}')
