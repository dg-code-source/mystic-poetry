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
# KAFI 16: 16. बस्स कर जी हुण बस्स कर जी
# ==========================================
k16_orig = """बस्स कर जी हुण बस्स कर जी,
इक बात असां नाल हस्स कर जी ।

तुसीं दिल मेरे विच वस्सदे हो, ऐवें साथों दूर क्यों नस्सदे हो,
नाले घत्त जादू दिल खस्सदे हो, हुण कित वल्ल जासो नस्स कर जी ।
बस्स कर जी हुण बस्स कर जी ।

तुसीं मोयां नूं मार ना मुक्कदे सी, खिद्दो वांङ खूंडी नित्त कुट्टदे सी,
गल्ल करदियां दा गल घुट्टदे सी, हुण तीर लगायो कस्स कर जी ।
बस्स कर जी हुण बस्स कर जी ।

तुसीं छपदे हो असां पकड़े हो, असां नाल ज़ुल्फ़ दे जकड़े हो,
तुसीं अजे छपन नूं तकड़े हो, हुण जाण ना मिलदा नस्स कर जी ।
बस्स कर जी हुण बस्स कर जी ।

बुल्ल्हा शौह मैं तेरी बरदी हां, तेरा मुक्ख वेखण नूं मरदी हां,
नित्त सौ सौ मिन्नतां करदी हां, हुण बैठ पिंजर विच धस्स कर जी ।
बस्स कर जी हुण बस्स कर जी ।"""

k16_hi = """बस करो जी, अब बस करो जी!  
हमसे एक बात ज़रा हँसकर करो जी!  

तुम तो मेरे ही हृदय में बसते हो,  
फिर यूँ ही हमसे दूर क्यों भागते हो?  
जादू डालकर दिल लूट लेते हो,  
अब भागकर किस ओर जाओगे जी?  
बस करो जी, अब बस करो जी!  

हम तो पहले ही अधमरे थे, फिर भी मारते रहे,  
गेंद की तरह छड़ी से रोज़ उछालते रहे!  
बात करते हुए का गला घोंटते रहे,  
अब कमान खींचकर तीर मार दिया जी!  
बस करो जी, अब बस करो जी!  

तुम छिपते रहे, पर हमने तुम्हें पकड़ लिया,  
प्रेम की ज़ुल्फ़ों की जंजीर में जकड़ लिया!  
तुम अब भी छिपने की ताक में हो,  
पर अब भागकर जाना मुमकिन नहीं जी!  
बस करो जी, अब बस करो जी!  

हे प्रभु! बुल्ला तो तुम्हारी दासी है,  
तुम्हारा पावन मुख देखने को प्यासी है!  
नित्य सौ-सौ मिन्नतें और प्रार्थनाएँ करती हूँ,  
अब इस सीने के पिंजरे में समाकर बैठ जाओ जी!  
बस करो जी, अब बस करो जी!"""

k16_en = """Enough, my Beloved! Now pray, call a cease!  
Speak just one tender word to me in smiling peace!  

Within the chambers of my heart You reside,  
Why then do You flee needlessly from my side?  
Casting sweet enchantments, my heart You have stolen away,  
Where will You run now, escaping my stay?  
Enough, my Beloved! Now pray, call a cease!  

We were already dead in love, yet You spared no blow,  
Tossing us like a ball with a crooked cane to and fro!  
Throttling the voice whenever we sought to speak,  
Now You have drawn the bow taut, piercing the weak!  
Enough, my Beloved! Now pray, call a cease!  

You tried to hide, but we have caught You fast,  
Bound tightly in the tresses of love at last!  
Though You are still bent upon slipping away,  
No flight shall avail You—here You must stay!  
Enough, my Beloved! Now pray, call a cease!  

O Lord, says Bulleh, I am Thy humble maid,  
Pining to behold Thy divine face displayed!  
A hundred entreaties I offer night and day,  
Come dwell in the cage of my heart, and never stray!  
Enough, my Beloved! Now pray, call a cease!"""

