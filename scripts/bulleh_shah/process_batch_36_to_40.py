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
# KAFI 36: 36. गुर जो चाहे सो करदा ए
# ==========================================
k36_orig = """मेरे घर विच चोरी होई, सुत्ती रही ना जाग्या कोई,
मैं गुर फड़ सोझी होई, जो माल ग्या सो तरदा ए ।
गुर जो चाहे सो करदा ए ।

पहले मख़फी आप खज़ाना सी, ओथे हैरत हैरतख़ाना सी,
फिर वहदत दे विच आना सी, कुल जुज़ दा मुजमल परदा ए ।
गुर जो चाहे सो करदा ए ।

कुनफईकून आवाज़ां देंदा, वहदत विचों कसरत लैंदा,
पहन लिबास बन्दा बण बहिंदा, कर बन्दगी मसजद वड़दा ए ।
गुर जो चाहे सो करदा ए ।

रोज़ मीसाक अलस्सत सुणावे, कालूबला अज़हद ना चाहवे,
विच कुझ आपना आप छुपावे, उह गिन गिन वसतां धरदा ए ।
गुर जो चाहे सो करदा ए ।

गुर अल्लाह आप कहेंदा ए गुर अली नबी हो बहिंदा ए,
घर हर दे दिल विच रहिंदा ए उह खाली भांडे भरदा ए ।
गुर जो चाहे सो करदा ए ।

बुल्ल्हा शौह नूं घर विच पाइआ, जिस सांगी सांग बणाइआ,
लोकां कोलों भेत छुपाइआ, उह दरस परम दा पढ़दा ए ।
गुर जो चाहे सो करदा ए ।"""

k36_hi = """मेरे घर में एक विचित्र चोरी हो गई, सब सोते रहे और कोई जाग न सका!  
पर जब मैंने सद्गुरु के चरण पकड़े, तब यह भेद समझ में आया: जिसका सब कुछ लुट गया, वही पार तर गया!  
वह सद्गुरु और स्वामी जो चाहे सो करता है!  

सृष्टि से पहले वह एक छिपा हुआ गुप्त खज़ाना था, जहाँ केवल विस्मय और अचंभे का आलम था!  
फिर वह अद्वैत की एकता में प्रकट हुआ, जहाँ व्यष्टि और समष्टि का घूंघट खिंच गया!  
वह सद्गुरु और स्वामी जो चाहे सो करता है!  

उसने 'कुन' (हो जा!) का नाद फूँका, और एकता में से अनेकता की सृष्टि बिखेर दी!  
फिर मनुष्य का चोला पहनकर बैठ गया, और स्वयं अपनी ही बंदगी करने मस्जिद में दाखिल हो गया!  
वह सद्गुरु और स्वामी जो चाहे सो करता है!  

सृष्टि के पहले दिन उसने पूछा था: 'क्या मैं तुम्हारा रब नहीं हूँ?' और रूहों ने पुकारा: 'हाँ, आप ही हमारे रब हैं!'  
इस लीला के बीच उसने अपनी पहचान छिपा रखी है, और गिन-गिन कर रूपों और सांसों को सजा रहा है!  
वह सद्गुरु और स्वामी जो चाहे सो करता है!  

वह गुरु स्वयं को अल्लाह कहता है, वही गुरु नबी और अली बनकर बैठ जाता है!  
वह हर प्राणी के हृदय में बसता है, और जो पात्र खाली होकर आते हैं, उन्हें अमृत से भर देता है!  
वह सद्गुरु और स्वामी जो चाहे सो करता है!  

बुल्ले ने उस स्वामी को अपने घट के भीतर पा लिया है, जिसने बहुरूपिया बनकर यह सारा स्वांग रचा है!  
संसार के अज्ञानियों से उसने यह भेद छिपा रखा है, और अपने ही घट में उस परम सत्य का पाठ पढ़ रहा है!  
वह सद्गुरु और स्वामी जो चाहे सो करता है!"""

k36_en = """A strange, mystical theft transpired within my home—  
While the whole world slumbered, blind beneath heaven's dome!  
When I held fast to the Master's feet, the radiant truth became clear:  
Whosoever loses his worldly baggage is the one who crosses near!  
The Master does whatever He pleases to do!  

In the beginning He was a hidden treasure concealed in sheer delight,  
An unfathomable sanctuary of wonder beyond human sight!  
Then into the realm of Unity He stepped forth to dwell,  
Veiling the cosmos in part and whole with His mystic spell!  
The Master does whatever He pleases to do!  

He sounded the primordial word: Kun!—Be, and it was done!  
Manifesting boundless multiplicity out of the One!  
Donning the fragile garment of flesh, He became a mortal man,  
And walked into the mosque to worship His own eternal plan!  
The Master does whatever He pleases to do!  

On the Day of the Primordial Covenant He whispered: Am I not your Lord?  
And the souls cried out: Yea, Thou art our Sovereign adored!  
Hiding His transcendent essence beneath the masks of time,  
He measures out all entities in a cadence sublime!  
The Master does whatever He pleases to do!  

The Master declares Himself to be Allah, the All-Sovereign and High,  
He sits as the Prophet and Ali beneath the arched sky!  
Dwelling silently in the chamber of every human heart,  
He fills the empty, surrendered chalices with nectar from His art!  
The Master does whatever He pleases to do!  

Bulleh has discovered his Lord right within his own breast,  
The Cosmic Actor who assumed this guise for His divine quest!  
Concealing this secret from the eyes of worldly debate,  
He studies the supreme revelation of His own boundless state!  
The Master does whatever He pleases to do!"""

batch.append({
    "id": 36,
    "title": "36. गुर जो चाहे सो करदा ए",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k36_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "मेरे घर विच चोरी होई, सुत्ती रही ना जाग्या कोई,",
                "hindi_gloss": "मेरे (मेरे) घर (हृदय-घर) विच (में) चोरी (आत्मिक चोरी) होई (हुई), सुत्ती (संसार की मोह-निद्रा में सोती) रही (रही) ना (नहीं) जाग्या (जागा) कोई (कोई भी),",
                "english_gloss": "mere (my) ghar (heart's home) vich (in) choree (spiritual theft) hoee (occurred), suttee (slumbering in delusion) rahee (remained) na (not) jaagya (awakened) koee (anyone),"
            },
            {
                "original": "मैं गुर फड़ सोझी होई, जो माल ग्या सो तरदा ए ।",
                "hindi_gloss": "मैं (जब मैंने) गुर (सद्गुरु के चरण) फड़ (पकड़े तब मुझे) सोझी (आत्म-चेतना की समझ) होई (हुई कि), जो (जो सांसारिक) माल (अहंकार और वासनाओं का धन) ग्या (चोरी चला गया/लूट लिया गया) सो (वही साधक) तरदा (भवसागर से तर जाता) ए (है) ।",
                "english_gloss": "main (I) gur (the Master's feet) phad (grasped) sozhee (illumination/understanding) hoee (dawned that), jo (whatever) maal (wealth of ego/worldly possessions) gya (was taken) so (that soul) tarda (is redeemed/ferried across) e (is) ."
            },
            {
                "original": "गुर जो चाहे सो करदा ए ।",
                "hindi_gloss": "गुर (वह सद्गुरु/परमेश्वर) जो (जो कुछ भी) चाहे (चाहता है) सो (वही सब) करदा (करता) ए (है) ।",
                "english_gloss": "gur (the Master/Divine) jo (whatever) chaahe (wills) so (that He) karda (does) e (does) ."
            },
            {
                "original": "पहले मख़फी आप खज़ाना सी, ओथे हैरत हैरतख़ाना सी,",
                "hindi_gloss": "पहले (सृष्टि से पूर्व वह) मख़फी (गुप्त/अदृश्य) आप (स्वयं एक अप्रकट) खज़ाना (खज़ाना) सी (था), ओथे (वहाँ केवल) हैरत (अकथनीय विस्मय का) हैरतख़ाना (विस्मय-भवन) सी (था),",
                "english_gloss": "pahle (initially) makhfee (hidden) aap (Himself) khazaana (treasure) see (was), othe (there) hairat (wonder) hairatkhaana (abode of awe) see (was),"
            },
            {
                "original": "फिर वहदत दे विच आना सी, कुल जुज़ दा मुजमल परदा ए ।",
                "hindi_gloss": "फिर (तत्पश्चात उसे) वहदत (अद्वैत/एकेश्वरवाद) दे (के) विच (भीतर) आना (प्रकट होना) सी (था), कुल (समस्त विराट्) जुज़ (और अणु-अंश) दा (का) मुजमल (गूढ़ संक्षेपीकरण का) परदा (रहस्य-पर्दा) ए (है) ।",
                "english_gloss": "phir (then) vahdat (Unity) de (of) vich (in) aana (to enter) see (was), kul (the whole) juz (the part) da (of) mujmal (summary/unfolded) parda (veil) e (is) ."
            },
            {
                "original": "गुर जो चाहे सो करदा ए ।",
                "hindi_gloss": "गुर (सद्गुरु) जो (जो) चाहे (चाहता है) सो (वही) करदा (करता) ए (है) ।",
                "english_gloss": "gur (the Master) jo (whatever) chaahe (wills) so (that) karda (does) e (does) ."
            },
            {
                "original": "कुनफईकून आवाज़ां देंदा, वहदत विचों कसरत लैंदा,",
                "hindi_gloss": "कुनफईकून ('कुन फयकून' / हो जा और वह हो गया की) आवाज़ां (आवाज़/आज्ञा) देंदा (देता है), वहदत (उस अद्वैत में) विचों (से) कसरत (सृष्टि की अनेकरूपता/बहुलता) लैंदा (प्रकट कर लेता है),",
                "english_gloss": "kunfayeekoon ('Kun fayakun' - 'Be, and it is') aavaazaan (voices/command) denda (gives), vahdat (from Unity) vichon (out of) kasrat (multiplicity) lainda (brings forth),"
            },
            {
                "original": "पहन लिबास बन्दा बण बहिंदा, कर बन्दगी मसजद वड़दा ए ।",
                "hindi_gloss": "पहन (पहनकर) लिबास (मानव चोला) बन्दा (दास/मनुष्य) बण (बनकर) बहिंदा (बैठ जाता है), कर (करके) बन्दगी (स्वयं अपनी ही बंदगी) मसजद (मस्जिद में) वड़दा (प्रवेश करता) ए (है) ।",
                "english_gloss": "pahan (donning) libaas (garb of flesh) banda (mortal servant) ban (becoming) bahinda (sits), kar (performing) bandagee (devotion/worship) masjad (mosque) vad-da (enters) e (does) ."
            },
            {
                "original": "गुर जो चाहे सो करदा ए ।",
                "hindi_gloss": "गुर (परम गुरु) जो (जो) चाहे (चाहता है) सो (वही) करदा (करता) ए (है) ।",
                "english_gloss": "gur (the Master) jo (whatever) chaahe (wills) so (that) karda (does) e (does) ."
            },
            {
                "original": "रोज़ मीसाक अलस्सत सुणावे, कालूबला अज़हद ना चाहवे,",
                "hindi_gloss": "रोज़ मीसाक (सृष्टि के आदि-दिन) अलस्सत ('अलस्तु बिरब्बिकुम' - क्या मैं तुम्हारा रब नहीं हूँ?) सुणावे (सुनाता है), कालूबला ('क़ालू बला' - हाँ, आप ही हमारे प्रभु हैं) अज़हद (सीमा से परे) ना (अन्य किसी को नहीं) चाहवे (चाहता),",
                "english_gloss": "roz meesaak (Day of the Primordial Covenant) alas-sat ('Alastu bi-rabbikum' - Am I not your Lord?) sunaave (recites), kaaloobala ('Qalu bala' - Yea, Thou art!) azhad (infinitely) na (none other) chaahve (desires),"
            },
            {
                "original": "विच कुझ आपना आप छुपावे, उह गिन गिन वसतां धरदा ए ।",
                "hindi_gloss": "विच (इस लीला के बीच) कुझ (कुछ) आपना (अपना वास्तविक स्वरूप) आप (स्वयं) छुपावे (छिपा लेता है), उह (और वह) गिन (गिन) गिन (गिनकर) वसतां (पदार्थों और उपाधियों को) धरदा (सजाता) ए (है) ।",
                "english_gloss": "vich (amidst this) kujh (somewhat) aapna (His own true nature) aap (Himself) chhupaave (conceals), uh (He) gin (counting) gin (and measuring) vastaan (objects/manifestations) dharda (places) e (does) ."
            },
            {
                "original": "गुर जो चाहे सो करदा ए ।",
                "hindi_gloss": "गुर (सद्गुरु) जो (जो) चाहे (चाहता है) सो (वही) करदा (करता) ए (है) ।",
                "english_gloss": "gur (the Master) jo (whatever) chaahe (wills) so (that) karda (does) e (does) ."
            },
            {
                "original": "गुर अल्लाह आप कहेंदा ए गुर अली नबी हो बहिंदा ए,",
                "hindi_gloss": "गुर (सद्गुरु) अल्लाह (स्वयं अल्लाह) आप (स्वयं को) कहेंदा (कहलाता) ए (है), गुर (वही गुरु) अली (हज़रत अली और) नबी (पैग़ंबर का रूप) हो (होकर) बहिंदा (विराजमान होता) ए (है),",
                "english_gloss": "gur (the Master) allaah (Allah Himself) aap (Himself) kahenda (calls) e (does), gur (the Master) alee (Ali) nabee (the Prophet) ho (becoming) bahinda (abides) e (does),"
            },
            {
                "original": "घर हर दे दिल विच रहिंदा ए उह खाली भांडे भरदा ए ।",
                "hindi_gloss": "घर (प्रत्येक के घट-घर में) हर दे (हर प्राणी के) दिल (हृदय) विच (में) रहिंदा (विराजता) ए (है), उह (वह) खाली (रिक्त पड़े) भांडे (हृदय-पात्रों को अमृत से) भरदा (भर देता) ए (है) ।",
                "english_gloss": "ghar (home) har de (of everyone) dil (heart) vich (within) rahinda (dwells) e (does), uh (He) khaalee (empty) bhaande (vessels) bharda (fills) e (does) ."
            },
            {
                "original": "गुर जो चाहे सो करदा ए ।",
                "hindi_gloss": "गुर (सद्गुरु) जो (जो) चाहे (चाहता है) सो (वही) करदा (करता) ए (है) ।",
                "english_gloss": "gur (the Master) jo (whatever) chaahe (wills) so (that) karda (does) e (does) ."
            },
            {
                "original": "बुल्ल्हा शौह नूं घर विच पाइआ, जिस सांगी सांग बणाइआ,",
                "hindi_gloss": "बुल्ल्हा (बुल्ले ने) शौह (अपने प्राण-स्वामी को) नूं (को) घर (अपने अंतःकरण के भीतर ही) पाइआ (पा लिया है), जिस (जिसने यह) सांगी (बहुरूपिया बनकर) सांग (संसार का स्वांग/वेश) बणाइआ (रचा है),",
                "english_gloss": "bullha (Bulleh) shauh (the Lord) noon (unto) ghar (home of the heart) vich (in) paaia (has found), jis (who as) saangee (actor) saang (cosmic guise) banaaia (assumed),"
            },
            {
                "original": "लोकां कोलों भेत छुपाइआ, उह दरस परम दा पढ़दा ए ।",
                "hindi_gloss": "लोकां (संसार के लोगों) कोलों (से) भेत (इस रहस्य को) छुपाइआ (छिपाकर रखा है), उह (और वह स्वयं ही) दरस (परम दर्शन का) परम (सर्वोच्च पाठ) दा (का) पढ़दा (अध्ययन करता) ए (है) ।",
                "english_gloss": "lokaan (from the world) kolon (from) bhet (the mystery) chhupaaia (hid), uh (He) daras (vision/lesson) param (supreme) da (of) padhda (reads/studies) e (does) ."
            },
            {
                "original": "गुर जो चाहे सो करदा ए ।",
                "hindi_gloss": "गुर (सद्गुरु परमात्मा) जो (जो) चाहे (चाहता है) सो (वही) करदा (करता) ए (है) ।",
                "english_gloss": "gur (the Master) jo (whatever) chaahe (wills) so (that) karda (does) e (does) ."
            }
        ],
        "hindi_meaning": k36_hi,
        "english_meaning": k36_en
    }]
})

