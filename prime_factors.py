import math


def factors(value):
    primes = []
    count = 2
    while value > math.prod(primes):
        while value % count == 0:
            value = value / count
            primes.append(count)
            if value % count != 0:
                count += 1
        if value % count != 0:
            count += 1
    if value != 1:
        primes.append(int(value))
    return primes
