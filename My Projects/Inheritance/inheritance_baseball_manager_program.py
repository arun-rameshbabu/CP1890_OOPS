from BB_inheritance_arun import Player, Lineup
from datetime import datetime

positions = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')
# team_list = [Player('Tommy', 'La Stella', '3B', 1316, 360),
#              Player('Mike', 'Yastrzemski', 'RF', 563, 168),
#              Player('Donovan', 'Solano', '2B', 1473, 407),
#              Player('Buster', 'Posey', 'C', 4575, 1380),
#              Player('Brandon', 'Belt', '1B', 3811, 1003),
#              Player('Brandon', 'Crawford', 'SS', 4402, 1099),
#              Player('Alex', 'Dickerson', 'LF', 586, 160),
#              Player('Austin', 'Slater', 'CF', 569, 147),
#              Player('Kevin', 'Gausman', 'P', 56, 2)]


def display_title():
    print('=' * 50)
    print('\t\t\t  Baseball Team Manager\n')
    get_game_date()
    print()
    display_menu()
    print()
    display_positions()
    print()
    print('=' * 50)


def get_game_date():
    current_date = datetime.now().date()
    print('CURRENT DATE:\t', current_date)
    game_date = datetime.fromisoformat(input('GAME DATE:\t\t ')).date()
    print(f'DAYS UNTIL GAME: {(game_date - current_date).days}')


def display_menu():
    print('MENU OPTIONS')
    print('1 - Display lineup')
    print('2 - Add player')
    print('3 - Remove player')
    print('4 - Move player')
    print('5 - Edit player position')
    print('6 - Edit player stats')
    print('7 - Exit program')


def display_positions():
    print('POSITIONS')
    for position in positions:
        print(position + ',', end=' ')


# def lineup():
#     if team_list == None:
#         print('No players in lineup')
#     else:
#         print(f"{'':3}{'Player':40}{'POS':6}{'AB':>6}{'H':>6}{'AVG':>6}")
#         print('-' * 80)
#         for i, player in enumerate(team_list):
#             print(f"{i+1:<3d}{player.full_name:40}{player.position:6}{player.atbats:6d}{player.hits:6d}{player.get_average:8.3f}")
#         print()


# def add_player():
#     first_name = input('First Name: ')
#     last_name = input('Last Name: ')
#     position = get_player_position()
#     at_bats = get_at_bats()
#     hits = get_hits(at_bats)
#
#     player = Player(first_name, last_name, position, at_bats, hits)
#     team_list.append(player)
#     print(f'Player {player.full_name} was added.')


def get_player_position():
    while True:
        position = input('Position: ').upper()
        if position in positions:
            return position
        else:
            print('Invalid position!')
            print('Valid positions are: ', display_positions())


def get_at_bats():
    while True:
        try:
            at_bats = int(input('At bats: '))
        except ValueError:
            print('Invalid Integer. Please try again.')
            continue

        if at_bats < 0 or at_bats > 9999:
            print('Invalid entry. Must be between 0 and 9999')
        else:
            return at_bats


def get_hits(at_bats):
    while True:
        try:
            hits = int(input('Hits: '))
        except ValueError:
            print('Invalid Integer. Please try again.')
            continue

        if hits < 0 or hits > at_bats:
            print(f'Invalid entry. Must be between 0 and {at_bats}')
        else:
            return hits


def main():
    lineup = Lineup([])
    display_title()
    while True:
        option = int(input('Menu option: '))
        if option == 1:
            print()
        elif option == 2:
            lineup.add_player()
        elif option == 7:
            print('Bye!')
            break


if __name__ == '__main__':
    main()
