

def lang_translate(text,language):
	from googletrans import Translator, LANGUAGES
	if language in LANGUAGES.values():
		translator = Translator()
		result = translator.translate(text, src='en', dest=language)
		return result
	else:
		return "None"