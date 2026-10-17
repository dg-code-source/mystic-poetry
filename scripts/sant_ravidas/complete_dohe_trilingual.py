# -*- coding: utf-8 -*-
"""
Generator for Sant_Ravidas_Dohe_Trilingual.md:
All 51 Amar Dohe / Sakhis of Sant Ravidas Ji.
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
RAW_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "raw", "dohe.json")
OUTPUT_MD = os.path.join(BASE_DIR, "content", "sant_ravidas", "Sant_Ravidas_Dohe_Trilingual.md")

sys.path.append(os.path.join(BASE_DIR, "scripts", "sant_ravidas"))
from ravidas_gloss_engine import generate_ravidas_gloss

dohe = json.load(open(RAW_PATH, encoding='utf-8'))
print(f"Loaded {len(dohe)} Dohe compositions.")

from dohe_translations_data import DOHE_DATA

print("Building Sant_Ravidas_Dohe_Trilingual.md...")

md_out = []
md_out.append("# संत रविदास जी: 51 अमर दोहे (Sant Ravidas: 51 Immortal Sakhis & Couplets)\n")
md_out.append("### त्रिभाषी संपूर्ण ग्रंथ: मूल दोहा, पदच्छेद, शब्दार्थ, काव्यानुवाद एवं सामाजिक-दार्शनिक मीमांसा\n")
md_out.append("> **ग्रंथ परिचय**: संत शिरोमणि रविदास जी के दोहे (साखियां) भारतीय समाज में समता, श्रम की प्रतिष्ठा, जाति-विनाश और निर्गुण भक्ति की अमर क्रांति हैं। इस त्रिभाषी संस्करण में प्रत्येक दोहे का मूल पाठ, पदच्छेद, शब्दार्थ (0 Devanagari in English gloss), पद्यानुवाद और गहन दार्शनिक विवेचन प्रस्तुत किया गया है।\n\n---\n")

# Table of Contents
md_out.append("## 📜 विषय-सूची (Table of Contents - 51 Dohe)\n\n| दोहा सं. | प्रथम पंक्ति (First Line) | केंद्रीय विषय (Core Theme) |\n|---|---|---|\n")

for d in dohe:
    d_id = d["id"]
    lines = d.get("lines", [])
    first_l = lines[0] if lines else f"दोहा {d_id}"
    clean_fl = re.sub(r'[\d॥।]+$', '', first_l).strip()
    theme_hi = DOHE_DATA.get(d_id, {}).get("theme_hi", f"आत्म-ज्ञान एवं भक्ति (दोहा {d_id})")
    md_out.append(f"| {d_id} | [{clean_fl}](#doha-{d_id}) | {theme_hi} |\n")

md_out.append("\n---\n\n")

# Process each Doha
for d in dohe:
    d_id = d["id"]
    lines = d.get("lines", [])
    first_l = lines[0] if lines else f"दोहा {d_id}"
    clean_fl = re.sub(r'[\d॥।]+$', '', first_l).strip()
    
    d_info = DOHE_DATA.get(d_id, {})
    theme_hi = d_info.get("theme_hi", f"आत्म-ज्ञान एवं प्रभु-भक्ति (दोहा {d_id})")
    theme_en = d_info.get("theme_en", f"Self-Realization & Devotion (Couplet {d_id})")
    hi_v = d_info.get("hi_v", "")
    en_v = d_info.get("en_v", "")
    comm_txt = d_info.get("comm", "")
    
    md_out.append(f"<a name=\"doha-{d_id}\"></a>\n")
    md_out.append(f"## दोहा {d_id}: {clean_fl}\n")
    md_out.append(f"**केंद्रीय विषय:** {theme_hi} ({theme_en})\n\n")
    
    # 1. Original Text
    md_out.append("### 📜 मूल दोहा (Original Couplet - Devanagari)\n```text\n")
    for l in lines:
        md_out.append(f"{l}\n")
    md_out.append("```\n\n")
    
    # 2. Word by word gloss
    md_out.append("### 🔍 पदच्छेद एवं त्रिभाषी शब्दार्थ (Word-by-Word Trilingual Gloss)\n\n")
    for idx, l in enumerate(lines, 1):
        clean_line = re.sub(r'[\d॥।]+$', '', l).strip()
        hi_gloss, en_gloss = generate_ravidas_gloss(clean_line)
        md_out.append(f"**पंक्ति {idx}:** `{clean_line}`  \n")
        md_out.append(f"- **हिन्दी शब्दार्थ:** {hi_gloss}  \n")
        md_out.append(f"- **English Gloss:** {en_gloss}  \n\n")
        
    # 3. Poetic Verse & Commentary
    md_out.append("### ✍️ पद्यानुवाद (Poetic Translations)\n\n")
    md_out.append("#### 🇮🇳 हिन्दी भावार्थ एवं काव्यानुवाद\n```text\n")
    md_out.append(f"{hi_v}\n```\n\n")
    md_out.append("#### 🇬🇧 Poetic English Translation\n```text\n")
    md_out.append(f"{en_v}\n```\n\n")
    md_out.append(f"{comm_txt}\n\n")
    md_out.append("[⬆️ वापस विषय-सूची पर जाएं](#-विषय-सूची-table-of-contents---51-dohe)\n\n---\n\n")

with open(OUTPUT_MD, "w", encoding="utf-8") as f:
    f.writelines(md_out)

print(f"Successfully generated {OUTPUT_MD} ({os.path.getsize(OUTPUT_MD)} bytes)")
