import os
import json
import re
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
KAFIAN_DIR = os.path.join(DATA_DIR, "kafian")
CHECKPOINT_JSON = os.path.join(DATA_DIR, "checkpoint.json")
LEXICON_JSON = os.path.join(DATA_DIR, "punjabi_sufi_lexicon.json")

os.makedirs(KAFIAN_DIR, exist_ok=True)

batch = []

# ==========================================
# KAFI 41: 41. होरी खेलूंगी कह बिसमिलाह
# ==========================================
k41_orig = """नाम नबी की रतन चढ़ी बून्द पड़ी अल्लाह अल्लाह,
रंग रंगीली ओही खिलावे, जो सिक्खी होवे फनाफी-अल्लाह,
होरी खेलूंगी कह बिसमिलाह ।

अलसतों तों बलबिकम प्रीतम बोले, सभ सखियां ने घुंघट खोल्हे,
कालू बला ही यूं कर बोले, लाइलाह इलइला,
होरी खेलूंगी कह बिसमिलाह ।

नाहन अकरब की बंसी बजाई, मन अरफ नफसहु की कूक सुणाई,
फसुमावज्जु उल्हा की धूम मचाई, विच दरबार रसूले अल्लाह,
होरी खेलूंगी कह बिसमिलाह ।

हाथ जोड़ कर पायों पड़ूंगी, आज़िज़ हो कर बेनती करूंगी,
झगड़ा कर भर झोली लूंगी, नूर मुहंमद सल्लउलाह ।
होरी खेलूंगी कह बिसमिलाह ।

फ़ज़करूनी की होरी बनाऊं, फ़ज़करूनी पिया को रिझाऊं,
ऐसो पिया के मैं बल बल जाऊं, कैसा पिया सुबहान अल्लाह ।
होरी खेलूंगी कह बिसमिलाह ।

सिबग़तउलाहै की भर पिचकारी, अलाह उस मद्द पी मूंह पर मारी,
नूर नबी दा हक्क से जारी, नूर मुहंमद-सल्ला इल्ला,
बुल्ल्हा शाह दी धूम मची है, लाय-ला-इल इलाह ।
होरी खेलूंगी कह बिसमिलाह ।"""

k41_hi = """पैग़ंबर के नाम का अमूल्य रत्न हृदय में चमक उठा, और अल्लाह-अल्लाह की अमृत-बूँदें बरस पड़ीं!  
यह रंगों से भरी प्रेम की होली वही प्रीतम खिलाता है, जो ईश्वर में 'फ़ना' (आत्म-समर्पण) होना जानता है!  
मैं 'बिस्मिल्लाह' (अल्लाह के नाम से) कहकर होली खेलूँगी!  

सृष्टि के आदि-दिन जब प्रीतम ने पुकारा: 'क्या मैं तुम्हारा रब नहीं हूँ?' तो सब सखियों ने अपने घूँघट खोल दिए,  
और सबने एक स्वर में कहा: 'हाँ, आप ही हमारे प्रभु हैं! ला इलाहा इल्लल्लाह!'  
मैं 'बिस्मिल्लाह' कहकर होली खेलूँगी!  

उसने अपनी बांसुरी में 'हम तुम्हारी शह-रग से भी निकट हैं' की धुन बजाई,  
और 'जिसने स्वयं को पहचाना उसने रब को पहचान लिया' की मधुर पुकार सुनाई!  
रसूल के पावन दरबार में 'जिधर देखो उधर अल्लाह का ही मुख है' की धूम मच गई!  
मैं 'बिस्मिल्लाह' कहकर होली खेलूँगी!  

मैं हाथ जोड़कर उनके पावन चरणों में गिर पड़ूँगी, दीन-हीन होकर प्रार्थना करूँगी,  
और प्रेम का हठ करके नूर-ए-मुहम्मद से अपनी झोली भरवा लूँगी!  
मैं 'बिस्मिल्लाह' कहकर होली खेलूँगी!  

'तुम मेरा स्मरण करो, मैं तुम्हारा स्मरण करूँगा'—इसी प्रभु-स्मरण की होली बनाकर अपने साजन को रिझाऊँगी!  
ऐसे प्रीतम पर मैं बार-बार बलिहारी जाऊँ, कैसा विस्मयकारी प्रीतम है—सुब्हान अल्लाह!  
मैं 'बिस्मिल्लाह' कहकर होली खेलूँगी!  

अल्लाह के दिव्य रंग की पिचकारी भरकर, उस बेनियाज़ शाश्वत प्रीतम ने मेरे चेहरे पर मार दी!  
सत्य से पैग़ंबर का नूर प्रवाहित हो रहा है,  
और बुल्ले शाह के घट में 'ला इलाहा इल्लल्लाह' की अनंत धूम मच गई है!  
मैं 'बिस्मिल्लाह' कहकर होली खेलूँगी!"""

k41_en = """The Prophet's jewel shines on my breast, while drops of "Allah, Allah" descend like rain,  
This radiant Holi of ecstatic colors only He can play who dissolves in God without stain!  
Chanting Bismillah—In the Name of God—I shall play Holi today!  

When the Beloved called at time's dawn: Am I not your Lord?  
All maidens unveiled their faces and bowed before their King adored,  
Crying: Yea, Thou art our God! There is no god but Allah!  
Chanting Bismillah—In the Name of God—I shall play Holi today!  

He sounded the flute: We are nearer than the jugular vein!  
And whispered: He who knows himself knows his Master plain!  
In the Prophet's royal court resounds: Wherever ye turn, there is the Face of God!  
Chanting Bismillah—In the Name of God—I shall play Holi today!  

With folded hands I shall fall at His holy feet, a humble maid in prayer,  
With sweet, loving persistence, of His celestial light I shall claim my share—  
Filling my hem with the radiant Light of Muhammad blessed!  
Chanting Bismillah—In the Name of God—I shall play Holi today!  

Remember Me, and I shall remember you!—this is the Holi I prepare,  
Delighting my Beloved with the incense of devotion and prayer!  
A hundred times over I surrender my soul to such a King—Subhan Allah!  
Chanting Bismillah—In the Name of God—I shall play Holi today!  

Filling the syringe with the sacred dye of God's own grace,  
The Eternal, Self-Subsisting Lord splashed it upon my face!  
The pure Light of the Prophet flows from the eternal Spring of Truth,  
In Bulleh Shah's awakened soul resounds: There is no god but Allah!  
Chanting Bismillah—In the Name of God—I shall play Holi today!"""