# ==========================================
# KAFI 37: 37. हाजी लोक मक्के नूं जांदे
# ==========================================
k37_orig = """हाजी लोक मक्के नूं जांदे,
मेरा रांझा माही मक्का,
नी मैं कमली हां ।

मैं ते मंग रांझे दी होईआं,
मेरा बाबल करदा धक्का,
नी मैं कमली हां ।

हाजी लोक मक्के वल्ल जांदे,
मेरे घर विच नौशोह मक्का,
नी मैं कमली हां ।

विचे हाजी विचे गाजी,
विचे चोर उचक्का,
नी मैं कमली हां ।

हाजी लोक मक्के वल्ल जांदे,
असां जाणा तख़त हज़ारे,
नी मैं कमली हां ।

जित वल्ल यार उते वल्ल कअबा,
भावें फोल किताबां चारे,
नी मैं कमली हां ।"""

k37_hi = """हज के यात्री काबा-मक्का की ओर जाते हैं,  
परंतु मेरा प्यारा रांझा ही मेरा मक्का है—अरी सखी, मैं तो प्रेम में बावरी हो गई हूँ!  

मैं तो अपने रांझा के नाम पर ब्याही जा चुकी हूँ,  
पर मेरा सांसारिक पिता ज़बरदस्ती किसी और से बाँधना चाहता है—अरी सखी, मैं तो बावरी हो गई हूँ!  

हज के यात्री मरुस्थल के मक्के की ओर भागते हैं,  
परंतु मेरे हृदय-घर में ही मेरा नित्य-नूतन दूल्हा-रूपी मक्का विराज रहा है—अरी सखी, मैं तो बावरी हो गई हूँ!  

इसी अंतःकरण में सच्चा हाजी है, इसी में मन को जीतने वाला ग़ाज़ी है,  
और इसी में विषय-वासनाओं को चुराने वाला चोर-उचक्का भी है—अरी सखी, मैं तो बावरी हो गई हूँ!  

हज के यात्री मक्के की ओर दौड़ते हैं,  
परंतु मुझे तो मेरे प्रीतम के पावन धाम 'तख़्त हज़ारा' जाना है—अरी सखी, मैं तो बावरी हो गई हूँ!  

जिधर मेरा यार खड़ा है, ठीक उसी दिशा में मेरा काबा है,  
चाहे चारों आसमानी किताबें (तौरेत, ज़बूर, इंजील और क़ुरआन) खोलकर देख लो—अरी सखी, मैं तो प्रेम में बावरी हो गई हूँ!"""

k37_en = """Pious pilgrims journey across desert sands to Mecca's shrine,  
Yet Ranjha, my Beloved, is the sole holy Kaaba of mine—  
O companions, crazed with divine love am I!  

To my Beloved Ranjha I have given my betrothal vow,  
Yet my earthly father forces worldly bonds upon me now—  
O companions, crazed with divine love am I!  

Pilgrims hasten toward distant walls of brick and stone,  
Yet within the sanctuary of my heart dwells the radiant Bridegroom alone—  
O companions, crazed with divine love am I!  

Within this very breast dwells the pilgrim, within is the warrior of grace,  
And within also lurks the stealthy thief of illusion’s embrace—  
O companions, crazed with divine love am I!  

Worldly pilgrims journey to Mecca far away,  
Yet to Takht Hazara, my lover's realm, I must hasten today—  
O companions, crazed with divine love am I!  

Whichever way my Beloved turns His gaze, that direction is my Kaaba true,  
Search through all four holy scriptures, and you will find this testament anew—  
O companions, crazed with divine love am I!"""

batch.append({
    "id": 37,
    "title": "37. हाजी लोक मक्के नूं जांदे",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k37_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "हाजी लोक मक्के नूं जांदे,",
                "hindi_gloss": "हाजी (हज के यात्री) लोक (लोग) मक्के (मक्का शरीफ़) नूं (की ओर) जांदे (जाते हैं),",
                "english_gloss": "haajee (pilgrims) lok (people) makke (to Mecca) noon (unto) jaande (go),"
            },
            {
                "original": "मेरा रांझा माही मक्का,",
                "hindi_gloss": "मेरा (मेरा तो) रांझा (प्यारा रांझा) माही (ही मेरा सच्चा) मक्का (काबा/मक्का है),",
                "english_gloss": "mera (my) raanjha (Ranjha) maahi (the Beloved) makka (is Mecca),"
            },
            {
                "original": "नी मैं कमली हां ।",
                "hindi_gloss": "नी (अरी सखी) मैं (मैं प्रेम में) कमली (बावरी/मतवाली) हां (हूँ) ।",
                "english_gloss": "neen (O friend) main (I) kamlee (crazed with love) haan (am) ."
            },
            {
                "original": "मैं ते मंग रांझे दी होईआं,",
                "hindi_gloss": "मैं (मैं) ते (तो) मंग (वाग्दत्ता/मंगेतर) रांझे (रांझा) दी (की) होईआं (हो चुकी हूँ),",
                "english_gloss": "main (I) te (indeed) mang (betrothed) raanjhe (of Ranjha) dee (of) hoee-aan (have become),"
            },
            {
                "original": "मेरा बाबल करदा धक्का,",
                "hindi_gloss": "मेरा (किंतु मेरा) बाबल (सांसारिक पिता) करदा (करता है) धक्का (अन्याय/ज़बरदस्ती),",
                "english_gloss": "mera (my) baabal (father) karda (does) dhakka (injustice/forceful constraint),"
            },
            {
                "original": "नी मैं कमली हां ।",
                "hindi_gloss": "नी (अरी सखी) मैं (मैं) कमली (बावरी) हां (हूँ) ।",
                "english_gloss": "neen (O friend) main (I) kamlee (crazed) haan (am) ."
            },
            {
                "original": "हाजी लोक मक्के वल्ल जांदे,",
                "hindi_gloss": "हाजी (हज करने वाले) लोक (लोग) मक्के (मक्का) वल्ल (की ओर) जांदे (जाते हैं),",
                "english_gloss": "haajee (pilgrims) lok (people) makke (toward Mecca) vall (direction) jaande (journey),"
            },
            {
                "original": "मेरे घर विच नौशोह मक्का,",
                "hindi_gloss": "मेरे (मेरे) घर (हृदय-घर) विच (में ही) नौशोह (नित्य नवीन दूल्हा/प्रभु ही) मक्का (सच्चा मक्का है),",
                "english_gloss": "mere (my) ghar (home) vich (within) naushauh (the eternal Bridegroom) makka (is Mecca),"
            },
            {
                "original": "नी मैं कमली हां ।",
                "hindi_gloss": "नी (अरी सखी) मैं (मैं) कमली (बावरी) हां (हूँ) ।",
                "english_gloss": "neen (O friend) main (I) kamlee (ecstatic) haan (am) ."
            },
            {
                "original": "विचे हाजी विचे गाजी,",
                "hindi_gloss": "विचे (उसी अंतःकरण में) हाजी (सच्चा हाजी है) विचे (उसी में) गाजी (इंद्रियों को जीतने वाला सच्चा ग़ाज़ी है),",
                "english_gloss": "viche (within is) haajee (the pilgrim) viche (within is) gaazee (the spiritual warrior),"
            },
            {
                "original": "विचे चोर उचक्का,",
                "hindi_gloss": "विचे (और उसी में मन रूपी) चोर (चोर और) उचक्का (उचक्का भी छिपा है),",
                "english_gloss": "viche (within is) chor (the thief) uchakka (the rogue/swindler of illusion),"
            },
            {
                "original": "नी मैं कमली हां ।",
                "hindi_gloss": "नी (अरी सखी) मैं (मैं) कमली (दीवानी) हां (हूँ) ।",
                "english_gloss": "neen (O friend) main (I) kamlee (crazed) haan (am) ."
            },
            {
                "original": "हाजी लोक मक्के वल्ल जांदे,",
                "hindi_gloss": "हाजी (हज के यात्री) लोक (लोग) मक्के (मक्का की) वल्ल (ओर) जांदे (जाते हैं),",
                "english_gloss": "haajee (pilgrims) lok (folk) makke (Mecca) vall (toward) jaande (go),"
            },
            {
                "original": "असां जाणा तख़त हज़ारे,",
                "hindi_gloss": "असां (हमें तो) जाणा (जाना है) तख़त हज़ारे (रांझा के दिव्य धाम तख़्त हज़ारा),",
                "english_gloss": "asaan (we) jaana (have to go) takhat hazaare (to Takht Hazara / Beloved's home),"
            },
            {
                "original": "नी मैं कमली हां ।",
                "hindi_gloss": "नी (अरी सखी) मैं (मैं) कमली (बावरी) हां (हूँ) ।",
                "english_gloss": "neen (O friend) main (I) kamlee (crazed) haan (am) ."
            },
            {
                "original": "जित वल्ल यार उते वल्ल कअबा,",
                "hindi_gloss": "जित (जिस) वल्ल (ओर मेरा) यार (प्रियतम है) उते (उसी) वल्ल (ओर मेरा सच्चा) कअबा (काबा है),",
                "english_gloss": "jit (whichever) vall (direction) yaar (Beloved is) ute (in that very) vall (direction) kaaba (is Kaaba),"
            },
            {
                "original": "भावें फोल किताबां चारे,",
                "hindi_gloss": "भावें (चाहे तुम) फोल (खंगाल कर देख लो) किताबां (धर्मग्रंथों की) चारे (चारों पवित्र किताबें),",
                "english_gloss": "bhaaven (even if) phol (you search through) kitaabaan (holy scriptures) chaare (all four books),"
            },
            {
                "original": "नी मैं कमली हां ।",
                "hindi_gloss": "नी (अरी सखी) मैं (मैं प्रेम में) कमली (बावरी) हां (हूँ) ।",
                "english_gloss": "neen (O friend) main (I) kamlee (crazed with love) haan (am) ."
            }
        ],
        "hindi_meaning": k37_hi,
        "english_meaning": k37_en
    }]
})

