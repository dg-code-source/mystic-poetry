import os
import glob
import re
from bs4 import BeautifulSoup
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

html_dir = "data/kabir/raw/html"
os.makedirs("data/kabir/raw", exist_ok=True)

def clean_text(text):
    text = re.sub(r'\r', '', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

dev_to_eng_digits = {'०':'0','१':'1','२':'2','३':'3','४':'4','५':'5','६':'6','७':'7','८':'8','९':'9'}

def transliterate_basic(dev_str):
    """Clean phonetic transliteration for titles."""
    charmap = {
        'अ': 'A', 'आ': 'Aa', 'इ': 'I', 'ई': 'Ee', 'उ': 'U', 'ऊ': 'Oo', 'ऋ': 'Ri',
        'ए': 'E', 'ऐ': 'Ai', 'ओ': 'O', 'औ': 'Au', 'अं': 'An', 'अः': 'Ah',
        'क': 'Ka', 'ख': 'Kha', 'ग': 'Ga', 'घ': 'Gha', 'ङ': 'Nga',
        'च': 'Cha', 'छ': 'Chha', 'ज': 'Ja', 'झ': 'Jha', 'ञ': 'Nya',
        'ट': 'Ta', 'ठ': 'Tha', 'ड': 'Da', 'ढ': 'Dha', 'ण': 'Na',
        'त': 'Ta', 'थ': 'Tha', 'द': 'Da', 'ध': 'Dha', 'न': 'Na',
        'प': 'Pa', 'फ': 'Pha', 'ब': 'Ba', 'भ': 'Bha', 'म': 'Ma',
        'य': 'Ya', 'र': 'Ra', 'ल': 'La', 'व': 'Va', 'श': 'Sha', 'ष': 'Sha', 'स': 'Sa', 'ह': 'Ha',
        'ा': 'a', 'ि': 'i', 'ी': 'ee', 'ु': 'u', 'ू': 'oo', 'ृ': 'ri',
        'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au', 'ं': 'n', 'ँ': 'n', '्': '',
        '॥': '', '।': '', '—': '-', '-': '-', ':': ':', '1':'1','2':'2','3':'3','4':'4','5':'5'
    }
    # Simple transliteration word by word
    words = dev_str.split()
    t_words = []
    for w in words:
        tw = ""
        for char in w:
            tw += charmap.get(char, char if char.isalnum() or char in ' -:' else '')
        if tw:
            t_words.append(tw.capitalize() if len(tw)>1 else tw)
    res = " ".join(t_words)
    return res if res else dev_str

# ==========================================
# 1. PARSE SHABADS (149 from SGGS)
# ==========================================
print("Parsing 149 SGGS Shabads...")
shabad_path = os.path.join(html_dir, "HindiShabadBhagatKabir.html")
with open(shabad_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

main_div = soup.find('div', class_='left') or soup
text = main_div.get_text(separator='\n')
parts = re.split(r'\n\s*(?=\d+\.\s+[\u0900-\u097F])', text)

shabads = []
for p in parts:
    p = p.strip()
    m = re.match(r'^(\d+)\.\s*([^\n]+)\n([\s\S]*)', p)
    if m:
        num = int(m.group(1))
        title_hi = m.group(2).strip()
        body = m.group(3).strip()
        lines = [clean_text(l) for l in body.split('\n') if clean_text(l) and not any(k in l for k in ['मुख्य पृष्ठ', 'कविता वेबसाइट', 'Shabad Bhakt Kabir'])]
        
        shabads.append({
            'id': f"kabir_shabad_{num:03d}",
            'poet_id': 'sant_kabir',
            'type': 'kabir_shabad',
            'section': 'Sri Guru Granth Sahib Ji Bani',
            'num': num,
            'title': f"Shabad {num}: {transliterate_basic(title_hi[:30])}",
            'title_hi': f"शब्द {num}: {title_hi}",
            'title_translit': f"Shabad {num}: {transliterate_basic(title_hi[:30])}",
            'original_text': "\n".join(lines),
            'devanagari_text': "\n".join(lines),
            'lines': lines
        })

print(f"Total Shabads parsed: {len(shabads)}")

# ==========================================
# 2. PARSE SALOKS (245 from SGGS)
# ==========================================
print("\nParsing 245 SGGS Saloks...")
salok_path = os.path.join(html_dir, "HindiSalokBhagatKabir.html")
with open(salok_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

text = soup.get_text(separator='\n')
start_marker = "सलोक भगत कबीर जीउ के"
idx = text.find(start_marker)
salok_part = text[idx:] if idx != -1 else text

pattern = r'॥\s*([०-९\d]+)\s*॥'
splits = re.split(pattern, salok_part)

saloks = []
salok_idx = 1
for i in range(1, len(splits), 2):
    marker_raw = splits[i]
    marker_num = "".join(dev_to_eng_digits.get(c, c) for c in marker_raw)
    body = splits[i-1].strip()
    if "सलोक भगत कबीर जीउ के" in body:
        body = re.sub(r'सलोक भगत कबीर जीउ केੴ सतिगुर प्रसादि ॥', '', body).strip()
        body = re.sub(r'सलोक भगत कबीर जीउ के', '', body).strip()
        
    lines = [clean_text(l) for l in body.split('\n') if clean_text(l) and not any(k in l for k in ['मुख्य पृष्ठ', 'कविता वेबसाइट', 'Salok Bhagat'])]
    if lines:
        first_line = lines[0]
        if first_line.startswith('सलोक कबीर'):
            lines = lines[1:]
            first_line = lines[0] if lines else first_line
        if first_line.startswith('ੴ सतिगुर प्रसादि'):
            lines = lines[1:]
            first_line = lines[0] if lines else first_line
            
        t_translit = transliterate_basic(first_line[:30])
        saloks.append({
            'id': f"kabir_salok_{salok_idx:03d}",
            'poet_id': 'sant_kabir',
            'type': 'kabir_salok',
            'section': 'Sri Guru Granth Sahib Ji Bani',
            'num': salok_idx,
            'marker': marker_num,
            'title': f"Salok {salok_idx}: {t_translit}",
            'title_hi': f"सलोक {salok_idx}: {first_line[:35]}...",
            'title_translit': f"Salok {salok_idx}: {t_translit}",
            'original_text': "\n".join(lines),
            'devanagari_text': "\n".join(lines),
            'lines': lines
        })
        salok_idx += 1

print(f"Total Saloks parsed: {len(saloks)}")

# ==========================================
# 3. PARSE POPULAR DOHAS (84 Classic Couplets)
# ==========================================
print("\nParsing 84 Popular Dohas...")
dohe_path = os.path.join(html_dir, "HindiDoheBhagatKabir.html")
with open(dohe_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

main = soup.find('div', class_='left') or soup
text = main.get_text(separator='\n')
dohas_raw = re.split(r'॥\s*', text)

dohe = []
doha_idx = 1
for d in dohas_raw:
    d = d.strip()
    if not d or len(d) < 15:
        continue
    raw_lines = [clean_text(l) for l in d.split('\n') if clean_text(l)]
    # filter navigation, headers, single char alphabets
    filtered_lines = []
    for l in raw_lines:
        if len(l) <= 2:
            continue
        if any(k in l for k in ['मुख्य पृष्ठ', 'कविता वेबसाइट', 'Dohe Bhagat Kabir', 'दोहे : भक्त कबीर जी']):
            continue
        filtered_lines.append(l)
        
    if filtered_lines:
        first_line = filtered_lines[0]
        t_translit = transliterate_basic(first_line[:30])
        # ensure last line ends with ॥
        if not filtered_lines[-1].endswith('॥'):
            filtered_lines[-1] += ' ॥'
            
        dohe.append({
            'id': f"kabir_doha_{doha_idx:03d}",
            'poet_id': 'sant_kabir',
            'type': 'kabir_doha',
            'section': 'Kabir Ke Dohe',
            'num': doha_idx,
            'title': f"Doha {doha_idx}: {t_translit}",
            'title_hi': f"दोहा {doha_idx}: {first_line[:35]}...",
            'title_translit': f"Doha {doha_idx}: {t_translit}",
            'original_text': "\n".join(filtered_lines),
            'devanagari_text': "\n".join(filtered_lines),
            'lines': filtered_lines
        })
        doha_idx += 1

print(f"Total Dohas parsed: {len(dohe)}")

# ==========================================
# 4. PARSE RAMAINIS (8 Metrical Discourses)
# ==========================================
print("\nParsing 8 Ramainis...")
ramaini_path = os.path.join(html_dir, "Ramaini-Bhakt-Kabir-Ji.html")
with open(ramaini_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

headings_elements = soup.find_all(['h2', 'h3'])[1:] # skip page title
ramainis = []
for idx_r, h in enumerate(headings_elements, 1):
    htext = h.get_text(strip=True)
    lines = []
    curr = h.next_sibling
    while curr and curr.name not in ['h2', 'h3']:
        if hasattr(curr, 'get_text'):
            t = curr.get_text(strip=True)
            if t:
                for l in t.split('\n'):
                    l = clean_text(l)
                    if l and not any(k in l for k in ['मुख्य पृष्ठ', 'कविता वेबसाइट', 'Ramaini : Bhakt Kabir']):
                        lines.append(l)
        curr = curr.next_sibling
        
    if lines:
        t_translit = transliterate_basic(htext)
        ramainis.append({
            'id': f"kabir_ramaini_{idx_r:02d}",
            'poet_id': 'sant_kabir',
            'type': 'kabir_ramaini',
            'section': 'Kabir Ramaini',
            'num': idx_r,
            'title': f"Ramaini {idx_r}: {t_translit}",
            'title_hi': f"रमैणी {idx_r}: {htext}",
            'title_translit': f"Ramaini {idx_r}: {t_translit}",
            'original_text': "\n".join(lines),
            'devanagari_text': "\n".join(lines),
            'lines': lines
        })

print(f"Total Ramainis parsed: {len(ramainis)}")

# ==========================================
# 5. PARSE KABIR GRANTHAVALI SAKHIS (59 Angs)
# ==========================================
print("\nParsing 59 Granthavali Sakhi Angs...")
sakhi_files = sorted(glob.glob(os.path.join(html_dir, "Sakhi-*-Ang-*.html")))
sakhis_by_ang = []

for idx_s, sf in enumerate(sakhi_files, 1):
    fname = os.path.basename(sf)
    with open(sf, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # get title
    h1 = soup.find('h1') or soup.find(['h2', 'h3'])
    ang_title_raw = h1.get_text(strip=True) if h1 else fname
    ang_title_clean = re.sub(r'^\d+\.\s*', '', ang_title_raw)
    ang_title_clean = ang_title_clean.replace('साखी - ', '').replace('साखी : ', '').strip()
    
    # Extract couplets
    text = soup.get_text(separator='\n')
    # find couplets ending with ॥\d+॥
    couplets_raw = re.findall(r'([^॥\n]+(?:[।\n][^॥\n]+)*?॥\s*(\d+)\s*॥)', text)
    lines_formatted = []
    couplets_data = []
    
    for c_text, c_num in couplets_raw:
        c_lines = [clean_text(l) for l in c_text.split('\n') if clean_text(l) and not any(k in l for k in ['मुख्य पृष्ठ', 'कविता वेबसाइट', 'स्पष्टीकरण', 'हस्तलिखित प्रति'])]
        if c_lines:
            # check if last line has marker
            c_str = "\n".join(c_lines) + f" ॥{c_num}॥"
            lines_formatted.extend(c_lines)
            lines_formatted.append(f"— [दोहा {c_num}]")
            couplets_data.append({
                'num': int(c_num),
                'lines': c_lines
            })
            
    t_translit = transliterate_basic(ang_title_clean)
    sakhis_by_ang.append({
        'id': f"kabir_sakhi_ang_{idx_s:02d}",
        'poet_id': 'sant_kabir',
        'type': 'kabir_sakhi',
        'section': 'Kabir Granthavali Sakhis',
        'num': idx_s,
        'ang_name': ang_title_clean,
        'title': f"Sakhi Ang {idx_s}: {t_translit}",
        'title_hi': f"साखी अंग {idx_s}: {ang_title_clean}",
        'title_translit': f"Sakhi Ang {idx_s}: {t_translit}",
        'couplets_count': len(couplets_data),
        'original_text': "\n".join(lines_formatted),
        'devanagari_text': "\n".join(lines_formatted),
        'lines': lines_formatted,
        'couplets': couplets_data
    })

print(f"Total Sakhi Angs parsed: {len(sakhis_by_ang)}")

# ==========================================
# 6. PARSE KABIR GRANTHAVALI PADS (17 Raags)
# ==========================================
print("\nParsing 17 Granthavali Pad Raags...")
pad_files = sorted(glob.glob(os.path.join(html_dir, "Pad-Raag-*.html")))
pads_by_raag = []

for idx_p, pf in enumerate(pad_files, 1):
    fname = os.path.basename(pf)
    with open(pf, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    h1 = soup.find('h1') or soup.find(['h2', 'h3'])
    raag_title_raw = h1.get_text(strip=True) if h1 else fname
    raag_title_clean = re.sub(r'^पद\s*-\s*', '', raag_title_raw).replace(' : भक्त कबीर जी (हिन्दी कविता)', '').strip()
    
    # extract lines
    main = soup.find('div', class_='left') or soup
    text = main.get_text(separator='\n')
    lines = [clean_text(l) for l in text.split('\n') if clean_text(l) and not any(k in l for k in ['मुख्य पृष्ठ', 'कविता वेबसाइट', 'स्पष्टीकरण', 'हस्तलिखित प्रति', 'Pad : Bhakt Kabir'])]
    
    t_translit = transliterate_basic(raag_title_clean)
    pads_by_raag.append({
        'id': f"kabir_pad_raag_{idx_p:02d}",
        'poet_id': 'sant_kabir',
        'type': 'kabir_pad',
        'section': 'Kabir Granthavali Pads',
        'num': idx_p,
        'raag_name': raag_title_clean,
        'title': f"Pad: {t_translit}",
        'title_hi': f"पद: {raag_title_clean}",
        'title_translit': f"Pad: {t_translit}",
        'original_text': "\n".join(lines),
        'devanagari_text': "\n".join(lines),
        'lines': lines
    })

print(f"Total Pad Raags parsed: {len(pads_by_raag)}")

# ==========================================
# COMPILE INTO MASTER RAW JSON
# ==========================================
all_kabir_items = (
    shabads +
    saloks +
    dohe +
    ramainis +
    sakhis_by_ang +
    pads_by_raag
)

print(f"\n==========================================")
print(f"GRAND TOTAL KABIR MASTERPIECES: {len(all_kabir_items)}")
print(f"  - SGGS Shabads: {len(shabads)}")
print(f"  - SGGS Saloks: {len(saloks)}")
print(f"  - Popular Dohe: {len(dohe)}")
print(f"  - Ramainis: {len(ramainis)}")
print(f"  - Granthavali Sakhi Angs: {len(sakhis_by_ang)}")
print(f"  - Granthavali Pad Raags: {len(pads_by_raag)}")
print(f"==========================================")

with open("data/kabir/raw/kabir_all_raw.json", "w", encoding="utf-8") as f:
    json.dump(all_kabir_items, f, ensure_ascii=False, indent=2)

print(f"Saved complete raw dataset to data/kabir/raw/kabir_all_raw.json ({os.path.getsize('data/kabir/raw/kabir_all_raw.json')} bytes)")
