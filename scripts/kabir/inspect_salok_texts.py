import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect Saloks 1 to 20 to see their exact texts
with open('data/kabir/raw/kabir_all_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

saloks = [x for x in items if x['type'] == 'kabir_salok']
print(f"Saloks count: {len(saloks)}")

for s in saloks[190:209]:
    print(f"--- SALOK {s['num']} ---")
    print("\n".join(s['lines']))