batch.append({
    "id": 41,
    "title": "41. होरी खेलूंगी कह बिसमिलाह",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k41_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "नाम नबी की रतन चढ़ी बून्द पड़ी अल्लाह अल्लाह,",
                "hindi_gloss": "नाम (नाम) नबी (पैग़ंबर के नाम) की (का) रतन (अमूल्य रत्न) चढ़ी (आभूषण बना और) बून्द (अमृत-बूँद) पड़ी (बरस पड़ी) अल्लाह (अल्लाह) अल्लाह (अल्लाह की),",
                "english_gloss": "naam (the Name) nabee (of the Prophet) kee (of) ratan (gem) chadhee (adorned) boond (nectar drop) padee (fell) allaah (Allah) allaah (Allah),"
            },
            {
                "original": "रंग रंगीली ओही खिलावे, जो सिक्खी होवे फनाफी-अल्लाह,",
                "hindi_gloss": "रंग रंगीली (रंग-रंगीली होली) ओही (वही प्रीतम) खिलावे (खिलाता है), जो (जिसने) सिक्खी (सीखी) होवे (हो) फनाफी-अल्लाह (ईश्वर में सर्वस्व विलीन हो जाने की अवस्था),",
                "english_gloss": "rang rangeelee (vibrant colorful Holi) ohee (He alone) khilaave (plays), jo (who) sikkhee (learned) hove (has) fanafee-allaah (annihilation in God),"
            },
            {
                "original": "होरी खेलूंगी कह बिसमिलाह ।",
                "hindi_gloss": "होरी (होली) खेलूंगी (खेलूँगी) कह (कहकर) बिसमिलाह (बिस्मिल्लाह / अल्लाह के नाम से) ।",
                "english_gloss": "horee (Holi) kheloongee (I shall play) kah (saying) bismilaah ('In the Name of Allah') ."
            },
            {
                "original": "अलसतों तों बलबिकम प्रीतम बोले, सभ सखियां ने घुंघट खोल्हे,",
                "hindi_gloss": "अलसतों तों बलबिकम ('अलस्तु बिरब्बिकुम' - क्या मैं तुम्हारा रब नहीं हूँ?) प्रीतम (मेरे प्रीतम ने) बोले (कहा), सभ (समस्त) सखियां (रूहों/सखियों) ने (ने) घुंघट (अपने घूँघट) खोल्हे (खोल दिए),",
                "english_gloss": "alaston ton balbikam ('Alastu bi-rabbikum') preetam (the Beloved) bole (spoke), sabh (all) sakheeyaan (souls/maidens) ne (did) ghoonaghat (veils) kholhe (unveil),"
            },
            {
                "original": "कालू बला ही यूं कर बोले, लाइलाह इलइला,",
                "hindi_gloss": "कालू बला ('क़ालू बला' - हाँ, आप ही हमारे प्रभु हैं) ही (ही) यूं कर (इस प्रकार) बोले (पुकार उठीं), लाइलाह इलइला (ला इलाहा इल्लल्लाह / कोई ईश्वर नहीं सिवाय अल्लाह के),",
                "english_gloss": "kaaloo bala ('Qalu bala' - Yea, Thou art!) hee (indeed) yoon kar (thus) bole (chanted), laailaah il-ila (There is no god but Allah),"
            },
            {
                "original": "होरी खेलूंगी कह बिसमिलाह ।",
                "hindi_gloss": "होरी (होली) खेलूंगी (खेलूँगी) कह (कहकर) बिसमिलाह (बिस्मिल्लाह) ।",
                "english_gloss": "horee (Holi) kheloongee (I shall play) kah (saying) bismilaah (In God's Name) ."
            },
            {
                "original": "नाहन अकरब की बंसी बजाई, मन अरफ नफसहु की कूक सुणाई,",
                "hindi_gloss": "नाहन अकरब ('नहनु अक़रब' - हम तुम्हारी जीवन-नस से भी निकट हैं) की (की) बंसी (दिव्य बांसुरी) बजाई (बजाई है), मन अरफ नफसहु ('मन अराफ़ा नफ़्सहु' - जिसने स्वयं को पहचाना) की (की) कूक (पुकार) सुणाई (सुनाई है),",
                "english_gloss": "naahan akrab ('Nahnu aqrab' - We are closer than the jugular vein) kee (of) bansee (flute) bajaaee (played), man araph nafsahu ('Man 'arafa nafsahu' - who knows self) kee (of) kook (divine call) sunaaee (proclaimed),"
            },
            {
                "original": "फसुमावज्जु उल्हा की धूम मचाई, विच दरबार रसूले अल्लाह,",
                "hindi_gloss": "फसुमावज्जु उल्हा ('फ़सुम्मा वज्जुल्लाह' - जिधर देखो उधर अल्लाह का चेहरा है) की (की) धूम (धूम) मचाई (मचा दी है), विच (में) दरबार (दरबार में) रसूले अल्लाह (पैग़ंबर अल्लाह के),",
                "english_gloss": "fasumaavajju ulha ('Fasumma wajhullah' - There is the Face of God) kee (of) dhoom (resounding celebration) machaaee (raised), vich (in) darbaar (holy court) rasoole allaah (of Allah's Messenger),"
            },
            {
                "original": "होरी खेलूंगी कह बिसमिलाह ।",
                "hindi_gloss": "होरी (होली) खेलूंगी (खेलूँगी) कह (कहकर) बिसमिलाह (बिस्मिल्लाह) ।",
                "english_gloss": "horee (Holi) kheloongee (I will play) kah (saying) bismilaah (Bismillah) ."
            },
            {
                "original": "हाथ जोड़ कर पायों पड़ूंगी, आज़िज़ हो कर बेनती करूंगी,",
                "hindi_gloss": "हाथ (हाथ) जोड़ कर (जोड़कर) पायों (चरणों में) पड़ूंगी (गिर पड़ूँगी), आज़िज़ (दीन-असमर्थ) हो कर (होकर) बेनती (विनम्र प्रार्थना) करूंगी (करूँगी),",
                "english_gloss": "haath (hands) jod kar (joining) paayon (at holy feet) padoongee (shall fall), aaziz (humble) ho kar (becoming) benatee (prayer) karoongee (shall make),"
            },
            {
                "original": "झगड़ा कर भर झोली लूंगी, नूर मुहंमद सल्लउलाह ।",
                "hindi_gloss": "झगड़ा कर (प्रेम का हठ करके) भर (भर) झोली (अपनी झोली) लूंगी (भरवा लूँगी), नूर (उस नूर से) मुहंमद (मुहम्मद के) सल्लउलाह (सल्लल्लाहु अलैहि व सल्लम) ।",
                "english_gloss": "jhagda kar (with loving insistence) bhar (filling) jholee (lap/skirt) loongee (shall take), noor (light) muhammad (of Muhammad) sall-ullaah (peace be upon him) ."
            },
            {
                "original": "होरी खेलूंगी कह बिसमिलाह ।",
                "hindi_gloss": "होरी (होली) खेलूंगी (खेलूँगी) कह (कहकर) बिसमिलाह (बिस्मिल्लाह) ।",
                "english_gloss": "horee (Holi) kheloongee (I shall play) kah (saying) bismilaah (Bismillah) ."
            },
            {
                "original": "फ़ज़करूनी की होरी बनाऊं, फ़ज़करूनी पिया को रिझाऊं,",
                "hindi_gloss": "फ़ज़करूनी ('फ़ज़कुरूनी' - मेरा स्मरण करो) की (की) होरी (होली) बनाऊं (बनाऊँगी), फ़ज़करूनी (प्रभु-स्मरण के रंग से) पिया (अपने प्रियतम) को (को) रिझाऊं (रिझाऊँगी),",
                "english_gloss": "fazkaroonee ('Fazkuroonee' - Remember Me) kee (of) horee (Holi) banaaoon (shall make), fazkaroonee (remembrance) piya (Beloved) ko (unto) rijhaaoon (shall please),"
            },
            {
                "original": "ऐसो पिया के मैं बल बल जाऊं, कैसा पिया सुबहान अल्लाह ।",
                "hindi_gloss": "ऐसो (ऐसे दिव्य) पिया (साजन) के (के ऊपर) मैं (मैं) बल बल (न्योछावर/बलिहारी) जाऊं (जाती हूँ), कैसा (कैसा अद्भुत) पिया (प्रियतम है) सुबहान अल्लाह (सुब्हान अल्लाह / परम पवित्र ईश्वर) !",
                "english_gloss": "aiso (such) piya (Beloved) ke (unto) main (I) bal bal (sacrificed) jaaoon (go), kaisa (what a wondrous) piya (Beloved) subahaan allaah ('Glory be to God!') !"
            },
            {
                "original": "होरी खेलूंगी कह बिसमिलाह ।",
                "hindi_gloss": "होरी (होली) खेलूंगी (खेलूँगी) कह (कहकर) बिसमिलाह (बिस्मिल्लाह) ।",
                "english_gloss": "horee (Holi) kheloongee (I will play) kah (saying) bismilaah (In God's Name) ."
            },
            {
                "original": "सिबग़तउलाहै की भर पिचकारी, अलाह उस मद्द पी मूंह पर मारी,",
                "hindi_gloss": "सिबग़तउलाहै ('सिबग़तुल्लाह' - अल्लाह के रंग/रूहानी रंग) की (की) भर (भरकर) पिचकारी (पिचकारी), अलाह उस मद्द ('अल्लाह-उस-समद' - अल्लाह बेनियाज़ और शाश्वत है) पी (मेरे प्रियतम ने) मूंह पर (मेरे मुख पर) मारी (छिड़क दी),",
                "english_gloss": "sibgat-ullaahai ('Sibghatallah' - the baptismal Color of God) kee (of) bhar (filling) pichkaaree (water-syringe), allaah us madd ('Allah-us-Samad' - God the Eternal Absolute) pee (Beloved) moonh par (upon face) maaree (sprayed),"
            },
            {
                "original": "नूर नबी दा हक्क से जारी, नूर मुहंमद-सल्ला इल्ला,",
                "hindi_gloss": "नूर (दिव्य नूर) नबी दा (पैग़ंबर का) हक्क से (सत्य से) जारी (प्रवाहित हो रहा है), नूर (नूर) मुहंमद-सल्ला इल्ला (मुहम्मद मुस्तफ़ा का),",
                "english_gloss": "noor (radiant light) nabee da (of the Prophet) hakk se (from the Truth) jaaree (flowing), noor (light) muhammad-salla illa (of Muhammad),"
            },
            {
                "original": "बुल्ल्हा शाह दी धूम मची है, लाय-ला-इल इलाह ।",
                "hindi_gloss": "बुल्ल्हा शाह (बुल्ले शाह) दी (की) धूम (धूम) मची है (मच गई है), लाय-ला-इल इलाह (ला इलाहा इल्लल्लाह) ।",
                "english_gloss": "bullha shaah (Bulleh Shah's) dee (of) dhoom (fame/rejoicing) machee hai (resounds), laay-laa-il ilaah (No god but Allah) ."
            },
            {
                "original": "होरी खेलूंगी कह बिसमिलाह ।",
                "hindi_gloss": "होरी (होली) खेलूंगी (खेलूँगी) कह (कहकर) बिसमिलाह (बिस्मिल्लाह) ।",
                "english_gloss": "horee (Holi) kheloongee (I shall play) kah (saying) bismilaah ('In the Name of Allah') ."
            }
        ],
        "hindi_meaning": k41_hi,
        "english_meaning": k41_en
    }]
})

# ==========================================
# KAFI 42: 42. हुण किस थीं आप छुपाईदा
# ==========================================
k42_orig = """किते मुल्लां हो बुलेंदे हो, किते सुन्नत फ़रज़ दसेंदे हो,
किते राम दुहाई देंदे हो, किते मत्थे तिलक लगाईदा ।
हुण किस थीं आप छुपाईदा ।

मैं मेरी है कि तेरी है, इह अंत भसम दी ढेरी है,
इह ढेरी पिया ने घेरी है, ढेरी नूं नाच नचाईदा ।
हुण किस थीं आप छुपाईदा ।

किते बेसिर चौड़ां पाओगे, किते जोड़ इनसान हंढाओगे,
किते आदम हवा बण आओगे, कदी मैथों वी भुल्ल जाईदा ।
हुण किस थीं आप छुपाईदा ।

बाहर ज़ाहर डेरा पायो, आपे ढों ढों ढोल बजायो,
जग ते आपना आप जितायो, फिर अबदुल्ल दे घर धाईदा।
हुण किस थीं आप छुपाईदा ।

जो भाल तुसाडी करदा है, मोयां तों अग्गे मरदा है,
उह मोयां वी तैथों डरदा है, मत मोयां नूं मार कुहाईदा ।
हुण किस थीं आप छुपाईदा ।

बिन्दराबन में गऊआं चरावे, लंका चढ़ के नाद वजावे,
मक्के दा बण हाजी आवे, वाह वाह रंग वटाईदा ।
हुण किस थीं आप छुपाईदा ।

मनसूर तुसां ते आया ए तुसां सूली पकड़ चढ़ाइआ ए,
मेरा भाई बाबल जाइआ ए दियो खून बहा मेरे भाई दा ।
हुण किस थीं आप छुपाईदा ।

तुसीं सभनीं भेसीं थींदे हो, आपे मद आपे पींदे हो,
मैनूं हर जा तुसीं दसींदे हो, आपे आप को आप चुकाईदा ।
हुण किस थीं आप छुपाईदा ।

हुण पास तुसाडे वस्सांगी, ना बेदिल हो के नस्सांगी,
सभ भेत तुसाडे दस्सांगी, क्यों मैनूं अंग ना लाईदा ।
हुण किस थीं आप छुपाईदा ।

वाह जिस पर करम अवेहा है, तहकीक उह वी तैं जेहा है,
सच्च सही रवायत एहा है, तेरी नज़र मेहर तर जाईदा ।
हुण किस थीं आप छुपाईदा ।

विच भांबड़ बाग़ लवाईदा, जेहड़ा विचों आप वखाईदा,
जां अलफों अहद बणाईदा, तां बातन क्या बतलाईदा ।
हुण किस थीं आप छुपाईदा ।

बेली अल्लाह वाली मालक हो, तुसीं आपे आपने सालक हो,
आपे ख़लकत आप ख़ालक हो, आपे अमर मअरूफ़ कराईदा ।
हुण किस थीं आप छुपाईदा ।

किधरे चोर हो किधरे काज़ी हो, किते मम्बर ते बह वाअज़ी हो,
किते तेग़ बहादर ग़ाज़ी हो, आपे आपणा कटक चढ़ाईदा ।
हुण किस थीं आप छुपाईदा ।

आपे यूसफ़ कैद करायो, यूनस मच्छली तों निगलायो,
साबर कीड़े घत्त बहायो, फेर उहनां तख़त चढ़ाईदा ।
हुण किस थीं आप छुपाईदा ।

बुल्ल्हा शौह हुण सही सिंञाते हो, हर सूरत नाल पछाते हो,
किते आते हो किते जाते हो, हुण मैथों भुल्ल ना जाईदा ।
हुण किस थीं आप छुपाईदा ।"""

