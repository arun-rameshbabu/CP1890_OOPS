from dataclasses import dataclass
import random


@dataclass
class Die:
    __value: int = 1

    def getValue(self):
        return self.__value

    def roll(self):
        self.__value = random.randint(1, 6)

class Dice:
    def __init__(self):
        self.__list_die = []

    def read_list(self):
        return self.__list_die

    def addDie(self, die):
        self.__list_die.append(die)

    def rollAll(self):
        for die in self.__list_die:
            die.roll()
