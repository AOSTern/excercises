# %%
import secrets


class Robot:
    def __init__(self):
        self.name = []
        while len(self.name) < 2:
            self.name.append(secrets.choice(r"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        while len(self.name) < 5:
            self.name.append(str(secrets.choice(range(0, 9, 1))))
        self.name = "".join(self.name)

    def reset(self):
        self.name = []
        while len(self.name) < 2:
            self.name.append(secrets.choice(r"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        while len(self.name) < 5:
            self.name.append(str(secrets.choice(range(0, 9, 1))))
        self.name = "".join(self.name)


# %%
