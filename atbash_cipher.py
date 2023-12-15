import string

forward = []
reverse = []
letters = "abcdefghijklmnopqrstuvwxyz"
for letter in letters:
    forward.append(letter)
reverse = forward[::-1]


def encode(plain_text):
    plain_text = plain_text.replace(" ", "")
    plain_text = plain_text.lower()
    plain_text = plain_text.translate(str.maketrans("", "", string.punctuation))
    plaintext = " ".join([plain_text[i : i + 5] for i in range(0, len(plain_text), 5)])
    coded = ""
    for letter in plaintext:
        if letter in forward:
            index_spot = forward.index(letter)
            coded = coded + (reverse[index_spot])
        if letter not in forward:
            coded = coded + letter
    return coded


def decode(ciphered_text):
    plaintext = ciphered_text.replace(" ", "")
    coded = ""
    for letter in plaintext:
        if letter in reverse:
            index_spot = reverse.index(letter)
            coded = coded + (forward[index_spot])
        if letter not in reverse:
            coded = coded + letter
    return coded
