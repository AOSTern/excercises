def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base <2:
        raise ValueError("output base must be >= 2")
    for i in digits:
        if i >= input_base or i < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    count = 0
    digits_in_base_10 = []
    reversed_digits = digits[::-1]
    output = []
    for i in reversed_digits:
        digits_in_base_10[count:] = [(i*pow(input_base,count)),]
        count = count + 1
    number_in_base_10 = sum(digits_in_base_10)
    count=-1
    while number_in_base_10 >= output_base:
        output[:count] = [(number_in_base_10 % output_base)]
        number_in_base_10 = number_in_base_10 // output_base
        count = count - 1
    output[:count] = [(number_in_base_10)]
    return output