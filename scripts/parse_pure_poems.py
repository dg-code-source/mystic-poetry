# -*- coding: utf-8 -*-
"""
Parse and extract pure poetic text for each of the 5 works.
"""

import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw_other_works")

def clean_html(html_str):
    # strip scripts, styles, forms, footers
    html_str = re.sub(r'<(script|style|form|nav|footer)[^>]*>.*?</\1>', '', html_str, flags=re.DOTALL | re.I)
    cutoff = re.search(r'<(div class=[\"\']footer|div id=[\"\']footer|div class=[\"\']comments)', html_str, re.I)
    if cutoff:
        html_str = html_str[:cutoff.start()]
    html_str = re.sub(r'<br\s*/?>', '\n', html_str, flags=re.I)
    html_str = re.sub(r'</p>\s*<p[^>]*>', '\n\n', html_str, flags=re.I)
    html_str = re.sub(r'<[^>]+>', '', html_str)
    lines = [l.strip() for l in html_str.split('\n')]
    return '\n'.join(lines)

# 1. Baranmah
with open(os.path.join(RAW_DIR, "baranmah.html"), "r", encoding="utf-8") as f:
    b_html = f.read()

# 2. Athwara
with open(os.path.join(RAW_DIR, "athwara.html"), "r", encoding="utf-8") as f:
    a_html = f.read()

# 3. Gandhan
with open(os.path.join(RAW_DIR, "gandhan.html"), "r", encoding="utf-8") as f:
    g_html = f.read()

# 4. Siharfian
with open(os.path.join(RAW_DIR, "siharfian.html"), "r", encoding="utf-8") as f:
    s_html = f.read()

# 5. Dohre
with open(os.path.join(RAW_DIR, "dohre.html"), "r", encoding="utf-8") as f:
    d_html = f.read()

print("File lengths:")
print(f"  Baranmah HTML: {len(b_html)}")
print(f"  Athwara HTML:  {len(a_html)}")
print(f"  Gandhan HTML:  {len(g_html)}")
print(f"  Siharfian HTML:{len(s_html)}")
print(f"  Dohre HTML:    {len(d_html)}")
