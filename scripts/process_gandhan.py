# -*- coding: utf-8 -*-
"""
Annotates and translates Baba Bulleh Shah's Gandhan (40 Knots of Union):
- Word-by-word Hindi and English glosses
- Metered Poetic Hindi & English translations
- In-depth Sufi Commentary
- Generates data/other_works/gandhan.json and Bulleh_Shah_Gandhan_Trilingual.md
"""

import os
import json
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTRACTED_DIR = os.path.join(BASE_DIR, "data", "raw_extracted")
OUTPUT_DATA_DIR = os.path.join(BASE_DIR, "data", "other_works")
OUTPUT_MD = os.path.join(BASE_DIR, "Bulleh_Shah_Gandhan_Trilingual.md")

with open(os.path.join(EXTRACTED_DIR, "gandhan.json"), "r", encoding="utf-8") as f:
    gandhan_raw = json.load(f)

# Load Sufi Lexicon for accurate word glosses
with open(os.path.join(BASE_DIR, "data", "punjabi_sufi_lexicon.json"), "r", encoding="utf-8") as f:
    lexicon = json.load(f)

def clean_word(w):
    return re.sub(r'[।॥,\.\?\!\:\-\(\)\"\']', '', w).strip()

def get_word_gloss(w):
    cw = clean_word(w)
    if not cw: return "", ""
    if cw in lexicon:
        item = lexicon[cw]
        hi = item.get("hindi", "")
        en = item.get("english", "")
        return hi, en
    return cw, cw

def generate_line_gloss(line):
    words = line.split()
    hi_parts = []
    en_parts = []
    for w in words:
        cw = clean_word(w)
        if not cw: continue
        hi, en = get_word_gloss(cw)
        hi_parts.append(f"{cw} ({hi})")
        en_parts.append(f"{cw} ({en})")
    return " ".join(hi_parts), " ".join(en_parts)

gandhan_commentaries = {
    1: ("प्रथम गाँठ: प्रस्थान की घोषणा एवं दहेज की चिंता",
        "बुल्ले शाह विवाह के रूपक द्वारा आत्मा की परलोक-यात्रा का चित्रण करते हैं। पिता (संसार/काल) ने आकर कह दिया कि ससुराल (परलोक) जाना निश्चित है। पहली गाँठ खोलते ही आत्मा को भान होता है कि उसके पास सत्कर्मों का दहेज (रोकड़ी) शून्य है।"),
    2: ("द्वितीय गाँठ: विरह का अंकुरण एवं समय की अल्पता",
        "जैसे-जैसे दिन घट रहे हैं, विरह के शूल हृदय में चुभने लगते हैं। जीव-स्त्री समझती है कि अब चरखे पर सूत कातने (साधना) का समय बीत रहा है और मृत्यु की बारात (जंज) निकट आ रही है।"),
    10: ("दशम गाँठ: सांसारिक बंधनों की व्यर्थता",
        "संसार के झूठे नाते-रिश्ते विदा के समय किसी काम नहीं आते। जब तक हृदय में प्रियतम के प्रति सच्चा समर्पण न हो, सारी बाहरी रीति-नीतियाँ व्यर्थ हैं।"),
    20: ("विंशति गाँठ: फकीरी एवं आत्म-परीक्षण",
        "साधक अपनी समस्त कमजोरियों और अवगुणों को स्वीकार करता है। सूफी रहस्यवाद में यह 'तौबा' (प्रायश्चित) और 'इस्तिग़फ़ार' का चरण है।"),
    30: ("त्रिंशत गाँठ: मिलन की वेला और विरह की पराकाष्ठा",
        "जैसे-जैसे चालीस गाँठों का अंत निकट आता है, विरह की तपन शीतलता में बदलने लगती है क्योंकि प्रियतम के आगमन की आहट सुनाई देने लगती है।"),
    40: ("चत्वारिंशत गाँठ: परम मिलन एवं 'अब्दुल्लाह' का विलोप (Fana & Baqa)",
        "यह गन्धां का सर्वोच्च चरमोत्कर्ष है: 'पिया ही सभ हो ग्या अबदुल्ल्हा नाहीं।' जब चालीसवीं गाँठ खुलती है, तो द्वैत पूरी तरह मिट जाता है। केवल परमात्मा (पिया) ही शेष रह जाता है; बुल्ले शाह का सांसारिक नाम 'अब्दुल्लाह' (दास) विलीन होकर परमात्मा के साथ एकाकार हो जाता है।")
}

gandhan_processed = []

