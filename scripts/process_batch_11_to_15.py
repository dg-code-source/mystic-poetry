import os
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
KAFIAN_DIR = os.path.join(DATA_DIR, "kafian")
CHECKPOINT_JSON = os.path.join(DATA_DIR, "checkpoint.json")

os.makedirs(KAFIAN_DIR, exist_ok=True)

batch = []

# ==========================================
# KAFI 11
# ==========================================
k11_orig = """अलफ़ अल्लाह नाल रत्ता दिल मेरा,
मैनूं 'बे' दी ख़बर ना काई ।

'बे' पढ़दियां मैनूं समझ ना आवे,
लज्जत अलफ़ दी आई ।

'ऐना ते गैना' नूं समझ ना जाणा,
गल्ल अलफ़ समझाई ।

बुल्ल्हआ कौल अलफ़ दे पूरे,
जिहड़े दिल दी करन सफाई ।"""

k11_hi = """अलिफ़ (अल्लाह) के नाम में मेरा दिल ऐसा रंग गया है,
कि मुझे 'बे' (दूसरे अक्षर/संसार) की कोई खबर ही नहीं!

जब मैं 'बे' पढ़ने लगता हूँ तो कुछ समझ नहीं आता,
क्योंकि मुझे तो अलिफ़ (एक ओंकार) का दिव्य स्वाद लग चुका है!

'ऐन' और 'ग़ैन' (शास्त्रों के उलझे अक्षरों) को मैं नहीं समझता,
मुझे तो अलिफ़ के अकेले हर्फ़ ने ही सारा रहस्य समझा दिया है!

बुल्ले शाह कहते हैं—अलिफ़ के वचन ही पूर्ण और सच्चे हैं,
जो साधक के अंतर्मन और हृदय की सारी मैल धोकर साफ़ कर देते हैं!"""

k11_en = """My heart is dyed in the divine Alif of Allah,
I have no knowledge or heed of the letter 'Bey'!

When I try to read 'Bey', my mind cannot comprehend,
For the sublime sweetness of Alif has tasted my soul!

I know naught of the intricate letters 'Ain' and 'Ghain',
The singular Alif has unveiled the entire Truth to me!

O Bulleh, the covenants of Alif are whole and complete,
They purify the soul, cleansing the heart of all deceit!"""

batch.append({
    "id": 11,
    "title": "11. अलफ़ अल्लाह नाल रत्ता दिल मेरा",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k11_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "अलफ़ अल्लाह नाल रत्ता दिल मेरा,",
                "hindi_gloss": "अलफ़ (अलिफ़/परमात्मा) अल्लाह (अल्लाह) नाल (के साथ) रत्ता (रंग गया है) दिल (हृदय) मेरा (मेरा),",
                "english_gloss": "alif (first letter/One God) allah (Allah) naal (with) ratta (dyed/steeped) dil (heart) mera (my),"
            },
            {
                "original": "मैनूं 'बे' दी ख़बर ना काई ।",
                "hindi_gloss": "मैनूं (मुझे) 'बे' ('बे'/संसार/द्वैत) दी (की) ख़बर (सुध) ना (नहीं) काई (कोई भी) ।",
                "english_gloss": "mainoon (unto me) 'bey' (second letter/duality) dee (of) khabar (heed/awareness) na (not) kaai (any) ."
            },
            {
                "original": "'बे' पढ़दियां मैनूं समझ ना आवे, लज्जत अलफ़ दी आई ।",
                "hindi_gloss": "'बे' ('बे'/दुनियावी विद्या) पढ़दियां (पढ़ते हुए) मैनूं (मुझे) समझ (समझ) ना (नहीं) आवे (आती), लज्जत (दिव्य रस/स्वाद) अलफ़ (अलिफ़) दी (का) आई (आया है) ।",
                "english_gloss": "'bey' (letter 'B'/worldly learning) padhdiyaan (while reading) mainoon (to me) samajh (understanding) na (not) aave (comes), lazzat (sweet relish) alif (of Alif) dee (of) aai (has arrived) ."
            },
            {
                "original": "'ऐना ते गैना' नूं समझ ना जाणा, गल्ल अलफ़ समझाई ।",
                "hindi_gloss": "'ऐना ('ऐन) ते (और) गैना' (ग़ैन को) नूं (को) समझ (समझना) ना (नहीं) जाणा (जानता), गल्ल (सारी बात/रहस्य) अलफ़ (अलिफ़ ने) समझाई (समझा दिया है) ।",
                "english_gloss": "'aina (letter Ain) te (and) gaina' (letter Ghain) noon (unto) samajh (comprehend) na (not) jaana (know), gall (secret of truth) alif (Alif) samjhaai (explained) ."
            },
            {
                "original": "बुल्ल्हआ कौल अलफ़ दे पूरे, जिहड़े दिल दी करन सफाई ।",
                "hindi_gloss": "बुल्ल्हआ (हे बुल्ले) कौल (वचन/मार्ग) अलफ़ (अलिफ़ के) दे (के) पूरे (पूर्ण/सच्चे हैं), जिहड़े (जो) दिल (हृदय) दी (की) करन (करते हैं) सफाई (पवित्रता/सफाई) ।",
                "english_gloss": "bullhya (O Bulleh) kaul (covenants/words) alif (of Alif) de (of) poore (perfect/complete), jihde (which) dil (of heart) dee (of) karan (perform) safaai (cleansing/purification) ."
            }
        ],
        "hindi_meaning": k11_hi,
        "english_meaning": k11_en
    }]
})

# ==========================================
# KAFI 12
# ==========================================
k12_orig = """अम्मां बाबे दी भलिआई, उह हुन कंम असाडे आई ।
अम्मां बाबा होर दो राहां दे, पुत्तर दी वड्याई ।
दाणे उत्तों गुत्त बिगुत्ती, घर घर पई लड़ाई ।
असां कज़ीए तदाहीं जाले, जदां कणक उन्हां टरघाई ।
खाए खैरातें फाटीए जुंमा, उल्टी दसतक लाई ।
बुल्ल्हा तोते मार बागां थीं कढ्ढे, उल्लू रहन उस जाई ।
अम्मां बाबे दी भलिआई, उह हुन कंम असाडे आई ।"""

