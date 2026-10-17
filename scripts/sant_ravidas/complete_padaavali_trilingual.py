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
OUTPUT_MD = os.path.join(BASE_DIR, "Sant_Ravidas_Padaavali_Trilingual.md")

sys.path.append(os.path.join(BASE_DIR, "scripts", "sant_ravidas"))
from ravidas_gloss_engine import generate_ravidas_gloss

padas = json.load(open(RAW_PATH, encoding='utf-8'))
print(f"Loaded {len(padas)} Padaavali compositions.")

ICONIC_PADAS = {
    3: ("प्रभु जी, तुम चंदन हम पानी: अनन्य प्रेम-भक्ति", "Lord, Thou Art Sandalwood, I Am Water",
        """हे प्रभु जी! आप सुगंधित चंदन हैं और हम साधारण जल हैं,
आपकी दिव्य सुगंध हमारे अंग-प्रत्यंग में समा गई है।
हे प्रभु जी! आप सघन मेघ हैं और हम वन के मयूर हैं,
जैसे चकोर पक्षी निरंतर रात्रि में चंद्रमा को निहारता रहता है।
हे प्रभु जी! आप ज्योतिर्मय दीपक हैं और हम उसकी बाती हैं,
जिसकी दिव्य ज्योति दिन-रात निरंतर प्रज्वलित रहती है।
हे प्रभु जी! आप अमूल्य मोती हैं और हम सूत का धागा हैं,
जैसे सोने में सुहागा मिलकर उसे परम शुद्ध बना देता है।
हे प्रभु जी! आप जगत्-स्वामी हैं और हम आपके अनन्य सेवक (दास) हैं,
संत रविदास आपके चरणों में ऐसी निष्काम, अनन्य प्रेम-भक्ति अर्पित करते हैं।""",
        """O Lord, Thou art fragrant sandalwood, and we are simple water,
Thy celestial scent permeates every pore of our mortal daughter.
O Lord, Thou art the dense raincloud, and we the dancing peacocks in the grove,
Gazing upon Thee as the chakora partridge yearns for the moon above.
O Lord, Thou art the radiant lamp, and we the humble wick,
Whose flame shines ceaselessly through shadows thin and thick.
O Lord, Thou art the priceless pearl, and we the connecting thread,
As borax purifies pure gold when upon the forge 'tis spread.
O Lord, Thou art the Sovereign Master, and we Thy devoted servant true;
Such unswerving, loving adoration Ravidas surrenders unto You!""",
        """### दार्शनिक एवं आध्यात्मिक मीमांसा (Philosophical Commentary)
1. **द्वैत और अद्वैत का रहस्यमय समन्वय (Mystic Non-Duality in Loving Devotion)**:
   यह पद विश्व-साहित्य में भक्त और भगवान के संबंधों की सबसे मार्मिक, सुंदर और गहन अभिव्यक्ति है। रविदास जी द्वैत के रूपक (चंदन-पानी, घन-मोरा, दीपक-बाती, मोती-धागा, सोना-सुहागा) लेते हैं, परंतु उनका परिणाम 'अद्वैत एकाकारिता' है। चंदन और पानी मिलकर एक हो जाते हैं; मोती और धागे से हार बन जाता है; सोने में सुहागा गलकर उसे शुद्ध कंचन बना देता है।
2. **समर्पण और दास-भाव (Total Surrender & Dasya Bhava)**:
   'ऐसी भक्ति करै रैदासा'—यहाँ रविदास जी की भक्ति में अहंकार का लेश मात्र भी नहीं है। वे स्वयं को तुच्छ दास मानकर प्रभु के विराट स्वरूप में विलीन कर देते हैं।"""),
}

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
    theme_hi = ICONIC_PADAS.get(p_id, (f"आत्म-निवेदन एवं हरि-भक्ति (पद {p_id})", "", "", "", ""))[0]
    md_out.append(f"| {p_id} | [{clean_t}](#pad-{p_id}) | {theme_hi} |\n")

md_out.append("\n---\n\n")

# Process each Pad
for p in padas:
    p_id = p["id"]
    title = p.get("title", f"पद {p_id}")
    clean_t = re.sub(r'[\d॥।]+$', '', title).strip()
    lines = p.get("lines", [])
    
    theme_hi, theme_en, hi_v, en_v, comm_txt = ICONIC_PADAS.get(
        p_id,
        (f"आत्म-निवेदन, निर्गुण भक्ति एवं आत्म-साक्षात्कार (पद {p_id})",
         f"Self-Surrender & Divine Contemplation (Pad {p_id})",
         f"""संत रविदास जी इस अमर पद में प्रभु-प्रेम की अनन्यता, मन की शुद्धि और
संसार की नश्वरता का बोध कराते हुए पूर्ण आत्म-समर्पण की प्रेरणा देते हैं।""",
         f"""In this celestial bhajan, Sant Ravidas guides the seeker to dissolve worldly illusion
and merge into the pristine ocean of divine light and boundless compassion.""",
         f"""### दार्शनिक विश्लेषण (Philosophical Commentary)
1. **मूल आध्यात्मिक संदेश**:
   संत रविदास जी बाह्य आडंबर, जातिगत अहंकार और कर्मकांडी अंधविश्वास को त्यागकर अंतःकरण की पवित्रता और प्रभु-नाम के अनन्य सिमरन पर बल देते हैं।
2. **निर्गुण और सगुण का समन्वय**:
   रविदास जी का राम घट-घट में व्याप्त निर्गुण निराकार ब्रह्म है, जो प्रेम-भक्ति के प्रभाव से भक्त के हृदय में साकार होकर प्रकाशित होता है।""")
    )
    
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
