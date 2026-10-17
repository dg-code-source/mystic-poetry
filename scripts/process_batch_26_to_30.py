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
# KAFI 26: 26. ढोला आदमी बण आया
# ==========================================
k26_orig = """आपे आहू आपे चीता, आपे मारन धाइआ,
आपे साहब आपे बरदा, आपे मुल्ल विकाइआ,
ढोला आदमी बण आया ।

कदी हाथी ते असवार होया, कदी ठूठा डांग भुवाइआ,
कदी रावल जोगी भोगी हो के, सांगी सांग बणाइआ,
ढोला आदमी बण आया ।

बाज़ीगर क्या बाज़ी खेली, मैनूं पुतली वांग नचाइआ,
मैं उस पड़ताली नचना हां, जिस गत मित यार लखाइआ,
ढोला आदमी बण आया ।

हाबील काबील आदम दे जाए, आदम किस दा जाइआ,
बुल्ल्हा उन्हां तों भी अग्गे आहा, दादा गोद खिडाइआ,
ढोला आदमी बण आया ।

पाठ-भेद

मौला आदमी बण आया
माटी विचों हीरा लद्धा,
गोबर महं दुद्ध पाइआ ।रहाउ।

सभो ऊठ कतारीं बद्धे
धन्ने दा वग्ग चराइआ ।
साडी भाजी लेवे नाहीं
बिदर दे साग अघाइआ ।

कहूं हाथी असवार होया,
कहूं ठूठा भांग भुवाइआ ।
कहूं रावल जोगी भोगी
कहूं सवांगी सवांग रचाइआ ।

आपे आहू आपे चीता
आपे मारन धाइआ ।
आपे साहब आपे बरदा
आपे मुल्ल विकाइआ ।

बाज़ीगर क्या बाज़ी खेली
पुतली वांग नचाया ।
मैं उस पड़ताली नच्चना हां
जिस गत मत यार लखाया ।

हाबील काबील आदम दे जाए
ते आदम कैं दा जाइआ ?
बुल्ल्हा सभना थीं अगै आहा
जिन दादा गोदि दिखाइआ ।"""

k26_hi = """स्वयं ही हिरण बना और स्वयं ही चीता बन झपट पड़ा,  
स्वयं ही मालिक बना जहाँ का, स्वयं ही गुलाम बन बिक पड़ा!  
अरे देखो! प्यारा साजन स्वयं मनुष्य बन आया है!  

कभी गजराज पर सवार हुआ, कभी भिक्षा-पात्र और लाठी घुमाया,  
कभी साधु-योगी और कभी संसारी बन, लीला का वेश बनाया!  
अरे देखो! प्यारा साजन स्वयं मनुष्य बन आया है!  

उस नटवर बाज़ीगर ने क्या अद्भुत लीला रची, मुझे कठपुतली-सा नचाया,  
मैं तो उसी की ताल पर नाचूँ, जिस ताल का मर्म मेरे प्रीतम ने सिखाया!  
अरे देखो! प्यारा साजन स्वयं मनुष्य बन आया है!  

हाबील और क़ाबील आदम के बेटे थे, पर आदम किसका बेटा था?  
बुल्ला तो उन सबसे भी पहले था, जिसने दादा आदम को गोद में खिलाया!  
अरे देखो! प्यारा साजन स्वयं मनुष्य बन आया है!  

(पाठ-भेद):
वह परमेश्वर स्वयं मनुष्य बन आया है,  
जैसे माटी की ढेरी से अनमोल हीरा मिल गया,  
जैसे गोबर के बीच में अमृत-दूध समाया है!  

धन्ना जाट के पशु चराए, ऊँटों की कतारें बाँधीं,  
दुर्योधन के छप्पन भोग ठुकराए, विदुर के भाजी-साग से तृप्त हुआ!  
कहीं हाथी पर हुआ सवार, कहीं भिक्षापात्र में भांग घुमाया,  
कहीं जोगी, कहीं भोगी, कहीं बहुरूपिया बन रूप बनाया!  
स्वयं ही हिरण, स्वयं ही चीता, स्वयं शिकार बन मार खाया,  
स्वयं ही प्रभु, स्वयं ही दास, स्वयं कौड़ियों के मोल बिकाया!  
कैसी बाज़ी खेली बाज़ीगर ने, कठपुतली की नाईं नचाया,  
मैं उसी ताल पर नाचा हूँ, जो भेद मेरे साजन ने लखाया!  
हाबील-क़ाबील आदम के बेटे, पर आदम किसका बेटा था?  
बुल्ला उन सबसे भी पहले था, जिसने दादा आदम को गोद खिलाया!"""

k26_en = """He Himself is the gazelle, Himself the tiger leaping to slay,  
He Himself is the sovereign Master, Himself the slave sold away!  
Behold, the Beloved in mortal form has come today!  

At times He rides the royal elephant high in noble state,  
At times a beggar’s bowl and staff become His wandering fate!  
Now a detached ascetic yogi, now enjoying worldly delight,  
An actor donning countless masks before our wondering sight!  
Behold, the Beloved in mortal form has come today!  

What a dazzling show the cosmic Juggler has begun,  
Making me dance like a puppet beneath the starry sun!  
I dance in rhythmic rapture to the beat of His command,  
To the secret cosmic cadence revealed by His own hand!  
Behold, the Beloved in mortal form has come today!  

Cain and Abel were born of Adam, but who gave Adam birth?  
Bulleh existed long before them, prior to heaven and earth!  
For in the timeless lap of Spirit, he cradled Adam as a child,  
When the Beloved took human form and through creation smiled!  
Behold, the Beloved in mortal form has come today!  

(Variant Reading):
The Sovereign Lord has descended in human grace,  
A radiant diamond discovered in clay's embrace,  
Pure celestial nectar hidden in humble place!  
He tended the herds for Dhanna, the simple devotee,  
Spurning royal banquets for Vidura’s leafy dish of glee!  
Here an emperor riding his elephant in proud array,  
There swirling herbal brew in a beggar’s bowl of clay!  
Yogi and king, hunter and prey in eternal flight,  
Master and servant, selling Himself in broad daylight!  
What a mystic play the Cosmic Magician weaves,  
Danced by puppets on strings between shadows and leaves!  
I dance to the cadence my Beloved whispered to my soul:  
Adam's sons were many, but Bulleh held the whole,  
Cradling the primordial father before time began its race,  
When the Lord took mortal breath to show His boundless grace!"""

