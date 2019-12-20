from random import choice
from googletrans import Translator, LANGCODES



def get_fdiedb():
    translator = Translator()
    language = choice(list(LANGCODES.keys()))
    print(language)
    result = translator.translate("fick die deutsche Bahn", dest=language)
    return language + ": "+ result.text


# for testing
if __name__ == '__main__':
    print(get_fdiedb())