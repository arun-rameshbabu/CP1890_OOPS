from Baseball_Class_AM import Player
import datetime


def title():
    print("=" * 75)
    print("\t\t\t\t\tBaseball Team Manager")

    print("CURRENT DATE: ", datetime.datetime.now().date())
    print(f"GAME DATE: {'2024-1-30':>13}")
    print(f"DAYS UNTIL GAME: {'':>13}", )

    print("MENU OPTIONS")
    print("1 - Display lineup\n2 - Add player\n3 - Remove player")
    print("4 - Move player\n5 - Edit player position\n6 - Edit player stats\n7 - Exit\n")
    position = "positions\nC, 1B, 2B, 3b, ss, lf, cf, rf, f"
    print(position.upper())
    print("=" * 75)


def players():
    player_list = [["Tommy La Stella", "3B", 1316, 360],
                   ["Mike Yastrzemski", "RF", 536, 168],
                   ["Donovan Solano", "2B", 1473, 407]]
    return player_list

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

def option2(player_list):
    first_name = input("First name: ").title()
    last_name = input("Last name: ").title()
    position = get_pos()
    at_bats = get_at_bats()
    hits = get_hits(at_bats)

    player = Player(first_name, last_name, position, at_bats, hits)
    player_list.append(player)
    print(f"{player.fullName} was added.")


def option1(player_list):
    print(f"{'':3}{'Player':40}{'POS':6}{'AB':>6}{'AVG':>8}")
    print("-" * 75)
    for i, player in enumerate(player_list):
        print(f"{i:3d}{player.fullName:40}{player.position:6}{player.at_bats:>6d}{player.hits:>8d}")



def main():
    title()
    menu = int(input("Menu option: "))
    while menu != 7:
        if menu == 1:
            option1(players())
            menu = int(input("\nMenu option: "))
        elif menu == 2:
            option2(players())
            menu = int(input("\nMenu option: "))
        else:
            break
    print("Bye!")


if __name__ == "__main__":
    main()
