from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/html/HindiDoheBhagatKabir.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

main = soup.find('div', class_='left') or soup
text = main.get_text(separator='\n')

# Find all couplets ending with ॥
# In Hindi dohas, they typically consist of two lines: line 1 ending in । or comma or newline, line 2 ending in ॥
dohas_raw = re.split(r'॥\s*', text)
print(f"Total splits by ॥: {len(dohas_raw)}")

clean_dohas = []
for d in dohas_raw:
    d = d.strip()
    if not d or len(d) < 15:
        continue
    # remove navigation or headings
    lines = [l.strip() for l in d.split('\n') if l.strip()]
    # filter out single letters (e.g. 'अ', 'आ', 'इ' section markers)
    lines = [l for l in lines if len(l) > 2 and not any(k in l for k in ['मुख्य पृष्ठ', 'कविता वेबसाइट', 'Dohe Bhagat Kabir'])]
    if len(lines) >= 1:
        # Check if it looks like a doha
        doha_text = "\n".join(lines) + " ॥"
        if len(doha_text) >= 20:
            clean_dohas.append(lines)

print(f"Clean Dohe parsed: {len(clean_dohas)}")
for i, d in enumerate(clean_dohas[:5], 1):
    print(f"\nDoha {i}:")
    for l in d:
        print("  ", l)

print(f"\nLast Doha ({len(clean_dohas)}):")
for l in clean_dohas[-1]:
    print("  ", l)
