# -*- coding: utf-8 -*-
"""
Process Kafian 121 to 125 for Bulleh Shah Trilingual Edition.
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
        "id": 121,
        "title": "प्यारे बिन मसल्हत उट्ठ जाणा",
        "title_english": "Without Counsel We Must Depart, O Beloved: Sometime Turn Wise!",
        "historical_context": "यह 4 बंधों की एक अत्यंत मर्मस्पर्शी, वैराग्यमयी और चेतावनीपरक काफी है। इसमें बुल्ले शाह मनुष्य को मृत्यु की अचानक और अप्रत्याशित प्रकृति से सचेत करते हैं। मृत्यु बिना किसी पूर्व सूचना, परामर्श ('मसल्हत') या अनुमति के आती है और जीव को इस संसार से उठा ले जाती है। चार दिन की सांसारिक मौज-मस्ती के बाद मनुष्य को अंततः अकिंचन होकर कब्र के 'शहर-ए-खामोशां' (खामोशों का नगर) में समाना पड़ता है जहाँ सारी दुनिया समाई हुई है। मलक-उल-मौत (यमदूत) वह निर्दयी मल्लाह है जो नाव भर-भरकर जीवों को उस पार ले जा रहा है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: प्यारे बिन मसल्हत उट्ठ जाना)",
        "raga": "राग काफी / आसा / भैरवी",
        "theme": "मृत्यु का अकस्मात आगमन (बिन मसल्हत), शहर-ए-खामोशां (कब्रिस्तान), मलक-उल-मौत का रूपक, अहंकार का त्याग",
        "stanzas": [
            {
                "original": [
                    "प्यारे बिन मसल्हत उट्ठ जाना ।  ",
                    "तूं कदी ते हो स्याना ।"
                ],
                "hindi_gloss": [
                    "प्यारे (ऐ प्यारे मनुष्य) बिन (बिना किसी पूर्व) मसल्हत (परामर्श/सूचना के अचानक यहाँ से) उट्ठ जाना (उठकर प्रस्थान कर जाना पड़ेगा) ।",
                    "तूं (तू) कदी (कभी तो अपने जीवन में) ते (तो) हो (हो जा) स्याना (बुद्धिमान और ज्ञानी) ।"
                ],
                "english_gloss": [
                    "प्यारे (O dear one) बिन मसल्हत (without counsel/warning) उट्ठ जाना (one must arise and depart) ।",
                    "तूं कदी ते हो स्याना (sometime at least, become thou wise and aware) ।"
                ],
                "poetic_hindi": [
                    "ऐ प्यारे, बिना किसी सम्मति के अचानक उठ जाना पड़ेगा,",
                    "कभी तो हो जा ज्ञानी तू, काल का डंका बाजेगा !"
                ],
                "poetic_english": [
                    "Without warning or counsel, O dear soul, thou must arise and depart;",
                    "Awaken and become wise sometime, and cleanse thy heedless heart!"
                ]
            },
            {
                "original": [
                    "करके चावड़ चार देहाड़े, थीसें अंत निमाना ।  ",
                    "ज़ुलम करें ते लोक सतावें, छड्ड दे ज़ुलम सताना ।  ",
                    "प्यारे बिन मसल्हत उट्ठ जाना ।"
                ],
                "hindi_gloss": [
                    "करके (करके अहंकार भरा) चावड़ (उछल-कूद और विलास) चार (चार) देहाड़े (दिनों का), थीसें (हो जाएगा तू) अंत (अंत समय सर्वथा असहाय और) निमाना (दीन-हीन),",
                    "ज़ुलम (दूसरों पर अत्याचार) करें (करता है) ते (और) लोक (निर्दोष लोगों को) सतावें (सताता है तू), छड्ड (छोड़) दे (दे यह) ज़ुलम (अत्याचार करना और दुर्बलों को) सताना (सताना) ।",
                    "प्यारे बिन मसल्हत उट्ठ जाना ।"
                ],
                "english_gloss": [
                    "करके चावड़ चार देहाड़े (making merry riot for four brief days), थीसें अंत निमाना (in the end thou shalt become utterly helpless and low),",
                    "ज़ुलम करें ते लोक सतावें (thou committest tyranny and tormentest folk), छड्ड दे ज़ुलम सताना (abandon this oppression and tormenting) ।",
                    "प्यारे बिन मसल्हत उट्ठ जाना (without counsel thou must depart) ।"
                ],
                "poetic_hindi": [
                    "चार दिनों का नाच-तमाशा, अंत समय लाचार बनेगा,",
                    "ज़ुल्म करे औरों पे अज्ञानी, छोड़ दे पाप, नहीं तो मरेगा !",
                    "ऐ प्यारे, बिना सलाह के जाना पड़ेगा !"
                ],
                "poetic_english": [
                    "Reveling in arrogance for four brief days, thou wilt end in helpless plight;",
                    "Oppressing the poor and torturing souls—forsake this tyrannical might!",
                    "Without warning or counsel thou must depart!"
                ]
            },
            {
                "original": [
                    "जिस जिस दा वी मान करें तूं, सो वी साथ ना जाना ।  ",
                    "शहर-खामोशां वेख हमेशां, जिस विच जग्ग समाना ।  ",
                    "प्यारे बिन मसल्हत उट्ठ जाना ।"
                ],
                "hindi_gloss": [
                    "जिस (जिस-जिस धन, कुटुम्ब और बल) जिस (का) दा (का) वी (भी) मान (घमंड) करें (करता है) तूं (तू), सो (वह कोई) वी (भी तेरे) साथ (साथ परलोक में) ना (नहीं) जाना (जाएगा),",
                    "शहर-खामोशां (उस खामोशों के नगर अर्थात् कब्रिस्तान को) वेख (देख तू) हमेशां (सदा ध्यान से), जिस (जिसकी मिट्टी के) विच (भीतर यह सारा) जग्ग (संसार) समाना (समा चुका है) ।",
                    "प्यारे बिन मसल्हत उट्ठ जाना ।"
                ],
                "english_gloss": [
                    "जिस जिस दा वी मान करें तूं (whatever worldly power thou boastest of), सो वी साथ ना जाना (none of that shall accompany thee),",
                    "शहर-खामोशां वेख हमेशां (gaze always upon the City of the Silent / the graveyard), जिस विच जग्ग समाना (wherein the whole world has dissolved) ।",
                    "प्यारे बिन मसल्हत उट्ठ जाना (without counsel thou must depart) ।"
                ],
                "poetic_hindi": [
                    "जिस-जिसका तू घमंड करे, वो संग नहीं जाने वाला,",
                    "शहर-ए-खामोशां देख ज़रा, जहाँ सारा जग समाने वाला !",
                    "ऐ प्यारे, बिना सलाह के जाना पड़ेगा !"
                ],
                "poetic_english": [
                    "Whatever worldly wealth thou boastest will vanish like thin air;",
                    "Behold the Silent City of graves—the entire world is sleeping there!",
                    "Without warning or counsel thou must depart!"
                ]
            },
            {
                "original": [
                    "भर भर पूर लंघावे डाढा, मलकुल-मौत मुहाना ।  ",
                    "ऐथे हैन तनते सभ, मैं अवगुणहार निमाना ।  ",
                    "प्यारे बिन मसल्हत उट्ठ जाना ।"
                ],
                "hindi_gloss": [
                    "भर (भर-) भर (भर कर) पूर (जीवों की भरी नावें) लंघावे (उस पार ले जाता है) डाढा (अत्यंत कठोर और बलवान), मलकुल-मौत (मलक-उल-मौत/यमदूत रूपी) मुहाना (मल्लाह),",
                    "ऐथे (इस संसार में) हैन (हैं सभी लोग) तनते (अपने-अपने प्रपंचों में तने हुए), मैं (परंतु मैं तो केवल एक) अवगुणहार (अवगुणों से भरा) निमाना (दीन सेवक हूँ) ।",
                    "प्यारे बिन मसल्हत उट्ठ जाना ।"
                ],
                "english_gloss": [
                    "भर भर पूर लंघावे डाढा (ferries full boatloads across, stern and relentless), मलकुल-मौत मुहाना (the Angel of Death as the grim boatman),",
                    "ऐथे हैन तनते सभ (here all worldly folk strut in proud pretense), मैं अवगुणहार निमाना (while I am a lowly sinner bereft of merit) ।",
                    "प्यारे बिन मसल्हत उट्ठ जाना (without counsel thou must depart) ।"
                ],
                "poetic_hindi": [
                    "नावें भर-भर पार उतारे, यमदूत-मल्लाह विकराल,",
                    "सब यहाँ दंभ में तने खड़े, मैं अवगुणहारा दीन कंगाल !",
                    "ऐ प्यारे, बिना सलाह के जाना पड़ेगा !"
                ],
                "poetic_english": [
                    "The Angel of Death, the relentless boatman, ferries full cargoes away;",
                    "While worldly men strut in arrogance, I weep as a sinner without sway!",
                    "Without warning or counsel thou must depart!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा दुशमन नाल बरे विच, है दुशमन बल ढाना ।  ",
                    "महबूब-रब्बानी करे रसाई, ख़ौफ जाए मलकाना ।  ",
                    "प्यारे बिन मसल्हत उट्ठ जाना ।  ",
                    "तूं कदी ते हो स्याना ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ले शाह कहते हैं) दुशमन (नफ़्स और काम-क्रोध रूपी शत्रु के) नाल (साथ इस संसार रूपी) बरे (रणक्षेत्र) विच (में युद्ध छिड़ा है), है (और इस) दुशमन (शत्रु के ही) बल (बल को) ढाना (ढहाना हमारा मुख्य कर्तव्य है),",
                    "महबूब-रब्बानी (परमात्मा के प्रिय सद्गुरु हज़रत शाह इनायत जब) करे (करते हैं अपनी कृपा भरी) रसाई (पहुँच/मार्गदर्शन), ख़ौफ (तो मृत्यु और यमदूत का सारा भय) जाए (मिट जाता है) मलकाना (और साधक निर्भय पद प्राप्त करता है) ।",
                    "प्यारे (ऐ प्यारे) बिन (बिना) मसल्हत (सलाह के) उट्ठ जाना (यहाँ से जाना ही है) । तूं (तू) कदी (कभी तो) ते (तो) हो (हो जा) स्याना (स्याना/ज्ञानी) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा दुशमन नाल बरे विच (Bulleh: the battle in this arena is against the enemy of ego), है दुशमन बल ढाना (to shatter the strength of this inner foe is our quest),",
                    "महबूब-रब्बानी करे रसाई (when the Divine Beloved Master grants access and grace), ख़ौफ जाए मलकाना (the dread of the Angel of Death dissolves away) ।",
                    "प्यारे बिन मसल्हत उट्ठ जाना (without counsel thou must depart) । तूं कदी ते हो स्याना (sometime become thou wise) ।"
                ],
                "poetic_hindi": [
                    "बुल्ला कहे: रण में नफ़्स से लड़ना, तोड़ना इस वैरी का मान,",
                    "रब का महबूब जब रहमत बख्शे, मिटे काल का डर और भान !",
                    "ऐ प्यारे, बिना किसी सम्मति के अचानक उठ जाना पड़ेगा,",
                    "कभी तो हो जा ज्ञानी तू, काल का डंका बाजेगा !"
                ],
                "poetic_english": [
                    "Says Bulleh: Wage war on the tyrant ego, shatter its power in the field;",
                    "When the Lord's Beloved extends His grace, all dread of death must yield!",
                    "Without warning or counsel, O dear soul, thou must arise and depart;",
                    "Awaken and become wise sometime, and cleanse thy heedless heart!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी सूफी जीवन-दर्शन के वैराग्य (जुहद) और आत्म-चेतना (मुहासिबा) का प्रखर उद्बोधन है। 'शहर-ए-खामोशां' (कब्रिस्तान) सूफी साहित्य का वह केंद्रीय प्रतीक है जहाँ जाकर मनुष्य का सारा सांसारिक दंभ, धन-दौलत और जातिगत अहंकार समाप्त हो जाता है। मृत्यु किसी की मर्जी या अनुमति की मोहताज नहीं है ('बिन मसल्हत')। 'मलक-उल-मौत मुहाना' का रूपक जीवन को नदी और मृत्यु को उस पार ले जाने वाले नाव-मल्लाह के रूप में देखता है। अंतिम पद में बुल्ला स्पष्ट करते हैं कि सच्चा युद्ध किसी बाहरी शत्रु से नहीं, बल्कि अपने ही 'नफ़्स' (वासना और अहंकार) से है, और इस युद्ध में विजय केवल सद्गुरु ('महबूब-ए-रब्बानी') की कृपा से ही संभव है।"
    },
    {
        "id": 122,
        "title": "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा",
        "title_english": "O Dear Soul, Enter Love With Caution, Lest Thou Repent Afterwards!",
        "historical_context": "यह 7 बंधों की एक अत्यंत गंभीर, चेतावनीपरक और सूफी इतिहास के रक्त-रंजित बलिदानों को उजागर करने वाली काफी है। बुल्ले शाह साधक को आगाह करते हैं कि ईश्वर का प्रेम कोई फूलों की सेज नहीं है; यह वह भयानक घाटी है जहाँ बड़े-बड़े शेरों के हौसले पस्त हो जाते हैं। यूसुफ को कुएं में फेंका गया और मिस्र के बाजार में कौड़ियों के मोल बेचा गया। जुलेखा तड़पी, मजनू विलाप करता रहा। शम्स तबरेज़ी की खाल खिंचवाई गई, जकरिया पर आरा चलवाया गया और मंसूर को सूली पर चढ़ाया गया। यदि तुममें 'अनलहक' कहकर सूली पर ढोले गाने का साहस है, तभी इस इश्क के मदिरालय में प्रवेश करो!",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: प्यारिआ संभल के नेहुं ला)",
        "raga": "राग काफी / आसावरी",
        "theme": "इश्क की कठिन परीक्षा, पैगंबरों और संतों के बलिदान, मंसूर की सूली, शम्स तबरेज़ी, शराब-ए-इश्क",
        "stanzas": [
            {
                "original": [
                    "जांदा जा ना आवीं फेर, ओथे बेपरवाही ढेर,  ",
                    "ओथे डहल खलोंदे शेर, तूं वी फद्ध्या जावेंगा ।  ",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा ।"
                ],
                "hindi_gloss": [
                    "जांदा (जाता है तो) जा (जा, परंतु लौटकर) ना (मत) आवीं (आना) फेर (पुनः), ओथे (उस प्रेम-मार्ग पर तो प्रभु की) बेपरवाही (उदासीनता और कठोर परीक्षाएं) ढेर (अपार हैं),",
                    "ओथे (वहाँ उस घाटी में) डहल (दहशत से कांप) खलोंदे (खड़े रह जाते हैं बब्बर) शेर (शेर जैसे वीर भी), तूं (तू तो एक दुर्बल मनुष्य है, तू) वी (भी) फद्ध्या (पकड़/जकड़ लिया) जावेंगा (जाएगा) ।",
                    "प्यारिआ (ऐ प्यारे) संभल (संभल-) के (करके) नेहुं (प्रेम) ला (लगाना), पिच्छों (अन्यथा बाद में जीवन भर) पछतावेंगा (पछताएगा) ।"
                ],
                "english_gloss": [
                    "जांदा जा ना आवीं फेर (go if thou wilt, but return no more), ओथे बेपरवाही ढेर (boundless is the heedless severity there),",
                    "ओथे डहल खलोंदे शेर (there mighty lions tremble and quail in terror), तूं वी फद्ध्या जावेंगा (thou too wilt be ensnared and caught) ।",
                    "प्यारिआ संभल के नेहुं ला (O dear one, enter Love with caution), पिच्छों पछतावेंगा (lest afterwards thou repentest in vain) ।"
                ],
                "poetic_hindi": [
                    "जाता है तो जा, मुड़ के न आना, वहाँ बेपरवाही अपार खड़ी,",
                    "जहाँ शेर भी दहशत से कांपें, तेरी हस्ती क्या बेचारी बड़ी?",
                    "ऐ प्यारे, संभल के प्रीत लगा, पीछे पछताएगा !"
                ],
                "poetic_english": [
                    "Go if thou wilt, but turn not back; boundless is the stern indifference there;",
                    "Mighty lions tremble in dread—how wilt thou brave that fiery snare?",
                    "O dear soul, enter Love with caution, lest thou repent in vain!"
                ]
            },
            {
                "original": [
                    "खूह विच यूसफ पाइओ ने, फड़ विच बज़ार विकाइओ ने,  ",
                    "इक्क अट्टी मुल्ल पवाइओ ने, तूं कौडी मुल्ल पवावेंगा ।  ",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा ।"
                ],
                "hindi_gloss": [
                    "खूह (अंधे कुएं) विच (में) यूसफ (हज़रत यूसुफ को) पाइओ (फेंक दिया) ने (सगे भाइयों ने), फड़ (पकड़कर) विच (में) बज़ार (मिस्र के बाजार में) विकाइओ (गुलाम बनाकर बिकवा दिया) ने,",
                    "इक्क (सूत की मात्र एक) अट्टी (लच्छी के) मुल्ल (मूल्य पर नीलाम) पवाइओ (करवा दिया) ने (उसे), तूं (तू तो साधारण जीव है, तू तो) कौडी (कौड़ियों के) मुल्ल (मोल) पवावेंगा (बेचा जाएगा) ।",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा ।"
                ],
                "english_gloss": [
                    "खूह विच यूसफ पाइओ ने (they cast Joseph into the deep, dark well), फड़ विच बज़ार विकाइओ ने (dragged Him to the market and sold Him as a slave),",
                    "इक्क अट्टी मुल्ल पवाइओ ने (sold Him for a meager skein of yarn), तूं कौडी मुल्ल पवावेंगा (thou wilt be auctioned off for a single cowrie) ।",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा (O dear soul, enter Love with caution) ।"
                ],
                "poetic_hindi": [
                    "यूसुफ को कुएं में डाला, मिस्र के बाज़ार में नीलाम किया,",
                    "सूत की लच्छी के मोल बिका वो, तेरा मोल तो कौड़ी न दिया !",
                    "ऐ प्यारे, संभल के प्रीत लगा, पीछे पछताएगा !"
                ],
                "poetic_english": [
                    "Into the dry well Joseph was cast, and sold in the slave-bazaar for a thread;",
                    "An emperor’s beauty bartered for yarn—for a broken coin wilt thou be shed!",
                    "O dear soul, enter Love with caution, lest thou repent in vain!"
                ]
            },
            {
                "original": [
                    "नेहुं ला वेख ज़ुलैखां लए, ओथे आशक तड़फन पए,  ",
                    "मजनूं करदा है है है, तूं ओथों की ल्यावेंगा ।  ",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा ।"
                ],
                "hindi_gloss": [
                    "नेहुं (प्रेम) ला (लगाने के परिणाम को) वेख (देख कि) ज़ुलैखां (रानी ज़ुलैखा ने कैसे दुख) लए (झेल लिए), ओथे (उस इश्क के मैदान में सच्चे) आशक (आशिक खून के आंसू) तड़फन (तड़पते) पए (रहे),",
                    "मजनूं (मजनू जंगल-जंगल भटकता) करदा (करता रहा विरह में) है (हाय!) है (हाय!) है (हाय!), तूं (तू भला दुर्बल होकर) ओथों (उस प्रेम-घाटी से) की (क्या लाभ) ल्यावेंगा (लेकर लौटेगा) ।",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा ।"
                ],
                "english_gloss": [
                    "नेहुं ला वेख ज़ुलैखां लए (behold how Zulaikha suffered when she pledged her love), ओथे आशक तड़फन पए (there true lovers writhe in unending agony),",
                    "मजनूं करदा है है है (Majnun cries 'Alas! Alas! Alas!' in the desert), तूं ओथों की ल्यावेंगा (what profit wilt thou bring from that wild shore) ।",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा (O dear soul, enter Love with caution) ।"
                ],
                "poetic_hindi": [
                    "ज़ुलैखा ने झेले विरह के कांटे, प्रेमी तड़पते रहे हर ओर,",
                    "मजनू चीखा 'हाय-हाय' जंगल में, तू क्या लाएगा इस छोर?",
                    "ऐ प्यारे, संभल के प्रीत लगा, पीछे पछताएगा !"
                ],
                "poetic_english": [
                    "Behold Zulaikha’s tears of grief; behold the lovers writhing in pain;",
                    "Majnun laments in the desert waste—what glory dost thou hope to gain?",
                    "O dear soul, enter Love with caution, lest thou repent in vain!"
                ]
            },
            {
                "original": [
                    "उथे इकना पोसत लुहाईदे, इक आरिआं नाल चिराईदे,  ",
                    "इक्क सूली पकड़ चढ़ाईदे, उथे तूं वी सीस कटावेंगा ।  ",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा ।"
                ],
                "hindi_gloss": [
                    "उथे (उस प्रेम-मार्ग पर) इकना (कितने ही संतों की खालें/चमड़ी) पोसत (जीवित ही) लुहाईदे (खिंचवा ली जाती हैं), इक (कितने ही नबी) आरिआं (आरे) नाल (से सिर से पैर तक) चिराईदे (चीर दिए जाते हैं),",
                    "इक्क (कितने ही निष्कलंक प्रेमी) सूली (सूली पर) पकड़ (पकड़ कर) चढ़ाईदे (चढ़ा दिए जाते हैं), उथे (उस विकट राह में) तूं (तू) वी (भी अपना) सीस (शीश) कटावेंगा (कटवा बैठेगा) ।",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा ।"
                ],
                "english_gloss": [
                    "उथे इकना पोसत लुहाईदे (there the skin is flayed alive from some), इक आरिआं नाल चिराईदे (some are sawn asunder with saws),",
                    "इक्क सूली पकड़ चढ़ाईदे (some are dragged and mounted on the gallows), उथे तूं वी सीस कटावेंगा (there thou too wilt have thy head severed) ।",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा (O dear soul, enter Love with caution) ।"
                ],
                "poetic_hindi": [
                    "जहाँ शम्स की खाल उतारी गई, ज़करिया आरे से चीरे गए,",
                    "मंसूर को सूली पे टांग दिया, तू भी तो शीश कटाएगा रे !",
                    "ऐ प्यारे, संभल के प्रीत लगा, पीछे पछताएगा !"
                ],
                "poetic_english": [
                    "There skin was stripped from living saints; with saws were prophets sawn in two;",
                    "Upon the gallows martyrs hung—wilt thou give up thy head there too?",
                    "O dear soul, enter Love with caution, lest thou repent in vain!"
                ]
            },
            {
                "original": [
                    "घर कलालां दा तेरे पासे, ओथे आवन मसत प्यासे,  ",
                    "भर भर पीवन प्याले कासे, तूं वी जिय ललचावेंगा ।  ",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा ।"
                ],
                "hindi_gloss": [
                    "घर (मदिरालय/प्रेम-मधुशाला) कलालां (शराब बनाने/बेचने वालों) दा (का) तेरे (तेरे ही) पासे (पड़ोस/समीप है), ओथे (वहाँ दिव्य प्रेम के) आवन (आते हैं) मसत (मदमस्त और) प्यासे (पिपासु साधक),",
                    "भर (भर-) भर (भर कर) पीवन (पीते हैं वे प्रेम-मदिरा के) प्याले (प्याले और) कासे (पात्र), तूं (तू) वी (भी उन्हें देखकर अपना) जिय (जी/मन) ललचावेंगा (ललचा बैठेगा) ।",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा ।"
                ],
                "english_gloss": [
                    "घर कलालां दा तेरे पासे (the tavern of the vintners is right beside thee), ओथे आवन मसत प्यासे (there arrive the ecstatic and the thirsty),",
                    "भर भर पीवन प्याले कासे (drinking brimful cups and bowls of wine), तूं वी जिय ललचावेंगा (thou too wilt let thy soul be tempted) ।",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा (O dear soul, enter Love with caution) ।"
                ],
                "poetic_hindi": [
                    "मदिरालय तेरे पास ही है, जहाँ मस्त-प्यासियों की भीड़ लगी,",
                    "भर-भर के पिएँ वो जाम वहाँ, तेरी भी तृष्णा जाग उठी !",
                    "ऐ प्यारे, संभल के प्रीत लगा, पीछे पछताएगा !"
                ],
                "poetic_english": [
                    "The tavern of vintners stands close by; the thirsty and crazed are flocking there;",
                    "Drinking brimful chalices of wine—thy soul will be lured to that fiery flare!",
                    "O dear soul, enter Love with caution, lest thou repent in vain!"
                ]
            },
            {
                "original": [
                    "दिलबर हुन ग्युं कित लोउं, भलके की जाणां की हो,  ",
                    "मसतां दे ना कोल खलो, तूं वी मसत सदावेंगा ।  ",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा ।"
                ],
                "hindi_gloss": [
                    "दिलबर (प्रियतम) हुन (अब) ग्युं (चला गया है) कित (किस अज्ञात) लोउं (दिशा/लोक में), भलके (आने वाले कल में) की (क्या) जाणां (जाने कि क्या) की (विपत्ति) हो (घटित हो जाए),",
                    "मसतां (इन प्रेम-मस्तों/दरवेशों) दे (के) ना (पास मत) कोल (समीप) खलो (खड़ा हो), तूं (अन्यथा तू) वी (भी संसार में) मसत (पागल/मस्त) सदावेंगा (कहलाएगा) ।",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा ।"
                ],
                "english_gloss": [
                    "दिलबर हुन ग्युं कित लोउं (whither has the Beloved departed now), भलके की जाणां की हो (who knows what tragedy tomorrow brings),",
                    "मसतां दे ना कोल खलो (stand not beside these ecstatic drunkards), तूं वी मसत सदावेंगा (else thou too wilt be branded crazed) ।",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा (O dear soul, enter Love with caution) ।"
                ],
                "poetic_hindi": [
                    "दिलबर जाने किस ओर गया, कल क्या हो कौन जाने भाई,",
                    "मस्तों के निकट न खड़ा हो तू, दुनिया कहेगी तू भी बौराई !",
                    "ऐ प्यारे, संभल के प्रीत लगा, पीछे पछताएगा !"
                ],
                "poetic_english": [
                    "Whither has the Beloved flown away? Who knows what tomorrow's dawn shall bring?",
                    "Stand not beside these intoxicated souls, lest they brand thee mad in everything!",
                    "O dear soul, enter Love with caution, lest thou repent in vain!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हआ ग़ैर शर्हा ना हो, सुक्ख दी नींदर भर के सो,  ",
                    "मूंहों अनुलहक्क बगो, चढ़ सूली ढोले गावेंगा ।  ",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हआ (हे बुल्ले) ग़ैर (शरिया के विरुद्ध) शर्हा (शरिया के विपरीत) ना (मत) हो (चल), सुक्ख (चैन) दी (की) नींदर (नींद की चादर) भर (तान) के (करके) सो (सोता रह दुनियादार बनकर),",
                    "मूंहों (यदि मुख से तूने) अनुलहक्क ('अनलहक' अर्थात् 'मैं ही ब्रह्म हूँ') बगो (बक दिया/उद्घोष कर दिया), चढ़ (तो तुझे भी) सूली (सूली पर चढ़कर) ढोले (प्रेम के गीत) गावेंगा (गाने पड़ेंगे) ।",
                    "प्यारिआ (ऐ प्यारे) संभल (संभल-) के (कर) नेहुं (प्रीत) ला (लगाना), पिच्छों (अन्यथा बाद में) पछतावेंगा (पछताएगा) ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हआ (O Bulleh) ग़ैर शर्हा ना हो (do not transgress the orthodox Law), सुक्ख दी नींदर भर के सो (sleep comfortably the sleep of ease),",
                    "मूंहों अनुलहक्क बगो (if thou blurtest 'Anal Haqq' from thy lips), चढ़ सूली ढोले गावेंगा (thou wilt sing love-lays hanging on the gallows) ।",
                    "प्यारिआ संभल के नेहुं ला पिच्छों पछतावेंगा (O dear soul, enter Love with caution, lest thou repent) ।"
                ],
                "poetic_hindi": [
                    "बुल्ला कहे: शरिया मत लांघ, सुख की चादर तान के सो,",
                    "मुख से गर 'अनलहक' बोला, तो सूली पे चढ़ ढोला गाएगा वो !",
                    "ऐ प्यारे, संभल के प्रीत लगा, पीछे पछताएगा !"
                ],
                "poetic_english": [
                    "Says Bulleh: Transgress not the formal Law; sleep on in worldly slumber deep;",
                    "For if thou criest 'Anal Haqq!', upon the gallows wilt thou weep!",
                    "O dear soul, enter Love with caution, lest thou repent in vain!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी सूफी साहित्य की एक अद्भुत व्यंग्यात्मक रचना है जिसमें बुल्ले शाह ऊपर से तो साधक को प्रेम-मार्ग से बचने की चेतावनी देते हैं, परंतु वस्तुतः वे यह समझा रहे हैं कि ईश्वर-प्रेम कोई बालकों का खेल नहीं है। यह 'सिर दी बाज़ी' (शीश का समर्पण) है। यूसुफ, ज़ुलैखा, मजनू, शम्स तबरेज़ी, जकरिया और मंसूर का उल्लेख यह स्पष्ट करता है कि इस मार्ग पर चलने वाले प्रत्येक सच्चे साधक को अपनी देह और सांसारिक प्रतिष्ठा का बलिदान देना पड़ा है। अंतिम बंध में 'चढ़ सूली ढोले गावेंगा' मंसूर हल्लाज की उस परम-मस्ती का परिचायक है जहाँ सूली पर लटकते हुए भी सूफी प्रेमी परमात्मा के गीत गाता है।"
    },
    {
        "id": 123,
        "title": "प्यारिआ सानूं मिट्ठड़ा ना लग्गदा शोर",
        "title_english": "O Beloved, Worldly Clamor No Longer Sounds Sweet to Us",
        "historical_context": "यह 3 बंधों की एक अत्यंत शांत, अंतर्मुखी और मधुर काफी है। इसमें सांसारिक प्रपंचों और कोलाहल से विरक्त होकर अंतःकरण के परम विश्राम (मौन) में प्रविष्ट होने का चित्रण है। साधक के हृदय में परमात्मा के प्रेम का एक नया 'शगूफा' (पुष्प) खिल चुका है, जिससे बाहर का शोर अब अरुचिकर लगता है। सांसारिक तृष्णा रूपी कौआ जब आत्मा की पूनी (कपास की बत्ती) छीनकर भागता है, तो साधक उस पूनी को भी ईश्वर के नाम पर दान कर देता है। अंत में हज़रत शाह इनायत कादरी के सान्निध्य में यह शाश्वत प्रण लिया जाता है कि अब सदा प्रियतम के हृदय में ही वास करना है।",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: प्यारिआ सानूं मिट्ठड़ा ना लग्गदा शोर)",
        "raga": "राग काफी / बिलावल",
        "theme": "सांसारिक कोलाहल से वैराग्य, अंतर्मुखी शांति, पूनी का रूपक, शाह इनायत का सान्निध्य",
        "stanzas": [
            {
                "original": [
                    "हुन मैं ते राजी रहनां,  ",
                    "प्यारिआ सानूं मिट्ठड़ा ना लग्गदा शोर ।"
                ],
                "hindi_gloss": [
                    "हुन (अब) मैं (मैं तो परमात्मा की रज़ा में) ते (तो) राजी (संतुष्ट/मग्न) रहनां (रहती हूँ),",
                    "प्यारिआ (ऐ प्यारे) सानूं (मुझको यह सांसारिक) मिट्ठड़ा (मीठा) ना (नहीं) लग्गदा (लगता) शोर (व्यर्थ का शोर-शराबा) ।"
                ],
                "english_gloss": [
                    "हुन मैं ते राजी रहनां (now I abide contented in the Divine Will),",
                    "प्यारिआ सानूं मिट्ठड़ा ना लग्गदा शोर (O beloved, worldly clamor no longer sounds sweet to us) ।"
                ],
                "poetic_hindi": [
                    "अब तो मैं रब की रज़ा में राज़ी रहती हूँ सदा,",
                    "ऐ प्यारे, यह सांसारिक शोर अब मुझको मीठा नहीं लगता !"
                ],
                "poetic_english": [
                    "Contented in the Sovereign Will I now abide in peace;",
                    "O beloved Friend, from worldly noise my weary senses cease!"
                ]
            },
            {
                "original": [
                    "मैं घर खिला शगूफा होर,  ",
                    "वेखियां बाग़ बहारां होर,  ",
                    "हुन मैनूं कुझ ना कहणा,  ",
                    "प्यारिआ सानूं मिट्ठड़ा ना लग्गदा शोर ।"
                ],
                "hindi_gloss": [
                    "मैं (मेरे अंतःकरण के) घर (गृह में) खिला (खिल उठा है एक दिव्य) शगूफा (पुष्प/कली) होर (अनोखा ही),",
                    "वेखियां (देख ली हैं मैंने आंतरिक) बाग़ (बागों की) बहारां (दिव्य वसंत) होर (अलौकिक ही),",
                    "हुन (अब) मैनूं (मुझको दुनियावी ज्ञान की बातें) कुझ (कुछ भी) ना (नहीं) कहणा (कहना),",
                    "प्यारिआ (ऐ प्यारे) सानूं (मुझको) मिट्ठड़ा (मीठा) ना (नहीं) लग्गदा (लगता) शोर (संसार का यह शोर) ।"
                ],
                "english_gloss": [
                    "मैं घर खिला शगूफा होर (within my home a wondrous blossom has unfurled),",
                    "वेखियां बाग़ बहारां होर (I beheld sublime gardens of eternal spring),",
                    "हुन मैनूं कुझ ना कहणा (now speak no worldly words to me),",
                    "प्यारिआ सानूं मिट्ठड़ा ना लग्गदा शोर (worldly clamor no longer sounds sweet to us) ।"
                ],
                "poetic_hindi": [
                    "मेरे घर में खिला अनूठा फूल, देखी अलौकिक वसंत-बहार,",
                    "अब मुझे कुछ न कहो दुनियावालो, फीका लगा यह कोलाहल असार !",
                    "ऐ प्यारे, यह सांसारिक शोर अब मुझको मीठा नहीं लगता !"
                ],
                "poetic_english": [
                    "Within my soul a wondrous flower has opened fresh and fair;",
                    "I saw the eternal spring unfold beneath the heavenly air;",
                    "Speak no more worldly tales to me—their hollow echoes tire:",
                    "Worldly clamor no longer sounds sweet to us!"
                ]
            },
            {
                "original": [
                    "हुन मैं मोई नी मेरीए मां,  ",
                    "पूनी मेरी लै गया कां,  ",
                    "डो डो करदी मगरे जां,  ",
                    "पूनी दे दईं साईं दे नां,  ",
                    "प्यारिआ सानूं मिट्ठड़ा ना लग्गदा शोर ।"
                ],
                "hindi_gloss": [
                    "हुन (अब) मैं (मैं सांसारिक दृष्टि से) मोई (मर चुकी हूँ) नी (अरी) मेरीए (मेरी) मां (माँ),",
                    "पूनी (चरखे की सूत की पूनी) मेरी (मेरी) लै (लेकर) गया (उड़ गया है) कां (काल रूपी कौआ),",
                    "डो (हाथ हिला-हिलाकर) डो (उड़ाती) करदी (हुई मैं उसके) मगरे (पीछे-पीछे) जां (जाती हूँ),",
                    "पूनी (परंतु फिर कहती हूँ: यह पूनी भी) दे (दे) दईं (दी मैंने अपने) साईं (सच्चे स्वामी) दे (के) नां (नाम पर दान),",
                    "प्यारिआ (ऐ प्यारे) सानूं (मुझको) मिट्ठड़ा ना लग्गदा शोर (संसार का शोर मीठा नहीं लगता) ।"
                ],
                "english_gloss": [
                    "हुन मैं मोई नी मेरीए मां (now I am dead to the world, O mother mine),",
                    "पूनी मेरी लै गया कां (the crow of time has carried away my cotton roll),",
                    "डो डो करदी मगरे जां (shooing and running behind it I go),",
                    "पूनी दे दईं साईं दे नां (yet let the cotton roll be surrendered in the Master's Name),",
                    "प्यारिआ सानूं मिट्ठड़ा ना लग्गदा शोर (worldly clamor no longer sounds sweet to us) ।"
                ],
                "poetic_hindi": [
                    "संसार से मैं तो मर गई ओ माँ, पूनी ले उड़ा कौआ चपल,",
                    "पीछे-पीछे दौड़ी उड़ाने, फिर कह दिया: पूनी साहिब के नाम अर्पण !",
                    "ऐ प्यारे, यह सांसारिक शोर अब मुझको मीठा नहीं लगता !"
                ],
                "poetic_english": [
                    "Dead to the world am I, O mother! The crow flew with my yarn away;",
                    "I chased it shooing through the fields, then gave it to my Lord to stay!",
                    "Worldly clamor no longer sounds sweet to us!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा साईं दे नाल प्यार,  ",
                    "मेहर इनायत करे हज़ार,  ",
                    "इहो कौल ते इहो करार,  ",
                    "दिलबर दे विच रहणा,  ",
                    "प्यारिआ सानूं मिट्ठड़ा ना लग्गदा शोर ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ले शाह कहते हैं) साईं (परमेश्वर/मुर्शिद) दे (के) नाल (साथ मेरा सच्चा) प्यार (प्रेम स्थापित हो गया है),",
                    "मेहर (अपनी अपार कृपा हज़रत शाह) इनायत (इनायत मुझ पर) करे (करते हैं) हज़ार (हजारों बार),",
                    "इहो (यही मेरा पक्का) कौल (वचन है) ते (और) इहो (यही अटल) करार (प्रण है कि),",
                    "दिलबर (सदा अपने प्यारे प्रियतम) दे (के) विच (भीतर ही) रहणा (रहना है),",
                    "प्यारिआ (ऐ प्यारे) सानूं (मुझको यह) मिट्ठड़ा (मीठा) ना (नहीं) लग्गदा (लगता) शोर (संसार का व्यर्थ शोर) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा साईं दे नाल प्यार (Bulleh: my love is bound with the Sovereign Lord),",
                    "मेहर इनायत करे हज़ार (Shah Inayat showers thousands of mercies),",
                    "इहो कौल ते इहो करार (this is the sole covenant and solemn pledge),",
                    "दिलबर दे विच रहणा (to abide forever within the Beloved),",
                    "प्यारिआ सानूं मिट्ठड़ा ना लग्गदा शोर (worldly clamor no longer sounds sweet to us) ।"
                ],
                "poetic_hindi": [
                    "बुल्ला कहे: साहिब संग प्यार, शाह इनायत की मेहर हज़ार,",
                    "यही वचन और यही प्रण है: दिलबर में रहना निरंतर यार !",
                    "ऐ प्यारे, यह सांसारिक शोर अब मुझको मीठा नहीं लगता !"
                ],
                "poetic_english": [
                    "Says Bulleh: Pledged unto the Lord, Shah Inayat pours His grace divine;",
                    "This is my vow, this is my pledge: to dwell within that Heart of mine!",
                    "Worldly clamor no longer sounds sweet to us!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी सूफी साधना की उस अवस्था को दर्शाती है जिसे 'खलवत दर अंजुमन' (भीड़ में एकांत) और 'सुकूत' (आंतरिक मौन) कहा जाता है। जब साधक के हृदय में परमात्मा के प्रेम का पुष्प ('शगूफा') खिल जाता है, तो बाहरी दुनिया के तर्क-वितर्क, निंदा-स्तुति और विवाद केवल व्यर्थ का शोर प्रतीत होते हैं। 'पूनी लै गया कां' सांसारिक जीवन और सांसों के छीने जाने का रूपक है; सच्चा साधक घबराने के बजाय अपनी समस्त हस्ती को 'साईं दे नां' (ईश्वर के चरणों में) समर्पित कर देता है। हज़रत शाह इनायत कादरी की कृपा से आत्मा प्रियतम के हृदय में शाश्वत विश्राम पाती है।"
    },
    {
        "id": 124,
        "title": "पिया पिया करते हमीं पिया हुए, अब पिया किस नूं कहीए",
        "title_english": "Repeating 'Pia, Pia!', I Myself Became the Beloved: Whom Shall I Call 'Pia' Now?",
        "historical_context": "यह 3 बंधों की एक अत्यंत प्रसिद्ध, अद्वैतवादी और रससिद्ध काफी है। इसमें सूफी फना-फिल-हक का वह अनुभव व्यक्त हुआ है जो बुल्ले शाह की प्रसिद्ध काफी 'रांझा रांझा करदी नी मैं आपे रांझा होई' में दिखाई देता है। प्रियतम का निरंतर ध्यान और नाम-जप करते-करते साधक का अपना अस्तित्व पूरी तरह मिट जाता है और वह स्वयं 'पिया' (प्रियतम) बन जाता है। इस अवस्था में विरह ('हिज्र') और मिलन ('विसाल') दोनों की द्वैतवादी सीमाएं समाप्त हो जाती हैं। मजनू की भांति साधक स्वयं लैला बन जाता है।",
        "meter": "पंजाबी-सधुक्कड़ी मिश्रित काफी (मात्रािक छंद)",
        "raga": "राग काफी / बिलावल / दरबारी",
        "theme": "अद्वैत (वहदत-उल-वुजूद), आत्म-विलय, हिज्र व विसाल से परे, मजनू का लैला में रूपांतरण",
        "stanzas": [
            {
                "original": [
                    "पिया पिया करते हमीं पिया हुए, अब पिया किस नूं कहीए ।"
                ],
                "hindi_gloss": [
                    "पिया (प्रियतम) पिया ('पिया-पिया') करते (पुकारते-पुकारते) हमीं (हम स्वयं ही) पिया (प्रियतम) हुए (हो गए हैं), अब (अब भला हम) पिया (प्रियतम) किस (किस दूसरे) नूं (को) कहीए (संबोधित करें) ।"
                ],
                "english_gloss": [
                    "पिया पिया करते (chanting 'Beloved, Beloved!') हमीं पिया हुए (I myself have become the Beloved), अब पिया किस नूं कहीए (unto whom now shall I call 'Beloved') ।"
                ],
                "poetic_hindi": [
                    "'पिया-पिया' जपते-जपते हम स्वयं ही पिया हो गए,",
                    "अब किस दूजे को हम पिया कह कर पुकारें भला?"
                ],
                "poetic_english": [
                    "Chanting 'Beloved, Beloved!', I myself became the Beloved whole;",
                    "Whom shall I summon as Beloved now, when Oneness claims my soul?"
                ]
            },
            {
                "original": [
                    "हजर वसल हम दोनों छोड़े, अब किस के हो रहीए ।  ",
                    "पिया पिया करते हमीं पिया हुए ।"
                ],
                "hindi_gloss": [
                    "हजर (वियोग/विरह) वसल (और मिलन के) हम (हमने) दोनों (दोनों ही द्वैतवादी छोर) छोड़े (त्याग दिए हैं), अब (अब हम) किस (किस दूसरे) के (के) हो (होकर) रहीए (रहें भला) ।",
                    "पिया (पिया) पिया (पिया) करते (करते) हमीं (हम ही) पिया (पिया) हुए (हो गए) ।"
                ],
                "english_gloss": [
                    "हजर वसल हम दोनों छोड़े (we have discarded both separation and union), अब किस के हो रहीए (unto whom now shall we belong),",
                    "पिया पिया करते हमीं पिया हुए (chanting 'Beloved, Beloved!' I myself became the Beloved) ।"
                ],
                "poetic_hindi": [
                    "विरह और मिलन दोनों छूटे, द्वैत का हर इक पर्दा टूटा,",
                    "किसके होकर रहें अब हम, जब अपना ही आपा छूटा !",
                    "'पिया-पिया' जपते-जपते हम स्वयं पिया हो गए !"
                ],
                "poetic_english": [
                    "Both parting and communion have we cast away in light;",
                    "Unto whom can we belong, when all duality dissolves from sight?",
                    "Chanting 'Beloved, Beloved!', I myself became the Beloved whole!"
                ]
            },
            {
                "original": [
                    "मजनूं लाल दीवाने वांङू, अब लैला हो रहीए ।  ",
                    "पिया पिया करते हमीं पिया हुए ।"
                ],
                "hindi_gloss": [
                    "मजनूं (मजनू) लाल (प्यारे) दीवाने (दीवाने की) वांङू (भांति), अब (अब हम स्वयं ही) लैला (लैला) हो (होकर) रहीए (जी रहे हैं) ।",
                    "पिया (पिया) पिया (पिया) करते (करते) हमीं (हम ही) पिया (पिया) हुए (हो गए) ।"
                ],
                "english_gloss": [
                    "मजनूं लाल दीवाने वांङू (like the ecstatic, crazed lover Majnun), अब लैला हो रहीए (now have we become Laila herself),",
                    "पिया पिया करते हमीं पिया हुए (chanting 'Beloved, Beloved!' I myself became the Beloved) ।"
                ],
                "poetic_hindi": [
                    "मजनू जैसे दीवाने की तरह, अब हम ही लैला बन बैठे,",
                    "मिट गई दूरी, मिटा फासला, प्रेम-सिंधु में जा पैठे !",
                    "'पिया-पिया' जपते-जपते हम स्वयं पिया हो गए !"
                ],
                "poetic_english": [
                    "Like crazed Majnun in desert sands, we have turned into Laila now;",
                    "No boundary separates the two, one crown upon the brow!",
                    "Chanting 'Beloved, Beloved!', I myself became the Beloved whole!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु घर मेरे आए, अब क्युं ताअने सहीए ।  ",
                    "पिया पिया करते हमीं पिया हुए, अब पिया किस नूं कहीए ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ले शाह कहते हैं) शहु (साक्षात् परमात्मा/सद्गुरु) घर (हृदय-गृह) मेरे (मेरे) आए (पधार चुके हैं), अब (अब हम संसार के झूठे) क्युं (क्यों) ताअने (ताने और व्यंग्य) सहीए (सहन करें) ।",
                    "पिया (पिया) पिया (पिया) करते (करते) हमीं (हम ही) पिया (पिया) हुए (हो गए), अब (अब) पिया (पिया) किस (किस) नूं (को) कहीए (कहें) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा शहु घर मेरे आए (Bulleh: the Sovereign Lord has entered my home), अब क्युं ताअने सहीए (why should we endure worldly taunts now),",
                    "पिया पिया करते हमीं पिया हुए (chanting 'Beloved, Beloved!' I myself became the Beloved), अब पिया किस नूं कहीए (whom shall I address as Beloved now) ।"
                ],
                "poetic_hindi": [
                    "बुल्ला कहे: साहिब घर आए, जग के ताने क्यों सहिए?",
                    "एक हुए जब प्रेमी-प्रियतम, अब किसको क्या कहिए?",
                    "'पिया-पिया' जपते-जपते हम स्वयं ही पिया हो गए !"
                ],
                "poetic_english": [
                    "Says Bulleh: The Sovereign King has entered my humble home;",
                    "Why heed the bitter taunts of folk, why longer weep and roam?",
                    "Chanting 'Beloved, Beloved!', I myself became the Beloved whole;",
                    "Whom shall I summon as Beloved now, when Oneness claims my soul?"
                ]
            }
        ],
        "sufi_commentary": "यह काफी भारतीय अद्वैत वेदांत के 'अयमात्मा ब्रह्म' (यह आत्मा ही ब्रह्म है) और सूफी तसव्वुफ के 'फना-फिल-महबूब' का सर्वोच्च काव्य-रूप है। जब साधक का अहं पूर्णतः समाप्त हो जाता है, तो 'मैं' और 'तू' का द्वैत मिट जाता है। सूफी कथाओं में आता है कि जब मजनू से किसी ने पूछा कि तू कौन है, तो उसने उत्तर दिया: 'अना लैला' (मैं ही लैला हूँ)। जब परमात्मा साधक के हृदय-गृह में आ जाता है, तो विरह और मिलन दोनों की अवधारणाएं अप्रासंगिक हो जाती हैं क्योंकि मिलन के लिए दो का होना आवश्यक है, और यहाँ केवल एक ही अखंड सत्ता विद्यमान है।"
    },
    {
        "id": 125,
        "title": "रातीं जागें करें इबादत",
        "title_english": "Thou Keepest Vigil at Night in Worship: At Night Dogs Keep Vigil Too—They Are Far Above Thee!",
        "historical_context": "यह 4 बंधों की बाबा बुल्ले शाह की सर्वाधिक प्रसिद्ध, क्रांतिकारी, लोक-प्रचलित और मर्मभेदी काफ़ियों में से एक है। इसमें बुल्ले शाह उन तथाकथित धर्मपरायण साधकों और मुल्लाओं के अहंकार को मिट्टी में मिला देते हैं जो रात-रात भर जागकर नमाज़ या पूजा करने का दंभ भरते हैं। बुल्ला उनकी तुलना गली के कुत्ते से करते हैं: कुत्ता रात भर जागता है, कूड़े के ढेर ('रूड़ी') पर सोता है, और मालिक चाहे उसे जूतों से मारे, वह कभी मालिक का द्वार छोड़कर नहीं भागता। बुल्ला चेतावनी देते हैं कि यदि तुमने अपने भीतर कुत्ते जैसी वफादारी, निष्कपटता और समर्पण का 'रख़्त' (सामग्री) नहीं कमाया, तो यह बाज़ी कुत्ते जीत ले जाएँगे और वे तुमसे कहीं ऊँचे सिद्ध होंगे!",
        "meter": "पंजाबी काफी (मात्रािक छंद, धुन: रातीं जागें करें इबादत)",
        "raga": "राग काफी / बिलावल / पहाड़ी",
        "theme": "धार्मिक दंभ का मर्दन, कुत्ते की निष्ठा और वफादारी, समर्पण की पराकाष्ठा, निस्वार्थ प्रेम",
        "stanzas": [
            {
                "original": [
                    "रातीं जागें करें इबादत,  ",
                    "रातीं जागन कुत्ते ।  ",
                    "तैथों उते ।"
                ],
                "hindi_gloss": [
                    "रातीं (तू रातों में) जागें (जाग-जाग कर) करें (करता है) इबादत (पूजा और नमाज़ का दिखावा),",
                    "रातीं (परंतु रातों में तो) जागन (जागते रहते हैं गली के) कुत्ते (कुत्ते भी),",
                    "तैथों (वे कुत्ते निष्ठा में तुझसे) उते (कहीं श्रेष्ठ और ऊँचे हैं) ।"
                ],
                "english_gloss": [
                    "रातीं जागें करें इबादत (thou wakest at night to perform ritual worship),",
                    "रातीं जागन कुत्ते (at night dogs keep wakeful vigil too),",
                    "तैथों उते (they are far above thee!) ।"
                ],
                "poetic_hindi": [
                    "रात-रात भर जाग कर करता तू इबादत का अभिमान,",
                    "रात-रात भर जागते कुत्ते, तुझसे ऊँचे उनकी शान !"
                ],
                "poetic_english": [
                    "Thou keepest vigil all the night to boast of prayer and grace;",
                    "At night the watchdogs keep their watch—they hold a higher place!"
                ]
            },
            {
                "original": [
                    "भौंकणों बन्द मूल ना हुन्दे,  ",
                    "जा रूड़ी ते सुत्ते ।  ",
                    "तैथों उते ।"
                ],
                "hindi_gloss": [
                    "भौंकणों (मालिक के द्वार की रक्षा में सतर्क रहने से) बन्द (बंद) मूल (तनिक भी) ना (नहीं) हुन्दे (होते),",
                    "जा (और थकने पर जाकर) रूड़ी (कूड़े के ढेर) ते (पर संतोष से) सुत्ते (सो जाते हैं, कोई महल नहीं मांगते),",
                    "तैथों (वे कुत्ते तुझ दंभी मनुष्य से) उते (कहीं ऊँचे हैं) ।"
                ],
                "english_gloss": [
                    "भौंकणों बन्द मूल ना हुन्दे (they never cease barking in faithful watch),",
                    "जा रूड़ी ते सुत्ते (and go to sleep contented upon the dung-heap),",
                    "तैथों उते (they are far above thee!) ।"
                ],
                "poetic_hindi": [
                    "मालिक की रखवाली में भौंकते, पल भर न बंद होते,",
                    "कूड़े की ढेरी पर जाकर संतोष की नींद हैं सोते !",
                    "तुझसे ऊँचे कुत्ते !"
                ],
                "poetic_english": [
                    "They never cease their vigilant bark to guard their master's keep;",
                    "Upon the garbage heap content, they curl themselves to sleep!",
                    "They are far above thee!"
                ]
            },
            {
                "original": [
                    "ख़सम आपने दा दर ना छड्डदे,  ",
                    "भावें वज्जन जुत्ते ।  ",
                    "तैथों उते ।"
                ],
                "hindi_gloss": [
                    "ख़सम (स्वामी/मालिक) आपने (अपने) दा (का) दर (द्वार वे कभी) ना (नहीं) छड्डदे (छोड़कर भागते),",
                    "भावें (चाहे मालिक के हाथों उनके सिर पर) वज्जन (पड़ते रहें) जुत्ते (जूते और डंडे),",
                    "तैथों (वे निष्ठावान कुत्ते तुझसे) उते (कहीं ऊँचे हैं) ।"
                ],
                "english_gloss": [
                    "ख़सम आपने दा दर ना छड्डदे (they never abandon their master's threshold),",
                    "भावें वज्जन जुत्ते (even though beaten with shoes and sticks),",
                    "तैथों उते (they are far above thee!) ।"
                ],
                "poetic_hindi": [
                    "मालिक का दर कभी न छोड़ें, चाहे जूतियां बरसें सिर पे,",
                    "द्वार पे पड़े रहें निष्ठा से, कभी न भागें द्वारे से !",
                    "तुझसे ऊँचे कुत्ते !"
                ],
                "poetic_english": [
                    "They never leave their master's door, though beaten with old shoes;",
                    "Unshaken in their loyalty, no other hearth they choose!",
                    "They are far above thee!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हे शाह कोई रख़त वेहाज लै,  ",
                    "नहीं ते बाज़ी लै गए कुत्ते ।  ",
                    "तैथों उते ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हे शाह (बुल्ले शाह कहते हैं कि ऐ मन, तू भी ऐसी वफादारी और प्रेम का) कोई (कोई) रख़त (सामग्री/पूंजी) वेहाज (खरीद/अर्जित) लै (ले),",
                    "नहीं (अन्यथा परमात्मा के दरबार में यह समर्पण की) ते (तो) बाज़ी (बाजी) लै गए (जीत ले जाएँगे ये निष्कपट) कुत्ते (कुत्ते),",
                    "तैथों (और वे सदा सिद्ध होंगे तुझसे) उते (कहीं श्रेष्ठ और ऊँचे) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हे शाह कोई रख़त वेहाज लै (Bulleh Shah: purchase some true provision of selfless devotion),",
                    "नहीं ते बाज़ी लै गए कुत्ते (otherwise the dogs will win the game of Love),",
                    "तैथों उते (they will stand far above thee!) ।"
                ],
                "poetic_hindi": [
                    "बुल्ले शाह: कुछ प्रेम-पूंजी कमा ले, सच्ची वफ़ा का सौदा कर,",
                    "वरना बाज़ी मार ले जाएँगे कुत्ते, रह जाएगा तू खाली हाथ अधर !",
                    "तुझसे ऊँचे उनकी शान !"
                ],
                "poetic_english": [
                    "Bulleh Shah: Buy some true treasure of selfless faith and love divine;",
                    "Or else the faithful dogs will win, while empty hands are thine!",
                    "They are far above thee!"
                ]
            }
        ],
        "sufi_commentary": "यह काफी सूफी साहित्य की सबसे साहसिक और अमर कविताओं में से एक है। इसमें बुल्ले शाह धार्मिक कर्मकांडों के अहंकार को चूर-चूर कर देते हैं। रात की इबादत (तहज्जुद की नमाज़) पर गर्व करने वाले को वे दिखाते हैं कि केवल जागना ही आध्यात्मिकता नहीं है; जागना तो कुत्ता भी जानता है। कुत्ते में तीन ऐसे गुण हैं जो साधक में होने चाहिए: 1. वह निरंतर अपने मालिक के प्रति सतर्क रहता है, 2. वह रूड़ी (कूड़े के ढेर) पर सोकर परम संतोष और त्याग का जीवन जीता है, और 3. मालिक चाहे उसे कितना भी प्रताड़ित करे, वह कभी उसका द्वार छोड़कर किसी अन्य के द्वार पर नहीं जाता। यदि मनुष्य में अपने ईश्वर के प्रति कुत्ते जैसी वफादारी और अनन्य निष्ठा नहीं है, तो उसकी सारी इबादत व्यर्थ है।"
    }
]

new_lexicon_terms = {
    "मसल्हत": {"hindi": "परामर्श, सम्मति, विचार-विमर्श, पूर्व सूचना", "english": "consultation, counsel, prior agreement"},
    "चावड़": {"hindi": "उछल-कूद, अहंकार भरा विलास, मस्ती", "english": "boisterous revelry, arrogant sport"},
    "शहर-खामोशां": {"hindi": "खामोशों का नगर, कब्रिस्तान, श्मशान", "english": "the City of the Silent, the graveyard/cemetery"},
    "मुहाना": {"hindi": "मल्लाह, केवट, नाव चलाने वाला", "english": "boatman, ferryman"},
    "शगूफा": {"hindi": "कली, नया खिला हुआ फूल; सूफी रूपक में: नया आध्यात्मिक अनुभव", "english": "blossom, bud, flowering of mystic consciousness"},
    "पूनी": {"hindi": "चरखे पर कातने के लिए तैयार की गई रुई की बत्ती", "english": "cotton sliver/roll prepared for spinning"},
    "हजर": {"hindi": "वियोग, विरह, जुदाई (हिज्र)", "english": "Hijr, separation from the Beloved"},
    "रूड़ी": {"hindi": "कूड़े-कचरे का ढेर, खाद का ढेर", "english": "dunghill, garbage heap, refuse pile"},
    "रख़त": {"hindi": "यात्रा की सामग्री, आध्यात्मिक पूंजी, संचित साधन", "english": "rakht, provisions/equipment for the journey"},
    "वेहाज": {"hindi": "खरीदना, सौदा करना, अर्जित करना", "english": "to purchase, acquire, trade for"}
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
        "completed_count": 125,
        "total": 160,
        "next_kafi_id": 126,
        "last_updated": "2026-10-17T19:25:00+05:30",
        "last_batch": "121-125",
        "status": "in_progress",
        "milestone": "125/160 (78.125%) finished."
    }
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print(f"Checkpoint updated: 125/160 completed. Next ID: 126")

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
