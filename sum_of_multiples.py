# %%
def sum_of_multiples(limit, multiples):
    list_of_multiples = []
    counter = 1
    for item in multiples:
        if item == 0:
            continue
        while item * counter < limit:
            if item * counter < limit:
                list_of_multiples.append(item * counter)
            counter += 1
        counter = 1
    return sum(set(list_of_multiples))


# %%