batch.append({
    "id": 26,
    "title": "26. ढोला आदमी बण आया",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k26_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "आपे आहू आपे चीता, आपे मारन धाइआ,",
                "hindi_gloss": "आपे (स्वयं ही) आहू (मृग/हिरण) आपे (स्वयं ही) चीता (चीता/व्याघ्र), आपे (स्वयं ही) मारन (शिकार करने/मारने) धाइआ (दौड़ता है),",
                "english_gloss": "aape (Himself) aahoo (the deer) aape (Himself) cheeta (the cheetah), aape (Himself) maaran (to strike/slay) dhaaia (rushes forward),"
            },
            {
                "original": "आपे साहब आपे बरदा, आपे मुल्ल विकाइआ,",
                "hindi_gloss": "आपे (स्वयं ही) साहब (स्वामी/मालिक) आपे (स्वयं ही) बरदा (दास/गुलाम), आपे (स्वयं ही) मुल्ल (मूल्य पर) विकाइआ (बिक जाता है),",
                "english_gloss": "aape (Himself) saahab (the Lord/master) aape (Himself) barda (the servant/slave), aape (Himself) mull (for a price) vikaaia (sells Himself),"
            },
            {
                "original": "ढोला आदमी बण आया ।",
                "hindi_gloss": "ढोला (परम प्रियतम) आदमी (मनुष्य का रूप) बण (बनकर) आया (आया है) ।",
                "english_gloss": "dhola (the Beloved) aadmi (human being) ban (becoming) aaya (has arrived) ."
            },
            {
                "original": "कदी हाथी ते असवार होया, कदी ठूठा डांग भुवाइआ,",
                "hindi_gloss": "कदी (कभी) हाथी (हाथी) ते (पर) असवार (सवार) होया (होता है), कदी (कभी) ठूठा (मिट्टी का भिक्षापात्र) डांग (और लाठी) भुवाइआ (घुमाता है),",
                "english_gloss": "kadi (sometimes) haathi (elephant) te (upon) asvaar (mounted) hoya (He is), kadi (sometimes) thootha (begging-bowl) daang (staff) bhuwaaia (He waves),"
            },
            {
                "original": "कदी रावल जोगी भोगी हो के, सांगी सांग बणाइआ,",
                "hindi_gloss": "कदी (कभी) रावल (अलख जगाने वाला साधु) जोगी (योगी) भोगी (और भोगी संसारी) हो के (होकर), सांगी (बहुरूपिया बन) सांग (स्वांग/लीला-वेश) बणाइआ (रचता है),",
                "english_gloss": "kadi (sometimes) raaval (wandering ascetic) jogi (yogi) bhogi (worldly enjoyer) ho ke (becoming), saangi (actor/mimic) saang (role/guise) banaaia (enacts),"
            },
            {
                "original": "ढोला आदमी बण आया ।",
                "hindi_gloss": "ढोला (परम प्रियतम) आदमी (मनुष्य रूप) बण (बनकर) आया (आया है) ।",
                "english_gloss": "dhola (the Beloved) aadmi (human) ban (becoming) aaya (has come) ."
            },
            {
                "original": "बाज़ीगर क्या बाज़ी खेली, मैनूं पुतली वांग नचाइआ,",
                "hindi_gloss": "बाज़ीगर (उस बाज़ीगर/मायावी नट ने) क्या (कैसी अद्भुत) बाज़ी (लीला/खेल) खेली (खेला है), मैनूं (मुझको) पुतली (कठपुतली के) वांग (समान) नचाइआ (नचाया है),",
                "english_gloss": "baazeegar (the master juggler) kya (what a) baazee (mystic game) khelee (has played), mainoon (me) putlee (puppet) vaang (like) nachaaia (He made to dance),"
            },
            {
                "original": "मैं उस पड़ताली नचना हां, जिस गत मित यार लखाइआ,",
                "hindi_gloss": "मैं (मैं) उस (उस) पड़ताली (ताल/लय पर) नचना (नाचता) हां (हूँ), जिस (जिस) गत (चाल) मित (और ताल का भेद) यार (मेरे प्रियतम ने) लखाइआ (मुझे समझाया/दिखाया है),",
                "english_gloss": "main (I) us (to that) padtaalee (rhythm/beat) nachna (dance) haan (do), jis (which) gat (step) mit (measure/tune) yaar (Beloved) lakhaaia (revealed to me),"
            },
            {
                "original": "ढोला आदमी बण आया ।",
                "hindi_gloss": "ढोला (परम प्रियतम) आदमी (इंसान) बण (बनकर) आया (आया है) ।",
                "english_gloss": "dhola (the Beloved) aadmi (human) ban (becoming) aaya (has come) ."
            },
            {
                "original": "हाबील काबील आदम दे जाए, आदम किस दा जाइआ,",
                "hindi_gloss": "हाबील (हाबील) काबील (और क़ाबील) आदम (बाबा आदम) दे (के) जाए (पुत्र/जन्मे हैं), आदम (किंतु आदम) किस (किससे) दा (का) जाइआ (उत्पन्न हुआ/किसका बेटा है),",
                "english_gloss": "haabeel (Abel) kaabeel (Cain) aadam (of Adam) de (of) jaae (sons/born of), aadam (Adam) kis (whose) da (of) jaaia (son/born of),"
            },
            {
                "original": "बुल्ल्हा उन्हां तों भी अग्गे आहा, दादा गोद खिडाइआ,",
                "hindi_gloss": "बुल्ल्हा (बुल्ले शाह/वह अमर आत्मा) उन्हां (उन सबसे) तों (से) भी (भी) अग्गे (पहले विद्यमान) आहा (था), दादा (और उसने आदि-पिता आदम को) गोद (गोद में) खिडाइआ (खिलाया है),",
                "english_gloss": "bullha (Bulleh/the primordial Soul) unhaan (them) ton (than) bhee (even) agge (before/prior) aaha (was), daada (the grandfather/Adam) god (in his lap) khidaaia (He dandled/cradled),"
            },
            {
                "original": "ढोला आदमी बण आया ।",
                "hindi_gloss": "ढोला (परम प्रियतम) आदमी (मनुष्य रूप) बण (बनकर) आया (आया है) ।",
                "english_gloss": "dhola (the Beloved) aadmi (human) ban (becoming) aaya (has come) ."
            },
            {
                "original": "पाठ-भेद",
                "hindi_gloss": "पाठ-भेद (पाठ-भेद / अन्य प्रामाणिक पाठान्तर) :",
                "english_gloss": "paath-bhed (Variant Reading / Alternate Textual Tradition) :"
            },
            {
                "original": "मौला आदमी बण आया",
                "hindi_gloss": "मौला (परमेश्वर/प्रभु) आदमी (मनुष्य) बण (बनकर) आया (आया है),",
                "english_gloss": "maula (the Lord Divine) aadmi (man) ban (becoming) aaya (has arrived),"
            },
            {
                "original": "माटी विचों हीरा लद्धा,",
                "hindi_gloss": "माटी (माटी/मिट्टी) विचों (में से) हीरा (अमूल्य हीरा) लद्धा (खोज निकाला है),",
                "english_gloss": "maatee (from clay) vichon (out of) heera (diamond) laddha (discovered),"
            },
            {
                "original": "गोबर महं दुद्ध पाइआ ।रहाउ।",
                "hindi_gloss": "गोबर (गोबर/गोमय) महं (में से पवित्र) दुद्ध (दुग्ध/अमृत) पाइआ (प्राप्त कर लिया है) ।रहाउ (टेक/विश्राम) ।",
                "english_gloss": "gobar (cow dung) mahan (within) duddh (pure milk) paaia (obtained) .rahaau (refrain) ."
            },
            {
                "original": "सभो ऊठ कतारीं बद्धे",
                "hindi_gloss": "सभो (समस्त) ऊठ (ऊंटों को) कतारीं (पंक्तियों में) बद्धे (बाँध दिया),",
                "english_gloss": "sabho (all) ooth (camels) kataareen (in lines) baddhe (bound),"
            },
            {
                "original": "धन्ने दा वग्ग चराइआ ।",
                "hindi_gloss": "धन्ने (भक्त धन्ना) दा (का) वग्ग (गोधन/पशुओं का झुंड) चराइआ (स्वयं चराया) ।",
                "english_gloss": "dhanne (of devotee Dhanna) da (of) vagg (herd of cattle) charaaia (He grazed) ."
            },
            {
                "original": "साडी भाजी लेवे नाहीं",
                "hindi_gloss": "साडी (हमारी अहंकार भरी) भाजी (व्यंजनों की भेंट) लेवे (स्वीकार करता) नाहीं (नहीं),",
                "english_gloss": "saadee (our proud) bhaajee (feasts/offerings) leve (accepts) naaheen (not),"
            },
            {
                "original": "बिदर दे साग अघाइआ ।",
                "hindi_gloss": "बिदर (भक्त विदुर) दे (के) साग (सरल बथुए के साग से ही) अघाइआ (तृप्त हो गया) ।",
                "english_gloss": "bidar (of Vidura) de (of) saag (simple greens/spinach) aghaaia (He was satiated) ."
            },
            {
                "original": "कहूं हाथी असवार होया,",
                "hindi_gloss": "कहूं (कहीं) हाथी (हाथी पर) असवार (सवार) होया (हो गया),",
                "english_gloss": "kahoon (somewhere) haathi (elephant) asvaar (mounted) hoya (He became),"
            },
            {
                "original": "कहूं ठूठा भांग भुवाइआ ।",
                "hindi_gloss": "कहूं (कहीं) ठूठा (भिक्षापात्र में) भांग (भांग को) भुवाइआ (घोटकर पीता है),",
                "english_gloss": "kahoon (somewhere) thootha (begging-bowl) bhaang (hemp) bhuwaaia (He swirls),"
            },
            {
                "original": "कहूं रावल जोगी भोगी",
                "hindi_gloss": "कहूं (कहीं) रावल (सन्यासी) जोगी (योगी अथवा) भोगी (सांसारिक विलासी),",
                "english_gloss": "kahoon (somewhere) raaval (ascetic) jogi (yogi) bhogi (pleasure-seeker),"
            },
            {
                "original": "कहूं सवांगी सवांग रचाइआ ।",
                "hindi_gloss": "कहूं (कहीं) सवांगी (बहुरूपिया बन) सवांग (विचित्र स्वांग) रचाइआ (रचता है) ।",
                "english_gloss": "kahoon (somewhere) savaangee (impersonator) savaang (disguise) rachaaia (He assumes) ."
            },
            {
                "original": "आपे आहू आपे चीता",
                "hindi_gloss": "आपे (स्वयं ही) आहू (मृग) आपे (स्वयं ही) चीता (चीता),",
                "english_gloss": "aape (Himself) aahoo (the deer) aape (Himself) cheeta (the cheetah),"
            },
            {
                "original": "आपे मारन धाइआ ।",
                "hindi_gloss": "आपे (स्वयं ही) मारन (शिकार करने) धाइआ (झपटता है) ।",
                "english_gloss": "aape (Himself) maaran (to kill) dhaaia (He lunges) ."
            },
            {
                "original": "आपे साहब आपे बरदा",
                "hindi_gloss": "आपे (स्वयं ही) साहब (मालिक) आपे (स्वयं ही) बरदा (दास),",
                "english_gloss": "aape (Himself) saahab (master) aape (Himself) barda (slave),"
            },
            {
                "original": "आपे मुल्ल विकाइआ ।",
                "hindi_gloss": "आपे (स्वयं ही) मुल्ल (दाम देकर) विकाइआ (बिक जाता है) ।",
                "english_gloss": "aape (Himself) mull (for a price) vikaaia (sells Himself) ."
            },
            {
                "original": "बाज़ीगर क्या बाज़ी खेली",
                "hindi_gloss": "बाज़ीगर (उस बाज़ीगर ने) क्या (कैसी विचित्र) बाज़ी (बाजी) खेली (खेली है),",
                "english_gloss": "baazeegar (the juggler) kya (what) baazee (game) khelee (played),"
            },
            {
                "original": "पुतली वांग नचाया ।",
                "hindi_gloss": "पुतली (कठपुतली के) वांग (समान सबको) नचाया (नचाया है) ।",
                "english_gloss": "putlee (puppet) vaang (like) nachaaya (danced us) ."
            },
            {
                "original": "मैं उस पड़ताली नच्चना हां",
                "hindi_gloss": "मैं (मैं) उस (उसकी) पड़ताली (ताल पर) नच्चना (नाचता) हां (हूँ),",
                "english_gloss": "main (I) us (His) padtaalee (rhythm) nachhna (dance) haan (do),"
            },
            {
                "original": "जिस गत मत यार लखाया ।",
                "hindi_gloss": "जिस (जिस) गत (गति) मत (और मति का रहस्य) यार (प्रियतम ने) लखाया (दिखाया है) ।",
                "english_gloss": "jis (which) gat (dance-movement) mat (wisdom) yaar (Beloved) lakhaaya (revealed) ."
            },
            {
                "original": "हाबील काबील आदम दे जाए",
                "hindi_gloss": "हाबील (हाबील) काबील (और क़ाबील) आदम (आदम) दे (के) जाए (पुत्र हैं),",
                "english_gloss": "haabeel (Abel) kaabeel (Cain) aadam (of Adam) de (of) jaae (sons born),"
            },
            {
                "original": "ते आदम कैं दा जाइआ ?",
                "hindi_gloss": "ते (और) आदम (आदम) कैं (किसका) दा (का) जाइआ (पुत्र था) ?",
                "english_gloss": "te (and) aadam (Adam) kain (whose) da (of) jaaia (son/born) ?"
            },
            {
                "original": "बुल्ल्हा सभना थीं अगै आहा",
                "hindi_gloss": "बुल्ल्हा (बुल्ले का मूल आत्म-रूप) सभना (उन सब) थीं (से) अगै (पूर्व ही विद्यमान) आहा (था),",
                "english_gloss": "bullha (Bulleh) sabhna (all of them) theen (than) agai (prior/before) aaha (was),"
            },
            {
                "original": "जिन दादा गोदि दिखाइआ ।",
                "hindi_gloss": "जिन (जिसने) दादा (आदि-पिता आदम को) गोदि (अपनी गोद में) दिखाइआ (लाड़-प्यार से खिलाया) ।",
                "english_gloss": "jin (who) daada (the grandfather/Adam) godi (in lap) dikhaaia (nurtured) ."
            }
        ],
        "hindi_meaning": k26_hi,
        "english_meaning": k26_en
    }]
})

