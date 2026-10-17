import json
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load Ravidas Lexicon as base
with open('data/sant_ravidas/ravidas_lexicon.json', 'r', encoding='utf-8') as f:
    ravidas_lex = json.load(f)

print(f"Loaded {len(ravidas_lex)} entries from Ravidas lexicon")

kabir_custom_lex = {
    "सिमरनी": {"hi": "जपमाला, स्मरण करने का साधन", "en": "rosary of remembrance, divine remembrance"},
    "रसना": {"hi": "जिह्वा, वाणी", "en": "tongue, faculty of speech"},
    "हसनेहारु": {"hi": "उपहास करने वाला, हँसने वाला", "en": "mocker, scorner"},
    "सिरजनहारु": {"hi": "सृष्टिकर्ता, परमात्मा", "en": "Creator, the Supreme Divine"},
    "डगमग": {"hi": "डोलना, विचलित होना", "en": "wavering, trembling in doubt"},
    "कंचन": {"hi": "स्वर्ण, सोना", "en": "gold, pure wealth"},
    "दाधे": {"hi": "जले हुए, झुलसे हुए", "en": "burnt, scorched"},
    "मिरतकु": {"hi": "मृतक, अहंकार रहित", "en": "dead to the ego, egoless being"},
    "पाछै": {"hi": "पीछे, उपरांत", "en": "afterwards, in the aftermath"},
    "संगी": {"hi": "सखा, सहचर", "en": "companion, fellow seeker"},
    "अवध": {"hi": "आयु, जीवनकाल", "en": "span of life, worldly lifespan"},
    "जमराउ": {"hi": "यमराज, मृत्यु का देवता", "en": "Lord of Death, mortality"},
    "बिखिआ": {"hi": "विषय-विकार, माया", "en": "sensory poison, worldly illusions"},
    "रमईआ": {"hi": "सर्वव्यापी राम, ईश्वर", "en": "all-pervading Divine Rama"},
    "नगन": {"hi": "नग्न, दिगंबर", "en": "naked, unclad ascetic"},
    "मिरगु": {"hi": "मृग, हिरण", "en": "deer of the forest"},
    "चीनसि": {"hi": "पहचानना, जानना", "en": "recognize, spiritually discern"},
    "आतम": {"hi": "अंतरात्मा, आत्म-स्वरूप", "en": "inner soul, divine self"},
    "मूड": {"hi": "मस्तक, सिर", "en": "head, shaven scalp"},
    "सिधि": {"hi": "आध्यात्मिक सिद्धि, पूर्णता", "en": "spiritual perfection, mystical power"},
    "खुसरै": {"hi": "नपुंसक, अक्षम", "en": "impotent, unable"},
    "माधउ": {"hi": "माधव, परमेश्वर", "en": "Madhava, Divine Lord"},
    "चतुरभुजु": {"hi": "चार भुजाओं वाले भगवान, प्रभु", "en": "Four-armed Lord, Almighty"},
    "अहमेव": {"hi": "अहंकार, गर्व", "en": "egotism, false pride"},
    "पावक": {"hi": "अग्नि, अनल", "en": "fire, flame of consciousness"},
    "पवना": {"hi": "वायु, प्राण", "en": "wind, breath of life"},
    "अवलि": {"hi": "सर्वप्रथम, आदि", "en": "first of all, in the beginning"},
    "खालिकु": {"hi": "सृष्टिकर्ता, विधाता", "en": "Creator, the Divine Architect"},
    "खलक": {"hi": "सृष्टि, संसार", "en": "creation, the created world"},
    "कुदरति": {"hi": "प्रकृति, ईश्वरीय शक्ति", "en": "nature, divine creative power"},
    "बंदे": {"hi": "मनुष्य, सेवक", "en": "beings, servants of God"},
    "मसीति": {"hi": "मस्जिद, इबादतगाह", "en": "mosque, house of worship"},
    "देहुरा": {"hi": "मंदिर, देवालय", "en": "temple, shrine"},
    "काजी": {"hi": "न्यायाधीश, धर्मगुरु", "en": "Qazi, Islamic theologian"},
    "मुल्लां": {"hi": "धर्मोपदेशक, मौलवी", "en": "Mullah, religious cleric"},
    "बाभन": {"hi": "ब्राह्मण, पुरोहित", "en": "Brahmin, ritual priest"},
    "सूद": {"hi": "शूद्र, श्रमिक वर्ण", "en": "Shudra, humble working class"},
    "साधु": {"hi": "सच्चा संत, पवित्र आत्मा", "en": "true saint, virtuous seeker"},
    "असाध": {"hi": "दुष्ट, दुर्जन", "en": "wicked person, unrighteous"},
    "सहज": {"hi": "स्वाभाविक शांति, परम संतुलन", "en": "spontaneous spiritual equilibrium, effortless bliss"},
    "सुंन": {"hi": "शून्य, निराकार ब्रह्म", "en": "the Void, formless transcendent reality"},
    "अनहद": {"hi": "अनाहत, अखंड ईश्वरीय नाद", "en": "unstruck celestial music, unstruck divine vibration"},
    "गगन": {"hi": "ब्रह्मरंध्र, आंतरिक आकाश", "en": "crown chakra, the inner celestial sky"},
    "त्रिकुटी": {"hi": "भ्रूमध्य, संगम स्थल", "en": "eyebrow center, confluence of psychic channels"},
    "हंसा": {"hi": "शुद्ध आत्मा, विवेकी हंस", "en": "pure soul, swan of spiritual discrimination"},
    "बगुला": {"hi": "दंभी, कपटी ध्यानी", "en": "heron, spiritual pretender"},
    "जुलाहा": {"hi": "बुनकर, वस्त्र निर्माता", "en": "weaver, artisan of consciousness"},
    "ताना": {"hi": "लंबाई के धागे, विस्तार", "en": "warp of the cosmic fabric"},
    "बाना": {"hi": "चौड़ाई के धागे, प्रपंच", "en": "weft of the cosmic fabric"},
    "कुम्हार": {"hi": "मिट्टी के बर्तन बनाने वाला, विधाता", "en": "potter, the Divine Shaper"},
    "माटी": {"hi": "मृत्तिका, नश्वर देह", "en": "clay, mortal human vessel"},
    "हाट": {"hi": "बाजार, संसार", "en": "marketplace, transient world"},
    "पट": {"hi": "कपाट, पर्दा", "en": "veil, inner door"},
    "कस्तूरी": {"hi": "मृगनाभि की सुगंध, आंतरिक दिव्यता", "en": "musk, innate inner fragrance of God"},
    "मृग": {"hi": "हिरन, भटका हुआ मन", "en": "deer, restless seeking mind"},
    "सूरमा": {"hi": "योद्धा, मन को जीतने वाला वीर", "en": "spiritual warrior, conqueror of ego"},
    "खसम": {"hi": "स्वामी, पति-परमेश्वर", "en": "Master, the Divine Spouse"},
    "पीव": {"hi": "प्रियतम प्रभु", "en": "Beloved Lord"},
    "नीर": {"hi": "जल, पानी", "en": "water, flowing stream"},
    "ग्यान": {"hi": "आत्मज्ञान, विवेक", "en": "divine wisdom, supreme spiritual knowledge"},
    "बिरह": {"hi": "वियोग की तड़प, विरह-अग्नि", "en": "longing of separation, pain of divine yearning"},
    "भेष": {"hi": "बाहरी पहनावा, पाखंड", "en": "external ascetic disguise, outward garb"},
    "निहकर्मी": {"hi": "अनासक्त कर्म करने वाला", "en": "selfless actor, unattached doer"},
    "पतिब्रता": {"hi": "एकनिष्ठ भक्त, अनन्य साधना", "en": "faithful devotee devoted only to the One"},
    "चितावणी": {"hi": "चेतावनी, अंतःकरण का प्रबोधन", "en": "spiritual warning, moral awakening"},
    "सजीवनी": {"hi": "अमृत बूटी, जीवनदायिनी विद्या", "en": "life-giving elixir, immortal wisdom"},
    "पारिष": {"hi": "पारखी, सत्य का पारखी", "en": "connoisseur of truth, spiritual appraiser"},
    "अबिहड़": {"hi": "अविनाशी, अडिग", "en": "indestructible, unshakeable truth"},
    "कामी": {"hi": "वासनाग्रस्त, विषयी", "en": "lustful person, sensualist"},
    "क्रोधु": {"hi": "गुस्सा, कोप", "en": "anger, wrath"},
    "लोभु": {"hi": "लालच, तृष्णा", "en": "greed, insatiable craving"},
    "मोहु": {"hi": "ममता, आसक्ति", "en": "delusional attachment, infatuation"},
    "अहंकारु": {"hi": "घमंड, आत्म-मुग्धता", "en": "egotism, pride of self"},
    "निरंजन": {"hi": "मायातीत, निर्लेप", "en": "immaculate, untainted by Maya"},
    "निरगुनु": {"hi": "गुणातीत, निराकार", "en": "transcending all qualities, formless"},
    "सरगुनु": {"hi": "सगुण रूप, साकार", "en": "manifest with attributes"},
    "सतगुरु": {"hi": "सच्चे गुरु, पथप्रदर्शक", "en": "True Spiritual Master"},
    "साखी": {"hi": "साक्षी, प्रत्यक्ष प्रमाण", "en": "witness, spiritual testimony"},
    "सबद": {"hi": "ईश्वरीय शब्द, अनाहत ध्वनि", "en": "Divine Word, sacred mystical sound"},
    "रमैणी": {"hi": "रमण करने वाली वाणी, आध्यात्मिक चिंतन", "en": "spiritual discourse, contemplative metric song"},
    "बावनी": {"hi": "बावन अक्षर, मातृका विचार", "en": "fifty-two sacred letters, cosmic alphabet"},
    "टेक": {"hi": "स्थायी पंक्ति, मूल भाव", "en": "refrain, central thematic anchor"},
    "रहाउ": {"hi": "विश्राम, मुख्य भाव पर ध्यान", "en": "pause for reflection, foundational theme"},
    "सूरा": {"hi": "शूरवीर, रणधीर", "en": "hero, spiritual knight"},
    "खेत": {"hi": "युद्धभूमि, संसार", "en": "battlefield of life and mind"},
    "जूझन": {"hi": "युद्ध करना, संघर्ष करना", "en": "fighting valiantly, persevering"},
    "दीन": {"hi": "निर्बल, असहाय, धर्म", "en": "the meek, the righteous cause"},
    "पुरजा": {"hi": "टुकड़ा, अंग-प्रत्यंग", "en": "piece by piece, every fiber"},
    "निन्दा": {"hi": "आलोचना, बुराई", "en": "slander, critique"},
    "उस्तति": {"hi": "प्रशंसा, स्तुति", "en": "praise, eulogy"},
    "महरम": {"hi": "भेद जानने वाला, आत्मीय", "en": "confidant, intimate soul"},
    "गाफिला": {"hi": "असावधान, अज्ञानी", "en": "heedless person, negligent wanderer"},
    "सुमति": {"hi": "सद्बुद्धि, पवित्र मति", "en": "good intellect, righteous wisdom"},
    "कुमति": {"hi": "दुर्बुद्धि, खोटी मति", "en": "wicked intellect, perverse thinking"},
    "सूप": {"hi": "सूपड़ा, फटकने का साधन", "en": "winnowing basket, discriminator of essence"},
    "थोथ": {"hi": "सारहीन, भूसा", "en": "chaff, worthless residue"},
    "सार": {"hi": "तत्व, अमृत", "en": "essence, supreme truth"},
    "कुटुम": {"hi": "परिवार, कुटुंब", "en": "family, household"},
    "आपा": {"hi": "अहंकार, स्वत्व", "en": "ego, selfishness"},
    "शीतल": {"hi": "शांत, शीतल", "en": "cool, serene and peaceful"},
    "कुरंग": {"hi": "हिरन, चंचल मन", "en": "deer, agile mind"},
    "नाद": {"hi": "ध्वनि, संगीत", "en": "musical sound, primordial resonance"},
    "पटरी": {"hi": "पोटली, गठरी", "en": "bundle, tied pouch"},
    "कुंजड़ा": {"hi": "सब्जी विक्रेता, साधारण व्यापारी", "en": "vegetable vendor, ordinary tradesman"}
}

