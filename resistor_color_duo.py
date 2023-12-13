resistors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def color_code(color):
    
    return resistors.index(color)

def colors():
    
    return resistors

def value(colors):
    number = []
    for i in colors[:2]:
        number[1:] = [str(color_code(i))]
    if (number)[0] == '0':
        return int((number)[-1])
    else:
        return int("".join(number))