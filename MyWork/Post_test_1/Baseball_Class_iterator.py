from dataclasses import dataclass


@dataclass
class Player:
    first_name: str = ""
    last_name: str = ""
    position: str = ""
    atBats: int = 0
    hits: int = 0

    @property
    def fullName(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def avg(self):
        try:
            return self.hits / self.atBats
        except ZeroDivisionError:
            return 0.0

    def __str__(self):
        return f"{self.fullName:40}{self.position:6}{self.atBats:>6d}{self.hits:>8d}{self.avg:>10.3f}"


class Lineup:
    def __init__(self):
        self.__players = [Player(first_name="Tommy", last_name="La Stella", position="3B", atBats=1316, hits=360),
            Player(first_name="Mike", last_name="Yastrzemski", position="RF", atBats=563, hits=168),
            Player(first_name="Donovan", last_name="Solano", position="2B", atBats=1473, hits=407),
            Player(first_name="Buster", last_name="Posey", position="C", atBats=4575, hits=1380),
            Player(first_name="Brandon", last_name="Belt", position="1B", atBats=3811, hits=1003),
            Player(first_name="Brandon", last_name="Crawford", position="SS", atBats=4402, hits=1099),
            Player(first_name="Alex", last_name="Dickerson", position="LF", atBats=586, hits=160),
            Player(first_name="Austin", last_name="Slater", position="CF", atBats=569, hits=147),
            Player(first_name="Kevin", last_name="Gausman", position="P", atBats=56, hits=2)
        ]

    def addPlayer(self, player: Player):
        self.__players.append(player)

    def removePlayer(self, number):
        self.__players.pop(number-1)

    def movePlayer(self, player):
        pass

    def retrievePlayer(self, player):
        pass

    def edit_player(self, player):
        pass

    @property
    def player_count(self):
        return len(self.__players)

    def __iter__(self):
        for i, player in enumerate(self.__players):
            yield f"{i+1:<3d}" + str(player)
