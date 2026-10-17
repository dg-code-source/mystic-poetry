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
# KAFI 21: 21. बुल्ला की जाणा मैं कौण
# ==========================================
k21_orig = """ना मैं मोमन विच मसीतां, ना मैं विच कुफ़र दीआं रीतां,
ना मैं पाकां विच पलीतां, ना मैं मूसा ना फरऔन ।
बुल्ल्हा की जाणा मैं कौण ।

ना मैं अन्दर बेद किताबां, ना विच भंगां ना शराबां,
ना विच रिन्दां मसत खराबां, ना विच जागन ना विच सौण ।
बुल्ल्हा की जाणा मैं कौण ।

ना विच शादी ना ग़मनाकी, ना मैं विच पलीती पाकी,
ना मैं आबी ना मैं ख़ाकी, ना मैं आतिश ना मैं पौण ।
बुल्ल्हा की जाणा मैं कौण ।

ना मैं अरबी ना लाहौरी, ना मैं हिन्दी शहर नगौरी,
ना हिन्दू ना तुर्क पशौरी, ना मैं रहन्दा विच नदौण ।
बुल्ल्हा की जाणा मैं कौण ।

ना मैं भेत मज़हब दा पाइआ, ना मैं आदम हवा जाइआ,
ना मैं आपना नाम धराइआ, ना विच बैठण ना विच भौण ।
बुल्ल्हा की जाणा मैं कौण ।

अव्वल आखर आप नूं जाणां, ना कोई दूजा होर पछाणां,
मैथों होर ना कोई स्याणा, बुल्हा शाह खढ़ा है कौण ।
बुल्ल्हा की जाणा मैं कौण ।"""

k21_hi = """न मैं मस्जिदों में बैठा मोमिन हूँ, न ही कुफ़्र की रीतियों में लीन,  
न मैं पवित्रों में हूँ न अपवित्रों में, न मैं मूसा हूँ न अहंकारी फ़िरऔन!  
हे बुल्ले! मैं क्या जानूँ कि मैं कौन हूँ!  

न मैं वेदों और धर्मग्रंथों के पाखंड में हूँ, न भांग और शराब के नशे में,  
न मैं मदमस्त रिंदों की टोली में हूँ, न जागने में हूँ न सोने में!  
हे बुल्ले! मैं क्या जानूँ कि मैं कौन हूँ!  

न मैं हर्ष और उत्सव में हूँ न गहरे शोक में, न मैल में हूँ न शुद्धि में,  
न मैं जल का हूँ न मिट्टी का, न मैं अग्नि हूँ न पवन की गति में!  
हे बुल्ले! मैं क्या जानूँ कि मैं कौन हूँ!  

न मैं अरबी हूँ न लाहौरी, न मैं हिन्दुस्तानी नागौर शहर का,  
न मैं हिन्दू हूँ न पेशावरी तुर्क, न नदौन में बसने वाला बाशिंदा!  
हे बुल्ले! मैं क्या जानूँ कि मैं कौन हूँ!  

न मैंने मज़हबों के छिपे भेद जाने, न मैं आदम और हव्वा की सन्तान हूँ,  
न मैंने अपना कोई नाम रखा, न मैं ठहरने में हूँ न भटकने में!  
हे बुल्ले! मैं क्या जानूँ कि मैं कौन हूँ!  

आदि से अंत तक मैं केवल एक उस परम सत्य को जानता हूँ, उसके सिवा किसी दूजे को नहीं पहचानता,  
मुझसे अधिक सचेत और कौन होगा, बुल्ले शाह के इस चोले में आख़िर खड़ा कौन है!  
हे बुल्ले! मैं क्या जानूँ कि मैं कौन हूँ!"""

k21_en = """Not a believer in the mosque am I, nor steeped in rites of heresy,  
Neither among the righteous nor defiled, neither Moses nor Pharaoh's plea!  
O Bulleh, what know I who I am!  

Not in the Vedas nor sacred lore, nor intoxicated in hemp or wine,  
Not among the roistering tavern wits, nor in sleep or waking mine!  
O Bulleh, what know I who I am!  

Neither in gladness nor in grief, neither in filth nor purity,  
Neither of water nor of earth, nor fire or wind's obscurity!  
O Bulleh, what know I who I am!  

Not an Arab nor of Lahore, nor Indian from Nagaur's ground,  
Neither a Hindu nor Peshawar's Turk, nor in Nadaun am I bound!  
O Bulleh, what know I who I am!  

No secret rites of creeds I found, nor was I born of Adam's race,  
I gave myself no worldly name, neither sitting still nor in wandering pace!  
O Bulleh, what know I who I am!  

From first to last I know but the One, recognizing none beside,  
None is wiser in this truth than I—who is this standing in Bulleh's hide?  
O Bulleh, what know I who I am!"""

