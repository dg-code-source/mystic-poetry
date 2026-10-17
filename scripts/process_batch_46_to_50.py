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
# KAFI 46: 46. इक नुक़्ता यार पढ़ाइआ ए
# ==========================================
k46_orig = """इक नुक़्ता यार पढ़ाइआ ए ।
इक नुक़्ता यार पढ़ाइआ ए ।

ऐन ग़ैन दी हिक्का सूरत, इक्क नुक़्ते शोर मचाइआ ए,
इक नुक़्ता यार पढ़ाइआ ए ।

सस्सी दा दिल लुट्टण कारण, होत पुनूं बण आया ए,
इक नुक़्ता यार पढ़ाइआ ए ।

बुल्ल्हा शहु दी ज़ात ना काई, मैं शौह इनायत पाइआ ए,
इक नुक़्ता यार पढ़ाइआ ए ।"""

k46_hi = """मेरे प्यारे साजन ने मुझे केवल एक बिंदु (नुक्ता) का पाठ पढ़ाया है!  
'ऐन' और 'ग़ैन' दोनों की आकृति बिल्कुल एक समान है,  
परंतु केवल एक बिंदु ने सारा शोर और भेद खड़ा कर रखा है!  
मेरे प्यारे साजन ने मुझे केवल एक बिंदु का पाठ पढ़ाया है!  

सस्सी के दिल को प्रेम में लूटने के लिए,  
वह परमात्मा स्वयं राजकुमार पुन्नूँ बनकर इस संसार में आया है!  
मेरे प्यारे साजन ने मुझे केवल एक बिंदु का पाठ पढ़ाया है!  

बुल्ले के उस प्राण-स्वामी प्रभु की कोई जाति, कुल या मजहब नहीं है,  
मैंने तो अपने मुर्शिद शाह इनायत के पावन रूप में ही उस सर्वेश्वर को पा लिया है!  
मेरे प्यारे साजन ने मुझे केवल एक बिंदु का पाठ पढ़ाया है!"""

k46_en = """A single dot my Beloved taught to me,  
A single dot unlocks eternity!  

The letters Ain and Ghain share the selfsame line,  
A single dot creates the stir of difference and design!  
A single dot my Beloved taught to me!  

To ravish the heart of Sassui in love's sweet play,  
He descended as the royal prince Punnu today!  
A single dot my Beloved taught to me!  

Bulleh’s Sovereign Lord possesses neither caste nor line,  
In my Murshid Shah Inayat I found that Lord divine!  
A single dot my Beloved taught to me!"""

batch.append({
    "id": 46,
    "title": "46. इक नुक़्ता यार पढ़ाइआ ए",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k46_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "इक नुक़्ता यार पढ़ाइआ ए ।",
                "hindi_gloss": "इक (एक ही) नुक़्ता (बिंदु/रहस्य) यार (मेरे प्रियतम ने) पढ़ाइआ (सिखाया) ए (है) ।",
                "english_gloss": "ik (one) nukta (single dot/secret) yaar (Beloved) padhaaia (taught) e (has) ."
            },
            {
                "original": "इक नुक़्ता यार पढ़ाइआ ए ।",
                "hindi_gloss": "इक (एक) नुक़्ता (नुक्ता) यार (साजन ने) पढ़ाइआ (पढ़ाया) ए (है) ।",
                "english_gloss": "ik (one) nukta (dot) yaar (Beloved) padhaaia (taught) e (has) ."
            },
            {
                "original": "ऐन ग़ैन दी हिक्का सूरत, इक्क नुक़्ते शोर मचाइआ ए,",
                "hindi_gloss": "ऐन ('ऐन' अक्षर और) ग़ैन ('ग़ैन' अक्षर) दी (की) हिक्का (एक ही समान) सूरत (आकृति है), इक्क (किंतु केवल एक) नुक़्ते (बिंदु ने संसार में) शोर (विवाद और भेद का शोर) मचाइआ (मचा रखा) ए (है),",
                "english_gloss": "ain (letter Ain) gain (letter Ghain) dee (of) hikka (one same) soorat (shape), ikk (a single) nukte (dot) shor (clamor/strife) machaaia (raised) e (has),"
            },
            {
                "original": "इक नुक़्ता यार पढ़ाइआ ए ।",
                "hindi_gloss": "इक (एक) नुक़्ता (बिंदु) यार (प्रियतम ने) पढ़ाइआ (सिखाया) ए (है) ।",
                "english_gloss": "ik (one) nukta (dot) yaar (Beloved) padhaaia (taught) e (has) ."
            },
            {
                "original": "सस्सी दा दिल लुट्टण कारण, होत पुनूं बण आया ए,",
                "hindi_gloss": "सस्सी दा (सस्सी का) दिल (हृदय) लुट्टण कारण (लूटने के लिए), होत पुनूं (होतों का राजकुमार पुन्नूँ) बण (बनकर वह परमात्मा ही) आया (आया) ए (है),",
                "english_gloss": "sassee da (of Sassui) dil (heart) luttan kaaran (to plunder), hot punoon (Prince Punnu) ban (becoming) aaya (came) e (has),"
            },
            {
                "original": "इक नुक़्ता यार पढ़ाइआ ए ।",
                "hindi_gloss": "इक (एक) नुक़्ता (रहस्य) यार (साजन ने) पढ़ाइआ (सिखाया) ए (है) ।",
                "english_gloss": "ik (one) nukta (dot) yaar (Beloved) padhaaia (taught) e (has) ."
            },
            {
                "original": "बुल्ल्हा शहु दी ज़ात ना काई, मैं शौह इनायत पाइआ ए,",
                "hindi_gloss": "बुल्ल्हा (हे बुल्ले!) शहु दी (उस प्राण-स्वामी परमात्मा की) ज़ात (कोई जाति या वर्ण) ना (नहीं) काई (कोई भी), मैं (मैंने अपने) शौह (स्वामी) इनायत (शाह इनायत के रूप में उस प्रभु को) पाइआ (पा लिया) ए (है),",
                "english_gloss": "bullha (O Bulleh) shahu dee (of the Lord) zaat (caste/lineage) na (no) kaaee (any), main (I) shauh inaayat (Lord Inayat) paaia (have found) e (have),"
            },
            {
                "original": "इक नुक़्ता यार पढ़ाइआ ए ।",
                "hindi_gloss": "इक (एक) नुक़्ता (बिंदु) यार (प्रियतम ने) पढ़ाइआ (पढ़ाया) ए (है) ।",
                "english_gloss": "ik (one) nukta (dot) yaar (Beloved) padhaaia (taught) e (has) ."
            }
        ],
        "hindi_meaning": k46_hi,
        "english_meaning": k46_en
    }]
})

# ==========================================
# KAFI 47: 47. इक नुक़्ते विच गल्ल मुक्कदी ए
# ==========================================
k47_orig = """फड़ नुक़्ता छोड़ हिसाबां नूं, कर दूर कुफ़र दीआं बाबां नूं,
लाह दोज़ख गोर अज़ाबां नूं, कर साफ दिले दीआं ख़ाबां नूं,
गल्ल एसे घर विच ढुक्कदी ए इक नुक़्ते विच गल्ल मुक्कदी ए ।

ऐवें मत्था ज़मीं घसाईदा, लंमा पा महराब दिखाई दा,
पढ़ कलमा लोक हसाई दा, दिल अन्दर समझ ना लिआई दा,
कदी बात सच्ची वी लुक्कदी ए ? इक नुक़्ते विच गल्ल मुक्कदी ए ।

कई हाजी बण बण आए जी, गल नीले जामे पाए जी,
हज्ज वेच टके लै खाए जी, भला इह गल्ल कीहनूं भाए जी,
कदी बात सच्ची भी लुक्कदी ए ? इक नुक़्ते विच गल्ल मुक्कदी ए ।

इक जंगल बहरीं जांदे नी, इक दाणा रोज़ लै खांदे नी,
बे समझ वजूद थकांदे नी, घर होवणा हो के मांदे नी,
ऐवें चिल्लिआं विच जिन्द मुक्कदी ए इक नुक़्ते विच गल्ल मुक्कदी ए ।

फड़ मुरशद आबद खुदाई हो, विच्च मसती बेपरवाही हो,
बेखाहश बेनवाई हो, विच्च दिल दे खूब सफाई हो,
बुल्ल्हा बात सच्ची कदों रुकदी ए इक नुक्ते विच गल्ल मुक्कदी ए ।"""

k47_hi = """उस एक सत्य-बिंदु को पकड़ लो और व्यर्थ के सारे हिसाब-किताब छोड़ दो!  
अधर्म और संशयों के सारे अध्यायों को अपने से दूर कर दो!  
नरक और कब्र की यातनाओं के काल्पनिक भय को उतार फेंको,  
और अपने दिल के दर्पण को वासनाओं के मैल से साफ़ कर लो!  
परम सत्य की बात तो अंतःकरण के इसी घर में घटती है,  
यह सारा गूढ़ रहस्य केवल एक बिंदु में ही समाप्त हो जाता है!  

यूँ ही ज़मीन पर माथा रगड़ते हो और माथे पर नमाज़ का बड़ा दाग़ दिखाते हो,  
मुख से कलमा पढ़कर दुनिया में अपनी हँसी उड़वाते हो, क्योंकि दिल में उसका मर्म कभी नहीं उतारा!  
भला कभी कोई सच्ची बात भी छिप सकी है?  
यह सारा रहस्य केवल एक बिंदु में ही समाप्त हो जाता है!  

कितने ही लोग मक्के से हाजी बनकर लौटते हैं, और गले में नीले लबादे सजाते हैं,  
हज के पुण्य को सांसारिक मान-बड़ाई के टकों में बेचकर खा जाते हैं—भला यह व्यापार किसे भाए?  
भला कभी कोई सच्ची बात भी छिप सकी है?  
यह सारा रहस्य केवल एक बिंदु में ही समाप्त हो जाता है!  

कोई जंगलों और बियाबानों में भटकता है, कोई दिन में केवल एक अन्न का दाना खाकर रहता है,  
अज्ञान में अपने शरीर को व्यर्थ ही सुखाते हैं, और घट में प्रभु के होते हुए भी विरही होकर दुखी रहते हैं!  
यूँ ही हठयोग के चिल्लों में जीवन समाप्त हो जाता है!  
यह सारा रहस्य केवल एक बिंदु में ही समाप्त हो जाता है!  

सद्गुरु का पल्ला पकड़ो और सच्चे दिल से उस परमात्मा के उपासक बनो!  
प्रेम की मस्ती में मग्न होकर संसार की चिंताओं से बेपरवाह हो जाओ!  
तृष्णाओं से मुक्त और वासनाओं से रिक्त हो जाओ, और अपने दिल को पूरी तरह निर्मल कर लो!  
हे बुल्ले! भला सत्य की बात भी कभी किसी के रोके रुकी है?  
यह सारा रहस्य केवल एक बिंदु में ही समाप्त हो जाता है!"""

