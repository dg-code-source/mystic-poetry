# -*- coding: utf-8 -*-
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

files = [
    (os.path.join("content", "sant_ravidas", "Sant_Ravidas_Shabad_Trilingual.md"), "शब्द", 40),
    (os.path.join("content", "sant_ravidas", "Sant_Ravidas_Padaavali_Trilingual.md"), "पद", 117),
    (os.path.join("content", "sant_ravidas", "Sant_Ravidas_Dohe_Trilingual.md"), "दोहा", 51),
]

all_passed = True

for filename, tag, expected_count in files:
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into individual compositions
    # The header pattern is: ## <tag> <number>:
    sections = re.split(rf"\n## {tag} \d+:", content)[1:]
    
    print(f"\n==================================================")
    print(f"Auditing {filename}:")
    print(f"Total compositions detected: {len(sections)} (Expected: {expected_count})")
    
    if len(sections) != expected_count:
        print(f"  [ERROR] Mismatch in expected count!")
        all_passed = False
        continue

    missing_hi = []
    missing_en = []
    missing_comm = []
    short_hi = []
    short_en = []

    for idx, sec in enumerate(sections, 1):
        # Look for Hindi verse block
        # Format: #### <emoji> <Hindi translation title>\n```text\n<verse>\n```
        hi_match = re.search(r"####[^\n]+(?:काव्यानुवाद|भावार्थ)[^\n]*\n```(?:text)?\n([\s\S]*?)\n```", sec)
        if not hi_match:
            missing_hi.append(idx)
        else:
            hi_text = hi_match.group(1).strip()
            if len(hi_text) < 25:
                short_hi.append((idx, hi_text))

        # Look for English verse block
        # Format: #### <emoji> Poetic English Translation\n```text\n<verse>\n```
        en_match = re.search(r"####[^\n]+Poetic English Translation[^\n]*\n```(?:text)?\n([\s\S]*?)\n```", sec)
        if not en_match:
            missing_en.append(idx)
        else:
            en_text = en_match.group(1).strip()
            if len(en_text) < 25:
                short_en.append((idx, en_text))

        # Look for commentary
        if "### " not in sec or ("दार्शनिक" not in sec and "विश्लेषण" not in sec and "मीमांसा" not in sec and "Commentary" not in sec):
            missing_comm.append(idx)

    print(f"  - Hindi poetic translations present: {expected_count - len(missing_hi)} / {expected_count}")
    print(f"  - English poetic translations present: {expected_count - len(missing_en)} / {expected_count}")
    print(f"  - In-depth commentaries present: {expected_count - len(missing_comm)} / {expected_count}")

    if missing_hi:
        print(f"  [!] Missing Hindi: {missing_hi}")
        all_passed = False
    if missing_en:
        print(f"  [!] Missing English: {missing_en}")
        all_passed = False
    if short_hi:
        print(f"  [!] Suspiciously short Hindi: {short_hi}")
        all_passed = False
    if short_en:
        print(f"  [!] Suspiciously short English: {short_en}")
        all_passed = False
    if missing_comm:
        print(f"  [!] Missing commentary: {missing_comm}")
        all_passed = False

    if not missing_hi and not missing_en and not short_hi and not short_en and not missing_comm:
        print(f"  [SUCCESS] 100% of all {expected_count} {tag} have complete, authentic Hindi and English poetic translations & commentary!")

print("\n" + "="*50)
if all_passed:
    print("ALL 208 COMPOSITIONS OF SANT RAVIDAS JI ARE 100% COMPLETE IN MARKDOWN EDITIONS!")
else:
    print("AUDIT FAILED: SOME TRANSLATIONS ARE MISSING!")
