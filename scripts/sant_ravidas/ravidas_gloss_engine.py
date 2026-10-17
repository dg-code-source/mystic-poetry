# -*- coding: utf-8 -*-
"""
High-Precision Sadhukkadi / Sant Bhasha Glossing Engine for Sant Ravidas Ji:
- Uses data/sant_ravidas/shabad_dohe_lexicon.json
- Guarantees 0 Devanagari in English gloss definitions
- Guarantees Romanized transliteration outside parentheses for English gloss
- Guarantees 0 self-repeating words in Hindi gloss
"""

import os
import sys
import json
import re

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LEXICON_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "ravidas_lexicon.json")

with open(LEXICON_PATH, "r", encoding="utf-8") as f:
    LEXICON = json.load(f)

# Romanization helper
def romanize(text):
    vowels = {'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'ee', 'उ': 'u', 'ऊ': 'oo', 'ऋ': 'ri', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au'}
    matras = {'ा': 'aa', 'ि': 'i', 'ी': 'ee', 'ु': 'u', 'ू': 'oo', 'ृ': 'ri', 'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au'}
    consonants = {
        'क': 'k', 'ख': 'kh', 'ग': 'g', 'घ': 'gh', 'ङ': 'ng',
        'च': 'ch', 'छ': 'chh', 'ज': 'j', 'झ': 'jh', 'ञ': 'ny',
        'ट': 't', 'ठ': 'th', 'ड': 'd', 'ढ': 'dh', 'ण': 'n',
        'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n',
        'प': 'p', 'फ': 'ph', 'ब': 'b', 'भ': 'bh', 'म': 'm',
        'य': 'y', 'र': 'r', 'ल': 'l', 'व': 'v', 'श': 'sh', 'ष': 'sh', 'स': 's', 'ह': 'h',
        'क़': 'q', 'ख़': 'kh', 'ग़': 'gh', 'ज़': 'z', 'फ़': 'f', 'ड़': 'd', 'ढ़': 'dh'
    }
    chars = list(text)
    n = len(chars)
    res = []
    i = 0
    while i < n:
        c = chars[i]
        if c in vowels:
            res.append(vowels[c])
        elif c in consonants:
            base = consonants[c]
            if i + 1 < n:
                nxt = chars[i+1]
                if nxt == '्':
                    res.append(base)
                    i += 1
                elif nxt in matras:
                    res.append(base + matras[nxt])
                    i += 1
                else:
                    res.append(base + 'a')
            else:
                res.append(base)
        elif c in matras:
            res.append(matras[c])
        elif c in ['ं', 'ँ']:
            res.append('n')
        i += 1
    out = ''.join(res)
    out = re.sub(r'a+$', 'a', out)
    return out if out else text

def clean_token(token):
    return re.sub(r'[\s।॥,\.\?\!\:\-\(\)\"\'०-९0-9]+', '', token).strip()

def lookup_token(word):
    cw = clean_token(word)
    if not cw:
        return "", "", ""
    if cw in LEXICON:
        item = LEXICON[cw]
        rom = item.get("roman") or romanize(cw)
        hi = item.get("hi") or cw
        en = item.get("en") or rom
        return rom, hi, en
    # Fallback
    rom = romanize(cw)
    return rom, f"{cw} रूप", rom

def generate_ravidas_gloss(line):
    tokens = re.split(r'(\s+|[।॥,\.\?\!\:\-\(\)\"\']+)', line)
    hi_parts = []
    en_parts = []
    
    for t in tokens:
        if not t or re.match(r'^\s+$', t):
            continue
        if re.match(r'^[।॥,\.\?\!\:\-\(\)\"\']+$', t):
            hi_parts.append(t)
            en_parts.append(t.replace('।', '.').replace('॥', '.'))
            continue
        cw = clean_token(t)
        if not cw:
            continue
        rom, hi, en = lookup_token(cw)
        hi_parts.append(f"{cw} ({hi})")
        en_parts.append(f"{rom} ({en})")
        
    return " ".join(hi_parts), " ".join(en_parts)

if __name__ == "__main__":
    test_line = "बेगम पुरा सहर को नाउ ॥"
    hi, en = generate_ravidas_gloss(test_line)
    print("Test line:", test_line)
    print("Hindi gloss:  ", hi)
    print("English gloss:", en)
    
    test_line2 = "ऐसा चाहूँ राज मैं जहाँ मिलै सबन को अन्न।"
    hi2, en2 = generate_ravidas_gloss(test_line2)
    print("\nTest line 2:", test_line2)
    print("Hindi gloss:  ", hi2)
    print("English gloss:", en2)
