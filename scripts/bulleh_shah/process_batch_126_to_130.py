# -*- coding: utf-8 -*-
"""
Process Kafian 126 to 130 for Bulleh Shah Trilingual Edition.
Includes the iconic anthem 'Ranjha Ranjha Kardi' (Kafi 129) and epic 'Rahu Rahu Oye Ishqa' (Kafi 126).
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
        "id": 126,
        "title": "रहु रहु उए इश्का मारिआ ई",
        "title_english": "Hold, Hold, O Love! Thou Hast Struck Down All: Say, Whom Hast Thou Ferried Across?",
        "historical_context": "यह 21 बंधों की बुल्ले शाह की सर्वाधिक विस्तृत, महाकाव्यात्मक और ऐतिहासिक-पौराणिक समीक्षात्मक काफी है। इसमें बुल्ले शाह दिव्य प्रेम ('इश्क') को एक सर्वग्रासी, अलौकिक और विस्मयकारी शक्ति के रूप में चित्रित करते हुए पूछते हैं कि हे इश्क! तूने इतिहास में किस प्रेमी को कष्ट दिए बिना पार उतारा है? आदम का स्वर्ग से निष्कासन, नूह का तूफ़ान, मूसा और कोहे-तूर, इस्माइल की कुर्बानी, यूनुस का मछली के पेट में जाना, यूसुफ-ज़ुलैखा, इब्राहीम की अग्नि-परीक्षा, अय्यूब (साबिर) के शरीर में कीड़े, शम्स तबरेज़ी की खाल, मंसूर की सूली, सरमद का सिर कटना, रांझा, मिर्ज़ा, सस्सी, सोहणी, महाभारत का युद्ध (18 अक्षौहिणी सेना का संहार), रामायण में लंका-दहन और रावण-वध, कृष्ण द्वारा कंस-वध, और कर्बला में इमाम हुसैन का सिर नेज़े पर चढ़ना—बुल्ले शाह इन सभी को प्रेम की भीषण अग्नि-परीक्षा के रूप में देखते हैं।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: रहु रहु उए इश्का मारिआ ई)",
        "raga": "राग काफी / आसा / जोगिया",
        "theme": "इश्क की सर्वग्रासी शक्ति, पैगंबरों, संतों और लोक-नायकों के बलिदान, इतिहास का आध्यात्मिक विश्लेषण",
        "stanzas": [
            {
                "original": [
                    "रहु रहु उए इश्का मारिआ ई ।  ",
                    "कहु किस नूं पार उतारिआ ई ।"
                ],
                "hindi_gloss": [
                    "रहु (ठहर) रहु (ठहर जा) उए (अरे ओ) इश्का (क्रूर इश्क!), मारिआ (तूने तो सबको अपने प्रेम-बाणों से मार ही डाला) ई (है) ।",
                    "कहु (जरा बता तो सही कि) किस (किस साधक) नूं (को तूने बिना प्रताड़ित किए सुख से) पार (संसार-सागर से पार) उतारिआ (उतारा) ई (है) ।"
                ],
                "english_gloss": [
                    "रहु रहु (hold, hold!) उए इश्का (O ruthless Love!), मारिआ ई (thou hast struck down everyone) ।",
                    "कहु (say) किस नूं (whom) पार उतारिआ ई (hast thou ever ferried across without trial) ।"
                ],
                "poetic_hindi": [
                    "ठहर जा, ठहर जा ऐ इश्क ! तूने सबको मार गिराया है,",
                    "ज़रा बता तो सही, तूने किसको सुख से पार लगाया है?"
                ],
                "poetic_english": [
                    "Hold, hold, O ruthless Love! Thou hast struck down all who dare;",
                    "Say, whom hast thou ever ferried across without torment and despair?"
                ]
            },
            {
                "original": [
                    "आदम कणकों मन्हा कराइआ, आपे मगर शैतान दुड़ाइआ,  ",
                    "कढ्ढ बहशतों ज़मीन रुलाइआ, केड पसार पसारिआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "आदम (हज़रत आदम को) कणकों (गेहूं का दाना खाने से) मन्हा (मना) कराइआ (करवाया), आपे (फिर स्वयं ही उसके) मगर (पीछे) शैतान (बहकाने वाला शैतान) दुड़ाइआ (दौड़ा दिया),",
                    "कढ्ढ (निकाल कर) बहशतों (स्वर्ग/जन्नत से उन्हें) ज़मीन (धरा की धूल में) रुलाइआ (भटकने पर विवश किया), केड (कैसा विशाल मायावी) पसार (पसारा तूने) पसारिआ (फैला रखा) ई (है) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "आदम कणकों मन्हा कराइआ (forbade Adam from the wheat grain), आपे मगर शैतान दुड़ाइआ (then set Satan running after Him),",
                    "कढ्ढ बहशतों (expelled Him from Paradise) ज़मीन रुलाइआ (to trail in earthly dust), केड पसार पसारिआ ई (what a vast cosmic snare hast thou spread) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "गेहूं खाने से आदम को रोका, पीछे शैतान को दौड़ाया,",
                    "स्वर्ग से निकाल कर मिट्टी में, कैसा खेल रचाया !",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "Thou forbade Adam the forbidden wheat, then loosed the tempter on His track;",
                    "Exiled from Eden to wander in dust—what cosmic net dost thou unpack?",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "ईसा नूं बिन बाप जंमाइआ, नूहे पर तूफान मंगाइआ,  ",
                    "नाल प्यु दे पुत्तर लड़ाइआ, डोब उहनां नूं मारिआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "ईसा (हज़रत ईसा) नूं (को) बिन (बिना) बाप (पिता के गर्भ से) जंमाइआ (जन्म दिलवाकर लोक-निंदा सहवाई), नूहे (हज़रत नूह) पर (के युग में महाप्रलयंकारी) तूफान (जल-तूफ़ान) मंगाइआ (बुलाया),",
                    "नाल (साथ) प्यु (पिता के उसके ही सगे) दे (के) पुत्तर (पुत्र को विद्रोही बनाकर) लड़ाइआ (लड़ा दिया), डोब (और जल में डुबोकर) उहनां (उन पापियों) नूं (को) मारिआ (मार डाला) ई (तूने) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "ईसा नूं बिन बाप जंमाइआ (caused Jesus to be born without earthly father), नूहे पर तूफान मंगाइआ (summoned the Great Deluge upon Noah's folk),",
                    "नाल प्यु दे पुत्तर लड़ाइआ (pitted the son against his father), डोब उहनां नूं मारिआ ई (and drowned them in the roaring deep) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "ईसा को बिन बाप जन्माया, नूह पे जल-तूफान बुलाया,",
                    "पिता संग बेटे को लड़ाकर, गहरे जल में डूब मराया !",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "Thou brought forth Jesus without a sire; on Noah summoned the deluge wide;",
                    "Pitted the son against the father, and drowned them in the surging tide!",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "मूसे नूं कोह-तूर चढ़ाययो, असमाईल नूं ज़िबाह करायओ,  ",
                    "यूनस मच्छी तों निगलाययो, की उहनां नूं रुत्तबे चाढ़आ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "मूसे (हज़रत मूसा) नूं (को) कोह-तूर (कोहे-तूर पर्वत पर) चढ़ाययो (चढ़ाकर अग्नि में तपाया), असमाईल (हज़रत इस्माइल) नूं (को पिता के हाथों) ज़िबाह (कुर्बान) करायओ (करवाने का हुक्म दिया),",
                    "यूनस (हज़रत यूनुस को) मच्छी (व्हेल मछली) तों (के उदर में) निगलाययो (निगलवाया), की (कैसा कठिन) उहनां (उन नबियों) नूं (को) रुत्तबे (आध्यात्मिक पदवी पर) चाढ़आ (चढ़ाया) ई (तूने) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "मूसे नूं कोह-तूर चढ़ाययो (made Moses ascend Mount Sinai), असमाईल नूं ज़िबाह करायओ (caused Ismail to be offered for slaughter),",
                    "यूनस मच्छी तों निगलाययो (caused Jonah to be swallowed by the fish), की उहनां नूं रुत्तबे चाढ़आ ई (what a steep trial to grant them rank) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "मूसा को कोह-तूर चढ़ाया, इस्माइल की गर्दन पे छुरी फिराई,",
                    "यूनुस को मछली से निगलवाया, कैसी यह पदवी बख्शाई?",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "Thou led Moses up Mount Sinai's blaze; bade Ismail under the knife be laid;",
                    "Swallowed Jonah in the belly of the whale—at what steep price is rank displayed?",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "ख़वाब ज़ुलैखां नूं दिखलाययो, यूसफ़ खूह दे विच पवायओ,  ",
                    "भाईआं नूं इलज़ाम दिवाययो, तां मरातब चाढ़आ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "ख़वाब (प्रेम का स्वप्न) ज़ुलैखां (मिस्र की रानी ज़ुलैखा) नूं (को) दिखलाययो (दिखाकर विरह में पागल किया), यूसफ़ (हज़रत यूसुफ को) खूह (अंधे कुएं) दे (के) विच (भीतर) पवायओ (फिंकवाया),",
                    "भाईआं (उनके सगे भाइयों) नूं (को कपट का) इलज़ाम (दोषी) दिवाययो (बनवाया), तां (तब जाकर उन्हें मिस्र का) मरातब (सर्वोच्च पद) चाढ़आ (प्रदान किया) ई (तूने) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "ख़वाब ज़ुलैखां नूं दिखलाययो (showed Zulaikha the dream of passion), यूसफ़ खूह दे विच पवायओ (cast Joseph into the dry well),",
                    "भाईआं नूं इलज़ाम दिवाययो (branded the brothers with guilt), तां मरातब चाढ़आ ई (then elevated Him to royal renown) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "ज़ुलैखा को दिखाया स्वप्न प्रेम का, यूसुफ को कुएं में डलवाया,",
                    "भाइयों के सिर कलंक मढ़ा, तब मिस्र का तख्त सजाया !",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "Thou showed Zulaikha dreams of love; in the dry well Joseph lay betrayed;",
                    "Branded His brothers with dark guilt, before His crown of gold was made!",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "भट्ठ सुलेमान नूं झुकाइओ, इबराहीम चिखा विच पाइओ,  ",
                    "साबर दे तन कीड़े पाययो, हुसन ज़हर दे मारिआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "भट्ठ (हम्माम की भट्टी में) सुलेमान (हज़रत सुलेमान से भट्टी) नूं (को) झुकाइओ (झुकवाकर अंगारे फिंकवाए), इबराहीम (हज़रत इब्राहीम को नमरूद की जलती) चिखा (चिता/अग्निकुंड) विच (में) पाइओ (डलवाया),",
                    "साबर (धैर्यवान हज़रत अय्यूब/साबिर) दे (के) तन (शरीर में भीषण) कीड़े (कीड़े) पाययो (डालकर परीक्षा ली), हुसन (और हज़रत हसन को) ज़हर (विष) दे (देकर) मारिआ (शहीद करवा दिया) ई (तूने) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "भट्ठ सुलेमान नूं झुकाइओ (made Solomon stoke the furnace of the public bath), इबराहीम चिखा विच पाइओ (hurled Abraham into Nimrod's blazing pyre),",
                    "साबर दे तन कीड़े पाययो (infested patient Job's flesh with worms), हुसन ज़हर दे मारिआ ई (and slew Hasan with treacherous poison) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "सुलेमान से भट्टी झुकवाई, इब्राहीम को चिता में डाला,",
                    "अय्यूब के तन में कीड़े डाले, हसन को विष दे मारा प्याला !",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "Solomon stoked the furnace fires; Abraham braved the pyre ablaze;",
                    "Job’s patient flesh was gnawed by worms; Hasan was poisoned all his days!",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "मनसूर नूं चा सूली दित्ता, राहब दा कढवाइओ पित्ता,  ",
                    "ज़करिया सिर कलवत्तर कीता, फेर उहनां कंम की सारिआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "मनसूर (मंसूर हल्लाज) नूं (को) चा (उठाकर) सूली (सूली पर चढ़ा) दित्ता (दिया), राहब (साधक राहिब) दा (का तूने) कढवाइओ (निकलवा लिया) पित्ता (कलेजा/पित्त),",
                    "ज़करिया (हज़रत जकरिया के) सिर (सिर पर तूने) कलवत्तर (चीरने वाला आरा) कीता (चलवाया), फेर (फिर बता कि) उहनां (उन निष्कलंक संतों का तूने कौन-सा) कंम (कार्य) की (क्या) सारिआ (संवारा) ई (तूने) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "मनसूर नूं चा सूली दित्ता (mounted Mansur upon the gallows), राहब दा कढवाइओ पित्ता (cut out the gall-bladder of Rahib),",
                    "ज़करिया सिर कलवत्तर कीता (drove the tearing saw across Zakariya's crown), फेर उहनां कंम की सारिआ ई (what earthly good didst thou deliver them) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "मंसूर को सूली पे चढ़ाया, राहिब का पित्ता कढ़वाया,",
                    "ज़करिया के सिर आरा चलवाया, फिर उनका क्या काज सँवारा?",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "Thou hung Mansur upon the tree; the Rahib’s gall-bladder was torn;",
                    "Upon Zakariya’s crown ran the saw—what earthly comfort have they borne?",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "शाह सरमद दा गला कटाययो, शमस ने जां सुखन अलायओ,  ",
                    "कुमबइजनी आप कहाययो, सिर पैरों खल्ल उतारिआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "शाह सरमद (सूफी संत हज़रत सरमद) दा (का) गला (गला) कटाययो (तूने दिल्ली में कटवा दिया), शमस (हज़रत शम्स तबरेज़ी) ने (ने) जां (जब सत्य का) सुखन (वचन) अलायओ (उच्चारित किया),",
                    "कुमबइजनी ('कुम बिइज़्नी' अर्थात् 'मेरे हुक्म से जी उठ'—यह शब्द जब शम्स से) आप (तूने स्वयं) कहाययो (कहलवाया), सिर (तो सिर से लेकर) पैरों (पैरों तक उनकी जीवित ही) खल्ल (खाल) उतारिआ (उतरवा ली) ई (तूने) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "शाह सरमद दा गला कटाययो (beheaded Saint Sarmad at the Delhi gate), शमस ने जां सुखन अलायओ (when Shams Tabrizi uttered the sacred word),",
                    "कुमबइजनी आप कहाययो (bidding the dead arise: 'Arise by my command!'), सिर पैरों खल्ल उतारिआ ई (they flayed his skin from head to feet) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "शाह सरमद का गला कटाया, शम्स ने जब यह वचन उचारा,",
                    "'कुम-बिइज़्नी' कह मुर्दा जिलाया, सिर से पाँव तक खाल उतारा !",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "Thou cut the throat of Sarmad the Saint; when Shams proclaimed the mystic word,",
                    "'Arise by my decree!'—they stripped his living skin with fire and sword!",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "एस इश्क दे बड़े अडम्बर, इश्क ना छप्पदा बाहर अन्दर,  ",
                    "इश्क कीता शाह शरफ़ कलन्दर, बार्हां वर्हे दरिआ विच ठारिआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "एस (इस दिव्य) इश्क (इश्क) दे (के) बड़े (बड़े विचित्र) अडम्बर (प्रपंच और लीलाएं हैं), इश्क (यह प्रेम) ना (नहीं) छप्पदा (छिपता कभी भी) बाहर (बाहर या) अन्दर (भीतर),",
                    "इश्क (जब यह इश्क) कीता (किया हज़रत) शाह (शाह) शरफ़ (शरफ़ुद्दीन बू अली) कलन्दर (कलंदर ने), बार्हां (तो बारह) वर्हे (वर्षों तक उन्हें ठंडे) दरिआ (दरिया के बर्फीले जल) विच (में खड़े रख कर) ठारिआ (ठिठुराया) ई (तूने) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "एस इश्क दे बड़े अडम्बर (vast and wondrous are the trials of this Love), इश्क ना छप्पदा बाहर अन्दर (Love remains hidden neither without nor within),",
                    "इश्क कीता शाह शरफ़ कलन्दर (when Shah Sharaf Qalandar embraced this Love), बार्हां वर्हे दरिआ विच ठारिआ ई (thou froze Him in the river waters for twelve long years) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "इस इश्क के बड़े प्रपंच, छिपता नहीं यह बाहर-अंदर,",
                    "बारह बरस दरिया में खड़ा रहा, जब इश्क किया शरफ़ कलंदर !",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "Wondrous are the trials of this Love, unhidden within and unhidden without;",
                    "When Shah Sharaf Qalandar surrendered, twelve years in icy streams He stood devout!",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "इश्क लेला दे धुंमां पाईआं, तां मजनूं ने अक्खियां लाईआं,  ",
                    "उहनूं धारां इश्क चुंघाईआं, खूहे बरस गुज़ारिआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "इश्क (इश्क ने जब) लेला (लैला के सौंदर्य की) दे (की) धुंमां (धूम/प्रसिद्धि) पाईआं (फैलाई), तां (तब विरही) मजनूं (मजनू) ने (ने उससे अपनी) अक्खियां (आँखें) लाईआं (लगाईं),",
                    "उहनूं (उस मजनू को तूने विरह-) धारां (धारों का) इश्क (इश्क) चुंघाईआं (पान करवाया), खूहे (और सूखे कुएं के भीतर उसने कई) बरस (वर्ष एकांत विरह में) गुज़ारिआ (बिताए) ई (तेरे कारण) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "इश्क लेला दे धुंमां पाईआं (Love spread the fame of Laila's charms), तां मजनूं ने अक्खियां लाईआं (then Majnun fixed his yearning eyes),",
                    "उहनूं धारां इश्क चुंघाईआं (thou fed him streams of bitter longing), खूहे बरस गुज़ारिआ ई (spending years inside a dry abandoned well) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "लैला के रूप की धूम मची, मजनू ने अंखियां जोड़ीं,",
                    "विरह का विष उसे पिलाया, सूखे कुएं में उम्रें तोड़ीं !",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "Love spread the fame of Laila's face, and trapped Majnun in endless grief;",
                    "Feeding him draughts of bitter thirst, within dry wells bereft of relief!",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "इश्क होरीं हीर वल्ल धाए, तांहीएं रांझे कन्न पड़वाए,  ",
                    "साहबां नूं जदों व्याहुन आए, सिर मिरज़े दा वारिआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "इश्क (प्रेम के देवता जब) होरीं (स्वयं) हीर (हीर की) वल्ल (ओर) धाए (दौड़े), तांहीएं (तभी तो विरह में तड़पकर) रांझे (रांझा ने अपने) कन्न (कान) पड़वाए (छिदवाए और जोगी बना),",
                    "साहबां (साहिबां) नूं (को) जदों (जब श्यालों की बारात) व्याहुन (ब्याहने) आए (आई), सिर (तो जंड के पेड़ तले) मिरज़े (मिर्ज़ा) दा (का शीश) वारिआ (कटवा दिया) ई (तूने) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "इश्क होरीं हीर वल्ल धाए (Love hastened towards Heer of Sial), तांहीएं रांझे कन्न पड़वाए (hence Ranjha pierced His ears to wander in beggar's guise),",
                    "साहबां नूं जदों व्याहुन आए (when suitors came to wed Sahiban), सिर मिरज़े दा वारिआ ई (thou sacrificed Mirza’s severed head beneath the tree) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "हीर की खातिर रांझे ने देखो, कानों में मुंद्राएं डलवाईं,",
                    "साहिबां को जब ब्याहने आए, मिर्ज़ा ने अपनी जान गंवाई !",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "Love flew to Heer, and Ranjha pierced His ears to take the yogi's pack;",
                    "When suitors came for Sahiban, Mirza fell slain beneath the attack!",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "सस्सी थलां दे विच रुलाई, सोहनी कच्चे घड़े रुढ़ाई,  ",
                    "रोडे पिच्छे गल्ल गवाई, टुकड़े कर कर मारिआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "सस्सी (सस्सी को तूने सिंध के दहकते) थलां (मरुस्थलों) दे (के) विच (बीच प्यास से तड़पाकर) रुलाई (भटकाया), सोहनी (सोहणी को) कच्चे (कच्चे मिट्टी के) घड़े (घड़े पर चेनाब के भंवर में) रुढ़ाई (डुबो दिया),",
                    "रोडे (रोडा के प्रेम के) पिच्छे (पीछे हीर/साधिका ने अपनी लोक-मर्यादा की) गल्ल (बात) गवाई (गंवा दी), टुकड़े (और उसके अंग-अंग के टुकड़े-) कर (करके) मारिआ (मार डाला) ई (तूने) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "सस्सी थलां दे विच रुलाई (drove Sassi to perish in the burning sands), सोहनी कच्चे घड़े रुढ़ाई (drowned Sohni upon the unbaked earthen pot),",
                    "रोडे पिच्छे गल्ल गवाई (wiped away honor for Rodah's sake), टुकड़े कर कर मारिआ ई (and hacked Him into pieces to slay) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "सस्सी को रेगिस्तान में भटकाया, सोहणी को कच्चे घड़े डुबोया,",
                    "रोडा के पीछे कुल खोया, टुकड़े कर-कर के मारा !",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "Sassi was scorched in desert dunes; Sohni drowned on the unbaked clay;",
                    "For Rodah's love their name was lost, hacked limb by limb and swept away!",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "फ़ौज़ां कतल कराईआं भाईआं, मशकां चूहआं तों कटवाईआं,  ",
                    "डिट्ठी कुदरत तेरी साईआं, सिर तैथों बलेहारिआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "फ़ौज़ां (सगी) कतल (फौजों का आपस में संहार) कराईआं (करवाया सगे) भाईआं (भाइयों से), मशकां (और जल की मशकों को) चूहआं (चूहों) तों (से) कटवाईआं (कटवाकर सेना को प्यासा मार दिया),",
                    "डिट्ठी (देख ली हमने) कुदरत (यह विचित्र लीला) तेरी (तेरी हे) साईआं (प्रभु), सिर (मेरा यह शीश) तैथों (तुझ पर ही) बलेहारिआ (बलिहारी/न्योछावर है) ई (सदा) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "फ़ौज़ां कतल कराईआं भाईआं (caused kin to slaughter fraternal armies), मशकां चूहआं तों कटवाईआं (caused the water-skins to be gnawed by mice),",
                    "डिट्ठी कुदरत तेरी साईआं (we have witnessed Thy omnipotent sovereignty, O Lord), सिर तैथों बलेहारिआ ई (and offer our head in sacrifice to Thee) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "भाइयों से फौजें कटवाईं, चूहों से मशकें कटवाईं,",
                    "देख ली कुदरत तेरी साहिब, शीश तुझ पर बलिहारी जाए !",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "Brother slew brother on the field; the water-skins were gnawed by mice;",
                    "We saw Thy sovereign majesty, and lay our lives in sacrifice!",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "कैरों पांडो करन लड़ाईआं, अठारां खूहणियां तदों खपाईआं,  ",
                    "मारन भाई सक्यां भाईआं, की ओथे न्यां नितारिआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "कैरों (कौरवों और) पांडो (पांडवों में महाभारत की) करन (करवाई तूने) लड़ाईआं (लड़ाइयां), अठारां (अठारह) खूहणियां (अक्षौहिणी सेनाओं को) तदों (उस कुरुक्षेत्र में) खपाईआं (नष्ट करवा दिया),",
                    "मारन (मार रहे थे सगे) भाई (भाई) सक्यां (सगे) भाईआं (भाइयों को), की (कैसा विचित्र) ओथे (वहाँ तूने अपना) न्यां (न्याय) नितारिआ (प्रकट किया) ई (है) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "कैरों पांडो करन लड़ाईआं (Thou caused the battle of Kauravas and Pandavas), अठारां खूहणियां तदों खपाईआं (eighteen mighty Akshauhinis were consumed in war),",
                    "मारन भाई सक्यां भाईआं (fraternal brothers slaughtered their own flesh and blood), की ओथे न्यां नितारिआ ई (what manner of justice didst Thou dispense there) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "कौरव-पांडव को लड़वाया, अठारह अक्षौहिणी सेना खपाई,",
                    "सगे भाई ने भाई को मारा, कैसी न्याय की रीति बनाई?",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "Kauravas and Pandavas clashed in arms; eighteen armies were swept in blood;",
                    "Brother struck brother down to dust—what justice ruled that crimson flood?",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "नमरूद ने वी खुदा सदाइआ, उस ने रब्ब नूं तीर चलाइआ,  ",
                    "मच्छर तों नमरूद मरवाइआ, कारूं ज़मीं निघारिआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "नमरूद (अहंकारी नमरूद) ने (ने) वी (भी स्वयं को) खुदा (ईश्वर) सदाइआ (कहलाया था), उस (उसने अहंकार में) ने (ने) रब्ब (परमात्मा की ओर आकाश में) नूं (को) तीर (बाण) चलाइआ (चलाया),",
                    "मच्छर (मात्र एक तुच्छ लंगड़े मच्छर) तों (के द्वारा) नमरूद (नमरूद के मस्तिष्क में पीड़ा देकर उसे) मरवाइआ (मरवा डाला तूने), कारूं (और घमंडी धनवान कारून को उसके खजाने सहित) ज़मीं (धरती में) निघारिआ (धंसा दिया) ई (तूने) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "नमरूद ने वी खुदा सदाइआ (Nimrod proclaimed himself to be God), उस ने रब्ब नूं तीर चलाइआ (and shot an arrow towards Heaven),",
                    "मच्छर तों नमरूद मरवाइआ (by a mere gnat Thou caused Nimrod to be slain), कारूं ज़मीं निघारिआ ई (and swallowed wealthy Qarun deep into the earth) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "नमरूद ने खुद को खुदा कहा, अंबर पे उसने तीर चलाया,",
                    "मच्छर से नमरूद को मारा, कारून को धरती में धंसाया !",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "Proud Nimrod deemed himself divine, and shot his arrow at the sky;",
                    "A puny gnat consumed his brain; Qarun deep in the earth did lie!",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "फिरऔन ने जदों ख़ुदा कहाइआ, नील नदी दे विच आया,  ",
                    "ओसे नाल अशटंड जगाइआ, खुदीयों कर तद मारिआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "फिरऔन (मिस्र के राजा फिरौन) ने (ने) जदों (जब स्वयं को) ख़ुदा (परमेश्वर) कहाइआ (घोषित किया), नील (तो जब वह हज़रत मूसा का पीछा करते हुए नील) नदी (नदी) दे (के) विच (बीच) आया,",
                    "ओसे (उसी जल) नाल (से तूने चमत्कार का) अशटंड (प्रचंड रूप) जगाइआ (प्रकट किया), खुदीयों (और उसके अहंकार को चूर-चूर) कर (करके) तद (तब उसे सेना सहित जलमग्न करके) मारिआ (मार डाला) ई (तूने) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "फिरऔन ने जदों ख़ुदा कहाइआ (when Pharaoh proclaimed himself to be Supreme God), नील नदी दे विच आया (and plunged into the parted Red Sea / Nile),",
                    "ओसे नाल अशटंड जगाइआ (Thou unleashed the raging waves upon him), खुदीयों कर तद मारिआ ई (and destroyed him for his monstrous pride) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "फिरौन ने जब खुदा कहलाया, नील नदी में जब वो आया,",
                    "लहरों का तूफ़ान उठा कर, उसके अहंकार को मार गिराया !",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "When Pharaoh boasted he was God, and marched into the parting Nile;",
                    "The roaring surge engulfed his host, shattering his arrogance and guile!",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "लंका चढ़ के नाद बजाययो, लंका राम कोलों लुटवायओ,  ",
                    "हरनाकश कित्ता बहशत बनाययो, उह विच दरवाज़े मारिआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "लंका (स्वर्ण-लंका पर) चढ़ (चढ़कर वानरों का) के (करके) नाद (युद्ध-शंख) बजाययो (बजवाया तूने), लंका (और रावण की लंका को) राम (भगवान श्री राम) कोलों (के हाथों) लुटवायओ (भस्म/नष्ट करवाया),",
                    "हरनाकश (अहंकारी हिरण्यकश्यप ने) कित्ता (कैसा झूठा) बहशत (स्वर्ग) बनाययो (बनाया था), उह (उसे नृसिंह रूप धरकर महल की देहरी/चौखट के) विच (भीतर) दरवाज़े (दरवाजे पर) मारिआ (मार गिराया) ई (तूने) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "लंका चढ़ के नाद बजाययो (sounded the clarion of war upon golden Lanka), लंका राम कोलों लुटवायओ (caused Lanka to be overthrown by Lord Ram),",
                    "हरनाकश कित्ता बहशत बनाययो (Harnakash fashioned an earthly paradise of pride), उह विच दरवाज़े मारिआ ई (and was slain upon the threshold by Narasimha) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "लंका पे रण-नाद बजाया, राम के हाथों लंका जलाई,",
                    "हिरण्यकश्यप को चौखट पे मारा, नृसिंह रूप की शक्ति दिखाई !",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "The war-horn sounded over Lanka; Ram laid her golden ramparts low;",
                    "Harnakash built a false paradise, but on the threshold met his blow!",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "सीता दैहसर लई बेचारी, तद हनूवंत ने लंका साड़ी,  ",
                    "रावन दी सभ ढाह अटारी, ओड़क रावन मारिआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "सीता (माता सीता को जब) दैहसर (दस-सिर वाले रावण ने) लई (अपहरण कर लिया) बेचारी (दीन-अकिंचन बना कर), तद (तब भक्त) हनूवंत (हनुमान) ने (ने अपनी पूंछ से सारी) लंका (लंका) साड़ी (जला डाली),",
                    "रावन (रावण) दी (के महलों की) सभ (सारी) ढाह (ढहा दीं) अटारी (अट्टालिकाएं), ओड़क (और अंततः अहंकारी) रावन (रावण को) मारिआ (मार डाला) ई (तूने) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "सीता दैहसर लई बेचारी (when ten-headed Ravana abducted gentle Sita), तद हनूवंत ने लंका साड़ी (then faithful Hanuman set Lanka ablaze),",
                    "रावन दी सभ ढाह अटारी (shattered all the lofty towers of Ravana), ओड़क रावन मारिआ ई (and in the end Ravana was slain) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "सीता हरी दशानन ने जब, हनुमत ने लंका फूँक जलाई,",
                    "रावण की सब अटारी ढहाई, अंत में रावण की मौत बुलाई !",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "When ten-faced Ravana stole Sita, Hanuman wrapped the towers in flame;",
                    "Ransacked the proud citadel of kings, and quenched the tyrant's boasted name!",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "गोपियां नाल की चज्ज कमाइआ, मक्खन कान्ह तों लुटवाइआ,  ",
                    "राजे कंस नूं पकड़ मंगाइआ, बोदीउं पकड़ पछाड़िआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "गोपियां (गोपियों) नाल (के साथ) की (कैसा अद्भुत प्रेम का) चज्ज (सलीका/आनंद) कमाइआ (रचाया), मक्खन (और गोकुल में घर-घर से) कान्ह (कान्हा/श्रीकृष्ण) तों (के हाथों) लुटवाइआ (लुटवाया),",
                    "राजे (पापी राजा) कंस (कंस) नूं (को उसके अखाड़े में) पकड़ (पकड़) मंगाइआ (मंगवाया), बोदीउं (और उसके सिर की शिखा/केशों से) पकड़ (पकड़कर भूमि पर) पछाड़िआ (पछाड़ कर मार डाला) ई (तूने) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "गोपियां नाल की चज्ज कमाइआ (what wondrous sport Thou played with the Gopis), मक्खन कान्ह तों लुटवाइआ (robbed butter through the hands of dark Krishna),",
                    "राजे कंस नूं पकड़ मंगाइआ (summoned tyrannical King Kamsa to the arena), बोदीउं पकड़ पछाड़िआ ई (and seizing him by his hair dashed him dead) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "गोपियों संग क्या लीला रचाई, कान्हा से माखन लुटवाया,",
                    "पापी कंस को पकड़ मंगवाया, बालों से पटक-पटक मराया !",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "With Gopis what enchanting sport! By Krishna’s hand the butter stolen;",
                    "Dragged cruel Kamsa to the dust, and crushed the tyrant proud and swollen!",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "आपे चा इमाम बणाइआ, उस दे नाल यज़ीद लड़ाइआ,  ",
                    "चौधीं तबकीं शोर मचाइआ, सिर नेज़े 'ते चाढ़आ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "आपे (तूने स्वयं ही हज़रत हुसैन को) चा (उठाकर) इमाम (इमाम और नबी का लाडला) बणाइआ (बनाया), उस (परंतु उसी इमाम) दे (के) नाल (विरुद्ध तूने पापी) यज़ीद (यज़ीद की सेना को) लड़ाइआ (लड़ा दिया),",
                    "चौधीं (चौदहों) तबकीं (लोकों में शोक का) शोर (आर्तनाद) मचाइआ (मचवा दिया), सिर (और कर्बला में इमाम हुसैन का पवित्र सिर) नेज़े (भाले की नोक) 'ते (पर) चाढ़आ (चढ़वा दिया) ई (तूने) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "आपे चा इमाम बणाइआ (Thou Thyself raised Husain as the Holy Imam), उस दे नाल यज़ीद लड़ाइआ (then pitted cruel Yazid against Him in combat),",
                    "चौधीं तबकीं शोर मचाइआ (filled all fourteen realms with cries of mourning), सिर नेज़े 'ते चाढ़आ ई (and mounted His sacred severed head upon the lance) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "हुसैन को तूने इमाम बनाया, फिर यज़ीद को उस पे चढ़ाया,",
                    "चौदह लोकों में मातम गूँजा, नेज़े पे पावन शीश चढ़ाया !",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "Thou raised Husain the Holy Imam, then against Him pitted Yazid’s spear;",
                    "All fourteen heavens mourned in grief, seeing His head on the lance appear!",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "मुग़लां ज़हर प्याले पीते, भूरियां वाले राजे कीते,  ",
                    "सभ असरफ़ फिरन चुप्प कीते, भला उहनां नूं झाड़िआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "hindi_gloss": [
                    "मुग़लां (शान-ओ-शौकत वाले मुगलों ने) ज़हर (अपनी पराजय के विष के) प्याले (प्याले) पीते (पी लिए), भूरियां (कंबलों/भूरी लोई) वाले (ओढ़ने वाले गरीब फकीरों और सिक्खों को तूने) राजे (राजा/शासक) कीते (बना दिया),",
                    "सभ (सारे बड़े-बड़े) असरफ़ (अशराफ़/कुलीन नवाब) फिरन (फिर रहे हैं) चुप्प (सहम कर चुपचाप) कीते (किए हुए), भला (कैसी अच्छी तरह) उहनां (उन अहंकारी अमीरों) नूं (को तूने) झाड़िआ (झाड़-पोंछ कर धूल चटा दी) ई (है) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "english_gloss": [
                    "मुग़लां ज़हर प्याले पीते (the mighty Mughals drank cups of bitter poison), भूरियां वाले राजे कीते (the humble blanket-wearers were crowned as kings),",
                    "सभ असरफ़ फिरन चुप्प कीते (the haughty aristocrats wander dumbstruck in silence), भला उहनां नूं झाड़िआ ई (how thoroughly hast thou swept them to the dust) ।",
                    "रहु रहु उए इश्का मारिआ ई ।"
                ],
                "poetic_hindi": [
                    "मुगलों ने विष के प्याले पिए, कंबल-वालों को राजा बनाया,",
                    "अमीरों की बोलती बंद हुई, क्या खूब सबक उनको सिखलाया !",
                    "ठहर जा ऐ इश्क, तूने सबको मार गिराया है !"
                ],
                "poetic_english": [
                    "The Mughal princes drank their bane; the blanket-wearers sat on thrones;",
                    "The haughty nobles wander mute, humbled amidst their ruined bones!",
                    "Hold, hold, O ruthless Love!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शाह फकीर विचारा, कर कर चल्या कूच नगारा,  ",
                    "रौशन जग्ग विच नाम हमारा, नूहों सरज उतारिआ ई ।  ",
                    "रहु रहु उए इश्का मारिआ ई ।  ",
                    "कहु किस नूं पार उतारिआ ई ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा शाह (बुल्ले शाह कहते हैं कि मैं तो) फकीर (एक दीन-अकिंचन फकीर) विचारा (बेचारा हूँ), कर (बजा-) कर (करके) चल्या (चल पड़ा हूँ अपने) कूच (महाप्रस्थान का) नगारा (नगाड़ा),",
                    "रौशन (परंतु सत्य के कारण अमर और प्रकाशमान हो गया है) जग्ग (संसार) विच (में) नाम (नाम) हमारा (हमारा), नूहों (जैसे जल-प्रलय से हज़रत नूह की कश्ती को तूने सकुशल) सरज (सृष्टि के तट पर) उतारिआ (उतार दिया) ई (तूने) ।",
                    "रहु (ठहर) रहु (ठहर जा) उए (अरे ओ) इश्का (क्रूर इश्क!) मारिआ (तूने तो सबको) ई (मार ही गिराया) । कहु (बता तो सही) किस (किस) नूं (को तूने) पार (पार) उतारिआ (उतारा) ई (है) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा शाह फकीर विचारा (Bulleh Shah is but a humble fakir), कर कर चल्या कूच नगारा (has sounded the departure drum for eternity),",
                    "रौशन जग्ग विच नाम हमारा (our name shines luminous throughout the cosmos), नूहों सरज उतारिआ ई (as Noah's ark was guided to the shore of life) ।",
                    "रहु रहु उए इश्का मारिआ ई (hold, hold, O ruthless Love! Thou hast struck down all: say, whom hast thou ferried across) ।"
                ],
                "poetic_hindi": [
                    "बुल्ला शाह दीन फकीर चला, कूच का डंका बजा कर प्यारा,",
                    "जग में नाम अमर हुआ मेरा, जैसे नूह को तट पे उतारा !",
                    "ठहर जा ऐ इश्क ! तूने सबको मार गिराया है,",
                    "ज़रा बता तो सही, तूने किसको सुख से पार लगाया है?"
                ],
                "poetic_english": [
                    "Poor Bulleh Shah, a mendicant soul, has beaten the drum to march away;",
                    "Our name shines bright across the world, like Noah's ark at dawn of day!",
                    "Hold, hold, O ruthless Love! Thou hast struck down all who dare;",
                    "Say, whom hast thou ever ferried across without torment and despair?"
                ]
            }
        ],
        "sufi_commentary": "यह 21 बंधों की काफी विश्व साहित्य में तुलनात्मक धार्मिक इतिहास और सूफी रहस्यवाद का एक अनुपम संगम है। इसमें सामी (सेमिटिक) परंपरा (आदम, नूह, इब्राहीम, मूसा, ईसा, यूसुफ, अय्यूब), भारतीय परंपरा (राम, सीता, हनुमान, रावण, कृष्ण, गोपियां, कंस, कौरव-पांडव महाभारत), सूफी इतिहास (मंसूर, शम्स तबरेज़ी, सरमद, शाह शरफ कलंदर, कर्बला में इमाम हुसैन), और पंजाबी लोकगाथाओं (हीर-रांझा, मिर्ज़ा-साहिबां, सस्सी-पुन्नूं, सोहणी-महीवाल, रोडा-जलाली) को एक ही धागे में पिरोया गया है। 20वें बंध में 18वीं शताब्दी के पंजाब की राजनीतिक उथल-पुथल ('मुगलों का पतन और कंबल ओढ़ने वाले सामान्य लोगों/सिक्खों का उदय') का ऐतिहासिक यथार्थ दर्ज है। यह काफी सिद्ध करती है कि ईश्वर का प्रेम केवल करुणा नहीं, बल्कि एक प्रलयंकारी अग्नि है जो आत्मा को कुंदन बनाने के लिए समस्त सांसारिक बंधनों को भस्म कर देती है।"
    },
    {
        "id": 127,
        "title": "रैन गई लटके (लुड़के) सभ तारे",
        "title_english": "The Night is Spent, the Stars Have Sunk Low: Awaken Now, O Dear Traveler!",
        "historical_context": "यह 5 बंधों की एक अत्यंत प्रसिद्ध और प्रेरणादायी जागृति-काफी है। इसमें जीवन की रात के बीतने और मृत्यु के प्रभात के आगमन का रूपक है। 'रैन गई' का अर्थ है कि आयु ढल चुकी है और जीवन रूपी तारे क्षितिज पर डूब रहे हैं। यह संसार एक सराय है जहाँ जन्म-मरण (आवागमन) के मुसाफिर डेरा डाले हुए हैं। जब कूच का नगाड़ा बज रहा है, तब भी मनुष्य अज्ञान की नींद में सो रहा है। बुल्ले शाह चेतावनी देते हैं कि साधना और शुभ कर्मों के बिना जीवन की यह अमूल्य खेती नष्ट हो जाएगी।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: रैन गई लटके सभ तारे)",
        "raga": "राग काफी / बिलावल / प्रभाती",
        "theme": "जीवन की नश्वरता, मृत्यु की सन्निकटता, आध्यात्मिक जागरण, आवागमन की सराय",
        "stanzas": [
            {
                "original": [
                    "रैन गई लटके (लुड़के) सभ तारे,  ",
                    "अब तो जाग मुसाफ़र प्यारे ।"
                ],
                "hindi_gloss": [
                    "रैन (आयु रूपी रात) गई (बीत गई है और) लटके/लुड़के (पश्चिम में डूब चले हैं) सभ (सारे) तारे (नक्षत्र और तारे),",
                    "अब (अब) तो (तो मोह-निद्रा से) जाग (जाग जा ऐ) मुसाफ़र (पथिक/मुसाफिर) प्यारे (प्यारे) ।"
                ],
                "english_gloss": [
                    "रैन गई (the night has passed away) लटके सभ तारे (all the stars have sunk low),",
                    "अब तो जाग (awaken now at least) मुसाफ़र प्यारे (O dear traveler) ।"
                ],
                "poetic_hindi": [
                    "रात बीत गई, तारे डूबे, अब तो जाग मुसाफिर प्यारे !",
                    "उड़ गया पंछी, ढली जवानी, किस उलझन में प्राण सँवारे?"
                ],
                "poetic_english": [
                    "The night is spent, the stars have sunk below the western sky;",
                    "Awaken now, O traveler dear, before thy life pass by!"
                ]
            },
            {
                "original": [
                    "आवागौन सराईं डेरे, साथ त्यार मुसाफर तेरे,  ",
                    "तैं ना सुण्यु कूच नगारे, अब तो जाग मुसाफ़र प्यारे ।"
                ],
                "hindi_gloss": [
                    "आवागौन (जन्म और मरण के इस) सराईं (सराय रूपी संसार में लगे हैं तेरे अस्थायी) डेरे (तम्बू और डेरे), साथ (सारे संगी-साथी) त्यार (प्रस्थान के लिए तैयार खड़े हैं) मुसाफर (यात्री) तेरे (तेरे),",
                    "तैं (तूने अभी तक) ना (नहीं) सुण्यु (सुना क्या मृत्यु के) कूच (प्रस्थान के बजते हुए) नगारे (नगाड़े को), अब (अब) तो (तो) जाग (जाग जा ऐ) मुसाफ़र (मुसाफिर) प्यारे (प्यारे) ।"
                ],
                "english_gloss": [
                    "आवागौन सराईं डेरे (encamped in this transit inn of transmigration), साथ त्यार मुसाफर तेरे (thy fellow-travelers are packed and ready),",
                    "तैं ना सुण्यु कूच नगारे (hast thou not heard the drums of departure), अब तो जाग मुसाफ़र प्यारे (awaken now, O dear traveler) ।"
                ],
                "poetic_hindi": [
                    "आवागमन की सराय में डेरे, साथी सब तैयार खड़े हैं,",
                    "कूच-नगाड़ा सुन न पाया, क्यों अज्ञान के फंद पड़े हैं?",
                    "अब तो जाग मुसाफिर प्यारे !"
                ],
                "poetic_english": [
                    "Encamped in transmigration's inn, thy comrades pack to go;",
                    "Hast thou not heard departure’s drum sounding its warning low?",
                    "Awaken now, O traveler dear!"
                ]
            },
            {
                "original": [
                    "कर लै अज्ज करनी दा बेरा, बहुड़ ना होसी आवन तेरा,  ",
                    "साथी चलो चल्ल पुकारे, अब तो जाग मुसाफ़र प्यारे ।"
                ],
                "hindi_gloss": [
                    "कर (तैयार कर) लै (ले) अज्ज (आज ही अपने शुभ) करनी (कर्मों की) दा (की मजबूत) बेरा (नाव/बेड़ा), बहुड़ (पुनः दोबारा) ना (नहीं) होसी (होगा इस मानव-देह में) आवन (आगमन) तेरा (तेरा),",
                    "साथी (सारे साथी) चलो (चलो!) चल्ल (चलो! की) पुकारे (पुकार लगा रहे हैं), अब (अब) तो (तो) जाग (जाग जा) मुसाफ़र प्यारे (मुसाफिर प्यारे) ।"
                ],
                "english_gloss": [
                    "कर लै अज्ज करनी दा बेरा (build today the strong boat of righteous deeds), बहुड़ ना होसी आवन तेरा (never again wilt thou return to this human birth),",
                    "साथी चलो चल्ल पुकारे (thy companions cry 'Depart! Depart!'), अब तो जाग मुसाफ़र प्यारे (awaken now, O dear traveler) ।"
                ],
                "poetic_hindi": [
                    "आज ही बाँध ले सुकृत की नैया, फिर न मिलेगा जनम दोबारा,",
                    "साथी सब 'चलो-चलो' पुकारें, छोड़ चला संसार किनारा !",
                    "अब तो जाग मुसाफिर प्यारे !"
                ],
                "poetic_english": [
                    "Fashion today the boat of righteous deeds while strength remains in hand;",
                    "Never again shalt thou return to walk this earthly land!",
                    "Awaken now, O traveler dear!"
                ]
            },
            {
                "original": [
                    "क्या सरधन क्या निरधन पौड़े, आपने आपने देश को दौड़े,  ",
                    "लद्धा नाम लै ल्यो सभारे, अब तो जाग मुसाफ़र प्यारे ।"
                ],
                "hindi_gloss": [
                    "क्या (चाहे कोई) सरधन (धनवान/समृद्ध हो) क्या (या चाहे) निरधन (निर्धन-कंगाल हो, सब मृत्यु की शय्या पर) पौड़े (सो गए हैं), आपने (अपने-) आपने (अपने वास्तविक पारलौकिक) देश (देश) को (की ओर) दौड़े (दौड़ पड़े हैं सब),",
                    "लद्धा (जो अनमोल) नाम (ईश्वरीय नाम प्राप्त हुआ है उसे) लै (ले) ल्यो (लो और अपने हृदय में) सभारे (संभाल कर संचित कर लो), अब (अब) तो (तो) जाग (जाग जा ऐ) मुसाफ़र प्यारे (मुसाफिर प्यारे) ।"
                ],
                "english_gloss": [
                    "क्या सरधन क्या निरधन पौड़े (both the wealthy and the destitute have lain down in death), आपने आपने देश को दौड़े (hastening unto their own eternal homeland),",
                    "लद्धा नाम लै ल्यो सभारे (cherish and safeguard the precious Name found by grace), अब तो जाग मुसाफ़र प्यारे (awaken now, O dear traveler) ।"
                ],
                "poetic_hindi": [
                    "क्या धनवान और क्या निर्धन, सब अपने वतन को भागे,",
                    "पाया हुआ प्रभु-नाम संभालो, जो सोए हैं सोई जागे !",
                    "अब तो जाग मुसाफिर प्यारे !"
                ],
                "poetic_english": [
                    "Both prince and pauper sleep in dust, sped to their native home;",
                    "Treasure the holy Name received, and cease through wastes to roam!",
                    "Awaken now, O traveler dear!"
                ]
            },
            {
                "original": [
                    "मोती चूनी पारस पासे, पास समुन्दर मरो प्यासे,  ",
                    "खोल्ह अक्खीं उट्ठ बहु भिकारे, अब तो जाग मुसाफ़र प्यारे ।  ",
                    "बुल्ल्हआ शौह दी पैरीं पड़ीए, ग़फ़लत छोड़ कुझ हीला करीए,  ",
                    "मिरग जतन बिन खेत उजाड़े, अब तो जाग मुसाफ़र प्यारे ।"
                ],
                "hindi_gloss": [
                    "मोती (तेरे अंतःकरण में मोती,) चूनी (माणिक्य) पारस (और पारस-मणि तेरे ही) पासे (पास विद्यमान है), पास (अमृत का) समुन्दर (समुद्र पास होते हुए भी तू अज्ञान से) मरो (मर रहा है) प्यासे (प्यासा),",
                    "खोल्ह (खोल अपनी) अक्खीं (आँखें और) उट्ठ (उठकर) बहु (बैठ जा ऐ) भिकारे (भिखारी/साधक), अब (अब) तो (तो) जाग (जाग जा ऐ) मुसाफ़र प्यारे (मुसाफिर प्यारे) ।",
                    "बुल्ल्हआ (बुल्ले शाह कहते हैं) शौह (परम प्रियतम सद्गुरु) दी (के) पैरीं (चरणों में) पड़ीए (समर्पित हो जा), ग़फ़लत (अज्ञान और प्रमाद को) छोड़ (छोड़कर) कुझ (कुछ तो आत्म-कल्याण का) हीला (यत्न) करीए (कर ले),",
                    "मिरग (अन्यथा वासना का चंचल मृग) जतन (बिना यत्न और रखवाली के जीवन का सारा) बिन (बिना) खेत (खेत) उजाड़े (उजाड़ कर नष्ट कर देगा), अब (अब) तो (तो) जाग (जाग जा ऐ) मुसाफ़र प्यारे (मुसाफिर प्यारे) ।"
                ],
                "english_gloss": [
                    "मोती चूनी पारस पासे (pearls, rubies, and the Philosopher's stone are right beside thee), पास समुन्दर मरो प्यासे (beside an ocean of nectar thou diest of thirst),",
                    "खोल्ह अक्खीं उट्ठ बहु भिकारे (open thine eyes and sit up, O beggar-seeker), अब तो जाग मुसाफ़र प्यारे (awaken now, O dear traveler) ।",
                    "बुल्ल्हआ शौह दी पैरीं पड़ीए (Bulleh: fall at the feet of the Sovereign King), ग़फ़लत छोड़ कुझ हीला करीए (forsake heedlessness and make spiritual effort),",
                    "मिरग जतन बिन खेत उजाड़े (without vigil, the wild deer of desire will ravage thy crop), अब तो जाग मुसाफ़र प्यारे (awaken now, O dear traveler) ।"
                ],
                "poetic_hindi": [
                    "पास में मोती, माणिक, पारस, सागर तीरे प्यासा मरे,",
                    "खोल नयन, उठ बैठ भिखारी, क्यों अज्ञान में आहें भरे?",
                    "बुल्ला कहे: सतगुरु पग पड़िए, छोड़ प्रमाद कुछ यत्न करिए,",
                    "चंचल हिरन खेत चर जाएगा, अब तो जाग मुसाफिर प्यारे !"
                ],
                "poetic_english": [
                    "Rubies and pearls are in thy grasp; beside the sea thou diest of thirst;",
                    "Open thine eyes, O beggar soul, and shake off this deep slumber cursed!",
                    "Says Bulleh: Fall at the Master’s feet, cast heedless folly to the wind;",
                    "Without thy vigil, wild beasts will strip the harvest of thy mind!",
                    "Awaken now, O traveler dear, before thy life pass by!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी कबीर के प्रसिद्ध पद 'जाग रे जमदूत आया' और फरीद के 'फरीदा पिछल रात न जागियों' की परंपरा का शिखर है। बुल्ले शाह मनुष्य को समझाते हैं कि यह संसार कोई स्थायी घर नहीं, बल्कि एक 'सराय' (विश्रामगृह) है जहाँ विभिन्न दिशाओं से आए यात्री केवल रात बिताने के लिए रुकते हैं और भोर होते ही प्रस्थान कर जाते हैं। 'मोती चूनी पारस पासे' आत्मज्ञान की ओर संकेत करता है: ईश्वर-रूपी पारस मनुष्य के अपने हृदय में है, परंतु वह कस्तूरी-मृग की भांति बाहर भटक कर प्यासा मर रहा है। वासना रूपी हिरन यदि जीवन-खेत को चर गया तो अंत में केवल पश्चाताप ही शेष रहेगा।"
    },
    {
        "id": 128,
        "title": "रांझा जोगीड़ा बण आया",
        "title_english": "Ranjha Has Arrived Having Become a Yogi: Wondrous is the Guise the Actor Plays!",
        "historical_context": "यह 4 बंधों की एक अत्यंत आनंदमयी, रूपकात्मक और शास्त्रीय काफी है। इसमें रांझा (परमेश्वर/शाह इनायत) हीर (आत्मा) के द्वार पर जोगी का भेष धारण करके भिक्षा मांगने आता है। बुल्ले शाह परमात्मा को एक कुशल 'सांगी' (स्वाँग रचने वाला अभिनेता) कहते हैं जो विश्व-रंगमंच पर नाना रूप धरता है। इस जोगी के नयन प्यालों जैसे हैं जो बाज़ की भांति दिल का शिकार करते हैं। कानों में मुंद्राएं, गले में माला और मुखड़ा हज़रत यूसुफ जैसा अनुपम है। यह वही परमात्मा है जिसने 'अलफ़' (अलिफ़) से 'अहद' (अकेला/अद्वैत) का रूप धारण किया है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: रांझा जोगीड़ा बण आया)",
        "raga": "राग काफी / जोग / बिलावल",
        "theme": "जोगी रांझा, परमात्मा का सांगी रूप, अलिफ़ से अहद, आत्म-समर्पण",
        "stanzas": [
            {
                "original": [
                    "रांझा जोगीड़ा बण आया ।  ",
                    "वाह सांगी सांग रचाइआ ।"
                ],
                "hindi_gloss": [
                    "रांझा (मेरा प्राण-प्यारा रांझा साक्षात्) जोगीड़ा (जोगी/वैरागी) बण (बनकर द्वारे पर) आया (आ पहुँचा है) ।",
                    "वाह (धन्य है वह) सांगी (स्वांग रचने वाला नटवर प्रभु, जिसने कैसा अद्भुत) सांग (जोगी का स्वांग/रूप) रचाइआ (रच लिया है) ।"
                ],
                "english_gloss": [
                    "रांझा जोगीड़ा बण आया (Ranjha has arrived having transformed into a Yogi) ।",
                    "वाह सांगी सांग रचाइआ (wondrous is the player who has staged this marvelous play) ।"
                ],
                "poetic_hindi": [
                    "रांझा जोगिया बन कर आया, धन्य है वो नटवर मतवाला,",
                    "कैसा अद्भुत रूप रचाया, कानों में मुंद्राएं डाला !"
                ],
                "poetic_english": [
                    "Ranjha has arrived as a Yogi, entering my humble door;",
                    "Wondrous is the Master Player who stages this divine lore!"
                ]
            },
            {
                "original": [
                    "एस जोगी दे नैन कटोरे, बाज़ां वांङू लैंदे डोरे,  ",
                    "मुक्ख डिठ्यां दुक्ख जावन झोरे, इन्हां अक्खियां लाल वंजाइआ ।  ",
                    "रांझा जोगीड़ा बण आया ।"
                ],
                "hindi_gloss": [
                    "एस (इस अद्भुत) जोगी (जोगी) दे (के) नैन (नेत्र प्रेम-अमृत से भरे) कटोरे (कटोरे जैसे विशाल हैं), बाज़ां (शिकारी बाज़ों की) वांङू (भांति) लैंदे (लेते हैं वे दिल पर प्रेम के) डोरे (तीखे झपट्टे),",
                    "मुक्ख (उसका मुखड़ा) डिठ्यां (देखते ही सारे) दुक्ख (दुख और विरह के) जावन (दूर हो जाते हैं) झोरे (संताप), इन्हां (इन मोहिनी) अक्खियां (अंखियों ने तो मेरा) लाल (लाल/रत्न जैसा दिल) वंजाइआ (लूट/मोहित कर लिया) ।",
                    "रांझा जोगीड़ा बण आया ।"
                ],
                "english_gloss": [
                    "एस जोगी दे नैन कटोरे (the eyes of this Yogi are chalices brimful), बाज़ां वांङू लैंदे डोरे (casting glances like diving falcons),",
                    "मुक्ख डिठ्यां दुक्ख जावन झोरे (beholding His face all sorrows and griefs vanish), इन्हां अक्खियां लाल वंजाइआ (these enchanting eyes have plundered my ruby heart) ।",
                    "रांझा जोगीड़ा बण आया ।"
                ],
                "poetic_hindi": [
                    "नयन कटोरे जैसे बाज़ झपटते, लूट लिया दिल का हर कोना,",
                    "मुखड़ा देखते दुख सब भागे, जादू कर गया नटवर सलोना !",
                    "रांझा जोगिया बन कर आया !"
                ],
                "poetic_english": [
                    "His eyes are brimming chalices that hunt like falcons in their flight;",
                    "Beholding His visage, all sorrows flee, overwhelmed in pure delight!",
                    "Ranjha has arrived as a Yogi!"
                ]
            },
            {
                "original": [
                    "एस जोगी दी की निशानी, कन्न विच मुन्दरां गल विच गानी,  ",
                    "सूरत इस दी यूसफ़ सानी, एस अलफ़ों आहद बणाइआ ।  ",
                    "रांझा जोगीड़ा बण आया ।"
                ],
                "hindi_gloss": [
                    "एस (इस दिव्य) जोगी (जोगी) दी (की) की (क्या सुंदर) निशानी (पहचान है), कन्न (कानों) विच (में) मुन्दरां (जोग की मुंद्राएं हैं और) गल (गले) विच (में प्रेम की) गानी (कंठी/माला है),",
                    "सूरत (इसकी मुख-छवि) इस (इसकी) दी (तो साक्षात् हज़रत) यूसफ़ (यूसुफ की) सानी (सानी/समान अद्वितीय सुंदर है), एस (इसी परमात्मा ने) अलफ़ों (अलिफ़ से स्वयं को) आहद (अहद/अकेला अद्वैत ब्रह्म) बणाइआ (बनाया है) ।",
                    "रांझा जोगीड़ा बण आया ।"
                ],
                "english_gloss": [
                    "एस जोगी दी की निशानी (what is the mark of this Yogi), कन्न विच मुन्दरां गल विच गानी (rings in His ears, a necklace round His throat),",
                    "सूरत इस दी यूसफ़ सानी (His countenance outshines Joseph in beauty), एस अलफ़ों आहद बणाइआ (from Alif He fashioned Ahad, the Sole One) ।",
                    "रांझा जोगीड़ा बण आया ।"
                ],
                "poetic_hindi": [
                    "कानों में मुंद्रा, गले में माला, रूप है यूसुफ जैसा प्यारा,",
                    "अलिफ़ से अहद बना वो साहिब, जिसने जग को रूप संवारा !",
                    "रांझा जोगिया बन कर आया !"
                ],
                "poetic_english": [
                    "Rings in His ears, a necklace round His neck, His visage fair as Joseph's face;",
                    "From Alif He shaped the Sole Ahad, radiating uncreated grace!",
                    "Ranjha has arrived as a Yogi!"
                ]
            },
            {
                "original": [
                    "रांझा जोगी ते मैं जोगयानी, इस दी खातर भरसां पाणी,  ",
                    "एवें पिछली उमर वेहाणी, एस हुन मैनूं भरमाइआ ।  ",
                    "रांझा जोगीड़ा बण आया ।"
                ],
                "hindi_gloss": [
                    "रांझा (यदि रांझा) जोगी (जोगी है) ते (तो) मैं (मैं उसकी समर्पित) जोगयानी (जोगन हूँ), इस (इस प्रियतम) दी (की) खातर (खातिर मैं दासियों की तरह) भरसां (भरूँगी) पाणी (पानी),",
                    "एवें (व्यर्थ ही मेरी) पिछली (पूर्व की सारी) उमर (आयु संसार में) वेहाणी (बीत गई थी), एस (इस प्यारे जोगी ने) हुन (अब) मैनूं (मुझको अपने प्रेम में) भरमाइआ (मोहित/रीझा लिया है) ।",
                    "रांझा जोगीड़ा बण आया ।"
                ],
                "english_gloss": [
                    "रांझा जोगी ते मैं जोगयानी (Ranjha is the Yogi and I His Yogini), इस दी खातर भरसां पाणी (for His sake I shall draw water like a servant),",
                    "एवें पिछली उमर वेहाणी (in vain my past life was squandered), एस हुन मैनूं भरमाइआ (now He has enchanted me in His love) ।",
                    "रांझा जोगीड़ा बण आया ।"
                ],
                "poetic_hindi": [
                    "रांझा जोगी, मैं जोगन उसकी, भरूँगी पानी उसके द्वारे,",
                    "पिछली उमर तो व्यर्थ गँवाई, अब तो सुध-बुध हारी प्यारे !",
                    "रांझा जोगिया बन कर आया !"
                ],
                "poetic_english": [
                    "Ranjha is the Yogi, His Yogini am I; for His sake I will draw the well;",
                    "My past years drifted in empty vanity, till bound beneath His holy spell!",
                    "Ranjha has arrived as a Yogi!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु दी इह गत बणाई, प्रीत पुरानी शोर मचाई,  ",
                    "इह गल्ल कीकूं छुपे छुपाई, नी तख़त हज़ार्युं धाइआ ।  ",
                    "रांझा जोगीड़ा बण आया ।  ",
                    "वाह सांगी सांग रचाइआ ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ले शाह कहते हैं) शहु (परमेश्वर ने) दी (की) इह (यह प्रेम की अद्भुत) गत (दशा) बणाई (बना दी है), प्रीत (हमारी जन्म-जन्मांतरों की) पुरानी (पुरातन प्रीत ने) शोर (सारा भेद) मचाई (प्रकट कर दिया है),",
                    "इह (यह पावन) गल्ल (सत्य की बात) कीकूं (कैसे भला) छुपे छुपाई (छिपाए से छिप सकती है), नी (जब वह स्वयं) तख़त हज़ार्युं (तख्त हजारे के सिंहासन से मेरी ओर) धाइआ (दौड़ा चला आया है) ।",
                    "रांझा जोगीड़ा बण आया । वाह सांगी सांग रचाइआ ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा शहु दी इह गत बणाई (Bulleh: such is the state wrought by the Sovereign Lord), प्रीत पुरानी शोर मचाई (ancient love raised its proclaimed shout),",
                    "इह गल्ल कीकूं छुपे छुपाई (how can this truth remain concealed), नी तख़त हज़ार्युं धाइआ (when He sped from Takht Hazara to my door) ।",
                    "रांझा जोगीड़ा बण आया । वाह सांगी सांग रचाइआ ।"
                ],
                "poetic_hindi": [
                    "बुल्ला कहे: साहिब की महिमा, पुरानी प्रीत ने शोर मचाया,",
                    "कैसे छिपे यह प्रेम का दरिया, जो तख्त हजारे से दौड़ा आया !",
                    "रांझा जोगिया बन कर आया, धन्य है वो नटवर मतवाला,",
                    "कैसा अद्भुत रूप रचाया !"
                ],
                "poetic_english": [
                    "Says Bulleh: Wondrous is the Sovereign’s sport; ancient love cries aloud its claim;",
                    "How can this secret remain concealed, when from Takht Hazara speeding He came?",
                    "Ranjha has arrived as a Yogi, entering my humble door;",
                    "Wondrous is the Master Player who stages this divine lore!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी सूफी 'तजल्ली' (ईश्वरीय प्रकटीकरण) का अनुपम उदाहरण है। परमात्मा निराकार होते हुए भी प्रेम की खातिर साकार रूप धारण करता है—'एस अलफ़ों आहद बणाइआ'। भारतीय नाथ-योग परंपरा के बाह्य प्रतीकों (मुंद्रा, गानी, भिक्षा) को बुल्ले शाह ने ईश्वर के अवतार और कृपा के रूप में स्वीकार किया है। आत्मा (हीर) अपने समस्त अहंकार को त्यागकर जोगी की 'जोगन' बन जाती है और उसके लिए पानी भरने को अपना परम सौभाग्य मानती है।"
    },
    {
        "id": 129,
        "title": "रांझा रांझा करदी नी मैं आपे रांझा होई",
        "title_english": "Repeating 'Ranjha, Ranjha!', O Sisters, I Myself Became Ranjha!",
        "historical_context": "यह बाबा बुल्ले शाह की विश्व-प्रसिद्ध, कालजयी और सर्वाधिक गाई जाने वाली अमर काफी है। यह सूफी फना-फिल-महबूब (प्रियतम में अहंकार का पूर्ण लोप) और भारतीय अद्वैत वेदांत के 'सोऽहम्' (वही मैं हूँ) का सर्वोच्च काव्यात्मक शिखर है। हीर निरंतर रांझा के नाम का जप करते-करते अपनी देह-चेतना और स्त्री-अहंकार को खो देती है और स्वयं रांझा बन जाती है। वह कहती है कि अब मुझे हीर मत कहो, मुझे 'धीदो रांझा' कहो! रांझा मुझमें है और मैं रांझा में हूँ, अब कोई दूसरा विचार शेष नहीं रहा। हाथ में लाठी, आगे गायों का झुंड और कंधे पर भूरी कम्बल—हीर पूर्णतः रांझा के स्वरूप में रूपांतरित हो चुकी है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: रांझा रांझा करदी)",
        "raga": "राग काफी / बिलावल / पहाड़ी",
        "theme": "अद्वैत का शिखर, फना-फिल-महबूब, 'सोऽहम्' की अनुभूति, द्वैत का पूर्ण विनाश",
        "stanzas": [
            {
                "original": [
                    "रांझा रांझा करदी नी मैं आपे रांझा होई ।  ",
                    "सद्दो नी मैनूं धीदो रांझा, हीर ना आखो कोई ।"
                ],
                "hindi_gloss": [
                    "रांझा (रांझा) रांझा ('रांझा-रांझा') करदी (जपते-जपते) नी (हे सखी) मैं (मैं स्वयं ही) आपे (स्वयं ही) रांझा (रांझा) होई (बन गई हूँ) ।",
                    "सद्दो (पुकारो) नी (अरी सखियो) मैनूं (मुझको तुम) धीदो (धीदो) रांझा (रांझा कहकर पुकारो), हीर (हीर) ना (मत) आखो (कहो) कोई (कोई भी मुझे अब) ।"
                ],
                "english_gloss": [
                    "रांझा रांझा करदी (chanting 'Ranjha, Ranjha!') नी मैं (O sisters, I) आपे रांझा होई (myself have become Ranjha) ।",
                    "सद्दो नी मैनूं (call me now) धीदो रांझा (Dheedo Ranjha), हीर ना आखो कोई (let no one call me Heer any more) ।"
                ],
                "poetic_hindi": [
                    "'रांझा-रांझा' करती री सखी, मैं आपे रांझा होई,",
                    "पुकारो अब मुझे 'धीदो रांझा', हीर न आखो कोई !"
                ],
                "poetic_english": [
                    "Repeating 'Ranjha, Ranjha!', O sisters, I myself became Ranjha whole;",
                    "Call me 'Dheedo Ranjha' now, let no one call me Heer in soul!"
                ]
            },
            {
                "original": [
                    "रांझा मैं विच्च मैं रांझे विच्च, होर ख़्याल ना कोई ।  ",
                    "मैं नहीं उह आप है, आपनी आप करे दिलजोई ।  ",
                    "रांझा रांझा करदी नी मैं आपे रांझा होई ।"
                ],
                "hindi_gloss": [
                    "रांझा (मेरा रांझा) मैं (मेरे) विच्च (भीतर समाया है और) मैं (मैं स्वयं) रांझे (रांझा के अस्तित्व के) विच्च (भीतर समा गई हूँ), होर (अन्य कोई) ख़्याल (विचार या द्वैत का संशय) ना (नहीं रहा) कोई (कोई भी),",
                    "मैं (अब 'मैं' नाम की कोई सत्ता) नहीं (नहीं बची), उह (वह परमात्मा ही) आप (स्वयं) है (विराजमान है), आपनी (अपनी ही आत्मा की) आप (वह स्वयं ही) करे (कर रहा है) दिलजोई (तसल्ली और प्रेम-क्रीड़ा) ।",
                    "रांझा (रांझा) रांझा (रांझा) करदी (करती) नी (अरी) मैं (मैं) आपे (स्वयं) रांझा (रांझा) होई (हो गई) ।"
                ],
                "english_gloss": [
                    "रांझा मैं विच्च (Ranjha is in me) मैं रांझे विच्च (and I am in Ranjha), होर ख़्याल ना कोई (no other thought remains),",
                    "मैं नहीं (I exist no more) उह आप है (He Himself is), आपनी आप करे दिलजोई (He comforts His own self in love) ।",
                    "रांझा रांझा करदी नी मैं आपे रांझा होई (chanting 'Ranjha, Ranjha!' I became Ranjha) ।"
                ],
                "poetic_hindi": [
                    "रांझा मुझमें, मैं रांझे में, दूजा ख्याल न कोई,",
                    "मैं न रही, वो खुद ही बैठा, अपनी प्रीत संजोई !",
                    "'रांझा-रांझा' करती री सखी, मैं आपे रांझा होई !"
                ],
                "poetic_english": [
                    "Ranjha is in me, and I in Ranjha; no second thought remains in sight;",
                    "I am no more, He solely is, comforting His own heart in light!",
                    "Repeating 'Ranjha, Ranjha!', O sisters, I myself became Ranjha whole!"
                ]
            },
            {
                "original": [
                    "हत्थ खूंडी मेरे अग्गे मंगू, मोढे भूरा लोई ।  ",
                    "बुल्ल्हा हीर सलेटी वेखो, कित्थे जा खलोई ।  ",
                    "रांझा रांझा करदी नी मैं आपे रांझा होई ।  ",
                    "सद्दो नी मैनूं धीदो रांझा, हीर ना आखो कोई ।"
                ],
                "hindi_gloss": [
                    "हत्थ (हाथ में चरवाहे की) खूंडी (लाठी है) मेरे (और मेरे) अग्गे (आगे गायों-भैंसों का) मंगू (झुंड चल रहा है), मोढे (कंधे पर मेरे) भूरा (काले-भूरे ऊन की) लोई (कम्बल ओढ़ रखी है),",
                    "बुल्ल्हा (बुल्ले शाह कहते हैं) हीर (हीर) सलेटी (सलेटी को) वेखो (ज़रा देखो तो सही कि), कित्थे (कहाँ किस अद्वैत के शिखर पर) जा (जाकर) खलोई (खड़ी हो गई है वह) ।",
                    "रांझा (रांझा) रांझा (रांझा) करदी (करती) नी (अरी सखी) मैं (मैं) आपे (स्वयं ही) रांझा (रांझा) होई (बन गई हूँ) । सद्दो (पुकारो) नी (अरी) मैनूं (मुझको) धीदो (धीदो) रांझा (रांझा), हीर (हीर) ना (मत) आखो (कहो) कोई (कोई भी) ।"
                ],
                "english_gloss": [
                    "हत्थ खूंडी (crook in hand) मेरे अग्गे मंगू (the herd of cattle before me), मोढे भूरा लोई (the coarse dark blanket over my shoulder),",
                    "बुल्ल्हा हीर सलेटी वेखो (Bulleh: behold Heer Saleti), कित्थे जा खलोई (where she has come to stand at last) ।",
                    "रांझा रांझा करदी नी मैं आपे रांझा होई (repeating 'Ranjha, Ranjha!' I myself became Ranjha) । सद्दो नी मैनूं धीदो रांझा, हीर ना आखो कोई (call me Dheedo Ranjha, let no one call me Heer) ।"
                ],
                "poetic_hindi": [
                    "हाथ में लाठी, आगे गोधन, कांधे कम्बल सोहे,",
                    "बुल्ला कहे: सलेटी हीर देखो, किस पदवी पे मोहे !",
                    "'रांझा-रांझा' करती री सखी, मैं आपे रांझा होई,",
                    "पुकारो अब मुझे 'धीदो रांझा', हीर न आखो कोई !"
                ],
                "poetic_english": [
                    "Staff in my hand, the grazing herd before me, the rustic blanket on my arm;",
                    "Bulleh proclaims: Behold Heer Saleti, crowned with non-dual charm!",
                    "Repeating 'Ranjha, Ranjha!', O sisters, I myself became Ranjha whole;",
                    "Call me 'Dheedo Ranjha' now, let no one call me Heer in soul!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी सूफी साहित्य और विश्व की रहस्यवादी कविता का एक जादुई शिखर है। 'रांझा रांझा करदी नी मैं आपे रांझा होई' उस मनोवैज्ञानिक और आध्यात्मिक प्रक्रिया का सजीव चित्रण है जिसे पतंजलि योगसूत्र में 'समापत्ति' (ध्येय में ध्याता का लीन होना), वेदांत में 'तत्त्वमसि' और तसव्वुफ में 'फना-फिल-महबूब' कहा जाता है। जब साधक अहर्निश परमात्मा का स्मरण करता है, तो उसका सीमित देह-बोध और सांसारिक नाम ('हीर') विलीन हो जाता है। वह केवल प्रियतम ('धीदो रांझा') के रूप में ही अनुभव करता है। 'मैं नहीं उह आप है' का अर्थ है कि कर्ता और भोक्ता का द्वैत मिट चुका है; परमात्मा ही अपने स्वरूप में अपनी ही महिमा का साक्षात्कार कर रहा है।"
    },
    {
        "id": 130,
        "title": "रोज़े हज्ज निमाज़ नी माए",
        "title_english": "Fasts, Hajj, and Ritual Prayers, O Mother: My Beloved Came and Made Me Forget Them All!",
        "historical_context": "यह 3 बंधों की एक अत्यंत आनंदमयी और क्रांतिकारी काफी है। जब आत्मा के अंतःकरण में प्रियतम का साक्षात दीदार हो जाता है, तो बाह्य धार्मिक औपचारिकताएं—रोज़े, हज और नमाज़—स्वतः विस्मृत हो जाती हैं। तर्कशास्त्र ('मंतक') और व्याकरण ('नहव') का शुष्क ज्ञान अनहद नाद के मधुर संगीत में बह जाता है। जब परमात्मा साधक के घर में पधारता है, तो शरिया के सारे कानूनी नियम पीछे छूट जाते हैं क्योंकि अब साधक को सृष्टि के प्रत्येक रूप ('हर मज़हर') में केवल वही एक प्रियतम दिखाई देता है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: रोज़े हज्ज निमाज़ नी माए)",
        "raga": "राग काफी / बिलावल",
        "theme": "साक्षात्कार के बाद कर्मकांडों की विस्मृति, अनहद नाद, हर मज़हर में ईश्वर का दीदार",
        "stanzas": [
            {
                "original": [
                    "रोज़े हज्ज निमाज़ नी माए,  ",
                    "मैनूं पिया ने आण भुलाए ।"
                ],
                "hindi_gloss": [
                    "रोज़े (रोज़े) हज्ज (हज की यात्रा) निमाज़ (और औपचारिक नमाज़ें) नी (हे) माए (मेरी प्यारी माँ),",
                    "मैनूं (मुझको मेरे प्यारे) पिया (प्रियतम ने) ने (ने आकर) आण (आकर अपने प्रेम में) भुलाए (विस्मृत करवा दिए हैं) ।"
                ],
                "english_gloss": [
                    "रोज़े हज्ज निमाज़ (fasts, Hajj, and formal prayers) नी माए (O mother mine),",
                    "मैनूं पिया ने आण भुलाए (my Beloved came and made me forget them all) ।"
                ],
                "poetic_hindi": [
                    "रोज़े, हज और नमाज़ें ओ माँ, सब प्रियतम ने आकर भुलाए,",
                    "जब से साहिब ने दरस दिखाया, मन में दिव्य अनहद मुस्काए !"
                ],
                "poetic_english": [
                    "Fasts, Hajj, and formal prayers, O mother mine;",
                    "My Beloved came and dissolved them in wine divine!"
                ]
            },
            {
                "original": [
                    "जां पिया दियां ख़बरां आईआं, मंतक नहव सभ्भे भुल्ल गईआं,  ",
                    "उस अनहद तार वजाए, रोज़े हज्ज निमाज़ नी माए ।"
                ],
                "hindi_gloss": [
                    "जां (जब से) पिया (प्रियतम के पावन आगमन) दियां (की मधुर) ख़बरां (खबरें) आईआं (आई हैं), मंतक (तर्कशास्त्र) नहव (और अरबी व्याकरण के) सभ्भे (सारे नियम) भुल्ल (विस्मृत हो) गईआं (गए हैं),",
                    "उस (उसने मेरे अंतःकरण में) अनहद (अनाहत नाद की दिव्य) तार (तारें) वजाए (बजा दी हैं), रोज़े (रोज़े) हज्ज (हज) निमाज़ (और नमाज़ें) नी (अरी) माए (माँ उसने भुला दी हैं) ।"
                ],
                "english_gloss": [
                    "जां पिया दियां ख़बरां आईआं (when the tidings of the Beloved arrived), मंतक नहव सभ्भे भुल्ल गईआं (logic and grammar were all forgotten),",
                    "उस अनहद तार वजाए (He struck the chords of the Unstruck Sound), रोज़े हज्ज निमाज़ नी माए (fasts, Hajj, and prayers, O mother mine) ।"
                ],
                "poetic_hindi": [
                    "प्रियतम की जब खबरें आईं, तर्क और व्याकरण भूल गईं,",
                    "अनहद की जब तारें बजीं, प्रेम-सुधा में सुरति घुल गईं !",
                    "रोज़े, हज और नमाज़ें ओ माँ !"
                ],
                "poetic_english": [
                    "When tidings of the Beloved reached my ear, logic and grammar fled away;",
                    "He struck the chords of the Anhad lute, turning the dark to heavenly day!",
                    "Fasts, Hajj, and formal prayers, O mother mine!"
                ]
            },
            {
                "original": [
                    "जां पिया मेरे घर आया, भुल्ल गया मैनूं शर्हा वकाइआ,  ",
                    "हर मुज़हर विच ऊहा दिसदा, अन्दर बाहर जलवा जिसदा,  ",
                    "लोकां खबर ना काए, रोज़े हज्ज निमाज़ नी माए ।"
                ],
                "hindi_gloss": [
                    "जां (जब मेरा) पिया (प्रियतम) मेरे (मेरे) घर (हृदय-गृह में) आया (पधार चुका), भुल्ल (विस्मृत हो) गया (गया) मैनूं (मुझको) शर्हा (रूढ़िवादी शरिया का) वकाइआ (सारा कानूनी बखेड़ा),",
                    "हर (प्रत्येक) मुज़हर (प्रकटीकरण/जीव) विच (के भीतर) ऊहा (वही परमात्मा) दिसदा (दिखाई दे रहा है), अन्दर (हृदय के भीतर और) बाहर (बाहर संसार में) जलवा (साक्षात् दिव्य तेज है) जिसदा (जिसका),",
                    "लोकां (अज्ञानी लोगों को इसकी) खबर (कोई भी खबर) ना (नहीं है) काए (कोई भी), रोज़े (रोज़े) हज्ज (हज) निमाज़ (और नमाज़) नी (हे) माए (माँ मेरे पिया ने भुला दी है) ।"
                ],
                "english_gloss": [
                    "जां पिया मेरे घर आया (when the Beloved entered my home), भुल्ल गया मैनूं शर्हा वकाइआ (I forgot all legalistic codes of the outer Law),",
                    "हर मुज़हर विच ऊहा दिसदा (in every manifest form He alone is beheld), अन्दर बाहर जलवा जिसदा (whose splendor radiates within and without),",
                    "लोकां खबर ना काए (of this the blind world has no inkling), रोज़े हज्ज निमाज़ नी माए (fasts, Hajj, and prayers, O mother mine) ।"
                ],
                "poetic_hindi": [
                    "पिया जब मेरे आँगन आया, शरिया का सब फेर मिटाया,",
                    "हर रूप में वही दिखता है, जिसका नूर घट-घट में छाया !",
                    "संसार को इसकी खबर नहीं, उसने सब कर्मकांड भुलाए,",
                    "रोज़े, हज और नमाज़ें ओ माँ, सब प्रियतम ने आकर भुलाए !"
                ],
                "poetic_english": [
                    "When my Beloved walked into my room, all legalistic codes were dead;",
                    "In every manifest form He shines, within and without His glory shed!",
                    "Of this the blind world has no heed, wandering in ritual forms apart:",
                    "Fasts, Hajj, and formal prayers, O mother mine, were washed forever from my heart!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी सूफी रहस्यवाद के उस बुनियादी सत्य का प्रतिपादन करती है जहाँ साधन साध्य में लीन हो जाता है। रोज़े, नमाज़ और हज परमात्मा तक पहुँचने के साधन हैं। जब साक्षात् परमात्मा ही साधक के हृदय-गृह में प्रविष्ट हो जाता है, तो साधनों का प्रयोजन स्वतः समाप्त हो जाता है। 'हर मुज़हर विच ऊहा दिसदा' (हर प्रकटीकरण में वही दिखता है) सूफी सर्वेश्वरवाद की पराकाष्ठा है। जब कण-कण में परमात्मा का जलवा दृष्टिगोचर होने लगे, तो किसी विशेष दिशा (किबला) की ओर झुकने या विशेष समय पर इबादत करने की सीमाएं तिरोहित हो जाती हैं।"
    }
]

new_lexicon_terms = {
    "कणकों": {"hindi": "गेहूं का दाना (हज़रत आदम का वर्जित फल)", "english": "wheat grain (forbidden fruit in Islamic tradition)"},
    "मरातब": {"hindi": "मर्तबा, उच्च पदवी, सम्मान, रूहानी दर्जा", "english": "maratib, high spiritual ranks/dignities"},
    "कलवत्तर": {"hindi": "बड़ा चीरने वाला आरा (हज़रत जकरिया की शहादत का रूपक)", "english": "saw (instrument of martyrdom of Prophet Zakariya)"},
    "कुमबइजनी": {"hindi": "'कुम बिइज़्नी' ('मेरे हुक्म से उठ!')—शम्स तबरेज़ी का वाक्य", "english": "'Qum bi-idhni' (Arise by my permission!)"},
    "असरफ़": {"hindi": "अशराफ़, कुलीन लोग, नवाब, सामंत", "english": "ashraf, nobles, aristocrats"},
    "बेरा": {"hindi": "नाव, बेड़ा; साधन", "english": "boat, ferry, righteous vessel of deeds"},
    "मंगू": {"hindi": "गायों, भैंसों या मवेशियों का झुंड", "english": "herd of cattle/buffalos"},
    "धीदो": {"hindi": "धीदो (रांझा का वास्तविक नाम)", "english": "Dheedo (Ranjha's personal first name)"},
    "सलेटी": {"hindi": "सयाल कोट/झंग सयाल की राजकुमारी (हीर की उपाधि)", "english": "Saleti (epithet of Heer, belonging to Sial)"},
    "मुज़हर": {"hindi": "प्रकटीकरण का स्थान/स्वरूप, बाह्य अभिव्यक्ति", "english": "mazhar, locus of manifestation, manifest form"}
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
        "completed_count": 130,
        "total": 160,
        "next_kafi_id": 131,
        "last_updated": "2026-10-17T19:45:00+05:30",
        "last_batch": "126-130",
        "status": "in_progress",
        "milestone": "130/160 (81.25%) finished. Milestone Kafi 129 included!"
    }
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print(f"Checkpoint updated: 130/160 completed (81.25%!). Next ID: 131")

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
