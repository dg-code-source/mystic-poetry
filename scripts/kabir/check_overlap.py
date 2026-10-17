import os
import glob
import re
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect HindiDoheBhagatKabir vs Sakhis
with open('data/kabir/raw/html/HindiDoheBhagatKabir.html', 'r', encoding='utf-8') as f:
    soup_dohe = BeautifulSoup(f.read(), 'html.parser')

dohe_text = soup_dohe.get_text()
# Find first phrases
dohas = [d.strip() for d in re.split(r'[॥\n]\s*', dohe_text) if len(d.strip()) > 15]

print(f"Sample doha phrases: {dohas[:5]}")

# Check in Sakhi files
sakhi_files = glob.glob('data/kabir/raw/html/Sakhi-*.html')
all_sakhi_text = ""
for sf in sakhi_files:
    with open(sf, 'r', encoding='utf-8') as f:
        all_sakhi_text += f.read()

found = 0
for d in dohas[:20]:
    # take 10 chars
    snip = d[:12]
    if snip in all_sakhi_text:
        found += 1

print(f"Out of first 20 doha snippets, found in Sakhis: {found}")
