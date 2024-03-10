import random
from dataclasses import dataclass


@dataclass
class Die:
    __value: int = 1

    def roll(self):
        self.__value = random.randint(1, 6)

    def get_value(self):
        return self.__value


class Dice:
    def __init__(self):
        self.__list_die = []

    def add_die(self, die):
        self.__list_die.append(die)

    def roll_all(self):
        for die in self.__list_die:
            die.roll()

    def get_die_values(self):
        return [die.get_value() for die in self.__list_die]