k47_en = """Grasp the single dot and leave all calculations behind,  
Cast off chapters of doubt and heresy from thy mind!  
Shed the terrors of hell and the tomb’s gloomy fright,  
Cleanse the mirror of thy heart with pure heavenly light!  
The Truth arrives right within this sanctuary so sweet—  
In a single mystic dot the whole matter is complete!  

In vain dost thou rub thy forehead upon the temple floor,  
Displaying a wide prayer-mark to pride thyself the more!  
Chanting the holy creed, thou makest wise men laugh at thee,  
For thy cold heart never comprehended its inner mystery!  
Can the absolute Truth ever be hidden beneath the sheet?  
In a single mystic dot the whole matter is complete!  

Many return from Mecca, bearing the pilgrim’s proud name,  
Draped in blue robes to feed their worldly fame!  
Selling the holy pilgrimage for a few copper coins of pride—  
Whom does such hollow hypocrisy please far and wide?  
Can the absolute Truth ever be hidden beneath the sheet?  
In a single mystic dot the whole matter is complete!  

Some wander into barren forests and deserts alone,  
Eating a single grain of grain upon the frozen stone!  
Without inner wisdom they exhaust the body in despair,  
While the Lord abides right inside, neglected and unaware!  
In vain ascetic fasts their precious breath is spent in defeat—  
In a single mystic dot the whole matter is complete!  

Grasp the Master’s mantle and become a true worshipper of God!  
Dwell in ecstatic carefree joy upon this earthly sod!  
Free from craving and pride, in humble, quiet surrender shine,  
Keeping the chambers of the heart immaculate and divine!  
O Bulleh, can the voice of Truth ever suffer a retreat?  
In a single mystic dot the whole matter is complete!"""

batch.append({
    "id": 47,
    "title": "47. इक नुक़्ते विच गल्ल मुक्कदी ए",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k47_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "फड़ नुक़्ता छोड़ हिसाबां नूं, कर दूर कुफ़र दीआं बाबां नूं,",
                "hindi_gloss": "फड़ (पकड़ लो) नुक़्ता (उस एक अद्वैत बिंदु को) छोड़ (छोड़ दो) हिसाबां (शास्त्रों और हिसाब-किताब के पचड़ों) नूं (को), कर दूर (दूर कर दो) कुफ़र (अधर्म और संशय) दीआं (के) बाबां (अध्यायों/बातों) नूं (को),",
                "english_gloss": "phad (grasp) nukta (the single dot) chhod (leave) hisaabaan noon (calculations), kar door (expel) kufar deeyaan (of heresy) baabaan noon (chapters),"
            },
            {
                "original": "लाह दोज़ख गोर अज़ाबां नूं, कर साफ दिले दीआं ख़ाबां नूं,",
                "hindi_gloss": "लाह (उतार फेंको) दोज़ख (नरक) गोर (और कब्र के) अज़ाबां (यातनाओं के डर) नूं (को), कर साफ (साफ़ कर लो) दिले (हृदय) दीआं (की) ख़ाबां (भ्रांतियों और वासनाओं) नूं (को),",
                "english_gloss": "laah (shed) dozakh (hell) gor (tomb's) azaabaan noon (torments), kar saaf (purify) dile deeyaan (heart's) khaabaan noon (illusions/dreams),"
            },
            {
                "original": "गल्ल एसे घर विच ढुक्कदी ए इक नुक़्ते विच गल्ल मुक्कदी ए ।",
                "hindi_gloss": "गल्ल (सत्य की बात) एसे (इसी अंतःकरण के) घर (घर) विच (में) ढुक्कदी (घटित होती) ए (है), इक नुक़्ते (एक बिंदु) विच (में) गल्ल (सारी बात) मुक्कदी (समाप्त हो जाती) ए (है) ।",
                "english_gloss": "gall (truth) ese ghar vich (in this very home) dhukkdee e (befits/arrives), ik nukte vich (in a single dot) gall mukkdee e (the whole matter ends) ."
            },
            {
                "original": "ऐवें मत्था ज़मीं घसाईदा, लंमा पा महराब दिखाई दा,",
                "hindi_gloss": "ऐवें (यूँ ही पाखंड में) मत्था (माथा) ज़मीं (ज़मीन पर) घसाईदा (घिसते हो), लंमा पा (बड़ा भारी) महराब (प्रार्थना का निशान/दाग़ माथे पर) दिखाई दा (दिखाते हो),",
                "english_gloss": "aiven (in vain) mattha (forehead) zameen (ground) ghasaa-eeda (is rubbed), lamma paa (broad mark) mahraab (prayer-arch mark) dikhaa-ee da (is displayed),"
            },
            {
                "original": "पढ़ कलमा लोक हसाई दा, दिल अन्दर समझ ना लिआई दा,",
                "hindi_gloss": "पढ़ (मुख से) कलमा (कलमा पढ़कर) लोक (दुनिया में अपना) हसाई दा (उपहास उड़ाते हो), दिल अन्दर (हृदय के भीतर उसका मर्म) समझ (समझ में) ना (नहीं) लिआई दा (लाते),",
                "english_gloss": "padh kalma (reciting creed) lok hasaa-ee da (makes folk mock), dil andar (within heart) samajh na liaa-ee da (bringest no understanding),"
            },
            {
                "original": "कदी बात सच्ची वी लुक्कदी ए ? इक नुक़्ते विच गल्ल मुक्कदी ए ।",
                "hindi_gloss": "कदी (क्या कभी) बात सच्ची (सच्ची बात) वी (भी) लुक्कदी (छिप सकती) ए (है)? इक नुक़्ते (एक बिंदु) विच (में) गल्ल (पूरी बात) मुक्कदी (पूरी होती) ए (है) ।",
                "english_gloss": "kadee baat sachhee vee lukkdee e (can Truth ever be hidden?), ik nukte vich gall mukkdee e (in one dot the matter ends) ."
            },
            {
                "original": "कई हाजी बण बण आए जी, गल नीले जामे पाए जी,",
                "hindi_gloss": "कई (कितने ही लोग) हाजी (हाजी) बण बण (बन-बनकर) आए (लौटते हैं) जी (जी), गल (गले में) नीले (नीले रंग के) जामे (चोले) पाए (पहने हुए) जी (जी),",
                "english_gloss": "kaee (many) haajee (pilgrims) ban ban aae jee (return as), gal (around neck) neele jaame paae jee (wearing blue robes),"
            },
            {
                "original": "हज्ज वेच टके लै खाए जी, भला इह गल्ल कीहनूं भाए जी,",
                "hindi_gloss": "हज्ज (हज के पुण्य को) वेच (बाज़ार में बेचकर) टके (दो-चार कौड़ियाँ) लै खाए (कमाकर खा जाते हैं) जी (जी), भला (भला) इह (यह पाखंड की) गल्ल (बात) कीहनूं (किस सच्चे दिल को) भाए (भा सकती है) जी (जी),",
                "english_gloss": "hajj vech (selling pilgrimage) take lai khaae jee (consume coppers), bhala eh gall keehnoon bhaae jee (whom does this please?),"
            },
            {
                "original": "कदी बात सच्ची भी लुक्कदी ए ? इक नुक़्ते विच गल्ल मुक्कदी ए ।",
                "hindi_gloss": "कदी (क्या कभी) बात सच्ची (सत्य की बात) भी (भी) लुक्कदी (छिपती) ए (है)? इक नुक़्ते (एक बिंदु) विच (में) गल्ल (पूरी बात) मुक्कदी (समाप्त होती) ए (है) ।",
                "english_gloss": "kadee baat sachhee bhee lukkdee e (can Truth ever be veiled?), ik nukte vich gall mukkdee e (in one dot all concludes) ."
            },
            {
                "original": "इक जंगल बहरीं जांदे नी, इक दाणा रोज़ लै खांदे नी,",
                "hindi_gloss": "इक (कुछ वैरागी) जंगल (जंगलों) बहरीं (और मरुस्थलों में) जांदे नी (भटकते फिरते हैं), इक (केवल एक) दाणा (अन्न का दाना) रोज़ (प्रतिदिन) लै (लेकर) खांदे नी (खाते हैं),",
                "english_gloss": "ik (some) jangal bahreen jaande neen (wander wild forests), ik daana roz lai khaande neen (eat one grain daily),"
            },
            {
                "original": "बे समझ वजूद थकांदे नी, घर होवणा हो के मांदे नी,",
                "hindi_gloss": "बे समझ (अज्ञान में) वजूद (इस मानव शरीर को) थकांदे नी (थकाते और सुखाते हैं), घर होवणा (हृदय के भीतर प्रभु के होते हुए भी) हो के मांदे नी (भूखे और बीमार पड़े रहते हैं),",
                "english_gloss": "be samajh (foolishly) vajood thakaande neen (exhaust the frame), ghar hovna (possessing home) ho ke maande neen (grow sick and worn),"
            },
            {
                "original": "ऐवें चिल्लिआं विच जिन्द मुक्कदी ए इक नुक़्ते विच गल्ल मुक्कदी ए ।",
                "hindi_gloss": "ऐवें (यूँ ही व्यर्थ) चिल्लिआं विच (चालीस दिन के हठयोग-तप में) जिन्द (जीवन) मुक्कदी (नष्ट हो जाती) ए (है), इक नुक़्ते (एक बिंदु) विच (में) गल्ल (पूरी बात) मुक्कदी (पूरी होती) ए (है) ।",
                "english_gloss": "aiven chilleeyaan vich (in futile forty-day fasts) jind mukkdee e (life perishes), ik nukte vich gall mukkdee e (in one dot the truth ends) ."
            },
            {
                "original": "फड़ मुरशद आबद खुदाई हो, विच्च मसती बेपरवाही हो,",
                "hindi_gloss": "फड़ (चरण पकड़ो) मुरशद (सद्गुरु के और) आबद (सच्चे उपासक) खुदाई (परमात्मा के) हो (बन जाओ), विच्च मसती (प्रेम की मस्ती में) बेपरवाही (संसार से बेपरवाह) हो (हो जाओ),",
                "english_gloss": "phad murshad (seize Master's hand) aabad khudaaee ho (be worshipper of God), vich mastee (in ecstasy) beparvaahee ho (be carefree),"
            },
            {
                "original": "बेखाहश बेनवाई हो, विच्च दिल दे खूब सफाई हो,",
                "hindi_gloss": "बेखाहश (समस्त तृष्णाओं से मुक्त) बेनवाई (और दीन-वैरागी) हो (हो जाओ), विच्च दिल दे (अपने दिल के भीतर) खूब सफाई (पूर्ण निर्मलता और शुद्धि) हो (रखो),",
                "english_gloss": "bekhaahash (desireless) benavaaee ho (humble), vich dil de (within heart) khoob safaaee ho (maintain pure clarity),"
            },
            {
                "original": "बुल्ल्हा बात सच्ची कदों रुकदी ए इक नुक्ते विच गल्ल मुक्कदी ए ।",
                "hindi_gloss": "बुल्ल्हा (हे बुल्ले!) बात सच्ची (सत्य की बात) कदों (कब) रुकदी (रुक सकती) ए (है), इक नुक्ते (एक बिंदु) विच (में) गल्ल (सारी बात) मुक्कदी (समाप्त हो जाती) ए (है) ।",
                "english_gloss": "bullha baat sachhee kadon rukdee e (when can Truth be arrested?), ik nukte vich gall mukkdee e (in a single dot all concludes) ."
            }
        ],
        "hindi_meaning": k47_hi,
        "english_meaning": k47_en
    }]
})

