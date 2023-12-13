import math

def score(x, y):
    if math.sqrt(x**2+y**2) <= 1:
        return 10
    elif math.sqrt(x**2+y**2) <= 5:
        return 5
    elif math.sqrt(x**2+y**2) <= 10:
        return 1
    return 0 