k12_hi = """हमारे आदि-माता-पिता (हव्वा और आदम) की 'भलाई' देखो,
वह भूल अब हमारी संतानों के सिर आ पड़ी है!
माता-पिता तो दो अलग राहों पर निकल गए,
और पुत्र की बड़ाई इसी में रही कि वह संसार में फंस गया!

गेहूं के एक दाने के पीछे गुत्थमगुत्था हो गए,
और आज घर-घर में वही कलह और लड़ाई फैली है!
हमने ये सारे कष्ट और क्लेश तभी से झेले हैं,
जब उन्होंने स्वर्ग में मना किया हुआ गेहूं खा लिया था!

खैरात और दान खाकर शुक्रवार को जमात में झगड़ते हैं,
संसार की उलटी ही रीत और दस्तक चल रही है!
बुल्ले शाह कहते हैं—सुंदर तोतों को मारकर बागों से भगा दिया गया,
और उस पवित्र स्थान पर अब उल्लू डेरा जमाए बैठे हैं!
हमारे आदि-माता-पिता की वह 'भलाई' अब हमारे काम आ रही है!"""

k12_en = """Behold the 'good deed' of our primal mother and father (Eve and Adam),
Whose ancient consequence now falls upon our head!
Mother and father parted ways down different roads,
Leaving their progeny tangled in this mortal spread!

Over a single forbidden grain they fell into brawl,
And now in every home that same bitter strife is shed!
All these miseries and trials have we endured,
Ever since they consumed the wheat from which they fled!

Feeding on alms yet tearing each other on Friday's prayer,
Upside down are the knocks and customs of this world!
Bulleh Shah says: Sweet parrots were slain and driven from the groves,
While dark owls dwell where celestial blossoms unfurled!
Behold the legacy of our primal ancestors,
Which now bears heavy upon us instead!"""

batch.append({
    "id": 12,
    "title": "12. अम्मां बाबे दी भलिआई",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k12_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "अम्मां बाबे दी भलिआई, उह हुन कंम असाडे आई ।",
                "hindi_gloss": "अम्मां (माता हव्वा) बाबे (पिता आदम) दी (की) भलिआई (भलाई/करतूत), उह (वह) हुन (अब) कंम (सिर पर/काम) असाडे (हमारे) आई (आई है) ।",
                "english_gloss": "ammaan (mother Eve) baabe (father Adam) dee (of) bhaliaai (good deed/conduct), uh (that) hun (now) kamm (to our lot) asaade (ours) aai (has come) ."
            },
            {
                "original": "अम्मां बाबा होर दो राहां दे, पुत्तर दी वड्याई ।",
                "hindi_gloss": "अम्मां (माता) बाबा (पिता) होर (दो अलग) दो (दो) राहां (राहों) दे (के हो गए), पुत्तर (संतान/पुत्र) दी (की यह) वड्याई (बड़ाई/दुर्दशा) ।",
                "english_gloss": "ammaan (mother) baaba (father) hor (different) do (two) raahaan (paths) de (of), puttar (son's) dee (of) vadyaai (glory/ironic fate) ."
            },
            {
                "original": "दाणे उत्तों गुत्त बिगुत्ती, घर घर पई लड़ाई ।",
                "hindi_gloss": "दाणे (गेहूं के दाने) उत्तों (के ऊपर) गुत्त बिगुत्ती (गुत्थमगुत्था/झगड़ा हुआ), घर (घर) घर (घर में) पई (पड़ गई है) लड़ाई (लड़ाई) ।",
                "english_gloss": "daane (grain of wheat) utton (over) gutt-bigutti (scuffle/tussle), ghar (home) ghar (home in) pai (erupted) ladaai (conflict/fighting) ."
            },
            {
                "original": "असां कज़ीए तदाहीं जाले, जदां कणक उन्हां टरघाई ।",
                "hindi_gloss": "असां (हमने) कज़ीए (कष्ट/क्लेश) तदाहीं (तभी से) जाले (झेले हैं), जदां (जब) कणक (गेहूं) उन्हां (उन्होंने) टरघाई (खा लिया था/हड़प किया) ।",
                "english_gloss": "asaan (we) kazie (miseries/trials) tadaaheen (ever since) jaale (endured), jadaan (when) kanak (wheat) unhaan (they) targhaai (devoured) ."
            },
            {
                "original": "खाए खैरातें फाटीए जुंमा, उल्टी दसतक लाई ।",
                "hindi_gloss": "खाए (खाते हैं) खैरातें (दान/खैरात) फाटीए (फाड़ते/झगड़ते हैं) जुंमा (जुमे की नमाज़ पर), उल्टी (उल्टी ही) दसतक (दस्तक/रीत) लाई (लगा रखी है) ।",
                "english_gloss": "khaaye (consuming) khairaaten (alms) faatiye (quarrel) jumma (on Friday prayer), ulti (inverted) dastak (custom/knock) laai (practiced) ."
            },
            {
                "original": "बुल्ल्हा तोते मार बागां थीं कढ्ढे, उल्लू रहन उस जाई ।",
                "hindi_gloss": "बुल्ल्हा (हे बुल्ले) तोते (सुंदर तोतों को) मार (मारकर) बागां (बागों) थीं (से) कढ्ढे (निकाल दिया), उल्लू (उल्लू) रहन (रहते हैं) उस (उस) जाई (स्थान पर) ।",
                "english_gloss": "bullha (O Bulleh) tote (sweet parrots) maar (killing) baagaan (gardens) theen (from) kaddhe (expelled), ulloo (owls) rahan (dwell) us (in that) jaai (place) ."
            }
        ],
        "hindi_meaning": k12_hi,
        "english_meaning": k12_en
    }]
})

# ==========================================
# KAFI 13
# ==========================================
k13_orig = """अपने संग रलाईं प्यारे, अपने संग रलाईं ।
पहलों नेहुं लगाइआ सी तैं आपे चाईं चाईं ।
मैं लाइआ ए कि तुद्ध लाइआ ए आपनी ओड़ निभाईं ।
राह पवां तां धाड़े बेले, जंगल लक्ख बलाईं ।
भौकन चीते ते चितमुचित्ते भौकन करन अदाईं ।
पार तेरे जगत तर चढ़आ कंढे लक्ख बलाईं ।
हौल दिले दा थर थर कम्बदा बेड़ा पार लंघाईं ।
कर लई बन्दगी रब्ब सच्चे दी पवन कबूल दुआईं ।
बुल्ल्हे शाह ते शाहां दा मुक्खड़ा घुंघट खोल्ह विखाईं ।
अपने संग रलाईं प्यारे, अपने संग रलाईं ।"""

