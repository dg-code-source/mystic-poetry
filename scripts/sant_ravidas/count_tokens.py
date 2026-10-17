# -*- coding: utf-8 -*-
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for fn, label in [('shabad.json', 'Shabad (40)'), ('dohe.json', 'Dohe (51)'), ('padaavali.json', 'Padaavali (117)')]:
    data = json.load(open('data/sant_ravidas/raw/' + fn, encoding='utf-8'))
    words = set()
    for item in data:
        for l in item.get('lines', []):
            toks = re.findall(r'[\u0900-\u097F]+', l)
            for t in toks:
                ct = re.sub(r'[\s।॥,\.\?\!\:\-\(\)\"\'०-९0-9]+', '', t).strip()
                if ct:
                    words.add(ct)
    print(f"{label}: {len(words)} unique tokens")
