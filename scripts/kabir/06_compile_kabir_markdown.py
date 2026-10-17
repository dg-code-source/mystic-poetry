import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

content_dir = "content/kabir"
os.makedirs(content_dir, exist_ok=True)

with open("data/kabir/kabir_data.json", "r", encoding="utf-8") as f:
    all_items = json.load(f)

print(f"Loaded {len(all_items)} translated items for markdown compilation.")

# Group by category
grouped = {
    'shabad': [x for x in all_items if x['type'] == 'kabir_shabad'],
    'salok': [x for x in all_items if x['type'] == 'kabir_salok'],
    'doha': [x for x in all_items if x['type'] == 'kabir_doha'],
    'ramaini': [x for x in all_items if x['type'] == 'kabir_ramaini'],
    'sakhi': [x for x in all_items if x['type'] == 'kabir_sakhi'],
    'pad': [x for x in all_items if x['type'] == 'kabir_pad'],
}

def render_markdown_volume(filename, title, subtitle, intro, items, prefix):
    filepath = os.path.join(content_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n")
        f.write(f"### {subtitle}\n")
        f.write(f"> **ग्रंथ परिचय**: {intro}\n\n")
        f.write("---\n")
        f.write(f"## 📜 विषय-सूची (Table of Contents - {len(items)} Masterpieces)\n\n")
        f.write("| क्र.सं. | शीर्षक (Title) | मुख्य विषय (Theme) |\n")
        f.write("|---|---|---|\n")
        
        for it in items:
            num = it.get('num', 1)
            t_hi = it['title_hi']
            anchor = f"{prefix}-{num}"
            theme = it['title']
            f.write(f"| {num} | [{t_hi}](#{anchor}) | {theme} |\n")
            
        f.write("\n---\n\n")
        
        for it in items:
            num = it.get('num', 1)
            t_hi = it['title_hi']
            t_en = it['title']
            anchor = f"{prefix}-{num}"
            orig = it['original_text']
            v_hi = it['verse_hi']
            v_en = it['verse_en']
            comm = it['meaning']
            gloss = it.get('glossary', {})
            g_hi = gloss.get('hindi', '')
            g_en = gloss.get('english', '')
            
            f.write(f'<a name="{anchor}"></a>\n')
            f.write(f"## {t_hi}\n")
            f.write(f"**English Title:** {t_en}\n\n")
            
            f.write("### 📜 मूल रचना (Original Text - Devanagari)\n")
            f.write("```text\n")
            f.write(f"{orig}\n")
            f.write("```\n\n")
            
            if g_hi or g_en:
                f.write("### 🔍 पदच्छेद एवं त्रिभाषी शब्दार्थ (Word-by-Word Trilingual Gloss)\n")
                if g_hi:
                    f.write("#### 🇮🇳 हिंदी शब्दार्थ (Hindi Word-by-Word Meaning)\n")
                    f.write("```text\n")
                    f.write(f"{g_hi}\n")
                    f.write("```\n\n")
                if g_en:
                    f.write("#### 🌍 English Word-by-Word Gloss (Transliteration & Meaning)\n")
                    f.write("```text\n")
                    f.write(f"{g_en}\n")
                    f.write("```\n\n")
                    
            f.write("### 🪶 छंदोबद्ध काव्यानुवाद (Metered Poetic Translations)\n")
            f.write("#### 🇮🇳 आधुनिक हिंदी पद्यानुवाद (Hindi Poetic Verse)\n")
            f.write(f"{v_hi}\n\n")
            f.write("#### 🇬🇧 Lyrical English Verse Translation\n")
            f.write(f"{v_en}\n\n")
            
            f.write("### 💡 दार्शनिक एवं आध्यात्मिक मीमांसा (Philosophical Commentary)\n")
            f.write(f"{comm}\n\n")
            f.write("---\n\n")
            
    print(f"Generated {filename} ({len(items)} items, {os.path.getsize(filepath)} bytes)")

# 1. Shabads (149)
render_markdown_volume(
    filename="Sant_Kabir_Shabad_Trilingual.md",
    title="संत कबीर: संपूर्ण 149 शब्द (Sant Kabir: Complete 149 Shabads)",
    subtitle="त्रिभाषी संपूर्ण महाग्रंथ: मूल देवनागरी, पदच्छेद, शब्दार्थ, काव्यानुवाद एवं दार्शनिक मीमांसा",
    intro="सिखों के परम पावन धर्मग्रंथ **'श्री गुरु ग्रंथ साहिब जी' (SGGS)** में दर्ज भक्त कबीर जी के संपूर्ण 149 पावन शब्द। प्रत्येक शब्द रागबद्ध, त्रिभाषी शब्दार्थ, छंदोबद्ध पद्यानुवाद और निर्गुण भक्ति की दार्शनिक व्याख्या से परिपूर्ण है।",
    items=grouped['shabad'],
    prefix="shabad"
)

# 2. Saloks (245)
render_markdown_volume(
    filename="Sant_Kabir_Salok_Trilingual.md",
    title="संत कबीर: संपूर्ण 245 सलोक (Sant Kabir: Complete 245 Saloks)",
    subtitle="त्रिभाषी संपूर्ण महाग्रंथ: मूल देवनागरी, पदच्छेद, शब्दार्थ, काव्यानुवाद एवं दार्शनिक मीमांसा",
    intro="श्री गुरु ग्रंथ साहिब जी में संकलित भक्त कबीर जी के संपूर्ण 243 सलोक एवं दो पराकाष्ठा सलोक (गगन दमामा बाजिओ एवं सूरा सो पहिचानीऐ)।",
    items=grouped['salok'],
    prefix="salok"
)

# 3. Dohe (84)
render_markdown_volume(
    filename="Sant_Kabir_Dohe_Trilingual.md",
    title="संत कबीर: संपूर्ण 84 अमर दोहे (Sant Kabir: Complete 84 Timeless Dohas)",
    subtitle="त्रिभाषी संपूर्ण महाग्रंथ: मूल देवनागरी, पदच्छेद, शब्दार्थ, काव्यानुवाद एवं दार्शनिक मीमांसा",
    intro="संत कबीर दास जी के सार्वकालिक, जन-मानस में रचे-बसे 84 अमर दोहे (जैसे: धीरे-धीरे रे मना, माटी कहे कुम्हार से, माला फेरत जुग भया, साईं इतना दीजिये, साधु ऐसा चाहिए)।",
    items=grouped['doha'],
    prefix="doha"
)

# 4. Ramaini (8)
render_markdown_volume(
    filename="Sant_Kabir_Ramaini_Trilingual.md",
    title="संत कबीर: संपूर्ण रमैणी संग्रह (Sant Kabir: Complete Ramaini Collection)",
    subtitle="त्रिभाषी संपूर्ण महाग्रंथ: मूल देवनागरी, पदच्छेद, शब्दार्थ, काव्यानुवाद एवं दार्शनिक मीमांसा",
    intro="कबीर बीजक एवं कबीर वाङ्मय की दार्शनिक आधारशिला 'रमैणी' (बावनी, सतपदी, अष्टपदी, दुपदी, बारहपदी, चौपदी)।",
    items=grouped['ramaini'],
    prefix="ramaini"
)

# 5. Granthavali Sakhi (59 Angs)
render_markdown_volume(
    filename="Sant_Kabir_Granthavali_Sakhi_Trilingual.md",
    title="कबीर ग्रंथावली: संपूर्ण 59 साखी अंग (Kabir Granthavali: Complete 59 Sakhi Angs)",
    subtitle="डॉ. श्यामसुंदर दास संपादित कबीर ग्रंथावली का प्रामाणिक त्रिभाषी अध्ययन संस्करण (935 साखियाँ)",
    intro="नागरीप्रचारिणी सभा द्वारा प्रकाशित एवं डॉ. श्यामसुंदर दास द्वारा संपादित 'कबीर ग्रंथावली' के संपूर्ण 59 साखी अंग (गुरुदेव कौ अंग, सुमिरण कौ अंग, बिरह कौ अंग, आदि)।",
    items=grouped['sakhi'],
    prefix="sakhi"
)

# 6. Granthavali Pad (17 Raags)
render_markdown_volume(
    filename="Sant_Kabir_Granthavali_Pad_Trilingual.md",
    title="कबीर ग्रंथावली: संपूर्ण 17 पद राग (Kabir Granthavali: Complete 17 Pad Raags)",
    subtitle="डॉ. श्यामसुंदर दास संपादित कबीर ग्रंथावली का प्रामाणिक त्रिभाषी पद संकलन (407 पद)",
    intro="कबीर ग्रंथावली के सभी 17 शास्त्रीय रागों (राग गौड़ी, रामकली, आसावरी, सोरठि, केदारौ, आदि) में निबद्ध संपूर्ण 407 पद।",
    items=grouped['pad'],
    prefix="pad"
)

print("\nAll 6 Markdown study volumes generated successfully in content/kabir/!")