batch.append({
    "id": 16,
    "title": "16. बस्स कर जी हुण बस्स कर जी",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k16_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "बस्स कर जी हुण बस्स कर जी,",
                "hindi_gloss": "बस्स (बस/पर्याप्त) कर (करो) जी (हे प्रियतम) हुण (अब) बस्स (बस) कर (करो) जी (जी),",
                "english_gloss": "bass (enough) kar (do/stop) jee (O Beloved) hun (now) bass (enough) kar (stop) jee (please),"
            },
            {
                "original": "इक बात असां नाल हस्स कर जी ।",
                "hindi_gloss": "इक (एक) बात (बात) असां (हमारे) नाल (साथ) हस्स (हँस) कर (करके) जी (कीजिए) ।",
                "english_gloss": "ik (one) baat (word/talk) asaan (us) naal (with) hass (smiling) kar (do) jee (please) ."
            },
            {
                "original": "तुसीं दिल मेरे विच वस्सदे हो, ऐवें साथों दूर क्यों नस्सदे हो,",
                "hindi_gloss": "तुसीं (आप) दिल (हृदय) मेरे (मेरे) विच (भीतर) वस्सदे (बसते) हो (हो), ऐवें (व्यर्थ ही) साथों (हमसे) दूर (दूर) क्यों (क्यों) नस्सदे (भागते) हो (हो),",
                "english_gloss": "tuseen (you) dil (heart) mere (my) vich (in) vassde (reside) ho (do), aiven (needlessly) saathon (from us) door (far) kyon (why) nassde (run away) ho (do),"
            },
            {
                "original": "नाले घत्त जादू दिल खस्सदे हो, हुण कित वल्ल जासो नस्स कर जी ।",
                "hindi_gloss": "नाले (और) घत्त (डालकर) जादू (जादू) दिल (दिल) खस्सदे (छीन लेते) हो (हो), हुण (अब) कित (किस) वल्ल (ओर) जासो (जाओगे) नस्स (भाग) कर (कर) जी (हे प्रिय) ।",
                "english_gloss": "naale (moreover) ghatt (casting) jaadoo (magic) dil (heart) khassde (snatch/steal) ho (do), hun (now) kit (which) vall (direction) jaaso (will you go) nass (fleeing) kar (having done) jee (O Beloved) ."
            },
            {
                "original": "बस्स कर जी हुण बस्स कर जी ।",
                "hindi_gloss": "बस्स (बस) कर (करो) जी (जी) हुण (अब) बस्स (बस) कर (करो) जी (जी) ।",
                "english_gloss": "bass (enough) kar (stop) jee (O Lord) hun (now) bass (enough) kar (stop) jee (please) ."
            },
            {
                "original": "तुसीं मोयां नूं मार ना मुक्कदे सी, खिद्दो वांङ खूंडी नित्त कुट्टदे सी,",
                "hindi_gloss": "तुसीं (आप) मोयां (मुर्दों/अधमरों) नूं (को) मार (मारने से) ना (नहीं) मुक्कदे (थकते/रुकते) सी (थे), खिद्दो (गेंद) वांङ (की भांति) खूंडी (छड़ी/हॉकी से) नित्त (सदा) कुट्टदे (पीटते/उछालते) सी (थे),",
                "english_gloss": "tuseen (you) moyaan (the already dead) noon (unto) maar (striking) na (not) mukkde (ceased) see (were), khiddo (cloth ball) vaang (like) khoondi (crooked stick) nitt (daily) kuttde (beat/toss) see (were),"
            },
            {
                "original": "गल्ल करदियां दा गल घुट्टदे सी, हुण तीर लगायो कस्स कर जी ।",
                "hindi_gloss": "गल्ल (बात) करदियां (करने वालों) दा (का) गल (गला) घुट्टदे (घोंटते) सी (थे), हुण (अब) तीर (तीर) लगायो (खींच कर मारा है) कस्स (कस) कर (कर) जी (जी) ।",
                "english_gloss": "gall (talk) kardiyaan (of those who speak) da (of) gal (throat) ghuttde (throttled) see (were), hun (now) teer (arrow) lagaayo (have struck) kass (tautly) kar (having pulled) jee (O Lord) ."
            },
            {
                "original": "बस्स कर जी हुण बस्स कर जी ।",
                "hindi_gloss": "बस्स (बस) कर (करो) जी (जी) हुण (अब) बस्स (बस) कर (करो) जी (जी) ।",
                "english_gloss": "bass (enough) kar (stop) jee (O Lord) hun (now) bass (enough) kar (stop) jee (please) ."
            },
            {
                "original": "तुसीं छपदे हो असां पकड़े हो, असां नाल ज़ुल्फ़ दे जकड़े हो,",
                "hindi_gloss": "तुसीं (आप) छपदे (छिपते) हो (हो) असां (हमने) पकड़े (पकड़ लिया) हो (है), असां (हमने) नाल (साथ) ज़ुल्फ़ (अपनी भक्ति/प्रेम की ज़ुल्फ़ों) दे (से) जकड़े (जकड़ लिया) हो (है),",
                "english_gloss": "tuseen (you) chhapde (hide) ho (do) asaan (we) pakde (caught) ho (have), asaan (we) naal (with) zulf (tresses of love) de (of) jakde (bound tightly) ho (have),"
            },
            {
                "original": "तुसीं अजे छपन नूं तकड़े हो, हुण जाण ना मिलदा नस्स कर जी ।",
                "hindi_gloss": "तुसीं (आप) अजे (अभी भी) छपन (छिपने) नूं (के लिए) तकड़े (मज़बूत/उतारू) हो (हो), हुण (अब) जाण (जाने) ना (नहीं) मिलदा (मिलेगा) नस्स (भाग) कर (कर) जी (जी) ।",
                "english_gloss": "tuseen (you) aje (still) chhapan (to hide) noon (for) takde (eager/strong) ho (are), hun (now) jaan (to leave) na (not) milda (shall be allowed) nass (running away) kar (having done) jee (please) ."
            },
            {
                "original": "बस्स कर जी हुण बस्स कर जी ।",
                "hindi_gloss": "बस्स (बस) कर (करो) जी (जी) हुण (अब) बस्स (बस) कर (करो) जी (जी) ।",
                "english_gloss": "bass (enough) kar (stop) jee (O Lord) hun (now) bass (enough) kar (stop) jee (please) ."
            },
            {
                "original": "बुल्ल्हा शौह मैं तेरी बरदी हां, तेरा मुक्ख वेखण नूं मरदी हां,",
                "hindi_gloss": "बुल्ल्हा (बुल्ले शाह कहते हैं) शौह (हे स्वामी) मैं (मैं) तेरी (तेरी) बरदी (दासी/सेविका) हां (हूँ), तेरा (तेरा) मुक्ख (मुखड़ा) वेखण (देखने) नूं (के लिए) मरदी (मरती/तरसती) हां (हूँ),",
                "english_gloss": "bullha (Bulleh) shauh (O Lord) main (I) teri (your) bardi (handmaiden/servant) haan (am), tera (your) mukkh (countenance/face) vekhan (to behold) noon (for) mardi (die/yearn) haan (am),"
            },
            {
                "original": "नित्त सौ सौ मिन्नतां करदी हां, हुण बैठ पिंजर विच धस्स कर जी ।",
                "hindi_gloss": "नित्त (प्रतिदिन) सौ (सौ) सौ (सौ) मिन्नतां (प्रार्थनाएँ/विनतियाँ) करदी (करती) हां (हूँ), हुण (अब) बैठ (बैठ जाओ) पिंजर (हृदय रूपी पिंजरे) विच (भीतर) धस्स (समा) कर (कर) जी (हे प्रिय) ।",
                "english_gloss": "nitt (daily) sau (hundred) sau (hundred) minnataan (entreaties) kardi (make) haan (do), hun (now) baith (sit down) pinjar (cage of my ribcage/heart) vich (within) dhass (entering deeply) kar (having done) jee (O Beloved) ."
            },
            {
                "original": "बस्स कर जी हुण बस्स कर जी ।",
                "hindi_gloss": "बस्स (बस) कर (करो) जी (जी) हुण (अब) बस्स (बस) कर (करो) जी (जी) ।",
                "english_gloss": "bass (enough) kar (stop) jee (O Lord) hun (now) bass (enough) kar (stop) jee (please) ."
            }
        ],
        "hindi_meaning": k16_hi,
        "english_meaning": k16_en
    }]
})

# ==========================================
# KAFI 17: 17. बेहद्द रमज़ां दसदा नीं, ढोलण माही
# ==========================================
k17_orig = """बेहद्द रमज़ां दसदा नीं, ढोलण माही ।
मीम दे उहले वस्सदा नीं, ढोलण माही ।

औलियां मनसूर कहावे, रमज़ अनलहक्क आप बतावे,
आपे आप नूं सूली चढ़ावे,ते कोल खलोके हस्सदा नीं, ढोलण माही ।

बेहद्द रमज़ां दसदा नीं, ढोलण माही ।
मीम दे उहले वस्सदा नीं, ढोलण माही ।"""