batch.append({
    "id": 21,
    "title": "21. बुल्ला की जाणा मैं कौण",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k21_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "ना मैं मोमन विच मसीतां, ना मैं विच कुफ़र दीआं रीतां,",
                "hindi_gloss": "ना (न) मैं (मैं) मोमन (सच्चा मोमिन/मुसलमान) विच (में) मसीतां (मस्जिदों में), ना (न) मैं (मैं) विच (में) कुफ़र (कुफ़्र/अधर्म) दीआं (की) रीतां (रीतियों में),",
                "english_gloss": "na (neither) main (I) moman (orthodox believer) vich (in) maseetaan (mosques), na (nor) main (I) vich (in) kufar (infidelity/heresy) deeyaan (of) reetaan (customs/rites),"
            },
            {
                "original": "ना मैं पाकां विच पलीतां, ना मैं मूसा ना फरऔन ।",
                "hindi_gloss": "ना (न) मैं (मैं) पाकां (पवित्रों) विच (में) पलीतां (न अपवित्रों में), ना (न) मैं (मैं) मूसा (हज़रत मूसा) ना (न ही) फरऔन (फ़िरऔन/अहंकारी राजा) ।",
                "english_gloss": "na (neither) main (I) paakaan (among the pure) vich (nor) paleetaan (among the impure), na (neither) main (I) moosa (Moses) na (nor) far-aun (Pharaoh) ."
            },
            {
                "original": "बुल्ल्हा की जाणा मैं कौण ।",
                "hindi_gloss": "बुल्ल्हा (हे बुल्ले) की (क्या) जाणा (जानूँ) मैं (मैं) कौण (कौन हूँ) ।",
                "english_gloss": "bullha (O Bulleh) kee (what) jaana (do I know) main (who I) kaun (am) ."
            },
            {
                "original": "ना मैं अन्दर बेद किताबां, ना विच भंगां ना शराबां,",
                "hindi_gloss": "ना (न) मैं (मैं) अन्दर (भीतर) बेद (वेदों) किताबां (और धर्मग्रंथों में), ना (न) विच (में) भंगां (भांग) ना (न) शराबां (मदिरा में),",
                "english_gloss": "na (neither) main (I) andar (within) bed (Vedas) kitaabaan (holy scriptures), na (nor) vich (in) bhangaan (intoxicating hemp) na (nor) sharaabaan (wines),"
            },
            {
                "original": "ना विच रिन्दां मसत खराबां, ना विच जागन ना विच सौण ।",
                "hindi_gloss": "ना (न) विच (में) रिन्दां (मस्त फ़क़ीरों) मसत (मतवालों) खराबां (शराबख़ाने के मस्तों में), ना (न) विच (में) जागन (जागने में) ना (न) विच (में) सौण (सोने में) ।",
                "english_gloss": "na (neither) vich (among) rindaan (free-spirited mystics) masat (intoxicated) kharaabaan (tavern-dwellers), na (nor) vich (in) jaagan (waking) na (nor) vich (in) saun (sleeping) ."
            },
            {
                "original": "बुल्ल्हा की जाणा मैं कौण ।",
                "hindi_gloss": "बुल्ल्हा (हे बुल्ले) की (क्या) जाणा (जानूँ) मैं (मैं) कौण (कौन हूँ) ।",
                "english_gloss": "bullha (O Bulleh) kee (what) jaana (do I know) main (who I) kaun (am) ."
            },
            {
                "original": "ना विच शादी ना ग़मनाकी, ना मैं विच पलीती पाकी,",
                "hindi_gloss": "ना (न) विच (में) शादी (हर्षोल्लास) ना (न) ग़मनाकी (शोक और दुःख में), ना (न) मैं (मैं) विच (में) पलीती (अपवित्रता) पाकी (अथवा पवित्रता में),",
                "english_gloss": "na (neither) vich (in) shaadi (joy/celebration) na (nor) gamnaaki (sorrow/grief), na (nor) main (I) vich (in) paleeti (defilement) paaki (or purity),"
            },
            {
                "original": "ना मैं आबी ना मैं ख़ाकी, ना मैं आतिश ना मैं पौण ।",
                "hindi_gloss": "ना (न) मैं (मैं) आबी (जल-तत्व का) ना (न) मैं (मैं) ख़ाकी (मिट्टी-तत्व का), ना (न) मैं (मैं) आतिश (अग्नि-तत्व) ना (न) मैं (मैं) पौण (वायु-तत्व) ।",
                "english_gloss": "na (neither) main (I) aabi (of water) na (nor) main (I) khaaki (of dust/earth), na (neither) main (I) aatish (of fire) na (nor) main (I) paun (of wind/air) ."
            },
            {
                "original": "बुल्ल्हा की जाणा मैं कौण ।",
                "hindi_gloss": "बुल्ल्हा (हे बुल्ले) की (क्या) जाणा (जानूँ) मैं (मैं) कौण (कौन हूँ) ।",
                "english_gloss": "bullha (O Bulleh) kee (what) jaana (do I know) main (who I) kaun (am) ."
            },
            {
                "original": "ना मैं अरबी ना लाहौरी, ना मैं हिन्दी शहर नगौरी,",
                "hindi_gloss": "ना (न) मैं (मैं) अरबी (अरब का वासी) ना (न) लाहौरी (लाहौर का), ना (न) मैं (मैं) हिन्दी (हिंदुस्तानी) शहर (शहर) नगौरी (नागौर का),",
                "english_gloss": "na (neither) main (I) arabi (an Arab) na (nor) laahori (of Lahore), na (nor) main (I) hindi (an Indian) shahar (city) nagauri (of Nagaur),"
            },
            {
                "original": "ना हिन्दू ना तुर्क पशौरी, ना मैं रहन्दा विच नदौण ।",
                "hindi_gloss": "ना (न) हिन्दू (हिन्दू) ना (न) तुर्क (तुर्क/मुसलमान) पशौरी (पेशावर का), ना (न) मैं (मैं) रहन्दा (रहता हूँ) विच (में) नदौण (नदौन नगर में) ।",
                "english_gloss": "na (neither) hindu (Hindu) na (nor) turk (Turk/Muslim) pashauri (of Peshawar), na (nor) main (I) rahanda (dwell) vich (in) nadaun (Nadaun city) ."
            },
            {
                "original": "बुल्ल्हा की जाणा मैं कौण ।",
                "hindi_gloss": "बुल्ल्हा (हे बुल्ले) की (क्या) जाणा (जानूँ) मैं (मैं) कौण (कौन हूँ) ।",
                "english_gloss": "bullha (O Bulleh) kee (what) jaana (do I know) main (who I) kaun (am) ."
            },
            {
                "original": "ना मैं भेत मज़हब दा पाइआ, ना मैं आदम हवा जाइआ,",
                "hindi_gloss": "ना (न) मैं (मैंने) भेत (भेद/रहस्य) मज़हब (मज़हब) दा (का) पाइआ (पाया), ना (न) मैं (मैं) आदम (आदम) हवा (हव्वा से) जाइआ (जन्मा),",
                "english_gloss": "na (neither) main (I) bhet (secret) mazhab (of religion) da (of) paaia (found), na (nor) main (I) aadam (Adam) hawa (Eve's) jaaia (begotten child),"
            },
            {
                "original": "ना मैं आपना नाम धराइआ, ना विच बैठण ना विच भौण ।",
                "hindi_gloss": "ना (न) मैं (मैंने) आपना (अपना कोई) नाम (नाम) धराइआ (रखा), ना (न) विच (में) बैठण (स्थिर बैठने में) ना (न) विच (में) भौण (भटकने/घूमने में) ।",
                "english_gloss": "na (neither) main (I) aapna (my own) naam (name) dharaaia (devised), na (nor) vich (in) baithan (sitting still) na (nor) vich (in) bhaun (wandering/roaming) ."
            },
            {
                "original": "बुल्ल्हा की जाणा मैं कौण ।",
                "hindi_gloss": "बुल्ल्हा (हे बुल्ले) की (क्या) जाणा (जानूँ) मैं (मैं) कौण (कौन हूँ) ।",
                "english_gloss": "bullha (O Bulleh) kee (what) jaana (do I know) main (who I) kaun (am) ."
            },
            {
                "original": "अव्वल आखर आप नूं जाणां, ना कोई दूजा होर पछाणां,",
                "hindi_gloss": "अव्वल (आदि में) आखर (अंत में) आप (स्वयं परमात्मा) नूं (को ही) जाणां (जानता हूँ), ना (न) कोई (किसी) दूजा (दूसरे को) होर (अन्य) पछाणां (पहचानता हूँ),",
                "english_gloss": "avval (first/beginning) aakhar (last/end) aap (the Self divine) noon (unto) jaanaan (I know), na (nor) koi (any) dooja (second) hor (other) pachhaanaan (I recognize),"
            },
            {
                "original": "मैथों होर ना कोई स्याणा, बुल्हा शाह खढ़ा है कौण ।",
                "hindi_gloss": "मैथों (मुझसे) होर (अधिक) ना (कोई नहीं) कोई (कोई) स्याणा (बुद्धिमान/सचेत), बुल्हा (बुल्ले) शाह (शाह के भीतर) खढ़ा (खड़ा) है (है) कौण (कौन) ।",
                "english_gloss": "maithon (than me) hor (other) na (not) koi (any) syaana (wiser/aware), bullha (Bulleh) shaah (Shah) khadha (standing) hai (is) kaun (who) ."
            },
            {
                "original": "बुल्ल्हा की जाणा मैं कौण ।",
                "hindi_gloss": "बुल्ल्हा (हे बुल्ले) की (क्या) जाणा (जानूँ) मैं (मैं) कौण (कौन हूँ) ।",
                "english_gloss": "bullha (O Bulleh) kee (what) jaana (do I know) main (who I) kaun (am) ."
            }
        ],
        "hindi_meaning": k21_hi,
        "english_meaning": k21_en
    }]
})

