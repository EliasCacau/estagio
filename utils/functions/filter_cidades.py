from pyUFbr.baseuf import ufbr


def capitalize_words_except_prepositions(text):
    prepositions = ["do", "da", "dos", "de", "dos"]

    def capitalize_word(word):
        if word.lower() in prepositions:
            return word.lower()
        else:
            return word.capitalize()

    return " ".join(capitalize_word(word) for word in text.split())


for i in ufbr.list_uf:
    for j in ufbr.list_cidades(i):
        capitalized_city = capitalize_words_except_prepositions(j)
        print(f'("{capitalized_city}", "{capitalized_city}"),')
