# -*- coding: utf-8 -*-
"""
Process Kafian 76 to 80 for Bulleh Shah Trilingual Edition.
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
        "id": 76,
        "title": "क्यों ओहले बह बह झाकी दा",
        "title_english": "Why Dost Thou Peep Sitting Behind The Veil?",
        "historical_context": "इस काफी में बुल्ले शाह परमात्मा की रहस्यमयी लुका-छिपी पर विस्मय और मीठा उलाहना व्यक्त करते हैं। वे पूछते हैं कि जब सब कुछ तू ही है—अहद भी तू, अहमद भी तू, रूमी और शामी भी तू—तो फिर यह नश्वर देह (बरज़ख़-ए-खाकी) का पर्दा लगाकर क्यों छिपता है? अंत में वे अपने मुर्शिद शाह इनायत के रूप में उस परमसत्य का साक्षात्कार करते हैं।",
        "meter": "पंजाबी काफी (मात्रािक छंद, तुक: झाकी दा / राखी दा / लौलाकी दा / साकी दा)",
        "raga": "राग काफी / बहार",
        "theme": "ईश्वर का पर्दा और प्रकटीकरण, हकीकत-ए-मोहम्मदिया, 'लौलाका', शाह इनायत का साक्षात्कार",
        "stanzas": [
            {
                "original": [
                    "क्यों ओहले बह बह झाकी दा ।  ",
                    "इह परदा किस तों राखी दा ।"
                ],
                "hindi_gloss": [
                    "क्यों (किसलिए) ओहले (पर्दे की ओट में) बह (बैठ-) बह (बैठकर) झाकी (झांकना होता) दा (है) ।",
                    "इह (यह) परदा (पर्दा/छिपाव) किस (किससे) तों (से) राखी (रखा जाता) दा (है) ।"
                ],
                "english_gloss": [
                    "क्यों (why) ओहले (behind the veil) बह (sitting) बह (sitting) झाकी (peepest) दा (dost Thou) ।",
                    "इह (this) परदा (screen/concealment) किस (whom) तों (from) राखी (keepest) दा (dost Thou) ।"
                ],
                "poetic_hindi": [
                    "क्यों ओट में बैठ-बैठ झांकता है ? यह परदा किससे रखता है ?"
                ],
                "poetic_english": [
                    "Why peepest Thou sitting behind the screen? From whom is this hiding veil between?"
                ]
            },
            {
                "original": [
                    "कारन पीत मीत बण आया, मीम दा घुंघट मुक्ख पर पाइआ,  ",
                    "अहद ते अहमद नाम धराइआ, सिर छतर झुल्ले लौलाकी दा ।  ",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "hindi_gloss": [
                    "कारन (खातिर) पीत (प्रीत के) मीत (सखा/मनुष्य) बण (बनकर) आया (आया), मीम (अक्षर 'मीम' का) दा (का) घुंघट (घूंघट) मुक्ख (मुख) पर (पर) पाइआ (डाल लिया),",
                    "अहद (अहद/अद्वैत से) ते (और) अहमद (अहमद/पैगंबर) नाम (नाम) धराइआ (रख लिया), सिर (सिर पर) छतर (छत्र) झुल्ले (झूलता है) लौलाकी ('लौलाका लमा ख़लक़तुल अफ़लाक'—यदि तू न होता तो मैं आकाश न बनाता) दा (का) ।",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "english_gloss": [
                    "कारन (for the sake of) पीत (love) मीत (friend/human form) बण (becoming) आया (arrived), मीम (of the letter Meem) दा (of) घुंघट (veil) मुक्ख (face) पर (upon) पाइआ (drew),",
                    "अहद (from Ahad) ते (and) अहमद (Ahmad) नाम (name) धराइआ (assumed), सिर (head) छतर (canopy) झुल्ले (waves) लौलाकी (of 'Law-laka'—'Were it not for thee') दा (of) ।",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "poetic_hindi": [
                    "प्रीत की खातिर मीत बना, मुखड़े पर 'मीम' का घूँघट तना,",
                    "'अहद' से 'अहमद' नाम धरा, सिर पर 'लौलाकी' छत्र फिरा !",
                    "क्यों ओट में बैठ-बैठ झांकता है ?"
                ],
                "poetic_english": [
                    "For love's sweet sake as Friend Thou camest near, drawing the 'Meem' across Thy countenance;",
                    "From Ahad, Ahmad's glorious name shone clear, beneath the 'Lawlaka' sovereign expanse!",
                    "Why peepest Thou sitting behind the screen?"
                ]
            },
            {
                "original": [
                    "तुसीं आपे आप ही सारे हो, क्यों कहन्दे असीं न्यारे हो,  ",
                    "आए आपने आप नज़्ज़ारे हो, विच बरजक्ख रख्या खाकी दा ।  ",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "hindi_gloss": [
                    "तुसीं (तुम) आपे (स्वयं ही) आप (स्वयं) ही (ही) सारे (सब कुछ) हो (हो), क्यों (फिर क्यों) कहन्दे (कहते हो कि) असीं (हम) न्यारे (सबसे पृथक/अलहदा) हो (हैं),",
                    "आए (आए हो) आपने (अपने ही) आप (स्वरूप के) नज़्ज़ारे (साक्षात्कार/लीला देखने) हो (हो), विच (बीच में) बरजक्ख (अंतराल/आवरण) रख्या (रखा है) खाकी (इस मिट्टी के शरीर) दा (का) ।",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "english_gloss": [
                    "तुसीं (Thou) आपे (Thyself) आप (Thyself) ही (alone) सारे (all) हो (art), क्यों (why) कहन्दे (claimest) असीं (we) न्यारे (aloof/apart) हो (art),",
                    "आए (comest) आपने (Thine own) आप (Self) नज़्ज़ारे (spectacle/vision) हो (to behold), विच (between) बरजक्ख (isthmus/veil) रख्या (placed) खाकी (of earthly clay) दा (of) ।",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "poetic_hindi": [
                    "तू ही स्वयं सब कुछ है स्वामी, फिर क्यों कहे कि न्यारा हूँ ?",
                    "अपने ही दर्शन करने आया, बीच में मिट्टी का पर्दा धारा हूँ !"
                ],
                "poetic_english": [
                    "Thou art Thyself all that exists below, why dost Thou claim to stand apart and high?",
                    "To view Thine own enchanting mirror-glow, draped in an earthy veil before the eye!",
                    "Why peepest Thou sitting behind the screen?"
                ]
            },
            {
                "original": [
                    "तुध बाझों दूसरा केहड़ा है, क्यों पाइआ उलटा झेड़ा है,  ",
                    "इह डिठा बड़ा अंधेरा है, हुन आप नूं आपे आखी दा ।  ",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "hindi_gloss": [
                    "तुध (तेरे) बाझों (बिना) दूसरा (दूसरा/अन्य) केहड़ा (कौन) है (है), क्यों (क्यों) पाइआ (फैला रखा है) उलटा (विचित्र/उल्टा) झेड़ा (विवाद/झगड़ा) है,",
                    "इह (यह) डिठा (देखा जाता है) बड़ा (बड़ा भारी) अंधेरा (अज्ञान का अंधकार) है, हुन (अब तो) आप (अपने) नूं (को) आपे (स्वयं ही) आखी (सत्य कहना होता) दा (है) ।",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "english_gloss": [
                    "तुध (Thee) बाझों (without) दूसरा (second/other) केहड़ा (who) है (is), क्यों (why) पाइआ (stirred) उलटा (paradoxical) झेड़ा (contention) है (has),",
                    "इह (this) डिठा (is seen) बड़ा (great) अंधेरा (darkness/delusion) है (is), हुन (now) आप (one’s self) नूं (unto) आपे (self) आखी (address/proclaim) दा (must) ।",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "poetic_hindi": [
                    "तेरे बिना दूजा है कौन, क्यों व्यर्थ विवाद खड़ा कीना ?",
                    "अज्ञान का घोर अंधेरा है, खुद अपने को ही खुद पहचाना !"
                ],
                "poetic_english": [
                    "Except for Thee who else is here to stand? Why stir this tangled controversy sore?",
                    "Deep darkness broods across the sleeping land, when self must call to Self for evermore!",
                    "Why peepest Thou sitting behind the screen?"
                ]
            },
            {
                "original": [
                    "किते रूमी हो किते शामी हो, किते साहब किते गुलामी हो,  ",
                    "तुसीं आपने आप तमामी हो, कहो खोटा खरा सौ लाखी दा ।  ",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "hindi_gloss": [
                    "किते (कहीं) रूमी (रोम के गोरे) हो (हो) किते (कहीं) शामी (सीरियाई/सांवले) हो (हो), किते (कहीं) साहब (स्वामी/मालिक) किते (कहीं) गुलामी (गुलाम/सेवक) हो (हो),",
                    "तुसीं (तुम) आपने (अपने) आप (स्वरूप में) तमामी (परिपूर्ण/समग्र) हो (हो), कहो (कहो, कौन) खोटा (खोटा है और कौन) खरा (खरा) सौ (सौ) लाखी (लाखों रुपयों के मूल्य) दा (का) ।",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "english_gloss": [
                    "किते (somewhere) रूमी (Roman) हो (art) किते (somewhere) शामी (Syrian) हो (art), किते (somewhere) साहब (master) किते (somewhere) गुलामी (servant) हो (art),",
                    "तुसीं (Thou) आपने (in Thine own) आप (Self) तमामी (the fullness/completeness) हो (art), कहो (tell) खोटा (base metal) खरा (pure gold) सौ (of a hundred) लाखी (thousands) दा (of) ।",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "poetic_hindi": [
                    "कहीं रूमी, कहीं शामी तू, कहीं स्वामी, कहीं गुलाम बने,",
                    "अपने आप में पूर्ण है तू, कौन खोटा-खरा का नाम गिने !"
                ],
                "poetic_english": [
                    "In Rome Thou rulest, or in Syrian air, as sovereign lord or in a bondsman's role;",
                    "In Thine own fullness complete and fair—who weighs the base or precious in the whole?",
                    "Why peepest Thou sitting behind the screen?"
                ]
            },
            {
                "original": [
                    "जिस तन विच इश्क दा जोश होया, उह बेख़ुद हो बेहोश होया,  ",
                    "उह क्यों कर रहे खामोश होया, जिस प्याला पीता साकी दा ।  ",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "hindi_gloss": [
                    "जिस (जिस) तन (तन) विच (में) इश्क (इश्क) दा (का) जोश (उफान/आवेश) होया (हुआ), उह (वह) बेख़ुद (आत्म-विस्मृत/बेखुद) हो (होकर) बेहोश (मदमस्त) होया (हो गया),",
                    "उह (वह) क्यों (कैसे) कर (करके) रहे (रहे) खामोश (मौन) होया (होकर), जिस (जिसने) प्याला (प्याला) पीता (पी लिया) साकी (दिव्य साकी) दा (का) ।",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "english_gloss": [
                    "जिस (which) तन (body) विच (in) इश्क (of love) दा (the) जोश (passion/fervor) होया (arose), उह (he) बेख़ुद (selfless) हो (becoming) बेहोश (entranced) होया (became),",
                    "उह (how) क्यों (why) कर (could) रहे (remain) खामोश (silent) होया (being), जिस (who) प्याला (cup) पीता (drank) साकी (of the Cupbearer) दा (of) ।",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "poetic_hindi": [
                    "जिस तन में इश्क का जोश उठा, वह बेखुद होकर मतवाला हुआ,",
                    "वह कैसे मौन रहे जग में, जिसने साकी का प्याला पिया !"
                ],
                "poetic_english": [
                    "In whom the tempest of true passion wakes, selfhood dissolves in ecstatic trance;",
                    "How can he silent stay who freely takes the Saki's chalice in the holy dance?",
                    "Why peepest Thou sitting behind the screen?"
                ]
            },
            {
                "original": [
                    "तुसीं आप असां नूं धाए जी, कद रहन्दे छुपे छुपाए जी,  ",
                    "तुसीं शाह 'इनायत' बण आए जी, हुन ला ला नैन झमाकी दा ।  ",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "hindi_gloss": [
                    "तुसीं (तुम) आप (स्वयं) असां (हमारी) नूं (ओर) धाए (दौड़े आए) जी (हे प्रभु), कद (कब तक) रहन्दे (रह सकते हो) छुपे (छिपे-) छुपाए (छुपाए) जी,",
                    "तुसीं (तुम स्वयं) शाह (शाह) 'इनायत' (इनायत का रूप) बण (बनकर) आए (आ गए) जी, हुन (अब) ला (लगाकर) ला (लगाकर) नैन (नेत्रों की) झमाकी (टकटकी/झलक) दा (का आनंद लो) ।",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "english_gloss": [
                    "तुसीं (Thou) आप (Thyself) असां (unto us) नूं (unto) धाए (hast run) जी (O Lord), कद (how long) रहन्दे (couldst remain) छुपे (concealed) छुपाए (hidden) जी,",
                    "तुसीं (Thou) शाह (Shah) 'इनायत' (Inayat) बण (becoming) आए (came) जी, हुन (now) ला (casting) ला (casting) नैन (eyes') झमाकी (winking radiance) दा (of) ।",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "poetic_hindi": [
                    "तुम आप हमारी ओर दौड़े, कब तक छिपते छिपवाए जी ?",
                    "तुम शाह इनायत बन कर आए, अब नैनों से नैन मिलाए जी !"
                ],
                "poetic_english": [
                    "Thou hast Thyself rushed forward to my heart—how couldst Thou remain hidden from my view?",
                    "As Master Shah Inayat Thou art, flashing Thine eyes of radiant morning dew!",
                    "Why peepest Thou sitting behind the screen?"
                ]
            },
            {
                "original": [
                    "बल्ल्हा शाह तन भा दी भट्ठी कर, अग्ग बाल हड्डां तन माटी कर,  ",
                    "इह शौक मुहबत बाटी कर, इह मधूवा इस बिध चाखी (झाकी) दा ।  ",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "hindi_gloss": [
                    "बल्ल्हा (बुल्ला कहता है) शाह (हे शाह) तन (तन को) भा (अग्नि) दी (की) भट्ठी (भट्ठी) कर (बना ले), अग्ग (अग्नि में) बाल (जलाकर) हड्डां (हड्डियों व) तन (तन को) माटी (खाक/राख) कर (कर दे),",
                    "इह (इस) शौक (प्रेम-उमंग व) मुहबत (निष्ठा की) बाटी (प्याला/कटोरी) कर (बना ले), इह (यह) मधूवा (अमृत-मदिरा) इस (इस) बिध (प्रकार) चाखी (चखी जाती) दा (है) ।",
                    "क्यों (किसलिए) ओहले (पर्दे में) बह (बैठ-) बह (बैठकर) झाकी दा, इह परदा किस तों राखी दा ।"
                ],
                "english_gloss": [
                    "बल्ल्हा (Bulleh says) शाह (O Lord) तन (body) भा (of fire) दी (of) भट्ठी (furnace) कर (make), अग्ग (in fire) बाल (burning) हड्डां (bones) तन (flesh) माटी (dust/ashes) कर (render),",
                    "इह (this) शौक (yearning) मुहबत (of love) बाटी (goblet) कर (fashion), इह (this) मधूवा (wine of ecstasy) इस (this) बिध (manner) चाखी (is tasted) दा (must be) ।",
                    "क्यों ओहले बह बह झाकी दा ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा शाह! तन को अग्नि-भट्ठी कर, जला हड्डियां, तन माटी कर,",
                    "प्रेम-शौक का प्याला बना ले, तब यह अमृत-रस चखा जाए !",
                    "क्यों ओट में बैठ-बैठ झांकता है ? यह परदा किससे रखता है ?"
                ],
                "poetic_english": [
                    "O Bulleh Shah, make of thy frame a flame, burn flesh and bone to dust in sacred fire;",
                    "Fashion Love's goblet in His holy name, and drink the nectar of supreme desire!",
                    "Why peepest Thou sitting behind the screen? From whom is this hiding veil between?"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी सूफ़ी दर्शन के 'हकीकत-ए-मोहम्मदिया' और 'इश्क के प्याले' का अद्भुत समन्वय है। 'लौलाका लमा ख़लक़तुल अफ़लाक' (हदीस-ए-कुदसी: 'यदि तुम न होते, तो मैं आकाशों की रचना न करता') का संदर्भ देते हुए बुल्ले शाह कहते हैं कि परमात्मा ने केवल प्रेम के प्रकटीकरण के लिए ही यह सृष्टि रची है। मुर्शिद शाह इनायत का प्रकटन ही परमात्मा के समस्त पर्दों को हटा देता है।"
    },
    {
        "id": 77,
        "title": "लणतरानी दस्स के जानी हुन क्यों मुक्ख छुपाइआ ई",
        "title_english": "Saying 'Thou Shalt Not See Me', O Darling, Why Hast Thou Hidden Thy Face?",
        "historical_context": "इस काफी में बुल्ले शाह हज़रत मूसा और तूर पर्वत की ऐतिहासिक घटना—जहाँ ईश्वर ने कहा था 'लन तरा-नी' (तुम मुझे नहीं देख सकते)—का उल्लेख करते हैं। वे परमात्मा से प्रेम-भरे अधिकार के साथ पूछते हैं कि जब तूने 'कलूना नहनु अकरबु इलैहि मिन हब्लिल वरीद' (हम तुम्हारी गर्दन की नस से भी निकट हैं) कहा है, तो फिर मूसा को 'लन तरा-नी' कहकर अपना मुख क्यों छिपाया? इसके पश्चात वे अय्यूब, मंसूर और आदम-इबलीस के आख्यानों से प्रेम का रहस्य उद्घाटित करते हैं।",
        "meter": "पंजाबी काफी (मात्रािक छंद, तुक: छुपाइआ ई / फ़ुरमाइआ ई / चढ़ाइआ ई)",
        "raga": "राग सोरठ / भैरवी",
        "theme": "'लन तरा-नी' का सूफी रहस्य, मूसा, मंसूर और शैतान का आख्यान, प्रेम का साक्षात्कार",
        "stanzas": [
            {
                "original": [
                    "मैं ढोलन विच फ़रक ना कोई एनुमा फ़ुरमाइआ ई ।  ",
                    "आयो सजन गल लग्ग सौवां मैं हुन घुंघट पाइआ ई ।  ",
                    "लणतरानी दस्स के जानी हुन क्यों मुक्ख छुपाइआ ई ?"
                ],
                "hindi_gloss": [
                    "मैं (मुझमें) ढोलन (और मेरे प्रियतम में) विच (में) फ़रक (कोई भेद) ना (नहीं) कोई (कोई भी), एनुमा ('ऐनुल हक़'—यथार्थ सत्य) फ़ुरमाइआ (तूने ही फरमाया) ई (है),",
                    "आयो (आओ) सजन (हे प्रियतम) गल (गले) लग्ग (लगकर) सौवां (सो जाऊँ), मैं (तूने) हुन (अब यह) घुंघट (घूंघट/पर्दा) पाइआ (डाल लिया) ई (है) ।",
                    "लणतरानी ('लन तरा-नी'—तू मुझे नहीं देख सकता) दस्स (कहकर) के (के) जानी (हे मेरे प्यारे) हुन (अब) क्यों (क्यों) मुक्ख (मुखड़ा) छुपाइआ (छिपा लिया) ई (है) ?"
                ],
                "english_gloss": [
                    "मैं (between me) ढोलन (and the Beloved) विच (in) फ़रक (difference) ना (no) कोई (none), एनुमा (as the absolute reality) फ़ुरमाइआ (Thou hast proclaimed) ई (hast),",
                    "आयो (come) सजन (O Beloved) गल (to bosom) लग्ग (clasping) सौवां (let me slumber), मैं (Thou) हुन (now) घुंघट (the veil) पाइआ (hast drawn) ई (hast) ।",
                    "लणतरानी ('Thou shalt not see Me') दस्स (proclaiming) के (having) जानी (O Beloved) हुन (now) क्यों (why) मुक्ख (Thy face) छुपाइआ (hast hidden) ई (Thou) ?"
                ],
                "poetic_hindi": [
                    "मुझमें-पिय में भेद नहीं कुछ, तूने ही फरमाया रे,",
                    "आओ साजन, अंक लगाऊँ, तूने घूँघट डाला रे !",
                    "'तुम न देख सकोगे मुझको' कह कर, मुख क्यों छुपाया रे ?"
                ],
                "poetic_english": [
                    "No difference lies 'twixt me and Thee—Thine own decree declared it so;",
                    "Come, Sweetheart, clasp me to Thy breast, why dost Thou hide beneath this glow?",
                    "Saying 'Thou shalt not see Me', Love, why hast Thou hidden Thy face?"
                ]
            },
            {
                "original": [
                    "तन साबर दे कीड़े पाए जो चढ़आ सो पाइआ ई ।  ",
                    "मनसूर कोलों कुझ ज़ाहर होया सूली पकड़ चढ़ाइआ ई ।  ",
                    "लणतरानी दस्स के जानी हुन क्यों मुक्ख छुपाइआ ई ?"
                ],
                "hindi_gloss": [
                    "तन (शरीर में) साबर (धैर्यवान अय्यूब के) दे (के) कीड़े (कीड़े) पाए (डाल दिए), जो (जो इस कसौटी पर) चढ़आ (चढ़ा) सो (उसी ने तुझे) पाइआ (प्राप्त किया) ई (है),",
                    "मनसूर (मंसूर हल्लाज) कोलों (के मुख से) कुझ (कुछ गुप्त सत्य) ज़ाहर (प्रकट) होया (हो गया), सूली (सूली पर) पकड़ (पकड़कर) चढ़ाइआ (चढ़वा दिया) ई (तूने) ।",
                    "लणतरानी दस्स के जानी हुन क्यों मुक्ख छुपाइआ ई ?"
                ],
                "english_gloss": [
                    "तन (in flesh) साबर (of patient Job) दे (of) कीड़े (worms) पाए (cast), जो (whoever) चढ़आ (ascended the ordeal) सो (he) पाइआ (attained Thee) ई (hast),",
                    "मनसूर (from Mansur) कोलों (from) कुझ (some secret) ज़ाहर (revealed) होया (became), सूली (to the gallows) पकड़ (seizing) चढ़ाइआ (hast raised) ई (Thou) ।",
                    "लणतरानी दस्स के जानी हुन क्यों मुक्ख छुपाइआ ई ?"
                ],
                "poetic_hindi": [
                    "अय्यूब के तन में कीड़े डाले, जो तपा सो उसने पाया,",
                    "मंसूर के मुख से सच प्रकटा तो सूली पर चढ़वाया !"
                ],
                "poetic_english": [
                    "Worms in the flesh of patient Job, who bore the fire attained Thy grace;",
                    "When Mansur blabbed the holy truth, the gallows claimed him in Thy place!"
                ]
            },
            {
                "original": [
                    "दस्सो नुकता ज़ात इलाही सज्जदा किस कराइआ ई ।  ",
                    "बुल्ल्हा शहु दा हुकम ना मन्न्या शैतान ख़वार कराइआ ई ।  ",
                    "लणतरानी दस्स के जानी हुन क्यों मुक्ख छुपाइआ ई ?"
                ],
                "hindi_gloss": [
                    "दस्सो (बताओ) नुकता (वह गूढ़ बिंदु) ज़ात (ईश्वरीय स्वरूप) इलाही (इलाही का), सज्जदा (सजदा/प्रणाम) किस (किसको) कराइआ (करवाया था तूने—आदम को या स्वयं अपने नूर को),",
                    "बुल्ल्हा (बुल्ले का) शहु (प्रभु) दा (का) हुकम (आदेश) ना (नहीं) मन्न्या (माना), शैतान (इबलीस/शैतान को) ख़वार (अपमानित/भ्रष्ट) कराइआ (कर दिया) ई (तूने) ।",
                    "लणतरानी (तू मुझे नहीं देख सकता) दस्स (कहकर) के जानी हुन क्यों मुक्ख छुपाइआ ई ?"
                ],
                "english_gloss": [
                    "दस्सो (reveal) नुकता (the subtle point) ज़ात (of the Essence) इलाही (Divine), सज्जदा (prostration) किस (unto whom) कराइआ (didst Thou command) ई (Thou),",
                    "बुल्ल्हा (Bulleh’s) शहु (Lord’s) दा (of) हुकम (command) ना (not) मन्न्या (obeyed), शैतान (Satan/Iblis) ख़वार (disgraced/cursed) कराइआ (was made) ई (by Thee) ।",
                    "लणतरानी दस्स के जानी हुन क्यों मुक्ख छुपाइआ ई ?"
                ],
                "poetic_hindi": [
                    "बताओ वह रहस्य दिव्य, सजदा करवाया किसको था ?",
                    "आज्ञा न मानी प्रभु की जब, शैतान को ख्वार कराया था !",
                    "'तुम न देख सकोगे मुझको' कह कर, मुख क्यों छुपाया रे ?"
                ],
                "poetic_english": [
                    "Reveal the secret of Thy Light: to whom was holy homage paid?",
                    "Because he spurned Thy sovereign word, Iblis in outer dark was laid!",
                    "Saying 'Thou shalt not see Me', Love, why hast Thou hidden Thy face?"
                ]
            }
        ],
        "philosophical_meaning": "सूफी धर्मशास्त्र में 'लन तरा-नी' (तुम मुझे नहीं देख सकते—सूरह आराफ़ 7:143) एक केंद्रीय प्रसंग है। जब मूसा ने कहा 'रब्बि अरिनी अनज़ुर इलैक' (हे मेरे रब, मुझे दर्शन दे), तो परमात्मा ने कहा कि भौतिक चर्मचक्षु उस असीम तेज को नहीं देख सकते। किंतु बुल्ले शाह प्रेम के अद्वैत स्तर से कहते हैं: यदि जीवात्मा और परमात्मा में कोई भेद नहीं है, तो फिर यह दर्शन से इंकार क्यों? जब आदम को सजदा करवाया गया, तो वह वास्तव में आदम के भीतर विराजमान परमात्मा के नूर को ही सजदा था।"
    },
    {
        "id": 78,
        "title": "माटी कुदम करेंदी यार",
        "title_english": "The Clay Dances and Gallops, O Friend!",
        "historical_context": "यह बाबा बुल्ले शाह की विश्व-प्रसिद्ध काफ़ियों में से एक है, जिसमें जीवन के संपूर्ण चक्र को 'माटी' (मिट्टी/धूल) के रूपक में पिरोया गया है। वस्त्र, अश्व, घुड़सवार, बाज़ार, बाग, हथियार—सब कुछ मिट्टी का ही रूपांतरण है। एक मिट्टी दूसरी मिट्टी पर घमंड करती है, उसे मारती है, और अंत में खेल-कूद कर पुनः मिट्टी में ही समा जाती है। यह नश्वरता और वैराग्य का अद्भुत काव्य-शिखर है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: माटी कुदम करेंदी यार)",
        "raga": "राग काफी / तिलक कामोद",
        "theme": "संसार की नश्वरता, मिट्टी का रूपक, अहंकार का खोखलापन, आध्यात्मिक मुक्ति",
        "stanzas": [
            {
                "original": [
                    "माटी जोड़ा माटी घोड़ा, माटी दा असवार,  ",
                    "माटी माटी नूं दौड़ाए, माटी दा खड़कार,  ",
                    "माटी कुदम करेंदी यार ।"
                ],
                "hindi_gloss": [
                    "माटी (मिट्टी का ही) जोड़ा (वस्त्र/परिधान), माटी (मिट्टी का ही) घोड़ा (अश्व), माटी (मिट्टी का ही) दा (का) असवार (घुड़सवार मनुष्य),",
                    "माटी (मिट्टी का सवार) माटी (मिट्टी के घोड़े) नूं (को) दौड़ाए (दौड़ाता है), माटी (मिट्टी के टापों) दा (का) खड़कार (खड़खड़ाहट/कोलाहल मचता है),",
                    "माटी (मिट्टी ही) कुदम (कूद-कूद कर नृत्य/अठखेलियां) करेंदी (कर रही है) यार (हे मित्र) ।"
                ],
                "english_gloss": [
                    "माटी (clay is) जोड़ा (the garment), माटी (clay the) घोड़ा (horse), माटी (clay) दा (of) असवार (the rider),",
                    "माटी (clay) माटी (clay) नूं (unto) दौड़ाए (spurs to gallop), माटी (of clay) दा (the) खड़कार (clatter and din),",
                    "माटी (clay) कुदम (dances/gallops) करेंदी (leaps) यार (O friend) ।"
                ],
                "poetic_hindi": [
                    "माटी का जोड़ा, माटी का घोड़ा, माटी का असवार,",
                    "माटी माटी को दौड़ाए, माटी का खड़कार ।",
                    "माटी कुदम करे री यार !"
                ],
                "poetic_english": [
                    "Clay is the garment, clay the steed, and clay the cavalier,",
                    "Clay spurs on clay at headlong speed, with clatter sounding near:",
                    "The clay leaps dancing, O my friend!"
                ]
            },
            {
                "original": [
                    "माटी माटी नूं मारन लग्गी, माटी दे हथ्यार,  ",
                    "जिस माटी पर बहुती माटी, तिस माटी हंकार,  ",
                    "माटी कुदम करेंदी यार ।"
                ],
                "hindi_gloss": [
                    "माटी (मिट्टी का मनुष्य) माटी (मिट्टी के मनुष्य) नूं (को) मारन (मारने) लग्गी (लगा है), माटी (मिट्टी के बने ही) दे (के) हथ्यार (अस्त्र-शस्त्र हैं),",
                    "जिस (जिस) माटी (मिट्टी/मनुष्य) पर (के पास) बहुती (अधिक धन-दौलत रूपी) माटी (मिट्टी है), तिस (उस) माटी (मिट्टी को) हंकार (अहंकार हो जाता है),",
                    "माटी कुदम करेंदी यार ।"
                ],
                "english_gloss": [
                    "माटी (clay) माटी (clay) नूं (unto) मारन (to slay) लग्गी (begins), माटी (of clay) दे (of) हथ्यार (weapons),",
                    "जिस (which) माटी (clay) पर (upon) बहुती (much) माटी (earthly dust/wealth), तिस (that) माटी (clay) हंकार (pride/arrogance),",
                    "माटी कुदम करेंदी यार ।"
                ],
                "poetic_hindi": [
                    "माटी माटी को मारने दौड़ी, माटी के हथियार,",
                    "जिस माटी पर बहुत है माटी, उस माटी अहंकार ।",
                    "माटी कुदम करे री यार !"
                ],
                "poetic_english": [
                    "Clay strikes at clay in mortal fight, with weapons wrought of clay,",
                    "The clay that heaps up earthly dust, grows haughty in its day:",
                    "The clay leaps dancing, O my friend!"
                ]
            },
            {
                "original": [
                    "माटी बाग़ बगीचा माटी, माटी दी गुलज़ार,  ",
                    "माटी माटी नूं वेखन आई, माटी दी ए बहार ।  ",
                    "माटी कुदम करेंदी यार ।"
                ],
                "hindi_gloss": [
                    "माटी (मिट्टी का ही) बाग़ (बाग है) बगीचा (बगीचा) माटी (मिट्टी है), माटी (मिट्टी की ही) दी (की) गुलज़ार (फूलों की क्यारी है),",
                    "माटी (मिट्टी का मनुष्य) माटी (मिट्टी के फूलों) नूं (को) वेखन (देखने) आई (आई है), माटी (मिट्टी की ही) दी (की) ए (यह) बहार (वसंत-बहार है),",
                    "माटी कुदम करेंदी यार ।"
                ],
                "english_gloss": [
                    "माटी (clay the) बाग़ (orchard) बगीचा (garden) माटी (is clay), माटी (of clay) दी (the) गुलज़ार (rose-bed),",
                    "माटी (clay) माटी (clay) नूं (unto) वेखन (to view) आई (comes), माटी (of clay) दी (is) ए (this) बहार (bloom/spring),",
                    "माटी कुदम करेंदी यार ।"
                ],
                "poetic_hindi": [
                    "माटी बाग-बगीचा माटी, माटी का गुलज़ार,",
                    "माटी माटी को देखने आई, माटी की यह बहार ।",
                    "माटी कुदम करे री यार !"
                ],
                "poetic_english": [
                    "Clay is the orchard, clay the bower, and clay the blooming rose,",
                    "Clay comes to gaze on clay's bright flower, where spring’s enchantment glows:",
                    "The clay leaps dancing, O my friend!"
                ]
            },
            {
                "original": [
                    "हस्स खेड मुड़ माटी होई, माटी पायों पसार,  ",
                    "बुल्हा इह बुझारत बुझ्झें, लाह सिरों भोएं मार(भार),  ",
                    "माटी कुदम करेंदी यार ।"
                ],
                "hindi_gloss": [
                    "हस्स (हँसकर) खेड (खेलकर) मुड़ (अंततः) माटी (मिट्टी में) होई (मिल गई), माटी (कब्र में माटी बनकर) पायों (पाँव) पसार (पसारकर सो गई),",
                    "बुल्हा (बुल्ला कहता है) इह (इस) बुझारत (पहेली को) बुझ्झें (बूझ ले/समझ ले), लाह (उतारकर) सिरों (सिर से) भोएं (भूमि पर) मार (फेंक दे अहंकार का भारी बोझ),",
                    "माटी (मिट्टी ही) कुदम (नृत्य) करेंदी (कर रही है) यार (हे मित्र) ।"
                ],
                "english_gloss": [
                    "हस्स (laughing) खेड (playing) मुड़ (in the end) माटी (clay) होई (became), माटी (clay) पायों (feet) पसार (stretched out in the grave),",
                    "बुल्हा (Bulleh) इह (this) बुझारत (riddle) बुझ्झें (solve), लाह (unloading) सिरों (from head) भोएं (upon the earth) मार (cast down the heavy load of pride),",
                    "माटी कुदम करेंदी यार ।"
                ],
                "poetic_hindi": [
                    "हँस-खेल कर माटी में मिल गई, पाँव पसारे माटी सोई,",
                    "बुल्ल्हा इस पहेली को बूझे, सिर से बोझ उतारे कोई !",
                    "माटी कुदम करे री यार !"
                ],
                "poetic_english": [
                    "Laughing and playing it turns to dust, stretching its limbs asleep;",
                    "Bulleh, solve now this riddle just, and cast down burdens deep:",
                    "The clay leaps dancing, O my friend!"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी कबीर के 'माटी कहे कुम्हार से तू क्या रूँदे मोहि' से भी अधिक गतिमान और नाटकीय है। समस्त सृष्टि 'माटी' का ही एक नाटक है। जब राजा घोड़े पर चढ़ता है, तो मिट्टी ही मिट्टी पर सवार होती है। जब कोई धनी अभिमानी बनता है, तो वह केवल इस बात का घमंड करता है कि उसके ऊपर अधिक मिट्टी (सोना, चांदी, जमीन) लदी हुई है। अंत में कब्र में पाँव पसारकर मिट्टी पुनः मूल तत्व में विलीन हो जाती है।"
    },
    {
        "id": 79,
        "title": "माही वे तैं मिलिआं सभ दुक्ख होवन दूर",
        "title_english": "O Beloved! In Meeting Thee All Sorrows Fade Away",
        "historical_context": "इस काफी में बुल्ले शाह परमात्मा (माही / रांझा) के साक्षात दर्शन के परम आनंद का वर्णन करते हैं। संसार जिसे दीन-हीन चरवाहा (चाक चकेटा) समझता है, वही सच्चा कृपालु परमात्मा (रब्ब गफूर) है। जब उसका नूर प्रत्यक्ष हो जाता है, तो विरह की सारी पीड़ाएं स्वतः विदा हो जाती हैं।",
        "meter": "पंजाबी काफी (चतुष्पदी, अंत्यानुप्रास दूर/गफ़ूर/झूर/नूर)",
        "raga": "राग आसावरी / काफी",
        "theme": "परमात्मा से मिलन का सुख, सांसारिक दृष्टि बनाम आध्यात्मिक दृष्टि, सर्वव्यापक नूर",
        "stanzas": [
            {
                "original": [
                    "लोकां दे भाने चाक चकेटा, साडा रब्ब ग़फ़ूर ।  ",
                    "माही वे तैं मिलिआं सभ दुक्ख होवन दूर ।"
                ],
                "hindi_gloss": [
                    "लोकां (सांसारिक लोगों) दे (के) भाने (दृष्टिकोण में वह तुच्छ) चाक (चरवाहा) चकेटा (छोकरा है), साडा (किंतु हमारा वह) रब्ब (परमात्मा) ग़फ़ूर (परम क्षमाशील प्रभु है) ।",
                    "माही (हे प्रियतम) वे (हे प्यारे) तैं (तुझसे) मिलिआं (मिलने पर) सभ (समस्त) दुक्ख (दुख) होवन (हो जाते हैं) दूर (दूर) ।"
                ],
                "english_gloss": [
                    "लोकां (of the worldly) दे (of) भाने (in judgment) चाक (herdsman) चकेटा (a common stripling), साडा (our) रब्ब (Lord God) ग़फ़ूर (the Forgiving/Merciful) ।",
                    "माही (O Beloved) वे (O) तैं (Thee) मिलिआं (in meeting) सभ (all) दुक्ख (sorrows) होवन (become) दूर (dispelled) ।"
                ],
                "poetic_hindi": [
                    "जग जाने चरवाहा छोकरा, हमारा रब-गफ़ूर है वह !",
                    "माही रे! तुझसे मिलने पर सब दुख मिट जाएँ दूर !"
                ],
                "poetic_english": [
                    "To worldly eyes a herdsman lad, to us the Lord of Grace on high!",
                    "Beloved, in meeting Thee, all sorrows fade and die!"
                ]
            },
            {
                "original": [
                    "मिलन दी ख़ातर चशमां, बहन्दियां सी नित झूर ।  ",
                    "माही वे तैं मिलिआं सभ दुक्ख होवन दूर ।"
                ],
                "hindi_gloss": [
                    "मिलन (दर्शन पाने) दी (की) ख़ातर (खातिर/आकांक्षा में) चशमां (मेरी दोनों आँखें), बहन्दियां (बहती रहती) सी (थीं) नित (प्रतिदिन) झूर (तड़प-तड़प कर) ।",
                    "माही वे तैं मिलिआं सभ दुक्ख होवन दूर ।"
                ],
                "english_gloss": [
                    "मिलन (union) दी (of) ख़ातर (for sake) चशमां (my weeping eyes), बहन्दियां (flowed) सी (were) नित (constantly) झूर (pining) ।",
                    "माही वे तैं मिलिआं सभ दुक्ख होवन दूर ।"
                ],
                "poetic_hindi": [
                    "मिलन की आस में अंखियां, नित्य रो-रो बहती थीं विह्वल !"
                ],
                "poetic_english": [
                    "Longing for union day and night, these weeping eyes in sorrow flowed!"
                ]
            },
            {
                "original": [
                    "उट्ठ गई हिजर जुदाई जिगरों, ज़ाहर दिसदा नूर ।  ",
                    "माही वे तैं मिलिआं सभ दुक्ख होवन दूर ।"
                ],
                "hindi_gloss": [
                    "उट्ठ (समाप्त हो) गई (गई) हिजर (विरह की) जुदाई (जुदाई) जिगरों (हृदय से), ज़ाहर (साक्षात प्रत्यक्ष) दिसदा (दिखाई दे रहा है) नूर (दिव्य ईश्वरीय प्रकाश) ।",
                    "माही वे तैं मिलिआं सभ दुक्ख होवन दूर ।"
                ],
                "english_gloss": [
                    "उट्ठ (vanished) गई (away) हिजर (of separation) जुदाई (the pain) जिगरों (from the core), ज़ाहर (manifest) दिसदा (is seen) नूर (the Divine Light) ।",
                    "माही वे तैं मिलिआं सभ दुक्ख होवन दूर ।"
                ],
                "poetic_hindi": [
                    "मिट गई विरह-जुदाई मन से, प्रकट लखा है पावन नूर !"
                ],
                "poetic_english": [
                    "The pangs of parting flee the chest, manifest shines the radiant Light!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा रमज़ समझ दी पाईआ, ना नेड़े ना दूर ।  ",
                    "माही वे तैं मिलिआं सभ दुक्ख होवन दूर ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ले ने) रमज़ (परम रहस्य) समझ (समझदारी का) दी (का) पाईआ (पा लिया है), ना (न वह परमात्मा) नेड़े (केवल निकट है) ना (न वह) दूर (कहीं दूर है—वह तो सर्वांतर्यामी है) ।",
                    "माही वे तैं मिलिआं सभ दुक्ख होवन दूर ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh) रमज़ (secret) समझ (of wisdom) दी (of) पाईआ (grasped), ना (neither) नेड़े (near) ना (nor) दूर (far—all-pervading) ।",
                    "माही वे तैं मिलिआं सभ दुक्ख होवन दूर ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा ने यह भेद समझ लिया: न वह निकट, न वह है दूर !",
                    "माही रे! तुझसे मिलने पर सब दुख मिट जाएँ दूर !"
                ],
                "poetic_english": [
                    "Bulleh has grasped the mystic clue: He is not near nor far away!",
                    "Beloved, in meeting Thee, all sorrows fade and die!"
                ]
            }
        ],
        "philosophical_meaning": "सांसारिक दृष्टि केवल बाह्य वेश को देखती है—वे रांझा को केवल भैंसें चराने वाला 'चाक चकेटा' मानते हैं; किंतु प्रेम की दिव्य दृष्टि जानती है कि वही साक्षात 'रब्ब गफूर' है। 'ना नेड़े ना दूर' उपनिषद के वचन 'तद् दूरे तद्वन्तिके' (वह दूर भी है और निकट भी है) का सूफी प्रतिध्वनि है।"
    },
    {
        "id": 80,
        "title": "मैं बे-कैद मैं बे-कैद",
        "title_english": "I Am Boundless, Unconfined and Free!",
        "historical_context": "यह काफी बुल्ले शाह की अद्वैतवादी मुक्ति (मुक्ति / विदेह-मुक्ति) का परम घोषणा-पत्र है। 80वीं काफी पर पहुंचकर बुल्ले शाह समस्त धार्मिक, सामाजिक और लौकिक संकीर्णताओं से परे होकर अपनी पूर्ण स्वतंत्रता का उद्घोष करते हैं। न वे रोगी हैं, न वैद्य; न मोमिन (मुसलमान) हैं, न काफ़िर; न सैयद हैं, न शिकार। चौदह भुवनों में उनका आत्मा विचरण करता है और वह किसी भी सीमा में आबद्ध नहीं हो सकता।",
        "meter": "पंजाबी छोटी काफी (लयबद्ध दोहा-संकर, अंत्यानुप्रास बे-कैद/वैद/सैद/ऐब/पैद)",
        "raga": "राग काफी / भैरवी",
        "theme": "आत्म-मुक्ति (इस्तक़लाल), धार्मिक संकीर्णताओं का अतिक्रमण, सर्वव्यापी आत्मा, अद्वैत आनंद",
        "stanzas": [
            {
                "original": [
                    "मैं बे-कैद मैं बे-कैद ।  ",
                    "ना रोगी ना वैद ।"
                ],
                "hindi_gloss": [
                    "मैं (मैं सर्वथा) बे-कैद (बंधन-मुक्त/असीम) मैं (मैं) बे-कैद (परम स्वतंत्र हूँ) ।",
                    "ना (न तो मैं कोई) रोगी (रोगी हूँ) ना (न ही कोई) वैद (वैद्य/उपचारक) ।"
                ],
                "english_gloss": [
                    "मैं (I am) बे-कैद (unconfined/unfettered) मैं (I am) बे-कैद (boundless and free) ।",
                    "ना (neither) रोगी (the sick patient) ना (nor) वैद (the physician) ।"
                ],
                "poetic_hindi": [
                    "मैं बे-कैद, मैं बे-कैद ! न रोगी हूँ, न मैं वैद !"
                ],
                "poetic_english": [
                    "Unbound am I, unfettered, free! No patient nor physician in me!"
                ]
            },
            {
                "original": [
                    "ना मैं मोमन ना मैं काफर,  ",
                    "ना सईयेद ना सैद ।"
                ],
                "hindi_gloss": [
                    "ना (न) मैं (मैं) मोमन (रूढ़िवादी मुसलमान/विश्वासी) ना (न) मैं (मैं) काफर (नास्तिक/काफिर),",
                    "ना (न मैं उच्च कुलीन) सईयेद (सैयद हूँ) ना (न किसी का शिकार/) सैद (शिकारी) ।"
                ],
                "english_gloss": [
                    "ना (neither) मैं (I am) मोमन (orthodox believer) ना (nor) मैं (I) काफर (infidel/unbeliever),",
                    "ना (neither) सईयेद (high-born Sayyid) ना (nor) सैद (hunted prey) ।"
                ],
                "poetic_hindi": [
                    "न मैं मोमिन, न मैं काफ़िर, न मैं सैयद, न कोई शिकार !"
                ],
                "poetic_english": [
                    "Neither believer nor infidel mild, no noble Sayyid nor victim wild!"
                ]
            },
            {
                "original": [
                    "चौदीं तबकीं सीर असाडा,  ",
                    "किते ना हुन्दा कैद ।"
                ],
                "hindi_gloss": [
                    "चौदीं (चौदह) तबकीं (लोकों/भुवनों में) सीर (सैर/विचरण) असाडा (हमारा है),",
                    "किते (कहीं पर भी यह आत्मा) ना (नहीं) हुन्दा (होता) कैद (कैद/सीमित) ।"
                ],
                "english_gloss": [
                    "चौदीं (through fourteen) तबकीं (realms/spheres) सीर (wander/sojourn) असाडा (mine),",
                    "किते (nowhere) ना (not) हुन्दा (becomes) कैद (confined/bound) ।"
                ],
                "poetic_hindi": [
                    "चौदह लोकों में सैर हमारी, कहीं न बंधती सत्ता हमारी !"
                ],
                "poetic_english": [
                    "Through fourteen spheres my spirits roam, in no cage trapped to make a home!"
                ]
            },
            {
                "original": [
                    "ख़राबात मैं जाल असाडी,  ",
                    "ना शोभा ना ऐब ।"
                ],
                "hindi_gloss": [
                    "ख़राबात (मदिरालय/उच्छृंखल फकीरी में) मैं (मेरी) जाल (गति/चाल) असाडी (हमारी है),",
                    "ना (न मुझे संसार की) शोभा (प्रशंसा की चाह है) ना (न किसी कलंक/) ऐब (दोष की चिंता) ।"
                ],
                "english_gloss": [
                    "ख़राबात (in the tavern of ruin) मैं (my) जाल (ways/gait) असाडी (mine),",
                    "ना (neither) शोभा (worldly honor) ना (nor) ऐब (blemish/disgrace) ।"
                ],
                "poetic_hindi": [
                    "मदिरालय में डगर हमारी, न शोभा की चाह, न दोष का भय भारी !"
                ],
                "poetic_english": [
                    "In the ruins of wine my footsteps tread, no praise I crave, no blame I dread!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु दी ज़ात की पुछनैं,  ",
                    "ना पैदा ना पैद ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ला कहता है) शहु (उस प्रभु/आत्मा) दी (की) ज़ात (जाति/स्वरूप) की (क्या) पुछनैं (पूछता है),",
                    "ना (न वह कभी) पैदा (जन्म लेता है) ना (न उसका कोई अंत/) पैद (नाश होता है—वह अजन्मा और शाश्वत है) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh says) शहु (of the Lord) दी (of) ज़ात (caste/identity) की (what) पुछनैं (inquirest thou),",
                    "ना (neither) पैदा (born) ना (nor) पैद (ended/perished—eternal and uncreated) ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा शौह की क्या जात पूछते, न जो जन्मा, न जिसका अंत होवे !",
                    "मैं बे-कैद, मैं बे-कैद ! न रोगी हूँ, न मैं वैद !"
                ],
                "poetic_english": [
                    "What dost thou ask of Bulleh’s Lord divine? Unborn, undying, beyond boundary line!",
                    "Unbound am I, unfettered, free! No patient nor physician in me!"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी भगवद्गीता के 'नैनं छिन्दन्ति शस्त्राणि' और शंकराचार्य के 'निर्वाणषट्कम' ('मनोबुद्ध्यहङ्कार चित्तानि नाहं...') की सूफी अभिव्यक्ति है। आत्मा शरीर नहीं है, न वह किसी धर्म, जाति (सैयद), देश या लोक (चौदह तबक) की सीमाओं में बंधी है। 'ना पैदा ना पैद' कुरान के 'लम यलिद व लम यूलद' (न उसने किसी को जन्म दिया, न वह किसी से जन्मा) का अद्वैतवादी बोध है।"
    }
]

new_lexicon_terms = {
    "बरजक्ख": {"hindi": "बरज़ख़, दो अवस्थाओं के बीच का अंतराल या पर्दा", "english": "isthmus, intermediate barrier between realms"},
    "लौलाकी": {"hindi": "हदीस: 'लौलाका लमा ख़लक़तुल अफ़लाक' (यदि तू न होता तो मैं आकाश न बनाता)", "english": "the divine utterance: 'Were it not for thee, I would not have created the cosmos'"},
    "लणतरानी": {"hindi": "कुरान का वाक्य: 'लन तरा-नी' (तुम मुझे नहीं देख सकते)", "english": "the divine refusal to Moses: 'Thou shalt not see Me'"},
    "कुदम": {"hindi": "कूदना, छलांग, नृत्य, तीव्र चाल", "english": "leaping, dancing, gallop"},
    "खड़कार": {"hindi": "खड़खड़ाहट, टापों की ध्वनि, कोलाहल", "english": "clatter, rattling din of hooves"},
    "असवार": {"hindi": "सवार, घुड़सवार", "english": "rider, horseman"},
    "गुलज़ार": {"hindi": "गुलाबों की क्यारी, हरा-भरा उपवन", "english": "rose-garden, verdant bower"},
    "बुझारत": {"hindi": "पहेली, गूढ़ रहस्य", "english": "riddle, mystic enigma"},
    "चशमां": {"hindi": "आँखें, नेत्र", "english": "eyes"},
    "झूर": {"hindi": "तड़प-तड़प कर, विलाप करके", "english": "pining, weeping in distress"},
    "बे-कैद": {"hindi": "बंधन-मुक्त, असीम, परम स्वतंत्र", "english": "unconfined, boundless, free from fetters"},
    "तबकीं": {"hindi": "तबक, भुवन, लोक (सप्त पाताल और सप्त स्वर्ग)", "english": "cosmic strata, the fourteen realms of the universe"},
    "ख़राबात": {"hindi": "मदिरालय, खंडहर; सूफी रूपक में: सांसारिक बंधनों से मुक्त फकीरी", "english": "tavern of ruins; place of mystic surrender beyond orthodox forms"},
    "पैद": {"hindi": "अंत, सीमा, विनाश", "english": "perishing, end, extinction"}
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
        "completed_count": 80,
        "total": 160,
        "next_kafi_id": 81,
        "last_updated": "2026-10-17T17:25:00+05:30",
        "last_batch": "76-80",
        "status": "in_progress"
    }
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print(f"Checkpoint updated: 80/160 completed. Next ID: 81")

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
