# -*- coding: utf-8 -*-
"""
Process Kafian 61 to 65 for Bulleh Shah Trilingual Edition.
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
        "id": 61,
        "title": "कदी मोड़ मुहारां ढोलिआ",
        "title_english": "Turn the Reins Sometime, O Beloved!",
        "historical_context": "इस लघु एवं मार्मिक काफी में विरहिणी जीवात्मा अपने रूठे हुए प्रियतम (ढोला/ईश्वर) से प्रार्थना करती है कि वह अपने ऊंट अथवा अश्व की बागडोर (मुहार) उसकी ओर मोड़ ले। विरहिणी ने सज-संवर कर प्रतीक्षा की, किंतु किसी अनजाने वचन के कारण प्रियतम के मन में गांठ पड़ गई।",
        "meter": "पंजाबी काफी (मात्रािक दोहा-संकर)",
        "raga": "राग तिलंग / काफी",
        "theme": "रूठे प्रियतम को मनाना, विरह की तड़प, क्षमा-याचना",
        "stanzas": [
            {
                "original": [
                    "कदी मोड़ मुहारां ढोलिआ ।  ",
                    "तेरियां वाटां तों सिर घोलिआ ।"
                ],
                "hindi_gloss": [
                    "कदी (कभी तो) मोड़ (मोड़ ले) मुहारां (बागडौर/ऊंट की नकेल) ढोलिआ (हे ढोला/प्रियतम प्यारे) ।",
                    "तेरियां (तेरी) वाटां (राहों) तों (पर) सिर (शीश) घोलिआ (न्योछावर कर दिया) ।"
                ],
                "english_gloss": [
                    "कदी (sometime) मोड़ (turn) मुहारां (the reins/bridle) ढोलिआ (O my Beloved) ।",
                    "तेरियां (Thy) वाटां (pathways) तों (upon) सिर (head/life) घोलिआ (sacrificed) ।"
                ],
                "poetic_hindi": [
                    "कभी तो मोड़ मुहारें ढोला, तेरी राहों पर सिर घोला !"
                ],
                "poetic_english": [
                    "Turn back the reins sometime, Beloved mine, upon Thy pathways I my life resign!"
                ]
            },
            {
                "original": [
                    "मैं न्हाती धोती रह गई, कोई गंढ सज्जन दिल बह गई,  ",
                    "कोई सुख़न अवल्ला बोलिआ, कदी मोड़ मुहारां ढोलिआ ।"
                ],
                "hindi_gloss": [
                    "मैं (मैं) न्हाती (नहा-) धोती (धोकर सजती ही) रह (रह) गई (गई), कोई (कोई) गंढ (गांठ/संदेह) सज्जन (सज्जन/प्रियतम के) दिल (दिल में) बह (बैठ) गई (गई),",
                    "कोई (शायद कोई) सुख़न (वचन/बात) अवल्ला (अनुचित/कड़वा) बोलिआ (बोल बैठी हूँगी), कदी (कभी) मोड़ (मोड़ ले) मुहारां (बागडौर) ढोलिआ (हे प्रियतम) ।"
                ],
                "english_gloss": [
                    "मैं (I) न्हाती (bathed) धोती (washed/adorned) रह (stood) गई (remained), कोई (some) गंढ (knot/suspicion) सज्जन (Beloved’s) दिल (in heart) बह (settled) गई (went),",
                    "कोई (some) सुख़न (word) अवल्ला (awkward/improper) बोलिआ (spoke I), कदी (sometime) मोड़ (turn) मुहारां (reins) ढोलिआ (O Beloved) ।"
                ],
                "poetic_hindi": [
                    "मैं नहाई-धोई सज कर बैठी, साजन के दिल में गाँठ पड़ी,",
                    "कोई अनुचित बोल कह बैठी, लौट आ प्यारे इस विरह-घड़ी !"
                ],
                "poetic_english": [
                    "Adorned and bathed I waited all in vain, some grievance in my Lover’s heart arose;",
                    "Did some unseemly word inflict Him pain? Turn back the reins and end these parting woes!"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु कदी घर आवसी, मेरी बलदी भा बुझावसी,  ",
                    "जीहदे दुक्खां ने मूंह खोल्हआ, कदी मोड़ मुहारां ढोलिआ ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ले का) शहु (शाह/स्वामी) कदी (कभी तो) घर (घर) आवसी (आएगा), मेरी (मेरी) बलदी (धधकती हुई) भा (विरह-अग्नि) बुझावसी (बुझाएगा),",
                    "जीहदे (जिसके) दुक्खां (दुखों) ने (ने) मूंह (मुख) खोल्हआ (खोल दिया/व्याकुल कर दिया), कदी (कभी) मोड़ (मोड़) मुहारां (बागडौर) ढोलिआ (हे प्रियतम) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh’s) शहु (Lord) कदी (sometime) घर (home) आवसी (will come), मेरी (my) बलदी (burning) भा (flames) बुझावसी (will quench),",
                    "जीहदे (whose) दुक्खां (sorrows) ने (have) मूंह (jaws/mouth) खोल्हआ (opened wide), कदी (sometime) मोड़ (turn) मुहारां (reins) ढोलिआ (O Beloved) ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा शौह जब घर आएँगे, धधकती विरह-आग बुझाएँगे,",
                    "जिसके दुखों ने मुख खोला, मोड़ मुहारें प्यारे ढोला !"
                ],
                "poetic_english": [
                    "Bulleh’s Lord to my home shall yet return, to quench the blazing fires that consume;",
                    "Whose sorrows wide their bitter hunger churn, turn back the reins and banish all my gloom!"
                ]
            }
        ],
        "philosophical_meaning": "आध्यात्मिक यात्रा में साधक को अनेक बार ईश्वर की विमुखता (क़ब्ज़ / विरह) का सामना करना पड़ता है। 'कोई गंढ सज्जन दिल बह गई' का अर्थ है कि साधक के किसी सूक्ष्म अहंकार या प्रमाद के कारण अंतरंग संबंध में दूरी आ गई है। साधक दीनभाव से क्षमा माँगकर पुनः सामीप्य की याचना करता है।"
    },
    {
        "id": 62,
        "title": "कपूरी रेवड़ी क्यों कर लड़े पतासे नाल",
        "title_english": "How Can Kapuri Revadi Fight With Patasa?",
        "historical_context": "यह बाबा बुल्ले शाह की सबसे प्रसिद्ध व्यंग्यात्मक और उलटबांसी शैली की काफी है। 18वीं सदी के पंजाब में मुग़ल सत्ता के पतन, नादिर शाह और अब्दाली के आक्रमणों तथा नैतिक मूल्यों के उलट-फेर के काल में बुल्ले शाह ने मिठाइयों (रेवड़ी, पतासा, जलेबी, लड्डू) और पशुओं की उल्टी प्रकृति (कौवे का बाज़ को मारना, भेड़ों का चीते को पछाड़ना, चूहों का बिल्ली के कान कुतरना) के रूपक द्वारा सामाजिक और राजनीतिक विपर्यय का तीखा चित्रण किया है।",
        "meter": "पंजाबी काफी (व्यंग्यात्मक उलटबांसी छंद)",
        "raga": "राग काफी / बिलावल",
        "theme": "सामाजिक पतन, उलटबांसी, कलियुगी विषमता, कयामत और दज्जाल का आगमन",
        "stanzas": [
            {
                "original": [
                    "तेल तिलां दे लड्डू ने, जलेबी पकड़ मंगाई,  ",
                    "डरदे नट्ठे कन्द शकर तों, मिसरी नाल लड़ाई,  ",
                    "कां लगड़ नूं मारन लग्गे, गोचें दी गल्ल्ह लाल ।  ",
                    "कपूरी रेवड़ी क्यों कर लड़े पतासे नाल ।"
                ],
                "hindi_gloss": [
                    "तेल (तेल में तले) तिलां (तिल) दे (के) लड्डू (लड्डू) ने (ने), जलेबी (जलेबी को) पकड़ (पकड़कर) मंगाई (तलब किया),",
                    "डरदे (डरकर) नट्ठे (भागे) कन्द (कंद-मिश्री) शकर (शक्कर) तों (से), मिसरी (मिश्री) नाल (के साथ) लड़ाई (युद्ध ठान लिया),",
                    "कां (कौवे) लगड़ (शिकारी बाज़) नूं (को) मारन (मारने) लग्गे (लगे), गोचें (गौंचे/चिड़िया) दी (के) गल्ल्ह (गाल) लाल (खून से लाल हो गए) ।",
                    "कपूरी (कपूर-युक्त/सफेद) रेवड़ी (रेवड़ी) क्यों (क्यों) कर (करके) लड़े (लड़े) पतासे (सदाशय पतासे) नाल (के साथ) ।"
                ],
                "english_gloss": [
                    "तेल (oil) तिलां (of sesame) दे (of) लड्डू (sweet-balls) ने (have), जलेबी (the coiled jalebi) पकड़ (seized) मंगाई (summoned),",
                    "डरदे (in fear) नट्ठे (fled) कन्द (sugar candy) शकर (raw sugar) तों (from), मिसरी (with refined sugar) नाल (with) लड़ाई (fought),",
                    "कां (crows) लगड़ (the falcon) नूं (unto) मारन (to slay) लग्गे (began), गोचें (of small birds) दी (of) गल्ल्ह (cheeks) लाल (red with blood) ।",
                    "कपूरी (camphor-scented) रेवड़ी (crisp revadi) क्यों (why) कर (how) लड़े (fight) पतासे (with the fragile patasa) नाल (with) ।"
                ],
                "poetic_hindi": [
                    "तिल के लड्डू ने जलेबी को बंदी कर मँगवाया,",
                    "शक्कर भागे कंद से डर कर, मिश्री से युद्ध रचाया ।",
                    "कौवे लगे हैं बाज़ को मारने, चिड़ियों के मुख लाल,",
                    "कपूरी रेवड़ी क्योंकर लड़े पतासे नाल ?"
                ],
                "poetic_english": [
                    "Sesame balls have seized the crisp jalebi in their thrall,",
                    "Raw sugar flees from refined sweets in terror at the wall;",
                    "Black crows now fall upon the hawk, small sparrows fight with zest:",
                    "How can Kapuri Revadi fight Patasa at its best?"
                ]
            },
            {
                "original": [
                    "हो फरिआदी लक्खपतियां ने, लून ते दसतक लाई,  ",
                    "गुलगलिआं मनसूबा बद्धा, पापड़ चोट चलाई,  ",
                    "भेडां मार पलंग खपाए, गुरगां बुरा अहवाल ।  ",
                    "कपूरी रेवड़ी क्यों कर लड़े पतासे नाल ।"
                ],
                "hindi_gloss": [
                    "हो (होकर) फरिआदी (फरियादी/याचक) लक्खपतियां (लाखपतियों) ने (ने), लून (साधारण नमक) ते (पर) दसतक (हाथ फैलाया/मांग की) लाई (लगाई),",
                    "गुलगलिआं (मीठे गुलगुलों ने) मनसूबा (षड्यंत्र/योजना) बद्धा (बांधी), पापड़ (पापड़ ने) चोट (आक्रमण) चलाई (चलाया),",
                    "भेडां (भेड़ों ने) मार (मारकर) पलंग (पलंग/चीतों-तेंदुओं को) खपाए (नष्ट कर दिया), गुरगां (भेड़ियों का) बुरा (अति बुरा) अहवाल (हाल हो गया) ।",
                    "कपूरी रेवड़ी क्यों कर लड़े पतासे नाल ।"
                ],
                "english_gloss": [
                    "हो (becoming) फरिआदी (petitioners/beggars) लक्खपतियां (millionaires) ने (have), लून (for common salt) ते (upon) दसतक (knock/petition) लाई (made),",
                    "गुलगलिआं (soft fried sweet-puffs) मनसूबा (plot/design) बद्धा (hatched), पापड़ (crisp poppadom) चोट (strikes) चलाई (launched),",
                    "भेडां (sheep) मार (slaying) पलंग (leopards/panthers) खपाए (destroyed), गुरगां (of wolves) बुरा (wretched) अहवाल (condition) ।",
                    "कपूरी रेवड़ी क्यों कर लड़े पतासे नाल ।"
                ],
                "poetic_hindi": [
                    "लखपति भिखारी बन कर घूमें, माँगें नमक का दान,",
                    "गुलगुले षड्यंत्र रचें, पापड़ चलाए बाण ।",
                    "भेड़ों ने पछाड़ दिए तेंदुए, भेड़ियों का बुरा हाल,",
                    "कपूरी रेवड़ी क्योंकर लड़े पतासे नाल ?"
                ],
                "poetic_english": [
                    "Proud millionaires become as beggars crying for cheap salt,",
                    "Soft puffs of dough plot wars while brittle wafers wage assault;",
                    "Frail sheep have routed leopards wild, wolves tremble in despair:",
                    "How can Kapuri Revadi fight Patasa fair and square?"
                ]
            },
            {
                "original": [
                    "गुड़ दे लड्डू गुस्से हो के, पेड़्यां ते फरिआदी,  ",
                    "बरफ़ी नूं कहे दाल चने दी, तूं हैं मेरी बांदी,  ",
                    "चढ़ सहे शीहणियां ते नच्चन लग्गे, वड्डी पई धमाल ।  ",
                    "कपूरी रेवड़ी क्यों कर लड़े पतासे नाल ।"
                ],
                "hindi_gloss": [
                    "गुड़ (गुड़) दे (के) लड्डू (लड्डू) गुस्से (क्रोधित) हो (हो) के (कर), पेड़्यां (दूध के पेड़ों) ते (पर) फरिआदी (अभियोग लगाने वाले बने),",
                    "बरफ़ी (राजसी बर्फी) नूं (को) कहे (कहती है) दाल (साधारण दाल) चने (चने) दी (की), तूं (तू) हैं (है) मेरी (मेरी) बांदी (दासी),",
                    "चढ़ (सवार होकर) सहे (खरगोश) शीहणियां (शेरनियों) ते (पर) नच्चन (नाचने) लग्गे (लगे), वड्डी (बड़ी भारी) पई (मची) धमाल (उत्पात/धूम) ।",
                    "कपूरी रेवड़ी क्यों कर लड़े पतासे नाल ।"
                ],
                "english_gloss": [
                    "गुड़ (jaggery) दे (of) लड्डू (balls) गुस्से (wrathful) हो (becoming) के (having), पेड़्यां (pedas/milk sweets) ते (against) फरिआदी (filed complaint),",
                    "बरफ़ी (unto barfi) कहे (says) दाल (pulse) चने (of chickpea) दी (of), तूं (thou) हैं (art) मेरी (my) बांदी (slave-girl),",
                    "चढ़ (mounted) सहे (hares/rabbits) शीहणियां (upon lionesses) ते (upon) नच्चन (to dance) लग्गे (began), वड्डी (immense) पई (spread) धमाल (chaos/uproar) ।",
                    "कपूरी रेवड़ी क्यों कर लड़े पतासे नाल ।"
                ],
                "poetic_hindi": [
                    "गुड़ के लड्डू क्रोध में आकर पेड़े पर दावा ठोकें,",
                    "चने की दाल कहे बर्फी को: 'तू है मेरी चेरी!'",
                    "खरगोश चढ़े शेरनियों पर, मचा है घोर धमाल,",
                    "कपूरी रेवड़ी क्योंकर लड़े पतासे नाल ?"
                ],
                "poetic_english": [
                    "Rough jaggery sweets in wrath indict rich pedas at the court,",
                    "Coarse gram-flour tells the royal barfi: 'Thou art my slave for sport!'",
                    "Hares mount upon the lioness and dance in wild delight:",
                    "How can Kapuri Revadi fight Patasa in the fight?"
                ]
            },
            {
                "original": [
                    "शकर खंड कहे मिसरी नूं, मेरी वेख सफ़ाई,  ",
                    "चिड़वे चने इह करन लग्गे, बदाने नाल लड़ाई,  ",
                    "चूहआं कन्न बिल्ली दे कुतरे, हो हो के खुशहाल ।  ",
                    "कपूरी रेवड़ी क्यों कर लड़े पतासे नाल ।"
                ],
                "hindi_gloss": [
                    "शकर (शक्कर) खंड (खांड) कहे (कहती है) मिसरी (मिश्री) नूं (से), मेरी (मेरी) वेख (देख) सफ़ाई (स्वच्छता/सफेदी),",
                    "चिड़वे (चिवड़ा/पोहा) चने (और भुने चने) इह (ये) करन (करने) लग्गे (लगे), बदाने (बूंदी/मीठे दाने) नाल (के साथ) लड़ाई (युद्ध),",
                    "चूहआं (चूहों ने) कन्न (कान) बिल्ली (बिल्ली) दे (के) कुतरे (कुतर डाले), हो (हो-) हो (होकर) के (के) खुशहाल (प्रसन्न) ।",
                    "कपूरी रेवड़ी क्यों कर लड़े पतासे नाल ।"
                ],
                "english_gloss": [
                    "शकर (raw sugar) खंड (crude sugar) कहे (says) मिसरी (to pure rock-sugar) नूं (to), मेरी (my) वेख (behold) सफ़ाई (cleanliness/purity),",
                    "चिड़वे (flattened rice) चने (and chickpeas) इह (these) करन (to wage) लग्गे (began), बदाने (sugar-droplets/boondi) नाल (with) लड़ाई (war),",
                    "चूहआं (mice) कन्न (ears) बिल्ली (of the cat) दे (of) कुतरे (nibbled off), हो (becoming) हो (becoming) के (having) खुशहाल (jubilant) ।",
                    "कपूरी रेवड़ी क्यों कर लड़े पतासे नाल ।"
                ],
                "poetic_hindi": [
                    "खांड कहे मिश्री से: 'मेरी देख सफ़ाई भारी',",
                    "चिवड़ा-चना लड़े बूँदी से, कैसी जंग पसारी !",
                    "हँस-हँस चूहों ने बिल्ली के कुतर दिए हैं कान,",
                    "कपूरी रेवड़ी क्योंकर लड़े पतासे नाल ?"
                ],
                "poetic_english": [
                    "Raw sugar boasts before refined: 'Behold my purity!',",
                    "Flaked rice and roasted grams contest sweet boondi’s pedigree;",
                    "Mice boldly gnaw the tomcat’s ears in triumph full and grand:",
                    "How can Kapuri Revadi fight Patasa in this land?"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु हुन क्या बतावे, जो दिसे सो लड़दा,  ",
                    "लत्त बलत्ती, गुत्त बगुत्ती, कोई नहीं हत्थ फड़दा,  ",
                    "वेखो केही क्यामत आई, आया खर दज्जाल ।  ",
                    "कपूरी रेवड़ी क्यों कर लड़े पतासे नाल ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ला) शहु (प्रभु की लीला) हुन (अब) क्या (क्या) बतावे (बताए), जो (जो कोई भी) दिसे (दिखता है) सो (वही) लड़दा (लड़ रहा है),",
                    "लत्त (लातों से) बलत्ती (लातम-लात), गुत्त (बालों/चोटियों से) बगुत्ती (गुथम-गुत्था), कोई (कोई भी) नहीं (नहीं) हत्थ (हाथ) फड़दा (रोकने वाला/मध्यस्थ),",
                    "वेखो (देखो) केही (कैसी विचित्र) क्यामत (कयामत/प्रलय) आई (आ गई है), आया (आ गया है) खर (गधा/गधे पर सवार) दज्जाल (दज्जाल/कलिकाल का दैत्य) ।",
                    "कपूरी (कपूर-रेवड़ी) रेवड़ी (रेवड़ी) क्यों (क्यों) कर (करके) लड़े (लड़े) पतासे (सदाचारी पतासे) नाल (के साथ) ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh says) शहु (what the Lord wills) हुन (now) क्या (what) बतावे (can tell), जो (whoever) दिसे (is seen) सो (that one) लड़दा (fights),",
                    "लत्त (kicks) बलत्ती (kicking one another), गुत्त (locks of hair) बगुत्ती (grappling by hair), कोई (no one) नहीं (not) हत्थ (hand) फड़दा (restrains/holds),",
                    "वेखो (behold) केही (what kind of) क्यामत (apocalypse) आई (has arrived), आया (has arrived) खर (the ass of) दज्जाल (Dajjal/Anti-Christ) ।",
                    "कपूरी रेवड़ी क्यों कर लड़े पतासे नाल ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा शौह अब क्या बतलाए, जो दिखता सो लड़े परस्पर,",
                    "लातम-लात, गुथम-गुत्था हैं, हाथ न पकड़े कोई रहबर ।",
                    "देखो कैसी कयामत आई, आया खर-दज्जाल,",
                    "कपूरी रेवड़ी क्योंकर लड़े पतासे नाल ?"
                ],
                "poetic_english": [
                    "What can poor Bulleh say of this, when all he sees is strife?",
                    "Kicking and grappling by the hair, in bitterness of life;",
                    "Behold the Doomsday has arrived, Dajjal rides on his beast:",
                    "How can Kapuri Revadi fight Patasa at the feast?"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी कबीर की उलटबासियों ('बैलहि डारि गऊ गुनि लाई', 'चींटी के पग नूपुर बाजै') की परंपरा में है। इसमें तत्कालीन पंजाब की अराजकता का रूपक है। 'खर दज्जाल' इस्लामी परंपरा में कयामत से पूर्व आने वाला वह दैत्य है जो गधे पर सवार होकर समाज के समस्त नैतिक और आध्यात्मिक मूल्यों को उलट देता है। बुल्ले शाह का संकेत है कि जब अहम् और अज्ञान का बोलबाला हो, तो तुच्छ तत्व (कच्ची शक्कर, भेड़, चूहे) उच्च सत्यों का उपहास उड़ाने लगते हैं।"
    },
    {
        "id": 63,
        "title": "कर कत्तन वल्ल ध्यान कुड़े",
        "title_english": "Pay Heed Unto Thy Spinning, O Maiden!",
        "historical_context": "यह बुल्ले शाह का प्रसिद्ध 'चरखा-नामा' है, जिसमें 24 बंद हैं। पंजाब की लोक-संस्कृति में कन्या जब अपने मायके (पेके) में होती है, तो चरखा कातकर अपने विवाह के लिए दहेज (दाज) तैयार करती है। सूफी रूपक में जीवात्मा एक कन्या है, यह संसार मायका है, मानव-शरीर चरखा है, श्वासें रुई हैं, और सत्कर्म व ईश्वर-स्मरण (ज़िक्र) वह सूत है जिसे कातकर परलोक (ससुराल) में परमात्मा रूपी दूल्हे को रिझाना है। यदि कन्या व्यर्थ खेल-कूद में समय गँवा देगी, तो ससुराल में लज्जित होगी।",
        "meter": "पंजाबी काफी (चरखा-नामा प्रबंध, 24 अंतरे)",
        "raga": "राग काफी / माझ",
        "theme": "चरखा और सूत का रूपक, जीवन की क्षणभंगुरता, मृत्यु और परलोक की तैयारी, सत्कर्म",
        "stanzas": [
            {
                "original": [
                    "नित मत्तीं देंदी मां धिया, क्यों फिरनी एं ऐवें आ धिया,  ",
                    "नी शरम हया ना गवा धिया, तूं कदी तां समझ नदान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "नित (नित्य) मत्तीं (शिक्षा/सद्बुद्धि) देंदी (देती है) मां (मां) धिया (हे पुत्री), क्यों (क्यों) फिरनी (घूमती) एं (है) ऐवें (व्यर्थ) आ (इधर-उधर) धिया (हे बेटी),",
                    "नी (अरी) शरम (लाज) हया (मर्यादा) ना (मत) गवा (खो) धिया (पुत्री), तूं (तू) कदी (कभी) तां (तो) समझ (समझ) नदान (हे नादान) कुड़े (हे कन्या) ।",
                    "कर (कर) कत्तन (सूत कातने/साधना की) वल्ल (ओर) ध्यान (ध्यान) कुड़े (हे सखी/कन्या) ।"
                ],
                "english_gloss": [
                    "नित (daily) मत्तीं (counsel) देंदी (gives) मां (mother) धिया (O daughter), क्यों (why) फिरनी (wanderest) एं (thou) ऐवें (aimlessly) आ (here and there) धिया (daughter),",
                    "नी (O) शरम (modesty) हया (decency) ना (do not) गवा (lose) धिया (daughter), तूं (thou) कदी (ever) तां (then) समझ (understand) नदान (foolish) कुड़े (maiden) ।",
                    "कर (turn) कत्तन (spinning the yarn/devotion) वल्ल (towards) ध्यान (attention) कुड़े (O girl) ।"
                ],
                "poetic_hindi": [
                    "माँ नित्य सिखाए: 'बेटी सुन, क्यों भटके व्यर्थ गँवाए गुण,",
                    "लाज-हया मत खो पुत्री, कुछ सीख समझ नादान कुड़े ।",
                    "कर कातने पर ध्यान कुड़े !'"
                ],
                "poetic_english": [
                    "Daily the mother warns: 'My daughter heed, why wander aimlessly without a care?",
                    "Lose not thy modesty in youthful deed, awaken now, naive and unaware:",
                    "Turn to thy spinning-wheel, O maiden fair!'"
                ]
            },
            {
                "original": [
                    "चरख़ा मुफत तेरे हत्थ आया, पल्ल्युं नहींउं खोल्ह गवाइआ,  ",
                    "नहीउं कदर मेहनत दा पाइआ, जद होया कंम आसान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "चरख़ा (यह चरखा/मानव-देह) मुफत (मुफ्त में/प्रभु-कृपा से) तेरे (तेरे) हत्थ (हाथ) आया (आया है), पल्ल्युं (अपनी गांठ से) नहींउं (नहीं) खोल्ह (खोलकर) गवाइआ (गँवाया कुछ),",
                    "नहीउं (नहीं) कदर (मूल्य/महत्व) मेहनत (श्रम) दा (का) पाइआ (समझा), जद (जब) होया (हो गया) कंम (कार्य) आसान (अति सुगम) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "चरख़ा (spinning wheel/human body) मुफत (free) तेरे (thy) हत्थ (in hands) आया (came), पल्ल्युं (from pocket/purse) नहींउं (not) खोल्ह (spending) गवाइआ (lost anything),",
                    "नहीउं (not) कदर (worth) मेहनत (of labor) दा (of) पाइआ (realized), जद (when) होया (became) कंम (task) आसान (easy) कुड़े (O maiden) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "यह चरखा मुफ्त मिला तुझको, अपनी गाँठ से कुछ न गँवाया,",
                    "श्रम की कद्र न जानी तूने, जब सुगम कार्य प्रभु ने बख्शाया ।",
                    "कर कातने पर ध्यान कुड़े !"
                ],
                "poetic_english": [
                    "This spinning-wheel was granted free of cost, no coin was spent from thine own pocket here;",
                    "Value of labor in smug ease is lost, because the priceless gift was brought so near:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "चरख़ा बण्या ख़ातर तेरी, खेडन दी कर हिरस थुरेड़ी,  ",
                    "होना नहीउं होर वडेरी, मत कर कोई अगिआन कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "चरख़ा (यह चरखा) बण्या (बनाया गया है) ख़ातर (खातिर/प्रयोजन हेतु) तेरी (तेरे), खेडन (खेल-कूद) दी (की) कर (कर) हिरस (लालसा) थुरेड़ी (थोड़ी/कम),",
                    "होना (होना) नहीउं (नहीं है) होर (और अधिक) वडेरी (आयु में बड़ी/अवसर पुनः नहीं मिलेगा), मत (मत) कर (कर) कोई (कोई) अगिआन (अज्ञान) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "चरख़ा (spinning wheel) बण्या (fashioned) ख़ातर (for the sake of) तेरी (thee), खेडन (of playing) दी (of) कर (make) हिरस (lust/greed) थुरेड़ी (scant/less),",
                    "होना (to become) नहीउं (not) होर (more) वडेरी (older/this chance won't return), मत (do not) कर (commit) कोई (any) अगिआन (foolishness/ignorance) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "यह चरखा तेरे हित निर्मित, खेल-कूद की चाह घटा ले,",
                    "सदा न जीवन-अवसर मिलना, मत अज्ञान में जन्म गँवा ले ।",
                    "कर कातने पर ध्यान कुड़े !"
                ],
                "poetic_english": [
                    "Fashioned expressly for thy soul's delight, curb now thy childish lust for idle play;",
                    "Thou shalt not always see this youth shine bright, let not dull ignorance lead thee astray:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "चरख़ा तेरा रंग रंगीला, रीस करेंदा सभ कबीला,  ",
                    "चलदे चारे कर लै हीला, हो घर दे विच आवादान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "चरख़ा (चरखा) तेरा (तेरा) रंग (रंग-) रंगीला (रंगीला/सुंदर), रीस (ईर्ष्या/स्पर्धा) करेंदा (करता है) सभ (समस्त) कबीला (कुनबा/परिवार),",
                    "चलदे (चलते हुए जीवन में) चारे (उपाय रहते) कर (कर) लै (ले) हीला (यत्न/साधना), हो (हो जा) घर (ससुराल के घर) दे (के) विच (में) आवादान (प्रतिष्ठित/सुखी) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "चरख़ा (spinning wheel) तेरा (thine) रंग (splendidly) रंगीला (adorned), रीस (envy) करेंदा (does) सभ (whole) कबीला (clan/tribe),",
                    "चलदे (while it turns) चारे (remedy/time) कर (make) लै (take) हीला (effort), हो (become) घर (home) दे (of) विच (in) आवादान (honored/flourishing) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "चरखा तेरा रंग-रंगीला, सारा कुनबा रीझ रहा,",
                    "साधन रहते कर ले यत्न, घर में सुख-समृद्धि लहा ।",
                    "कर कातने पर ध्यान कुड़े !"
                ],
                "poetic_english": [
                    "Thy spinning-wheel is wondrous, bright and grand, envied by all the kin that gather round;",
                    "While breath still moves, stretch forth thy willing hand, that in thy Husband's mansion peace be found:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "इस चरख़े दी कीमत भारी, तूं की जाने कदर गवारी,  ",
                    "उच्ची नज़र फिरें हंकारी, विच आपने शान गुमान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "इस (इस) चरख़े (चरखे) दी (की) कीमत (मूल्य) भारी (अमूल्य/महान), तूं (तू) की (क्या) जाने (जानेगी) कदर (कद्र) गवारी (हे गंवार/अज्ञानी),",
                    "उच्ची (ऊंची) नज़र (दृष्टि किए) फिरें (घूमती है) हंकारी (अहंकारिणी), विच (में) आपने (अपनी झूठी) शान (शान) गुमान (घमंड में) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "इस (of this) चरख़े (spinning wheel) दी (of) कीमत (price/worth) भारी (boundless), तूं (thou) की (what) जाने (knowest) कदर (value) गवारी (rustic fool),",
                    "उच्ची (lofty) नज़र (gaze) फिरें (wanderest) हंकारी (arrogant), विच (in) आपने (thine own) शान (glory) गुमान (vanity) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "इस चरखे का मूल्य अपार, तू क्या जाने मूढ़ गंवार !",
                    "ऊँची दृष्टि अहंकार में डोले, झूठी शान-गुमान सँवार ।",
                    "कर कातने पर ध्यान कुड़े !"
                ],
                "poetic_english": [
                    "Priceless this wheel, beyond all gems and gold, how canst thou know its worth, O rustic blind?",
                    "With haughty glance and arrogance untold, strutting in foolish vanities of mind:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "मैं कूकां कर खलियां बाहीं, ना हो ग़ाफ़ल समझ कदाईं,  ",
                    "ऐसा चरख़ा घड़ना नाहीं. फेर किसे तरखान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "मैं (मैं) कूकां (पुकारता हूँ) कर (फैलाकर) खलियां (खड़ी/उठाकर) बाहीं (दोनों बाहें), ना (मत) हो (हो) ग़ाफ़ल (गाफिल/असावधान) समझ (समझ) कदाईं (कभी तो),",
                    "ऐसा (ऐसा दिव्य) चरख़ा (चरखा/मानव शरीर) घड़ना (गढ़ेगा) नाहीं (नहीं), फेर (पुनः) किसे (कोई भी) तरखान (बढ़ई/स्रष्टा) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "मैं (I) कूकां (cry aloud) कर (lifting) खलियां (outstretched) बाहीं (arms), ना (not) हो (be) ग़ाफ़ल (heedless) समझ (understand) कदाईं (ever),",
                    "ऐसा (such a) चरख़ा (wheel) घड़ना (will fashion) नाहीं (never), फेर (again) किसे (any) तरखान (carpenter/maker) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "दोनों बाहें उठा पुकारूँ: मत गाफ़िल हो, सुन ले बात,",
                    "ऐसा चरखा फिर न गढ़ेगा कोई बढ़ई दिन या रात !",
                    "कर कातने पर ध्यान कुड़े !"
                ],
                "poetic_english": [
                    "With arms outstretched I cry with all my might: shake off thy sleep, take heed before the fall!",
                    "No carpenter can carve with sacred light a wheel like this again upon this ball:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "इह चरख़ा तूं क्यों गवाया, क्यों तूं खेह दे विच रुलाया,  ",
                    "जद दा हत्थ तेरे विच आया, तूं कदे ना डाहआ आण कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "इह (यह) चरख़ा (चरखा) तूं (तूने) क्यों (क्यों) गवाया (व्यर्थ खो दिया), क्यों (क्यों) तूं (तूने) खेह (धूल/मिट्टी) दे (के) विच (में) रुलाया (रौंद दिया/धूल-धूसरित किया),",
                    "जद (जब) दा (से) हत्थ (हाथ) तेरे (तेरे) विच (में) आया (आया है), तूं (तूने) कदे (कभी) ना (नहीं) डाहआ (जोड़ा/चलाया) आण (आकर) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "इह (this) चरख़ा (wheel) तूं (thou) क्यों (why) गवाया (squandered), क्यों (why) तूं (thou) खेह (dust/dirt) दे (of) विच (in) रुलाया (dragged/soiled),",
                    "जद (since) दा (when) हत्थ (hands) तेरे (thy) विच (in) आया (came), तूं (thou) कदे (ever) ना (never) डाहआ (set up to spin) आण (coming) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "यह चरखा क्यों व्यर्थ गँवाया, क्यों मिट्टी में धूल मिलाई ?",
                    "जब से हाथों में यह आया, कातने की न सुध उपजाई ।",
                    "कर कातने पर ध्यान कुड़े !"
                ],
                "poetic_english": [
                    "Why hast thou cast this holy gift aside, dragging its beauty in the earthly dust?",
                    "Since into hands of thine it did abide, never didst set it spinning in pure trust:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "नित्त मतीं द्यां वलल्ली नूं, इस भोली कमली झल्ली नूं,  ",
                    "जद पवेगा वख़त इकल्ली नूं, तद हाए हाए करसी जान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "नित्त (नित्य) मतीं (शिक्षा) द्यां (देता हूँ) वलल्ली (अलबेली/मूर्ख) नूं (को), इस (इस) भोली (भोली) कमली (पगली) झल्ली (पागल) नूं (को),",
                    "जद (जब) पवेगा (पड़ेगा) वख़त (कठिन समय/यम का प्रकोप) इकल्ली (अकेली) नूं (पर), तद (तब) हाए (हाय) हाए (हाय) करसी (करेगी) जान (तेरी जान/प्राण) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "नित्त (daily) मतीं (counsel) द्यां (I give) वलल्ली (to the reckless) नूं (to), इस (this) भोली (simple) कमली (crazy) झल्ली (foolish girl) नूं (to),",
                    "जद (when) पवेगा (falls) वख़त (dire hour) इकल्ली (upon her alone) नूं (to), तद (then) हाए (alas) हाए (alas) करसी (will cry) जान (thy soul) कुड़े (O maiden) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "नित्य समझाऊँ इस पगली को, भोली-भाली बे-सुध छोरी,",
                    "जब संकट में अकेली होगी, तड़पेगी यह जान निगोड़ी !",
                    "कर कातने पर ध्यान कुड़े !"
                ],
                "poetic_english": [
                    "Daily I counsel this distracted soul, this naive, wild and foolish maiden here;",
                    "When lonely trials upon thy spirit roll, then shalt thou wail 'Alas!' in trembling fear:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "मुढों दी तूं रिज़क वेहूणी, गोहड़्युं ना तूं कत्ती पूणी,  ",
                    "हुन क्यों फिरनी एं निंमोझूणी, किस दा करें गुमान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "मुढों (आरंभ) दी (से ही) तूं (तू) रिज़क (जीविका/पुण्य-धन से) वेहूणी (वंचित/रिक्त), गोहड़्युं (रुई के ढेर से) ना (नहीं) तूं (तूने) कत्ती (काती) पूणी (एक भी पूनी/सूत),",
                    "हुन (अब) क्यों (क्यों) फिरनी (घूमती) एं (है) निंमोझूणी (उदास/सिर झुकाए), किस (किसका) दा (का) करें (करती है) गुमान (घमंड) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "मुढों (from the start) दी (of) तूं (thou) रिज़क (sustenance/grace) वेहूणी (bereft), गोहड़्युं (from cotton bales) ना (not) तूं (thou) कत्ती (spun) पूणी (a skein),",
                    "हुन (now) क्यों (why) फिरनी (wanderest) एं (thou) निंमोझूणी (downcast/crestfallen), किस (whose) दा (of) करें (dost boast) गुमान (vanity) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "शुरू से ही तू रिक्त-हस्त है, रुई से न एक पूनी काती,",
                    "अब क्यों घूमे उदास-मना तू, किस बूते पर गर्व सजाती ?",
                    "कर कातने पर ध्यान कुड़े !"
                ],
                "poetic_english": [
                    "Destitute from the start of spirit's bread, from fluffy bolls not one thread didst thou spin;",
                    "Why wander crestfallen with drooping head? What vanity is this thou nursest in?",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "ना तक्कला रास करावें तूं, ना बायड़ माल्ह पवावें तूं,  ",
                    "क्यों घड़ी मुड़ी चरख़ा चावें तूं, तूं करनी एं आपना ज़्यान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "ना (न तो) तक्कला (तकला/तकली) रास (सीधी/ठीक) करावें (कराती है) तूं (तू), ना (न) बायड़ (धुरी) माल्ह (चरखे की डोरी/माला) पवावें (डलवाती है) तूं (तू),",
                    "क्यों (क्यों) घड़ी (बार-) मुड़ी (बार) चरख़ा (चरखे को) चावें (उठाती/हिलाती है) तूं (तू), तूं (तू) करनी (करती) एं (है) आपना (अपना ही) ज़्यान (नुकसान/हानि) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "ना (neither) तक्कला (spindle) रास (straight/aligned) करावें (hast set) तूं (thou), ना (nor) बायड़ (bearing) माल्ह (driving-cord) पवावें (fitted) तूं (thou),",
                    "क्यों (why) घड़ी (again) मुड़ी (and again) चरख़ा (wheel) चावें (liftest/shift) तूं (thou), तूं (thou) करनी (dost) एं (art) आपना (thine own) ज़्यान (harm/loss) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "न तकली साधी, न डोरी डाली, चरखा बारम्बार हिलाए,",
                    "अपने हाथों अपना ही अहित, क्यों तू करती जाए ?"
                ],
                "poetic_english": [
                    "The spindle crooked, cord untied and loose, shifting the wheel from place to place in vain;",
                    "What profits this evasion and excuse? Thou workest thine own lasting loss and pain:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "डिंगा तक्कला रास करा लै, नाल शताबी बायड़ पवा लै,  ",
                    "ज्युं कर वगे तिवें वगा लै, मत कर कोई अगिआन कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "डिंगा (टेढ़ा) तक्कला (तकला) रास (सीधा) करा (करा) लै (ले), नाल (साथ में) शताबी (शीघ्रता से) बायड़ (धुरी/डोरी) पवा (डाल) लै (ले),",
                    "ज्युं (जैसे) कर (भी) वगे (घूमे/चले) तिवें (वैसे ही) वगा (चला) लै (ले), मत (मत) कर (कर) कोई (कोई) अगिआन (अज्ञान) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "डिंगा (crooked) तक्कला (spindle) रास (straight) करा (make) लै (have), नाल (with) शताबी (haste/speed) बायड़ (bearings) पवा (string) लै (take),",
                    "ज्युं (as) कर (how) वगे (spins) तिवें (so) वगा (spin it) लै (let), मत (do not) कर (commit) कोई (any) अगिआन (ignorance) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "टेढ़े तकले को सीधा करवा, शीघ्र चरखे में माल चढ़ा ले,",
                    "जैसे भी घूमे इसे घुमा, मत अज्ञान में जन्म गँवा ले !"
                ],
                "poetic_english": [
                    "Straighten the crooked spindle with all speed, tighten the driving-cord without delay;",
                    "Spin as it spins to meet the soul's deep need, cast all foolish delusions far away:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "अज्ज घर विच नवीं कपाह कुड़े, तूं झब झब वेलना डाह कुड़े,  ",
                    "रूं वेल पिंजावन जाह कुड़े, मुड़ कल्ल्ह ना तेरा जान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "अज्ज (आज) घर (घर) विच (में) नवीं (नयी) कपाह (कपास/श्वासों की पूंजी) कुड़े (हे कन्या), तूं (तू) झब (जल्दी-) झब (जल्दी) वेलना (बेलना/कपास ओटने का यंत्र) डाह (लगा) कुड़े,",
                    "रूं (रुई को) वेल (ओटकर) पिंजावन (धुनाने) जाह (जा) कुड़े, मुड़ (पुनः) कल्ल्ह (कल का) ना (नहीं) तेरा (तेरा) जान (कोई भरोसा/ज्ञान) कुड़े ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "अज्ज (today) घर (home) विच (in) नवीं (fresh) कपाह (cotton) कुड़े (O girl), तूं (thou) झब (quickly) झब (swiftly) वेलना (ginning-frame) डाह (set up) कुड़े,",
                    "रूं (cotton) वेल (gin) पिंजावन (to card) जाह (go) कुड़े, मुड़ (again) कल्ल्ह (tomorrow) ना (not) तेरा (thine) जान (known/certain) कुड़े ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "घर में नयी कपास पड़ी है, जल्दी-जल्दी बेलन डाह,",
                    "ओट रुई, धुनवाने जा तू, कल का किसको पता अहा ?"
                ],
                "poetic_english": [
                    "Fresh cotton bolls within thy home abide, set up the ginning-frame with eager speed;",
                    "Cleanse and prepare the lint in morning-tide, of coming morrows no one can take heed:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "जद रूं पंजा लिआवेंगी, सईआं विच पूणियां पावेंगी,  ",
                    "मुड़ आप ही पई भावेंगी, विच सारे जग्ग जहान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "जद (जब) रूं (रुई) पंजा (धुनाकर) लिआवेंगी (लाएगी), सईआं (सखियों के) विच (बीच) पूणियां (पूनियां) पावेंगी (बनाकर रखेगी),",
                    "मुड़ (तब) आप (स्वयं) ही (ही) पई (होकर) भावेंगी (शोभा पाएगी/प्रिय लगेगी), विच (में) सारे (सारे) जग्ग (जग-) जहान (संसार) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "जद (when) रूं (cotton) पंजा (carded) लिआवेंगी (thou bringest), सईआं (companions) विच (among) पूणियां (skeins) पावेंगी (rollest),",
                    "मुड़ (then) आप (thyself) ही (alone) पई (shalt) भावेंगी (be pleasing/honored), विच (in) सारे (all) जग्ग (world) जहान (creation) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "जब रुई धुना कर लाएगी, सखियों संग पूनी बनाएगी,",
                    "तब जग-जहान में शोभा पाकर, सबके मन को भाएगी !"
                ],
                "poetic_english": [
                    "When soft, clean cotton carded thou dost bring, rolling neat skeins amid the maiden band;",
                    "Then shall thy praises through the village ring, beloved and honored across all the land:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "तेरे नाल दियां सभ सईआं ने, कत्त पूणियां सभना लईआं ने,  ",
                    "तैनूं बैठी नूं पिछों पईआं ने, क्यों बैठी एं हुन हैरान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "तेरे (तेरे) नाल (साथ) दियां (की) सभ (समस्त) सईआं (सखियों) ने (ने), कत्त (कातकर) पूणियां (पूनियां) सभना (सबने) लईआं (तैयार कर ली) ने,",
                    "तैनूं (तुझे) बैठी (बैठे-बैठे) नूं (को) पिछों (पीछे से) पईआं (विपदाएं आ पड़ीं) ने, क्यों (क्यों) बैठी (बैठी) एं (है) हुन (अब) हैरान (हैरान/स्तब्ध) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "तेरे (thy) नाल (companion) दियां (of) सभ (all) सईआं (friends) ने (have), कत्त (spinning) पूणियां (skeins) सभना (all of them) लईआं (gathered/finished) ने,",
                    "तैनूं (unto thee) बैठी (seated) नूं (to) पिछों (from behind) पईआं (troubles descended) ने, क्यों (why) बैठी (seated) एं (art) हुन (now) हैरान (bewildered) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "साथ की सखियों ने कात लिया, सूत का ढेर लगाया है,",
                    "तू बैठी रही अचेत यहाँ, अब सिर पर संकट आया है !"
                ],
                "poetic_english": [
                    "All of thy peers have spun their cotton fine, their baskets laden with the finished thread;",
                    "While idle thou didst waste this youth of thine, bewildered now beneath a sky of dread:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "दीवा आपने पास जगावीं, कत्त कत्त सूत भड़ोली पावीं,  ",
                    "अक्खीं विचों रात लंघावीं, औखी करके जान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "दीवा (ज्ञान का दीपक) आपने (अपने) पास (समीप) जगावीं (जला लेना), कत्त (कात-) कत्त (कातकर) सूत (सूत/धागा) भड़ोली (अन्न-कोठरी/मटके में) पावीं (डालती जाना),",
                    "अक्खीं (आँखों) विचों (में से ही) रात (रात) लंघावीं (बिताना/जागना), औखी (कष्ट सहकर) करके (करके) जान (प्राणों को) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "दीवा (lamp) आपने (thine own) पास (beside) जगावीं (kindle), कत्त (spinning) कत्त (spinning) सूत (yarn) भड़ोली (storage bin) पावीं (put),",
                    "अक्खीं (through the eyes) विचों (from) रात (night) लंघावीं (pass/remain wakeful), औखी (enduring hardship) करके (making) जान (life) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "पास जला ले ज्ञान का दीया, कात-कात कर सूत सँभाल,",
                    "जाग-जाग कर रात बिता ले, कष्ट सह कर जीवन ढाल !"
                ],
                "poetic_english": [
                    "Kindle the lamp of awareness by thy side, store skeins of yarn within the earthen bin;",
                    "Through watchful eyes let starry midnights glide, enduring toil until the dawn breaks in:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "राज पेका दिन चार कुड़े, ना खेडो खेड गुज़ार कुड़े,  ",
                    "ना हो वेहली कर कार कुड़े, घर बार ना कर वीरान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "राज (सुख-चैन) पेका (मायके का) दिन (दिन) चार (चार दिन का ही है) कुड़े (हे कन्या), ना (मत) खेडो (खेल ही) खेड (खेल में) गुज़ार (बिता) कुड़े,",
                    "ना (मत) हो (हो) वेहली (निठल्ली/आलसी) कर (कर) कार (सत्कर्म/श्रम) कुड़े, घर (हृदय का घर-) बार (संसार) ना (मत) कर (कर) वीरान (उजाड़/नष्ट) कुड़े ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "राज (sovereignty/comfort) पेका (of parents’ home) दिन (days) चार (four brief days) कुड़े (O girl), ना (not) खेडो (in play) खेड (idle game) गुज़ार (spend) कुड़े,",
                    "ना (do not) हो (be) वेहली (idle) कर (do) कार (virtuous toil) कुड़े, घर (home) बार (hearth) ना (do not) कर (make) वीरान (desolate) कुड़े ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "चार दिनों का मायका री, खेल-कूद में मत गँवा,",
                    "आलस तज कर कर्म संभाल, घर-बार न कर वीरान बना !"
                ],
                "poetic_english": [
                    "Four fleeting days this parents' home remains, waste not the hours in empty juvenile play;",
                    "Shun lazy sloth, endure the noble pains, leave not thy inner garden to decay:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "तूं सुत्यां रैन गुज़ार नहीं, मुड़ आउना दूजी वार नहीं,  ",
                    "फिर बहना एस भंडार नहीं, विच इको जेडे हान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "तूं (तू) सुत्यां (सोते हुए) रैन (जीवन-रात्रि) गुज़ार (व्यतीत) नहीं (मत कर), मुड़ (पुनः) आउना (आना) दूजी (दूसरी) वार (बार) नहीं (नहीं होगा),",
                    "फिर (फिर) बहना (बैठना) एस (इस) भंडार (संसार-मंडप में) नहीं (नहीं होगा), विच (बीच में) इको (एक ही) जेडे (समान आयु के) हान (हमउम्र सखियों के) कुड़े ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "तूं (thou) सुत्यां (in sleep) रैन (night) गुज़ार (spend) नहीं (not), मुड़ (again) आउना (to come) दूजी (second) वार (time) नहीं (never),",
                    "फिर (then) बहना (to sit) एस (this) भंडार (spinning circle/assembly) नहीं (never), विच (among) इको (equal) जेडे (age) हान (peers) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "सोते हुए यह रैन न खो, दूजी बार न आना होगा,",
                    "इस सखी-मंडली के बीच, फिर कभी न बैठ पाना होगा !"
                ],
                "poetic_english": [
                    "Pass not in slumber this ephemeral night, never a second time shalt thou return;",
                    "No more to sit within this circle bright, with youthful companions for the truth to yearn:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "तूं सदा ना पेके रहना एं, ना पास अम्बड़ी दे बहना एं,  ",
                    "भा अंत विछोड़ा सहना एं, वस्स पएंगी सस्स ननान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "तूं (तू) सदा (सदा) ना (नहीं) पेके (मायके/संसार में) रहना (रहना) एं (है), ना (न) पास (पास) अम्बड़ी (अम्बा/माता) दे (के) बहना (बैठना) एं (है),",
                    "भा (अवश्य) अंत (अंततः) विछोड़ा (वियोग) सहना (सहना) एं (है), वस्स (वश में) पएंगी (पड़ेगी) सस्स (सास—मृत्यु/कर्मफल) ननान (ननद—कठोर परीक्षा) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "तूं (thou) सदा (forever) ना (not) पेके (in father’s home) रहना (stay) एं (shalt), ना (nor) पास (beside) अम्बड़ी (mother) दे (of) बहना (sit) एं (shalt),",
                    "भा (surely) अंत (at the end) विछोड़ा (parting) सहना (endure) एं (must), वस्स (under dominion) पएंगी (wilt fall) सस्स (mother-in-law) ननान (sister-in-law) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "सदा न रहना मायके में, सदा न अम्मा का संग मिले,",
                    "अंत विछोह सहना ही होगा, सास-ननद के फंदे पड़े !"
                ],
                "poetic_english": [
                    "Forever in this home thou canst not bide, nor sit beside thy mother's loving knee;",
                    "At last severe departure must betide, when in-laws claim their grim authority:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "कत्त लै नी कुझ कता लै नी, हुन तानी तन्द उना लै नी,  ",
                    "तूं आपना दाज रंगा लै नी, तूं तद होवें परधान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "कत्त (कात) लै (ले) नी (अरी) कुझ (कुछ) कता (कतवा) लै (ले) नी,",
                    "हुन (अब) तानी (ताना) तन्द (धागा) उना (बुनवा) लै (ले) नी,",
                    "तूं (तू) आपना (अपना) दाज (दहेज/परलोक का वस्त्र) रंगा (रंगवा) लै (ले) नी, तूं (तू) तद (तब ही) होवें (होगी) परधान (प्रधान/मान्य) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "कत्त (spin) लै (take) नी (O) कुझ (something) कता (get spun) लै (take) नी,",
                    "हुन (now) तानी (warp) तन्द (threads) उना (weave) लै (take) नी,",
                    "तूं (thou) आपना (thy) दाज (trousseau/dowry) रंगा (dye) लै (take) नी, तूं (thou) तद (then alone) होवें (shalt be) परधान (exalted/honored) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "कुछ कात ले, कुछ बुनवा ले री, ताना-बाना सजवा ले री,",
                    "रंग ले अपना सुंदर दहेज, तब ससुराल में मान पा ले री !"
                ],
                "poetic_english": [
                    "Spin out some yarn, weave warp and weft today, dye the bridal robes in colors sweet;",
                    "Adorn thy dowry while thou hast the way, that thou with dignity the King may meet:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "जद घर बेगाने जावेंगी, मुड़ वत्त ना ओथों आवेंगी,  ",
                    "ओथे जा के पछोतावेंगी, कुझ अगदों कर सम्यान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "जद (जब) घर (ससुराल के घर) बेगाने (अनजान लोक में) जावेंगी (जाएगी), मुड़ (पुनः) वत्त (फिर) ना (नहीं) ओथों (वहाँ से) आवेंगी (लौटेगी),",
                    "ओथे (वहाँ) जा (जा-) के (कर) पछोतावेंगी (पछताएगी), कुझ (कुछ) अगदों (आगे के लिए/पहले से) कर (कर ले) सम्यान (सामान/पाथेय) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "जद (when) घर (to house) बेगाने (stranger’s/afterlife) जावेंगी (thou goest), मुड़ (again) वत्त (ever) ना (not) ओथों (thence) आवेंगी (wilt return),",
                    "ओथे (there) जा (going) के (having) पछोतावेंगी (wilt repent), कुझ (some) अगदों (in advance) कर (gather) सम्यान (provisions/dowry) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "जब पराये घर जाएगी, फिर लौट कभी न आएगी,",
                    "वहाँ जा कर पछताएगी, पहले से ही कुछ सामान जुटा ले री !"
                ],
                "poetic_english": [
                    "Once carried to that strange and distant shore, never again shalt thou return to play;",
                    "Bitter repentance waits behind that door—prepare provisions for the lonely way:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "अज्ज ऐडा तेरा कंम कुड़े, क्यों होई एं बे-ग़म कुड़े ,  ",
                    "कीकर लैना उस दंम कुड़े, जद घर आए महमान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "अज्ज (आज) ऐडा (इतना बड़ा) तेरा (तेरा) कंम (कार्य/दायित्व है) कुड़े,",
                    "क्यों (क्यों) होई (हो गई) एं (है) बे-ग़म (निश्चिंत/लापरवाह) कुड़े,",
                    "कीकर (कैसे) लैना (श्वास लेना संभव होगा) उस (उस) दंम (क्षण) कुड़े, जद (जब) घर (घर में) आए (आ पहुँचेंगे) महमान (मेहमान—यमदूत/बाराती) कुड़े ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "अज्ज (today) ऐडा (such immense) तेरा (thy) कंम (task) कुड़े (O girl),",
                    "क्यों (why) होई (become) एं (art) बे-ग़म (careless/complacent) कुड़े,",
                    "कीकर (how) लैना (to draw) उस (that) दंम (breath) कुड़े, जद (when) घर (at home) आए (arrive) महमान (guests/messengers of death) कुड़े ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "इतना भारी काम है सिर पर, क्यों निश्चिंत बनी है तू ?",
                    "श्वास भी कैसे ले पाएगी, जब आ धमकेंगे मेहमान बहू !"
                ],
                "poetic_english": [
                    "A task so heavy rests upon thy head, why art thou lost in slumber's careless trance?",
                    "How shalt thou draw thy breath in sudden dread, when the unbidden guests of death advance?",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "जद सभ सईआं टुर जाणगियां, फिर ओथे मूल ना आउणगियां,  ",
                    "आ चरख़े मूल ना डाहुणगियां, तेरा त्रिंञन प्या वीरान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "जद (जब) सभ (समस्त) सईआं (सखियां) टुर (विदा होकर) जाणगियां (चली जाएंगी), फिर (फिर) ओथे (वहाँ/मायके में) मूल (कभी) ना (नहीं) आउणगियां (आएंगी),",
                    "आ (आकर) चरख़े (चरखे) मूल (कदापि) ना (नहीं) डाहुणगियां (जोड़ेंगी), तेरा (तेरा) त्रिंञन (त्रिंजन/सूत कातने का समूह-स्थल) प्या (पड़ा रहेगा) वीरान (सूना/उजाड़) कुड़े ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "जद (when) सभ (all) सईआं (companions) टुर (depart) जाणगियां (will go), फिर (again) ओथे (there) मूल (ever) ना (never) आउणगियां (will return),",
                    "आ (coming) चरख़े (wheels) मूल (at all) ना (not) डाहुणगियां (set up), तेरा (thy) त्रिंञन (spinning courtyard/assembly) प्या (lies) वीरान (desolate) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "सखियाँ सब विदा हो जाएँगी, फिर लौट कभी न आएँगी,",
                    "चरखे न कभी यहाँ जुड़ेंगे, त्रिंजन सूना कर जाएँगी !"
                ],
                "poetic_english": [
                    "When all thy comrades to their grooms are gone, never again to assemble in this hall;",
                    "No spinning-wheel will turn at early dawn, and silent dust upon the court will fall:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "कर मान ना हुसन जवानी दा, परदेस ना रहन सैलानी दा,  ",
                    "कोई दुनियां झूठी फ़ानी दा, ना रहसी नाम निशान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "कर (कर) मान (घमंड) ना (मत) हुसन (रूप) जवानी (तथा यौवन) दा (का), परदेस (पराए देश में) ना (नहीं) रहन (स्थायी निवास होता) सैलानी (सैलानी/मुसाफिर) दा (का),",
                    "कोई (इस) दुनियां (संसार) झूठी (झूठी) फ़ानी (नश्वर) दा (का), ना (नहीं) रहसी (रहेगा) नाम (नाम-) निशान (निशान) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "कर (make) मान (pride) ना (not) हुसन (beauty) जवानी (youth) दा (of), परदेस (foreign land) ना (not) रहन (permanent stay) सैलानी (traveler) दा (of),",
                    "कोई (of this) दुनियां (world) झूठी (false) फ़ानी (transient) दा (of), ना (not) रहसी (shall remain) नाम (name) निशान (trace) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "रूप-जवानी का गर्व न कर, परदेसी का क्या टिकना यहाँ ?",
                    "यह नश्वर संसार है झूठा, नाम-निशान न बचना यहाँ !"
                ],
                "poetic_english": [
                    "Boast not of youthful bloom or transient grace, no wanderer settles in a foreign land;",
                    "This fleeting world leaves not a single trace, swept like dry embers on the barren sand:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            },
            {
                "original": [
                    "इक औखा वेला आवेगा, सभ साक सैन भज्ज जावेगा,  ",
                    "कर मदत पार लंघावेगा, उह बुल्ल्हे दा सुलतान कुड़े ।  ",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "hindi_gloss": [
                    "इक (एक) औखा (अति कठिन) वेला (समय/मृत्यु-वेला) आवेगा (आएगा), सभ (समस्त) साक (सगे-) सैन (संबंधी) भज्ज (भाग/छूट) जावेगा (जाएगा),",
                    "कर (करके) मदत (सहायता) पार (भवसागर से पार) लंघावेगा (उतारेगा), उह (वही) बुल्ल्हे (बुल्ले) दा (का) सुलतान (सुल्तान/मुर्शिद शाह इनायत) कुड़े (हे कन्या) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "english_gloss": [
                    "इक (a) औखा (hard/dreaded) वेला (hour) आवेगा (shall arrive), सभ (all) साक (kin) सैन (relatives) भज्ज (flee away) जावेगा (will),",
                    "कर (doing) मदत (succor/aid) पार (across the abyss) लंघावेगा (shall ferry thee), उह (He alone) बुल्ल्हे (Bulleh’s) दा (of) सुलतान (Sultan/Master Shah Inayat) कुड़े (O girl) ।",
                    "कर कत्तन वल्ल ध्यान कुड़े ।"
                ],
                "poetic_hindi": [
                    "एक कठिन वेला आएगी, जब सगे-संबंधी भागेंगे,",
                    "बस बुल्ल्हे का सुल्तान ही आकर, पार तुझे उतारेगा !"
                ],
                "poetic_english": [
                    "A fearful hour of reckoning will arrive, when all false kin and comrades take to flight;",
                    "Bulleh’s Great Sultan only shall arrive, to ferry thee across the darkest night:",
                    "Turn to thy spinning-wheel, O maiden fair!"
                ]
            }
        ],
        "philosophical_meaning": "यह 24 अंतरे का प्रबंध-काव्य सूफी 'चरखा-नामा' का अप्रतिम शिखर है। चरखे के प्रत्येक अंग का आध्यात्मिक अर्थ है: चामड़ (काया), तकला (मन), माल (प्रेम की डोरी), पूनी (सत्कर्म), सूत (स्मरण)। बुल्ले शाह चेतावनी देते हैं कि जीवन का मायका क्षणभंगुर है। जब मृत्यु रूपी ससुराल का बुलावा आएगा, तो केवल वही आत्मा परमात्मा (दूल्हे) के सम्मुख सम्मानित होगी जिसने 'सूत' (साधना) एकत्र किया है। अंतिम पद में वे अपने मुर्शिद (बुल्ल्हे दा सुलतान) को ही अंतिम उद्धारक बताते हैं।"
    },
    {
        "id": 64,
        "title": "कत्त कुड़े ना वत्त कुड़े",
        "title_english": "Spin, O Maiden, Do Not Wander In Vain!",
        "historical_context": "यह काफी भी चरखा-काव्य की श्रृंखला का भाग है। इसमें जीवात्मा को हिदायत दी गई है कि वह समय रहते अपने सूत की 'छल्ली' (अटी) उतार कर 'भड़ोले' (कोठरी) में सहेज ले। जो आत्मा जीवन भर आलस्य में दिन बिताती है, मृत्यु के पश्चात उसका कोई आदर नहीं होता।",
        "meter": "पंजाबी काफी (मात्रािक छंद, तुक: वत्त कुड़े / घत्त कुड़े / गत्त कुड़े)",
        "raga": "राग काफी / सोरठ",
        "theme": "साधना की तत्परता, समय का सदुपयोग, दहेज रूपी पुण्य, ईश्वर की प्रसन्नता",
        "stanzas": [
            {
                "original": [
                    "कत्त कुड़े ना वत्त कुड़े ।  ",
                    "छल्ली लाह भड़ोले घत्त कुड़े ।"
                ],
                "hindi_gloss": [
                    "कत्त (सूत कात) कुड़े (हे कन्या) ना (मत) वत्त (व्यर्थ भटक) कुड़े (हे सखी) ।",
                    "छल्ली (सूत की अटी/पिंड) लाह (उतारकर) भड़ोले (अन्न/सूत के मटके में) घत्त (डाल ले/सहेज ले) कुड़े ।"
                ],
                "english_gloss": [
                    "कत्त (spin) कुड़े (O girl) ना (not) वत्त (wander idle) कुड़े (O maiden) ।",
                    "छल्ली (the spun spool/hank) लाह (remove) भड़ोले (in the granary bin) घत्त (store) कुड़े (O girl) ।"
                ],
                "poetic_hindi": [
                    "कात री कन्या, व्यर्थ न डोल, सूत-अटी भड़ोले में खोल !"
                ],
                "poetic_english": [
                    "Spin, maiden, spin, and roam no more in vain, store in the bin thy skein of holy grain!"
                ]
            },
            {
                "original": [
                    "जे पूनी पूनी कत्तेंगी, तां नंगी मूल ना वत्तेंगी,  ",
                    "सै वर्हआं दे जे कत्तेंगी, तां काग मारेगा झट कुड़े ।  ",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "hindi_gloss": [
                    "जे (यदि) पूनी (पूनी-) पूनी (पूनी/एक-एक श्वास में) कत्तेंगी (कातेगी), तां (तो) नंगी (वस्त्रहीन/लज्जित) मूल (कदापि) ना (नहीं) वत्तेंगी (भटकेगी),",
                    "सै (सैकड़ों) वर्हआं (वर्षों) दे (का) जे (यदि) कत्तेंगी (कातती रहेगी/विलंब करेगी), तां (तो) काग (काल रूपी कौवा) मारेगा (मारेगा) झट (झपट्टा) कुड़े (हे कन्या) ।",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "english_gloss": [
                    "जे (if) पूनी (skein) पूनी (by skein) कत्तेंगी (thou spinnest), तां (then) नंगी (naked/destitute) मूल (at all) ना (not) वत्तेंगी (shalt wander),",
                    "सै (hundreds) वर्हआं (of years) दे (of) जे (if) कत्तेंगी (dost postpone/linger), तां (then) काग (the crow of death) मारेगा (shall strike) झट (sudden swoop) कुड़े (O girl) ।",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "poetic_hindi": [
                    "पूनी-पूनी कातेगी तो नग्न न डोलेगी कभी,",
                    "सौ वर्षों की ढिलाई की तो काल-काग झपटेगा अभी !"
                ],
                "poetic_english": [
                    "Spin skein by skein, so shalt thou never go naked and stripped before the judgment-throne;",
                    "If thou delayest through decades slow, the crow of death will claim thee for his own!"
                ]
            },
            {
                "original": [
                    "विच गफ़लत जे तैं दिन जाले, कत्त के कुझ ना ल्यु संभाले.  ",
                    "बाझों गुन शहु आपने नाले, तेरी क्यों कर होसी गत्त कुड़े ।  ",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "hindi_gloss": [
                    "विच (में) गफ़लत (लापरवाही/प्रमाद) जे (यदि) तैं (तूने) दिन (दिन) जाले (बिता दिए), कत्त (कात) के (कर) कुझ (कुछ भी) ना (नहीं) ल्यु (दहेज/वस्त्र) संभाले (सहेजे),",
                    "बाझों (बिना) गुन (गुणों के) शहु (प्रभु रूपी पति के) आपने (अपने) नाले (साथ), तेरी (तेरी) क्यों (कैसे) कर (करके) होसी (होगी) गत्त (सद्गति) कुड़े ।",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "english_gloss": [
                    "विच (in) गफ़लत (heedlessness) जे (if) तैं (thou) दिन (days) जाले (spent), कत्त (spinning) के (having) कुझ (anything) ना (not) ल्यु (trousseau) संभाले (secured),",
                    "बाझों (without) गुन (virtues) शहु (Lord) आपने (thine own) नाले (beside), तेरी (thy) क्यों (how) कर (manner) होसी (shall be) गत्त (deliverance/salvation) कुड़े (O girl) ।",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "poetic_hindi": [
                    "गाफ़िल रह कर दिन जो बिताए, कात के कुछ न वस्त्र सँभाले,",
                    "बिना गुणों के स्वामी-संग, सद्गति कौन तेरी करे निकाले ?"
                ],
                "poetic_english": [
                    "If days are passed in heedless, idle ease, storing no bridal garment for the soul;",
                    "Devoid of virtues canst thou the Master please? What hand can guide thee to salvation's goal?"
                ]
            },
            {
                "original": [
                    "मां प्यो तेरे गंढीं पाईआं, अजे ना तैनूं सुरतां आईआं,  ",
                    "दिन थोड़े ते चाय मकाईआं, ना आसें पेके वत्त कुड़े ।  ",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "hindi_gloss": [
                    "मां (माता) प्यो (पिता ने) तेरे (तेरे विवाह की) गंढीं (गांठें/लग्न-पत्रिकाएं) पाईआं (भेज दीं), अजे (अब तक) ना (नहीं) तैनूं (तुझे) सुरतां (होश/ज्ञान) आईआं (आई),",
                    "दिन (दिन) थोड़े (अल्प) ते (तथा) चाय (विवाह की तैयारी) मकाईआं (समाप्त होने को है), ना (नहीं) आसें (आएगी) पेके (मायके में) वत्त (फिर कभी) कुड़े ।",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "english_gloss": [
                    "मां (mother) प्यो (father) तेरे (thy) गंढीं (wedding-knots/invitations) पाईआं (have sent), अजे (yet) ना (not) तैनूं (to thee) सुरतां (awareness) आईआं (dawned),",
                    "दिन (days) थोड़े (few) ते (and) चाय (eagerness) मकाईआं (exhausted), ना (never) आसें (shalt return) पेके (to father’s home) वत्त (again) कुड़े (O girl) ।",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "poetic_hindi": [
                    "मात-पिता ने लग्न बाँध दी, तुझे अभी तक होश न आया,",
                    "दिन थोड़े हैं, विदा निकट है, फिर न मिलेगा मायका-साया !"
                ],
                "poetic_english": [
                    "Thy parents tied the wedding-knots today, yet no awareness dawns upon thy mind;",
                    "The days are few before they bear away, leaving this loving father's home behind!"
                ]
            },
            {
                "original": [
                    "जे दाज वेहूनी जावेंगी, तां किसे भली ना भावेंगी,  ",
                    "ओथे शहु नूं किवें रीझावेंगी, कुझ लै फ़करां दी मत्त कुड़े ।  ",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "hindi_gloss": [
                    "जे (यदि) दाज (दहेज/पुण्य-वस्त्र से) वेहूनी (विहीन/खाली हाथ) जावेंगी (जाएगी), तां (तो) किसे (किसी को भी) भली (अच्छी) ना (नहीं) भावेंगी (लगेगी),",
                    "ओथे (वहाँ ससुराल में) शहु (प्रभु-पति) नूं (को) किवें (कैसे) रीझावेंगी (प्रसन्न करेगी), कुझ (कुछ) लै (ले ले) फ़करां (फकीरों/संतों) दी (की) मत्त (शिक्षा/मति) कुड़े ।",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "english_gloss": [
                    "जे (if) दाज (dowry/virtue) वेहूनी (bereft) जावेंगी (thou goest), तां (then) किसे (to anyone) भली (pleasing) ना (not) भावेंगी (wilt appear),",
                    "ओथे (there) शहु (the Lord) नूं (unto) किवें (how) रीझावेंगी (wilt please), कुझ (some) लै (take) फ़करां (of dervishes) दी (of) मत्त (counsel) कुड़े (O girl) ।",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "poetic_hindi": [
                    "यदि दहेज बिन जाएगी तो किसी को भली न भाएगी,",
                    "कैसे स्वामी को रीझाएगी? कुछ संतों की मति ले री !"
                ],
                "poetic_english": [
                    "Bereft of dowry shouldst thou cross the door, no eye will welcome thee with tender gaze;",
                    "How wilt thou charm the Master evermore? Accept the dervish counsel for thy ways!"
                ]
            },
            {
                "original": [
                    "तेरे नाल दियां दाज रंगाए नी, ओहनां सूहे सालू पाए नी,  ",
                    "तूं पैर उलटे क्यों चाए नी, जा ओथे लग्गी तत्त कुड़े ।  ",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "hindi_gloss": [
                    "तेरे (तेरे) नाल (साथ) दियां (वालियों ने) दाज (दहेज) रंगाए (रंगवा लिए) नी, ओहनां (उन्होंने) सूहे (लाल/सुहाग के) सालू (चादर/दुपट्टे) पाए (पहन लिए) नी,",
                    "तूं (तूने) पैर (पैर) उलटे (उल्टे मार्ग पर) क्यों (क्यों) चाए (उठाए) नी, जा (जाकर) ओथे (वहाँ) लग्गी (लगेगी) तत्त (तप्त वायु/अग्नि) कुड़े (हे कन्या) ।",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "english_gloss": [
                    "तेरे (thy) नाल (companion) दियां (peers) दाज (dowry) रंगाए (have dyed) नी, ओहनां (they) सूहे (crimson) सालू (bridal shawls) पाए (have worn) नी,",
                    "तूं (thou) पैर (feet) उलटे (reversed/perverse) क्यों (why) चाए (hast lifted) नी, जा (going) ओथे (there) लग्गी (shall strike) तत्त (scorching blast) कुड़े (O girl) ।",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "poetic_hindi": [
                    "सखियों ने लाल चुनरियाँ ओढ़ीं, सुंदर दहेज रंगाया है,",
                    "तू उल्टे पथ पर क्यों डोले, आगे तपता साया है !"
                ],
                "poetic_english": [
                    "Thy peers have dyed their trousseaus richly bright, donning red bridal shawls of sacred grace;",
                    "Why set thy feet in backward paths of night, where scorching winds consume the resting place?"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु घर आपने आवे, चूड़ा बीड़ा सभ सुहावे,  ",
                    "गुन होसी तां गले लगावे, नहीं रोसें नैणीं रत्त कुड़े ।  ",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ला कहता है) शहु (प्रभु-पति) घर (घर में) आपने (अपने) आवे (जब आएगा), चूड़ा (सुहाग का चूड़ा) बीड़ा (पान का बीड़ा) सभ (सब कुछ) सुहावे (तभी शोभा पाता है),",
                    "गुन (यदि गुण) होसी (होंगे) तां (तो ही) गले (हृदय से) लगावे (लगाएगा), नहीं (अन्यथा) रोसें (रोएगी) नैणीं (नेत्रों से) रत्त (रक्त के आंसू) कुड़े (हे कन्या) ।",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh says) शहु (the Lord) घर (to home) आपने (His own) आवे (when comes), चूड़ा (bridal bangles) बीड़ा (betel fold) सभ (all) सुहावे (graceful appear),",
                    "गुन (virtues) होसी (if there be) तां (then) गले (to His bosom) लगावे (will embrace), नहीं (otherwise) रोसें (wilt weep) नैणीं (from eyes) रत्त (tears of blood) कुड़े (O girl) ।",
                    "कत्त कुड़े ना वत्त कुड़े ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा शौह जब घर आएँगे, चूड़ा-बीड़ा सब भाएगा,",
                    "गुण होंगे तो गले लगाएगा, नहीं नैनों से रक्त बहाएगा !"
                ],
                "poetic_english": [
                    "When Bulleh’s Lord enters His bridal home, bangles and betel shine in radiant grace;",
                    "If virtues dwell within, He bids thee come; else tears of blood shall wash thy weeping face!"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी चेतावनी और आत्म-निरीक्षण का गीत है। परमात्मा का मिलन केवल बाह्य आभूषणों (चूड़ा-बीड़ा) से नहीं, बल्कि आंतरिक आध्यात्मिक साधना (गुण) से संभव है। यदि जीवन काल में परमात्मा का 'सूत' (नाम-स्मरण) नहीं काता गया, तो जीवात्मा को परलोक में 'नैनों से रक्त' रोना पड़ेगा।"
    },
    {
        "id": 65,
        "title": "कौन आया पहन लिबास कुड़े",
        "title_english": "Who Has Arrived Donning This Garb, O Maidens?",
        "historical_context": "यह हीर-रांझा के आख्यान पर आधारित एक अत्यंत रहस्यमयी और रसपूर्ण सूफी काफी है। रांझा जब हीर की खोज में भैंसों का चरवाहा (चाक) बनकर आता है, तो सखियां उसके अलौकिक सौंदर्य और आंखों के नूर को देखकर चकित रह जाती हैं। बुल्ले शाह कहते हैं कि वह साधारण चरवाहा नहीं, बल्कि स्वयं साक्षात परमात्मा है जो प्रेम के वशीभूत होकर सेवक का वेश धारण करके आया है।",
        "meter": "पंजाबी काफी (चतुष्पदी, अंत्यानुप्रास लिबास/इख़लास/पास/तलाश)",
        "raga": "राग काफी / तिलक कामोद",
        "theme": "हीर-रांझा रूपक, परमात्मा का मानवरूप में आगमन, सच्चे आशिक की पहचान",
        "stanzas": [
            {
                "original": [
                    "कौन आया पहन लिबास कुड़े ।  ",
                    "तुसीं पुच्छो नाल इख़लास कुड़े ।"
                ],
                "hindi_gloss": [
                    "कौन (कौन महापुरुष) आया (आया है) पहन (पहनकर) लिबास (यह विचित्र वेश/कमली) कुड़े (हे सखियो) ।",
                    "तुसीं (तुम सब) पुच्छो (पूछो) नाल (के साथ) इख़लास (सच्चे आदर/प्रेम) कुड़े (हे सखियो) ।"
                ],
                "english_gloss": [
                    "कौन (who) आया (has come) पहन (wearing) लिबास (this attire/garb) कुड़े (O maidens) ।",
                    "तुसीं (ye) पुच्छो (inquire) नाल (with) इख़लास (sincere devotion/love) कुड़े (O friends) ।"
                ],
                "poetic_hindi": [
                    "कौन आया पहन लिबास सखी ? तुम पूछो प्रेम के साथ सखी !"
                ],
                "poetic_english": [
                    "Who hath arrived in this disguise, O friends? Inquire with love and reverence in your eyes!"
                ]
            },
            {
                "original": [
                    "हत्थ खूंडी कम्बल काला, अक्खियां विच वसे उजाला,  ",
                    "चाक नहीं कोई है मतवाला, पुच्छो बिठा के पास कुड़े ।  ",
                    "कौन आया पहन लिबास कुड़े ।"
                ],
                "hindi_gloss": [
                    "हत्थ (हाथ में) खूंडी (लाठी/कूबड़ी) कम्बल (कंबल) काला (काला है), अक्खियां (नेत्रों) विच (में) वसे (बसता है) उजाला (दिव्य आलोक),",
                    "चाक (साधारण चरवाहा/सेवक) नहीं (नहीं है) कोई (वह तो कोई) है (है) मतवाला (मस्ताना/अवधूत), पुच्छो (पूछो) बिठा (बिठाकर) के (के) पास (अपने पास) कुड़े (हे सखियो) ।",
                    "कौन आया पहन लिबास कुड़े ।"
                ],
                "english_gloss": [
                    "हत्थ (in hand) खूंडी (crook/staff) कम्बल (blanket) काला (black), अक्खियां (in eyes) विच (within) वसे (dwells) उजाला (radiant light),",
                    "चाक (herdsman/servant) नहीं (is not) कोई (someone) है (is) मतवाला (ecstatic divine lover), पुच्छो (inquire) बिठा (seating him) के (having) पास (close beside) कुड़े (O girls) ।",
                    "कौन आया पहन लिबास कुड़े ।"
                ],
                "poetic_hindi": [
                    "हाथ में लाठी, काला कम्बल, आँखों में दिव्य उजाला,",
                    "साधारण चरवाहा नहीं यह, कोई अलौकिक मतवाला !",
                    "कौन आया पहन लिबास सखी ?"
                ],
                "poetic_english": [
                    "Staff in his hand, a blanket dark and plain, yet in his eyes celestial splendors shine;",
                    "No common herdsman over fields and grain, but an enraptured traveler divine:",
                    "Who hath arrived in this disguise, O friends?"
                ]
            },
            {
                "original": [
                    "चाकर चाक ना इस नूं आखो, इह ना खाली गुझ्झड़ी घातों,  ",
                    "विछड़्या होया पहली रातों, आया करन तलाश कुड़े ।  ",
                    "कौन आया पहन लिबास कुड़े ।"
                ],
                "hindi_gloss": [
                    "चाकर (नौकर) चाक (चरवाहा) ना (मत) इस (इसको) नूं (को) आखो (कहो), इह (यह) ना (नहीं) खाली (शून्य) गुझ्झड़ी (गूढ़/गुप्त) घातों (घात/रहस्य से),",
                    "विछड़्या (बिछुड़ा) होया (हुआ) पहली (सृष्टि की प्रथम) रातों (रात—रोज़-ए-अलस्त से), आया (आया है) करन (करने) तलाश (अपनी खोई प्रेमिका की खोज) कुड़े ।",
                    "कौन आया पहन लिबास कुड़े ।"
                ],
                "english_gloss": [
                    "चाकर (servant) चाक (herdsman) ना (do not) इस (him) नूं (unto) आखो (call), इह (he) ना (not) खाली (empty of) गुझ्झड़ी (hidden) घातों (secret designs/mysteries),",
                    "विछड़्या (parted) होया (being) पहली (from the primal) रातों (night of creation/Alast), आया (has come) करन (to make) तलाश (search) कुड़े (O maidens) ।",
                    "कौन आया पहन लिबास कुड़े ।"
                ],
                "poetic_hindi": [
                    "चाकर-चरवाहा मत कहो इसे, यह गुप्त रहस्य से भरा हुआ,",
                    "आदि-रात का बिछुड़ा प्रेमी, अपनी हीर को ढूँढ रहा !",
                    "कौन आया पहन लिबास सखी ?"
                ],
                "poetic_english": [
                    "Call him no hired serf nor shepherd boy, fraught with deep mysteries his silence stays;",
                    "Parted since primal dawn from sacred joy, seeking his beloved through earthly ways:",
                    "Who hath arrived in this disguise, O friends?"
                ]
            },
            {
                "original": [
                    "ना इह चाकर चाक कही दा, ना इस ज़र्रा शौक महीं दा,  ",
                    "ना मुशताक है दुद्ध दहीं दा, ना उस भुक्ख प्यास कुड़े ।  ",
                    "कौन आया पहन लिबास कुड़े ।"
                ],
                "hindi_gloss": [
                    "ना (न) इह (यह) चाकर (नौकर है) चाक (न चरवाहा) कही (किसी) दा (का), ना (न) इस (इसे) ज़र्रा (ज़रा भी) शौक (शौक/रुचि) महीं (भैंसें चराने) दा (का),",
                    "ना (न) मुशताक (इच्छुक) है (है) दुद्ध (दूध) दहीं (और दही) दा (का), ना (न) उस (उसे) भुक्ख (सांसारिक भूख) प्यास (या प्यास है) कुड़े ।",
                    "कौन आया पहन लिबास कुड़े ।"
                ],
                "english_gloss": [
                    "ना (neither) इह (he) चाकर (servant) चाक (herdsman) कही (of anyone) दा (is), ना (nor) इस (he) ज़र्रा (particle of) शौक (fondness for) महीं (buffaloes) दा (has),",
                    "ना (nor) मुशताक (desirous) है (is) दुद्ध (of milk) दहीं (and curd) दा (of), ना (nor) उस (unto him) भुक्ख (hunger) प्यास (thirst) कुड़े (O maidens) ।",
                    "कौन आया पहन लिबास कुड़े ।"
                ],
                "poetic_hindi": [
                    "न किसी का यह नौकर-चाकर, न भैंसें चराने की चाह इसे,",
                    "दूध-दही का लोभ नहीं कुछ, भूख-प्यास की न परवाह इसे !",
                    "कौन आया पहन लिबास सखी ?"
                ],
                "poetic_english": [
                    "No bondsman he to any earthly lord, caring no whit for herds of kine or sheep;",
                    "Craving no milk or curd from peasant board, free from the pangs of hunger or of sleep:",
                    "Who hath arrived in this disguise, O friends?"
                ]
            },
            {
                "original": [
                    "बुल्ल्हा शहु लुक बैठा ओहले, दस्से भेत ना मुक्ख से बोले,  ",
                    "बाबल वर खेड़्यां तों टोले, वर मांहढा महंडे पास कुड़े ।  ",
                    "कौन आया पहन लिबास कुड़े ।"
                ],
                "hindi_gloss": [
                    "बुल्ल्हा (बुल्ला कहता है) शहु (प्रभु-शाह) लुक (छिपकर) बैठा (बैठ गया है) ओहले (पर्दे की ओट में), दस्से (बताता) भेत (भेद) ना (नहीं) मुक्ख (मुख) से (से) बोले (बोलता है),",
                    "बाबल (पिता संसार) वर (वर/पति) खेड़्यां (खेड़ों/सांसारिक बंधनों) तों (में) टोले (ढूंढता फिरता है), वर (सच्चा वर/स्वामी) मांहढा (मेरा) महंडे (मेरे ही) पास (अंग-संग है) कुड़े ।",
                    "कौन आया पहन लिबास कुड़े ।"
                ],
                "english_gloss": [
                    "बुल्ल्हा (Bulleh says) शहु (Lord) लुक (hidden) बैठा (sits) ओहले (behind the veil), दस्से (reveals) भेत (secret) ना (not) मुक्ख (from mouth) से (with) बोले (speaks),",
                    "बाबल (father/the world) वर (bridegroom) खेड़्यां (among the Kheras/worldly suitors) तों (from) टोले (seeks), वर (the true Bridegroom) मांहढा (mine) महंडे (with me) पास (very near/beside) कुड़े (O maidens) ।",
                    "कौन आया पहन लिबास कुड़े ।"
                ],
                "poetic_hindi": [
                    "बुल्ल्हा शौह ओट में बैठा, मुख से कोई भेद न खोले,",
                    "बाबुल ढूँढे खेड़ों में वर, मेरा वर तो मेरे ही पास री !"
                ],
                "poetic_english": [
                    "Bulleh's Lord sits behind the veil concealed, uttering no secret word to human ear;",
                    "My father seeks among the worldly Kheras, while my true Groom abides beside me here:",
                    "Who hath arrived in this disguise, O friends?"
                ]
            }
        ],
        "philosophical_meaning": "यह काफी सूफी प्रतीकवाद का शिखर है। हीर (जीवात्मा) को उसके माता-पिता सांसारिक पति 'खेड़ों' (माया/सांसारिक धर्म) से बांधना चाहते हैं, किंतु उसका वास्तविक वर 'रांझा' (परमात्मा) है, जो 'चाक' (दीन-हीन चरवाहे) के वेश में आया है। परमात्मा ऐश्वर्य में नहीं, बल्कि दीनता और प्रेम के वेश में मिलता है। सच्चा प्रियतम बाहर कहीं नहीं, बल्कि अंतरात्मा के 'अंग-संग' उपस्थित है।"
    }
]

new_lexicon_terms = {
    "मुहार": {"hindi": "ऊंट की नकेल, बागडोर", "english": "reins, bridle/halter of camel or steed"},
    "ढोला": {"hindi": "प्रियतम प्यारे, साजन", "english": "sweet beloved, darling"},
    "अवल्ला": {"hindi": "अनुचित, कड़वा, अटपटा", "english": "awkward, untoward, harsh"},
    "कपूरी रेवड़ी": {"hindi": "कपूर-सुगंधित या सफेद उत्तम रेवड़ी", "english": "camphor-scented/refined sweet crisp revadi"},
    "पतासा": {"hindi": "बताशा, चीनी की हल्की फुल्की मिठाई", "english": "patasa, light puffed sugar sweet"},
    "लगड़": {"hindi": "शिकारी बाज़", "english": "falcon, hunting hawk"},
    "गोचें": {"hindi": "छोटी चिड़िया, गौंचा", "english": "small sparrow or lark"},
    "गुरग": {"hindi": "भेड़िया", "english": "wolf"},
    "सहे": {"hindi": "खरगोश", "english": "hares, rabbits"},
    "शीहणी": {"hindi": "शेरनी", "english": "lioness"},
    "खर दज्जाल": {"hindi": "दज्जाल का गधा; कयामत से पूर्व आने वाला अधर्म का वाहन", "english": "the ass of Dajjal (Anti-Christ); apocalyptic beast of chaos"},
    "चरख़ा": {"hindi": "चरखा; सूफी रूपक में: मानव देह", "english": "spinning wheel; allegorically: the human body"},
    "कत्तन": {"hindi": "सूत कातना, साधना करना", "english": "spinning yarn; practicing spiritual devotion"},
    "तक्कला": {"hindi": "चरखे की तकली/धुरी", "english": "spindle of the spinning wheel"},
    "बायड़": {"hindi": "चरखे की धुरी का सिरा", "english": "spindle-bearing / pivot of wheel"},
    "माल्ह": {"hindi": "चरखे के पहिए को तकली से जोड़ने वाली डोरी", "english": "driving-cord linking wheel and spindle"},
    "भड़ोली": {"hindi": "अन्न या सूत रखने का मिट्टी का मटका/कोठरी", "english": "large earthen storage jar or bin"},
    "दाज": {"hindi": "दहेज; रूपक में: परलोक हेतु पुण्य-कर्म", "english": "dowry; metaphorically: spiritual virtues for afterlife"},
    "त्रिंञन": {"hindi": "चरखा कातने वाली सखियों की गोष्ठी/बैठक", "english": "spinning bee / village gathering of maidens"},
    "छल्ली": {"hindi": "सूत की अटी, कती हुई सूत का पिंड", "english": "hank/spool of spun yarn"},
    "सालू": {"hindi": "विवाह की लाल चुनरी/चादर", "english": "red wedding shawl/veil"},
    "इख़लास": {"hindi": "सच्चा प्रेम, निष्कपट श्रद्धा, आदर", "english": "sincerity, pure devotion and love"},
    "खूंडी": {"hindi": "चरवाहे की लाठी, कूबड़ी", "english": "shepherd's crook/staff"},
    "चाक": {"hindi": "चरवाहा, सेवक (विशेषतः रांझा)", "english": "herdsman, servant (specifically Ranjha)"}
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
        "completed_count": 65,
        "total": 160,
        "next_kafi_id": 66,
        "last_updated": "2026-10-17T17:05:00+05:30",
        "last_batch": "61-65",
        "status": "in_progress"
    }
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    print(f"Checkpoint updated: 65/160 completed. Next ID: 66")

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
