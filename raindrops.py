def convert(number):
    a=""
    b=""
    c=""
    if number %3 != 0 and number %5 != 0 and number %7 != 0:
        return str(number)
    else:
        if number % 3 == 0:
            a="Pling"
        if number % 5 == 0:
            b="Plang"
        if number % 7 == 0:
            c="Plong"
        return (a+b+c)