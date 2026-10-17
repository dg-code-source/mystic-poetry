import os
import re
import json
import bs4
import sys

sys.stdout.reconfigure(encoding='utf-8')

def parse_gloss_definitions(gloss_str):
    gloss_dict = {}
    if not gloss_str:
        return gloss_dict
    
    # Strip enclosing parentheses
    cleaned = re.sub(r'^\s*\(|\)\s*$', '', gloss_str.strip())
    # Split by comma or semicolon when followed by a term or word
    # Notice terms might have multiple synonyms like "करबत,करवत=आरे से कटना"
    parts = re.split(r'[,;]\s*(?=[^=]+=[^=]+)', cleaned)
    for part in parts:
        part = part.strip()
        if '=' in part:
            pair = part.split('=', 1)
            term = pair[0].strip()
            meaning = pair[1].strip()
            # Clean newlines inside meaning
            meaning = re.sub(r'\s+', ' ', meaning)
            term = re.sub(r'\s+', ' ', term)
            if term and meaning:
                gloss_dict[term] = meaning
        elif part and gloss_dict:
            # might be continuation of previous definition
            last_key = list(gloss_dict.keys())[-1]
            gloss_dict[last_key] += " " + re.sub(r'\s+', ' ', part)
            
    return gloss_dict

def parse_meerabai_all():
    all_poems = []
    global_id = 0
    
    for part_num in range(1, 10):
        filepath = f"data/meerabai/raw/html/part_{part_num}.html"
        if not os.path.exists(filepath):
            print(f"Error: {filepath} does not exist!")
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
            
        # Cut off footer / external links
        for stop_marker in ['class="links-container"', 'class="footer"', '<div class="footer"']:
            pos = text.find(stop_marker)
            if pos != -1:
                text = text[:pos]
                
        h3_matches = list(re.finditer(r'<h3[^>]*>(.*?)</h3>', text, re.IGNORECASE | re.DOTALL))
        print(f"Part {part_num}: found {len(h3_matches)} poems")
        
        for idx, m in enumerate(h3_matches):
            global_id += 1
            h3_html = m.group(0)
            h3_content = m.group(1)
            
            start = m.end()
            end = h3_matches[idx + 1].start() if idx + 1 < len(h3_matches) else len(text)
            body_html = text[start:end]
            
            # Extract anchor
            anchor_m = re.search(r'name=["\']?([^"\'>\s]+)', h3_html)
            anchor = anchor_m.group(1) if anchor_m else ""
            
            # Strip tags from title
            raw_title = re.sub(r'<[^>]+>', '', h3_content).strip()
            num_match = re.match(r"^(\d+)[\.\s]+(.*)$", raw_title)
            if num_match:
                orig_num = int(num_match.group(1))
                clean_title = num_match.group(2).strip()
            else:
                orig_num = global_id
                clean_title = raw_title
                
            # Clean body html
            cleaned = re.sub(r'<(?:br|p|/p)[^>]*>', '\n', body_html, flags=re.IGNORECASE)
            cleaned = re.sub(r'<[^>]+>', '', cleaned)
            
            raw_lines = [l.strip() for l in cleaned.split('\n') if l.strip()]
            
            verse_lines = []
            gloss_lines = []
            for l in raw_lines:
                # If line is part of glossary
                if l.startswith('(') or '=' in l or l.endswith(')') or (gloss_lines and not any(mark in l for mark in ['।', '॥'])):
                    gloss_lines.append(l)
                else:
                    verse_lines.append(l)
                    
            raw_gloss_str = ' '.join(gloss_lines).strip()
            gloss_dict = parse_gloss_definitions(raw_gloss_str)
            
            all_poems.append({
                "id": global_id,
                "part": part_num,
                "orig_num": orig_num,
                "anchor": anchor,
                "title": clean_title,
                "lines": verse_lines,
                "raw_gloss": raw_gloss_str,
                "gloss_dict": gloss_dict
            })
            
    print(f"\nSuccessfully parsed {len(all_poems)} Sant Mirabai poems.")
    out_file = "data/meerabai/raw/padavali.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_poems, f, ensure_ascii=False, indent=2)
    print(f"Saved complete raw dataset to {out_file} ({os.path.getsize(out_file)} bytes)")
    
    # Validation checks
    empty_lines = [p for p in all_poems if len(p['lines']) == 0]
    has_gloss = [p for p in all_poems if p['gloss_dict']]
    print(f"Poems with empty lines: {len(empty_lines)}")
    print(f"Poems with parsed vocabulary gloss: {len(has_gloss)}")
    if empty_lines:
        print("Empty poems sample:", empty_lines[:3])

if __name__ == "__main__":
    parse_meerabai_all()
