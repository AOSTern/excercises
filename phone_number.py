import re


class PhoneNumber:
    def __init__(self, number):
        self.number = self.validate(number)
        self.area_code = self.number[0:3]

    def validate(self, number):
        number = re.sub(r"[+-. \(\)]", "", number)
        if len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(number) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(number) == 11:
            if number[0] == "1":
                number = number[1:]
            else:
                raise ValueError("11 digits must start with 1")
        if number[0] == "0":
            raise ValueError("area code cannot start with zero")
        if number[0] == "1":
            raise ValueError("area code cannot start with one")
        if number[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if number[3] == "1":
            raise ValueError("exchange code cannot start with one")
        for i in number:
            if i.isalpha() == True:
                raise ValueError("letters not permitted")
        if number.isdigit() == False:
            raise ValueError("punctuations not permitted")
        return number

    def pretty(self):
        return "(" + self.number[0:3] + ")-" + self.number[3:6] + "-" + self.number[6:]
