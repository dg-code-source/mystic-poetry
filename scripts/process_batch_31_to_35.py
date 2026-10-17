import os
import json
import re
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
KAFIAN_DIR = os.path.join(DATA_DIR, "kafian")
CHECKPOINT_JSON = os.path.join(DATA_DIR, "checkpoint.json")
LEXICON_JSON = os.path.join(DATA_DIR, "punjabi_sufi_lexicon.json")

os.makedirs(KAFIAN_DIR, exist_ok=True)

batch = []

# ==========================================
# KAFI 31: 31. गल्ल रौले लोकां पाई ए
# ==========================================
k31_orig = """गल्ल रौले लोकां पाई ए ।
गल्ल रौले लोकां पाई ए ।

सच्च आख मना क्यों डरना एं, इस सच्च पिच्छे तूं तुरना एं,
सच्च सदा आबादी करना एं, सच्च वसत अचंभा आई ए ।
गल्ल रौले लोकां पाई ए ।

बाहमण आण जजमान डराए, पित्तर पीड़ दस्स भरम दुड़ाए,
आपे दस्स के जतन कराए, पूजा शुरू कराई ए ।
गल्ल रौले लोकां पाई ए ।

पुत्तर तुसां दे उपर पीड़ा, गुड़ चावल मनायो लीड़ा,
जंजू पायो लाहो बीड़ा, चुल्ली तुरत पवाई ए ।
गल्ल रौले लोकां पाई ए ।

पीड़ नहीं ऐवें निकलण लग्गी, रोक रुपईआ भांडे ढग्गी,
होवे लाखी दुरस्सत ना बग्गी, बुल्ल्हा इह बात बणाई ए ।
गल्ल रौले लोकां पाई ए ।

पिरथम चंडी मात बणाई, जिस नूं पूजे सरब लोकाई,
पाछी वढ्ढ के जंज चढ़ाई, डोली ठुम ठुम आई ए ।
गल्ल रौले लोकां पाई ए ।

भुल्ल ख़ुदा नूं जाण ख़ुदाई, बुत्तां अग्गे सीस निवाई,
जिहड़े घड़ के आप बणाई, शरम रता ना आई ए ।
गल्ल रौले लोकां पाई ए ।

वेखो तुलसी मात बणाई, सालगरामी संग परनाई,
हस्स हस्स डोली चा चढ़ाई, साला सहुरा बणे जवाई ए ।
गल्ल रौले लोकां पाई ए ।

धीआं भैणां सभ व्याहवण, परदे आपने आप कजावण,
बुल्ल्हा शाह की आखण आवण, ना मात किसे व्याही ए ।
गल्ल रौले लोकां पाई ए ।

शाह रग थीं रब्ब दिसदा नेड़े, लोकां पाए लंमे झेड़े,
वां के झगड़े कौण नबेड़े, भज्ज भज्ज उमर गवाई ए ।
गल्ल रौले लोकां पाई ए ।

बिरछ बाग़ विच नहीं जुदाई, बन्दा रब्ब तीवीं बण आई,
पिछले सोते ते खिड़ आई, दुबिधा आण मिटाई ए ।
गल्ल रौले लोकां पाई ए ।

बुल्ल्हा आपे भुल्ल भुलाइआ ए आपे चिल्लिआं विच दबाइआ ए,
आपे होका दे सुणाइआ ए मुझ में भेत ना काई ए ।
गल्ल रौले लोकां पाई ए ।

गरम सरद हो जिस नूं पाला, हरकत कीता चेहरा काला,
तिस नूं आखण जी सुखाला, इस दी करो दवाई ए ।
गल्ल रौले लोकां पाई ए ।

अक्खियां पक्कियां आखण आईआं, अलसी समझ के आउनी माईआ,
आपे भुल्ल गईआं हुण साईआं, हुण तीरथ पास सुधाई ए ।
गल्ल रौले लोकां पाई ए ।

पोसत आखे मिले अफीम, बन्दा भाले कादर करीम,
ना कोई दिस्से ज्ञान हकीम, अकल तुसाडी जाई ए ।
गल्ल रौले लोकां पाई ए ।

जो कोई दिसदा एहो प्यारा, बुल्ल्हा आपे वेखणहारा,
आपे बेद कुरान पुकारा, जो सुफने वसत भुलाई ए ।
गल्ल रौले लोकां पाई ए ।"""

k31_hi = """सीधी-सच्ची बात को लोगों ने व्यर्थ के झगड़ों और प्रपंचों में डाल रखा है!  
हे मन! सत्य का उद्घोष कर, भला तू सच कहने से क्यों डरता है?  
तुझे तो इसी सत्य के पावन मार्ग पर आजीवन चलना है!  
सत्य से ही अंतःकरण में अमर जीवन और आत्मिक विस्तार होता है,  
सत्य तो वह परम विस्मयकारी अमृत-निधि है जो घट में प्रकट हुई है!  

पुरोहित आकर यजमान को पूर्वजों के कोप और पितर-दोष से डराते हैं,  
मनगढ़ंत वहम पैदा करके स्वयं ही निवारण के उपाय बताते हैं,  
और धन-दौलत ऐंठने के लिए तरह-तरह की पूजा शुरू करवा देते हैं!  
कहते हैं: तुम्हारे पुत्र पर ग्रहों की भारी विपत्ति छाई है,  
गुड़, चावल और वस्त्र चढ़ाओ, जनेऊ धारण करो, संकल्प छोड़ो और आचमन करो!  
यह विपत्ति ऐसे ही दूर नहीं होगी—रोकड़ रुपये, तांबे-पीतल के बर्तन और गाय दो,  
चाहे गाय लाल हो या सफ़ेद, पुरोहितों ने यह ठगी का जाल फैला रखा है!  

पहले अपने हाथों से मिट्टी की चंडी माता गढ़ी, जिसे सारी दुनिया पूजने लगी,  
टोकरियों को काटकर बारात निकाली और माता की डोली सजाकर ठुमकते हुए ले आए!  
उस सच्चे सृजनहार ख़ुदा को भूलकर, हाथों की गढ़ी हुई बेजान मूर्तियों के आगे  
यह अज्ञानी दुनिया शीश झुकाती है और इन्हें ज़रा भी लज्जा नहीं आती!  
तुलसी के पौधे को माता मानकर शालिग्राम के पत्थर से उसका विवाह रचाया,  
हँस-हँसकर डोली उठाई और साला, ससुर, दामाद के रिश्ते गढ़ लिए!  
बेटियों और बहनों का विवाह तो अपनी कुल-मर्यादा के लिए किया जाता है,  
पर बुल्ले शाह पूछते हैं कि कभी किसी ने अपनी माता का भी विवाह कराया है?  

परमात्मा तो मनुष्य की शह-रग (गर्दन की नस) से भी अधिक निकट विद्यमान है,  
किंतु अज्ञानियों ने लंबे-चौड़े आडंबर और झगड़े खड़े कर रखे हैं!  
हवा जैसे इन खोखले झगड़ों को कौन सुलझाए? लोगों ने भटक-भटक कर जीवन गँवा दिया!  
जैसे बाग़ और उसके वृक्षों में कोई भेद नहीं होता,  
वैसे ही यह जीव भी प्रभु-प्रेम में समर्पित होकर परमात्मा का ही रूप बन जाता है!  
जब पिछली रात की बेला में आत्म-चेतना जागृत हुई, सारा द्वैत मिट गया!  
वह प्रभु स्वयं ही माया की भूल में भुलाता है, स्वयं ही कठिन चिल्लों में तपाता है,  
और फिर स्वयं ही भीतर से उद्घोष करता है: मुझमें और तुझमें कोई भेद नहीं है!  

जब विरह में जीव का चेहरा फक़ हो जाता है और देह जाड़े से कांपने लगती है,  
तो दुनिया के नादान कहते हैं: अरे, कोई शारीरिक रोग है, इसका इलाज करो!  
आँसू बहाते-बहाते आँखें पक जाती हैं, तो माताएँ अलसी की पुल्टिस बांधने दौड़ती हैं,  
सहेलियाँ भ्रम में पड़कर विरहिणी को तीर्थों और वैद्यों के पास दौड़ाती फिरती हैं!  
जैसे नशेड़ी अफीम का मोहताज होता है, वैसे ही यह दुनिया परमात्मा को बाहर ढूँढती है,  
जब तक कोई आत्मज्ञानी हकीम न मिले, तुम्हारी यह सांसारिक अक्ल व्यर्थ ही भटकेगी!  
संसार में जो कोई भी रूप दिखाई देता है, वह उसी प्यारे परमात्मा का रूप है,  
बुल्ला तो स्वयं उसी का साक्षी है, उसी ने वेद और क़ुरआन का ज्ञान दिया है,  
ताकि स्वप्नवत संसार में भूली हुई आत्मा अपने शाश्वत स्वरूप को पहचान सके!"""

k31_en = """The plain, radiant Truth has been drowned in the clamor of worldly disputes!  
Speak the Truth, O my soul! Why dost thou tremble in fear?  
It is upon this sacred path alone that thou art destined to tread!  
Truth kindles an eternal kingdom of flourishing light within,  
Truth is that wondrous jewel unveiled in the sanctuary of the heart!  

The priest approaches to terrify his patron with tales of ancestral wrath,  
Spreading webs of superstition only to prescribe costly remedies of his own,  
Initiating endless rituals to fill his coffers with gold!  
He cries: "A dire omen hovers over thy son's head!  
Bring offerings of rice and jaggery, bestow garments, don the sacred thread,  
Take the ritual vows and drink the purifying water swiftly!  
This torment will not depart so easily—offer cash, vessels, and a dairy cow,  
Be it spotted, red, or white!"—O Bulleh, such are the illusions they weave!  

First they fashion Mother Chandi from clay, bidding all humanity to bow,  
Cutting woven reeds to build a procession, parading her palanquin through the street!  
Forgetting the living Lord of the cosmos, they prostrate before inanimate stone  
Sculpted by their own mortal hands, without feeling the slightest shame!  
Behold, they crown the holy basil as Mother, wedding her to the Shaligram stone,  
Laughing as they raise the bridal palanquin, creating ties of father-in-law and bridegroom!  
Men arrange marriages for daughters and sisters to preserve household dignity,  
Yet Bulleh Shah asks in wonder: when did a mortal ever marry away his own mother?  

God is nearer unto thee than thine own jugular vein,  
Yet blind men have tangled themselves in interminable squabbles!  
Who can unravel these disputes built on empty wind? They waste their days running in vain!  
Just as there is no division between the blossoming tree and the soil of the garden,  
So the devotee, surrendering as a bride of Love, dissolves into the Beloved Divine!  
When the soul awakens in the quiet watch of the dawn, all duality dissolves away!  
The Lord Himself leads the mind through the maze, He plunges the seeker into rigorous penance,  
And then He Himself cries from within: "Between Me and thee there is no secret or divide!"  

When the chills of spiritual longing make the seeker shudder and the countenance turns pale,  
Worldly observers dismiss it lightly: "It is an ordinary ailment, administer some medicine!"  
When eyes swell and burn from weeping tears of divine love, mothers rush with poultices of flaxseed,  
Companions become bewildered, dragging the lover to shrines and worldly doctors!  
Just as the addict yearns blindly for his opium, so humanity seeks the Almighty in outer temples,  
Yet without an enlightened master of the soul, all thy worldly intellect is utterly lost!  
Whatever form appears in this living creation is none other than the Beloved,  
Bulleh is himself the eternal witness; the Lord proclaimed the Vedas and the Holy Quran,  
To awaken the slumbering soul that had forgotten its divine identity in this fleeting dream!"""

