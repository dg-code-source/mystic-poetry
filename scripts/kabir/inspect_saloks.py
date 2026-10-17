from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/html/HindiSalokBhagatKabir.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

text = soup.get_text()
# Find the start of Saloks
start_marker = "सलोक भगत कबीर जीउ के"
idx = text.find(start_marker)
if idx != -1:
    salok_part = text[idx:]
    # Split by ॥\d+॥
    pattern = r'॥\s*(\d+)\s*॥'
    splits = re.split(pattern, salok_part)
    # splits will alternate: intro, num1, text1, num2, text2, ...
    print(f"Splits length: {len(splits)}")
    # Print first 5 saloks
    for i in range(1, min(12, len(splits)), 2):
        num = splits[i]
        content = splits[i-1] if i == 1 else splits[i-1].strip()
        # The content of salok i is before marker i
        print(f"\n--- Salok {num} ---")
        print(splits[i-1].strip()[-150:])
