import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("data/kabir/kabir_data.json", "r", encoding="utf-8") as f:
    items = json.load(f)

genre_map = {
    "kabir_shabad": "शब्द",
    "kabir_salok": "सलोक",
    "kabir_doha": "दोहा",
    "kabir_ramaini": "रमैणी",
    "kabir_sakhi": "साखी अंग",
    "kabir_pad": "पद राग"
}

manifest = []
for item in items:
    genre = item["type"]
    first_line = item["original_text"].split("\n")[0] if item.get("original_text") else item["title_hi"]
    
    entry = {
        "uid": item["id"],
        "poet": "sant_kabir",
        "poet_name": "संत कबीर दास",
        "genre": genre,
        "genre_label": genre_map.get(genre, "रचना"),
        "id": item.get("num", 1),
        "title": item["title_hi"],
        "theme": item["title_hi"],
        "theme_en": item["title"],
        "first_line": first_line
    }
    manifest.append(entry)

out_manifest_path = "data/kabir/kabir_manifest.js"
with open(out_manifest_path, "w", encoding="utf-8") as f:
    f.write("/**\n * Sant Kabir Das Master Manifest (562 Works)\n */\n")
    f.write("window.KABIR_MANIFEST = ")
    json.dump(manifest, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Generated {out_manifest_path} with {len(manifest)} entries ({os.path.getsize(out_manifest_path)} bytes)")
