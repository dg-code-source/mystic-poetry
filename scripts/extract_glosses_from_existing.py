# -*- coding: utf-8 -*-
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

words_needed = set(json.load(open('data/words_to_translate.json', encoding='utf-8')))
print(f"Target words needed: {len(words_needed)}")

extracted = {}

for fn in ['Bulleh_Shah_Kafian.md', 'Bulleh_Shah_Baranmah_Trilingual.md', 'Bulleh_Shah_Athwara_Trilingual.md']:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    
    blocks = re.findall(r'\*\*हिन्दी शब्दार्थ:\*\*\s*(.+?)\n\*\*English Gloss:\*\*\s*(.+?)\n', content)
    for hi_line, en_line in blocks:
        hi_items = re.findall(r'([\u0900-\u097F]+)\s*\(([^)]+)\)', hi_line)
        en_items = re.findall(r'([a-zA-Z\u0900-\u097F]+)\s*\(([^)]+)\)', en_line)
        
        # If lengths match or can be aligned
        if len(hi_items) == len(en_items):
            for i in range(len(hi_items)):
                hw, hm = hi_items[i]
                ew, em = en_items[i]
                cw = re.sub(r'[\s।॥,\.\?\!\:\-\(\)\"\'०-९0-9]+', '', hw).strip()
                # Ensure no devanagari in English gloss
                if cw and cw in words_needed and not re.search(r'[\u0900-\u097F]', em):
                    # Also ensure it's not a self-repeat
                    if hm != cw and em.lower() != cw.lower():
                        if cw not in extracted:
                            extracted[cw] = {
                                "roman": ew.lower(),
                                "hi": hm.strip(),
                                "en": em.strip()
                            }

print(f"Found clean, verified translations for {len(extracted)} / {len(words_needed)} words directly from Kafian, Baranmah, and Athwara!")
with open('data/extracted_from_existing.json', 'w', encoding='utf-8') as f:
    json.dump(extracted, f, ensure_ascii=False, indent=2)
