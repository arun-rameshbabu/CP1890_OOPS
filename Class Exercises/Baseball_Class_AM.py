from dataclasses import dataclass


@dataclass
class Player:
    first_name: str = ""
    last_name: str = ""
    position: str = ""
    atBats: int = 0
    hits: int = 0

    def firstName(self):
        self.first_name = input("First name: ")

    def lastName(self):
        self.last_name = input("Last name: ")

    def posit(self):
        pos = ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'F']
        while True:
            userPos = input("Position: ").upper()
            if userPos in pos:
                break
            else:
                print("Invalid position, try again\nPositions: ", pos)
        self.position = userPos

    def bats(self):
        self.atBats = int(input("At Bats: "))

    def hit(self):
        self.hits = int(input("Hits: "))
