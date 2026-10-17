# -*- coding: utf-8 -*-
"""
Analysis of unmapped token roots in Sant Ravidas Ji's 4,273 vocabulary list.
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORDS_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "still_unresolved.json")
words = json.load(open(WORDS_PATH, encoding='utf-8'))

print(f"Total words to analyze: {len(words)}")

# Group by first letter
by_initial = {}
for w in words:
    init = w[0]
    by_initial.setdefault(init, []).append(w)

print("\nWord count by initial character:")
for init, wlist in sorted(by_initial.items(), key=lambda x: len(x[1]), reverse=True)[:20]:
    print(f"  {init}: {len(wlist)} words (e.g., {', '.join(wlist[:5])})")