# ==========================================
# KAFI 38: 38. हत्थी ढिलक गई मेरे चरखे दी, हुण मैथों कत्त्या ना जावे
# ==========================================
k38_orig = """हुण दिन-चढ़आ कद होवे, मैनूं प्यारा मूंह दिखलावे,
तकले नूं वल पै पै जांदे, कौण लुहार लिआवे,
हत्थी ढिलक गई मेरे चरखे दी, हुण मैथों कत्त्या ना जावे ।

तक्कल्युं वल कढ्ढ लुहारा, तन्द चलेंदा नाहीं,
घड़ी घड़ी इह झोला खांदा, छल्ली कित बिध लाहवे,
हत्थी ढिलक गई मेरे चरखे दी, हुण मैथों कत्त्या ना जावे ।

पलीता नहीं जे बीड़ी बन्नहां, बायड़ हत्थ ना आवे,
चमड़्यां नूं चोपड़ नाहीं, माहल पई बतलावे,
हत्थी ढिलक गई मेरे चरखे दी, हुण मैथों कत्त्या ना जावे ।

त्रिंजन कत्तन सद्दण सईआं, बिरहों ढोल बजावे,
तीली नहीं जो पूणियां वट्टां, वच्छा गोहड़े खावे,
हत्थी ढिलक गई मेरे चरखे दी, हुण मैथों कत्त्या ना जावे ।

माही छिड़ गया नाल महीं दे, हुण कत्तन किस नूं भावे,
जित्त वल्ल यार उते वल्ल अक्खियां, मेरा दिल बेले वल्ल धावे,
हत्थी ढिलक गई मेरे चरखे दी, हुण मैथों कत्त्या ना जावे ।

अरज़ एहो मैनूं आण मिले हुण, कौण वसीला जावे,
सै मणां दा कत्त लया बुल्ल्हा, शहु मैनूं गल लावे,
हत्थी ढिलक गई मेरे चरखे दी, हुण मैथों कत्त्या ना जावे ।"""

k38_hi = """अब कब सबेरा होगा जब मेरा प्यारा मुझे अपना मुख दिखलाएगा?  
मेरी चरखे की तकली में बार-बार बल पड़ जाता है, भला कौन लोहार को बुलाकर लाए?  
मेरे चरखे की हत्थी ढीली पड़ गई है, अब मुझसे सूत काता नहीं जाता!  

हे लोहार! इस तकली का टेढ़ापन निकाल दे, इससे धागा आगे नहीं बढ़ता!  
घड़ी-घड़ी यह चरखा हिचकोले खाता है, भला इस पर सूत की पिंडी कैसे उतारी जाए?  
मेरे चरखे की हत्थी ढीली पड़ गई है, अब मुझसे सूत काता नहीं जाता!  

न तो मेरे पास पलीता है जिससे तकली का बंधन बाँधूँ, और न धुरी का धागा हाथ आता है!  
चमड़े के पुर्जों में तेल-चिकनाई नहीं रही, डोरी बार-बार उतर कर गिरती है!  
मेरे चरखे की हत्थी ढीली पड़ गई है, अब मुझसे सूत काता नहीं जाता!  

सखियाँ त्रिंजन (कताई-सभा) में कातने के लिए बुलाती हैं, पर मेरे सीने में विरह का ढोल बज रहा है!  
सलाई नहीं है जिससे कपास की पूनियाँ बनाऊँ, और बछड़ा आकर कपास के गोलों को खा जाता है!  
मेरे चरखे की हत्थी ढीली पड़ गई है, अब मुझसे सूत काता नहीं जाता!  

मेरा माही भैंसों को लेकर चराने निकल गया है, अब सूत कातना भला किसे भाए?  
जिधर मेरा साजन गया है, उधर ही मेरी आँखें लगी हैं, मेरा दिल जंगल के कछार की ओर दौड़ा जाता है!  
मेरे चरखे की हत्थी ढीली पड़ गई है, अब मुझसे सूत काता नहीं जाता!  

मेरी तो बस यही प्रार्थना है कि मेरा साजन अब आकर मुझसे मिल जाए, भला कौन दूत बनकर संदेश ले जाएगा?  
बुल्ले ने तो प्रेम में सैकड़ों मन सूत कात लिया है, काश अब मेरे प्राण-स्वामी आकर मुझे गले लगा लें!  
मेरे चरखे की हत्थी ढीली पड़ गई है, अब मुझसे सूत काता नहीं जाता!"""

k38_en = """When will the dawn break that my Beloved may reveal His face?  
The spindle of my wheel twists with every turn in painful grace;  
Who will fetch the blacksmith to make this spindle straight?  
The handle of my spinning wheel has loosened—no longer can I spin or wait!  

Remove the kink from the iron spindle, O blacksmith, the thread will not draw,  
With every rotation the wheel wobbles and falters without law!  
How can the yarn be lifted from the reeling spool today?  
The handle of my spinning wheel has loosened—no longer can I spin or wait!  

I lack the binding cord to tie the spindle secure,  
The axle thread slips from my fingers, frail and unsure!  
The leather bearings run dry without drops of soothing oil,  
The drive-belt drops away, mocking my futile toil!  
The handle of my spinning wheel has loosened—no longer can I spin or wait!  

Companions call me to join the spinning circle in cheerful pride,  
Yet the relentless drum of separation resounds inside!  
I have no reed to roll the soft cotton slivers fine,  
While straying calves devour the raw bolls of mine!  
The handle of my spinning wheel has loosened—no longer can I spin or wait!  

My sweet herdsman has wandered far with the cattle into the meadow wild,  
Who can sit and spin when the heart is captivated like a child?  
Wherever my Beloved wanders, my gazing eyes pursue,  
My soul flies across the thickets of the river-forest true!  
The handle of my spinning wheel has loosened—no longer can I spin or wait!  

My sole, burning plea is that He return and take my hand,  
Who will carry my secret message across the barren land?  
Bulleh has spun hundreds of maunds of devotional thread in pain,  
May the Lord press me to His bosom and end this yearning rain!  
The handle of my spinning wheel has loosened—no longer can I spin or wait!"""

batch.append({
    "id": 38,
    "title": "38. हत्थी ढिलक गई मेरे चरखे दी, हुण मैथों कत्त्या ना जावे",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k38_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "हुण दिन-चढ़आ कद होवे, मैनूं प्यारा मूंह दिखलावे,",
                "hindi_gloss": "हुण (अब) दिन-चढ़आ (भोर का सूर्योदय) कद (कब) होवे (होगा कि), मैनूं (मुझको) प्यारा (मेरा प्यारा प्रीतम) मूंह (अपना श्रीमुख) दिखलावे (दिखाएगा),",
                "english_gloss": "hun (now) din-chadha (dawn/sunrise) kad (when) hove (shall be that), mainoon (unto me) pyaara (the Beloved) moonh (face) dikhlaave (shows),"
            },
            {
                "original": "तकले नूं वल पै पै जांदे, कौण लुहार लिआवे,",
                "hindi_gloss": "तकले (चरखे की तकली) नूं (में) वल (बल/टेढ़ापन) पै (पड़) पै (पड़) जांदे (जाता है), कौण (भला कौन) लुहार (लोहार को) लिआवे (बुलाकर लाए),",
                "english_gloss": "takle (spindle) noon (unto) val (bends/twists) pai (falling) pai (falling) jaande (keep getting), kaun (who) luhaar (blacksmith) liaave (shall fetch),"
            },
            {
                "original": "हत्थी ढिलक गई मेरे चरखे दी, हुण मैथों कत्त्या ना जावे ।",
                "hindi_gloss": "हत्थी (हत्थी/हैंडल) ढिलक गई (ढीली पड़ गई है) मेरे (मेरे) चरखे (चरखे) दी (की), हुण (अब) मैथों (मुझसे सूत) कत्त्या (काता) ना (नहीं) जावे (जाता) ।",
                "english_gloss": "hatthee (the handle) dhilak gayee (has grown loose) mere (my) charkhe (spinning wheel's) dee (of), hun (now) maithon (by me) kattya (spun) na (not) jaave (can be) ."
            },
            {
                "original": "तक्कल्युं वल कढ्ढ लुहारा, तन्द चलेंदा नाहीं,",
                "hindi_gloss": "तक्कल्युं (तकली में से) वल (बल/मुड़ाव) कढ्ढ (निकाल दो) लुहारा (हे लोहार), तन्द (सूत का धागा) चलेंदा (चल) नाहीं (नहीं पाता),",
                "english_gloss": "takkalyun (from the spindle) val (kink/twist) kaddh (remove) luhaara (O blacksmith), tand (the thread) chalenda (draws/moves) naaheen (not),"
            },
            {
                "original": "घड़ी घड़ी इह झोला खांदा, छल्ली कित बिध लाहवे,",
                "hindi_gloss": "घड़ी (घड़ी) घड़ी (घड़ी) इह (यह चरखा) झोला (झटके) खांदा (खाता है), छल्ली (सूत की अट्टी/पिंडी) कित (किस) बिध (विधि से) लाहवे (उतारी जा सके),",
                "english_gloss": "ghadee (moment) ghadee (by moment) eh (this wheel) jhola (jolts) khaanda (takes), chhallee (spool/skein) kit (which) bidh (manner) laahve (can be unspooled),"
            },
            {
                "original": "हत्थी ढिलक गई मेरे चरखे दी, हुण मैथों कत्त्या ना जावे ।",
                "hindi_gloss": "हत्थी (हत्थी) ढिलक गई (ढीली हो गई) मेरे (मेरे) चरखे (चरखे) दी (की), हुण (अब) मैथों (मुझसे) कत्त्या (सूत काता) ना (नहीं) जावे (जाता) ।",
                "english_gloss": "hatthee (handle) dhilak gayee (loosened) mere (my) charkhe (wheel's) dee (of), hun (now) maithon (by me) kattya (spun) na (not) jaave (can be) ."
            },
            {
                "original": "पलीता नहीं जे बीड़ी बन्नहां, बायड़ हत्थ ना आवे,",
                "hindi_gloss": "पलीता (सूत का बंध) नहीं (नहीं है) जे (कि) बीड़ी (तकली का बंधन) बन्नहां (बाँधूँ), बायड़ (धुरी का धागा) हत्थ (हाथ) ना (नहीं) आवे (आता),",
                "english_gloss": "paleeta (wick/cord) naaheen (not) je (that) beedee (spindle brace) bannhaan (I may bind), baayad (spindle axis cord) hatth (in hand) na (not) aave (comes),"
            },
            {
                "original": "चमड़्यां नूं चोपड़ नाहीं, माहल पई बतलावे,",
                "hindi_gloss": "चमड़्यां (चरखे के चर्म-पुर्ज़ों) नूं (में) चोपड़ (चिकनाई/तेल) नाहीं (नहीं रही), माहल (चमड़े की डोरी) पई (गिरकर) बतलावे (कमज़ोरी दर्शाती है),",
                "english_gloss": "chamdyaan (leather bearings) noon (unto) chopad (lubrication/oil) naaheen (not), maahal (driving belt) payee (slipping) batlaave (tells of decay),"
            },
            {
                "original": "हत्थी ढिलक गई मेरे चरखे दी, हुण मैथों कत्त्या ना जावे ।",
                "hindi_gloss": "हत्थी (हत्थी) ढिलक गई (ढीली पड़ गई) मेरे (मेरे) चरखे (चरखे) दी (की), हुण (अब) मैथों (मुझसे) कत्त्या (काता) ना (नहीं) जावे (जाता) ।",
                "english_gloss": "hatthee (handle) dhilak gayee (loosened) mere (my) charkhe (wheel's) dee (of), hun (now) maithon (by me) kattya (spun) na (not) jaave (can be) ."
            },
            {
                "original": "त्रिंजन कत्तन सद्दण सईआं, बिरहों ढोल बजावे,",
                "hindi_gloss": "त्रिंजन (सामूहिक कताई-सभा में) कत्तन (सूत कातने के लिए) सद्दण (बुलाती हैं) सईआं (सहेलियाँ), बिरहों (परंतु विरह का) ढोल (ढोल मेरे हृदय में) बजावे (बज रहा है),",
                "english_gloss": "trinjan (spinning circle) kattan (to spin) saddan (invite) saeeyaan (companions), birhon (of separation) dhol (drum) bajaave (beats),"
            },
            {
                "original": "तीली नहीं जो पूणियां वट्टां, वच्छा गोहड़े खावे,",
                "hindi_gloss": "तीली (सलाई) नहीं (नहीं है) जो (जिससे) पूणियां (कपास की पूनियाँ) वट्टां (बना सकूँ), वच्छा (बछड़ा) गोहड़े (कपास के गोलों को) खावे (चबाए जा रहा है),",
                "english_gloss": "teelee (straw rod) naaheen (not) jo (with which) pooneeyaan (cotton rolls) vattan (I may roll), vachha (calf) gohde (cotton bolls) khaave (eats),"
            },
            {
                "original": "हत्थी ढिलक गई मेरे चरखे दी, हुण मैथों कत्त्या ना जावे ।",
                "hindi_gloss": "हत्थी (हत्थी) ढिलक गई (ढीली पड़ गई) मेरे (मेरे) चरखे (चरखे) दी (की), हुण (अब) मैथों (मुझसे) कत्त्या (काता) ना (नहीं) जावे (जाता) ।",
                "english_gloss": "hatthee (handle) dhilak gayee (loosened) mere (my) charkhe (wheel's) dee (of), hun (now) maithon (by me) kattya (spun) na (not) jaave (can be) ."
            },
            {
                "original": "माही छिड़ गया नाल महीं दे, हुण कत्तन किस नूं भावे,",
                "hindi_gloss": "माही (मेरा प्रियतम रांझा) छिड़ गया (चला गया) नाल (साथ) महीं (भैंसों) दे (के चराने), हुण (अब भला) कत्तन (सूत कातना) किस (किसे) नूं (को) भावे (रुचेगा),",
                "english_gloss": "maahi (Beloved) chhid gya (has departed) naal (with) maheen (the buffaloes) de (of), hun (now) kattan (spinning) kis (whom) noon (unto) bhaave (pleases),"
            },
            {
                "original": "जित्त वल्ल यार उते वल्ल अक्खियां, मेरा दिल बेले वल्ल धावे,",
                "hindi_gloss": "जित्त (जिस) वल्ल (ओर मेरा) यार (यार है) उते (उसी) वल्ल (ओर मेरी) अक्खियां (आँखें लगी हैं), मेरा (मेरा) दिल (मन) बेले (नदी के कछार/जंगल) वल्ल (की ओर) धावे (दौड़ा जाता है),",
                "english_gloss": "jitt (whichever) vall (direction) yaar (Beloved is) ute (in that very) vall (direction) akkheeyaan (eyes gaze), mera (my) dil (heart) bele (to the river grove) vall (toward) dhaave (runs),"
            },
            {
                "original": "हत्थी ढिलक गई मेरे चरखे दी, हुण मैथों कत्त्या ना जावे ।",
                "hindi_gloss": "हत्थी (हत्थी) ढिलक गई (ढीली हो गई) मेरे (मेरे) चरखे (चरखे) दी (की), हुण (अब) मैथों (मुझसे) कत्त्या (सूत) ना (नहीं) जावे (जाता) ।",
                "english_gloss": "hatthee (handle) dhilak gayee (loosened) mere (my) charkhe (wheel's) dee (of), hun (now) maithon (by me) kattya (spun) na (not) jaave (can be) ."
            },
            {
                "original": "अरज़ एहो मैनूं आण मिले हुण, कौण वसीला जावे,",
                "hindi_gloss": "अरज़ (मेरी तो बस यही प्रार्थना) एहो (है कि) मैनूं (मुझसे) आण (आकर) मिले (मिल जाए) हुण (अब), कौण (कौन भला) वसीला (मध्यस्थ/दूत बनकर) जावे (जाएगा),",
                "english_gloss": "araz (plea) eho (this alone) mainoon (me) aan (coming) mile (meet) hun (now), kaun (who) vaseela (mediator/messenger) jaave (shall go),"
            },
            {
                "original": "सै मणां दा कत्त लया बुल्ल्हा, शहु मैनूं गल लावे,",
                "hindi_gloss": "सै (सैकड़ों) मणां (मन सूत) दा (का) कत्त लया (कात लिया है) बुल्ल्हा (बुल्ले ने), शहु (अब तो प्राण-स्वामी) मैनूं (मुझे) गल (गले से) लावे (लगा लें) ।",
                "english_gloss": "sai (hundreds) manaan (of maunds of yarn) da (of) katt laya (has spun) bullha (Bulleh), shahu (the Lord) mainoon (me) gal (to His bosom) laave (may embrace) ."
            },
            {
                "original": "हत्थी ढिलक गई मेरे चरखे दी, हुण मैथों कत्त्या ना जावे ।",
                "hindi_gloss": "हत्थी (हत्थी) ढिलक गई (ढीली हो गई) मेरे (मेरे) चरखे (चरखे) दी (की), हुण (अब) मैथों (मुझसे) कत्त्या (सूत काता) ना (नहीं) जावे (जाता) ।",
                "english_gloss": "hatthee (handle) dhilak gayee (loosened) mere (my) charkhe (wheel's) dee (of), hun (now) maithon (by me) kattya (spun) na (not) jaave (can be) ."
            }
        ],
        "hindi_meaning": k38_hi,
        "english_meaning": k38_en
    }]
})