k13_hi = """मुझे अपने संग मिला ले प्यारे, अपने संग मिला ले!
पहले तो बड़े चाव और उमंग से तूने खुद मुझसे नेह लगाया था!
अब यह मैंने लगाया या तूने, तू ही इस प्रेम को अंत तक निभा ले!

जब तेरी राह पर कदम रखती हूँ, तो रास्ते में डाकुओं से भरे बीहड़ हैं,
और जंगल में लाखों बलाएं और भयानक विपत्तियां हैं!
चीते और कपटी जानवर गरजते हैं और डरावने हमले करते हैं!
संसार रूपी इस भवसागर के किनारे पर लाखों आपदाएं खड़ी हैं,
डर के मारे मेरा दिल थर-थर कांप रहा है, तू ही मेरी नाव पार लगा ले!

सच्चे परमात्मा की सच्ची बंदगी कर ली है, अब ये दुआएं कबूल हो जाएं!
बुल्ले शाह के परमेश्वर! घूंघट खोलकर अपना नूरानी मुखड़ा दिखा दे!
मुझे अपने संग मिला ले प्यारे, अपने संग मिला ले!"""

k13_en = """Unite me with Thyself, O Beloved, blend me with Thyself!
At first, with eager joy and longing, Thou Thyself didst kindle this love!
Whether I wove it or Thou didst, now fulfill it to the very end!

When I tread Thy path, wild bandits lurk in the ravines,
And a hundred thousand perils haunt the deep woods!
Cheetahs and treacherous beasts roar and stalk in ambush!
At the shore of this worldly ocean, a million calamities arise,
My heart trembles in dread; guide my fragile vessel across the tide!

I have offered my devotion to the True Lord, may these prayers be accepted!
O Master of Bulleh Shah, lift Thy veil and reveal Thy radiant face!
Unite me with Thyself, O Beloved, blend me with Thyself!"""

batch.append({
    "id": 13,
    "title": "13. अपने संग रलाईं प्यारे, अपने संग रलाईं",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k13_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "अपने संग रलाईं प्यारे, अपने संग रलाईं ।",
                "hindi_gloss": "अपने (अपने) संग (साथ) रलाईं (मिला ले) प्यारे (हे प्रियतम), अपने (अपने) संग (साथ) रलाईं (मिला ले) ।",
                "english_gloss": "apne (own) sang (with) ralaaeen (unite/blend) pyaare (O Beloved), apne (own) sang (with) ralaaeen (unite) ."
            },
            {
                "original": "पहलों नेहुं लगाइआ सी तैं आपे चाईं चाईं ।",
                "hindi_gloss": "पहलों (पहले) नेहुं (प्रेम) लगाइआ (लगाया) सी (था) तैं (तूने) आपे (स्वयं ही) चाईं (चाव से) चाईं (उमंग से) ।",
                "english_gloss": "pahlon (at first) nehun (love) lagaaiya (bound) see (had) tain (you) aape (yourself) chaaeen (with eager joy) chaaeen (fondly) ."
            },
            {
                "original": "मैं लाइआ ए कि तुद्ध लाइआ ए आपनी ओड़ निभाईं ।",
                "hindi_gloss": "मैं (मैंने) लाइआ (लगाया) ए (है) कि (या) तुद्ध (तूने) लाइआ (लगाया) ए (है), आपनी (अपनी ओर से) ओड़ (अंत तक) निभाईं (निभा लेना) ।",
                "english_gloss": "main (I) laaiya (bound) e (have) ki (or) tuddh (you) laaiya (bound) e (have), aapni (your own) od (to the very end) nibhaaeen (fulfill/honor) ."
            },
            {
                "original": "राह पवां तां धाड़े बेले, जंगल लक्ख बलाईं ।",
                "hindi_gloss": "राह (मार्ग पर) पवां (चलती हूँ) तां (तो) धाड़े (डाकुओं के) बेले (बीहड़ हैं), जंगल (जंगल में) लक्ख (लाखों) बलाईं (बलाएं/विपत्तियां हैं) ।",
                "english_gloss": "raah (on path) pawaan (if I set foot) taan (then) dhaade (of bandits) bele (wildernesses), jangal (forest in) lakkh (lakhs of) balaaeen (calamities/perils) ."
            },
            {
                "original": "भौकन चीते ते चितमुचित्ते भौकन करन अदाईं ।",
                "hindi_gloss": "भौकन (गरजते हैं) चीते (चीते) ते (और) चितमुचित्ते (कपटी पशु) भौकन (गुर्राते हैं) करन (करते हैं) अदाईं (हमले/घात) ।",
                "english_gloss": "bhaukan (roar) cheete (cheetahs/leopards) te (and) chit-muchitte (treacherous beasts) bhaukan (snarl) karan (make) adaaeen (ambushes/attacks) ."
            },
            {
                "original": "पार तेरे जगत तर चढ़आ कंढे लक्ख बलाईं ।",
                "hindi_gloss": "पार (उस पार) तेरे (तेरे दर्शन की चाह में) जगत (संसार-नदी पर) तर (तैरने) चढ़आ (चढ़ा है), कंढे (किनारे पर) लक्ख (लाखों) बलाईं (मुसीबतें हैं) ।",
                "english_gloss": "paar (across) tere (towards you) jagat (world ocean) tar (crossing) chadha (embarked), kandhe (on shore) lakkh (lakhs of) balaaeen (dangers) ."
            },
            {
                "original": "हौल दिले दा थर थर कम्बदा बेड़ा पार लंघाईं ।",
                "hindi_gloss": "हौल (भय से) दिले (हृदय) दा (का) थर (थर) थर (थर) कम्बदा (कांपता है), बेड़ा (जीवन की नाव) पार (उस पार) लंघाईं (पार लगा देना) ।",
                "english_gloss": "haul (dread) dile (heart) da (of) thar (trembling) thar (quivering) kambda (shakes), beda (ferry/boat) paar (across) langhaaeen (ferry safely) ."
            },
            {
                "original": "कर लई बन्दगी रब्ब सच्चे दी पवन कबूल दुआईं ।",
                "hindi_gloss": "कर (कर) लई (ली है) बन्दगी (इबादत) रब्ब (परमात्मा) सच्चे (सच्चे) दी (की), पवन (हो जाएं) कबूल (स्वीकार) दुआईं (प्रार्थनाएं) ।",
                "english_gloss": "kar (having made) laee (done) bandagi (devotion) rabb (Lord) sachche (True) dee (of), pawan (may become) kabool (accepted) duaaeein (supplications) ."
            },
            {
                "original": "बुल्ल्हे शाह ते शाहां दा मुक्खड़ा घुंघट खोल्ह विखाईं ।",
                "hindi_gloss": "बुल्ल्हे (बुल्ले के) शाह (शाह) ते (तथा) शाहां (शाखों के शाह का) मुक्खड़ा (मुखड़ा) घुंघट (घूंघट) खोल्ह (खोलकर) विखाईं (दिखा दो) ।",
                "english_gloss": "bullhe (of Bulleh) shah (Master) te (and) shaahaan (of Kings) da (of) mukkhda (radiant face) ghungat (veil) kholh (lifting) vikhaaeen (reveal) ."
            }
        ],
        "hindi_meaning": k13_hi,
        "english_meaning": k13_en
    }]
})

