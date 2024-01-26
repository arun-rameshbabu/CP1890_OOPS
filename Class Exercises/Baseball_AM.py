from Baseball_Class_AM import Player
import datetime

def title():
    print("=" * 75)
    print("\t\t\t\t\tBaseball Team Manager")

    print("CURRENT DATE: ", datetime.datetime.now().date())
    print("GAME DATE: 2024-1-30")
    print("DAYS UNTIL GAME: ", )

    print("MENU OPTIONS")
    print("1 - Display lineup\n2 - Add player\n3 - Remove player")
    print("4 - Move player\n5 - Edit player position\n6 - Edit player stats\n7 - Exit\n")
    position = "positions\nC, 1B, 2B, 3b, ss, lf, cf, rf, f"
    print(position.upper())
    print("=" * 75)


def main():
    title()


if __name__ == "__main__":
    main()
