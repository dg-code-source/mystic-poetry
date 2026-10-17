# -*- coding: utf-8 -*-
import json
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORDS_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "words_to_translate.json")
MASTER_PATH = os.path.join(BASE_DIR, "data", "master_complete_bilingual_lexicon.json")

words = json.load(open(WORDS_PATH, encoding='utf-8'))
master = json.load(open(MASTER_PATH, encoding='utf-8'))

# Phonetic normalization patterns for Sadhukkadi -> Standard Hindi
def normalize_phonetics(w):
    cand = []
    # gyan variants
    if 'ग्यां' in w:
        cand.append(w.replace('ग्यां', 'ज्ञान'))
    if 'ग्या' in w:
        cand.append(w.replace('ग्या', 'ज्ञा'))
    # anusvara before m
    if 'नांम' in w:
        cand.append(w.replace('नांम', 'नाम'))
    if 'कांम' in w:
        cand.append(w.replace('कांम', 'काम'))
    if 'धांम' in w:
        cand.append(w.replace('धांम', 'धाम'))
    # b -> v
    if w.startswith('बि'):
        cand.append('वि' + w[2:])
    if w.startswith('ब'):
        cand.append('व' + w[1:])
    # s -> sh
    if 'स' in w:
        cand.append(w.replace('स', 'श'))
    # kh -> sh (braj/sadhukkadi khashti sha)
    if 'ख' in w:
        cand.append(w.replace('ख', 'ष'))
    # single consonant for conjuncts
    if 'सिधि' in w:
        cand.append(w.replace('सिधि', 'सिद्धि'))
    if 'बुधि' in w:
        cand.append(w.replace('बुधि', 'बुद्धि'))
    if 'सुधि' in w:
        cand.append(w.replace('सुधि', 'शुद्धि'))
    if 'मुकति' in w:
        cand.append(w.replace('मुकति', 'मुक्ति'))
    if 'भगति' in w:
        cand.append(w.replace('भगति', 'भक्ति'))
    if 'सकति' in w:
        cand.append(w.replace('सकति', 'शक्ति'))
    if 'जुगति' in w:
        cand.append(w.replace('जुगति', 'युक्ति'))
    if 'बरन' in w:
        cand.append(w.replace('बरन', 'वर्ण'))
    if 'करम' in w:
        cand.append(w.replace('करम', 'कर्म'))
    if 'धरम' in w:
        cand.append(w.replace('धरम', 'धर्म'))
    if 'सरब' in w:
        cand.append(w.replace('सरब', 'सर्व'))
    if 'परगट' in w:
        cand.append(w.replace('परगट', 'प्रकट'))
    if 'परकास' in w:
        cand.append(w.replace('परकास', 'प्रकाश'))
    if 'दरसन' in w:
        cand.append(w.replace('दरसन', 'दर्शन'))
    if 'सरन' in w:
        cand.append(w.replace('सरन', 'शरण'))
    if 'चरन' in w:
        cand.append(w.replace('चरन', 'चरण'))
    if 'पिरथमी' in w or 'प्रथमी' in w:
        cand.append('पृथ्वी')
    return cand

matches = 0
for w in words:
    for c in normalize_phonetics(w):
        if c in master:
            matches += 1
            break

print(f"Phonetic normalization yielded additional matches: {matches}")
