# -*- coding: utf-8 -*-
"""
Process Kafian 111 to 115 for Bulleh Shah Trilingual Edition.
Part 3 (भाग 3: काफ़ियां 101-160).
"""

import json
import os

BASE_DIR = r"c:\my-code\Bulleh-Shah"
DATA_DIR = os.path.join(BASE_DIR, "data")
KAFIAN_DIR = os.path.join(DATA_DIR, "kafian")
CHECKPOINT_FILE = os.path.join(DATA_DIR, "checkpoint.json")
LEXICON_FILE = os.path.join(DATA_DIR, "punjabi_sufi_lexicon.json")

kafian_data = [
    {
        "id": 111,
        "title": "नी कुटीचल मेरा नां",
        "title_english": "O Sisters, 'The Bruised and Beaten One' is My Name!",
        "historical_context": "यह 5 बंधों की एक अत्यंत मर्मस्पर्शी, व्यंग्यात्मक और प्रतीकात्मक काफी है। 'कुटीचल' उस विद्रोही साधिका (आत्मा) का नाम है जिसे रूढ़िवादी समाज, परिवार, माता-पिता, ससुराल और मदरसे के मौलवी—सभी ने मिलकर पीटा और प्रताड़ित किया है। मुल्ला उसे अलिफ़ (एकत्व) से आगे नहीं जाने देता और जूतियां मारता है। परिजन उसे घर से निकाल देते हैं। समाज उसे किसी भी रूप में स्वीकार नहीं करता। अंत में साधिका कहती है कि जब परमात्मा का यह प्रेम-रोग तुम्हें भी लगेगा, तभी तुम सच्चा न्याय कर पाओगे।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: नी कुटीचल मेरा नां)",
        "raga": "राग काफी / बिलावल",
        "theme": "इश्क के कारण सामाजिक प्रताड़ना, अलिफ़ की निष्ठा, जाति-समाज से निष्कासन, सच्चा न्याय",
        "stanzas": [
            {
                "original": [
                    "मुल्लां मैनूं सबक पढ़ाइआ, अलफों अग्गे कुझ्झ ना आया,  ",
                    "उस दियां जुत्तियां खांदी सां, नी कुटीचल मेरा नां ।"
                ],
                "hindi_gloss": [
                    "मुल्लां (मौलवी ने) मैनूं (मुझको) सबक (मदरसे का पाठ) पढ़ाइआ (पढ़ाया), अलफों (परंतु अलिफ़/एक परमात्मा से) अग्गे (आगे बढ़कर मेरे मन में) कुझ्झ (कुछ भी) ना (नहीं) आया (समाया),",
                    "उस (उस मुल्ला) दियां (की) जुत्तियां (जूतियां और मार) खांदी (सदा खाती) सां (रही हूँ), नी (अरी सखी) कुटीचल (कुटीचल/मार खाई हुई) मेरा (मेरा) नां (नाम पड़ गया है) ।"
                ],
                "english_gloss": [
                    "मुल्लां मैनूं सबक पढ़ाइआ (the Mullah taught me the lesson), अलफों अग्गे कुझ्झ ना आया (beyond Alif, nothing would enter my mind),",
                    "उस दियां जुत्तियां खांदी सां (I bore his slippers and blows), नी कुटीचल मेरा नां (O sisters, 'Kutichal' / the Bruised One is my name) ।"
                ],
                "poetic_hindi": [
                    "मुल्ला ने मुझे सबक पढ़ाया, अलिफ़ से आगे कुछ न भाया,",
                    "उसकी जूतियां खाती रही मैं, 'कुटीचल' मेरा नाम कहाया !"
                ],
                "poetic_english": [
                    "The Mullah taught his rigid creed; past 'Alif' not a letter stayed;",
                    "Beneath his beating slippers bruised: 'Kutichal' is the name I made!"
                ]
            },
            {
                "original": [
                    "किवें किवें दो अक्खियां लाईआं, रल के सईआं मारन आईआं,  ",
                    "नाले मारे बाबल मां, नी कुटीचल मेरा नां ।"
                ],
                "hindi_gloss": [
                    "किवें किवें (जैसे-तैसे/संयोगवश) दो (दोनों) अक्खियां (नेत्रों की) लाईआं (प्रीत लगाई मैंने प्रियतम से), रल (इकट्ठी होकर) के (करके) सईआं (सखियां भी) मारन (मारने) आईआं (दौड़ीं),",
                    "नाले (और साथ ही) मारे (मारते हैं) बाबल (पिता और) मां (माता भी), नी (अरी) कुटीचल (कुटीचल) मेरा (मेरा) नां (नाम है) ।"
                ],
                "english_gloss": [
                    "किवें किवें दो अक्खियां लाईआं (somehow my two eyes pledged their love), रल के सईआं मारन आईआं (friends gathered in a pack to beat me),",
                    "नाले मारे बाबल मां (and mother and father struck me too), नी कुटीचल मेरा नां (O sisters, 'Kutichal' is my name) ।"
                ],
                "poetic_hindi": [
                    "जैसे-तैसे अंखियां जोड़ीं, सखियां मारने दौड़ीं मोरी,",
                    "माता-पिता भी डंडा बरसाएँ, घायल हुई यह काया गोरी !",
                    "सखी री, 'कुटीचल' मेरा नाम !"
                ],
                "poetic_english": [
                    "Somehow my eyes were bound in love; my girlhood friends rushed in to strike;",
                    "My mother and father beat me sore, treating me with cold dislike:",
                    "O sisters, 'Kutichal' is my name!"
                ]
            },
            {
                "original": [
                    "साहवरे सानूं वड़न ना देंदे, नानक दादक घरों कढेंदे,  ",
                    "मेरा पेके नहीउं थां, नी कुटीचल मेरा नां ।"
                ],
                "hindi_gloss": [
                    "साहवरे (ससुराल वाले) सानूं (मुझको द्वार के भीतर) वड़न (प्रवेश करने) ना (नहीं) देंदे (देते), नानक (नाना का कुल) दादक (और दादा का परिवार) घरों (घर से बाहर) कढेंदे (निकाल फेंकता है),",
                    "मेरा (मेरा तो अपने) पेके (मायके में भी) नहीउं (नहीं रहा कोई) थां (स्थान/ठिकाना), नी (हे सखी) कुटीचल (कुटीचल) मेरा (मेरा) नां (नाम है) ।"
                ],
                "english_gloss": [
                    "साहवरे सानूं वड़न ना देंदे (in-laws permit me not to cross their door), नानक दादक घरों कढेंदे (maternal and paternal kin cast me out),",
                    "मेरा पेके नहीउं थां (I have no shelter even at my father's hearth), नी कुटीचल मेरा नां (O sisters, 'Kutichal' is my name) ।"
                ],
                "poetic_hindi": [
                    "ससुराल में मुझको घुसने न दें, ननिहाल-ददिहाल ने बाहर निकाला,",
                    "मायके में भी कोई ठौर नहीं, प्रेम ने ऐसा रूप संभाला !",
                    "सखी री, 'कुटीचल' मेरा नाम !"
                ],
                "poetic_english": [
                    "My in-laws bar the bridal door; both mother’s and father’s kin cast me out;",
                    "No refuge in my childhood home, a wanderer mocked with scorn and shout:",
                    "O sisters, 'Kutichal' is my name!"
                ]
            },
            {
                "original": [
                    "पढ़न सेती सभ मारन आहीं, बिनां पढ़आं हुन छड्डदा नाहीं,  ",
                    "नी मैं मुड़के कित वल्ल जां, नी कुटीचल मेरा नां ।"
                ],
                "hindi_gloss": [
                    "पढ़न (अलिफ़ का पाठ पढ़ने) सेती (के कारण ही) सभ (सब लोग) मारन (मारने) आहीं (आते हैं), बिनां (और अब बिना) पढ़आं (उस परम नाम को पढ़े यह प्रेम) हुन (अब) छड्डदा (मुझे छोड़ता) नाहीं (नहीं),",
                    "नी (अरी सखी) मैं (मैं) मुड़के (लौटकर अब) कित (किस) वल्ल (ओर) जां (जाऊँ), नी (हे सखी) कुटीचल (कुटीचल) मेरा (मेरा) नां (नाम है) ।"
                ],
                "english_gloss": [
                    "पढ़न सेती सभ मारन आहीं (for reading Alif all rush to beat me), बिनां पढ़आं हुन छड्डदा नाहीं (yet without chanting it Love releases me not),",
                    "नी मैं मुड़के कित वल्ल जां (whither, O sister, can I turn now), नी कुटीचल मेरा नां (O sisters, 'Kutichal' is my name) ।"
                ],
                "poetic_hindi": [
                    "अलिफ़ पढूँ तो सब पीटें मुझको, बिना पढ़े अब चैन न पाए,",
                    "कहाँ जाऊँ मैं लौट के सखियो, मन का संशय कौन मिटाए?",
                    "सखी री, 'कुटीचल' मेरा नाम !"
                ],
                "poetic_english": [
                    "For reading the One they beat me sore; yet unread, Love will not let me go;",
                    "Whither shall I turn my steps, caught in this boundless tide of woe?",
                    "O sisters, 'Kutichal' is my name!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु की लाई मैनूं, मत कुझ लग्गे उह ही तैनूं,  ",
                    "तद करेंगा तूं न्यां, नी कुटीचल मेरा नां ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ले शाह कहते हैं) शहु (मेरे प्रियतम ने) की (कैसी अद्भुत लगन) लाई (लगा दी है) मैनूं (मुझको), मत (संभवतः) कुझ (कुछ वही प्रेम-रोग) लग्गे (लग जाए कभी) उह ही (वही) तैनूं (तुझको भी),",
                    "तद (तभी) करेंगा (कर सकेगा) तूं (तू निष्पक्ष) न्यां (सच्चा न्याय), नी (अरी सखी) कुटीचल (कुटीचल) मेरा (मेरा) नां (नाम है) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा शहु की लाई मैनूं (Bulleh's Lord: what love-passion has He lit in me), मत कुझ लग्गे उह ही तैनूं (may that same holy passion strike thee too),",
                    "तद करेंगा तूं न्यां (then alone wilt thou deliver true justice), नी कुटीचल मेरा नां (O sisters, 'Kutichal' is my name) ।"
                ],
                "poetic_hindi": [
                    "बुल्ला कहे: साहिब ने कैसी लगन लगाई, काश तुम्हें भी यह रोग सताए,",
                    "तभी करोगे सच्चा न्याय, जब यह मीठा दर्द समझ में आए !",
                    "सखी री, 'कुटीचल' मेरा नाम !"
                ],
                "poetic_english": [
                    "Says Bulleh: What passion the Lord has lit! May that same fire ignite thy heart;",
                    "Then alone canst thou judge my soul, when wounded by that holy dart:",
                    "O sisters, 'Kutichal' is my name!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी सूफी जीवन की उस ऐतिहासिक त्रासदी का यथार्थवादी दस्तावेज़ है जहाँ समाज और परिवार साधक को बहिष्कृत कर देते हैं। 'कुटीचल' (निरंतर कुटी/पिटी जाने वाली) शब्द में गहरा दर्द और आत्म-समर्पण दोनों हैं। कबीर की तरह ('कबिरा खड़ा बज़ार में लिए लुकाठी हाथ') बुल्ले शाह भी घर-द्वार, माता-पिता और समाज की रूढ़ियों को त्यागकर खड़े हैं। अंतिम पंक्ति 'तद करेंगा तूं न्यां' एक कालजयी चुनौती है: जब तक किसी ने स्वयं प्रेम की आग में जलने का अनुभव न किया हो, तब तक उसे किसी प्रेमी पर न्याय का फैसला सुनाने का कोई नैतिक अधिकार नहीं है।"
    },
    {
        "id": 112,
        "title": "नी मैं हुन सुण्या इश्क शर्हा की नाता",
        "title_english": "Hear, O Sisters: What Kinship Has Love With Formal Law?",
        "historical_context": "यह 5 बंधों की एक अत्यंत प्रखर, तार्किक और क्रांतिकारी काफी है। इसमें बुल्ले शाह शरिया (रूढ़िवादी धार्मिक विधि-विधान) और हकीकी इश्क (दिव्य प्रेम) के बुनियादी अंतर को स्पष्ट करते हैं। वे कहते हैं कि प्रेम का एक घूँट पीते ही सारे बाह्य विवाद और शास्त्रीय तर्क विस्मृत हो जाते हैं। 'मंतक' (तर्कशास्त्र), 'माअनी' (शब्दार्थ) और 'कन्नज़ व क़ुदूरी' (इस्लामी न्यायशास्त्र की प्रसिद्ध पुस्तकें) केवल बुद्धि का जाल हैं। जब हृदय में सद्गुरु का वास हो जाता है, तो बाह्य कर्मकांड निरर्थक हो जाते हैं।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: नी मैं हुन सुण्या)",
        "raga": "राग काफी / बिलावल",
        "theme": "इश्क और शरिया का द्वंद्व, पोथी-ज्ञान का तिरस्कार, आंतरिक मुर्शिद, मजलिस-ए-इश्क",
        "stanzas": [
            {
                "original": [
                    "नी मैं हुन सुण्या इश्क शर्हा की नाता ।"
                ],
                "hindi_gloss": [
                    "नी (अरी सखी) मैं (मैंने) हुन (अब पूर्णतः) सुण्या (समझ लिया है कि) इश्क (दिव्य प्रेम और) शर्हा (रूढ़िवादी विधान का आपस में) की (क्या कोई) नाता (संबंध हो सकता है भला) ।"
                ],
                "english_gloss": [
                    "नी मैं हुन सुण्या (O sisters, now have I truly realized) इश्क शर्हा की नाता (what kinship can Love have with formal Law) ।"
                ],
                "poetic_hindi": [
                    "अरी सखी, मैंने अब जाना: प्रेम और शरिया का क्या नाता?",
                    "कहाँ रूहानी इश्क का दरिया, कहाँ विधि-विधान का खाता !"
                ],
                "poetic_english": [
                    "Listen, O sisters, now have I understood: what kinship has Love with formal Law?",
                    "Where passion’s boundless ocean rolls, dogmatic rules are empty straw!"
                ]
            },
            {
                "original": [
                    "मुहब्बत दा इक प्याला पी, भुल्ल जावन सभ बातां,  ",
                    "घर घर साईं है उह साईं, हर हर नाल पछाता ।"
                ],
                "hindi_gloss": [
                    "मुहब्बत (इलाही प्रेम) दा (का) इक (एक ही) प्याला (प्याला) पी (पी लेने पर), भुल्ल (विस्मृत हो) जावन (जाती हैं) सभ (संसार की सारी) बातां (बातें और झंझट),",
                    "घर (प्रत्येक घट/) घर (घर में) साईं (वही सच्चा स्वामी) है (विराजमान है) उह (वही) साईं (परमात्मा), हर (प्रत्येक प्राणी के) हर (अंदर) नाल (उसकी पहचान) पछाता (कर ली गई है) ।"
                ],
                "english_gloss": [
                    "मुहब्बत दा इक प्याला पी (drinking a single goblet of divine Love), भुल्ल जावन सभ बातां (all worldly discourses are clean forgotten),",
                    "घर घर साईं है उह साईं (in every home abides that very Sovereign Master), हर हर नाल पछाता (recognized intimately within every form) ।"
                ],
                "poetic_hindi": [
                    "प्रेम का एक ही घूँट जो पी ले, भूल जाए वो दुनिया सारी,",
                    "घट-घट में वो साहिब बैठा, पहचानी उसकी सूरत प्यारी !"
                ],
                "poetic_english": [
                    "Drink but a single cup of Love, and all worldly cares are washed away;",
                    "In every home the Master dwells, recognized in every creature’s ray!"
                ]
            },
            {
                "original": [
                    "अन्दर साडे मुरशद वस्सदा, नेहुं लग्गा तां जाता,  ",
                    "मंतक माअने कन्नज़ कदूरी, पढ़आ इलम गवाता ।"
                ],
                "hindi_gloss": [
                    "अन्दर (हृदय के भीतर) साडे (हमारे साक्षात्) मुरशद (सद्गुरु) वस्सदा (निवास करते हैं), नेहुं (जब सच्चा प्रेम) लग्गा (लगा) तां (तब यह भेद) जाता (जाना गया),",
                    "मंतक (तर्कशास्त्र) माअने (शब्दार्थ/व्याकरण) कन्नज़ (कंज-उद-दकाइल) कदूरी (और मुख़्तसर-उल-कुदूरी जैसे भारी-भरकम ग्रंथ), पढ़आ (इनका पढ़ा हुआ सारा पोथी-) इलम (ज्ञान) गवाता (मिटा दिया प्रेम ने) ।"
                ],
                "english_gloss": [
                    "अन्दर साडे मुरशद वस्सदा (within our soul abides the holy Murshid), नेहुं लग्गा तां जाता (when love was pledged, this truth was known),",
                    "मंतक माअने (logic and semantics) कन्नज़ कदूरी (the dense lawbooks Kanz and Quduri), पढ़आ इलम गवाता (dissolved all scholastic book-learning) ।"
                ],
                "poetic_hindi": [
                    "अंतर में सतगुरु बसते हैं, प्रेम लगा तब जाना भेद,",
                    "मंतक, मानी, कंज, कदूद—भुला दिए सब शास्त्रीय खेद !"
                ],
                "poetic_english": [
                    "Within our heart the Murshid dwells—when Love was struck, this truth shone bright;",
                    "Logic, semantics, heavy law-books were swept away by inner light!"
                ]
            },
            {
                "original": [
                    "नमाज़ रोज़ा ओस की करना, जिस मध पीती मधमाता,  ",
                    "पढ़ पढ़ पंडित मुल्लां हारे, किसे ना भेद पछाता ।"
                ],
                "hindi_gloss": [
                    "नमाज़ (औपचारिक नमाज़) रोज़ा (और रोज़ा) ओस (उस साधक ने) की (क्या) करना (करना है भला), जिस (जिसने इलाही) मध (मदिरा) पीती (पीकर जो सदा) मधमाता (मदमस्त/उन्मत्त हो चुका है),",
                    "पढ़ (शास्त्र पढ़-) पढ़ (पढ़कर) पंडित (पंडित) मुल्लां (और मुल्ला) हारे (थक कर हार गए), किसे (परंतु किसी ने भी इस) ना (नहीं) भेद (रहस्य को) पछाता (पहचाना) ।"
                ],
                "english_gloss": [
                    "नमाज़ रोज़ा ओस की करना (what need of formal prayers and fasts has he), जिस मध पीती मधमाता (who drank the wine of love and is intoxicated),",
                    "पढ़ पढ़ पंडित मुल्लां हारे (pandits and mullahs grew weary reading endlessly), किसे ना भेद पछाता (none of them unraveled the mystery) ।"
                ],
                "poetic_hindi": [
                    "नमाज़ और रोज़े वो क्या जाने, जिसने पी ली प्रेम-शराब,",
                    "पढ़-पढ़ हारे पंडित-मुल्ला, समझ न पाए प्रेम-किताब !"
                ],
                "poetic_english": [
                    "What care has he for fast and prayer who drank the wine of ecstasy?",
                    "Pandits and clerics exhausted their minds, yet failed to grasp the mystery!"
                ]
            },
            {
                "original": [
                    "ज़री बाफ़दी कदर की जाणे, छट्ट ओनां जत काता,  ",
                    "बुल्ल्हा शहु दी मजलस बह के, हो गया गूंगा बाता ।  ",
                    "नी मैं हुन सुण्या इश्क शर्हा की नाता ।"
                ],
                "hindi_gloss": [
                    "ज़री (स्वर्ण-तारों से बुने) बाफ़दी (जरीदार वस्त्र की) कदर (कीमत) की (क्या) जाणे (जानेगा वह जुलाहा जिसने), छट्ट (मोटा) ओनां (ऊन) जत (और बकरी के बाल ही) काता (काते हों सदा),",
                    "बुल्ल्हा (बुल्ले शाह कहते हैं) शहु (परमेश्वर/मुर्शिद) दी (की दिव्य) मजलस (सभा में) बह (बैठ) के (करके), हो (हो) गया (गया है साधक) गूंगा (वाणी से मूक और) बाता (अवाक) ।",
                    "नी (हे सखी) मैं (मैंने) हुन (अब) सुण्या (जान लिया है कि) इश्क (प्रेम और) शर्हा (शरिया का) की (क्या) नाता (नाता है) ।"
                ],
                "english_gloss": [
                    "ज़री बाफ़दी कदर की जाणे (what can a coarse weaver know of golden brocade), छट्ट ओनां जत काता (who spun only rough wool and camel hair),",
                    "बुल्ल्हा शहु दी मजलस बह के (seated in the assembly of Bulleh's Sovereign King), हो गया गूंगा बाता (became mute and struck dumb with wonder) ।",
                    "नी मैं हुन सुण्या इश्क शर्हा की नाता (what kinship has Love with formal Law) ।"
                ],
                "poetic_hindi": [
                    "जरीदार रेशम की कद्र क्या जाने, जिसने काता मोटा ऊन,",
                    "साहिब की मजलिस में बैठ के, गूंगा हुआ मन का कानून !",
                    "अरी सखी, मैंने अब जाना: प्रेम और शरिया का क्या नाता?"
                ],
                "poetic_english": [
                    "How can a coarse spinner value gold cloth, who spun but goat-hair all his days?",
                    "Seated in Bulleh’s Sovereign court, the soul falls mute in awe and praise!",
                    "What kinship can Love ever have with formal Law?"
                ]
            }
        ],
        "sufi_commentary": "यह काफी ज्ञान मार्ग के थोथेपन और प्रेम मार्ग की दिव्यता का विश्लेषण करती है। 'कंज' (कंज-उद-दकाइल) और 'कदूद' (मुख़्तसर-उल-कुदूरी) हनफ़ी न्यायशास्त्र की वे प्रमाणिक पोथियां हैं जिन्हें मदरसों में रटाया जाता था। बुल्ले शाह कहते हैं कि जब तक हृदय में साक्षात परमात्मा का प्रेम न हो, तब तक ये किताबें केवल मानसिक बोझ हैं। 'जरी बाफदी कदर की जाणे' एक उत्कृष्ट रूपक है: रूढ़िवादी मौलवी उस साधारण बुनकर की तरह हैं जो केवल मोटे ऊन को जानता है, वह प्रेम के स्वर्ण-तारों से बुने हुए जरीदार आध्यात्मिक अनुभव का मूल्य कभी नहीं समझ सकता।"
    },
    {
        "id": 113,
        "title": "हाजी लोक मक्के नूं जांदे",
        "title_english": "The Pilgrims Journey to Mecca, But My Mecca is Ranjha Mahi!",
        "historical_context": "यह 6 लघु बंधों की बुल्ले शाह की सर्वाधिक लोकप्रिय, गेय और अनूठी काफ़ियों में से एक है। इसमें बुल्ले शाह बाह्य तीर्थयात्रा (हज) की तुलना आंतरिक आध्यात्मिक काबा (मुर्शिद/रांझा) से करते हैं। हाजी लोग काबा की यात्रा करते हैं, परंतु बुल्ला के लिए उसका प्रियतम ही काबा है। काबा किसी मरुस्थल के पत्थर में नहीं, बल्कि प्रेमी के हृदय में है। 'विचे हाजी विचे गाजी, विचे चोर उचक्का' के द्वारा बुल्ले शाह सर्वेश्वरवाद के उस शिखर को छूते हैं जहाँ पुण्यवान और पापी, दोनों ही उसी एक परमात्मा के विभिन्न रूप दिखाई देते हैं।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: हाजी लोक मक्के नूं जांदे)",
        "raga": "राग काफी / बिलावल / पहाड़ी",
        "theme": "हज का आंतरिक स्वरूप, रांझा ही काबा, सर्वेश्वरवाद (हाजी-चोर में एक ही नूर), तख्त हजारा",
        "stanzas": [
            {
                "original": [
                    "हाजी लोक मक्के नूं जांदे,  ",
                    "मेरा रांझा माही मक्का,  ",
                    "नी मैं कमली हां ।"
                ],
                "hindi_gloss": [
                    "हाजी (हाजी) लोक (लोग) मक्के (मक्का शरीफ) नूं (की ओर) जांदे (जाते हैं),",
                    "मेरा (परंतु मेरा) रांझा (रांझा) माही (माही ही मेरा पावन) मक्का (काबा है),",
                    "नी (हे सखी) मैं (मैं तो प्रेम में) कमली (दीवानी/बावली) हां (हूँ) ।"
                ],
                "english_gloss": [
                    "हाजी लोक मक्के नूं जांदे (the pilgrim folk journey unto Mecca),",
                    "मेरा रांझा माही मक्का (my Beloved Ranjha is my holy Mecca),",
                    "नी मैं कमली हां (O sisters, I am crazed in love) ।"
                ],
                "poetic_hindi": [
                    "हाजी लोग मक्का को जाते, मेरा रांझा माही काबा,",
                    "अरी सखी री, मैं तो प्रेम-दीवानी हुई !"
                ],
                "poetic_english": [
                    "The pilgrims journey towards holy Mecca afar;",
                    "My Ranjha Mahi is my Kaaba and star—",
                    "O sisters, crazed in Love am I!"
                ]
            },
            {
                "original": [
                    "मैं ते मंग रांझे दी होईआं,  ",
                    "मेरा बाबल करदा धक्का,  ",
                    "नी मैं कमली हां ।"
                ],
                "hindi_gloss": [
                    "मैं (मैं) ते (तो सदा से) मंग (वाग्दत्ता/मंगनी) रांझे (रांझा) दी (की) होईआं (हो चुकी हूँ),",
                    "मेरा (मेरा) बाबल (पिता चूचक संसार के दबाव में) करदा (कर रहा है जबरन) धक्का (अन्याय/धक्का),",
                    "नी (अरी सखी) मैं (मैं) कमली (दीवानी) हां (हूँ) ।"
                ],
                "english_gloss": [
                    "मैं ते मंग रांझे दी होईआं (I am betrothed forever unto Ranjha),",
                    "मेरा बाबल करदा धक्का (my father enforces worldly coercion),",
                    "नी मैं कमली हां (O sisters, I am crazed in love) ।"
                ],
                "poetic_hindi": [
                    "मैं तो रांझा की वाग्दत्ता, बाबुल ज़बरन विवाह रचाए,",
                    "अरी सखी री, मैं तो प्रेम-दीवानी हुई !"
                ],
                "poetic_english": [
                    "Pledged unto Ranjha is my spirit and plight,",
                    "Yet father forces customs in spite—",
                    "O sisters, crazed in Love am I!"
                ]
            },
            {
                "original": [
                    "हाजी लोक मक्के वल्ल जांदे,  ",
                    "मेरे घर विच नौशोह मक्का,  ",
                    "नी मैं कमली हां ।"
                ],
                "hindi_gloss": [
                    "हाजी (हाजी) लोक (लोग) मक्के (मक्का की) वल्ल (ओर) जांदे (जाते हैं),",
                    "मेरे (मेरे अपने ही) घर (हृदय-गृह) विच (में साक्षात् नवल वर परमात्मा) नौशोह (परमेश्वर ही) मक्का (काबा बनकर विराजा है),",
                    "नी (अरी) मैं (मैं) कमली (दीवानी) हां (हूँ) ।"
                ],
                "english_gloss": [
                    "हाजी लोक मक्के वल्ल जांदे (the pilgrims travel towards Mecca),",
                    "मेरे घर विच नौशोह मक्का (within my own home abides the Bridegroom Mecca),",
                    "नी मैं कमली हां (O sisters, I am crazed in love) ।"
                ],
                "poetic_hindi": [
                    "हाजी मक्के की ओर सिधारें, मेरे घर में नवल-वर काबा,",
                    "अरी सखी री, मैं तो प्रेम-दीवानी हुई !"
                ],
                "poetic_english": [
                    "To Mecca the pious pilgrims wander and roam;",
                    "My heavenly Bridegroom is Mecca at home—",
                    "O sisters, crazed in Love am I!"
                ]
            },
            {
                "original": [
                    "विचे हाजी विचे गाजी,  ",
                    "विचे चोर उचक्का,  ",
                    "नी मैं कमली हां ।"
                ],
                "hindi_gloss": [
                    "विचे (उसी परमात्मा के भीतर साक्षात्) हाजी (हाजी भी है) विचे (और उसी के भीतर धर्म-योद्धा) गाजी (गाज़ी भी),",
                    "विचे (उसी में समाया हुआ) चोर (चोर है और विचे ही) उचक्का (जेबकतरा/पापी भी),",
                    "नी (हे सखी) मैं (मैं) कमली (दीवानी) हां (हूँ) ।"
                ],
                "english_gloss": [
                    "विचे हाजी (within Him is the pilgrim) विचे गाजी (within Him is the holy warrior),",
                    "विचे चोर (within Him is the thief) उचक्का (and the pickpocket too),",
                    "नी मैं कमली हां (O sisters, I am crazed in love) ।"
                ],
                "poetic_hindi": [
                    "उसी में हाजी, उसी में गाज़ी, उसी में चोर-उचक्का बोले,",
                    "अरी सखी री, मैं तो प्रेम-दीवानी हुई !"
                ],
                "poetic_english": [
                    "In Him is the pilgrim, in Him the brave knight,",
                    "In Him moves the thief in the shadows of night—",
                    "O sisters, crazed in Love am I!"
                ]
            },
            {
                "original": [
                    "हाजी लोक मक्के वल्ल जांदे,  ",
                    "असां जाना तख़त हज़ारे,  ",
                    "नी मैं कमली हां ।"
                ],
                "hindi_gloss": [
                    "हाजी (हाजी) लोक (लोग) मक्के (मक्का की) वल्ल (ओर) जांदे (जाते हैं),",
                    "असां (परंतु हमको तो अपने प्रियतम के पावन धाम) जाना (जाना है) तख़त (तख्त) हज़ारे (हजारे की ओर),",
                    "नी (अरी) मैं (मैं) कमली (दीवानी) हां (हूँ) ।"
                ],
                "english_gloss": [
                    "हाजी लोक मक्के वल्ल जांदे (pilgrims journey towards Mecca),",
                    "असां जाना तख़त हज़ारे (we must journey to Takht Hazara),",
                    "नी मैं कमली हां (O sisters, I am crazed in love) ।"
                ],
                "poetic_hindi": [
                    "हाजी मक्के की ओर प्रयाण करें, हमको तो जाना तख्त हजारे,",
                    "अरी सखी री, मैं तो प्रेम-दीवानी हुई !"
                ],
                "poetic_english": [
                    "Let pilgrims seek Mecca across the burning plain;",
                    "Unto Takht Hazara my soul turns again—",
                    "O sisters, crazed in Love am I!"
                ]
            },
            {
                "original": [
                    "जित वल्ल यार उते वल्ल कअबा,  ",
                    "भावें फोल किताबां चारे,  ",
                    "नी मैं कमली हां ।"
                ],
                "hindi_gloss": [
                    "जित (जिस) वल्ल (दिशा में मेरा प्यारा) यार (प्रियतम विराजमान है) उते (उसी) वल्ल (दिशा में साक्षात् पवित्र) कअबा (काबा है),",
                    "भावें (चाहे तुम) फोल (खंगाल कर देख लो) किताबां (आसमानी पवित्र धर्मग्रंथ) चारे (चारों—तौरेत, ज़बूर, इंजील और कुरान),",
                    "नी (अरी सखी) मैं (मैं तो) कमली (दीवानी) हां (हूँ) ।"
                ],
                "english_gloss": [
                    "जित वल्ल यार (whichever way the Beloved turns) उते वल्ल कअबा (that very way is the Kaaba),",
                    "भावें फोल किताबां चारे (search through all the four scriptures if you will),",
                    "नी मैं कमली हां (O sisters, I am crazed in love) ।"
                ],
                "poetic_hindi": [
                    "जिस ओर यार, उसी ओर काबा, चारों वेद-किताबें खंगालो,",
                    "अरी सखी री, मैं तो प्रेम-दीवानी हुई !"
                ],
                "poetic_english": [
                    "Whichever way the Beloved turns, there is the Kaaba bright;",
                    "Search all four scriptures for this heavenly sight—",
                    "O sisters, crazed in Love am I!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी सूफी रहस्यवाद का एक अत्यंत प्रसिद्ध सूत्र प्रस्तुत करती है: 'काबा पत्थरों की इमारत नहीं, बल्कि प्रेम का केंद्र है'। बुल्ले शाह कहते हैं कि परमात्मा किसी भौगोलिक स्थान (मक्का) में सीमित नहीं है। 'जित वल्ल यार उते वल्ल कअबा' कुरान की आयत 'फ-ऐनमा तुवल्लू फ-थम्मा वज्हुल्लाह' (तुम जिधर भी मुँह फेरोगे, उधर ही अल्लाह का मुख है) का काव्यात्मक अनुवाद है। 'विचे हाजी विचे गाजी, विचे चोर उचक्का' इब्न अरबी के 'वहदत-उल-वुजूद' का सर्वोच्च निरूपण है, जहाँ सारी सृष्टि को एक ही परम चेतना की विभिन्न अभिव्यक्तियों के रूप में देखा गया है।"
    },
    {
        "id": 114,
        "title": "नी मैनूं लग्गड़ा इश्क अवल्ल दा",
        "title_english": "O Sisters, the Love of the Primordial Day Has Struck Me!",
        "historical_context": "यह 5 बंधों की एक अत्यंत गंभीर, भावपूर्ण और तीव्र विरह-काफी है। बुल्ले शाह कहते हैं कि उनका प्रेम कोई कल या आज का नहीं है, यह तो 'रोज़-ए-अज़ल' (सृष्टि के आदि दिवस, अहद-ए-अलस्त) का अनादि संबंध है। यह प्रेम साधक को कड़ाही में बार-बार तलता है, और पहले से मरे हुए को भी बार-बार मारता है। यह प्रेम-तीर जिगर के भीतर ऐसा गहरा लगा है कि हिलाए भी नहीं हिलता।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: नी मैनूं लग्गड़ा इश्क अवल्ल दा)",
        "raga": "राग काफी / आसावरी",
        "theme": "अनादि प्रेम (रोज़-ए-अज़ल), विरह की कड़ाही में तलना, जिगर का तीर, अनन्य निष्ठा",
        "stanzas": [
            {
                "original": [
                    "नी मैनूं लग्गड़ा इश्क अवल्ल दा ।  ",
                    "अवल्ल दा रोज़ अज़ल्ल दा ।"
                ],
                "hindi_gloss": [
                    "नी (हे सखी) मैनूं (मुझको) लग्गड़ा (लग चुका है) इश्क (दिव्य प्रेम) अवल्ल (सृष्टि के प्रथम दिन) दा (का) ।",
                    "अवल्ल (प्रथम दिवस) दा (का,) रोज़ (उस अनादि दिन) अज़ल्ल (रोज़-ए-अज़ल) दा (का) ।"
                ],
                "english_gloss": [
                    "नी मैनूं लग्गड़ा (O sisters, there has struck me) इश्क अवल्ल दा (the Love of the Primordial Day) ।",
                    "अवल्ल दा (of the First Dawn) रोज़ अज़ल्ल दा (of the Day of Pre-Eternity/Azal) ।"
                ],
                "poetic_hindi": [
                    "सखी री, मुझको लगा है प्रेम आदि-काल का,",
                    "सृष्टि के प्रथम दिवस, अनादि रोज़-ए-अज़ल का !"
                ],
                "poetic_english": [
                    "O sisters, the Love of the First Dawn has struck my soul complete;",
                    "The Love of the Primordial Day, when time and eternity meet!"
                ]
            },
            {
                "original": [
                    "विच कड़ाही तल तल जावे, तल्यां नूं चा तलदा,  ",
                    "नी मैनूं लग्गड़ा इश्क अवल्ल दा ।"
                ],
                "hindi_gloss": [
                    "विच (विरह की) कड़ाही (कड़ाही में यह प्रेम मुझे) तल (तल-) तल (तलकर भस्म करता) जावे (जाता है), तल्यां (जो पहले से ही जले-भुने हैं) नूं (उनको) चा (पुनः उठा-उठा कर) तलदा (तलता रहता है) ।",
                    "नी (अरी सखी) मैनूं (मुझको) लग्गड़ा (लगा है) इश्क (प्रेम) अवल्ल (अनादि काल) दा (का) ।"
                ],
                "english_gloss": [
                    "विच कड़ाही तल तल जावे (in the cauldron of separation it fries again and again), तल्यां नूं चा तलदा (it fries over and over those already fried) ।",
                    "नी मैनूं लग्गड़ा इश्क अवल्ल दा (the Love of the Primordial Day has struck me) ।"
                ],
                "poetic_hindi": [
                    "विरह-कड़ाही में तल-तल खाए, जले हुए को फिर-फिर तलता,",
                    "सखी री, मुझको लगा है प्रेम आदि-काल का !"
                ],
                "poetic_english": [
                    "In separation’s cauldron fried, it fries again the already fried;",
                    "The Love of the Primordial Day has claimed me for its bride!"
                ]
            },
            {
                "original": [
                    "मोयां नूं इह वल वल मारे, वल्यां नूं चा वलदा,  ",
                    "नी मैनूं लग्गड़ा इश्क अवल्ल दा ।"
                ],
                "hindi_gloss": [
                    "मोयां (जो अहंकार से पहले ही मर चुके हैं) नूं (उनको) इह (यह इश्क) वल (बार-) वल (बार) मारे (मारता है), वल्यां (जो पहले ही इसके चक्करों में उलझे हैं) नूं (उनको) चा (उठाकर पुनः) वलदा (अपने फंदों में लपेटता है) ।",
                    "नी (हे सखी) मैनूं (मुझको) लग्गड़ा (लगा है) इश्क (प्रेम) अवल्ल दा (अनादि काल का) ।"
                ],
                "english_gloss": [
                    "मोयां नूं इह वल वल मारे (it slays repeatedly those already dead to self), वल्यां नूं चा वलदा (it winds into snares those already entangled) ।",
                    "नी मैनूं लग्गड़ा इश्क अवल्ल दा (the Love of the Primordial Day has struck me) ।"
                ],
                "poetic_hindi": [
                    "मरे हुए को बार-बार मारे, उलझे हुए को और उलझाए,",
                    "सखी री, मुझको लगा है प्रेम आदि-काल का !"
                ],
                "poetic_english": [
                    "It slays anew the already dead, and binds again the captured heart;",
                    "The Love of the Primordial Day has pierced me with its dart!"
                ]
            },
            {
                "original": [
                    "क्या जाना कोई चिनग कक्खी ए नित्त सूल कलेजे सल्लदा,  ",
                    "नी मैनूं लग्गड़ा इश्क अवल्ल दा ।"
                ],
                "hindi_gloss": [
                    "क्या (क्या कोई) जाना (जाने कि जैसे) कोई (कोई) चिनग (अग्नि की चिंगारी) कक्खी (घास-फूस में सुलग रही) ए (हो), नित्त (नित्य ही प्रेम का) सूल (शूल/कांटा) कलेजे (हृदय को) सल्लदा (छलनी करता रहता है) ।",
                    "नी (हे सखी) मैनूं (मुझको) लग्गड़ा (लगा है) इश्क (प्रेम) अवल्ल दा (अनादि काल का) ।"
                ],
                "english_gloss": [
                    "क्या जाना कोई चिनग कक्खी ए (who knows, like a hidden spark in dry straw), नित्त सूल कलेजे सल्लदा (daily a sharp thorn pricks the heart) ।",
                    "नी मैनूं लग्गड़ा इश्क अवल्ल दा (the Love of the Primordial Day has struck me) ।"
                ],
                "poetic_hindi": [
                    "घास में जैसे चिंगारी सुलगे, नित्य कलेजे में शूल चुभाए,",
                    "सखी री, मुझको लगा है प्रेम आदि-काल का !"
                ],
                "poetic_english": [
                    "Like a hidden spark in dry straw, it burns in secret deep inside;",
                    "The Love of the Primordial Day has claimed me for its bride!"
                ]
            },
            {
                "original": [
                    "तीर जिगर विच लग्गा इश्कों, नहीं हलाइआ हल्लदा,  ",
                    "नी मैनूं लग्गड़ा इश्क अवल्ल दा ।  ",
                    "बुल्ल्हा शहु दा नेहुं अनोखा, नहीं रलाइआ रलदा,  ",
                    "नी मैनूं लग्गड़ा इश्क अवल्ल दा ।"
                ],
                "hindi_gloss": [
                    "तीर (यह प्रेम-बाण) जिगर (हृदय के) विच (भीतर) लग्गा (लगा है) इश्कों (इश्क का), नहीं (किसी के भी) हलाइआ (हिलाने से यह) हल्लदा (तनिक भी नहीं डिगता),",
                    "बुल्ल्हा (बुल्ले शाह कहते हैं) शहु (परम प्रियतम) दा (का) नेहुं (प्रेम) अनोखा (अत्यंत अनूठा है), नहीं (यह किसी अन्य में) रलाइआ (मिलाने से भी) रलदा (मिश्रित नहीं होता) ।",
                    "नी (हे सखी) मैनूं (मुझको) लग्गड़ा (लगा है) इश्क (प्रेम) अवल्ल (आदि दिवस) दा (का), अवल्ल दा (प्रथम दिन का,) रोज़ अज़ल्ल दा (रोज़-ए-अज़ल का) ।"
                ],
                "english_gloss": [
                    "तीर जिगर विच लग्गा इश्कों (the arrow of Love struck deep into the liver), नहीं हलाइआ हल्लदा (cannot be moved by any shaking),",
                    "बुल्ल्हा शहु दा नेहुं अनोखा (Bulleh's love for the Sovereign is wondrous), नहीं रलाइआ रलदा (cannot be diluted or mixed with any other) ।",
                    "नी मैनूं लग्गड़ा इश्क अवल्ल दा (the Love of the Primordial Day has struck me) ।"
                ],
                "poetic_hindi": [
                    "जिगर में तीर लगा इश्क का, हिलाए भी न हिले ये बाण,",
                    "बुल्ले शाह का नेह अनोखा, जो न्योछावर कर दे जान !",
                    "सखी री, मुझको लगा है प्रेम आदि-काल का !"
                ],
                "poetic_english": [
                    "Love’s arrow struck deep in my breast, unyielding to the world’s command;",
                    "Bulleh’s devotion is unique, the purest treasure of the land:",
                    "The Love of the Primordial Day has claimed me for its bride!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी सूफी रहस्यवाद में 'अलस्त-अल-रब्बिकुम' (क्या मैं तुम्हारा रब नहीं हूँ?) के उस अहद (वचन) को समर्पित है जो सृष्टि रचना से पूर्व ईश्वर और आत्माओं के बीच हुआ था। बुल्ले शाह कहते हैं कि उनका प्रेम लौकिक या अस्थायी नहीं है, यह 'रोज़-ए-अज़ल' (अनादि काल) का संबंध है। 'तल्यां नूं चा तलदा' फना-दर-फना (अहंकार के विनाश पर और अधिक आत्म-शून्यता) की सूफी अवस्था का सुंदर चित्रण है। जब साधक एक बार संसार की दृष्टि से मर जाता है, तो प्रेम उसे और अधिक परिष्कृत करने के लिए पुनः विरह की आंच में तपाता है।"
    },
    {
        "id": 115,
        "title": "नी सईयो मैं गई गवाची",
        "title_english": "O Sister Friends, I Am Lost to Myself!",
        "historical_context": "यह 2 बंधों की एक अत्यंत गहन, फना और बका की पराकाष्ठा को दर्शाने वाली काफी है। इसमें विरहिणी आत्मा अपने अहं ('मैं') को पूर्णतः खोकर परमात्मा के साथ एकाकार हो जाती है और लोक-लाज का घूंघट खोलकर नृत्य करती है। इसमें कुरान की आयत 'फ-ऐनमा तुवल्लू फ-थम्मा वज्हुल्लाह' (जिधर भी तुम देखोगे, उधर ही अल्लाह का मुखड़ा है) का सीधा उल्लेख 'फैहूना माअकुम' के रूप में हुआ है। जब कब्र में आत्मा का हिसाब होता है, तो केवल यही सत्य जीवित बचता है कि परमात्मा के अतिरिक्त किसी वस्तु का अस्तित्व नहीं है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: नी सईयो मैं गई गवाची)",
        "raga": "राग काफी / तिलक कामोद",
        "theme": "फना (अहंकार का लोप), घूंघट खोलकर नृत्य, सर्वत्र परमात्मा का दर्शन (वज्हुल्लाह), सत्य का साक्षात्कार",
        "stanzas": [
            {
                "original": [
                    "नी सईयो मैं गई गवाची,  ",
                    "खोल घुंघट मुक्ख नाची ।"
                ],
                "hindi_gloss": [
                    "नी (हे) सईयो (मेरी प्यारी सखियो) मैं (मेरी 'मैं' / अहंकार) गई (पूरी तरह) गवाची (खो गया/विलीन हो गया है),",
                    "खोल (उघाड़ कर) घुंघट (लोक-लाज का घूंघट अपने) मुक्ख (मुख से, मैं प्रेम में) नाची (नृत्य करने लगी हूँ) ।"
                ],
                "english_gloss": [
                    "नी सईयो (O sister friends) मैं गई गवाची (I am lost to myself / my ego has dissolved),",
                    "खोल घुंघट (unveiling the face) मुक्ख नाची (I danced in ecstatic abandon) ।"
                ],
                "poetic_hindi": [
                    "ओ सखियो, मेरी 'मैं' खो गई, खो गई मेरी हस्ती सारी,",
                    "मुख से घूँघट खोल दिया अब, नाची मैं प्रेम-दीवानी !"
                ],
                "poetic_english": [
                    "O sister friends, I am utterly lost to myself, my ego is undone;",
                    "Casting the veil from off my face, I dance before the Sun!"
                ]
            },
            {
                "original": [
                    "जित वल्ल वेखां उत वल्ल ओही, कसम ओसे दी होर ना कोई,  ",
                    "फैहूना माअकुम फिर गई ध्रोही, जब गोर तेरी बाची ।  ",
                    "नी सईयो मैं गई गवाची ।"
                ],
                "hindi_gloss": [
                    "जित (जिस) वल्ल (ओर) वेखां (मैं देखती हूँ) उत (उसी) वल्ल (ओर केवल) ओही (वही परमात्मा है), कसम (सौगंध है) ओसे (उसी परमेश्वर) दी (की कि उसके सिवाय) होर (और दूसरा) ना (नहीं है) कोई (कोई भी),",
                    "फैहूना माअकुम ('वह तुम्हारे साथ है जहाँ भी तुम हो'—कुरान की यह आयत) फिर (फिर सिद्ध हो) गई (गई और मिट गया सारा) ध्रोही (कपट और द्वैत), जब (जब अंततः तेरी) गोर (कब्र में वास्तविकता) बाची (बांची/पहचानी गई) ।",
                    "नी (हे) सईयो (सखियो) मैं (मेरी 'मैं') गई (खो) गवाची (गई है) ।"
                ],
                "english_gloss": [
                    "जित वल्ल वेखां (whichever way I look) उत वल्ल ओही (there He alone abides), कसम ओसे दी (by His own holy oath) होर ना कोई (none other exists),",
                    "फैहूना माअकुम ('And He is with you wherever ye be') फिर गई ध्रोही (all deceit and duality dissolved), जब गोर तेरी बाची (when the secret of thy grave was read) ।",
                    "नी सईयो मैं गई गवाची (O sister friends, I am lost to myself) ।"
                ],
                "poetic_hindi": [
                    "जिधर भी देखूँ, उधर वही है, कसम खुदा की दूजा न कोई,",
                    "कब्र का जब हिसाब खुला तो द्वैत की सारी कालिमा धोई !",
                    "ओ सखियो, मेरी 'मैं' खो गई !"
                ],
                "poetic_english": [
                    "Whichever way I turn my eyes, there He alone appears;",
                    "By His holy oath, no second lives across the cosmic spheres!",
                    "'He is with you wherever you are'—all falsehood fades away:",
                    "O sister friends, I am utterly lost to myself this day!"
                ]
            },
            {
                "original": [
                    "नाम निशान ना मेरा सईयो, जो आखां तुसीं चुप्प कर रहीओ,  ",
                    "इह गल्ल मूल किसे ना कहीयो, बुल्ल्हा ख़ूब हकीकत जाची ।  ",
                    "नी सईयो मैं गई गवाची, खोल घुंघट मुक्ख नाची ।"
                ],
                "hindi_gloss": [
                    "नाम (न कोई नाम) निशान (न कोई पहचान) ना (नहीं रही) मेरा (मेरी अब) सईयो (हे सखियो), जो (जो कुछ भी) आखां (मैं कहूँ) तुसीं (तुम सुनकर) चुप्प (मौन धारण) कर (करके) रहीओ (रहो),",
                    "इह (यह रहस्यमयी) गल्ल (बात) मूल (कदापि) किसे (किसी नासमझ से) ना (मत) कहीयो (कहना), बुल्ल्हा (बुल्ले शाह ने) ख़ूब (भली-भांति) हकीकत (परम सत्य को) जाची (परख और जान लिया है) ।",
                    "नी (अरी) सईयो (सखियो) मैं (मेरी 'मैं') गई (खो) गवाची (गई है), खोल (खोलकर) घुंघट (घूंघट) मुक्ख (मुख से) नाची (मैं नाच उठी हूँ) ।"
                ],
                "english_gloss": [
                    "नाम निशान ना मेरा सईयो (no name or trace remains of me, O sisters), जो आखां तुसीं चुप्प कर रहीओ (whatever I utter, keep ye silence),",
                    "इह गल्ल मूल किसे ना कहीयो (speak this secret unto none), बुल्ल्हा ख़ूब हकीकत जाची (Bulleh has thoroughly tested and verified the Truth) ।",
                    "नी सईयो मैं गई गवाची (O sister friends, I am lost to myself), खोल घुंघट मुक्ख नाची (unveiling the face I danced in joy) ।"
                ],
                "poetic_hindi": [
                    "न नाम रहा न निशान मेरा, जो कहूँ तुम सुनकर मौन रहो,",
                    "इस गूढ़ भेद को दुनिया के किसी अज्ञानी से मत कहो !",
                    "बुल्ले शाह ने सत्य को परखा, मिट गई संशय-काली रात,",
                    "ओ सखियो, मेरी 'मैं' खो गई, मुख से घूँघट खोल नाची !"
                ],
                "poetic_english": [
                    "No name or trace remains of me; whatever I speak, keep silent heed;",
                    "Disclose this secret unto none, for blind souls mock the holy seed!",
                    "Bulleh has verified the Truth, the veil of mortal dust is torn:",
                    "O sister friends, I am lost to myself, in ecstatic dancing reborn!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी सूफी फना-फिल-हक (ईश्वर में स्वयं का पूर्ण विलय) का चरम गीत है। जब साधक कहता है 'मैं गई गवाची', तो इसका अर्थ है कि उसकी सीमित व्यक्तिगत पहचान समाप्त हो चुकी है। अब केवल परमात्मा ही शेष है। 'फैहूना माअकुम' कुरान की प्रसिद्ध आयत 'व हुवा मअकुम ऐनमा कुन्तुम' (वह तुम्हारे साथ है तुम जहाँ भी हो—सूरह अल-हदीद 57:4) का प्रत्यक्ष संकेत है। जब साधक को यह बोध हो जाता है, तो वह समाज की लोक-लाज का घूंघट उतार फेंक कर प्रेमानंद में नृत्य करता है।"
    }
]

new_lexicon_terms = {
    "कुटीचल": {"hindi": "मार खाई हुई, प्रताड़ित, निरंतर पीटी जाने वाली", "english": "the bruised and beaten one; severely chastised"},
    "मंतक": {"hindi": "तर्कशास्त्र (लॉजिक), अरबी दर्शन का एक विषय", "english": "mantiq, logic/formal syllogism"},
    "माअनी": {"hindi": "शब्दार्थ विज्ञान, अर्थ-मीमांसा, सेमेंटिक्स", "english": "semantics, science of rhetorical meanings"},
    "कन्नज़": {"hindi": "'कंज-उद-दकाइल' (इस्लामी हनफ़ी न्यायशास्त्र की प्रसिद्ध पुस्तक)", "english": "Kanz al-Daqaiq, classic medieval Islamic jurisprudence manual"},
    "कदूरी": {"hindi": "'मुख़्तसर-उल-कुदूरी' (हनफ़ी शरीअती कानून का प्रसिद्ध ग्रंथ)", "english": "Mukhtasar al-Quduri, textbook of Islamic law"},
    "बाफ़दी": {"hindi": "बुनकर, जुलाहा; वस्त्र-निर्माण का कार्य", "english": "weaver, weaver's craft"},
    "मंग": {"hindi": "वाग्दत्ता, जिसकी सगाई हो चुकी हो", "english": "betrothed, pledged bride"},
    "अवल्ल दा": {"hindi": "प्रथम दिन का, सृष्टि के आदि काल का", "english": "of the First Day, of primordial origin"},
    "अज़ल्ल दा": {"hindi": "अनादि काल का (रोज़-ए-अज़ल का)", "english": "of the Day of Pre-Eternity (Azal)"},
    "सल्लदा": {"hindi": "छलनी करता है, चुभता है, बींधता है", "english": "pricks, pierces through, torments"}
}

def main():
    os.makedirs(KAFIAN_DIR, exist_ok=True)
    
    # Save individual JSONs
    for kafi in kafian_data:
        file_path = os.path.join(KAFIAN_DIR, f"kafi_{kafi['id']:03d}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(kafi, f, ensure_ascii=False, indent=2)
        print(f"Saved {file_path}")

    # Update checkpoint
    checkpoint = {
        "completed_count": 115,
        "total": 160,
        "next_kafi_id": 116,
        "last_updated": "2026-10-17T18:50:00+05:30",
        "last_batch": "111-115",
        "status": "in_progress",
        "milestone": "115/160 (71.875%) finished."
    }
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print(f"Checkpoint updated: 115/160 completed. Next ID: 116")

    # Update Lexicon
    if os.path.exists(LEXICON_FILE):
        with open(LEXICON_FILE, "r", encoding="utf-8") as f:
            lexicon = json.load(f)
    else:
        lexicon = {}

    added_count = 0
    for term, trans in new_lexicon_terms.items():
        if term not in lexicon:
            lexicon[term] = trans
            added_count += 1

    with open(LEXICON_FILE, "w", encoding="utf-8") as f:
        json.dump(lexicon, f, ensure_ascii=False, indent=2)
    print(f"Lexicon updated: added {added_count} new entries, total now {len(lexicon)}")

if __name__ == "__main__":
    main()
