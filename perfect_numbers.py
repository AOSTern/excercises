from functools import reduce

def factors(n):    
    return list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    l = factors(number)
    l.sort()
    b = len(l)
    m = 0
    d = 0
    while m < b-1:
        y = l[m] 
        m = m + 1
        d = d + int(y)
    if number == d:
        return "perfect"
    elif number <= d: 
        return "abundant"
    elif number >= d:
        return "deficient"