# ==========================================
# KAFI 48: 48. इक रांझा मैनूं लोड़ीदा
# ==========================================
k48_orig = """कुन-फअकूनों अग्गे दीआं लगियां,
नेहुं ना लगड़ा चोरी दा,
इक रांझा मैनूं लोड़ीदा ।

आप छिड़ जांदा नाल मझ्झीं दे,
सानूं क्यों बेलियों मोड़ीदा,
इक रांझा मैनूं लोड़ीदा ।

रांझे जेहा मैनूं होर ना कोई,
मिन्नतां कर कर मोड़ीदा,
इक रांझा मैनूं लोड़ीदा ।

मान वालियां दे नैन सलोने,
सूहा दुपट्टा गोरी दा,
इक रांझा मैनूं लोड़ीदा ।

अहद अहमद विच फरक ना बुल्लिआ,
इक रत्ती भेत मरोड़ी दा,
इक रांझा मैनूं लोड़ीदा ।"""

k48_hi = """सृष्टि के निर्माण ('कुन फयकून') से भी पहले हमारी यह प्रीत जुड़ चुकी थी,  
यह कोई चोरी-छिपे का प्रेम नहीं है,  
मुझे तो बस केवल मेरा एक रांझा ही चाहिए!  

वह स्वयं तो भैंसों को लेकर चराने जंगल में निकल जाता है,  
फिर मुझे उस जंगल के कछार में आने से क्यों रोकता है?  
मुझे तो बस केवल मेरा एक रांझा ही चाहिए!  

मेरे रांझा जैसा मुझे कोई और दूसरा नहीं भाता,  
संसार के सारे सांसारिक रिश्तों को मैं हाथ जोड़कर लौटा देती हूँ!  
मुझे तो बस केवल मेरा एक रांझा ही चाहिए!  

संसार की गर्वीली स्त्रियों के नयन चाहे कितने भी सलोने हों,  
और सुंदर गोरी नार का दुपट्टा चाहे कितना भी चटक लाल हो, मुझे संसार के रूप-रंग से क्या!  
मुझे तो बस केवल मेरा एक रांझा ही चाहिए!  

हे बुल्ले! 'अहद' (परमात्मा) और 'अहमद' (रसूल) में कोई भेद नहीं है,  
बस केवल 'मीम' के सूक्ष्म घुमाव का ही रत्ती भर भेद है!  
मुझे तो बस केवल मेरा एक रांझा ही चाहिए!"""

k48_en = """Before the primordial decree of Kun fayakun, our love was tied,  
This is no stolen, shameful passion to be kept inside!  
One Ranjha alone is all my soul’s desire!  

He wanders away with the herd into the meadows free,  
Why then does He bar the river-forest paths to me?  
One Ranjha alone is all my soul’s desire!  

None in all the world can ever equal my Beloved’s grace,  
With humble entreaties I turn all worldly suitors from my place!  
One Ranjha alone is all my soul’s desire!  

Let proud earthly beauties boast of charming eyes so bright,  
And drape their scarlet scarves in vanity’s fleeting light!  
One Ranjha alone is all my soul’s desire!  

Between Ahad and Ahmad, O Bulleh, there is no divide,  
Save the single curling curve where the letter Meem must hide!  
One Ranjha alone is all my soul’s desire!"""

batch.append({
    "id": 48,
    "title": "48. इक रांझा मैनूं लोड़ीदा",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k48_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "कुन-फअकूनों अग्गे दीआं लगियां,",
                "hindi_gloss": "कुन-फअकूनों ('कुन फयकून' / सृष्टि की रचना के आदेश) अग्गे दीआं (से पूर्व की ही) लगियां (हमारी प्रीत जुड़ी है),",
                "english_gloss": "kun-fa-akoonon (from before 'Kun fayakun') agge deeyaan (prior to that) lageeyaan (attached was our love),"
            },
            {
                "original": "नेहुं ना लगड़ा चोरी दा,",
                "hindi_gloss": "नेहुं (यह पावन प्रेम) ना लगड़ा (नहीं लगा है) चोरी दा (किसी चोरी-छिपे का),",
                "english_gloss": "nehun (love) na lagda (was not struck) choree da (of stealth/theft),"
            },
            {
                "original": "इक रांझा मैनूं लोड़ीदा ।",
                "hindi_gloss": "इक (केवल एक) रांझा (रांझा) मैनूं (मुझको) लोड़ीदा (चाहिए) ।",
                "english_gloss": "ik (one) raanjha (Ranjha) mainoon (unto me) lodeeda (is desired) ."
            },
            {
                "original": "आप छिड़ जांदा नाल मझ्झीं दे,",
                "hindi_gloss": "आप (वह स्वयं तो) छिड़ जांदा (चला जाता है) नाल (साथ) मझ्झीं दे (भैंसों को चराने),",
                "english_gloss": "aap (Himself) chhid jaanda (wanders off) naal (with) majjheen de (the buffaloes),"
            },
            {
                "original": "सानूं क्यों बेलियों मोड़ीदा,",
                "hindi_gloss": "सानूं (मुझको) क्यों (क्यों भला) बेलियों (जंगल के कछार में आने से) मोड़ीदा (रोकता है),",
                "english_gloss": "saanoon (unto me) kyon (why) beleeyon (from river grove) modeeda (dost turn back),"
            },
            {
                "original": "इक रांझा मैनूं लोड़ीदा ।",
                "hindi_gloss": "इक (एक) रांझा (रांझा) मैनूं (मुझे) लोड़ीदा (चाहिए) ।",
                "english_gloss": "ik (one) raanjha (Ranjha) mainoon (me) lodeeda (is needed) ."
            },
            {
                "original": "रांझे जेहा मैनूं होर ना कोई,",
                "hindi_gloss": "रांझे जेहा (मेरे प्यारे रांझा के समान) मैनूं (मुझको) होर (अन्य) ना कोई (कोई नहीं भाता),",
                "english_gloss": "raanjhe jeha (like Ranjha) mainoon (unto me) hor na koee (none other exists),"
            },
            {
                "original": "मिन्नतां कर कर मोड़ीदा,",
                "hindi_gloss": "मिन्नतां कर कर (संसार के अन्य दूल्हों को मैं विनती कर-करके) मोड़ीदा (लौटा देती हूँ),",
                "english_gloss": "minnataan kar kar (with pleadings) modeeda (I turn suitors away),"
            },
            {
                "original": "इक रांझा मैनूं लोड़ीदा ।",
                "hindi_gloss": "इक (एक) रांझा (रांझा) मैनूं (मुझको) लोड़ीदा (चाहिए) ।",
                "english_gloss": "ik (one) raanjha (Ranjha) mainoon (me) lodeeda (is desired) ."
            },
            {
                "original": "मान वालियां दे नैन सलोने,",
                "hindi_gloss": "मान वालियां दे (अहंकारी सखियों के) नैन सलोने (नेत्र चाहे सलोने हों),",
                "english_gloss": "maan vaaliyaan de (of proud maids) nain salone (eyes may be charming),"
            },
            {
                "original": "सूहा दुपट्टा गोरी दा,",
                "hindi_gloss": "सूहा (और चाहे लाल चटक) दुपट्टा (दुपट्टा) गोरी दा (सुंदर गोरी दुल्हन का हो, मुझे क्या),",
                "english_gloss": "sooha (crimson) dupatta (veil) goree da (of fair maiden),"
            },
            {
                "original": "इक रांझा मैनूं लोड़ीदा ।",
                "hindi_gloss": "इक (एक) रांझा (रांझा) मैनूं (मुझको) लोड़ीदा (चाहिए) ।",
                "english_gloss": "ik (one) raanjha (Ranjha) mainoon (unto me) lodeeda (is desired) ."
            },
            {
                "original": "अहद अहमद विच फरक ना बुल्लिआ,",
                "hindi_gloss": "अहद ('अहद' / परमात्मा) अहमद (और 'अहमद' / नबी) विच (के बीच में) फरक ना (कोई भेद नहीं है) बुल्लिआ (हे बुल्ले),",
                "english_gloss": "ahad ahmad vich (between Ahad and Ahmad) pharak na (no difference) bullia (O Bulleh),",
            },
            {
                "original": "इक रत्ती भेत मरोड़ी दा,",
                "hindi_gloss": "इक रत्ती (केवल रत्ती भर) भेत (रहस्य है 'मीम' के) मरोड़ी दा (मोड़/घुमाव का),",
                "english_gloss": "ik rattee (a single grain) bhet (the mystery) marodee da (of the twist of 'Meem'),"
            },
            {
                "original": "इक रांझा मैनूं लोड़ीदा ।",
                "hindi_gloss": "इक (एक) रांझा (रांझा) मैनूं (मुझको) लोड़ीदा (चाहिए) ।",
                "english_gloss": "ik (one) raanjha (Ranjha) mainoon (unto me) lodeeda (is desired) ."
            }
        ],
        "hindi_meaning": k48_hi,
        "english_meaning": k48_en
    }]
})

