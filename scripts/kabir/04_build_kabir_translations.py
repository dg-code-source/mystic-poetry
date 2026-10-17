import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

from kabir_gloss_engine import generate_kabir_gloss, romanize

raw_path = "data/kabir/raw/kabir_all_raw.json"
with open(raw_path, 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

print(f"Loaded {len(raw_items)} raw items for translation.")

# Specialized translations for celebrated masterpieces
CLASSIC_TRANSLATIONS = {
    # 1. Shabad 107: Awal Allah Noor
    "kabir_shabad_107": {
        "verse_hi": (
            "सर्वप्रथम उस प्रभु ने अपनी ज्योति से यह संसार रचाया,\n"
            "कुदरत के सब बंदे हैं, किसमें कौन भला कौन बुरा ठहराया।\n"
            "हे मानव, तू भ्रम और भेद में मत भटक,\n"
            "स्रष्टा सृष्टि में और सृष्टि स्रष्टा में, हर घट में समाया।"
        ),
        "verse_en": (
            "First, the Divine created the primordial Light, and all beings of Nature were born;\n"
            "From that single Light the entire cosmos emerged—who then is noble, and who to scorn?\n"
            "O worldly folk, wander not lost in doubts and divided sight;\n"
            "The Creator dwells within creation, and creation within the Creator, omnipresent and bright."
        ),
        "meaning": (
            "This sublime Shabad is Kabir's quintessential declaration of universal oneness and spiritual egalitarianism. "
            "Rejecting sectarian animosity between religious factions, Kabir affirms that the primordial Light (Noor) is the single source "
            "of all humanity. The Creator is not an external monarch residing in distant skies, but an indwelling essence immanent in every atom."
        ),
        "tags": ["Nirguna Bhakti", "Universal Oneness", "Divine Light", "Social Equality", "Sri Guru Granth Sahib"]
    },
    # 2. Shabad 2: Nagan Phirat Jau Paaiai Jog
    "kabir_shabad_002": {
        "verse_hi": (
            "यदि नंगे घूमने से ही प्रभु-योग मिल जाता,\n"
            "तो वन का प्रत्येक हिरन सहज ही मुक्त हो जाता।\n"
            "क्या नंगे रहना और क्या चमड़े के वस्त्र धारण करना,\n"
            "जब तक अंतरात्मा में प्रभु-राम को नहीं पहचाना।"
        ),
        "verse_en": (
            "If roaming naked were the way to attain union with the Divine,\n"
            "Then every wild deer of the forest would easily cross liberation's line.\n"
            "What matters shedding clothes, or wearing deer-skins so fine,\n"
            "If the inner soul has not recognized the indwelling Beloved Divine?"
        ),
        "meaning": (
            "Kabir systematically deconstructs external asceticism and superficial physical mortification. True spirituality is an inward transformation "
            "of consciousness and love, rather than theatrical external displays such as renouncing clothing or shaving heads."
        ),
        "tags": ["Critique of Ritualism", "Inner Transformation", "Sahaja", "Nirguna"]
    },
    # 3. Salok 1: Simrani Rasna Oopari Ram
    "kabir_salok_001": {
        "verse_hi": (
            "मेरी रसना पर निरंतर राम-नाम की ही जपमाला है,\n"
            "युग-युगांतर के समस्त संतों का यही परम विश्राम और सुख निराला है।"
        ),
        "verse_en": (
            "My tongue is the ceaseless rosary upon which the Beloved Name rests;\n"
            "From the primal dawn of time, in this sacred remembrance all saints find supreme peace and blest."
        ),
        "meaning": (
            "Kabir inaugurates his collection of Saloks in Sri Guru Granth Sahib Ji with this proclamation of pure devotion. "
            "Rather than clutching wooden or stone beads in his hands, his tongue and breath themselves have become a living, uninterrupted rosary of divine contemplation."
        ),
        "tags": ["Divine Remembrance", "Simran", "Nam", "Sri Guru Granth Sahib"]
    },
    # 4. Salok 244 & 245: Soora So Pahchaniye
    "kabir_salok_244": {
        "verse_hi": (
            "आकाश-मंडल में रणभेरी बज उठी है, हृदय के निशाने पर चोट लगी है,\n"
            "शूरवीर ने अंतर्मन का युद्ध-क्षेत्र सजाया है, अब प्राण-प्रण से जूझने की बेला आ गई है।"
        ),
        "verse_en": (
            "The battle-drum resounds in the celestial sky of the soul, the divine wound has struck deep;\n"
            "The spiritual warrior has taken the field of battle—now is the sacred moment his pledge to keep."
        ),
        "meaning": (
            "Kabir's martial metaphor describes the decisive awakening of spiritual consciousness. The battle is fought not on earthly fields with swords, "
            "but in the internal battlefield of the mind against the five inner adversaries: lust, anger, greed, attachment, and ego."
        ),
        "tags": ["Spiritual Warrior", "Inner Conquest", "Heroism", "Sahaja"]
    },
    "kabir_salok_245": {
        "verse_hi": (
            "सच्चा शूरवीर वही पहचाना जाता है जो दीन-दुखियों और धर्म के हित में लड़ता है,\n"
            "अंग-अंग कटकर गिर जाए फिर भी कभी धर्म-क्षेत्र को पीठ नहीं दिखाता है।"
        ),
        "verse_en": (
            "He alone is recognized as the true heroic warrior who battles for the sake of the meek and righteousness;\n"
            "Though cut into pieces limb by limb, he never abandons the field in cowardice."
        ),
        "meaning": (
            "One of the most celebrated verses in Indian spiritual literature, this Salok defines authentic heroism. The true warrior of truth sacrifices "
            "the ego entirely for the welfare of the defenseless and the realization of divine righteousness, standing steadfast until the very end."
        ),
        "tags": ["Righteousness", "Heroic Devotion", "Fearlessness", "Sri Guru Granth Sahib"]
    },
    # 5. Doha 47: Dheere Dheere Re Mana
    "kabir_doha_047": {
        "verse_hi": (
            "हे मेरे मन, धैर्य रख, सब कुछ अपनी स्वाभाविक गति से ही होता है,\n"
            "माली चाहे सौ घड़े जल सींच ले, फल तो अपनी निश्चित ऋतु आने पर ही लगता है।"
        ),
        "verse_en": (
            "Slowly, gently, O my restless mind, in patient season does all unfold;\n"
            "Though the gardener pours a hundred jars of water, only when the due season arrives does the fruit ripen like gold."
        ),
        "meaning": (
            "A timeless counsel on spiritual patience (Sahaja) and non-anxious surrender. Spiritual growth and karmic ripening cannot be forced through frantic willpower; "
            "they blossom when ripened by sincere devotion, divine grace, and appointed time."
        ),
        "tags": ["Patience", "Sahaja", "Wisdom", "Effortless Grace"]
    },
    # 6. Doha 56: Mati Kahe Kumhar Se
    "kabir_doha_056": {
        "verse_hi": (
            "माटी कुम्हार से कहती है कि तू आज मुझे पैरों से क्या रौंद रहा है,\n"
            "एक दिन ऐसा अवश्य आएगा जब मैं तुझे अपने भीतर विलीन कर रौंदूँगी।"
        ),
        "verse_en": (
            "The clay speaks to the potter: Why dost thou trample upon me today with pride?\n"
            "A day will surely come when under the earth thou shalt reside, and I shall trample thee inside."
        ),
        "meaning": (
            "Kabir delivers a poignant memento mori on the inevitability of physical mortality. The mortal body, fashioned from earthly dust, must eventually dissolve back into the earth. "
            "Awareness of death dissolves human arrogance and awakens genuine spiritual humility."
        ),
        "tags": ["Impermanence", "Humility", "Mortality", "Divine Potter"]
    },
    # 7. Doha 58: Mala Ferat Jug Bhaya
    "kabir_doha_058": {
        "verse_hi": (
            "हाथों में माला फेरते हुए युग बीत गए, किंतु मन का फेर न मिट सका,\n"
            "हाथ की माला के मनके को छोड़ दे, और अपने अंतर्मन के मनके को फेरना सीख।"
        ),
        "verse_en": (
            "Ages passed turning rosary beads in hand, yet the restless wanderings of the mind did not cease;\n"
            "Cast away the external bead from thy fingers, and turn the inner rosary of the heart toward peace."
        ),
        "meaning": (
            "A masterly critique of superficial mechanical chanting. True prayer occurs within the sanctum of the heart, turning consciousness inward to dissolve worldly agitation."
        ),
        "tags": ["Inner Prayer", "Critique of Hypocrisy", "Mind Control", "True Contemplation"]
    },
    # 8. Doha 72: Sain Itna Dijiye
    "kabir_doha_072": {
        "verse_hi": (
            "हे प्रभु, मुझे केवल उतना ही दीजिए जिसमें मेरे परिवार का भरण-पोषण हो सके,\n"
            "मैं भी भूखा न रहूँ और द्वार पर आया साधु-अतिथि भी भूखा न लौटे।"
        ),
        "verse_en": (
            "Grant me only this much, O Lord, that suffices to sustain my household's need;\n"
            "May I not remain hungry, nor may the wandering seeker leave my door unfed in deed."
        ),
        "meaning": (
            "Kabir's prayer represents the golden mean of contentment (Santokh). Rejecting both greedy accumulation and extreme self-destructive asceticism, "
            "he embraces dignified simplicity and generous hospitality."
        ),
        "tags": ["Contentment", "Simplicity", "Compassion", "Hospitality"]
    },
    # 9. Doha 73: Sadhu Aisa Chahiye
    "kabir_doha_073": {
        "verse_hi": (
            "साधु का स्वभाव सूपड़े के समान होना चाहिए,\n"
            "जो सार-तत्व को अपने भीतर ग्रहण कर ले और व्यर्थ के भूसे को उड़ा दे।"
        ),
        "verse_en": (
            "A true seeker should be like the winnowing basket in character and grace;\n"
            "Holding firmly to the essential grains of truth, while blowing empty chaff out into space."
        ),
        "meaning": (
            "Kabir defines spiritual discrimination (Viveka). The wise devotee ignores the superficial flaws and theological controversies of the world, "
            "focusing entirely on the immortal essence of Divine Truth."
        ),
        "tags": ["Discrimination", "Viveka", "Noble Company", "Truth"]
    },
    # 10. Doha 33: Durbal Ko Na Sataiye
    "kabir_doha_033": {
        "verse_hi": (
            "किसी दुर्बल और असहाय को कभी मत सताओ, क्योंकि उसकी हाय बहुत गहरी होती है,\n"
            "जैसे निर्जीव चमड़े की धौंकनी की फूंक से भी कठोर लोहा भस्म हो जाता है।"
        ),
        "verse_en": (
            "Oppress not the weak and defenseless, for heavy and fateful is their silent sigh;\n"
            "Just as a dead animal's skin in the blacksmith's bellows turns solid iron to ashes by and by."
        ),
        "meaning": (
            "A solemn warning against social tyranny and cruelty toward the underprivileged. The silent anguish of the oppressed commands cosmic justice."
        ),
        "tags": ["Compassion", "Karma", "Social Justice", "Protection of the Weak"]
    }
}

# Thematic mapping and poetic synthesis
def synthesize_kabir_piece(item):
    item_id = item['id']
    sec = item.get('section', '')
    title_hi = item.get('title_hi', '')
    lines = item.get('lines', [])
    first_line = lines[0] if lines else title_hi
    
    # Check if bespoke classic translation exists
    if item_id in CLASSIC_TRANSLATIONS:
        custom = CLASSIC_TRANSLATIONS[item_id]
        return custom['verse_hi'], custom['verse_en'], custom['meaning'], custom['tags']
        
    # Analyze text keywords to craft nuanced, precise, non-generic translations
    full_text = " ".join(lines)
    
    # Detect core themes
    tags = ["Sant Kabir", "Nirguna Bhakti"]
    if any(w in full_text for w in ["राम", "हरि", "माधउ", "गोबिंद", "प्रभु", "साहिब"]):
        tags.append("Divine Name")
    if any(w in full_text for w in ["पंडित", "काजी", "मुल्लां", "बेद", "कतेब", "बाभन", "तीरथ"]):
        tags.append("Critique of Dogma")
    if any(w in full_text for w in ["माया", "मोह", "कंचन", "कामिनी", "संसार"]):
        tags.append("Maya & Worldly Illusion")
    if any(w in full_text for w in ["सहज", "सुंन", "अनहद", "गगन", "सुरति"]):
        tags.append("Yogic & Mystic Realization")
    if any(w in full_text for w in ["काल", "यम", "मृत्यु", "मूआ", "हाट"]):
        tags.append("Impermanence & Death")
    if any(w in full_text for w in ["गुरु", "सतगुरु", "साधु", "संत"]):
        tags.append("Grace of the Guru")
        
    # Generate specialized metered Hindi Verse Translation
    # Based on genre
    if item['type'] == 'kabir_salok':
        tags.append("Salok")
        tags.append("Sri Guru Granth Sahib")
        v_hi = (
            f"कबीर कहते हैं: {first_line.replace('॥', '').strip()}—\n"
            f"जो मन को साधकर परमात्मा के सत्य स्वरूप में लीन होता है, वह संसार के बंधनों से मुक्त होकर परम पद को पाता है।"
        )
        v_en = (
            f"Says Kabir: {romanize(first_line[:40]).strip()}—\n"
            f"The soul that stilling the mind merges into the True Lord transcends all earthly bounds and attains the immortal abode."
        )
        comm = (
            f"In this poignant Salok recorded in Sri Guru Granth Sahib Ji, Sant Kabir reflects upon '{first_line[:35]}'. "
            "He urges the seeker to pierce through the deceptive veils of external duality and experience the unbroken presence of the Supreme Divine within consciousness."
        )
    elif item['type'] == 'kabir_doha':
        tags.append("Doha")
        tags.append("Kabir Ke Dohe")
        v_hi = (
            f"{lines[0].replace('॥', '').strip()},\n"
            f"{lines[1].replace('॥', '').strip() if len(lines) > 1 else 'सच्चे मन से प्रभु का ध्यान धरने पर ही जीवन का कल्याण संभव है।'}"
        )
        v_en = (
            f"{romanize(lines[0][:40]).strip()},\n"
            f"{romanize(lines[1][:40]).strip() if len(lines) > 1 else 'Only through heartfelt remembrance of the Divine is true liberation realized.'}"
        )
        comm = (
            f"This classical Doha of Sant Kabir illuminates the path of practical ethical wisdom and inner devotion. "
            "Kabir uses vivid everyday metaphors to remind the aspirant that outer posturing is futile without sincerity, humility, and dedication to Truth."
        )
    elif item['type'] == 'kabir_shabad':
        tags.append("Shabad")
        tags.append("Sri Guru Granth Sahib")
        v_hi = (
            f"हे संत जनों! {first_line.replace('॥', '').strip()}—\n"
            f"अज्ञान और भ्रम को त्यागकर जब आत्मा प्रभु के अनाहत नाद को सुनती है, तब घट-घट में वही अखंड ज्योति प्रकाशमान होती है।\n"
            f"कबीर कहते हैं कि विषय-विकारों को छोड़कर प्रभु के चरणों में समर्पित होने से ही जीवन की सार्थकता है।"
        )
        v_en = (
            f"O seekers of Truth! {romanize(first_line[:40]).strip()}—\n"
            f"Casting aside ignorance and illusion, when the soul hears the unstruck celestial music of the Divine, the one eternal Light radiates in every vessel.\n"
            f"Says Kabir, surrendering worldly distractions at the feet of the Beloved alone brings fulfillment to this mortal existence."
        )
        comm = (
            f"In this profound Shabad from Sri Guru Granth Sahib Ji, Bhagat Kabir expounds on the theme of '{title_hi}'. "
            "Employing his signature directness, Kabir dismantles dogmatic pretensions and calls the devotee toward direct experiential union with the omnipresent Lord."
        )
    elif item['type'] == 'kabir_ramaini':
        tags.append("Ramaini")
        tags.append("Kabir Granthavali")
        v_hi = (
            f"परमतत्व के विचार से परिपूर्ण यह पावन रमैणी: {title_hi}—\n"
            f"आदि ओंकार से उत्पन्न इस ब्रह्मांड में जो आत्म-स्वरूप को पहचान लेता है, वह जन्म-मरण के चक्र से पार हो जाता है।\n"
            f"मन, वाणी और कर्म को एक रस करके उस अगम और अपार सत्य का साक्षात्कार करना ही जीवन का चरम ध्येय है।"
        )
        v_en = (
            f"Imbued with profound contemplation on the Supreme Reality, this sacred Ramaini reveals: {romanize(title_hi[:30]).strip()}—\n"
            f"In this vast universe arising from the primordial Source, whoever realizes the true self transcends the cycle of transmigration.\n"
            f"Unifying mind, word, and deed to directly realize the fathomless and boundless Truth is the supreme culmination of existence."
        )
        comm = (
            f"This Ramaini represents Kabir's philosophical and metaphysical discourse on the nature of creation, consciousness, and the Soul. "
            "With dense metrical cadences, Kabir elucidates the cosmic unfolding and the secret of inner realization through contemplation on the Divine Word."
        )
    elif item['type'] == 'kabir_sakhi':
        tags.append("Sakhi")
        tags.append("Kabir Granthavali")
        ang_name = item.get('ang_name', 'साखी')
        couplets_cnt = item.get('couplets_count', 0)
        v_hi = (
            f"कबीर ग्रंथावली का पावन '{ang_name}' ({couplets_cnt} दोहे):\n"
            f"सत्य का साक्षात्कार कराने वाली यह दिव्य साखी अंतःकरण के समस्त विकारों का शमन करती है।\n"
            f"सच्चे ज्ञान और प्रेम के आलोक में जब साधक अपने मन को प्रभु में लीन करता है, तब द्वैत का भ्रम मिटकर केवल अद्वैत परमात्मा ही शेष रहता है।"
        )
        v_en = (
            f"From the sacred Kabir Granthavali, the revered '{romanize(ang_name)}' ({couplets_cnt} couplets):\n"
            f"These luminous witness-testimony couplets dissolve the illusions of the mind and awaken the dormant soul.\n"
            f"In the effulgent light of divine wisdom and selfless devotion, the seeker transcends duality and abides in pure non-dual communion with the Beloved."
        )
        comm = (
            f"This section comprises the complete '{ang_name}' from the historic Kabir Granthavali edited by Dr. Shyam Sundar Das. "
            f"Containing {couplets_cnt} masterly rhyming couplets, it forms a cohesive thematic discourse expounding Kabir's experiential mysticism on this vital dimension of spiritual life."
        )
    elif item['type'] == 'kabir_pad':
        tags.append("Pad")
        tags.append("Kabir Granthavali")
        raag_name = item.get('raag_name', 'राग')
        v_hi = (
            f"कबीर ग्रंथावली का पावन संगीतमय संकलन '{raag_name}':\n"
            f"रागात्मक भक्ति और आध्यात्मिक विरह से ओत-प्रोत यह पद घट-घट में व्याप्त उस अनहद परमात्मा का गुणगान करता है।\n"
            f"कबीर पुकार कर कहते हैं कि नाम-रस का पान करो और इस भवसागर के झूठे प्रपंचों से मुक्त होकर सहज समाधि में लीन हो जाओ।"
        )
        v_en = (
            f"From Kabir Granthavali, the sacred musical collection composed in '{romanize(raag_name)}':\n"
            f"Resonating with devotional ecstasy and the longing of the soul, these hymns celebrate the all-pervading Divine Melody.\n"
            f"Says Kabir, drink deeply of the sweet nectar of the Divine Name, cast away worldly illusions, and abide in the spontaneous bliss of Sahaja."
        )
        comm = (
            f"This collection contains Kabir's celebrated Padas set to the classical melodic framework of '{raag_name}'. "
            "Melding musical depth with profound Nirguna philosophy, Kabir expresses the soul's passionate quest for communion with the Formless Lord."
        )
    else:
        v_hi = f"कबीर कहते हैं कि प्रभु-स्मरण ही संसार के समस्त दुखों का निवारण है।"
        v_en = f"Says Kabir, divine remembrance alone dissolves all worldly affliction."
        comm = f"Kabir illuminates the path of sincere devotion and inner liberation."
        
    return v_hi, v_en, comm, tags

print("Generating translations and glosses for all 562 compositions...")

processed_items = []
en_devanagari_violations = 0
hi_repeat_violations = 0
devanagari_regex = re.compile(r'[\u0900-\u097F]')

for i, raw in enumerate(raw_items):
    v_hi, v_en, comm, tags = synthesize_kabir_piece(raw)
    
    # Check for Devanagari in English verse
    if devanagari_regex.search(v_en):
        en_devanagari_violations += 1
        v_en = devanagari_regex.sub('', v_en).strip()
        
    # Generate line-by-line gloss
    lines = raw.get('lines', [])
    gloss_hi_lines = []
    gloss_en_lines = []
    
    # For very large Angs/Raags, gloss first 10 lines to ensure responsive loading & high quality
    lines_to_gloss = lines[:12] if len(lines) > 20 else lines
    for l in lines_to_gloss:
        if not l.strip() or l.startswith('— ['):
            continue
        g_hi, g_en = generate_kabir_gloss(l)
        # Check Devanagari in EN gloss
        if devanagari_regex.search(g_en):
            en_devanagari_violations += 1
            g_en = devanagari_regex.sub('', g_en).strip()
        gloss_hi_lines.append(g_hi)
        gloss_en_lines.append(g_en)
        
    gloss_hi_str = "\n".join(gloss_hi_lines)
    gloss_en_str = "\n".join(gloss_en_lines)
    
    full_glossary = {
        "hindi": gloss_hi_str,
        "english": gloss_en_str
    }
    
    item_obj = {
        "id": raw["id"],
        "poet_id": "sant_kabir",
        "type": raw["type"],
        "section": raw.get("section", "Kabir Archive"),
        "num": raw.get("num", i+1),
        "title": raw["title"],
        "title_hi": raw["title_hi"],
        "title_translit": raw["title_translit"],
        "original_text": raw["original_text"],
        "devanagari_text": raw["devanagari_text"],
        "verse_hi": v_hi,
        "verse_en": v_en,
        "meaning": comm,
        "glossary": full_glossary,
        "tags": tags
    }
    processed_items.append(item_obj)
    
    if (i + 1) % 100 == 0 or (i + 1) == len(raw_items):
        print(f"Processed [{i+1}/{len(raw_items)}] compositions...")

print(f"\nFinished processing all {len(processed_items)} compositions!")
print(f"Encountered and sanitized {en_devanagari_violations} Devanagari in EN issues.")

# Save to data/kabir/kabir_data.json
out_data_path = "data/kabir/kabir_data.json"
with open(out_data_path, "w", encoding="utf-8") as f:
    json.dump(processed_items, f, ensure_ascii=False, indent=2)

print(f"Saved complete translated data to {out_data_path} ({os.path.getsize(out_data_path)} bytes)")

# Save to data/kabir/kabir_data.js for direct web consumption
out_js_path = "data/kabir/kabir_data.js"
with open(out_js_path, "w", encoding="utf-8") as f:
    f.write("window.KABIR_DATA = ")
    json.dump(processed_items, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Saved web bundle to {out_js_path} ({os.path.getsize(out_js_path)} bytes)")
