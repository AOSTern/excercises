import string

def rotate(text, key):
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)
    new_text = ""
    new_key = 0
    for item in text:
        if key > 25:
            new_key = new_key + key-26
        else:
            new_key = key
        if item in string.ascii_lowercase:
            if alphabet_lower.index(item) == 13 or alphabet_lower.index(item) + new_key >= 26:
                new_key = new_key-26
            new_text = new_text + alphabet_lower[alphabet_lower.index(item)+new_key]
        if item in string.ascii_uppercase:
            if alphabet_upper.index(item) == 13 or alphabet_upper.index(item) + new_key >= 26:
                new_key = new_key-26
            new_text = new_text + alphabet_upper[alphabet_upper.index(item)+new_key]
        if item not in string.ascii_lowercase and item not in string.ascii_uppercase:
            new_text = new_text + item
    return new_text    