batch.append({
    "id": 31,
    "title": "31. गल्ल रौले लोकां पाई ए",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k31_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "गल्ल रौले लोकां पाई ए ।",
                "hindi_gloss": "गल्ल (सत्य की सीधी बात को) रौले (शोर-शराबे और झगड़े में) लोकां (संसार के लोगों ने) पाई (डाल दिया) ए (है) ।",
                "english_gloss": "gall (the matter of Truth) raule (in noisy dispute/confusion) lokaan (the people) paaee (have cast) e (has) ."
            },
            {
                "original": "गल्ल रौले लोकां पाई ए ।",
                "hindi_gloss": "गल्ल (सीधी बात को) रौले (विवादों के जाल में) लोकां (दुनिया वालों ने) पाई (उलझा दिया) ए (है) ।",
                "english_gloss": "gall (the simple truth) raule (in conflict and noise) lokaan (mortals) paaee (have entangled) e (has) ."
            },
            {
                "original": "सच्च आख मना क्यों डरना एं, इस सच्च पिच्छे तूं तुरना एं,",
                "hindi_gloss": "सच्च (सत्य) आख (कहो) मना (हे मेरे मन) क्यों (क्यों) डरना (डरते) एं (हो), इस (इस) सच्च (सत्य के) पिच्छे (मार्ग पर) तूं (तुझे) तुरना (चलना) एं (है),",
                "english_gloss": "sachh (truth) aakh (speak) mana (O mind) kyon (why) darna (fear) ain (dost thou), is (this) sachh (truth) pichhe (upon path of) toon (thou) turna (must walk) ain (art to),"
            },
            {
                "original": "सच्च सदा आबादी करना एं, सच्च वसत अचंभा आई ए ।",
                "hindi_gloss": "सच्च (सत्य तो) सदा (सदा) आबादी (जीवन और आनंद का विस्तार) करना (करता) एं (है), सच्च (यह सत्य की) वसत (वस्तु/रहस्य) अचंभा (परम विस्मयकारी) आई (प्रकट हुई) ए (है) ।",
                "english_gloss": "sachh (truth) sada (ever) aabaadee (prosperity/spiritual life) karna (creates) ain (does), sachh (truth) vasat (treasure/essence) achambha (wondrous) aayee (has arrived) e (has) ."
            },
            {
                "original": "गल्ल रौले लोकां पाई ए ।",
                "hindi_gloss": "गल्ल (सत्य की बात को) रौले (झगड़े में) लोकां (लोगों ने) पाई (डाल दिया) ए (है) ।",
                "english_gloss": "gall (truth) raule (in dispute) lokaan (people) paaee (have cast) e (has) ."
            },
            {
                "original": "बाहमण आण जजमान डराए, पित्तर पीड़ दस्स भरम दुड़ाए,",
                "hindi_gloss": "बाहमण (पुरोहित/ब्राह्मण) आण (आकर) जजमान (यजमान को) डराए (डराता है), पित्तर (पितरों की) पीड़ (पीड़ा और कोप) दस्स (बताकर) भरम (तरह-तरह के भ्रम) दुड़ाए (दौड़ाता है),",
                "english_gloss": "baahaman (the priest) aan (coming) jajmaan (patron) daraae (frightens), pittar (ancestors') peed (affliction/wrath) dass (describing) bharam (superstitions) dudaae (incites),"
            },
            {
                "original": "आपे दस्स के जतन कराए, पूजा शुरू कराई ए ।",
                "hindi_gloss": "आपे (स्वयं ही उपाय) दस्स के (बताकर) जतन (पूजा के अनुष्ठान) कराए (कराता है), पूजा (और धन कमाने की पूजा) शुरू (शुरू) कराई (करवाता) ए (है) ।",
                "english_gloss": "aape (himself) dass ke (prescribing) jatan (rituals) karaae (causes to do), pooja (worship) shuroo (started) karaaee (has initiated) e (has) ."
            },
            {
                "original": "गल्ल रौले लोकां पाई ए ।",
                "hindi_gloss": "गल्ल (सीधी बात को) रौले (झगड़े में) लोकां (लोगों ने) पाई (डाल दिया) ए (है) ।",
                "english_gloss": "gall (the truth) raule (in confusion) lokaan (people) paaee (have thrown) e (has) ."
            },
            {
                "original": "पुत्तर तुसां दे उपर पीड़ा, गुड़ चावल मनायो लीड़ा,",
                "hindi_gloss": "पुत्तर (तुम्हारे पुत्र) तुसां दे (के) उपर (ऊपर भारी) पीड़ा (ग्रहों की पीड़ा/दोष है), गुड़ (गुड़) चावल (चावल) मनायो (चढ़ाओ और) लीड़ा (वस्त्र दान करो),",
                "english_gloss": "puttar (son) tusaan de (of yours) upar (upon) peeda (affliction/curse), gud (jaggery) chaaval (rice) manaayo (offer) leeda (clothing),"
            },
            {
                "original": "जंजू पायो लाहो बीड़ा, चुल्ली तुरत पवाई ए ।",
                "hindi_gloss": "जंजू (यज्ञोपवीत/जनेऊ) पायो (पहनाओ) लाहो (उतारो) बीड़ा (बीड़ा/संकल्प), चुल्ली (मंत्रोच्चार के साथ आचमन) तुरत (तुरंत) पवाई (करवाता) ए (है) ।",
                "english_gloss": "janju (sacred thread) paayo (put on) laaho (relieve) beeda (pledge/token), chullee (ritual sip/purification) turat (swiftly) pavaaee (administers) e (has) ."
            },
            {
                "original": "गल्ल रौले लोकां पाई ए ।",
                "hindi_gloss": "गल्ल (सीधी बात को) रौले (प्रपंच में) लोकां (लोगों ने) पाई (डाल दिया) ए (है) ।",
                "english_gloss": "gall (the matter) raule (in dispute) lokaan (people) paaee (have cast) e (has) ."
            },
            {
                "original": "पीड़ नहीं ऐवें निकलण लग्गी, रोक रुपईआ भांडे ढग्गी,",
                "hindi_gloss": "पीड़ (वह कहता है कि यह बाधा) नहीं (नहीं) ऐवें (यूँ ही) निकलण (निकलने/दूर होने) लग्गी (लगेगी), रोक (रोकड़) रुपईआ (रुपये) भांडे (बर्तन) ढग्गी (और गाय/बछड़ा दो),",
                "english_gloss": "peed (affliction) naaheen (not) aiven (just like that) niklan (to depart) laggee (is about to), rok (cash) rupayeea (silver coins) bhaande (utensils) dhaggee (cattle/ox),"
            },
            {
                "original": "होवे लाखी दुरस्सत ना बग्गी, बुल्ल्हा इह बात बणाई ए ।",
                "hindi_gloss": "होवे (चाहे वह गाय) लाखी (लाल रंग की हो) दुरस्सत (या हष्ट-पुष्ट) ना (या) बग्गी (सफ़ेद हो), बुल्ल्हा (हे बुल्ले) इह (यह सारी पाखंड की) बात (कहानी) बणाई (गढ़ी गई) ए (है) ।",
                "english_gloss": "hove (be it) laakhee (reddish-brown) durassat (sturdy) na (or) baggee (white), bullha (O Bulleh) eh (this fabricated) baat (story) banaaee (has been invented) e (has) ."
            },
            {
                "original": "गल्ल रौले लोकां पाई ए ।",
                "hindi_gloss": "गल्ल (सीधी बात को) रौले (झगड़े में) लोकां (लोगों ने) पाई (डाल दिया) ए (है) ।",
                "english_gloss": "gall (the truth) raule (in dispute) lokaan (people) paaee (have cast) e (has) ."
            },
            {
                "original": "पिरथम चंडी मात बणाई, जिस नूं पूजे सरब लोकाई,",
                "hindi_gloss": "पिरथम (पहले तो मिट्टी की) चंडी (चंडी) मात (माता की मूर्ति) बणाई (बनाई), जिस (जिसको) नूं (को) पूजे (पूजती है) सरब (समस्त) लोकाई (संसार की जनता),",
                "english_gloss": "piratham (first) chandee (Chandi/goddess) maat (Mother) banaaee (fashioned), jis (whom) noon (unto) pooje (worships) sarab (all) lokaaee (humanity),"
            },
            {
                "original": "पाछी वढ्ढ के जंज चढ़ाई, डोली ठुम ठुम आई ए ।",
                "hindi_gloss": "पाछी (टोकरी) वढ्ढ के (काटकर) जंज (बारात) चढ़ाई (चढ़ाई जाती है), डोली (और माता की डोली) ठुम (ठुमक) ठुम (ठुमक कर) आई (लाई जाती) ए (है) ।",
                "english_gloss": "paachhee (basket) vaddh ke (cutting) janj (procession/entourage) chadhaaee (is mounted), dolee (palanquin) thum (slowly) thum (stepping) aayee (has arrived) e (has) ."
            },
            {
                "original": "गल्ल रौले लोकां पाई ए ।",
                "hindi_gloss": "गल्ल (सीधी बात को) रौले (विवाद में) लोकां (लोगों ने) पाई (डाल दिया) ए (है) ।",
                "english_gloss": "gall (the truth) raule (in dispute) lokaan (people) paaee (have cast) e (has) ."
            },
            {
                "original": "भुल्ल ख़ुदा नूं जाण ख़ुदाई, बुत्तां अग्गे सीस निवाई,",
                "hindi_gloss": "भुल्ल (भूलकर) ख़ुदा (परमात्मा) नूं (को) जाण (जानबूझकर यह) ख़ुदाई (संसार), बुत्तां (पत्थर की मूर्तियों) अग्गे (के आगे) सीस (अपना शीश) निवाई (झुकाती है),",
                "english_gloss": "bhull (forgetting) khuda (God) noon (unto) jaan (knowingly this) khudaaee (creation), buttaan (statues/idols) agge (before) sees (head) nivaaee (bows),"
            },
            {
                "original": "जिहड़े घड़ के आप बणाई, शरम रता ना आई ए ।",
                "hindi_gloss": "जिहड़े (जिन्हें) घड़ के (अपने हाथों से गढ़कर) आप (स्वयं) बणाई (बनाया है), शरम (लज्जा) रता (ज़रा भी) ना (नहीं) आई (आती) ए (है) ।",
                "english_gloss": "jihde (which) ghad ke (carving) aap (themselves) banaaee (created), sharam (shame) rata (the least) na (not) aayee (felt) e (has) ."
            },
            {
                "original": "गल्ल रौले लोकां पाई ए ।",
                "hindi_gloss": "गल्ल (सीधी बात को) रौले (विवाद में) लोकां (लोगों ने) पाई (डाल दिया) ए (है) ।",
                "english_gloss": "gall (truth) raule (in dispute) lokaan (people) paaee (have cast) e (has) ."
            },
            {
                "original": "वेखो तुलसी मात बणाई, सालगरामी संग परनाई,",
                "hindi_gloss": "वेखो (देखो) तुलसी (तुलसी के पौधे को) मात (माता) बणाई (बनाया), सालगरामी (और शालिग्राम पत्थर के) संग (साथ) परनाई (उसका विवाह रचाया),",
                "english_gloss": "vekho (look) tulsee (basil plant) maat (Mother) banaaee (made), saalagraamee (Shaligram stone) sang (with) parnaaee (wedded),"
            },
            {
                "original": "हस्स हस्स डोली चा चढ़ाई, साला सहुरा बणे जवाई ए ।",
                "hindi_gloss": "हस्स (हँस) हस्स (हँसकर) डोली (डोली) चा (उठाकर) चढ़ाई (चढ़ाई), साला (साला) सहुरा (ससुर) बणे (और) जवाई (दामाद का नाता बना लिया) ए (है) ।",
                "english_gloss": "hass (laughing) hass (joyfully) dolee (palanquin) cha (lifting) chadhaaee (conducted), saala (brother-in-law) sahura (father-in-law) bane (became) javaaee (son-in-law) e (has) ."
            },
            {
                "original": "गल्ल रौले लोकां पाई ए ।",
                "hindi_gloss": "गल्ल (सीधी बात को) रौले (प्रपंच में) लोकां (लोगों ने) पाई (डाल दिया) ए (है) ।",
                "english_gloss": "gall (truth) raule (in dispute) lokaan (people) paaee (have cast) e (has) ."
            },
            {
                "original": "धीआं भैणां सभ व्याहवण, परदे आपने आप कजावण,",
                "hindi_gloss": "धीआं (अपनी बेटियों) भैणां (और बहनों का) सभ (सब) व्याहवण (विवाह करते हैं), परदे (और अपनी लाज के पर्दे) आपने (स्वयं) आप (ही) कजावण (ढाँकते हैं),",
                "english_gloss": "dheeyaan (daughters) bhainaan (sisters) sabh (all) vyaahavan (they marry off), parde (veils of honor) aapne (their own) aap (themselves) kajaavan (cover),"
            },
            {
                "original": "बुल्ल्हा शाह की आखण आवण, ना मात किसे व्याही ए ।",
                "hindi_gloss": "बुल्ल्हा (बुल्ले) शाह (शाह कहते हैं कि) की (क्या) आखण (कहने) आवण (जाएँ), ना (कभी भी) मात (माता का विवाह) किसे (किसी ने) व्याही (रचाया है) ए (भला) ।",
                "english_gloss": "bullha (Bulleh) shaah (Shah) kee (what) aakhan (to say) aavan (can come), na (never) maat (Mother) kise (by anyone) vyaahee (has been wedded) e (has) ."
            },
            {
                "original": "गल्ल रौले लोकां पाई ए ।",
                "hindi_gloss": "गल्ल (सीधी बात को) रौले (विवाद में) लोकां (लोगों ने) पाई (डाल दिया) ए (है) ।",
                "english_gloss": "gall (truth) raule (in dispute) lokaan (people) paaee (have cast) e (has) ."
            },
            {
                "original": "शाह रग थीं रब्ब दिसदा नेड़े, लोकां पाए लंमे झेड़े,",
                "hindi_gloss": "शाह रग (शह-रग/जीवन-नस) थीं (से भी अधिक) रब्ब (परमात्मा) दिसदा (दिखता है) नेड़े (समीप), लोकां (किंतु लोगों ने) पाए (खड़े कर रखे हैं) लंमे (लंबे-लंबे व्यर्थ) झेड़े (विवाद और झगड़े),",
                "english_gloss": "shaah rag (jugular vein) theen (than) rabb (God) disda (appears) nede (closer), lokaan (people) paae (have created) lamme (long) jhede (disputes),"
            },
            {
                "original": "वां के झगड़े कौण नबेड़े, भज्ज भज्ज उमर गवाई ए ।",
                "hindi_gloss": "वां के (हवा जैसे निरर्थक) झगड़े (झगड़ों को) कौण (भला कौन) नबेड़े (सुलझाए), भज्ज (दौड़) भज्ज (दौड़कर व्यर्थ) उमर (पूरी उम्र) गवाई (गँवा दी) ए (है) ।",
                "english_gloss": "vaan ke (airy/empty) jhagde (squabbles) kaun (who) nabede (can resolve), bhajj (running) bhajj (racing) umar (lifetime) gavaaee (wasted) e (has) ."
            },
            {
                "original": "गल्ल रौले लोकां पाई ए ।",
                "hindi_gloss": "गल्ल (सत्य की बात को) रौले (विवाद में) लोकां (लोगों ने) पाई (डाल दिया) ए (है) ।",
                "english_gloss": "gall (truth) raule (in dispute) lokaan (people) paaee (have cast) e (has) ."
            },
            {
                "original": "बिरछ बाग़ विच नहीं जुदाई, बन्दा रब्ब तीवीं बण आई,",
                "hindi_gloss": "बिरछ (वृक्ष और) बाग़ (बाग़) विच (में जैसे) नहीं (कोई) जुदाई (भेद नहीं होता), बन्दा (वैसे ही मनुष्य) रब्ब (और परमात्मा के बीच प्रेम की सुहागिन) तीवीं (स्त्री बनकर) बण आई (एकाकार हो गई),",
                "english_gloss": "birachh (tree) baag (garden) vich (in) naaheen (no) judaaee (separation), banda (man) rabb (God) teeveen (as bride) ban aayee (united),"
            },
            {
                "original": "पिछले सोते ते खिड़ आई, दुबिधा आण मिटाई ए ।",
                "hindi_gloss": "पिछले (अंतिम प्रहर में जब यह चेतना) सोते (सोती हुई दुनिया से जागकर) ते (पर) खिड़ आई (खिल उठी), दुबिधा (तो सारा द्वैत और संशय) आण (आकर) मिटाई (नष्ट हो गया) ए (है) ।",
                "english_gloss": "pichhle (in the final watch) sote (from slumber) te (upon) khid aayee (blossomed), dubidha (duality) aan (arriving) mitaaee (effaced) e (has) ."
            },
            {
                "original": "गल्ल रौले लोकां पाई ए ।",
                "hindi_gloss": "गल्ल (सीधी बात को) रौले (विवाद में) लोकां (लोगों ने) पाई (डाल दिया) ए (है) ।",
                "english_gloss": "gall (truth) raule (in dispute) lokaan (people) paaee (have cast) e (has) ."
            },
            {
                "original": "बुल्ल्हा आपे भुल्ल भुलाइआ ए आपे चिल्लिआं विच दबाइआ ए,",
                "hindi_gloss": "बुल्ल्हा (हे बुल्ले! वह परमात्मा) आपे (स्वयं ही) भुल्ल (भूल में) भुलाइआ (भटकाता) ए (है), आपे (स्वयं ही कठिन) चिल्लिआं (चालीस दिन के तप-साधना) विच (में) दबाइआ (तपाता) ए (है),",
                "english_gloss": "bullha (O Bulleh) aape (Himself) bhull (in delusion) bhulaaia (causes to forget) e (has), aape (Himself) chilleeyaan (forty-day ascetic fasts) vich (within) dabaaia (presses) e (has),"
            },
            {
                "original": "आपे होका दे सुणाइआ ए मुझ में भेत ना काई ए ।",
                "hindi_gloss": "आपे (और स्वयं ही) होका (मुक्ति का उद्घोष) दे (देकर) सुणाइआ (सुनाता) ए (है कि) मुझ (मुझमें और तुझमें) में (में) भेत (कोई भेद) ना (नहीं) काई (रत्ती भर भी) ए (है) ।",
                "english_gloss": "aape (Himself) hoka (proclamation) de (giving) sunaaia (announces) e (has), mujh (in Me) mein (in) bhet (difference/secret) na (not) kaaee (any) e (is) ."
            },
            {
                "original": "गल्ल रौले लोकां पाई ए ।",
                "hindi_gloss": "गल्ल (सत्य की बात को) रौले (विवाद में) लोकां (लोगों ने) पाई (डाल दिया) ए (है) ।",
                "english_gloss": "gall (truth) raule (in dispute) lokaan (people) paaee (have cast) e (has) ."
            },
            {
                "original": "गरम सरद हो जिस नूं पाला, हरकत कीता चेहरा काला,",
                "hindi_gloss": "गरम (कभी गर्म) सरद (कभी सर्द) हो (होकर) जिस (जिसको विरह का) नूं (को) पाला (जाड़ा लग जाता है), हरकत (अंदर की तड़प से) कीता (हो जाता है) चेहरा (चेहरा) काला (फ़क़ और कांतिहीन),",
                "english_gloss": "garam (hot) sarad (cold) ho (becoming) jis (who) noon (unto) paala (chills of yearning), harkat (inner agitation) keeta (made) chehra (face) kaala (dark/pale),"
            },
            {
                "original": "तिस नूं आखण जी सुखाला, इस दी करो दवाई ए ।",
                "hindi_gloss": "तिस (उसको) नूं (को दुनिया के अज्ञानी) आखण (कहते हैं कि) जी (अरे) सुखाला (सरल है), इस (इस बेचारे) दी (की) करो (करो) दवाई (कोई शारीरिक दवा) ए (है) ।",
                "english_gloss": "tis (unto that one) noon (to) aakhan (they say) jee (well) sukhaala (easy), is (this one's) dee (of) karo (administer) davaaee (medicine) e (has) ."
            },
            {
                "original": "गल्ल रौले लोकां पाई ए ।",
                "hindi_gloss": "गल्ल (सीधी बात को) रौले (विवाद में) लोकां (लोगों ने) पाई (डाल दिया) ए (है) ।",
                "english_gloss": "gall (truth) raule (in dispute) lokaan (people) paaee (have cast) e (has) ."
            },
            {
                "original": "अक्खियां पक्कियां आखण आईआं, अलसी समझ के आउनी माईआ,",
                "hindi_gloss": "अक्खियां (रो-रोकर आँखें) पक्कियां (लाल और पक गई हैं) आखण (और सब कहने) आईआं (आई हैं), अलसी (अलसी की पुल्टिस) समझ के (समझकर) आउनी (दौड़ती आती हैं) माईआ (माताएँ),",
                "english_gloss": "akkheeyaan (eyes) pakkeeyaan (swollen from tears) aakhan (to speak) aaeeyaan (have come), alsee (flaxseed poultice) samajh ke (thinking) aaunee (rush) maayeeyaa (mothers),"
            },
            {
                "original": "आपे भुल्ल गईआं हुण साईआं, हुण तीरथ पास सुधाई ए ।",
                "hindi_gloss": "आपे (स्वयं ही) भुल्ल (भ्रम में) गईआं (पड़ गई हैं) हुण (अब) साईआं (सहेलियाँ), हुण (अब वे रोगी को लेकर) तीरथ (तीर्थों के) पास (पास) सुधाई (दौड़ाती फिरती) ए (हैं) ।",
                "english_gloss": "aape (themselves) bhull (deluded) gayeeyaan (became) hun (now) saayeeyaan (companions), hun (now) teerath (to shrines) paas (near) sudhaaee (rush them) e (are) ."
            },
            {
                "original": "गल्ल रौले लोकां पाई ए ।",
                "hindi_gloss": "गल्ल (सीधी बात को) रौले (विवाद में) लोकां (लोगों ने) पाई (डाल दिया) ए (है) ।",
                "english_gloss": "gall (truth) raule (in dispute) lokaan (people) paaee (have cast) e (has) ."
            },
            {
                "original": "पोसत आखे मिले अफीम, बन्दा भाले कादर करीम,",
                "hindi_gloss": "पोसत (अफीम का डोडा) आखे (चाहता है कि) मिले (मुझे प्राप्त हो) अफीम (अफीम का नशा), बन्दा (और अज्ञानी मनुष्य बाहर) भाले (खोजता फिरता है) कादर (उस सर्वशक्तिमान) करीम (कृपालु प्रभु को),",
                "english_gloss": "posat (poppy pod) aakhe (craves) mile (to obtain) afeem (pure opium), banda (man) bhaale (searches for) kaadar (the Almighty) kareem (Bountiful Lord),"
            },
            {
                "original": "ना कोई दिस्से ज्ञान हकीम, अकल तुसाडी जाई ए ।",
                "hindi_gloss": "ना (नहीं) कोई (कोई) दिस्से (दिखाई देता) ज्ञान (सच्चे आत्मज्ञान का) हकीम (वैद्य), अकल (हे लोगो! बुद्धि) तुसाडी (तुम्हारी) जाई (कहाँ नष्ट हो गई) ए (है) ।",
                "english_gloss": "na (not) koee (any) disse (appears) gyaan (spiritual wisdom) hakeem (physician), akal (wisdom) tusaadee (of yours) jaaee (lost) e (is) ."
            },
            {
                "original": "गल्ल रौले लोकां पाई ए ।",
                "hindi_gloss": "गल्ल (सीधी बात को) रौले (विवाद में) लोकां (लोगों ने) पाई (डाल दिया) ए (है) ।",
                "english_gloss": "gall (truth) raule (in dispute) lokaan (people) paaee (have cast) e (has) ."
            },
            {
                "original": "जो कोई दिसदा एहो प्यारा, बुल्ल्हा आपे वेखणहारा,",
                "hindi_gloss": "जो (जो) कोई (कोई भी रूप) दिसदा (दिखाई पड़ता है) एहो (वही मेरा) प्यारा (प्रियतम प्रभु है), बुल्ल्हा (हे बुल्ले! वह) आपे (स्वयं ही) वेखणहारा (देखने वाला साक्षी है),",
                "english_gloss": "jo (whatever) koee (form) disda (appears) eho (this very) pyaara (Beloved), bullha (O Bulleh) aape (Himself) vekhanhaara (the true Seer/Witness),"
            },
            {
                "original": "आपे बेद कुरान पुकारा, जो सुफने वसत भुलाई ए ।",
                "hindi_gloss": "आपे (स्वयं ही उसने) बेद (वेद और) कुरान (क़ुरआन का ज्ञान) पुकारा (प्रकट किया), जो (जिसने) सुफने (इस स्वप्नवत संसार में अपनी मूल) वसत (सच्ची आत्मा को) भुलाई (भुला रखा था) ए (है) ।",
                "english_gloss": "aape (Himself) bed (Vedas) kuraan (Quran) pukaara (proclaimed), jo (who) suphane (in dream-state) vasat (true essence) bhulaaee (forgot) e (has) ."
            },
            {
                "original": "गल्ल रौले लोकां पाई ए ।",
                "hindi_gloss": "गल्ल (सीधी बात को) रौले (विवाद में) लोकां (लोगों ने) पाई (डाल दिया) ए (है) ।",
                "english_gloss": "gall (truth) raule (in dispute) lokaan (people) paaee (have cast) e (has) ."
            }
        ],
        "hindi_meaning": k31_hi,
        "english_meaning": k31_en
    }]
})