# ==========================================
# KAFI 49: 49. इलमों बस्स करीं ओ यार
# ==========================================
k49_orig = """इलम ना आवे विच शुमार, इको अलफ़ तेरे दरकार,
जांदी उमर नहीं इतबार, इलमों बस्स करीं ओ यार ।
इलमों बस्स करीं ओ यार ।

पढ़ पढ़ इलम लगावें ढेर, कुरान किताबां चार चुफेर,
गिरदे चानण विच अन्हेर, बाझों राहबर ख़बर ना सार ।
इलमों बस्स करीं ओ यार ।

पढ़ पढ़ शेख मसायख़ होया, भर भर पेट नींदर भर सोया,
जांदी वारी नैण भर रोया, डुब्बा विच उरार ना पार ।
इलमों बस्स करीं ओ यार ।

पढ़ पढ़ शेख मसायम कहावें, उलटे मसले घरों बणावें,
बे-अकलां नूं लुट लुट खावें, उलटे सिद्धे करें करार ।
इलमों बस्स करीं ओ यार ।

पढ़ पढ़ मुल्लां होइ काज़ी, अल्लाह इलमा बाहझों राज़ी,
होए हिरस दिनो दिन ताज़ी, नफ़ा नियत विच गुज़ार ।
इलमों बस्स करीं ओ यार ।

पढ़ पढ़ नफ़ल नमाज़ गुज़ारें, उच्चियां बांगां चांघां मारें,
मंतर ते चढ़ वाअज़ पुकारें, कीता तैनूं हिरस खुआर ।
इलमों बस्स करीं ओ यार ।

पढ़ पढ़ मसले रोज़ सुणावें, खाणा शक्क सुबहे दा खावें,
दस्सें होर ते होर कमावें, अन्दर खोट बाहर सच्यार ।
इलमों बस्स करीं ओ यार ।

पढ़ पढ़ इलम नजूम विचारे, गिणदा रासां बुरज सतारे,
पढ़े अज़ीमतां मंतर झाड़े, अब जद गिने तअवीज़ शुमार ।
इलमों बस्स करीं ओ यार ।

इलमों पए कज़ीए होर, अक्खीं वाले अन्न्हे कोर,
फड़े साध ते छड्डे चोर, दोहीं जहानीं होया खुआर ।
इलमों बस्स करीं ओ यार ।

इलमों पए हज़ारां फसते, राही अटक रहे विच रसते,
मारिआ हिजर होए दिल खसते, पिआ विछोड़े दा सिर भार ।
इलमों बस्स करीं ओ यार ।

इलमों मियां जी कहावें, तम्बा चुक्क चुक्क मंडी जावें,
धेला लै के छुरी चलावें, नाल कसाईआं बहुत प्यार ।
इलमों बस्स करीं ओ यार ।

बहुता इलम अज़राईल ने पढ़आ, झुग्गा तां ओसे दा सड़्या,
गल विच तौक लाहनत दा पड़्या, आख़िर गया उह बाज़ी हार ।
इलमों बस्स करीं ओ यार ।

जद मैं सबक इश्क दा पढ़आ, दरिआ वेख वहदत दा वड़्या,
घुंमणा घेरां दे विच अड़्या, शाह इनायत लाइआ पार ।
इलमों बस्स करीं ओ यार ।

बुल्ल्हा ना राफज़ी ना है सुन्नी, आलम फ़ाज़ल ना आलम जुन्नी,
इको पढ़आ इलम लदुन्नी, वाहद अलफ़ मीम दरकार ।
इलमों बस्स करीं ओ यार ।"""

k49_hi = """किताबी ज्ञान का कोई अंत नहीं है, तुझे तो बस केवल एक 'अलिफ़' का ज्ञान चाहिए!  
बीतती हुई इस उम्र का कोई भरोसा नहीं, हे यार! अब इस किताबी पोथियों से बस कर!  

किताबों का ढेर लगा रखा है, चारों ओर क़ुरआन और पोथियाँ बिखरी पड़ी हैं!  
चारों ओर किताबों का उजाला है, पर दिल के भीतर घोर अंधेरा छाया है—बिना सच्चे सद्गुरु के कोई आत्म-ज्ञान नहीं मिलता!  
हे यार! अब इस किताबी पोथियों से बस कर!  

पढ़-पढ़कर तू बड़ा शेख और पीर बन गया, पेट भर-भर खाया और अज्ञान की नींद सोया!  
पर अंत समय में जब आँखें भर-भरकर रोया, तो भवसागर में ऐसा डूबा कि न इधर का रहा न उधर का!  
हे यार! अब इस किताबी पोथियों से बस कर!  

पढ़-पढ़कर बड़ा धर्मगुरु कहलाता है, और घर बैठे उल्टे-सीधे फ़तवे गढ़ता है!  
नासमझ जनता को लूट-लूटकर खाता है, और दुनिया से उल्टे-सीधे झूठे वादे करता है!  
हे यार! अब इस किताबी पोथियों से बस कर!  

पढ़-पढ़कर मुल्ला से बड़ा क़ाज़ी बन गया, जबकि अल्लाह तो बिना किताबी आडंबर के केवल सच्चे प्रेम से रीझता है!  
दिन-प्रतिदिन तेरा सांसारिक लोभ बढ़ता जा रहा है, और केवल मुनाफ़ा कमाने की नीयत में तेरा जीवन बीत रहा है!  
हे यार! अब इस किताबी पोथियों से बस कर!  

दिन-रात नफ़्ल नमाज़ें पढ़ता है, ऊँची-ऊँची बाँगें और चीखें मारता है,  
मिंबर पर चढ़कर दुनिया को उपदेश सुनाता है, पर तेरे इस सांसारिक लोभ ने ही तुझे अपमानित कर दिया है!  
हे यार! अब इस किताबी पोथियों से बस कर!  

रोज़ धार्मिक मसले सुनाता है, पर संदेहास्पद और हराम की कमाई खाता है!  
उपदेश कुछ और देता है और आचरण कुछ और करता है, भीतर कपट भरा है और बाहर सच्चा बनता है!  
हे यार! अब इस किताबी पोथियों से बस कर!  

ज्योतिष का इल्म पढ़-पढ़कर राशियाँ, बुर्ज और सितारे गिनता है,  
मंत्र पढ़ता है, झाड़-फूँक करता है, और अब्जद के अंक गिनकर तावीज़ बनाता फिरता है!  
हे यार! अब इस किताबी पोथियों से बस कर!  

इस किताबी विद्या ने समाज में नए-नए झगड़े खड़े कर दिए हैं, आँखों वाले लोग भी नितांत अंधे हो गए हैं!  
सच्चे साधुओं को पकड़ते हैं और चोरों को छोड़ देते हैं, दोनों जहाँ में यह पाखंडी विद्वान अपमानित होता है!  
हे यार! अब इस किताबी पोथियों से बस कर!  

किताबी बहसों में फँसकर हज़ारों पथिक मार्ग के बीच में ही अटक कर रह गए!  
अहंकार के वियोग में उनके दिल जर्जर हो गए, और विरह का भारी बोझ उनके सिर पर पड़ गया!  
हे यार! अब इस किताबी पोथियों से बस कर!  

किताबी इल्म से तू 'मियाँ जी' कहलाता है, पाजामा उठा-उठाकर मंडी भागता है,  
एक धेला लेकर मूक जानवर पर छुरी चलाता है, कसाइयों के साथ तेरी गहरी मित्रता है!  
हे यार! अब इस किताबी पोथियों से बस कर!  

अज़ाज़ील (शैतान) ने बहुत सारा ज्ञान पढ़ा था, पर अंत में उसी का घर जलकर राख हुआ!  
उसके गले में लानत का पट्टा पड़ गया, और आख़िरकार वह जीवन की सारी बाज़ी हार गया!  
हे यार! अब इस किताबी पोथियों से बस कर!  

जब मैंने ईश्वरीय प्रेम का पाठ पढ़ा, तो देखा कि सामने अद्वैत का विशाल दरिया लहरा रहा है!  
जब मैं संसार के भँवरों में फँसने लगा, तो मुर्शिद शाह इनायत ने मुझे भवसागर के पार लगा दिया!  
हे यार! अब इस किताबी पोथियों से बस कर!  

बुल्ला न शिया है और न सुन्नी, न वह कोई घमंडी आलिम है और न कोई संन्यासी!  
उसने तो केवल एक ईश्वरीय आत्मज्ञान (इल्म-ए-लदुन्नी) पढ़ा है, उसे तो बस केवल 'अलिफ़' और 'मीम' की ही आवश्यकता है!  
हे यार! अब इस किताबी पोथियों से बस कर!"""

k49_en = """Bookish learning has no limit or measure, a single Alif is thy only treasure!  
Time is fleeting fast beyond return—cease bookish knowledge, O friend, and learn!  
Cease bookish knowledge, O friend, and learn!  

Piling high mountains of volumes and lore, Holy Quran and scriptures all around thy floor;  
Surrounded by light, yet within reigns deep dark night—without a true Guide, no truth is in sight!  
Cease bookish knowledge, O friend, and learn!  

Studying hard, thou becamest a proud Sheikh and guide, feasting thy belly and sleeping in pride;  
When departure came near, bitter tears didst thou weep, drowning midway in the ocean so deep!  
Cease bookish knowledge, O friend, and learn!  

Calling thyself an authority grand, fabricating crooked decrees by thine own hand;  
Plundering the simple folk without shame or care, making false covenants out of thin air!  
Cease bookish knowledge, O friend, and learn!  

Rising from mullah to judge in high court, yet God is pleased without bookish resort;  
Day by day thy worldly greed waxes green, living for profit behind a religious screen!  
Cease bookish knowledge, O friend, and learn!  

Chanting voluntary prayers through the night, screaming shrill calls at the morning light;  
Climbing the pulpit to preach with proud breath, while thy hidden lust leads thee toward death!  
Cease bookish knowledge, O friend, and learn!  

Reciting sacred doctrines by the hour, yet devouring doubtful food for earthly power;  
Preaching one sermon while living another, false within while playing the pious brother!  
Cease bookish knowledge, O friend, and learn!  

Poring over astrology books with care, counting constellations and zodiacs in the air;  
Chanting incantations and charms in disguise, calculating numerology beneath empty skies!  
Cease bookish knowledge, O friend, and learn!  

From dry bookish learning rise endless debates, turning seeing men blind before heaven’s gates;  
They imprison the saint and let the thief go free, disgraced in both worlds for eternity!  
Cease bookish knowledge, O friend, and learn!  

In the maze of dry knowledge thousands were caught, travelers stranded where pathways are fraught;  
Stricken by separation, their spirits grew frail, crushed by the burden of exile’s pale veil!  
Cease bookish knowledge, O friend, and learn!  

Proudly hailed as the reverend scholar by all, hitching thy garments to rush to the stall;  
For a single penny wielding the slaughtering knife, keeping close company with butchers for life!  
Cease bookish knowledge, O friend, and learn!  

Azazeel (Iblis) mastered mountain-loads of lore, yet his own house burned down to the floor;  
A collar of eternal curse fell on his neck, losing the game, an utter moral wreck!  
Cease bookish knowledge, O friend, and learn!  

When I studied the sacred lesson of Love, I stepped into the river of Unity from above;  
Caught in the whirlpools of worldly strife, Murshid Shah Inayat ferried me into Life!  
Cease bookish knowledge, O friend, and learn!  

Bulleh is neither Shia nor Sunni bound, neither scholar nor ascetic wearing proud crown;  
He studied the single lore of direct divine grace—the sacred Alif and Meem are his only place!  
Cease bookish knowledge, O friend, and learn!"""

