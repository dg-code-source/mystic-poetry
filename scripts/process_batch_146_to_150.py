"""
Process Batch 146 to 150 of Bulleh Shah's Kafian.
Kafi 146: टुक्क बूझ कौन छुप आया ए (Decipher Who Has Come in Disguise!)
Kafi 147: तुसीं आओ मिल मेरी प्यारी (Come Meet Me, O My Beloved Companion)
Kafi 148: तुसीं करो असाडी कारी (Come Find a Cure for My Ailment!)
Kafi 149: उलटे होर ज़माने आए (Inverted Times Have Arrived)
Kafi 150: उलटी गंग बहाइओ रे साधो, तब हर दरसन पाए (Make the Ganges Flow in Reverse, O Seekers!)
"""

import json
import os

DATA_DIR = os.path.abspath("c:/my-code/Bulleh-Shah/data")
KAFIAN_DIR = os.path.join(DATA_DIR, "kafian")
LEXICON_PATH = os.path.join(DATA_DIR, "punjabi_sufi_lexicon.json")
CHECKPOINT_PATH = os.path.join(DATA_DIR, "checkpoint.json")

batch_kafian = [
    {
        "id": 146,
        "title_punjabi": "टुक्क बूझ कौन छुप आया ए",
        "title_english": "Decipher Who Has Come in Disguise!",
        "raga": "Raga Kafi / Bhairavi",
        "meter": "Matrik Chhand (16-12 matras)",
        "theme": "The Cosmic Masquerade of the Divine across Forms, Faiths, and the Dot of Duality",
        "historical_context": "One of Bulleh Shah's most intellectually rigorous and mystical compositions. Bulleh challenges the religious establishment by declaring that God plays a cosmic game of hide-and-seek behind the masks of human beings ('भेखी भेख वटाइआ'). He explains the four stages of Sufism (Shariat as wet-nurse, Tariqat as mother, Haqiqat as reality, and Marifat as direct gnosis), and solves the theological mystery using the Perso-Arabic alphabet: the only difference between Ghayn (غ, the veiled/other) and Ayn (ع, the Pure Essence) is a single dot (nuqta)—the dot of egoic illusion.",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "टुक्क बूझ कौन छुप आया ए ।  ",
                    "किसे भेखी भेख वटाइआ ए ।"
                ],
                "hindi_gloss": "टुक्क (जरा/तनिक) बूझ (बूझ/पहचान तो सही) कौन (कौन) छुप आया ए (छिपकर आया है)? किसे (किसी) भेखी (बहुरूपिए ने) भेख (अपना वेश) वटाइआ ए (बदल लिया है)।",
                "english_gloss": "टुक्क (Just a little) बूझ (discern and decipher) कौन (who) छुप आया ए (has arrived in hiding)? किसे (Some) भेखी (master of disguises) भेख वटाइआ ए (has changed his costume).",
                "poetic_hindi": "तनिक बूझ, कौन छुप आया है?\nकिस बहुरूपिए ने वेश बदलाया है!",
                "poetic_english": "Discern, who walks here in disguise?\nSome cosmic actor before our eyes!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "जिस ना दरद की बात कही, उस प्रेम नगर ना झात पई,  ",
                    "उह डुब्ब मोई सभ घात गई, उह क्युं चन्दरी ने जाइआ ए ।  ",
                    "टुक्क बूझ कौन छुप आया ए ।"
                ],
                "hindi_gloss": "जिस (जिसने) ना (नहीं) दरद (प्रेम-पीड़ा) की बात कही (बात कही/अनुभव की), उस (उसकी) प्रेम नगर (प्रेम-नगर में) ना झात पई (झांकी तक न पड़ी), उह (वह) डुब्ब मोई (डूब मरी) सभ घात गई (उसका समस्त अवसर नष्ट हो गया), उह (उसे) क्युं (क्यों) चन्दरी ने (अभागिन माँ ने) जाइआ ए (जन्म दिया?)।",
                "english_gloss": "जिस ना दरद की बात कही (He who never spoke of Love's ache), उस प्रेम नगर ना झात पई (never caught a glimpse of Love's city), उह डुब्ब मोई (she drowned and perished) सभ घात गई (all spiritual opportunity was squandered), उह क्युं चन्दरी ने जाइआ ए (why did that wretched mother ever give him birth?).",
                "poetic_hindi": "जिसने न प्रेम-पीड़ा पाई, प्रेम-नगर की झाँकी न पाई;\nअवसर खोया, डूब पराई, जननी ने काहे जनमाया?\nतनिक बूझ, कौन छुप आया है?",
                "poetic_english": "Who never spoke of love's deep pain, saw not Love's city across the plain;\nAll chances lost, in waters slain—why was he born of womb in vain?\nDiscern, who walks here in disguise?"
            },
            {
                "stanza_number": 3,
                "original": [
                    "मानन्द पलास बणाइओ ई मेरी सूरत चा लिखाइओ ई,  ",
                    "मुक्ख काला कर दिखलाइओ ई क्या स्याही रंग लगाइआ ए ।  ",
                    "टुक्क बूझ कौन छुप आया ए ।"
                ],
                "hindi_gloss": "मानन्द (समान) पलास (पलाश/ढाक के लाल-पीले पुष्प या खुरदरे वृक्ष के) बणाइओ ई (तूने बनाया), मेरी (मेरी) सूरत (रूप-रेखा) चा (उठाकर) लिखाइओ ई (चित्रित की), मुक्ख (मुख को) काला (अज्ञान और विरह के रंग से काला) कर (करके) दिखलाइओ ई (दिखलाया), क्या (कैसा विचित्र) स्याही (कालिमा/स्याही का) रंग लगाइआ ए (तूने रंग लगाया है)।",
                "english_gloss": "मानन्द पलास (Like a palas tree) बणाइओ ई (Thou fashioned me), मेरी सूरत (my countenance) चा लिखाइओ ई (Thou sketched out), मुक्ख काला कर दिखलाइओ ई (displaying my face darkened with sorrow), क्या स्याही रंग लगाइआ ए (what a strange ink-black color Thou hast applied).",
                "poetic_hindi": "पलाश-समान मुझे रचाया, सूरत का चित्र बनाया,\nमुख काला कर मुझे दिखाया, क्या स्याह रंग लगाया!\nतनिक बूझ, कौन छुप आया है?",
                "poetic_english": "Like coarse palas Thou made my clay, and sketched my form along the way;\nWith blackened face Thou didst portray—what ink Thou chose for this display!\nDiscern, who walks here in disguise?"
            },
            {
                "stanza_number": 4,
                "original": [
                    "इक रब्ब दा नां ख़ज़ाना ए संग चोरां यारां दाना ए,  ",
                    "उस रहमत दा खसमाना ए संग ख़ौफ रकीब बणाइआ ए ।  ",
                    "टुक्क बूझ कौन छुप आया ए ।"
                ],
                "hindi_gloss": "इक (एक) रब्ब दा (परमात्मा का) नां (नाम ही) ख़ज़ाना ए (सच्चा खजाना है), संग (किंतु साथ ही) चोरां (चोरों) यारां (मित्रों का) दाना ए (दांव/चाल है), उस (उसकी) रहमत (कृपा) दा (का) खसमाना ए (संरक्षण और प्रभुत्व है), संग (साथ में) ख़ौफ (भय रूपी) रकीब (शत्रु/प्रतिद्वंद्वी) बणाइआ ए (खड़ा किया है)।",
                "english_gloss": "इक रब्ब दा नां (God's holy Name alone) ख़ज़ाना ए (is the true treasure), संग चोरां यारां दाना ए (yet thieves and companions lay their traps), उस रहमत दा खसमाना ए (His mercy remains our sole master/shelter), संग ख़ौफ रकीब बणाइआ ए (while dread is made our rivaling foe).",
                "poetic_hindi": "प्रभु-नाम का खजाना भारी, चोर-सखा संग घात पसारी,\nरहमत की प्रभुताई न्यारी, भय को दुश्मन रूप सजाया!\nतनिक बूझ, कौन छुप आया है?",
                "poetic_english": "The Name of God is treasure true, though thieves and friends conspire anew;\nHis mercy reigns as sovereign due, while fear is made a rival too!\nDiscern, who walks here in disguise?"
            },
            {
                "stanza_number": 5,
                "original": [
                    "दूई दूर करो कोई शोर नहीं, इह तुरक हिन्दू कोई होर नहीं,  ",
                    "सभ साध कहो कोई चोर नहीं, हर घट विच आप समाइआ ए ।  ",
                    "टुक्क बूझ कौन छुप आया ए ।"
                ],
                "hindi_gloss": "दूई (द्वैतभाव को) दूर करो (हृदय से निकाल दो), कोई शोर नहीं (सांप्रदायिक झगड़े का कोई औचित्य नहीं), इह (यह) तुरक (मुसलमान) हिन्दू (और हिन्दू) कोई होर नहीं (कोई भिन्न नहीं हैं), सभ (सबको) साध (सज्जन/साधु) कहो (मानो), कोई (कोई भी) चोर नहीं (चोर या पापी नहीं), हर घट विच (प्रत्येक हृदय के भीतर) आप (वह परमात्मा स्वयं) समाइआ ए (विराजमान है)।",
                "english_gloss": "दूई दूर करो (Cast away duality) कोई शोर नहीं (let there be no partisan clamor), इह तुरक हिन्दू (this Turk/Muslim and Hindu) कोई होर नहीं (are not separate at all), सभ साध कहो (deem all to be holy saints) कोई चोर नहीं (none is a thief), हर घट विच (within every heart) आप समाइआ ए (He Himself indwells).",
                "poetic_hindi": "द्वैत मिटाओ, शोर न होवे, तुर्क-हिन्दू में भेद न जोवे;\nसब साधु हैं, चोर न कोई, हर घट में वो आप समाया!\nतनिक बूझ, कौन छुप आया है?",
                "poetic_english": "Cast out duality's noisy strain; Turk and Hindu are one in grain;\nCall all souls saints, none thieves remain; in every heart He holds His reign!\nDiscern, who walks here in disguise?"
            },
            {
                "stanza_number": 6,
                "original": [
                    "ऐवें किस्से काहनूं घड़ना एं, ते गुलसतां, बोसतां पढ़ना एं,  ",
                    "ऐवें बेमूज़ब क्युं लड़ना एं, किस उलटा वेद पढ़ाइआ ए ।  ",
                    "टुक्क बूझ कौन छुप आया ए ।"
                ],
                "hindi_gloss": "ऐवें (व्यर्थ ही) किस्से (काल्पनिक किस्से) काहनूं (किसलिए) घड़ना एं (गढ़ता है?), ते (और) गुलसतां बोसतां (शेख सादी की गुलिस्तां व बोस्तां जैसी पुस्तकें) पढ़ना एं (रटता फिरता है?), ऐवें (यूँ ही) बेमूज़ब (बिना किसी कारण के) क्युं लड़ना एं (क्यों आपस में लड़ता है?), किस (तुझे किसने) उलटा (विकृत/विपरीत) वेद (ज्ञान/शास्त्र) पढ़ाइआ ए (सिखा दिया है?)।",
                "english_gloss": "ऐवें किस्से काहनूं घड़ना एं (Why fabricate idle tales in vain?), ते गुलसतां बोसतां पढ़ना एं (and pore over Gulistan and Bostan?), ऐवें बेमूज़ब क्युं लड़ना एं (why wage battle without any cause?), किस उलटा वेद पढ़ाइआ ए (who taught thee such inverted scriptures?).",
                "poetic_hindi": "क्यों किस्से व्यर्थ गढ़ता जाए? 'गुलिस्ताँ-बोस्ताँ' रट खाए?\nबिना सबब क्यों युद्ध मचाए? किसने उलटा वेद पढ़ाया?\nतनिक बूझ, कौन छुप आया है?",
                "poetic_english": "Why forge vain tales in empty pride, or memorise 'Gulistan' inside?\nWhy fight where no true causes hide? Who turned the sacred text aside?\nDiscern, who walks here in disguise?"
            },
            {
                "stanza_number": 7,
                "original": [
                    "शरियत साडी दाई ए तरीकत साडी माई ए,  ",
                    "अग्गों हक्क हकीकत आई ए अते मारफतों कुझ पाइआ ए ।  ",
                    "टुक्क बूझ कौन छुप आया ए ।"
                ],
                "hindi_gloss": "शरियत (शरिया/बाह्य धर्म-नियम) साडी (हमारी) दाई ए (धाय/दाई माँ के समान है जो केवल बाल्यावस्था में संभालती है), तरीकत (तरीकत/आध्यात्मिक साधना-पथ) साडी (हमारी) माई ए (सच्ची जन्मदात्री माँ है), अग्गों (इसके आगे चलकर) हक्क हकीकत (परम सत्य 'हकीकत') आई ए (प्रकट होती है), अते (और) मारफतों (मारिफत/आत्म-साक्षात्कार से) कुझ पाइआ ए (परम पद की प्राप्ति होती है)।",
                "english_gloss": "शरियत (Shariat / sacred law) साडी दाई ए (is our nursemaid), तरीकत (Tariqat / mystical discipline) साडी माई ए (is our true mother), अग्गों (further ahead) हक्क हकीकत (Truth / Ultimate Reality) आई ए (arrives), अते मारफतों (and through Marifat / direct gnosis) कुझ पाइआ ए (the supreme prize is attained).",
                "poetic_hindi": "शरियत दाई, तरीकत माई, हकीकत आगे दरस दिखाई;\nमारिफत से निधि हमने पाई, सत्य का पावन दीप जलाया!\nतनिक बूझ, कौन छुप आया है?",
                "poetic_english": "Shariat's our nurse, Tariqat our mother dear; Haqiqat's Truth shines pure and clear;\nIn Marifat gnosis draws near—the soul has found its home sincere!\nDiscern, who walks here in disguise?"
            },
            {
                "stanza_number": 8,
                "original": [
                    "है विरली बात बतावन दी, तुसीं समझो दिल ते लावन दी,  ",
                    "कोई गत्त दस्सो इस बावन दी, इह काहनूं भेत बणाइआ ए ।  ",
                    "टुक्क बूझ कौन छुप आया ए ।"
                ],
                "hindi_gloss": "है विरली (अत्यंत दुर्लभ/गुप्त) बात (बात है) बतावन दी (बताने योग्य), तुसीं (तुम सब) समझो (समझो और) दिल ते लावन दी (हृदय में धारण करने योग्य), कोई (कोई विवेकी) गत्त (रहस्य/मर्म) दस्सो (बताओ) इस बावन (बावन अक्षरों की वर्णमाला) दी (का), इह (यह) काहनूं (किसलिए) भेत (गूढ़ भेद) बणाइआ ए (रचा गया है)।",
                "english_gloss": "है विरली बात (Rare and subtle is this truth) बतावन दी (to declare), तुसीं समझो दिल ते लावन दी (worthy of grasping and holding to heart), कोई गत्त दस्सो (let someone reveal the essence) इस बावन दी (of these fifty-two sacred letters), इह काहनूं भेत बणाइआ ए (why this profound riddle was created).",
                "poetic_hindi": "विरली बात है कहने वाली, समझो दिल पे धरने वाली;\nबावन अक्षरों का मर्म बताओ, क्यों ये भेद रचाया?\nतनिक बूझ, कौन छुप आया है?",
                "poetic_english": "A wondrous truth, subtle and rare; take it to heart with loving care;\nReveal the fifty-two letters' air—why was this mystery hidden there?\nDiscern, who walks here in disguise?"
            },
            {
                "stanza_number": 9,
                "original": [
                    "इह पढ़ना इलम ज़रूर होया, पर दसना ना मंज़ूर होया,  ",
                    "जिस दस्या सो मनसूर होया, इस सूली पकड़ चढ़ाइआ ए ।  ",
                    "टुक्क बूझ कौन छुप आया ए ।"
                ],
                "hindi_gloss": "इह (यह) पढ़ना (पढ़ना/जानना) इलम (रहस्य-ज्ञान) ज़रूर होया (अति आवश्यक तो हुआ), पर (किंतु) दसना (संसार को प्रकट रूप से बताना) ना मंज़ूर होया (स्वीकार्य नहीं रहा), जिस (जिसने भी यह) दस्या (रहस्य खोला) सो (वह) मनसूर होया (मंसूर अल-हल्लाज बन गया), इस (इस संसार ने उसे) सूली पकड़ चढ़ाइआ ए (पकड़कर सूली पर चढ़ा दिया)।",
                "english_gloss": "इह पढ़ना इलम (To master this divine gnosis) ज़रूर होया (became mandatory), पर दसना ना मंज़ूर होया (yet uttering it openly was forbidden), जिस दस्या (whosoever revealed it) सो मनसूर होया (became like Mansur Hallaj), इस सूली पकड़ चढ़ाइआ ए (and was seized and mounted upon the gallows).",
                "poetic_hindi": "इल्म ये पढ़ना लाजिम हुआ, पर जग को बताना मना हुआ;\nजिसने कहा वो मंसूर हुआ, सूली पे पकड़ चढ़ाया!\nतनिक बूझ, कौन छुप आया है?",
                "poetic_english": "This gnosis must be learned indeed, yet speaking it no law decreed;\nWho spoke it like Mansur did bleed, hanged on the gallows for his creed!\nDiscern, who walks here in disguise?"
            },
            {
                "stanza_number": 10,
                "original": [
                    "मैनूं किसब ना फिकर तमीज़ कीता, दुख तन आरफ बाज़ीद कीता,  ",
                    "कर ज़ुहद किताब मजीद कीता, किसे बे-मेहनत नहीं पाइआ ए ।  ",
                    "टुक्क बूझ कौन छुप आया ए ।"
                ],
                "hindi_gloss": "मैनूं (मुझमें) किसब (न कोई कौशल) ना फिकर (न विचार) तमीज़ (न बुद्धि का विवेक) कीता, दुख (कठिन तपस्या के कष्ट ने) तन (शरीर को) आरफ (आरिफ/सिद्ध ज्ञानी) बाज़ीद (बायज़ीद बुस्तामी के समान) कीता, कर (करके) ज़ुहद (घोर तपस्या) किताब मजीद कीता (कुरान मजीद का जीवंत रूप बना दिया), किसे (किसी ने भी) बे-मेहनत (बिना कठोर साधना के) नहीं पाइआ ए (परम पद को नहीं पाया)।",
                "english_gloss": "मैनूं किसब ना फिकर तमीज़ कीता (Neither craft nor worldly wit made me pure), दुख तन (corporal suffering and austerity) आरफ बाज़ीद कीता (forged me like the mystic Bayazid), कर ज़ुहद (through rigorous penance) किताब मजीद कीता (realized the Holy Book within), किसे बे-मेहनत नहीं पाइआ ए (none ever attained without toil).",
                "poetic_hindi": "न हुनर, न बुद्धि काम आई, तन-पीड़ा ने बायेज़ीद बनाई;\nतप से कुरान की ज्योति जगाई, बिना परिश्रम कोई न पाया!\nतनिक बूझ, कौन छुप आया है?",
                "poetic_english": "No worldly craft my senses feed; pain made me like saint Bayazid;\nThrough holy zeal the Book I freed; none wins this prize without toil in deed!\nDiscern, who walks here in disguise?"
            },
            {
                "stanza_number": 11,
                "original": [
                    "इस दुक्ख से किचरक भागेंगा, रहें सुत्ता कद तूं जागेंगा,  ",
                    "फेर उठदा रोवन लागेंगा, किसे ग़फ़लत मार सुलाइआ ए ।  ",
                    "टुक्क बूझ कौन छुप आया ए ।"
                ],
                "hindi_gloss": "इस (इस साधना के) दुक्ख से (कष्ट से) किचरक (कब तक) भागेंगा (भागता फिरेगा?), रहें सुत्ता (सोया ही रहता है) कद तूं जागेंगा (तू कब जागेगा?), फेर (फिर अंत समय) उठदा (उठते ही) रोवन लागेंगा (रोने लगेगा), किसे (कैसी भीषण) ग़फ़लत (लापरवाही/अज्ञान ने) मार सुलाइआ ए (तुझे बेहोश सुला रखा है)।",
                "english_gloss": "इस दुक्ख से (From this purifying grief) किचरक भागेंगा (how long wilt thou flee?), रहें सुत्ता (thou remainest asleep) कद तूं जागेंगा (when wilt thou awake?), फेर उठदा रोवन लागेंगा (then rising on that day thou wilt weep), किसे ग़फ़लत (what slumber of heedlessness) मार सुलाइआ ए (has struck thee down in sleep).",
                "poetic_hindi": "कब तक भागेगा इस दुःख से? सोया है, जागेगा कब रे?\nउठकर अंत में रोएगा रे, कैसी ग़फ़लत ने सुलाया!\nतनिक बूझ, कौन छुप आया है?",
                "poetic_english": "How long will you flee this sorrow's grace? When will you wake to run the race?\nYou'll weep when death stares in your face—what heedless sleep holds your embrace?\nDiscern, who walks here in disguise?"
            },
            {
                "stanza_number": 12,
                "original": [
                    "ग़ैन ऐन दी सूरत इक ठहरा, इक नुकते दा है फरक पड़ा,  ",
                    "जो नुकता दिल थीं दूर करा, फिर ग़ैन वा ऐन जिताइआ ए ।  ",
                    "टुक्क बूझ कौन छुप आया ए ।"
                ],
                "hindi_gloss": "ग़ैन (अरबी अक्षर 'गैन' غ) ऐन (और 'ऐन' ع) दी (की) सूरत (मूल आकृति) इक ठहरा (एक ही समान है), इक (केवल एक) नुकते (बिंदु/नुकते) दा (का) है फरक पड़ा (अंतर पड़ता है), जो (जब उस) नुकता (अहंकार रूपी नुकते को) दिल थीं (हृदय से) दूर करा (हटा दिया जाता है), फिर (तब) ग़ैन वा ऐन (गैन ही ऐन रूप सत्य) जिताइआ ए (प्रत्यक्ष सिद्ध हो जाता है)।",
                "english_gloss": "ग़ैन ऐन दी सूरत (The shapes of Ghayn [غ] and Ayn [ع]) इक ठहरा (are identical in form), इक नुकते दा (of a single dot alone) है फरक पड़ा (is the only difference), जो नुकता (when that dot of ego) दिल थीं दूर करा (is erased from the heart), फिर ग़ैन वा ऐन जिताइआ ए (then Ghayn is revealed as the very Ayn of Reality).",
                "poetic_hindi": "'गैन' और 'ऐन' की मूरत एक, इक नुक्ते का बस भेद देख;\nहृदय से नुक्ता मिटे जो एक, गैन ही ऐन प्रगटाया!\nतनिक बूझ, कौन छुप आया है?",
                "poetic_english": "Ghayn and Ayn share one design; a single dot makes the dividing line;\nErase that dot within your shrine, and Ghayn turns into Ayn divine!\nDiscern, who walks here in disguise?"
            },
            {
                "stanza_number": 13,
                "original": [
                    "जेहड़ा मन विच लग्गा दूआ रे, इह कौन कहे मैं मूआ रे,  ",
                    "तन सभ इनायत हूआ रे, फिर बुल्ल्हा नाम धराइआ ए ।  ",
                    "टुक्क बूझ कौन छुप आया ए ।  ",
                    "किसे भेखी भेख वटाइआ ए ।"
                ],
                "hindi_gloss": "जेहड़ा (जो) मन विच (मन के भीतर) लग्गा (लगा हुआ था) दूआ (द्वैत/दूसरापन) रे (रे भाई!), इह (अब यह) कौन कहे (कौन कह सकता है कि) मैं मूआ रे (मैं मर गया या मिट गया?), तन (यह सम्पूर्ण शरीर) सभ (सबका सब) इनायत हूआ रे (मुर्शिद शाह इनायत का स्वरूप बन गया), फिर (और फिर उसी ने) बुल्ल्हा (बुल्लेशाह) नाम धराइआ ए (नाम धारण कर लिया है)।",
                "english_gloss": "जेहड़ा मन विच लग्गा दूआ रे (The duality that clung to the mind), इह कौन कहे (who can say now) मैं मूआ रे ('I have died'?), तन सभ (this whole body) इनायत हूआ रे (has become Inayat Himself!), फिर बुल्ल्हा नाम धराइआ ए (and then assumed the name of Bulleh!).",
                "poetic_hindi": "मन का जब दूजापन मिट जाए, कौन कहे कि मैं मर पाए?\nतन सब इनायत रूप कहाए, फिर 'बुल्ल्हा' नाम धराया!\nतनिक बूझ, कौन छुप आया है?\nकिस बहुरूपिए ने वेश बदलाया है!",
                "poetic_english": "When duality's ghost departs from head, who can assert that 'I am dead'?\nThis body becomes Inayat instead, and 'Bulleh' is the name He read!\nDiscern, who walks here in disguise?\nSome cosmic actor before our eyes!"
            }
        ],
        "sufi_commentary": "Kafi 146 is an extraordinary masterpiece of philosophical Sufism (Tasawwuf) and semiotics. Bulleh opens with the cosmic riddle of the Divine Masquerade: the Absolute is a Supreme Actor ('भेखी') who changes costumes across history, religions, and bodies. In Stanza 5, Bulleh makes his immortal declaration of non-duality across creeds: 'इह तुरक हिन्दू कोई होर नहीं, सभ साध कहो कोई चोर नहीं, हर घट विच आप समाइआ ए'—annihilating sectarian bigotry by asserting that the Divine Indweller operates through all forms equally. In Stanza 7, he delineates the four classical stations of the mystical path: Shariat (the wet-nurse that feeds the spiritual infant with moral laws), Tariqat (the true mother that births spiritual maturity), Haqiqat (the unveiling of Essential Truth), and Marifat (unitive gnosis). In Stanza 12, Bulleh achieves one of the most brilliant graphical metaphors in world literature: in the Arabic script, the letter Ayn (ع, representing the Divine Essence, the Eye of Truth) and Ghayn (غ, representing the Ghayr / the Other, the veil of duality) share the exact same skeletal form; they differ solely by a single diacritical dot (nuqta). That dot is the Nafs—the phantom ego. The moment this dot of selfhood is removed from the heart ('जो नुकता दिल थीं दूर करा'), the 'other' (Ghayn) dissolves into the Supreme Essence (Ayn). Finally, Bulleh realizes that his individuality was an illusion: his entire being has become Murshid Shah Inayat ('तन सभ इनायत हूआ रे'), who playfully calls Himself 'Bulleh'."
    },
    {
        "id": 147,
        "title_punjabi": "तुसीं आओ मिल मेरी प्यारी",
        "title_english": "Come Meet Me, O My Beloved Companion",
        "raga": "Raga Tilang / Kafi",
        "meter": "Baint / Matrik (16-12 matras)",
        "theme": "The Bridal Departure (Rukhsati) as the Allegory of the Soul's Death and Final Journey",
        "historical_context": "Rooted in the poignant Punjabi bridal departure ceremony ('Rukhsati' / 'Doli torni'), where aunts, maternal relatives, and childhood companions gather to bid a tearful farewell to the weeping bride as she leaves her paternal home (Peyke) for the in-laws' eternal realm (Sohre). Bulleh Shah uses this deeply emotional folk tradition as an allegory for death: the physical world is the paternal home, the funeral procession is the bridal departure, and the grave is the bridal bed where she meets the Divine Spouse.",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "तुसीं आओ मिल मेरी प्यारी ।  ",
                    "मेरे टुरने दी होई त्यारी ।"
                ],
                "hindi_gloss": "तुसीं (तुम सब) आओ मिल (आकर गले मिल लो) मेरी प्यारी (मेरी प्यारी सखियों!), मेरे (मेरे) टुरने दी (संसार से प्रस्थान करने की) होई (हो चुकी है) त्यारी (तैयारी)।",
                "english_gloss": "तुसीं आओ मिल (Come gather and embrace me) मेरी प्यारी (O my beloved friends!), मेरे टुरने दी (for my departure hence) होई त्यारी (all preparation is complete).",
                "poetic_hindi": "आओ मिल लो सखियो प्यारी,\nमेरे चलने की हुई तैयारी!",
                "poetic_english": "Come embrace me, sisters dear;\nMy time to leave this world is near!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "सभ्भे रल के टोरन आईआं, आईआं फुफ्फियां चाचियां ताईआं,  ",
                    "सभ्भे रोंदियां ज़ारो ज़ारी, मेरे टुरने दी होई त्यारी ।"
                ],
                "hindi_gloss": "सभ्भे (सभी) रल के (मिलकर) टोरन आईआं (विदा करने आई हैं), आईआं (आई हैं) फुफ्फियां (बुआएं) चाचियां (चाचियां) ताईआं (ताईयां), सभ्भे (सभी) रोंदियां (रो रही हैं) ज़ारो ज़ारी (फूट-फूट कर), मेरे टुरने दी होई त्यारी ।",
                "english_gloss": "सभ्भे रल के (All together) टोरन आईआं (have come to send me off), आईआं फुफ्फियां (paternal aunts have come) चाचियां ताईआं (elder and younger aunts), सभ्भे रोंदियां (all weeping bitterly) ज़ारो ज़ारी (with streaming tears), मेरे टुरने दी होई त्यारी ।",
                "poetic_hindi": "मिल-जुल कर सब विदा कराएं, बुआ-चाची-ताई आएँ,\nरोतीं सब जारो-जारी, मेरे चलने की हुई तैयारी!",
                "poetic_english": "Aunts and kinfolk gather round, weeping with sorrowful sound;\nTears of grief fall to the ground; to that far shore my ship is bound!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "सभ्भे आखन इह गल्ल जाणी, रव्हीं तूं हर दम हो निमाणी,  ",
                    "ताहीं लग्गेगीं ओथे प्यारी, मेरे टुरने दी होई त्यारी ।"
                ],
                "hindi_gloss": "सभ्भे (सभी स्त्रियाँ) आखन (कहती हैं) इह गल्ल जाणी (यह सीख गाँठ बांध ले), रव्हीं (रहना) तूं (तू) हर दम (सदा) हो निमाणी (अहंकार-रहित, अत्यंत विनीत व नम्र), ताहीं (तभी) लग्गेगीं (लगेगी) ओथे (उस ससुराल/परलोक में) प्यारी (प्रियतम को प्यारी), मेरे टुरने दी होई त्यारी ।",
                "english_gloss": "सभ्भे आखन (All counsel me) इह गल्ल जाणी (heed this essential truth): रव्हीं तूं हर दम (remain ever) हो निमाणी (utterly humble and meek), ताहीं लग्गेगीं ओथे प्यारी (then alone wilt thou be beloved there in that realm), मेरे टुरने दी होई त्यारी ।",
                "poetic_hindi": "सबकी सीख यही कल्याणी: 'रहना तू हरदम अभिमानी-हीन, निमानी';\nतभी लगेगी पिया को प्यारी, मेरे चलने की हुई तैयारी!",
                "poetic_english": "One counsel all my elders speak: 'Abide forever humble and meek;\nThen the Beloved's love you'll seek!' My soul departs this earthly creek!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "सभ्भे टोर घरां नूं मुड़ियां, मैं हो इक इकल्लड़ी टुरियां,  ",
                    "होईआं डारों मैं कूंज न्यारी, मेरे टुरने दी होई त्यारी ।"
                ],
                "hindi_gloss": "सभ्भे (सभी) टोर (विदा करके) घरां नूं (अपने-अपने घरों को) मुड़ियां (लौट गईं), मैं (मैं) हो (होकर) इक इकल्लड़ी (सर्वथा अकेली/एकाकिनी) टुरियां (चल पड़ी), होईआं (हो गई हूँ) डारों (सारस/कुररी पक्षियों के झुंड से) मैं (मैं) कूंज (कूंज पक्षी की भाँति) न्यारी (अलग-थलग), मेरे टुरने दी होई त्यारी ।",
                "english_gloss": "सभ्भे टोर (Having seen me off, all) घरां नूं मुड़ियां (returned to their own homes), मैं हो इक इकल्लड़ी (I, all solitary and alone) टुरियां (departed on the long road), होईआं डारों (from the flock) मैं कूंज न्यारी (like a lonely crane separated from her flock), मेरे टुरने दी होई त्यारी ।",
                "poetic_hindi": "विदा करा सब घर को मुड़ीं, अकेली उस रस्ते पे मुड़ी;\nझुंड से जैसे कूँज बिछुड़ी, मेरे चलने की हुई तैयारी!",
                "poetic_english": "All turn back home, their duties done; I walk the lonely road alone;\nLike a stray crane whose flock has flown; my departure bell is blown!"
            },
            {
                "stanza_number": 5,
                "original": [
                    "बुल्ल्हा शहु मेरे घर आवे, मैं कुचज्जी नूं लै गल लावे,  ",
                    "इको शौह दी ए बात प्यारी, मेरे टुरने दी होई त्यारी ।  ",
                    "तुसीं आओ मिल मेरी प्यारी ।  ",
                    "मेरे टुरने दी होई त्यारी ।"
                ],
                "hindi_gloss": "बुल्ल्हा (बुल्लेशाह कहता है) शहु (प्रभु-प्रियतम) मेरे घर आवे (मेरे द्वार आ जाए), मैं (मुझ) कुचज्जी नूं (गुणहीन/फूहड़ दासी को) लै (लेकर) गल लावे (कंठ से लगा ले), इको (एकमात्र) शौह दी (प्रभु की ही) ए बात प्यारी (यह कृपा सबसे प्यारी है), मेरे टुरने दी होई त्यारी ।",
                "english_gloss": "बुल्ल्हा शहु (Bulleh's King!) मेरे घर आवे (if He visits my courtyard), मैं कुचज्जी नूं (and takes uncultured, flawed me) लै गल लावे (into His divine embrace), इको शौह दी ए बात प्यारी (this alone is the Master's sweetest grace), मेरे टुरने दी होई त्यारी ।",
                "poetic_hindi": "बुल्ल्हा कहे, शाह घर आए, मुझ कुचज्जी को कंठ लगाए;\nएक पिया की बात सुहाए, मेरे चलने की हुई तैयारी!\nआओ मिल लो सखियो प्यारी, मेरे चलने की हुई तैयारी!",
                "poetic_english": "Bulleh says: if the King draw near, and hold this clumsy servant dear;\nHis love alone dispels my fear; my hour of marching has appeared!\nCome embrace me, sisters dear;\nMy time to leave this world is near!"
            }
        ],
        "sufi_commentary": "Kafi 147 is a deeply moving bridal-departure lament that doubles as a sublime meditation on death and the soul's solitary voyage. In the folk culture of Punjab, the departure of the bride in her palanquin (doli) is one of the most heart-wrenching rituals. Relatives weep ('सभ्भे रोंदियां ज़ारो ज़ारी'), but once the procession passes the village boundary, every relative returns home ('सभ्भे टोर घरां नूं मुड़ियां'). Bulleh connects this directly to the graveyard: friends and relatives accompany the bier, weep at the graveside, and then return to their daily routines, leaving the soul completely alone ('मैं हो इक इकल्लड़ी टुरियां'). Like a migratory crane (koonj) separated from its flying wedge ('डारों मैं कूंज न्यारी'), the soul must face the ultimate journey alone. What saves the soul in this terrifying isolation? Not ritual pride or intellectual learning, but radical humility ('रव्हीं तूं हर दम हो निमाणी') and the unmerited grace of the Beloved, who embraces the flawed soul ('कुचज्जी') and redeems her forever."
    },
    {
        "id": 148,
        "title_punjabi": "तुसीं करो असाडी कारी",
        "title_english": "Come Find a Cure for My Ailment!",
        "raga": "Raga Dhanasri / Asa",
        "meter": "Baint / Davayya (16-12 matras)",
        "theme": "The Incurable Wound of Ishq, Krishna's Flute, and the Terror of the Love-Storm",
        "historical_context": "A passionate 10-stanza prayer where Bulleh Shah depicts the agony of divine love as an acute medical crisis that defies all earthly physicians, herbs, and potions ('की कोई वैद पसारी'). He weaves together pastoral imagery of Krishna playing his enchanting flute ('इह जो मुरली कान्ह वजाई'), the terror of a goat at the butcher's stall ('हां मैं बक्करी कोल कसाईआं'), and the solitary bamboo reed torn from its roots crying for its maker.",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "तुसीं करो असाडी कारी ।  ",
                    "केही हो गई वेदन भारी ।"
                ],
                "hindi_gloss": "तुसीं (तुम सब) करो (करो) असाडी (मेरी) कारी (उपाय/इलाज/चिकित्सा)। केही (कैसी विचित्र और असह्य) हो गई (हो चुकी है) वेदन (विरह-वेदना) भारी (अत्यंत भारी)।",
                "english_gloss": "तुसीं करो (Find and administer) असाडी कारी (a remedy for me). केही हो गई (How dreadful has become) वेदन भारी (this heavy agony of separation).",
                "poetic_hindi": "सखियो! करो कोई उपचार हमारा,\nकैसा कठिन रोग विरह का डारा!",
                "poetic_english": "O companions, find a healing art;\nWhat heavy agony strikes my heart!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "उह घर मेरे विच आया, उस आ मैनूं भरमाइआ,  ",
                    "पुच्छो जादू है कि साइआ, उस तों लवो हकीकत सारी ।  ",
                    "तुसीं करो असाडी कारी ।"
                ],
                "hindi_gloss": "उह (वह प्रियतम) घर मेरे विच (मेरे घर के भीतर) आया (आया), उस (उसने) आ (आकर) मैनूं (मुझको) भरमाइआ (मोहित/भ्रमित कर दिया), पुच्छो (उससे पूछो कि) जादू है (यह कोई जादू-टोना है) कि (या) साइआ (किसी भूत-प्रेत की छाया है?), उस तों (उसी से) लवो (प्राप्त करो) हकीकत (सच्चा रहस्य) सारी (सम्पूर्ण)।",
                "english_gloss": "उह घर मेरे विच आया (He stepped into my house), उस आ मैनूं भरमाइआ (coming in He bewitched and enchanted me), पुच्छो जादू है कि साइआ (ask Him whether it is sorcery or a haunting shadow), उस तों लवो हकीकत सारी (extract from Him the whole truth of this affair).",
                "poetic_hindi": "वो घर मेरे भीतर आया, आकर उसने भरमाया;\nजादू है कि प्रेत का साया? पूछो उससे भेद सारा!\nसखियो! करो कोई उपचार हमारा!",
                "poetic_english": "He stepped into my chamber floor, and cast enchantment at my core;\nIs it a phantom or magic lore? Inquire the truth behind His door!\nO companions, find a healing art!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "ओहो दिल मेरे विच वस्सदा, बैठा नाल असाडे हस्सदा,  ",
                    "पुच्छां बातां ते उट्ठ नस्सदा, लै बाज़ां वांङ उडारी ।  ",
                    "तुसीं करो असाडी कारी ।"
                ],
                "hindi_gloss": "ओहो (वही प्रियतम) दिल मेरे विच (मेरे हृदय के भीतर) वस्सदा (निवास करता है), बैठा (बैठकर) नाल असाडे (हमारे साथ) हस्सदा (हंसता-बतियाता है), पुच्छां बातां (जब मैं कोई गूढ़ बात पूछती हूँ) ते (तो) उट्ठ नस्सदा (उठकर भाग जाता है), लै बाज़ां वांङ (शिकारी बाज़ के समान) उडारी (उड़ान भरकर)।",
                "english_gloss": "ओहो दिल मेरे विच वस्सदा (He alone dwells within my heart), बैठा नाल असाडे हस्सदा (sitting beside me He smiles and laughs), पुच्छां बातां (yet when I ask Him intimate questions) ते उट्ठ नस्सदा (He leaps up and flees), लै बाज़ां वांङ उडारी (taking flight like a soaring falcon).",
                "poetic_hindi": "हृदय में मेरे वो बसता है, बैठ हमारे संग हँसता है;\nभेद पूछूँ तो उड़ नसता है, जैसे बाज़ उड़े मतवारा!\nसखियो! करो कोई उपचार हमारा!",
                "poetic_english": "Within my heart He loves to bide, and smiles while sitting at my side;\nYet when I ask, He flees wide, like falcons soaring over tide!\nO companions, find a healing art!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "मैं शहु दरिआवां पईआं, ठाठां लहरां दे मूंह गईआं,  ",
                    "फड़ के घुंमन घेर भवईआं, उपर बरखा रैन अंध्यारी ।  ",
                    "तुसीं करो असाडी कारी ।"
                ],
                "hindi_gloss": "मैं (मैं) शहु (गहरे अगाध) दरिआवां (दरिया के प्रवाह में) पईआं (गिर पड़ी हूँ), ठाठां (उमड़ती तूफानी) लहरां दे (लहरों के) मूंह गईआं (मुँह में समा गई हूँ), फड़ के (पकड़कर) घुंमन घेर (भँवरों ने) भवईआं (मुझे चक्कर खिला दिए हैं), उपर (ऊपर से) बरखा (मूसलाधार वर्षा है और) रैन (रात) अंध्यारी (अंधकारमयी है)।",
                "english_gloss": "मैं शहु दरिआवां पईआं (I have fallen into deep ocean rivers), ठाठां लहरां दे मूंह गईआं (swept into the jaws of crashing waves), फड़ के घुंमन घेर भवईआं (seized by whirlpools spinning me round), उपर बरखा (above falls torrential rain in) रैन अंध्यारी (a pitch-black night).",
                "poetic_hindi": "गहरे दरिया में मैं गिरी, तूफानी लहरों में घिरी;\nभँवर में चकराती फिरी, ऊपर बरसे नैन-अंधियारा!\nसखियो! करो कोई उपचार हमारा!",
                "poetic_english": "In fathomless torrents I am thrown, into the jaws of breakers blown;\nSpun round by whirlpools all alone, 'neath stormy skies in darkness prone!\nO companions, find a healing art!"
            },
            {
                "stanza_number": 5,
                "original": [
                    "सईआं ऐड छनिच्छर चाए, तारे खारिआं हेठ छुपाए,  ",
                    "मुंज दियां रस्सियां नाग बणाए, इहनां सेहरां तों बलेहारी ।  ",
                    "तुसीं करो असाडी कारी ।"
                ],
                "hindi_gloss": "सईआं (सखियों ने) ऐड (ऐसे-ऐसे) छनिच्छर (टोने-टोटके/कौतुक) चाए (रचे हैं), तारे (आकाश के तारों को) खारिआं हेठ (टोकरियों के नीचे) छुपाए (छिपा दिया), मुंज दियां (मूंज घास की) रस्सियां (साधारण रस्सियों को) नाग (विषधर सर्प) बणाए (बना दिया), इहनां (इन अद्भुत) सेहरां तों (जादू-टोनों पर मैं) बलेहारी (बलिहारी जाती हूँ)।",
                "english_gloss": "सईआं ऐड छनिच्छर चाए (My companions have raised such uncanny arts), तारे खारिआं हेठ छुपाए (hiding the stars beneath baskets), मुंज दियां रस्सियां (coarse hempen ropes) नाग बणाए (turned into venomous cobras), इहनां सेहरां तों (unto such wizardries and spells) बलेहारी (I surrender in wonder).",
                "poetic_hindi": "सखियों ने ऐसे खेल रचाए, टोकरियों तले तारे छुपाए;\nमूँज की रस्सी को नाग बनाए, बलिहारी जाऊँ जादू न्यारा!\nसखियो! करो कोई उपचार हमारा!",
                "poetic_english": "Such sorceries my companions weave: stars beneath baskets to deceive;\nFrom hempen ropes live vipers cleave—what wizardry must I believe!\nO companions, find a healing art!"
            },
            {
                "stanza_number": 6,
                "original": [
                    "इह जो मुरली कान्ह वजाई, दिल मेरे नूं चोट लगाई,  ",
                    "आह दे नाअरे करदी आही, मैं रोवां ज़ारो ज़ारी ।  ",
                    "तुसीं करो असाडी कारी ।"
                ],
                "hindi_gloss": "इह जो (यह जो) मुरली (बांसुरी) कान्ह (कान्हा/भगवान कृष्ण ने) वजाई (बजाई है), दिल मेरे नूं (उसने मेरे दिल पर) चोट लगाई (गहरी चोट कर दी है), आह दे (आर्तनाद के) नाअरे (गगनभेदी नारे) करदी आही (लगाती फिरती हूँ), मैं रोवां (और मैं रोती हूँ) ज़ारो ज़ारी (जार-जार बहते अश्रुओं से)।",
                "english_gloss": "इह जो मुरली (This sweet flute which) कान्ह वजाई (Krishna played), दिल मेरे नूं चोट लगाई (struck a mortal blow upon my heart), आह दे नाअरे करदी आही (I raise loud cries of agony), मैं रोवां ज़ारो ज़ारी (weeping with incessant torrents of tears).",
                "poetic_hindi": "कान्हा ने ऐसी बंसी बजाई, दिल पे गहरी चोट लगाई;\nचीख-चीख कर आहें भरीं, रोऊँ मैं जारो-जारी सारा!\nसखियो! करो कोई उपचार हमारा!",
                "poetic_english": "The flute that Krishna played so sweet, struck deep where soul and sorrow meet;\nCrying aloud in lane and street, I weep in tears before His feet!\nO companions, find a healing art!"
            },
            {
                "stanza_number": 7,
                "original": [
                    "इश्क दीवाने लीकां लाईआं, डाढियां घणियां सत्थां पाईआं,  ",
                    "हां मैं बक्करी कोल कसाईआं, रहन्दा सहम हमेशा भारी ।  ",
                    "तुसीं करो असाडी कारी ।"
                ],
                "hindi_gloss": "इश्क (प्रेम के) दीवाने (दीवानेपन ने) लीकां (मर्यादा की रेखाएं) लाईआं/मिटाईं (खींच/मिटा दी हैं), डाढियां (कठोर) घणियां (घनी) सत्थां (पंचायतें/अदालतें) पाईआं (बैठाई गईं), हां मैं (मैं तो ऐसी हूँ जैसे) बक्करी (बकरी बंधी हो) कोल कसाईआं (कसाई के खूँटे के पास), रहन्दा (बना रहता है) सहम (मृत्यु का भय) हमेशा भारी (सदा भारी)।",
                "english_gloss": "इश्क दीवाने लीकां लाईआं (Love's madness drew its relentless boundaries), डाढियां घणियां सत्थां पाईआं (harsh panchayats sat in judgment upon me), हां मैं बक्करी कोल कसाईआं (I am like a helpless goat tethered beside the butcher), रहन्दा सहम हमेशा भारी (living in perpetual, suffocating dread).",
                "poetic_hindi": "दीवाने इश्क ने रेखा खींची, पंचायत बैठी कड़वी-मीची;\nकसाई के खूँटे बँधी मैं बकरी, सहम का छाया पहरा भारी!\nसखियो! करो कोई उपचार हमारा!",
                "poetic_english": "Mad passion drew its lines austere; harsh tribunals condemned me here;\nLike a goat tied to the butcher near, I tremble in perpetual fear!\nO companions, find a healing art!"
            },
            {
                "stanza_number": 8,
                "original": [
                    "इश्क रोहेला नाहीं छप्पदा, अन्दर धरिआ बन्न्हीं नच्चदा,  ",
                    "मैनूं द्यु सुनेहुड़ा सच्च दा, मेरी करो कोई ग़मखारी ।  ",
                    "तुसीं करो असाडी कारी ।"
                ],
                "hindi_gloss": "इश्क (प्रेम रूपी) रोहेला (पहाड़ी रोहिल्ला पठान शूरवीर) नाहीं छप्पदा (कभी छिपाये नहीं छिपता), अन्दर (अंतःकरण में) धरिआ (रखा हुआ भी) बन्न्हीं (बंधन तोड़कर) नच्चदा (नाचता है), मैनूं (मुझको) द्यु (दो) सुनेहुड़ा (सच्चा संदेश) सच्च दा (परम सत्य का), मेरी करो (मेरी सुध लो) कोई ग़मखारी (कोई तो मेरी व्यथा का साझीदार बनो)।",
                "english_gloss": "इश्क रोहेला (Love, like a fierce Rohilla warrior) नाहीं छप्पदा (can never be hidden), अन्दर धरिआ (though kept locked inside) बन्न्हीं नच्चदा (it breaks all bonds and dances), मैनूं द्यु सुनेहुड़ा सच्च दा (bring me the message of the Ultimate Truth), मेरी करो कोई ग़मखारी (come share and comfort my sorrow).",
                "poetic_hindi": "इश्क-रोहिल्ला छुपता नाहीं, बंधे न बंधन मन के माहीं;\nसच्चा संदेशा लाओ री कोई, करो विरह की गमख्वारी!\nसखियो! करो कोई उपचार हमारा!",
                "poetic_english": "Love like a fierce Rohilla steed, brooks no restraint and knows no breed;\nBring me Truth's message in my need, and comfort my sore heart indeed!\nO companions, find a healing art!"
            },
            {
                "stanza_number": 9,
                "original": [
                    "मैं की मेहर मुहब्बत जाणां, सईआं करदियां ज़ोर धिङाणा,  ",
                    "गलगल मेवा की हदवाणा, की कोई वैद पसारी ।  ",
                    "तुसीं करो असाडी कारी ।"
                ],
                "hindi_gloss": "मैं (मैं) की (क्या) मेहर (कृपा) मुहब्बत (और प्रेम का रहस्य) जाणां (जानती थी?), सईआं (सखियाँ) करदियां (करती हैं) ज़ोर धिङाणा (जबरदस्ती/अन्याय), गलगल (नींबू/गलगल फल) मेवा (मेवा-मिष्ठान्न) की (और क्या) हदवाणा (तरबूज-फल), की कोई (क्या कोई सांसारिक) वैद (वैद्य) पसारी (या पंसारी का काढ़ा काम आएगा?)।",
                "english_gloss": "मैं की मेहर मुहब्बत जाणां (What did I know of love and grace?), सईआं करदियां ज़ोर धिङाणा (companions enforce their tyranny upon me), गलगल मेवा की हदवाणा (what use are sour citrons, dry fruits, or watermelons?), की कोई वैद पसारी (what cure can herbalist or grocer bring?).",
                "poetic_hindi": "मैं क्या जानूँ प्रेम-सगाई? सखियों ने जबरन रीति चलाई;\nमेवा-तरबूज का काम न काई, वैद-पंसारी क्या करे बिचारा?\nसखियो! करो कोई उपचार हमारा!",
                "poetic_english": "What did I know of love's deep tide? My friends force custom at my side;\nNo fruit or melon can heal inside; what herb can apothecary guide?\nO companions, find a healing art!"
            },
            {
                "stanza_number": 10,
                "original": [
                    "नौ शौह जिस दा बांस बरेली, टुट्टी डालों रही इकेली,  ",
                    "कूके बेली बेली बेली, उहदी करे कोई दिलदारी ।  ",
                    "तुसीं करो असाडी कारी ।"
                ],
                "hindi_gloss": "नौ शौह (वह नया प्रियतम/वंशीधर) जिस दा (जिसकी बाँसुरी का) बांस (बांस) बरेली (बरेली नगर का उत्कृष्ट बांस था), टुट्टी (टूटकर) डालों (अपनी टहनी से) रही इकेली (अकेली रह गई है), कूके (कराहती है) बेली बेली बेली ('हे मेरे साथी! हे मेरे प्रियतम!'), उहदी (उस विरहिणी की) करे कोई (कोई तो करे) दिलदारी (धीरज/सांत्वना)।",
                "english_gloss": "नौ शौह जिस दा बांस बरेली (The youthful King whose flute was carved of Bareilly's reed), टुट्टी डालों (severed from its parent branch) रही इकेली (it weeps solitary and alone), कूके बेली बेली बेली (crying: 'O Friend, O Beloved, O Companion!'), उहदी करे कोई दिलदारी (let someone bring solace to its broken heart).",
                "poetic_hindi": "बरेली के बाँस की बंसी पिया की, डाली से टूटी एकाकिनी बाकी;\n'बेली-बेली' कूकती विरहन साकी, कोई तो दे धीरज सहारा!\nसखियो! करो कोई उपचार हमारा!",
                "poetic_english": "From Bareilly's groves the flute was torn, severed from roots to weep forlorn;\n'Beloved! Beloved!' it cries unworn—who can console a heart so torn?\nO companions, find a healing art!"
            },
            {
                "stanza_number": 11,
                "original": [
                    "बुल्ल्हा शौह दे जे मैं जावां, आपना सिर धड़ फेर ना पावां,  ",
                    "ओथे जावां फेर ना आवां, एथे ऐवें उमर गुज़ारी ।  ",
                    "तुसीं करो असाडी कारी ।  ",
                    "केही हो गई वेदन भारी ।"
                ],
                "hindi_gloss": "बुल्ल्हा (बुल्लेशाह कहता है) शौह दे (यदि मैं उस प्रियतम के दरबार) जे मैं जावां (चली जाऊँ), आपना (अपना) सिर (सिर) धड़ (और धड़) फेर ना पावां (फिर कभी वापस न पा सकूँ - पूर्ण आत्म-समर्पण हो जाए), ओथे जावां (यदि वहाँ चली जाऊँ) फेर ना आवां (तो फिर इस नश्वर लोक में कभी लौटकर न आऊँ), एथे (यहाँ संसार में) ऐवें (व्यर्थ ही) उमर (अपनी आयु) गुज़ारी (गँवा दी है)।",
                "english_gloss": "बुल्ल्हा शौह दे जे मैं जावां (If I enter the portal of the Sovereign Beloved), आपना सिर धड़ फेर ना पावां (I shall never regain my severed head or torso), ओथे जावां फेर ना आवां (once I go there, I shall never return), एथे ऐवें उमर गुज़ारी (here in this worldly illusion I wasted my precious life in vain).",
                "poetic_hindi": "बुल्ल्हा कहे, शाह-दर जाऊँ, शीश-धड़ फिर कभी न पाऊँ;\nजाऊँ वहाँ तो लौट न आऊँ, यहाँ व्यर्थ ही जनम गँवारा!\nसखियो! करो कोई उपचार हमारा,\nकैसा कठिन रोग विरह का डारा!",
                "poetic_english": "Bulleh cries: if to that King I fly, my head and torso severed lie;\nOnce entered there, no more shall I return to where vain years pass by!\nO companions, find a healing art;\nWhat heavy agony strikes my heart!"
            }
        ],
        "sufi_commentary": "Kafi 148 is an impassioned masterpiece on the incurable nature of Divine Love (Ishq-e-Haqiqi). Bulleh mocks all conventional cures: no country doctor ('वैद') or village apothecary ('पसारी') can treat a heart struck by the arrow of God. In Stanza 6, Bulleh evokes the piercing sound of Krishna's flute ('मुरली कान्ह वजाई'), which acts as a fatal blow that unravels all worldly conditioning. In Stanza 7, he creates a chilling metaphor of sacrificial surrender: the lover is like a helpless goat tethered beside the butcher ('बक्करी कोल कसाईआं'), waiting with trembling joy for the decapitating blade of Fana. In Stanza 10, Bulleh pays homage to the famous opening of Rumi's Masnavi (the Song of the Reed): the soul is like a hollow reed torn from the bamboo groves of Bareilly, whose haunting melody is nothing other than its agonizing lament for reunion with its Source ('कूके बेली बेली बेली'). Bulleh concludes that crossing the Master's threshold is irreversible: once entering that realm, the egoic head and body are severed forever ('आपना सिर धड़ फेर ना पावां'), dissolving the finite seeker into the Infinite Beloved."
    },
    {
        "id": 149,
        "title_punjabi": "उलटे होर ज़माने आए",
        "title_english": "Inverted Times Have Arrived",
        "raga": "Raga Kafi / Bhairavi",
        "meter": "Dohra / Matrik (16-12 matras)",
        "theme": "Cosmic Inversion, Collapse of the Social Hierarchy, and Sovereign Decree of the Divine",
        "historical_context": "Composed in response to the revolutionary upheaval of 18th-century Punjab. The decline of the Mughal aristocracy, the peasant uprisings of the Banda Singh Bahadur era, and the rise of Dalit, lower-caste, and Sikh Misls completely overturned feudal norms. Bulleh observes this revolution without bourgeois grief: crows hunt falcons, sparrows devour hawks, and thoroughbred Iraqi steeds are whipped while donkeys graze on lush clover. Recognizing that this social upheaval is commanded from the Divine Court ('हुकम हज़ूरों आया'), Bulleh accepts this holy inversion as Divine Justice against tyrannical elites.",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "उलटे होर ज़माने आए ।  ",
                    "कां लगड़ नूं मारन लग्गे चिड़ियां जुर्रे खाए,  ",
                    "उलटे होर ज़माने आए ।"
                ],
                "hindi_gloss": "उलटे (विपरीत/उलटे) होर (और भी विचित्र) ज़माने (युग/दिन) आए (आ पहुँचे हैं)। कां (कौवे) लगड़ नूं (शिकारी बाज/फाल्कन को) मारन लग्गे (मारने लगे हैं), चिड़ियां (नन्हीं गौरैया चिड़ियाँ) जुर्रे (शिकारी शिकारी बाजों को) खाए (मार-मार कर खा रही हैं)।",
                "english_gloss": "उलटे होर ज़माने आए (Inverted, topsy-turvy times have arrived). कां (Crows) लगड़ नूं (falcons) मारन लग्गे (have begun to strike and kill), चिड़ियां (fragile sparrows) जुर्रे खाए (devour mighty hunting hawks).",
                "poetic_hindi": "उलटे और ज़माने आए!\nकौवे बाज को मारन लागे, चिड़ियाँ शिकरे खाए,\nउलटे और ज़माने आए!",
                "poetic_english": "Topsy-turvy times have come to pass!\nCrows strike down the falcon fast, sparrows eat the hawks at last,\nTopsy-turvy times have come to pass!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "इराकियां नूं पई चाबक पउंदी गद्धो खोद पवाए,  ",
                    "उलटे होर ज़माने आए ।"
                ],
                "hindi_gloss": "इराकियां नूं (उच्च नस्ल के इराकी अरबी घोड़ों पर) पई चाबक पउंदी (चाबुकों की मार पड़ रही है), गद्धो (और गधों को) खोद (हरी-हरी दूब/घास की क्यारियों में) पवाए (चरने के लिए मखमली आसन दिए जा रहे हैं)।",
                "english_gloss": "इराकियां नूं (Noble Iraqi steeds) पई चाबक पउंदी (are lashed with whips), गद्धो (while lowly donkeys) खोद पवाए (are fed rich pasture and pampering).",
                "poetic_hindi": "इराकी घोड़ों पे चाबुक बरसे, गधे हरी घास चबाए,\nउलटे और ज़माने आए!",
                "poetic_english": "Iraqi thoroughbreds feel the whip, while donkeys feast and clover sip,\nTopsy-turvy times have come to pass!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "बुल्ल्हा हुकम हज़ूरों आया तिस नूं कौन हटाए,  ",
                    "उलटे होर ज़माने आए ।"
                ],
                "hindi_gloss": "बुल्ल्हा (बुल्लेशाह कहता है) हुकम (यह क्रांति और युग-परिवर्तन का आदेश) हज़ूरों (सर्वोच्च परमात्मा के दरबार से) आया (आया है), तिस नूं (उस सर्वशक्तिमान आदेश को) कौन (कौन मनुष्य) हटाए (रोक या टाल सकता है?)।",
                "english_gloss": "बुल्ल्हा (Bulleh cries) हुकम हज़ूरों आया (this sovereign decree has arrived from the Supreme Court on high), तिस नूं कौन हटाए (who possesses the power to avert it?).",
                "poetic_hindi": "बुल्ल्हा! हुक्म हुज़ूर से आया, इसे कौन लौटाए?\nउलटे और ज़माने आए!",
                "poetic_english": "Bulleh cries: this edict came from God's Court above, who can defame?\nTopsy-turvy times have come to pass!"
            }
        ],
        "sufi_commentary": "Kafi 149 is a sharp sociopolitical and cosmic commentary on historical inversion (Inqilab / Ulat-pulaat). During the mid-18th century in Punjab, the decadent Mughal feudal nobility was smashed by peasant revolts, Afghan incursions, and the rise of local subaltern warriors. Bulleh captures this cataclysm through traditional ornithological and equestrian metaphors: the aristocratic hunters (the lagar-falcon, the jurra-hawk, and the thoroughbred Iraqi horse) are stripped of their supremacy, while the downtrodden (the crow, the sparrow, and the donkey) rise to power. Most orthodox chroniclers mourned this as the end of civilization; Bulleh Shah, however, recognizes it as a manifestation of Divine Irony and Cosmic Retribution: 'बुल्ल्हा हुकम हज़ूरों आया तिस नूं कौन हटाए'. When earthly tyrants exceed their measure, the Divine will inverts the cosmos, empowering sparrows to devour falcons."
    },
    {
        "id": 150,
        "title_punjabi": "उलटी गंग बहाइओ रे साधो, तब हर दरसन पाए",
        "title_english": "Make the Ganges Flow in Reverse, O Seekers!",
        "raga": "Raga Ramkali / Bhairav",
        "meter": "Sant Bhasha / Chhand (16-14 matras)",
        "theme": "Esoteric Yogic Awakening (Ulat-Bansi), Kundalini Ascension, and Defeating the Ten-Headed Ego",
        "historical_context": "Reflecting deep confluence with the Nath Yogic, Sant Sahaj, and Gorakhnath traditions of Punjab, Bulleh Shah employs the esoteric genre of 'Ulat-bansi' (reversal poetry). To see God ('तब हर दरसन पाए'), the seeker must reverse the downward-flowing sensory stream ('उलटी गंग') through Kumbhaka (breath retention / Kumbhakarna) and decapitate the ten-headed demon of egoic senses (Ravana / Dahsir), bathing in the Amrita-mandala of the crown chakra.",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "उलटी गंग बहाइओ रे साधो, तब हर दरसन पाए ।  ",
                    "प्रेम दी पूनी हाथ में लीजो, गुझ्झ मरोड़ी पड़ने ना दीजो ।"
                ],
                "hindi_gloss": "उलटी (विपरीत दिशा में/उर्ध्वगामी) गंग (गंगा रूपी प्राण-धारा/इडा-पिंगला को) बहाइओ (बहाओ) रे साधो (हे संत साधको!), तब (तभी) हर (भगवान हरि का) दरसन (साक्षात्कार) पाए (पा सकोगे)। प्रेम दी (ईश्वरीय प्रेम की) पूनी (कपास की पूनी/लच्छी) हाथ में (अपने हाथ में) लीजो (ले लो), गुझ्झ (भीतर कोई) मरोड़ी (गांठ या ऐंठन) पड़ने (पड़ने) ना दीजो (मत देना)।",
                "english_gloss": "उलटी गंग बहाइओ (Make the Ganges stream flow in reverse) रे साधो (O seekers/ascetics!), तब हर दरसन पाए (then alone shall you behold Hari's face). प्रेम दी पूनी (The sliver of divine love's cotton) हाथ में लीजो (hold firmly in your hand), गुझ्झ मरोड़ी (secret tangles and knots) पड़ने ना दीजो (do not allow to form).",
                "poetic_hindi": "उलटी गंग बहाओ साधो! तब हरि-दरशन पाए;\nप्रेम की पूनी हाथ में लीजो, गुप्त मरोड़ी पड़ने न दीजो!",
                "poetic_english": "Make the Ganges backward roll, O seekers of the Way!\nThen alone Hari's face divine your longing shall survey;\nTake the spool of love in hand, and spin without delay;\nLet no tangled knot of pride across your spinning stray!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "गयान का तक्कला ध्यान का चरखा, उलटा फेर भुवाए ।  ",
                    "उलटे पाउं पर कुंभकरन जाए, तब लंका का भेद उपाए ।"
                ],
                "hindi_gloss": "गयान (आत्म-ज्ञान) का (का) तक्कला (तकला/धुरी) ध्यान (गहन ध्यान) का चरखा (चरखा बनाकर), उलटा (विपरीत दिशा में) फेर (घुमाकर) भुवाए (चलाओ)। उलटे पाउं पर (विपरीत पाँव पर/कुंभक प्राणायाम के संतुलन पर) कुंभकरन (कुंभकर्ण रूपी अचेतन निद्रा) जाए (जागृत होकर विलीन हो), तब (तभी) लंका (मायावी लंका रूपी शरीर) का (का) भेद (सच्चा रहस्य) उपाए (प्रकट होता है)।",
                "english_gloss": "गयान का तक्कला (The spindle of divine gnosis) ध्यान का चरखा (upon the spinning-wheel of one-pointed meditation), उलटा फेर भुवाए (spin in reverse motion). उलटे पाउं पर (Upon reversed feet / through Kumbhaka breath-retention) कुंभकरन जाए (the slumbering giant Kumbhakarna dissolves), तब लंका का भेद उपाए (then the secret of Lanka / the body is revealed).",
                "poetic_hindi": "ज्ञान का तकला, ध्यान का चरखा, उलटा फेर घुमाए;\nउलटे पाँव कुंभकर्ण जाए, तब लंका का भेद उपाए!",
                "poetic_english": "The spindle made of gnosis true, upon contemplation's wheel;\nSpin it backwards, upside-down, to break the worldly seal;\nWhen the slumbering Kumbhakarna falls, the breath-restraint will heal,\nAnd the citadel of Lanka its mystic core reveal!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "दैहंसर लुट्ट्या हुन लछमन बाकी, तब अनहद नाद बजाए ।  ",
                    "इह गत गुर की पैरों पावें, गुर का सेवक तभी सदाए ।"
                ],
                "hindi_gloss": "दैहंसर (दस सिरों वाला रावण अर्थात दस इन्द्रियों का अहंकार) लुट्ट्या (नष्ट/लुट गया), हुन (अब) लछमन (लक्ष्मण रूपी सजग वैराग्य और मन) बाकी (शेष रह गया), तब (तब अंतःकरण में) अनहद (अनाहत) नाद (दिव्य ओंकार ध्वनि) बजाए (गूंज उठती है)। इह गत (यह परम गति/अवस्था) गुर की (सद्गुरु के) पैरों (चरणों में समर्पित होकर ही) पावें (प्राप्त हो सकती है), गुर का (सद्गुरु का सच्चा) सेवक (शिष्य) तभी (तभी) सदाए (कहलाता है)।",
                "english_gloss": "दैहंसर लुट्ट्या (When the ten-headed Ravana of the ten senses is plundered and destroyed), हुन लछमन बाकी (now only vigilant Lakshmana / pure mind remains), तब अनहद नाद बजाए (then the unstruck celestial sound resonates). इह गत (This transcendent state) गुर की पैरों पावें (is attained at the feet of the Guru), गुर का सेवक तभी सदाए (then alone is one worthy to be called the Guru's disciple).",
                "poetic_hindi": "दशमुख लूटा, लछमन बाकी, तब अनहद नाद बजाए;\nयह गति गुरु के चरणों पावे, गुरु-सेवक तब कहलाए!",
                "poetic_english": "The ten-headed titan Ravana falls, and Lakshmana stands alone;\nThen the unstruck cosmic horn resounds from zone to zone;\nAt the Guru's holy feet this exalted state is known;\nOnly then the true disciple by his Master's mark is shown!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "अंमृत मंडल मूं तब ऐसी दे, कि हरी हरि हो जाए ।  ",
                    "उलटी गंग बहाइओ रे साधो, तब हर दरसन पाए ।"
                ],
                "hindi_gloss": "अंमृत मंडल (सहस्रार चक्र के अमृत-मंडल में) मूं (अपने मुख को) तब ऐसी दे (इस प्रकार लगा दे), कि हरी (जीवात्मा स्वयं) हरि (परमात्मा हरि के साथ तद्रूप) हो जाए (हो जाए)। उलटी गंग बहाइओ रे साधो, तब हर दरसन पाए ।",
                "english_gloss": "अंमृत मंडल (Unto the realm of divine Nectar in the Sahasrara) मूं तब ऐसी दे (apply thy mouth so deeply), कि हरी हरि हो जाए (that the green sprout of the soul merges into Hari, becoming Hari Himself). उलटी गंग बहाइओ रे साधो, तब हर दरसन पाए ।",
                "poetic_hindi": "अमृत-मण्डल में मुख ऐसा दे, कि हरी हरि हो जाए;\nउलटी गंग बहाओ साधो! तब हरि-दरशन पाए!",
                "poetic_english": "Drink deep from the Nectar-Chamber till all boundaries fade away,\nTill the mortal soul turns Hari in eternal, shining day!\nMake the Ganges backward roll, O seekers of the Way!\nThen alone Hari's face divine your longing shall survey!"
            }
        ],
        "sufi_commentary": "Kafi 150 represents Bulleh Shah's sublime mastery of the Yogic-Sant esoteric lexicon (Ulat-bansi / inverted discourse). The phrase 'उलटी गंग बहाइओ' (make the Ganges flow backward) is the classical Yogic technical term for reversing the downward dissipation of vital energy (Apana / sensory craving) and channeling it upward along the Sushumna Nadi into the Sahasrara Chakra. The spinning wheel (Charkha) of Dhyana is driven by the spindle (Takla) of Gnosis (Jnana). Bulleh allegorizes the Ramayana into interior Kundalini anatomy: 'कुंभकरन' (Kumbhakarna) represents both the lethargic sleep of ignorance and the esoteric practice of Kumbhaka (pranayama breath-holding); 'लंका' (Lanka) is the physical body surrounded by the ocean of Maya; 'दैहंसर' (Dahsira / the ten-headed Ravana) represents the ten sensory and motor organs (Indriyas) dominated by ego. When the ten-headed demon is slain and purified discipline (Lakshmana) remains, the unstruck sound (Anahata Nada) reverberates through consciousness. Finally, the seeker drinks from the Amrita Mandala (the lunar vessel of ambrosia at the crown chakra), dissolving all duality until the seeker ('हरी', the tender green plant) merges irreversibly into the Supreme Reality ('हरि')."
    }
]