# ==========================================
# KAFI 32: 32. घड़िआली दियो निकाल नी
# ==========================================
k32_orig = """घड़िआली दियो निकाल नी ।
अज्ज पी घर आया लाल नी ।

घड़ी घड़ी घड़िआल बजावे, रैण वसल दी पिआ घटावे,
मेरे मन दी बात जो पावे, हत्थों चा सुट्टो घड़िआल नी ।
अज्ज पी घर आया लाल नी ।

अनहद वाजा वज्जे सुहाणा, मुतरिब सुघड़ा तान तराना,
निमाज़ रोज़ा भुल्ल ग्या दुगाणा, मध प्याला देण कलाल नी ।
अज्ज पी घर आया लाल नी ।

मुख वेखण दा अजब नज़ारा, दुक्ख दिले दा उट्ठ ग्या सारा,
रैण वड्डी क्या करे पसारा, दिल अग्गे पारो दीवाल नी ।
अज्ज पी घर आया लाल नी ।

मैनूं आपनी ख़बर ना काई, क्या जाणां मैं कित व्याही,
इह गल्ल क्यों कर छुपे छपाई, हुण होया फ़ज़ल कमाल नी ।
अज्ज पी घर आया लाल नी ।

टूणे टामण करे बथेरे, मिहरे आए वड्डे वडेरे,
हुण घर आया जानी मेरे, रहां लक्ख वर्हे इहदे नाल नी ।
अज्ज पी घर आया लाल नी ।

बुल्हा शहु दी सेज़ प्यारी, नी मैं तारनहारे तारी,
किवें किवें हुण आई वारी, हुण विछड़न होया मुहाल नी ।
अज्ज पी घर आया लाल नी ।"""