batch.append({
    "id": 49,
    "title": "49. इलमों बस्स करीं ओ यार",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k49_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "इलम ना आवे विच शुमार, इको अलफ़ तेरे दरकार,",
                "hindi_gloss": "इलम (किताबी ज्ञान) ना आवे (नहीं आता) विच शुमार (गिनती में/उसका कोई अंत नहीं), इको (केवल एक) अलफ़ (अलिफ़ का सत्य) तेरे दरकार (तुझे आवश्यक है),",
                "english_gloss": "ilam (bookish learning) na aave (comes not) vich shumaar (in calculation/endless), iko alaf (one Alif alone) tere darkaar (is thy requirement),"
            },
            {
                "original": "जांदी उमर नहीं इतबार, इलमों बस्स करीं ओ यार ।",
                "hindi_gloss": "जांदी (बीतती जा रही) उमर (उम्र का) नहीं इतबार (कोई भरोसा नहीं), इलमों (किताबी विद्या से) बस्स करीं (अब बस कर) ओ यार (ओ यार) ।",
                "english_gloss": "jaandee umar (departing life) naaheen itbaar (no trust), ilamon (of bookish learning) bass kareen (put an end) o yaar (O friend) ."
            },
            {
                "original": "इलमों बस्स करीं ओ यार ।",
                "hindi_gloss": "इलमों (किताबी ज्ञान से) बस्स करीं (बस कर) ओ यार (ओ मित्र) ।",
                "english_gloss": "ilamon (with scholarly books) bass kareen (cease) o yaar (O friend) ."
            },
            {
                "original": "पढ़ पढ़ इलम लगावें ढेर, कुरान किताबां चार चुफेर,",
                "hindi_gloss": "पढ़ पढ़ इलम (पढ़-पढ़कर किताबी ज्ञान) लगावें ढेर (तूने पोथियों का ढेर लगा रखा है), कुरान (क़ुरआन और) किताबां (शास्त्र) चार चुफेर (चारों तरफ़ बिखरे हैं),",
                "english_gloss": "padh padh ilam (reading lore) lagaaven dher (pilest heaps), kuraan (Quran) kitaabaan (books) chaar chupher (all around),"
            },
            {
                "original": "गिरदे चानण विच अन्हेर, बाझों राहबर ख़बर ना सार ।",
                "hindi_gloss": "गिरदे (चारों तरफ़) चानण (पोथियों का प्रकाश है किंतु) विच (हृदय के भीतर) अन्हेर (घोर अंधकार है), बाझों राहबर (सच्चे मार्गदर्शक गुरु के बिना) ख़बर ना सार (कोई आत्म-ज्ञान नहीं मिलता) ।",
                "english_gloss": "girde (around) chaanan (light) vich (within) anher (darkness), baajhon raahbar (without Guide) khabar na saar (no news or awareness) ."
            },
            {
                "original": "इलमों बस्स करीं ओ यार ।",
                "hindi_gloss": "इलमों (किताबी विद्या से) बस्स करीं (बस कर) ओ यार (ओ यार) ।",
                "english_gloss": "ilamon (with bookish study) bass kareen (cease) o yaar (O friend) ."
            },
            {
                "original": "पढ़ पढ़ शेख मसायख़ होया, भर भर पेट नींदर भर सोया,",
                "hindi_gloss": "पढ़ पढ़ (पढ़-पढ़कर) शेख मसायख़ होया (बड़ा पूज्य शेख और मुर्शद बन गया), भर भर पेट (पेट भर-भर खाया और) नींदर भर सोया (अज्ञान की गहरी नींद सोया),",
                "english_gloss": "padh padh (studying) shekh masaayakh hoya (became venerated Sheikh), bhar bhar pet (stuffing belly) neendar bhar soya (slept in ignorance),"
            },
            {
                "original": "जांदी वारी नैण भर रोया, डुब्बा विच उरार ना पार ।",
                "hindi_gloss": "जांदी वारी (मृत्यु के समय) नैण भर रोया (आँखों में आँसू भर-भरकर रोया), डुब्बा (भवसागर में डूब गया) विच उरार ना पार (न इस किनारे का रहा न उस पार का) ।",
                "english_gloss": "jaandee vaaree (at dying hour) nain bhar roya (wept with full eyes), dubba (drowned) vich uraar na paar (neither on this shore nor that) ."
            },
            {
                "original": "इलमों बस्स करीं ओ यार ।",
                "hindi_gloss": "इलमों (किताबी ज्ञान से) बस्स करीं (अब बस कर) ओ यार (ओ यार) ।",
                "english_gloss": "ilamon (of learning) bass kareen (stop) o yaar (O friend) ."
            },
            {
                "original": "पढ़ पढ़ शेख मसायम कहावें, उलटे मसले घरों बणावें,",
                "hindi_gloss": "पढ़ पढ़ (पढ़-पढ़कर) शेख मसायम कहावें (बड़ा धर्मगुरु कहलाता है), उलटे मसले (मनमाने उल्टे नियम) घरों बणावें (घर बैठे गढ़ता है),",
                "english_gloss": "padh padh (studying) shekh masaayam kahaaven (callest thyself Sheikh), ulte masle (crooked dogmas) gharon banaaven (inventest at home),"
            },
            {
                "original": "बे-अकलां नूं लुट लुट खावें, उलटे सिद्धे करें करार ।",
                "hindi_gloss": "बे-अकलां नूं (नासमझ जनता को) लुट लुट खावें (लूट-लूटकर खाता है), उलटे सिद्धे (उल्टे-सीधे झूठे) करें करार (वादे करता है) ।",
                "english_gloss": "be-aklaan noon (unto fools) lut lut khaaven (lootest and devourest), ulte siddhe (crooked and straight) karen karaar (makest false pledges) ."
            },
            {
                "original": "इलमों बस्स करीं ओ यार ।",
                "hindi_gloss": "इलमों (किताबी विद्या से) बस्स करीं (बस कर) ओ यार (ओ प्यारे) ।",
                "english_gloss": "ilamon (from books) bass kareen (cease) o yaar (O friend) ."
            },
            {
                "original": "पढ़ पढ़ मुल्लां होइ काज़ी, अल्लाह इलमा बाहझों राज़ी,",
                "hindi_gloss": "पढ़ पढ़ (पढ़-पढ़कर) मुल्लां होइ काज़ी (मुल्ला से क़ाज़ी बन बैठा), अल्लाह (अल्लाह तो) इलमा बाहझों (किताबी ज्ञान के बिना सच्चे प्रेम से) राज़ी (प्रसन्न होता है),",
                "english_gloss": "padh padh (studying) mullaan hoi kaazee (from mullah becamest judge), allaah (Allah) ilma baahjhon (without bookish lore) raazee (is pleased),"
            },
            {
                "original": "होए हिरस दिनो दिन ताज़ी, नफ़ा नियत विच गुज़ार ।",
                "hindi_gloss": "होए (होती जाती है) हिरस (सांसारिक लोभ-लालच) दिनो दिन ताज़ी (दिन-प्रतिदिन ताज़ा), नफ़ा (केवल मुनाफ़ा कमाने की) नियत (नियत) विच गुज़ार (में जीवन बिताता है) ।",
                "english_gloss": "hoe hiras (greed becomes) dino din taazee (fresher day by day), nafa (profit) niyat vich guzaar (passing life in intention of worldly gain) ."
            },
            {
                "original": "इलमों बस्स करीं ओ यार ।",
                "hindi_gloss": "इलमों (किताबी ज्ञान से) बस्स करीं (बस कर) ओ यार (ओ मित्र) ।",
                "english_gloss": "ilamon (of dry lore) bass kareen (halt) o yaar (O friend) ."
            },
            {
                "original": "पढ़ पढ़ नफ़ल नमाज़ गुज़ारें, उच्चियां बांगां चांघां मारें,",
                "hindi_gloss": "पढ़ पढ़ (पढ़-पढ़कर) नफ़ल नमाज़ गुज़ारें (अतिरिक्त नफ़्ल नमाज़ें पढ़ता है), उच्चियां बांगां (ऊँची-ऊँची बाँगें और) चांघां मारें (चीखें मारता है),",
                "english_gloss": "padh padh (chanting) nafal namaaz guzaaren (passest extra prayers), uchheeyaan baangaan (loud calls) chaanghaan maaren (shriekest),"
            },
            {
                "original": "मंतर ते चढ़ वाअज़ पुकारें, कीता तैनूं हिरस खुआर ।",
                "hindi_gloss": "मंतर ते चढ़ (मिंबर पर चढ़कर) वाअज़ पुकारें (उपदेश देता है), कीता (किंतु तेरे इस) तैनूं (तुझको) हिरस (लालच ने ही) खुआर (अपमानित और पतित कर दिया है) ।",
                "english_gloss": "mamar te chadh (mounting pulpit) va'az pukaaren (preachest sermons), keeta tainoon (has made thee) hiras (greed) khuaar (humiliated) ."
            },
            {
                "original": "इलमों बस्स करीं ओ यार ।",
                "hindi_gloss": "इलमों (किताबी विद्या से) बस्स करीं (बस कर) ओ यार (ओ यार) ।",
                "english_gloss": "ilamon (with scholarly pride) bass kareen (desist) o yaar (O friend) ."
            },
            {
                "original": "पढ़ पढ़ मसले रोज़ सुणावें, खाणा शक्क सुबहे दा खावें,",
                "hindi_gloss": "पढ़ पढ़ (पढ़-पढ़कर) मसले (धार्मिक मसले) रोज़ सुणावें (प्रतिदिन सुनाता है), खाणा (किंतु भोजन) शक्क सुबहे दा (संदेहास्पद और हराम की कमाई का) खावें (खाता है),",
                "english_gloss": "padh padh (studying) masle (doctrines) roz sunaaven (recitest daily), khaana (food) shakk subhe da (of doubt/illicit origin) khaaven (eatest),"
            },
            {
                "original": "दस्सें होर ते होर कमावें, अन्दर खोट बाहर सच्यार ।",
                "hindi_gloss": "दस्सें होर (उपदेश कुछ और देता है) ते (और) होर कमावें (आचरण कुछ और करता है), अन्दर खोट (भीतर कपट भरा है) बाहर सच्यार (और बाहर सच्चा बनता है) ।",
                "english_gloss": "dassen hor (teachest one thing) te hor kamaaven (practicest another), andar khot (impurity within) baahar sachyaar (truthful without) ."
            },
            {
                "original": "इलमों बस्स करीं ओ यार ।",
                "hindi_gloss": "इलमों (किताबी ज्ञान से) बस्स करीं (बस कर) ओ यार (ओ मित्र) ।",
                "english_gloss": "ilamon (with bookish pride) bass kareen (cease) o yaar (O friend) ."
            },
            {
                "original": "पढ़ पढ़ इलम नजूम विचारे, गिणदा रासां बुरज सतारे,",
                "hindi_gloss": "पढ़ पढ़ इलम नजूम (ज्योतिष का ज्ञान पढ़-पढ़कर) विचारे (विचार करता है), गिणदा (गिनता है) रासां (राशियाँ) बुरज (राशियों के बुर्ज) सतारे (और सितारे),",
                "english_gloss": "padh padh ilam najoom (astrology) vichaare (contemplates), ginda (counts) raasaan (zodiacs) buraj (mansions) sataare (stars),"
            },
            {
                "original": "पढ़े अज़ीमतां मंतर झाड़े, अब जद गिने तअवीज़ शुमार ।",
                "hindi_gloss": "पढ़े अज़ीमतां (मंत्र और आयतें पढ़ता है) मंतर झाड़े (झाड़-फूँक करता है), अब जद गिने (अब्जद के अंक गिनता है) तअवीज़ शुमार (और तावीज़ों का हिसाब रखता है) ।",
                "english_gloss": "padhe azeemataan (chants spells) mantar jhaade (exorcises), ab jad gine (calculates numerology) ta'veez shumaar (tallies amulets) ."
            },
            {
                "original": "इलमों बस्स करीं ओ यार ।",
                "hindi_gloss": "इलमों (किताबी विद्या से) बस्स करीं (बस कर) ओ यार (ओ यार) ।",
                "english_gloss": "ilamon (of dry lore) bass kareen (cease) o yaar (O friend) ."
            },
            {
                "original": "इलमों पए कज़ीए होर, अक्खीं वाले अन्न्हे कोर,",
                "hindi_gloss": "इलमों (इस किताबी ज्ञान से) पए (पैदा हुए हैं) कज़ीए होर (हज़ारों नए झगड़े), अक्खीं वाले (आँखों वाले लोग भी) अन्न्हे कोर (नितांत अंधे बन गए हैं),",
                "english_gloss": "ilamon (from pedantry) pae (arose) kazee-e hor (fresh disputes), akkheen vaale (those with eyes) annhe kor (totally blind),"
            },
            {
                "original": "फड़े साध ते छड्डे चोर, दोहीं जहानीं होया खुआर ।",
                "hindi_gloss": "फड़े साध (सच्चे साधुओं को पकड़ते हैं) ते (और) छड्डे चोर (चोरों को खुला छोड़ देते हैं), दोहीं जहानीं (दोनों लोकों में) होया खुआर (यह अहंकारी विद्वान अपमानित होता है) ।",
                "english_gloss": "phade saadh (imprison saint) te chhadde chor (release thief), doheen jahaaneen (in both worlds) hoya khuaar (humiliated) ."
            },
            {
                "original": "इलमों बस्स करीं ओ यार ।",
                "hindi_gloss": "इलमों (किताबी ज्ञान से) बस्स करीं (बस कर) ओ यार (ओ प्यारे) ।",
                "english_gloss": "ilamon (from lore) bass kareen (cease) o yaar (O friend) ."
            },
            {
                "original": "इलमों पए हज़ारां फसते, राही अटक रहे विच रसते,",
                "hindi_gloss": "इलमों (किताबी बहसों में) पए (पड़कर) हज़ारां फसते (हज़ारों लोग फँस गए), राही (सच्चे पथिक) अटक रहे (अटक कर रह गए) विच रसते (मार्ग के बीच में ही),",
                "english_gloss": "ilamon (in bookish traps) pae (fell) hazaaraan phaste (thousands entangled), raahee (travelers) atak rahe (halted) vich raste (in midway),"
            },
            {
                "original": "मारिआ हिजर होए दिल खसते, पिआ विछोड़े दा सिर भार ।",
                "hindi_gloss": "मारिआ हिजर (विरह की मार से) होए दिल खसते (हृदय जर्जर हो गए), पिआ (पड़ गया) विछोड़े दा (वियोग का) सिर भार (सिर पर भारी बोझ) ।",
                "english_gloss": "maaria hijar (struck by separation) hoe dil khaste (hearts ruined), pia (fell) vichhode da (of exile) sir bhaar (heavy load on head) ."
            },
            {
                "original": "इलमों बस्स करीं ओ यार ।",
                "hindi_gloss": "इलमों (किताबी विद्या से) बस्स करीं (बस कर) ओ यार (ओ यार) ।",
                "english_gloss": "ilamon (with book study) bass kareen (stop) o yaar (O friend) ."
            },
            {
                "original": "इलमों मियां जी कहावें, तम्बा चुक्क चुक्क मंडी जावें,",
                "hindi_gloss": "इलमों (किताबी इल्म से) मियां जी कहावें (मियाँ जी कहलाता है), तम्बा चुक्क चुक्क (अपना पाजामा उठा-उठाकर) मंडी जावें (मंडी में भागता है),",
                "english_gloss": "ilamon (by book learning) miyaan jee kahaaven (art called scholar), tamba chukk chukk (lifting robes) mandee jaaven (rushest to market),"
            },
            {
                "original": "धेला लै के छुरी चलावें, नाल कसाईआं बहुत प्यार ।",
                "hindi_gloss": "धेला लै के (एक धेला लेकर जानवर पर) छुरी चलावें (हलाल की छुरी चलाता है), नाल कसाईआं (कसाइयों के साथ) बहुत प्यार (तेरा बड़ा गहरा प्रेम है) ।",
                "english_gloss": "dhela lai ke (taking half-penny) chhooree chalaaven (wieldest knife), naal kasaaeeyaan (with butchers) bahut pyaar (much affection) ."
            },
            {
                "original": "इलमों बस्स करीं ओ यार ।",
                "hindi_gloss": "इलमों (किताबी ज्ञान से) बस्स करीं (बस कर) ओ यार (ओ मित्र) ।",
                "english_gloss": "ilamon (with scholarly pride) bass kareen (halt) o yaar (O friend) ."
            },
            {
                "original": "बहुता इलम अज़राईल ने पढ़आ, झुग्गा तां ओसे दा सड़्या,",
                "hindi_gloss": "बहुता इलम (बहुत सारा ज्ञान) अज़राईल (अज़ाज़ील / इब्लीस / शैतान) ने पढ़आ (ने पढ़ा था), झुग्गा (किंतु घर) तां ओसे दा सड़्या (उसी का जलकर राख हुआ),",
                "english_gloss": "bahuta ilam (immense knowledge) azraaeel ne padha (Azazeel/Iblis studied), jhugga (abode) taan ose da sadya (his alone was burned),"
            },
            {
                "original": "गल विच तौक लाहनत दा पड़्या, आख़िर गया उह बाज़ी हार ।",
                "hindi_gloss": "गल विच (गले में) तौक लाहनत दा (लाहौल और लानत का पट्टा) पड़्या (पड़ गया), आख़िर (अंत में) गया उह बाज़ी हार (वह जीवन की बाज़ी हार गया) ।",
                "english_gloss": "gal vich (around neck) tauk laahnat da padya (collar of curse fell), aakhir (at last) gaya uh baazee haar (lost the game) ."
            },
            {
                "original": "इलमों बस्स करीं ओ यार ।",
                "hindi_gloss": "इलमों (किताबी विद्या से) बस्स करीं (बस कर) ओ यार (ओ यार) ।",
                "english_gloss": "ilamon (from dry lore) bass kareen (cease) o yaar (O friend) ."
            },
            {
                "original": "जद मैं सबक इश्क दा पढ़आ, दरिआ वेख वहदत दा वड़्या,",
                "hindi_gloss": "जद (जब) मैं (मैंने) सबक (पाठ) इश्क दा (इश्क़ का) पढ़आ (पढ़ा), दरिआ वेख (देखा कि अद्वैत का विशाल दरिया है) वहदत दा वड़्या (उसमें उतर पड़ा),",
                "english_gloss": "jad main (when I) sabak ishq da padha (studied lesson of Love), daria vekh vahdat da vadya (seeing river of Unity entered),"
            },
            {
                "original": "घुंमणा घेरां दे विच अड़्या, शाह इनायत लाइआ पार ।",
                "hindi_gloss": "घुंमणा घेरां दे विच (भँवरों के चक्कर में जब मैं) अड़्या (फँस गया), शाह इनायत (तब मुर्शिद शाह इनायत ने) लाइआ पार (मुझको भवसागर के पार लगा दिया) ।",
                "english_gloss": "ghumnan gheraan de vich adya (stuck in whirlpools), shaah inaayat (Shah Inayat) laaia paar (ferried me across) ."
            },
            {
                "original": "इलमों बस्स करीं ओ यार ।",
                "hindi_gloss": "इलमों (किताबी ज्ञान से) बस्स करीं (अब बस कर) ओ यार (ओ मित्र) ।",
                "english_gloss": "ilamon (with scholarly books) bass kareen (cease) o yaar (O friend) ."
            },
            {
                "original": "बुल्ल्हा ना राफज़ी ना है सुन्नी, आलम फ़ाज़ल ना आलम जुन्नी,",
                "hindi_gloss": "बुल्ल्हा (बुल्ले शाह) ना राफज़ी (न तो शिया है) ना है सुन्नी (और न ही सुन्नी है), आलम फ़ाज़ल ना (न वह कोई महान विद्वान है) आलम जुन्नी (न कोई पाखंडी तपस्वी),",
                "english_gloss": "bullha (Bulleh) na raafzee (neither Shia) na hai sunnee (nor Sunni), aalam faazal na (neither erudite scholar) na aalam junnee (nor cloistered ascetic),"
            },
            {
                "original": "इको पढ़आ इलम लदुन्नी, वाहद अलफ़ मीम दरकार ।",
                "hindi_gloss": "इको पढ़आ (उसने तो केवल एक ही) इलम लदुन्नी (इलाही आत्मज्ञान का पाठ पढ़ा है), वाहद (केवल उस एक) अलफ़ (अलिफ़ और) मीम दरकार (मीम की ही उसे आवश्यकता है) ।",
                "english_gloss": "iko padha (read only one) ilam ladunnee (divine esoteric knowledge), vaahad alaf meem darkaar (the One Alif and Meem are his only need) ."
            },
            {
                "original": "इलमों बस्स करीं ओ यार ।",
                "hindi_gloss": "इलमों (किताबी ज्ञान से) बस्स करीं (बस कर) ओ यार (ओ प्यारे मित्र) ।",
                "english_gloss": "ilamon (with bookish pride) bass kareen (cease) o yaar (O beloved friend) ."
            }
        ],
        "hindi_meaning": k49_hi,
        "english_meaning": k49_en
    }]
})

