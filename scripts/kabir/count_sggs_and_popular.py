from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. HindiShabadBhagatKabir.php.html
with open('data/kabir/raw/html/HindiShabadBhagatKabir.php.html', 'r', encoding='utf-8') as f:
    shabad_html = f.read()

soup_shabad = BeautifulSoup(shabad_html, 'html.parser')
# Find all poem sections. In hindi-kavita, poems usually have <h2> or <h3> with titles, or are inside specific divs
shabad_h = soup_shabad.find_all(['h2', 'h3'])
print(f"Shabad headings count: {len(shabad_h)}")
valid_shabad = [h.get_text(strip=True) for h in shabad_h if re.match(r'^\d+\.', h.get_text(strip=True))]
print(f"Numbered Shabads: {len(valid_shabad)}")
if valid_shabad:
    print(f"First 5: {valid_shabad[:5]}")
    print(f"Last 5: {valid_shabad[-5:]}")

# 2. HindiSalokBhagatKabir.php.html
with open('data/kabir/raw/html/HindiSalokBhagatKabir.php.html', 'r', encoding='utf-8') as f:
    salok_html = f.read()

soup_salok = BeautifulSoup(salok_html, 'html.parser')
salok_text = soup_salok.get_text()
# Find all saloks by ॥\d+॥
salok_items = re.findall(r'([^॥\n]+(?:॥\s*[^॥\n]+)*?॥\s*(\d+)\s*॥)', salok_text)
print(f"\nSaloks matched by ॥N॥: {len(salok_items)}")
if salok_items:
    print(f"First salok number: {salok_items[0][1]}, text: {salok_items[0][0].strip()[:60]}...")
    print(f"Last salok number: {salok_items[-1][1]}, text: {salok_items[-1][0].strip()[:60]}...")

# 3. HindiDoheBhagatKabir.php.html
with open('data/kabir/raw/html/HindiDoheBhagatKabir.php.html', 'r', encoding='utf-8') as f:
    dohe_html = f.read()

soup_dohe = BeautifulSoup(dohe_html, 'html.parser')
# Let's inspect paragraphs or text blocks
dohe_text = soup_dohe.get_text()
# Check for double dandas ॥
dohe_matches = [p.strip() for p in re.split(r'\n\s*\n', dohe_text) if '॥' in p and len(p.strip()) > 15]
print(f"\nDohe blocks with ॥: {len(dohe_matches)}")
if dohe_matches:
    print(f"First doha: {dohe_matches[0][:80]}...")

# 4. HindiPadBhagatKabir.php.html
with open('data/kabir/raw/html/HindiPadBhagatKabir.php.html', 'r', encoding='utf-8') as f:
    pad_html = f.read()

soup_pad = BeautifulSoup(pad_html, 'html.parser')
pad_text = soup_pad.get_text()
pad_blocks = [p.strip() for p in re.split(r'\n\s*\n', pad_text) if '॥' in p and len(p.strip()) > 30]
print(f"\nPad blocks with ॥: {len(pad_blocks)}")
if pad_blocks:
    print(f"First pad: {pad_blocks[0][:80]}...")