# ==========================================
# KAFI 22: 22. बुल्ला की जाने ज़ात इश्क दी कौण
# ==========================================
k22_orig = """बुल्ल्हा की जाने ज़ात इश्क दी कौण ।
ना सूहां ना कंम बखेड़े वंञे जागन सौण ।

रांझे नूं मैं गालियां देवां, मन विच करां दुआईं ।
मैं ते रांझा इको कोई, लोकां नूं अज़माईं ।
जिस बेले विच बेली दिस्से, उस दीआं लवां बलाईं ।
बुल्ल्हा शौह नूं पासे छड्ड के, जंगल वल्ल ना जाईं ।

बुल्ल्हा की जाणा ज़ात इश्क दी कौण ।
ना सूहां ना कंम बखेड़े वंञे जागन सौण ।"""

k22_hi = """बुल्ला क्या जाने कि इस दिव्य प्रेम की जाति और कुल क्या है!  
न यहाँ कोई सांसारिक भेद-भाव है, न कर्मों के बखेड़े, जागना और सोना सब मिट चुका है!  

मुख से तो मैं अपने रांझे को उलाहने और गालियाँ देती हूँ,  
परंतु मन के भीतर केवल उसी के लिए दुआएँ और प्रार्थनाएँ करती हूँ!  
वास्तव में मैं और रांझा मिलकर एक ही हो चुके हैं,  
यह द्वैत तो केवल दुनिया के लोगों को परखने का एक बहाना है!  
जिस वन-उपवन में मेरा वह सच्चा सखा दिखाई दे जाए,  
मैं उस पावन भूमि पर सौ-सौ बार बलिहारी जाती हूँ!  
हे बुल्ले! अपने हृदय में विराजमान प्रभु को छोड़कर,  
व्यर्थ में बाहर के बीहड़ जंगलों में मत भटको!  

बुल्ला क्या जाने कि इस दिव्य प्रेम की जाति और कुल क्या है!  
न यहाँ कोई सांसारिक भेद-भाव है, न कर्मों के बखेड़े, जागना और सोना सब मिट चुका है!"""

k22_en = """What does Bulleh comprehend of Love's lineage and creed?  
No worldly clues, no petty chores remain; all sleep and waking have ceased indeed!  

With my lips I cast reproaches at my Ranjha in feigned disdain,  
Yet deep within my secret soul, blessings and prayers for Him remain!  
For Ranjha and I have merged as one indivisible entity,  
This outward separation is but a mask to test the world's credulity!  
Upon whatever riverbank or grove my Beloved Companion appears,  
I shower my life and blessings there, shedding ecstatic tears!  
O Bulleh, forsaking not the Lord who dwells so near and kind,  
Wander not in barren deserts, leaving His grace behind!  

What does Bulleh comprehend of Love's lineage and creed?  
No worldly clues, no petty chores remain; all sleep and waking have ceased indeed!"""

batch.append({
    "id": 22,
    "title": "22. बुल्ला की जाने ज़ात इश्क दी कौण",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k22_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "बुल्ल्हा की जाने ज़ात इश्क दी कौण ।",
                "hindi_gloss": "बुल्ल्हा (बुल्ला) की (क्या) जाने (जाने) ज़ात (जाति/स्वभाव) इश्क (दिव्य प्रेम) दी (की) कौण (कौन सी है) ।",
                "english_gloss": "bullha (Bulleh) kee (what) jaane (knows) zaat (essence/caste) ishq (of love) dee (of) kaun (what is) ."
            },
            {
                "original": "ना सूहां ना कंम बखेड़े वंञे जागन सौण ।",
                "hindi_gloss": "ना (न कोई) सूहां (गंभीर भेद) ना (न) कंम (सांसारिक काम) बखेड़े (और उलझनें), वंञे (चला गया/मिट गया) जागन (जागना) सौण (और सोना) ।",
                "english_gloss": "na (no) soohaan (clues/deliberations) na (nor) kamm (worldly chores) bakhede (and disputes), vanje (departed) jaagan (waking) saun (and sleeping) ."
            },
            {
                "original": "रांझे नूं मैं गालियां देवां, मन विच करां दुआईं ।",
                "hindi_gloss": "रांझे (प्रियतम रांझे) नूं (को) मैं (मैं मुख से) गालियां (उलाहने/गालियाँ) देवां (देती हूँ), मन (पर अंतर्मन) विच (में) करां (करती हूँ) दुआईं (प्रार्थनाएँ/दुआएँ) ।",
                "english_gloss": "raanjhe (to Ranjha) noon (unto) main (I) gaaliyaan (reproaches/curses) devaan (give), man (heart) vich (in) karaan (make) duaaeen (prayers) ."
            },
            {
                "original": "मैं ते रांझा इको कोई, लोकां नूं अज़माईं ।",
                "hindi_gloss": "मैं (मैं) ते (और) रांझा (रांझा) इको (एक) कोई (ही हैं), लोकां (लोगों) नूं (को केवल) अज़माईं (परखने/दिखाने के लिए) ।",
                "english_gloss": "main (I) te (and) raanjha (Ranjha) iko (one single) koi (are), lokaan (people) noon (unto) azmaaeen (to test/veil) ."
            },
            {
                "original": "जिस बेले विच बेली दिस्से, उस दीआं लवां बलाईं ।",
                "hindi_gloss": "जिस (जिस) बेले (नदी-कछार) विच (में) बेली (सच्चा मित्र/सखा) दिस्से (दिखाई दे), उस (उसकी) दीआं (की) लवां (लेती हूँ) बलाईं (बलाएं/न्योछावर होती हूँ) ।",
                "english_gloss": "jis (which) bele (river-pasture) vich (in) beli (companion/Beloved) disse (is seen), us (his) deeyaan (of) lavaan (take) balaaeen (blessings/sacrifice) ."
            },
            {
                "original": "बुल्ल्हा शौह नूं पासे छड्ड के, जंगल वल्ल ना जाईं ।",
                "hindi_gloss": "बुल्ल्हा (हे बुल्ले) शौह (अपने प्रभु) नूं (को) पासे (अपने निकट) छड्ड (छोड़) के (कर), जंगल (बाहर जंगलों की) वल्ल (ओर) ना (मत) जाईं (भटको) ।",
                "english_gloss": "bullha (O Bulleh) shauh (the Lord) noon (unto) paase (beside) chhadd (leaving) ke (having done), jangal (forests) vall (toward) na (not) jaaeen (wander) ."
            },
            {
                "original": "बुल्ल्हा की जाणा ज़ात इश्क दी कौण ।",
                "hindi_gloss": "बुल्ल्हा (बुल्ला) की (क्या) जाणा (जाने) ज़ात (जाति) इश्क (प्रेम) दी (की) कौण (कौन सी है) ।",
                "english_gloss": "bullha (Bulleh) kee (what) jaana (knows) zaat (caste/nature) ishq (of love) dee (of) kaun (what is) ."
            },
            {
                "original": "ना सूहां ना कंम बखेड़े वंञे जागन सौण ।",
                "hindi_gloss": "ना (न) सूहां (भेद) ना (न) कंम (काम) बखेड़े (बखेड़े) वंञे (मिट गए) जागन (जागना) सौण (सोना) ।",
                "english_gloss": "na (no) soohaan (clues) na (nor) kamm (chores) bakhede (entanglements) vanje (departed) jaagan (waking) saun (sleeping) ."
            }
        ],
        "hindi_meaning": k22_hi,
        "english_meaning": k22_en
    }]
})

