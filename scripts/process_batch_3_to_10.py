import os
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
KAFIAN_DIR = os.path.join(DATA_DIR, "kafian")
CHECKPOINT_JSON = os.path.join(DATA_DIR, "checkpoint.json")

os.makedirs(KAFIAN_DIR, exist_ok=True)

batch_kafian = []

# ==========================================
# KAFI 3
# ==========================================
kafi_3_orig = """आयो सईयो रल दियो नी वधाई ।
मैं वर पाइआ रांझा माही ।

अज्ज तां रोज़ मुबारक चढ़आ, रांझा साडे वेहड़े वड़्या,
हत्थ खूंडी मोढे कम्बल धरिआ, चाकां वाली शकल बणाई,
आयो सईयो रल दियो नी वधाई ।

मुक्कट गऊआं दे विच रुल्लदा, जंगल जूहां दे विच रुल्लदा ।
है कोई अल्लाह दे वल्ल भुल्लदा, असल हकीकत ख़बर ना काई,
आयो सईयो रल दियो नी वधाई ।

बुल्ल्हे शाह इक सौदा कीता, पीता ज़हर प्याला पीता,
ना कुझ लाहा टोटा लीता, दर्द दुक्खां दी गठड़ी चाई,
आयो सईयो रल दियो नी वधाई ।
मैं वर पाइआ रांझा माही ।"""

kafi_3_hi_meaning = """आओ सखियो, मिलकर मुझे बधाई दो,
मैंने अपना वर रांझा पा लिया है!

आज बड़ा ही मुबारक दिन उगा है,
रांझा आज हमारे आंगन में उतरा है!
हाथ में लाठी, कंधे पर कंबल डाले,
ग्वाले का भेष बनाकर वो आया है!

वो मुकुटधारी प्रभु गायों के बीच घूमता है,
जंगलों और चरागाहों में भटकता है!
क्या कोई अल्लाह को पहचान कर भी भटकता है?
पर किसी को उसकी असल हकीकत की खबर ही नहीं!

बुल्ले शाह ने प्रेम का ऐसा सौदा किया है,
कि हंसकर विष का भरा प्याला पी लिया है!
न कोई नफ़ा देखा, न कोई घाटा,
बस प्रेम के दर्द-दुखों की गठरी सिर उठा ली है!
आओ सखियो, मिलकर मुझे बधाई दो,
मैंने अपना वर रांझा पा लिया है!"""

kafi_3_en_meaning = """Come, O sisters, join and congratulate me,
For I have won my Beloved Ranjha as my Lord!

A day most blessed has dawned today,
Ranjha has walked into my courtyard's way!
With a crook in hand and blanket on shoulder,
In the humble garb of a cowherd, he appears bolder!

The Crowned Lord wanders amongst the kine,
Roaming the meadows and forests divine!
Can anyone truly go astray from the Lord?
Yet none perceives the truth of this hidden chord!

Bulleh Shah has struck a singular bargain,
Drinking the cup of poison without disdain!
Caring naught for profit, fearing no pain,
Bearing the bundle of sacred grief in love's domain!
Come, O sisters, join and congratulate me,
For I have won my Beloved Ranjha as my Lord!"""

batch_kafian.append({
    "id": 3,
    "title": "3. आओ सईयो रल दियो नी वधाई",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": kafi_3_orig,
    "annotated_stanzas": [
        {
            "lines": [
                {
                    "original": "आयो सईयो रल दियो नी वधाई ।",
                    "hindi_gloss": "आयो (आओ) सईयो (हे सखियों) रल (मिलकर) दियो (दो) नी (री/अरी) वधाई (बधाई) ।",
                    "english_gloss": "aayo (come) saiyo (O friends/sisters) ral (together) diyo (give) nee (O dear) vadhaai (congratulations/blessings) ."
                },
                {
                    "original": "मैं वर पाइआ रांझा माही ।",
                    "hindi_gloss": "मैं (मैंने) वर (वर/पति/प्रियतम) पाइआ (पा लिया है) रांझा (रांझा) माही (माही/प्रियतम) ।",
                    "english_gloss": "main (I) var (bridegroom/beloved Lord) paaiya (have found) ranjha (Ranjha) maahi (my Beloved) ."
                },
                {
                    "original": "अज्ज तां रोज़ मुबारक चढ़आ, रांझा साडे वेहड़े वड़्या,",
                    "hindi_gloss": "अज्ज (आज) तां (तो) रोज़ (दिन) मुबारक (शुभ/मंगलमय) चढ़आ (उगा/आया है), रांझा (रांझा) साडे (हमारे) वेहड़े (आंगन में) वड़्या (प्रवेश किया है/आया है),",
                    "english_gloss": "ajj (today) taan (indeed) roz (day) mubaarak (blessed/auspicious) chadha (has dawned), ranjha (Ranjha) saade (our) vehde (courtyard) vadya (has entered),"
                },
                {
                    "original": "हत्थ खूंडी मोढे कम्बल धरिआ, चाकां वाली शकल बणाई,",
                    "hindi_gloss": "हत्थ (हाथ में) खूंडी (लाठी/डंडा) मोढे (कंधे पर) कम्बल (कंबल) धरिआ (रखा है), चाकां (ग्वालों/सेवकों) वाली (जैसी) शकल (सूरत/वेष) बणाई (बनाया है),",
                    "english_gloss": "hatth (in hand) khoondi (staff/crook) modhe (on shoulder) kambal (blanket) dharia (placed), chaakaan (cowherds/servants) waali (like) shakal (appearance) banaai (assumed),"
                },
                {
                    "original": "मुक्कट गऊआं दे विच रुल्लदा, जंगल जूहां दे विच रुल्लदा ।",
                    "hindi_gloss": "मुक्कट (मुकुटधारी/परमेश्वर) गऊआं (गायों) दे (के) विच (बीच) रुल्लदा (भटकता/चराता है), जंगल (जंगलों) जूहां (बीहड़ों/चरागाहों) दे (के) विच (बीच) रुल्लदा (घूमता है) ।",
                    "english_gloss": "mukkat (the crown-wearer/Divine Lord) gaaoon (cows) de (of) vich (among) rullda (wanders/tends), jangal (forests) joohaan (pastures/wilderness) de (of) vich (amidst) rullda (roams) ."
                },
                {
                    "original": "है कोई अल्लाह दे वल्ल भुल्लदा, असल हकीकत ख़बर ना काई,",
                    "hindi_gloss": "है (क्या) कोई (कोई) अल्लाह (परमात्मा) दे (के) वल्ल (मार्ग से/ओर) भुल्लदा (भूलता/भटकता है), असल (वास्तविक) हकीकत (सच्चाई की) ख़बर (खबर/ज्ञान) ना (नहीं) काई (कोई) ,",
                    "english_gloss": "hai (is) koi (anyone) allah (God) de (of) vall (towards/path) bhullda (errs/strays), asal (true) hakeekat (reality) khabar (knowledge/awareness) na (not) kaai (any) ,"
                },
                {
                    "original": "बुल्ल्हे शाह इक सौदा कीता, पीता ज़हर प्याला पीता,",
                    "hindi_gloss": "बुल्ल्हे (बुल्ले) शाह (शाह ने) इक (एक) सौदा (सौदा) कीता (किया है), पीता (पी लिया) ज़हर (विष का) प्याला (प्याला) पीता (पी लिया),",
                    "english_gloss": "bullhe (Bulleh) shah (Shah) ik (a) sauda (bargain) keeta (made), peeta (drank) zehar (poison) pyaala (cup of) peeta (drank),"
                },
                {
                    "original": "ना कुझ लाहा टोटा लीता, दर्द दुक्खां दी गठड़ी चाई,",
                    "hindi_gloss": "ना (न) कुझ (कुछ) लाहा (लाभ/मुनाफ़ा) टोटा (हानि/घाटा) लीता (लिया/देखा), दर्द (दर्द) दुक्खां (दुखों) दी (की) गठड़ी (पोटली) चाई (उठा ली है),",
                    "english_gloss": "na (neither) kujh (any) laaha (profit/gain) tota (loss) leeta (considered), dard (pain) dukkhaan (sorrows) dee (of) gathdi (bundle) chaai (lifted on shoulders) ,"
                }
            ],
            "hindi_meaning": kafi_3_hi_meaning,
            "english_meaning": kafi_3_en_meaning
        }
    ]
})

# ==========================================
# KAFI 4
# ==========================================
kafi_4_orig = """आ सजन गल लग्ग असाडे, केहा झेड़ा लाययो ई ?
सुत्त्यां बैठ्यां कुझ्झ ना डिट्ठा, जागदियां सहु पाययो ई ।
'कुम-ब-इज़नी' शमस बोले, उलटा कर लटकाययो ई ।
इश्कन इश्कन जग्ग विच होईआं, दे दिलास बिठाययो ई ।
मैं तैं काई नहीं जुदाई, फिर क्यों आप छुपाययो ई ।
मझ्झियां आईआं माही ना आया, फूक ब्रिहों  रुलाययो ई ।
एस इश्क दे वेखे कारे, यूसफ़ खूह पवाययो ई ।
वांग ज़ुलैखां विच मिसर दे, घुंगट खोल्ह रुलाययो ई ।
रब्ब-इ-अरानी मूसा बोले, तद कोह-तूर जलाययो ई ।
लण-तरानी झिड़कां वाला, आपे हुकम सुणाययो ई ।
इश्क दिवाने कीता फ़ानी, दिल यतीम बनाययो ई ।
बुल्हा शौह घर वस्या आ के, शाह इनायत पाययो ई ।
आ सजन गल लग्ग असाडे, केहा झेड़ा लाययो ई ?"""

