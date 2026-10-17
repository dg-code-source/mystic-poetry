# -*- coding: utf-8 -*-
"""
Generates the complete, authentic Trilingual Master Edition for all 56 Dohre of Baba Bulleh Shah:
- 100% complete word-by-word Hindi gloss (zero blank parentheses)
- 100% complete word-by-word English gloss
- Metered Poetic Hindi translations for all 56 couplets
- Metered Poetic English translations for all 56 couplets
- In-depth Sufi & Philosophical commentary for all 56 couplets
- Updates data/other_works/dohre.json and Bulleh_Shah_Dohre_Trilingual.md
"""

import os
import sys
import json
import re

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from sufi_gloss_engine import generate_line_gloss

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DATA_DIR = os.path.join(BASE_DIR, "data", "other_works")
OUTPUT_MD = os.path.join(BASE_DIR, "Bulleh_Shah_Dohre_Trilingual.md")

# Load raw dohre
with open(os.path.join(BASE_DIR, "data", "raw_extracted", "dohre.json"), "r", encoding="utf-8") as f:
    raw_dohre = json.load(f)

# Comprehensive curation for all 56 Dohre
dohre_data = {
    1: {
        "theme": "आत्मानुभूति एवं घट-घट व्यापी ब्रह्म (Wahdat al-Wujud)",
        "poetic_hi": [
            "तन की अपने खबर नहीं, साजन की सुध कौन बताए?",
            "न मैं मिट्टी न मैं अग्नि, न जल-पवन मेरा रूप कहाए।",
            "कुप्पे में कंकड़ खड़कें, मूरख पूछें कौन यह बोले?",
            "बुल्ला! साईं घट-घट में ज्यों, आटे में नमक घुले!"
        ],
        "poetic_en": [
            "No news have I of my own flesh; who brings my Lover's grace?",
            "Nor earth, nor fire, nor air am I, nor water in this place.",
            "In hollow flask loose pebbles clink, fools ask who speaks within;",
            "Bulleh! The Lord fills every heart, as salt in meal blends in!"
        ],
        "commentary": "बुल्ले शाह कहते हैं कि जब तक मनुष्य को अपने वास्तविक आत्म-स्वरूप का भान नहीं होता, वह परमात्मा को कैसे जान सकता है? नश्वर देह पंचतत्वों की बनी है, पर आत्म-चेतना इन सबसे परे है। जैसे कुप्पे (मशक) में कंकड़ खड़कने पर मूर्ख पूछते हैं कौन बोल रहा है, वैसे ही ईश्वर घट-घट में आटे में नमक की भाँति रचा-बसा है।"
    },
    2: {
        "theme": "अलस्त का अहद एवं रूहानी कर्ज़ (Divine Covenant)",
        "poetic_hi": [
            "अल्लाह से मैंने ऋण लिया, तू मेरा हुआ कर्जदार,",
            "वहाँ तूने पोषण किया, जहाँ न थी किसी को सार।",
            "वहाँ से हम यहाँ आए, जब पहले रोजी आई द्वार,",
            "बुल्ले शाह आशिक उसका, जिसने पाया हक़-दीदार!"
        ],
        "poetic_en": [
            "A loan I drew from God on high, yet You my debtor stand,",
            "You nurtured me in unseen womb, beyond all mortal land.",
            "From thence we journeyed to this world, as sustenance paved the way;",
            "Bulleh Shah is lover of the one who found Truth's living ray!"
        ],
        "commentary": "यह दोहा जीव और ईश्वर के अनादि प्रेम-संबंध का रहस्य उद्घाटित करता है। परमात्मा ने गर्भ के अंधकार में जीव का पोषण किया और इस संसार में आने से पहले ही उसकी रोज़ी (प्रारब्ध) निर्धारित कर दी। सच्चा प्रेमी वही है जिसने इस परम सत्य (तहक़ीक़-ए-हक़ीक़त) का साक्षात्कार किया है।"
    },
    3: {
        "theme": "चार तत्वों का महल एवं अद्वैत लीला (Cosmic Theatre)",
        "poetic_hi": [
            "चार तत्वों का महल बनाकर, खुद ही अंदर बैठा आप,",
            "खुद ही कन्या, खुद ही बालक, खुद ही माता-पिता का जाप।",
            "खुद ही मरे और खुद ही जीवे, खुद ही करे विलाप-संताप,",
            "बुल्ला! कुदरत रब्ब की ऐसी, आप ही आप को जाने आप!"
        ],
        "poetic_en": [
            "Four elements formed His palace hall, within He entered alone,",
            "Himself the youth, Himself the maid, as parents Himself is known.",
            "Himself He dies, Himself He wakes, Himself laments the bier;",
            "Bulleh! Such is the play of God—Himself beholding clear!"
        ],
        "commentary": "सूफी अद्वैतवाद (वहदत-उल-वुजूद) का अनुपम चित्रण। परमात्मा ने चार तत्वों से यह सृष्टि-प्रासाद रचा और स्वयं ही इसमें प्रविष्ट होकर समस्त रूपों (स्त्री, पुरुष, माता, पिता) में लीला कर रहा है। जीवन और मृत्यु का यह नाटक उसी का आत्म-विस्तार है।"
    },
    4: {
        "theme": "कर्मकांड का तिरस्कार एवं अंतर का साक्षात्कार (Beyond Orthodoxy)",
        "poetic_hi": [
            "भट्ठी में झोंको नमाज़ें, कीचड़ सम रोज़े जान,",
            "कलमे पर स्याही फिर गई, जब अंतर मिला भगवान!",
            "बुल्ले शाह! प्रियतम अंदर पाया, बाहर भटके अज्ञान!"
        ],
        "poetic_en": [
            "Into the kiln cast formal prayers, like mud let fastings lie,",
            "Black ink has washed the sacred creed, as Truth unveiled the eye!",
            "Bulleh Shah found the Lord within, while world roams blind and high!"
        ],
        "commentary": "बुल्ले शाह का क्रांतिकारी उद्घोष। वे कहते हैं कि यदि हृदय में निष्कपट प्रेम नहीं, तो केवल बाह्य धार्मिक अनुष्ठान (नमाज़, रोज़ा) व्यर्थ का भार हैं। जब परमात्मा का साक्षात्कार अंतःकरण में हो गया, तो समस्त बाह्य औपचारिकताओं से मुक्ति मिल जाती है।"
    },
    5: {
        "theme": "कसूर का खेल एवं सत्य की तलवार (Martyrdom of Truth)",
        "poetic_hi": [
            "बुल्ला! कसूर नाम कसूर है, मुख से न निकले बात,",
            "सच्चों की गर्दन कटती यहाँ, झूठे करें विलास की रात!"
        ],
        "poetic_en": [
            "Bulleh! 'Kasur' is fault in name; no tongue may utter word,",
            "The truthful have their necks struck down, while liars feast unheard!"
        ],
        "commentary": "बुल्ले शाह अपने नगर कसूर के नाम पर श्लेष करते हैं। दुनिया का नियम उलटा है—यहाँ मंसूर-अल-हल्लाज जैसे सत्यवादी प्रेमियों को सूली दी जाती है, जबकि पाखंडी और चापलूस लोग ऐश्वर्य भोगते हैं।"
    },
    6: {
        "theme": "यार का बावरचीखाना (The Altar of Sacrifice)",
        "poetic_hi": [
            "बुल्ले चल यार के बावरचीखाने, जहाँ कत्लेआम मचे भारी,",
            "मोटे बकरे हलाल हों वहाँ, दुर्बलों की न बारी!"
        ],
        "poetic_en": [
            "To Lover's kitchen, Bulleh, haste, where slaughter knows no stay;",
            "Fat rams of ego bleed to death, the weak are turned away!"
        ],
        "commentary": "प्रेम का मार्ग आत्म-बलिदान की परीक्षा है। बावरचीखाना (वधशाला) उस स्थान का प्रतीक है जहाँ अहंकारी और अभिमानी 'मोटे बकरे' हलाल किए जाते हैं। जो साधक पूरी तरह समर्पित नहीं होता, उसे इस दिव्य वेदी पर स्वीकार नहीं किया जाता।"
    },
    7: {
        "theme": "मस्जिद बनाम आंतरिक पवित्रता (True Temple of Heart)",
        "poetic_hi": [
            "बुल्ले को लोग सिखावन दें, जा बैठ मस्जिद की छाँव,",
            "मस्जिद में क्या मिलना बंदे, जो दिल से न की नमाज़ का दाँव!",
            "बाहर से तन धोने से क्या, जो अंतर मैल न छूटी पाँव?",
            "बिन पूर्ण मुर्शिद बुल्ले शाह, गई व्यर्थ तेरी सब इबादत ठाँव!"
        ],
        "poetic_en": [
            "People advise poor Bulleh Shah: 'Go sit within the shrine!'",
            "What boots the mosque when heart beats cold, devoid of Love divine?",
            "What avails washing external limbs, when filth still clogs the soul?",
            "Without a Perfect Guide, O Bulleh, in vain your prayers roll!"
        ],
        "commentary": "मस्जिद की चारदीवारी में बैठने से ईश्वर नहीं मिलता जब तक मन का कल्मष (ईर्ष्या, द्वेष, लोभ) दूर न हो। पूर्ण मुर्शिद की कृपा के बिना केवल शारीरिक वज़ू और औपचारिक सिजदे निरर्थक हैं।"
    },
    8: {
        "theme": "चूल्हा बनाम बुल्हा (Humility & Selflessness)",
        "poetic_hi": [
            "बुल्ले से तो चूल्हा भला, जिस पर पकती रोटी-दाल,",
            "रुक-रुक कर फकीर मिल बैठें, खाएं तृप्त निहाल!"
        ],
        "poetic_en": [
            "Better than Bulleh is the hearth, where meals are baked and fed;",
            "Dervishes gather in the hall, content on morsels of bread!"
        ],
        "commentary": "परम विनम्रता की अभिव्यक्ति। बुल्ले शाह कहते हैं कि मिट्टी का चूल्हा मुझसे कहीं उत्तम है, क्योंकि वह भूखों का पेट भरता है और संतों-फ़कीरों की सेवा करता है। अहंकार से भरा मनुष्य इस निःस्वार्थ चूल्हे के बराबर भी नहीं।"
    },
    9: {
        "theme": "अंधों का देश (Where All Are Blind)",
        "poetic_hi": [
            "बुल्ले शाह! चल वहाँ चलें, जहाँ सारे हों अंधे लोग,",
            "न कोई अपनी कदर पहचाने, न कोई माने जाति का रोग!"
        ],
        "poetic_en": [
            "Bulleh Shah! Let us journey there, where all men sightless live,",
            "Where none shall weigh our lineage proud, nor praise or blame shall give!"
        ],
        "commentary": "संसार की संकीर्ण जातिवादी और सामाजिक प्रतिष्ठा से विरक्त होकर बुल्ले शाह ऐसे समाज की कामना करते हैं जहाँ कोई कुल और मर्यादा का झूठा दंभ न भरे। सूफी दृष्टि में यह बाह्य चक्षुओं को बंद कर अंतर्चक्षु खोलने का प्रतीक है।"
    },
    10: {
        "theme": "कुरान और जनेऊ में एक ही प्रियतम (Beyond Religious Dogma)",
        "poetic_hi": [
            "बुल्ले शाह! वह कौन है, उत्तम तेरा यार?",
            "उसी के हाथ कुरान है, उसी के गले जनेऊ-हार!"
        ],
        "poetic_en": [
            "Bulleh Shah! Who is that Lord, supreme Beloved of thine?",
            "In His one hand the Holy Book, round His neck thread divine!"
        ],
        "commentary": "सर्वधर्म समभाव और अद्वैत की पराकाष्ठा। बुल्ले शाह अपने प्रियतम को हर रूप में देखते हैं—वही क़ुरआन थामे हुए है और वही ब्राह्मण का जनेऊ (ज़ुन्नार) पहने है। सच्चा सूफी सभी धार्मिक भेदों से ऊपर उठकर केवल एक ईश्वर को देखता है।"
    },
    11: {
        "theme": "बीते दिन और व्यर्थ पछतावा (The Fleeting Opportunity)",
        "poetic_hi": [
            "बुल्ले! अच्छे दिन तो बीत गए, जब हरि से न की प्रीत,",
            "अब पछताए क्या बने, जब चिड़ियाँ चुग गईं खेत!"
        ],
        "poetic_en": [
            "Bulleh! The golden days are fled, when God you did not love;",
            "What boots repentance when the birds have stripped the fields above!"
        ],
        "commentary": "मानव जन्म का अमूल्य अवसर खो देने की चेतावनी। युवावस्था और सामर्थ्य के समय जब ईश्वर का स्मरण नहीं किया, तो बुढ़ापे या अंत समय में पश्चाताप करने से कोई लाभ नहीं होता।"
    },
    12: {
        "theme": "मलामत और लोक-निंदा का आनंद (The Glory of Infamy)",
        "poetic_hi": [
            "बुल्ले! जब रब का आशिक हुआ, तो लाखों हुई मलामत सार,",
            "लोग कहें जब काफ़िर-काफ़िर, तू 'हाँ-हाँ' कह स्वीकार!"
        ],
        "poetic_en": [
            "Bulleh! A lover of the Lord, countless reproaches fly;",
            "When people brand you 'Infidel!', say 'Yes! Yes!' in reply!"
        ],
        "commentary": "सूफी संप्रदाय की 'मलामतिया' परंपरा का निरूपण। जब दुनिया साधक को नास्तिक या काफ़िर कहे, तो उसे बुरा मानने के बजाय सहर्ष स्वीकार करना चाहिए, क्योंकि यह निंदा साधक के अहंकार को जड़ से मिटा देती है।"
    },
    13: {
        "theme": "साजन का आगमन और भेदों का नाश (The Arriving Beloved)",
        "poetic_hi": [
            "बुल्ले! आते साजन को देख, जाते को मत निहार,",
            "विरह-दर्द के मारे लोग, बन बैठे पंडित-शेख अपार!"
        ],
        "poetic_en": [
            "Bulleh! Behold the coming Friend, look not on parting grief;",
            "Pierced by the pangs of longing separation, men turn priest and sheikh for relief!"
        ],
        "commentary": "परमात्मा के सनातन आगमन (उपस्थिति) पर ध्यान केंद्रित करने का उपदेश। जो लोग विरह के रहस्य को नहीं समझते, वे औपचारिक धर्मगुरु (ब्राह्मण या शेख) बनकर अपनी आध्यात्मिक असफलता को छिपाते हैं।"
    },
    14: {
        "theme": "सुनार की दुकान और सोने की एकता (Gold in All Ornaments)",
        "poetic_hi": [
            "बुल्ले! चल सुनार के द्वारे, जहाँ लाखों गहने घड़े अपार,",
            "आकार भले ही भिन्न हों, पर सोना एक ही सार!"
        ],
        "poetic_en": [
            "To the goldsmith's forge, O Bulleh, go, where endless jewels shine;",
            "Diverse the shapes of ornament, one gold through all design!"
        ],
        "commentary": "वेदांत और तसव्वुफ़ का प्रसिद्ध रूपक। जैसे सोने के अनेक आभूषण होते हैं पर मूल धातु एक ही सोना है, वैसे ही संसार के समस्त जीव और रूप एक ही परमात्मा की भिन्न-भिन्न अभिव्यक्तियाँ हैं।"
    },
    15: {
        "theme": "हिन्दू-मुस्लिम का समन्वय (Transcending Duality)",
        "poetic_hi": [
            "बुल्ले! दासी बनूँ मुसलमान की, हिन्दू पर जाऊँ वार,",
            "दोनों पर से जल वार कर पीऊँ, जो रचे सिरजनहार!"
        ],
        "poetic_en": [
            "Bulleh! Handmaid to Muslim faith, yet Hindu's soul I prize;",
            "I wave the water round them both, where God's own grace doth rise!"
        ],
        "commentary": "धार्मिक संकीर्णता से परे जाकर मानवता और प्रेम का सम्मान। बुल्ले शाह कहते हैं कि सच्चा साधक दोनों संप्रदायों का आदर करता है और उनके ऊपर से न्योछावर होने को तैयार रहता है।"
    },
    16: {
        "theme": "धर्मशाला और मंदिर में पाखंड (Hypocrites in Sacred Places)",
        "poetic_hi": [
            "धर्मशाला में व्यापारी बसते, ठाकुरद्वारे में ठग का फेर,",
            "मस्जिदों में कपटी रहते, आशिक रहें अलग सब बेर!"
        ],
        "poetic_en": [
            "In inns and shrines the weighers trade, in temples swindlers hide;",
            "In mosques the hypocrites abide; true lovers dwell aside!"
        ],
        "commentary": "धार्मिक स्थानों में होने वाले पाखंड पर तीखा कटाक्ष। धर्मशालाओं में बनिए, मंदिरों में ठग और मस्जिदों में झूठे लोग जमे बैठे हैं; इसलिए सच्चे ईश्वर-प्रेमी इन सबसे अलग-थलग अपनी साधना में लीन रहते हैं।"
    },
    17: {
        "theme": "सच्चे प्रभु का द्वार (The True Threshold of Peace)",
        "poetic_hi": [
            "धर्मशाला में शांति नहीं, जहाँ पाखंडी भोग लगाएं,",
            "मस्जिद में भी धक्के मिलते, मुल्लां त्यौरी चढ़ाएं।",
            "दौलतमंदों ने दरवाजों पर, दरबान कड़े बिठाए,",
            "पकड़ द्वार उस सच्चे रब का, जहाँ दिल का दुख मिट जाए!"
        ],
        "poetic_en": [
            "No peace within the pilgrim inn where hypocrites feed greed,",
            "In mosques they shove and mullahs scowl, deaf to the seeker's need.",
            "The wealthy set their haughty guards before the palaced gate;",
            "Cling to the door of God alone, where griefs of soul abate!"
        ],
        "commentary": "संसार और संस्थागत धर्मों की विफलता। न धर्मशाला में तृप्ति है, न मस्जिद के धक्कों में, और न अमीरों के महलों में। केवल परमात्मा का आंतरिक द्वार ही आत्मा के कष्टों का सच्चा निवारण करता है।"
    },
    18: {
        "theme": "अहंकार को कुएं में फेंकना (Burning the Ego)",
        "poetic_hi": [
            "बुल्ले! गर्व-अहंकार को जला डाल, मान को कुएं में फेंक बहा,",
            "तन-मन की सब सुध भुला दे, घर बैठे प्रियतम मिलेगा आ!"
        ],
        "poetic_en": [
            "Burn down all pride, O Bulleh, cast all vanity in the deep well;",
            "Lose all awareness of self and flesh; at home shall the Beloved dwell!"
        ],
        "commentary": "जब तक साधक अपनी मान-प्रतिष्ठा और शारीरिक चेतना का विसर्जन नहीं करता, तब तक ईश्वर की प्राप्ति असंभव है। अहंकार मिटते ही प्रियतम स्वयं अंतःकरण में प्रकट हो जाता है।"
    },
    19: {
        "theme": "हरि-मंदिर में लेखा-जोखा (Accounting in the Divine Temple)",
        "poetic_hi": [
            "हरि-मंदिर में आकर के, अपना लेखा-जोखा बताओ भ्रात,",
            "पढ़े-लिखे पंडित दूर किए, अनपढ़ों को अपनाया साथ!"
        ],
        "poetic_en": [
            "Enter the temple of the Lord, give reckoning of thy deed;",
            "Learned scholars were turned away, simple fools received in need!"
        ],
        "commentary": "प्रभु के दरबार में शास्त्रीय पाण्डित्य काम नहीं आता; वहाँ निष्कपट हृदय और भोला प्रेम ही स्वीकार होता है। घमंडी पंडित बाहर रह जाते हैं, जबकि निष्कपट प्रेमी अपना लिए जाते हैं।"
    },
    20: {
        "theme": "सच्ची हिजरत और नित्य पुनर्जन्म (Spiritual Hijrah)",
        "poetic_hi": [
            "सच्चे इस्लाम की हिजरत में, मिलता नित विश्राम महान,",
            "नित्य मरूँ और नित्य ही जीऊँ, नित्य कूच और नित्य मुकाम!"
        ],
        "poetic_en": [
            "In true migration of the soul, my spirit finds its peace;",
            "Daily I die and daily wake; my wanderings never cease!"
        ],
        "commentary": "सूफी हिजरत भौतिक यात्रा नहीं, बल्कि अहंता से ईश्वरीय सत्ता की ओर अंतर्यात्रा है। यहाँ साधक प्रतिक्षण अपने क्षुद्र 'अहं' को मारता है (फना) और प्रभु-प्रेम में नया जीवन पाता है (बका)।"
    },
    21: {
        "theme": "साजन का प्रेमी और भाट (The Divine Bard)",
        "poetic_hi": [
            "साजन के प्रेम ने आकर, मुझको बना दिया गायक-भाट,",
            "वह दाता परम उदार है, मैं सेवा में कंजूस निपाट!"
        ],
        "poetic_en": [
            "The love of my Beloved came and made me bard to sing;",
            "He is the generous Lord supreme, I poor in offering!"
        ],
        "commentary": "ईश्वरीय प्रेम मनुष्य को संसार की प्रतिष्ठा छुड़ाकर प्रभु का विनम्र यशगान करने वाला बना देता है। परमात्मा की असीम कृपा के सामने साधक अपनी तुच्छता और न्यूनता को स्वीकार करता है।"
    },
    22: {
        "theme": "ऐन और ग़ैन का नुक़्ता (The Nuqta of Ain and Ghain)",
        "poetic_hi": [
            "बुल्ले! जैसी सूरत 'ऐन' की, वैसी ही सूरत 'ग़ैन' की जान,",
            "एक नुक्ते का केवल फेर है, भूला फिरे सारा जहान!"
        ],
        "poetic_en": [
            "As 'Ayn is shaped, so 'Ghayn appears, O Bulleh, clear and plain;",
            "A single dot divides the two, yet world seeks Truth in vain!"
        ],
        "commentary": "फारसी-अरबी लिपि में 'ऐन' (ع - हक़ीक़त/परम तत्व) और 'ग़ैन' (غ - ग़फ़लत/अविद्या का पर्दा) की बनावट एक जैसी है, केवल एक बिंदु (नुक़्ते) का अंतर है। वह नुक़्ता मनुष्य का 'अहंकार' है; अहंकार हटते ही जीव ही ब्रह्म बन जाता है।"
    },
    23: {
        "theme": "सच्चा गाज़ी और अंतःकरण का युद्ध (The Inner Jihad)",
        "poetic_hi": [
            "बुल्ले! यदि सच्चा गाज़ी बनना, तो कमर में बाँध तलवार,",
            "पहले अंदर के दुष्ट को मार, फिर बाहरी काफ़िर पर कर वार!"
        ],
        "poetic_en": [
            "If thou wouldst be a warrior true, bind sword upon thy waist;",
            "Slay first the unruly beast within, ere outer foes are faced!"
        ],
        "commentary": "जिहाद-ए-अकबर (महानतम धर्मयुद्ध) का आह्वान। असली शत्रु बाहर नहीं, बल्कि मनुष्य के भीतर बैठा काम, क्रोध और अहंकार (नफ़्स) है। जो अपने भीतर के अवगुणों को जीत लेता है, वही सच्चा योद्धा (गाज़ी) है।"
    },
    24: {
        "theme": "तीन घातक तलवारें (The Three Deadly Swords)",
        "poetic_hi": [
            "कनक, कौड़ी और कामिनी—तीनों ही तीक्ष्ण तलवार,",
            "आए थे हरि-नाम जपने को, बीच में ही दिए मार!"
        ],
        "poetic_en": [
            "Wealth, gold and lust of flesh—these three are deadly swords that kill;",
            "We came to chant the Holy Name, but fell upon the hill!"
        ],
        "commentary": "संसार की तीन सबसे बड़ी वासनाएँ—अन्न/सोना (कनक), धन-दौलत (कौड़ी) और काम-वासना (कामिनी)—साधक की आध्यात्मिक यात्रा को मार्ग में ही नष्ट कर देती हैं।"
    },
    25: {
        "theme": "कसूर बेदस्तूर (The Realm Beyond Rules)",
        "poetic_hi": [
            "बुल्ले! कसूर है बेदस्तूर, वहाँ जाना हुआ लाचार,",
            "न कोई पुण्य न दान वहाँ, न कोई रस्म-दस्तूर का भार!"
        ],
        "poetic_en": [
            "Bulleh! Kasur is lawless realm, there journey we must make;",
            "No charity nor ritual counts, no worldly custom's sake!"
        ],
        "commentary": "परम पद (लाहूत) की अवस्था जहाँ सांसारिक विधियाँ, रस्में और कर्मकांड समाप्त हो जाते हैं। परमात्मा के विशुद्ध प्रेम-लोक में केवल आत्मा का सत्य ही मान्य है।"
    },
    26: {
        "theme": "मलामत और मदिरालय (The Paradox of Mystic Love)",
        "poetic_hi": [
            "खा हराम और पढ़ शुकराना, तौबा कर सवाब के विचार से,",
            "छोड़ मस्जिद और पकड़ किनारा, छूटेगी जान अज़ाब के प्रहार से।",
            "वह अक्षर न पढ़ो जिससे, रह जाए जान जवाब के भार से,",
            "बुल्ले शाह! चल वहाँ चलें, जहाँ रोके न कोई शराब के खुमार से!"
        ],
        "poetic_en": [
            "Eat forbidden, give your thanks, renounce the thirst for heavenly prize,",
            "Quit the mosque and seek the edge, from inner torments to arise.",
            "Study not that pedant lore which leaves the soul in tangled lies;",
            "Haste, O Bulleh, to the tavern, where wine of love none denies!"
        ],
        "commentary": "सूफी मलामतिया संप्रदाय का अत्यंत प्रतीकात्मक दोहा। यहाँ 'हराम' सांसारिक मान-सम्मान को ठुकराना है, और 'शराब' ईश्वरीय प्रेम का मदिरापान है। औपचारिक स्वर्ग के लोभ को छोड़कर केवल ईश्वर-मिलन की प्यास रखने का संदेश है।"
    },
    27: {
        "theme": "मन की मूँज को कूटना (Thrashing the Fibers of Mind)",
        "poetic_hi": [
            "बुल्ले! यह मन मूँज का गट्ठर है, एकांत में बैठ इसे कूट,",
            "यह अर्श का खजाना है तुझमें, तू संभल-संभल इसे लूट!"
        ],
        "poetic_en": [
            "Bulleh! The mind is tough reed grass; in quiet corner beat it sore;",
            "Within thee lies the throne of God; plunder its boundless store!"
        ],
        "commentary": "जैसे मूँज की घास को कूट-कूटकर कोमल रस्सी बनाई जाती है, वैसे ही हठधर्मी मन को ध्यान और साधना की चोट से शुद्ध किया जाता है। जब मन वश में होता है, तो अंतरात्मा का दिव्य खज़ाना खुल जाता है।"
    },
    28: {
        "theme": "कुम्हार की मिट्टी (Clay in the Potter's Hands)",
        "poetic_hi": [
            "बुल्ले! मैं मिट्टी कुम्हार की, कह न सकूँ कोई बात,",
            "मुझ अभागिन को क्यों गढ़ा, कहीं टूट न जाऊँ प्रभात!"
        ],
        "poetic_en": [
            "Bulleh! I am the potter's clay, no word have I to plea;",
            "Why didst Thou shape this wretched form, if broken it must be?"
        ],
        "commentary": "परम समर्पण और विवशता का भाव। जीव परमात्मा के हाथ में कुम्हार की गीली मिट्टी के समान है। वह जैसे चाहे गढ़े और जैसे चाहे रखे, साधक पूर्णतः उसी की इच्छा पर निर्भर है।"
    },
    29: {
        "theme": "मुल्ला और मशालची (The Blind Guides)",
        "poetic_hi": [
            "मुल्ला और मशालची—दोनों का एक ही हाल,",
            "औरों को करते रोशनी, खुद अंधेरे में कंगाल!"
        ],
        "poetic_en": [
            "The preacher and the torch-bearer share but a single plight;",
            "They show the path to other men, while blind in their own night!"
        ],
        "commentary": "पाखंडी धर्मोपदेशकों पर व्यंग्य। जैसे मशालची दूसरों के रास्ते पर रोशनी डालता है पर स्वयं मशाल के नीचे अंधेरे में रहता है, वैसे ही पाखंडी उपदेशक दूसरों को ज्ञान सिखाते हैं पर स्वयं अज्ञान और वासना के अंधकार में डूबे रहते हैं।"
    },
    30: {
        "theme": "प्रेम का विषम मार्ग (The Tangled Road of Love)",
        "poetic_hi": [
            "प्रेम के लंबे पड़े हैं पंथ, क्या छूटे आवागमन का दौर?",
            "अंधे को अंधा मिल गया, राह दिखाए कौन ठौर?"
        ],
        "poetic_en": [
            "Long and arduous is the trail of love, how break rebirth's decree?",
            "When blind man leads another blind, what pathway can they see?"
        ],
        "commentary": "सच्चे मुर्शिद के बिना साधना व्यर्थ है। यदि गुरु स्वयं आत्मज्ञानी नहीं है, तो वह शिष्य को भी भटका देगा—'अंधे को अंधा मिला, राह बताए कौन।'"
    },
    31: {
        "theme": "काफ़िर और मूर्ति-पूजा (The Transcendent State)",
        "poetic_hi": [
            "परसों काफ़िर हो गया, कल मूर्ति-पूजा की रात,",
            "आज जा बैठे अपने घर में, जहाँ होती नहीं कोई बात!"
        ],
        "poetic_en": [
            "Two days ago an infidel, yesterday before idols bowed;",
            "Today I sit in my true home, beyond all speech and crowd!"
        ],
        "commentary": "साधक की चेतना का क्रमिक विकास। पहले सामाजिक धर्म से विमुख हुआ (काफ़िर), फिर साकार रूप की पूजा की (मूर्ति), और अंततः अपने अंतर-स्वरूप (निज-घर) में स्थिर होकर मौन समाधि पा ली।"
    },
    32: {
        "theme": "ठगों के ठग को ठगना (The Holy Outlaw)",
        "poetic_hi": [
            "पी शराब और खा कबाब, नीचे हड्डियों की जला आग,",
            "चोरी कर, तोड़ रब का घर, उस ठगों के ठग को ठगने भाग!"
        ],
        "poetic_en": [
            "Drink deep of wine, feast on roast meat, burn bones to kindle flame;",
            "Steal and break into the house of God, outwit the Trickster's game!"
        ],
        "commentary": "सूफी रहस्यवाद की प्रतीकात्मक भाषा। 'शराब' प्रेम-रस है, 'हड्डियों की आग' तपस्या और विरह है, और 'ठगों के ठग को ठगना' उस मायापति ईश्वर को अनन्य प्रेम के बल पर अपने वश में कर लेना है।"
    },
    33: {
        "theme": "काज़ी, मुल्ला और आशिक की चाह (What Pleases Whom)",
        "poetic_hi": [
            "काज़ी राज़ी रिश्वत से, मुल्ला राज़ी मौत पर आए,",
            "आशिक राज़ी प्रभु-राग से, कभी न उसका प्रेम घटाए!"
        ],
        "poetic_en": [
            "The judge is pleased with heavy bribes, the priest when death draws near;",
            "The lover thrives on melody, his faith forever clear!"
        ],
        "commentary": "संसार के स्वार्थ का पर्दाफ़ाश। काज़ी को रिश्वत में सुख मिलता है, मुल्ला को किसी के मरने पर फातिहा पढ़ने की दक्षिणा में; केवल सच्चा प्रेमी ही निस्वार्थ भाव से ईश्वर के प्रेम-राग में मग्न रहता है।"
    },
    34: {
        "theme": "संसार की कमाई (The Fruit of Worldliness)",
        "poetic_hi": [
            "रंग-महलों में चढ़ गया, लोग पूछें कुशल-क्षेम की बात,",
            "हमने दुनिया से यह पाया—मुख काला और नीले पैर के पात!"
        ],
        "poetic_en": [
            "I mounted to the painted halls, men asked for news of grace;",
            "Behold what from the world I won—blue bruised feet and blackened face!"
        ],
        "commentary": "सांसारिक प्रतिष्ठा और ऐश्वर्य का कड़वा सच। दुनिया के पीछे भागने वाले को अंत में केवल बदनामी (काला मुख) और भटकाव के घाव (नीले पैर) ही हाथ लगते हैं।"
    },
    35: {
        "theme": "मज़ाज़ी सीढ़ियाँ और हक़ीक़त (The Ladder of Form)",
        "poetic_hi": [
            "बुल्ले! सब सांसारिक रूप हैं सीढ़ियाँ, तू परम हक़ीक़त देख,",
            "जो कोई उस मुकाम पर पहुँचे, भूल जाए औपचारिक सलाम-अलेक!"
        ],
        "poetic_en": [
            "All earthly forms are ladder rungs; gaze on the Truth supreme;",
            "Whoever climbs that summit high forgets each formal theme!"
        ],
        "commentary": "इश्क-ए-मज़ाज़ी (लौकिक प्रेम) केवल सीढ़ी है जो इश्क-ए-हक़ीक़ी (ईश्वरीय प्रेम) तक ले जाती है। जब साधक परम सत्य में विलीन हो जाता है, तो समस्त औपचारिक शिष्टाचार स्वतः छूट जाते हैं।"
    },
    36: {
        "theme": "पाखंडी दानी (The Feigned Givers)",
        "poetic_hi": [
            "वारें जाएं उन लोगों पर, जो बातों से बहलाएं मन,",
            "सुई-सलाई का दान करें, और छुपा लें निहाई-धन!"
        ],
        "poetic_en": [
            "Woe to those cunning flatterers who charm with words so light;",
            "They donate needles to the poor, but hide the anvils bright!"
        ],
        "commentary": "दिखावे के दानियों पर व्यंग्य जो छोटी-मोटी चीज़ें (सुई) देकर महान दानी बनने का ढोंग करते हैं, पर भारी संपदा (निहाई) छिपाकर रख लेते हैं।"
    },
    37: {
        "theme": "झूठी शेखी मारने वाले (The Boasters)",
        "poetic_hi": [
            "बलिहारी उन पाखंडियों पर, जो मारें गप्प अपार,",
            "कौड़ी मिले तो बाँटें सबको, खजाना हड़पें जार-जार!"
        ],
        "poetic_en": [
            "Hail to the boasters who display a false and empty brag;",
            "They flaunt a penny found by chance, but seize the hidden bag!"
        ],
        "commentary": "संसार के झूठे ढोंगियों की निंदा जो तनिक से सद्गुण या दान का ढिंढोरा पीटते हैं, पर दूसरों का पूरा हक निगल जाते हैं।"
    },
    38: {
        "theme": "ऋतु का बदलना और नियति के पक्षी (Birds of Destiny)",
        "poetic_hi": [
            "फूलों की ऋतु फिर आई, चिड़ियाँ चुगने दाना आईं,",
            "किसी को शिकारी बाज़ ने खाया, कितनों के गले फंदा पाईं।",
            "किसी को घर लौटने की आस थी, कोई सीख कबाब चढ़ाईं,",
            "बुल्ले शाह! उन पर क्या बस था, किस्मत ने चाल चलाईं!"
        ],
        "poetic_en": [
            "The season of fresh blossoms turned, birds flocked to peck the grain;",
            "Some were devoured by hawks of prey, some choked in snares of pain.",
            "Some hoped to reach their nest once more, some burned upon the spit;",
            "O Bulleh Shah! What power was theirs? 'Twas destiny that hit!"
        ],
        "commentary": "संसार की नश्वरता और काल की विभीषिका। जैसे चिड़ियाँ दाना चुगने आती हैं और विविध प्रकार से काल का ग्रास बन जाती हैं, वैसे ही संसार के जीव अपनी-अपनी वासनाओं में उलझकर मृत्यु के मुख में चले जाते हैं।"
    },
    39: {
        "theme": "केवल अल्लाह की बात (Nothing Else Matters)",
        "poetic_hi": [
            "और सब तो व्यर्थ की बातें, केवल अल्लाह-अल्लाह की बात सार,",
            "कुछ शोर मचाया आलिमों ने, कुछ कागज़ों ने फैलाया अंधकार!"
        ],
        "poetic_en": [
            "All other words are idle chatter; God's holy Name alone is true;",
            "Scholars raised loud disputing noise, dry scrolls obscured the view!"
        ],
        "commentary": "किताबी ज्ञान बनाम ईश्वरीय नाम-स्मरण। आलिमों और मुल्लाओं ने शास्त्रार्थ और कागज़ के पन्नों में उलझाकर सत्य को ढक दिया है; मुक्ति केवल ईश्वर के पावन नाम में है।"
    },
    40: {
        "theme": "प्रेमियों को ही दीदार (Vision Given Only to Lovers)",
        "poetic_hi": [
            "उसी को अपना मुख दिखलाता, जिससे उसकी सच्ची प्रीत,",
            "उसी को वह प्रभु मिलता है, जो बन बैठे उसका मीत!"
        ],
        "poetic_en": [
            "He unveils His radiant face to those whose love is true and bright;",
            "To them alone the Lord appears who walk as companions of light!"
        ],
        "commentary": "परमात्मा का साक्षात्कार तर्कों या कर्मकांडों से नहीं होता; वह केवल उन्हीं भक्तों को अपना स्वरूप दिखाता है जो निष्कपट प्रेम के धागे में उससे बंधे होते हैं।"
    },
    41: {
        "theme": "मुख ज्योति है, घूँघट संसार (The Cosmic Veil)",
        "poetic_hi": [
            "उस प्रभु का मुख एक परम ज्योति है, घूँघट बना संसार,",
            "घूँघट में वह छिप गया, मुख पर आंचल डार!"
        ],
        "poetic_en": [
            "His holy face is living light, this world His veil so fine;",
            "Behind the veil He hides away, screened by His robe divine!"
        ],
        "commentary": "सूफी दर्शन का अत्यंत गूढ़ रहस्य। यह दृश्यमान जगत कोई स्वतंत्र सत्ता नहीं, बल्कि परमात्मा के प्रकाश पर पड़ा हुआ उसका घूँघट (माया/हिजाब) है। जो घूँघट हटाना जानता है, उसे हर ओर केवल वही ज्योति दिखाई देती है।"
    },
    42: {
        "theme": "तपता चूल्हा और फ़कीरों की तृप्ति (The Welcoming Hearth)",
        "poetic_hi": [
            "ईंट खड़के, दुक्कड़ बाजे, चूल्हा तपे तैयार,",
            "आएं फ़कीर और खाकर जाएं, बुल्ला हो निहाल अपार!"
        ],
        "poetic_en": [
            "Bricks rattle, earthen dishes clink, the hearth glows warm and bright;",
            "Dervishes come and feast content; Bulleh is drenched in light!"
        ],
        "commentary": "फ़कीरी और संत-सेवा का परमानंद। बुल्ले शाह कहते हैं कि जब मेरे दरवेश भाई आकर मेरे चूल्हे पर पकी रोटी तृप्त होकर खाते हैं, तो मुझे ब्रह्मांड का परम सुख मिल जाता है।"
    },
    43: {
        "theme": "विस्मृत उद्देश्य (The Forgotten Purpose)",
        "poetic_hi": [
            "कनक, कौड़ी और कामिनी—तीनों ही तीक्ष्ण तलवार,",
            "आया था जिस काम के हित, भूल गई वह बात सार!"
        ],
        "poetic_en": [
            "Gold, wealth, and lust—these three are blades of sorrow and deceit;",
            "The sacred goal for which you came lies trampled at your feet!"
        ],
        "commentary": "मानव जीवन के मूल उद्देश्य को भूल जाने की वेदना। मनुष्य इस संसार में ईश्वर-साक्षात्कार के लिए आया था, परंतु मायावी आकर्षणों में फँसकर अपना मूल लक्ष्य भूल बैठा।"
    },
    44: {
        "theme": "छिपने और दिखने का खेल (The Divine Hide and Seek)",
        "poetic_hi": [
            "मुख दिखलावे और छिप जाए, छल-बल है इस जग के देश,",
            "पास रहे और मिले नहीं, धरता बीसों भेष!"
        ],
        "poetic_en": [
            "He shows His face and hides again in this deceptive sphere;",
            "He stays so close yet stays unseen, in twenty garbs severe!"
        ],
        "commentary": "परमात्मा की रहस्यमयी लीला। वह हर प्राणी के निकटतम है, पर अपनी अनंत मायावी छवियों में छिपकर साधक के प्रेम की परीक्षा लेता है।"
    },
    45: {
        "theme": "मस्जिद-काबा से परे (Beyond Mosque and Kaaba)",
        "poetic_hi": [
            "न खुदा मस्जिद में मिलता, न काबा के धाम,",
            "न खुदा कुरान-किताबों में, न केवल नमाज़ के नाम!"
        ],
        "poetic_en": [
            "God dwells not in the vaulted mosque, nor Kaaba's stones around;",
            "Nor in the pages of the scrolls, nor formal prostrations found!"
        ],
        "commentary": "ईश्वर का वास किसी भौगोलिक स्थान, इमारत या पोथियों में सीमित नहीं है। वह असीम चेतना है जिसे केवल अंतःकरण के शुद्ध प्रेम द्वारा अनुभव किया जा सकता है।"
    },
    46: {
        "theme": "तीर्थों की व्यर्थता एवं सद्गुरु की महिमा (The Master's Grace)",
        "poetic_hi": [
            "न खुदा मैंने तीर्थों में देखा, व्यर्थ ही पंथ तै किए सारे,",
            "बुल्ले शाह! जब मुर्शिद मिला, टूटे सब बंधन और तगादे हमारे!"
        ],
        "poetic_en": [
            "I found no God at pilgrim shrines, in vain I roamed the land;",
            "When Bulleh met his Perfect Guide, all worldly bonds were banned!"
        ],
        "commentary": "बाहरी तीर्थयात्राओं की सीमा और सद्गुरु (इनायत शाह) की असीम महिमा। जब पूर्ण गुरु का सान्निध्य मिला, तो मन के सारे द्वंद्व, भय और वासनाओं के तकाज़े स्वतः समाप्त हो गए।"
    },
    47: {
        "theme": "पत्थर बनाम अहंकारी (Humbler than a Stepping Stone)",
        "poetic_hi": [
            "अहंकारी से तो रोड़ा भला, जिस पर पैर घिसें सब लोग,",
            "बुल्ले के प्रभु को वही पाए, जो बने कसाई का बकरा अनूठा भोग!"
        ],
        "poetic_en": [
            "Better than proud tyrants is the rough stone where travelers scrape their feet;",
            "Bulleh's Lord is attained by him who surrenders as the butcher's meat!"
        ],
        "commentary": "आत्म-समर्पण की पराकाष्ठा। घमंडी व्यक्ति से वह पत्थर अच्छा है जो राहगीरों के काम आता है। ईश्वर की प्राप्ति उसी को होती है जो कसाई के हाथ में बकरे की तरह अपने अहंकार की बलि चढ़ा देता है।"
    },
    48: {
        "theme": "हरि का द्वार (The True Threshold of Love)",
        "poetic_hi": [
            "ठाकुरद्वारे में ठग बसते, मस्जिद में धूर्तों का वेश,",
            "हरि के द्वारे केवल भिक्षुक (प्रेमी) बसते, यही हमारी प्रीत का देश!"
        ],
        "poetic_en": [
            "In stone-built shrines the swindlers thrive, in mosques the cunning preach;",
            "At Hari's court the humble beg; such is the faith we reach!"
        ],
        "commentary": "संस्थागत धार्मिक स्थलों के मुकाबले सच्चे प्रेमियों की विनम्र शरणस्थली। प्रभु के सच्चे दरबार में केवल वे फ़कीर और भक्त बसते हैं जो अपने अहंकार की भिक्षा मांगकर प्रभु में लीन हो चुके हैं।"
    },
    49: {
        "theme": "अंतर का सद्गुरु (The Voice of the Inner Master)",
        "poetic_hi": [
            "वह मार्गदर्शक मेरे अंदर बोला, सब पाप बहकर मिट गए,",
            "पहाड़ों पर बाजरा लहलहाया, बंजर पर शहतूत खिल गए!"
        ],
        "poetic_en": [
            "The inner Guide spoke in my heart, my sins dissolved away;",
            "Millets bloomed on rocky cliffs, barren trees bore fruits today!"
        ],
        "commentary": "आंतरिक ज्ञानोदय का चमत्कार। जब अंतरात्मा में सद्गुरु की आवाज़ गूँजती है, तो जन्म-जन्मांतरों के पाप नष्ट हो जाते हैं और हृदय की बंजर भूमि पर भी प्रेम और आनंद के फल लद जाते हैं।"
    },
    50: {
        "theme": "अद्वैत का सागर (Ocean of Wahdat)",
        "poetic_hi": [
            "अद्वैत की नदियाँ उमड़ रही हैं, मेरी वहदत किस ओर सिधारी?",
            "पूर्ण मुर्शिद ने पार उतारा, बिना नाव और मशक के भारी!"
        ],
        "poetic_en": [
            "Rivers of Oneness surge ahead; whither my soul hath fled?",
            "The Perfect Master ferried me across, with no raft or skin instead!"
        ],
        "commentary": "वहदत (अद्वैत) का अगाध सागर। जब साधक अद्वैत में प्रवेश करता है, तो 'मैं' और 'तू' का भेद मिट जाता है। पूर्ण मुर्शिद साधक को बिना किसी बाह्य साधन (नाव, मशक) के भवसागर पार करा देता है।"
    },
    51: {
        "theme": "अपने आप को पढ़ना (Read Thyself)",
        "poetic_hi": [
            "पढ़-पढ़ कर आलिम-फ़ाज़िल हुआ, कभी अपने आप को पढ़ा ही नहीं,",
            "जा-जाकर मंदिर-मस्जिद में बैठा, कभी मन के भीतर चढ़ा ही नहीं।",
            "रोज़ ही व्यर्थ शैतान से लड़ता, कभी अपने नफ़्स से लड़ा ही नहीं,",
            "बुल्ले शाह! आकाश में उड़ते पंछी पकड़े, जो घर बैठा उसे पकड़ा ही नहीं!"
        ],
        "poetic_en": [
            "You read the books till scholar crowned, yet never read your soul within;",
            "You rushed to mosque and temple shrine, yet never stepped where Truth had been.",
            "You fight with Satan day by day, yet never fought your selfish sin;",
            "Bulleh! You grasp at birds aloft, yet miss the Lord who dwells within!"
        ],
        "commentary": "बुल्ले शाह का सर्वाधिक प्रसिद्ध और अमर दोहा। किताबी ज्ञान, बाह्य इबादत और काल्पनिक शैतान से लड़ने का कोई लाभ नहीं, जब तक मनुष्य अपने ही मन का अध्ययन न करे और अपने भीतर बैठे अहम् (नफ़्स) को परास्त न करे।"
    },
    52: {
        "theme": "रब तेरे अंदर बसता है (God Dwells Within You)",
        "poetic_hi": [
            "रब-रब कहते बूढ़े हो गए, मुल्लां-पंडित हारे,",
            "रब की खोज न पा सके, सजदे कर-कर के थारे।",
            "रब तो तेरे अंदर बसता, यह कुरआन के इशारे,",
            "बुल्ले शाह! रब उसको मिलता, जो यार पर सर्वस्व वारे!"
        ],
        "poetic_en": [
            "Crying 'O God! O God!' they aged, both priest and mullah in despair;",
            "No trace of Him could they behold, worn out in endless lines of prayer.",
            "God lives within your very breath, as holy verses clear declare;",
            "Bulleh! The Lord belongs to him who crowns his Beloved with love and care!"
        ],
        "commentary": "ईश्वर का निवास स्थान। मुल्ला और पंडित जीवन भर बाहर भटकते रहे और सिजदे करते-करते थक गए, पर ईश्वर को न पा सके। पवित्र ग्रंथ स्वयं संकेत करते हैं कि परमात्मा मनुष्य की शह-रग से भी निकट है; वह केवल उसी को मिलता है जो अपने प्रियतम पर अपना सर्वस्व न्योछावर कर देता है।"
    },
    53: {
        "theme": "इश्क की बाज़ी और घुंघरू (Dancing for the Beloved)",
        "poetic_hi": [
            "वार दे सब कुछ अपने यार पर, जो जीतनी इश्क की बाज़ी,",
            "यार के नाम की नीयत बांध ले, तब कहें तुझे इश्क-नमाज़ी।",
            "तेरा यार कहे तो घुंघरू बाँध ले, चाहे फ़तवे लगाए काज़ी,",
            "बुल्ले शाह! जग रूठता है तो रूठ जाए, हमें यार को रखना राज़ी!"
        ],
        "poetic_en": [
            "Surrender all to thy Beloved, if thou wouldst win Love's game of grace;",
            "Direct thy prayer in His sweet Name, then stand in true devotion's place.",
            "If He commands, tie ankle bells, though judges curse thy shameless race;",
            "Bulleh! Let the whole world take offense, our only joy is His embrace!"
        ],
        "commentary": "सच्चे प्रेम का सर्वोच्च समर्पण। जब बुल्ले शाह के मुर्शिद इनायत शाह उनसे रूठ गए थे, तो बुल्ले ने घुंघरू बांधकर नृत्य किया था। समाज चाहे कितने भी फतवे लगाए, प्रेमी की एकमात्र साधना अपने प्रियतम को प्रसन्न रखना है।"
    },
    54: {
        "theme": "इश्क के न्यायालय में सब लुट गया (Plundered in Love's Court)",
        "poetic_hi": [
            "इश्क के न्यायालय में जब मैं गया, तो उसने मेरी अकड़ लूट ली,",
            "मैं तो गया था सौदा करने, पर इश्क ने मेरी रस्सी ही लूट ली।",
            "इश्क लूटता है वलियों और नबियों को, कई बादशाहों की बादशाही लूट ली,",
            "अरे बुल्ले! तेरा क्या लूटा है? इस इश्क ने तो खुदा की खुदाई ही लूट ली!"
        ],
        "poetic_en": [
            "I entered Love's imperial court, and Love stripped off my stubborn pride;",
            "I went as merchant to buy and sell, but Love seized all I had inside.",
            "Love plundered saints and prophets high, cast crowns of emperors aside;",
            "What has Love stolen from thee, Bulleh? It plundered God of His empire wide!"
        ],
        "commentary": "इश्क की सर्वग्रासी शक्ति। लौकिक और आध्यात्मिक जगत की कोई भी सत्ता प्रेम के सामने टिक नहीं सकती। प्रेम में पड़कर अहंकारी की अकड़, बादशाहों के ताज और वलियों की साधना सब विलीन हो जाती है; स्वयं परमात्मा भी प्रेम के अधीन हो जाता है।"
    },
    55: {
        "theme": "पाँचों वक़्त की नमाज़ बनाम यार की रज़ा (The Ultimate Metric)",
        "poetic_hi": [
            "पाँचों वक़्त नमाज़ें पढ़ीं, तो लोग कहें नमाज़ी,",
            "जंग जीतकर घर लौटा, तो लोग कहें गाज़ी।",
            "न्याय की कुर्सी पर बैठा, तो लोग कहें काज़ी,",
            "बुल्ले शाह! कुछ नहीं पाया, जो यार न किया राज़ी!"
        ],
        "poetic_en": [
            "Prayed five times daily, men salute and call thee 'True Devout' with praise;",
            "Returned victorious from the war, as 'Holy Victor' crowns ablaze.",
            "Sat on the bench of righteousness, hailed as a 'Judge' of ancient ways;",
            "O Bulleh Shah! You gained nothing at all, if your Beloved unpleased stays!"
        ],
        "commentary": "आध्यात्मिक जीवन की सर्वोच्च कसौटी। चाहे कोई बड़ा नमाज़ी हो, युद्ध जीतने वाला गाज़ी हो, या न्याय करने वाला काज़ी—यदि उसने अपने प्रियतम (परमात्मा/सद्गुरु) का प्रेम और प्रसन्नता प्राप्त नहीं की, तो उसकी सारी सांसारिक व धार्मिक उपलब्धियाँ शून्य हैं।"
    },
    56: {
        "theme": "मैं भी तू और तू भी तू (Tat Tvam Asi - Absolute Non-Duality)",
        "poetic_hi": [
            "जो मैं तुझको बाहर ढूँढूँ, तो मेरे भीतर कौन समाना?",
            "जो मैं तुझको अंदर ढूँढूँ, तो सीमा में बंधा जाना।",
            "सब कुछ तू है, सब में तू है, सबसे पवित्र तुझको पहचाना,",
            "मैं भी तू है और तू भी तू है, यहाँ बुल्ला कौन निमाना!"
        ],
        "poetic_en": [
            "If I seek Thee outside myself, who is it that abides within?",
            "If I seek Thee within my breast, I bind Thee to a finite skin.",
            "Thou art all things, in all Thou dwell'st, beyond all taint of worldly sin;",
            "I too am Thou, and Thou art Thou—where is poor Bulleh to begin?"
        ],
        "commentary": "बाबा बुल्ले शाह का परम चरम दोहा—उपनिषदों के 'तत् त्वम् असि' और सूफी 'अनलहक' का साकार रूप। यदि ईश्वर बाहर है तो भीतर कौन बोल रहा है? और यदि केवल भीतर है तो उसे सीमित कर दिया। वास्तव में सब कुछ वही है—समस्त सृष्टि उसी का विस्तार है। जब 'मैं' और 'तू' का द्वैत मिट गया, तो बुल्ले का कोई पृथक अस्तित्व ही नहीं बचा; केवल वही एकमेव ब्रह्म शेष है।"
    }
}