# Lexicon updates for batch 146-150
new_lexicon_entries = {
    "भेखी": {
        "gurmukhi": "ਭੇਖੀ",
        "hindi": "बहुरूपिया, वेश बदलने वाला, मायावी नट",
        "english": "Master of disguises, cosmic actor, masquerader",
        "context": "किसे भेखी भेख वटाइआ ए (Kafi 146)"
    },
    "पलास": {
        "gurmukhi": "ਪਲਾਸ",
        "hindi": "पलाश, ढाक का वृक्ष (जिसके पुष्प लाल होते हैं किंतु गंधहीन होते हैं)",
        "english": "Palas / Butea monosperma tree (flame of the forest)",
        "context": "मानन्द पलास बणाइओ ई (Kafi 146)"
    },
    "नुकता": {
        "gurmukhi": "ਨੁਕਤਾ",
        "hindi": "बिंदु, अरबी लिपि का नुकता (अहंकार का सूक्ष्म प्रतीक)",
        "english": "Diacritical dot in Arabic script; symbol of egoic illusion",
        "context": "इक नुकते दा है फरक पड़ा (Kafi 146)"
    },
    "निमाणी": {
        "gurmukhi": "ਨਿਮਾਣੀ",
        "hindi": "अहंकार-शून्य, दीन, नम्र, विनीत",
        "english": "Humble, without pride, meek",
        "context": "रव्हीं तूं हर दम हो निमाणी (Kafi 147)"
    },
    "कुचज्जी": {
        "gurmukhi": "ਕੁਚੱਜੀ",
        "hindi": "फूहड़, गुणहीन, गृहकार्य व सलीके से अनभिज्ञ",
        "english": "Unskilled, clumsy, lacking virtues or manners",
        "context": "मैं कुचज्जी नूं लै गल लावे (Kafi 147)"
    },
    "कारी": {
        "gurmukhi": "ਕਾਰੀ",
        "hindi": "इलाज, उपचार, उपाय",
        "english": "Cure, remedy, treatment",
        "context": "तुसीं करो असाडी कारी (Kafi 148)"
    },
    "रोहेला": {
        "gurmukhi": "ਰੋਹੇਲਾ",
        "hindi": "रोहिल्ला पठान, दुर्दम्य शूरवीर योद्धा",
        "english": "Rohilla Afghan warrior; fierce, unstoppable fighter",
        "context": "इश्क रोहेला नाहीं छप्पदा (Kafi 148)"
    },
    "गद्धो": {
        "gurmukhi": "ਗੱਧੋ",
        "hindi": "गधा, गर्दभ",
        "english": "Donkey, ass",
        "context": "गद्धो खोद पवाए (Kafi 149)"
    },
    "उलटी गंग": {
        "gurmukhi": "ਉਲਟੀ ਗੰਗ",
        "hindi": "उलटी गंगा, कुंडलिनी शक्ति का उर्ध्वगमन",
        "english": "Reverse Ganges; upward flow of prana/Kundalini",
        "context": "उलटी गंग बहाइओ रे साधो (Kafi 150)"
    },
    "दैहंसर": {
        "gurmukhi": "ਦੈਹੰਸਰ",
        "hindi": "दशसिर, दस सिरों वाला रावण (दस इन्द्रियों का अहंकार)",
        "english": "Ten-headed Ravana; symbol of the ten senses and ego",
        "context": "दैहंसर लुट्ट्या हुन लछमन बाकी (Kafi 150)"
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
        "last_processed_kafi_id": 150,
        "completed_count": 150,
        "total": 160,
        "next_kafi_id": 151,
        "status": "in_progress"
    }
    with open(CHECKPOINT_PATH, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print("Checkpoint updated: 150/160 completed. Next ID: 151")

if __name__ == "__main__":
    save_batch()
