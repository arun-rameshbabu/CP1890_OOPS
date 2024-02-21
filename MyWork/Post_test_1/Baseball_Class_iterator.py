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


class Lineup:
    def __init__(self):
        self.players = [
            Player(first_name="Tommy", last_name="La Stella", position="3B", atBats=1316, hits=360),
            Player(first_name="Mike", last_name="Yastrzemski", position="RF", atBats=563, hits=168),
            Player(first_name="Donovan", last_name="Solano", position="2B", atBats=1473, hits=407),
            Player(first_name="", last_name="", position="", atBats=, hits=),
            Player(first_name="", last_name="", position="", atBats=, hits=),
            Player(first_name="", last_name="", position="", atBats=, hits=),
            Player(first_name="", last_name="", position="", atBats=, hits=)
        ]