k42_hi = """कहीं मुल्ला बनकर बाँग पुकारते हो, कहीं सुन्नत और फ़र्ज़ के नियम सिखाते हो,  
कहीं 'राम-राम' की दुहाई देते हो, कहीं माथे पर तिलक लगाकर घूमते हो!  
अब भला अपने-आपको किससे छिपा रहे हो?  

यह 'मैं-मेरी' और 'तेरा-तेरी' क्या है? अंत में यह शरीर केवल राख की एक ढेरी है!  
इस माटी की ढेरी को साजन ने चारों ओर से घेर रखा है, और इसे कठपुतली की नाईं नचा रहा है!  
अब भला अपने-आपको किससे छिपा रहे हो?  

कहीं असीम शून्य में विस्तार पाते हो, कहीं हाड़-मांस जोड़कर मनुष्य का रूप धरते हो,  
कहीं आदम और हव्वा बनकर आते हो—भला क्या कभी मुझसे भी अपनी पहचान छिपा सकते हो?  
अब भला अपने-आपको किससे छिपा रहे हो?  

संसार में खुलेआम अपना डेरा जमाया, और स्वयं ही अपनी महिमा का ढोल बजाया!  
सारी दुनिया पर अपना प्रभुत्व जताया, और फिर अब्दुल्लाह के घर में नन्हे बालक बनकर आ गए!  
अब भला अपने-आपको किससे छिपा रहे हो?  

जो तुम्हारी खोज में निकलता है, वह शारीरिक मृत्यु से पूर्व ही अपने अहंकार से मर जाता है!  
वह मरकर भी तुमसे डरता है, कि कहीं तुम मरे हुए को पुनः विरह की आग में न तपा दो!  
अब भला अपने-आपको किससे छिपा रहे हो?  

वृंदावन में गायें चराते हो, लंका पर चढ़ाई करके शंख बजाते हो,  
मक्के का हाजी बनकर चले आते हो—वाह-वाह! क्या अद्भुत रंग बदलते हो!  
अब भला अपने-आपको किससे छिपा रहे हो?  

मंसूर तुम्हारे ही द्वार पर आया था, और तुमने उसे पकड़कर सूली पर चढ़ा दिया!  
वह तो मेरा सगा भाई और परम पिता का जाया था, मुझे मेरे भाई के ख़ून का बदला चुकाओ!  
अब भला अपने-आपको किससे छिपा रहे हो?  

तुम ही हर वेश में प्रकट होते हो, स्वयं ही प्रेम की शराब बनते हो और स्वयं ही उसे पीते हो!  
मुझे तो हर जगह बस तुम ही दिखाई देते हो, स्वयं ही अपना हिसाब चुकाते हो!  
अब भला अपने-आपको किससे छिपा रहे हो?  

अब तो मैं तुम्हारे ही पास रहूँगी, निराश होकर कभी तुमसे दूर नहीं भागूँगी!  
तुम्हारे सारे भेद दुनिया के सामने खोल दूँगी, तुम मुझे अपने गले से क्यों नहीं लगाते?  
अब भला अपने-आपको किससे छिपा रहे हो?  

जिस पर तुम्हारी ऐसी कृपा हो जाती है, वह भी साक्षात तुम्हारे ही समान ब्रह्म-स्वरूप हो जाता है!  
यही सत्य और प्रामाणिक वचन है कि तुम्हारी कृपादृष्टि से ही यह भवसागर पार किया जाता है!  
अब भला अपने-आपको किससे छिपा रहे हो?  

जलते हुए अंगारों में फूलों का बाग़ खिला देते हो, और उस बाग़ के बीच से साक्षात दर्शन देते हो!  
जब 'अलिफ़' से उस अद्वैत 'अहद' का सृजन हुआ, तो उस आंतरिक रहस्य का क्या बखान किया जाए!  
अब भला अपने-आपको किससे छिपा रहे हो?  

हे मित्र! तुम ही औलिया के स्वामी हो, और स्वयं ही अपने मार्ग के साधक हो!  
तुम ही सृष्टि हो और तुम ही सृजनहार हो, स्वयं ही धर्म के नियम बनाते हो!  
अब भला अपने-आपको किससे छिपा रहे हो?  

कहीं चोर बने बैठे हो, कहीं न्याय करने वाले क़ाज़ी हो, कहीं मिंबर पर बैठकर उपदेश देते हो,  
कहीं हाथ में तलवार लिए शूरवीर ग़ाज़ी हो, और स्वयं ही अपनी सेना का दल चढ़ा लाते हो!  
अब भला अपने-आपको किससे छिपा रहे हो?  

स्वयं ही यूसुफ़ को कैद कराया, यूनुस को मछली के पेट से निगलवाया,  
अय्यूब के शरीर में कीड़े डालकर परीक्षा ली, और फिर उन सबको साम्राज्य के सिंहासन पर बिठा दिया!  
अब भला अपने-आपको किससे छिपा रहे हो?  

हे बुल्ले के प्राण-स्वामी! अब मैंने आपको भली-भाँति पहचान लिया है, हर सूरत और रूप में आपको जान लिया है!  
चाहे कहीं से आओ या कहीं को जाओ, अब आप मुझसे छिप नहीं सकते!  
अब भला अपने-आपको किससे छिपा रहे हो?"""

k42_en = """Here as a mullah shouting the dawn call to prayer,  
There preaching strict rituals and dogmas with care,  
Here invoking Rama’s name with hands uplifted high,  
There wearing the sandal tilak beneath the open sky!  
From whom art Thou hiding Thyself now?  

What is this "I and mine", or "thou and thine" in the dust?  
In the end, this body is a heap of ash that returns to crust!  
Yet this heap of clay is besieged by the Beloved from above,  
Made to dance upon earth by the puppet-strings of Love!  
From whom art Thou hiding Thyself now?  

Here expanding boundless into formless space,  
There weaving bones and sinews to build a human face!  
Here stepping forth as Adam and Eve upon the sod—  
Canst Thou ever conceal Thine identity from me, O God?  
From whom art Thou hiding Thyself now?  

Thou didst pitch Thy royal pavilion in broad, manifest light,  
Sounding the victory drum before the universe's sight!  
Proclaiming Thy sovereignty over all lands and sea,  
Then running into Abdullah’s home as a babe in sweet decree!  
From whom art Thou hiding Thyself now?  

Whoever seeks Thee dies to the ego before mortal breath is spent,  
Yet even after dying, he trembles before Thy holy intent,  
Lest Thou strike the already slain with fresh yearnings anew!  
From whom art Thou hiding Thyself now?  

Grazing herds in Vrindavan as the flute-playing cowherd boy,  
Storming Lanka’s fortresses with conch-horns of warlike joy!  
Arriving at Mecca’s shrine as a pilgrim pure and white—  
Marvelous, O marvelous, are Thy masks of cosmic delight!  
From whom art Thou hiding Thyself now?  

Mansur Hallaj came running to Thy sanctuary of grace,  
And Thou didst seize him and raise him to the gallows’ place!  
He was my own brother, born of the same celestial sire—  
Pay me the ransom of my brother's blood from Thy fire!  
From whom art Thou hiding Thyself now?  

Thou art manifested in every single guise under the sun,  
Thou art Thyself the wine and the drinker merged in one!  
In every atom and star, Thou alone dost appear to me,  
Settling Thine own accounts through Thine own decree!  
From whom art Thou hiding Thyself now?  

Now beside Thee shall I abide, never to flee in grief,  
I shall unveil all Thy secrets to the world without relief!  
Why dost Thou delay to take me to Thy radiant breast?  
From whom art Thou hiding Thyself now?  

Blessed is the soul upon whom Thy grace falls complete,  
For truly he becomes one with Thee at Thy feet!  
This is the authentic scripture, ancient and true:  
A single glance of Thy mercy ferries the spirit through!  
From whom art Thou hiding Thyself now?  

In roaring flames Thou plantest a garden of fragrant flowers,  
And gazest out in splendor from within those blooming bowers!  
When the singular Alif unfolds into the Primordial One,  
What words can utter the mystery beneath the sun?  
From whom art Thou hiding Thyself now?  

O Friend, Thou art the Sovereign Lord of every saint and seer,  
Thyself the pilgrim walking the path both far and near!  
Thyself the creation and Thyself the Maker divine,  
Commanding virtue through every holy line!  
From whom art Thou hiding Thyself now?  

Here a thief lurking in shadows, there the judge upon the bench,  
Here preaching on the mosque’s high pulpit in Arabic and French!  
Here the valiant warrior wielding the battle blade,  
Leading Thine own armies in grand crusade!  
From whom art Thou hiding Thyself now?  

Thou didst plunge Joseph into the well and prison dark,  
Hadst Jonah swallowed in the belly of the sea’s vast shark!  
Tortured Job with biting worms upon his patient frame,  
Then raised them all to thrones of everlasting fame!  
From whom art Thou hiding Thyself now?  

Bulleh's Sovereign Lord! Now I recognize Thee through and through,  
In every single countenance I behold Thy vision true!  
Whether Thou comest near or departest far away,  
Thou canst no longer hide Thy face from me today!  
From whom art Thou hiding Thyself now?"""