# ==========================================
# KAFI 27: 27. दिल लोचे माही यार नूं
# ==========================================
k27_orig = """इक हस्स हस्स गल्ल करदीआं, इक रोंदीआं धोंदीआं मरदीआं,
कहो फुल्ली बसंत बहार नूं, दिल लोचे माही यार नूं ।

मैं न्हाती धोती रह गई, इक गंढ माही दिल बह गई,
भाह लाईए हार शिंगार नूं, दिल लोचे माही यार नूं ।

मैं कमली कीती दूतियां, दुक्ख घेर चुफेरों लीतियां,
घर आ माही दीदार नूं, दिल लोचे माही यार नूं ।

बुल्ल्हा शौह मेरे घर आया, मैं घुट्ट रांझण गल लाइआ,
दुक्ख गए समुन्दर पार नूं, दिल लोचे माही यार नूं ।"""

k27_hi = """कुछ सखियाँ हँस-हँसकर बातें करती हैं, और कुछ विरह में रो-रोकर मरती हैं,  
जाकर कह दो वसंत की इस बहार से, यह दिल तो बस प्यारे साजन को तरसता है!  

मैं नहा-धोकर श्रृंगार ही करती रह गई, पर साजन के दिल में विरह की गाँठ पड़ गई,  
आग लगे इस हार और श्रृंगार को, यह दिल तो बस प्यारे साजन को तरसता है!  

इस ज़माने के तानों ने मुझे बावरी कर दिया, चारों तरफ से दुःखों ने मुझे घेर लिया,  
हे प्रीतम! दर्शन देने घर आ जाओ, यह दिल तो बस प्यारे साजन को तरसता है!  

बुल्ले के घर जब प्राण-स्वामी पधारे, मैंने भींचकर रांझा को गले लगाया,  
सारे दुःख सात समंदर पार भाग गए, यह दिल जो प्यारे साजन को तरसता था!"""