k32_hi = """अरी सखी! उस घड़ियाल बजाने वाले पहरेदार को बाहर निकाल दो!  
आज मेरे घर में मेरे प्यारे लाल (प्राण-प्रीतम) पधारे हैं!  

वह पहरेदार घड़ी-घड़ी घड़ियाल पीटकर, मिलन की इस रात को घटाए जा रहा है!  
जो कोई मेरे दिल की तड़प को समझता हो, जाकर उसके हाथ से घड़ियाल छीनकर फेंक दो!  
अरी सखी! आज मेरे घर में मेरे प्यारे लाल पधारे हैं!  

भीतर अनाहत नाद की मधुर वीणा बज रही है, दिव्य गायक सुरीली तान और तराना छेड़ रहा है!  
दो रकअत नमाज़ और रोज़े के नियम सब विस्मृत हो गए हैं, जब साक़ी ने प्रेम का प्याला भर दिया है!  
अरी सखी! आज मेरे घर में मेरे प्यारे लाल पधारे हैं!  

उनके मुखारविंद का दर्शन क्या हुआ, दिल के सारे दुःख पल भर में विलीन हो गए!  
यह रात अनंत हो जाए, दुनिया चाहे कुछ भी प्रपंच करे, मेरे हृदय के आगे रक्षा-दीवार खड़ी कर दो!  
अरी सखी! आज मेरे घर में मेरे प्यारे लाल पधारे हैं!  

मुझे अपनी देह और सुध-बुध की कोई सुध नहीं रही, मैं क्या जानूँ किस लोक में मेरा ब्याह हो गया!  
यह अलौकिक प्रेम भला छिपाए कैसे छिप सकता है? अब तो मुझ पर पूर्ण ईश्वरीय कृपा बरस पड़ी है!  
अरी सखी! आज मेरे घर में मेरे प्यारे लाल पधारे हैं!  

दुनिया ने बड़े-बड़े टोने-टोटके किए, कुटुंब के बड़े-बुजुर्ग समझाने चले आए,  
पर अब जब मेरे प्राण-प्यारे साजन घर आ गए हैं, मैं तो लाखों वर्ष इन्हीं के संग रहूँगी!  
अरी सखी! आज मेरे घर में मेरे प्यारे लाल पधारे हैं!  

बुल्ले के स्वामी की यह सेज कितनी प्यारी है! उस भवसागर-तारणहार ने मुझ दासी को पार लगा दिया!  
बड़े कष्टों और जन्मों के बाद आज मेरी बारी आई है, अब उनसे एक पल भी बिछुड़ना असंभव है!  
अरी सखी! आज मेरे घर में मेरे प्यारे लाल पधारे हैं!"""

