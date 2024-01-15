import string


def abbreviate(words):
    first_letters = []
    for index, letter in enumerate(words):
        if index == 0:
            first_letters.append(letter)
        if letter == " " or letter == "-" or letter == "_":
            a = index + 1
            if words[a] in string.ascii_letters:
                first_letters.append(words[a])
    acronym = "".join(first_letters)
    return acronym.upper()