# ==========================================
# KAFI 39: 39. हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा
# ==========================================
k39_orig = """गल अलफी सिर-पा-बरहना, भलके रूप वटावेंगा,
इस लालच नफ़सानी कोलों, ओड़क मून मनावेंगा,
घाट ज़िकात मंगणगे प्यादे, कहु की अमल विखावेंगा,
आण बनी सिर पर भारी, अगों की बतलावेंगा,
हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।

हक्क पराइआ जातो नाहीं, खा कर भार उठावेंगा,
फेर ना आ कर बदला देसें लाखी खेत लुटावेंगा,
दाअ ला के विच जग दे जूए, जित्ते दम हरावेंगा,
हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।

जैसी करनी वैसी भरनी, प्रेम नगर दा वरतारा ए,
एथे दोज़ख कट्ट तूं दिलबर, अगे खुल्ल्ह बहारा ए,
केसर बीज जो केसर जंमे, लस्हन बीज की खावेंगा,
हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।

करो कमाई मेरे भाई, इहो वकत कमावण दा,
पौ-सतारां पैंदे ने हुण, दाय ना बाज़ी हारन दा,
उजड़ी खेड छपणगियां नरदां, झाड़ू कान उठावेंगा,
हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।

खावें मास चबावें बीड़े, अंग पुशाक लगाइआ ई,
टेढी पगड़ी अक्कड़ चलें, जुत्ती पैर अड़ाइआ ई,
पलदा हैं तूं जम दा बकरा, आपना आप कुहावेंगा,
हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।

पल दा वासा वस्सन एथे, रहन नूं अगे डेरा ए,
लै लै तुहफे घर नूं घल्लीं, इहो वेला तेरा ए,
ओथे हत्थ ना लगदा कुझ वी, एथों ही लै जावेंगा,
हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।

पढ़ सबक मुहब्बत ओसे दा तूं, बेमूजब क्यों डुबना एं,
पढ़ पढ़ किस्से मगज़ खपावें, क्यों खुभण विच खुभना एं,
हरफ़ इश्क दा इक्को नुक़्ता, काहे को ऊठ लदावेंगा,
हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।

भुक्ख मरेंदीआं नाम अल्लाह दा, इहो बात चंगेरी ए,
दोवें थोक पत्थर थीं भारे, औखी जेही इह फेरी ए,
आण बणी जद सिर पर भारी, अग्गों की बतलावेंगा,
हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।

अम्मां बाबा बेटी बेटा, पुच्छ वेखां क्यों रोंदे नी,
रन्नां कंजकां भैणां भाई, वारस आण खलोंदे नी,
इह जो लुट्टदे तूं नहीं लुट्टदा, मर के आप लुटावेंगा,
हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।

इक इकलिआं जाणा ई तैं, नाल ना कोई जावेगा,
खवेश-कबीला रोंदा पिटदा, राहों ही मुड़ आवेगा,
शहरों बाहर जंगल विच वासे, ओथे डेरा पावेंगा,
हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।

करां नसीहत वड्डी जे कोई, सुण कर दिल 'ते लावेंगा,
मोए तां रोज़-हशर नूं उट्ठण, आशक ना मर जावेंगा,
जे तूं मरें मरन तों अग्गे, मरने दा मुल्ल पावेंगा,
हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।

जां राह शर्हा दा पकड़ेंगा, तां ओट मुहंमदी होवेगा,
कहिंदी है पर करदी नाहीं, इहो ख़लकत रोवेंगा,
हुण सुत्त्यां तैनूं कौण जगाए, जागदिआं पछतावेंगा,
हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।

जे तूं साडे आखे लग्गें, तैनूं तख़त बहावांगे,
जिस नूं सारा आलम ढूंडे, तैनूं आण मिलावांगे,
ज़ुहदी हो के ज़ुहद कमावें, लै पिया गल लावेंगा,
हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।

ऐवें उमर गवाईआ औगत, अकबत चा रुढ़ाइआ ई,
लालच कर कर दुनियां उत्ते, मुक्ख सफैदी आया ई,
अजे वी सुन जे तायब होवें, तां आशना सदावेंगा,
हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।

बुल्ल्हा शौह दे चलणा एं तां चल, केहा चिर लाइआ ई,
जिको धक्के की करने, जां वतनों दफ़तर आया ई,
वाचन्दिआं खत अकल गईओ ई रो रो हाल वंजावेंगा,
हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।"""

