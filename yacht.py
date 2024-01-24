# %%
# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 35
FOUR_OF_A_KIND = 40
LITTLE_STRAIGHT = 30
BIG_STRAIGHT = 31
CHOICE = 0

import statistics


def score(dice, category):
    if category is ONES or TWOS or THREES or FOURS or FIVES or SIXES:
        values = []
        for roll in dice:
            if roll == category:
                values.append(roll)
    if category is YACHT:
        for roll in dice:
            if roll != int(statistics.mean(dice)):
                return 0
            values = [1]
    if category is LITTLE_STRAIGHT:
        values = []
        for roll in dice:
            if roll == 6:
                return 0
            values.append(roll)
        if len(set(values)) < 5:
            return 0
        return category
    if category is BIG_STRAIGHT:
        values = []
        for roll in dice:
            if roll == 1:
                return 0
            values.append(roll)
        if len(set(values)) < 5:
            return 0
        return category - 1
    if category is CHOICE:
        return sum(dice)
    if category is FOUR_OF_A_KIND:
        values = []
        for roll in dice:
            values.append(roll)
        if len(set(values)) > 2:
            return 0
        values.sort()
        if values.count(values[0]) >= 4:
            return int(category / 10 * values[0])
        if values.count(values[-1]) == 4:
            return int(category / 10 * values[-1])
        else:
            return 0
    if category is FULL_HOUSE:
        values = []
        for roll in dice:
            values.append(roll)
        if len(set(values)) > 2:
            return 0
        values.sort()
        if values.count(values[0]) == 3:
            return sum(values)
        if values.count(values[-1]) == 3:
            return sum(values)
        else:
            return 0

    return len(values) * category


# %%