k17_hi = """अरी सखी! मेरा प्रियतम माही अनंत रहस्य प्रकट करता है!  
वह 'मीम' के सूक्ष्म परदे की ओट में वास करता है!  

संतों-फ़कीरों में वही मंसूर बन जाता है,  
'अनलहक़' (मैं ही सत्य हूँ) का दिव्य रहस्य स्वयं समझाता है!  
अपने-आप को ही सूली पर चढ़ा देता है,  
और फिर निकट ही खड़ा होकर मंद-मंद मुस्कुराता है!  

अरी सखी! मेरा प्रियतम माही अनंत रहस्य प्रकट करता है!  
वह 'मीम' के सूक्ष्म परदे की ओट में वास करता है!"""

k17_en = """O dear friend, infinite mysteries does my Beloved unfold!  
Behind the subtle veil of 'Meem' dwells my Master untold!  

Among the saints, as Mansur Hallaj He proclaims His grace,  
Revealing Himself the divine mystery of 'Anal Haq' in that place!  
He ascends the gallows upon His own command,  
And smilingly observes the spectacle close at hand!  

O dear friend, infinite mysteries does my Beloved unfold!  
Behind the subtle veil of 'Meem' dwells my Master untold!"""

batch.append({
    "id": 17,
    "title": "17. बेहद्द रमज़ां दसदा नीं, ढोलण माही",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k17_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "बेहद्द रमज़ां दसदा नीं, ढोलण माही ।",
                "hindi_gloss": "बेहद्द (असीम/अनंत) रमज़ां (गूढ़ रहस्य) दसदा (बताता/दिखाता है) नीं (अरी सखी), ढोलण (प्रियतम) माही (माहिवाल/ईश्वर) ।",
                "english_gloss": "behadd (boundless) ramzaan (mysteries/secrets) dasda (reveals) neen (O friend), dholan (Beloved) maahi (Sweetheart/Lord) ."
            },
            {
                "original": "मीम दे उहले वस्सदा नीं, ढोलण माही ।",
                "hindi_gloss": "मीम (अक्षर 'मीम' अर्थात् मुहम्मद) दे (के) उहले (ओट/परदे के पीछे) वस्सदा (बसता है) नीं (अरी सखी), ढोलण (प्रियतम) माही (माहिवाल/प्रभु) ।",
                "english_gloss": "meem (the letter 'M') de (of) uhle (veil/behind) vassda (resides) neen (O friend), dholan (Beloved) maahi (Lord) ."
            },
            {
                "original": "औलियां मनसूर कहावे, रमज़ अनलहक्क आप बतावे,",
                "hindi_gloss": "औलियां (सूफ़ियों में) मनसूर (मंसूर हल्लाज) कहावे (कहलाता है), रमज़ (रहस्य) अनलहक्क ('अहं ब्रह्मास्मि' / मैं ही सत्य हूँ) आप (स्वयं) बतावे (सिखाता है),",
                "english_gloss": "auliyaan (among saints) mansoor (Mansur Hallaj) kahaave (calls himself), ramz (mystery) analhaqq ('I am the Truth') aap (himself) bataave (reveals),"
            },
            {
                "original": "आपे आप नूं सूली चढ़ावे,ते कोल खलोके हस्सदा नीं, ढोलण माही ।",
                "hindi_gloss": "आपे (स्वयं ही) आप (अपने-आप) नूं (को) सूली (सूली पर) चढ़ावे (चढ़ाता है), ते (और) कोल (पास) खलोके (खड़े होकर) हस्सदा (हँसता है) नीं (अरी सखी), ढोलण (प्रियतम) माही (प्रभु) ।",
                "english_gloss": "aape (himself) aap (himself) noon (unto) sooli (gallows) chadhaave (raises), te (and) kol (nearby) khaloke (standing) hassda (smiles/laughs) neen (O friend), dholan (Beloved) maahi (Lord) ."
            },
            {
                "original": "बेहद्द रमज़ां दसदा नीं, ढोलण माही ।",
                "hindi_gloss": "बेहद्द (असीम) रमज़ां (गूढ़ रहस्य) दसदा (प्रकट करता है) नीं (अरी सखी), ढोलण (प्रियतम) माही (प्रभु) ।",
                "english_gloss": "behadd (boundless) ramzaan (secrets) dasda (reveals) neen (O friend), dholan (Beloved) maahi (Lord) ."
            },
            {
                "original": "मीम दे उहले वस्सदा नीं, ढोलण माही ।",
                "hindi_gloss": "मीम (अक्षर 'मीम') दे (के) उहले (परदे में) वस्सदा (रहता है) नीं (अरी सखी), ढोलण (प्रियतम) माही (प्रभु) ।",
                "english_gloss": "meem (letter 'M') de (of) uhle (veil) vassda (dwells) neen (O friend), dholan (Beloved) maahi (Lord) ."
            }
        ],
        "hindi_meaning": k17_hi,
        "english_meaning": k17_en
    }]
})

# ==========================================
# KAFI 18: 18. भैणां मैं कत्तदी कत्तदी हुट्टी
# ==========================================
k18_orig = """पिड़ी पिछे पछवाड़े रह गई, हत्थ विच रह गई जुट्टी,
अग्गे चरखा पिच्छे पीहड़ा, मेरे हत्थों तन्द तरुट्टी,
भैणां मैं कत्तदी कत्तदी हुट्टी ।

दाज जवाहर असां की करना, जिस प्रेम कटवाई मुट्ठी,
ओहो चोर मेरा पकड़ मंगायो, जिस मेरी जिन्द कुट्ठी,
भैणां मैं कत्तदी कत्तदी हुट्टी ।

भला होया मेरा चरखा टुट्टा, मेरी जिन्द अज़ाबों छुट्टी,
बुल्ल्हा शौह ने नाच नचाए, ओथे धुंम पई कड़-कुट्टी,
भैणां मैं कत्तदी कत्तदी हुट्टी ।"""

k18_hi = """सखियों की टोली पीछे आँगन में छूट गई, हाथ में केवल सूत की पूणी रह गई,  
आगे चरखा धरा रहा, पीछे पीढ़ी, और मेरे हाथ से जीवन का धागा टूट गया!  
हे बहनों! मैं सांसारिक चरखा कातते-कातते थक कर चूर हो गई!  

अब हमें दहेज़ और हीरों-जवाहरात का क्या करना है,  
जब प्रभु-प्रेम ने सांसारिक लालच की मुट्ठी ही काट दी!  
मेरे उस चित्तचोर प्रीतम को पकड़कर मेरे पास ले आओ,  
जिसने मेरे प्राणों को अपने विरह में घायल कर दिया है!  
हे बहनों! मैं सांसारिक चरखा कातते-कातते थक कर चूर हो गई!  

बड़ा भला हुआ कि मेरा यह नश्वर चरखा टूट गया,  
मेरी आत्मा दुनियावी जंजाल और यातना से सदा के लिए छूट गई!  
बुल्ले शाह कहते हैं—जब प्रियतम ने अपने दिव्य प्रेम का नाच नचाया,  
तो अहंकार की सारी दीवारें टूटकर चारों ओर प्रेम की धूम मच गई!  
हे बहनों! मैं सांसारिक चरखा कातते-कातते थक कर चूर हो गई!"""

