from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/html/HindiShabadBhagatKabir.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

headings = soup.find_all(['h2', 'h3'])
print(f"Total headings: {len(headings)}")
for i, h in enumerate(headings[1:6], 1):
    print(f"\nHeading {i}: {h.get_text(strip=True)}")
    curr = h.next_sibling
    texts = []
    while curr and (curr.name not in ['h2', 'h3']):
        if hasattr(curr, 'get_text'):
            t = curr.get_text(separator='\n', strip=True)
            if t:
                texts.append(t)
        curr = curr.next_sibling
    print("Content preview:\n" + "\n".join(texts)[:200])