# ==========================================
# KAFI 23: 23. बुल्ल्हे नूं समझावण आईआं, भैणां ते भरजाईआं
# ==========================================
k23_orig = """बुल्ल्हे नूं समझावण आईआं, भैणां ते भरजाईआं ।
मन्न लै बुल्लिआ साडा कहणा, छड्ड दे पल्ला राईआं ।
आल नबी औलाद नबी नूं, तूं की लीकां लाईआं ।
जेहड़ा सानूं सईअद सद्दे, दोज़ख मिलण सजाईआं ।
जो कोई सानूं राईं आखे, बहशतीं पींघां पाईआं ।
राईं साईं सभनी थाईं, रब्ब दीआं बेपरवाहियां ।
सोहणीयां परे हटाईआं ने ते, कोझीयां लै गल लाईआं ।
जे तूं लोड़ें बाग़ बहारां, चाकर हो जा राईआं ।
बुल्ल्हा शौह दी ज़ात की पुच्छना एं, शक्कर हो रजाईआं ।"""

k23_hi = """बुल्ले को समझाने के लिए उसकी सगी बहनें और भाभियाँ दौड़कर आईं—  
"हे बुल्ले! हमारी बात मान ले और उस अराईं (माली) का पल्ला छोड़ दे!  
तू पैग़म्बर के पावन वंश का सैय्यद है, तूने कुल की मर्यादा पर कैसा कलंक लगा दिया!"  

बुल्ले ने उत्तर दिया—  
"जो कोई मुझे उच्च कुलीन सैय्यद कहकर पुकारेगा, उसे नरक की घोर यातनाएँ मिलेंगी!  
और जो कोई मुझे अराईं (शाह इनायत का दास) कहेगा, वह स्वर्ग के बाग़ों में आनंद के झूले झूलेगा!  
अराईं में भी वही ईश्वर बसता है और हर एक कण में वही समाया हुआ है,  
उस परवरदिगार की लीलाएँ कितनी अगोचर और बेपरवाह हैं!  
उसने अहंकार से भरी सुंदरियों को तो परे धकेल दिया,  
और दीन-हीन, कुरूप दिखने वाली दासियों को अपने गले से लगा लिया!  
यदि तू सचमुच आत्मिक ज्ञान के बाग़ों की अमर बहारें चाहता है,  
तो उस अराईं मुर्शिद का विनम्र चाकर बन जा!  
हे बुल्ले! प्रभु की जाति क्या पूछता है?  
उसकी पावन रज़ा में शक्कर की तरह घुलकर मीठा हो जा!"""

k23_en = """Sisters and sisters-in-law arrived in haste, counseling Bulleh with grief:  
"Heed our advice, O Bulleh, and forsake that lowly Arain gardener's fief!  
Born of the Prophet's noble blood, a holy Sayyid of high acclaim,  
Why hast thou cast upon our proud clan this indelible smudge of shame?"  

Bulleh replied:  
"Whoever dares call me a high-born Sayyid shall suffer the torments of hell!  
And whoever calls me an Arain's slave in the gardens of heaven shall dwell!  
In the humble Arain dwells the Master, pervading every space and land,  
Unfathomable and carefree are the mysteries of the Lord's supreme command!  
He cast aside the haughty beauties boasting of noble race and face,  
And gathered the simple, humble souls into His tender embrace!  
If thou truly desirest the eternal blossoms of spiritual spring,  
Become a lowly servant unto that Arain, and to his threshold cling!  
O Bulleh, what need is there to question the caste of the Lord divine?  
Dissolve like sweet sugar in His holy Will, and let His purpose shine!"""

batch.append({
    "id": 23,
    "title": "23. बुल्ल्हे नूं समझावण आईआं, भैणां ते भरजाईआं",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k23_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "बुल्ल्हे नूं समझावण आईआं, भैणां ते भरजाईआं ।",
                "hindi_gloss": "बुल्ल्हे (बुल्ले को) नूं (को) समझावण (समझाने) आईआं (आईं), भैणां (सगी बहनें) ते (और) भरजाईआं (भाभियाँ) ।",
                "english_gloss": "bullhe (unto Bulleh) noon (to) samjhaavan (to admonish/counsel) aaeeyaan (came), bhainaan (sisters) te (and) bharjaaeeyaan (sisters-in-law) ."
            },
            {
                "original": "मन्न लै बुल्लिआ साडा कहणा, छड्ड दे पल्ला राईआं ।",
                "hindi_gloss": "मन्न (मान) लै (लो) बुल्लिआ (हे बुल्ले) साडा (हमारा) कहणा (कहना), छड्ड (छोड़) दे (दो) पल्ला (पल्ला/शरण) राईआं (अराईं जाति के शाह इनायत का) ।",
                "english_gloss": "mann (accept) lai (take) bullia (O Bulleh) saada (our) kahna (plea/counsel), chhadd (leave) de (give up) palla (hem/association) raaeeyaan (of the Arain gardener) ."
            },
            {
                "original": "आल नबी औलाद नबी नूं, तूं की लीकां लाईआं ।",
                "hindi_gloss": "आल (वंश) नबी (पैग़म्बर के) औलाद (संतान) नबी (रसूल की) नूं (को), तूं (तूने) की (कैसा) लीकां (कलंक का टीका) लाईआं (लगा दिया है) ।",
                "english_gloss": "aal (family) nabi (of Prophet) aulaad (lineage) nabi (of Prophet) noon (unto), toon (you) kee (what) leekaan (blemish/disgrace) laaeeyaan (have cast) ."
            },
            {
                "original": "जेहड़ा सानूं सईअद सद्दे, दोज़ख मिलण सजाईआं ।",
                "hindi_gloss": "जेहड़ा (जो कोई) सानूं (हमें) सईअद (उच्च कुलीन सैय्यद) सद्दे (पुकारेगा), दोज़ख (नरक में) मिलण (मिलेंगी) सजाईआं (सज़ाएँ) ।",
                "english_gloss": "jehda (whoever) saanoon (us) sayyad (Sayyid/noble) sadde (calls), dozakh (in hell) milan (shall receive) sajaaeeyaan (punishments) ."
            },
            {
                "original": "जो कोई सानूं राईं आखे, बहशतीं पींघां पाईआं ।",
                "hindi_gloss": "जो (जो) कोई (कोई) सानूं (हमें) राईं (अराईं/बाग़बान का दास) आखे (कहेगा), बहशतीं (स्वर्ग के बाग़ों में) पींघां (झूले) पाईआं (झूलेगा) ।",
                "english_gloss": "jo (who) koi (ever) saanoon (us) raaeen (Arain gardener) aakhe (calls), bahashteen (in paradise) peenghaan (swings of joy) paaeeyaan (shall enjoy) ."
            },
            {
                "original": "राईं साईं सभनी थाईं, रब्ब दीआं बेपरवाहियां ।",
                "hindi_gloss": "राईं (अराईं में भी) साईं (वही ईश्वर है) सभनी (सभी) थाईं (स्थानों में वही व्यापक है), रब्ब (परमात्मा) दीआं (की) बेपरवाहियां (अगाध और बेपरवाह लीलाएँ हैं) ।",
                "english_gloss": "raaeen (in the Arain) saaen (the Lord dwells) sabhnee (in all) thaaeen (places), rabb (of God) deeyaan (of) beparwaahiyaan (sovereign ways) ."
            },
            {
                "original": "सोहणीयां परे हटाईआं ने ते, कोझीयां लै गल लाईआं ।",
                "hindi_gloss": "सोहणीयां (अहंकारी सुंदरियों को) परे (दूर) हटाईआं (हटा दिया) ने (है) ते (और), कोझीयां (विनम्र और कुरूप दिखने वाली दासियों को) लै (लेकर) गल (सीने से) लाईआं (लगा लिया है) ।",
                "english_gloss": "sohneeyaan (the proud beauties) pare (aside) hataaeeyaan (pushed) ne (has) te (and), kojheeyaan (the humble/homely souls) lai (taking) gal (to bosom) laaeeyaan (embraced) ."
            },
            {
                "original": "जे तूं लोड़ें बाग़ बहारां, चाकर हो जा राईआं ।",
                "hindi_gloss": "जे (यदि) तूं (तू) लोड़ें (चाहता है) बाग़ (दिव्य बाग़ों की) बहारां (आनंदमयी बहारें), चाकर (सेवक) हो (बन) जा (जा) राईआं (अराईं गुरु का) ।",
                "english_gloss": "je (if) toon (you) lodein (seek) baag (spiritual gardens) bahaaraan (spring blossoms), chaakar (humble servant) ho (become) ja (go) raaeeyaan (of the Arain) ."
            },
            {
                "original": "बुल्ल्हा शौह दी ज़ात की पुच्छना एं, शक्कर हो रजाईआं ।",
                "hindi_gloss": "बुल्ल्हा (हे बुल्ले) शौह (प्रभु) दी (की) ज़ात (जाति) की (क्या) पुच्छना (पूछता) एं (है), शक्कर (संतुष्ट और मधुर) हो (हो जा) रजाईआं (उसकी रज़ा और इच्छा में) ।",
                "english_gloss": "bullha (Bulleh) shauh (of the Lord) dee (of) zaat (caste) kee (what) puchhna (ask) aen (do you), shakkar (sweet as sugar) ho (become) rajaaeeyaan (in divine Will) ."
            }
        ],
        "hindi_meaning": k23_hi,
        "english_meaning": k23_en
    }]
})

