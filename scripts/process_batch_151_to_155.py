"""
Process Batch 151 to 155 of Bulleh Shah's Kafian.
Kafi 151: उट्ठ गए गवांढों यार (The Beloved Has Departed from the Neighborhood)
Kafi 152: उट्ठ जाग घुराड़े मार नहीं (Arise, Awake! Snore Not in Slumber!)
Kafi 153: वेखो नी कर गया माही (Behold, What My Herdsman Has Done!)
Kafi 154: वेखो नी प्यारा मैनूं सुफने में छल गया (Behold, the Beloved Beguiled Me in a Dream)
Kafi 155: वेखो नी शहु इनायत साईं (Behold the Play of Master Shah Inayat!)
"""

import json
import os

DATA_DIR = os.path.abspath("c:/my-code/Bulleh-Shah/data")
KAFIAN_DIR = os.path.join(DATA_DIR, "kafian")
LEXICON_PATH = os.path.join(DATA_DIR, "punjabi_sufi_lexicon.json")
CHECKPOINT_PATH = os.path.join(DATA_DIR, "checkpoint.json")

batch_kafian = [
    {
        "id": 151,
        "title_punjabi": "उट्ठ गए गवांढों यार",
        "title_english": "The Beloved Has Departed from the Neighborhood",
        "raga": "Raga Marwa / Kafi",
        "meter": "Matrik Chhand (16-12 matras)",
        "theme": "The Desolation of the Beloved's Departure and the Searing Fire of Separation",
        "historical_context": "Composed when Murshid Shah Inayat was compelled to relocate or when distance arose between Bulleh Shah and his master. The departure of the Beloved's caravan from the immediate vicinity leaves the seeker suspended between worlds ('रहे उरार ना पार'), burning in the inner furnace of separation.",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "उट्ठ गए गवांढों यार,  ",
                    "रब्बा हुन की करीए ?"
                ],
                "hindi_gloss": "उट्ठ गए (कूच कर गए/चले गए) गवांढों (पड़ोस/निकट से) यार (मेरे प्रियतम), रब्बा (हे प्रभु/ईश्वर!) हुन (अब) की करीए (क्या करें/कहाँ जाएं?)।",
                "english_gloss": "उट्ठ गए (Have departed) गवांढों (from the neighborhood) यार (my Beloved Friend), रब्बा (O Lord!) हुन की करीए (what now shall I do?).",
                "poetic_hindi": "पड़ोस से उठ गए यार प्यारे,\nहे रब! अब क्या करें सहारे?",
                "poetic_english": "From my close doors my Love has flown;\nO Lord, what shall I do, alone?"
            },
            {
                "stanza_number": 2,
                "original": [
                    "उट्ठ गए हुन बहन्दे नाहीं,होया साथ त्यार,  ",
                    "रब्बा हुन की करीए ?"
                ],
                "hindi_gloss": "उट्ठ गए (वे कूच कर गए) हुन (अब) बहन्दे नाहीं (रुकते या बैठते नहीं), होया (हो चुका है) साथ (काफिला/संगी-साथी) त्यार (प्रस्थान को तैयार), रब्बा हुन की करीए ?",
                "english_gloss": "उट्ठ गए हुन (They have departed now) बहन्दे नाहीं (they linger or sit no more), होया साथ त्यार (their caravan is fully prepared and set forth), रब्बा हुन की करीए ?",
                "poetic_hindi": "चल दिए अब वो रुकते नाहीं, काफिला तैयार माहीं;\nहे रब! अब क्या करें सहारे?",
                "poetic_english": "They linger not, they pause no more; their caravan has left the shore;\nO Lord, what shall I do, alone?"
            },
            {
                "stanza_number": 3,
                "original": [
                    "दाढ कलेजे बल बल उठदी, भड़के बिरहों नार,  ",
                    "रब्बा हुन की करीए ?"
                ],
                "hindi_gloss": "दाढ (प्रचंड पीड़ा/दाह) कलेजे (हृदय में) बल बल उठदी (सुलग-सुलग कर धधक रही है), भड़के (भड़क उठी है) बिरहों (विरह की) नार (प्रचंड आग), रब्बा हुन की करीए ?",
                "english_gloss": "दाढ कलेजे (A searing flame in the breast) बल बल उठदी (flares up incessantly), भड़के बिरहों नार (separation's raging fire blazes high), रब्बा हुन की करीए ?",
                "poetic_hindi": "कलेजे में दावानल जागे, विरह-अग्नि भड़क कर भागे;\nहे रब! अब क्या करें सहारे?",
                "poetic_english": "Within my heart a furnace glows; the fire of grief and parting blows;\nO Lord, what shall I do, alone?"
            },
            {
                "stanza_number": 4,
                "original": [
                    "बुल्ल्हा शहु प्यारे बाझों रहे उरार ना पार,  ",
                    "रब्बा हुन की करीए ?"
                ],
                "hindi_gloss": "बुल्ल्हा (बुल्लेशाह कहता है) शहु प्यारे बाझों (उस प्यारे प्रभु-प्रियतम के बिना), रहे (हम रह गए हैं) उरार (न इस किनारे के) ना पार (न उस पार के), रब्बा हुन की करीए ?",
                "english_gloss": "बुल्ल्हा शहु प्यारे बाझों (Bulleh cries: without the beloved Sovereign Master), रहे उरार ना पार (we are stranded neither on this bank nor on the far shore), रब्बा हुन की करीए ?",
                "poetic_hindi": "बुल्ल्हा कहे, पिया बिन प्यारे, न इस पार रहे, न उस द्वारे;\nहे रब! अब क्या करें सहारे?",
                "poetic_english": "Bulleh cries: without that Master grand, neither on near nor far shore I stand;\nO Lord, what shall I do, alone?"
            }
        ],
        "sufi_commentary": "Kafi 151 expresses the terrifying desolation of the sudden spiritual void (Qabd). In Sufi pathwork, the physical or spiritual presence of the Kamil Murshid (Perfect Master) is the anchor of the disciple's universe. When the Beloved's caravan departs ('उट्ठ गए गवांढों यार'), the heart feels completely abandoned. The soul is caught in the existential no-man's-land: 'रहे उरार ना पार'—it has already renounced the worldly shore ('उरार'), yet has not achieved permanent union on the transcendent shore ('पार'). In this searing limbo, the fire of separation ('बिरहों नार') burns away the remaining dross of selfhood."
    },
    {
        "id": 152,
        "title_punjabi": "उट्ठ जाग घुराड़े मार नहीं",
        "title_english": "Arise, Awake! Snore Not in Slumber!",
        "raga": "Raga Bhairav / Asavari",
        "meter": "Hazaj / Baint (14-14 matras)",
        "theme": "The Grand Memento Mori: Impermanence, Historical Ruin, and Spiritual Vigilance",
        "historical_context": "One of Bulleh Shah's most magnificent and expansive compositions (20 stanzas). A monumental sermon on mortality, transience, and the spiritual dowry. Bulleh invokes the tragic march of world history: Alexander the Great (Sikandar), King Solomon with his flying throne (Takht-i Suleman), Prophet Yusuf and Zulaikha, emperors, conquerors, fragrant gardens—all turned to dust under the autumn wind of Death (Bad-i Khazan). He warns the human soul that no second chance is granted in the arena of existence ('फेर आवन दूजी वार नहीं').",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "उट्ठ जाग घुराड़े मार नहीं ।  ",
                    "इह सौन तेरे दरकार नहीं ।"
                ],
                "hindi_gloss": "उट्ठ (उठ) जाग (जाग जा), घुराड़े (खर्राटे) मार नहीं (मत भर/असावधान मत सो)। इह (यह प्रमादपूर्ण) सौन (सोना) तेरे (तेरे लिए) दरकार (उचित/हितकर) नहीं (नहीं है)।",
                "english_gloss": "उट्ठ जाग (Arise, awake!) घुराड़े मार नहीं (snore not in heedless slumber!). इह सौन (This deep sleep) तेरे दरकार नहीं (is not what befits thy soul).",
                "poetic_hindi": "उठ जाग! खर्राटे मार नहीं,\nये सोना तेरे दरकार नहीं!",
                "poetic_english": "Arise, awake! Snore not in sleep so deep!\nSuch heedless rest thy soul must never keep!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "इक रोज़ जहानों जाना ए जा कबरे विच समाना ए,  ",
                    "तेरा गोशत कीड़िआं खाना ए कर चेता मरग विसार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "इक रोज़ (एक दिन) जहानों (संसार से) जाना ए (प्रस्थान करना है), जा (जाकर) कबरे विच (कब्र की मिट्टी में) समाना ए (समा जाना है), तेरा (तेरा यह सुंदर) गोशत (मांस) कीड़िआं (कीड़े-मकोड़ों ने) खाना ए (खा जाना है), कर चेता (स्मरण रख) मरग (मृत्यु को) विसार नहीं (भूल मत जाना), उट्ठ जाग घुराड़े मार नहीं ।",
                "english_gloss": "इक रोज़ (One day) जहानों जाना ए (thou must depart from this world), जा कबरे विच समाना ए (and enter into the grave), तेरा गोशत (thy flesh) कीड़िआं खाना ए (worms and insects shall devour), कर चेता (remember ever) मरग विसार नहीं (forget not thy mortal end), उट्ठ जाग घुराड़े मार नहीं ।",
                "poetic_hindi": "इक दिन जग से है जाना रे, कब्र के भीतर समाना रे;\nकीड़े खाएँगे मांस तेरा, मत भूल मृत्यु, चेत सवेरा!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "One day from this earth you must surely depart, into the cold grave to lay down your heart;\nWorms shall devour your flesh and your art; remember your death ere life's threads dispart!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "तेरा साहा नेड़े आया ए कुझ्झ चोली दाज रंगाइआ ए,  ",
                    "क्युं आपना आप वंजाइआ ए ऐ ग़ाफ़ल तैनूं सार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "तेरा (तेरा) साहा (विवाह का लग्न/मृत्यु का निश्चित मुहूर्त) नेड़े (अत्यंत निकट) आया ए (आ चुका है), कुझ्झ (क्या तूने कुछ) चोली (चोली/वस्त्र और) दाज (परलोक का दहेज) रंगाइआ ए (रंग कर तैयार किया है?), क्युं (क्यों) आपना आप (अपना अमूल्य आत्म-स्वरूप) वंजाइआ ए (व्यर्थ गँवा दिया?), ऐ ग़ाफ़ल (हे बेखबर जीव!) तैनूं (तुझे कोई) सार (सुध-बुध) नहीं (नहीं है)।",
                "english_gloss": "तेरा साहा (The nuptial hour of thy departure) नेड़े आया ए (has drawn near), कुझ्झ चोली दाज रंगाइआ ए (hast thou dyed any spiritual robe or dowry?), क्युं आपना आप वंजाइआ ए (why hast thou squandered thy very soul?), ऐ ग़ाफ़ल (O heedless one!) तैनूं सार नहीं (thou hast no realization whatsoever).",
                "poetic_hindi": "लगन का दिन अति निकट आया, क्या दहेज़ तूने रंगवाया?\nक्यों व्यर्थ ये जीवन गँवाया? ग़ाफ़िल! तुझे कुछ सार नहीं!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "The nuptial hour of death draws near; have you dyed the bridal robes you'll wear?\nWhy squander yourself in empty care? O heedless soul, you are not aware!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "तूं सुत्त्यां उमर वंजाई ए तूं चरखे तन्द ना पाई ए,  ",
                    "की करसें दाज त्यार नहीं, उट्ठ जाग घुराड़े मार नहीं ।  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "तूं (तूने) सुत्त्यां (सोते-सोते ही) उमर (सम्पूर्ण आयु) वंजाई ए (गँवा दी है), तूं (तूने) चरखे (नाम-स्मरण के चरखे पर) तन्द (सद्कर्मों का एक धागा भी) ना पाई ए (नहीं काता), की करसें (वहाँ ससुराल में क्या करेगी जब) दाज (दहेज) त्यार नहीं (तैयार नहीं होगा?), उट्ठ जाग घुराड़े मार नहीं ।",
                "english_gloss": "तूं सुत्त्यां उमर वंजाई ए (Sleeping thou hast squandered all thy days), तूं चरखे तन्द ना पाई ए (thou didst not spin a single strand of devotion upon the wheel), की करसें (what wilt thou present when) दाज त्यार नहीं (thy dowry is not ready?), उट्ठ जाग घुराड़े मार नहीं ।",
                "poetic_hindi": "सोते-सोते जनम गँवाया, चरखे पे इक तंत न चढ़ाया;\nदहेज़ न हो तो क्या दिखलाए? उठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "Sleeping you let the years slip through; on the spinning wheel spun no thread true;\nWhat dowry will you show the King in view? Arise, awake! Snore not in sleep anew!"
            },
            {
                "stanza_number": 5,
                "original": [
                    "तूं जिस दिन जोबन मत्ती सैं, तूं नाल सईआं दे रत्ती सैं,  ",
                    "हो गाफल गल्लीं वत्ती सैं, इह भोरा तैनूं सार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "तूं जिस दिन (जिस समय) जोबन मत्ती सैं (यौवन के मद में मतवाली थी), तूं नाल सईआं दे (सखियों के संग) रत्ती सैं (मस्त और लीन थी), हो गाफल (लापरवाह होकर) गल्लीं वत्ती सैं (व्यर्थ बातों में दिन बिताती रही), इह भोरा (तनिक भी) तैनूं सार नहीं (तुझे मृत्यु की सुध न रही)।",
                "english_gloss": "तूं जिस दिन जोबन मत्ती सैं (When thou were drunk with the vanity of youth), तूं नाल सईआं दे रत्ती सैं (reveling among thy worldly companions), हो गाफल गल्लीं वत्ती सैं (careless, gossiping the precious hours away), इह भोरा तैनूं सार नहीं (thou hadst not an ounce of spiritual awareness).",
                "poetic_hindi": "यौवन-मद में तू मतवाली, सखियों संग रमती लाली;\nबातों में गँवाई थाली, तनिक तुझे सुध-सार नहीं!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "Intoxicated in youth's bright flair, merry with companions free of care;\nWasting your breath in gossip's snare, you never saw the final stair!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 6,
                "original": [
                    "तूं मुढ्ढों बहुत कुचज्जी सैं, निरलज्ज्यां दी निरलज्जी सैं,  ",
                    "तूं खा खा खाने रज्जी सैं, हुन ताईं तेरा बार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "तूं (तू) मुढ्ढों (आरम्भ से ही) बहुत कुचज्जी सैं (अत्यंत गुणहीन और फूहड़ रही), निरलज्ज्यां दी (निर्लज्जों में भी) निरलज्जी सैं (परम निर्लज्ज बनी रही), तूं खा खा खाने (तरह-तरह के स्वादिष्ट भोजन खा-खाकर) रज्जी सैं (पेट भरती रही), हुन ताईं (अब तक) तेरा बार (तेरा कोई उद्धार/पार) नहीं, उट्ठ जाग घुराड़े मार नहीं ।",
                "english_gloss": "तूं मुढ्ढों बहुत कुचज्जी सैं (From the beginning thou wert clumsy and uncultivated), निरलज्ज्यां दी निरलज्जी सैं (shameless among the shameless), तूं खा खा खाने रज्जी सैं (feasting and stuffing thyself with fine delicacies), हुन ताईं तेरा बार नहीं (even now there is no limit to thy greed/folly).",
                "poetic_hindi": "आदि से ही तू रही कुचज्जी, बेशर्मों में परम निर्लज्जी;\nस्वादों में बस पेट भरी री, अब भी पापों का अंत नहीं!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "From the very start uncouth and vain, shameless amid the worldly train;\nFeasting on dainties again and again, with no end to your greedy chain!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 7,
                "original": [
                    "अज्ज कल्ल्ह तेरा मुक्कलावा ए क्युं सुत्ती कर कर दाअवा ए ?  ",
                    "अनडिठ्यां नाल मिलावा ए इह भलके गरम बज़ार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "अज्ज कल्ल्ह (आज या कल में ही) तेरा मुक्कलावा ए (तेरी विदाई/गौना होने वाला है), क्युं सुत्ती (क्यों सोई पड़ी है) कर कर दाअवा ए (झूठे दावे और दंभ करके?), अनडिठ्यां नाल (उस अनदेखे परमेश्वर के सम्मुख) मिलावा ए (तेरी भेंट होनी है), इह भलके (कल प्रातः यह) गरम बज़ार नहीं (संसार का यह चहल-पहल भरा बाजार नहीं रहेगा)।",
                "english_gloss": "अज्ज कल्ल्ह (Today or tomorrow) तेरा मुक्कलावा ए (thy final consummation and departure looms), क्युं सुत्ती (why sleepest thou) कर कर दाअवा ए (boasting with loud pretensions?), अनडिठ्यां नाल मिलावा ए (thy union is with the Unseen Lord), इह भलके गरम बज़ार नहीं (tomorrow this bustling worldly bazaar will vanish).",
                "poetic_hindi": "आज-कल में है मुकलावा, क्यों सोई कर-कर के दावा?\nअनदेखे से मिलना होगा, कल न रहेगा ये बाज़ार!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "Today or tomorrow your gauna will fall; why sleep with arrogant claims so tall?\nBefore the Unseen King you must crawl; tomorrow this bustling mart leaves all!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 8,
                "original": [
                    "तूं एस जहानों जाएंगी, फिर कदम ना एथे पाएंगी,  ",
                    "इह जोबन रूप वंजाएंगी, तैं रहना विच संसार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "तूं (तू) एस जहानों (इस संसार से) जाएंगी (चली जाएगी), फिर (पुनः कभी) कदम (अपने पाँव) ना एथे (यहाँ मर्त्यलोक में) पाएंगी (नहीं रखेगी), इह जोबन (यह सौंदर्य और यौवन) रूप (सब कुछ) वंजाएंगी (नष्ट हो जाएगा), तैं रहना (तुझे सदा नहीं रहना) विच संसार नहीं (इस संसार के भीतर)।",
                "english_gloss": "तूं एस जहानों जाएंगी (Thou wilt depart from this world), फिर कदम ना एथे पाएंगी (never again wilt thou set foot here), इह जोबन रूप वंजाएंगी (this youth and beauty thou shalt lose), तैं रहना विच संसार नहीं (thou art not destined to remain in this world).",
                "poetic_hindi": "इस जग से जब तू जाएगी, फिर लौट न यहाँ कभी आएगी;\nरूप-यौवन सब खोएगी, रहना नहीं संसार मझार!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "When from this earth your feet dispart, no more shall you walk upon this chart;\nYouth, beauty, grace will all depart; forever you leave this mortal mart!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 9,
                "original": [
                    "मंज़ल तेरी दूर दुराडी, तूं पौणां विच जंगल वादी,  ",
                    "औखा पहुंचन पैर प्यादी, दिसदी तूं असवार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "मंज़ल (अंतिम मंजिल) तेरी (तेरी) दूर दुराडी (अत्यंत दूर है), तूं पौणां (तुझे प्रस्थान करना है) विच जंगल वादी (भयानक बीहड़ जंगलों और घाटियों में), औखा (अति कठिन है) पहुंचन (वहाँ पहुँचना) पैर प्यादी (पैदल चलते हुए), दिसदी तूं (दिखाई देती तू) असवार नहीं (किसी साधन पर सवार नहीं है)।",
                "english_gloss": "मंज़ल तेरी दूर दुराडी (Thy destination is far, far distant), तूं पौणां विच जंगल वादी (thou must cross desolate wastes and perilous valleys), औखा पहुंचन पैर प्यादी (reaching on foot is nearly impossible), दिसदी तूं असवार नहीं (yet thou art not mounted upon any spiritual steed).",
                "poetic_hindi": "मंज़िल तेरी दूर-दुराडी, चलना जंगल और घाटी;\nकठिन है पहुँचना पैदल नारी, सवार तू तो दिखती नाहीं!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "Far is your goal on that unknown strand, through wild ravines and desert sand;\nImpossible on foot to reach that land, yet no winged charger at your command!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 10,
                "original": [
                    "इक इकल्ली तनहा चलसें, जंगल बरबर्र दे विच रुलसें,  ",
                    "लै लै तोशा इथों घलसें, उथे लैन उधार नहीं ।  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "इक इकल्ली (सर्वथा अकेली) तनहा (नितांत एकाकिनी) चलसें (तू चलेगी), जंगल बरबर्र दे विच (बीहड़ जंगल की झाड़ियों में) रुलसें (भटकेगी और तड़पेगी), लै लै (लेकर) तोशा (पुण्य-मार्ग का पाथेय/संबल) इथों (इसी संसार से) घलसें (आगे भेज ले), उथे (वहाँ परलोक में) लैन उधार नहीं (कोई उधार नहीं मिलता)।",
                "english_gloss": "इक इकल्ली तनहा चलसें (All solitary and alone thou shalt walk), जंगल बरबर्र दे विच रुलसें (stumbling through thorny wildernesses), लै लै तोशा इथों घलसें (prepare and send thy spiritual provisions from here), उथे लैन उधार नहीं (for there in that realm no credit or loan is given).",
                "poetic_hindi": "अकेली-तन्हा तू चलेगी, कंटीले जंगल में रुलगी;\nपाथेय यहीं से साथ ले जा, उधार वहाँ कुछ मिलता नाहीं!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "All alone you must make that solitary tread, through thorny wastes where wild beasts spread;\nPack provisions here ere life is shed, for no loans are lent among the dead!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 11,
                "original": [
                    "उह खाली ए सुंञ हवेली, तूं विच रहसें इक्क इकेली,  ",
                    "ओथे होसी होर ना बेली, साथ किसे दा बार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "उह (वह कब्र) खाली ए (सूनी और खाली) सुंञ हवेली (उजाड़ हवेली है), तूं (तू) विच (उसके भीतर) रहसें (रहेगी) इक्क इकेली (सर्वथा अकेली), ओथे (वहाँ) होसी (होगा) होर ना (अन्य कोई) बेली (सखा या मित्र), साथ (साथ निभाने वाला) किसे दा (किसी का भी) बार नहीं (कोई सहारा नहीं होगा)।",
                "english_gloss": "उह खाली ए सुंञ हवेली (That grave is an empty, desolate mansion), तूं विच रहसें इक्क इकेली (therein thou shalt abide utterly alone), ओथे होसी होर ना बेली (there shall be no other companion or friend), साथ किसे दा बार नहीं (none can share that solitary burden).",
                "poetic_hindi": "सूनी हवेली कब्र की भारी, अकेली रहेगी उसमें नारी;\nवहाँ न कोई संगी-साक्षी, साथ न देगा कोई परवारी!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "A hollow mansion is that quiet grave, where you must lie in a silent cave;\nNo kin or friend your soul can save, no earthly companion to make you brave!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 12,
                "original": [
                    "जेहड़े सन देसां दे राजे, नाल जिन्हां दे वज्जदे वाजे,  ",
                    "गए रो रो बेतखते ताजे, कोई दुनियां दा इतबार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "जेहड़े (जो) सन (थे) देसां दे राजे (विशाल देशों के चक्रवर्ती राजा), नाल जिन्हां दे (जिनके आगे) वज्जदे (बजते थे) वाजे (शाही नगाड़े और बाजे), गए (वे सब चले गए) रो रो (रो-रोकर) बेतखते ताजे (तख्त और ताज छोड़कर कंगाल होकर), कोई दुनियां दा इतबार नहीं (इस नश्वर संसार का कोई भरोसा नहीं)।",
                "english_gloss": "जेहड़े सन देसां दे राजे (Those who were kings of vast empires), नाल जिन्हां दे वज्जदे वाजे (before whom royal drums and trumpets sounded), गए रो रो (they departed weeping bitterly) बेतखते ताजे (stripped of their thrones and crowns), कोई दुनियां दा इतबार नहीं (there is no reliance to be placed on this world).",
                "poetic_hindi": "जो थे देशों के सुल्ताना, बजते जिनके आगे बाजा;\nतख्त-ताज तज रो-रो गए, जग का कोई ऐतबार नहीं!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "The monarchs who held vast domains in sway, heralded with trumpets night and day,\nDeparted weeping, crowns cast away—trust not this world of fleeting clay!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 13,
                "original": [
                    "कित्थे है सुलतान सिकन्दर, मौत ना छड्डे पीर पैगम्बर,  ",
                    "सभ्भे छड्ड गए अडम्बर, कोई एथे पायदार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "कित्थे है (कहाँ गया) सुलतान सिकन्दर (विश्वविजेता सिकंदर महान?), मौत (मृत्यु) ना छड्डे (नहीं छोड़ती) पीर पैगम्बर (पीरों और पैगंबरों को भी), सभ्भे (सभी महापुरुष) छड्ड गए (त्याग कर चले गए) अडम्बर (संसार के ठाठ-बाट), कोई (कोई भी) एथे (यहाँ) पायदार (शाश्वत/स्थायी) नहीं (नहीं है)।",
                "english_gloss": "कित्थे है सुलतान सिकन्दर (Where is Sultan Alexander the Great?), मौत ना छड्डे पीर पैगम्बर (death spares neither saints nor prophets), सभ्भे छड्ड गए अडम्बर (all left their worldly grandeur behind), कोई एथे पायदार नहीं (nothing here possesses enduring permanence).",
                "poetic_hindi": "कहाँ गया सिकंदर सुल्ताना? मौत न छोड़े पीर-पैग़म्बराना;\nछोड़ गए सब ठाठ-समाना, कोई यहाँ पायदार नहीं!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "Where is great Alexander now? To death both saints and prophets bow;\nAll left their pomp, none can endow a permanent station here below!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 14,
                "original": [
                    "किथे यूसफ माह-कन्यानी, लई ज़ूलैखां फेर जवानी,  ",
                    "कीती मौत ने ओड़क फ़ानी, फेर उह हार शिंगार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "किथे (कहाँ हैं) यूसफ (हज़रत यूसुफ) माह-कन्यानी (कनान देश के चंद्र-मुख सौन्दर्य?), लई (जिसके प्रेम में पुनः प्राप्त की) ज़ूलैखां (जुलेखा ने) फेर जवानी (अपनी खोई हुई जवानी), कीती मौत ने (किंतु मृत्यु ने कर दिया) ओड़क (अंततः सबको) फ़ानी (नष्ट/फना), फेर (फिर) उह हार शिंगार नहीं (न वह श्रृंगार रहा, न सौंदर्य)।",
                "english_gloss": "किथे यूसफ माह-कन्यानी (Where is Joseph, the moon of Canaan?), लई ज़ूलैखां फेर जवानी (for whom Zulaikha regained her youthful bloom?), कीती मौत ने ओड़क फ़ानी (yet death made all perish in the end), फेर उह हार शिंगार नहीं (and no cosmetic adornment remained).",
                "poetic_hindi": "कहाँ गए कनान के चंदा? जुलेखा ने पाया यौवन ताज़ा;\nमौत ने सबको किया फना, फिर वो हार-श्रृंगार नहीं!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "Where is Canaan's moon, Prince Joseph fair? Where is Zulaikha's golden hair?\nDeath turned them all to dust and air; no garlands or adornments there!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 15,
                "original": [
                    "कित्थे तख़त सुलेमां वाला, विच हवा उड्डदा सी बाला,  ",
                    "उह भी कादर आप संभाला, कोई ज़िन्दगी दा इतबार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "कित्थे (कहाँ है) तख़त (तख्त/सिंहासन) सुलेमां वाला (हज़रत सुलेमान का), विच हवा (हवा के मध्य) उड्डदा सी बाला (जो आकाश में उड़ता था?), उह भी (उसे भी) कादर (सर्वशक्तिमान ईश्वर ने) आप संभाला (वापस समेट लिया), कोई ज़िन्दगी दा इतबार नहीं (इस क्षणभंगुर जीवन का कोई भरोसा नहीं)।",
                "english_gloss": "कित्थे तख़त सुलेमां वाला (Where is the airborne throne of Solomon), विच हवा उड्डदा सी बाला (which flew on the winds through the high heavens?), उह भी कादर आप संभाला (even that the Almighty reclaimed unto Himself), कोई ज़िन्दगी दा इतबार नहीं (there is no certainty in this mortal life).",
                "poetic_hindi": "कहाँ सुलेमाँ का वो तख़्ता, जो पवन-मार्ग में उड़ता रहता?\nकादिर ने वो भी समेट लिया, जीवन का कोई ऐतबार नहीं!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "Where is King Solomon's aerial throne, that flew on the winds through the clouds alone?\nEven that by the Almighty was overthrown—to life's short breath no trust is known!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 16,
                "original": [
                    "कित्थे मीर मलक सुलतानां, सभ्भे छड्ड छड्ड गए टिकाणा,  ",
                    "कोई मार ना बैठे ठाणा, लशकर दा जिन्हां शुमार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "कित्थे (कहाँ गए वे) मीर (अमीर) मलक (मलिक) सुलतानां (और सुलतान?), सभ्भे (सभी) छड्ड छड्ड गए (छोड़-छोड़ कर चले गए) टिकाणा (अपने आलीशान महल और ठिकाने), कोई मार ना बैठे ठाणा (कोई भी यहाँ स्थायी थाना बनाकर न बैठ सका), लशकर दा जिन्हां (जिनकी विशाल सेनाओं की) शुमार नहीं (कोई गिनती नहीं थी)।",
                "english_gloss": "कित्थे मीर मलक सुलतानां (Where are the amirs, kings, and sultans?), सभ्भे छड्ड छड्ड गए टिकाणा (all abandoned their grand habitations), कोई मार ना बैठे ठाणा (none could establish an eternal throne), लशकर दा जिन्हां शुमार नहीं (though their armies were beyond numbering).",
                "poetic_hindi": "कहाँ अमीर-मलिक-सुलताना? सब छोड़ गए अपना ठिकाना;\nस्थिर न रहा किसी का थाना, जिनकी सेना का शुमार नहीं!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "Where are the sultans, nobles, and lords? All left their palaces, riches, and swords;\nNone kept their fortress against death's hordes, though countless armies stood at their words!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 17,
                "original": [
                    "फुल्लां फुल्ल चम्बेली लाला, सोसन सिम्बल सरू निराला,  ",
                    "बादि-खिज़ां कीता बुर हाला, नरगस नित खुमार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "फुल्लां (सुंदर फूलों में) फुल्ल चम्बेली (चमेली के फूल) लाला (लाल ट्यूलिप/गुले-लाला), सोसन (सुसन) सिम्बल (सेमल) सरू (सरू के सीधे सुंदर वृक्ष) निराला (अद्वितीय), बादि-खिज़ां (पतझड़ की शीतल मारक आँधी ने) कीता (कर दिया) बुर हाला (बुरा हाल/सबको मुरझा दिया), नरगस (नरगिस के पुष्पों में) नित (सदा) खुमार नहीं (नशा या मादकता नहीं रहती)।",
                "english_gloss": "फुल्लां फुल्ल चम्बेली लाला (Among blossoms the jasmine and crimson tulip), सोसन सिम्बल सरू निराला (the lily, silk-cotton, and stately cypress), बादि-खिज़ां (the autumn gale) कीता बुर हाला (reduced to a miserable ruin), नरगस नित खुमार नहीं (the narcissus flower cannot retain its intoxicating gaze forever).",
                "poetic_hindi": "चमेली, लाला, सरू सुहाने, सेमल-सुसन के रूप दिवाने;\nपतझड़ ने सब बाग उजाड़े, नरगिस में नित्य खुमार नहीं!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "The jasmine, tulip, and cypress tall, the lily and narcissus all;\nBeneath the autumn gales must fall; no garden retains its intoxicating thrall!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 18,
                "original": [
                    "जो कुझ करसें, सो कुझ पासें, नहीं ते ओड़क पिछोतासें,  ",
                    "सुंञी कूंज वांङ कुरलासें, खंभां बाझ उडार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "जो कुझ करसें (जो कुछ तू शुभ या अशुभ कर्म करेगा), सो कुझ पासें (वही फल तू भोगेगा), नहीं ते (अन्यथा) ओड़क (अंत समय) पिछोतासें (पछताएगा), सुंञी कूंज वांङ (एकाकिनी विलग कुररी पक्षी की तरह) कुरलासें (चीखेगा और विलाप करेगा), खंभां बाझ (पंखों के बिना) उडार नहीं (उड़ान संभव नहीं होती)।",
                "english_gloss": "जो कुझ करसें (Whatsoever thou sowest) सो कुझ पासें (that shalt thou reap), नहीं ते ओड़क पिछोतासें (otherwise at the end thou wilt regret in bitter remorse), सुंञी कूंज वांङ कुरलासें (shrieking like a lost, lonely crane), खंभां बाझ उडार नहीं (without wings of devotion no flight is possible).",
                "poetic_hindi": "जो कुछ बोएगा, वही तू पाएगा, नहीं तो अंत में पछताएगा;\nकूँज-समान तू कुरलाएगा, पंखों बिन कोई उड़ान नहीं!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "As you have sown, so shall you reap, or at the end in anguish weep;\nLike a wingless crane in sorrow steep, no soul can cross the aerial deep!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 19,
                "original": [
                    "डेरा करसें उहनीं जाईं, जिथे सेर पलंग बलाई,  ",
                    "खाली रहसन महल सराईं, फिर तूं विरसेदार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "डेरा करसें (तू अपना अंतिम डेरा डालेगा) उहनीं जाईं (उस अंधकारमय स्थान पर), जिथे (जहाँ) सेर पलंग (शरीर का पलंग मिट्टी का ढेर है और) बलाई (विपत्ति व भय पहरा देते हैं), खाली रहसन (खाली छूट जाएंगे) महल सराईं (ये महल और चौबारे), फिर (फिर) तूं (तू उनका) विरसेदार नहीं (उत्तराधिकारी या स्वामी नहीं रहेगा)।",
                "english_gloss": "डेरा करसें उहनीं जाईं (Thou shalt pitch thy tent in that solitary place), जिथे सेर पलंग बलाई (where a clod of earth is thy bed and tribulation guards thy rest), खाली रहसन महल सराईं (empty shall remain thy palaces and mansions), फिर तूं विरसेदार नहीं (no longer shalt thou be the inheritor or master).",
                "poetic_hindi": "डेरा करेगा तू उस ठाँव, मिट्टी का बिस्तर, विरह का गाँव;\nमहल-चौबारे खाली रह जाएँ, फिर तू इनका हक़दार नहीं!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "You'll pitch your tent where clods are bed, where fears and sorrows guard the dead;\nYour halls will stand with glories fled; no more your title shall be read!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 20,
                "original": [
                    "असीं आज़ज़ विच कोट इलम दे, ओसे आंदे विच कलम दे,  ",
                    "बिन कलमे दे नाहीं कंम दे, बाझों कलमे पार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।"
                ],
                "hindi_gloss": "असीं (हम) आज़ज़ (दीन-हीन जीव) विच कोट इलम दे (ज्ञान के दुर्ग के भीतर सुरक्षित होते हैं), ओसे (वे ही) आंदे (आते हैं) विच कलम दे (जो पवित्र ईश्वरीय कलम के लेख में अंकित हैं), बिन कलमे दे (बिना तौहीद के पवित्र कलमे के) नाहीं कंम दे (कोई काम नहीं आता), बाझों कलमे (कलमे की सत्यता के बिना) पार नहीं (उद्धार नहीं होता)।",
                "english_gloss": "असीं आज़ज़ (We humble, frail souls) विच कोट इलम दे (take shelter in the fortress of divine knowledge), ओसे आंदे विच कलम दे (which is inscribed by the Primal Pen), बिन कलमे दे नाहीं कंम दे (without the holy Kalima nothing is of any worth), बाझों कलमे पार नहीं (without the Kalima there is no crossing over).",
                "poetic_hindi": "हम दीन-हीन ज्ञान-कोट में आए, जो पावन कलम के लेख सजाए;\nकलमे बिन कोई काम न आए, कलमे बिन कोई पार नहीं!\nउठ जाग! खर्राटे मार नहीं!",
                "poetic_english": "In Wisdom's fort we paupers hide, by the Eternal Pen supplied;\nWithout the Word, no deeds abide; without the Word, no far-off side!\nArise, awake! Snore not in sleep so deep!"
            },
            {
                "stanza_number": 21,
                "original": [
                    "बुल्ल्हा शौह बिन कोई नाहीं, एथों ओथे दोहीं सराईं,  ",
                    "संभल संभल के कदम टिकाईं, फेर आवन दूजी वार नहीं,  ",
                    "उट्ठ जाग घुराड़े मार नहीं ।  ",
                    "इह सौन तेरे दरकार नहीं ।"
                ],
                "hindi_gloss": "बुल्ल्हा (बुल्लेशाह कहता है) शौह बिन (उस परम प्रभु-स्वामी के बिना) कोई नाहीं (कोई दूसरा रक्षक नहीं है), एथों (यहाँ इस लोक में) ओथे (और परलोक में) दोहीं सराईं (दोनों सरायों/जगतों में), संभल संभल के (सावधान होकर) कदम टिकाईं (अपने पग रखना), फेर आवन (पुनः मानव जन्म पाना) दूजी वार नहीं (दूसरी बार संभव नहीं है)।",
                "english_gloss": "बुल्ल्हा शौह बिन कोई नाहीं (Bulleh cries: none exists save the Sovereign Lord), एथों ओथे दोहीं सराईं (in both caravanserais—this world and the hereafter), संभल संभल के कदम टिकाईं (step with watchful caution and vigilance), फेर आवन दूजी वार नहीं (for there is no second return to this earthly arena).",
                "poetic_hindi": "बुल्ल्हा कहे, शाह बिन कोई नाहीं, यहाँ और वहाँ दोनों सराय माहीं;\nसंभल-संभल पग धरिए भाई, फिर आना दूसरी बार नहीं!\nउठ जाग! खर्राटे मार नहीं, ये सोना तेरे दरकार नहीं!",
                "poetic_english": "Bulleh cries: save the King, no friend is known, in both these worlds where seeds are sown;\nTread softly, cautiously, alone; no second chance to you is shown!\nArise, awake! Snore not in sleep so deep!\nSuch heedless rest thy soul must never keep!"
            }
        ],
        "sufi_commentary": "Kafi 152 is Bulleh Shah's most comprehensive and epic homily on spiritual vigilance (Yaqza) and mortality. Spanning 21 stanzas, it serves as the definitive encyclopedia of Sufi memento mori. Bulleh systematically dismantles every earthly refuge: bodily beauty dissolves into worm-food ('तेरा गोशत कीड़िआं खाना ए'); power and conquest vanish into oblivion, as exemplified by Alexander the Great ('सिकन्दर'), Solomon's flying throne ('तख़त सुलेमां'), and Joseph's beauty ('यूसफ माह-कन्यानी'); seasonal splendor is withered by the gale of autumn ('बादि-खिज़ां'). The central recurring refrain—'उट्ठ जाग घुराड़े मार नहीं'—is a thunderous spiritual commandment: snore not in heedlessness! The human incarnation is an irrecoverable opportunity ('फेर आवन दूजी वार नहीं'). In both worlds ('दोहीं सराईं'), only the Divine Word (the Kalima of Oneness) and the refuge of the Supreme Master can rescue the naked soul from the desolate grave."
    },
    {
        "id": 153,
        "title_punjabi": "वेखो नी कर गया माही",
        "title_english": "Behold, What My Herdsman Has Done!",
        "raga": "Raga Sarang / Kafi",
        "meter": "Matrik Chhand (16-14 matras)",
        "theme": "The Theophany of the Divine Herdsman and the Reckless Price of Love",
        "historical_context": "Rooted in the Heer-Ranjha and Sohni-Mahiwal motifs. Bulleh Shah portrays the Divine as the enchanter Mahi (Ranjha) who blows his mystical horn at the village door, robbing the seeker of worldly intellect and social standing. Bulleh faces family reproach, recalls Mansur's martyrdom, and tears off the veil of worldly modesty.",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "वेखो नी कर गया माही ।  ",
                    "लै दे के दिल हो गया राही ।"
                ],
                "hindi_gloss": "वेखो नी (अरी सखियो, देखो!) कर गया (कैसा कौतुक कर गया) माही (मेरा प्रियतम चरवाहा माहीवाल)। लै दे के (मेरे मन-प्राण को छीनकर) दिल (मेरा हृदय) हो गया (हो गया है) राही (उसी के मार्ग का बटोही/अनुगामी)।",
                "english_gloss": "वेखो नी (Behold, O friends!) कर गया माही (what my beloved Herdsman has done!). लै दे के दिल (Taking away my very heart) हो गया राही (He has departed on His way / made my soul a wanderer).",
                "poetic_hindi": "देखो री! कर गया कैसा माही,\nदिल छीन के हो गया राही!",
                "poetic_english": "Behold what my Herdsman has done, O friends dear!\nTaking my heart, He has vanished from here!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "अंमां झिड़के बाबल मारे, ताअने देंदे वीर प्यारे,  ",
                    "मैं जेही बुरी बुरिआर वे लोका, मैनूं देवो ओते वल त्राही ।  ",
                    "वेखो नी कर गया माही ।"
                ],
                "hindi_gloss": "अंमां (माता) झिड़के (डांटती-फटकारती है) बाबल (पिता) मारे (मारता है), ताअने (व्यंग्य-बाण) देंदे (देते हैं) वीर (भाई) प्यारे (प्यारे), मैं जेही (मुझ जैसी) बुरी (बुरी/बदनाम) बुरिआर (कुलटा को) वे लोका (हे लोगो!), मैनूं (मुझको) देवो (दिलाओ) ओते वल (उस परमात्मा से) त्राही (त्राण/मुक्ति)।",
                "english_gloss": "अंमां झिड़के (Mother scolds) बाबल मारे (father beats me), ताअने देंदे वीर प्यारे (my dear brothers shower me with taunts), मैं जेही बुरी बुरिआर वे लोका (unto a disgraced wrongdoer like me, O people!), मैनूं देवो ओते वल त्राही (grant me refuge and salvation from on High).",
                "poetic_hindi": "अम्माँ झिड़के, बाबुल मारे, ताने मारें वीर पियारे;\nमुझ जैसी बदनाम को लोगो, दो उस रब से त्राही!\nदेखो री! कर गया कैसा माही!",
                "poetic_english": "Mother scolds, father beats me in rage; my brothers mock my shameful stage;\nUnto a sinner on this earthly page, grant me deliverance, O Heavenly Sage!\nBehold what my Herdsman has done, O friends dear!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "आ बूहे ते नाद वजाइआ, अकल फ़िकर सभ चा गवाया,  ",
                    "अल्ल्हा दी सहुं अल्ल्हा जाणे, हस्सद्यां गल विच पै गई फाही ।  ",
                    "वेखो नी कर गया माही ।"
                ],
                "hindi_gloss": "आ (आकर) बूहे ते (मेरे द्वार पर) नाद (योगी का अनहद नाद/शृंग) वजाइआ (बजा दिया), अकल (मेरी बुद्धि) फ़िकर (और सोच-विचार) सभ (सब कुछ) चा गवाया (मिटा दिया), अल्ल्हा दी सहुं (अल्लाह की सौगंध!) अल्ल्हा जाणे (अल्लाह ही जानता है कि), हस्सद्यां (हंसते-खेलते ही) गल विच (गले में) पै गई (पड़ गई) फाही (प्रेम की प्राणघातक फांसी)।",
                "english_gloss": "आ बूहे ते नाद वजाइआ (Coming to my doorway He blew His horn), अकल फ़िकर सभ चा गवाया (sweeping away all intellect and calculation), अल्ल्हा दी सहुं (by God!) अल्ल्हा जाणे (God alone knows), हस्सद्यां (in mere laughing play) गल विच पै गई फाही (a fatal noose of love slipped around my neck).",
                "poetic_hindi": "दर पे आकर नाद बजाया, अक्ल-फिक्र सब दूर भगाया;\nअल्लाह की कसम, अल्लाह जाने, हँसते-हँसते फाँसी पाई!\nदेखो री! कर गया कैसा माही!",
                "poetic_english": "At my portal He sounded His horn of grace, scattering reason without a trace;\nBy Allah, Allah alone knows the case—in laughter a noose clasped my embrace!\nBehold what my Herdsman has done, O friends dear!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "रहु इश्का की करें अखाड़े, शाह मनसूर सूली 'ते चाढ़े,  ",
                    "आन बनी जद नाल असाडे, बुल्ल्हे मूंह तों लोई लाही ।  ",
                    "वेखो नी कर गया माही ।  ",
                    "लै दे के दिल हो गया राही ।"
                ],
                "hindi_gloss": "रहु इश्का (अरे ओ इश्क, ठहर!) की करें (क्या-क्या रचाता है) अखाड़े (अपने खूनी अखाड़े/तमाशे?), शाह मनसूर (महान संत मंसूर को) सूली 'ते (सूली के तख्ते पर) चाढ़े (चढ़ा दिया), आन बनी (जब वही प्रेम-परीक्षा आन पड़ी) जद नाल असाडे (हमारे सिर पर), बुल्ल्हे (तो बुल्लेशाह ने भी) मूंह तों (अपने मुख से) लोई (लोक-लाज की चादर) लाही (उतार फेंकी)।",
                "english_gloss": "रहु इश्का (Hold, O Love!) की करें अखाड़े (what bloody arenas dost thou stage?), शाह मनसूर (Saint Mansur) सूली 'ते चाढ़े (thou hoisted upon the gallows), आन बनी जद नाल असाडे (when that same crisis fell upon us), बुल्ल्हे मूंह तों लोई लाही (Bulleh flung the veil of worldly shame from his face!).",
                "poetic_hindi": "ठहर ओ इश्क! क्या अखाड़े सजाए, मंसूर को सूली पे चढ़ाए;\nजब आन पड़ी सिर पर हमारे, बुल्ल्हे ने लाज की चादर उतारी!\nदेखो री! कर गया कैसा माही, दिल छीन के हो गया राही!",
                "poetic_english": "Hold, O Love, what battles you stage! Mansur was hanged upon your cage;\nWhen the same trial struck our age, Bulleh tore the veil from off the page!\nBehold what my Herdsman has done, O friends dear!\nTaking my heart, He has vanished from here!"
            }
        ],
        "sufi_commentary": "Kafi 153 depicts the sudden, violent shattering of conventional life by the advent of Ishq. The Divine Beloved arrives disguised as a wandering yogic herdsman ('माही') and blows his horn ('नाद वजाइआ') at the threshold. Instantly, all social conformity, intellect, and worldly prudence are demolished. The seeker becomes a social outcast—scolded by mother, beaten by father, mocked by brothers. In Stanza 3, Bulleh describes how divine love strikes: not through solemn preparation, but in playful laughter ('हस्सद्यां गल विच पै गई फाही'), catching the soul in an inescapable noose. Recalling Mansur al-Hallaj's martyrdom on the gallows, Bulleh realizes that love accepts no compromise; he tears off the veil of social honor ('मूंह तों लोई लाही') and surrenders to the scandal of pure love."
    },
    {
        "id": 154,
        "title_punjabi": "वेखो नी प्यारा मैनूं सुफने में छल गया",
        "title_english": "Behold, the Beloved Beguiled Me in a Dream",
        "raga": "Raga Kafi / Tilang",
        "meter": "Baint / Davayya (16-14 matras)",
        "theme": "The Ephemeral Vision (Ru'ya), Burning of Mount Sinai, and Fulfillment in Shah Inayat",
        "historical_context": "Exploring the mystical phenomenon of the visionary dream (Kashf / Ru'ya). The Beloved appears in the seeker's slumber, igniting an all-consuming fire of love, and then disappears before awakening, leaving the lover shattered. Bulleh invokes Mount Sinai (Koh-e-Tur) scorched by God's radiant self-disclosure to Moses, Farhad carving Mount Bisutun for Shirin, and finally finds waking fulfillment at the feet of Shah Inayat.",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "मैं सोई होई मुट्ठी आं, मैं वांग ज़ुलैखां कुट्ठी आं,  ",
                    "चा इश्क ने मैं फट्टी आं, मेरा बन्द बन्द हिल्ल गया ।  ",
                    "वेखो नी प्यारा मैनूं सुफने में छल गया ।"
                ],
                "hindi_gloss": "मैं (मैं तो) सोई होई (सोते हुए ही) मुट्ठी आं (लुट गई हूँ), मैं (मैं) वांग ज़ुलैखां (जुलेखा के समान) कुट्ठी आं (विरह से विदीर्ण हो गई हूँ), चा इश्क ने (प्रेम ने उठाकर) मैं फट्टी आं (मुझे घावों से छलनी कर दिया है), मेरा (मेरा) बन्द बन्द (अंग-प्रत्यंग/जोड़-जोड़) हिल्ल गया (हिल/काँप उठा है)। वेखो नी (सखियो देखो!) प्यारा (प्रियतम) मैनूं (मुझको) सुफने में (स्वप्न में) छल गया (छल कर चला गया)।",
                "english_gloss": "मैं सोई होई मुट्ठी आं (As I lay asleep I was utterly robbed), मैं वांग ज़ुलैखां कुट्ठी आं (slain like Zulaikha in passion's grip), चा इश्क ने मैं फट्टी आं (love struck and pierced me with deep wounds), मेरा बन्द बन्द हिल्ल गया (every joint and limb of my body trembled). वेखो नी प्यारा मैनूं सुफने में छल गया (Behold, O friends, the Beloved beguiled me in a dream).",
                "poetic_hindi": "सोते-सोते मैं लुट गई री, जुलेखा जैसी कुट गई री;\nइश्क ने तन को चीर दिया, अंग-अंग मेरा हिल गया!\nदेखो री! प्यारा मुझे सपने में छल गया!",
                "poetic_english": "As I lay sleeping, robbed was I; like slain Zulaikha doomed to sigh;\nPierced by love's arrow from on high, my trembling joints in torment lie!\nBehold, the Beloved beguiled me in a dream!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "मैं स्याणियां सभ बुलाईआं, मैं औसियां सभ पवाईआं,  ",
                    "जवाब दित्ता नजूमियां, मेरी नैणीं नीर उच्छल गया ।  ",
                    "वेखो नी प्यारा मैनूं सुफने में छल गया ।"
                ],
                "hindi_gloss": "मैं (मैंने) स्याणियां (सभी सयानी बुद्धिमती स्त्रियों को) सभ बुलाईआं (बुलाकर पूछ लिया), मैं (मैंने) औसियां (आगमन की रेखाएं/शकुन) सभ पवाईआं (खिचवा कर देख लिए), जवाब दित्ता (निराश कर दिया) नजूमियां (ज्योतिषियों ने), मेरी नैणीं (मेरे नेत्रों से) नीर (अश्रुओं का सागर) उच्छल गया (उमड़ पड़ा)।",
                "english_gloss": "मैं स्याणियां सभ बुलाईआं (I summoned all wise women), मैं औसियां सभ पवाईआं (I drew all lines of augury and omen), जवाब दित्ता नजूमियां (the astrologers gave up in helplessness), मेरी नैणीं नीर उच्छल गया (and torrents of tears surged from my eyes).",
                "poetic_hindi": "सयानी स्त्रियाँ सब बुलाईं, शकुन की रेखाएँ खिंचाईं;\nज्योतिषियों ने जवाब दिया, नयनों से नीर उछल गया!\nदेखो री! प्यारा मुझे सपने में छल गया!",
                "poetic_english": "I called wise women of the land, drew lines of omen in the sand;\nAstrologers folded helpless hands, as tears rushed forth at grief's command!\nBehold, the Beloved beguiled me in a dream!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "नेड़े क्युं नहीं आईदा, सानूं दूरों नहीं दिखलाईदा,  ",
                    "नज़्ज़ारे तों ड्राईदा, कोह तूर पहाड़ जल गया ।  ",
                    "वेखो नी प्यारा मैनूं सुफने में छल गया ।"
                ],
                "hindi_gloss": "नेड़े (पास) क्युं नहीं आईदा (क्यों नहीं आते?), सानूं (हमें) दूरों (दूर से भी) नहीं दिखलाईदा (दर्शन क्यों नहीं देते?), नज़्ज़ारे तों (अपने प्रत्यक्ष तेज के दर्शन से) ड्राईदा (डराते हैं), कोह तूर (जिस तेज से तूर पर्वत) पहाड़ (पहाड़ जैसा पर्वत भी) जल गया (जलकर राख हो गया था)।",
                "english_gloss": "नेड़े क्युं नहीं आईदा (Why dost Thou not come near?), सानूं दूरों नहीं दिखलाईदा (why dost Thou not show Thyself even from afar?), नज़्ज़ारे तों ड्राईदा (Thou terrifiest us with Thy fiery glance), कोह तूर पहाड़ जल गया (whereby Mount Sinai itself was burnt to ash).",
                "poetic_hindi": "पास क्यों नहीं आते पिया? दूर से भी दर्शन न दिया;\nतेज से तेरे डर कंपे जिया, तूर पहाड़ भी जल गया!\nदेखो री! प्यारा मुझे सपने में छल गया!",
                "poetic_english": "Why draw not near to soothe my soul? Why hide from far where glories roll?\nThy fiery glance strikes fear whole, beneath which Mount Sinai turned to coal!\nBehold, the Beloved beguiled me in a dream!"
            },
            {
                "stanza_number": 4,
                "original": [
                    "पिया ने नैन बान ला के, बिरहों सूं चहचेहा के,  ",
                    "फरहाद तों कोह कटा के, शीरीं सों रल गया ।  ",
                    "वेखो नी प्यारा मैनूं सुफने में छल गया ।"
                ],
                "hindi_gloss": "पिया ने (प्रियतम ने) नैन बान (अपने कटाक्ष-बाण) ला के (मारकर), बिरहों सूं (विरह की आग से) चहचेहा के (हृदय को तड़पाकर), फरहाद तों (फरहाद से) कोह कटा के (पहाड़ कटवा कर), शीरीं सों (शीरीं के साथ) रल गया (जा मिला)।",
                "english_gloss": "पिया ने नैन बान ला के (The Beloved, shooting arrows from His eyes), बिरहों सूं चहचेहा के (making the soul writhe in separation's flame), फरहाद तों कोह कटा के (having made Farhad hew through the granite mountain), शीरीं सों रल गया (united with Shirin).",
                "poetic_hindi": "नैनों के तीर चला कर के, विरह में मुझे जला कर के;\nफरहाद से पर्वत कटा के, शीरीं संग जा मिल गया!\nदेखो री! प्यारा मुझे सपने में छल गया!",
                "poetic_english": "He shot His glance of piercing art, and kindled anguish in my heart;\nMade Farhad carve the rocks apart, to merge with Shirin in the mart!\nBehold, the Beloved beguiled me in a dream!"
            },
            {
                "stanza_number": 5,
                "original": [
                    "बुल्ल्हा आप तों लभाईदा, शहु इनायत है पाईदा,  ",
                    "नेड़े ही पछोताईदा, बुल्ल्हा अज्ज शहु मिल गया ।  ",
                    "वेखो नी प्यारा मैनूं सुफने में छल गया ।"
                ],
                "hindi_gloss": "बुल्ल्हा (बुल्लेशाह कहता है) आप तों (अपने भीतर ही) लभाईदा (वह प्रियतम प्राप्त होता है), शहु इनायत (मुर्शिद शाह इनायत के माध्यम से) है पाईदा (पाया जाता है), नेड़े ही (अत्यंत निकट होने पर भी अज्ञानवश) पछोताईदा (मनुष्य पछताता रहता है), बुल्ल्हा (आज बुल्लेशाह को) अज्ज (आज) शहु (प्रभु-प्रियतम) मिल गया (प्राप्त हो गया है)।",
                "english_gloss": "बुल्ल्हा आप तों लभाईदा (Bulleh says: within one's own self He is found), शहु इनायत है पाईदा (through Master Shah Inayat He is realized), नेड़े ही पछोताईदा (so near was He, yet mortals mourn in delusion), बुल्ल्हा अज्ज शहु मिल गया (today Bulleh has met the Sovereign Beloved!).",
                "poetic_hindi": "अपने ही भीतर वो बसता है, शाह इनायत से मिलता है;\nनिकट ही था, मन पछताता है, आज बुल्ल्हा को शाह मिल गया!\nदेखो री! प्यारा मुझे सपने में छल गया!",
                "poetic_english": "Within one's soul He is revealed, through Shah Inayat's blessing sealed;\nSo near He lay, in blindness concealed—today Bulleh's wounded heart is healed!\nBehold, the Beloved beguiled me in a dream!"
            }
        ],
        "sufi_commentary": "Kafi 154 explores the spiritual paradox of the dream-visitation (Ru'ya). When the Divine manifests in a dream, the experience is real, yet upon waking, the physical absence feels like a cruel deception ('सुफने में छल गया'). Bulleh uses classical mystical archetypes: Zulaikha's lovesick torment for Yusuf, Moses fainting as Mount Sinai turns to dust before the Tajalli (Divine Theophany) in Quran 7:143 ('कोह तूर पहाड़ जल गया'), and Farhad carving through Mount Bisutun with his mattock for Shirin. Bulleh resolves the agony in the final stanza by shifting from dream-projection to waking realization: the Beloved does not dwell in distant skies or elusive dreams, but indwells one's very own consciousness ('आप तों लभाईदा'), revealed through the living grace of Murshid Shah Inayat."
    },
    {
        "id": 155,
        "title_punjabi": "वेखो नी शहु इनायत साईं",
        "title_english": "Behold the Play of Master Shah Inayat!",
        "raga": "Raga Kafi / Bhairavi",
        "meter": "Dohra / Matrik (16-12 matras)",
        "theme": "The Alternating States of Spiritual Union and Separation (Bast wa Qabd)",
        "historical_context": "Reflecting the intense personal relationship between Bulleh Shah and Shah Inayat Qadiri. The Master alternately grants union and withdraws his presence to test and refine the disciple's soul. In the dark night of the soul, Bulleh ventures through the terrifying wilderness ('औझड़') to reach the riverbank of grace.",
        "stanzas": [
            {
                "stanza_number": 1,
                "original": [
                    "वेखो नी शहु इनायत साईं ।  ",
                    "मैं नाल करदा किवें अदाईं ।"
                ],
                "hindi_gloss": "वेखो नी (सखियो देखो!) शहु इनायत साईं (मुर्शिद शाह इनायत सांई), मैं नाल (मेरे साथ) करदा (करता है) किवें (कैसी-कैसी) अदाईं (नाज़-नखरे और प्रेम-कौतुक)।",
                "english_gloss": "वेखो नी (Behold, O friends!) शहु इनायत साईं (Master Shah Inayat Sai), मैं नाल करदा किवें अदाईं (how He plays with me in wondrous ways).",
                "poetic_hindi": "देखो री! शाह इनायत साईं,\nमेरे संग कैसी करे अदाईं!",
                "poetic_english": "Behold how Master Inayat plays;\nIn wondrous and enchanting ways!"
            },
            {
                "stanza_number": 2,
                "original": [
                    "कदी आवे कदी आवे नाहीं, त्युं त्युं मैनूं भड़कन भाहीं,  ",
                    "नाम अल्ल्हा पैग़ाम सुणाईं, मुक्ख वेखन नूं ना तरसाईं ।  ",
                    "वेखो नी शहु इनायत साईं ।"
                ],
                "hindi_gloss": "कदी आवे (कभी आता है) कदी आवे नाहीं (कभी नहीं आता), त्युं त्युं (त्यों-त्यों) मैनूं (मेरे भीतर) भड़कन (भड़क उठती हैं) भाहीं (विरह की ज्वालाएं), नाम अल्ल्हा (अल्लाह के नाम पर) पैग़ाम सुणाईं (कोई संदेशा सुनाओ), मुक्ख (अपना मुखड़ा) वेखन नूं (देखने के लिए) ना तरसाईं (मुझे मत तरसाओ)।",
                "english_gloss": "कदी आवे (Sometimes He comes) कदी आवे नाहीं (sometimes He comes not), त्युं त्युं (the more so) मैनूं भड़कन भाहीं (flames of separation flare within me), नाम अल्ल्हा (in God's name) पैग़ाम सुणाईं (bring me a message), मुक्ख वेखन नूं (to behold Thy face) ना तरसाईं (make me not thirst in vain).",
                "poetic_hindi": "कभी आए, कभी न आए, त्यों-त्यों विरह-अग्नि भड़काए;\nरब के नाम संदेश सुनाए, मुख देखने को न तरसाए!\nदेखो री! शाह इनायत साईं!",
                "poetic_english": "Sometimes He comes, sometimes He stays; separation sets my soul ablaze;\nIn Allah's name bring news that stays; starve not my eyes from Thy sweet gaze!\nBehold how Master Inayat plays!"
            },
            {
                "stanza_number": 3,
                "original": [
                    "बुल्ल्हा शहु केही आई मैनूं, रात हनेरी उट्ठ टुरदी नै नूं,  ",
                    "जिस औझड़ तों सभ कोई ड्रदा, सो मैं ढूंडां चाईं चाईं ।  ",
                    "वेखो नी शहु इनायत साईं ।  ",
                    "मैं नाल करदा किवें अदाईं ।"
                ],
                "hindi_gloss": "बुल्ल्हा (बुल्लेशाह कहता है) शहु (प्रभु-प्रियतम की) केही आई मैनूं (कैसी लगन मुझ पर आ पड़ी है कि), रात हनेरी (काली अंधेरी रात में) उट्ठ (उठकर) टुरदी (चल पड़ती हूँ) नै नूं (नदी चनाब की ओर), जिस (जिस) औझड़ तों (भयानक बीहड़ जंगल से) सभ कोई (हर कोई) ड्रदा (डरता है), सो (उसे) मैं (मैं) ढूंडां (खोजती फिरती हूँ) चाईं चाईं (उमंग और उत्साह से भरकर)।",
                "english_gloss": "बुल्ल्हा शहु केही आई मैनूं (Bulleh cries: what state has seized me from the King?), रात हनेरी (in pitch-black night) उट्ठ टुरदी नै नूं (I arise and walk to the river), जिस औझड़ तों (that perilous wilderness which) सभ कोई ड्रदा (everyone dreads), सो मैं ढूंडां (that I seek out) चाईं चाईं (with eager joy and love).",
                "poetic_hindi": "बुल्ल्हा कहे, क्या दशा समाई! काली रात में नदी को धाई;\nजिस बीहड़ से डरे खुदाई, उसे खोजती चाव लगाई!\nदेखो री! शाह इनायत साईं, मेरे संग कैसी करे अदाईं!",
                "poetic_english": "Bulleh cries: what passion holds my soul? Through dark of night I seek the stream whole;\nThe dreadful wilds where terrors roll, I search with joy to reach my goal!\nBehold how Master Inayat plays;\nIn wondrous and enchanting ways!"
            }
        ],
        "sufi_commentary": "Kafi 155 is a tender, intimate portrait of the spiritual dynamic between Master and disciple. The mystic life is not static peace; it oscillates between Bast (spiritual expansion/nearness) and Qabd (spiritual contraction/perceived distance). When Inayat withdraws, Bulleh's longing turns into a roaring blaze ('भड़कन भाहीं'). Yet this divine coquetry ('अदाईं') produces a fearless transformation: the frail disciple who once feared the dark now strides into the pitch-black night toward the turbulent river ('रात हनेरी उट्ठ टुरदी नै नूं') and ventures with overflowing joy ('चाईं चाईं') into the terrifying wilderness ('औझड़') where ordinary men fear to tread."
    }
]

# Lexicon updates for batch 151-155
new_lexicon_entries = {
    "दाढ": {
        "gurmukhi": "ਦਾੜ੍ਹ",
        "hindi": "प्रचंड जलन, भीतरी दाह, टीस",
        "english": "Searing burning sensation, intense inner smart",
        "context": "दाढ कलेजे बल बल उठदी (Kafi 151)"
    },
    "घुराड़े": {
        "gurmukhi": "ਘੁਰਾੜੇ",
        "hindi": "खर्राटे, गहरी गाढ़ी नींद का प्रमाद",
        "english": "Snores, deep heedless slumber",
        "context": "उट्ठ जाग घुराड़े मार नहीं (Kafi 152)"
    },
    "साहा": {
        "gurmukhi": "ਸਾਹਾ",
        "hindi": "विवाह का निश्चित लग्न, मृत्यु का निश्चित समय",
        "english": "Appointed hour for marriage or death",
        "context": "तेरा साहा नेड़े आया ए (Kafi 152)"
    },
    "मुक्कलावा": {
        "gurmukhi": "ਮੁਕਲਾਵਾ",
        "hindi": "गौना, वधू की ससुराल के लिए अंतिम विदाई",
        "english": "Gauna, final departure of the bride to marital home",
        "context": "अज्ज कल्ल्ह तेरा मुक्कलावा ए (Kafi 152)"
    },
    "बादि-खिज़ां": {
        "gurmukhi": "ਬਾਦਿ-ਖ਼ਿਜ਼ਾਂ",
        "hindi": "पतझड़ की मारक वायु, काल-बयार",
        "english": "Autumn gale, withering wind of mortality",
        "context": "बादि-खिज़ां कीता बुर हाला (Kafi 152)"
    },
    "औझड़": {
        "gurmukhi": "ਔਝੜ",
        "hindi": "बीहड़, दुर्गम निर्जन जंगल, भटकाव का मार्ग",
        "english": "Wild perilous wasteland, trackless forest",
        "context": "जिस औझड़ तों सभ कोई ड्रदा (Kafi 155)"
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
        "last_processed_kafi_id": 155,
        "completed_count": 155,
        "total": 160,
        "next_kafi_id": 156,
        "status": "in_progress"
    }
    with open(CHECKPOINT_PATH, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print("Checkpoint updated: 155/160 completed. Next ID: 156")

if __name__ == "__main__":
    save_batch()
