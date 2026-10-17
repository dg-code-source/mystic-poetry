from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/html/Sakhi-Gurudev-Ko-Ang-Bhakt-Kabir-Ji.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("Title:", soup.title.string.strip() if soup.title else "")
main = soup.find('main') or soup
text = main.get_text()
# Split by ॥\d+॥
import re
sakhis = re.findall(r'([^॥\n]+(?:[।\n][^॥\n]+)*?॥\s*(\d+)\s*॥)', text)
print(f"Found {len(sakhis)} sakhis in Gurudev Ko Ang:")
for s, num in sakhis[:5]:
    print(f"\n[Sakhi {num}]:\n{s.strip()}")
