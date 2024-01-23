# %%
class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        self.q1 = self
        self.q2 = another_queen
        if self.q1.row == self.q2.row and self.q1.column == self.q2.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        return (
            self.q1.row == self.q2.row
            or self.q1.column == self.q2.column
            or (abs(self.q1.row - self.q2.row) == abs(self.q1.column - self.q2.column))
        )


# %%
