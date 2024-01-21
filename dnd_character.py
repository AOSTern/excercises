import secrets
import math


class Character:
    def __init__(self):
        self.strength = diceroll()
        self.dexterity = diceroll()
        self.constitution = diceroll()
        self.intelligence = diceroll()
        self.wisdom = diceroll()
        self.charisma = diceroll()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return diceroll()


def diceroll():
    rolls = []
    while len(rolls) < 4:
        rolls.append(secrets.choice([1, 2, 3, 4, 5, 6]))
    for roll in rolls:
        if roll == min(rolls):
            rolls.remove(roll)
            break
    return sum(rolls)


def modifier(number):
    if number < 10 and number % 2 != 0:
        number = number - 1
    return math.trunc((number - 10) / 2)
