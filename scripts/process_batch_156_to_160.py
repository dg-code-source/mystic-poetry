"""
Process Batch 156 to 160 of Bulleh Shah's Kafian (The Grand Finale).
Kafi 156: वाह सोहण्यां तेरी चाल अजायब लटकां नाल चलेंदे ओ (Wondrous Is Thy Gait, O Beautiful One, Walking with Graceful Strides!)
Kafi 157: वाह वाह छिंझ पई दरबार (Marvelous Is the Cosmic Wrestling Match at the Royal Court!)
Kafi 158: वाह वाह रमज़ सजन दी होर (How Sublime and Inscrutable Is the Secret of the Beloved!)
Kafi 159: वल परदे विच पाइआ यार आपे मेल मिलाइआ ए (Behind the Veil the Friend Revealed Himself, Uniting Me to His Grace)
Kafi 160: वत्त ना करसां मान रंझेटे यार दा वे अड़िआ (Never Again Shall I Boast of My Herdsman's Love, O Friend!)
"""

import json
import os

DATA_DIR = os.path.abspath("c:/my-code/Bulleh-Shah/data")
KAFIAN_DIR = os.path.join(DATA_DIR, "kafian")
LEXICON_PATH = os.path.join(DATA_DIR, "punjabi_sufi_lexicon.json")
CHECKPOINT_PATH = os.path.join(DATA_DIR, "checkpoint.json")

