from dataclasses import dataclass


@dataclass
class Player:
    first_name: str = ''
    last_name: str = ''
    position: str = ''
    at_bats: int = 0
    hits: int = 0

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def average(self):
        try:
            avg = self.hits / self.at_bats
            return avg
        except ZeroDivisionError:
            return 0.0


@dataclass
class Lineup:
    __player_list: list

    @property
    def count(self):
        return len(self.__player_list)

    def add_player(self, player: Player):
        self.__player_list.append(player)

    def remove_player(self, number):
        self.__player_list.pop(number - 1)

    def __iter__(self):
        for player in self.__player_list:
            yield player


def main():
    lineup = Lineup([])
    lineup.add_player(Player("Arun", "Rameshbabu", "S", 100, 100))
    lineup.add_player(Player("Buster", "Posey", "C", 4575, 1380))

    for player in lineup:
        print(f"Player: {player.full_name}")
        print(f"Batting Average: {player.average}")
        print()

    print("Done")


if __name__ == "__main__":
    main()