batch.append({
    "id": 42,
    "title": "42. हुण किस थीं आप छुपाईदा",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k42_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "किते मुल्लां हो बुलेंदे हो, किते सुन्नत फ़रज़ दसेंदे हो,",
                "hindi_gloss": "किते (कहीं) मुल्लां (मुल्ला/मौलवी) हो (होकर) बुलेंदे हो (अज़ान पुकारते हो), किते (कहीं) सुन्नत (सुन्नत) फ़रज़ (और फ़र्ज़ के नियम) दसेंदे हो (सिखाते हो),",
                "english_gloss": "kite (somewhere) mullaan (mullah) ho (becoming) bulende ho (call to prayer), kite (somewhere) sunnat (Sunnah) faraz (obligatory duties) dasende ho (teach),"
            },
            {
                "original": "किते राम दुहाई देंदे हो, किते मत्थे तिलक लगाईदा ।",
                "hindi_gloss": "किते (कहीं) राम (राम नाम की) दुहाई (दुहाई) देंदे हो (देते हो), किते (और कहीं) मत्थे (माथे पर) तिलक (तिलक) लगाईदा (लगाए घूमते हो) ।",
                "english_gloss": "kite (somewhere) raam (Lord Rama's) duhaaee (invocation) dende ho (give), kite (somewhere) matthe (on forehead) tilak (sacred mark) lagaaeeda (wear) ."
            },
            {
                "original": "हुण किस थीं आप छुपाईदा ।",
                "hindi_gloss": "हुण (अब भला) किस थीं (किससे) आप (अपने-आप को) छुपाईदा (छिपाते हो) ।",
                "english_gloss": "hun (now) kis theen (from whom) aap (thine own Self) chhupaa-eeda (art hiding) ."
            },
            {
                "original": "मैं मेरी है कि तेरी है, इह अंत भसम दी ढेरी है,",
                "hindi_gloss": "मैं मेरी (यह 'मैं और मेरा') है कि (अथवा) तेरी (तेरी है), इह (यह शरीर) अंत (अंत में) भसम (राख) दी (की) ढेरी (ढेरी मात्र) है,",
                "english_gloss": "main meree (this 'I and mine') hai ki (or is it) teree (thine), eh (this body) ant (in the end) bhasam (ashes) dee (of) dheree (heap) hai (is),"
            },
            {
                "original": "इह ढेरी पिया ने घेरी है, ढेरी नूं नाच नचाईदा ।",
                "hindi_gloss": "इह (इस माटी की) ढेरी (ढेरी को) पिया ने (प्रियतम ने चारों ओर से) घेरी है (घेर रखा है), ढेरी नूं (और इस माटी की देह को कठपुतली की नाईं) नाच (नाच) नचाईदा (नचाया जा रहा है) ।",
                "english_gloss": "eh (this) dheree (heap of clay) piya ne (Beloved) gheree hai (has encompassed), dheree noon (unto this clay heap) naach (dance) nachaa-eeda (makes dance) ."
            },
            {
                "original": "हुण किस थीं आप छुपाईदा ।",
                "hindi_gloss": "हुण (अब) किस थीं (किससे) आप (अपने को) छुपाईदा (छिपाओगे) ।",
                "english_gloss": "hun (now) kis theen (from whom) aap (thyself) chhupaa-eeda (art hiding) ."
            },
            {
                "original": "किते बेसिर चौड़ां पाओगे, किते जोड़ इनसान हंढाओगे,",
                "hindi_gloss": "किते (कहीं) बेसिर (असीम शून्य में) चौड़ां (विस्तार) पाओगे (पाते हो), किते (कहीं) जोड़ (अंग-प्रत्यंग जोड़कर) इनसान (मनुष्य रूप) हंढाओगे (भोगते हो),",
                "english_gloss": "kite (somewhere) besir (formless) chaudaan (expanses) paaoge (measure), kite (somewhere) jod (joining limbs) insaan (human) handhaaoge (experience),"
            },
            {
                "original": "किते आदम हवा बण आओगे, कदी मैथों वी भुल्ल जाईदा ।",
                "hindi_gloss": "किते (कहीं) आदम (आदम) हवा (और हव्वा) बण (बनकर) आओगे (आते हो), कदी (क्या कभी) मैथों वी (मुझसे भी अपनी पहचान) भुल्ल (भुलाई) जाईदा (जा सकती है) ।",
                "english_gloss": "kite (somewhere) aadam (Adam) hava (Eve) ban (becoming) aaoge (comest), kadee (can ever) maithon vee (from me too) bhull (forgotten) jaa-eeda (be) ."
            },
            {
                "original": "हुण किस थीं आप छुपाईदा ।",
                "hindi_gloss": "हुण (अब) किस थीं (किससे) आप (अपने-आप को) छुपाईदा (छिपाते हो) ।",
                "english_gloss": "hun (now) kis theen (from whom) aap (thine own Self) chhupaa-eeda (art hiding) ."
            },
            {
                "original": "बाहर ज़ाहर डेरा पायो, आपे ढों ढों ढोल बजायो,",
                "hindi_gloss": "बाहर (संसार में) ज़ाहर (प्रत्यक्ष रूप से) डेरा (अपना डेरा) पायो (डाला है), आपे (स्वयं ही) ढों ढों (डंका बजाकर) ढोल (ढोल) बजायो (बजाते हो),",
                "english_gloss": "baahar (outwardly) zaahar (manifestly) dera (camp) paayo (pitched), aape (thyself) dhon dhon (drumbeat) dhol (drum) bajaayo (soundest),"
            },
            {
                "original": "जग ते आपना आप जितायो, फिर अबदुल्ल दे घर धाईदा।",
                "hindi_gloss": "जग ते (संसार पर) आपना आप (अपनी महिमा का डंका) जितायो (जताया), फिर (और फिर पैग़ंबर मुहम्मद के पिता) अबदुल्ल (अब्दुल्लाह) दे (के) घर (घर में शिशु बनकर) धाईदा (दौड़ आते हो) ।",
                "english_gloss": "jag te (upon the world) aapna aap (thy glory) jitaayo (proclaimed), phir (then) abdull (Abdullah's) de (of) ghar (home) dhaa-eeda (rushest) ."
            },
            {
                "original": "हुण किस थीं आप छुपाईदा ।",
                "hindi_gloss": "हुण (अब) किस थीं (किससे) आप (स्वयं को) छुपाईदा (छिपाओगे) ।",
                "english_gloss": "hun (now) kis theen (from whom) aap (thyself) chhupaa-eeda (art hiding) ."
            },
            {
                "original": "जो भाल तुसाडी करदा है, मोयां तों अग्गे मरदा है,",
                "hindi_gloss": "जो (जो कोई) भाल (खोज) तुसाडी (तुम्हारी) करदा है (करता है), मोयां तों अग्गे (शारीरिक मृत्यु से पहले ही) मरदा है (अहंकार से मर जाता है),",
                "english_gloss": "jo (whoever) bhaal (search) tusaadee (of thee) karda hai (does), moyaan ton agge (prior to dying) marda hai (dies to self),"
            },
            {
                "original": "उह मोयां वी तैथों डरदा है, मत मोयां नूं मार कुहाईदा ।",
                "hindi_gloss": "उह (वह) मोयां वी (मरकर भी) तैथों (तुमसे) डरदा है (डरता है कि), मत (कहीं तुम) मोयां नूं (मरे हुए को पुनः विरह में) मार (मार-मारकर) कुहाईदा (तड़पा न डालो) ।",
                "english_gloss": "uh (he) moyaan vee (even dead) taithon (of thee) darda hai (fears), mat (lest) moyaan noon (the already dead) maar (striking) kuhaa-eeda (torture) ."
            },
            {
                "original": "हुण किस थीं आप छुपाईदा ।",
                "hindi_gloss": "हुण (अब) किस थीं (किससे) आप (अपने को) छुपाईदा (छिपाते हो) ।",
                "english_gloss": "hun (now) kis theen (from whom) aap (thyself) chhupaa-eeda (art hiding) ."
            },
            {
                "original": "बिन्दराबन में गऊआं चरावे, लंका चढ़ के नाद वजावे,",
                "hindi_gloss": "बिन्दराबन में (वृंदावन में कन्हैया बन) गऊआं (गायों को) चरावे (चराता है), लंका (लंका पर) चढ़ के (चढ़ाई करके श्रीराम बन) नाद (युद्ध का शंख) वजावे (बजाता है),",
                "english_gloss": "bindraaban mein (in Vrindavan) gaaoo-aan (cows) charaave (grazes), lanka (Lanka) chadh ke (invading) naad (conch) vajaave (sounds),"
            },
            {
                "original": "मक्के दा बण हाजी आवे, वाह वाह रंग वटाईदा ।",
                "hindi_gloss": "मक्के दा (मक्का का) बण (बनकर) हाजी (हाजी) आवे (आता है), वाह वाह (वाह-वाह! कैसा अद्भुत) रंग (रंग-रूप) वटाईदा (बदलते हो) ।",
                "english_gloss": "makke da (of Mecca) ban (becoming) haajee (pilgrim) aave (comes), vaah vaah (marvelous!) rang (guise) vataa-eeda (thou exchangest) ."
            },
            {
                "original": "हुण किस थीं आप छुपाईदा ।",
                "hindi_gloss": "हुण (अब) किस थीं (किससे) आप (अपने को) छुपाईदा (छिपाते हो) ।",
                "english_gloss": "hun (now) kis theen (from whom) aap (thyself) chhupaa-eeda (art hiding) ."
            },
            {
                "original": "मनसूर तुसां ते आया ए तुसां सूली पकड़ चढ़ाइआ ए,",
                "hindi_gloss": "मनसूर (मंसूर अल-हल्लाज) तुसां ते (तुम्हारे द्वार पर) आया ए (आया था), तुसां (पर तुमने उसे) सूली (फांसी के तख्ते पर) पकड़ (पकड़कर) चढ़ाइआ ए (चढ़ा दिया),",
                "english_gloss": "mansoor (Mansur Hallaj) tusaan te (to thee) aaya e (came), tusaan (ye) soolee (upon gallows) pakad (seizing) chadhaaia e (mounted),"
            },
            {
                "original": "मेरा भाई बाबल जाइआ ए दियो खून बहा मेरे भाई दा ।",
                "hindi_gloss": "मेरा (वह मेरा) भाई (सगा भाई) बाबल जाइआ (आदि-पिता परमात्मा का जन्मा) ए (था), दियो (मुझे दो) खून बहा (ख़ून का बदला/दियत) मेरे (मेरे) भाई (भाई) दा (का) ।",
                "english_gloss": "mera (my) bhaaee (brother) baabal jaaia (father-born) e (was), diyo (give) khoon baha (blood-money) mere (my) bhaaee (brother's) da (of) ."
            },
            {
                "original": "हुण किस थीं आप छुपाईदा ।",
                "hindi_gloss": "हुण (अब) किस थीं (किससे) आप (अपने को) छुपाईदा (छिपाते हो) ।",
                "english_gloss": "hun (now) kis theen (from whom) aap (thyself) chhupaa-eeda (art hiding) ."
            },
            {
                "original": "तुसीं सभनीं भेसीं थींदे हो, आपे मद आपे पींदे हो,",
                "hindi_gloss": "तुसीं (तुम) सभनीं (समस्त) भेसीं (वेशों में) थींदे हो (विद्यमान होते हो), आपे (स्वयं ही) मद (शराब हो) आपे (और स्वयं ही उसे) पींदे हो (पीते हो),",
                "english_gloss": "tuseen (thou) sabhneen (in all) bheseen (guises) theende ho (art), aape (thyself) mad (wine) aape (thyself) peende ho (drinkest),"
            },
            {
                "original": "मैनूं हर जा तुसीं दसींदे हो, आपे आप को आप चुकाईदा ।",
                "hindi_gloss": "मैनूं (मुझको) हर जा (हर स्थान पर) तुसीं (तुम ही) दसींदे हो (दिखाई देते हो), आपे (स्वयं ही) आप को (अपने-आप को) आप (स्वयं) चुकाईदा (परखते और चुकाते हो) ।",
                "english_gloss": "mainoon (unto me) har jaa (everywhere) tuseen (thou) daseende ho (art visible), aape (thyself) aap ko (to thyself) aap (thyself) chukaa-eeda (satisfiest) ."
            },
            {
                "original": "हुण किस थीं आप छुपाईदा ।",
                "hindi_gloss": "हुण (अब) किस थीं (किससे) आप (अपने को) छुपाईदा (छिपाओगे) ।",
                "english_gloss": "hun (now) kis theen (from whom) aap (thyself) chhupaa-eeda (art hiding) ."
            },
            {
                "original": "हुण पास तुसाडे वस्सांगी, ना बेदिल हो के नस्सांगी,",
                "hindi_gloss": "हुण (अब मैं) पास (पास) तुसाडे (तुम्हारे ही) वस्सांगी (बसूँगी), ना (नहीं) बेदिल (निराश) हो के (होकर) नस्सांगी (भागूँगी),",
                "english_gloss": "hun (now) paas (near) tusaade (thee) vassaangee (shall abide), na (not) bedil (broken-hearted) ho ke (becoming) nassaangee (shall flee),"
            },
            {
                "original": "सभ भेत तुसाडे दस्सांगी, क्यों मैनूं अंग ना लाईदा ।",
                "hindi_gloss": "सभ (सारे) भेत (रहस्य) तुसाडे (तुम्हारे संसार को) दस्सांगी (बता दूँगी), क्यों (तुम क्यों भला) मैनूं (मुझको) अंग (अपने आलिंगन में) ना (नहीं) लाईदा (लगाते) ।",
                "english_gloss": "sabh (all) bhet (secrets) tusaade (thine) dassaangee (shall reveal), kyon (why) mainoon (me) ang (to bosom) na (not) laa-eeda (dost embrace) ."
            },
            {
                "original": "हुण किस थीं आप छुपाईदा ।",
                "hindi_gloss": "हुण (अब) किस थीं (किससे) आप (अपने को) छुपाईदा (छिपाओगे) ।",
                "english_gloss": "hun (now) kis theen (from whom) aap (thyself) chhupaa-eeda (art hiding) ."
            },
            {
                "original": "वाह जिस पर करम अवेहा है, तहकीक उह वी तैं जेहा है,",
                "hindi_gloss": "वाह (धन्य है वह) जिस पर (जिस पर तुम्हारी) करम (कृपा की नज़र) अवेहा है (ऐसी होती है), तहकीक (निश्चय ही) उह वी (वह भी) तैं जेहा (तुम्हारे ही समान परमात्मा) है,",
                "english_gloss": "vaah (blessed) jis par (upon whom) karam (grace) aveha hai (such is), tahkeek (truly) uh vee (he too) tain jeha (like unto thee) hai (is),"
            },
            {
                "original": "सच्च सही रवायत एहा है, तेरी नज़र मेहर तर जाईदा ।",
                "hindi_gloss": "सच्च (सत्य) सही (और प्रामाणिक) रवायत (परंपरा/कथन) एहा है (यही है कि), तेरी (तुम्हारी) नज़र (कृपादृष्टि और) मेहर (महरबानी से भवसागर) तर जाईदा (तर जाया जाता है) ।",
                "english_gloss": "sachh (truth) sahee (authentic) ravaayat (tradition) eha hai (is this), teree (thy) nazar (glance) mehar (of grace) tar jaa-eeda (one crosses over) ."
            },
            {
                "original": "हुण किस थीं आप छुपाईदा ।",
                "hindi_gloss": "हुण (अब) किस थीं (किससे) आप (अपने को) छुपाईदा (छिपाओगे) ।",
                "english_gloss": "hun (now) kis theen (from whom) aap (thyself) chhupaa-eeda (art hiding) ."
            },
            {
                "original": "विच भांबड़ बाग़ लवाईदा, जेहड़ा विचों आप वखाईदा,",
                "hindi_gloss": "विच (अग्नि के) भांबड़ (भीषण अंगारों में) बाग़ (फूलों का बाग़) लवाईदा (लगा देते हो जैसे इब्राहीम के लिए), जेहड़ा (जो) विचों (भीतर से) आप (स्वयं प्रकट होकर) वखाईदा (दर्शन देते हो),",
                "english_gloss": "vich (in) bhaambad (roaring fire) baag (garden) lavaa-eeda (makest bloom), jehda (who) vichon (from within) aap (thyself) vakhaa-eeda (showest),"
            },
            {
                "original": "जां अलफों अहद बणाईदा, तां बातन क्या बतलाईदा ।",
                "hindi_gloss": "जां (जब) अलफों ('अलिफ़' से) अहद ('अहद' / परम एकत्व) बणाईदा (बनता है), तां (तब) बातन (आंतरिक गूढ़ रहस्यों को) क्या (क्या कहकर) बतलाईदा (बतलाया जाए) ।",
                "english_gloss": "jaan (when) alafon (from Alif) ahad (Ahad/the One) banaa-eeda (is made), taan (then) baatan (hidden truths) kya (what) batlaa-eeda (can be expressed) ."
            },
            {
                "original": "हुण किस थीं आप छुपाईदा ।",
                "hindi_gloss": "हुण (अब) किस थीं (किससे) आप (अपने को) छुपाईदा (छिपाते हो) ।",
                "english_gloss": "hun (now) kis theen (from whom) aap (thyself) chhupaa-eeda (art hiding) ."
            },
            {
                "original": "बेली अल्लाह वाली मालक हो, तुसीं आपे आपने सालक हो,",
                "hindi_gloss": "बेली (हे सखा!) अल्लाह (अल्लाह) वाली (और औलिया के) मालक हो (स्वामी हो), तुसीं (तुम) आपे (स्वयं ही) आपने (अपने मार्ग के) सालक (साधक/पथिक) हो,",
                "english_gloss": "belee (O Friend) allaah (Allah) vaalee (guardian/saint's) maalak ho (Master art thou), tuseen (thou) aape (thyself) aapne (thy own) saalak (seeker/traveler) ho (art),"
            },
            {
                "original": "आपे ख़लकत आप ख़ालक हो, आपे अमर मअरूफ़ कराईदा ।",
                "hindi_gloss": "आपे (स्वयं ही) ख़लकत (सृष्टि) आप (और स्वयं ही) ख़ालक (सृजनहार) हो, आपे (स्वयं ही शुभ धर्म-कर्म का) अमर मअरूफ़ (आदेश) कराईदा (करवाते हो) ।",
                "english_gloss": "aape (thyself) khalkat (creation) aap (thyself) khaalak (Creator) ho (art), aape (thyself) amar ma'roof (moral injunctions) karaa-eeda (prescribest) ."
            },
            {
                "original": "हुण किस थीं आप छुपाईदा ।",
                "hindi_gloss": "हुण (अब) किस थीं (किससे) आप (अपने को) छुपाईदा (छिपाओगे) ।",
                "english_gloss": "hun (now) kis theen (from whom) aap (thyself) chhupaa-eeda (art hiding) ."
            },
            {
                "original": "किधरे चोर हो किधरे काज़ी हो, किते मम्बर ते बह वाअज़ी हो,",
                "hindi_gloss": "किधरे (कहीं) चोर हो (चोर बने हो) किधरे (कहीं न्याय करने वाले) काज़ी हो (क़ाज़ी हो), किते (कहीं) मम्बर ते (मस्जिद के मिंबर पर) बह (बैठकर) वाअज़ी हो (उपदेशक बने हो),",
                "english_gloss": "kidhre (somewhere) chor ho (thief art) kidhre (somewhere) kaazee ho (judge art), kite (somewhere) mambr te (upon the pulpit) bah (sitting) va'azee ho (preacher art),"
            },
            {
                "original": "किते तेग़ बहादर ग़ाज़ी हो, आपे आपणा कटक चढ़ाईदा ।",
                "hindi_gloss": "किते (कहीं) तेग़ बहादर (हाथ में तलवार लिए शूरवीर) ग़ाज़ी हो (ग़ाज़ी बने हो), आपे (स्वयं ही) आपणा (अपनी ही सेना का) कटक (कटक/दल) चढ़ाईदा (चढ़ा लाते हो) ।",
                "english_gloss": "kite (somewhere) teg bahaadar (valiant sword-bearing) gaazee ho (warrior art), aape (thyself) aapna (thine own) katak (army) chadhaa-eeda (leadest into battle) ."
            },
            {
                "original": "हुण किस थीं आप छुपाईदा ।",
                "hindi_gloss": "हुण (अब) किस थीं (किससे) आप (अपने को) छुपाईदा (छिपाते हो) ।",
                "english_gloss": "hun (now) kis theen (from whom) aap (thyself) chhupaa-eeda (art hiding) ."
            },
            {
                "original": "आपे यूसफ़ कैद करायो, यूनस मच्छली तों निगलायो,",
                "hindi_gloss": "आपे (स्वयं ही तुमने) यूसफ़ (हज़रत यूसुफ़ को कुएं और जेल में) कैद करायो (कैद कराया), यूनस (हज़रत यूनुस को) मच्छली तों (मछली के पेट से) निगलायो (निगलवाया),",
                "english_gloss": "aape (thyself) yoosaf (Joseph) kaid karaayo (imprisoned), yoonas (Jonah) machhalee ton (by whale) niglaayo (caused to be swallowed),"
            },
            {
                "original": "साबर कीड़े घत्त बहायो, फेर उहनां तख़त चढ़ाईदा ।",
                "hindi_gloss": "साबर (धैर्यवान अय्यूब के शरीर में) कीड़े घत्त (कीड़े डालकर) बहायो (तपाया), फेर (और फिर) उहनां (उन सबको साम्राज्य के) तख़त (सिंहासन पर) चढ़ाईदा (आसीन किया) ।",
                "english_gloss": "saabar (the patient Job) keede ghatt (casting worms) bahaayo (tested), pher (then) uhnaan (them) takhat (upon the throne) chadhaa-eeda (exalted) ."
            },
            {
                "original": "हुण किस थीं आप छुपाईदा ।",
                "hindi_gloss": "हुण (अब) किस थीं (किससे) आप (अपने को) छुपाईदा (छिपाओगे) ।",
                "english_gloss": "hun (now) kis theen (from whom) aap (thyself) chhupaa-eeda (art hiding) ."
            },
            {
                "original": "बुल्ल्हा शौह हुण सही सिंञाते हो, हर सूरत नाल पछाते हो,",
                "hindi_gloss": "बुल्ल्हा (बुल्ले के) शौह (प्राण-स्वामी!) हुण (अब मैंने आपको) सही (भली-भाँति) सिंञाते हो (पहचान लिया है), हर (प्रत्येक) सूरत नाल (सूरत में) पछाते हो (पहचान लिया है),",
                "english_gloss": "bullha (Bulleh's) shauh (Lord) hun (now) sahee (accurately) sinjaate ho (hast been recognized), har (in every) soorat naal (face/form) pachhaate ho (discerned),"
            },
            {
                "original": "किते आते हो किते जाते हो, हुण मैथों भुल्ल ना जाईदा ।",
                "hindi_gloss": "किते (चाहे कहीं) आते हो (आते हो) किते (या कहीं) जाते हो (जाते हो), हुण (अब) मैथों (मुझसे अपने रूप को) भुल्ल ना (छिपाया नहीं) जाईदा (जा सकता) ।",
                "english_gloss": "kite (somewhere) aate ho (thou comest) kite (somewhere) jaate ho (thou goest), hun (now) maithon (from me) bhull na (forgotten/hidden) jaa-eeda (canst be) ."
            },
            {
                "original": "हुण किस थीं आप छुपाईदा ।",
                "hindi_gloss": "हुण (अब) किस थीं (किससे) आप (अपने को) छुपाईदा (छिपाते हो) ।",
                "english_gloss": "hun (now) kis theen (from whom) aap (thine own Self) chhupaa-eeda (art hiding) ."
            }
        ],
        "hindi_meaning": k42_hi,
        "english_meaning": k42_en
    }]
})

