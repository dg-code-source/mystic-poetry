# -*- coding: utf-8 -*-
"""
Compiles structured Web Application Data for Sant Ravidas Ji's 208 Works:
- 40 आदि ग्रंथ शब्द (Shabad)
- 117 अमर पद (Padaavali)
- 51 अमर दोहे (Dohe)

Generates:
1. data/sant_ravidas/ravidas_manifest.js
2. data/sant_ravidas/ravidas_data.js
3. data/sant_ravidas/ravidas_data.json
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(BASE_DIR, "scripts", "sant_ravidas"))

from ravidas_gloss_engine import generate_ravidas_gloss
from dohe_translations_data import DOHE_DATA
from shabad_translations_data import SHABAD_DATA
from padaavali_translations_data import PADAAVALI_DATA

RAW_SHABAD = os.path.join(BASE_DIR, "data", "sant_ravidas", "raw", "shabad.json")
RAW_DOHE = os.path.join(BASE_DIR, "data", "sant_ravidas", "raw", "dohe.json")
RAW_PADA = os.path.join(BASE_DIR, "data", "sant_ravidas", "raw", "padaavali.json")

MANIFEST_JS = os.path.join(BASE_DIR, "data", "sant_ravidas", "ravidas_manifest.js")
DATA_JS = os.path.join(BASE_DIR, "data", "sant_ravidas", "ravidas_data.js")
DATA_JSON = os.path.join(BASE_DIR, "data", "sant_ravidas", "ravidas_data.json")

shabads = json.load(open(RAW_SHABAD, encoding='utf-8'))
dohe = json.load(open(RAW_DOHE, encoding='utf-8'))
padas = json.load(open(RAW_PADA, encoding='utf-8'))

assert len(shabads) == 40, f"Expected 40 shabads, got {len(shabads)}"
assert len(dohe) == 51, f"Expected 51 dohe, got {len(dohe)}"
assert len(padas) == 117, f"Expected 117 padas, got {len(padas)}"

assert len(SHABAD_DATA) == 40, f"Expected 40 in SHABAD_DATA, got {len(SHABAD_DATA)}"
assert len(DOHE_DATA) == 51, f"Expected 51 in DOHE_DATA, got {len(DOHE_DATA)}"
assert len(PADAAVALI_DATA) == 117, f"Expected 117 in PADAAVALI_DATA, got {len(PADAAVALI_DATA)}"

all_items = []
manifest = []

# 1. Process 40 Shabad
for item in shabads:
    s_id = item["id"]
    title = item["title"]
    clean_t = re.sub(r'^\d+\.\s*', '', title).strip()
    s_info = SHABAD_DATA[s_id]
    raga = s_info.get("raga", "राग गउड़ी")
    ang = s_info.get("ang", 345)
    theme = s_info.get("theme", clean_t)
    lines = item.get("lines", [])
    
    hi_glosses = []
    en_glosses = []
    for l in lines:
        cl = re.sub(r'[\d॥।]+$', '', l).strip()
        hg, eg = generate_ravidas_gloss(cl)
        hi_glosses.append(hg)
        en_glosses.append(eg)
        
    hi_v = s_info["hi_v"].strip()
    en_v = s_info["en_v"].strip()
    comm = s_info["comm"].strip()
    uid = f"ravidas_shabad_{s_id}"
    
    entry = {
        "uid": uid,
        "poet": "sant_ravidas",
        "poet_name": "संत रविदास जी",
        "genre": "shabad",
        "genre_label": "आदि ग्रंथ शब्द",
        "id": s_id,
        "title": f"शब्द {s_id}: {clean_t}",
        "raga": raga,
        "ang": ang,
        "theme": theme,
        "first_line": lines[0] if lines else "",
        "lines": lines,
        "hindi_gloss": hi_glosses,
        "english_gloss": en_glosses,
        "hindi_translation": hi_v,
        "english_translation": en_v,
        "commentary": comm
    }
    all_items.append(entry)
    manifest.append({
        "uid": uid,
        "poet": "sant_ravidas",
        "poet_name": "संत रविदास जी",
        "genre": "shabad",
        "genre_label": "आदि ग्रंथ शब्द",
        "id": s_id,
        "title": f"शब्द {s_id}: {clean_t}",
        "raga": raga,
        "ang": ang,
        "theme": theme,
        "first_line": lines[0] if lines else ""
    })

print(f"Processed {len(shabads)} Shabad.")

# 2. Process 51 Dohe
for item in dohe:
    d_id = item["id"]
    lines = item.get("lines", [])
    first_l = lines[0] if lines else f"दोहा {d_id}"
    clean_fl = re.sub(r'[\d॥।]+$', '', first_l).strip()
    
    d_info = DOHE_DATA[d_id]
    theme_hi = d_info.get("theme_hi", f"आत्म-ज्ञान एवं भक्ति (दोहा {d_id})")
    hi_v = d_info["hi_v"].strip()
    en_v = d_info["en_v"].strip()
    comm = d_info["comm"].strip()
    
    hi_glosses = []
    en_glosses = []
    for l in lines:
        cl = re.sub(r'[\d॥।]+$', '', l).strip()
        hg, eg = generate_ravidas_gloss(cl)
        hi_glosses.append(hg)
        en_glosses.append(eg)
        
    uid = f"ravidas_dohe_{d_id}"
    entry = {
        "uid": uid,
        "poet": "sant_ravidas",
        "poet_name": "संत रविदास जी",
        "genre": "dohe",
        "genre_label": "साखी दोहे",
        "id": d_id,
        "title": f"दोहा {d_id}: {clean_fl}",
        "raga": "",
        "ang": None,
        "theme": theme_hi,
        "first_line": clean_fl,
        "lines": lines,
        "hindi_gloss": hi_glosses,
        "english_gloss": en_glosses,
        "hindi_translation": hi_v,
        "english_translation": en_v,
        "commentary": comm
    }
    all_items.append(entry)
    manifest.append({
        "uid": uid,
        "poet": "sant_ravidas",
        "poet_name": "संत रविदास जी",
        "genre": "dohe",
        "genre_label": "साखी दोहे",
        "id": d_id,
        "title": f"दोहा {d_id}: {clean_fl}",
        "raga": "",
        "ang": None,
        "theme": theme_hi,
        "first_line": clean_fl
    })

print(f"Processed {len(dohe)} Dohe.")

# 3. Process 117 Padaavali
for item in padas:
    p_id = item["id"]
    title = item.get("title", f"पद {p_id}")
    clean_t = re.sub(r'[\d॥।]+$', '', title).strip()
    lines = item.get("lines", [])
    
    p_info = PADAAVALI_DATA[p_id]
    theme_hi = p_info.get("theme_hi", f"आत्म-निवेदन एवं हरि-भक्ति (पद {p_id})")
    hi_v = p_info["hi_v"].strip()
    en_v = p_info["en_v"].strip()
    comm = p_info["comm"].strip()
    
    # Try to extract Raga if present in lines
    raga_match = None
    for l in lines:
        m = re.search(r'\((राग [^)]+)\)', l)
        if m:
            raga_match = m.group(1)
            break
    raga_str = raga_match if raga_match else "राग आधारित"
    
    hi_glosses = []
    en_glosses = []
    for l in lines:
        cl = re.sub(r'[\d॥।]+$', '', l).strip()
        hg, eg = generate_ravidas_gloss(cl)
        hi_glosses.append(hg)
        en_glosses.append(eg)
        
    uid = f"ravidas_padaavali_{p_id}"
    entry = {
        "uid": uid,
        "poet": "sant_ravidas",
        "poet_name": "संत रविदास जी",
        "genre": "padaavali",
        "genre_label": "अमर पद",
        "id": p_id,
        "title": f"पद {p_id}: {clean_t}",
        "raga": raga_str,
        "ang": None,
        "theme": theme_hi,
        "first_line": lines[0] if lines else clean_t,
        "lines": lines,
        "hindi_gloss": hi_glosses,
        "english_gloss": en_glosses,
        "hindi_translation": hi_v,
        "english_translation": en_v,
        "commentary": comm
    }
    all_items.append(entry)
    manifest.append({
        "uid": uid,
        "poet": "sant_ravidas",
        "poet_name": "संत रविदास जी",
        "genre": "padaavali",
        "genre_label": "अमर पद",
        "id": p_id,
        "title": f"पद {p_id}: {clean_t}",
        "raga": raga_str,
        "ang": None,
        "theme": theme_hi,
        "first_line": lines[0] if lines else clean_t
    })

print(f"Processed {len(padas)} Padaavali.")
print(f"Total Sant Ravidas compositions: {len(all_items)} (Manifest: {len(manifest)})")

# Save JSON
with open(DATA_JSON, "w", encoding="utf-8") as f:
    json.dump(all_items, f, ensure_ascii=False, indent=2)

# Save JS Manifest
with open(MANIFEST_JS, "w", encoding="utf-8") as f:
    f.write("window.RAVIDAS_MANIFEST = ")
    json.dump(manifest, f, ensure_ascii=False)
    f.write(";\n")

# Save JS Data as dictionary keyed by uid
data_dict = {item["uid"]: item for item in all_items}
with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write("window.RAVIDAS_DATA = ")
    json.dump(data_dict, f, ensure_ascii=False)
    f.write(";\n")

print(f"Successfully compiled:")
print(f"  - {MANIFEST_JS} ({os.path.getsize(MANIFEST_JS)} bytes)")
print(f"  - {DATA_JS} ({os.path.getsize(DATA_JS)} bytes)")
print(f"  - {DATA_JSON} ({os.path.getsize(DATA_JSON)} bytes)")
