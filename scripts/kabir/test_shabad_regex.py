from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/html/HindiShabadBhagatKabir.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Get text preserving newlines
main_div = soup.find('div', class_='left') or soup
text = main_div.get_text(separator='\n')

# Split by numbered headings: regex matching start of line or newline, followed by digits and dot and space
parts = re.split(r'\n\s*(?=\d+\.\s+[\u0900-\u097F])', text)

print(f"Total parts split by heading regex: {len(parts)}")
parsed_shabads = []
for p in parts:
    p = p.strip()
    m = re.match(r'^(\d+)\.\s*([^\n]+)\n([\s\S]*)', p)
    if m:
        num = int(m.group(1))
        title = m.group(2).strip()
        body = m.group(3).strip()
        lines = [l.strip() for l in body.split('\n') if l.strip() and not any(k in l for k in ['मुख्य पृष्ठ', 'कविता वेबसाइट', 'Shabad Bhakt Kabir'])]
        parsed_shabads.append({
            'num': num,
            'title': title,
            'lines': lines
        })

print(f"Successfully extracted Shabads: {len(parsed_shabads)}")
if parsed_shabads:
    print(f"First Shabad (num {parsed_shabads[0]['num']}): {parsed_shabads[0]['title']}")
    print(f"Lines count: {len(parsed_shabads[0]['lines'])}")
    print("Preview:\n  " + "\n  ".join(parsed_shabads[0]['lines'][:4]))
    
    print(f"\nShabad 107 (num {parsed_shabads[105]['num']}): {parsed_shabads[105]['title']}")
    print(f"Lines count: {len(parsed_shabads[105]['lines'])}")
    print("Preview:\n  " + "\n  ".join(parsed_shabads[105]['lines'][:4]))
    
    print(f"\nLast Shabad (num {parsed_shabads[-1]['num']}): {parsed_shabads[-1]['title']}")
    print(f"Lines count: {len(parsed_shabads[-1]['lines'])}")
    print("Preview:\n  " + "\n  ".join(parsed_shabads[-1]['lines'][:4]))
