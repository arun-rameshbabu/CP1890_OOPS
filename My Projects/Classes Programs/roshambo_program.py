from roshambo_classes import Player, Bart, Lisa


def main():
    print("\nRoshambo Game")

    name = str(input("\nEnter your name: "))
    player1 = Player(name)

    opponent = str(input("\nWould you like to play Bart or Lisa? (b/l): ")).lower()

    if opponent == "b":
        player2 = Bart()
    elif opponent == "l":
        player2 = Lisa()

    while True:
        player2.generate_roshambo()

        attack = str(input("\nRock, Paper, or Scissors? (r/p/s): ")).lower()
        if attack == 'r':
            player1.value = 'rock'
        elif attack == 'p':
            player1.value = 'paper'
        elif attack == 's':
            player1.value = 'scissors'

        print(player1)
        print(player2)

        winner = player1.play(player2)
        if winner is None:
            print('Draw!\n')
        else:
            print(f'{winner.name} wins!\n')
            winner.add_win()
            if winner is player1:
                player2.add_loss()
            else:
                player1.add_loss()

        print(f'{player1.name}: {player1.wins} total wins, {player1.losses} total losses')
        print(f'{player2.name}: {player2.wins} total wins, {player2.losses} total losses')

        loop = input("\nPlay again? (y/n): ")
        if loop == 'n':
            print("\nBye!")
            break


if __name__ == "__main__":
    main()
