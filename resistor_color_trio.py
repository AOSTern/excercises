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
prefixes = [
    " ",
    "0 ",
    "00 ",
    " kilo",
    "0 kilo",
    "00 kilo",
    " mega",
    "0 mega",
    "00 mega",
    " giga",
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


def label(colors):
    prefix = colors.pop(2)
    number = value(colors)
    if number in [10, 20, 30, 40, 50, 60, 70, 80]:
        return str(number)[0] + prefixes[resistors.index("orange")] + "ohms"
    return str(number) + prefixes[resistors.index(prefix)] + "ohms"
