from dataclasses import dataclass
import random as r


class Dice:
    def __init__(self):
        self.list_dice = []

    def add_die(self, die):
        self.list_dice.append(die)

    def roll_all(self):
        for die in self.list_dice:
            die.roll()


@dataclass
class Die:
    value: int = 0

    def roll(self):
        self.value = r.randint(1, 6)
        return self.value
