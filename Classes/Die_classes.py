import random
from dataclasses import dataclass


@dataclass
class Dice(object):
    def __init__(self, die6= 1, die5= 1, die4= 1, die3= 1, die2=1, die1=1):
        self.dice = random.randint(1,6)

        die = [die1,die2,die3,die4,die5,die6]
        __dievalue : int = random.randint(1,6)
        random.shuffle()
        self.roll = random.randint(1,6)