dohre_processed = []

for item in raw_dohre:
    d_id = item["id"]
    lines = item["lines"]
    
    # Clean Dohra 56 of trailing footer code
    if d_id == 56:
        clean_lines = []
        for l in lines:
            if "footer {" in l or "#___gcse" in l or "function()" in l or "/*" in l or "line-height" in l:
                break
            clean_lines.append(l)
        lines = clean_lines
        
    cur = dohre_data.get(d_id, {
        "theme": f"आध्यात्मिक दोहा {d_id}",
        "poetic_hi": [f"{l}" for l in lines],
        "poetic_en": [f"Reflecting the spiritual truth of couplet {d_id}"],
        "commentary": "यह दोहा बाबा बुल्ले शाह के फकीरी अनुभव और अद्वैत दर्शन को व्यक्त करता है।"
    })
    
    annotated_lines = []
    for l in lines:
        hi_g, en_g = generate_line_gloss(l)
        annotated_lines.append({
            "original": l,
            "hindi_gloss": hi_g,
            "english_gloss": en_g
        })
        
    dohre_processed.append({
        "id": d_id,
        "title": f"दोहरा {d_id}",
        "theme": cur["theme"],
        "lines_annotated": annotated_lines,
        "poetic_hindi": cur["poetic_hi"],
        "poetic_english": cur["poetic_en"],
        "sufi_commentary": cur["commentary"]
    })

