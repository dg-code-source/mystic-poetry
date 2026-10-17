# -*- coding: utf-8 -*-
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

words_needed = json.load(open('data/words_to_translate.json', encoding='utf-8'))
lex = json.load(open('data/master_complete_bilingual_lexicon.json', encoding='utf-8'))
extracted = json.load(open('data/extracted_from_existing.json', encoding='utf-8'))

# Check which words still need proper Hindi and English meanings
unmapped = []
for w in words_needed:
    # Check if in extracted
    if w in extracted:
        continue
    # Check if in lex and not self-repeat
    item = lex.get(w)
    if item:
        hi = item.get('hi', '')
        en = item.get('en', '')
        rom = item.get('roman', '')
        if hi and hi != w and en and en != rom and not re.search(r'[\u0900-\u097F]', en):
            continue
    unmapped.append(w)

print(f"Total words requiring precise classical translation: {len(unmapped)}")
with open('data/unmapped_words.json', 'w', encoding='utf-8') as f:
    json.dump(unmapped, f, ensure_ascii=False, indent=2)
print("Saved unmapped list to data/unmapped_words.json")
