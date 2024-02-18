"""
Assignment 1

Question 1
"""

from Classes import Rectangle


def title():
    """
    Prints title of program.
    """
    print("Rectangle Calculator")
    print()


def main():
    """
    Main code for program.
    """
    title()

    loop = True

    while loop:
        rectangle = Rectangle()
                                                          # Test variables:
        print(f'Perimeter:  {rectangle.get_perimeter()}') # 10 / 5
        print(f'Area:  \t\t{rectangle.get_area()}')       # 20 / 10

        rectangle.create()

        again = input("\nContinue? (y/n): ").lower()

        if again == 'y':
            loop = True
        elif again == 'n':
            loop = False

    print("\nBye!")


if __name__ == "__main__":
    main()
