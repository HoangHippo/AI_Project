

def lang_translate(text,language):
	from googletrans import Translator, LANGUAGES
	if language in LANGUAGES.values():
		translator = Translator()
		result = translator.translate(text, src='vi', dest=language)
		return result.text
	else:
		return "None"