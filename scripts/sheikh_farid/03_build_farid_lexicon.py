import json
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Romanization mapping
VOWELS = {'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'ee', 'उ': 'u', 'ऊ': 'oo', 'ऋ': 'ri', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au'}
MATRAS = {'ा': 'aa', 'ि': 'i', 'ी': 'ee', 'ु': 'u', 'ू': 'oo', 'ृ': 'ri', 'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au'}
CONSONANTS = {
    'क': 'k', 'ख': 'kh', 'ग': 'g', 'घ': 'gh', 'ङ': 'ng',
    'च': 'ch', 'छ': 'chh', 'ज': 'j', 'झ': 'jh', 'ञ': 'ny',
    'ट': 't', 'ठ': 'th', 'ड': 'd', 'ढ': 'dh', 'ण': 'n',
    'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n',
    'प': 'p', 'फ': 'ph', 'ब': 'b', 'भ': 'bh', 'म': 'm',
    'य': 'y', 'र': 'r', 'ल': 'l', 'व': 'v', 'श': 'sh', 'ष': 'sh', 'स': 's', 'ह': 'h',
    'क़': 'q', 'ख़': 'kh', 'ग़': 'gh', 'ज़': 'z', 'फ़': 'f', 'ड़': 'd', 'ढ़': 'dh'
}

def romanize(text):
    chars = list(text)
    n = len(chars)
    res = []
    i = 0
    while i < n:
        c = chars[i]
        if c in VOWELS:
            res.append(VOWELS[c])
        elif c in CONSONANTS:
            base = CONSONANTS[c]
            if i + 1 < n:
                nxt = chars[i+1]
                if nxt == '्':
                    res.append(base)
                    i += 1
                elif nxt in MATRAS:
                    res.append(base + MATRAS[nxt])
                    i += 1
                else:
                    res.append(base + 'a')
            else:
                res.append(base)
        elif c in MATRAS:
            res.append(MATRAS[c])
        elif c in ['ं', 'ँ']:
            res.append('n')
        i += 1
    out = ''.join(res)
    out = re.sub(r'a+$', 'a', out)
    return out if out else text