# ==========================================
# KAFI 43: 43. हुण मैं लखिआ सोहणा यार
# ==========================================
k43_orig = """हुण मैं लखिआ सोहणा यार ।
जिस दे हुसन दा गरम बज़ार ।

जद अहद इक इकल्ला सी, ना ज़ाहर कोई तजल्ला सी,
ना रब्ब रसूल ना अल्लाह सी, ना जबार ते ना कहार ।
हुण मैं लखिआ सोहणा यार ।

बेचून वा बेचगूना सी, बेशबीह बेनमूना सी,
ना कोई रंग ना नमूना सी, हुण गूनां-गुन हज़ार ।
हुण मैं लखिआ सोहणा यार ।

प्यारा पहन पोशाकां आया, आदम आपना नाम धराइआ,
अहद ते बण अहमद आया, नबियां दा सरदार ।
हुण मैं लखिआ सोहणा यार ।

कुन केहा फाजीकून कहाइआ, बेचूनी से चूनी बणाइआ,
अहद दे विच मीम रलाइआ, तां कीता ऐड पसार ।
हुण मैं लखिआ सोहणा यार ।

तजूं मसीत तजूं बुत्तखाना, बरती रहां ना रोज़ा जाणा,
भुल्ल गया वुज़ू नमाज़ दुगाणा, तैं पर जान करां बलिहार ।
हुण मैं लखिआ सोहणा यार ।

पीर पैग़म्बर इसदे बरदे, इस मलायक सजदे करदे,
सर कदमां दे उत्ते धरदे, सभ तों वड्डी उह सरकार ।
हुण मैं लखिआ सोहणा यार ।

जो कोई उस नूं लखिआ चाहे, बाझ वसीले लखिआ ना जाए,
शाह अनायत भेत बताए, तां खुल्ल्हे सभ इसरार ।
हुण मैं लखिआ सोहणा यार ।"""

k43_hi = """अब मैंने उस परम सुंदर साजन को पहचान लिया है,  
जिसके अलौकिक सौंदर्य से सारा ब्रह्मांड जगमगा उठा है!  

जब वह अद्वैत 'अहद' नितांत अकेला था, तब न कोई प्रकाश प्रकट था और न कोई संसार!  
न रब, न रसूल, न अल्लाह का नाम था, और न कोई जब्बार या क़हहार का रूप था!  
अब मैंने उस परम सुंदर साजन को पहचान लिया है!  

वह अकथनीय, अतुलनीय, उपमा-रहित और अद्वितीय था!  
न उसका कोई रंग था और न कोई आकार, पर आज देखो तो उसके हज़ारों रंग और रूप प्रकट हैं!  
अब मैंने उस परम सुंदर साजन को पहचान लिया है!  

वह प्यारा प्रियतम मनुष्य का चोला पहनकर आया, और उसने अपना नाम 'आदम' रखवाया!  
उस अद्वैत 'अहद' से वह नबियों का सरदार 'अहमद' बनकर प्रकट हुआ!  
अब मैंने उस परम सुंदर साजन को पहचान लिया है!  

उसने 'कुन' (हो जा!) कहा और सृष्टि रच दी, निराकार से वह साकार बन गया!  
उस 'अहद' के बीच उसने 'मीम' का रहस्य मिला दिया, और इस सारे ब्रह्मांड का विस्तार कर दिया!  
अब मैंने उस परम सुंदर साजन को पहचान लिया है!  

मैं मस्जिद को भी छोड़ता हूँ और मंदिर-बुत्तख़ाने को भी त्यागता हूँ!  
न मैं व्रत रखता हूँ और न रोज़ों के बंधन जानता हूँ!  
वज़ू और दो रकअत नमाज़ के सारे नियम भूल गए हैं, मैं तो अपनी जान तुम पर न्योछावर करता हूँ!  
अब मैंने उस परम सुंदर साजन को पहचान लिया है!  

सारे पीर और पैग़ंबर जिसके विनम्र सेवक हैं, फ़रिश्ते जिसे सजदा करते हैं,  
और अपना शीश जिसके पावन चरणों में रखते हैं—उसकी सत्ता समस्त संसार में सर्वोच्च है!  
अब मैंने उस परम सुंदर साजन को पहचान लिया है!  

जो कोई उस परमात्मा को पहचानना चाहता है, वह बिना सद्गुरु के माध्यम के कभी नहीं जान सकता!  
जब मुर्शिद शाह इनायत ने यह आंतरिक भेद समझाया, तब जाकर सारे ईश्वरीय रहस्य खुल गए!  
अब मैंने उस परम सुंदर साजन को पहचान लिया है!"""

