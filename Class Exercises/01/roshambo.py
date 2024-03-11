from dataclasses import dataclass
import random
@dataclass
class Player:
    def __init__(self, name):
        self.name = name
        self.roshambo = None

    def generateRock(self):
        self.roshambo = "rock"

    def play(self, other_player):
        if self.roshambo == "rock" and other_player.roshambo == "scissors":
            return self
        elif self.roshambo == "scissors" and other_player.roshambo == "paper":
            return self
        elif self.roshambo == "paper" and other_player.roshambo == "rock":
            return self
        elif self.roshambo == other_player.roshambo:
            return None
        else:
            return other_player

class Bart(Player):
    def __init__(self):
        super().__init__("Bart")

class Lisa(Player):
    def __init__(self):
        super().__init__("Lisa")

    def generateRock(self):
        choices = ["rock", "paper", "scissors"]
        self.roshambo = random.choice(choices)

def main():
    player_name = input("Enter your name: ")
    user = Player(player_name)
    bart = Bart()
    lisa = Lisa()

    user.generateRock()

    print(f"{user.name} chose {user.roshambo}")
    print(f"{bart.name} chose rock")
    print(f"{lisa.name} chose {lisa.roshambo}")

    winner = user.play(bart)
    if winner:
        print(f"{winner.name} wins!")
    else:
        print("It's a tie!")

    winner = user.play(lisa)
    if winner:
        print(f"{winner.name} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
