"""
Process Batch 141 to 145 of Bulleh Shah's Kafian.
Kafi 141: तांघ माही दी जलियां (Burning in Yearning for the Herdsman Beloved)
Kafi 142: बहुड़ीं वे तबीबा मैंडी जिन्द गईआ / तेरे इश्क नचाइआ (Heal Me, O Divine Physician! Thy Love Has Made Me Dance)
Kafi 143: टूने कामन करके नी मैं प्यारा यार मनावांगी (Through Spells and Incantations I Shall Win My Beloved)
Kafi 144: तूं किधरों आया किधर जाणा, आपना दस्स टिकाणा (Whence Have You Come, Whither Shall You Go? Declare Your Abode)
Kafi 145: तूं नहीउं मैं नाहीं वे सज्जणा, तूं नहीउं मैं नाहीं (Neither Art Thou, Nor Am I, O Beloved!)
"""

import json
import os

DATA_DIR = os.path.abspath("c:/my-code/Bulleh-Shah/data")
KAFIAN_DIR = os.path.join(DATA_DIR, "kafian")
LEXICON_PATH = os.path.join(DATA_DIR, "punjabi_sufi_lexicon.json")
CHECKPOINT_PATH = os.path.join(DATA_DIR, "checkpoint.json")

batch_kafian = [
    {
        "id": 141,
        "title_punjabi": "तांघ माही दी जलियां",
        "title_english": "Burning in Yearning for the Herdsman Beloved",
        "raga": "Raga Marwa / Tilang",
        "meter": "Matrik Chhand (16-11 matras)",
        "theme": "Sohni's Night Crossing of the Swirling Chenab as the Soul's Perilous Voyage to God",
        "historical_context": "Rooted in the indigenous Punjabi romance of Sohni-Mahiwal, Bulleh Shah transposes Sohni's nocturnal swim across the torrential river Chenab into the soul's perilous transit across the ocean of worldly delusion (Samsara). Lacking money, boats, or swimming skills ('मैं मनतारू'), the seeker stands on the riverbank under midnight stars ('अद्धी रात लटकदे तारे'), driven solely by the searing agony of separation ('तांघ माही दी').",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "तांघ माही दी जलियां,  ",
                    "नित्त काग उडावां खलियां ।"
                ],
                "hindi_gloss": "तांघ (तीव्र तड़प/विरह) माही (माहीवाल/प्रियतम) दी (की आग में) जलियां (जल रही हूँ), नित्त (प्रतिदिन/निरंतर) काग (मुंडेर पर बैठे कौवे को) उडावां (उड़ाती हूँ) खलियां (खड़ी-खड़ी प्रियतम के संदेश की प्रतीक्षा में)।",
                "english_gloss": "तांघ (In burning yearning) माही दी (for my herdsman Beloved) जलियां (I am consumed with fire), नित्त (constantly) काग उडावां (I shoo away the crow) खलियां (standing in wait for news of His arrival).",
                "poetic_hindi": "माही की तड़प में जलती हूँ,\nखड़ी नित्य मैं काग उड़ाती हूँ!",
                "poetic_english": "In yearning for my Love I burn,\nAnd shoo the crows for His return!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "कउडी दमड़े पल्ले ना काई, पार वंञन नूं मैं सधराई,  ",
                    "नाल मलाहां दे नहीं आशनाई, झेड़ा करां वलल्लियां ।  ",
                    "तांघ माही दी जलियां ।"
                ],
                "hindi_gloss": "कउडी (फूटी कौड़ी) दमड़े (या कोई सिक्का/धन) पल्ले (मेरी झोली में) ना काई (कुछ भी नहीं है), पार (नदी पार) वंञन नूं (जाने की) मैं (मुझमें) सधराई (तीव्र लालसा भरी है), नाल (साथ) मलाहां दे (नाविकों के) नहीं (नहीं है) आशनाई (कोई परिचय या मैत्री), झेड़ा (विवाद/अनुनय) करां (करती हूँ) वलल्लियां (दीवानी/नादान होकर)।",
                "english_gloss": "कउडी दमड़े (Neither copper penny nor coin) पल्ले ना काई (is in my hem), पार वंञन नूं (to cross over to the far bank) मैं सधराई (I yearn with all my heart), नाल मलाहां दे (with the ferrymen) नहीं आशनाई (I have no acquaintance or friendship), झेड़ा करां (I plead and quarrel) वलल्लियां (like a distraught madwoman).",
                "poetic_hindi": "कौड़ी-दमड़ी पल्ले नाहीं, पार उतरने की सुधि छाई,\nमल्लाहों से नहीं सगाई, झगड़ूँ बावली होकर माई!\nमाही की तड़प में जलती हूँ!",
                "poetic_english": "No penny lingers in my dress, yet for the far shore I profess;\nNo ferryman heeds my distress, I plead in wild unguidedness!\nIn yearning for my Love I burn!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "नै चन्दल दे शोर किनारे, घुंमन घेर विच ठाठां मारे,  ",
                    "डुब्ब डुब्ब मोए भारे, जे शोर करां तां झल्लियां ।  ",
                    "तांघ माही दी जलियां ।"
                ],
                "hindi_gloss": "नै (नदी) चन्दल/चनाब (चनाब नदी) दे (के) शोर (उमड़ते हुए गर्जना भरे) किनारे (तट हैं), घुंमन घेर (भँवरों) विच (में) ठाठां मारे (तूफानी लहरें हिलोरे मार रही हैं), डुब्ब डुब्ब (डूब-डूब कर) मोए (प्राण त्याग दिए) भारे (बलशाली तैराकों ने), जे (यदि) शोर करां (चीख-पुकार करूँ) तां (तो लोग मुझे) झल्लियां (पागल कहेंगे)।",
                "english_gloss": "नै चन्दल दे (Of river Chenab's) शोर किनारे (the roaring banks), घुंमन घेर विच (in swirling whirlpools) ठाठां मारे (surging waves crash), डुब्ब डुब्ब मोए (drowned and perished) भारे (mighty swimmers), जे शोर करां (if I cry aloud) तां झल्लियां (then they will brand me mad).",
                "poetic_hindi": "चनाब नदी का शोर किनारा, भँवरों में उठता जल-धारा,\nडूब मरे बलवान तैराका, चीखूँ तो जग कहे दिवाना!\nमाही की तड़प में जलती हूँ!",
                "poetic_english": "Chenab's roaring banks resound, where crashing whirlpools spin around;\nMighty swimmers have sunk and drowned; if I shriek out, I'm crazy found!\nIn yearning for my Love I burn!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "नै चन्दल दे डूंघे पाहे, तारू गोते खांदे आहे,  ",
                    "माही मुंडे पार सिधाए, मैं केवल रहियां कल्लियां ।  ",
                    "तांघ माही दी जलियां ।"
                ],
                "hindi_gloss": "नै (नदी) चन्दल दे (चनाब के) डूंघे (अथाह गहरे) पाहे (घाट/मार्ग हैं), तारू (प्रवीण तैराक) गोते खांदे आहे (हिचकोले खाकर डूबते रहे), माही (प्रियतम माहीवाल) मुंडे (चरवाहे ग्वाले) पार (उस पार) सिधाए (चले गए), मैं (मैं) केवल (मात्र) रहियां (रह गई हूँ) कल्लियां (एकाकिनी/अकेली)।",
                "english_gloss": "नै चन्दल दे (Of Chenab's river) डूंघे पाहे (fathomless deep passages), तारू (expert swimmers) गोते खांदे आहे (gasp and flounder), माही मुंडे (the beloved shepherd lads) पार सिधाए (have crossed over to the other side), मैं केवल रहियां (I alone am left behind) कल्लियां (forsaken and solitary).",
                "poetic_hindi": "गहरे घाट नदी के भारी, गोते खाएँ तैराक अनाड़ी,\nउस पार गए सब संगी-साक्षी, अकेली बैठी विरह-पुजारी!\nमाही की तड़प में जलती हूँ!",
                "poetic_english": "Deep are the chasms of the tide, where seasoned divers sink inside;\nAcross the stream my companions glide, while alone upon this bank I abide!\nIn yearning for my Love I burn!"
            },
            {
                "stanza_number": 5,
                "original": [
                    "नै चन्दल दियां तारू फाटां, खली उडीकां माही दियां वाटां,  ",
                    "इश्क माही दे लाईआं चाटां, जे कूकां तां मैं गलियां ।  ",
                    "तांघ माही दी जलियां ।"
                ],
                "hindi_gloss": "नै (नदी) चन्दल दियां (चनाब के) तारू (अगाध जल वाले) फाटां (जल-प्रवाह/चौड़े पाट), खली (खड़ी हुई) उडीकां (प्रतीक्षा कर रही हूँ) माही दियां (प्रियतम के) वाटां (मार्ग की), इश्क (प्रेम की) माही दे (माहीवाल के) लाईआं (लगाई हैं) चाटां (तीव्र घाव/चोटें), जे (यदि) कूकां (दर्द से कराहूँ) तां (तो) मैं (मैं) गलियां (गल-सड़ कर मिट जाऊँगी/बदनाम होऊँगी)।",
                "english_gloss": "नै चन्दल दियां (Of Chenab) तारू फाटां (the impassable wide torrents), खली उडीकां (standing I watch) माही दियां वाटां (the pathways of my Beloved), इश्क माही दे (the love of Mahi) लाईआं चाटां (has struck deep wounds), जे कूकां (if I wail) तां मैं गलियां (then I wither away in shame).",
                "poetic_hindi": "चनाब के गहरे-चौड़े पाट, खड़ी जोहती प्रीतम की बाट,\nइश्क ने मारे तीखे चाट, रोऊँ तो घुल जाऊँ खाट!\nमाही की तड़प में जलती हूँ!",
                "poetic_english": "Chenab's wide torrents surge and swell; watching His path my sorrows dwell;\nHis love has struck like blows from hell; I melt if I my agony tell!\nIn yearning for my Love I burn!"
            },
            {
                "stanza_number": 6,
                "original": [
                    "पार झनायों जंगल बेले, ओथे खूनी शेर बघेले,  ",
                    "झब्ब रब्ब मैनूं माही मेले, मैं एस फिकर विच गलियां ।  ",
                    "तांघ माही दी जलियां ।"
                ],
                "hindi_gloss": "पार (उस पार) झनायों (चनाब के उस पार) जंगल (घने जंगल) बेले (घास-झाड़ियों के बीहड़ हैं), ओथे (वहाँ) खूनी (रक्तपिपासु) शेर (सिंह) बघेले (तेंदुए/भेड़िए घूमते हैं), झब्ब (शीघ्र ही) रब्ब (परमेश्वर) मैनूं (मुझको) माही (प्रियतम से) मेले (मिला दे), मैं (मैं) एस (इसी) फिकर विच (चिंता में) गलियां (घुल-घुल कर सूख रही हूँ)।",
                "english_gloss": "पार झनायों (Across the Chenab) जंगल बेले (are wild jungles and riverine swamps), ओथे (there) खूनी शेर बघेले (prowl bloodthirsty lions and leopards), झब्ब रब्ब (may God swiftly) मैनूं माही मेले (unite me with my Mahiwal), मैं एस फिकर विच (in this anguish) गलियां (I waste away).",
                "poetic_hindi": "पार चनाब के जंगल-झाड़, शेर-बघेले खूँखार पहाड़,\nरब झट मुझे माही से मिलाए, इसी फिकर में गई मैं हार!\nमाही की तड़प में जलती हूँ!",
                "poetic_english": "Across Chenab wild forests sprawl, where lions roar and panthers call;\nMay God unite us past that wall; in this dread fear my senses fall!\nIn yearning for my Love I burn!"
            },
            {
                "stanza_number": 7,
                "original": [
                    "अद्धी रात लटकदे तारे, इक लटके इक लटकणहारे,  ",
                    "मैं उट्ठ आई नदी किनारे, हुन पार लंघन नूं खलियां ।  ",
                    "तांघ माही दी जलियां ।"
                ],
                "hindi_gloss": "अद्धी (आधी) रात (रात को) लटकदे (झिलमिलाते/डगमगाते) तारे (तारे हैं), इक लटके (कुछ तारे ढल चुके हैं) इक लटकणहारे (कुछ ढलने वाले हैं), मैं (मैं) उट्ठ आई (उठकर आ गई हूँ) नदी किनारे (चनाब के तट पर), हुन (अब) पार (उस पार) लंघन नूं (लांघने/उतरने के लिए) खलियां (दृढ़ संकल्प से खड़ी हूँ)।",
                "english_gloss": "अद्धी रात (At midnight hour) लटकदे तारे (stars hang low in the sky), इक लटके (some have already dipped) इक लटकणहारे (some are about to set), मैं उट्ठ आई (I arose and reached) नदी किनारे (the river's edge), हुन पार लंघन नूं (now to plunge across) खलियां (I stand resolute).",
                "poetic_hindi": "आधी रात ढलें सब तारे, कुछ डूबे, कुछ डूबनहारे,\nउठ आई मैं नदी किनारे, पार उतरने को पग धारे!\nमाही की तड़प में जलती हूँ!",
                "poetic_english": "Midnight has come, the stars hang low; some set, while others dim their glow;\nUnto the riverbank I go, to plunge across this surging flow!\nIn yearning for my Love I burn!"
            },
            {
                "stanza_number": 8,
                "original": [
                    "मैं मनतारू सार की जाणां, वंझ चप्पा ना तुल्हा पुराणा,  ",
                    "घुंमन घेर ना टांग टिकाणा, रो रो फाटां तलियां ।  ",
                    "तांघ माही दी जलियां ।"
                ],
                "hindi_gloss": "मैं (मैं तो) मनतारू (अनाड़ी/तैरना न जानने वाली) सार (मर्म/भेद) की जाणां (क्या जानूँ?), वंझ (पतवार) चप्पा (डाँड) ना (न) तुल्हा (लकड़ियों का बेड़ा) पुराणा (पुराना भी कोई नहीं है), घुंमन घेर (भँवर में) ना (न कोई) टांग (आलंब) टिकाणा (न कोई ठिकाना), रो रो (रो-रोकर) फाटां (जल-धाराओं पर) तलियां (हाथ-पाँव मार रही हूँ)।",
                "english_gloss": "मैं मनतारू (I am a novice swimmer) सार की जाणां (what do I know of crossing deep waters?), वंझ (neither bamboo pole) चप्पा (nor oar) ना तुल्हा पुराणा (nor even an old wooden raft have I), घुंमन घेर (in the whirlpool's swirl) ना टांग टिकाणा (neither foothold nor resting place), रो रो (weeping bitterly) फाटां तलियां (I strike my palms against the water).",
                "poetic_hindi": "अनाड़ी मैं तैराकी का मर्म क्या जानूँ? न पतवार न बेड़ा पुराना,\nभँवर में न सहारा न कोई ठिकाना, रो-रो मारूँ जल में पंजा अनजाना!\nमाही की तड़प में जलती हूँ!",
                "poetic_english": "No swimmer I, unskilled and frail; no oar, no raft to weather gale;\nIn whirlpools where all footholds fail, I beat the waves and weeping wail!\nIn yearning for my Love I burn!"
            },
            {
                "stanza_number": 9,
                "original": [
                    "बुल्ल्हा शहु घर मेरे आवे, हार शिंगार मेरे मन भावे,  ",
                    "मूंह मुकट मत्थे तिलक लगावे, जे वेखे तां मैं भलियां ।  ",
                    "तांघ माही दी जलियां,  ",
                    "नित्त काग उडावां खलियां ।"
                ],
                "hindi_gloss": "बुल्ल्हा (बुल्लेशाह कहता है) शहु (प्रभु-प्रियतम) घर (आँगन में) मेरे आवे (आ जाए), हार (पुष्प-हार) शिंगार (श्रृंगार) मेरे मन भावे (तभी मेरे मन को सुहाएगा), मूंह (मुख पर) मुकट (मुकुट) मत्थे (माथे पर) तिलक (तिलक) लगावे (लगाए), जे (यदि वह) वेखे (कृपा-दृष्टि से देख ले) तां (तो) मैं (मैं) भलियां (धन्य और कृतार्थ हो जाऊँगी)।",
                "english_gloss": "बुल्ल्हा शहु (Bulleh's King!) घर मेरे आवे (if He enters my home), हार शिंगार (bridal garlands and adornments) मेरे मन भावे (then alone will please my heart), मूंह मुकट (upon His head a crown) मत्थे तिलक लगावे (with a sacred tilak gracing His forehead), जे वेखे (if He casts His glance upon me) तां मैं भलियां (then blessed and perfected shall I be).",
                "poetic_hindi": "बुल्ल्हा कहे, शाह घर आए, तब श्रृंगार ये मन को भाए,\nशीश मुकुट, माथे तिलक लगाए, जो देखे तो भाग्य जगाए!\nमाही की तड़प में जलती हूँ,\nखड़ी नित्य मैं काग उड़ाती हूँ!",
                "poetic_english": "Bulleh says: if the King steps to my room, bridal adornments then will bloom;\nCrowned with His diadems, dispelling gloom, His glance transforms my earthly tomb!\nIn yearning for my Love I burn,\nAnd shoo the crows for His return!"
            }
        ],
        "sufi_commentary": "Kafi 141 is Bulleh Shah's sublime adaptation of the Punjabi Sohni-Mahiwal cycle into an allegorical epic of spiritual passage. The river Chenab ('नै चन्दल') is the turbulent sea of empirical existence, Maya, and worldly distraction. Sohni is the awakening soul standing destitute on the near bank: she has no money ('कउडी दमड़े पल्ले ना काई'—no accumulated ritual merit), no acquaintance with the boatmen ('नाल मलाहां दे नहीं आशनाई'—no scholastic connections), and no swimming competence ('मैं मनतारू'—no spiritual self-sufficiency). All around her, even expert swimmers sink in the fatal whirlpools ('घुंमन घेर') of worldly vanity. The midnight hour ('अद्धी रात लटकदे तारे') represents the dark night of the soul, where all external light dims, leaving only the pure fire of love ('तांघ'). In the final stanza, Bulleh daringly fuses Sufi union with Hindu iconography: the Beloved arrives adorned with a crown and sacred tilak ('मूंह मुकट मत्थे तिलक लगावे'), transcending sectarian boundaries and revealing the Absolute as the Sovereign Lover of every surrendered heart."
    },
    {
        "id": 142,
        "title_punjabi": "बहुड़ीं वे तबीबा मैंडी जिन्द गईआ / तेरे इश्क नचाइआ",
        "title_english": "Heal Me, O Divine Physician! Thy Love Has Made Me Dance",
        "raga": "Raga Kafi / Bhairavi",
        "meter": "Dohra / Matrik Baint (16-14 matras)",
        "theme": "Sacred Ecstatic Dance (Raqs), Holy Madness, and Healing through Total Devotion",
        "historical_context": "Unquestionably the most famous and universally beloved Kafi of Baba Bulleh Shah. Tradition records that when his Murshid, Shah Inayat Qadiri, was displeased with Bulleh due to societal criticism, Bulleh spent years learning classical music and dance from courtesans (kanjris). He then disguised himself as a dancing girl, adorned with ankle-bells (ghungroos), and danced ecstatically before Shah Inayat at the shrine of Shah Raza Qadiri. Overwhelmed by Bulleh's pure, ego-less devotion, Shah Inayat embraced him, saying: 'Bulleh, tu taan Inayat nu mana litta!' (Bulleh, you have won over Inayat!).",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "बहुड़ीं वे तबीबा मैंडी जिन्द गईआ ।  ",
                    "तेरे इश्क नचाइआ कर थईआ थईआ ।"
                ],
                "hindi_gloss": "बहुड़ीं (शीघ्र आकर रक्षा कर/सुध ले) वे (हे!) तबीबा (हकीम/दिव्य वैद्य!) मैंडी (मेरी) जिन्द (प्राण/जीवन) गईआ (निकल रही है/समाप्त हो रही है)। तेरे (तेरे) इश्क (प्रेम ने) नचाइआ (मुझे नचा दिया है) कर थईआ थईआ (थैया-थैया की ताल पर बेसुध होकर)।",
                "english_gloss": "बहुड़ीं (Come quickly to my aid) वे तबीबा (O Divine Physician!) मैंडी जिन्द गईआ (my very soul is slipping away). तेरे इश्क (Thy love) नचाइआ (has made me dance) कर थईआ थईआ (stepping to the ecstatic rhythm: Thaiyya Thaiyya!).",
                "poetic_hindi": "सुध ले हकीम! मेरी जान गई रे,\nतेरे इश्क नचाया थैया-थैया!",
                "poetic_english": "Come heal me, Physician, my life flies away!\nThy love makes me dance to its wild, frantic sway!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "इश्क डेरा मेरे अन्दर कीता,  ",
                    "भर के ज़हर प्याला मैं पीता,  ",
                    "झबदे आवीं वे तबीबा नहीं ते मैं मर गईआं ।  ",
                    "तेरे इश्क नचाइआ कर थईआ थईआ ।"
                ],
                "hindi_gloss": "इश्क (प्रेम ने) डेरा (अपना निवास) मेरे अन्दर (मेरे हृदय के भीतर) कीता (कर लिया है), भर के (भर-भर कर) ज़हर प्याला (विरह-विष का प्याला) मैं (मैंने) पीता (पी लिया है), झबदे (शीघ्र ही) आवीं (आना) वे तबीबा (हे वैद्यराज!) नहीं ते (अन्यथा) मैं (मैं) मर गईआं (मृत्यु को प्राप्त हो जाऊँगी)।",
                "english_gloss": "इश्क (Love) डेरा मेरे अन्दर कीता (has pitched its camp within my breast), भर के ज़हर प्याला (a goblet brimming with poison) मैं पीता (I drank down), झबदे आवीं वे तबीबा (come swiftly, O Physician!) नहीं ते मैं मर गईआं (or else I shall surely die).",
                "poetic_hindi": "इश्क ने डेरा मन भीतर डाला, पी लिया भर के विष का प्याला,\nझट आ वैद्य, नहीं तो मरी रे! तेरे इश्क नचाया थैया-थैया!",
                "poetic_english": "Love pitched its deep camp inside my wounded core;\nA goblet of poison I drank to the floor;\nCome swiftly, Physician, or I am no more!\nThy love makes me dance to its wild, frantic sway!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "छुप्प गया सूरज बाहर रह गई आ लाली,  ",
                    "होवां मैं सदके मुड़ जे दें विखाली ,  ",
                    "मैं भुल्ल गईआं तेरे नाल ना गईआं ।  ",
                    "तेरे इश्क नचाइआ कर थईआ थईआ ।"
                ],
                "hindi_gloss": "छुप्प गया (डूब गया/अस्त हो गया) सूरज (सूर्य रूपी जीवन/साधना का समय), बाहर (केवल क्षितिज पर) रह गई आ लाली (गोधूलि की हल्की लाली शेष है), होवां मैं (मैं हो जाऊँ) सदके (न्योछावर/बलिहारी) मुड़ (पुनः) जे (यदि) दें विखाली (तू अपना दर्शन दे दे), मैं (मैं) भुल्ल गईआं (भूल कर बैठी) तेरे नाल (तेरे साथ) ना गईआं (जो तेरे साथ न चल पड़ी)।",
                "english_gloss": "छुप्प गया सूरज (The sun has set) बाहर रह गई आ लाली (leaving only the twilight's fading crimson), होवां मैं सदके (I would sacrifice my very life) मुड़ जे दें विखाली (if once more Thou wouldst grant me a glimpse of Thy face), मैं भुल्ल गईआं (alas, I committed the grave error) तेरे नाल ना गईआं (of not departing with Thee).",
                "poetic_hindi": "डूब गया सूरज, शेष रही लाली, वारी जाऊँ जो दे फिर विखाली,\nभूल गई जो संग न चली रे! तेरे इश्क नचाया थैया-थैया!",
                "poetic_english": "The sun has sunk low, leaving twilight's red hue;\nI'd surrender my life for one vision of You;\nAlas, that I lagged and I followed not through!\nThy love makes me dance to its wild, frantic sway!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "तेरे इश्क दी सार वे मैं ना जाणां,  ",
                    "इह सिर आया ए मेरा हेठ वदाणां,  ",
                    "सट्ट पई इश्के दी तां कूकां दईआं ।  ",
                    "तेरे इश्क नचाइआ कर थईआ थईआ ।"
                ],
                "hindi_gloss": "तेरे (तेरे) इश्क दी (प्रेम का) सार (मर्म/गहनता) वे (हे सखे!) मैं (मैं) ना जाणां (नहीं जानती थी), इह सिर (यह मेरा सिर) आया ए (आ चुका है) मेरा (मेरा) हेठ (नीचे) वदाणां (लुहार के भारी हथौड़े/निहाई के नीचे), सट्ट (चोट) पई (पड़ी है) इश्के दी (प्रेम के घनों की) तां (तब) कूकां (पुकारती हूँ) दईआं (हे दयालु ईश्वर/सद्गुरु!)।",
                "english_gloss": "तेरे इश्क दी सार (The true depth of Thy love) वे मैं ना जाणां (alas, I did not know), इह सिर आया ए मेरा (now this head of mine has come) हेठ वदाणां (under the blacksmith's heavy sledgehammer), सट्ट पई इश्के दी (the hammer-blows of love have struck) तां कूकां दईआं (and I shriek: O Merciful Lord!).",
                "poetic_hindi": "प्रेम का मर्म न पहले मैं जानी, सिर पर पड़ा है हथौड़ा वदानी,\nचोट लगी तो पुकार उठी रे! तेरे इश्क नचाया थैया-थैया!",
                "poetic_english": "The depths of Thy passion I never could tell;\nNow my head 'neath the blacksmith's sledgehammer fell;\nStruck by love's blows, 'O Compassion!' I yell;\nThy love makes me dance to its wild, frantic sway!"
            },
            {
                "stanza_number": 5,
                "original": [
                    "एस इश्क दे कोलों सानूं हटक ना माए,  ",
                    "लाहू (लाहौर) जांदड़े बेड़े मोड़ कौन हटाए,  ",
                    "मेरी अकल भुल्ली नाल मुहाण्यां दे गईआं ।  ",
                    "तेरे इश्क नचाइआ कर थईआ थईआ ।"
                ],
                "hindi_gloss": "एस (इस) इश्क दे कोलों (प्रेम के मार्ग से) सानूं (मुझको) हटक ना (रोक मत) माए (हे मेरी माँ!), लाहू/लाहौर (लाहौर की ओर धारा के वेग से) जांदड़े (जाती हुई) बेड़े (नावों को) मोड़ (वापस मोड़कर) कौन हटाए (कौन रोक सकता है?), मेरी (मेरी) अकल (बुद्धि) भुल्ली (भ्रमित/नष्ट हो गई), नाल (साथ) मुहाण्यां दे (नाविकों के साथ) गईआं (वह बह गई)।",
                "english_gloss": "एस इश्क दे कोलों (From this passion of love) सानूं हटक ना माए (do not restrain me, O mother!), लाहू जांदड़े बेड़े (boats rushing down the current toward Lahore) मोड़ कौन हटाए (who can ever turn back?), मेरी अकल भुल्ली (my worldly intellect was unseated) नाल मुहाण्यां दे गईआं (and sailed away with the ferrymen).",
                "poetic_hindi": "रोक न मुझको इस प्रेम से माई! लाहौर को जाती नाव मुड़ न पाई,\nअक्ल भुलाई, मल्लाह संग धाई रे! तेरे इश्क नचाया थैया-थैया!",
                "poetic_english": "Restrain me not, mother, from love's stormy shore;\nCan boats racing downstream be turned from Lahore?\nMy intellect drowned with the boatmen of yore;\nThy love makes me dance to its wild, frantic sway!"
            },
            {
                "stanza_number": 6,
                "original": [
                    "एस इश्क दी झंगी विच मोर बुलेंदा,  ",
                    "सानूं काबा ते किबला प्यारा यार दसेंदा,  ",
                    "सानूं घायल करके फिर खबर ना लईआ ।  ",
                    "तेरे इश्क नचाइआ कर थईआ थईआ ।"
                ],
                "hindi_gloss": "एस (इस) इश्क दी (प्रेम की) झंगी विच (कुंज/झुरमुट में) मोर (मोर) बुलेंदा (कूक रहा है/पुकार रहा है), सानूं (मुझको) काबा (पवित्र काबा) ते (और) किबला (प्रार्थना की दिशा) प्यारा (मेरा प्रियतम) यार (यार/सद्गुरु) दसेंदा (दिखाई देता है), सानूं (मुझको) घायल (प्रेम-बाणों से घायल) करके (करके) फिर (पुनः) खबर (कोई सुध-बुध) ना लईआ (नहीं ली)।",
                "english_gloss": "एस इश्क दी झंगी विच (In the lush grove of this divine love) मोर बुलेंदा (the peacock calls), सानूं (to me) काबा ते किबला (my Ka'aba and my Qibla) प्यारा यार दसेंदा (is revealed as my beloved Friend), सानूं घायल करके (having wounded me mortally) फिर खबर ना लईआ (Thou took no further heed of me).",
                "poetic_hindi": "प्रेम की कुंज में मोर पुकारे, काबा-ओ-किबला है यार पियारे,\nघायल किया पर सुध न ली रे! तेरे इश्क नचाया थैया-थैया!",
                "poetic_english": "In the groves of this love the peacock sings clear;\nMy Kaaba and Qibla's my Beloved Friend dear;\nHaving wounded my soul, Thou no longer drew near;\nThy love makes me dance to its wild, frantic sway!"
            },
            {
                "stanza_number": 7,
                "original": [
                    "बुल्ल्हा शाह इनायत दे बह बूहे,  ",
                    "जिस पहनाए सानूं सावे सूहे,  ",
                    "जां मैं मारी उडारी मिल प्या वहिया ।  ",
                    "तेरे इश्क नचाइआ कर थईआ थईआ ।"
                ],
                "hindi_gloss": "बुल्ल्हा (बुल्लेशाह कहता है) शाह इनायत (मुर्शिद शाह इनायत) दे (के) बह (बैठ गया है) बूहे (द्वार पर), जिस (जिस कृपालु मुर्शिद ने) पहनाए (पहना दिए) सानूं (मुझको) सावे (हरे/उमंग भरे) सूहे (गहरे लाल/सुहाग के वस्त्र), जां (जब) मैं (मैंने) मारी (लगाई) उडारी (उड़ान/छलांग), मिल प्या (मुझसे मिल गया) वहिया (वह शाश्वत प्रियतम प्रभु)।",
                "english_gloss": "बुल्ल्हा (Bulleh sits) शाह इनायत दे बह बूहे (at the portal of Shah Inayat), जिस पहनाए सानूं (who adorned me in) सावे सूहे (robes of fresh emerald green and crimson bridal red), जां मैं मारी उडारी (the moment I took mystical flight) मिल प्या वहिया (I met the Supreme One, my Lord).",
                "poetic_hindi": "शाह इनायत के दर बुल्ल्हा आया, जिसने मुझे हरा-लाल सुहाग सजाया,\nमारी उड़ान तो प्रीतम पाया रे!\nतेरे इश्क नचाया कर थैया-थैया,\nसुध ले हकीम! मेरी जान गई रे!",
                "poetic_english": "At Shah Inayat's threshold Bulleh takes his place;\nHe draped me in garments of emerald and grace;\nI took flight to heaven and met His embrace!\nThy love makes me dance to its wild, frantic sway!\nCome heal me, Physician, my life flies away!"
            }
        ],
        "sufi_commentary": "Kafi 142 represents the crowning pinnacle of ecstatic devotion (wajd and raqs) in the Indian Sufi tradition. The historical context of Bulleh donning dancing bells and dancing to appease his offended Murshid Shah Inayat embodies the total annihilation of scholarly pedigree, high-caste Sayyid lineage, and intellectual dignity. In Sufi ontology, true dance is not an exhibitionist performance; it is the involuntary movement of the soul when struck by the anvil of Divine Love ('इह सिर आया ए मेरा हेठ वदाणां'). Bulleh drinks the poison-cup of separation and boldly proclaims that conventional religion is superseded by love: his Kaaba and Qibla are no longer a stone cubic shrine in Mecca, but the living face of the Beloved ('सानूं काबा ते किबला प्यारा यार दसेंदा'). The ecstatic refrain 'तेरे इश्क नचाइआ कर थईआ थईआ' transforms the earthly dancer into the cosmic dancer of the Divine Will. When Inayat clothes him in green and red ('सावे सूहे'—green representing spiritual life and rejuvenation, red representing the consummation of mystical marriage), the soul takes its final flight ('मारी उडारी') into the non-dual ocean of Absolute Reality."
    },
    {
        "id": 143,
        "title_punjabi": "टूने कामन करके नी मैं प्यारा यार मनावांगी",
        "title_english": "Through Spells and Incantations I Shall Win My Beloved",
        "raga": "Raga Sorath / Kafi",
        "meter": "Matrik Chhand (16-14 matras)",
        "theme": "Subversion of Folk Sorcery (Tona-Kamana) as Esoteric Tantric-Sufi Yoga of Love",
        "historical_context": "Rooted in the indigenous rural Punjabi folklore where spurned women resort to love potions, charms, and spells ('टूने कामन') cast by ascetics or sorcerers, Bulleh Shah boldly appropriates this vernacular idiom. He transforms vulgar witchcraft into a cosmic, yogic, and mystical alchemy: burning the sun with eyes lined with stormy kohl, rousing the seven oceans within the heart, and playing the cosmic horn (nada) upon the terrace of the Spaceless Realm (La-makan).",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "इस टूने नूं पढ़ फूकांगी, सूरज अगन जलावांगी ।  ",
                    "टूने कामन करके नी मैं प्यारा यार मनावांगी ।"
                ],
                "hindi_gloss": "इस (इस दिव्य) टूने नूं (मंत्र/टोने को) पढ़ (पढ़कर) फूकांगी (फूँक मारूँगी), सूरज (सूर्य में) अगन (प्रचंड अग्नि) जलावांगी (जला दूँगी)। टूने (टोने) कामन (जादू-टोने/प्रेम के तंत्र) करके (करके) नी (हे सखी!) मैं (मैं) प्यारा (मेरे प्यारे) यार (प्रियतम को) मनावांगी (मनाकर वश में कर लूँगी)।",
                "english_gloss": "इस टूने नूं (This mystical spell) पढ़ फूकांगी (I will recite and breathe forth), सूरज अगन जलावांगी (and kindle fire in the very sun). टूने कामन करके (By weaving love-spells and charms) नी मैं प्यारा यार मनावांगी (O friend, I shall win and reconcile my Beloved).",
                "poetic_hindi": "मन्त्र पढ़ूँ, फूँकूँ ऐसा, सूरज में अगन जलाऊँगी;\nटोने-कामन कर री सखी! प्यारे यार को मनाऊँगी!",
                "poetic_english": "I'll chant this spell and blow its spark, to set the sun with fire agleam;\nWith charms and secret arts of love, I will redeem my Love supreme!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "अक्खियां काजल काले बादल, भवां से आग लगावांगी ।  ",
                    "टूने कामन करके नी मैं प्यारा यार मनावांगी ।"
                ],
                "hindi_gloss": "अक्खियां (नेत्रों में) काजल (काजल आँजकर) काले (काले) बादल (मेघों का रूप धरूँगी), भवां से (अपनी भृकुटियों के चाप से) आग (विरह की आग) लगावांगी (लगा दूँगी)।",
                "english_gloss": "अक्खियां काजल (In my eyes kohl deep as) काले बादल (black rainclouds), भवां से (with the arch of my eyebrows) आग लगावांगी (I shall set a cosmic fire).",
                "poetic_hindi": "नयनों में काजल घन-कारा, भृकुटि से आग लगाऊँगी;\nटोने-कामन कर री सखी! प्यारे यार को मनाऊँगी!",
                "poetic_english": "Kohl in my eyes like thunderclouds, my arched brows kindle lightning's beam;\nWith charms and secret arts of love, I will redeem my Love supreme!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "और बसात नहीं कुझ मेरी, जोबन धड़ी गुन्दावांगी ।  ",
                    "टूने कामन करके नी मैं प्यारा यार मनावांगी ।"
                ],
                "hindi_gloss": "और (अन्य कोई) बसात (पूँजी/सामर्थ्य) नहीं (नहीं है) कुझ (कुछ भी) मेरी (मेरी), जोबन (अपनी सम्पूर्ण जवानी/यौवन की) धड़ी (केश-वेणी/लटें) गुन्दावांगी (सजाकर गूंथूँगी)।",
                "english_gloss": "और बसात नहीं कुझ मेरी (Other wealth or merit I have none), जोबन धड़ी (the tresses of my full youth) गुन्दावांगी (I shall plait and offer).",
                "poetic_hindi": "और बिसात नहीं कुछ मेरी, यौवन की वेणी गूँथूँगी;\nटोने-कामन कर री सखी! प्यारे यार को मनाऊँगी!",
                "poetic_english": "No other wealth have I to bring, than tresses of youth's flowering stream;\nWith charms and secret arts of love, I will redeem my Love supreme!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "सत्त समुन्दर दिल दे अन्दर, दिल से लहर उठावांगी ।  ",
                    "टूने कामन करके नी मैं प्यारा यार मनावांगी ।"
                ],
                "hindi_gloss": "सत्त (सातों) समुन्दर (सागर) दिल दे अन्दर (मेरे हृदय के भीतर समाए हैं), दिल से (हृदय की गहराई से) लहर (प्रेम के ज्वार की तरंगें) उठावांगी (उठाऊँगी)।",
                "english_gloss": "सत्त समुन्दर (All seven oceans) दिल दे अन्दर (dwell within my heart), दिल से (from within this heart) लहर उठावांगी (I will raise storming waves of ecstasy).",
                "poetic_hindi": "सातों सागर मन के भीतर, दिल से लहर उठाऊँगी;\nटोने-कामन कर री सखी! प्यारे यार को मनाऊँगी!",
                "poetic_english": "Seven oceans roll within my heart, from its deep core vast waves I'll teem;\nWith charms and secret arts of love, I will redeem my Love supreme!"
            },
            {
                "stanza_number": 5,
                "original": [
                    "बिजली हो कर चमक ड्रावां, मैं बादल घिर घिर जावांगी ।  ",
                    "टूने कामन करके नी मैं प्यारा यार मनावांगी ।"
                ],
                "hindi_gloss": "बिजली (कौंधती तड़ित) हो कर (बनकर) चमक (चमक से) ड्रावां (विस्मय में डालूँगी), मैं (मैं) बादल (काले मेघ बनकर) घिर घिर (घिर-घिर कर) जावांगी (चारों ओर छा जाऊँगी)।",
                "english_gloss": "बिजली हो कर (Becoming lightning) चमक ड्रावां (flashing I will terrify/awe), मैं बादल घिर घिर जावांगी (I shall gather as enveloping rainclouds).",
                "poetic_hindi": "बिजली बन कर चमक डराऊँ, बादल बन घिर जाऊँगी;\nटोने-कामन कर री सखी! प्यारे यार को मनाऊँगी!",
                "poetic_english": "Flashing like lightning I'll strike awe, and gather like clouds across the scheme;\nWith charms and secret arts of love, I will redeem my Love supreme!"
            },
            {
                "stanza_number": 6,
                "original": [
                    "इश्क अंगीठी हरमल तारे, सूरज अगन चढ़ावांगी ।  ",
                    "टूने कामन करके नी मैं प्यारा यार मनावांगी ।"
                ],
                "hindi_gloss": "इश्क (प्रेम की) अंगीठी (अंगीठी में) हरमल (हरमल नामक अभिमंत्रित धूप/बीज) तारे (तारों को बनाकर) सूरज (सूर्य की) अगन (प्रचंड ज्वाला) चढ़ावांगी (धधका दूँगी)।",
                "english_gloss": "इश्क अंगीठी (In the brazier of divine love) हरमल तारे (tossing the stars like incense seeds), सूरज अगन चढ़ावांगी (I will stoke the sun's fiery blaze).",
                "poetic_hindi": "इश्क-अँगीठी में तारे सुलगाऊँ, सूरज की अगन बढ़ाऊँगी;\nटोने-कामन कर री सखी! प्यारे यार को मनाऊँगी!",
                "poetic_english": "In love's hearth tossing stars like seed, to stoke the solar fire agleam;\nWith charms and secret arts of love, I will redeem my Love supreme!"
            },
            {
                "stanza_number": 7,
                "original": [
                    "ना मैं व्याही ना मैं कवारी, बेटा गोद खिडावांगी ।  ",
                    "टूने कामन करके नी मैं प्यारा यार मनावांगी ।"
                ],
                "hindi_gloss": "ना (न तो) मैं व्याही (विवाहिता स्त्री हूँ), ना मैं कवारी (न ही मैं कुँवारी कन्या हूँ), बेटा (एक दिव्य बालक/ज्ञान-शिशु को) गोद (अपनी गोद में) खिडावांगी (खिलाऊँगी)।",
                "english_gloss": "ना मैं व्याही (Neither am I married) ना मैं कवारी (nor am I an unwed maid), बेटा (a child of divine illumination) गोद खिडावांगी (I shall cradle and play in my lap).",
                "poetic_hindi": "न ब्याही, न हूँ मैं कँवारी, बालक गोद खिलाऊँगी;\nटोने-कामन कर री सखी! प्यारे यार को मनाऊँगी!",
                "poetic_english": "Neither a maiden nor a wife, a child I'll cradle, rare to deem;\nWith charms and secret arts of love, I will redeem my Love supreme!"
            },
            {
                "stanza_number": 8,
                "original": [
                    "बुल्ल्हा लामकान दी पटड़ी उते, बहके नाद वजावांगी ।  ",
                    "टूने कामन करके नी मैं प्यारा यार मनावांगी ।"
                ],
                "hindi_gloss": "बुल्ल्हा (बुल्लेशाह कहता है) लामकान (उस असीम, देश-कालातीत ला-मकां) दी (की) पटड़ी (चौखट/मंच) उते (पर), बहके (बैठकर) नाद (अनहद नाद/शंख) वजावांगी (बजाऊँगी)।",
                "english_gloss": "बुल्ल्हा (Bulleh cries) लामकान दी पटड़ी उते (upon the terrace/threshold of the Spaceless Void), बहके (seated) नाद वजावांगी (I shall sound the primordial unstruck Horn).",
                "poetic_hindi": "बुल्ल्हा ला-मकां की पटरी पे बैठ, अनहद नाद बजाऊँगी;\nटोने-कामन कर री सखी! प्यारे यार को मनाऊँगी!",
                "poetic_english": "Seated on Spaceless terraces, I'll blow the eternal cosmic horn;\nWith charms and secret arts of love, I'll bring my Love to dawn!"
            }
        ],
        "sufi_commentary": "Kafi 143 is an audacious metaphysical tour de force that subverts rural Punjabi folk-magic ('टूने कामन') into an esoteric yogic-Sufi allegory of cosmic power. In village society, a desperate woman employs 'tonas' (spells and charms) using incensed seeds ('हरमल') and incantations to regain her estranged lover. Bulleh takes these folk motifs and elevates them to cosmic proportions: the hearth is the fire of Ishq, the incense seeds tossed into the flame are the stars of the cosmos, and the blazing embers are the sun itself. In Stanza 4, he anticipates modern depth psychology and Advaitic cosmology: 'सत्त समुन्दर दिल दे अन्दर'—the seven cosmic oceans do not lie outside, but churn within the human spiritual heart (Qalb). In Stanza 7, he presents a profound mystical riddle (sandhyabhasha / ultabansi): 'ना मैं व्याही ना मैं कवारी, बेटा गोद खिडावांगी' (Neither married nor virgin, I shall play a child in my lap). This denotes the soul that is free from worldly institutional bonds (neither married to social dogma nor uninitiated), yet gives birth to the Christ/Krishna-child of spiritual gnosis (Irfan). Finally, seated upon the terrace of the Spaceless (La-makan), the lover blows the primordial horn (Nada), dissolving all creation back into the Beloved."
    },
    {
        "id": 144,
        "title_punjabi": "तूं किधरों आया किधर जाणा, आपना दस्स टिकाणा",
        "title_english": "Whence Have You Come, Whither Shall You Go? Declare Your Abode",
        "raga": "Raga Tilang / Bhairav",
        "meter": "Dohra / Matrik (16-12 matras)",
        "theme": "The Inevitability of Death, Illusion of Power, and the City of Silence (Graveyard)",
        "historical_context": "A profound moral and mystical interrogation. Bulleh Shah addresses the corrupt magistrates, oppressive tax collectors, and arrogant elites of his era who abused state power ('जिस ठाने दा तूं मान करें') and extorted the common folk. He drags them to the ultimate equalizer—the graveyard, which he christens 'The City of Silence' ('शहर खमोशां'), where emperors and beggars alike dissolve under the ferrymanship of the Angel of Death (Malak-ul-Maut).",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "तूं किधरों आया किधर जाणा, आपना दस्स टिकाना ।  ",
                    "जिस ठाने दा तूं मान करें, तेरे नाल ना जासी ठाना ।"
                ],
                "hindi_gloss": "तूं (तू) किधरों (कहाँ से) आया (आया है) किधर (कहाँ तुझे) जाणा (जाना है), आपना (अपना सच्चा) दस्स (बता) टिकाना (ठिकाना/मूल स्वरूप)। जिस (जिस सांसारिक) ठाने दा (पद/थाने/अधिकार का) तूं (तू) मान करें (अहंकार करता है), तेरे (तेरे) नाल (साथ) ना (नहीं) जासी (जाएगा) ठाना (वह पद-प्रतिष्ठा)।",
                "english_gloss": "तूं किधरों आया (Whence hast thou come) किधर जाणा (whither must thou go), आपना दस्स टिकाना (declare thy true abode). जिस ठाने दा (Of which worldly station/post) तूं मान करें (thou art so proud), तेरे नाल ना जासी ठाना (that post shall not accompany thee beyond).",
                "poetic_hindi": "कहाँ से आया, कहाँ है जाना? अपना बता ठिकाना!\nजिस ठाने का मान करे तू, साथ न जाए वो थाना!",
                "poetic_english": "Whence have you come, whither will you tread? Declare your true domain!\nThat earthly throne of which you boast will not with you remain!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "ज़ुलम करें ते लोक सतावें, कसब फड़्यु लुट्ट खाना ।  ",
                    "महबूब सुबहानी करे आसानी, खौफ जाए मलकाना ।"
                ],
                "hindi_gloss": "ज़ुलम (अत्याचार) करें (करता है) ते (और) लोक (जनता/संसार को) सतावें (सताता है), कसब (पेशा/व्यवसाय) फड़्यु (बना लिया है) लुट्ट खाना (दूसरों को लूटकर खाना)। महबूब सुबहानी (ईश्वर का परम प्रिय/सद्गुरु) करे आसानी (जब कृपा से राह आसान करे), खौफ (भय) जाए (दूर हो जाए) मलकाना (मालिक होने के अहंकार का)।",
                "english_gloss": "ज़ुलम करें (Thou commit tyranny) ते लोक सतावें (and torment the people), कसब फड़्यु (thou hast made a profession of) लुट्ट खाना (plundering and devouring others' wealth). महबूब सुबहानी (If the Beloved of the Divine) करे आसानी (grants spiritual ease), खौफ जाए (the dread will vanish) मलकाना (of false ownership and worldly terror).",
                "poetic_hindi": "जुल्म करे, जनता को सताए, पेशा लूट-कमाना,\nमहबूब सुब्हानी दया करे तो, मिटे खौफ सुल्ताना!",
                "poetic_english": "You practice cruelty, oppress the weak, and make a trade of greed;\nMay the Divine Beloved grant ease, from tyrannical terror freed!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "शहर खमोशां दे चल वस्सीए, जित्थे मुलक समाना ।  ",
                    "भर भर पूर लंघावे डाढा , मलक-उल-मौत मुहाना ।"
                ],
                "hindi_gloss": "शहर (उस नगर में) खमोशां दे (मौन के नगर/कब्रिस्तान में) चल (चलकर) वस्सीए (बसें), जित्थे (जहाँ सारा) मुलक (संसार/जन-समुदाय) समाना (समा गया है)। भर भर पूर (नाव भर-भर कर समूह के समूह) लंघावे (पार उतारता है) डाढा (वह अत्यंत शक्तिशाली), मलक-उल-मौत (मौत का फरिश्ता अज़राईल रूपी) मुहाना (नाविक)।",
                "english_gloss": "शहर खमोशां दे (In the City of Silence / graveyard) चल वस्सीए (let us go and dwell), जित्थे (where) मुलक समाना (the entire multitude of nations has vanished). भर भर पूर (Ferryload after ferryload) लंघावे (transports across) डाढा (the mighty, relentless), मलक-उल-मौत (Angel of Death) मुहाना (as the stern boatman).",
                "poetic_hindi": "शहर-ए-खामोशाँ में चल बसिए, जहाँ मुल्क समाया सारा,\nभर-भर बेड़े पार उतारे, यम-दूत मल्लाह विकराला!",
                "poetic_english": "Come, let us dwell in the City of Silence, where vanished nations lie;\nThe Angel of Death is a boatman stern, ferrying all who die!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "करे चावड़ चार देहाड़े, ओड़क तूं उट्ठ जाना ।  ",
                    "इन्हां सभनां थीं ए बुल्ल्हा, औगुणहार पुराना ।  ",
                    "तूं किधरों आया किधर जाणा, आपना दस्स टिकाना ।  ",
                    "जिस ठाने दा तूं मान करें, तेरे नाल ना जासी ठाना ।"
                ],
                "hindi_gloss": "करे (करता है) चावड़ (उछल-कूद/चंचलता/उल्लास) चार देहाड़े (चार दिनों की इस क्षणिक आयु में), ओड़क (अंततः) तूं (तुझे) उट्ठ जाना (यहाँ से उठकर चले जाना है)। इन्हां सभनां थीं (इन सब में सबसे अधिक) ए बुल्ल्हा (यह बुल्ला ही) औगुणहार (अवगुणों का पुतला/दोषी) पुराना (पुराना पापी है)।",
                "english_gloss": "करे चावड़ (Thou makest merry and revels) चार देहाड़े (for four fleeting days), ओड़क (ultimately) तूं उट्ठ जाना (thou must arise and depart). इन्हां सभनां थीं (More than all these) ए बुल्ल्हा (this Bulleh himself is) औगुणहार पुराना (an ancient transgressor, full of faults).",
                "poetic_hindi": "चार दिनों की मौज-मस्ती, अंत में है उठ जाना;\nइन सब में बुल्ल्हा खुद को जाने अवगुणहार पुराना!\nकहाँ से आया, कहाँ है जाना? अपना बता ठिकाना!\nजिस ठाने का मान करे तू, साथ न जाए वो थाना!",
                "poetic_english": "Four fleeting days you frolic and dance, then you must arise and go;\nYet Bulleh sees his own frail self as the guiltiest soul below!\nWhence have you come, whither will you tread? Declare your true domain!\nThat earthly throne of which you boast will not with you remain!"
            }
        ],
        "sufi_commentary": "Kafi 144 is an uncompromising memento mori and a sharp social critique of the illusions of temporal power. In 18th-century feudal Punjab, magistrates and landlords derived immense arrogance from their 'thana' (police station, district administrative seat). Bulleh pierces this bloated ego by reminding them that no earthly office, army, or title crosses the threshold of mortality. He introduces one of the most haunting poetic metaphors in Sufi literature: the cemetery as 'शहर खमोशां' (The City of Silence). In this quiet necropolis, the entire diversity of humanity—kings, tyrants, paupers, and ascetics—is leveled into equal dust. The Angel of Death (Malak-ul-Maut) is depicted as a tireless, unrelenting ferryman ('मुहाना') who continually ferries whole boatloads ('भर भर पूर') of mortals across the river of non-existence. Rather than adopting a holier-than-thou stance, Bulleh concludes with characteristic Sufi Malamati humility: he turns the mirror upon himself, confessing that among all these heedless souls, he, Bulleh, is the oldest and greatest wrongdoer ('औगुणहार पुराना')."
    },
    {
        "id": 145,
        "title_punjabi": "तूं नहीउं मैं नाहीं वे सज्जणा, तूं नहीउं मैं नाहीं",
        "title_english": "Neither Art Thou, Nor Am I, O Beloved!",
        "raga": "Raga Tilang / Asavari",
        "meter": "Dohra / Matrik (16-12 matras)",
        "theme": "The Total Extinction of Subject-Object Duality in Non-Dual Awareness",
        "historical_context": "A pristine diamond of pure Advaita / Wahdat al-Wujud. In this intimate song of absolute union, Bulleh Shah strips away both the 'I' (the seeker's separate ego) and the 'Thou' (the external, objectified deity). Like the shadow that follows the crumbling ruined wall, the Beloved is indistinguishable from the seeker's every breath, speech, movement, and sleep.",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "खोले दे परछावें वांङू, घुम रेहा मन माहीं ।  ",
                    "तूं नहीउं मैं नाहीं वे सज्जणा, तूं नहीउं मैं नाहीं ।"
                ],
                "hindi_gloss": "खोले (खंडहर/गिरे हुए मकान) दे (की) परछावें (छाया के) वांङू (समान), घुम रेहा (घूम रहा/मंडरा रहा है) मन माहीं (मेरे मन के भीतर)। तूं नहीउं (न तू अलग है) मैं नाहीं (न मैं अलग हूँ) वे सज्जणा (हे प्रियतम!), तूं नहीउं मैं नाहीं (न तू है, न मैं हूँ - केवल अद्वैत सत्य है)।",
                "english_gloss": "खोले दे (Of a ruined, crumbling wall) परछावें वांङू (like the shifting shadow), घुम रेहा (circling ever) मन माहीं (within my soul). तूं नहीउं (Neither art Thou separate) मैं नाहीं (nor am I separate) वे सज्जणा (O Beloved!), तूं नहीउं मैं नाहीं (neither art Thou, nor am I).",
                "poetic_hindi": "खंडहर की परछाईं जैसा, मन में घुमड़े माहीं,\nतू नहीं, मैं भी नहीं सजन! तू नहीं, मैं नाहीं!",
                "poetic_english": "Like shadow cast by crumbling walls, circling within my heart unseen;\nNeither art Thou, nor am I, Love! No distance lies between!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "जां बोलां तूं नाले बोलें चुप्प करां मन माहीं ।  ",
                    "तूं नहीउं मैं नाहीं वे सज्जणा, तूं नहीउं मैं नाहीं ।"
                ],
                "hindi_gloss": "जां (जब) बोलां (मैं बोलती हूँ) तूं (तू ही) नाले बोलें (मेरे साथ बोलता है), चुप्प करां (जब मैं मौन हो जाती हूँ) मन माहीं (तो तू ही मौन में स्थित है)। तूं नहीउं मैं नाहीं वे सज्जणा, तूं नहीउं मैं नाहीं ।",
                "english_gloss": "जां बोलां (When I speak) तूं नाले बोलें (Thou speakest along), चुप्प करां (when I keep silent) मन माहीं (Thou abidest in the silence of my heart). तूं नहीउं मैं नाहीं वे सज्जणा, तूं नहीउं मैं नाहीं ।",
                "poetic_hindi": "जब बोलूँ तू संग में बोले, चुप हूँ तो तू माहीं;\nतू नहीं, मैं भी नहीं सजन! तू नहीं, मैं नाहीं!",
                "poetic_english": "Whene'er I speak, Thou speakest too; in silence Thou dost reign;\nNeither art Thou, nor am I, Love! No dual masks remain!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "जां सौंवां तां नाले सौवें जां टुरां तां राहीं ।  ",
                    "तूं नहीउं मैं नाहीं वे सज्जणा, तूं नहीउं मैं नाहीं ।"
                ],
                "hindi_gloss": "जां (जब) सौंवां (मैं सोती हूँ) तां (तब) नाले (मेरे साथ) सौवें (तू ही सोता है), जां (जब) टुरां (मैं चलती हूँ) तां (तब) राहीं (मार्ग पर मेरे संग तू ही चलता है)। तूं नहीउं मैं नाहीं वे सज्जणा, तूं नहीउं मैं नाहीं ।",
                "english_gloss": "जां सौंवां (When I sleep) तां नाले सौवें (Thou sleepest with me), जां टुरां (when I walk) तां राहीं (Thou walkest upon the road beside me). तूं नहीउं मैं नाहीं वे सज्जणा, तूं नहीउं मैं नाहीं ।",
                "poetic_hindi": "जब सोऊँ तू संग में सोवे, चलूँ तो राह सजाई;\nतू नहीं, मैं भी नहीं सजन! तू नहीं, मैं नाहीं!",
                "poetic_english": "Whene'er I sleep, Thou sleepest too; when I walk, Thou art the way;\nNeither art Thou, nor am I, Love! Beyond the night and day!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "बुल्ल्हा शहु घर आया साडे जिन्दड़ी घोल घुमाईं ।  ",
                    "तूं नहीउं मैं नाहीं वे सज्जणा, तूं नहीउं मैं नाहीं ।"
                ],
                "hindi_gloss": "बुल्ल्हा (बुल्लेशाह कहता है) शहु (प्रभु-प्रियतम) घर आया साडे (हमारे घर पधार चुका है), जिन्दड़ी (अपनी इस जीवात्मा को) घोल घुमाईं (उस पर न्योछावर/बलिहार कर दिया है)। तूं नहीउं मैं नाहीं वे सज्जणा, तूं नहीउं मैं नाहीं ।",
                "english_gloss": "बुल्ल्हा शहु (Bulleh's King!) घर आया साडे (has arrived in our very home), जिन्दड़ी घोल घुमाईं (I have sacrificed and surrendered my soul unto Him). तूं नहीउं मैं नाहीं वे सज्जणा, तूं नहीउं मैं नाहीं ।",
                "poetic_hindi": "बुल्ल्हा कहे, शाह घर आया, जिन्दड़ी वार बिहाई;\nतू नहीं, मैं भी नहीं सजन! तू नहीं, मैं नाहीं!",
                "poetic_english": "Bulleh says: the King has stepped into our home divine;\nI cast my soul in sacrifice, and merge my heart with Thine!\nNeither art Thou, nor am I, Love! No distance lies between!"
            }
        ],
        "sufi_commentary": "Kafi 145 is the zenith of mystical deconstruction. Most theological and religious literature presupposes a duality: the worshipper ('I') and the worshipped ('Thou'). Even in intense love, conventional poetry maintains the lover who yearns and the beloved who is sought. Bulleh Shah demolishes this final duality with the radical refrain: 'तूं नहीउं मैं नाहीं' (Neither art Thou, nor am I). When the false ego-identity ('I') dissolves in Fana, the projection of an external, separate God ('Thou') simultaneously evaporates. What remains is only Pure Consciousness, non-dual Being. Bulleh captures this seamless immanence in everyday acts: when speech arises, it is the One speaking through the instrument; when silence settles, it is the One resting in stillness; when sleep overtakes the body, the Divine sleeps; when feet move upon the road, the Divine walks. The opening simile—'खोले दे परछावें वांङू' (like the shadow of a crumbling wall)—is magnificent: just as the shadow cannot be separated from the wall, yet possesses no independent substance of its own, the individual psyche is merely an insubstantial contour of the One Infinite Reality."
    }
]

