from Dice_encapsule_AM import Die, Dice

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
        for die in dice.read_list:
            print(die.getValue, end=' ')
        print('\n')
        cont = input('Roll Again? (y/n): ')
    print('Bye!')

if __name__ == '__main__':
    main()
