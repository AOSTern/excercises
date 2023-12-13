import string

def is_valid(isbn):
    new_isbn = isbn.translate(str.maketrans('','','-'))
    new_isbn = list(new_isbn)
    if len(new_isbn) != 10:
        return False
    if new_isbn[-1] not in '0123456789X':
        return False
    for item in new_isbn[:-1]:
        if item not in '0123456789':
            return False
    if new_isbn[-1] == 'X':
        new_isbn [-1] = 10 
    checker = [10,9,8,7,6,5,4,3,2,1]
    new_isbn = list(map(int,new_isbn))
    multiplied = []
    for value1, value2 in zip(new_isbn,checker):
        multiplied.append(value1*value2)
    addition = sum(multiplied)
    return addition % 11 == 0