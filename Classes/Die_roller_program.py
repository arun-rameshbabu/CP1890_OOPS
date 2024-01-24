import random
from Die_classes import Dice

def roll_dice():
    return random.randint(1,6)

def roll_all():
    singledie = random.randint(1,6)

    return singledie * 6

def main():
        print("The Dice Roller Program")
        print()
        choice = input("Enter the number of dice to roll: ")
        while True:
            if choice == "1":
                print("YOUR ROLL:")
                print(f"{roll_dice()}")
            elif choice == "2":
                print("YOUR ROLL:")
                print(f"{roll_dice()},{roll_dice()}")
            elif choice == "3":
                print("YOUR ROLL:")
                print(f"{roll_dice()},{roll_dice()},{roll_dice()}")
            elif choice == "4":
                print("YOUR ROLL:")
                print(f"{roll_dice()},{roll_dice()},{roll_dice()},{roll_dice()}")
            elif choice == "5":
                print("YOUR ROLL:")
                print(f"{roll_dice()},{roll_dice()},{roll_dice()},{roll_dice()},{roll_dice()}")
            elif choice == "6":

                print("YOUR ROLL:")
                print(f"{roll_dice()},{roll_dice()},{roll_dice()},{roll_dice()},{roll_dice()},{roll_dice()}")

            rg = input("Do you want to roll again? (y/n): ")
            if rg.lower() == "y":
                continue
            else:
                print()
                print("Bye!")
                break


if __name__ == '__main__':
    main()