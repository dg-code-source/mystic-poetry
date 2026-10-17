# -*- coding: utf-8 -*-
"""
Generator for Sant_Ravidas_Padaavali_Trilingual.md:
All 117 Amar Pad (Bhajans) of Sant Ravidas Ji.
Includes:
1. Original Devanagari Text
2. Word-by-word Hindi Gloss (using verified ravidas_lexicon.json)
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
RAW_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "raw", "padaavali.json")
OUTPUT_MD = os.path.join(BASE_DIR, "content", "sant_ravidas", "Sant_Ravidas_Padaavali_Trilingual.md")

sys.path.append(os.path.join(BASE_DIR, "scripts", "sant_ravidas"))
from ravidas_gloss_engine import generate_ravidas_gloss
from padaavali_translations_data import PADAAVALI_DATA

padas = json.load(open(RAW_PATH, encoding='utf-8'))
print(f"Loaded {len(padas)} Padaavali compositions.")
assert len(PADAAVALI_DATA) == 117, f"Expected 117 Padas in translations data, got {len(PADAAVALI_DATA)}"

print("Building Sant_Ravidas_Padaavali_Trilingual.md...")

md_out = []
md_out.append("# संत रविदास जी: 117 अमर पद (Sant Ravidas: 117 Immortal Padas & Bhajans)\n")
md_out.append("### त्रिभाषी संपूर्ण महाग्रंथ: मूल पद, पदच्छेद, शब्दार्थ, काव्यानुवाद एवं दार्शनिक मीमांसा\n")
md_out.append("> **ग्रंथ परिचय**: संत शिरोमणि रविदास जी की पदावली भारतीय भक्ति आंदोलन का वह स्वर्णिम शिखर है जहाँ आत्मा और परमात्मा का विरह और मिलन, सामाजिक न्याय और निर्गुण अद्वैत एक सुर में झंकृत होते हैं। 'प्रभु जी तुम चंदन हम पानी' जैसे विश्व-विख्यात पदों से सुशोभित यह त्रिभाषी महाग्रंथ प्रत्येक पद का मूल पाठ, पदच्छेद, शुद्ध शब्दार्थ (0 Devanagari in English gloss), पद्यानुवाद और दार्शनिक व्याख्या प्रस्तुत करता है।\n\n---\n")

# Table of Contents
md_out.append("## 📜 विषय-सूची (Table of Contents - 117 Padas)\n\n| पद सं. | प्रथम पंक्ति (First Line) | केंद्रीय विषय (Core Theme) |\n|---|---|---|\n")

for p in padas:
    p_id = p["id"]
    title = p.get("title", f"पद {p_id}")
    clean_t = re.sub(r'[\d॥।]+$', '', title).strip()
    theme_hi = PADAAVALI_DATA.get(p_id, {}).get("theme_hi", f"आत्म-निवेदन एवं हरि-भक्ति (पद {p_id})")
    md_out.append(f"| {p_id} | [{clean_t}](#pad-{p_id}) | {theme_hi} |\n")

md_out.append("\n---\n\n")

# Process each Pad
for p in padas:
    p_id = p["id"]
    title = p.get("title", f"पद {p_id}")
    clean_t = re.sub(r'[\d॥।]+$', '', title).strip()
    lines = p.get("lines", [])
    
    p_info = PADAAVALI_DATA.get(p_id, {})
    theme_hi = p_info.get("theme_hi", f"आत्म-निवेदन एवं हरि-भक्ति (पद {p_id})")
    theme_en = p_info.get("theme_en", f"Divine Contemplation (Pad {p_id})")
    hi_v = p_info.get("hi_v", "").strip()
    en_v = p_info.get("en_v", "").strip()
    comm_txt = p_info.get("comm", "").strip()
    
    assert hi_v, f"Missing hi_v for Pad {p_id}"
    assert en_v, f"Missing en_v for Pad {p_id}"
    assert comm_txt, f"Missing comm for Pad {p_id}"
    
    md_out.append(f"<a name=\"pad-{p_id}\"></a>\n")
    md_out.append(f"## पद {p_id}: {clean_t}\n")
    md_out.append(f"**केंद्रीय विषय:** {theme_hi} ({theme_en})\n\n")
    
    # 1. Original Text
    md_out.append("### 📜 मूल रचना (Original Hymn - Devanagari)\n```text\n")
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
    md_out.append("[⬆️ वापस विषय-सूची पर जाएं](#-विषय-सूची-table-of-contents---117-padas)\n\n---\n\n")

with open(OUTPUT_MD, "w", encoding="utf-8") as f:
    f.writelines(md_out)

print(f"Successfully generated {OUTPUT_MD} ({os.path.getsize(OUTPUT_MD)} bytes)")