k39_hi = """कल कफ़न का सादा कुर्ता पहनकर, नंगे सिर और नंगे पैर तुझे इस संसार से विदा होना पड़ेगा!  
इस सांसारिक लालच और वासना के अंत में तुझे अपना सिर मुंडवाकर पश्चाताप करना पड़ेगा!  
जब यमदूत और कर-संग्राहक आकर तेरे कर्मों का हिसाब मांगेंगे, तब तू अपने कौन-से भले कर्म दिखाएगा?  
जब मृत्यु की भारी विपत्ति सिर पर आ पड़ेगी, तब उस ईश्वर के आगे क्या उत्तर देगा?  
अरे! संतों की फ़क़ीरी से तू शर्म करता है, सांसारिक शक्ति का यह हुक्म भला कब तक चलाएगा?  

तूने दूसरों के हक़ की कभी परवाह नहीं की, दूसरों का धन हड़पकर पापों की भारी गठरी उठाएगा!  
फिर दोबारा इस संसार में आकर तू उस क़र्ज़ को चुका नहीं सकेगा, अपनी सारी हरी-भरी खेती लुटा बैठेगा!  
इस संसार के जुए में बाज़ी लगाकर, अपनी जीती हुई अमूल्य साँसों को तू हार जाएगा!  
अरे! संतों की फ़क़ीरी से तू शर्म करता है, सांसारिक शक्ति का यह हुक्म भला कब तक चलाएगा?  

प्रेम की नगरी का यह अटल नियम है कि जो जैसा करेगा, वैसा ही फल पाएगा!  
हे प्यारे! इस संसार में ही अहंकार को मिटाकर संयम की तपस्या कर ले, आगे मुक्ति की अनंत बहारें हैं!  
केसर बोएगा तभी तो केसर उगेगी, लहसुन का बीज बोकर भला क्या खाएगा?  
अरे! संतों की फ़क़ीरी से तू शर्म करता है, सांसारिक शक्ति का यह हुक्म भला कब तक चलाएगा?  

हे मेरे भाई! शुभ कर्मों की कमाई कर लो, यही कमाई करने का सुनहरा अवसर है!  
अब जीवन की चौसर पर अनुकूल पासे (पौ-सत्रह) पड़ रहे हैं, इस बाज़ी को हारने का अवसर मत गँवाओ!  
जब यह खेल उजड़ जाएगा और मोहरें बंद हो जाएँगी, तो पछताकर तिनके और झाड़ू ही उठाता फिरेगा!  
अरे! संतों की फ़क़ीरी से तू शर्म करता है, सांसारिक शक्ति का यह हुक्म भला कब तक चलाएगा?  

स्वादिष्ट मांस खाता है, पान के बीड़े चबाता है, शरीर पर रेशमी पोशाकें सजा रखी हैं!  
टेढ़ी पगड़ी बाँधकर अकड़ कर चलता है, पैरों में जरी की जूती अटका रखी है!  
अरे नादान! तू तो काल का बकरा बनकर पल रहा है, स्वयं अपने ही हाथों अपनी बलि दिलवाएगा!  
अरे! संतों की फ़क़ीरी से तू शर्म करता है, सांसारिक शक्ति का यह हुक्म भला कब तक चलाएगा?  

यहाँ तो केवल पल भर का बसेरा है, असली और शाश्वत डेरा तो आगे परलोक में है!  
यहाँ रहते-रहते शुभ कर्मों के उपहार अपने असली घर भेज ले, यही तेरा समय है!  
वहाँ पहुँचकर कुछ भी हाथ नहीं लगेगा, जो कुछ यहाँ से लेकर जाएगा वही तेरे काम आएगा!  
अरे! संतों की फ़क़ीरी से तू शर्म करता है, सांसारिक शक्ति का यह हुक्म भला कब तक चलाएगा?  

उस परम प्रियतम के प्रेम का सच्चा पाठ पढ़, अज्ञान के दरिया में बिना वजह क्यों डूबता है?  
व्यर्थ के किस्से-कहानियाँ पढ़कर दिमाग़ खपाता है, भ्रम के दलदल में क्यों धँसता जाता है?  
इश्क़ का अक्षर तो केवल एक सीधा 'अलिफ़' का नुक्ता है, सिर पर पोथियों के ऊँट क्यों लादता है?  
अरे! संतों की फ़क़ीरी से तू शर्म करता है, सांसारिक शक्ति का यह हुक्म भला कब तक चलाएगा?  

भूख सहते हुए भी केवल अल्लाह का नाम जपना ही सबसे उत्तम मार्ग है!  
भोग और संग्रह के पत्थर से भी भारी बोझ को ढोना बहुत कठिन यात्रा है!  
जब मृत्यु का संताप सिर पर आ टूटेगा, तब उस रब के सामने क्या बहाना बनाएगा?  
अरे! संतों की फ़क़ीरी से तू शर्म करता है, सांसारिक शक्ति का यह हुक्म भला कब तक चलाएगा?  

माता, पिता, बेटा और बेटी—ज़रा देख तो सही, वे तेरे मरने पर किसलिए रोते हैं?  
स्त्रियाँ, कन्याएँ, बहनें और भाई केवल तेरी छोड़ी हुई संपत्ति के वारिस बनकर खड़े हैं!  
जो धन वे आज लूट रहे हैं, उस धन से तू स्वयं का कल्याण न कर सका, अंत में सब कुछ यहीं लुटवा जाएगा!  
अरे! संतों की फ़क़ीरी से तू शर्म करता है, सांसारिक शक्ति का यह हुक्म भला कब तक चलाएगा?  

तुझे अकेले ही उस अंतिम यात्रा पर जाना होगा, तेरे साथ कोई भी सगा नहीं जाएगा!  
कुटुंब-क़बीला रोता-पीटता हुआ श्मशान के मार्ग से ही वापस लौट आएगा!  
शहर से बाहर वीरान जंगल की कब्र में ही तुझे अपना अंतिम डेरा डालना होगा!  
अरे! संतों की फ़क़ीरी से तू शर्म करता है, सांसारिक शक्ति का यह हुक्म भला कब तक चलाएगा?  

मैं तुझे सबसे बड़ी आत्मिक सीख देता हूँ, यदि तू सुनकर इसे अपने दिल में धारण करे:  
अज्ञानी तो कयामत के दिन तक कब्रों में पड़े रहेंगे, परंतु सच्चा आशिक़ कभी नहीं मरता!  
यदि तू इस भौतिक शरीर के मरने से पूर्व अपने अहंकार को मार दे, तो तू अमर जीवन का मूल्य पा जाएगा!  
अरे! संतों की फ़क़ीरी से तू शर्म करता है, सांसारिक शक्ति का यह हुक्म भला कब तक चलाएगा?  

जब तू धर्म और सत्य के पावन मार्ग को पकड़ेगा, तभी पैग़ंबर की रहमत की छत्रछाया मिलेगी!  
यह संसार केवल उपदेश देता है पर आचरण नहीं करता, अंत में रो-रोकर पछताएगा!  
इस मोह-निद्रा में सोए हुए तुझे कौन जगाए? जब होश में आएगा तो भारी पश्चाताप करेगा!  
अरे! संतों की फ़क़ीरी से तू शर्म करता है, सांसारिक शक्ति का यह हुक्म भला कब तक चलाएगा?  

यदि तू हमारे कहे अनुसार चले, तो हम तुझे आध्यात्मिक साम्राज्य के तख़्त पर बैठा देंगे!  
जिस परमात्मा को सारा संसार बाहर ढूँढता फिरता है, हम तुझे उससे साक्षात मिला देंगे!  
सच्चा वैरागी बनकर साधना कर, तब तू अपने प्रियतम को साक्षात गले से लगाएगा!  
अरे! संतों की फ़क़ीरी से तू शर्म करता है, सांसारिक शक्ति का यह हुक्म भला कब तक चलाएगा?  

तूने अपनी पूरी उम्र व्यर्थ के प्रपंचों में गँवा दी, और अपना परलोक डुबो दिया!  
संसार के पीछे लालच करते-करते तेरे बालों में बुढ़ापे की सफ़ेदी उतर आई!  
अब भी मेरी बात सुन और पश्चाताप करके प्रभु की शरण में आ जा, तभी सच्चा आशिक़ कहलाएगा!  
अरे! संतों की फ़क़ीरी से तू शर्म करता है, सांसारिक शक्ति का यह हुक्म भला कब तक चलाएगा?  

हे बुल्ले! यदि प्रभु-मिलन के मार्ग पर चलना है तो अभी चल पड़, अब कैसी देर लगा रहा है?  
जब उस परम देश से बुलावा आ जाएगा, तब दुनिया के धक्के किस काम आएँगे?  
उस परवाने को पढ़कर जब बुद्धि चकरा जाएगी, तब छाती पीट-पीटकर रोता फिरेगा!  
अरे! संतों की फ़क़ीरी से तू शर्म करता है, सांसारिक शक्ति का यह हुक्म भला कब तक चलाएगा?"""

k39_en = """Tomorrow thou shalt don the simple white shroud, walking bareheaded to the tomb,  
Transfigured and stripped of worldly pride beneath heaven's vaulted dome!  
For this greedy lust of the ego, thou shalt bend thy shaved head in grief,  
When the bailiffs of heaven demand the taxes of thy deeds without relief!  
When the dire hour strikes upon thy head, what answer wilt thou display?  
Thou art ashamed of saintly poverty—how long wilt thou brandish earthly authority?  

Thou didst never respect the rights of others, bearing a crushing burden of sin,  
Never able to return and repay the harvest of fields thou didst squander within!  
Staking thy soul in the gambling-den of this ephemeral earthly game,  
Losing thy won breaths, drowning in regret and shame!  
Thou art ashamed of saintly poverty—how long wilt thou brandish earthly authority?  

As a man sows, so shall he reap—such is Love's sovereign law,  
Burn out thy hellish ego right here, that eternal spring may thaw!  
Sow saffron seeds if saffron blooms thou dost desire to taste,  
If thou plantest garlic, what harvest canst thou expect but waste?  
Thou art ashamed of saintly poverty—how long wilt thou brandish earthly authority?  

Earn the true spiritual treasure, my brother, now is the golden hour,  
Favorable throws of the dice are falling now with supreme power!  
When the game is over and the pieces are packed in the dark bag of clay,  
Thou shalt wander picking up broom-twigs in helpless dismay!  
Thou art ashamed of saintly poverty—how long wilt thou brandish earthly authority?  

Thou feastest upon rich meats, chewing betel, draped in robes of gold,  
Strutting with a cocked turban and proud boots, arrogant and bold!  
Thou art only fattening thyself like a goat for Death’s butcher-knife,  
Led to the slaughter by thine own blind clinging to life!  
Thou art ashamed of saintly poverty—how long wilt thou brandish earthly authority?  

Only for a fleeting moment is thy sojourn beneath this mortal sky,  
The eternal dwelling awaits thee when the curtain is lifted on high!  
Dispatch gifts of righteous deeds to that homeland while breath remains,  
For nothing can be gathered over there; here alone are the true gains!  
Thou art ashamed of saintly poverty—how long wilt thou brandish earthly authority?  

Study the single lesson of divine Love—why drown without cause or rhyme?  
Wasting thy brain in endlessly parsing tales through passing time?  
The whole alphabet of Love is contained in a single Alif’s dot,  
Why load whole camels with heavy books when the essence is forgot?  
Thou art ashamed of saintly poverty—how long wilt thou brandish earthly authority?  

Enduring hunger while chanting the Holy Name is the noblest course to trace,  
Carrying rocks of worldly possessions is too heavy a race!  
When the summons of the final hour falls upon thy shivering brow,  
What excuse before the Sovereign Judge wilt thou deliver now?  
Thou art ashamed of saintly poverty—how long wilt thou brandish earthly authority?  

Mother, father, daughter, and son—ask thyself why they weep so loud:  
Wives, sisters, and brothers stand eager like heirs around the shroud!  
What they plunder now, thou couldst not surrender to God in thy prime,  
At death thou shalt yield it all, an empty victim of time!  
Thou art ashamed of saintly poverty—how long wilt thou brandish earthly authority?  

Alone, utterly alone, shalt thou depart on that solitary path ahead,  
Not a single friend or kinsman will follow where the silent walk is led!  
The weeping family will turn back at the graveyard's sandy gate,  
Leaving thee in the wilderness tomb to meet thy destined fate!  
Thou art ashamed of saintly poverty—how long wilt thou brandish earthly authority?  

I give thee the supreme counsel, if thou hast ears and heart to receive:  
The worldly dead sleep until Resurrection, but true lovers never grieve!  
If thou diest to thy selfish ego before mortal death draws nigh,  
Thou shalt attain the priceless pearl of immortality on high!  
Thou art ashamed of saintly poverty—how long wilt thou brandish earthly authority?  

If thou graspest the sacred path of Truth, the Prophet’s shield shall be thine,  
This hypocritical world preaches words it never weaves into the divine!  
Who will awaken thee from slumber before life slips away?  
When thou wakest too late, bitter tears will be thy only pay!  
Thou art ashamed of saintly poverty—how long wilt thou brandish earthly authority?  

If thou heedest our loving word, we will seat thee upon the spiritual throne,  
We will unite thee with that Beloved whom all creation seeks alone!  
Renounce the world in true ascetic fire, cultivate devotion deep,  
And the Lord Himself shall fold thee in His arms while the blind weep!  
Thou art ashamed of saintly poverty—how long wilt thou brandish earthly authority?  

Thou hast squandered thy prime in vanity, wrecking the life to come,  
Chasing shadows of earthly wealth until gray hair tells the sum!  
Hearken even now! If thou repentest and turnest to the Divine,  
Thou shalt be crowned as a true lover in Love’s eternal shrine!  
Thou art ashamed of saintly poverty—how long wilt thou brandish earthly authority?  

O Bulleh, if thou art to walk to the Lord's abode, start without delay,  
Why tarry when the final decree has already been signed today?  
When the warrant of departure arrives from the native land on high,  
Thy wits will shatter, and all thy proud commands will end in a cry!  
Thou art ashamed of saintly poverty—how long wilt thou brandish earthly authority?"""

