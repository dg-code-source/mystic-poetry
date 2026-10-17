import sys, json, re
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')
lex = json.load(open('data/punjabi_sufi_lexicon.json', encoding='utf-8'))
counts = Counter()
for fname in ['dohre.json', 'gandhan.json', 'siharfian.json']:
    data = json.load(open(f'data/raw_extracted/{fname}', encoding='utf-8'))
    txt = json.dumps(data, ensure_ascii=False)
    raw_words = re.findall(r'[\u0900-\u097F]+', txt)
    for rw in raw_words:
        w = re.sub(r'[\s।॥,\.\?\!\:\-\(\)\"\']+', '', rw).strip()
        w = re.sub(r'[०-९0-9]+', '', w)
        if w and w not in lex:
            counts[w] += 1

print("Top 50 missing words by frequency:")
for w, c in counts.most_common(50):
    print(f"{w}: {c}")