k43_en = """Now have I beheld the Beautiful Beloved bright,  
Whose radiant splendor fills the cosmic bazaar with light!  

When the One Ahad dwelt in solitary grace,  
No manifestation yet illuminated time or space;  
Neither Lord nor Messenger, nor Allah’s holy Name,  
Neither Wrathful nor Subduer in that primordial flame!  
Now have I beheld the Beautiful Beloved bright!  

Ineffable, peerless, beyond all image and style,  
Without form or likeness across the cosmic mile;  
Devoid of earthly colors or patterned design,  
Yet today He blossoms in thousand hues divine!  
Now have I beheld the Beautiful Beloved bright!  

Donning the mortal robe, the Beloved came to birth,  
Calling Himself "Adam" upon the virgin earth;  
From the transcendent Ahad, Ahmad stepped in view,  
Sovereign of the prophets, radiant and true!  
Now have I beheld the Beautiful Beloved bright!  

He uttered: Kun!—Be!—and the universe unfurled,  
From formless silence shaping the living world;  
In the word Ahad, He joined the mystic Meem,  
Spreading the vast expanse of creation's dream!  
Now have I beheld the Beautiful Beloved bright!  

I leave the mosque behind, and renounce the idol-shrine,  
I observe neither ritual fasting nor formal line;  
Ablutions and dual prayers vanish from my mind,  
For upon Thy altar my breath is resigned!  
Now have I beheld the Beautiful Beloved bright!  

Prophets and holy masters are bondmen at His door,  
Angels bow in prostration upon His palace floor;  
Placing their reverent crowns upon His feet so sweet—  
Supreme is His kingdom where time and eternity meet!  
Now have I beheld the Beautiful Beloved bright!  

Whosoever yearns to know that Sovereign Lord of grace,  
Without a guiding Master can never see His face;  
When Murshid Shah Inayat revealed the inner key,  
All hidden mysteries unlocked in ecstasy!  
Now have I beheld the Beautiful Beloved bright!"""

batch.append({
    "id": 43,
    "title": "43. हुण मैं लखिआ सोहणा यार",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k43_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "हुण मैं लखिआ सोहणा यार ।",
                "hindi_gloss": "हुण (अब) मैं (मैंने) लखिआ (पहचान लिया है) सोहणा (उस परम सुंदर) यार (प्रियतम को) ।",
                "english_gloss": "hun (now) main (I) lakhea (have beheld/recognized) sohna (the beautiful) yaar (Beloved) ."
            },
            {
                "original": "जिस दे हुसन दा गरम बज़ार ।",
                "hindi_gloss": "जिस दे (जिसके) हुसन दा (सौंदर्य का) गरम (धूम मचाने वाला) बज़ार (बाज़ार सजा है) ।",
                "english_gloss": "jis de (whose) husan da (of beauty's) garam (bustling/radiant) bazaar (marketplace) ."
            },
            {
                "original": "जद अहद इक इकल्ला सी, ना ज़ाहर कोई तजल्ला सी,",
                "hindi_gloss": "जद (जब) अहद (वह अद्वैत परमात्मा) इक इकल्ला सी (बिल्कुल अकेला था), ना (न कोई) ज़ाहर (प्रकट) कोई (कोई) तजल्ला (दिव्य ज्योति/प्रकाश) सी (था),",
                "english_gloss": "jad (when) ahad (the One/Ahad) ik ikalla see (was all alone), na (no) zaahar (manifest) koee (any) tajalla (radiance/light) see (was),"
            },
            {
                "original": "ना रब्ब रसूल ना अल्लाह सी, ना जबार ते ना कहार ।",
                "hindi_gloss": "ना (न कोई) रब्ब (रब) रसूल (रसूल) ना (न कोई) अल्लाह (अल्लाह नाम) सी (था), ना (न कोई) जबार (जब्बार/सर्वशक्तिमान) ते (और) ना (न) कहार (क़हहार/दंडदाता) ।",
                "english_gloss": "na (neither) rabb (Lord) rasool (Messenger) na (nor) allaah see (was Allah), na (neither) jabaar (Compeller) te (nor) na (neither) kahaar (Subduer) ."
            },
            {
                "original": "हुण मैं लखिआ सोहणा यार ।",
                "hindi_gloss": "हुण (अब) मैं (मैंने) लखिआ (पहचान लिया है) सोहणा (सुंदर) यार (प्रियतम को) ।",
                "english_gloss": "hun (now) main (I) lakhea (have recognized) sohna (the lovely) yaar (Beloved) ."
            },
            {
                "original": "बेचून वा बेचगूना सी, बेशबीह बेनमूना सी,",
                "hindi_gloss": "बेचून (अकथनीय) वा (और) बेचगूना (अतुलनीय) सी (था), बेशबीह (जिसकी कोई उपमा न थी) बेनमूना (अद्वितीय) सी (था),",
                "english_gloss": "bechoon (ineffable) va (and) bechagoona see (peerless was), beshabeeh (incomparable) benamoona see (unmodeled was),"
            },
            {
                "original": "ना कोई रंग ना नमूना सी, हुण गूनां-गुन हज़ार ।",
                "hindi_gloss": "ना (न) कोई (कोई) रंग (रंग) ना (न) नमूना (आकार) सी (था), हुण (अब उसके) गूनां-गुन (हज़ारों गुण और रंग) हज़ार (हज़ार हैं) ।",
                "english_gloss": "na (no) koee (any) rang (color) na (nor) namoona see (form was), hun (now) goonaan-gun (countless modes) hazaar (thousands) ."
            },
            {
                "original": "हुण मैं लखिआ सोहणा यार ।",
                "hindi_gloss": "हुण (अब) मैं (मैंने) लखिआ (पहचाना) सोहणा (सुंदर) यार (प्रियतम) ।",
                "english_gloss": "hun (now) main (I) lakhea (have seen) sohna (the beautiful) yaar (Beloved) ."
            },
            {
                "original": "प्यारा पहन पोशाकां आया, आदम आपना नाम धराइआ,",
                "hindi_gloss": "प्यारा (वह प्रियतम) पहन पोशाकां (मानव चोला पहनकर) आया (प्रकट हुआ), आदम (आदम) आपना (अपना) नाम धराइआ (नाम रखवाया),",
                "english_gloss": "pyaara (Beloved) pahan poshaakaan (wearing garments) aaya (came), aadam (Adam) aapna (His own) naam dharaaia (named),"
            },
            {
                "original": "अहद ते बण अहमद आया, नबियां दा सरदार ।",
                "hindi_gloss": "अहद ते (उस 'अहद' एकत्व से) बण (बनकर) अहमद ('अहमद' / मुहम्मद) आया (आया), नबियां दा (पैग़ंबरों का) सरदार (सरदार) ।",
                "english_gloss": "ahad te (from Ahad) ban (becoming) ahmad aaya (came Ahmad), nabiyaan da (of prophets) sardaar (the Chief/Leader) ."
            },
            {
                "original": "हुण मैं लखिआ सोहणा यार ।",
                "hindi_gloss": "हुण (अब) मैं (मैंने) लखिआ (जाना) सोहणा (सुंदर) यार (यार) ।",
                "english_gloss": "hun (now) main (I) lakhea (have known) sohna (the fair) yaar (Friend) ."
            },
            {
                "original": "कुन केहा फाजीकून कहाइआ, बेचूनी से चूनी बणाइआ,",
                "hindi_gloss": "कुन केहा ('कुन' / हो जा कहा) फाजीकून ('फयकून' / और सृष्टि हो गई कहलाया), बेचूनी से (अपरिमित से) चूनी (साकार) बणाइआ (बनाया),",
                "english_gloss": "kun keha (said 'Kun') phaajeekoon kahaaia (became 'fayakun'), bechoonee se (from formlessness) choonee banaaia (created form),"
            },
            {
                "original": "अहद दे विच मीम रलाइआ, तां कीता ऐड पसार ।",
                "hindi_gloss": "अहद दे विच ('अहद' के भीतर) मीम ('मीम' अक्षर / मुहम्मद का भाव) रलाइआ (मिला दिया), तां (तब) कीता (किया) ऐड (इतना विशाल) पसार (संसार का फैलाव) ।",
                "english_gloss": "ahad de vich (in Ahad) meem rlaaia (blended 'M'), taan (then) keeta (made) aid (so vast) pasaar (cosmic expansion) ."
            },
            {
                "original": "हुण मैं लखिआ सोहणा यार ।",
                "hindi_gloss": "हुण (अब) मैं (मैंने) लखिआ (पहचान लिया) सोहणा (सुंदर) यार (प्रियतम) ।",
                "english_gloss": "hun (now) main (I) lakhea (have beheld) sohna (the beloved) yaar (Friend) ."
            },
            {
                "original": "तजूं मसीत तजूं बुत्तखाना, बरती रहां ना रोज़ा जाणा,",
                "hindi_gloss": "तजूं (त्याग दूँ) मसीत (मस्जिद) तजूं (त्याग दूँ) बुत्तखाना (मंदिर), बरती रहां (न व्रत रखूँ) ना (न) रोज़ा जाणा (रोज़े के नियम जानूँ),",
                "english_gloss": "tajoon (I renounce) maseet (mosque) tajoon (I leave) buttkhaana (temple), bartee rahaan (keep fasting) na (nor) roza jaana (know formal fast),"
            },
            {
                "original": "भुल्ल गया वुज़ू नमाज़ दुगाणा, तैं पर जान करां बलिहार ।",
                "hindi_gloss": "भुल्ल गया (विस्मृत हो गया) वुज़ू (वज़ू) नमाज़ (नमाज़) दुगाणा (दो रकअत की नमाज़), तैं पर (तुम पर अपनी) जान (जान) करां (कर दूँ) बलिहार (न्योछावर) ।",
                "english_gloss": "bhull gaya (forgotten) vuzoo (ablution) namaaz dugaana (two-rak'at prayer), tain par (upon Thee) jaan (life) karaan (I make) balihaar (sacrifice) ."
            },
            {
                "original": "हुण मैं लखिआ सोहणा यार ।",
                "hindi_gloss": "हुण (अब) मैं (मैंने) लखिआ (पहचाना) सोहणा (सुंदर) यार (प्रियतम) ।",
                "english_gloss": "hun (now) main (I) lakhea (have beheld) sohna (fair) yaar (Beloved) ."
            },
            {
                "original": "पीर पैग़म्बर इसदे बरदे, इस मलायक सजदे करदे,",
                "hindi_gloss": "पीर (पीर) पैग़म्बर (और पैग़ंबर) इसदे (इसके) बरदे (विनम्र दास हैं), इस (इसको) मलायक (देवदूत/फ़रिश्ते) सजदे करदे (सजदा करते हैं),",
                "english_gloss": "peer (saints) paigambar (prophets) isde (His) barde (slaves/servants), is (unto Him) malaayak (angels) sajde karde (prostrate),"
            },
            {
                "original": "सर कदमां दे उत्ते धरदे, सभ तों वड्डी उह सरकार ।",
                "hindi_gloss": "सर (शीश) कदमां दे उत्ते (चरणों पर) धरदे (रखते हैं), सभ तों (सबसे) वड्डी (महान) उह (उस प्रभु की) सरकार (सत्ता है) ।",
                "english_gloss": "sar (heads) kadmaan de utte (upon feet) dharde (place), sabh ton (above all) vaddee (supreme) uh (that) sarkaar (Sovereignty) ."
            },
            {
                "original": "हुण मैं लखिआ सोहणा यार ।",
                "hindi_gloss": "हुण (अब) मैं (मैंने) लखिआ (पहचाना) सोहणा (सुंदर) यार (प्रियतम) ।",
                "english_gloss": "hun (now) main (I) lakhea (have recognized) sohna (Beloved) yaar (Friend) ."
            },
            {
                "original": "जो कोई उस नूं लखिआ चाहे, बाझ वसीले लखिआ ना जाए,",
                "hindi_gloss": "जो कोई (जो कोई भी) उस नूं (उस परमात्मा को) लखिआ चाहे (पहचानना चाहता है), बाझ (बिना सद्गुरु के) वसीले (माध्यम के) लखिआ ना जाए (पहचाना नहीं जा सकता),",
                "english_gloss": "jo koee (whoever) us noon (Him) lakhea chaahe (wishes to perceive), baajh (without) vaseele (mediator/Master) lakhea na jaae (cannot perceive),"
            },
            {
                "original": "शाह अनायत भेत बताए, तां खुल्ल्हे सभ इसरार ।",
                "hindi_gloss": "शाह अनायत (सद्गुरु शाह इनायत जब) भेत (गूढ़ भेद) बताए (समझाते हैं), तां (तभी) खुल्ल्हे (खुलते हैं) सभ (समस्त) इसरार (ईश्वरीय रहस्य) ।",
                "english_gloss": "shaah anaayat (Shah Inayat) bhet bataae (reveals secrets), taan (then) khullhe (unlocked) sabh (all) israar (divine mysteries) ."
            },
            {
                "original": "हुण मैं लखिआ सोहणा यार ।",
                "hindi_gloss": "हुण (अब) मैं (मैंने) लखिआ (पहचान लिया है) सोहणा (परम सुंदर) यार (प्रियतम को) ।",
                "english_gloss": "hun (now) main (I) lakhea (have recognized) sohna (the Beautiful) yaar (Beloved) ."
            }
        ],
        "hindi_meaning": k43_hi,
        "english_meaning": k43_en
    }]
})

