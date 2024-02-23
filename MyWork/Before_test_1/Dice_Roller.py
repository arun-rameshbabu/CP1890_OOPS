from Dice_OB import Die, Dice


def main():
    cont = 'y'
    print("The Dice Roller program\n")

    user_input = int(input("Enter the number of dice to roll: "))
    dice = Dice()
    for i in range(user_input):
        die = Die()
        dice.addDie(die)

    while cont == 'y':
        dice.rollAll()
        print('YOUR ROLL: ', end='')
        for die in dice.list_die:
            print(die.value, end=' ')
        print('\n')
        cont = input('Roll Again? (y/n): ')


if __name__ == '__main__':
    main()
    print('Bye!')