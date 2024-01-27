# %%
numbers = {
    "     |  |   ": 1,
    " _  _||_    ": 2,
    " _  _| _|   ": 3,
    "   |_|  |   ": 4,
    " _ |_  _|   ": 5,
    " _ |_ |_|   ": 6,
    " _   |  |   ": 7,
    " _ |_||_|   ": 8,
    " _ |_| _|   ": 9,
    " _ | ||_|   ": 0,
}


def convert(input_grid):
    for item in input_grid:
        if len(item) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid) == 4:
        if len(input_grid[0]) == 3:
            return get_number(input_grid)
        return long_numbers(input_grid)
    splits = len(input_grid) // 4
    individual_strings = [[] for i in range(0, splits)]
    count = 0
    count_two = 0
    for index, items in enumerate(input_grid):
        while index + count_two < len(input_grid):
            individual_strings[count].append(input_grid[count_two : count_two + 4])
            count += 1
            count_two += 4
    composite = []
    for item in individual_strings:
        composite.append(long_numbers(item[0]))
    return ",".join(composite)


def get_number(number_grid):
    converted_seq = "".join(number_grid)
    if converted_seq not in numbers:
        return "?"
    return str(numbers.get(converted_seq))


def long_numbers(input_grid):
    for item in input_grid:
        pieces = len(item) // 3
        numbers_list = [[] for i in range(0, pieces)]

    for item in input_grid:
        count = 0
        count_two = 0
        for index, symbol in enumerate(item):
            while index + count < len(item):
                numbers_list[count_two].append(item[count : count + 3])
                count += 3
                count_two += 1

    long_number = ""
    for item in numbers_list:
        long_number = long_number + str(get_number(item))
    return long_number


# %%
