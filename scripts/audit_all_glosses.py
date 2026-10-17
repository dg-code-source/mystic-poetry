import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('data/kafian_data.json', encoding='utf-8'))
print(f"Total keys in dataStore: {len(data)}")

issues_by_genre = {}

for key, item in data.items():
    genre = item.get('genre', 'unknown')
    if genre not in issues_by_genre:
        issues_by_genre[genre] = {
            'total_lines': 0,
            'devanagari_in_en': 0,
            'empty_parens': 0,
            'self_repeat': 0,
            'sample_issues': []
        }
        
    stanzas = item.get('stanzas', [])
    for st in stanzas:
        lines = st.get('lines', [])
        for l in lines:
            if not isinstance(l, dict):
                continue
            issues_by_genre[genre]['total_lines'] += 1
            en_gloss = l.get('english_gloss', '')
            hi_gloss = l.get('hindi_gloss', '')
            
            has_issue = False
            issue_desc = []
            
            # 1. Check empty parens
            if '()' in en_gloss or '()' in hi_gloss:
                issues_by_genre[genre]['empty_parens'] += 1
                has_issue = True
                issue_desc.append("empty parens ()")
                
            # 2. Check Devanagari inside English gloss parentheses
            m = re.findall(r'\(([^)]+)\)', en_gloss)
            dev_in_en = any(re.search(r'[\u0900-\u097F]', g) for g in m)
            if dev_in_en:
                issues_by_genre[genre]['devanagari_in_en'] += 1
                has_issue = True
                issue_desc.append("devanagari in English gloss")
                
            # 3. Check self-repeat like सुन्यार (सुन्यार)
            repeat_hi = re.search(r'([\u0900-\u097F]+)\s*\(\1\)', hi_gloss)
            repeat_en = re.search(r'([\u0900-\u097F]+)\s*\(\1\)', en_gloss)
            if repeat_hi or repeat_en:
                issues_by_genre[genre]['self_repeat'] += 1
                has_issue = True
                issue_desc.append("self-repeat word(word)")
                
            if has_issue and len(issues_by_genre[genre]['sample_issues']) < 3:
                issues_by_genre[genre]['sample_issues'].append({
                    'item': item.get('title'),
                    'line': l.get('original'),
                    'issue': ", ".join(issue_desc),
                    'hi': hi_gloss,
                    'en': en_gloss
                })

print("=" * 60)
print("AUDIT SUMMARY ACROSS ALL 6 GENRES")
print("=" * 60)
for g, counts in issues_by_genre.items():
    print(f"\nGenre: [{g.upper()}] (Total lines evaluated: {counts['total_lines']})")
    print(f"  - Devanagari inside English gloss: {counts['devanagari_in_en']}")
    print(f"  - Empty parentheses (): {counts['empty_parens']}")
    print(f"  - Self-repeated word(word): {counts['self_repeat']}")
    if counts['sample_issues']:
        print("  Sample Issues:")
        for s in counts['sample_issues']:
            print(f"    * In '{s['item']}': {s['issue']}")
            print(f"      Orig: {s['line']}")
            print(f"      Hi:   {s['hi']}")
            print(f"      En:   {s['en']}")