# ==========================================
# KAFI 14 (Tere Ishq Nachaya)
# ==========================================
k14_orig = """बहुड़ीं वे तबीबा मैंडी जिन्द गईआ ।
तेरे इश्क नचाइआ कर थईआ थईआ ।

इश्क डेरा मेरे अन्दर कीता,
भर के ज़हर प्याला मैं पीता,
झबदे आवीं वे तबीबा नहीं ते मैं मर गईआं ।
तेरे इश्क नचाइआ कर थईआ थईआ ।

छुप्प ग्या सूरज बाहर रह गई आ लाली,
होवां मैं सदके मुड़ जे दें विखाली ,
मैं भुल्ल गईआं तेरे नाल ना गईआं ।
तेरे इश्क नचाइआ कर थईआ थईआ ।

तेरे इश्क दी सार वे मैं ना जाणां,
इह सिर आया ए मेरा हेठ वदाणां,
सट्ट पई इश्के दी तां कूकां दईआं ।
तेरे इश्क नचाइआ कर थईआ थईआ ।

एस इश्क दे कोलों सानूं हटक ना माए,
लाहू (लाहौर) जांदड़े बेड़े मोड़ कौन हटाए,
मेरी अकल भुल्ली नाल मुहाणिआँ दे गईआं ।
तेरे इश्क नचाइआ कर थईआ थईआ ।

एस इश्क दी झंगी विच मोर बुलेंदा,
सानूं काबा ते किबला प्यारा यार दसेंदा,
सानूं घायल करके फिर ख़बर ना लईआ ।
तेरे इश्क नचाइआ कर थईआ थईआ ।

बुल्ल्हा शाह इनायत दे बह बूहे,
जिस पहनाए सानूं सावे सूहे,
जां मैं मारी उडारी मिल पिआ वहीआ ।
तेरे इश्क नचाइआ कर थईआ थईआ ।"""

k14_hi = """जल्दी आ मेरे हकीम, मेरी जान निकली जा रही है,
तेरे इश्क ने मुझे थिरक-थिरक नाचना सिखाया है!

इस इश्क ने मेरे अंतर्मन में अपना डेरा डाल लिया,
और मैंने हंसकर विष से भरा प्याला पी लिया!
जल्दी आ मेरे चारागर, वरना मेरी सांसें छूट जाएंगी;
तेरे इश्क ने मुझे थिरक-थिरक नाचना सिखाया है!

सूरज डूब गया है और क्षितिज पर केवल लाली बाकी रह गई,
मैं तुझ पर न्योछावर हो जाऊं अगर तू फिर से एक बार दर्शन दे दे!
मुझसे भारी भूल हुई कि उस समय मैं तेरे संग न गई;
तेरे इश्क ने मुझे थिरक-थिरक नाचना सिखाया है!

मैं तेरे इश्क की गहराई और मर्म को नहीं समझ पाई थी,
अब मेरा यह सिर निहाई के नीचे लोहार के हथौड़ों पर आ पड़ा है!
इश्क की ऐसी चोट पड़ी है कि हृदय से विरह की चीखें निकल रही हैं;
तेरे इश्क ने मुझे थिरक-थिरक नाचना सिखाया है!

हे मेरी मां! मुझे इस इश्क के रास्ते से मत रोक,
लाहौर की ओर बहती नावों को मोड़कर भला कौन रोक सकता है?
मेरी सांसारिक अक्ल खो गई, मैं तो प्रेम के मल्लाहों संग निकल पड़ी;
तेरे इश्क ने मुझे थिरक-थिरक नाचना सिखाया है!

इस प्रेम के घने कुंज-वन में दिव्य मोर मधुर कूकता है,
हमारे लिए तो काबा और किबला हमारा प्यारा यार ही दिखाई देता है!
उसने मुझे अपने प्रेम-बाण से घायल कर दिया, फिर कोई सुध न ली;
तेरे इश्क ने मुझे थिरक-थिरक नाचना सिखाया है!

बुल्ले शाह सतगुरु शाह इनायत के पावन द्वार पर आ बैठा है,
जिन्होंने मुझे सुहाग के हरे और लाल वस्त्र पहना दिए हैं!
जैसे ही मैंने आत्मा की उड़ान भरी, मुझे वही परमेश्वर मिल गया;
तेरे इश्क ने मुझे थिरक-थिरक नाचना सिखाया है!"""

k14_en = """Come quickly, O spiritual Physician, my life is slipping away,
Thy love has made me dance in ecstatic surrender!

Love has pitched its tent deep within my heart,
Smiling, I drained the chalice brimmed with poison!
Hasten, O Healer, lest breath desert my earthly clay;
Thy love has made me dance in ecstatic surrender!

The sun has set, only the dusk's crimson glow remains,
I would surrender my all if Thou wouldst appear once again!
Great was my folly that I did not walk with Thee when Thou didst depart;
Thy love has made me dance in ecstatic surrender!

I knew not the unfathomed depth of this divine love,
Now my head lies upon the anvil beneath the blacksmith's sledge!
When love's hammer struck, cries of longing burst from my soul;
Thy love has made me dance in ecstatic surrender!

O mother, restrain me not from this sacred path of love,
Who can turn back the vessels bound for Lahore's rushing tide?
My worldly intellect is gone, I have boarded with the divine ferrymen;
Thy love has made me dance in ecstatic surrender!

In the dense grove of this love, the celestial peacock calls,
For me, the Kaaba and Qibla are revealed in the face of my Beloved!
He wounded me with love's dart, then asked no tidings of my plight;
Thy love has made me dance in ecstatic surrender!

Bulleh sits at the threshold of Master Shah Inayat,
Who adorned me in the green and crimson robes of the Bride!
As soon as my spirit took wing, the Supreme Beloved met me there;
Thy love has made me dance in ecstatic surrender!"""

