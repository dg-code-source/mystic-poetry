# -*- coding: utf-8 -*-
"""
Process Kafian 66 to 70 for Bulleh Shah Trilingual Edition.
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
        "id": 66,
        "title": "केहे लारे देना एं सानूं दो घड़ियां मिल जाईं",
        "title_english": "Why Make Such False Excuses? Come Meet Me For Two Fleeting Moments!",
        "historical_context": "इस काफी में विरहिणी आत्मा प्रियतम के छल-प्रपंच और झूठे आश्वासनों (लारों) पर मीठा उलाहना देती है। परमात्मा अंतर्यामी होकर भी हृदय के ओट में छिपा रहता है। बुल्ले शाह कहते हैं कि जब तू मेरे ही घर (हृदय) में बसता है, तो फिर मुझे दर्शन के लिए क्यों तरसाता है?",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: केहे लारे देना एं)",
        "raga": "राग काफी / देस",
        "theme": "प्रियतम को उलाहना, ईश्वर की सर्वव्यापकता बनाम प्रत्यक्ष दर्शन का अभाव, विरह-पीड़ा",
        "stanzas": [
            {
                "original": [
                    "केहे लारे देना एं सानूं दो घड़ियां मिल जाईं ।"
                ],
                "hindi_gloss": [
                    "केहे (कैसे झूठे) लारे (आश्वासन/बहाने) देना (देता) एं (है) सानूं (हमें), दो (दो) घड़ियां (घड़ी/पल भर के लिए) मिल (आकर मिल) जाईं (जा) ।"
                ],
                "english_gloss": [
                    "केहे (what) लारे (false promises/excuses) देना (givest) एं (thou) सानूं (unto us), दो (for two) घड़ियां (fleeting moments) मिल (meet) जाईं (come) ।"
                ],
                "poetic_hindi": [
                    "क्यों झूठे लारे देता है, दो घड़ियाँ आ मिल जाईं !"
                ],
                "poetic_english": [
                    "Why give such promises in vain? Come meet me for two fleeting moments, Love!"
                ]
            },
            {
                "original": [
                    "नेड़े वस्सें थां ना दस्सें  ",
                    "ढूंडां कित वल्ल जाहीं,  ",
                    "आपे झाती पाई अहमद  ",
                    "वेखां तां मुड़ नाहीं ।"
                ],
                "hindi_gloss": [
                    "नेड़े (समीप ही) वस्सें (बसता है) थां (किंतु अपना स्थान/पता) ना (नहीं) दस्सें (बताता है),",
                    "ढूंडां (ढूंढूँ) कित (किस) वल्ल (ओर) जाहीं (जाकर),",
                    "आपे (स्वयं ही) झाती (अपनी झांकी) पाई (दिखाई) अहमद (हे अहमद/प्रियतम),",
                    "वेखां (जब मैं देखने लगूँ) तां (तो) मुड़ (पुनः) नाहीं (लोप हो जाता है) ।"
                ],
                "english_gloss": [
                    "नेड़े (close beside) वस्सें (dwellest) थां (abode) ना (not) दस्सें (revealest),",
                    "ढूंडां (should I search) कित (which) वल्ल (way) जाहीं (go),",
                    "आपे (Thyself) झाती (a glimpse) पाई (cast) अहमद (O Ahmad/Beloved),",
                    "वेखां (when I gaze) तां (then) मुड़ (again) नाहीं (art gone) ।"
                ],
                "poetic_hindi": [
                    "निकट बसे, पर पता न देवे, किस पथ ढूँढूँ धाई ?",
                    "अहमद बन कर झलक दिखाई, देखूँ तो छिप जाई !"
                ],
                "poetic_english": [
                    "Thou dwellest near, yet hidest Thine abode—which way to seek Thee should my footsteps turn?",
                    "As Ahmad Thou didst flash upon the road, yet vanished when my eyes began to burn!"
                ]
            },
            {
                "original": [
                    "आख ग्युं मुड़ आइउं नहीं  ",
                    "सीने दे विच भड़कन भाहीं,  ",
                    "इकसे घर विच वसदियां रसदियां,  ",
                    "कित वल्ल कूक सुणाईं ।"
                ],
                "hindi_gloss": [
                    "आख (कहकर) ग्युं (गया था कि लौटूंगा) मुड़ (पुनः) आइउं (आया) नहीं (नहीं),",
                    "सीने (हृदय) दे (के) विच (भीतर) भड़कन (धधक रही हैं) भाहीं (विरह की ज्वालाएं),",
                    "इकसे (एक ही) घर (हृदय-घर) विच (में) वसदियां (बसते हुए) रसदियां (आनंद लेते हुए),",
                    "कित (किस) वल्ल (दिशा में) कूक (अपनी विरह-पुकार) सुणाईं (सुनाऊँ) ।"
                ],
                "english_gloss": [
                    "आख (promising) ग्युं (wentest) मुड़ (again) आइउं (returned) नहीं (not),",
                    "सीने (chest) दे (of) विच (within) भड़कन (blaze) भाहीं (flames of longing),",
                    "इकसे (in the very same) घर (house/heart) विच (within) वसदियां (dwelling) रसदियां (reveling),",
                    "कित (which) वल्ल (way) कूक (my cry of grief) सुणाईं (should I voice) ।"
                ],
                "poetic_hindi": [
                    "आने का कह कर गया न लौटा, सीने में आग भड़कती जाए,",
                    "एक ही घर में साथ बसे जब, किसे पुकारूँ हाय ?"
                ],
                "poetic_english": [
                    "Pledging return Thou didst depart unseen, while in my chest the searing embers leap;",
                    "Dwelling together within walls serene, to whom shall I lift up my voice and weep?"
                ]
            },
            {
                "original": [
                    "पांधी जा, मेरा देह सुनेहा  ",
                    "दिल दे उहले लुकदा केहा,  ",
                    "नाम अल्लाह दे ना हो वैरी  ",
                    "मुक्ख वेखन नूं ना तरसाईं ।"
                ],
                "hindi_gloss": [
                    "पांधी (हे पथिक) जा (जा), मेरा (मेरा) देह (दे दे) सुनेहा (संदेश),",
                    "दिल (हृदय) दे (के) उहले (ओट/पर्दे में) लुकदा (छिपना) केहा (कैसा),",
                    "नाम (नाम पर) अल्लाह (अल्लाह के) दे (दे) ना (मत) हो (हो) वैरी (शत्रु/निष्ठुर),",
                    "मुक्ख (मुखड़ा) वेखन (देखने) नूं (के लिए) ना (मत) तरसाईं (तरसा) ।"
                ],
                "english_gloss": [
                    "पांधी (O traveler) जा (go), मेरा (my) देह (deliver) सुनेहा (message),",
                    "दिल (heart) दे (of) उहले (behind the screen) लुकदा (hiding) केहा (why so),",
                    "नाम (in the name) अल्लाह (of God) दे (give) ना (not) हो (be) वैरी (cruel foe),",
                    "मुक्ख (face) वेखन (to behold) नूं (unto) ना (do not) तरसाईं (make me pine) ।"
                ],
                "poetic_hindi": [
                    "हे पथिक! जा मेरा संदेशा दे, दिल की ओट में छिपना कैसा ?",
                    "अल्लाह के नाम पर वैर न साध, मुख देखने को तरसावे ऐसा !"
                ],
                "poetic_english": [
                    "Go, traveler, convey this plea of mine: why lurk behind the curtains of the heart?",
                    "In Allah’s name, be not a foe malign, nor keep me from Thy radiant face apart!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु की लाइआ मैनूं  ",
                    "रात अद्धी है तेरी महमा,  ",
                    "औझड़ बेले सभ कोई डरदा  ",
                    "सो ढूंडां मैं चाईं चाईं ।  ",
                    "केहे लारे देना एं सानूं दो घड़ियां मिल जाईं ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ला कहता है) शहु (हे शाह/प्रियतम) की (क्या रोग) लाइआ (लगा दिया) मैनूं (मुझको),",
                    "रात (रात) अद्धी (आधी रात के समय) है (होती है) तेरी (तेरी) महमा (महिमा/उपासना),",
                    "औझड़ (बीहड़/घने) बेले (जंगल में जाने से) सभ (हर) कोई (कोई) डरदा (डरता है),",
                    "सो (उसी में) ढूंडां (ढूंढती फिरती हूँ) मैं (मैं) चाईं (उत्साह से) चाईं (चाव-पूर्वक) ।",
                    "केहे (कैसे झूठे) लारे (आश्वासन) देना (देता) एं सानूं दो घड़ियां मिल जाईं ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh says) शहु (O Lord) की (what malady) लाइआ (hast inflicted) मैनूं (upon me),",
                    "रात (night) अद्धी (at midnight) है (is) तेरी (Thy) महमा (praise/vigil),",
                    "औझड़ (wild/perilous) बेले (forest) सभ (everyone) कोई (anyone) डरदा (dreads),",
                    "सो (there) ढूंडां (seek) मैं (I) चाईं (with longing) चाईं (with eager zeal) ।",
                    "केहे लारे देना एं सानूं दो घड़ियां मिल जाईं ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा शौह! क्या रोग लगाया, आधी रात में सुध तेरी आए,",
                    "बीहड़ वन से जग डरता है, मैं चाव भरी ढूँढती जाए ।",
                    "क्यों झूठे लारे देता है, दो घड़ियाँ आ मिल जाईं !"
                ],
                "poetic_english": [
                    "Bulleh’s Great Lord, what fever hast Thou laid, waking my spirit in the midnight deep?",
                    "Through haunted wilds where others shrink afraid, with eager joy my searching footsteps leap.",
                    "Why give such promises in vain? Come meet me for two fleeting moments, Love!"
                ]
            }
        ],
        "philosophical_meaning": "सूफी मनोविज्ञान में साधक की विरह-अवस्था का जीवंत वर्णन है। परमात्मा 'हब्लिल वरीद' (गर्दन की नस) से भी निकट है, किंतु साधक जब तक द्वैत की दृष्टि रखता है, वह उसे पा नहीं सकता। 'औझड़ बेला' सांसारिक भय और संशय का प्रतीक है, जिसे केवल तीव्र प्रेम (इश्क) से ही पार किया जा सकता है।"
    },
    {
        "id": 67,
        "title": "ख़ाकी ख़ाक स्युं रल जाणा",
        "title_english": "This Dust Shall Merge With Dust",
        "historical_context": "इस गंभीर और वैराग्यमय काफी में बुल्ले शाह मानव-शरीर की नश्वरता और सांसारिक अहंकार की व्यर्थता का बोध कराते हैं। मिट्टी से बना यह शरीर अंततः मिट्टी में ही मिल जाएगा; इसलिए किसी पर अत्याचार या ज़ोर-जबरदस्ती करना मूर्खता है। परलोक की यात्रा में केवल ईश्वर का 'नाम' ही पाथेय (खर्ची) के रूप में काम आता है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, तुक: जाणा / धिङाना)",
        "raga": "राग तिलंग / भैरवी",
        "theme": "शरीर की नश्वरता, मृत्यु का अटल सत्य, अहंकार का त्याग, नाम-स्मरण की अनिवार्यता",
        "stanzas": [
            {
                "original": [
                    "ख़ाकी ख़ाक सूं (स्युं) रल जाणा  ",
                    "कुछ नहीं ज़ोर धिङाना ।"
                ],
                "hindi_gloss": [
                    "ख़ाकी (मिट्टी का बना यह शरीर) ख़ाक (मिट्टी) स्युं (के साथ) रल (मिल) जाणा (जाएगा) ।",
                    "कुछ (कुछ भी) नहीं (नहीं चलेगा) ज़ोर (बल/शक्ति) धिङाना (अन्याय/ज़बरदस्ती) ।"
                ],
                "english_gloss": [
                    "ख़ाकी (earth-born dust) ख़ाक (dust) स्युं (with) रल (blend/merge) जाणा (must go) ।",
                    "कुछ (nothing) नहीं (not avails) ज़ोर (force) धिङाना (coercion/tyranny) ।"
                ],
                "poetic_hindi": [
                    "माटी की देह माटी में मिलेगी, न चलेगा ज़ोर-धिगाना कोई !"
                ],
                "poetic_english": [
                    "Dust must dissolve in dust at last, no pride nor tyranny avails!"
                ]
            },
            {
                "original": [
                    "गए सो गए फेर नहीं आए, मेरे जानी मीत प्यारे,  ",
                    "मेरे बाझों रहन्दे नाहीं, हुन क्यों असां विसारे,  ",
                    "ख़ाकी ख़ाक सूं (स्युं) रल जाना ।"
                ],
                "hindi_gloss": [
                    "गए (जो चले गए) सो (वे) गए (चले गए) फेर (पुनः) नहीं (नहीं) आए (लौटे), मेरे (मेरे) जानी (प्राण-समान) मीत (मित्र/सखा) प्यारे (प्यारे),",
                    "मेरे (मेरे) बाझों (बिना जो एक पल) रहन्दे (रहते) नाहीं (नहीं थे), हुन (अब) क्यों (क्यों) असां (हमें) विसारे (भुला दिया) ।",
                    "ख़ाकी ख़ाक सूं रल जाना ।"
                ],
                "english_gloss": [
                    "गए (departed) सो (who) गए (went) फेर (again) नहीं (never) आए (returned), मेरे (my) जानी (life-long) मीत (friends) प्यारे (beloved),",
                    "मेरे (me) बाझों (without) रहन्दे (could live) नाहीं (never), हुन (now) क्यों (why) असां (us) विसारे (forgotten) ।",
                    "ख़ाकी ख़ाक सूं रल जाना ।"
                ],
                "poetic_hindi": [
                    "जो गए सो गए, लौट न आए, मेरे प्राण-सखा प्यारे,",
                    "जिनका पल भर न कटता था बिन मेरे, क्यों आज हमें बिसारे ?",
                    "ख़ाकी ख़ाक स्युं रल जाणा !"
                ],
                "poetic_english": [
                    "Those who departed ne'er return, beloved companions of the heart;",
                    "Who could not live without me once, now dwell in silent graves apart.",
                    "Dust must dissolve in dust at last!"
                ]
            },
            {
                "original": [
                    "चित प्यार ना जाए साथों, उभ्भे साह ना रहन्दे,  ",
                    "असीं मोयां दे परले पार, ज्यूंद्यां दे विच बहन्दे,  ",
                    "ख़ाकी ख़ाक सूं (स्युं) रल जाना ।"
                ],
                "hindi_gloss": [
                    "चित (हृदय से उनका) प्यार (प्रेम) ना (नहीं) जाए (जाता) साथों (हमारे), उभ्भे (उखड़ती हुई) साह (गहरी सांसें/आहें) ना (नहीं) रहन्दे (रुकती हैं),",
                    "असीं (हम) मोयां (मृतकों) दे (के) परले (उस) पार (पार के हैं), ज्यूंद्यां (जीवितों) दे (के) विच (बीच) बहन्दे (बैठे रहते हैं) ।",
                    "ख़ाकी ख़ाक सूं रल जाना ।"
                ],
                "english_gloss": [
                    "चित (from heart) प्यार (love) ना (does not) जाए (depart) साथों (from us), उभ्भे (deep/gasping) साह (sighs) ना (not) रहन्दे (cease),",
                    "असीं (we) मोयां (of the dead) दे (of) परले (further) पार (shore belong), ज्यूंद्यां (among the living) दे (of) विच (within) बहन्दे (sit) ।",
                    "ख़ाकी ख़ाक सूं रल जाना ।"
                ],
                "poetic_hindi": [
                    "मन से उनका प्यार न छूटे, ठंडी सांसें भरते हैं,",
                    "हम मुर्दों के उस पार खड़े, जीवित के संग बैठते हैं !",
                    "ख़ाकी ख़ाक स्युं रल जाणा !"
                ],
                "poetic_english": [
                    "Their memory cannot fade away, sighing with heavy breath and slow;",
                    "Kin of the dead upon the brink, yet lingering with the living below.",
                    "Dust must dissolve in dust at last!"
                ]
            },
            {
                "original": [
                    "ओथे मगर प्यादे लग्गे, तां असीं एथे आए,  ",
                    "एथे सानूं रहन ना मिलदा, अग्गे कित वल धाए,  ",
                    "ख़ाकी ख़ाक सूं (स्युं) रल जाना ।"
                ],
                "hindi_gloss": [
                    "ओथे (वहाँ पूर्व जन्म में) मगर (पीछे) प्यादे (यम के दूत/कर्म-फल) लग्गे (लग गए थे), तां (तब) असीं (हम) एथे (यहाँ संसार में) आए (आए थे),",
                    "एथे (यहाँ भी) सानूं (हमें) रहन (स्थायी रहना) ना (नहीं) मिलदा (मिलता), अग्गे (आगे अब) कित (किस) वल (ओर) धाए (दौड़कर जाएं) ।",
                    "ख़ाकी ख़ाक सूं रल जाना ।"
                ],
                "english_gloss": [
                    "ओथे (there, in past realm) मगर (behind) प्यादे (messengers/guards) लग्गे (pursued), तां (so) असीं (we) एथे (here) आए (came),",
                    "एथे (here) सानूं (unto us) रहन (to stay) ना (not) मिलदा (is granted), अग्गे (ahead) कित (which) वल (way) धाए (should we flee) ।",
                    "ख़ाकी ख़ाक सूं रल जाना ।"
                ],
                "poetic_hindi": [
                    "वहाँ पीछे यमदूत लगे थे, तब हम भाग यहाँ पर आए,",
                    "यहाँ भी टिकना न मिला हमको, अब आगे कहाँ सिधाएं ?",
                    "ख़ाकी ख़ाक स्युं रल जाणा !"
                ],
                "poetic_english": [
                    "Pursued by bailiffs from that world, we fled and entered earthly space;",
                    "Yet here no abiding home is found—whither to run to seek our place?",
                    "Dust must dissolve in dust at last!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा एथे रहन ना मिलदा, रोंदे पिटदे चल्ले,  ",
                    "इको नाम ओसे दा ख़रची, पैसा होर ना पल्ले,  ",
                    "ख़ाकी ख़ाक सूं (स्युं) रल जाणा  ",
                    "ना कर ज़ोर धिङाना ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ला कहता है) एथे (यहाँ) रहन (रहना) ना (नहीं) मिलदा (मिलता), रोंदे (रोते-) पिटदे (पीटते सब) चल्ले (चल दिए),",
                    "इको (एकमात्र) नाम (प्रभु का पावन नाम ही) ओसे (उसका) दा (का) ख़रची (मार्ग-व्यय/पाथेय है), पैसा (सांसारिक धन) होर (अन्य कोई) ना (नहीं) पल्ले (साथ रहेगा),",
                    "ख़ाकी (मिट्टी) ख़ाक (मिट्टी में) स्युं (के साथ) रल (मिल) जाणा,",
                    "ना (मत) कर (कर) ज़ोर (अहंकार) धिङाना (अत्याचार/जबरदस्ती) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh says) एथे (here) रहन (to remain) ना (not) मिलदा (permitted), रोंदे (weeping) पिटदे (lamenting) चल्ले (all depart),",
                    "इको (only) नाम (the Holy Name) ओसे (of Him) दा (of) ख़रची (travel-fare/provision), पैसा (coin) होर (other) ना (none) पल्ले (in pocket),",
                    "ख़ाकी (dust) ख़ाक (with dust) स्युं (with) रल (merge) जाणा (must),",
                    "ना (do not) कर (commit) ज़ोर (oppression) धिङाना (coercion) ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा! यहाँ कोई टिक न पाया, रोते-पीटते सब प्रस्थान करें,",
                    "एक प्रभु-नाम ही मार्ग का पाथेय, धन-दौलत सब व्यर्थ धरें ।",
                    "माटी की देह माटी में मिलेगी, न कर ज़ोर-धिगाना कोई !"
                ],
                "poetic_english": [
                    "None can remain here, Bulleh knows; weeping and mourning all take flight;",
                    "His Name alone the journey’s fare, no earthly coin outlasts the night.",
                    "Dust must dissolve in dust at last, no pride nor tyranny avails!"
                ]
            }
        ],
        "philosophical_meaning": "सूफी परंपरा में मृत्यु का स्मरण (ज़िक्र-उल-मौत) आत्म-शुद्धि का सर्वोत्तम साधन है। मनुष्य मिट्टी से बना है और मिट्टी में ही विलीन होगा (कुरान: 'मिन्हा ख़लक़नाकुम व फ़ीहा नुईदुकुम')। संसार में जो व्यक्ति पद, बल और धन के नशे में 'ज़ोर-धिगाना' (अत्याचार) करते हैं, उनका अंत विनाश है। केवल ईश्वर का 'नाम' ही अंत समय में आत्मा की एकमात्र पूंजी है।"
    },
    {
        "id": 68,
        "title": "खेड लै विच वेहड़े घुंमी घुंम",
        "title_english": "Dance Spinning in the Courtyard!",
        "historical_context": "इस काफी में बुल्ले शाह नाथपंथी योग और सूफी अध्यात्म के देह-दर्शन को लोक-नृत्य (घूमर/घूमी-घूम) के रूपक में प्रस्तुत करते हैं। मानव देह वह 'वेहड़ा' (आंगन) है जिसमें नौ दरवाजे (इंद्रियां) हैं और दसवां गुप्त द्वार (दसम द्वार) है। साधक को मन रूपी मस्त हाथी को संयम की जंजीर से बांधकर आत्मिक आनंद में लीन होना चाहिए।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: खेड लै विच वेहड़े)",
        "raga": "राग भैरवी / सूही",
        "theme": "काया-योग, दसम द्वार, मन रूपी मस्त हाथी का संयम, आध्यात्मिक रास",
        "stanzas": [
            {
                "original": [
                    "खेड लै विच वेहड़े घुंमी घुंम ।"
                ],
                "hindi_gloss": [
                    "खेड (क्रीड़ा कर/नाच) लै (ले) विच (में) वेहड़े (हृदय रूपी आंगन में) घुंमी (घूम-) घुंम (घूम कर) ।"
                ],
                "english_gloss": [
                    "खेड (play/dance) लै (take) विच (in) वेहड़े (courtyard of the heart) घुंमी (spinning) घुंम (round and round) ।"
                ],
                "poetic_hindi": [
                    "नाच ले अंतर-आँगन माहीं, घूम-घूम कर मस्त कन्हाई !"
                ],
                "poetic_english": [
                    "Dance spinning in the courtyard round, where sacred ecstasy is found!"
                ]
            },
            {
                "original": [
                    "एस वेहड़े विच आला सोंहदा, आले दे विच ताकी  ",
                    "ताकी दे विच सेज विछावां, नाल पिया संग राती  ",
                    "एस वेहड़े दे नौं दरवाज़े, दसवां गुपत रखाती  ",
                    "योस गली दी मैं सार ना जानां, जहां आवे पिया जाती ।"
                ],
                "hindi_gloss": [
                    "एस (इस) वेहड़े (आंगन/काया) विच (में) आला (आला/दीपक रखने का ताक) सोंहदा (सुशोभित है), आले (ताक) दे (के) विच (अंदर) ताकी (झरोखा/गुप्त खिड़की),",
                    "ताकी (झरोखे) दे (के) विच (भीतर) सेज (प्रेम-शय्या) विछावां (बिछाती हूँ), नाल (साथ) पिया (प्रियतम के) संग (संग) राती (रात बिताने को),",
                    "एस (इस) वेहड़े (काया-आंगन) दे (के) नौं (नौ) दरवाज़े (प्रकट द्वार हैं), दसवां (दसवां द्वार) गुपत (गुप्त) रखाती (रखा हुआ है),",
                    "योस (उस दिव्य) गली (मार्ग) दी (का) मैं (मैं) सार (भेद) ना (नहीं) जानां (जानती), जहां (जहाँ से) आवे (आता) पिया (प्रियतम) जाती (जाता है) ।"
                ],
                "english_gloss": [
                    "एस (in this) वेहड़े (courtyard) विच (in) आला (alcove) सोंहदा (shines), आले (alcove) दे (of) विच (in) ताकी (window/shutter),",
                    "ताकी (window) दे (of) विच (in) सेज (bed) विछावां (I spread), नाल (with) पिया (Beloved) संग (beside) राती (by night),",
                    "एस (of this) वेहड़े (courtyard) दे (of) नौं (nine) दरवाज़े (gates), दसवां (the tenth) गुपत (secret) रखाती (is kept),",
                    "योस (of that) गली (lane) दी (of) मैं (I) सार (knowledge) ना (not) जानां (know), जहां (whence) आवे (comes) पिया (Beloved) जाती (goes) ।"
                ],
                "poetic_hindi": [
                    "इस आँगन में आला सोहे, आले में खिड़की प्यारी,",
                    "खिड़की में सेज बिछाऊँ, पिय संग रात बिताऊँ सारी ।",
                    "नौ दरवाज़े खुले देह के, दसवाँ गुप्त दुवारा,",
                    "उस गली की मैं सुध न जानूँ, जहाँ से आए पिय प्यारा !"
                ],
                "poetic_english": [
                    "Within this courtyard shines an alcove bright, with a secret casement set on high;",
                    "There spread I the bridal bed by night, beneath the Lover's starry sky.",
                    "Nine portals open to the worldly state, the tenth is veiled in mystic mystery;",
                    "Unknown to me that pathway and that gate, through which my Lord moves silently!"
                ]
            },
            {
                "original": [
                    "एस वेहड़े विच आला सोंहदा, आले दे विच ताकी  ",
                    "आपने पिया नूं याद करेसां, चरख़े दे हर फेरे  ",
                    "एस वेहड़े विच मकना हाथी, संगल नाल कहेड़े  ",
                    "बुल्ल्हे शाह फ़कीर साईं दा, जागद्यां कूं छेड़े ।  ",
                    "खेड लै विच वेहड़े घुंमी घुंम ।"
                ],
                "hindi_gloss": [
                    "एस (इस) वेहड़े (आंगन) विच (में) आला (आला) सोंहदा (शोभता है), आले (ताक) दे (के) विच (भीतर) ताकी (खिड़की है),",
                    "आपने (अपने) पिया (प्रियतम) नूं (को) याद (स्मरण) करेसां (करूँगी), चरख़े (चरखे) दे (के) हर (प्रत्येक) फेरे (चक्कर/श्वास पर),",
                    "एस (इस) वेहड़े (काया-आंगन) विच (में) मकना (मस्त/मदमस्त) हाथी (हाथी—अहंकारी मन), संगल (लोहे की जंजीर) नाल (से) कहेड़े (बाँध रखा है),",
                    "बुल्ल्हे (बुल्ले) शाह (शाह) फ़कीर (फकीर) साईं (प्रभु) दा (का), जागद्यां (जागृत साधकों) कूं (को) छेड़े (जगाता/प्रेरित करता है) ।",
                    "खेड लै विच वेहड़े घुंमी घुंम ।"
                ],
                "english_gloss": [
                    "एस (in this) वेहड़े (courtyard) विच (in) आला (alcove) सोंहदा (shines), आले (alcove) दे (of) विच (in) ताकी (window),",
                    "आपने (my own) पिया (Beloved) नूं (unto) याद (remember) करेसां (I will), चरख़े (of spinning wheel) दे (of) हर (every) फेरे (revolution/turn),",
                    "एस (in this) वेहड़े (courtyard) विच (in) मकना (rogue/rutting) हाथी (elephant—mind), संगल (chains) नाल (with) कहेड़े (bound fast),",
                    "बुल्ल्हे (Bulleh) शाह (Shah) फ़कीर (dervish) साईं (of the Lord) दा (of), जागद्यां (the wakeful souls) कूं (unto) छेड़े (prods/inspires) ।",
                    "खेड लै विच वेहड़े घुंमी घुंम ।"
                ],
                "poetic_hindi": [
                    "अपने पिया को याद करूँगी चरखे के हर फेरे,",
                    "इस आँगन में मतवाला हाथी, जंजीरों ने घेरे ।",
                    "बुल्ल्हे शाह साँईं का साधक, जाग्रत मन को छेड़े,",
                    "नाच ले अंतर-आँगन माहीं, घूम-घूम कर मस्त कन्हाई !"
                ],
                "poetic_english": [
                    "At every turning of the spinning wheel, I keep the memory of my Love awake;",
                    "A wild rut elephant in chains must kneel, within this yard for truth's celestial sake.",
                    "Bulleh the dervish of the King on high, prods wakeful souls until the day is won:",
                    "Dance spinning in the courtyard round, beneath the spirit’s rising sun!"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी नाथ-योग और सूफी रहस्यवाद का अद्वितीय समन्वय है। शरीर के नौ द्वार (दो आँखें, दो कान, दो नथुने, मुख, गुदा, जननेन्द्रिय) बाह्य संसार से जुड़े हैं; दसवां द्वार (दसम द्वार / ब्रह्मरंध्र) परमात्मा के मिलन का गुप्त स्थान है। 'मकना हाथी' अनियंत्रित अहंकार व काम-वासना का प्रतीक है, जिसे वैराग्य व नाम-स्मरण की 'संगल' (जंजीर) से बांधना आवश्यक है।"
    },
    {
        "id": 69,
        "title": "की बेदरदां संग यारी",
        "title_english": "What Avails Friendship With The Heartless?",
        "historical_context": "इस काफी में बुल्ले शाह उन सांसारिक व कपटी प्रेमियों से संबंध जोड़ने का पश्चाताप व्यक्त करते हैं जो विरह का तीर कलेजे में गाड़कर हँसते-हँसते चले जाते हैं। यह काफी मुहावरों ('चिड़ियों की मौत, गवारों का हासा') और मार्मिक बिम्बों से अलंकृत है। अंत में साधक समझता है कि सच्चा प्रेम केवल परमात्मा से ही हो सकता है, नश्वर प्राणियों से प्रेम तो विष का प्याला पीने जैसा है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, तुक: यारी / ज़ारी / हैंस्यारी / बपारी)",
        "raga": "राग तिलंग / सोरठ",
        "theme": "सांसारिक प्रेम की निस्सारता, विश्वासघात, विरह का विष, सच्चा प्रेम ईश्वर से",
        "stanzas": [
            {
                "original": [
                    "की बेदरदां संग यारी,  ",
                    "रोवन अक्खियां ज़ारो ज़ारी ।"
                ],
                "hindi_gloss": [
                    "की (क्या लाभ) बेदरदां (निष्ठुरों/कठोर-हृदय वालों के) संग (साथ) यारी (प्रेम/मित्रता करने से),",
                    "रोवन (रोती हैं) अक्खियां (मेरी आँखें) ज़ारो (फूट-) ज़ारी (फूटकर) ।"
                ],
                "english_gloss": [
                    "की (what avails) बेदरदां (the heartless) संग (with) यारी (friendship/love),",
                    "रोवन (weep) अक्खियां (my eyes) ज़ारो (bitterly) ज़ारी (in endless streams) ।"
                ],
                "poetic_hindi": [
                    "क्या निष्ठुर से प्रीत लगाई, आँखें रोतीं ज़ारो-ज़ारी !"
                ],
                "poetic_english": [
                    "What profits love with heartless folk? My weeping eyes shed bitter streams!"
                ]
            },
            {
                "original": [
                    "सानूं गए बेदरदी चड्ड के, हिजरे सांग सीने विच गड्ड के,  ",
                    "जिसमों जिन्द नूं लै गए कढ्ढ के, इह गल्ल कर गए हैंस्यारी ।  ",
                    "की बेदरदां संग यारी,"
                ],
                "hindi_gloss": [
                    "सानूं (हमें) गए (चले गए) बेदरदी (वे निष्ठुर) चड्ड (छोड़) के (कर), हिजरे (विरह का) सांग (भाला/बरछी) सीने (हृदय) विच (में) गड्ड (गाड़) के (कर),",
                    "जिसमों (शरीर में से) जिन्द (प्राणों) नूं (को) लै (ले) गए (गए) कढ्ढ (निकाल) के (कर), इह (यह) गल्ल (काम) कर (कर) गए (गए) हैंस्यारी (हंसी उड़ाने/कपटपूर्ण) ।",
                    "की बेदरदां संग यारी,"
                ],
                "english_gloss": [
                    "सानूं (us) गए (went) बेदरदी (the cruel one) चड्ड (leaving) के (having), हिजरे (of separation) सांग (spear) सीने (in chest) विच (in) गड्ड (plunging) के (having),",
                    "जिसमों (from body) जिन्द (life/soul) नूं (unto) लै (took) गए (away) कढ्ढ (extracting) के (having), इह (this) गल्ल (deed) कर (done) गए (went) हैंस्यारी (mocking/heartless) ।",
                    "की बेदरदां संग यारी,"
                ],
                "poetic_hindi": [
                    "छोड़ गए निर्मोही मुझको, विरह का भाला सीने गाड़ा,",
                    "तन से प्राण निकाल ले गए, करके यह उपहास हमारा !"
                ],
                "poetic_english": [
                    "The heartless left me in my pain, plunging grief's spear deep in my breast;",
                    "Tearing the soul from flesh in vain, making my misery their jest!"
                ]
            },
            {
                "original": [
                    "बेदरदां दा की भरवासा, खौफ़ नहीं दिल अन्दर मासा,  ",
                    "चिड़ियां मौत गवारां हासा, मगरों हस्स हस्स ताड़ी मारी ।  ",
                    "की बेदरदां संग यारी,"
                ],
                "hindi_gloss": [
                    "बेदरदां (कठोर-हृदय वालों का) दा (का) की (क्या) भरवासा (भरोसा/विश्वास), खौफ़ (ईश्वर का भय) नहीं (नहीं है) दिल (उनके हृदय के) अन्दर (भीतर) मासा (माशा-भर भी),",
                    "चिड़ियां (चिड़ियों की) मौत (मृत्यु हो जाती है और) गवारां (मूर्खों का) हासा (मनोरंजन/हंसी होती है), मगरों (पीछे से) हस्स (हँस-) हस्स (हँसकर) ताड़ी (ताली) मारी (बजाते हैं) ।",
                    "की बेदरदां संग यारी,"
                ],
                "english_gloss": [
                    "बेदरदां (of the cruel) दा (of) की (what) भरवासा (trust), खौफ़ (fear of God) नहीं (none) दिल (heart) अन्दर (within) मासा (an iota),",
                    "चिड़ियां (to sparrows) मौत (death) गवारां (to rustics) हासा (sport/laughter), मगरों (behind) हस्स (laughing) हस्स (laughing) ताड़ी (clapping hands) मारी (struck) ।",
                    "की बेदरदां संग यारी,"
                ],
                "poetic_hindi": [
                    "क्या विश्वास करें निष्ठुर का, दिल में रत्ती-भर न दया,",
                    "चिड़ियों की तो मौत हुई, और गँवारों का हास्य बना !"
                ],
                "poetic_english": [
                    "What trust can rest in callous men, devoid of fear of God or right?",
                    "Death to the bird is sport to them, who clap their hands in mock delight!"
                ]
            },
            {
                "original": [
                    "आवन कह गए फेर ना आए, आवन दे सभ कौल भुलाए,  ",
                    "मैं भुल्ली भुल्ल नैन लगाए, केहे मिले सानूं ठग्ग बपारी ।  ",
                    "की बेदरदां संग यारी,"
                ],
                "hindi_gloss": [
                    "आवन (लौट आने की) कह (कह) गए (गए थे) फेर (पुनः) ना (नहीं) आए (आए), आवन (आने के) दे (के) सभ (समस्त) कौल (वचन/प्रतिज्ञाएं) भुलाए (भुला दिए),",
                    "मैं (मैं) भुल्ली (भूल में पड़कर) भुल्ल (भूल से) नैन (नेत्र) लगाए (लगा बैठी), केहे (कैसे कपटी) मिले (मिल गए) सानूं (हमें) ठग्ग (ठग) बपारी (व्यापारी) ।",
                    "की बेदरदां संग यारी,"
                ],
                "english_gloss": [
                    "आवन (to return) कह (saying) गए (went) फेर (again) ना (never) आए (came), आवन (of returning) दे (of) सभ (all) कौल (promises) भुलाए (forgot),",
                    "मैं (I) भुल्ली (deluded) भुल्ल (by error) नैन (eyes) लगाए (attached), केहे (what kind of) मिले (met) सानूं (unto us) ठग्ग (swindler) बपारी (traders) ।",
                    "की बेदरदां संग यारी,"
                ],
                "poetic_hindi": [
                    "आने को कह कर गए, न आए, सारे वचन भुलाए रे,",
                    "भूल गई मैं नैन लगा कर, ठग-व्यापारी पाए रे !"
                ],
                "poetic_english": [
                    "Pledging return they went away, all promises forgotten quite;",
                    "Blind was my heart to yield that day, to swindlers trading in the night!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हे शाह इक सौदा कीता, पीता ज़हर प्याला पीता,  ",
                    "ना कुझ नफ़ा ना टोटा लीता, दरद दुक्खां दी गठड़ी भारी ।  ",
                    "की बेदरदां संग यारी,  ",
                    "रोवन अक्खियां ज़ारो ज़ारी ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हे (बुल्ले) शाह (शाह ने) इक (एक ऐसा) सौदा (व्यापार) कीता (किया), पीता (पी लिया) ज़हर (हलाहल विष का) प्याला (प्याला) पीता (पी डाला),",
                    "ना (न) कुझ (कुछ) नफ़ा (लाभ पाया) ना (न केवल) टोटा (घाटा) लीता (उठाया), दरद (दर्द और) दुक्खां (दुखों) दी (की) गठड़ी (पोटली) भारी (भारी सिर पर ले ली) ।",
                    "की बेदरदां संग यारी, रोवन अक्खियां ज़ारो ज़ारी ।"
                ],
                "english_gloss": [
                    "बुल्ल्हे (Bulleh) शाह (Shah) इक (one) सौदा (bargain) कीता (made), पीता (drank) ज़हर (of poison) प्याला (chalice) पीता (drank deep),",
                    "ना (neither) कुझ (any) नफ़ा (profit) ना (nor mere) टोटा (loss) लीता (took), दरद (of pain) दुक्खां (sorrows) दी (of) गठड़ी (bundle) भारी (heavy) ।",
                    "की बेदरदां संग यारी, रोवन अक्खियां ज़ारो ज़ारी ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हे शाह ने सौदा कीना, ज़हर-प्याला पी डाला,",
                    "नफ़ा-टोटा कुछ न पाया, सिर पर दुखों का बोझ सँभाला !",
                    "क्या निष्ठुर से प्रीत लगाई, आँखें रोतीं ज़ारो-ज़ारी !"
                ],
                "poetic_english": [
                    "Bulleh Shah made a bargain sore, drinking the poisoned cup of gall;",
                    "No profit gained for evermore, but heavy loads of grief withal.",
                    "What profits love with heartless folk? My weeping eyes shed bitter streams!"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी सांसारिक संबंधों की नश्वरता और धोखे पर कड़ा प्रहार करती है। सूफी साधक जब नश्वर जीवों में ईश्वरीय निष्ठा खोजता है, तो उसे केवल उपहास और पीड़ा मिलती है। 'चिड़ियों की मौत, गवारों का हासा' लोक-कहावत के माध्यम से बुल्ले शाह समझाते हैं कि संसार साधक की आध्यात्मिक तड़प को नहीं समझ सकता। इसलिए मन को केवल शाश्वत ईश्वर की ओर ही मोड़ना चाहिए।"
    },
    {
        "id": 70,
        "title": "कीहनूं ला-मकानी दस्सदे हो",
        "title_english": "Whom Art Thou Telling Thou Art Spaceless?",
        "historical_context": "यह बुल्ले शाह की अद्वैत वेदांत और सूफी 'वह्दत-उल-वजूद' (अस्तित्व की एकता) की चरम क्रांतिकारी काफी है। जब मुल्ला और दार्शनिक ईश्वर को 'ला-मकान' (स्थान-रहित / अगम्य / शून्य) बताते हैं, तो बुल्ले शाह ईश्वर को ललकार कर कहते हैं: 'किसे धोखा दे रहे हो? तुम तो सृष्टि के प्रत्येक रूप और रंग में स्वयं प्रत्यक्ष होकर नाच रहे हो!' आदम, मंसूर, सिकंदर, यूसुफ, रूमी, ज़ंगी, फिरंगी—इन सब में ईश्वर ही लीला कर रहा है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: कीहनूं ला-मकानी दस्सदे हो)",
        "raga": "राग काफी / बहार",
        "theme": "वह्दत-उल-वजूद, ईश्वर की सर्वव्यापकता, ला-मकान का खंडन, बहुविध रूपों में एक परमात्मा",
        "stanzas": [
            {
                "original": [
                    "कीहनूं ला-मकानी दस्सदे हो ।  ",
                    "तुसीं हर रंग दे विच वस्सदे हो ।"
                ],
                "hindi_gloss": [
                    "कीहनूं (किसे) ला-मकानी (स्थान-रहित/अगम्य-अगोचर) दस्सदे (बताते) हो (हो) ।",
                    "तुसीं (तुम तो) हर (प्रत्येक) रंग (रूप-रंग) दे (के) विच (भीतर) वस्सदे (बसते) हो (हो) ।"
                ],
                "english_gloss": [
                    "कीहनूं (unto whom) ला-मकानी (spaceless/unmanifest/placeless) दस्सदे (claimest) हो (art Thou) ।",
                    "तुसीं (Thou) हर (in every) रंग (hue/manifestation) दे (of) विच (within) वस्सदे (dwellest) हो (art) ।"
                ],
                "poetic_hindi": [
                    "किसे बताते हो तुम खुद को स्थान-हीन अगोचर श्याम ?",
                    "तुम तो हर इक रंग में बसते, जग में फैला तुम्हारा धाम !"
                ],
                "poetic_english": [
                    "Whom art Thou telling Thou art spaceless, Lord? In every hue Thou art manifested and adored!"
                ]
            },
            {
                "original": [
                    "कुनफईकून तैं आप कहाआ, तैं बाझों होर केहड़ा आया,  ",
                    "इश्कों सभ ज़हूर बणाइआ, आशक हो के वस्सदे हो ।  ",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "hindi_gloss": [
                    "कुनफईकून (सृष्टि की आदि आज्ञा: 'कुन फ़-यकून'—हो जा, और वह हो गया) तैं (तूने) आप (स्वयं) कहाआ (कहा), तैं (तेरे) बाझों (बिना) होर (अन्य) केहड़ा (कौन) आया (प्रकट हुआ),",
                    "इश्कों (अपने ही प्रेम से) सभ (समस्त) ज़हूर (सृष्टि का प्रकटीकरण) बणाइआ (बनाया), आशक (स्वयं प्रेमी) हो (बन-) के (कर) वस्सदे (बसते) हो (हो) ।",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "english_gloss": [
                    "कुनफईकून ('Be and it is'—the primal fiat) तैं (Thou) आप (Thyself) कहाआ (spakest), तैं (Thee) बाझों (except) होर (else) केहड़ा (who) आया (arrived),",
                    "इश्कों (from Love alone) सभ (all) ज़हूर (manifest creation) बणाइआ (fashioned), आशक (as the lover) हो (becoming) के (having) वस्सदे (dwellest) हो (Thou) ।",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "poetic_hindi": [
                    "'कुन-फ़यकून' का बोल उचारा, तेरे बिन कौन यहाँ आया ?",
                    "प्रेम से सारी सृष्टि सजाई, खुद आशिक बन कर छाया !"
                ],
                "poetic_english": [
                    "'Be and it is'—Thou spakest the primal word, who else but Thee within this realm was stirred?",
                    "From Love alone this universe did rise, where Thou Thyself art lover in disguise!"
                ]
            },
            {
                "original": [
                    "पुच्छो आदम किस ने आंदा ए किथों आया कित्थे जांदा ए,  ",
                    "ओथे किस दा तैनूं लांहजा ए ओथे खा दाना उठ नस्सदे हो ।  ",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "hindi_gloss": [
                    "पुच्छो (पूछो) आदम (आदम को) किस (किसने) ने (ने) आंदा (यहाँ उतारा) ए (है), किथों (कहाँ से) आया (आया है) कित्थे (कहाँ) जांदा (जाता) ए (है),",
                    "ओथे (वहाँ स्वर्ग में) किस (किसका) दा (का) तैनूं (तुझको) लांहजा (उलाहना/भय) ए (है), ओथे (वहाँ) खा (खाकर) दाना (गेहूं का दाना) उठ (उठकर) नस्सदे (भागते) हो (हो) ।",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "english_gloss": [
                    "पुच्छो (ask) आदम (Adam) किस (who) ने (has) आंदा (brought) ए (has), किथों (whence) आया (came) कित्थे (whither) जांदा (goes) ए (does),",
                    "ओथे (there in Eden) किस (whose) दा (of) तैनूं (unto Thee) लांहजा (rebuke/reproach) ए (is), ओथे (there) खा (eating) दाना (the forbidden grain) उठ (rising) नस्सदे (fleest) हो (Thou) ।",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "poetic_hindi": [
                    "पूछो आदम को किसने रचाया, कहाँ से आया, कहाँ को धाया ?",
                    "स्वर्ग में किसका भय था तुझको, गेहूँ खा कर क्यों भाग आया ?"
                ],
                "poetic_english": [
                    "Inquire of Adam who hath placed him here, whence did he come, whither his course to steer?",
                    "Whose censure fearedst Thou in Eden’s shade, that tasting wheat Thou fleddest dismayed?"
                ]
            },
            {
                "original": [
                    "आपे सुने ते आप सुणावें, आपे गावें आप बजावें,  ",
                    "हक्कों कौल सरोद सुणावें, किते जाहल हो के नस्सदे हो ।  ",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "hindi_gloss": [
                    "आपे (स्वयं ही) सुने (सुनता है) ते (और) आप (स्वयं ही) सुणावें (सुनाता है), आपे (स्वयं ही) गावें (गाता है) आप (स्वयं) बजावें (वाद्य बजाता है),",
                    "हक्कों (परम सत्य के) कौल (वचन और) सरोद (राग) सुणावें (सुनाता है), किते (कहीं पर) जाहल (मूर्ख/अज्ञानी) हो (बन-) के (कर) नस्सदे (भागता) हो (है) ।",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "english_gloss": [
                    "आपे (Thyself) सुने (hearest) ते (and) आप (Thyself) सुणावें (makest heard), आपे (Thyself) गावें (singest) आप (Thyself) बजावें (playest),",
                    "हक्कों (from the Truth) कौल (words) सरोद (melodies) सुणावें (chantest), किते (somewhere) जाहल (an ignorant fool) हो (becoming) के (having) नस्सदे (fleest) हो (Thou) ।",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "poetic_hindi": [
                    "आप ही सुने, आप ही सुनावे, आप ही गावे, आप बजावे,",
                    "सत्य के पावन राग सुनावे, कहीं अज्ञानी बन भाग जावे !"
                ],
                "poetic_english": [
                    "Thou art the listener and the singer too, playing the harp and singing what is true;",
                    "Chanting the sacred song with holy grace, yet playing the fool in some dark, earthly place!"
                ]
            },
            {
                "original": [
                    "तेरी वहदत तूएं पुचावें, अनलहक्क दी तार मिलावें,  ",
                    "सूली ते मनसूर चढ़ावें, ओथे कोल खलो के हस्सदे हो ।  ",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "hindi_gloss": [
                    "तेरी (तेरी ही) वहदत (अद्वैत/एकेश्वरवाद की अनुभूति) तूएं (तू स्वयं ही) पुचावें (हृदय तक पहुंचाता है), अनलहक्क ('अहं ब्रह्मास्मि' / मैं ही सत्य हूँ) दी (की) तार (तान/सुर) मिलावें (मिलाता है),",
                    "सूली (सूली) ते (पर) मनसूर (मंसूर को) चढ़ावें (चढ़ाता है), ओथे (वहाँ) कोल (पास) खलो (खड़े हो-) के (कर) हस्सदे (हंसता) हो (है) ।",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "english_gloss": [
                    "तेरी (Thy) वहदत (Unity) तूएं (Thou Thyself) पुचावें (bringest to heart), अनलहक्क ('I am the Truth') दी (of) तार (chords) मिलावें (tunest),",
                    "सूली (upon the cross) ते (upon) मनसूर (Mansur) चढ़ावें (raisen), ओथे (there) कोल (beside) खलो (standing) के (having) हस्सदे (smilest) हो (Thou) ।",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "poetic_hindi": [
                    "तू ही अद्वैत का भेद सिखावे, 'अन-अल-हक' की तार मिलावे,",
                    "मंसूर को सूली पर चढ़ा कर, पास खड़े हो कर मुस्कावे !"
                ],
                "poetic_english": [
                    "Thy Unity Thou makest the heart proclaim, tuning the chord of 'I am God' in flame;",
                    "Thou mountest Mansur on the gallows tree, and smilest beside him in sweet ecstasy!"
                ]
            },
            {
                "original": [
                    "जिवें सिकन्दर तरफ नौशाबां, हो रसूल लै आया किताबां,  ",
                    "यूसफ़ हो के अन्दर खुआबां, ज़ुलैखां दा दिल खस्सदे हो ।  ",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "hindi_gloss": [
                    "जिवें (जैसे) सिकन्दर (सिकंदर महान) तरफ (की ओर) नौशाबां (रानी नौशाबा के प्रेम में दूत बना), हो (होकर) रसूल (पैगंबर) लै (लेकर) आया (आया) किताबां (दिव्य ग्रंथ),",
                    "यूसफ़ (यूसुफ का अप्रतिम रूप) हो (बन-) के (कर) अन्दर (में) खुआबां (सपनों), ज़ुलैखां (महारानी ज़ुलैखा) दा (का) दिल (हृदय) खस्सदे (छीनते/लूटते) हो (हो) ।",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "english_gloss": [
                    "जिवें (as) सिकन्दर (Alexander) तरफ (unto) नौशाबां (Queen Naushaba), हो (becoming) रसूल (Messenger) लै (bringing) आया (came) किताबां (scriptures),",
                    "यूसफ़ (Joseph) हो (becoming) के (having) अन्दर (within) खुआबां (dreams), ज़ुलैखां (Zulaikha’s) दा (of) दिल (heart) खस्सदे (steals) हो (Thou) ।",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "poetic_hindi": [
                    "सिकंदर बन नौशाबा की ओर धाया, पैगंबर बन कर ग्रंथ लाया,",
                    "यूसुफ़ बन कर सपनों में आकर, ज़ुलैखा का मन चुराया !"
                ],
                "poetic_english": [
                    "As Alexander seeking Queen Naushaba, as holy prophets bearing sacred lore;",
                    "As Joseph appearing in Zulaikha's dreams, stealing her heart for evermore!"
                ]
            },
            {
                "original": [
                    "किते रूमी हो किते ज़ंगी हो, किते टोपी पोश फ़रंगी हो,  ",
                    "किते मै-ख़ाने विच भंगी हो, किते मेहर महरी बण वसदे हो ।  ",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "hindi_gloss": [
                    "किते (कहीं पर) रूमी (गोरे तुर्क/रूमी) हो (हो), किते (कहीं पर) ज़ंगी (हब्शी/काले अफ्रीकी) हो (हो), किते (कहीं) टोपी (टोपी) पोश (पहनने वाले) फ़रंगी (यूरोपीय/फिरंगी) हो (हो),",
                    "किते (कहीं) मै-ख़ाने (मदिरालय) विच (में) भंगी (मस्त फकीर/भांग पीने वाले) हो (हो), किते (कहीं पर) मेहर (ग्राम-प्रधान) महरी (उनकी पत्नियां) बण (बनकर) वसदे (बसते) हो (हो) ।",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "english_gloss": [
                    "किते (somewhere) रूमी (fair Turk/Roman) हो (art), किते (somewhere) ज़ंगी (dark Ethiopian/Zangi) हो (art), किते (somewhere) टोपी (hat) पोश (wearing) फ़रंगी (European/Westerner) हो (art),",
                    "किते (somewhere) मै-ख़ाने (in tavern) विच (in) भंगी (hemp-intoxicated mystic) हो (art), किते (somewhere) मेहर (chieftain) महरी (chieftainess) बण (becoming) वसदे (dwellest) हो (Thou) ।",
                    "कीहनूं ला-मकानी दस्सदे हो ।"
                ],
                "poetic_hindi": [
                    "कहीं रूमी, कहीं ज़ंगी तुम, कहीं टोपी-पोश फिरंगी तुम,",
                    "मदिरालय में मतवाले भंगी, कहीं राजा-रानी बन बसते तुम !"
                ],
                "poetic_english": [
                    "In Rome Thou art fair, in Zanzibar dark; wearing the hat of the Frank abroad;",
                    "A wandering mendicant drunk in the tavern, or prince and princess ruling as lord!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु इनायत आरफ़ है, उह दिल मेरे दा वारस है,  ",
                    "मैं लोहा ते उह पारस है, तुसीं ओसे दे संग खस्सदे हो ।  ",
                    "कीहनूं ला-मकानी दस्सदे हो ।  ",
                    "तुसीं हर रंग दे विच वस्सदे हो ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ले का) शहु (प्रभु) इनायत (शाह इनायत) आरफ़ (परम तत्वज्ञानी/आरिफ) है, उह (वह) दिल (हृदय) मेरे (मेरे) दा (का) वारस (स्वामी/अधिपति) है,",
                    "मैं (मैं) लोहा (लोहा हूँ) ते (और) उह (वह) पारस (पारसमणि) है, तुसीं (तुम प्रभु) ओसे (उसी मुर्शिद) दे (के) संग (साथ) खस्सदे (मुस्कराते/लीला करते) हो ।",
                    "कीहनूं ला-मकानी दस्सदे हो, तुसीं हर रंग दे विच वस्सदे हो ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh’s) शहु (Lord) इनायत (Shah Inayat) आरफ़ (the Knower/Gnostic) है (is), उह (he) दिल (heart) मेरे (my) दा (of) वारस (master/owner) है (is),",
                    "मैं (I am) लोहा (iron) ते (and) उह (he is) पारस (the philosopher's stone) है (is), तुसीं (Thou, O God) ओसे (with him) दे (of) संग (along with) खस्सदे (playest/smilest) हो (Thou) ।",
                    "कीहनूं ला-मकानी दस्सदे हो, तुसीं हर रंग दे विच वस्सदे हो ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा शौह! शाह इनायत आरिफ़, मेरे दिल का स्वामी वह,",
                    "मैं लोहा, वह पारस-मणि है, उसके संग मिल मुस्काते तुम !",
                    "किसे बताते हो तुम खुद को स्थान-हीन अगोचर श्याम ?",
                    "तुम तो हर इक रंग में बसते, जग में फैला तुम्हारा धाम !"
                ],
                "poetic_english": [
                    "Bulleh's Lord is Shah Inayat, the Knower, sole Master of this heart in me;",
                    "I am base iron, he the touchstone gold, where Thou dost reveal Thine ecstasy!",
                    "Whom art Thou telling Thou art spaceless, Lord?",
                    "In every hue Thou art manifested and adored!"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी इब्न अरबी के 'वह्दत-उल-वजूद' और श्रीमद्भगवद्गीता के 'विश्वरूप दर्शन' का सूफी रूपांतरण है। ईश्वर किसी सातवें आसमान पर बैठा अमूर्त सत्ता नहीं है, बल्कि वह स्वयं दृश्यमान जगत का प्रत्येक कण, प्रत्येक जाति, प्रत्येक व्यक्ति और प्रत्येक मनोभाव बनकर प्रकट हो रहा है। 'रूमी, ज़ंगी, फिरंगी' कहकर बुल्ले शाह समस्त जातीय और धार्मिक सीमाओं को भस्म कर देते हैं।"
    }
]

new_lexicon_terms = {
    "लारे": {"hindi": "झूठे बहाने, टालमटोल, झूठे आश्वासन", "english": "false promises, excuses, evasions"},
    "सुनेहा": {"hindi": "संदेश, समाचार", "english": "message, tidings"},
    "औझड़": {"hindi": "बीहड़, भयानक घना जंगल", "english": "wild, rugged, pathless wilderness"},
    "ख़ाकी": {"hindi": "मिट्टी का बना हुआ, पार्थिव शरीर", "english": "earth-born, fashioned of dust"},
    "धिङाना": {"hindi": "अन्याय, ज़बरदस्ती, ज़ुल्म", "english": "coercion, high-handed oppression, tyranny"},
    "खर्ची": {"hindi": "यात्रा का मार्ग-व्यय, पाथेय", "english": "travel provisions, journey fare"},
    "ताकी": {"hindi": "खिड़की, झरोखा", "english": "small window, shuttered opening"},
    "मकना हाथी": {"hindi": "मस्त हाथी, विशाल हाथी जिसके दांत न हों; रूपक में: मदमस्त मन", "english": "tuskless large rutting elephant; metaphorically: uncontrolled ego-mind"},
    "संगल": {"hindi": "लोहे की जंजीर, सांकल", "english": "iron chain, fetter"},
    "सांग": {"hindi": "बरछी, भाला", "english": "spear, javelin"},
    "ला-मकानी": {"hindi": "स्थान-रहित, देश-कालातीत, अगम्य निराकार", "english": "spaceless, placeless, transcending physical location"},
    "कुनफईकून": {"hindi": "कुरान का वाक्य: 'कुन फ़-यकून' (हो जा और वह हो गया)", "english": "the divine creative fiat: 'Be, and it is'"},
    "आरफ़": {"hindi": "आरिफ, परम तत्ववेत्ता, ब्रह्मज्ञानी", "english": "Arif, gnostic, knower of divine truth"}
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
        "completed_count": 70,
        "total": 160,
        "next_kafi_id": 71,
        "last_updated": "2026-10-17T17:10:00+05:30",
        "last_batch": "66-70",
        "status": "in_progress"
    }
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print(f"Checkpoint updated: 70/160 completed. Next ID: 71")

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
