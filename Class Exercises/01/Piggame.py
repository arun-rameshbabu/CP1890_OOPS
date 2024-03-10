from Pigclass import Game



def display_welcome():
    print("Let's play PIG!\n")
    print("Game Instructions Lines \n")


def main():
    display_welcome()
    game_running = True
    while game_running:
        game = Game()
        game.play()

        choice = input("Play again? (y/n):  ")
        print()

    print("Thanks for playing!")


if __name__ == '__main__':
    main()