batch.append({
    "id": 14,
    "title": "14. बहुड़ीं वे तबीबा मैंडी जिन्द गईआ",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k14_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "बहुड़ीं वे तबीबा मैंडी जिन्द गईआ ।",
                "hindi_gloss": "बहुड़ीं (जल्दी आ/सुध ले) वे (हे) तबीबा (हकीम/वैद्य) मैंडी (मेरी) जिन्द (जान/प्राण) गईआ (निकल गई) ।",
                "english_gloss": "bahudeen (come quickly/heal) ve (O) tabeeba (physician) maindi (my) jind (life/breath) gaeea (is departed) ."
            },
            {
                "original": "तेरे इश्क नचाइआ कर थईआ थईआ ।",
                "hindi_gloss": "तेरे (तेरे) इश्क (प्रेम ने) नचाइआ (नचाया है) कर (करके) थईआ (थिरक-थिरक) थईआ (ता-थैया) ।",
                "english_gloss": "tere (your) ishq (love) nachaaiya (made dance) kar (making) thayya (rhythmic steps) thayya (dancing in ecstasy) ."
            },
            {
                "original": "इश्क डेरा मेरे अन्दर कीता, भर के ज़हर प्याला मैं पीता,",
                "hindi_gloss": "इश्क (प्रेम ने) डेरा (अपना बसेरा) मेरे (मेरे) अन्दर (भीतर) कीता (बना लिया), भर (भर) के (कर) ज़हर (विष का) प्याला (प्याला) मैं (मैंने) पीता (पी लिया),",
                "english_gloss": "ishq (love) dera (abode/camp) mere (my) andar (within) keeta (made), bhar (filled) ke (having) zehar (poison) pyaala (cup) main (I) peeta (drank),"
            },
            {
                "original": "झबदे आवीं वे तबीबा नहीं ते मैं मर गईआं ।",
                "hindi_gloss": "झबदे (शीघ्र/जल्दी) आवीं (आना) वे (हे) तबीबा (वैद्य) नहीं (नहीं) ते (तो) मैं (मैं) मर (मर) गईआं (जाऊंगी) ।",
                "english_gloss": "jhabde (swiftly/without delay) aaveen (come) ve (O) tabeeba (physician) nahin (not) te (otherwise) main (I) mar (die) gaeeaan (shall) ."
            },
            {
                "original": "छुप्प ग्या सूरज बाहर रह गई आ लाली, होवां मैं सदके मुड़ जे दें विखाली ,",
                "hindi_gloss": "छुप्प (डूब) ग्या (गया) सूरज (सूरज) बाहर (क्षितिज पर) रह (रह) गई (गई है) आ (केवल) लाली (लालिमा), होवां (हो जाऊं) मैं (मैं) सदके (न्योछावर/बलिहारी) मुड़ (पुनः/फिर) जे (यदि) दें (दे दो) विखाली (दर्शन/दीदार) ,",
                "english_gloss": "chhupp (set) gya (has) sooraj (sun) baahar (outside/horizon) rah (remained) gaee (has) a (only) laali (red dusk), howaan (may I be) main (I) sadke (sacrificed) mud (again) je (if) dein (grant) vikhaali (vision/glimpse) ,"
            },
            {
                "original": "मैं भुल्ल गईआं तेरे नाल ना गईआं ।",
                "hindi_gloss": "मैं (मुझसे) भुल्ल (भूल) गईआं (हो गई कि) तेरे (तेरे) नाल (साथ) ना (नहीं) गईआं (गई) ।",
                "english_gloss": "main (I) bhull (erred) gaeeaan (in that) tere (with you) naal (along) na (not) gaeeaan (departed) ."
            },
            {
                "original": "तेरे इश्क दी सार वे मैं ना जाणां, इह सिर आया ए मेरा हेठ वदाणां,",
                "hindi_gloss": "तेरे (तेरे) इश्क (प्रेम) दी (की) सार (गहराई/मर्म) वे (हे प्रिय) मैं (मैं) ना (नहीं) जाणां (जानती थी), इह (यह) सिर (सिर) आया (आ गया) ए (है) मेरा (मेरा) हेठ (नीचे) वदाणां (निहाई/हथौड़ों के),",
                "english_gloss": "tere (your) ishq (of love) dee (of) saar (depth/mystery) ve (O) main (I) na (not) jaanaan (knew), eh (this) sir (head) aaya (has come) e (is) mera (my) heth (beneath) vadaanaan (the anvil/hammers),"
            },
            {
                "original": "सट्ट पई इश्के दी तां कूकां दईआं ।",
                "hindi_gloss": "सट्ट (चोट) पई (पड़ी) इश्के (इश्क) दी (की) तां (तब) कूकां (चीखें/पुकार) दईआं (निकल पड़ीं) ।",
                "english_gloss": "satt (blow) pai (fell) ishqe (of love) dee (of) taan (then) kookaan (cries of yearning) daeeaan (burst forth) ."
            },
            {
                "original": "एस इश्क दे कोलों सानूं हटक ना माए, लाहू (लाहौर) जांदड़े बेड़े मोड़ कौन हटाए,",
                "hindi_gloss": "एस (इस) इश्क (इश्क) दे (के मार्ग) कोलों (से) सानूं (मुझे) हटक (मत रोक) ना (न) माए (हे मेरी मां), लाहू (लाहौर की ओर) जांदड़े (जाती हुई) बेड़े (नावों को) मोड़ (मोड़कर) कौन (कौन) हटाए (हटा सकता है),",
                "english_gloss": "es (this) ishq (love) de (from) kolon (from) saanoon (me) hatak (restrain) na (not) maaye (O mother), laahoo (to Lahore) jaandde (heading) bede (vessels/boats) mod (turning back) kaun (who) hataaye (can stop),"
            },
            {
                "original": "मेरी अकल भुल्ली नाल मुहाणिआँ दे गईआं ।",
                "hindi_gloss": "मेरी (मेरी) अकल (सांसारिक बुद्धि) भुल्ली (भूल गई) नाल (साथ) मुहाणिआँ (प्रेम के मल्लाहों) दे (के) गईआं (चली गई) ।",
                "english_gloss": "meri (my) akal (intellect) bhulli (forgotten/erred) naal (with) muhaaniyaan (boatmen) de (of) gaeeaan (departed) ."
            },
            {
                "original": "एस इश्क दी झंगी विच मोर बुलेंदा, सानूं काबा ते किबला प्यारा यार दसेंदा,",
                "hindi_gloss": "एस (इस) इश्क (इश्क) दी (की) झंगी (घने कुंज-वन) विच (में) मोर (दिव्य मोर) बुलेंदा (कूकता है), सानूं (हमें तो) काबा (काबा) ते (और) किबला (किबला) प्यारा (प्यारा) यार (प्रियतम ही) दसेंदा (दिखाई देता है),",
                "english_gloss": "es (this) ishq (of love) dee (of) jhangi (dense grove) vich (in) mor (peacock) bulenda (calls), saanoon (to us) kaaba (Kaaba) te (and) qibla (Qibla) pyaara (beloved) yaar (friend/Lord) dasenda (appears),"
            },
            {
                "original": "सानूं घायल करके फिर ख़बर ना लईआ ।",
                "hindi_gloss": "सानूं (हमें) घायल (प्रेम-बाण से घायल) करके (करके) फिर (फिर) ख़बर (सुध) ना (नहीं) लईआ (ली) ।",
                "english_gloss": "saanoon (unto us) ghaayal (wounded) karke (having made) phir (again) khabar (news/care) na (not) laeea (took) ."
            },
            {
                "original": "बुल्ल्हा शाह इनायत दे बह बूहे, जिस पहनाए सानूं सावे सूहे,",
                "hindi_gloss": "बुल्ल्हा (बुल्ला) शाह (शाह) इनायत (इनायत) दे (के) बह (बैठ गया) बूहे (दरवाजे पर), जिस (जिन्होंने) पहनाए (पहना दिए) सानूं (हमें) सावे (हरे) सूहे (और गहरे लाल सुहाग-वस्त्र),",
                "english_gloss": "bullha (Bulleh) shah (Shah) inaayat (Inayat) de (of) bah (seated) boohe (at the threshold), jis (who) pahnaaye (adorned/clothed) saanoon (unto us) saave (green) soohe (crimson bridal robes),"
            },
            {
                "original": "जां मैं मारी उडारी मिल पिआ वहीआ ।",
                "hindi_gloss": "जां (जैसे ही) मैं (मैंने) मारी (लगाई) उडारी (उड़ान) मिल (मिल) पिआ (गया) वहीआ (वही प्रियतम/परमात्मा) ।",
                "english_gloss": "jaan (as soon as) main (I) maari (took) udaari (spiritual flight) mil (met/united) pia (was found) vaheea (the very same Beloved) ."
            }
        ],
        "hindi_meaning": k14_hi,
        "english_meaning": k14_en
    }]
})