k18_en = """The maidens' spinning circle was left behind in the yard,  
In my trembling hands only the raw spool remained!  
Before me stood the wheel, behind me the wooden seat,  
And the fragile thread snapped from my hands unfeigned!  
O sisters, I am utterly weary and exhausted of spinning!  

What have we to do now with dowries and shining gems,  
When the sword of divine love has severed earthly greed?  
Go capture and bring before me that thief of my soul,  
Whose intoxicating love has made my spirit bleed!  
O sisters, I am utterly weary and exhausted of spinning!  

Blessed be this moment that my spinning wheel has shattered,  
For my soul is liberated from earthly torment and strife!  
Bulleh Shah's Lord has made him dance in divine ecstasy,  
Where worldly pride was crushed, awakening eternal life!  
O sisters, I am utterly weary and exhausted of spinning!"""

batch.append({
    "id": 18,
    "title": "18. भैणां मैं कत्तदी कत्तदी हुट्टी",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k18_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "पिड़ी पिछे पछवाड़े रह गई, हत्थ विच रह गई जुट्टी,",
                "hindi_gloss": "पिड़ी (कताई का घेरा/सखियों की टोली) पिछे (पीछे) पछवाड़े (आँगन के पिछले भाग में) रह (रह) गई (गई), हत्थ (हाथ) विच (में) रह (रह) गई (गई) जुट्टी (सूत की पूणी/लच्छी),",
                "english_gloss": "pidi (spinning circle of maidens) pichhe (behind) pachhwaade (backyard) rah (remained) gayee (did), hatth (hand) vich (in) rah (remained) gayee (did) jutti (hank of raw cotton/spool),"
            },
            {
                "original": "अग्गे चरखा पिच्छे पीहड़ा, मेरे हत्थों तन्द तरुट्टी,",
                "hindi_gloss": "अग्गे (आगे) चरखा (चरखा) पिच्छे (पीछे) पीहड़ा (बैठने की पीढ़ी), मेरे (मेरे) हत्थों (हाथों से) तन्द (सूत का धागा) तरुट्टी (टूट गया),",
                "english_gloss": "agge (in front) charkha (spinning wheel) pichhe (behind) peehda (low wooden seat) mere (my) hatthon (from hands) tand (thread) tarutti (snapped),"
            },
            {
                "original": "भैणां मैं कत्तदी कत्तदी हुट्टी ।",
                "hindi_gloss": "भैणां (हे बहनों/सखियों) मैं (मैं) कत्तदी (सूत कातते) कत्तदी (कातते) हुट्टी (थक कर चूर हो गई) ।",
                "english_gloss": "bhainaan (O sisters) main (I) kattdi (spinning) kattdi (spinning) hutti (exhausted/worn out) ."
            },
            {
                "original": "दाज जवाहर असां की करना, जिस प्रेम कटवाई मुट्ठी,",
                "hindi_gloss": "दाज (दहेज) जवाहर (रत्न और आभूषण) असां (हमें) की (क्या) करना (करना है), जिस (जिस) प्रेम (दिव्य प्रेम ने) कटवाई (कटवा दी/नष्ट कर दी) मुट्ठी (संसार की मुट्ठी/पकड़),",
                "english_gloss": "daaj (dowry) jawaahar (jewels) asaan (we) kee (what) karna (to do with), jis (which) prem (divine love) katvaai (severed/vanquished) mutthi (fist/greed of world),"
            },
            {
                "original": "ओहो चोर मेरा पकड़ मंगायो, जिस मेरी जिन्द कुट्ठी,",
                "hindi_gloss": "ओहो (उसी) चोर (चित्तचोर प्रियतम को) मेरा (मेरे) पकड़ (पकड़ कर) मंगायो (यहाँ बुलवाओ/लाओ), जिस (जिसने) मेरी (मेरी) जिन्द (जान/प्राण) कुट्ठी (घायल/तड़पाई है),",
                "english_gloss": "oho (that very) chor (heart-thief) mera (my) pakad (capturing) mangaayo (summon/bring), jis (who) meri (my) jind (soul/life) kutthi (slaughtered/smitten),"
            },
            {
                "original": "भैणां मैं कत्तदी कत्तदी हुट्टी ।",
                "hindi_gloss": "भैणां (हे बहनों) मैं (मैं) कत्तदी (कातते) कत्तदी (कातते) हुट्टी (थक गई) ।",
                "english_gloss": "bhainaan (O sisters) main (I) kattdi (spinning) kattdi (spinning) hutti (exhausted) ."
            },
            {
                "original": "भला होया मेरा चरखा टुट्टा, मेरी जिन्द अज़ाबों छुट्टी,",
                "hindi_gloss": "भला (अच्छा ही) होया (हुआ) मेरा (मेरा) चरखा (सांसारिक कर्मों का चरखा) टुट्टा (टूट गया), मेरी (मेरी) जिन्द (आत्मा/जीवन) अज़ाबों (यातना और बंधन से) छुट्टी (मुक्त हो गई),",
                "english_gloss": "bhala (well/fortunate) hoya (happened) mera (my) charkha (spinning wheel) tutta (broke), meri (my) jind (soul) azaabon (from torments) chhutti (was freed),"
            },
            {
                "original": "बुल्ल्हा शौह ने नाच नचाए, ओथे धुंम पई कड़-कुट्टी,",
                "hindi_gloss": "बुल्ल्हा (बुल्ले शाह कहते हैं) शौह (परमेश्वर ने) ने (ने) नाच (प्रेम का अलौकिक नृत्य) नचाए (नचाया), ओथे (वहाँ उस दिव्य मिलन में) धुंम (धूम) पई (मच गई) कड़-कुट्टी (अहंकार के चूर्ण-विचूर्ण होने की),",
                "english_gloss": "bullha (Bulleh) shauh (the Lord) ne (by) naach (dance of ecstasy) nachaaye (made to dance), othe (there) dhumm (great tumult/fame) payee (arose) kad-kutti (of the crushing of ego),"
            },
            {
                "original": "भैणां मैं कत्तदी कत्तदी हुट्टी ।",
                "hindi_gloss": "भैणां (हे बहनों) मैं (मैं) कत्तदी (कातते) कत्तदी (कातते) हुट्टी (थक गई) ।",
                "english_gloss": "bhainaan (O sisters) main (I) kattdi (spinning) kattdi (spinning) hutti (exhausted) ."
            }
        ],
        "hindi_meaning": k18_hi,
        "english_meaning": k18_en
    }]
})

