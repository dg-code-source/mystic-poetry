from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Sakhi
with open('data/kabir/raw/html/Sakhi-Bhakt-Kabir-Ji.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
sakhi_links = []
for a in soup.find_all('a', href=True):
    h = a['href']
    if 'Sakhi-' in h and h != 'Sakhi-Bhakt-Kabir-Ji.php':
        sakhi_links.append((h, a.get_text(strip=True)))

print(f"Sakhi sub-pages: {len(sakhi_links)}")
for h, t in sakhi_links:
    print(f"  {h} -> {t}")

# Pad
with open('data/kabir/raw/html/Pad-Bhakt-Kabir-Ji.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
pad_links = []
for a in soup.find_all('a', href=True):
    h = a['href']
    if 'Pad-' in h and h != 'Pad-Bhakt-Kabir-Ji.php':
        pad_links.append((h, a.get_text(strip=True)))

print(f"\nPad sub-pages: {len(pad_links)}")
for h, t in pad_links:
    print(f"  {h} -> {t}")