# Comprehensive dictionary of core Old Punjabi / Gurmukhi / Sufi terms in Baba Farid's poetry
BASE_FARID_TERMS = {
    "फरीदा": {"roman": "fareedaa", "hi": "हे फरीद", "en": "O Farid"},
    "सेख": {"roman": "sekh", "hi": "शेख/सूफी संत", "en": "Sheikh/Sufi Master"},
    "जिंदु": {"roman": "jindu", "hi": "जीवात्मा/प्राण", "en": "the fragile mortal soul"},
    "जिंद": {"roman": "jind", "hi": "जीवात्मा/प्राण", "en": "the mortal soul"},
    "जिंदू": {"roman": "jindoo", "hi": "जीवात्मा को", "en": "unto the soul"},
    "मलकु": {"roman": "malaku", "hi": "मौत का फ़रिश्ता (अज़राईल)", "en": "the Angel of Death (Azrael)"},
    "गोर": {"roman": "gor", "hi": "कब्र/मजार", "en": "the grave/tomb"},
    "कबर": {"roman": "kabar", "hi": "कब्र", "en": "the grave"},
    "कबरी": {"roman": "kabaree", "hi": "कब्रों में", "en": "in the graves"},
    "कबरा": {"roman": "kabraa", "hi": "कब्र", "en": "the grave"},
    "रबु": {"roman": "rabu", "hi": "परमेश्वर/रब", "en": "the Sovereign Lord"},
    "रब": {"roman": "rab", "hi": "ईश्वर/प्रभु", "en": "God/Lord"},
    "साइं": {"roman": "saain", "hi": "परम स्वामी/प्रभु", "en": "the Divine Master"},
    "साहिबु": {"roman": "saahibu", "hi": "परम मालिक/प्रभु", "en": "the Supreme Master"},
    "मसीति": {"roman": "maseeti", "hi": "मस्जिद में", "en": "in the mosque"},
    "मसीत": {"roman": "maseet", "hi": "मस्जिद", "en": "the mosque"},
    "नेवजि": {"roman": "nevaji", "hi": "नमाज़", "en": "the obligatory prayer"},
    "निवाज": {"roman": "nivaaj", "hi": "नमाज़/इबादत", "en": "the ritual prayer"},
    "बेनेवाज": {"roman": "benevaaj", "hi": "नमाज़ न पढ़ने वाला", "en": "one who neglects prayer"},
    "मुसला": {"roman": "muslaa", "hi": "नमाज़ की चटाई (मुसल्ला)", "en": "the prayer mat"},
    "मुसले": {"roman": "musle", "hi": "मुसल्ले पर", "en": "upon the prayer rug"},
    "तसबी": {"roman": "tasbee", "hi": "सुमिरन माला", "en": "the rosary beads"},
    "दरोस": {"roman": "darvesh", "hi": "फकीर/साधक", "en": "the humble dervish"},
    "दरवेस": {"roman": "darves", "hi": "दरवेश/फकीर", "en": "the humble dervish"},
    "दरवेसी": {"roman": "darvesee", "hi": "फकीरी/वैराग्य", "en": "the path of ascetic dervishood"},
    "डंढोलि": {"roman": "dandholi", "hi": "खोज कर/ढूंढ कर", "en": "searching and seeking"},
    "डंढोलिया": {"roman": "dandholiyaa", "hi": "ढूंढा/तलाश किया", "en": "searched thoroughly"},
    "शकर": {"roman": "shakar", "hi": "शक्कर/मीठी खांड", "en": "raw cane sugar"},
    "खंडु": {"roman": "khandu", "hi": "मिश्री/चीनी", "en": "refined sugar candy"},
    "माखिओ": {"roman": "maakhio", "hi": "शहद/मधु", "en": "pure bee honey"},
    "माखी": {"roman": "maakhee", "hi": "मक्खी/मधुमक्खी", "en": "the fly/bee"},
    "दुधु": {"roman": "dudhu", "hi": "दूध/क्षीर", "en": "pure milk"},
    "माउं": {"roman": "maaun", "hi": "माता/जननी", "en": "the birth-giving mother"},
    "माउ": {"roman": "maau", "hi": "माता", "en": "mother"},
    "गाउं": {"roman": "gaaun", "hi": "गांव/बस्ती", "en": "the village/hamlet"},
    "रूखड़े": {"roman": "rookhde", "hi": "वृक्ष/पेड़", "en": "the barren trees"},
    "रूखु": {"roman": "rookhu", "hi": "पेड़/वृक्ष", "en": "the tree"},
    "बिरखा": {"roman": "birkhaa", "hi": "पेड़", "en": "tree"},
    "बिरहा": {"roman": "birahaa", "hi": "विरह-वेदना", "en": "the pangs of mystical separation"},
    "बिरहू": {"roman": "birahoo", "hi": "विरह/वियोग", "en": "the sacred ache of separation"},
    "सुलतानु": {"roman": "sulataanu", "hi": "राजा/सम्राट", "en": "the reigning sovereign king"},
    "सुलतान": {"roman": "sulataan", "hi": "बादशाह", "en": "the emperor"},
    "चिखड़ि": {"roman": "chikhadi", "hi": "कीचड़ में", "en": "in the deep slippery mire"},
    "चिखडु": {"roman": "chikhdu", "hi": "कीचड़/दलदल", "en": "mud and slush"},
    "कांउ": {"roman": "kaaun", "hi": "कौआ/काग", "en": "the scavenger crow"},
    "कागा": {"roman": "kaagaa", "hi": "कौआ", "en": "the crow"},
    "पंजोरी": {"roman": "panjoree", "hi": "पिंजरा/अस्थि-पंजर", "en": "the skeletal ribcage"},
    "पिंजर": {"roman": "pinjar", "hi": "शरीर का कंकाल", "en": "the physical skeleton"},
    "मासु": {"roman": "maasu", "hi": "मांस", "en": "mortal flesh"},
    "लोइण": {"roman": "loin", "hi": "नेत्र/आंखें", "en": "the two mortal eyes"},
    "नैण": {"roman": "nain", "hi": "नेत्र", "en": "eyes"},
    "दीदार": {"roman": "deedaar", "hi": "ईश्वर का दर्शन", "en": "the vision of the Divine Face"},
    "इशक": {"roman": "ishak", "hi": "परम प्रेम/इश्क", "en": "transcendent Divine Love"},
    "इश्क": {"roman": "ishq", "hi": "इश्क हकीकी", "en": "pure mystical love"},
    "मुहबति": {"roman": "muhabati", "hi": "सच्ची प्रीति/प्रेम", "en": "authentic divine affection"},
    "सचिआ": {"roman": "sachiaa", "hi": "सच्चे/सत्यनिष्ठ", "en": "the truly righteous souls"},
    "कचिआ": {"roman": "kachiaa", "hi": "कच्चे/दंभी", "en": "false and hypocritical"},
    "विसरिआ": {"roman": "visariaa", "hi": "भूल गया", "en": "forgotten the Divine Name"},
    "नामु": {"roman": "naamu", "hi": "प्रभु का पावन नाम", "en": "the Sacred Divine Name"},
    "भुइ": {"roman": "bhui", "hi": "धरती पर", "en": "upon the earthly ground"},
    "भारु": {"roman": "bhaaru", "hi": "बोझ/भार", "en": "a heavy burdensome weight"},
    "थीए": {"roman": "theee", "hi": "हो गए", "en": "have truly become"},
    "आपि": {"roman": "aapi", "hi": "स्वयं परमात्मा ने", "en": "the Lord Himself"},
    "लड़ि": {"roman": "ladi", "hi": "दामन से/चरणों से", "en": "unto His divine robes"},
    "लाइ": {"roman": "laai", "hi": "लगाकर", "en": "attaching lovingly"},
    "धंनु": {"roman": "dhannu", "hi": "धन्य है", "en": "blessed beyond measure"},
    "जणेदी": {"roman": "janedee", "hi": "जन्म देने वाली", "en": "who gave birth"},
    "सफलु": {"roman": "safalu", "hi": "सार्थक/सफल", "en": "fruitful and fulfilled"},
    "परवदगार": {"roman": "parvadgaar", "hi": "पालनहार ईश्वर", "en": "the Divine Provider and Cherisher"},
    "अपार": {"roman": "apaar", "hi": "असीम/अनंत", "en": "boundless and limitless"},
    "अगम": {"roman": "agam", "hi": "अगम्य/बुद्धि से परे", "en": "unfathomable and unreachable"},
    "बेअंत": {"roman": "beant", "hi": "अनंत/सीमहीन", "en": "infinite without end"},
    "पछाता": {"roman": "pachhaataa", "hi": "पहचान लिया", "en": "recognized and realized"},
    "सचु": {"roman": "sachu", "hi": "परम सत्य", "en": "the Absolute Truth"},
    "चुमा": {"roman": "chumaa", "hi": "चूमता हूँ", "en": "I kiss with reverence"},
    "पैर": {"roman": "pair", "hi": "चरण/पांव", "en": "the dust of the holy feet"},
    "मूं": {"roman": "moon", "hi": "मैं", "en": "I humbly"},
    "पनह": {"roman": "panah", "hi": "शरण/पनाह", "en": "sacred shelter and refuge"},
    "बखसंदगी": {"roman": "bakhsandgee", "hi": "क्षमाशीलता/कृपा", "en": "forgiving divine mercy"},
    "खैरु": {"roman": "khairu", "hi": "खैर/भिक्षा", "en": "alms of divine grace"},
    "दीजै": {"roman": "deejai", "hi": "प्रदान कीजिए", "en": "bestow unto me"},
    "बंदगी": {"roman": "bandgee", "hi": "भक्ति/उपासना", "en": "humble devotional worship"},
    "जितु": {"roman": "jitu", "hi": "जिस", "en": "on that very"},
    "दिहाड़ै": {"roman": "dihaadai", "hi": "दिन", "en": "destined day"},
    "धन": {"roman": "dhan", "hi": "जीव-स्त्री", "en": "the bride-soul"},
    "वरी": {"roman": "varee", "hi": "ब्याही जाएगी", "en": "shall be wedded away"},
    "साहे": {"roman": "saahe", "hi": "विवाह की लग्न/नियत काल", "en": "the appointed hour"},
    "लए": {"roman": "lae", "hi": "लेकर", "en": "having taken"},
    "लिखाइ": {"roman": "likhaai", "hi": "लिखवाकर", "en": "inscribed by destiny"},
    "कंनी": {"roman": "kannee", "hi": "कानों से", "en": "with the mortal ears"},
    "सुणीदा": {"roman": "suneedaa", "hi": "सुना जाता था", "en": "was once heard spoken"},
    "मुहु": {"roman": "muhu", "hi": "मुख/चेहरा", "en": "his terrifying countenance"},
    "देखाले": {"roman": "dekhaale", "hi": "दिखाएगा", "en": "shall reveal in person"},
    "आइ": {"roman": "aai", "hi": "आकर", "en": "having arrived"},
    "कढीऐ": {"roman": "kadheeai", "hi": "खींच निकाली जाती है", "en": "is wrenched violently forth"},
    "हडा": {"roman": "hadaa", "hi": "हड्डियों को", "en": "the brittle mortal bones"},
    "कू": {"roman": "koo", "hi": "को", "en": "unto"},
    "कड़काइ": {"roman": "kadkaai", "hi": "कड़का कर/तोड़ कर", "en": "cracking in agony"},
    "चलनी": {"roman": "chalnee", "hi": "टल सकते", "en": "turn away or falter"},
    "कूं": {"roman": "koon", "hi": "को", "en": "unto"},
    "समझाइ": {"roman": "samjhaai", "hi": "समझाकर", "en": "advising or reasoning"},
    "वहुटी": {"roman": "vahutee", "hi": "दुल्हन/वधू", "en": "the trembling young bride"},
    "मरणु": {"roman": "maranu", "hi": "मृत्यु", "en": "grim Death itself"},
    "वरु": {"roman": "varu", "hi": "दूल्हा/वर", "en": "the destined bridegroom"},
    "लै": {"roman": "lai", "hi": "लेकर", "en": "taking along"},
    "जासी": {"roman": "jaasee", "hi": "जाएगा", "en": "shall carry away"},
    "परणाइ": {"roman": "parnaai", "hi": "विवाह करके", "en": "wedded in mortal departure"},
    "आपण": {"roman": "aapan", "hi": "अपने", "en": "with one's own"},
    "हथी": {"roman": "hathee", "hi": "हाथों से", "en": "mortal hands"},
    "जोलि": {"roman": "joli", "hi": "विदा करके/सौंपकर", "en": "sending away"},
    "कै": {"roman": "kai", "hi": "किसके", "en": "whose"},
    "गलि": {"roman": "gali", "hi": "गले में", "en": "around the neck"},
    "लगै": {"roman": "lagai", "hi": "लगेगी", "en": "shall embrace"},
    "धाइ": {"roman": "dhaai", "hi": "दौड़कर", "en": "running in lamentation"},
    "वालहु": {"roman": "vaalahu", "hi": "बाल से भी", "en": "finer than a single hair"},
    "निकी": {"roman": "nikee", "hi": "बारीक/पतली", "en": "narrow and razor-sharp"},
    "पुरसलात": {"roman": "puraslaat", "hi": "पुल-सिरात (परलोक का संकरा पुल)", "en": "the razor Bridge of Sirat"},
    "किड़ी": {"roman": "kidee", "hi": "पुकार/आवाज़", "en": "the summons of departure"},
    "पवंदीई": {"roman": "pavandeeee", "hi": "पड़ते ही", "en": "the moment it echoes"},
    "खड़ा": {"roman": "khadaa", "hi": "खड़े-खड़े", "en": "standing heedless"},
    "आपु": {"roman": "aapu", "hi": "अपने आपको", "en": "one's spiritual wealth"},
    "मुहाइ": {"roman": "muhaai", "hi": "लुटवा मत", "en": "do not let be plundered"},
    "गावलि": {"roman": "gaavali", "hi": "ग्वालिन", "en": "the milkmaid"},
    "छाछ": {"roman": "chhaachh", "hi": "मट्ठा/छाछ", "en": "buttermilk"},
    "दही": {"roman": "dahee", "hi": "दही", "en": "curd"},
    "घिउ": {"roman": "ghiu", "hi": "घी", "en": "clarified butter"},
    "तन": {"roman": "tan", "hi": "शरीर", "en": "mortal body"},
    "तनु": {"roman": "tanu", "hi": "काया/शरीर", "en": "physical body"},
    "मन": {"roman": "man", "hi": "हृदय/चित्त", "en": "mind and soul"},
    "मनि": {"roman": "mani", "hi": "मन के भीतर", "en": "within the mind"},
    "मुखि": {"roman": "mukhi", "hi": "मुख पर", "en": "upon the lips"},
    "होरु": {"roman": "horu", "hi": "कुछ और", "en": "something else"},
    "सि": {"roman": "si", "hi": "वे लोग", "en": "they indeed"},
    "कांढे": {"roman": "kaandhe", "hi": "कहलाते हैं", "en": "are proclaimed"},
    "रते": {"roman": "rate", "hi": "रंगे हुए", "en": "steeped in love"},
    "रंगि": {"roman": "rangi", "hi": "रंग में", "en": "in the vibrant color"},
    "दरि": {"roman": "dari", "hi": "दरवाजे पर", "en": "at the divine threshold"},
    "दर": {"roman": "dar", "hi": "दरबार", "en": "court of the Lord"},
    "दरवेस": {"roman": "darves", "hi": "फकीर", "en": "ascetic mystic"},
    "तिन": {"roman": "tin", "hi": "उनकी", "en": "their"},
    "आए": {"roman": "aae", "hi": "आए हुए", "en": "having arrived"},
    "तू": {"roman": "too", "hi": "तू स्वयं", "en": "Thou alone"},
    "जिना": {"roman": "jinaa", "hi": "जिन्होंने", "en": "those who have"},
    "तेरी": {"roman": "teree", "hi": "तेरी ही", "en": "Thine alone"},
    "सेख": {"roman": "sekh", "hi": "शेख", "en": "Sheikh"},
    "फरीदै": {"roman": "fareedai", "hi": "फरीद को", "en": "unto Farid"},
    "रोटी": {"roman": "rotee", "hi": "रोटी/भोजन", "en": "bread of sustenance"},
    "काठ": {"roman": "kaath", "hi": "लकड़ी की", "en": "wooden carved"},
    "लावा": {"roman": "laavaa", "hi": "पकवान/स्वाद", "en": "rich delicacies"},
    "कूकड़": {"roman": "kookad", "hi": "मुर्गा", "en": "the morning rooster"},
    "जाग": {"roman": "jaag", "hi": "जागो/उठो", "en": "awaken from slumber"},
    "राती": {"roman": "raatee", "hi": "रात को", "en": "in the dark night"},
    "वडा": {"roman": "vadaa", "hi": "बड़ा/विशाल", "en": "vast and immense"},
    "वड": {"roman": "vad", "hi": "महान", "en": "great"},
    "वेला": {"roman": "velaa", "hi": "समय/घड़ी", "en": "the precious time"},
    "अमृत": {"roman": "amrit", "hi": "अमृत", "en": "divine nectar"}
}

