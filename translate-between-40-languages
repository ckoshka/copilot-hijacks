text = "When’s she arriving?"
await get_human_translation(text=text, to="French", category="informal, conversational", use_informal=True)
# Should return "Quand qu’elle va arriver?"

text = "This symptom of omicron is related to the stomach."
await get_human_translation(text=text, to="Hindi", category="news, headline", transliterate=True)
# Should return 
{"पेट से जुड़ा है ओमिक्रॉन का ये लक्षण, दिखे तो हो जाएं सतर्क": "pet se juda hai omikron ka ye lakshan, dikhe to ho jaen satark"}

text = """Oh, tranquility!
Penetrating the very rock
A cicada’s voice."""
await get_human_translation(text=text, to="Japanese", category="poetry, haiku", prioritise_naturalness=True)
# Should return 
"""閑けさや
岩にしみいる
蝉の声"""

text = "jemandem die Daumen drücken"
await get_human_translation(text=text, to="English", category="idiom, dictionary", provide_literal_translation=True, provide_alternate_translations=True)
# Should return
{
    "literal": "give someone a thumbs up",
    "idiomatic": "to wish someone good luck"
}

text = "“我最喜欢的一天是节日？可能是圣诞节。”他说，深深地掩饰着自己的疑惑。"
await get_human_translation(text=text, to="English", category="informal, conversational", use_informal=True, instructions_to_translator="Make it sound natural", provide_phrase_table=True)
# Should return
{
    "translation": "\"My favourite day of the year? Probably Christmas.\", he said with a deep sigh.",
    "phrase_table": {
    "我最喜欢的": "My favourite",
    "一天": "day",
    "是节日": "is a holiday",
    "可能是": "possibly",
    "圣诞节": "Christmas",
    "他说": "he said",
    "深深地": "deeply",
    "掩饰着": "hid",
    "自己的": "own",
    "疑惑": "doubt"
    }
}

text = "Gmornin', how's life treatin' ya?"
await get_human_translation(text=text, to="Arabic", category="informal, conversational", transliterate=True, instructions_to_translator="make it said by a lower-class country bumpkin")
# Should return
{"صباح الورد, كيف حالك؟": "sabāh il-wird, kifalalak?"}
