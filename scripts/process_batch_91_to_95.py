# -*- coding: utf-8 -*-
"""
Process Kafian 91 to 95 for Bulleh Shah Trilingual Edition.
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
        "id": 91,
        "title": "मैं उडीकां कर रही कदी आ कर फेरा",
        "title_english": "I Stand Waiting in Yearning: Come Sometime and Grace My Hearth!",
        "historical_context": "यह 11 बंधों की एक अत्यंत मार्मिक और महाकाव्यात्मक विरह-काफी है। विरहिणी आत्मा अपने मुर्शिद हज़रत शाह इनायत कादरी और परमेश्वर के आगमन की प्रतीक्षा कर रही है। इसमें लोक-संस्कृति के शृंगार (सिंदूर, रत्तड़ा चोला, कंगन) से लेकर मृत्यु, कब्र (गोर), पुल-सिरात और प्रलय-वेला तक के दृश्य चित्रित हैं। साधक हाजियों की तरह मक्का जाने के स्थान पर अपने प्रियतम के मुखड़े को ही अपना काबा मानता है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: मैं उडीकां कर रही)",
        "raga": "राग काफी / जोगिया",
        "theme": "प्रतीक्षा, विरह की तड़प, मृत्यु और परलोक (पुल-सिरात), शाह इनायत का दीदार",
        "stanzas": [
            {
                "original": [
                    "मैं जो तैनूं आख्या कोई घल्ल सुनेहड़ा ।  ",
                    "चशमां सेज विछाईआं दिल कीता डेरा ।  ",
                    "लटक चलेंदा आंवदा शाह इनायत मेरा ।  ",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "hindi_gloss": [
                    "मैं (मैंने) जो (जो) तैनूं (तुझसे) आख्या (कहा था कि) कोई (कोई तो) घल्ल (भेज) सुनेहड़ा (संदेश),",
                    "चशमां (नेत्रों में) सेज (प्रेम-शय्या) विछाईआं (बिछा रखी है) दिल (और हृदय में) कीता (बनाया है तेरा) डेरा (आवास),",
                    "लटक (मस्तानी चाल से) चलेंदा (चलता हुआ) आंवदा (आ रहा है) शाह (शाह) इनायत (इनायत) मेरा (मेरा प्यारा सद्गुरु),",
                    "मैं (मैं तेरी) उडीकां (प्रतीक्षा/राह देख) कर (कर) रही (रही हूँ) कदी (कभी तो) आ (आकर) कर (कर ले यहाँ अपना) फेरा (आगमन) ।"
                ],
                "english_gloss": [
                    "मैं (I) जो (who) तैनूं (unto Thee) आख्या (besought) कोई (some) घल्ल (send) सुनेहड़ा (message),",
                    "चशमां (in eyes) सेज (bridal couch) विछाईआं (spread) दिल (in heart) कीता (made) डेरा (abode),",
                    "लटक (with graceful swaying step) चलेंदा (walking) आंवदा (comes) शाह (Shah) इनायत (Inayat) मेरा (mine),",
                    "मैं (I) उडीकां (yearning wait) कर (am making) रही (standing) कदी (sometime) आ (come) कर (make) फेरा (a visit) ।"
                ],
                "poetic_hindi": [
                    "मैंने तुझसे कहा था कोई संदेशा भेज प्यारे,",
                    "अंखियों में सेज बिछाई, दिल में तेरा डेरा सँवारे ।",
                    "मस्तानी चाल से आता शाह इनायत मेरा,",
                    "मैं बाट जोह रही, कभी आ कर ले फेरा !"
                ],
                "poetic_english": [
                    "I prayed unto Thee: send a message sweet to heal my sighs;",
                    "My heart Thy dwelling, while the bridal couch is spread in weeping eyes.",
                    "With swaying majesty Shah Inayat strides towards my door:",
                    "I stand waiting in yearning: come sometime and leave me nevermore!"
                ]
            },
            {
                "original": [
                    "उह अजेहा कौन है जा आखे जेहड़ा ।  ",
                    "मैं विच की तकसीर है मैं बरदा तेरा ।  ",
                    "तैं बाझों मेरा कौन है दिल ढा ना मेरा ।  ",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "hindi_gloss": [
                    "उह (वह) अजेहा (ऐसा) कौन (कौन मध्यस्थ) है (है) जा (जाकर) आखे (जो निवेदन करे) जेहड़ा (जो भी समर्थ हो),",
                    "मैं (मुझ) विच (में) की (क्या) तकसीर (त्रुटि/दोष) है (है), मैं (मैं तो) बरदा (सदा का खरीदा हुआ दास) तेरा (तेरा हूँ),",
                    "तैं (तेरे) बाझों (बिना) मेरा (मेरा) कौन (कौन है संसार में) है, दिल (हृदय) ढा (मत तोड़) ना (न) मेरा (मेरा),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "english_gloss": [
                    "उह (that) अजेहा (such) कौन (who) है (is) जा (go) आखे (speak) जेहड़ा (whoever can),",
                    "मैं (in me) विच (in) की (what) तकसीर (fault) है (is), मैं (I am) बरदा (the purchased slave) तेरा (Thine),",
                    "तैं (Thee) बाझों (except) मेरा (mine) कौन (who) है (is), दिल (heart) ढा (crush/break) ना (do not) मेरा (mine),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "poetic_hindi": [
                    "ऐसा कौन दूत है जो जाकर मेरी अरदास सुनाए ?",
                    "मुझमें क्या अपराध है स्वामी, मैं तो दास तेरा कहलाए ।",
                    "तेरे बिना कौन है मेरा, दिल मत तोड़ो मेरा,",
                    "मैं बाट जोह रही, कभी आ कर ले फेरा !"
                ],
                "poetic_english": [
                    "Who is that kindly messenger to bear my trembling plea?",
                    "What is my fault, when I remain a purchased slave to Thee?",
                    "Who else in all the world is mine? Break not this heart of mine:",
                    "I stand waiting in yearning: come sometime with love divine!"
                ]
            },
            {
                "original": [
                    "दसत कंगन बाहीं चूड़ियां गल नौरंग चोला ।  ",
                    "माही मैनूं कर गिआ कोई रावल रौला ।  ",
                    "जल थल आहीं मारदियां दिल पत्थर मेरा ।  ",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "hindi_gloss": [
                    "दसत (हाथों में) कंगन (कंगन) बाहीं (बाँहों में) चूड़ियां (चूड़ियां और) गल (गले में) नौरंग (नवरंगी) चोला (वस्त्र सज रखा है),",
                    "माही (प्रियतम) मैनूं (मुझको) कर (कर) गिआ (गया है) कोई (कोई संन्यासी जैसा) रावल (जोगी/अवधूत का) रौला (भ्रम/आकर्षण),",
                    "जल (जल और) थल (थल सब मेरी विरह की) आहीं (आहों से कांप रहे हैं, किंतु) मारदियां (हाय) दिल (हृदय) पत्थर (कठोर पत्थर बना है) मेरा (उसका),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "english_gloss": [
                    "दसत (on hands) कंगन (bracelets) बाहीं (on arms) चूड़ियां (bangles) गल (on neck) नौरंग (nine-colored) चोला (robe),",
                    "माही (Beloved) मैनूं (me) कर (made) गिआ (went) कोई (some) रावल (wandering yogi's) रौला (spell/madness),",
                    "जल (waters) थल (lands) आहीं (sighs) मारदियां (heaving), दिल (heart) पत्थर (stone) मेरा (mine / His),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "poetic_hindi": [
                    "हाथों में कंगन, बांहों में चूड़ी, गले नवरंगी चोला,",
                    "माही ने जोगी बन कर मन पर मोहिनी-जादू घोला ।",
                    "जल-थल सब विरह से रोते, पाषाण बना दिल उसका,",
                    "मैं बाट जोह रही, कभी आ कर ले फेरा !"
                ],
                "poetic_english": [
                    "Bracelets upon my hands, bright bangles and a nine-hued bridal gown;",
                    "The Beloved like a wandering yogi cast His wild spell through the town.",
                    "Oceans and earth heave heavy sighs, while stone-like seems His heart:",
                    "I stand waiting in yearning: why must we dwell apart?"
                ]
            },
            {
                "original": [
                    "क्या तेरी मांग संधूर भरी सोहे रतड़ा चोला ।  ",
                    "पई वांग समीं मैं कूकदी कर ढोला ढोला ।  ",
                    "अणगिणवें सूलां पा लिआ सूलां दा खेरा ।  ",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "hindi_gloss": [
                    "क्या (कैसी सुंदर) तेरी (तेरी) मांग (मांग) संधूर (सिंदूर से) भरी (भरी है और) सोहे (शोभता है) रतड़ा (रक्त-वर्ण लाल) चोला (चोला),",
                    "पई (पड़कर) वांग (समान) समीं (सम्मी—विरहिणी नायिका के) मैं (मैं) कूकदी (पुकारती फिरती हूँ) कर (कह-कहकर) ढोला (ढोला) ढोला (ढोला),",
                    "अणगिणवें (अनगिनत) सूलां (विरह-शूलों ने) पा (डाल) लिआ (लिया है) सूलां (कांटों) दा (का) खेरा (घेरा चारों ओर),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "english_gloss": [
                    "क्या (how) तेरी (thy) मांग (parting of hair) संधूर (vermilion) भरी (filled) सोहे (shines) रतड़ा (crimson red) चोला (robe),",
                    "पई (like) वांग (as) समीं (Sammi/folk heroine) मैं (I) कूकदी (cry aloud) कर (calling) ढोला (Beloved) ढोला (Beloved),",
                    "अणगिणवें (countless) सूलां (thorns/spikes of grief) पा (cast) लिआ (have) सूलां (of thorns) दा (a) खेरा (circle/siege),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "poetic_hindi": [
                    "मांग सिंदूर भरी है सोहे लाल सुहाग का चोला,",
                    "सम्मी सदृश पुकारूँ वन में: 'ढोला, प्यारे ढोला!'",
                    "अनगिन कांटों ने मुझे घेरा, विरह-शूल का डेरा,",
                    "मैं बाट जोह रही, कभी आ कर ले फेरा !"
                ],
                "poetic_english": [
                    "Vermilion in the parting of my hair, a crimson bridal vest;",
                    "Like folk-maid Sammi crying aloud 'Beloved!' in my chest.",
                    "Countless sharp thorns of separation hedge my soul around:",
                    "I stand waiting in yearning: let Thy sweet step be found!"
                ]
            },
            {
                "original": [
                    "मैं जाता दुक्ख घर आपने दुक्ख पै घर कईआं ।  ",
                    "जेहा सिर सिर भांबड़ भड़क्या सभ टप्पदियां गईआं ।  ",
                    "हुन आण पई सिर आपने सभ चुक्क गिआ झेड़ा ।  ",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "hindi_gloss": [
                    "मैं (मैंने) जाता (समझा था कि) दुक्ख (यह विरह-दुख केवल) घर (घर में) आपने (मेरे ही है, किंतु यह) दुक्ख (दुख तो) पै (पड़ा है) घर (घर-घर में) कईआं (अनेकों के),",
                    "जेहा (जैसा) सिर (सिर पर) सिर (सिर पर) भांबड़ (विरह का शोला) भड़क्या (धधका), सभ (सब सखियां) टप्पदियां (कूद-कूद कर पार) गईआं (हो गईं),",
                    "हुन (अब यह विपत्ति) आण (आकर) पई (पड़ी है) सिर (सिर पर) आपने (मेरे अपने), सभ (समस्त) चुक्क (मिट) गिआ (गया) झेड़ा (संसार का विवाद),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "english_gloss": [
                    "मैं (I) जाता (thought) दुक्ख (grief was) घर (in house) आपने (my own), दुक्ख (yet grief) पै (fell in) घर (houses) कईआं (of many),",
                    "जेहा (as) सिर (upon head) सिर (each head) भांबड़ (blazing flame) भड़क्या (leaped), सभ (all) टप्पदियां (leaping across) गईआं (went),",
                    "हुन (now) आण (coming) पई (fell upon) सिर (head) आपने (my own), सभ (all) चुक्क (ended) गिआ (is) झेड़ा (dispute),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "poetic_hindi": [
                    "समझा था दुख केवल मेरा, दुख तो घर-घर छाया,",
                    "जिस-जिस पर शोला भड़का, कूद-कूद पार सिधाया ।",
                    "अब आ पड़ा सिर पर मेरे, मिट गया सब झगड़ा-झेड़ा,",
                    "मैं बाट जोह रही, कभी आ कर ले फेरा !"
                ],
                "poetic_english": [
                    "I thought this agony was mine alone, but grief invades each floor;",
                    "As leaping flames upon each forehead shone, others leaped to the shore.",
                    "Now falls the trial upon my head, ending each petty plea:",
                    "I stand waiting in yearning: come sometime unto me!"
                ]
            },
            {
                "original": [
                    "जेहड़ियां साहवरे मत्तियां सोई पेके होवन ।  ",
                    "शहु जिन्हां दे कायल ए चढ़ सेजे सोवन ।  ",
                    "जिस घर कौंत ना बोलिआ सोई खाली वेढ़ा ।  ",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "hindi_gloss": [
                    "जेहड़ियां (जो स्त्रियां/आत्माएं) साहवरे (ससुराल में मान पाने वाली) मत्तियां (मदमस्त हैं), सोई (वही) पेके (मायके में भी आदरणीय) होवन (होती हैं),",
                    "शहु (स्वामी-प्रभु) जिन्हां (जिनके प्रेम का) दे (का) कायल (प्रशंसक/वश में) ए (है), चढ़ (चढ़कर) सेजे (प्रेम-शय्या पर) सोवन (आनंद से सोती हैं),",
                    "जिस (जिस) घर (हृदय-घर में) कौंत (कांत/प्रियतम) ना (नहीं) बोलिआ (बोलता), सोई (वही) खाली (सूना/उजाड़) वेढ़ा (आंगन रहता है),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "english_gloss": [
                    "जेहड़ियां (those who) साहवरे (in in-laws' home) मत्तियां (honored/exalted), सोई (they alone) पेके (in father’s home) होवन (are esteemed),",
                    "शहु (Lord) जिन्हां (whose) दे (of) कायल (charmed/won over) ए (is), चढ़ (ascending) सेजे (bridal bed) सोवन (slumber in bliss),",
                    "जिस (in which) घर (hearth) कौंत (Husband/Lord) ना (not) बोलिआ (spoke), सोई (that) खाली (desolate) वेढ़ा (courtyard remains),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "poetic_hindi": [
                    "जो ससुराल में मान पातीं, मायके में वही सोहें,",
                    "जिनके साजन वश में आए, वे सेज सुहाग की मोहें ।",
                    "जिस घर में कांत न बोले, सूना वह आँगन-डेरा,",
                    "मैं बाट जोह रही, कभी आ कर ले फेरा !"
                ],
                "poetic_english": [
                    "Those praised in their Husband's home are blessed in their father's hall;",
                    "Whose beauty has captivated the King, mount the bridal bed at His call.",
                    "The courtyard where the Spouse speaks not is desolate and bare:",
                    "I stand waiting in yearning: come, answer my soul's prayer!"
                ]
            },
            {
                "original": [
                    "मैं ढूंड शहर भालिआ घल्लां कासद केहड़ा ।  ",
                    "हुन चढ़ियां डोली प्रेम दी दिल धड़के मेरा ।  ",
                    "दिलदार मुहंमद आरबी हत्थ पकड़ीं मेरा ।  ",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "hindi_gloss": [
                    "मैं (मैंने) ढूंड (ढूंढकर) शहर (पूरा नगर) भालिआ (छान मारा), घल्लां (भेजूं किस) कासद (संदेशवाहक को) केहड़ा (कौन ऐसा विश्वस्त है),",
                    "हुन (अब तो मैं) चढ़ियां (चढ़ बैठी हूँ) डोली (डोली में) प्रेम (प्रेम की), दिल (और हृदय) धड़के (धड़क रहा है) मेरा (मेरा),",
                    "दिलदार (हे परम प्रेमी) मुहंमद (मुहम्मद) आरबी (अरबी रसूल), हत्थ (हाथ) पकड़ीं (पकड़ लेना) मेरा (मेरा),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "english_gloss": [
                    "मैं (I) ढूंड (searching) शहर (the city) भालिआ (scoured), घल्लां (whom send) कासद (messenger) केहड़ा (which faithful one),",
                    "हुन (now) चढ़ियां (mounted) डोली (the palanquin) प्रेम (of Love) दी (of), दिल (heart) धड़के (flutters) मेरा (mine),",
                    "दिलदार (O Beloved) मुहंमद (Muhammad) आरबी (the Arabian Prophet), हत्थ (hand) पकड़ीं (hold Thou) मेरा (mine),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "poetic_hindi": [
                    "पूरा नगर छान मारा, किस कासिद को भेजूँ प्यारा ?",
                    "प्रेम की डोली चढ़ी हूँ अब, दिल धड़के विह्वल सारा ।",
                    "हे दिलदार मुहम्मद अरबी! पकड़ो हाथ तुम मेरा,",
                    "मैं बाट जोह रही, कभी आ कर ले फेरा !"
                ],
                "poetic_english": [
                    "I searched through all the city streets: what courier can I send?",
                    "Mounting the palanquin of Love, my fluttering heart must bend.",
                    "O Sweet Beloved of Arabia, Muhammad, take my hand:",
                    "I stand waiting in yearning: come lead to the Promise Land!"
                ]
            },
            {
                "original": [
                    "पहली पउड़ी उतरी पुल-सराते डेरा ।  ",
                    "हाजी मक्के जाहुन मैं मुक्ख वेखां तेरा ।  ",
                    "आ इनायत कादरी दिल चाहे मेरा ।  ",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "hindi_gloss": [
                    "पहली (पहली) पउड़ी (सीढ़ी पर जब पैर) उतरी (उतारा, तो) पुल-सराते (पुल-सिरात के मुहाने पर) डेरा (डेरा जम गया),",
                    "हाजी (हाजी लोग भले ही) मक्के (मक्का तीर्थ की ओर) जाहुन (जाएं), मैं (किंतु मैं तो केवल) मुक्ख (मुखड़ा) वेखां (देखना चाहती हूँ) तेरा (तेरा),",
                    "आ (आ जा) इनायत (हे शाह इनायत) कादरी (कादरी पीर), दिल (हृदय) चाहे (चाहता है) मेरा (मेरा तुझे देखना),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "english_gloss": [
                    "पहली (the first) पउड़ी (step) उतरी (descended), पुल-सराते (upon the bridge of Sirat) डेरा (encampment),",
                    "हाजी (pilgrims) मक्के (to Mecca) जाहुन (let go), मैं (I) मुक्ख (face) वेखां (gaze upon) तेरा (Thine),",
                    "आ (come) इनायत (Inayat) कादरी (Qadiri Master), दिल (heart) चाहे (yearns) मेरा (mine),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "poetic_hindi": [
                    "पहली सीढ़ी उतरी तो पुल-सिरात पर पड़ा डेरा,",
                    "हाजी मक्के जाएँ भले, मैं मुख देखूँ बस तेरा ।",
                    "आ जाओ इनायत कादरी! मन चाहे दरस सवेरा,",
                    "मैं बाट जोह रही, कभी आ कर ले फेरा !"
                ],
                "poetic_english": [
                    "Stepping upon the first stair down, I pitch my tent on Sirat's brink;",
                    "Let pilgrims journey to Mecca’s stone—of Thy face alone I think!",
                    "Come, Inayat Qadiri, my soul's desire, my guiding light:",
                    "I stand waiting in yearning: dispel this lonely night!"
                ]
            },
            {
                "original": [
                    "पहली रात है साल दी दिल खौफ़े मेरा ।  ",
                    "डूंघी गोर कढेंद्या होया लहदों डेरा ।  ",
                    "पहला बन्द खोल्हद्यां मूंह काअबे मेरा ।  ",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "hindi_gloss": [
                    "पहली (प्रथम) रात (रात है) है (है) साल (नए साल की/कब्र की), दिल (हृदय) खौफ़े (भयभीत कांपता है) मेरा (मेरा),",
                    "डूंघी (गहरी) गोर (कब्र) कढेंद्या (खोदते हुए) होया (हुआ) लहदों (कब्र की संकरी कोठरी में) डेरा (डेरा),",
                    "पहला (कफन का पहला) बन्द (बंधन) खोल्हद्यां (खोलते ही) मूंह (मुखड़ा) काअबे (काबा की दिशा में किया गया) मेरा (मेरा),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "english_gloss": [
                    "पहली (the first) रात (night) है (is) साल (of the year/grave), दिल (heart) खौफ़े (trembles in fear) मेरा (mine),",
                    "डूंघी (deep) गोर (grave) कढेंद्या (digging) होया (made) लहदों (in the burial niche) डेरा (camp),",
                    "पहला (the first) बन्द (knot of shroud) खोल्हद्यां (unloosing) मूंह (face) काअबे (towards Kaaba) मेरा (mine),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "poetic_hindi": [
                    "कब्र की पहली रात है आई, दिल कांपे थर-थर मेरा,",
                    "गहरी गोर में खोदी कोठरी, लहद में डाला डेरा ।",
                    "कफ़न का पहला बंद खुला, मुख काबे की ओर फेरा,",
                    "मैं बाट जोह रही, कभी आ कर ले फेरा !"
                ],
                "poetic_english": [
                    "The first grim midnight in the tomb sets my poor heart quaking low;",
                    "Digging the deep and narrow grave, down to the earthen trench I go.",
                    "Unloosing the shroud's first binding knot, turning towards the sacred stone:",
                    "I stand waiting in yearning: leave me not here alone!"
                ]
            },
            {
                "original": [
                    "मिली है बांग रसूल दी फुल्ल खिड़्या मेरा ।  ",
                    "सदा होया मैं हाज़री हां हाज़र तेरा ।  ",
                    "हर पल तेरी हाज़री इहो सजदा मेरा ।  ",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "hindi_gloss": [
                    "मिली (सुनाई पड़ी) है (है) बांग (अज़ान/पुकार) रसूल (रसूल की), दी (से) फुल्ल (कमल-पुष्प) खिड़्या (खिल उठा) मेरा (मेरा हृदय),",
                    "सदा (सदा के लिए) होया (हो गई) मैं (मेरी) हाज़री (उपस्थिति), हां (हूँ मैं सदा) हाज़र (उपस्थित) तेरा (तेरा सेवक),",
                    "हर (प्रत्येक) पल (क्षण) तेरी (तेरी) हाज़री (उपस्थिति में रहना ही) इहो (यही) सजदा (सच्चा सजदा है) मेरा (मेरा),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "english_gloss": [
                    "मिली (heard) है (is) बांग (the call) रसूल (of the Prophet) दी (of), फुल्ल (flower) खिड़्या (bloomed) मेरा (my heart),",
                    "सदा (forever) होया (became) मैं (my) हाज़री (attendance), हां (am I) हाज़र (present) तेरा (Thy servant),",
                    "हर (every) पल (moment) तेरी (Thy) हाज़री (presence) इहो (this is) सजदा (prostration) मेरा (mine),",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "poetic_hindi": [
                    "रसूल की पावन बाँग सुनी तो खिल उठा कमल-मन मेरा,",
                    "सदा-सदा की हाज़िरी पाई, मैं हाज़िर सेवक तेरा ।",
                    "हर पल तेरी हाज़िरी में रहना, यही सजदा है मेरा,",
                    "मैं बाट जोह रही, कभी आ कर ले फेरा !"
                ],
                "poetic_english": [
                    "Hearing the Prophet’s holy call, my blossoming heart rejoices free;",
                    "Enrolled forever in Thy court: 'Behold, I stand present before Thee!';",
                    "To dwell each instant in Thy sight is my eternal, living prayer:",
                    "I stand waiting in yearning: come, O Beloved Fair!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा भड़कन शहु लई सीने विच भाहीं ।  ",
                    "औखा पैंडा प्रेम दा सो घटदा नाहीं ।  ",
                    "पै धक्के दिल विच झेड़ दे सिर धाईं बेरा ।  ",
                    "मैं उडीकां कर रही कदी आ कर फेरा ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ला कहता है) भड़कन (धधक रही हैं) शहु (प्रभु के) लई (लिए) सीने (हृदय) विच (में) भाहीं (विरह की ज्वालाएं),",
                    "औखा (कठिन है) पैंडा (मार्ग) प्रेम (प्रेम) दा (का), सो (जो कभी) घटदा (कम) नाहीं (नहीं होता),",
                    "पै (पड़ रहे हैं) धक्के (धक्के) दिल (हृदय) विच (में) झेड़ (विवादों) दे (के), सिर (सिर पर) धाईं (दौड़ती हुई विपदाओं का) बेरा (बेड़ा आ पड़ा है),",
                    "मैं (मैं तेरी) उडीकां (प्रतीक्षा) कर (कर) रही (रही हूँ) कदी (कभी तो) आ (आकर) कर (कर ले) फेरा (फेरा) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh says) भड़कन (blazing) शहु (for the Lord) लई (for) सीने (in chest) विच (in) भाहीं (flames),",
                    "औखा (arduous is) पैंडा (the road) प्रेम (of Love) दा (of), सो (which) घटदा (diminishes) नाहीं (not),",
                    "पै (buffeted by) धक्के (blows) दिल (heart) विच (in) झेड़ (of strife) दे (of), सिर (upon head) धाईं (surging) बेरा (fleet of sorrows),",
                    "मैं (I) उडीकां (wait in yearning) कर (am) रही (standing) कदी (sometime) आ (come) कर (make) फेरा (a visit) ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा! सीने में विरह-ज्वाला भड़कती, घटती नाहीं,",
                    "कठिन पंथ है प्रेम का, जग-झंझट धक्के खाई ।",
                    "सिर पर दुखों का बेड़ा डोले, दिल बेचैन घनेरा,",
                    "मैं बाट जोह रही, कभी आ कर ले फेरा !"
                ],
                "poetic_english": [
                    "Flames of longing for the Lord blaze in poor Bulleh’s breast;",
                    "Rugged the pathway of true Love, giving no hour of rest.",
                    "Buffeted by the world’s harsh strife, amidst the stormy sea:",
                    "I stand waiting in yearning: come sometime unto me!"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी सूफी रहस्यवाद का 'एस्केटोलॉजी' (परलोक-विद्या) और विरह-काव्य का चरम संगम है। डोली (मृत्यु), पुल-सिरात (कर्मों का पुल), गोर (कब्र) और कफन का खुलना—इन सभी कठोर सत्यों के सम्मुख साधक केवल एक ही सहारा जानता है: 'दिलदार मुहम्मद अरबी' और 'इनायत कादरी'। जब तक सांसारिक काबा और हाजियों के अनुष्ठान बाह्य रहते हैं, तब तक आत्मा को शांति नहीं मिलती; शांति तभी मिलती है जब मुर्शिद के प्रत्यक्ष दीदार से हर पल 'हाज़िरी' बन जाता है।"
    },
    {
        "id": 92,
        "title": "मैनूं इश्क हुलारे देंदा",
        "title_english": "Love Gives Me Sweet Ecstatic Swings",
        "historical_context": "इस काफी में बुल्ले शाह आध्यात्मिक मस्ती (हाल / वज्द) का वर्णन करते हैं। प्रेम की तरंगें जब उठती हैं, तो साधक का मुख स्वयं प्रियतम की वाणी बोलने लगता है ('मूंह चढ़आ यार बुलेंदा')। वे कुरान की आयत 'नहनु अकरबु इलैहि मिन हब्लिल वरीद' (हम तुम्हारी गर्दन की नस से भी अधिक निकट हैं) का उल्लेख करते हुए कहते हैं कि मेरी जाति आदम वाली है और मैं शिया-सुन्नी, जटाधारी-मुंडी के समस्त सांप्रदायिक बंधनों से मुक्त (फारिग) हो चुका हूँ।",
        "meter": "पंजाबी काफी (चतुष्पदी, तुक: देंदा / बुलेंदा / झुलेंदा / मनेंदा / भुलेंदा)",
        "raga": "राग काफी / बहार",
        "theme": "इश्क के हुलारे, नहनु-अकरब, सांप्रदायिक संकीर्णताओं से मुक्ति, शाह इनायत का जमाल",
        "stanzas": [
            {
                "original": [
                    "मैनूं इश्क हुलारे देंदा ।  ",
                    "मूंह चढ़आ यार बुलेंदा ।"
                ],
                "hindi_gloss": [
                    "मैनूं (मुझको) इश्क (इश्क/ईश्वरीय प्रेम) हुलारे (झोंके/मस्ती की तरंगें) देंदा (देता है) ।",
                    "मूंह (मेरे मुख पर) चढ़आ (आरूढ़ होकर) यार (स्वयं प्रियतम प्रभु) बुलेंदा (बोलता है) ।"
                ],
                "english_gloss": [
                    "मैनूं (unto me) इश्क (divine love) हुलारे (ecstatic swings/surges) देंदा (gives) ।",
                    "मूंह (upon my lips) चढ़आ (mounted) यार (the Beloved) बुलेंदा (speaks) ।"
                ],
                "poetic_hindi": [
                    "मुझको इश्क हुलारे देता, मुख पर चढ़ कर यार ही बोलता !"
                ],
                "poetic_english": [
                    "Love rocks me in ecstatic swings, and on my tongue the Lover sings!"
                ]
            },
            {
                "original": [
                    "की पुच्छदा हैं की ज़ात सफ़्फ़ात मेरी, उहो आदम वाली ज़ात मेरी,  ",
                    "नहुन-अकरब दे विच घात मेरी, विच रब्ब दा सिर झुलेंदा ।  ",
                    "मैनूं इश्क हुलारे देंदा ।"
                ],
                "hindi_gloss": [
                    "की (क्या) पुच्छदा (पूछता) हैं (है कि) की (क्या) ज़ात (जाति और) सफ़्फ़ात (गुण/लक्षण हैं) मेरी (मेरे), उहो (वही मूल) आदम (आदम) वाली (की) ज़ात (जाति) मेरी (मेरी है),",
                    "नहुन-अकरब ('नहनु अकरब'—हम गर्दन की नस से भी निकट हैं) दे (के) विच (भीतर) घात (रहस्य/अवस्था) मेरी (मेरी है), विच (जिसके भीतर) रब्ब (परमात्मा) दा (का) सिर (नूर) झुलेंदा (झूमता है) ।",
                    "मैनूं इश्क हुलारे देंदा ।"
                ],
                "english_gloss": [
                    "की (what) पुच्छदा (askest) हैं (thou) की (what) ज़ात (caste) सफ़्फ़ात (attributes) मेरी (mine), उहो (that very) आदम (of Adam) वाली (belonging) ज़ात (caste) मेरी (mine),",
                    "नहुन-अकरब ('We are nearer than the jugular vein') दे (of) विच (in) घात (station/ambush) मेरी (mine), विच (wherein) रब्ब (of God) दा (the) सिर (radiance) झुलेंदा (sways) ।",
                    "मैनूं इश्क हुलारे देंदा ।"
                ],
                "poetic_hindi": [
                    "क्या पूछता है जाति-सिफ़त मेरी? आदम वाली जात मेरी,",
                    "'नहनु-अक़रब' में वास मेरा, जहाँ रब का नूर झूलता !"
                ],
                "poetic_english": [
                    "Why ask my caste or lineage here? Adam's human line I wear;",
                    "Nearer than the jugular vein I abide, where God's own splendors sway and glide!"
                ]
            },
            {
                "original": [
                    "किते शिया ते किते सुन्नी ए किते जटाधारी किते मुन्नी ए,  ",
                    "मेरी सभ से फ़ारग कुन्नी ए जो कहां सो यार मनेंदा ।  ",
                    "मैनूं इश्क हुलारे देंदा ।"
                ],
                "hindi_gloss": [
                    "किते (कहीं संसार में) शिया (शिया) ते (तथा) किते (कहीं) सुन्नी (सुन्नी का झगड़ा) ए (है), किते (कहीं) जटाधारी (जटा रखने वाले संन्यासी) किते (कहीं) मुन्नी (सिर मुंडाने वाले जैन/मुनि) ए (हैं),",
                    "मेरी (मेरी तो) सभ (इन सबसे) से (से) फ़ारग (सर्वथा मुक्त) कुन्नी (मटकी/दुनिया) ए (है), जो (जो कुछ भी) कहां (मैं कहता हूँ) सो (वही मेरा) यार (प्रियतम) मनेंदा (मान लेता है) ।",
                    "मैनूं इश्क हुलारे देंदा ।"
                ],
                "english_gloss": [
                    "किते (somewhere) शिया (Shia) ते (and) किते (somewhere) सुन्नी (Sunni) ए (is), किते (somewhere) जटाधारी (matted-hair ascetics) किते (somewhere) मुन्नी (shaven-headed monks) ए (are),",
                    "मेरी (my) सभ (from all) से (from) फ़ारग (freed/unfettered) कुन्नी (vessel/abode) ए (is), जो (whatever) कहां (I say) सो (that) यार (the Friend) मनेंदा (approves) ।",
                    "मैनूं इश्क हुलारे देंदा ।"
                ],
                "poetic_hindi": [
                    "कहीं शिया और कहीं सुन्नी, कहीं जटाधारी, कहीं मुनि विराजे,",
                    "मेरी मटकी इन सबसे मुक्त, जो कहूँ सो यार माने साजे !"
                ],
                "poetic_english": [
                    "Somewhere Shia, somewhere Sunni strife; somewhere matted locks, somewhere shaven head;",
                    "My earthen pot is free from sectarian life, what I speak is blessed by the Friend instead!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा दूरों चल के आया जी, उहदी सूरत ने भरमाइआ जी,  ",
                    "ओसे पाक जमाल विखाइआ जी, उह हिक्क दम ना भुलेंदा ।  ",
                    "मैनूं इश्क हुलारे देंदा ।  ",
                    "मूंह चढ़आ यार बुलेंदा ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ला) दूरों (दूर प्रदेश से) चल (चल-) के (कर) आया (आया) जी (हे संतो), उहदी (उस प्रियतम की) सूरत (दिव्य छवि) ने (ने) भरमाइआ (मोहित कर लिया) जी,",
                    "ओसे (उसी ने मुझे अपना) पाक (परम पावन) जमाल (सौंदर्य) विखाइआ (दिखा दिया) जी, उह (वह अब) हिक्क (एक) दम (क्षण के लिए भी) ना (नहीं) भुलेंदा (भूलता) ।",
                    "मैनूं इश्क हुलारे देंदा, मूंह चढ़आ यार बुलेंदा ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh) दूरों (from afar) चल (journeying) के (having) आया (came) जी (O friends), उहदी (His) सूरत (countenance) ने (has) भरमाइआ (enchanted) जी,",
                    "ओसे (He Himself) पाक (holy) जमाल (beauty) विखाइआ (revealed) जी, उह (He) हिक्क (a single) दम (breath) ना (never) भुलेंदा (is forgotten) ।",
                    "मैनूं इश्क हुलारे देंदा, मूंह चढ़आ यार बुलेंदा ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा दूर देश से चलकर आया, उसकी सूरत ने मन भरमाया,",
                    "उसने अपना पाक जमाल दिखाया, एक पल भी न भुलाया जाता !",
                    "मुझको इश्क हुलारे देता, मुख पर चढ़ कर यार ही बोलता !"
                ],
                "poetic_english": [
                    "Bulleh journeyed from a distant shore, captivated by His radiant face;",
                    "His holy splendor opened evermore, never forgotten for a breath of space!",
                    "Love rocks me in ecstatic swings, and on my tongue the Lover sings!"
                ]
            }
        ],
        "philosophical_meaning": "जब जीवात्मा परमात्मा में लीन (फ़ना) हो जाती है, तो उसके अपने शब्द समाप्त हो जाते हैं; जो कुछ वह बोलती है, वह स्वयं परमात्मा की वाणी होती है (हदीस: 'कुन्तु सम्अहुल्लज़ी यस्मउ बिही व लिसानहुल्लज़ी यनतिकु बिही'—मैं उसके कान बन जाता हूँ जिससे वह सुनता है और उसकी जीभ बन जाता हूँ जिससे वह बोलता है)। शिया-सुन्नी और हिंदू-जैन के बाह्य भेद मिट जाते हैं।"
    },
    {
        "id": 93,
        "title": "मैनूं की होया हुन मैथों गई गवाती मैं",
        "title_english": "What Hath Befallen Me? From Me My 'I-ness' Is Lost and Gone!",
        "historical_context": "इस काफी में बुल्ले शाह अहंकार के पूर्ण विलीनीकरण (फ़ना-फ़िल-हक़) का उत्सव मनाते हैं। संसार उन्हें 'कमली' (पागल) कहता है, किंतु वे कहते हैं कि मुझे कुछ नहीं हुआ सिवाय इसके कि मेरी झूठी 'मैं' (अहं) मुझसे सदा के लिए खो गई है। अब जब वे अपने भीतर देखते हैं, तो अपनी कोई सत्ता नहीं दिखाई देती; सिर से पैर तक केवल वही प्रियतम दिखाई देता है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, तुक: मैं / तूं / नैं / कैं / तैं)",
        "raga": "राग तिलंग / काफी",
        "theme": "अहंकार का लय (फ़ना), अद्वैत दर्शन, 'अनलहक़' का रहस्य, सांसारिक लोक-लाज से मुक्ति",
        "stanzas": [
            {
                "original": [
                    "मैनूं की होया क्यों मैनूं कमली कहन्दी हैं ।  ",
                    "मैनूं की होया हुन मैथों गई गवाती मैं ।"
                ],
                "hindi_gloss": [
                    "मैनूं (मुझको) की (क्या) होया (हुआ है), क्यों (क्यों) मैनूं (मुझको) कमली (पगली/दीवानी) कहन्दी (कहती) हैं (हो सखियो) ।",
                    "मैनूं (मुझको) की (क्या) होया (हुआ है—केवल इतना ही कि), हुन (अब) मैथों (मुझसे) गई (खो गई है) गवाती (सदा के लिए नष्ट हो गई) मैं (मेरी 'मैं' / अहंकार) ।"
                ],
                "english_gloss": [
                    "मैनूं (unto me) की (what) होया (has happened), क्यों (why) मैनूं (me) कमली (crazy/mad) कहन्दी (call) हैं (ye) ।",
                    "मैनूं (unto me) की (what) होया (befell), हुन (now) मैथों (from me) गई (is gone) गवाती (lost) मैं ('I' / ego) ।"
                ],
                "poetic_hindi": [
                    "मुझे क्या हुआ, क्यों मुझे कमली कहती हो सखी ?",
                    "मुझे क्या हुआ ? अब तो मुझसे मेरी 'मैं' ही खो गई सखी !"
                ],
                "poetic_english": [
                    "What hath befallen me, that ye call me a crazed and foolish maid?",
                    "What hath befallen me? From me my separate 'I' is lost and dead!"
                ]
            },
            {
                "original": [
                    "मैं विच वेखां तां मैं नहीं हुन्दी मैं विच दिसना एं मैं ।  ",
                    "मैनूं की होया हुन मैथों गई गवाती मैं ।"
                ],
                "hindi_gloss": [
                    "मैं (जब मैं अपने) विच (भीतर) वेखां (देखती हूँ), तां (तो) मैं (मेरी 'मैं') नहीं (नहीं) हुन्दी (दिखाई देती), मैं (मुझ) विच (के भीतर) दिसना (दिखाई देता) एं (है केवल) मैं (तू ही तू/परम प्रभु) ।",
                    "मैनूं की होया हुन मैथों गई गवाती मैं ।"
                ],
                "english_gloss": [
                    "मैं (myself) विच (within) वेखां (when I gaze), तां (then) मैं ('I') नहीं (not) हुन्दी (exist), मैं (in me) विच (within) दिसना (appearest) एं (Thou) मैं (alone) ।",
                    "मैनूं की होया हुन मैथों गई गवाती मैं ।"
                ],
                "poetic_hindi": [
                    "भीतर देखूँ तो 'मैं' न पाऊँ, मुझमें तू ही तू मुस्काए !"
                ],
                "poetic_english": [
                    "Gazing within, no trace of self appears—Thou only shinest through my tears!"
                ]
            },
            {
                "original": [
                    "सिर तों पैर तीकर वी तूं हैं अन्दर बाहर हैं तूं ।  ",
                    "मैनूं की होया हुन मैथों गई गवाती मैं ।"
                ],
                "hindi_gloss": [
                    "सिर (सिर) तों (से लेकर) पैर (पैरों) तीकर (तक) वी (भी) तूं (तू ही) हैं (है), अन्दर (भीतर भी) बाहर (और बाहर भी) हैं (है) तूं (तू ही तू) ।",
                    "मैनूं की होया हुन मैथों गई गवाती मैं ।"
                ],
                "english_gloss": [
                    "सिर (head) तों (from) पैर (to feet) तीकर (unto) वी (too) तूं (Thou) हैं (art), अन्दर (within) बाहर (without) हैं (art) तूं (Thou) ।",
                    "मैनूं की होया हुन मैथों गई गवाती मैं ।"
                ],
                "poetic_hindi": [
                    "सिर से लेकर पाँव तलक तू, भीतर तू और बाहर तू !"
                ],
                "poetic_english": [
                    "From head to foot Thou art the whole, without, within, Thou art the Soul!"
                ]
            },
            {
                "original": [
                    "छुट्ट पई उरारों पारों ना बेड़ी ना नैं ।  ",
                    "मैनूं की होया हुन मैथों गई गवाती मैं ।"
                ],
                "hindi_gloss": [
                    "छुट्ट (छूट) पई (गई हूँ मैं) उरारों (इस तट से भी और) पारों (उस पार के तट से भी), ना (न अब कोई) बेड़ी (नाव बची है) ना (न ही कोई) नैं (नदी/भवसागर शेष रहा) ।",
                    "मैनूं की होया हुन मैथों गई गवाती मैं ।"
                ],
                "english_gloss": [
                    "छुट्ट (released) पई (am I) उरारों (from hither bank) पारों (and thither bank), ना (no) बेड़ी (boat) ना (nor) नैं (river remains) ।",
                    "मैनूं की होया हुन मैथों गई गवाती मैं ।"
                ],
                "poetic_hindi": [
                    "इस पार और उस पार से छूटी, न कोई नैया, न नदी रही !"
                ],
                "poetic_english": [
                    "Free from this shore and from the further side, no boat, no stream, where boundless depths abide!"
                ]
            },
            {
                "original": [
                    "मनसूर प्यारे केहा अनलहक्क कहो कहाइआ कैं ।  ",
                    "मैनूं की होया हुन मैथों गई गवाती मैं ।"
                ],
                "hindi_gloss": [
                    "मनसूर (मंसूर) प्यारे (प्यारे ने) केहा (कहा था) अनलहक्क ('अनलहक़'—मैं ही सत्य हूँ), कहो (अब बताओ कि यह वचन) कहाइआ (किसने कहलवाया था) कैं (किसने—स्वयं परमात्मा ने ही तो) ।",
                    "मैनूं की होया हुन मैथों गई गवाती मैं ।"
                ],
                "english_gloss": [
                    "मनसूर (Mansur) प्यारे (the beloved) केहा (uttered) अनलहक्क ('I am the Truth'), कहो (say) कहाइआ (caused to speak) कैं (who else but God) ।",
                    "मैनूं की होया हुन मैथों गई गवाती मैं ।"
                ],
                "poetic_hindi": [
                    "प्यारे मंसूर ने 'अनलहक' बोला, कहो किसने यह वचन कहलवाया ?"
                ],
                "poetic_english": [
                    "Beloved Mansur cried 'I am the Truth!'—who made him speak that word uncouth?"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु ओसे दा आशक आपना आप वंजाइआ तैं ।  ",
                    "मैनूं की होया हुन मैथों गई गवाती मैं ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ला कहता है) शहु (वह प्रभु) ओसे (उसी) दा (का) आशक (सच्चा प्रेमी बन जाता है), आपना (जिसने अपना) आप (पृथक अस्तित्व/अहंकार) वंजाइआ (मिटा दिया) तैं (तूने) ।",
                    "मैनूं की होया हुन मैथों गई गवाती मैं ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh says) शहु (the Lord) ओसे (of that one) दा (of) आशक (lover becomes), आपना (thine own) आप (self) वंजाइआ (lost/dissolved) तैं (hast thou) ।",
                    "मैनूं की होया हुन मैथों गई गवाती मैं ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा शौह उसी का आशिक, जिसने अपना आप मिटाया !",
                    "मुझे क्या हुआ ? अब तो मुझसे मेरी 'मैं' ही खो गई सखी !"
                ],
                "poetic_english": [
                    "The Lord becomes the lover of that soul who drowns his ego in the cosmic Whole!",
                    "What hath befallen me? From me my separate 'I' is lost and dead!"
                ]
            }
        ],
        "philosophical_meaning": "सूफी दर्शन का 'फ़ना' (Ego-death) इस काफी का केंद्रीय विषय है। जब जीवात्मा अपनी सीमा (मैं) खो देती है, तो वह असीम (तू) हो जाती है। मंसूर का 'अनलहक़' कोई नास्तिकता या घमंड नहीं था, बल्कि वह अवस्था थी जहाँ मंसूर का अहंकार समाप्त हो चुका था और केवल परमात्मा ही उसके माध्यम से बोल रहा था।"
    },
    {
        "id": 94,
        "title": "मैनूं सुक्ख दा सुनेहड़ा तूं झब लिआवीं वे",
        "title_english": "Bring Me The Tidings of Joy With Speed, O Wayfarer!",
        "historical_context": "इस काफी में विरहिणी जीवात्मा एक राहगीर / पथिक (पांधी) से प्रार्थना करती है कि वह उसके प्रियतम तक उसका संदेश पहुँचा दे और वहाँ से कुशल-क्षेम का समाचार शीघ्र लेकर आए। वह विरह में झुक चुकी है, डूब चुकी है; बाल बिखरे हैं, गले में शोक का परांदा है। वह प्रियतम के मिलन के लिए अपना सर्वस्व न्योछावर करने को तत्पर है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: पांधिया हो)",
        "raga": "राग तिलंग / सारंग",
        "theme": "पथिक द्वारा संदेश भेजना, विरह की दीन-हीन दशा, सर्वस्व-समर्पण, मिलन की आतुरता",
        "stanzas": [
            {
                "original": [
                    "मैनूं सुक्ख दा सुनेहड़ा तूं झब लिआवीं वे,  ",
                    "पांधिया हो ।"
                ],
                "hindi_gloss": [
                    "मैनूं (मुझको) सुक्ख (आनंद/कुशल-क्षेम) दा (का) सुनेहड़ा (संदेश) तूं (तू) झब (शीघ्र) लिआवीं (लेकर आना) वे (हे),",
                    "पांधिया (हे पथिक/राहगीर) हो (हे) ।"
                ],
                "english_gloss": [
                    "मैनूं (unto me) सुक्ख (of joy) दा (the) सुनेहड़ा (message/tidings) तूं (thou) झब (swiftly) लिआवीं (bring) वे (O),",
                    "पांधिया (O traveler/wayfarer) हो (O) ।"
                ],
                "poetic_hindi": [
                    "मुझको सुख का संदेशा तू शीघ्र ले आ री, ओ पथिक प्यारे !"
                ],
                "poetic_english": [
                    "Bring me the tidings of joy with speed, O wayfarer on the road!"
                ]
            },
            {
                "original": [
                    "मैं कुबड़ी मैं डुबड़ी होईआं,  ",
                    "मेरे सभ दुक्खड़े बतलावीं वे ।  ",
                    "पांधिया हो ।"
                ],
                "hindi_gloss": [
                    "मैं (मैं विरह के भार से) कुबड़ी (झुक गई हूँ) मैं (और आंसुओं में) डुबड़ी (डूब गई) होईआं (हो चुकी हूँ),",
                    "मेरे (मेरे ये) सभ (समस्त) दुक्खड़े (दुख-दर्द प्रियतम को जाकर) बतलावीं (कह सुनाना) वे ।",
                    "पांधिया हो ।"
                ],
                "english_gloss": [
                    "मैं (I am) कुबड़ी (bent with grief) मैं (I) डुबड़ी (drowned in tears) होईआं (have become),",
                    "मेरे (my) सभ (all) दुक्खड़े (sorrows) बतलावीं (narrate) वे (O) ।",
                    "पांधिया हो ।"
                ],
                "poetic_hindi": [
                    "मैं झुक गई, मैं विरह में डूबी, मेरे सब दुखड़े बतलाना रे !"
                ],
                "poetic_english": [
                    "Bent double with grief, drowned in my tears, recount to Him my bitter fears!"
                ]
            },
            {
                "original": [
                    "खुल्हियां लिटां गल दसत परांदा,  ",
                    "इह गल्ल आखीं ना शरमावीं वे ।  ",
                    "पांधिया हो ।"
                ],
                "hindi_gloss": [
                    "खुल्हियां (बिखरी हुई हैं) लिटां (केशों की लटें) गल (गले में) दसत (हाथों में शोक का) परांदा (परांदा है),",
                    "इह (यह) गल्ल (सच्ची बात) आखीं (कहने में) ना (मत) शरमावीं (संकोच करना) वे ।",
                    "पांधिया हो ।"
                ],
                "english_gloss": [
                    "खुल्हियां (unbound/disheveled) लिटां (tresses) गल (on neck) दसत (in hands) परांदा (braid-ribbon of mourning),",
                    "इह (this) गल्ल (fact) आखीं (speaking) ना (do not) शरमावीं (hesitate) वे (O) ।",
                    "पांधिया हो ।"
                ],
                "poetic_hindi": [
                    "बिखरी लटें, विरह का बाना, यह कहने में मत सकुचाना रे !"
                ],
                "poetic_english": [
                    "My hair disheveled, robes of grief display, tell this plain truth without delay!"
                ]
            },
            {
                "original": [
                    "इक्क लक्ख देंदी मैं दो लक्ख देसां,  ",
                    "मैनूं प्यारा आण मिलावीं वे ।  ",
                    "पांधिया हो ।"
                ],
                "hindi_gloss": [
                    "इक्क (एक) लक्ख (लाख टका) देंदी (देती हूँ) मैं (और आवश्यकता हुई तो) दो (दो) लक्ख (लाख भी) देसां (न्योछावर कर दूँगी),",
                    "मैनूं (मुझको बस) प्यारा (मेरे प्यारे प्रियतम से) आण (आकर) मिलावीं (मिला दे) वे ।",
                    "पांधिया हो ।"
                ],
                "english_gloss": [
                    "इक्क (one) लक्ख (hundred thousand) देंदी (I offer) मैं (I) दो (two) लक्ख (hundred thousand) देसां (will give),",
                    "मैनूं (me) प्यारा (my Beloved) आण (coming) मिलावीं (unite with) वे (O) ।",
                    "पांधिया हो ।"
                ],
                "poetic_hindi": [
                    "एक लाख दूँ, दो लाख दूँगी, मुझे प्यारे से आ मिला दे रे !"
                ],
                "poetic_english": [
                    "A hundred thousand coins I yield, two hundred thousand more for Thee,",
                    "If Thou wilt bring my Love across the field to set my weeping spirit free!"
                ]
            },
            {
                "original": [
                    "यारां लिख किताबत भेजी,  ",
                    "किते गोशे बह समझावीं वे ।  ",
                    "पांधिया हो ।"
                ],
                "hindi_gloss": [
                    "यारां (मैंने अपने प्रियतम के लिए) लिख (लिखकर) किताबत (प्रेम-पत्र) भेजी (भेजा है),",
                    "किते (किसी) गोशे (एकांत कोने में) बह (बैठकर उन्हें यह) समझावीं (समझा देना) वे ।",
                    "पांधिया हो ।"
                ],
                "english_gloss": [
                    "यारां (unto the Friend) लिख (writing) किताबत (a letter) भेजी (have sent),",
                    "किते (some) गोशे (solitary nook) बह (sitting) समझावीं (explain) वे (O) ।",
                    "पांधिया हो ।"
                ],
                "poetic_hindi": [
                    "यार को मैंने चिट्ठी भेजी, एकांत में बैठ समझाना रे !"
                ],
                "poetic_english": [
                    "A letter have I penned unto the Friend, in some quiet corner explain its end!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु दियां मुड़न मुहारां,  ",
                    "लिख पत्तियां तूं झब पावीं वे ।  ",
                    "मैनूं सुक्ख दा सुनेहड़ा तूं झब लिआवीं वे,  ",
                    "पांधिया हो ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ले के) शहु (प्रभु-शाह के ऊंट की) दियां (की) मुड़न (मुड़ जाएं) मुहारां (बागडौरें इस ओर),",
                    "लिख (लिखकर) पत्तियां (प्रेम-पाती) तूं (तू) झब (शीघ्र) पावीं (भेजना) वे ।",
                    "मैनूं सुक्ख दा सुनेहड़ा तूं झब लिआवीं वे, पांधिया हो ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh’s) शहु (Lord’s) दियां (of) मुड़न (may turn) मुहारां (reins towards me),",
                    "लिख (writing) पत्तियां (epistles) तूं (thou) झब (swiftly) पावीं (send) वे (O) ।",
                    "मैनूं सुक्ख दा सुनेहड़ा तूं झब लिआवीं वे, पांधिया हो ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा शौह की मुड़ें मुहारें, लिख पाती तुरंत पहुँचाना रे !",
                    "मुझको सुख का संदेशा तू शीघ्र ले आ री, ओ पथिक प्यारे !"
                ],
                "poetic_english": [
                    "That Bulleh’s Lord may turn His bridle rein, speed forth the letter through the wind and rain!",
                    "Bring me the tidings of joy with speed, O wayfarer on the road!"
                ]
            }
        ],
        "philosophical_meaning": "सूफी परंपरा में 'पांधी' (राहगीर / दूत) गुरु या आध्यात्मिक सत्संग का प्रतीक है। जीवात्मा संसार में विरह से व्याकुल होकर अपनी पीड़ा का संदेश प्रियतम तक पहुँचाना चाहती है। 'एक लाख दूँ, दो लाख दूँगी' का भावार्थ सांसारिक धन नहीं, बल्कि अपने अहंकार और संपूर्ण अस्तित्व का उत्सर्ग है।"
    },
    {
        "id": 95,
        "title": "मैं विच मैं ना रह गई राई",
        "title_english": "Not An Iota of 'I' Remained In Me",
        "historical_context": "यह 10 बंधों की एक अत्यंत गंभीर, भावपूर्ण और शास्त्रीय काफी है। जब से प्रियतम से प्रीत लगाई है, तब से साधक के भीतर अहंकार की एक रत्ती भी शेष नहीं बची है। मिलन का यह अनुभव 'गूंगे का गुड़' है जिसे वाणी से व्यक्त नहीं किया जा सकता। बुल्ले शाह विरह और मिलन के नाना विरोधाभासों को पार करते हुए अंततः दसवें द्वार पर प्रियतम के सम्मुख स्वयं को पूर्णतः न्योछावर कर देते हैं।",
        "meter": "पंजाबी काफी (10 अंतरे, तुक: राई / लगाई / खाई / सिधाई / आशनाई)",
        "raga": "राग काफी / भैरवी",
        "theme": "अहंकार-शून्यता, गूंगे का गुड़, वहदत और हैरत, दसवां द्वार, पूर्ण आत्म-समर्पण",
        "stanzas": [
            {
                "original": [
                    "मैं विच मैं ना रह गई राई ।  ",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "hindi_gloss": [
                    "मैं (मेरे) विच (भीतर) मैं ('मैं' / अहंकार) ना (नहीं) रह (रह) गई (गई) राई (राई-भर भी/ज़रा सी भी) ।",
                    "जब (जब) की (से) पिया (प्रियतम) संग (के साथ) पीत (प्रीत/प्रेम) लगाई (लगाई है) ।"
                ],
                "english_gloss": [
                    "मैं (in me) विच (within) मैं ('I' / ego) ना (not) रह (remained) गई (went) राई (a mustard seed's iota) ।",
                    "जब (since) की (when) पिया (Beloved) संग (with) पीत (love) लगाई (pledged) ।"
                ],
                "poetic_hindi": [
                    "मुझमें 'मैं' न रही रत्ती-भर, जब से पिया संग प्रीत लगाई !"
                ],
                "poetic_english": [
                    "Not an iota of 'I' remained in me, since with my Lover I pledged to be!"
                ]
            },
            {
                "original": [
                    "जद वसल वसाल बणाएगा, तद गुंगे दा गुड़ खाएगा,  ",
                    "सिर पैर ना आपना पाएगा, मैं इह होर ना किसे बणाई ।  ",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "hindi_gloss": [
                    "जद (जब) वसल (मिलन) वसाल (और एकात्मता) बणाएगा (बनाएगा प्रभु), तद (तब साधक) गुंगे (गूंगे) दा (के) गुड़ (गुड़ के स्वाद के समान अवर्णनीय आनंद) खाएगा (पाएगा),",
                    "सिर (सिर और) पैर (पैर की) ना (नहीं) आपना (अपनी सुध-बुध) पाएगा (पा सकेगा), मैं (मेरे) इह (यह अवस्था) होर (और) ना (नहीं) किसे (किसी अन्य ने) बणाई (बनाई है) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "english_gloss": [
                    "जद (when) वसल (union) वसाल (ultimate communion) बणाएगा (He establishes), तद (then) गुंगे (of the mute) दा (of) गुड़ (molasses/sweetness) खाएगा (will taste),",
                    "सिर (head) पैर (nor feet) ना (not) आपना (his own) पाएगा (will find), मैं (to me) इह (this state) होर (other) ना (no one) किसे (anyone else) बणाई (wrought) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "poetic_hindi": [
                    "जब मिलन का संयोग रचाएगा, तब गूंगे का गुड़ खाएगा,",
                    "न सिर-पाँव की सुध रह पाएगी, यह दशा प्रेम ने बनाई !"
                ],
                "poetic_english": [
                    "When union seals the bond divine, like mute men tasting honeyed sweets;",
                    "Lost to all sense of limb and line, in wonder every heartbeat beats!"
                ]
            },
            {
                "original": [
                    "होए नैन नैणां दे बरदे, दरशन सै कोहां तों करदे,  ",
                    "पल्ल पल्ल दौड़न मारे डरदे, तैं कोई लालच घत भरमाई ।  ",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "hindi_gloss": [
                    "होए (हो गए हैं) नैन (मेरे नेत्र) नैणां (तेरे नेत्रों) दे (के) बरदे (गुलाम/सेवक), दरशन (साक्षात्कार) सै (सैकड़ों) कोहां (कोसों की दूरी) तों (से भी) करदे (करते हैं),",
                    "पल्ल (पल-) पल्ल (पल) दौड़न (दौड़ते हैं) मारे (मारे) डरदे (भय के), तैं (तूने) कोई (कोई ऐसा) लालच (प्रेम-लोभ) घत (डालकर) भरमाई (मोहित कर लिया है) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "english_gloss": [
                    "होए (became) नैन (eyes) नैणां (of Thy eyes) दे (of) बरदे (captives/slaves), दरशन (vision) सै (hundreds) कोहां (of leagues) तों (from) करदे (behold),",
                    "पल्ल (moment) पल्ल (by moment) दौड़न (run) मारे (struck by) डरदे (awe/fear), तैं (Thou) कोई (some) लालच (enticement) घत (casting) भरमाई (beguiled) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "poetic_hindi": [
                    "नैन हुए तेरे नयनों के गुलाम, सौ कोसों से दरस करें,",
                    "पल-पल दौड़ें डर के मारे, प्रेम का लोभ डाल भरमाई !"
                ],
                "poetic_english": [
                    "My eyes became Thy glances' thrall, viewing Thy light across the miles;",
                    "Running in awe at every call, beguiled by Thine enchanting smiles!"
                ]
            },
            {
                "original": [
                    "हुन असां वहदत विच घर पाइआ, वासा हैरत दे संग आया,  ",
                    "जीवन जंमन मरन वंजाइआ, आपनी सुद्ध बुद्ध रही ना काई ।  ",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "hindi_gloss": [
                    "हुन (अब) असां (हमने) वहदत (अद्वैत/परम एकात्मता) विच (में) घर (अपना घर) पाइआ (बना लिया है), वासा (हमारा निवास) हैरत (असीम विस्मय/हैरानी) दे (के) संग (साथ) आया (आ गया है),",
                    "जीवन (जीना) जंमन (जन्म लेना और) मरन (मरना सब) वंजाइआ (मिटा दिया), आपनी (अपनी कोई) सुद्ध (सुध-) बुद्ध (बुद्धि) रही (रही) ना (नहीं) काई (कुछ भी) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "english_gloss": [
                    "हुन (now) असां (we) वहदत (in Divine Unity) विच (in) घर (home) पाइआ (found), वासा (abode) हैरत (with awe/astonishment) दे (with) संग (with) आया (came),",
                    "जीवन (living) जंमन (birth) मरन (death) वंजाइआ (effaced), आपनी (one’s own) सुद्ध (sense) बुद्ध (wit) रही (remained) ना (not) काई (any) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "poetic_hindi": [
                    "अद्वैत में घर पाया हमने, विस्मय के संग वास किया,",
                    "जन्म-मरण का फेर मिटाया, सुध-बुध अपनी बिसराई !"
                ],
                "poetic_english": [
                    "Within the Oneness now we dwell, in wonder lost and starry awe;",
                    "Erasing birth and death and hell, beyond all petty mortal law!"
                ]
            },
            {
                "original": [
                    "मैं जाता सी इश्क सुखाला, चहुं नदियां दा वहन उजाला,  ",
                    "कदी ते अग्ग भड़के कदी पाला, नित्त बिरहों अग्ग लगाई ।  ",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "hindi_gloss": [
                    "मैं (मैंने) जाता (समझा) सी (था कि) इश्क (प्रेम का मार्ग) सुखाला (अति सरल/सुखद है), चहुं (चारों) नदियां (नदियों का) वहन (निर्मल प्रवाह) उजाला (उज्ज्वल है),",
                    "कदी (किंतु कभी) ते (तो यहाँ) अग्ग (आग) भड़के (भड़कती है) कदी (कभी) पाला (शीत का कंपकंपी), नित्त (नित्य) बिरहों (विरह ने) अग्ग (अग्नि) लगाई (सुलगा रखी है) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "english_gloss": [
                    "मैं (I) जाता (thought) सी (was) इश्क (love) सुखाला (easy/gentle), चहुं (four) नदियां (rivers) दा (of) वहन (stream) उजाला (clear/bright),",
                    "कदी (sometimes) ते (indeed) अग्ग (fire) भड़के (flames) कदी (sometimes) पाला (freezing cold), नित्त (daily) बिरहों (separation) अग्ग (fire) लगाई (kindled) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "poetic_hindi": [
                    "समझा था मैंने इश्क सुगम है, जैसे चार नदियों का निर्मल प्रवाह,",
                    "कभी आग भड़के, कभी ठंड सतावे, नित्य विरह ने आग लगाई !"
                ],
                "poetic_english": [
                    "I thought that Love was smooth and sweet, a shining river flowing wide;",
                    "Yet scorching fires and freezing sleet now burn and freeze from side to side!"
                ]
            },
            {
                "original": [
                    "डेहों डेहों इश्क नक्कारे वज्जदे, आशक वेख उते वल्ल भज्जदे,  ",
                    "तड़ तड़ तिड़क गए लड़ लज्जदे, लग्ग गिआ नेहुं तां शरम सिधाई ।  ",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "hindi_gloss": [
                    "डेहों (दिन-) डेहों (दिन) इश्क (इश्क के) नक्कारे (रण-नगाड़े) वज्जदे (बजते हैं), आशक (प्रेमी) वेख (देखकर) उते (उसी) वल्ल (ओर) भज्जदे (दौड़ते हैं),",
                    "तड़ (तड़-) तड़ (तड़ करके) तिड़क (टूट) गए (गए) लड़ (आंचल/बंधन) लज्जदे (लोक-लाज के), लग्ग (लग) गिआ (गया) नेहुं (प्रेम) तां (तो) शरम (सारी लोक-शर्म) सिधाई (विदा हो गई) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "english_gloss": [
                    "डेहों (day) डेहों (by day) इश्क (of love) नक्कारे (kettledrums) वज्जदे (resound), आशक (lovers) वेख (seeing) उते (that) वल्ल (way) भज्जदे (rush),",
                    "तड़ (cracking) तड़ (snapping) तिड़क (split) गए (went) लड़ (hems) लज्जदे (of false modesty), लग्ग (attached) गिआ (is) नेहुं (love) तां (then) शरम (shame) सिधाई (departed) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "poetic_hindi": [
                    "दिन-प्रतिदिन इश्क-नगाड़े बजते, आशिक उस ओर दौड़ते हैं,",
                    "तड़क-तड़क लोक-लाज के बंधन टूटे, जब नेह लगा तो शर्म बिसराई !"
                ],
                "poetic_english": [
                    "Day after day Love's war-drums sound, towards the field the lovers fly;",
                    "Snapping the threads of modesty, all earthly shames and censures die!"
                ]
            },
            {
                "original": [
                    "प्यारे बस्स कर बहुती होई, तेरा इश्क मेरी दिलजोई,  ",
                    "तैं बिन मेरा सक्का ना कोई, अंमां बाबल भैन ना भाई ।  ",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "hindi_gloss": [
                    "प्यारे (हे प्यारे प्रियतम) बस्स (बस) कर (करो) बहुती (बहुत अधिक) होई (हो गई यह परीक्षा), तेरा (तेरा) इश्क (इश्क ही) मेरी (मेरी) दिलजोई (सांत्वना/हृदय का सहारा है),",
                    "तैं (तेरे) बिन (बिना) मेरा (मेरा) सक्का (सगा-संबंधी) ना (नहीं) कोई (कोई भी), अंमां (न अम्मा) बाबल (न पिता) भैन (न बहन) ना (न) भाई (भाई) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "english_gloss": [
                    "प्यारे (O Beloved) बस्स (enough) कर (make) बहुती (much) होई (has been), तेरा (Thy) इश्क (love is) मेरी (my) दिलजोई (heart’s sole comfort),",
                    "तैं (Thee) बिन (without) मेरा (my) सक्का (kin) ना (none) कोई (anyone), अंमां (neither mother) बाबल (nor father) भैन (sister) ना (nor) भाई (brother) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "poetic_hindi": [
                    "प्यारे! बस कर बहुत हुई अब, तेरा इश्क ही दिल की ढाढ़स,",
                    "तेरे बिन न कोई मेरा, न मात-पिता, न बहन-भाई !"
                ],
                "poetic_english": [
                    "O Sweet Beloved, hold Thy hand, Thy love alone my comfort stays;",
                    "No kin have I in all the land, no parents, kin, or worldly praise!"
                ]
            },
            {
                "original": [
                    "कदी जा असमानी बहन्दे हो, कदी इस जग्ग दा दुक्ख सहन्दे हो,  ",
                    "कदी पीरेमुग़ां बण बहन्दे हो, मैं तां इकसे नाच नचाई ।  ",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "hindi_gloss": [
                    "कदी (कभी) जा (जाकर) असमानी (सातवें आसमान पर) बहन्दे (विराजमान होते) हो (हो), कदी (कभी) इस (इस) जग्ग (संसार) दा (का) दुक्ख (दुख-दर्द) सहन्दे (सहते) हो (हो),",
                    "कदी (कभी) पीरेमुग़ां (शराबखाने के स्वामी/पीर-ए-मुगां) बण (बनकर) बहन्दे (बैठ जाते) हो (हो), मैं (मुझको) तां (तो तूने) इकसे (एक ही) नाच (नाच पर) नचाई (नचा रखा है) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "english_gloss": [
                    "कदी (sometimes) जा (going) असमानी (in skies) बहन्दे (sit) हो (Thou), कदी (sometimes) इस (of this) जग्ग (world) दा (of) दुक्ख (grief) सहन्दे (bearest) हो (Thou),",
                    "कदी (sometimes) पीरेमुग़ां (Master of the Tavern) बण (becoming) बहन्दे (sittest) हो (Thou), मैं (me) तां (then) इकसे (to one ceaseless) नाच (dance) नचाई (hast made dance) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "poetic_hindi": [
                    "कभी आसमान पर जा बैठो, कभी इस जग का दुख सहते हो,",
                    "कभी मदिरालय के स्वामी बनकर, मुझको ही नाच नचाई !"
                ],
                "poetic_english": [
                    "Sometimes Thou dwellest in the skies, sometimes enduring earthly pain;",
                    "Sometimes as Master of the Tavern, dancing my soul through joy and rain!"
                ]
            },
            {
                "original": [
                    "तेरे हिजरे विच मेरा हुजरा ए दुक्ख डाढा मैं पर गुज़रा ए,  ",
                    "कदे हो मायल मेरा मुजरा ए मैं तैथों घोल घुमाई ।  ",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "hindi_gloss": [
                    "तेरे (तेरे) हिजरे (विरह) विच (में ही) मेरा (मेरा) हुजरा (प्रार्थना-कक्ष/एकांत कुटीर) ए (है), दुक्ख (दुख) डाढा (अति भीषण) मैं (मुझ) पर (पर) गुज़रा (बीता) ए (है),",
                    "कदे (कभी तो) हो (होकर) मायल (कृपालु/प्रसन्न) मेरा (मेरी यह वंदना/) मुजरा (समर्पण स्वीकार कर) ए (हे प्रभु), मैं (मैं) तैथों (तुझ पर) घोल (न्योछावर) घुमाई (होती हूँ) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "english_gloss": [
                    "तेरे (Thy) हिजरे (separation) विच (in) मेरा (my) हुजरा (cell/retreat) ए (is), दुक्ख (sorrow) डाढा (immense) मैं (upon me) पर (upon) गुज़रा (passed) ए (has),",
                    "कदे (sometime) हो (becoming) मायल (inclined with favor) मेरा (my) मुजरा (homage/devotion) ए (accept), मैं (I) तैथों (upon Thee) घोल (sacrifice) घुमाई (render) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "poetic_hindi": [
                    "तेरे विरह में मेरी कुटिया, भारी दुख मुझ पर बीता है,",
                    "कभी तो कृपालु हो मेरा मुजरा ले, मैं तुझ पर बलिहारी जाई !"
                ],
                "poetic_english": [
                    "Within Thy parting stands my cell, a grievous load upon me lies;",
                    "Incline Thy grace, accept my song, as I dissolve before Thine eyes!"
                ]
            },
            {
                "original": [
                    "तुध कारन मैं ऐसा होया, तूं दरवाज़े बन्द कर सोया,  ",
                    "दर दसवें ते आण खलोया, कदे मन्न मेरी आशनाई ।  ",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "hindi_gloss": [
                    "तुध (तेरे) कारन (कारण) मैं (मेरी) ऐसा (ऐसी विह्वल दशा) होया (हो गई), तूं (और तू अपने) दरवाज़े (कपाट) बन्द (बंद) कर (करके) सोया (सो गया),",
                    "दर (द्वार) दसवें (दसवें गुप्त द्वार—दसम द्वार) ते (पर) आण (आकर) खलोया (खड़ा हो गया हूँ), कदे (कभी तो) मन्न (स्वीकार कर) मेरी (मेरी सच्ची) आशनाई (प्रीत/मैत्री) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "english_gloss": [
                    "तुध (for Thee) कारन (sake) मैं (I) ऐसा (such) होया (became), तूं (Thou) दरवाज़े (doors) बन्द (closed) कर (making) सोया (slept),",
                    "दर (at the door) दसवें (the tenth/mystic gate) ते (upon) आण (coming) खलोया (I stood), कदे (sometime) मन्न (accept) मेरी (my) आशनाई (love/friendship) ।",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "poetic_hindi": [
                    "तेरे कारण यह दशा भई, तू द्वार बंद कर सो गया रे,",
                    "दसवें द्वार पर आ खड़ा हुआ, कभी तो मान मेरी आशनाई !"
                ],
                "poetic_english": [
                    "For Thy sweet sake I turned to this, while Thou didst sleep behind the gate;",
                    "At the Tenth Portal now I knock: accept my love, resolve my fate!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु मैं तेरे वारे हां, मुक्ख वेखन दे वणजारे हां,  ",
                    "कुझ असीं वी तैनूं प्यारे हां, कि मैं ऐवें घोल घुमाई ।  ",
                    "जब की पिया संग पीत लगाई ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ला कहता है) शहु (हे प्रभु) मैं (मैं) तेरे (तुझ पर) वारे (बलिहारी) हां (हूँ), मुक्ख (तेरे पावन मुखड़े को) वेखन (देखने) दे (के) वणजारे (व्यापारी/पिपासु) हां (हम हैं),",
                    "कुझ (क्या कुछ) असीं (हम) वी (भी) तैनूं (तुझको) प्यारे (प्रिय) हां (हैं), कि (अथवा) मैं (मैं) ऐवें (व्यर्थ ही) घोल (न्योछावर होकर) घुमाई (घूम रही हूँ) ।",
                    "मैं विच मैं ना रह गई राई, जब की पिया संग पीत लगाई ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh says) शहु (O Lord) मैं (I am) तेरे (unto Thee) वारे (sacrificed) हां (am), मुक्ख (face) वेखन (beholding) दे (of) वणजारे (traders/seekers) हां (we are),",
                    "कुझ (at all) असीं (we) वी (too) तैनूं (unto Thee) प्यारे (beloved) हां (are), कि (or) मैं (I) ऐवें (in vain) घोल (consecrated) घुमाई (wander) ।",
                    "मैं विच मैं ना रह गई राई, जब की पिया संग पीत लगाई ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा शौह! मैं तुझ पर वारी, मुख देखने के वणजारे हम,",
                    "क्या हम भी तुझको प्यारे हैं, या व्यर्थ ही बलिहारी जाई ?",
                    "मुझमें 'मैं' न रही रत्ती-भर, जब से पिया संग प्रीत लगाई !"
                ],
                "poetic_english": [
                    "Bulleh is sacrificed to Thee, eager to trade for Thy sweet glance;",
                    "Am I too dear unto Thy heart, or do I waste this longing dance?",
                    "Not an iota of 'I' remained in me, since with my Lover I pledged to be!"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी कबीर के दोहे 'जब मैं था तब हरि नहीं, अब हरि हैं मैं नाहिं' का पूर्ण भाष्य है। 'गूंगे का गुड़' आध्यात्मिक आनंद की अनिर्वचनीयता को सिद्ध करता है। जब साधक 'वहदत' (अद्वैत) और 'हैरत' (परम विस्मय) के स्तर पर पहुंचता है, तो जीवन, जन्म और मरण सब विलीन हो जाते हैं। बंद 9 में 'दर दसवें' (दसम द्वार / ब्रह्मरंध्र) पर पहुँचकर आत्मा परमात्मा से अपने प्रेम की स्वीकृति मांगती है।"
    }
]

new_lexicon_terms = {
    "गूंगे दा गुड़": {"hindi": "अनिर्वचनीय आध्यात्मिक आनंद जिसे वाणी से व्यक्त नहीं किया जा सकता", "english": "sweetness tasted by a mute; ineffable mystical bliss"},
    "हैरत": {"hindi": "परम विस्मय, आश्चर्य, आध्यात्मिक अवाक-अवस्था", "english": "mystic awe, divine bewilderment/wonder (hayrat)"},
    "पीरेमुग़ां": {"hindi": "मदिरालय का स्वामी; सूफी रूपक में: पूर्ण सद्गुरु/मुर्शिद", "english": "Pir-e-Mughan, master of the tavern/spiritual elder"},
    "हुजरा": {"hindi": "एकांत साधना-कक्ष, कुटीर", "english": "solitary meditation cell, cloister"},
    "मायल": {"hindi": "कृपालु, प्रवृत्त, रीझा हुआ", "english": "inclined with favor, gracious"},
    "मुजरा": {"hindi": "समर्पण, वंदना, हाज़िरी, प्रणाम", "english": "salutation, devotion, formal homage"},
    "घोल घुमाई": {"hindi": "सर्वस्व न्योछावर करना, बलिहारी जाना", "english": "sacrificing oneself completely, devoted dedication"},
    "वणजारे": {"hindi": "व्यापारी, पिपासु साधक", "english": "traders, seekers of spiritual merchandise"}
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
        "completed_count": 95,
        "total": 160,
        "next_kafi_id": 96,
        "last_updated": "2026-10-17T17:55:00+05:30",
        "last_batch": "91-95",
        "status": "in_progress"
    }
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print(f"Checkpoint updated: 95/160 completed. Next ID: 96")

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
