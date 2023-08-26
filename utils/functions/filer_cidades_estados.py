from pyUFbr.baseuf import ufbr


def capitalize_words_except_prepositions(text):
    prepositions = ["do", "da", "dos", "de", "dos"]

    def capitalize_word(word):
        if word.lower() in prepositions:
            return word.lower()
        else:
            return word.capitalize()

    return " ".join(capitalize_word(word) for word in text.split())


for estado in ufbr.list_uf:
    print(
        f'"{estado}":{[capitalize_words_except_prepositions(city) for city in ufbr.list_cidades(estado)]}'
    )
