# -*- coding: utf-8 -*-
"""
Tests orthographic normalization and root matching for Sant Ravidas vocabulary.
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORDS_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "words_to_translate.json")
MASTER_LEX_PATH = os.path.join(BASE_DIR, "data", "master_complete_bilingual_lexicon.json")

words = json.load(open(WORDS_PATH, encoding='utf-8'))
master_lex = json.load(open(MASTER_LEX_PATH, encoding='utf-8'))

def normalize_orthography(w):
    cand = []
    # 1. Nasal
    cand.append(w.replace('ं', '').replace('ँ', ''))
    cand.append(w.replace('ँ', 'ं'))
    # 2. Geminates in Sant Bhasha
    cand.append(w.replace('करंम', 'कर्म').replace('धरंम', 'धर्म').replace('परंम', 'परम').replace('भरंम', 'भ्रम'))
    # 3. Sibilant
    cand.append(w.replace('स', 'श'))
    cand.append(w.replace('स', 'ष'))
    cand.append(w.replace('श', 'स'))
    cand.append(w.replace('ष', 'स'))
    # 4. Glide b/v
    cand.append(w.replace('ब', 'व'))
    cand.append(w.replace('व', 'ब'))
    # 5. Diphthong
    cand.append(w.replace('अउ', 'औ').replace('अइ', 'ऐ'))
    # 6. Case endings
    for sfx in ['हु', 'हि', 'उ', 'इ', 'ै', 'ौ', 'नि', 'ां', 'े']:
        if w.endswith(sfx) and len(w) > len(sfx) + 1:
            cand.append(w[:-len(sfx)])
            cand.append(w[:-len(sfx)] + 'ा')
            cand.append(w[:-len(sfx)] + 'ना')
    return list(set(cand))

resolved = 0
for w in words:
    if w in master_lex:
        resolved += 1
        continue
    cands = normalize_orthography(w)
    if any(c in master_lex for c in cands):
        resolved += 1

print(f"Total tokens resolved via normalization against Master Lexicon: {resolved} / {len(words)} ({resolved/len(words)*100:.1f}%)")
