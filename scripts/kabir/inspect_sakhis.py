# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/kabir_all_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

sakhis = [x for x in items if x['type'] == 'kabir_sakhi']
print(f"Total Sakhi Angs: {len(sakhis)}")
for s in sakhis[:20]:
    print(f"Sakhi {s['num']}: {s['title_hi'][:35]} | Lines: {len(s['lines'])}")