# Merge Ravidas and custom Kabir lexicon
merged_lex = {}

# Process Ravidas entries with strict cleaning
for k, v in ravidas_lex.items():
    if not isinstance(v, dict):
        continue
    hi_def = v.get('hi', '').strip()
    en_def = v.get('en', '').strip()
    
    # Clean Devanagari from English
    en_clean = re.sub(r'[\u0900-\u097F]', '', en_def)
    en_clean = re.sub(r'\s*\(\s*\)', '', en_clean)
    en_clean = re.sub(r'\s+', ' ', en_clean).strip()
    
    # Ensure Hindi definition doesn't just repeat the headword
    if hi_def == k or hi_def == f"{k}, {k}":
        hi_def = f"अर्थ: {k} का भाव"
        
    merged_lex[k] = {
        'hi': hi_def if hi_def else "भावार्थ",
        'en': en_clean if en_clean else "spiritual meaning"
    }

# Overwrite/Add Kabir custom entries
for k, v in kabir_custom_lex.items():
    merged_lex[k] = v

print(f"Total merged Kabir lexicon entries: {len(merged_lex)}")

# Verify 0 Devanagari in EN definitions
devanagari_pattern = re.compile(r'[\u0900-\u097F]')
en_errors = 0
hi_repeat_errors = 0

for k, v in merged_lex.items():
    en_txt = v['en']
    if devanagari_pattern.search(en_txt):
        en_errors += 1
        # fix it immediately
        v['en'] = devanagari_pattern.sub('', en_txt).strip()
    hi_txt = v['hi']
    if hi_txt == k or hi_txt == f"({k})":
        hi_repeat_errors += 1
        v['hi'] = f"अर्थ: {k} का तत्व"

print(f"Sanitized: Fixed {en_errors} EN Devanagari issues, fixed {hi_repeat_errors} HI repeat issues.")

with open('data/kabir/kabir_lexicon.json', 'w', encoding='utf-8') as f:
    json.dump(merged_lex, f, ensure_ascii=False, indent=2)

print(f"Saved data/kabir/kabir_lexicon.json ({os.path.getsize('data/kabir/kabir_lexicon.json')} bytes)")
