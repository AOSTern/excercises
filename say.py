# %%

first_19 = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "one hundred",
}


def hundreds(number):
    number_two = []
    if number < 101 and (number < 20 or number % 10 == 0):
        return first_19.get(number)
    if number > 20 and number < 101:
        number_two = list(str(number))
        number_two[0] = first_19.get(int(number_two[0]) * 10)
        number_two[1] = "-" + first_19.get(int(number_two[1]))
        return "".join(number_two)
    if number >= 101 and number <= 999:
        number_two = list(str(number))
        number_two[0] = first_19.get(int(number_two[0])) + " hundred"
        if number_two[1] == "0":
            number_two[1] = ""
        elif number_two[1] == "1":
            number_two[1] = " " + first_19.get(int(number_two[1] + number_two[2]))
            number_two[2] = "0"
        else:
            number_two[1] = " " + first_19.get(int(number_two[1]) * 10)
        if number_two[2] == "0":
            number_two[2] = ""
        else:
            number_two[2] = "-" + first_19.get(int(number_two[2]))
        return "".join(number_two)


def thousands(number):
    number_one = int(number / 1000)
    number_two = abs(number - number_one * 1000)
    if number_two == 000:
        return hundreds(number_one) + " thousand"
    if number_one == 000:
        return hundreds(number_two)
    return (hundreds(number_one) + " thousand " + hundreds(number_two)).strip()


def millions(number):
    number_one = int(number / 1000000)
    number_two = abs(number - number_one * 1000000)
    if number_two == 000000:
        return hundreds(number_one) + " million"
    if number_one == 000:
        return thousands(number_two)
    return (hundreds(number_one) + " million " + thousands(number_two)).strip()


def billions(number):
    number_one = int(number / 1000000000)
    number_two = abs(number - number_one * 1000000000)
    if number_two == 000000:
        return hundreds(number_one) + " billion"
    return (hundreds(number_one) + " billion " + millions(number_two)).strip()


def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    if number <= 999:
        return hundreds(number)
    if number >= 1000 and number <= 999999:
        return thousands(number)
    if number >= 1000000 and number <= 999999999:
        return millions(number)
    if number >= 1000000000 and number <= 999999999999:
        return billions(number)


# %%
