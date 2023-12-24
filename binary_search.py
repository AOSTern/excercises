# %%
def find(search_list, value):
    if value not in search_list or search_list == []:
        raise ValueError("value not in array")
    for index, values in enumerate(search_list):
        if value == values:
            return index


# %%
