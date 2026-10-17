from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/html/HindiPadBhagatKabir.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("Title:", soup.title.string.strip() if soup.title else "")
h2s = soup.find_all(['h2', 'h3'])
print(f"Headings count: {len(h2s)}")
for h in h2s[:5]:
    print("  H:", h.get_text(strip=True))

for h in h2s[1:3]:
    print(f"\nUnder heading '{h.get_text(strip=True)}':")
    curr = h.next_sibling
    texts = []
    while curr and (curr.name not in ['h2', 'h3']):
        if hasattr(curr, 'get_text'):
            t = curr.get_text(strip=True)
            if t:
                texts.append(t)
        curr = curr.next_sibling
    for t in texts[:2]:
        print("  Pad preview:\n", t[:150], "...\n")