k32_en = """O companions, drive the watchman away from my door!  
For today my radiant Ruby, my Beloved, steps upon my floor!  

Hour after hour he strikes the ringing gong,  
Shortening the night of union with clanging song!  
If anyone understands the yearning of my breast,  
Snatched from his hands, let that clock be laid to rest!  
O companions, drive the watchman away from my door!  

The unstruck celestial lute rings sweet and profound,  
A master minstrel weaves harmonies all around!  
Formal prayers and fasting rituals vanish from my mind,  
As the Tavern-Master pours the wine of love divine!  
O companions, drive the watchman away from my door!  

Beholding His luminous face is a marvel to the eyes,  
Every lingering sorrow of the aching spirit dies!  
Let this sacred night stretch long without end or fall,  
Erect around my heart an impenetrable wall!  
O companions, drive the watchman away from my door!  

I retain no lingering sense of this earthly frame,  
To what celestial kingdom wedded, I cannot name!  
How can this triumphant mystery ever stay concealed,  
When the peak of divine grace stands totally revealed?  
O companions, drive the watchman away from my door!  

They tried myriad amulets and magical charms in vain,  
Elders and patriarchs counselled again and again,  
Yet now that my Life’s darling has entered my home,  
For hundred thousand years beside Him shall I roam!  
O companions, drive the watchman away from my door!  

How sublime is the bridal couch of Bulleh's Lord tonight!  
The Supreme Redeemer has ferried me to shores of light!  
After endless trials my blessed turn has come to be,  
Now parting from Him is an absolute impossibility!  
O companions, drive the watchman away from my door!"""

batch.append({
    "id": 32,
    "title": "32. घड़िआली दियो निकाल नी",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k32_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "घड़िआली दियो निकाल नी ।",
                "hindi_gloss": "घड़िआली (घड़ियाल/घंटा बजाने वाले पहरेदार को) दियो (दे दो) निकाल (बाहर निकाल) नी (अरी सखी) ।",
                "english_gloss": "ghadiyaalee (gong-striker/time-keeper) diyo (give/cast) nikaal (out) neen (O friend) ."
            },
            {
                "original": "अज्ज पी घर आया लाल नी ।",
                "hindi_gloss": "अज्ज (आज) पी (मेरे प्राण-प्रियतम) घर (घर-आँगन में) आया (पधारे हैं) लाल (मेरे प्रियतम लाल) नी (अरी) ।",
                "english_gloss": "ajj (today) pee (Beloved Lord) ghar (home) aaya (has arrived) laal (ruby/darling) neen (O friend) ."
            },
            {
                "original": "घड़ी घड़ी घड़िआल बजावे, रैण वसल दी पिआ घटावे,",
                "hindi_gloss": "घड़ी (प्रत्येक घड़ी) घड़ी (घंटे पर) घड़िआल (घड़ियाल का घंटा) बजावे (बजाता है), रैण (रात को) वसल (मिलन की पावन रात) दी (को) पिआ (व्यर्थ ही) घटावे (घटा रहा है),",
                "english_gloss": "ghadee (hour) ghadee (by hour) ghadiaal (the gong) bajaave (he strikes), rain (the night) vasal (of divine union) dee (of) pia (keeps) ghataave (shortening),"
            },
            {
                "original": "मेरे मन दी बात जो पावे, हत्थों चा सुट्टो घड़िआल नी ।",
                "hindi_gloss": "मेरे (मेरे) मन (मन) दी (की) बात (व्यथा को) जो (जो कोई भी) पावे (समझ सके), हत्थों (उसके हाथों से) चा (उठाकर) सुट्टो (फेंक दो) घड़िआल (उस घड़ियाल को) नी (अरी) ।",
                "english_gloss": "mere (my) man (heart's) dee (of) baat (state) jo (whoever) paave (perceives), hatthon (from his hands) cha (seizing) sutto (throw away) ghadiaal (the gong) neen (O friend) ."
            },
            {
                "original": "अज्ज पी घर आया लाल नी ।",
                "hindi_gloss": "अज्ज (आज) पी (प्राण-प्रीतम) घर (घर) आया (पधारे) लाल (लाल) नी (अरी) ।",
                "english_gloss": "ajj (today) pee (Beloved) ghar (home) aaya (has arrived) laal (ruby) neen (O friend) ."
            },
            {
                "original": "अनहद वाजा वज्जे सुहाणा, मुतरिब सुघड़ा तान तराना,",
                "hindi_gloss": "अनहद (अनाहत नाद का) वाजा (दिव्य बाजा) वज्जे (बज रहा है) सुहाणा (अति सुहावना), मुतरिब (अलौकिक गायक) सुघड़ा (कुशल संगीतकार) तान (तान और) तराना (तराना छेड़ रहा है),",
                "english_gloss": "anhad (unstruck celestial melody) vaaja (instrument) vajje (plays) suhaana (delightful), mutrib (divine singer/musician) sughda (skillful) taan (melody) taraana (rhapsody),"
            },
            {
                "original": "निमाज़ रोज़ा भुल्ल ग्या दुगाणा, मध प्याला देण कलाल नी ।",
                "hindi_gloss": "निमाज़ (नमाज़) रोज़ा (और रोज़ा सब) भुल्ल ग्या (विस्मृत हो गया) दुगाणा (दो रकअत नमाज़ का विधान), मध (प्रेम-मदिरा का) प्याला (प्याला) देण (भरकर पिला रहे हैं) कलाल (दिव्य साक़ी) नी (अरी) ।",
                "english_gloss": "nimaaz (formal prayers) roza (fasting) bhull gya (forgotten) dugaana (two-rak'at prayer), madh (nectar/wine of love) pyaala (cup) den (is offering) kalaal (the Tavern-Master/Beloved) neen (O friend) ."
            },
            {
                "original": "अज्ज पी घर आया लाल नी ।",
                "hindi_gloss": "अज्ज (आज) पी (प्रियतम) घर (घर) आया (पधारे) लाल (लाल) नी (अरी) ।",
                "english_gloss": "ajj (today) pee (Beloved) ghar (home) aaya (has come) laal (darling) neen (O friend) ."
            },
            {
                "original": "मुख वेखण दा अजब नज़ारा, दुक्ख दिले दा उट्ठ ग्या सारा,",
                "hindi_gloss": "मुख (उनके श्रीमुख को) वेखण (देखने) दा (का) अजब (अद्भुत अलौकिक) नज़ारा (नज़ारा है), दुक्ख (सारे दुःख) दिले (हृदय) दा (के) उट्ठ ग्या (मिट गए) सारा (समस्त),",
                "english_gloss": "mukh (His holy face) vekhan (to behold) da (of) ajab (wondrous) nazaara (vision/spectacle), dukkh (sorrow) dile (of heart) da (of) utth gya (vanished) saara (entirely),"
            },
            {
                "original": "रैण वड्डी क्या करे पसारा, दिल अग्गे पारो दीवाल नी ।",
                "hindi_gloss": "रैण (यह मिलन की रात) वड्डी (और लंबी हो जाए) क्या (भला कैसा) करे (करे) पसारा (संसार का फैलाव), दिल (मेरे दिल के) अग्गे (आगे) पारो (उस पार तक) दीवाल (एक रक्षा-दीवार खड़ी कर दो) नी (अरी) ।",
                "english_gloss": "rain (this night) vaddee (extended) kya (what) kare (can do) pasaara (world's expanse), dil (heart's) agge (before) paaro (across) deevaal (build a protective wall) neen (O friend) ."
            },
            {
                "original": "अज्ज पी घर आया लाल नी ।",
                "hindi_gloss": "अज्ज (आज) पी (प्रियतम) घर (घर) आया (आया है) लाल (लाल) नी (अरी) ।",
                "english_gloss": "ajj (today) pee (Beloved) ghar (home) aaya (has arrived) laal (ruby) neen (O friend) ."
            },
            {
                "original": "मैनूं आपनी ख़बर ना काई, क्या जाणां मैं कित व्याही,",
                "hindi_gloss": "मैनूं (मुझको) आपनी (अपनी देह और सुध-बुध की) ख़बर (ख़बर) ना (नहीं) काई (रत्ती भर भी), क्या (क्या) जाणां (जानूँ) मैं (मैं कि) कित (कहाँ और किस दिव्य लोक में) व्याही (मेरा ब्याह हो गया),",
                "english_gloss": "mainoon (unto me) aapnee (my own self's) khabar (awareness) na (not) kaaee (any), kya (what) jaanaan (do I know) main (I) kit (whereunto) vyaahee (I have been wedded),"
            },
            {
                "original": "इह गल्ल क्यों कर छुपे छपाई, हुण होया फ़ज़ल कमाल नी ।",
                "hindi_gloss": "इह (यह परम प्रेम की) गल्ल (बात) क्यों कर (कैसे भला) छुपे (छिपाए) छपाई (छिप सकती है), हुण (अब तो) होया (हो गया है) फ़ज़ल (ईश्वरीय कृपा की) कमाल (पूर्णता/कमाल) नी (अरी) ।",
                "english_gloss": "eh (this) gall (mystery) kyon kar (how) chhupe (remain hidden) chhapaaee (by concealing), hun (now) hoya (has occurred) fazal (divine grace's) kamaal (supreme height) neen (O friend) ."
            },
            {
                "original": "अज्ज पी घर आया लाल नी ।",
                "hindi_gloss": "अज्ज (आज) पी (साजन) घर (घर) आया (पधारे) लाल (लाल) नी (अरी) ।",
                "english_gloss": "ajj (today) pee (Beloved) ghar (home) aaya (has arrived) laal (ruby) neen (O friend) ."
            },
            {
                "original": "टूणे टामण करे बथेरे, मिहरे आए वड्डे वडेरे,",
                "hindi_gloss": "टूणे (टोने) टामण (और तांत्रिक टोटके) करे (किए) बथेरे (बहुत सारे), मिहरे (बुजुर्ग) आए (आए) वड्डे (बड़े) वडेरे (और सयाने),",
                "english_gloss": "toone (spells) taaman (charms/amulets) kare (tried) bathere (countless), mihre (wise elders) aae (came) vadde (great) vadere (ancestors),"
            },
            {
                "original": "हुण घर आया जानी मेरे, रहां लक्ख वर्हे इहदे नाल नी ।",
                "hindi_gloss": "हुण (किंतु अब) घर (मेरे घर में) आया (पधार गए हैं) जानी (मेरे प्राण-प्यारे) मेरे (मेरे), रहां (अब तो मैं रहूँगी) लक्ख (लाखों) वर्हे (वर्षों तक) इहदे (इन्हीं के) नाल (साथ) नी (अरी) ।",
                "english_gloss": "hun (now) ghar (home) aaya (has arrived) jaanee (beloved of my life) mere (mine), rahaan (may I abide) lakkh (hundreds of thousands) varhe (of years) ehde (with Him) naal (together) neen (O friend) ."
            },
            {
                "original": "अज्ज पी घर आया लाल नी ।",
                "hindi_gloss": "अज्ज (आज) पी (प्रियतम) घर (घर) आया (आए हैं) लाल (लाल) नी (अरी) ।",
                "english_gloss": "ajj (today) pee (Beloved) ghar (home) aaya (has come) laal (ruby) neen (O friend) ."
            },
            {
                "original": "बुल्हा शहु दी सेज़ प्यारी, नी मैं तारनहारे तारी,",
                "hindi_gloss": "बुल्हा (बुल्ले) शहु (के प्राण-स्वामी) दी (की) सेज़ (मिलन-सेज) प्यारी (अति सुखदाई है), नी (अरी सखी) मैं (मुझ डूबती हुई को) तारनहारे (उस तारनहार स्वामी ने) तारी (पार उतार दिया),",
                "english_gloss": "bullha (Bulleh's) shahu (Lord's) dee (of) sez (nuptial bed) pyaaree (beloved/sweet), neen (O friend) main (me) taaranhaare (the Redeemer) taaree (has ferried across),"
            },
            {
                "original": "किवें किवें हुण आई वारी, हुण विछड़न होया मुहाल नी ।",
                "hindi_gloss": "किवें (जैसे-तैसे) किवें (बड़े भाग्य से) हुण (अब) आई (आई है) वारी (मेरी मिलन की बारी), हुण (अब इनसे) विछड़न (वियोग होना) होया (हो गया है) मुहाल (असंभव) नी (अरी) ।",
                "english_gloss": "kiven (somehow) kiven (by immense fortune) hun (now) aayee (has arrived) vaaree (my turn), hun (now) vichhadan (parting/separation) hoya (has become) muhaal (impossible) neen (O friend) ."
            },
            {
                "original": "अज्ज पी घर आया लाल नी ।",
                "hindi_gloss": "अज्ज (आज) पी (प्रियतम) घर (घर) आया (आया है) लाल (लाल) नी (अरी) ।",
                "english_gloss": "ajj (today) pee (Beloved) ghar (home) aaya (has arrived) laal (ruby) neen (O friend) ."
            }
        ],
        "hindi_meaning": k32_hi,
        "english_meaning": k32_en
    }]
})