batch.append({
    "id": 39,
    "title": "39. हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k39_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "गल अलफी सिर-पा-बरहना, भलके रूप वटावेंगा,",
                "hindi_gloss": "गल (गले में) अलफी (कफ़न का सादा कुर्ता) सिर-पा-बरहना (नंगे सिर और नंगे पैर), भलके (कल मृत्यु के बाद) रूप (अपना रूप) वटावेंगा (बदल जाएगा),",
                "english_gloss": "gal (around neck) alafee (shroud/coarse frock) sir-paa-barahna (bareheaded and barefoot), bhalke (tomorrow) roop (guise) vataavengaa (thou shalt transform),"
            },
            {
                "original": "इस लालच नफ़सानी कोलों, ओड़क मून मनावेंगा,",
                "hindi_gloss": "इस (इस) लालच (सांसारिक लोभ) नफ़सानी (और वासना) कोलों (के कारण), ओड़क (अंततः) मून (सिर मुंडवाकर) मनावेंगा (शोक मनाएगा),",
                "english_gloss": "is (this) laalach (greed) nafsaanee (carnal/sensual) kolon (from), odak (at last) moon (shaved head) manaavengaa (shalt lament),"
            },
            {
                "original": "घाट ज़िकात मंगणगे प्यादे, कहु की अमल विखावेंगा,",
                "hindi_gloss": "घाट (भवसागर के घाट पर) ज़िकात (कर्मों का कर) मंगणगे (माँगेंगे) प्यादे (यमदूत), कहु (बताओ) की (कौन-से) अमल (शुभ कर्म) विखावेंगा (दिखाएगा),",
                "english_gloss": "ghaat (wharf/ferry) zikaat (tax/toll) mangange (will demand) pyaade (messengers/guards), kahu (tell) kee (what) amal (deeds) vikhaavengaa (wilt thou show),"
            },
            {
                "original": "आण बनी सिर पर भारी, अगों की बतलावेंगा,",
                "hindi_gloss": "आण (आ) बनी (पड़ेगी जब) सिर पर (सिर पर) भारी (भारी विपत्ति), अगों (आगे प्रभु के सम्मुख) की (क्या) बतलावेंगा (उत्तर देगा),",
                "english_gloss": "aan (arriving) banee (befalls) sir par (upon head) bhaaree (heavy doom), agon (before God) kee (what) batlaavengaa (wilt thou reply),"
            },
            {
                "original": "हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।",
                "hindi_gloss": "हिजाब (लज्जा/संकोच) करें (करता है) दरवेशी (संतों की फ़क़ीरी) कोलों (से), कद तक (कब तक) हुक्म (अपनी सांसारिक सत्ता का हुक्म) चलावेंगा (चलाएगा) ।",
                "english_gloss": "hijaab (shame/veiling) karen (thou dost) darveshee (saintly poverty) kolon (from), kad tak (how long) hukam (authority) chalaavengaa (wilt thou wield) ."
            },
            {
                "original": "हक्क पराइआ जातो नाहीं, खा कर भार उठावेंगा,",
                "hindi_gloss": "हक्क (हक़) पराइआ (पराया) जातो नाहीं (जाना नहीं/पहचाना नहीं), खा कर (दूसरों का हक़ खाकर पापों का) भार (बोझ) उठावेंगा (उठाएगा),",
                "english_gloss": "hakk (rights) paraaia (of others) jaato naaheen (cared not), khaa kar (usurping) bhaar (heavy burden) uthaavengaa (shalt carry),"
            },
            {
                "original": "फेर ना आ कर बदला देसें लाखी खेत लुटावेंगा,",
                "hindi_gloss": "फेर (पुनः लौटकर) ना (नहीं) आ कर (आकर) बदला (उसका बदला/कर्ज़) देसें (दे सकेगा), लाखी (अपनी हरी-भरी अनमोल) खेत (खेती) लुटावेंगा (लुटा बैठेगा),",
                "english_gloss": "pher (again) na (not) aa kar (returning) badla (repayment) desen (canst give), laakhee (precious) khet (field/harvest) lutaavengaa (shalt squander),"
            },
            {
                "original": "दाअ ला के विच जग दे जूए, जित्ते दम हरावेंगा,",
                "hindi_gloss": "दाअ (दाँव) ला के (लगाकर) विच (में) जग (संसार) दे (के) जूए (जूए में), जित्ते (अपनी जीती हुई अनमोल) दम (साँसों को) हरावेंगा (हार बैठेगा),",
                "english_gloss": "daa-a (wager) laa ke (placing) vich (in) jag (world's) de (of) jooe (gamble), jitte (won) dam (breaths) haraavengaa (shalt lose),"
            },
            {
                "original": "हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।",
                "hindi_gloss": "हिजाब (शर्म) करें (करता है) दरवेशी (फ़क़ीरी) कोलों (से), कद तक (कब तक) हुक्म (हुक्म) चलावेंगा (चलाएगा) ।",
                "english_gloss": "hijaab (shame) karen (thou feelest) darveshee (dervish path) kolon (from), kad tak (how long) hukam (command) chalaavengaa (wilt wield) ."
            },
            {
                "original": "जैसी करनी वैसी भरनी, प्रेम नगर दा वरतारा ए,",
                "hindi_gloss": "जैसी (जैसी) करनी (करनी) वैसी (वैसी) भरनी (भरनी), प्रेम नगर (ईश्वरीय प्रेम की नगरी) दा (का यह) वरतारा (अटल नियम) ए (है),",
                "english_gloss": "jaisee (as) karnee (action) vaisee (so) bharnee (recompense), prem nagar (city of Love) da (of) varataara (custom/law) e (is),"
            },
            {
                "original": "एथे दोज़ख कट्ट तूं दिलबर, अगे खुल्ल्ह बहारा ए,",
                "hindi_gloss": "एथे (यहीं संसार में) दोज़ख (अहंकार के कष्ट) कट्ट (काट ले) तूं (तू) दिलबर (हे प्यारे), अगे (आगे परलोक में) खुल्ल्ह (उन्मुक्त) बहारा (आनंद की बहारें) ए (हैं),",
                "english_gloss": "ethe (here) dozakh (hell/mortification) katt (endure) toon (thou) dilbar (O friend), agge (hereafter) khullh (boundless) bahaara (spring/bliss) e (is),"
            },
            {
                "original": "केसर बीज जो केसर जंमे, लस्हन बीज की खावेंगा,",
                "hindi_gloss": "केसर (केसर) बीज (बोएगा) जो (तब) केसर (केसर) जंमे (उगेगी), लस्हन (लहसुन) बीज (बोकर) की (भला क्या) खावेंगा (खाएगा),",
                "english_gloss": "kesar (saffron) beej (sow) jo (then) kesar (saffron) jamme (sprouts), lashan (garlic) beej (sowing) kee (what) khaavengaa (wilt thou eat),"
            },
            {
                "original": "हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।",
                "hindi_gloss": "हिजाब (संकोच) करें (करता है) दरवेशी (संतत्व) कोलों (से), कद तक (कब तक) हुक्म (हुक्म) चलावेंगा (चलाएगा) ।",
                "english_gloss": "hijaab (shame) karen (thou hast) darveshee (saintliness) kolon (from), kad tak (how long) hukam (sway) chalaavengaa (wilt maintain) ."
            },
            {
                "original": "करो कमाई मेरे भाई, इहो वकत कमावण दा,",
                "hindi_gloss": "करो (करो) कमाई (शुभ कर्मों की कमाई) मेरे (मेरे) भाई (भाई), इहो (यही मानव जीवन) वकत (समय है) कमावण (आत्म-धन कमाने) दा (का),",
                "english_gloss": "karo (make) kamaaee (spiritual earnings) mere (my) bhaaee (brother), eho (this very) vakat (time) kamaavan (of earning) da (is),"
            },
            {
                "original": "पौ-सतारां पैंदे ने हुण, दाय ना बाज़ी हारन दा,",
                "hindi_gloss": "पौ-सतारां (चौसर के उत्तम पासे) पैंदे ने (पड़ रहे हैं) हुण (अब), दाय (यह अवसर) ना (नहीं है) बाज़ी (इस बाज़ी को) हारन (हारने) दा (का),",
                "english_gloss": "pau-sataaraan (winning dice throws) painde ne (are falling) hun (now), daay (time) na (not) baazee (the game) haaran (to lose) da (is),"
            },
            {
                "original": "उजड़ी खेड छपणगियां नरदां, झाड़ू कान उठावेंगा,",
                "hindi_gloss": "उजड़ी (जब खेल समाप्त हो जाएगा) खेड (खेल) छपणगियां (और मोहरें बंद हो जाएँगी) नरदां (मोहरें), झाड़ू (झाड़ू के) कान (तिनके ही) उठावेंगा (उठाता फिरेगा),",
                "english_gloss": "ujdee (ended) khed (game) chhapangeeyaan (hidden/stored) nardaan (game-pieces), jhaadoo (broom's) kaan (twigs/straws) uthaavengaa (wilt thou gather),"
            },
            {
                "original": "हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।",
                "hindi_gloss": "हिजाब (शर्म) करें (करता है) दरवेशी (फ़क़ीरी) कोलों (से), कद तक (कब तक) हुक्म (हुक्म) चलावेंगा (चलाएगा) ।",
                "english_gloss": "hijaab (shame) karen (thou dost) darveshee (dervish way) kolon (from), kad tak (how long) hukam (command) chalaavengaa (wilt thou wield) ."
            },
            {
                "original": "खावें मास चबावें बीड़े, अंग पुशाक लगाइआ ई,",
                "hindi_gloss": "खावें (खाता है) मास (मांस) चबावें (चबाता है) बीड़े (पान के बीड़े), अंग (अंग-अंग पर) पुशाक (रेशमी पोशाक) लगाइआ ई (सजा रखी है),",
                "english_gloss": "khaaven (eatest) maas (meat) chabaaven (chewest) beede (betel packets), ang (limbs) pushaak (costly attire) lagaaia ee (hast adorned),"
            },
            {
                "original": "टेढी पगड़ी अक्कड़ चलें, जुत्ती पैर अड़ाइआ ई,",
                "hindi_gloss": "टेढी (टेढ़ी) पगड़ी (पगड़ी बाँधकर) अक्कड़ (अकड़कर) चलें (चलता है), जुत्ती (जरीदार जूती) पैर (पैरों में) अड़ाइआ ई (अटका रखी है),",
                "english_gloss": "tedhee (tilted) pagdee (turban) akkad (arrogantly) chalen (walkest), juttee (embroidered shoe) pair (in foot) adaaia ee (hast put),"
            },
            {
                "original": "पलदा हैं तूं जम दा बकरा, आपना आप कुहावेंगा,",
                "hindi_gloss": "पलदा हैं (पल रहा है) तूं (तू) जम दा (यमराज का) बकरा (बकरा बनकर), आपना आप (स्वयं अपने हाथों अपनी बलि) कुहावेंगा (दिलवाएगा),",
                "english_gloss": "palda hain (art being fattened) toon (thou) jam da (Death's) bakra (goat), aapna aap (thine own self) kuhaavengaa (shalt cause to be slaughtered),"
            },
            {
                "original": "हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।",
                "hindi_gloss": "हिजाब (संकोच) करें (करता है) दरवेशी (संतत्व) कोलों (से), कद तक (कब तक) हुक्म (हुक्म) चलावेंगा (चलाएगा) ।",
                "english_gloss": "hijaab (shame) karen (dost feel) darveshee (poverty) kolon (from), kad tak (how long) hukam (sway) chalaavengaa (wilt maintain) ."
            },
            {
                "original": "पल दा वासा वस्सन एथे, रहन नूं अगे डेरा ए,",
                "hindi_gloss": "पल दा (क्षण भर का) वासा (बसेरा) वस्सन (बसना है) एथे (यहाँ इस लोक में), रहन नूं (सदा रहने के लिए) अगे (आगे परलोक में) डेरा (स्थाई डेरा) ए (है),",
                "english_gloss": "pal da (momentary) vaasa (lodging) vassan (dwelling) ethe (here), rahan noon (to abide) agge (hereafter) dera (permanent abode) e (is),"
            },
            {
                "original": "लै लै तुहफे घर नूं घल्लीं, इहो वेला तेरा ए,",
                "hindi_gloss": "लै लै (ले-लेकर) तुहफे (पुण्य-कर्मों के उपहार) घर नूं (सच्चे घर) घल्लीं (भेज दे), इहो (यही अवसर) वेला (समय) तेरा (तेरा) ए (है),",
                "english_gloss": "lai lai (taking) tuhfe (gifts of good deeds) ghar noon (to true home) ghalleen (send), eho (this) vela (opportunity) tera (thine) e (is),"
            },
            {
                "original": "ओथे हत्थ ना लगदा कुझ वी, एथों ही लै जावेंगा,",
                "hindi_gloss": "ओथे (वहाँ पहुँचकर) हत्थ ना लगदा (हाथ कुछ नहीं आएगा) कुझ वी (कुछ भी), एथों ही (यहाँ से जो कमाकर) लै जावेंगा (ले जाएगा वही काम आएगा),",
                "english_gloss": "othe (there) hatth na lagda (nothing comes to hand) kujh vee (at all), ethon hee (from here alone) lai jaavengaa (what thou takest),"
            },
            {
                "original": "हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।",
                "hindi_gloss": "हिजाब (शर्म) करें (करता है) दरवेशी (फ़क़ीरी) कोलों (से), कद तक (कब तक) हुक्म (हुक्म) चलावेंगा (चलाएगा) ।",
                "english_gloss": "hijaab (shame) karen (dost feel) darveshee (spiritual poverty) kolon (from), kad tak (how long) hukam (command) chalaavengaa (wilt wield) ."
            },
            {
                "original": "पढ़ सबक मुहब्बत ओसे दा तूं, बेमूजब क्यों डुबना एं,",
                "hindi_gloss": "पढ़ (पढ़ो) सबक (पाठ) मुहब्बत (ईश्वरीय प्रेम का) ओसे दा (उसी प्रभु के) तूं (तू), बेमूजब (बिना किसी कारण) क्यों (क्यों अज्ञान के सागर में) डुबना (डूबता) एं (है),",
                "english_gloss": "padh (study) sabak (the lesson) muhabbat (of love) ose da (of that One) toon (thou), be-moojab (without cause) kyon (why) dubna (drownest) ain (art thou),"
            },
            {
                "original": "पढ़ पढ़ किस्से मगज़ खपावें, क्यों खुभण विच खुभना एं,",
                "hindi_gloss": "पढ़ पढ़ (पढ़-पढ़कर) किस्से (किस्से-कहानियाँ) मगज़ (मस्तिष्क) खपावें (खपाता है), क्यों (क्यों) खुभण विच (दलदल में) खुभना (धँसता जाता) एं (है),",
                "english_gloss": "padh padh (reading endlessly) kisse (tales) magaz (brain) khapaaven (weariest), kyon (why) khubhan vich (in quagmire) khubhna (sinkest) ain (thou),"
            },
            {
                "original": "हरफ़ इश्क दा इक्को नुक़्ता, काहे को ऊठ लदावेंगा,",
                "hindi_gloss": "हरफ़ (अक्षर) इश्क दा (इश्क़ का तो) इक्को (केवल एक) नुक़्ता (सीधा नुक्ता/अलिफ़ है), काहे को (किसलिए) ऊठ (ऊंटों पर पोथियाँ) लदावेंगा (लादता फिरेगा),",
                "english_gloss": "haraf (letter) ishq da (of Love) ikko (is a single) nukta (dot), kaahe ko (why) ooth (camels with books) ladaavengaa (wilt load),"
            },
            {
                "original": "हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।",
                "hindi_gloss": "हिजाब (शर्म) करें (करता है) दरवेशी (संतत्व) कोलों (से), कद तक (कब तक) हुक्म (हुक्म) चलावेंगा (चलाएगा) ।",
                "english_gloss": "hijaab (shame) karen (thou feelest) darveshee (dervish way) kolon (from), kad tak (how long) hukam (authority) chalaavengaa (wilt wield) ."
            },
            {
                "original": "भुक्ख मरेंदीआं नाम अल्लाह दा, इहो बात चंगेरी ए,",
                "hindi_gloss": "भुक्ख मरेंदीआं (भूख सहते हुए भी) नाम (नाम) अल्लाह दा (अल्लाह का जपना), इहो (यही) बात (मार्ग) चंगेरी (सर्वोत्तम) ए (है),",
                "english_gloss": "bhukkh marendeeyaan (even dying of hunger) naam (the Name) allaah da (of Allah), eho (this) baat (matter) changeree (best) e (is),"
            },
            {
                "original": "दोवें थोक पत्थर थीं भारे, औखी जेही इह फेरी ए,",
                "hindi_gloss": "दोवें थोक (संसार और संग्रह के दोनों पदार्थ) पत्थर थीं (पत्थर से भी) भारे (भारी हैं), औखी जेही (अत्यंत कठिन) इह (यह जीवन की) फेरी (फेरी) ए (है),",
                "english_gloss": "doven thok (both worldly treasures) patthar theen (than stone) bhaare (heavier), aukhee jehee (arduous) eh (this) pheree (circuit of life) e (is),"
            },
            {
                "original": "आण बणी जद सिर पर भारी, अग्गों की बतलावेंगा,",
                "hindi_gloss": "आण बणी (जब आ पड़ेगी) जद (जब) सिर पर (सिर पर) भारी (विपत्ति), अग्गों (आगे प्रभु के सम्मुख) की (क्या) बतलावेंगा (उत्तर देगा),",
                "english_gloss": "aan banee (when it befalls) jad (when) sir par (upon head) bhaaree (heavy doom), aggon (before God) kee (what) batlaavengaa (wilt answer),"
            },
            {
                "original": "हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।",
                "hindi_gloss": "हिजाब (संकोच) करें (करता है) दरवेशी (फ़क़ीरी) कोलों (से), कद तक (कब तक) हुक्म (हुक्म) चलावेंगा (चलाएगा) ।",
                "english_gloss": "hijaab (shame) karen (thou hast) darveshee (saintly path) kolon (from), kad tak (how long) hukam (rule) chalaavengaa (wilt wield) ."
            },
            {
                "original": "अम्मां बाबा बेटी बेटा, पुच्छ वेखां क्यों रोंदे नी,",
                "hindi_gloss": "अम्मां (माता) बाबा (पिता) बेटी (पुत्री) बेटा (और पुत्र), पुच्छ वेखां (जरा पूछकर देख) क्यों (वे तेरे मरने पर क्यों) रोंदे नी (रो रहे हैं),",
                "english_gloss": "ammaan (mother) baaba (father) betee (daughter) beta (son), puchh vekhaan (ask and see) kyon (why) ronde neen (they weep),"
            },
            {
                "original": "रन्नां कंजकां भैणां भाई, वारस आण खलोंदे नी,",
                "hindi_gloss": "रन्नां (स्त्रियाँ) कंजकां (कन्याएँ) भैणां (बहनें) भाई (और भाई), वारस (केवल संपत्ति के उत्तराधिकारी) आण (आकर) खलोंदे नी (खड़े होते हैं),",
                "english_gloss": "rannaan (wives) kanjkaan (daughters) bhainaan (sisters) bhaaee (brothers), vaaras (inheritors/heirs) aan (coming) khalonde neen (stand),"
            },
            {
                "original": "इह जो लुट्टदे तूं नहीं लुट्टदा, मर के आप लुटावेंगा,",
                "hindi_gloss": "इह जो (जो यह धन) लुट्टदे (वे लूटते हैं) तूं नहीं (तूने अपने जीवन में प्रभु-राह में नहीं) लुट्टदा (लुटाया), मर के (अब मरकर तू) आप (स्वयं सब) लुटावेंगा (लुटवा बैठेगा),",
                "english_gloss": "eh jo (this which) luttde (they loot) toon naaheen (thou didst not) luttda (spend on God), mar ke (dying) aap (thyself) lutaavengaa (shalt squander),"
            },
            {
                "original": "हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।",
                "hindi_gloss": "हिजाब (शर्म) करें (करता है) दरवेशी (दरवेशी) कोलों (से), कद तक (कब तक) हुक्म (हुक्म) चलावेंगा (चलाएगा) ।",
                "english_gloss": "hijaab (shame) karen (thou dost) darveshee (dervish way) kolon (from), kad tak (how long) hukam (authority) chalaavengaa (wilt wield) ."
            },
            {
                "original": "इक इकलिआं जाणा ई तैं, नाल ना कोई जावेगा,",
                "hindi_gloss": "इक (अकेले) इकलिआं (नितांत अकेले) जाणा ई (जाना है) तैं (तुझे), नाल (तेरे साथ) ना (नहीं) कोई (कोई भी) जावेगा (जाएगा),",
                "english_gloss": "ik (alone) ikliaan (all alone) jaana ee (hast to go) tain (thou), naal (with thee) na (not) koee (anyone) jaavega (will go),"
            },
            {
                "original": "खवेश-कबीला रोंदा पिटदा, राहों ही मुड़ आवेगा,",
                "hindi_gloss": "खवेश-कबीला (कुटुंब और क़बीला) रोंदा (रोता) पिटदा (और छाती पीटता हुआ), राहों ही (मार्ग से ही) मुड़ (वापस लौट) आवेगा (आएगा),",
                "english_gloss": "khavesh-kabeela (kin and clan) ronda (weeping) pitda (beating breast), raahon hee (from midway) mud (turning back) aavega (will return),"
            },
            {
                "original": "शहरों बाहर जंगल विच वासे, ओथे डेरा पावेंगा,",
                "hindi_gloss": "शहरों बाहर (शहर से बाहर) जंगल विच (सन्नाटे भरे जंगल में) वासे (तेरा वास होगा), ओथे (वहाँ मिट्टी की कब्र में) डेरा (अपना डेरा) पावेंगा (डालेगा),",
                "english_gloss": "shahron baahar (outside the city) jangal vich (in the wild wilderness) vaase (dwelling), othe (there) dera (camp/tomb) paavengaa (shalt pitch),"
            },
            {
                "original": "हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।",
                "hindi_gloss": "हिजाब (संकोच) करें (करता है) दरवेशी (संतत्व) कोलों (से), कद तक (कब तक) हुक्म (हुक्म) चलावेंगा (चलाएगा) ।",
                "english_gloss": "hijaab (shame) karen (feelest) darveshee (saintly state) kolon (from), kad tak (how long) hukam (command) chalaavengaa (wilt maintain) ."
            },
            {
                "original": "करां नसीहत वड्डी जे कोई, सुण कर दिल 'ते लावेंगा,",
                "hindi_gloss": "करां (मैं करता हूँ) नसीहत (हितोपदेश/सीख) वड्डी (सबसे बड़ी) जे कोई (यदि कोई), सुण कर (सुनकर) दिल 'ते (अपने हृदय पर) लावेंगा (धारण करे),",
                "english_gloss": "karaan (I give) naseehat (counsel) vaddee (supreme) je koee (if any), sun kar (hearing) dil 'te (upon heart) laavengaa (wilt take),"
            },
            {
                "original": "मोए तां रोज़-हशर नूं उट्ठण, आशक ना मर जावेंगा,",
                "hindi_gloss": "मोए (संसारी मुर्दे) तां (तो) रोज़-हशर नूं (प्रलय के दिन) उट्ठण (उठेंगे), आशक (किंतु सच्चा आशिक़) ना (कभी) मर (मर नहीं) जावेंगा (जाता),",
                "english_gloss": "moe (the worldly dead) taan (indeed) roz-hashar noon (on Judgment Day) utthan (arise), aashak (the true lover) na (not) mar (dies) jaavengaa (shall ever),"
            },
            {
                "original": "जे तूं मरें मरन तों अग्गे, मरने दा मुल्ल पावेंगा,",
                "hindi_gloss": "जे (यदि) तूं (तू) मरें (मर जाए) मरन तों अग्गे (शारीरिक मृत्यु से पूर्व अहंकार को मार ले), मरने दा (तो तू इस मरने का अमर) मुल्ल (मूल्य/वरदान) पावेंगा (पा जाएगा),",
                "english_gloss": "je (if) toon (thou) maren (diest to self) maran ton agge (before mortal death), marne da (of dying) mull (price/reward) paavengaa (shalt obtain),"
            },
            {
                "original": "हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।",
                "hindi_gloss": "हिजाब (शर्म) करें (करता है) दरवेशी (फ़क़ीरी) कोलों (से), कद तक (कब तक) हुक्म (हुक्म) चलावेंगा (चलाएगा) ।",
                "english_gloss": "hijaab (shame) karen (dost feel) darveshee (dervish path) kolon (from), kad tak (how long) hukam (sway) chalaavengaa (wilt wield) ."
            },
            {
                "original": "जां राह शर्हा दा पकड़ेंगा, तां ओट मुहंमदी होवेगा,",
                "hindi_gloss": "जां (जब) राह (मार्ग) शर्हा दा (सच्चे ईश्वरीय नियम का) पकड़ेंगा (पकड़ेगा), तां (तब तुझे) ओट (शरण/छत्रछाया) मुहंमदी (हज़रत मुहम्मद की) होवेगा (प्राप्त होगी),",
                "english_gloss": "jaan (when) raah (path) sharha da (of divine law) pakdengaa (shalt seize), taan (then) ot (refuge) muhammadee (of Muhammad) hovega (shalt have),"
            },
            {
                "original": "कहिंदी है पर करदी नाहीं, इहो ख़लकत रोवेंगा,",
                "hindi_gloss": "कहिंदी है (यह केवल मुख से उपदेश कहती है) पर (परंतु) करदी नाहीं (आचरण नहीं करती), इहो (इसी कारण यह) ख़लकत (संसार की सृष्टि) रोवेंगा (रोएगी/पछताएगी),",
                "english_gloss": "kahindee hai (speaks) par (but) kardee naaheen (practices not), eho (thus this) khalkat (creation/people) rovengaa (will lament),"
            },
            {
                "original": "हुण सुत्त्यां तैनूं कौण जगाए, जागदिआं पछतावेंगा,",
                "hindi_gloss": "हुण (अब इस मोह में) सुत्त्यां (सोए हुए) तैनूं (तुझको) कौण (कौन) जगाए (जगाए), जागदिआं (जब बाद में जागेगा तब केवल) पछतावेंगा (पछताएगा),",
                "english_gloss": "hun (now) suttyaan (slumbering) tainoon (thee) kaun (who) jagaae (can awaken), jaagdiaan (upon awakening) pachhtaavengaa (shalt regret),"
            },
            {
                "original": "हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।",
                "hindi_gloss": "हिजाब (संकोच) करें (करता है) दरवेशी (संतत्व) कोलों (से), कद तक (कब तक) हुक्म (हुक्म) चलावेंगा (चलाएगा) ।",
                "english_gloss": "hijaab (shame) karen (thou hast) darveshee (poverty) kolon (from), kad tak (how long) hukam (rule) chalaavengaa (wilt wield) ."
            },
            {
                "original": "जे तूं साडे आखे लग्गें, तैनूं तख़त बहावांगे,",
                "hindi_gloss": "जे (यदि) तूं (तू) साडे (हमारे) आखे (कहने पर) लग्गें (चले), तैनूं (तुझको हम आध्यात्मिक) तख़त (सिंहासन पर) बहावांगे (बैठा देंगे),",
                "english_gloss": "je (if) toon (thou) saade (our) aakhe (counsel) laggen (heedest), tainoon (thee) takhat (upon royal throne) bahaavaange (we will seat),"
            },
            {
                "original": "जिस नूं सारा आलम ढूंडे, तैनूं आण मिलावांगे,",
                "hindi_gloss": "जिस (जिस परमात्मा) नूं (को) सारा (समस्त) आलम (संसार बाहर) ढूंडे (खोजता फिरता है), तैनूं (तुझको उससे) आण (लाकर साक्षात) मिलावांगे (मिला देंगे),",
                "english_gloss": "jis (whom) noon (unto) saara (entire) aalam (universe) dhoonde (searches for), tainoon (thee) aan (bringing) milaavaange (we will unite),"
            },
            {
                "original": "ज़ुहदी हो के ज़ुहद कमावें, लै पिया गल लावेंगा,",
                "hindi_gloss": "ज़ुहदी (सच्चा वैरागी) हो के (होकर) ज़ुहद (तपस्या और संयम) कमावें (कमाए), लै (तब तू) पिया (अपने प्यारे साजन को) गल (गले से) लावेंगा (लगा लेगा),",
                "english_gloss": "zuhdee (ascetic/renunciant) ho ke (becoming) zuhad (disciplined devotion) kamaaven (practicest), lai (taking) piya (Beloved) gal (to bosom) laavengaa (shalt embrace),"
            },
            {
                "original": "हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।",
                "hindi_gloss": "हिजाब (शर्म) करें (करता है) दरवेशी (फ़क़ीरी) कोलों (से), कद तक (कब तक) हुक्म (हुक्म) चलावेंगा (चलाएगा) ।",
                "english_gloss": "hijaab (shame) karen (dost feel) darveshee (dervish way) kolon (from), kad tak (how long) hukam (command) chalaavengaa (wilt wield) ."
            },
            {
                "original": "ऐवें उमर गवाईआ औगत, अकबत चा रुढ़ाइआ ई,",
                "hindi_gloss": "ऐवें (यूँ ही व्यर्थ) उमर (पूरी उम्र) गवाईआ (गँवा दी) औगत (दुर्दशा और पाप में), अकबत (और अपना परलोक) चा (उठाकर) रुढ़ाइआ ई (बहा दिया/नष्ट कर दिया),",
                "english_gloss": "aiven (in vain) umar (lifetime) gavaaeea (squandered) augat (in wretchedness), akbat (hereafter) cha (taking) rudhaaia ee (hast ruined),"
            },
            {
                "original": "लालच कर कर दुनियां उत्ते, मुक्ख सफैदी आया ई,",
                "hindi_gloss": "लालच कर कर (लोभ करते-करते) दुनियां उत्ते (इस संसार के प्रति), मुक्ख (मुख पर बुढ़ापे की) सफैदी (सफ़ेदी) आया ई (छा गई है),",
                "english_gloss": "laalach kar kar (coveting) duniyaan utte (upon worldly gain), mukkh (face/hair) safaidee (whiteness/pale age) aaya ee (has arrived),"
            },
            {
                "original": "अजे वी सुन जे तायब होवें, तां आशना सदावेंगा,",
                "hindi_gloss": "अजे वी (अब भी) सुन (सुन ले) जे (यदि तू) तायब (पश्चाताप करने वाला) होवें (हो जाए), तां (तब तू) आशना (सच्चा प्रेमी/ईश्वर का मित्र) सदावेंगा (कहलाएगा),",
                "english_gloss": "aje vee (even now) sun (hearken) je (if) taayab (repentant) hoven (becomest), taan (then) aashna (beloved friend) sadaavengaa (shalt be called),"
            },
            {
                "original": "हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।",
                "hindi_gloss": "हिजाब (संकोच) करें (करता है) दरवेशी (संतत्व) कोलों (से), कद तक (कब तक) हुक्म (हुक्म) चलावेंगा (चलाएगा) ।",
                "english_gloss": "hijaab (shame) karen (thou hast) darveshee (saintly state) kolon (from), kad tak (how long) hukam (authority) chalaavengaa (wilt maintain) ."
            },
            {
                "original": "बुल्ल्हा शौह दे चलणा एं तां चल, केहा चिर लाइआ ई,",
                "hindi_gloss": "बुल्ल्हा (हे बुल्ले) शौह दे (स्वामी के धाम) चलणा एं (चलना है) तां चल (तो अब चल पड़), केहा (कैसी यह) चिर (देरी) लाइआ ई (लगा रहा है),",
                "english_gloss": "bullha (O Bulleh) shauh de (to the Lord's abode) chalna ain (wilt go) taan chal (then depart), keha (what) chir (delay) laaia ee (art making),"
            },
            {
                "original": "जिको धक्के की करने, जां वतनों दफ़तर आया ई,",
                "hindi_gloss": "जिको (संसार के यह) धक्के (धक्के) की करने (किस काम आएँगे), जां (जब) वतनों (परलोक/सच्चे वतन से) दफ़तर (बुलावे का आदेश-पत्र) आया ई (आ चुका है),",
                "english_gloss": "jiko (of this world) dhakke (shoves/struggles) kee karne (what use), jaan (when) vatanon (from celestial homeland) daftar (decree/summons) aaya ee (has arrived),"
            },
            {
                "original": "वाचन्दिआं खत अकल गईओ ई रो रो हाल वंजावेंगा,",
                "hindi_gloss": "वाचन्दिआं (पढ़ते ही उस) खत (मृत्यु-पत्र को) अकल (तेरी बुद्धि) गईओ ई (उड़ जाएगी और), रो रो (रो-रोकर अपना) हाल (बुरा हाल) वंजावेंगा (बनाएगा),",
                "english_gloss": "vaachandiaan (upon reading) khat (letter/decree) akal (wits) gayeeo ee (shall flee), ro ro (weeping) haal (thy condition) vanjaavengaa (shalt ruin),"
            },
            {
                "original": "हिजाब करें दरवेशी कोलों, कद तक हुक्म चलावेंगा ।",
                "hindi_gloss": "हिजाब (शर्म) करें (करता है) दरवेशी (दरवेशी) कोलों (से), कद तक (कब तक) हुक्म (हुक्म) चलावेंगा (चलाएगा) ।",
                "english_gloss": "hijaab (shame) karen (thou dost) darveshee (dervish way) kolon (from), kad tak (how long) hukam (authority) chalaavengaa (wilt wield) ."
            }
        ],
        "hindi_meaning": k39_hi,
        "english_meaning": k39_en
    }]
})