k27_en = """Some maidens laugh and whisper in sheer delight,  
While others weep, consumed by yearning’s night!  
Go tell the blooming spring with all its flowers,  
My heart seeks only the Beloved in lonely hours!  

I bathed and cleansed myself with tender care,  
Yet doubt formed a bitter knot in my lover’s lair!  
Cast all ornaments and necklaces into the fire,  
The Beloved alone is my spirit's sole desire!  

Cruel slanderers have driven me completely wild,  
Sufferings hem me in, no longer gentle or mild!  
Return to my courtyard, O Beloved, let me see your face,  
My heart longs only for your healing embrace!  

When the Lord crossed my threshold and stepped inside,  
I clutched my Ranjha tightly, my soul’s true bride!  
All sorrow fled across the distant sea,  
For my yearning heart was unified and free!"""

batch.append({
    "id": 27,
    "title": "27. दिल लोचे माही यार नूं",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k27_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "इक हस्स हस्स गल्ल करदीआं, इक रोंदीआं धोंदीआं मरदीआं,",
                "hindi_gloss": "इक (कुछ सखियाँ) हस्स (हँस-हँसकर) हस्स (प्रसन्नता से) गल्ल (बातें) करदीआं (करती हैं), इक (और कुछ विरहिणी) रोंदीआं (रो-रोकर) धोंदीआं (आँसुओं से धुलती) मरदीआं (तड़पकर मर रही हैं),",
                "english_gloss": "ik (some) hass (laughing) hass (joyfully) gall (conversations) kardiaan (make), ik (and others) rondeeyaan (weeping) dhondeeyaan (washed in tears) mardeeyaan (dying in agony),"
            },
            {
                "original": "कहो फुल्ली बसंत बहार नूं, दिल लोचे माही यार नूं ।",
                "hindi_gloss": "कहो (कह दो उस) फुल्ली (खिली हुई) बसंत (वसंत ऋतु की) बहार (बहार/उल्लास) नूं (से), दिल (कि मेरा हृदय केवल) लोचे (चाहता/तरसता है) माही (मेरे प्रियतम) यार (प्यारे) नूं (के लिए) ।",
                "english_gloss": "kaho (tell) phullee (blossomed) basant (spring) bahaar (bloom) noon (unto), dil (my heart) loche (yearns for) maahi (the Beloved) yaar (Friend) noon (unto) ."
            },
            {
                "original": "मैं न्हाती धोती रह गई, इक गंढ माही दिल बह गई,",
                "hindi_gloss": "मैं (मैं तो केवल) न्हाती (नहाती) धोती (सजती-धजती) रह गई (रह गई), इक (परंतु एक) गंढ (गहरी गाँठ/संदेह या विरह की टीस) माही (प्रियतम के) दिल (हृदय में) बह (बैठ) गई (गई है),",
                "english_gloss": "main (I) nhaatee (bathed) dhotee (cleansed) rah (remained) gayee (having been), ik (one) gandh (knot/distrust) maahi (the Beloved's) dil (heart) bah (settled) gayee (in),"
            },
            {
                "original": "भाह लाईए हार शिंगार नूं, दिल लोचे माही यार नूं ।",
                "hindi_gloss": "भाह (आग) लाईए (लगा दी जाए) हार (इस हार) शिंगार (और साज-श्रृंगार) नूं (को), दिल (यह मन तो केवल) लोचे (तरसता है) माही (प्रियतम) यार (यार) नूं (के मिलन को) ।",
                "english_gloss": "bhaah (fire) laaee-e (let us set to) haar (necklace) shingaar (adornment) noon (unto), dil (heart) loche (longs for) maahi (Beloved) yaar (Friend) noon (unto) ."
            },
            {
                "original": "मैं कमली कीती दूतियां, दुक्ख घेर चुफेरों लीतियां,",
                "hindi_gloss": "मैं (मुझको) कमली (बावरी/पागल) कीती (बना दिया) दूतियां (द्वेषी निंदकों और दूतों ने), दुक्ख (और दुःखों ने मुझे) घेर (घेरकर) चुफेरों (चारों तरफ़ से) लीतियां (जकड़ लिया है),",
                "english_gloss": "main (me) kamlee (crazed) keetee (made) dooteeyan (scornful slanderers), dukkh (sorrows) gher (surrounding) chupheron (from all sides) leeteeyaan (have seized),"
            },
            {
                "original": "घर आ माही दीदार नूं, दिल लोचे माही यार नूं ।",
                "hindi_gloss": "घर (मेरे घर के आँगन) आ (आ जाओ) माही (हे प्रियतम) दीदार (अपने पावन दर्शन) नूं (के लिए), दिल (मेरा हृदय) लोचे (तड़पता है) माही (प्रियतम) यार (यार) नूं (के लिए) ।",
                "english_gloss": "ghar (to home) aa (come) maahi (O Beloved) deedaar (sight/vision) noon (for), dil (heart) loche (yearns for) maahi (Beloved) yaar (Friend) noon (unto) ."
            },
            {
                "original": "बुल्ल्हा शौह मेरे घर आया, मैं घुट्ट रांझण गल लाइआ,",
                "hindi_gloss": "बुल्ल्हा (बुल्ले शाह कहते हैं कि जब) शौह (परम स्वामी) मेरे (मेरे) घर (हृदय-आँगन में) आया (पधारे), मैं (मैंने) घुट्ट (कसकर/भींचकर) रांझण (प्यारे रांझा को) गल (गले से) लाइआ (लगा लिया),",
                "english_gloss": "bullha (Bulleh Shah says when) shauh (the Lord) mere (my) ghar (home) aaya (came), main (I) ghutt (tightly) raanjhan (Ranjha) gal (to bosom/neck) laaia (embraced),"
            },
            {
                "original": "दुक्ख गए समुन्दर पार नूं, दिल लोचे माही यार नूं ।",
                "hindi_gloss": "दुक्ख (मेरे समस्त दुःख) गए (चले गए) समुन्दर (सात समंदर) पार (पार दूर) नूं (को), दिल (जो दिल सदा) लोचे (तरसता था) माही (प्रियतम) यार (यार) नूं (के लिए) ।",
                "english_gloss": "dukkh (all sorrows) gae (departed) samundar (ocean) paar (across) noon (unto), dil (heart) loche (longed for) maahi (Beloved) yaar (Friend) noon (unto) ."
            }
        ],
        "hindi_meaning": k27_hi,
        "english_meaning": k27_en
    }]
})

# ==========================================
# KAFI 28: 28. इह अचरज साधो कौण कहावे
# ==========================================
k28_orig = """इह अचरज साधो कौण कहावे ।
छिन छिन रूप कितों बण आवे ।

मक्का लंका सहदेव के भेत, दोऊ को एक बतावे ।
जब जोगी तुम वसल करोगे, बांग कहै भावें नाद वजावे ।
भगती भगत नतारो नाहीं, भगत सोई जेहड़ा मन भावे ।
हर परगट परगट ही देखो, क्या पंडत फिर बेद सुनावे ।
ध्यान धरो इह काफ़र नाहीं, क्या हिन्दू क्या तुर्क कहावे ।
जब देखूं तब ओही ओही, बुल्ल्हा शौह हर रंग समावे ।

इह अचरज साधो कौण कहावे ।
छिन छिन रूप कितों बण आवे ।"""

