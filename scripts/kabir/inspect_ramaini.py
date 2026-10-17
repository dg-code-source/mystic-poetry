from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/html/Ramaini-Bhakt-Kabir-Ji.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("Title:", soup.title.string.strip() if soup.title else "")
headings = [h.get_text(strip=True) for h in soup.find_all(['h2', 'h3'])]
print(f"Headings: {headings}")

# Check content
text = soup.get_text()
# Find ramaini markers like ॥१॥ or similar
lines = [l.strip() for l in text.split('\n') if l.strip()]
print(f"Lines count: {len(lines)}")
# Find numbered sections
numbered = [l for l in lines if re.match(r'^(?:रमैणी|\d+|राग)\b', l)]
print(f"Sample numbered/section lines: {numbered[:10]}")
