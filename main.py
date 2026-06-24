from analyzer.text_analyzer import (
	count_words,
	count_characters,
	count_sentences,
	longest_word,
)

text = "Hola. Mundo. Otra vez."

print("Número de palabras:", count_words(text))
print("Número de caracteres:", count_characters(text))
print("Número de oraciones:", count_sentences(text))
print("Palabra más larga:", longest_word(text))