k28_hi = """हे साधो! इस अद्भुत रहस्य का बखान कौन कर सकता है?  
जो प्रतिक्षण किसी न किसी नवीन रूप में सामने आ जाता है!  

चाहे मक्का हो, लंका हो या सहदेव का ज्योतिष-भेद,  
वह ज्ञानी दोनों में एक ही अद्वैत सत्ता को देखता है!  
हे योगी! जब तुम उस परम प्रियतम से एकाकार हो जाओगे,  
चाहे मस्जिद की अज़ान पुकारे या मंदिर का नाद गूँजे, सब एक ही है!  
भक्ति और भक्त में बाह्य भेद मत करो,  
सच्चा भक्त वही है जो उस परमात्मा के मन को भा जाए!  
जब हरि साक्षात प्रत्यक्ष दिखाई दे रहे हैं,  
तो पंडित फिर पोथियों और वेदों की कथा क्यों सुनाए?  
ध्यान से समझो, यह प्रेमी कोई काफ़िर नहीं है,  
संसार चाहे उसे हिन्दू कहे या तुर्क पुकारे!  
मैं जिधर भी देखता हूँ, बस वही-वही नज़र आता है,  
बुल्ले का शाह हर रंग और हर रूप में समाया हुआ है!  

हे साधो! इस अद्भुत रहस्य का बखान कौन कर सकता है?  
जो प्रतिक्षण किसी न किसी नवीन रूप में सामने आ जाता है!"""

k28_en = """O seekers of Truth, who can utter this wondrous mystery,  
Which shapes a fresh countenance every moment in ecstasy!  

Whether Mecca's sanctuary or Lanka's ancient domain,  
He sees both as one undivided divine terrain!  
When thou art merged in the Beloved, O yogi enlightened and clear,  
The muezzin’s call or the conch’s resonant blow sound the same to thine ear!  
Judge not between forms of devotion or sects that divide,  
The true lover is the one in whose heart the Divine is pleased to abide!  
When the Lord is visibly shining everywhere before thine eyes,  
Why need the pundit repeat scripture beneath empty skies?  
Know with certainty that this ecstatic lover is no infidel or blind,  
Whether called a Hindu or a Muslim by the wandering worldly mind!  
Wherever I turn my gaze, He alone, He alone stands bright,  
Bulleh’s Lord permeates every hue of universal light!  

O seekers of Truth, who can utter this wondrous mystery,  
Which shapes a fresh countenance every moment in ecstasy!"""

batch.append({
    "id": 28,
    "title": "28. इह अचरज साधो कौण कहावे",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k28_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "इह अचरज साधो कौण कहावे ।",
                "hindi_gloss": "इह (यह) अचरज (विस्मयकारी सत्य) साधो (हे संतों/साधुओं) कौण (कौन) कहावे (समझाए/कहे) ।",
                "english_gloss": "eh (this) achraj (wondrous mystery) saadho (O seekers/saints) kaun (who) kahaave (can declare) ."
            },
            {
                "original": "छिन छिन रूप कितों बण आवे ।",
                "hindi_gloss": "छिन (क्षण) छिन (प्रतिक्षण) रूप (नया-नया रूप) कितों (कहीं न कहीं से) बण (बनकर) आवे (सामने आता है) ।",
                "english_gloss": "chhin (moment) chhin (by moment) roop (form) kiton (from everywhere) ban (taking shape) aave (manifests) ."
            },
            {
                "original": "मक्का लंका सहदेव के भेत, दोऊ को एक बतावे ।",
                "hindi_gloss": "मक्का (मक्का शरीफ़) लंका (और रावण की लंका अथवा) सहदेव (सहदेव ज्योतिषी) के (के) भेत (गूढ़ रहस्यों को), दोऊ (दोनों को) को (को) एक (एक समान अद्वैत) बतावे (बताता है) ।",
                "english_gloss": "makka (Mecca) lanka (Lanka) sahdev (Sahadeva's astrology) ke (of) bhet (mysteries), do-oo (both) ko (to) ek (one essence) bataave (reveals as) ."
            },
            {
                "original": "जब जोगी तुम वसल करोगे, बांग कहै भावें नाद वजावे ।",
                "hindi_gloss": "जब (जब) जोगी (हे योगी) तुम (तुम परमात्मा से) वसल (एकाकार/मिलन) करोगे (कर लोगे), बांग (चाहे कोई मस्जिद की अज़ान) कहै (पुकारे) भावें (अथवा) नाद (शंख/नाद) वजावे (बजाए, दोनों में एक ही गूँज है) ।",
                "english_gloss": "jab (when) jogi (O yogi) tum (you) vasal (divine union) karoge (attain), baang (call to prayer) kahai (chants) bhaaven (or) naad (conch horn) vajaave (sounds) ."
            },
            {
                "original": "भगती भगत नतारो नाहीं, भगत सोई जेहड़ा मन भावे ।",
                "hindi_gloss": "भगती (भक्ति और) भगत (भक्त में) नतारो (भेदभाव/विभाजन) नाहीं (मत करो), भगत (सच्चा भक्त) सोई (वही है) जेहड़ा (जो प्रभु के) मन (हृदय को) भावे (प्रिय लगे) ।",
                "english_gloss": "bhagatee (devotion) bhagat (devotee) nataaro (discriminate) naaheen (do not), bhagat (devotee) soee (is he) jehda (who to the Divine) man (heart) bhaave (is pleasing) ."
            },
            {
                "original": "हर परगट परगट ही देखो, क्या पंडत फिर बेद सुनावे ।",
                "hindi_gloss": "हर (हरि/प्रभु को) परगट (प्रत्यक्ष) परगट (प्रत्यक्ष रूप में) ही (ही) देखो (साक्षात निहारो), क्या (फिर क्या आवश्यकता कि) पंडत (पंडित) फिर (पुनः) बेद (वेदों की ऋचाएं) सुनावे (सुनाकर भ्रम में डाले) ।",
                "english_gloss": "har (the Divine Lord) pargat (manifest) pargat (directly visible) hee (indeed) dekho (behold), kya (why should) pandat (priest/scholar) phir (again) bed (Vedas) sunaave (recite) ."
            },
            {
                "original": "ध्यान धरो इह काफ़र नाहीं, क्या हिन्दू क्या तुर्क कहावे ।",
                "hindi_gloss": "ध्यान (चित्त में विचार) धरो (धारण करो) इह (यह परमात्मा या प्रेमी) काफ़र (काफ़िर/अधर्मी) नाहीं (नहीं है), क्या (चाहे संसार उसे) हिन्दू (हिन्दू) क्या (या) तुर्क (मुसलमान) कहावे (कहे) ।",
                "english_gloss": "dhyaan (mindful contemplation) dharo (hold) eh (this soul) kaafar (infidel) naaheen (is not), kya (whether) hindoo (Hindu) kya (or) turk (Muslim) kahaave (be called) ."
            },
            {
                "original": "जब देखूं तब ओही ओही, बुल्ल्हा शौह हर रंग समावे ।",
                "hindi_gloss": "जब (जब भी) देखूं (मैं दृष्टि डालता हूँ) तब (तब) ओही (वही परमेश्वर) ओही (केवल वही दिखाई देता है), बुल्ल्हा (हे बुल्ले) शौह (वह प्राण-स्वामी) हर (प्रत्येक) रंग (रंग-रूप में) समावे (समाया हुआ है) ।",
                "english_gloss": "jab (whenever) dekhoon (I look) tab (then) ohee (He alone) ohee (He alone is), bullha (O Bulleh) shauh (the Lord) har (in every) rang (hue/color) samaave (pervades) ."
            },
            {
                "original": "इह अचरज साधो कौण कहावे ।",
                "hindi_gloss": "इह (यह) अचरज (अद्भुत लीला) साधो (हे साधुओं) कौण (कौन) कहावे (वर्णन करे) ।",
                "english_gloss": "eh (this) achraj (wonder) saadho (O saints) kaun (who) kahaave (can declare) ."
            },
            {
                "original": "छिन छिन रूप कितों बण आवे ।",
                "hindi_gloss": "छिन (क्षण) छिन (प्रतिक्षण) रूप (उसका रूप) कितों (सर्वत्र) बण (नया रूप धरकर) आवे (प्रकट होता है) ।",
                "english_gloss": "chhin (moment) chhin (by moment) roop (form) kiton (from all realms) ban (becoming) aave (manifests) ."
            }
        ],
        "hindi_meaning": k28_hi,
        "english_meaning": k28_en
    }]
})

