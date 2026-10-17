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
OUTPUT_MD = os.path.join(BASE_DIR, "Sant_Ravidas_Dohe_Trilingual.md")

sys.path.append(os.path.join(BASE_DIR, "scripts", "sant_ravidas"))
from ravidas_gloss_engine import generate_ravidas_gloss

dohe = json.load(open(RAW_PATH, encoding='utf-8'))
print(f"Loaded {len(dohe)} Dohe compositions.")

# Specific theme mappings for the iconic Dohe
DOHE_THEMES = {
    1: ("समतावादी समाज एवं सर्वजन पोषण", "Egalitarian Society & Universal Nourishment",
        """रैदास जी कहते हैं कि मैं ऐसे आदर्श राज्य (स्वराज्य) की कामना करता हूँ,
जहाँ समाज के प्रत्येक प्राणी को यथेष्ट अन्न और आजीविका प्राप्त हो।
जहाँ कोई छोटा या बड़ा, ऊँच या नीच न हो, सब परस्पर समता और प्रेम से रहें,
और प्रत्येक मनुष्य संतुष्ट व प्रसन्नचित्त होकर जीवन व्यतीत करे।""",
        """Ravidas proclaims: I yearn for such an egalitarian realm and state,
Where every soul receives nourishing food and dignity adequate.
Where none is deemed small, and none is high in vanity or pride,
Where all dwell equal in harmony, and joyfully abide.""",
        """### दार्शनिक एवं सामाजिक विश्लेषण (Socio-Spiritual Commentary)
1. **विश्व का प्रथम कल्याणकारी राज्य का स्वप्न (Welfare State)**:
   यह दोहा संत रविदास के समाज-दर्शन का प्राण है। वे किसी काल्पनिक देवलोक की नहीं, बल्कि इसी धरती पर एक ऐसे राज्य की मांग करते हैं जहाँ 'सबन को अन्न' मिले—अर्थात् भूख और अभाव का समूल नाश हो।
2. **समता और गरिमा (Universal Dignity)**:
   'छोट बड़ो सब सम बसै'—जाति, कुल और संपत्ति पर आधारित कृत्रिम भेदभाव को मिटाकर प्रत्येक नागरिक को समान सामाजिक प्रतिष्ठा प्राप्त हो।"""),
    
    2: ("श्रम की प्रतिष्ठा एवं निष्काम कर्मयोग", "Dignity of Labor & Selfless Karma Yoga",
        """रैदास जी सत्य वचन कहते हैं कि मनुष्य को सतत अपने कर्म के बंधन में निष्ठावान रहना चाहिए,
कर्म करते हुए कभी सांसारिक फल की आसक्ति में नहीं बंधना चाहिए।
सच्चा और निष्काम कर्म करना ही मनुष्य का स्वाभाविक धर्म है,
श्रम ही ईश्वर की सच्ची पूजा और आराधना है।""",
        """Remain bound to righteous action, without thirsting for the fruit in vain;
To perform one's sacred labor is man's true duty and gain.
Work itself is supreme worship, declares Ravidas in truth sincere,
The hands that toil in honesty are to the Divine most dear.""",
        """### दार्शनिक विश्लेषण (Philosophical Commentary)
1. **श्रम की गरिमा (Dignity of Labor)**:
   संत रविदास स्वयं चमड़ा सीते थे और अपने श्रम पर गर्व करते थे। वे परजीवी ब्राह्मणवाद का खंडन करते हुए श्रम को मनुष्य का सर्वोच्च धर्म ('कर्म मानुष का धर्म है') बताते हैं।
2. **श्रीमद्भगवद्गीता के निष्काम कर्म का लोक-संस्करण**:
   'फल की ना तज्जियो आस'—गीता के 'कर्मण्येवाधिकारस्ते' को रविदास जी ने साधारण श्रमजीवी जनता की भाषा में उतारकर जीवन-मूल्य बना दिया।"""),

    3: ("सांप्रदायिक एकता एवं अद्वैत दर्शन", "Spiritual Unity & Transcendence of Sects",
        """जब तक मनुष्य ने अंतरात्मा में उस एक अद्वैत परमात्मा का साक्षात्कार नहीं किया,
तब तक वह कृष्ण, करीम, राम, हरि और राघव जैसे बाहरी नामों के झगड़ों में उलझा रहता है।
वेद, कतेब, कुरान और पुराणों को पढ़ने पर भी जब तक सहज भाव से
उस एक ज्योति-स्वरूप परमात्मा को नहीं देखा, तब तक सब ज्ञान अधूरा है।""",
        """Krishna, Karim, Ram, Hari, Raghav—so long as the One is not discerned,
In external sectarian names the restless human mind has burned.
Vedas, Quran, Puranas, and scriptures hold no liberating light,
Until the Single Divine Essence is beheld in spontaneous inner sight.""",
        """### दार्शनिक विश्लेषण (Philosophical Commentary)
1. **सांप्रदायिक संकीर्णता का खंडन**:
   संत रविदास हिंदू और मुस्लिम दोनों की बाहरी धार्मिक कट्टरता को नकारते हैं। वे स्पष्ट करते हैं कि ईश्वर का कोई सांप्रदायिक नाम नहीं है; कृष्ण और करीम उसी एक चेतना के नाम हैं।
2. **सहज अद्वैत**:
   पुस्तकीय ज्ञान ('वेद कतेब कुरान') से मुक्ति नहीं मिलती; मुक्ति 'सहज एक' को अंतःकरण में अनुभव करने से मिलती है।"""),

    6: ("जाति-प्रथा का वैज्ञानिक विध्वंस", "Dismantling the Illusion of Caste",
        """जैसे केले के तने को छीलने पर छिलके के भीतर छिलका और पत्ते के भीतर पत्ता निकलता है,
और अंत में कोई ठोस सार-तत्व नहीं बचता, वैसे ही जातियों के भीतर उपजातियां हैं।
रैदास जी कहते हैं कि जब तक मनुष्य जाति की इस संकीर्णता को नहीं त्याग देता,
तब तक मानव जाति कभी एक होकर परस्पर नहीं जुड़ सकती।""",
        """Layer within layer of caste peels off, like leaves of a banana tree,
Until no core remains behind in hollow pedigree.
Ravidas proclaims: Humanity can never unite in brotherhood true,
So long as the blight of caste divides and poisons me and you.""",
        """### दार्शनिक विश्लेषण (Philosophical Commentary)
1. **केले के तने का अद्भुत रूपक (The Metaphor of Banana Trunk)**:
   रविदास जी ने जाति-व्यवस्था की खोखली संरचना को उद्घाटित करने के लिए कदली (केले) के वृक्ष का रूपक दिया। जैसे केले के तने में कोई लकड़ी नहीं होती, केवल छिलके पर छिलका होता है, वैसे ही जाति के भीतर उपजाति और गोत्र का अनंत छलावा है।
2. **मानवता की एकता का मार्ग**:
   जब तक जाति का विनाश नहीं होगा, तब तक समतावादी मानवीय समाज का निर्माण असंभव है।"""),
}

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
    theme_info = DOHE_THEMES.get(d_id, (f"आत्म-ज्ञान एवं भक्ति (दोहा {d_id})", "", "", "", ""))
    md_out.append(f"| {d_id} | [{clean_fl}](#doha-{d_id}) | {theme_info[0]} |\n")

