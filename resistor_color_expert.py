resistors = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]
resistance = [
    {
        "grey": 0.05,
        "violet": 0.1,
        "blue": 0.25,
        "green": 0.5,
        "brown": 1,
        "red": 2,
        "gold": 5,
        "silver": 10,
    }
]


def color_code(color):
    return resistors.index(color)


def colors():
    return resistors


def value(colors):
    number = []
    for i in colors[:2]:
        number[1:] = [str(color_code(i))]
    if (number)[0] == "0":
        return int((number)[-1])
    else:
        return int("".join(number))


def value_three(colors):
    number = []
    for i in colors[:3]:
        number[2:] = [str(color_code(i))]
    if (number)[0] == "0":
        return int((number)[-1])
    else:
        return int("".join(number))


def label(colors):
    prefix = colors.pop(2)
    number = value(colors)
    number_arithmetic = number * (10 ** (resistors.index(prefix)))
    if len(str(number_arithmetic)) <= 3:
        number_arithmetic_mod = str(number_arithmetic)
        return number_arithmetic_mod + " ohms"
    if len(str(number_arithmetic)) >= 4 < 7:
        number_arithmetic_mod = str(number_arithmetic / 1000) + " kilo"
    if len(str(number_arithmetic)) >= 7 < 10:
        number_arithmetic_mod = str(number_arithmetic / 1000000) + " mega"
    if len(str(number_arithmetic)) >= 10 < 13:
        number_arithmetic_mod = str(number_arithmetic / 1000000000) + " giga"
    if number_arithmetic_mod[1:3] == ".0":
        number_arithmetic_mod = number_arithmetic_mod[:1] + number_arithmetic_mod[3:]
    if number_arithmetic_mod[2:4] == ".0":
        number_arithmetic_mod = number_arithmetic_mod[:2] + number_arithmetic_mod[4:]
    return number_arithmetic_mod + "ohms"


def label_three(colors):
    prefix = colors.pop(3)
    number = value_three(colors)
    number_arithmetic = number * (10 ** (resistors.index(prefix)))
    if len(str(number_arithmetic)) <= 3:
        number_arithmetic_mod = str(number_arithmetic)
        return number_arithmetic_mod + " ohms"
    if len(str(number_arithmetic)) >= 4 < 7:
        number_arithmetic_mod = str(number_arithmetic / 1000) + " kilo"
    if len(str(number_arithmetic)) >= 7 < 10:
        number_arithmetic_mod = str(number_arithmetic / 1000000) + " mega"
    if len(str(number_arithmetic)) >= 10 < 13:
        number_arithmetic_mod = str(number_arithmetic / 1000000000) + " giga"
    if number_arithmetic_mod[1:3] == ".0":
        number_arithmetic_mod = number_arithmetic_mod[:1] + number_arithmetic_mod[3:]
    if number_arithmetic_mod[2:4] == ".0":
        number_arithmetic_mod = number_arithmetic_mod[:2] + number_arithmetic_mod[4:]
    return number_arithmetic_mod + "ohms"


def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"
    elif len(colors) == 4:
        result = [sub[colors[-1]] for sub in resistance]
        resistance_str = map(str, result)
        resistance_str_f = "".join(resistance_str)
        return label(colors) + " ±" + resistance_str_f + "%"
    elif len(colors) == 5:
        result = [sub[colors[-1]] for sub in resistance]
        resistance_str = map(str, result)
        resistance_str_f = "".join(resistance_str)
        return label_three(colors) + " ±" + resistance_str_f + "%"
