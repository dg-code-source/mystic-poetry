from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/html/Ramaini-Bhakt-Kabir-Ji.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

headings = soup.find_all(['h2', 'h3'])[1:] # skip title

for h in headings:
    htext = h.get_text(strip=True)
    lines = []
    curr = h.next_sibling
    while curr and curr.name not in ['h2', 'h3']:
        if hasattr(curr, 'get_text'):
            t = curr.get_text(strip=True)
            if t:
                for l in t.split('\n'):
                    l = l.strip()
                    if l and not any(k in l for k in ['मुख्य पृष्ठ', 'कविता वेबसाइट']):
                        lines.append(l)
        curr = curr.next_sibling
    print(f"\n=== {htext} (Lines: {len(lines)}) ===")
    if lines:
        print("  Line 1:", lines[0])
        print("  Line 2:", lines[1] if len(lines) > 1 else "")