# ==========================================
# KAFI 24: 24. चलो देखिए उस मसतानड़े नूं
# ==========================================
k24_orig = """चलो देखिए उस मसतानड़े नूं,
जिद्ही त्रिंञणां दे विच पई ए धुंम ।
उह ते मैं वहदत विच रंगदा ए,
नहीं पुच्छदा जात दे की हो तुम ।

जीद्हा शोर चुफेरे पैंदा ए,
उह कोल तेरे नित्त रहन्दा ए,
नाले 'नाहन अकरब' कहन्दा ए,
नाले आखे 'वफ़ी-अनफ़स-कुम' ।

छड्ड झूठ भरम दी बसती नूं,
कर इश्क दी कायम मसती नूं,
गए पहुंच सजन दी हसती नूं,
जिहड़े हो गए 'सुम-बुकम-उम' ।

ना तेरा ए ना मेरा ए,
जग्ग फ़ानी झगड़ा झेड़ा ए,
बिनां मुरशद रहबर किहड़ा ए,
पढ़-'फाज़-रूनी-अज़-कुर-कुम' ।

बुल्ल्हे शाह इह बात इशारे दी,
जिन्हा लग्ग गई तांघ नज़ारे दी,
दस्स पैंदी घर वणजारे दी,
है 'यदउल्ल्हा-फ़ौका अयदीकुम' ।

चलो देखिए उस मसतानड़े नूं,
जिद्ही त्रिंञणां दे विच पई ए धुंम ।"""

k24_hi = """आओ, चलें उस मस्त-अलमस्त फ़कीर के दर्शन करें,  
जिसके पावन सत्संग और चरखा-मंडली में भारी धूम मची है!  
वह 'तू' और 'मैं' के द्वैत को मिटाकर सबको अद्वैत के एक रंग में रंग देता है,  
और किसी से कभी नहीं पूछता कि तुम्हारी जाति क्या है!  

जिस परमात्मा की चर्चा की गूँज चारों ओर फैली हुई है,  
वह तो नित्य तुम्हारे ही बिल्कुल पास और अंग-संग रहता है!  
वह स्वयं शास्त्र में कहता है—'मैं तुम्हारी जीवन-नस से भी अधिक निकट हूँ,'  
और कहता है—'मैं तो तुम्हारे अपने ही अंतर्मन में हूँ, क्या तुम देखते नहीं?'  

इस झूठे और भरम भरे सांसारिक नगर का मोह त्याग दो,  
और प्रभु-प्रेम की अविचल मस्ती को अपने भीतर जाग्रत करो!  
वे साधक प्रियतम की परम सत्ता तक सहज ही पहुँच गए,  
जो इस नश्वर दुनिया की वासनाओं के लिए बहरे, गूँगे और अंधे बन गए!  

न यह संसार तेरा है और न मेरा है,  
यह सारा जगत नश्वर है और इसके सारे झगड़े-बखेड़े व्यर्थ हैं!  
सच्चे मुर्शिद के बिना भला तुम्हारा दूसरा रहनुमा और कौन हो सकता है?  
उस दिव्य वचन को पढ़ो—'तुम मुझे याद करो, मैं तुम्हें याद रखूँगा!'  

बुल्ले शाह कहते हैं—यह ज्ञान केवल सूक्ष्म इशारे और आत्म-अनुभूति का है,  
जिन्हें उस दिव्य स्वरूप के दर्शन की सच्ची लगन लग गई है,  
उन्हें उस परम व्यापारी के सच्चे धाम की पहचान मिल जाती है,  
जहाँ साक्षात सिद्ध होता है—'अल्लाह का हाथ तुम्हारे हाथों के ऊपर है!'  

आओ, चलें उस मस्त-अलमस्त फ़कीर के दर्शन करें,  
जिसके पावन सत्संग और चरखा-मंडली में भारी धूम मची है!"""

k24_en = """Come, let us go behold that divine Ecstatic One,  
Whose renown resounds across all the spinning circles!  
Dyeing all differences in the singular hue of divine Oneness,  
He never inquires of what caste or clan thou art!  

The One whose glory echoes throughout all creation,  
Abides forever intimate and close beside thee!  
Declaring in truth: "I am nearer than thine own jugular vein,"  
And whispering within: "I dwell in thine own soul, dost thou not see?"  

Forsake this worldly town of falsehood and empty delusions,  
Establish within thine heart the enduring ecstasy of divine Love!  
Those seekers reached the exalted presence of the Beloved,  
Who became deaf, dumb, and blind to the world's false noise!  

Neither is this transient earth thine, nor is it mine,  
All worldly strife and bitter feuds are fleeting dust!  
Without the illumined Master, who else can guide thy steps?  
Heed the holy scripture: "Remember Me, and I shall remember you!"  

Says Bulleh Shah—this is a secret revealed only through subtle grace,  
Those who burn with deep yearning for the Beloved's sacred sight,  
Discover the true abode of the divine Merchant,  
Where shines the truth: "The hand of God is upon their hands!"  

Come, let us go behold that divine Ecstatic One,  
Whose renown resounds across all the spinning circles!"""