# ==========================================
# KAFI 19: 19. भावें जाण ना जाण वे वेहड़े आ वड़ मेरे
# ==========================================
k19_orig = """भावें जाण ना जाण वे वेहड़े आ वड़ मेरे ।
मैं तेरे कुरबान वे वेहड़े आ वड़ मेरे ।

तेरे जेहा मैनूं होर ना कोई ढूंडां जंगल बेला रोही,
ढूंडां तां सारा जहान वे वेहड़े आ वड़ मेरे ।

लोकां दे भाणे चाक महीं दा रांझा तां लोकां विच कहींदा,
साडा तां दीन ईमान वे वेहड़े आ वड़ मेरे ।

मापे छोड़ लग्गी लड़ तेरे शाह इनायत साईं मेरे,
लाईआं दी लज्ज पाल वे वेहड़े आ वड़ मेरे ।
मैं तेरे कुरबान वे वेहड़े आ वड़ मेरे ।"""

k19_hi = """चाहे मुझे अपनी जानो या बेगानी समझो, हे प्रियतम! मेरे आँगन में कदम रख दो!  
मैं तुम पर सर्वस्व न्योछावर करती हूँ, हे प्यारे! मेरे आँगन में कदम रख दो!  

तुम्हारे जैसा मुझे कोई दूसरा दिखाई नहीं देता,  
मैंने सघन जंगलों, नदी-कछारों और रेगिस्तानों को छान मारा!  
चाहे मैं सारे संसार में ढूँढ लूँ, तुम्हारे समान कोई नहीं,  
हे प्रियतम! कृपा करके मेरे इस सूने आँगन में आ जाओ!  

दुनिया के विचार में तो रांझा केवल भैंसें चराने वाला एक चरवाहा है,  
लोग उसे केवल एक साधारण सा ग्वाला ही कहते हैं!  
परंतु हमारे लिए तो वही हमारा धर्म, हमारा ईमान और हमारा सर्वस्व है,  
हे प्रियतम! कृपा करके मेरे हृदय के आँगन में आ जाओ!  

माता-पिता और सारे कुल को छोड़कर मैं तुम्हारे पल्ले से बँध गई हूँ,  
हे मेरे मुर्शिद, मेरे सतगुरु शाह इनायत!  
इस लगाई हुई प्रीत की लाज रखो और वचन निभाओ,  
मैं तुम पर बार-बार बलिहारी जाती हूँ, मेरे आँगन में आ जाओ!"""

k19_en = """Whether Thou deemest me Thine own or a stranger,  
O Beloved, enter the courtyard of my longing heart!  
I surrender my very life as a sacrifice unto Thee,  
O Beloved, enter the courtyard of my longing heart!  

There is none like Thee in all creation,  
I searched the tangled woods, the river shores, the sandy waste!  
Even if I search the entire universe around,  
None equals Thy beauty, none matches Thy taste!  
O Beloved, enter the courtyard of my longing heart!  

In the eyes of worldly folk, Ranjha is but a cattle-herd,  
A humble servant whom people merely name in scorn!  
Yet to my devoted soul, He is my faith and holy Word,  
The singular truth for which my soul was born!  
O Beloved, enter the courtyard of my longing heart!  

Leaving parents, kith, and kin, I clung unto Thy sacred hem,  
O my revered Master, my Murshid, Shah Inayat divine!  
Preserve the sacred honor of the love we have entwined,  
I sacrifice my very self to be forever Thine!  
O Beloved, enter the courtyard of my longing heart!"""

