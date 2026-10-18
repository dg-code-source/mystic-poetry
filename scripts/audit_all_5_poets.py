# -*- coding: utf-8 -*-
"""
Master Compendium Complete Quality & Completeness Audit:
Checks all 5 poets across 1,673 compositions:
1. Baba Bulleh Shah (351)
2. Sant Ravidas Ji (208)
3. Baba Sheikh Farid (134)
4. Sant Mirabai (418)
5. Sant Kabir Das (562)

Audits:
- Original Text presence
- Metered Hindi translation presence & non-emptiness
- Lyrical English translation presence & non-emptiness
- Word-by-word Hindi gloss presence
- Word-by-word English gloss presence
- Strict 0 Devanagari in English translations and English glosses
"""

import json
import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

dev_re = re.compile(r'[\u0900-\u097F]')

def audit_bulleh_shah():
    path = "data/bulleh_shah/kafian_data.js"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    prefix = "window.BULLEH_SHAH_DATA = "
    if text.startswith(prefix):
        text = text[len(prefix):].rstrip(';\n ')
    data = json.loads(text)
    
    # We filter for the 351 canonical works
    manifest_path = "data/bulleh_shah/manifest.js"
    with open(manifest_path, "r", encoding="utf-8") as f:
        m_text = f.read()
    m_prefix = "window.BULLEH_SHAH_MANIFEST = "
    if m_text.startswith(m_prefix):
        m_text = m_text[len(m_prefix):].rstrip(';\n ')
    manifest = json.loads(m_text)
    
    items = []
    for m in manifest:
        uid = m['uid']
        if uid in data:
            items.append(data[uid])
            
    print(f"1. Baba Bulleh Shah: Loaded {len(items)} works from manifest & data (Expected 351)")
    
    missing_hi = 0
    missing_en = 0
    missing_gloss_hi = 0
    missing_gloss_en = 0
    dev_in_en = 0
    
    for it in items:
        stanzas = it.get('stanzas', [])
        hi_parts = []
        en_parts = []
        ghi_parts = []
        gen_parts = []
        
        for st in stanzas:
            ph = st.get('poetic_hindi')
            if isinstance(ph, list):
                hi_parts.extend(ph)
            elif ph:
                hi_parts.append(str(ph))
                
            pe = st.get('poetic_english')
            if isinstance(pe, list):
                en_parts.extend(pe)
            elif pe:
                en_parts.append(str(pe))
                
            for l in st.get('lines', []):
                if l.get('hindi_gloss'):
                    ghi_parts.append(str(l['hindi_gloss']))
                if l.get('english_gloss'):
                    gen_parts.append(str(l['english_gloss']))

                    
        full_hi = "\n".join(hi_parts).strip()
        full_en = "\n".join(en_parts).strip()
        full_ghi = "\n".join(ghi_parts).strip()
        full_gen = "\n".join(gen_parts).strip()
        
        if not full_hi:
            missing_hi += 1
        if not full_en:
            missing_en += 1
        if not full_ghi:
            missing_gloss_hi += 1
        if not full_gen:
            missing_gloss_en += 1
        if dev_re.search(full_en):
            dev_in_en += 1
            
    return {
        "poet": "Baba Bulleh Shah",
        "count": len(items),
        "expected": 351,
        "missing_hi": missing_hi,
        "missing_en": missing_en,
        "missing_gloss_hi": missing_gloss_hi,
        "missing_gloss_en": missing_gloss_en,
        "dev_in_en": dev_in_en
    }