# ==========================================
# KAFI 40: 40. हिन्दू ना नहीं मुसलमान
# ==========================================
k40_orig = """हिन्दू ना नहीं मुसलमान ।
बहीए त्रिंजन तज अभिमान ।

सुन्नी ना नहीं हम शिया ।
सुल्हा कुल्ल का मारग लिया ।

भुक्खे ना नहीं हम रज्जे ।
नंगे ना नहीं हम कज्जे ।

रोंदे ना नहीं हम हस्सदे ।
उजड़े ना नहीं हम वस्सदे ।

पापी ना सुधरमी ना ।
पाप पुन्न की राह ना जाणा ।

बुल्ल्हा शहु जो हरि चित लागे ।
हिन्दू तुर्क दूजन त्यागे ।"""

k40_hi = """न हम हिन्दू हैं और न ही हम मुसलमान!  
आओ, समस्त अहंकार को त्यागकर प्रेम की सत्संग-सभा में साथ बैठें!  

न हम सुन्नी हैं और न ही शिया संप्रदाय के,  
हमने तो 'सुलह-ए-कुल' (सबके प्रति पूर्ण प्रेम और शांति) का पावन मार्ग चुन लिया है!  

न हम भूखे हैं और न ही तृप्त होकर अघाए हैं,  
न हम नंगे हैं और न ही वस्त्रों से ढके हुए हैं!  

न हम विलाप करते हैं और न ही व्यर्थ हँसते हैं,  
न हम उजड़े हुए हैं और न ही किसी नगर में बसे हैं!  

न हम पापी हैं और न ही धर्मात्मा का दंभ भरते हैं,  
हमने तो पाप और पुण्य के सांसारिक बंधनों को पीछे छोड़ दिया है!  

हे बुल्ले! जिसका चित्त उस एक परम प्रियतम हरि में रम गया,  
उसने हिन्दू और तुर्क के सारे द्वैत और भेदभाव को सदा के लिए त्याग दिया!"""

