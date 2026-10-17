from bs4 import BeautifulSoup
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/html/BhaktKabir.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("Page Title:", soup.title.string if soup.title else "No Title")

# Group links by target base url
grouped = defaultdict(list)
for a in soup.find_all('a', href=True):
    href = a['href']
    text = a.get_text(strip=True)
    base = href.split('#')[0]
    grouped[base].append((href, text))

print(f"\nUnique base pages found in links: {len(grouped)}")
for base, items in grouped.items():
    print(f"\nBase: {base} (Total links: {len(items)})")
    for h, t in items[:5]:
        print(f"   {h} -> {t}")
    if len(items) > 5:
        print(f"   ... and {len(items)-5} more")