kafi_4_hi_meaning = """आ प्यारे साजन, गले से लग जा,
यह कैसा झगड़ा तूने खड़ा किया है?

सोते-बैठे तो कुछ न दिखाई दिया,
जागते ही प्रीतम को पा लिया है!
शम्स तबरेज़ ने जब 'कुम-बि-इज़्नी' पुकारा,
तो उन्हें उल्टा लटका कर खाल खिंचवा दिया!

संसार में प्रेम की ऐसी पुकार मची,
कि तूने सांत्वना देकर पास बिठा लिया!
जब तुझमें और मुझमें कोई जुदाई ही नहीं,
फिर तूने स्वयं को क्यों छिपा लिया?

भैंसें चरकर लौट आईं, पर रांझा न आया,
विरह की आग में मुझे खूब रुला दिया!
इस इश्क के अजीब खेल तो देखो,
यूसुफ को कुएं में फिकवा दिया!
मिस्र के बाज़ार में ज़ुलैख़ा की मानिंद,
पर्दा खोलकर दर-दर रुला दिया!

मूसा ने जब कहा 'हे रब! मुझे अपना दीदार करा',
तो तूर पर्वत को जलाकर राख बना दिया!
और 'तू मुझे कभी नहीं देख सकता' की फटकार से,
स्वयं ही अपना फरमान सुना दिया!

इस इश्क ने दीवाने को फ़ना कर डाला,
मेरे दिल को अनाथ और बेसहारा बना दिया!
बुल्ले शाह के घर में प्रियतम स्वयं आ बसे,
जब सतगुरु शाह इनायत को पा लिया!
आ प्यारे साजन, गले से लग जा,
यह कैसा झगड़ा तूने खड़ा किया है?"""

kafi_4_en_meaning = """Come, O Beloved, embrace me close,
What is this strife you have begun?

While sleeping and idle, naught was perceived,
Awakening, the Beloved was retrieved!
When Shams cried aloud, 'Arise by my word!',
He was hung upside down, his flayed skin unstirred!

The clamor of love in the world grew loud,
You offered solace and calmed the crowd!
When there is no parting 'twixt you and me,
Why hide Thyself so secretly?

The herds returned, but the Herdsman stayed,
In the flames of parting my spirit frayed!
Behold the strange ways of this mystic love,
It cast young Joseph in the well from above!
Like Zulaikha in Egypt's crowded square,
Unveiled and weeping in sweet despair!

When Moses pleaded, 'Reveal Thyself, Lord!',
Mount Sinai burned at the flash of Thy sword!
With the stern rebuke, 'Thou shalt not see Me!',
Thou Thyself proclaimed the harsh decree!

This love has dissolved the seeker to dust,
Leaving the heart an orphan in trust!
The Supreme Lord has entered Bulleh's door,
In Master Shah Inayat, found evermore!
Come, O Beloved, embrace me close,
What is this strife you have begun?"""

batch_kafian.append({
    "id": 4,
    "title": "4. आ सजन गल लग्ग असाडे",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": kafi_4_orig,
    "annotated_stanzas": [
        {
            "lines": [
                {
                    "original": "आ सजन गल लग्ग असाडे, केहा झेड़ा लाययो ई ?",
                    "hindi_gloss": "आ (आओ) सजन (प्रियतम) गल (गले) लग्ग (लगो) असाडे (हमारे), केहा (कैसा) झेड़ा (विवाद/झगड़ा) लाययो (लगाया है) ई (तुमने) ?",
                    "english_gloss": "aa (come) sajan (beloved) gal (neck/embrace) lagg (hug) asaade (ours), keha (what kind of) jheda (quarrel/strife) laayyo (have stirred) ee (you) ?"
                },
                {
                    "original": "सुत्त्यां बैठ्यां कुझ्झ ना डिट्ठा, जागदियां सहु पाययो ई ।",
                    "hindi_gloss": "सुत्त्यां (सोते हुए) बैठ्यां (बैठे हुए) कुझ्झ (कुछ) ना (नहीं) डिट्ठा (दिखा), जागदियां (जागते हुए) सहु (स्वामी/प्रियतम को) पाययो (पा लिया) ई (है) ।",
                    "english_gloss": "suttyaan (while sleeping) baithyaan (while sitting) kujjh (nothing) na (not) dittha (was seen), jaagdiyaan (upon awakening) sahu (the Lord/Beloved) paayyo (found) ee (have) ."
                },
                {
                    "original": "'कुम-ब-इज़नी' शमस बोले, उलटा कर लटकाययो ई ।",
                    "hindi_gloss": "'कुम-ब-इज़नी' (मेरे हुक्म से जी उठ) शमस (शम्स तबरेज़) बोले (बोले), उलटा (उल्टा) कर (करके) लटकाययो (लटका दिया) ई (उन्हें/खाल खिंचवा दी) ।",
                    "english_gloss": "'qum-bi-izni' ('Arise by my command') shamas (Shams Tabrizi) bole (uttered), ulta (upside down) kar (making) latkaayyo (hanged/flayed) ee (was) ."
                },
                {
                    "original": "इश्कन इश्कन जग्ग विच होईआं, दे दिलास बिठाययो ई ।",
                    "hindi_gloss": "इश्कन (इश्क की चर्चाएं) इश्कन (प्रेम की पुकार) जग्ग (संसार) विच (में) होईआं (हुईं), दे (देकर) दिलास (सांत्वना/ढांढस) बिठाययो (बिठा लिया) ई (पास) ।",
                    "english_gloss": "ishqan (love's outcry) ishqan (tales of love) jagg (world) vich (in) hoiyaan (resounded), de (giving) dilaas (solace/comfort) bithaayyo (seated near) ee (have) ."
                },
                {
                    "original": "मैं तैं काई नहीं जुदाई, फिर क्यों आप छुपाययो ई ।",
                    "hindi_gloss": "मैं (मुझमें) तैं (तुझमें) काई (कोई) नहीं (नहीं है) जुदाई (दूरी/विछोह), फिर (फिर भी) क्यों (क्यों) आप (स्वयं को) छुपाययो (छिपा रखा है) ई (तुमने) ।",
                    "english_gloss": "main (in me) tain (in you) kaai (any) nahin (not) judai (separation), phir (then) kyon (why) aap (yourself) chhupaayyo (have hidden) ee (you) ."
                },
                {
                    "original": "मझ्झियां आईआं माही ना आया, फूक ब्रिहों  रुलाययो ई ।",
                    "hindi_gloss": "मझ्झियां (भैंसें) आईआं (लौट आईं) माही (माही/रांझा) ना (नहीं) आया (आया), फूक (फूंककर/जलाकर) ब्रिहों (विरह में) रुलाययो (रुला दिया) ई (है) ।",
                    "english_gloss": "majjhiyaan (buffaloes) aaiyaan (returned) maahi (the Beloved) na (not) aaya (came), phook (burning) brihon (in separation) rulaayyo (made to weep) ee (have) ."
                },
                {
                    "original": "एस इश्क दे वेखे कारे, यूसफ़ खूह पवाययो ई ।",
                    "hindi_gloss": "एस (इस) इश्क (इश्क) दे (के) वेखे (देखे हैं) कारे (अद्भुत करतब/खेल), यूसफ़ (हज़रत यूसुफ़ को) खूह (कुएं में) पवाययो (फेंकवा दिया) ई (था) ।",
                    "english_gloss": "es (this) ishq (love) de (of) vekhe (behold) kaare (deeds/miracles), yoosaf (Joseph) khooh (in the well) pawaayyo (caused to be cast) ee (was) ."
                },
                {
                    "original": "वांग ज़ुलैखां विच मिसर दे, घुंगट खोल्ह रुलाययो ई ।",
                    "hindi_gloss": "वांग (तरह) ज़ुलैखां (ज़ुलैख़ा की) विच (में) मिसर (मिस्र) दे (के), घुंगट (घूंघट/पर्दा) खोल्ह (खोलकर) रुलाययो (रुला दिया/तड़पाया) ई (था) ।",
                    "english_gloss": "vaang (like) zulaikhaan (Zulaikha) vich (in) misar (Egypt) de (of), ghungat (veil) kholh (unveiling) rulaayyo (made to weep/yearn) ee (was) ."
                },
                {
                    "original": "रब्ब-इ-अरानी मूसा बोले, तद कोह-तूर जलाययो ई ।",
                    "hindi_gloss": "रब्ब-इ-अरानी (हे प्रभु, मुझे अपना दीदार करा) मूसा (हज़रत मूसा) बोले (बोले), तद (तब) कोह-तूर (तूर पर्वत को) जलाययो (जलाकर भस्म कर दिया) ई (था) ।",
                    "english_gloss": "rabb-i-araani ('O Lord, show Thyself to me') moosa (Moses) bole (spoke), tad (then) koh-toor (Mount Sinai) jalaayyo (burned to ashes) ee (was) ."
                },
                {
                    "original": "लण-तरानी झिड़कां वाला, आपे हुकम सुणाययो ई ।",
                    "hindi_gloss": "लण-तरानी (तू मुझे कदापि नहीं देख सकता) झिड़कां (फटकार/चेतावनी) वाला (भरा), आपे (स्वयं ही) हुकम (हुक्म/आदेश) सुणाययो (सुनाया) ई (था) ।",
                    "english_gloss": "lan-taraani ('Thou canst not behold Me') jhidkaan (rebuke/admonition) waala (laden with), aape (Thyself) hukam (command) sunaayyo (proclaimed) ee (Thou) ."
                },
                {
                    "original": "इश्क दिवाने कीता फ़ानी, दिल यतीम बनाययो ई ।",
                    "hindi_gloss": "इश्क (इश्क ने) दिवाने (दीवाने/साधक को) कीता (कर दिया) फ़ानी (नष्ट/फ़ना), दिल (हृदय को) यतीम (अनाथ/निराधार) बनाययो (बना दिया) ई (है) ।",
                    "english_gloss": "ishq (love) deewaane (the lover/seeker) keeta (made) faani (annihilated/dissolved), dil (heart) yateem (orphan/destitute) banaayyo (rendered) ee (has) ."
                },
                {
                    "original": "बुल्हा शौह घर वस्या आ के, शाह इनायत पाययो ई ।",
                    "hindi_gloss": "बुल्हा (बुल्ले के) शौह (परमेश्वर/प्रियतम) घर (हृदय-घर में) वस्या (बस गए) आ (आकर) के (के), शाह (शाह) इनायत (इनायत को) पाययो (पा लिया) ई (है) ।",
                    "english_gloss": "bullha (of Bulleh) shauh (Divine Beloved) ghar (in the inner home) vasya (dwelt) aa (coming) ke (having), shah (Shah) inaayat (Inayat) paayyo (found/attained) ee (has) ."
                }
            ],
            "hindi_meaning": kafi_4_hi_meaning,
            "english_meaning": kafi_4_en_meaning
        }
    ]
})

