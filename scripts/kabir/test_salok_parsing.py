from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/html/HindiSalokBhagatKabir.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

text = soup.get_text(separator='\n')
start_marker = "सलोक भगत कबीर जीउ के"
idx = text.find(start_marker)
salok_part = text[idx:]

# Find saloks: split by ॥\s*([०-९\d]+)\s*॥
pattern = r'॥\s*([०-९\d]+)\s*॥'
splits = re.split(pattern, salok_part)

dev_to_eng = {'०':'0','१':'1','२':'2','३':'3','४':'4','५':'5','६':'6','७':'7','८':'8','९':'9'}

saloks = []
salok_idx = 1
for i in range(1, len(splits), 2):
    marker_raw = splits[i]
    marker_num = "".join(dev_to_eng.get(c, c) for c in marker_raw)
    body = splits[i-1].strip()
    # clean out heading
    if "सलोक भगत कबीर जीउ के" in body:
        body = re.sub(r'सलोक भगत कबीर जीउ केੴ सतिगुर प्रसादि ॥', '', body).strip()
        body = re.sub(r'सलोक भगत कबीर जीउ के', '', body).strip()
        
    lines = [l.strip() for l in body.split('\n') if l.strip() and not any(k in l for k in ['मुख्य पृष्ठ', 'कविता वेबसाइट', 'Salok Bhagat'])]
    if lines:
        first_line = lines[0]
        # remove 'सलोक कबीर ॥' if present
        if first_line.startswith('सलोक कबीर'):
            lines = lines[1:]
            first_line = lines[0] if lines else first_line
        saloks.append({
            'num': salok_idx,
            'marker': marker_num,
            'title': f"Salok {salok_idx}: {first_line[:35]}...",
            'title_hi': f"सलोक {salok_idx}: {first_line[:35]}...",
            'lines': lines
        })
        salok_idx += 1

print(f"Extracted Saloks: {len(saloks)}")
print(f"Salok 1:\n  Title: {saloks[0]['title_hi']}\n  Marker: {saloks[0]['marker']}\n  Lines: {saloks[0]['lines']}")
print(f"Salok 243:\n  Title: {saloks[242]['title_hi']}\n  Marker: {saloks[242]['marker']}\n  Lines: {saloks[242]['lines']}")
print(f"Salok 244 (Soora So Pahchaniye 1):\n  Title: {saloks[243]['title_hi']}\n  Marker: {saloks[243]['marker']}\n  Lines: {saloks[243]['lines']}")
print(f"Salok 245 (Soora So Pahchaniye 2):\n  Title: {saloks[244]['title_hi']}\n  Marker: {saloks[244]['marker']}\n  Lines: {saloks[244]['lines']}")