# ==========================================
# KAFI 29: 29. इह दुख जा कहूं किस आगे
# ==========================================
k29_orig = """इह दुख जा कहूं किस आगे,
रोम रोम घा प्रेम के लागे ।

इक मरना दूजा जग्ग दी हासी ।
करत फिरत नित्त मोही रे मोही ।

कौण करे मोहे से दिलजोई ।
शाम पिया मैं देती हूं धरोई ।

दुक्ख जग्ग के मोहे पूछन आए ।
जिन को पिया परदेस सिधाए ।

ना पिया जाए ना पिया आए ।
इह दुक्ख जा कहूं किस जाए ।

बुल्ल्हा शाह घर आ प्यारिआ ।
इक घड़ी को करन गुज़ारिआ ।
तन मन धन जिया तैं पर वारिआ ।

इह दुख जा कहूं किस आगे,
रोम रोम घा प्रेम के लागे ।"""

k29_hi = """यह विरह का दुःख मैं जाकर किसके आगे कहूँ?  
मेरे रोम-रोम में ईश्वरीय प्रेम के गहरे घाव लग गए हैं!  

एक तो विरह में तिल-तिल मरना, उस पर संसार की हँसी और ताने!  
मैं मतवाली होकर रात-दिन उसी के ध्यान में भटकती हूँ!  
मुझ अभागिन के दिल को भला कौन तसल्ली दे?  
हे मेरे साँवरिया प्यारे! मैं तुम्हें अपने प्रेम की दुहाई देती हूँ!  
दुनिया भर के सारे दुःख आज मुझसे मेरा हाल पूछने आ गए हैं,  
उन विरहिणियों की व्यथा जैसी जिनके साजन परदेस सिधार गए हों!  
न तो मेरा साजन आँखों से ओझल होता है, न ही साक्षात मिलने आता है,  
यह विचित्र दुःख मैं कहाँ जाकर और किससे कहूँ!  
हे बुल्ले के प्रियतम शाह! मेरे घर आ जाओ,  
कम-से-कम एक घड़ी के लिए ही अपना दीदार करा जाओ!  
मैंने अपना तन, मन, धन और यह प्राण सब तुम पर न्योछावर कर दिया है!  

यह विरह का दुःख मैं जाकर किसके आगे कहूँ?  
मेरे रोम-रोम में ईश्वरीय प्रेम के गहरे घाव लग गए हैं!"""

k29_en = """Before whom shall I unfold this secret sorrow of my heart?  
In every single pore, the deep wounds of Love impart!  

On one side lies this agonizing death, on the other the world's cold sneer,  
Enchanted and crazed I wander, yearning for my Sovereign dear!  
Who is there to soothe this aching breast and bring me consolation?  
O my dark-hued Shyam, I pledge my soul to thy sweet invocation!  
The world’s afflictions come to me to learn what sorrow means,  
Like lonely brides whose beloveds have fled across earthly scenes!  
He never truly goes away, yet never draws fully near,  
To which haven can I carry this torment, desolate and severe?  
O Beloved Lord of Bulleh, step into my humble door,  
If only for a single fleeting moment on this temporal shore!  
My body, heart, treasure, and very breath I yield entirely to thee!  

Before whom shall I unfold this secret sorrow of my heart?  
In every single pore, the deep wounds of Love impart!"""

