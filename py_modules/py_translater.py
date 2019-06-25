from googletrans import Translator
class MyTranslater:
    def TransText(self,text):
        translator = Translator()
        translation = translator.translate(text, dest='en')
        return translation.text
