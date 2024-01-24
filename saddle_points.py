# %%
def saddle_points(matrix):
    if matrix == []:
        return []
    for item in matrix:
        if len(item) != len(matrix[0]):
            raise ValueError("irregular matrix")
    maxnum = []
    for index, item in enumerate(matrix):
        for position, number in enumerate(item):
            if number is max(item):
                maxnum.append(list((index + 1, position + 1, number)))
    minnum = []
    for index, item in enumerate(transpose(matrix)):
        for position, number in enumerate(item):
            if number is min(item):
                minnum.append(list((position + 1, index + 1, number)))
    trees = []
    for item in maxnum:
        if item in minnum:
            trees.append(item)

    answer = []
    for item in trees:
        answer.append(({"row": (item[0]), "column": (item[1])}))

    return answer


def transpose(lines):
    split_lines = lines
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
    transposed = [transposed[i] for i in range(0, maxl)]

    return transposed


# %%