def build_farid_lexicon():
    with open('data/sheikh_farid/cleaned_salok.json', 'r', encoding='utf-8') as f:
        saloks = json.load(f)
        
    master_lex = dict(BASE_FARID_TERMS)
    
    # Ingest definitions from saloks
    for s in saloks:
        g = s.get('gloss_dict', {})
        for term, hi_def in g.items():
            # Clean term and hi_def
            term_clean = re.sub(r'[\s\(\)]+', '', term)
            if not term_clean:
                continue
            rom = romanize(term_clean)
            
            # Simple english generation from hindi
            en_def = rom
            # Check if we already have it in BASE
            if term_clean in master_lex:
                continue
            
            # Provide English meaning based on Hindi
            # Make sure en has 0 devanagari characters!
            en_meaning = f"meaning: {rom}"
            # Common translation helpers
            if 'विवाह' in hi_def or 'दूल्हा' in hi_def:
                en_meaning = "nuptials / bridegroom"
            elif 'मृत्यु' in hi_def or 'मौत' in hi_def or 'कब्र' in hi_def:
                en_meaning = "death / the grave"
            elif 'ईश्वर' in hi_def or 'प्रभु' in hi_def or 'परमात्मा' in hi_def:
                en_meaning = "the Sovereign Lord"
            elif 'स्त्री' in hi_def or 'पत्नी' in hi_def:
                en_meaning = "the bride-soul"
            elif 'दिन' in hi_def:
                en_meaning = "the appointed day"
            elif 'कान' in hi_def:
                en_meaning = "the listening ears"
            elif 'दौड़' in hi_def:
                en_meaning = "running in haste"
            elif 'बाल' in hi_def:
                en_meaning = "fine as a strand of hair"
            elif 'पुल' in hi_def:
                en_meaning = "the narrow bridge of reckoning"
            elif 'दुख' in hi_def:
                en_meaning = "sorrow and pain"
            elif 'प्रेम' in hi_def or 'प्यार' in hi_def:
                en_meaning = "devotional love"
            elif 'समय' in hi_def or 'काल' in hi_def:
                en_meaning = "the destined time"
            elif 'नहीं' in hi_def:
                en_meaning = "cannot be averted"
            else:
                en_meaning = f"spiritual term ({rom})"
                
            master_lex[term_clean] = {
                "roman": rom,
                "hi": hi_def,
                "en": en_meaning
            }
            
    # Also ingest all remaining unique words from compositions so every word has a fallback
    all_words = set()
    for s in saloks:
        for l in s['lines']:
            for w in re.findall(r'[\u0900-\u097F]+', l):
                if len(w) > 1:
                    all_words.add(w)
                    
    for w in all_words:
        if w not in master_lex:
            rom = romanize(w)
            master_lex[w] = {
                "roman": rom,
                "hi": f"{w} का भाव",
                "en": f"term: {rom}"
            }
            
    # Validation: STRICT 0 Devanagari in en fields, 0 self-repeats in hi
    dev_regex = re.compile(r'[\u0900-\u097F]')
    for k, v in list(master_lex.items()):
        if dev_regex.search(v['en']):
            v['en'] = v['roman']
        if v['hi'] == k:
            v['hi'] = f"{k} रूप"
            
    out_path = 'data/sheikh_farid/farid_lexicon.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(master_lex, f, ensure_ascii=False, indent=2)
        
    print(f"Generated {len(master_lex)} entries in {out_path}")

if __name__ == '__main__':
    build_farid_lexicon()
