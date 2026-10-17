# -*- coding: utf-8 -*-
"""
Generates clean Devanagari Markdown editions for the 5 works:
- Bulleh_Shah_Baranmah.md
- Bulleh_Shah_Athwara.md
- Bulleh_Shah_Gandhan.md
- Bulleh_Shah_Dohre.md
- Bulleh_Shah_Siharfian.md
With zero external links.
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTRACTED_DIR = os.path.join(BASE_DIR, "data", "raw_extracted")

# 1. Baranmah
with open(os.path.join(EXTRACTED_DIR, "baranmah.json"), "r", encoding="utf-8") as f:
    b_data = json.load(f)

b_md = [
    "# बाबा बुल्ले शाह : बारहमाह (Baranmah)",
    "## Baba Bulleh Shah : The Song of Twelve Months\n",
    "> **प्रमाणिक संकलन:** बाबा बुल्ले शाह जी की कालजयी रचना 'बारहमाह' (अस्सू से भादों) का मूल देवनागरी पाठ\n",
    "---\n",
    "## विषय-सूची (Table of Contents)\n"
]
for item in b_data:
    b_md.append(f"- [{item['title']}](#{item['title'].replace(' ', '-').replace('.', '')})")
b_md.append("\n---\n")

for item in b_data:
    b_md.append(f"## {item['title']}\n")
    for l in item["lines"]:
        b_md.append(f"{l}  ")
    b_md.append("\n---\n")

with open(os.path.join(BASE_DIR, "Bulleh_Shah_Baranmah.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(b_md))

# 2. Athwara
with open(os.path.join(EXTRACTED_DIR, "athwara.json"), "r", encoding="utf-8") as f:
    a_data = json.load(f)

a_md = [
    "# बाबा बुल्ले शाह : अठवारा (Athwara)",
    "## Baba Bulleh Shah : The Song of the Seven Days\n",
    "> **प्रमाणिक संकलन:** बाबा बुल्ले शाह जी का आध्यात्मिक 'अठवारा' (छनिछरवार से जुंमा) का मूल देवनागरी पाठ\n",
    "---\n",
    "## विषय-सूची (Table of Contents)\n"
]
for item in a_data:
    a_md.append(f"- [{item['title']}](#{item['title'].replace(' ', '-').replace('.', '')})")
a_md.append("\n---\n")

for item in a_data:
    a_md.append(f"## {item['title']}\n")
    for l in item["lines"]:
        b_md.append(f"{l}  ")
        a_md.append(f"{l}  ")
    a_md.append("\n---\n")

with open(os.path.join(BASE_DIR, "Bulleh_Shah_Athwara.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(a_md))

# 3. Gandhan
with open(os.path.join(EXTRACTED_DIR, "gandhan.json"), "r", encoding="utf-8") as f:
    g_data = json.load(f)

g_md = [
    "# बाबा बुल्ले शाह : गन्धां (Gandhan)",
    "## Baba Bulleh Shah : The Forty Knots of Mystical Nuptials\n",
    "> **प्रमाणिक संकलन:** बाबा बुल्ले शाह जी की प्रतीकात्मक रचना 'गन्धां' (गाँठें) का मूल देवनागरी पाठ\n",
    "---\n",
    "## विषय-सूची (Table of Contents)\n"
]
for item in g_data:
    g_md.append(f"- [{item['title']}](#{item['title'].replace(' ', '-').replace('.', '')})")
g_md.append("\n---\n")

for item in g_data:
    g_md.append(f"## {item['title']}\n")
    for l in item["lines"]:
        g_md.append(f"{l}  ")
    g_md.append("\n---\n")

with open(os.path.join(BASE_DIR, "Bulleh_Shah_Gandhan.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(g_md))

# 4. Dohre
with open(os.path.join(EXTRACTED_DIR, "dohre.json"), "r", encoding="utf-8") as f:
    d_data = json.load(f)

d_md = [
    "# बाबा बुल्ले शाह : सम्पूर्ण दोहरे (Dohre)",
    "## Baba Bulleh Shah : The Complete Couplets (1–56)\n",
    "> **प्रमाणिक संकलन:** बाबा बुल्ले शाह जी के 56 आध्यात्मिक दोहों का मूल देवनागरी संकलन\n",
    "---\n",
    "## विषय-सूची (Table of Contents)\n"
]
for item in d_data:
    first_snippet = item["lines"][0][:30] if item["lines"] else ""
    d_md.append(f"- [{item['title']}: {first_snippet}](#{item['title'].replace(' ', '-').replace('.', '')})")
d_md.append("\n---\n")

for item in d_data:
    d_md.append(f"## {item['title']}\n")
    for l in item["lines"]:
        d_md.append(f"{l}  ")
    d_md.append("\n---\n")

with open(os.path.join(BASE_DIR, "Bulleh_Shah_Dohre.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(d_md))

# 5. Siharfian
with open(os.path.join(EXTRACTED_DIR, "siharfian.json"), "r", encoding="utf-8") as f:
    s_data = json.load(f)

s_md = [
    "# बाबा बुल्ले शाह : सम्पूर्ण सीहरफ़ियां (Siharfian)",
    "## Baba Bulleh Shah : The Complete Alphabetical Acrostics\n",
    "> **प्रमाणिक संकलन:** बाबा बुल्ले शाह जी की 3 सीहरफ़ियों का मूल देवनागरी पाठ\n",
    "---\n",
    "## विषय-सूची (Table of Contents)\n"
]
for cycle in s_data:
    s_md.append(f"\n### {cycle['cycle']}\n")
    if cycle.get("refrain"):
        s_md.append(f"> *टेक (Refrain):* {cycle['refrain']}\n")
    for item in cycle["stanzas"]:
        s_md.append(f"- [{item['title']}](#{item['title'].replace(' ', '-').replace('.', '').replace('(', '').replace(')', '')})")

s_md.append("\n\n---\n")

for cycle in s_data:
    s_md.append(f"\n# {cycle['cycle']}\n")
    if cycle.get("refrain"):
        s_md.append(f"> **टेक (Refrain):** {cycle['refrain']}\n")
    s_md.append("---\n")
    for item in cycle["stanzas"]:
        s_md.append(f"## {item['title']}\n")
        for l in item["lines"]:
            s_md.append(f"{l}  ")
        s_md.append("\n---\n")

with open(os.path.join(BASE_DIR, "Bulleh_Shah_Siharfian.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(s_md))

print("Created all 5 clean Devanagari Markdown editions:")
print("  - Bulleh_Shah_Baranmah.md")
print("  - Bulleh_Shah_Athwara.md")
print("  - Bulleh_Shah_Gandhan.md")
print("  - Bulleh_Shah_Dohre.md")
print("  - Bulleh_Shah_Siharfian.md")
