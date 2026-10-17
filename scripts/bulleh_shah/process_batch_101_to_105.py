# -*- coding: utf-8 -*-
"""
Process Kafian 101 to 105 for Bulleh Shah Trilingual Edition.
Initiates Part 3 (भाग 3: काफ़ियां 101-160).
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
        "id": 101,
        "title": "मेरे क्युं चिर लाइआ माही",
        "title_english": "Why Has My Beloved Tarried So Long?",
        "historical_context": "यह 23 बंधों की एक विशाल, महाकाव्यात्मक और आख्यानात्मक सूफी काफी है। इसमें बुल्ले शाह ने हीर-रांझा की संपूर्ण गाथा को आध्यात्मिक रूपक बनाकर प्रस्तुत किया है। 'कुन-फयाकून' (सृष्टि की आदि-ध्वनि) से लेकर रांझा का तख्त हजारे से प्रस्थान, चूचक का चाक (ग्वाला) बनना, मुल्तान में बहाउद्दीन जकरिया से आशीर्वाद, खेड़ों का बारात लाना और जबरन निकाह, रांझा का टिल्ला गोरखनाथ जाकर कान छिदवाना और जोगी बनना, खेड़ों के गांव में भीख मांगते हुए खप्पर टूटना, सहती का रहस्य समझना और सर्पदंश के नाटक द्वारा हीर-रांझा का अंतिम मिलन—यह सब जीवात्मा की सांसारिक प्रताड़ना और अंततः ईश्वरीय मिलन की यात्रा को दर्शाता है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: मेरे क्युं चिर लाइआ माही)",
        "raga": "राग काफी / बिलावल",
        "theme": "हीर-रांझा का सम्पूर्ण सूफी आख्यान, विरह, जबरन निकाह, जोग-दीक्षा, सर्पदंश का रूपक, ईश्वरीय मिलन",
        "stanzas": [
            {
                "original": [
                    "मेरे क्युं चिर लाइआ माही ।  ",
                    "नी मैं उस तों घोल-घुमाई ।"
                ],
                "hindi_gloss": [
                    "मेरे (मेरे प्यारे) क्युं (क्यों इतनी) चिर (देर/विलंब) लाइआ (लगा दिया है) माही (माही/प्रियतम ने) ।",
                    "नी (हे सखी) मैं (मैं तो) उस (उस प्रियतम) तों (पर) घोल-घुमाई (सर्वस्व न्योछावर/बलिहारी जाती हूँ) ।"
                ],
                "english_gloss": [
                    "मेरे (my) क्युं (why) चिर लाइआ (has delayed so long) माही (Beloved herd-prince) ।",
                    "नी (O sister) मैं (I) उस तों (upon Him) घोल-घुमाई (am sacrificed wholly) ।"
                ],
                "poetic_hindi": [
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?",
                    "हे सखी, मैं तो उस प्यारे पर वारी-वारी जाऊँ सौ-सौ बार !"
                ],
                "poetic_english": [
                    "Why has my Beloved tarried so long, delaying His coming sweet?",
                    "O sisters, I offer my soul and life in surrender at His feet!"
                ]
            },
            {
                "original": [
                    "दरद फ़िराक बथेरा करिआ, इह दुक्ख मैथों जाए ना जरिआ,  ",
                    "टमक असाडे सिर ते धरिआ, डोई बुग़चा लोह कड़ाही ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "दरद (विरह की पीड़ा) फ़िराक (और वियोग) बथेरा (अत्यंत असह्य) करिआ (व्याकुल कर दिया है), इह (यह) दुक्ख (दुख) मैथों (मुझसे) जाए ना जरिआ (सहा नहीं जाता),",
                    "टमक (नगाड़ा) असाडे (हमारे) सिर (सिर) ते (पर) धरिआ (रख दिया गया है), डोई (करछुल) बुग़चा (पोटली) लोह (लोहे का तवा) कड़ाही (और कड़ाही साधु-सामग्री के रूप में लाद दी गई है) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "दरद फ़िराक (pain of separation) बथेरा करिआ (has overwhelmed me), इह दुक्ख (this sorrow) मैथों जाए ना जरिआ (cannot be borne by me),",
                    "टमक (kettledrum) असाडे सिर ते (upon our head) धरिआ (is laid), डोई (ladle) बुग़चा (pack) लोह कड़ाही (iron griddle and pan) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "विरह के दर्द ने मुझको घेरा, सहा न जाए अब दुख का फेरा,",
                    "सिर पे ढोल और कंधों पे कांसा, जोगी का सामान बखेरा !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "The pangs of separation pierce, too heavy is this grief to bear;",
                    "The drum is laid upon my head, a beggar's bundle and ironware!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "जागद्यां मैं घर विच मुट्ठी, कदी नहीं सां बैठी उट्ठी,  ",
                    "जिस दी सां मैं ओसे कुट्ठी, हुन की कर ल्या बेपरवाही ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "जागद्यां (जागते-जागते ही) मैं (मैं अपने) घर (घर) विच (में) मुट्ठी (लुट गई), कदी (कभी भी) नहीं (नहीं) सां (थी) बैठी (चैन से बैठी) उट्ठी (या उठी),",
                    "जिस (जिस प्रियतम) दी (की) सां (थी) मैं (मैं), ओसे (उसी ने मुझे प्रेम-खंजर से) कुट्ठी (ज़िब्ह/घायल कर दिया), हुन (अब उसने) की (कैसी) कर ल्या (कर ली है यह) बेपरवाही (उदासीनता/बेपरवाही) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "जागद्यां (while awake) मैं (I) घर विच (at home) मुट्ठी (was robbed), कदी नहीं (never) सां बैठी उट्ठी (could rest or rise in peace),",
                    "जिस दी (whose) सां मैं (I was) ओसे (by Him) कुट्ठी (slain/struck), हुन की (now what) कर ल्या (has assumed) बेपरवाही (heedless indifference) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "जागते-जागते घर में लूटी गई, चैन कभी न पाया मैंने,",
                    "जिसकी थी मैं, उसी ने घायल की, फिर क्यों मुखड़ा छुपाया उसने?",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "Robbed broad awake within my house, no rest in night or day I found;",
                    "Slain by the very One I loved, who leaves me now with mortal wound!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु तेरे तों वारी, मैं बलेहारी लक्ख लक्ख वारी,  ",
                    "तेरी सूरत बहुत प्यारी, मैं वे बिचारी घोल घुमाई ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ले शाह कहते हैं) शहु (हे प्रियतम स्वामी) तेरे (तेरे) तों (ऊपर से) वारी (मैं न्योछावर हूँ), मैं (मैं) बलेहारी (बलिहारी जाती हूँ) लक्ख (लाख) लक्ख (लाख) वारी (बार),",
                    "तेरी (तेरी यह अलौकिक) सूरत (छवि/सूरत) बहुत (अत्यंत) प्यारी (मनमोहिनी है), मैं (मैं) वे (तो) बिचारी (दीन-अकिंचन विरहिणी) घोल घुमाई (तुझ पर बलिहारी जाती हूँ) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा शहु (Bulleh's Lord) तेरे तों वारी (surrendered unto Thee), मैं बलेहारी (I sacrifice myself) लक्ख लक्ख वारी (myriad times),",
                    "तेरी सूरत (Thy visage) बहुत प्यारी (infinitely lovely), मैं वे बिचारी (poor helpless me) घोल घुमाई (wholly devoted) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "बुल्ला कहे: तुझ पर जाऊँ वारी, लाखों बार मैं बलिहारी,",
                    "तेरी सूरत मन को मोहे, न्योछावर यह दासी बेचारी !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "Bulleh proclaims: Unto Thee I bow, a million times I yield my heart;",
                    "Exceeding lovely is Thy face, from which I nevermore can part!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "मेरे माही दे पंज पीर पनाही, ढूंडन उस नूं विच लोकाई,  ",
                    "मेरे माही ते फ़ज़ल इलाही, जिस ने गैबों तार हिलाई ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "मेरे (मेरे) माही (माही के) दे (के) पंज (पाँचों सिद्ध) पीर (पीर) पनाही (रक्षक/आश्रयदाता हैं), ढूंडन (संसार के लोग ढूँढ रहे हैं) उस (उस प्रियतम) नूं (को) विच (भीतर) लोकाई (संसार में),",
                    "मेरे (मेरे) माही (माही) ते (पर है) फ़ज़ल (कृपा) इलाही (ईश्वरीय अनुग्रह), जिस (जिसने) ने (ने) गैबों (अदृश्य रहस्य-लोक से) तार (प्रेम की सूक्ष्म तार) हिलाई (झंकृत कर दी है) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "मेरे माही दे (unto my Beloved) पंज पीर (five Pirs) पनाही (are protector/shelter), ढूंडन उस नूं (people seek Him) विच लोकाई (among the multitude),",
                    "मेरे माही ते (upon my Beloved) फ़ज़ल इलाही (is Divine Grace), जिस ने (who) गैबों (from the Unseen) तार हिलाई (vibrated the mystical chord) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "पाँचों पीरों का साया माही पे, संसार उसे वन-उपवन ढूँढे,",
                    "रब का फज़ल हुआ है उस पर, जिसने गुप्त जगत की तारें छेड़े !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "The Holy Five Pirs shield my Love, though blind crowds seek Him far and wide;",
                    "Divine Compassion rests on Him, who moves the Unseen chords inside!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "कुन फ़ैकून आवाज़ा आया, तख़त हज़ार्युं रांझा धाइआ,  ",
                    "'चूचक' दा उस चाक सदाइआ, उह आहा साहब सफ़ाई ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "कुन (हो जा) फ़ैकून (और वह हो गया—सृष्टि की आदि-आवाज) आवाज़ा (दिव्य नाद) आया (गूँज उठा), तख़त हज़ार्युं (तख्त हजारे से) रांझा (रांझा/आत्मा का प्रियतम) धाइआ (दौड़ा चला आया),",
                    "'चूचक' ('चूचक' का) दा (का) उस (उसने स्वयं को) चाक (ग्वाला/सेवक) सदाइआ (कहलाया), उह (वह तो स्वयं) आहा (था) साहब (सच्चा स्वामी/बादशाह) सफ़ाई (पवित्रता और निर्मलता का) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "कुन फ़ैकून ('Be! And it was' - primordial command) आवाज़ा आया (the voice resounded), तख़त हज़ार्युं (from Takht Hazara) रांझा धाइआ (Ranjha hastened),",
                    "'चूचक' दा (of Chuchak) चाक सदाइआ (called Himself cowherd/servant), उह आहा (He indeed was) साहब सफ़ाई (the Sovereign Lord of purity) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "'कुन-फ़याकून' का नाद गुंजा जब, तख्त हजारे से रांझा आया,",
                    "चूचक का वो बना चरवाहा, जो साक्षात् मालिक कहलाया !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "When 'Kun Fayakun' the mandate spoke, from Takht Hazara Ranjha sped;",
                    "He served as Chuchak’s humble herd, though crown of kings adorned His head!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "चल्ल रांझा मुलतान चलाहें, गौश बहावल पीर मनावें,  ",
                    "आपनी तुरत मुराद ल्यावें, मेरा जी रब्ब मौला चाही ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "चल्ल (चल) रांझा (हे रांझा) मुलतान (मुल्तान की पावन भूमि पर) चलाहें (चलें), गौश (गौस-उल-आलम) बहावल (हज़रत बहाउद्दीन जकरिया) पीर (पीर को) मनावें (मनाएँ/प्रसन्न करें),",
                    "आपनी (अपनी) तुरत (शीघ्र ही) मुराद (मनोकामना/प्रेम-प्राप्ति) ल्यावें (लेकर आएं), मेरा (मेरा) जी (हृदय) रब्ब (परम प्रभु) मौला (मौला को ही) चाही (चाहता है) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "चल्ल रांझा (come Ranjha) मुलतान चलाहें (let us go to Multan), गौश बहावल पीर (Ghaus Bahawal Zakariya) मनावें (propitiate),",
                    "आपनी तुरत मुराद ल्यावें (fetch our cherished desire instantly), मेरा जी (my soul) रब्ब मौला चाही (longs for the Divine Master) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "चल मुल्तान चलें ऐ रांझा, पीर बहावल को मनाएँ,",
                    "शीघ्र पूरी हो मन की मुरादें, मौला का हम दरस पाएँ !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "Come, Ranjha, let us seek Multan, and Ghaus Bahawal's shrine entreat;",
                    "To win our fond desire at once, and lay our heart at Allah's feet!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "जित्थे इश्क डेरा घत बहन्दा, ओथे सबर करार ना रहन्दा,  ",
                    "कोई छुटकन ऐवें कहन्दा, गल पई प्रेम दी फाही ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "जित्थे (जहाँ) इश्क (इलाही इश्क) डेरा (अपना डेरा) घत (डालकर) बहन्दा (बैठ जाता है), ओथे (वहाँ) सबर (धैर्य) करार (और विश्राम) ना (नहीं) रहन्दा (रहता),",
                    "कोई (कोई अज्ञानी) छुटकन (छुटकारे की बात) ऐवें (व्यर्थ ही) कहन्दा (कहता है), गल (गले में जब) पई (पड़ चुकी हो) प्रेम (सच्चे प्रेम) दी (की) फाही (फांसी/बंधन) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "जित्थे (where) इश्क (Divine Love) डेरा घत बहन्दा (pitches its camp and sits), ओथे (there) सबर करार (patience and rest) ना रहन्दा (remain not),",
                    "कोई (anyone) छुटकन (of release) ऐवें कहन्दा (speaks in vain), गल पई (around neck is cast) प्रेम दी फाही (the holy noose of Love) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "जहाँ इश्क ने डेरा डाला, सब्र-करार न रह पाए,",
                    "छुटकारे की बात व्यर्थ है, गले में प्रेम की फाँसी आए !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "Where Love has pitched its fiery tent, all patience and contentment flee;",
                    "Vain is the talk of loose escape, when bound by Love’s sweet decree!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "आ जंञ खेड़िआं दी ढुकी, मैं हुन हीर निमानी मुक्की,  ",
                    "मेरी रत्त सरीरों सुक्की, वल वल मारे बिरहों खाई ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "आ (आकर) जंञ (खेड़ों की बारात) खेड़िआं (खेड़ों) दी (की) ढुकी (द्वार पर आ धमकी), मैं (मैं) हुन (अब) हीर (हीर) निमानी (दीन-दुखियारी) मुक्की (समाप्त/मृतप्राय हो गई),",
                    "मेरी (मेरा सारा) रत्त (रक्त) सरीरों (शरीर से) सुक्की (सूख गया), वल (बार-बार) वल (उमड़-उमड़कर) मारे (घायल करती है) बिरहों (विरह की) खाई (खाई/ज्वाला) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "आ जंञ खेड़िआं दी ढुकी (the wedding party of Kheras has arrived), मैं हुन (I now) हीर निमानी मुक्की (helpless Heer am ruined),",
                    "मेरी रत्त सरीरों सुक्की (blood dried up from my body), वल वल मारे (repeatedly strikes) बिरहों खाई (the trench of separation) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "खेड़ों की बारात आ पहुँची, दीन-दुखियारी हीर तो टूटी,",
                    "सूख गया तन-रक्त विरह में, आशा की हर डोरी छूटी !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "The Kheras' bridal cavalcade arrives; poor, helpless Heer is spent;",
                    "The blood has dried within my veins, in separation's torment bent!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "खेड़ा फुल्ल घोड़े ते चढ़आ, फक्कर धूड़ गरद विच रल्या,  ",
                    "एडा मान क्युं कूड़ा करिआ, उस कीती बेपरवाही ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "खेड़ा (सैदा खेड़ा) फुल्ल (अहंकार में फूला हुआ) घोड़े (घोड़े) ते (पर) चढ़आ (सवार हुआ), फक्कर (परंतु साधक/रांझा) धूड़ (धूल) गरद (और मिट्टी) विच (में) रल्या (रोल दिया गया),",
                    "एडा (इतना बड़ा) मान (अहंकार) क्युं (क्यों) कूड़ा (झूठा) करिआ (किया उसने), उस (उसने) कीती (दिखाई अपनी) बेपरवाही (उदासीनता) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "खेड़ा (the Khera groom) फुल्ल (puffed with pride) घोड़े ते चढ़आ (mounted the steed), फक्कर (the holy mendicant) धूड़ गरद विच रल्या (mingled in dust),",
                    "एडा मान (such vanity) क्युं कूड़ा करिआ (why did he boast falsely), उस कीती बेपरवाही (shewn utter heedlessness) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "खेड़ा घोड़े चढ़ इतराए, फकीर पड़ा मिट्टी में धूल,",
                    "झूठा घमंड क्यों पाला जग ने, भूला ईश्वर की वो मूल !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "Puffed up with pride, the Khera rode; the holy fakir trailed the dust;",
                    "Why harbor worldly vanity, in fleeting false illusions trust?",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "चढ़ के पीर खेड़िआं दा आया, उस ने केहा शोर मचाइआ,  ",
                    "मैनूं माही नज़र ना आया, तांहीएं कीती हाल दुहाई ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "चढ़ (सवार होकर) के (कर) पीर (पीर/पुरोहित) खेड़िआं (खेड़ों) दा (का) आया (आया), उस (उसने) ने (ने) केहा (कैसा प्रचंड) शोर (बखेड़ा) मचाइआ (मचाया),",
                    "मैनूं (मुझको) माही (मेरा माही) नज़र (दिखाई) ना (नहीं) आया (दिया), तांहीएं (तभी तो) कीती (मैंने की) हाल (अपनी आंतरिक पीड़ा की) दुहाई (आर्त पुकार) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "चढ़ के (mounted) पीर खेड़िआं दा आया (the Kheras' priest arrived), उस ने केहा शोर मचाइआ (what an uproar he raised),",
                    "मैनूं माही नज़र ना आया (my Beloved was not visible to me), तांहीएं कीती हाल दुहाई (hence I cried aloud in lamentation) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "खेड़ों का पुरोहित आया, शोर मचाया द्वारे पे,",
                    "माही मुझे नज़र न आया, चीख उठी मैं धारे पे !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "The Kheras' cleric rode in pomp, creating turmoil in the square;",
                    "My eyes saw not my Beloved Prince, and so I screamed in wild despair!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "मैं माही दी माही मेरा, गोशत पोसत बेरा-बेरा,  ",
                    "दिन हशर दे करसां झेड़ा, जद देसी दाद इलाही ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "मैं (मैं) माही (माही) दी (की हूँ) माही (और माही) मेरा (मेरा है), गोशत (मांस) पोसत (और खाल चाहे) बेरा-बेरा (टुकड़े-टुकड़े कर दिए जाएँ),",
                    "दिन (दिन) हशर (प्रलय/कयामत) दे (के) करसां (करूँगी मैं) झेड़ा (मुकदमा/न्याय की मांग), जद (जब) देसी (देगा) दाद (सच्चा न्याय) इलाही (परमेश्वर) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "मैं माही दी (I am my Beloved's) माही मेरा (my Beloved is mine), गोशत पोसत बेरा-बेरा (though flesh and skin be rent shred by shred),",
                    "दिन हशर दे (on Judgment Day) करसां झेड़ा (I shall contest this suit), जद देसी दाद इलाही (when God delivers justice supreme) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "मैं माही की, माही मेरा, चाहे तन का टुकड़ा हो,",
                    "रोज़-ए-हशर हिसाब करूँगी, जब रब का सच्चा न्याय हो !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "I am His own, and He is mine, though bone and flesh be torn apart;",
                    "On Judgment Day I'll plead my case when God gives justice to my heart!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "चूचक काज़ी सद बहाइआ, मैं मन रांझू माही भाइआ,  ",
                    "धक्को धक्क निकाह पढ़ाइआ, उस कीता फ़रज़ अदाई ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "चूचक (पिता चूचक ने) काज़ी (काजी को) सद (बुलाकर) बहाइआ (बिठा लिया), मैं (मेरे) मन (मन में तो) रांझू (रांझा) माही (माही ही) भाइआ (बसा हुआ था),",
                    "धक्को धक्क (बलपूर्वक/ज़बरदस्ती) निकाह (निकाह) पढ़ाइआ (पढ़वा दिया), उस (उस काजी ने केवल) कीता (किया अपना) फ़रज़ (धार्मिक कर्तव्य) अदाई (अदा करने का ढोंग) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "चूचक काज़ी सद बहाइआ (Chuchak summoned and seated the Qazi), मैं मन (in my heart) रांझू माही भाइआ (Ranjha my Love was cherished),",
                    "धक्को धक्क (by sheer force) निकाह पढ़ाइआ (forced the marriage vows), उस कीता फ़रज़ अदाई (he merely fulfilled his ritual duty) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "चूचक ने काजी बुलवाया, मन में रांझा माही बसा,",
                    "धक्के से निकाह पढ़वाया, रूढ़ि का पाखंड रचा !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "My father called the Qazi stern, though Ranjha dwelt within my breast;",
                    "By force they sealed the wedding rites, fulfilling custom's cold behest!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "तेल वटना कंधे मल्या, चोया चन्दन मत्थे रल्या,  ",
                    "माही मेरा बेले वड़िआ, मैं की करनी कंङन बाही ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "तेल (तेल) वटना (और उबटन) कंधे (कंधों पर) मल्या (मला गया), चोया (इत्र/अर्क) चन्दन (और चंदन) मत्थे (माथे पर) रल्या (लगाया गया),",
                    "माही (परंतु मेरा माही) मेरा (मेरा) बेले (जंगल/बीहड़ में) वड़िआ (चला गया), मैं (मैंने) की (क्या) करनी (करना है यह विवाह का) कंङन (कंगन) बाही (अपनी बाँहों में पहनकर) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "तेल वटना कंधे मल्या (scented oil and turmeric smeared on shoulders), चोया चन्दन मत्थे रल्या (sandalwood and essence on forehead),",
                    "माही मेरा बेले वड़िआ (my Beloved wandered into the wilderness), मैं की करनी कंङन बाही (what use have I for bridal bangles on arms) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "उबटन और तेल मला कंधों पे, माथे पे चंदन छिड़क दिया,",
                    "माही मेरा बीहड़ में भटके, कंगन बाँहों में क्या करूँ पिया?",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "With turmeric they anointed me, with sandalwood they washed my brow;",
                    "My Love was driven to the wilds—what use are bridal bangles now?",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "होर सभ्भो कुझ दस्सन करिआ, इह दुक्ख जाए ना मैथों जरिआ,  ",
                    "टमक रांझन दे सिर ते धरिआ, मोढे बुग़चा लोह कड़ाही ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "होर (और) सभ्भो (सब) कुझ (कुछ) दस्सन (कहने/व्यक्त करने का यत्न) करिआ (किया), इह (यह) दुक्ख (दुख) जाए ना मैथों जरिआ (मुझसे सहन नहीं होता),",
                    "टमक (नगाड़ा) रांझन (रांझा) दे (के) सिर (सिर) ते (पर) धरिआ (रखा गया), मोढे (कंधे पर) बुग़चा (पोटली) लोह कड़ाही (और लोहे का तवा-कड़ाही) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "होर सभ्भो कुझ दस्सन करिआ (I tried to recount all else), इह दुक्ख जाए ना मैथों जरिआ (this pain cannot be endured),",
                    "टमक रांझन दे सिर ते धरिआ (the drum was placed on Ranjha's head), मोढे बुग़चा लोह कड़ाही (pack and pan upon his shoulder) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "हाल-ए-दिल सब कह डाला, पर यह विरह सहा न जाए,",
                    "रांझा के सिर ढोल धरा, कंधों पे पोटली लटकाए !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "I tell the world of all my plight, but this deep grief defies my song;",
                    "The drum was placed on Ranjha’s head, while with His load He trudged along!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "टमक सुट्ट टिल्ले वल जावे, बैठा उस दा नाम ध्यावे,  ",
                    "कन्न पड़वा के मुन्दरां पावे, गुड़ लै के दो सेर शाही ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "टमक (नगाड़े को) सुट्ट (फेंककर) टिल्ले (गुरु गोरखनाथ के टिल्ले की) वल (ओर) जावे (जाता है), बैठा (वहाँ बैठकर) उस (परमात्मा/हीर) दा (का) नाम (नाम) ध्यावे (ध्याता है),",
                    "कन्न (कान) पड़वा (छिड़वा) के (करके) मुन्दरां (जोग की मुंद्राएं) पावे (पहनता है), गुड़ (गुड़) लै (ले) के (करके) दो (दो) सेर (सेर) शाही (शाही नाप का गुरु-भेंट) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "टमक सुट्ट (casting away the drum) टिल्ले वल जावे (heads towards the Tilla), बैठा उस दा नाम ध्यावे (sitting there meditates upon His Name),",
                    "कन्न पड़वा के मुन्दरां पावे (has ears pierced to wear yogic rings), गुड़ लै के दो सेर शाही (offering two royal seers of brown sugar) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "ढोल फेंक टिल्ले की ओर चला, जोगी बन कर नाम ध्याए,",
                    "दो सेर शाही गुड़ चढ़ाकर, कानों में मुंद्राएं सजाए !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "He cast the drum and sought the Mount, in meditation deep and still;",
                    "With royal sugar brought as gift, He pierced His ears upon the Hill!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "गुर गोरख नूं पीर मनावे, हीरे हीरे कर कुरलावे,  ",
                    "जिस दे कारन मूंड मुंडावे, उह मूंह पीला ज़रद मलाही ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "गुर (गुरु) गोरख (गोरखनाथ) नूं (को) पीर (अपना सिद्ध गुरु) मनावे (स्वीकार करता है), हीरे (हीर) हीरे (हीर) कर (कह-कह कर) कुरलावे (विलाप करता है),",
                    "जिस (जिस हीर) दे (के) कारन (कारण उसने अपना) मूंड (सिर) मुंडावे (मुंडवाया है), उह (उसका) मूंह (मुख) पीला (पीला) ज़रद (और कांतिहीन) मलाही (हो गया है) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "गुर गोरख नूं पीर मनावे (venerates Guru Gorakh as Master), हीरे हीरे कर कुरलावे (cries 'Heer! Heer!' in agony),",
                    "जिस दे कारन मूंड मुंडावे (for whose sake He shaved His head), उह मूंह पीला ज़रद मलाही (visage pale, ashen, and wan) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "गुरु गोरख को पीर बनाया, 'हीर-हीर' कह कर रोया,",
                    "जिसकी खातिर शीश मुंडाया, पीला मुखड़ा आँसू धोया !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "He took Guru Gorakh for His Guide, crying 'O Heer!' in grief and pain;",
                    "For her He shaved His head complete, His pallid visage washed with rain!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "जोगी जोग सिधारन आया, सिर दाढ़ी मूंह मोन मुनाइआ,  ",
                    "इस ते भगवा भेस वटाइआ, काली सेहली गल विच पाई ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "जोगी (वह जोगी) जोग (जोग-साधना को) सिधारन (सिद्ध करने) आया (आया), सिर (सिर) दाढ़ी (दाढ़ी) मूंह (और मूँछों को) मोन मुनाइआ (मुंडवा लिया),",
                    "इस (इस रूप) ते (पर) भगवा (गेरुआ) भेस (वस्त्र) वटाइआ (धारण किया), काली (काले ऊन की) सेहली (पवित्र माला/सेहली) गल (गले) विच (में) पाई (पहन ली) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "जोगी जोग सिधारन आया (the Yogi came having accomplished Yoga), सिर दाढ़ी मूंह मोन मुनाइआ (shaved head, beard, and mustache),",
                    "भगवा भेस वटाइआ (donned ochre robes), काली सेहली गल विच पाई (draped the black woolen cord around neck) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "जोग साध कर जोगी आया, सिर-दाढ़ी सब मुंडवाई,",
                    "पहने भगवे वस्त्र बदन पे, काली सेहली गले सजाई !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "Accomplished in the yogic path, with clean-shorn head and beard He trod;",
                    "In saffron robes and sable cord, an emissary of His God!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "जोगी शहर खेड़िआं दे आवे, जिस घर मतलब से घर पावे,  ",
                    "बूहे जा के नाद बजावे, आपे होया फ़ज़ल इलाही ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "जोगी (जोगी) शहर (गांव) खेड़िआं (खेड़ों) दे (के) आवे (पहुँचता है), जिस (जिस) घर (घर से उसका) मतलब (आध्यात्मिक प्रयोजन था) से (उसी) घर (घर को) पावे (ढूँढ लेता है),",
                    "बूहे (उसके द्वार पर) जा (जा) के (कर) नाद (शंख/जोगी-नाद) बजावे (बजाता है), आपे (स्वतः ही) होया (हो गया) फ़ज़ल (कृपा) इलाही (ईश्वर की) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "जोगी शहर खेड़िआं दे आवे (the Yogi arrives at the Kheras' town), जिस घर मतलब से घर पावे (finds the exact home He sought),",
                    "बूहे जा के नाद बजावे (sounds the yogic horn at the door), आपे होया फ़ज़ल इलाही (Divine Grace spontaneously manifested) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "खेड़ों के गाँव में जोगी आया, हीर का आँगन ढूँढ निकाला,",
                    "द्वारे पे जा नाद बजाया, रब का फज़ल हुआ मतवाला !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "The Yogi reached the Kheras' town, and found the portal of His quest;",
                    "He blew His horn before her door, with heavenly benediction blessed!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "बूहे पे खुड़ब्यां धङाणे, टुट्ट प्या खप्पर डुल्ल्ह पे दाणे,  ",
                    "इस दे वल छल कौन पछाणे, चीना रुल्ल गया विच पाही ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "बूहे (द्वार पर) पे (पड़े) खुड़ब्यां (झगड़े/धक्का-मुक्की) धङाणे (और उपद्रव में), टुट्ट (टूट) प्या (गया) खप्पर (जोगी का भिक्षापात्र/खप्पर) डुल्ल्ह (बिखर) पे (गए) दाणे (अन्न के दाने),",
                    "इस (इस जोगी) दे (की) वल छल (लीला/गूढ़ चालों को) कौन (कौन) पछाणे (पहचान सकता है), चीना (बाजरे/चीने के दाने) रुल्ल (बिखर) गया (गए) विच (में) पाही (धूल-कीचड़ के) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "बूहे पे (at the door) खुड़ब्यां धङाणे (in the commotion and scuffle), टुट्ट प्या खप्पर (the earthen begging bowl broke) डुल्ल्ह पे दाणे (grains spilled out),",
                    "इस दे वल छल कौन पछाणे (who can unravel His mystic guiles), चीना रुल्ल गया विच पाही (millet grains mingled with the dust) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "द्वारे पर धक्का-मुक्की में खप्पर टूटा, दाने बिखरे,",
                    "इस जोगी की लीला कौन जाने, धूल में मोती जैसे निखरे !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "Amidst the brawl before the gate, the begging-bowl in shards did break;",
                    "The grains rolled down into the dust—what artifice for True Love’s sake!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "चीना चुन चुन झोली पावे, बैठा हीरे तरफ़ तकावे,  ",
                    "जो कुझ लिख्या लेख सो पावे, रो रो लड़दे नैन सिपाही ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "चीना (बाजरे के दाने) चुन (चुन-) चुन (चुन कर) झोली (अपनी झोली में) पावे (डालता है), बैठा (बैठकर) हीरे (हीर की) तरफ़ (ओर) तकावे (प्रेम-दृष्टि से निहारता है),",
                    "जो (जो) कुझ (कुछ) लिख्या (लिखा है) लेख (प्रारब्ध में) सो (वही) पावे (पाता है मनुष्य), रो (रो-) रो (रोकर) लड़दे (लड़ रहे हैं प्रेम-युद्ध) नैन (नेत्र रूपी) सिपाही (सैनिक) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "चीना चुन चुन झोली पावे (picking grains one by one into the scrip), बैठा हीरे तरफ़ तकावे (sitting there gazes upon Heer),",
                    "जो कुझ लिख्या लेख सो पावे (one receives what destiny has inscribed), रो रो लड़दे नैन सिपाही (weeping, the soldier eyes wage battle) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "दाने चुन-चुन झोली डाले, हीर की ओर आँखें गड़ाए,",
                    "जो लिखा किस्मत में वही हो, रो-रो नैन सिपाही भिड़ाए !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "He gathers grains into His sack, yet keeps His gaze on Heer intent;",
                    "What destiny wrote must be fulfilled; the weeping eyes in combat bent!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "इह गल्ल सहती ननद पछाती, दोहां दी वेदन इक्को जाती,  ",
                    "उह वी आही सी मदमाती, ओथे दोहवां सत्थर पाही ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "इह (यह) गल्ल (गूढ़ बात) सहती (ननद सहती ने) ननद (ननद) पछाती (पहचान ली), दोहां (दोनों प्रेमियों) दी (की) वेदन (पीड़ा) इक्को (एक जैसी ही) जाती (जानी/समझी),",
                    "उह (वह सहती) वी (भी मुराद बलोच के प्रेम में) आही (थी) सी (थी) मदमाती (मतवाली), ओथे (वहाँ) दोहवां (दोनों ने मिलकर प्रेम की) सत्थर (योजना/सेज) पाही (बनाई) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "इह गल्ल (this secret) सहती ननद पछाती (sister-in-law Sehti recognized), दोहां दी वेदन इक्को जाती (knew their pangs were one and the same),",
                    "उह वी आही सी मदमाती (she too was intoxicated with love), ओथे दोहवां सत्थर पाही (there both aligned in secret concord) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "ननद सहती ने भेद पहचाना, दोनों की विरह-व्यथा को जाना,",
                    "वो भी थी प्रेम-दीवानी, दोनों ने मिलकर जाल ताना !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "The sister Sehti guessed the truth, and felt their sorrow as her own;",
                    "Enamored of love herself, she forged a covenant with them alone!",
                    "Why has my Beloved tarried so long, delaying His coming sweet?"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा सहती फन्द चलाइआ, हीर सलेटी नाग लड़ाइआ,  ",
                    "जोगी मंतर झाड़न आया, दुहां दी आस मुराद पुचाई ।  ",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ले शाह कहते हैं) सहती (सहती ने) फन्द (युक्ति/छल का उपाय) चलाइआ (चलाया), हीर (हीर) सलेटी (सलेटी को) नाग (नाग) लड़ाइआ (डसने का बहाना रचा),",
                    "जोगी (जोगी रांझा) मंतर (विष-निवारक मंत्र) झाड़न (फूंकने) आया (आया), दुहां (और दोनों प्रेमियों) दी (की) आस (आशा) मुराद (और मनोकामना) पुचाई (ईश्वर ने पूरी कर दी) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh) सहती फन्द चलाइआ (Sehti set the stratagem into motion), हीर सलेटी नाग लड़ाइआ (a snakebite was staged upon Heer),",
                    "जोगी मंतर झाड़न आया (the Yogi came to chant the healing charm), दुहां दी आस मुराद पुचाई (fulfilled the cherished desire of both) ।",
                    "मेरे क्युं चिर लाइआ माही ।"
                ],
                "poetic_hindi": [
                    "सहती ने रची युक्ति भारी, हीर को नाग डसने का स्वाँग रचाया,",
                    "झाड़-फूँक करने जोगी पहुँचा, रब ने दोनों का मिलन कराया !",
                    "सच्चा प्रेम अमर हुआ जग में, दूर हुआ विरह का वार,",
                    "मेरे माही ने क्यों इतनी देर लगाई, धन्य हुआ मेरा दीदार !"
                ],
                "poetic_english": [
                    "Says Bulleh: Sehti wrought the plot, a serpent’s sting on Heer was staged;",
                    "The Yogi came with healing spells, and their long agony assuaged!",
                    "Their deepest yearning was fulfilled, the lovers flew forever free:",
                    "Why did my Prince tarry so long to crown my soul with ecstasy?"
                ]
            }
        ],
        "sufi_commentary": "यह 23 बंधों की काफी बुल्ले शाह के काव्य का एक अद्वितीय महाकाव्यात्मक आख्यान है। इसमें वारिस शाह से पूर्व ही हीर-रांझा की लोकगाथा को एक संपूर्ण सूफी साधना-प्रक्रिया के रूप में ढाला गया है। 'कुन-फयाकून' से आरंभ होना यह सिद्ध करता है कि आत्मा और परमात्मा का संबंध अनादि है। रांझा का चूचक का चाक (सेवक) बनना ईश्वर की विनम्रता और प्रेम की खातिर अवतार लेने का प्रतीक है। खेड़ों द्वारा जबरन विवाह सांसारिक मोह-माया और नफ़्स के बंधनों का रूपक है। टिल्ला गोरखनाथ पर कान छिदवाकर जोग लेना सांसारिक मान-मर्यादा के पूर्ण त्याग (फना) को दर्शाता है। खप्पर का टूटना अहंकार के ठीकरे का फूटना है, और अंत में सर्पदंश का स्वाँग सांसारिक समाज को चकमा देकर आध्यात्मिक मुक्ति (बका) की ओर पलायन का प्रतीक है।"
    },
    {
        "id": 102,
        "title": "मेरे माही क्युं चिर लाइआ ए",
        "title_english": "Why Has My Beloved Tarried So Long, O Sisters?",
        "historical_context": "यह 5 बंधों की अत्यंत प्रभावशाली और रहस्यवादी काफी है। विरहिणी आत्मा अपने प्रियतम के विरह में संसार के ताने-बाने और उपहास सहते हुए मंसूर हल्लाज की भांति 'तहकीक' (सत्य का साक्षात्कार) का प्याला पीती है। इसमें मेअराज, कुएं से वुजू करना, इश्क के मुल्ला की अजान और दिल के मेहराब में सजदा करने जैसे अनूठे सूफी रूपक प्रयुक्त हुए हैं। अंत में सद्गुरु शाह इनायत कादरी का दीदार ही विरह का अंतिम समाधान बनता है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: मेरे माही क्युं चिर लाइआ ए)",
        "raga": "राग काफी / आसावरी",
        "theme": "मंसूर हल्लाज का जाम, आंतरिक नमाज़ (मेहराब), शाह इनायत का दीदार, विरह और विसाल",
        "stanzas": [
            {
                "original": [
                    "कह बुल्ल्हा हुन प्रेम कहाणी, जिस तन लागे सो तन जाणे,  ",
                    "अन्दर झिड़कां बाहर ताअने, नेहुं ला इह सुक्ख पाइआ ए ।  ",
                    "मेरे माही क्युं चिर लाइआ ए ।"
                ],
                "hindi_gloss": [
                    "कह (कहता है) बुल्ल्हा (बुल्ले शाह) हुन (अब) प्रेम (इलाही प्रेम की) कहाणी (कथा), जिस (जिस) तन (शरीर/मन को यह चोट) लागे (लगती है) सो (वही) तन (अंतःकरण) जाणे (इसके रहस्य को जानता है),",
                    "अन्दर (घर के भीतर परिजनों की) झिड़कां (झिड़कियां हैं) बाहर (और बाहर समाज के) ताअने (कड़वे ताने), नेहुं (प्रीत) ला (लगाकर) इह (यह ऐसा अनोखा) सुक्ख (सुख) पाइआ (पाया है मैंने) ए (रे) ।",
                    "मेरे (मेरे प्यारे) माही (माही ने) क्युं (क्यों इतनी) चिर (देर) लाइआ (लगा दी) ए (है) ।"
                ],
                "english_gloss": [
                    "कह बुल्ल्हा (says Bulleh) हुन प्रेम कहाणी (now the tale of Love), जिस तन लागे (the body that is pierced) सो तन जाणे (that body alone knows),",
                    "अन्दर झिड़कां (scoldings within) बाहर ताअने (taunts without), नेहुं ला (binding love) इह सुक्ख पाइआ ए (such strange 'peace' have I obtained) ।",
                    "मेरे माही क्युं चिर लाइआ ए (why has my Beloved tarried so long) ।"
                ],
                "poetic_hindi": [
                    "बुल्ला कहे प्रेम की बतियाँ: जिस तन लागे वही तन जाने,",
                    "अंदर परिजनों की झिड़कें, बाहर जग के तीखे ताने !",
                    "प्रीत लगा कर ऐसा सुख पाया, दिन-रैन विरह ने सताया,",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "Says Bulleh, hear the tale of Love: only the wounded knows the smart;",
                    "Rebukes at home and taunts abroad are all that soothe my aching heart!",
                    "Is this the wondrous peace I bought, pledging my love to One so sweet?",
                    "Why has my Beloved tarried so long, delaying His coming to meet?"
                ]
            },
            {
                "original": [
                    "नैणां कार रोवन दी पकड़ी, इक मरना दो जग्ग दी फकड़ी,  ",
                    "ब्रेहों जिन्द अवल्ली जकड़ी, नी मैं रो रो हाल वंजाइआ ए ।  ",
                    "मेरे माही क्युं चिर लाइआ ए ।"
                ],
                "hindi_gloss": [
                    "नैणां (नेत्रों ने केवल) कार (काम) रोवन (रोते रहने) दी (का ही) पकड़ी (पकड़ लिया है), इक (एक ओर विरह में तिल-तिल) मरना (मरना है) दो (दूसरी ओर) जग्ग (संसार भर) दी (की) फकड़ी (जिल्लत/अपयश सहना),",
                    "ब्रेहों (इस दारुण विरह ने) जिन्द (मेरे प्राणों को) अवल्ली (विचित्र रूप से) जकड़ी (जकड़ लिया है), नी (हे सखी) मैं (मैंने) रो (रो-) रो (रोकर अपना) हाल (हाल-ए-दिल) वंजाइआ (बर्बाद कर लिया) ए (है) ।",
                    "मेरे (मेरे) माही (माही ने) क्युं (क्यों इतनी) चिर (देर) लाइआ (लगा दी) ए (है) ।"
                ],
                "english_gloss": [
                    "नैणां (eyes) कार रोवन दी पकड़ी (have taken up the sole vocation of weeping), इक मरना (on one hand is dying) दो जग्ग दी फकड़ी (on the other, worldly disgrace),",
                    "ब्रेहों (separation) जिन्द अवल्ली जकड़ी (has strangely ensnared my soul), नी मैं रो रो (O weeping and weeping) हाल वंजाइआ ए (have ruined my state) ।",
                    "मेरे माही क्युं चिर लाइआ ए (why has my Beloved delayed so long) ।"
                ],
                "poetic_hindi": [
                    "अंखियों ने बस रोना सीखा, इक तिल-तिल मरना, दूजी रुसवाई,",
                    "अनोखे विरह ने जकड़ी काया, रो-रो अपनी सुध बिसराई !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "My eyes have made weeping their sole trade; on one side death, on the other shame;",
                    "Cruel separation has bound my breath, leaving me ruined in Love’s flame!",
                    "Why has my Beloved tarried so long, delaying His coming to meet?"
                ]
            },
            {
                "original": [
                    "मैं प्याला तहकीक लीता ए जो भर के मनसूर पीता ए,  ",
                    "दीदार मिअराज पिया लीता ए मैं खूह थीं वुज़ू सजाया ए ।  ",
                    "मेरे माही क्युं चिर लाइआ ए ।"
                ],
                "hindi_gloss": [
                    "मैं (मैंने) प्याला (वह प्याला) तहकीक (परम सत्य/तहकीक का) लीता (हाथ में थाम लिया) ए (है) जो (जिसे) भर (भर-भर) के (कर) मनसूर (मंसूर हल्लाज ने सूली चढ़ने से पहले) पीता (पिया था),",
                    "दीदार (प्रियतम का साक्षात दीदार ही) मिअराज (मेरी मेअराज/आकाशीय आरोहण) पिया (प्रियतम के साथ) लीता (अनुभव किया) ए (है), मैं (मैंने अपने अंतःकरण के) खूह (प्रेम-कुएं) थीं (के जल से) वुज़ू (पवित्र वुज़ू) सजाया (कर लिया) ए (है) ।",
                    "मेरे (मेरे) माही (माही ने) क्युं (क्यों इतनी) चिर (देर) लाइआ (लगा दी) ए (है) ।"
                ],
                "english_gloss": [
                    "मैं प्याला तहकीक लीता ए (I have accepted the chalice of divine Truth), जो भर के मनसूर पीता ए (which Mansur Hallaj drank brimful),",
                    "दीदार मिअराज पिया लीता ए (beholding the Beloved's face was my heavenly Mi'raj), मैं खूह थीं वुज़ू सजाया ए (I performed ablution from the inner well of tears) ।",
                    "मेरे माही क्युं चिर लाइआ ए (why has my Beloved delayed so long) ।"
                ],
                "poetic_hindi": [
                    "सत्य का वो प्याला मैंने पिया, जो भर-भर मंसूर ने पिया था,",
                    "दीदार-ए-यार ही मेअराज हुआ, कुएं के नीर से वुज़ू किया था !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "I took the cup of verified Truth that Mansur drank brimful on the tree;",
                    "Gazing on Him was my Mi'raj; from the deep well I made ablution free!",
                    "Why has my Beloved tarried so long, delaying His coming to meet?"
                ]
            },
            {
                "original": [
                    "इश्क मुल्लां ने बांग दिवाई, शहु आवन दी गल्ल सुणाई,  ",
                    "कर नीयत सजदे वल्ल धाई, नी मैं मूंह महराब लगाया ए ।  ",
                    "मेरे माही क्युं चिर लाइआ ए ।"
                ],
                "hindi_gloss": [
                    "इश्क (प्रेम रूपी) मुल्लां (सच्चे मुल्ला) ने (ने अंतःकरण में) बांग (अजान) दिवाई (दिलाई है), शहु (परमेश्वर/मुर्शिद के) आवन (आगमन) दी (का) गल्ल (संदेश) सुणाई (सुनाया है),",
                    "कर (सच्ची) नीयत (नीयत बांधकर) सजदे (साष्टांग दंडवत) वल्ल (की ओर) धाई (दौड़ पड़ी हूँ), नी (अरी सखी) मैं (मैंने अपना) मूंह (मुख) महराब (प्रियतम के दीदार रूपी मेहराब में) लगाया (लगा दिया) ए (है) ।",
                    "मेरे (मेरे) माही (माही ने) क्युं (क्यों इतनी) चिर (देर) लाइआ (लगा दी) ए (है) ।"
                ],
                "english_gloss": [
                    "इश्क मुल्लां ने बांग दिवाई (Love's inner Muezzin raised the call), शहु आवन दी गल्ल सुणाई (proclaimed the tidings of the Sovereign's arrival),",
                    "कर नीयत (forming true intention) सजदे वल्ल धाई (hastened towards prostration), नी मैं मूंह महराब लगाया ए (I placed my face within Love's archway/mihrab) ।",
                    "मेरे माही क्युं चिर लाइआ ए (why has my Beloved delayed so long) ।"
                ],
                "poetic_hindi": [
                    "इश्क-मुल्ला ने अज़ान दी जब, प्रियतम के आने की बात सुनाई,",
                    "नीयत बाँध सजदे में गिरी, दिल के मेहराब में लौ लगाई !",
                    "मेरे माही ने क्यों इतनी देर लगाई, क्यों न आया मेरा यार?"
                ],
                "poetic_english": [
                    "Love’s Muezzin cried the holy call, announcing that the King draws near;",
                    "I bent in prayer with vowed intent, and kissed the mihrab of my Dear!",
                    "Why has my Beloved tarried so long, delaying His coming to meet?"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु घर लपट लगाईं, रसते में सभ बण तण जाईं,  ",
                    "मैं वेखां आ इनायत साईं, इस मैनूं शहु मिलाइआ ए ।  ",
                    "मेरे माही क्युं चिर लाइआ ए ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ले शाह कहते हैं) शहु (प्रियतम के) घर (द्वार पर प्रेम की) लपट (सुगंधित ज्योति) लगाईं (जला रखी है), रसते (उसके मार्ग) में (में) सभ (सब दिशाओं में) बण (सँवर) तण (सजकर) जाईं (जाती हूँ),",
                    "मैं (मैं) वेखां (देख रही हूँ) आ (आकर साक्षात्) इनायत (हज़रत शाह इनायत) साईं (सद्गुरु को), इस (इन्हीं मुर्शिद ने) मैनूं (मुझको) शहु (परमेश्वर से) मिलाइआ (मिला दिया) ए (है) ।",
                    "मेरे (मेरे) माही (माही ने) क्युं (क्यों इतनी) चिर (देर) लाइआ (लगा दी) ए (है) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा शहु घर लपट लगाईं (Bulleh kindled the fragrant lamp at the Lord's house), रसते में (on the path) सभ बण तण जाईं (adorned myself in all beauty),",
                    "मैं वेखां (I behold) आ इनायत साईं (Master Inayat Shah arriving), इस मैनूं शहु मिलाइआ ए (He has united me with the Sovereign Lord) ।",
                    "मेरे माही क्युं चिर लाइआ ए (why has my Beloved delayed so long) ।"
                ],
                "poetic_hindi": [
                    "साहिब के घर प्रेम-दीप जलाया, सज-धज कर राहों में बैठी,",
                    "शाह इनायत सदगुरु आए, जिनसे मेरे प्रियतम की सेज सजी !",
                    "सच्चे मुर्शिद ने पार लगाया, मिटा विरह का भारी भार,",
                    "मेरे माही ने क्यों इतनी देर लगाई, धन्य हुआ मेरा दीदार !"
                ],
                "poetic_english": [
                    "Bulleh lit candles in Love’s shrine, decked in bridal robes so fine;",
                    "Lo! Shah Inayat came at last, and merged my soul in the Divine!",
                    "Why did my Prince tarry so long, to crown my life with bliss complete?"
                ]
            }
        ],
        "sufi_commentary": "यह काफी सूफी इस्लाम के उच्चतम रहस्यों को उजागर करती है। 'प्याला तहकीक' का उल्लेख सीधे मंसूर हल्लाज के उस आध्यात्मिक अनुभव की ओर संकेत करता है जहां 'अनलहक' (मैं ही सत्य हूँ) की घोषणा करने पर उसे फांसी दी गई थी। बुल्ला कहते हैं कि वास्तविक मेअराज मस्जिद या अर्श पर जाना नहीं, बल्कि प्रियतम का साक्षात दीदार है। नमाज़ के बाह्य कर्मकांडों के स्थान पर वे 'इश्क के मुल्ला' की अजान और अपने हृदय को ही 'मेहराब' (वह स्थान जहाँ नमाज़ का इमाम झुकता है) बनाकर सजदा करते हैं। अंत में हज़रत शाह इनायत कादरी का आगमन यह सिद्ध करता है कि पूर्ण सद्गुरु की कृपा के बिना जीवात्मा का परमात्मा से मिलन असंभव है।"
    },
    {
        "id": 103,
        "title": "मेरे नौशहु दा कित मोल",
        "title_english": "What Can Measure the Worth of My Divine Bridegroom?",
        "historical_context": "यह 3 बंधों की एक अत्यंत गंभीर, दार्शनिक और व्यंग्यात्मक काफी है। 'नौशहु' का अर्थ है नया दूल्हा अर्थात् परमात्मा। बुल्ले शाह पूछते हैं कि उस अलौकिक प्रियतम का कोई क्या मूल्य आंक सकता है? संसार की विडंबना यह है कि झूठे और पाखंडी लोग मौज-मस्ती ('कलोल') करते हैं जबकि सच्चे साधकों को जूतियां ('पौले') खानी पड़ती हैं। ग्रंथों और किताबों को खंगालने पर भी उस पारमार्थिक रहस्य की थाह नहीं मिलती। ऐसे अंधे समाज में जब कोई ज्ञानी सच बोलता है तो उसे सुनने वाला कोई नहीं होता।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: मेरे नौशहु दा कित मोल)",
        "raga": "राग काफी / बिलावल",
        "theme": "परमात्मा की अमूल्यता (नौशहु), सांसारिक पाखंड पर व्यंग्य, सत्य की दुर्दशा, मौन साधना",
        "stanzas": [
            {
                "original": [
                    "मेरे नौशहु दा कित मोल ।  ",
                    "मेरे नौशहु दा कित मोल ।"
                ],
                "hindi_gloss": [
                    "मेरे (मेरे अलौकिक) नौशहु (नवल दूल्हे/परमात्मा) दा (का) कित (कितना/क्या) मोल (मूल्य कोई आंक सकता है) ।",
                    "मेरे (मेरे प्यारे) नौशहु (प्रियतम दूल्हे) दा (का) कित (क्या) मोल (मूल्य हो सकता है) ।"
                ],
                "english_gloss": [
                    "मेरे नौशहु दा (of my Divine Bridegroom) कित मोल (what price / what measure of worth) ।",
                    "मेरे नौशहु दा कित मोल (what can ever match the worth of my heavenly King) ।"
                ],
                "poetic_hindi": [
                    "मेरे नवल-दूल्हे का क्या कोई मोल लगा सकता है?",
                    "उस अनमोल प्रीतम की महिमा कौन गा सकता है?"
                ],
                "poetic_english": [
                    "What price could ever buy my radiant Groom?",
                    "What earthly wealth could match His cosmic bloom?"
                ]
            },
            {
                "original": [
                    "अगले वल्ल दी खबर ना कोई रही किताबां फोल ।  ",
                    "सच्चियां नूं पए वज्जन पौले झूठियां करन कलोल ।"
                ],
                "hindi_gloss": [
                    "अगले (उस पारलौकिक/ईश्वरीय) वल्ल (लोक) दी (की) खबर (सुध/ज्ञान) ना (नहीं) कोई (किसी को भी), रही (मैं रह गई व्यर्थ ही) किताबां (धार्मिक पोथियों को) फोल (खंगाल-खंगाल कर),",
                    "सच्चियां (सच्चे प्रेमियों) नूं (को तो) पए (पड़ रहे हैं) वज्जन (लगने) पौले (जूते/अपमान), झूठियां (और झूठे पाखंडी लोग) करन (कर रहे हैं मौज-) कलोल (कलोल/आनंद-विलास) ।"
                ],
                "english_gloss": [
                    "अगले वल्ल दी (of the world beyond) खबर ना कोई (no news remains), रही किताबां फोल (leafing endlessly through scriptures),",
                    "सच्चियां नूं (unto the truthful ones) पए वज्जन पौले (shoes/blows rain upon their heads), झूठियां (the hypocrites and liars) करन कलोल (revel in merry pleasures) ।"
                ],
                "poetic_hindi": [
                    "पोथियाँ खंगाल के थक गई, उस पार का भेद न पाया कोई,",
                    "सच्चों के सिर पे जूते बरसें, झूठे मौज उड़ाएँ हर कोई !"
                ],
                "poetic_english": [
                    "I searched the dusty books from shelf to shelf, yet found no news of that transcendent Shore;",
                    "The truthful ones are beaten with old shoes, while brazen liars celebrate and roar!"
                ]
            },
            {
                "original": [
                    "चंग चंगेरे परे परेरे असीं आईआं सी अनभोल ।  ",
                    "बुल्ल्हा शाह जे बोलांगा हुन कौन सुने मेरे बोल ।  ",
                    "मेरे नौशहु दा कित मोल ।"
                ],
                "hindi_gloss": [
                    "चंग चंगेरे (उत्तम से अति-उत्तम ज्ञानी) परे परेरे (उस रहस्य से कोसों दूर रह गए), असीं (हम तो) आईआं (आई थीं यहाँ) सी (थीं) अनभोल (सर्वथा भोली-भाली बनकर),",
                    "बुल्ल्हा शाह (बुल्ले शाह कहते हैं) जे (यदि) बोलांगा (मैं अब सच बोलूँगा) हुन (तो भला) कौन (कौन) सुने (सुनेगा) मेरे (मेरे इन मर्मभेदी) बोल (वचनों को) ।",
                    "मेरे नौशहु दा कित मोल ।"
                ],
                "english_gloss": [
                    "चंग चंगेरे (the finest scholars) परे परेरे (stood far away baffled), असीं आईआं सी अनभोल (we came here naive, innocent, and pure),",
                    "बुल्ल्हा शाह (Bulleh Shah) जे बोलांगा (if I speak the truth) हुन कौन सुने (now who will listen to) मेरे बोल (my prophetic words) ।",
                    "मेरे नौशहु दा कित मोल (what price can match my Bridegroom's worth) ।"
                ],
                "poetic_hindi": [
                    "बड़े-बड़े ज्ञानी दूर खड़े रहे, हम भोली-भाली प्रेम में आईं,",
                    "बुल्ले शाह: गर सच बोलूँ तो कौन सुनेगा मेरी गवाही?",
                    "मेरे नवल-दूल्हे का क्या कोई मोल लगा सकता है?"
                ],
                "poetic_english": [
                    "The proudest scholars stood perplexed and far, while naive we came to claim our Bridegroom's hand;",
                    "Says Bulleh Shah: If I speak naked truth, who in this blinded world will understand?",
                    "What price could ever buy my radiant Groom?"
                ]
            }
        ],
        "sufi_commentary": "यह काफी कबीर के निर्भीक सामाजिक व्यंग्य और सूफी ज्ञान का संगम है। 'नौशहु' (नया दूल्हा) जीव और ब्रह्म के नित्य-नवीन संबंध का द्योतक है। बुल्ले शाह समाज की नैतिक गिरावट को बेनकाब करते हैं—'सच्चियां नूं पए वज्जन पौले झूठियां करन कलोल'। जब सत्यवादी अपमानित हो और झूठा सम्मानित, तब पोथियों और किताबों का ज्ञान व्यर्थ सिद्ध होता है। 'जे बोलांगा हुन कौन सुने मेरे बोल' मंसूर और सुकरात की नियति को दर्शाता है: अज्ञानी समाज में सत्य बोलने पर केवल प्रताड़ना ही मिलती है, इसीलिए सूफी साधक कभी-कभी मौन की शरण लेता है।"
    },
    {
        "id": 104,
        "title": "मेरी बुक्कल दे विच्च चोर",
        "title_english": "The Thief is Hiding Within My Own Cloak!",
        "historical_context": "यह बाबा बुल्ले शाह की विश्व-प्रसिद्ध, सर्वाधिक उद्धृत और कालजयी काफ़ियों में शीर्षस्थ है। इसमें 'चोर' परमात्मा का सबसे प्रिय सूफी रूपक है जो मनुष्य के अपने अंतःकरण ('बुक्कल' अर्थात् कंबल/हृदय के आंचल) में छिपा बैठा है, जबकि संसार उसे बाहर मस्जिदों, मंदिरों और कब्रों में ढूँढ रहा है। बुल्ले शाह हिंदू-मुस्लिम के बाह्य विवादों—रामदास और फतेह मुहम्मद के टकराव, श्मशान और कब्र के भय—को निरर्थक घोषित करते हुए उद्घोष करते हैं कि जब रहस्य प्रकट होता है तो यह विवाद मिट जाता है और भीतर से 'कुछ और ही' (परम ब्रह्म) निकल पड़ता है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: मेरी बुक्कल दे विच्च चोर)",
        "raga": "राग काफी / बिलावल / दरबारी",
        "theme": "अंतःकरण में ईश्वर की उपस्थिति (चोर), सांप्रदायिकता का उन्मूलन, रामदास-फ़तेह मुहम्मद का समन्वय, शाह इनायत का आकर्षण",
        "stanzas": [
            {
                "original": [
                    "मेरी बुक्कल दे विच्च चोर ।  ",
                    "नी मेरी बुक्कल दे विच्च चोर ।"
                ],
                "hindi_gloss": [
                    "मेरी (मेरी) बुक्कल (कमली/हृदय के आंचल) दे (के) विच्च (भीतर ही छिपा है वह) चोर (रहस्यमयी प्रियतम चोर) ।",
                    "नी (अरी सखी) मेरी (मेरी) बुक्कल (कंबल के आंचल) दे (के) विच्च (भीतर ही बसा है) चोर (मेरा चित्तचोर) ।"
                ],
                "english_gloss": [
                    "मेरी बुक्कल दे विच्च (within the folds of my own cloak) चोर (is the Thief) ।",
                    "नी मेरी बुक्कल दे विच्च चोर (O sisters, within the embrace of my cloak hides the Thief) ।"
                ],
                "poetic_hindi": [
                    "मेरी ही बुक्कल में छिपा है वो चितचोर,",
                    "अरी सखी, मेरे ही आँचल में बैठा वो अलख किशोर !"
                ],
                "poetic_english": [
                    "Within the secret folds of my own cloak the Thief resides!",
                    "O sisters mine, within my very breast the subtle Robber hides!"
                ]
            },
            {
                "original": [
                    "कीहनूं कूक सुणावां नी मेरी बुक्कल दे विच्च चोर ।  ",
                    "चोरी चोरी निकल गया जग विच्च पै गया शोर ।  ",
                    "मेरी बुक्कल दे विच्च चोर ।"
                ],
                "hindi_gloss": [
                    "कीहनूं (किसको जाकर) कूक (अपनी पुकार/गुहार) सुणावां (सुनाऊँ), नी (हे सखी) मेरी (मेरी) बुक्कल (कमली) दे (के) विच्च (भीतर ही है वह) चोर (चोर),",
                    "चोरी (चोरी-) चोरी (चोरी से) निकल (प्रकट हो) गया (गया वह), जग (और सारे संसार) विच्च (में) पै (मच) गया (गया) शोर (भारी शोर) ।",
                    "मेरी बुक्कल दे विच्च चोर ।"
                ],
                "english_gloss": [
                    "कीहनूं कूक सुणावां (unto whom shall I cry my lament), नी मेरी बुक्कल दे विच्च चोर (O within my cloak is the Thief),",
                    "चोरी चोरी निकल गया (stealthily He slipped away), जग विच्च पै गया शोर (an uproar arose throughout the world) ।",
                    "मेरी बुक्कल दे विच्च चोर (within my cloak is the Thief) ।"
                ],
                "poetic_hindi": [
                    "किसको जाकर पुकार सुनाऊँ, जब चोर छिपा मेरे अंदर?",
                    "चोरी-चोरी वो प्रकट हुआ, जग में गूँज उठा कलंदर !",
                    "मेरी बुक्कल में बैठा वो चितचोर !"
                ],
                "poetic_english": [
                    "Unto whom shall I raise my cry when the Thief is in my breast?",
                    "He slipped out stealthily, and filled the world with clamor and unrest!",
                    "Within the secret folds of my own cloak the Thief resides!"
                ]
            },
            {
                "original": [
                    "मुसलमान सिव्यां (सड़ने) तों ड्रदे हिन्दू ड्रदे गोर ।  ",
                    "दोवें एसे दे विच्च मरदे इहो दोहां दी खोर ।  ",
                    "मेरी बुक्कल दे विच्च चोर ।"
                ],
                "hindi_gloss": [
                    "मुसलमान (मुसलमान) सिव्यां (श्मशान में जलने) तों (से) ड्रदे (डरते हैं), हिन्दू (और हिंदू) ड्रदे (डरते हैं) गोर (कब्र में दफनाए जाने से),",
                    "दोवें (दोनों ही) एसे (इसी अविद्या और संकीर्णता) दे (के) विच्च (भीतर) मरदे (व्यर्थ मर-खप रहे हैं), इहो (यही) दोहां (दोनों पक्षों) दी (की परस्पर) खोर (दुर्भावना/हठधर्मी है) ।",
                    "मेरी बुक्कल दे विच्च चोर ।"
                ],
                "english_gloss": [
                    "मुसलमान सिव्यां तों ड्रदे (the Muslim dreads the flaming pyre), हिन्दू ड्रदे गोर (the Hindu dreads the silent grave),",
                    "दोवें एसे दे विच्च मरदे (both perish in this very strife), इहो दोहां दी खोर (this is the stubborn malice of both) ।",
                    "मेरी बुक्कल दे विच्च चोर (within my cloak is the Thief) ।"
                ],
                "poetic_hindi": [
                    "मुस्लिम डरे श्मशान से, हिंदू को कब्र डराए,",
                    "दोनों इस झगड़े में मरे, यह हठ दोनों को खाए !",
                    "मेरी बुक्कल में बैठा वो चितचोर !"
                ],
                "poetic_english": [
                    "Muslims dread the cremation pyre; Hindus dread the grave's deep clay;",
                    "Both consume their lives in fear, trapped in their narrow bigot way!",
                    "Within the secret folds of my own cloak the Thief resides!"
                ]
            },
            {
                "original": [
                    "किते राम दास किते फ़तह मुहंमद इहो कदीमी शोर ।  ",
                    "मिट गया दोहां दा झगड़ा निकल प्या कुझ होर ।  ",
                    "मेरी बुक्कल दे विच्च चोर ।"
                ],
                "hindi_gloss": [
                    "किते (कहीं पर नाम रखा है) राम दास (रामदास) किते (और कहीं) फ़तह मुहंमद (फतेह मुहम्मद), इहो (यही तो है) कदीमी (सदा-सदा से चला आ रहा पुराना) शोर (बखेड़ा),",
                    "मिट (समाप्त हो) गया (गया) दोहां (इन दोनों) दा (का) झगड़ा (झगड़ा तब), निकल (जब भीतर से प्रकट हो) प्या (पड़ा) कुझ (कुछ) होर (और ही परम अलौकिक सत्य) ।",
                    "मेरी बुक्कल दे विच्च चोर ।"
                ],
                "english_gloss": [
                    "किते राम दास (somewhere Ram Das) किते फ़तह मुहंमद (somewhere Fateh Muhammad), इहो कदीमी शोर (this is the ancient clamor),",
                    "मिट गया दोहां दा झगड़ा (the dispute of both dissolved), निकल प्या कुझ होर (when something else entirely emerged) ।",
                    "मेरी बुक्कल दे विच्च चोर (within my cloak is the Thief) ।"
                ],
                "poetic_hindi": [
                    "कहीं पे रामदास है नाम, कहीं पे फ़तेह मुहम्मद का शोर,",
                    "दोनों का झगड़ा मिट गया, जब भीतर से निकला कुछ और !",
                    "मेरी बुक्कल में बैठा वो चितचोर !"
                ],
                "poetic_english": [
                    "Here he is named Ram Das, and there Fateh Muhammad is the shout;",
                    "Their ancient quarrel melted away when Something Else came stepping out!",
                    "Within the secret folds of my own cloak the Thief resides!"
                ]
            },
            {
                "original": [
                    "अरश मुनव्वर बांगां मिलियां सुणियां तख़त लाहौर ।  ",
                    "शाह इनायत कुंडियां पाईआं लुक छुप खिचदा डोर ।  ",
                    "मेरी बुक्कल दे विच्च चोर ।"
                ],
                "hindi_gloss": [
                    "अरश (परम आकाश) मुनव्वर (प्रकाशमान अर्श से) बांगां (दिव्य पुकारें) मिलियां (गूँज उठीं), सुणियां (वे पुकारें सुनाई दीं) तख़त (आध्यात्मिक तख्त) लाहौर (लाहौर के दरबार में),",
                    "शाह इनायत (हज़रत शाह इनायत कादरी ने) कुंडियां (प्रेम के अंकुश/कांटे) पाईआं (डाल रखे हैं), लुक (छिप-) छुप (छुपकर) खिचदा (खींच रहे हैं प्रेम की) डोर (डोरी) ।",
                    "मेरी बुक्कल दे विच्च चोर ।"
                ],
                "english_gloss": [
                    "अरश मुनव्वर बांगां मिलियां (calls sounded from the Luminous Heaven), सुणियां तख़त लाहौर (were heard at the Throne of Lahore),",
                    "शाह इनायत कुंडियां पाईआं (Shah Inayat cast His mystic hooks), लुक छुप खिचदा डोर (hiding in secret, He pulls the twine) ।",
                    "मेरी बुक्कल दे विच्च चोर (within my cloak is the Thief) ।"
                ],
                "poetic_hindi": [
                    "अर्श-ए-मुनव्वर से उठी पुकार, तख्त लाहौर पे गूंजी तान,",
                    "शाह इनायत ने कांटा डाला, खींच रहे डोरी सुजान !",
                    "मेरी बुक्कल में बैठा वो चितचोर !"
                ],
                "poetic_english": [
                    "Calls resounded from Luminous Heavens, heard at the Throne of Lahore on high;",
                    "Shah Inayat cast His wondrous hooks, and pulls the cord unseen and shy!",
                    "Within the secret folds of my own cloak the Thief resides!"
                ]
            },
            {
                "original": [
                    "जिस ढूंडाइआ तिस ने पाइआ ना झुर झुर होया मोर ।  ",
                    "पीरे पीरां बग़दाद असाडा मुरशद तख़त लाहौर ।  ",
                    "मेरी बुक्कल दे विच्च चोर ।"
                ],
                "hindi_gloss": [
                    "जिस (जिसने अंतःकरण में) ढूंडाइआ (खोजा) तिस (उसी) ने (ने) पाइआ (उसे प्राप्त किया), ना (वह संशय में) झुर (झुर-झुरकर/घुल-घुलकर) होया (नहीं हुआ) मोर (मोर की भांति व्याकुल),",
                    "पीरे पीरां (पीरों के पीर हज़रत अब्दुल कादिर जिलानी) बग़दाद (बगदाद वाले) असाडा (हमारे सर्वोच्च मार्गदर्शक हैं), मुरशद (और प्रत्यक्ष सद्गुरु हैं) तख़त (तख्त) लाहौर (लाहौर वाले शाह इनायत) ।",
                    "मेरी बुक्कल दे विच्च चोर ।"
                ],
                "english_gloss": [
                    "जिस ढूंडाइआ तिस ने पाइआ (whosoever sought found Him within), ना झुर झुर होया मोर (wasted not away like the pining peacock),",
                    "पीरे पीरां बग़दाद असाडा (Pir of Pirs of Baghdad is ours), मुरशद तख़त लाहौर (our living Murshid graces the Throne of Lahore) ।",
                    "मेरी बुक्कल दे विच्च चोर (within my cloak is the Thief) ।"
                ],
                "poetic_hindi": [
                    "जिसने खोजा उसने पाया, मन का संशय सारा खोया,",
                    "पीरों के पीर बगदाद हमारे, लाहौर तख्त पे मुर्शिद बोया !",
                    "मेरी बुक्कल में बैठा वो चितचोर !"
                ],
                "poetic_english": [
                    "Who sought within has found the prize, freed from all pining grief and dross;",
                    "The Pir of Pirs in Baghdad dwells; our Master rules Lahore across!",
                    "Within the secret folds of my own cloak the Thief resides!"
                ]
            },
            {
                "original": [
                    "इहो तुसीं वी आखो सारे आप गुड्डी आप डोर ।  ",
                    "मैं दसनां तुसीं पकड़ ल्याउ बुल्ल्हे शाह दा चोर ।  ",
                    "मेरी बुक्कल दे विच्च चोर । नी मेरी बुक्कल दे विच्च चोर ।"
                ],
                "hindi_gloss": [
                    "इहो (यही परम सत्य) तुसीं (तुम) वी (भी) आखो (कहो) सारे (सब मिलकर कि) आप (वह परमात्मा स्वयं ही) गुड्डी (पतंग है) आप (और स्वयं ही उड़ाने वाली) डोर (डोरी है),",
                    "मैं (मैं) दसनां (पता बताता हूँ) तुसीं (तुम जाकर) पकड़ (पकड़) ल्याउ (ले आओ) बुल्ल्हे (बुल्ले) शाह (शाह) दा (का यह प्यारा) चोर (चोर) ।",
                    "मेरी बुक्कल दे विच्च चोर । नी मेरी बुक्कल दे विच्च चोर ।"
                ],
                "english_gloss": [
                    "इहो तुसीं वी आखो सारे (let all of you proclaim this very truth), आप गुड्डी आप डोर (He Himself is the kite, He Himself the cord),",
                    "मैं दसनां (I disclose His whereabouts) तुसीं पकड़ ल्याउ (go and apprehend) बुल्ल्हे शाह दा चोर (the Thief of Bulleh Shah) ।",
                    "मेरी बुक्कल दे विच्च चोर (within my cloak is the Thief) ।"
                ],
                "poetic_hindi": [
                    "तुम सब भी बोलो: वही पतंग है, वही उड़ाने वाली डोर,",
                    "पता बताऊँ, पकड़ के लाओ बुल्ले शाह का नवल-किशोर !",
                    "मेरी बुक्कल में बैठा वो चितचोर,",
                    "अरी सखी, मेरे ही आँचल में बैठा वो नवल किशोर !"
                ],
                "poetic_english": [
                    "Sing out together this truth divine: He is the kite, and He the thread!",
                    "I tell His lair—go seize the Thief who captured Bulleh’s heart instead!",
                    "Within the secret folds of my own cloak the Thief resides!",
                    "O sisters mine, within my very breast the subtle Robber hides!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी सूफी साहित्य का वह अमर हीरा है जिसने धार्मिक कट्टरता और द्वैत की दीवारों को सदा के लिए ढहा दिया। 'बुक्कल दे विच्च चोर' उपनिषदों के 'तत्त्वमसि' और कुरान के 'वह तुम्हारी गर्दन की नस (हब्लिल वरीद) से भी अधिक निकट है' का काव्यात्मक अनुवाद है। मनुष्य परमात्मा को काबा या काशी में ढूँढता फिरता है, जबकि वह स्वयं साधक के भीतर विराजमान है। 'किते राम दास किते फ़तह मुहंमद... निकल प्या कुझ होर' यह प्रमाणित करता है कि ईश्वर न हिंदू है न मुसलमान; वह इन सभी मानवनिर्मित उपाधियों से परे विशुद्ध सच्चिदानंद स्वरूप है। 'आप गुड्डी आप डोर' सर्वेश्वरवाद (वहदत-उल-वुजूद) का ऐसा लोक-रूपक है जो बताता है कि उड़ाने वाला भी वही है और उड़ने वाली पतंग भी वही है।"
    },
    {
        "id": 105,
        "title": "मिल लओ सहेलड़ीयो मेरी राज गहेलड़ीयो, मैं साहुरिआं घर जाणा",
        "title_english": "Meet Me, O Sister Friends of My Youth: I Must Depart for My In-Laws' Home!",
        "historical_context": "यह 4 बंधों की एक अत्यंत कारुणिक, मर्मस्पर्शी और रूपकात्मक काफी है। इसमें विदाई और मृत्यु का लोक-संस्कृति के माध्यम से आध्यात्मिक निरूपण किया गया है। मायका यह नश्वर संसार है और ससुराल परलोक (ईश्वर का दरबार)। सखियां सांसारिक संगी-साथी हैं। आत्मा अपनी सखियों से अंतिम विदाई मांगती है क्योंकि अल्लाह का हुक्म आ चुका है। माता-पिता (संसार) ने दहेज में केवल एक चोली और चुनरी दी है, जबकि ससुराल में सांसारिक कर्मों का हिसाब होगा। केवल वही आत्मा परमात्मा को प्रिय होगी जिसके पल्ले शुभ कर्म और मीठे बोल होंगे।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: मिल लओ सहेलड़ीयो)",
        "raga": "राग काफी / बिलावल / आसा",
        "theme": "संसार से महाप्रस्थान (मृत्यु/विदाई), ससुराल (परलोक), कर्मों का दहेज, शुभ कर्मों की अनिवार्यता",
        "stanzas": [
            {
                "original": [
                    "मिल लओ सहेलड़ीयो मेरी राज गहेलड़ीयो, मैं साहुरिआं घर जाना ।  ",
                    "तुसां भी होसी अल्ल्हा भाणा, मैं साहुरिआं घर जाना ।"
                ],
                "hindi_gloss": [
                    "मिल (मिल) लओ (लो गले) सहेलड़ीयो (हे मेरी प्यारी सहेलियो) मेरी (मेरी) राज (राजसी सुखों की) गहेलड़ीयो (बचपन की हमजोलियो), मैं (मुझको तो अब अपने) साहुरिआं (ससुराल/परलोक के) घर (घर) जाना (जाना ही है) ।",
                    "तुसां (तुम सब पर) भी (भी एक दिन) होसी (होगा यही) अल्ल्हा (अल्लाह का) भाणा (ईश्वरीय विधान/हुक्म लागू), मैं (मुझे तो) साहुरिआं घर जाना (ससुराल जाना ही है) ।"
                ],
                "english_gloss": [
                    "मिल लओ सहेलड़ीयो (embrace me, O sister friends) मेरी राज गहेलड़ीयो (companions of my royal youth), मैं साहुरिआं घर जाना (I must depart for my in-laws' home) ।",
                    "तुसां भी होसी अल्ल्हा भाणा (unto you too will fall God's sovereign decree), मैं साहुरिआं घर जाना (I must depart for my in-laws' home) ।"
                ],
                "poetic_hindi": [
                    "गले मिलो सखियो, मेरी बचपन की हमजोलियो, मुझे ससुराल सिधारना है,",
                    "तुम पर भी रब की रज़ा होगी, मुझे तो उस पार उतरना है !"
                ],
                "poetic_english": [
                    "Embrace me, O sister friends, sweet comrades of my youth so fair;",
                    "I must depart unto my in-laws' home, the call of death is in the air!",
                    "Unto you too shall fall the Lord's decree—we all must journey there!"
                ]
            },
            {
                "original": [
                    "अंमां बाबुल दाज जो दित्ता, इक चोली इक चुन्नी ।  ",
                    "दाज तिन्हां दे वेख के हुन मैं, हंझू भर भर रुन्नी ।  ",
                    "इक विछोड़ा सईआं दा, जिवें डारों कूंज विछुन्नी ।"
                ],
                "hindi_gloss": [
                    "अंमां (माता) बाबुल (और पिता ने) दाज (दहेज में) जो (जो कुछ) दित्ता (दिया है, वह केवल) इक (एक) चोली (चोली) इक (और एक) चुन्नी (चुनरी ही है),",
                    "दाज (यह तुच्छ दहेज) तिन्हां (उनका) दे (का) वेख (देख) के (कर) हुन (अब) मैं (मैं) हंझू (आंसुओं से) भर (भर-) भर (भर कर) रुन्नी (रोई),",
                    "इक (एक तो यह) विछोड़ा (वियोग है मेरी प्यारी) सईआं (सखियों) दा (का), जिवें (जैसे) डारों (अपने झुंड से) कूंज (कोई कुंज पक्षी) विछुन्नी (बिछुड़ जाती है) ।"
                ],
                "english_gloss": [
                    "अंमां बाबुल दाज जो दित्ता (the dowry my parents gave was but) इक चोली इक चुन्नी (a single bodice and a veil),",
                    "दाज तिन्हां दे वेख के हुन मैं (seeing their poor dowry now) हंझू भर भर रुन्नी (I wept with brimful tears),",
                    "इक विछोड़ा सईआं दा (on one side the parting from dearest companions), जिवें डारों कूंज विछुन्नी (like a lone crane severed from her flock) ।"
                ],
                "poetic_hindi": [
                    "माता-पिता ने दहेज में केवल एक चोली और चुनरी दी,",
                    "यह तुच्छ दहेज देख कर अंखियों ने अश्रुओं की धारा पी !",
                    "सखियों का वियोग ऐसा सालता, जैसे झुंड से बिछुड़ी कूंज अकेली !"
                ],
                "poetic_english": [
                    "My mother and father gave as dowry a single bodice and a fragile veil;",
                    "Beholding this meager store of deeds, with streaming tears I weep and wail!",
                    "Severed from cherished sister souls, like a lone crane parted from her flock!"
                ]
            },
            {
                "original": [
                    "रंग बरंगे सूल अपुट्ठे, जांदे चीर नैन जी नूं ।  ",
                    "ऐथों दे दुक्ख नाल लिजावां, अगले सौंपां कीहनूं ।"
                ],
                "hindi_gloss": [
                    "रंग (भांति-) बरंगे (भांति के) सूल (कांटे/शूल) अपुट्ठे (उलटे-सीधे), जांदे (जा रहे हैं) चीर (चीरते हुए मेरे) नैन (नेत्रों और) जी (प्राणों) नूं (को),",
                    "ऐथों (इस नश्वर संसार) दे (के) दुक्ख (दुखों को) नाल (अपने साथ) लिजावां (लेकर जा रही हूँ), अगले (उस परलोक में जाकर अपने दुख) सौंपां (सौंपूँ/सुनाऊँ) कीहनूं (किसको) ।"
                ],
                "english_gloss": [
                    "रंग बरंगे सूल अपुट्ठे (motley and perverse thorns of anguish), जांदे चीर नैन जी नूं (rend my eyes and soul asunder),",
                    "ऐथों दे दुक्ख नाल लिजावां (I bear with me the griefs of this earthly realm), अगले सौंपां कीहनूं (unto whom in the hereafter shall I entrust them) ।"
                ],
                "poetic_hindi": [
                    "तरह-तरह के कांटे चुभते, चीर रहे तन-मन के प्राण,",
                    "यहाँ के दुख संग ले चली, वहाँ किसको सौंपूँ अपनी जान?"
                ],
                "poetic_english": [
                    "Sharp, twisted thorns of myriad griefs pierce through my weeping eyes and soul;",
                    "I carry the sorrows of this fleeting world—unto whom shall I yield them at the goal?"
                ]
            },
            {
                "original": [
                    "सस्स ननान रहन ना मिलदा, जाना वारो वारी ।  ",
                    "चंग चंगेरे पकड़ मंगाए, मैं कीहदी पनेहारी ।  ",
                    "जिस गुन पल्ले बोल सवल्ले, सोई शहु नूं प्यारी ।"
                ],
                "hindi_gloss": [
                    "सस्स (सास/कर्म-विधान) ननान (और ननद के साथ सदा) रहन (रहना) ना (नहीं) मिलदा (मिलता), जाना (जाना तो सबको ही है) वारो (अपनी-अपनी) वारी (बारी से),",
                    "चंग (बड़े-बड़े) चंगेरे (उत्तम और गुणी लोगों को भी मृत्यु के दूतों ने) पकड़ (पकड़ कर) मंगाए (बुला लिया), मैं (मैं दीन) कीहदी (किसकी) पनेहारी (पनहारिन/दासी हूँ भला),",
                    "जिस (जिस साधक के) गुन (सद्गुण) पल्ले (पल्ले/दामन में होंगे और) बोल (वाणी में) सवल्ले (मधुर और नम्र वचन होंगे), सोई (वही आत्मा) शहु (परम प्रियतम प्रभु) नूं (को) प्यारी (प्रिय लगेगी) ।"
                ],
                "english_gloss": [
                    "सस्स ननान रहन ना मिलदा (cannot abide forever with mother-in-law or sister-in-law), जाना वारो वारी (each must depart in their turn),",
                    "चंग चंगेरे पकड़ मंगाए (the mightiest and best were summoned by force), मैं कीहदी पनेहारी (whose water-bearer am I, frail and poor),",
                    "जिस गुन पल्ले (who has virtues in her apron) बोल सवल्ले (and sweet gentle words), सोई शहु नूं प्यारी (she alone is beloved of the Sovereign Lord) ।"
                ],
                "poetic_hindi": [
                    "सास-ननद संग सदा न रहना, अपनी-अपनी बारी जाना,",
                    "बड़े-बड़े गुणी चले गए, फिर मुझ पणिहारिन का क्या ठिकाना?",
                    "जिसके पल्ले सद्गुण होंगे, बोल मधुर और सच्चा प्यार,",
                    "वही सुहागन प्यारी होगी, पाएगा जिसको करतार !"
                ],
                "poetic_english": [
                    "No one can dwell forever here; each takes their turn when life is run;",
                    "The mightiest souls were borne away—frail water-bearer, who am I to shun?",
                    "She who bears virtue in her skirt, with gentle words of humble grace,",
                    "She alone is the Master's bride, embraced within His sacred place!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी कबीर और गुरु नानक की विदाई और ससुराल के रूपकों से परिपूर्ण है। सूफी और संत परंपरा में मायका संसार का और ससुराल परलोक का प्रतीक है। जब विदाई की वेला (मृत्यु) आती है, तो आत्मा देखती है कि उसके पास केवल 'एक चोली और एक चुन्नी' (नश्वर देह और सांसारिक कर्म) ही है। सास और ननद माया और सांसारिक आसक्तियों के प्रतीक हैं जो आत्मा को निरंतर ताने देते हैं। अंतिम बंध में बुल्ले शाह जीवन का चरम सत्य उद्घाटित करते हैं: 'जिस गुन पल्ले बोल सवल्ले, सोई शहु नूं प्यारी'। बाह्य सौंदर्य, कुल-मर्यादा या धन-दौलत परमात्मा के दरबार में किसी काम नहीं आते; केवल विनम्रता, मधुर वाणी और आत्मीय सद्गुण ही परमात्मा से मिलन का साधन बनते हैं।"
    }
]

new_lexicon_terms = {
    "टमक": {"hindi": "बड़ा नगाड़ा, रण-ढोल, जोगी का वाद्य", "english": "large kettledrum, begging-drum"},
    "बुग़चा": {"hindi": "कपड़े की बड़ी पोटली जिसमें सामान बांधा जाता है", "english": "bundle of cloth/pack for carrying gear"},
    "कुन फ़ैकून": {"hindi": "कुरान का शब्द: 'हो जा! और वह हो गया' (सृष्टि की आदि-ध्वनि)", "english": "'Kun Fayakun', the divine fiat 'Be! And it was'"},
    "चाक": {"hindi": "ग्वाला, पशु चराने वाला सेवक (रांझा चूचक का चाक बना)", "english": "cowherd, servant tending herds"},
    "सेहली": {"hindi": "काले ऊन की बटी हुई माला जो नाथ जोगी गले में पहनते हैं", "english": "sehli, black woolen sacred cord worn by yogis"},
    "चीना": {"hindi": "एक प्रकार का छोटा अन्न/मोटा अनाज (बाजरा-कांगणी)", "english": "millet, proso millet grain"},
    "फन्द": {"hindi": "युक्ति, छल, गुप्त योजना", "english": "stratagem, clever device/ruse"},
    "नौशहु": {"hindi": "नया दूल्हा, नवल वर, साक्षात् परमात्मा", "english": "new bridegroom; the Supreme Divine Beloved"},
    "पौले": {"hindi": "जूतियां, पुराने जूते से मार", "english": "shoes, strikes with slippers/beating"},
    "कलोल": {"hindi": "क्रीड़ा, मौज-मस्ती, आनंद-विलास", "english": "frolic, carefree revelry/sport"},
    "बुक्कल": {"hindi": "कंबल का आंचल, हृदय का कोना, अंतःकरण की चादर", "english": "folds of a shawl/cloak; the intimate bosom/heart"},
    "खोर": {"hindi": "दुर्भावना, कपट, हठधर्मी, द्वेष", "english": "malice, grudge, obstinate bigotry"},
    "राज गहेलड़ीयो": {"hindi": "बचपन की सखियां, राजसी सुख की हमजोलियां", "english": "playmates of youth, companions of joyous childhood"},
    "सवल्ले": {"hindi": "सुहावने, मधुर, नम्र और कल्याणकारी", "english": "sweet, gentle, auspicious and humble"}
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
        "completed_count": 105,
        "total": 160,
        "next_kafi_id": 106,
        "last_updated": "2026-10-17T18:20:00+05:30",
        "last_batch": "101-105",
        "status": "in_progress",
        "milestone": "Part 3 commenced! 105/160 (65.6%) finished."
    }
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print(f"Checkpoint updated: 105/160 completed. Next ID: 106")

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
