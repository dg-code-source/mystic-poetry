# -*- coding: utf-8 -*-
"""
Assembles all processed Kafian from data/kafian/*.json into the definitive
master trilingual markdown edition: Bulleh_Shah_Kafian_Trilingual.md
Supports both Schema 1 (Kafian 1-50) and Schema 2 (Kafian 51-160) seamlessly.
"""

import os
import json
import glob
import re
import unicodedata

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
KAFIAN_DIR = os.path.join(DATA_DIR, "kafian")
OUTPUT_MD = os.path.join(BASE_DIR, "Bulleh_Shah_Kafian_Trilingual.md")

def gfm_slug(text):
    """Generates standard GitHub Flavored Markdown slug preserving Devanagari letters & marks."""
    text = text.strip().lower()
    clean = []
    for ch in text:
        cat = unicodedata.category(ch)
        if cat.startswith('L') or cat.startswith('M') or cat.startswith('N') or cat == 'Pd' or ch.isspace() or ch == '-':
            clean.append(ch)
    s = ''.join(clean)
    s = re.sub(r'[\s]+', '-', s)
    return s.strip('-')

def get_section_title(kafi_id):
    if 1 <= kafi_id <= 50:
        return "भाग 1 (काफ़ियां 1–50)"
    elif 51 <= kafi_id <= 100:
        return "भाग 2 (काफ़ियां 51–100)"
    else:
        return "भाग 3 (काफ़ियां 101–160)"

def format_title(kafi):
    k_id = kafi["id"]
    raw_title = (kafi.get("title") or kafi.get("title_punjabi") or "").strip()
    # Check if raw_title already starts with number
    if re.match(r'^\d+\.', raw_title):
        return raw_title
    return f"{k_id}. {raw_title}"

