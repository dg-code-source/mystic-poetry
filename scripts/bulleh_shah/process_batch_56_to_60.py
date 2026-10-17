# -*- coding: utf-8 -*-
"""
Process Kafian 56 to 60 for Bulleh Shah Trilingual Edition.
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
        "id": 56,
        "title": "जिस तन लगिआ इश्क कमाल",
        "title_english": "The Body Where Consummate Love Strikes",
        "historical_context": "इस काफी में बुल्ले शाह आध्यात्मिक उन्माद (हाल / वज्द) का निरूपण करते हैं। जब किसी साधक के शरीर व चेतना में परिपूर्ण प्रेम (इश्क कमाल) उतरता है, तो वह शास्त्रीय सुरों और तालों के बंधनों से मुक्त होकर नृत्य करने लगता है। सांसारिक प्रश्नों और धर्मशास्त्रीय फतवों से परे होकर वह प्रियतम के पावन जमाल (सौंदर्य) का साक्षात कर लेता है।",
        "meter": "पंजाबी काफी (चतुष्पदी, अंत्यानुप्रास कमाल/बेताल/सहेड़े/हुगेड़े)",
        "raga": "राग काफी / बिलावल",
        "theme": "इश्क का उन्माद (वज्द), आध्यात्मिक नृत्य, बाह्य विधियों से परे आंतरिक शांति",
        "stanzas": [
            {
                "original": [
                    "जिस तन लगिआ इश्क कमाल ।  ",
                    "नाचे बेसुर ते बेताल ।"
                ],
                "hindi_gloss": [
                    "जिस (जिस) तन (शरीर में) लगिआ (लगा/उतरा) इश्क (इश्क/प्रेम) कमाल (कमाल/परिपूर्ण),",
                    "नाचे (वह नाचता है) बेसुर (सुर-हीन/नियम-मुक्त) ते (और) बेताल (बिना ताल के/उन्मत्त होकर) ।"
                ],
                "english_gloss": [
                    "जिस (which) तन (body) लगिआ (struck) इश्क (love) कमाल (consummate/perfect),",
                    "नाचे (dances) बेसुर (beyond measured notes) ते (and) बेताल (beyond strict cadence/unmeasured rhythm) ।"
                ],
                "poetic_hindi": [
                    "जिस तन में इश्क-कमाल जगा, वह नाचे बे-सुर और बे-ताल,",
                    "लोक-लाज सब धूल हुई, बिसरा जग का व्यवहार-जंजाल !"
                ],
                "poetic_english": [
                    "The frame where Love triumphant makes its seat, dances unchained by rhythm, rhyme, or tone;",
                    "Lost to all measured forms and cold conceit, ecstatically moving for the Friend alone!"
                ]
            },
            {
                "original": [
                    "दरदमन्दां नूं कोई ना छेड़े, आपे आपना दुक्ख सहेड़े,  ",
                    "जंमना ज्यूना मूल हुगेड़े, आपना बूझे आप ख़्याल ।  ",
                    "जिस तन लगिआ इश्क कमाल ।"
                ],
                "hindi_gloss": [
                    "दरदमन्दां (दर्द-मंदों/प्रेम-पीडि़तों) नूं (को) कोई (कोई) ना (मत) छेड़े (छेड़े/कष्ट दे), आपे (स्वयं ही) आपना (अपना) दुक्ख (दुख/दर्द) सहेड़े (सहेजा/चुन लिया है),",
                    "जंमना (जन्म लेना) ज्यूना (जीना) मूल (जड़ से) हुगेड़े (उखाड़ फेंकता है), आपना (अपने) बूझे (बूझता/समझता है) आप (स्वयं) ख़्याल (भाव/ध्यान) ,",
                    "जिस (जिस) तन (तन में) लगिआ (लगा) इश्क (इश्क) कमाल (कमाल) ।"
                ],
                "english_gloss": [
                    "दरदमन्दां (the grief-stricken lovers) नूं (unto) कोई (anyone) ना (do not) छेड़े (disturb/provoke), आपे (themselves) आपना (their own) दुक्ख (pain) सहेड़े (have embraced/gathered),",
                    "जंमना (birth) ज्यूना (living) मूल (from the root) हुगेड़े (uproots), आपना (one’s own) बूझे (understands) आप (self) ख़्याल (inner thought/state) ,",
                    "जिस (which) तन (body) लगिआ (struck) इश्क (love) कमाल (consummate) ।"
                ],
                "poetic_hindi": [
                    "मत छेड़ो इन दर्द-मन्दों को, इन्होंने खुद यह विरह चुना,",
                    "जन्म-मरण की जड़ें उखाड़ीं, अपना भाव स्वयं है गुना ।",
                    "जिस तन लगिआ इश्क कमाल !"
                ],
                "poetic_english": [
                    "Provoke not those whose souls in sorrow pine, who willingly embraced this sacred grief;",
                    "Uprooting birth and death by power divine, in silent self-contemplation finding relief.",
                    "The frame where Love triumphant makes its seat!"
                ]
            },
            {
                "original": [
                    "जिस ने वेस इश्क दा कीता, धुर दरबारों फ़तवा लीता,  ",
                    "जदों हज़ूरों प्याला पीता, कुझ्झ ना रेहा जवाब सवाल ।  ",
                    "जिस तन लगिआ इश्क कमाल ।"
                ],
                "hindi_gloss": [
                    "जिस (जिसने) ने (ने) वेस (वेश/स्वरूप) इश्क (इश्क) दा (का) कीता (धारण किया), धुर (परम आदि) दरबारों (ईश्वरीय दरबार से) फ़तवा (फतवा/आदेश) लीता (प्राप्त किया),",
                    "जदों (जब) हज़ूरों (प्रभु के साक्षात हज़ूर से) प्याला (प्रेम-मदिरा का प्याला) पीता (पी लिया), कुझ्झ (कुछ भी) ना (नहीं) रेहा (रहा) जवाब (उत्तर) सवाल (प्रश्न/तर्क-वितर्क) ,",
                    "जिस (जिस) तन (तन में) लगिआ (लगा) इश्क (इश्क) कमाल (कमाल) ।"
                ],
                "english_gloss": [
                    "जिस (whoever) ने (has) वेस (garb) इश्क (of love) दा (of) कीता (donned), धुर (primal) दरबारों (from the Court of Eternity) फ़तवा (decree/sanction) लीता (received),",
                    "जदों (when) हज़ूरों (from the Divine Presence) प्याला (cup of ecstasy) पीता (drank), कुझ्झ (anything) ना (not) रेहा (remained) जवाब (answer) सवाल (question) ,",
                    "जिस (which) तन (body) लगिआ (struck) इश्क (love) कमाल (consummate) ।"
                ],
                "poetic_hindi": [
                    "जिसने इश्क का बाना पहना, आदि-दरबार से फतवा पाया,",
                    "हज़ूर से जब प्याला पीया, प्रश्न-उत्तर का भेद मिटाया ।",
                    "जिस तन लगिआ इश्क कमाल !"
                ],
                "poetic_english": [
                    "Whoever wore the mantle Love decreed, bore sanction from the Primal Court sublime;",
                    "Drinking that chalice of celestial mead, erased all questions of debate and time.",
                    "The frame where Love triumphant makes its seat!"
                ]
            },
            {
                "original": [
                    "जिस दे अन्दर वस्या यार, उठ्या यारो यार पुकार,  ",
                    "ना उह चाहे राग ना तार, ऐवें बैठा खेडे हाल ।  ",
                    "जिस तन लगिआ इश्क कमाल ।"
                ],
                "hindi_gloss": [
                    "जिस (जिसके) दे (के) अन्दर (भीतर) वस्या (बस गया) यार (प्रियतम), उठ्या (उठी) यारो (यार ही) यार (यार की) पुकार (पुकार/गुंजार),",
                    "ना (न) उह (वह) चाहे (चाहता है) राग (राग-विद्या) ना (न) तार (वाद्ययंत्र के तार), ऐवें (बस यूं ही) बैठा (बैठकर) खेडे (अनुभव करता/खेलता है) हाल (आध्यात्मिक वज्द/हाल) ,",
                    "जिस (जिस) तन (तन में) लगिआ (लगा) इश्क (इश्क) कमाल (कमाल) ।"
                ],
                "english_gloss": [
                    "जिस (in whom) दे (of) अन्दर (within) वस्या (abides) यार (the Friend), उठ्या (arose) यारो (Beloved alone) यार (Beloved) पुकार (cry/chant),",
                    "ना (neither) उह (he) चाहे (craves) राग (raga/tune) ना (nor) तार (musical strings), ऐवें (spontaneously) बैठा (seated) खेडे (manifests/plays) हाल (mystic trance/ecstasy) ,",
                    "जिस (which) तन (body) लगिआ (struck) इश्क (love) कमाल (consummate) ।"
                ],
                "poetic_hindi": [
                    "जिसके अंतर यार समाया, 'यार-यार' की गूँजी तान,",
                    "राग न चाहे, तंत्री त्यागे, बैठे-बैठे खेले हाल-महान ।",
                    "जिस तन लगिआ इश्क कमाल !"
                ],
                "poetic_english": [
                    "Within whose core the Friend has taken place, arises one continuous lover's cry;",
                    "Craving no strings nor melodies of grace, seated in trance his spirit mounts the sky.",
                    "The frame where Love triumphant makes its seat!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शौह नगर सच्च पाइआ, झूठा रौला सभ मुकाइआ,  ",
                    "सच्च्यां कारन सच्च सुणाइआ, पाइआ उस दा पाक जमाल ।  ",
                    "जिस तन लगिआ इश्क कमाल ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ला कहता है) शौह (शाह/परमात्मा के) नगर (सच्चे नगर/सत्य-लोक को) सच्च (सत्य में) पाइआ (पा लिया), झूठा (झूठा) रौला (संसार का कोलाहल) सभ (समस्त) मुकाइआ (समाप्त कर दिया),",
                    "सच्च्यां (सच्चे साधकों के) कारन (लिए) सच्च (परम सत्य) सुणाइआ (सुना दिया), पाइआ (प्राप्त कर लिया) उस (उस परमात्मा का) दा (का) पाक (परम पावन) जमाल (सौंदर्य/आलोक) ,",
                    "जिस (जिस) तन (तन में) लगिआ (लगा) इश्क (इश्क) कमाल (कमाल) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh says) शौह (Lord’s) नगर (realm) सच्च (of Truth) पाइआ (attained), झूठा (false) रौला (din/clamor) सभ (all) मुकाइआ (quelled/ended),",
                    "सच्च्यां (the seekers of Truth) कारन (for the sake of) सच्च (the Truth) सुणाइआ (proclaimed), पाइआ (beheld) उस (His) दा (of) पाक (pure/holy) जमाल (beauty/radiance) ,",
                    "जिस (which) तन (body) लगिआ (struck) इश्क (love) कमाल (consummate) ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा शौह ने सत्य-नगर पाया, झूठा जग-कोलाहल मिटाया,",
                    "सत्य-प्रेमियों को सच बतलाया, पावन दिव्य-जमाल लखाया ।",
                    "जिस तन लगिआ इश्क कमाल !"
                ],
                "poetic_english": [
                    "Bulleh hath reached the Sovereign Realm of Grace, all false disputes and noisy doubts are gone;",
                    "Speaking plain truth unto the faithful race, gazing upon His pure celestial Dawn.",
                    "The frame where Love triumphant makes its seat!"
                ]
            }
        ],
        "philosophical_meaning": "सूफी परंपरा में 'हाल' (धार्मिक परमानंद/वज्द) उस स्थिति को कहते हैं जब साधक के ऊपर ईश्वरीय प्रकाश इस कदर छा जाता है कि उसकी शारीरिक और बौद्धिक सीमाएं टूट जाती हैं। वह 'बेसुर ते बेताल' नाचता है क्योंकि ईश्वरीय प्रेम का ताल संसार के किसी भी संगीत के नियमों में नहीं समा सकता। 'धुर दरबारों फतवा लीता' यह सिद्ध करता है कि प्रेम का विधान शरीअत के मौलवियों से नहीं बल्कि सीधे आदि-अनादि ईश्वरीय दरबार से स्वीकृत होता है।"
    },
    {
        "id": 57,
        "title": "जो रंग रंगिआ गूढ़ा रंगिआ, मुरशद वाली लाली ओ यार",
        "title_english": "The Deep Dye Wherewith I am Dyed, The Master's Crimson Glow, O Friend!",
        "historical_context": "यह काफी सूफी हकीकत और तसव्वुफ के गूढ़ रहस्यों से परिपूर्ण है। इसमें बुल्ले शाह प्रसिद्ध सूफी सूत्र 'अना अहमद बिला मीम' (मैं अहमद हूँ बिना मीम के—अर्थात् आहद/अद्वैत) और हदीस 'मूतू कबला अन तमूतू' (मरने से पहले मर जाओ) का संदर्भ देते हैं। वे अपने मुर्शिद हज़रत शाह इनायत कादरी के प्रेम-रंग की लाली का गुणगान करते हैं।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: मुरशद वाली लाली ओ यार)",
        "raga": "राग लालित / भैरव",
        "theme": "अद्वैत (वह्दत-उल-वजूद), हकीकत-ए-मोहम्मदिया, यद-ए-बैज़ा, मरने से पूर्व मरने का रहस्य",
        "stanzas": [
            {
                "original": [
                    "आहद विचों अहमद होया, विचों मीम निकाली ओ यार ।  ",
                    "दरमुआनी दी धूम मची है, नैणां तों घुंड उठाली ओ यार ।  ",
                    "जो रंग रंगिआ गूढ़ा रंगिआ, मुरशद वाली लाली ओ यार ।"
                ],
                "hindi_gloss": [
                    "आहद (आहद—परम निराकार एक ईश्वर) विचों (में से) अहमद (अहमद/पैगंबर मोहम्मद का स्वरूप) होया (प्रकट हुआ), विचों (बीच में से) मीम (अक्षर 'मीम'—मानवीय आवरण/स्थूल देह) निकाली (निकाल दिया) ओ (हे) यार (मित्र/प्यारे) ।",
                    "दरमुआनी (मध्यस्थता/प्रेम-व्यापार) दी (की) धूम (धूम/चर्चा) मची (मची) है (है), नैणां (नेत्रों) तों (से) घुंड (घूंघट/अज्ञान का पर्दा) उठाली (उठा दिया) ओ (हे) यार (मित्र) ।",
                    "जो (जो) रंग (रंग) रंगिआ (रंगा गया है) गूढ़ा (अति गहरा) रंगिआ (रंगा है), मुरशद (सद्गुरु/मुर्शिद) वाली (की) लाली (लालिमा/नूर) ओ (हे) यार (मित्र) ।"
                ],
                "english_gloss": [
                    "आहद (The Absolute One/Ahad) विचों (from within) अहमद (Ahmad/Muhammad) होया (became), विचों (from within) मीम (the letter Meem/veil of human form) निकाली (withdrew/removed) ओ (O) यार (friend) ।",
                    "दरमुआनी (intercession/union of love) दी (of) धूम (fame/clamor) मची (arisen) है (has), नैणां (from the eyes) तों (from) घुंड (veil) उठाली (lifted) ओ (O) यार (friend) ।",
                    "जो (which) रंग (hue) रंगिआ (dyed) गूढ़ा (deep/indelible) रंगिआ (dyed), मुरशद (of the Master) वाली (belonging) लाली (crimson glow) ओ (O) यार (friend) ।"
                ],
                "poetic_hindi": [
                    "आहद से ही अहमद प्रगटे, 'मीम' का परदा दूर किया,",
                    "नेत्रों से घूँघट को खोला, प्रेम-नूर भरपूर किया ।",
                    "जो रंग रँगिया गहरा रँगिया, मुर्शिद वाली लाली ओ यार !"
                ],
                "poetic_english": [
                    "From Ahad, the Sole One, Ahmad came to flower, removing the 'Meem' which veiled His face;",
                    "The veil from my eyes was lifted that hour, revealing the splendor of infinite grace.",
                    "The dye wherewith I am dyed is deep, the Master’s crimson glow, O Friend!"
                ]
            },
            {
                "original": [
                    "सूराएयासीन मज़मल्ल वाला, बदला गरज संभाली ओ यार ।  ",
                    "ज़ुलफ स्याह दे विच यद बैज़ा, दे चमकार विखाली ओ यार ।  ",
                    "जो रंग रंगिआ गूढ़ा रंगिआ, मुरशद वाली लाली ओ यार ।"
                ],
                "hindi_gloss": [
                    "सूराएयासीन (सूरह यासीन—कुरान का हृदय) मज़मल्ल (सूरह मुज़्ज़म्मिल—कम्बल ओढ़ने वाले प्रियतम) वाला (वाला), बदला (बादल) गरज (गरजकर) संभाली (कृपा-वर्षा को संभाल लिया) ओ (हे) यार (प्यारे) ।",
                    "ज़ुलफ (केशों/काली लटों) स्याह (काली) दे (के) विच (भीतर) यद (यद-ए-बैज़ा—मूसा का चमत्कारिक श्वेत-दीप्त हाथ) बैज़ा (चमकता हुआ हाथ), दे (देकर) चमकार (दिव्य चमक/चमत्कार) विखाली (दिखाई) ओ (हे) यार (मित्र) ।",
                    "जो (जो) रंग (रंग) रंगिआ (रंगा) गूढ़ा (गहरा) रंगिआ (रंगा), मुरशद (मुर्शिद) वाली (की) लाली (लाली) ओ यार ।"
                ],
                "english_gloss": [
                    "सूराएयासीन (Surah Yaseen) मज़मल्ल (Surah al-Muzzammil/the mantle-cloaked one) वाला (the possessor), बदला (cloud of mercy) गरज (thundering) संभाली (poured down) ओ (O) यार (friend) ।",
                    "ज़ुलफ (tresses) स्याह (dark/pitch-black) दे (of) विच (within) यद (hand) बैज़ा (luminous/white hand of Moses), दे (giving) चमकार (radiant flashes) विखाली (revealed) ओ (O) यार (friend) ।",
                    "जो (which) रंग (dye) रंगिआ (dyed) गूढ़ा (deep) रंगिआ (dyed), मुरशद (the Master’s) वाली (belonging) लाली (crimson glow) ओ यार ।"
                ],
                "poetic_hindi": [
                    "सूरह यासीन, मुज़्ज़म्मिल वाले, कृपा-घटा बन गरज उठे,",
                    "काली ज़ुल्फ़ों में चमका 'यद-ए-बैज़ा', दिव्य नूर से नैन जुड़े ।",
                    "जो रंग रँगिया गहरा रँगिया, मुर्शिद वाली लाली ओ यार !"
                ],
                "poetic_english": [
                    "He of Ya-Seen and the Mantle of grace, poured mercy like thunderclouds sweeping the skies;",
                    "Through black curling tresses the White Hand shone bright, flashing with wonder before longing eyes.",
                    "The dye wherewith I am dyed is deep, the Master’s crimson glow, O Friend!"
                ]
            },
            {
                "original": [
                    "मूतू-कबला-अंता-मूतू होया, मोयां नूं मार जवाली ओ यार ।  ",
                    "बुल्ल्हा शौह मेरे घर आया, कर कर नाच वखाली ओ यार ।  ",
                    "जो रंग रंगिआ गूढ़ा रंगिआ, मुरशद वाली लाली ओ यार ।"
                ],
                "hindi_gloss": [
                    "मूतू-कबला-अंता-मूतू (हदीस: 'मूतू क़ब्ल अन तमूतू'—मरने से पूर्व मर जाओ) होया (हो गया/सिद्ध हुआ), मोयां (मृतप्राय/अहंकारी को) नूं (को) मार (अहं को मारकर) जवाली (अमर जीवन प्रदान किया) ओ यार ।",
                    "बुल्ल्हा (बुल्ले का) शौह (शाह/परमात्मा) मेरे (मेरे) घर (हृदय-गृह में) आया (आ गया), कर (कर-) कर (करके) नाच (आनंद-नृत्य) वखाली (दिखाया) ओ यार ।",
                    "जो (जो) रंग (रंग) रंगिआ (रंगा) गूढ़ा (गहरा) रंगिआ (रंगा), मुरशद (मुर्शिद) वाली (की) लाली (लाली) ओ यार ।"
                ],
                "english_gloss": [
                    "मूतू-कबला-अंता-मूतू (the prophetic saying: 'Die before you die') होया (became realized), मोयां (the living-dead) नूं (unto) मार (slaying their ego) जवाली (revived into immortal life) ओ (O) यार (friend) ।",
                    "बुल्ल्हा (Bulleh’s) शौह (Lord) मेरे (my) घर (home/heart) आया (came), कर (making) कर (doing) नाच (ecstatic dance) वखाली (manifested) ओ (O) यार (friend) ।",
                    "जो (which) रंग (dye) रंगिआ (dyed) गूढ़ा (deep) रंगिआ (dyed), मुरशद (Master’s) वाली (belonging) लाली (crimson glow) ओ यार ।"
                ],
                "poetic_hindi": [
                    "'मरने से पहले मर जाओ', मिट कर अमर जीवन पाया,",
                    "बुल्ल्हा शौह मेरे घर आए, झूम-झूम कर नाच दिखाया ।",
                    "जो रंग रँगिया गहरा रँगिया, मुर्शिद वाली लाली ओ यार !"
                ],
                "poetic_english": [
                    "'Die before dying'—the holy decree, slays the false self to awaken the soul;",
                    "Bulleh's Lord entered my courtyard so free, dancing in ecstasy making me whole.",
                    "The dye wherewith I am dyed is deep, the Master’s crimson glow, O Friend!"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी सूफ़ी हकीकत का सर्वोच्च शिखर है। 1. 'आहद विचों अहमद': अरबी में 'आहद' (अकेला/ईश्वर) में 'मीम' जोड़ने पर 'अहमद' बनता है। सूफियों के अनुसार 'मीम' सृष्टि और मानवरूप का प्रतीक है; जब साधक 'मीम' (अहंकार/भौतिकता) को निकाल देता है तो वह पुनः 'आहद' (शुद्ध ब्रह्म) में विलीन हो जाता है। 2. 'यद-ए-बैज़ा': हज़रत मूसा का चमत्कारिक हाथ जो सूर्य की भांति चमकता था—यहाँ यह मुर्शिद के आंतरिक नूर का रूपक है। 3. 'मूतू कबला अन तमूतू': शारीरिक मृत्यु से पूर्व अहंकार की मृत्यु ही अमर जीवन (बक़ा) का मार्ग है।"
    },
    {
        "id": 58,
        "title": "कदी आ मिल बिरहों सताई नूं",
        "title_english": "Come Meet Me Sometime, Sufferer of Separation",
        "historical_context": "इस काफी में विरहिणी जीवात्मा की करुण पुकार है। वह अपने प्रियतम से मिलने की प्रार्थना करती है और इस बात को रेखांकित करती है कि प्रेम कोई सहज व्यापार नहीं है; जिसने भी प्रेम की चाह की है, उसे सर्वप्रथम अपना शीश प्रभु को अर्पित करना पड़ा है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: कदी आ मिल बिरहों सताई नूं)",
        "raga": "राग जोगिया / आसावरी",
        "theme": "विरह की तड़प, शीश का समर्पण, कर्मकांडों से परे ईश्वर-कृपा",
        "stanzas": [
            {
                "original": [
                    "इश्क लग्गे तां है है कूकें,  ",
                    "तूं की जाने पीड़ पराई नूं ।  ",
                    "कदी आ मिल बिरहों सताई नूं ।"
                ],
                "hindi_gloss": [
                    "इश्क (प्रेम) लग्गे (लगे जब) तां (तब) है (हाय) है (हाय) कूकें (पुकारता/चीखता है),",
                    "तूं (तू) की (क्या) जाने (जानेगा) पीड़ (पीड़ा/दर्द) पराई (दूसरे की) नूं (को) ।",
                    "कदी (कभी) आ (आकर) मिल (मिल) बिरहों (विरह की) सताई (सताई हुई) नूं (को) ।"
                ],
                "english_gloss": [
                    "इश्क (love) लग्गे (strikes) तां (then) है (alas) है (alas) कूकें (one wails/cries aloud),",
                    "तूं (thou) की (what) जाने (knowest) पीड़ (the pain/agony) पराई (of another) नूं (unto) ।",
                    "कदी (sometime) आ (come) मिल (meet) बिरहों (by separation) सताई (tormented soul) नूं (unto) ।"
                ],
                "poetic_hindi": [
                    "इश्क लगे तब हाय-हाय पुकारे, तू क्या जाने पीर पराई ?",
                    "कभी तो आकर दरस दिखा दे, इस विरह-दुखियारी को भाई !"
                ],
                "poetic_english": [
                    "When stricken with love men cry 'Alas!', how canst thou know another's grief?",
                    "Come meet me sometime, Love, at last, and grant this parted soul relief!"
                ]
            },
            {
                "original": [
                    "जे कोई इश्क वेहाज्या लोड़े,  ",
                    "सिर देवे पहले साईं नूं ।  ",
                    "कदी आ मिल बिरहों सताई नूं ।"
                ],
                "hindi_gloss": [
                    "जे (यदि) कोई (कोई मनुष्य) इश्क (प्रेम का सौदा) वेहाज्या (खरीदना/अर्जित करना) लोड़े (चाहता है),",
                    "सिर (अपना शीश) देवे (समर्पित करे) पहले (सर्वप्रथम) साईं (प्रभु/स्वामी) नूं (को) ।",
                    "कदी (कभी) आ (आकर) मिल (मिल) बिरहों (विरह) सताई (सताई हुई) नूं (को) ।"
                ],
                "english_gloss": [
                    "जे (if) कोई (anyone) इश्क (love) वेहाज्या (to purchase/traffic in) लोड़े (desires),",
                    "सिर (head) देवे (must give) पहले (first) साईं (unto the Lord/Master) नूं (to) ।",
                    "कदी (sometime) आ (come) मिल (meet) बिरहों (by parting) सताई (tormented one) नूं (unto) ।"
                ],
                "poetic_hindi": [
                    "जो कोई चाहे इश्क खरीदना, पहले शीश चढ़ाए साईं को,",
                    "अहंकार मिटा कर जो मरे, वही पाए उस दानाई को ।",
                    "कदी आ मिल बिरहों सताई नूं !"
                ],
                "poetic_english": [
                    "Whoever seeks Love's boundless store, must yield his head unto the King;",
                    "Laying down life before His door, with selfless soul surrender bring.",
                    "Come meet me sometime, Love, at last!"
                ]
            },
            {
                "original": [
                    "अमलां वालियां लंघ लंघ गईआं,  ",
                    "साडियां लज्जां माही नूं ।  ",
                    "कदी आ मिल बिरहों सताई नूं ।"
                ],
                "hindi_gloss": [
                    "अमलां (सत्कर्मों/धार्मिक आचार) वालियां (वाली स्त्रियां/साधक) लंघ (पार) लंघ (पार) गईआं (हो गईं/भवसागर तर गईं),",
                    "साडियां (मेरी/हम जैसों की) लज्जां (लाज/मर्यादा का भार) माही (प्रियतम/ईश्वर) नूं (पर ही है) ।",
                    "कदी (कभी) आ मिल बिरहों सताई नूं ।"
                ],
                "english_gloss": [
                    "अमलां (good deeds/virtues) वालियां (possessors of) लंघ (crossed) लंघ (crossed) गईआं (over),",
                    "साडियां (our) लज्जां (honor/shame) माही (unto the Beloved) नूं (belongs) ।",
                    "कदी (sometime) आ मिल बिरहों सताई नूं ।"
                ],
                "poetic_hindi": [
                    "सत्कर्मों वाली तो पार उतर गईं, हम निर्गुण का कौन सहारा ?",
                    "मेरी लाज अब तेरे ही हाथ, तू ही खेवेगा यह किनारा !"
                ],
                "poetic_english": [
                    "The souls of righteous works have crossed, the ocean safely to the shore;",
                    "My honor rests in Thee alone, Beloved Lord for evermore!",
                    "Come meet me sometime, Love, at last!"
                ]
            },
            {
                "original": [
                    "ग़म दे वहन सितम दियां कांगां,  ",
                    "किसे कयर कप्पर विच पाई नूं ।  ",
                    "कदी आ मिल बिरहों सताई नूं ।"
                ],
                "hindi_gloss": [
                    "ग़म (शोक/दुख) दे (के) वहन (प्रवाह/धाराएं) सितम (अत्याचार/पीड़ा) दियां (की) कांगां (बाढ़/उफनती लहरें),",
                    "किसे (किसी भयानक) कयर (गहरे भंवर) कप्पर (कपाट/चट्टानों वाले भंवर) विच (में) पाई (फंसी हुई मुझ) नूं (को) ।",
                    "कदी (कभी) आ मिल बिरहों सताई नूं ।"
                ],
                "english_gloss": [
                    "ग़म (of sorrow) दे (of) वहन (currents) सितम (of tyranny) दियां (of) कांगां (floods/surging waves),",
                    "किसे (some) कयर (abyssal) कप्पर (whirlpool/eddy) विच (in) पाई (thrust/trapped) नूं (unto me) ।",
                    "कदी (sometime) आ मिल बिरहों सताई नूं ।"
                ],
                "poetic_hindi": [
                    "गम की धारा, सितम की बाढ़, गहरे भंवर में नैया डोले,",
                    "तू ही आ पतवार पकड़ ले, जब कोई न मीठा बोले !"
                ],
                "poetic_english": [
                    "Currents of grief and floods of tears, sweep me in whirlpools dark and deep;",
                    "Beset by tempest, dread, and fears, upon the rocks my spirits weep.",
                    "Come meet me sometime, Love, at last!"
                ]
            },
            {
                "original": [
                    "मां प्यु छड्ड सईआं मैं भुल्लियां,  ",
                    "बलेहारी राम दुहाई नूं ।  ",
                    "कदी आ मिल बिरहों सताई नूं ।"
                ],
                "hindi_gloss": [
                    "मां (माता) प्यु (पिता को) छड्ड (छोड़कर) सईआं (सखियों को) मैं (मैं) भुल्लियां (भूल गई),",
                    "बलेहारी (बलिहारी/न्योछावर हूँ) राम (प्रभु/राम की) दुहाई (दुहाई/पुकार) नूं (पर) ।",
                    "कदी (कभी) आ मिल बिरहों सताई नूं ।"
                ],
                "english_gloss": [
                    "मां (mother) प्यु (father) छड्ड (leaving) सईआं (companions) मैं (I) भुल्लियां (forgot),",
                    "बलेहारी (consecrated/surrendered) राम (of the Lord/Ram) दुहाई (invocation/plea) नूं (unto) ।",
                    "कदी (sometime) आ मिल बिरहों सताई नूं ।"
                ],
                "poetic_hindi": [
                    "मात-पिता छोड़े, सखियां बिसराईं, सब जग का नाता तोड़ा,",
                    "राम-दुहाई पर बलिहारी, तुमसे ही जीवन जोड़ा !"
                ],
                "poetic_english": [
                    "Forsaking parents, friends, and kin, to Thy sweet name I consecrated all;",
                    "Cleansed of all earthly pride within, answering Thine eternal call.",
                    "Come meet me sometime, Love, at last!"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी कबीर और मीरा की भक्ति-परंपरा के समान सूफी समर्पण को दर्शाती है। 'सिर देवे पहले साईं नूं'—यह सूफी और संतमत दोनों का केंद्रीय विचार है (कबीर: 'सीस उतारे भुईं धरै तब पैठे घर माहिं')। बुल्ले शाह 'राम दुहाई' शब्द का प्रयोग करके यह सिद्ध करते हैं कि उनके लिए ईश्वर की सत्ता किसी विशेष धार्मिक शब्दावली में सीमित नहीं है।"
    },
    {
        "id": 59,
        "title": "कदी आ मिल यार प्यारिआ",
        "title_english": "Come Meet Me, Beloved Friend",
        "historical_context": "इस संक्षिप्त किंतु अत्यंत कोमल काफी में बुल्ले शाह विरह की तीव्र अग्नि में जलते हुए हृदय की तड़प को कोयल के कूकने और 'शाम' (भगवान श्रीकृष्ण / प्रियतम) की स्मृति से जोड़ते हैं।",
        "meter": "पंजाबी छोटी काफी (लयबद्ध दोहा-संकर)",
        "raga": "राग सारंग / मेघ",
        "theme": "विरह की अग्नि, कोयल की कूक, प्रियतम शाम की स्मृति, मिलन की अभिलाषा",
        "stanzas": [
            {
                "original": [
                    "कदी आ मिल यार प्यारिआ ।  ",
                    "तेरियां वाटां तों सिर वारिआ ।"
                ],
                "hindi_gloss": [
                    "कदी (कभी) आ (आकर) मिल (मिल) यार (हे मित्र/प्रियतम) प्यारिआ (प्यारे),",
                    "तेरियां (तेरी) वाटां (मार्गों/रास्तों) तों (पर) सिर (शीश) वारिआ (न्योछावर कर दिया) ।"
                ],
                "english_gloss": [
                    "कदी (sometime) आ (come) मिल (meet) यार (friend) प्यारिआ (beloved),",
                    "तेरियां (upon Thy) वाटां (pathways) तों (upon) सिर (head/life) वारिआ (sacrificed) ।"
                ],
                "poetic_hindi": [
                    "कभी तो आ मिल प्यारे यार, तेरी राहों पर शीश निसार !"
                ],
                "poetic_english": [
                    "Come meet me, O Beloved Friend, upon Thy paths my life I spend!"
                ]
            },
            {
                "original": [
                    "चढ़ बागीं कोइल कूकदी,  ",
                    "नित सोज़-इ-अलम दे फूकदी,  ",
                    "मैनूं ततड़ी को शाम विसारिआ ।  ",
                    "कदी आ मिल यार प्यारिआ ।"
                ],
                "hindi_gloss": [
                    "चढ़ (चढ़कर) बागीं (बगीचों में) कोइल (कोयल) कूकदी (कूकती है),",
                    "नित (नित्य/प्रतिदिन) सोज़-इ-अलम (शोक और विरह की अग्नि) दे (के अंगारे) फूकदी (फूंकती/जलाती है),",
                    "मैनूं (मुझ) ततड़ी (दुर्भागिनी/विरह-तपी) को (को) शाम (श्याम/प्रियतम कृष्ण) विसारिआ (भुला दिया है) ।",
                    "कदी आ मिल यार प्यारिआ ।"
                ],
                "english_gloss": [
                    "चढ़ (perched) बागीं (in gardens) कोइल (the cuckoo) कूकदी (calls/sings),",
                    "नित (daily) सोज़-इ-अलम (flames of sorrow and longing) दे (of) फूकदी (fans/kindles),",
                    "मैनूं (me) ततड़ी (the wretched/burning one) को (unto) शाम (Shyam/Beloved Krishna) विसारिआ (has forgotten) ।",
                    "कदी आ मिल यार प्यारिआ ।"
                ],
                "poetic_hindi": [
                    "बागों में चढ़ कोयल कूकती, नित्य विरह-अंगारे फूंकती,",
                    "मुझ दुखियारी को बिसराया, क्यों न आए शाम मुरार ?"
                ],
                "poetic_english": [
                    "The cuckoo cries from leafy bowers, fanning grief's fire through lonely hours;",
                    "Shyam hath forgotten this burning heart, leaving me bruised by sorrow's dart!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु कदी घर आवसी,  ",
                    "मेरी बलदी भा बुझावसी,  ",
                    "उहदी वाटां तों सिर वारिआ ।  ",
                    "कदी आ मिल यार प्यारिआ ।  ",
                    "तेरियां वाटां तों सिर वारिआ ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ला कहता है) शहु (शाह/प्रियतम) कदी (कभी तो) घर (मेरे हृदय-घर) आवसी (आएगा),",
                    "मेरी (मेरी) बलदी (जलती हुई) भा (आग/अग्नि) बुझावसी (बुझाएगा),",
                    "उहदी (उसकी) वाटां (राहों) तों (पर) सिर (शीश) वारिआ (न्योछावर कर दिया) ।",
                    "कदी (कभी) आ मिल यार प्यारिआ ।",
                    "तेरियां वाटां तों सिर वारिआ ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh says) शहु (the Lord) कदी (sometime) घर (home) आवसी (will arrive),",
                    "मेरी (my) बलदी (burning) भा (fire/flames of separation) बुझावसी (will quench),",
                    "उहदी (His) वाटां (pathways) तों (upon) सिर (head) वारिआ (sacrificed) ।",
                    "कदी आ मिल यार प्यारिआ ।",
                    "तेरियां वाटां तों सिर वारिआ ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा शौह जब घर आएँगे, जलती विरह-आग बुझाएँगे,",
                    "उनकी राहों पर शीश निसार, कभी तो आ मिल प्यारे यार !"
                ],
                "poetic_english": [
                    "Bulleh’s Lord shall to my cottage turn, and quench these flames that fiercely burn;",
                    "Upon His pathway life I lay, come meet me, Love, without delay!"
                ]
            }
        ],
        "philosophical_meaning": "इस काफी में भारतीय भक्ति-काव्य और सूफी विरह-भावना का मधुर संगम है। कोयल की कूक विरह के उद्दीपन विभाव का कार्य करती है। बुल्ले शाह का 'शाम' (श्याम) शब्द का प्रयोग परमात्मा के साक्षात माधुर्य स्वरूप का द्योतक है।"
    },
    {
        "id": 60,
        "title": "कदी आपनी आख बुलाओगे",
        "title_english": "Wilt Thou Ever Call Me Thine Own?",
        "historical_context": "यह 10 बंधों की एक अत्यंत गंभीर, भावपूर्ण और शास्त्रीय काफी है। इसमें बुल्ले शाह अपने मुर्शिद हज़रत शाह इनायत के समक्ष पूर्ण आत्म-समर्पण की याचना करते हैं। वे अपने अहंकार के विनाश (फना), मंसूर की भांति सूली पर चढ़ने की तैयारी और अनहद नाद के साक्षात्कार का वर्णन करते हुए पूछते हैं कि हे प्रभु, क्या कभी तुम मुझे 'अपना' कहकर पुकारोगे?",
        "meter": "पंजाबी काफी (10 अंतरे, तुक: बुलाओगे / चढ़ाओगे / बणाओगे)",
        "raga": "राग तोड़ी / धनाश्री",
        "theme": "आत्म-समर्पण, फना और बका, मंसूर का दृष्टांत, मुर्शिद शाह इनायत का दीदार",
        "stanzas": [
            {
                "original": [
                    "मैं बेगुन क्या गुन किया है, तन पिया है मन पिया है,  ",
                    "उह पिया सु मोरा जिया है, पिया पिया से रल जाओगे ।  ",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "hindi_gloss": [
                    "मैं (मैं) बेगुन (निर्गुण/गुणहीन ने) क्या (क्या) गुन (गुण/पुण्य) किया (किया) है, तन (तन भी) पिया (प्रियतम का) है (है) मन (मन भी) पिया (प्रियतम का) है,",
                    "उह (वही) पिया (प्रियतम) सु (तो) मोरा (मेरा) जिया (प्राण/जीवन) है, पिया (पिया) पिया (पिया के साथ) से (से) रल (एकाकार हो) जाओगे (जाओगे) ।",
                    "कदी (कभी क्या) आपनी (अपनी दासी) आख (कहकर) बुलाओगे (बुलाओगे) ।"
                ],
                "english_gloss": [
                    "मैं (I) बेगुन (virtueless) क्या (what) गुन (merit) किया (have done) है (have), तन (body) पिया (belongs to Beloved) है (is) मन (mind) पिया (belongs to Beloved) है,",
                    "उह (that) पिया (Beloved) सु (indeed) मोरा (my) जिया (life/soul) है (is), पिया (Beloved) पिया (with Beloved) से (with) रल (merge) जाओगे (wilt Thou) ।",
                    "कदी (ever) आपनी (Thine own) आख (saying) बुलाओगे (wilt Thou call me) ।"
                ],
                "poetic_hindi": [
                    "मुझ निर्गुण में क्या गुण स्वामी, तन भी तेरा, मन भी तेरा,",
                    "तू ही मेरे प्राणों का आधार, पिया में मिल जाए जीवन मेरा ।",
                    "कभी अपनी कह कर बुलाओगे ?"
                ],
                "poetic_english": [
                    "No virtues, Lord, have I to claim—my body and my soul are Thine;",
                    "Beloved is my breath and aim, when shall this drop blend with the Divine?",
                    "Wilt Thou ever call me Thine own?"
                ]
            },
            {
                "original": [
                    "मैं फ़ानी आप को दूर करां, तैं बाकी आप हज़ूर करां,  ",
                    "जे अज़हार वांग मनसूर करां, खड़ सूली पकड़ चढ़ाओगे ।  ",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "hindi_gloss": [
                    "मैं (मैं) फ़ानी (नश्वर/अहंकारमय) आप (स्वयं) को (को) दूर (नष्ट) करां (करूँ), तैं (तुझ) बाकी (चिरंतन/अमर प्रभु को) आप (स्वयं) हज़ूर (उपस्थित/प्रत्यक्ष) करां (अनुभव करूँ),",
                    "जे (यदि) अज़हार (रहस्योद्घाटन/सत्य का प्रकटन) वांग (तरह) मनसूर (मंसूर की) करां (करूँ), खड़ (ले जाकर) सूली (सूली पर) पकड़ (पकड़कर) चढ़ाओगे (चढ़ा दोगे) ।",
                    "कदी (कभी क्या) आपनी (अपनी) आख (कहकर) बुलाओगे ।"
                ],
                "english_gloss": [
                    "मैं (I) फ़ानी (mortal self) आप (myself) को (unto) दूर (efface) करां (shall make), तैं (Thee) बाकी (the Eternal) आप (Thyself) हज़ूर (present) करां (realize),",
                    "जे (if) अज़हार (revelation of Truth) वांग (like) मनसूर (Mansur Hallaj) करां (I proclaim), खड़ (taking) सूली (gallows) पकड़ (grasping) चढ़ाओगे (wilt raise me) ।",
                    "कदी (ever) आपनी (Thine own) आख (saying) बुलाओगे (wilt call me) ।"
                ],
                "poetic_hindi": [
                    "नश्वर मैं को दूर हटाऊँ, नित्य प्रभु को हज़ूर मैं पाऊँ,",
                    "मंसूर सदृश सच प्रकट करूँ तो क्या सूली पर चढ़वाओगे ?",
                    "कभी अपनी कह कर बुलाओगे ?"
                ],
                "poetic_english": [
                    "Let mortal self be swept away, that Thine eternal Face may shine;",
                    "If like Hallaj the Truth I say, wilt Thou to gallows me consign?",
                    "Wilt Thou ever call me Thine own?"
                ]
            },
            {
                "original": [
                    "मैं जागी सभ सोया है, खुल्ल्ही पलक ते उठ के रोया है,  ",
                    "जुज़ मसती काम ना होया है, कदी मसत अलस्सत बणाओगे ।  ",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "hindi_gloss": [
                    "मैं (मैं) जागी (जाग रही हूँ) सभ (सारा संसार) सोया (सोया हुआ) है, खुल्ल्ही (खुली) पलक (पलकें) ते (और) उठ (उठकर) के (के) रोया (रोई) है,",
                    "जुज़ (बिना/सिवाय) मसती (ईश्वरीय मस्ती के) काम (कार्य/मुक्ति) ना (नहीं) होया (हो सकता) है, कदी (कभी क्या मुझे) मसत (मस्त) अलस्सत (अलस्त के दिन का मतवाला) बणाओगे (बनाओगे) ।",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "english_gloss": [
                    "मैं (I) जागी (awake) सभ (all) सोया (slumbers) है (is), खुल्ल्ही (opened) पलक (eyelids) ते (and) उठ (rising) के (having) रोया (wept) है (has),",
                    "जुज़ (except/without) मसती (divine drunkenness) काम (salvation/purpose) ना (not) होया (accomplished) है (is), कदी (ever) मसत (drunk) अलस्सत (with the wine of the Primal Covenant/Alast) बणाओगे (wilt Thou make me) ।",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "poetic_hindi": [
                    "सारा जग सोता, मैं जागी, पलकें खोल विरह में रोई,",
                    "बिन मस्ती यह काम न सधता, 'अलस्त'-मदिरा में कर दो विभोरी ।",
                    "कभी अपनी कह कर बुलाओगे ?"
                ],
                "poetic_english": [
                    "I watch while all the world doth sleep, with open eyes my sorrows stream;",
                    "Unless through holy joy I weep, nothing fulfills this earthly dream.",
                    "Wilt Thou make me drunk with the Primal Wine? Wilt Thou ever call me Thine own?"
                ]
            },
            {
                "original": [
                    "जदों अनहद बण दो नैन धरे, अग्गे सिर बिन धड़ के लाख पड़े,  ",
                    "उच्छल रंगन दे दरिआ चढ़े, मेरे लहू दी नदी वगाओगे ।  ",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "hindi_gloss": [
                    "जदों (जब) अनहद (अनहद नाद के समान) बण (बनकर) दो (दोनों) नैन (नेत्र) धरे (सामने रखे/दृष्टि डाली), अग्गे (आगे) सिर (शीश) बिन (बिना) धड़ (धड़ों) के (के) लाख (लाखों) पड़े (पड़े हैं),",
                    "उच्छल (उछलकर) रंगन (प्रेम-रंगों) दे (के) दरिआ (दरिया/नदियां) चढ़े (उफन पड़े), मेरे (मेरे) लहू (रक्त) दी (की) नदी (नदी) वगाओगे (बहाओगे) ।",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "english_gloss": [
                    "जदों (when) अनहद (infinite/unstruck sound) बण (becoming) दो (two) नैन (eyes) धरे (gazed), अग्गे (ahead) सिर (heads) बिन (without) धड़ (torso/bodies) के (of) लाख (hundreds of thousands) पड़े (lie fallen),",
                    "उच्छल (surging) रंगन (of hues) दे (of) दरिआ (rivers) चढ़े (swelled), मेरे (my) लहू (blood’s) दी (of) नदी (river) वगाओगे (wilt Thou cause to flow) ।",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "poetic_hindi": [
                    "अनहद बन जब नैन मिले, लाखों शीश कटे बिन धड़ के,",
                    "रंगों के दरिया उफन पड़े, क्या मेरे लहू की नदी बहाओगे ?",
                    "कभी अपनी कह कर बुलाओगे ?"
                ],
                "poetic_english": [
                    "When Thy celestial eyes flashed clear, a hundred thousand heads lay low;",
                    "Rivers of ecstasy draw near—wilt Thou bid my heart's blood to flow?",
                    "Wilt Thou ever call me Thine own?"
                ]
            },
            {
                "original": [
                    "किसे आशक ना सुक्ख सोना ए असां रो रो के मुक्ख धोना ए,  ",
                    "इह जादू है कि टूना ए इस रोग दा भोग बणाओगे ।  ",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "hindi_gloss": [
                    "किसे (किसी भी) आशक (सच्चे प्रेमी ने) ना (नहीं) सुक्ख (सुख की नींद) सोना (सोया) ए (है), असां (हमने) रो (रो-) रो (रोकर) के (के) मुक्ख (मुख) धोना (धोया) ए (है),",
                    "इह (यह) जादू (जादू) है (है) कि (अथवा) टूना (टोना/सम्मोहन) ए (है), इस (इस) रोग (प्रेम-रोग) दा (का) भोग (भोग/औषध) बणाओगे (बनाओगे) ।",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "english_gloss": [
                    "किसे (any) आशक (lover) ना (not) सुक्ख (in peace) सोना (sleeps) ए (has), असां (we) रो (weeping) रो (weeping) के (having) मुक्ख (face) धोना (wash) ए (do),",
                    "इह (is this) जादू (magic) है (is) कि (or) टूना (sorcery/spell) ए (is), इस (of this) रोग (malady) दा (of) भोग (consummation/cure) बणाओगे (wilt Thou make) ।",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "poetic_hindi": [
                    "आशिक को सुख-नींद कहाँ, हम रो-रो मुखड़ा धोते हैं,",
                    "जादू है यह या टोना है, इस रोग का भोग बनाते हो ?",
                    "कभी अपनी कह कर बुलाओगे ?"
                ],
                "poetic_english": [
                    "No lover finds sweet sleep or rest, with tears we wash our face each day;",
                    "Is this enchantment in the breast? Wilt Thou this torment's price repay?",
                    "Wilt Thou ever call me Thine own?"
                ]
            },
            {
                "original": [
                    "कहो क्या सिर इश्क बिचारेगा, फिर क्या बीसी निरवारेगा,  ",
                    "जथ दार उप्पर सिर वारेगा, तब पिच्छों ढोल वजाओगे ।  ",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "hindi_gloss": [
                    "कहो (कहो) क्या (क्या) सिर (शीश की) इश्क (इश्क) बिचारेगा (परवाह करेगा), फिर (फिर) क्या (क्या) बीसी (गिनती/सांसारिक हिसाब) निरवारेगा (निपटाएगा),",
                    "जथ (जब) दार (सूली/फांसी) उप्पर (पर) सिर (शीश) वारेगा (न्योछावर करेगा), तब (तब) पिच्छों (उसके बाद) ढोल (विजय का ढोल) वजाओगे (बजाओगे) ।",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "english_gloss": [
                    "कहो (say) क्या (what) सिर (head/life) इश्क (love) बिचारेगा (cares for), फिर (then) क्या (what) बीसी (scores/reckoning) निरवारेगा (settle),",
                    "जथ (when) दार (gallows) उप्पर (upon) सिर (head) वारेगा (sacrifices), तब (then) पिच्छों (afterwards) ढोल (victory drums) वजाओगे (wilt Thou beat) ।",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "poetic_hindi": [
                    "शीश की चिंता क्या आशिक को, क्या वह गिनती गिनता है ?",
                    "सूली पर जब शीश चढ़ेगा, तब क्या ढोल बजाओगे ?",
                    "कभी अपनी कह कर बुलाओगे ?"
                ],
                "poetic_english": [
                    "What lover counts the price of head, or weighs the petty score of loss?",
                    "When life upon the scaffold's shed, wilt Thou beat drums before the cross?",
                    "Wilt Thou ever call me Thine own?"
                ]
            },
            {
                "original": [
                    "मैं आपना मन कबाब किया, आंखों का अरक शराब किया,  ",
                    "रग तारां हड्ड कबाब किया, क्यामत क्या नाम बुलाओगे ।  ",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "hindi_gloss": [
                    "मैं (मैंने) आपना (अपना) मन (हृदय) कबाब (कबाब/अग्नि में भुना हुआ) किया (कर दिया), आंखों (नेत्रों) का (का) अरक (अश्रु-जल/अर्क) शराब (मदिरा) किया (बना दिया),",
                    "रग (नसों के) तारां (तारों) हड्ड (तथा हड्डियों को) कबाब (अंगारों पर भुना) किया (कर दिया), क्यामत (कयामत/प्रलय के दिन) क्या (किस) नाम (नाम से) बुलाओगे (पुकारोगे) ।",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "english_gloss": [
                    "मैं (I) आपना (my own) मन (heart) कबाब (roasted/broiled) किया (have made), आंखों (of eyes) का (the) अरक (distilled essence/tears) शराब (wine) किया (have turned),",
                    "रग (veins) तारां (strings) हड्ड (bones) कबाब (roasted) किया (have made), क्यामत (on the Day of Judgment) क्या (by what) नाम (name) बुलाओगे (wilt Thou summon me) ।",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "poetic_hindi": [
                    "मन को कबाब किया विरह में, नयनों का अर्क शराब किया,",
                    "रग-तंतु और हड्डियों को भून दिया, महशर में किस नाम बुलाओगे ?",
                    "कभी अपनी कह कर बुलाओगे ?"
                ],
                "poetic_english": [
                    "My heart is roasted in the flame, my tears are wine of sacred art;",
                    "At Judgment Day what holy name wilt Thou bestow upon this heart?",
                    "Wilt Thou ever call me Thine own?"
                ]
            },
            {
                "original": [
                    "शकरंजी को क्या कीजीएगा, मन भाना सौदा लीजीएगा,  ",
                    "इह दीन दुनी किस दी जीएगा, मुझे आपना दरस बताओगे ।  ",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "hindi_gloss": [
                    "शकरंजी (शतरंज/सांसारिक चालबाजी) को (को) क्या (क्या) कीजीएगा (कीजिएगा), मन (मन को) भाना (जो प्रिय लगे वह) सौदा (प्रेम का सौदा) लीजीएगा (लीजिए),",
                    "इह (यह) दीन (धर्म) दुनी (तथा संसार) किस (किसके लिए) दी (दिए) जीएगा (जिएंगे), मुझे (मुझे) आपना (अपना) दरस (साक्षात दर्शन) बताओगे (दिखाओगे) ।",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "english_gloss": [
                    "शकरंजी (chess-game of worldly schemes) को (unto) क्या (what) कीजीएगा (wilt Thou do), मन (heart’s) भाना (pleasing) सौदा (bargain of love) लीजीएगा (take),",
                    "इह (this) दीन (faith) दुनी (and world) किस (for whose sake) दी (granted) जीएगा (live), मुझे (to me) आपना (Thy) दरस (vision) बताओगे (wilt reveal) ।",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "poetic_hindi": [
                    "शतरंज की चालों में क्या रखा, मन-भाता प्रेम-सौदा लो,",
                    "किस काम के यह दीन-दुनिया, अपना पावन दीदार तो दो !",
                    "कभी अपनी कह कर बुलाओगे ?"
                ],
                "poetic_english": [
                    "What use are worldly games of chess? Take the heart’s bargain, pure and free;",
                    "Vain are both worlds without Thy grace—unveil Thy radiant face to me!",
                    "Wilt Thou ever call me Thine own?"
                ]
            },
            {
                "original": [
                    "मैनूं आण नज़ारे ताइआ है, दो नैणां बरखा लाइआ है,  ",
                    "बन रोज़ इनायत आया है, ऐवें आपना आप जिताओगे ।  ",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "hindi_gloss": [
                    "मैनूं (मुझको) आण (आकर) नज़ारे (तेरे साक्षात दर्शन ने) ताइआ (तपा दिया/व्याकुल कर दिया) है, दो (दोनों) नैणां (नेत्रों ने) बरखा (आंसुओं की वर्षा) लाइआ (लगा दी) है,",
                    "बन (बनकर) रोज़ (नित्य/प्रतिदिन) इनायत (मुर्शिद शाह इनायत/कृपा-स्वरूप) आया (आया) है, ऐवें (यूं ही) आपना (अपना) आप (स्वरूप) जिताओगे (जताओगे/प्रकट करोगे) ।",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "english_gloss": [
                    "मैनूं (unto me) आण (arriving) नज़ारे (Thy vision) ताइआ (has heated/inflamed) है (has), दो (two) नैणां (eyes) बरखा (rain of tears) लाइआ (have brought) है (have),",
                    "बन (becoming) रोज़ (daily) इनायत (Grace / Shah Inayat) आया (arrived) है (has), ऐवें (thus) आपना (Thy own) आप (Self) जिताओगे (wilt manifest) ।",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "poetic_hindi": [
                    "तेरे नज़ारों ने तपा दिया, दो नैनों ने वर्षा लाई,",
                    "शाह इनायत बन कर आए, अपनी सत्ता यों दिखलाई !",
                    "कभी अपनी कह कर बुलाओगे ?"
                ],
                "poetic_english": [
                    "Thy vision sets my soul on fire, my two eyes pour like monsoon rain;",
                    "Shah Inayat comes with grace supreme, revealing God without a stain!",
                    "Wilt Thou ever call me Thine own?"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु नूं वेखन जाओगे, इन्हां अक्खियां नूं समझाओगे,  ",
                    "दीदार तदाहीं पाओगे, बण शाह इनायत घर आओगे ।  ",
                    "कदी आपनी आख बुलाओगे ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ला कहता है) शहु (प्रभु/शाह) नूं (को) वेखन (देखने) जाओगे (जाओगे), इन्हां (इन व्याकुल) अक्खियां (आंखों) नूं (को) समझाओगे (धैर्य बंधाओगे),",
                    "दीदार (साक्षात्कार) तदाहीं (तभी) पाओगे (पाओगे), बण (बनकर) शाह (शाह) इनायत (इनायत) घर (मेरे घर) आओगे (आओगे) ।",
                    "कदी (कभी क्या) आपनी (अपनी) आख (कहकर) बुलाओगे (बुलाओगे) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh says) शहु (the Lord) नूं (unto) वेखन (to behold) जाओगे (wilt go), इन्हां (these) अक्खियां (eyes) नूं (unto) समझाओगे (wilt console),",
                    "दीदार (the vision) तदाहीं (then alone) पाओगे (shalt obtain), बण (as) शाह (Shah) इनायत (Inayat) घर (home) आओगे (when Thou comest) ।",
                    "कदी (ever) आपनी (Thine own) आख (saying) बुलाओगे (wilt Thou summon me) ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा शौह को देखने जाओ, इन अंखियों को धीर धराओ,",
                    "दीदार तभी संभव होगा, जब शाह इनायत बन आओ !",
                    "कभी अपनी कह कर बुलाओगे ?"
                ],
                "poetic_english": [
                    "O Bulleh, go behold the Lord, console these weeping, restless eyes;",
                    "The vision only is attained when as Shah Inayat Thou arise!",
                    "Wilt Thou ever call me Thine own?"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी बुल्ले शाह के मुर्शिद-प्रेम (फना-फिश-शेख) का अनुपम उदाहरण है। सूफी दर्शन में परमात्मा का कोई निराकार अमूर्त रूप नहीं बल्कि मुर्शिद का प्रत्यक्ष रूप ही साक्षात्कार का माध्यम बनता है। अंतिम बंध में वे स्पष्ट कहते हैं: 'बण शाह इनायत घर आओगे'—अर्थात् जब तक प्रभु शाह इनायत के रूप में नहीं आते, तब तक आत्मा तृप्त नहीं हो सकती।"
    }
]

new_lexicon_terms = {
    "कमाल": {"hindi": "परिपूर्ण, सर्वोच्च, उत्कृष्ट", "english": "consummate, supreme, perfect"},
    "बेसुर": {"hindi": "सुर-रहित, शास्त्रीय संगीत के नियमों से मुक्त", "english": "unmeasured, free from formal musical scales"},
    "हुगेड़े": {"hindi": "जड़ से उखाड़ फेंकना", "english": "uproot completely"},
    "हाल": {"hindi": "आध्यात्मिक समाधि, ईश्वरीय परमानंद की अवस्था, वज्द", "english": "spiritual ecstasy, mystical trance (hal/wajd)"},
    "जमाल": {"hindi": "परम पावन सौंदर्य, ईश्वरीय आभा", "english": "divine beauty and radiant splendor"},
    "आहद": {"hindi": "अकेला, अद्वैत, निराकार ईश्वर", "english": "The One, Absolute Non-Dual Divine (Ahad)"},
    "अहमद": {"hindi": "प्रशंसा योग्य, पैगंबर मोहम्मद का नाम", "english": "The Praised One, Ahmad (Muhammad)"},
    "मीम": {"hindi": "अरबी वर्णमाला का 'म' अक्षर; सूफी रहस्यवाद में मानवरूप और स्थूल जगत का आवरण", "english": "the letter 'Meem'; symbol of human incarnation and creaturely veil"},
    "दरमुआनी": {"hindi": "मध्यस्थता, मध्य का संबंध", "english": "intercession, intermediate liaison"},
    "यद बैज़ा": {"hindi": "यद-ए-बैज़ा, मूसा का चमत्कारिक दीप्तिमान श्वेत हाथ; आध्यात्मिक प्रकाश", "english": "the luminous white hand of Moses; radiant mystic sign"},
    "जवाली": {"hindi": "जीवित किया, पुनर्जीवन दिया", "english": "revived, granted eternal life"},
    "वेहाज्या": {"hindi": "खरीदना, प्राप्त करना, व्यापार करना", "english": "to purchase, acquire, trade in"},
    "कयर": {"hindi": "गहरा भंवर, भयानक खाई", "english": "abyssal depth, treacherous gulf"},
    "कप्पर": {"hindi": "भंवर, जल-चक्र", "english": "whirlpool, deep eddy"},
    "भा": {"hindi": "आग, विरह की ज्वाला", "english": "fire, flame of separation"},
    "अलस्सत": {"hindi": "अलस्त का दिन ('अलस्तु बि-रब्बिकुम'—क्या मैं तुम्हारा रब नहीं हूँ?)", "english": "The Primal Day of the Covenant ('Am I not your Lord?')" }
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
        "completed_count": 60,
        "total": 160,
        "next_kafi_id": 61,
        "last_updated": "2026-10-17T16:55:00+05:30",
        "last_batch": "56-60",
        "status": "in_progress"
    }
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print(f"Checkpoint updated: 60/160 completed. Next ID: 61")

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
