import os
import re
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_dir = "data/kabir/raw/html"

def clean_text(text):
    text = re.sub(r'\r', '', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

path = os.path.join(html_dir, "HindiShabadBhagatKabir.html")
with open(path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

headings = soup.find_all(['h2', 'h3'])
print(f"Total headings found: {len(headings)}")
shabads = []
for h in headings:
    txt = h.get_text(strip=True)
    m = re.match(r'^(\d+)\.\s*(.*)', txt)
    if m:
        num = int(m.group(1))
        title = m.group(2).strip()
        shabads.append((num, title))

print(f"Matched numbered headings: {len(shabads)}")
if shabads:
    print(f"Min num: {min(x[0] for x in shabads)}, Max num: {max(x[0] for x in shabads)}")
    print("Numbers present:", [x[0] for x in shabads])
