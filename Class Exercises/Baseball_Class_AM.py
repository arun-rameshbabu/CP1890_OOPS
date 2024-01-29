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
