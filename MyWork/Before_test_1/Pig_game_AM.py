from Pig_game_encap import Game


def title_desc():
    print("Let's play PIG!\n\n"
          "* See how many turns it takes you to get 20.\n"
          "* Turn ends when you hold or roll 1.\n"
          "* If you roll a 1, you lose all points for the turn.\n"
          "* If you hold, you save all points for the turn.\n")


def main():
    title_desc()
    choice = 'y'
    while choice.lower() == 'y':
        game = Game()
        game.play()

        choice = input("Play again? (y/n): ").lower()
        print()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
