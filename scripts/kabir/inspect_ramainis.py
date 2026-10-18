# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/kabir_all_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

ramainis = [x for x in items if x['type'] == 'kabir_ramaini']
print(f"Total Ramainis: {len(ramainis)}")
for r in ramainis:
    print(f"Ramaini {r['num']}: {r['title_hi']} | Lines: {len(r['lines'])} | First: {r['lines'][0][:50] if r['lines'] else ''}")