# Lexicon updates for batch 141-145
new_lexicon_entries = {
    "तांघ": {
        "gurmukhi": "ਤਾਂਘ",
        "hindi": "तीव्र उत्कंठा, तड़प, विरह-वेदना",
        "english": "Intense yearning, deep longing, yearning ache",
        "context": "तांघ माही दी जलियां (Kafi 141)"
    },
    "सधराई": {
        "gurmukhi": "ਸਧਰਾਈ",
        "hindi": "इच्छुक, लालायित, साध भरी",
        "english": "Filled with deep wish, longing",
        "context": "पार वंञन नूं मैं सधराई (Kafi 141)"
    },
    "मनतारू": {
        "gurmukhi": "ਮਨਤਾਰੂ",
        "hindi": "अनाड़ी तैराक, तैरने में असमर्थ",
        "english": "Incompetent swimmer, novice at swimming",
        "context": "मैं मनतारू सार की जाणां (Kafi 141)"
    },
    "तुल्हा": {
        "gurmukhi": "ਤੁੱਲ੍ਹਾ",
        "hindi": "लकड़ी या बांसों का बना कच्चा बेड़ा",
        "english": "Raft made of logs or reeds",
        "context": "वंझ चप्पा ना तुल्हा पुराणा (Kafi 141)"
    },
    "बहुड़ीं": {
        "gurmukhi": "ਬਹੁੜੀਂ",
        "hindi": "आकर रक्षा कर, सुध ले, सहायता कर",
        "english": "Come to aid, rescue, rush to help",
        "context": "बहुड़ीं वे तबीबा मैंडी जिन्द गईआ (Kafi 142)"
    },
    "वदाण": {
        "gurmukhi": "ਵਦਾਣ",
        "hindi": "लुहार का भारी हथौड़ा / घन",
        "english": "Blacksmith's heavy sledgehammer",
        "context": "इह सिर आया ए मेरा हेठ वदाणां (Kafi 142)"
    },
    "सावे सूहे": {
        "gurmukhi": "ਸਾਵੇ ਸੂਹੇ",
        "hindi": "हरे और गहरे लाल (सुहाग व आध्यात्मिक नवजीवन के रंग)",
        "english": "Emerald green and bright crimson bridal garments",
        "context": "जिस पहनाए सानूं सावे सूहे (Kafi 142)"
    },
    "टूने कामन": {
        "gurmukhi": "ਟੂਣੇ ਕਾਮਣ",
        "hindi": "जादू-टोने, वशीकरण मन्त्र, तंत्र-साधना",
        "english": "Love-spells, charms, incantations, folk sorcery",
        "context": "टूने कामन करके नी मैं प्यारा यार मनावांगी (Kafi 143)"
    },
    "हरमल": {
        "gurmukhi": "ਹਰਮਲ",
        "hindi": "हरमल (धूप व टोने-टोटके में प्रयुक्त एक औषधीय पौधा/बीज)",
        "english": "Wild rue seeds (used in exorcism and protective fumigation)",
        "context": "इश्क अंगीठी हरमल तारे (Kafi 143)"
    },
    "शहर खमोशां": {
        "gurmukhi": "ਸ਼ਹਿਰ ਖ਼ਮੋਸ਼ਾਂ",
        "hindi": "कब्रिस्तान, मौन का नगर",
        "english": "The City of Silence (cemetery / graveyard)",
        "context": "शहर खमोशां दे चल वस्सीए (Kafi 144)"
    },
    "खोला": {
        "gurmukhi": "ਖੋਲਾ",
        "hindi": "खंडहर, गिरा हुआ पुराना मकान",
        "english": "Ruined house, dilapidated crumbling wall",
        "context": "खोले दे परछावें वांङू (Kafi 145)"
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
        "last_processed_kafi_id": 145,
        "completed_count": 145,
        "total": 160,
        "next_kafi_id": 146,
        "status": "in_progress"
    }
    with open(CHECKPOINT_PATH, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print("Checkpoint updated: 145/160 completed. Next ID: 146")

if __name__ == "__main__":
    save_batch()
