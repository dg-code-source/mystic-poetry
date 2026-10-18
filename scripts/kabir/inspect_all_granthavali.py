# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/kabir_all_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

ramainis = [x for x in items if x['type'] == 'kabir_ramaini']
sakhis = [x for x in items if x['type'] == 'kabir_sakhi']
pads = [x for x in items if x['type'] == 'kabir_pad']

print("=== RAMAINIS ===")
for r in ramainis:
    first_few = " / ".join(r['lines'][:2])
    print(f"Ramaini {r['num']} | ID: {r['id']} | Title: {r['title_hi']} | Lines: {len(r['lines'])}")
    print(f"   Opening: {first_few[:70]}")

print("\n=== SAKHI ANGS (All 59) ===")
for s in sakhis:
    ang = s.get('ang_name', s['title_hi'])
    cnt = s.get('couplets_count', len(s['lines']) // 2)
    first_few = " / ".join(s['lines'][:2]) if s['lines'] else ""
    print(f"Sakhi {s['num']} | ID: {s['id']} | Ang: {ang} | Couplets: {cnt} | Lines: {len(s['lines'])}")
    print(f"   Opening: {first_few[:70]}")

print("\n=== PAD RAAGS (All 17) ===")
for p in pads:
    raag = p.get('raag_name', p['title_hi'])
    first_few = " / ".join(p['lines'][:2]) if p['lines'] else ""
    print(f"Pad {p['num']} | ID: {p['id']} | Raag: {raag} | Lines: {len(p['lines'])}")
    print(f"   Opening: {first_few[:70]}")