k40_en = """Neither Hindu nor Muslim am I,  
Renouncing all ego, in Love's circle we lie!  

Neither Sunni nor Shia bound by creed,  
Universal peace (Sulh-e-Kull) is our only need!  

Neither hungry nor sated with worldly food,  
Neither naked nor draped in garments crude!  

Neither weeping in sorrow nor laughing in vanity,  
Neither desolate ruins nor settled humanity!  

Neither sinful transgressors nor pious and proud,  
We know not the dual paths of the crowd!  

O Bulleh, whose soul is absorbed in the Lord divine,  
Transcends Hindu and Muslim, beyond every line!"""

batch.append({
    "id": 40,
    "title": "40. हिन्दू ना नहीं मुसलमान",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k40_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "हिन्दू ना नहीं मुसलमान ।",
                "hindi_gloss": "हिन्दू (हिन्दू) ना (न) नहीं (न ही) मुसलमान (मुसलमान) ।",
                "english_gloss": "hindoo (Hindu) na (neither) naaheen (nor) musalmaan (Muslim) ."
            },
            {
                "original": "बहीए त्रिंजन तज अभिमान ।",
                "hindi_gloss": "बहीए (बैठते हैं) त्रिंजन (सत्संग की सभा में) तज (त्यागकर) अभिमान (अहंकार और गर्व) ।",
                "english_gloss": "baheeye (let us sit) trinjan (in spinning-circle/communion) taj (abandoning) abhimaan (pride/arrogance) ."
            },
            {
                "original": "सुन्नी ना नहीं हम शिया ।",
                "hindi_gloss": "सुन्नी (सुन्नी) ना (न) नहीं (न ही) हम (हम) शिया (शिया) ।",
                "english_gloss": "sunnee (Sunni) na (neither) naaheen (nor) ham (we) sheeya (Shia) ."
            },
            {
                "original": "सुल्हा कुल्ल का मारग लिया ।",
                "hindi_gloss": "सुल्हा (सुलह) कुल्ल (सर्व-शांति/सार्वभौमिक प्रेम) का (का) मारग (मार्ग) लिया (स्वीकार किया है) ।",
                "english_gloss": "sulha (peace with) kull (all creation/universal reconciliation) ka (of) maarag (path) liya (have taken) ."
            },
            {
                "original": "भुक्खे ना नहीं हम रज्जे ।",
                "hindi_gloss": "भुक्खे (भूखे) ना (न) नहीं (न ही) हम (हम) रज्जे (तृप्त/रजे-पुजे) ।",
                "english_gloss": "bhukkhe (hungry) na (neither) naaheen (nor) ham (we) rajje (sated/full) ."
            },
            {
                "original": "नंगे ना नहीं हम कज्जे ।",
                "hindi_gloss": "नंगे (नग्न) ना (न) नहीं (न ही) हम (हम) कज्जे (वस्त्रों से ढके) ।",
                "english_gloss": "nange (naked) na (neither) naaheen (nor) ham (we) kajje (clothed/covered) ."
            },
            {
                "original": "रोंदे ना नहीं हम हस्सदे ।",
                "hindi_gloss": "रोंदे (रोने वाले) ना (न) नहीं (न ही) हम (हम) हस्सदे (हँसने वाले) ।",
                "english_gloss": "ronde (weeping) na (neither) naaheen (nor) ham (we) hassde (laughing) ."
            },
            {
                "original": "उजड़े ना नहीं हम वस्सदे ।",
                "hindi_gloss": "उजड़े (उजड़े हुए) ना (न) नहीं (न ही) हम (हम) वस्सदे (बसे हुए) ।",
                "english_gloss": "ujde (ruined/desolate) na (neither) naaheen (nor) ham (we) vassde (settled/dwelling) ."
            },
            {
                "original": "पापी ना सुधरमी ना ।",
                "hindi_gloss": "पापी (पापी) ना (न) सुधरमी (धर्मात्मा) ना (न) ।",
                "english_gloss": "paapee (sinner) na (neither) sudharmee (righteous/virtuous) na (nor) ."
            },
            {
                "original": "पाप पुन्न की राह ना जाणा ।",
                "hindi_gloss": "पाप (पाप) पुन्न (और पुण्य) की (का) राह (सांसारिक मार्ग) ना (नहीं) जाणा (जानते) ।",
                "english_gloss": "paap (sin) punn (virtue) kee (of) raah (path) na (not) jaana (know) ."
            },
            {
                "original": "बुल्ल्हा शहु जो हरि चित लागे ।",
                "hindi_gloss": "बुल्ल्हा (हे बुल्ले) शहु (प्राण-स्वामी) जो (जो) हरि (हरि/परमात्मा के) चित (चित्त/ध्यान में) लागे (रम गया),",
                "english_gloss": "bullha (O Bulleh) shahu (the Lord) jo (who) hari (in the Divine) chit (heart/mind) laage (is absorbed),"
            },
            {
                "original": "हिन्दू तुर्क दूजन त्यागे ।",
                "hindi_gloss": "हिन्दू (हिन्दू और) तुर्क (तुर्क/मुस्लिम के) दूजन (द्वैत/भेदभाव को) त्यागे (त्याग देता है) ।",
                "english_gloss": "hindoo (Hindu) turk (Turk/Muslim) doojan (duality/division) tyaage (renounces) ."
            }
        ],
        "hindi_meaning": k40_hi,
        "english_meaning": k40_en
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
