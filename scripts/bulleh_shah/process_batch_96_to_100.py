# -*- coding: utf-8 -*-
"""
Process Kafian 96 to 100 for Bulleh Shah Trilingual Edition.
Completes Part 2 (भाग 2: काफ़ियां 51-100).
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
        "id": 96,
        "title": "मैं वैसां जोगी दे नाल, मत्थे तिलक लगा के",
        "title_english": "I Shall Go With the Yogi, Having Anointed My Brow With Tilak",
        "historical_context": "यह 16 बंधों (15 अंतरे और टेक) की बुल्ले शाह की सर्वाधिक प्रसिद्ध, क्रांतिकारी और महाकाव्यात्मक सूफी रचनाओं में से एक है। इसमें बुल्ले शाह ने हीर के जोगन बनने के लोक-आख्यान को एक सार्वभौमिक आध्यात्मिक कैनवास पर प्रस्तुत किया है। साधिका सामाजिक मान-मर्यादा और मजहबी संकीर्णता को त्यागकर अपने माथे पर तिलक लगाकर जोगी (परमेश्वर/सद्गुरु) के संग जाने का अटल प्रण लेती है। इस काफी में हज़रत मूसा और कोहे-तूर, मेअराज और बुर्राक़, कर्बला में हज़रत हसन-हुसैन की शहादत, सोहणी-महीवाल का समर्पण और कैदों की पराजय जैसे गूढ़ सूफी-ऐतिहासिक प्रसंगों को अद्वैत में पिरोया गया है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: मैं वैसां जोगी दे नाल)",
        "raga": "राग काफी / जोग / आसा",
        "theme": "प्रेम-दीक्षा, सामाजिक विद्रोह, तिलक और जोग का समन्वय, सर्वेश्वरवाद (वहदत-उल-वुजूद), कर्बला व सोहणी के रूपक",
        "stanzas": [
            {
                "original": [
                    "मैं वैसां ना रहसां होड़े, कौन कोई मैं जांदी नूं मोड़े,  ",
                    "मैनूं मुड़ना होया मुहाल, सिर ते मेहना चा के,  ",
                    "मैं वैसां जोगी दे नाल, मत्थे तिलक लगा के ।"
                ],
                "hindi_gloss": [
                    "मैं (मैं तो) वैसां (जाऊँगी ही) ना (नहीं) रहसां (रुकूँगी) होड़े (किसी के रोके), कौन (कौन है) कोई (ऐसा जो) मैं (मुझ) जांदी (जाती हुई) नूं (को) मोड़े (रोक सके/वापस मोड़ सके),",
                    "मैनूं (मेरे लिए) मुड़ना (लौटना) होया (हो चुका है) मुहाल (असंभव/दुश्वार), सिर (सिर) ते (पर) मेहना (कुल का उलाहना/कलंक) चा (उठा) के (कर),",
                    "मैं (मैं तो) वैसां (जाऊँगी) जोगी (उस जोगी) दे (के) नाल (संग ही), मत्थे (अपने माथे पर) तिलक (तिलक) लगा (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "मैं (I) वैसां (shall surely go) ना (not) रहसां (shall stay) होड़े (held back/restrained), कौन (who) कोई (anyone) मैं (me) जांदी (departing) नूं (to) मोड़े (can turn back),",
                    "मैनूं (to me) मुड़ना (turning back) होया (has become) मुहाल (impossible/arduous), सिर (head) ते (upon) मेहना (reproach/taunt) चा (bearing/taking) के (having),",
                    "मैं (I) वैसां (shall go) जोगी (yogi) दे (with) नाल (along), मत्थे (upon forehead) तिलक (sacred tilak mark) लगा (applying) के (having) ।"
                ],
                "poetic_hindi": [
                    "मैं तो जाऊँगी, रुकूँ न किसी के मोड़े, कौन भला मुझे जाने से रोड़े?",
                    "लौटना अब मेरे बस में नहीं, सिर पे कुल का कलंक उठाए ।",
                    "मैं तो चलूँगी उस जोगी के संग, माथे तिलक लगाए !"
                ],
                "poetic_english": [
                    "I shall go, none can restrain my pace; who dares turn back my departing grace?",
                    "To return is impossible now for me, bearing all taunts upon my head:",
                    "I shall go with the Yogi unto the end, with the tilak marked upon my brow so red!"
                ]
            },
            {
                "original": [
                    "जोगी नहीं इह दिल दा मीता, भुल्ल गई मैं प्यार क्यों कीता,  ",
                    "मैनूं रही ना कुझ संभाल, उस दे दरशन पा के,  ",
                    "मैं वैसां जोगी दे नाल, मत्थे तिलक लगा के ।"
                ],
                "hindi_gloss": [
                    "जोगी (यह जोगी) नहीं (कोई साधारण जोगी नहीं) इह (यह तो) दिल (मेरे हृदय) दा (का) मीता (परम मित्र/प्राणनाथ है), भुल्ल (भूल) गई (गई हूँ सब सुध-बुध कि) मैं (मैंने) प्यार (यह अगाध प्रेम) क्यों (कैसे) कीता (कर लिया),",
                    "मैनूं (मुझे) रही (रही) ना (नहीं) कुझ (कुछ भी) संभाल (तन-मन की सुध), उस (उस प्रियतम) दे (के) दरशन (दीदार) पा (प्राप्त कर) के (लेने के बाद),",
                    "मैं (मैं तो) वैसां (जाऊँगी) जोगी (उस जोगी) दे (के) नाल (संग), मत्थे (माथे पर) तिलक (तिलक) लगा (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "जोगी (yogi) नहीं (not merely) इह (this is) दिल (of heart) दा (the) मीता (true bosom friend/beloved), भुल्ल (forgot) गई (have) मैं (I) प्यार (love) क्यों (why/how) कीता (did/made),",
                    "मैनूं (to me) रही (remained) ना (not) कुझ (any) संभाल (awareness/poise), उस (his) दे (of) दरशन (divine sight) पा (gaining) के (having),",
                    "मैं (I) वैसां (shall go) जोगी (yogi) दे (with) नाल (along), मत्थे (on forehead) तिलक (tilak) लगा (applying) के (having) ।"
                ],
                "poetic_hindi": [
                    "जोगी केवल वैरागी नहीं, मेरे मन का सच्चा यार हुआ,",
                    "सुध-बुध भूली, कब और कैसे उससे ऐसा प्यार हुआ !",
                    "दीदार किया जब से उसका, अपनी कोई खबर न पाई,",
                    "मैं तो चलूँगी उस जोगी के संग, माथे तिलक लगाई !"
                ],
                "poetic_english": [
                    "This Yogi is no stranger mendicant, but the sovereign friend of my deep soul;",
                    "Lost to the world, I marvel how this boundless love consumed me whole!",
                    "Since drinking the nectar of His face, no trace of self remains in me:",
                    "I shall go with the Yogi unto the end, crowned with the tilak of ecstasy!"
                ]
            },
            {
                "original": [
                    "एस जोगी मैनूं कहियां लाईआं, हैन कलेजे कुंडियां पाईआं,  ",
                    "इश्क दा पाइआ जाल, मिट्ठी बात सुना के,  ",
                    "मैं वैसां जोगी दे नाल, मत्थे तिलक लगा के ।"
                ],
                "hindi_gloss": [
                    "एस (इस) जोगी (जोगी ने) मैनूं (मुझ पर) कहियां (गहरे प्रहार/तीर) लाईआं (चलाए हैं), हैन (और) कलेजे (मेरे हृदय में) कुंडियां (प्रेम के कांटे/अंकुश) पाईआं (फँसा दिए हैं),",
                    "इश्क (इलाही इश्क) दा (का) पाइआ (फेंका है) जाल (मायावी जाल), मिट्ठी (मधुर अमृतमयी) बात (वाणी) सुना (सुना) के (कर),",
                    "मैं (मैं तो) वैसां (जाऊँगी) जोगी (उस जोगी) दे (के) नाल (संग), मत्थे (माथे पर) तिलक (तिलक) लगा (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "एस (this) जोगी (yogi) मैनूं (unto me) कहियां (wounds/strikes) लाईआं (has dealt), हैन (has) कलेजे (in heart/liver) कुंडियां (fishhooks/barbs) पाईआं (cast/embedded),",
                    "इश्क (of divine love) दा (the) पाइआ (cast) जाल (net), मिट्ठी (sweet) बात (words) सुना (speaking) के (having),",
                    "मैं (I) वैसां (shall go) जोगी (yogi) दे (with) नाल (along), मत्थे (on forehead) तिलक (tilak) लगा (applying) के (having) ।"
                ],
                "poetic_hindi": [
                    "इस जोगी ने ऐसे घाव लगाए, दिल में प्रेम की बर्छी खाई,",
                    "मीठी-मीठी बातें कह कर, इश्क की जाली मुझ पे बिछाई ।",
                    "उसकी मोहिनी सूरत ने तो खींच लिया मेरा हर हाल,",
                    "मैं तो चलूँगी उस जोगी के संग, माथे तिलक लगा के लाल !"
                ],
                "poetic_english": [
                    "This Yogi pierced me with wondrous wounds, His hooks plunged deep into my breast;",
                    "He cast the snare of divine love with words the sweetest and the best.",
                    "Entangled in His holy net, captive to His melodious art:",
                    "I shall go with the Yogi unto the end, with the tilak blazing on my heart!"
                ]
            },
            {
                "original": [
                    "मैं जोगी नूं ख़ूब पछाता, लोकां मैनूं कमली जाता,  ",
                    "लुट्टी झंग स्याल, कन्नीं मुन्दरां पा के,  ",
                    "मैं वैसां जोगी दे नाल, मत्थे तिलक लगा के ।"
                ],
                "hindi_gloss": [
                    "मैं (मैंने तो) जोगी (इस जोगी) नूं (को) ख़ूब (भली-भाँति) पछाता (पहचान लिया है), लोकां (संसार के लोगों ने) मैनूं (मुझे) कमली (पागल/दीवानी) जाता (समझ रखा है),",
                    "लुट्टी (उसने लूट ली है पूरी) झंग (झंग) स्याल (स्याल की नगरी), कन्नीं (अपने कानों में) मुन्दरां (जोग की मुंद्राएं) पा (पहन) के (कर),",
                    "मैं (मैं तो) वैसां (जाऊँगी) जोगी (उस जोगी) दे (के) नाल (संग), मत्थे (माथे पर) तिलक (तिलक) लगा (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "मैं (I) जोगी (yogi) नूं (the) ख़ूब (well/truly) पछाता (recognized), लोकां (people) मैनूं (me) कमली (mad/crazed) जाता (deemed),",
                    "लुट्टी (plundered) झंग (Jhang) स्याल (Sial), कन्नीं (in ears) मुन्दरां (yogi earrings) पा (wearing) के (having),",
                    "मैं (I) वैसां (shall go) जोगी (yogi) दे (with) नाल (along), मत्थे (on forehead) तिलक (tilak) लगा (applying) के (having) ।"
                ],
                "poetic_hindi": [
                    "मैंने तो इस जोगी को पहचाना, जग समझे मुझको दीवानी,",
                    "कानों में मुंद्राएं पहन के लूटी उसने झंग-स्याल की राजधानी !",
                    "उसकी अलख जगाने पर तो लूट गया मेरा माल-ओ-ताल,",
                    "मैं तो चलूँगी उस जोगी के संग, माथे तिलक लगा के लाल !"
                ],
                "poetic_english": [
                    "I have known the Yogi in His truth, though worldly fools pronounce me blind;",
                    "Wearing earrings in His ears, He plundered the city of Jhang-Sial's mind!",
                    "Stripped of all pride, in ecstasy drowned, answering His sovereign call:",
                    "I shall go with the Yogi unto the end, with the tilak shining over all!"
                ]
            },
            {
                "original": [
                    "जे जोगी घर आवे मेरे, मुक्क जावन सभ झगड़े झेड़े,  ",
                    "ला सीने दे नाल, लक्ख लक्ख शगन मना के,  ",
                    "मैं वैसां जोगी दे नाल, मत्थे तिलक लगा के ।"
                ],
                "hindi_gloss": [
                    "जे (यदि) जोगी (यह जोगी) घर (आँगन/कुटी) आवे (आ जाए) मेरे (मेरे), मुक्क (समाप्त) जावन (हो जाएँ) सभ (सारे) झगड़े (विवाद) झेड़े (और कलेश),",
                    "ला (लगा लूँगी) सीने (हृदय) दे (के) नाल (साथ), लक्ख (लाखों) लक्ख (लाखों) शगन (मंगलाचार/उत्सव) मना (मना) के (कर),",
                    "मैं (मैं तो) वैसां (जाऊँगी) जोगी (उस जोगी) दे (के) नाल (संग), मत्थे (माथे पर) तिलक (तिलक) लगा (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "जे (if) जोगी (yogi) घर (home) आवे (comes) मेरे (mine), मुक्क (finished) जावन (shall be) सभ (all) झगड़े (feuds) झेड़े (disputes),",
                    "ला (clasping) सीने (breast) दे (to) नाल (close), लक्ख (hundred thousand) लक्ख (hundred thousand) शगन (blessed omens/auspicious rites) मना (celebrating) के (having),",
                    "मैं (I) वैसां (shall go) जोगी (yogi) दे (with) नाल (along), मत्थे (on forehead) तिलक (tilak) लगा (applying) के (having) ।"
                ],
                "poetic_hindi": [
                    "आ जाए गर जोगी घर मेरे, मिट जाएँ सब झगड़े-झेड़े,",
                    "लाख-लाख शगुन मना कर उसको सीने से लगा लूँ घेरे !",
                    "जीवन के सब संशय कट जाएँ, पाए मन परम निहाल,",
                    "मैं तो चलूँगी उस जोगी के संग, माथे तिलक लगा के लाल !"
                ],
                "poetic_english": [
                    "If the Yogi enters my humble home, all feuds and bitter Strife shall cease;",
                    "Clasping Him close unto my chest with myriad omens of boundless peace!",
                    "All sorrow shall dissolve in light, no shadow of grief shall ever fall:",
                    "I shall go with the Yogi unto the end, with the tilak blazing on my brow withal!"
                ]
            },
            {
                "original": [
                    "माए नी इक्क जोगी आया, दर साडे उस धूंआं पाइआ,  ",
                    "मंगदा हीर स्याल, बैठा भेस वटा के,  ",
                    "मैं वैसां जोगी दे नाल, मत्थे तिलक लगा के ।"
                ],
                "hindi_gloss": [
                    "माए (हे माँ) नी (अरी), इक्क (एक अद्भुत) जोगी (जोगी) आया (आया है), दर (द्वार पर) साडे (हमारे) उस (उसने) धूंआं (अपनी धुनी/पवित्र अग्नि) पाइआ (रमा ली है),",
                    "मंगदा (भिक्षा में मांगता है) हीर (हीर) स्याल (स्याल को), बैठा (बैठा हुआ है) भेस (जोगी का भेष) वटा (बदल) के (कर),",
                    "मैं (मैं तो) वैसां (जाऊँगी) जोगी (उस जोगी) दे (के) नाल (संग), मत्थे (माथे पर) तिलक (तिलक) लगा (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "माए (O mother) नी (listen), इक्क (a) जोगी (yogi) आया (has come), दर (at door) साडे (ours) उस (he) धूंआं (sacred fire/dhuni) पाइआ (has set/kindled),",
                    "मंगदा (begs for alms) हीर (Heer) स्याल (Sial), बैठा (sitting) भेस (guise) वटा (altering) के (having),",
                    "मैं (I) वैसां (shall go) जोगी (yogi) दे (with) नाल (along), मत्थे (on forehead) तिलक (tilak) लगा (applying) के (having) ।"
                ],
                "poetic_hindi": [
                    "ओ माँ री ! इक जोगी आया, द्वारे उसने धुनी रमाई,",
                    "भेष बदल कर बैठा है वो, हीर स्याल की भिक्षा चाही !",
                    "रोम-रोम मेरा रीझ गया है, देख के उसका रूप-जमाल,",
                    "मैं तो चलूँगी उस जोगी के संग, माथे तिलक लगा के लाल !"
                ],
                "poetic_english": [
                    "O mother mine, a Yogi came, kindle He did His sacred fire at our door;",
                    "Disguised in mendicant attire, He begs for Heer and nothing more!",
                    "My soul is captive to His charm, His beggar’s garb outshines them all:",
                    "I shall go with the Yogi unto the end, with the tilak shining on my brow withal!"
                ]
            },
            {
                "original": [
                    "तअने ना दे फुफ्फी ताई, एथे जोगी नूं किसमत लिआई,  ",
                    "हुन होया फ़ज़ल कमाल, आया है जोग सिधा के,  ",
                    "मैं वैसां जोगी दे नाल, मत्थे तिलक लगा के ।"
                ],
                "hindi_gloss": [
                    "तअने (उलाहने/व्यंग्य) ना (मत) दे (दो) फुफ्फी (हे बुआ) ताई (और ताई), एथे (यहाँ) जोगी (जोगी) नूं (को) किसमत (ईश्वरीय प्रारब्ध) लिआई (लेकर आई है),",
                    "हुन (अब) होया (हुआ है) फ़ज़ल (कृपा/अनुग्रह) कमाल (परम अनुपम), आया (वह आया) है (है) जोग (जोग/योग-साधना को) सिधा (सिद्ध कर) के (लेने के बाद),",
                    "मैं (मैं तो) वैसां (जाऊँगी) जोगी (उस जोगी) दे (के) नाल (संग), मत्थे (माथे पर) तिलक (तिलक) लगा (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "तअने (taunts) ना (do not) दे (give) फुफ्फी (aunt/father's sister) ताई (elder aunt), एथे (here) जोगी (the yogi) नूं (to) किसमत (destiny/grace) लिआई (brought),",
                    "हुन (now) होया (has happened) फ़ज़ल (divine grace) कमाल (miraculous/supreme), आया (come) है (has) जोग (yoga) सिधा (perfecting) के (having),",
                    "मैं (I) वैसां (shall go) जोगी (yogi) दे (with) नाल (along), मत्थे (on forehead) तिलक (tilak) लगा (applying) के (having) ।"
                ],
                "poetic_hindi": [
                    "ताई-बुआ मत ताने मारो, किस्मत इस जोगी को लाई,",
                    "रब का फज़ल हुआ है कामिल, जोग साध कर अलख जगाई !",
                    "सच्चे साहिब ने की रहमत, पूरी हुई मेरी प्रतिपाल,",
                    "मैं तो चलूँगी उस जोगी के संग, माथे तिलक लगा के लाल !"
                ],
                "poetic_english": [
                    "Taunt me no more, O aunts so stern, 'twas destined grace that brought Him here;",
                    "The Lord's sublime compassion shone, having perfected Yoga clear!",
                    "Now miracles of love unfold to break each worldly bond and stall:",
                    "I shall go with the Yogi unto the end, with the tilak shining on my brow withal!"
                ]
            },
            {
                "original": [
                    "माही नहीं कोई नूर इलाही, अनहद दी जिस मुरली वाही,  ",
                    "मुठीयो सू हीर स्याल, डाढे कामन पा के,  ",
                    "मैं वैसां जोगी दे नाल, मत्थे तिलक लगा के ।"
                ],
                "hindi_gloss": [
                    "माही (वह केवल ग्वाला) नहीं (नहीं है, बल्कि) कोई (साक्षात्) नूर (परम ज्योति) इलाही (इलाही/ईश्वरीय) है, अनहद (अनाहत नाद) दी (की) जिस (जिसने) मुरली (मुरली/वंशी) वाही (बजाई है),",
                    "मुठीयो (लूट/वश में कर) सू (ली है उसने) हीर (हीर) स्याल (स्याल), डाढे (अत्यंत प्रचंड/गहरे) कामन (प्रेम-जादू/वशीकरण) पा (डाल) के (कर),",
                    "मैं (मैं तो) वैसां (जाऊँगी) जोगी (उस जोगी) दे (के) नाल (संग), मत्थे (माथे पर) तिलक (तिलक) लगा (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "माही (cowherd) नहीं (not merely) कोई (some) नूर (light) इलाही (divine), अनहद (unstruck sound/Anhad) दी (of) जिस (who) मुरली (flute) वाही (played),",
                    "मुठीयो (bewitched/captivated) सू (he) हीर (Heer) स्याल (Sial), डाढे (mighty/irresistible) कामन (spells/charms of love) पा (casting) के (having),",
                    "मैं (I) वैसां (shall go) जोगी (yogi) दे (with) नाल (along), मत्थे (on forehead) तिलक (tilak) लगा (applying) के (having) ।"
                ],
                "poetic_hindi": [
                    "ग्वाला नहीं वो नूर-ए-इलाही, अनहद की बंसी लहराई,",
                    "हीर स्याल को वश में कीना, ऐसी मीठी तान सुनाई !",
                    "प्रेम के जादू डाल दिए हैं, हर ली मेरी देह-संभाल,",
                    "मैं तो चलूँगी उस जोगी के संग, माथे तिलक लगा के लाल !"
                ],
                "poetic_english": [
                    "No simple herd-boy is this prince, but God’s own transcendent ray;",
                    "He breathes the flute of Anhad Nada that sweeps the universe away!",
                    "With potent spells of mystic grace, He won Heer’s soul beyond recall:",
                    "I shall go with the Yogi unto the end, with the tilak shining on my brow withal!"
                ]
            },
            {
                "original": [
                    "लक्खां गए हज़ारां आए, उस दे भेत किसे ना पाए,  ",
                    "गल्लां तां मूसे नाल, पर कोह तूर चढ़ा के,  ",
                    "मैं वैसां जोगी दे नाल, मत्थे तिलक लगा के ।"
                ],
                "hindi_gloss": [
                    "लक्खां (लाखों) गए (चले गए) हज़ारां (हजारों) आए (आए), उस (उस परमात्मा) दे (के) भेत (रहस्य) किसे (किसी ने भी) ना (नहीं) पाए (पाए),",
                    "गल्लां (बातें कीं) तां (तो) मूसे (हज़रत मूसा) नाल (के साथ), पर (परंतु) कोह (पर्वत) तूर (तूर पर) चढ़ा (चढ़ा) के (कर),",
                    "मैं (मैं तो) वैसां (जाऊँगी) जोगी (उस जोगी) दे (के) नाल (संग), मत्थे (माथे पर) तिलक (तिलक) लगा (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "लक्खां (hundreds of thousands) गए (departed) हज़ारां (thousands) आए (arrived), उस (his) दे (of) भेत (mysteries/secrets) किसे (anyone) ना (not) पाए (unraveled),",
                    "गल्लां (discourses/talks) तां (indeed) मूसे (Moses) नाल (with), पर (yet) कोह (mount) तूर (Sinai/Tur) चढ़ा (ascending) के (having),",
                    "मैं (I) वैसां (shall go) जोगी (yogi) दे (with) नाल (along), मत्थे (on forehead) तिलक (tilak) लगा (applying) के (having) ।"
                ],
                "poetic_hindi": [
                    "लाखों आए, लाखों गुज़रे, भेद किसी ने उसका न पाया,",
                    "कोह-ए-तूर पे मूसा को भी उसने अपना जलवा दिखाया !",
                    "गूढ़ अलख है उसकी लीला, करता है वो अजब कमाल,",
                    "मैं तो चलूँगी उस जोगी के संग, माथे तिलक लगा के लाल !"
                ],
                "poetic_english": [
                    "Millions departed, thousands came, none could His deepest secret trace;",
                    "Yet unto Moses on Mount Sinai, He spoke unveiled with dazzling grace!",
                    "Beyond all dogma, forms, and creeds, His mystery governs great and small:",
                    "I shall go with the Yogi unto the end, with the tilak shining on my brow withal!"
                ]
            },
            {
                "original": [
                    "अबदहू रसूल कहाइआ, विच मिअराज बुर्राक मंगाइआ,  ",
                    "जिबराईल पकड़ लै आया, हरां मंगल गा के,  ",
                    "मैं वैसां जोगी दे नाल, मत्थे तिलक लगा के ।"
                ],
                "hindi_gloss": [
                    "अबदहू (उसका परम दास) रसूल (और पैगंबर) कहाइआ (कहलाया), विच (में) मिअराज (मेअराज/आकाशीय आरोहण की रात) बुर्राक (स्वर्गीय वाहन बुर्राक) मंगाइआ (मंगवाया),",
                    "जिबराईल (देवदूत जिबरील) पकड़ (थाम कर) लै (ले) आया (आया), हरां (स्वर्ग की अप्सराओं/हूरों ने) मंगल (मंगलगान) गा (गा) के (कर उत्सव मनाया),",
                    "मैं (मैं तो) वैसां (जाऊँगी) जोगी (उस जोगी) दे (के) नाल (संग), मत्थे (माथे पर) तिलक (तिलक) लगा (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "अबदहू (His servant) रसूल (messenger) कहाइआ (proclaimed), विच (during) मिअराज (celestial ascension/Mi'raj) बुर्राक (heavenly steed Buraq) मंगाइआ (summoned),",
                    "जिबराईल (Gabriel) पकड़ (leading/holding) लै (take) आया (brought), हरां (the heavenly houris) मंगल (felicitous songs) गा (singing) के (having),",
                    "मैं (I) वैसां (shall go) जोगी (yogi) दे (with) नाल (along), मत्थे (on forehead) तिलक (tilak) लगा (applying) के (having) ।"
                ],
                "poetic_hindi": [
                    "'अब्दुहू' रसूल कहलाया जिसने, शब-ए-मेअराज बुर्राक़ मँगाया,",
                    "जिब्राईल ने थामा जिसको, हूरों ने मंगलगान सुनाया !",
                    "उस नूरी महबूब की खातिर अर्श-ओ-फ़र्श हुए खुशहाल,",
                    "मैं तो चलूँगी उस जोगी के संग, माथे तिलक लगा के लाल !"
                ],
                "poetic_english": [
                    "Proclaimed 'His Servant and His Messenger', He bade Buraq on Mi'raj night;",
                    "Archangel Gabriel held the reins amidst the houris' anthems bright!",
                    "He who transcended space and time to sit within the heavenly hall:",
                    "I shall go with the Yogi unto the end, with the tilak shining on my brow withal!"
                ]
            },
            {
                "original": [
                    "एस जोगी दे सुनो अखाड़े, हसन हुसैन नबी दे प्यारे,  ",
                    "मार्यो सू विच जद्दाल, पानी बिन तरसा के,  ",
                    "मैं वैसां जोगी दे नाल, मत्थे तिलक लगा के ।"
                ],
                "hindi_gloss": [
                    "एस (इस) जोगी (जोगी/परम सत्ता) दे (के) सुनो (सुनो) अखाड़े (रहस्यमयी लीला-क्षेत्र/अखाड़े), हसन (हज़रत हसन) हुसैन (और हुसैन) नबी (पैगंबर) दे (के) प्यारे (लाडले),",
                    "मार्यो (बलिदान करवा दिया) सू (उसने) विच (में) जद्दाल (रणभूमि/कर्बला के भीषण संग्राम), पानी (जल के) बिन (बिना) तरसा (तड़पा) के (कर),",
                    "मैं (मैं तो) वैसां (जाऊँगी) जोगी (उस जोगी) दे (के) नाल (संग), मत्थे (माथे पर) तिलक (तिलक) लगा (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "एस (this) जोगी (yogi's) दे (of) सुनो (hear) अखाड़े (arenas/mystic proving grounds), हसन (Hasan) हुसैन (Husain) नबी (Prophet's) दे (of) प्यारे (beloveds),",
                    "मार्यो (martyred/slain) सू (he) विच (in) जद्दाल (battle/strife of Karbala), पानी (water) बिन (without) तरसा (parched/thirsting) के (having),",
                    "मैं (I) वैसां (shall go) जोगी (yogi) दे (with) नाल (along), मत्थे (on forehead) तिलक (tilak) लगा (applying) के (having) ।"
                ],
                "poetic_hindi": [
                    "इस जोगी के अखाड़े देखो: नबी के प्यारे हसन-हुसैन,",
                    "कर्बला के मैदान में मारे, बूँद-बूँद पानी बिन चैन !",
                    "इश्क की बाज़ी में शीश दिए हैं, ऐसा हुआ अजब अहवाल,",
                    "मैं तो चलूँगी उस जोगी के संग, माथे तिलक लगा के लाल !"
                ],
                "poetic_english": [
                    "Hear the stern arena of this Yogi: Hasan and Husain, the Prophet’s pride,",
                    "Were martyred in the sands of battle, parched without water by His side!",
                    "Love demands the ultimate price, a severed head, the highest thrall:",
                    "I shall go with the Yogi unto the end, with the tilak shining on my brow withal!"
                ]
            },
            {
                "original": [
                    "एस जोगी दी सुनो कहाणी, सोहनी डुब्बी डूंघे पाणी,  ",
                    "फिर रलिआ महींवाल, सारा रख़त लुटा के,  ",
                    "मैं वैसां जोगी दे नाल, मत्थे तिलक लगा के ।"
                ],
                "hindi_gloss": [
                    "एस (इस) जोगी (जोगी) दी (की) सुनो (सुनो) कहाणी (अमर प्रेम-गाथा), सोहनी (सोहणी) डुब्बी (डूब गई) डूंघे (अथाह गहरे) पाणी (चेनाब के पानी में),",
                    "फिर (फिर) रलिआ (उसमें एकाकार हो गया) महींवाल (महीवाल भी), सारा (अपना सारा) रख़त (सामग्री/धन-दौलत) लुटा (न्योछावर कर) के (देने के बाद),",
                    "मैं (मैं तो) वैसां (जाऊँगी) जोगी (उस जोगी) दे (के) नाल (संग), मत्थे (माथे पर) तिलक (तिलक) लगा (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "एस (this) जोगी (yogi's) दी (of) सुनो (hear) कहाणी (the tale), सोहनी (Sohni) डुब्बी (drowned) डूंघे (deep) पाणी (waters),",
                    "फिर (then) रलिआ (merged) महींवाल (Mahiwal), सारा (all) रख़त (wealth/provisions) लुटा (surrendering/spending) के (having),",
                    "मैं (I) वैसां (shall go) जोगी (yogi) दे (with) नाल (along), मत्थे (on forehead) तिलक (tilak) लगा (applying) के (having) ।"
                ],
                "poetic_hindi": [
                    "सुनो कहानी इस जोगी की: सोहणी गहरे जल में डूबी,",
                    "महीवाल भी कूद पड़ा फिर, छोड़ के अपनी हर खूबी !",
                    "धन-दौलत सब त्याग के उसने पाया प्रेमी का विसाल,",
                    "मैं तो चलूँगी उस जोगी के संग, माथे तिलक लगा के लाल !"
                ],
                "poetic_english": [
                    "Hear this Yogi’s tragic saga: Sohni drowned in river deep,",
                    "Mahiwal plunged into the torrent, having cast all wealth to sleep!",
                    "United in the swirling wave where earthly illusions fall:",
                    "I shall go with the Yogi unto the end, with the tilak shining on my brow withal!"
                ]
            },
            {
                "original": [
                    "डांवां डोली लै चल्ले खेड़े, मुढ्ढ कदीमीं दुशमन जेहड़े,  ",
                    "रांझा तां होया नाल, सिर 'ते टमक धरा सजा के,  ",
                    "मैं वैसां जोगी दे नाल, मत्थे तिलक लगा के ।"
                ],
                "hindi_gloss": [
                    "डांवां डोली (डगमगाती डोली) लै (लेकर) चल्ले (चल पड़े) खेड़े (खेड़े लोग), मुढ्ढ (आदि काल से) कदीमीं (पुरातन) दुशमन (शत्रु) जेहड़े (जो हमारे रहे हैं),",
                    "रांझा (परंतु रांझा) तां (तो) होया (हो गया) नाल (साथ-साथ), सिर (अपने सिर) 'ते (पर) टमक (नगाड़ा/रण-ढोल) धरा (रख कर) सजा (बजाते हुए) के (हुए),",
                    "मैं (मैं तो) वैसां (जाऊँगी) जोगी (उस जोगी) दे (के) नाल (संग), मत्थे (माथे पर) तिलक (तिलक) लगा (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "डांवां डोली (wavering palanquin) लै (taking) चल्ले (departed) खेड़े (the Kheras), मुढ्ढ कदीमीं (from ancestral ancient times) दुशमन (enemies) जेहड़े (who were),",
                    "रांझा (Ranjha) तां (verily) होया (went) नाल (alongside), सिर (head) 'ते (upon) टमक (kettledrum) धरा (placing) सजा के (playing/adorning),",
                    "मैं (I) वैसां (shall go) जोगी (yogi) दे (with) नाल (along), मत्थे (on forehead) तिलक (tilak) लगा (applying) के (having) ।"
                ],
                "poetic_hindi": [
                    "डोली ले के खेड़े भागे, जो पुरखों के बैरी थे,",
                    "रांझा सिर पर ढोल सजाए संग-संग चलता द्वारे पे !",
                    "डंके की चोट पे जीत लिया है उसने मेरा रोम-रोम,",
                    "मैं तो चलूँगी उस जोगी के संग, गाती हुई प्रेम का ओम् !"
                ],
                "poetic_english": [
                    "The ancestral foes, the Kheras, bore my trembling palanquin away;",
                    "Yet Ranjha marched beside my carriage, beating the kettledrum bold and gay!",
                    "Proclaiming victory over the world, defying society’s thrall:",
                    "I shall go with the Yogi unto the end, with the tilak shining on my brow withal!"
                ]
            },
            {
                "original": [
                    "जोगी नहीं कोई दूजा साइआ, भर भर प्याला ज़ौक पिलाइआ,  ",
                    "मैं पी पी होई नेहाल, अंग भबूत रमा के,  ",
                    "मैं वैसां जोगी दे नाल, मत्थे तिलक लगा के ।"
                ],
                "hindi_gloss": [
                    "जोगी (यह जोगी) नहीं (कोई) दूजा (अन्य नहीं, साक्षात् मेरा) साइआ (स्वामी/सद्गुरु है), भर (भर) भर (भर कर) प्याला (प्रेम का प्याला) ज़ौक (परमानंद का) पिलाइआ (पिलाया है),",
                    "मैं (मैं तो) पी (पी) पी (पीकर) होई (हो गई हूँ) नेहाल (कृतकृत्य/निहाल), अंग (अंग-प्रत्यंग पर) भबूत (त्याग की भस्म) रमा (रमा) के (कर),",
                    "मैं (मैं तो) वैसां (जाऊँगी) जोगी (उस जोगी) दे (के) नाल (संग), मत्थे (माथे पर) तिलक (तिलक) लगा (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "जोगी (yogi) नहीं (not) कोई दूजा (anyone else) साइआ (master/divine Lord), भर भर (brimful) प्याला (cup) ज़ौक (of ecstasy/divine relish) पिलाइआ (made me drink),",
                    "मैं (I) पी पी (drinking and drinking) होई (became) नेहाल (blessed/liberated), अंग (on limbs) भबूत (sacred ash) रमा के (smearing),",
                    "मैं (I) वैसां (shall go) जोगी (yogi) दे (with) नाल (along), मत्थे (on forehead) तिलक (tilak) लगा (applying) के (having) ।"
                ],
                "poetic_hindi": [
                    "जोगी नहीं वो साक्षात् स्वामी, भर-भर ज़ौक का जाम पिलाया,",
                    "पीते ही मैं निहाल हो गई, तन पर प्रेम-भभूत रमाया !",
                    "मिट गए सारे भेद-भरम अब, मिटा जगत का सारा जाल,",
                    "मैं तो चलूँगी उस जोगी के संग, माथे तिलक लगा के लाल !"
                ],
                "poetic_english": [
                    "This Yogi is none other than my Sovereign Master, Lord of Grace;",
                    "He poured the cup of ecstasy brimming before my weeping face!",
                    "Drunk on that wine, my soul is blessed, in sacred ashes dressed:",
                    "I shall go with the Yogi unto the end, with the tilak shining on my breast!"
                ]
            },
            {
                "original": [
                    "जोगी नाल करेंदे झेड़े, केहे पा बैठे काज़ी झेड़े (भैड़े),  ",
                    "विच कैदों पाई मुकाल, कूड़ा बरा लगा के,  ",
                    "मैं वैसां जोगी दे नाल, मत्थे तिलक लगा के ।"
                ],
                "hindi_gloss": [
                    "जोगी (जोगी) नाल (के साथ) करेंदे (करते हैं) झेड़े (विवाद), केहे (कैसा व्यर्थ बखेड़ा) पा (खड़ा कर) बैठे (बैठे हैं) काज़ी (काजी-मुल्ला) झेड़े/भैड़े (बुरे/कपटी लोग),",
                    "विच (बीच में) कैदों (लंगड़ा कैदों/पाखंडी समाज) पाई (डाली गई) मुकाल (कालिमा/अपयश), कूड़ा (झूठा) बरा/इल्जाम (आरोप) लगा (लगा) के (करके),",
                    "मैं (मैं तो) वैसां (जाऊँगी) जोगी (उस जोगी) दे (के) नाल (संग), मत्थे (माथे पर) तिलक (तिलक) लगा (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "जोगी (yogi) नाल (with) करेंदे (quarrel) झेड़े (disputes), केहे (what kind of) पा बैठे (have brewed) काज़ी (qazis/clerics) भैड़े (wicked/quarrelsome),",
                    "विच (amidst) कैदों (Kaidu/hypocrite) पाई (cast) मुकाल (blackened face/disgrace), कूड़ा (false) बरा (accusation) लगा के (levying),",
                    "मैं (I) वैसां (shall go) जोगी (yogi) दे (with) नाल (along), मत्थे (on forehead) तिलक (tilak) लगा (applying) के (having) ।"
                ],
                "poetic_hindi": [
                    "जोगी से झगड़ा मोल लिया है, काजी-मुल्ला व्यर्थ बिलापें,",
                    "झूठे कैदों का मुँह काला, जो झूठे इल्जामों को नापे !",
                    "सच्चे प्रेम की जीत हुई है, भागा पाखंडी का हाल,",
                    "मैं तो चलूँगी उस जोगी के संग, माथे तिलक लगा के लाल !"
                ],
                "poetic_english": [
                    "The corrupt qazis pick their quarrels with the Yogi in blind disdain;",
                    "While Kaidu’s slanderous mouth was blackened by his own fabrications vain!",
                    "Truth stands victorious over deceit, shattering orthodoxy’s wall:",
                    "I shall go with the Yogi unto the end, with the tilak shining on my brow withal!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा मैं जोगी नाल व्याही, लोकां कमलिआं ख़बर ना काई,  ",
                    "मैं जोगी दा माल, पंजे पीर मना के,  ",
                    "मैं वैसां जोगी दे नाल, मत्थे तिलक लगा के ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ले शाह कहते हैं) मैं (मैं तो) जोगी (उस जोगी) नाल (के साथ) व्याही (सदा के लिए ब्याही गई हूँ), लोकां (संसार के) कमलिआं (नासमझ/मूर्ख लोगों को) ख़बर (इस रहस्य की खबर) ना (नहीं है) काई (कोई भी),",
                    "मैं (मैं तो पूरी तरह) जोगी (उस जोगी) दा (की ही) माल (धरोहर/संपत्ति हूँ), पंजे (पाँचों) पीर (सिद्ध पीरों को) मना (मना) के (कर यह प्रण लिया है),",
                    "मैं (मैं तो) वैसां (जाऊँगी) जोगी (उस जोगी) दे (के) नाल (संग ही), मत्थे (माथे पर) तिलक (तिलक) लगा (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh) मैं (I am) जोगी (yogi) नाल (to) व्याही (wedded), लोकां (people) कमलिआं (foolish) ख़बर (news/inkling) ना काई (none at all),",
                    "मैं (I am) जोगी (yogi's) दा (own) माल (property/treasure), पंजे (five) पीर (Pirs/spiritual masters) मना के (having propitiated),",
                    "मैं (I) वैसां (shall go) जोगी (yogi) दे (with) नाल (along), मत्थे (on forehead) तिलक (tilak) लगा (applying) के (having) ।"
                ],
                "poetic_hindi": [
                    "बुल्ला कहे: मैं जोगी से ब्याही, इस जग को कुछ खबर न भाई,",
                    "पाँचों पीरों को साक्षी कर के, मैं जोगी की जागीर कहलाई !",
                    "अब कौन मुझे रोके जग में, जब साहिब ने ली सुध सम्भाल,",
                    "मैं तो चलूँगी उस जोगी के संग, माथे तिलक लगा के लाल !"
                ],
                "poetic_english": [
                    "Says Bulleh: I am wed to the Yogi, of this the foolish world knows naught;",
                    "Having invoked the Holy Five Pirs, my soul is His own possession bought!",
                    "No power can sever this sacred bond, nor keep my spirit in thrall:",
                    "I shall go with the Yogi unto the end, with the tilak shining on my brow withal!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी बुल्ले शाह के काव्य का एक शिखर है जहां लोक-साहित्य (हीर-रांझा), सूफी रहस्यवाद (वहदत-उल-वुजूद), इस्लामी इतिहास (मूसा, मेअराज, कर्बला) और भारतीय योग परंपरा (तिलक, भभूत, मुंद्रा) एकाकार हो जाते हैं। 'मत्थे तिलक लगा के' कहना उस समय के रूढ़िवादी शरीअती समाज में एक प्रचंड क्रांति थी, जो यह दर्शाती है कि पूर्ण समर्पित प्रेमी मजहबों के बाह्य प्रतीकों से परे उठकर परमात्मा को ही अपना एकमात्र आराध्य स्वीकार करता है। 11वें बंध में कर्बला का उल्लेख सूफी परंपरा में प्रेम की सर्वोच्च कीमत—आत्म-बलिदान—को रेखांकित करता है। यह काफी घोषणा करती है कि जब साधक अपने मुर्शिद (रांझा/जोगी) के चरणों में पांचों पीरों की गवाही के साथ सर्वस्व समर्पित कर देता है, तो संसार के काजी और कैदों (पाखंडी) स्वतः परास्त हो जाते हैं।"
    },
    {
        "id": 97,
        "title": "मन अटकियो शाम सुन्दर सों",
        "title_english": "The Mind is Enamored of Shyam Sundar",
        "historical_context": "यह काफी भारतीय भक्ति आंदोलन और सूफी अद्वैतवाद (वहदत-उल-वुजूद) के विलक्षण संगम का प्रमाण है। बुल्ले शाह परमात्मा को 'शाम सुन्दर' (श्रीकृष्ण) के रूप में संबोधित करते हैं। वे तत्कालीन बाह्य धार्मिक पाखंडों—ब्राह्मणों और शेखों की कर्मकांडी गणनाओं—को नकारते हुए यह प्रतिपादित करते हैं कि प्रेम के नगर में 'राम दुहाई' के प्रभाव से द्वैत समाप्त हो जाता है और 'हम तुम एक ना दूजा काई' का साक्षात अनुभव होता है। अंत में अहंकार का शीश काटकर मुर्शिद के चरणों में समर्पित करने पर सर्वत्र केवल 'हरि' (ईश्वर) ही दिखाई देता है।",
        "meter": "पंजाबी-सधुक्कड़ी मिश्रित काफी (मात्रािक छंद)",
        "raga": "राग काफी / सारंग / बिलावल",
        "theme": "वैष्णव-सूफी समन्वय, अद्वैत (एकत्व), धार्मिक आडंबरों का खंडन, अहंकार-समर्पण",
        "stanzas": [
            {
                "original": [
                    "कहूं वेखूं बाहमन कहूं सेखा,  ",
                    "आप आप करन सभ लेखा,  ",
                    "क्या क्या खोलिआ हुनर सों ।  ",
                    "मन अटकियो शाम सुन्दर सों ।"
                ],
                "hindi_gloss": [
                    "कहूं (कहीं) वेखूं (मैं देखता हूँ) बाहमन (ब्राह्मणों को) कहूं (तो कहीं) सेखा (शेखों/मुल्लाओं को),",
                    "आप (अपने) आप (आप ही) करन (कर रहे हैं) सभ (सब अपना-अपना) लेखा (तर्क-वितर्क और हिसाब-किताब),",
                    "क्या (कैसे-कैसे) क्या (क्या) खोलिआ (उघाड़ रखे हैं उन्होंने) हुनर (पाखंड और चतुराई के कला-कौशल) सों (के साथ) ।",
                    "मन (मेरा यह मन तो) अटकियो (अटक/मोहित हो गया है) शाम (श्याम) सुन्दर (सुन्दर परब्रह्म) सों (के साथ) ।"
                ],
                "english_gloss": [
                    "कहूं (somewhere) वेखूं (I see) बाहमन (Brahmins) कहूं (somewhere) सेखा (Sheikhs/Muslim clerics),",
                    "आप आप (each by themselves) करन (calculate) सभ (all) लेखा (accounts/disputes),",
                    "क्या क्या (what manifold) खोलिआ (have displayed) हुनर (clever artifices/tricks) सों (with) ।",
                    "मन (mind/soul) अटकियो (is captivated/enchained) शाम सुन्दर (Shyam Sundar/the Dark Beloved) सों (with) ।"
                ],
                "poetic_hindi": [
                    "कहीं पे ब्राह्मण, कहीं पे शेख, हिसाब अपना-अपना जोड़ें,",
                    "कैसे-कैसे हुनर उघाड़ें, तर्कों के वो जाल मरोड़ें ।",
                    "इन झगड़ों से पार हुआ मैं, छोड़ के झूठे ढोंग-प्रपंच,",
                    "मेरा मन अटका श्याम सुन्दर से, छूटे सारे द्वैत के मंच !"
                ],
                "poetic_english": [
                    "Here stands the Brahmin, there the Sheikh, each tallying up his rigid score;",
                    "Displaying crafts of intellect, defending dogmas at the door.",
                    "Far from their disputes I have flown, beyond their theoretical art:",
                    "Enamored of Shyam Sundar now, my soul has given Him its heart!"
                ]
            },
            {
                "original": [
                    "सूझ पड़ी तब राम दुहाई,  ",
                    "हम तुम एक ना दूजा काई,  ",
                    "इस प्रेम नगर के घर सों ।  ",
                    "मन अटकियो शाम सुन्दर सों ।"
                ],
                "hindi_gloss": [
                    "सूझ (सच्ची समझ/ज्ञान) पड़ी (प्रकट हुई) तब (तब जब) राम (परम प्रभु राम की) दुहाई (दुहाई/गंभीर पुकार सुनी),",
                    "हम (हम) तुम (और तुम) एक (सर्वथा एक ही हैं) ना (नहीं है) दूजा (कोई दूसरा) काई (कोई भी),",
                    "इस (इस पावन) प्रेम (प्रेम) नगर (के नगर) के (के) घर (आंतरिक भवन) सों (से) ।",
                    "मन (मेरा मन) अटकियो (अटक गया है) शाम (श्याम) सुन्दर (सुन्दर के चरणों) सों (से) ।"
                ],
                "english_gloss": [
                    "सूझ पड़ी (comprehension dawned) तब (then when) राम (of Ram/Divine) दुहाई (sovereign proclamation/invocation),",
                    "हम (I) तुम (Thou) एक (are one) ना (not) दूजा (second) काई (anyone),",
                    "इस (this) प्रेम (of divine love) नगर (city) के (of) घर (mansion) सों (from/within) ।",
                    "मन (mind) अटकियो (is captivated) शाम सुन्दर (Shyam Sundar) सों (with) ।"
                ],
                "poetic_hindi": [
                    "राम-दुहाई की जब समझी, खुल गया भेद अद्वैत का सार,",
                    "हम-तुम एक, न दूजा कोई, इस पावन प्रेम-नगर के द्वार !",
                    "सारे परदे दूर हुए जब, मिट गया भ्रांति का घोर प्रपंच,",
                    "मेरा मन अटका श्याम सुन्दर से, छूटे सारे द्वैत के मंच !"
                ],
                "poetic_english": [
                    "When Ram’s divine decree awoke, the truth of oneness shone ablaze:",
                    "'Thou and I are one, no second exists', within Love’s citadel of grace!",
                    "All veil of separateness dissolved, no border partitions the divine:",
                    "Enamored of Shyam Sundar now, His eternal light is wholly mine!"
                ]
            },
            {
                "original": [
                    "पंडित कौन कित लिख सुणाए,  ",
                    "ना कहीं आए ना कहीं जाए,  ",
                    "जैसे गुर का कंगन कर सों ।  ",
                    "मन अटकियो शाम सुन्दर सों ।"
                ],
                "hindi_gloss": [
                    "पंडित (पंडित) कौन (कौन-सी) कित (किताबें/शास्त्र) लिख (लिखकर) सुणाए (सुनाता है),",
                    "ना (परमात्मा न तो) कहीं (कहीं से) आए (आता है) ना (और न ही) कहीं (कहीं) जाए (जाता है),",
                    "जैसे (जैसे) गुर (गुरु का दिया हुआ) कंगन (कंगन शोभित होता है) कर (हाथ) सों (के साथ अभिन्न होकर) ।",
                    "मन (मेरा मन) अटकियो (मुग्ध हो गया है) शाम (श्याम) सुन्दर (सुन्दर) सों (से) ।"
                ],
                "english_gloss": [
                    "पंडित (the scholar/pandit) कौन (which) कित (scriptures/books) लिख (writing) सुणाए (recites),",
                    "ना (neither) कहीं (anywhere) आए (comes) ना (nor) कहीं (anywhere) जाए (departs),",
                    "जैसे (just as) गुर (Guru's) कंगन (bracelet) कर (hand) सों (with, inseparably),",
                    "मन (mind) अटकियो (is hooked) शाम सुन्दर (Shyam Sundar) सों (with) ।"
                ],
                "poetic_hindi": [
                    "पंडित कौन किताबें बांचे, व्यर्थ ही पोथी-पन्ने खोले?",
                    "आता-जाता कहीं नहीं वो, घट-घट में अविनाशी बोले !",
                    "जैसे हाथ से कंगन साजे, वैसे रब की महिमा सार,",
                    "मेरा मन अटका श्याम सुन्दर से, देख लिया जग का करतार !"
                ],
                "poetic_english": [
                    "What scriptures does the pandit read, and write his learned scrolls in vain?",
                    "The Lord neither arrives nor goes, omnipresent in joy and pain!",
                    "As a golden bangle fits the wrist, indivisible and complete:",
                    "Enamored of Shyam Sundar now, my heart is anchored at His feet!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु दी पैरीं पड़ीए,  ",
                    "सीस काट कर आगे धरीए,  ",
                    "हुन मैं हर देखा हर हर सों ।  ",
                    "मन अटकियो शाम सुन्दर सों ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ले शाह कहते हैं) शहु (उस परम प्रियतम/सद्गुरु) दी (के) पैरीं (चरणों में) पड़ीए (समर्पित हो जाइए),",
                    "सीस (अपने अहंकार रूपी सिर को) काट (काट) कर (करके) आगे (उसके आगे) धरीए (भेंट रख दीजिए),",
                    "हुन (अब तो) मैं (मैं) हर (प्रत्येक रूप में) देखा (देख रहा हूँ) हर (हरि/परमात्मा को ही) हर (प्रत्येक) सों (से) ।",
                    "मन (मेरा मन) अटकियो (मुग्ध हो गया है) शाम (श्याम) सुन्दर (सुन्दर) सों (से) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh) शहु (Beloved Lord) दी (of) पैरीं (at feet) पड़ीए (let us fall),",
                    "सीस (head of ego) काट कर (severing) आगे (before Him) धरीए (lay/offer),",
                    "हुन (now) मैं (I) हर (Hari/Lord) देखा (behold) हर (in everyone) हर सों (through all beings) ।",
                    "मन (mind) अटकियो (is captivated) शाम सुन्दर (Shyam Sundar) सों (with) ।"
                ],
                "poetic_hindi": [
                    "बुल्ला कहे: साहिब के चरणों में शीश काट कर धर दीजिए,",
                    "अहंकार की बलि देकर के, प्रेम-सुधा रस पी लीजिए !",
                    "अब तो कण-कण में, हर जन में दिखता केवल हरि का रूप,",
                    "मेरा मन अटका श्याम सुन्दर से, छा गई आनंद की धूप !"
                ],
                "poetic_english": [
                    "Says Bulleh: Fall at the Master’s feet, slice off the head of arrogant pride;",
                    "Surrender selfhood at His throne, and cast all mortal claims aside!",
                    "Now in every face I see the Lord, through every form does Hari shine:",
                    "Enamored of Shyam Sundar now, my soul is merged in love divine!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी बुल्ले शाह की अद्वैतवादी दृष्टि और धार्मिक सहिष्णुता का सर्वोच्च उदाहरण है। वे ईश्वर को 'श्याम सुन्दर' कहकर पुकारते हैं, जो दिखाता है कि एक सूफी के लिए अल्लाह, राम, कृष्ण या हरि में कोई तात्विक भेद नहीं है। 'हम तुम एक ना दूजा काई' सीधे तौर पर उपनिषदों के 'अहं ब्रह्मास्मि' और सूफी मंसूर हल्लाज के 'अनलहक' का उद्घोष है। ज्ञानियों और पंडितों की पोथियों की सीमाओं को रेखांकित करते हुए बुल्ला स्पष्ट करते हैं कि ईश्वर कोई बाहर से आने-जाने वाला तत्व नहीं है, वह आत्मा से वैसे ही अभिन्न है जैसे हाथ से कंगन। अंतिम पद में 'सीस काट कर आगे धरीए' सूफी फना (अहंकार-शून्यता) की शर्त है, जिसके पूरे होते ही साधक को सर्वत्र केवल 'हरि' (परमात्मा) ही दृष्टिगोचर होता है।"
    },
    {
        "id": 98,
        "title": "माए ! ना मुड़दा इश्क दीवाना, शहु नाल परीतां ला के",
        "title_english": "O Mother! This Mad Love Will Not Relent, Having Bound Love with the Sovereign",
        "historical_context": "यह 10 बंधों की अत्यंत ओजस्वी और क्रांतिकारी काफी है। बुल्ले शाह इसमें पारंपरिक शरिया (सामाजिक-धार्मिक नियमों) और हकीकी इश्क (दिव्य प्रेम) के संघर्ष को जुए/चौपड़ की बाजी के रूप में चित्रित करते हैं। साधक शरिया के बाह्य आवरणों को तोड़कर प्रेम की बाजी जीत लेता है। 'वहदत' (एकत्व) की अवस्था में पहुँचकर मोमिन और काफिर का भेद स्वतः मिट जाता है। इस काफी में 'मारिआ खाविन्द' (अपने पति अर्थात् नफ़्स/अहंकार को जहर देकर मारना) और 'धूनी शिरक जला के' (द्वैतभाव को भस्म करना) जैसे विस्मयकारी सूफी रूपक प्रयुक्त हुए हैं।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: माए ना मुड़दा इश्क दीवाना)",
        "raga": "राग भैरवी / काफी",
        "theme": "नफ़्स (अहंकार) का विनाश, वहदत में मोमिन-काफिर का विलोप, शरिया पर प्रेम की विजय, विसाल (परम मिलन)",
        "stanzas": [
            {
                "original": [
                    "माए ! ना मुड़दा इश्क दीवाना, शहु नाल परीतां ला के ।  ",
                    "इश्क शर्हा दी लग्ग गई बाज़ी, खेडां मैं दायो लगा के ।"
                ],
                "hindi_gloss": [
                    "माए (हे माँ), ना (नहीं) मुड़दा (पीछे मुड़ता/लौटता) इश्क (यह) दीवाना (दीवाना इलाही प्रेम), शहु (अपने परम प्रियतम/सद्गुरु) नाल (के साथ) परीतां (सच्ची प्रीत) ला (लगा) के (लेने के बाद) ।",
                    "इश्क (इश्क) शर्हा (और रूढ़िवादी शरिया) दी (की) लग्ग (लग) गई (चुकी है) बाज़ी (चौपड़ की बाजी/दांव), खेडां (खेल रही हूँ) मैं (मैं) दायो (सर्वस्व दांव पर) लगा (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "माए (O mother), ना (not) मुड़दा (turns back) इश्क दीवाना (crazed divine love), शहु (the Sovereign Lord) नाल (with) परीतां (love) ला के (having bound) ।",
                    "इश्क (Love) शर्हा (dogmatic law/Shariah) दी (of) लग्ग गई (is staked) बाज़ी (the game/wager), खेडां (play) मैं (I) दायो लगा के (putting all on the line) ।"
                ],
                "poetic_hindi": [
                    "ओ माँ ! यह पागल इश्क कभी मुड़ कर न पीछे जाएगा,",
                    "जिसने प्रियतम से प्रीत लगाई, वो जीवन न्योछावर पाएगा !",
                    "इश्क और शरिया की बाज़ी लगी है, दांव पे मैंने जान लगाई,",
                    "सच्चे साहिब के चरणों में, अपनी हर इक सुध बिसराई !"
                ],
                "poetic_english": [
                    "O mother! This frenzied love will never turn back from its goal;",
                    "Having pledged eternal devotion to the Sovereign of my soul!",
                    "Love and the formal Law have wagered in a high and fateful game:",
                    "I play with my very life at stake, engulfed in Passion's flame!"
                ]
            },
            {
                "original": [
                    "मारन बोली ते बोली ना बोलां, सुणां ना कन्न ला के ।  ",
                    "वेहड़े विच शैतान नचेंदा, उस नूं रक्ख समझा के ।"
                ],
                "hindi_gloss": [
                    "मारन (लोग मारते हैं) बोली (व्यंग्य-बाण/ताने) ते (परंतु) बोली (मैं उलाहने भरी बोली) ना (नहीं) बोलां (बोलती), सुणां (सुनती भी) ना (नहीं) कन्न (कान) ला (लगा) के (करके),",
                    "वेहड़े (आँगन) विच (में) शैतान (संदेह और अहंकार का शैतान) नचेंदा (नाच रहा है), उस (उस अपने शैतानी मन) नूं (को) रक्ख (रख तू) समझा (समझा) के (कर) ।"
                ],
                "english_gloss": [
                    "मारन (they cast) बोली (taunts/insults) ते (yet) बोली (taunt) ना बोलां (I speak not), सुणां ना (nor hear) कन्न ला के (lending an ear),",
                    "वेहड़े विच (in the courtyard) शैतान (Satan/ego-devil) नचेंदा (dances), उस नूं (him) रक्ख (keep) समझा के (disciplined/counseled) ।"
                ],
                "poetic_hindi": [
                    "लोग ताने कसते हैं मुझ पर, पर मैं पलट के बोल न बोलूँ,",
                    "कान लगाकर सुनूँ न उनकी, प्रेम का अमृत ही मन में घोलूँ ।",
                    "तेरे ही आँगन में शैतान नाचता, उसे ज़रा समझा ले माँ री,",
                    "मैं तो प्रेम-दीवानी होकर, दुनिया के सब झगड़े हारी !"
                ],
                "poetic_english": [
                    "They fling their barbs and bitter taunts, yet I return no angry word;",
                    "I lend no ear to malicious tongues, attentive only to my Lord.",
                    "The devil of doubts dances in your yard—go discipline his pride, O mother!",
                    "For I have surrendered to holy love, and know no earthly other!"
                ]
            },
            {
                "original": [
                    "तोड़ शर्हा नूं जित्त लई बाज़ी, फिरदी नक्क वढा के ।  ",
                    "मैं वे अंजानी खेड विगुच्चियां, खेडां मैं आके बाके ।"
                ],
                "hindi_gloss": [
                    "तोड़ (तोड़कर) शर्हा (रूढ़िवादी शरिया के बंधनों) नूं (को) जित्त (जीत) लई (ली है मैंने) बाज़ी (प्रेम की बाजी), फिरदी (फिरती है शरिया) नक्क (नाक) वढा (कटवा) के (करके अपमानित),",
                    "मैं (मैं) वे (तो) अंजानी (भोली-अंजान) खेड (खेल में) विगुच्चियां (उलझी थी पहले), खेडां (अब खेलती हूँ) मैं (मैं) आके (प्रौढ़/कुशल होकर) बाके (निडर और बाँकी होकर) ।"
                ],
                "english_gloss": [
                    "तोड़ (breaking) शर्हा नूं (the outer Law) जित्त लई (won) बाज़ी (the game), फिरदी (wanders) नक्क वढा के (with severed nose/disgraced),",
                    "मैं वे (I indeed) अंजानी (ignorant) खेड विगुच्चियां (was lost in play), खेडां मैं (now I play) आके बाके (mature, fearless, and bold) ।"
                ],
                "poetic_hindi": [
                    "शरिया के बंधनों को तोड़ के मैंने प्रेम की बाज़ी जीती,",
                    "रूढ़िवादी नाक कटा कर भागे, बदली जग की रीति !",
                    "अंजानी थी जब खेल न समझा, अब तो बाँकी खेल रचाई,",
                    "दांव पे दांव लगा कर मैंने अपनी मंज़िल पाई !"
                ],
                "poetic_english": [
                    "Shattering the chains of ritual Law, I won the contested game;",
                    "While dogmatic orthodoxy roams with severed nose in shame!",
                    "Once I was naive and stumbled in play, but now I play fearless and bold:",
                    "Checkmating the world with sovereign love, more precious than rubies and gold!"
                ]
            },
            {
                "original": [
                    "इह खेडां हुन लगदियां झेडां, घर पिया दे आ के ।  ",
                    "सईआं नाल मैं पावां गिद्धा, दिलबर लुक्क लुक्क झाके ।"
                ],
                "hindi_gloss": [
                    "इह (ये सांसारिक) खेडां (खेल) हुन (अब) लगदियां (लगते हैं मुझे) झेडां (तुच्छ झगड़े/झंझट), घर (भवन में) पिया (प्रियतम) दे (के) आ (आ) के (जाने के बाद),",
                    "सईआं (अपनी सखियों) नाल (के साथ) मैं (मैं) पावां (डालती हूँ) गिद्धा (आनंद का गिद्धा/नृत्य), दिलबर (मेरा प्यारा प्रियतम) लुक्क (छिप) लुक्क (छिपकर) झाके (प्रेम-दृष्टि से मुझे निहारता है) ।"
                ],
                "english_gloss": [
                    "इह खेडां (these worldly plays) हुन (now) लगदियां (appear like) झेडां (trivial disputes), घर पिया दे (in Beloved's abode) आ के (having entered),",
                    "सईआं नाल (with maidens/companions) मैं पावां (I dance) गिद्धा (joyous Giddha), दिलबर (the Beloved) लुक्क लुक्क (in hiding) झाके (peeps with loving glances) ।"
                ],
                "poetic_hindi": [
                    "प्रियतम के घर आकर मुझको सांसारिक सब खेल लगे झंझट भारी,",
                    "सखियों के संग गिद्धा डालूँ, नाचे मेरी सुरति सारी !",
                    "छिप-छिप कर दीदार कराए मेरा प्यारा दिलबर यार,",
                    "उसकी इक मीठी चितवन पे न्योछावर संसार !"
                ],
                "poetic_english": [
                    "Having entered my Beloved’s abode, worldly disputes seem petty and vain;",
                    "I dance the Giddha with sister souls, free from all sorrow and pain!",
                    "My Sweetheart watches from behind the veil with fond and radiant gaze,",
                    "Enfolding my heart in secret joy, lost in a mystical maze!"
                ]
            },
            {
                "original": [
                    "पुच्छो नी इह क्यों शरमांदा, जांदा ना भेत बता के ।  ",
                    "काफर काफर आखन तैनूं, सारे लोक सुना के ।"
                ],
                "hindi_gloss": [
                    "पुच्छो (अरी सखियो, उससे पूछो) नी (तो), इह (यह प्रियतम) क्यों (क्यों) शरमांदा (लजाता है), जांदा (जाता) ना (नहीं) भेत (अपना रहस्य) बता (खोल) के (कर),",
                    "काफर (काफिर) काफर (काफिर/नास्तिक) आखन (कहते हैं) तैनूं (तुझको), सारे (सारे) लोक (संसार के लोग) सुना (सुना) के (करके) ।"
                ],
                "english_gloss": [
                    "पुच्छो नी (ask Him, O sisters) इह क्यों शरमांदा (why does He feel shy), जांदा ना (departs without) भेत बता के (disclosing His mystery),",
                    "काफर काफर (infidel, infidel!) आखन तैनूं (call thee) सारे लोक (all the folk) सुना के (declaring aloud) ।"
                ],
                "poetic_hindi": [
                    "सखियो पूछो उससे ज़रा, वो क्यों इतना शरमाता है?",
                    "बिना बताए अपना भेद, नैन चुरा कर जाता है !",
                    "लोग तुझे काफ़िर कहते हैं, दुनिया शोर मचाए,",
                    "पर मुझको तो तेरे मुखड़े में साक्षात् रब नज़र आए !"
                ],
                "poetic_english": [
                    "Ask Him, O sisters, why does He hide and feign such modest grace?",
                    "Departing without revealing His secret, turning away His face?",
                    "The townsfolk cry 'Kafir! Kafir!' in chorus to brand my name with shame,",
                    "Yet in that heresy I behold God’s uncorrupted flame!"
                ]
            },
            {
                "original": [
                    "मोमन काफर मैनूं दोवें ना दिसदे, वहदत दे विच जा के ।  ",
                    "चोली चुन्नी ते फुक्या झग्गा, धूनी शिरक जला के ।"
                ],
                "hindi_gloss": [
                    "मोमन (मुस्लिम/मोमिन) काफर (और काफिर) मैनूं (मुझे) दोवें (दोनों ही) ना (नहीं) दिसदे (दिखाई देते), वहदत (परम अद्वैत/एकेश्वरवाद) दे (के) विच (भीतर) जा (प्रविष्ट हो) के (जाने पर),",
                    "चोली (चोली) चुन्नी (दुपट्टा) ते (और) फुक्या (जला दिया है मैंने अपना) झग्गा (कुर्ता/सांसारिक परिधान), धूनी (अग्नि में) शिरक (द्वैतभाव/बहुदेववाद की कुरीति को) जला (भस्म कर) के (देने के बाद) ।"
                ],
                "english_gloss": [
                    "मोमन (believer/Momin) काफर (infidel/Kafir) मैनूं (unto me) दोवें (both) ना दिसदे (are visible neither), वहदत दे विच (into the oceanic Oneness) जा के (having entered),",
                    "चोली (bodice) चुन्नी (veil) ते फुक्या (and burnt) झग्गा (robe/outer cloak), धूनी (sacred blaze) शिरक (idolatry of duality/shirk) जला के (having immolated) ।"
                ],
                "poetic_hindi": [
                    "मोमिन-काफिर दोनों मिटे जब वहदत के दरिया में उतरा,",
                    "चोली, चुनरी, कुर्ती फूँकी, द्वैत का हर इक तिनका बिखरा !",
                    "शिरक-अविद्या की भट्टी में भस्म किया सब झूठा मान,",
                    "एक नूर से सब जग उपजा, मिट गया दो होने का गुमान !"
                ],
                "poetic_english": [
                    "Neither believer nor infidel remains when merged in the Ocean of One;",
                    "I burnt the bodice, the veil, the cloak, my worldly disguises are done!",
                    "Kindling the blaze that consumed all shirk, all illusion of duality's art:",
                    "Nothing exists but the Single Light, throbbing within my heart!"
                ]
            },
            {
                "original": [
                    "वारिआ कुफर वड्डा मैं दिल थीं, तली ते सीस टिका के ।  ",
                    "मैं वडभागी मारिआ खाविन्द, हत्थीं ज़हर पिला के ।"
                ],
                "hindi_gloss": [
                    "वारिआ (न्योछावर कर दिया) कुफर (कुफ्र/अहंकार) वड्डा (बड़ा भारी) मैं (मैंने) दिल (अपने हृदय) थीं (से), तली (अपनी हथेली) ते (पर) सीस (सिर) टिका (रख) के (करके),",
                    "मैं (मैं ऐसी) वडभागी (परम भाग्यशाली हूँ जिसने) मारिआ (मार डाला है अपने) खाविन्द (पति अर्थात् नफ़्स/अहंकार को), हत्थीं (अपने ही हाथों से) ज़हर (त्याग का विष) पिला (पिला) के (करके) ।"
                ],
                "english_gloss": [
                    "वारिआ (renounced/cast away) कुफर वड्डा (the great infidelity of ego) मैं दिल थीं (from my heart), तली ते (upon palm) सीस (severed head) टिका के (resting),",
                    "मैं वडभागी (I, most blessed one) मारिआ (slew/killed) खाविन्द (husband, i.e., the carnal ego/Nafs), हत्थीं (with own hands) ज़हर (poison) पिला के (administering) ।"
                ],
                "poetic_hindi": [
                    "हथेली पे रख शीश न्योछावर, दिल से कुफ्र का पर्दा तारा,",
                    "बड़ी भागवान हूँ मैं जिसने अपने ही पति (अहंकार) को मारा !",
                    "हाथों से विष का घूँट पिलाकर नफ़्स का फंदा काट दिया,",
                    "सच्चे साहिब के चरणों में तन-मन-जीवन बाँट दिया !"
                ],
                "poetic_english": [
                    "Placing my severed head on my palm, I purged my heart of ego’s blight;",
                    "Blessed am I, who slew my 'husband'—the carnal self that obscured the light!",
                    "I served him poison with my own hands to murder the tyrant within:",
                    "Now freed from the grip of mortal lust, my heavenly vows begin!"
                ]
            },
            {
                "original": [
                    "वसल करां मैं नाल सज्जन दे, शरम हया गवा के ।  ",
                    "विच चमन मैं पलंघ विछाइआ, यार सुत्ती गल ला के ।"
                ],
                "hindi_gloss": [
                    "वसल (परम मिलन) करां (करती हूँ) मैं (मैं) नाल (संग) सज्जन (अपने प्यारे प्रियतम) दे (के), शरम (संसार की लज्जा) हया (और संकोच को) गवा (मिटा) के (करके),",
                    "विच (भीतर) चमन (हृदय-उद्यान के) मैं (मैंने) पलंघ (प्रेम की सेज) विछाइआ (बिछा ली है), यार (और प्रियतम को) सुत्ती (सो रही हूँ) गल (गले से) ला (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "वसल (divine union) करां मैं (I celebrate) नाल सज्जन दे (with the Beloved), शरम हया (all earthly shame and restraint) गवा के (having cast away),",
                    "विच चमन (in the garden of heart) मैं पलंघ विछाइआ (I spread the couch), यार (Beloved) सुत्ती (I sleep) गल ला के (embracing to my bosom) ।"
                ],
                "poetic_hindi": [
                    "लोक-लाज का पर्दा खोकर, साहिब संग विसाल किया,",
                    "हृदय-चमन में सेज बिछाकर, यार को उर से लगा लिया !",
                    "अब न कोई दूरी बाकी, न कोई पर्दा दरमियान,",
                    "एक हुए हम दोनों मिलकर, धन्य हुआ मेरा जहान !"
                ],
                "poetic_english": [
                    "Casting aside all earthly shame, I celebrate communion divine;",
                    "Spreading the bridal couch in the garden, His arms around me entwine!",
                    "Embracing the Beloved close to my breast, all distance fades to nought:",
                    "In the deep sanctuary of ecstasy, the treasure of life is bought!"
                ]
            },
            {
                "original": [
                    "सिर देही नाल मिल गई सिर देही, बुल्ल्हा शहु नूं पा के ।  ",
                    "माए ! ना मुड़दा इश्क दीवाना, शहु नाल परीतां ला के ।"
                ],
                "hindi_gloss": [
                    "सिर देही (मेरी आत्मा की देह) नाल (के साथ) मिल (एकाकार हो) गई (गई है) सिर देही (परमेश्वर की ज्योतिर्मय देह), बुल्ल्हा (बुल्ले शाह कहते हैं) शहु (सच्चे प्रियतम) नूं (को) पा (प्राप्त कर) के (लेने के बाद) ।",
                    "माए (हे माँ), ना (नहीं) मुड़दा (पीछे हटता) इश्क (यह) दीवाना (दीवाना प्रेम), शहु (परमेश्वर) नाल (के साथ) परीतां (प्रीत) ला (लगा) के (कर) ।"
                ],
                "english_gloss": [
                    "सिर देही (my body and soul) नाल मिल गई (merged into oneness) सिर देही (His divine form/essence), बुल्ल्हा (Bulleh) शहु नूं पा के (having attained the Sovereign Lord) ।",
                    "माए (O mother), ना मुड़दा (turns not back) इश्क दीवाना (this mad love), शहु नाल (with the Lord) परीतां ला के (having bound love) ।"
                ],
                "poetic_hindi": [
                    "देह से देह और आत्मा से आत्मा मिलकर हुई एकाकार,",
                    "बुल्ले शाह ने साहिब पाकर पा लिया जीवन का सार !",
                    "ओ माँ ! यह पागल इश्क कभी मुड़ कर न पीछे जाएगा,",
                    "जिसने प्रियतम से प्रीत लगाई, वो अमर पदवी पाएगा !"
                ],
                "poetic_english": [
                    "Body with body and spirit with spirit have fused into single grace;",
                    "Bulleh has found his Sovereign King, gazing upon His face!",
                    "O mother! This frenzied love will never turn back from its goal:",
                    "Having pledged eternal devotion to the Sovereign of my soul!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी सूफी साहित्य की सबसे साहसिक और रूपकात्मक रचनाओं में गिनी जाती है। इसमें 'मारिआ खाविन्द' (पति को जहर देकर मारना) एक अत्यंत गूढ़ सूफी रूपक है। सूफी शब्दावली में सांसारिक पति 'नफ़्स' (इंद्रियलोलुप निम्न अहं) का प्रतीक है जो जीवात्मा को वासना और दुनियादारी में बांधे रखता है। जब साधिका साधना और वैराग्य के विष से इस नफ़्स की हत्या कर देती है, तभी वह अपने वास्तविक दिव्य पति (शाह इनायत/परमात्मा) के साथ 'वसल' (शाश्वत मिलन) कर सकती है। इसी प्रकार 'धूनी शिरक जला के' और 'वहदत दे विच जा के' यह दर्शाते हैं कि पूर्ण अद्वैत में हिंदू-मुस्लिम या मोमिन-काफिर की कृत्रिम विभाजक रेखाएं भस्म हो जाती हैं। 'सिर देही नाल मिल गई सिर देही' जीवात्मा और परमात्मा के उस तादात्म्य की पराकाष्ठा है जिसे उपनिषदों में 'तत्वमसि' और सूफियों में 'अनलहक' कहा गया है।"
    },
    {
        "id": 99,
        "title": "मेरा रांझा हुन कोई होर",
        "title_english": "My Ranjha is Now Someone Else Entirely",
        "historical_context": "यह काफी बुल्ले शाह के फना और बका के अनुभव का सार है। रांझा अब तख्त हजारे का ग्वाला या ऐतिहासिक चरित्र नहीं रहा, बल्कि वह 'तख्त मुनव्वर' (प्रकाशमय दिव्य लोक) और 'तख्त लाहौर' (मुर्शिद हज़रत शाह इनायत का आसन) की सार्वभौमिक चेतना बन चुका है। साधक उद्घोष करता है कि प्रेम में अहंकार के नष्ट हो जाने के बाद आत्मा अमर हो जाती है: 'असीं मरना नाहीं, कबर पाय कोई होर' (हम कभी नहीं मरेंगे, कब्र में तो कोई और भौतिक शरीर जाएगा), जो कबीर के 'हम ना मरब मरिहै संसारा' के अद्वैत दर्शन से सीधा साम्य रखता है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: मेरा रांझा हुन कोई होर)",
        "raga": "राग काफी / धनसरी",
        "theme": "आत्म-अमरत्व, बका-बिल्लाह, रांझा का सार्वभौम स्वरूप, मायावी देह से मुक्ति",
        "stanzas": [
            {
                "original": [
                    "मेरा रांझा हुन कोई होर ।",
                    "तखत मुनव्वर बांगां मिलियां,  ",
                    "तां सुणियां तखत लाहौर ।"
                ],
                "hindi_gloss": [
                    "मेरा (मेरा) रांझा (रांझा/परम प्रियतम) हुन (अब) कोई (कोई) होर (और ही अलौकिक सत्ता बन गया है) ।",
                    "तखत (सिंहासन) मुनव्वर (परम प्रकाशमान अर्श/स्वर्ग से) बांगां (दिव्य पुकार/अजान) मिलियां (गूँज उठीं),",
                    "तां (तो वे पुकारें) सुणियां (सुनाई दीं) तखत (मुर्शिद के तख्त) लाहौर (लाहौर के दरबार में) ।"
                ],
                "english_gloss": [
                    "मेरा (my) रांझा (Ranjha/Divine Beloved) हुन (now) कोई होर (is someone else entirely) ।",
                    "तखत मुनव्वर (from the Throne of Luminous Light) बांगां (the celestial calls) मिलियां (resounded),",
                    "तां (then) सुणियां (were heard at) तखत लाहौर (the Throne of Lahore) ।"
                ],
                "poetic_hindi": [
                    "मेरा रांझा अब कोई और ही हुआ, रूप उसका अनूप,",
                    "अर्श-ए-मुनव्वर से उठी पुकारें, लाहौर तख्त पे खिली दिव्य धूप !"
                ],
                "poetic_english": [
                    "My Ranjha has become someone else entirely, beyond all mortal shore;",
                    "The calls resounded from the Luminous Throne, and were heard at the Throne of Lahore!"
                ]
            },
            {
                "original": [
                    "इश्क मारे ऐवें फिरदे,  ",
                    "जिवें जंगल विच ढोर ।"
                ],
                "hindi_gloss": [
                    "इश्क (सच्चे इश्क की समझ से विहीन) मारे (अज्ञान में भटके हुए लोग) ऐवें (व्यर्थ ही) फिरदे (भटकते फिरते हैं),",
                    "जिवें (जैसे) जंगल (जंगल) विच (में) ढोर (पशु/मवेशी भटकते हैं) ।"
                ],
                "english_gloss": [
                    "इश्क मारे (bereft of true love/smitten in ignorance) ऐवें फिरदे (wander aimlessly),",
                    "जिवें (just as) जंगल विच (in the wild forest) ढोर (dumb cattle wander) ।"
                ],
                "poetic_hindi": [
                    "सच्चे प्रेम की सुध नहीं जिनको, व्यर्थ भटकते चारों ओर,",
                    "जैसे बीहड़ जंगल के अंदर भटके कोई मूक ढोर !"
                ],
                "poetic_english": [
                    "Those who know not the secret of Love wander aimless in despair,",
                    "Like bewildered beasts that roam untamed through the forest's tangled snare!"
                ]
            },
            {
                "original": [
                    "रांझा तखत हज़ारे दा साईं,  ",
                    "हुन ओथों होया चोर ।"
                ],
                "hindi_gloss": [
                    "रांझा (जो रांझा कभी) तखत हज़ारे (तख्त हजारे) दा (का) साईं (स्वामी/राजकुमार था),",
                    "हुन (अब) ओथों (वहाँ से) होया (हो गया है) चोर (छिपकर भागने वाला/चोर) ।"
                ],
                "english_gloss": [
                    "रांझा (Ranjha) तखत हज़ारे दा (of Takht Hazara) साईं (was master/lord),",
                    "हुन (now) ओथों (from there) होया चोर (has slipped away like a thief) ।"
                ],
                "poetic_hindi": [
                    "तख्त हजारे का जो था साहिब, वहाँ से चोर बन निकला यार,",
                    "छोड़ के दुनियावी शान-ओ-शौकत, दिल चुराने आया इस बार !"
                ],
                "poetic_english": [
                    "He who once was the sovereign prince of Takht Hazara's golden plain,",
                    "Has slipped away like a subtle thief to steal my heart through joy and pain!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शाह असीं मरना नाहीं,  ",
                    "कबर पाय कोई होर ।  ",
                    "मेरा रांझा हुन कोई होर ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा शाह (बुल्ले शाह कहते हैं) असीं (हम) मरना (कभी मरने वाले) नाहीं (नहीं हैं),",
                    "कबर (कब्र में) पाय (दफनाया जाएगा) कोई (कोई) होर (अन्य ही भौतिक शरीर) ।",
                    "मेरा (मेरा) रांझा (रांझा) हुन (अब) कोई (कोई) होर (और ही परम प्रकाश बन गया है) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा शाह (Bulleh Shah) असीं (we) मरना नाहीं (shall never die),",
                    "कबर (in the grave) पाय (shall be laid) कोई होर (someone else/the outer clay) ।",
                    "मेरा रांझा हुन कोई होर (My Ranjha is now someone else entirely) ।"
                ],
                "poetic_hindi": [
                    "बुल्ले शाह: हम कभी न मरेंगे, अमर हुई आत्मा की डोर,",
                    "कब्र में तो कोई और गिरेगा, मिटेगा केवल मिट्टी का छोर !",
                    "मेरा रांझा अब कोई और ही हुआ, रूप उसका अनूप !"
                ],
                "poetic_english": [
                    "Bulleh Shah proclaims: We shall never die, death cannot claim our breath;",
                    "Into the grave they will lay someone else—the mortal shell of dust and death!",
                    "My Ranjha has become someone else entirely, luminous forevermore!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी सूफी रहस्यवाद में 'बका-बिल्लाह' (परमेश्वर में शाश्वत जीवन) का स्पष्टतम घोषणापत्र है। बुल्ले शाह जब कहते हैं कि 'मेरा रांझा हुन कोई होर', तो इसका अर्थ है कि लौकिक रांझा अब अलौकिक सर्वव्यापी ब्रह्म बन चुका है। वह तख्त हजारे (भौतिक संसार) से 'चोर' बनकर निकल चुका है और अब तख्त लाहौर (हज़रत शाह इनायत का आध्यात्मिक सिंहासन) पर विराजमान है। अंतिम पंक्ति 'असीं मरना नाहीं, कबर पाय कोई होर' आत्मज्ञान की पराकाष्ठा है। देह नश्वर है और कब्र में देह का ही संस्कार होता है, परंतु जो आत्मा अपने प्रियतम के साथ एकाकार हो चुकी है, वह काल और मृत्यु से परे अमर हो जाती है। यह कबीर के 'हम ना मरब मरिहै संसारा' और श्रीमद्भगवद्गीता के 'नैनं छिन्दन्ति शस्त्राणि' का सूफी प्रतिरूप है।"
    },
    {
        "id": 100,
        "title": "मेरे घर आया पिया हमारा",
        "title_english": "My Beloved Has Arrived at My Home",
        "historical_context": "यह काफी भाग 2 (काफ़ियां 51–100) का भव्य, विजयी और आनंदोल्लासपूर्ण शिखर है। विरह के समस्त कष्ट, संशय और साधना की तपस्या अब 'वसल' (पूर्ण मिलन) में परिणत हो चुकी है। साधक के अंतर्मन में अनहद नाद की वंशी बज रही है, अद्वैत ('वाहदत') का जयघोष हो रहा है, और लाहौर के तख्त (मुर्शिद शाह इनायत का सान्निध्य) की प्राप्ति हो चुकी है। समस्त खोट (दोष) प्रेम की आंच में जलकर भस्म हो गए हैं, और संसार के बीस-पचास झंझट समाप्त होकर चारों ओर केवल 'लाल' (परम प्रियतम का रंग) दिखाई दे रहा है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: मेरे घर आया पिया हमारा)",
        "raga": "राग बिलावल / काफी",
        "theme": "वसल (परम मिलन), अनहद नाद, तख्त लाहौर की प्राप्ति, अद्वैत का उत्सव (वहदत), भाग 2 का महा-समापन",
        "stanzas": [
            {
                "original": [
                    "वाह वाह वाहदत कीना शोर, अनहद बांसरी दी घंगोर,  ",
                    "असां हुन पाइआ तखत लाहौर, मेरे घर आया पिया हमारा ।"
                ],
                "hindi_gloss": [
                    "वाह (धन्य है) वाह (धन्य है), वाहदत (परम अद्वैत/एकेश्वरवाद) कीना (ने मचा दिया है आनंद का) शोर (जयघोष), अनहद (अनाहत नाद की) बांसरी (वंशी) दी (की गूंज रही है) घंगोर (गंभीर मधुर झंकार),",
                    "असां (हमने) हुन (अब) पाइआ (प्राप्त कर लिया है) तखत (आध्यात्मिक सिंहासन) लाहौर (लाहौर का), मेरे (मेरे) घर (हृदय-गृह में) आया (पधार चुका है) पिया (प्रियतम) हमारा (हमारा) ।"
                ],
                "english_gloss": [
                    "वाह वाह (hail, wondrous hail!), वाहदत (divine Oneness/Wahdat) कीना शोर (raised its glorious proclaim), अनहद (unstruck) बांसरी (flute) दी घंगोर (resonant swell),",
                    "असां (we) हुन (now) पाइआ (have attained) तखत लाहौर (the Throne of Lahore), मेरे घर (to my home) आया (has come) पिया हमारा (our Beloved) ।"
                ],
                "poetic_hindi": [
                    "वाह री वाहदत ! गूँजा जयघोष, अनहद बंसी की मधुर घंघोर,",
                    "पाया हमने तख्त लाहौर, मेरे घर आया पिया हमारा !",
                    "बरसा अमृत, मिटा अंधेरा, दूर हुआ विरह का रोष,",
                    "परमानंद में डूबी सुरति, मिट गया मन का सारा क्लेश !"
                ],
                "poetic_english": [
                    "Hail, wondrous Oneness! The skies resound, the Anhad flute swells rich and deep;",
                    "We have attained the Throne of Lahore, no longer does my spirit weep!",
                    "My Beloved has entered my humble home, dispelling every shadow of fright:",
                    "The universe sings in sweet accord, crowned with eternal love and light!"
                ]
            },
            {
                "original": [
                    "जल गए मेरे खोट निखोट, लग गई प्रेम सच्चे दी चोट,  ",
                    "हुन सानूं ओस खसम दी ओट, मेरे घर आया पिया हमारा ।"
                ],
                "hindi_gloss": [
                    "जल (जलकर भस्म) गए (हो गए) मेरे (मेरे सारे) खोट (खोट/दोष) निखोट (और सूक्ष्म से सूक्ष्म कमियां), लग (लग) गई (चुकी है) प्रेम (सच्चे इलाही प्रेम) सच्चे (सच्चे) दी (की) चोट (तीखी चोट/बाण),",
                    "हुन (अब) सानूं (मुझको) ओस (उस परम) खसम (स्वामी/सद्गुरु) दी (की ही एकमात्र) ओट (शरण/आश्रय है), मेरे (मेरे) घर (घर में) आया (आया है) पिया (प्रियतम) हमारा (हमारा) ।"
                ],
                "english_gloss": [
                    "जल गए (burnt to ash) मेरे खोट निखोट (all my impurities and blemishes), लग गई (struck deep) प्रेम सच्चे दी चोट (the arrow of true love),",
                    "हुन सानूं (now unto us) ओस खसम दी ओट (is the sole shelter of that Sovereign Master), मेरे घर आया पिया हमारा (my Beloved has entered my home) ।"
                ],
                "poetic_hindi": [
                    "खोट-कपट सब जल कर खाक, जब सच्चे प्रेम की चोट लगी,",
                    "उस साहिब की ओट मिली जब, सोई हुई किस्मत जाग उठी !",
                    "पाप-पुण्य के पार हुई मैं, पाया सच्चा सहारा,",
                    "मेरे घर आया पिया हमारा !"
                ],
                "poetic_english": [
                    "All dross and blemish burnt away when true Love struck its piercing dart;",
                    "Beneath the shelter of my Lord rests now my healed and peaceful heart!",
                    "Beyond all merit, beyond all sin, His sanctuary holds me fast:",
                    "My Beloved has entered my humble home, the night of separation is past!"
                ]
            },
            {
                "original": [
                    "हुन क्या कन्नें साल वसाल, लग गिआ मसत प्याला हाथ,  ",
                    "हुन मेरी भुल्ल गई ज़ात सफ्फात, मेरे घर आया पिया हमारा ।"
                ],
                "hindi_gloss": [
                    "हुन (अब) क्या (क्या पूछना) कन्नें (कानों में गूंजते हुए) साल (वर्षों) वसाल (और वियोग-मिलन के किस्सों का), लग (लग) गिआ (चुका है) मसत (मदमस्त कर देने वाला प्रेम का) प्याला (प्याला) हाथ (मेरे हाथों में),",
                    "हुन (अब) मेरी (मेरी) भुल्ल (विस्मृत/गायब हो) गई (गई है) ज़ात (जाति/अस्तित्व) सफ्फात (और सारे सांसारिक गुण-धर्म), मेरे (मेरे) घर (घर में) आया (पधारा है) पिया (प्रियतम) हमारा (हमारा) ।"
                ],
                "english_gloss": [
                    "हुन क्या (what now) कन्नें साल वसाल (of years and tales whispered in ears), लग गिआ (is grasped) मसत प्याला हाथ (the ecstatic goblet in hand),",
                    "हुन मेरी (now mine) भुल्ल गई (forgotten are) ज़ात (caste/identity) सफ्फात (attributes and forms), मेरे घर आया पिया हमारा (my Beloved has entered my home) ।"
                ],
                "poetic_hindi": [
                    "वर्षों के वियोग अब क्या गिनूँ, जब हाथ में मस्ती का प्याला आया,",
                    "जात-पांत और गुण-अवगुण सब भूल गई, जब साहिब पाया !",
                    "मिट गई हस्ती, मिट गया आपा, बह निकली रस की धारा,",
                    "मेरे घर आया पिया हमारा !"
                ],
                "poetic_english": [
                    "What care I now for whispered years, for tales of parting long and sore?",
                    "When ecstasy’s brimful golden chalice is placed in my hand forevermore!",
                    "Forgotten is caste, forgotten all forms, my petty self dissolves in grace:",
                    "My Beloved has entered my humble home, illuminating time and space!"
                ]
            },
            {
                "original": [
                    "हुन क्या कीने बीस पचास, प्रीतम पाई असां वल झात,  ",
                    "हुन सानूं सभ जग्ग दिसदा लाल, मेरे घर आया पिया हमारा ।"
                ],
                "hindi_gloss": [
                    "हुन (अब) क्या (क्या लेना-देना) कीने (किए हुए दुनियावी) बीस (बीस) पचास (पचास प्रपंचों से), प्रीतम (जब मेरे परम प्रियतम ने) पाई (डाल दी है) असां (हमारी) वल (ओर अपनी अनुग्रह भरी) झात (प्रेम-दृष्टि),",
                    "हुन (अब) सानूं (मुझको) सभ (सारा) जग्ग (संसार) दिसदा (दिखाई दे रहा है) लाल (प्रियतम के ही लाल रंग में रंगा हुआ), मेरे (मेरे) घर (घर में) आया (आया है) पिया (प्रियतम) हमारा (हमारा) ।"
                ],
                "english_gloss": [
                    "हुन क्या कीने (what care I for) बीस पचास (twenty or fifty worldly stratagems), प्रीतम (the Beloved) पाई (cast) असां वल (towards us) झात (His radiant loving glance),",
                    "हुन सानूं (now unto us) सभ जग्ग (the entire universe) दिसदा लाल (appears ruby-red/dyed in Beloved's hue), मेरे घर आया पिया हमारा (my Beloved has entered my home) ।"
                ],
                "poetic_hindi": [
                    "बीस-पचास के फंद छूटे जब प्रीतम ने डाली प्रेम-झात,",
                    "पल भर में सब कलुष धुल गया, उजियारी हो गई काली रात !",
                    "कण-कण में अब लाल दिखे वो, लाल हुआ जग सारा,",
                    "मेरे घर आया पिया हमारा !"
                ],
                "poetic_english": [
                    "What care I for worldly scores and schemes of twenty, forty, or fifty cares?",
                    "Since my Beloved turned His eyes and answered all my secret prayers!",
                    "The universe glows in radiant crimson, dyed in His beauty pure and bright:",
                    "My Beloved has entered my humble home, flooding my cosmos with delight!"
                ]
            },
            {
                "original": [
                    "हुन सानूं आस दी फ़ाश, बुल्ल्हा शहु आया हमरे पास,  ",
                    "साईं पुचाई साडी आस, मेरे घर आया पिया हमारा ।"
                ],
                "hindi_gloss": [
                    "हुन (अब) सानूं (हमारी) आस (सांसारिक तृष्णा/आशा) दी (का हो गया है) फ़ाश (विनाश/फांस कट चुकी है), बुल्ल्हा (बुल्ले शाह कहते हैं) शहु (साक्षात् परमात्मा/सद्गुरु) आया (पधार चुके हैं) हमरे (हमारे) पास (समीप),",
                    "साईं (मेरे सच्चे प्रभु/मुर्शिद ने) पुचाई (पूरी कर दी है) साडी (हमारी चिर-संचित) आस (प्रेम की अभिलाषा), मेरे (मेरे) घर (घर में) आया (आया है) पिया (प्रियतम) हमारा (हमारा) ।"
                ],
                "english_gloss": [
                    "हुन सानूं (now unto us) आस दी फ़ाश (all earthly hopes/snares are severed/fulfilled), बुल्ल्हा (Bulleh) शहु (Sovereign Lord) आया हमरे पास (has arrived beside us),",
                    "साईं (the Master Lord) पुचाई (fulfilled) साडी आस (our deepest longing), मेरे घर आया पिया हमारा (my Beloved has entered my home) ।"
                ],
                "poetic_hindi": [
                    "सांसारिक तृष्णा की फाँसी कटी, जब बुल्ले के घर साहिब आया,",
                    "साईं ने पूरी आस करी, मनचाहा सच्चा मीत मिलाया !",
                    "पूर्ण हुआ भाग दो का मंगल, धन्य हुआ जीवन सारा,",
                    "मेरे घर आया पिया हमारा !"
                ],
                "poetic_english": [
                    "The snares of mortal hope are severed, the Sovereign King is by my side;",
                    "The Master has fulfilled my yearning, taking Bulleh as His bride!",
                    "Part Two concludes in triumph grand, my soul attains its haven shore:",
                    "My Beloved has entered my humble home, and dwells with me forevermore!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी बुल्ले शाह की काव्य-यात्रा के द्वितीय खंड (काफ़ियां 51–100) का परम आनंदमय और परिपूर्ण निष्कर्ष है। विरह की अग्नि में तपकर कुंदन बनी जीवात्मा अब 'वसल' (शाश्वत समागम) का उत्सव मना रही है। 'वाहदत कीना शोर' का अर्थ है कि द्वैत का संशय पूरी तरह मिट चुका है और केवल एकत्व का डंका बज रहा है। 'अनहद बांसरी' अंतःकरण में बजने वाले उस अनाहत नाद का प्रतीक है जो समाधि की अवस्था में स्वतः प्रकट होता है। 'तखत लाहौर' हज़रत शाह इनायत कादरी के आध्यात्मिक दरबार और साक्षात साक्षात्कार का सूचक है। सांसारिक आशाओं (आस) की फांसी कट चुकी है क्योंकि जब स्वयं परमात्मा घर आ गया, तो फिर किसी अन्य वस्तु की कामना शेष नहीं रहती। 'सभ जग्ग दिसदा लाल' अमीर खुसरो के 'छाप तिलक सब छीनी रे मोसे नैना मिलाइके' और 'लाली मोरे लाल की जित देखूँ तित लाल' की भांति सर्वेश्वरवाद की अंतिम अनुभूति है।"
    }
]

new_lexicon_terms = {
    "टमक": {"hindi": "बड़ा नगाड़ा, रण-ढोल", "english": "large kettledrum, martial battle-drum"},
    "मुकाल": {"hindi": "मुँह पर कालिमा, कलंक, बदनामी", "english": "blackening of face, public disgrace/scandal"},
    "पंजे पीर": {"hindi": "सूफी परंपरा में पाँच परम सिद्ध पीर (ख्व़ाजा मोइनुद्दीन चिश्ती, बाबा फरीद, बहाउद्दीन जकरिया, लाल शहबाज कलंदर, मखदूम जहांगियां)", "english": "the five venerable master saints of Punjab/Sufi tradition"},
    "शाम सुन्दर": {"hindi": "श्रीकृष्ण, श्यामसुंदर, परब्रह्म का मधुर रूप", "english": "Shyam Sundar, the Beautiful Dark One (Krishna as Supreme Divine)"},
    "खाविन्द": {"hindi": "पति; सूफी रूपक में: नफ़्स, सांसारिक अहंकार जो जीवात्मा को बांधे रखता है", "english": "husband; in Sufi metaphor: the carnal self (Nafs) / lower ego"},
    "सिर देही": {"hindi": "आत्मा और परमात्मा की सूक्ष्म देह, आत्मिक स्वरूप", "english": "the spiritual subtle body, divine essence"},
    "तखत मुनव्वर": {"hindi": "परम प्रकाशमान सिंहासन, अर्श-ए-इलाही", "english": "the Throne of Luminous Light, celestial divine throne"},
    "घंगोर": {"hindi": "गंभीर मधुर गूंज, अनहद नाद का प्रसार", "english": "resonant profound swell, echoing melody"},
    "ज़ात सफ्फात": {"hindi": "मूल सत्ता (ज़ात) और उसके गुण/विशेषण (सिफात)", "english": "Essence (Dhat) and Attributes (Sifat)"},
    "झात": {"hindi": "कृपा-दृष्टि, प्रेममयी झलक, झांकना", "english": "benevolent glance, loving gaze/look"}
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
        "completed_count": 100,
        "total": 160,
        "next_kafi_id": 101,
        "last_updated": "2026-10-17T18:05:00+05:30",
        "last_batch": "96-100",
        "status": "in_progress",
        "milestone": "Part 2 (51-100) Complete! 62.5% of corpus finished."
    }
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print(f"Checkpoint updated: 100/160 completed. Part 2 Complete! Next ID: 101")

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
