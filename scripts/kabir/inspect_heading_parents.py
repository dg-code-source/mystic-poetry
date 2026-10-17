from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/raw/html/HindiShabadBhagatKabir.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

headings = soup.find_all(['h2', 'h3'])
print("Heading 1 parent:", headings[1].parent.name, headings[1].parent.get('class'))
print("Heading 2 parent:", headings[2].parent.name, headings[2].parent.get('class'))
print("Heading 20 parent:", headings[20].parent.name, headings[20].parent.get('class'))
print("Heading 50 parent:", headings[50].parent.name, headings[50].parent.get('class'))
print("Heading 100 parent:", headings[100].parent.name, headings[100].parent.get('class'))
