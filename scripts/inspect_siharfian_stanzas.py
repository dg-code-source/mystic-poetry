import sys, json
sys.stdout.reconfigure(encoding='utf-8')

s = json.load(open('data/raw_extracted/siharfian.json', encoding='utf-8'))
for c_idx, cycle in enumerate(s, 1):
    print(f"=== Cycle {c_idx}: {cycle['cycle']} ===")
    for st_idx, st in enumerate(cycle['stanzas'][:5], 1):
        print(f"  Stanza {st_idx}: {st['letter']} ({len(st['lines'])} lines)")
        print(f"    Line 1: {st['lines'][0]}")
