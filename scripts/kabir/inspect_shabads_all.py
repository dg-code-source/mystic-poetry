# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/kabir_all_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

shabads = [x for x in items if x['type'] == 'kabir_shabad']
for s in shabads[:5]:
    print(f"\n==================== SHABAD {s['num']} ====================")
    print(f"Title: {s['title_hi']}")
    print("\n".join(s['lines']))
