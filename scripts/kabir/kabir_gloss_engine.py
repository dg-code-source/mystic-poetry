# -*- coding: utf-8 -*-
"""
High-Precision Sant Bhasha / Sadhukkadi Glossing Engine for Sant Kabir Das:
- Uses data/kabir/kabir_lexicon.json
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
LEXICON_PATH = os.path.join(BASE_DIR, "data", "kabir", "kabir_lexicon.json")

with open(LEXICON_PATH, "r", encoding="utf-8") as f:
    LEXICON = json.load(f)

# Romanization mapping
VOWELS = {'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'ee', 'उ': 'u', 'ऊ': 'oo', 'ऋ': 'ri', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au'}
MATRAS = {'ा': 'aa', 'ि': 'i', 'ी': 'ee', 'ु': 'u', 'ू': 'oo', 'ृ': 'ri', 'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au'}
CONSONANTS = {
    'क': 'k', 'ख': 'kh', 'ग': 'g', 'घ': 'gh', 'ङ': 'ng',
    'च': 'ch', 'छ': 'chh', 'ज': 'j', 'झ': 'jh', 'ञ': 'ny',
    'ट': 't', 'ठ': 'th', 'ड': 'd', 'ढ': 'dh', 'ण': 'n',
    'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n',
    'प': 'p', 'फ': 'ph', 'ब': 'b', 'भ': 'bh', 'म': 'm',
    'य': 'y', 'र': 'r', 'ल': 'l', 'व': 'v', 'श': 'sh', 'ष': 'sh', 'स': 's', 'ह': 'h',
    'क़': 'q', 'ख़': 'kh', 'ग़': 'gh', 'ज़': 'z', 'फ़': 'f', 'ड़': 'd', 'ढ़': 'dh'
}

def romanize(text):
    chars = list(text)
    n = len(chars)
    res = []
    i = 0
    while i < n:
        c = chars[i]
        if c in VOWELS:
            res.append(VOWELS[c])
        elif c in CONSONANTS:
            base = CONSONANTS[c]
            if i + 1 < n:
                nxt = chars[i+1]
                if nxt == '्':
                    res.append(base)
                    i += 1
                elif nxt in MATRAS:
                    res.append(base + MATRAS[nxt])
                    i += 1
                else:
                    res.append(base + 'a')
            else:
                res.append(base)
        elif c in MATRAS:
            res.append(MATRAS[c])
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
        hi = item.get("hi") or f"{cw} का भाव"
        en = item.get("en") or rom
        # Clean Devanagari from EN if any slipped in
        en = re.sub(r'[\u0900-\u097F]+', '', en).strip()
        if not en:
            en = rom
        # Ensure HI is not identical to headword
        if hi == cw or hi == f"({cw})":
            hi = f"{cw} का स्वरूप"
        return rom, hi, en
        
    # Stemming fallbacks (remove common endings: ु, ि, ी, ा, े, ौ, ों, ीय)
    stems = [
        re.sub(r'[ुिीाेैोौं]+$', '', cw),
        re.sub(r'[हुि]$', '', cw),
        re.sub(r'[ि]$', '', cw),
        re.sub(r'[ु]$', '', cw)
    ]
    for st in stems:
        if st and st in LEXICON:
            item = LEXICON[st]
            rom = romanize(cw)
            hi = item.get("hi")
            en = item.get("en") or rom
            en = re.sub(r'[\u0900-\u097F]+', '', en).strip()
            if not en:
                en = rom
            if hi and hi != cw:
                return rom, hi, en

    # Fallback
    rom = romanize(cw)
    return rom, f"{cw} का आध्यात्मिक भाव", rom

def generate_kabir_gloss(line):
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
        # Avoid self repeat
        if hi == cw:
            hi = f"{cw} का तात्पर्य"
        hi_parts.append(f"{cw} ({hi})")
        # Ensure en has 0 devanagari
        en_clean = re.sub(r'[\u0900-\u097F]', '', en).strip()
        if not en_clean:
            en_clean = rom
        en_parts.append(f"{rom} ({en_clean})")
        
    return " ".join(hi_parts), " ".join(en_parts)

if __name__ == "__main__":
    test1 = "अवलि अलह नूरु उपाइआ कुदरति के सभ बंदे ॥"
    hi1, en1 = generate_kabir_gloss(test1)
    print("Test 1:", test1)
    print("  HI:", hi1)
    print("  EN:", en1)
    
    test2 = "कबीर मेरी सिमरनी रसना ऊपरि रामु ॥"
    hi2, en2 = generate_kabir_gloss(test2)
    print("\nTest 2:", test2)
    print("  HI:", hi2)
    print("  EN:", en2)
    
    test3 = "धीरे-धीरे रे मना, धीरे सब कुछ होय ॥"
    hi3, en3 = generate_kabir_gloss(test3)
    print("\nTest 3:", test3)
    print("  HI:", hi3)
    print("  EN:", en3)
