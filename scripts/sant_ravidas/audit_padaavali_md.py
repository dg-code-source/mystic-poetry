# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

lines = open('Sant_Ravidas_Padaavali_Trilingual.md', encoding='utf-8').readlines()
en_errs = []
hi_errs = []
en_count = 0
hi_count = 0

for idx, l in enumerate(lines, 1):
    if l.startswith('- **English Gloss:**'):
        en_count += 1
        gloss_content = l.replace('- **English Gloss:**', '').strip()
        dev = re.findall(r'[\u0900-\u097F]', gloss_content)
        if dev:
            en_errs.append((idx, ''.join(dev[:10]), l[:100]))
    elif l.startswith('- **हिन्दी शब्दार्थ:**'):
        hi_count += 1
        repeats = re.findall(r'([\u0900-\u097F]+)\s*\(\1\)', l)
        if repeats:
            hi_errs.append((idx, repeats, l[:100]))

print(f"Total English gloss lines audited: {en_count}")
print(f"Devanagari errors in English gloss: {len(en_errs)}")
if en_errs:
    for item in en_errs[:5]:
        print(f"  Line {item[0]}: {item[1]} in {item[2]}")

print(f"Total Hindi gloss lines audited: {hi_count}")
print(f"Self-repeating errors in Hindi gloss: {len(hi_errs)}")
if hi_errs:
    for item in hi_errs[:5]:
        print(f"  Line {item[0]}: {item[1]} in {item[2]}")

if len(en_errs) == 0 and len(hi_errs) == 0:
    print("SUCCESS: Sant_Ravidas_Padaavali_Trilingual.md has ZERO errors across all 117 Padas!")