# ==========================================
# KAFI 44: 44. हुण मैनूं कौण पछाणे, हुण मैं हो गई नी कुझ होर
# ==========================================
k44_orig = """हादी मैनूं सबक पढ़ाइआ, ओथे ग़ैर ना आया जाइआ,
मतलक ज़ात जमाल विखाइआ, वहदत पाइआ शोर ।
हुण मैनूं कौण पछाणे, हुण मैं हो गई नी कुझ होर ।

अव्वल हो के लामकानी, ज़ाहर बातन दिसदा जानी,
रिहा ना मेरा नाम निशानी, मिट गया झगड़ा शोर ।
हुण मैनूं कौण पछाणे, हुण मैं हो गई नी कुझ होर ।

प्यारा आप जमाल विखाले, मसत कलन्दर होण मतवाले,
हंसां दे हुण वेख लै चाले, बुल्ल्हा कागां दी हुण गई टोर ।
हुण मैनूं कौण पछाणे, हुण मैं हो गई नी कुझ होर ।"""

k44_hi = """सद्गुरु ने मुझे वह दिव्य पाठ पढ़ाया, जहाँ दूसरे किसी का कोई अस्तित्व ही नहीं रह गया!  
उन्होंने मुझे उस निरपेक्ष परम सत्य के सौंदर्य के साक्षात दर्शन कराए, और अद्वैत की एकता में परमानंद की गूँज उठ पड़ी!  
अरी सखी! अब भला मुझे कौन पहचानेगा? अब तो मैं कुछ और ही बन गई हूँ!  

वह प्राण-प्रियतम देश-काल की सीमाओं से परे होकर, बाहर और भीतर सर्वत्र साक्षात दिखाई दे रहा है!  
अब मेरा नाम और सांसारिक अस्तित्व का कोई निशान शेष नहीं बचा, द्वैत का सारा झगड़ा और शोर सदा के लिए मिट गया!  
अरी सखी! अब भला मुझे कौन पहचानेगा? अब तो मैं कुछ और ही बन गई हूँ!  

प्यारा प्रीतम जब स्वयं अपना सौंदर्य दिखाता है, तो मस्त फ़क़ीर और कलंदर प्रेम में मतवाले हो जाते हैं!  
हे बुल्ले! अब मेरी आत्मा परमहंसों की दिव्य चाल चलने लगी है, कौओं की भांति सांसारिक कूड़े पर भटकने की चाल अब सदा के लिए छूट गई है!  
अरी सखी! अब भला मुझे कौन पहचानेगा? अब तो मैं कुछ और ही बन गई हूँ!"""

k44_en = """The Divine Guide instructed me in that sacred lore,  
Where duality and "the other" can enter nevermore!  
Unveiling the absolute splendor of the Sovereign Essence divine,  
Where the thunderous ecstasy of Unity makes all realms align!  
Who can ever recognize me now?  
O friends, I have become something else entirely!  

Transcending the bounds of space, He is the Primordial Light,  
Manifest within and without before my wondering sight!  
No trace or earthly name of my former self remains,  
Effaced is all worldly dispute and clamor of chains!  
Who can ever recognize me now?  
O friends, I have become something else entirely!  

When the Beloved reveals His peerless beauty to the soul,  
Ecstatic dervishes drink the cup of madness whole!  
Behold, Bulleh now glides in the graceful dance of the royal swan,  
The awkward hopping of the earthbound crow is forever gone!  
Who can ever recognize me now?  
O friends, I have become something else entirely!"""

batch.append({
    "id": 44,
    "title": "44. हुण मैनूं कौण पछाणे, हुण मैं हो गई नी कुझ होर",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k44_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "हादी मैनूं सबक पढ़ाइआ, ओथे ग़ैर ना आया जाइआ,",
                "hindi_gloss": "हादी (सद्गुरु/मार्गदर्शक ने) मैनूं (मुझको वह) सबक (पाठ) पढ़ाइआ (सिखाया है), ओथे (जहाँ) ग़ैर (द्वैत/दूसरा कोई) ना (न) आया (आ सकता है) जाइआ (न जा सकता है),",
                "english_gloss": "haadee (the True Guide) mainoon (me) sabak (lesson) padhaaia (taught), othe (there) gair (the other/duality) na (not) aaya (entered) jaaia (left),"
            },
            {
                "original": "मतलक ज़ात जमाल विखाइआ, वहदत पाइआ शोर ।",
                "hindi_gloss": "मतलक (परम शुद्ध निरपेक्ष) ज़ात (ब्रह्म-स्वरूप का) जमाल (सौंदर्य) विखाइआ (दिखा दिया), वहदत (उस अद्वैत में) पाइआ (मच गया) शोर (परमानंद का शोर) ।",
                "english_gloss": "matlak (absolute) zaat (essence's) jamaal (splendor) vikhaaia (showed), vahdat (unity) paaia (raised) shor (roar of joy) ."
            },
            {
                "original": "हुण मैनूं कौण पछाणे, हुण मैं हो गई नी कुझ होर ।",
                "hindi_gloss": "हुण (अब) मैनूं (मुझको) कौण (कौन भला) पछाणे (पहचानेगा), हुण (अब) मैं (मैं) हो गई (हो गई हूँ) नी (अरी सखी) कुझ (कुछ) होर (और ही अलौकिक सत्ता) ।",
                "english_gloss": "hun (now) mainoon (me) kaun (who) pachhaane (can recognize), hun (now) main (I) ho gayee (have become) neen (O friend) kujh (something) hor (else entirely) ."
            },
            {
                "original": "अव्वल हो के लामकानी, ज़ाहर बातन दिसदा जानी,",
                "hindi_gloss": "अव्वल (आदि से अंत तक) हो के (होकर) लामकानी (देश-काल से परे ला-मकां), ज़ाहर (बाहर भी) बातन (और भीतर भी) दिसदा (दिखाई देता है) जानी (मेरा प्राण-प्रियतम),",
                "english_gloss": "avval (first and last) ho ke (being) laamakaanee (spaceless/transcendent), zaahar (outwardly) baatan (inwardly) disda (appears) jaanee (Soul's Beloved),"
            },
            {
                "original": "रिहा ना मेरा नाम निशानी, मिट गया झगड़ा शोर ।",
                "hindi_gloss": "रिहा ना (रहा नहीं) मेरा (मेरा) नाम (नाम) निशानी (और सांसारिक अस्तित्व का कोई निशान), मिट गया (मिट गया) झगड़ा (संसार का सारा द्वंद्व और) शोर (शोर) ।",
                "english_gloss": "raha na (remained not) mera (my) naam (name) nishaanee (trace), mit gaya (effaced was) jhagda (conflict) shor (clamor) ."
            },
            {
                "original": "हुण मैनूं कौण पछाणे, हुण मैं हो गई नी कुझ होर ।",
                "hindi_gloss": "हुण (अब) मैनूं (मुझको) कौण (कौन) पछाणे (पहचाने), हुण (अब) मैं (मैं) हो गई (हो गई) नी (अरी) कुझ (कुछ) होर (और) ।",
                "english_gloss": "hun (now) mainoon (me) kaun (who) pachhaane (recognizes), hun (now) main (I) ho gayee (became) neen (O friend) kujh (something) hor (different) ."
            },
            {
                "original": "प्यारा आप जमाल विखाले, मसत कलन्दर होण मतवाले,",
                "hindi_gloss": "प्यारा (मेरा प्यारा प्रियतम) आप (स्वयं अपना) जमाल (अलौकिक सौंदर्य) विखाले (प्रकट करता है), मसत (मस्त) कलन्दर (फ़क़ीर और साधक) होण (हो जाते हैं) मतवाले (प्रेम में मतवाले),",
                "english_gloss": "pyaara (Beloved) aap (Himself) jamaal (splendor) vikhaale (reveals), masat (intoxicated) kalandar (dervishes) hon (become) matwaale (entranced),"
            },
            {
                "original": "हंसां दे हुण वेख लै चाले, बुल्ल्हा कागां दी हुण गई टोर ।",
                "hindi_gloss": "हंसां दे (परमहंसों की) हुण (अब) वेख लै (देख लो) चाले (दिव्य चाल), बुल्ल्हा (हे बुल्ले! अब वासना-रूपी) कागां दी (कौओं की) हुण (अब) गई (छूट गई) टोर (चाल) ।",
                "english_gloss": "hansaan de (of swans) hun (now) vekh lai (behold) chaale (gait/flight), bullha (O Bulleh) kaagaan dee (of crows) hun (now) gayee (departed) tor (waddling) ."
            },
            {
                "original": "हुण मैनूं कौण पछाणे, हुण मैं हो गई नी कुझ होर ।",
                "hindi_gloss": "हुण (अब) मैनूं (मुझको) कौण (कौन) पछाणे (पहचानेगा), हुण (अब) मैं (मैं) हो गई (हो गई हूँ) नी (अरी सखी) कुझ (कुछ) होर (और ही) ।",
                "english_gloss": "hun (now) mainoon (me) kaun (who) pachhaane (can know), hun (now) main (I) ho gayee (have become) neen (O friend) kujh (something) hor (other) ."
            }
        ],
        "hindi_meaning": k44_hi,
        "english_meaning": k44_en
    }]
})

# ==========================================
# KAFI 45: 45. इक अलफ़ पढ़ो छुटकारा ए
# ==========================================
k45_orig = """इक अलफ़ों दो तिन्न चार होए, फिर लक्ख करोड़ हज़ार होए,
फिर उथों बाझों शमार होए, इक अलफ़ दा नुक़्ता न्यारा ए,
इक अलफ़ पढ़ो छुटकारा ए ।

क्यों पढ़ना एं गड्ड किताबां दी, सिर चाना एं पंड अज़ाबां दी,
हुण होइउं शकल जल्लादां दी, अग्गे पैंडा मुशकल भारा ए,
इक अलफ़ पढ़ो छुटकारा ए ।

बण हाफ़ज हिफ़ज कुरान करें, पढ़ पढ़ के साफ़ ज़बान करें,
फिर न्यामत विच ध्यान करें, मन फिरदा ज्युं हलकारा ए,
इक अलफ़ पढ़ो छुटकारा ए ।

बुल्ल्हा बी बोहड़ दा बोया ई उह बिरछ वड्डा जा होया ई,
जद बिरछ उह फ़ानी होया ई फिर रह गया बी अकारा ए,
इक अलफ़ पढ़ो छुटकारा ए ।"""

