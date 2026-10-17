# -*- coding: utf-8 -*-
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

sh = json.load(open('data/sant_ravidas/raw/shabad.json', encoding='utf-8'))
doh = json.load(open('data/sant_ravidas/raw/dohe.json', encoding='utf-8'))

words = set()
for item in sh + doh:
    for l in item.get('lines', []):
        toks = re.findall(r'[\u0900-\u097F]+', l)
        for t in toks:
            ct = re.sub(r'[\s।॥,\.\?\!\:\-\(\)\"\'०-९0-9]+', '', t).strip()
            if ct:
                words.add(ct)

print(f"Combined unique words in Shabad + Dohe: {len(words)}")
with open('data/sant_ravidas/words_shabad_dohe.json', 'w', encoding='utf-8') as f:
    json.dump(sorted(list(words)), f, ensure_ascii=False, indent=2)