batch.append({
    "id": 24,
    "title": "24. चलो देखिए उस मसतानड़े नूं",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k24_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "चलो देखिए उस मसतानड़े नूं,",
                "hindi_gloss": "चलो (आओ चलें) देखिए (दर्शन करें) उस (उस) मसतानड़े (मस्त-अलमस्त फ़क़ीर/मुर्शिद) नूं (के),",
                "english_gloss": "chalo (come let us go) dekhiye (behold) us (that) mastaan-de (ecstatic master/mystic) noon (unto),"
            },
            {
                "original": "जिद्ही त्रिंञणां दे विच पई ए धुंम ।",
                "hindi_gloss": "जिद्ही (जिसकी) त्रिंञणां (सखियों की कताई-मंडली/सत्संग) दे (के) विच (भीतर) पई (मची) ए (हुई है) धुंम (महान धूम) ।",
                "english_gloss": "jidhee (whose) trinjanaan (spinning assemblies/spiritual circles) de (of) vich (in) payee (arisen) e (has) dhumm (fame/celebration) ."
            },
            {
                "original": "उह ते मैं वहदत विच रंगदा ए,",
                "hindi_gloss": "उह (वह) ते (तू) मैं (और मैं सबको) वहदत (अद्वैत/एकेश्वरवाद के रंग) विच (में) रंगदा (रंग देता) ए (है),",
                "english_gloss": "uh (he) te (and) main (I) vahdat (divine Oneness/unity) vich (in) rangda (dyes/colors) e (does),"
            },
            {
                "original": "नहीं पुच्छदा जात दे की हो तुम ।",
                "hindi_gloss": "नहीं (कभी नहीं) पुच्छदा (पूछता) जात (जाति) दे (के) की (क्या) हो (हो) तुम (तुम) ।",
                "english_gloss": "naheen (not) puchhda (asks) jaat (caste) de (of) kee (what) ho (are) tum (you) ."
            },
            {
                "original": "जीद्हा शोर चुफेरे पैंदा ए,",
                "hindi_gloss": "जीद्हा (जिसकी चर्चा का) शोर (गूँज) चुफेरे (चारों दिशाओं में) पैंदा (पड़ता) ए (है),",
                "english_gloss": "jeedha (whose) shor (clamor/renown) chufere (all four corners) painda (falls) e (does),"
            },
            {
                "original": "उह कोल तेरे नित्त रहन्दा ए,",
                "hindi_gloss": "उह (वह परमात्मा) कोल (समीप) तेरे (तेरे) नित्त (सदा) रहन्दा (रहता) ए (है),",
                "english_gloss": "uh (he) kol (near) tere (unto you) nitt (always) rahanda (dwells) e (does),"
            },
            {
                "original": "नाले 'नाहन अकरब' कहन्दा ए,",
                "hindi_gloss": "नाले (और) 'नाहन अकरब' (कुरआन का वचन: 'हम तुम्हारी गर्दन की नस से भी अधिक निकट हैं') कहन्दा (कहता) ए (है),",
                "english_gloss": "naale (moreover) 'nahnu aqrab' ('We are nearer to him than his jugular vein') kahnda (declares) e (does),"
            },
            {
                "original": "नाले आखे 'वफ़ी-अनफ़स-कुम' ।",
                "hindi_gloss": "नाले (और) आखे (कहता है) 'वफ़ी-अनफ़स-कुम' ('और तुम्हारे भीतर ही हूँ, क्या तुम देखते नहीं?') ।",
                "english_gloss": "naale (also) aakhe (says) 'wa fee anfusikum' ('And in your own souls, will you not perceive?') ."
            },
            {
                "original": "छड्ड झूठ भरम दी बसती नूं,",
                "hindi_gloss": "छड्ड (त्याग दो) झूठ (झूठ) भरम (और भ्रम) दी (की) बसती (सांसारिक बस्ती) नूं (को),",
                "english_gloss": "chhadd (forsake) jhooth (falsehood) bharam (delusion) dee (of) bastee (abode) noon (unto),"
            },
            {
                "original": "कर इश्क दी कायम मसती नूं,",
                "hindi_gloss": "कर (स्थापित करो) इश्क (दिव्य प्रेम) दी (की) कायम (अविचल) मसती (मस्ती) नूं (को),",
                "english_gloss": "kar (establish) ishq (divine love) dee (of) kaayam (enduring) mastee (intoxication) noon (unto),"
            },
            {
                "original": "गए पहुंच सजन दी हसती नूं,",
                "hindi_gloss": "गए (पहुँच गए) पहुंच (परम पद तक) सजन (प्रियतम की) दी (की) हसती (दिव्य सत्ता) नूं (तक),",
                "english_gloss": "gaye (went) pahunch (reaching) sajan (the Beloved's) dee (of) hastee (divine Presence) noon (unto),"
            },
            {
                "original": "जिहड़े हो गए 'सुम-बुकम-उम' ।",
                "hindi_gloss": "जिहड़े (जो साधक) हो (हो) गए (गए) 'सुम-बुकम-उम' (संसार के प्रति बहरे, गूँगे और अंधे) ।",
                "english_gloss": "jehde (those who) ho (became) gaye (did) 'summun bukmun um-yun' (deaf, dumb, and blind to worldly illusion) ."
            },
            {
                "original": "ना तेरा ए ना मेरा ए,",
                "hindi_gloss": "ना (न) तेरा (तेरा) ए (है) ना (न) मेरा (मेरा) ए (है),",
                "english_gloss": "na (neither) tera (yours) e (is) na (nor) mera (mine) e (is),"
            },
            {
                "original": "जग्ग फ़ानी झगड़ा झेड़ा ए,",
                "hindi_gloss": "जग्ग (यह संसार) फ़ानी (नश्वर है) झगड़ा (सारे वाद-विवाद) झेड़ा (और झगड़े व्यर्थ हैं) ए (हैं),",
                "english_gloss": "jagg (world) faani (perishable/transient) jhagda (strife) jheda (dispute) e (is),"
            },
            {
                "original": "बिनां मुरशद रहबर किहड़ा ए,",
                "hindi_gloss": "बिनां (बिना) मुरशद (सद्गुरु के) रहबर (सच्चा मार्गदर्शक) किहड़ा (और कौन) ए (है),",
                "english_gloss": "binaan (without) murshad (spiritual guide) rahbar (pathfinder) kihda (who) e (is),"
            },
            {
                "original": "पढ़-'फाज़-रूनी-अज़-कुर-कुम' ।",
                "hindi_gloss": "पढ़ (पढ़ो और आचरण करो) 'फाज़-रूनी-अज़-कुर-कुम' ('तुम मुझे याद करो, मैं तुम्हें याद रखूँगा') ।",
                "english_gloss": "padh (recite/heed) 'fazkuroonee azkurkum' ('Remember Me; I will remember you') ."
            },
            {
                "original": "बुल्ल्हे शाह इह बात इशारे दी,",
                "hindi_gloss": "बुल्ल्हे (बुल्ले) शाह (शाह कहते हैं) इह (यह) बात (गूढ़ रहस्य) इशारे (संकेत/अनुभूति) दी (का है),",
                "english_gloss": "bullhe (Bulleh) shaah (Shah says) ih (this) baat (matter) ishaare (of subtle hint) dee (of is),"
            },
            {
                "original": "जिन्हा लग्ग गई तांघ नज़ारे दी,",
                "hindi_gloss": "जिन्हा (जिन साधकों को) लग्ग (लग) गई (गई) तांघ (तीव्र तड़प) नज़ारे (दीदार/दर्शन) दी (की),",
                "english_gloss": "jinha (those who) lagg (ignited) gayee (did) taangh (yearning) nazaare (of divine Vision) dee (of),"
            },
            {
                "original": "दस्स पैंदी घर वणजारे दी,",
                "hindi_gloss": "दस्स (पहचान) पैंदी (मिल जाती है) घर (उस परम आत्मिक) वणजारे (सच्चे व्यापारी के घर) दी (की),",
                "english_gloss": "dass (knowledge/discovery) paindi (dawns) ghar (abode) vanjaare (of divine merchant/soul) dee (of),"
            },
            {
                "original": "है 'यदउल्ल्हा-फ़ौका अयदीकुम' ।",
                "hindi_gloss": "है (कि) 'यदउल्ल्हा-फ़ौका अयदीकुम' ('अल्लाह का हाथ उनके हाथों के ऊपर है') ।",
                "english_gloss": "hai (that) 'yadullaahi fawqa aydeehim' ('The hand of Allah is over their hands') ."
            },
            {
                "original": "चलो देखिए उस मसतानड़े नूं,",
                "hindi_gloss": "चलो (आओ चलें) देखिए (दर्शन करें) उस (उस) मसतानड़े (मस्त फ़क़ीर) नूं (के),",
                "english_gloss": "chalo (come let us go) dekhiye (behold) us (that) mastaan-de (ecstatic master) noon (unto),"
            },
            {
                "original": "जिद्ही त्रिंञणां दे विच पई ए धुंम ।",
                "hindi_gloss": "जिद्ही (जिसकी) त्रिंञणां (सत्संग-मंडली) दे (के) विच (बीच) पई (मची) ए (है) धुंम (धूम) ।",
                "english_gloss": "jidhee (whose) trinjanaan (spinning assemblies) de (of) vich (in) payee (has arisen) e (is) dhumm (fame) ."
            }
        ],
        "hindi_meaning": k24_hi,
        "english_meaning": k24_en
    }]
})

