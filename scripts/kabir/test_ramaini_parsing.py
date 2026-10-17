from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/html/Ramaini-Bhakt-Kabir-Ji.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

main = soup.find('div', class_='left') or soup
text = main.get_text(separator='\n')

headings = ['राग सूहौ', 'ग्रंथ बावनी', 'सतपदी रमैणी', 'बड़ी अष्टपदी रमैणी', 'दुपदी रमैणी', 'अष्टपदी रमैणी', 'बारहपदी रमैणी', 'चौपदी रमैणी']

# Split text by headings
pattern = r'\n(?=(?:राग सूहौ|ग्रंथ बावनी|सतपदी रमैणी|बड़ी अष्टपदी रमैणी|दुपदी रमैणी|अष्टपदी रमैणी|बारहपदी रमैणी|चौपदी रमैणी))'
sections = re.split(pattern, text)

print(f"Total Ramaini sections: {len(sections)}")
parsed_ramaini = []
for s in sections:
    s = s.strip()
    if not s:
        continue
    first_line = s.split('\n')[0].strip()
    if any(h in first_line for h in headings):
        body_lines = [l.strip() for l in s.split('\n')[1:] if l.strip() and not any(k in l for k in ['मुख्य पृष्ठ', 'कविता वेबसाइट'])]
        parsed_ramaini.append({
            'title': first_line,
            'lines': body_lines
        })

print(f"Extracted Ramainis: {len(parsed_ramaini)}")
for i, r in enumerate(parsed_ramaini, 1):
    print(f"\nRamaini {i}: {r['title']} (Lines: {len(r['lines'])})")
    print("  Preview:", r['lines'][0] if r['lines'] else "None")