# ==========================================
# KAFI 33: 33. घर में गंगा आई संतो, घर में गंगा आई
# ==========================================
k33_orig = """घर में गंगा आई संतो, घर में गंगा आई ।
आपे मुरली आप घनईआ, आपे जादूराई ।
आप गोबरिया आप गडरिया, आपे देत दिखाई ।
अनहद दवार का आया गवरिया, कंङण दसत चढ़ाई ।
मूंड मुंडा मोहे परीती कोरेन कन्नां मैं पाई ।
अम्मृत फल खा ल्यो रे गुसाईं, थोड़ी करो बफाई ।
घर में गंगा आई संतो, घर में गंगा आई ।"""

k33_hi = """हे संतो! आज मेरे हृदय-घर में ही पावन गंगा उतर आई है!  
वह स्वयं ही मुरली है, स्वयं ही घनश्याम है, और स्वयं ही यदुराय कृष्ण है!  
वह स्वयं ही गाय चराने वाला ग्वाला है और स्वयं ही सेवाभावी ग्वालिन है, वह हर रूप में साक्षात दर्शन दे रहा है!  
अनाहत नाद के दशम द्वार से वह दिव्य ग्वाला पधारा है, जिसने मेरे हाथों में प्रेम का कंगन पहना दिया है!  
अहंकार का शीश मुंडवाकर उसने मेरे कानों में प्रेम की अविनाशी मुद्रा पहना दी है!  
हे मेरे प्राण-गोसाईं! इस आत्म-अमृत के पावन फल को ग्रहण करो, और अपनी दासी पर तनिक कृपा की नज़र करो!  
हे संतो! आज मेरे हृदय-घर में ही पावन गंगा उतर आई है!"""

k33_en = """O saints, the sacred Ganges has flowed into my home today!  
He Himself is the flute, Himself dark Krishna, Himself the Sovereign of Yadus in sweet display!  
He Himself is the humble cowherd maid, Himself the shepherd on the lea,  
Visible everywhere in His wondrous cosmic decree!  
From the portal of the Unstruck Realm, the divine cowherd came down to stand,  
Placing the luminous bangles of love upon my willing hand!  
Shaving the head of pride, He inserted love’s mystic rings in my ear,  
Partake of this nectar-fruit, O Lord, and hold this faithful servant dear!  
O saints, the sacred Ganges has flowed into my home today!"""

batch.append({
    "id": 33,
    "title": "33. घर में गंगा आई संतो, घर में गंगा आई",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k33_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "घर में गंगा आई संतो, घर में गंगा आई ।",
                "hindi_gloss": "घर (मेरे अंतःकरण के घर) में (में) गंगा (आत्मज्ञान की पावन गंगा) आई (उतर आई है) संतो (हे संतो), घर (घट के भीतर) में (में) गंगा (गंगा) आई (आ गई है) ।",
                "english_gloss": "ghar (home of the heart) mein (in) ganga (Ganges of divine realization) aayee (has arrived) santo (O saints), ghar (in the soul) mein (in) ganga (Ganges) aayee (has arrived) ."
            },
            {
                "original": "आपे मुरली आप घनईआ, आपे जादूराई ।",
                "hindi_gloss": "आपे (वह स्वयं ही) मुरली (मुरली/बांसुरी है) आप (स्वयं ही) घनईआ (घनश्याम/कृष्ण है), आपे (स्वयं ही) जादूराई (यदुराय/जादूगर प्रभु है) ।",
                "english_gloss": "aape (Himself) murlee (the flute) aap (Himself) ghanayeea (Krishna/Ghanashyam), aape (Himself) jaadooraaee (Jadurai/Lord of Yadus) ."
            },
            {
                "original": "आप गोबरिया आप गडरिया, आपे देत दिखाई ।",
                "hindi_gloss": "आप (स्वयं ही गोपी) गोबरिया (गोबर लीपने/सेवा करने वाली ग्वालिन) आप (स्वयं ही) गडरिया (ग्वाला/पशुपालक), आपे (स्वयं ही सर्वत्र) देत (दे रहा) दिखाई (दर्शन है) ।",
                "english_gloss": "aap (Himself) gobariya (cowherd maid/cleaner) aap (Himself) gadariya (shepherd/cowherd), aape (Himself) det (giving) dikhaaee (manifests/visible) ."
            },
            {
                "original": "अनहद दवार का आया गवरिया, कंङण दसत चढ़ाई ।",
                "hindi_gloss": "अनहद (अनाहत नाद के) दवार (द्वार/दशम द्वार) का (से) आया (आया है) गवरिया (वह दिव्य ग्वाला कृष्ण), कंङण (और मेरे) दसत (हाथों में प्रेम के कंगन) चढ़ाई (पहना दिए हैं) ।",
                "english_gloss": "anhad (unstruck sound's) davaar (portal/Tenth Gate) ka (from) aaya (came) gavariya (the divine cowherd), kankan (bangles of love) dast (upon hands) chadhaaee (placed) ."
            },
            {
                "original": "मूंड मुंडा मोहे परीती कोरेन कन्नां मैं पाई ।",
                "hindi_gloss": "मूंड (अहंकार का शीश) मुंडा (मुंडवाकर/समर्पित कर) मोहे (मुझको) परीती (ईश्वरीय प्रेम की) कोरेन (मुद्रा/कुंडल) कन्नां (कानों) मैं (में) पाई (पहना दी है) ।",
                "english_gloss": "moond (head of ego) mundaa (shaved/surrendered) mohe (unto me) pareetee (of divine love) koren (earrings/rings) kannaan (in ears) main (in) paaee (inserted) ."
            },
            {
                "original": "अम्मृत फल खा ल्यो रे गुसाईं, थोड़ी करो बफाई ।",
                "hindi_gloss": "अम्मृत (अमर आत्म-रस का) फल (फल) खा ल्यो (चख लो/ग्रहण करो) रे (रे) गुसाईं (हे मेरे गोसाईं/स्वामी), थोड़ी (अब तनिक) करो (करो) बफाई (वफ़ा/सच्ची कृपा) ।",
                "english_gloss": "amrit (nectar) phal (fruit) khaa lyo (partake of) re (O) gusaa-een (Lord/Master), thodee (a little) karo (show) bafaaee (faithfulness/grace) ."
            },
            {
                "original": "घर में गंगा आई संतो, घर में गंगा आई ।",
                "hindi_gloss": "घर (मेरे अंतर्हृदय) में (में) गंगा (गंगा) आई (आई है) संतो (हे संतो), घर (हृदय) में (में) गंगा (गंगा) आई (आई है) ।",
                "english_gloss": "ghar (in the home) mein (in) ganga (Ganges) aayee (has arrived) santo (O saints), ghar (in home) mein (in) ganga (Ganges) aayee (has arrived) ."
            }
        ],
        "hindi_meaning": k33_hi,
        "english_meaning": k33_en
    }]
})

# ==========================================
# KAFI 34: 34. घुंघट चुक्क ओ सजणा, हुण शरमां काहनूं रक्खियां वे
# ==========================================
k34_orig = """ज़ुल्फ़ कुंडल ने घेरा पाइआ, बिसियर हो के डंग चलाइआ,
वेख असां वल्ल तरस ना आया, कर के खूनी अक्खियां वे ।
घुंघट चुक्क ओ सजणा, हुण शरमां काहनूं रक्खियां वे ।

दो नैणां दा तीर चलाइआ, मैं आज़िज़ दे सीने लाइआ,
घायल कर के मुक्ख छुपाइआ, चोरियां इह किन दस्सियां वे ।
घुंघट चुक्क ओ सजणा, हुण शरमां काहनूं रक्खियां वे ।

ब्रिहों कटारी तूं कस्स के मारी, तद मैं होई बेदिल भारी,
मुड़ ना लई तैं सार हमारी, पतियां तेरियां कच्चियां वे ।
घुंघट चुक्क ओ सजणा, हुण शरमां काहनूं रक्खियां वे ।

नेहुं लगा के मन हर लीता, फेर ना आपणा दरशन दीता,
ज़हर प्याला मैं इह पीता, सां अकलों मैं कच्चियां वे ।
घुंघट चुक्क ओ सजणा, हुण शरमां काहनूं रक्खियां वे ।"""