# ==========================================
# KAFI 25: 25. चुप्प करके करीं गुज़ारे नूं
# ==========================================
k25_orig = """सच्च सुणदे लोक ना सहिंदे नी, सच्च आखिए तां गल पैंदे नी,
फिर सच्चे पास ना बहिंदे नी, सच्च मिट्ठा आशक प्यारे नूं ।
चुप्प करके करीं गुज़ारे नूं ।

सच्च शर्हा करे बरबादी ए सच्च आशक दे घर शादी ए,
सच्च करदा नवीं आबादी ए जेही शर्हा तरीकत हारे नूं ।
चुप्प करके करीं गुज़ारे नूं ।

चुप्प आशक तों ना हुन्दी ए, जिस आई सच्च सुगंधी ए,
जिस माला सुहाग दी गुन्दी ए छड्ड दुनियां कूड़ पसारे नूं ।
चुप्प करके करीं गुज़ारे नूं ।

बुल्ल्हा शौह सच्च हुण बोले हैं, सच्च शर्हा तरीकत फोले हैं,
गल्ल चौथे पद दी खोल्हे हैं, जेही शर्हा तरीकत हारे नूं ।
चुप्प करके करीं गुज़ारे नूं ।"""

k25_hi = """सत्य सुनते ही दुनिया के लोग सहन नहीं कर पाते,  
यदि सत्य कह दिया जाए तो वे तुरंत झगड़ने और गला पकड़ने आ जाते हैं!  
वे कभी किसी सच्चे मनुष्य के पास बैठना नहीं चाहते,  
परंतु सच्चे प्रेमी और आशिक़ को तो यही सत्य अमृत के समान मधुर लगता है!  
इसलिए ऐ दिल! इस संसार में मौन रहकर ही अपना जीवन गुज़ारो!  

सत्य रूढ़िवादी कर्मकांडों और बाह्य आडंबरों की नींव हिला देता है,  
पर वही सत्य प्रेमी के अंतःकरण में परमानंद का उत्सव मनाता है!  
जो साधक बाह्य नियमों और औपचारिक साधनाओं से थक कर हार चुके हैं,  
यह सत्य उनके भीतर एक नवीन आत्मिक संसार बसा देता है!  
इसलिए ऐ दिल! इस संसार में मौन रहकर ही अपना जीवन गुज़ारो!  

परंतु जिसे सत्य की पावन सुगंध मिल चुकी हो,  
उस सच्चे आशिक़ से चुप भी तो नहीं रहा जाता!  
जिसने इस मिथ्या संसार के सारे प्रपंचों को छोड़कर,  
अपने प्रभु के नाम का पावन सुहाग-हार गूँथ लिया हो, वह कैसे मौन रहे!  
फिर भी ऐ दिल! इस संसार में मौन रहकर ही अपना जीवन गुज़ारो!  

बुल्ले शाह अब खुलकर उस परम सत्य का उद्घोष कर रहे हैं,  
उन्होंने शरियत और तरीक़त के सारे रहस्यों को उजागर कर दिया है!  
और उस चौथे पद (तुरीयावस्था/हक़ीक़त) का अंतिम सत्य खोल दिया है,  
जो बाह्य साधनों से थके हुए हर जिज्ञासु का उद्धार कर देता है!  
इसलिए ऐ दिल! इस संसार में मौन रहकर ही अपना जीवन गुज़ारो!"""

k25_en = """Worldly folk cannot endure the Truth when it is spoken,  
Speak the Truth, and at thy throat in fury they will fly!  
Near a truthful soul they will never sit or abide,  
Yet to the true lover, Truth is the sweetest nectar from on high!  
Wherefore, O heart, pass thy worldly days in quiet silence!  

The Truth shatters the rigid walls of dogma and outward law,  
Yet in the lover's home it kindles a joyous wedding light!  
For those worn weary by rituals and hollow formal paths,  
Truth builds a fresh kingdom of radiant spiritual delight!  
Wherefore, O heart, pass thy worldly days in quiet silence!  

Yet silence is impossible for the intoxicated lover,  
Whose soul has caught the intoxicating fragrance of the True!  
Having abandoned the false expanse of earthly illusions,  
She weaves the garland of eternal union, pure and new!  
Wherefore, O heart, pass thy worldly days in quiet silence!  

Now Bulleh Shah speaks the absolute Truth without fear,  
Unveiling the hidden essence of law and mystic way!  
Opening wide the gate to the Fourth Realm of supreme light,  
Redeeming the weary seeker who had lost the earthly day!  
Wherefore, O heart, pass thy worldly days in quiet silence!"""

