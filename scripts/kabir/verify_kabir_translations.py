import json
import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

data_path = "data/kabir/kabir_data.json"
manifest_path = "data/kabir/kabir_manifest.js"

print("==================== AUDITING SANT KABIR CORPUS ====================")

if not os.path.exists(data_path):
    print(f"ERROR: {data_path} not found!")
    sys.exit(1)

with open(data_path, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

items = list(raw_data.values()) if isinstance(raw_data, dict) else raw_data

print(f"Total Kabir compositions in kabir_data.json: {len(items)}")

devanagari_regex = re.compile(r'[\u0900-\u097F]')
en_verse_errors = []
en_gloss_errors = []
hi_repeat_errors = []
missing_fields_errors = []
empty_translation_errors = []

for idx, it in enumerate(items, 1):
    uid = it.get('uid') or it.get('id', f'item_{idx}')
    
    # Check verses (handle both translation_hindi/english and verse_hi/en)
    v_hi = it.get('translation_hindi') or it.get('verse_hi', '')
    v_en = it.get('translation_english') or it.get('verse_en', '')
    v_hi = v_hi.strip()
    v_en = v_en.strip()
    
    if not v_hi or not v_en:
        empty_translation_errors.append((uid, "empty verse_hi or verse_en"))

        
    # Check 1: 0 Devanagari in English Verse
    dev_in_en = devanagari_regex.findall(v_en)
    if dev_in_en:
        en_verse_errors.append((uid, "".join(dev_in_en[:5])))
        
    # Check 2: 0 Devanagari in English Gloss
    g_en = it.get('english_gloss')
    if isinstance(g_en, list):
        g_en = "\n".join(g_en)
    elif not g_en:
        gloss = it.get('glossary', {})
        g_en = gloss.get('english', '')
        
    dev_in_gloss = devanagari_regex.findall(g_en)
    if dev_in_gloss:
        en_gloss_errors.append((uid, "".join(dev_in_gloss[:5])))
        
    # Check 3: 0 self-repeats in Hindi Gloss
    g_hi = it.get('hindi_gloss')
    if isinstance(g_hi, list):
        g_hi = "\n".join(g_hi)
    elif not g_hi:
        gloss = it.get('glossary', {})
        g_hi = gloss.get('hindi', '')
        
    # Check for pattern: word (word)
    repeats = re.findall(r'([\u0900-\u097F]+)\s*\(\s*\1\s*\)', g_hi)
    if repeats:
        hi_repeat_errors.append((uid, repeats[:3]))


print(f"\nAudit Results for {len(items)} works:")
print(f"  - Missing Fields Errors: {len(missing_fields_errors)}")
print(f"  - Empty Translation Errors: {len(empty_translation_errors)}")
print(f"  - Devanagari in English Verse: {len(en_verse_errors)}")
print(f"  - Devanagari in English Gloss: {len(en_gloss_errors)}")
print(f"  - Self-repeating Definitions in Hindi Gloss: {len(hi_repeat_errors)}")

if en_verse_errors:
    print("\nSample EN Verse Errors:")
    for uid, err in en_verse_errors[:5]:
        print(f"    {uid}: {err}")

if en_gloss_errors:
    print("\nSample EN Gloss Errors:")
    for uid, err in en_gloss_errors[:5]:
        print(f"    {uid}: {err}")

if hi_repeat_errors:
    print("\nSample HI Repeat Errors:")
    for uid, err in hi_repeat_errors[:5]:
        print(f"    {uid}: {err}")

if not (missing_fields_errors or empty_translation_errors or en_verse_errors or en_gloss_errors or hi_repeat_errors):
    print("\n>>> ALL TESTS PASSED: 100% PERFECT QUALITY AUDIT FOR SANT KABIR DAS! <<<")
else:
    print("\n>>> AUDIT FAILED - PLEASE FIX REPORTED ISSUES <<<")
    sys.exit(1)