batch.append({
    "id": 29,
    "title": "29. इह दुख जा कहूं किस आगे",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k29_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "इह दुख जा कहूं किस आगे,",
                "hindi_gloss": "इह (यह विरह का) दुख (दुःख) जा (जाकर) कहूं (मैं कहूँ) किस (किसके) आगे (सामने),",
                "english_gloss": "eh (this) dukkh (sorrow of separation) jaa (going) kahoon (shall I tell) kis (whom) aage (before),"
            },
            {
                "original": "रोम रोम घा प्रेम के लागे ।",
                "hindi_gloss": "रोम (मेरे रोम) रोम (रोम में) घा (गहरे घाव) प्रेम (इलाही प्रेम) के (के) लागे (लग चुके हैं) ।",
                "english_gloss": "rom (pore) rom (every pore) ghaa (wounds) prem (of divine love) ke (of) laage (are afflicted) ."
            },
            {
                "original": "इक मरना दूजा जग्ग दी हासी ।",
                "hindi_gloss": "इक (एक तो विरह की मृत्यु में) मरना (तिल-तिल मरना है) दूजा (और दूसरा) जग्ग (इस संसार) दी (की) हासी (उपहास/हँसी उड़ती है) ।",
                "english_gloss": "ik (first) marna (to perish) dooja (second) jagg (world's) dee (of) haasee (mockery/ridicule) ."
            },
            {
                "original": "करत फिरत नित्त मोही रे मोही ।",
                "hindi_gloss": "करत (करते) फिरत (फिरते हैं) नित्त (नित्य/सदा) मोही (मुझ मुग्धा को) रे (रे) मोही (व्याकुल और मोहित) ।",
                "english_gloss": "karat (doing) phirat (wandering) nitt (constantly) mohee (bewildered/charmed) re (O) mohee (enchanted) ."
            },
            {
                "original": "कौण करे मोहे से दिलजोई ।",
                "hindi_gloss": "कौण (कौन भला) करे (करेगा) मोहे (मुझ अभागिन) से (से) दिलजोई (सहानुभूति और तसल्ली भरी बातें) ।",
                "english_gloss": "kaun (who) kare (will offer) mohe (to me) se (with) diljoee (comfort/consolation) ."
            },
            {
                "original": "शाम पिया मैं देती हूं धरोई ।",
                "hindi_gloss": "शाम (हे श्याम/साँवरिया) पिया (प्रियतम) मैं (मैं तुम्हें) देती (देती) हूं (हूँ) धरोई (दुहाई/सौगंध) ।",
                "english_gloss": "shaam (O dark-hued Shyam) piya (Beloved) main (I) detee (give) hoon (do) dharoee (solemn oath/plea) ."
            },
            {
                "original": "दुक्ख जग्ग के मोहे पूछन आए ।",
                "hindi_gloss": "दुक्ख (संसार भर के समस्त) जग्ग (जगत) के (के) मोहे (मुझसे कुशल-क्षेम) पूछन (पूछने) आए (आए हैं),",
                "english_gloss": "dukkh (sorrows) jagg (of the world) ke (of) mohe (unto me) poochan (to inquire) aae (have come),"
            },
            {
                "original": "जिन को पिया परदेस सिधाए ।",
                "hindi_gloss": "जिन (जिन विरहिणियों) को (के) पिया (प्रियतम) परदेस (सुदूर परदेस) सिधाए (चले गए हों) ।",
                "english_gloss": "jin (whose) ko (of) piya (beloved) pardes (foreign land) sidhaae (have departed to) ."
            },
            {
                "original": "ना पिया जाए ना पिया आए ।",
                "hindi_gloss": "ना (न तो) पिया (प्रियतम मुझसे दूर) जाए (जाता है) ना (और न ही प्रत्यक्ष रूप में) पिया (प्रियतम) आए (आता है),",
                "english_gloss": "na (neither) piya (Beloved) jaae (departs) na (nor) piya (Beloved) aae (arrives),"
            },
            {
                "original": "इह दुक्ख जा कहूं किस जाए ।",
                "hindi_gloss": "इह (यह विचित्र) दुक्ख (पीड़ा) जा (जाकर) कहूं (मैं कहूँ) किस (किस) जाए (स्थान पर/किसके आगे) ।",
                "english_gloss": "eh (this) dukkh (torment) jaa (going) kahoon (shall I recount) kis (which) jaae (place/person) ."
            },
            {
                "original": "बुल्ल्हा शाह घर आ प्यारिआ ।",
                "hindi_gloss": "बुल्ल्हा (बुल्ले के) शाह (प्राण-स्वामी) घर (मेरे घर-आँगन में) आ (आ जाओ) प्यारिआ (हे प्यारे) ।",
                "english_gloss": "bullha (Bulleh's) shaah (Lord) ghar (home) aa (come) pyaaria (O Beloved) ."
            },
            {
                "original": "इक घड़ी को करन गुज़ारिआ ।",
                "hindi_gloss": "इक (एक छोटी-सी) घड़ी (घड़ी) को (के लिए ही सही) करन (जीवन) गुज़ारिआ (बिताने के लिए) ।",
                "english_gloss": "ik (one single) ghadee (moment) ko (for) karan (to make) guzaaria (abiding/spending) ."
            },
            {
                "original": "तन मन धन जिया तैं पर वारिआ ।",
                "hindi_gloss": "तन (अपना तन) मन (मन) धन (धन) जिया (और जीवन) तैं (तुम) पर (पर) वारिआ (न्योछावर कर दिया है) ।",
                "english_gloss": "tan (body) man (mind) dhan (wealth) jiya (life/soul) tain (upon you) par (upon) vaaria (I have surrendered) ."
            },
            {
                "original": "इह दुख जा कहूं किस आगे,",
                "hindi_gloss": "इह (यह विरह का) दुख (दुःख) जा (जाकर) कहूं (मैं कहूँ) किस (किसके) आगे (सामने),",
                "english_gloss": "eh (this) dukkh (pain) jaa (going) kahoon (shall I tell) kis (whom) aage (before),"
            },
            {
                "original": "रोम रोम घा प्रेम के लागे ।",
                "hindi_gloss": "रोम (रोम) रोम (रोम में) घा (घाव) प्रेम (प्रेम) के (के) लागे (लग गए हैं) ।",
                "english_gloss": "rom (pore) rom (every pore) ghaa (wounds) prem (of love) ke (of) laage (are struck) ."
            }
        ],
        "hindi_meaning": k29_hi,
        "english_meaning": k29_en
    }]
})

# ==========================================
# KAFI 30: 30. फ़सुमा वजउल-अल्लाह दस्सना एं अज्ज ओ यार
# ==========================================
k30_orig = """घुंघट खोल्ह मुक्ख वेख ना मेरा,
ऐब निमाणी दे कज्ज ओ यार ।
फ़सुमा वजउल-अल्लाह दस्सना एं अज्ज ओ यार ।

मैं अणजाणी तेरा नेहुं की जाणां,
लावण दा नहीं चज्ज ओ यार ।
फ़सुमा वजउल-अल्लाह दस्सना एं अज्ज ओ यार ।

हाजी लोक मक्के नूं जांदे,
साडा हैं तूं हज्ज ओ यार ।
फ़सुमा वजउल-अल्लाह दस्सना एं अज्ज ओ यार ।

डूंघी नदी ते तुलाह पुराणा,
मिलसां किहड़े पज्ज ओ यार ।
फ़सुमा वजउल-अल्लाह दस्सना एं अज्ज ओ यार ।

बुल्ल्हा शौह मैं ज़ाहर डिट्ठा,
लाह मूंह तों लज्ज ओ यार ।
फ़सुमा वजउल-अल्लाह दस्सना एं अज्ज ओ यार ।"""

k30_hi = """मेरा घूँघट उठाकर मेरे चेहरे के ऐब मत देखो,  
मुझ दीन-हीन के सारे अवगुणों को अपनी रहमत से ढाँक लो, ऐ यार!  
आज तुम हर दिशा में 'फ़सुम्मा वजउल-अल्लाह' (जहाँ भी मुँह फेरो, वहीं अल्लाह का मुख है) का नूर दिखा रहे हो!  

मैं नादान और अज्ञानी भला तुम्हारे पावन प्रेम को क्या जानूँ?  
मुझको तो इस इश्क़ को सलीक़े से निभाना भी नहीं आता, ऐ यार!  
आज तुम हर दिशा में 'फ़सुम्मा वजउल-अल्लाह' का नूर दिखा रहे हो!  

हज करने वाले तीर्थयात्री तो काबा-मक्का की ओर जाते हैं,  
परंतु हमारे लिए तो बस तुम्हारा ही दीदार सच्चा हज है, ऐ यार!  
आज तुम हर दिशा में 'फ़सुम्मा वजउल-अल्लाह' का नूर दिखा रहे हो!  

यह भवसागर की नदी बहुत गहरी है और मेरा तृण-काष्ठ का बेड़ा पुराना,  
भला किस उपाय और किस बहाने मैं तुमसे मिल पाऊँगी, ऐ यार?  
आज तुम हर दिशा में 'फ़सुम्मा वजउल-अल्लाह' का नूर दिखा रहे हो!  

बुल्ले शाह ने आज अपने स्वामी को प्रत्यक्ष प्रकट देख लिया है,  
संसार की सारी लोक-लाज का घूँघट चेहरे से उतार फेंका है, ऐ यार!  
आज तुम हर दिशा में 'फ़सुम्मा वजउल-अल्लाह' का नूर दिखा रहे हो!"""

k30_en = """Lift not my veil to scrutinize the flaws upon my face,  
Cover this humble creature's faults beneath thy boundless grace, O Friend!  
Today thou dost reveal everywhere: Wherever ye turn, there is the Face of God!  

A simple, naive girl am I—what can I know of Love divine?  
I have not even learned the art to walk this path of thine, O Friend!  
Today thou dost reveal everywhere: Wherever ye turn, there is the Face of God!  

Pious pilgrims travel far to reach Mecca’s sacred stone,  
Yet our sole, consummate Hajj is beholding thee alone, O Friend!  
Today thou dost reveal everywhere: Wherever ye turn, there is the Face of God!  

The river of existence runs deep, my reed raft is frail and old,  
By what craft or pretext shall I reach thy shore of gold, O Friend?  
Today thou dost reveal everywhere: Wherever ye turn, there is the Face of God!  

Bulleh has beheld his Sovereign Lord in open splendor clear,  
Casting aside the trembling veil of earthly shame and fear, O Friend!  
Today thou dost reveal everywhere: Wherever ye turn, there is the Face of God!"""