k34_hi = """तुम्हारी घुंघराली काली लटों ने मुझे चारों तरफ़ से घेर लिया,  
और काले नाग की तरह मुझ पर विरह का डंक मार दिया!  
अपनी नशीली-कातिल आँखों से घायल करके, तुम्हें मुझ पर ज़रा भी तरस न आया!  
हे साजन! अब अपना घूँघट उठा दो, अब यह कैसी लोक-लाज और पर्दा रख रखा है?  

अपने दोनों नयनों के तीक्ष्ण बाण चलाकर, मुझ दीन-हीन के सीने को छलनी कर दिया,  
और मुझे तड़पता हुआ घायल छोड़कर अपना मुखड़ा छिपा लिया!  
पीठ पीछे छिपकर वार करने की यह चोरी तुम्हें किसने सिखाई है?  
हे साजन! अब अपना घूँघट उठा दो, अब यह कैसी लोक-लाज और पर्दा रख रखा है?  

विरह की कटार तुमने पूरे बल से मेरे हृदय में उतार दी,  
जिससे मैं विह्वल और मूर्छित होकर गिर पड़ी!  
घायल करके फिर कभी तुमने पलटकर मेरी सुध तक न ली, तुम्हारे सारे वादे कच्चे निकले!  
हे साजन! अब अपना घूँघट उठा दो, अब यह कैसी लोक-लाज और पर्दा रख रखा है?  

पहले तो मीठा प्रेम लगाकर मेरा मन हर लिया,  
और फिर मुड़कर कभी अपना दीदार तक न कराया!  
मैंने इस विरह का ज़हर का प्याला पी लिया है, मैं ही नादान थी जो तुम्हारी बातों में आ गई!  
हे साजन! अब अपना घूँघट उठा दो, अब यह कैसी लोक-लाज और पर्दा रख रखा है?"""

k34_en = """The curling ringlets of thy hair have encircled me in a snare,  
Striking like a black serpent's fang, beyond all mortal care!  
With slaying eyes that pierce the soul, no mercy didst thou show,  
Lift the veil, O Beloved! Why holdest thou this modest curtain so?  

Thou didst loose the piercing arrows from thine intoxicating eyes,  
Striking the tender breast of this helpless maid beneath the skies!  
Leaving me mortally wounded, thou didst turn and hide thy face,  
Who taught thee this art of stealthy theft and vanished grace?  
Lift the veil, O Beloved! Why holdest thou this modest curtain so?  

Thou didst plunge the dagger of separation deep into my core,  
Leaving me shattered and undone upon a lonely shore!  
Never once didst thou return to ask how thy wounded bride did fare,  
All thy solemn vows were fragile webs dissolved in empty air!  
Lift the veil, O Beloved! Why holdest thou this modest curtain so?  

Entangling me in cords of love, thou stolest my very heart away,  
Yet never showed thy radiant face to brighten my dark day!  
I have drained this cup of deadly poison to the final draught in pain,  
How simple and naive was I to believe that love could be my gain!  
Lift the veil, O Beloved! Why holdest thou this modest curtain so?"""

batch.append({
    "id": 34,
    "title": "34. घुंघट चुक्क ओ सजणा, हुण शरमां काहनूं रक्खियां वे",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k34_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "ज़ुल्फ़ कुंडल ने घेरा पाइआ, बिसियर हो के डंग चलाइआ,",
                "hindi_gloss": "ज़ुल्फ़ (काली लटों के) कुंडल (घुंघराले छल्ले) ने (ने) घेरा (चारों तरफ़ से घेरा) पाइआ (डाल दिया है), बिसियर (काले नाग की नाईं) हो के (होकर) डंग (विरह का डंक) चलाइआ (मार दिया है),",
                "english_gloss": "zulf (tresses) kundal (curled rings) ne (have) ghera (encirclement) paaia (cast), bisiyar (venomous serpent) ho ke (becoming) dang (sting) chlaaia (struck),"
            },
            {
                "original": "वेख असां वल्ल तरस ना आया, कर के खूनी अक्खियां वे ।",
                "hindi_gloss": "वेख (देखकर) असां (मेरी) वल्ल (ओर ज़रा भी) तरस (दया/तरस) ना (नहीं) आया (आया), कर के (करके) खूनी (रक्त-पिपासु कातिलाना) अक्खियां (नशीली आँखें) वे (हे प्रियतम) ।",
                "english_gloss": "vekh (beholding) asaan (me) vall (toward) taras (pity/mercy) na (not) aaya (came), kar ke (making) khoonee (murderous/slaying) akkheeyaan (eyes) ve (O Beloved) ."
            },
            {
                "original": "घुंघट चुक्क ओ सजणा, हुण शरमां काहनूं रक्खियां वे ।",
                "hindi_gloss": "घुंघट (अपना घूँघट) चुक्क (उठा दो) ओ (हे) सजणा (साजन), हुण (अब भला) शरमां (यह लज्जा और पर्दा) काहनूं (किसलिए) रक्खियां (रख रखा है) वे (हे प्रियतम) ।",
                "english_gloss": "ghoonaghat (the veil) chukk (lift) o (O) sajna (Beloved), hun (now) sharmaan (shame/coyness) kaahnoon (why) rakkheeyaan (hast thou kept) ve (O Friend) ."
            },
            {
                "original": "दो नैणां दा तीर चलाइआ, मैं आज़िज़ दे सीने लाइआ,",
                "hindi_gloss": "दो (दोनों) नैणां (नेत्रों) दा (का तीक्ष्ण) तीर (बाण) चलाइआ (चलाया), मैं (मुझ) आज़िज़ (दीन-असमर्थ दासी) दे (के) सीने (हृदय में) लाइआ (मार दिया),",
                "english_gloss": "do (both) nainaan (eyes') da (of) teer (arrow) chlaaia (thou didst loose), main (me) aaziz (helpless humble one) de (of) seene (in breast) laaia (lodged),"
            },
            {
                "original": "घायल कर के मुक्ख छुपाइआ, चोरियां इह किन दस्सियां वे ।",
                "hindi_gloss": "घायल (घायल) कर के (करके अपना) मुक्ख (मुखड़ा) छुपाइआ (छिपा लिया), चोरियां (यह चोरी-छिपे वार करने की रीति) इह (यह) किन (किसने तुम्हें) दस्सियां (सिखाई) वे (हे प्रियतम) ।",
                "english_gloss": "ghaayal (wounded) kar ke (having made) mukkh (face) chhupaaia (hid), choreeyaan (thefts/stealthy ways) eh (these) kin (who) dasseeyaan (taught thee) ve (O Friend) ."
            },
            {
                "original": "घुंघट चुक्क ओ सजणा, हुण शरमां काहनूं रक्खियां वे ।",
                "hindi_gloss": "घुंघट (घूँघट) चुक्क (उठाओ) ओ (हे) सजणा (साजन), हुण (अब) शरमां (शरम/पर्दा) काहनूं (क्यों) रक्खियां (रखते हो) वे (हे सजन) ।",
                "english_gloss": "ghoonaghat (veil) chukk (lift) o (O) sajna (Beloved), hun (now) sharmaan (shyness) kaahnoon (why) rakkheeyaan (hast kept) ve (O Friend) ."
            },
            {
                "original": "ब्रिहों कटारी तूं कस्स के मारी, तद मैं होई बेदिल भारी,",
                "hindi_gloss": "ब्रिहों (विरह की) कटारी (कटार) तूं (तुमने) कस्स के (पूरी ताक़त से खींचकर) मारी (मारी), तद (तभी से) मैं (मैं) होई (हो गई हूँ) बेदिल (बेहोश और विह्वल) भारी (अत्यधिक),",
                "english_gloss": "brihon (of separation) kataaree (dagger) toon (thou) kass ke (with full force) maaree (struck), tad (thence) main (I) hoee (became) bedil (broken-hearted/senseless) bhaaree (heavily),"
            },
            {
                "original": "मुड़ ना लई तैं सार हमारी, पतियां तेरियां कच्चियां वे ।",
                "hindi_gloss": "मुड़ (फिर पलटकर) ना (नहीं) लई (ली) तैं (तुमने) सार (सुध/ख़बर) हमारी (हमारी), पतियां (प्रतिज्ञाएं और वादे) तेरियां (तुम्हारे) कच्चियां (सब कच्चे निकले) वे (हे साजन) ।",
                "english_gloss": "mud (again/ever) na (not) laee (took) tain (thou) saar (news/care) hamaaree (our), pateeyaan (promises/vows) tereeyaan (thy) kachheeyaan (proved false/frail) ve (O Friend) ."
            },
            {
                "original": "घुंघट चुक्क ओ सजणा, हुण शरमां काहनूं रक्खियां वे ।",
                "hindi_gloss": "घुंघट (घूँघट) चुक्क (हटाओ) ओ (हे) सजणा (साजन), हुण (अब) शरमां (पर्दा) काहनूं (क्यों) रक्खियां (रखा है) वे (हे प्रिय) ।",
                "english_gloss": "ghoonaghat (veil) chukk (lift) o (O) sajna (Beloved), hun (now) sharmaan (veil/shame) kaahnoon (why) rakkheeyaan (hast kept) ve (O Friend) ."
            },
            {
                "original": "नेहुं लगा के मन हर लीता, फेर ना आपणा दरशन दीता,",
                "hindi_gloss": "नेहुं (प्रेम) लगा के (लगाकर मेरा) मन (मन) हर लीता (चुरा लिया), फेर (फिर पलटकर) ना (नहीं) आपणा (अपना पावन) दरशन (दीदार) दीता (दिया),",
                "english_gloss": "nehun (love) laga ke (weaving) man (mind/heart) har leeta (stole away), pher (then again) na (not) aapna (thy own) darshan (vision/sight) deeta (granted),"
            },
            {
                "original": "ज़हर प्याला मैं इह पीता, सां अकलों मैं कच्चियां वे ।",
                "hindi_gloss": "ज़हर (विष का) प्याला (प्याला) मैं (मैंने) इह (यह विरह का) पीता (पी लिया है), सां (थी) अकलों (बुद्धि से) मैं (मैं ही) कच्चियां (नादान और अल्हड़) वे (हे साजन) ।",
                "english_gloss": "zahar (poison) pyaala (cup) main (I) eh (this) peeta (have drunk), saan (was) aklon (in intellect) main (I) kachheeyaan (naive/raw) ve (O Friend) ."
            },
            {
                "original": "घुंघट चुक्क ओ सजणा, हुण शरमां काहनूं रक्खियां वे ।",
                "hindi_gloss": "घुंघट (घूँघट) चुक्क (उठाओ) ओ (हे) सजणा (साजन), हुण (अब) शरमां (लाज का घूँघट) काहनूं (किसलिए) रक्खियां (रख रखा है) वे (हे प्यारे) ।",
                "english_gloss": "ghoonaghat (veil) chukk (lift) o (O) sajna (Beloved), hun (now) sharmaan (coyness) kaahnoon (why) rakkheeyaan (hast kept) ve (O Friend) ."
            }
        ],
        "hindi_meaning": k34_hi,
        "english_meaning": k34_en
    }]
})

