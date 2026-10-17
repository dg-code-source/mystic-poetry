# -*- coding: utf-8 -*-
"""
Builds the complete unified database and manifest for Baba Bulleh Shah's Entire Works:
- 160 Kafian
- 12 Baranmah
- 7 Athwara
- 40 Gandhan
- 76 Siharfian (3 cycles)
- 56 Dohre
Total: 351 Masterpieces
Generates:
- data/manifest.js & data/manifest.json
- data/all_works_data.js & data/all_works_data.json
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
OTHER_DIR = os.path.join(DATA_DIR, "other_works")

# Load existing 160 Kafian data
with open(os.path.join(DATA_DIR, "kafian_data.json"), "r", encoding="utf-8") as f:
    kafian_data = json.load(f)

# Load other works
with open(os.path.join(OTHER_DIR, "baranmah.json"), "r", encoding="utf-8") as f:
    baranmah_data = json.load(f)

with open(os.path.join(OTHER_DIR, "athwara.json"), "r", encoding="utf-8") as f:
    athwara_data = json.load(f)

with open(os.path.join(OTHER_DIR, "gandhan.json"), "r", encoding="utf-8") as f:
    gandhan_data = json.load(f)

with open(os.path.join(OTHER_DIR, "dohre.json"), "r", encoding="utf-8") as f:
    dohre_data = json.load(f)

with open(os.path.join(OTHER_DIR, "siharfian.json"), "r", encoding="utf-8") as f:
    siharfian_data = json.load(f)

manifest = []
unified_store = {}

# 1. Add 160 Kafian
for k_id_str, k in kafian_data.items():
    k_id = int(k_id_str)
    item_key = f"kafi_{k_id}"
    
    first_line = k["original_verses"][0] if k.get("original_verses") else ""
    manifest_item = {
        "uid": item_key,
        "genre": "kafi",
        "genre_label": "काफ़ियां",
        "id": k_id,
        "title": k["title"],
        "title_english": k.get("title_english", ""),
        "section": k.get("section", ""),
        "raga": k.get("raga", ""),
        "first_line": first_line
    }
    manifest.append(manifest_item)
    
    # Store with both key and numeric id for full backward compatibility
    k_copy = dict(k)
    k_copy["uid"] = item_key
    k_copy["genre"] = "kafi"
    k_copy["genre_label"] = "काफ़ियां"
    unified_store[item_key] = k_copy
    unified_store[str(k_id)] = k_copy

# 2. Add Baranmah (12 months)
for m in baranmah_data:
    m_id = m["id"]
    item_key = f"baranmah_{m_id}"
    
    orig_verses = [l["original"] for l in m["lines_annotated"]]
    lines_annotated = [{
        "original": l["original"],
        "hindi_gloss": l["hindi_gloss"],
        "english_gloss": l["english_gloss"]
    } for l in m["lines_annotated"]]
    
    store_item = {
        "uid": item_key,
        "genre": "baranmah",
        "genre_label": "बारहमाह",
        "id": m_id,
        "title": f"बारहमाह: {m['month']}",
        "title_english": m["english_title"],
        "section": "बारहमाह (12 मास)",
        "theme": m["mystical_theme"],
        "season": m["season"],
        "original_verses": orig_verses,
        "stanzas": [{
            "lines": lines_annotated,
            "poetic_hindi": m["poetic_hindi"],
            "poetic_english": m["poetic_english"]
        }],
        "commentary": m["sufi_commentary"]
    }
    unified_store[item_key] = store_item
    manifest.append({
        "uid": item_key,
        "genre": "baranmah",
        "genre_label": "बारहमाह",
        "id": m_id,
        "title": f"बारहमाह: {m['month']}",
        "title_english": m["english_title"],
        "section": "बारहमाह",
        "first_line": orig_verses[0] if orig_verses else ""
    })

# 3. Add Athwara (7 days)
for d in athwara_data:
    d_id = d["id"]
    item_key = f"athwara_{d_id}"
    
    orig_verses = [l["original"] for l in d["lines_annotated"]]
    lines_annotated = [{
        "original": l["original"],
        "hindi_gloss": l["hindi_gloss"],
        "english_gloss": l["english_gloss"]
    } for l in d["lines_annotated"]]
    
    store_item = {
        "uid": item_key,
        "genre": "athwara",
        "genre_label": "अठवारा",
        "id": d_id,
        "title": f"अठवारा: {d['day']}",
        "title_english": d["english_title"],
        "section": "अठवारा (7 वार)",
        "theme": d["mystical_theme"],
        "original_verses": orig_verses,
        "stanzas": [{
            "lines": lines_annotated,
            "poetic_hindi": d["poetic_hindi"],
            "poetic_english": d["poetic_english"]
        }],
        "commentary": d["sufi_commentary"]
    }
    unified_store[item_key] = store_item
    manifest.append({
        "uid": item_key,
        "genre": "athwara",
        "genre_label": "अठवारा",
        "id": d_id,
        "title": f"अठवारा: {d['day']}",
        "title_english": d["english_title"],
        "section": "अठवारा",
        "first_line": orig_verses[0] if orig_verses else ""
    })

# 4. Add Dohre (56 couplets)
for d in dohre_data:
    d_id = d["id"]
    item_key = f"dohre_{d_id}"
    
    orig_verses = [l["original"] for l in d["lines_annotated"]]
    lines_annotated = [{
        "original": l["original"],
        "hindi_gloss": l["hindi_gloss"],
        "english_gloss": l["english_gloss"]
    } for l in d["lines_annotated"]]
    
    store_item = {
        "uid": item_key,
        "genre": "dohre",
        "genre_label": "दोहरे",
        "id": d_id,
        "title": d["title"],
        "title_english": f"Couplet {d_id}",
        "section": "दोहरे (1–56)",
        "theme": d["theme"],
        "original_verses": orig_verses,
        "stanzas": [{
            "lines": lines_annotated,
            "poetic_hindi": d["poetic_hindi"],
            "poetic_english": d["poetic_english"]
        }],
        "commentary": d["sufi_commentary"]
    }
    unified_store[item_key] = store_item
    manifest.append({
        "uid": item_key,
        "genre": "dohre",
        "genre_label": "दोहरे",
        "id": d_id,
        "title": d["title"],
        "title_english": f"Couplet {d_id}",
        "section": "दोहरे",
        "first_line": orig_verses[0] if orig_verses else ""
    })

# 5. Add Gandhan (40 knots)
for g in gandhan_data:
    g_id = g["id"]
    item_key = f"gandhan_{g_id}"
    
    orig_verses = [l["original"] for l in g["lines_annotated"]]
    lines_annotated = [{
        "original": l["original"],
        "hindi_gloss": l["hindi_gloss"],
        "english_gloss": l["english_gloss"]
    } for l in g["lines_annotated"]]
    
    store_item = {
        "uid": item_key,
        "genre": "gandhan",
        "genre_label": "गन्धां",
        "id": g_id,
        "title": f"गंढ {g_id}",
        "title_english": f"Knot {g_id}",
        "section": "गन्धां (40 गाँठें)",
        "theme": g["theme"],
        "original_verses": orig_verses,
        "stanzas": [{
            "lines": lines_annotated,
            "poetic_hindi": g["poetic_hindi"],
            "poetic_english": g["poetic_english"]
        }],
        "commentary": g["sufi_commentary"]
    }
    unified_store[item_key] = store_item
    manifest.append({
        "uid": item_key,
        "genre": "gandhan",
        "genre_label": "गन्धां",
        "id": g_id,
        "title": f"गंढ {g_id}",
        "title_english": f"Knot {g_id}",
        "section": "गन्धां",
        "first_line": orig_verses[0] if orig_verses else ""
    })

# 6. Add Siharfian (76 letter stanzas)
s_counter = 1
for cycle in siharfian_data:
    c_name = cycle["cycle_name"]
    refrain = cycle.get("refrain", "")
    for s in cycle["stanzas"]:
        letter = s["letter"]
        item_key = f"siharfi_{s_counter}"
        
        orig_verses = [l["original"] for l in s["lines_annotated"]]
        lines_annotated = [{
            "original": l["original"],
            "hindi_gloss": l["hindi_gloss"],
            "english_gloss": l["english_gloss"]
        } for l in s["lines_annotated"]]
        
        store_item = {
            "uid": item_key,
            "genre": "siharfian",
            "genre_label": "सीहरफ़ियां",
            "id": s_counter,
            "cycle": c_name,
            "letter": letter,
            "title": f"{letter} ({c_name})",
            "title_english": f"Letter {letter}",
            "section": c_name,
            "refrain": refrain,
            "original_verses": orig_verses,
            "stanzas": [{
                "lines": lines_annotated,
                "poetic_hindi": s["poetic_hindi"],
                "poetic_english": s["poetic_english"]
            }],
            "commentary": s["sufi_commentary"]
        }
        unified_store[item_key] = store_item
        manifest.append({
            "uid": item_key,
            "genre": "siharfian",
            "genre_label": "सीहरफ़ियां",
            "id": s_counter,
            "title": f"{letter} ({c_name})",
            "title_english": f"Letter {letter}",
            "section": c_name,
            "first_line": orig_verses[0] if orig_verses else ""
        })
        s_counter += 1

print(f"Total manifest items: {len(manifest)}")
print(f"Total unified store keys: {len(unified_store)}")

# Write manifest files
m_json_path = os.path.join(DATA_DIR, "manifest.json")
with open(m_json_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

m_js_path = os.path.join(DATA_DIR, "manifest.js")
with open(m_js_path, "w", encoding="utf-8") as f:
    f.write("window.BULLEH_SHAH_MANIFEST = " + json.dumps(manifest, ensure_ascii=False) + ";\n")

# Write data store files
d_json_path = os.path.join(DATA_DIR, "kafian_data.json")
with open(d_json_path, "w", encoding="utf-8") as f:
    json.dump(unified_store, f, ensure_ascii=False)

d_js_path = os.path.join(DATA_DIR, "kafian_data.js")
with open(d_js_path, "w", encoding="utf-8") as f:
    f.write("window.BULLEH_SHAH_DATA = " + json.dumps(unified_store, ensure_ascii=False) + ";\n")

print(f"Manifest written: {m_js_path} ({os.path.getsize(m_js_path) // 1024} KB)")
print(f"Data store written: {d_js_path} ({os.path.getsize(d_js_path) // 1024} KB)")
