# -*- coding: utf-8 -*-
"""
Master Builder for Sant Kabir's 84 Timeless Dohas (Popular Tradition).
Outputs scripts/kabir/kabir_doha_data.py with authentic metered Hindi poetic verse,
elevated lyrical English verse (STRICT 0 Devanagari), and deep socio-spiritual commentary.
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT_FILE = os.path.join(BASE_DIR, "scripts", "kabir", "kabir_doha_data.py")

# Raw text mapping for all 84 Dohas with bespoke themes, poetic translations, and commentary
DOHA_SPECS = {
    1: {
        "theme_hi": "अंतर्यामी प्रभु और आत्म-समर्पण",
        "theme_en": "The Indwelling Lord and Surrender of the Soul",
        "title_hi": "दोहा 1: अन्तर्यामी एक तुम, आत्मा के आधार",
        "title_en": "Doha 1: The Indwelling Lord, Foundation of the Soul",
        "v_hi": "हे अंतर्यामी प्रभु! केवल तू ही इस आत्मा का एकमात्र आधार और प्राण है,\nयदि तू ही मेरा हाथ छोड़ दे, तो इस भवसागर से भला कौन मुझे पार उतारेगा?",
        "v_en": "Thou alone art the Indwelling Knower, the soul's foundation and grace;\nIf Thou shouldst release my hand, who else shall ferry me across this cosmic space?",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **घट-घट वासी चैतन्य**: कबीर बाह्य आकाश में बैठे ईश्वर को नहीं, अंतरात्मा में रमने वाले राम को पुकारते हैं।\n2. **शरण-गति का भाव**: सांसारिक रिश्ते स्वार्थ टूटने पर बिखर जाते हैं; केवल परमात्मा का अखंड सहारा ही जीव को भवसागर से पार लगाता है।"
    },
    2: {
        "theme_hi": "मानव जन्म का उद्देश्य और आत्म-जागरण",
        "theme_en": "The Purpose of Mortal Life and Spiritual Awakening",
        "title_hi": "दोहा 2: आया था किस काम को, तू सोया चादर तान",
        "title_en": "Doha 2: For What Purpose Didst Thou Arrive",
        "v_hi": "हे नासमझ जीव! तू इस संसार में किस परम कर्तव्य को सिद्ध करने आया था, और चादर तानकर मोह की नींद में सो रहा है?\nअरे गाफ़िल! अब अपनी चेतना को संभाल, जाग और अपने वास्तविक आत्म-स्वरूप को पहचान!",
        "v_en": "For what noble quest didst thou arrive, yet sleepest covered in heedless slumber deep?\nAwaken thy dormant consciousness, O wanderer, and thy true divine essence know and keep!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **चेतना का विस्मरण**: मनुष्य संसार में आत्म-साक्षात्कार के लिए आता है, किंतु माया के प्रपंच में उलझकर अपने मूल स्वरूप को भूल जाता है।\n2. **गाफिल मन को चेतावनी**: कबीर का उपदेश मनुष्य को प्रमाद की निद्रा से झकझोर कर आत्म-बोध की ओर अग्रसर करता है।"
    },
    3: {
        "theme_hi": "मृत्यु की समरसता और कर्मों की गति",
        "theme_en": "The Universal Leveler of Death and Destiny",
        "title_hi": "दोहा 3: आए हैं सो जाएँगे, राजा रंक फकीर",
        "title_en": "Doha 3: All Who Arrive Shall Depart",
        "v_hi": "जो भी इस नश्वर जग में आया है, वह अवश्य विदा होगा—चाहे राजा हो, कंगाल हो या फकीर;\nसत्कर्मी प्रभु के दिव्य सिंहासन पर आरूढ़ होकर जाते हैं, जबकि पापी यम की बेड़ियों में जकड़े खींचे जाते हैं!",
        "v_en": "All who have entered this mortal realm must depart—the monarch, beggar, and ascetic alike;\nOne ascends upon a throne of light, while another is bound in chains when Death's summons strike!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **काल की निरपेक्षता**: मृत्यु किसी के पद, संपत्ति या कुल का भेद नहीं करती; सब अंत में धूल में मिल जाते हैं।\n2. **कर्म-फल की व्यवस्था**: परलोक की यात्रा भौतिक ऐश्वर्य से नहीं, बल्कि सत्य और नाम-स्मरण के संस्कारों से तय होती है।"
    },
    4: {
        "theme_hi": "विनम्रता की महिमा और अहंकार का अभाव",
        "theme_en": "The Glory of Humility and Drought of Pride",
        "title_hi": "दोहा 4: ऊँचे पानी न टिके, नीचे ही ठहराय",
        "title_en": "Doha 4: Water Rests Not Upon High Heights",
        "v_hi": "अहंकार के ऊंचे शिखरों पर ज्ञान का जल कभी नहीं ठहरता, वह तो सदा नीचे की ओर ही रुकता है;\nजो मन से विनीत और झुककर रहता है, वह तृप्त होकर पीता है, और जो अकड़कर ऊंचा खड़ा रहता है, वह प्यासा ही भटकता है!",
        "v_en": "Water tarries not upon steep lofty heights; downward into low hollows it flows and abides;\nHe who bows low drinks his fill of nectar, while the haughty remains parched in vanity and pride!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **जल और विनम्रता**: जल सदा निचले धरातल को अपनाता है; वैसे ही परमात्मा की कृपा केवल निरहंकारी अंतःकरण में ठहरती है।\n2. **पर्वत का सूखापन**: घमंड का शिखर कभी भक्ति के अमृत को संजो नहीं सकता।"
    },
    5: {
        "theme_hi": "मधुर वचन और अंतर्मन की शीतलता",
        "theme_en": "Sweet Speech and Inner Tranquility",
        "title_hi": "दोहा 5: ऐसी वाणी बोलीए, मन का आपा खोय",
        "title_en": "Doha 5: Speak Such Words That Melt the Ego",
        "v_hi": "मन के समस्त अहंकार और दंभ को त्यागकर ऐसी मधुर व हितकारी वाणी का उच्चारण करना चाहिए,\nजो सुनने वाले दूसरों के हृदय को भी शांत और शीतल कर दे, और अपने स्वयं के अंतःकरण को भी परम शांति प्रदान करे!",
        "v_en": "Speak such gentle and compassionate words, surrendering the mind's haughty pride;\nThat cools the aching heart of the listener, and brings soothing peace to thine own soul inside!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **आपा खोने का भाव**: जब तक भीतर 'मैं' रहता है, तब तक वाणी में विष रहता है; अहंकार मिटते ही वाणी अमृत बन जाती है।\n2. **पारस्परिक कल्याण**: प्रेमपूर्ण संवाद सामाजिक सौहार्द और व्यक्तिगत आत्म-शांति दोनों का जनक है।"
    },
    6: {
        "theme_hi": "अंतर्मन की आंतरिक माला और बाह्य ढोंग",
        "theme_en": "The Rosary of the Heart and Worldly Pretence",
        "title_hi": "दोहा 6: कबिरा माला मनहि की, और संसारी भेख",
        "title_en": "Doha 6: Turn the Rosary of the Inner Heart",
        "v_hi": "कबीर कहते हैं—सच्ची जपमाला तो अंतर्मन की एकाग्रता है, बाकी सब तो संसार को दिखाने वाले बाह्य वेश हैं;\nयदि केवल लकड़ी के मनके फेरने से ही परमात्मा मिल जाते, तो कुएं के रहट के गले में बंधी मालाओं को कब का ईश्वर मिल गया होता!",
        "v_en": "The true rosary is of the inner mind, O Kabir—all else is worldly guise and deceit;\nIf spinning beads alone brought the Divine, the Persian wheel's pots would have touched His feet!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **रहट का दृष्टांत**: कुएं का रहट निरंतर घूमता है पर जड़ ही रहता है; उसी प्रकार यांत्रिक जप से चेतना का उत्थान नहीं होता।\n2. **मन की माला**: सुरति को प्रभु-स्मरण में पिरोना ही सच्ची भक्ति है।"
    },
    7: {
        "theme_hi": "नश्वर देह का सदुपयोग और साधु-सेवा",
        "theme_en": "Noble Utilization of the Mortal Frame",
        "title_hi": "दोहा 7: कबिरा यह तन जात है, सके तो ठौर लगा",
        "title_en": "Doha 7: This Transient Body Is Rapidly Passing",
        "v_hi": "कबीर कहते हैं—यह नश्वर शरीर तो प्रतिपल मृत्यु की ओर भागा जा रहा है, यदि सामर्थ्य हो तो इसे किसी सार्थक कार्य में लगा ले;\nया तो निष्कपट भाव से संतों की सेवा कर, या फिर अपने अंतर्मन से गोविंद के पावन गुणों का गान कर!",
        "v_en": "This mortal clay is swiftly passing away—anchor it to a worthy shore while thou may;\nEither serve the righteous saints in humility, or sing the virtues of Govinda day by day!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **देह की नश्वरता**: क्षणभंगुर शरीर को भोगों में नष्ट करने के स्थान पर परोपकार और प्रभु-भक्ति में लगाना ही जीवन की सार्थकता है।\n2. **सत्संगति और कीर्तन**: संतों का संग और ईश्वर-स्मरण ही आत्मा को अमरता का द्वार दिखाते हैं।"
    },
    8: {
        "theme_hi": "काष्ठ की जपनी की व्यर्थता और हृदय-स्मरण",
        "theme_en": "Vanity of Wooden Beads and Heart-Felt Remembrance",
        "title_hi": "दोहा 8: कबीरा जपनी काठ की, क्या दिखलावे लोय",
        "title_en": "Doha 8: What Good Are Wooden Beads to Flaunt",
        "v_hi": "कबीर कहते हैं—हाथ में लकड़ी की माला लेकर संसार के लोगों को क्या ढोंग दिखा रहा है?\nयदि तेरे हृदय के भीतर प्रभु का नाम नहीं धड़कता, तो इस निर्जीव काष्ठ की माला को फेरने से भला क्या लाभ होगा?",
        "v_en": "Flaunting a rosary carved of dry wood before worldly eyes, what dost thou seek to gain?\nIf the inner heart chants not the Beloved Name, turning these wooden beads is all in vain!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **आडंबर का खंडन**: कबीर पाखंडी धार्मिकता को लताड़ते हैं; धर्म हृदय की पवित्रता है, हाथ की अंगुलियों का खेल नहीं।\n2. **हृदय का नाम**: जब नाम चित्त में बस जाता है, तब किसी बाह्य साधन की आवश्यकता नहीं रहती।"
    },
    9: {
        "theme_hi": "सद्गुरु की सर्वोच्च सत्ता और अभय आश्रय",
        "theme_en": "Supreme Sanctuary of the True Master",
        "title_hi": "दोहा 9: कबीरा ते नर अन्ध हैं, गुरु को कहते और",
        "title_en": "Doha 9: Blind Are Those Who Deem the Guru Mere Mortal",
        "v_hi": "कबीर कहते हैं—वे मनुष्य ज्ञान की दृष्टि से सर्वथा अंधे हैं, जो सद्गुरु को एक साधारण मनुष्य समझकर ईश्वर से भिन्न मानते हैं;\nयदि ईश्वर रुष्ट हो जाए तो सद्गुरु की शरण में रक्षा हो जाती है, परंतु यदि सद्गुरु ही रुष्ट हो जाएं, तो तीनों लोकों में कहीं कोई आश्रय नहीं मिलता!",
        "v_en": "Blind indeed are those foolish mortals who regard the Master as a mere human form apart;\nIf God is displeased the Guru offers refuge, but if the Guru turns away no shelter heals the heart!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **गुरु-तत्त्व की महिमा**: सद्गुरु ज्ञान का साक्षात स्वरूप हैं जो अज्ञान-अंधकार को मिटाकर ब्रह्म से साक्षात्कार कराते हैं।\n2. **परम आश्रय**: गुरु की कृपा के बिना साधना का कोई भी मार्ग सुगम नहीं हो सकता।"
    },
    10: {
        "theme_hi": "धैर्य का महा-संतोष और तृष्णा का भटकाव",
        "theme_en": "Noble Patience of the Elephant versus Restless Greed",
        "title_hi": "दोहा 10: कबीरा धीरज के धरे, हाथी मन भर खाय",
        "title_en": "Doha 10: With Steady Patience the Elephant Feeds",
        "v_hi": "कबीर कहते हैं—अपने सहज धैर्य और गंभीरता के बल पर विशाल गजराज बैठकर मन भर अन्न सम्मानपूर्वक पाता है;\nजबकि अधीर और चंचल कुत्ता केवल एक सूखे टुकड़े के लोभ में घर-घर दुत्कार खाता भटकता है!",
        "v_en": "Holding steadfast patience, the majestic elephant feeds upon hearty bundles in peace;\nWhile for a single dry crust the restless hound begs from door to door without cease!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **हाथी और श्वान का रूपक**: हाथी गरिमा और धैर्य का प्रतीक है, कुत्ता तृष्णा और दीनता का।\n2. **संतोष ही सुख**: जो ईश्वर के विधान पर भरोसा रखता है, वह सम्मान पाता है; लोभी दर-दर अपमानित होता है।"
    },
    11: {
        "theme_hi": "मृत्यु की आसन्नता और देह की म्यान",
        "theme_en": "Imminence of Death and the Empty Scabbard",
        "title_hi": "दोहा 11: कबीरा सोया क्या करे, उठि न भजे भगवान",
        "title_en": "Doha 11: Why Dost Thou Slumber, O Kabir",
        "v_hi": "कबीर कहते हैं—हे जीव! तू मोह की नींद में क्यों पड़ा है, उठकर भगवान का भजन क्यों नहीं करता?\nजब यमदूत आकर आत्मा रूपी तलवार को खींचकर ले जाएंगे, तो यह शरीर रूपी म्यान यहीं धूल में पड़ी रह जाएगी!",
        "v_en": "Why dost thou lie in heedless slumber, O Kabir—arise and praise the Lord Divine;\nWhen the Messengers of Death snatch the soul's blade, the body's empty sheath shall rot in time!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **म्यान और तलवार का रूपक**: शरीर केवल म्यान है, प्राण और चेतना तलवार हैं। म्यान का कोई स्वतंत्र मूल्य नहीं है।\n2. **काल की पुकार**: मृत्यु कभी पूर्व सूचना देकर नहीं आती; हर श्वास में नाम-स्मरण ही एकमात्र सुरक्षा है।"
    },
    12: {
        "theme_hi": "कथनी और करनी का अंतर",
        "theme_en": "The Chasm between Words and Realization",
        "title_hi": "दोहा 12: कहता तो बहुत मिला, गहता मिला न कोय",
        "title_en": "Doha 12: Many Preach Words, Yet None Practice",
        "v_hi": "उपदेश देने वाले और बातें बनाने वाले तो संसार में बहुत मिले, किंतु सत्य को आचरण में धारण करने वाला कोई न मिला;\nकबीर कहते हैं—उस बोलने वाले को जाने दो, जो सत्य को जीवन में अंगीकार ही नहीं करता!",
        "v_en": "Many are found who preach lofty words, yet scarce is one who lives the sacred art;\nLet that empty speaker depart, who holds not truth within his practicing heart!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **कथनी-करनी की एकता**: आध्यात्मिक जीवन मौखिक पांडित्य का नाम नहीं, बल्कि चरित्र और अंतःकरण के शुद्धिकरण का नाम है।\n2. **गहनता का अभाव**: जो केवल बोलता है पर जीता नहीं, वह स्वयं भी अंधकार में रहता है और दूसरों को भी भटकाता है।"
    },
    13: {
        "theme_hi": "अद्वैत की पराकाष्ठा और मौन समाधि",
        "theme_en": "The Summit of Non-Duality and Silent Samadhi",
        "title_hi": "दोहा 13: कहना सो कह दिया, अब कुछ कहा न जाय",
        "title_en": "Doha 13: All That Could Be Uttered Has Been Said",
        "v_hi": "जो कुछ वाणी से कहा जा सकता था वह सब कह दिया, अब उस परम मौन का वर्णन शब्दों से नहीं किया जा सकता;\nद्वैत का भ्रम मिट गया और केवल वह एक ही शेष रह गया, जैसे नदी की लहर नदी के जल में ही समा जाती है!",
        "v_en": "All that could be spoken has been uttered, now speech dissolves in silent ecstasy;\nDuality has vanished and the One remains, like a surging wave merging back into the sea!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **लहर और दरिया (The Wave and the Ocean)**: आत्मा परमात्मा से अलग नहीं है; अविद्या के मिटते ही वह पूर्ण ब्रह्म में लीन हो जाती है।\n2. **अनिर्वचनीय समाधि**: परम सत्य वाणी का विषय नहीं, अपरोक्ष अनुभूति का विषय है ('गूँगे का गुड़')।"
    },
    14: {
        "theme_hi": "सच्ची भक्ति की वीरता और कुल-जाति का त्याग",
        "theme_en": "Heroism of Pure Devotion and Shedding Pedigree",
        "title_hi": "दोहा 14: कामी, क्रोधी, लालची, इनसे भक्ति न होय",
        "title_en": "Doha 14: The Lustful and Greedy Cannot Attain Devotion",
        "v_hi": "कामी, क्रोधी और लोभी व्यक्तियों से प्रभु की सच्ची भक्ति कभी नहीं हो सकती;\nभक्ति तो केवल वही आध्यात्मिक शूरवीर कर सकता है, जो अपनी जाति, वर्ण और कुल के अहंकार को पूर्णतः विसर्जित कर दे!",
        "v_en": "The lustful, wrathful, and covetous can never walk the razor path of devotion pure;\nOnly that heroic warrior can worship, who casts away caste, pedigree, and worldly lure!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **भक्ति एक युद्ध है**: भक्ति कायरों का काम नहीं है; यह आंतरिक विकारों और सामाजिक अभिमान के विरुद्ध परम शूरवीरता है।\n2. **जाति-वर्ण का विसर्जन**: परमात्मा के दरबार में कुल और वर्ण का कोई महत्व नहीं है; वहाँ केवल प्रेम और निष्कामता की परख होती है।"
    },
    15: {
        "theme_hi": "काल रूपी घुन और देह का क्षय",
        "theme_en": "The Termite of Time and the Fragile Frame",
        "title_hi": "दोहा 15: काया काठी काल घुन, जतन-जतन सो खाय",
        "title_en": "Doha 15: The Body Is Wood and Time Is the Termite",
        "v_hi": "यह मानव शरीर लकड़ी के लट्ठे के समान है और काल रूपी घुन इसे भीतर ही भीतर धीरे-धीरे खोखला कर रहा है;\nयह काया तो केवल परम वैद्य ईश्वर के अधीन है, सांसारिक वैद्य इसके रहस्य और अंत को कभी नहीं जान सकते!",
        "v_en": "This physical frame is a block of wood, which Time like a termite eats away unseen;\nThe secret of this body rests with the Divine Physician alone, beyond what mortal doctors glean!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **दीमक का रूपक**: जैसे घुन लकड़ी को बाहर से सुंदर रखते हुए भीतर से नष्ट कर देता है, वैसे ही काल देह की आयु को निरंतर हर रहा है।\n2. **परम वैद्य**: भौतिक औषधियां आत्मा को अमर नहीं बना सकतीं; केवल राम-नाम की संजीवनी ही जीव को जन्म-मरण से मुक्त करती है।"
    },
    16: {
        "theme_hi": "समय की महत्ता और तत्क्षण साधना",
        "theme_en": "Preciousness of Time and Immediate Action",
        "title_hi": "दोहा 16: काल करे सो आज कर, आज करे सो अब",
        "title_en": "Doha 16: What Must Be Done Tomorrow, Do Today",
        "v_hi": "जो शुभ कार्य कल करना है उसे आज ही कर ले, और जो आज करना है उसे इसी क्षण संपन्न कर;\nक्योंकि अगले ही पल में प्रलय और मृत्यु आ सकती है, फिर भला तू अपने उद्धार का साधन कब करेगा?",
        "v_en": "What must be done on the morrow do today, and what is due today accomplish right now;\nIn a fleeting instant doom may strike, then how shalt thou fulfill thy sacred vow?",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **क्षणभंगुरता का बोध**: कल कभी नहीं आता; कल पर टालना मन का सबसे बड़ा छल है जो मनुष्य को चौरासी के चक्र में फंसाए रखता है।\n2. **वर्तमान का महत्व**: केवल वर्तमान क्षण ही हमारे हाथ में है; इसी क्षण में परमात्मा का स्मरण संभव है।"
    },
    17: {
        "theme_hi": "कुटिल वाणी का दाह और संत वाणी का अमृत",
        "theme_en": "The Scorching of Bitter Words and Nectar of Saints",
        "title_hi": "दोहा 17: कुटिल वचन सबसे बुरा, जारि करे तन छार",
        "title_en": "Doha 17: Malicious Words Are the Cruelest Blaze",
        "v_hi": "कुटिल और कड़वे वचन संसार में सबसे घातक होते हैं, जो मनुष्य के तन और मन को जलाकर भस्म कर देते हैं;\nइसके विपरीत संतों के पावन वचन अमृत जल के समान होते हैं, जिनकी शीतल धारा बरसकर अंतरात्मा को तृप्त कर देती है!",
        "v_en": "Malicious speech is the cruelest fire, turning both body and mind to ash and pain;\nWhile the gentle word of the saint is nectar pure, pouring down in a soothing, healing rain!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **शब्द का प्रभाव**: शब्द में सृजन और संहार दोनों की शक्ति है। कड़वी वाणी हृदय में स्थायी घाव कर देती है।\n2. **संत वाणी की संजीवनी**: सद्गुरु के वचन भवताप से तपे हुए जीव को शांति और मुक्ति प्रदान करते हैं।"
    },
    18: {
        "theme_hi": "सांस-सांस में सिमरन और देह की अनित्यता",
        "theme_en": "Remembrance with Every Breath and Transient Clay",
        "title_hi": "दोहा 18: क्या भरोसा देह का, बिनस जात छिन मांहि",
        "title_en": "Doha 18: What Faith Can Rest Upon This Fragile Frame",
        "v_hi": "इस नश्वर शरीर का भला क्या भरोसा है, जो एक क्षण में बुलबुले के समान नष्ट हो जाता है;\nइसलिए प्रत्येक श्वास के साथ परमात्मा का निरंतर स्मरण कर, इसके अतिरिक्त मुक्ति का कोई दूसरा यत्न नहीं है!",
        "v_en": "What faith can rest upon this mortal clay, which dissolves like a bubble in a fleeting breath?\nWith every inhalation chant the Beloved Name—no other refuge shields the soul from death!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **अजपा-जाप का रहस्य**: श्वास ही जीवन की डोरी है; जब तक श्वास में नाम नहीं जुड़ता, तब तक जीवन व्यर्थ व्यतीत हो रहा है।\n2. **अनित्यता का यथार्थ**: देह का कोई भरोसा नहीं, इसलिए साधना को किसी भविष्य पर नहीं छोड़ा जा सकता।"
    },
    19: {
        "theme_hi": "गाली की प्रतिक्रिया और साधुता की कसौटी",
        "theme_en": "The Curse of Abuses and the Triumph of Forbearance",
        "title_hi": "दोहा 19: गारी ही सों ऊपजे, कलह कष्ट और मींच",
        "title_en": "Doha 19: From Spiteful Abuse Arises Strife and Death",
        "v_hi": "अपशब्दों और गालियों से ही कलह, पीड़ा और अंततः विनाशकारी मृत्यु उत्पन्न होती है;\nजो अपमान को सहकर हार मान लेता है वही सच्चा साधु है, और जो बदला लेने पर अड़ा रहता है वही अधम और नीच है!",
        "v_en": "From bitter insult and verbal abuse springs discord, agony, and deadly strife;\nHe who yields in humble peace is the true saint, while he who retaliates soils his life!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **हारने में जीत**: कबीर की दृष्टि में सांसारिक विवाद में झुक जाना कायरता नहीं, बल्कि आत्मिक बल और साधुता का सर्वोच्च प्रमाण है।\n2. **क्रोध का शमन**: गाली का उत्तर मौन और क्षमा है; प्रतिक्रिया करना अहंकार का पोषण करना है।"
    },
    20: {
        "theme_hi": "सद्गुरु की अनन्य महिमा और गोविंद का बोध",
        "theme_en": "Supreme Glory of the Master Who Revealed the Lord",
        "title_hi": "दोहा 20: गुरु गोविन्द दोनों खड़े, काके लागूं पाँय",
        "title_en": "Doha 20: Master and the Lord Both Stand Before Me",
        "v_hi": "मेरे सम्मुख सद्गुरु और साक्षात परमात्मा गोविंद दोनों खड़े हैं, मैं धर्मसंकट में हूँ कि पहले किसके चरणों का स्पर्श करूँ;\nहे सद्गुरु! मैं आप पर सौ-सौ बार न्योछावर होता हूँ, जिन्होंने कृपा करके मुझे गोविंद के सत्य स्वरूप का साक्षात दर्शन कराया!",
        "v_en": "Before me stand both the Guru and the Lord Supreme—unto whose feet should I first bow?\nAll sacrifice am I unto my Master, who revealed the Beloved's path and showed me how!",
        "comm": "### दार्शनिक एवं आध्यात्मिक विश्लेषण (Philosophical Commentary)\n1. **भारतीय दर्शन का अमर दोहा**: गुरु गोविंद से भी ऊंचा स्थान पाते हैं क्योंकि यदि गुरु ज्ञान का चक्षु न खोलते, तो जीव कभी गोविंद को पहचान ही न पाता।\n2. **कृतज्ञता की पराकाष्ठा**: शिष्य का सर्वस्व गुरु के चरणों में समर्पित होना ही मोक्ष का मूल है।"
    }
}

print(f"Loaded {len(DOHA_SPECS)} doha specifications.")

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dohas_21_50 import DOHAS_21_50
from dohas_51_84 import DOHAS_51_84

# Combine all 84 Dohas
ALL_DOHAS = {}
ALL_DOHAS.update(DOHA_SPECS)
ALL_DOHAS.update(DOHAS_21_50)
ALL_DOHAS.update(DOHAS_51_84)

print(f"Total Dohas assembled: {len(ALL_DOHAS)} / 84")
assert len(ALL_DOHAS) == 84, f"Expected 84 Dohas, got {len(ALL_DOHAS)}"

# Audit for Devanagari in English verse
dev_regex = re.compile(r'[\u0900-\u097F]')
for num, d in ALL_DOHAS.items():
    v_en = d["v_en"]
    m = dev_regex.search(v_en)
    if m:
        raise ValueError(f"Doha {num} contains Devanagari in English verse: {m.group(0)}")

# Write to scripts/kabir/kabir_doha_data.py
with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\n')
    f.write("Master Curated Data for All 84 Timeless Dohas of Sant Kabir Das.\n")
    f.write("Contains authentic metered Hindi poetic verse, lyrical English verse (STRICT 0 Devanagari),\n")
    f.write("and scholarly socio-spiritual commentary.\n")
    f.write('"""\n\n')
    f.write("KABIR_DOHA_DATA = ")
    json.dump(ALL_DOHAS, f, ensure_ascii=False, indent=2)
    f.write("\n\n")
    f.write('if __name__ == "__main__":\n')
    f.write('    print(f"Loaded {len(KABIR_DOHA_DATA)} timeless Dohas of Sant Kabir Das.")\n')

print(f"Successfully generated {OUT_FILE} ({os.path.getsize(OUT_FILE)} bytes) with all 84 Dohas!")

