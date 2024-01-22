from dataclasses import dataclass
import random as r


class Dice:
    def __init__(self):
        self.__list_dice = []

    def list_die(self):
        return self.__list_dice

    def add_die(self, die):
        self.__list_dice.append(die)

    def roll_all(self):
        for die in self.__list_dice:
            die.roll()


class Die:
    def __init__(self):
        self.__value: int = 0

    def read_value(self):
        return self.__value

    def roll(self):
        self.__value = r.randint(1, 6)
        return self.__value
