from DRC import Die, Dice

def main():
    print("The Dice Roller program\n")

    # Get the input
    num_dice = int(input("Enter the number of dice to roll: "))

    dice = Dice()
    for _ in range(num_dice):
        die = Die()
        dice.add_die(die)

    choice = 'y'
    while choice.lower() == 'y':
        dice.roll_all()

        print("YOUR ROLL: ", end="")
        for die in dice.get_die_values():
            print(die, end=' ')
        print()

        choice = input("Roll again? (y/n): ")

    print("Bye!")

if __name__ == "__main__":
    main()
