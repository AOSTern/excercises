import re


class Luhn:
    def __init__(self, card_num):
        Luhn.card_num = re.sub(r" ", "", card_num)

    def valid(self):
        if self.card_num.isdigit() == False:
            return False
        result = 0
        intermediate = 0
        self.card_num = self.card_num[::-1]
        for index, digit in enumerate(self.card_num):
            if index % 2 == 0:
                result += int(digit)
            if index % 2 != 0:
                intermediate = int(digit) * 2
                if intermediate > 9:
                    intermediate -= 9
                result += intermediate
                intermediate = 0
        if result == 0 and len(self.card_num) <= 1:
            return False
        return result % 10 == 0
