# -*- coding: utf-8 -*-
"""
Process Kafian 86 to 90 for Bulleh Shah Trilingual Edition.
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
        "id": 86,
        "title": "मैं पा पढ़िआं तों नस्सना हां",
        "title_english": "I Flee From The Pious Pedants and Bookish Scholars",
        "historical_context": "इस लघु एवं चुटीली काफी में बुल्ले शाह उन पोथी-पंडितों और मुल्लाओं (पा-पढ़े = थोड़ा-बहुत पढ़े-लिखे दंभी विद्वान) से दूर भागने की बात करते हैं जो केवल शब्दों का आडंबर रचते हैं। सांसारिक आलिमों और फाजिलों की इस शुष्क विद्या ने बुद्धि को भ्रमित कर दिया है; जबकि इश्क की एक ही तरंग हृदय को सत्य का साक्षात्कार करा देती है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: मैं पा पढ़िआं तों नस्सना हां)",
        "raga": "राग काफी / बिलावल",
        "theme": "किताबी ज्ञान का तिरस्कार, इश्क की मस्ती, पाखंडी विद्वानों से पलायन",
        "stanzas": [
            {
                "original": [
                    "मैं पा पढ़िआं तों नस्सना हां ।  ",
                    "मैं पा पढ़िआं तों नस्सना हां ।"
                ],
                "hindi_gloss": [
                    "मैं (मैं) पा (अल्पज्ञ/किताबी) पढ़िआं (पढ़े-लिखे दंभियों) तों (से) नस्सना (भागता) हां (हूँ) ।"
                ],
                "english_gloss": [
                    "मैं (I) पा (half-baked/pedantic) पढ़िआं (the lettered scholars) तों (from) नस्सना (flee away) हां (do) ।"
                ],
                "poetic_hindi": [
                    "मैं पोथी-पढ़े पंडितों से भागता हूँ, मैं पाखंडी आलिमों से भागता हूँ !"
                ],
                "poetic_english": [
                    "I flee from pompous pedants of the book, I flee from lettered dogmas cold and dry!"
                ]
            },
            {
                "original": [
                    "कोई मुनसफ्फ हो निरवारे तां मैं दस्सनां हां,  ",
                    "मैं पा पढ़िआं तों नस्सना हां ।"
                ],
                "hindi_gloss": [
                    "कोई (यदि कोई सच्चा) मुनसफ्फ (न्यायप्रिय/निष्पक्ष जन) हो (हो जो सत्य का) निरवारे (निर्णय करे), तां (तो) मैं (मैं उसे अपना कारण) दस्सनां (बताता) हां (हूँ),",
                    "मैं पा पढ़िआं तों नस्सना हां ।"
                ],
                "english_gloss": [
                    "कोई (if some) मुनसफ्फ (just and impartial judge) हो (arises to) निरवारे (settle/discern), तां (then) मैं (I) दस्सनां (will explain) हां (do),",
                    "मैं पा पढ़िआं तों नस्सना हां ।"
                ],
                "poetic_hindi": [
                    "कोई निष्पक्ष न्याय करने वाला हो तो मैं अपना भेद बताऊँ,",
                    "मैं पोथी-पढ़े पंडितों से भागता हूँ !"
                ],
                "poetic_english": [
                    "If an impartial judge should hear the case, my secret truth before him I will show;",
                    "I flee from pompous pedants of the book!"
                ]
            },
            {
                "original": [
                    "आलम-फाज़ल मेरे भाई पा पढ़िआं मेरी अकल गवाई,  ",
                    "दे इश्क दे हुलारे मैं दस्सनां हां,  ",
                    "मैं पा पढ़िआं तों नस्सना हां ।"
                ],
                "hindi_gloss": [
                    "आलम-फाज़ल (बड़े-बड़े आलिम और विद्वान) मेरे (मेरे सगे) भाई (भाई-बंधु थे, किंतु) पा (किताबी) पढ़िआं (पढ़ाई ने) मेरी (मेरी सहज) अकल (बुद्धि) गवाई (भ्रष्ट कर दी),",
                    "दे (उठाकर) इश्क (प्रेम) दे (के) हुलारे (झोंके/तरंगें) मैं (मैं अब) दस्सनां (सच्चाई प्रकट करता) हां (हूँ),",
                    "मैं पा पढ़िआं तों नस्सना हां ।"
                ],
                "english_gloss": [
                    "आलम-फाज़ल (learned scholars and savants) मेरे (were my) भाई (brethren), पा (pedantic) पढ़िआं (reading) मेरी (my) अकल (wits) गवाई (ruined),",
                    "दे (surging with) इश्क (of love) दे (of) हुलारे (ecstatic waves) मैं (I) दस्सनां (proclaim) हां (do),",
                    "मैं पा पढ़िआं तों नस्सना हां ।"
                ],
                "poetic_hindi": [
                    "आलिम-फ़ाज़िल भाई थे मेरे, पोथियों ने मति भ्रष्ट कराई,",
                    "इश्क की मस्ती में झूम-झूम कर, सत्य कथा मैंने समझाई !",
                    "मैं पाखंडी आलिमों से भागता हूँ !"
                ],
                "poetic_english": [
                    "Learned scholars were my kinsmen proud, whose bookish lore destroyed my simple mind;",
                    "Riding on waves of sacred passion now, the living spark of timeless Truth I find:",
                    "I flee from pompous pedants of the book!"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी कबीर के 'पोथी पढ़ि पढ़ि जग मुआ पंडित भया न कोय' की परंपरा में है। धार्मिक ग्रंथों का बाह्य अध्ययन जब अहंकार और वाद-विवाद का कारण बन जाता है, तो वह आत्म-साक्षात्कार में सबसे बड़ा बाधक सिद्ध होता है। सूफी साधक इस शुष्क पांडित्य को त्यागकर प्रेम के 'हुलारे' (अनुभूतिजन्य तरंगों) में लीन होता है।"
    },
    {
        "id": 87,
        "title": "मैं पाइआ ए मैं पाइआ ए",
        "title_english": "I Have Found Him! I Have Found Him!",
        "historical_context": "यह बुल्ले शाह की सबसे अद्भुत, सर्वसमावेशी और सर्वधर्म-समभाव की काफी है। इसमें वे परमात्मा को प्रत्येक भेष और संप्रदाय में साक्षात देखते हैं: कभी वह कुरान पढ़ता है, कभी हिंदू भक्त बनकर जप करता है, कभी गोरखनाथी कान-फटा योगी बनता है; कभी गुरु तेग बहादुर बनकर धर्म की रक्षा में गाज़ी बनता है; कभी मस्जिद में है, कभी ठाकुरद्वारे में है, कभी बैरागी जटाधारी है, तो कभी शेख। अंत में वे कहते हैं कि प्रियतम का यह दर्शन ही उनके लिए 'मेराज' (परम साक्षात्कार) है।",
        "meter": "पंजाबी काफी (चतुष्पदी, अंत्यानुप्रास वटाइआ/लडाइआ/समाइआ/बणाइआ/गाइआ)",
        "raga": "राग काफी / बिलावल / भैरव",
        "theme": "सर्वव्यापकता, सर्वधर्म-समभाव, गुरु तेग बहादुर का उल्लेख, मिअराज का आध्यात्मिक अर्थ",
        "stanzas": [
            {
                "original": [
                    "मैं पाइआ ए मैं पाइआ ए ।  ",
                    "तैं आप सरूप वटाइआ ए ।"
                ],
                "hindi_gloss": [
                    "मैं (मैंने) पाइआ (पा लिया) ए (है) मैं (मैंने अपने प्रभु को) पाइआ (पा लिया) ए (है) ।",
                    "तैं (तूने) आप (स्वयं ही नाना) सरूप (रूप-स्वरूप) वटाइआ (बदल लिए हैं) ए (हैं) ।"
                ],
                "english_gloss": [
                    "मैं (I) पाइआ (have found) ए (have) मैं (I) पाइआ (have found Him) ए (have) ।",
                    "तैं (Thou) आप (Thyself) सरूप (Thy form/guise) वटाइआ (hast transformed) ए (hast) ।"
                ],
                "poetic_hindi": [
                    "मैंने पा लिया है, मैंने पा लिया है ! तूने स्वयं ही रूप बदल लिया है !"
                ],
                "poetic_english": [
                    "I have found Him! I have found Him! Thou Thyself hast donned each changing guise!"
                ]
            },
            {
                "original": [
                    "कहूं तरक किताबां पढ़ते हो, कहूं भगत हिन्दू जप करते हो,  ",
                    "कहूं गोरकंडी विच पड़ते हो, हर घर घर लाड लडाइआ ए ।  ",
                    "तैं आप सरूप वटाइआ ए ।"
                ],
                "hindi_gloss": [
                    "कहूं (कहीं पर) तरक (तुर्क/मुसलमान बनकर) किताबां (कुरान आदि ग्रंथ) पढ़ते (पढ़ते) हो (हो), कहूं (कहीं पर) भगत (भक्त) हिन्दू (हिंदू बनकर) जप (प्रभु-नाम जप) करते (करते) हो (हो),",
                    "कहूं (कहीं पर) गोरकंडी (गोरखपंथी/कानफटे नाथ योगियों) विच (में) पड़ते (प्रविष्ट होते) हो (हो), हर (प्रत्येक) घर (घर-) घर (घर में) लाड (प्रेम-क्रीड़ा) लडाइआ (लड़ाई) ए (है) ।",
                    "तैं आप सरूप वटाइआ ए ।"
                ],
                "english_gloss": [
                    "कहूं (somewhere) तरक (as a Muslim) किताबां (scriptures) पढ़ते (readest) हो (Thou), कहूं (somewhere) भगत (devotee) हिन्दू (Hindu) जप (chanting) करते (makest) हो (Thou),",
                    "कहूं (somewhere) गोरकंडी (among Gorakh’s ear-pierced yogis) विच (in) पड़ते (entourest) हो (Thou), हर (in each) घर (hearth) घर (and home) लाड (loving play) लडाइआ (hast staged) ए (Thou) ।",
                    "तैं आप सरूप वटाइआ ए ।"
                ],
                "poetic_hindi": [
                    "कहीं मुस्लिम बन ग्रंथ पढ़े, कहीं हिंदू भक्त बन जप करता,",
                    "कहीं गोरखपंथी योगी बन, घर-घर में लाड लड़ाता है !"
                ],
                "poetic_english": [
                    "Somewhere as Muslim reading holy text, somewhere as Hindu chanting hymns of grace;",
                    "Somewhere as Gorakh’s yogi in deep caves, in every home Thy loving sports embrace!"
                ]
            },
            {
                "original": [
                    "किते वैरी हो किते बेली हो, किते आप गुरू किते चेली हो,  ",
                    "किते मजनू हो किते लेली हो, हर घट घट बीच समाइआ ए ।  ",
                    "तैं आप सरूप वटाइआ ए ।"
                ],
                "hindi_gloss": [
                    "किते (कहीं पर) वैरी (शत्रु) हो (हो) किते (कहीं पर) बेली (परम मित्र) हो (हो), किते (कहीं पर) आप (स्वयं) गुरू (गुरु हो) किते (कहीं) चेली (शिष्या) हो (हो),",
                    "किते (कहीं) मजनू (दीवाना मजनूं) हो (हो) किते (कहीं रूपवती) लेली (लैला) हो (हो), हर (प्रत्येक) घट (घट-) घट (घट के) बीच (भीतर) समाइआ (समाए हुए) ए (हो) ।",
                    "तैं आप सरूप वटाइआ ए ।"
                ],
                "english_gloss": [
                    "किते (somewhere) वैरी (enemy) हो (art) किते (somewhere) बेली (friend) हो (art), किते (somewhere) आप (Thyself) गुरू (Guru) किते (somewhere) चेली (disciple) हो (art),",
                    "किते (somewhere) मजनू (Majnun) हो (art) किते (somewhere) लेली (Laila) हो (art), हर (every) घट (heart) घट (within each) बीच (in) समाइआ (pervadest) ए (Thou) ।",
                    "तैं आप सरूप वटाइआ ए ।"
                ],
                "poetic_hindi": [
                    "कहीं शत्रु बने, कहीं मित्र बने, कहीं गुरु, कहीं चेली का रूप लिया,",
                    "कहीं मजनूँ, कहीं लैला बनकर, घट-घट में वास अनूप किया !"
                ],
                "poetic_english": [
                    "Somewhere as foe, somewhere as faithful friend, somewhere as Master, somewhere disciple meek;",
                    "Somewhere as lover, somewhere as beloved, in every human vessel Thou dost speak!"
                ]
            },
            {
                "original": [
                    "कहूं गाफ़ल कहूं नमाज़ी हो, कहूं मिम्बर ते बह काज़ी हो,  ",
                    "कहूं तेग़ बहादुर ग़ाज़ी हो, कहूं आपना पंथ बणाइआ ए ।  ",
                    "तैं आप सरूप वटाइआ ए ।"
                ],
                "hindi_gloss": [
                    "कहूं (कहीं पर) गाफ़ल (लापरवाह/अधर्मी) कहूं (कहीं पर) नमाज़ी (सच्चा नमाज़ी) हो (हो), कहूं (कहीं) मिम्बर (मस्जिद के आसन) ते (पर) बह (बैठकर) काज़ी (काज़ी बनते) हो (हो),",
                    "कहूं (कहीं पर गुरु) तेग़ (तेग) बहादुर (बहादुर बनकर धर्म-रक्षक) ग़ाज़ी (योद्धा) हो (हो), कहूं (कहीं पर) आपना (अपना नया) पंथ (पंथ/मार्ग) बणाइआ (बनाया) ए (है) ।",
                    "तैं आप सरूप वटाइआ ए ।"
                ],
                "english_gloss": [
                    "कहूं (somewhere) गाफ़ल (heedless) कहूं (somewhere) नमाज़ी (devout in prayer) हो (art), कहूं (somewhere) मिम्बर (upon the pulpit) ते (upon) बह (seated as) काज़ी (judge) हो (art),",
                    "कहूं (somewhere as Guru) तेग़ (Tegh) बहादुर (Bahadur) ग़ाज़ी (the holy martyr/warrior) हो (art), कहूं (somewhere) आपना (Thine own) पंथ (faith/path) बणाइआ (hast founded) ए (Thou) ।",
                    "तैं आप सरूप वटाइआ ए ।"
                ],
                "poetic_hindi": [
                    "कहीं गाफ़िल, कहीं नमाज़ी तू, कहीं मंच पर काज़ी बन बैठा,",
                    "कहीं तेग बहादुर गाज़ी बन, तूने अपना पंथ रचा डाला !"
                ],
                "poetic_english": [
                    "Somewhere profane, somewhere devout in prayer, somewhere as judge upon the pulpit high;",
                    "Somewhere as brave Tegh Bahadur standing tall, founding a sovereign faith beneath the sky!"
                ]
            },
            {
                "original": [
                    "कहूं मसजद दा वरतारा ए कहूं बण्या ठाकुरदुआरा ए,  ",
                    "कहूं बैरागी जट धारा ए कहूं शैखन बण बण आया ए ।  ",
                    "तैं आप सरूप वटाइआ ए ।"
                ],
                "hindi_gloss": [
                    "कहूं (कहीं पर) मसजद (मस्जिद) दा (का) वरतारा (व्यवहार/विधान) ए (है), कहूं (कहीं पर) बण्या (बन गया है) ठाकुरदुआरा (मंदिर/ठाकुरद्वारा) ए (है),",
                    "कहूं (कहीं) बैरागी (वैरागी साधु बनकर) जट (जटाएं) धारा (धारण की हैं) ए (तूने), कहूं (कहीं) शैखन (शेख/सूफी पीर) बण (बन-) बण (बनकर) आया (आया) ए (है) ।",
                    "तैं आप सरूप वटाइआ ए ।"
                ],
                "english_gloss": [
                    "कहूं (somewhere) मसजद (mosque) दा (of) वरतारा (ordinance) ए (is), कहूं (somewhere) बण्या (fashioned) ठाकुरदुआरा (temple of the Lord) ए (is),",
                    "कहूं (somewhere) बैरागी (as ascetic) जट (matted locks) धारा (holding) ए (art), कहूं (somewhere) शैखन (as a Muslim Sheikh) बण (becoming) आया (hast appeared) ए (Thou) ।",
                    "तैं आप सरूप वटाइआ ए ।"
                ],
                "poetic_hindi": [
                    "कहीं मस्जिद का व्यवहार बना, कहीं ठाकुरद्वारा रूप रचा,",
                    "कहीं जटाधारी बैरागी तू, कहीं शेख बन कर आन सजा !"
                ],
                "poetic_english": [
                    "Somewhere in holy mosques the rites resound, somewhere in temples bells ring sweet and clear;",
                    "Somewhere with matted locks as hermit bound, somewhere as solemn Sheikh Thou dost appear!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु दा मैं मुहताज होया, महाराज मिले मेरा काज होया,  ",
                    "मुझे पिया का दरस मिअराज होया, लग्गा इश्क तां इह गुन गाइआ ए ।  ",
                    "मैं पाइआ ए मैं पाइआ ए ।  ",
                    "तैं आप सरूप वटाइआ ए ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ला) शहु (उस प्रभु-शाह) दा (का) मैं (मैं) मुहताज (सदा का याचक/दास) होया (हो गया), महाराज (वे परम प्रभु महाराज जब) मिले (मिल गए तो) मेरा (मेरा संपूर्ण) काज (जीवन-कार्य) होया (सफल हो गया),",
                    "मुझे (मुझको) पिया (प्रियतम) का (का) दरस (साक्षात्कार ही सच्चा) मिअराज (मेराज/ईश्वरीय मिलन) होया (हो गया), लग्गा (जब हृदय में लगा) इश्क (इश्क) तां (तो) इह (यह) गुन (गुणगान) गाइआ (गाया) ए (है) ।",
                    "मैं पाइआ ए मैं पाइआ ए, तैं आप सरूप वटाइआ ए ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh) शहु (unto the Lord) दा (of) मैं (I) मुहताज (humble supplicant) होया (became), महाराज (the Sovereign King) मिले (met me) मेरा (my) काज (life's purpose) होया (was fulfilled),",
                    "मुझे (unto me) पिया (Beloved’s) का (of) दरस (vision) मिअराज (celestial Ascension) होया (became), लग्गा (ignited) इश्क (when love) तां (then) इह (this) गुन (praise) गाइआ (sang) ए (I) ।",
                    "मैं पाइआ ए मैं पाइआ ए, तैं आप सरूप वटाइआ ए ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा शौह का दास हुआ, महाराज मिले, सब काज हुआ,",
                    "पिया का दीदार ही मेराज हुआ, इश्क लगा तो गुणगान किया !",
                    "मैंने पा लिया है, मैंने पा लिया है ! तूने स्वयं ही रूप बदल लिया है !"
                ],
                "poetic_english": [
                    "Bulleh became a mendicant of the King, the Sovereign came, fulfilling every grace;",
                    "My Lover’s vision was my Ascension high, when Love awoke this song before His face!",
                    "I have found Him! I have found Him! Thou Thyself hast donned each changing guise!"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी सूफी रहस्यवाद और भारतीय अद्वैत वेदांत का अमर समन्वय है। नौवें सिख गुरु, गुरु तेग बहादुर जी ('कहूं तेग बहादुर गाज़ी हो') का सम्मानपूर्वक उल्लेख बुल्ले शाह की असीम सांप्रदायिक उदारता और ऐतिहासिक निष्पक्षता को प्रमाणित करता है। 'मुझे पिया का दरस मिअराज होया'—इस्लाम में पैगंबर के आकाश-गमन (मेराज) को सर्वोच्च ईश्वरीय निकटता माना जाता है; बुल्ले शाह कहते हैं कि प्रियतम का यह प्रत्यक्ष दीदार ही आत्मा का साक्षात मेराज है।"
    },
    {
        "id": 88,
        "title": "मैं पुच्छां शहु दियां वाटां नी",
        "title_english": "I Ask The Pathways Unto The Lord, O Sisters!",
        "historical_context": "इस काफी में विरहिणी जीवात्मा सखियों से प्रभु-मिलन के मार्ग (शहु दियां वाटां) पूछती है। वह चेतावनी देती है कि प्रमाद और विषय-वासनाओं (नफ़्स) की चोट में समय न गँवाओ। प्रेम-नगर की चाल उलटी है—यहाँ सांसारिक प्रतिष्ठा खोकर ही परमात्मा से नाता जुड़ता है। जब साधक 'अहं ब्रह्मास्मि' (बुल्ल्हा रब्ब बण बैठों) का अनुभव करता है, तो सारा संसार उसका शत्रु बन जाता है।",
        "meter": "पंजाबी काफी (चतुष्पदी, अंत्यानुप्रास वाटां/बातां/चाटां/लाटां/घातां/आफातां)",
        "raga": "राग सोरठ / काफी",
        "theme": "ईश्वर की राह की खोज, नफ़्स की वासनाएं, संसार का विरोध, आत्म-साक्षात्कार",
        "stanzas": [
            {
                "original": [
                    "मैं पुच्छां शहु दियां वाटां नी ।  ",
                    "कोई करे असां नाल बातां नी ।"
                ],
                "hindi_gloss": [
                    "मैं (मैं) पुच्छां (पूछती हूँ) शहु (प्रभु-प्रियतम की) दियां (की) वाटां (राहें/मार्ग) नी (हे सखियो) ।",
                    "कोई (कोई तो) करे (करे) असां (हमारे) नाल (साथ ज्ञान की) बातां (बातें) नी (हे सखी) ।"
                ],
                "english_gloss": [
                    "मैं (I) पुच्छां (inquire) शहु (of the Lord) दियां (of) वाटां (pathways) नी (O friends) ।",
                    "कोई (someone) करे (speak) असां (unto us) नाल (with) बातां (words of truth) नी (O maidens) ।"
                ],
                "poetic_hindi": [
                    "मैं पूछूँ साजन की राहें री ! कोई करे हमसे प्रीत की बातें री !"
                ],
                "poetic_english": [
                    "I ask the pathways to my Lord today! Let someone speak of Love along the way!"
                ]
            },
            {
                "original": [
                    "भुल्ले रहे नाम ना जप्या, ग़फलत अन्दर यार है छप्या,  ",
                    "उह सिध पुरखा तेरे अन्दर वस्या, लगियां नफ़स दियां चाटां नी ।  ",
                    "कोई करे असां नाल बातां नी ।"
                ],
                "hindi_gloss": [
                    "भुल्ले (भटके) रहे (रहे और) नाम (प्रभु का नाम) ना (नहीं) जप्या (जपा), ग़फलत (असावधानी/प्रमाद के) अन्दर (भीतर) यार (प्रियतम) है (है) छप्या (छिपा रहा),",
                    "उह (वह) सिध (सिद्ध) पुरखा (पुरुष परमात्मा) तेरे (तेरे) अन्दर (भीतर ही) वस्या (बसता है, किंतु तुझे) लगियां (लग गईं) नफ़स (इंद्रिय-वासनाओं) दियां (की) चाटां (चोटें/लत) नी ।",
                    "कोई करे असां नाल बातां नी ।"
                ],
                "english_gloss": [
                    "भुल्ले (deluded) रहे (remained) नाम (Holy Name) ना (not) जप्या (chanted), ग़फलत (of heedlessness) अन्दर (within) यार (the Friend) है (is) छप्या (hidden),",
                    "उह (that) सिध (Perfect) पुरखा (Divine Being) तेरे (thee) अन्दर (within) वस्या (dwells), लगियां (struck) नफ़स (of sensual ego) दियां (of) चाटां (appetites/wounds) नी ।",
                    "कोई करे असां नाल बातां नी ।"
                ],
                "poetic_hindi": [
                    "भूल में रहकर नाम न जपा, अज्ञान में साजन छिपा रहा,",
                    "सिद्ध-पुरुष अंतर में बसा था, वासनाओं ने मन को ठगा रहा !"
                ],
                "poetic_english": [
                    "Lost in delusions we forgot His name, hidden behind the veil of heedless sleep;",
                    "Within our heart the Perfect Being came, while sensual appetites made spirits weep!"
                ]
            },
            {
                "original": [
                    "जप लै ना हो भोली भाली, मत तूं साएं मुक्ख मुकाली,  ",
                    "उलटी प्रेम नगर दी चाली, भड़कन इश्क दियां लाटां नी ।  ",
                    "कोई करे असां नाल बातां नी ।"
                ],
                "hindi_gloss": [
                    "जप (नाम जप) लै (ले) ना (मत) हो (हो) भोली (भोली-) भाली (भाली/अज्ञानी), मत (कहीं ऐसा न हो कि) तूं (तू) साएं (स्वामी के सम्मुख) मुक्ख (मुख से) मुकाली (कालिमा-युक्त/लज्जित हो),",
                    "उलटी (उल्टी है) प्रेम (प्रेम-) नगर (नगर) दी (की) चाली (रीति), भड़कन (धधकती हैं) इश्क (इश्क) दियां (की) लाटां (प्रचंड ज्वालाएं) नी ।",
                    "कोई करे असां नाल बातां नी ।"
                ],
                "english_gloss": [
                    "जप (chant) लै (take) ना (do not) हो (be) भोली (simple) भाली (naive), मत (lest) तूं (thou) साएं (before the Lord) मुक्ख (with face) मुकाली (blackened with shame),",
                    "उलटी (inverted) प्रेम (of Love’s) नगर (city) दी (of) चाली (custom/gait), भड़कन (blaze) इश्क (of passion) दियां (of) लाटां (flames) नी ।",
                    "कोई करे असां नाल बातां नी ।"
                ],
                "poetic_hindi": [
                    "नाम जप ले, मत बन भोली, कहीं साजन के आगे लज्जित न हो जाए,",
                    "उल्टी है प्रेम-नगर की रीति, जहाँ इश्क की ज्वाला भड़कती जाए !"
                ],
                "poetic_english": [
                    "Chant the Lord’s name, be not naive and blind, lest with a blackened face before Him stand;",
                    "Strange are the customs of the lover's mind, where leaping fires consume the desert sand!"
                ]
            },
            {
                "original": [
                    "भोली ना हो, हो स्याणी, इश्क नूर दा भर लै पाणी,  ",
                    "इस दुनियां दी छोड़ कहाणी, इह यार मिलन दियां घातां नी ।  ",
                    "कोई करे असां नाल बातां नी ।"
                ],
                "hindi_gloss": [
                    "भोली (अबोली) ना (मत) हो (हो), हो (बन जा) स्याणी (चतुर/प्रबुद्ध), इश्क (इश्क के) नूर (दिव्य प्रकाश) दा (का) भर (भर) लै (ले) पाणी (अमृत-जल),",
                    "इस (इस) दुनियां (संसार) दी (की) छोड़ (छोड़ दे) कहाणी (झूठी कहानियां), इह (ये ही) यार (प्रियतम से) मिलन (मिलने) दियां (की) घातां (गुप्त युक्तियां) नी ।",
                    "कोई करे असां नाल बातां नी ।"
                ],
                "english_gloss": [
                    "भोली (simple) ना (not) हो (be), हो (become) स्याणी (wise), इश्क (of love’s) नूर (light) दा (of) भर (draw) लै (take) पाणी (water of life),",
                    "इस (of this) दुनियां (world) दी (of) छोड़ (leave) कहाणी (tales), इह (these) यार (Beloved) मिलन (to meet) दियां (of) घातां (secret arts/ways) नी ।",
                    "कोई करे असां नाल बातां नी ।"
                ],
                "poetic_hindi": [
                    "भोली मत बन, चतुर बन जा तू, प्रेम-नूर का जल भर ले री,",
                    "संसार की व्यर्थ कथाएं तज, साजन से मिलन की युक्ति कर ले री !"
                ],
                "poetic_english": [
                    "Awake to wisdom, childish dreams resign, draw the pure water of celestial Light;",
                    "Abandon worldly tales of false design—these are the paths to reach the Lover’s sight!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा रब्ब बण बैठों आपे, तद दुनियां दे पए स्यापे,  ",
                    "दूती वेहड़ा, दुशमन मापे, सभ कड़क पईआं आफातां नी ।  ",
                    "मैं पुच्छां शहु दियां वाटां नी ।  ",
                    "कोई करे असां नाल बातां नी ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ला जब) रब्ब (परमात्मा में लीन होकर साक्षात रब) बण (बन) बैठों (बैठ गया) आपे (स्वयं), तद (तब) दुनियां (संसार) दे (के) पए (शुरू हो गए) स्यापे (विलाप/कलह),",
                    "दूती (निंदक बन गया सारा) वेहड़ा (मोहल्ला/आंगन), दुशमन (शत्रु बन गए) मापे (माता-पिता), सभ (सारी) कड़क (कड़क) पईआं (पड़ीं मुझ पर) आफातां (विपत्तियां) नी ।",
                    "मैं पुच्छां शहु दियां वाटां नी, कोई करे असां नाल बातां नी ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh) रब्ब (God/One with the Divine) बण (becoming) बैठों (sat) आपे (himself), तद (then) दुनियां (the world’s) दे (of) पए (fell) स्यापे (mournings/clamor),",
                    "दूती (calumniator became) वेहड़ा (the neighborhood), दुशमन (foes became) मापे (parents), सभ (all) कड़क (thunderously) पईआं (descended) आफातां (calamities) नी ।",
                    "मैं पुच्छां शहु दियां वाटां नी, कोई करे असां नाल बातां नी ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा जब खुद रब बन बैठा, तब जग ने विलाप मचाया री,",
                    "पड़ोसी निंदक, मात-पिता वैरी, विपदाओं का कहर छाया री !",
                    "मैं पूछूँ साजन की राहें री ! कोई करे हमसे प्रीत की बातें री !"
                ],
                "poetic_english": [
                    "When Bulleh sat united with the Lord, the world cried out in scandal and in fright;",
                    "Neighbors calumniated, parents drew the sword, and thundering tempests broke upon the night!",
                    "I ask the pathways to my Lord today! Let someone speak of Love along the way!"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी 'अन-अल-हक' के उद्घोष के परिणाम को दर्शाती है। जब सूफी साधक परमात्मा में विलीन होकर 'बुल्ल्हा रब्ब बण बैठों आपे' (अहं ब्रह्मास्मि) की अवस्था में पहुंचता है, तो रूढ़िवादी समाज, संबंधी और माता-पिता सभी उसके विरोधी हो जाते हैं। किंतु यह विरोध ही प्रेम के मार्ग की अनिवार्य कसौटी है।"
    },
    {
        "id": 89,
        "title": "मैनूं छड्ड गए आप लद्द गए मैं विच की तकसीर",
        "title_english": "Leaving Me Behind, He Departed: What Was My Fault?",
        "historical_context": "इस मार्मिक काफी में विरहिणी जीवात्मा प्रियतम के अकस्मात प्रस्थान पर विलाप करती है। वह पूछती है कि हे प्रभु, मुझमें ऐसा क्या दोष (तकसीर) था कि तू मुझे छोड़कर चला गया? तोपों और तलवारों के घाव समय के साथ भर जाते हैं, किंतु इश्क के तीरों का घाव कभी नहीं भरता। केवल शाह इनायत का अनुग्रह ही इस विरह-वेदना को शांत कर सकता है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, तुक: तकसीर / नीर / तीर / बेपीर / पीड़ / तग़ईर)",
        "raga": "राग सारंग / जोगिया",
        "theme": "प्रियतम का अकस्मात विछोह, विरह का असह्य बाण, शाह इनायत की दया",
        "stanzas": [
            {
                "original": [
                    "मैनूं छड्ड गए आप लद्द गए मैं विच की तकसीर ।  ",
                    "रातीं नींद ना दिन सुक्ख सुत्ती अक्खीं पलट्या नीर ।"
                ],
                "hindi_gloss": [
                    "मैनूं (मुझको) छड्ड (छोड़कर) गए (चले गए) आप (स्वयं अपना ऊंट) लद्द (लादकर) गए (चले गए), मैं (मुझ) विच (में) की (क्या) तकसीर (दोष/अपराध था) ।",
                    "रातीं (रातों में) नींद (नींद नहीं) ना (न) दिन (दिन में) सुक्ख (सुख से) सुत्ती (सो सकी), अक्खीं (आँखों से) पलट्या (उलट पड़ा) नीर (आंसुओं का जल) ।"
                ],
                "english_gloss": [
                    "मैनूं (me) छड्ड (leaving) गए (went) आप (himself) लद्द (loading steed) गए (departed), मैं (in me) विच (in) की (what) तकसीर (fault/error) ।",
                    "रातीं (at night) नींद (no sleep) ना (nor) दिन (by day) सुक्ख (in peace) सुत्ती (slept), अक्खीं (from eyes) पलट्या (poured) नीर (streams of tears) ।"
                ],
                "poetic_hindi": [
                    "मुझे छोड़ कर, लाद कर चल दिए, मुझमें क्या अपराध था स्वामी ?",
                    "रातों में नींद न, दिन में चैन, नयनों से जल बहता अविरल !"
                ],
                "poetic_english": [
                    "Leaving me here, He packed and rode away—what was the fault in me, my Sovereign Dear?",
                    "No sleep by night, no peace by weary day, while weeping eyes pour out continuous tear!"
                ]
            },
            {
                "original": [
                    "छवियां (तोपां) ते तलवारां कोलों इश्क दे तिक्खे तीर ।  ",
                    "इश्के जेड ना ज़ालम कोई इह ज़हमत बेपीर ।"
                ],
                "hindi_gloss": [
                    "छवियां (तोपों/बरछियों) ते (तथा) तलवारां (तलवारों) कोलों (से भी अधिक) इश्क (इश्क) दे (के) तिक्खे (तीखे होते हैं) तीर (बाण) ।",
                    "इश्के (इश्क) जेड (के समान) ना (नहीं है) ज़ालम (अत्याचारी) कोई (कोई भी), इह (यह प्रेम-रोग ऐसा) ज़हमत (कष्ट है जो) बेपीर (दया-हीन/अत्यंत निष्ठुर है) ।"
                ],
                "english_gloss": [
                    "छवियां (cannons/spears) ते (and) तलवारां (swords) कोलों (than) इश्क (of love) दे (of) तिक्खे (sharper) तीर (arrows) ।",
                    "इश्के (love) जेड (like) ना (no) ज़ालम (tyrant) कोई (any), इह (this is) ज़हमत (an affliction) बेपीर (ruthless/merciless) ।"
                ],
                "poetic_hindi": [
                    "तोपों और तलवारों से तीखे प्रेम के बाण कलेजे गड़े,",
                    "इश्क सदृश कोई ज़ालिम नहीं, यह रोग बड़ा निष्ठुर आ पड़े !"
                ],
                "poetic_english": [
                    "Sharper than swords or cannons' thunderous blast, the fiery darts of passion strike the soul;",
                    "No tyrant reigns like Love when hope is past, a pitiless affliction takes its toll!"
                ]
            },
            {
                "original": [
                    "इक पल सायत आराम ना आवे बुरी ब्रेहों दी पीड़ ।  ",
                    "बुल्ल्हा शहु जे करे अनायत दुक्ख होवन तग़ईर ।  ",
                    "मैनूं छड्ड गए आप लद्द गए मैं विच की तकसीर ।"
                ],
                "hindi_gloss": [
                    "इक (एक) पल (पल) सायत (एक क्षण भी) आराम (चैन) ना (नहीं) आवे (आता), बुरी (अति दारुण है) ब्रेहों (विरह) दी (की) पीड़ (पीड़ा) ।",
                    "बुल्ल्हा (बुल्ले का) शहु (प्रभु) जे (यदि) करे (करे) अनायत (इनायत/कृपा), दुक्ख (सारे दुख) होवन (हो जाएं) तग़ईर (दूर/रूपांतरित) ।",
                    "मैनूं छड्ड गए आप लद्द गए मैं विच की तकसीर ।"
                ],
                "english_gloss": [
                    "इक (one) पल (moment) सायत (instant) आराम (relief) ना (not) आवे (comes), बुरी (cruel is) ब्रेहों (of separation) दी (the) पीड़ (pain) ।",
                    "बुल्ल्हा (Bulleh’s) शहु (Lord) जे (if) करे (grant) अनायत (grace/Inayat), दुक्ख (sorrows) होवन (become) तग़ईर (transformed/dispelled) ।",
                    "मैनूं छड्ड गए आप लद्द गए मैं विच की तकसीर ।"
                ],
                "poetic_hindi": [
                    "एक पल, एक क्षण भी आराम न आए, दारुण विरह की पीर सतावे,",
                    "बुल्ल्हा शौह यदि कृपा कर दें, सब दुख मिट कर सुख बन जावे !",
                    "मुझे छोड़ कर, लाद कर चल दिए, मुझमें क्या अपराध था स्वामी ?"
                ],
                "poetic_english": [
                    "Not for one fleeting breath does solace come, cruel the agony of parting's night;",
                    "If Bulleh’s Lord bestow His mercy from on high, all grief transforms to radiant light!",
                    "Leaving me here, He packed and rode away—what was the fault in me, my Sovereign Dear?"
                ]
            }
        ],
        "philosophical_meaning": "सूफी विरह की चरम अभिव्यक्ति है। विरह का बाण किसी भी भौतिक अस्त्र (तलवार या तोप) से अधिक घातक होता है क्योंकि यह शरीर को नहीं बल्कि अंतरात्मा को चीरता है। 'तकसीर' (दोष) की खोज साधक को आत्म-निरीक्षण और पूर्ण दीनता की ओर ले जाती है। अंत में केवल मुर्शिद की 'इनायत' (कृपा) ही इस पीड़ा को दिव्य आनंद (तग़ीर) में बदल सकती है।"
    },
    {
        "id": 90,
        "title": "मैनूं दरद अवल्लड़े दी पीड़",
        "title_english": "I Suffer The Torment of A Strange and Wonder-Filled Malady",
        "historical_context": "यह हीर के स्वर में गाई गई एक अत्यंत आर्त और विह्वल काफी है। वह अपने प्रियतम रांझा को 'हीर निमानी दा पीर' (दीन-हीन हीर का आध्यात्मिक मार्गदर्शक) कहती है और उससे अपने समस्त अपराध क्षमा करके एक झलक (नज़ारा) देने की विनती करती है। संसार के अन्य दूल्हों की तरह उसका प्रियतम आता-जाता क्यों नहीं?",
        "meter": "पंजाबी काफी (मात्रािक छंद, तुक: पीड़ / तकसीर / पीर)",
        "raga": "राग काफी / पिलू",
        "theme": "अनोखा विरह-दर्द, हीर-रांझा रूपक, क्षमा-याचना, प्रियतम के दर्शन की लालसा",
        "stanzas": [
            {
                "original": [
                    "मैनूं दरद अवल्लड़े दी पीड़ ।  ",
                    "मैनूं दरद अवल्लड़े दी पीड़ ।  ",
                    "आ मियां रांझा दे दे नज़ारा मुआफ़ करीं तकसीर ।  ",
                    "मैनूं दरद अवल्लड़े दी पीड़ ।"
                ],
                "hindi_gloss": [
                    "मैनूं (मुझको) दरद (दर्द) अवल्लड़े (विचित्र/अनोखे प्रेम) दी (की) पीड़ (पीड़ा लगी है) ।",
                    "आ (आओ) मियां (हे मियाँ) रांझा (रांझा प्यारे) दे (दे) दे (दीजिए) नज़ारा (अपना साक्षात दर्शन), मुआफ़ (क्षमा) करीं (कर दो मेरी समस्त) तकसीर (भूलें/अपराध) ।",
                    "मैनूं दरद अवल्लड़े दी पीड़ ।"
                ],
                "english_gloss": [
                    "मैनूं (unto me) दरद (the pain) अवल्लड़े (of a wondrous/wondrously strange love) दी (of) पीड़ (anguish) ।",
                    "आ (come) मियां (O noble) रांझा (Ranjha) दे (grant) दे (give) नज़ारा (Thy vision), मुआफ़ (forgive) करीं (make) तकसीर (my transgressions) ।",
                    "मैनूं दरद अवल्लड़े दी पीड़ ।"
                ],
                "poetic_hindi": [
                    "मुझे अनोखे विरह-दर्द की पीर सतावे !",
                    "आ मियाँ रांझा! दरस दिखा दे, सारे दोष भुलावे !",
                    "मुझे अनोखे विरह-दर्द की पीर सतावे !"
                ],
                "poetic_english": [
                    "I suffer the torment of a strange and wondrous pain!",
                    "Come, Ranjha, grant a glimpse of Thy sweet face, forgive my faults again!",
                    "I suffer the torment of a strange and wondrous pain!"
                ]
            },
            {
                "original": [
                    "तख़त हज़ार्युं रांझा टुरिआ हीर निमानी दा पीर ।  ",
                    "मैनूं दरद अवल्लड़े दी पीड़ ।"
                ],
                "hindi_gloss": [
                    "तख़त (तख्त) हज़ार्युं (हज़ारा से) रांझा (रांझा) टुरिआ (चल पड़ा था), हीर (मुझ दीन) निमानी (अभागिनी हीर) दा (का जो) पीर (आध्यात्मिक गुरु व प्रियतम है) ।",
                    "मैनूं दरद अवल्लड़े दी पीड़ ।"
                ],
                "english_gloss": [
                    "तख़त (from Takht) हज़ार्युं (Hazara) रांझा (Ranjha) टुरिआ (set forth), हीर (of Heer) निमानी (the humble) दा (of) पीर (the spiritual guide and lord) ।",
                    "मैनूं दरद अवल्लड़े दी पीड़ ।"
                ],
                "poetic_hindi": [
                    "तख़्त हज़ारे से रांझा चला था, दीन हीर का पीर बना जो !"
                ],
                "poetic_english": [
                    "From Takht Hazara Ranjha set His stride, the holy Master of poor Heer alone!"
                ]
            },
            {
                "original": [
                    "होरनां दे नौशहु आवे जावे की बुल्ल्हे विच तकसीर ।  ",
                    "मैनूं दरद अवल्लड़े दी पीड़ ।"
                ],
                "hindi_gloss": [
                    "होरनां (औरों/अन्य स्त्रियों) दे (के) नौशहु (नव-दूल्हा/पति) आवे (आता है) जावे (और जाता है), की (क्या) बुल्ल्हे (मुझ बुल्ले) विच (के भीतर ऐसी) तकसीर (खामी/दोष है कि तू नहीं आता) ।",
                    "मैनूं दरद अवल्लड़े दी पीड़ ।"
                ],
                "english_gloss": [
                    "होरनां (of others) दे (of) नौशहु (the young bridegroom) आवे (comes) जावे (goes freely), की (what) बुल्ल्हे (in Bulleh) विच (in) तकसीर (defect/fault is there) ।",
                    "मैनूं दरद अवल्लड़े दी पीड़ ।"
                ],
                "poetic_hindi": [
                    "औरों के दूल्हे आते-जाते, क्या बुल्ल्हे में दोष रहा ?",
                    "मुझे अनोखे विरह-दर्द की पीर सतावे !"
                ],
                "poetic_english": [
                    "To other maidens their young bridegrooms turn—what fault in Bulleh keeps Thee far away?",
                    "I suffer the torment of a strange and wondrous pain!"
                ]
            }
        ],
        "philosophical_meaning": "रांझा यहाँ केवल एक सांसारिक प्रेमी नहीं बल्कि 'हीर निमानी दा पीर' (आत्मा का सद्गुरु और परमात्मा) है। विरह का यह दर्द 'अवल्लड़ा' (अनोखा/अलौकिक) है क्योंकि यह संसार की किसी औषधि से ठीक नहीं हो सकता; इसकी एकमात्र औषधि प्रियतम का 'नज़ारा' (दर्शन) है।"
    }
]

new_lexicon_terms = {
    "पा पढ़िआं": {"hindi": "अल्पज्ञ, थोड़ा-बहुत पढ़कर दंभ करने वाले किताबी विद्वान", "english": "half-educated pedants, shallow bookish scholars"},
    "हुलारे": {"hindi": "झोंके, मस्ती की तरंगें, उफान", "english": "swings, ecstatic surges, waves of passion"},
    "गोरकंडी": {"hindi": "गोरखनाथ के अनुयायी, कानफटे नाथ योगी", "english": "Gorakhnath's order of ear-pierced ascetics"},
    "वरतारा": {"hindi": "व्यवहार, रीति-नीति, विधान", "english": "custom, practice, ritual ordinance"},
    "मिअराज": {"hindi": "मेराज, पैगंबर का ईश्वरीय साक्षात्कार हेतु आकाश-गमन; रूपक में: आत्म-साक्षात्कार", "english": "Miraj, heavenly ascension and direct vision of God"},
    "सिध पुरखा": {"hindi": "सिद्ध पुरुष, परिपूर्ण परमात्मा", "english": "the Perfect Being, Supreme Divine Purusha"},
    "मुकाली": {"hindi": "मुंह काला होना, लज्जित होना", "english": "blackened face, shame, disgrace"},
    "तकसीर": {"hindi": "दोष, अपराध, त्रुटि", "english": "fault, transgression, shortcoming"},
    "तग़ईर": {"hindi": "रूपांतरित, परिवर्तित, दूर", "english": "transformed, changed, dispelled"},
    "नौशहु": {"hindi": "नया दूल्हा, प्रियतम", "english": "young bridegroom, newly-wed lover"}
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
        "completed_count": 90,
        "total": 160,
        "next_kafi_id": 91,
        "last_updated": "2026-10-17T17:45:00+05:30",
        "last_batch": "86-90",
        "status": "in_progress"
    }
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print(f"Checkpoint updated: 90/160 completed. Next ID: 91")

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
