from random import randint
from dataclasses import dataclass


@dataclass
class Die:
    value: int = 1

    def roll(self):
        self.value = randint(1, 6)
    @property
    def get_value(self):
        return self.value


class Dice:
    def __init__(self):
        self.__list_die = []

    def addDie(self, die):
        self.__list_die.append(die)

    def rollAll(self):
        for die in self.__list_die:
            die.roll()

    @property
    def list_dice(self):
        return tuple(self.__list_die)
