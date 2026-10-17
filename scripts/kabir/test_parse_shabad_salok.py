import os
import re
from bs4 import BeautifulSoup
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

html_dir = "data/kabir/raw/html"

def clean_text(text):
    text = re.sub(r'\r', '', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

# 1. Parse Shabads
def parse_shabads():
    path = os.path.join(html_dir, "HindiShabadBhagatKabir.html")
    with open(path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    headings = soup.find_all(['h2', 'h3'])
    shabads = []
    
    for h in headings:
        txt = h.get_text(strip=True)
        m = re.match(r'^(\d+)\.\s*(.*)', txt)
        if not m:
            continue
        num = int(m.group(1))
        title = m.group(2).strip()
        
        lines = []
        curr = h.next_sibling
        while curr and curr.name not in ['h2', 'h3']:
            if hasattr(curr, 'get_text'):
                t = curr.get_text(strip=True)
                if t:
                    # Split lines by newline
                    for l in t.split('\n'):
                        l_clean = clean_text(l)
                        if l_clean and not any(k in l_clean for k in ['मुख्य पृष्ठ', 'कविता वेबसाइट', 'Shabad Bhakt Kabir']):
                            lines.append(l_clean)
            curr = curr.next_sibling
            
        if lines:
            shabads.append({
                'id': f"kabir_shabad_{num:03d}",
                'num': num,
                'type': 'shabad',
                'title': f"Shabad {num}: {title}",
                'title_hi': f"शब्द {num}: {title}",
                'first_line': lines[0] if lines else title,
                'lines': lines
            })
    return shabads

shabads = parse_shabads()
print(f"Parsed {len(shabads)} Shabads")
if shabads:
    print(f"Sample Shabad 1:\n  Title: {shabads[0]['title_hi']}\n  Lines ({len(shabads[0]['lines'])}):\n  " + "\n  ".join(shabads[0]['lines'][:3]))
    print(f"\nSample Shabad 107 (Awal Allah Noor):\n  Title: {shabads[106]['title_hi']}\n  Lines ({len(shabads[106]['lines'])}):\n  " + "\n  ".join(shabads[106]['lines'][:3]))

# 2. Parse Saloks
def parse_saloks():
    path = os.path.join(html_dir, "HindiSalokBhagatKabir.html")
    with open(path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    text = soup.get_text()
    start_marker = "सलोक भगत कबीर जीउ के"
    idx = text.find(start_marker)
    if idx == -1:
        return []
        
    salok_part = text[idx:]
    pattern = r'॥\s*([०-९\d]+)\s*॥'
    splits = re.split(pattern, salok_part)
    
    saloks = []
    salok_idx = 1
    
    # Devanagari numeral map
    dev_num_map = {'०':'0','१':'1','२':'2','३':'3','४':'4','५':'5','६':'6','७':'7','८':'8','९':'9'}
    
    for i in range(1, len(splits), 2):
        marker_raw = splits[i]
        marker_str = "".join(dev_num_map.get(c, c) for c in marker_raw)
        body = splits[i-1].strip()
        
        # Remove header intro if in body 0
        if "सलोक भगत कबीर जीउ के" in body:
            body = re.sub(r'सलोक भगत कबीर जीउ केੴ सतिगुर प्रसादि ॥', '', body).strip()
            
        raw_lines = [clean_text(l) for l in body.split('\n') if clean_text(l)]
        # Filter out nav
        filtered = [l for l in raw_lines if not any(k in l for k in ['मुख्य पृष्ठ', 'कविता वेबसाइट', 'Salok Bhagat'])]
        
        if filtered:
            first_line = filtered[0]
            saloks.append({
                'id': f"kabir_salok_{salok_idx:03d}",
                'num': salok_idx,
                'marker': marker_str,
                'type': 'salok',
                'title': f"Salok {salok_idx}: {first_line[:40]}...",
                'title_hi': f"सलोक {salok_idx}: {first_line[:40]}...",
                'first_line': first_line,
                'lines': filtered
            })
            salok_idx += 1
            
    return saloks

saloks = parse_saloks()
print(f"\nParsed {len(saloks)} Saloks")
if saloks:
    print(f"Sample Salok 1:\n  Title: {saloks[0]['title_hi']}\n  Lines: {saloks[0]['lines']}")
    print(f"Sample Salok 245:\n  Title: {saloks[-1]['title_hi']}\n  Lines: {saloks[-1]['lines']}")