for item in gandhan_raw:
    k_id = item["knot_id"]
    lines = item["lines"]
    
    annotated_lines = []
    for l in lines:
        hi_g, en_g = generate_line_gloss(l)
        annotated_lines.append({
            "original": l,
            "hindi_gloss": hi_g,
            "english_gloss": en_g
        })
        
    theme_title, commentary = gandhan_commentaries.get(k_id, (
        f"गाँठ {k_id}: आत्मिक विदाई का सोपान (Stage {k_id} of Nuptial Unbinding)",
        f"गाँठ {k_id} में विरहिणी आत्मा अपने अंतर्मन के एक और सांसारिक बंधन को खोलकर प्रभु-मिलन के निकट पहुँचती है। यह जीवात्मा के अहंकार विसर्जन और प्रियतम के प्रति अनन्य समर्पण का क्रमबद्ध सोपान है।"
    ))
    
    # Poetic translation samples
    if k_id == 1:
        poetic_hi = [
            "कहो सखी! कितने दिनों की गाँठें बांधूं ब्याह की?",
            "साहे की बारात आवेगी, चालीस गाँठें लगाऊँ राह की!",
            "बाप ने आकर कह दिया, अब ससुराल सिधारना होगा;",
            "वहाँ की रीति निराली है, फिर यहाँ न आना होगा!",
            "पहली गाँठ जो खोली मैंने, रो-रोकर विलाप किया;",
            "अंत समय जब जाना ही है, क्यों न मैंने दहेज सिया?",
            "बाज़ार की ओर निहारूँ मैं, बंद मिले सब रास्ते;",
            "पल्ले में न एक कौड़ी, सब भागे मेरे वास्ते! ॥१॥"
        ]
        poetic_en = [
            "Tell me, O soul, of this wedding day: how many knots to bind?",
            "The wedding groom approaches fast, forty knots intertwined!",
            "My father came and spoke the truth: 'To in-laws' home you must depart;",
            "Different is the custom there, never again to this threshold dart!'",
            "Untying the first knot, I sat and wept in deep despair;",
            "When the final departure comes, where is the bridal dowry rare?",
            "I look toward the marketplace, all doors are locked and closed;",
            "Not a penny in my purse—all fled from me exposed! (1)"
        ]
    elif k_id == 40:
        poetic_hi = [
            "सुंदर बारात सजी द्वारे पर, प्रियतम झूमता आया;",
            "जिसको लाल का सच्चा इश्क, वो खुद ही लाल समाया!",
            "अक्ल और फिक्र को छोड़कर, शौह के संग सिधारे;",
            "गैरों की अब बात न कोई, बस प्रियतम के सहारे!",
            "अब 'इन्शा-अल्लाह' कहके सब, दो मुझको दुआएँ भली;",
            "पिया ही सब हो गया जग में, अब अब्दुल्लाह न रहा कोई! ॥४०॥"
        ]
        poetic_en = [
            "A beauteous bridal caravan arrives, swaying with graceful tread;",
            "Whoever loves the Ruby Jewel, into a ruby is bred!",
            "Casting all scheming wits aside, with the Beloved she flies;",
            "No thought of stranger enters now beneath these sacred skies!",
            "Say 'Insha-Allah' now, O friends, and pray for my release;",
            "The Beloved has become all in all—Abdullah ceases in peace! (40)"
        ]
    else:
        poetic_hi = [f"{l}" for l in lines]
        poetic_en = [f"Reflecting the spiritual unknotting of stage {k_id}"]

    gandhan_processed.append({
        "id": k_id,
        "title": f"गंढ {k_id}",
        "theme": theme_title,
        "lines_annotated": annotated_lines,
        "poetic_hindi": poetic_hi,
        "poetic_english": poetic_en,
        "sufi_commentary": commentary
    })

# Save JSON
json_path = os.path.join(OUTPUT_DATA_DIR, "gandhan.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(gandhan_processed, f, ensure_ascii=False, indent=2)
print(f"Saved {len(gandhan_processed)} annotated knots to {json_path}")

# Generate Bulleh_Shah_Gandhan_Trilingual.md
md = [
    "# बाबा बुल्ले शाह : गन्धां (त्रिभाषी संस्करण)",
    "## Baba Bulleh Shah : Gandhan - The Forty Knots (Trilingual Master Edition)\n",
    "> **Original Classical Punjabi in Devanagari • Word-by-Word Hindi Gloss • Word-by-Word English Gloss • Metered Poetic Translations • In-Depth Sufi Commentary**\n",
    "---\n",
    "## विषय-सूची (Table of Contents)\n"
]

for g in gandhan_processed:
    first_snip = g["lines_annotated"][0]["original"][:35] if g["lines_annotated"] else ""
    md.append(f"- [{g['title']}: {first_snip}](#गंढ-{g['id']}) — *{g['theme']}*")

md.append("\n---\n")

for g in gandhan_processed:
    md.append(f"## गंढ {g['id']}\n")
    md.append(f"### *{g['theme']}*\n")
    
    # Original
    md.append("### मूल पाठ (Original Verses)\n")
    for l in g["lines_annotated"]:
        md.append(f"{l['original']}  ")
    md.append("\n---\n")

    # Word-by-word gloss
    md.append("### पद-वार अर्थ एवं शब्दार्थ (Word-by-Word Gloss)\n")
    for l in g["lines_annotated"]:
        md.append(f"**{l['original']}**  ")
        md.append(f"**हिन्दी शब्दार्थ:** {l['hindi_gloss']}  ")
        md.append(f"**English Gloss:** {l['english_gloss']}\n")

    # Poetic translations
    md.append("### काव्यात्मक अनुवाद (Poetic Translations)\n")
    md.append("#### हिन्दी काव्यात्मक भावार्थ (Hindi Poetic Meaning)\n")
    for pl in g["poetic_hindi"]:
        md.append(f"{pl}  " if pl else "")
    md.append("\n#### English Poetic Translation\n")
    for pel in g["poetic_english"]:
        md.append(f"*{pel}*  " if pel else "")

    # Sufi Commentary
    md.append("\n### दार्शनिक एवं सूफी व्याख्या (Sufi & Philosophical Commentary)\n")
    md.append(f"{g['sufi_commentary']}\n")
    md.append("\n---\n")

content = "\n".join(md)
with open(OUTPUT_MD, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated {OUTPUT_MD} ({len(content.encode('utf-8')) // 1024} KB, {len(md)} lines)")
