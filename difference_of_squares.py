# %%
def square_of_sum(number):
    counter = 0
    counter_two = 1
    while counter_two <= number:
        counter = counter + counter_two
        counter_two += 1
    return counter**2


def sum_of_squares(number):
    counter = 0
    counter_two = 1
    while counter_two <= number:
        counter = counter + counter_two**2
        counter_two += 1
    return counter


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)


# %%
