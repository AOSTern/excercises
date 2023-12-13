def is_vowel(char):
    return char.lower() in 'aeiouxy'

def is_consonant(char):
    return char.lower() in 'cdfghjklmnpqrstvwz'

def is_q(char):
    return char.lower() in 'q'

def is_y(char):
    return char.lower() in 'y'

def is_x(char):
    return char.lower() in 'x'
    
def is_u(char):
    return char.lower() in 'u'

def word_translate(word):
   
            if is_x(word[0]) == True and is_vowel(word[1]) == True:
                return word[1:]+word[0]+'ay'
            if is_y(word[0]) == True and is_vowel(word[1]) == True:
                return word[1:]+word[0]+'ay'
            if is_vowel(word[0]) == True:
                return word+'ay'
            elif is_q(word[0]) == True and is_u(word[1]) == True:
                return word[2:]+word[0:2]+'ay'
            elif is_consonant(word[0]) == True:
                if is_q(word[1]) == True:
                    return word[3:]+'squ'+'ay'
                if is_y(word[1]) == True:
                    return 'y'+word[0]+'ay'
                if is_consonant(word[1]) == True and is_consonant(word[2]) is True:
                    return word[3:]+word[0:3]+'ay'
            if is_consonant(word[1]) == True:
                return word[2:]+word[0:2]+'ay'
            return word[1:]+word[0]+'ay'

def translate(text):
    words=text.split()
    a=""
    l=0
    while l < len(words):
        a = a+word_translate(words[l])+" "
        l = l + 1
    return a.strip()