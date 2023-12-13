def is_armstrong_number(number):
    
    l = str(number)
    b = len(l)
    x = [int(a) for a in l]
    m = 0
    d = 0
    while m < b:
        y = x[m]**b 
        m = m +1
        d = d + y
    if number == d:
        return True
    else:
        return False
