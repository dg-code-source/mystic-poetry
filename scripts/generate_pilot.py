import os
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
KAFIAN_DIR = os.path.join(DATA_DIR, "kafian")
CHECKPOINT_JSON = os.path.join(DATA_DIR, "checkpoint.json")

os.makedirs(KAFIAN_DIR, exist_ok=True)

kafi_1_original = """आ मिल यार सार लै मेरी, मेरी जान दुक्खां ने घेरी ।
अन्दर ख़ाब विछोड़ा होया, ख़बर ना पैंदी तेरी ।
सुंञे बन विच लुट्टी साईआं, सूर पलंग ने घेरी ।
इह तां ठग्ग जगत दे, जेहा लावन जाल चफेरी ।
करम शर्हा दे धरम बतावन, संगल पावन पैरीं ।
ज़ात मज़्हब इह इश्क ना पुच्छदा, इश्क शर्हा दा वैरी ।
नदियों पार मुल्क सजन दा लहवो-लआब ने घेरी ।
सतिगुर बेड़ी फड़ी खलोती तैं क्यों लाई आ देरी ।
प्रीतम पास ते टोलना किस नूं, भुल्ल गयों सिखर दुपहरी ।
बुल्ल्हा शाह शौह तैनूं मिलसी, दिल नूं देह दलेरी ।
आ मिल यार सार लै मेरी, मेरी जान दुक्खां ने घेरी ।"""

kafi_1_hi_meaning = """आ मिल प्यारे यार, ज़रा सुध ले ले मेरी,
विरह और दुखों ने जां है घेरी!

अज्ञान की नींद में विछोह हो गया,
अब कोई खबर न मिलती तेरी।
सूने वन में लुट गई जीवन-संपदा,
विकारों के हिंसक पशुओं ने राह मेरी है घेरी।

ये दुनियावी ठग चारों ओर जाल बिछाते,
रीत-शरीयत की जंजीरें पांवों में डालते;
पर सच्चा इश्क न जाति पूछे न मजहब,
वह तो है मजहबी पाखंडों का वैरी!

उस पार है मेरे प्रीतम का प्यारा वतन,
पर माया और प्रलोभनों ने राह है घेरी।
किनारे पर सतगुरु नाव लिए खड़े हैं,
फिर आने में तूने क्यों कर दी देरी?

जब प्रीतम पास ही है, तो किसे ढूंढ रहा है,
भटक गया तू क्यों भरी दुपहरी?
बुल्ले शाह! दिल को दे ज़रा तसल्ली,
मिलेगा वो शौह, रख थोड़ी दलेरी!
आ मिल प्यारे यार, ज़रा सुध ले ले मेरी!"""

kafi_1_en_meaning = """Come, my Beloved, and care for me,
For sorrows have besieged my soul!

In deep slumber, I drifted apart,
Now no word of You reaches my heart.
Plundered am I in this barren wild,
By beasts of desire trapped and beguiled.

Worldly impostors cast their net wide,
Chaining our feet in dogma and pride;
Yet Divine Love knows neither creed nor clan,
Defying the rigid bounds of man!

Across the river lies my Lover's land,
Trapped on this shore in illusions I stand.
The True Guide waits with the ferry in sight,
Why delay your crossing, lost in the night?

When the Beloved is near, within your own breast,
Why wander at noon in a blinded quest?
O Bulleh Shah, let your heart take heart,
The Lord shall unite, never to part!
Come, my Beloved, and care for me!"""

