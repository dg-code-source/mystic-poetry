# -*- coding: utf-8 -*-
"""
Generates web-ready normalized datasets for Baba Bulleh Shah Interactive Web App:
- data/manifest.js & data/manifest.json (50 KB index for fast search & listing)
- data/kafian_data.js & data/kafian_data.json (Complete unified study database)
"""

import os
import json
import glob
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
KAFIAN_DIR = os.path.join(DATA_DIR, "kafian")

def get_section(k_id):
    if 1 <= k_id <= 50:
        return "भाग 1 (काफ़ियां 1–50)"
    elif 51 <= k_id <= 100:
        return "भाग 2 (काफ़ियां 51–100)"
    else:
        return "भाग 3 (काफ़ियां 101–160)"

def normalize_kafi(k):
    k_id = k["id"]
    title = (k.get("title") or k.get("title_punjabi") or "").strip()
    if not re.match(r'^\d+\.', title):
        title = f"{k_id}. {title}"
    
    stanzas = []
    original_verses = []
    
    if "original_poem" in k and k["original_poem"]:
        original_verses = [line.strip() for line in k["original_poem"].strip().split("\n") if line.strip()]

    if "annotated_stanzas" in k:
        for s in k["annotated_stanzas"]:
            lines = []
            for l in s.get("lines", []):
                orig = l.get("original", "").strip()
                lines.append({
                    "original": orig,
                    "hindi_gloss": l.get("hindi_gloss", "").strip(),
                    "english_gloss": l.get("english_gloss", "").strip()
                })
                if not original_verses and orig:
                    original_verses.append(orig)
            
            hi_m = s.get("hindi_meaning", "")
            en_m = s.get("english_meaning", "")
            hi_lines = [x.strip() for x in hi_m.split("\n") if x.strip()] if isinstance(hi_m, str) else hi_m
            en_lines = [x.strip() for x in en_m.split("\n") if x.strip()] if isinstance(en_m, str) else en_m
            stanzas.append({
                "lines": lines,
                "poetic_hindi": hi_lines,
                "poetic_english": en_lines
            })
    elif "stanzas" in k:
        for s in k["stanzas"]:
            orig = s.get("original", [])
            hi_g = s.get("hindi_gloss", [])
            en_g = s.get("english_gloss", [])
            if isinstance(hi_g, str):
                hi_g = [x.strip() for x in hi_g.split("\n") if x.strip()]
            if isinstance(en_g, str):
                en_g = [x.strip() for x in en_g.split("\n") if x.strip()]
            
            lines = []
            max_l = max(len(orig), len(hi_g), len(en_g))
            for i in range(max_l):
                ol = orig[i].strip() if i < len(orig) else ""
                hl = hi_g[i].strip() if i < len(hi_g) else ""
                el = en_g[i].strip() if i < len(en_g) else ""
                lines.append({
                    "original": ol,
                    "hindi_gloss": hl,
                    "english_gloss": el
                })
                if not original_verses and ol:
                    original_verses.append(ol)
            
            hi_m = s.get("poetic_hindi", [])
            en_m = s.get("poetic_english", [])
            if isinstance(hi_m, str):
                hi_m = [x.strip() for x in hi_m.split("\n") if x.strip()]
            if isinstance(en_m, str):
                en_m = [x.strip() for x in en_m.split("\n") if x.strip()]
            
            stanzas.append({
                "lines": lines,
                "poetic_hindi": hi_m,
                "poetic_english": en_m
            })

    if not original_verses:
        for s in stanzas:
            for l in s["lines"]:
                if l["original"]:
                    original_verses.append(l["original"])

    commentary = k.get("sufi_commentary") or k.get("philosophical_meaning") or ""
    
    return {
        "id": k_id,
        "title": title,
        "title_english": k.get("title_english", "").strip(),
        "section": get_section(k_id),
        "raga": k.get("raga", "").strip(),
        "meter": k.get("meter", "").strip(),
        "theme": k.get("theme", "").strip(),
        "historical_context": k.get("historical_context", "").strip(),
        "original_verses": original_verses,
        "stanzas": stanzas,
        "commentary": commentary.strip()
    }

def main():
    files = sorted(glob.glob(os.path.join(KAFIAN_DIR, "kafi_*.json")))
    print(f"Found {len(files)} files in {KAFIAN_DIR}")
    
    manifest = []
    data_store = {}
    
    for fpath in files:
        with open(fpath, "r", encoding="utf-8") as f:
            raw = json.load(f)
        norm = normalize_kafi(raw)
        k_id = norm["id"]
        data_store[str(k_id)] = norm
        
        first_line = norm["original_verses"][0] if norm["original_verses"] else ""
        manifest.append({
            "id": k_id,
            "title": norm["title"],
            "title_english": norm["title_english"],
            "section": norm["section"],
            "raga": norm["raga"],
            "first_line": first_line
        })
    
    manifest.sort(key=lambda x: x["id"])
    
    # Save manifest.json & manifest.js
    m_json_path = os.path.join(DATA_DIR, "manifest.json")
    with open(m_json_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    
    m_js_path = os.path.join(DATA_DIR, "manifest.js")
    with open(m_js_path, "w", encoding="utf-8") as f:
        f.write("window.BULLEH_SHAH_MANIFEST = " + json.dumps(manifest, ensure_ascii=False, indent=2) + ";\n")
        
    # Save kafian_data.json & kafian_data.js
    d_json_path = os.path.join(DATA_DIR, "kafian_data.json")
    with open(d_json_path, "w", encoding="utf-8") as f:
        json.dump(data_store, f, ensure_ascii=False)
        
    d_js_path = os.path.join(DATA_DIR, "kafian_data.js")
    with open(d_js_path, "w", encoding="utf-8") as f:
        f.write("window.BULLEH_SHAH_DATA = " + json.dumps(data_store, ensure_ascii=False) + ";\n")
        
    print(f"Manifest written: {m_js_path} ({os.path.getsize(m_js_path) // 1024} KB)")
    print(f"Data store written: {d_js_path} ({os.path.getsize(d_js_path) // 1024} KB)")
    print("Done!")

if __name__ == "__main__":
    main()