# ==========================================
# KAFI 50: 50. इश्क असां नाल केही कीती, लोक मरेंदे तअने
# ==========================================
k50_orig = """दिल दी वेदन कोई ना जाणे, अन्दर देस बगाने,
जिस नूं चाट अमर दी होवे, सोई अमर पछाणे,
एस इश्क दी औखी घाटी, जो चढ़आ सो जाणे ।
इश्क असां नाल केही कीती, लोक मरेंदे तअने ।

आतश इश्क फ़राक तेरे दी, पल विच साड़ विखाईआं,
एस इश्क दे साड़े कोलों, जग विच दिआं दुहाईआं,
जिस तन लग्गे सो तन जाणे, दूजा कोई ना जाणे ।
इश्क असां नाल केही कीती, लोक मरेंदे तअने ।

इश्क कसाई ने जेही कीती, रह गई ख़बर ना काई,
इश्क चवाती लाई छाती, फेर ना झाती पाई,
माप्यां कोलों छुप छुप रोवां, कर कर लक्ख बहाने ।
इश्क असां नाल केही कीती, लोक मरेंदे तअने ।

हिजर तेरे ने झल्ली करके, कमली नाम धराइआ,
सुमुन बुकमुन व उमयुन हो के, आपणा वकत लंघाइआ,
कर हुण नज़र करम दी साईआं, न कर ज़ोर धङाने ।
इश्क असां नाल केही कीती, लोक मरेंदे तअने ।

हस्स बुलावां तेरा जानी, याद करां हर वेले,
पल पल दे विच दर्द जुदाई, तेरा शाम सवेले,
रो रो याद करां दिन रातीं, पिछले वकत वेहाने ।
इश्क असां नाल केही कीती, लोक मरेंदे तअने ।

इश्क तेरा दरकार असां नूं, हर वेले हर हीले,
पाक रसूल मुहंमद साहब, मेरे खास वसीले,
बुल्ल्हे शाह जो मिले प्यारा, लक्ख करां शुकराने ।
इश्क असां नाल केही कीती, लोक मरेंदे तअने ।"""