kafi_1_data = {
    "id": 1,
    "title": "1. आ मिल यार सार लै मेरी",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": kafi_1_original,
    "annotated_stanzas": [
        {
            "lines": [
                {
                    "original": "आ मिल यार सार लै मेरी, मेरी जान दुक्खां ने घेरी ।",
                    "hindi_gloss": "आ (आओ) मिल (मिलो) यार (प्रियतम/सखा) सार (सुध/संभाल) लै (लो) मेरी (मेरी), मेरी (मेरी) जान (प्राण/जीवन) दुक्खां (दुखों) ने (ने) घेरी (घेर लिया है) ।",
                    "english_gloss": "aa (come) mil (meet) yaar (beloved/friend) saar (care/tidings) lai (take) meri (of mine), meri (my) jaan (life/soul) dukkhaan (sorrows) ne (by) gheri (surrounded) ."
                },
                {
                    "original": "अन्दर ख़ाब विछोड़ा होया, ख़बर ना पैंदी तेरी ।",
                    "hindi_gloss": "अन्दर (भीतर/अंतर्मन में) ख़ाब (नींद/अज्ञान के स्वप्न में) विछोड़ा (वियोग/अलगाव) होया (हुआ), ख़बर (सुध/समाचार) ना (नहीं) पैंदी (पड़ती/मिलती) तेरी (तुम्हारी) ।",
                    "english_gloss": "andar (within/inwardly) khwaab (dream/slumber of ignorance) vichhoda (separation) hoya (occurred), khabar (news/trace) na (not) paindi (is received) teri (of yours) ."
                },
                {
                    "original": "सुंञे बन विच लुट्टी साईआं, सूर पलंग ने घेरी ।",
                    "hindi_gloss": "सुंञे (सूनसान/निर्जन) बन (वन/जंगल) विच (में) लुट्टी (लुट गई) साईआं (हे स्वामी/हे ईश्वर), सूर (सूअर/विषय-विकार) पलंग (तेंदुए/हिंसक पशु) ने (ने) घेरी (घेर लिया है) ।",
                    "english_gloss": "sunje (desolate/deserted) ban (wilderness/forest) vich (in) lutti (plundered/robbed) saaiyan (O Master/Lord), soor (wild boars/base vices) palang (leopards/beasts of desire) ne (by) gheri (encircled) ."
                },
                {
                    "original": "इह तां ठग्ग जगत दे, जेहा लावन जाल चफेरी ।",
                    "hindi_gloss": "इह (ये) तां (तो) ठग्ग (ठग/छलिया) जगत (संसार) दे (के), जेहा (जो) लावन (बिछाते हैं) जाल (फंदा/जाल) चफेरी (चारों ओर) ।",
                    "english_gloss": "eh (these) taan (indeed) thagg (deceivers/swindlers) jagat (of the world) de (of), jeha (who) laavan (cast/spread) jaal (snares/traps) chapheri (all around) ."
                },
                {
                    "original": "करम शर्हा दे धरम बतावन, संगल पावन पैरीं ।",
                    "hindi_gloss": "करम (कर्मकांड) शर्हा (रूढ़िवादी विधान/शरीयत) दे (के) धरम (कर्तव्य/धर्म) बतावन (सिखाते हैं), संगल (ज़ंजीरें/सांकल) पावन (डालते हैं) पैरीं (पैरों में) ।",
                    "english_gloss": "karam (rituals) sharha (religious law/orthodoxy) de (of) dharam (duties/faith) bataavan (prescribe/teach), sangal (chains/fetters) paavan (put/bind) pairin (upon the feet) ."
                },
                {
                    "original": "ज़ात मज़्हब इह इश्क ना पुच्छदा, इश्क शर्हा दा वैरी ।",
                    "hindi_gloss": "ज़ात (जाति/कुल) मज़्हब (धर्म/मज़हब) इह (यह) इश्क (दिव्य प्रेम) ना (नहीं) पुच्छदा (पूछता), इश्क (इश्क) शर्हा (मजहबी पाखंड/शरीयत) दा (का) वैरी (शत्रु/विरोधी) ।",
                    "english_gloss": "zaat (caste/lineage) mazhab (religion/creed) eh (this) ishq (Divine Love) na (not) puchhda (asks/regards), ishq (love) sharha (dogmatic law) da (of) vairi (adversary/enemy) ."
                },
                {
                    "original": "नदियों पार मुल्क सजन दा लहवो-लआब ने घेरी ।",
                    "hindi_gloss": "नदियों (नदी के) पार (उस पार) मुल्क (देश/आशियाना) सजन (प्रियतम) दा (का), लहवो-लआब (सांसारिक प्रलोभनों व व्यर्थ आमोद-प्रमोद) ने (ने) घेरी (रोक/घेर रखा है) ।",
                    "english_gloss": "nadiyon (river) paar (across/beyond) mulk (homeland/realm) sajan (of the Beloved) da (of), lahvo-laaab (worldly illusions and fleeting pleasures) ne (by) gheri (surrounded/held back) ."
                },
                {
                    "original": "सतिगुर बेड़ी फड़ी खलोती तैं क्यों लाई आ देरी ।",
                    "hindi_gloss": "सतिगुर (सच्चे गुरु) बेड़ी (नाव) फड़ी (थामकर) खलोती (खड़े हैं), तैं (तूने) क्यों (क्यों) लाई (लगाई) आ (आने में) देरी (देरी/विलंब) ।",
                    "english_gloss": "satgur (True Master/Guru) bedi (boat) phadi (holding) khaloti (stands waiting), tain (you) kyon (why) laai (made) aa (in reaching) deri (delay) ."
                },
                {
                    "original": "प्रीतम पास ते टोलना किस नूं, भुल्ल गयों सिखर दुपहरी ।",
                    "hindi_gloss": "प्रीतम (प्रियतम/ईश्वर) पास (पास ही/भीतर) ते (तो) टोलना (खोजना/ढूंढना) किस (किसे) नूं (को), भुल्ल (भूल/भटक) गयों (गया है) सिखर (कड़कती/चरम) दुपहरी (दोपहरी में) ।",
                    "english_gloss": "preetam (Beloved Lord) paas (near/within) te (then) tolna (seeking) kis (whom) noon (unto), bhull (lost/forgotten) gayon (you have become) sikhar (blazing peak) dupahari (in noon) ."
                },
                {
                    "original": "बुल्ल्हा शाह शौह तैनूं मिलसी, दिल नूं देह दलेरी ।",
                    "hindi_gloss": "बुल्ल्हा (हे बुल्ले शाह) शाह (स्वामी) शौह (परमेश्वर/प्रियतम) तैनूं (तुझे) मिलसी (मिलेगा), दिल (हृदय/मन) नूं (को) देह (दो) दलेरी (साहस/धैर्य) ।",
                    "english_gloss": "bullha (O Bulleh) shah (Master) shauh (Supreme Beloved) tainoon (unto you) milsi (shall unite), dil (heart) noon (to) deh (give) daleri (courage/fortitude) ."
                },
                {
                    "original": "आ मिल यार सार लै मेरी, मेरी जान दुक्खां ने घेरी ।",
                    "hindi_gloss": "आ (आओ) मिल (मिलो) यार (प्रियतम) सार (सुध) लै (लो) मेरी (मेरी), मेरी (मेरी) जान (प्राण) दुक्खां (दुखों) ने (ने) घेरी (घेर लिया है) ।",
                    "english_gloss": "aa (come) mil (meet) yaar (beloved) saar (care) lai (take) meri (of mine), meri (my) jaan (soul/life) dukkhaan (sorrows) ne (by) gheri (surrounded) ."
                }
            ],
            "hindi_meaning": kafi_1_hi_meaning,
            "english_meaning": kafi_1_en_meaning
        }
    ]
}

