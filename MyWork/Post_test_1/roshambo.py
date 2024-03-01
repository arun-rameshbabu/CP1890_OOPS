from roshambo_class import Player, Bart, Lisa

def main():
    print("Roshambo Game")
    cont = 'y'
    name = input("\nEnter your name: ")
    vers_2 = 'h'
    while vers_2 == 'h':
        vers = input("\nWould you like to play Bart or Lisa? (b/l): ").lower()
        if vers == 'b':
            opp = Bart
            vers_2 = 'H'
        elif vers == 'l':
            opp = Lisa
            vers_2 = 'H'
        else:
            print("Invalid choice, try again.")
    
    user = Player(name=name)

    while cont.lower() == 'y':

        choice = input("\nRock, Paper, or Scissors? (r/p/s): ").lower()

        ans = rps(choice)
        user.roshambo = ans

        opp.generateRoshambo()

        print(user)
        print(opp)

        cont = input("\nPlay Again? (y/n): ").lower()
    print("Thank you for playing Roshambo")

def rps(choice):
    if choice == "r":
        return "Rock"
    elif choice == "p":
        return "Paper"
    elif choice == "s":
        return "Scissors"


if __name__ == '__main__':
    main()
