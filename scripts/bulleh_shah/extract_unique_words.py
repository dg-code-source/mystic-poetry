import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')
all_words = set()
for fn in ['data/other_works/dohre.json', 'data/other_works/gandhan.json', 'data/other_works/siharfian.json']:
    data = json.load(open(fn, encoding='utf-8'))
    txt = json.dumps(data, ensure_ascii=False)
    for l in re.findall(r'"original":\s*"([^"]+)"', txt):
        words = re.findall(r'[\u0900-\u097F]+', l)
        for w in words:
            cw = re.sub(r'[\s।॥,\.\?\!\:\-\(\)\"\'०-९0-9]+', '', w).strip()
            if cw:
                all_words.add(cw)

print(f"Total unique words across Dohre, Gandhan, Siharfian: {len(all_words)}")
with open('data/words_to_translate.json', 'w', encoding='utf-8') as f:
    json.dump(sorted(list(all_words)), f, ensure_ascii=False, indent=2)
print("Saved to data/words_to_translate.json")