# ==========================================
# KAFI 5
# ==========================================
kafi_5_orig = """अब हम गुंम हूए, प्रेम नगर के शहर ।
आपने आप नूं सोध रिहा हूं, ना सिर हाथ ना पैर ।
खुदी खोई अपना पद चीता, तब होई गल्ल ख़ैर ।
लत्थे पगड़े पहले घर थीं, कौन करे निरवैर ?
बुल्ल्हा शहु है दोहीं जहानीं, कोई ना दिसदा ग़ैर ।"""

kafi_5_hi_meaning = """अब हम खो गए हैं प्रेम-नगर के शहर में,
जहाँ खुद को ढूंढ रहा हूँ, पर न सिर है, न हाथ, न पैर!

जब अहंकार मिटा और अपने आत्म-पद को पहचाना,
तब जाकर जीवन की बात कुशल और मंगलमय हुई।
उस आदि-घर (परमात्मा) से सारे झगड़े-प्रपंच मिट गए,
अब यहाँ किससे बैर और किससे विरोध?
बुल्ले शाह कहते हैं—दोनों लोकों में केवल वही स्वामी व्याप्त है,
अब कोई भी मुझे दूसरा या पराया नहीं दिखता!"""

kafi_5_en_meaning = """Now have we dissolved in the City of Love,
Searching for myself, yet find neither head, hand, nor feet!

When ego was shed and the true self realized,
All turned auspicious and sweet peace was found.
All strife vanished at the threshold of the Primal Home,
With whom then could any enmity remain?
Bulleh Shah declares: The Lord pervades both the worlds,
Not a single soul appears as a stranger now!"""

batch_kafian.append({
    "id": 5,
    "title": "5. अब हम गुंम हूए, प्रेम नगर के शहर",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": kafi_5_orig,
    "annotated_stanzas": [
        {
            "lines": [
                {
                    "original": "अब हम गुंम हूए, प्रेम नगर के शहर ।",
                    "hindi_gloss": "अब (अब) हम (हम) गुंम (गायब/लीन) हूए (हो गए हैं), प्रेम (प्रेम) नगर (नगर) के (के) शहर (शहर में) ।",
                    "english_gloss": "ab (now) ham (we) gumm (lost/dissolved) hooye (have become), prem (love) nagar (town) ke (of) shahar (city in) ."
                },
                {
                    "original": "आपने आप नूं सोध रिहा हूं, ना सिर हाथ ना पैर ।",
                    "hindi_gloss": "आपने (अपने) आप (आप) नूं (को) सोध (तलाश/खोज) रिहा (रहा) हूं (हूं), ना (न) सिर (सिर है) हाथ (न हाथ) ना (न) पैर (पैर) ।",
                    "english_gloss": "aapne (own) aap (self) noon (unto) sodh (searching) riha (am) hoon (I), na (neither) sir (head) haath (nor hand) na (nor) pair (feet) ."
                },
                {
                    "original": "खुदी खोई अपना पद चीता, तब होई गल्ल ख़ैर ।",
                    "hindi_gloss": "खुदी (अहंकार/अहम) खोई (खो दिया/त्याग दिया) अपना (अपने वास्तविक) पद (स्वरूप को) चीता (पहचाना/स्मरण किया), तब (तब जाकर) होई (हुई) गल्ल (बात) ख़ैर (कुशल/कल्याणकारी) ।",
                    "english_gloss": "khudi (ego/selfhood) khoi (lost/eradicated) apna (one's own) pad (true spiritual state) cheeta (realized/contemplated), tab (then) hoi (became) gall (matter) khair (well/blessed) ."
                },
                {
                    "original": "लत्थे पगड़े पहले घर थीं, कौन करे निरवैर ?",
                    "hindi_gloss": "लत्थे (उतर गए) पगड़े (झगड़े/विवाद) पहले (मूल/परमात्मा के) घर (घर) थीं (से), कौन (कौन) करे (करे) निरवैर (वैर या विवाद) ?",
                    "english_gloss": "latthe (fell away/resolved) pagde (disputes/quarrels) pehle (original/Divine) ghar (home) theen (from), kaun (who) kare (does/holds) nirvair (enmity/discord) ?"
                },
                {
                    "original": "बुल्ल्हा शहु है दोहीं जहानीं, कोई ना दिसदा ग़ैर ।",
                    "hindi_gloss": "बुल्ल्हा (हे बुल्ले) शहु (परमेश्वर/प्रियतम) है (है) दोहीं (दोनों) जहानीं (जहानों/लोकों में), कोई (कोई भी) ना (नहीं) दिसदा (दिखाई देता) ग़ैर (पराया/अन्य) ।",
                    "english_gloss": "bullha (O Bulleh) shauh (the Lord) hai (is) doheen (in both) jahaaneen (worlds), koi (anyone) na (not) disda (appears) gair (stranger/other) ."
                }
            ],
            "hindi_meaning": kafi_5_hi_meaning,
            "english_meaning": kafi_5_en_meaning
        }
    ]
})

# ==========================================
# KAFI 6
# ==========================================
kafi_6_orig = """अब क्यों साजन चिर लायो रे ?
ऐसी आई मन में काई,
दुख सुख सभ वंजाययो रे,
हार शिंगार को आग लगाउं,
घट उप्पर ढांड मचाययो रे ;
अब क्यों साजन चिर लाययो रे ?

सुन के ज्ञान की ऐसी बातां,
नाम निशान सभी अणघातां,
कोइल वांगूं कूकां रातां,
तैं अजे वी तरस ना आइयो रे ;
अब क्यों साजन चिर लाययो रे ?

गल मिरगानी सीस खपरिया,
भीख मंगन नूं रो रो फिरिआ,
जोगन नाम भ्या लिट धरिआ,
अंग बिभूत रमाययो रे ;
अब क्यों साजन चिर लाययो रे ?

इश्क मुल्लां ने बांग दिवाई,
उट्ठ बहुड़न गल्ल वाजब आई,
कर कर सिजदे घर वल धाई,
मत्थे महराब टिकाययो रे ;
अब क्यों साजन चिर लाययो रे ?

प्रेम नगर दे उलटे चाले,
ख़ूनी नैन होए खुशहाले,
आपे आप फसे विच जाले,
फस फस आप कुहाययो रे ;
अब क्यों साजन चिर लाययो रे ?

दुक्ख बिरहों ना होन पुराणे,
जिस तन पीड़ां सो तन जाणे,
अन्दर झिड़कां बाहर ताअने,
नेहुं लग्यां दुक्ख पाययो रे ;
अब क्यों साजन चिर लाययो रे ?

मैना मालन रोंदी पकड़ी,
बिरहों पकड़ी करके तकड़ी,
इक मरना दूजी जग्ग दी फक्कड़ी,
हुन कौन बन्ना बण आइयो रे ;
अब क्यों साजन चिर लाययो रे ?

बुल्ल्हा शौह संग प्रीत लगाई,
सोहनी बण तण सभ कोई आई,
वेख के शाह इनायत साईं,
जिय मेरा भर आइयो रे ;
अब क्यों साजन चिर लाययो रे ?"""

