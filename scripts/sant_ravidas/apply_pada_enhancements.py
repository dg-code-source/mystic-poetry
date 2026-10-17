# -*- coding: utf-8 -*-
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LEX_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "ravidas_lexicon.json")

lex = json.load(open(LEX_PATH, encoding='utf-8'))

ENHANCEMENTS = {
    "अँग": {"roman": "ang", "hi": "अंग-प्रत्यंग में", "en": "every limb of the body"},
    "जी": {"roman": "jee", "hi": "परम आदरणीय प्रभु", "en": "Revered Lord"},
    "चितवत": {"roman": "chitvat", "hi": "प्रेमपूर्वक निहारता है", "en": "gazes yearningly"},
    "सोनहिं": {"roman": "sonahin", "hi": "कंचन/शुद्ध स्वर्ण में", "en": "in pure gold"},
    "समानी": {"roman": "samaanee", "hi": "समा गई/व्याप्त हुई", "en": "permeated within"},
    "बाती": {"roman": "baatee", "hi": "दीप की वर्तिका/बाती", "en": "lamp-wick"},
    "बरै": {"roman": "barai", "hi": "प्रज्वलित होती है/जलती है", "en": "burns/radiates light"},
    "मोरा": {"roman": "moraa", "hi": "मयूर/मोर", "en": "dancing peacock"},
    "चकोरा": {"roman": "chakoraa", "hi": "चकोर पक्षी", "en": "partridge bird"},
    "सुहागा": {"roman": "suhaagaa", "hi": "स्वर्ण-शोधक सुहागा", "en": "borax flux"},
}

for k, v in ENHANCEMENTS.items():
    lex[k] = v

json.dump(lex, open(LEX_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("Updated enhancements in ravidas_lexicon.json")