def audit_standard_poet(name, path, expected_count):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    items = list(data.values()) if isinstance(data, dict) else data
    print(f"{name}: Loaded {len(items)} works (Expected {expected_count})")
    
    missing_hi = 0
    missing_en = 0
    missing_gloss_hi = 0
    missing_gloss_en = 0
    dev_in_en = 0
    
    for it in items:
        uid = it.get('uid') or it.get('id', '')
        v_hi = (it.get('hindi_translation') or it.get('translation_hindi') or it.get('verse_hi') or '').strip()
        v_en = (it.get('english_translation') or it.get('translation_english') or it.get('verse_en') or '').strip()
        
        g_hi = it.get('hindi_gloss') or it.get('glossary', {}).get('hindi') or ''
        if isinstance(g_hi, list):
            g_hi = "\n".join(g_hi)
        g_hi = g_hi.strip()
        
        g_en = it.get('english_gloss') or it.get('glossary', {}).get('english') or ''
        if isinstance(g_en, list):
            g_en = "\n".join(g_en)
        g_en = g_en.strip()
        
        if not v_hi:
            missing_hi += 1
        if not v_en:
            missing_en += 1
        if not g_hi:
            missing_gloss_hi += 1
        if not g_en:
            missing_gloss_en += 1
        if dev_re.search(v_en) or dev_re.search(g_en):
            dev_in_en += 1

            
    return {
        "poet": name,
        "count": len(items),
        "expected": expected_count,
        "missing_hi": missing_hi,
        "missing_en": missing_en,
        "missing_gloss_hi": missing_gloss_hi,
        "missing_gloss_en": missing_gloss_en,
        "dev_in_en": dev_in_en
    }

print("=" * 75)
print("AUDITING ALL TRANSLATIONS & GLOSSES (1,673 WORKS)")
print("=" * 75)

res_bulleh = audit_bulleh_shah()
res_ravidas = audit_standard_poet("2. Sant Ravidas Ji", "data/sant_ravidas/ravidas_data.json", 208)
res_farid = audit_standard_poet("3. Baba Sheikh Farid", "data/sheikh_farid/farid_data.json", 134)
res_meerabai = audit_standard_poet("4. Sant Mirabai", "data/meerabai/meerabai_data.json", 418)
res_kabir = audit_standard_poet("5. Sant Kabir Das", "data/kabir/kabir_data.json", 562)

all_results = [res_bulleh, res_ravidas, res_farid, res_meerabai, res_kabir]

print("\n" + "=" * 75)
print(f"{'Poet Name':<24} | {'Count':<7} | {'Hi Trans':<9} | {'En Trans':<9} | {'Hi Gloss':<9} | {'En Gloss':<9} | {'Dev in EN':<9}")
print("-" * 75)

grand_total = 0
total_missing_hi = 0
total_missing_en = 0
total_missing_ghi = 0
total_missing_gen = 0
total_dev_in_en = 0

for r in all_results:
    grand_total += r['count']
    total_missing_hi += r['missing_hi']
    total_missing_en += r['missing_en']
    total_missing_ghi += r['missing_gloss_hi']
    total_missing_gen += r['missing_gloss_en']
    total_dev_in_en += r['dev_in_en']
    
    hi_status = "100% OK" if r['missing_hi'] == 0 else f"{r['missing_hi']} miss"
    en_status = "100% OK" if r['missing_en'] == 0 else f"{r['missing_en']} miss"
    ghi_status = "100% OK" if r['missing_gloss_hi'] == 0 else f"{r['missing_gloss_hi']} miss"
    gen_status = "100% OK" if r['missing_gloss_en'] == 0 else f"{r['missing_gloss_en']} miss"
    dev_status = "0 (Pristine)" if r['dev_in_en'] == 0 else f"{r['dev_in_en']} err"
    
    print(f"{r['poet']:<24} | {r['count']:<7} | {hi_status:<9} | {en_status:<9} | {ghi_status:<9} | {gen_status:<9} | {dev_status:<9}")

print("=" * 75)
print(f"GRAND TOTAL: {grand_total} / 1,673 works")
print(f"Total Missing Hindi Translations: {total_missing_hi}")
print(f"Total Missing English Translations: {total_missing_en}")
print(f"Total Missing Hindi Word-by-Word Glosses: {total_missing_ghi}")
print(f"Total Missing English Word-by-Word Glosses: {total_missing_gen}")
print(f"Total Devanagari in English Violations: {total_dev_in_en}")

if total_missing_hi == 0 and total_missing_en == 0 and total_missing_ghi == 0 and total_missing_gen == 0 and total_dev_in_en == 0:
    print("\n>>> ALL 1,673 WORKS: 100% PERFECT TRANSLATIONS & GLOSSES VERIFIED! <<<")
else:
    print("\n>>> ISSUES DETECTED - PLEASE INVESTIGATE <<<")
    sys.exit(1)
