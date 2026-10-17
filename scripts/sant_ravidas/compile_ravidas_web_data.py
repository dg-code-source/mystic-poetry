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

RAW_SHABAD = os.path.join(BASE_DIR, "data", "sant_ravidas", "raw", "shabad.json")
RAW_DOHE = os.path.join(BASE_DIR, "data", "sant_ravidas", "raw", "dohe.json")
RAW_PADA = os.path.join(BASE_DIR, "data", "sant_ravidas", "raw", "padaavali.json")

MANIFEST_JS = os.path.join(BASE_DIR, "data", "sant_ravidas", "ravidas_manifest.js")
DATA_JS = os.path.join(BASE_DIR, "data", "sant_ravidas", "ravidas_data.js")
DATA_JSON = os.path.join(BASE_DIR, "data", "sant_ravidas", "ravidas_data.json")

shabads = json.load(open(RAW_SHABAD, encoding='utf-8'))
dohe = json.load(open(RAW_DOHE, encoding='utf-8'))
padas = json.load(open(RAW_PADA, encoding='utf-8'))

# Import SHABAD_META
from complete_shabad_trilingual import SHABAD_META, generate_shabad_commentary
from complete_dohe_trilingual import DOHE_THEMES
from complete_padaavali_trilingual import ICONIC_PADAS

all_items = []
manifest = []

# 1. Process 40 Shabad
for item in shabads:
    s_id = item["id"]
    title = item["title"]
    clean_t = re.sub(r'^\d+\.\s*', '', title).strip()
    meta = SHABAD_META.get(s_id, {"raga": "राग गउड़ी", "ang": 345, "theme": clean_t})
    lines = item.get("lines", [])
    
    hi_glosses = []
    en_glosses = []
    for l in lines:
        cl = re.sub(r'[\d॥।]+$', '', l).strip()
        hg, eg = generate_ravidas_gloss(cl)
        hi_glosses.append(hg)
        en_glosses.append(eg)
        
    hi_v, en_v, comm = generate_shabad_commentary(s_id, meta, lines)
    uid = f"ravidas_shabad_{s_id}"
    
    entry = {
        "uid": uid,
        "poet": "sant_ravidas",
        "poet_name": "संत रविदास जी",
        "genre": "shabad",
        "genre_label": "आदि ग्रंथ शब्द",
        "id": s_id,
        "title": f"शब्द {s_id}: {clean_t}",
        "raga": meta["raga"],
        "ang": meta["ang"],
        "theme": meta["theme"],
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
        "raga": meta["raga"],
        "ang": meta["ang"],
        "theme": meta["theme"],
        "first_line": lines[0] if lines else ""
    })

print(f"Processed {len(shabads)} Shabad.")

# 2. Process 51 Dohe
for item in dohe:
    d_id = item["id"]
    lines = item.get("lines", [])
    first_l = lines[0] if lines else f"दोहा {d_id}"
    clean_fl = re.sub(r'[\d॥।]+$', '', first_l).strip()
    
    theme_info = DOHE_THEMES.get(
        d_id,
        (f"आत्म-ज्ञान, सदाचार एवं प्रभु-भक्ति (दोहा {d_id})",
         f"Self-Realization & Devotion (Couplet {d_id})",
         f"""संत रविदास जी इस अमर दोहे में उपदेश देते हैं कि मनुष्य को सांसारिक अहंकार त्यागकर
सच्चे हृदय से प्रभु की आराधना करनी चाहिए और समस्त मानवता के साथ समता का व्यवहार करना चाहिए।""",
         f"""In this immortal sakhi, Sant Ravidas guides humanity to shed transient ego
and embrace the eternal light of divine contemplation and universal love.""",
         f"""### दार्शनिक विश्लेषण (Philosophical Commentary)
1. **केंद्रीय संदेश**:
   संत रविदास जी बाह्य आडंबरों, कुल-अभिमान और अंधविश्वास का खंडन कर अंतरात्मा की शुद्धि और निष्काम कर्म पर बल देते हैं।""")
    )
    
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
        "theme": theme_info[0],
        "first_line": clean_fl,
        "lines": lines,
        "hindi_gloss": hi_glosses,
        "english_gloss": en_glosses,
        "hindi_translation": theme_info[2],
        "english_translation": theme_info[3],
        "commentary": theme_info[4]
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
        "theme": theme_info[0],
        "first_line": clean_fl
    })

print(f"Processed {len(dohe)} Dohe.")

# 3. Process 117 Padaavali
for item in padas:
    p_id = item["id"]
    title = item.get("title", f"पद {p_id}")
    clean_t = re.sub(r'[\d॥।]+$', '', title).strip()
    lines = item.get("lines", [])
    
    theme_info = ICONIC_PADAS.get(
        p_id,
        (f"आत्म-निवेदन, निर्गुण भक्ति एवं आत्म-साक्षात्कार (पद {p_id})",
         f"Self-Surrender & Divine Contemplation (Pad {p_id})",
         f"""संत रविदास जी इस अमर पद में प्रभु-प्रेम की अनन्यता, मन की शुद्धि और
संसार की नश्वरता का बोध कराते हुए पूर्ण आत्म-समर्पण की प्रेरणा देते हैं।""",
         f"""In this celestial bhajan, Sant Ravidas guides the seeker to dissolve worldly illusion
and merge into the pristine ocean of divine light and boundless compassion.""",
         f"""### दार्शनिक विश्लेषण (Philosophical Commentary)
1. **मूल आध्यात्मिक संदेश**:
   संत रविदास जी बाह्य आडंबर, जातिगत अहंकार और कर्मकांडी अंधविश्वास को त्यागकर अंतःकरण की पवित्रता और प्रभु-नाम के अनन्य सिमरन पर बल देते हैं।""")
    )
    
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
        "raga": "शास्त्रीय राग",
        "ang": None,
        "theme": theme_info[0],
        "first_line": lines[0] if lines else clean_t,
        "lines": lines,
        "hindi_gloss": hi_glosses,
        "english_gloss": en_glosses,
        "hindi_translation": theme_info[2],
        "english_translation": theme_info[3],
        "commentary": theme_info[4]
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
        "raga": "शास्त्रीय राग",
        "ang": None,
        "theme": theme_info[0],
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