batch.append({
    "id": 19,
    "title": "19. भावें जाण ना जाण वे वेहड़े आ वड़ मेरे",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k19_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "भावें जाण ना जाण वे वेहड़े आ वड़ मेरे ।",
                "hindi_gloss": "भावें (चाहे) जाण (पहचानो/अपनाओ) ना (अथवा न) जाण (पहचानो) वे (हे प्रिय), वेहड़े (मेरे आँगन) आ (आकर) वड़ (प्रवेश करो) मेरे (मेरे) ।",
                "english_gloss": "bhaavein (whether) jaan (acknowledge/know) na (or not) jaan (know) ve (O Beloved), vehde (courtyard) aa (come) vad (enter) mere (my) ."
            },
            {
                "original": "मैं तेरे कुरबान वे वेहड़े आ वड़ मेरे ।",
                "hindi_gloss": "मैं (मैं) तेरे (तुम पर) कुरबान (न्योछावर/बलिहारी हूँ) वे (हे प्रिय), वेहड़े (मेरे आँगन) आ (आकर) वड़ (प्रवेश करो) मेरे (मेरे) ।",
                "english_gloss": "main (I) tere (upon you) kurbaan (sacrifice) ve (O Beloved), vehde (courtyard) aa (come) vad (enter) mere (my) ."
            },
            {
                "original": "तेरे जेहा मैनूं होर ना कोई ढूंडां जंगल बेला रोही,",
                "hindi_gloss": "तेरे (तुम्हारे) जेहा (समान) मैनूं (मुझे) होर (अन्य) ना (कोई नहीं) कोई (दिखता), ढूंडां (ढूँढती हूँ) जंगल (जंगलों) बेला (नदी-कछारों) रोही (और मरुस्थलों में),",
                "english_gloss": "tere (your) jeha (like) mainoon (to me) hor (other) na (not) koi (any), dhoondaan (I search) jangal (forests) bela (river-banks) rohi (deserts),"
            },
            {
                "original": "ढूंडां तां सारा जहान वे वेहड़े आ वड़ मेरे ।",
                "hindi_gloss": "ढूंडां (चाहे ढूँढ लूँ) तां (तो) सारा (संपूर्ण) जहान (संसार), वे (हे प्रियतम) वेहड़े (मेरे आँगन) आ (आकर) वड़ (प्रवेश करो) मेरे (मेरे) ।",
                "english_gloss": "dhoondaan (I search) taan (though) saara (entire) jahaan (world), ve (O Beloved) vehde (courtyard) aa (come) vad (enter) mere (my) ."
            },
            {
                "original": "लोकां दे भाणे चाक महीं दा रांझा तां लोकां विच कहींदा,",
                "hindi_gloss": "लोकां (लोगों) दे (के) भाणे (नज़र में) चाक (मवेशी चराने वाला/सेवक) महीं (भैंसों) दा (का), रांझा (रांझा) तां (तो) लोकां (लोगों) विच (के बीच) कहींदा (कहा जाता है),",
                "english_gloss": "lokaan (people's) de (of) bhaane (in estimation) chaak (servant/herdsman) maheen (of buffaloes) da (of), raanjha (Ranjha) taan (indeed) lokaan (people) vich (among) kaheenda (is called),"
            },
            {
                "original": "साडा तां दीन ईमान वे वेहड़े आ वड़ मेरे ।",
                "hindi_gloss": "साडा (हमारा) तां (तो वही) दीन (धर्म) ईमान (और सच्चा ईमान है), वे (हे प्रिय) वेहड़े (मेरे आँगन) आ (आकर) वड़ (प्रवेश करो) मेरे (मेरे) ।",
                "english_gloss": "saada (our) taan (indeed) deen (religion) eemaan (faith), ve (O Beloved) vehde (courtyard) aa (come) vad (enter) mere (my) ."
            },
            {
                "original": "मापे छोड़ लग्गी लड़ तेरे शाह इनायत साईं मेरे,",
                "hindi_gloss": "मापे (माता-पिता/कुल-कुटुंब) छोड़ (त्यागकर) लग्गी (लग गई हूँ) लड़ (पल्ले/शरण में) तेरे (तुम्हारी), शाह (हे शाह) इनायत (इनायत) साईं (सतगुरु/स्वामी) मेरे (मेरे),",
                "english_gloss": "maape (parents/kin) chhod (abandoning) laggi (attached/clung) lad (hem/refuge) tere (your), shaah (Shah) inaayat (Inayat) saaen (Master) mere (my),"
            },
            {
                "original": "लाईआं दी लज्ज पाल वे वेहड़े आ वड़ मेरे ।",
                "hindi_gloss": "लाईआं (लगाई हुई प्रीत) दी (की) लज्ज (लाज/मर्यादा) पाल (निभाओ) वे (हे प्रिय), वेहड़े (मेरे आँगन) आ (आकर) वड़ (प्रवेश करो) मेरे (मेरे) ।",
                "english_gloss": "laaiyaan (of bonds formed) dee (of) lajj (honor/trust) paal (preserve/honor) ve (O Beloved), vehde (courtyard) aa (come) vad (enter) mere (my) ."
            },
            {
                "original": "मैं तेरे कुरबान वे वेहड़े आ वड़ मेरे ।",
                "hindi_gloss": "मैं (मैं) तेरे (तुम पर) कुरबान (बलिहारी हूँ) वे (हे प्यारे), वेहड़े (मेरे आँगन) आ (आकर) वड़ (प्रवेश करो) मेरे (मेरे) ।",
                "english_gloss": "main (I) tere (upon you) kurbaan (sacrifice) ve (O Beloved), vehde (courtyard) aa (come) vad (enter) mere (my) ."
            }
        ],
        "hindi_meaning": k19_hi,
        "english_meaning": k19_en
    }]
})

# ==========================================
# KAFI 20: 20. भरवासा की आशनाई दा
# ==========================================
k20_orig = """भरवासा की आशनाई दा ।
डर लगदा बे-परवाही दा ।

इबराहीम चिखा विच पायो, सुलेमान नूं भट्ठ झुकायो,
यूनस मच्छी तों निगलायो, फड़ यूसफ मिसर विकाईदा ।
भरवासा की आशनाई दा ।

ज़िकरिया सिर कलवत्तर चलायो, साबर दे तन कीड़े पायो,
सुन्नआं गल ज़न्नार पवायो,किते उलटा पोश लुहाई दा ।
भरवासा की आशनाई दा ।

पैग़म्बर ते नूर उपायो, नाम इमाम हुसैन धरायो,
झुला जिबराईल झुलायो, फिर प्यासा गला कटाईदा ।
भरवासा की आशनाई दा ।

जा ज़करिया रुक्ख छुपाइआ, छपणां उस दा बुरा मनाइआ,
आरा सिर ते चा वगाइआ, सणे रुक्ख चराईदा ।
भरवासा की आशनाई दा ।

यहीहा उस दा यार कहाइआ, नाल ओसे दे नेहुं लगाइआ,
राह शर्हा दा उन्न बतलाइआ, सिर उस दा थाल कटाईदा ।
भरवासा की आशनाई दा ।

बुल्ल्हा शौह हुण असीं संञाते हैं, हर सूरत नाल पछाते हैं,
किते आते हैं किते जाते हैं,हुण मैथों भुल्ल ना जाई दा ।
भरवासा की आशनाई दा ।"""

k20_hi = """इस ईश्वरीय प्रेम और यारी का क्या भरोसा किया जाए?  
प्रभु की रहस्यमयी बेपरवाही और लीला का सदा डर लगा रहता है!  

हज़रत इब्राहिम को सुलगती चिता की आग में डलवा दिया,  
और सुलेमान बादशाह को भट्टी की राख में झुकवा दिया!  
यूनुस नबी को मछली के पेट में निगलवा दिया,  
और हज़रत यूसुफ़ को मिस्र के बाज़ार में गुलाम बनवाकर बिकवा दिया!  
इस ईश्वरीय प्रेम और यारी का क्या भरोसा किया जाए?  

हज़रत ज़करिया के पावन सिर पर आरा चलवा दिया,  
और साबर (अय्यूब) के शरीर को कीड़ों से छिन्न-भिन्न करवा दिया!  
सनाआन जैसे ज्ञानी के गले में जनेऊ डलवा दिया,  
और कहीं शम्स की उल्टी खाल उतरवा ली!  
इस ईश्वरीय प्रेम और यारी का क्या भरोसा किया जाए?  

पैग़म्बर के पवित्र कुल से दिव्य नूर प्रकट किया,  
और उनका पावन नाम इमाम हुसैन रखा!  
जिसका झूला फ़रिश्ते जिब्राईल ने झुलाया था,  
अंत में कर्बला की तपती रेत पर प्यासा ही उसका गला कटवा दिया!  
इस ईश्वरीय प्रेम और यारी का क्या भरोसा किया जाए?  

जब हज़रत ज़करिया ने वृक्ष के खोखल में शरण ली,  
तो प्रभु ने उनका छिपना भी स्वीकार न किया!  
उनके सिर पर आरा रखवाकर चलवा दिया,  
और वृक्ष के साथ ही उनके शरीर को दो फाड़ करवा दिया!  
इस ईश्वरीय प्रेम और यारी का क्या भरोसा किया जाए?  

हज़रत यहया उनके परम प्रेमी और सखा कहलाए,  
जिन्होंने प्रभु के साथ गहरा आत्मिक नेह लगाया!  
सच्चे धर्म और शरियत का सीधा मार्ग बताया,  
पर अंत में उनका कटा हुआ सिर थाल में सजवा दिया!  
इस ईश्वरीय प्रेम और यारी का क्या भरोसा किया जाए?  

बुल्ले शाह कहते हैं—हे मेरे स्वामी! अब मैंने तुम्हें पहचान लिया है,  
सृष्टि के हर एक रूप और रंग में तुम्हें साफ़ जान लिया है!  
कहीं तुम आते हुए दिखते हो और कहीं जाते हुए,  
अब तुम लाख भेष बदलो, पर मुझसे छिपकर नहीं जा सकते!  
इस ईश्वरीय प्रेम और यारी का क्या भरोसा किया जाए?"""

