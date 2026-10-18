# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/kabir_all_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

pads = [x for x in items if x['type'] == 'kabir_pad']
print(f"Total Pad Raags: {len(pads)}")
for p in pads:
    print(f"Pad {p['num']}: {p['title_hi'][:40]} | Lines: {len(p['lines'])}")
