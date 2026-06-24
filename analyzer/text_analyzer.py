def count_words(text):
    return len(text.split())

def count_characters(text):
    return len(text)

def count_sentences(text):
    return sum(1 for sentence in text.split('.') if sentence.strip())

def longest_word(text):
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)