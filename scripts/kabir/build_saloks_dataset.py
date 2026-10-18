# -*- coding: utf-8 -*-
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

from saloks_part1 import SALOKS_PART1
from saloks_part2 import SALOKS_PART2
from saloks_part3 import SALOKS_PART3
from saloks_part4 import SALOKS_PART4

print(f"Saloks Part 1: {len(SALOKS_PART1)}")
print(f"Saloks Part 2: {len(SALOKS_PART2)}")
print(f"Saloks Part 3: {len(SALOKS_PART3)}")
print(f"Saloks Part 4: {len(SALOKS_PART4)}")

all_saloks = {}
all_saloks.update(SALOKS_PART1)
all_saloks.update(SALOKS_PART2)
all_saloks.update(SALOKS_PART3)
all_saloks.update(SALOKS_PART4)

print(f"Total Combined Saloks: {len(all_saloks)}")

# Verify 1 to 245
missing = [i for i in range(1, 246) if i not in all_saloks]
if missing:
    print(f"ERROR: Missing saloks: {missing}")
    sys.exit(1)

devanagari_regex = re.compile(r'[\u0900-\u097F]')
dev_violations = 0
for num, s in all_saloks.items():
    for field in ['theme_en', 'title_en', 'v_en']:
        text = s.get(field, '')
        if devanagari_regex.search(text):
            print(f"Devanagari violation in Salok {num} field {field}: {text}")
            dev_violations += 1

if dev_violations > 0:
    print(f"ERROR: Found {dev_violations} Devanagari violations in English fields!")
    sys.exit(1)

print("SUCCESS: 0 Devanagari violations found in all 245 Saloks!")

# Write out scripts/kabir/kabir_salok_data.py
out_file = "scripts/kabir/kabir_salok_data.py"
with open(out_file, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\n')
    f.write('Unified Translations and Scholarly Commentary Data for Bhagat Kabir Ji SGGS Saloks.\n')
    f.write('Complete 245/245 Saloks with authentic Hindi verse, lyrical English verse (STRICT 0 Devanagari), and commentary.\n')
    f.write('"""\n\n')
    f.write("KABIR_SALOK_DATA = {\n")
    for num in range(1, 246):
        s = all_saloks[num]
        f.write(f"    {num}: {{\n")
        f.write(f'        "theme_hi": {repr(s["theme_hi"])},\n')
        f.write(f'        "theme_en": {repr(s["theme_en"])},\n')
        f.write(f'        "title_hi": {repr(s["title_hi"])},\n')
        f.write(f'        "title_en": {repr(s["title_en"])},\n')
        f.write(f'        "v_hi": {repr(s["v_hi"])},\n')
        f.write(f'        "v_en": {repr(s["v_en"])},\n')
        f.write(f'        "comm": {repr(s["comm"])}\n')
        f.write("    },\n")
    f.write("}\n")

print(f"Successfully generated {out_file} ({os.path.getsize(out_file)} bytes) with 245/245 Saloks!")
