import os
import glob
import re
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_dir = "data/kabir/raw/html"

print("==================== CENSUS OF KABIR CORPUS ====================")

# 1. Shabads (from Sri Guru Granth Sahib Ji)
shabad_path = os.path.join(html_dir, "HindiShabadBhagatKabir.html")
shabads = []
if os.path.exists(shabad_path):
    with open(shabad_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    headings = soup.find_all(['h2', 'h3'])
    for h in headings:
        t = h.get_text(strip=True)
        m = re.match(r'^(\d+)\.\s*(.*)', t)
        if m:
            # get following lines
            curr = h.next_sibling
            lines = []
            while curr and curr.name not in ['h2', 'h3']:
                if hasattr(curr, 'get_text'):
                    txt = curr.get_text(strip=True)
                    if txt:
                        lines.append(txt)
                curr = curr.next_sibling
            shabads.append({
                'num': int(m.group(1)),
                'title': m.group(2),
                'lines': lines
            })
print(f"1. SGGS Shabads: {len(shabads)}")

# 2. Saloks (from Sri Guru Granth Sahib Ji)
salok_path = os.path.join(html_dir, "HindiSalokBhagatKabir.html")
saloks = []
if os.path.exists(salok_path):
    with open(salok_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    text = soup.get_text()
    start_marker = "सलोक भगत कबीर जीउ के"
    idx = text.find(start_marker)
    if idx != -1:
        salok_part = text[idx:]
        pattern = r'॥\s*([०-९\d]+)\s*॥'
        splits = re.split(pattern, salok_part)
        for i in range(1, len(splits), 2):
            num = splits[i]
            body = splits[i-1].strip()
            # clean up body
            body_lines = [l.strip() for l in body.split('\n') if l.strip()]
            saloks.append({
                'marker': num,
                'body': body_lines
            })
print(f"2. SGGS Saloks: {len(saloks)}")

# 3. Popular Dohe
dohe_path = os.path.join(html_dir, "HindiDoheBhagatKabir.html")
dohe = []
if os.path.exists(dohe_path):
    with open(dohe_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    # Look for doha blocks
    content_div = soup.find('main') or soup.find('div', class_='content') or soup
    # split by ॥
    full_text = content_div.get_text()
    # dohas end with ॥
    raw_dohas = re.findall(r'([^॥\n]+(?:[।\n][^॥\n]+)*?॥)', full_text)
    clean_dohas = []
    for d in raw_dohas:
        d_clean = d.strip()
        # skip header texts or navigation
        if len(d_clean) > 20 and not any(k in d_clean for k in ['मुख्य पृष्ठ', 'कविता वेबसाइट', 'Dohe Bhagat']):
            # Remove single leading alphabet char if any (e.g. 'अ', 'आ')
            lines = [l.strip() for l in d_clean.split('\n') if l.strip()]
            if lines and len(lines[0]) == 1 and '\u0900' <= lines[0] <= '\u097F':
                lines = lines[1:]
            if lines:
                clean_dohas.append("\n".join(lines))
    print(f"3. Popular Dohe: {len(clean_dohas)}")

# 4. Popular Pad
pad_path = os.path.join(html_dir, "HindiPadBhagatKabir.html")
if os.path.exists(pad_path):
    with open(pad_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    content_div = soup.find('main') or soup
    full_text = content_div.get_text()
    # pads often have टेक
    pad_blocks = [p.strip() for p in re.split(r'\n\s*\n', full_text) if ('॥टेक॥' in p or '॥ टेक ॥' in p or '॥1॥' in p or '॥१॥' in p) and len(p.strip()) > 40]
    print(f"4. Popular Pads: {len(pad_blocks)}")

# 5. Kabir Granthavali Sakhis (60 Angs)
sakhi_files = sorted(glob.glob(os.path.join(html_dir, "Sakhi-*-Ang-*.html")))
total_granthavali_sakhis = 0
print(f"5. Granthavali Sakhi Ang files: {len(sakhi_files)}")
for sf in sakhi_files[:5]:
    with open(sf, 'r', encoding='utf-8') as f:
        s_soup = BeautifulSoup(f.read(), 'html.parser')
    s_text = s_soup.get_text()
    # count markers ॥\d+॥
    markers = re.findall(r'॥\s*(\d+)\s*॥', s_text)
    total_granthavali_sakhis += len(markers)
    print(f"   {os.path.basename(sf)}: {len(markers)} Sakhis")

# 6. Kabir Granthavali Pads (18 Raags)
pad_files = sorted(glob.glob(os.path.join(html_dir, "Pad-Raag-*.html")))
print(f"6. Granthavali Pad Raag files: {len(pad_files)}")
total_granthavali_pads = 0
for pf in pad_files[:5]:
    with open(pf, 'r', encoding='utf-8') as f:
        p_soup = BeautifulSoup(f.read(), 'html.parser')
    p_text = p_soup.get_text()
    markers = re.findall(r'॥\s*(\d+)\s*॥', p_text)
    total_granthavali_pads += len(markers)
    print(f"   {os.path.basename(pf)}: {len(markers)} markers")

# 7. Ramaini
ramaini_path = os.path.join(html_dir, "Ramaini-Bhakt-Kabir-Ji.html")
if os.path.exists(ramaini_path):
    with open(ramaini_path, 'r', encoding='utf-8') as f:
        r_soup = BeautifulSoup(f.read(), 'html.parser')
    r_h = [h.get_text(strip=True) for h in r_soup.find_all(['h2', 'h3']) if 'रमैणी' in h.get_text() or 'बावनी' in h.get_text()]
    print(f"7. Ramaini sections: {len(r_h)} ({r_h})")