# ==========================================
# KAFI 15
# ==========================================
k15_orig = """बंसी वालिआ चाका रांझा, तेरा सुर है सभ नाल सांझा,
तेरियां मौजां साडा मांझा, साडी सुर तैं आप मिलाई ।
बंसी काहन अचरज बजाई ।

बंसी वालिआ काहन कहावें, सब दा नेक अनूप मनावें,
अक्खियां दे विच नज़र ना आवें, कैसी बिखड़ी खेल रचाई ।
बंसी काहन अचरज बजाई ।

बंसी सभ कोई सुने सुणावे, अरथ इस दा कोई विरला पावे,
जो कोई अनहद की सुर पावे, सो इस बंसी का शौदाई ।
बंसी काहन अचरज बजाई ।

सुणीआं बंसी दियां घंगोरां, कूकां तन मन वांङू मोरां,
डिठियां इस दियां तोड़ां जोड़ां, इक सुर दी सभ कला उठाई ।
बंसी काहन अचरज बजाई ।

इस बंसी दा लंमा लेखा, जिस ने ढूंडा तिस ने देखा,
शादी इस बंसी दी रेखा, एस वजूदों सिफत उठाई ।
बंसी काहन अचरज बजाई ।

इस बंसी दे पंज सत तारे, आप आपनी सुर भरदे सारे,
इक सुर सभ दे विच दम मारे, साडी इस ने होश भुलाई ।
बंसी काहन अचरज बजाई ।

बुल्ल्हा पुज्ज पए तकरार, बूहे आण खलोते यार,
रक्खीं कलमे नाल ब्योपार, तेरी हज़रत भरे गवाही ।
बंसी काहन अचरज बजाई ।"""

