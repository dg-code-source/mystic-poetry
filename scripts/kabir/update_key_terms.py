import json
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/kabir/kabir_lexicon.json', 'r', encoding='utf-8') as f:
    merged_lex = json.load(f)

additional_terms = {
    "अलह": {"hi": "अल्लाह, परमेश्वर, एक परमात्मा", "en": "Allah, the One Supreme Divine"},
    "नूरु": {"hi": "दिव्य प्रकाश, ब्रह्म-ज्योति", "en": "Divine Light, primordial radiance"},
    "उपाइआ": {"hi": "उत्पन्न किया, सृजन किया", "en": "created, manifested into being"},
    "धीरे": {"hi": "धैर्यपूर्वक, सहज रूप से", "en": "patiently, gently in due season"},
    "मना": {"hi": "हे मन, अंतःकरण", "en": "O inner mind, O seeker within"},
    "होय": {"hi": "होता है, संभव होता है", "en": "comes to pass, happens naturally"},
    "माली": {"hi": "बगीचे की देखभाल करने वाला, साधक", "en": "gardener, tender of the soul"},
    "सींचे": {"hi": "जल देना, साधना से सींचना", "en": "waters, nourishes with effort"},
    "घड़ा": {"hi": "कलश, जलपात्र", "en": "pitcher of water, vessel"},
    "ॠतु": {"hi": "उचित समय, वसंत आदि काल", "en": "appointed season, right time"},
    "फल": {"hi": "परिणाम, आत्मिक सिद्धि", "en": "fruit, divine realization"},
    "आपा": {"hi": "अहंकार, स्व-भाव", "en": "egotism, individual vanity"},
    "बोलीए": {"hi": "उच्चारण करना, प्रेम से बोलना", "en": "speak with sweet humility"},
    "औरन": {"hi": "दूसरों को, जग को", "en": "unto others, all people"},
    "अन्तर्यामी": {"hi": "घट-घट वासी, सर्वज्ञाता", "en": "Indwelling Divine, Knower of hearts"},
    "आधार": {"hi": "आश्रय, सहारा", "en": "foundation, supreme support"},
    "पार": {"hi": "भवसागर से पार, मुक्ति", "en": "across the ocean of rebirth, ultimate liberation"},
    "गाफिला": {"hi": "बेखबर, असावधान", "en": "heedless one, unaware sleeper"},
    "पहचान": {"hi": "ज्ञान, आत्म-बोध", "en": "realize, discover your divine self"},
    "सिंहासन": {"hi": "राजगद्दी, प्रभु का तख्त", "en": "throne of honor, elevated station"},
    "जंजीर": {"hi": "बंधन, कर्म-पाश", "en": "chains of karmic bondage"},
    "शीतल": {"hi": "शांत, तृप्त", "en": "cool, soothing and peaceful"},
    "चकोर": {"hi": "चंद्रमा का प्रेमी पक्षी, अनन्य प्रेमी", "en": "Chakor bird, devoted lover of the moon"},
    "अंगार": {"hi": "धधकता कोयला, विरह की ज्वाला", "en": "burning ember, fire of love"},
    "कुम्हार": {"hi": "माटी गढ़ने वाला, परम विधाता", "en": "potter, Divine Creator"},
    "रौंदे": {"hi": "पैरों से कुचलना, विवश करना", "en": "trample upon, mold with force"},
    "मनका": {"hi": "माला का दाना, हृदय", "en": "rosary bead, inner heart"},
    "डार": {"hi": "छोड़ देना, त्यागना", "en": "discard, cast away"},
    "सूप": {"hi": "सूपड़ा, सार छांटने वाला", "en": "winnowing fan, discriminator of truth"},
    "सुभाय": {"hi": "स्वभाव, निर्मल आचरण", "en": "nature, intrinsic virtue"},
    "थोथ": {"hi": "सारहीन भूसा, व्यर्थ आडंबर", "en": "empty chaff, superficial husks"},
    "गहि": {"hi": "ग्रहण करना, धारण करना", "en": "grasp, retain with reverence"},
    "उड़ाय": {"hi": "उड़ा देना, दूर करना", "en": "blow away, discard as worthless"},
    "दुर्बल": {"hi": "कमजोर, निर्बल प्राणी", "en": "weak, vulnerable soul"},
    "हाय": {"hi": "आह, अंतस की पुकार", "en": "lament, silent curse of the oppressed"},
    "भस्म": {"hi": "राख, विलीन", "en": "ashes, burnt to cinder"},
    "लोह": {"hi": "लोहा, कठोर पाषाण", "en": "iron, hardest metal"}
}

for k, v in additional_terms.items():
    merged_lex[k] = v

with open('data/kabir/kabir_lexicon.json', 'w', encoding='utf-8') as f:
    json.dump(merged_lex, f, ensure_ascii=False, indent=2)

print(f"Updated kabir_lexicon.json with additional key terms. Total: {len(merged_lex)}")
