from Baseball_Class_iterator import Player, Lineup
import datetime


def title():
    print("=" * 75)
    print("\t\t\t\t\tBaseball Team Manager")

    print("CURRENT DATE: ", datetime.datetime.now().date())
    print(f"GAME DATE: \n")  # {'2024-1-30':>13}")
    # print(f"DAYS UNTIL GAME: {'':>13}", )

    print("MENU OPTIONS")
    print("1 - Display lineup\n2 - Add player\n3 - Remove player")
    print("4 - Move player\n5 - Edit player position\n6 - Edit player stats\n7 - Exit\n")
    position = "positions\nC, 1B, 2B, 3b, ss, lf, cf, rf, f"
    print(position.upper())
    print("=" * 75)


def get_pos():
    pos_list = ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'F']
    while True:
        pos = input("Position: ").upper()
        if pos not in pos_list:
            print(f"Invalid position.\n Valid positions: {pos_list}")
        else:
            return pos


def get_at_bats():
    while True:
        try:
            at_bats = int(input("At Bats: "))
        except ValueError:
            print("Invalid integer.")
            continue

        if at_bats < 0 or at_bats > 5000:
            print("Invalid entry.")
        else:
            return at_bats


def get_hits(at_bats):
    while True:
        try:
            hits = int(input("Hits: "))
        except ValueError:
            print("Invalid integer.")
            continue

        if hits < 0 or hits > at_bats:
            print("Invalid entry.")
        else:
            return hits


def add():
    Lineup.add_player()


def player_list():
    lineup = Lineup()
    print(f"{'':3}{'Player':40}{'POS':6}{'AB':>6}{'H':>8}{'AVG':>10}")
    print("-" * 75)
    for player in lineup:
        print(player)


def main():
    title()
    menu = int(input("Menu option: "))
    while menu != 7:
        if menu == 1:
            player_list()
            menu = int(input("\nMenu option: "))
        elif menu == 2:
            add()
            menu = int(input("\nMenu option: "))
        elif menu == 3:
            num = input("Number of player to remove.")
            Lineup.removePlayer(num)
        elif menu == 7:
            break
        else:
            print("Invalid entry, please try again.")
            menu = int(input("\nMenu option: "))

    print("Bye!")


if __name__ == "__main__":
    main()
