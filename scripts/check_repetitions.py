# -*- coding: utf-8 -*-
"""
Deep cross-comparison to find duplicate or repeating verses:
1. Between the 5 works and the 160 Kafian
2. Across the 5 works themselves
3. Internally within each work
"""

import os
import re
import glob
import json
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw_other_works")
KAFIAN_DIR = os.path.join(DATA_DIR, "kafian")

def clean_line(l):
    l = re.sub(r'<[^>]+>', '', l)
    l = re.sub(r'[।॥,\.\?\!\:\-\(\)\"\'\d०-९]', '', l)
    l = re.sub(r'\s+', ' ', l).strip()
    return l

# Load Kafian lines
kafi_lines = defaultdict(list)
for f in sorted(glob.glob(os.path.join(KAFIAN_DIR, "kafi_*.json"))):
    with open(f, "r", encoding="utf-8") as fp:
        k = json.load(fp)
    k_id = k["id"]
    k_title = k.get("title", f"Kafi {k_id}")
    
    lines = []
    if "original_poem" in k and k["original_poem"]:
        lines = [l for l in k["original_poem"].split("\n") if l.strip()]
    elif "stanzas" in k:
        for s in k["stanzas"]:
            for l in s.get("original", []):
                if l.strip(): lines.append(l)
    elif "annotated_stanzas" in k:
        for s in k["annotated_stanzas"]:
            for l in s.get("lines", []):
                orig = l.get("original", "").strip()
                if orig: lines.append(orig)
                
    for l in lines:
        cl = clean_line(l)
        if len(cl) > 8:
            kafi_lines[cl].append((k_id, k_title))

print(f"Loaded {len(kafi_lines)} unique indexed lines from 160 Kafian.")

# Load lines from each of the 5 files
works_lines = {}
for name in ['baranmah', 'athwara', 'gandhan', 'siharfian', 'dohre']:
    path = os.path.join(RAW_DIR, f"{name}.html")
    with open(path, "r", encoding="utf-8") as fp:
        html = fp.read()
    
    # Extract text
    h2_idx = html.find('</h2>')
    content = html[h2_idx+5:] if h2_idx != -1 else html
    cutoff = re.search(r'<(div class=[\"\']footer|footer|form|nav)', content, re.I)
    if cutoff: content = content[:cutoff.start()]
    content = re.sub(r'<br\s*/?>', '\n', content)
    text = re.sub(r'<[^>]+>', '', content)
    
    lines = [clean_line(l) for l in text.split('\n') if len(clean_line(l)) > 8]
    works_lines[name] = lines
    print(f"Loaded {len(lines)} lines from {name}")

# Check 1: Cross-check against 160 Kafian
print("\n=== REPETITIONS: 5 Works vs 160 Kafian ===")
matches_with_kafian = []
for name, lines in works_lines.items():
    for l in lines:
        if l in kafi_lines:
            matches_with_kafian.append((name, l, kafi_lines[l]))

if matches_with_kafian:
    print(f"Found {len(matches_with_kafian)} lines overlapping with 160 Kafian:")
    seen = set()
    for name, l, k_matches in matches_with_kafian:
        key = (name, l)
        if key not in seen:
            seen.add(key)
            k_info = ", ".join([f"Kafi #{m[0]} ({m[1]})" for m in k_matches[:2]])
            print(f"  [{name.upper()}] \"{l}\" == {k_info}")
else:
    print("Zero overlaps found with 160 Kafian.")

# Check 2: Overlaps BETWEEN the 5 works
print("\n=== REPETITIONS: Between the 5 Works ===")
names = list(works_lines.keys())
cross_matches = []
for i in range(len(names)):
    for j in range(i+1, len(names)):
        n1, n2 = names[i], names[j]
        set1 = set(works_lines[n1])
        set2 = set(works_lines[n2])
        common = set1.intersection(set2)
        if common:
            print(f"Overlap between {n1} and {n2}: {len(common)} lines:")
            for cl in list(common)[:5]:
                print(f"  \"{cl}\"")

# Check 3: Internal repetitions within each work
print("\n=== REPETITIONS: Internal within each work ===")
for name, lines in works_lines.items():
    counts = defaultdict(int)
    for l in lines:
        counts[l] += 1
    repeats = {l: c for l, c in counts.items() if c > 1}
    print(f"{name.upper()}: {len(repeats)} lines repeat internally.")
    if repeats:
        for l, c in sorted(repeats.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  Repeated {c}x: \"{l}\"")