kafi_6_hi_meaning = """हे साजन! आने में इतनी देर क्यों लगा दी?
मन में ऐसी विरह-वेदना उठी है,
कि सुख और दुख का भेद ही मिट गया है!
सारे साज-श्रृंगार को आग लगा दूँ,
हृदय के भीतर विरह की ज्वाला धधक रही है;
हे साजन! आने में इतनी देर क्यों लगा दी?

ज्ञान और उपदेश की ऐसी बातें सुनीं,
कि सारे नाम और निशान बेअसर हो गए!
रात भर कोयल की तरह कूकती तड़पती हूँ,
पर तुझको ज़रा भी तरस न आया;
हे साजन! आने में इतनी देर क्यों लगा दी?

गले में मृगछाला और सिर पर खप्पर लिए,
तेरे दर्शन की भीख मांगती रोती फिरती हूँ!
जोगन बन जटाएं रख ली हैं,
और सारे अंगों पर भस्म रमा ली है;
हे साजन! आने में इतनी देर क्यों लगा दी?

इश्क रूपी मुल्लां ने जब अज़ान दी,
तो अंतर्मन में सत्य की बात जाग उठी!
सजदे करती हुई तेरे घर की ओर दौड़ी,
और माथे पर इबादत का मेहराब सजा लिया;
हे साजन! आने में इतनी देर क्यों लगा दी?

प्रेम-नगर की रीत ही बड़ी उल्टी है,
जहाँ खून के आंसू बहाने वाले नैन भी खुशहाल हैं!
अपने-आप प्रेम के जाल में फंस गए,
और फंस-फंस कर खुद को कुर्बान कर दिया;
हे साजन! आने में इतनी देर क्यों लगा दी?

विरह का यह दुख कभी पुराना नहीं पड़ता,
जिस तन पर यह बीतती है वही इसका मर्म जानता है!
भीतर प्रियतम की झिड़कियां और बाहर दुनिया के ताने,
प्रेम करके केवल विरह का दुख ही पाया;
हे साजन! आने में इतनी देर क्यों लगा दी?

बुल्ले शाह ने उस परमेश्वर से प्रीत लगाई है,
हर कोई सज-संवर कर सुहागिन बनकर आई है;
पर जब सतगुरु शाह इनायत का दीदार किया,
तो मेरा हृदय प्रेम के आंसुओं से भर आया;
हे साजन! आने में इतनी देर क्यों लगा दी?"""

kafi_6_en_meaning = """O Beloved! Why have You delayed so long?
Such an inner pang has struck my mind,
That all sorrow and joy are washed away!
I would set fire to all ornaments and adornments,
A blazing inferno rages within my breast;
O Beloved! Why have You delayed so long?

Hearing these deep discourses of spiritual knowledge,
All earthly names and traces seem meaningless!
Like a cuckoo I cry out in the dark of night,
Yet pity has not touched Your heart;
O Beloved! Why have You delayed so long?

With deer-skin on my neck and begging bowl in hand,
I wander weeping, begging for a single glimpse of You!
I have taken the name of an ascetic yogini with matted locks,
Smearing sacred ash across my limbs;
O Beloved! Why have You delayed so long?

When Love, like a Mullah, sounded the call to prayer,
The imperative of divine truth dawned upon me!
Prostrating in devotion, I rushed toward Your home,
Imprinting the mihrab of surrender upon my forehead;
O Beloved! Why have You delayed so long?

Upside down are the ways of Love's domain,
Where blood-weeping eyes rejoice in ecstasy!
Willingly I fell into love's tender snare,
Entangled and gladly slaughtered in sacrifice;
O Beloved! Why have You delayed so long?

The grief of separation never grows old,
Only the body that endures it knows its depth!
Scoldings from within and mockery from the world without,
In loving You, only the ache of yearning was earned;
O Beloved! Why have You delayed so long?

Bulleh Shah has forged love with the Supreme Lord,
Each soul arrives adorned like a lovely bride;
Yet beholding the Master, Shah Inayat the Divine,
My heart wells up in tears of sacred love;
O Beloved! Why have You delayed so long?"""

batch_kafian.append({
    "id": 6,
    "title": "6. अब क्यों साजन चिर लायो रे",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": kafi_6_orig,
    "annotated_stanzas": [
        {
            "lines": [
                {
                    "original": "अब क्यों साजन चिर लायो रे ?",
                    "hindi_gloss": "अब (अब) क्यों (क्यों) साजन (हे साजन/प्रियतम) चिर (देर/विलंब) लायो (लगाया है) रे (रे) ?",
                    "english_gloss": "ab (now) kyon (why) saajan (O Beloved) chir (delay) laayo (have made) re (O friend) ?"
                },
                {
                    "original": "ऐसी आई मन में काई, दुख सुख सभ वंजाययो रे,",
                    "hindi_gloss": "ऐसी (ऐसी) आई (आई है) मन (मन) में (में) काई (वेदना/काट), दुख (दुख) सुख (सुख) सभ (सब) वंजाययो (गंवा/मिटा दिया) रे,",
                    "english_gloss": "aisi (such) aai (has come) man (in mind) kaai (ache/anguish), dukh (sorrow) sukh (joy) sabh (all) vanjaayyo (lost/dissolved) re,"
                },
                {
                    "original": "हार शिंगार को आग लगाउं, घट उप्पर ढांड मचाययो रे ;",
                    "hindi_gloss": "हार (हार) शिंगार (श्रृंगार) को (को) आग (आग) लगाउं (लगा दूँ), घट (हृदय) उप्पर (पर) ढांड (अग्नि की लपटें) मचाययो (मचा दी हैं) रे ;",
                    "english_gloss": "haar (garlands) shingaar (ornaments) ko (to) aag (fire) lagaaoon (set), ghat (heart) uppar (upon) dhaand (blazing fire) machaayyo (has stirred) re ;"
                },
                {
                    "original": "सुन के ज्ञान की ऐसी बातां, नाम निशान सभी अणघातां,",
                    "hindi_gloss": "सुन (सुन) के (कर) ज्ञान (ज्ञान) की (की) ऐसी (ऐसी) बातां (बातें), नाम (नाम) निशान (निशान) सभी (सभी) अणघातां (व्यर्थ/अस्पष्ट हो गए),",
                    "english_gloss": "sun (hearing) ke (having) gyaan (wisdom) kee (of) aisi (such) baataan (words), naam (name) nishaan (trace) sabhi (all) anghaataan (meaningless/lost),"
                },
                {
                    "original": "कोइल वांगूं कूकां रातां, तैं अजे वी तरस ना आइयो रे ;",
                    "hindi_gloss": "कोइल (कोयल) वांगूं (की तरह) कूकां (कूकती/रोती हूँ) रातां (रातों में), तैं (तुझे) अजे (अभी) वी (भी) तरस (दया) ना (नहीं) आइयो (आई) रे ;",
                    "english_gloss": "koil (cuckoo) vaangoon (like) kookaan (cry out) raataan (in nights), tain (to you) aje (still) vee (even) taras (pity) na (not) aaiyo (came) re ;"
                },
                {
                    "original": "गल मिरगानी सीस खपरिया, भीख मंगन नूं रो रो फिरिआ,",
                    "hindi_gloss": "गल (गले में) मिरगानी (मृगछाला) सीस (सिर पर) खपरिया (खप्पर), भीख (दर्शन की भीख) मंगन (मांगने) नूं (को) रो (रो) रो (रोकर) फिरिआ (भटकती हूँ),",
                    "english_gloss": "gal (on neck) mirgaani (deer-skin) sees (on head) khapriya (begging bowl), bheekh (alms of vision) mangan (to beg) noon (for) ro (weeping) ro (crying) phiria (wandered),"
                },
                {
                    "original": "जोगन नाम भ्या लिट धरिआ, अंग बिभूत रमाययो रे ;",
                    "hindi_gloss": "जोगन (जोगन का) नाम (नाम) भ्या (लेकर) लिट (जटाएं) धरिआ (रख ली हैं), अंग (अंगों पर) बिभूत (भस्म) रमाययो (रमा ली है) रे ;",
                    "english_gloss": "jogan (ascetic yogini) naam (name) bhya (taking) lit (matted locks) dharia (kept), ang (on limbs) bibhoot (sacred ashes) ramaayyo (smeared) re ;"
                },
                {
                    "original": "इश्क मुल्लां ने बांग दिवाई, उट्ठ बहुड़न गल्ल वाजब आई,",
                    "hindi_gloss": "इश्क (प्रेम रूपी) मुल्लां (मुल्ला) ने (ने) बांग (अज़ान) दिवाई (दिलाई), उट्ठ (उठकर) बहुड़न (लौटने की) गल्ल (बात) वाजब (उचित/सत्य) आई (लगी),",
                    "english_gloss": "ishq (love) mullaan (mullah) ne (by) baang (call to prayer) divaai (sounded), utth (arising) bahudan (returning) gall (matter) vaajab (just/imperative) aai (appeared),"
                },
                {
                    "original": "कर कर सिजदे घर वल धाई, मत्थे महराब टिकाययो रे ;",
                    "hindi_gloss": "कर (कर) कर (करके) सिजदे (सजदे/दंडवत) घर (तेरे घर की) वल (ओर) धाई (दौड़ी), मत्थे (माथे पर) महराब (मेहराब/इबादत का चिह्न) टिकाययो (सजा लिया) रे ;",
                    "english_gloss": "kar (making) kar (repeating) sijde (prostrations) ghar (home) val (towards) dhaai (rushed), matthe (on forehead) mehraab (prayer arch) tikaayyo (affixed) re ;"
                },
                {
                    "original": "प्रेम नगर दे उलटे चाले, ख़ूनी नैन होए खुशहाले,",
                    "hindi_gloss": "प्रेम (प्रेम) नगर (नगर) दे (की) उलटे (उल्टी) चाले (रीत/चालें हैं), ख़ूनी (रक्त बहाने वाले) नैन (नेत्र) होए (होते हैं) खुशहाले (प्रसन्न/आनंदित),",
                    "english_gloss": "prem (love) nagar (town) de (of) ulte (inverted) chaale (customs/ways), khooni (blood-weeping) nain (eyes) hoye (become) khush-haale (joyful),"
                },
                {
                    "original": "आपे आप फसे विच जाले, फस फस आप कुहाययो रे ;",
                    "hindi_gloss": "आपे (अपने) आप (आप) फसे (फंस गए) विच (में) जाले (प्रेम-जाल के), फस (फंसकर) फस (फंसकर) आप (स्वयं को) कुहाययो (कुर्बान कर दिया) रे ;",
                    "english_gloss": "aape (oneself) aap (voluntarily) phase (trapped) vich (in) jaale (net of love), phas (entangled) phas (caught) aap (self) kuhaayyo (slaughtered/sacrificed) re ;"
                },
                {
                    "original": "दुक्ख बिरहों ना होन पुराणे, जिस तन पीड़ां सो तन जाणे,",
                    "hindi_gloss": "दुक्ख (दुख) बिरहों (विरह का) ना (नहीं) होन (होते) पुराणे (पुराने), जिस (जिस) तन (शरीर/मन पर) पीड़ां (पीड़ा बीतती है) सो (वही) तन (तन) जाणे (जानता है),",
                    "english_gloss": "dukkh (sorrow) birhon (of separation) na (not) hon (become) puraane (old), jis (which) tan (body) peedaan (agony strikes) so (that) tan (body) jaane (knows),"
                },
                {
                    "original": "अन्दर झिड़कां बाहर ताअने, नेहुं लग्यां दुक्ख पाययो रे ;",
                    "hindi_gloss": "अन्दर (भीतर) झिड़कां (झिड़कियां) बाहर (बाहर) ताअने (दुनियावी ताने), नेहुं (प्रेम) लग्यां (करने पर) दुक्ख (दुख ही) पाययो (पाया है) रे ;",
                    "english_gloss": "andar (within) jhidkaan (rebukes) baahar (outside) taane (taunts), nehun (love) lagyaan (having bound) dukkh (pain) paayyo (received) re ;"
                },
                {
                    "original": "बुल्ल्हा शौह संग प्रीत लगाई, सोहनी बण तण सभ कोई आई,",
                    "hindi_gloss": "बुल्ल्हा (बुल्ले ने) शौह (परमेश्वर) संग (साथ) प्रीत (प्रेम) लगाई (लगाया है), सोहनी (सुंदर सज-संवर कर) बण (बन) तण (ठान कर) सभ (हर) कोई (कोई) आई (आई है),",
                    "english_gloss": "bullha (Bulleh) shauh (with the Lord) sang (with) preet (love) lagaai (forged), sohni (beautiful) ban (becoming) tan (adorned) sabh (all) koi (everyone) aai (came),"
                },
                {
                    "original": "वेख के शाह इनायत साईं, जिय मेरा भर आइयो रे ;",
                    "hindi_gloss": "वेख (देख) के (कर) शाह (शाह) इनायत (इनायत) साईं (स्वामी को), जिय (हृदय) मेरा (मेरा) भर (आंसुओं से भर) आइयो (आया है) रे ;",
                    "english_gloss": "vekh (beholding) ke (having) shah (Shah) inaayat (Inayat) saaeen (Master), jiy (heart) mera (my) bhar (welled up) aaiyo (came) re ;"
                }
            ],
            "hindi_meaning": kafi_6_hi_meaning,
            "english_meaning": kafi_6_en_meaning
        }
    ]
})

