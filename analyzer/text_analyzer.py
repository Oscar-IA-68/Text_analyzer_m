def count_words(text):
    return len(text.split())

def count_characters(text):
    return len(text)

def count_sentences(text):
    sentences = text.count('.')
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)

def longest_word(text):
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)