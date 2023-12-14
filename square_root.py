def square_root(number):
    root_bajo = 1
    root_alto = 2
    count = 0
    while root_bajo * root_bajo <= number:
        if root_bajo * root_bajo == number:
            return root_bajo
        root_bajo = root_bajo + 1
        root_alto = root_alto + 1
    root_alto = root_alto - 1
    root_bajo = root_bajo - 1
    while count < 50 and root_alto * root_alto > number:
        root_alto = (number / root_alto + root_alto) / 2
        count = count + 1
    return root_alto
