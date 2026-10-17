# -*- coding: utf-8 -*-
"""
Full Compiler for Sant Mirabai:
Generates:
1. content/meerabai/Sant_Mirabai_Padavali_Trilingual.md (418 Padas)
2. data/meerabai/meerabai_manifest.js
3. data/meerabai/meerabai_data.js
4. data/meerabai/meerabai_data.json
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(BASE_DIR, "scripts", "meerabai"))

from meerabai_gloss_engine import generate_meerabai_gloss
from meerabai_translations_data import MEERABAI_PADA_DATA

RAW_FILE = os.path.join(BASE_DIR, "data", "meerabai", "raw", "padavali.json")

with open(RAW_FILE, "r", encoding="utf-8") as f:
    RAW_PADAS = json.load(f)

print(f"Loaded {len(RAW_PADAS)} Sant Mirabai Padas from raw dataset.")

all_web_items = []
web_manifest = []

md_lines = [
    "# संत मीराबाई: सम्पूर्ण 418 अमर पद (Sant Mirabai: Complete 418 Bhakti Padas)",
    "### त्रिभाषी संपूर्ण महाग्रंथ: मूल देवनागरी, पदच्छेद, शब्दार्थ, काव्यानुवाद एवं दार्शनिक मीमांसा",
    "> **ग्रंथ परिचय**: 16वीं सदी के भक्ति आंदोलन की अमर प्रेमावतार **संत मीराबाई (1498–1547 ई.)** की सम्पूर्ण पदावली का यह प्रामाणिक त्रिभाषी संकलन है। इसमें कुल **418 कालजयी पद** मूल राजस्थानी/डिंगल/ब्रज भाषा, पदच्छेद, त्रिभाषी शब्दार्थ (0 Devanagari in English), छंदोबद्ध हिंदी व अंग्रेजी अनुवाद और गहन दार्शनिक व्याख्या सहित प्रस्तुत हैं।",
    "",
    "---",
    "## 📜 विषय-सूची (Table of Contents - 418 Padas)",
    "",
    "| क्र.सं. | पद का शीर्षक (Title) | भाग (Part) | मुख्य विषय (Theme) |",
    "|---|---|---|---|"
]

for p in RAW_PADAS:
    pid = p["id"]
    pt = p["title"]
    part = p.get("part", 1)
    p_info = MEERABAI_PADA_DATA.get(pid) or MEERABAI_PADA_DATA.get(str(pid))
    theme_hi = p_info["theme_hi"]
    theme_en = p_info["theme_en"]
    md_lines.append(f"| {pid} | [{pt}](#pada-{pid}) | Part {part} | {theme_hi} ({theme_en}) |")

md_lines.append("\n---\n")

for p in RAW_PADAS:
    pid = p["id"]
    pt = p["title"]
    part = p.get("part", 1)
    p_info = MEERABAI_PADA_DATA.get(pid) or MEERABAI_PADA_DATA.get(str(pid))
    lines = p["lines"]
    
    hi_glosses = []
    en_glosses = []
    for l in lines:
        cl = re.sub(r'[\d॥।]+$', '', l).strip()
        hg, eg = generate_meerabai_gloss(cl)
        hi_glosses.append(hg)
        en_glosses.append(eg)
        
    hi_v = p_info["hi_v"].strip()
    en_v = p_info["en_v"].strip()
    comm = p_info["comm"].strip()
    theme_hi = p_info["theme_hi"]
    theme_en = p_info["theme_en"]
    
    md_lines.extend([
        f'<a name="pada-{pid}"></a>',
        f"## पद {pid}: {pt}",
        f"**भाग (Part):** {part} | **केंद्रीय भाव:** {theme_hi} ({theme_en})",
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
    
    uid = f"meerabai_pada_{pid}"
    web_entry = {
        "uid": uid,
        "poet": "meerabai",
        "poet_name": "संत मीराबाई",
        "genre": "padaavali",
        "genre_label": "अमर पद",
        "id": pid,
        "part": part,
        "title": f"पद {pid}: {pt}",
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
        "poet": "meerabai",
        "poet_name": "संत मीराबाई",
        "genre": "padaavali",
        "genre_label": "अमर पद",
        "id": pid,
        "part": part,
        "title": f"पद {pid}: {pt}",
        "theme": theme_hi,
        "theme_en": theme_en,
        "first_line": lines[0] if lines else ""
    })

md_path = os.path.join(BASE_DIR, "content", "meerabai", "Sant_Mirabai_Padavali_Trilingual.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))
print(f"Saved {md_path} ({os.path.getsize(md_path)} bytes)")

# Web Datasets
meerabai_data_dict = {item["uid"]: item for item in all_web_items}

manifest_js_path = os.path.join(BASE_DIR, "data", "meerabai", "meerabai_manifest.js")
with open(manifest_js_path, "w", encoding="utf-8") as f:
    f.write("/**\n * Sant Mirabai Master Manifest (418 Padas)\n */\n")
    f.write(f"window.MEERABAI_MANIFEST = {json.dumps(web_manifest, ensure_ascii=False, indent=2)};\n")
print(f"Saved {manifest_js_path} ({os.path.getsize(manifest_js_path)} bytes)")

data_js_path = os.path.join(BASE_DIR, "data", "meerabai", "meerabai_data.js")
with open(data_js_path, "w", encoding="utf-8") as f:
    f.write("/**\n * Sant Mirabai Master Data Store (418 Padas)\n */\n")
    f.write(f"window.MEERABAI_DATA = {json.dumps(meerabai_data_dict, ensure_ascii=False, indent=2)};\n")
print(f"Saved {data_js_path} ({os.path.getsize(data_js_path)} bytes)")

data_json_path = os.path.join(BASE_DIR, "data", "meerabai", "meerabai_data.json")
with open(data_json_path, "w", encoding="utf-8") as f:
    json.dump(meerabai_data_dict, f, ensure_ascii=False, indent=2)
print(f"Saved {data_json_path} ({os.path.getsize(data_json_path)} bytes)")

print(f"\n Sant Mirabai Compilation Complete: {len(all_web_items)} Padas fully generated!")
