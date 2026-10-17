import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("data/kabir/kabir_data.json", "r", encoding="utf-8") as f:
    items = json.load(f)

# Genre normalization for manifest and data
genre_map = {
    "kabir_shabad": ("shabad", "शब्द"),
    "kabir_salok": ("salok", "सलोक"),
    "kabir_doha": ("doha", "दोहा"),
    "kabir_ramaini": ("ramaini", "रमैणी"),
    "kabir_sakhi": ("sakhi", "साखी अंग"),
    "kabir_pad": ("pad", "पद राग")
}

manifest = []
data_dict = {}

for it in items:
    raw_type = it["type"]
    short_genre, genre_label = genre_map.get(raw_type, (raw_type, "रचना"))
    num = it.get("num", 1)
    uid = f"kabir_{short_genre}_{num}"
    
    # Original lines
    orig_lines = it.get("original_text", "").split("\n")
    first_line = orig_lines[0] if orig_lines else it["title_hi"]
    
    # Gloss lines
    gloss = it.get("glossary", {})
    hi_gloss_lines = gloss.get("hindi", "").split("\n") if gloss.get("hindi") else []
    en_gloss_lines = gloss.get("english", "").split("\n") if gloss.get("english") else []
    
    # Manifest entry
    manifest_entry = {
        "uid": uid,
        "poet": "sant-kabir",
        "poet_name": "संत कबीर दास",
        "genre": short_genre,
        "genre_label": genre_label,
        "id": num,
        "title": it["title_hi"],
        "theme": it["title_hi"],
        "theme_en": it["title"],
        "first_line": first_line
    }
    manifest.append(manifest_entry)
    
    # Data entry
    data_entry = {
        "uid": uid,
        "poet": "sant-kabir",
        "poet_name": "संत कबीर दास",
        "genre": short_genre,
        "genre_label": genre_label,
        "id": num,
        "title": it["title_hi"],
        "theme": it["title_hi"],
        "theme_en": it["title"],
        "first_line": first_line,
        "lines": orig_lines,
        "hindi_gloss": hi_gloss_lines,
        "english_gloss": en_gloss_lines,
        "translation_hindi": it["verse_hi"],
        "translation_english": it["verse_en"],
        "commentary": it["meaning"],
        "tags": it.get("tags", ["Sant Kabir", "Nirguna Bhakti"])
    }
    data_dict[uid] = data_entry

# Write manifest.js
out_manifest_path = "data/kabir/kabir_manifest.js"
with open(out_manifest_path, "w", encoding="utf-8") as f:
    f.write("/**\n * Sant Kabir Das Master Manifest (562 Works)\n */\n")
    f.write("window.KABIR_MANIFEST = ")
    json.dump(manifest, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Generated {out_manifest_path} with {len(manifest)} entries ({os.path.getsize(out_manifest_path)} bytes)")

# Write kabir_data.js
out_data_js_path = "data/kabir/kabir_data.js"
with open(out_data_js_path, "w", encoding="utf-8") as f:
    f.write("/**\n * Sant Kabir Das Master Data Store (562 Works)\n */\n")
    f.write("window.KABIR_DATA = ")
    json.dump(data_dict, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Generated {out_data_js_path} with {len(data_dict)} entries ({os.path.getsize(out_data_js_path)} bytes)")

# Also update kabir_data.json as a dictionary for easy server/build consumption
out_data_json_path = "data/kabir/kabir_data.json"
with open(out_data_json_path, "w", encoding="utf-8") as f:
    json.dump(data_dict, f, ensure_ascii=False, indent=2)

print(f"Updated {out_data_json_path} with {len(data_dict)} entries ({os.path.getsize(out_data_json_path)} bytes)")
