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


class Lineup:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def move_player(self, old_index, new_index):
        self.players.insert(new_index, self.players.pop(old_index))

    def retrieve_player(self, index):
        return self.players[index]

    def edit_player(self, index, player):
        self.players[index] = player

    def number_of_players(self):
        return len(self.players)

    def __iter__(self):
        return iter(self.players)


POSITIONS = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')

def display_seperator():
    print("="*50)

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
    lineup = Lineup()

    while True:
        try:
            choice = int(input('Menu Option: '))
        except ValueError:
            choice = -1

        if choice == 1:
            display_lineup(lineup.players)
        elif choice == 2:
            add_player(lineup.players)
        elif choice == 3:
            break
        else:
            print('Invalid choice. Please try again\n')
            display_menu()


if __name__ == '__main__':
    main()
