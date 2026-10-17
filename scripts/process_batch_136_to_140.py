"""
Process Batch 136 to 140 of Bulleh Shah's Kafian.
Kafi 136: सानूं आ मिल यार प्यारिआ (Come Meet Me, O Beloved Friend)
Kafi 137: सईयो हुन मैं साजन पाइओ ई (O Friends, Now I Have Found My Beloved)
Kafi 138: से वणजारे आए नी माए, से वणजारे आए (Those Jewel-Merchants Have Arrived, O Mother!)
Kafi 139: सुनो तुम इश्क की बाज़ी, मलायक है कहां राज़ी (Listen to the Cosmic Wager of Love)
Kafi 140: तैं कित पर पाउं पसारा ए (Why Have You Spread Your Feet in Heedless Slumber?)
"""

import json
import os

DATA_DIR = os.path.abspath("c:/my-code/Bulleh-Shah/data")
KAFIAN_DIR = os.path.join(DATA_DIR, "kafian")
LEXICON_PATH = os.path.join(DATA_DIR, "punjabi_sufi_lexicon.json")
CHECKPOINT_PATH = os.path.join(DATA_DIR, "checkpoint.json")

batch_kafian = [
    {
        "id": 136,
        "title_punjabi": "सानूं आ मिल यार प्यारिआ",
        "title_english": "Come Meet Me, O Beloved Friend",
        "raga": "Raga Kafi / Pahadi",
        "meter": "Matrik Chhand (16-14 matras)",
        "theme": "Historical Turmoil as Cosmic Estrangement & Plea for Spiritual Sanctuary",
        "historical_context": "Composed during the tumultuous 18th century in Punjab, marked by Nadir Shah and Ahmad Shah Abdali's invasions, the collapse of Mughal central authority, widespread looting, and social unraveling coinciding with the end of the 11th and dawn of the 12th Islamic century (Hijri 12th century / 18th CE). Bulleh Shah uses this external apocalyptic chaos ('बुरा हाल होया पंजाब दा') as a mirror of inner existential desperation, pleading with Shah Inayat to grant refuge.",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "दूर दूर असाथों ग्युं, अजला (अरशां) ते आ के बह रहउं,  ",
                    "की कसर कसूर विसारिआ, सानूं आ मिल यार प्यारिआ ।"
                ],
                "hindi_gloss": "दूर (दूर) दूर (दूर) असाथों (हमसे) ग्युं (चले गए हो), अजला/अरशां (अनंत आकाशों/सिंहासन) ते (पर) आ (आकर) के बह (बैठ) रहउं (रहे हो), की (क्या) कसर (कमी) कसूर (अपराध) विसारिआ (देखकर भुला दिया), सानूं (हमें) आ (आकर) मिल (मिलो) यार (सखे) प्यारिआ (प्यारे Beloved)।",
                "english_gloss": "दूर (Far) दूर (far) असाथों (from us) ग्युं (you have gone), अजला/अरशां (on the highest celestial spheres/throne) ते (upon) आ के (having come) बह रहउं (seated you remain), की (what) कसर (shortcoming) कसूर (fault/transgression) विसारिआ (having seen you forgot/abandoned us), सानूं (to us) आ (come) मिल (meet) यार (friend) प्यारिआ (O beloved).",
                "poetic_hindi": "दूर बहुत हमसे तुम भागे, अर्शों पर जा आसन साधे,\nकिस खता पे दिल से बिसारा? आ मिल मुझको यार पियारे!",
                "poetic_english": "Far, so far from us You have flown, enthroned above the heavens alone;\nFor what transgression am I cast aside? Come meet me, O Beloved guide!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "मेरा इक अनोखा यार है, मेरा ओसे नाल प्यार है,  ",
                    "किवें समझें वड परवाइआ, सानूं आ मिल यार प्यारिआ ।"
                ],
                "hindi_gloss": "मेरा (मेरा) इक (एक) अनोखा (अद्भुत/अद्वितीय) यार (सखा) है (है), मेरा (मेरा) ओसे (उसी) नाल (के साथ) प्यार (प्रेम) है (है), किवें (कैसे) समझें (समझेगा) वड (महान/बेपरवाह) परवाइआ (सर्वथा स्वाधीन बेपरवाह प्रभु), सानूं (हमें) आ (आकर) मिल (मिलो) यार (सखे) प्यारिआ (प्यारे)।",
                "english_gloss": "मेरा (My) इक (one) अनोखा (wondrous/peerless) यार (Beloved Friend) है (is), मेरा (my) ओसे (with Him alone) नाल (with) प्यार (love) है (is), किवें (how) समझें (shall He perceive) वड (immensely) परवाइआ (indifferent/carefree Supreme Master), सानूं (to us) आ (come) मिल (meet) यार (friend) प्यारिआ (beloved).",
                "poetic_hindi": "एक अनोखा प्रीतम मेरा, उस संग नाता अति गहरा,\nकैसे जाने बेपरवाह हमारा? आ मिल मुझको यार पियारे!",
                "poetic_english": "A wondrous Friend is mine alone, my heart beats solely for His throne;\nYet utterly heedless He seems to abide—come meet me, O Beloved guide!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "जदों आपनी आपनी पै गई, धी मां नूं लुट्ट के लै गई,  ",
                    "मूंह बाहरवीं सदी पसारिआ, सानूं आ मिल यार प्यारिआ ।"
                ],
                "hindi_gloss": "जदों (जब) आपनी (अपनी-अपनी) आपनी (जान की) पै गई (पड़ गई), धी (बेटी) मां (माता) नूं (को) लुट्ट (लूट) के (कर) लै गई (ले गई), मूंह (मुख) बाहरवीं (बारहवीं) सदी (सदी हिजरी ने) पसारिआ (फैलाया भयंकर रूप से), सानूं (हमें) आ (आकर) मिल (मिलो) यार (सखे) प्यारिआ (प्यारे)।",
                "english_gloss": "जदों (When) आपनी आपनी (each-for-himself frenzy) पै गई (befell every soul), धी (daughter) मां नूं (the mother) लुट्ट के (plundering) लै गई (dragged away), मूंह (its maw/jaws) बाहरवीं सदी (the twelfth century AH) पसारिआ (spread wide open), सानूं (to us) आ (come) मिल (meet) यार (friend) प्यारिआ (beloved).",
                "poetic_hindi": "अपनी-अपनी जान पड़ी है, माँ-बेटी भी लूट खड़ी है,\nबारहवीं सदी ने जब मुँह पसारा, आ मिल मुझको यार पियारे!",
                "poetic_english": "When selfish panic seized each soul, and daughters plundered mothers whole,\nThe twelfth century oped its fiery maw wide—come meet me, O Beloved guide!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "दर खुल्ल्हा हशर अज़ाब दा, बुरा हाल होया पंजाब दा,  ",
                    "डर हावीए दोज़ख मारिआ, सानूं आ मिल यार प्यारिआ ।"
                ],
                "hindi_gloss": "दर (द्वार) खुल्ल्हा (खुल गया) हशर (प्रलय/कयामत के) अज़ाब (यातना) दा (का), बुरा (अति दयनीय) हाल (दशा) होया (हो गई) पंजाब (पंजाब प्रान्त) दा (की), डर (भय ने) हावीए (हाविया नामक रौरव नरक की) दोज़ख (दोजख की आग ने) मारिआ (त्रस्त कर दिया), सानूं (हमें) आ (आकर) मिल (मिलो) यार (सखे) प्यारिआ (प्यारे)।",
                "english_gloss": "दर (The gateway) खुल्ल्हा (opened wide) हशर (of the Day of Reckoning's) अज़ाब दा (torment), बुरा हाल (ruined state) होया (has become) पंजाब दा (of Punjab), डर (the dread of) हावीए (the lowest pit of Hell, Hawiyah) दोज़ख (inferno) मारिआ (has struck down with terror), सानूं (to us) आ (come) मिल (meet) यार (friend) प्यारिआ (beloved).",
                "poetic_hindi": "खुला है अज़ाब-ए-हशर का द्वार, पंजाब हुआ है तार-ओ-तार,\nदोजख-ए-हाविया ने डस डारा, आ मिल मुझको यार पियारे!",
                "poetic_english": "The gates of Judgment's agony blow wide, in bloody ruins Punjab must abide;\nThe dread pit of Hawiyah burns on every side—come meet me, O Beloved guide!"
            },
            {
                "stanza_number": 5,
                "original": [
                    "बुल्ल्हा शहु मेरे घर आवसी, मेरी बलदी भा बुझावसी,  ",
                    "इनायत दमदम नाल चितारिआ, सानूं आ मिल यार प्यारिआ ।"
                ],
                "hindi_gloss": "बुल्ल्हा (बुल्लेशाह कहता है) शहु (प्रभु-प्रियतम) मेरे (मेरे) घर (हृदय-गृह) आवसी (आएगा), मेरी (मेरी) बलदी (सुलगती हुई) भा (विरह की आग) बुझावसी (बुझाएगा), इनायत (मुर्शिद शाह इनायत को) दमदम (प्रत्येक श्वास) नाल (के साथ) चितारिआ (स्मरण किया है), सानूं (हमें) आ (आकर) मिल (मिलो) यार (सखे) प्यारिआ (प्यारे)।",
                "english_gloss": "बुल्ल्हा (Bulleh says) शहु (the Lord-Beloved) मेरे घर (to my courtyard) आवसी (will come), मेरी (my) बलदी (blazing) भा (fire of separation) बुझावसी (will quench), इनायत (Murshid Shah Inayat) दमदम नाल (with every single breath) चितारिआ (I have remembered/invoked), सानूं (to us) आ (come) मिल (meet) यार (friend) प्यारिआ (beloved).",
                "poetic_hindi": "बुल्ल्हा कहे, शाह घर आए, जलती विरह-अग्नि बुझाए,\nदम-दम इनायत को पुकारा, आ मिल मुझको यार पियारे!",
                "poetic_english": "Bulleh says: the King will grace my door, and quench the blaze within my core;\nWith every breath Inayat's name is cried—come meet me, O Beloved guide!"
            }
        ],
        "sufi_commentary": "Kafi 136 is of immense historical and mystical significance. Bulleh Shah directly addresses the collapse of civil order during the 18th century CE (12th Hijri century, 'मूंह बाहरवीं सदी पसारिआ'). The invasion of Nadir Shah in 1739 and the recurring carnage by Ahmad Shah Durrani turned Punjab into an apocalyptic battlefield ('बुरा हाल होया पंजाब दा'), breaking all familial ties and societal decencies ('धी मां नूं लुट्ट के लै गई'). In Sufi metaphysics, such cosmic crises and collective destructions are manifestations of Jalal (Divine Rigor and Wrath) where human beings are stripped of superficial pride and worldly illusions. In this terrifying twilight, Bulleh turns neither to earthly rulers nor dogmatic clerics, but to his supreme refuge—the Eternal Beloved manifested in Murshid Shah Inayat ('इनायत दमदम नाल चितारिआ'). Through constant zikr ('दमदम'), the burning fires of worldly suffering and hellish dread ('हावीए दोज़ख') are transformed into the sanctifying waters of spiritual union."
    },
    {
        "id": 137,
        "title_punjabi": "सईयो हुन मैं साजन पाइओ ई",
        "title_english": "O Friends, Now I Have Found My Beloved",
        "raga": "Raga Bilawal / Bhairavi",
        "meter": "Dohra / Hazaj variant",
        "theme": "The Theophany of Wahdat al-Wujud across Quranic Ayaat & Islamic Mystical History",
        "historical_context": "One of the most erudite and daring master-kafian in the entire Punjabi mystical corpus. Bulleh Shah synthesizes the classic hadith qudsi ('Kuntu Kanzan Makhfiyyan'), the primordial covenant ('Alastu bi-Rabbikum'), Quranic revelations (Fa-aynama tuwallu fa-tsamma wajhullah, Nahnu aqrabu, Wa fee anfusikum), and the ecstasy of Mansur al-Hallaj and Junayd of Baghdad, celebrating the non-dual revelation that Hari and Allah are One Reality manifest within every human heart.",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "सईयो हुन मैं साजन पाइओ ई ।  ",
                    "हरि हर दे विच्च समाइओ ई ।"
                ],
                "hindi_gloss": "सईयो (हे सखियों!) हुन (अब) मैं (मैंने) साजन (परम प्रियतम को) पाइओ ई (पा लिया है)। हरि (भगवान हरि) हर (प्रत्येक घट) दे विच्च (के भीतर) समाइओ ई (समाया हुआ है)।",
                "english_gloss": "सईयो (O companions/friends!) हुन (now) मैं (I) साजन (the Beloved) पाइओ ई (have found). हरि (The Supreme Lord Hari) हर (every single heart/form) दे विच्च (within) समाइओ ई (is wholly pervading).",
                "poetic_hindi": "सखियों! अब मैंने प्रीतम पाया,\nहरि हर घट के बीच समाया!",
                "poetic_english": "O companions, now the Beloved I have found!\nIn every form Hari's mysteries abound!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "अनाअहद दा गीत सुणाइओ,  ",
                    "अना अहमद हूं फिर फरमाइओ,  ",
                    "अनाअरब बे ऐन बताइओ,  ",
                    "फिर नाम रसूल धराइओ ई ।  ",
                    "सईयो हुन मैं साजन पाइओ ई ।"
                ],
                "hindi_gloss": "अनाअहद (अहद - 'मैं अद्वितीय परब्रह्म हूँ') दा (का) गीत (गान) सुणाइओ (सुनाया), अना अहमद हूं ('मैं अहमद हूँ') फिर (पुनः) फरमाइओ (फरमाया/कहा), अनाअरब ('मैं निष्कलंक अरब हूँ' - अरबी बिना 'ऐन' अर्थात रब) बे ऐन (बिना ऐन अक्षर के रब बन जाना) बताइओ (दर्शाया), फिर (फिर) नाम (नाम) रसूल (पैगंबर) धराइओ ई (धारण किया)।",
                "english_gloss": "अनाअहद ('I am the One Indivisible Absolute') दा (of) गीत (song) सुणाइओ (He sang), अना अहमद हूं ('I am Ahmad') फिर (then) फरमाइओ (He decreed), अनाअरब ('I am Arab' without the letter 'Ayn', revealing 'Rabb') बे ऐन (without Ayn) बताइओ (He revealed), फिर (then) नाम रसूल (the name of Messenger) धराइओ ई (He assumed).",
                "poetic_hindi": "'अना-अहद' का तराना गाया, फिर 'अहमद' कह रूप दिखाया,\n'अरब' बिना 'ऐन' रब बतलाया, फिर नाम 'रसूल' धराया!",
                "poetic_english": "He sang: 'I am the One, the unmanifest Core,' then spoke: 'I am Ahmad, whom mortals adore!'\nWithout 'Ayn' in Arab, Rabb shines evermore, then assumed as the Prophet His glorious shore!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "फसुमावजउल अल्ल्हाहू नूर तेरा,  ",
                    "हर हर के बीच ज़हूर तेरा,  ",
                    "है अलइनसान मज़कूर तेरा,  ",
                    "एथे आपना सिर्र लोकाइओ ई ।  ",
                    "सईयो हुन मैं साजन पाइओ ई ।"
                ],
                "hindi_gloss": "फसुमावजउल अल्ल्हाहू ('फा-अयना-मा तुवल्लू फा-तम्मा वज्हुल्लाह' - जहाँ भी मुड़ो वहीं अल्लाह का चेहरा है) नूर (दिव्य प्रकाश) तेरा (तेरा), हर हर (प्रत्येक कण/हृदय) के बीच (के मध्य) ज़हूर (प्रत्यक्ष प्रकटीकरण) तेरा (तेरा), है (है) अलइनसान ('अल-इंसान सिर्री वा अना सिर्रुहु' - मनुष्य मेरा गुप्त भेद है) मज़कूर (चर्चा/उल्लेख) तेरा (तेरा), एथे (यहाँ) आपना (अपना) सिर्र (रहस्य/राज़) लोकाइओ ई (छिपाया है)।",
                "english_gloss": "फसुमावजउल अल्ल्हाहू ('Whithersoever ye turn, there is the Face of God') नूर तेरा (Thy radiant light), हर हर के बीच (in every single being) ज़हूर तेरा (Thy clear manifestation), है अलइनसान (Man is Thy mention/secret) मज़कूर तेरा (Thy eternal subject), एथे (here in humanity) आपना सिर्र (Thy intimate Mystery) लोकाइओ ई (Thou hast concealed).",
                "poetic_hindi": "'फ-तम्मा वज्हुल्लाह' नूर तुम्हारा, हर इक रूप में जलवा पसारा,\n'इंसान' बना कर भेद सँवारा, इस मिट्टी में सिर्र को छुपाया!",
                "poetic_english": "'Whithersoever ye turn, God's countenance glows'; through every creation Thy majesty flows;\nIn 'Man' as Thy mirror the mystery grows, where the hiddenmost Secret in silence repose!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "तूं आइउं ते मैं ना आई,  ",
                    "गंज मख़फ़ी दी तैं मुरली बजाई,  ",
                    "आख अलस्सत गवाही चाही,  ",
                    "ओथे कालाबूला सुणाययो ई ।  ",
                    "सईयो हुन मैं साजन पाइओ ई ।"
                ],
                "hindi_gloss": "तूं (तू) आइउं (प्रकट हुआ) ते (और) मैं (मेरा पृथक अहंकार) ना आई (समाप्त हो गया/नहीं रहा), गंज मख़फ़ी ('कुन्तु कन्ज़न मख़फ़िय्यन' - मैं एक गुप्त खजाना था) दी (की) तैं (तूने) मुरली (बांसुरी) बजाई (बजाई), आख (कहकर) अलस्सत ('अलस्तु बि-रब्बिकुम' - क्या मैं तुम्हारा रब नहीं?) गवाही (साक्षी) चाही (मांगी), ओथे (वहाँ) कालाबूला ('कालू बला' - उन्होंने कहा: हाँ, तू ही है!) सुणाययो ई (सबने स्वीकार किया)।",
                "english_gloss": "तूं (Thou) आइउं (came forth) ते (and) मैं (my ego) ना आई (ceased to exist), गंज मख़फ़ी ('I was a Hidden Treasure') दी (of) तैं (Thou) मुरली (flute) बजाई (played), आख (saying) अलस्सत ('Alastu bi-Rabbikum' - Am I not your Lord?) गवाही (witness) चाही (sought), ओथे (there) कालाबूला ('Qalu Bala' - They said: Yea, indeed!) सुणाययो ई (Thou caused all to proclaim).",
                "poetic_hindi": "तू ही आया, मैं मिट पाई, गुप्त खजाने की मुरली बजाई,\nपूछ 'अलस्त' गवाही चाही, सबने 'कालू बला' सुनाया!",
                "poetic_english": "Thou alone didst arise, my ego untied, the flute of the 'Hidden Treasure' Thou plied;\n'Am I not your Lord?' to creation Thou cried, and 'Truly Yea!' all spirits replied!"
            },
            {
                "stanza_number": 5,
                "original": [
                    "परगट हो कर नूर सदाइओ,  ",
                    "अहमद तों मौजूद कराइओ,  ",
                    "नाबूदों कर बूद दिखलाइओ,  ",
                    "फ़नफ़ख़तोफ़ी ही सुणाइओ ई ।  ",
                    "सईयो हुन मैं साजन पाइओ ई ।"
                ],
                "hindi_gloss": "परगट (प्रत्यक्ष) हो कर (होकर) नूर (नूर-ए-इलाही) सदाइओ (कहलाया), अहमद तों (अहमद/हकीकत-ए-मुहम्मदिया से) मौजूद (समस्त सृष्टि को अस्तित्व में) कराइओ (लाया), नाबूदों (अभाव/शून्यता से) कर बूद (अस्तित्व/हस्ती) दिखलाइओ (प्रकट किया), फ़नफ़ख़तोफ़ी ही ('फा-नफख्ना फीही मिन रूहिना' - और हमने उसमें अपनी रूह फूंकी) सुणाइओ ई (घोषणा की)।",
                "english_gloss": "परगट हो कर (Manifesting openly) नूर (as primordial Light) सदाइओ (Thou called Thyself), अहमद तों (through Ahmad's reality) मौजूद कराइओ (brought all into existence), नाबूदों (from non-being) कर बूद (into being) दिखलाइओ (revealed), फ़नफ़ख़तोफ़ी ही ('And I breathed into him of My Spirit') सुणाइओ ई (Thou declared).",
                "poetic_hindi": "प्रगट हुआ तो नूर कहाया, अहमद से संसार रचाया,\nशून्य से हस्ती का रूप सजाया, 'फ-नफख्तो' का मर्म जताया!",
                "poetic_english": "Manifested as Light, Thy splendor arose, through Ahmad the dawn of creation arose;\nFrom nothingness being in brilliance arose, 'I breathed of My Spirit' Thy mystery prose!"
            },
            {
                "stanza_number": 6,
                "original": [
                    "नाहनअकरब लिख दित्तोई,  ",
                    "हूवामअकुम सबक दित्तोई,  ",
                    "वफ़ियनफ़ुसकुम हुकम कीतोई,  ",
                    "फिर केहा घुंघट पाइओ ई ।  ",
                    "सईयो हुन मैं साजन पाइओ ई ।"
                ],
                "hindi_gloss": "नाहनअकरब ('नहनु अकरबु इलैहि मिन हबलिल वरीद' - हम तुम्हारी प्राण-नस से भी अधिक निकट हैं) लिख दित्तोई (तूने ग्रंथ में लिख दिया), हूवामअकुम ('व हुवा म'अकुम अय्नमा कुन्तुम' - और जहाँ भी तुम हो वह तुम्हारे साथ है) सबक (पाठ) दित्तोई (तूने सिखाया), वफ़ियनफ़ुसकुम ('व फी अन्फुसिकुम अफाला तुब्सिरून' - और वह तुम्हारी आत्माओं के भीतर है, क्या तुम देखते नहीं?) हुकम (आदेश) कीतोई (तूने दिया), फिर (तो फिर) केहा (कैसा) घुंघट (पर्दा) पाइओ ई (तूने डाल रखा है?)।",
                "english_gloss": "नाहनअकरब ('We are nearer to him than his jugular vein') लिख दित्तोई (Thou hast inscribed), हूवामअकुम ('And He is with you wheresoever ye be') सबक दित्तोई (Thou taught as our lesson), वफ़ियनफ़ुसकुम ('And within your own souls, will ye not see?') हुकम कीतोई (Thou didst decree), फिर केहा घुंघट (then what veil is this) पाइओ ई (Thou hast cast over Thyself?).",
                "poetic_hindi": "'नहन-अकरब' का लेख लिखाया, 'हुवा-म'अकुम' का पाठ पढ़ाया,\n'फी-अनफुसिकुम' का भेद बताया, फिर काहे को घूँघट पाया?",
                "poetic_english": "'Nearer than jugular vein' Thou hast writ, 'With you wherever you walk' Thou hast lit;\n'Behold in your souls!' is Thy sovereign decree—then why keep this veil of false mystery free?"
            },
            {
                "stanza_number": 7,
                "original": [
                    "भर के वहदत जाम पिलाइओ,  ",
                    "मनसूर नूं मसत कराइओ,  ",
                    "उस तों अनुलहक्क आप कहाइओ,  ",
                    "फिर सूली पकड़ चढ़ाइओ ई ।  ",
                    "सईयो हुन मैं साजन पाइओ ई ।"
                ],
                "hindi_gloss": "भर के (भर-भर कर) वहदत (अद्वैत/एकेश्वरत्व का) जाम (प्याला) पिलाइओ (तूने पिलाया), मनसूर नूं (मनसूर अल-हल्लाज को) मसत (मस्त-बेखुद) कराइओ (कर दिया), उस तों (उसी के मुख से) अनुलहक्क ('अनल-हक' - मैं ही परम सत्य/ईश्वर हूँ) आप (स्वयं) कहाइओ (कहलवाया), फिर (और फिर) सूली (फांसी के तख्ते पर) पकड़ (पकड़कर) चढ़ाइओ ई (तूने चढ़ा दिया)।",
                "english_gloss": "भर के (Filling to brim) वहदत जाम (the goblet of Divine Oneness) पिलाइओ (Thou made him drink), मनसूर नूं (Mansur Hallaj) मसत कराइओ (made intoxicated), उस तों (through him) अनुलहक्क ('Anal Haq' - I am the Truth) आप (Thyself) कहाइओ (caused to utter), फिर (and then) सूली (upon the gallows) पकड़ (grasping) चढ़ाइओ ई (Thou hanged him).",
                "poetic_hindi": "एकत्व का भर-भर जाम पिलाया, मंसूर को अलमस्त बनाया,\nमुख से 'अनल-हक' आप कहाया, फिर सूली पे पकड़ चढ़ाया!",
                "poetic_english": "The chalice of Oneness Thou gavest to drink, plunging Mansur past mortality's brink;\n'I am the Truth!' through his lips Thou didst cry, then hoisted him high on the gallows to die!"
            },
            {
                "stanza_number": 8,
                "original": [
                    "घुंघट खोल्ह जमाल विखाइआ,  ",
                    "शैख जुनैद कमाल सदाइआ,  ",
                    "लैशाफ़ीजन्नेती हाल बणाइआ,  ",
                    "अशरफ इनसान बणाइओ ई ।  ",
                    "सईयो हुन मैं साजन पाइओ ई ।"
                ],
                "hindi_gloss": "घुंघट (घूँघट) खोल्ह (खोलकर) जमाल (दिव्य सौन्दर्य) विखाइआ (दिखाया), शैख (शेख) जुनैद (बगदादी को) कमाल (परम सिद्ध/पूर्ण) सदाइआ (कहलवाया), लैशाफ़ीजन्नेती ('लैसा फी जुब्बती सिवा अल्लाह' - मेरी गुदड़ी में सिवाय खुदा के कुछ नहीं) हाल (आध्यात्मिक अवस्था) बणाइआ (बनाई), अशरफ (सर्वश्रेष्ठ/अशरफुल मखलूकात) इनसान (मानव को) बणाइओ ई (तूने रचा)।",
                "english_gloss": "घुंघट खोल्ह (Lifting the veil) जमाल विखाइआ (revealed Divine Beauty), शैख जुनैद (Shaikh Junayd of Baghdad) कमाल सदाइआ (proclaimed as supreme perfection), लैशाफ़ीजन्नेती ('There is nothing in my robe save God') हाल बणाइआ (made his mystical station), अशरफ इनसान ('The Noblest of Creation') बणाइओ ई (Thou fashioned human beings).",
                "poetic_hindi": "घूँघट खोल जमाल दिखाया, शैख जुनैद को सिद्ध बनाया,\n'लैस फी जुब्बती' हाल सजाया, अशरफ इंसान बनाया!",
                "poetic_english": "Unveiling Thy Beauty in transcendent grace, Junayd found perfection in Thy holy embrace;\n'Naught in my cloak except God' did he trace, making Man the crown of creation's place!"
            },
            {
                "stanza_number": 9,
                "original": [
                    "वलकदकरमना याद कराइओ,  ",
                    "ला इल्लाहा दा परदा लाइओ,  ",
                    "इल्लअल्ल्हाहू कहो झाती पाइओ,  ",
                    "फिर बुल्ल्हा (भुल्ला) नाम धराइओ ई ।  ",
                    "सईयो हुन मैं साजन पाइओ ई ।  ",
                    "हरि हर दे विच्च समाइओ ई ।"
                ],
                "hindi_gloss": "वलकदकरमना ('व लकद कर्रम्ना बनी आदमा' - और हमने आदम की संतान को महिमामंडित किया) याद (स्मरण) कराइओ (कराया), ला इल्लाहा ('ला इलाहा' - कोई अन्य ईश्वर नहीं, केवल निषेध) दा (का) परदा (परदा) लाइओ (लगाया), इल्लअल्ल्हाहू ('इल्लल्लाह' - केवल अल्लाह ही शाश्वत सत्य है) कहो (कहते ही) झाती (अपनी प्रत्यक्ष झांकी) पाइओ (दिखाई), फिर (फिर) बुल्ल्हा/भुल्ला (भटका हुआ या बुल्लेशाह) नाम (नाम) धराइओ ई (रखा)।",
                "english_gloss": "वलकदकरमना ('And We have honored the children of Adam') याद कराइओ (Thou reminded us), ला इल्लाहा ('There is no god' - the veil of cosmic negation) दा परदा लाइओ (Thou cast as a veil), इल्लअल्ल्हाहू ('Except God' - the ultimate affirmation) कहो (saying) झाती पाइओ (Thou peeked/revealed Thyself), फिर (then) बुल्ल्हा/भुल्ला (the wandering Bulleh) नाम धराइओ ई (assumed the humble name).",
                "poetic_hindi": "'कर्रम्ना' कह मान बढ़ाया, 'ला इलाहा' का पर्दा लगाया,\n'इल्लल्लाह' से झाँक दिखाया, फिर 'बुल्ल्हा' नाम धराया!\nसखियों! अब मैंने प्रीतम पाया, हरि हर घट के बीच समाया!",
                "poetic_english": "'We honored Adam's race' Thou didst sing, 'La ilaha' the veil of negation to bring;\nWith 'Illallah' Thou peeked as the Sovereign King, and named Thyself 'Bulleh'—the wandering thing!\nO companions, now the Beloved I have found,\nIn every form Hari's mysteries abound!"
            }
        ],
        "sufi_commentary": "Kafi 137 stands as an absolute summit of Wahdat al-Wujud (Transcendent Non-Duality) in classical Sufi literature, operating seamlessly across the Quranic canon, Hadith Qudsi, and Sufi historical hagiography. Bulleh traces the entire descent (tanazzulat) of Being from the Absolute Unmanifest (Ahad) into Ahmad (the Muhammadan Reality), decoding the sacred cipher that the Arabic word 'Arab' (عرب) without its initial letter 'Ayn' (ع) becomes 'Rabb' (رب)—God Himself. He then marshals seven cardinal Quranic verses of immanence: (1) Fa-aynama tuwallu fa-tsamma wajhullah (2:115), confirming God's Face wherever one turns; (2) Al-Insanu sirri wa ana sirruh; (3) The Primordial Covenant of 'Alastu bi-Rabbikum' (7:172) where all souls answered 'Qalu Bala'; (4) Wa nafakhtu feehi min roohi (15:29), the inbreathing of the Divine Spirit into human clay; (5) Nahnu aqrabu ilayhi min hablil-warid (50:16); (6) Wa huwama'akum aynama kuntum (57:4); and (7) Wa fee anfusikum afala tubsirun (51:21). He recalls Mansur al-Hallaj's ecstasy of 'Anal Haq' and martyrdom on the gibbet, alongside Junayd's theophany of 'Laysa fee jubbati siwa Allah'. Finally, he proclaims the supreme synthesis: this transcendent Mystery is none other than 'Hari' indwelling every human heart ('हरि हर दे विच्च समाइओ ई'), veiling and unveiling Himself until He plays the role of the humble seeker named Bulleh Shah."
    },
    {
        "id": 138,
        "title_punjabi": "से वणजारे आए नी माए, से वणजारे आए",
        "title_english": "Those Jewel-Merchants Have Arrived, O Mother!",
        "raga": "Raga Dhanasri / Asa",
        "meter": "Baint / Chhand (16-12 matras)",
        "theme": "The Ruby of Divine Love and the Cost of Spiritual Enlightenment (Severing the Ego)",
        "historical_context": "Drawn from the rich merchant and caravanserai culture of Punjab along the Silk Road, Bulleh Shah employs the allegory of jewel merchants (vanjare) who arrive in the village selling priceless rubies (spiritual illumination / divine love). When the unprepared seeker enters the market thinking gold or social status can purchase these rubies, she is confronted with the ultimate spiritual price: the offering of one's own severed head (complete ego-annihilation, Fana).",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "से वणजारे आए नी माए, से वणजारे आए ।  ",
                    "लालां दा उह वनज करेंदे, होका आख सुणाए ।"
                ],
                "hindi_gloss": "से (वे दिव्य) वणजारे (व्यापारी/सौदागर) आए (आए हैं) नी माए (हे मेरी माँ!), से (वे) वणजारे (सौदागर) आए (आए हैं)। लालां (रत्नों/माणिक्यों/रूबी) दा (का) उह (वे) वनज (व्यापार) करेंदे (करते हैं), होका (पुकार/घोषणा) आख (कहकर) सुणाए (सुना रहे हैं)।",
                "english_gloss": "से (Those) वणजारे (jewel-merchants) आए (have arrived) नी माए (O mother!), से वणजारे आए (those jewel-traders have arrived). लालां दा (In priceless rubies) उह (they) वनज करेंदे (trade), होका आख (shouting their street-cry) सुणाए (they make heard).",
                "poetic_hindi": "वे सौदागर आए री माई, वे सौदागर आए,\nरत्नों का व्यापार करें हैं, हाक लगा सुनाए!",
                "poetic_english": "Those jewel-merchants have arrived, O mother, their caravans draw near;\nTrading in radiant rubies of love, their clarion call sounds clear!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "लाल ने गहने सोने साथी, माए नाल लै जावां,  ",
                    "सुण्या होका मैं दिल गुज़री, मैं भी लाल ल्यावां,  ",
                    "इक ना इक कन्नां विच पा के, लोकां नूं दिखलावां,  ",
                    "लोक जानन इह लालां वाले, लईआं मैं भरमाए ।  ",
                    "से वणजारे आए नी माए, से वणजारे आए ।"
                ],
                "hindi_gloss": "लाल (रत्न) ने (हैं) गहने (आभूषण) सोने (स्वर्ण के) साथी (साथी), माए (माँ) नाल (साथ) लै जावां (ले जाऊं), सुण्या (सुना) होका (पुकार) मैं (मेरे) दिल (हृदय में) गुज़री (विचार आया), मैं भी (मैं भी) लाल (रत्न) ल्यावां (खरीद लाऊँ), इक ना इक (एक-न-एक) कन्नां विच (कानों में) पा के (पहनकर) लोकां नूं (लोगों को) दिखलावां (दिखाऊँ), लोक (लोग) जानन (जानें कि) इह (यह) लालां वाले (रत्नों वाली रानी है), लईआं (मैं) मैं भरमाए (सबको भ्रमित करूँ/प्रभावित करूँ)।",
                "english_gloss": "लाल (Rubies) ने गहने (are ornaments) सोने साथी (companions of gold), माए (mother) नाल (with me) लै जावां (let me take), सुण्या होका (hearing the call) मैं दिल गुज़री (the thought passed my heart), मैं भी (I too) लाल ल्यावां (may bring a ruby), इक ना इक (one at least) कन्नां विच पा के (wearing in my ears) लोकां नूं दिखलावां (show off to people), लोक जानन (people will deem) इह लालां वाले (she possesses rubies), लईआं मैं भरमाए (I will bewitch and impress them all).",
                "poetic_hindi": "सोने-गहने संग लाल लूँ, माँ! मैं भी ले आऊँ,\nकानों में चमका कर जग को अपनी शान दिखाऊँ;\nलोग कहें 'यह लालों वाली', सब पर धाक जमाऊँ,\nवे सौदागर आए री माई, वे सौदागर आए!",
                "poetic_english": "Gold and gems are treasures fine; mother, let me buy and wear;\nI thought I too would fetch a ruby to grace my braided hair,\nTo flash within my earlobes, and let the townsfolk stare:\n'Behold the maiden crowned in gems!'—such vanity I'd share!\nThose jewel-merchants have arrived, O mother, their caravans draw near!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "ओड़क जा खलोती उहनां ते, मैं मनों सधराईआं,  ",
                    "भाई वे लालां वालिओ मैंं वी लाल लेवन नूं आईआं,  ",
                    "उहनां भरे सन्दूक विखाले, मैनूं रीझां आईआं,  ",
                    "वेखे लाल सुहाने सारे, इक तों इक सवाए ।  ",
                    "से वणजारे आए नी माए, से वणजारे आए ।"
                ],
                "hindi_gloss": "ओड़क (अंततः) जा (जाकर) खलोती (खड़ी हो गई) उहनां ते (उनके सामने), मैं (मैं) मनों (मन से) सधराईआं (अत्यंत लालायित/इच्छुक थी), भाई वे (हे भाई!) लालां वालिओ (रत्न-व्यापारियों!) मैंं वी (मैं भी) लाल (रत्न) लेवन नूं (लेने के लिए) आईआं (आई हूँ), उहनां (उन्होंने) भरे (भरे हुए) सन्दूक (पेटारे) विखाले (दिखाए), मैनूं (मुझमें) रीझां (तीव्र चाह/उमंग) आईआं (जाग उठीं), वेखे (देखे) लाल (रत्न) सुहाने (सुंदर) सारे (सभी), इक तों इक (एक से बढ़कर एक) सवाए (सवाया/श्रेष्ठतर)।",
                "english_gloss": "ओड़क (At last) जा खलोती (I went and stood) उहनां ते (before them), मैं मनों सधराईआं (my heart filled with longing), भाई वे लालां वालिओ (O brother ruby-merchants!) मैं वी (I too) लाल लेवन नूं (to purchase rubies) आईआं (have come), उहनां (they) भरे सन्दूक (caskets overflowing) विखाले (opened and displayed), मैनूं रीझां आईआं (waves of desire overwhelmed me), वेखे लाल (I beheld the jewels) सुहाने सारे (all exquisitely wondrous), इक तों इक सवाए (each more dazzling than the last).",
                "poetic_hindi": "दौड़ खड़ी जा हाट में उनके, मन में आस सँजोई,\n'हे भाई! मैं लाल खरीदने आई हूँ' मुख बोली;\nखोले पेटारे उन्होंने तो, मैं सुध-बुध खोई,\nएक से बढ़कर एक नगीने, सुंदर रूप समाए!\nवे सौदागर आए री माई, वे सौदागर आए!",
                "poetic_english": "At last I stood before their stalls, with yearning heart so bold:\n'O brother traders, I have come to buy your gems untold!'\nThey flung their heavy caskets wide, a marvel to behold,\nEach ruby grander than the next, outshining sun and gold!\nThose jewel-merchants have arrived, O mother, their caravans draw near!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "भाई वे लालां वाल्या वीरा इन्हां दा मुल्ल दसाईं,  ",
                    "जे तूं आई हैं लाल खरीदन, धड़ तों सीस लहाईं,  ",
                    "डम्ह कदी सूई दा ना सहआ, सिर किथों दिता जाई,  ",
                    "लाज़म हो के मुड़ घर आई, पुच्छन गवांढी आए ।  ",
                    "से वणजारे आए नी माए, से वणजारे आए ।"
                ],
                "hindi_gloss": "भाई वे (हे भाई!) लालां वाल्या (रत्न वाले) वीरा (वीर/भाई!) इन्हां दा (इनका) मुल्ल (मूल्य/कीमत) दसाईं (बताओ), जे (यदि) तूं (तू) आई हैं (आई है) लाल (रत्न) खरीदन (खरीदने), धड़ तों (धड़ से) सीस (सिर) लहाईं (उतार कर भेंट कर), डम्ह (चुभन/डंक) कदी (कभी) सूई दा (एक सुई की भी) ना सहआ (नहीं सही), सिर (अपना मस्तक) किथों (कहाँ से/कैसे) दिता जाई (दिया जा सके?), लाज़म/लाचार (लज्जित/विवश) हो के (होकर) मुड़ (लौटकर) घर (घर) आई (आ गई), पुच्छन (पूछने) गवांढी (पड़ोसी) आए (आए)।",
                "english_gloss": "भाई वे लालां वाल्या वीरा (O brother jewel-merchant!) इन्हां दा मुल्ल (their price) दसाईं (kindly tell), जे तूं आई हैं (if thou hast come) लाल खरीदन (to buy rubies), धड़ तों (from thy torso) सीस लहाईं (sever thy head and offer it), डम्ह (prick) कदी (ever) सूई दा (of a needle) ना सहआ (I never endured), सिर किथों दिता जाई (how could I give my head?), लाज़म/शर्मिंदा (humiliated and empty-handed) हो के (becoming) मुड़ घर आई (I returned home), पुच्छन (to inquire) गवांढी आए (the neighbors came).",
                "poetic_hindi": "'भाई! इन रत्नों की कीमत क्या है, मुझे बताओ?';\n'खरीदना है तो धड़ से अपना शीश उतार चढ़ाओ!';\nसुई की चुभन न सही कभी, अब शीश कहाँ से लाओ?\nलाचार हो घर लौटी मैं, पूछन पड़ोसी आए!\nवे सौदागर आए री माई, वे सौदागर आए!",
                "poetic_english": "'Tell me the price, O brother trader, what is the ransom due?'\n'If thou hast come to buy our rubies, sever thy head in two!'\nI who could never bear a needle's prick, what could I dare to do?\nShamed and bewildered I crept back home, while neighbors mocked anew!\nThose jewel-merchants have arrived, O mother, their caravans draw near!"
            },
            {
                "stanza_number": 5,
                "original": [
                    "तूं जो गई सैं लाल ख़रीदन, उच्ची अड्डी चाई नी,  ",
                    "केहड़ा मुहरा ओथों रन्ने, तूं लै के घर आई नी,  ",
                    "लाल सी भारे मैं सां हलकी, खाली कन्नी साई नी,  ",
                    "भारा लाल अनमुल्ला ओथों, मैथों चुक्या ना जाए ।  ",
                    "से वणजारे आए नी माए, से वणजारे आए ।"
                ],
                "hindi_gloss": "तूं (तू) जो (जो) गई सैं (गई थी) लाल ख़रीदन (रत्न खरीदने), उच्ची अड्डी चाई नी (एड़ियां उठा-उठा कर इतराती हुई!), केहड़ा (कौन सा) मुहरा (मोहर/रत्न) ओथों (वहाँ से) रन्ने (अरी औरत/सखी!), तूं (तू) लै के (लेकर) घर (घर) आई नी (आई है?), लाल (रत्न) सी (थे) भारे (अति भारी/गंभीर), मैं सां (मैं थी) हलकी (हल्की/छिछली), खाली (खाली) कन्नी (दुपट्टे का कोना) साई नी (लेकर लौटी), भारा (भारी) लाल (रत्न) अनमुल्ला (अमूल्य) ओथों (वहाँ से), मैथों (मुझसे) चुक्या ना जाए (उठाया नहीं गया)।",
                "english_gloss": "तूं जो गई सैं (Thou who went) लाल ख़रीदन (to buy rubies), उच्ची अड्डी चाई नी (strutting with lifted heels on tiptoe!), केहड़ा मुहरा (which jewel/coin) ओथों (from there) रन्ने (O woman!) तूं लै के (hast thou brought) घर आई नी (home?), लाल सी भारे (The rubies were heavy/profound) मैं सां हलकी (I was frivolous and shallow), खाली कन्नी (with an empty veil's hem) साई नी (I returned), भारा लाल (the weighty ruby) अनमुल्ला (priceless) ओथों (from there), मैथों चुक्या ना जाए (could never be lifted by me).",
                "poetic_hindi": "'एड़ियां उठा कर इतराती तू रत्न खरीदने धाई,\nकौन सा हीरा लेकर घर में आई है, ओ माई?';\n'रत्न थे भारी, मैं थी हलकी, खाली पल्ला लाई,\nभारी अमोलक लाल था वो, जो मुझसे उठाया न जाए!'\nवे सौदागर आए री माई, वे सौदागर आए!",
                "poetic_english": "'You strutted forth on high-arched heels to buy the gem of pride;\nWhich jewel of splendor have you brought back to your hearth inside?'\n'The rubies were weighty, I was frail, my empty veil I tied;\nThat priceless gem was far too vast for my weak hands to guide!'\nThose jewel-merchants have arrived, O mother, their caravans draw near!"
            },
            {
                "stanza_number": 6,
                "original": [
                    "कच्ची कच्च वेहाजन जाणां, लाल वेहाजन चल्ली,  ",
                    "पल्ले खरच ना साख ना काई, हत्थों हारन चल्ली,  ",
                    "मैं मोटी मुसटंडी दिस्सां, लाल नूं चारन चल्ली,  ",
                    "जिस शाह ने मुल्ल लै के देणा, सो शाह मूंह ना लाए ।  ",
                    "से वणजारे आए नी माए, से वणजारे आए ।"
                ],
                "hindi_gloss": "कच्ची (कच्ची/अपरिपक्व) कच्च (कांच/नकली पत्थर) वेहाजन (खरीदना) जाणां (जानती थी), लाल (सच्चे माणिक्य) वेहाजन (खरीदने) चल्ली (चल पड़ी), पल्ले (पल्ले में) खरच (खर्च/पूंजी) ना (नहीं), साख (साख/प्रतिष्ठा) ना काई (कोई नहीं थी), हत्थों (अपने हाथों) हारन (हारने/लुटने) चल्ली (चल पड़ी), मैं (मैं) मोटी (स्थूल) मुसटंडी (हठीली/अहंकारी) दिस्सां (दिखती हूँ), लाल नूं (रत्न को) चारन (चराने/सस्ता मोल लगाने) चल्ली (चल पड़ी), जिस (जिस) शाह (सर्वेश्वर/सच्चे शाह) ने (ने) मुल्ल (मूल्य) लै के (लेकर) देणा (देना था), सो (वह) शाह (सच्चा स्वामी) मूंह ना लाए (मुँह ही नहीं लगाता)।",
                "english_gloss": "कच्ची (Immature me) कच्च वेहाजन जाणां (knew only how to barter cheap glass beads), लाल वेहाजन चल्ली (set out to purchase true rubies), पल्ले खरच ना (no capital in my purse) साख ना काई (nor any spiritual credit), हत्थों हारन चल्ली (set out to lose everything by my own hands), मैं मोटी मुसटंडी दिस्सां (coarse, stubborn, and heavy with ego I appear), लाल नूं चारन चल्ली (set out to graze/graze down the jewel), जिस शाह ने (the True King who alone) मुल्ल लै के देणा (accepts the price and bestows), सो शाह (that Master) मूंह ना लाए (does not deign to speak to me).",
                "poetic_hindi": "काँच की परख थी मुझको केवल, लाल खरीदने धाई,\nपास न पूँजी, साख न कोई, बाज़ी हारन आई;\nमोटी-मुस्टंडी अहंकारन, रतन परखने आई,\nजिस शाह ने मोल लगाना था, वो मुँह भी न लगाए!\nवे सौदागर आए री माई, वे सौदागर आए!",
                "poetic_english": "I who knew only glass and clay, for gems divine made haste;\nWith neither coin nor credit left, my soul went out to waste;\nCrude and conceit-bound was my gaze, on holy rubies placed;\nThe Sovereign Merchant of the mart turned from me in distaste!\nThose jewel-merchants have arrived, O mother, their caravans draw near!"
            },
            {
                "stanza_number": 7,
                "original": [
                    "गलियां दे विच फिरें दीवानी, नी कुड़ीए मुट्यारे,  ",
                    "लाल चुगेंदी नाज़क होई, इह गल्ल कौन नितारे,  ",
                    "जा मैं मुल्ल ओन्हां नूं पुच्छ्या, मुल्ल करन उह भारे,  ",
                    "डम्ह सूई दा कदे ना खाधा, उह आखन सिर वारे,  ",
                    "जेहड़ियां गईआं लाल वेहाजन, उहनां सीस लुहाए ।  ",
                    "से वणजारे आए नी माए, से वणजारे आए ।  ",
                    "लालां दा उह वनज करेंदे, होका आख सुणाए ।"
                ],
                "hindi_gloss": "गलियां दे विच (गलियों में) फिरें (भटकती फिरती है) दीवानी (दीवानी/पागल बनकर), नी कुड़ीए (अरी युवती/कन्या!) मुट्यारे (नवयौवना!), लाल चुगेंदी (रत्न चुगते-चुगते/खोजते हुए) नाज़क (सुकुमार) होई (हो गई), इह गल्ल (यह बात) कौन (कौन) नितारे (सुलझाए/निपटाए), जा (जब) मैं (मैंने) मुल्ल (मूल्य) ओन्हां नूं (उनसे) पुच्छ्या (पूछा), मुल्ल (मूल्य) करन (करते हैं) उह (वे) भारे (अति भारी), डम्ह (डंक/चुभन) सूई दा (सुई का) कदे ना (कभी नहीं) खाधा/सहा, उह (वे) आखन (कहते हैं) सिर वारे (सिर कुर्बान कर), जेहड़ियां (जो-जो भी साधिकायें) गईआं (गईं) लाल वेहाजन (रत्न खरीदने), उहनां (उन्होंने) सीस (अपने शीश/अहंकार) लुहाए (उतार कर समर्पित कर दिए)।",
                "english_gloss": "गलियां दे विच फिरें दीवानी (Wandering mad through alleyways) नी कुड़ीए मुट्यारे (O haughty maiden!), लाल चुगेंदी नाज़क होई (seeking rubies thou became delicate and weary), इह गल्ल कौन नितारे (who can settle this dispute?), जा मैं मुल्ल ओन्हां नूं पुच्छ्या (when I asked them the price), मुल्ल करन उह भारे (they demand a stupendous cost), डम्ह सूई दा कदे ना खाधा (never having endured a needle's prick), उह आखन सिर वारे (they demand one's head in sacrifice), जेहड़ियां गईआं लाल वेहाजन (those true lovers who went to buy the rubies), उहनां सीस लुहाए (they severed their heads and laid them down!).",
                "poetic_hindi": "गलियों में दीवानी भटके, अरी मुटियारे कन्या!\nसुई की चुभन सही नहीं, कैसे बनेगी धन्या?\n'शीश चढ़ाओ' व्यापारी का हुक्म यही है भारी,\nजो भी लाल खरीदने पहुँचीं, सीस कटा घर आई!\nवे सौदागर आए री माई, वे सौदागर आए,\nरत्नों का व्यापार करें हैं, हाक लगा सुनाए!",
                "poetic_english": "Rambling demented through the streets, O maiden proud and vain!\nSeeking the gem thou art worn thin, yet who can clear the plain?\nWhen I inquired the ruby's price, they named a toll of pain:\n'Sever thy head upon our scales, or seek no heavenly gain!'\nThose souls who truly bought the gem laid down their lives outright!\nThose jewel-merchants have arrived, O mother, their caravans draw near;\nTrading in radiant rubies of love, their clarion call sounds clear!"
            }
        ],
        "sufi_commentary": "Kafi 138 is a celebrated masterpiece on the economics of Divine Love (Ishq). Bulleh Shah constructs a vivid allegory of jewel merchants (vanjare) representing the Prophets, Perfect Masters (Kamil Murshids), and Divine emissaries who arrive in the transient bazaar of this world offering the priceless 'Lal' (the ruby of Irfan, Gnosis, and Divine Essence). The naive soul (embodied as an immature, vain village maiden, 'कच्ची', 'मोटी मुसटंडी') assumes she can purchase mystical union with worldly currency—social righteousness, superficial rituals, or intellectual gold—so that she may display it as an egoic jewel in her earlobe ('इक ना इक कन्नां विच पा के, लोकां नूं दिखलावां'). But in the spiritual marketplace of Fana (annihilation), external wealth is worthless glass. When she asks the price, the Merchants declare: 'धड़ तों सीस लहाईं' (Sever your head from your torso). The severed head is the classical Sufi symbol for the total destruction of the Nafs (the false ego-identity). The seeker who has never even endured the slight prick of spiritual discipline ('डम्ह कदी सूई दा ना सहआ') recoils in terror. Bulleh concludes with an uncompromising truth: only those lovers who surrender their heads without hesitation ('उहनां सीस लुहाए') can possess the ruby of Divine Reality."
    },
    {
        "id": 139,
        "title_punjabi": "सुनो तुम इश्क की बाज़ी, मलायक है कहां राज़ी",
        "title_english": "Listen to the Cosmic Wager of Love",
        "raga": "Raga Sarang / Kafi",
        "meter": "Hazaj / Baint (14-14 matras)",
        "theme": "The Primordial Trust of Love (Amanah) Refused by Angels and Borne by Mortals",
        "historical_context": "Composed in an elevated Punjabi-Braj idiom, this Kafi reflects on Quran 33:72 ('Indeed, We offered the Trust to the heavens and the earth and the mountains, and they declined to bear it and feared it; but man undertook to bear it'). Bulleh contrasts the sterile obedience of angels (malayik) with the impassioned, reckless, self-sacrificing love of mortal lovers who are willing to dance naked, drink their own blood, and embrace martyrdom in love.",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "सुनो तुम इश्क की बाज़ी, मलायक है कहां राज़ी,  ",
                    "यहां बिरहों पर है गाज़ी, वेखां फिर कौन हारेगा ।"
                ],
                "hindi_gloss": "सुनो (सुनो) तुम (तुम सब) इश्क (दिव्य प्रेम) की (की) बाज़ी (दांव/जुआ/खेल), मलायक (देवदूत/फरिश्ते) है कहां (कहाँ भला) राज़ी (सहमति दे सके?), यहां (इस भूमि पर) बिरहों (विरह-व्यथा) पर है (पर आरूढ़) गाज़ी (शूरवीर/योद्धा), वेखां (देखते हैं) फिर (फिर) कौन (कौन) हारेगा (परास्त होता है)।",
                "english_gloss": "सुनो तुम (Listen ye) इश्क की बाज़ी (to the cosmic wager of Love), मलायक (the angels) है कहां राज़ी (how could they ever agree to bear it?), यहां (here on earth) बिरहों पर (upon separation's steed) है गाज़ी (is the true warrior), वेखां फिर (let us see then) कौन हारेगा (who will suffer defeat).",
                "poetic_hindi": "सुनो तुम प्रेम की बाज़ी, मलक कब इसमें थे राज़ी?\nयहाँ तो विरह का ग़ाज़ी, परख लें कौन हारेगा!",
                "poetic_english": "Hearken unto Love's cosmic game, which angels shrank from in their dread;\nHere separation rides the field, to see which warrior loses head!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "साजन की भाल हुन होई, मैं लहू नैन भर रोई,  ",
                    "नच्चे हम लाह कर लोई, हैरत के पत्थर मारेगा ।"
                ],
                "hindi_gloss": "साजन (प्रियतम) की (की) भाल (खोज/तलाश) हुन (अब) होई (आरम्भ हुई), मैं (मैं) लहू (रक्त) नैन भर (नेत्रों से अश्रुओं के रूप में) रोई (रोई हूँ), नच्चे (नाचे) हम (हम) लाह कर (उतार कर) लोई (लोक-लाज की चादर), हैरत (विस्मय/हैरानी) के (के) पत्थर (पत्थर) मारेगा (यह संसार हम पर बरसाएगा)।",
                "english_gloss": "साजन की भाल (The quest for the Beloved) हुन होई (has now begun), मैं लहू नैन भर रोई (I wept weeping tears of blood), नच्चे हम (I danced) लाह कर लोई (flinging aside the shawl of worldly shame), हैरत के पत्थर मारेगा (the world will pelt stones of bewilderment).",
                "poetic_hindi": "हुई साजन की जब जोई, लहू नयनों से मैं रोई,\nउतार लाज की लोई, जगत पत्थर चलाएगा!",
                "poetic_english": "The quest for my Beloved woke, tears of red blood my eyelids shed;\nI danced, casting my veil aside, though stones of wonder strike my head!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "महूरत पूछ कर जाऊं, साजन को देखने पाऊं,  ",
                    "उसे मैं ले गले लाऊं, नहीं फिर खुद गुज़ारेगा ।"
                ],
                "hindi_gloss": "महूरत (शुभ मुहूर्त) पूछ कर (पूछकर) जाऊं (चल पड़ूँ), साजन को (प्रियतम का) देखने पाऊं (दीदार पा सकूँ), उसे (उसे) मैं (मैं) ले गले लाऊं (गले से लगा लूँ), नहीं फिर (अन्यथा वह) खुद (मेरी सत्ता को) गुज़ारेगा (नष्ट/मिटा देगा)।",
                "english_gloss": "महूरत पूछ कर जाऊं (Let me consult the auspicious moment and set forth), साजन को देखने पाऊं (that I may behold the Beloved), उसे मैं ले गले लाऊं (clasp Him closely in my embrace), नहीं फिर खुद गुज़ारेगा (lest my fragile self be wholly obliterated).",
                "poetic_hindi": "मुहूरत पूछ कर धाऊँ, पिया के दरस को पाऊँ,\nउसे मैं कंठ लगाऊँ, नहीं तो खुद मिटाएगा!",
                "poetic_english": "I seek the blessed hour to fly, to gaze upon His face supreme;\nTo hold Him closely to my breast, or vanish in His fiery beam!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "इश्क की तेग़ से मूई, नहीं वोह ज़ात की दूई,  ",
                    "और पिया पिया कर मूई, मोयां विच रूह चितारेगा ।"
                ],
                "hindi_gloss": "इश्क (प्रेम) की (की) तेग़ (तलवार) से (से) मूई (मृत्यु को प्राप्त हुई), नहीं (नहीं रही) वोह (वह) ज़ात (अस्तित्व) की (की) दूई (द्वैत/द्वैतभाव), और (और) पिया पिया (पिया-पिया की पुकार) कर (करके) मूई (मर मिटी), मोयां विच (मृतकों में) रूह (आत्मा को) चितारेगा (पुनर्जीवित/अमर कर देगा)।",
                "english_gloss": "इश्क की तेग़ से मूई (Slain by Love's celestial sword), नहीं वोह ज़ात की दूई (the duality of selfhood vanished), और पिया पिया कर मूई (calling 'Beloved! Beloved!' I died), मोयां विच (amongst the dead) रूह चितारेगा (He will resurrect the spirit into immortality).",
                "poetic_hindi": "कटी तलवार से प्रेम की, मिटी सब द्वैत की छाया,\n'पिया-पिया' जप कर मरी, उसने मृतकों में रूह जगाया!",
                "poetic_english": "Slain by the sabre of His love, duality was carved away;\nCrying 'Beloved!' I expired; He breathed life into mortal clay!"
            },
            {
                "stanza_number": 5,
                "original": [
                    "साजन की भाल सर दिया, लहू मध अपना पिया,  ",
                    "कफ़न बाहों से सी लिया, लहद में पा उतारेगा ।"
                ],
                "hindi_gloss": "साजन (प्रियतम) की (की) भाल (तलाश में) सर (अपना शीश) दिया (दे दिया), लहू (रक्त रूपी) मध (मदिरा) अपना (अपना) पिया (पी लिया), कफ़न (कफ़न) बाहों से (अपनी भुजाओं से) सी लिया (सील लिया), लहद (कब्र/समाधि) में (में) पा (डालकर) उतारेगा (वह मुझे उतारेगा)।",
                "english_gloss": "साजन की भाल (In quest of the Beloved) सर दिया (I surrendered my head), लहू मध अपना पिया (I drank my own blood as wine), कफ़न (the shroud) बाहों से सी लिया (I stitched with my own arms), लहद में (into the tomb) पा उतारेगा (He will lower me down).",
                "poetic_hindi": "खोज में शीश भी वार दिया, लहू को मदिरा मान पिया,\nकफ़न को बाहों से सीया, वो लहद में अब उतारेगा!",
                "poetic_english": "I gave my head upon His search, and drank my blood like vintage wine;\nI stitched my shroud with my own arms, to rest within His grave divine!"
            },
            {
                "stanza_number": 6,
                "original": [
                    "बुल्ल्हा शहु इश्क है तेरा, उसी ने जी लिया मेरा,  ",
                    "मेरे घर बार कर फेरा, वेखां सिर कौन वारेगा ।"
                ],
                "hindi_gloss": "बुल्ल्हा (बुल्लेशाह कहता है) शहु (हे प्रभु-स्वामी!) इश्क (यह प्रेम) है तेरा (तेरा ही है), उसी ने (उसी प्रेम ने) जी (प्राण/जीवन) लिया (हरण कर लिया) मेरा (मेरा), मेरे (मेरे) घर (घर-आँगन) बार (द्वार पर) कर फेरा (एक फेरा लगा/चरण धर), वेखां (देखूं तो सही) सिर (अपना शीश) कौन (कौन प्रेमी) वारेगा (कुर्बान करता है)।",
                "english_gloss": "बुल्ल्हा शहु (Bulleh's Master!) इश्क है तेरा (Thy love it is), उसी ने (that very love) जी लिया मेरा (has claimed my life), मेरे घर बार (to my home and hearth) कर फेरा (make a round/visit), वेखां (let me see) सिर कौन वारेगा (who will sacrifice their head for Thee).",
                "poetic_hindi": "बुल्ल्हा कहे, यह इश्क तुम्हारा, जिसने मुझको जीत सँवारा,\nआ जा मेरे घर-द्वारे, देखूँ कौन शीश वारेगा!",
                "poetic_english": "Bulleh cries: King, Thy love alone has seized my life and claimed its throne;\nStep to my portal, let it be shown: who gives his head to be Thine own!"
            }
        ],
        "sufi_commentary": "Kafi 139 is an impassioned meditation on the cosmic drama of Ishq and the primordial Trust (Amanat). The opening line directly echoes Quran 33:72, where the heavens, earth, and angels shrank from carrying the agonizing wager of Love ('मलायक है कहां राज़ी'). The angels, created of light, know only adoration without tribulation; only human beings, forged of clay and spirit, possess the capacity to ride the battle-steed of separation ('बिरहों पर है गाज़ी') and conquer ego through voluntary death. The imagery of drinking one's own blood as wine ('लहू मध अपना पिया') and stitching one's own shroud ('कफ़न बाहों से सी लिया') evokes the profound Sufi doctrine of 'Mootoo qabla an tamootoo' (Die before you die). True love is not a romantic indulgence; it is a decapitating blade ('इश्क की तेग़') that amputates the illusion of duality ('नहीं वोह ज़ात की दूई'). When Bulleh asks the Master to grace his courtyard to see who is willing to lay down their head, he challenges the formalist world to show if any ritualist possesses the supreme courage of self-annihilation."
    },
    {
        "id": 140,
        "title_punjabi": "तैं कित पर पाउं पसारा ए",
        "title_english": "Why Have You Spread Your Feet in Heedless Slumber?",
        "raga": "Raga Bhairav / Asavari",
        "meter": "Davayya / Baint (16-12 matras)",
        "theme": "Spiritual Vigilance, Transience of Earthly Life, and Awakening from Illusion",
        "historical_context": "A classic waking song (Jagaran/Chetavani) of the Sufi-Sant tradition. Using the common Punjabi idiom of spreading one's legs in deep, carefree sleep ('पाउं पसारा'), Bulleh Shah shakes the sleeping traveler, reminding him that this earthly existence is nothing more than a momentary stopover in a caravanserai where the departure drums will sound at dawn.",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "तैं कित पर पाउं पसारा ए ।  ",
                    "कोई दम का अथां गुज़ारा ए ।"
                ],
                "hindi_gloss": "तैं (तूने) कित पर (किस भरोसे पर) पाउं पसारा ए (पाँव पसार रखे हैं/असावधान सोया है)? कोई (बस चंद) दम का (सांसों का) अथां (यहाँ इस संसार में) गुज़ारा ए (ठहराव/गुज़र-बसर है)।",
                "english_gloss": "तैं कित पर (On what pretext hast thou) पाउं पसारा ए (spread thy feet in carefree slumber)? कोई दम का (Only for a few fleeting breaths) अथां (here in this world) गुज़ारा ए (is thy sojourn).",
                "poetic_hindi": "किस भरोसे पाँव पसारा है?\nचंद साँसों का यहाँ गुज़ारा है!",
                "poetic_english": "Why stretch your limbs in heedless sleep so bold?\nA few short breaths are all this world can hold!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "इक पलक झलक दा मेला ए कुझ कर लै इहो वेला ए,  ",
                    "इक घड़ी ग़नीमत देहाड़ा ए तैं कित पर पाउं पसारा ए ।"
                ],
                "hindi_gloss": "इक (एक) पलक (पलक झपकने की) झलक (क्षणभंगुर झलक) दा (का) मेला ए (यह जीवन का मेला है), कुझ (कुछ शुभ कर्म/साधना) कर लै (कर ले), इहो (यही अनुकूल) वेला ए (अवसर है), इक (एक) घड़ी (घड़ी) ग़नीमत (परम वरदान/अवसर) देहाड़ा ए (दिन का यह समय है), तैं कित पर पाउं पसारा ए (तूने किस भरोसे पाँव पसारा है?)।",
                "english_gloss": "इक पलक झलक दा मेला ए (A fair that lasts only for a blink's flash), कुझ कर लै (accomplish something of worth), इहो वेला ए (now is the precious time), इक घड़ी (a single fleeting hour) ग़नीमत देहाड़ा ए (is a blessing of priceless fortune), तैं कित पर पाउं पसारा ए (why hast thou stretched thy feet in slumber?).",
                "poetic_hindi": "एक पलक-झलक का मेला है, कुछ कर ले, यही सु-वेला है,\nइक घड़ी ग़नीमत का तारा है, किस भरोसे पाँव पसारा है?",
                "poetic_english": "A passing fair that vanishes in an eye's quick blink,\nAwake and act while standing on this transient brink;\nEach fleeting moment is a treasure rich and rare,\nWhy stretch your feet in slumber free of care?"
            },
            {
                "stanza_number": 3,
                "original": [
                    "इक रात सरां दा रहना ए एथे आ कर फुल्ल ना बहना ए,  ",
                    "कल्ल्ह सभ दा कूच नकारा ए तैं कित पर पाउं पसारा ए ।"
                ],
                "hindi_gloss": "इक (एक) रात (रात) सरां दा (सराय में) रहना ए (रहना है), एथे (यहाँ) आ कर (आकर) फुल्ल ना बहना ए (अहंकार में फूल कर मत बैठ जाना), कल्ल्ह (कल प्रातः ही) सभ दा (सभी का) कूच नकारा ए (प्रस्थान का नगाड़ा बजेगा), तैं कित पर पाउं पसारा ए (तूने किस भरोसे पाँव पसारा है?)।",
                "english_gloss": "इक रात (A single night) सरां दा रहना ए (is the stay in this traveler's inn), एथे आ कर (having arrived here) फुल्ल ना बहना ए (do not sit puffed up with pride), कल्ल्ह (on the morrow) सभ दा (for all) कूच नकारा ए (the departure drum will sound), तैं कित पर पाउं पसारा ए (why hast thou spread thy feet in slumber?).",
                "poetic_hindi": "एक रात सराय का रहना है, मत फूल यहाँ कुछ कहना है,\nकल कूच-नकारा बजना है, किस भरोसे पाँव पसारा है?",
                "poetic_english": "One night alone within this caravanserai you stay;\nPuff not with vanity before you fade away;\nTomorrow's drum will sound the final marching call;\nWhy stretch your feet as if death would not fall?"
            },
            {
                "stanza_number": 4,
                "original": [
                    "तूं ओस मकानों आया एं, एथे आदम बण समाइआ एं,  ",
                    "हुन छड्ड मजलस कोई कारा ए तैं कित पर पाउं पसारा ए ।"
                ],
                "hindi_gloss": "तूं (तू) ओस (उस परम ला-मकां/दिव्य धाम) मकानों (धाम से) आया एं (आया है), एथे (यहाँ मर्त्यलोक में) आदम (मानव का रूप) बण (बनकर) समाइआ एं (प्रविष्ट हुआ है), हुन (अब) छड्ड (त्याग दे) मजलस (तुच्छ विषयों की संगत/विलासिता), कोई कारा ए (कोई सार्थक आध्यात्मिक कर्म कर), तैं कित पर पाउं पसारा ए (तूने किस भरोसे पाँव पसारा है?)।",
                "english_gloss": "तूं (Thou) ओस मकानों (from that spaceless Realm Divine) आया एं (hast descended), एथे (here) आदम बण (taking Adam's mortal form) समाइआ एं (hast entered), हुन (now) छड्ड मजलस (abandon shallow earthly assemblies), कोई कारा ए (perform some real work of devotion), तैं कित पर पाउं पसारा ए (why hast thou spread thy feet in slumber?).",
                "poetic_hindi": "तू उस पावन धाम से आया, यहाँ आदम का रूप सजाया,\nछोड़ विलास, कर साधन सारा, किस भरोसे पाँव पसारा है?",
                "poetic_english": "From that celestial Home of Light you descended low,\nAssuming mortal Adam's form to walk below;\nForsake vain company, work for the soul's release;\nWhy stretch your feet in false, unearned peace?"
            },
            {
                "stanza_number": 5,
                "original": [
                    "बुल्ल्हा शहु इह भरम तुम्हारा ए सिर चुक्क्या परबत भारा ए,  ",
                    "उस मंज़ल राह ना खाहड़ा ए तैं कित पर पाउं पसारा ए ।"
                ],
                "hindi_gloss": "बुल्ल्हा (बुल्लेशाह कहता है) शहु (हे जीव!) इह (यह जो अहंता है) भरम (भ्रम/मिथ्या माया) तुम्हारा ए (तुम्हारा है), सिर (सिर पर) चुक्क्या (उठा रखा है) परबत (पापों और वासनाओं का पर्वत) भारा ए (भारी), उस (उस परमात्मा की) मंज़ल (मंजिल का) राह ना खाहड़ा ए (तुझे कोई मार्ग या सुराग ज्ञात नहीं), तैं कित पर पाउं पसारा ए (तूने किस भरोसे पाँव पसारा है?)।",
                "english_gloss": "बुल्ल्हा (Bulleh says) शहु (the Master says) इह भरम तुम्हारा ए (this is merely thy delusion of separate self), सिर चुक्क्या (upon thy head thou hast borne) परबत भारा ए (a heavy mountain of karmas/pride), उस मंज़ल (of that Divine destination) राह ना खाहड़ा ए (thou hast neither path nor track), तैं कित पर पाउं पसारा ए (why hast thou spread thy feet in slumber?).",
                "poetic_hindi": "बुल्ल्हा कहे, यह भरम तुम्हारा, सिर ढोता पर्वत अति भारा,\nमंज़िल की राह न ढूँढी ज़रा, किस भरोसे पाँव पसारा है?",
                "poetic_english": "Bulleh says: this phantom ego is your self-made plight,\nA mountain of heavy sin you bear into the night;\nYou know not the road that leads to the Master's door;\nWhy stretch your feet in slumber upon the floor?"
            }
        ],
        "sufi_commentary": "Kafi 140 is a piercing wake-up call to the spiritual seeker slumbering in the hypnotic trance of Ghaflat (heedlessness). The phrase 'पाउं पसारा' (stretching one's legs) denotes someone who has settled into deep, carefree comfort, forgetting danger and transience. Bulleh dismantles this complacency through the ancient metaphor of the caravanserai ('सरां'). Life in human form is merely a single night's lodging; at dawn, the marching drum ('कूच नकारा') will inevitably sound. Bulleh reminds the soul of its celestial origin: 'तूं ओस मकानों आया एं, एथे आदम बण समाइआ एं'—the soul descended from the Spaceless Divine Presence (La-makan) and took on the mortal garment of Adam. Instead of fulfilling the purpose of this incarnation by seeking reunion, man wastes his brief hours in trivial worldly gatherings ('मजलस') and burdens his head with a mountain of worldly illusions ('सिर चुक्क्या परबत भारा'). Without realizing the true path ('राह ना खाहड़ा'), slumber is spiritual suicide. Bulleh urges immediate vigilance before the brief opportunity of human life dissolves forever."
    }
]

