# -*- coding: utf-8 -*-
"""
Detailed inspection and duplicate detection across the 5 additional works:
- Baranmah
- Athwara
- Gandhan
- Siharfian
- Dohre
And cross-checking against the 160 Kafian.
"""

import os
import re
import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw_other_works")
KAFIAN_DIR = os.path.join(DATA_DIR, "kafian")

# 1. Load all verses from 160 Kafian for duplicate checking
all_kafi_verses = {}
for f in sorted(glob.glob(os.path.join(KAFIAN_DIR, "kafi_*.json"))):
    with open(f, "r", encoding="utf-8") as fp:
        k = json.load(fp)
    k_id = k["id"]
    k_title = k.get("title", f"Kafi {k_id}")
    
    # gather lines
    lines = []
    if "original_poem" in k and k["original_poem"]:
        lines = [l.strip() for l in k["original_poem"].split("\n") if l.strip()]
    elif "stanzas" in k:
        for s in k["stanzas"]:
            for l in s.get("original", []):
                if l.strip(): lines.append(l.strip())
    elif "annotated_stanzas" in k:
        for s in k["annotated_stanzas"]:
            for l in s.get("lines", []):
                orig = l.get("original", "").strip()
                if orig: lines.append(orig)
                
    for l in lines:
        clean_l = re.sub(r'[।॥,\.\?\!]', '', l).strip()
        if len(clean_l) > 10:
            all_kafi_verses[clean_l] = (k_id, k_title)

print(f"Loaded {len(all_kafi_verses)} unique verse lines from 160 Kafian.")

# 2. Inspect Baranmah
with open(os.path.join(RAW_DIR, "baranmah.html"), "r", encoding="utf-8") as fp:
    b_html = fp.read()
b_parts = re.split(r'<h3[^>]*>', b_html, flags=re.I)
print(f"\n--- BARANMAH ---")
print(f"Sections found: {len(b_parts)-1}")
for p in b_parts[1:]:
    h3_title, content = p.split('</h3>', 1)
    title = re.sub(r'<[^>]+>', '', h3_title).strip()
    cutoff = re.search(r'<(div|footer|form|nav)', content, re.I)
    if cutoff: content = content[:cutoff.start()]
    text = re.sub(r'<[^>]+>', '', content).strip()
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    print(f"  Month: {title} ({len(lines)} lines) -> Sample: {lines[0] if lines else 'empty'}")

# 3. Inspect Athwara
with open(os.path.join(RAW_DIR, "athwara.html"), "r", encoding="utf-8") as fp:
    a_html = fp.read()
a_parts = re.split(r'<h3[^>]*>', a_html, flags=re.I)
print(f"\n--- ATHWARA ---")
print(f"Sections found: {len(a_parts)-1}")
for p in a_parts[1:]:
    h3_title, content = p.split('</h3>', 1)
    title = re.sub(r'<[^>]+>', '', h3_title).strip()
    cutoff = re.search(r'<(div|footer|form|nav)', content, re.I)
    if cutoff: content = content[:cutoff.start()]
    text = re.sub(r'<[^>]+>', '', content).strip()
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    print(f"  Day: {title} ({len(lines)} lines) -> Sample: {lines[0] if lines else 'empty'}")

# 4. Inspect Gandhan
with open(os.path.join(RAW_DIR, "gandhan.html"), "r", encoding="utf-8") as fp:
    g_html = fp.read()
# Let's find how Gandhan is divided
print(f"\n--- GANDHAN ---")
h2_idx = g_html.find('</h2>')
g_content = g_html[h2_idx+5:] if h2_idx != -1 else g_html
cutoff = re.search(r'<(div class=[\"\']footer|footer|form)', g_content, re.I)
if cutoff: g_content = g_content[:cutoff.start()]
g_text = re.sub(r'<br\s*/?>', '\n', g_content)
g_text = re.sub(r'<[^>]+>', '', g_text).strip()
g_stanzas = [s.strip() for s in re.split(r'\n\s*\n', g_text) if s.strip()]
print(f"Gandhan total stanzas: {len(g_stanzas)}")
for idx, s in enumerate(g_stanzas[:10]):
    first_line = s.split('\n')[0].strip()
    print(f"  Stanza {idx+1}: {first_line}")

# 5. Inspect Siharfian
with open(os.path.join(RAW_DIR, "siharfian.html"), "r", encoding="utf-8") as fp:
    s_html = fp.read()
s_parts = re.split(r'<h3[^>]*>', s_html, flags=re.I)
print(f"\n--- SIHARFIAN ---")
print(f"H3 sections in Siharfian: {len(s_parts)-1}")
siharfi_groups = []
current_group = "पहली सीहरफ़ी"
for p in s_parts[1:]:
    h3_title, content = p.split('</h3>', 1)
    title = re.sub(r'<[^>]+>', '', h3_title).strip()
    if "सीहरफ़ी" in title or "सीहरफी" in title:
        current_group = title
        print(f"  Found Major Division: {current_group}")
    else:
        cutoff = re.search(r'<(div|footer|form|nav)', content, re.I)
        if cutoff: content = content[:cutoff.start()]
        text = re.sub(r'<[^>]+>', '', content).strip()
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        # print first few
        siharfi_groups.append((current_group, title, len(lines)))

print(f"Total letter stanzas across Siharfian: {len(siharfi_groups)}")

# 6. Inspect Dohre
with open(os.path.join(RAW_DIR, "dohre.html"), "r", encoding="utf-8") as fp:
    d_html = fp.read()
print(f"\n--- DOHRE ---")
h2_idx = d_html.find('</h2>')
d_content = d_html[h2_idx+5:] if h2_idx != -1 else d_html
cutoff = re.search(r'<(div class=[\"\']footer|footer|form)', d_content, re.I)
if cutoff: d_content = d_content[:cutoff.start()]
d_text = re.sub(r'<br\s*/?>', '\n', d_content)
d_text = re.sub(r'<[^>]+>', '', d_text).strip()

# Split by numbers
dohre_items = re.split(r'\n\s*([०-९\d]+)\s*\n', '\n' + d_text)
print(f"Dohre items split parts: {len(dohre_items)}")
dohre_list = []
if len(dohre_items) > 1:
    for i in range(1, len(dohre_items), 2):
        num_str = dohre_items[i].strip()
        body = dohre_items[i+1].strip() if i+1 < len(dohre_items) else ""
        dohre_list.append((num_str, body))
print(f"Parsed {len(dohre_list)} Dohre.")
for num_str, body in dohre_list[:8]:
    first_line = body.split('\n')[0].strip() if body else ''
    print(f"  Dohra #{num_str}: {first_line}")
