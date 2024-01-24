def transpose(lines):
    split_lines = lines.split("\n")
    maxl = len(max(split_lines, key=len))
    transposed = [[] for i in range(0, maxl)]

    split_lines = split_lines[::-1]

    for index, item in enumerate(split_lines):
        while index + 1 < len(split_lines):
            if len(split_lines[index + 1]) < len(split_lines[index]):
                split_lines[index + 1] = split_lines[index + 1] + (
                    " " * (len(split_lines[index]) - len(split_lines[index + 1]))
                )
            else:
                break

    split_lines = split_lines[::-1]

    for index, item in enumerate(split_lines):
        for index, letter in enumerate(item):
            transposed[index].append(letter)
    transposed = ["".join(transposed[i]) for i in range(0, maxl)]

    return "\n".join(transposed)