k20_en = """What certainty can there be in the Beloved's mysterious friendship?  
One trembles at the sublime indifference of His unfathomed sway!  

Abraham was cast into the roaring furnace of fire,  
And mighty Solomon was brought low to tend the kiln's grey ash!  
Jonah was consigned to the belly of the leviathan,  
And Joseph was sold into bondage in Egypt's marketplace!  
What certainty can there be in the Beloved's mysterious friendship?  

A jagged saw was brought down upon Zechariah's head,  
And Job the Patient was covered in festering sores and worms!  
The devout Sheikh San'an was made to wear the pagan thread,  
And Shams was flayed alive upon the earth's cruel terms!  
What certainty can there be in the Beloved's mysterious friendship?  

From the Prophet's holy line was born a radiant light,  
Whom they named Imam Husain with reverence and praise!  
Gabriel himself had rocked the cradle in his sight,  
Yet His throat was slit while parched in Karbala's blazing rays!  
What certainty can there be in the Beloved's mysterious friendship?  

When Zechariah sought refuge within the hollow tree,  
His attempt to hide was counted as a fault divine!  
The tearing saw was summoned forth upon His plea,  
Cleaving both tree and prophet in one ruthless line!  
What certainty can there be in the Beloved's mysterious friendship?  

John the Baptist was declared His beloved intimate friend,  
Bound in the truest devotion to the One on high!  
He taught the righteous path of truth unto the end,  
Yet His severed head upon a platter was laid to die!  
What certainty can there be in the Beloved's mysterious friendship?  

Says Bulleh—O Beloved Lord, I have recognized Thee now!  
Through every mask and countenance Thy face is made clear!  
Somewhere Thou arrivest, somewhere Thou departest,  
Disguise Thyself as Thou wilt, Thou canst not elude me here!  
What certainty can there be in the Beloved's mysterious friendship?"""

