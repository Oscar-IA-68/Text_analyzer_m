import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


from analyzer.text_analyzer import (
	count_words,
	count_characters,
	count_sentences,
	longest_word,
)


def test_count_words():
	assert count_words("Hola mundo") == 2


def test_count_characters():
	assert count_characters("Hola") == 4


def test_count_sentences():
	assert count_sentences("Hola. Mundo. Otra vez.") == 3


def test_longest_word():
	assert longest_word("uno tres cinco") == "cinco"
