# -*- coding: utf-8 -*-
import json
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORDS_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "words_to_translate.json")
MASTER_LEX = os.path.join(BASE_DIR, "data", "master_complete_bilingual_lexicon.json")

words = json.load(open(WORDS_PATH, encoding='utf-8'))
master = json.load(open(MASTER_LEX, encoding='utf-8'))

def get_stems(w):
    stems = []
    # If ends with ु or उ
    if w.endswith('ु') or w.endswith('उ'):
        stems.append(w[:-1])
    # If ends with ि or इ
    if w.endswith('ि') or w.endswith('इ'):
        stems.append(w[:-1])
    # If ends with ै
    if w.endswith('ै'):
        stems.append(w[:-1] + 'ा')
        stems.append(w[:-1] + 'ना')
        stems.append(w[:-1])
    # If ends with ौ
    if w.endswith('ौ'):
        stems.append(w[:-1] + 'ा')
        stems.append(w[:-1])
    # If ends with ो
    if w.endswith('ो'):
        stems.append(w[:-1] + 'ा')
        stems.append(w[:-1])
    # If ends with हु
    if w.endswith('हु'):
        stems.append(w[:-2])
    # If ends with हि
    if w.endswith('हि'):
        stems.append(w[:-2])
    # If ends with नि
    if w.endswith('नि'):
        stems.append(w[:-2])
    # If ends with ीं or ें
    if w.endswith('हीं') or w.endswith('हिं'):
        stems.append(w[:-3])
    # If ends with ँ or ं
    if w.endswith('ँ') or w.endswith('ं'):
        stems.append(w[:-1])
    return stems

direct = 0
stemmed = 0
unmatched = []

for w in words:
    if w in master:
        direct += 1
    else:
        stems = get_stems(w)
        found = False
        for s in stems:
            if s in master:
                stemmed += 1
                found = True
                break
        if not found:
            unmatched.append(w)

print(f"Total words: {len(words)}")
print(f"Direct match in master: {direct}")
print(f"Stem match in master: {stemmed}")
print(f"Total matched: {direct + stemmed} ({ (direct + stemmed)/len(words)*100:.1f}%)")
print(f"Remaining unmatched: {len(unmatched)}")