kafi_2_original = """आयो फ़कीरो मेले चलिए, आरफ़ दा सुन वाजा रे ।
अनहद सबद सुनो बहु रंगी, तजीए भेख प्याजा रे ।
अनहद बाजा सरब मिलापी, निरवैरी सिरनाजा रे ।
मेले बाझों मेला औतर, रुढ़ ग्या मूल व्याजा रे ।
कठिन फ़कीरी रसता आशक, कायम करो मन बाजा रे ।
बन्दा रब्ब ब्रिहों  इक मगर सुख, बुल्हा पड़ जहान बराजा रे ।"""

kafi_2_hi_meaning = """आओ फकीरो, उस मेले चलें,
ज्ञानी पीर का बाजा सुनकर चलें!

अनाहत शब्द सुनो बहुरंगी,
छोड़ो सारे भेष और ढोंग-पाखंडी!
अनाहत बाजा सबको मिलाता,
वैर-रहित, सिरताज कहलाता!

सच्चे मिलन बिन यह मेला है सूना,
मूल और ब्याज सब बह जाएगा दूना!
कठिन फकीरी का मार्ग है प्रेमी,
मन के बाजे को स्थिर करो नेमी!

विरह की तपन में आत्मा-प्रभु एक हों,
संसार का प्रपंच छोड़, बुल्ले के बोल सच हों!"""

kafi_2_en_meaning = """Come, O dervishes, let us to the gathering go,
Hearing the mystic flute softly blow!

Listen to the unstruck celestial sound,
Cast off the false robes of deceit around!
This unstruck music all hearts will bind,
Free from all malice, supreme of its kind!

Without the Beloved, this carnival is vain,
Both principal and interest are washed in pain!
Arduous is the lover's dervish way,
Attune your mind, do not go astray!

In the fire of longing, soul and Lord are one,
Rise above worldly shadows, the quest is won!"""

