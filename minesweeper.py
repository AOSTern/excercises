import string


def annotate(minefield):
    if minefield == []:
        return []
    if minefield == [""]:
        return [""]
    for items in minefield:
        for char in items:
            if char not in " *":
                raise ValueError("The board is invalid with current input.")
    values = {"*": "1", " ": "0", "b": "0"}
    values_two = {"0": " "}
    count = 0
    modified_list = []
    modified_list_two = []
    third_list = []
    last_list = []
    cluster_size = 0
    while count < (len(minefield) - 1):
        if len(minefield) == 1:
            break
        if len(minefield[count]) != len(minefield[(count + 1)]):
            raise ValueError("The board is invalid with current input.")
        count = count + 1
    cluster_size = len(minefield[count])
    minefield.insert(0, ("b" * cluster_size))
    minefield.append(("b" * cluster_size))
    minefield = [("b" + element + "b") for element in minefield]
    for element in minefield:
        element = element.translate(str.maketrans(values))
        modified_list.append(element)
    count = 1
    for element in minefield[1:-1]:
        count_two = 1
        for number in element[1:-1]:
            if number == "*":
                third_list.append(number)
                count_two = count_two + 1
                continue
            if number == " ":
                app_number = 0
                app_number = (
                    int(modified_list[(count - 1)][(count_two - 1)])
                    + int(modified_list[(count - 1)][count_two])
                    + int(modified_list[(count - 1)][(count_two + 1)])
                    + int(modified_list[count][(count_two - 1)])
                    + int(modified_list[count][count_two])
                    + int(modified_list[count][(count_two + 1)])
                    + int(modified_list[(count + 1)][(count_two - 1)])
                    + int(modified_list[(count + 1)][count_two])
                    + int(modified_list[(count + 1)][(count_two + 1)])
                )
                third_list.append(str(app_number))
            count_two = count_two + 1
        count = count + 1
    for element in third_list:
        element = element.translate(str.maketrans(values_two))
        modified_list_two.append(element)
    last_list = "".join(modified_list_two)
    return [
        last_list[i : i + cluster_size] for i in range(0, len(last_list), cluster_size)
    ]
