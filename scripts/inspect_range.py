import json
import os

with open("data/raw_kafian.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

with open("data/temp_inspect.txt", "w", encoding="utf-8") as out:
    for k in raw:
        if 26 <= k["id"] <= 30:
            out.write(f"=== KAFI {k['id']}: {k['title']} ===\n")
            out.write(f"Section: {k.get('section', '')}\n")
            for i, st in enumerate(k.get("stanzas", []), 1):
                out.write(f"-- Stanza {i} --\n")
                out.write("\n".join(st) + "\n\n")
            out.write("=" * 60 + "\n\n")



print("Wrote to data/temp_inspect.txt")


