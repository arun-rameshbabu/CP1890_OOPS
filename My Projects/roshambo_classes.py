from dataclasses import dataclass
import random as r


@dataclass
class Player:
    name: str = ''
    value: str = ''
    __wins: int = 0
    __losses: int = 0

    def generate_roshambo(self):
        self.value = 'rock'
        return self.value

    def play(self, opponent):
        if opponent.value == self.value:
            return None

        elif self.value == 'rock':
            if opponent.value == 'scissors':
                return self
            elif opponent.value == 'paper':
                return opponent

        elif self.value == 'paper':
            if opponent.value == 'rock':
                return self
            elif opponent.value == 'scissors':
                return opponent

        elif self.value == 'scissors':
            if opponent.value == 'paper':
                return self
            elif opponent.value == 'rock':
                return opponent

    @property
    def wins(self):
        return self.__wins

    @property
    def losses(self):
        return self.__losses

    def add_win(self):
        self.__wins += 1

    def add_loss(self):
        self.__losses += 1

    def __str__(self):
        return f'{self.name}: {self.value}'


@dataclass
class Bart(Player):
    def __post_init__(self):
        self.name = 'Bart'


@dataclass
class Lisa(Player):
    def __post_init__(self):
        self.name = 'Lisa'

    def generate_roshambo(self):
        self.value = ['rock', 'paper', 'scissors'][r.randint(0, 2)]