k15_hi = """हे बांसुरी बजाने वाले कान्हा रांझा!
तेरी मुरली का स्वर सबके लिए एक समान और साझा है!
तेरी मौजों में ही हमारे जीवन का किनारा और बहाव है,
तूने हमारी धुन को अपनी दिव्य धुन में स्वयं मिला लिया है!
कान्हा ने कैसी अद्भुत और विस्मयकारी बांसुरी बजाई है!

तू बांसुरी वाला कान्हा कहलाता है,
सभी के कल्याण और मंगल की कामना करता है!
पर इन चर्म-चक्षुओं से तू दिखाई नहीं देता,
कैसा दुर्गम और रहस्यमयी खेल तूने रचाया है!
कान्हा ने कैसी अद्भुत और विस्मयकारी बांसुरी बजाई है!

इस बांसुरी की धुन हर कोई सुनता और सुनाता है,
पर इसका वास्तविक आध्यात्मिक अर्थ कोई विरला ही पाता है!
जो इस अनाहत नाद के स्वर को पहचान लेता है,
वही इस बंसी का सच्चा दीवाना और प्रेमी बन जाता है!
कान्हा ने कैसी अद्भुत और विस्मयकारी बांसुरी बजाई है!

जब बांसुरी की गंभीर झंकारें कानों में पड़ीं,
तो मेरा तन-मन मोर की तरह विरह में कूक उठा!
जब इसके राग-रागिनियों के जोड़ और तोड़ देखे,
तो समझ आया कि एक ही स्वर से यह सारा ब्रह्मांड रचा गया है!
कान्हा ने कैसी अद्भुत और विस्मयकारी बांसुरी बजाई है!

इस बांसुरी का इतिहास और रहस्य अत्यंत गहरा है,
जिसने सच्चे मन से खोजा उसी ने इसके दीदार किए!
यह बांसुरी आत्मा के आनंद और परम-मिलन की रेखा है,
जिसने इस नश्वर शरीर से दिव्य महिमा प्रकट कर दी!
कान्हा ने कैसी अद्भुत और विस्मयकारी बांसुरी बजाई है!

इस बंसी में पांच और सात स्वर-तत्व समाए हैं,
सभी अपनी-अपनी रागिनी में झंकृत हो रहे हैं!
पर उन सब में केवल एक ही प्राण-स्वर गूंज रहा है,
जिसने हमारी सांसारिक सुध-बुध पूरी तरह भुला दी है!
कान्हा ने कैसी अद्भुत और विस्मयकारी बांसुरी बजाई है!

बुल्ले शाह के सारे तर्क और विवाद अब समाप्त हो गए,
जब साक्षात प्रियतम द्वार पर आकर खड़े हो गए!
उस एक दिव्य कलमे से ही अपना आत्मिक व्यापार बनाए रखना,
तेरी भक्ति की गवाही स्वयं तेरा परमात्मा भरेगा!
कान्हा ने कैसी अद्भुत और विस्मयकारी बांसुरी बजाई है!"""

k15_en = """O cowherd Ranjha, divine Flutist dear!
The sweet melody of Thy flute belongs equally to all!
In the flow of Thy waves does our life's current steer,
Thou Thyself hast tuned our spirit to Thy celestial call!
What a wondrous and mystical flute has Krishna played!

Thou art known as the Flute-bearer Krishna,
Willing good and radiant grace unto all creation!
Yet Thou remainest invisible to these mortal eyes,
What an intricate, elusive game hast Thou displayed!
What a wondrous and mystical flute has Krishna played!

Everyone hears and repeats the notes of this flute,
Yet rare is the soul who grasps its hidden truth!
Whoever perceives the unstruck resonance within,
Becomes an ecstatic devotee of this heavenly flute!
What a wondrous and mystical flute has Krishna played!

When the resounding echoes of the flute reached my ear,
My body and soul cried out like peacocks in yearning!
Observing its rhythmic transitions and harmonies clear,
I saw all manifest creation rising from that one turning!
What a wondrous and mystical flute has Krishna played!

Vast and unfathomed is the account of this flute,
Whoever truly sought, beheld its divine light!
Auspicious is the grace carved by this flute,
Awakening celestial glory from mortal plight!
What a wondrous and mystical flute has Krishna played!

The five and seven subtle strings of this flute,
Vibrate in their respective tones and pitch!
Yet a single breath animates all that is mute,
Wiping away our earthly wits with ecstasy rich!
What a wondrous and mystical flute has Krishna played!

All disputes and arguments have ceased for Bulleh,
As the Divine Beloved arrived at his door!
Keep thy commerce solely with the sacred Word,
Thy Master Himself shall bear witness evermore!
What a wondrous and mystical flute has Krishna played!"""

