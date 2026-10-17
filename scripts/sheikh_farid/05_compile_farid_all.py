# -*- coding: utf-8 -*-
"""
Full Compiler for Baba Sheikh Farid:
Generates:
1. content/sheikh_farid/Sheikh_Farid_Salok_Trilingual.md (130 Saloks)
2. content/sheikh_farid/Sheikh_Farid_Shabad_Trilingual.md (4 Shabads)
3. data/sheikh_farid/farid_manifest.js
4. data/sheikh_farid/farid_data.js
5. data/sheikh_farid/farid_data.json
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(BASE_DIR, "scripts", "sheikh_farid"))

from farid_gloss_engine import generate_farid_gloss
from farid_translations_data import FARID_SALOK_DATA, FARID_SHABAD_DATA

SALOK_FILE = os.path.join(BASE_DIR, "data", "sheikh_farid", "cleaned_salok.json")
SHABAD_FILE = os.path.join(BASE_DIR, "data", "sheikh_farid", "cleaned_shabad.json")

with open(SALOK_FILE, "r", encoding="utf-8") as f:
    RAW_SALOKS = json.load(f)
with open(SHABAD_FILE, "r", encoding="utf-8") as f:
    RAW_SHABADS = json.load(f)

print(f"Loaded {len(RAW_SALOKS)} Saloks and {len(RAW_SHABADS)} Shabads.")

all_web_items = []
web_manifest = []

# ==========================================
# 1. COMPILE SALOKS MARKDOWN & WEB DATA
# ==========================================
salok_md_lines = [
    "# बाबा शेख फरीद: सम्पूर्ण 130 सलोक (Baba Sheikh Farid: Complete 130 Saloks)",
    "### त्रिभाषी संपूर्ण महाग्रंथ: मूल देवनागरी, पदच्छेद, शब्दार्थ, काव्यानुवाद एवं दार्शनिक मीमांसा",
    "> **ग्रंथ परिचय**: सिखों के परम पावन धर्मग्रंथ **'श्री गुरु ग्रंथ साहिब जी' (SGGS)** में सूफी शिरोमणि बाबा शेख फरीद जी (1173–1266 ई.) के कुल **130 पावन सलोक** अंग 1377 से 1384 तक संकलित हैं। यह संस्करण प्रत्येक सलोक का मूल पाठ, त्रिभाषी शब्दार्थ (0 Devanagari in English), छंदोबद्ध हिंदी व अंग्रेजी अनुवाद और चिश्ती सूफी दार्शनिक व्याख्या को प्रस्तुत करता है।",
    "",
    "---",
    "## 📜 विषय-सूची (Table of Contents - 130 Saloks)",
    "",
    "| क्र.सं. | सलोक शीर्षक (Title) | मुख्य विषय (Theme) |",
    "|---|---|---|"
]

for s in RAW_SALOKS:
    sid = s["id"]
    st = s["title"]
    clean_t = re.sub(r'^सलोक\s+\d+:\s*', '', st).strip()
    s_info = FARID_SALOK_DATA.get(sid) or FARID_SALOK_DATA.get(str(sid))
    theme_hi = s_info["theme_hi"]
    theme_en = s_info["theme_en"]
    salok_md_lines.append(f"| {sid} | [{clean_t}](#salok-{sid}) | {theme_hi} ({theme_en}) |")

salok_md_lines.append("\n---\n")

for s in RAW_SALOKS:
    sid = s["id"]
    st = s["title"]
    clean_t = re.sub(r'^सलोक\s+\d+:\s*', '', st).strip()
    s_info = FARID_SALOK_DATA.get(sid) or FARID_SALOK_DATA.get(str(sid))
    lines = s["lines"]
    
    hi_glosses = []
    en_glosses = []
    for l in lines:
        cl = re.sub(r'[\d॥।]+$', '', l).strip()
        hg, eg = generate_farid_gloss(cl)
        hi_glosses.append(hg)
        en_glosses.append(eg)
        
    hi_v = s_info["hi_v"].strip()
    en_v = s_info["en_v"].strip()
    comm = s_info["comm"].strip()
    theme_hi = s_info["theme_hi"]
    theme_en = s_info["theme_en"]
    
    salok_md_lines.extend([
        f'<a name="salok-{sid}"></a>',
        f"## सलोक {sid}: {clean_t}",
        f"**केंद्रीय भाव:** {theme_hi} ({theme_en})",
        "",
        "### 📜 मूल रचना (Original Text - Devanagari)",
        "```text",
        "\n".join(lines),
        "```",
        "",
        "### 🔍 पदच्छेद एवं त्रिभाषी शब्दार्थ (Word-by-Word Trilingual Gloss)",
        "#### 🇮🇳 हिंदी शब्दार्थ (Hindi Word-by-Word Meaning)",
        "```text",
        "\n".join(hi_glosses),
        "```",
        "",
        "#### 🌍 English Word-by-Word Gloss (Transliteration & Meaning)",
        "```text",
        "\n".join(en_glosses),
        "```",
        "",
        "### 🌸 काव्यानुवाद एवं दार्शनिक भावार्थ (Poetic Translations & Meaning)",
        "#### 🇮🇳 छंदोबद्ध हिंदी काव्यानुवाद",
        "```text",
        hi_v,
        "```",
        "",
        "#### 🇬🇧 Poetic English Verse Translation",
        "```text",
        en_v,
        "```",
        "",
        comm,
        "",
        "---",
        ""
    ])
    
    uid = f"farid_salok_{sid}"
    web_entry = {
        "uid": uid,
        "poet": "sheikh_farid",
        "poet_name": "बाबा शेख फरीद",
        "genre": "salok",
        "genre_label": "सलोक",
        "id": sid,
        "title": f"सलोक {sid}: {clean_t}",
        "theme": theme_hi,
        "theme_en": theme_en,
        "first_line": lines[0] if lines else "",
        "lines": lines,
        "hindi_gloss": hi_glosses,
        "english_gloss": en_glosses,
        "hindi_translation": hi_v,
        "english_translation": en_v,
        "commentary": comm
    }
    all_web_items.append(web_entry)
    web_manifest.append({
        "uid": uid,
        "poet": "sheikh_farid",
        "poet_name": "बाबा शेख फरीद",
        "genre": "salok",
        "genre_label": "सलोक",
        "id": sid,
        "title": f"सलोक {sid}: {clean_t}",
        "theme": theme_hi,
        "theme_en": theme_en,
        "first_line": lines[0] if lines else ""
    })

salok_md_path = os.path.join(BASE_DIR, "content", "sheikh_farid", "Sheikh_Farid_Salok_Trilingual.md")
with open(salok_md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(salok_md_lines))
print(f"Saved {salok_md_path} ({os.path.getsize(salok_md_path)} bytes)")

# ==========================================
# 2. COMPILE SHABADS MARKDOWN & WEB DATA
# ==========================================
shabad_md_lines = [
    "# बाबा शेख फरीद: आदि ग्रंथ के 4 अमर शब्द (Baba Sheikh Farid: 4 Shabads of Sri Guru Granth Sahib Ji)",
    "### त्रिभाषी संपूर्ण महाग्रंथ: मूल देवनागरी, पदच्छेद, शब्दार्थ, काव्यानुवाद एवं दार्शनिक मीमांसा",
    "> **ग्रंथ परिचय**: सिखों के परम पावन धर्मग्रंथ **'श्री गुरु ग्रंथ साहिब जी' (SGGS)** में बाबा शेख फरीद जी के कुल **4 पावन शब्द** राग आसा (अंग 488) और राग सूही (अंग 794) में संकलित हैं। यह संस्करण प्रत्येक शब्द का राग, अंग, मूल पद, त्रिभाषी शब्दार्थ, छंदोबद्ध अनुवाद और चिश्ती सूफी दार्शनिक व्याख्या को समेटे हुए है।",
    "",
    "---",
    "## 📜 विषय-सूची (Table of Contents - 4 Shabads)",
    "",
    "| क्र.सं. | शब्द शीर्षक (Title) | राग (Raga) | आदि ग्रंथ अंग (Ang) | मुख्य विषय (Theme) |",
    "|---|---|---|---|---|"
]

for s in RAW_SHABADS:
    sid = s["id"]
    st = s["title"]
    clean_t = re.sub(r'^शब्द\s+\d+\s*', '', st).strip()
    s_info = FARID_SHABAD_DATA.get(sid) or FARID_SHABAD_DATA.get(str(sid))
    raga = s_info.get("raga", "राग आसा")
    ang = s_info.get("ang", 488)
    theme_hi = s_info["theme_hi"]
    theme_en = s_info["theme_en"]
    shabad_md_lines.append(f"| {sid} | [{st}](#shabad-{sid}) | {raga} | Ang {ang} | {theme_hi} ({theme_en}) |")

shabad_md_lines.append("\n---\n")

for s in RAW_SHABADS:
    sid = s["id"]
    st = s["title"]
    clean_t = re.sub(r'^शब्द\s+\d+\s*', '', st).strip()
    s_info = FARID_SHABAD_DATA.get(sid) or FARID_SHABAD_DATA.get(str(sid))
    lines = s["lines"]
    
    hi_glosses = []
    en_glosses = []
    for l in lines:
        cl = re.sub(r'[\d॥।]+$', '', l).strip()
        hg, eg = generate_farid_gloss(cl)
        hi_glosses.append(hg)
        en_glosses.append(eg)
        
    hi_v = s_info["hi_v"].strip()
    en_v = s_info["en_v"].strip()
    comm = s_info["comm"].strip()
    raga = s_info.get("raga", "राग आसा")
    ang = s_info.get("ang", 488)
    theme_hi = s_info["theme_hi"]
    theme_en = s_info["theme_en"]
    
    shabad_md_lines.extend([
        f'<a name="shabad-{sid}"></a>',
        f"## शब्द {sid}: {st}",
        f"**राग:** {raga} | **आदि ग्रंथ अंग (Ang):** {ang} | **केंद्रीय भाव:** {theme_hi} ({theme_en})",
        "",
        "### 📜 मूल रचना (Original Text - Devanagari)",
        "```text",
        "\n".join(lines),
        "```",
        "",
        "### 🔍 पदच्छेद एवं त्रिभाषी शब्दार्थ (Word-by-Word Trilingual Gloss)",
        "#### 🇮🇳 हिंदी शब्दार्थ (Hindi Word-by-Word Meaning)",
        "```text",
        "\n".join(hi_glosses),
        "```",
        "",
        "#### 🌍 English Word-by-Word Gloss (Transliteration & Meaning)",
        "```text",
        "\n".join(en_glosses),
        "```",
        "",
        "### 🌸 काव्यानुवाद एवं दार्शनिक भावार्थ (Poetic Translations & Meaning)",
        "#### 🇮🇳 छंदोबद्ध हिंदी काव्यानुवाद",
        "```text",
        hi_v,
        "```",
        "",
        "#### 🇬🇧 Poetic English Verse Translation",
        "```text",
        en_v,
        "```",
        "",
        comm,
        "",
        "---",
        ""
    ])
    
    uid = f"farid_shabad_{sid}"
    web_entry = {
        "uid": uid,
        "poet": "sheikh_farid",
        "poet_name": "बाबा शेख फरीद",
        "genre": "shabad",
        "genre_label": "शब्द",
        "id": sid,
        "title": f"शब्द {sid}: {st}",
        "raga": raga,
        "ang": ang,
        "theme": theme_hi,
        "theme_en": theme_en,
        "first_line": lines[0] if lines else "",
        "lines": lines,
        "hindi_gloss": hi_glosses,
        "english_gloss": en_glosses,
        "hindi_translation": hi_v,
        "english_translation": en_v,
        "commentary": comm
    }
    all_web_items.append(web_entry)
    web_manifest.append({
        "uid": uid,
        "poet": "sheikh_farid",
        "poet_name": "बाबा शेख फरीद",
        "genre": "shabad",
        "genre_label": "शब्द",
        "id": sid,
        "title": f"शब्द {sid}: {st}",
        "raga": raga,
        "ang": ang,
        "theme": theme_hi,
        "theme_en": theme_en,
        "first_line": lines[0] if lines else ""
    })

shabad_md_path = os.path.join(BASE_DIR, "content", "sheikh_farid", "Sheikh_Farid_Shabad_Trilingual.md")
with open(shabad_md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(shabad_md_lines))
print(f"Saved {shabad_md_path} ({os.path.getsize(shabad_md_path)} bytes)")

# ==========================================
# 3. COMPILE WEB DATASETS (JS & JSON)
# ==========================================
farid_data_dict = {item["uid"]: item for item in all_web_items}

manifest_js_path = os.path.join(BASE_DIR, "data", "sheikh_farid", "farid_manifest.js")
with open(manifest_js_path, "w", encoding="utf-8") as f:
    f.write("/**\n * Baba Sheikh Farid Master Manifest (134 Works)\n */\n")
    f.write(f"window.FARID_MANIFEST = {json.dumps(web_manifest, ensure_ascii=False, indent=2)};\n")
print(f"Saved {manifest_js_path} ({os.path.getsize(manifest_js_path)} bytes)")

data_js_path = os.path.join(BASE_DIR, "data", "sheikh_farid", "farid_data.js")
with open(data_js_path, "w", encoding="utf-8") as f:
    f.write("/**\n * Baba Sheikh Farid Master Data Store (134 Works)\n */\n")
    f.write(f"window.FARID_DATA = {json.dumps(farid_data_dict, ensure_ascii=False, indent=2)};\n")
print(f"Saved {data_js_path} ({os.path.getsize(data_js_path)} bytes)")

data_json_path = os.path.join(BASE_DIR, "data", "sheikh_farid", "farid_data.json")
with open(data_json_path, "w", encoding="utf-8") as f:
    json.dump(farid_data_dict, f, ensure_ascii=False, indent=2)
print(f"Saved {data_json_path} ({os.path.getsize(data_json_path)} bytes)")

print(f"\n Baba Sheikh Farid Compilation Complete: {len(all_web_items)} works (130 Salok + 4 Shabad) fully generated!")
