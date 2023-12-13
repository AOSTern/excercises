import string

def check_for_repetition(new_string,char):

    char_count =  new_string.count(char)
    return char_count

def is_isogram(string):
    new_string = string.lower()
    count = 0
    if new_string == "":
        return True
    else:
        for char in new_string:
            count = count + 1
            if char.isalnum():
                if check_for_repetition(new_string,char) >= 2:
                    return False
                if count >= len(new_string):
                    return True