batch.append({
    "id": 20,
    "title": "20. भरवासा की आशनाई दा",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k20_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "भरवासा की आशनाई दा ।",
                "hindi_gloss": "भरवासा (भरोसा/निश्चिंतता) की (क्या) आशनाई (ईश्वरीय प्रेम/यारी) दा (का) ।",
                "english_gloss": "bharwaasa (reliance/certainty) kee (what) aashnaai (divine love/friendship) da (of) ."
            },
            {
                "original": "डर लगदा बे-परवाही दा ।",
                "hindi_gloss": "डर (भय) लगदा (लगता है) बे-परवाही (प्रभु की बेपरवाही/अगोचर लीला) दा (का) ।",
                "english_gloss": "dar (fear/awe) lagda (feels) be-parwaahi (carefree indifference/unfathomable nature) da (of) ."
            },
            {
                "original": "इबराहीम चिखा विच पायो, सुलेमान नूं भट्ठ झुकायो,",
                "hindi_gloss": "इबराहीम (हज़रत इब्राहिम को) चिखा (अग्निकुंड/चिता) विच (में) पायो (डाल दिया), सुलेमान (हज़रत सुलेमान) नूं (को) भट्ठ (भट्ठी में) झुकायो (झोंक दिया/सेवा करवाई),",
                "english_gloss": "ibraaheem (Abraham) chikha (fiery furnace) vich (in) paayo (cast), sulemaan (Solomon) noon (unto) bhatth (furnace/kiln) jhukaayo (bowed/subjected to sweep),"
            },
            {
                "original": "यूनस मच्छी तों निगलायो, फड़ यूसफ मिसर विकाईदा ।",
                "hindi_gloss": "यूनस (हज़रत यूनुस को) मच्छी (मछली) तों (से) निगलायो (निगलवाया), फड़ (पकड़कर) यूसफ (हज़रत यूसुफ़ को) मिसर (मिस्र के बाज़ार में) विकाईदा (गुलाम बनाकर बिकवा दिया) ।",
                "english_gloss": "yoonas (Jonah) machhi (fish/whale) ton (by) niglaayo (caused to be swallowed), phad (seized) yoosaf (Joseph) misar (Egypt) vikaaeeda (caused to be sold as slave) ."
            },
            {
                "original": "भरवासा की आशनाई दा ।",
                "hindi_gloss": "भरवासा (भरोसा) की (क्या) आशनाई (प्रेम) दा (का) ।",
                "english_gloss": "bharwaasa (reliance) kee (what) aashnaai (love) da (of) ."
            },
            {
                "original": "ज़िकरिया सिर कलवत्तर चलायो, साबर दे तन कीड़े पायो,",
                "hindi_gloss": "ज़िकरिया (हज़रत ज़करिया के) सिर (सिर पर) कलवत्तर (आरा) चलायो (चलवाया), साबर (अय्यूब साबर/संत अय्यूब) दे (के) तन (शरीर पर) कीड़े (कीड़े) पायो (डाल दिए),",
                "english_gloss": "zikariya (Zechariah) sir (head) kalvattar (two-handled saw) chalaayo (ran), saabar (Job the Patient) de (of) tan (body) keede (worms) paayo (placed),"
            },
            {
                "original": "सुन्नआं गल ज़न्नार पवायो,किते उलटा पोश लुहाई दा ।",
                "hindi_gloss": "सुन्नआं (सुन्नी मुल्लाओं के) गल (गले में) ज़न्नार (जनेऊ/कुफ़्र का धागा) पवायो (डलवा दिया/सनआन को सुअर चराने भेजा), किते (कहीं शम्स तबरेज़ की) उलटा (उल्टी) पोश (खाल) लुहाई (उतरवा) दा (ली जाती है) ।",
                "english_gloss": "sunnaan (orthodox Sunnis/Sheikh San'an) gal (neck) zannaar (sacred thread) pawaayo (made to wear), kite (elsewhere like Shams) ulta (reversed) posh (skin) luhaaeeda (flayed) ."
            },
            {
                "original": "भरवासा की आशनाई दा ।",
                "hindi_gloss": "भरवासा (भरोसा) की (क्या) आशनाई (प्रेम) दा (का) ।",
                "english_gloss": "bharwaasa (reliance) kee (what) aashnaai (love) da (of) ."
            },
            {
                "original": "पैग़म्बर ते नूर उपायो, नाम इमाम हुसैन धरायो,",
                "hindi_gloss": "पैग़म्बर (पैग़म्बर के वंश) ते (से) नूर (दिव्य नूर) उपायो (उत्पन्न किया), नाम (उनका नाम) इमाम (इमाम) हुसैन (हुसैन) धरायो (रखा),",
                "english_gloss": "paighambar (Prophet) te (from) noor (divine Light) upaayo (created), naam (name) imaam (Imam) husain (Husain) dharaayo (bestowed),"
            },
            {
                "original": "झुला जिबराईल झुलायो, फिर प्यासा गला कटाईदा ।",
                "hindi_gloss": "झुला (झूला) जिबराईल (फ़रिश्ते जिब्राईल ने) झुलायो (झुलाया), फिर (फिर भी कर्बला में) प्यासा (प्यासा रखकर) गला (गला) कटाईदा (कटवा दिया जाता है) ।",
                "english_gloss": "jhula (cradle) jibraaeel (Gabriel) jhulaayo (rocked), phir (yet) pyaasa (thirsty) gala (throat) kataaeeda (caused to be slit) ."
            },
            {
                "original": "भरवासा की आशनाई दा ।",
                "hindi_gloss": "भरवासा (भरोसा) की (क्या) आशनाई (प्रेम) दा (का) ।",
                "english_gloss": "bharwaasa (reliance) kee (what) aashnaai (love) da (of) ."
            },
            {
                "original": "जा ज़करिया रुक्ख छुपाइआ, छपणां उस दा बुरा मनाइआ,",
                "hindi_gloss": "जा (जब) ज़करिया (हज़रत ज़करिया ने) रुक्ख (पेड़ के खोखल में स्वयं को) छुपाइआ (छिपाया), छपणां (उनका छिपना) उस (उस प्रभु ने) बुरा (अनुचित) मनाइआ (समझा),",
                "english_gloss": "ja (when) zakariya (Zechariah) rukkh (tree) chhupaaia (hid in), chhapnaan (hiding) us (his) da (of) bura (ill/displeased) manaaia (deemed),"
            },
            {
                "original": "आरा सिर ते चा वगाइआ, सणे रुक्ख चराईदा ।",
                "hindi_gloss": "आरा (आरा) सिर (सिर) ते (पर) चा (उठाकर) वगाइआ (चलवा दिया), सणे (सहित) रुक्ख (वृक्ष के) चराईदा (दो फाड़ करवा दिया) ।",
                "english_gloss": "aara (saw) sir (head) te (upon) chaa (lifting) vagaaia (wielded), sane (along with) rukkh (tree) charaaeda (cleaved in two) ."
            },
            {
                "original": "भरवासा की आशनाई दा ।",
                "hindi_gloss": "भरवासा (भरोसा) की (क्या) आशनाई (प्रेम) दा (का) ।",
                "english_gloss": "bharwaasa (reliance) kee (what) aashnaai (love) da (of) ."
            },
            {
                "original": "यहीहा उस दा यार कहाइआ, नाल ओसे दे नेहुं लगाइआ,",
                "hindi_gloss": "यहीहा (हज़रत यहया/यूहन्ना ने) उस (उस परमात्मा) दा (का) यार (मित्र/आशिक़) कहाइआ (कहलाया), नाल (साथ) ओसे (उसी) दे (के) नेहुं (प्रेम) लगाइआ (लगाया),",
                "english_gloss": "yahihha (John the Baptist/Yahya) us (his) da (of) yaar (beloved friend) kahaaia (was called), naal (with) ose (that very One) de (of) nehun (love) lagaaia (pledged),"
            },
            {
                "original": "राह शर्हा दा उन्न बतलाइआ, सिर उस दा थाल कटाईदा ।",
                "hindi_gloss": "राह (सत्य का मार्ग) शर्हा (शरियत/धर्म) दा (का) उन्न (उन्होंने) बतलाइआ (सिखाया), सिर (सिर) उस (उनका) दा (का) थाल (थाल में) कटाईदा (कटवाकर रखवाया गया) ।",
                "english_gloss": "raah (path) sharha (religious law/divine law) da (of) unn (he) batlaaia (taught), sir (head) us (his) da (of) thaal (platter) kataaeeda (severed and laid) ."
            },
            {
                "original": "भरवासा की आशनाई दा ।",
                "hindi_gloss": "भरवासा (भरोसा) की (क्या) आशनाई (प्रेम) दा (का) ।",
                "english_gloss": "bharwaasa (reliance) kee (what) aashnaai (love) da (of) ."
            },
            {
                "original": "बुल्ल्हा शौह हुण असीं संञाते हैं, हर सूरत नाल पछाते हैं,",
                "hindi_gloss": "बुल्ल्हा (बुल्ले शाह कहते हैं) शौह (हे प्रभु) हुण (अब) असीं (हमने) संञाते (पहचान लिया) हैं (है), हर (हर एक) सूरत (रूप/आकार) नाल (के साथ) पछाते (पहचान लिया) हैं (है),",
                "english_gloss": "bullha (Bulleh) shauh (O Lord) hun (now) aseen (we) sanjaate (recognized) hain (have), har (every) soorat (form) naal (with) pachhaate (identified) hain (have),"
            },
            {
                "original": "किते आते हैं किते जाते हैं,हुण मैथों भुल्ल ना जाई दा ।",
                "hindi_gloss": "किते (कहीं) आते (आते) हैं (हो) किते (कहीं) जाते (जाते) हैं (हो), हुण (अब) मैथों (मुझसे) भुल्ल (भूलकर भी मत छिपो) ना (मत) जाई (जाओ) दा (जी) ।",
                "english_gloss": "kite (somewhere) aate (arriving) hain (are) kite (somewhere) jaate (departing) hain (are), hun (now) maithon (from me) bhull (forgetting/feigning) na (not) jaaeda (slip away) ."
            },
            {
                "original": "भरवासा की आशनाई दा ।",
                "hindi_gloss": "भरवासा (भरोसा) की (क्या) आशनाई (प्रेम) दा (का) ।",
                "english_gloss": "bharwaasa (reliance) kee (what) aashnaai (love) da (of) ."
            }
        ],
        "hindi_meaning": k20_hi,
        "english_meaning": k20_en
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
