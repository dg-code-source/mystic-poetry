# -*- coding: utf-8 -*-
"""
01_extract_farid_raw.py
Extract all 130 Saloks and 4 Shabads of Hazrat Baba Sheikh Farid Ji
from https://hindi-kavita.com/HindiSalokBabaSheikhFarid.php
and  https://hindi-kavita.com/HindiShabadBabaSheikhFarid.php.

Saves clean structured JSON to:
- data/sheikh_farid/raw/salok.json
- data/sheikh_farid/raw/shabad.json
"""

import os
import sys
import re
import json
import urllib.request
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_DIR = os.path.join(BASE_DIR, "data", "sheikh_farid", "raw")
os.makedirs(RAW_DIR, exist_ok=True)

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch_html(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode('utf-8', errors='ignore')

def extract_saloks():
    url = "https://hindi-kavita.com/HindiSalokBabaSheikhFarid.php"
    print(f"Fetching Saloks from {url}...")
    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    content_div = soup.find('div', class_='content')

    # All text inside content_div
    raw_lines = [s.strip() for s in content_div.stripped_strings if s.strip()]
    
    # Exclude nav headers/footers
    cleaned_lines = []
    ignoring = True
    for line in raw_lines:
        if "सलोक सेख फरीद के" in line:
            ignoring = False
        if "नोट=" in line or "मुख्य पृष्ठ :" in line:
            break
        if not ignoring:
            cleaned_lines.append(line)

    saloks = []
    curr_id = None
    curr_lines = []
    author_note = ""

    # Parse Salok blocks
    for line in cleaned_lines:
        # Check if line is a number 1..130 or heading like 'सलोक सेख फरीद केੴ सतिगुर प्रसादि1'
        m_start = re.match(r'^(?:सलोक सेख फरीद के\s*ੴ सतिगुर प्रसादि)?\s*(\d+)$', line)
        if m_start:
            num = int(m_start.group(1))
            if curr_id is not None and curr_lines:
                saloks.append({
                    "id": curr_id,
                    "title": f"सलोक {curr_id}: {curr_lines[0]}",
                    "guru_attribution": author_note,
                    "lines": curr_lines
                })
                curr_lines = []
                author_note = ""
            curr_id = num
            continue

        if re.match(r'^\(?म[ः:]\s*\d+\)?$', line):
            author_note = line
            continue

        # Add line to current salok
        curr_lines.append(line)

    # Save last salok
    if curr_id is not None and curr_lines:
        saloks.append({
            "id": curr_id,
            "title": f"सलोक {curr_id}: {curr_lines[0]}",
            "guru_attribution": author_note,
            "lines": curr_lines
        })

    print(f"Extracted {len(saloks)} Saloks of Baba Sheikh Farid Ji.")
    out_file = os.path.join(RAW_DIR, "salok.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(saloks, f, ensure_ascii=False, indent=2)
    print(f"Saved: {out_file} ({os.path.getsize(out_file)} bytes)")
    return saloks

def extract_shabads():
    url = "https://hindi-kavita.com/HindiShabadBabaSheikhFarid.php"
    print(f"Fetching Shabads from {url}...")
    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    content_div = soup.find('div', class_='content')

    raw_lines = [s.strip() for s in content_div.stripped_strings if s.strip()]

    # Extract 4 Shabads
    shabads = []
    shabad_defs = [
        {"id": 1, "raga": "राग आसा (Raag Aasa)", "ang": 488, "title_prefix": "1. आसा सेख फरीद जीउ की बाणी"},
        {"id": 2, "raga": "राग आसा (Raag Aasa)", "ang": 488, "title_prefix": "2. आसा"},
        {"id": 3, "raga": "राग सूही (Raag Suhi)", "ang": 794, "title_prefix": "3. ੴ सतिगुर प्रसादि"},
        {"id": 4, "raga": "राग सूही ललित (Raag Suhi Lalit)", "ang": 794, "title_prefix": "4. सूही ललित"}
    ]

    curr_shabad = None
    curr_lines = []

    for line in raw_lines:
        if "मुख्य पृष्ठ :" in line:
            break

        # Check for shabad headers
        matched_id = None
        for sdef in shabad_defs:
            if line.startswith(f"{sdef['id']}."):
                matched_id = sdef['id']
                break

        if matched_id:
            if curr_shabad is not None and curr_lines:
                curr_shabad["lines"] = curr_lines
                shabads.append(curr_shabad)
                curr_lines = []

            sdef = next(s for s in shabad_defs if s['id'] == matched_id)
            curr_shabad = {
                "id": matched_id,
                "raga": sdef["raga"],
                "ang": sdef["ang"],
                "header": line,
                "title": f"शब्द {matched_id} ({sdef['raga']})",
                "lines": []
            }
            continue

        if curr_shabad:
            # skip boilerplate
            if line in ["शब्द : बाबा शेख फ़रीद", "Shabd in Hindi : Baba Sheikh Farid", "Home", "Hindi Poetry"]:
                continue
            curr_lines.append(line)

    if curr_shabad is not None and curr_lines:
        curr_shabad["lines"] = curr_lines
        shabads.append(curr_shabad)

    print(f"Extracted {len(shabads)} Shabads of Baba Sheikh Farid Ji.")
    out_file = os.path.join(RAW_DIR, "shabad.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(shabads, f, ensure_ascii=False, indent=2)
    print(f"Saved: {out_file} ({os.path.getsize(out_file)} bytes)")
    return shabads

if __name__ == "__main__":
    saloks = extract_saloks()
    shabads = extract_shabads()
    print(f"\nPhase 1 (Baba Sheikh Farid) Complete: {len(saloks)} Saloks + {len(shabads)} Shabads = {len(saloks) + len(shabads)} Compositions!")
