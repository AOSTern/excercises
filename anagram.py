# %%
def letter_comp(word, word_two):
    for letter in word:
        if word.count(letter) != word_two.count(letter):
            return False
        return True


def find_anagrams(word, candidates):
    word = word.casefold()
    candidates_two = []
    indexes = []
    indexes_two = []
    indexes_three = []
    count = 0
    for element in candidates:
        candidates_two.append(element.casefold())
    enumerate(candidates_two)
    for element in enumerate(candidates_two):
        if len(word) > len(element[1]):
            indexes.append(element[0])
        elif len(word) < len(element[1]):
            indexes.append(element[0])
        elif element[1] == word:
            indexes.append(element[0])
        else:
            continue
        count = count + 1
    indexes = indexes[::-1]
    for i in indexes:
        del candidates[i]
        del candidates_two[i]
    for words in enumerate(candidates_two):
        if set(words[1]) != set(word):
            indexes_two.append(words[0])
    indexes_two = indexes_two[::-1]
    for i in indexes_two:
        del candidates[i]
        del candidates_two[i]
    for words in enumerate(candidates_two):
        if letter_comp(words[1], word) == False:
            indexes_three.append(words[0])
    indexes_three = indexes_three[::-1]
    for i in indexes_three:
        del candidates[i]
        del candidates_two[i]
    return candidates


# %%