k45_hi = """एक 'अलिफ़' से दो, तीन और चार बने, फिर हज़ारों, लाखों और करोड़ों रूप बने!  
फिर उससे भी आगे असंख्य रूप फैल गए, पर उस एक 'अलिफ़' का मूल बिंदु सबसे निराला है!  
केवल उस एक 'अलिफ़' का पाठ पढ़ लो, तो समस्त बंधनों से छुटकारा मिल जाएगा!  

गाड़ियाँ भर-भरकर पोथियाँ क्यों पढ़ता है? अपने सिर पर चिंताओं और यातनाओं का यह भारी गट्ठर क्यों ढोता है?  
शाब्दिक ज्ञान के अहंकार से तेरा चेहरा जल्लादों जैसा कठोर हो गया है, जबकि आगे का आध्यात्मिक मार्ग बहुत कठिन और दुर्गम है!  
केवल उस एक 'अलिफ़' का पाठ पढ़ लो, तो समस्त बंधनों से छुटकारा मिल जाएगा!  

हाफ़िज़ बनकर तू सारा क़ुरआन कंठस्थ करता है, और पढ़-पढ़कर अपनी ज़बान को शुद्ध करता है,  
परंतु तेरा ध्यान स्वादिष्ट व्यंजनों और सांसारिक दक्षिणा में लगा रहता है, तेरा मन किसी हरकारे (डाकिए) की तरह भटकता फिरता है!  
केवल उस एक 'अलिफ़' का पाठ पढ़ लो, तो समस्त बंधनों से छुटकारा मिल जाएगा!  

हे बुल्ले! जैसे बरगद का एक छोटा-सा बीज बोया गया, और वह बढ़कर एक विशाल वटवृक्ष बन गया,  
परंतु जब वह भौतिक वृक्ष नष्ट हो गया, तो अंत में केवल वही मूल बीज शेष रह गया!  
केवल उस एक 'अलिफ़' का पाठ पढ़ लो, तो समस्त बंधनों से छुटकारा मिल जाएगा!"""

k45_en = """From the single Alif emerged two, three, and four,  
Then thousands, millions, and myriads more!  
Unfolding into infinite numbers beyond count,  
Yet the single dot of Alif is the peerless fount!  
Read the single letter Alif, and attain liberation complete!  

Why dost thou read cartloads of scriptures and lore,  
Piling heavy bundles of torment upon thy head evermore?  
Thy face has grown grim and harsh like a hangman in pride,  
While the arduous path ahead is treacherous and wide!  
Read the single letter Alif, and attain liberation complete!  

Becoming a Hafiz, thou memorizest the Holy Book with care,  
Polishing thy tongue with holy verses in the air,  
Yet thy wandering mind hungers for delicacies and gold,  
Pacing like a restless courier across the world cold!  
Read the single letter Alif, and attain liberation complete!  

O Bulleh, a tiny seed of the banyan tree was sown in the loam,  
Which spread its vast leafy branches into a mighty home;  
Yet when that sprawling tree withers and turns to clay,  
The primordial seed alone survives the decay!  
Read the single letter Alif, and attain liberation complete!"""

batch.append({
    "id": 45,
    "title": "45. इक अलफ़ पढ़ो छुटकारा ए",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k45_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "इक अलफ़ों दो तिन्न चार होए, फिर लक्ख करोड़ हज़ार होए,",
                "hindi_gloss": "इक अलफ़ों (एक 'अलिफ़' से) दो (दो) तिन्न (तीन) चार (चार संख्याएं) होए (बनीं), फिर (फिर) लक्ख (लाख) करोड़ (करोड़ और) हज़ार (हज़ार) होए (हो गईं),",
                "english_gloss": "ik alafon (from one Alif) do (two) tinn (three) chaar hoe (four arose), phir (then) lakkh (hundred-thousands) karod (crores) hazaar hoe (thousands became),"
            },
            {
                "original": "फिर उथों बाझों शमार होए, इक अलफ़ दा नुक़्ता न्यारा ए,",
                "hindi_gloss": "फिर (फिर) उथों (उससे भी) बाझों शमार (अनगिनत/असंख्य) होए (रूप बन गए), इक (किंतु एक) अलफ़ दा (अलिफ़ का) नुक़्ता (मूल बिंदु) न्यारा (सबसे विलक्षण और अद्वितीय) ए (है),",
                "english_gloss": "phir (then) uthon (therefrom) baajhon shamaar hoe (became beyond counting), ik (one) alaf da (of Alif) nukta (the dot) nyaara (unique/transcendent) e (is),"
            },
            {
                "original": "इक अलफ़ पढ़ो छुटकारा ए ।",
                "hindi_gloss": "इक (केवल एक) अलफ़ (अलिफ़ को) पढ़ो (पढ़ लो तो भवबंधन से) छुटकारा (मुक्ति) ए (है) ।",
                "english_gloss": "ik (one) alaf (Alif) padho (read) chhutkaara (liberation) e (is) ."
            },
            {
                "original": "क्यों पढ़ना एं गड्ड किताबां दी, सिर चाना एं पंड अज़ाबां दी,",
                "hindi_gloss": "क्यों (क्यों) पढ़ना एं (पढ़ता है तू) गड्ड (गाड़ियों भर-भर के) किताबां दी (किताबें), सिर (अपने सिर पर) चाना एं (उठाता है) पंड (भारी गट्ठर) अज़ाबां दी (यातनाओं और चिंताओं का),",
                "english_gloss": "kyon (why) padhna ain (readest thou) gadd kitaabaan dee (cartloads of books), sir (on head) chaana ain (carriest) pand azaabaan dee (bundle of torments),"
            },
            {
                "original": "हुण होइउं शकल जल्लादां दी, अग्गे पैंडा मुशकल भारा ए,",
                "hindi_gloss": "हुण (अहंकार से) होइउं (हो गई है तेरी) शकल (सूरत) जल्लादां दी (जल्लादों जैसी कठोर), अग्गे (आगे परलोक का) पैंडा (मार्ग) मुशकल (अत्यंत दुर्गम और) भारा (भारी) ए (है),",
                "english_gloss": "hun (now) ho-eon (thou hast become) shakal jallaadaan dee (visage of executioners), agge (ahead) painda (the journey) mushkal (difficult) bhaara (arduous) e (is),"
            },
            {
                "original": "इक अलफ़ पढ़ो छुटकारा ए ।",
                "hindi_gloss": "इक (एक) अलफ़ (अलिफ़) पढ़ो (पढ़ो) छुटकारा (मुक्ति) ए (है) ।",
                "english_gloss": "ik (one) alaf (Alif) padho (read) chhutkaara (salvation) e (is) ."
            },
            {
                "original": "बण हाफ़ज हिफ़ज कुरान करें, पढ़ पढ़ के साफ़ ज़बान करें,",
                "hindi_gloss": "बण (बनकर) हाफ़ज (हाफ़िज़) हिफ़ज (कंठस्थ) कुरान करें (क़ुरआन करता है), पढ़ पढ़ के (पढ़-पढ़कर) साफ़ (शुद्ध) ज़बान (अपनी वाणी) करें (करता है),",
                "english_gloss": "ban haafaz (becoming Hafiz) hifaz kuraan karen (memorizest Quran), padh padh ke (reading) saaf zabaan karen (makest tongue pure),"
            },
            {
                "original": "फिर न्यामत विच ध्यान करें, मन फिरदा ज्युं हलकारा ए,",
                "hindi_gloss": "फिर (किंतु मन में) न्यामत (स्वादिष्ट पकवानों और धन-दौलत) विच (में) ध्यान करें (ध्यान अटका रहता है), मन (तेरा मन) फिरदा (भटकता फिरता है) ज्युं (जैसे कोई) हलकारा (डाकिया/संदेशवाहक) ए (है),",
                "english_gloss": "phir (yet) nyaamat vich (upon worldly delicacies) dhyaan karen (focusest), man (mind) phirda (wanders) jyun (like) halkaara (courier) e (is),"
            },
            {
                "original": "इक अलफ़ पढ़ो छुटकारा ए ।",
                "hindi_gloss": "इक (एक) अलफ़ (अलिफ़) पढ़ो (पढ़ो) छुटकारा (मुक्ति) ए (है) ।",
                "english_gloss": "ik (one) alaf (Alif) padho (read) chhutkaara (freedom) e (is) ."
            },
            {
                "original": "बुल्ल्हा बी बोहड़ दा बोया ई उह बिरछ वड्डा जा होया ई,",
                "hindi_gloss": "बुल्ल्हा (हे बुल्ले!) बी (जैसे बीज) बोहड़ दा (बरगद के विशाल वृक्ष का एक सूक्ष्म बीज) बोया ई (बोया गया), उह (वह बढ़कर) बिरछ (विशाल वृक्ष) वड्डा जा (अत्यंत विशाल) होया ई (हो गया),",
                "english_gloss": "bullha (O Bulleh) bee bohad da (seed of banyan) boya ee (was sown), uh birachh (that tree) vadda jaa hoya ee (became immense),"
            },
            {
                "original": "जद बिरछ उह फ़ानी होया ई फिर रह गया बी अकारा ए,",
                "hindi_gloss": "जद (परंतु जब) बिरछ (वह विशाल वृक्ष) उह (वह) फ़ानी (नष्ट/सूख) होया ई (हो गया), फिर (तो अंत में) रह गया (शेष बच गया) बी (वही अविनाशी बीज) अकारा (अपने मूल निराकार स्वरूप में) ए (है) ।",
                "english_gloss": "jad birachh uh (when that tree) faanee hoya ee (perished), phir (then) rah gaya (remained) bee (the seed) akaara (in its formless essence) e (is) ."
            },
            {
                "original": "इक अलफ़ पढ़ो छुटकारा ए ।",
                "hindi_gloss": "इक (एक) अलफ़ (अलिफ़) पढ़ो (पढ़ो) छुटकारा (मुक्ति) ए (है) ।",
                "english_gloss": "ik (one) alaf (Alif) padho (read) chhutkaara (deliverance) e (is) ."
            }
        ],
        "hindi_meaning": k45_hi,
        "english_meaning": k45_en
    }]
})

# Save each Kafi to data/kafian/
for k in batch:
    k_id = k["id"]
    fname = os.path.join(KAFIAN_DIR, f"kafi_{k_id:03d}.json")
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(k, f, ensure_ascii=False, indent=2)
    print(f"Saved {fname}")

# Update checkpoint.json
with open(CHECKPOINT_JSON, "r", encoding="utf-8") as f:
    chk = json.load(f)

chk["completed_ids"] = sorted(list(set(chk["completed_ids"] + [k["id"] for k in batch])))
chk["completed_count"] = len(chk["completed_ids"])
chk["last_updated"] = datetime.now().isoformat()
chk["next_kafi_id"] = max(chk["completed_ids"]) + 1
chk["status"] = "in_progress"

with open(CHECKPOINT_JSON, "w", encoding="utf-8") as f:
    json.dump(chk, f, ensure_ascii=False, indent=2)

print(f"Checkpoint updated: {chk['completed_count']}/160 completed. Next ID: {chk['next_kafi_id']}")

# Update lexicon
if os.path.exists(LEXICON_JSON):
    with open(LEXICON_JSON, "r", encoding="utf-8") as f:
        lexicon = json.load(f)
else:
    lexicon = {}

new_words_count = 0
for k in batch:
    for st in k.get("annotated_stanzas", []):
        for line_item in st.get("lines", []):
            h_gloss = line_item.get("hindi_gloss", "")
            e_gloss = line_item.get("english_gloss", "")
            h_matches = re.findall(r"([^\s\(\)]+)\s*\(([^)]+)\)", h_gloss)
            e_matches = re.findall(r"([^\s\(\)]+)\s*\(([^)]+)\)", e_gloss)
            for i in range(min(len(h_matches), len(e_matches))):
                punj_word = h_matches[i][0].strip("।,").strip()
                hi_meaning = h_matches[i][1].strip()
                en_meaning = e_matches[i][1].strip()
                if punj_word and punj_word not in lexicon:
                    lexicon[punj_word] = {"hi": hi_meaning, "en": en_meaning}
                    new_words_count += 1

with open(LEXICON_JSON, "w", encoding="utf-8") as f:
    json.dump(lexicon, f, ensure_ascii=False, indent=2)

print(f"Lexicon updated: added {new_words_count} new entries, total now {len(lexicon)}")
