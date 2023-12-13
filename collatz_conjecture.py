def steps(number):
    
    if number >= 1 and int: 
    
        a=0
        number=int(number)
        while number != 1:
            a=a+1
            if number % 2 == 0: 
                number = number/2
            else: 
                number = (3*number)+1
        return a
    else:
        raise ValueError('Only positive integers are allowed')
