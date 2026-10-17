# -*- coding: utf-8 -*-
"""
Process Kafian 106 to 110 for Bulleh Shah Trilingual Edition.
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
        "id": 106,
        "title": "मित्तर प्यारे कारन नी मैं लोक उल्हामें लैनी हां",
        "title_english": "For the Sake of My Beloved Friend, I Bear the World's Reproach",
        "historical_context": "यह 4 बंधों की एक अत्यंत भावुक और मार्मिक विरह-काफी है। इसमें हीर (आत्मा) अपने प्यारे मित्र (रांझा/परमेश्वर/शाह इनायत) की खातिर संसार भर के ताने और उलाहने हंसकर स्वीकार करती है। संसार के नियम और रीतियां प्रेम की अनुभूति के सम्मुख तुच्छ प्रतीत होती हैं। विरह की बीमारी का एकमात्र उपचार केवल प्रियतम का दीदार और उसका सामीप्य है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: मित्तर प्यारे कारन)",
        "raga": "राग काफी / तिलक कामोद",
        "theme": "इश्क के लिए सामाजिक उलाहने सहना, विरह-व्यथा, एकमात्र औषधि दीदार, प्रेमानंद",
        "stanzas": [
            {
                "original": [
                    "लग्गा नेहुं मेरा जिस सेती, सरहाने वेख पलंघ दे जीती,  ",
                    "आलम क्युं समझावे रीती, मैं डिट्ठे बाझ ना रहनी हां ।  ",
                    "मित्तर प्यारे कारन नी मैं लोक उल्हामें लैनी हां ।"
                ],
                "hindi_gloss": [
                    "लग्गा (लगा है) नेहुं (प्रेम/नेह) मेरा (मेरा) जिस (जिस प्रियतम) सेती (के साथ), सरहाने (सेज के सिरहाने) वेख (देखकर उसे) पलंघ (पलंग) दे (के पास) जीती (मेरी आत्मा जीवित हो उठी है),",
                    "आलम (यह सारा संसार) क्युं (क्यों व्यर्थ ही) समझावे (सिखाता है मुझे कुल की) रीती (मर्यादा और रीतियां), मैं (मैं उसके) डिट्ठे (दीदार/दर्शन के) बाझ (बिना) ना (नहीं) रहनी (रह सकती) हां (हूँ) ।",
                    "मित्तर (उस प्यारे मित्र) प्यारे (प्रियतम के) कारन (खातिर) नी (हे सखी) मैं (मैं) लोक (संसार भर के) उल्हामें (उलाहने/ताने) लैनी (हंसकर सहती) हां (हूँ) ।"
                ],
                "english_gloss": [
                    "लग्गा नेहुं मेरा (my love was pledged) जिस सेती (with whom), सरहाने वेख पलंघ दे (beholding Him at the head of my couch) जीती (my soul revived),",
                    "आलम क्युं समझावे रीती (why does the world preach its customs to me), मैं डिट्ठे बाझ ना रहनी हां (I cannot live without beholding Him) ।",
                    "मित्तर प्यारे कारन (for the sake of my beloved Friend) नी मैं (O sisters, I) लोक उल्हामें लैनी हां (bear the world's taunts and reproach) ।"
                ],
                "poetic_hindi": [
                    "जिससे लगी मेरी प्रीत सुहानी, सेज के सिरहाने देख उसे जी उठी दीवानी,",
                    "संसार मुझे क्यों रीत सिखाए, उसके दीदार बिना मन चैन न पाए !",
                    "मित्र प्यारे की खातिर सखी री, मैं जग के उलाहने सहती हूँ !"
                ],
                "poetic_english": [
                    "With Him my heart is bound in love; seeing Him at my pillow revived my breath;",
                    "Why should the world preach customs vain, when parting from Him is worse than death?",
                    "For the sake of my dearest Beloved Friend, I bear the world’s reproach each day!"
                ]
            },
            {
                "original": [
                    "तुसीं समझायो वीरो भोरी, रांझन वेंहदा मैथों चोरी,  ",
                    "जीहदे इश्क कीती मैं डोरी, मैं नाल आराम ना बहनी हां ।  ",
                    "मित्तर प्यारे कारन नी मैं लोक उल्हामें लैनी हां ।"
                ],
                "hindi_gloss": [
                    "तुसीं (तुम सब मिलकर) समझायो (समझाओ) वीरो (हे वीरों/भाइयों) भोरी (ज़रा सा उसे), रांझन (मेरा रांझा) वेंहदा (देखता/निहारता है) मैथों (मुझसे) चोरी (चोरी-छिपे),",
                    "जीहदे (जिसके) इश्क (प्रेम ने) कीती (कर दिया है) मैं (मुझको) डोरी (प्रेम की डोरी में बंधा हुआ/सुधबुध हीन), मैं (मैं) नाल (तनिक भी) आराम (चैन से) ना (नहीं) बहनी (बैठ सकती) हां (हूँ) ।",
                    "मित्तर (मित्र) प्यारे (प्यारे के) कारन (खातिर) नी (हे सखी) मैं (मैं) लोक (संसार के) उल्हामें (उलाहने) लैनी (सहती) हां (हूँ) ।"
                ],
                "english_gloss": [
                    "तुसीं समझायो (counsel Him) वीरो भोरी (O brothers a little), रांझन वेंहदा मैथों चोरी (Ranjha steals glances at me in secret),",
                    "जीहदे इश्क (whose divine love) कीती मैं डोरी (has strung my heart on its thread), मैं नाल आराम ना बहनी हां (I cannot sit in peaceful repose) ।",
                    "मित्तर प्यारे कारन (for the sake of my Beloved Friend) नी मैं लोक उल्हामें लैनी हां (O sisters, I bear the world's reproach) ।"
                ],
                "poetic_hindi": [
                    "भाइयो, समझाओ ज़रा उसको, जो चोरी-चोरी मुझको निहारे,",
                    "जिसके इश्क ने बाँध लिया दिल, बिन उसके पल भर न चैन सँवारे !",
                    "मित्र प्यारे की खातिर सखी री, मैं जग के उलाहने सहती हूँ !"
                ],
                "poetic_english": [
                    "O brothers, counsel Him a little: He steals His glances from behind the wall;",
                    "His passion spun my heart into twine, leaving no peace in my soul at all!",
                    "For the sake of my dearest Beloved Friend, I bear the world’s reproach each day!"
                ]
            },
            {
                "original": [
                    "बिरहों आ वड़िआ विच वेहड़े, ज़ोरो ज़ोर देवे तन घेरे,  ",
                    "दारू दरद ना बाझों तेरे, मैं सज्जणां बाझ मरेनी हां ।  ",
                    "मित्तर प्यारे कारन नी मैं लोक उल्हामें लैनी हां ।"
                ],
                "hindi_gloss": [
                    "बिरहों (दारुण विरह ने) आ (आकर) वड़िआ (प्रवेश कर लिया है) विच (मेरे) वेहड़े (हृदय-आँगन में), ज़ोरो ज़ोर (बलपूर्वक/प्रचंड वेग से) देवे (दे रहा है) तन (मेरे शरीर को) घेरे (घेरा),",
                    "दारू (औषधि/उपचार) दरद (इस प्रेम-दर्द की) ना (नहीं है कोई) बाझों (सिवाय) तेरे (तेरे दीदार के), मैं (मैं तो अपने) सज्जणां (प्रियतम के) बाझ (बिना तिल-तिल) मरेनी (मर रही) हां (हूँ) ।",
                    "मित्तर (मित्र) प्यारे (प्यारे के) कारन (खातिर) नी (हे सखी) मैं (मैं) लोक (संसार के) उल्हामें (उलाहने) लैनी (सहती) हां (हूँ) ।"
                ],
                "english_gloss": [
                    "बिरहों आ वड़िआ (separation has marched inside) विच वेहड़े (the courtyard of my soul), ज़ोरो ज़ोर देवे तन घेरे (encircles my frail body with mighty force),",
                    "दारू दरद (cure for this pain) ना बाझों तेरे (exists none without Thee), मैं सज्जणां बाझ मरेनी हां (I am dying without my Beloved Friend) ।",
                    "मित्तर प्यारे कारन (for the sake of my Beloved Friend) नी मैं लोक उल्हामें लैनी हां (O sisters, I bear the world's reproach) ।"
                ],
                "poetic_hindi": [
                    "आँगन में विरह ने डेरा डाला, तन को घेरा ज़ोरों-ज़ोर,",
                    "तेरे बिना कोई दारू न इसकी, सजन बिना मेरा टूटे छोर !",
                    "मित्र प्यारे की खातिर सखी री, मैं जग के उलाहने सहती हूँ !"
                ],
                "poetic_english": [
                    "Grim separation invaded my yard, surrounding my body with ruthless might;",
                    "There is no balm for this aching grief save Thee, my haven and holy light!",
                    "For the sake of my dearest Beloved Friend, I bear the world’s reproach each day!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हे शाह घर रांझन आवे, मैं तत्ती नूं लै गल लावे,  ",
                    "नाल ख़ुशी दे रैन वेहावे, नाल ख़ुशी दे रहनी हां ।  ",
                    "मित्तर प्यारे कारन नी मैं लोक उल्हामें लैनी हां ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हे शाह (बुल्ले शाह कहते हैं) घर (मेरे घर) रांझन (मेरा प्रियतम रांझा) आवे (पधार जाए), मैं (मुझ) तत्ती (तप्त/विरह-दग्ध विरहिणी) नूं (को) लै (लेकर अपने) गल (गले से) लावे (लगा ले),",
                    "नाल (परम) ख़ुशी (आनंद के) दे (साथ) रैन (जीवन की रात) वेहावे (बीत जाए), नाल (सदा) ख़ुशी (परमानंद के) दे (साथ) रहनी (रहती) हां (हूँ) ।",
                    "मित्तर (मित्र) प्यारे (प्यारे के) कारन (खातिर) नी (हे सखी) मैं (मैं) लोक (संसार के) उल्हामें (उलाहने) लैनी (सहती) हां (हूँ) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हे शाह (Bulleh Shah) घर रांझन आवे (if Ranjha enters my dwelling), मैं तत्ती नूं (unto me, the burnt and suffering one) लै गल लावे (clasps me to His bosom),",
                    "नाल ख़ुशी दे (with radiant bliss) रैन वेहावे (the night of life shall pass), नाल ख़ुशी दे रहनी हां (in divine joy shall I forever abide) ।",
                    "मित्तर प्यारे कारन (for the sake of my Beloved Friend) नी मैं लोक उल्हामें लैनी हां (O sisters, I bear the world's reproach) ।"
                ],
                "poetic_hindi": [
                    "बुल्ला कहे: घर रांझा आए, विरह-जली को गले लगाए,",
                    "आनंद में सारी रैन कटेगी, रोम-रोम में सुख मुस्काए !",
                    "मित्र प्यारे की खातिर सखी री, मैं जग के उलाहने सहती हूँ !"
                ],
                "poetic_english": [
                    "Says Bulleh: If Ranjha comes to my home, and folds my suffering heart in grace;",
                    "The night of life shall dissolve in bliss, enclosed within His fond embrace!",
                    "For the sake of my dearest Beloved Friend, I bear the world’s reproach each day!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी सूफी परंपरा में 'मलामत' (संसार की निंदा और तिरस्कार को प्रेमपूर्वक स्वीकार करने) के सिद्धांत को प्रतिपादित करती है। जब साधक सांसारिक मान-मर्यादा, लोक-लाज और पारिवारिक दबाव की चिंता छोड़ देता है, तो संसार उस पर 'उल्हामें' (उलाहने) की वर्षा करता है। प्रेमी के लिए ये उलाहने फूलों की वर्षा जैसे होते हैं क्योंकि वे उसके अहंकार को नष्ट करते हैं। विरह की व्याधि का कोई भौतिक उपचार ('दारू') नहीं है, इसका एकमात्र उपचार प्रियतम का आलिंगन और साक्षात्कार है।"
    },
    {
        "id": 107,
        "title": "मूंह आई बात ना रहन्दी ए",
        "title_english": "The Truth That Rises to the Lips Cannot Be Kept Within!",
        "historical_context": "यह 13 बंधों की एक अमर, क्रांतिकारी और विश्व-प्रसिद्ध काफी है। बुल्ले शाह इसमें सत्य के प्रकटीकरण की उस अनिवार्य विवशता को व्यक्त करते हैं जिससे मंसूर हल्लाज, शम्स तबरेज़ी और सुकरात जैसे महापुरुष गुजरे थे। वे कहते हैं: 'झूठ आखां ते कुझ बचदा ए, सच्च आख्यां भांबड़ मचदा ए' (यदि मैं झूठ बोलूँ तो संसार में कुछ प्रतिष्ठा बचती है, पर यदि सच बोल दूँ तो मजहबियों का भांभा/आग भड़क उठती है)। मन दोनों के बीच संशय में पड़ता है, परंतु अंतरात्मा की पुकार चुप नहीं रह सकती। इस काफी में कलंदर का आंतरिक सुख-मंदिर, मूसा और कोहे-तूर, मंसूर की फांसी, बारूद में चिंगारी, और 'हर-हर विच सूरत रब्ब दी' का अद्वैत दर्शन उद्घाटित हुआ है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: मूंह आई बात ना रहन्दी ए)",
        "raga": "राग काफी / भैरवी / दरबारी",
        "theme": "सत्य का निर्भीक प्रकटीकरण, मंसूर की शहादत, कोहे-तूर, अंतःकरण का सुख-मंदिर, वहदत-उल-वुजूद (अद्वैत)",
        "stanzas": [
            {
                "original": [
                    "झूठ आखां ते कुझ बचदा ए सच्च आख्यां भांबड़ मचदा ए,  ",
                    "जी दोहां गल्लां तों जचदा ए जच जच के जेहवा कहन्दी ए ।  ",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "hindi_gloss": [
                    "झूठ (यदि मैं असत्य) आखां (कहूँ) ते (तो दुनियादारी में) कुझ (कुछ मान-सम्मान) बचदा (बचता) ए (है), सच्च (परंतु यदि नग्न सत्य) आख्यां (कहा जाए तो चारों ओर) भांबड़ (कट्टरपंथ की प्रलयंकारी आग) मचदा (भड़क उठती) ए (है),",
                    "जी (मेरा हृदय) दोहां (इन दोनों ही) गल्लां (बातों के परिणामों) तों (से) जचदा (सहमता/सोच-विचार में पड़ता) ए (है), जच (खूब परख-) जच (परख) के (करके भी अंततः यह) जेहवा (जिह्वा/वाणी) कहन्दी (सच कह ही देती) ए (है) ।",
                    "मूंह (मुख तक) आई (आ पहुँची) बात (सत्य की बात भीतर) ना (नहीं) रहन्दी (दबी रह सकती) ए (है) ।"
                ],
                "english_gloss": [
                    "झूठ आखां (if I tell a lie) ते कुझ बचदा ए (then something of worldly face is saved), सच्च आख्यां (if I speak the truth) भांबड़ मचदा ए (a roaring fire blazes forth),",
                    "जी दोहां गल्लां तों जचदा ए (the soul hesitates and weighs both options), जच जच के (weighing and testing carefully) जेहवा कहन्दी ए (yet the tongue speaks out) ।",
                    "मूंह आई बात (the word that rises to the lips) ना रहन्दी ए (cannot be contained within) ।"
                ],
                "poetic_hindi": [
                    "झूठ कहूँ तो कुछ बचता है, सच बोलूँ तो भड़कती आग,",
                    "मन दोनों बातों को तौले, पर जिह्वा बोले सच का राग !",
                    "मुख आई बात न रुकती है, सच की धारा न छुपती है !"
                ],
                "poetic_english": [
                    "If I speak lies, some worldly grace is spared; if I speak truth, a furious fire will rage;",
                    "Between the two the trembling spirit wavers, yet boldly speaks across this darkened age:",
                    "The truth that rises to the lips cannot be kept within!"
                ]
            },
            {
                "original": [
                    "जिस पाइआ भेत कलन्दर दा, राह खोज्या आपने अन्दर दा,  ",
                    "उह वासी है सुक्ख मन्दर दा, जिथे कोई ना चढ़दी लहन्दी ए ।  ",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "hindi_gloss": [
                    "जिस (जिस साधक ने) पाइआ (पा लिया है) भेत (गूढ़ रहस्य) कलन्दर (मस्त कलंदर/सद्गुरु) दा (का), राह (और मार्ग) खोज्या (खोज निकाला है) आपने (अपने ही) अन्दर (अंतःकरण) दा (का),",
                    "उह (वह) वासी (निवासी बन चुका) है (है) सुक्ख (परमानंद के उस) मन्दर (मंदिर/धाम) दा (का), जिथे (जहाँ संसार की) कोई (कोई भी हानि-लाभ की धूप-छांव) ना (नहीं) चढ़दी (उठती) लहन्दी (या गिरती) ए (है) ।",
                    "मूंह (मुख पर) आई (आई) बात (बात) ना (नहीं) रहन्दी (छिपती) ए (है) ।"
                ],
                "english_gloss": [
                    "जिस पाइआ भेत कलन्दर दा (who discovered the secret of the Qalandar), राह खोज्या आपने अन्दर दा (searched the path within his own self),",
                    "उह वासी है सुक्ख मन्दर दा (he becomes a dweller of the Temple of Peace), जिथे कोई ना चढ़दी लहन्दी ए (where no tide rises or falls) ।",
                    "मूंह आई बात ना रहन्दी ए (the truth that rises to the lips cannot be kept within) ।"
                ],
                "poetic_hindi": [
                    "जिसने कलंदर का भेद पाया, अपने ही भीतर राह बनाया,",
                    "वो सुख-मंदिर का वासी हुआ, जहाँ कोई उतार-चढ़ाव न आया !",
                    "मुख आई बात न रुकती है !"
                ],
                "poetic_english": [
                    "Who found the secret of the free Qalandar, and searched the highway deep within his soul,",
                    "Dwells in the sanctuary of pure peace, where no wild tides of ebb and sorrow roll:",
                    "The truth that rises to the lips cannot be kept within!"
                ]
            },
            {
                "original": [
                    "इक लाज़म बात अदब दी ए सानूं बात मलूमी सभ दी ए,  ",
                    "हर हर विच सूरत रब्ब दी ए किते ज़ाहर किते छुपेंदी ए ।  ",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "hindi_gloss": [
                    "इक (एक ओर) लाज़म (अनिवार्य) बात (नियम है) अदब (मर्यादा और शिष्टाचार) दी (का), ए (परंतु) सानूं (मुझको) बात (हकीकत) मलूमी (ज्ञात) सभ (सब) दी (की) ए (है),",
                    "हर (प्रत्येक) हर (प्राणी) विच (के भीतर) सूरत (छवि/स्वरूप) रब्ब (परमात्मा) दी (का ही) ए (है), किते (कहीं पर वह) ज़ाहर (प्रकट रूप में) किते (और कहीं) छुपेंदी (छिपी हुई) ए (है) ।",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "english_gloss": [
                    "इक लाज़म बात अदब दी ए (custom demands the decorum of silence), सानूं बात मलूमी सभ दी ए (yet the truth of all is revealed to us),",
                    "हर हर विच सूरत रब्ब दी ए (in every single being is the visage of God), किते ज़ाहर (somewhere manifest) किते छुपेंदी ए (somewhere concealed) ।",
                    "मूंह आई बात ना रहन्दी ए (the truth that rises to the lips cannot be kept within) ।"
                ],
                "poetic_hindi": [
                    "मर्यादा कहती मौन रहो, पर हकीकत मुझको मालूम हुई,",
                    "कण-कण में सूरत रब की है, कहीं खुली तो कहीं गुमसुम हुई !",
                    "मुख आई बात न रुकती है !"
                ],
                "poetic_english": [
                    "Decorum claims that silence must be kept, yet all reality is clear to me;",
                    "In every creature shines the form of God, unveiled in light or veiled in mystery:",
                    "The truth that rises to the lips cannot be kept within!"
                ]
            },
            {
                "original": [
                    "एथे दुनियां विच अन्हेरा ए इह तिलकन बाज़ी वेहड़ा ए,  ",
                    "वड़ अन्दर वेखो केहड़ा ए क्युं खफ़तन बाहर ढूंडेदी ए ।  ",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "hindi_gloss": [
                    "एथे (यहाँ इस) दुनियां (संसार) विच (में घोर अज्ञान का) अन्हेरा (अंधेरा) ए (है), इह (यह संसार तो) तिलकन (फिसलन भरा) बाज़ी (मायावी) वेहड़ा (आँगन) ए (है),",
                    "वड़ (प्रविष्ट होकर) अन्दर (भीतर) वेखो (देखो कि भीतर बैठा) केहड़ा (कौन) ए (है), क्युं (क्यों तेरी अज्ञानता) खफ़तन (अंधी होकर) बाहर (बाहरी संसार में) ढूंडेदी (उसे ढूँढती फिरती) ए (है) ।",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "english_gloss": [
                    "एथे दुनियां विच अन्हेरा ए (here in this world is thick darkness), इह तिलकन बाज़ी वेहड़ा ए (this courtyard is slippery and deceptive),",
                    "वड़ अन्दर वेखो केहड़ा ए (enter within and behold who abides there), क्युं खफ़तन बाहर ढूंडेदी ए (why do you wander blind searching outside) ।",
                    "मूंह आई बात ना रहन्दी ए (the truth that rises to the lips cannot be kept within) ।"
                ],
                "poetic_hindi": [
                    "इस दुनिया में घोर अंधेरा, फिसलन भरा यह आँगन सारा,",
                    "भीतर जा कर देख कौन है, बाहर क्यों भटके जग बंजारा?",
                    "मुख आई बात न रुकती है !"
                ],
                "poetic_english": [
                    "A blinding darkness wraps this mortal realm; this courtyard is a treacherous, slippery floor;",
                    "Step in and see Who dwells within your heart—why wander searching at the outer door?",
                    "The truth that rises to the lips cannot be kept within!"
                ]
            },
            {
                "original": [
                    "एथे लेखा पायों पसारा ए इहदा वखरा भेत न्यारा ए,  ",
                    "इह सूरत दा चमकारा ए जिवें चिनग दारू विच पैंदी ए ।  ",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "hindi_gloss": [
                    "एथे (यहाँ जो सृष्टि का) लेखा (विस्तार और) पायों (रचा हुआ) पसारा (प्रसार) ए (है), इहदा (इसका) वखरा (अनोखा ही) भेत (रहस्य) न्यारा (न्यारा) ए (है),",
                    "इह (यह सारा ब्रह्मांड उस परमात्मा की) सूरत (दिव्य छवि) दा (का ही) चमकारा (प्रकाश) ए (है), जिवें (जैसे) चिनग (अग्नि की एक चिंगारी) दारू (बारूद) विच (में) पैंदी (पड़ते ही सब उड़ा देती) ए (है) ।",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "english_gloss": [
                    "एथे लेखा पायों पसारा ए (this vast cosmic expanse laid out here), इहदा वखरा भेत न्यारा ए (has a wondrous secret of its own),",
                    "इह सूरत दा चमकारा ए (it is the flashing radiance of His Countenance), जिवें चिनग दारू विच पैंदी ए (just as a spark falls into gunpowder) ।",
                    "मूंह आई बात ना रहन्दी ए (the truth that rises to the lips cannot be kept within) ।"
                ],
                "poetic_hindi": [
                    "यह जो फैला जगत-पसारा, इसका भेद बड़ा ही न्यारा,",
                    "उसकी छवि की चमक है ऐसी, जैसे बारूद में पड़े अंगारा !",
                    "मुख आई बात न रुकती है !"
                ],
                "poetic_english": [
                    "This vast expanse of cosmic majesty conceals a mystery unique and bright;",
                    "It is the blinding flash of His own face, like gunpowder ignited by a spark of light:",
                    "The truth that rises to the lips cannot be kept within!"
                ]
            },
            {
                "original": [
                    "किते नाज़ अदा दिखलाईदा, किते हो रसूल मिलाईदा,  ",
                    "किते आशक बण बण आईदा, किते जान जुदाई सहन्दी ए ।  ",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "hindi_gloss": [
                    "किते (कहीं पर वह प्रियतम बनकर) नाज़ (नाज़-) अदा (अदाएं) दिखलाईदा (दिखाता है), किते (कहीं पर) हो (होकर) रसूल (पैगंबर) मिलाईदा (उम्मत को परमात्मा से मिलाता है),",
                    "किते (कहीं पर स्वयं विरही) आशक (आशिक) बण (बन-) बण (बनकर) आईदा (आता है), किते (और कहीं उसकी) जान (प्राण) जुदाई (विरह की ज्वाला) सहन्दी (सहन करते हैं) ए (है) ।",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "english_gloss": [
                    "किते नाज़ अदा दिखलाईदा (somewhere He displays coquettish charm), किते हो रसूल मिलाईदा (somewhere as the Prophet He unites hearts with God),",
                    "किते आशक बण बण आईदा (somewhere He appears as the yearning lover), किते जान जुदाई सहन्दी ए (somewhere His own soul endures separation's pangs) ।",
                    "मूंह आई बात ना रहन्दी ए (the truth that rises to the lips cannot be kept within) ।"
                ],
                "poetic_hindi": [
                    "कहीं नाज़-अदा दिखलाता है, कहीं रसूल बन मिलाता है,",
                    "कहीं आशिक बन तड़पता खुद, कहीं विरह की ज्वाला सहता है !",
                    "मुख आई बात न रुकती है !"
                ],
                "poetic_english": [
                    "Somewhere He flaunts His beauty's coquetry; somewhere as Prophet He unites the soul;",
                    "Somewhere as Lover He weeps in longing; somewhere in parting pays the bitter toll:",
                    "The truth that rises to the lips cannot be kept within!"
                ]
            },
            {
                "original": [
                    "जदों ज़ाहर होए नूर हुरीं, जल गए पहाड़ कोह-तूर हुरीं,  ",
                    "तदों दार चढ़े मनसूर हुरीं, ओथे शेखी पेश ना वैंदी ए ।  ",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "hindi_gloss": [
                    "जदों (जब) ज़ाहर (प्रकट) होए (हुए परमात्मा के) नूर (दिव्य नूर के दर्शन) हुरीं (स्वयं), जल (जलकर भस्म) गए (हो गया) पहाड़ (पहाड़) कोह-तूर (कोहे-तूर का) हुरीं (सहित),",
                    "तदों (उसी सत्य के उद्घोष पर) दार (सूली पर) चढ़े (चढ़ाए गए) मनसूर (मंसूर हल्लाज) हुरीं (जैसे संत), ओथे (उस परमात्मा के दरबार में रूढ़िवादियों की कोई) शेखी (दंभ/शेखी) पेश (प्रस्तुत/सफल) ना (नहीं) वैंदी (होती) ए (है) ।",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "english_gloss": [
                    "जदों ज़ाहर होए नूर हुरीं (when the Divine Light manifested unveiled), जल गए पहाड़ कोह-तूर हुरीं (Mount Sinai itself was burnt to cinders),",
                    "तदों दार चढ़े मनसूर हुरीं (then Mansur was raised upon the gallows), ओथे शेखी पेश ना वैंदी ए (there the boasts of the orthodox avail nothing) ।",
                    "मूंह आई बात ना रहन्दी ए (the truth that rises to the lips cannot be kept within) ।"
                ],
                "poetic_hindi": [
                    "जब नूर प्रकट हुआ साहिब का, जल कर राख हुआ कोह-तूर,",
                    "उसी सत्य की खातिर देखो, सूली पे चढ़ गया मंसूर !",
                    "मुख आई बात न रुकती है !"
                ],
                "poetic_english": [
                    "When His unclouded Light shone forth, Mount Sinai burned to ashes on the height;",
                    "Upon the gallows Mansur gave his head; no pious boast avails before that Light:",
                    "The truth that rises to the lips cannot be kept within!"
                ]
            },
            {
                "original": [
                    "जे ज़ाहर करां इसरार ताईं, सभ भुल्ल जावन तकरार ताईं,  ",
                    "फिर मारन बुल्ल्हे यार ताईं, एथे मख़फ़ी गल्ल सोहेंदी ए ।  ",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "hindi_gloss": [
                    "जे (यदि) ज़ाहर (प्रकट) करां (कर दूँ मैं इस) इसरार (परम रहस्य) ताईं (को), सभ (सारे लोग) भुल्ल (भूल) जावन (जाएँगे अपने सारे बाह्य) तकरार (धार्मिक विवादों) ताईं (को),",
                    "फिर (परंतु इसके बाद वे पाखंडी) मारन (मार डालेंगे) बुल्ल्हे (बुल्ले जैसे) यार (प्रेमी) ताईं (को), एथे (इसलिए यहाँ इस) मख़फ़ी (गुप्त) गल्ल (रहस्य में ही शोभा) सोहेंदी (होती) ए (है) ।",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "english_gloss": [
                    "जे ज़ाहर करां इसरार ताईं (if I disclose the esoteric mystery), सभ भुल्ल जावन तकरार ताईं (all will forget their theological disputes),",
                    "फिर मारन बुल्ल्हे यार ताईं (yet then they will murder Bulleh the lover), एथे मख़फ़ी गल्ल सोहेंदी ए (here the concealed truth is most becoming) ।",
                    "मूंह आई बात ना रहन्दी ए (the truth that rises to the lips cannot be kept within) ।"
                ],
                "poetic_hindi": [
                    "गर खोल दूँ इस रहस्य को मैं, जग भूल जाए तकरार सारा,",
                    "पर मार डालेंगे बुल्ले को वो, इस भेद में पर्दा ही प्यारा !",
                    "मुख आई बात न रुकती है !"
                ],
                "poetic_english": [
                    "Were I to lay the secret bare, all theological feuds would cease to exist;",
                    "Yet they would slay this lover Bulleh—concealment suits this mystic mist:",
                    "The truth that rises to the lips cannot be kept within!"
                ]
            },
            {
                "original": [
                    "असां पढ़आ इलम तहकीकी ए ओथे इको हरफ़ हकीकी ए,  ",
                    "होर झगड़ा सभ वधीकी ए ऐवें रौला पा पा बहन्दी ए ।  ",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "hindi_gloss": [
                    "असां (हमने) पढ़आ (पढ़ा है) इलम (ज्ञान) तहकीकी (सत्य के साक्षात्कार/अनुभूति का) ए (है), ओथे (उस ज्ञान में) इको (केवल एक ही) हरफ़ (अक्षर—अलिफ़/परमेश्वर) हकीकी (सच्चा) ए (है),",
                    "होर (अन्य) झगड़ा (सारे विवाद) सभ (सब) वधीकी (व्यर्थ का प्रपंच/अनावश्यक) ए (हैं), ऐवें (संसार व्यर्थ ही) रौला (शोर-शराबा) पा (मचा-) पा (मचा कर) बहन्दी (बैठा रहता) ए (है) ।",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "english_gloss": [
                    "असां पढ़आ इलम तहकीकी ए (we have studied the knowledge of verified Truth), ओथे इको हरफ़ हकीकी ए (there a single letter alone is Real),",
                    "होर झगड़ा सभ वधीकी ए (all other dispute is superfluous excess), ऐवें रौला पा पा बहन्दी ए (people merely sit raising empty clamor) ।",
                    "मूंह आई बात ना रहन्दी ए (the truth that rises to the lips cannot be kept within) ।"
                ],
                "poetic_hindi": [
                    "हमने पढ़ी है तहकीक की विद्या, जहाँ एक ही हर्फ़ हकीकी है,",
                    "और सारे झगड़े व्यर्थ के हैं, दुनिया में बस शोर-शराबा ही है !",
                    "मुख आई बात न रुकती है !"
                ],
                "poetic_english": [
                    "We read the science of verified Truth, where but a single Letter stands sincere;",
                    "All other arguments are idle excess, an empty noise the worldly love to hear:",
                    "The truth that rises to the lips cannot be kept within!"
                ]
            },
            {
                "original": [
                    "ए शाह अकल तूं आया कर, सानूं अदब अदाब सिखाइआ कर,  ",
                    "मैं झूठी नूं समझाइआ कर, जो मूरख माहनूं कहन्दी ए ।  ",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "hindi_gloss": [
                    "ए (हे) शाह (बादशाह) अकल (सांसारिक बुद्धि के स्वामी), तूं (तू) आया (आया) कर (कर मेरे पास), सानूं (मुझको दुनियावी) अदब (मर्यादा और) अदाब (सलीका) सिखाइआ (सिखाया) कर,",
                    "मैं (मुझ) झूठी (प्रेम-दीवानी/झूठी) नूं (को) समझाइआ (समझाया) कर, जो (जो यह दुनियावी बुद्धि मुझको) मूरख (मूर्ख) माहनूं (मानव) कहन्दी (कहती) ए (है) ।",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "english_gloss": [
                    "ए शाह अकल (O king of worldly intellect) तूं आया कर (come unto me), सानूं अदब अदाब सिखाइआ कर (teach us your etiquette and manners),",
                    "मैं झूठी नूं समझाइआ कर (counsel me, the 'false' and crazed one), जो मूरख माहनूं कहन्दी ए (whom worldly folk brand as a foolish human) ।",
                    "मूंह आई बात ना रहन्दी ए (the truth that rises to the lips cannot be kept within) ।"
                ],
                "poetic_hindi": [
                    "ऐ अक्ल के बादशाह, आ मुझे भी दुनियावी सलीका सिखा,",
                    "मुझ दीवानी को समझा ज़रा, जिसे दुनिया मूर्ख कहती सदा !",
                    "मुख आई बात न रुकती है !"
                ],
                "poetic_english": [
                    "O Sovereign Intellect, draw near, and teach us all your etiquette and rules;",
                    "Counsel this 'false' and foolish soul, condemned as mad in worldly schools:",
                    "The truth that rises to the lips cannot be kept within!"
                ]
            },
            {
                "original": [
                    "वाह वाह कुदरत बेपरवाही ए देवे कैदी दे सिर शाही ए,  ",
                    "ऐसा बेटा जाइआ माई ए सभ कलमा उस दा कहन्दी ए ।  ",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "hindi_gloss": [
                    "वाह (धन्य है) वाह (धन्य है), कुदरत (ईश्वर की कुदरत की यह) बेपरवाही (सर्वस्वतंत्र लीला) ए (है), देवे (जो पहना देती है) कैदी (जेल के बंदी यूसुफ) दे (के) सिर (सिर पर) शाही (मिस्र का राजमुकुट) ए (है),",
                    "ऐसा (ऐसा अद्भुत) बेटा (पुत्र/मुहम्मद) जाइआ (जना है) माई (माता अमीना ने) ए (है), सभ (कि सारी कायनात) कलमा (कलमा) उस (उसका) दा (का) कहन्दी (पढ़ती) ए (है) ।",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "english_gloss": [
                    "वाह वाह कुदरत बेपरवाही ए (wondrous is the sovereignty of Nature/Divine Will), देवे कैदी दे सिर शाही ए (crowns a captive in prison with kingship),",
                    "ऐसा बेटा जाइआ माई ए (such a son did the Mother bear), सभ कलमा उस दा कहन्दी ए (the whole creation recites His praise and Kalima) ।",
                    "मूंह आई बात ना रहन्दी ए (the truth that rises to the lips cannot be kept within) ।"
                ],
                "poetic_hindi": [
                    "वाह री कुदरत की बेपरवाही ! कैदी के सिर पे ताज धरा,",
                    "ऐसा बेटा जन्मा माँ ने, जग जिसका कलमा पढ़ता खड़ा !",
                    "मुख आई बात न रुकती है !"
                ],
                "poetic_english": [
                    "Wondrous is Nature's sovereign sway, which crowns a dungeon captive king;",
                    "Such was the Son a mother bore, whose Kalima all creations sing:",
                    "The truth that rises to the lips cannot be kept within!"
                ]
            },
            {
                "original": [
                    "इस आज़िज़ दा की हीला ए रंग ज़रद ते मुक्खड़ा पीला ए,  ",
                    "जिथे आपे आप वसीला ए ओथे की अदालत कहन्दी ए ।  ",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "hindi_gloss": [
                    "इस (मुझ) आज़िज़ (दीन-हीन अकिंचन साधक) दा (का भला) की (क्या) हीला (यत्न/उपाय) ए (हो सकता है), रंग (मेरा रंग) ज़रद (उड़ चुका) ते (और) मुक्खड़ा (मुखड़ा) पीला (पीला पड़ चुका) ए (है),",
                    "जिथे (जहाँ पर परमात्मा) आपे (स्वयं ही न्यायकर्ता) आप (और स्वयं ही एकमात्र) वसीला (साधन/माध्यम) ए (है), ओथे (वहाँ सांसारिक काजियों की) की (क्या) अदालत (अदालत) कहन्दी (फैसला सुना सकती) ए (है) ।",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "english_gloss": [
                    "इस आज़िज़ दा की हीला ए (what plea can this helpless mendicant make), रंग ज़रद ते मुक्खड़ा पीला ए (with pale complexion and ashen face),",
                    "जिथे आपे आप वसीला ए (where He Himself is the sole Means and Judge), ओथे की अदालत कहन्दी ए (what decree can any mortal court proclaim) ।",
                    "मूंह आई बात ना रहन्दी ए (the truth that rises to the lips cannot be kept within) ।"
                ],
                "poetic_hindi": [
                    "मुझ अकिंचन का क्या चारा, पीला मुखड़ा, रंग उड़ा हुआ,",
                    "जहाँ वो खुद ही वसीला है, वहाँ कौन सी अदालत फैसला सुनाए भला?",
                    "मुख आई बात न रुकती है !"
                ],
                "poetic_english": [
                    "What plea can this poor wretch present, with pale visage and trembling knee?",
                    "Where He Himself is Judge and Means, what court can pass decree on me?",
                    "The truth that rises to the lips cannot be kept within!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु असां थीं वक्ख नहीं, बिन शहु थीं दूजा कक्ख नहीं,  ",
                    "पर वेखन वाली अक्ख नहीं, ताहीं जान जुदाईआं सहन्दी ए ।  ",
                    "मूंह आई बात ना रहन्दी ए ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ले शाह उद्घोष करते हैं) शहु (वह परम प्रियतम परमात्मा) असां (हमसे) थीं (से) वक्ख (अलग/पृथक) नहीं (बिल्कुल नहीं है), बिन (उसके बिना) शहु (प्रियतम के) थीं (अलावा) दूजा (दूसरा) कक्ख (एक तिनका भी) नहीं (अस्तित्व में नहीं है),",
                    "पर (परंतु अज्ञानी मनुष्यों के पास उसे) वेखन (पहचानने) वाली (वाली दिव्य) अक्ख (आँख) नहीं (नहीं है), ताहीं (तभी तो अज्ञानवश) जान (जीवात्मा) जुदाईआं (विरह के कष्ट) सहन्दी (झेलती रहती) ए (है) ।",
                    "मूंह (मुख तक) आई (आ पहुँची) बात (सत्य की बात कभी) ना (नहीं) रहन्दी (दबी रह सकती) ए (है) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा शहु असां थीं वक्ख नहीं (Bulleh: the Sovereign Lord is not separate from us), बिन शहु थीं दूजा कक्ख नहीं (without the Lord not a straw exists),",
                    "पर वेखन वाली अक्ख नहीं (yet the eye to perceive Him is lacking), ताहीं जान जुदाईआं सहन्दी ए (hence the soul endures the pangs of separation) ।",
                    "मूंह आई बात ना रहन्दी ए (the truth that rises to the lips cannot be kept within) ।"
                ],
                "poetic_hindi": [
                    "बुल्ला कहे: साहिब हमसे जुदा नहीं, प्रभु बिन दूजा तिनका नहीं,",
                    "पर देखने वाली आँख नहीं, तभी विरह की मार सही !",
                    "मुख आई बात न रुकती है, सच की धारा न छुपती है !"
                ],
                "poetic_english": [
                    "Says Bulleh: The Sovereign is not apart; without Him exists not a blade of grass;",
                    "Yet blind mortals lack the seeing eye, and let this night of sorrow pass!",
                    "The truth that rises to the lips cannot be kept within!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी सूफी दर्शन के इतिहास में एक मील का पत्थर है। यह कविता उस आंतरिक अग्नि का प्रकटीकरण है जिसे दार्शनिक 'सत्य की अनिवार्यता' कहते हैं। बुल्ले शाह स्पष्ट करते हैं कि जब रहस्य का अनुभव हो जाता है तो मनुष्य मौन नहीं रह सकता, चाहे संसार उसके प्राण ही क्यों न ले ले। 'बिन शहु थीं दूजा कक्ख नहीं' सर्वेश्वरवाद (वहदत-उल-वुजूद) का अंतिम सूत्र है—संसार में परमात्मा के अतिरिक्त किसी वस्तु की स्वतंत्र सत्ता नहीं है। विरह केवल दृष्टि के अभाव ('वेखन वाली अक्ख नहीं') के कारण प्रतीत होता है; जैसे ही ज्ञान की आँख खुलती है, द्वैत का भ्रम समाप्त हो जाता है।"
    },
    {
        "id": 108,
        "title": "मुल्लां मैनूं मारदा ई",
        "title_english": "The Mullah Beats Me For Loving Alif!",
        "historical_context": "यह 2 बंधों की एक अत्यंत तीखी, प्रतीकात्मक और संक्षिप्त काफी है। इसमें बुल्ले शाह मदरसे की औपचारिक, शुष्क और तोता-रटंत शिक्षा प्रणाली की तुलना हृदय की आत्मानुभूति से करते हैं। मुल्ला बालक बुल्ले को वर्णमाला सिखाता है, परंतु बुल्ला पहले अक्षर 'अलिफ़' (एक ईश्वर) पर ही अटक जाता है और दूसरे अक्षर 'बे' (संसार/द्वैत) पर जाने से इनकार कर देता है। इस पर मुल्ला क्रोधित होकर उसे मारता है। यह काफी रूढ़िवादी मौलवियों द्वारा अद्वैतवादी संतों पर किए जाने वाले अत्याचारों का रूपक है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: मुल्लां मैनूं मारदा ई)",
        "raga": "राग काफी / आसा",
        "theme": "अलिफ़ (एकेश्वरवाद) बनाम बे (द्वैत), मुल्ला का पाखंड, औपचारिक शिक्षा का तिरस्कार",
        "stanzas": [
            {
                "original": [
                    "मुल्लां मैनूं मारदा ई ।  ",
                    "मुल्लां मैनूं मारदा ई ।"
                ],
                "hindi_gloss": [
                    "मुल्लां (रूढ़िवादी मुल्ला) मैनूं (मुझको व्यर्थ ही) मारदा (पीटता/मारता) ई (है) ।",
                    "मुल्लां (मुल्ला) मैनूं (मुझको) मारदा (मारता) ई (है) ।"
                ],
                "english_gloss": [
                    "मुल्लां (the orthodox cleric/Mullah) मैनूं (me) मारदा ई (beats/chastises) ।",
                    "मुल्लां मैनूं मारदा ई (the Mullah beats me without cause) ।"
                ],
                "poetic_hindi": [
                    "मुल्ला मुझको मारता है रे, मुल्ला मुझको मारता है !",
                    "एक अलिफ़ के फेर में देखो, व्यर्थ मुझको सताता है !"
                ],
                "poetic_english": [
                    "The Mullah beats me with his rod, the Mullah strikes me sore!",
                    "For clinging to the Single God, he chastens more and more!"
                ]
            },
            {
                "original": [
                    "मुल्लां मैनूं सबक पढ़ाइआ।  ",
                    "अलफों अग्गे कुझ ना आया ।  ",
                    "उह बे ई बे पुकारदा ई ।  ",
                    "मुल्लां मैनूं मारदा ई ।"
                ],
                "hindi_gloss": [
                    "मुल्लां (मुल्ला ने) मैनूं (मुझको विद्या का) सबक (पाठ) पढ़ाइआ (पढ़ाया),",
                    "अलफों (परंतु अलिफ़/एक परमात्मा से) अग्गे (आगे बढ़कर) कुझ (कुछ भी मेरे मन में) ना (नहीं) आया (समाया),",
                    "उह (वह मुल्ला केवल द्वैत का अक्षर) बे (बे) ई (ही) बे (बे) पुकारदा (पुकारता और रटवाता रहता) ई (है) ।",
                    "मुल्लां (मुल्ला) मैनूं (मुझको) मारदा (मारता) ई (है) ।"
                ],
                "english_gloss": [
                    "मुल्लां मैनूं सबक पढ़ाइआ (the Mullah taught me the lesson),",
                    "अलफों अग्गे कुझ ना आया (beyond Alif, nothing would enter my heart),",
                    "उह बे ई बे पुकारदा ई (he keeps shouting 'Bay! Bay!' demanding duality),",
                    "मुल्लां मैनूं मारदा ई (the Mullah beats me relentlessly) ।"
                ],
                "poetic_hindi": [
                    "मुल्ला ने जब सबक पढ़ाया, अलिफ़ से आगे कुछ न आया,",
                    "वो 'बे-बे' की रट लगाए, मुझ पर डंडा बरसाए !",
                    "मुल्ला मुझको मारता है रे !"
                ],
                "poetic_english": [
                    "The Mullah taught his learned scroll, but past 'Alif' my mind won’t stray;",
                    "He screams for 'Bay' with rigid soul, and beats me when I turn away!",
                    "The Mullah strikes me sore!"
                ]
            }
        ],
        "sufi_commentary": "यह सूक्ष्म और चुटीली काफी सूफी दर्शन के बुनियादी सिद्धांत को उजागर करती है। अरबी वर्णमाला का पहला अक्षर 'अलिफ़' अल्लाह (एक ओंकार/अद्वैत) का प्रतीक है, जबकि दूसरा अक्षर 'बे' द्वैत (संसार, दोई, भेद) का सूचक है। सूफी साधक का मन जब एक बार अलिफ़ के दिव्य रस में रंग जाता है, तो वह 'बे' अर्थात् सांसारिक कर्मकांडों और विभाजनों को स्वीकार नहीं कर सकता। मुल्ला का मारना रूढ़िवादी शरिया द्वारा रहस्यवादी साधकों को प्रताड़ित करने का सार्वभौमिक प्रतीक है।"
    },
    {
        "id": 109,
        "title": "मुरली बाज उठी अणघातां",
        "title_english": "The Divine Flute Has Sounded at an Unearthly Hour!",
        "historical_context": "यह 5 बंधों की एक अत्यंत संगीतमय और वैष्णव-सूफी समन्वय से ओतप्रोत काफी है। इसमें श्रीकृष्ण की बंसी को सूफी 'अनहद नाद' के रूप में देखा गया है। जब अंतर्मन में अनहद बंसी बजती है ('अणघातां' अर्थात् असमय/अलौकिक पहर में), तो सांसारिक बातें और प्रपंच विस्मृत हो जाते हैं। मन रूपी चंचल हिरन प्रेम के जाल में फंस जाता है। बुल्ले शाह इसमें दो रकअत की नमाज़ (इश्क का दुगाना) और नबी मुहम्मद की शफ़ाअत का भी सुंदर समन्वय करते हैं।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: मुरली बाज उठी अणघातां)",
        "raga": "राग सारंग / काफी",
        "theme": "अनहद नाद की मुरली, वैष्णव-सूफी समन्वय, चंचल मन का वशीकरण, प्रेम की नमाज़",
        "stanzas": [
            {
                "original": [
                    "मुरली बाज उठी अणघातां ।  ",
                    "सुन के भुल्ल गईआं सभ बातां ।"
                ],
                "hindi_gloss": [
                    "मुरली (दिव्य मुरली) बाज (बज) उठी (उठी है) अणघातां (असमय/अलौकिक पहर में),",
                    "सुन (उसे सुनकर) के (करके) भुल्ल (विस्मृत हो) गईआं (गई हैं मुझे) सभ (संसार की सारी) बातां (बातें और झंझट) ।"
                ],
                "english_gloss": [
                    "मुरली बाज उठी (the Flute has resounded) अणघातां (at an unearthly, timeless hour),",
                    "सुन के (hearing it) भुल्ल गईआं (forgotten are) सभ बातां (all worldly discourses) ।"
                ],
                "poetic_hindi": [
                    "अलौकिक वेला में बंसी बजी, गूँज उठी अनहद की तान,",
                    "सुनते ही संसार भूला, भूला जग का सारा भान !"
                ],
                "poetic_english": [
                    "The Flute has sounded at a timeless hour, resonant and sweet;",
                    "Hearing its call, all earthly tales lay forgotten at its feet!"
                ]
            },
            {
                "original": [
                    "लग्ग गए अनहद बान न्यारे, झूठी दुनियां कूड़ पसारे,  ",
                    "साईं मुक्ख वेखन वणजारे, मैनूं भुल्ल गईआं सभ बातां ।  ",
                    "मुरली बाज उठी अणघातां ।"
                ],
                "hindi_gloss": [
                    "लग्ग (लग) गए (चुके हैं) अनहद (अनाहत नाद के) बान (तीखे प्रेम-बाण) न्यारे (अनोखे), झूठी (यह मिथ्या) दुनियां (दुनिया है और) कूड़ (असत्य के हैं इसके सारे) पसारे (पसारे),",
                    "साईं (सच्चे स्वामी का) मुक्ख (मुखड़ा) वेखन (देखते हैं पिपासु) वणजारे (सच्चे साधक), मैनूं (मुझको) भुल्ल (विस्मृत हो) गईआं (गई हैं) सभ (सब) बातां (बातें) ।",
                    "मुरली बाज उठी अणघातां ।"
                ],
                "english_gloss": [
                    "लग्ग गए अनहद बान न्यारे (wondrous arrows of Anhad pierced the heart), झूठी दुनियां कूड़ पसारे (the world is false, its expanse a fleeting lie),",
                    "साईं मुक्ख वेखन वणजारे (true seeking traders gaze upon the Master's face), मैनूं भुल्ल गईआं सभ बातां (all tales have vanished from my mind) ।",
                    "मुरली बाज उठी अणघातां ।"
                ],
                "poetic_hindi": [
                    "अनहद के तीखे तीर लगे, झूठी दुनिया के ढोंग भगे,",
                    "सच्चे व्यापारी मुखड़ा देखें, सोए हुए सब भाग जगे !",
                    "मुरली बजी अणघातां !"
                ],
                "poetic_english": [
                    "The piercing darts of Anhad struck, shattering this false worldly maze;",
                    "Truth-seeking merchants gather round to fix upon the Master’s gaze!",
                    "The Flute has sounded at an unearthly hour!"
                ]
            },
            {
                "original": [
                    "हुन मैं चैंचल मिरग फहाइआ, ओसे मैनूं बन्न्ह बहाइआ,  ",
                    "सिरफ दुगाना इश्क पढ़ाइआ, रह गईआं त्रै चार कातां ।  ",
                    "मुरली बाज उठी अणघातां ।"
                ],
                "hindi_gloss": [
                    "हुन (अब) मैं (मैंने अपने) चैंचल (चंचल मन रूपी) मिरग (मृग/हिरन को प्रेम के फंदे में) फहाइआ (फांस लिया है), ओसे (उसी ने) मैनूं (मुझको साधना के खूंटे से) बन्न्ह (बांध कर) बहाइआ (बिठा दिया है),",
                    "सिरफ (केवल दो रकअत का) दुगाना (नमाज़-ए-इश्क) पढ़ाइआ (पढ़ाया है), रह (छूट) गईआं (गई हैं बाकी) त्रै (तीन) चार (चार रस्मी) कातां/रकआतां (औपचारिक नमाज़ें) ।",
                    "मुरली बाज उठी अणघातां ।"
                ],
                "english_gloss": [
                    "हुन मैं चैंचल मिरग फहाइआ (now I ensnared the restless deer of mind), ओसे मैनूं बन्न्ह बहाइआ (that very Love bound and seated me still),",
                    "सिरफ दुगाना इश्क पढ़ाइआ (it taught me solely the two-fold prayer of Love), रह गईआं त्रै चार कातां (leaving aside the three or four formal hours) ।",
                    "मुरली बाज उठी अणघातां ।"
                ],
                "poetic_hindi": [
                    "चंचल हिरन मन का फांसा, बाँध बिठाया प्रेम के धाम,",
                    "दो रकअत का इश्क पढ़ा जब, छूटे चारों पहर के काम !",
                    "मुरली बजी अणघातां !"
                ],
                "poetic_english": [
                    "I trapped the restless deer of mind; Love tethered me in peaceful thrall;",
                    "It taught the twofold prayer of grace, setting aside all ritual call!",
                    "The Flute has sounded at an unearthly hour!"
                ]
            },
            {
                "original": [
                    "बूहे आण खलोता यार, बाबल पुज्ज प्या तकरार,  ",
                    "कलमे नाल जे रहे वेहार, नबी मुहंमद भरे सफातां ।  ",
                    "मुरली बाज उठी अणघातां ।"
                ],
                "hindi_gloss": [
                    "बूहे (द्वार पर) आण (आकर) खलोता (खड़ा हुआ है मेरा प्यारा) यार (प्रियतम), बाबल (पिता चूचक ने) पुज्ज (खड़ा कर) प्या (दिया है) तकरार (व्यर्थ विवाद),",
                    "कलमे (सच्चे ईश्वरीय कलमे/नाम) नाल (के साथ) जे (यदि) रहे (रहेगा हमारा) वेहार (जीवन का व्यापार), नबी (तो स्वयं नबी) मुहंमद (मुहम्मद साहब) भरे (भरेंगे हमारी) सफातां (सिफारिश/शफ़ाअत) ।",
                    "मुरली बाज उठी अणघातां ।"
                ],
                "english_gloss": [
                    "बूहे आण खलोता यार (the Beloved has arrived and stands at the door), बाबल पुज्ज प्या तकरार (the father raises angry dispute),",
                    "कलमे नाल जे रहे वेहार (if our conduct abides by the true Kalima), नबी मुहंमद भरे सफातां (Prophet Muhammad Himself will intercede for us) ।",
                    "मुरली बाज उठी अणघातां ।"
                ],
                "poetic_hindi": [
                    "द्वारे पे आ खड़ा हुआ यार, पिता ने व्यर्थ बखेड़ा ठाना,",
                    "कलमे से जो सच्चा व्यापार करे, नबी ने उसकी शफ़ाअत माना !",
                    "मुरली बजी अणघातां !"
                ],
                "poetic_english": [
                    "My Sweetheart stands before the door, while father raises bitter strife;",
                    "If with the Kalima we trade, the Prophet intercedes for life!",
                    "The Flute has sounded at an unearthly hour!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हे शाह मैं हुन बरलाई, जद दी मुरली काहन बजाई,  ",
                    "बावरी हो तुसां वल्ल धाई, खोजियां कित वल दसत बारतां ।  ",
                    "मुरली बाज उठी अणघातां ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हे शाह (बुल्ले शाह कहते हैं) मैं (मैं तो) हुन (अब पूर्णतः) बरलाई (दीवानी/मतवाली हो चुकी हूँ), जद (जब) दी (से) मुरली (यह दिव्य बंसी) काहन (कान्हा/श्रीकृष्ण ने) बजाई (बजाई है),",
                    "बावरी (बावली होकर) हो (होकर) तुसां (तुम्हारी) वल्ल (ओर) धाई (दौड़ पड़ी हूँ), खोजियां (खोजी बनकर) कित (किस) वल (ओर) दसत (दश्त/बीहड़ जंगल के) बारतां (मार्गों को नापती फिरूँ) ।",
                    "मुरली बाज उठी अणघातां ।"
                ],
                "english_gloss": [
                    "बुल्ल्हे शाह मैं हुन बरलाई (says Bulleh: I have now become ecstatic and wild), जद दी मुरली काहन बजाई (ever since Krishna blew His magic Flute),",
                    "बावरी हो तुसां वल्ल धाई (mad in love I rushed towards Thee), खोजियां कित वल दसत बारतां (seeking Thy traces across the desert wilderness) ।",
                    "मुरली बाज उठी अणघातां ।"
                ],
                "poetic_hindi": [
                    "बुल्ला कहे: मैं दीवानी हुई, जब से कान्हा ने मुरली बजाई,",
                    "बावली हो तेरी ओर दौड़ी, बीहड़ में तेरी खोज लगाई !",
                    "मुरली बजी अणघातां !"
                ],
                "poetic_english": [
                    "Says Bulleh: Ecstatic have I grown since Krishna breathed His mystic melody;",
                    "Crazed with divine desire I ran across the desert sands to Thee!",
                    "The Flute has sounded at an unearthly hour!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी इस बात का अनुपम प्रमाण है कि बुल्ले शाह के लिए भारतीय कृष्ण-भक्ति और इस्लामी तसव्वुफ में कोई विरोध नहीं था। 'मुरली काहन' को वे अनहद नाद और रूहानी प्रेरणा का प्रतीक मानते हैं। जब यह दिव्य ध्वनि सुनाई देती है, तो सांसारिक विवाद और रस्मी औपचारिकताएं छूट जाती हैं। 'दुगाना इश्क' प्रेम की उस नमाज़ की ओर संकेत करता है जो चौबीसों घंटे बिना किसी दिशा या कर्मकांड के केवल हृदय में प्रियतम के सम्मुख अदा की जाती है।"
    },
    {
        "id": 110,
        "title": "ना जीवां महाराज, मैं तेरे बिन ना जीवां",
        "title_english": "I Cannot Live, O Maharaj, Without Thee I Cannot Live!",
        "historical_context": "यह 4 बंधों की अत्यंत विनयपूर्ण, आर्त और भक्तिभाव से परिपूर्ण काफी है। बुल्ले शाह परमात्मा को 'महाराज' कहकर पुकारते हैं और विरह की असह्यता का वर्णन करते हैं। वे मानव को चेतावनी देते हैं कि जीवन अत्यंत अल्प है और मृत्यु सिर पर खड़ी है, अतः प्रमाद की चादर तानकर सोने के स्थान पर परमात्मा के नाम का सुमिरन करना चाहिए। रो-रोकर दोनों नैन गंवा देने वाली विरहिणी आत्मा अंत में जब अपने प्रियतम को परदेस से आते देखती है, तो वह उसके नाम पर अपना शीश न्योछावर कर देती है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: ना जीवां महाराज)",
        "raga": "राग काफी / बिलावल / असावरी",
        "theme": "महाराज (ईश्वर) से अनन्य प्रार्थना, मृत्यु की निकटता की चेतावनी, विरह का रुदन, शीश-समर्पण",
        "stanzas": [
            {
                "original": [
                    "इहनां सुक्यां फुल्लां विच बास नहीं,  ",
                    "परदेस गयां दी कोई आस नहीं,  ",
                    "जेहड़े साईं साजन साडे पास नहीं,  ",
                    "ना जीवां महाराज, मैं तेरे बिन ना जीवां ।"
                ],
                "hindi_gloss": [
                    "इहनां (इन) सुक्यां (सूखे हुए) फुल्लां (मुरझाए फूलों) विच (में अब कोई) बास (सुगंध) नहीं (नहीं रही),",
                    "परदेस (परदेस) गयां (चले गए प्रियतमों की लौटने की) दी (की) कोई (कोई) आस (आशा) नहीं (नहीं बची),",
                    "जेहड़े (जब मेरे) साईं (सच्चे स्वामी) साजन (और प्यारे प्रियतम) साडे (हमारे) पास (निकट) नहीं (नहीं हैं),",
                    "ना (तो मैं नहीं) जीवां (जी सकती) महाराज (हे मेरे महाराज/प्रभु), मैं (मैं) तेरे (तेरे) बिन (बिना) ना (नहीं) जीवां (जी सकती) ।"
                ],
                "english_gloss": [
                    "इहनां सुक्यां फुल्लां विच बास नहीं (in these withered blossoms no fragrance remains),",
                    "परदेस गयां दी कोई आस नहीं (no hope lingers from those gone to distant lands),",
                    "जेहड़े साईं साजन साडे पास नहीं (when my Sovereign Beloved is not beside me),",
                    "ना जीवां महाराज (I cannot live, O Maharaj), मैं तेरे बिन ना जीवां (without Thee I cannot live) ।"
                ],
                "poetic_hindi": [
                    "सूखे फूलों में बास न कोई, परदेसी की आस न कोई,",
                    "जब साहिब-साजन पास न मेरे, मन का धीरज सारा खोई !",
                    "हे महाराज, मैं तेरे बिना जी नहीं सकती !"
                ],
                "poetic_english": [
                    "In withered petals no sweet perfume stays; no hope returns from far-off foreign ways;",
                    "When my Sovereign Lover is not near my side, desolate are my numbered days:",
                    "I cannot live, O Maharaj, without Thee I cannot live!"
                ]
            },
            {
                "original": [
                    "तूं की सुत्ता एं चादर तान के,  ",
                    "सिर मौत खलोती तेरे आण के,  ",
                    "कोई अमल ना कीता जान के,  ",
                    "ना जीवां महाराज, मैं तेरे बिन ना जीवां ।"
                ],
                "hindi_gloss": [
                    "तूं (तू) की (क्यों) सुत्ता (सो रहा) एं (है) चादर (अज्ञान की चादर) तान (तान) के (करके),",
                    "सिर (तेरे सिरहाने) मौत (मृत्यु) खलोती (आ खड़ी हुई है) तेरे (तेरे सम्मुख) आण (आ) के (करके),",
                    "कोई (तूने कोई भी शुभ) अमल (कर्म/साधना) ना (नहीं) कीता (की) जान (जान-) के (बूझकर),",
                    "ना (मैं नहीं) जीवां (जी सकती) महाराज (हे महाराज), मैं (मैं) तेरे (तेरे) बिन (बिना) ना (नहीं) जीवां (जी सकती) ।"
                ],
                "english_gloss": [
                    "तूं की सुत्ता एं चादर तान के (why sleepest thou pulling up the veil of heedlessness),",
                    "सिर मौत खलोती तेरे आण के (death has arrived and stands above thy head),",
                    "कोई अमल ना कीता जान के (wittingly thou hast performed no good deed),",
                    "ना जीवां महाराज मैं तेरे बिन ना जीवां (I cannot live, O Maharaj, without Thee) ।"
                ],
                "poetic_hindi": [
                    "चादर तान के क्यों सोता है, सिर पर काल खड़ा विकराल,",
                    "जान-बूझ कर कर्म न कीने, कैसे कटेगा यम का जाल?",
                    "हे महाराज, मैं तेरे बिना जी नहीं सकती !"
                ],
                "poetic_english": [
                    "Why sleepest thou pulling the shroud over head, while death stands tall above thy bed?",
                    "Knowingly thou hast gathered no righteous deeds, wandering where mortal folly led!",
                    "I cannot live, O Maharaj, without Thee I cannot live!"
                ]
            },
            {
                "original": [
                    "की मैं खट्ट्या तेरी हो के,  ",
                    "दोवें नैन गवाय रो के,  ",
                    "तेरा नाम लईए मुक्ख धो के,  ",
                    "ना जीवां महाराज, मैं तेरे बिन ना जीवां ।"
                ],
                "hindi_gloss": [
                    "की (क्या) मैं (मैंने) खट्ट्या (कमाई की) तेरी (तेरी दासी) हो (हो) के (कर),",
                    "दोवें (अपने दोनों) नैन (नेत्र) गवाय (गंवा दिए मैंने) रो (रो-) के (रोकर),",
                    "तेरा (तेरा पावन) नाम (नाम) लईए (लेती हूँ अपना) मुक्ख (मुखड़ा आंसुओं से) धो (धो) के (करके),",
                    "ना (मैं नहीं) जीवां (जी सकती) महाराज (हे मेरे महाराज), मैं (मैं) तेरे (तेरे) बिन (बिना) ना (नहीं) जीवां (जी सकती) ।"
                ],
                "english_gloss": [
                    "की मैं खट्ट्या तेरी हो के (what did I earn having surrendered to Thee),",
                    "दोवें नैन गवाय रो के (lost both eyes weeping in separation),",
                    "तेरा नाम लईए मुक्ख धो के (I invoke Thy Holy Name having washed my face in tears),",
                    "ना जीवां महाराज मैं तेरे बिन ना जीवां (I cannot live, O Maharaj, without Thee) ।"
                ],
                "poetic_hindi": [
                    "तेरी होकर क्या पाया मैंने, रो-रो दोनों नैन गँवाए,",
                    "अंसुअन से मुख धो-धो करके, तेरा पावन नाम ध्याए !",
                    "हे महाराज, मैं तेरे बिना जी नहीं सकती !"
                ],
                "poetic_english": [
                    "What did I gain by yielding my soul? I lost both eyes to bitter tears;",
                    "Washing my face, I chant Thy Name amidst the passing of the years:",
                    "I cannot live, O Maharaj, without Thee I cannot live!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु बदेसों आउंदा,  ",
                    "हत्थ कंगना ते बाहीं लटकाउंदा,  ",
                    "सिर सदका तेरे नाउं दा,  ",
                    "ना जीवां महाराज, मैं तेरे बिन ना जीवां ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ले शाह कहते हैं) शहु (मेरा परम प्रियतम) बदेसों (परदेस/अलौकिक लोक से) आउंदा (लौटकर आ रहा है),",
                    "हत्थ (हाथों में प्रेम का) कंगना (कंगन) ते (और) बाहीं (बाँहों को मस्तानी चाल में) लटकाउंदा (झुलाता हुआ),",
                    "सिर (मेरा यह शीश) सदका (न्योछावर/बलिहारी है) तेरे (तेरे पावन) नाउं (नाम) दा (का),",
                    "ना (मैं नहीं) जीवां (जी सकती) महाराज (हे महाराज), मैं (मैं) तेरे (तेरे) बिन (बिना) ना (नहीं) जीवां (जी सकती) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा शहु बदेसों आउंदा (Bulleh: the Sovereign Lord returns from the distant realm),",
                    "हत्थ कंगना ते बाहीं लटकाउंदा (bangles on wrist, swinging arms in graceful majesty),",
                    "सिर सदका तेरे नाउं दा (my head is an offering consecrated to Thy Name),",
                    "ना जीवां महाराज मैं तेरे बिन ना जीवां (I cannot live, O Maharaj, without Thee) ।"
                ],
                "poetic_hindi": [
                    "बुल्ला कहे: साहिब घर आए, हाथों में कंगन, बाहें झुलाए,",
                    "शीश न्योछावर तेरे नाम पे, मन का सारा क्लेश मिटाए !",
                    "हे महाराज, मैं तेरे बिना जी नहीं सकती !"
                ],
                "poetic_english": [
                    "Says Bulleh: The King returns from afar, with bangles swinging upon His arm;",
                    "My head is a consecrated gift unto Thy Name, shielded from harm!",
                    "I cannot live, O Maharaj, without Thee I cannot live!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी संत-काव्य और सूफी परंपरा के उस समन्वय का आदर्श रूप है जहाँ परमात्मा को 'महाराज' (महान राजा/प्रभु) के रूप में संबोधित किया गया है। विरहिणी आत्मा की स्थिति सूखे फूल जैसी है जो अपनी सुगंध खो चुका है। जब तक साहिब पास न हों, तब तक जीवन व्यर्थ है। बुल्ले शाह मनुष्य को मृत्यु की अकाट्यता की याद दिलाते हैं—'सिर मौत खलोती तेरे आण के'। अंत में जब प्रियतम लौटता है, तो साधक किसी उपहार या सांसारिक सुख की मांग नहीं करता, बल्कि अपना शीश ही उसके चरणों में न्योछावर कर देता है।"
    }
]

new_lexicon_terms = {
    "उल्हामें": {"hindi": "उलाहने, व्यंग्य, ताने, कुल की निंदा", "english": "reproach, taunts, censure of society"},
    "भांबड़": {"hindi": "प्रचंड अग्नि की ज्वाला, भभकता हुआ अलाव", "english": "blazing conflagration, roaring fire"},
    "जेहवा": {"hindi": "जिह्वा, जीभ, वाणी", "english": "tongue, speech, voice"},
    "सुक्ख मन्दर": {"hindi": "परमानंद का धाम, आंतरिक शांत अवस्था", "english": "the Temple of Peace, inner realm of unruffled bliss"},
    "तिलकन बाज़ी": {"hindi": "फिसलन भरी, धोखेबाज, मायावी", "english": "slippery, deceptive, treacherous terrain"},
    "चिनग": {"hindi": "चिंगारी, अग्नि-कण", "english": "spark of fire"},
    "मख़फ़ी": {"hindi": "गुप्त, रहस्यमयी, छिपा हुआ", "english": "hidden, concealed, esoteric (makhfi)"},
    "दुगाना": {"hindi": "दो रकअत की नमाज़; सूफी रूपक में: हृदय का नित्य प्रेम-सजदा", "english": "two-rak'ah prayer; in Sufi metaphor: continuous prayer of Love"},
    "अणघातां": {"hindi": "असमय, अलौकिक पहर, अचरज भरी वेला", "english": "untimely/unearthly hour, mysterious moment"},
    "बरलाई": {"hindi": "दीवानी, मतवाली, प्रेम-विह्वल", "english": "frenzied with love, rapturous, ecstatic"}
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
        "completed_count": 110,
        "total": 160,
        "next_kafi_id": 111,
        "last_updated": "2026-10-17T18:35:00+05:30",
        "last_batch": "106-110",
        "status": "in_progress",
        "milestone": "110/160 (68.75%) finished."
    }
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print(f"Checkpoint updated: 110/160 completed. Next ID: 111")

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
