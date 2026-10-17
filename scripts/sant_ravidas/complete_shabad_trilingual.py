# -*- coding: utf-8 -*-
"""
Generator for Sant_Ravidas_Shabad_Trilingual.md:
All 40 Shabad of Sant Ravidas Ji preserved in Sri Guru Granth Sahib Ji.
Includes:
1. Original Devanagari Text
2. Word-by-word Hindi Gloss (using verified shabad_dohe_lexicon.json)
3. Word-by-word English Gloss (Roman transliteration + 0 Devanagari in meanings)
4. Metered Hindi Poetic Translation
5. Metered English Poetic Translation
6. In-depth Socio-Spiritual & Philosophical Commentary
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "raw", "shabad.json")
OUTPUT_MD = os.path.join(BASE_DIR, "Sant_Ravidas_Shabad_Trilingual.md")

sys.path.append(os.path.join(BASE_DIR, "scripts", "sant_ravidas"))
from ravidas_gloss_engine import generate_ravidas_gloss
from shabad_translations_data import SHABAD_DATA

shabads = json.load(open(RAW_PATH, encoding='utf-8'))
print(f"Loaded {len(shabads)} Shabad compositions.")

print("Building Sant_Ravidas_Shabad_Trilingual.md...")

md_out = []
md_out.append("# संत रविदास जी: आदि ग्रंथ के 40 शब्द (Sant Ravidas: 40 Shabad of Sri Guru Granth Sahib Ji)\n")
md_out.append("### त्रिभाषी संपूर्ण महाग्रंथ: मूल देवनागरी, पदच्छेद, शब्दार्थ, काव्यानुवाद एवं दार्शनिक मीमांसा\n")
md_out.append("> **ग्रंथ परिचय**: सिखों के परम पावन धर्मग्रंथ **'श्री गुरु ग्रंथ साहिब जी' (SGGS)** में संत शिरोमणि रविदास जी के कुल **40 पवित्र शब्द (Hymns)** और **1 सलोक** 16 रागों के अंतर्गत अंग 345 से अंग 1428 तक पूर्ण श्रद्धा और सम्मान के साथ संकलित हैं। यह संस्करण प्रत्येक शब्द के राग, अंग, मूल पद, त्रिभाषी शब्दार्थ (0 Devanagari in English), छंदोबद्ध अनुवाद और दार्शनिक व्याख्या को समेटे हुए है।\n\n---\n")

# Table of Contents
md_out.append("## 📜 विषय-सूची (Table of Contents - 40 Shabad)\n\n| क्र.सं. | शब्द का शीर्षक (Title) | राग (Raga) | आदि ग्रंथ अंग (Ang) | मुख्य विषय (Theme) |\n|---|---|---|---|---|\n")

for item in shabads:
    s_id = item["id"]
    title = item["title"]
    clean_t = re.sub(r'^\d+\.\s*', '', title).strip()
    data = SHABAD_DATA.get(s_id, {})
    raga = data.get("raga", "राग")
    ang = data.get("ang", 345)
    theme = data.get("theme", clean_t)
    md_out.append(f"| {s_id} | [{clean_t}](#shabad-{s_id}) | {raga} | Ang {ang} | {theme} |\n")

md_out.append("\n---\n\n")

# Process each Shabad
for item in shabads:
    s_id = item["id"]
    title = item["title"]
    clean_t = re.sub(r'^\d+\.\s*', '', title).strip()
    data = SHABAD_DATA.get(s_id, {})
    raga = data.get("raga", "राग")
    ang = data.get("ang", 345)
    theme = data.get("theme", clean_t)
    lines = item.get("lines", [])
    
    md_out.append(f"<a name=\"shabad-{s_id}\"></a>\n")
    md_out.append(f"## शब्द {s_id}: {clean_t}\n")
    md_out.append(f"**राग:** {raga} | **आदि ग्रंथ अंग (Ang):** {ang} | **केंद्रीय भाव:** {theme}\n\n")
    
    # 1. Original Text
    md_out.append("### 📜 मूल रचना (Original Text - Devanagari)\n```text\n")
    for l in lines:
        md_out.append(f"{l}\n")
    md_out.append("```\n\n")
    
    # 2. Word by word gloss
    md_out.append("### 🔍 पदच्छेद एवं त्रिभाषी शब्दार्थ (Word-by-Word Trilingual Gloss)\n\n")
    for idx, l in enumerate(lines, 1):
        clean_line = re.sub(r'[\d॥।]+$', '', l).strip()
        hi_gloss, en_gloss = generate_ravidas_gloss(clean_line)
        md_out.append(f"**चरण {idx}:** `{clean_line}`  \n")
        md_out.append(f"- **हिन्दी शब्दार्थ:** {hi_gloss}  \n")
        md_out.append(f"- **English Gloss:** {en_gloss}  \n\n")
    
    # 3. Poetic translations & Commentary
    hi_verse = data.get("hi_v", "")
    en_verse = data.get("en_v", "")
    comm = data.get("comm", "")
    
    md_out.append("### ✍️ पद्यानुवाद (Poetic Translations)\n\n")
    md_out.append("#### 🇮🇳 हिन्दी काव्यानुवाद\n```text\n")
    md_out.append(f"{hi_verse}\n```\n\n")
    md_out.append("#### 🇬🇧 Poetic English Translation\n```text\n")
    md_out.append(f"{en_verse}\n```\n\n")
    md_out.append(f"{comm}\n\n")
    md_out.append("[⬆️ वापस विषय-सूची पर जाएं](#-विषय-सूची-table-of-contents---40-shabad)\n\n---\n\n")

with open(OUTPUT_MD, "w", encoding="utf-8") as f:
    f.writelines(md_out)

print(f"Successfully generated {OUTPUT_MD} ({os.path.getsize(OUTPUT_MD)} bytes)")
