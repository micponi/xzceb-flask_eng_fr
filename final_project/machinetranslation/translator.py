"""Translation between English-French-English"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Translation from English to French"""
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """Translation from French to English"""
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text



# print(english_to_french("hello"))
# print(french_to_english("bonjour!"))
