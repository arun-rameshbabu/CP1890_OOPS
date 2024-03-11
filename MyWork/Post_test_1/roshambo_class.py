from dataclasses import dataclass
import random

lis = ["Rock", "Paper", "Scissors"]


class Player:
    def __init__(self, name: str):
        self.name = name
        roshambo = lis[0]
        __wins: int = 0
        __losses: int = 0

    @property
    def generateRoshambo(self):
        self.roshambo = lis[0]

    def play(self, player):
        if self.roshambo == player.roshambo:
            return None
        elif self.roshambo == "Paper" and player.roshambo == "Scissors":
            return player
        elif self.roshambo == "Scissors" and player.roshambo == "Paper":
            return self
        elif self.roshambo == "Paper" and player.roshambo == "Rock":
            return self
        elif self.roshambo == "Rock" and player.roshambo == "Paper":
            return player
        elif self.roshambo == "Scissors" and player.roshambo == "Rock":
            return player
        elif self.roshambo == "Rock" and player.roshambo == "Scissors":
            return self

    @property
    def wins(self):
        return self.__wins

    def addWin(self):
        self.__wins += 1

    def addLoss(self):
        self.__losses += 1

    def __str__(self):
        return f"{self.name}: {self.roshambo}"


@dataclass
class Bart(Player):
    def __post_init__(self):
        self.name = "Bart"


@dataclass
class Lisa(Player):
    def __post_init__(self):
        self.name = "Lisa"

    @property
    def generateRoshambo(self):
        ran = random.randint(0, 2)
        self.roshambo = lis[ran]