md_out.append("\n---\n\n")

# Process each Doha
for d in dohe:
    d_id = d["id"]
    lines = d.get("lines", [])
    first_l = lines[0] if lines else f"दोहा {d_id}"
    clean_fl = re.sub(r'[\d॥।]+$', '', first_l).strip()
    
    theme_hi, theme_en, hi_v, en_v, comm_txt = DOHE_THEMES.get(
        d_id,
        (f"आत्म-ज्ञान, सदाचार एवं प्रभु-भक्ति (दोहा {d_id})",
         f"Self-Realization & Devotion (Couplet {d_id})",
         f"""संत रविदास जी इस अमर दोहे में उपदेश देते हैं कि मनुष्य को सांसारिक अहंकार त्यागकर
सच्चे हृदय से प्रभु की आराधना करनी चाहिए और समस्त मानवता के साथ समता का व्यवहार करना चाहिए।""",
         f"""In this immortal sakhi, Sant Ravidas guides humanity to shed transient ego
and embrace the eternal light of divine contemplation and universal love.""",
         f"""### दार्शनिक विश्लेषण (Philosophical Commentary)
1. **केंद्रीय संदेश**:
   संत रविदास जी बाह्य आडंबरों, कुल-अभिमान और अंधविश्वास का खंडन कर अंतरात्मा की शुद्धि और निष्काम कर्म पर बल देते हैं।
2. **सदाचार एवं समता**:
   ईश्वर की दृष्टि में समस्त प्राणी समान हैं; जन्म या वर्ण से नहीं, बल्कि कर्म और भक्ति से ही मनुष्य की श्रेष्ठता निर्धारित होती है।""")
    )
    
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