batch.append({
    "id": 15,
    "title": "15. बंसी काहन अचरज बजाई",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k15_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "बंसी वालिआ चाका रांझा, तेरा सुर है सभ नाल सांझा,",
                "hindi_gloss": "बंसी (बांसुरी) वालिआ (वाले) चाका (ग्वाले/सेवक) रांझा (रांझा), तेरा (तुम्हारा) सुर (स्वर/संगीत) है (है) सभ (सबके) नाल (साथ) सांझा (साझा/समान),",
                "english_gloss": "bansi (flute) waalia (player) chaaka (cowherd) ranjha (Ranjha), tera (your) sur (melody) hai (is) sabh (all) naal (with) saanjha (shared/common),"
            },
            {
                "original": "तेरियां मौजां साडा मांझा, साडी सुर तैं आप मिलाई ।",
                "hindi_gloss": "तेरियां (तुम्हारी) मौजां (आनंद-तरंगों में) साडा (हमारा) मांझा (मांझा/किनारा), साडी (हमारी) सुर (धुन) तैं (तुमने) आप (स्वयं) मिलाई (मिला ली है) ।",
                "english_gloss": "teriyaan (your) maujaan (waves of bliss) saada (our) maanjha (midstream), saadi (our) sur (tune) tain (you) aap (yourself) milaai (harmonized) ."
            },
            {
                "original": "बंसी काहन अचरज बजाई ।",
                "hindi_gloss": "बंसी (बांसुरी) काहन (कान्हा/कृष्ण ने) अचरज (अद्भुत/विस्मयकारी) बजाई (बजाई है) ।",
                "english_gloss": "bansi (flute) kaahan (Krishna) achraj (wondrous) bajaai (has played) ."
            },
            {
                "original": "बंसी वालिआ काहन कहावें, सब दा नेक अनूप मनावें,",
                "hindi_gloss": "बंसी (बांसुरी) वालिआ (वाला) काहन (कान्हा) कहावें (कहलाते हो), सब (सबका) दा (का) नेक (कल्याण) अनूप (अनोखा/सुंदर) मनावें (चाहते/मनाते हो),",
                "english_gloss": "bansi (flute) waalia (bearer) kaahan (Krishna) kahaaven (are called), sab (of all) da (of) nek (good/welfare) anoop (matchless) manaaven (celebrate/seek),"
            },
            {
                "original": "अक्खियां दे विच नज़र ना आवें, कैसी बिखड़ी खेल रचाई ।",
                "hindi_gloss": "अक्खियां (आंखों) दे (के) विच (बीच) नज़र (दिखाई) ना (नहीं) आवें (आते), कैसी (कैसा) बिखड़ी (कठिन/दुर्गम) खेल (खेल) रचाई (रचाया है) ।",
                "english_gloss": "akkhiyaan (eyes) de (of) vich (in) nazar (sight) na (not) aaven (appear), kaisi (what an) bikhdi (intricate/difficult) khel (game) rachaai (have staged) ."
            },
            {
                "original": "बंसी सभ कोई सुने सुणावे, अरथ इस दा कोई विरला पावे,",
                "hindi_gloss": "बंसी (बांसुरी) सभ (सब) कोई (कोई) सुने (सुनता है) सुणावे (और सुनाता है), अरथ (गहरा अर्थ) इस (इसका) दा (का) कोई (कोई) विरला (विरला साधक ही) पावे (पाता है),",
                "english_gloss": "bansi (flute) sabh (every) koi (one) sune (hears) sunaave (recounts), arath (meaning) is (its) da (of) koi (any) virla (rare one) paave (comprehends),"
            },
            {
                "original": "जो कोई अनहद की सुर पावे, सो इस बंसी का शौदाई ।",
                "hindi_gloss": "जो (जो) कोई (कोई) अनहद (अनाहत नाद) की (का) सुर (स्वर) पावे (पा लेता है), सो (वही) इस (इस) बंसी (बांसुरी) का (का) शौदाई (दीवाना/प्रेमी है) ।",
                "english_gloss": "jo (who) koi (ever) anhad (unstruck) kee (of) sur (resonance) paave (attains), so (he alone) is (this) bansi (flute) ka (of) shaudaai (intoxicated lover) ."
            },
            {
                "original": "सुणीआं बंसी दियां घंगोरां, कूकां तन मन वांङू मोरां,",
                "hindi_gloss": "सुणीआं (सुनीं जब) बंसी (बांसुरी) दियां (की) घंगोरां (गंभीर झंकारें), कूकां (कूक उठा) तन (तन) मन (मन) वांङू (की तरह) मोरां (मोरो की),",
                "english_gloss": "suniyaan (heard) bansi (flute) diyaan (of) ghangoraan (resounding chords), kookaan (cries out) tan (body) man (mind) vaangoo (like) moraan (peacocks),"
            },
            {
                "original": "डिठियां इस दियां तोड़ां जोड़ां, इक सुर दी सभ कला उठाई ।",
                "hindi_gloss": "डिठियां (देखे जब) इस (इसके) दियां (के) तोड़ां (राग-रागिनियों के तोड़) जोड़ां (और जोड़), इक (एक ही) सुर (स्वर) दी (की) सभ (सारी) कला (लीला/सृष्टि) उठाई (प्रकट की है) ।",
                "english_gloss": "dithiyaan (beheld) is (its) diyaan (of) todaan (melodic cadences) jodaan (harmonies), ik (one) sur (note) dee (of) sabh (all) kala (creation/manifestation) uthaai (raised) ."
            },
            {
                "original": "इस बंसी दा लंमा लेखा, जिस ने ढूंडा तिस ने देखा,",
                "hindi_gloss": "इस (इस) बंसी (बांसुरी) दा (का) लंमा (अथाह/लंबा) लेखा (रहस्य/हिसाब है), जिस (जिसने) ने (ने) ढूंडा (खोजा) तिस (उसी) ने (ने) देखा (दीदार किया),",
                "english_gloss": "is (this) bansi (flute) da (of) lanma (vast/deep) lekha (account), jis (whoever) ne (by) dhoonda (sought) tis (he) ne (by) dekha (beheld),"
            },
            {
                "original": "शादी इस बंसी दी रेखा, एस वजूदों सिफत उठाई ।",
                "hindi_gloss": "शादी (परमानंद/मिलन) इस (इस) बंसी (बांसुरी) दी (की) रेखा (भाग्य-रेखा है), एस (इस नश्वर) वजूदों (अस्तित्व से) सिफत (दिव्य महिमा) उठाई (प्रकट कर दी) ।",
                "english_gloss": "shaadi (blissful union) is (this) bansi (flute) dee (of) rekha (destiny/line), es (this mortal) vajoodon (body/existence) sifat (divine praise) uthaai (raised) ."
            },
            {
                "original": "इस बंसी दे पंज सत तारे, आप आपनी सुर भरदे सारे,",
                "hindi_gloss": "इस (इस) बंसी (बांसुरी) दे (के) पंज (पांच) सत (और सात) तारे (सुर-तत्व), आप (अपनी) आपनी (अपनी) सुर (रागिनी) भरदे (भरते हैं) सारे (सभी),",
                "english_gloss": "is (this) bansi (flute) de (of) panj (five) sat (seven) taare (subtle strings/notes), aap (their) aapni (own) sur (tones) bharde (fill) saare (all),"
            },
            {
                "original": "इक सुर सभ दे विच दम मारे, साडी इस ने होश भुलाई ।",
                "hindi_gloss": "इक (एक ही) सुर (प्राण-स्वर) सभ (सब) दे (के) विच (भीतर) दम (श्वास) मारे (भरता है), साडी (हमारी) इस (इसने) ने (ने) होश (सांसारिक होश) भुलाई (भुला दी है) ।",
                "english_gloss": "ik (one) sur (breath/melody) sabh (all) de (of) vich (within) dam (breath) maare (blows), saadi (our) is (this) ne (by) hosh (consciousness) bhulaai (obliterated) ."
            },
            {
                "original": "बुल्ल्हा पुज्ज पए तकरार, बूहे आण खलोते यार,",
                "hindi_gloss": "बुल्ल्हा (हे बुल्ले) पुज्ज (समाप्त हो) पए (गए) तकरार (सारे विवाद), बूहे (द्वार पर) आण (आकर) खलोते (खड़े हो गए) यार (प्रियतम),",
                "english_gloss": "bullha (O Bulleh) pujj (exhausted/ceased) paye (have) takraar (disputes), boohe (at the door) aan (coming) khalote (stood) yaar (the Beloved),"
            },
            {
                "original": "रक्खीं कलमे नाल ब्योपार, तेरी हज़रत भरे गवाही ।",
                "hindi_gloss": "रक्खीं (रखना) कलमे (सत्य के कलमे) नाल (साथ) ब्योपार (आत्मिक व्यापार), तेरी (तेरी भक्ति की) हज़रत (प्रभु/रसूल) भरे (भरेंगे) गवाही (साक्षी) ।",
                "english_gloss": "rakkheen (keep) kalme (divine Word) naal (with) byopaar (commerce/devotion), teri (your) hazrat (the Divine Presence) bhare (shall bear) gawaahi (testimony) ."
            }
        ],
        "hindi_meaning": k15_hi,
        "english_meaning": k15_en
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