# ==========================================
# KAFI 7
# ==========================================
kafi_7_orig = """अब लगन लगी किह करिए ?
ना जी सकीए ते ना मरीए ।

तुम सुनो हमारी बैना,
मोहे रात दिने नहीं चैना,
हुन पी बिन पलक ना सरीए ।
अब लगन लगी किह करीए ?

इह अगन बिरहों दी जारी,
कोई हमरी प्रीत निवारी,
बिन दरशन कैसे तरीए ?
अब लगन लगी किह करीए ?

बुल्ल्हे पई मुसीबत भारी,
कोई करो हमारी कारी,
इक अजेहे दुक्ख कैसे जरीए ?
अब लगन लगी किह करीए ?"""

kafi_7_hi_meaning = """अब प्रेम की लगन लग गई है, कहो अब क्या करें?
न तो जिया जाता है और न ही मरा जाता है!

हे सखियो! तुम मेरी विनती सुनो,
मुझे रात-दिन एक पल भी चैन नहीं है!
अब प्रियतम के बिना पलक झपकने भर भी नहीं गुज़रता,
अब प्रेम की लगन लग गई है, कहो अब क्या करें?

यह विरह की अग्नि निरंतर धधक रही है,
कोई आकर हमारी इस प्रीत का निवारण करे!
प्रियतम के दर्शन बिना इस भवसागर को कैसे पार करें?
अब प्रेम की लगन लग गई है, कहो अब क्या करें?

बुल्ले पर बहुत भारी मुसीबत आन पड़ी है,
कोई आकर हमारा कोई इलाज करे!
ऐसे असह्य विरह-दुखों को हम कैसे सहें?
अब प्रेम की लगन लग गई है, कहो अब क्या करें?"""

kafi_7_en_meaning = """Now that this longing of love has taken hold, what should I do?
Neither can I live, nor can I die!

Listen, O friends, to my humble plea,
Night and day, there is no peace for me!
Without my Beloved, not a single moment can pass,
Now that this longing of love has taken hold, what should I do?

This fire of separation burns ceaselessly,
Will someone come and tend to my love's misery?
Without beholding His face, how can I cross this sea?
Now that this longing of love has taken hold, what should I do?

A heavy calamity has fallen upon Bulleh,
Will someone bring a remedy to ease the way?
How can one bear such agonizing pain day by day?
Now that this longing of love has taken hold, what should I do?"""

batch_kafian.append({
    "id": 7,
    "title": "7. अब लगन लगी किह करिए",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": kafi_7_orig,
    "annotated_stanzas": [
        {
            "lines": [
                {
                    "original": "अब लगन लगी किह करिए ?",
                    "hindi_gloss": "अब (अब) लगन (प्रेम की लगन) लगी (लग गई है) किह (क्या) करिए (करें) ?",
                    "english_gloss": "ab (now) lagan (attachment/longing of love) lagi (has struck) kih (what) kariye (should we do) ?"
                },
                {
                    "original": "ना जी सकीए ते ना मरीए ।",
                    "hindi_gloss": "ना (न तो) जी (जी) सकीए (सकते हैं) ते (और) ना (न ही) मरीए (मर सकते हैं) ।",
                    "english_gloss": "na (neither) jee (live) sakiye (can we) te (and) na (nor) mariye (can we die) ."
                },
                {
                    "original": "तुम सुनो हमारी बैना, मोहे रात दिने नहीं चैना,",
                    "hindi_gloss": "तुम (तुम) सुनो (सुनो) हमारी (मेरी) बैना (विनती/वचन), मोहे (मुझे) रात (रात) दिने (दिन) नहीं (नहीं है) चैना (चैन/शांति),",
                    "english_gloss": "tum (you) suno (listen to) hamaari (my) baina (words/plea), mohe (to me) raat (night) dine (day) nahin (not) chaina (peace/rest),"
                },
                {
                    "original": "हुन पी बिन पलक ना सरीए ।",
                    "hindi_gloss": "हुन (अब) पी (प्रियतम के) बिन (बिना) पलक (एक पल भी) ना (नहीं) सरीए (गुज़रता/सरता) ।",
                    "english_gloss": "hun (now) pee (Beloved) bin (without) palak (a moment) na (not) sariye (can be spent/passed) ."
                },
                {
                    "original": "इह अगन बिरहों दी जारी, कोई हमरी प्रीत निवारी,",
                    "hindi_gloss": "इह (यह) अगन (अग्नि) बिरहों (विरह) दी (की) जारी (निरंतर जल रही है), कोई (कोई) हमरी (हमारी) प्रीत (प्रीत की पीड़ा को) निवारी (निवारण करे/दूर करे),",
                    "english_gloss": "eh (this) agan (fire) birhon (of separation) dee (of) jaari (is burning), koi (someone) hamri (our) preet (anguish of love) nivaari (cure/relieve),"
                },
                {
                    "original": "बिन दरशन कैसे तरीए ?",
                    "hindi_gloss": "बिन (बिना) दरशन (दीदार/दर्शन के) कैसे (कैसे) तरीए (पार उतरें/तरें) ?",
                    "english_gloss": "bin (without) darshan (sight/vision) kaise (how) tariye (can we cross/swim) ?"
                },
                {
                    "original": "बुल्ल्हे पई मुसीबत भारी, कोई करो हमारी कारी,",
                    "hindi_gloss": "बुल्ल्हे (बुल्ले पर) पई (आन पड़ी है) मुसीबत (मुसीबत/विपदा) भारी (भारी), कोई (कोई) करो (करो) हमारी (हमारा) कारी (इलाज/उपाय),",
                    "english_gloss": "bullhe (upon Bulleh) pai (has fallen) museebat (calamity/trouble) bhaari (heavy), koi (someone) karo (make) hamaari (our) kaari (remedy/cure),"
                },
                {
                    "original": "इक अजेहे दुक्ख कैसे जरीए ?",
                    "hindi_gloss": "इक (ऐसे) अजेहे (असह्य/अजीब) दुक्ख (दुखों को) कैसे (कैसे) जरीए (सहन करें/झेलें) ?",
                    "english_gloss": "ik (such) ajehe (unbearable/wondrous) dukkh (sorrows) kaise (how) jariye (can be endured) ?"
                }
            ],
            "hindi_meaning": kafi_7_hi_meaning,
            "english_meaning": kafi_7_en_meaning
        }
    ]
})