k50_hi = """इस पराई दुनिया में मेरे दिल की विरह-वेदना को कोई नहीं समझता!  
जिसके दिल पर उस अमर प्रेम की चोट लगी हो, वही उस अमर सत्य को पहचान सकता है!  
इस प्रेम की चढ़ाई बड़ी कठिन और दुर्गम घाटी है, जो इस पर चढ़ता है केवल वही इसका दर्द जानता है!  
इस इश्क़ ने मेरे साथ क्या हाल कर दिया है, और दुनिया मुझ पर ताने मारती है!  

तुम्हारे विरह की इस आग ने पल भर में मुझे जलाकर राख कर दिया है!  
इस प्रेम की जलन से मेरी चीखें सारे संसार में गूँज उठी हैं!  
जिस तन पर यह चोट लगती है वही तन जानता है, दूसरा कोई इसका भेद नहीं जान सकता!  
इस इश्क़ ने मेरे साथ क्या हाल कर दिया है, और दुनिया मुझ पर ताने मारती है!  

इस इश्क़-रूपी कसाई ने मेरे साथ ऐसी क्रूरता की है कि मेरी सुध-बुध ही नहीं रही!  
मेरे सीने पर विरह का सुलगता अंगारा रख दिया, और फिर पलटकर कभी मुझे नहीं देखा!  
लाखों बहाने बना-बनाकर मैं अपने माता-पिता और परिजनों से छिप-छिपकर रोती हूँ!  
इस इश्क़ ने मेरे साथ क्या हाल कर दिया है, और दुनिया मुझ पर ताने मारती है!  

तुम्हारे विरह ने मुझे बावली कर दिया, और संसार ने मेरा नाम 'कमली' रख दिया!  
संसार के प्रति मैं बहरी, गूँगी और अंधी होकर अपना समय बिता रही हूँ!  
हे मेरे स्वामी! अब तो मुझ पर अपनी रहमत की नज़र करो, मुझ दीन पर यह ज़ुल्म मत करो!  
इस इश्क़ ने मेरे साथ क्या हाल कर दिया है, और दुनिया मुझ पर ताने मारती है!  

हे मेरे प्राण-प्यारे! मैं हर समय तुम्हें याद करती हूँ, और सुबह-शाम तुम्हारे वियोग की असह्य पीड़ा सहती हूँ!  
बीते हुए मिलन के पलों को याद कर-करके मैं रात-दिन आँसू बहाती हूँ!  
इस इश्क़ ने मेरे साथ क्या हाल कर दिया है, और दुनिया मुझ पर ताने मारती है!  

मुझे हर क्षण और हर उपाय से केवल तुम्हारा ही पावन प्रेम चाहिए!  
पवित्र पैग़ंबर मुहम्मद साहब मेरे सर्वोच्च आश्रय और माध्यम हैं!  
हे बुल्ले शाह! यदि मुझे मेरा प्यारा स्वामी मिल जाए, तो मैं लाखों बार उस ईश्वर का धन्यवाद करूँ!  
इस इश्क़ ने मेरे साथ क्या हाल कर दिया है, और दुनिया मुझ पर ताने मारती है!"""

k50_en = """None understands the secret agony of my soul in this alien land!  
Only one struck by the eternal spark can understand what Love has planned!  
The steep cliff of Love is an arduous climb—only the traveler knows the height!  
Alas, what has Love done to me, while worldly folk mock my plight!  

The blazing fire of thy separation has burned me to ash in a breath,  
From the agony of this flame, my cries shake the chambers of death!  
The body that bears the wound alone knows the searing pain,  
No onlooker can ever fathom the torment of this rain!  
Alas, what has Love done to me, while worldly folk mock my plight!  

Like a merciless butcher, Love has severed my senses and pride,  
Placing a burning coal on my breast, turning His face to hide!  
With thousand excuses I steal away, weeping behind the door,  
Hiding my overflowing tears from parents upon the floor!  
Alas, what has Love done to me, while worldly folk mock my plight!  

Thy separation has driven me mad, crowning me with folly's name,  
Deaf, dumb, and blind to the world I wander, oblivious to praise or shame!  
Cast a glance of grace upon me now, O Master of my soul,  
End this relentless torment and make this broken spirit whole!  
Alas, what has Love done to me, while worldly folk mock my plight!  

With a trembling smile I call thy sweet name, my Life, my Darling King,  
At dawn and dusk the barbed arrows of parting relentlessly sting!  
Weeping through the lonely night, I recall the golden days of old,  
When thy sweet presence warmed my heart against the winter’s cold!  
Alas, what has Love done to me, while worldly folk mock my plight!  

Thy divine Love alone is the sole need of my thirsty breast,  
The Holy Prophet Muhammad is my refuge and sacred rest!  
If Bulleh Shah meets his Beloved Lord in luminous embrace,  
A hundred thousand songs of gratitude shall fill eternal space!  
Alas, what has Love done to me, while worldly folk mock my plight!"""

