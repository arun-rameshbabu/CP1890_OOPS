from Baseball_Players import Player
from dataclasses import dataclass


@dataclass
class Player:
    firstName: str = ''
    lastName: str = ''
    position: str = ''
    atBats: int = 0
    hits: int = 0

    @property
    def fullName(self):
        return f'{self.firstName} {self.lastName}'

    @property
    def battingAvg(self) -> float:
        try:
            avg = self.hits / self.atBats
            return avg
        except ZeroDivisionError:
            return 0.0


def main():
    player1 = Player('Arun', 'Rameshbabu', 'S', 10, 10)
    print(f'Player: {player1.fullName}')
    print(f'Batting average: {player1.battingAvg}')
    print('Test complete')

POSITIONS = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')


def add_player(players):
    first_name = input('First name: ').title()
    last_name = input('Last name: ').title()
    position = get_player_positon()
    at_bats = get_at_bats()
    hits = get_hits(at_bats)

    player = Player(first_name, last_name, position, at_bats, hits)
    players.append(player)
    print(f'Player {player.fullName} was added. \n')


def get_player_positon():
    while True:
        position = input('Position: ').upper()
        if position in POSITIONS:
            return position
        else:
            print('Invalid position. Please enter correctly.')
            print('Valid positions are: ', ','.join(POSITIONS))


def get_at_bats():
    while True:
        try:
            at_bats = int(input('At bats: '))
        except ValueError:
            print('Invalid integer. Please try again')
            continue

        if at_bats < 0 or at_bats > 500:
            print('Invalid entry. Must be between 0 and 500')
        else:
            return at_bats


def get_hits(at_bats):
    while True:
        try:
            hits = int(input('Hits: '))
        except ValueError:
            print('Invalid integer. Please try again')
            continue

        if hits < 0 or hits > at_bats:
            print(f'Invalid entry. Must be between 0 and {at_bats}')
        else:
            return hits


def display_lineup(players):
    if players == None:
        print('No players in the lineup.')
    else:
        print(f"{'':3}{'Player':40}{'POS':6}{'AB':>6}{'H':>6}{'AVG':>8}")
        print('-' * 80)
        for i, player in enumerate(players, start=1):
            print(
                f'{i:<3d}{player.fullName:40}{player.position:6}{player.atBats:6d}{player.hits:6d}{player.battingAvg:8.3f}')
        print()


def display_seperator():
    print('-' * 80)


def display_title():
    print('\t\t\t\t Baseball Team Manager')


def display_menu():
    print('Menu Options:')
    print('1 - Display Lineup')
    print('2 - Add Player')
    print('3 - Exit Program')


def display_positions():
    print('POSITIONS')
    print(','.join(POSITIONS))


def main():
    display_seperator()
    display_title()
    display_menu()
    display_positions()
    display_seperator()

    players = []

    while True:
        try:
            choice = int(input('Menu Option: '))
        except ValueError:
            choice = -1

        if choice == 1:
            display_lineup(players)
        elif choice == 2:
            add_player(players)
        else:
            print('Invalid choice. Please try again\n')
            display_menu()


if __name__ == '__main__':
    main()
