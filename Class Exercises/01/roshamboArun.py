from dataclasses import dataclass
import random

ROCHAMBO_COLL = ("rock", "paper", "scissors")
@dataclass
class Player:
    name: str = ''
    roshambo: str = ROSHAMBO_COLL[0]
    __wins:int = 0
    __losses: int=

    def generateRoshambo(self):
        self.__roshambo = ROSHAMBO_COLL[0]

    def play(self, other_player):
        if self.roshambo == other_player.roshambo:
            return None
        else:
            if (self.roshambo == 'rock' and other_player.roshambo == 'scissors') \
                or (self.roshambo == 'paper' and other_player.roshambo == 'rock') \
                    or (self.roshambo == 'scissors' and other_player.roshambo == 'paper'):
                return self
            else:
                return other_player

    @property
    def wins(self):
        return self.__wins

    def losses(self):
        return self.__losses

    def addWin(self):
        self.__wins += 1

    def addLoss(self):
        self.__losses += 1

    def __str__(self):
        return f'{self.name}: {self.roshambo}'

@dataclass
class Bart(Player):
    def __post_init__(self):
        self.name = "Bart"

@dataclass
class Lisa(Player):
    def __post_init__(self):
        self.name = "Lisa"

    def generateRoshambo(self):
        self.roshambo = random.choice(ROSHAMBO_COLL)

def main():
    print('Roshambo Game\n')
    name = input("Enter your name")
    print()

    player1 = Player(name)
    opponent = input("Opponent")
    print()

    if opponent.lower == 'b':
        player2= Bart()
    elif opponent.lower == 'l':
        player2= Lisa()

    play_again = 'y'
    while play_again.lower == 'y':
        selection = input("R P or S").lower()
        print()

        if selection =='r':
            player1.roshambo = 'rock'
        elif selection =='s':
            player1.roshambo = 'scissors'
        elif selection =='p':
            player1.roshambo = 'paper'