batch.append({
    "id": 50,
    "title": "50. इश्क असां नाल केही कीती, लोक मरेंदे तअने",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k50_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "दिल दी वेदन कोई ना जाणे, अन्दर देस बगाने,",
                "hindi_gloss": "दिल दी (हृदय की) वेदन (गहरी विरह-वेदना को) कोई ना जाणे (कोई नहीं जानता), अन्दर (इस पराए) देस बगाने (देश संसार में),",
                "english_gloss": "dil dee (heart's) vedan (secret anguish) koee na jaane (none knows), andar des bagaane (in this alien land),"
            },
            {
                "original": "जिस नूं चाट अमर दी होवे, सोई अमर पछाणे,",
                "hindi_gloss": "जिस नूं (जिसको) चाट (चोट/तीव्र प्यास) अमर दी (अमर प्रेम की) होवे (होती है), सोई (वही साधक) अमर पछाणे (उस अमर तत्व को पहचानता है),",
                "english_gloss": "jis noon (whoever) chaat (wound/thirst) amar dee (of the immortal) hove (has), soee (he alone) amar pachhaane (discerns the immortal),"
            },
            {
                "original": "एस इश्क दी औखी घाटी, जो चढ़आ सो जाणे ।",
                "hindi_gloss": "एस (इस) इश्क दी (इश्क़ की) औखी (कठिन और दुर्गम) घाटी (घाटी है), जो (जो इस पर) चढ़आ (चढ़ता है) सो (वही इसका रहस्य) जाणे (जानता है) ।",
                "english_gloss": "es ishq dee (of this Love) aukhee ghaatee (arduous cliff), jo chadha (who mounts) so jaane (he alone knows) ."
            },
            {
                "original": "इश्क असां नाल केही कीती, लोक मरेंदे तअने ।",
                "hindi_gloss": "इश्क (इस ईश्वरीय प्रेम ने) असां नाल (मेरे साथ) केही (कैसी विचित्र दशा) कीती (की है), लोक (संसार के लोग) मरेंदे तअने (मुझ पर ताने मारते हैं) ।",
                "english_gloss": "ishq (Love) asaan naal (with me) kehee keetee (what has done), lok marende ta-ane (folk cast taunts) ."
            },
            {
                "original": "आतश इश्क फ़राक तेरे दी, पल विच साड़ विखाईआं,",
                "hindi_gloss": "आतश (अग्नि) इश्क (प्रेम और) फ़राक (तुम्हारे विरह की) तेरे दी (तुम्हारी), पल विच (पल भर में) साड़ विखाईआं (जलाकर भस्म कर दिया है),",
                "english_gloss": "aatash ishq (fire of love) faraak tere dee (of thy separation), pal vich (in a moment) saad vikhaaeeaan (burned away),"
            },
            {
                "original": "एस इश्क दे साड़े कोलों, जग विच दिआं दुहाईआं,",
                "hindi_gloss": "एस इश्क दे (इस प्रेम की) साड़े कोलों (जलन के कारण), जग विच (संसार में) दिआं दुहाईआं (मेरी चीखें गूँज उठी हैं),",
                "english_gloss": "es ishq de saade kolon (from this burning of love), jag vich (in the world) deeyaan duhaaeeaan (my cries resound),"
            },
            {
                "original": "जिस तन लग्गे सो तन जाणे, दूजा कोई ना जाणे ।",
                "hindi_gloss": "जिस तन (जिस तन पर) लग्गे (यह चोट लगती है) सो तन (वही तन) जाणे (जानता है), दूजा (अन्य) कोई ना (कोई भी नहीं) जाणे (जान सकता) ।",
                "english_gloss": "jis tan lagge (the body that suffers) so tan jaane (that body alone knows), dooja koee na jaane (no other can know) ."
            },
            {
                "original": "इश्क असां नाल केही कीती, लोक मरेंदे तअने ।",
                "hindi_gloss": "इश्क (प्रेम ने) असां नाल (मेरे साथ) केही कीती (कैसा हाल किया), लोक (लोग) मरेंदे तअने (ताने मारते हैं) ।",
                "english_gloss": "ishq (Love) asaan naal (with me) kehee keetee (what has done), lok (people) marende ta-ane (hurl taunts) ."
            },
            {
                "original": "इश्क कसाई ने जेही कीती, रह गई ख़बर ना काई,",
                "hindi_gloss": "इश्क कसाई ने (इस इश्क़-रूपी कसाई ने) जेही (जैसी क्रूर दशा) कीती (की है), रह गई (रह गई) ख़बर ना काई (मेरी कोई सुध-बुध नहीं रही),",
                "english_gloss": "ishq kasaaee ne (Love the butcher) jehee keetee (what has wrought), rah gayee khabar na kaaee (no consciousness remained),"
            },
            {
                "original": "इश्क चवाती लाई छाती, फेर ना झाती पाई,",
                "hindi_gloss": "इश्क चवाती (इश्क़ का सुलगता अंगारा) लाई (लगा दिया) छाती (मेरे सीने पर), फेर ना (और फिर कभी पलटकर) झाती पाई (मेरी ओर झाँक कर नहीं देखा),",
                "english_gloss": "ishq chavaatee (firebrand of love) laaee chhaatee (set upon breast), pher na jhaatee paaee (glanced back no more),"
            },
            {
                "original": "माप्यां कोलों छुप छुप रोवां, कर कर लक्ख बहाने ।",
                "hindi_gloss": "माप्यां कोलों (अपने माता-पिता और परिजनों से) छुप छुप (छिप-छिपकर) रोवां (मैं रोती हूँ), कर कर (बना-बनाकर) लक्ख बहाने (लाखों बहाने) ।",
                "english_gloss": "maapyaan kolon (from parents) chhup chhup rovaan (I weep in secret), kar kar lakkh bahaane (making myriad excuses) ."
            },
            {
                "original": "इश्क असां नाल केही कीती, लोक मरेंदे तअने ।",
                "hindi_gloss": "इश्क (प्रेम ने) असां नाल (मेरे साथ) केही कीती (कैसा हाल किया), लोक (संसार) मरेंदे तअने (ताने मारता है) ।",
                "english_gloss": "ishq (Love) asaan naal (unto me) kehee keetee (what has done), lok (folk) marende ta-ane (fling taunts) ."
            },
            {
                "original": "हिजर तेरे ने झल्ली करके, कमली नाम धराइआ,",
                "hindi_gloss": "हिजर तेरे ने (तुम्हारे वियोग ने) झल्ली करके (मुझे पागल/विह्वल करके), कमली (बावरी का) नाम धराइआ (नाम दिला दिया है),",
                "english_gloss": "hijar tere ne (thy separation) jhallee karke (making maddened), kamlee naam dharaaia (conferred name of 'crazed'),"
            },
            {
                "original": "सुमुन बुकमुन व उमयुन हो के, आपणा वकत लंघाइआ,",
                "hindi_gloss": "सुमुन बुकमुन व उमयुन ('सुम्मुन बुक्मुन उम्युन' - बहरी, गूँगी और अंधी) हो के (होकर संसार के प्रति), आपणा (अपना) वकत (समय) लंघाइआ (गुज़ारा है),",
                "english_gloss": "sumun bukmun va umyun ho ke (becoming deaf, dumb, and blind), aapna vakat langhaaia (passed my days),"
            },
            {
                "original": "कर हुण नज़र करम दी साईआं, न कर ज़ोर धङाने ।",
                "hindi_gloss": "कर (करो) हुण (अब तो) नज़र (कृपादृष्टि) करम दी (रहमत की) साईआं (हे मेरे स्वामी), न कर (मत करो) ज़ोर धङाने (मुझ पर यह जबरदस्ती और बेरुखी) ।",
                "english_gloss": "kar hun nazar karam dee saaeeyaan (cast now a glance of grace, O Master), na kar zor dhadaane (force not tyranny on me) ."
            },
            {
                "original": "इश्क असां नाल केही कीती, लोक मरेंदे तअने ।",
                "hindi_gloss": "इश्क (प्रेम ने) असां नाल (मेरे साथ) केही कीती (कैसी दशा बनाई), लोक (लोग) मरेंदे तअने (ताने कसते हैं) ।",
                "english_gloss": "ishq (Love) asaan naal (with me) kehee keetee (what has wrought), lok (folk) marende ta-ane (shoot taunts) ."
            },
            {
                "original": "हस्स बुलावां तेरा जानी, याद करां हर वेले,",
                "hindi_gloss": "हस्स (हँस-हँसकर) बुलावां (मैं पुकारती हूँ) तेरा जानी (तुम्हारा नाम, हे मेरे प्राण-प्यारे), याद करां (याद करती हूँ) हर वेले (हर समय),",
                "english_gloss": "hass bulaavaan (smiling I invoke) tera jaanee (thee, Soul's Beloved), yaad karaan (remember) har vele (at all times),"
            },
            {
                "original": "पल पल दे विच दर्द जुदाई, तेरा शाम सवेले,",
                "hindi_gloss": "पल पल दे विच (प्रतिक्षण में) दर्द (दर्द भरा है) जुदाई (वियोग का) तेरा (तुम्हारा), शाम सवेले (सुबह और शाम),",
                "english_gloss": "pal pal de vich (in every moment) dard judaaee (pain of parting) tera (thine), shaam savele (dusk and dawn),"
            },
            {
                "original": "रो रो याद करां दिन रातीं, पिछले वकत वेहाने ।",
                "hindi_gloss": "रो रो (रो-रोकर) याद करां (स्मरण करती हूँ) दिन रातीं (दिन और रात), पिछले (बीते हुए सुहावने) वकत वेहाने (मिलन के पलों को) ।",
                "english_gloss": "ro ro yaad karaan (weeping I remember) din raateen (day and night), pichhle vakat vehaane (bygone sweet times) ."
            },
            {
                "original": "इश्क असां नाल केही कीती, लोक मरेंदे तअने ।",
                "hindi_gloss": "इश्क (प्रेम ने) असां नाल (मेरे साथ) केही कीती (कैसा व्यवहार किया), लोक (लोग) मरेंदे तअने (ताने मारते हैं) ।",
                "english_gloss": "ishq (Love) asaan naal (with me) kehee keetee (what has done), lok (folk) marende ta-ane (taunt me) ."
            },
            {
                "original": "इश्क तेरा दरकार असां नूं, हर वेले हर हीले,",
                "hindi_gloss": "इश्क तेरा (तुम्हारा पावन प्रेम) दरकार (अनिवार्य) असां नूं (हमारे लिए), हर वेले (हर घड़ी) हर हीले (हर यत्न से),",
                "english_gloss": "ishq tera (thy love) darkaar (is sought) asaan noon (unto us), har vele (at all hours) har heele (by every means),"
            },
            {
                "original": "पाक रसूल मुहंमद साहब, मेरे खास वसीले,",
                "hindi_gloss": "पाक रसूल (पवित्र पैग़ंबर) मुहंमद साहब (हज़रत मुहम्मद मुस्तफ़ा), मेरे (मेरे) खास वसीले (परम माध्यम और आश्रय हैं),",
                "english_gloss": "paak rasool muhammad saahab (the holy Messenger Muhammad), mere khaas vaseele (my special intercessor),"
            },
            {
                "original": "बुल्ल्हे शाह जो मिले प्यारा, लक्ख करां शुकराने ।",
                "hindi_gloss": "बुल्ल्हे शाह (बुल्ले शाह को) जो (यदि) मिले (मिल जाएँ) प्यारा (प्राण-प्यारे स्वामी), लक्ख (लाखों बार) करां (करूँगा) शुकराने (ईश्वर का शुक्राना/धन्यवाद) ।",
                "english_gloss": "bullhe shaah (Bulleh Shah) jo mile pyaara (if Beloved is met), lakkh karaan shukraane (hundred thousand thanks I shall offer) ."
            },
            {
                "original": "इश्क असां नाल केही कीती, लोक मरेंदे तअने ।",
                "hindi_gloss": "इश्क (प्रेम ने) असां नाल (मेरे साथ) केही कीती (कैसा हाल किया), लोक (लोग) मरेंदे तअने (ताने मारते हैं) ।",
                "english_gloss": "ishq (Love) asaan naal (with me) kehee keetee (what has done), lok (folk) marende ta-ane (mock me) ."
            }
        ],
        "hindi_meaning": k50_hi,
        "english_meaning": k50_en
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
