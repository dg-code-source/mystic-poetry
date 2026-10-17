# -*- coding: utf-8 -*-
"""
Parses raw HTML of the 5 works and generates clean extracted JSON files
and base Devanagari Markdown files without external links.
"""

import os
import re
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, "data", "raw_other_works")
EXTRACTED_DIR = os.path.join(BASE_DIR, "data", "raw_extracted")
os.makedirs(EXTRACTED_DIR, exist_ok=True)

def clean_text_chunk(content):
    cutoff = re.search(r'<(div|footer|form|nav|script|style)', content, re.I)
    if cutoff:
        content = content[:cutoff.start()]
    content = re.sub(r'<br\s*/?>', '\n', content, flags=re.I)
    content = re.sub(r'</p>\s*<p[^>]*>', '\n\n', content, flags=re.I)
    content = re.sub(r'<[^>]+>', '', content)
    lines = [l.strip() for l in content.split('\n') if l.strip()]
    return lines

# 1. Baranmah
with open(os.path.join(RAW_DIR, "baranmah.html"), "r", encoding="utf-8") as f:
    b_html = f.read()

b_parts = re.split(r'<h3[^>]*>', b_html, flags=re.I)
baranmah_data = []
for idx, p in enumerate(b_parts[1:], 1):
    h3, content = p.split('</h3>', 1)
    m_name = re.sub(r'<[^>]+>', '', h3).strip()
    lines = clean_text_chunk(content)
    baranmah_data.append({
        "id": idx,
        "title": f"{idx}. {m_name}",
        "month": m_name,
        "lines": lines
    })

with open(os.path.join(EXTRACTED_DIR, "baranmah.json"), "w", encoding="utf-8") as f:
    json.dump(baranmah_data, f, ensure_ascii=False, indent=2)

# 2. Athwara
with open(os.path.join(RAW_DIR, "athwara.html"), "r", encoding="utf-8") as f:
    a_html = f.read()

a_parts = re.split(r'<h3[^>]*>', a_html, flags=re.I)
athwara_data = []
for idx, p in enumerate(a_parts[1:], 1):
    h3, content = p.split('</h3>', 1)
    d_name = re.sub(r'<[^>]+>', '', h3).strip()
    lines = clean_text_chunk(content)
    athwara_data.append({
        "id": idx,
        "title": f"{idx}. {d_name}",
        "day": d_name,
        "lines": lines
    })

with open(os.path.join(EXTRACTED_DIR, "athwara.json"), "w", encoding="utf-8") as f:
    json.dump(athwara_data, f, ensure_ascii=False, indent=2)

# 3. Gandhan
with open(os.path.join(RAW_DIR, "gandhan.html"), "r", encoding="utf-8") as f:
    g_html = f.read()

h2_idx = g_html.find('</h2>')
g_content = g_html[h2_idx+5:] if h2_idx != -1 else g_html
cutoff = re.search(r'<(div class=[\"\']footer|footer|form)', g_content, re.I)
if cutoff: g_content = g_content[:cutoff.start()]
g_content = re.sub(r'<br\s*/?>', '\n', g_content, flags=re.I)
g_content = re.sub(r'<[^>]+>', '', g_content)
raw_g_lines = [l.strip() for l in g_content.split('\n') if l.strip()]

# Parse into Gandhan stanzas / knots (1 to 40)
# Lines often have numbers like ।१।, ।२।, ।३। etc.
gandhan_stanzas = []
current_lines = []
current_num = 1
for l in raw_g_lines:
    current_lines.append(l)
    m = re.search(r'[।॥](\d+|[०-९]+)[।॥]', l)
    if m:
        num_val = m.group(1)
        gandhan_stanzas.append({
            "knot_id": current_num,
            "title": f"गंढ {current_num}",
            "lines": current_lines
        })
        current_lines = []
        current_num += 1

if current_lines:
    gandhan_stanzas.append({
        "knot_id": current_num,
        "title": f"गंढ {current_num} (समापन)",
        "lines": current_lines
    })

with open(os.path.join(EXTRACTED_DIR, "gandhan.json"), "w", encoding="utf-8") as f:
    json.dump(gandhan_stanzas, f, ensure_ascii=False, indent=2)

# 4. Dohre
with open(os.path.join(RAW_DIR, "dohre.html"), "r", encoding="utf-8") as f:
    d_html = f.read()

h2_idx = d_html.find('</h2>')
d_content = d_html[h2_idx+5:] if h2_idx != -1 else d_html
cutoff = re.search(r'<(div class=[\"\']footer|footer|form)', d_content, re.I)
if cutoff: d_content = d_content[:cutoff.start()]
d_content = re.sub(r'<br\s*/?>', '\n', d_content, flags=re.I)
d_content = re.sub(r'<[^>]+>', '', d_content)

# Split by digits / Gurmukhi digits
dohre_parts = re.split(r'\n\s*([०-९\d]+)\s*\n', '\n' + d_content)
dohre_data = []
if len(dohre_parts) > 1:
    for i in range(1, len(dohre_parts), 2):
        num_str = dohre_parts[i].strip()
        body = dohre_parts[i+1].strip() if i+1 < len(dohre_parts) else ""
        lines = [l.strip() for l in body.split('\n') if l.strip()]
        if lines:
            # normalize num_str
            # convert devanagari/gurmukhi digits if needed
            dohre_data.append({
                "id": len(dohre_data) + 1,
                "label": num_str,
                "title": f"दोहरा {len(dohre_data) + 1}",
                "lines": lines
            })

with open(os.path.join(EXTRACTED_DIR, "dohre.json"), "w", encoding="utf-8") as f:
    json.dump(dohre_data, f, ensure_ascii=False, indent=2)

# 5. Siharfian
with open(os.path.join(RAW_DIR, "siharfian.html"), "r", encoding="utf-8") as f:
    s_html = f.read()

s_parts = re.split(r'<h3[^>]*>', s_html, flags=re.I)
siharfian_cycles = []
current_cycle_name = "पहली सीहरफ़ी"
current_cycle_items = []
refrain = ""

for p in s_parts[1:]:
    h3, content = p.split('</h3>', 1)
    title = re.sub(r'<[^>]+>', '', h3).strip()
    
    if "सीहरफ़ी" in title or "सीहरफी" in title:
        if current_cycle_items:
            siharfian_cycles.append({
                "cycle": current_cycle_name,
                "refrain": refrain,
                "stanzas": current_cycle_items
            })
            current_cycle_items = []
        current_cycle_name = title
        # check if there's immediate refrain text
        lines = clean_text_chunk(content)
        if lines:
            refrain = " / ".join(lines)
    else:
        letter = title.replace('-', '').strip()
        lines = clean_text_chunk(content)
        if lines:
            current_cycle_items.append({
                "letter": letter,
                "title": f"{letter} ({current_cycle_name})",
                "lines": lines
            })

if current_cycle_items:
    siharfian_cycles.append({
        "cycle": current_cycle_name,
        "refrain": refrain,
        "stanzas": current_cycle_items
    })

with open(os.path.join(EXTRACTED_DIR, "siharfian.json"), "w", encoding="utf-8") as f:
    json.dump(siharfian_cycles, f, ensure_ascii=False, indent=2)

print("Extraction Summary:")
print(f"  Baranmah: {len(baranmah_data)} months")
print(f"  Athwara: {len(athwara_data)} days")
print(f"  Gandhan: {len(gandhan_stanzas)} knots")
print(f"  Dohre: {len(dohre_data)} couplets")
print(f"  Siharfian: {len(siharfian_cycles)} cycles with {[len(c['stanzas']) for c in siharfian_cycles]} stanzas")
