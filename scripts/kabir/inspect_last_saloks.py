from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/html/HindiSalokBhagatKabir.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

text = soup.get_text()
start_marker = "सलोक भगत कबीर जीउ के"
idx = text.find(start_marker)
salok_part = text[idx:]
pattern = r'॥\s*([०-९\d]+)\s*॥'
splits = re.split(pattern, salok_part)

print(f"Total parts: {len(splits)}")
# Show last 5
for i in range(len(splits)-10, len(splits), 2):
    if i > 0 and i < len(splits):
        print(f"\nMarker: {splits[i]}")
        print(f"Content: {splits[i-1].strip()[-120:]}")
