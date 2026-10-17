from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/html/Ramaini-Bhakt-Kabir-Ji.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

headings = soup.find_all(['h2', 'h3'])
print(f"Headings count: {len(headings)}")
for h in headings:
    print("  Heading:", repr(h.get_text(strip=True)))