# Lexicon updates for batch 136-140
new_lexicon_entries = {
    "अजला": {
        "gurmukhi": "ਅਜ਼ਲਾ / ਅਰਸ਼ਾਂ",
        "hindi": "अनादि काल / सर्वोच्च आकाश (अर्श)",
        "english": "Eternity / highest celestial sphere (Arsh)",
        "context": "सानूं आ मिल यार प्यारिआ (Kafi 136)"
    },
    "हावीए": {
        "gurmukhi": "ਹਾਵੀਏ",
        "hindi": "हाविया (कुरान में वर्णित दोजख का सबसे निचला और भीषण गर्त)",
        "english": "Hawiyah (the lowest, hottest abyss of Hell in Islamic eschatology)",
        "context": "डर हावीए दोज़ख मारिआ (Kafi 136)"
    },
    "मज़कूर": {
        "gurmukhi": "ਮਜ਼ਕੂਰ",
        "hindi": "उल्लेख, चर्चा, विषय",
        "english": "Mentioned, stated, subject of discourse",
        "context": "है अलइनसान मज़कूर तेरा (Kafi 137)"
    },
    "नाबूद": {
        "gurmukhi": "ਨਾਬੂਦ",
        "hindi": "अस्तित्वहीन, शून्यता, अभाव",
        "english": "Non-existence, nothingness",
        "context": "नाबूदों कर बूद दिखलाइओ (Kafi 137)"
    },
    "बूद": {
        "gurmukhi": "ਬੂਦ",
        "hindi": "हस्ती, अस्तित्व, सत्ता",
        "english": "Existence, being",
        "context": "नाबूदों कर बूद दिखलाइओ (Kafi 137)"
    },
    "मुसटंडी": {
        "gurmukhi": "ਮੁਸਟੰਡੀ",
        "hindi": "मोटी, उद्दंड, अहंकारी, हठी",
        "english": "Coarse, arrogant, stubbornly self-willed",
        "context": "मैं मोटी मुसटंडी दिस्सां (Kafi 138)"
    },
    "मुहरा": {
        "gurmukhi": "ਮੁਹਰਾ",
        "hindi": "स्वर्णमुद्रा, अनमोल रत्न, मोहर",
        "english": "Gold coin, precious talisman or gem",
        "context": "केहड़ा मुहरा ओथों रन्ने (Kafi 138)"
    },
    "मलायक": {
        "gurmukhi": "ਮਲਾਯਕ",
        "hindi": "मलाइका, देवदूत, फरिश्ते",
        "english": "Angels (plural of Malak)",
        "context": "मलायक है कहां राज़ी (Kafi 139)"
    },
    "लहद": {
        "gurmukhi": "ਲਹਦ",
        "hindi": "कब्र का भीतरी गर्त, समाधि",
        "english": "The niche within a grave, tomb",
        "context": "लहद में पा उतारेगा (Kafi 139)"
    },
    "सरां": {
        "gurmukhi": "ਸਰਾਂ",
        "hindi": "सराय, मुसाफिरखाना, विश्रामगृह",
        "english": "Caravanserai, traveler's inn",
        "context": "इक रात सरां दा रहना ए (Kafi 140)"
    },
    "कूच": {
        "gurmukhi": "ਕੂਚ",
        "hindi": "प्रस्थान, महाप्रयाण, कूच करना",
        "english": "Departure, march onward, passing away",
        "context": "कल्ल्ह सभ दा कूच नकारा ए (Kafi 140)"
    }
}

def save_batch():
    os.makedirs(KAFIAN_DIR, exist_ok=True)
    for kafi in batch_kafian:
        file_path = os.path.join(KAFIAN_DIR, f"kafi_{kafi['id']:03d}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(kafi, f, ensure_ascii=False, indent=2)
        print(f"Saved {file_path}")

    # Update Lexicon
    if os.path.exists(LEXICON_PATH):
        with open(LEXICON_PATH, "r", encoding="utf-8") as f:
            lexicon = json.load(f)
    else:
        lexicon = {}

    initial_len = len(lexicon)
    lexicon.update(new_lexicon_entries)
    with open(LEXICON_PATH, "w", encoding="utf-8") as f:
        json.dump(lexicon, f, ensure_ascii=False, indent=2)
    print(f"Lexicon updated: added {len(lexicon) - initial_len} new entries, total now {len(lexicon)}")

    # Update Checkpoint
    checkpoint = {
        "last_processed_kafi_id": 140,
        "completed_count": 140,
        "total": 160,
        "next_kafi_id": 141,
        "status": "in_progress"
    }
    with open(CHECKPOINT_PATH, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print("Checkpoint updated: 140/160 completed. Next ID: 141")

if __name__ == "__main__":
    save_batch()