# ==========================================
# KAFI 8
# ==========================================
kafi_8_orig = """ऐसा जगिआ ज्ञान पलीता ।
ना हम हिन्दू ना तुर्क ज़रूरी, नाम इश्क दी है मनज़ूरी,
आशक ने वर जीता, ऐसा जग्या ज्ञान पलीता ।

वेखो ठग्गां शोर मचाइआ, जंमना मरना चा बणाइआ ।
मूर्ख भुल्ले रौला पाइआ, जिस नूं आशक ज़ाहर कीता,
ऐसा जग्या ज्ञान पलीता ।

बुल्ल्हा आशक दी बात न्यारी, प्रेम वालिआं बड़ी करारी,
मूर्ख दी मत्त ऐवें मारी, वाक सुख़न चुप्प कीता,
ऐसा जग्या ज्ञान पलीता ।"""

kafi_8_hi_meaning = """अंदर ज्ञान की ऐसी दिव्य ज्योति जाग उठी है,
कि अज्ञान का सारा अंधेरा मिट गया!

न हम पक्के हिन्दू हैं, न कट्टर मुसलमान,
हमें तो केवल सच्चे प्रेम का नाम ही मंज़ूर है!
सच्चे प्रेमी ने उस परमेश्वर को पा लिया है,
अंदर ज्ञान की ऐसी दिव्य ज्योति जाग उठी है!

देखो, पाखंडी ठगों ने कैसा शोर मचा रखा है,
जन्म और मरण का झूठा प्रपंच बना रखा है!
नासमझ मूर्खों ने व्यर्थ का शोर मचाया,
पर सच्चे आशिक ने ईश्वर के रहस्य को प्रकट कर दिया!

बुल्ले शाह कहते हैं—सच्चे प्रेमी की बात ही निराली है,
प्रेमियों की लगन अत्यंत दृढ़ और खरी है!
मूर्खों की मति व्यर्थ के विवादों में मारी गई,
जबकि ज्ञानी साधक मौन रहकर मौज में आ गया!
अंदर ज्ञान की ऐसी दिव्य ज्योति जाग उठी है!"""

kafi_8_en_meaning = """Such a torch of divine wisdom has been ignited within,
That all darkness of illusion has melted away!

Neither are we strictly Hindu, nor orthodox Muslim,
We accept only the sacred decree of Divine Love!
The true lover has won the Divine Bridegroom,
Such a torch of divine wisdom has been ignited within!

Behold the loud uproar stirred by worldly impostors,
Inventing superstitious dogmas of birth and death!
Deluded fools raise a hollow clamor,
While the true lover reveals the hidden Reality!

Bulleh Shah says: Rare is the tale of the mystic lover,
Firm and resolute is the path of those who truly love!
The sense of the ignorant is ruined by petty disputes,
While the wise saint rests in deep and golden silence!
Such a torch of divine wisdom has been ignited within!"""

batch_kafian.append({
    "id": 8,
    "title": "8. ऐसा जगिआ ज्ञान पलीता",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": kafi_8_orig,
    "annotated_stanzas": [
        {
            "lines": [
                {
                    "original": "ऐसा जगिआ ज्ञान पलीता ।",
                    "hindi_gloss": "ऐसा (ऐसा) जगिआ (जाग उठा है/प्रज्वलित हुआ) ज्ञान (ज्ञान का) पलीता (मशाल/दीपक) ।",
                    "english_gloss": "aisa (such a) jagia (ignited/awakened) gyaan (of divine wisdom) paleeta (torch/spark) ."
                },
                {
                    "original": "ना हम हिन्दू ना तुर्क ज़रूरी, नाम इश्क दी है मनज़ूरी,",
                    "hindi_gloss": "ना (न) हम (हम) हिन्दू (हिन्दू हैं) ना (न ही) तुर्क (मुसलमान) ज़रूरी (कट्टर/अनिवार्य रूप से), नाम (केवल नाम) इश्क (प्रेम) दी (की) है (है) मनज़ूरी (स्वीकृति),",
                    "english_gloss": "na (neither) ham (are we) hindoo (Hindu) na (nor) turk (Muslim) zaroori (strictly/necessarily), naam (name/ordinance) ishq (of Divine Love) dee (of) hai (is) manzoori (approved/accepted),"
                },
                {
                    "original": "आशक ने वर जीता, ऐसा जग्या ज्ञान पलीता ।",
                    "hindi_gloss": "आशक (सच्चे प्रेमी) ने (ने) वर (परमेश्वर/प्रियतम को) जीता (पा/जीत लिया है), ऐसा (ऐसा) जग्या (जाग उठा) ज्ञान (ज्ञान का) पलीता (दीपक) ।",
                    "english_gloss": "aashak (true lover) ne (by) var (divine Spouse) jeeta (won), aisa (such) jagya (ignited) gyaan (wisdom) paleeta (torch) ."
                },
                {
                    "original": "वेखो ठग्गां शोर मचाइआ, जंमना मरना चा बणाइआ ।",
                    "hindi_gloss": "वेखो (देखो) ठग्गां (पाखंडी ठगों ने) शोर (शोर) मचाइआ (मचाया है), जंमना (जन्म) मरना (मरण का प्रपंच) चा (उठाकर) बणाइआ (बना रखा है) ।",
                    "english_gloss": "vekho (behold) thaggaan (deceivers) shor (clamor) machaaiya (have stirred), jamna (birth) marna (death) cha (conjuring up) banaaiya (have fabricated) ."
                },
                {
                    "original": "मूर्ख भुल्ले रौला पाइआ, जिस नूं आशक ज़ाहर कीता,",
                    "hindi_gloss": "मूर्ख (मूर्खों ने) भुल्ले (भूलकर) रौला (हल्ला/विवाद) पाइआ (डाल रखा है), जिस (जिस सत्य को) नूं (को) आशक (सच्चे प्रेमी ने) ज़ाहर (प्रकट/प्रत्यक्ष) कीता (कर दिया है),",
                    "english_gloss": "moorkh (fools) bhulle (deluded) raula (quarrel/noise) paaiya (have created), jis (which truth) noon (unto) aashak (the lover) zaahar (manifest) keeta (has made),"
                },
                {
                    "original": "बुल्ल्हा आशक दी बात न्यारी, प्रेम वालिआं बड़ी करारी,",
                    "hindi_gloss": "बुल्ल्हा (हे बुल्ले) आशक (सच्चे प्रेमी) दी (की) बात (बात ही) न्यारी (निराली है), प्रेम (प्रेम) वालिआं (वालों की निष्ठा) बड़ी (बड़ी) करारी (दृढ़/अडिग है),",
                    "english_gloss": "bullha (O Bulleh) aashak (of the lover) dee (of) baat (matter) nyaari (unique/sublime), prem (love) vaaliyaan (of those who possess) badi (very) karaari (unshakable/firm),"
                },
                {
                    "original": "मूर्ख दी मत्त ऐवें मारी, वाक सुख़न चुप्प कीता,",
                    "hindi_gloss": "मूर्ख (मूर्ख) दी (की) मत्त (बुद्धि) ऐवें (व्यर्थ ही) मारी (भ्रष्ट हो गई), वाक (वचन/वाणी) सुख़न (और शब्दों को) चुप्प (मौन) कीता (कर लिया) ,",
                    "english_gloss": "moorkh (of the fool) dee (of) matt (intellect) aiven (needlessly) maari (ruined), vaak (words) sukhan (speech) chupp (silence) keeta (embraced) ,"
                }
            ],
            "hindi_meaning": kafi_8_hi_meaning,
            "english_meaning": kafi_8_en_meaning
        }
    ]
})

# ==========================================
# KAFI 9
# ==========================================
kafi_9_orig = """ऐसा मन में आइयो रे, दुक्ख सुक्ख सभ वंञाययो रे ।
हार शिंगार को आग लगाऊं, तन पर ढांड मचाययो रे ।

सुन के ज्ञान कियां ऐसी बातां, नाम-निशान तभी अलघातां,
कोइल वांङ मैं कूकां रातां, तैं अजे भी तरस ना आइउ रे ।

गल मिरगानी सीस खप्परियां, दरशन की भीख मंगन चढ़आ,
जोगन नाम बूहलत धरिआ, अंग बिभूत रमायउ रे ।

इश्क मुल्लां ने बांग सुणाई, इह गल्ल वाजब आई,
कर कर सिदक सिजदे वल धाई, मूंह महराब टिकाययो रे ।

प्रेम नगर वाले उलटे चाले, मैं मोई भर खुशियां नाले,
आन फसी आपे विच जाले, हस्स हस्स आप कुहाययो रे ।

बुल्ल्हा शौह संग प्रीत लगाई, जिय जामे दी दित्ती साई,
मुरशद शाह अनायत साईं, जिस दिल मेरा भरमाययो रे ।"""

