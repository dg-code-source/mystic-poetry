import json
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def parse_farid_gloss(gloss_text):
    gloss_dict = {}
    cleaned = re.sub(r'^\s*\(|\)\s*$', '', gloss_text.strip())
    parts = re.split(r'[,;]\s*(?=[^=]+=[^=]+)', cleaned)
    for part in parts:
        part = part.strip()
        if '=' in part:
            pair = part.split('=', 1)
            term = pair[0].strip()
            meaning = pair[1].strip()
            meaning = re.sub(r'\s+', ' ', meaning)
            term = re.sub(r'\s+', ' ', term)
            if term and meaning:
                gloss_dict[term] = meaning
        elif part and gloss_dict:
            last_key = list(gloss_dict.keys())[-1]
            gloss_dict[last_key] += " " + re.sub(r'\s+', ' ', part)
    return gloss_dict

def clean_farid():
    # 1. Saloks
    with open('data/sheikh_farid/raw/salok.json', 'r', encoding='utf-8') as f:
        raw_saloks = json.load(f)
        
    cleaned_saloks = []
    all_gloss_entries = {}
    
    for s in raw_saloks:
        lines = s['lines']
        verse_lines = []
        gloss_lines = []
        
        for l in lines:
            l_str = l.strip()
            # If header/invocation
            if l_str in ['सलोक सेख फरीद के', 'ੴ सतिगुर प्रसादि']:
                continue
            if l_str.startswith('(') or '=' in l_str or l_str.endswith(')'):
                gloss_lines.append(l_str)
            else:
                verse_lines.append(l_str)
                
        raw_gloss = ' '.join(gloss_lines).strip()
        parsed_defs = parse_farid_gloss(raw_gloss)
        all_gloss_entries.update(parsed_defs)
        
        cleaned_saloks.append({
            "id": s["id"],
            "title": s["title"],
            "lines": verse_lines,
            "raw_gloss": raw_gloss,
            "gloss_dict": parsed_defs
        })
        
    out_salok = 'data/sheikh_farid/cleaned_salok.json'
    with open(out_salok, 'w', encoding='utf-8') as f:
        json.dump(cleaned_saloks, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(cleaned_saloks)} cleaned Saloks to {out_salok}")
    
    # 2. Shabads
    with open('data/sheikh_farid/raw/shabad.json', 'r', encoding='utf-8') as f:
        raw_shabads = json.load(f)
        
    cleaned_shabads = []
    for s in raw_shabads:
        lines = [l.strip() for l in s['lines'] if l.strip() and l.strip() != 'ੴ सतिगुर प्रसादि']
        cleaned_shabads.append({
            "id": s["id"],
            "title": s["title"],
            "lines": lines
        })
        
    out_shabad = 'data/sheikh_farid/cleaned_shabad.json'
    with open(out_shabad, 'w', encoding='utf-8') as f:
        json.dump(cleaned_shabads, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(cleaned_shabads)} cleaned Shabads to {out_shabad}")
    
    print(f"Extracted {len(all_gloss_entries)} vocabulary definitions from Saloks.")

if __name__ == '__main__':
    clean_farid()