batch.append({
    "id": 30,
    "title": "30. फ़सुमा वजउल-अल्लाह दस्सना एं अज्ज ओ यार",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k30_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "घुंघट खोल्ह मुक्ख वेख ना मेरा,",
                "hindi_gloss": "घुंघट (मेरा घूँघट) खोल्ह (खोलकर) मुक्ख (मेरा मुख) वेख (देख) ना (मत),",
                "english_gloss": "ghoonaghat (veil) kholh (lifting) mukkh (face) vekh (look) na (not) mera (my),"
            },
            {
                "original": "ऐब निमाणी दे कज्ज ओ यार ।",
                "hindi_gloss": "ऐब (सारे दोष और पाप) निमाणी (मुझ दीन-हीन दासी) दे (के) कज्ज (ढाँक लो) ओ (हे) यार (मेरे प्यारे यार) ।",
                "english_gloss": "aib (flaws/sins) nimaanee (of this humble one) de (of) kajj (cover/conceal) o (O) yaar (Beloved Friend) ."
            },
            {
                "original": "फ़सुमा वजउल-अल्लाह दस्सना एं अज्ज ओ यार ।",
                "hindi_gloss": "फ़सुमा (जहाँ भी मुँह फेरो वहीं) वजउल-अल्लाह (अल्लाह का चेहरा है) दस्सना (दिखा/प्रकट कर रहा) एं (है) अज्ज (आज) ओ (हे) यार (मेरे प्यारे यार) ।",
                "english_gloss": "fasumma (wherever you turn) wajhullaha (is the Face of Allah) dassna (revealing) ain (thou art) ajj (today) o (O) yaar (Beloved Friend) ."
            },
            {
                "original": "मैं अणजाणी तेरा नेहुं की जाणां,",
                "hindi_gloss": "मैं (मैं तो) अणजाणी (अज्ञानी/नादान हूँ) तेरा (तुम्हारा पावन) नेहुं (प्रेम) की (क्या) जाणां (जानूँ),",
                "english_gloss": "main (I) anjaanee (ignorant/naive) tera (thy) nehun (divine love) kee (what) jaanaan (do I know),"
            },
            {
                "original": "लावण दा नहीं चज्ज ओ यार ।",
                "hindi_gloss": "लावण (प्रेम निभाने) दा (का) नहीं (मुझे नहीं आता) चज्ज (सलीक़ा/ढंग) ओ (हे) यार (मेरे यार) ।",
                "english_gloss": "laavan (to cultivate/keep) da (of) naaheen (not) chajj (manner/skill) o (O) yaar (Beloved Friend) ."
            },
            {
                "original": "फ़सुमा वजउल-अल्लाह दस्सना एं अज्ज ओ यार ।",
                "hindi_gloss": "फ़सुमा (सर्वत्र) वजउल-अल्लाह (ईश्वर का नूरानी चेहरा) दस्सना (दिखा रहा) एं (है) अज्ज (आज) ओ (हे) यार (मेरे यार) ।",
                "english_gloss": "fasumma (everywhere) wajhullaha (the Face of God) dassna (revealing) ain (art thou) ajj (today) o (O) yaar (Beloved Friend) ."
            },
            {
                "original": "हाजी लोक मक्के नूं जांदे,",
                "hindi_gloss": "हाजी (हज करने वाले) लोक (संसारी लोग) मक्के (काबा मक्का शरीफ़) नूं (को) जांदे (जाते हैं),",
                "english_gloss": "haajee (pilgrims) lok (people) makke (to Mecca) noon (unto) jaande (go),"
            },
            {
                "original": "साडा हैं तूं हज्ज ओ यार ।",
                "hindi_gloss": "साडा (हमारा परम) हैं (है) तूं (तू ही) हज्ज (हज/तीर्थ) ओ (हे) यार (मेरे यार) ।",
                "english_gloss": "saada (our supreme) hain (are) toon (thou alone) hajj (pilgrimage) o (O) yaar (Beloved Friend) ."
            },
            {
                "original": "फ़सुमा वजउल-अल्लाह दस्सना एं अज्ज ओ यार ।",
                "hindi_gloss": "फ़सुमा (जहाँ भी दृष्टि जाए) वजउल-अल्लाह (खुदा का वजूद/चेहरा) दस्सना (प्रकट कर रहा) एं (है) अज्ज (आज) ओ (हे) यार (मेरे यार) ।",
                "english_gloss": "fasumma (wherever turned) wajhullaha (is Allah's Countenance) dassna (unveiling) ain (thou art) ajj (today) o (O) yaar (Beloved Friend) ."
            },
            {
                "original": "डूंघी नदी ते तुलाह पुराणा,",
                "hindi_gloss": "डूंघी (गहरी भवसागर की) नदी (नदी है) ते (और) तुलाह (घास-फूस का बेड़ा/साधन) पुराणा (अत्यंत जर्जर और पुराना है),",
                "english_gloss": "doonghee (deep) nadee (river) te (and) tulaah (reed raft) puraana (worn and frail),"
            },
            {
                "original": "मिलसां किहड़े पज्ज ओ यार ।",
                "hindi_gloss": "मिलसां (मैं तुमसे मिलूँगी) किहड़े (किस) पज्ज (बहाने/उपाय से) ओ (हे) यार (मेरे यार) ।",
                "english_gloss": "milsaan (shall I meet thee) kihde (by what) pajj (pretext/means) o (O) yaar (Beloved Friend) ."
            },
            {
                "original": "फ़सुमा वजउल-अल्लाह दस्सना एं अज्ज ओ यार ।",
                "hindi_gloss": "फ़सुमा (सर्वत्र ही) वजउल-अल्लाह (अल्लाह का नूर) दस्सना (झलक रहा) एं (है) अज्ज (आज) ओ (हे) यार (मेरे यार) ।",
                "english_gloss": "fasumma (everywhere) wajhullaha (Face of God) dassna (revealing) ain (thou art) ajj (today) o (O) yaar (Beloved Friend) ."
            },
            {
                "original": "बुल्ल्हा शौह मैं ज़ाहर डिट्ठा,",
                "hindi_gloss": "बुल्ल्हा (बुल्ले शाह कहते हैं कि मैंने) शौह (अपने प्राण-स्वामी को) ज़ाहर (प्रत्यक्ष रूप से सर्वत्र) डिट्ठा (देख लिया है),",
                "english_gloss": "bullha (Bulleh says) shauh (the Lord) main (I) zaahar (manifest visibly) dittha (have beheld),"
            },
            {
                "original": "लाह मूंह तों लज्ज ओ यार ।",
                "hindi_gloss": "लाह (उतारकर) मूंह (मुख) तों (से) लज्ज (लोक-लाज का पर्दा) ओ (हे) यार (मेरे यार) ।",
                "english_gloss": "laah (casting off) moonh (face) ton (from) lajj (modesty/worldly shame) o (O) yaar (Beloved Friend) ."
            },
            {
                "original": "फ़सुमा वजउल-अल्लाह दस्सना एं अज्ज ओ यार ।",
                "hindi_gloss": "फ़सुमा (जिधर भी देखूँ) वजउल-अल्लाह (अल्लाह का नूरानी दीदार) दस्सना (दिखा रहा) एं (है) अज्ज (आज) ओ (हे) यार (मेरे यार) ।",
                "english_gloss": "fasumma (wherever turned) wajhullaha (is Allah's Divine Face) dassna (showing) ain (thou art) ajj (today) o (O) yaar (Beloved Friend) ."
            }
        ],
        "hindi_meaning": k30_hi,
        "english_meaning": k30_en
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