kafi_2_data = {
    "id": 2,
    "title": "2. आओ फ़कीरो मेले चलिए",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": kafi_2_original,
    "annotated_stanzas": [
        {
            "lines": [
                {
                    "original": "आयो फ़कीरो मेले चलिए, आरफ़ दा सुन वाजा रे ।",
                    "hindi_gloss": "आयो (आओ) फ़कीरो (हे फकीरों/साधकों) मेले (सत्संग/मिलन के मेले में) चलिए (चलें), आरफ़ (ज्ञानी/ब्रह्मवेत्ता) दा (का) सुन (सुनकर) वाजा (बाजा/नाद) रे (रे) ।",
                    "english_gloss": "aayo (come) fakeero (O seekers/dervishes) mele (to the spiritual fair/gathering) chaliye (let us go), aaraf (of the enlightened gnostic) da (of) sun (hearing) vaaja (music/instrument) re (O friend) ."
                },
                {
                    "original": "अनहद सबद सुनो बहु रंगी, तजीए भेख प्याजा रे ।",
                    "hindi_gloss": "अनहद (अनाहत/असीम) सबद (शब्द/नाद) सुनो (सुनो) बहु (अनेक) रंगी (रंगों/छवियों वाला), तजीए (त्याग दें) भेख (पाखंडी भेष) प्याजा (दिखावे का/छलपूर्ण) रे (रे) ।",
                    "english_gloss": "anhad (unstruck/boundless) sabad (celestial sound/word) suno (listen to) bahu (many) rangi (colorful/wondrous), tajiye (let us renounce) bhekh (guises/robes) pyaaja (hypocritical/pretentious) re (O friend) ."
                },
                {
                    "original": "अनहद बाजा सरब मिलापी, निरवैरी सिरनाजा रे ।",
                    "hindi_gloss": "अनहद (अनाहत) बाजा (संगीत/बाजा) सरब (सबको) मिलापी (मिलाने/एकाकार करने वाला), निरवैरी (वैर-रहित) सिरनाजा (सर्वश्रेष्ठ/मुकुटमणि) रे (रे) ।",
                    "english_gloss": "anhad (unstruck) baaja (divine instrument) sarab (with all) milaapi (unifying/harmonizing), nirvairi (free from malice) sirnaaja (supreme/crowning glory) re (O friend) ."
                },
                {
                    "original": "मेले बाझों मेला औतर, रुढ़ ग्या मूल व्याजा रे ।",
                    "hindi_gloss": "मेले (प्रभु-मिलन) बाझों (के बिना) मेला (यह संसार रूपी मेला) औतर (व्यर्थ/बांझ), रुढ़ (बह) ग्या (गया) मूल (मूलधन/यह जीवन) व्याजा (ब्याज/कर्म-फल) रे (रे) ।",
                    "english_gloss": "mele (divine union) baajhon (without) mela (this worldly carnival) autar (barren/fruitless), rudh (swept away) gya (has gone) mool (principal/life) vyaaja (interest/merits) re (O friend) ."
                },
                {
                    "original": "कठिन फ़कीरी रसता आशक, कायम करो मन बाजा रे ।",
                    "hindi_gloss": "कठिन (दुर्गम/कठिन) फ़कीरी (फकीरी/त्याग का) रसता (मार्ग) आशक (हे प्रेमी), कायम (स्थिर/अडिग) करो (करो) मन (मन के) बाजा (बाजे/ध्यान को) रे (रे) ।",
                    "english_gloss": "kathin (arduous/difficult) fakeeri (of renunciation/dervishhood) rasta (path) aashak (O lover), kaayam (steady/resolute) karo (make) man (of mind) baaja (instrument/focus) re (O friend) ."
                },
                {
                    "original": "बन्दा रब्ब ब्रिहों  इक मगर सुख, बुल्हा पड़ जहान बराजा रे ।",
                    "hindi_gloss": "बन्दा (जीवात्मा/मानव) रब्ब (परमात्मा) ब्रिहों (प्रेम-विरह में) इक (एकाकार/एक) मगर (तभी) सुख (सच्चा सुख), बुल्हा (बुल्ला) पड़ (पार पाकर) जहान (संसार के) बराजा (प्रपंच/दिखावे को) रे (रे) ।",
                    "english_gloss": "banda (human seeker) rabb (the Lord) brihon (in the pangs of separation) ik (one/united) magar (only then) sukh (true bliss), bullha (Bulleh) pad (surpassing/transcending) jahaan (of world) baraaja (carnival/illusions) re (O friend) ."
                }
            ],
            "hindi_meaning": kafi_2_hi_meaning,
            "english_meaning": kafi_2_en_meaning
        }
    ]
}

with open(os.path.join(KAFIAN_DIR, "kafi_001.json"), "w", encoding="utf-8") as f:
    json.dump(kafi_1_data, f, ensure_ascii=False, indent=2)

with open(os.path.join(KAFIAN_DIR, "kafi_002.json"), "w", encoding="utf-8") as f:
    json.dump(kafi_2_data, f, ensure_ascii=False, indent=2)

print("Updated kafi_001.json and kafi_002.json with original poem and verse-line-break poetic translations.")
