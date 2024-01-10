# %%
def append(list1, list2):
    final_list = []
    for index, item in enumerate(list1):
        final_list.insert(index, item)
    for index, item in enumerate(list2):
        final_list.insert((index + len(list1)), item)
    return final_list


def concat(lists):
    final_list = []
    for item in lists:
        final_list = append(final_list, item)
    return final_list


def filter(function, list):
    filtered_list = []
    for item in list:
        if function(item) == True:
            filtered_list.append(item)
    return filtered_list


def length(list):
    number = 0
    for index, item in enumerate(list):
        number = index
    if number == 0:
        return number
    return number + 1


def map(function, list):
    mapped_list = []
    for item in list:
        mapped_list.append(function(item))
    return mapped_list


def foldl(function, list, initial):
    reducer = initial
    for items in list:
        reducer = function(reducer, items)
    return reducer


def foldr(function, list, initial):
    reducer = initial
    list = list[::-1]
    for items in list:
        reducer = function(reducer, items)
    return reducer


def reverse(list):
    return list[::-1]


# %%
