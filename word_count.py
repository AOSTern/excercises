import re


def count_words(sentence):
    sentence = sentence.casefold()
    sentence = sentence.strip("'")
    sentence = re.sub(r"\s'", " ", sentence)
    sentence = re.sub(r"'\s", " ", sentence)
    word_list = re.split(r"[ :.!&@$%^&,_\t\n]", sentence)
    word_list = list(filter(None, word_list))
    values = {}
    for word in set(word_list):
        values[word] = word_list.count(word)
    return values