batch_kafian = [
    {
        "id": 156,
        "title_punjabi": "वाह सोहण्यां तेरी चाल अजायब लटकां नाल चलेंदे ओ",
        "title_english": "Wondrous Is Thy Gait, O Beautiful One, Walking with Graceful Strides!",
        "raga": "Raga Kafi / Tilang",
        "meter": "Matrik Chhand (16-14 matras)",
        "theme": "The Absolute as the Cosmic Coquette across Orthodoxy and Heresy",
        "historical_context": "A sparkling declaration of Wahdat al-Wujud. Bulleh Shah depicts God as the sublime lover walking with intoxicating, coquettish strides ('लटकां नाल चलेंदे ओ'). The Beloved plays every role: the Zahir (manifest) and Batin (hidden), the Mullah delivering fatwas and the Qazi judging trials, donning the Hindu sacred thread (zunnar) in the idol temple, yet also causing the heavens to celebrate the Prophet ('Lawlaaka lamaa khalaqtu al-aflaak').",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "आपे ज़ाहर आपे बातन आपे लुक्क लुक्क बहन्दे ओ ।  ",
                    "आपे मुल्लां आपे काज़ी आपे इलम पढ़ेंदे ओ ।  ",
                    "वाह सोहण्यां तेरी चाल अजायब लटकां नाल चलेंदे ओ ।"
                ],
                "hindi_gloss": "आपे (स्वयं ही) ज़ाहर (प्रत्यक्ष प्रकट) आपे (स्वयं ही) बातन (अप्रत्यक्ष/गुप्त) आपे (स्वयं ही) लुक्क लुक्क (छिप-छिप कर) बहन्दे ओ (बैठते हो)। आपे (स्वयं ही) मुल्लां (मौलवी बनते हो) आपे (स्वयं ही) काज़ी (न्यायाधीश बनते हो) आपे (स्वयं ही धर्म का) इलम (ज्ञान) पढ़ेंदे ओ (पढ़ते-पढ़ाते हो)। वाह (अहा!) सोहण्यां (हे परम सुंदर प्रियतम!) तेरी (तेरी) चाल (चाल/अंदाज) अजायब (अद्भुत/विचित्र है), लटकां नाल (नाज़-नखरों और मस्तानी अदा से) चलेंदे ओ (चलते हो)।",
                "english_gloss": "आपे ज़ाहर (Thyself the Manifest) आपे बातन (Thyself the Hidden) आपे लुक्क लुक्क बहन्दे ओ (Thyself seated in hiding). आपे मुल्लां (Thyself the Mullah) आपे काज़ी (Thyself the Judge) आपे इलम पढ़ेंदे ओ (Thyself reciting the holy scriptures). वाह सोहण्यां (Wondrous, O Beautiful One!) तेरी चाल अजायब (Thy gait is marvelous), लटकां नाल चलेंदे ओ (Thou walkest with such enchanting, swaying grace!).",
                "poetic_hindi": "आप ही ज़ाहिर, आप ही बातिन, आप ही छिप-छिप बैठे हो;\nआप ही मुल्ला, आप ही काज़ी, आप ही इल्म को पढ़ते हो!\nवाह सोहणे! तेरी चाल अजब, नाज़ों से कदम बढ़ाते हो!",
                "poetic_english": "Thyself the Seen, Thyself the Unseen, Thyself in secret keeping place;\nThyself the Priest, Thyself the Judge, reciting scrolls of holy grace!\nWondrous, O Beautiful! Thy gait sways with such captivating pace!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "घत्त ज़न्नार कुफ़र दा गल विच बुत्त-ख़ाने वड़ बहन्दे ओ ।  ",
                    "लोलाक लमा अफलाक विचारे आपे धुंम मचेंदे ओ ।  ",
                    "वाह सोहण्यां तेरी चाल अजायब लटकां नाल चलेंदे ओ ।"
                ],
                "hindi_gloss": "घत्त (डालकर) ज़न्नार (जनेऊ/कुफ्र का पवित्र धागा) कुफ़र दा (कुफ्र का) गल विच (कंठ में) बुत्त-ख़ाने (मूर्ति-मंदिर में) वड़ बहन्दे ओ (प्रविष्ट होकर आसन जमा लेते हो)। लोलाक लमा अफलाक ('लौ लाका लमा खलक्तुल अफलाक' - यदि तू न होता तो मैं आकाशों को न रचता) विचारे (उस वचन से) आपे (स्वयं ही) धुंम (महिमा का डंका) मचेंदे ओ (बजाते हो)। वाह सोहण्यां तेरी चाल अजायब लटकां नाल चलेंदे ओ ।",
                "english_gloss": "घत्त ज़न्नार कुफ़र दा (Donning the sacred thread of heresy) गल विच (around Thy neck) बुत्त-ख़ाने वड़ बहन्दे ओ (Thou enterest the idol-temple and takest Thy seat). लोलाक लमा अफलाक ('Were it not for thee, I had not created the celestial spheres') विचारे आपे धुंम मचेंदे ओ (proclaiming Thyself, Thou causest Thy fame to resound). वाह सोहण्यां तेरी चाल अजायब लटकां नाल चलेंदे ओ ।",
                "poetic_hindi": "गले में डाल जनेऊ कुफ्र का, बुत-खाने में जा बैठते हो;\n'लौलाका' की महिमा रच कर, अपना ही डंका पीटते हो!\nवाह सोहणे! तेरी चाल अजब, नाज़ों से कदम बढ़ाते हो!",
                "poetic_english": "Draping the pagan thread around, in idol-temples Thou dost hide;\nThen chanting 'Were it not for thee', Thy cosmic fame rings far and wide!\nWondrous, O Beautiful! Thy gait sways with such captivating pace!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "ज़ात तों है अज़राफ रंझेटा लाईआं दी लाज रखेंदे ओ ।  ",
                    "बुल्ल्हा शहु अनायत मैनूं पल पल दरशन देंदे ओ ।  ",
                    "वाह सोहण्यां तेरी चाल अजायब लटकां नाल चलेंदे ओ ।"
                ],
                "hindi_gloss": "ज़ात तों (अपनी जाति और स्वरूप से) है (है) अज़राफ (अशरफ/अत्यंत कुलीन और निष्कलंक) रंझेटा (मेरा प्रियतम रांझा), लाईआं दी (प्रेम की बांधी हुई प्रीति की) लाज (लाज/मर्यादा) रखेंदे ओ (निभाते हो)। बुल्ल्हा (बुल्लेशाह कहता है) शहु अनायत (मुर्शिद शाह इनायत के रूप में) मैनूं (मुझको) पल पल (प्रतिक्षण) दरशन (अपना प्रत्यक्ष दीदार) देंदे ओ (देते हो)। वाह सोहण्यां तेरी चाल अजायब लटकां नाल चलेंदे ओ ।",
                "english_gloss": "ज़ात तों है अज़राफ (By lineage and essence Thou art supremely noble) रंझेटा (my beloved Ranjha), लाईआं दी लाज रखेंदे ओ (Thou honorest the sacred covenant of pledged love). बुल्ल्हा शहु अनायत (Bulleh cries: through Master Shah Inayat) मैनूं पल पल दरशन देंदे ओ (Thou grantest me Thy divine vision at every fleeting breath). वाह सोहण्यां तेरी चाल अजायब लटकां नाल चलेंदे ओ ।",
                "poetic_hindi": "अति कुलीन है प्रियतम रांझा, प्रीत की लाज निभाते हो;\nबुल्ल्हा कहे, शाह इनायत बन कर, पल-पल दरस दिखाते हो!\nवाह सोहणे! तेरी चाल अजब, नाज़ों से कदम बढ़ाते हो!",
                "poetic_english": "Nobility is Thy Ranjha's birth, keeping love's pledges upon earth;\nThrough Shah Inayat, Bulleh cries, Thou grantest vision to my eyes!\nWondrous, O Beautiful! Thy gait sways with such captivating pace!"
            }
        ],
        "sufi_commentary": "Kafi 156 is an ecstatic anthem of Divine Immanence. God is the sovereign Flâneur of the cosmos whose playful gait ('लटकां नाल चलेंदे ओ') mesmerizes creation. Bulleh obliterates the binary between sacred and profane: the same God is both Zahir (exterior) and Batin (interior); the same God writes religious laws as the Mullah and issues verdicts as the Qazi. In Stanza 2, Bulleh evokes the supreme scandal of love: the Beloved wears the Brahmin's sacred thread (zunnar) in the pagan temple, yet simultaneously proclaims the Hadith Qudsi addressed to the Prophet Muhammad: 'Law laaka lamaa khalaqtu al-aflaak' ('Were it not for thee, I would not have created the heavenly spheres'). In the final stanza, the noble Ranjha keeps the pledge of love by revealing His face every single moment through Murshid Shah Inayat."
    },
    {
        "id": 157,
        "title_punjabi": "वाह वाह छिंझ पई दरबार",
        "title_english": "Marvelous Is the Cosmic Wrestling Match at the Royal Court!",
        "raga": "Raga Tilang / Kafi",
        "meter": "Baint / Davayya (16-14 matras)",
        "theme": "The Cosmic Arena of Life (Chhinjh), the Great Fall of Mortals, and Salvation through Deeds",
        "historical_context": "Rooted in the traditional rural Punjabi wrestling tournament ('Chhinjh' / 'Dangal'). Bulleh Shah envisions the universe as a grand wrestling arena staged before the Divine Court ('दरबार'). Human beings enter the ring boasting of youth, wealth, and status, but are thrown to the ground in turn by the wrestler of Destiny/Death. The turban of earthly prestige is hurled into the dust ('लाह पगड़ी भोइं मार'), and only true devotion and the intercession of the Prophet bring salvation.",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "वाह वाह छिंझ पई दरबार ।  ",
                    "ख़लक तमाशे आई यार ।"
                ],
                "hindi_gloss": "वाह वाह (क्या ही अद्भुत!) छिंझ (कुश्ती का अखाड़ा/दंगल) पई (सजा हुआ है) दरबार (ईश्वर के राज-दरबार में)। ख़लक (संसार की समस्त सृष्टि) तमाशे (इस कौतुक को देखने) आई (आई है) यार (हे मित्र!)।",
                "english_gloss": "वाह वाह (Marvelous, glorious!) छिंझ पई (a wrestling tournament is staged) दरबार (in the Divine Court). ख़लक (All creation) तमाशे (to witness the spectacle) आई यार (has gathered, O friend!).",
                "poetic_hindi": "वाह-वाह! क्या दंगल सजा दरबार,\nसृष्टि तमाशा देखने आई यार!",
                "poetic_english": "Marvelous is the wrestling arena at the Court on high!\nAll creation has gathered to watch beneath the sky!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "असां अज्ज की कीता ते कल्ल्ह की करना भट्ठ असाडा आया,  ",
                    "ऐसी वाह क्यारी बीजी चिड़ियां खेत वंजाइआ,  ",
                    "जेहड़े मगर प्यादे लग्गे उट्ठ चल्ले पहुते तार ।  ",
                    "वाह वाह छिंझ पई दरबार ।"
                ],
                "hindi_gloss": "असां (हमने) अज्ज (आज) की कीता (क्या किया) ते (और) कल्ल्ह (कल) की करना (क्या करना है), भट्ठ (भट्ठी में/व्यर्थ) असाडा आया (हमारा जीवन नष्ट हो गया), ऐसी (हमने ऐसी) वाह (विचित्र) क्यारी (खेत की क्यारी) बीजी (बोई कि) चिड़ियां (चिड़ियों ने) खेत (सम्पूर्ण खेत) वंजाइआ (चुग कर उजाड़ दिया), जेहड़े मगर (जिनके पीछे यमराज के) प्यादे लग्गे (दूत लग गए), उट्ठ चल्ले (वे उठकर चल दिए) पहुते तार (जिन्हें कोई बचा न सका)।",
                "english_gloss": "असां अज्ज की कीता (What have we accomplished today) ते कल्ल्ह की करना (and what shall we do tomorrow?), भट्ठ असाडा आया (our existence was consumed in a barren furnace), ऐसी वाह क्यारी बीजी (such a field we sowed) चिड़ियां खेत वंजाइआ (that wild birds devoured the entire harvest), जेहड़े मगर प्यादे लग्गे (those pursued by death's foot-soldiers) उट्ठ चल्ले (arose and marched away) पहुते तार (beyond all rescue).",
                "poetic_hindi": "आज क्या किया, कल क्या करना? भट्ठी में जनम गँवाया,\nऐसी क्यारी बोई हमने, चिड़ियों ने खेत चुगाया;\nपीछे जिनके प्यादे भागे, उठ चले वो बेसहारा!\nवाह-वाह! क्या दंगल सजा दरबार!",
                "poetic_english": "What have we done today? What will tomorrow yield? Our lives burnt in a kiln conceiled;\nWe sowed such seed that hungry sparrows stripped the field;\nWhen death's footmen pursue, the soul must arise and yield!\nMarvelous is the wrestling arena at the Court on high!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "इक्क उल्हामा सईआं दा है दूजा है संसार,  ",
                    "नंग नमूज़ (नामूस) एथों दे एथे, लाह पगड़ी भोइं मार,  ",
                    "नाम साईं दे कंडे लवाए खिल पई गुलज़ार ।  ",
                    "वाह वाह छिंझ पई दरबार ।"
                ],
                "hindi_gloss": "इक्क (एक ओर) उल्हामा (उलाहना/शिकायत) सईआं दा (सखियों का) है (है) दूजा (दूसरी ओर उलाहना) है संसार (संसार का है), नंग नमूज़ (लोक-लाज, मर्यादा और कुल की झूठी प्रतिष्ठा) एथों दे एथे (यहीं संसार में पड़ी रह जाएगी), लाह (उतार कर) पगड़ी (अहंकार की पगड़ी) भोइं मार (जमीन पर पटक दे), नाम साईं दे (परमात्मा के नाम ने जब) कंडे लवाए (कांटों को स्पर्श किया), खिल पई (तो खिल उठा) गुलज़ार (सुगंधित गुलाब का बाग)।",
                "english_gloss": "इक्क उल्हामा सईआं दा है (On one side is the reproach of companions) दूजा है संसार (on the other, the condemnation of the world), नंग नमूज़ (honor, shame, and prestige) एथों दे एथे (remain here in the dust), लाह पगड़ी (strip off thy turban of vanity) भोइं मार (and dash it to the ground), नाम साईं दे (by the Master's holy Name) कंडे लवाए (even thorny briers were transformed) खिल पई गुलज़ार (into a blooming rose-garden).",
                "poetic_hindi": "सखियों का उलाहना एक, दूसरा संसार का भार,\nलोक-लाज सब यहीं रहेगी, पगड़ी पटक उतार;\nसाईं के नाम से कांटे भी बन गए चमन गुलज़ार!\nवाह-वाह! क्या दंगल सजा दरबार!",
                "poetic_english": "Companions taunt on one hand, the world reproaches round;\nHonor and fame belong to earth, throw thy proud turban to the ground!\nAt the Master's Name, the thorns with fragrant roses crowned!\nMarvelous is the wrestling arena at the Court on high!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "नढ्ढा गिरदा बुढ्ढा गिरदा आपो आपनी वारी,  ",
                    "की बीवी की बांदी लौंडी की धोबन भठ्यारी,  ",
                    "अमलां सेती होन नबेड़े नबी लंघावे पार ।  ",
                    "वाह वाह छिंझ पई दरबार ।"
                ],
                "hindi_gloss": "नढ्ढा गिरदा (नवयुवक पहलवान गिरता है) बुढ्ढा गिरदा (वृद्ध गिरता है) आपो आपनी वारी (अपनी-अपनी बारी आने पर), की बीवी (चाहे सम्मानित बेगम हो) की बांदी लौंडी (या दासी-लौंडी हो) की धोबन भठ्यारी (चाहे धोबी की स्त्री हो या भठियारी), अमलां सेती (कर्मों के आधार पर ही) होन नबेड़े (अंतिम निर्णय/हिसाब होता है), नबी (और पैगंबर की कृपा ही) लंघावे पार (संसार-सागर से पार उतारती है)।",
                "english_gloss": "नढ्ढा गिरदा बुढ्ढा गिरदा (The young man falls, the old man falls) आपो आपनी वारी (each in his appointed turn), की बीवी (be it noble mistress) की बांदी लौंडी (or slave girl) की धोबन भठ्यारी (washerwoman or innkeeper), अमलां सेती होन नबेड़े (by righteous deeds alone is the final judgment settled), नबी लंघावे पार (and the Prophet ferries the soul across).",
                "poetic_hindi": "युवा गिरे और वृद्ध गिरे, अपनी-अपनी बारी,\nक्या रानी, क्या दासी-चेरी, क्या धोबन-भठियारी;\nकर्मों से ही न्याय होगा, नबी उतारे पार!\nवाह-वाह! क्या दंगल सजा दरबार!",
                "poetic_english": "Youths fall and elders tumble down, each taking turn in line;\nWhether noble lady, slave-girl, washerwoman, or innkeeper fine;\nBy deeds alone the scales are weighed, through the Prophet's grace divine!\nMarvelous is the wrestling arena at the Court on high!"
            },
            {
                "stanza_number": 5,
                "original": [
                    "बुल्ल्हा शहु नूं वेखन जावे आपना बहाना करदा,  ",
                    "गूनो गूनी भांडे घड़ के ठीकरियां कर धरदा,  ",
                    "इह तमाशा वेख के चल्ल अगला वेख बज़ार ।  ",
                    "वाह वाह छिंझ पई दरबार ।  ",
                    "ख़लक तमाशे आई यार ।"
                ],
                "hindi_gloss": "बुल्ल्हा (बुल्लेशाह कहता है) शहु नूं (प्रभु-प्रियतम को) वेखन जावे (देखने जाता है) आपना (अपना कोई न कोई) बहाना करदा (बहाना बनाकर), गूनो गूनी (भांति-भांति के सुंदर) भांडे (मिट्टी के बर्तन) घड़ के (गढ़-गढ़ कर) ठीकरियां कर धरदा (उन्हें ठीकरियों में फोड़ कर रख देता है), इह तमाशा (इस संसार के खेल को) वेख के (देखकर) चल्ल (अब आगे चल) अगला (अगले शाश्वत) वेख बज़ार (बाजार का दर्शन कर)।",
                "english_gloss": "बुल्ल्हा शहु नूं वेखन जावे (Bulleh goes to behold the King) आपना बहाना करदा (making some pretext of his own), गूनो गूनी भांडे घड़ के (fashioning pots of diverse exquisite shapes) ठीकरियां कर धरदा (He smashes them into shards of clay), इह तमाशा वेख के (having seen this earthly play) चल्ल अगला वेख बज़ार (walk on to witness the Market of Eternity!).",
                "poetic_hindi": "बुल्ल्हा शाह को देखने जाए, बहाना नया बनाए,\nरंग-बिरंगे बर्तन गढ़ के, ठीकरियाँ कर गिराए;\nइस तमाशे को देख के साधो! अगला बाज़ार सिधारे!\nवाह-वाह! क्या दंगल सजा दरबार, सृष्टि तमाशा देखने आई यार!",
                "poetic_english": "Bulleh goes to behold the King, seeking pretexts sweet and fair;\nHe molds clay pots of diverse forms, then breaks them into shards right there;\nWitness this fleeting earthly show, then seek that higher Market rare!\nMarvelous is the wrestling arena at the Court on high!\nAll creation has gathered to watch beneath the sky!"
            }
        ],
        "sufi_commentary": "Kafi 157 uses the indigenous Punjabi metaphor of the 'Chhinjh'—the grand rural wrestling tourney. The cosmos is God's wrestling arena, where all mortals enter full of pride, only to be thrown into the dust by the champion wrestler of Time ('नढ्ढा गिरदा बुढ्ढा गिरदा आपो आपनी वारी'). Death makes no caste, gender, or social distinctions: the noble queen ('बीवी'), the indentured slave-girl ('बांदी'), the washerwoman ('धोबन'), and the innkeeper ('भठ्यारी') all fall alike. Conventional status ('पगड़ी') is useless; Bulleh urges the seeker to dash the turban of pride to the ground ('लाह पगड़ी भोइं मार'). In the cosmic court, judgment is settled strictly by righteous deeds ('अमलां सेती होन नबेड़े'), aided by the intercession of the Prophet. Finally, Bulleh portrays God as the Divine Potter who fashions magnificent vessels only to smash them back into shards of dust, reminding us to look beyond this temporary spectacle toward the eternal Bazaar of Truth."
    },
    {
        "id": 158,
        "title_punjabi": "वाह वाह रमज़ सजन दी होर",
        "title_english": "How Sublime and Inscrutable Is the Secret of the Beloved!",
        "raga": "Raga Kafi / Bhairavi",
        "meter": "Baint / Davayya (16-12 matras)",
        "theme": "The Esoteric Cipher (Ramz) of Divine Love and the Panoply of Martyr-Lovers",
        "historical_context": "A comprehensive 9-stanza panegyric to the mystery of Ishq. Bulleh Shah proclaims that the secret cipher of the Beloved ('रमज़ सजन दी') is incomprehensible to the intellect and blind formalists ('आशक बिनां ना समझे कोर'). He reviews the grand lineage of mystic lovers—Farhad and Shirin, Yusuf and Zulaikha, Layla and Majnun, Sohni and Mahiwal, Heer and Ranjha—all ensnared by the same divine net, and confesses that he was robbed by the Divine Master in Lahore ('मैनूं मिल गया ठग्ग लाहौर').",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "वाह वाह रमज़ सजन दी होर ।  ",
                    "आशक बिनां ना समझे कोर ।"
                ],
                "hindi_gloss": "वाह वाह (अहा, क्या ही अद्भुत!) रमज़ (गूढ़ संकेत/गुप्त रहस्य) सजन दी (प्रियतम का) होर (अलौकिक और अद्वितीय है)। आशक बिनां (सच्चे प्रेमी के अतिरिक्त) ना समझे (नहीं समझ सकता) कोर (अंधा बुद्धिवादी/अज्ञानी)।",
                "english_gloss": "वाह वाह (How sublime and wondrous!) रमज़ सजन दी (is the secret cipher of the Beloved) होर (utterly unique and beyond grasp). आशक बिनां (Save for the true lover) ना समझे कोर (no blind worldly soul can ever comprehend).",
                "poetic_hindi": "वाह-वाह! सजन का भेद है न्यारा,\nआशिक बिना न जाने अंधा जग सारा!",
                "poetic_english": "Sublime is the cipher my Beloved weaves;\nWhich none but the lover's deep heart perceives!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "कोठे ते चढ़ देवां होका, इश्क वेहाज्यु कोई ना लोका,  ",
                    "इस दा मूल ना खाना धोखा, जंगल बसती मिले ना ठोर ।  ",
                    "वाह वाह रमज़ सजन दी होर ।"
                ],
                "hindi_gloss": "कोठे ते चढ़ (छत पर चढ़कर) देवां (देती हूँ) होका (पुकार/घोषणा), इश्क (दिव्य प्रेम का सौदा) वेहाज्यु कोई ना लोका (हे लोगो, कोई मत खरीदना!), इस दा (इसके विषय में) मूल ना खाना (कदापि मत खाना) धोखा (धोखा/भ्रम), जंगल बसती (न जंगल में, न बस्ती में) मिले ना ठोर (कहीं कोई ठिकाना नहीं मिलता)।",
                "english_gloss": "कोठे ते चढ़ देवां होका (Climbing the rooftop I cry aloud), इश्क वेहाज्यु कोई ना लोका (buy not this bargain of love, O people!), इस दा मूल ना खाना धोखा (suffer no illusion regarding its toll), जंगल बसती मिले ना ठोर (in neither wilderness nor city will you find refuge).",
                "poetic_hindi": "कोठे पे चढ़ कर दूँ मैं होका: 'इश्क न मोल लियो कोई लोका!';\nधोखा न खाना इसके कारण, जंगल-बस्ती मिले न ठौर!\nवाह-वाह! सजन का भेद है न्यारा!",
                "poetic_english": "From high roofs I shout to the passers-by: 'Never purchase this love, nor its bargain try!\nBe not deceived by its golden sky, for in forest or town no resting-places lie!'\nSublime is the cipher my Beloved weaves!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "आशक दोहीं जहानीं मुट्ठे, नाज़ मशूकां दे उह कुट्ठे,  ",
                    "इश्क दा फट्ट्या कोई ना छुट्टे, कीतो सू बांदा फट्ट फलोर ।  ",
                    "वाह वाह रमज़ सजन दी होर ।"
                ],
                "hindi_gloss": "आशक (सच्चे प्रेमी) दोहीं जहानीं (दोनों लोकों में) मुट्ठे (लुट जाते हैं), नाज़ मशूकां दे (माशूकों के नाज़-नखरों से) उह कुट्ठे (वे कुर्बान/कत्ल होते हैं), इश्क दा फट्ट्या (प्रेम के बाणों से घायल) कोई ना छुट्टे (कोई नहीं बच पाता), कीतो सू (उस प्रेम ने कर दिया है) बांदा (मनुष्य को) फट्ट फलोर (घावों से छलनी-छलनी)।",
                "english_gloss": "आशक दोहीं जहानीं मुट्ठे (Lovers are plundered in both worlds), नाज़ मशूकां दे उह कुट्ठे (slain by the coquetry of the Beloved), इश्क दा फट्ट्या (struck by the wound of love) कोई ना छुट्टे (none escapes), कीतो सू बांदा फट्ट फलोर (it tears open every seam of the mortal servant).",
                "poetic_hindi": "आशिक दोनों जहाँ में लुटते, माशूक के नाज़ों पे हैं कटते;\nइश्क का घायल कभी न छूटे, चीर दिया तन का हर छोर!\nवाह-वाह! सजन का भेद है न्यारा!",
                "poetic_english": "In both worlds the lovers are stripped of pride, slain by the glance where enchantments hide;\nNone struck by love's arrow can turn aside, torn open and wounded on every side!\nSublime is the cipher my Beloved weaves!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "दे दीदार होया जद राही, अचणचेत पई गल फाही,  ",
                    "डाढी कीती लापरवाही, मैनूं मिल गया ठग्ग लाहौर ।  ",
                    "वाह वाह रमज़ सजन दी होर ।"
                ],
                "hindi_gloss": "दे दीदार (एक क्षण अपनी दिव्य झांकी दिखाकर) होया जद राही (जब वह प्रस्थान कर गया), अचणचेत (अचानक ही) पई (पड़ गई) गल (गले में) फाही (फांसी), डाढी (कैसी भीषण) कीती (की है उसने) लापरवाही (बेपरवाही), मैनूं (मुझको) मिल गया (मिल गया है) ठग्ग (महा-ठग) लाहौर (लाहौर नगर का - शाह इनायत)।",
                "english_gloss": "दे दीदार होया जद राही (Having granted a fleeting vision, He departed), अचणचेत पई गल फाही (suddenly a fatal noose seized my neck), डाढी कीती लापरवाही (what immense indifference He displayed!), मैनूं मिल गया ठग्ग लाहौर (I fell into the hands of the Great Thug of Lahore!).",
                "poetic_hindi": "दरस दिखा कर राही हुआ, गले में अचानक फंदा पड़ा;\nकैसी बेपरवाही की उसने, लाहौर का ठग मुझको मिला!\nवाह-वाह! सजन का भेद है न्यारा!",
                "poetic_english": "He granted a glimpse and then walked away, casting a noose round my neck to stay;\nWhat heedless cruelty He did display—that Thug of Lahore stole my soul away!\nSublime is the cipher my Beloved weaves!"
            },
            {
                "stanza_number": 5,
                "original": [
                    "शीरीं है बिरहों दा खाणा, कोह चोटी फरहाद निमाणा,  ",
                    "यूसफ़ मिसर बज़ार विकाणा, उस नूं नाहीं वेखन कोर ।  ",
                    "वाह वाह रमज़ सजन दी होर ।"
                ],
                "hindi_gloss": "शीरीं (शीरीं) है (है) बिरहों दा (विरह का) खाणा (भोजन बन गई), कोह चोटी (पहाड़ की चोटियों पर) फरहाद निमाणा (दीन फरहाद ने छेनी चलाई), यूसफ़ (हज़रत यूसुफ) मिसर बज़ार विकाणा (मिस्र के बाजार में गुलाम की तरह बिके), उस नूं (उस सौन्दर्य को) नाहीं वेखन (नहीं देख सकते) कोर (अंधे संसारी)।",
                "english_gloss": "शीरीं है बिरहों दा खाणा (Shirin became the feast of separation's pangs), कोह चोटी फरहाद निमाणा (wretched Farhad carved the mountain peaks), यूसफ़ मिसर बज़ार विकाणा (Joseph was auctioned as a slave in Egypt's mart), उस नूं नाहीं वेखन कोर (blind eyes possess no power to perceive Him).",
                "poetic_hindi": "शीरीं बनी विरह का खाना, फरहाद ने पर्वत को काटा;\nयूसुफ मिस्र के हाट बिका था, अंधे न देखें उसका रूप अनोखा!\nवाह-वाह! सजन का भेद है न्यारा!",
                "poetic_english": "Shirin was devoured by grief alone; humble Farhad carved the mountain stone;\nIn Egypt's bazaar Joseph was thrown; to blind men His beauty remains unknown!\nSublime is the cipher my Beloved weaves!"
            },
            {
                "stanza_number": 6,
                "original": [
                    "लैला मजनूं दोवें बरदे, सोहनी डुब्बी विच बहर दे,  ",
                    "हीरा वंझाए सभ्भे घर दे, इस दी खिच्ची माही डोर ।  ",
                    "वाह वाह रमज़ सजन दी होर ।"
                ],
                "hindi_gloss": "लैला मजनूं (लैला और मजनू) दोवें (दोनों ही) बरदे (प्रेम के दास बन गए), सोहनी (सोहनी) डुब्बी (डूब गई) विच बहर दे (चनाब नदी के अथाह जल में), हीरा (हीर ने) वंझाए (त्याग दिए) सभ्भे घर दे (अपने कुल-कुटुंब के सभी लोग), इस दी (इस प्रेम की) खिच्ची (खींच ली) माही (माहीवाल/रांझा ने) डोर (आंतरिक डोर)।",
                "english_gloss": "लैला मजनूं दोवें बरदे (Layla and Majnun both became enslaved to love), सोहनी डुब्बी विच बहर दे (Sohni drowned in the torrential deep), हीर वंझाए सभ्भे घर दे (Heer renounced all her kinsfolk and home), इस दी खिच्ची माही डोर (pulled by the invisible thread of the Herdsman).",
                "poetic_hindi": "लैला-मजनूँ बने दास प्रेम के, सोहनी डूबी बीच भँवर के;\nहीर ने छोड़े सब परिजन घर के, माही ने खींची मन की डोर!\nवाह-वाह! सजन का भेद है न्यारा!",
                "poetic_english": "Layla and Majnun were slaves to love's sway; Sohni in the churning deep drowned away;\nHeer cast all her family and home away, pulled by the Herdsman's unseen ray!\nSublime is the cipher my Beloved weaves!"
            },
            {
                "stanza_number": 7,
                "original": [
                    "आशक फिरदे चुप्प चुपाते, जैसे मसत सदा मध माते,  ",
                    "दाम ज़ुलफ दे अन्दर फाथे, ओथे चल्ले वस्स ना ज़ोर ।  ",
                    "वाह वाह रमज़ सजन दी होर ।"
                ],
                "hindi_gloss": "आशक (सच्चे प्रेमी) फिरदे (घूमते हैं) चुप्प चुपाते (मौन और शांत), जैसे (मानो) मसत (अलमस्त) सदा (सदा) मध माते (दिव्य मदिरा के मद में मतवाले हों), दाम (जाल) ज़ुलफ दे अन्दर (प्रियतम की काली लटों के जाल में) फाथे (फंसे हुए हैं), ओथे (वहाँ) चल्ले (चलता) वस्स ना (न कोई वश) ज़ोर (न कोई बल)।",
                "english_gloss": "आशक फिरदे चुप्प चुपाते (Lovers wander silently, speaking no word), जैसे मसत सदा मध माते (like mystics perpetually intoxicated with vintage wine), दाम ज़ुलफ दे अन्दर फाथे (ensnared within the net of His dark tresses), ओथे चल्ले वस्स ना ज़ोर (where neither cunning nor force avails).",
                "poetic_hindi": "आशिक फिरते मौन-सधाए, जैसे मदिरा पी मतवाए;\nलटों के जाल में ऐसे फँसाए, चले न कोई वश या ज़ोर!\nवाह-वाह! सजन का भेद है न्यारा!",
                "poetic_english": "Lovers wander silent, speechless and still, drunk on the wine of the Beloved's will;\nCaught in the net of His tresses until no cunning or force can break the skill!\nSublime is the cipher my Beloved weaves!"
            },
            {
                "stanza_number": 8,
                "original": [
                    "जे उह आण मिले दिलजानी, उस तों जान करां कुरबानी,  ",
                    "सूरत दे विच यूसफ़ सानी, आलम दे विच जिस दा शोर ।  ",
                    "वाह वाह रमज़ सजन दी होर ।"
                ],
                "hindi_gloss": "जे (यदि) उह (वह) आण मिले (आकर मुझसे मिल जाए) दिलजानी (मेरा हृदय-प्राण प्रियतम), उस तों (उस पर) जान (अपने प्राण) करां (कर दूँ) कुरबानी (कुर्बान), सूरत दे विच (सौंदर्य में जो) यूसफ़ सानी (द्वितीय यूसुफ के समान अद्वितीय है), आलम दे विच (सारे संसार में) जिस दा (जिसके सौन्दर्य की) शोर (चर्चा और धूम है)।",
                "english_gloss": "जे उह आण मिले दिलजानी (If that Soul of my heart would come and meet me), उस तों जान करां कुरबानी (unto Him I would sacrifice my very life), सूरत दे विच यूसफ़ सानी (who in beauty is a second Joseph), आलम दे विच जिस दा शोर (whose renown resounds through all the world).",
                "poetic_hindi": "जो आ मिले वो दिलजानी, उस पे वारूँ जान दिवानी;\nरूप में जो है यूसुफ-सानी, जग में जिसकी धूम चहुँओर!\nवाह-वाह! सजन का भेद है न्यारा!",
                "poetic_english": "If that Darling of my soul would draw near, I'd sacrifice my life without fear;\nA second Joseph in beauty clear, whose fame is celebrated far and near!\nSublime is the cipher my Beloved weaves!"
            },
            {
                "stanza_number": 9,
                "original": [
                    "बुल्ल्हा शहु कोई ना वेखे, जो वेखे सो किसे ना लेखे,  ",
                    "उस दा रंग रूप ना रेखे, उह ई होवे हो के चोर ।  ",
                    "वाह वाह रमज़ सजन दी होर ।  ",
                    "आशक बिनां ना समझे कोर ।  ",
                    "वाह वाह रमज़ सजन दी होर ।"
                ],
                "hindi_gloss": "बुल्ल्हा (बुल्लेशाह कहता है) शहु (उस परम प्रभु को) कोई ना वेखे (सांसारिक चर्म-चक्षुओं से कोई नहीं देख सकता), जो वेखे (जो उसे देख लेता है) सो (वह) किसे ना लेखे (सांसारिक गणना और समाज के काम का नहीं रहता), उस दा (उसका) रंग रूप ना रेखे (न कोई निश्चित रंग है, न रूप, न रेखा), उह ई होवे (वह साधक स्वयं वही बन जाता है) हो के चोर (अहंकार को चुराकर)।",
                "english_gloss": "बुल्ल्हा शहु कोई ना वेखे (Bulleh says: that King none with physical eyes can see), जो वेखे (he who beholds Him) सो किसे ना लेखे (is counted of no worldly use anymore), उस दा रंग रूप ना रेखे (He has neither color, form, nor boundary), उह ई होवे (the seeker becomes Him alone) हो के चोर (stealing into His hidden Oneness).",
                "poetic_hindi": "बुल्ल्हा कहे, शाह को कोई न देखे, जो देखे सो जग के न लेखे;\nरूप-रंग न रेखा जिसके, वही बन जाए बन के चोर!\nवाह-वाह! सजन का भेद है न्यारा,\nआशिक बिना न जाने अंधा जग सारा!",
                "poetic_english": "Bulleh says: no eye can behold that King; who sees Him is dead to what mortals sing;\nNo color or contour or outward thing; he turns into Him, a secret wing!\nSublime is the cipher my Beloved weaves;\nWhich none but the lover's deep heart perceives!"
            }
        ],
        "sufi_commentary": "Kafi 158 is an epic catalogue of mystical martyrdom and the esoteric cipher ('रमज़') of Divine Love. Bulleh begins by warning the casual passerby: never buy the merchandise of Ishq ('इश्क वेहाज्यु कोई ना लोका'), for it guarantees neither worldly comfort nor spiritual reputation. He then invokes the great archetypes of mystical passion: Farhad chipping away at Mount Bisutun, Yusuf sold into slavery in Egypt, Layla and Majnun, Sohni drowning in the Chenab, and Heer intoxicated by Ranjha's flute. In Stanza 4, Bulleh names his personal enchanter: 'ठग्ग लाहौर' (The Thug of Lahore)—Shah Inayat, who robbed him of all egoic pride. In the final stanza, Bulleh reaches the pinnacle of apophatic mysticism: the Sovereign King has no physical color, form, or outline ('रंग रूप ना रेखे'). Whoever truly beholds Him ceases to belong to worldly calculations, dissolving into the Divine through holy stealth ('उह ई होवे हो के चोर')."
    },
    {
        "id": 159,
        "title_punjabi": "वल परदे विच पाइआ यार आपे मेल मिलाइआ ए",
        "title_english": "Behind the Veil the Friend Revealed Himself, Uniting Me to His Grace",
        "raga": "Raga Tilang / Kafi",
        "meter": "Matrik Chhand (16-14 matras)",
        "theme": "The Crow Stealing the Cotton, Transmutation of Majnun into Layla, and the Solitary Alif",
        "historical_context": "A deeply esoteric Kafi utilizing pastoral spinning metaphors and mystical transmutation. The crow of mortality steals the sliver of worldly karma ('पूनी लै गया कां'), forcing the seeker into exile. The lover abandons all conventional alphabetic learning (the 28/30 letters of knowledge) to study only the single letter Alif (the symbol of Absolute Oneness). Majnun is so completely absorbed in Layla that he becomes Layla himself.",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "हुन मैं मोई नी मेरीए मां, मेरी पूनी लै गया कां,  ",
                    "पिच्छे डों डों करदी जां, जिस मेरा वतन छुडाया ए ।  ",
                    "वल परदे विच पाइआ यार आपे मेल मिलाइआ ए ।"
                ],
                "hindi_gloss": "हुन (अब) मैं (मैं) मोई (मर मिटी हूँ) नी मेरीए मां (हे मेरी माँ!), मेरी (मेरी कताई की) पूनी (कपास की पूनी) लै गया (छीन कर ले गया) कां (कौआ), पिच्छे (उसके पीछे-पीछे) डों डों (विलाप करती हुई) करदी जां (दौड़ती जाती हूँ), जिस (जिसने) मेरा (मेरा पैतृक) वतन (वतन) छुडाया ए (छुड़वा दिया है)। वल (घूँघट की सिलवटों और) परदे विच (पर्दे के भीतर) पाइआ यार (प्रियतम ने दर्शन दिए हैं) आपे (स्वयं ही उसने) मेल मिलाइआ ए (मुझसे अपना मिलन रचाया है)।",
                "english_gloss": "हुन मैं मोई (Now I am undone/dead) नी मेरीए मां (O my mother!), मेरी पूनी (my cotton roll) लै गया कां (the crow has snatched away), पिच्छे डों डों करदी जां (crying out in pursuit I run behind it), जिस मेरा वतन छुडाया ए (which caused me to abandon my native home). वल परदे विच (Through the folds of the veil) पाइआ यार (the Beloved showed Himself) आपे मेल मिलाइआ ए (and Himself accomplished our union).",
                "poetic_hindi": "अब मैं मरी री मेरी माँ! मेरी पूनी ले गया काग,\nपीछे रोती-धोती दौड़ी, जिसने छुड़वाया निज धाम;\nपर्दे की ओट में प्रीतम पाया, उसने खुद ही मेल मिलाया!",
                "poetic_english": "Now I am slain, O mother mine! The crow has snatched my spool of twine;\nWeeping I chase its flight divine, which tore me from my native shrine;\nThrough veil's soft folds my Love drew near, and forged our union pure and clear!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "कांवां पूनी दईं पिया दे नां, तेरियां मिन्नतां करदी हां,  ",
                    "ज़रबां तेरियां जरनी हां, जिस मैनूं दूर कराइआ ए ।  ",
                    "वल परदे विच पाइआ यार आपे मेल मिलाइआ ए ।"
                ],
                "hindi_gloss": "कांवां (हे कौए!) पूनी (यह कपास की पूनी) दईं (दे देना) पिया दे नां (मेरे प्रियतम के नाम पर), तेरियां (तेरी) मिन्नतां (अनेक प्रार्थनाएं/विनती) करदी हां (करती हूँ), ज़रबां (तेरे कठोर प्रहार/चोटें) तेरियां (तेरी) जरनी हां (सहन करती हूँ), जिस (जिस विरह ने) मैनूं (मुझको) दूर कराइआ ए (प्रियतम से दूर कर दिया है)।",
                "english_gloss": "कांवां (O crow!) पूनी दईं (surrender this cotton spool) पिया दे नां (in my Beloved's sacred name), तेरियां मिन्नतां करदी हां (I plead with thee with folded hands), ज़रबां तेरियां जरनी हां (I endure thy sharp pecks and strikes), जिस मैनूं दूर कराइआ ए (which has cast me far from Him).",
                "poetic_hindi": "हे काग! ये पूनी दे पिया के नाम, करती हूँ मैं कोटि प्रणाम;\nसहूँ चोटें तेरी हर शाम, जिसने मुझको दूर कराया!\nपर्दे की ओट में प्रीतम पाया, उसने खुद ही मेल मिलाया!",
                "poetic_english": "O crow, give back that spool of love, in the Name of my Beloved above;\nI plead with tears and suffer blows, which parted me where sorrow flows;\nThrough veil's soft folds my Love drew near, and forged our union pure and clear!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "हुन मैनूं भला ना लग्गदा शोर, मैं घर खिड़िआ शुगूफ़ा होर,  ",
                    "बे ना ते ना से ना होर, इक्को अलफ़ पढ़ाइआ ए ।  ",
                    "वल परदे विच पाइआ यार आपे मेल मिलाइआ ए ।"
                ],
                "hindi_gloss": "हुन (अब) मैनूं (मुझको) भला ना लग्गदा (अच्छा नहीं लगता) शोर (संसार और शास्त्रों का कोलाहल), मैं घर (मेरे अंतःकरण रूपी घर में) खिड़िआ (खिल उठा है) शुगूफ़ा (एक दिव्य पुष्प/कली) होर (अलौकिक), बे ना (न 'बे' वर्ण) ते ना (न 'ते' वर्ण) से ना होर (न 'से' और अन्य अक्षर), इक्को (एकमात्र) अलफ़ (अद्वैत का अक्षर 'अलिफ़') पढ़ाइआ ए (मुर्शिद ने पढ़ाया है)।",
                "english_gloss": "हुन मैनूं भला ना लग्गदा शोर (Now I take no pleasure in noisy disputes), मैं घर खिड़िआ शुगूफ़ा होर (within my home a different mystical flower has bloomed), बे ना ते ना से ना होर (neither 'Be', nor 'Te', nor 'Se' nor any other letter), इक्को अलफ़ पढ़ाइआ ए (only the solitary letter 'Alif' of Oneness has my Master taught).",
                "poetic_hindi": "अब भाए न जग का शोर, खिला हृदय में गुलशन और;\nन 'बे', न 'ते', न 'से' का दौर, केवल एक 'अलिफ़' पढ़ाया!\nपर्दे की ओट में प्रीतम पाया, उसने खुद ही मेल मिलाया!",
                "poetic_english": "No noisy chatter soothes my mind; a rarer blossom here I find;\nNo 'Be' or 'Te' of scholastic kind—one 'Alif' alone left all behind!\nThrough veil's soft folds my Love drew near, and forged our union pure and clear!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "हुन मैनूं मजनूं आखो ना, दिन दिन लैला हुन्दा जां,  ",
                    "डेरा यार बणाए तां, इह तन बंगला बणाइआ ए ।  ",
                    "वल परदे विच पाइआ यार आपे मेल मिलाइआ ए ।"
                ],
                "hindi_gloss": "हुन (अब) मैनूं (मुझको) मजनूं (मजनू) आखो ना (मत कहो), दिन दिन (दिन-प्रतिदिन) लैला (स्वयं लैला) हुन्दा जां (बनता जा रहा हूँ), डेरा (अपना स्थायी निवास) यार (प्रियतम) बणाए तां (बना सके, इसलिए), इह तन (इस शरीर को) बंगला (सुंदर महल) बणाइआ ए (बना दिया है)।",
                "english_gloss": "हुन मैनूं मजनूं आखो ना (Call me Majnun no more!), दिन दिन लैला हुन्दा जां (day by day I turn into Layla herself), डेरा यार बणाए तां (so that the Beloved may pitch His camp), इह तन बंगला बणाइआ ए (I have transformed this body into a radiant palace).",
                "poetic_hindi": "मजनूँ कह कर मत बुलाओ, दिन-दिन लैला बनती जाऊँ;\nयार का डेरा यहाँ सजाऊँ, तन को सुंदर भवन बनाया!\nपर्दे की ओट में प्रीतम पाया, उसने खुद ही मेल मिलाया!",
                "poetic_english": "Call me Majnun no more in vain; as Layla now I walk the plain;\nThat my Beloved here may reign, this body turns to a palace sane!\nThrough veil's soft folds my Love drew near, and forged our union pure and clear!"
            },
            {
                "stanza_number": 5,
                "original": [
                    "बुल्ल्हा इनायत करे हज़ार, इहो कौल इहो तकरार,  ",
                    "वल परदे विच पाइआ यार आपे मेल मिलाइआ ए ।"
                ],
                "hindi_gloss": "बुल्ल्हा (बुल्लेशाह कहता है) इनायत (मुर्शिद शाह इनायत) करे हज़ार (हजारों कृपाएं करे), इहो (यही हमारा) कौल (सत्य वचन) इहो (यही हमारा) तकरार (दृढ़ निश्चय/संवाद है), वल परदे विच पाइआ यार आपे मेल मिलाइआ ए ।",
                "english_gloss": "बुल्ल्हा (Bulleh cries) इनायत करे हज़ार (may Inayat shower thousands of blessings), इहो कौल (this is the sole covenant) इहो तकरार (this is the immutable declaration): behind the veil the Friend revealed Himself, and Himself accomplished our union.",
                "poetic_hindi": "बुल्ल्हा कहे, इनायत की बहार, यही कौल और यही इकरार;\nपर्दे की ओट में प्रीतम पाया, उसने खुद ही मेल मिलाया!",
                "poetic_english": "Bulleh cries: Inayat's bounties stream; this is my covenant and my theme:\nThrough veil's soft folds my Love supreme, fulfilled Himself our holy dream!"
            }
        ],
        "sufi_commentary": "Kafi 159 touches the mystical heights of Fana fi'l-Mahbub (Annihilation in the Beloved). In Stanza 3, Bulleh repeats his famous doctrine of sacred illiteracy: conventional religion teaches the alphabet of worldly division ('बे', 'ते', 'से'), while the Kamil Murshid teaches only the solitary vertical stroke of 'Alif' (ا)—the symbol of Allah, the Indivisible Absolute. In Stanza 4, Bulleh captures the supreme psychological phenomenon of non-dual love: 'हुन मैनूं मजनूं आखो ना, दिन दिन लैला हुन्दा जां' (Call me Majnun no more, day by day I am turning into Layla). In constant, unremitting remembrance, the subject dissolves into the object; the lover becomes the Beloved. The body is no longer a cage of dust, but a palace ('बंगला') prepared for the indwelling of Master Shah Inayat."
    },
    {
        "id": 160,
        "title_punjabi": "वत्त ना करसां मान रंझेटे यार दा वे अड़िआ",
        "title_english": "Never Again Shall I Boast of My Herdsman's Love, O Friend!",
        "raga": "Raga Kafi / Bhairavi",
        "meter": "Baint / Davayya (16-14 matras)",
        "theme": "The Absolute Culmination of Surrender, Annihilation of Egoic Pride, and Final Theophany",
        "historical_context": "The crowning masterpiece and grand finale of Bulleh Shah's entire poetic corpus (Kafi 160). After traversing the entire path of love, longing, societal censure, philosophical non-duality, and mystical madness, Bulleh reaches the ultimate station of surrender: the eradication of even spiritual pride ('मान'). The seeker realizes that boasting of one's love or claiming intimacy with the Divine is the final subtle trap of the ego. When every claim is surrendered, the Master steps into the heart and the eternal hour of direct vision arrives ('होया वकत दीदार दा वे अड़िआ').",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "वत्त ना करसां मान रंझेटे यार दा वे अड़िआ ।"
                ],
                "hindi_gloss": "वत्त (पुनः/कभी फिर) ना (नहीं) करसां (करूँगी) मान (अहंकार/गर्व) रंझेटे यार दा (अपने प्यारे यार रांझा के प्रेम का) वे अड़िआ (हे मेरे प्यारे सखा/मित्र!)।",
                "english_gloss": "वत्त ना करसां मान (Never again shall I harbor pride or boast) रंझेटे यार दा (of my beloved Herdsman Ranjha's love) वे अड़िआ (O my dear friend!).",
                "poetic_hindi": "फिर कभी न करूँगी गुमान रांझा यार का रे सखा!",
                "poetic_english": "Never again shall I boast of my Herdsman's love, O dear companion!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "जान करां कुरबान भेत ना दस्सना एं,  ",
                    "ढूंडां तकीए दुआर तैनूं उट्ठ नस्सना एं,  ",
                    "रल मिल सईआं पुच्छन गईआं,  ",
                    "होया वकत भंडार दा वे अड़िआ ।  ",
                    "वत्त ना करसां मान रंझेटे यार दा वे अड़िआ ।"
                ],
                "hindi_gloss": "जान (अपने प्राण) करां कुरबान (तुझ पर न्योछावर करती हूँ, फिर भी) भेत (अपना आंतरिक भेद) ना दस्सना एं (तू मुझे नहीं बताता), ढूंडां (मैं तुझे खोजती हूँ) तकीए दुआर (दरगाहों, तकियों और द्वारों पर) तैनूं (और तू) उट्ठ नस्सना एं (उठकर भाग जाता है), रल मिल (मिल-जुलकर) सईआं (सखियाँ) पुच्छन गईआं (उसका पता पूछने गईं), होया वकत (अब समय आ गया है) भंडार दा (भंडारे/महा-प्रसाद के वितरण का) वे अड़िआ ।",
                "english_gloss": "जान करां कुरबान (I sacrifice my life, yet) भेत ना दस्सना एं (Thou revealest not Thy secret), ढूंडां तकीए दुआर (I search shrines and portals) तैनूं उट्ठ नस्सना एं (and Thou fleest away), रल मिल सईआं पुच्छन गईआं (companions gathered to inquire of Thee), होया वकत भंडार दा (the hour of the great mystical banquet has struck) वे अड़िआ (O friend!).",
                "poetic_hindi": "जान करूँ कुर्बान, भेद तू न बतलाए,\nखोजूँ दरगाहों पर, तू उठ भाग जाए;\nसखियाँ पूछने गईं सब मिल कर,\nभंडारे का समय हुआ रे सखा!\nफिर कभी न करूँगी गुमान रांझा यार का रे सखा!",
                "poetic_english": "I lay my life down, yet Thy secret remains unsaid;\nI seek Thee at shrines, but away Thou hast fled;\nCompanions went together to search where Thou led;\nThe hour of the holy banquet has sped!\nNever again shall I boast of my Herdsman's love, O dear companion!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "इश्क अल्लाह दी ज़ात लोकां दा मेहणा,  ",
                    "केहनूं करां पुकार किसे नहीं रहणा,  ",
                    "ओसे दी गल्ल उहो जाणे,  ",
                    "कौन कोई मारदा वे अड़िआ ।  ",
                    "वत्त ना करसां मान रंझेटे यार दा वे अड़िआ ।"
                ],
                "hindi_gloss": "इश्क (यह दिव्य प्रेम) अल्लाह दी ज़ात (स्वयं अल्लाह का मूल स्वरूप है) लोकां दा मेहणा (किंतु संसारी लोगों के लिए यह ताना और कलंक है), केहनूं (किसके आगे) करां पुकार (मैं गुहार लगाऊँ जब) किसे नहीं रहणा (यहाँ किसी को सदा नहीं रहना), ओसे दी गल्ल (उस परमात्मा की बात को) उहो जाणे (वही जान सकता है), कौन कोई मारदा (कि कौन किसे प्रेम-बाणों से मार रहा है) वे अड़िआ ।",
                "english_gloss": "इश्क (Love) अल्लाह दी ज़ात (is the very Essence of God), लोकां दा मेहणा (yet mortals make it a taunt and scandal), केहनूं करां पुकार (unto whom shall I cry aloud) किसे नहीं रहणा (when no earthly mortal shall endure?), ओसे दी गल्ल उहो जाणे (His mystery He alone comprehends), कौन कोई मारदा (who slays whom in love's battle) वे अड़िआ (O friend!).",
                "poetic_hindi": "इश्क तो रब की ज़ात है, दुनिया का ताना,\nकिसको पुकारूँ? जग को तो है मिट जाना;\nउसकी बात वोही बस जाने,\nकौन किसे है मारता रे सखा!\nफिर कभी न करूँगी गुमान रांझा यार का रे सखा!",
                "poetic_english": "Love is God's Essence, though mortals mock and chide;\nTo whom shall I cry when none shall abide?\nHis mystery only He can decide:\nWho strikes whom down on passion's tide?\nNever again shall I boast of my Herdsman's love, O dear companion!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "अज्ज अजोकड़ी रात मेरे घर वस्स खां वे अड़िआ,  ",
                    "दिल दियां घुंढियां खोल्ह असां नाल हस्स खां वे अड़िआ ,  ",
                    "जद कीते कौल करार की इतबार,  ",
                    "सोहने यार दा वे अड़िआ ।  ",
                    "वत्त ना करसां मान रंझेटे यार दा वे अड़िआ ।"
                ],
                "hindi_gloss": "अज्ज अजोकड़ी रात (आज की इस पावन रात) मेरे घर (मेरे हृदय-गृह में) वस्स खां (विराजमान हो जाओ) वे अड़िआ (हे मेरे प्यारे!), दिल दियां (हृदय की) घुंढियां (गुप्त गांठें/कपट) खोल्ह (खोलकर) असां नाल (हमारे साथ) हस्स खां (हंस-बोल लो) वे अड़िआ, जद (जब) कीते कौल करार (वचन और प्रतिज्ञाएं की थीं) की इतबार (तब कैसा अविश्वास) सोहने यार दा वे अड़िआ ।",
                "english_gloss": "अज्ज अजोकड़ी रात (Just for this single sacred night) मेरे घर वस्स खां (dwell within my home) वे अड़िआ (O dear one!), दिल दियां घुंढियां खोल्ह (open the secret knots of the heart) असां नाल हस्स खां (and laugh and converse with me), जद कीते कौल करार (when solemn pledges were sealed) की इतबार (what doubt can remain of my Fair Beloved's love) वे अड़िआ (O friend!).",
                "poetic_hindi": "आज की रात मेरे घर बस जा प्यारे,\nगांठें खोल दिल की, हँस ले हमारे;\nजब किए थे कौल-करार संग द्वारे,\nफिर क्या अविश्वास सुंदर यार का रे सखा!\nफिर कभी न करूँगी गुमान रांझा यार का रे सखा!",
                "poetic_english": "Dwell in my chamber for this one blessed night;\nUnloose heart's tight knots in laughter and light;\nWhen eternal covenants were sworn in His sight,\nWhat doubt can shadow my Beloved bright?\nNever again shall I boast of my Herdsman's love, O dear companion!"
            },
            {
                "stanza_number": 5,
                "original": [
                    "इक करदियां ख़ुदी हंकार उहनां नूं तारनैं वे अड़िआ,  ",
                    "इक रहन्दियां नित्त ख़ुआर सड़ियां नूं साड़नैं वे अड़िआ,  ",
                    "मैंडे सोहने यार दा की इतबार तेरे प्यार दा वे अड़िआ ।  ",
                    "वत्त ना करसां मान रंझेटे यार दा वे अड़िआ ।"
                ],
                "hindi_gloss": "इक (कुछ लोग) करदियां (करते हैं) ख़ुदी (अहंकार) हंकार (और घमंड) उहनां नूं (उन्हें तू) तारनैं (भवसागर से पार उतार देता है) वे अड़िआ, इक (और कुछ विरहिणी आत्माएं) रहन्दियां (रहती हैं) नित्त (सदा) ख़ुआर (दुखी और तड़पती हुई) सड़ियां नूं (उन जली-सुलगी आत्माओं को) साड़नैं (और अधिक विरह में जलाता है) वे अड़िआ, मैंडे (मेरे) सोहने यार दा (सुंदर प्रियतम का) की इतबार (क्या भरोसा) तेरे प्यार दा वे अड़िआ ।",
                "english_gloss": "इक करदियां ख़ुदी हंकार (Some strut in ego and pride) उहनां नूं तारनैं (and yet Thou ferriest them across) वे अड़िआ, इक रहन्दियां नित्त ख़ुआर (while others suffer constant grief and torment) सड़ियां नूं साड़नैं (and Thou burnest the already burning) वे अड़िआ, मैंडे सोहने यार दा (unto my Fair Beloved) की इतबार तेरे प्यार दा (what predictable reliance can be placed upon Thy wild love) वे अड़िआ (O friend!).",
                "poetic_hindi": "अहंकारी-दंभियों को तू पार उतारे,\nसुलगती विरहणियों को और जलाए;\nमेरे सुंदर यार का क्या ऐतबार,\nकैसी तेरी बेपरवाह प्यार की रीत रे सखा!\nफिर कभी न करूँगी गुमान रांझा यार का रे सखा!",
                "poetic_english": "The proud and the boastful Thou ferriest through;\nWhile the weeping and burnt Thou scorchest anew;\nO my Fair Beloved, beyond reason and view,\nWhat predictable path can Thy passion pursue?\nNever again shall I boast of my Herdsman's love, O dear companion!"
            },
            {
                "stanza_number": 6,
                "original": [
                    "चिक्कड़ भरियां नाल झूंमर घत्तना एं वे अड़िआ,  ",
                    "मैं लाइआ हार शिंगार उट्ठ नस्सना एं वे अड़िआ,  ",
                    "बुल्ल्हा शहु घर आया प्यारा,  ",
                    "होया वकत दीदार दा वे अड़िआ ।  ",
                    "वत्त ना करसां मान रंझेटे यार दा वे अड़िआ ।"
                ],
                "hindi_gloss": "चिक्कड़ भरियां नाल (कीचड़ से लथपथ मैली-कुचैली स्त्रियों के साथ) झूंमर (झूमर नृत्य) घत्तना एं (तू नाचता फिरता है) वे अड़िआ, मैं (और मैंने जब) लाइआ (सजाया) हार शिंगार (सुंदर श्रृंगार और पुष्पहार) उट्ठ नस्सना एं (तो तू उठकर भाग जाता है) वे अड़िआ, बुल्ल्हा (अंततः बुल्लेशाह कहता है) शहु (प्रभु-प्रियतम) घर आया प्यारा (मेरे घर पधार चुका है), होया वकत (अब समय हो चुका है) दीदार दा (साक्षात्कार और शाश्वत दीदार का) वे अड़िआ ।",
                "english_gloss": "चिक्कड़ भरियां नाल (With those smeared in mud and dust) झूंमर घत्तना एं (Thou dancest the ecstatic Jhumar) वे अड़िआ, मैं लाइआ हार शिंगार (and when I arrayed myself in fine bridal adornments) उट्ठ नस्सना एं (Thou didst leap up and flee) वे अड़िआ, बुल्ल्हा शहु घर आया प्यारा (now Bulleh's Beloved King has entered my courtyard), होया वकत दीदार दा (the auspicious hour of eternal Vision has arrived!) वे अड़िआ (O friend!).",
                "poetic_hindi": "कीचड़ में लथपथ संग झूमर तू पावे,\nमैं करूँ श्रृंगार तो उठ भाग जावे;\nबुल्ल्हा कहे, शाह घर आया पियारा,\nहो गया समय दीदार का रे सखा!\nफिर कभी न करूँगी गुमान रांझा यार का रे सखा!",
                "poetic_english": "With those smeared in mire Thou dancest in glee;\nWhen I put on fine jewels, away Thou didst flee;\nBulleh cries: the Beloved has entered to me;\nThe hour of supreme Vision shines clear and free!\nNever again shall I boast of my Herdsman's love, O dear companion!"
            }
        ],
        "sufi_commentary": "Kafi 160 is the majestic, definitive finale of Baba Bulleh Shah's entire corpus of 160 Kafian. It represents the final, supreme purification of the soul: the surrender of spiritual pride. Throughout the spiritual journey, the seeker risks spiritual conceit—boasting that one is chosen, beloved, or superior in devotion. Here, Bulleh renounces even that last vestige of the ego: 'वत्त ना करसां मान रंझेटे यार दा वे अड़िआ' (Never again shall I boast of Ranjha's love). The Beloved's ways are utterly beyond human logic: He dances the ecstatic Jhumar dance with those smeared in mud ('चिक्कड़ भरियां'), while fleeing from those adorned in proud spiritual finery ('हार शिंगार'). Love is not a human achievement; 'इश्क अल्लाह दी ज़ात'—Love is the very Essence of God Himself. When all pride, claims, and self-identities are pulverized into dust, the curtain lifts, and the Sovereign Beloved steps into the humble courtyard: 'बुल्ल्हा शहु घर आया प्यारा, होया वकत दीदार दा वे अड़िआ!' The journey ends not in dogma or speculation, but in direct, unmediated, eternal Vision (Didar)."
    }
]

