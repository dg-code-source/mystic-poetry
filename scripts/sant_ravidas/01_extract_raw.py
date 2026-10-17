# -*- coding: utf-8 -*-
"""
Extracts raw text for all 3 collections of Sant Ravidas Ji from hindi-kavita.com:
1. Shabad (40 compositions from Sri Guru Granth Sahib Ji)
2. Padaavali (117 Padas)
3. Dohe / Sakhis (51 Dohe)
"""

import os
import sys
import json
import re
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_DIR = os.path.join(BASE_DIR, "data", "sant_ravidas", "raw")
os.makedirs(RAW_DIR, exist_ok=True)

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch_html(url):
    print(f"Fetching {url}...")
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode('utf-8', errors='ignore')

def clean_html(text):
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<p[^>]*>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'</p>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<[^>]+>', '', text)
    # Replace non-breaking space and HTML entities
    text = text.replace('&nbsp;', ' ').replace('&zwnj;', '').replace('&zwj;', '')
    lines = [l.strip() for l in text.split('\n')]
    return [l for l in lines if l]

# ====================================================================
# 1. EXTRACT SHABAD (Guru Granth Sahib Ji - 40 Shabad)
# ====================================================================
def extract_shabad():
    url = "https://hindi-kavita.com/HindiShabadBhagatRavidas.php"
    html = fetch_html(url)
    
    # Save raw HTML backup
    with open(os.path.join(RAW_DIR, "shabad.html"), "w", encoding="utf-8") as f:
        f.write(html)
        
    # The shabads are divided by anchors or headings like <a name="Ravidas1"> or id="Ravidas1"
    # Find all anchor markers
    markers = list(re.finditer(r'<a\s+[^>]*(?:name|id)=["\'](Ravidas\d+)["\'][^>]*>', html, re.IGNORECASE))
    print(f"Found {len(markers)} Shabad markers in HTML")
    
    shabads = []
    for i in range(len(markers)):
        m = markers[i]
        anchor_id = m.group(1)
        start_idx = m.end()
        end_idx = markers[i+1].start() if i + 1 < len(markers) else len(html)
        block = html[start_idx:end_idx]
        
        # Stop at footer or comments if last
        if i + 1 == len(markers):
            footer_m = re.search(r'<(?:div class="footer"|footer|div id="comments")', block, re.IGNORECASE)
            if footer_m:
                block = block[:footer_m.start()]
                
        # Extract title (usually in <h3>, <h2> or <b>/<strong>)
        title_m = re.search(r'<h[234][^>]*>(.*?)</h[234]>', block, re.DOTALL)
        title = ""
        if title_m:
            title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip()
            
        clean_lines = clean_html(block)
        # Filter out navigation / junk
        filtered = []
        for l in clean_lines:
            if l.startswith("मुख्य पृष्ठ") or l.startswith("कविता संकलन") or l.startswith("Home") or "Google" in l:
                continue
            if l == title:
                continue
            filtered.append(l)
            
        if not title and filtered:
            title = filtered[0]
            filtered = filtered[1:]
            
        shabads.append({
            "id": i + 1,
            "anchor": anchor_id,
            "title": title,
            "lines": filtered
        })
        
    output_path = os.path.join(RAW_DIR, "shabad.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(shabads, f, ensure_ascii=False, indent=2)
    print(f"Extracted {len(shabads)} Shabad saved to {output_path}")
    return shabads

# ====================================================================
# 2. EXTRACT PADAAVALI (117 Padas)
# ====================================================================
def extract_padaavali():
    url = "https://hindi-kavita.com/HindiPoetryBhagatRavidas.php"
    html = fetch_html(url)
    
    with open(os.path.join(RAW_DIR, "padaavali.html"), "w", encoding="utf-8") as f:
        f.write(html)
        
    # Match Pad anchors: <a name="Pad1"> or <a name="Pad1">1. ...</h3>
    markers = list(re.finditer(r'<a\s+[^>]*(?:name|id)=["\']Pad(\d+)["\'][^>]*>(.*?)</h3>', html, re.DOTALL | re.IGNORECASE))
    if not markers:
        markers = list(re.finditer(r'<a\s+[^>]*(?:name|id)=["\']Pad(\d+)["\'][^>]*>', html, re.IGNORECASE))
    print(f"Found {len(markers)} Padaavali poem markers")
    
    padas = []
    for i in range(len(markers)):
        m = markers[i]
        pada_num = int(m.group(1))
        # If title is captured in group 2
        title = ""
        if len(m.groups()) >= 2 and m.group(2):
            raw_title = re.sub(r'<[^>]+>', '', m.group(2)).strip()
            title = re.sub(r'^\d+\.\s*', '', raw_title).strip()
            
        start_idx = m.end()
        end_idx = markers[i+1].start() if i + 1 < len(markers) else len(html)
        block = html[start_idx:end_idx]
        
        if i + 1 == len(markers):
            footer_m = re.search(r'<(?:div class="footer"|footer|div id="comments")', block, re.IGNORECASE)
            if footer_m:
                block = block[:footer_m.start()]
                
        clean_lines = clean_html(block)
        filtered = []
        for l in clean_lines:
            if l.startswith("मुख्य पृष्ठ") or l.startswith("कविता संकलन") or l.startswith("Home") or "Google" in l:
                continue
            filtered.append(l)
            
        padas.append({
            "id": pada_num,
            "title": title,
            "lines": filtered
        })
        
    output_path = os.path.join(RAW_DIR, "padaavali.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(padas, f, ensure_ascii=False, indent=2)
    print(f"Extracted {len(padas)} Padas saved to {output_path}")
    return padas

# ====================================================================
# 3. EXTRACT DOHE (51 Dohe)
# ====================================================================
def extract_dohe():
    url = "https://hindi-kavita.com/HindiDoheBhagatRavidas.php"
    html = fetch_html(url)
    
    with open(os.path.join(RAW_DIR, "dohe.html"), "w", encoding="utf-8") as f:
        f.write(html)
        
    # In Dohe, headings are typically <h3>1</h3>, <h3>2</h3>, etc.
    headings = list(re.finditer(r'<h[234][^>]*>\s*(\d+)\s*</h[234]>', html))
    print(f"Found {len(headings)} Dohe headings")
    
    dohe = []
    for i in range(len(headings)):
        h = headings[i]
        doha_num = int(h.group(1))
        start_idx = h.end()
        end_idx = headings[i+1].start() if i + 1 < len(headings) else len(html)
        block = html[start_idx:end_idx]
        
        if i + 1 == len(headings):
            footer_m = re.search(r'<(?:div class="footer"|footer|div id="comments")', block, re.IGNORECASE)
            if footer_m:
                block = block[:footer_m.start()]
                
        clean_lines = clean_html(block)
        filtered = []
        for l in clean_lines:
            if l.startswith("मुख्य पृष्ठ") or l.startswith("कविता संकलन") or l.startswith("Home") or "Google" in l:
                continue
            filtered.append(l)
            
        dohe.append({
            "id": doha_num,
            "title": f"दोहा {doha_num}",
            "lines": filtered
        })
        
    output_path = os.path.join(RAW_DIR, "dohe.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(dohe, f, ensure_ascii=False, indent=2)
    print(f"Extracted {len(dohe)} Dohe saved to {output_path}")
    return dohe

if __name__ == "__main__":
    print("=" * 60)
    print("EXTRACTING SANT RAVIDAS COMPLETE WORKS")
    print("=" * 60)
    shabads = extract_shabad()
    padas = extract_padaavali()
    dohe = extract_dohe()
    print("=" * 60)
    print(f"SUMMARY: Shabad: {len(shabads)}, Padaavali: {len(padas)}, Dohe: {len(dohe)}")
    print(f"TOTAL COMPOSITIONS EXTRACTED: {len(shabads) + len(padas) + len(dohe)}")
    print("=" * 60)