kafi_9_hi_meaning = """मन में ऐसा वैराग्य समाया है,
कि सुख और दुख का भेद ही मिट गया है!
सारे हार-श्रृंगार को आग लगा दूँ,
तन के भीतर विरह की आग धधक उठी है!

ज्ञान और आत्म-साक्षात्कार की ऐसी बातें सुनीं,
कि सारे सांसारिक नाम और निशान मिट गए!
रात भर कोयल की तरह विरह में कूकती हूँ,
पर तुझको ज़रा भी तरस न आया!

गले में मृगछाला, सिर पर खप्पर लिए,
तेरे दीदार की भीख मांगने निकली हूँ!
जोगन का भेष धारण कर लिया है,
और सारे अंगों पर भस्म रमा ली है!

इश्क रूपी मुल्लां ने जब अज़ान सुनाई,
तो यही बात सत्य और अनिवार्य जान पड़ी!
सच्चे विश्वास से सजदा करने भागी,
और हृदय के मुख पर इबादत का मेहराब सजा लिया!

प्रेम-नगर की रीत ही बड़ी उल्टी है,
जहाँ मिटकर भी प्राणों में आनंद भर आया!
अपने-आप प्रेम के जाल में आकर फंसी,
और हंसते-हंसते खुद को कुर्बान कर दिया!

बुल्ले शाह ने उस परमेश्वर से ऐसी प्रीत लगाई,
कि अपने प्राणों का जामा ही उसके नाम कर दिया!
वे सतगुरु शाह इनायत ही मेरे स्वामी हैं,
जिन्होंने मेरे दिल को अपने प्रेम में मोह लिया!"""

kafi_9_en_meaning = """Such intense longing has enveloped my mind,
That all sorrow and pleasure are completely lost!
I would burn every worldly jewel and adornment,
A raging blaze of separation burns within my flesh!

Hearing these profound words of divine wisdom,
All earthly names and identities vanished away!
Like a lonely cuckoo I cry through the night,
Yet Your heart remains unmoved by pity!

With deer-skin on my neck and begging bowl in hand,
I have set out begging for the alms of Thy vision!
I have assumed the matted guise of an ascetic yogini,
Smearing holy ashes across all my limbs!

When Love, like the Mullah, gave the call to prayer,
This truth appeared righteous and inescapable!
With sincere faith I rushed to prostrate,
Adorning my countenance with the prayer-arch of devotion!

Upside down are the ways of Love's domain,
Where in dying, the heart is filled with pure bliss!
Willingly I walked into love's tender snare,
Laughing with joy as I surrendered in sacrifice!

Bulleh Shah has forged love with the Eternal Beloved,
Offering his very soul and body as an earnest pledge!
Master Shah Inayat is my divine Lord,
Who has captivated my heart with His celestial grace!"""

batch_kafian.append({
    "id": 9,
    "title": "9. ऐसा मन में आइयो रे",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": kafi_9_orig,
    "annotated_stanzas": [
        {
            "lines": [
                {
                    "original": "ऐसा मन में आइयो रे, दुक्ख सुक्ख सभ वंञाययो रे ।",
                    "hindi_gloss": "ऐसा (ऐसा भाव) मन (मन) में (में) आइयो (आया है) रे (रे), दुक्ख (दुख) सुक्ख (सुख) सभ (सब) वंञाययो (गंवा/मिटा दिया) रे ।",
                    "english_gloss": "aisa (such) man (mind) mein (in) aaiyo (came) re (O friend), dukkh (sorrow) sukkh (joy) sabh (all) vanjaayyo (lost/dissolved) re ."
                },
                {
                    "original": "हार शिंगार को आग लगाऊं, तन पर ढांड मचाययो रे ।",
                    "hindi_gloss": "हार (हार) शिंगार (श्रृंगार) को (को) आग (आग) लगाऊं (लगा दूँ), तन (तन) पर (पर/भीतर) ढांड (अग्नि की लपटें) मचाययो (मचा दी हैं) रे ।",
                    "english_gloss": "haar (garlands) shingaar (ornaments) ko (to) aag (fire) lagaaoon (set), tan (body) par (upon/within) dhaand (blaze) machaayyo (stirred) re ."
                },
                {
                    "original": "सुन के ज्ञान कियां ऐसी बातां, नाम-निशान तभी अलघातां,",
                    "hindi_gloss": "सुन (सुन) के (कर) ज्ञान (ज्ञान) कियां (की) ऐसी (ऐसी) बातां (बातें), नाम (नाम) निशान (निशान) तभी (तभी) अलघातां (मिट/विलीन हो गए),",
                    "english_gloss": "sun (hearing) ke (having) gyaan (wisdom) kiyaan (of) aisi (such) baataan (words), naam (name) nishaan (trace) tabhi (then) alghaataan (dissolved/vanished),"
                },
                {
                    "original": "कोइल वांङ मैं कूकां रातां, तैं अजे भी तरस ना आइउ रे ।",
                    "hindi_gloss": "कोइल (कोयल) वांङ (की तरह) मैं (मैं) कूकां (कूकती हूँ) रातां (रातों में), तैं (तुझे) अजे (अभी) भी (भी) तरस (दया) ना (नहीं) आइउ (आई) रे ।",
                    "english_gloss": "koil (cuckoo) vaang (like) main (I) kookaan (cry) raataan (in nights), tain (unto you) aje (yet) bhee (even) taras (pity) na (not) aaiu (came) re ."
                },
                {
                    "original": "गल मिरगानी सीस खप्परियां, दरशन की भीख मंगन चढ़आ,",
                    "hindi_gloss": "गल (गले में) मिरगानी (मृगछाला) सीस (सिर पर) खप्परियां (खप्पर), दरशन (दीदार) की (की) भीख (भीख) मंगन (मांगने) चढ़आ (निकली हूँ),",
                    "english_gloss": "gal (on neck) mirgaani (deer-skin) sees (on head) khappariyaan (begging bowl), darshan (vision) kee (of) bheekh (alms) mangan (to beg) chadha (set forth),"
                },
                {
                    "original": "जोगन नाम बूहलत धरिआ, अंग बिभूत रमायउ रे ।",
                    "hindi_gloss": "जोगन (जोगन का) नाम (नाम) बूहलत (वेष) धरिआ (धारण किया है), अंग (अंगों पर) बिभूत (भस्म) रमायउ (रमा ली है) रे ।",
                    "english_gloss": "jogan (ascetic yogini) naam (name) boohlat (guise) dharia (held/donned), ang (on limbs) bibhoot (ashes) ramaayu (smeared) re ."
                },
                {
                    "original": "इश्क मुल्लां ने बांग सुणाई, इह गल्ल वाजब आई,",
                    "hindi_gloss": "इश्क (प्रेम रूपी) मुल्लां (मुल्ला ने) बांग (अज़ान) सुणाई (सुनाई), इह (यह) गल्ल (बात) वाजब (सत्य/उचित) आई (जान पड़ी),",
                    "english_gloss": "ishq (love) mullaan (mullah) ne (by) baang (call to prayer) sunaai (sounded), eh (this) gall (matter) vaajab (just/righteous) aai (appeared),"
                },
                {
                    "original": "कर कर सिदक सिजदे वल धाई, मूंह महराब टिकाययो रे ।",
                    "hindi_gloss": "कर (कर) कर (करके) सिदक (सच्चा विश्वास) सिजदे (सजदे की) वल (ओर) धाई (दौड़ी), मूंह (मुख पर) महराब (इबादत का मेहराब) टिकाययो (सजा लिया) रे ।",
                    "english_gloss": "kar (with) kar (deep) sidak (sincere faith) sijde (prostration) val (towards) dhaai (rushed), moonh (upon face) mehraab (prayer arch) tikaayyo (adorned) re ."
                },
                {
                    "original": "प्रेम नगर वाले उलटे चाले, मैं मोई भर खुशियां नाले,",
                    "hindi_gloss": "प्रेम (प्रेम) नगर (नगर) वाले (की) उलटे (उल्टी) चाले (रीत है), मैं (मैं) मोई (मिटकर/मरकर) भर (भर उठी हूँ) खुशियां (आनंद से) नाले (साथ ही),",
                    "english_gloss": "prem (love) nagar (town) waale (of) ulte (inverted) chaale (ways), main (I) moi (having died) bhar (filled) khushiyaan (with joys) naale (alongside),"
                },
                {
                    "original": "आन फसी आपे विच जाले, हस्स हस्स आप कुहाययो रे ।",
                    "hindi_gloss": "आन (आकर) फसी (फंस गई) आपे (अपने-आप) विच (में) जाले (प्रेम-जाल के), हस्स (हंस-हंसकर) हस्स (हंसकर) आप (स्वयं को) कुहाययो (कुर्बान कर दिया) रे ।",
                    "english_gloss": "aan (coming) phasi (trapped) aape (voluntarily) vich (in) jaale (snare), hass (laughing) hass (smiling) aap (self) kuhaayyo (slaughtered/sacrificed) re ."
                },
                {
                    "original": "बुल्ल्हा शौह संग प्रीत लगाई, जिय जामे दी दित्ती साई,",
                    "hindi_gloss": "बुल्ल्हा (बुल्ले ने) शौह (परमेश्वर) संग (साथ) प्रीत (प्रेम) लगाई (लगाया है), जिय (प्राण) जामे (और शरीर) दी (का) दित्ती (दे दिया) साई (बयाना/संकल्प),",
                    "english_gloss": "bullha (Bulleh) shauh (with Supreme Lord) sang (with) preet (love) lagaai (forged), jiy (soul) jaame (body) dee (of) ditti (gave) saai (pledge/token),"
                },
                {
                    "original": "मुरशद शाह अनायत साईं, जिस दिल मेरा भरमाययो रे ।",
                    "hindi_gloss": "मुरशद (गुरु) शाह (शाह) अनायत (इनायत) साईं (स्वामी हैं), जिस (जिन्होंने) दिल (हृदय) मेरा (मेरा) भरमाययो (मोहित कर लिया है) रे ।",
                    "english_gloss": "murshad (Master) shah (Shah) anaayat (Inayat) saaeen (is the Lord), jis (who) dil (heart) mera (my) bharmaayyo (captivated/enamored) re ."
                }
            ],
            "hindi_meaning": kafi_9_hi_meaning,
            "english_meaning": kafi_9_en_meaning
        }
    ]
})

