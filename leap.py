def leap_year(year):
    a = 0
    b = 0
    c = 0
    if year % 4 == 0:
       a = 1
    if year % 400 == 0:
        b = 1
    if year % 100 == 0 and not year %400 == 0:
        c = 1
    if a == 1 and b == 1 and c == 0:
        return True
    elif a==1 and b == 0 and c == 1:
        return False
    elif a==1 and b == 0:
        return True
    else:
        return False