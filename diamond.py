import string


def rows(letter):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter = letter.upper()
    size_of_diamond = abc.index(letter) + 1
    diamond = []
    count = 0
    while count < size_of_diamond:
        if count == 0:
            diamond.append(
                ((" ") * (size_of_diamond - (count + 1)))
                + (abc[(count)])
                + ((" ") * ((count * 2) - 1))
                + ((" ") * (size_of_diamond - (count + 1)))
            )
        if count > 0:
            diamond.append(
                ((" ") * (size_of_diamond - (count + 1)))
                + (abc[(count)])
                + ((" ") * ((count * 2) - 1))
                + (abc[(count)])
                + ((" ") * (size_of_diamond - (count + 1)))
            )
        count = count + 1
    while count > 1:
        count = count - 1
        if count > 1:
            diamond.append(
                ((" ") * (size_of_diamond - (count)))
                + (abc[((count) - 1)])
                + ((" ") * (((count - 1) * 2) - 1))
                + (abc[((count) - 1)])
                + ((" ") * (size_of_diamond - (count)))
            )
        if count == 1:
            diamond.append(
                ((" ") * (size_of_diamond - (count)))
                + (abc[((count) - 1)])
                + ((" ") * (((count - 1) * 2) - 1))
                + ((" ") * (size_of_diamond - (count)))
            )
    return diamond