# ==========================================
# KAFI 10
# ==========================================
kafi_10_orig = """अक्खां विच दिल जानी प्यारिआ, केही चेटक लाइआ ई ।
मैं तेरे विच जर्रा ना जुदाई, साथों आप छुपाइआ ई ।

मझीं आईआं रांझा यार ना आया, फूक बिरहों डोलाइआ ई
अक्खां विच दिल जानी प्यारिआ ।

मैं नेड़े मैनूं दूर क्यों दिसना एं, साथों आप छुपाइआ ई
अक्खां विच दिल जानी प्यारिआ ।

विच मिसर दे वांग ज़ुलैख़ां, घुंगट खोल्ह रुलाइआ ई
अक्खां विच दिल जानी प्यारिआ ।

शौह बुल्ल्हे दे सिर पर बुरका, तेरे इश्क नचाइआ ई
अक्खां विच दिल जानी प्यारिआ,
केही चेटक लाइआ ई ।"""

kafi_10_hi_meaning = """मेरी आँखों में बसने वाले प्यारे दिलजानी!
यह तूने कैसा जादू और आकर्षण मुझ पर डाल दिया है?

मुझमें और तुझमें रत्ती भर भी जुदाई नहीं है,
फिर भी तूने स्वयं को मुझसे क्यों छिपा रखा है?

भैंसें चरकर लौट आईं, पर रांझा यार न आया,
विरह की आग में मुझे जलाकर विचलित कर दिया!
मेरी आँखों में बसने वाले प्यारे दिलजानी!

तू तो मेरे इतने निकट है, फिर मुझे दूर क्यों दिखाई देता है?
तूने खुद को मुझसे क्यों छिपा रखा है?
मेरी आँखों में बसने वाले प्यारे दिलजानी!

मिस्र के बाज़ार में ज़ुलैख़ा की तरह,
मेरा घूंघट खोलकर मुझे दर-दर रुला दिया!
मेरी आँखों में बसने वाले प्यारे दिलजानी!

बुल्ले शाह के सिर पर जो अहं का बुर्का था,
तेरे प्रेम ने उसे नचा-नचा कर तार-तार कर दिया!
मेरी आँखों में बसने वाले प्यारे दिलजानी,
यह तूने कैसा जादू और सम्मोहन डाल दिया है?"""

kafi_10_en_meaning = """O Beloved darling residing within my very eyes!
What enchanting spell have You cast over me?

Between You and me, there is not an atom of separation,
Why then have You hidden Yourself from my sight?

The herds have returned, but my beloved Herdsman came not,
Burning me in separation's fire, shaking my soul!
O Beloved darling residing within my very eyes!

When You are so near to me, why do You appear so far away?
Why have You concealed Yourself from me?
O Beloved darling residing within my very eyes!

Like Zulaikha in the midst of Egypt's bazaars,
Unveiling my shame, You made me weep in longing!
O Beloved darling residing within my very eyes!

Upon Bulleh's head was the veil of mortal pride,
Your love made him dance and cast it away!
O Beloved darling residing within my very eyes,
What enchanting spell have You cast over me?"""

batch_kafian.append({
    "id": 10,
    "title": "10. अक्खां विच दिल जानी प्यारिआ",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": kafi_10_orig,
    "annotated_stanzas": [
        {
            "lines": [
                {
                    "original": "अक्खां विच दिल जानी प्यारिआ, केही चेटक लाइआ ई ।",
                    "hindi_gloss": "अक्खां (आंखों) विच (में बसने वाले) दिल (दिल) जानी (के प्यारे) प्यारिआ (प्रियतम), केही (कैसा) चेटक (जादू/सम्मोहन) लाइआ (लगा दिया है) ई (तुमने) ।",
                    "english_gloss": "akkhaan (eyes) vich (within) dil (heart's) jaani (darling) pyaaria (beloved), kehi (what kind of) chetak (spell/magic) laaiya (have cast) ee (you) ."
                },
                {
                    "original": "मैं तेरे विच जर्रा ना जुदाई, साथों आप छुपाइआ ई ।",
                    "hindi_gloss": "मैं (मुझमें) तेरे (तुझमें) विच (में) जर्रा (रत्ती भर भी) ना (नहीं है) जुदाई (दूरी/विछोह), साथों (हमसे) आप (स्वयं को) छुपाइआ (छिपा रखा है) ई (तुमने) ।",
                    "english_gloss": "main (in me) tere (in you) vich (between) zarra (an atom) na (not) judai (separation), saathon (from us) aap (yourself) chhupaaiya (have hidden) ee (you) ."
                },
                {
                    "original": "मझीं आईआं रांझा यार ना आया, फूक बिरहों डोलाइआ ई",
                    "hindi_gloss": "मझीं (भैंसें) आईआं (लौट आईं) रांझा (रांझा) यार (प्रियतम) ना (नहीं) आया (आया), फूक (फूंककर/जलाकर) बिरहों (विरह ने) डोलाइआ (विचलित कर दिया है) ई (मुझे)",
                    "english_gloss": "majheen (buffaloes) aaiyaan (returned) ranjha (Ranjha) yaar (beloved friend) na (not) aaya (came), phook (scorching) birhon (separation) dolaaiya (shaken/unsettled) ee (has me)"
                },
                {
                    "original": "अक्खां विच दिल जानी प्यारिआ ।",
                    "hindi_gloss": "अक्खां (आंखों) विच (में बसने वाले) दिल (दिल के) जानी (प्रिय) प्यारिआ (प्यारे) ।",
                    "english_gloss": "akkhaan (eyes) vich (in) dil (heart) jaani (darling) pyaaria (beloved) ."
                },
                {
                    "original": "मैं नेड़े मैनूं दूर क्यों दिसना एं, साथों आप छुपाइआ ई",
                    "hindi_gloss": "मैं (मेरे) नेड़े (इतने पास होकर भी) मैनूं (मुझे) दूर (दूर) क्यों (क्यों) दिसना (दिखाई देता) एं (है), साथों (हमसे) आप (स्वयं को) छुपाइआ (छिपा रखा है) ई (तूने)",
                    "english_gloss": "main (to me) nede (so near) mainoon (unto me) door (far) kyon (why) disna (appear) ain (you), saathon (from us) aap (yourself) chhupaaiya (hidden) ee (you have)"
                },
                {
                    "original": "विच मिसर दे वांग ज़ुलैख़ां, घुंगट खोल्ह रुलाइआ ई",
                    "hindi_gloss": "विच (में) मिसर (मिस्र) दे (के) वांग (तरह) ज़ुलैख़ां (ज़ुलैख़ा की), घुंगट (घूंघट/पर्दा) खोल्ह (खोलकर) रुलाइआ (रुला दिया है) ई (तूने)",
                    "english_gloss": "vich (in) misar (Egypt) de (of) vaang (like) zulaikhaan (Zulaikha), ghungat (veil) kholh (opening) rulaaiya (made to weep) ee (you have)"
                },
                {
                    "original": "शौह बुल्ल्हे दे सिर पर बुरका, तेरे इश्क नचाइआ ई",
                    "hindi_gloss": "शौह (परमेश्वर) बुल्ल्हे (बुल्ले) दे (के) सिर (सिर) पर (पर जो) बुरका (अहंकार का पर्दा था), तेरे (तेरे) इश्क (प्रेम ने) नचाइआ (नचाकर उतार फेंका) ई (है)",
                    "english_gloss": "shauh (Lord) bullhe (of Bulleh) de (of) sir (head) par (upon) burqa (veil of ego), tere (your) ishq (love) nachaaiya (made dance/unveiled) ee (has)"
                }
            ],
            "hindi_meaning": kafi_10_hi_meaning,
            "english_meaning": kafi_10_en_meaning
        }
    ]
})

# Save each Kafi to data/kafian/kafi_{id:03d}.json
for k in batch_kafian:
    k_id = k["id"]
    fname = os.path.join(KAFIAN_DIR, f"kafi_{k_id:03d}.json")
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(k, f, ensure_ascii=False, indent=2)
    print(f"Saved {fname}")

# Update checkpoint.json
with open(CHECKPOINT_JSON, "r", encoding="utf-8") as f:
    chk = json.load(f)

chk["completed_ids"] = sorted(list(set(chk["completed_ids"] + [k["id"] for k in batch_kafian])))
chk["completed_count"] = len(chk["completed_ids"])
chk["last_updated"] = datetime.now().isoformat()
chk["next_kafi_id"] = max(chk["completed_ids"]) + 1
chk["status"] = "in_progress"

with open(CHECKPOINT_JSON, "w", encoding="utf-8") as f:
    json.dump(chk, f, ensure_ascii=False, indent=2)

print(f"Checkpoint updated: {chk['completed_count']}/160 completed. Next ID: {chk['next_kafi_id']}")
