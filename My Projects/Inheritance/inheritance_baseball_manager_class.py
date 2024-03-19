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
    def get_average(self):
        try:
            avg = self.hits / self.at_bats
            return avg
        except ZeroDivisionError:
            return 0.0


@dataclass
class Lineup:
    lineup_list = []
    lineup_number: int = 0

    def add_player(self):
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        position = input('Position: ')
        at_bats = int(input('At Bats: '))
        hits = int(input('Hits: '))

        new_player = Player(first_name, last_name, position, at_bats, hits)
        self.lineup_list.append(new_player)
        print(f'Player {new_player.full_name} was added.')

    def remove_player(self):
        player_number = int(input('Enter player number: '))
        removed_player = self.lineup_list.pop(player_number - 1)
        print(f'Player {removed_player.full_name} was removed.')


def main():
    lineup = Lineup()
    lineup.add_player()
    lineup.remove_player()


if __name__ == '__main__':
    main()