def assemble():
    files = sorted(glob.glob(os.path.join(KAFIAN_DIR, "kafi_*.json")))
    if not files:
        print("No completed Kafian found in data/kafian/")
        return

    kafian = []
    for fpath in files:
        with open(fpath, "r", encoding="utf-8") as f:
            kafian.append(json.load(f))
    
    kafian.sort(key=lambda x: x["id"])

    md = []
    md.append("# बाबा बुल्ले शाह : सम्पूर्ण काफ़ियां (त्रिभाषी संस्करण)")
    md.append("## Baba Bulleh Shah : Complete Kafian (Trilingual Edition)\n")
    md.append("> **Original Classical Punjabi in Devanagari • Word-by-Word Hindi Gloss • Word-by-Word English Gloss • Metered Poetic Translations • In-Depth Sufi Commentary**\n")
    md.append("---\n")
    md.append("## विषय-सूची (Table of Contents)\n")

    current_sec_toc = None
    for k in kafian:
        k_id = k["id"]
        sec = get_section_title(k_id)
        if sec != current_sec_toc:
            current_sec_toc = sec
            md.append(f"\n### {current_sec_toc}\n")
        
        full_title = format_title(k)
        slug = gfm_slug(full_title)
        en_title = k.get("title_english")
        if en_title:
            md.append(f"- [{full_title}](#{slug}) — *{en_title}*")
        else:
            md.append(f"- [{full_title}](#{slug})")

    md.append("\n---\n")

    current_sec = None
    for k in kafian:
        k_id = k["id"]
        sec = get_section_title(k_id)
        if sec != current_sec:
            current_sec = sec
            md.append(f"\n# {current_sec}\n")
            md.append("---\n")

        full_title = format_title(k)
        md.append(f"## {full_title}\n")

        en_title = k.get("title_english")
        if en_title:
            md.append(f"### *{en_title}*\n")

        # Metadata block
        meta_items = []
        if k.get("raga"):
            meta_items.append(f"**राग:** {k['raga']}")
        if k.get("meter"):
            meta_items.append(f"**छंद:** {k['meter']}")
        if k.get("theme"):
            meta_items.append(f"**विषय:** {k['theme']}")
        if meta_items:
            md.append(" • ".join(meta_items) + "  ")

        hist = k.get("historical_context")
        if hist:
            md.append(f"> **प्रसंग एवं संदर्भ:** {hist}\n")

        # Original Poem block
        md.append("### मूल काफ़िया (Original Poem)\n")
        if "original_poem" in k and k["original_poem"]:
            for stanza in k["original_poem"].strip().split("\n\n"):
                for line in stanza.split("\n"):
                    md.append(f"{line.strip()}  ")
                md.append("")
        elif "stanzas" in k:
            for stanza_obj in k["stanzas"]:
                orig_lines = stanza_obj.get("original", [])
                for line in orig_lines:
                    md.append(f"{line.strip()}  ")
                md.append("")
        md.append("---\n")

        # Detailed Word-by-Word Gloss & Translations
        md.append("### पद-वार अर्थ एवं काव्यात्मक अनुवाद (Word-by-Word Gloss & Translations)\n")

        if "annotated_stanzas" in k:
            for s_idx, stanza_data in enumerate(k["annotated_stanzas"], 1):
                if len(k["annotated_stanzas"]) > 1:
                    md.append(f"#### छंद {s_idx} (Stanza {s_idx})\n")
                
                for line_obj in stanza_data.get("lines", []):
                    orig = line_obj["original"]
                    hi_gloss = line_obj["hindi_gloss"]
                    en_gloss = line_obj["english_gloss"]
                    
                    md.append(f"**{orig}**  ")
                    md.append(f"**हिन्दी शब्दार्थ:** {hi_gloss}  ")
                    md.append(f"**English Gloss:** {en_gloss}\n")
                
                hi_meaning = stanza_data.get("hindi_meaning", "").strip()
                en_meaning = stanza_data.get("english_meaning", "").strip()
                
                if hi_meaning:
                    md.append("#### हिन्दी काव्यात्मक भावार्थ (Hindi Poetic Meaning)\n")
                    for st in hi_meaning.split("\n\n"):
                        for vl in st.split("\n"):
                            md.append(f"{vl.strip()}  ")
                        md.append("")
                
                if en_meaning:
                    md.append("#### English Poetic Translation\n")
                    for st in en_meaning.split("\n\n"):
                        for vl in st.split("\n"):
                            md.append(f"{vl.strip()}  ")
                        md.append("")

        elif "stanzas" in k:
            for s_idx, stanza_obj in enumerate(k["stanzas"], 1):
                md.append(f"#### छंद {s_idx} (Stanza {s_idx})\n")
                
                orig_lines = stanza_obj.get("original", [])
                hi_gloss_raw = stanza_obj.get("hindi_gloss", [])
                en_gloss_raw = stanza_obj.get("english_gloss", [])

                # Normalize glosses into lists of lines
                if isinstance(hi_gloss_raw, str):
                    hi_gloss_lines = [l.strip() for l in hi_gloss_raw.strip().split("\n") if l.strip()]
                elif isinstance(hi_gloss_raw, list):
                    hi_gloss_lines = [l.strip() for l in hi_gloss_raw if isinstance(l, str) and l.strip()]
                else:
                    hi_gloss_lines = []

                if isinstance(en_gloss_raw, str):
                    en_gloss_lines = [l.strip() for l in en_gloss_raw.strip().split("\n") if l.strip()]
                elif isinstance(en_gloss_raw, list):
                    en_gloss_lines = [l.strip() for l in en_gloss_raw if isinstance(l, str) and l.strip()]
                else:
                    en_gloss_lines = []

                # If gloss has exactly 1 string covering the whole stanza, but orig_lines has multiple lines
                if len(hi_gloss_lines) == 1 and len(orig_lines) > 1:
                    # Print all original lines, then the full gloss block
                    for ol in orig_lines:
                        md.append(f"**{ol.strip()}**  ")
                    md.append("")
                    md.append(f"**हिन्दी शब्दार्थ:** {hi_gloss_lines[0]}  ")
                    if en_gloss_lines:
                        md.append(f"**English Gloss:** {en_gloss_lines[0]}\n")
                    else:
                        md.append("")
                else:
                    # Line-by-line pairing
                    import itertools
                    max_len = max(len(orig_lines), len(hi_gloss_lines), len(en_gloss_lines))
                    for i in range(max_len):
                        ol = orig_lines[i] if i < len(orig_lines) else ""
                        hl = hi_gloss_lines[i] if i < len(hi_gloss_lines) else ""
                        el = en_gloss_lines[i] if i < len(en_gloss_lines) else ""

                        if ol:
                            md.append(f"**{ol.strip()}**  ")
                        if hl:
                            md.append(f"**हिन्दी शब्दार्थ:** {hl.strip()}  ")
                        if el:
                            md.append(f"**English Gloss:** {el.strip()}\n")
                        elif hl:
                            md.append("")

                poetic_hi = stanza_obj.get("poetic_hindi")
                if poetic_hi:
                    if isinstance(poetic_hi, str):
                        poetic_hi_lines = [l.strip() for l in poetic_hi.strip().split("\n") if l.strip()]
                    elif isinstance(poetic_hi, list):
                        poetic_hi_lines = [l.strip() for l in poetic_hi if isinstance(l, str) and l.strip()]
                    else:
                        poetic_hi_lines = []
                    
                    if poetic_hi_lines:
                        md.append("**हिन्दी काव्यात्मक भावार्थ:**  ")
                        for pl in poetic_hi_lines:
                            md.append(f"> {pl}  ")
                        md.append("")

                poetic_en = stanza_obj.get("poetic_english")
                if poetic_en:
                    if isinstance(poetic_en, str):
                        poetic_en_lines = [l.strip() for l in poetic_en.strip().split("\n") if l.strip()]
                    elif isinstance(poetic_en, list):
                        poetic_en_lines = [l.strip() for l in poetic_en if isinstance(l, str) and l.strip()]
                    else:
                        poetic_en_lines = []
                    
                    if poetic_en_lines:
                        md.append("**English Poetic Translation:**  ")
                        for pel in poetic_en_lines:
                            md.append(f"> *{pel}*  ")
                        md.append("")

        # Sufi Commentary
        commentary = k.get("sufi_commentary") or k.get("philosophical_meaning")
        if commentary:
            md.append("### दार्शनिक एवं सूफी व्याख्या (Sufi & Philosophical Commentary)\n")
            md.append(f"{commentary.strip()}\n")

        md.append("\n---\n")

    content = "\n".join(md)
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully assembled all {len(kafian)} Kafian into {OUTPUT_MD}")
    print(f"Total lines: {len(md)}, File size: {len(content.encode('utf-8')) / 1024:.2f} KB")

if __name__ == "__main__":
    assemble()
