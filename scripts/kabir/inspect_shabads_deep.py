# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/kabir_all_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

shabads = [x for x in items if x['type'] == 'kabir_shabad']
print(f"Total Shabads: {len(shabads)}")

# Let's inspect their titles, first lines, and line counts
for s in shabads:
    first_line = s['lines'][0] if s['lines'] else ""
    rahaau = [l for l in s['lines'] if 'रहाउ' in l]
    rahaau_str = rahaau[0] if rahaau else (s['lines'][1] if len(s['lines']) > 1 else "")
    last_line = s['lines'][-1] if s['lines'] else ""
    print(f"ID: {s['id']} | Num: {s['num']} | Title: {s['title_hi'][:30]}")
    print(f"   First: {first_line[:50]}")
    print(f"   Rahaau: {rahaau_str[:50]}")
    print(f"   Last: {last_line[:50]}")