batch.append({
    "id": 25,
    "title": "25. चुप्प करके करीं गुज़ारे नूं",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k25_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "सच्च सुणदे लोक ना सहिंदे नी, सच्च आखिए तां गल पैंदे नी,",
                "hindi_gloss": "सच्च (सत्य) सुणदे (सुनते ही) लोक (दुनिया के लोग) ना (नहीं) सहिंदे (सहन कर पाते) नी (अरी सखी), सच्च (सत्य) आखिए (कहें) तां (तो) गल (गले) पैंदे (पड़ जाते हैं) नी (अरी),",
                "english_gloss": "sachh (truth) sunde (upon hearing) lok (worldly folk) na (not) sahinde (can endure) neen (O friend), sachh (truth) aakhiye (if spoken) taan (then) gal (throat) painde (leap at) neen (they),"
            },
            {
                "original": "फिर सच्चे पास ना बहिंदे नी, सच्च मिट्ठा आशक प्यारे नूं ।",
                "hindi_gloss": "फिर (और फिर) सच्चे (सत्यवादी के) पास (पास) ना (नहीं) बहिंदे (बैठते) नी (अरी), सच्च (परम सत्य) मिट्ठा (अमृत जैसा मीठा लगता है) आशक (सच्चे आशिक़/प्रेमी) प्यारे (प्यारे) नूं (को) ।",
                "english_gloss": "phir (then) sachhe (truthful one) paas (near) na (not) bahinde (sit) neen (they), sachh (truth) mittha (sweet like honey) aashak (devoted lover) pyaare (dear) noon (unto) ."
            },
            {
                "original": "चुप्प करके करीं गुज़ारे नूं ।",
                "hindi_gloss": "चुप्प (मौन/शांत) करके (रहकर ही) करीं (बिताओ) गुज़ारे (जीवन के गुज़ारे/दिनों) नूं (को) ।",
                "english_gloss": "chupp (silence) karke (keeping) kareen (spend) guzaare (days/existence) noon (unto) ."
            },
            {
                "original": "सच्च शर्हा करे बरबादी ए सच्च आशक दे घर शादी ए,",
                "hindi_gloss": "सच्च (सत्य) शर्हा (कर्मकांडी शरियत की) करे (करता है) बरबादी (बरबादी) ए (है), सच्च (सत्य) आशक (सच्चे प्रेमी) दे (के) घर (हृदय में) शादी (परमानंद का उत्सव) ए (है),",
                "english_gloss": "sachh (truth) sharha (dogmatic law's) kare (causes) barbaadi (ruin) e (is), sachh (truth) aashak (of the lover) de (of) ghar (in house) shaadi (wedding celebration) e (is),"
            },
            {
                "original": "सच्च करदा नवीं आबादी ए जेही शर्हा तरीकत हारे नूं ।",
                "hindi_gloss": "सच्च (सत्य) करदा (करता है) नवीं (नवीन आत्मिक) आबादी (जीवन का सृजन) ए (है), जेही (जैसी) शर्हा (कर्मकांड) तरीकत (और औपचारिक साधना से) हारे (थके-हारे साधक) नूं (के लिए) ।",
                "english_gloss": "sachh (truth) karda (creates) naveen (new) aabaadi (habitation/spiritual life) e (is), jehi (such as for) sharha (dogma) tareeqat (pathways) haare (exhausted) noon (unto) ."
            },
            {
                "original": "चुप्प करके करीं गुज़ारे नूं ।",
                "hindi_gloss": "चुप्प (मौन) करके (साधकर) करीं (करो) गुज़ारे (जीवन का निर्वाह) नूं (को) ।",
                "english_gloss": "chupp (silence) karke (maintaining) kareen (pass) guzaare (life) noon (unto) ."
            },
            {
                "original": "चुप्प आशक तों ना हुन्दी ए, जिस आई सच्च सुगंधी ए,",
                "hindi_gloss": "चुप्प (मौन रहना) आशक (सच्चे प्रेमी) तों (से) ना (नहीं) हुन्दी (हो पाता) ए (है), जिस (जिसे) आई (प्राप्त हो गई) सच्च (सत्य की पावन) सुगंधी (सुगंध) ए (है),",
                "english_gloss": "chupp (silence) aashak (lover) ton (from) na (not) hundi (is possible) e (is), jis (who has) aai (received) sachh (of truth) sugandhi (fragrance) e (has),"
            },
            {
                "original": "जिस माला सुहाग दी गुन्दी ए छड्ड दुनियां कूड़ पसारे नूं ।",
                "hindi_gloss": "जिस (जिसने) माला (माला) सुहाग (परम सुहाग/प्रियतम के मिलन) दी (की) गुन्दी (पिरो ली) ए (है), छड्ड (त्यागकर) दुनियां (संसार के) कूड़ (मिथ्या) पसारे (प्रपंच/पसारे) नूं (को) ।",
                "english_gloss": "jis (who) maala (rosary/garland) suhaag (of divine union) dee (of) gundi (woven) e (has), chhadd (abandoning) duniyaan (world's) kood (false) pasaare (illusion/sprawl) noon (unto) ."
            },
            {
                "original": "चुप्प करके करीं गुज़ारे नूं ।",
                "hindi_gloss": "चुप्प (मौन) करके (साधकर) करीं (करो) गुज़ारे (गुज़ारा) नूं (को) ।",
                "english_gloss": "chupp (silence) karke (maintaining) kareen (pass) guzaare (existence) noon (unto) ."
            },
            {
                "original": "बुल्ल्हा शौह सच्च हुण बोले हैं, सच्च शर्हा तरीकत फोले हैं,",
                "hindi_gloss": "बुल्ल्हा (बुल्ले शाह) शौह (प्रभु के) सच्च (परम सत्य को) हुण (अब साफ़) बोले (बोलते) हैं (हैं), सच्च (सत्य के द्वारा) शर्हा (शरियत) तरीकत (और तरीक़त के रहस्यों को) फोले (खोल दिया) हैं (है),",
                "english_gloss": "bullha (Bulleh) shauh (the Lord's) sachh (truth) hun (now) bole (speaks) hain (does), sachh (truth) sharha (dogma) tareeqat (spiritual stage) fole (unveiled) hain (has),"
            },
            {
                "original": "गल्ल चौथे पद दी खोल्हे हैं, जेही शर्हा तरीकत हारे नूं ।",
                "hindi_gloss": "गल्ल (गूढ़ बात) चौथे (चौथे पद / तुरीयावस्था / हक़ीक़त-मारिफ़त) पद (की अवस्था) दी (की) खोल्हे (खोल दी) हैं (है), जेही (जो) शर्हा (बाह्य कर्मकांड) तरीकत (और औपचारिक रास्तों से) हारे (थक चुके साधक को तार देती है) नूं (को) ।",
                "english_gloss": "gall (mystery) chauthe (fourth) pad (state/Turiyavastha) dee (of) kholhe (unlocked) hain (has), jehi (which unto) sharha (external law) tareeqat (formal stages) haare (exhausted seeker) noon (unto) ."
            },
            {
                "original": "चुप्प करके करीं गुज़ारे नूं ।",
                "hindi_gloss": "चुप्प (मौन) करके (साधकर) करीं (करो) गुज़ारे (गुज़ारा) नूं (को) ।",
                "english_gloss": "chupp (silence) karke (maintaining) kareen (pass) guzaare (life) noon (unto) ."
            }
        ],
        "hindi_meaning": k25_hi,
        "english_meaning": k25_en
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
