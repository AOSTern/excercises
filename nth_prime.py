from itertools import islice, count

def is_prime(n):
    return not any(n % k == 0 for k in range(2, int(n ** 0.5) + 1))

def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    gen = islice(filter(is_prime, count(2)), number)
    for _ in range(number - 1): next(gen)
    return next(gen)