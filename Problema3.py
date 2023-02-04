# Equipe: Alanna Gilcielle Mesquita de Farias e Maria Graziela Brito de Souza

verb_suffixes = {"en", "o", "os", "a", "om", "ons", "am", "ei", "es", "e", "em", "est", "im", "ai", "ais", "i", "aem", "aist", "aim"}

tenses = {"presente", "pretérito", "futuro"}

conjugation = {
    "presente": {"1a pessoa": "o", "2a pessoa": "os", "3a pessoa": "a",
                 "4a pessoa": "om", "5a pessoa": "ons", "6a pessoa": "am"},
    "futuro": {"1a pessoa": "ai", "2a pessoa": "ais", "3a pessoa": "i",
               "4a pessoa": "aem", "5a pessoa": "aist", "6a pessoa": "aim"},
    "pretérito": {"1a pessoa": "ei", "2a pessoa": "es", "3a pessoa": "e",
                  "4a pessoa": "em", "5a pessoa": "est", "6a pessoa": "im"}

}


def analyze_verb(word):
    for suffix in verb_suffixes:
        if word.endswith(suffix):
            verb = word[:-len(suffix)]
            for tense, persons in conjugation.items():
                for person, suffixes in persons.items():
                    if word.endswith(suffixes):
                        end_of_word = verb.rstrip('en')
                        if end_of_word[-1] == 'a':
                            end = end_of_word[:-1]
                            return f"{word} - {end}en, {person}, {tense}"
                        else:
                            return f"{word} - {verb}en, {person}, {tense}"
            return f"{word} {verb}en: Verbo regular"
    else:
        return f"{word}: não é um tempo verbal"


words = input("Insira uma lista de palavras: ").strip().split("\n")
for word in words:
    print(analyze_verb(word))