# ==========================================
# KAFI 35: 35. घुंघट ओहले ना लुक्क सोहणिआँ
# ==========================================
k35_orig = """घुंघट ओहले ना लुक्क सोहणिआँ,
मैं मुशताक दीदार दी हां ।

जानी बाझ दीवानी होई, टोकां करदे लोक सभोई,
जे कर यार करे दिलजोई, मैं तां फरिआद पुकारदी हां ।
मैं मुशताक दीदार दी हां ।

मुफ़त विकांदी जांदी बांदी, मिल माहिया जिन्द ऐंवें जांदी,
इकदम हिजर नहीं मैं सहिंदी, मैं बुलबुल इस गुलज़ार दी हां ।
मैं मुशताक दीदार दी हां ।"""

k35_hi = """घूँघट की ओट में मत छिपो, हे मेरे सुंदर प्रीतम!  
मैं तो बस तुम्हारे पावन दीदार की प्यासी हूँ!  

अपने प्राण-प्यारे के बिना मैं मतवाली बावरी हो गई हूँ, सारा संसार मुझ पर तानों के तीर चलाता है!  
यदि मेरा यार ही मुझे तसल्ली न देगा, तो मैं यह विरह की फ़रियाद किसके आगे पुकारूँ!  
मैं तो बस तुम्हारे पावन दीदार की प्यासी हूँ!  

तुम्हारी यह दासी तो तुम्हारे प्रेम में कौड़ियों के मोल मुफ्त बिक चुकी है!  
हे माही! आकर मिल जाओ, विरह में मेरी यह जान यूँ ही निकली जा रही है!  
एक पल के लिए भी यह वियोग मुझसे सहन नहीं होता, मैं तो तुम्हारे इस प्रेम-बाग़ की चहकती बुलबुल हूँ!  
मैं तो बस तुम्हारे पावन दीदार की प्यासी हूँ!"""

k35_en = """Hide not behind the veil, O Beautiful One divine!  
I thirst solely for that radiant countenance of thine!  

Bereft of my Soul’s darling, I am driven wild and mad,  
The entire world hurls mockery at a heart so bruised and sad!  
If my Beloved does not soothe this burning pain,  
To whom else shall I cry this lament in vain?  
I thirst solely for that radiant countenance of thine!  

Thy humble bondmaid sells herself for naught at thy feet,  
Come meet me, O Maahi, before life's fading pulses retreat!  
Not for a single breath can I endure separation's sting,  
I am the nightingale meant in thy rose garden to sing!  
I thirst solely for that radiant countenance of thine!"""

batch.append({
    "id": 35,
    "title": "35. घुंघट ओहले ना लुक्क सोहणिआँ",
    "section": "भाग 1 (काफ़ियां 1–50)",
    "original_poem": k35_orig,
    "annotated_stanzas": [{
        "lines": [
            {
                "original": "घुंघट ओहले ना लुक्क सोहणिआँ,",
                "hindi_gloss": "घुंघट (घूँघट की) ओहले (ओट में) ना (मत) लुक्क (छिपो) सोहणिआँ (हे मेरे परम सुंदर साजन),",
                "english_gloss": "ghoonaghat (veil's) ohle (behind/in shelter) na (not) lukk (hide) sohniyaan (O Beautiful One),"
            },
            {
                "original": "मैं मुशताक दीदार दी हां ।",
                "hindi_gloss": "मैं (मैं तो केवल) मुशताक (दीवानी/प्यासी) दीदार (तुम्हारे पावन दर्शन) दी (की) हां (हूँ) ।",
                "english_gloss": "main (I) mushtaak (ardently longing) deedaar (sight/vision) dee (of) haan (am) ."
            },
            {
                "original": "जानी बाझ दीवानी होई, टोकां करदे लोक सभोई,",
                "hindi_gloss": "जानी (अपने प्राण-प्रियतम के) बाझ (बिना) दीवानी (पागल/बावरी) होई (हो चुकी हूँ), टोकां (ताने और व्यंग्य) करदे (करते हैं) लोक (संसार के लोग) सभोई (समस्त),",
                "english_gloss": "jaanee (Beloved of soul) baajh (without) deevaanee (crazed) hoee (have become), tokaan (taunts) karde (make) lok (people) sabhoee (all),"
            },
            {
                "original": "जे कर यार करे दिलजोई, मैं तां फरिआद पुकारदी हां ।",
                "hindi_gloss": "जे कर (यदि) यार (मेरा प्यारा यार) करे (करे) दिलजोई (मेरी तसल्ली और सांत्वना), मैं तां (तभी तो मैं) फरिआद (अपने प्रेम की पुकार) पुकारदी (लगा रही) हां (हूँ) ।",
                "english_gloss": "je kar (if only) yaar (Beloved) kare (offers) diljoee (consolation), main taan (that is why I) fariaad (plaintive cry) pukaardee (call out) haan (am) ."
            },
            {
                "original": "मैं मुशताक दीदार दी हां ।",
                "hindi_gloss": "मैं (मैं तो) मुशताक (व्याकुल अभिलाषिणी) दीदार (दीदार) दी (की) हां (हूँ) ।",
                "english_gloss": "main (I) mushtaak (longing seeker) deedaar (of vision) dee (of) haan (am) ."
            },
            {
                "original": "मुफ़त विकांदी जांदी बांदी, मिल माहिया जिन्द ऐंवें जांदी,",
                "hindi_gloss": "मुफ़त (बिना किसी मूल्य के) विकांदी जांदी (बिकती जा रही है यह) बांदी (तुम्हारी दासी), मिल (मुझसे मिल जाओ) माहिया (हे प्यारे माही) जिन्द (यह जीवन) ऐंवें (यूँ ही व्यर्थ) जांदी (बीता जा रहा है),",
                "english_gloss": "mufat (free of cost) vikaandee jaandee (getting sold away) baandee (slave-maid), mil (meet me) maahiya (O Beloved) jind (life) aiven (in vain) jaandee (is ebbing away),"
            },
            {
                "original": "इकदम हिजर नहीं मैं सहिंदी, मैं बुलबुल इस गुलज़ार दी हां ।",
                "hindi_gloss": "इकदम (एक क्षण के लिए भी) हिजर (विरह की तड़प) नहीं (नहीं) मैं (मुझसे) सहिंदी (सही जाती), मैं (मैं तो) बुलबुल (बुलबुल) इस (तुम्हारे इस प्रेम रूपी) गुलज़ार (उद्यान) दी (की) हां (हूँ) ।",
                "english_gloss": "ikdam (for a single breath) hijar (torment of separation) naaheen (not) main (I) sahindi (can endure), main (I) bulbul (the nightingale) is (of this) gulzaar (rose garden) dee (of) haan (am) ."
            },
            {
                "original": "मैं मुशताक दीदार दी हां ।",
                "hindi_gloss": "मैं (मैं तो) मुशताक (प्यासी) दीदार (तुम्हारे दीदार) दी (की) हां (हूँ) ।",
                "english_gloss": "main (I) mushtaak (yearning) deedaar (of vision) dee (of) haan (am) ."
            }
        ],
        "hindi_meaning": k35_hi,
        "english_meaning": k35_en
    }]
})

# Save each Kafi to data/kafian/
for k in batch:
    k_id = k["id"]
    fname = os.path.join(KAFIAN_DIR, f"kafi_{k_id:03d}.json")
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(k, f, ensure_ascii=False, indent=2)
    print(f"Saved {fname}")

# Update checkpoint.json
with open(CHECKPOINT_JSON, "r", encoding="utf-8") as f:
    chk = json.load(f)

chk["completed_ids"] = sorted(list(set(chk["completed_ids"] + [k["id"] for k in batch])))
chk["completed_count"] = len(chk["completed_ids"])
chk["last_updated"] = datetime.now().isoformat()
chk["next_kafi_id"] = max(chk["completed_ids"]) + 1
chk["status"] = "in_progress"

with open(CHECKPOINT_JSON, "w", encoding="utf-8") as f:
    json.dump(chk, f, ensure_ascii=False, indent=2)

print(f"Checkpoint updated: {chk['completed_count']}/160 completed. Next ID: {chk['next_kafi_id']}")

# Update lexicon
if os.path.exists(LEXICON_JSON):
    with open(LEXICON_JSON, "r", encoding="utf-8") as f:
        lexicon = json.load(f)
else:
    lexicon = {}

new_words_count = 0
for k in batch:
    for st in k.get("annotated_stanzas", []):
        for line_item in st.get("lines", []):
            h_gloss = line_item.get("hindi_gloss", "")
            e_gloss = line_item.get("english_gloss", "")
            h_matches = re.findall(r"([^\s\(\)]+)\s*\(([^)]+)\)", h_gloss)
            e_matches = re.findall(r"([^\s\(\)]+)\s*\(([^)]+)\)", e_gloss)
            for i in range(min(len(h_matches), len(e_matches))):
                punj_word = h_matches[i][0].strip("।,").strip()
                hi_meaning = h_matches[i][1].strip()
                en_meaning = e_matches[i][1].strip()
                if punj_word and punj_word not in lexicon:
                    lexicon[punj_word] = {"hi": hi_meaning, "en": en_meaning}
                    new_words_count += 1

with open(LEXICON_JSON, "w", encoding="utf-8") as f:
    json.dump(lexicon, f, ensure_ascii=False, indent=2)

print(f"Lexicon updated: added {new_words_count} new entries, total now {len(lexicon)}")