# Save JSON
json_path = os.path.join(OUTPUT_DATA_DIR, "dohre.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(dohre_processed, f, ensure_ascii=False, indent=2)
print(f"Saved {len(dohre_processed)} fully translated Dohre to {json_path}")

# Build Bulleh_Shah_Dohre_Trilingual.md
md = [
    "# बाबा बुल्ले शाह : सम्पूर्ण दोहरे (त्रिभाषी संस्करण)",
    "## Baba Bulleh Shah : Complete Dohre (Trilingual Master Edition)\n",
    "> **Original Classical Punjabi in Devanagari • Complete Word-by-Word Hindi Gloss • Complete Word-by-Word English Gloss • Metered Poetic Translations • In-Depth Sufi Commentary**\n",
    "---\n",
    "## विषय-सूची (Table of Contents)\n"
]

for d in dohre_processed:
    first_snip = d["lines_annotated"][0]["original"][:35] if d["lines_annotated"] else ""
    md.append(f"- [{d['title']}: {first_snip}](#{d['title'].replace(' ', '-')}) — *{d['theme']}*")

md.append("\n---\n")

for d in dohre_processed:
    md.append(f"## {d['title']}\n")
    md.append(f"### *{d['theme']}*\n")
    md.append("### मूल पाठ (Original Verses)\n")
    for a in d["lines_annotated"]:
        md.append(f"{a['original']}  ")
    md.append("\n---\n")
    md.append("### पद-वार अर्थ एवं शब्दार्थ (Word-by-Word Gloss)\n")
    for a in d["lines_annotated"]:
        md.append(f"**{a['original']}**  ")
        md.append(f"**हिन्दी शब्दार्थ:** {a['hindi_gloss']}  ")
        md.append(f"**English Gloss:** {a['english_gloss']}\n")
    md.append("### काव्यात्मक अनुवाद (Poetic Translations)\n")
    md.append("#### हिन्दी काव्यात्मक भावार्थ (Hindi Poetic Meaning)\n")
    for phi in d["poetic_hindi"]:
        md.append(f"{phi}  ")
    md.append("\n#### English Poetic Translation\n")
    for pen in d["poetic_english"]:
        md.append(f"*{pen}*  ")
    md.append("\n### दार्शनिक एवं सूफी व्याख्या (Sufi & Philosophical Commentary)\n")
    md.append(f"{d['sufi_commentary']}\n")
    md.append("\n---\n")

with open(OUTPUT_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(md))

print(f"Generated complete trilingual Markdown: {OUTPUT_MD} ({os.path.getsize(OUTPUT_MD)} bytes)")
