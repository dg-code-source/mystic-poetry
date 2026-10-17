# -*- coding: utf-8 -*-
"""
Process Kafian 51 to 55 for Bulleh Shah Trilingual Edition.
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
        "id": 51,
        "title": "इश्क दी नवीयों नवीं बहार",
        "title_english": "The Springtime of Love is Ever New",
        "historical_context": "यह बाबा बुल्ले शाह की सर्वाधिक प्रसिद्ध, उल्लासपूर्ण और क्रांतिकारी काफ़ियों में से एक है। इसमें प्रेम (इश्क) को एक निरंतर नवीन, परिवर्तनकारी और मुक्तिदायक अनुभव के रूप में प्रस्तुत किया गया है। बुल्ले शाह रूढ़िवादी शरीअती बाह्याचारों—मस्जिद, वेद, कुरान के तोता-रटंत पाठ, तस्बीह और मुसल्ले—को त्यागकर हृदय के वास्तविक मंदिर और निरंतर खिलने वाली ईश्वरीय वसंत में प्रवेश करते हैं।",
        "meter": "पारंपरिक पंजाबी काफी (मात्रािक छंद, धुन: नवीयों नवीं बहार)",
        "raga": "राग काफी / बहार",
        "theme": "इश्क का चिर-नूतन स्वरूप, धार्मिक बाह्याडंबरों का तिरस्कार, आंतरिक शुद्धता और अद्वैत दर्शन",
        "stanzas": [
            {
                "original": [
                    "जां मैं सबक इश्क दा पढ़आ, मसजद कोलों जीउड़ा डरिआ,",
                    "डेरे जा ठाकर दे वड़्या, जित्थे वज्जदे नाद हज़ार ।",
                    "इश्क दी नवीयों नवीं बहार ।"
                ],
                "hindi_gloss": [
                    "जां (जब) मैं (मैंने) सबक (पाठ) इश्क (इश्क/प्रेम) दा (का) पढ़आ (पढ़ा), मसजद (मस्जिद) कोलों (से) जीउड़ा (हृदय/जी) डरिआ (डर गया/सहम गया),",
                    "डेरे (डेरे/आश्रम में) जा (जाकर) ठाकर (ठाकुर/प्रियतम प्रभु) दे (के) वड़्या (प्रविष्ट हुआ), जित्थे (जहाँ) वज्जदे (बजते हैं) नाद (अनहद नाद/दिव्य स्वर) हज़ार (हजारों) ।",
                    "इश्क (प्रेम) दी (की) नवीयों (नयी-से-) नवीं (नयी) बहार (वसंत/बहार) ।"
                ],
                "english_gloss": [
                    "जां (when) मैं (I) सबक (lesson) इश्क (of divine love) दा (of) पढ़आ (studied), मसजद (mosque) कोलों (from) जीउड़ा (my heart) डरिआ (fled in dread),",
                    "डेरे (abode) जा (having gone) ठाकर (of Thakur/Lord) दे (of) वड़्या (entered), जित्थे (where) वज्जदे (resound) नाद (mystic melodies) हज़ार (thousands) ।",
                    "इश्क (of love) दी (the) नवीयों (ever-) नवीं (new) बहार (spring/bloom) ।"
                ],
                "poetic_hindi": [
                    "जब से प्रेम-सबक दिल पढ़िया, मस्जिद से मन सहम उखड़िया,",
                    "ठाकुर-द्वारे जा पग धरिया, गूँजे अनहद नाद हज़ार ।",
                    "इश्क दी नवीयों नवीं बहार !"
                ],
                "poetic_english": [
                    "Since the lesson of true Love I chose to read, my heart from empty mosques did flee in fright,",
                    "And entered Thakur’s shrine to take its heed, where myriad holy melodies ignite.",
                    "The spring of Love is ever fresh and bright!"
                ]
            },
            {
                "original": [
                    "जां मैं रमज़ इश्क दी पाई, मैना तोता मार गवाई,",
                    "अन्दर बाहर होई सफ़ाई, जित वल्ल वेखां यारो यार ।",
                    "इश्क दी नवीयों नवीं बहार ।"
                ],
                "hindi_gloss": [
                    "जां (जब) मैं (मैंने) रमज़ (रहस्य/भेद) इश्क (प्रेम) दी (का) पाई (पाया), मैना (मैना) तोता (तोता—रटंत विद्या/द्वैत) मार (मारकर) गवाई (नष्ट कर दिया),",
                    "अन्दर (भीतर) बाहर (बाहर) होई (हो गई) सफ़ाई (पूर्ण निर्मलता/स्वच्छता), जित (जिस) वल्ल (ओर) वेखां (देखता हूँ) यारो (यार ही) यार (यार/प्रियतम ही प्रियतम) ।",
                    "इश्क (प्रेम) दी (की) नवीयों (नयी-से-) नवीं (नयी) बहार (बहार) ।"
                ],
                "english_gloss": [
                    "जां (when) मैं (I) रमज़ (subtle secret) इश्क (of love) दी (of) पाई (grasped), मैना (myna) तोता (parrot—rote prattle) मार (slew) गवाई (cast away),",
                    "अन्दर (within) बाहर (without) होई (occurred) सफ़ाई (complete purification), जित (which) वल्ल (way) वेखां (I gaze) यारो (friend/beloved) यार (beloved alone) ।",
                    "इश्क (of love) दी (the) नवीयों (ever-) नवीं (new) बहार (spring) ।"
                ],
                "poetic_hindi": [
                    "पाई जब इस इश्क की रमज़ें, तोता-मैना मार बहाए,",
                    "भीतर-बाहर शुद्धि छाई, जिधर लखूँ बस यार समाए ।",
                    "इश्क दी नवीयों नवीं बहार !"
                ],
                "poetic_english": [
                    "When Love's deep secret opened to my sight, I slew the mind’s rote parrots, freed the space,",
                    "Purged clean within and out in radiant light, everywhere now I behold my Lover’s face.",
                    "The spring of Love is ever fresh and bright!"
                ]
            },
            {
                "original": [
                    "हीर रांझे दे हो गए मेले, भुल्ली हीर ढूंडेदी बेले,",
                    "रांझा यार बुक्कल विच खेले, मैनूं सुध रही ना सार ।",
                    "इश्क दी नवीयों नवीं बहार ।"
                ],
                "hindi_gloss": [
                    "हीर (हीर) रांझे (रांझा) दे (का) हो (हो) गए (गए) मेले (मिलन/संयोग), भुल्ली (भूलकर) हीर (हीर) ढूंडेदी (ढूंढती फिरती है) बेले (जंगलों/घाटी में),",
                    "रांझा (रांझा) यार (प्रियतम) बुक्कल (आँचल/आलिंगन/हृदय) विच (में) खेले (क्रीड़ा करता है), मैनूं (मुझे) सुध (होश) रही (रही) ना (न) सार (खबर/ज्ञान) ।",
                    "इश्क (प्रेम) दी (की) नवीयों (नयी-से-) नवीं (नयी) बहार (बहार) ।"
                ],
                "english_gloss": [
                    "हीर (Heer) रांझे (Ranjha) दे (their) हो (became) गए (attained) मेले (union), भुल्ली (forgetful) हीर (Heer) ढूंडेदी (wanders searching) बेले (in pastures/groves),",
                    "रांझा (Ranjha) यार (the Friend) बुक्कल (embrace/bosom) विच (in) खेले (plays/resides), मैनूं (to me) सुध (awareness) रही (remained) ना (no) सार (clue/sense) ।",
                    "इश्क (of love) दी (the) नवीयों (ever-) नवीं (new) बहार (spring) ।"
                ],
                "poetic_hindi": [
                    "हीर-रांझणे का मेला छाया, हीर भटकी बन-बेले धाए,",
                    "रांझा यार तो बुक्कल बैठा, सुध-बुध मेरी सब बिसराए ।",
                    "इश्क दी नवीयों नवीं बहार !"
                ],
                "poetic_english": [
                    "Now Heer and Ranjha meet in bliss divine, yet forgetful Heer still combs the meadows bare;",
                    "While Ranjha plays within this cloak of mine, lost is all sense, erased each worldly care.",
                    "The spring of Love is ever fresh and bright!"
                ]
            },
            {
                "original": [
                    "बेद कुरानां पढ़ पढ़ थक्के, सज्जदे करद्यां घस्स गए मत्थे,",
                    "ना रब्ब तीरथ ना रब्ब मक्के, जिस पाइआ तिस नूर अनवार ।",
                    "इश्क दी नवीयों नवीं बहार ।"
                ],
                "hindi_gloss": [
                    "बेद (वेद) कुरानां (कुरान) पढ़ (पढ़) पढ़ (पढ़) थक्के (थक गए), सज्जदे (सजदे/माथा टेकते) करद्यां (करते-करते) घस्स (घिस) गए (गए) मत्थे (माथे),",
                    "ना (न) रब्ब (प्रभु) तीरथ (तीर्थ में) ना (न) रब्ब (प्रभु) मक्के (मक्का में), जिस (जिसने) पाइआ (पाया) तिस (उसे) नूर (ईश्वरीय नूर) अनवार (प्रकाश-पुंज) ।",
                    "इश्क (प्रेम) दी (की) नवीयों (नयी-से-) नवीं (नयी) बहार (बहार) ।"
                ],
                "english_gloss": [
                    "बेद (Vedas) कुरानां (Qurans) पढ़ (reading) पढ़ (reading) थक्के (wearied/exhausted), सज्जदे (prostrations) करद्यां (doing) घस्स (rubbed smooth/worn) गए (went) मत्थे (foreheads),",
                    "ना (neither) रब्ब (is Lord) तीरथ (at pilgrim pools) ना (nor) रब्ब (Lord) मक्के (at Mecca), जिस (whoever) पाइआ (found Him) तिस (upon him) नूर (divine light) अनवार (radiant splendor) ।",
                    "इश्क (of love) दी (the) नवीयों (ever-) नवीं (new) बहार (spring) ।"
                ],
                "poetic_hindi": [
                    "वेद-कुरान पढ़े थक हारे, सजदा कर-कर माथा घिसिया,",
                    "न रब तीरथ, न रब मक्के, जिसने लखा नूर-भर हँसिया ।",
                    "इश्क दी नवीयों नवीं बहार !"
                ],
                "poetic_english": [
                    "Reading both Vedas and Qurans men tire, their foreheads bruised by formal prayer and rite;",
                    "Neither in Mecca nor by pilgrim pyre, He dwells with those who bathe in living Light.",
                    "The spring of Love is ever fresh and bright!"
                ]
            },
            {
                "original": [
                    "फूक मुसल्ला भन्न सुट्ट लोटा, ना फड़ तसबी कासा सोटा,",
                    "आशक कहन्दे दे दे होका, तरक हलालों खाह मुरदार ।",
                    "इश्क दी नवीयों नवीं बहार ।"
                ],
                "hindi_gloss": [
                    "फूक (जला दे/फूंक दे) मुसल्ला (जा-नमाज़/प्रार्थना-चटाई) भन्न (तोड़) सुट्ट (फेंक) लोटा (वज़ू का लोटा), ना (मत) फड़ (पकड़) तसबी (तस्बीह/माला) कासा (भिक्षापात्र) सोटा (लाठी),",
                    "आशक (प्रेमी) कहन्दे (कहते हैं) दे (दे) दे (कर) होका (पुकार/घोषणा), तरक (त्याग) हलालों (पाखंडी हलाल को) खाह (खा ले) मुरदार (मुर्दार—सांसारिक रूप से तिरस्कृत सत्य) ।",
                    "इश्क (प्रेम) दी (की) नवीयों (नयी-से-) नवीं (नयी) बहार (बहार) ।"
                ],
                "english_gloss": [
                    "फूक (burn) मुसल्ला (prayer mat) भन्न (break) सुट्ट (cast away) लोटा (ablution pot), ना (do not) फड़ (grasp) तसबी (rosary) कासा (begging bowl) सोटा (ascetic staff),",
                    "आशक (lovers) कहन्दे (proclaim) दे (giving) दे (giving) होका (open call), तरक (abandon) हलालों (the lawful pretext) खाह (consume) मुरदार (the despised carrion/scorned truth) ।",
                    "इश्क (of love) दी (the) नवीयों (ever-) नवीं (new) बहार (spring) ।"
                ],
                "poetic_hindi": [
                    "फूँक मुसल्ला, तोड़ दे लोटा, तज दे माला, कासा, सोटा,",
                    "आशिक दें यह खुला ढिंढोरा: तज हलाल, खा ले मुरदार ।",
                    "इश्क दी नवीयों नवीं बहार !"
                ],
                "poetic_english": [
                    "Burn the prayer mat, break the pious cup, shun rod and beads and beggar's bowl of pride;",
                    "The heralds of pure Love lift voices up: forsake smug dogmas, take the truth denied!",
                    "The spring of Love is ever fresh and bright!"
                ]
            },
            {
                "original": [
                    "उमर गवाई विच मसीती, अन्दर भरिआ नाल पलीती,",
                    "कदे नमाज़ तौहीद ना कीती, हुन की करना एं शोर पुकार ।",
                    "इश्क दी नवीयों नवीं बहार ।"
                ],
                "hindi_gloss": [
                    "उमर (पूरी आयु) गवाई (खो दी/व्यर्थ गँवा दी) विच (में) मसीती (मस्जिद), अन्दर (भीतर/हृदय) भरिआ (भरा रहा) नाल (के साथ) पलीती (अपवित्रता/मैल/कपट),",
                    "कदे (कभी) नमाज़ (सच्ची नमाज़/प्रार्थना) तौहीद (एकेश्वरवाद/अद्वैत की) ना (नहीं) कीती (की), हुन (अब) की (क्या) करना (करता) एं (है) शोर (शोर) पुकार (पुकार/विलाप) ।",
                    "इश्क (प्रेम) दी (की) नवीयों (नयी-से-) नवीं (नयी) बहार (बहार) ।"
                ],
                "english_gloss": [
                    "उमर (life) गवाई (squandered) विच (inside) मसीती (the mosque), अन्दर (inside/heart) भरिआ (brimmed) नाल (with) पलीती (filth/hypocrisy),",
                    "कदे (ever) नमाज़ (prayer) तौहीद (of Divine Unity) ना (never) कीती (performed), हुन (now) की (why) करना (do) एं (you) शोर (clamor) पुकार (wailing) ।",
                    "इश्क (of love) दी (the) नवीयों (ever-) नवीं (new) बहार (spring) ।"
                ],
                "poetic_hindi": [
                    "उम्र गँवाई मस्जिद माहीं, भीतर मैल भरा अघ-कारी,",
                    "किए न सजदे एकत्व के, अब क्यों रटता रो-रो भारी ?",
                    "इश्क दी नवीयों नवीं बहार !"
                ],
                "poetic_english": [
                    "Within the mosque whole lifetimes passed in vain, while malice festered deep inside the chest;",
                    "Never didst thou true Unity attain—why make this frantic clamor and protest?",
                    "The spring of Love is ever fresh and bright!"
                ]
            },
            {
                "original": [
                    "इश्क भुलाइआ सजदा तेरा, हुन क्यों ऐवें पावें झेड़ा,",
                    "बुल्ल्हा हुन्दा चुप्प बथेरा, इश्क करेंदा मारो मार ।",
                    "इश्क दी नवीयों नवीं बहार ।"
                ],
                "hindi_gloss": [
                    "इश्क (इश्क ने) भुलाइआ (भुला दिया) सजदा (औपचारिक सजदा) तेरा (तेरा), हुन (अब) क्यों (क्यों) ऐवें (व्यर्थ) पावें (डालता है) झेड़ा (झगड़ा/विवाद),",
                    "बुल्ल्हा (बुल्ला) हुन्दा (रहना चाहता है) चुप्प (मौन/शांत) बथेरा (बहुत अधिक), इश्क (किंतु प्रेम) करेंदा (करता रहता है) मारो (मार-) मार (मार/प्रचंड विप्लव) ।",
                    "इश्क (प्रेम) दी (की) नवीयों (नयी-से-) नवीं (नयी) बहार (बहार) ।"
                ],
                "english_gloss": [
                    "इश्क (love) भुलाइआ (made to forget) सजदा (ritual prostrations) तेरा (thy), हुन (now) क्यों (why) ऐवें (needlessly) पावें (wilt thou raise) झेड़ा (quarrel/dispute),",
                    "बुल्ल्हा (Bulleh) हुन्दा (wishes to be) चुप्प (silent) बथेरा (greatly), इश्क (yet love) करेंदा (wages) मारो (relentless) मार (assault/overwhelming surge) ।",
                    "इश्क (of love) दी (the) नवीयों (ever-) नवीं (new) बहार (spring) ।"
                ],
                "poetic_hindi": [
                    "इश्क भुलाए सब दिखावे, क्यों तू व्यर्थ विवाद उठाए ?",
                    "बुल्ल्हा चाहे मौन ही रहना, इश्क प्रचंड लहर बन आए ।",
                    "इश्क दी नवीयों नवीं बहार !"
                ],
                "poetic_english": [
                    "Thy formal bowings Love hath swept away; why stir this petty controversy more?",
                    "Bulleh desires in quietude to stay, but fierce Love storms and breaks through every door!",
                    "The spring of Love is ever fresh and bright!"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी सूफी रहस्यवाद का सर्वोच्च उद्घोष है। प्रेम का मार्ग 'नवीयों नवीं बहार' (अनंत नवीनता) है—यह किसी मृत परंपरा या रूढ़ि में नहीं बंधता। जब साधक 'रमज़' (भेद) पा लेता है तो मस्जिद और ठाकुरद्वारे की बाह्य सीमाएं मिट जाती हैं; केवल प्रियतम का 'नूर अनवार' शेष रह जाता है। 'तरक हलालों खाह मुरदार' का प्रतीकात्मक अर्थ है कि संसार के पाखंडी आचार को त्यागकर वह सत्य स्वीकार करो जिसे संकीर्ण धर्मशास्त्र वर्जित मानते हैं।"
    },
    {
        "id": 52,
        "title": "इश्क हकीकी ने मुट्ठी कुड़े",
        "title_english": "Divine Love Hath Enraptured Me, O Sisters!",
        "historical_context": "इस काफी में बुल्ले शाह 'इश्क हकीकी' (परम ईश्वरीय प्रेम) की मदिरा में आकंठ डूबी जीवात्मा की विह्वल पुकार व्यक्त करते हैं। वे सांसारिक सखियों (कुड़े) से प्रियतम के अलौकिक देश का मार्ग पूछते हैं। यहां बाह्य पोथियों (मनतक, मअनी, कन्ज, कदूरी) की निस्सारता सिद्ध की गई है।",
        "meter": "पंजाबी दोहा-काफी मिश्रण",
        "raga": "राग आसा / पिलू",
        "theme": "इश्क हकीकी का सर्वग्रासी प्रभाव, बाह्य पुस्तकीय ज्ञान की व्यर्थता, प्रियतम के देश की खोज",
        "stanzas": [
            {
                "original": [
                    "इश्क हकीकी ने मुट्ठी कुड़े,  ",
                    "मैनूं दस्सो पिया दा देस ।"
                ],
                "hindi_gloss": [
                    "इश्क (इश्क) हकीकी (हकीकी/परम ईश्वरीय प्रेम) ने (ने) मुट्ठी (लूट लिया/वश में कर लिया) कुड़े (हे सखियो),",
                    "मैनूं (मुझे) दस्सो (बताओ) पिया (प्रियतम) दा (का) देस (देश/धाम) ।"
                ],
                "english_gloss": [
                    "इश्क (love) हकीकी (divine/real) ने (has) मुट्ठी (robbed/bewitched) कुड़े (O maidens/friends),",
                    "मैनूं (to me) दस्सो (tell/reveal) पिया (Beloved’s) दा (of) देस (realm/homeland) ।"
                ],
                "poetic_hindi": [
                    "इश्क-हकीकी ने मन लूटा, सखियो, हाल न पूछो लेश,",
                    "कोई बता दो, राह दिखा दो, कहाँ बसे पिय का परदेस ?"
                ],
                "poetic_english": [
                    "True Divine Love hath robbed my heart away, O sisters, hear my soul's confessing plea!",
                    "Point me the path without an hour’s delay: where lies the country of my Love to be?"
                ]
            },
            {
                "original": [
                    "माप्यां दे घर बाल इञाणी, पीत लगा लुट्टी कुड़े,  ",
                    "मैनूं दस्सो पिया दा देस ।"
                ],
                "hindi_gloss": [
                    "माप्यां (माता-पिता) दे (के) घर (घर में) बाल (बालक/अबोली) इञाणी (अंजान/नादान थी), पीत (प्रीत) लगा (लगाकर) लुट्टी (लूट ली गई/सर्वस्व वार बैठी) कुड़े (हे सखी),",
                    "मैनूं (मुझे) दस्सो (बताओ) पिया (प्रियतम) दा (का) देस (देश) ।"
                ],
                "english_gloss": [
                    "माप्यां (parents') दे (of) घर (house) बाल (child) इञाणी (innocent/simple), पीत (love) लगा (attaching) लुट्टी (plundered) कुड़े (O friends),",
                    "मैनूं (to me) दस्सो (tell) पिया (Beloved’s) दा (of) देस (land) ।"
                ],
                "poetic_hindi": [
                    "मात-पिता के घर थी भोली, बाल्यावस्था बीती शेष,",
                    "नेह लगा कर लुट गई सखियो, बतलाओ अब पिय का देस !"
                ],
                "poetic_english": [
                    "A naive child within my parents’ home, innocent of the world I lived so free;",
                    "Till love struck fast and robbed me bare to roam: where lies the country of my Love to be?"
                ]
            },
            {
                "original": [
                    "मनतक मअने कन्नज़ कदूरी, मैं पढ़ पढ़ इलम वगुच्ची कुड़े,  ",
                    "मैनूं दस्सो पिया दा देस ।"
                ],
                "hindi_gloss": [
                    "मनतक (मंतिक/तर्कशास्त्र) मअने (इल्म-ए-मआनी/शब्दार्थ विद्या) कन्नज़ (कन्ज-उद्-दकाइक/विधि-ग्रंथ) कदूरी (मुख्तसर अल-कुदूरी/धर्मशास्त्रीय ग्रंथ), मैं (मैंने) पढ़ (पढ़) पढ़ (पढ़कर) इलम (विद्या) वगुच्ची (भटक गई/नष्ट हो गई) कुड़े (हे सखियो),",
                    "मैनूं (मुझे) दस्सो (बताओ) पिया (प्रियतम) दा (का) देस (देश) ।"
                ],
                "english_gloss": [
                    "मनतक (logic/Mantiq) मअने (semantics/Ma'ani) कन्नज़ (Kanz-ud-Daqaiq) कदूरी (al-Quduri/canonical jurisprudence), मैं (I) पढ़ (reading) पढ़ (reading) इलम (knowledge/pedantry) वगुच्ची (ruined/lost astray) कुड़े (O maidens),",
                    "मैनूं (to me) दस्सो (tell) पिया (Beloved’s) दा (of) देस (land) ।"
                ],
                "poetic_hindi": [
                    "मंतिक, मअनी, कन्ज, कुदूरी, पोथी-पोथी भटकी रीत,",
                    "इल्म पढ़े तो मति खो बैठी, दिल को भावे बस पिय-प्रीत !"
                ],
                "poetic_english": [
                    "Logic and syntax, Kanz and bookish lore, I read and read till soul in grief was drowned;",
                    "Pedantic learning left me bruised and sore: where can the realm of my Beloved be found?"
                ]
            },
            {
                "original": [
                    "नमाज़ रोज़ा ओहनां की करना, जिन्हां प्रेम सुराही लुट्टी कुड़े,  ",
                    "मैनूं दस्सो पिया दा देस ।"
                ],
                "hindi_gloss": [
                    "नमाज़ (नमाज़) रोज़ा (रोज़ा/व्रत) ओहनां (उनको) की (क्या) करना (करना/प्रयोजन), जिन्हां (जिन्होंने) प्रेम (प्रेम की) सुराही (सुराही/प्याला) लुट्टी (लूट लिया/पी लिया) कुड़े (हे सखियो),",
                    "मैनूं (मुझे) दस्सो (बताओ) पिया (प्रियतम) दा (का) देस (देश) ।"
                ],
                "english_gloss": [
                    "नमाज़ (prayers) रोज़ा (fasting) ओहनां (to them) की (what) करना (need to perform), जिन्हां (who) प्रेम (of divine love) सुराही (the goblet) लुट्टी (plundered/drunk deep) कुड़े (O maidens),",
                    "मैनूं (to me) दस्सो (tell) पिया (Beloved’s) दा (of) देस (land) ।"
                ],
                "poetic_hindi": [
                    "क्या व्रत-रोज़े, क्या नमाज़ें, जिन्होंने पी ली प्रेम-सुराही,",
                    "मस्त हुए मतवारे सारे, मिट गई जग की चतुराई !"
                ],
                "poetic_english": [
                    "What need of fasting or of ritual line, for souls who drank Love’s goblet deep and sweet?",
                    "Intoxicated with the celestial wine, where is the homeland where my Love I meet?"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शौह दी मजलस बह के, सभ करनी मेरी छुट्टी कुड़े ,  ",
                    "मैनूं दस्सो पिया दा देस ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ला कहता है) शौह (शाह/प्रियतम प्रभु) दी (की) मजलस (सभा/संगति में) बह (बैठ) के (कर), सभ (समस्त) करनी (कर्मकांड/कर्तव्य-भार) मेरी (मेरी) छुट्टी (छूट गई/समाप्त हो गई) कुड़े (हे सखियो),",
                    "मैनूं (मुझे) दस्सो (बताओ) पिया (प्रियतम) दा (का) देस (देश) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh says) शौह (Lord/Master) दी (of) मजलस (company/presence) बह (sitting) के (having), सभ (all) करनी (formal actions/ritual burdens) मेरी (my) छुट्टी (dropped away/relieved) कुड़े (O friends),",
                    "मैनूं (to me) दस्सो (tell) पिया (Beloved’s) दा (of) देस (land) ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा शौह की संगति बैठूं, छूटे सारे कर्म-बखेड़े,",
                    "कोई बताओ पिय की नगरी, कब पहुँचूँगी पिय के डेरे ?"
                ],
                "poetic_english": [
                    "Seated with Lordly Bullah face to face, ritual obligations shed their weight;",
                    "Absorbed within the shelter of His grace, reveal, O sisters, my Beloved’s gate!"
                ]
            }
        ],
        "philosophical_meaning": "'इश्क हकीकी' के सम्मुख पारंपरिक इस्लामी न्यायशास्त्र की पुस्तकें (मंतिक, कन्ज-उद्-दकाइक, मुख्तसर-अल-कुदूरी) पूरी तरह निरर्थक सिद्ध होती हैं। बुद्धि के तर्क जब शांत होते हैं, तभी प्रेम-सुराही का रस मिलता है। इस काफी में जीवात्मा की बाल-सुलभ सरलता और सांसारिक बंधनों से संपूर्ण मुक्ति का उत्सव है।"
    },
    {
        "id": 53,
        "title": "इस नेहुं दी उलटी चाल",
        "title_english": "The Inverted, Paradoxical Ways of Love",
        "historical_context": "इस काफी में बाबा बुल्ले शाह प्रेम के कठोर, अग्नि-तुल्य और विरोधाभासी विधान का वर्णन करते हैं। इतिहास के महान पैगंबरों और सूफियों—हज़रत अय्यूब (साबिर), हज़रत ज़करिया, हज़रत यह्या, मंसूर हल्लाज और हज़रत सुलेमान—का दृष्टांत देकर वे बताते हैं कि ईश्वर जिससे प्रेम करता है, उसे सांसारिक सुख नहीं बल्कि घोर आत्मिक व शारीरिक परीक्षाएं और शहादत प्रदान करता है।",
        "meter": "पंजाबी काफी (सोरठा/दोहा संकर, ध्रुपद लय)",
        "raga": "राग मारू / सोरठ",
        "theme": "इश्क की कठिन परीक्षा, पैगंबरों और सूफी शहीदों का बलिदान, आत्म-समर्पण",
        "stanzas": [
            {
                "original": [
                    "साबिर ने जद नेहुं लगाइआ, देख पिया ने की दिखलाइआ,  ",
                    "रग रग अन्दर किरम चलाइआ, ज़ोरावर दी गल्ल मुहाल,  ",
                    "इस नेहुं दी उलटी चाल ।"
                ],
                "hindi_gloss": [
                    "साबिर (अय्यूब पैगंबर—धैर्यवान) ने (ने) जद (जब) नेहुं (प्रेम) लगाइआ (लगाया), देख (देख) पिया (प्रियतम ने) ने (ने) की (क्या) दिखलाइआ (दिखाया),",
                    "रग (रग-) रग (रग/नस-नस) अन्दर (में) किरम (कीड़े/कृमि) चलाइआ (चला दिए/पैदा कर दिए), ज़ोरावर (उस सर्वशक्तिमान ईश्वर) दी (की) गल्ल (लीला/बात) मुहाल (अगम्य/अति कठिन) ,",
                    "इस (इस) नेहुं (प्रेम) दी (की) उलटी (उल्टी/विचित्र) चाल (रीति/चाल) ।"
                ],
                "english_gloss": [
                    "साबिर (Prophet Job/the Patient one) ने (when) जद (when) नेहुं (love) लगाइआ (pledged), देख (behold) पिया (the Beloved) ने (what) की (what) दिखलाइआ (revealed),",
                    "रग (vein) रग (in every vein) अन्दर (within) किरम (worms/parasites) चलाइआ (caused to crawl), ज़ोरावर (of the Almighty) दी (of) गल्ल (matter/ways) मुहाल (beyond comprehension) ,",
                    "इस (of this) नेहुं (love) दी (the) उलटी (paradoxical/reversed) चाल (ways/nature) ।"
                ],
                "poetic_hindi": [
                    "साबिर ने जब प्रीत लगाई, देख पिया ने क्या दिखलाई,",
                    "रग-रग में कीड़े चलवाए, ज़ोरावर की समझ न आई ।",
                    "इस नेहुं दी उलटी चाल !"
                ],
                "poetic_english": [
                    "When patient Job pledged love to God on high, behold what trials the Beloved decreed:",
                    "In every vein crawled worms beneath his eye—inscrutable the Lord’s almighty deed!",
                    "How strangely inverted are the ways of Love!"
                ]
            },
            {
                "original": [
                    "ज़करिया ने जद पाइआ कहारा, जिस दम वज्या इश्क नग्गारा,  ",
                    "धरिआ सिर ते तिक्खा आरा, कीता अड्ड जवाल,  ",
                    "इस नेहुं दी उलटी चाल ।"
                ],
                "hindi_gloss": [
                    "ज़करिया (पैगंबर ज़करिया) ने (ने) जद (जब) पाइआ (पाया/अनुभव किया) कहारा (प्रभु का प्रकोप/कहर), जिस (जिस) दम (क्षण) वज्या (बजा) इश्क (इश्क का) नग्गारा (नगाड़ा),",
                    "धरिआ (रखा गया) सिर (सिर) ते (पर) तिक्खा (तीखा) आरा (आरा/चीरने वाला आरी), कीता (कर दिया) अड्ड (दो टुकड़े) जवाल (विनाश/कष्ट में) ,",
                    "इस (इस) नेहुं (प्रेम) दी (की) उलटी (विचित्र) चाल (चाल) ।"
                ],
                "english_gloss": [
                    "ज़करिया (Prophet Zechariah) ने (when) जद (when) पाइआ (met) कहारा (the fierce trial/wrath), जिस (which) दम (moment) वज्या (sounded) इश्क (of love) नग्गारा (the war-drum),",
                    "धरिआ (was placed) सिर (head) ते (upon) तिक्खा (sharp) आरा (saw), कीता (severed) अड्ड (in twain) जवाल (in ordeal/anguish) ,",
                    "इस (of this) नेहुं (love) दी (the) उलटी (reversed) चाल (gait/course) ।"
                ],
                "poetic_hindi": [
                    "ज़करिया पर जब इश्क पुकारा, बजा प्रेम का रण-नगारा,",
                    "सिर पर तीखा आरा धरकर, तन को दो टुकड़ों में उतारा ।",
                    "इस नेहुं दी उलटी चाल !"
                ],
                "poetic_english": [
                    "When Zechariah heard the mystic drum of Love resounding through the boundless skies,",
                    "A saw upon his holy head had come, which cut his flesh in twain before men's eyes!",
                    "How strangely inverted are the ways of Love!"
                ]
            },
            {
                "original": [
                    "जदों यहीए ने पाई झाती, रमज़ इश्क दी लाई काती,  ",
                    "जलवा दित्ता आपना ज़ाती, तन खंजर कीता लाल,  ",
                    "इस नेहुं दी उलटी चाल ।"
                ],
                "hindi_gloss": [
                    "जदों (जब) यहीए (पैगंबर यह्या/जॉन द बैपटिस्ट) ने (ने) पाई (डाली) झाती (हृदय में दृष्टि/प्रेम-झांकी), रमज़ (भेद) इश्क (प्रेम) दी (की) लाई (लगाई) काती (कैंची/छुरी),",
                    "जलवा (तेज/साक्षात्कार) दित्ता (दिया) आपना (अपना) ज़ाती (स्वरूपीय/तात्विक), तन (शरीर को) खंजर (खंजर ने) कीता (कर दिया) लाल (रक्त-रंजित) ,",
                    "इस (इस) नेहुं (प्रेम) दी (की) उलटी (उल्टी) चाल (चाल) ।"
                ],
                "english_gloss": [
                    "जदों (when) यहीए (Prophet Yahya/John) ने (when) पाई (cast) झाती (glance within), रमज़ (secret) इश्क (of love) दी (of) लाई (struck) काती (shears/knife),",
                    "जलवा (revelation) दित्ता (granted) आपना (His own) ज़ाती (essential/divine Self), तन (body) खंजर (dagger) कीता (made) लाल (crimson red) ,",
                    "इस (of this) नेहुं (love) दी (the) उलटी (reversed) चाल (ways) ।"
                ],
                "poetic_hindi": [
                    "यहीया ने जब झाँक निहारा, प्रेम-छुरी का वार स्वीकारा,",
                    "प्रभु ने अपना नूर दिखाया, खंजर से तन लहू-लुहारा ।",
                    "इस नेहुं दी उलटी चाल !"
                ],
                "poetic_english": [
                    "When Yahya gazed upon the mystic spark, Love’s shears of sacrifice cut straight and keen;",
                    "The Lord revealed His Essence in the dark, while daggers dyed his martyred frame unseen!",
                    "How strangely inverted are the ways of Love!"
                ]
            },
            {
                "original": [
                    "आप इशारा अक्ख दा कीता, तां मधुवा मनसूर ने पीता,  ",
                    "सूली चढ़ के दरशन लीता, होया इश्क कमाल,  ",
                    "इस नेहुं दी उलटी चाल ।"
                ],
                "hindi_gloss": [
                    "आप (स्वयं प्रभु ने) इशारा (इशारा/संकेत) अक्ख (आँख) दा (का) कीता (किया), तां (तब) मधुवा (प्रेम-मदिरा) मनसूर (मंसूर हल्लाज) ने (ने) पीता (पी ली),",
                    "सूली (सूली/फांसी के तख्ते पर) चढ़ (चढ़) के (कर) दरशन (दर्शन/साक्षात्कार) लीता (पाया), होया (हुआ) इश्क (इश्क का) कमाल (परम चमत्कार/कमाल) ,",
                    "इस (इस) नेहुं (प्रेम) दी (की) उलटी (उल्टी) चाल (चाल) ।"
                ],
                "english_gloss": [
                    "आप (Himself) इशारा (glance/gesture) अक्ख (of eye) दा (of) कीता (made), तां (then) मधुवा (wine of ecstatic love) मनसूर (Mansur al-Hallaj) ने (drank) पीता (drank),",
                    "सूली (the gallows) चढ़ (ascending) के (having) दरशन (vision of Beloved) लीता (beheld), होया (became) इश्क (of love) कमाल (consummate wonder) ,",
                    "इस (of this) नेहुं (love) दी (the) उलटी (reversed) चाल (nature) ।"
                ],
                "poetic_hindi": [
                    "प्रभु ने नयनों से मति मारी, तब मंसूर पिया मतवारी,",
                    "सूली चढ़ कर पाया दर्शन, इश्क-कमाल हुआ बलिहारी ।",
                    "इस नेहुं दी उलटी चाल !"
                ],
                "poetic_english": [
                    "The Lord winked softly with His eye of grace, and Hallaj drank the wine of ecstatic thrill;",
                    "Mounted the gallows to behold His face—such was the wonder of Love's sovereign will!",
                    "How strangely inverted are the ways of Love!"
                ]
            },
            {
                "original": [
                    "सुलेमान नूं इश्क जो आया, मुन्दरा हत्थों चा गवाइआ,  ",
                    "तख़त ना परियां दा फिर आया, भट्ठ झोके प्या बेहाल,  ",
                    "इस नेहुं दी उलटी चाल ।"
                ],
                "hindi_gloss": [
                    "सुलेमान (हज़रत सुलेमान/सोलोमन) नूं (को) इश्क (इश्क) जो (जो) आया (आया/व्यापा), मुन्दरा (अंगूठी/मुद्रिका—राजसत्ता का प्रतीक) हत्थों (हाथ से) चा (उठाकर) गवाइआ (गंवा दी/खो दी),",
                    "तख़त (सिंहासन) ना (न) परियां (परियों) दा (का) फिर (पुनः) आया (आया), भट्ठ (भट्टी) झोके (झोंकता फिरा/लकड़ी जलाता रहा) प्या (पड़ा रहा) बेहाल (बेहाल/दीन-हीन) ,",
                    "इस (इस) नेहुं (प्रेम) दी (की) उलटी (उल्टी) चाल (चाल) ।"
                ],
                "english_gloss": [
                    "सुलेमान (Solomon) नूं (to) इश्क (love) जो (which) आया (came), मुन्दरा (magic seal-ring) हत्थों (from his hand) चा (was) गवाइआ (lost/cast),",
                    "तख़त (throne) ना (no more) परियां (of fairies) दा (of) फिर (again) आया (returned), भट्ठ (furnace/kiln) झोके (stoking coals) प्या (lay) बेहाल (wretched/distressed) ,",
                    "इस (of this) नेहुं (love) दी (the) उलटी (reversed) चाल (ways) ।"
                ],
                "poetic_hindi": [
                    "सुलेमान को नेह सताया, हाथ से राज-मुंदरी को गँवाया,",
                    "परी-तख़्त फिर हाथ न आया, भट्ठी झोंके भिक्षुक भाया ।",
                    "इस नेहुं दी उलटी चाल !"
                ],
                "poetic_english": [
                    "When Solomon was struck by Love’s sweet pain, he cast his sovereign signet-ring away;",
                    "The throne of fairies ne'er returned again, stoking hot ovens as a serf each day!",
                    "How strangely inverted are the ways of Love!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हे शाह हुन चुप्प चंगेरी, ना कर एथे ऐड दलेरी,  ",
                    "गल्ल ना बणदी तेरी मेरी, छड्ड दे सारे वहम ख़्याल,  ",
                    "इस नेहुं दी उलटी चाल ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हे (बुल्ले) शाह (शाह) हुन (अब) चुप्प (मौन रहना ही) चंगेरी (उत्तम/श्रेष्ठ है), ना (मत) कर (कर) एथे (यहाँ) ऐड (इतनी बड़ी) दलेरी (साहस/गुस्ताखी),",
                    "गल्ल (बात) ना (नहीं) बणदी (बनती) तेरी (तेरी) मेरी (मेरी—मन के तर्कों से), छड्ड (छोड़) दे (दे) सारे (समस्त) वहम (भ्रम) ख़्याल (काल्पनिक विचार) ,",
                    "इस (इस) नेहुं (प्रेम) दी (की) उलटी (उल्टी) चाल (चाल) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हे (Bulleh) शाह (Shah) हुन (now) चुप्प (silence) चंगेरी (is far better), ना (do not) कर (make) एथे (here) ऐड (such) दलेरी (audacity/boldness),",
                    "गल्ल (matter) ना (not) बणदी (settles/fits) तेरी (thy) मेरी (mine—by petty intellect), छड्ड (abandon) दे (give up) सारे (all) वहम (delusions) ख़्याल (vain fancies) ,",
                    "इस (of this) नेहुं (love) दी (the) उलटी (reversed) चाल (course) ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हे शाह! अब मौन भलाई, तज दे साहस की तरुणाई,",
                    "तेरी-मेरी बात न टिकती, छोड़ वहम की माया-खाई ।",
                    "इस नेहुं दी उलटी चाल !"
                ],
                "poetic_english": [
                    "O Bulleh Shah, hold silent now thy tongue, venture no reckless boasts before His gate;",
                    "By mortal minds Love's praises can't be sung—drop all illusions, bow to sovereign Fate!",
                    "How strangely inverted are the ways of Love!"
                ]
            }
        ],
        "philosophical_meaning": "सूफी परंपरा में 'बला' (कष्ट/परीक्षण) को 'विलायत' (ईश्वरीय मित्रता) का उपहार माना गया है। हदीस-ए-कुदसी का वचन है: 'अशद्दुल् बला-ए अलल अंबिया' (सबसे कठिन परीक्षाएं नबियों की होती हैं)। बुल्ले शाह इस सत्य को उद्घाटित करते हैं कि सांसारिक मनुष्य जिसे सौभाग्य मानते हैं, इश्क की दुनिया में वह शून्य है; और जिसे संसार विपत्ति या मृत्यु कहता है, वह प्रेमी के लिए प्रियतम का आलिंगन है।"
    },
    {
        "id": 54,
        "title": "जिचर ना इश्क मजाज़ी लागे",
        "title_english": "Until Metaphorical Love Awakens the Heart",
        "historical_context": "सूफी अध्यात्म में एक मौलिक सिद्धांत है: 'अल-मजाज़ु क़ंतरातुल हक़ीक़ा' (सांसारिक/रूपक प्रेम ही परम सत्य के प्रेम का सेतु है)। इस काफी में बुल्ले शाह समझाते हैं कि जब तक मनुष्य के हृदय में किसी रूपवान के प्रति तीव्र अनुराग (इश्क मजाज़ी) नहीं जागता, तब तक वह निराकार परमेश्वर (इश्क हकीकी) के विरह और मिलन को समझ ही नहीं सकता। जैसे बिना धागे के सुई वस्त्र नहीं सिल सकती, वैसे ही बिना भाव के आत्मा परमात्मा से नहीं जुड़ सकती।",
        "meter": "पंजाबी दोहा/चौपाई छंद",
        "raga": "राग तिलंग / काफी",
        "theme": "इश्क मजाज़ी और इश्क हकीकी का संबंध, सुई और धागे का रूपक, अहंकार का क्षय",
        "stanzas": [
            {
                "original": [
                    "जिचर ना इश्क मजाज़ी लागे ।  ",
                    "सूई सीवे ना बिन धागे ।  ",
                    "इश्क मजाज़ी दाता है ।  ",
                    "जिस पिच्छे मसत हो जाता है ।"
                ],
                "hindi_gloss": [
                    "जिचर (जब तक) ना (नहीं) इश्क (इश्क) मजाज़ी (मजाज़ी/सांसारिक-रूपक प्रेम) लागे (लगता/जागृत होता) ।",
                    "सूई (सूई) सीवे (सीलती/जोड़ती) ना (नहीं) बिन (बिना) धागे (धागे के) ।",
                    "इश्क (प्रेम) मजाज़ी (मजाज़ी) दाता (दाता/अनुग्रहकारी शिक्षक) है ।",
                    "जिस (जिसके) पिच्छे (पीछे/प्रभाव से) मसत (मस्त/मदमस्त) हो (हो) जाता (जाता) है ।"
                ],
                "english_gloss": [
                    "जिचर (as long as) ना (not) इश्क (love) मजाज़ी (metaphorical/earthly) लागे (strikes/awakens) ।",
                    "सूई (needle) सीवे (sews/stitches) ना (not) बिन (without) धागे (thread) ।",
                    "इश्क (love) मजाज़ी (metaphorical) दाता (the generous giver/catalyst) है (is) ।",
                    "जिस (which) पिच्छे (following/through) मसत (intoxicated) हो (becomes) जाता (goes) है (is) ।"
                ],
                "poetic_hindi": [
                    "जब तक नैन मजाज़ी जागे, सूई सिले न बिना ही धागे,",
                    "इश्क-मजाज़ी प्रथम सहारा, जिसके पीछे मन मतवारा !"
                ],
                "poetic_english": [
                    "Till earthly love ignites the slumbering soul, no needle stitches cloth without a thread;",
                    "Metaphoric love makes broken spirits whole, and leaves the mind in holy madness led!"
                ]
            },
            {
                "original": [
                    "इश्क जिन्हां दी हड्डीं पैंदा,  ",
                    "सोई निरजीवत मर जांदा,  ",
                    "इश्क पिता ते माता है,  ",
                    "जिस पिच्छे मसत हो जाता है ।"
                ],
                "hindi_gloss": [
                    "इश्क (प्रेम) जिन्हां (जिनकी) दी (की) हड्डीं (हड्डियों/अस्थि-मज्जा में) पैंदा (प्रविष्ट होता है),",
                    "सोई (वही) निरजीवत (जीते-जी निर्जीव/अहं-शून्य होकर) मर (मर) जांदा (जाता है),",
                    "इश्क (इश्क ही) पिता (पिता) ते (तथा) माता (माता) है (है),",
                    "जिस (जिसके) पिच्छे (कारण) मसत (मस्त) हो (हो) जाता (जाता) है ।"
                ],
                "english_gloss": [
                    "इश्क (love) जिन्हां (those whose) दी (of) हड्डीं (bones/marrow) पैंदा (enters),",
                    "सोई (they alone) निरजीवत (lifeless to ego/dead before dying) मर (die) जांदा (go),",
                    "इश्क (love) पिता (father) ते (and) माता (mother) है (is),",
                    "जिस (after which) पिच्छे (behind/in pursuit) मसत (ecstatic) हो (becomes) जाता (goes) है (is) ।"
                ],
                "poetic_hindi": [
                    "इश्क समाए जिनकी हड्डी, जीते-जी वे जग से मरते,",
                    "इश्क ही माता, इश्क पिता है, मदमाते भव-सागर तरते !"
                ],
                "poetic_english": [
                    "Those in whose marrow Love doth sink its shaft, die to the ego while they walk the earth;",
                    "Love is the parent of celestial craft, whose holy madness brings the soul rebirth!"
                ]
            },
            {
                "original": [
                    "आशक दा तन सुक्कदा जाए,  ",
                    "मैं खड़ी चन्द पिर के साए,  ",
                    "वेख मशूकां खिड़ खिड़ हासे,  ",
                    "इश्क बेताल पढ़ाता है ।"
                ],
                "hindi_gloss": [
                    "आशक (प्रेमी) दा (का) तन (शरीर) सुक्कदा (सूखता) जाए (जाता है),",
                    "मैं (मैं) खड़ी (खड़ी हूँ) चन्द (चाँद जैसे) पिर (प्रियतम) के (के) साए (छाया/आलोक में),",
                    "वेख (देखकर) मशूकां (माशूक/प्रियतम के) खिड़ (खिल-खिलाकर) खिड़ (खिल-खिलाकर) हासे (हँसी/मुस्कान),",
                    "इश्क (इश्क) बेताल (असाधारण/बिना ताल का नृत्य) पढ़ाता (सिखाता) है ।"
                ],
                "english_gloss": [
                    "आशक (lover’s) दा (of) तन (flesh/body) सुक्कदा (withers/wastes) जाए (away),",
                    "मैं (I) खड़ी (stand) चन्द (moon-like) पिर (Beloved) के (of) साए (shadow/presence),",
                    "वेख (beholding) मशूकां (Beloved’s) खिड़ (blooming) खिड़ (blooming) हासे (radiant laughter),",
                    "इश्क (love) बेताल (unmeasured rhythm/wild rapture) पढ़ाता (teaches) है (is) ।"
                ],
                "poetic_hindi": [
                    "सूख चला आशिक का काया, चंदा जैसे पिय की छाया,",
                    "हँसे माशूक जब मंद-मंद हँसी, इश्क बेताल का नाच नचाया !"
                ],
                "poetic_english": [
                    "The lover's body withers thin and pale, while standing under my Moon-Lover’s grace;",
                    "When sweet Beloved smiles behind the veil, wild rhythmic ecstasies dissolve the space!"
                ]
            },
            {
                "original": [
                    "जिस ते इश्क इह आया है,  ",
                    "उह बेबस कर दिखलाइआ है,  ",
                    "नशा रोम रोम में आया है,  ",
                    "इस विच ना रत्ती उहला है,"
                ],
                "hindi_gloss": [
                    "जिस (जिस) ते (पर) इश्क (इश्क) इह (यह) आया (आया) है,",
                    "उह (उसे) बेबस (विवश/असहाय) कर (करके) दिखलाइआ (दिखा दिया) है,",
                    "नशा (प्रेम-नशा) रोम (रोम-) रोम (रोम) में (में) आया (छा गया) है,",
                    "इस (इस) विच (में) ना (नहीं) रत्ती (रत्ती-भर/ज़रा भी) उहला (पर्दा/छिपाव) है ।"
                ],
                "english_gloss": [
                    "जिस (upon whom) ते (upon) इश्क (love) इह (this) आया (arrives) है (has),",
                    "उह (him) बेबस (helpless/surrendered) कर (making) दिखलाइआ (manifested) है (has),",
                    "नशा (intoxication) रोम (every pore) रोम (every pore) में (in) आया (entered) है (has),",
                    "इस (this) विच (in) ना (not) रत्ती (iota of) उहला (veil/concealment) है (is) ।"
                ],
                "poetic_hindi": [
                    "जिस पर यह प्रेम-रंग चढ़ जाए, विवश करे, निज रूप दिखाए,",
                    "रोम-रोम में सुरूर समाए, रत्ती-भर पर्दा न सुहाए !"
                ],
                "poetic_english": [
                    "Upon whom this fierce passion casts its spell, it strips all power and renders self undone;",
                    "In every single pore its splendors swell, leaving no veil beneath the blazing sun!"
                ]
            },
            {
                "original": [
                    "हर तरफ दसेंदा मौला है,  ",
                    "बुल्ल्हा आशक वी हुन तरदा है,  ",
                    "जिस फिकर पिया दे घर दा है,  ",
                    "रब्ब मिलदा वेख उचरदा है ।  ",
                    "मन अन्दर होया झाता है ।  ",
                    "जिस पिच्छे मसत हो जाता है ।"
                ],
                "hindi_gloss": [
                    "हर (प्रत्येक) तरफ (ओर) दसेंदा (दिखाई देता) मौला (ईश्वर/मौला) है,",
                    "बुल्ल्हा (बुल्ला) आशक (आशिक) वी (भी) हुन (अब) तरदा (भवसागर से पार होता) है,",
                    "जिस (जिसको) फिकर (चिंता/ध्यान) पिया (प्रियतम) दे (के) घर (घर) दा (का) है,",
                    "रब्ब (प्रभु) मिलदा (मिलता हुआ) वेख (देखकर) उचरदा (पुकारता/उच्चारता) है ।",
                    "मन (हृदय के) अन्दर (भीतर) होया (हुआ) झाता (साक्षात्कार/झांकी) है ।",
                    "जिस (जिसके) पिच्छे (पीछे/कारण) मसत (मस्त) हो (हो) जाता (जाता) है ।"
                ],
                "english_gloss": [
                    "हर (every) तरफ (direction) दसेंदा (is visible) मौला (the Divine Master) है (is),",
                    "बुल्ल्हा (Bulleh) आशक (the lover) वी (too) हुन (now) तरदा (swims across/crosses) है (is),",
                    "जिस (who) फिकर (yearning/care) पिया (Beloved’s) दे (of) घर (home) दा (of) है (has),",
                    "रब्ब (Lord) मिलदा (meeting) वेख (seeing) उचरदा (utters/cries out) है ।",
                    "मन (mind/heart) अन्दर (within) होया (occurred) झाता (glance/inner illumination) है ।",
                    "जिस (after which) पिच्छे (behind/in wake) मसत (intoxicated) हो (becomes) जाता (goes) है (is) ।"
                ],
                "poetic_hindi": [
                    "चारों ओर लखे बस मौला, बुल्ल्हा आशिक तरता जाए,",
                    "पिय के घर की सुध धर मन में, रब को लख कर वचन सुनाए ।",
                    "भीतर ही झांकी प्रकटी है, मन मस्त हुआ मुस्काए !"
                ],
                "poetic_english": [
                    "On every side the Lord alone appears, and Bulleh the ecstatic swims across;",
                    "Mindful of the Beloved's home he steers, counting all worldly pride as dust and dross.",
                    "Within the inner sanctum shines the grace, where drunken joy beholds Him face to face!"
                ]
            }
        ],
        "philosophical_meaning": "सूफी दर्शन में प्रेम की सीढ़ी संसार (मजाज़) से शुरू होकर हकीकत (सत्य) तक जाती है। सुई और धागे का दृष्टांत अद्भुत है—सुई (हृदय) बिना धागे (मजाज़ी प्रेम के तार) के दो अलग टुकड़ों (आत्मा और परमात्मा) को जोड़ नहीं सकती। जब प्रेम हड्डियों तक पहुंच जाता है, तो द्वैत का पर्दा हट जाता है और सर्वत्र केवल 'मौला' ही दृष्टिगोचर होता है।"
    },
    {
        "id": 55,
        "title": "जिन्द कुड़िकी दे मूंह आई",
        "title_english": "My Soul Has Fallen Into the Snare",
        "historical_context": "यह बाबा बुल्ले शाह की सबसे मार्मिक, दीर्घ और विरह-दग्ध काफ़ियों में से एक है। 13 बंधों में रचित यह रचना जीवात्मा की उस अवस्था को दर्शाती है जहाँ वह संसार और ईश्वर दोनों के बीच फँस चुकी है। 'कुड़िकी' (शिकारी के फंदे/पिंजरे) का रूपक बताता है कि प्रभु-प्रेम में पड़ना एक ऐसा जाल है जिससे मुक्ति असंभव है—न आगे जाया जा सकता है, न पीछे लौटा जा सकता है।",
        "meter": "पंजाबी काफी (प्रबंधात्मक दीर्घ छंद, 13 अंतरे)",
        "raga": "राग सोरठ / जोगिया",
        "theme": "इश्क का फंदा, विरह की असह्य वेदना, शरीअत बनाम तसव्वुफ, सर्वव्यापकता का संशय और अद्वैत साक्षात्कार",
        "stanzas": [
            {
                "original": [
                    "आपे हैं तूं लहमका लहमी, आपे हैं तूं न्यारा,  ",
                    "गल्लां सुन तेरियां, मेरा अकल गिआ उड्ड सारा,  ",
                    "शरियत तों बेशरियत करके, भली खुभ्भन विच पाई ।  ",
                    "जिन्द कुड़िकी दे मूंह आई ।"
                ],
                "hindi_gloss": [
                    "आपे (स्वयं ही) हैं (है) तूं (तू) लहमका लहमी (लहमका लहमी—मांस में मांसवत मिला हुआ/सर्वव्यापी), आपे (स्वयं ही) हैं (है) तूं (तू) न्यारा (सर्वथा पृथक/अलिप्त),",
                    "गल्लां (बातें) सुन (सुनकर) तेरियां (तेरी), मेरा (मेरी) अकल (बुद्धि) गिआ (गई) उड्ड (उड़) सारा (पूरी तरह),",
                    "शरियत (रूढ़िवादी शरीअत) तों (से) बेशरियत (बंधन-मुक्त/मस्त) करके (करके), भली (अच्छी) खुभ्भन (दलदल/गहरे भंवर) विच (में) पाई (डाल दी) ।",
                    "जिन्द (मेरी जान/जीवात्मा) कुड़िकी (शिकारी के फंदे/पिंजरे) दे (के) मूंह (मुहाने पर) आई (आ गई है) ।"
                ],
                "english_gloss": [
                    "आपे (Thyself) हैं (art) तूं (Thou) लहमका लहमी (flesh within my flesh/immanent), आपे (Thyself) हैं (art) तूं (Thou) न्यारा (transcendent/distinct),",
                    "गल्लां (words/mysteries) सुन (hearing) तेरियां (Thy), मेरा (my) अकल (intellect) गिआ (went) उड्ड (flown away) सारा (completely),",
                    "शरियत (from orthodoxy) तों (from) बेशरियत (unbound/heretical) करके (having made), भली (pretty) खुभ्भन (quagmire/morass) विच (in) पाई (thrust) ।",
                    "जिन्द (my soul) कुड़िकी (snare/trap) दे (of) मूंह (mouth/jaws) आई (has entered) ।"
                ],
                "poetic_hindi": [
                    "मांस में मांस तू, आप ही न्यारा, बातें सुन मति भागी सारी,",
                    "शरीअत छुड़ा कर बे-शरीअत कीना, गहरी दलदल में पटकी बेचारी ।",
                    "जिन्द कुड़िकी दे मूंह आई !"
                ],
                "poetic_english": [
                    "Thou art the flesh within my flesh, yet far beyond all mortal trace;",
                    "Hearing Thy words my wits took flight, stripped bare of intellect and grace.",
                    "Cast out of dogma into swamps, my struggling spirit trapped in sighs:",
                    "Caught in the snare my frail soul lies!"
                ]
            },
            {
                "original": [
                    "ज़र्रा इश्क तुसाडा दिसदा, परबत कोलों भारा,  ",
                    "इक घड़ी दे वेखन कारन, चुक्क लिआ जग्ग सारा,  ",
                    "कीती मेहनत मिलदी नाहीं, हुन की करे लुकाई ।  ",
                    "जिन्द कुड़िकी दे मूंह आई ।"
                ],
                "hindi_gloss": [
                    "ज़र्रा (एक कण-मात्र) इश्क (प्रेम) तुसाडा (आपका) दिसदा (दिखता है), परबत (पहाड़) कोलों (से भी) भारा (भारी),",
                    "इक (एक) घड़ी (पल/क्षण) दे (के) वेखन (दर्शन करने के) कारन (लिए), चुक्क (सिर पर उठा) लिआ (लिया) जग्ग (संसार का विरोध) सारा (सारा),",
                    "कीती (की हुई) मेहनत (साधना/प्रयास) मिलदी (फलवती होती) नाहीं (नहीं), हुन (अब) की (क्या) करे (करे) लुकाई (यह बेबस जन/सृष्टि) ।",
                    "जिन्द (मेरी आत्मा) कुड़िकी (फंदे) दे (के) मूंह (मुंह पर) आई (आ गई) ।"
                ],
                "english_gloss": [
                    "ज़र्रा (a tiny atom) इश्क (of love) तुसाडा (Thine) दिसदा (appears), परबत (mountain) कोलों (than) भारा (heavier),",
                    "इक (one) घड़ी (moment) दे (of) वेखन (beholding) कारन (for the sake of), चुक्क (lifted/endured) लिआ (took) जग्ग (the world’s wrath) सारा (entire),",
                    "कीती (striven) मेहनत (toil/effort) मिलदी (yields fruit) नाहीं (not), हुन (now) की (what) करे (can do) लुकाई (helpless humanity) ।",
                    "जिन्द (my soul) कुड़िकी (trap) दे (of) मूंह (mouth) आई (has come) ।"
                ],
                "poetic_hindi": [
                    "एक कण तेरे नेह का, पर्वत से भी भारी जानूँ,",
                    "इक पल के दर्शन को सारा जग का ताना-बाना मानूँ ।",
                    "साधना सारी व्यर्थ हुई, अब क्या करे लुगाई ?"
                ],
                "poetic_english": [
                    "A single speck of Thy sweet love outweighs the mountain's mighty crest;",
                    "For one brief glance of Thee I bore the scorn and fury of the rest.",
                    "No toil or merit brings Thee near—what can helpless mortals do?",
                    "Caught in the snare my frail soul lies!"
                ]
            },
            {
                "original": [
                    "वा-वेला की करना, जिन्द जु साड़े सु साड़े,  ",
                    "सुक्खां दा इक पूला नाहीं, दुक्खां दे खलवाड़े,  ",
                    "होनी सी जु उस दिन होई, हुन की करीए भाई ।  ",
                    "जिन्द कुड़िकी दे मूंह आई ।"
                ],
                "hindi_gloss": [
                    "वा-वेला (क्रंदन/विलाप) की (क्या) करना (करना), जिन्द (प्राणों को) जु (जो) साड़े (जलाता है) सु (वह) साड़े (जलाए),",
                    "सुक्खां (सुखों) दा (का) इक (एक) पूला (पूला/मुट्ठी-भर तृण) नाहीं (नहीं), दुक्खां (दुखों) दे (के) खलवाड़े (खलिहान/विशाल ढेर),",
                    "होनी (जो होनी) सी (थी) जु (जो) उस (उस) दिन (दिन) होई (हो चुकी), हुन (अब) की (क्या) करीए (करें) भाई (हे भाई) ।",
                    "जिन्द (जान) कुड़िकी (फंदे) दे (के) मूंह (मुंह पर) आई (आ फंसी) ।"
                ],
                "english_gloss": [
                    "वा-वेला (wailing/lament) की (why) करना (make), जिन्द (the soul) जु (which) साड़े (burns) सु (let it) साड़े (burn),",
                    "सुक्खां (of joys) दा (of) इक (a single) पूला (sheaf/handful) नाहीं (none), दुक्खां (of sorrows) दे (of) खलवाड़े (heaped threshing floors),",
                    "होनी (destiny) सी (was) जु (which) उस (that) दिन (day) होई (transpired), हुन (now) की (what) करीए (can we do) भाई (O brothers) ।",
                    "जिन्द (the soul) कुड़िकी (snare) दे (of) मूंह (jaws) आई (has entered) ।"
                ],
                "poetic_hindi": [
                    "व्यर्थ विलाप करूँ क्यों, जो जले सो जले अंगार,",
                    "सुखों की एक पूली नहीं, दुखों का लगा खलिहान अपार ।",
                    "होनी थी जो हो गई, अब क्या करें भ्रात ?"
                ],
                "poetic_english": [
                    "Why weep or raise a bitter cry? If soul must burn, then let it burn;",
                    "No sheaf of joy is left in hand, but barns of grief at every turn.",
                    "What was decreed that primal day hath come to pass for evermore:",
                    "Caught in the snare my frail soul lies!"
                ]
            },
            {
                "original": [
                    "सलाह ना मन्नदा वात (ना) पुच्छदा, आख वेखां की करदा,  ",
                    "कल्ल्ह मैं कमली ते (अज्ज) उह कमला, हुन क्यों मैथों डरदा,  ",
                    "उहले बह के रमज़ चलाई, दिल नूं चोट लगाई ।  ",
                    "जिन्द कुड़िकी दे मूंह आई ।"
                ],
                "hindi_gloss": [
                    "सलाह (परामर्श) ना (नहीं) मन्नदा (मानता) वात (हाल-चाल) ना (नहीं) पुच्छदा (पूछता), आख (कहकर) वेखां (देखता हूँ) की (क्या) करदा (करता है),",
                    "कल्ल्ह (कल तक) मैं (मैं) कमली (पगली/दीवानी) ते (तथा) अज्ज (आज) उह (वह स्वयं) कमला (दीवाना), हुन (अब) क्यों (क्यों) मैथों (मुझसे) डरदा (डरता/भागता है),",
                    "उहले (ओट/पर्दे में) बह (बैठ) के (कर) रमज़ (गुप्त संकेत) चलाई (चलाया), दिल (हृदय) नूं (को) चोट (तीव्र चोट) लगाई (लगा दी) ।",
                    "जिन्द (जीवात्मा) कुड़िकी (फंदे) दे (के) मूंह (मुंह पर) आई ।"
                ],
                "english_gloss": [
                    "सलाह (counsel) ना (not) मन्नदा (accepts) वात (news/state) ना (not) पुच्छदा (inquires), आख (saying) वेखां (I watch) की (what) करदा (He does),",
                    "कल्ल्ह (yesterday) मैं (I was) कमली (mad/frenzied) ते (and) अज्ज (today) उह (He) कमला (crazed with love), हुन (now) क्यों (why) मैथों (from me) डरदा (fears/flees),",
                    "उहले (in concealment) बह (sitting) के (having) रमज़ (secret arrow/sign) चलाई (shot), दिल (to my heart) नूं (to) चोट (wound) लगाई (inflicted) ।",
                    "जिन्द (the soul) कुड़िकी (snare) दे (of) मूंह (jaws) आई (has fallen) ।"
                ],
                "poetic_hindi": [
                    "न बात सुने, न सलाह गिने, देखूँ वह क्या करतब ढाए,",
                    "कल मैं पगली, आज वह बावरा, फिर क्यों मुझसे कतराए ?",
                    "ओट में बैठ के बाण चलाया, हृदय पर गहरी चोट लगाई !"
                ],
                "poetic_english": [
                    "He heeds no counsel, asks no news, I watch the strange game that He plays;",
                    "Mad was I once, now mad is He, yet why from me He turns his gaze?",
                    "Sitting behind the veil He shot His arrow deep into my breast:",
                    "Caught in the snare my frail soul lies!"
                ]
            },
            {
                "original": [
                    "सीने बान धन्दाला गल विच, इस हालत विच जालां,  ",
                    "चा चा सिर भोएं ते मारां, रो रो यार संभालां,  ",
                    "अग्गे वी सईआं ने नेहुं लगाइआ, के मैं ही प्रीत लगाई ।  ",
                    "जिन्द कुड़िकी दे मूंह आई ।"
                ],
                "hindi_gloss": [
                    "सीने (सीने में) बान (बाण/तीर) धन्दाला (दांतोंदार/आरीदार कांटा) गल (गले) विच (में), इस (इस) हालत (दशा) विच (में) जालां (जलती/तड़पती हूँ),",
                    "चा (उठा-) चा (उठाकर) सिर (सिर) भोएं (भूमि) ते (पर) मारां (पटकती हूँ), रो (रो-) रो (रोकर) यार (यार/प्रियतम को) संभालां (याद करती हूँ),",
                    "अग्गे (पहले) वी (भी तो) सईआं (सखियों) ने (ने) नेहुं (प्रेम) लगाइआ (लगाया था), के (क्या) मैं (मैंने) ही (ही केवल) प्रीत (प्रीत) लगाई (लगाई थी) ।",
                    "जिन्द (प्राण) कुड़िकी (फंदे) दे (के) मूंह (मुंह पर) आई ।"
                ],
                "english_gloss": [
                    "सीने (in chest) बान (arrow) धन्दाला (barbed/serrated) गल (throat) विच (in), इस (this) हालत (state) विच (in) जालां (I suffer/burn),",
                    "चा (lifting) चा (lifting) सिर (head) भोएं (on the ground) ते (upon) मारां (I strike), रो (weeping) रो (weeping) यार (Beloved) संभालां (I remember),",
                    "अग्गे (before) वी (also) सईआं (other maidens) ने (have) नेहुं (love) लगाइआ (pledged), के (or) मैं (did I) ही (alone) प्रीत (love) लगाई (attach) ।",
                    "जिन्द (soul) कुड़िकी (snare) दे (of) मूंह (mouth) आई ।"
                ],
                "poetic_hindi": [
                    "छाती में तीर, गले फंदा, इस विरह-दशा में जलती हूँ,",
                    "धरती पर सिर पटक-पटक कर, रो-रो कर सुध करती हूँ ।",
                    "क्या औरों ने प्रीत न की थी, जो मुझी पर यह विपदा आई ?"
                ],
                "poetic_english": [
                    "A barbed dart lodged within my chest, a choking noose around my throat;",
                    "I beat my head upon the dust, while tears of longing blind and float.",
                    "Did other maidens never love, that I alone this torment bear?",
                    "Caught in the snare my frail soul lies!"
                ]
            },
            {
                "original": [
                    "जग्ग विच रोशन नां तुसाडा, आशक तों क्यों नस्सदे हो,  ",
                    "वस्सो रसो विच बुक्कल दे, आपना भेत ना दसदे हो,  ",
                    "विचोकड़े विचकारों फड़के, मैं कर उलटी लटकाई ।  ",
                    "जिन्द कुड़िकी दे मूंह आई ।"
                ],
                "hindi_gloss": [
                    "जग्ग (संसार) विच (में) रोशन (प्रसिद्ध/उज्ज्वल) नां (नाम) तुसाडा (आपका), आशक (आशिक/प्रेमी) तों (से) क्यों (क्यों) नस्सदे (भागते) हो (हो),",
                    "वस्सो (बसते हो) रसो (आनंद लेते हो) विच (में) बुक्कल (आँचल/हृदय) दे (के), आपना (अपना) भेत (भेद/रहस्य) ना (नहीं) दसदे (बताते) हो (हो),",
                    "विचोकड़े (मध्यस्थ को/साधना की धारा में) विचकारों (बीच में से) फड़के (पकड़कर), मैं (मुझे) कर (करके) उलटी (उल्टा) लटकाई (लटका दिया) ।",
                    "जिन्द (जान) कुड़िकी (फंदे) दे (के) मूंह (मुंह पर) आई ।"
                ],
                "english_gloss": [
                    "जग्ग (world) विच (in) रोशन (renowned) नां (name) तुसाडा (Thine), आशक (from lover) तों (from) क्यों (why) नस्सदे (flee) हो (Thou),",
                    "वस्सो (dwell) रसो (revel) विच (within) बुक्कल (cloak/bosom) दे (of), आपना (Thy) भेत (secret) ना (not) दसदे (reveal) हो (Thou),",
                    "विचोकड़े (by the middle/waist) विचकारों (from halfway) फड़के (gripping), मैं (me) कर (making) उलटी (upside down) लटकाई (suspended) ।",
                    "जिन्द (my soul) कुड़िकी (snare) दे (of) मूंह (mouth) आई ।"
                ],
                "poetic_hindi": [
                    "जग में रोशन नाम तुम्हारा, आशिक से क्यों दूर भगाओ,",
                    "आँचल में ही वास तुम्हारा, फिर क्यों अपना भेद छुपाओ ?",
                    "अधर-बीच से पकड़ मुझे, क्यों उल्टी फाँसी लटकाई ?"
                ],
                "poetic_english": [
                    "Thy name is famed through all the worlds, why flee from lovers in disguise?",
                    "Thou dwellest inside my very cloak, yet hide Thy secret from my eyes!",
                    "Gripping me mid-way in the air, upside down Thou hast hung my plight:",
                    "Caught in the snare my frail soul lies!"
                ]
            },
            {
                "original": [
                    "अन्दर वालिआ बाहर आवीं, बाहों पकड़ खलोवां,  ",
                    "ज़ाहरा मैथों लुक्कन छिपन, बातन कोले होवां,  ",
                    "ऐसे बातन फटी जुलैखां, मैं बातन बिरलाई ।  ",
                    "जिन्द कुड़िकी दे मूंह आई ।"
                ],
                "hindi_gloss": [
                    "अन्दर (भीतर) वालिआ (बसने वाले प्रियतम) बाहर (बाहर) आवीं (आओ), बाहों (बाँह से) पकड़ (पकड़कर) खलोवां (खड़ी हो जाऊँ),",
                    "ज़ाहरा (बाह्य रूप से) मैथों (मुझसे) लुक्कन (छिपते) छिपन (छिपाव करते हो), बातन (आंतरिक रूप से) कोले (समीप/हृदय के पास) होवां (होते हो),",
                    "ऐसे (इसी) बातन (आंतरिक विरह से) फटी (विदीर्ण हो गई) जुलैखां (ज़ुलैखा—यूसुफ के प्रेम में), मैं (मैं भी) बातन (आंतरिक रूप से) बिरलाई (व्याकुल विलाप कर रही हूँ) ।",
                    "जिन्द (मेरी आत्मा) कुड़िकी (फंदे) दे (के) मूंह (मुंह पर) आई ।"
                ],
                "english_gloss": [
                    "अन्दर (inside) वालिआ (O dweller) बाहर (outside) आवीं (come out), बाहों (by arm) पकड़ (clasping) खलोवां (let me stand),",
                    "ज़ाहरा (outwardly) मैथों (from me) लुक्कन (hiding) छिपन (concealing), बातन (inwardly/esoterically) कोले (very near) होवां (art Thou),",
                    "ऐसे (by this) बातन (inner longing) फटी (torn/consumed) जुलैखां (Zulaikha), मैं (I too) बातन (inwardly) बिरलाई (wail in separation) ।",
                    "जिन्द (soul) कुड़िकी (trap) दे (of) मूंह (jaws) आई ।"
                ],
                "poetic_hindi": [
                    "भीतर वाले! बाहर आओ, बाहें गहि सम्मुख आ जाओ,",
                    "बाहर-बाहर छिपते फिरते, भीतर अंग-संग मुस्काओ ।",
                    "जैसे विरह में फटी ज़ुलैखा, वैसे मैं भी बिलखाई !"
                ],
                "poetic_english": [
                    "O Inward Dweller, step outside, that I may grasp Thy loving hand!",
                    "Outwardly Thou art veiled from sight, while inwardly beside me stand.",
                    "Thus was Zulaikha torn within, and thus my weeping soul cries free:",
                    "Caught in the snare my frail soul lies!"
                ]
            },
            {
                "original": [
                    "आखणियां सी आख सुणाईआं, मचला सुणदा नाहीं,  ",
                    "हत्थ मरोड़ां फाटां तलियां, रोवां ढाहीं ढाहीं,  ",
                    "लैने थीं मुड़ देना आया, इह तेरी भलिआई ।  ",
                    "जिन्द कुड़िकी दे मूंह आई ।"
                ],
                "hindi_gloss": [
                    "आखणियां (कहने योग्य बातें) सी (थीं जो) आख (कहकर) सुणाईआं (सुना दीं), मचला (हठी/लापरवाह प्रियतम) सुणदा (सुनता) नाहीं (नहीं),",
                    "हत्थ (हाथ) मरोड़ां (मरोड़ती हूँ) फाटां (पीटती हूँ) तलियां (हथेलियाँ), रोवां (रोती हूँ) ढाहीं (चीत्कार करके) ढाहीं (चीख-चीख कर),",
                    "लैने (प्राण लेने) थीं (से) मुड़ (फिर) देना (प्राण देना/जीवित रखना) आया (आया), इह (यह) तेरी (तेरी कैसी) भलिआई (भलाई/दया है) ।",
                    "जिन्द (जीवात्मा) कुड़िकी (फंदे) दे (के) मूंह (मुंह पर) आई ।"
                ],
                "english_gloss": [
                    "आखणियां (words to speak) सी (which were) आख (speaking) सुणाईआं (I voiced), मचला (heedless/feigning deaf) सुणदा (listens) नाहीं (not),",
                    "हत्थ (hands) मरोड़ां (I wring) फाटां (I beat) तलियां (palms), रोवां (I weep) ढाहीं (crying aloud) ढाहीं (bitter wails),",
                    "लैने (taking life) थीं (from) मुड़ (again) देना (restoring life/prolonging torment) आया (came), इह (this is) तेरी (Thy) भलिआई (goodness/mercy) ।",
                    "जिन्द (the soul) कुड़िकी (snare) दे (of) मूंह (mouth) आई ।"
                ],
                "poetic_hindi": [
                    "कहनी थीं जो बातें कह दीं, हठी छलिया सुनता नाहीं,",
                    "हाथ मरोड़ूँ, तलवे पीटूँ, रोती चीख-चीख कर माहीं ।",
                    "प्राण न लेवे, न जीने देवे, क्या यह तेरी भलाई ?"
                ],
                "poetic_english": [
                    "All that was in my heart I told, yet feigning deaf He turns away;",
                    "I wring my hands and beat my palms, weeping in anguish night and day.",
                    "Thou wilt not take my breath nor heal—is this Thy mercy and Thy care?",
                    "Caught in the snare my frail soul lies!"
                ]
            },
            {
                "original": [
                    "इक इक लहर अजेही आवे, नहीं दस्सणियां सो दस्सां,  ",
                    "सच्च आखां तां सूली फाहा, झूठ कहां तां वस्सां,  ",
                    "ऐसी नाज़क बात क्यों आखां, कहन्द्यां होवे पराई ।  ",
                    "जिन्द कुड़िकी दे मूंह आई ।"
                ],
                "hindi_gloss": [
                    "इक (एक) इक (एक) लहर (भाव-तरंग) अजेही (ऐसी प्रबल) आवे (आती है), नहीं (जो नहीं) दस्सणियां (बताने योग्य) सो (वही) दस्सां (कहने को विवश हूँ),",
                    "सच्च (सत्य/अन-अल-हक) आखां (कहूँ) तां (तो) सूली (सूली) फाहा (फांसी का फंदा), झूठ (झूठ) कहां (बोलूँ) तां (तो) वस्सां (संसार में बस सकती हूँ),",
                    "ऐसी (ऐसी) नाज़क (नाजुक/गूढ़) बात (रहस्य) क्यों (क्यों) आखां (कहूँ), कहन्द्यां (कहते ही जो) होवे (हो जाती है) पराई (अपवित्र/अनधिकार चर्चा) ।",
                    "जिन्द (आत्मा) कुड़िकी (फंदे) दे (के) मूंह (मुंह पर) आई ।"
                ],
                "english_gloss": [
                    "इक (one) इक (after one) लहर (wave of ecstasy) अजेही (such) आवे (surges), नहीं (not) दस्सणियां (to be told) सो (that) दस्सां (I am compelled to speak),",
                    "सच्च (truth) आखां (if I speak) तां (then) सूली (gallows) फाहा (noose), झूठ (lie) कहां (if I utter) तां (then) वस्सां (I abide safely),",
                    "ऐसी (such) नाज़क (delicate/secret) बात (mystery) क्यों (why) आखां (should I utter), कहन्द्यां (speaking which) होवे (becomes) पराई (alienated/violated) ।",
                    "जिन्द (soul) कुड़िकी (snare) दे (of) मूंह (mouth) आई ।"
                ],
                "poetic_hindi": [
                    "एक-एक लहर ऐसी उठे, जो अकथनीय सो कह जाऊँ,",
                    "सच बोलूँ तो सूली-फाँसी, झूठ कहूँ तो जग पाऊँ ।",
                    "ऐसी नाज़ुक बात कहूँ क्यों, कहते ही जग होय पराई ?"
                ],
                "poetic_english": [
                    "Such waves of ecstasy arise, I utter what must not be said;",
                    "Truth brings the gallows and the noose, by lies alone is safety fed.",
                    "Why speak this delicate mystic word, where speech itself profanes the air?",
                    "Caught in the snare my frail soul lies!"
                ]
            },
            {
                "original": [
                    "वही वसीला पाकां दा, तुसीं आपे साडे होवो,  ",
                    "जागद्यां संग साडे जागो, सवां तां नाले सौंवो,  ",
                    "जिसने तैं संग प्रीत लगाई, केहड़े सुक्ख सुवाई ।  ",
                    "जिन्द कुड़िकी दे मूंह आई ।"
                ],
                "hindi_gloss": [
                    "वही (वही परम परमात्मा) वसीला (आधार/आश्रय) पाकां (पवित्र संतों) दा (का), तुसीं (आप) आपे (स्वयं ही) साडे (हमारे) होवो (हो जाओ),",
                    "जागद्यां (जब मैं जागूँ) संग (साथ) साडे (मेरे) जागो (जागो), सवां (जब मैं सोऊँ) तां (तो) नाले (साथ ही) सौंवो (सोओ),",
                    "जिसने (जिसने भी) तैं (तेरे) संग (साथ) प्रीत (प्रेम) लगाई (लगाया), केहड़े (किस) सुक्ख (सुख में) सुवाई (वह सुखपूर्वक सो सका) ।",
                    "जिन्द (जीवात्मा) कुड़िकी (फंदे) दे (के) मूंह (मुंह पर) आई ।"
                ],
                "english_gloss": [
                    "वही (He alone) वसीला (haven/mediator) पाकां (of the pure saints) दा (of), तुसीं (Thou) आपे (Thyself) साडे (mine) होवो (become),",
                    "जागद्यां (when I wake) संग (with) साडे (me) जागो (wake Thou), सवां (when I sleep) तां (then) नाले (beside me) सौंवो (sleep Thou),",
                    "जिसने (whoever) तैं (Thee) संग (with) प्रीत (love) लगाई (bound), केहड़े (what) सुक्ख (peace/sleep) सुवाई (could ever find) ।",
                    "जिन्द (soul) कुड़िकी (snare) दे (of) मूंह (jaws) आई ।"
                ],
                "poetic_hindi": [
                    "संतों का तू ही सहारा, तू ही अब बस मेरा हो जा,",
                    "जागूँ तो संग मेरे जागे, सोऊँ तो संग मेरे सो जा ।",
                    "जिसने तुझसे प्रीत लगाई, उसने कब सुख-नींद गंवाई ?"
                ],
                "poetic_english": [
                    "Sole haven of the holy saints, make Thyself mine and wholly stay;",
                    "Awake with me when I awake, sleep by my side till break of day.",
                    "Whoever pledged their love to Thee—what peaceful slumber could they share?",
                    "Caught in the snare my frail soul lies!"
                ]
            },
            {
                "original": [
                    "ऐसियां लीकां लाईआं मैनूं, होर कई घर गाले,  ",
                    "उपरवारों पावें झाती, वतें फिरे दुआले,  ",
                    "लुक्कन छिपन ते छल जावन, इह तेरी वड्याई ।  ",
                    "जिन्द कुड़िकी दे मूंह आई ।"
                ],
                "hindi_gloss": [
                    "ऐसियां (ऐसी अपमानजनक) लीकां (लांछन/कालिमा की लकीरें) लाईआं (लगा दीं) मैनूं (मुझ पर), होर (और भी) कई (अनेक) घर (घर-परिवार) गाले (नष्ट/बर्बाद कर दिए),",
                    "उपरवारों (छत के ऊपर से/चोरी-छिपे) पावें (डालता है) झाती (झांकी/नज़र), वतें (फिरता रहता है) फिरे (घूमता) दुआले (चारों ओर),",
                    "लुक्कन (छिपना) छिपन (छिपे रहना) ते (और) छल (छल) जावन (करके चले जाना), इह (यह) तेरी (तेरी कैसी) वड्याई (महिमा/बड़प्पन है) ।",
                    "जिन्द (आत्मा) कुड़िकी (फंदे) दे (के) मूंह (मुंह पर) आई ।"
                ],
                "english_gloss": [
                    "ऐसियां (such) लीकां (stigma/lines of shame) लाईआं (marked upon) मैनूं (me), होर (and other) कई (many) घर (homes) गाले (ruined/destroyed),",
                    "उपरवारों (from rooftops/above) पावें (cast) झाती (a fleeting glance), वतें (ever) फिरे (wanderest) दुआले (around outside),",
                    "लुक्कन (to hide) छिपन (conceal) ते (and) छल (to deceive) जावन (depart), इह (is this) तेरी (Thy) वड्याई (glory/greatness) ।",
                    "जिन्द (soul) कुड़िकी (snare) दे (of) मूंह (mouth) आई ।"
                ],
                "poetic_hindi": [
                    "लांछन की रेखाएं खींचीं, कितने घर बर्बाद कराए,",
                    "ऊपर से झाँकी दे जाता, चारों ओर फेरे मुस्काए ।",
                    "छिपना, छलना, आँख चुराना—क्या यह शोभा तुमको पाई ?"
                ],
                "poetic_english": [
                    "Thou marked me with the lines of shame, and ruined many a hearth and home;",
                    "Peeping from rooftops now and then, around my courtyard Thou dost roam.",
                    "To hide, deceive, and slip away—is this the glory Thou dost wear?",
                    "Caught in the snare my frail soul lies!"
                ]
            },
            {
                "original": [
                    "तेरा मेरा न्याउं नबेड़े, रूमों काज़ी आवे,  ",
                    "खोल्ह किताबां करे तसल्ली, दोहां इक बतावे,  ",
                    "भरम्या काज़ी मेरे उत्ते, मैं काज़ी भरमाई ।  ",
                    "जिन्द कुड़िकी दे मूंह आई ।"
                ],
                "hindi_gloss": [
                    "तेरा (तेरा) मेरा (मेरा) न्याउं (न्याय/फैसला) नबेड़े (निपटाने के लिए), रूमों (रूम/इस्तांबुल के महान धर्मकेंद्र से) काज़ी (काज़ी/इस्लामी न्यायाधीश) आवे (आए),",
                    "खोल्ह (खोलकर) किताबां (ग्रंथों/शरीयती पोथियों को) करे (करे) तसल्ली (समाधान), दोहां (दोनों—तुझे और मुझे) इक (एक ही ब्रह्म/अद्वैत) बतावे (बताए),",
                    "भरम्या (भ्रमित/हैरान हुआ) काज़ी (काज़ी) मेरे (मेरे) उत्ते (ऊपर), मैं (मैंने) काज़ी (काज़ी को ही) भरमाई (चकित/निरुत्तर कर दिया) ।",
                    "जिन्द (मेरी जान) कुड़िकी (फंदे) दे (के) मूंह (मुंह पर) आई ।"
                ],
                "english_gloss": [
                    "तेरा (between Thee) मेरा (and me) न्याउं (justice/arbitration) नबेड़े (to settle), रूमों (from Rome/Rûm) काज़ी (the supreme Qazi) आवे (let come),",
                    "खोल्ह (opening) किताबां (the books of law) करे (grant) तसल्ली (conviction/peace), दोहां (the two of us) इक (as One) बतावे (proclaim),",
                    "भरम्या (confounded was) काज़ी (the Qazi) मेरे (upon me) उत्ते (over), मैं (I) काज़ी (the judge himself) भरमाई (perplexed/bewildered) ।",
                    "जिन्द (the soul) कुड़िकी (trap) दे (of) मूंह (jaws) आई ।"
                ],
                "poetic_hindi": [
                    "तेरा-मेरा न्याय निबटाने, रूमी काज़ी चलकर आए,",
                    "पोथी खोले, साक्ष्य बतावे, दोनों को वह एक बताए ।",
                    "काज़ी मुझ पर भ्रमित हुआ, मैंने काज़ी की मति भरमाई !"
                ],
                "poetic_english": [
                    "Let Rûm’s high judge descend in state to arbitrate between us two;",
                    "Opening his ancient texts to prove that Lover and Beloved are true,",
                    "Yet bewildered was the judge at me, when I his dogmas did ensnare:",
                    "Caught in the snare my frail soul lies!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शौह तूं केहा जेहा हुन, तूं केहा मैं कही,  ",
                    "तैनूं जो मैं ढूंडन लग्गी, मैं भी आप ना रही,  ",
                    "पाइआ ज़ाहर बातन तैनूं, बातन अन्दर रुशनाई ।  ",
                    "जिन्द कुड़िकी दे मूंह आई ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ला कहता है) शौह (हे शाह/प्रभु) तूं (तू) केहा (कैसा) जेहा (सा) हुन (अब), तूं (तू) केहा (कैसा) मैं (मैं) कही (कैसी—द्वैत का भेद मिट गया),",
                    "तैनूं (तुझे) जो (जब) मैं (मैं) ढूंडन (खोजने) लग्गी (लगी), मैं (मैं) भी (भी) आप (स्वयं/मेरा पृथक अस्तित्व) ना (नहीं) रही (रहा),",
                    "पाइआ (पा लिया) ज़ाहर (बाह्य रूप में) बातन (आंतरिक रूप में) तैनूं (तुझे), बातन (अंतरतम के) अन्दर (भीतर) रुशनाई (परम प्रकाश/दिव्य ज्योति जगमगा उठी) ।",
                    "जिन्द (मेरी आत्मा) कुड़िकी (प्रेम के फंदे) दे (के) मूंह (मुंह पर) आई ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh says) शौह (O Lord/Master) तूं (Thou) केहा (what kind) जेहा (like) हुन (now), तूं (what art Thou) केहा (what am I) मैं (I) कही (who am I—distinction dissolved),",
                    "तैनूं (Thee) जो (when) मैं (I) ढूंडन (to seek) लग्गी (began), मैं (I) भी (too) आप (my own separate self) ना (no longer) रही (remained),",
                    "पाइआ (found) ज़ाहर (outwardly) बातन (inwardly) तैनूं (Thee), बातन (the inward realm) अन्दर (within) रुशनाई (radiance/divine illumination shone) ।",
                    "जिन्द (the soul) कुड़िकी (snare of divine love) दे (of) मूंह (mouth) आई ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा शौह! तू कैसा अब, तू कैसा मैं कौन रही,",
                    "ढूँढने निकली तुझको जब मैं, अपनी ही सत्ता न रही ।",
                    "ज़ाहिर-बातिन तुझको पाया, भीतर दिव्य उजाला छाई !"
                ],
                "poetic_english": [
                    "O Bulleh Shah, what art Thou now, and what am I in this domain?",
                    "When I set forth to search for Thee, no trace of self did e'er remain;",
                    "Outward and inward Thou art found, the inner core shines bright and fair:",
                    "Caught in the snare my frail soul lies!"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी सूफी रहस्यवाद के विरह (फ़िराक) से मिलन (विसाल) और अंततः 'फ़ना' (अहं के लय) तक की संपूर्ण आध्यात्मिक यात्रा का महाकाव्य है। 'लहमका लहमी' कुरान/हदीस के इस भाव को इंगित करता है कि परमात्मा मनुष्य की गर्दन की नस (हब्लिल वरीद) से भी निकट है। बंध 12 और 13 में बुल्ले शाह काज़ी और रूढ़िवादी शरीअत को परास्त करते हैं: जब प्रेमी अपने आप को खोकर प्रियतम में लीन हो जाता है, तो द्वैत समाप्त हो जाता है—'तूं केहा मैं कही'।"
    }
]

new_lexicon_terms = {
    "सबक": {"hindi": "पाठ, शिक्षा", "english": "lesson, spiritual teaching"},
    "ठाकर": {"hindi": "ठाकुर, प्रभु, परमात्मा", "english": "Lord, Beloved Master"},
    "नाद": {"hindi": "अनहद नाद, दिव्य आंतरिक स्वर", "english": "mystic cosmic sound/resonance"},
    "रमज़": {"hindi": "गूढ़ भेद, आध्यात्मिक रहस्य", "english": "subtle esoteric secret"},
    "बुक्कल": {"hindi": "आँचल, चादर, हृदय का आलिंगन", "english": "cloak, inner embrace, bosom"},
    "मुसल्ला": {"hindi": "प्रार्थना-चटाई, जा-नमाज़", "english": "prayer rug, formal ritual mat"},
    "तसबी": {"hindi": "तस्बीह, माला", "english": "rosary, prayer beads"},
    "कासा": {"hindi": "भिक्षापात्र", "english": "begging bowl"},
    "सोटा": {"hindi": "लाठी, दण्ड", "english": "ascetic staff/stick"},
    "मुरदार": {"hindi": "मुर्दा मांस; रूपक में: सांसारिक रूप से तिरस्कृत सत्य", "english": "carrion; metaphorically: despised divine truth"},
    "तौहीद": {"hindi": "एकेश्वरवाद, अद्वैत, एकात्म भाव", "english": "divine unity, non-duality, oneness"},
    "मसीती": {"hindi": "मस्जिद में", "english": "in the mosque"},
    "इश्क हकीकी": {"hindi": "परम ईश्वरीय प्रेम, सत्य प्रेम", "english": "Divine Love, ultimate spiritual love"},
    "इश्क मजाज़ी": {"hindi": "सांसारिक या रूपक प्रेम", "english": "metaphorical/earthly love"},
    "मंतिक": {"hindi": "तर्कशास्त्र", "english": "logic (scholastic formal discipline)"},
    "मअनी": {"hindi": "शब्दार्थ विद्या, अलंकार शास्त्र", "english": "semantics and rhetoric"},
    "कन्नज़": {"hindi": "कन्ज-उद्-दकाइक (इस्लामी न्यायशास्त्र की प्रसिद्ध पुस्तक)", "english": "Kanz al-Daqaiq (classical manual of Hanafi jurisprudence)"},
    "कदूरी": {"hindi": "मुख्तसर अल-कुदूरी (इस्लामी विधि का ग्रन्थ)", "english": "Mukhtasar al-Quduri (classical legal compendium)"},
    "वगुच्ची": {"hindi": "भटक गई, नष्ट हो गई", "english": "went astray, ruined through overthinking"},
    "सुराही": {"hindi": "शराब का पात्र, प्रेम-घट", "english": "goblet/flagon of ecstatic love"},
    "किरम": {"hindi": "कीड़े, कृमि", "english": "worms, parasites"},
    "ज़ोरावर": {"hindi": "सर्वशक्तिमान, बलशाली परमात्मा", "english": "All-Powerful, Almighty Lord"},
    "मुहाल": {"hindi": "असंभव, अत्यंत कठिन, अगम्य", "english": "impossible, unfathomable, arduous"},
    "आरा": {"hindi": "आरी, चीरने वाला यंत्र", "english": "saw for cutting timber"},
    "जवाल": {"hindi": "विनाश, पतन, घोर संकट", "english": "decline, ruin, severe ordeal"},
    "काती": {"hindi": "कैंची, छुरी", "english": "shears, small sharp blade"},
    "मधुवा": {"hindi": "प्रेम-मदिरा, मधु", "english": "wine of ecstasy"},
    "मुन्दरा": {"hindi": "मुद्रिका, अंगूठी", "english": "signet ring"},
    "बेताल": {"hindi": "ताल-रहित, उन्मत्त", "english": "without fixed meter, wild ecstatic cadence"},
    "कुड़िकी": {"hindi": "शिकारी का फंदा, पिंजरा, जाल", "english": "snare, trap, hunter's cage"},
    "लहमका लहमी": {"hindi": "मांस में मांसवत मिला हुआ, अति-समीप, अंतर्व्यापी", "english": "flesh within flesh, profoundly intimate/immanent"},
    "खुभ्भन": {"hindi": "दलदल, गहरा कीचड़", "english": "quagmire, deep swamp"},
    "खलवाड़े": {"hindi": "खलिहान, अनाजों के विशाल ढेर", "english": "threshing floors, vast heaps"},
    "धन्दाला": {"hindi": "दांतों वाला कांटा, आरीदार बाण", "english": "toothed/barbed arrow or hook"},
    "मचला": {"hindi": "हठी, अनजान बनने वाला, नटखट", "english": "obstinate, pretending ignorance/heedless"},
    "फाटां": {"hindi": "पीटती हूँ", "english": "I beat/strike repeatedly"},
    "लीकां": {"hindi": "रेखाएं, लांछन की लकीरें", "english": "lines, marks of social stigma"},
    "न्याउं": {"hindi": "न्याय, फैसला", "english": "justice, arbitration"},
    "नबेड़े": {"hindi": "निपटारा करे, समाप्त करे", "english": "settle, resolve a dispute"},
    "काज़ी": {"hindi": "न्यायाधीश, शरीअती मुफ्ती", "english": "Qazi, Islamic judge"}
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
        "completed_count": 55,
        "total": 160,
        "next_kafi_id": 56,
        "last_updated": "2026-10-17T16:50:00+05:30",
        "last_batch": "51-55",
        "status": "in_progress"
    }
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print(f"Checkpoint updated: 55/160 completed. Next ID: 56")

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
