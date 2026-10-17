from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Shabad
with open('data/kabir/raw/html/HindiShabadBhagatKabir.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("=== SHABAD INSPECTION ===")
# Find all h2/h3
headings = soup.find_all(['h2', 'h3'])
print(f"Total headings: {len(headings)}")
for i, h in enumerate(headings[1:6], 1):
    print(f"\n--- Heading {i}: {h.get_text(strip=True)} ---")
    # Let's inspect following siblings or parent
    curr = h.next_sibling
    texts = []
    while curr and (curr.name not in ['h2', 'h3']):
        if hasattr(curr, 'get_text'):
            t = curr.get_text(strip=True)
            if t:
                texts.append(t)
        curr = curr.next_sibling
    print("Content preview:", "\n".join(texts[:3]))

# Salok
with open('data/kabir/raw/html/HindiSalokBhagatKabir.html', 'r', encoding='utf-8') as f:
    soup_s = BeautifulSoup(f.read(), 'html.parser')

print("\n=== SALOK INSPECTION ===")
p_tags = soup_s.find_all('p')
print(f"P tags count: {len(p_tags)}")
for i, p in enumerate(p_tags[:4]):
    t = p.get_text(strip=True)
    if len(t) > 20:
        print(f"P {i} preview: {t[:120]}...")
