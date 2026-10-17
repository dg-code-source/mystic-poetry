from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/html/HindiShabadBhagatKabir.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

headings = soup.find_all(['h2', 'h3'])
for i in [1, 2, 10, 50, 100]:
    h = headings[i]
    print(f"\n================ Heading {i}: {h.get_text(strip=True)} ================")
    p = h.parent
    print(f"Parent tag: <{p.name}> with class {p.get('class')}")
    # print text of parent
    print("Parent text preview:\n", p.get_text(separator='\n', strip=True)[:250])