# Lexicon updates for batch 156-160
new_lexicon_entries = {
    "लटका": {
        "gurmukhi": "ਲਟਕ",
        "hindi": "नाज़-नखरा, मस्तानी चाल, लुभावनी अदा",
        "english": "Graceful swaying gait, coquettish charm, enchanting stride",
        "context": "लटकां नाल चलेंदे ओ (Kafi 156)"
    },
    "ज़न्नार": {
        "gurmukhi": "ਜ਼ੁੰਨਾਰ",
        "hindi": "जनेऊ, कण्ठ का पवित्र धागा (सूफी शायरी में बाह्य धर्म का प्रतीक)",
        "english": "Sacred thread (worn by Brahmins / Zoroastrians; symbol of outward religion)",
        "context": "घत्त ज़न्नार कुफ़र दा गल विच (Kafi 156)"
    },
    "छिंझ": {
        "gurmukhi": "ਛਿੰਝ",
        "hindi": "दंगल, कुश्ती का अखाड़ा / ग्रामीण मेला",
        "english": "Wrestling tourney, open wrestling arena or festival",
        "context": "वाह वाह छिंझ पई दरबार (Kafi 157)"
    },
    "रमज़": {
        "gurmukhi": "ਰਮਜ਼",
        "hindi": "गूढ़ संकेत, रहस्यमयी पहेली, गुप्त भेद",
        "english": "Esoteric cipher, subtle hint, mystical secret",
        "context": "वाह वाह रमज़ सजन दी होर (Kafi 158)"
    },
    "शुगूफ़ा": {
        "gurmukhi": "ਸ਼ਗੂਫ਼ਾ",
        "hindi": "कली, नव-प्रस्फुटित पुष्प, अलौकिक रहस्य",
        "english": "Bud, blossom, wondrous unfolding mystery",
        "context": "मैं घर खिड़िआ शुगूफ़ा होर (Kafi 159)"
    },
    "झूंमर": {
        "gurmukhi": "ਝੂੰਮਰ",
        "hindi": "झूमर (पंजाब का एक पारंपरिक गोलाकार उल्लासमय लोक-नृत्य)",
        "english": "Jhumar (traditional circular ecstatic folk dance of Punjab)",
        "context": "चिक्कड़ भरियां नाल झूंमर घत्तना एं (Kafi 160)"
    },
    "दीदार": {
        "gurmukhi": "ਦੀਦਾਰ",
        "hindi": "साक्षात्कार, प्रत्यक्ष दर्शन, परमात्मा का सान्निध्य",
        "english": "Direct beatific vision, Divine sight",
        "context": "होया वकत दीदार दा वे अड़िआ (Kafi 160)"
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

    # Update Checkpoint to 100% COMPLETE!
    checkpoint = {
        "last_processed_kafi_id": 160,
        "completed_count": 160,
        "total": 160,
        "next_kafi_id": None,
        "status": "completed"
    }
    with open(CHECKPOINT_PATH, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print("Checkpoint updated: 160/160 COMPLETED! Status: completed")

if __name__ == "__main__":
    save_batch()
