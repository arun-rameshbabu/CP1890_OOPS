from encapsulation_die_class import Die, Dice


def main():
    print("The Dice Roller Program.\n")
    number_dice = int(input("Enter the number of dice to roll: "))
    dice = Dice()
    for i in range(number_dice):
        die = Die()
        dice.add_die(die)

    while True:
        dice.roll_all()
        print("YOUR ROLL: ", end='')
        for die in dice.list_dice:
            print(die.read_value(), end=' ')

        roll = input("\nRoll again? (y/n): ")
        if roll == 'n':
            print("\nBye!")
            break


if __name__ == "__main__":
    main()